"""Validation: runs tools/consistency_check.py (imported, never reimplemented)
plus a small set of editor-specific extras.
"""
from __future__ import annotations

import importlib.util
import re
import sys
import threading
from pathlib import Path

from .types import ATTR_TYPOS
from .vault import Vault, parse_text

REPO_ROOT = Path(__file__).resolve().parents[2]

_checker = None
_checker_lock = threading.Lock()


def checker():
    """Import tools/consistency_check.py as a module (stdlib only)."""
    global _checker
    with _checker_lock:
        if _checker is None:
            spec = importlib.util.spec_from_file_location(
                "exceed_consistency_check", REPO_ROOT / "tools" / "consistency_check.py")
            mod = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = mod
            spec.loader.exec_module(mod)
            _checker = mod
        return _checker


# Spell files no longer have Basic/Advanced version sections (magic revamp
# removed them); the checker's rule is stale. We keep parity with the checker
# but label it so the UI can present it honestly.
STALE_CHECKS = {"no Basic/Advanced version sections"}

_checker_path = REPO_ROOT / "tools" / "consistency_check.py"


def checker_stamp() -> float:
    """Mtime of the checker source — editing it invalidates cached results."""
    try:
        return _checker_path.stat().st_mtime_ns
    except OSError:
        return 0.0


_cache_lock = threading.Lock()
_cache: dict = {"key": None, "results": None}

# Files exempt from content-validity checks: conventions docs (their broken
# embeds are intentional examples) and draft-marked files (WIP by definition).
EXEMPT_FILENAMES = {"claude.md", "claude_reference.md"}


def _exempt_reasons(vault: Vault, rels: list[str]) -> dict[str, str]:
    import re as _re
    from pathlib import Path as _Path
    reasons: dict[str, str] = {}
    for rel in rels:
        if _Path(rel).name.lower() in EXEMPT_FILENAMES:
            reasons[rel] = "conventions doc"
            continue
        parsed = vault.get(rel)
        if parsed.frontmatter and _re.search(r"^draft:\s*true\s*$", parsed.frontmatter, _re.M | _re.I):
            reasons[rel] = "draft"
    return reasons


def _filter_exempt(vault: Vault, results: dict) -> dict:
    rels = vault.scan()
    exempt = _exempt_reasons(vault, rels)
    if not exempt:
        return results

    def keep_file(rel: str) -> bool:
        return rel not in exempt

    for key in ("legacy", "brokenEmbeds", "brokenLinks", "deprecatedRefs",
                "perkViolations", "spellViolations", "deprecatedAttr"):
        results[key] = [h for h in results[key] if keep_file(h["file"])]
    results["editorExtras"] = [h for h in results["editorExtras"]
                               if keep_file(h["file"]) and not any(
                                   p in exempt for p in h.get("paths", []))]
    results["exemptFiles"] = {rel: reason for rel, reason in sorted(exempt.items())}
    return results


def run_checks(vault: Vault, force: bool = False) -> dict:
    """Full vault consistency run + editor extras. Cached by (file set, mtimes, checker stamp)."""
    rels = vault.scan()
    key = tuple(
        [(rel, vault.abs_path(rel).stat().st_mtime_ns) for rel in rels]
        + [("checker", checker_stamp())]
    )
    with _cache_lock:
        if not force and _cache["key"] == key:
            return _cache["results"]

    cc = checker()
    cc.ROOT = str(vault.root.resolve())  # short() paths must match our rels
    files = [str(vault.abs_path(rel)) for rel in rels]
    contents = {p: cc.read(p) for p in files}

    be, bl, dr = cc.check_links(files, contents)
    results = {
        "fileCount": len(files),
        "legacy": cc.check_legacy(files, contents),
        "brokenEmbeds": be,
        "brokenLinks": bl,
        "deprecatedRefs": dr,
        "duplicates": cc.check_duplicates(files),
        "perkViolations": cc.check_perks(files, contents),
        "spellViolations": cc.check_spells(files, contents),
        "deprecatedAttr": cc.check_deprecated_refs(files, contents),
        "staleChecks": sorted(STALE_CHECKS),
        "editorExtras": editor_extras(vault, rels),
    }

    with _cache_lock:
        _cache["key"] = key
        _cache["results"] = results
    return _filter_exempt(vault, results)


