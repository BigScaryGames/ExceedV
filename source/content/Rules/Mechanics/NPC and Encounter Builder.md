---
draft: true
---

> MS7 draft. Generated from array of notes. Needs a final pass later

# Creatures

Creatures use **DC = 11 + 2T**. No character build, no Wounds, no Strain, no Limit. One HP pool; at 0 the non boss creature is out, summons vanish.

A creature is a **Level 0-10**, a **tyoe**, and a handful of abilities from the player-facing lists. That is the whole statblock.

The same bandit as a person will have two different stat block depending on the player levels. 



##  Behavior
Behavior varies based on NPC and GM interpretation. Most creatures would prefer to not die, but at the same time they wouldn't be combatants if they were completely averse to risk. There might be a morale threshold or triggers to creatures, but its up to gm to decide if someone flees, surrenders, gets a traumatic episore or fights till the end. 
## Level

Two levels per tier. A tier 2 party fights Levels 3-5; when in doubt, **Level = 2 x tier**. Odd levels are the half-steps between tiers.
### Leveled graph

| L   | Attack | HP  | Damage |
| --- | ------ | --- | ------ |
| 0   | +0     | 12  | 1d3    |
| 1   | +1     | 16  | 1d4    |
| 2   | +2     | 24  | 1d6    |
| 3   | +3     | 28  | 1d8    |
| 4   | +4     | 32  | 1d10   |
| 5   | +5     | 40  | 1d12   |
| 6   | +6     | 48  | 2d6+1  |
| 7   | +7     | 60  | 3d4+2  |
| 8   | +8     | 72  | 2d10   |
| 9   | +9     | 84  | 3d8    |
| 10  | +10    | 96  | 3d10   |

- Defenses start at **11 + Level**, then the spread.
- Damage is per hit. Crits double the damage.
- Spells and effects that scale on Magery use **M = half Level, rounded down**. for casters 
- Checks use Level; pick two specialties at +2.

## Type

| Type | HP   | AP   | Attacks      | Reactions |
| ---- | ---- | ---- | ------------ | --------- |
| Mook | 1/4  | 3    | one per turn | —         |
| NPC  | full | 5    | any          | 1         |
| Boss | x2   | 5 x2 | any          | 1-2       |

- Creatures roll attacks and defenses like anyone else. Printed offenses and defenses double as DCs when you'd rather not roll. (e.g.  mooks or to keep pace faster)
- **Mook:** Move, Engage, attack — 1 AP each. Mook's attacks are one dice smaller than similar level NPC's.
  Packs share one initiative slot. If a mook takes damage and you can't tell whether it survives, it dies. 

- **NPC:** 5 AP regained normally.
- **Boss:** acts twice in the round order — 10AP that is regained at the end of the bottom turn. Dots play at the end of the bottom turn as well.
Unike PCs NPCs don't spend actions when using reactions.
- Two NPCs fighting each other: don't simulate. Tell it, or roll once for the round.

## Adjusting the stats
Enemies have stats, and the stats have a numeric value. Moving numbers costs.
When moving numbers move them up or down the leveled graph.

NPC attribute level adjustment cost.

| Attack | HP  | Damage | Deflect | Dodge | Resolve | Endure | Abiltiy/Effects |
| ------ | --- | ------ | ------- | ----- | ------- | ------ | --------------- |
| 2      | 1   | 2      | 1       | 1     | 0.5     | 0.5    | Varies          |
E.g. to move attack 1 level up, i need 2 points, so i drop resolve, endure and deflect by 1 level.



+1 attack - -1 to endure and resolve and deflect (0.5 0.5 1).

If i want someone who is very strong and very clumsy i move damage up by 3 tiers and attack down by 3 tiers.
in case of level 3 attack o hit was 10 became 13 almost halfing the to hit chance, damage from 1d8 went to 2d6+1 almost doubling. This is not ideal progression, but its good enough.
If I want a glass cannon i do the same with HP and defenses. Moving 2 tiers up the attack, and dropping 3 defenses by 3 for 4.5 or HP by a tier.

When making characters be sensible, and don't do more than +-2 on dodge and deflect. And don't move dodge more than 2 away from deflect. Unless trying to create insanely good dodger character.

## Abilities

Player abilities and spells, as written, prerequisites ignored. What it needs at the table — a free hand, ammunition, a grabbed target — it still needs(most of the time).

- A roll written as Prowess or Magery + attribute is the creature's **Attack**. Any other contest targets one of its listed defenses. 
- Weapon attacks use the row damage. 2 AP — mooks 1 AP.
- Enemies don't track strain or limit.
- #Attuned effects are on for the whole fight.
- Casters take spells of tier ≤ M, at the printed AP. Casting succeeds — targets still defend.

