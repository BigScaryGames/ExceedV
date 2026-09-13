"""Rulebook tree: derives the rules reading hierarchy from structure.

The Rulebook page (Rules/Rulebook.md) embeds the chapter pages; each
chapter page embeds its section hubs. The tree is derived from those
embeds in document order — no manifest to maintain. Files that sit in a
chapter folder but aren't embedded by their chapter page are flagged as
unwired; embeds that resolve to nothing are flagged broken; draft-marked
files inside the tree are flagged (they vanish from the published site).
"""
from __future__ import annotations

from pathlib import Path

from .records import _is_draft
from .vault import EMBED_RE, Vault, clean_target

RULEBOOK_PAGE = "Rules/Rulebook.md"
CHAPTER_FOLDERS = {"Intro", "Core", "Combat", "Magic",
                   "Social And World", "Downtime And Exploration"}


def rulebook_tree(vault: Vault) -> dict:
    if not vault.is_inside(RULEBOOK_PAGE):
        return {"root": None, "drafts": [], "issues": []}

    issues: list[dict] = []
    drafts: list[str] = []

    def node_for(rel: str, depth: int) -> dict:
        p = vault.get(rel)
        children, broken = [], []
        for m in EMBED_RE.finditer(p.text):
            target = clean_target(m.group(1))
            resolved = vault.resolve_stem(target)
            if resolved:
                child = node_for(resolved, depth + 1)
                children.append(child)
                if child["draft"]:
                    drafts.append(resolved)
                    issues.append({"file": resolved, "severity": "medium",
                                   "label": "draft-marked file is embedded in the published rulebook tree"})
            else:
                broken.append(target)
                issues.append({"file": rel, "severity": "high",
                               "label": f"broken embed in tree: ![[{target}]]"})

        # unwired: .md files in the chapter folder not embedded by the chapter page
        unwired: list[str] = []
        chapter_folder = vault.abs_path(f"Rules/{Path(rel).stem}")
        if depth == 1 and Path(rel).stem in CHAPTER_FOLDERS and chapter_folder.is_dir():
            embedded = {Path(c["path"]).name for c in children}
            for f in sorted(chapter_folder.glob("*.md")):
                if f.name not in embedded:
                    unwired.append(f.name)
                    issues.append({"file": f"Rules/{Path(rel).stem}/{f.name}",
                                   "severity": "medium",
                                   "label": f"in chapter folder but not embedded by {Path(rel).name}"})
        return {"path": rel, "name": Path(rel).stem, "draft": _is_draft(p),
                "children": children, "brokenEmbeds": broken, "unwired": unwired}

    root = node_for(RULEBOOK_PAGE, 0)
    return {"root": root, "drafts": sorted(set(drafts)), "issues": issues}
