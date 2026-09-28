# ExceedV TTXPG Core Rules Reference

> **Version Status:** Milestone 6 (v0.6) in progress - Lines and Zones transition
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
2. **Starting XP:** GM awards Battle XP and Life XP separately
3. **Spend XP:** Skills, perks, spells (each shows which attributes benefit)
4. **Calculate AP:** Base 5 AP + your highest domain tier (Prowess or Magery)
5. **Starting Gear:** Equipment and final statistics

### Attribute System
- **8 Core Attributes:** Perception, Will, Charisma, Wit, Strength, Endurance, Agility, Dexterity
- **Cannot buy directly:** Only increase through skills/abilities
- **Threshold Progression:** 10/30/60/100/150 points = +1 to attribute

### Skill Progression
- **Regular Skills:** 2/+4/+6/+8/+10 XP per level
- **Domains (Special Skills):**
  - Magery: 10/+20/+30/+40/+50 XP (progressed by learning spells)
  - Prowess: 10/+20/+30/+40/+50 XP (progressed by learning perks and weapon training)

### Weapon Training System (v0.6)
- **8 Weapon Categories:** Brawling, Shield, Blades, Axes, Impact, Polearms, Bows, Thrown
- **Untrained Penalty:** -2 to use weapons without training
- **Training Perks:** 5 XP each, grants proficiency + category-specific bonus
  - **Blades:** Expanded crit range (beat defense by 10+ = crit)
  - **Shield:** Shield Block reaction (damage reduction on failed blocks)
  - **Brawling:** 2 AP and 3 AP unarmed attacks (supplementary)
  - **Polearms:** Ready strikes cost -1 AP (defensive stance)
  - **Axes:** Overswing (Reaction: +2 vs Deflect defense when declared, -2 to attackers defends till the start of next turn)
  - **Thrown:** Skirmisher's Strike (Step back as part of thrown attack, once per turn)
  - **Bows:** Learn Aim action (works with all ranged weapons)
  - **Impact:** Shoving Strike (+1 AP, Impact or Unarmed; on hit target rolls Endure vs attack roll or is Shoved out of the skirmish)

### Battle Perk Trees (v0.6)
Battle perks with 5+ interconnected requirements form perk trees organized into subfolders.

**Perk Folder Structure (`Perks/Prowess/`):**