Mooks take 0-2 abilities, NPCs 2-4, bosses 3-6. A statblock can always carry a bespoke line.

## Encounter Value

Same-level base points: **mook 1/3, NPC 1, boss 2**. **ΔL = creature Level − party Level** (party Level = 2 x the average of the PCs' highest domain tiers). 
Each level up costs x1.5; each level down x0.7. Two levels up doubles, two down halves.

| ΔL  | −4  | −2  | 0   | +2  | +4  |
| --- | --- | --- | --- | --- | --- |
| ×   | ¼   | ½   | 1   | 2   | 4   |


Four PCs: 3 points is standard - encounter, 4 is hard, 6 is deadly. 

Everything below 1 points must have a secondary objective, a time limit, a defense mission. Otherwise it is considered too easy to contribute to growth and . 

**Battle XP per PC = resolved points x 4 ÷ party size.** Rounding fractions up to GM.
 A party of four drops their-tier boss: 2 XP each.

Build the fight in [[Encounter Setup]]; ambushes per [[Surprise Rounds]]. Routed or surrendered creatures pay the same as dead ones.

# Statblocks (AI gen)

**Kiln Zealot** | L6 | Mook | 1/3 pt
HP 12 · 3 AP, one attack · Attack +6 · Deflect 17 / Dodge 18 / Resolve 16 / Endure 16
— Flensing Knife | 1 AP | #Strike | 2d4+1

**Enforcer** | L6 | NPC | 1 pt
HP 48 · 5 AP at the start and end of its turn · 1 reaction · Attack +7 · Deflect 16 / Dodge 16 / Resolve 16 / Endure 18
— Hooked Chain | 2 AP | #Strike | 2d6+1
— Grapple | 3 AP | vs Dodge, one free hand | on a failure, the defender gets a free attack
— Shove | 3 AP | vs Endure | force the target out of its skirmish
— Counter Grab | Reaction | after a critical Deflect against a melee attack | [[Grapple]] the attacker

**Emberpriest** | L6 | Boss | 2 pts
HP 96 · acts twice in the round, 5 AP per activation · 1 reaction · Attack +6 · Deflect 16 / Dodge 17 / Resolve 18 / Endure 16
— Cinder Staff | 2 AP | #Strike | 2d6+1
— Ember Lance | 2 AP | #Strike | half damage, round down; push the target out of the skirmish
— Binding Chains | 5 AP | attack vs Endure | on a failed Endure, pull a target in its zone into the skirmish
— Ember Lance | Reaction | after taking damage | hit the attacker with Ember Lance
— Pinning Strike | Reaction | strike a creature entering the skirmish from outside
— Last Stand | once per combat | below 0 HP: strike; on a hit, regain the damage dealt — above 0, it stays up


*Built off the adjusting rules — check the trades.*

**Kiln Ogre** | L6 | NPC | 1 pt — strong and clumsy: damage +3 levels (6 pts) for attack −3 levels (6 pts)
HP 48 · 5 AP · 1 reaction · Attack +3 · Deflect 17 / Dodge 17 / Resolve 17 / Endure 17
— Greatclub | 2 AP | #Strike | 3d8
— Grapple | 3 AP | vs Dodge, one free hand | on a failure, the defender gets a free attack
— Shove | 3 AP | vs Endure | force the target out of its skirmish

**Needle** | L6 | NPC | 1 pt — glass cannon: attack +2 levels (4 pts) for all defenses −1 (3 pts) and HP one level down (1 pt)
HP 40 · 5 AP · 1 reaction · Attack +8 · Deflect 16 / Dodge 16 / Resolve 16 / Endure 16
— Stiletto | 2 AP | #Strike | 2d6+1, Light
— Piranha Strike | each −3 to attack buys +1 damage die, multiple times | off-guard target, Light weapon

**The Pacifist** | L6 | NPC | 1 pt — the insanely-good-dodger exception: Dodge +4 (4 pts) for attack −1 level (2 pts) and all damage dropped to 0
HP 48 · 5 AP · 1 reaction · Attack +5 · Deflect 17 / Dodge 21 / Resolve 17 / Endure 17
— Six-Shot | 2 AP | #Projectile | damage 0 — an attempt to disarm within own and adjacent zones  
— Slip | effect | 
— Shot from the Hip | Reaction | when attacked in its skirmish | attack vs Dodge; on a hit, the attacker is disarmed

**Alley Cutter** | L2 | Mook | 1/3 pt
HP 6 · 3 AP, one attack · Attack +2 · Deflect 13 / Dodge 14 / Resolve 12 / Endure 13
— Rusty Shiv | 1 AP | #Strike | 1d4

**Tags:** #Combat
