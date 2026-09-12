# Utility Skill System — AFG Implementation

*Functional draft for the 33 skills in [[5. Skills]] only. Combat and magic remain in the Martial/Spellcraft domains. Built from the research synthesis (`0-synthesis.md`): A (leveled skills, classes, Unlocks, untrained penalties) + F (adjacency web) + G (specialty tags). Experimental files (Skill Trees/Skill Groups/Rework Plan) are shelved; only transplants that survive review are here.*

## 1. Framework

### Classes and costs

| Class | Cost per level | Total to L5 | Untrained penalty | Entry skills |
| --- | --- | --- | --- | --- |
| **Simple** | 1 / 2 / 4 / 6 / 8 | 21 | attribute −3 | household/childhood skills |
| **Normal** | 2 / 4 / 6 / 8 / 10 | 30 | attribute −4 | professional skills |
| **Complex** | 4 / 6 / 8 / 10 / 12 | 40 | attribute −5 | graduate/rare skills |

- Untrained use is always possible for utility skills: roll attribute only at the class penalty.
- **Adjacent skill:** if you own a skill that names another as adjacent, you may use the unowned one at **(adjacent skill −2)**. Adjacency is symmetric, **never chains** (A via B via C is forbidden), and each skill holds max 2–3 edges — the web stays sparse and legible.
- XP feeds attributes 1:1 as always, including tags.

### The verb-split rule (skills vs perks)

- **Skill Unlocks** = what any practitioner at that level can do (universal capability).
- **Perks** = exceptional techniques a practitioner *may choose* to learn (never duplicated by an Unlock). Existing perk gates (level 1–3 in 5.1) are unchanged.

### Specialty tags (G)

- **First tag 2 XP, second tag 4 XP**, max 2 per skill, +1 when the named niche applies, feeds attributes 1:1 (same pair as parent skill). The niche must be narrower than any existing skill and can't be "always-on" (GM approval).
- Tags are scope + a small edge, never a second progression track.
- **Standard depth reward (proposed):** reaching **L4 in any skill grants one free specialty tag** for it — a uniform payoff for the expensive levels (GURPS high-skill economy pattern). If both tag slots are full, no refund.

### Unlock ladder format (per skill)

`L1..L5: one line each` — capability tiers first ("what you can attempt"), concrete mechanic hooks where they exist. Where canon already gates an activity ([[Treatment Methods]], [[Circumvent Security Device]], Forage, march checks), the ladder cites it instead of inventing. **Wording convention:** *Gives* = a capability you lack by default (Swimming gives swim speed); *Increases* = enhances one everyone has (Lifting increases carry capacity). L1–L3 must ship filled; #TODO allowed only at L4–L5 (and blocks that skill's playtest sign-off).

---

## 2. Class & adjacency table (32 skills — after Thievery merge)

| Skill | Class | Adjacent to | Notes |
| --- | --- | --- | --- |
| Dancing | S | Acrobatics | |
| Negotiating | N | Fast-talk | |
| Manipulation | C | Acting | |
| Leadership | N | Intimidation | |
| Fast-talk | S | Negotiating | |
| Singing | S | — | |
| Gossip | S | Streetwise | |
| Intimidation | N | Leadership | |
| Acting | N | Manipulation | |
| Running | S | — | Speed formula already uses Running ÷ 2 |
| Climbing | S | — | Might-driven; stands alone |
| Swimming | S | — | |
| Jumping | S | Acrobatics | |
| Acrobatics | N | Dancing, Jumping | Climbing edge cut (density); Might-driven Climbing stands alone |
| Lifting | S | Breaking | Capacity = (5+EN+MI)² |
| Breaking | N | Lifting | canon: Breaking opens average locks/safes |
| Smithing | N | Engineering | |
| Woodworking | N | Engineering | |
| Textilework | S | — | |
| Engineering | C | Smithing, Woodworking | |
| Biology | N | Medicine | |
| Chemistry | N | Medicine | |
| Medicine | C | Biology, Chemistry | |
| Stealth | N | Thievery | |
| Thievery | N | Stealth | **Merge:** Lockpicking + Sleight of Hand. Lock Consul perk gate re-keys Lockpicking 1 → Thievery 1 |
| Survival | N | Tracking, Streetwise | |
| Tracking | N | Survival | |
| Navigation | S | — | owns route-difficulty reduction |
| Magical Theory | N | — | Normal *deliberately*: L1 = 2 XP keeps mage entry near-free; L2 = 6 XP gates Tier 2 spells |
| History | S | Theology | |
| Theology | N | History | |
| Streetwise | S | Gossip, Survival | |

