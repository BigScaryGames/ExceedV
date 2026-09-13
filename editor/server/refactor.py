"""Refactor flows: rename/move with vault-wide wikilink rewrite, and delete.

Rewrites only the *target* portion of each [[X]] / ![[X]] occurrence;
aliases, embed markers and surrounding text are preserved.
"""
from __future__ import annotations

import re
from pathlib import Path

from .vault import Vault

# [[target]] with optional #heading, |alias or \|escaped-alias suffix
LINK_ANY_RE = re.compile(r"(!?)\[\[([^\[\]]*)\]\]")


def _rewrite_target(target: str, old_stem: str, old_rel: str,
                    new_stem: str, new_rel: str) -> str | None:
    """New target text if this link points at the renamed file, else None."""
    raw = target
    # split off heading part and escaped pipe suffixes
    body = raw
    suffix = ""
    if "#" in body:
        body, _, heading = body.partition("#")
        suffix = "#" + heading
    # escaped pipe alias: "Aid\|Aid" -> target "Aid", alias "\|Aid"
    alias = ""
    if "\\" + "|" in body:
        body, _, alias_rest = body.partition("\\|")
        alias = "\\|" + alias_rest
    elif "|" in body:
        body, _, alias_rest = body.partition("|")
        alias = "|" + alias_rest

    clean = body.strip().rstrip("\\").strip()
    norm = clean.replace("\\", "/")
    if norm.endswith(".md"):
        norm = norm[:-3]

    is_match = False
    if norm == old_stem:
        is_match = True
    elif norm == old_rel[:-3]:  # path-style link to the old file
        is_match = True
    if not is_match:
        return None

    # If the link was path-style, keep it path-style (updated); bare stays bare.
    if "/" in norm:
        new_target = new_rel[:-3]
    else:
        new_target = new_stem
    return new_target + suffix + alias


def plan_rename(vault: Vault, rel: str, new_name: str | None = None,
                new_folder: str | None = None) -> dict:
    """Preview every change a rename/move would make. Nothing is written."""
    old_path = Path(rel)
    old_stem = old_path.stem
    new_stem = (new_name or old_stem).strip()
    new_folder = (new_folder if new_folder is not None else str(old_path.parent))
    if new_folder == ".":
        new_folder = ""
    new_rel = f"{new_folder}/{new_stem}.md" if new_folder else f"{new_stem}.md"

    if new_stem != old_stem and not new_stem:
        raise ValueError("new name is empty")
    if "/" in new_stem or "\\" in new_stem:
        raise ValueError("name must not contain path separators")

    # duplicate stem check against the whole vault (excluding self)
    for other, paths in vault.stem_index().items():
        for p in paths:
            if p != rel and Path(p).stem == new_stem:
                raise ValueError(f"a file named '{new_stem}' already exists: {p}")
    if vault.abs_path(new_rel).exists() and new_rel != rel:
        raise ValueError(f"target file already exists: {new_rel}")

    changes: list[dict] = []
    for other_rel in vault.scan():
        if other_rel == rel:
            continue
        parsed = vault.get(other_rel)
        for m in LINK_ANY_RE.finditer(parsed.text):
            new_target = _rewrite_target(m.group(2), old_stem, rel, new_stem, new_rel)
            if new_target is None or new_target == m.group(2):
                continue
            before = m.group(0)
            after = f"{m.group(1)}[[{new_target}]]"
            line_no = parsed.text.count("\n", 0, m.start()) + 1
            changes.append({"file": other_rel, "line": line_no,
                            "before": before, "after": after})

    return {
        "from": rel,
        "to": new_rel,
        "stemChanged": new_stem != old_stem,
        "folderChanged": new_folder != (str(old_path.parent) if str(old_path.parent) != "." else ""),
        "referenceChanges": changes,
    }


def apply_rename(vault: Vault, plan: dict) -> dict:
    """Apply a rename plan: rewrite references, then move the file."""
    rel, new_rel = plan["from"], plan["to"]
    old_stem, new_stem = Path(rel).stem, Path(new_rel).stem
    rewritten: set[str] = set()

    # rewrite references file by file (each file's offsets come from its own
    # fresh parse, so replacements never interfere)
    for other_rel in vault.scan():
        if other_rel == rel:
            continue
        parsed = vault.get(other_rel)
        replacements: list[tuple[int, str, str]] = []
        for m in LINK_ANY_RE.finditer(parsed.text):
            nt = _rewrite_target(m.group(2), old_stem, rel, new_stem, new_rel)
            if nt is None:
                continue
            before = m.group(0)
            after = f"{m.group(1)}[[{nt}]]"
            if before != after:
                replacements.append((m.start(), before, after))
        if not replacements:
            continue
        text = parsed.text
        for start, before, after in sorted(replacements, key=lambda r: -r[0]):
            assert text[start:start + len(before)] == before
            text = text[:start] + after + text[start + len(before):]
        vault.invalidate(other_rel)
        vault.write_text(other_rel, text)
        rewritten.add(other_rel)

    # move the file itself
    if new_rel != rel:
        src = vault.abs_path(rel)
        dst = vault.abs_path(new_rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            raise ValueError(f"target file already exists: {new_rel}")
        src.rename(dst)
        vault.invalidate(rel)

    return {"renamed": rel, "to": new_rel, "rewrittenFiles": sorted(rewritten)}


def plan_delete(vault: Vault, rel: str) -> dict:
    """Inbound references to a file about to be deleted."""
    stem = Path(rel).stem
    inbound: list[dict] = []
    for other_rel in vault.scan():
        if other_rel == rel:
            continue
        parsed = vault.get(other_rel)
        for m in LINK_ANY_RE.finditer(parsed.text):
            target = m.group(2)
            body = target.split("#")[0].split("|")[0]
            body = body.strip().rstrip("\\").strip()
            norm = body.replace("\\", "/")
            if norm.endswith(".md"):
                norm = norm[:-3]
            if norm == stem or norm == rel[:-3]:
                line_no = parsed.text.count("\n", 0, m.start()) + 1
                inbound.append({"file": other_rel, "line": line_no,
                                "reference": m.group(0)})
    return {"file": rel, "inboundReferences": inbound}


def apply_delete(vault: Vault, rel: str) -> dict:
    vault.invalidate(rel)
    vault.abs_path(rel).unlink()
    return {"deleted": rel}
