#!/usr/bin/env python3
"""
ExceedV Consistency & Legacy Checker
=====================================
Scans source/content for:
  1. Legacy / grid-drift terminology (meters, tiles, flanking, adjacent, deleted actions)
  2. Broken wikilinks & embeds ([[X]] / ![[X]] pointing at nonexistent files)
  3. Links pointing at Deprecated/UNEDITED files
  4. Duplicate filenames (breaks Obsidian wikilink resolution)
  5. Perk template violations (missing required header fields)
  6. Spell template violations (missing required fields)
  7. Deprecated attribute codes & old domain names
  8. Perks/spells embedding nothing (no ![[Ability/Effect]])

Usage:
  python3 tools/consistency_check.py            # full report
  python3 tools/consistency_check.py --fix-hints # show suggested replacements
  python3 tools/consistency_check.py --json      # machine-readable output
"""
import os, re, json, argparse
from collections import defaultdict

ROOT = os.path.join(os.path.dirname(__file__), "..", "source", "content")
ROOT = os.path.abspath(ROOT)

# ═══════════════════════════════════════════════════════════════════════════
# Gather files
# ═══════════════════════════════════════════════════════════════════════════

def gather():
    files = []
    for dp, dn, fn in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT)
        # skip hidden dirs
        if rel != "." and os.path.basename(rel).startswith("."):
            continue
        for f in fn:
            if f.endswith(".md"):
                files.append(os.path.join(dp, f))
    return files

