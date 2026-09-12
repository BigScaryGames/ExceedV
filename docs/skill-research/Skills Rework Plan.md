# Skills Rework Plan

Working draft — difficulty classes, tiered costs, hierarchy prereqs. If adopted, replaces the flat 2/4/6/8/10 in [[3. Character Creation and Point buy Costs]] and re-keys gates across perks/spells.

## The Scheme

| Class   | Cost per level    | Min start | Raw total | Entry price (chain incl.)               |
| ------- | ----------------- | --------- | --------- | --------------------------------------- |
| Simple  | 1 / 2 / 4 / 6 / 8 | L1        | 21        | 1                                       |
| Normal  | 4 / 6 / 8 / 10    | L2        | 28        | 7 (requires a named Simple @ 2)         |
| Complex | 6 / 8 / 10        | L3        | 24        | per chain (requires named Normal @ 2–3) |

- First purchase of a Normal/Complex skill puts you **at the minimum level** (buy Medicine → you are Medicine 3).
- Prereqs are **named per skill** (GURPS-style), not class-generic: Medicine names First Aid 2 + Biology 2.
- The pyramid carries over: levels bought as prereqs are yours; nothing is wasted.

## The Medicine Chain (worked example)

| Step | Skill | Class | Level | XP | Running total |
| --- | --- | --- | --- | --- | --- |
| 1 | First Aid | Simple | 2 | 3 | 3 |
| 1 | Herbalism | Simple | 2 | 3 | 6 |
| 2 | Biology | Normal | 2 | 4 | 10 |
| 2 | Medicine | Complex | 3 | 6 | 16 |
| 3 | Surgery | Complex | 3 | 6 | 22 |

Full surgeon = **22 XP, 5 skills on the sheet** (First Aid 2, Herbalism 2, Biology 2, Medicine 3, Surgery 3).

GURPS precedent — the .skl validates the shape:
- **Surgery ← First Aid OR Physician** (literally this chain).
- **Herb Lore ← Naturalist**, **Pharmacy (Herbal) ← Naturalist** — folk knowledge sits under the science, same as Biology ← Herbalism.
- Open question: Medicine requires Biology **2** here, not 3. Named prereqs vs. generic tier floors ("any Normal@3") — pick one rule. Named is richer and matches GURPS data.


## Master Skill List — rearrange me

