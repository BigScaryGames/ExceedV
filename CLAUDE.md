# ExceedV TTXPG Core Rules Reference

> **Version Status:** This is a 0.4 → 0.5 WIP (Work in Progress)
> - Martial domain restructure in progress
> - Weapon training system implementation ongoing
> - Combat perk overhaul planned
> - Extra HP deprecation (replacing with Conditioning perks)

## Game Overview
- **System:** 2d10 dice system with advantage/disadvantage (3d10 keep 2)
- **Target Audience:** Skill-based fantasy TTXPG for players wanting more control than class-based systems
- **Key Features:**
  - Limit system prevents buff stacking
  - Skills and perks drive attributes (bottom-up design)
  - Armor as stamina multiplier
  - Bounded accuracy (skills/attributes capped at 5)

## Core Resolution Mechanics

### Dice System
- **Standard Roll:** 2d10 + Skill + Attribute + Bonuses/Penalties
- **Advantage:** 3d10 take 2
- **Disadvantage:** 3d10 keep 2 lowest
- **Criticals:** Doubles on kept dice (success → critical success, failure → critical failure)

### Check Types
- **Unopposed:** Roll result ≥ DC = Success
- **Opposed:** Higher roll wins, doubles create critical success
- **Skill Applications:**
  - Direct skill use: Full skill bonus
  - Raw attribute: Attribute only
  - Related skill: -1 to -3 penalty
  - Creative alternatives: GM discretion

## Character Creation

### Steps
1. **Concept:** Name and character concept
2. **Starting XP:** GM awards Combat XP and Skill XP separately
3. **Spend XP:** Skills, perks, spells (each shows which attributes benefit)
4. **Calculate Bonus Actions:** Every 5 Mental/Physical attribute points = +1 action of that type
5. **Starting Gear:** Equipment and final statistics

### Attribute System
- **8 Core Attributes:** Perception, Will, Charisma, Wit, Might, Endurance, Agility, Dexterity
- **Cannot buy directly:** Only increase through skills/abilities
- **Threshold Progression:** 10/30/60/100/150 points = +1 to attribute
- **Mental Actions:** Every 5 total Mental attributes = +1 Mental AP
- **Physical Actions:** Every 5 total Physical attributes = +1 Physical AP

### Skill Progression
- **Regular Skills:** 2/+4/+6/+8/+10 XP per level
- **Domains (Special Skills):**
  - Spellcraft: 10/+20/+30/+40/+50 XP (progressed by learning spells)
  - Martial Domain: 10/+20/+30/+40/+50 XP (progressed by learning perks and weapon training)

### Weapon Training System (v0.5)
- **8 Weapon Categories:** Brawling, Shield, Blades, Axes, Impact, Polearms, Bows, Thrown
- **Untrained Penalty:** -2 to use weapons without training
- **Training Perks:** 5 XP each, grants proficiency + category-specific bonus
  - **Blades:** Expanded crit range (beat defense by 10+ = crit)
  - **Shield:** Shield Block reaction (damage reduction on failed blocks)
  - **Brawling:** 2 AP and 3 AP unarmed attacks (supplementary)
  - **Polearms:** Ready strikes cost -1 AP (defensive stance)
  - **Axes:** Overswing (Reaction: +2 vs Block defense when declared)
  - **Thrown:** Skirmisher's Strike (Step back as part of thrown attack, once per turn)
  - **Bows:** Learn Aim action (works with all ranged weapons)
  - **Impact:** Shoving Strike (+1 AP; on hit target rolls Endure or shoved 1m/2m on crit)

### Combat Perk Trees (v0.5)
Combat perks with 5+ interconnected requirements form perk trees organized into subfolders.

#### Shield Tree (`Perks/CombatPerks/Shields/`)
**Base Requirement:** Shield Training (from WeaponTraining)

**Tier 1 (5-10 XP):**
- Shield Warden (5 XP, PR/EN) - Use Shield Block to protect allies taking damage
- Shield Rush (2 XP, MG/EN, req: MG1) - Move and strike with shield, adding Might to damage twice
- Multipurpose Shield (3 XP, AG/MG) - Strike with shield boss without losing defensive bonus

**Tier 2 (3-10 XP):**
- Shield Guardian (10 XP, PR/AG, req: Shield Warden) - Block attacks targeting adjacent allies
- Spell Guard (5 XP, PR/AG) - Block magical effects and spells with shield
- Perfect Block (5 XP, MG/EN) - Critical block makes attacker off-guard
- Behind the Shield Strike (3 XP, AG/CH) - Strike from behind shield with enemy penalties to defense