**Weapon Trees (Complete):**
- `WeaponTraining/` - 8 weapon category training perks (Ax, Blades, Bow, Brawling, Impact, Polearms, Shield, Thrown)
- `Shields/` - Complete shield tree (9 perks: Shield Rush, Multipurpose Shield, Shield Warden, Perfect Block, Spell Guard, Shield Guardian, Behind the Shield Strike, The Wall, Guardian Aura)
- `Archery/` - Complete archery tree (15 files: Double Shot, Fast Archer, Tower, Hair Trigger, Mobile Draw, Tower Defender, Artillery, Spell Shot, Overpowered Draw, Close Quarters Shooter, Defensive Archer, Zen Archer, Don't Turn Your Back On Me, Ricochet Shot, Storm of Arrows)
- `Footwork/` - Evasion and movement (9 perks: Footwork, Light Steps, Small Steps, Big Steps, Dodging Step, Elusive, Dodge-Roll, Dodge Behind Your Back, Come and Get Me)
- `Polearms/` - Polearm techniques (8 perks: Quarter-staff Adept, Walking Stick, Pointy Stick, Grip Switch, Spinning Staff, Monkey King Strike, Staff Acrobat, Spear Brothers)
- `Parrying And Riposte/` - Defensive counter-attacks (5 perks: Parry This Parry That, Painful Parry, Repose This Repose That, Riposte, Projectile Parry)
- `Dual Wielding/` - Two-weapon fighting (3 perks: Twin Parry, Double Strike, Ambidexterity)
- `Wrestling/` - Grappling tree (8 perks: Takedown, Drag Along, Wrestler's Control, Iron Grip, Counter Grab, Weapon Thief, Chokehold, Throw)
- `Blades/` - Blade-specific techniques (3 perks: Ready Hand, Long Knives, The Edgelord)
- `Thrown/` - Thrown weapon techniques (2 perks: Throwing Hand, Throwing Distraction)

**Other Categories:**
- `../Conditioning/` - HP progression perks, top-level `Perks/Conditioning/` (8 perks: Poison Resistance, Waterfall Training, Mental Resilience, Cold Conditioning, Heat Conditioning, Magical Conditioning, Battle Scarred, Bones of Steel) — advance no domain
- `Combat Maneuvers/` - Universal combat techniques (10 perks: Calf Strike, Tripping Strike, Piranha Strike, Mighty Charge, Follow-Up Strike, Sweep (was Two Birds), All the Birds, Throw Enemy; Duelist line: Spend Some Time with You, Just the Two of Us, You and I)
- `Shoving/` - Forced-movement strike line (4 perks: Herding Strike, Home Run, Bowling Strike, WIP Rocket Strike; builds on basic Shove action + Shoving Strike)
- `Predictive/` - Experimental predictive combat system (6 files: Predicted Exchange, Predictive Defense, Predictive Strike, Reactive Prediction, WIP Predict A Perfect Ambush, WIP Predicted Duel)

**Defensive/Social (Loose files and folders):**
- `Defender/` - Protective loose perks, no domain (Defender, Too Selfish, Watching your back) - any Battle XP buyer can take them, mages included
- Backstab, Reactive Strike (Into the Battle is now Life XP)
- Leadership lives in `Perks/LifePerks/Leadership/` (The Aspiring Hero, The Leader, The Cult Inner Member, The Cult Leader)

## Hit Points & Health

### HP Pools
- **Stamina:** (Armor + Endurance) × Max Wounds (depleted first)
- **Health:** HP Per Wound × Max Wounds (+ bonuses from effects, e.g. Conditioning stages)
- **Starting:** 2 Max Wounds, 5 HP Per Wound

### Increasing HP
- **Extra HP Perk (v0.4, deprecated in v0.5):** Max_Wounds × XP per level
- **Consolidation:** Every 5 Extra HP levels → +1 Max Wound
- **v0.5 Replacement:** Conditioning perks (same mechanics, thematic capstone rewards)
  - Poison Resistance, Waterfall Training, Mental Resilience, Cold/Heat Conditioning, Battle Scarred, Magical Conditioning

## Combat System

### Action Economy
- **Base:** 5 AP + 1 Reaction per turn
- **Domain AP:** Add your highest domain (Prowess or Magery) tier to the AP pool (`Rules/Mechanics/Action Points.md`).
- **Initiative:** 2d10 + Perception
- **Surprise/Ambush:** Coordinated initiative, stunned targets lose 3 AP

### Defenses
- **Deflect:** Prowess + Agility/Dexterity/Strength (based on weapon type) + Equipment Defense bonus
- **Dodge:** Agility + Perception
- **Resolve:** Will + Charisma
- **Endure:** Endurance + Strength

### Combat Resolution Sequence (v0.6)
Written into `Rules/Combat/4. Combat Conflict Resolution.md`:
1. **Attacker declares the attack** — target, weapon or spell, and its trait(s)
2. **Defender declares the defense** — one allowed by the attack's traits
3. **Attacker declares pre-roll boosts** — stances, abilities, spent reactions
4. **Defender declares pre-roll boosts** — defensive abilities, buffs, reactions
5. **Both roll**
6. **Resolve the outcome**

**Defending is free:** Deflect/Dodge/Resolve/Endure cost no AP and never require the Reaction.

### Movement System (v0.6)
- **Lines and Zones:** Primary positioning system. Zones are abstract areas (rooms, squares, etc.). Lines connect zones with distance stats.
- **Skirmishes:** Groups in melee range within a zone. Engage all targets in a skirmish with one action.
- **Numeric Advantage:** -1 to deflect/dodge per disadvantage in skirmish (capped at -4). With at least 3 allies in your skirmish (or counting as having 3), no numeric disadvantage (back-to-back).
- **Reach Weapons:** Attack without entering skirmish, count for numeric advantage.
- **Ranged Attacks:** Range increment = ceil(Total Distance / Weapon Range). Same skirmish = point blank.

### Defense Applications by Attack Type
- **Strike:** Deflect, Dodge (melee, touch spells)
- **Projectile:** Dodge, Deflect (with shield or perks)
- **Burst:** Dodge (Deflect with perks)
- **Mind:** Resolve (fear, charm, mind control)
- **Body:** Endure (poison, disease, exhaustion)

### Attacks & Damage
- **Weapon Stats:** Agility for all, Heavy allows Strength, Finesse allows Dexterity
- **Ranged:** Dexterity or Perception based on weapon
- **Damage:** N weapon dice + Strength — N by Prowess band (tiers 0-1 → 1 die, 2-3 → 2, 4-5 → 3); die size by weight: Light d4/d6, Normal d6/d8, Heavy d8/d10, two-handed steps the die up. Crits double dice, never statics
- **Ranged:** Range increment = weapon Tier × 10 meters
- **Weapon AP Costs:** Light = 2 AP, Normal = 3 AP, Heavy = 4 AP

## Magic System

### Core Principles
- **Mage Requirement:** Must have Mage perk (GM permission)
- **Two Types:** Passive (uses Limit) vs Active (requires casting roll)
- **Limit Stat:** 3 + Will + Magery (capacity for persistent effects)
- **Active Casting:** 2d10 + Magery + Wit vs DC [8 + Tier × 2]
- **Strain:** failed Tier 1+ casts +1 Strain; +Strain to casting DCs (cap +5); 5th Strain and beyond → Consequence Rolls/wounds; a Breather clears all Strain

### Magery Domain
- **Progression:** Learning spells advances the domain
- **Tier Unlocks:** Each Magery level unlocks new spell tiers
- **Learning Requirements:** Magical Theory/Theology ≥ spell tier (or teacher)
- **Learning Time:** 1 day per XP spent

### Spell Costs by Tier
| Tier | Cost | XP to Next Tier |
|------|------|-----------------|
| 0    | 1    | -               |
| 1    | 3    | 10              |
| 2    | 5    | +20             |
| 3    | 7    | +30             |
| 4    | 10   | +40             |
| 5    | 15   | +50             |

> **Note (v0.6):** Advanced spell cost tier removed. Prerequisites now gate access — the Basic/Advanced split is no longer used. All spells cost a flat XP per tier.

### Metamagic (v0.6)
- Spell-modifying options granted by #Magery #Metamagic perks (`Perks/MagicPerks/Metamagic/`); perk XP counts toward Magery tiers like spells
- Each application adds an AP surcharge and a casting DC surcharge (per-option); cap = Magery tier per cast
- #Attuned spells pay +1 Limit per application instead of DC
- Grand Weaving (Magery 3) removes the cap and allows multi-turn casting
- Options: Reaching, Subtle, Lingering, Split, Widened, Empowered + Grand Weaving
- Specializations (bonus inside/penalty outside): Mage of an Element, Inward Focus, Withering Focus

## Skills List

### Social Skills
- Etiquette (Agility/Charisma), Negotiating (Charisma/Wit), Manipulation (Charisma/Will)
- Leadership (Will/Charisma), Gossip (Charisma/Perception), Intimidation (Charisma/Strength), Acting (Charisma/Will)
- The authoritative skill list (in rework) lives in `Rules/Core/Skills.md`

### Athletic Skills
- Climbing (Strength/Agility), Athletics (Strength/Endurance — Lifting and Breaking inside), Acrobatics (Agility/Dexterity)

### Knowledge Skills
- Magical Theory, History, Theology, Streetwise and the science skills — see `Rules/Core/Skills.md` for current pairings (in rework)

### Other Categories
- **Crafting:** Smithing, Woodworking, Textilework, Engineering
- **Sciences:** Biology, Chemistry, Medicine
- **Stealth/Criminal:** Stealth, Lockpicking, Sleight of Hand
- **Wilderness:** Survival, Tracking, Navigation

## Traits System

### Defense Traits
- **#Strike:** Deflect, Dodge
- **#Projectile:** Dodge, Deflect (with shield or perks)
- **#Burst:** Dodge (Deflect with perks)
- **#Mind:** Resolve
- **#Body:** Endure
- **#Defend:** Generic trait for all defensive actions (Deflect, Dodge, Resolve, Endure) - used for buffs like "All in Defense"

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
3. **Until Removed** - Source specifies removal (Grabbed, Off-Guard while prone, Dazzled until cleared)

### Enhancement Conditions (Attribute Modifiers)
- **Grace X:** ±X to Agility/Dexterity rolls
- **Vigor X:** ±X to Strength/Endurance rolls
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
- **Prone:** Disadvantage on Prowess Domain (attacks, Deflect). Advantage on Dodge and Endure vs #Projectile and #Burst. Speed reduced to 1/5th.
- **Grabbed:** Grants Off-Guard and Immobilized; attacks at disadvantage, no reach weapons vs grappler. Grappler releases free; grappled must Escape.
- **Off-Guard:** -1 to defend against attacks.
- **Blinded:** All sight-reliant checks are Screwed (1d10).
- **Dazzled:** All sight-reliant checks at disadvantage.
- **Unconscious:** Deflect/Dodge are Screwed, Perception at disadvantage.

### Rest Conditions
- **Fatigued X:** -X to all rolls, -2X to exploration/downtime. At Fatigue 4, unconscious.
- **Well Rested:** +1 to +3 to Downtime/Exploration until Fatigued or night's rest.

### Damage Riders (no ticking DOTs — temp design v0.6)
- No damage-over-time; lingering harm = front-loaded damage, one-time riders, or zone hazards (track the map, not tokens)
- **Bleed X:** next movement action → take X, then clears (First Aid clears safely)
- **Fragile X:** next damage instance +X, then clears
- **Pinned X:** next movement action +X AP, or 1 AP to remove projectile
- **Stunned X (defined):** Lose X AP at start of turn, no reactions until next turn; excess carries over

## Social Interactions

### Disposition
- **Range:** -5 (hostile) to +5 (fanatical adoration)
- **Factors:** Race, appearance, social class, rank
- **Favor Costs:** Disposition affects price (negative = higher cost, positive = lower/free)

### Social Actions
- **Improving Disposition:** Social skill + Charisma vs target's resistance
- **Detect Falsehood:** Perception + Manipulation or Perception + Will
- **Fast-Talk:** Fast-talk vs Detect Falsehood or Perception/Will

### Trading
- **Base Prices:** Pawn shops buy 50%, sell 100% of listed price
- **Disposition Modifier:** ±5% per disposition level
- **Bargaining Range:** 25-125% of listed price based on disposition

## Key Actions

### Movement
- **Engage:** 1 AP - Enter a skirmish within a zone
- **Disengage:** 1 AP - Leave a skirmish without provoking reactions
- **Move:** Variable AP - Move between zones (Cost = ceil((Distance × Multiplier) / Speed)), no partial movement
- **Stand Up:** 2 AP - Remove Prone condition

### Combat Actions
- **Basic Attack:** 2-4 AP based on weapon weight
- **All in Defense:** 2 AP - Gain advantage on all #Defend actions until your next turn (requires no offensive action this turn)
- **Grapple:** 3 AP - Attempt to grab opponent (Prowess + Strength/Agility vs Dodge). On success, the target gains Grabbed; you are locked together in the skirmish.
- **Escape:** 2 AP - Attempt to break free from Grabbed (Athletics, Acrobatics or Prowess vs the grappler's roll)
- **Disarm:** 2 AP - Prowess + ST/DX vs target's weapon roll; -5 and free retaliation on failure unless target is Grabbed by you
- **Trip:** 2 AP - Prowess + ST/AG vs Endure; target Prone
- **Shove:** 3 AP - Prowess + ST vs Endure; target forced out of its skirmish (no damage, team tactic)
- **Feint (WIP):** 1 AP - Prowess + CH/DX vs Resolve; target Off-Guard vs your next attack
- **Ready (v0.5):** Variable AP (activity cost) - prepare action with trigger, execute as Reaction
  - Examples: Ready strike, ready spell, ready movement
  - Most combat preparations are obvious to observers
- **First Aid:** 4 AP, Medicine skill
- **Aid:** 2+R AP, provides bonus to ally

### Social Actions
- **Demoralize:** 2 AP, Intimidation vs Resolve
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


**Reading tree:** `Rules/Rulebook.md` embeds the chapter hubs (`Rules/Intro.md`, `Core.md`, `Combat.md`, `Magic.md`, `Social And World.md`, `Downtime And Exploration.md`); each hub embeds the numbered section files from its matching subfolder.

**Chapter folders:**
- `source/content/Rules/Intro/` - `1. Welcome to Exceed.md` (overview and introduction)
- `source/content/Rules/Core/` - `Core Resolution System.md` (dice, check types), `Character Creation and Point buy Costs.md`, `Attributes.md`, `Perks and Flaws.md`, `Skills.md` (skill list with attribute pairings; its skill sections mirror the LifePerks subfolders)
- `source/content/Rules/Combat/` - `4. Combat Conflict Resolution.md` (resolution sequence, free defenses, embeds), `4.0 Lines and Zones.md`, `4.1 Taking Damage.md` (death rules), `4.2 Wounds And Consequences.md`, `4.3 Conditions.md`, `4.4 Weapons and Combat Training.md`, `11. Actions.md` (embeds from Actions/)
- `source/content/Rules/Magic/` - `6. Magic System.md` (Limit system, Strain, magery domain, Metamagic, spell lists), `6.1 Summoning.md`, `6.2 Magic Perks.md`
- `source/content/Rules/Social And World/` - `Social Mechanics.md` (Disposition, values, social actions), `8.1 Organizations.md` (WIP till MS8)
- `source/content/Rules/Downtime And Exploration/` - `7. Equipment.md` (weapon builder, armor, shields), `7.1 Encumbrance.md`, `9.1 Time and Travel.md` (time ladder), `9.2 Downtime and Training.md` (embeds from Mechanics/), `9.3 Exploration and Out of combat Activities.md`, `Camping and Maintanence Rules.md`

**Subfolders:**
- `source/content/Rules/Mechanics/` - Embeddable mechanic files (Action Points, Initiative, Recovery Rules, etc.)
- `source/content/Rules/Lines And Zones/` - Zone effects (Skirmish, Crowded, Duel Zone, Zone Capacity, Fortified Defenders)
- `source/content/Actions/` - Individual action definitions (Movement/, Combat/, Social/, Support/, Abilities/) - at content root, NOT under Rules/
- `source/content/Rules/Effects/` - Embeddable effect files (`Effect - Name.md`)
- `source/content/Rules/References/` - Reference tables (Bonus Types, Defense Traits, Downtime Quality, Rank System, Conditions/)
- `source/content/Rules/Design Philosophy.md` - Design notes and rationale
### Combat System Files
- `source/content/Perks/Prowess/` - Battle-side perk trees (was BattlePerks/)
- `source/content/Perks/Conditioning/` - Conditioning lines (top level, advance no domain)
- `source/content/Perks/LifePerks/` - Skill-based perks
- `source/content/Perks/MagicPerks/` - Magic-related perks
- `source/content/Rules/Mechanics/Dual Wielding.md` - Dual wielding rules (WIP)
- `source/content/Design Guidelines.md` - Comprehensive perk design document

### Spell System Files
- `source/content/Spells/` - Individual spell definitions organized by tier folders (Tier 0-5 + Rituals + Trees)
- `source/content/Spells/0 Spell Template.md` - Template for creating new spells
- `source/content/Spells/Rituals/Team Ritual.md` - Team formation and ritual mechanics

### Perk System Files
- `source/content/Perks/0 Universal Perk Template.md` - Template for creating new perks
- `source/content/Perks/Prowess/` - Prowess/battle perks organized by weapon/type
- `source/content/Perks/LifePerks/` - Non-combat life perks. Subfolders mirror the skill sections of `Rules/Core/Skills.md`: Social, Athletic, Craft (Smithing/Woodworking/Textilework/Engineering), Natural Sciences (Biology/Chemistry/Medicine), Underworld (Stealth/Criminal), Wilderness, Knowledge. Each perk is filed under the section of its **first skill requirement**. `Rank and Reputation Perks/` is a side category (standing/rank perks, kept regardless of skill requirements)
- `source/content/Perks/MagicPerks/` - Magic system perks
- `source/content/Perks/Flaws/` - Disadvantage perks (flaws; Cost line carries the negative XP and its Battle/Life Flaw pool)
- `source/content/Perks/Companions/` - Bonded companions & familiars - untagged Battle XP perks, advance no domain (see `Rules/Mechanics/Bonded Companions.md`)

### Special Character Files
- `source/content/Perks/MagicPerks/Mage.md` - Mage character type and requirements

### Design Documentation
- `source/content/Design Guidelines.md` - Design philosophy and guidelines
- `source/content/Rules/Mechanics/Size Rules.md` - Size steps, wound scaling, #Size modifiers
- `source/content/Rules/Mechanics/Bonded Companions.md` - Companion command economy (no own AP; commands cost your AP)
- `source/content/Rules/References/Prices.md` - Full price tables (silver standard, anchored to the Earning Income Rules)
- `source/content/Rules/References/Bestiary/` - Simplified statblocks (bond presets + summon units)

## Quick Search Patterns

### Finding Core Mechanics
- **Dice System:** Search `2d10`, `advantage`, `disadvantage`, `doubles`
- **Attributes:** Search `Perception`, `Will`, `Charisma`, `Wit`, `Strength`, `Endurance`, `Agility`, `Dexterity`
- **Combat:** Search `AP`, `action points`, `initiative`, `deflect`, `dodge`, `resolve`, `endure`
- **Magic:** Search `Limit`, `magery`, `persistent`, `active spell`

### Finding Specific Rules
- **Character Creation:** Files 3.x, search `XP`, `Experience Points`
- **Combat Resolution:** File 4, search `attack`, `damage`, `defense`
- **Health System:** Files 3.2, 4.1, 4.2, search `HP`, `stamina`, `health`, `wounds`
- **Skills:** `Rules/Core/Skills.md`, search skill names or `(Attribute/Attribute)` pattern
- **Magic Rules:** Files 6.x, search `tier`, `spell`, `casting`
- **Social Rules:** Files 8.x, search `disposition`, `favor`, `negotiation`

### Finding Content by Type
- **Perks:** `source/content/Perks/Prowess/`, `source/content/Perks/LifePerks/`
- **Spells:** `source/content/Spells/` organized by tier folders
- **Conditions:** `source/content/Rules/References/Conditions/`
- **Effects:** `source/content/Rules/Effects/`
- **Abilities:** `source/content/Actions/Abilities/`
- **Templates:** Search `Template.md` for creation guidelines

### Search by Game Element
- **Specific Skill:** Search skill name in `Rules/Core/Skills.md` or related perk files
- **Combat Mechanics:** Files 4.x, search `strike`, `projectile`, `burst`, `mental`, `physical`
- **Equipment Rules:** Files 7.x, search weapon/armor names or `encumbrance`
- **Movement:** File 4.0 and `Actions/Movement/`, search `zone`, `line`, `engage`, `disengage`, `move`

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
/source/content/Actions/Abilities/Ability - Name.md    → Contains ability mechanics only
/source/content/Rules/Effects/Effect - Name.md         → Contains effect mechanics only
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
2. Create file in `Actions/Abilities/` or `Rules/Effects/`
3. Name file: `Ability - Descriptive Name.md` or `Effect - Descriptive Name.md`
4. Write mechanics (no "Ability:" or "Effect:" label needed - filename shows type)
5. Add relevant tags for mechanics (mechanic tags like #Strike — not perk discipline tags like #Prowess)
6. In perk file, embed with `![[Ability - Name]]` or `![[Effect - Name]]`

### Tag Conventions
**Perk-level tags** (in perk file) say what the perk IS — never which XP pays for it (that lives in the Cost line, e.g. `**Cost:** 5 Battle XP`):
- `#Prowess` (fighting techniques, advance the Prowess domain), `#Magery` (advance the Magery domain), `#Conditioning` (HP stages), `#Skill` (life-skill applications), `#Universal`, `#Flaw`
- Battle-side perks that advance no domain (the Defender line) carry no discipline tag — just a Battle XP cost
- `#WeaponTraining`, `#Shield`, `#StavesSpears`, etc. (tree tags)

**Mechanic tags** (in ability/effect file):
- `#Strike`, `#Projectile`, `#Burst`, `#Reaction`
- `#Passive`, `#Dodge`, `#Deflect`, `#Endure`, `#Resolve`
- `#Damage`, `#Healing`, `#Buff`, `#Debuff`
- `#AoE`, `#Melee`, `#Ranged`, `#Movement`
- dont put random tags where they don't belong.
- don't write the name of the file in the first line of the file as a header. Name of the file is a header already.
- DONT ADD UNNEEDED TAGS
