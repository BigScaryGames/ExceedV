# Combat Perk Design Guidelines

## Purpose
This document categorizes all existing combat perks to streamline future perk creation. Use these categories and examples as templates when designing new combat abilities.

---

## Perk Categories

### 1. AP Compression
Perks that combine multiple actions or reduce AP costs, improving action economy efficiency.

| Perk Name | Domain | Cost | AP Modification | Design Intent |
|-----------|--------|------|----------------|---------------|
| Double Strike | 1H | 5 XP | -2 AP (saves 2 AP) | Fast dual-wield attack with risk - if first is defended, second misses |
| Follow-Up Strike | 1H | 5 XP | -1 AP on consecutive strikes | Reward combo chains against single target |
| Shield Rush | Sh | 2 XP | 3-5 AP (saves 1 AP) | Charge attack: move twice + strike with double Might damage |
| Spear Charge | SaS | 15 XP | Combines movement + strike | Movement becomes damage, cavalry charge mechanic |
| Pushing Strike | SaS | 3 XP | +1 AP initially, 1 AP for shove | Strike + forced movement combo, maintain reach distance |
| Fast Archer | Arc | 5 XP | Aim as free action while moving | Mobile archer, shoot on the move (max Aim1) |
| Reactive | Universal | 20 XP | Gain second reaction | Massive action economy boost, highest cost compression perk |

**Design Notes:**
- AP compression is powerful - balance with restrictions or higher XP costs
- Most save 1-2 AP; Reactive doubles reactions for 20 XP premium
- Conditional compression (Follow-Up, Fast Archer) costs less than unconditional

---

### 2. Added Effects
Perks that apply conditions, forced movement, or status effects beyond basic damage.

| Perk Name | Domain | Cost | Effect Applied | Design Intent |
|-----------|--------|------|----------------|---------------|
| Calf Strike | SaS | 5 XP | Halve speed (save vs Might) | Mobility control, non-lethal takedown |
| Tripping Strike | SaS | 5 XP | Prone on hit (Dodge or fall) | Progression from Calf Strike, stronger control |
| Pushing Strike | SaS | 3 XP | Shove outside reach | Battlefield positioning with reach weapons |
| Behind the Shield Strike | Sh | 3 XP | Target -2 to parry/dodge | Use shield for offensive advantage |
| Perfect Block | Sh | 5 XP | Target off-guard on crit block | Reward excellent defense with vulnerability window |
| Dodge behind your back | Universal | 10 XP | Hidden + reposition on success | High-skill defensive maneuver with offensive payoff |
| Throwing Distraction | 1H | 10 XP | Target off-guard for ally | Sacrifice damage for tactical advantage |

**Design Notes:**
- Effects divided by severity: movement debuff < prone < off-guard
- Most require opposed checks or saving throws for balance
- Combo well with "Adding Damage" category for synergy
- Cost 3-10 XP based on effect power and requirements

---

### 3. Multiple Targets
Perks allowing attacks against more than one enemy.

| Perk Name | Domain | Cost | AP Cost | Target Count | Design Intent |
|-----------|--------|------|---------|--------------|---------------|
| Two Birds | Universal | 10 XP | +2 AP | 2 adjacent | Basic multi-target, requires Might investment |
| All the Birds | Universal | 15 XP | +4 AP | All in reach | Ultimate crowd control for high-level warriors |
| Monkey King Strike | SaS | 15 XP | +2 AP | Line (reach+1) | Cinematic acrobatic attack combining mobility |
| Double Shot | Arc | 10 XP | 4 AP total | 2 different targets | Ranged split fire, second at -2 to hit |
| Spinning Staff | SaS | 10 XP | 3 AP setup | All approaching enemies | Defensive zone creation, anti-swarm |

**Design Notes:**
- AP premium scales with target count: +2 AP for 2 targets, +4 AP for all
- Roll attack/damage once for efficiency (except Double Shot with penalty)
- Requires specific positioning (adjacent, reach, line)
- High-tier abilities (level 3-4 requirements)

---

### 4. Adding Damage
Perks that increase damage output through bonuses or die improvements.

| Perk Name              | Domain    | Cost        | Damage Bonus            | Conditions               | Design Intent                                      |
| ---------------------- | --------- | ----------- | ----------------------- | ------------------------ | -------------------------------------------------- |
| Piranha Strike         | 1H        | 10 XP       | +2 per damage die       | Target off-guard         | Rogue/assassin archetype, punish vulnerable        |
| The Edgelord           | Universal | 10 XP       | +2 flat                 | Edged weapons only       | Humorous "only one" mechanic with duel consequence |
| ==Shield Rush==        | ==Sh==    | ==2 XP==    | ==Double Might bonus==  | ==Movement required==    | ==Momentum-based damage, charge mechanic==         |
| ==Spear Charge==       | ==SaS==   | ==15 XP==   | ==+1 per meter moved==  | ==Straight line charge== | ==Distance becomes damage scalar==                 |
| Long Knives            | 1H        | 2 XP        | 1d4 → 1d6               | Knives/daggers only      | Make small weapons viable damage dealers           |
| Overpowered Draw       | Arc       | Outside PT4 | +1 per aim (cumulative) | Stationary               | Scaling damage for patient snipers                 |
| Close Quarters Shooter | Arc       | Outside PT4 | +Archery level          | Close range aimed        | Anti-intuitive close-range archer damage           |
| Tower                  | Arc       | 10 XP       | Free Aim1               | Didn't move 2 turns      | Stationary sniper bonus                            |

**Design Notes:**
- Conditional bonuses cost less than unconditional (Piranha vs Edgelord)
- Scaling bonuses (per die, per meter) more valuable than flat
- Die size increases cheapest (2 XP) for weapon-specific boosts
- Movement-based damage encourages tactical positioning

---

### 5. Critical Effects
Perks that trigger on critical success/failure or modify critical mechanics.

| Perk Name | Domain | Cost | Trigger | Effect | Design Intent |
|-----------|--------|------|---------|--------|---------------|
| Riposte | Universal | 5 XP | Crit defense or enemy crit fail | Free counter-strike | Punish mistakes, reward defense skill |
| Painful Parry | 1H | 5 XP | Critical parry success | Free light weapon strike | Dual-wielding defense reward |
| Perfect Block | Sh | 5 XP | Critical block success | Target off-guard | Create vulnerability window |
| Repose This, Repose That | Universal | 10 XP | Crit spell parry | Reflect spell at caster | Master-tier spell reflection |

**Design Notes:**
- All reward critical defense successes with counter-attacks or effects
- Cost 5-10 XP based on power level and requirements
- Create high-skill gameplay moments
- Defensive crits more common than offensive (doubles on 2/3 dice)
- **Missing Element:** No perks modify crit range or crit damage multipliers yet

---

### 6. Weapon Improvement
Perks that enhance weapon properties, stats, or capabilities.

| Perk Name              | Domain | Cost        | Improvement Type                    | Design Intent                             |
| ---------------------- | ------ | ----------- | ----------------------------------- | ----------------------------------------- |
| Grip Switch            | SaS    | 2 XP        | Free grip change (reach/long reach) | Tactical flexibility with pole weapons    |
| Long Knives            | 1H     | 2 XP        | Damage die increase (1d4→1d6)       | Make daggers viable                       |
| Throwing Hand          | 1H     | 2 XP        | +3 range, add throwing capability   | Enable ranged option for melee weapons    |
| Multipurpose Shield    | Sh     | 3 XP        | Strike without losing defense bonus | Sword-and-board offense without sacrifice |
| Quarter-staff Training | SaS    | 10 XP       | +1 to all defenses                  | Make defensive staff builds viable        |
| Artillery              | Arc    | Outside PT4 | Range = Aim, double aim value       | Extreme range sniper                      |
| Defensive Archer       | Arc    | 5 XP        | Parry with bow (no break risk)      | Melee defense for ranged characters       |