**Tier 3 (10-15 XP):**
- The Wall (15 XP, EN/MG, req: Shield Warden) - Allow adjacent allies to hide behind you and heavy shield
- The Guardian Aura (10 XP, EN/MG, req: Spell Guard + Shield Warden) - Provide defensive advantages to allies within aura range

**Tree Branches:**
- **Guardian Branch:** Shield Training → Shield Warden → Shield Guardian / The Wall
- **Spell Defense Branch:** Shield Training → Spell Guard → Guardian Aura (also requires Shield Warden)
- **Offensive Techniques:** Shield Training → Shield Rush / Multipurpose Shield / Behind Shield Strike
- **Defensive Tech:** Shield Training → Perfect Block

## Hit Points & Health

### HP Pools
- **Stamina:** (Armor + Endurance) × Max Wounds (depleted first)
- **Health:** HP Per Wound × Max Wounds + Extra HP
- **Starting:** 2 Max Wounds, 5 HP Per Wound

### Increasing HP
- **Extra HP Perk (v0.4, deprecated in v0.5):** Max_Wounds × XP per level
- **Consolidation:** Every 5 Extra HP levels → +1 Max Wound
- **v0.5 Replacement:** Conditioning perks (same mechanics, thematic capstone rewards)
  - Poison Resistance, Waterfall Training, Mental Resilience, Cold/Heat Conditioning, Battle Scarred, Magical Conditioning

## Combat System

### Action Economy
- **Base:** 5 AP + 1 Reaction per turn
- **Reaction Usage:** Reduces next turn's AP by 1
- **Initiative:** 2d10 + Perception
- **Surprise/Ambush:** Coordinated initiative, stunned targets lose 3 AP

### Defenses
- **Parry:** Martial Domain + Agility/Dexterity
- **Block:** Shield Domain + Agility/Endurance/Might (also: magical barriers, natural armor, some monsters)
- **Dodge:** Agility + Perception
- **Endure:** Endurance + Will

### Combat Resolution Sequence (v0.5)
1. **Attacker declares activity:** "I swing at you"
2. **Defender declares defense type:** "I Block/Dodge/Parry/Endure"
3. **Attacker declares pre-roll boosts:** Spending reactions, stances, abilities
4. **Defender declares pre-roll boosts and reactions:** Defensive abilities, buffs
5. **Both roll**
6. **Resolve outcome**

### Defense Applications by Attack Type
- **Strike:** Parry, Block, Dodge (melee, touch spells)
- **Projectile:** Block, Dodge (arrows, ranged spells)
- **Burst:** Dodge only (explosions, AoE)
- **Mental:** Endure (fear, charm, mind control)
- **Physical:** Endure (poison, disease, exhaustion)

### Attacks & Damage
- **Weapon Stats:** Agility for all, Heavy allows Might, Finesse allows Dexterity
- **Ranged:** Dexterity or Perception based on weapon
- **Damage:** Weapon Dice + Might + Bonuses
- **Damage Dice by Skill:** 1-2 skill = 1 die, 3-4 skill = 2 dice, 5+ skill = 3 dice
- **Weapon AP Costs:** Light = 2 AP, Normal = 3 AP, Heavy = 4 AP

## Magic System

### Core Principles
- **Mage Requirement:** Must have Mage perk (GM permission)
- **Two Types:** Passive (uses Limit) vs Active (requires casting roll)
- **Limit Stat:** 3 + Will + Spellcraft (capacity for persistent effects)
- **Active Casting:** 2d10 + Spellcraft + Wit vs DC [8 + Tier × 2]

### Spellcraft Domain
- **Progression:** Learning spells advances the domain
- **Tier Unlocks:** Each Spellcraft level unlocks new spell tiers
- **Learning Requirements:** Magical Theory/Theology ≥ spell tier (or teacher)
- **Learning Time:** 1 day per XP spent

### Spell Costs by Tier
| Tier | Basic | Advanced | XP to Next Tier |
|------|-------|----------|-----------------|
| 0    | 1     | 3        | -               |
| 1    | 3     | 5        | 10              |
| 2    | 5     | 7        | +20             |
| 3    | 7     | 10       | +30             |
| 4    | 10    | 15       | +40             |
| 5    | 15    | 25       | +50             |

## Skills List

