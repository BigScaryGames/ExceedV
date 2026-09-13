---
draft: true
---
Temporary NPCs don't use the full PC machinery. They don't buy perks and don't track skills they'll never use. Their defenses are static DCs the players roll against; real NPCs roll their attacks, mooks are fully static.

> MS7 draft (early — pulled forward for playtesting). Numbers are first-pass; tune at playtest.

## Design Rules

1. **Defenses are always static.** Players always roll against NPCs — attacks, spells, and effects all target a DC.
2. **Real NPCs roll attacks** (2d10 + Attack Bonus vs the target's defense roll) and can crit on doubles. **Mooks don't roll** — their attacks are static DCs, and mooks can't crit.
3. **One pool: Health.** No Stamina/Health split — damage just depletes Health. At 0 the NPC is down; at negative Health, dead. No Consequence Rolls. Named NPCs can opt into the full [[4.1 Taking Damage|wound rules]] if the fiction needs them to survive.
4. **No XP economy.** Assign final numbers directly — write the flat result a perk would buy a PC (free Defense bonuses, free reaction abilities). Prerequisites don't apply to NPCs.
5. **Few buttons.** 1–3 attacks/abilities total. An NPC never needs the full action list.
6. **Only relevant skills.** 2–4 skills at most, as flat DCs. A tavern keeper needs Haggling and Gossip, not Track.
7. **Mook economy:** 1 HP each. One move + one ability per turn (Move + attack, or Engage + attack). No reactions. Mooks are fragile — their threat is their damage, which stays at full tier dice.

## NPC Math

**Threat = the adventurer tier this NPC threatens one-on-one.** Adventurers attack in steps of 2 per tier, so a Threat X NPC attacks like a tier-X adventurer:

| Threat | Mook attack DC | NPC attack bonus | Damage   | Health        | Defenses | Buttons |
| ------ | -------------- | ---------------- | -------- | ------------- | -------- | ------- |
| 0      | 10             | −1               | d4       | 1 (mook) / 6–8 | 10–11    | 1       |
| 1      | 12             | +1               | d6+1     | 12–16         | 12–14    | 1–2     |
| 2      | 14             | +3               | d8+2     | 18–24         | 14–16    | 2       |
| 3      | 16             | +5               | d10+3    | 26–32         | 16–18    | 2–3     |
| 4      | 18             | +7               | 2 dice+  | 34–42         | 18+      | 3       |
| 5      | 20             | +9               | 2 dice+  | 45+           | 20+      | 3       |

NPC attack bonus = mook DC − 11 (the average of 2d10), so a rolling NPC hits as often as its DC suggests.

**Other values:**

| NPC Value      | Static DC                          |
| -------------- | ---------------------------------- |
| Deflect        | 11 + Martial + Deflect stat + armor |
| Dodge          | 11 + Agility + Perception          |
| Resolve        | 11 + Will + Charisma               |
| Endure         | 11 + Endurance + Might             |
| Skill          | 11 + skill level + attribute       |
| Initiative     | 10 + Perception (fixed — no roll)  |

**Defense spread:** put the NPC's strong defense at the top of its band; lagging defenses sit 2–4 lower. What lags follows PC logic:
- **Deflect** keeps pace for martial NPCs (weapon and armor carry it).
- **Dodge** lags behind for everyone — it leans on two attributes.
- **Resolve** lags for noncasters.
- **Endure** lags for casters and glass cannons.

**Crits:**
- NPC attacks crit on doubles (damage ×2), like any rolled attack. Mooks can't crit.
- Attacks against NPCs crit on the attacker's doubles vs the static DC, as normal.

**Caster NPCs** skip casting checks (no Strain): a spell is just a button — a rolled attack if it targets a defense, otherwise a static DC the players roll against (e.g. Fear Aura: Resolve DC 14).

- **NPC vs NPC:** compare static values, defender wins ties (matches [[Opposed Checks]]).
- **Damage is still rolled:** weapon dice + flat bonus from the ladder.
- **Action economy:** real NPCs: 5 AP + 1 Reaction. Mooks: one move + one ability.

**Calibration:** a Threat 1 NPC attacks at 2d10+1 (avg 12) against a starting PC's defense roll (avg ~12–13) — an even duel, decided by PC perks.

## Statblock Template

```
Name | Threat X | #role #role (#mook)
Init X | Speed X | AP 5 (R: yes) — mooks: 1 move + 1 ability

Deflect X | Dodge X | Resolve X | Endure X
Health X (down at 0; mooks: 1)

— Attacks & Abilities (1-3) —
NPC:   Name | AP X | #Strike | 2d10+B vs defense roll | dX+Y | traits (Reach, Nonlethal...)
Mook:  Name | #Strike | DC X vs Deflect/Dodge | dX+Y | traits
Name | reaction / aura / trait — one line

— Skills —
Skill X (DC Y), Skill X (DC Y)

— Notes —
Morale / Attitude / loot / one behavioral quirk
```

Role tags: #melee #ranged #brute #skirmisher #support #caster #social #mook.

## Encounter Budget

Weigh each PC: fresh ≈ 1, established ≈ 2, veteran ≈ 3.

| Difficulty | Total Threat vs party weight |
| ---------- | ---------------------------- |
| Speed bump | ≤ half                       |
| Even       | ≈ equal                      |
| Hard       | 1.5×                         |
| Deadly     | 2×+                          |

## Building the Encounter

1. **Venue:** 2–5 zones with distance lines — see [[Encounter Setup]]. One zone is fine for a brawl.
2. **Budget:** pick a difficulty, sum threat, stay within it. Mooks count full threat — their fragility is offset by their damage.
3. **Mix roles:** pressure more than one defense (a #Projectile or #Burst forces Dodge; a #Mind effect forces Resolve). Mooks in pairs minimum — solo mooks die before acting.
4. **Place and roll:** ambushes per [[Surprise Rounds]]; all mooks of one type share a single initiative slot.
5. **Dials:** Health and attack values can move ±2 mid-fight without breaking math. Retreat/morale is a valid off-switch — most NPCs flee at half Health or when their leader drops (note it in the statblock).

## Worked Examples

**Bandit** | Threat 1 | #melee #skirmisher
Init 10 | Speed 5 | AP 5 (R: yes)
Deflect 13 | Dodge 12 | Resolve 11 | Endure 13
Health 14
— Shortsword | 2 AP | #Strike | 2d10+1 vs defense roll | d6+1
— Shield Block | Reaction | +2 Deflect vs one attack
— Skills: Intimidation 1 (DC 12), Athletics 1 (DC 12)
Flees at half Health if alone. Carries 10g of assorted gear.

**Bandit Archer** | Threat 1 | #ranged
Init 11 | Speed 5 | AP 5 (R: no)
Deflect 11 | Dodge 13 | Resolve 10 | Endure 11
Health 12
— Shortbow | 3 AP | #Projectile | 2d10+1 vs defense roll | d8+1 | Range 10m
— Retreating Shot | Reaction | single attack when someone Engages them
— Skills: Perception 1 (DC 12)
Repositions to a new zone when engaged.

**Rabid Dog** | Threat 0 | #mook #melee
Init 11 | Speed 6 | 1 move + 1 ability
Deflect 10 | Dodge 12 | Resolve 8 | Endure 11
Health 1
— Bite | #Strike | DC 10 vs Deflect/Dodge | d4
Never flees, fights to death. Pack of 3–4.

**Guild Clerk** | Threat — | #social
Attitude 0 | Deflect 9 | Dodge 10 | Resolve 13 | Endure 10 | Health 8
— Skills: Haggling 2 (DC 13), Bureaucracy 2 (DC 13), Gossip 1 (DC 12)
— Wants: quiet shifts; Fears: his boss; Lever: flattery about his ledgers
Initial attitude per [[Attitude System]]. Bribable at −20% for 25g.

**Tags:** #Combat
