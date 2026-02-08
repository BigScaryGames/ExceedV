# ExceedV TTXPG Core Rules Reference

> **Version Status:** Milestone 5 (v0.5) in progress
> See `/MILESTONES.md` for roadmap through v1.0

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
- **Screwed:** 1d10 (worst case - blinded, unconscious, severe curses)
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
  - Martial: 10/+20/+30/+40/+50 XP (progressed by learning perks and weapon training)

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

**Perk Folder Structure (`Perks/CombatPerks/`):**

**Weapon Trees (Complete):**
- `WeaponTraining/` - 8 weapon category training perks (Ax, Blades, Bow, Brawling, Impact, Polearms, Shield, Thrown)
- `Shields/` - Complete shield tree (9 perks: Shield Rush, Multipurpose Shield, Shield Warden, Perfect Block, Spell Guard, Shield Guardian, Behind the Shield Strike, The Wall, Guardian Aura)
- `Archery/` - Complete archery tree (15 perks: Aim, Double Shot, Fast Archer, Tower, Hair Trigger, Mobile Draw, Tower Defender, Artillery, Spell Shot, Overpowered Draw, Close Quarters Shooter, Defensive Archer, Zen Archer, Don't Turn Your Back On Me, WIP: Ricochet Shot, Storm of Arrows)
- `Footwork/` - Evasion and movement (8 perks: Footwork, Light Steps, Small Steps, Big Steps, Dodging Step, Elusive, Dodge-Roll, Dodge Behind Your Back)
- `Polearms/` - Polearm techniques (8 perks: Quarter-staff Adept, Walking Stick, Pointy Stick, Grip Switch, Spinning Staff, Monkey King Strike, Staff Acrobat, Spear Brothers)
- `Parrying And Riposte/` - Defensive counter-attacks (5 perks: Parry This Parry That, Painful Parry, Repose This Repose That, Riposte, Projectile Parry)
- `Dual Wielding/` - Two-weapon fighting (3 perks: Twin Parry, Double Strike, Ambidexterity)
- `Blades/` - Blade-specific techniques (3 perks: Ready Hand, Long Knives, The Edgelord)
- `Thrown/` - Thrown weapon techniques (2 perks: Throwing Hand, Throwing Distraction)

**Other Categories:**
- `Conditioning/` - HP progression perks (7 perks: Poison Resistance, Waterfall Training, Mental Resilience, Cold Conditioning, Heat Conditioning, Magical Conditioning, Battle Scarred)
- `Combat Maneuvers/` - Universal combat techniques (7 perks: Calf Strike, Tripping Strike, Piranha Strike, Mighty Charge, Follow-Up Strike, Two Birds, All the Birds)
- `Predictive/` - Experimental predictive combat system (6 files)

**Social/Universal (Loose files and folders):**
- `Leadership/` - Social leadership perks (4 perks: The Aspiring Hero, The Leader, The Cult Inner Member, The Cult Leader)
- Backstab, Plot Armor, Reactive, Reactive Strike, That Type of a Person, The Loner, Too Selfish, Watching your back

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
- **#Defend:** Generic trait for all defensive actions (Block, Parry, Dodge, Endure) - used for buffs like "All in Defense"

### Effect Types
- **#Boon:** Beneficial effects
- **#Bane:** Detrimental effects
- **#Protection:** Damage mitigation
- **#Healing:** Health restoration

### Bonus Types (Stacking Rules)
- **Same type:** Don't stack, take higher
- **Different types:** Stack together
- **Types:** #Competence, #Morale, #Enhancement, #Luck, #Equipment, #Situational, #Armor, #Size
- **Condition stacking:** Same condition = highest applies, opposites negate, different types stack
- **Condition range:** +3 to -3

## Conditions System

Conditions are stored in `/source/content/Rules/References/Conditions/` and defined in `4.3 Conditions.md`

### Duration Presets
1. **One-Time Use** - Next qualifying action (luck effects, feint Off-Guard)
2. **End of Turn** - Fades at turn end (Shaken, Flash Blinded)
3. **Until Removed** - Source specifies removal (Grabbed, Off-Guard while flanked, Dazzled until cleared)

### Enhancement Conditions (Attribute Modifiers)
- **Grace X:** ±X to Agility/Dexterity rolls
- **Vigor X:** ±X to Might/Endurance rolls
- **Focus X:** ±X to Willpower/Perception rolls
- **Sharpness X:** ±X to Charisma/Wit rolls
- **Quickened X:** ±X actions at start of turn

### Morale Conditions
- **Shaken X:** X morale penalty on all rolls
- **Inspired X:** X morale bonus on all rolls

### Luck Conditions
- **Jinxed:** Next roll at disadvantage
- **Blessed:** Next roll at advantage

### Situational Conditions
- **Prone:** Disadvantage on Martial Domain (attacks, Parry, Block). Advantage on Dodge/Endure vs #Projectile and #Burst. Cannot Step/Stride/Run - only Crawl or Stand Up.
- **Grabbed:** -2 to attacking/manipulating, intricate actions at disadvantage, no reach weapons vs grappler. Grappler releases free; grappled must Escape.
- **Off-Guard:** -1 to defend against attacks. Applied by effects like Flanked.
- **Blinded:** All sight-reliant checks are Screwed (1d10).
- **Dazzled:** All sight-reliant checks at disadvantage.
- **Unconscious:** Block/Parry/Dodge are Screwed, Perception at disadvantage.

### Rest Conditions
- **Fatigued X:** -X to all rolls, -2X to exploration/downtime. At Fatigue 4, unconscious.
- **Well Rested:** +1 to +3 to Downtime/Exploration until Fatigued or night's rest.

### DOT Conditions (Musings)
- Bleed X, Fragile X, Pinned X, Stunned X - to be defined

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
- **Crawl:** Move 1m while prone (1 AP)
- **Stand Up:** Remove Prone condition (2 AP)

### Combat Actions
- **Basic Attack:** 2-4 AP based on weapon weight
- **All in Defense:** 2 AP - Gain advantage on all #Defend actions until your next turn (requires no offensive action this turn)
- **Grapple:** 3 AP - Attempt to grab opponent (Brawling + Might/Agility vs defense). On success, both gain Grabbed condition.
- **Escape:** 1 AP - Attempt to break free from Grabbed condition (Athletics or Escape Artist vs grappler's Brawling)
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

### Core Rules Files (Wiki Structure)
Core Rules use wiki-style organization with hub files embedding mechanics from subfolders.


**Hub Files (numbered):**
- `source/content/Rules/0.Index.md` - Navigation index
- `source/content/Rules/1.0 Introduction.md` - Overview and introduction to ExceedV
- `source/content/Rules/2. Basic Mechanics.md` - Dice system, check types (embeds from Mechanics/)
- `source/content/Rules/3. Character Creation and Point buy Costs.md` - XP system, creation steps
- `source/content/Rules/3.1 Attributes.md` - 8-attribute system
- `source/content/Rules/3.2 Perks and Flaws.md` - Perks and flaws system
- `source/content/Rules/3.3 HP And Wounds.md` - Dual HP pools, wound system
- `source/content/Rules/4. Combat Conflict Resolution.md` - Action economy, attacks, defenses
- `source/content/Rules/4.1 Taking Damage.md` - Damage application
- `source/content/Rules/4.2 Wounds And Consequences.md` - Wound effects, treatment
- `source/content/Rules/4.3 Conditions.md` - Condition system
- `source/content/Rules/4.4 Weapons and Combat Training.md` - Weapon training and combat techniques
- `source/content/Rules/5. Skills.md` - Skill list with attribute pairings
- `source/content/Rules/5.1 Skill And Universal Perks.md` - Skill progression, universal perks
- `source/content/Rules/6. Magic System.md` - Magic system overview
- `source/content/Rules/6. Types of magic.md` - Limit system, spellcraft domain
- `source/content/Rules/6.1 Summoning.md` - Summoning mechanics
- `source/content/Rules/6.2 Magic Perks.md` - Magic-related perks
- `source/content/Rules/7. Equipment.md` - Weapons, armor, gear
- `source/content/Rules/7.1 Encumbrance.md` - Encumbrance system
- `source/content/Rules/8. Social Interactions.md` - Attitude system, trading
- `source/content/Rules/8.1 Organizations.md` - Ranks, org benefits/obligations (WIP till MS8)
- `source/content/Rules/9. Movement and Distance.md` - Speed, movement actions
- `source/content/Rules/9.1 Time and Travel.md` - Time and travel mechanics
- `source/content/Rules/9.2 Downtime and Training.md` - Training, recovery, income (embeds from Mechanics/)
- `source/content/Rules/9.3 Exploration and Out of combat Activities.md` - Exploration, downtime activities
- `source/content/Rules/10. Traits.md` - Traits, bonus types (embeds from References/)
- `source/content/Rules/11. Actions.md` - All action types (embeds from Actions/)

**Subfolders:**
- `source/content/Rules/Mechanics/` - Embeddable mechanic files (Action Points, Initiative, Recovery Rules, etc.)
- `source/content/Rules/Actions/` - Individual action definitions (Movement/, Combat/, Social/, Support/, Abilities/)
- `source/content/Rules/References/` - Reference tables (Bonus Types, Defense Traits, Downtime Quality, Rank System, Effects/, Conditions/)
- `source/content/Rules/Design Philosophy.md` - Design notes and rationale
### Combat System Files
- `source/content/Perks/CombatPerks/` - All combat perks organized into folders
- `source/content/Perks/SkillPerks/` - Skill-based perks
- `source/content/Perks/MagicPerks/` - Magic-related perks
- `source/content/Rules/Mechanics/Dual Wielding.md` - Dual wielding rules (WIP)
- `source/content/Design Guidelines.md` - Comprehensive perk design document

### Spell System Files
- `source/content/Spells/` - Individual spell definitions organized by tier
- `source/content/Spells/0 Spell Template.md` - Template for creating new spells
- `source/content/Spells/Rituals/Team Ritual.md` - Team formation and ritual mechanics

### Perk System Files
- `source/content/Perks/0 Universal Perk Template.md` - Template for creating new perks
- `source/content/Perks/CombatPerks/` - Combat perks organized by weapon/type
- `source/content/Perks/SkillPerks/` - Non-combat skill perks
- `source/content/Perks/MagicPerks/` - Magic system perks
- `source/content/Perks/UNEDITED/` - Perks pending revision

### Special Character Files
- `Ruleset/Mage.md` - Mage character type and requirements

### Design Documentation
- `source/content/Design Guidelines.md` - Design philosophy and guidelines

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
- **Perks:** `source/content/Perks/CombatPerks/`, `source/content/Perks/SkillPerks/`
- **Spells:** `source/content/Spells/` organized by tier folders
- **Conditions:** `source/content/Rules/References/Conditions/`
- **Effects:** `source/content/Rules/References/Effects/`
- **Abilities:** `source/content/Rules/Actions/Abilities/`
- **Templates:** Search `Template.md` for creation guidelines

### Search by Game Element
- **Specific Skill:** Search skill name in File 5 or related perk files
- **Combat Mechanics:** Files 4.x, search `strike`, `projectile`, `burst`, `mental`, `physical`
- **Equipment Rules:** Files 7.x, search weapon/armor names or `encumbrance`
- **Movement:** File 9, search `speed`, `step`, `stride`, `run`

### Trait and Tag Searches
- **Defense Traits:** Search `#Strike`, `#Projectile`, `#Burst`, `#Mind`, `#Body`, `#Defend`
- **Effect Types:** Search `#Boon`, `#Bane`, `#Protection`, `#Healing`
- **Magic Schools:** Search `#Spell`, `#Conjuration`, `#Manipulation`, `#Transformation`
- **Bonus Types:** Search `#Competence`, `#Morale`, `#Enhancement`, `#Luck`
- **Conditions:** Search `#Condition`, `#Situational`

## Milestones
See `/MILESTONES.md` for full roadmap.

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
/source/content/Perks/Category/Perk Name.md    → Contains XP cost, requirements, embeds ability/effect
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
- DONT ADD UNNEEDED TAGS