*(Edge count check: Acrobatics 2, Engineering 2, Medicine 2, SoH 2, Survival 2, Streetwise 2, Stealth 1, Lockpicking 1 — within limit.)*

---

## 3. Unlock ladders

### Social

**Dancing (S)** AG/CH
- L1: formal and social dances
- L2: skilled performances; earn income performing ([[Earning Income]])
- L3: teach students; choreograph group performances
- L4: signature style — free specialty tag
- L5: performances that anchor events; renown follows the dance

**Negotiating (N)** CH/WT
- L1: everyday deals and haggling ([[Trading Rules]] baseline)
- L2: high-stakes deals; shift bargaining range one step in your favor
- L3: draft binding agreements both sides honor
- L4: close-the-room instinct — free specialty tag
- L5: treaties and truces; your word moves institutions

**Manipulation (C)** CH/WL
- L1: plant suggestions that surface later
- L2: run a multi-step con on one target
- L3: groom a long-term asset (witting or unwitting)
- L4: puppeteer — free specialty tag
- L5: installed beliefs do your work for you (GM-negotiated scale)

**Leadership (N)** CH/WL
- L1: coordinate a small team; clear orders under stress
- L2: rally the demoralized — remove [[Shaken]] from allies who can see/hear you (1/scene each)
- L3: command hirelings and retainers ([[Rank Benefits]])
- L4: commander's eye — free specialty tag
- L5: people follow your banner before they've met you

**Fast-talk (S)** CH/AG
- L1: stall, misdirect, quick lies
- L2: [[Fast-Talk]] social action without setup
- L3: improvised cover stories on the spot
- L4: truth-sounding fabrications — detect attempts against your lies at −2
- L5: talk past gatekeepers of any station

**Singing (S)** EN/CH
- L1: carry a tune; communal songs
- L2: perform for income
- L3: teach; train a chorus
- L4: moving performances — free specialty tag
- L5: a voice people travel to hear

**Gossip (S)** CH/PR
- L1: local small talk; who's who
- L2: find who knows what in a settlement (a shift of asking)
- L3: trace a rumor to its source
- L4: web of ears — free specialty tag
- L5: information broker; secrets find *you*

**Intimidation (N)** CH/MI
- L1: threats, posturing, menacing presence
- L2: [[Demoralize]] action (canon: 2 AP, vs Endure)
- L3: wring compliance from captives via fear (interrogations)
- L4: fearsome mien — free specialty tag
- L5: your reputation walks into the room first; weak foes fold without a roll

**Acting (N)** CH/WL
- L1: play a role; sustain under casual notice
- L2: hold character through conversation
- L3: pass as a specific person of similar build
- L4: method — free specialty tag
- L5: the mask holds under interrogation and old friends

### Athletic

**Running (S)** AG/EN — Speed already scales (Running ÷ 2)
- L1: trained sprints and pacing
- L2: make fatigue checks for marches with Running (canon: Endure or Running)
- L3: set the pace — party travels at your rhythm (group travel hooks)
- L4: marathoner — free specialty tag; +1 March before checks #TODO
- L5: courier endurance; legendary distances

