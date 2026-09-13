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

This cost logic is applied to both Magery and Prowess. Despite Prowess requiring half the cost, the other half in Magery can be substituted by spells.

Spell Cost by Level
Cost to reach next levels. 10 to reach lvl1, 20 to reach lvl2, 30 to reach lvl 3, 40 to reach level 4 and 50 for level 5.
Spell Costs by Tier (v0.6: single cost per tier, Advanced removed — prerequisites gate access):
 - Tier 0: 1 XP   (10 spells = lvl 1)
 - Tier 1: 3 XP   (~7 spells = lvl 2)
 - Tier 2: 5 XP   (6 spells = lvl 3)
 - Tier 3: 7 XP   (~6 spells = lvl 4)
 - Tier 4: 10 XP  (5 spells = lvl 5)
 - Tier 5: 15 XP

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
**Average human (Strength 0 / Endurance 0, 0 XP invested):**
- Capacity: 25 kg, No penalty threshold: 12.5 kg

**Early Character (Strength 1 / Endurance 1, 20 XP invested):**
- Capacity: 49 kg, No penalty threshold: 24.5 kg

**Early-Mid Character (Strength 2 or Endurance 2):**
- Capacity: 64 kg, No penalty threshold: 32 kg

**Sample Loadout:**
- Kite shield: 5 kg + Defensive armor: 8 kg + Average weapon: 2 kg + Secondary weapon: 2 kg + Basic equipment: 5 kg = **22 kg total**

**Results:**
- Starting character 12kg = no encumbrance penalty
- Early character: 22 kg = no encumbrance penalty
- Early-mid character: 22 kg + 12 kg additional gear = 34 kg = light encumbrance

Adding daily food/water (1 kg) pushes characters toward light encumbrance during travel.
