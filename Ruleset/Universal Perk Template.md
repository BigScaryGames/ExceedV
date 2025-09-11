# Universal Perk Template for App Export

This document defines a standardized structure for all perks in the Exceed TTRPG system, designed for easy export to digital applications.

## Category Structure

The template uses 3 main categories based on how players search for perks:
- **Skill** - All non-combat skills (medicine, stealth, knowledge, social, wilderness, status, etc.)
- **Martial** - Combat domains and fighting abilities
- **Magic** - Spellcraft and supernatural perks

This grouping matches how players actually think about character building and perk selection.

## Template Schema

```json
{
  "id": "string (unique_identifier)",
  "name": "string (display_name)",
  "category": "string (skill|martial|magic)",
  "subcategory": "string (optional - specific domain or skill type)",
  "tier": "integer (0-5, representing power level)",
  "cpCost": "integer (base cost in character points)",
  "variableCost": "boolean (true if cost varies by level/circumstances)",
  "costFormula": "string (describes variable cost calculation)",
  "requirements": {
    "skills": [
      {
        "name": "string (skill name)",
        "level": "integer (minimum level required)"
      }
    ],
    "attributes": [
      {
        "name": "string (attribute abbreviation)",
        "level": "integer (minimum level required)"
      }
    ],
    "domains": [
      {
        "name": "string (domain name)",
        "level": "integer (minimum level required)"
      }
    ],
    "perks": ["array of prerequisite perk names"],
    "special": ["array of special requirements like GM permission"],
    "misc": "string (other requirements like reputation)"
  },
  "attributeBonuses": {
    "bonuses": ["array of attribute bonuses granted"],
    "formula": "string (how bonuses are applied)"
  },
  "gameplayType": ["array of gameplay archetypes this supports"],
  "shortDescription": "string (brief summary for lists and tooltips)",
  "longDescription": "string (complete mechanical and narrative description)",
  "tags": ["array of mechanical tags"],
  "restrictions": ["array of limitations or conflicts"],
  "linkedPerks": {
    "prerequisites": ["array of prerequisite perk IDs"],
    "unlocks": ["array of perks this unlocks"],
    "conflicts": ["array of conflicting perk IDs"]
  },
  "mechanics": {
    "actionType": "string (reaction|free|standard|passive|none)",
    "apCost": "integer (action point cost, if applicable)",
    "duration": "string (instant|turn|combat|permanent)",
    "range": "string (self|adjacent|speed|unlimited)",
    "targeting": "string (self|ally|enemy|area)"
  },
  "notes": "string (design notes or clarifications)",
  "status": "string (complete|wip|concept|deprecated)"
}
```

## Example Perks

### Martial Perk Example
```json
{
  "id": "riposte",
  "name": "Riposte",
  "category": "martial",
  "subcategory": "universal",
  "tier": 2,
  "cpCost": 5,
  "variableCost": false,
  "costFormula": null,
  "requirements": {
    "skills": [],
    "attributes": [
      {"name": "AG", "level": 3}
    ],
    "domains": [
      {"name": "Any Martial Domain", "level": 3}
    ],
    "perks": [],
    "special": [],
    "misc": null
  },
  "attributeBonuses": {
    "bonuses": [],
    "formula": null
  },
  "gameplayType": ["duelist", "defender"],
  "shortDescription": "Counter-attack when enemy fails or you succeed critically on defense",
  "longDescription": "You know how to capitalize on enemy mistakes. When an enemy critically fails on his attack or you critically succeed defending against it, make a strike against the enemy as a reaction.",
  "tags": ["reactive", "counter-attack"],
  "restrictions": [],
  "linkedPerks": {
    "prerequisites": [],
    "unlocks": [],
    "conflicts": []
  },
  "mechanics": {
    "actionType": "reaction",
    "apCost": 0,
    "duration": "instant",
    "range": "weapon_reach",
    "targeting": "enemy"
  },
  "notes": "Triggers on critical defense success or enemy critical failure",
  "status": "complete"
}
```

