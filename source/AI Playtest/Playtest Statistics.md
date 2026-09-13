**Session:** The Toll at Greywater Mill (one-shot, three trained adventurers, 50+50 XP each)
**Method:** Every check, attack, defense, initiative and damage roll was produced by a Python RNG script (`random.randint`) at the moment of the roll and transcribed verbatim into the session log. No numbers were chosen by the narrator. Discarded rolls (target died first, action never taken) are listed, not silently dropped.

---

## 1. Roll ledger by category

### Skill checks (out-of-combat) — 15 rolls, 10 success / 5 fail (67%)

| Scene | Roller | Check | Dice | Result |
|-------|--------|-------|------|--------|
| 1 | Yara | Gossip 2+CH 1 vs 12 | 10+3+3 = 16 | ✓ |
| 1 | Cobb | Streetwise 2+PR 1 vs 12 | 1+8+3 = 12 | ✓ (exactly) |
| 1 | Bram | Negotiating 2+WT 1 vs 13 | 3+10+3 = 16 | ✓ |
| 1 | Cobb | Gossip 2+PR 1 vs 12 | 8+8+3 = 19 | ✓ **crit (doubles)** |
| 1 | Bram | Intimidation 2+ST 2 vs 12 | 2+7+4 = 13 | ✓ |
| 2 | Cobb | Tracking 2+PR 1 vs 12 | 5+4+3 = 12 | ✓ (exactly) |
| 2 | Cobb | Observation 1+PR 1 vs 14 | 4+5+2 = 11 | ✗ |
| 2 | Yara | Observation 2+PR 0 vs 14 | 8+3+2 = 13 | ✗ (by 1) |
| 3 | Cobb | Stealth 3+AG 2 vs 12 | 5+9+5 = 19 | ✓ |
| 3 | Bram | Search 2+WT 1 vs 12 | 3+2+3 = 8 | ✗ |
| 3 | Cobb | Search 1+WT 0 vs 13 | 6+7+0 = 13 | ✓ (exactly) |
| 3 | Bram | Observation 1+PR 0 vs 12 | 1+8+1 = 10 | ✗ |
| 4 | Yara | Ruse: Negotiating 3+CH 1 vs 12 | 6+1+4 = 11 | ✗ (by 1) |

*(Plus two casting checks under "spells" below. Pattern: four successes landed on exactly the DC — the "success = meet the DC" rule carried a lot of weight.)*

### Initiative — 5 rolls

| Roller | Dice | Total |
|--------|------|-------|
| Bram (wolves) | 4+2 | 6 |
| Yara (wolves) | 2+9 | 11 |
| Cobb (wolves) | 9+7+1 | 17 |
| Wolf pack | 4+2+1 | 7 |
| Party coordinated ambush (leader Cobb) | 8+7+1 | 16 |

### Attacks — 17 rolls, 13 hit / 4 miss (76%)

| Roller | Attacks | Hits | Notes |
|--------|---------|------|-------|
| Cobb (shortbow/dagger) | 8 | 5 (63%) | **2 critical failures** (both 2+2 doubles vs armored Pike) |
| Bram (javelin) | 5 | 4 (80%) | +5 attack vs DC 10–14 |
| Yara (Elemental Strike) | 4 | 4 (100%) | **2 critical casts** — 24 and 23 vs static Dodge 12 (beat-by-10 extended crit) |

### PC defenses — 13 rolls, 8 success / 5 fail (62%)

| Defender | Rolls | Successes | Notes |
|----------|-------|-----------|-------|
| Bram (Deflect +5) | 6 | 5 (83%) | 2 **critical defenses** (4+4, 8+8) |
| Yara (Dodge +0) | 3 | 1 (33%) | took both hits that landed on her |
| Cobb (Dodge +4) | 1 | 1 | |
| Resolve vs Bellow (DC 14) | 3 | 1 | Bram 5 ✗, Yara 13 ✗, Cobb 15 ✓ |

### GM-side NPC attacks — 5 rolls, 1 hit / 4 miss (20%)

Fenn 18 (hit Bram) · Pike 6, 9, 16, 10 (all missed; the 16 tied Bram's 16 — defender wins ties). Bowman 13 (missed Cobb's 19). Wolves and toll-boys were mooks (static DC, no roll).

### Casting checks — 6 rolls, 6 success (100%), 3 critical

| Spell | Roll | Outcome |
|-------|------|---------|
| Ghost Sound (DC 8) | 20 | ✓ **crit** (beat by 12 → duration up) |
| Detect Magic (DC 8) | 10 | ✓ |
| Minor Healing (DC 10) | 22 | ✓ **crit** (beat by 12 → healing dice doubled, 12 HP) |
| Elemental Strike ×4 | 18 / 24 / 23 / 15 | all hit; 24 and 23 crit |

**Strain accumulated all session: 0.** Lowest margin on any cast was +2. The risk economy never engaged.

### Discarded rolls (rolled but never consumed — kept for the record)

