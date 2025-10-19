---
type: perk
subtype: combat  # combat | skill | magic

name: Perk Name
id: perk-name  # kebab-case for machine lookups

requirements:
  domain: null  # "SH1", "OH2", etc. (combat perks only)
  skills: []  # ["Medicine 2", "Biology 2"]
  perks: []  # ["Other Perk Name"]
  special: []  # ["GM permission"]

attributes:
  - Attribute1  # Perception, Will, Charisma, Wit, Might, Endurance, Agility, Dexterity
  - Attribute2
  # - Domain  # Add if combat perk (e.g., Shield, OneHanded, Archery)

cost:
  xp: 0  # Fixed cost, or base cost for multi-level perks
  ap: null  # number or null (only combat perks usually have AP costs)
  
# Multi-level perk support (set to null if not applicable)
leveling:
  enabled: false  # true for perks that can be taken multiple times
  xp_formula: null  # e.g., "Max_Wounds * level" for ExtraHP
  max_level: null  # null for unlimited, or specific number
  consolidation: null  # Special rule when reaching certain levels

tags:
  - Tag1  # Shield, Strike, Social, Instant, etc.

short_description: Brief one-line description for tables and quick reference

effect: |
  Mechanical effects of the perk - what it does in game terms.
  This section describes the rules and mechanics.
  Multi-line is fine.

flavor: |
  Optional flavor text and narrative description.
  Context, lore, or examples of how the perk manifests.
  This was previously the "Description" section.
---

# Perk Name

## Short Description
Brief one-line description for tables and quick reference

## Effect
Mechanical effects of the perk - what it does in game terms

## Flavor
Optional flavor text and additional context

---

# Template Usage Notes

## Field Definitions

### Required Fields (All Perks)
- **type**: Always "perk"
- **subtype**: "combat", "skill", or "magic"
- **name**: Human-readable perk name
- **id**: Machine-readable kebab-case identifier
- **cost.xp**: XP cost to learn the perk
- **short_description**: One-line summary
- **effect**: Mechanical game rules

### Optional Fields
- **requirements.domain**: Combat domain requirement (e.g., "SH1" = Shield 1)
- **requirements.skills**: Skill prerequisites (e.g., ["Medicine 2"])
- **requirements.perks**: Other perk prerequisites
- **requirements.special**: Special requirements (e.g., ["GM permission"])
- **cost.ap**: Action point cost (usually combat perks only)
- **leveling.enabled**: Set to true for perks that can be taken multiple times
- **leveling.xp_formula**: Formula for calculating cost per level (e.g., "Max_Wounds * level")
- **leveling.max_level**: Maximum times perk can be taken (null = unlimited)
- **leveling.consolidation**: Special rules when reaching certain levels
- **flavor**: Narrative description (formerly "Description" section)

### Arrays (use [] for empty, not null)
- **requirements.skills**
- **requirements.perks**
- **requirements.special**
- **attributes**
- **tags**

## Examples by Subtype

### Combat Perk Example
```yaml
subtype: combat
name: Shield Rush
id: shield-rush
requirements:
  domain: SH1
  skills: []
  perks: []
  special: []
attributes:
  - Might
  - Endurance
  - Shield
cost:
  xp: 2
  ap: 4
tags:
  - Shield
  - Strike
```

### Skill Perk Example
```yaml
subtype: skill
name: Anatomical Knowledge
id: anatomical-knowledge
requirements:
  domain: null
  skills: ["Medicine 2", "Biology 2"]
  perks: []
  special: []
attributes:
  - Perception
  - Wit
cost:
  xp: 5
  ap: null
tags:
  - Knowledge
  - Combat
```

### Magic Perk Example
```yaml
subtype: magic
name: Mage
id: mage
requirements:
  domain: null
  skills: []
  perks: []
  special: ["GM permission"]
attributes:
  - Will
cost:
  xp: 5
  ap: null
leveling:
  enabled: false
  xp_formula: null
  max_level: null
  consolidation: null
tags:
  - Instant
  - Magic
```

### Multi-Level Perk Example (ExtraHP)
```yaml
subtype: skill
name: ExtraHP
id: extra-hp
requirements:
  domain: null
  skills: []
  perks: []
  special: []
attributes:
  - Endurance
  - Will
cost:
  xp: 0  # Not fixed - uses formula
  ap: null
leveling:
  enabled: true
  xp_formula: "Max_Wounds * level"
  max_level: null  # Can be taken unlimited times
  consolidation: "Every 5 levels consolidates into +1 Max_Wounds"
tags:
  - HP
  - Leveling
short_description: Increase health pool
effect: |
  Gain additional HP based on your current Max_Wounds.
  Cost: Max_Wounds × current level XP
  Consolidation: When ExtraHP level reaches 5, it consolidates into +1 Max_Wounds.
```
