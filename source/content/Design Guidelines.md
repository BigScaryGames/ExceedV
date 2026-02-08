# Costs
Perk Costs by Level:
 - Level 0: Cheap (2), Average (3), Expensive
 (5) - Basic techniques
 - Level 1: Cheap (3), Average (5), Expensive
 (10) - Refined skills
 - Level 2: Cheap (5), Average (10), Expensive
 (15) - Advanced techniques
 - Level 3: Cheap (10), Average (15), Expensive
  (20) - Master techniques
 - Level 4: Cinematic effects (arbitrary costs)
  - Legendary techniques

This cost logic is applied to both Spellcraft and Martial. Despite Martial requiring half the cost, the other half in Spellcraft can be substituted by spells.

Spell Cost by Level
Cost to reach next levels. 10 to reach lvl1, 20 to reach lvl2, 30 to reach lvl 3, 40 to reach level 4 and 50 for level 5.
Spell Costs by Tier:
 - Tier 0 Spells: Basic (1), Advanced (3)  (10 basic or 6.6 Advanced) 10cp
 - Tier 1 Spells: Basic (3), Advanced(5)   (6.6 basic or 4 Advanced) 20cp
 - Tier 2 Spells: Basic (5), Advanced(7) (6 basic or 4.3 Advanced) 30cp
 - Tier 3 Spells: Basic (7), Advanced(10)   (5.6 basic or 4 advanced) 40cp
 - Tier 4 Spells: Basic (10), Advanced(15) (5 basic or 3.3 advanced)50cp
 - Tier 5 Spells: Basic (15), Advanced(25)

# Weights
## Weapon Weights
| Weapon Type    | Weight  |     |
| -------------- | ------- | --- |
| Light weapon   | .5-1 kg |     |
| Average weapon | 2-3 kg  |     |
| Large weapon   | 3-5 kg  |     |
2h weapons being heavier then 1h on average. Some weapons remain nimble despite that, so an average weapon Like a greatsword (yes, its not about KG weight but that it is quite fast) can weight like a heavy one.
## Armor Weights
| Armor Type | Weight |     |
| ---------- | ------ | --- |
| Scout      | 4 kg   |     |
| Tactical   | 6 kg   |     |
| Defensive  | 8 kg   |     |
| Protective | 10 kg  |     |
| Bulwark    | 12 kg  |     |
| Titanic    | 15 kg  |     |
| Colossal   | 20 kg  |     |

## Shield Weights
| Shield Type | Weight |
|---|---|
| Buckler | 1 kg |
| Shield | 3 kg |
| Kite | 5 kg |
| Tower | 10 kg |
| Fortress | 15 kg |

## Other Equipment
| Item                   | Weight         |
| ---------------------- | -------------- |
| Food and water per day | 1 kg (minimum) |
| Basic equipment/gear   | ~5 kg          |
| Clothes                | 1 kg           |
| Clothes (warm)         | 2 kg           |
| Backpack               | 1-3 kg         |

## Encumbrance Simulation
**Average human (MG0/EN0, 0 XP invested):**
- Capacity: 25 kg, No penalty threshold: 12.5 kg

**Early Character (MG1/EN1, 20 XP invested):**
- Capacity: 49 kg, No penalty threshold: 24.5 kg

**Early-Mid Character (MG2 or EN2):**
- Capacity: 64 kg, No penalty threshold: 32 kg

**Sample Loadout:**
- Kite shield: 5 kg + Defensive armor: 8 kg + Average weapon: 2 kg + Secondary weapon: 2 kg + Basic equipment: 5 kg = **22 kg total**

**Results:**
- Starting character 12kg = no encumbrance penalty
- Early character: 22 kg = no encumbrance penalty
- Early-mid character: 22 kg + 12 kg additional gear = 34 kg = light encumbrance

Adding daily food/water (1 kg) pushes characters toward light encumbrance during travel.

## Designer Notes

### Playtesting Notes
[Record feedback and observations from testing]

# Design Decisions & Logic

### Unique Selling Proposition (USP)

**The Limit System** - The core innovation of Exceed is the "Limit" stat, which governs the maximum number of persistent magical and non-magical effects a character can sustain simultaneously.

#### Problem Solved
Traditional systems suffer from "pre-buff" issues where players stack numerous temporary bonuses before encounters, and "magic item bloat" where characters accumulate dozens of persistent magical effects. D&D 5e attempts to address this with concentration, time limits, and attunement slots, while PF2E uses 10 attunement slots but still allows hundreds of different buffs to stack.

#### Solution: Limit
The Limit stat creates a hard cap on the total number of active persistent effects, forcing meaningful tactical choices:
- Players must prioritize which effects to maintain
- No endless stacking of buffs
- Clear, trackable resource management
- Scales with character power (Limit increases as characters advance)
- Applies to all persistent effects: spells, permanent magic items, class abilities, etc.

This system eliminates bookkeeping nightmares while maintaining strategic depth through meaningful choice constraints.

### Core Concepts
The game aims to fix 3 problems recurrent in TTRPGs
- Buff Stacking/Endless Buffing, character progression disconnected from the play-style, and armor-hp interactions.
  For this it offers its USPs as solutions.
The Limit system in [[6. Magic System]] - limiting the active buffs and magical effects a character can sustain on self and group.

[[3.3 HP And Wounds]]. - where Armor works as ablation multiplied by the character's resilience.
  2. [[3.1 Attributes]] - Attributes deriving from skills, creating positive feedback loops, separation of social and combat XP based on the session contents.
### Target Audience
Skill-based TTRPG enjoyers. Earned progression connoisseurs.
Target audience is TTRPG players who prefer when they are not dictated how to play a character from the moment they choose the class at level 1.
It still absolutely should work for new players as well as experienced ones. Though groups with new players are suggested lower XP starting point.
It's a game for GURPS players who want less complexity and more streamlined experience, Pathfinder players who want more control over their characters, LitRPG lovers who love numbers go up, slow burn progression.
