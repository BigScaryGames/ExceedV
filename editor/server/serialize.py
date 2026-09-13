"""Surgical, lossless serialization.

All edits are expressed as splices (start, end, replacement) over the
ORIGINAL file text. Anything not covered by a splice is preserved
byte-for-byte. The only wholesale regeneration is the leading header
field block (auto-normalize on save, per agreed semantics) and sections
explicitly edited (Grants, text sections, intro body).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field as dc_field

from .types import HEADER_FIELDS, infer_type, schema_for
from .vault import BOM, EMBED_RE, ParsedFile


@dataclass
class Edits:
    header_fields: dict[str, str] = dc_field(default_factory=dict)   # canonical header values ("" = remove)
    loose_fields: dict[str, str] = dc_field(default_factory=dict)    # field lines outside the header block
    section_bodies: dict[str, "str | None"] = dc_field(default_factory=dict)  # title-lower -> new body; None = remove section
    section_renames: dict[str, str] = dc_field(default_factory=dict)  # title-lower -> new title
    grants: dict | None = None                                       # {"mode": "simple"|"staged", ...}
    intro: str | None = None                                         # replace intro region
    draft: bool | None = None                                        # True/False sets draft frontmatter
    rename_stem: str | None = None                                   # informational, used by API layer


def _norm_body(body: str, eol: str) -> str:
    return body.replace("\r\n", "\n").replace("\n", eol)


def _canonical_grants_body(grants: dict, eol: str) -> tuple[str, str]:
    """(title, body) for the Grants section, canonical formatting."""
    if grants.get("mode") == "staged":
        lines = []
        for stage_no in sorted(grants.get("stages", {}), key=int):
            embeds = grants["stages"][stage_no]
            joined = " + ".join(f"![[{t}]]" for t in embeds)
            lines.append(f"- **Stage {stage_no}:** {joined}")
        body = "\n".join(lines) + eol if lines else eol
        return "Grants by Stage", body
    embeds = grants.get("embeds", [])
    body = eol + eol.join(f"![[{t}]]" for t in embeds) + eol if embeds else eol
    return "Grants", body


def _field_line(name: str, value: str) -> str:
    return f"**{name}:** {value}"


def build_splices(parsed: ParsedFile, edits: Edits) -> list[tuple[int, int, str]]:
    text = parsed.text
    eol = parsed.eol
    splices: list[tuple[int, int, str]] = []
    type_, _ = infer_type(parsed.rel)

    # ---- 0. draft frontmatter toggle ---------------------------------------
    if edits.draft is not None:
        fm = parsed.frontmatter
        if edits.draft:
            if fm is None:
                splices.append((0, 0, "---\ndraft: true\n---\n"))
            elif re.search(r"^draft:", fm, re.M):
                new_fm = re.sub(r"^draft:.*$", "draft: true", fm, flags=re.M)
                if new_fm != fm:
                    splices.append((0, len(fm), new_fm))
            else:
                new_fm = fm.replace("---" + eol, "---" + eol + "draft: true" + eol, 1)
                splices.append((0, len(fm), new_fm))
        elif fm is not None and re.search(r"^draft:", fm, re.M):
            new_fm = re.sub(r"^draft:.*\n", "", fm, flags=re.M)
            remaining = [l for l in new_fm.splitlines() if l.strip() and l.strip() != "---"]
            if not remaining:
                new_fm = ""  # frontmatter held nothing but the draft flag
            splices.append((0, len(fm), new_fm))

    # ---- 1. header block regeneration ------------------------------------
    if edits.header_fields:
        provided = {k.strip(): v for k, v in edits.header_fields.items()}
        existing = {}
        for f in parsed.fields:
            if f.in_header_block:
                existing.setdefault(f.name.strip(), f.value)

        canonical = HEADER_FIELDS.get(type_) or [f["name"] for f in schema_for(type_)["fields"]]
        final: list[tuple[str, str]] = []
        used = set()
        for name in canonical:
            if name in provided or name in existing:
                value = provided.get(name, existing.get(name, "-"))
                if value == "" and name in provided and name in existing:
                    continue  # clearing an existing field removes its line
                final.append((name, value if value not in ("", None) else "-"))
                used.add(name)
        for name in existing:  # unknown/legacy block fields are preserved
            if name not in used:
                if name in provided and provided[name] == "":
                    continue
                final.append((name, provided.get(name, existing[name])))
        # names the schema doesn't know and the file doesn't have yet
        # ("+ Add field") join the end of an EXISTING header block; body-first
        # files keep their loose-field convention (no block gets created).
        # Fields inside a section whose body this same save rewrites don't
        # count as "already exists" — the rewrite replaces that region, so a
        # header_fields entry is the field's new home (section→header move).
        replaced_spans = []
        for title in edits.section_bodies:
            sec = parsed.section(title)
            if sec is not None:
                replaced_spans.append((sec.heading.start, sec.end))

        def _region_replaced(line_start: int) -> bool:
            return any(s <= line_start < e for s, e in replaced_spans)

        parsed_ci = {f.name.strip().lower() for f in parsed.fields
                     if f.in_header_block or not _region_replaced(f.line.start)}
        in_final = {n for n, _ in final}
        new_items = [(n, "-" if v == "" else v) for n, v in provided.items()
                     if n not in in_final and n not in canonical and n.lower() not in parsed_ci]
        if parsed.header_block:
            final.extend(new_items)

        if not final:
            pass  # nothing belongs in the header block for this edit
        else:
            # "" on an existing field removes its line; the remaining fields
            # keep their lines and order — blank-line grouping inside the
            # block (e.g. Trigger/Effect vs Tags) is deliberate layout and
            # survives the edit; freshly added fields fold into the last kept
            # line's splice so nothing else moves
            removed = {n for n in existing if provided.get(n) == ""}
            kept_names = [n for n in existing if n not in removed]
            final_names = [n for n, _ in final]
            if parsed.header_block and (kept_names or not new_items) \
                    and final_names[:len(kept_names)] == kept_names:
                by_name = {n: v for n, v in final}
                block_fields = [f for f in parsed.fields if f.in_header_block]
                by_field = {}
                for f in block_fields:
                    by_field.setdefault(f.name.strip(), f)
                for name in removed:
                    f = by_field.get(name)
                    if f is not None:
                        splices.append((f.line.start, f.line.end_with_eol, ""))
                kept_fields = [f for f in block_fields if f.name.strip() not in removed]
                tail = final[len(kept_names):]
                last = kept_fields[-1] if kept_fields else None
                for f in kept_fields:
                    if tail and f is last:
                        continue
                    new_line = _field_line(f.name, by_name[f.name.strip()])
                    if new_line != f.raw:
                        splices.append((f.line.start, f.line.end, new_line))
                if tail and last is not None:
                    folded = _field_line(last.name, by_name[last.name.strip()])
                    folded += eol + eol.join(_field_line(n, v) for n, v in tail)
                    splices.append((last.line.start, last.line.end, folded))
            elif parsed.header_block:
                block_text = eol.join(_field_line(n, v) for n, v in final)
                s, e = parsed.header_block
                splices.append((s, e, block_text))
            else:
                # insert a new header block at the top (after frontmatter)
                block_text = eol.join(_field_line(n, v) for n, v in final)
                ins = parsed.intro_start
                following = text[ins:parsed.intro_end] if parsed.intro_end > ins else ""
                sep = eol + eol if following.strip() else eol
                splices.append((ins, ins, block_text + sep))

    # ---- 2. loose field lines (outside the header block) ------------------
    for raw_name, value in edits.loose_fields.items():
        name = raw_name.strip()
        target = None
        for f in parsed.fields:
            if not f.in_header_block and f.name.strip().lower() == name.lower():
                target = f
                break
        if target is not None:
            if value == "":
                # "" removes the whole line (including its EOL); if the line
                # is last and its removal leaves a trailing blank, eat that too
                s, e = target.line.start, target.line.end_with_eol
                if e >= len(text) and text[:s].endswith(eol + eol):
                    s -= len(eol)
                splices.append((s, e, ""))
            else:
                splices.append((target.line.start, target.line.end,
                                _field_line(target.name, value)))
        else:
            # new field line: prefer inserting just before a trailing
            # Tags/Traits line (abilities/actions keep meta fields above
            # their tags); otherwise append at end of file
            body_fields = [f for f in parsed.fields if not f.in_header_block]
            anchor = None
            if body_fields and body_fields[-1].name.strip().lower() in ("tags", "traits"):
                anchor = body_fields[-1]
            if anchor is not None:
                before = text[:anchor.line.start]
                prefix = eol if before and not before.endswith(eol + eol) else ""
                splices.append((anchor.line.start, anchor.line.start,
                                prefix + _field_line(name, value) + eol))
            else:
                add = ("" if text.endswith(eol) else eol)
                add += eol + _field_line(name, value) + eol
                splices.append((len(text), len(text), add))

    # ---- 3. section bodies -------------------------------------------------
    for title, body in edits.section_bodies.items():
        sec = parsed.section(title)
        if sec is None:
            if body is None:
                continue  # removing a section that doesn't exist
            # append a new section at the end
            add = eol if text.endswith(eol) else ""
            add += eol + f"## {title}" + eol + _norm_body(body, eol)
            splices.append((len(text), len(text), add))
            continue
        if body is None:
            # remove the whole section (heading + body); the blank line above
            # the heading stays, so the neighbours keep single-line separation
            splices.append((sec.heading.start, sec.end, ""))
            continue
        new_body = _norm_body(body, eol)
        old_body = text[sec.body_start:sec.end]
        if sec.end < len(text) and not new_body.endswith(eol):
            new_body += eol
        if sec.end == len(text) and old_body.endswith(eol) and not new_body.endswith(eol):
            new_body += eol
        splices.append((sec.body_start, sec.end, new_body))

    # ---- 3b. section renames (heading line only) ---------------------------
    for title, new_title in edits.section_renames.items():
        sec = parsed.section(title)
        if sec is None:
            continue
        new_heading = f"{'#' * sec.level} {new_title}"
        if new_heading != sec.heading.content:
            splices.append((sec.heading.start, sec.heading.end, new_heading))

    # ---- 4. grants section regeneration ------------------------------------
    if edits.grants is not None:
        grants = dict(edits.grants)
        # normalize embed targets to strings
        if grants.get("mode") == "simple":
            grants["embeds"] = [str(t) for t in grants.get("embeds", [])]
        else:
            grants["stages"] = {int(k): [str(t) for t in v]
                                for k, v in grants.get("stages", {}).items()}
        title, body = _canonical_grants_body(grants, eol)

        sec = None
        for s in parsed.sections:
            if s.title.strip().lower() in ("grants", "grants by stage"):
                sec = s
                break
        if sec is not None:
            replacement = f"## {title}" + eol + body
            if sec.end < len(text) and not replacement.endswith(eol + eol):
                replacement += eol  # keep a blank line before the next heading
            splices.append((sec.heading.start, sec.end, replacement))
        else:
            # insert before Description if present, else append
            desc = parsed.section("Description")
            if desc is not None:
                splices.append((desc.heading.start, desc.heading.start,
                                f"## {title}" + eol + body + eol))
            else:
                add = eol if text.endswith(eol) else ""
                add += eol + f"## {title}" + eol + body
                splices.append((len(text), len(text), add))

    # ---- 5. intro body ------------------------------------------------------
    if edits.intro is not None:
        new_intro = _norm_body(edits.intro, eol)
        old = text[parsed.intro_start:parsed.intro_end]
        if old.endswith(eol) and not new_intro.endswith(eol) and parsed.intro_end < len(text):
            new_intro += eol
        splices.append((parsed.intro_start, parsed.intro_end, new_intro))

    # Loose field lines can live inside a section body (a spell's Duration /
    # Prerequisites used to sit inside ## Description) or inside the intro
    # region (ability **Tags:** at end of body-first files). When the user
    # edited that containing region as text, the region edit wins and the
    # structured field edit within it is dropped.
    regions = [(s, e) for (s, e, rep) in splices if rep and e > s]
    kept: list[tuple[int, int, str]] = []
    for sp in splices:
        s0, e0, _ = sp
        if any(s1 <= s0 and e0 <= e1 and (s1, e1) != (s0, e0) for (s1, e1) in regions):
            continue
        kept.append(sp)
    splices = kept

    # sanity: splices must not overlap
    splices.sort(key=lambda s: (s[0], s[1]))
    for i in range(1, len(splices)):
        if splices[i][0] < splices[i - 1][1]:
            raise ValueError(f"overlapping splices at {splices[i-1][:2]} / {splices[i][:2]}")
    return splices


def apply_edits(parsed: ParsedFile, edits: Edits) -> str:
    """Original text + splices (applied tail-first) -> new full text.

    Re-adds the BOM if the original file had one."""
    text = parsed.text
    splices = build_splices(parsed, edits)
    for s, e, rep in sorted(splices, key=lambda x: -x[0]):
        text = text[:s] + rep + text[e:]
    return (BOM if parsed.bom else "") + text