**Climbing (S)** MI/AG
- L1: ladders, rigging, easy slopes
- L2: rough walls with handholds; climb at quarter Speed
- L3: sheer surfaces; climb at half Speed
- L4: cliffborn — free specialty tag; overhangs and chimneys
- L5: scale near-surface walls others call unclimbable

**Swimming (S)** EN/MI
- L1: stay afloat; calm water at half Speed
- L2: rough water; full swim speed
- L3: rapids and floods; underwater work
- L4: long hauls — free specialty tag; rescue others without penalty
- L5: water is just another road

**Jumping (S)** MI/AG
- L1: gaps at a run; low obstacles
- L2: vertical leaps; precision takeoffs
- L3: precise landings on small/targeted footholds
- L4: vaulter — free specialty tag; obstacles don't break stride #TODO numbers
- L5: leaps that become local legend

**Acrobatics (N)** AG/DX
- L1: rolls, recoveries, basic balance
- L2: fall mitigation — treat a fall as one distance band shorter #TODO
- L3: tightrope, beams, unstable footing
- L4: contortion — free specialty tag; squeeze through improbable gaps
- L5: run across ropes, mastheads, moving surfaces

**Lifting (S)** MI/EN
- L1: heavy labor; steady carrying
- L2: trained feats — treat Capacity as ×1.25 for carry #TODO
- L3: overhead presses, moving furniture solo
- L4: strongman — free specialty tag
- L5: feats of strength stories are told about

**Breaking (N)** MI/WT
- L1: doors, furniture, crates
- L2: targeted demolition — know the weak point (structural reading)
- L3: breach walls and strong containers ([[Circumvent Security Device]] lists Breaking)
- L4: controlled demolition — free specialty tag; collateral where you want it
- L5: nothing built withstands you for long

### Crafts

**Smithing (N)** MI/DX
- L1: repairs, nails, simple tools
- L2: serviceable weapons and armor
- L3: quality goods (masterwork hook — items milestone)
- L4: alloys and special materials — free specialty tag
- L5: work that carries your mark across borders

**Woodworking (N)** DX/WT
- L1: repairs, simple furniture, tool handles
- L2: bows, doors, fitted joints
- L3: construction — beams, bridges, structures
- L4: master joiner — free specialty tag; siege-scale timberwork
- L5: wooden wonders; your frames outlive their builders

**Textilework (S)** DX/PR
- L1: mend, sew, patch gear
- L2: rope, leather goods, pack repairs
- L3: tailored clothing, armor padding, quality goods
- L4: master craft — free specialty tag
- L5: cloth and leather work recognized by name

**Engineering (C)** WT/PR
- L1: mechanisms, pulleys, simple machines
- L2: structural design; supervise construction
- L3: complex interlocking mechanisms (locks, clocks, lifts)
- L4: visionary — free specialty tag; project-scale works
- L5: machines that make people reconsider what's possible

### Sciences

**Biology (N)** WT/PR
- L1: identify common flora and fauna
- L2: anatomy, behavior, warning signs
- L3: remedies, poisons, and venoms identification (Forage uses Biology for herbs — canon)
- L4: field naturalist — free specialty tag
- L5: read an ecosystem like a book

**Chemistry (N)** WT/DX
- L1: properties, tests, safe handling
- L2: acids, compounds, useful brews
- L3: explosives and incendiaries
- L4: synthesis — free specialty tag; rare compounds
- L5: novel materials; alchemists ask *your* advice

**Medicine (C)** WT/DX — ladder is canon ([[Treatment Methods]])
- L1: [[First Aid]] in combat (4 AP trained)
- L2: [[Treat Wounds]] (requires training + tools)
- L3: [[Surgery]] (requires skill 3+ and surgical tools — canon gate)
- L4: specialist — free specialty tag (field surgery, poison care…)
- L5: pull patients back from Severity 3 consequences others write off #TODO

### Stealth