def read(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        return f"[READ ERROR: {e}]"

def short(p):
    return os.path.relpath(p, ROOT)

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 1: Legacy terminology
# ═══════════════════════════════════════════════════════════════════════════

LEGACY_PATTERNS = [
    # Grid / positioning terms
    (r'\btiles?\b', "grid: tile", "high"),
    (r'\bsquares?\b(?!\s*,\s*etc)', "grid: square", "high"),
    (r'\bflank(?:ing|ed)?\b', "removed: flanking", "high"),
    (r'\b(\d+)\s*(?:meters?|metres|m)\b(?!\s*(?:inute|s|s\b))', "distance: meter (→ zones/lines)", "high"),
    (r'\b(\d+)\s*(?:feet|foot|ft|yards?|yd)\b', "distance: imperial (→ zones/lines)", "high"),
    (r'\badjacent\b', "grid: adjacent (→ same skirmish/zone)", "medium"),
    # Deleted movement actions
    (r'(?<!\w)Stride\b(?!s?\s+(on|over|across|by))', "deleted action: Stride (→ Move)", "medium"),
    (r'(?<!\w)Crawl\b', "deleted action: Crawl", "medium"),
    # Legacy mechanical terms
    (r'\bconcentration\b(?!\s*(?:check|camp|rate))', "legacy: concentration (→ Limit)", "low"),
    (r'\bExtra\s*Wounds?\b', "legacy: Extra Wound (→ Conditioning)", "low"),
    (r'\battunement\b', "legacy: attunement (→ Limit)", "low"),
]

# Contexts to skip (false positives)
SKIP_CTX = re.compile(
    r'(minute|hour|second|schedule|format|image|wimmer|warm|run\s+(?:operations?|time|through|out|down|up|the|faster|a|an|its)|'
    r'home\s+run|bowling|spear|running|story\s+progression|adjacent\s+things|run\s+their|long\s+run)',
    re.I
)

def check_legacy(files, contents):
    hits = []
    skip_files = {"Map To Zones", "Content Plan Musings", "MILESTONES", "Design Guidelines"}
    for path in files:
        fname = os.path.basename(path)[:-3]
        if any(s in fname for s in skip_files):
            continue
        lines = contents[path].split("\n")
        for i, line in enumerate(lines, 1):
            for pat, label, sev in LEGACY_PATTERNS:
                for m in re.finditer(pat, line, re.I):
                    snippet = line.strip()[:120]
                    if SKIP_CTX.search(snippet):
                        continue
                    hits.append({"file": short(path), "line": i, "label": label,
                                 "severity": sev, "snippet": snippet})
    return hits

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 2: Broken wikilinks & embeds
# ═══════════════════════════════════════════════════════════════════════════

def check_links(files, contents):
    # Build lookup: stem (filename without ext) → True, AND full relative paths
    valid_stems = {os.path.basename(p)[:-3] for p in files}
    deprecated_stems = {os.path.basename(p)[:-3] for p in files
                        if "Deprecated" in p or "UNEDITED" in p}
    # Also index by relative path (with and without .md) for path-style links
    valid_paths = {short(p) for p in files}
    valid_paths_nomd = {p[:-3] for p in valid_paths}

    def resolve_target(target):
        """Return 'valid', 'deprecated', or 'broken'. Assumes target is pre-cleaned."""
        target = target.strip()
        if target.startswith("http"):
            return "skip"
        # Try as stem first (Obsidian default)
        if "/" not in target and "\\" not in target:
            if target in deprecated_stems:
                return "deprecated"
            if target in valid_stems:
                return "valid"
            return "broken"
        # Path-style link: normalize and check
        normalized = target.replace("\\", "/").replace("source/content/", "")
        # Try with .md
        if normalized in valid_paths:
            return "valid"
        # Try without .md
        if normalized in valid_paths_nomd:
            return "valid"
        # Try matching the last segment as a stem (Obsidian resolves to filename)
        last_seg = os.path.basename(normalized).replace(".md", "")
        if last_seg in valid_stems:
            # Check if it's deprecated
            # Find actual path
            for p in files:
                if os.path.basename(p)[:-3] == last_seg:
                    if "Deprecated" in p or "UNEDITED" in p:
                        return "deprecated"
                    return "valid"
            return "valid"
        return "broken"

    broken_embeds = []
    broken_links = []
    deprecated_refs = []

    EMBED_RE = re.compile(r'!\[\[([^\]|#]+?)(?:[#|][^\]]*)?\]\]')
    LINK_RE = re.compile(r'(?<!\!)\[\[([^\]|#]+?)(?:[#|][^\]]*)?\]\]')

    def clean_target(t):
        """Strip trailing backslash from escaped pipes: [[Aid\|Aid]] → 'Aid'."""
        return t.strip().rstrip("\\").strip()

    for path in files:
        lines = contents[path].split("\n")
        for i, line in enumerate(lines, 1):
            for m in EMBED_RE.finditer(line):
                target = clean_target(m.group(1))
                status = resolve_target(target)
                if status == "skip":
                    continue
                if status == "broken":
                    broken_embeds.append({"file": short(path), "line": i,
                                          "target": target, "snippet": line.strip()[:100]})
            for m in LINK_RE.finditer(line):
                target = clean_target(m.group(1))
                status = resolve_target(target)
                if status == "skip":
                    continue
                if status == "deprecated":
                    deprecated_refs.append({"file": short(path), "line": i,
                                            "target": target, "snippet": line.strip()[:100]})
                elif status == "broken":
                    broken_links.append({"file": short(path), "line": i,
                                         "target": target, "snippet": line.strip()[:100]})
    return broken_embeds, broken_links, deprecated_refs

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 3: Duplicate filenames
# ═══════════════════════════════════════════════════════════════════════════

def check_duplicates(files):
    name_map = defaultdict(list)
    for p in files:
        name_map[os.path.basename(p)].append(p)
    dups = {name: paths for name, paths in name_map.items() if len(paths) > 1}
    return [{"name": name, "paths": [short(p) for p in paths]}
            for name, paths in dups.items()]

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 4: Perk template violations
# ═══════════════════════════════════════════════════════════════════════════

PERK_REQUIRED = ["Requirements", "Attributes", "Cost", "Tags"]
PERK_HEADER_RE = re.compile(r'^\*\*(Requirements|Attributes|Cost|Tags)\**[:(]', re.M)

def check_perks(files, contents):
    violations = []
    perk_dirs = ["Perks/CombatPerks", "Perks/SkillPerks", "Perks/MagicPerks", "Perks/Flaws"]
    for path in files:
        sp = short(path)
        if not any(sp.startswith(d) for d in perk_dirs):
            continue
        if "UNEDITED" in sp:
            continue
        text = contents[path]
        found = set(PERK_HEADER_RE.findall(text))
        missing = [f for f in PERK_REQUIRED if f not in found]

        # Check for embed (grants something)
        has_embed = bool(re.search(r'!\[\[(Ability|Effect)', text))

        issues = []
        if missing:
            issues.append(f"missing fields: {', '.join(missing)}")
        if not has_embed:
            issues.append("no ![[Ability/Effect]] embed found")
        if issues:
            violations.append({"file": sp, "issues": issues})
    return violations

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 5: Spell template violations
# ═══════════════════════════════════════════════════════════════════════════

SPELL_REQUIRED = ["Tier", "AP Cost", "Attributes"]
# Matches **Tier:** (colon inside bold, the actual format)
SPELL_HEADER_RE = re.compile(r'\*\*(Tier|AP Cost|Attributes):', re.M)

def check_spells(files, contents):
    violations = []
    for path in files:
        sp = short(path)
        if not sp.startswith("Spells/"):
            continue
        if "Template" in sp or "Plan" in sp:
            continue
        text = contents[path]
        found = set(SPELL_HEADER_RE.findall(text))
        missing = [f for f in SPELL_REQUIRED if f not in found]
        has_limit = bool(re.search(r'\*\*Limit Cost:', text))
        has_version = bool(re.search(r'## (Basic|Advanced) Version', text))

        issues = []
        if missing:
            issues.append(f"missing fields: {', '.join(missing)}")
        if not has_limit:
            issues.append("no 'Limit Cost' field")
        if not has_version:
            issues.append("no Basic/Advanced version sections")
        if issues:
            violations.append({"file": sp, "issues": issues})
    return violations

# ═══════════════════════════════════════════════════════════════════════════
# CHECK 6: Deprecated attribute codes & old domain references
# ═══════════════════════════════════════════════════════════════════════════

# Valid 2-letter attribute abbreviations
VALID_ATTRS = {"PR", "WL", "CH", "WT", "MG", "EN", "AG", "DX"}
# Old 3-letter codes that should have been replaced
OLD_ATTR_RE = re.compile(r'\b(PER|WIL|CHA|WIT|MIG|END|AGI|DEX|CON|INT|STR)\b')
# Old domain names
OLD_DOMAIN_RE = re.compile(r'\b(Weapon Training|CN\d|PW\d|HT\d|SP\b)\b')

def check_deprecated_refs(files, contents):
    hits = []
    skip = {"Map To Zones", "Content Plan", "MILESTONES", "HEAP of concepts",
            "Design Guidelines", "0 Skill Perk Template", "0 Spell Template",
            "0 Universal Perk Template"}
    for path in files:
        fname = os.path.basename(path)[:-3]
        if any(s in fname for s in skip):
            continue
        lines = contents[path].split("\n")
        for i, line in enumerate(lines, 1):
            for m in OLD_ATTR_RE.finditer(line):
                code = m.group(1)
                snippet = line.strip()[:110]
                hits.append({"file": short(path), "line": i,
                             "label": f"old attr code: {code}", "snippet": snippet})
    return hits

# ═══════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fix-hints", action="store_true")
    args = ap.parse_args()

    files = gather()
    contents = {p: read(p) for p in files}

    results = {
        "file_count": len(files),
        "legacy": check_legacy(files, contents),
        "broken_embeds": None,
        "broken_links": None,
        "deprecated_refs": None,
        "duplicates": check_duplicates(files),
        "perk_violations": check_perks(files, contents),
        "spell_violations": check_spells(files, contents),
        "deprecated_attr": check_deprecated_refs(files, contents),
    }

    be, bl, dr = check_links(files, contents)
    results["broken_embeds"] = be
    results["broken_links"] = bl
    results["deprecated_refs"] = dr

    if args.json:
        print(json.dumps(results, indent=2))
        return

    print_report(results, fix_hints=args.fix_hints)

def print_report(r, fix_hints=False):
    sep = "=" * 75
    print(f"\n{sep}")
    print(f"EXCEEDV CONSISTENCY CHECK — {r['file_count']} files scanned")
    print(sep)

    # --- Legacy ---
    print(f"\n{'─'*75}")
    print("1. LEGACY / GRID DRIFT")
    print(f"{'─'*75}")
    for sev in ("high", "medium", "low"):
        items = [h for h in r["legacy"] if h["severity"] == sev]
        print(f"\n  [{sev.upper()}] {len(items)} hits")
        by_label = defaultdict(list)
        for h in items:
            by_label[h["label"]].append(h)
        for label, hits in sorted(by_label.items(), key=lambda x: -len(x[1])):
            print(f"\n    ■ {label} ({len(hits)} hits)")
            for h in hits[:10]:
                print(f"      {h['file']}:{h['line']}  {h['snippet']}")
            if len(hits) > 10:
                print(f"      ... +{len(hits)-10} more")

    # --- Broken embeds ---
    print(f"\n{'─'*75}")
    print(f"2. BROKEN EMBEDS (![[...]] → nonexistent file)  — {len(r['broken_embeds'])}")
    print(f"{'─'*75}")
    for e in sorted(r["broken_embeds"], key=lambda x: x["target"])[:30]:
        print(f"  {e['file']}:{e['line']}  → '{e['target']}'")
    if len(r["broken_embeds"]) > 30:
        print(f"  ... +{len(r['broken_embeds'])-30} more")

    # --- Broken links ---
    print(f"\n{'─'*75}")
    print(f"3. BROKEN LINKS ([[...]] → nonexistent file)  — {len(r['broken_links'])}")
    print(f"{'─'*75}")
    by_tgt = defaultdict(list)
    for l in r["broken_links"]:
        by_tgt[l["target"]].append(l)
    for tgt, hits in sorted(by_tgt.items(), key=lambda x: -len(x[1]))[:25]:
        print(f"\n  '{tgt}' ({len(hits)} refs)")
        for h in hits[:3]:
            print(f"    {h['file']}:{h['line']}")
    if len(by_tgt) > 25:
        print(f"\n  ... +{len(by_tgt)-25} more targets")

    # --- Deprecated file refs ---
    print(f"\n{'─'*75}")
    print(f"4. LINKS TO DEPRECATED/UNEDITED FILES  — {len(r['deprecated_refs'])}")
    print(f"{'─'*75}")
    for d in sorted(r["deprecated_refs"], key=lambda x: x["target"])[:20]:
        print(f"  {d['file']}:{d['line']}  → '{d['target']}'")

    # --- Duplicates ---
    print(f"\n{'─'*75}")
    print(f"5. DUPLICATE FILENAMES  — {len(r['duplicates'])}")
    print(f"{'─'*75}")
    for d in r["duplicates"]:
        print(f"\n  '{d['name']}'")
        for p in d["paths"]:
            print(f"    {p}")

    # --- Perk template ---
    print(f"\n{'─'*75}")
    print(f"6. PERK TEMPLATE VIOLATIONS  — {len(r['perk_violations'])}")
    print(f"{'─'*75}")
    for v in sorted(r["perk_violations"], key=lambda x: x["file"])[:30]:
        print(f"  {v['file']}")
        for iss in v["issues"]:
            print(f"    ⚠ {iss}")
    if len(r["perk_violations"]) > 30:
        print(f"  ... +{len(r['perk_violations'])-30} more")

    # --- Spell template ---
    print(f"\n{'─'*75}")
    print(f"7. SPELL TEMPLATE VIOLATIONS  — {len(r['spell_violations'])}")
    print(f"{'─'*75}")
    for v in sorted(r["spell_violations"], key=lambda x: x["file"]):
        print(f"  {v['file']}")
        for iss in v["issues"]:
            print(f"    ⚠ {iss}")

    # --- Deprecated attr codes ---
    print(f"\n{'─'*75}")
    print(f"8. OLD ATTRIBUTE CODES (3-letter / D&D-isms)  — {len(r['deprecated_attr'])}")
    print(f"{'─'*75}")
    by_lbl = defaultdict(list)
    for h in r["deprecated_attr"]:
        by_lbl[h["label"]].append(h)
    for lbl, hits in sorted(by_lbl.items(), key=lambda x: -len(x[1])):
        print(f"\n  ■ {lbl} ({len(hits)} hits)")
        for h in hits[:8]:
            print(f"    {h['file']}:{h['line']}  {h['snippet']}")
        if len(hits) > 8:
            print(f"    ... +{len(hits)-8} more")

    # --- Summary ---
    print(f"\n{sep}")
    print("SUMMARY")
    print(sep)
    hi = len([h for h in r["legacy"] if h["severity"] == "high"])
    md = len([h for h in r["legacy"] if h["severity"] == "medium"])
    lo = len([h for h in r["legacy"] if h["severity"] == "low"])
    print(f"  Legacy (H/M/L):     {hi} / {md} / {lo}")
    print(f"  Broken embeds:      {len(r['broken_embeds'])}")
    print(f"  Broken links:       {len(r['broken_links'])}")
    print(f"  Dep'd file refs:    {len(r['deprecated_refs'])}")
    print(f"  Duplicate files:    {len(r['duplicates'])}")
    print(f"  Perk violations:    {len(r['perk_violations'])}")
    print(f"  Spell violations:   {len(r['spell_violations'])}")
    print(f"  Old attr codes:     {len(r['deprecated_attr'])}")
    print()

if __name__ == "__main__":
    main()