- Bram javelin 2+3+5 = 10 (wolves died before his initiative).
- Toll-boy attack 9+1−1 = 9 vs Yara (boy's partner died first; the surviving boy's swing, 2+6−1 = 7, was the consumed hit).
- Fenn's round-3 attack 4+9+1 = 14 (killed by Yara at initiative 16 before acting).
- Yara's paired defense vs Fenn (2+9−1 = 10).
- Cobb's hostage shot 8+4+2 = 14 vs Deflect 15 — never fired; disclosed at the table as a would-be miss.

## 2. Dice fairness audit (122 individual d10s)

| Metric | Observed | Fair expectation |
|--------|----------|------------------|
| Face mean | 5.80 | 5.50 |
| Most common face | 9 (×18) | ~12.2 each |
| Least common face | 1 (×7) | ~12.2 each |
| Pair-sum mean | 11.61 | 11.0 |
| Doubles rate | 8.2% (5/61) | 10% |

Mild high bias, within normal variance for this sample size. The *narrative* impression ("the dice loved the party") is confirmed by the math — attacks outperformed defenses all session — but no single face dominated.

## 3. Damage ledger

**Dealt by the party — 71 total**

| Source | Dice | Damage | Targets |
|--------|------|--------|---------|
| Cobb (d8 ×4) | 3, 1, 6, 4 | 14 | wolves ×2, bowman |
| Bram (d6+2 ×3) | 6, 7, 5 | 18 | Harl, Pike ×2 |
| Yara — normal 2d6 (×3 applications) | 5 / 10 / 4 | 19 | wolf, Harl, Pike |
| Yara — **crit** 4d6 (×2) | 1+1+3+2 = 7 · 3+1+3+6 = 13 | 20 | Fenn ×2 (both survived one crit, died to the second/third hit) |

- Overkill vs mooks: 9 damage dealt to 3 wolf HP.
- Crit vs normal kettle damage: crit avg 10.0 vs normal avg 6.3 — the doubling mattered less than the theater (the 4d6 crit that rolled 1+1+3+2 is now table legend).
- Yara's 12 damage d6s averaged 3.08 (fair 3.5) — her "hot streak" was entirely the +5 bonus and static DCs, not the dice.

**Taken by the party — 13 total**

| Who | Damage | Source | Where it landed |
|-----|--------|--------|-----------------|
| Yara | 2 | wolf bite | Stamina 4→2 |
| Yara | 4 | toll-boy stick | Stamina 2→0, Health 10→8 |
| Bram | 7 | Fenn shortsword | Stamina 6→0, Health 14→13 |
| Cobb | 0 | — | untouched all session |

**Healing — 12** (one critical Minor Healing; 5 points lost to pool overflow — Health capped, Stamina capped, remainder vanished).

## 4. Action economy observations

- **Nobody ever exhausted 7 AP.** Every round, every player left 1–3 AP unspent — turns were limited by *targets and positioning*, not points. The domain-locked AP (2 each) got used for strikes and casts, exactly as designed.
- **Wasted turns:** Bram lost a full round to mook evaporation (wolves); Yara deliberately held a cast (threat assessment) — the only "waste" that felt intentional.
- **Reactions used:** Shield Block (never triggered — Bram's Deflect only failed once, vs the hit that cost 7), Shield Warden (never — allies in other skirmishes), Retreating Shot (NPC, never — bowman fled instead). The reaction economy existed mostly as *deterrence*.

## 5. Encounter budget vs outcome

| Fight | Threat vs party weight 6 | Party damage taken | Notes |
|-------|--------------------------|--------------------|-------|
| Wolf pack (3 mooks, T0) | 3 vs 6 — speed bump | 2 | over in one round; tank wasted turn |
| Mill yard wave 1 (2 bandits + bowman, T1) | 3 vs 6, ambushed | 7 | ambush stun deleted enemy turn one |
| Mill yard wave 2 (Pike T1 + 2 mooks) | 2-ish in wave, ~7 total | 4 | Yara swarmed — the one scary moment |
| Rook (T2, social off-ramp) | — | 0 | ended by negotiation + Intimidation |

Total party damage taken across the whole adventure: **13 of 47 available HP** (two fights ended by morale/social mechanics). For "trained adventurer" tier this was a fair-but-forgiving difficulty curve — ambush execution and spell crit rate did most of the work.

## 6. XP economy

| Character | Battle spent | Life spent | Banked | Attribute outcome |
|-----------|--------------|------------|--------|-------------------|
| Bram | 49/50 | 50/50 | 1 | ST +2, EN/WL/WT/AG +1; PR 0 |
| Yara | 49/50 | 50/50 | 1 | WL +2, WT +1 (28 pool), CH +1 (29 pool) |
| Cobb | 50/50 | 54/50 (+4 flaw) | 0 | AG +2, DX +1 (29 pool), PR +1 |

- Near-miss thresholds (pool within 3 of 10/30): **4 instances** across three characters.
- Session award: 10 Battle XP + 6 Life XP each — roughly 20% of starting Battle budget for one adventure; advancement pace feels generous at this tier (needs a longer arc to confirm).
- Yara's magic budget bought 23 spells at Magery 2 — spell-list breadth is extremely cheap (1–3 XP) relative to its table cost in lookup time.
