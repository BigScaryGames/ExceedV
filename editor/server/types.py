"""Record type inference (folder/prefix based, per source/content/CLAUDE.md)
and the per-type field schemas that drive the editor forms.
"""
from __future__ import annotations

VALID_ATTRS = ["PR", "WL", "CH", "WT", "MG", "EN", "AG", "DX"]
# The spell template and 4 real files use WI as a Wit typo.
ATTR_TYPOS = {"WI": "WT", "PER": "PR", "WIL": "WL", "CHA": "CH", "WIT": "WT",
              "MIG": "MG", "END": "EN", "AGI": "AG", "DEX": "DX",
              "CON": "EN", "INT": "WT", "STR": "MG"}

# Two-tier tag vocabulary from CLAUDE.md ("Tag Conventions").
# CATEGORY_TAGS are the organizing dimension for rule/mechanic files:
# #Combat (used in fights), #Core (base resolution), #Downtime (between
# adventures), #Magic, #Social.
CATEGORY_TAGS = ["#Combat", "#Core", "#Downtime", "#Magic", "#Social"]
PERK_TAGS = ["#Combat", "#Skill", "#Magic", "#Universal", "#Flaw",
             "#WeaponTraining", "#Shield", "#StavesSpears", "#Conditioning",
             "#Leveled", "#Rank", "#Spellcraft", "#Metamagic", "#Instant",
             "#Specialization", "#GM", "#Wrestling"]
MECHANIC_TAGS = CATEGORY_TAGS + ["#Strike", "#Projectile", "#Burst", "#Reaction", "#Passive",
                 "#Dodge", "#Deflect", "#Endure", "#Resolve", "#Damage",
                 "#Healing", "#Buff", "#Debuff", "#AoE", "#Melee", "#Ranged",
                 "#Movement", "#Attack", "#Block", "#Mind", "#Body", "#Defend",
                 "#Aura", "#HP", "#limit1"]
SPELL_TAGS = ["#Spell", "#Active", "#Attuned", "#Healing", "#Boon", "#Bane",
              "#Manipulation", "#Illusion", "#Conjuration", "#Transformation",
              "#Protection", "#Scrying", "#Ward", "#Ritual", "#Equipment",
              "#Strike", "#AOE", "#Summoning"]

TYPES = ["perk", "spell", "ability", "effect", "action", "condition",
         "mechanic", "rule", "template", "doc"]


def infer_type(rel: str) -> tuple[str, str]:
    """(type, subtype) from the vault-relative posix path."""
    p = rel
    stem = p.rsplit("/", 1)[-1][:-3] if p.endswith(".md") else p.rsplit("/", 1)[-1]
    low = stem.lower()

    if low.startswith("0 ") and "template" in low:
        return "template", ""

    if p.startswith("Perks/UNEDITED/"):
        return "perk", "unedited"
    if p.startswith("Perks/CombatPerks/"):
        return "perk", "combat"
    if p.startswith("Perks/SkillPerks/"):
        return "perk", "skill"
    if p.startswith("Perks/MagicPerks/"):
        return "perk", "magic"
    if p.startswith("Perks/Flaws/"):
        return "perk", "flaw"
    if p.startswith("Perks/"):
        return ("template", "perk") if low.startswith("0 ") and "template" in low else ("doc", "")

    if p.startswith("Spells/Rituals/"):
        return "spell", "ritual"
    if p.startswith("Spells/Tier 0/"):
        return "spell", "tier0"
    if p.startswith("Spells/"):
        if low.startswith("0 ") and "template" in low:
            return "template", "spell"
        if "plan" in low:
            return "doc", "plan"
        return "spell", ""

    if p.startswith("Actions/Abilities/") or stem.startswith("Ability - "):
        return "ability", ""
    if p.startswith("Rules/Effects/") or stem.startswith("Effect - "):
        return "effect", ""
    for sub in ("Combat", "Movement", "Social", "Support"):
        if p.startswith(f"Actions/{sub}/"):
            return "action", sub.lower()
    if p.startswith("Actions/"):
        return "action", ""
    if p.startswith("Rules/References/Conditions/"):
        return "condition", ""
    if p.startswith("Rules/Mechanics/"):
        return "mechanic", ""
    if p.startswith("Rules/Lines And Zones/"):
        return "mechanic", ""
    if p.startswith("Rules/References/"):
        return "rule", "reference"
    if p.startswith("Rules/"):
        return "rule", ""
    return "doc", ""


