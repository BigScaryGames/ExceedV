# Perk Name

**Requirements:** Requirement text or -
**Attributes:** AT1/AT2 or AT1/AT2+Domain
**Cost:** X XP
**AP Cost:** X or -
**Tags:** #Tag1 #Tag2 or -

## Short Description
Brief one-line description for tables and quick reference

## Effect
Mechanical effects of the perk - what it does in game terms

## Description
Narrative description, lore, and context (optional - can be omitted if Effect is sufficient)

---

# Template Usage Guide

## Header Fields (Always in this order)

### **Requirements:**
- Skill requirements: `Medicine 2`, `Biology 2/History 2`
- Domain requirements: `SH1`, `OH2`, `AR3`
- Perk prerequisites: `Shield Block, Shield Warden`
- Special requirements: `GM permission`, `Must be in water`
- Multiple requirements: Separate with commas
- No requirements: Use `-`

**Examples:**
```
**Requirements:** Medicine 2
**Requirements:** SH1
**Requirements:** Shield Block, Medicine 2
**Requirements:** GM permission
**Requirements:** -
```

### **Attributes:**
- Format: `AT1/AT2` or `AT1/AT2+Domain`
- NO brackets `[]` - keep it clean
- Use abbreviated form: `PR/WL`, `MG/EN+SH`
- Domains added with `+`: `AG/DX+OH` (Agility/Dexterity + One-Handed)

**Abbreviations:**
- **Mental:** PR (Perception), WL (Will), CH (Charisma), WT (Wit)
- **Physical:** MG (Might), EN (Endurance), AG (Agility), DX (Dexterity)
- **Domains:** SH (Shield), OH (One-Handed), TH (Two-Handed), AR (Archery), SP (Spear), ST (Staff)

**Examples:**
```
**Attributes:** PR/WT
**Attributes:** MG/EN+SH
**Attributes:** AG/DX+OH
**Attributes:** WL/WT
```

### **Cost:**
- Always format: `X XP`
- For variable costs: `Variable (formula)`
- Never use just numbers or "P" suffix

**Examples:**
```
**Cost:** 5 XP
**Cost:** 10 XP
**Cost:** Variable (Max_Wounds × level)
```

### **AP Cost:**
- Number for action point cost
- `-` if not applicable (most non-combat perks)

**Examples:**
```
**AP Cost:** 2
**AP Cost:** 4
**AP Cost:** -
```

### **Tags:**
- Use hashtags: `#Tag1 #Tag2`
- Common tags: `#Combat`, `#Social`, `#Magic`, `#Instant`, `#Passive`, `#Leveling`
- Domain tags: `#Shield`, `#Archery`, `#OneHanded`
- Spell tags: `#Spellcraft`, `#Spellshape`
- Use `-` if no tags

**Examples:**
```
**Tags:** #Shield #Combat
**Tags:** #Social #Passive
**Tags:** #Instant
**Tags:** -
```

---

## Content Sections

### Short Description
- One-line summary
- Used in tables and quick reference
- Keep it under 100 characters if possible

### Effect
- Mechanical game rules
- What the perk does in concrete terms
- Include numbers, bonuses, conditions
- Can use bullet points for clarity

### Description (Optional)
- Narrative description
- Lore and context
- How it might manifest in-game
- Can be omitted if Effect section is self-explanatory

---

## Examples by Type

### Combat Perk
```markdown
# Shield Rush

**Requirements:** SH1
**Attributes:** MG/EN+SH
**Cost:** 2 XP
**AP Cost:** 4
**Tags:** #Shield #Strike

## Short Description
Move twice and strike with shield, adding Might to damage twice.

## Effect
Move twice (up to full movement), then strike with your shield.
Add Might bonus to damage twice.
Total cost: 4 AP (reduced from normal 5 AP for move + attack)

## Description
You charge forward with shield raised, using momentum to deliver a devastating bash.
```

### Skill Perk
```markdown
# Animal Affinity

**Requirements:** Survival 2
**Attributes:** CH/WL
**Cost:** 5 XP
**AP Cost:** -
**Tags:** #Social #Passive

## Short Description
Animals' starting attitude toward you is increased by +2.

## Effect
Animals' starting attitude with you is increased by 2.
You have a short window to negotiate with animals before combat begins.

## Description
One day you noticed that cats and dogs love you more than others. Unless on guarding duty they never bark at you or try to harm you, horses generally don't throw you off, even wild animals don't attack you instantly on sight, and may allow you to walk away.
```

### Magic Perk
```markdown
# Mage

**Requirements:** GM permission
**Attributes:** WL
**Cost:** 5 XP
**AP Cost:** -
**Tags:** #Instant #Magic

## Short Description
Awaken your magical talent and unlock spellcasting.

## Effect
- Select one Tier 0 spell and add it to your repertoire (this spell doesn't contribute to attribute advancement)
- You unlock Tier 0 spells for learning
- You can learn Team Ritual in one day with written guidance or one shift with help
- This perk requires GM permission and no time to learn
- Can be selected as part of character background

## Description
Everyone wants to bend reality to their will. Unlike most, you can, because you are a mage.

Perhaps you were trained by a journeyman or master mage, or maybe during a pivotal moment in your life, your talent awakened. You might have been a child lost in darkness who summoned light, a pilgrim whose exhaustion lightened their burden, or someone who willed wounds to stop bleeding.
```

### Leveling Perk
```markdown
# ExtraHP

**Requirements:** -
**Attributes:** EN/WL
**Cost:** Variable (Max_Wounds × level)
**AP Cost:** -
**Tags:** #Leveling #Passive

## Short Description
Increase your health pool (can be taken multiple times).

## Effect
Gain additional HP based on your current Max_Wounds.

**Cost Formula:** Max_Wounds × current level in ExtraHP
- Example: With 2 Max_Wounds, 1st level costs 2 XP, 2nd costs 4 XP, 3rd costs 6 XP

**Consolidation:** When ExtraHP reaches level 5, it consolidates into +1 Max_Wounds. The new wound operates like all others (gains full armor and endurance bonuses).

## Description
Through rigorous training and conditioning, you've expanded your body's resilience beyond normal limits.
```

---

## Parser Notes (for build-time tool)

When parsing these files, the build tool should:

1. **Extract title** from `# Perk Name`
2. **Parse header fields** (Requirements, Attributes, Cost, AP Cost, Tags)
3. **Extract sections** (Short Description, Effect, Flavor)
4. **Detect leveling perks** by `Variable` in Cost field
5. **Generate ID** from title (kebab-case)
6. **Infer type** from directory:
   - `Perks/CombatPerks/` → `combat`
   - `Perks/SkillPerks/` → `skill`
   - `Perks/MagicPerks/` → `magic`

**Output JSON structure:**
```json
{
  "type": "perk",
  "subtype": "combat",
  "id": "shield-rush",
  "name": "Shield Rush",
  "requirements": {
    "text": "SH1",
    "domain": "SH1",
    "skills": [],
    "perks": [],
    "special": []
  },
  "attributes": ["Might", "Endurance", "Shield"],
  "cost": {
    "xp": 2,
    "variable": false
  },
  "apCost": 4,
  "tags": ["Shield", "Strike"],
  "shortDescription": "Move twice and strike with shield...",
  "effect": "Move twice (up to full movement)...",
  "flavor": "You charge forward with shield raised..."
}
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
