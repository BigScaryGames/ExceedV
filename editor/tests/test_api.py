"""API layer tests against a temporary vault (never the real one)."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from fastapi.testclient import TestClient  # noqa: E402

import editor.server.main as main  # noqa: E402
from editor.server.vault import Vault  # noqa: E402

PERK_A = (
    "**Requirements:** Tier 1\n"
    "**Attributes:** AG/DX\n"
    "**Cost:** 5 XP\n"
    "**Tags:** #Combat\n"
    "\n"
    "## Short Description\n"
    "Quick feint.\n"
    "\n"
    "## Grants\n"
    "\n"
    "![[Effect - Feint]]\n"
    "\n"
    "## Description\n"
    "Lore text.\n"
)
EFFECT_FEINT = "You gain +1 to Feints.\n\n**Tags:** #Passive\n"
SPELL = (
    "**Requirements:** [[Feint]]\n"
    "**Tier:** 1\n"
    "**AP Cost:** 3\n"
    "**Attributes:** WL/CH\n"
    "**Base Target/Range:** 1 target in your zone\n"
    "**Traits:** #Spell #Active\n"
    "**Limit Cost:** -\n"
    "**Duration:** Instant\n"
    "\n"
    "## Effect\n"
    "**Effect:** Heal 1d6.\n"
    "\n"
    "## Description\n"
    "Heal.\n"
)


@pytest.fixture()
def client():
    with TemporaryDirectory() as tmp:
        root = Path(tmp) / "content"
        (root / "Perks/CombatPerks").mkdir(parents=True)
        (root / "Rules/Effects").mkdir(parents=True)
        (root / "Spells").mkdir(parents=True)
        (root / "Perks/CombatPerks/Feint.md").write_text(PERK_A, encoding="utf-8")
        (root / "Rules/Effects/Effect - Feint.md").write_text(EFFECT_FEINT, encoding="utf-8")
        (root / "Spells/Heal.md").write_text(SPELL, encoding="utf-8")

        real_vault = main.vault
        main.vault = Vault(root)
        try:
            with TestClient(main.app) as c:
                yield c
        finally:
            main.vault = real_vault


def read(root_client_vault, rel):
    return main.vault.read_text(rel)


def test_meta(client):
    r = client.get("/api/meta")
    assert r.status_code == 200
    body = r.json()
    assert body["attributeCodes"] == ["PR", "WL", "CH", "WT", "MG", "EN", "AG", "DX"]
    assert any(s["key"] == "perk" for s in body["scaffolds"])


def test_index_and_record(client):
    rows = client.get("/api/index", params={"type": "perk"}).json()
    assert [r["stem"] for r in rows] == ["Feint"]
    rec = client.get("/api/record", params={"path": "Perks/CombatPerks/Feint.md"}).json()
    assert rec["headerFields"]["Cost"] == "5 XP"
    assert rec["grants"]["embeds"] == ["Effect - Feint"]
    assert rec["type"] == "perk"


def test_save_is_surgical(client):
    r = client.put("/api/record", json={
        "path": "Perks/CombatPerks/Feint.md",
        "headerFields": {"Cost": "7 XP"},
    })
    assert r.status_code == 200
    assert r.json()["changed"] is True
    after = read(None, "Perks/CombatPerks/Feint.md")
    expected = PERK_A.replace("**Cost:** 5 XP", "**Cost:** 7 XP")
    assert after == expected


def test_save_noop_when_unchanged(client):
    r = client.put("/api/record", json={
        "path": "Perks/CombatPerks/Feint.md",
        "headerFields": {"Cost": "5 XP", "Tags": "#Combat"},
        "sectionBodies": {},
    })
    assert r.json()["changed"] is False


def test_header_add_field_lands_in_header_block(client):
    spell_no_duration = (
        "**Tier:** 1\n"
        "**AP Cost:** 2\n"
        "**Attributes:** WL/CH\n"
        "**Traits:** #Spell #Active\n"
        "\n"
        "## Effect\n"
        "**Effect:** Glow.\n"
        "\n"
        "## Description\n"
        "It glows.\n"
    )
    import editor.server.main as m
    m.vault.write_text("Spells/Glow.md", spell_no_duration)
    m.vault.invalidate("Spells/Glow.md")
    r = client.put("/api/record", json={
        "path": "Spells/Glow.md",
        "headerFields": {"Limit Cost": "-", "Duration": "Instant"},
    })
    assert r.status_code == 200
    after = read(None, "Spells/Glow.md")
    assert after == (
        "**Tier:** 1\n"
        "**AP Cost:** 2\n"
        "**Attributes:** WL/CH\n"
        "**Traits:** #Spell #Active\n"
        "**Limit Cost:** -\n"
        "**Duration:** Instant\n"
        "\n"
        "## Effect\n"
        "**Effect:** Glow.\n"
        "\n"
        "## Description\n"
        "It glows.\n"
    )
    rec = client.get("/api/record", params={"path": "Spells/Glow.md"}).json()
    secondary = [f["name"] for f in rec["fields"]
                 if f["inHeader"] and f["name"] not in ("Tier", "AP Cost", "Attributes", "Traits")]
    assert secondary == ["Limit Cost", "Duration"]


def test_header_remove_field_deletes_line(client):
    import editor.server.main as m
    spell_with_fields = (
        "**Tier:** 1\n"
        "**AP Cost:** 2\n"
        "**Attributes:** WL/CH\n"
        "**Traits:** #Spell #Active\n"
        "**Limit Cost:** -\n"
        "**Duration:** Instant\n"
        "\n"
        "## Effect\n"
        "**Effect:** Glow.\n"
        "\n"
        "## Description\n"
        "It glows.\n"
    )
    m.vault.write_text("Spells/Glow.md", spell_with_fields)
    m.vault.invalidate("Spells/Glow.md")
    r = client.put("/api/record", json={
        "path": "Spells/Glow.md",
        "headerFields": {"Limit Cost": "", "Duration": "1 round"},
    })
    assert r.status_code == 200
    after = read(None, "Spells/Glow.md")
    assert after == (
        "**Tier:** 1\n"
        "**AP Cost:** 2\n"
        "**Attributes:** WL/CH\n"
        "**Traits:** #Spell #Active\n"
        "**Duration:** 1 round\n"
        "\n"
        "## Effect\n"
        "**Effect:** Glow.\n"
        "\n"
        "## Description\n"
        "It glows.\n"
    )
    assert read(None, "Perks/CombatPerks/Feint.md") == PERK_A


def test_write_guard_rejects_outside_paths(client):
    for path in ("../outside.md", ".obsidian/app.json", "source/quartz/x.md"):
        r = client.get("/api/record", params={"path": path})
        assert r.status_code in (400, 404), path


def test_create_and_duplicate_guard(client):
    r = client.post("/api/create", json={
        "scaffold": "effect", "name": "Blessed", "folder": "Rules/Effects"})
    assert r.status_code == 200
    assert read(None, "Rules/Effects/Effect - Blessed.md").startswith("What the effect does")

    # duplicate stem forbidden (filenames are global identifiers)
    r = client.post("/api/create", json={
        "scaffold": "perk", "name": "Feint", "folder": "Perks/SkillPerks"})
    assert r.status_code == 400
    assert "duplicate stem" in r.json()["detail"]

    # ability prefix enforcement
    r = client.post("/api/create", json={
        "scaffold": "ability", "name": "Dash", "folder": "Actions/Abilities"})
    assert r.status_code == 200
    assert (main.vault.root / "Actions/Abilities/Ability - Dash.md").exists()


def test_rename_preview_and_apply(client):
    # preview: the spell references [[Feint]]
    r = client.post("/api/rename", json={"path": "Perks/CombatPerks/Feint.md",
                                         "newName": "Improved Feint"})
    body = r.json()
    assert body["preview"] is True
    assert any(c["file"] == "Spells/Heal.md" and c["after"] == "[[Improved Feint]]"
               for c in body["referenceChanges"])

    r = client.post("/api/rename", json={"path": "Perks/CombatPerks/Feint.md",
                                         "newName": "Improved Feint", "apply": True})
    assert r.status_code == 200
    assert "Perks/CombatPerks/Improved Feint.md" in main.vault.scan()
    assert "[[Improved Feint]]" in read(None, "Spells/Heal.md")
    assert "![[Effect - Feint]]" in read(None, "Perks/CombatPerks/Improved Feint.md")


def test_rename_move_updates_path_links(client):
    (main.vault.root / "Perks/SkillPerks").mkdir(parents=True, exist_ok=True)
    r = client.post("/api/rename", json={"path": "Perks/CombatPerks/Feint.md",
                                         "newFolder": "Perks/SkillPerks", "apply": True})
    assert r.status_code == 200
    assert "Perks/SkillPerks/Feint.md" in main.vault.scan()


def test_delete_preview_shows_inbound(client):
    r = client.post("/api/delete", json={"path": "Rules/Effects/Effect - Feint.md"})
    body = r.json()
    assert body["preview"] is True
    assert any(i["file"] == "Perks/CombatPerks/Feint.md"
               for i in body["inboundReferences"])

    r = client.post("/api/delete", json={"path": "Rules/Effects/Effect - Feint.md",
                                         "apply": True})
    assert r.status_code == 200
    assert "Rules/Effects/Effect - Feint.md" not in main.vault.scan()


def test_refs_and_tree(client):
    r = client.get("/api/refs", params={"stem": "Effect - Feint"})
    body = r.json()
    assert "Perks/CombatPerks/Feint.md" in body["embedders"]

    r = client.get("/api/tree", params={"stem": "Heal"})
    assert r.status_code == 200
    assert r.json()["field"] == "Requirements"


def test_checks_run(client):
    r = client.get("/api/checks")
    assert r.status_code == 200
    body = r.json()
    assert body["fileCount"] == 3
    assert isinstance(body["brokenEmbeds"], list)


def test_rulebook_tree(client):
    main.vault.write_text("Rules/Rulebook.md", "The book.\n\n![[Combat]]\n")
    main.vault.write_text("Rules/Combat.md", "The chapter.\n\n![[Section]]\n")
    main.vault.write_text("Rules/Combat/Section.md", "Section body.\n")
    main.vault.write_text("Rules/Combat/Extra.md", "Not wired.\n")

    r = client.get("/api/rulebook").json()
    assert r["root"]["name"] == "Rulebook"
    ch = r["root"]["children"][0]
    assert ch["name"] == "Combat"
    assert [c["name"] for c in ch["children"]] == ["Section"]
    assert ch["unwired"] == ["Extra.md"]
    assert [i["label"] for i in r["issues"]] == [
        "in chapter folder but not embedded by Combat.md"]

    # draft-marked section is flagged as part of the published tree
    client.put("/api/record", json={"path": "Rules/Combat/Section.md", "draft": True})
    r = client.get("/api/rulebook").json()
    assert r["root"]["children"][0]["children"][0]["draft"] is True
    assert any("draft" in i["label"] for i in r["issues"])


def test_read_resolves_embeds(client):
    r = client.get("/api/read", params={"path": "Perks/CombatPerks/Feint.md"}).json()
    assert r["embeds"] == [{"target": "Effect - Feint",
                            "path": "Rules/Effects/Effect - Feint.md",
                            "name": "Effect - Feint"}]


def test_draft_save_endpoint(client):
    r = client.put("/api/record", json={"path": "Spells/Heal.md", "draft": True})
    assert 'draft: true' in main.vault.read_text("Spells/Heal.md")
    r = client.put("/api/record", json={"path": "Spells/Heal.md", "draft": False})
    assert 'draft' not in main.vault.read_text("Spells/Heal.md")


def test_draft_and_conventions_files_exempt_from_checks(client):
    # conventions doc with an intentional example embed -> not an issue
    main.vault.write_text("CLAUDE.md", "Examples: ![[Ability - Name]]\n")
    # draft-marked file with a broken embed -> WIP, not checked
    main.vault.write_text("Perks/CombatPerks/WIP Thing.md",
                          "**Cost:** TBD\n\n![[Effect - Does Not Exist]]\n")
    client.put("/api/record", json={"path": "Perks/CombatPerks/WIP Thing.md", "draft": True})
    # a non-draft file with a broken embed still counts
    main.vault.write_text("Perks/CombatPerks/Broken.md",
                          "**Cost:** 5 XP\n\n![[Effect - Also Missing]]\n")

    r = client.get("/api/checks").json()
    assert all("CLAUDE.md" not in json.dumps(h) for h in
               r["brokenEmbeds"] + r["brokenLinks"] + r["editorExtras"])
    assert all("WIP Thing" not in json.dumps(h) for h in
               r["brokenEmbeds"] + r["editorExtras"])
    assert any("Broken.md" in e["file"] for e in r["brokenEmbeds"])
    assert r["exemptFiles"]["CLAUDE.md"] == "conventions doc"
    assert r["exemptFiles"]["Perks/CombatPerks/WIP Thing.md"] == "draft"


def test_session_records_writes(client):
    client.put("/api/record", json={"path": "Perks/CombatPerks/Feint.md",
                                    "headerFields": {"Cost": "6 XP"}})
    r = client.get("/api/session").json()
    assert any(w["path"] == "Perks/CombatPerks/Feint.md" and w["action"] == "edited"
               for w in r["writes"])


def test_selftest(client):
    r = client.get("/api/selftest").json()
    assert r["ok"] is True and r["files"] == 3