### Skill Perk Example
```json
{
  "id": "first_aid",
  "name": "First Aid",
  "category": "skill",
  "subcategory": "medicine",
  "tier": 1,
  "cpCost": 5,
  "variableCost": false,
  "costFormula": null,
  "requirements": {
    "skills": [
      {"name": "Medicine", "level": 1}
    ],
    "attributes": [],
    "domains": [],
    "perks": [],
    "special": [],
    "misc": null
  },
  "attributeBonuses": {
    "bonuses": [],
    "formula": null
  },
  "gameplayType": ["healer", "support"],
  "shortDescription": "Restore HP without supplies once per person per day",
  "longDescription": "Basic medical training allows emergency treatment. Restore HP without supplies once per person per day using improvised methods and knowledge of anatomy.",
  "tags": ["healing", "utility", "limited_use"],
  "restrictions": ["Once per person per day"],
  "linkedPerks": {
    "prerequisites": [],
    "unlocks": ["surgeons_precision"],
    "conflicts": []
  },
  "mechanics": {
    "actionType": "standard",
    "apCost": null,
    "duration": "instant",
    "range": "adjacent",
    "targeting": "ally"
  },
  "notes": "Basic healing without requiring medical supplies",
  "status": "complete"
}
```

### Skill Perk Example (Status)
```json
{
  "id": "licensed_healer",
  "name": "Licensed Healer",
  "category": "skill",
  "subcategory": "status",
  "tier": 1,
  "cpCost": 5,
  "variableCost": true,
  "costFormula": "5 per level (1-5)",
  "requirements": {
    "skills": [
      {"name": "Medicine", "level": 1}
    ],
    "attributes": [],
    "domains": [],
    "perks": [],
    "special": [],
    "misc": "Must be taken at appropriate skill levels"
  },
  "attributeBonuses": {
    "bonuses": [],
    "formula": null
  },
  "gameplayType": ["social", "professional"],
  "shortDescription": "Legal medical practice and noble preferential treatment",
  "longDescription": "Official recognition as a medical practitioner grants legal authority to practice medicine and preferential treatment from nobility who value your professional services.",
  "tags": ["social", "legal_authority", "scalable"],
  "restrictions": ["Must maintain professional standards"],
  "linkedPerks": {
    "prerequisites": [],
    "unlocks": [],
    "conflicts": []
  },
  "mechanics": {
    "actionType": "passive",
    "apCost": 0,
    "duration": "permanent",
    "range": "self",
    "targeting": "self"
  },
  "notes": "Provides legal authority and social standing",
  "status": "complete"
}
```

## Field Documentation

### Core Identity
- **id**: Unique identifier for database storage and cross-referencing
- **name**: Display name shown to players
- **category**: Primary classification for filtering and organization
- **subcategory**: Secondary classification for specific domains or skill types
- **tier**: Power level indicator (0=basic, 5=legendary)

### Cost Structure
- **cpCost**: Base character point investment required
- **variableCost**: Boolean indicating if cost scales with level or circumstances
- **costFormula**: Human-readable description of variable cost calculation

### Requirements System
- **skills**: Minimum skill levels needed
- **attributes**: Minimum attribute values required
- **domains**: Martial domain prerequisites
- **perks**: Other perks that must be taken first
- **special**: GM permission, deity relationships, etc.
- **misc**: Reputation, published works, or other narrative requirements

### Mechanical Integration
- **attributeBonuses**: Permanent bonuses this perk grants to character attributes
- **gameplayType**: Supported playstyles for character building recommendations
- **mechanics**: Action economy details for precise implementation

### Relationships
- **linkedPerks**: Prerequisite chains, unlocked options, and conflicts for dependency management

## Conversion Guidelines

### From Existing Table Format
1. **Name** → `name`
2. **Requirements** → Parse into appropriate `requirements` subcategories
3. **Attr** → Parse into `attributeBonuses` if granting bonuses, otherwise may indicate roll formula
4. **CP Cost** → `cpCost` and `variableCost`/`costFormula` if applicable
5. **Description** → Use as `shortDescription`, expand with context for `longDescription`

### Category Mapping
- Universal Combat → `category: "martial", subcategory: "universal"`
- One-Handed perks → `category: "martial", subcategory: "one_handed"`
- Medicine perks → `category: "skill", subcategory: "medicine"`
- Street Wisdom → `category: "skill", subcategory: "criminal"`
- Wilderness perks → `category: "skill", subcategory: "wilderness"`
- Stealth perks → `category: "skill", subcategory: "stealth"`
- Status perks → `category: "skill", subcategory: "status"`
- Social perks → `category: "skill", subcategory: "social"`
- Magic perks → `category: "magic", subcategory: varies`

### Special Considerations
- **GM Requirements**: Add to `requirements.special` array
- **Variable Costs**: Set `variableCost: true` and describe in `costFormula`
- **Instant Perks**: Mark as `tags: ["instant"]` and note no training required
- **Paired Perks**: Use `linkedPerks` to establish master/follower relationships

This template ensures all perk data can be systematically exported while maintaining the mechanical complexity and narrative richness of the Exceed system.