# Field schemas per type. kind drives the form widget; order is the canonical
# header order used when regenerating the header block on save.
FIELD_KINDS = {
    "requirements": "requirements",
    "attributes": "attributes",
    "cost": "cost",
    "apcost": "apcost",
    "tags": "tags",
    "text": "text",
    "number": "number",
}

SCHEMAS: dict[str, dict] = {
    "perk": {
        "fields": [
            {"name": "Requirements", "kind": "requirements", "label": "Requirements"},
            {"name": "Attributes", "kind": "attributes", "label": "Attributes"},
            {"name": "Cost", "kind": "cost", "label": "Cost"},
            {"name": "AP Cost", "kind": "apcost", "label": "AP Cost", "optional": True},
            {"name": "Tags", "kind": "tags:perk", "label": "Tags"},
        ],
        "sections": ["Grants", "Grants by Stage", "Description"],
        "tableColumns": ["Requirements", "Attributes", "Cost", "Tags", "Grants"],
    },
    "spell": {
        "fields": [
            {"name": "Requirements", "kind": "requirements", "label": "Requirements"},
            {"name": "Tier", "kind": "number", "label": "Tier", "half": True},
            {"name": "AP Cost", "kind": "apcost", "label": "AP Cost", "half": True},
            {"name": "XP Cost", "kind": "text", "label": "XP Cost", "optional": True, "half": True},
            {"name": "Attributes", "kind": "attributes", "label": "Attributes", "half": True},
            {"name": "Base Target/Range", "kind": "text", "label": "Target"},
            {"name": "Traits", "kind": "tags:spell", "label": "Traits"},
            {"name": "Tags", "kind": "tags:spell", "label": "Tags", "optional": True},
        ],
        "sections": ["Effect", "Description"],
        "looseFields": ["Limit Cost", "Duration"],
        "tableColumns": ["Tier", "AP Cost", "Attributes", "Traits", "Requirements"],
    },
    "ability": {
        "fields": [
            {"name": "AP Cost", "kind": "apcost", "label": "AP Cost"},
            {"name": "Tags", "kind": "tags:mechanic", "label": "Tags"},
        ],
        "looseFields": ["Trigger", "Effect", "Roll", "Limit Cost"],
        "sections": [],
        "tableColumns": ["AP Cost", "Tags"],
    },
    "effect": {
        "fields": [],
        "looseFields": ["Tags", "Progression", "Trigger", "Effect"],
        "sections": [],
        "tableColumns": ["Tags"],
    },
    "action": {
        "fields": [
            {"name": "AP Cost", "kind": "apcost", "label": "AP Cost"},
            {"name": "Traits", "kind": "tags:mechanic", "label": "Traits"},
        ],
        "looseFields": ["Roll", "Trigger", "Effect"],
        "sections": [],
        "tableColumns": ["AP Cost", "Traits"],
    },
    "condition": {"fields": [], "sections": [], "tableColumns": []},
    "mechanic": {"fields": [], "sections": [], "tableColumns": []},
    "rule": {"fields": [], "sections": [], "tableColumns": []},
    "template": {"fields": [], "sections": [], "tableColumns": []},
    "doc": {"fields": [], "sections": [], "tableColumns": []},
}

# Header fields that are part of the leading block for each type (order).
HEADER_FIELDS = {
    "perk": ["Requirements", "Attributes", "Cost", "AP Cost", "Tags"],
    "spell": ["Requirements", "Tier", "AP Cost", "XP Cost", "Attributes",
              "Base Target/Range", "Traits", "Tags"],
    "ability": ["AP Cost"],
    "action": ["AP Cost"],
}


def schema_for(type_: str) -> dict:
    return SCHEMAS.get(type_, SCHEMAS["doc"])


def is_perk(type_: str) -> bool:
    return type_ == "perk"