### Social Skills
- Dancing (Agility/Charisma), Negotiating (Charisma/Wit), Manipulation (Charisma/Will)
- Leadership (Charisma/Will), Fast-talk (Charisma/Agility), Singing (Endurance/Charisma)
- Gossip (Charisma/Perception), Intimidation (Charisma/Might), Acting (Charisma/Will)

### Athletic Skills
- Running (Agility/Endurance), Climbing (Might/Agility), Swimming (Endurance/Might)
- Jumping (Might/Agility), Acrobatics (Agility/Dexterity), Lifting (Might/Endurance)
- Breaking (Might/Wit)

### Knowledge Skills
- Magical Theory (Wit/Will), History (Wit/Will), Theology (Will/Charisma), Streetwise (Charisma/Perception)

### Other Categories
- **Crafting:** Smithing, Woodworking, Textilework, Engineering
- **Sciences:** Biology, Chemistry, Medicine
- **Stealth/Criminal:** Stealth, Lockpicking, Sleight of Hand
- **Wilderness:** Survival, Tracking, Navigation

## Traits System

### Defense Traits
- **#Strike:** Block, Parry, Dodge
- **#Projectile:** Block, Dodge (Parry with perks)
- **#Burst:** Dodge (Block/Parry with perks)
- **#Mind:** Endure
- **#Body:** Endure

### Effect Types
- **#Boon:** Beneficial effects
- **#Bane:** Detrimental effects
- **#Protection:** Damage mitigation
- **#Healing:** Health restoration

### Bonus Types (Stacking Rules)
- **Same type:** Don't stack, take higher
- **Different types:** Stack together
- **Types:** #Competence, #Morale, #Enhancement, #Luck/#Unluck, #Equipment, #Situational, #Armor, #Size

## Social Interactions

### Attitude System
- **Range:** -5 (hostile) to +5 (fanatical adoration)
- **Factors:** Race, appearance, social class, rank
- **Favor Costs:** Attitude affects price (negative = higher cost, positive = lower/free)

### Social Actions
- **Affect Attitude:** Social skill + Charisma vs target's resistance
- **Detect Falsehood:** Perception + Manipulation or Perception + Will
- **Fast-Talk:** Fast-talk vs Detect Falsehood or Perception/Will

### Trading
- **Base Prices:** Pawn shops buy 50%, sell 100% of listed price
- **Attitude Modifier:** ±5% per attitude step
- **Bargaining Range:** 25-125% of listed price based on attitude

## Key Actions

### Movement (1 AP each)
- **Step:** 1m, no reactions provoked
- **Stride:** Speed/2 rounded up
- **Run:** Full speed (after striding)

### Combat Actions
- **Basic Attack:** 2-4 AP based on weapon weight
- **Ready (v0.5):** Variable AP (activity cost) - prepare action with trigger, execute as Reaction
  - Examples: Ready strike, ready spell, ready movement
  - Most combat preparations are obvious to observers
- **First Aid:** 4 AP, Medicine skill
- **Aid:** 2+R AP, provides bonus to ally

### Social Actions
- **Demoralize:** 1 AP, Intimidation vs Endure
- **Deduce:** 1 AP, knowledge skills for information

## Design Philosophy
- **Bounded Accuracy:** Skills/attributes max at 5
- **Positive Feedback:** Higher skills → higher attributes → better performance
- **Player Agency:** Choose attribute increases when raising skills
- **Resource Management:** Limit system for magical effects
- **Tactical Depth:** Multiple defense options and action economy choices

---

# CODEBASE DOCUMENTATION

## File Structure Overview

### Main Ruleset Files
- `Ruleset/1. General.md` - Game overview, quick reference, design notes
- `Ruleset/2. Basic Mechanics.md` - Core 2d10 system, dice mechanics, check types
- `Ruleset/3. Character Creation and Point buy Costs.md` - XP system, character creation steps
- `Ruleset/3.1 Attributes.md` - 8-attribute system, skill-driven progression
- `Ruleset/3.2 HP And Wounds.md` - Dual HP pools (Stamina/Health), wound system
- `Ruleset/3.4 Learning and Training.md` - Downtime training, XP progression variants
- `Ruleset/4. Combat Conflict Resolution.md` - Action economy, attacks, defenses, initiative
- `Ruleset/4.1 Taking Damage.md` - Damage application rules
- `Ruleset/4.2 Wounds And Consequences.md` - Wound effects and consequences
- `Ruleset/5. Skills.md` - Complete skill list with attribute pairings
- `Ruleset/5.1 Skill And Universal Perks.md` - Skill progression, universal perks
- `Ruleset/6. Magic System.md` - Limit system, spellcraft domain, spell learning
- `Ruleset/6.1 Magic Perks.md` - Magic-related perks and abilities
- `Ruleset/6.1 Summoning.md` - Summoning mechanics and rules
- `Ruleset/7. Equipment.md` - Weapons, armor, gear mechanics
- `Ruleset/7.1 Encumbrance.md` - Carrying capacity, weight penalties
- `Ruleset/8. Social Interactions.md` - Attitude system, social mechanics, trading
- `Ruleset/8.1 Rank and Status.md` - Social hierarchy, status mechanics
- `Ruleset/9. Movement and Distance.md` - Speed calculation, movement actions
- `Ruleset/10. Traits.md` - Spell/ability traits, defense types, bonus stacking
- `Ruleset/11. Actions.md` - Combat, social, knowledge, and support actions