All skills TL≤5. **★ = in the current [[5. Skills]]**. **† = GURPS difficulty disagrees with the column.** Regrouped by prereq role: foundations (is-a-prereq) sit left, the skills built on them sit beside with the presumed prereq in the next column. Blank row = theme break. Presumed levels follow the scheme — Simple @ 2 for Average, named @ 2–3 for Complex; GURPS-attested chains kept (12/14/16 → 2/3/4, Mathematics (Applied) → Mathematics (Advanced), Shiphandling's Leadership swapped for Seamanship to stay in-tier). **Blank prereq = gets a stat prereq from me.**

| Simple              | Average                | Average's prereqs           | Complex                               | Complex's Prereqs                               |
| ------------------- | ---------------------- | --------------------------- | ------------------------------------- | ----------------------------------------------- |
| Cooking             | Brewing                | Cooking 2                   | Alchemy                               | Herbalism 2, Brewing 2                          |
| Gardening           | Farming                | Gardening 2                 | Poisons                               | Herbalism 2                                     |
| Herbalism           | Bartender              | Cooking 2                   |                                       |                                                 |
| Fishing             |                        |                             |                                       |                                                 |
| Housekeeping        |                        |                             |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| Mathematics (Basic) | Accounting             | Mathematics (Basic) 2       | Economics                             | Mathematics (Advanced) 2                        |
|                     | Mathematics (Advanced) | Mathematics (Basic) 2       |                                       |                                                 |
|                     | Merchant               | Accounting 2                |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| ★Navigation         | Shiphandling           | Navigation 2 + Seamanship 2 | Airshipman                            | Shiphandling 2                                  |
| Area Knowledge      | Cartography            | Navigation 2                |                                       |                                                 |
| Seamanship          | Boating                |                             |                                       |                                                 |
|                     | Weather Sense          |                             |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| ★Fast-talk          | ★Manipulation          | ★Fast-talk 2                | Diplomacy                             | ★Manipulation 2                                 |
| ★Gossip             |                        |                             |                                       |                                                 |
|                     |                        |                             | Brainwashing                          | Social Science 2                                |
| Body Language       | Detect Lies            | Body Language 2             |                                       |                                                 |
|                     |                        |                             | Captivate                             | Suggest 2 + Public Speaking 2 + perk: Charisma  |
| Public Speaking     | ★Leadership†           | Public Speaking 2           | Enthrallment                          | Public Speaking 2 + perk: Charisma              |
|                     |                        |                             | Persuade                              | Public Speaking 2 + perk: Charisma              |
|                     |                        |                             | Suggest                               | Persuade 2 + Public Speaking 2 + perk: Charisma |
|                     |                        |                             | Sway Emotions                         | Public Speaking 2 + perk: Charisma              |
|                     |                        |                             |                                       |                                                 |
| Carousing           | Administration         |                             | Law                                   | Politics 2                                      |
| Savoir-Faire        | ★Intimidation          |                             | Propaganda†                           | Public Speaking 2                               |
| Sex Appeal          | Interrogation          | ★Intimidation 2             |                                       |                                                 |
|                     | ★Negotiating           |                             |                                       |                                                 |
|                     | Politics               | ★Negotiating 2              |                                       |                                                 |
|                     | Erotic Art             | Sex Appeal 2                |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| ★Dancing†           | ★Acting                |                             | Mimicry                               | ★Acting 2                                       |
| ★Singing            | Musical Instrument     |                             | Artist                                |                                                 |
|                     | Performance            | ★Acting 2                   | Musical Composition                   | Musical Instrument 2                            |
|                     | Poetry                 | Writing 2                   | Ventriloquism                         | ★Acting 2                                       |
|                     | Stage Combat           | ★Acting 2                   |                                       |                                                 |
|                     | Writing                |                             |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| ★Climbing†          | ★Acrobatics†           | ★Jumping 2                  |                                       |                                                 |
| ★Jumping            | Hiking                 | ★Running 2                  |                                       |                                                 |
| ★Lifting†           |                        |                             |                                       |                                                 |
| ★Running†           |                        |                             |                                       |                                                 |
| ★Swimming           |                        |                             |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
|                     | Gambling               | Games 2                     | Escape                                | ★Lockpicking 2                                  |
| Games               | Disguise               | Makeup 2                    | Forgery                               | Writing 2                                       |
| Makeup              |                        | ★Sleight of Hand† 2         | Pickpocket                            | Filch 2                                         |
| Panhandling         |                        |                             |                                       |                                                 |
| Scrounging          | Lip Reading            |                             |                                       |                                                 |
| ★Sleight of Hand†   | Observation            |                             |                                       |                                                 |
| ★Streetwise†        | Search                 | Observation 2               |                                       |                                                 |
|                     | Shadowing              | ★Stealth 2                  |                                       |                                                 |
|                     | Smuggling              | ★Streetwise† 2              |                                       |                                                 |
|                     | ★Stealth               |                             |                                       |                                                 |
| Camouflage          | Trapmaking             | ★Camouflage                 |                                       |                                                 |
|                     | Urban Survival         | ★Streetwise† 2              |                                       |                                                 |
|                     | ★Breaking              |                             |                                       |                                                 |
|                     | ★Lockpicking           | ★Sleight of Hand† 2         |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| Animal Handling     | Falconry               | Animal Handling 2           | Naturalist                            | ★Survival 2                                     |
|                     | Riding                 | Animal Handling 2           | Veterinary                            | Animal Handling 2 + ★Biology† 2                 |
|                     | ★Survival              |                             |                                       |                                                 |
|                     | ★Tracking              | ★Survival 2                 |                                       |                                                 |
|                     |                        |                             |                                       |                                                 |
| First Aid           | ★Medicine              | First Aid 2 + ★Biology† 2   | Pharmacy                              | Naturalist 2                                    |
|                     | Physiology             | ★Biology† 2                 | Surgery                               | ★Medicine 3                                     |
|                     |                        |                             |                                       |                                                 |
| Research            | ★Biology†              | Herbalism 2                 | Archaeology                           | ★History† 2                                     |
|                     | Astronomy              | Mathematics (Advanced) 2    | ★Chemistry                            | Mathematics (Advanced) 2                        |
|                     | Cryptography           | Mathematics (Basic) 2       | Geography                             | Cartography 2                                   |
|                     | Heraldry               | Research 2                  | Geology                               | Geography 2                                     |
|                     | ★History†              | Research 2                  | Linguistics                           | Research 2                                      |
|                     | Teaching               |                             | Literature                            | Research 2                                      |
|                     |                        |                             | Philosophy                            |                                                 |
|                     |                        |                             | Physics                               | Mathematics (Advanced) 2                        |
|                     |                        |                             | Social Science (Applicable of Choice) | Research 2                                      |
|                     |                        |                             |                                       |                                                 |
|                     | Fortune-Telling        |                             | Autohypnosis                          | Hypnotism 2                                     |
|                     | Hidden Lore            | Occultism 2                 | Breath Control                        | Meditation 2                                    |
|                     | Occultism              |                             | Dreaming                              |                                                 |
|                     | ★Theology†             |                             | Exorcism                              | ★Theology† 2                                    |
|                     |                        |                             | Hypnotism                             |                                                 |
|                     |                        |                             | ★Magical Theory                       | Occultism 2                                     |
|                     |                        |                             | Meditation                            |                                                 |
|                     |                        |                             | Religious Ritual                      | ★Theology† 2                                    |
|                     |                        |                             | Ritual Magic                          | Religious Ritual 2                              |
|                     |                        |                             |                                       |                                                 |
|                     | Soldier                |                             | Intelligence Analysis                 | Research 2                                      |
|                     | Armoury                | ★Smithing 2                 | Strategy                              | ★History† 2                                     |
|                     |                        |                             | Tactics                               | Soldier 2                                       |
|                     |                        |                             |                                       |                                                 |
| Knot-Tying          | Architecture           | Mathematics (Basic) 2       | ★Engineering                          | Mathematics (Advanced) 2                        |
| Leatherworking      | Freight Handling       |                             | Jeweler                               | ★Smithing 2                                     |
| Masonry             | Prospecting            |                             | Metallurgy                            | Geology 2                                       |
|                     | ★Textilework           |                             | ★Smithing                             |                                                 |
|                     | ★Woodworking           |                             |                                       |                                                 |

**Cut this pass (6):** Cooking + Herbalism duplicate rows · ★Navigation double-listed (Simple + Average) — merged to Simple ★Navigation, class call is yours · Psychology → Social Science (Applicable of Choice) (Brainwashing prereq updated) · Finance → Economics · Counterfeiting → Forgery.

**Fold candidates (kept, your call):** Captivate/Enthrallment/Persuade/Suggest/Sway Emotions → one Complex Enthrallment · Meditation/Autohypnosis/Breath Control → one discipline · Mimicry/Ventriloquism · Hidden Lore/Occultism · Physiology/Biology.

**Combat check:** main table is clean — weapons/unarmed live in their own table; Stage Combat kept (it is performing arts).



## GURPS Import (Basic Set Skills.skl — parsed)

718 rows = 277 unique skills + 60 techniques (skip techniques) + specialization variants. Difficulty: **E 45 / A 123 / H 94 / VH 15**.

Mapping: E→Simple, A→Normal, H→Complex, VH→Complex (with deeper prereqs / lower world cap).


### GURPS's own prereq chains (93 named edges in the file)

- Engineer (every spec) ← Mathematics (Applied); Physics ← Mathematics (Applied); Astronomy ← Mathematics (Applied).
- Shiphandling ← {Seamanship, Navigation (sea), Leadership}.
- Group Performance ← {Diplomacy OR Intimidation OR Leadership} + spec skill.
- Esoterics gate at **absolute levels** (12/14/16) — ExceedV's tier-level gates (2/3) are the cleaner equivalent.
- Fantasy-relevant: Surgery ← First Aid|Physician; Herb Lore ← Naturalist; Pharmacy (Herbal) ← Naturalist.

### Import shortlist (fantasy-relevant gaps in the current 33)

| Skill              | GURPS | ExceedV class | Why                                            |
| ------------------ | ----- | ------------- | ---------------------------------------------- |
| First Aid          | e     | S             | required by Medicine chain — currently missing |
| Herbalism          | vh    | S             | required by Biology — user-defined Simple      |
| Surgery            | vh    | C             | top of Medicine chain                          |
| Diagnosis          | h     | C             | medic loop: identify → treat                   |
| Pharmacy (Herbal)  | h     | C             | potions                                        |
| Naturalist         | h     | N             | GURPS anchors Herb Lore/Pharmacy on it         |
| Animal Handling    | a     | N             | Tamer perk, mounts                             |
| Riding             | a     | N             | Polearm/mount combat perks                     |
| Merchant           | a     | N             | Haggler, Bribery Expert, economy               |
| Performance        | a     | N             | bard suite (Singing/Dancing already exist)     |
| Musical Instrument | h     | C             | bard suite                                     |
| Public Speaking    | a     | N             | feeds Leadership/Enthrallment chains           |
| Detect Lies        | h     | N             | Liar Liar                                      |
| Disguise           | a     | N             | rogue suite                                    |
| Forgery            | h     | C             | rogue suite                                    |
| Pickpocket         | h     | N             | rogue suite                                    |
| Shadowing          | a     | N             | rogue suite                                    |
| Gambling           | a     | N             | Cheater                                        |
| Carousing          | e     | S             | social breadth                                 |
| Scrounging         | e     | S             | Simple fodder                                  |
| Fishing            | e     | S             | Forager                                        |
| Camouflage         | e     | S             | Simple fodder                                  |
| Knot-Tying         | e     | S             | Simple fodder                                  |
| Strategy           | h     | C             | Wargame master                                 |
| Tactics            | h     | C             | Wargame master                                 |
| Teaching           | a     | N             | [[Training Rules]] synergy — teachers matter   |
| Research           | a     | N             | Librarian, Well Read                           |
| Writing            | a     | N             | scholarly                                      |
| Heraldry           | a     | N             | Heraldist perk                                 |
| Savoir-Faire       | e     | S             | perk already exists                            |
| Occultism          | a     | N             | magical breadth                                |
| Religious Ritual   | h     | C             | Ordained                                       |
| Exorcism           | h     | C             | undead content                                 |
| Cooking            | e     | S             | Simple fodder                                  |
| Weather Sense      | a     | S             | outdoor                                        |
| Astronomy          | h     | C             | scholarly                                      |
| Geography          | h     | N             | scholarly                                      |
| Law                | h     | C             | Licensed Healer, politics                      |
| Politics           | a     | N             | Leadership chain                               |

## Perk → Skill Conversions (candidates)

Perks whose entire body is "you are good at X" dissolve into skill levels / Unlocks lists:

| Perk file | Becomes | Class | GURPS anchor |
| --- | --- | --- | --- |
| First Responder | First Aid | S | First Aid (e) |
| Herbalist's Eye | Herbalism unlocks | S | Herb Lore |
| Surgeon's Precision (UNEDITED) | Surgery | C | Surgery (vh) |
| Toxicologist (UNEDITED) | Poisons | N | Poisons (h) |
| Potion Brewer / Master Brewer | Potioncraft | C | Pharmacy (h) |
| Anatomical Knowledge | Anatomy | C | Physiology (h) |
| Cartographer's Mind | Cartography | N | Cartography (a) |
| Public Speaker (UNEDITED) | Public Speaking | N | (a) |
| Librarian / Well Read (UNEDITED) | Research | N | Research (a) |
| Liar Liar | Detect Lies | N | Detect Lies (h) |
| Tamer (UNEDITED) | Animal Handling | N | (a) |
| Wargame master | Strategy | C | Strategy (h) |
| Cheater | Gambling | N | Gambling (a) |
| Comedian | Performance | N | Performance (a) |
| Haggler / Bribery Expert | Merchant | N | Merchant (a) |
| Spell Identification / Spell-Craft (UNEDITED) | Spellcraft | — | already skill-gated, missing from [[5. Skills]] |
| Rumour Monger / Avid Gosspier | Gossip unlocks | S | — |
| Forager | Survival / Fishing unlocks | — | — |
| Natural Predator / Primeval Awareness | Survival / Tracking unlocks | — | — |
| Tracker | Tracking unlocks | — | — |
