**Requirements:** Requirement text or -
**Attributes:** AT1/AT2 or AT1/AT2+Domain
**Cost:** X XP
**Tags:** #Tag1 #Tag2 or -

## Short Description
Brief one-line description for tables and quick reference

## Grants
Use this section to embed the Ability or Effect this perk grants.

**Format:**
- `![[Ability - Name]]` - Active actions (have AP cost in the ability file)
- `![[Effect - Name]]` - Passive bonuses, conditional triggers, always-on modifications

## Description
Narrative description, lore, and context (optional - can be omitted if Grants section is sufficient)

---

# Template Usage Guide

## Header Fields (Always in this order)

### **Requirements:**
- Tier requirements: `Tier 1`, `Tier 2`, etc.
- Skill requirements: `Medicine 2`, `Biology 2/History 2`
- Perk prerequisites: `[[Shield Training]]`, `[[Footwork]]`
- Attribute requirements: `AG 2`, `MG 3`
- Special requirements: `GM permission`
- Multiple requirements: Separate with commas
- No requirements: Use `-`

**Examples:**
```
**Requirements:** Tier 1, [[Footwork]]
**Requirements:** Tier 2, AG 2
**Requirements:** Medicine 2
**Requirements:** -
```

### **Attributes:**
- Format: `AT1/AT2`
- NO brackets `[]` - keep it clean
- Use abbreviated form: `PR/WL`, `MG/EN`

**Abbreviations:**
- **Mental:** PR (Perception), WL (Will), CH (Charisma), WT (Wit)
- **Physical:** MG (Might), EN (Endurance), AG (Agility), DX (Dexterity)

**Examples:**
```
**Attributes:** PR/WT
**Attributes:** MG/EN
**Attributes:** AG/DX
```

### **Cost:**
- Always format: `X XP`
- For variable costs: `Variable (formula)`

**Examples:**
```
**Cost:** 5 XP
**Cost:** 10 XP
**Cost:** Variable (Max_Wounds × level)
```

### **Tags:**
- Use hashtags: `#Tag1 #Tag2`
- Keep tags minimal and meaningful
- Use `-` or leave empty if no tags

---

## Ability vs Effect Decision

**Use Ability when:**
- Player actively chooses to use it
- Has an AP cost
- Examples: Strike attacks, reactions, special moves

**Use Effect when:**
- Always on or triggers automatically
- No AP cost
- Examples: Stat bonuses, expanded crit ranges, passive auras

---

## Examples by Type

### Combat Perk (grants Ability)
```markdown
**Requirements:** Tier 1, [[Shield Training]]
**Attributes:** MG/EN
**Cost:** 2 XP
**Tags:**

## Short Description
Move twice and strike with shield.

## Grants

![[Ability - Shield Rush]]

## Description
You charge forward with shield raised, using momentum to deliver a devastating bash.
```

### Skill Perk (grants Effect)
```markdown
**Requirements:** Survival 2
**Attributes:** CH/WL
**Cost:** 5 XP
**Tags:**

## Short Description
Animals' starting attitude toward you is increased by +2.

## Grants

![[Effect - Animal Affinity]]

## Description
Cats and dogs love you more than others.
```

---

## Parser Notes

When parsing perk files:
1. **Extract title** from filename (not header - there is none)
2. **Parse header fields** (Requirements, Attributes, Cost, Tags)
3. **Extract embedded files** from `![[Ability - X]]` or `![[Effect - X]]`
4. **Detect leveling perks** by `Variable` in Cost field
5. **Infer type** from directory path
