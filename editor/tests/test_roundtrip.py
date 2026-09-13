"""Round-trip gates for the vault parser.

1. Model spans must reassemble to the original text byte-identically for
   every .md file in the vault (554 files).
2. apply_edits with an empty Edits must be a no-op.
3. Field edits on synthetic and real files must only touch the intended
   region.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from editor.server.selfcheck import reassemble  # noqa: E402
from editor.server.serialize import Edits, apply_edits  # noqa: E402
from editor.server.vault import BOM, Vault, parse_text  # noqa: E402

VAULT = Vault()


def all_rels() -> list[str]:
    return VAULT.scan()


@pytest.mark.parametrize("rel", all_rels())
def test_reassembly_byte_identical(rel: str):
    parsed = VAULT.get(rel)
    assert reassemble(parsed) == parsed.text, "model spans failed to reassemble"


def test_empty_edits_are_noop():
    for rel in all_rels():
        parsed = VAULT.get(rel)
        assert apply_edits(parsed, Edits()) == parsed.text


def test_field_span_integrity():
    for rel in all_rels():
        parsed = VAULT.get(rel)
        for f in parsed.fields:
            assert parsed.text[f.line.start:f.line.end] == f.raw
        for s in parsed.sections:
            assert parsed.text[s.heading.start:s.body_start].startswith("#")


# ---- synthetic edit tests ---------------------------------------------------

PERK = (
    "**Requirements:** Martial 2\n"
    "**Attributes:** AG/DX\n"
    "**Cost:** 10 XP\n"
    "**Tags:** #Combat \n"
    "\n"
    "## Description\n"
    "Shoot two different targets with one attack.\n"
    "\n"
    "## Grants\n"
    "\n"
    "![[Ability - Double Shot]]\n"
)


def test_header_edit_only_touches_header():
    parsed = parse_text(PERK, rel="Perks/CombatPerks/Test Perk.md")
    new = apply_edits(parsed, Edits(header_fields={"Cost": "12 XP"}))
    # header regen canonicalizes: new Cost value, trailing space on Tags dropped
    expected = PERK.replace("**Cost:** 10 XP", "**Cost:** 12 XP")
    expected = expected.replace("**Tags:** #Combat \n", "**Tags:** #Combat\n")
    assert new == expected


def test_header_edit_drops_quirk_prefix():
    quirk = "1**Requirements:** Martial 2\n" + PERK.split("\n", 1)[1]
    parsed = parse_text(quirk, rel="Perks/CombatPerks/Test Perk.md")
    new = apply_edits(parsed, Edits(header_fields={"Cost": "10 XP"}))
    assert new.startswith("**Requirements:** Martial 2\n")


def test_section_edit_only_touches_section():
    parsed = parse_text(PERK, rel="Perks/CombatPerks/Test Perk.md")
    new = apply_edits(parsed, Edits(section_bodies={"description": "New text.\n"}))
    # the body span is replaced verbatim (the old body ended with a blank
    # line; the new body is exactly what was sent)
    assert new == PERK.replace(
        "Shoot two different targets with one attack.\n\n", "New text.\n")
    # everything after the body span is untouched
    assert new.endswith("## Grants\n\n![[Ability - Double Shot]]\n")


def test_grants_regen():
    parsed = parse_text(PERK, rel="Perks/CombatPerks/Test Perk.md")
    new = apply_edits(parsed, Edits(grants={"mode": "simple",
                                            "embeds": ["Ability - A", "Effect - B"]}))
    assert "## Grants\n\n![[Ability - A]]\n![[Effect - B]]\n" in new
    assert "![[Ability - Double Shot]]" not in new
    # everything before the Grants section is untouched
    assert new[: new.index("## Grants")] == PERK[: PERK.index("## Grants")]


def test_grants_staged_regen():
    staged = PERK.replace("## Grants\n\n![[Ability - Double Shot]]\n",
                          "## Grants by Stage\n- **Stage 1:** ![[Effect - A]]\n")
    parsed = parse_text(staged, rel="Perks/CombatPerks/Conditioning/Cold.md")
    new = apply_edits(parsed, Edits(grants={
        "mode": "staged",
        "stages": {"1": ["Effect - A"], "2": ["Effect - B", "Effect - C"]}}))
    assert "## Grants by Stage\n- **Stage 1:** ![[Effect - A]]\n- **Stage 2:** ![[Effect - B]] + ![[Effect - C]]\n" in new


def test_grants_insert_when_missing():
    no_grants = PERK[: PERK.index("## Grants")]
    parsed = parse_text(no_grants, rel="Perks/CombatPerks/Test Perk.md")
    new = apply_edits(parsed, Edits(grants={"mode": "simple", "embeds": ["Effect - X"]}))
    assert "## Description\n" in new  # still present
    assert "## Grants\n\n![[Effect - X]]\n" in new


def test_loose_field_append_and_edit():
    ability = ("**AP Cost:** 4\n\nShoot.\n\n**Tags:** #Attack\n")
    parsed = parse_text(ability, rel="Actions/Abilities/Ability - Test.md")
    new = apply_edits(parsed, Edits(loose_fields={"Tags": "#Attack #Burst"}))
    assert new == "**AP Cost:** 4\n\nShoot.\n\n**Tags:** #Attack #Burst\n"

    no_tags = "**AP Cost:** 4\n\nShoot.\n"
    parsed = parse_text(no_tags, rel="Actions/Abilities/Ability - Test.md")
    new = apply_edits(parsed, Edits(loose_fields={"Tags": "#Passive"}))
    assert new == "**AP Cost:** 4\n\nShoot.\n\n**Tags:** #Passive\n"


def test_header_insert_into_body_first_file():
    body_first = "Just description text.\n"
    parsed = parse_text(body_first, rel="Perks/CombatPerks/Test.md")
    new = apply_edits(parsed, Edits(header_fields={"Cost": "5 XP"}))
    assert new == "**Cost:** 5 XP\n\nJust description text.\n"


def test_header_insert_noop_for_wrong_type():
    # effects keep Tags as a loose end-of-file field, not a header field
    effect = "Gain +1 to defenses.\n"
    parsed = parse_text(effect, rel="Rules/Effects/Effect - Test.md")
    new = apply_edits(parsed, Edits(header_fields={"Tags": "#Passive"}))
    assert new == effect


def test_crlf_preserved():
    perk_crlf = PERK.replace("\n", "\r\n")
    parsed = parse_text(perk_crlf, rel="Perks/CombatPerks/Test.md")
    new = apply_edits(parsed, Edits(header_fields={"Cost": "10 XP"}))
    assert "\r\n" in new
    assert new.replace("\r\n", "\n") == apply_edits(
        parse_text(PERK, rel="Perks/CombatPerks/Test.md"),
        Edits(header_fields={"Cost": "10 XP"}))


def test_bom_preserved():
    parsed = parse_text(BOM + PERK, rel="Perks/CombatPerks/Test.md")
    assert parsed.bom
    new = apply_edits(parsed, Edits(header_fields={"Cost": "10 XP"}))
    assert new.startswith(BOM)


def test_real_perk_header_regen_minimal_diff():
    rel = "Perks/CombatPerks/Footwork/Footwork.md"
    parsed = VAULT.get(rel)
    same = apply_edits(parsed, Edits(header_fields={
        "Requirements": parsed.field_value("Requirements"),
        "Attributes": parsed.field_value("Attributes"),
        "Cost": parsed.field_value("Cost"),
        "Tags": parsed.field_value("Tags"),
    }))
    # canonical regeneration must only normalize the header block:
    # Footwork's header is canonical except the trailing space on Tags.
    assert same == parsed.text.replace("**Tags:** #Combat \n", "**Tags:** #Combat\n")


def test_grants_parsing():
    parsed = VAULT.get("Perks/CombatPerks/Conditioning/Cold Conditioning.md")
    g = parsed.grants()
    assert g["mode"] == "staged"
    assert g["stages"][5] == ["Effect - Cold Conditioning", "Effect - Extra Wound"]
    parsed = VAULT.get("Perks/CombatPerks/Archery/Double Shot.md")
    g = parsed.grants()
    assert g["mode"] == "simple"
    assert g["embeds"] == ["Ability - Double Shot"]


def test_spell_loose_fields():
    parsed = VAULT.get("Spells/Minor Healing.md")
    assert parsed.field("Limit Cost") is not None
    assert parsed.field("Duration").value == "Instant"
    assert parsed.header_block is not None
    assert parsed.field("Tier").in_header_block
    assert not parsed.field("Prerequisites").in_header_block


def test_section_edit_supersedes_loose_field_inside_it():
    spell = (
        "**Tier:** 1\n**AP Cost:** 3\n**Attributes:** WL/CH\n"
        "\n## Description\n\nFlavor.\n\n"
        "**Duration:** Instant\n**Prerequisites:** [[Heal]]\n"
    )
    parsed = parse_text(spell, rel="Spells/Test.md")
    # editing the Description body AND the Duration line inside it: the
    # body (region) edit wins; no overlap error
    new = apply_edits(parsed, Edits(
        section_bodies={"description": "New flavor.\n\n**Duration:** 1 shift\n"},
        loose_fields={"Duration": "1 shift"},
    ))
    assert "New flavor." in new
    assert "**Duration:** 1 shift" in new
    assert "Instant" not in new


def test_loose_field_edit_alone_still_works():
    spell = "## Description\n\nFlavor.\n\n**Duration:** Instant\n"
    parsed = parse_text(spell, rel="Spells/Test.md")
    new = apply_edits(parsed, Edits(loose_fields={"Duration": "1 shift"}))
    assert new == spell.replace("Instant", "1 shift")


def test_draft_toggle_roundtrip():
    base = "Some content.\n"
    parsed = parse_text(base, rel="Rules/Mechanics/Test.md")
    with_draft = apply_edits(parsed, Edits(draft=True))
    assert with_draft == "---\ndraft: true\n---\nSome content.\n"

    parsed = parse_text(with_draft, rel="Rules/Mechanics/Test.md")
    without = apply_edits(parsed, Edits(draft=False))
    assert without == base

    # toggling twice is a no-op the second time
    parsed = parse_text(with_draft, rel="Rules/Mechanics/Test.md")
    assert apply_edits(parsed, Edits(draft=True)) == with_draft


def test_draft_toggle_preserves_existing_frontmatter():
    fm = "---\nCore Rules Index: \"*A skill-based fantasy tabletop RPG*\"\n---\n"
    parsed = parse_text(fm + "Body.\n", rel="index.md")
    out = apply_edits(parsed, Edits(draft=True))
    assert 'draft: true' in out and 'Core Rules Index' in out
    parsed = parse_text(out, rel="index.md")
    out2 = apply_edits(parsed, Edits(draft=False))
    assert 'draft' not in out2 and 'Core Rules Index' in out2


def test_ability_blank_line_layout_survives_same_value_save():
    ability = (
        "**AP Cost:** R\n"
        "\n"
        "**Trigger:** Adjacent ally takes damage.\n"
        "**Effect:** Use your reaction to apply Shield Block for your ally.\n"
        "\n"
        "**Tags:** #Reaction #Block\n"
    )
    parsed = parse_text(ability, rel="Actions/Abilities/Ability - Shield Warden.md")
    same = apply_edits(parsed, Edits(header_fields={
        "AP Cost": "R", "Trigger": "Adjacent ally takes damage.",
        "Effect": "Use your reaction to apply Shield Block for your ally.",
        "Tags": "#Reaction #Block"}))
    assert same == ability  # identical values -> byte-identical file
    changed = apply_edits(parsed, Edits(header_fields={
        "AP Cost": "R", "Trigger": "Adjacent ally takes damage or is prone.",
        "Effect": "Use your reaction to apply Shield Block for your ally.",
        "Tags": "#Reaction #Block"}))
    assert changed == ability.replace("Adjacent ally takes damage.",
                                      "Adjacent ally takes damage or is prone.")


def test_new_field_inserts_before_trailing_tags():
    # Mobile Draw shape: AP Cost header, body, Tags at end — adding a
    # Trigger field should land above Tags, not at file end
    ability = "**AP Cost:** 2\n\nMove and draw.\n\n**Tags:** #Movement #Attack\n"
    parsed = parse_text(ability, rel="Actions/Abilities/Ability - Mobile Draw.md")
    new = apply_edits(parsed, Edits(loose_fields={"Trigger": "You move at least 1 zone."}))
    assert new == ("**AP Cost:** 2\n\nMove and draw.\n\n"
                   "**Trigger:** You move at least 1 zone.\n**Tags:** #Movement #Attack\n")


def test_new_field_appends_when_no_trailing_tags():
    ability = "**AP Cost:** 2\n\nMove.\n"
    parsed = parse_text(ability, rel="Actions/Abilities/Ability - Test.md")
    new = apply_edits(parsed, Edits(loose_fields={"Trigger": "Something."}))
    assert new == "**AP Cost:** 2\n\nMove.\n\n**Trigger:** Something.\n"


def test_effect_file_without_fields():
    parsed = VAULT.get("Rules/Effects/Effect - Footwork.md")
    assert parsed.fields == []
    assert parsed.sections == []
    assert parsed.intro.strip() == "While Unencumbered, gain +1 to all defenses."
