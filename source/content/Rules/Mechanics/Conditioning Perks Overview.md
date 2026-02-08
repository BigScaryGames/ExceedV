Hit points can be increased through **Conditioning** perks - specialized training regimens that build both physical resilience and provide unique benefits at mastery.

Conditioning perks are **leveled perks** found in `/Ruleset/Perks/CombatPerks/Conditioning/`. Each can be taken multiple times and provides both HP progression and a thematic capstone reward.

## Available Conditioning Perks

| Perk | Requirement | Theme |
|------|-------------|-------|
| **Poison Resistance** | Medicine 1 | Resist toxins |
| **Waterfall Training** | Athletics 1 | Resist forced movement |
| **Mental Resilience** | Will 2 | Resist mental effects |
| **Cold Conditioning** | Survival 1 | Thrive in cold |
| **Heat Conditioning** | Survival 1 | Thrive in heat |
| **Battle Scarred** | Martial 1 | Easier to heal |
| **Magical Conditioning** | Mage, Spellcraft 1 | Resist transmutation |

## Progression

- **Cost:** Max_Wounds × level XP
- **Levels 1-4:** Gain +1 HP per level
- **Level 5:** Consolidates into +1 Max_Wounds AND grants capstone effect
  - The new wound operates like all others (gains full armor and endurance bonuses)
  - Capstone effects vary by conditioning type (see individual perk descriptions)

## Example Progression

Character with 2 Max_Wounds, 0 Endurance, +2 Armor:

| Level | Total  XP Cost | HP Gain                  | Totals                       |
| ----- | -------------- | ------------------------ | ---------------------------- |
| 1     | 2 XP           | +1 HP                    | 11 Health, 4 Stamina = 15 HP |
| 2     | 4 XP           | +1 HP                    | 12 Health, 4 Stamina = 16 HP |
| 3     | 6 XP           | +1 HP                    | 13 Health, 4 Stamina = 17 HP |
| 4     | 8 XP           | +1 HP                    | 14 Health, 4 Stamina = 18 HP |
| 5     | 10 XP          | +1 Max Wounds + Capstone | 15 Health, 6 Stamina = 21 HP |
