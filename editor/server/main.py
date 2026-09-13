"""Exceed Vault Editor — local FastAPI server.

Binds to 127.0.0.1 only. Serves the SPA from editor/web/dist and the JSON
API under /api (which doubles as the machine surface for AI tooling /
parsers: everything the UI does goes through it).
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import session, refactor
from .checks import issues_for_record, run_checks
from .records import index_rows, record_full, record_row
from .scaffolds import SCAFFOLDS, scaffold_meta
from .serialize import Edits, apply_edits
from .types import (CATEGORY_TAGS, HEADER_FIELDS, MECHANIC_TAGS, PERK_TAGS,
                    SPELL_TAGS, VALID_ATTRS, infer_type, schema_for)
from .vault import Vault, clean_target

app = FastAPI(title="Exceed Vault Editor", version="0.1.0")
vault = Vault()

WEB_DIST = Path(__file__).resolve().parents[1] / "web" / "dist"


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _checked_rel(path: str) -> str:
    path = path.replace("\\", "/").lstrip("/")
    if not vault.is_inside(path):
        raise HTTPException(404, "file not found (or outside source/content)")
    return path


def _fail_on_write_guard(rel: str) -> None:
    """Writes are restricted to non-hidden .md files under source/content/."""
    try:
        resolved = vault.abs_path(rel)
        rel_parts = resolved.relative_to(vault.root.resolve()).parts
    except ValueError:
        raise HTTPException(400, "writes are restricted to source/content/**/*.md")
    if resolved.suffix != ".md" or any(p.startswith(".") for p in rel_parts):
        raise HTTPException(400, "writes are restricted to source/content/**/*.md")


# ─────────────────────────────────────────────────────────────────────────────
# Meta / index
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/api/meta")
def meta() -> dict:
    folders: dict[str, list[str]] = {}
    for rel in vault.scan():
        folder = rel.rsplit("/", 1)[0] if "/" in rel else ""
        folders.setdefault(folder, None)
    perk_folders = sorted({f for f in folders if f.startswith("Perks/") and "UNEDITED" not in f})
    spell_folders = sorted({f for f in folders if f.startswith("Spells/")})
    rule_folders = sorted({f for f in folders if f.startswith("Rules/")})
    action_folders = sorted({f for f in folders if f.startswith("Actions/")})
    return {
        "attributeCodes": VALID_ATTRS,
        "categoryTags": CATEGORY_TAGS,
        "tagVocab": {"perk": PERK_TAGS, "mechanic": MECHANIC_TAGS, "spell": SPELL_TAGS},
        "headerFields": HEADER_FIELDS,
        "folders": {
            "perks": perk_folders, "spells": spell_folders,
            "rules": rule_folders, "actions": action_folders,
            "all": sorted(folders),
        },
        "scaffolds": scaffold_meta(),
        "typeCounts": _type_counts(),
    }


def _type_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for rel in vault.scan():
        t, _ = infer_type(rel)
        counts[t] = counts.get(t, 0) + 1
    return counts


@app.get("/api/index")
def api_index(type: str | None = None, q: str | None = None,
              fullText: bool = False) -> list[dict]:
    rows = index_rows(vault)
    if type:
        wanted = {t.strip() for t in type.split(",")}
        rows = [r for r in rows if r["type"] in wanted]
    if q:
        query = q.lower()
        if fullText:
            hits = set()
            for rel in vault.scan():
                if query in vault.get(rel).text.lower():
                    hits.add(rel)
            rows = [r for r in rows if r["path"] in hits or query in r["stem"].lower()
                    or query in (r.get("requirements") or "").lower()]
        else:
            rows = [r for r in rows
                    if query in r["stem"].lower()
                    or query in (r.get("requirements") or "").lower()
                    or any(query in c.lower() for c in r["columns"].values() if isinstance(c, str))]
    return rows


@app.get("/api/record")
def api_record(path: str) -> dict:
    rel = _checked_rel(path)
    rec = record_full(vault, rel)
    try:
        rec["issues"] = issues_for_record(vault, rel)
    except Exception as e:  # checker must never break the record view
        rec["issues"] = [{"severity": "low", "label": f"checks unavailable: {e}", "detail": ""}]
    return rec


@app.get("/api/raw")
def api_raw(path: str) -> dict:
    rel = _checked_rel(path)
    return {"path": rel, "text": vault.read_text(rel)}


# ─────────────────────────────────────────────────────────────────────────────
# Save (surgical)
# ─────────────────────────────────────────────────────────────────────────────

class SaveBody(BaseModel):
    path: str
    headerFields: dict[str, str] = {}
    looseFields: dict[str, str] = {}
    sectionBodies: dict[str, str] = {}
    grants: dict | None = None
    intro: str | None = None
    draft: bool | None = None


@app.put("/api/record")
def api_save(body: SaveBody) -> dict:
    rel = _checked_rel(body.path)
    _fail_on_write_guard(rel)

    parsed = vault.get(rel)
    before = parsed.text
    edits = Edits(header_fields=body.headerFields, loose_fields=body.looseFields,
                  section_bodies=body.sectionBodies, grants=body.grants,
                  intro=body.intro, draft=body.draft)
    try:
        after = apply_edits(parsed, edits)
    except ValueError as e:
        raise HTTPException(400, str(e))

    if after != before:
        vault.invalidate(rel)
        vault.write_text(rel, after)
        session.record_write(rel, "edited")
    run_checks(vault)  # refresh cache

    saved = record_full(vault, rel)
    try:
        saved["issues"] = issues_for_record(vault, rel)
    except Exception:
        saved["issues"] = []
    saved["changed"] = after != before
    return saved


# ─────────────────────────────────────────────────────────────────────────────
# Create / rename / delete
# ─────────────────────────────────────────────────────────────────────────────

class CreateBody(BaseModel):
    scaffold: str
    name: str
    folder: str


@app.post("/api/create")
def api_create(body: CreateBody) -> dict:
    scaffold = SCAFFOLDS.get(body.scaffold)
    if not scaffold:
        raise HTTPException(400, f"unknown scaffold '{body.scaffold}'")
    name = body.name.strip()
    prefix = scaffold.get("namePrefix", "")
    if prefix and not name.startswith(prefix):
        name = prefix + name
    if not name or "/" in name or "\\" in name:
        raise HTTPException(400, "invalid name")
    folder = body.folder.strip().strip("/")
    rel = f"{folder}/{name}.md" if folder else f"{name}.md"
    _fail_on_write_guard(rel)
    if vault.abs_path(rel).exists():
        raise HTTPException(400, f"file already exists: {rel}")
    for other in vault.scan():
        if Path(other).stem == name:
            raise HTTPException(
                400, f"duplicate stem: '{name}' already exists at {other} "
                     f"(filenames are global identifiers)")

    content = scaffold["template"]
    vault.write_text(rel, content)
    session.record_write(rel, "created")
    run_checks(vault)
    rec = record_full(vault, rel)
    try:
        rec["issues"] = issues_for_record(vault, rel)
    except Exception:
        rec["issues"] = []
    return rec


class RenameBody(BaseModel):
    path: str
    newName: str | None = None
    newFolder: str | None = None
    apply: bool = False


@app.post("/api/rename")
def api_rename(body: RenameBody) -> dict:
    rel = _checked_rel(body.path)
    try:
        plan = refactor.plan_rename(vault, rel, body.newName, body.newFolder)
    except ValueError as e:
        raise HTTPException(400, str(e))
    if not body.apply:
        return {"preview": True, **plan}
    _fail_on_write_guard(plan["to"])
    result = refactor.apply_rename(vault, plan)
    session.record_write(rel, "renamed")
    session.record_write(plan["to"], "renamed-to")
    for f in result["rewrittenFiles"]:
        session.record_write(f, "links-rewritten")
    run_checks(vault)
    return {"preview": False, **plan, "result": result}


class DeleteBody(BaseModel):
    path: str
    apply: bool = False


@app.post("/api/delete")
def api_delete(body: DeleteBody) -> dict:
    rel = _checked_rel(body.path)
    plan = refactor.plan_delete(vault, rel)
    if not body.apply:
        return {"preview": True, **plan}
    _fail_on_write_guard(rel)
    result = refactor.apply_delete(vault, rel)
    session.record_write(rel, "deleted")
    run_checks(vault)
    return {"preview": False, **plan, "result": result}


# ─────────────────────────────────────────────────────────────────────────────
# Checks / refs / session / selftest
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/api/checks")
def api_checks(force: bool = False) -> dict:
    return run_checks(vault, force=force)


@app.get("/api/refs")
def api_refs(stem: str) -> dict:
    """Reverse deps: who embeds / links / requires / prereqs this stem."""
    from .vault import EMBED_RE, LINK_RE
    embedders, linkers, requirers, prereqs = [], [], [], []
    target_stem = stem.strip()
    for rel in vault.scan():
        if Path(rel).stem == target_stem:
            continue
        parsed = vault.get(rel)
        for m in EMBED_RE.finditer(parsed.text):
            if clean_target(m.group(1)) == target_stem:
                embedders.append(rel)
                break
        for m in LINK_RE.finditer(parsed.text):
            if clean_target(m.group(1)) == target_stem:
                linkers.append(rel)
                break
        req = parsed.field_value("Requirements") or ""
        if f"[[{target_stem}]]" in req:
            requirers.append(rel)
        pre = parsed.field_value("Prerequisites") or ""
        if f"[[{target_stem}]]" in pre:
            prereqs.append(rel)
    return {"stem": target_stem, "embedders": sorted(set(embedders)),
            "linkers": sorted(set(linkers) - set(embedders)),
            "requirers": sorted(set(requirers)),
            "prerequisites": sorted(set(prereqs))}


@app.get("/api/tree")
def api_tree(stem: str) -> dict:
    """Requirement/prerequisite chain upward from a record."""
    # find the record for this stem
    start = None
    for rel in vault.scan():
        if Path(rel).stem == stem:
            start = rel
            break
    if start is None:
        raise HTTPException(404, f"no file with stem '{stem}'")

    def node_for(rel: str, field: str, depth: int, seen: set) -> dict:
        parsed = vault.get(rel)
        children = []
        if depth < 20 and rel not in seen:
            seen = seen | {rel}
            value = parsed.field_value(field) or ""
            for m in re.finditer(r"\[\[([^\]|#]+?)(?:[#|][^\]]*)?\]\]", value):
                target = clean_target(m.group(1))
                resolved = vault.resolve_stem(target)
                if resolved and resolved != rel:
                    child_field = "Prerequisites" if field == "Prerequisites" else "Requirements"
                    children.append(node_for(resolved, child_field, depth + 1, seen))
        return {"path": rel, "name": Path(rel).stem,
                "type": infer_type(rel)[0], "children": children}

    parsed = vault.get(start)
    field = "Prerequisites" if parsed.field_value("Prerequisites") is not None else "Requirements"
    return {"root": Path(start).stem, "field": field, "tree": node_for(start, field, 0, set())}


@app.get("/api/read")
def api_read(path: str) -> dict:
    """Content + resolved embeds for the reader/zoom view."""
    from .records import _is_draft
    from .vault import EMBED_RE, clean_target
    rel = _checked_rel(path)
    parsed = vault.get(rel)
    embeds = []
    for m in EMBED_RE.finditer(parsed.text):
        target = clean_target(m.group(1))
        resolved = vault.resolve_stem(target)
        embeds.append({"target": target, "path": resolved,
                       "name": Path(resolved).stem if resolved else target})
    return {"path": rel, "name": Path(rel).stem, "draft": _is_draft(parsed),
            "content": parsed.text, "embeds": embeds}


@app.get("/api/resolve")
def api_resolve(stem: str) -> str:
    """Stem → vault-relative path (the wikilink resolution the editor uses)."""
    rel = vault.resolve_stem(stem)
    if rel is None:
        raise HTTPException(404, f"no file with stem '{stem}'")
    return rel


@app.get("/api/rulebook")
def api_rulebook() -> dict:
    """The rules reading tree, derived from Rulebook/chapter page embeds."""
    from .rulebook import rulebook_tree
    return rulebook_tree(vault)


@app.get("/api/session")
def api_session() -> dict:
    return {"writes": session.session_writes(), "gitStatus": session.git_status()}


@app.get("/api/diff")
def api_diff(path: str) -> dict:
    rel = _checked_rel(path)
    return {"path": rel, "diff": session.git_diff_for(rel)}


@app.get("/api/selftest")
def api_selftest() -> dict:
    """Round-trip proof over the whole vault: parse->reassemble == original."""
    from .selfcheck import reassemble
    fails = []
    for rel in vault.scan():
        parsed = vault.get(rel)
        try:
            if reassemble(parsed) != parsed.text:
                fails.append(rel)
        except Exception as e:
            fails.append(f"{rel} ({e})")
    return {"files": len(vault.scan()), "failures": fails[:50],
            "ok": not fails}


# ─────────────────────────────────────────────────────────────────────────────
# Static SPA
# ─────────────────────────────────────────────────────────────────────────────

if WEB_DIST.exists():
    app.mount("/assets", StaticFiles(directory=WEB_DIST / "assets"), name="assets")

    @app.get("/")
    def spa_root() -> FileResponse:
        return FileResponse(WEB_DIST / "index.html")

    @app.get("/{full_path:path}")
    def spa_catchall(full_path: str) -> Any:
        candidate = WEB_DIST / full_path
        if full_path and candidate.is_file() and WEB_DIST in candidate.resolve().parents:
            return FileResponse(candidate)
        return FileResponse(WEB_DIST / "index.html")
else:
    @app.get("/")
    def no_frontend() -> JSONResponse:
        return JSONResponse({
            "message": "frontend not built yet — run `npm install && npm run build` in editor/web",
            "api": "/api/meta"})