### Combat System Files
- `Ruleset/Combat Skills and perks/1. Martial Domains.md` - Combat skill domains (v0.4, being restructured)
- `Ruleset/Combat Skills and perks/0 Combat Perk Template.md` - Template for combat perks
- `Ruleset/Combat Skills and perks/Perks/` - Individual combat perk definitions
- `Ruleset/Combat Skills and perks/Conditions/` - Status effects and conditions
- `Ruleset/Perks/CombatPerks/WeaponTraining/` - Weapon training perks (v0.5)
- `Ruleset/Perks/CombatPerks/Conditioning/` - Conditioning perks for HP progression (v0.5)
- `Ruleset/Perks/CombatPerks/Shields/` - Shield perk tree (v0.5)
- `Ruleset/Combat Perk Design Guidelines.md` - Comprehensive perk design document

### Spell System Files
- `Ruleset/Spells/` - Individual spell definitions organized by tier
- `Ruleset/Universal Spell Template.md` - Template for creating new spells
- `Ruleset/Team Ritual.md` - Team formation and ritual mechanics

### Perk System Files
- `Ruleset/Perks List/` - Individual perk definitions
- `Ruleset/Perks List/UNEDITED/` - Perks pending revision

### Special Character Files
- `Ruleset/Mage.md` - Mage character type and requirements

### Design Documentation
- `Ruleset/Design Guidelines.md` - Design philosophy and guidelines

## Quick Search Patterns

### Finding Core Mechanics
- **Dice System:** Search `2d10`, `advantage`, `disadvantage`, `doubles`
- **Attributes:** Search `Perception`, `Will`, `Charisma`, `Wit`, `Might`, `Endurance`, `Agility`, `Dexterity`
- **Combat:** Search `AP`, `action points`, `initiative`, `parry`, `block`, `dodge`, `endure`
- **Magic:** Search `Limit`, `spellcraft`, `persistent`, `active spell`

### Finding Specific Rules
- **Character Creation:** Files 3.x, search `XP`, `Experience Points`
- **Combat Resolution:** File 4, search `attack`, `damage`, `defense`
- **Health System:** Files 3.2, 4.1, 4.2, search `HP`, `stamina`, `health`, `wounds`
- **Skills:** File 5, search skill names or `(Attribute/Attribute)` pattern
- **Magic Rules:** Files 6.x, search `tier`, `spell`, `casting`
- **Social Rules:** Files 8.x, search `attitude`, `favor`, `negotiation`

### Finding Content by Type
- **Perks:** `Ruleset/Perks List/` or `Ruleset/Combat Skills and perks/Perks/`
- **Spells:** `Ruleset/Spells/` organized by tier folders
- **Conditions:** `Ruleset/Combat Skills and perks/Conditions/`
- **Templates:** Search `Template.md` for creation guidelines

### Search by Game Element
- **Specific Skill:** Search skill name in File 5 or related perk files
- **Combat Mechanics:** Files 4.x, search `strike`, `projectile`, `burst`, `mental`, `physical`
- **Equipment Rules:** Files 7.x, search weapon/armor names or `encumbrance`
- **Movement:** File 9, search `speed`, `step`, `stride`, `run`

### Trait and Tag Searches
- **Defense Traits:** Search `#Strike`, `#Projectile`, `#Burst`, `#Mind`, `#Body`
- **Effect Types:** Search `#Boon`, `#Bane`, `#Protection`, `#Healing`
- **Magic Schools:** Search `#Spell`, `#Conjuration`, `#Manipulation`, `#Transformation`
- **Bonus Types:** Search `#Competence`, `#Morale`, `#Enhancement`, `#Luck`

