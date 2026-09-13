"""Record model → API JSON: index rows and full record dicts."""
from __future__ import annotations

import re
from pathlib import Path

from .types import VALID_ATTRS, infer_type, schema_for
from .vault import EMBED_RE, LINK_RE, ParsedFile, Vault, clean_target

TAG_RE = re.compile(r"#\S+")

GRANTS_SECTION_RE = re.compile(r"grants( by stage)?", re.I)

DRAFT_RE = re.compile(r"^draft:\s*true\s*$", re.M | re.I)


def _is_draft(p: ParsedFile) -> bool:
    return bool(p.frontmatter and DRAFT_RE.search(p.frontmatter))


def _tags(value: str | None) -> list[str]:
    if not value:
        return []
    return [t for t in value.split() if t.startswith("#")]


def _attrs(value: str | None) -> list[str]:
    if not value or value.strip() == "-":
        return []
    parts = [p.strip() for p in re.split(r"[/,]", value) if p.strip() and p.strip() != "-"]
    return parts


def record_row(vault: Vault, rel: str) -> dict:
    p = vault.get(rel)
    type_, subtype = infer_type(rel)
    schema = schema_for(type_)
    grants = p.grants()

    def val(name: str) -> str:
        f = p.field(name)
        return f.value if f else ""

    cols = {}
    for name in schema["tableColumns"]:
        if name == "Grants":
            cols[name] = len(grants["embeds"]) if grants else 0
        elif name == "Prerequisites":
            cols[name] = val("Prerequisites")
        else:
            cols[name] = val(name)

    return {
        "path": rel,
        "stem": Path(rel).stem,
        "name": Path(rel).stem,
        "type": type_,
        "subtype": subtype,
        "folder": rel.rsplit("/", 1)[0] if "/" in rel else "",
        "columns": cols,
        "requirements": val("Requirements"),
        "attributes": val("Attributes"),
        "cost": val("Cost"),
        "apCost": val("AP Cost"),
        "tier": val("Tier"),
        "tags": _tags(val("Tags")) + _tags(val("Traits")),
        "attrCodes": _attrs(val("Attributes")),
        "hasEmbeds": bool(EMBED_RE.search(p.text)),
        "grantCount": len(grants["embeds"]) if grants else 0,
        "leveled": "Variable" in (val("Cost") or ""),
    }


def _section_dict(p: ParsedFile, s) -> dict:
    body = p.text[s.body_start:s.end]
    return {
        "title": s.title,
        "level": s.level,
        "line": s.heading.line_no if hasattr(s.heading, "line_no") else None,
        "body": body,
        "embeds": [clean_target(m.group(1)) for m in EMBED_RE.finditer(body)],
        "links": [clean_target(m.group(1)) for m in LINK_RE.finditer(body)],
    }


def _section_for_line(p: ParsedFile, line_start: int) -> str | None:
    for s in p.sections:
        if s.heading.start <= line_start < s.end:
            return s.title
    return None


def record_full(vault: Vault, rel: str) -> dict:
    p = vault.get(rel)
    type_, subtype = infer_type(rel)
    schema = schema_for(type_)
    grants = p.grants()

    header_fields = {}
    for f in p.fields:
        if f.in_header_block:
            header_fields[f.name] = f.value
    loose_fields = {f.name: f.value for f in p.fields if not f.in_header_block}

    return {
        "path": rel,
        "stem": Path(rel).stem,
        "type": type_,
        "subtype": subtype,
        "folder": rel.rsplit("/", 1)[0] if "/" in rel else "",
        "draft": _is_draft(p),
        "schema": schema,
        "headerFields": header_fields,
        "looseFields": loose_fields,
        "fields": [{"name": f.name, "value": f.value, "line": f.line_no,
                    "inHeader": f.in_header_block,
                    "inSection": _section_for_line(p, f.line.start)} for f in p.fields],
        "intro": p.intro,
        "sections": [_section_dict(p, s) for s in p.sections],
        "grants": grants,
        "embeds": [clean_target(m.group(1)) for m in EMBED_RE.finditer(p.text)],
        "links": [clean_target(m.group(1)) for m in LINK_RE.finditer(p.text)],
        "attrCodesValid": all(a in VALID_ATTRS for a in _attrs(p.field_value("Attributes"))),
    }


def index_rows(vault: Vault) -> list[dict]:
    return [record_row(vault, rel) for rel in vault.scan()]


def full_text_search(vault: Vault, query: str, rels: list[str] | None = None) -> list[str]:
    """Case-insensitive substring search over file text; returns matching rels."""
    q = query.lower()
    out = []
    for rel in (rels if rels is not None else vault.scan()):
        if q in vault.get(rel).text.lower():
            out.append(rel)
    return out
