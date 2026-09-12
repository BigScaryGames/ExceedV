# GURPS skill architecture

*Research report for the ExceedV skill rework. Primary sources: local GCS library — `/home/r/GCS/Master Library/Basic Set/Basic Set Skills.skl` (718 entries, refs B167–B251), DF1 class `.gct` templates, Traveller templates, techniques `.skl` files, and GURPS Magic v4.1 PDF (Ritual Magic p. 200, Wildcard Magic p. 202, High Skill pp. 10–12). No Basic Set PDF on disk; B-page numbers come from `.skl` reference fields and Magic PDF citations.*

## 1. Cost table by difficulty (B170, verified against template point allocations)

Skill level = attribute + **relative level**. Points → relative level:

| Points | Easy | Average | Hard | Very Hard |
|---|---|---|---|---|
| 1/2 | attr / +1 | −1 / attr | −2 / −1 | −3 / −2 |
| 4/8 | +2 / +3 | +1 / +2 | attr / +1 | −1 / attr |
| 12/16 | +4 / +5 | +3 / +4 | +2 / +3 | +1 / +2 |
| 20/24 | +6 / +7 | +5 / +6 | +4 / +5 | +3 / +4 |

Verified: Thief template Lockpicking IQ/A 4 pts = IQ+1 ✓; Stealth DX/A 12 = DX+3 ✓; Filch DX/A 2 = DX ✓. Above +2 over attribute, **+4 points per level, flat, forever** — quadratic→linear cost curve. Distribution: ~198 IQ/A, 140 IQ/H, 86 DX/A, 64 DX/E; only 28 VH entries.

## 2. Defaults = breadth web without purchases

Every untrained skill has a **default**: attribute−4/−5/−6 (dominant: IQ−5 ×202 entries, IQ−6 ×118, DX−5 ×57) or **another skill at a penalty**. Measured: **1,117 skill→skill edges** among 718 skills; 468 skills default from at least one other skill. Penalty tiers: same-family specializations at **−2** (97 edges), −3 (74), −4 (253). One purchase radiates sideways competence for 0 points. Magic extends defaults to spells: unknown spell defaults to any known spell in-college at −4 + prerequisite count; casting at default costs 2× energy and 2× time (Magic p. 202).

## 3. Specializations (parenthetical types)

437 of 718 entries carry a `specialization` field over **304 base names**; 53 families have >1 type — Mechanic (45), Engineer (19), Survival (19), Area Knowledge (18), Piloting (17). Two patterns: (a) **closed list** (Survival types, Artist's 12 types); (b) **open parameterized** — `Professional Skill (type)` is literally a template skill (B215, IQ/A, default IQ−5) for jobs with no dedicated skill. **Levels are NOT shared between types**: `Artist (Body Art)` and `Artist (Calligraphy)` are separate purchases — but each defaults to siblings at −2…−6, so breadth after one specialization is ~2–4 points per new type. The family is a *naming convention riding on the defaults web*.

## 4. Techniques vs. skills

Basic Set ships **70 techniques** (B230–B233). Structurally distinct in the data: a **singular `default`** (not a list), no attribute pairing, and a **`limit` field** — max levels above the default (Arm Lock limit 4; Back Kick limit 0 = buy off the penalty only, never exceed parent skill). A technique can never exceed its parent skill; it prices a *specific maneuver's penalty removal or trade-off*, never general competence. Ritual Magic reuses this: every spell = Hard technique defaulting to college skill at −(prerequisite count).

## 5. Templates as professions

DF1 has 13 class `.gct` files (Barbarian…Wizard). Structure: fixed attribute boosts + advantages + a **three-tier skill tree: Primary / Secondary / Background**, where Secondary/Background contain **choice-lists** (`selection_type`): Thief: 8 fixed primaries (Stealth 12 pts = DX+3), then "One ranged" (Bow/Crossbow/Sling/Throwing), "One defense", "One melee", "7 points among 17 skills". Traveller Doctor: Diagnosis/Physician/Electronics Op 4 each, "any two of" Hypnotism/Pharmacy/Poisons/Psychology/Veterinary, 3 floating points. **Profession = curated point-allocation guide with constrained choices, not a mechanic.**

## 6. What high skill buys

3d6 bell curve makes 14–16 the practical ceiling (≈90%+ success). Beyond the roll (Magic PDF, verified): **skill 15–19** → −1 energy cost, minimal ritual; **skill 20–24** → −2 cost, **casting time halved**, no ritual; reductions apply to maintenance too (can reach 0 → indefinite spells); levels past 20 give no further cost reduction. Standard B rules (B346–348): Time Spent doubling = +1; retries after failure disallowed without a new approach; Complementary skill grants +1/+2 (B175); Rule of 16 caps skill vs. active defenses; Wildcard skills (B175) = 3×-cost uber-skills.

## Precedent check for prereq trees

93 named prereq edges in the whole Basic Set — real dependency trees are *rare*: Medicine/First Aid chains and spell colleges, almost nothing else. Shape is nearly nonexistent in the wild; adjacency (defaults) is everywhere.

---

## 5 structural ideas worth stealing for ExceedV

1. **Defaults as a free breadth web.** Define every untrained skill as "attribute−N or [specific skill]−N." Solves breadth-vs-depth pricing with zero list reorganization.
2. **Parameterized families + Professional Skill (Type).** `Crafting (Type)` is canon GURPS — provided each type is its own purchase cross-defaulting to siblings.
3. **Profession = template = curated point guide with choice-lists.** Ship packages: fixed core skills + "choose one of" lists. The profession is a shopping list, not a mechanic.
4. **Techniques with a `limit` field** — maneuver-specific, capped, priced off the parent skill; never general competence.
5. **Tiered high-skill rewards** (15/20 thresholds): past skill level X, unlock *economy* changes — reduced cost, halved time, ritual-free use. Gives a 5-level skill a reason to be maxed beyond the roll.

## 3 traps to avoid

1. **280+ skill granularity.** 304 base names / 718 entries only works because GCS software manages it. DFRPG cut to ~151 names. Cap at ~40–60.
2. **IQ/A point-sink asymmetry:** 198 IQ/A skills vs 26 VH — the "right answer" was always many cheap mental skills at 1 pt. Cheap breadth needs caps or rising marginal costs.
3. **Levels shared-or-not ambiguity.** GURPS's separate-levels-per-type + cross-defaults is coherent but invisible to new players. Whatever you pick, state it in one sentence.
