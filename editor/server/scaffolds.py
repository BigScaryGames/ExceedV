"""New-file scaffolds per type (create flows).

Formats mirror the real vault conventions so created files immediately
satisfy tools/consistency_check.py and the playtest app's parser
(**Field:** with colon outside bold, ## Grants with ![[...]] embeds).
"""
from __future__ import annotations

SCAFFOLDS: dict[str, dict] = {
    "perk": {
        "label": "Perk",
        "defaultFolder": "Perks/CombatPerks",
        "folderChoices": "perks",
        "template": (
            "**Requirements:** -\n"
            "**Attributes:** -\n"
            "**Cost:** 5 XP\n"
            "**Tags:** #Combat\n"
            "\n"
            "## Short Description\n"
            "\n"
            "## Grants\n"
            "\n"
            "## Description\n"
        ),
    },
    "skillPerk": {
        "label": "Skill Perk",
        "defaultFolder": "Perks/SkillPerks",
        "folderChoices": "perks",
        "template": (
            "**Requirements:** -\n"
            "**Attributes:** -\n"
            "**Cost:** 5 XP\n"
            "**Tags:** #Skill\n"
            "\n"
            "## Short Description\n"
            "\n"
            "## Grants\n"
            "\n"
            "## Description\n"
        ),
    },
    "magicPerk": {
        "label": "Magic Perk",
        "defaultFolder": "Perks/MagicPerks",
        "folderChoices": "perks",
        "template": (
            "**Requirements:** -\n"
            "**Attributes:** -\n"
            "**Cost:** 5 XP\n"
            "**Tags:** #Magic\n"
            "\n"
            "## Short Description\n"
            "\n"
            "## Grants\n"
            "\n"
            "## Description\n"
        ),
    },
    "flaw": {
        "label": "Flaw",
        "defaultFolder": "Perks/Flaws",
        "folderChoices": "perks",
        "template": (
            "**Requirements:** -\n"
            "**Attributes:** -\n"
            "**Cost:** -\n"
            "**Tags:** #Flaw\n"
            "\n"
            "## Short Description\n"
            "\n"
            "## Grants\n"
            "\n"
            "## Description\n"
        ),
    },
    "spell": {
        "label": "Spell",
        "defaultFolder": "Spells",
        "folderChoices": "spells",
        "template": (
            "**Tier:** 1\n"
            "**AP Cost:** 2\n"
            "**Attributes:** WL/CH\n"
            "**Base Target/Range:** 1 target in your zone\n"
            "**Traits:** #Spell #Active\n"
            "\n"
            "## Short Description\n"
            "\n"
            "## Effect\n"
            "**Limit Cost:** -\n"
            "**Effect:** \n"
            "\n"
            "## Description\n"
            "\n"
            "**Duration:** Instant\n"
            "**Prerequisites:** -\n"
        ),
    },
    "ritual": {
        "label": "Ritual",
        "defaultFolder": "Spells/Rituals",
        "folderChoices": "spells",
        "template": (
            "**Tier:** 1\n"
            "**AP Cost:** 1 minute (out of combat)\n"
            "**Attributes:** WL/CH\n"
            "**Base Target/Range:** 1 target in your zone\n"
            "**Traits:** #Spell #Ritual\n"
            "\n"
            "## Short Description\n"
            "\n"
            "## Effect\n"
            "**Limit Cost:** -\n"
            "**Effect:** \n"
            "\n"
            "## Description\n"
            "\n"
            "**Duration:** \n"
            "**Prerequisites:** -\n"
        ),
    },
    "ability": {
        "label": "Ability",
        "defaultFolder": "Actions/Abilities",
        "folderChoices": "folders-under:Actions",
        "namePrefix": "Ability - ",
        "template": (
            "**AP Cost:** 2\n"
            "\n"
            "What the ability does.\n"
            "\n"
            "**Tags:** #Passive\n"
        ),
    },
    "effect": {
        "label": "Effect",
        "defaultFolder": "Rules/Effects",
        "folderChoices": "folders-under:Rules",
        "namePrefix": "Effect - ",
        "template": (
            "What the effect does and when it applies.\n"
            "\n"
            "**Tags:** #Passive\n"
        ),
    },
    "action": {
        "label": "Action",
        "defaultFolder": "Actions/Combat",
        "folderChoices": "folders-under:Actions",
        "template": (
            "**AP Cost:** 2\n"
            "**Traits:** -\n"
            "**Roll:** -\n"
            "\n"
            "What the action does.\n"
        ),
    },
    "condition": {
        "label": "Condition",
        "defaultFolder": "Rules/References/Conditions",
        "folderChoices": "folders-under:Rules",
        "namePrefix": "Condition - ",
        "template": "Describe the condition and its mechanical impact.\n",
    },
    "mechanic": {
        "label": "Rule / Mechanic",
        "defaultFolder": "Rules/Mechanics",
        "folderChoices": "folders-under:Rules",
        "template": "Describe the mechanic.\n",
    },
}


def scaffold_meta() -> list[dict]:
    return [
        {"key": key, "label": s["label"], "defaultFolder": s["defaultFolder"],
         "namePrefix": s.get("namePrefix", "")}
        for key, s in SCAFFOLDS.items()
    ]