QUIRK_PATTERNS = [
    (re.compile(r"^\d\*\*"), "header line has stray characters before the field"),
    (re.compile(r"\bWI\b"), "attribute typo: WI (should be WT)"),
    (re.compile(r"\bMG\s*\d"), "attribute requirement without space (MG2 -> MG 2)"),
]


def editor_extras(vault: Vault, rels: list[str]) -> list[dict]:
    """Editor-specific issues the pipeline checker doesn't cover."""
    issues: list[dict] = []

    # duplicate stems (checker reports duplicate *filenames*, same thing, but
    # we also flag empty duplicate stubs explicitly)
    from collections import defaultdict
    by_stem = defaultdict(list)
    for rel in rels:
        by_stem[Path(rel).stem].append(rel)
    for stem, paths in by_stem.items():
        if len(paths) > 1:
            empties = [p for p in paths if vault.abs_path(p).stat().st_size == 0]
            label = "duplicate file stem (breaks wikilink resolution)"
            if empties:
                label += f" — empty stubs: {', '.join(empties)}"
            issues.append({"file": paths[0], "line": None, "severity": "high",
                           "label": label, "paths": paths})
        if vault.abs_path(paths[0]).stat().st_size == 0 and len(paths) == 1:
            issues.append({"file": paths[0], "line": None, "severity": "medium",
                           "label": "empty file"})

    for rel in rels:
        if vault.abs_path(rel).stat().st_size == 0:
            continue
        parsed = vault.get(rel)
        for f in parsed.fields:
            for pat, label in QUIRK_PATTERNS:
                if pat.search(f.raw):
                    issues.append({"file": rel, "line": f.line_no,
                                   "severity": "low", "label": label,
                                   "snippet": f.raw[:100]})
            if f.name.strip().lower() == "requirement":
                issues.append({"file": rel, "line": f.line_no, "severity": "low",
                               "label": "singular field name 'Requirement' (should be 'Requirements')",
                               "snippet": f.raw[:100]})
        # WI / deprecated attr codes in Attributes values
        attr = parsed.field_value("Attributes")
        if attr:
            for code in re.split(r"[/,\s]+", attr):
                if code in ATTR_TYPOS and code == "WI":
                    issues.append({"file": rel, "line": parsed.field("Attributes").line_no,
                                   "severity": "low",
                                   "label": f"attribute typo: {code} (should be {ATTR_TYPOS[code]})",
                                   "snippet": attr})
    return issues


def issues_for_record(vault: Vault, rel: str, full: dict | None = None) -> list[dict]:
    """Filter the full check results down to one record (for the record view)."""
    full = full or run_checks(vault)
    out = []

    def add(sev, label, detail=""):
        out.append({"severity": sev, "label": label, "detail": detail})

    for h in full["legacy"]:
        if h["file"] == rel:
            add(h["severity"], h["label"], f"line {h['line']}: {h['snippet']}")
    for e in full["brokenEmbeds"]:
        if e["file"] == rel:
            add("high", f"broken embed → {e['target']}", f"line {e['line']}")
    for l in full["brokenLinks"]:
        if l["file"] == rel:
            add("high", f"broken link → {l['target']}", f"line {l['line']}")
    for d in full["deprecatedRefs"]:
        if d["file"] == rel:
            add("medium", f"link into UNEDITED/Deprecated → {d['target']}", f"line {d['line']}")
    for v in full["perkViolations"]:
        if v["file"] == rel:
            for iss in v["issues"]:
                add("high", f"perk template: {iss}")
    for v in full["spellViolations"]:
        if v["file"] == rel:
            for iss in v["issues"]:
                sev = "low" if iss in STALE_CHECKS else "high"
                add(sev, f"spell template: {iss}")
    for h in full["deprecatedAttr"]:
        if h["file"] == rel:
            add("medium", h["label"], f"line {h['line']}: {h['snippet']}")
    for i in full["editorExtras"]:
        if i["file"] == rel or rel in i.get("paths", []):
            add(i["severity"], i["label"])
    return out