## File Status Notes (v0.4 → v0.5 WIP)
- **Modified Files:** Several core files have recent changes (per git status)
- **Unedited Content:** Some perks in `/UNEDITED/` folder need revision
- **New Content:** Recent additions in combat perks and main perk list
- **v0.5 Progress:**
  - ✅ Ready action implemented (11. Actions.md)
  - ✅ Weapon training structure defined (8 categories, 5 XP each)
  - ✅ All weapon training perks complete: Blades, Shield, Brawling, Polearms, Axes, Thrown, Bows, Impact
  - ✅ Conditioning perks: Replace Extra HP system (7 conditioning types with leveled progression and capstones)
  - ✅ Shield perk tree organized (9 perks in 3 tiers, based on Shield Training)
  - ⏳ Combat perk overhaul: Convert from old domains to weapon trait requirements
  - ⏳ Combat perk tree organization: Shields complete, Leadership/Parrying/other trees pending
  - ⏳ Archery domain remake (flagged for later)

## Development Workflow
- **Templates:** Use Universal templates before creating new content
- **Git Status:** Check git status for recent changes and untracked files
- **Cross-References:** Many files link to each other using `[[filename]]` notation

## Ability & Effect System (GAS-Inspired)

### Naming Convention
The system uses Unreal Engine GAS (Gameplay Ability System) naming conventions:
- **Abilities:** Active actions players choose to use (files prefixed with `Ability - `)
- **Effects:** Passive bonuses, triggers, or ongoing modifications (files prefixed with `Effect - `)

### File Structure
```
/Ruleset/Abilities/Ability - Name.md    → Contains ability mechanics only
/Ruleset/Effects/Effect - Name.md       → Contains effect mechanics only
/Ruleset/Perks/Category/Perk Name.md    → Contains XP cost, requirements, embeds ability/effect
```

### Ability vs Effect Decision Tree
- **Is it an active choice the player makes?** → Ability
  - Examples: Strike attacks, reactions, castable spells, preparing actions
- **Is it always on or triggers automatically?** → Effect
  - Examples: Stat bonuses, expanded crit ranges, passive auras, conditional triggers

### File Format

**Ability Files** (`Ability - Name.md`):
```markdown
Description of what the ability does and how it works.

**Tags:** #RelevantTags #ForMechanics
```

**Effect Files** (`Effect - Name.md`):
```markdown
Description of what the effect does and when it applies.

**Tags:** #Passive #RelevantTags
```

**Perk Files** (embed abilities/effects):
```markdown
# Perk Name

**Requirements:** Prerequisites
**Attributes:** Affected attributes
**Cost:** XP cost
**AP Cost:** Action point cost (or -)
**Tags:** #Category #Type

## Short Description
Brief one-liner

## Grants

![[Ability - Name]]

## Description
Flavor text
```

### Why This Structure?
1. **No Duplication:** Ability/effect mechanics live in one file only
2. **Reusability:** Multiple perks can grant the same ability/effect
3. **Clean Embedding:** Obsidian shows "Ability - Name" as title (clear type indicator)
4. **Parser-Friendly:** Files identifiable by `Ability - ` or `Effect - ` prefix
5. **No Recursion:** Perk files and ability/effect files have different names

### Creating New Abilities/Effects
1. Determine if it's an Ability (active) or Effect (passive)
2. Create file in `/Ruleset/Abilities/` or `/Ruleset/Effects/`
3. Name file: `Ability - Descriptive Name.md` or `Effect - Descriptive Name.md`
4. Write mechanics (no "Ability:" or "Effect:" label needed - filename shows type)
5. Add relevant tags for mechanics (NOT perk-level tags like #Combat)
6. In perk file, embed with `![[Ability - Name]]` or `![[Effect - Name]]`

### Tag Conventions
**Perk-level tags** (in perk file):
- `#Combat`, `#Skill`, `#Magic`, `#Universal`
- `#WeaponTraining`, `#Shield`, `#StavesSpears`, etc.

**Mechanic tags** (in ability/effect file):
- `#Strike`, `#Projectile`, `#Burst`, `#Reaction`
- `#Passive`, `#Dodge`, `#Parry`, `#Block`, `#Endure`
- `#Damage`, `#Healing`, `#Buff`, `#Debuff`
- `#AoE`, `#Melee`, `#Ranged`, `#Movement`
- dont put random tags where they don't belong.
- don't write the name of the file in the first line of the file as a header. Name of the file is a header already.