**Design Notes:**
- Cheap improvements (2-3 XP) for basic weapon function
- Defensive bonuses more expensive (10 XP for +1 all defenses)
- Cross-category capabilities (melee → ranged) enable build variety
- Stat improvements balanced by weapon-type restrictions

---

### 7. Reaction Attacks
Perks that enable counter-attacks, opportunity strikes, or reaction-based offense.

| Perk Name          | Domain    | Cost      | Trigger                         | Design Intent                            |
| ------------------ | --------- | --------- | ------------------------------- | ---------------------------------------- |
| Riposte            | Universal | 5 XP      | Crit defense or enemy crit fail | Classic counter-strike mechanic          |
| Reactive Strike    | Universal | 10 XP     | Enemy strides/runs away         | Punish tactical retreats, control space  |
| ==Pointy stick==   | ==SaS==   | ==5 XP==  | ==Enemy enters reach==          | ==Anti-charge defense, prepared action== |
| ==Spinning Staff== | ==SaS==   | ==10 XP== | ==Each enemy approaches== <br>  | ==Create defensive zone, anti-swarm==    |
| Painful Parry      | 1H        | 5 XP      | Critical parry                  | Dual-wielding counter                    |

**Design Notes:**
- Cost 5-10 XP based on trigger frequency
- Require reaction resource (limited per turn)
- Pair well with Reactive perk (second reaction) for 20 XP investment
- Enable defensive playstyles with offensive output

---

### 8. Defensive Abilities
Perks that improve defenses, provide new defense options, or protect allies.

#### Solo Defense

| Perk Name | Domain | Cost | Defense Type | Design Intent |
|-----------|--------|------|--------------|---------------|
| Dodging Step | Universal | 5 XP | +1 dodge + movement | Mobility during defense |
| Dodge behind your back | Universal | 10 XP | Stealth defense + reposition | High-skill tactical maneuver |
| Dodge-Roll | Universal | 10 XP | +3 vs AOE, fall prone | Specialized AOE defense |
| Projectile Parry | Universal | 5 XP | Parry ranged attacks | Extend parry to projectiles |
| Parry This, Parry that | Universal | 10 XP | Parry magic (Lines/Rays/Bursts/Cones) | Anime-style magical deflection |
| Repose This, Repose That | Universal | 10 XP | Reflect spells on crit | Master-tier spell reflection |
| Shield Block | Sh | Free | Reduce damage by Shield Negation | Shields always help even on failure |
| Quarter-staff Training | SaS | 10 XP | +1 all defenses | Make defensive staff viable |
| Twin Parry | 1H | 3 XP | +1 parry when dual wielding | Defensive dual-wielding option |
| Defensive Archer | Arc | 5 XP | Parry with bow | Melee defense for ranged |

#### Ally Protection

| Perk Name | Domain | Cost | Protection Type | Design Intent |
|-----------|--------|------|----------------|---------------|
| Watching your back | Universal | 5 XP | Adjacent allies can't be flanked | Basic team support |
| That Type of a Person | Universal | 5 XP | Rush to downed ally, take attacks | Self-sacrifice mechanic |
| Shield Warden | Sh | 5 XP | Use Shield Block for allies | Share shield defense |
| Shield Guardian | Sh | 10 XP | Block attacks for adjacent allies | Advanced protection, works on AOE |
| The Wall | Sh | 15 XP | Allies hide behind you, use your defense | Ultimate tank, heavy shield fortress |
| Spell Guard | Sh | 5 XP (1 Limit) | Block magical effects for self/allies | Anti-mage shield build |
| The Guardian Aura | Sh | 10 XP (2 Limit) | Grant advantage to allies in 3 tiles | Master protector, paladin-style aura |

**Design Notes:**
- Solo defenses: 5-10 XP, scale with versatility
- Ally protection: 5-15 XP, scale with protection scope
- Spell Guard/Guardian Aura use Limit resource (magic system)
- Clear progression: Warden → Guardian → Wall
- Shield domain identity: ultimate protector

---

### 9. Attribute Substitution
Perks that allow using different attributes for attacks or checks.

| Perk Name | Domain | Cost | Substitution | Design Intent |
|-----------|--------|------|-------------|---------------|
| Throwing Hand | 1H | 2 XP | Dexterity for thrown attacks | Enable throwing build with finesse |
| Zen Archer | Arc | 5 XP | Perception instead of Dexterity for bows | Wisdom-archer archetype, awareness shooter |

