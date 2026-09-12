# Skill System Research Synthesis

*Synthesis of four research reports (this folder) for the ExceedV utility-skill rework. Scope: **utility skills only** — combat and magic competence live entirely in the Martial and Spellcraft domains (perks/spells), which are out of scope here. Compiled 2026-08-19.*

## The question and the answer

**Q:** How should the utility skill list be organized — profession synthesis nodes, trunk→branch trees, or parameterized (Type) families?

**A:** None of them, as *list shapes*. Across ~20 systems, **no successful skill-based game organizes its skill list.** The list stays flat and small; the jobs we were trying to build into its shape are each handled by a separate mechanism beside it:

| Job | Solved by the list? | Solved instead by |
| --- | --- | --- |
| Breadth | nobody | **Adjacency/defaults** (GURPS −2/−3/−4 web, 1,117 edges; CofD untrained penalties; PF2e untrained actions; Torchbearer Beginner's Luck) |
| Depth meaning | nobody | **Rank-gated verbs + per-level tasks** (PF2e sample DCs & skill feats; 4e skill powers; GURPS technique `limit`; TOR undertakings) |
| Identity / profession | nobody | **Packages** (GURPS templates; CoC occupations; 5e backgrounds; Blades playbooks; WFRP careers as price structure) |
| Active use | nobody | **Verb layers** (PF2e skill feats; 4e skill powers; SR specializations; ExceedV's planned Unlocks lists) |

Two field-measured facts anchor this (report 1): GURPS — the most list-heavy game ever published — has only **93 prereq edges among 718 skills**; and its specializations "work" only because each type is a separate purchase **cross-defaulting to siblings**. Shape is rare in the wild; adjacency is everywhere.

## Why each attempt felt wrong (diagnosis)

1. **Synthesis nodes** (Medicine ✦ = First Aid 2 + Biology 1). Identity-as-node is the one design no successful game uses — profession fantasy is always curation (a shopping list) or price structure, never a new skill. Also manufactures the abhorrence: the capstone's number eclipses its own ingredients (Performance 3 makes Singing 1 dead weight).
2. **Trunk trees**. A tree is a toll booth where there's no real knowledge dependency (most skills). It also fights ExceedV's bottom-up attribute feeding: trunks become either cheap attribute feedstock (abuse) or mandatory taxes (the mage scholarship chain). Prereqs are only honest where a genuine knowledge chain exists — Medicine←Biology, Forgery←Writing.
3. **(Type) families with one shared number.** GURPS canon *and* a trap, simultaneously: families work because types cross-default; without an adjacency layer, "shared levels?" has no good answer (shared = mastery transfer exploit; separate = why one row?). **Families are a naming convention riding on a defaults web — adopt them only together with defaults.**

## The ExceedV skill model (proposal)

Flat list + four thin layers, all already native to the architecture:

### 1. Flat list, ~40–60 utility skills, no shape

Groups remain flavor headers. No trunks, no synthesis nodes. A skill earns a row only if it has **its own body of knowledge to roll** — otherwise it's an activity (Surgery = Medicine 3 activity), a product (poisons = Alchemy output), or a package (Bard = recipe).

### 2. Adjacency (defaults) — the missing layer

Each skill names 1–3 adjacent skills. Using a skill you don't have via an adjacent one: **−2**. Unrelated attempt: raw attribute **−4** (formalizes today's "related skill −1 to −3"). One sentence each, printed on the sheet; the companion app can render the web. This replaces trees for breadth, replaces cross-type discounts for families, and covers the noble-who-just-dances.

### 2b. Specializations as tags, not rows

First type free at purchase (Performance (Singing)); extra types ~5 XP perks granting **scope**, not numbers. With adjacency in place, tags don't eclipse anything — the SR/CofD pattern (cheap tag, +niche benefit), and the weapon-training precedent.

### 3. Per-level tasks + Unlocks — depth meaning

Each skill publishes one line of "what each level lets you attempt" (PF2e sample tasks): *Swimming — L0: stay afloat; L1: calm water; L2: rough water, +speed; L3: rapids/floods; L4: …* Levels 4–5 additionally grant **economy payoffs** (GURPS 15/20 pattern): halved time, reduced cost, helper slots. This is where Surgery-as-activity and Brewing-at-Cooking-3 live (`Unlocks: L3 — Brewing`). Stat-stick skills die by construction.

### 4. Profession packages — identity outside the list

One block per fantasy, zero mechanics: fixed skills at levels + "choose one of" lists + 1–2 perks + trappings + reputation line. Surgeon, Bard, Idol, Spy, Hedge Witch… DF templates and CoC occupations are the models. The app renders them as one-click presets; packages are content, never rules. (WFRP-style career *progression* is a later-milestone option, parked.)

### What stays home

- **Bottom-up attribute feeding** — exists in none of the surveyed systems; the flat list is maximally coherent with it (feeding doesn't care about shape).
- **Martial/Spellcraft domains** — combat and magic competence stay out of the skill list entirely (the Fallout 4 lesson: two parallel competence layers without distinct jobs collapse into one).
- **Simple/Complex cost classes** — survive as pricing only; they never carried shape anyway.

## Decision checklist

| Decision | Recommendation |
| --- | --- |
| List shape | Flat, ~40–60 skills, flavor groups only |
| Breadth | Adjacency −2 named edges; unrelated −4 attribute default |
| (Type) families | Keep as naming; types = tags; first free, extras 5 XP perks |
| Extra-type benefit | Scope (can attempt at full skill), not a number bonus |
| Untrained use | Attribute −4, or adjacent skill −2 — always possible for utility skills |
| Levels 4–5 | Economy payoffs (time/cost/helpers), not just bigger rolls |
| Surgery-style specialties | Activities at skill level N (`Unlocks:`), not skills |
| Professions | Packages: curated shopping lists, zero mechanics |
| Prereqs | Only real knowledge chains (Medicine←Biology, Forgery←Writing); no generic trunks |
| Mage scholarship | Magical Theory prereqs stay thin (Math (basic) 1); packages, not chains, carry mage identity |
| Perk gating | Perks continue to gate on named skill levels (PF2e-validated pattern) |

## Report index

1. `1-gurps-skill-architecture.md` — primary-source parse of the local GCS library (.skl/.gct + Magic PDF): costs, 1,117 default edges, specializations, techniques, templates, high-skill economy.
2. `2-d20-lineage.md` — 3.5/PF1, 4e, 5e, PF2e from live SRDs: rank-gated verbs, sample tasks, skill powers, backgrounds.
3. `3-career-percentile-systems.md` — RQG, CoC, Pendragon, WFRP4e, Shadowrun, CofD from quick-start PDFs and system docs: packages, careers, tags, passions.
4. `4-indie-modern-crgp.md` — Blades (SRD-verified), Burning Wheel, Torchbearer, Fate, Cortex, TOR2e, Savage Worlds, Fallout/TES: verbs-first lists, Beginner's Luck, pyramid, the Fallout 4 merge warning.