**Stealth (N)** AG/PR
- L1: hide and move quietly when unobserved
- L2: stay silent while moving at half Speed
- L3: shadow a target through crowds
- L4: minimal cover suffices — free specialty tag
- L5: people swear the room was empty

**Thievery (N)** DX/PR — *merge of Lockpicking + Sleight of Hand; both bodies live in one ladder*
- L1: palming, retrieving, and planting small objects unseen; simple padlocks
- L2: pick pockets in a crowd; average locks and basic traps (canon example: 1 success/1 Minuta)
- L3: safe-cracking — high-end safes (canon: 3 successes); alarm mechanisms; rigged games
- L4: mechanism intuition — free specialty tag; picks unfamiliar lock families without penalty
- L5: "locked" is a rumor; objects change owners in plain sight

### Wilderness

**Survival (N)** PR/EN
- L1: camp, fire, shelter, knots, gathering wood, reading terrain
- L2: [[Forage]] while marching without the +2 DC penalty (canon activity)
- L3: reduce route difficulty one step ([[Time and Travel]] hook; stacks per its rules)
- L4: hardier — free specialty tag; hostile biomes treated one step milder #TODO
- L5: the wild provides; you belong anywhere green

**Tracking (N)** PR/WT
- L1: follow clear trails at half Speed
- L2: read sign — age, count, burden, haste
- L3: hard surfaces and weathered trails
- L4: predictor — free specialty tag; deduce quarry's intent and destination
- L5: named beasts are found when you're hired

**Navigation (S)** PR/WT
- L1: maps, landmarks, asking the way
- L2: celestial and terrain wayfinding; reduce route difficulty one step
- L3: trackless wastes; chart new routes
- L4: pathfinder — free specialty tag; party navigates by you in zero visibility
- L5: you have never been lost

### Knowledge

**Magical Theory (N)** WT/WL — mage entry stays near-free (L1 = 2 XP)
- L1: magical lore; recognize effects and schools (spell learning gate: skill ≥ tier — canon)
- L2: identify spells as they're cast ([[Spell Identification]] perk adds the defensive use)
- L3: contest wards and glyph traps ([[Circumvent Security Device]] lists Magical Theory)
- L4: theorist — free specialty tag; aid spell research #TODO
- L5: magic is a solved subject, as far as you're concerned

**History (S)** WT/WL
- L1: broad events, famous figures
- L2: regional detail, legends, lineages
- L3: obscure and contested knowledge
- L4: connective tissue — free specialty tag; [[Deduce]] with History on old matters
- L5: a living archive; scholars cite you

**Theology (N)** WL/CH
- L1: rites, pantheon, observances
- L2: conduct ceremonies (weddings, blessings, funerals) with standing
- L3: heresies, obscure cults, apocrypha
- L4: disputant — free specialty tag; sway congregations
- L5: your interpretations become tradition

**Streetwise (S)** CH/PR
- L1: underworld slang; who runs which turf
- L2: find fences, fixers, and buyers (Trading hook; city [[Forage]] — canon lists Streetwise)
- L3: read territory — danger, debts, and rivalries before entering
- L4: known quantity — free specialty tag; doors open in two cities #TODO
- L5: kings of gutter and guild both take your calls

---

## 4. Three-tier cost investigation

**Verdict: yes, three tiers — the middle tier earns its keep.** Distribution after the merge: 13 Simple, 16 Normal, 3 Complex. Without a middle class, Navigation, Tracking, Stealth, or Medicine-type skills must collapse into "household" or "graduate," and neither fits — professional skills are the bulk of the list and need a professional price point between 21 and 40 XP totals.

**Perk-gate sanity check** (5.1 gates: skill level 1–3 for 5/10/15 XP perks):