**Design Notes:**
- Rare category with only 2 examples
- Opens alternative attribute paths for builds
- Cost 2-5 XP (cheap since doesn't directly improve power)
- Enables concept diversity (wise archer, agile thrower)
- **Missing Element:** No Might-based alternatives yet (e.g., heavy throw using Might)

---

### 10. Team Support & Leadership
Perks that buff allies, coordinate tactics, or provide shared benefits.

| Perk Name | Domain | Cost | Support Type | Design Intent |
|-----------|--------|------|-------------|---------------|
| Spear Brothers | SaS | 3 XP | +1 to all SaS checks when adjacent | Phalanx formation bonus |
| Throwing Distraction | 1H | 10 XP | Make target off-guard for ally | Tactical teamwork, sacrifice damage |
| Don't Turn Your Back on Me | Arc | 10 XP | Count as flanking at range | Ranged positioning for flanking |
| The Leader | Universal | 5 XP | Share fear resistance | Inspire courage mechanic |
| The Cult Leader | Universal | 10 XP | Drive followers into Fervor (+2 atk/-3 def) | Fanatic leadership archetype |
| The Cult Inner Member | Universal | Free | Mind control resistance, protect leader | Paired perk with risk-reward trade-off |
| Shield Guardian | Sh | 10 XP | Block for allies, works on AOE | Advanced team protection |
| The Guardian Aura | Sh | 10 XP (2 Limit) | Advantage to allies in 3 tiles | Area buff mechanic |

**Design Notes:**
- Some require pairing (Cult Leader/Member, Spear Brothers)
- Cost 3-10 XP based on benefit scope
- Mix of positioning bonuses and active abilities
- Leadership chain creates party role identity
- Shield domain has strongest ally protection suite

---

### 11. Mobility & Utility
Perks that enhance movement, positioning, or provide non-combat benefits.

| Perk Name | Domain | Cost | Benefit | Design Intent |
|-----------|--------|------|---------|---------------|
| Staff Acrobat | SaS | 2 XP | +reach to long jump, half to high jump, +2 balance | Parkour with pole weapons |
| Walking Stick | SaS | Free | Heavy weapons don't count to encumbrance | Make pole weapons viable for travelers |
| Ready Hand | 1H | Free | Draw weapon on initiative even when ambushed | Quick-draw specialist |
| Grip Switch | SaS | 2 XP | Free grip change (reach adjustment) | Tactical flexibility |

**Design Notes:**
- Mostly cheap or free (2 XP or starting perks)
- Enable specific character concepts (traveler, quick-draw artist)
- Support rather than combat-focused
- Walking Stick unique: encumbrance management
- Staff Acrobat pairs with Monkey King Strike (15 XP mobility attack)

---

### 12. Narrative Abilities
GM-mediated special mechanics with story integration.

| Perk Name | Domain | Cost | Effect | Design Intent |
|-----------|--------|------|--------|---------------|
| Plot Armor | Universal | 50 XP | Heroic destiny protection | Most expensive perk, pure protagonist shield |
| The Aspiring Hero | Universal | 10 XP | Cheat death (lose 10 CP + take limitation) | Death prevention with real cost |
| Too Selfish | Universal | Free (instant) | Bargain with Master of Universe on protection failure | Dramatic "can't lose you" moment |
| The Loner | Universal | 20 XP | +2 AP solo, can't have allies | Solo archetype with permanent drawback |
| The Edgelord | Universal | 10 XP | +2 damage, must duel other Edgelords | Humorous "there can be only one" mechanic |

**Design Notes:**
- Most expensive perks (10-50 XP) or free instant-use
- Require GM permission/mediation
- Some have permanent drawbacks (Loner, Edgelord duel consequence)
- Aspiring Hero has CP cost on use (lose 10 CP when activated)
- Enable cinematic moments and protagonist protection

---

### 13. Spell Integration
Perks that combine martial abilities with magic system.

| Perk Name | Domain | Cost | Integration Type | Design Intent |
|-----------|--------|------|-----------------|---------------|
| Spell Guard | Sh | 5 XP (1 Limit) | Block magical effects with shield | Anti-mage tank, uses magic resource |
| The Guardian Aura | Sh | 10 XP (2 Limit) | Share magical protection in area | Paladin-style protective aura |
| Repose This, Repose That | Universal | 10 XP | Reflect spells on critical parry | Ultimate spell-deflection mastery |
| Spell Shot | Arc | Outside PT4 | Store single-target spell in arrow | Arcane archer concept |

**Design Notes:**
- Uses Limit resource (magic system) for shield perks
- Enables gish builds (warrior-mage hybrids)
- Shield + magic combination creates unique tank role
- Spell Shot outside current scope but shows future direction
- Parry magic chain: Projectile Parry → Parry This → Repose This

---

## Domain Identity Summary

### Universal Combat
**Identity:** Mastery of fundamentals, leadership, reactions, multi-target control

**Key Features:**
- Reaction attacks (Riposte, Reactive Strike)
- Second reaction (Reactive - 20 XP)
- Multi-target strikes (Two Birds → All the Birds)
- Parry progression (Projectile → Magic → Reflect)
- Leadership mechanics (The Leader, Cult system)
- Ultimate protection (That Type of a Person → Too Selfish)

**Cost Range:** 5-50 XP (Plot Armor highest at 50)

---

### Staves & Spears (SaS)
**Identity:** Reach control, mobility, crowd control, defensive techniques, acrobatics

**Key Features:**
- Free starting perk (Walking Stick - encumbrance)
- Grip flexibility (Grip Switch - 2 XP)
- Control effects (Calf Strike → Tripping Strike)
- Mobility attacks (Staff Acrobat → Monkey King Strike)
- Zone control (Pointy stick, Spinning Staff)
- Formation bonuses (Spear Brothers)
- Charge attacks (Spear Charge)

**Cost Range:** 2-15 XP
**Status:** Fully implemented for PT4

---

### One-Handed (1H)
**Identity:** Dual wielding, precision, throwing, combo chains, versatility

**Key Features:**
- Free starting perk (Ready Hand - quick draw)
- Dual-wield mechanics (Twin Parry, Double Strike, Painful Parry)
- Throwing specialization (Throwing Hand, Throwing Distraction)
- Combo attacks (Follow-Up Strike - AP compression)
- Precision damage (Piranha Strike vs off-guard)
- Weapon versatility (Long Knives die upgrade)

**Cost Range:** 2-10 XP
**Status:** Fully implemented for PT4

---

### Two-Handed (2H)
**Identity:** Power attacks, cleaving, heavy damage, knockback

**Key Features:**
- Free starting perk (Half-Sword Strike - accuracy option)
- **STATUS:** Flagged as incomplete, only 1 perk implemented
- **HEAP concepts:** Powerful Smack, Charge, Cleave, Grievous Wounds, Whirlwind, Send them Flying

**Cost Range:** TBD
**Status:** Outside PT4 scope, needs full implementation

---

### Shield (Sh)
**Identity:** Ultimate protection, ally defense, magic blocking, fortress tank

**Key Features:**
- Free starting perk (Shield Block - damage reduction)
- Offense without sacrifice (Multipurpose Shield, Behind the Shield Strike)
- Protection progression (Warden → Guardian → Wall)
- Critical block rewards (Perfect Block)
- Magic defense (Spell Guard → Guardian Aura using Limit)
- Charge attacks (Shield Rush)

**Cost Range:** 2-15 XP (plus Limit costs for magic perks)
**Status:** Fully implemented for PT4, strongest ally protection suite

---

### Archery (Arc)
**Identity:** Precision, stationary bonuses, multi-shot, spell integration

**Key Features:**
- Attribute substitution (Zen Archer - Perception instead of Dex)
- Mobile shooting (Fast Archer)
- Stationary bonuses (Tower - free Aim1)
- Multi-target (Double Shot)
- Extreme range (Artillery)
- Melee defense (Defensive Archer)
- **STATUS:** Flagged as "almost unedited from v1" and "poorly organized"

**Cost Range:** 5-10 XP (implemented perks only)
**Status:** Marked for complete remake before PT5, many perks outside PT4 scope

---

### Unarmed (Not Yet Implemented)
**Status:** Outside PT4 scope, no implemented perks

---

## XP Cost Guidelines

### By Price Tier

| XP Cost | Perk Count | Typical Effect |
|---------|-----------|---------------|
| Free | 5 | Starting perks, paired perks, instant-use narrative |
| 2 XP | 6 | Basic utility, weapon improvements, simple bonuses |
| 3 XP | 6 | Team support, basic offensive enhancements |
| 5 XP | 19 | Standard combat abilities, defense options, reaction attacks |
| 10 XP | 15 | Advanced techniques, multi-target attacks, critical effects |
| 15 XP | 4 | Ultimate abilities with high requirements |
| 20 XP | 2 | Game-changing mechanics (Reactive, The Loner) |
| 50 XP | 1 | Plot Armor (narrative protection) |

### By Category Average

| Category | Average Cost | Range |
|----------|-------------|-------|
| Utility/Mobility | 2 XP | Free-2 XP |
| Weapon Improvement | 4 XP | 2-10 XP |
| Added Effects | 5 XP | 3-10 XP |
| Defensive Abilities | 6 XP | Free-15 XP |
| Reaction Attacks | 7 XP | 5-10 XP |
| Multiple Targets | 12 XP | 10-15 XP |
| AP Compression | 9 XP | 2-20 XP |
| Narrative Abilities | 20 XP | Free-50 XP |

---

## Requirement Patterns

### Attribute Requirements
- **Single Attribute:** Entry-level perks (AG 2, MG 1)
- **Attribute + Domain:** Standard requirement (AG 3 + MD 3)
- **Multiple Attributes:** High-tier perks (MG 5 + WL 3)
- **Skill Requirements:** Specialized perks (Stealth 4, Leadership 3)

### Domain Level Requirements
- **Level 1:** Starting perks, basic abilities (free-5 XP)
- **Level 2:** Intermediate techniques (5-10 XP)
- **Level 3:** Advanced abilities (10-15 XP)
- **Level 4:** Master techniques (15+ XP)

### Prerequisite Chains
Many perks form progression chains requiring previous perks:
- Dodging Step → Dodge-Roll / Dodge behind your back
- Projectile Parry → Parry This → Repose This
- Calf Strike → Tripping Strike
- Shield Warden → Shield Guardian → The Wall
- Two Birds → All the Birds
- The Leader → The Aspiring Hero / The Cult Leader

---

## Design Patterns & Insights

### Action Economy Focus
- 7 perks directly modify AP costs
- Reactive (20 XP) doubles reaction capacity
- Most compression saves 1-2 AP
- Conditional compression costs less than unconditional

### Critical Success Rewards
- 4 perks trigger on critical defense success
- All provide counter-attacks or conditions
- Creates high-skill gameplay moments
- Defensive crits more accessible (2/3 dice)

### Conditional vs Unconditional
- **Conditional bonuses:** Lower XP cost, higher potential (Piranha Strike +2/die vs off-guard)
- **Unconditional bonuses:** Higher XP cost, reliable (The Edgelord +2 always)
- **Setup requirements:** Moderate cost (Tower - free Aim1 if stationary)

### Team vs Solo Balance
- **Team perks:** 11 perks support allies (5-10 XP typical)
- **Solo perks:** The Loner (20 XP) provides +2 AP but restricts allies
- **Paired perks:** Cult system, Spear Brothers require coordination

### Multi-Target Premium
- Basic 2-target: +2 AP cost, 10 XP (Two Birds)
- All targets: +4 AP cost, 15 XP (All the Birds)
- Requires high attributes (MG 3-4) and domain level (3-4)
- Roll once for efficiency

### Defensive Depth
- 18 defensive perks across all categories
- Shield domain = ultimate protector identity
- Universal = defense mastery progression
- Each domain has unique defensive option

### Limit Resource Integration
- 2 perks use Limit (Shield magic defense)
- Creates warrior-mage hybrid option
- Spell Guard (1 Limit) basic, Guardian Aura (2 Limit) advanced
- Opens gish build path

---

## Missing Elements & Future Design Space

### Identified Gaps

1. **Critical Range/Multiplier Modifiers**
   - No perks increase critical range (e.g., "crit on 17-20")
   - No perks modify critical damage multipliers
   - Design space for glass cannon builds

2. **Attribute Substitution Variety**
   - Only 2 perks (Throwing Hand, Zen Archer)
   - Missing: Might-based throwing, Will-based intimidation strikes
   - Design space for unusual attribute combinations

3. **Two-Handed Domain**
   - Only 1 implemented perk (Half-Sword Strike)
   - Needs: Cleave, Knockback, Power Attack, Whirlwind
   - Flagged outside PT4 scope

4. **Unarmed Domain**
   - No implemented perks
   - Outside PT4 scope entirely

5. **Archery Domain**
   - Needs complete remake (flagged "poorly organized")
   - Many concepts outside PT4 scope
   - Spell Shot interesting but not implemented

6. **Spell Integration**
   - Limited examples (Shield magic defense, Spell Shot concept)
   - Design space for arcane archer, spell blade, etc.
   - Could use Limit resource for hybrid builds

7. **Debuff/Status Effect Variety**
   - Current: Prone, Off-guard, Speed reduction, Hidden
   - Missing: Bleed, Daze, Stun, Blind, Fear (combat application)
   - Design space for condition specialists

8. **Resource Management**
   - Limit used minimally (2 perks)
   - HP-costing abilities? Stamina costs?
   - Risk-reward mechanics underexplored

9. **Movement-Based Attacks**
   - Spear Charge and Shield Rush only examples
   - Design space: Leap attacks, sliding strikes, momentum builds

10. **Critical Failure Exploitation**
    - Riposte triggers on enemy crit fail
    - Design space for abilities that worsen enemy failures

### Concepts in HEAP (Not Yet Implemented)
From 2.X Martial Perks and old concepts HEAP.md:
- Powerful Smack (double weapon damage)
- Cleave (kill → free attack chain)
- Improved Criticals (add conditions to crits)
- Grievous Wounds (worsen consequence rolls)
- Danger Zone / Whirlwind (stance + multi-target)
- Send them Flying (knockback on bludgeoning)
- Weapon's Weight (jumping charge with distance damage)

---

## Perk Creation Checklist

When designing a new combat perk:

### 1. Categorize Primary Function
- [ ] Which category? (AP Compression, Added Effects, Multiple Targets, etc.)
- [ ] Does it fit domain identity?
- [ ] Is this category underrepresented in the domain?

### 2. Define Requirements
- [ ] Domain level requirement (1-5)?
- [ ] Attribute requirements (which attributes, what values)?
- [ ] Prerequisite perks (if part of progression chain)?
- [ ] Skill requirements (if applicable)?
- [ ] Special requirements (GM permission, paired perk)?

### 3. Set XP Cost
- [ ] Compare to similar perks in same category
- [ ] 2 XP: Basic utility/improvement
- [ ] 5 XP: Standard ability
- [ ] 10 XP: Advanced technique
- [ ] 15+ XP: Ultimate ability or game-changer
- [ ] Adjust for conditions/restrictions (lower if conditional)

### 4. Define AP Cost/Modification
- [ ] Does it change AP costs?
- [ ] Compression: -1 to -2 AP typical
- [ ] Premium: +1 to +4 AP for multi-target
- [ ] Setup: 1-3 AP preparation
- [ ] Free action: Part of another action

### 5. Balance Mechanics
- [ ] Conditional vs unconditional effect?
- [ ] Opposed check or automatic?
- [ ] Duration (instant, 1 turn, until end of combat)?
- [ ] Resource cost beyond XP (Limit, HP, Stamina)?
- [ ] Drawbacks or limitations?

### 6. Consider Synergies
- [ ] Does it combo with existing perks?
- [ ] Does it create a progression chain?
- [ ] Does it enable a specific build archetype?
- [ ] Does it pair with specific equipment?

### 7. Check Domain Identity
- [ ] Does it reinforce domain theme?
- [ ] Universal: Reactions, multi-target, leadership, mastery?
- [ ] SaS: Reach, mobility, control, acrobatics?
- [ ] 1H: Dual wield, precision, combos, throwing?
- [ ] 2H: Power, cleave, knockback, heavy damage?
- [ ] Sh: Protection, ally defense, fortress tank?
- [ ] Arc: Precision, range, multi-shot, mobility?

### 8. Name & Flavor
- [ ] Clear, evocative name describing function
- [ ] Consistent naming with domain perks
- [ ] Flavor text explaining technique or concept

### 9. Compare to Examples
- [ ] Find 2-3 perks in same category
- [ ] Compare XP cost, requirements, power level
- [ ] Ensure consistency with established patterns

### 10. Playtest Considerations
- [ ] Will this be fun to use?
- [ ] Does it create interesting tactical decisions?
- [ ] Is it clear when to use this vs other options?
- [ ] Does it overshadow existing perks or become mandatory?

---

## Quick Reference: Perk Templates by Category

### Template: AP Compression
**Name:** [Action Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [5-20 XP based on power]
**AP Cost:** [Original Cost - 1 to 2 AP] OR [Combines X + Y actions]
**Effect:** [Describe combined actions or AP reduction]
**Conditions/Limitations:** [e.g., "only against same target," "requires movement"]

**Example:** Follow-Up Strike (1H2, 5 XP): After hitting, next strike vs same target -1 AP

---

### Template: Added Effects
**Name:** [Strike/Attack Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [3-10 XP based on effect severity]
**AP Cost:** [Base Strike AP +0 to +2 AP]
**Effect:** On hit, [condition/forced movement/status effect]
**Resistance:** [Target rolls Attribute vs your Attribute/DC] OR [Automatic if hit]
**Duration:** [Instant/1 turn/End of target's turn/Until removed]

**Example:** Tripping Strike (SaS2, 5 XP, +1 AP): On hit, target Dodges or falls prone

---

### Template: Multiple Targets
**Name:** [Area/Multi Attack Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level 3-4], [High Attributes], [Prerequisite Perks]
**Cost:** [10-15 XP]
**AP Cost:** [Base Strike AP +2 to +4 AP]
**Target Count:** [2 adjacent / All in reach / Line / Cone]
**Roll Method:** [Single roll for all OR separate rolls with penalties]
**Positioning Requirements:** [Adjacent/reach/range restrictions]

**Example:** Two Birds (Universal, MG3+AG2, 10 XP, +2 AP): Strike 2 adjacent targets, roll once

---

### Template: Adding Damage
**Name:** [Strike/Technique Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [2-15 XP based on conditions and scaling]
**Damage Bonus:** [+X flat / +X per die / +X per meter / Die size increase]
**Conditions:** [Unconditional / Target off-guard / Movement required / Stationary / etc.]
**Stacking:** [Does it stack with other damage bonuses?]

**Example:** Piranha Strike (1H2, 10 XP): +2 per damage die vs off-guard targets

---

### Template: Critical Effects
**Name:** [Critical Technique Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level 2-4], [High Attributes], [Prerequisite Perks]
**Cost:** [5-10 XP]
**Trigger:** [Critical success on attack/defense / Enemy critical failure]
**Effect:** [Free counter-strike / Apply condition / Reflect / Special effect]
**Limitations:** [Uses reaction? Once per turn?]

**Example:** Riposte (Universal, AG3+MD3, 5 XP): Crit defense or enemy crit fail → free strike

---

### Template: Weapon Improvement
**Name:** [Mastery/Enhancement Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes]
**Cost:** [2-10 XP based on improvement scope]
**Weapon Restriction:** [Specific weapons / Weapon category]
**Improvement Type:** [+X to defenses / Die size increase / Range increase / Add capability / Free action]

**Example:** Long Knives (1H1, 2 XP): Knives/daggers deal 1d6 in your hands

---

### Template: Reaction Attack
**Name:** [Counter/Opportunity Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [5-10 XP based on trigger frequency]
**Trigger:** [Enemy action that provokes]
**Action Cost:** [Uses reaction]
**Effect:** [Strike as reaction / Prepared strike / Zone control]

**Example:** Reactive Strike (Universal, AG2+MD2, 10 XP): Strike enemies that stride/run away

---

### Template: Defensive Ability (Solo)
**Name:** [Defense Technique Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [5-10 XP]
**Defense Type:** [Enhance existing / New defense option / Situational bonus]
**Bonus/Effect:** [+X to defense / Extend defense to new attack types / Add movement]
**Conditions:** [Always active / Specific attack types / Positioning requirements]

**Example:** Dodging Step (Universal, AG2, 5 XP): +1 dodge and make a step

---

### Template: Defensive Ability (Ally Protection)
**Name:** [Guardian/Protector Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [5-15 XP based on protection scope]
**Protection Range:** [Adjacent / 3 tiles / Line of sight]
**Protection Type:** [Block for ally / Share defense / Grant bonus / Take damage]
**Action Cost:** [Reaction / Free action / Setup action]

**Example:** Shield Guardian (Sh2, 10 XP): Reaction to block attacks for adjacent allies

---

### Template: Team Support
**Name:** [Support/Leadership Name]
**Domain:** [Universal/1H/2H/SaS/Sh/Arc]
**Requirements:** [Domain Level], [Attributes], [Skill Requirements], [Prerequisite Perks]
**Cost:** [3-10 XP based on benefit scope]
**Benefit Type:** [Positioning bonus / Shared defense / Advantage creation / Buff]
**Range:** [Adjacent / Line of sight / Area]
**Duration:** [Always active / 1 turn / Until combat ends]
**Limitations:** [Requires positioning / Paired perk / Action cost]

**Example:** Spear Brothers (SaS1, 3 XP): Adjacent spearman with perk grants +1 to all SaS checks

---

### Template: Narrative Ability
**Name:** [Heroic/Fate Name]
**Domain:** Usually Universal
**Requirements:** GM Permission (almost always), [Domain Level], [Attributes], [Prerequisite Perks]
**Cost:** [10-50 XP] OR [Free for instant-use]
**Effect:** [Dramatic story-level effect]
**Limitations/Drawbacks:** [Permanent restrictions / CP cost on use / Opposed drawback]
**GM Mediation:** [How GM determines outcome or consequence]

**Example:** The Aspiring Hero (Universal, Lead3+The Leader+GM, 10 XP): Instant. Cheat death by losing 10 CP and taking GM-chosen limitation

---

## Domain-Specific Design Guidelines

### Universal Combat Perks
**When to use Universal:**
- Fundamental techniques any warrior could learn
- Leadership and team coordination
- Mastery-level abilities requiring high investment
- Multi-target attacks available to all
- Reaction-based techniques
- Ultimate defense options (parry magic, second reaction)

**Design Philosophy:**
- Accessible to all martial characters
- Often has higher requirements to show mastery
- Expensive perks (15-50 XP) for game-changing abilities
- Clear progression chains (dodge, parry, multi-target)

---

### Staves & Spears (SaS) Perks
**When to use SaS:**
- Reach-based tactics and zone control
- Mobility enhancements and acrobatic moves
- Control effects (trip, slow, push)
- Formation bonuses and coordinated fighting
- Versatile grip and weapon handling

**Design Philosophy:**
- Emphasize reach advantage
- Mobile combatants (Staff Acrobat → Monkey King Strike)
- Defensive versatility (Spinning Staff, Pointy stick)
- Travelers and explorers (Walking Stick encumbrance)
- Cost range: 2-15 XP, mostly 5-10 XP sweet spot

**Avoid:**
- Pure damage boosts without tactical elements
- Static, immobile techniques (belongs in 2H or Tower archery)
- Heavy armor synergies (belongs in Shield)

---

### One-Handed (1H) Perks
**When to use 1H:**
- Dual-wielding mechanics
- Precision and finesse techniques
- Combo attacks and action chains
- Throwing weapon integration
- Speed and versatility

**Design Philosophy:**
- Fastest weapons, quick combos (Follow-Up Strike, Double Strike)
- Precision over power (Piranha Strike vs off-guard)
- Versatile weapon options (knives, swords, axes, thrown)
- Critical-based counters (Painful Parry)
- Cost range: 2-10 XP, affordable and accessible

**Avoid:**
- Multi-target cleaves (belongs in 2H or Universal Two Birds)
- Heavy armor reliance (belongs in Shield)
- Long reach tactics (belongs in SaS)

---

### Two-Handed (2H) Perks
**When to use 2H:** *(Currently limited implementation)*
- Raw power and high damage
- Cleaving through multiple enemies
- Knockback and forced movement
- Grievous wounds and critical damage
- Overwhelming force tactics

**Design Philosophy:** *(Inferred from HEAP concepts)*
- Highest damage potential
- Multi-target through cleave chains
- Momentum-based attacks (charge, leap)
- Risk-reward (accuracy for power, or vice versa)
- Currently: Half-Sword Strike shows accuracy trade-off option

**Future Direction:**
- Powerful Smack, Cleave, Whirlwind, Send them Flying
- Grievous Wounds (worsen consequences)
- Weapon's Weight (momentum damage)

---

### Shield (Sh) Perks
**When to use Shield:**
- Ultimate protection and tanking
- Ally defense and bodyguard roles
- Shield as weapon integration
- Magic blocking and anti-caster
- Critical blocks and counterplay

**Design Philosophy:**
- Strongest ally protection in game (Warden → Guardian → Wall)
- Shield as offensive tool (Multipurpose, Behind the Shield, Shield Rush)
- Magic defense using Limit (Spell Guard → Guardian Aura)
- Critical blocks create openings (Perfect Block)
- Free starting perk (Shield Block) ensures shields always help
- Cost range: 2-15 XP, progression-heavy

**Avoid:**
- High mobility builds (shield = heavy)
- Ranged attack focus
- Solo DPS optimization (shield = team protector identity)

---

### Archery (Arc) Perks
**When to use Archery:** *(Needs remake, current guidelines)*
- Precision ranged attacks
- Aiming and patient shooting
- Multi-shot and target switching
- Mobility vs stationary trade-offs
- Spell integration (future)

**Design Philosophy:** *(Under revision)*
- Attribute substitution (Zen Archer - Perception-based)
- Stationary bonuses (Tower) vs mobile shooting (Fast Archer)
- Extreme range options (Artillery)
- Melee defense for ranged (Defensive Archer)
- **Current Status:** Flagged for complete remake before PT5

**Future Direction:**
- Better organization needed
- Spell Shot integration (store spell in arrow)
- Many abilities currently outside PT4 scope
- Need clear identity separate from thrown weapons (1H) and spells

---

## Balance Considerations

### Power Budget Guidelines

#### Cheap Perks (2-3 XP)
**Should provide:**
- Minor utility bonuses (+2 to specific check)
- Weapon-specific improvements (die size, range)
- Basic team support (formation bonuses)
- Enabling capabilities (add throwing, free grip switch)

**Should NOT provide:**
- Direct combat advantage without restrictions
- Multi-target attacks
- Significant damage boosts
- Action economy improvements

**Examples:** Long Knives (1d4→1d6), Grip Switch (free grip change), Spear Brothers (+1 adjacent)

---

#### Standard Perks (5 XP)
**Should provide:**
- Solid combat techniques with clear use cases
- Basic reaction attacks
- Defense option expansions (parry ranged)
- Conditional damage bonuses
- Added effects with opposed checks

**Should NOT provide:**
- Unconditional major damage boosts
- Multi-target without restrictions
- Action economy game-changers

**Examples:** Riposte (counter on crit), Dodging Step (+1 dodge + move), Pointy stick (prepared strike)

---

#### Advanced Perks (10 XP)
**Should provide:**
- Strong tactical abilities
- Multi-target attacks (2 targets)
- Significant conditional bonuses
- Advanced defense options (parry magic)
- Action economy improvements with restrictions

**Should NOT provide:**
- Overwhelming power without counterplay
- Unconditional auto-win conditions

**Examples:** Parry This Parry that (parry magic), Double Shot (2 targets), Piranha Strike (+2/die vs off-guard)

---

#### Ultimate Perks (15-20 XP)
**Should provide:**
- Build-defining abilities
- Game-changing mechanics
- Multi-target all in reach
- Second reaction
- Major narrative abilities

**May include:**
- Permanent drawbacks (The Loner)
- High attribute requirements (MG 5, WL 3)
- Multiple prerequisite perks
- Domain level 4-5 requirements

**Examples:** All the Birds (all in reach), Reactive (2nd reaction), The Loner (+2 AP solo)

---

#### Legendary Perks (50 XP)
**Should provide:**
- Pure narrative protection
- GM-mediated story effects
- Character-defining identity

**Current Example:** Plot Armor (50 XP, GM permission, heroic destiny)

---

### Conditional vs Unconditional Balance

#### Unconditional Benefits (More Expensive)
- The Edgelord: +2 damage (no conditions) = 10 XP
- Reactive: +1 reaction (always active) = 20 XP
- Long Knives: 1d6 damage (always with daggers) = 2 XP (weapon-specific balances)

#### Conditional Benefits (Less Expensive)
- Piranha Strike: +2/die vs off-guard (requires setup) = 10 XP (higher burst potential)
- Tower: Free Aim1 if stationary (positioning requirement) = 10 XP
- Follow-Up Strike: -1 AP against same target (requires consecutive hits) = 5 XP

**Design Rule:** Conditional benefits can be more powerful for same XP cost, but require setup/positioning/combat state

---

### AP Cost Balance

#### AP Compression Value
- Saving 1 AP ≈ 5 XP value
- Saving 2 AP ≈ 10-15 XP value
- Additional reaction ≈ 20 XP value (Reactive perk)

#### Multi-Target AP Premium
- +2 AP for 2 targets (Two Birds)
- +4 AP for all targets (All the Birds)
- Roll once for efficiency (don't multiply AP by target count)

#### Setup Action Costs
- 1 AP setup (Pointy stick) for reaction strike = 5 XP
- 3 AP setup (Spinning Staff) for multiple reaction strikes = 10 XP

**Design Rule:** AP compression must have restrictions, high XP cost, or both

---

### Damage Scaling Balance

#### Flat Bonuses
- +2 damage unconditional = 10 XP (The Edgelord)
- +Might bonus again = 2 XP (Shield Rush, includes movement)

#### Scaling Bonuses
- +2 per damage die (conditional) = 10 XP (Piranha Strike)
- +1 per meter moved = 15 XP (Spear Charge, requires charge line)
- +Archery level at close range = Outside PT4 (Close Quarters Shooter)

#### Die Size Increases
- 1d4 → 1d6 (weapon-specific) = 2 XP (Long Knives)

**Design Rule:** Scaling bonuses more valuable than flat, cost more or require conditions

---

### Defense Bonus Balance

#### Single Defense Type
- +1 to one defense (Dodging Step includes movement) = 5 XP
- +1 circumstance bonus dual wielding (Twin Parry) = 3 XP (requires 2 weapons)

#### All Defenses
- +1 to all defenses (Quarter-staff Training, weapon-specific) = 10 XP

#### New Defense Options
- Extend defense to new attack type (Projectile Parry) = 5 XP
- Parry magic (Parry This Parry that, high requirements) = 10 XP

**Design Rule:** Defense bonuses expensive because they apply to many situations; all-defenses = 2x single-defense cost

---

### Ally Protection Balance

#### Basic Protection (5 XP)
- Prevent flanking adjacent allies (Watching your back)
- Use Shield Block for allies (Shield Warden)

#### Advanced Protection (10 XP)
- Block attacks for adjacent allies (Shield Guardian, works on AOE)
- Rush to downed ally and take hits (That Type of a Person, permanent commitment)

#### Ultimate Protection (15 XP)
- Allies hide behind you (The Wall, heavy shield, level 3)
- Area advantage granting (Guardian Aura, 2 Limit cost)

**Design Rule:** Protection scope determines cost - adjacent < area < unconditional

---

### Resource Cost Integration

#### Limit Costs (Magic System)
- 1 Limit = Basic persistent effect (Spell Guard, 5 XP)
- 2 Limit = Advanced area effect (Guardian Aura, 10 XP)

**Design Rule:** Limit costs allow powerful persistent effects but compete with spell slots

#### CP Costs on Use
- Aspiring Hero: Lose 10 CP when cheating death (one-time cost)

**Design Rule:** Pay-per-use with CP creates powerful emergency buttons with real cost

#### Reaction Costs
- Most reaction attacks use the reaction resource
- Reactive perk (20 XP) provides second reaction for action economy

**Design Rule:** Reaction cost balances powerful triggered abilities

---

## Common Design Mistakes to Avoid

### 1. Forgetting Domain Identity
**Bad:** Giving one-handed domain a cleaving multi-target attack
**Why:** Cleaving = two-handed identity, one-handed = precision and combos
**Fix:** Use multi-target via speed/combos (Double Strike) not raw power

### 2. Conditional Without Benefit
**Bad:** 10 XP perk with +2 damage, requires prone + off-guard + flanking
**Why:** Conditions too restrictive for reward level
**Fix:** Either easier condition or higher reward (+4 damage or critical effect)

### 3. Unconditional Power Too Cheap
**Bad:** 3 XP perk with +2 damage to all attacks
**Why:** No conditions make it auto-pick, undercosted for power
**Fix:** Either add conditions (vs off-guard) or increase cost (10 XP)

### 4. AP Compression Too Strong
**Bad:** 5 XP perk: Strike 3 times for 4 AP total
**Why:** Saves 5 AP (normal = 9 AP), worth ~25 XP value
**Fix:** Reduce to 2 strikes for 4 AP (saves 2 AP, balanced at 5-10 XP)

### 5. Unclear Trigger or Effect
**Bad:** "Warrior's Might: Sometimes hit harder"
**Why:** Vague trigger, vague benefit, unclear when to use
**Fix:** "On critical hit, deal +Might bonus damage again"

### 6. Overlapping with Existing Perk
**Bad:** Creating "Better Riposte" that does same thing for less XP
**Why:** Invalidates existing perk, breaks cost structure
**Fix:** Make variant with different trigger (counter on block vs parry) or requirement

### 7. Missing Prerequisites
**Bad:** Domain level 1 perk with "strike all enemies in reach"
**Why:** Too powerful for entry level, no progression chain
**Fix:** Require Two Birds perk (10 XP) and domain level 4, cost 15 XP

### 8. Wrong Domain Assignment
**Bad:** Defensive aura in Archery domain
**Why:** Archers = ranged precision, not party protection
**Fix:** Move to Universal or Shield domain

### 9. Ignoring Action Economy
**Bad:** Perk that takes 8 AP (more than most characters have)
**Why:** Unusable in practice, feels bad
**Fix:** Cost 5-6 AP max, or allow splitting across turns

### 10. Narrative Without Mechanics
**Bad:** "You are very brave"
**Why:** No mechanical effect, unclear benefit
**Fix:** "Gain advantage on fear saves" or "Adjacent allies can use your Will for fear checks"

### 11. Mechanics Without Flavor
**Bad:** "Attack Bonus 2"
**Why:** Boring, doesn't inspire character concepts
**Fix:** "Monkey King Strike - Vault over your staff to strike a line of foes"

### 12. Power Creep from Stacking
**Bad:** Multiple perks each giving +2 damage with no stacking restrictions
**Why:** Creates mandatory perk chains, huge damage scaling
**Fix:** Ensure perks don't stack or have different conditions (vs off-guard, vs prone, on crits)

### 13. Forgetting Bounded Accuracy
**Bad:** +5 to attack at domain level 2
**Why:** Skills and attributes max at 5, +5 breaks bounded accuracy
**Fix:** Keep bonuses +1 to +3, use advantage/critical effects for bigger swings

### 14. Paired Perks Without Balance
**Bad:** Leader gets +5 to everything, followers get nothing
**Why:** Nobody wants to be follower
**Fix:** Both perks provide unique benefits (Cult Leader = drive fervor, Inner Member = mind control resistance)

### 15. Instant-Win Conditions
**Bad:** "Critical hit kills any enemy"
**Why:** Removes challenge, breaks encounter design
**Fix:** "Critical hit applies Bleeding 3" or "Critical hit allows Intimidation check to demoralize"

---

## Design Exercises

### Exercise 1: Fill the Gap
**Identified Gap:** No perks increase critical range
**Your Task:** Design a perk that expands critical range (doubles on more results)
**Considerations:**
- Which domains should have access? (Precision = 1H, Arc?)
- Cost? (Critical range = very powerful)
- Restrictions? (Specific weapons? High requirements?)
- How much expansion? (18-20? 17-20 too strong?)

### Exercise 2: Domain Identity
**Task:** Design 3 perks for Two-Handed domain that reinforce its identity
**Identity:** Power, cleaving, knockback, overwhelming force
**Requirements:**
- One entry-level (5 XP)
- One mid-tier (10 XP)
- One ultimate (15 XP)
- All must feel "two-handed" not "one-handed with bigger weapon"

### Exercise 3: Progression Chain
**Task:** Create a 3-perk progression chain for a new concept
**Example Concept:** Grappling / wrestling
**Requirements:**
- Entry perk (5 XP): Basic grapple mechanic
- Mid perk (10 XP): Requires first, adds control or damage
- Ultimate perk (15 XP): Requires both, build-defining ability
- Assign to appropriate domain(s)

### Exercise 4: Balance Test
**Given Perk:** "Lightning Strike - 1H3, AG4+DX4, 8 XP - Strike twice with off-hand weapon for 3 AP total"
**Your Task:** Is this balanced? Why or why not?
**Compare to:**
- Double Strike (2 strikes for 4 AP, 5 XP, but second auto-misses if first defended)
- Normal strikes (2 strikes = 4-6 AP depending on weapons)
**Fix if needed**

### Exercise 5: Conditional Design
**Task:** Design two versions of a damage boost perk
**Version A:** Unconditional (always active)
**Version B:** Conditional (requires setup or situation)
**Requirements:**
- Same domain and level requirements
- Version B should be more powerful but require work
- Cost appropriately (conditional should cost less for same power or more power for same cost)

---

## Final Notes

### Remember: Player Fun First
- Perks should create interesting decisions, not math optimization
- Narrative flavor makes perks memorable (Monkey King Strike > "Pole Vault Attack")
- Synergies between perks create emergent build variety
- Not every perk needs to be optimal - some enable character concepts

### Playtest Constantly
- Theory doesn't equal practice
- Watch for perks that are never picked (too weak or unclear benefit)
- Watch for perks that are always picked (mandatory = design problem)
- Ask players what perks they enjoy using and why

### Iterate Based on Feedback
- If perk feels bad to use (too expensive AP, too restrictive conditions), adjust
- If perk feels mandatory (auto-pick at its level), add restrictions or cost
- If perk is confusing (players ask "when do I use this?"), clarify trigger and benefit
- If perk is forgotten (players have it but never use), make more impactful or easier to trigger

### Maintain Consistency
- Use this document as reference for XP costs, AP costs, and requirements
- When in doubt, find 2-3 similar perks and match their patterns
- Document new perks in this file for future reference
- Update categories if you create new design space

---

## Appendix: Complete Perk List by Domain

### Universal Combat (28 perks)

#### Tier 1 (Domain 1-2, 5 XP typical)
1. Riposte (AG3+MD3, 5 XP) - Counter on crit defense or enemy crit fail
2. Reactive Strike (AG2+MD2, 10 XP) - Strike retreating enemies
3. Dodging Step (AG2, 5 XP) - +1 dodge and make a step
4. Projectile Parry (MD1, 5 XP) - Parry ranged attacks
5. Watching your back (none, 5 XP) - Adjacent allies can't be flanked
6. The Leader (Lead1, 5 XP) - Share fear resistance with team

#### Tier 2 (Domain 2-3, 10 XP typical)
7. Dodge behind your back (AG4+Dodging Step+Stealth4, 10 XP) - Hidden + reposition
8. Dodge-Roll (AG3+Dodging Step, 10 XP) - +3 vs AOE, go prone
9. Two Birds (MG3+AG2, 10 XP) - Strike 2 adjacent targets
10. Parry This, Parry that (MD3+Projectile Parry, 10 XP) - Parry magic
11. That Type of a Person (Watching your back, 5 XP) - Rush to downed ally, take hits
12. The Cult Leader (GM+The Leader+Lead3+Manip3, 10 XP) - Drive followers into Fervor
13. The Aspiring Hero (Lead3+The Leader+GM, 10 XP instant) - Cheat death, lose 10 CP

#### Tier 3 (Domain 3-4, 15-20 XP)
14. All the Birds (MD4+MG4+Two Birds, 15 XP) - Strike all targets in reach
15. Repose This, Repose That (MG5+Parry This+WL3, 10 XP) - Reflect spells on crit parry
16. Reactive (AG3+PR3, 20 XP) - Gain second reaction

#### Special / Narrative
17. The Edgelord (1H2/2H2+GM, 10 XP) - +2 with edged weapons, duel mechanic
18. The Loner (none, 20 XP) - +2 AP solo, can't have allies
19. Plot Armor (GM, 50 XP) - Heroic destiny protection
20. Too Selfish (That Type of a Person, Free instant) - Bargain with fate
21. The Cult Inner Member (none, Free paired) - Mind control resistance, protect leader

### Staves & Spears - 13 perks

#### Starting (Free)
1. Walking Stick (SaS1 automatic) - Heavy weapons don't count to encumbrance

#### Tier 1 (2-5 XP)
2. Grip Switch (SaS1, 2 XP) - Free grip change between reach/long reach
3. Staff Acrobat (SaS1, 2 XP) - +reach to long jump, +2 balance
4. Calf Strike (SaS1, 5 XP) - Halve enemy speed on hit
5. Spear Brothers (SaS1, 3 XP) - +1 to all SaS checks when adjacent to partner
6. Pointy stick (SaS2, 5 XP) - Prepared strike when enemy enters reach

#### Tier 2 (5-10 XP)
7. Tripping Strike (SaS2+Calf Strike, 5 XP) - Prone on hit
8. Pushing Strike (SaS2+MG1, 3 XP) - Shove enemy outside reach
9. Quarter-staff training (SaS2, 10 XP) - +1 to all defenses
10. Spinning Staff (SaS3, 10 XP) - Strike each approaching enemy

#### Tier 3 (15 XP)
11. Spear Charge (SaS3+MG2, 15 XP) - Charge line, +1 damage per meter
12. Monkey King Strike (SaS3+AG3+Staff Acrobat, 15 XP) - Vault and strike line

### One-Handed - 9 perks

#### Starting (Free)
1. Ready Hand (1H1 automatic) - Draw weapon on initiative even when ambushed

#### Tier 1 (2-5 XP)
2. Long Knives (1H1, 2 XP) - Knives/daggers deal 1d6
3. Throwing Hand (1H1, 2 XP) - Add throwing capability, +3 range, use Dexterity
4. Twin Parry (1H1, 3 XP) - +1 parry when dual wielding
5. Double Strike (1H1, 5 XP) - Strike both weapons for -2 AP, risk of miss
6. Follow-Up Strike (1H2, 5 XP) - Consecutive strikes vs same target -1 AP

#### Tier 2 (5-10 XP)
7. Painful Parry (1H2+Twin Parry, 5 XP) - Free light weapon strike on crit parry
8. Piranha Strike (1H2, 10 XP) - +2 per die vs off-guard targets
9. Throwing Distraction (1H3+Throwing Hand, 10 XP) - Make target off-guard for ally

### Two-Handed - 1 perk (Incomplete)

#### Starting (Free)
1. Half-Sword Strike (2H1 automatic) - +2 to hit, -2 damage

**Note:** Domain flagged as outside PT4 scope, needs full implementation

### Shield - 11 perks

#### Starting (Free)
1. Shield Block (SH1 automatic) - Reduce damage by Shield Negation on failed block

#### Tier 1 (2-5 XP)
2. Multipurpose Shield (SH1, 3 XP) - Strike with boss without losing defense
3. Shield Rush (SH1, 2 XP) - Move twice and strike, double Might bonus
4. Shield Warden (SH1, 5 XP) - Use Shield Block for allies
5. Spell Guard (SH2, 5 XP, 1 Limit) - Block magical effects

#### Tier 2 (5-10 XP)
6. Behind the Shield strike (SH2, 3 XP) - Target -2 to parry/dodge
7. Perfect block (SH2, 5 XP) - Crit block makes target off-guard
8. Shield Guardian (SH2, 10 XP) - Block attacks for adjacent allies
9. The Guardian Aura (SH3+Spell Guard+Shield Warden, 10 XP, 2 Limit) - Grant advantage in 3 tiles

#### Tier 3 (15 XP)
10. The Wall (SH3+Shield Warden+Heavy Shield, 15 XP) - Allies hide behind you, use your defense

### Archery - 8 perks (Needs Remake)

#### Tier 1 (5 XP)
1. Zen Archer (Arc1, 5 XP) - Use Perception instead of Dexterity for bows
2. Defensive Archer (Arc1, 5 XP) - Parry with bow without break risk
3. Fast Archer (Arc1, 5 XP) - Aim as free action while moving (max Aim1)

#### Tier 2 (10 XP)
4. Tower (Arc2, 10 XP) - Free Aim1 if stationary last 2 turns
5. Don't Turn your back on me! (Arc2, 10 XP) - Count as flanking at range
6. Double Shot (Arc2, 10 XP, 4 AP) - Shoot 2 different targets, second at -2

#### Tier 3+ (Outside PT4 scope)
7. Overpowered draw (Arc3) - Cumulative +1 per aim action
8. Close quarters shooter (Arc3) - +Archery level damage at close range
9. Spell shot (Arc3) - Store single-target spell in arrow
10. Artillery (Arc4+Tower) - Range = Aim, double aim value

**Note:** Domain flagged for complete remake before PT5

---

**Total Implemented Perks: 70+** (28 Universal, 13 SaS, 9 1H, 1 2H, 11 Sh, 8 Arc)
**Domains Needing Work:** Two-Handed (incomplete), Archery (needs remake), Unarmed (not started)

---

*This document is a living reference. Update as new perks are designed and playtested. Last updated: [Current Date]*

[^1]: these 2 are the same, almost
	