| Gate | Old cost (flat 2/4/6) | New cost | Perk price behind it | OK? |
| --- | --- | --- | --- | --- |
| Medicine 1 (Herbalist's Eye) | 2 | 4 (C) | 5 | fine |
| Medicine 3 (Life and Death) | 12 | 18 (C) | 15 | steep but right for a capstone perk |
| Magical Theory 2 (Glyphwright) | 6 | 6 (N) | 10 | fine; mage entry preserved |
| Stealth 1 (Silent Steps) | 2 | 2 (N) | 5 | fine |
| Stealth 3 (Shadow Master) | 12 | 12 (N) | 15 | fine |
| Theology 3 (Consult the Scripture) | 12 | 12 (N) | 15 | fine |

The scheme compresses cheap entries (Simple L1 = 1) and makes Complex mastery genuinely expensive — the spread the research recommended (escalating depth, cheap breadth). Untrained penalties −3/−4/−5 give the difficulty axis mechanical teeth without a second cost table. Note: **Magical Theory is Normal class** (2/4/6/8/10) — advocate flagged that pricing it Complex would double the mage entry cost and quietly reverse the "thin mage entry" decision; Normal keeps L1 = 2 XP.

## 5. Merge verdicts (transplants from the shelved files — advocate-passed)

- **Lockpicking + Sleight of Hand → Thievery: ADOPTED** (advocate verdict: one manual-dexterity criminal body, PF2e Thievery precedent; both sub-bodies interleaved in one ladder; Lock Consul gate re-keys Lockpicking 1 → Thievery 1). 32 skills after merge.
- **Crafting (Type) replacing the 3 crafts: REJECTED** (confirmed) — three attribute pairs can't be one skill; tags cover niches (Bladesmith, Bowyer).
- **Surgery/Brewing-style specialties as Unlocks: ADOPTED** — Medicine ladder mirrors canon Treatment Methods. **Re-key required:** Surgeon's Precision (Medicine 2) currently *grants* surgery and would undercut the Medicine 3 Unlock — becomes an enhancement (+2 / cancel a complication); Master Brewer (Medicine 2) collides with any brewing Unlock — becomes enhancement or moves to an Alchemy-adjacent home. Safe-cracking is clean (Lock Consul is tools, not safes).
- **Performance/synthesis nodes: NOT TRANSPLANTED** (confirmed clean — no candidate smuggles them back).
- **Level-gated activities format**: every canon activity that already assumes skill (First Aid, Treat Wounds, Surgery, Circumvent tiers, Forage, march checks, ward-bypass) now has an explicit level home in a ladder.

Advocate's full per-edge audit (C1–C9): all 17 adjacency edges pass except Climbing↔Acrobatics (cut — density; Acrobatics held at 2 edges). No-chaining rule added to adjacency. Tag pricing escalates (2 XP → 4 XP). L1–L3 ladders must ship filled, #TODO only at L4–L5.

## 6. What deliberately did NOT change

- The 33 skills, their names, and attribute pairs (one candidate merge deferred).
- Attribute feeding 1:1; tags feed too.
- Perk system, perk prices, and perk level-gates (5.1 untouched — only skill entry prices shift under them).
- Actions doc (Demoralize, Fast-Talk, First Aid stay as-is; ladders reference them).
- Combat and magic: no skill touches AP, damage, or Limit.

## 7. Open questions (yours to rule on)

1. **Universal L4 = free tag** — adopt as a standard depth reward, or per-skill only?
2. **Numeric #TODOs**: fall-mitigation band (Acrobatics L2), carry ×1.25 (Lifting L2), +1 March (Running L4), hostile-biome step (Survival L4), Singing/Leadership morale-adjacent effects — all need your numbers.
3. **Thievery merge** — ADOPTED by advocate; your call still overrides (reverting is one table row + two ladders restored).
4. **Class calls I'm least sure of**: Intimidation (N vs S), Acrobatics (N vs S), Breaking (N), Theology (N).
5. **Street Wisdom** references in 5.1 should rename to Streetwise when you re-key (typo-level fix, left for your edit pass).
