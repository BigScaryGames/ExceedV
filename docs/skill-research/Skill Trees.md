# Skill Trees

Idea under test: skills organized as trees (trunk → branch → leaf), like spell trees. Trunk = entry point ("I want to be a medic" → grab the Medic trunk). Cross-prereqs between trees are intentional.
★ = current skill, rehomed. (basic) = node that prereqs many things elsewhere.
Classes: **Simple** = 1/2/4/6/8 XP. **Complex** = 2/4/6/8/10 XP, sometimes requires another skill at a level. No entry-level minimums.

## Medic
| Node | Class | Prereq | Notes |
| --- | --- | --- | --- |
| First Aid | Simple | — | Trunk |
| ★Medicine | Complex | First Aid 2 | Absorbs Physician, Diagnostics, Esoteric Medicine |
| Surgery | Complex | Medicine 2 | Absorbs Physiology (→ Biology in Natural Sciences) |

## Faith
| Node                   | Class   | Prereq     | Notes                                             |
| ---------------------- | ------- | ---------- | ------------------------------------------------- |
| ★Theology              | Complex | Wit 1      | Trunk. Absorbs Religious Ritual. Unlocks Exorcism |
| Exorcism               | Complex | Theology 2 |                                                   |

## Natural Sciences
| Node       | Class   | Prereq                        | Notes                            |
| ---------- | ------- | ----------------------------- | -------------------------------- |
| Naturalism | Simple  | —                             | Trunk. You can teach it to a kid |
| ★Biology   | Complex | Naturalism 2                  | Absorbs Physiology               |
| ★Chemistry | Complex | Naturalism 2                  |                                  |
| Physics    | Complex | Naturalism 2 + Math (basic) 1 |                                  |
| Herbalism  | Complex | Naturalism 1                  | Food & Herbs lane                |
| Astronomy  | Complex | Naturalism 1 + Math (basic) 1 |                                  |

## Crafts
| Node | Class | Prereq | Notes |
| --- | --- | --- | --- |
| Tinkering | Simple | — | Trunk. Unlocks crafting skills |
| ★Smithing | Complex | Tinkering 1 | |
| ★Woodworking | Complex | Tinkering 1 | |
| ★Textilework | Complex | Tinkering 1 | |
| ★Engineering | Complex | Tinkering 2 + Math (basic) 1 | |
| Alchemy | Complex | Herbalism 2 + Chemistry 1 | Cross: Natural Sciences |

## Wilderness
| Node | Class | Prereq | Notes |
| --- | --- | --- | --- |
| ★Survival | Simple | — | Trunk. Absorbs foraging |
| ★Tracking | Complex | Survival 1 | |
| ★Navigation | Simple | Survival 1 | |
| Fishing | Simple | Survival 1 | |
| Hunting | Complex | Survival 1 | |

## Beast
| Node            | Class   | Prereq                         | Notes        |
| --------------- | ------- | ------------------------------ | ------------ |
| Animal Handling | Simple  | —                              | Trunk        |
| Riding          | Complex | Animal Handling 1              |              |
| Falconry        | Complex | Animal Handling 2              |              |
| Veterinary      | Complex | Animal Handling 1 + Medicine 1 | Cross: Medic |

## Skulduggery
| Node             | Class   | Prereq                        | Notes              |
| ---------------- | ------- | ----------------------------- | ------------------ |
| ★Stealth         | Simple  | —                             | Trunk              |
| ★Lockpicking     | Complex | Stealth 1                     |                    |
| ★Sleight of Hand | Complex | Stealth 1                     |                    |
| ★Streetwise      | Complex | Stealth 1 or Fast-talk 1      | Cross: Charm       |
| Disguise         | Complex | Stealth 1                     | Absorbs Makeup     |
| Traps            | Complex | Lockpicking 1                 |                    |
| Forgery          | Complex | Sleight of Hand 1 + Writing 1 | Cross: Scholarship |

## Performance
| Node                            | Class   | Prereq                         | Notes                       |
| ------------------------------- | ------- | ------------------------------ | --------------------------- |
| Performance                     | Simple  | —                              | Trunk                       |
| ★Acting                         | Complex | Performance 1                  |                             |
| ★Dancing                        | Complex | Performance 1                  |                             |
| Musical Instrument (or Singing) | Complex | Performance 1                  |                             |
| Public Speaking                 | Complex | Performance 1                  | Feeds Diplomacy, Propaganda |
| Stage Combat                    | Complex | Acting 1 + any weapon training | Cross: weapon system        |

## Charm
| Node          | Class   | Prereq                          | Notes                       |
| ------------- | ------- | ------------------------------- | --------------------------- |
| ★Fast-talk    | Simple  | —                               | Trunk                       |
| ★Gossip       | Complex | Fast-talk 1                     |                             |
| ★Manipulation | Complex | Fast-talk 2                     | Absorbs Enthrallment family |
| ★Negotiating  | Complex | Fast-talk 1                     |                             |
| Savoir-Faire  | Simple  | —                               | Fitting-in lane             |
| Carousing     | Simple  | —                               |                             |
| Diplomacy     | Complex | Manipulation 2 + Negotiating 1  |                             |
| Detect Lies   | Complex | Gossip 2                        |                             |
| Interrogation | Complex | Manipulation 1 + Intimidation 1 | Cross: Command              |

## Command
| Node | Class | Prereq | Notes |
| --- | --- | --- | --- |
| ★Leadership | Simple | — | Trunk |
| ★Intimidation | Complex | Leadership 1 | |
| Strategy | Complex | Leadership 1 + History 1 | Cross: Scholarship |
| Politics | Complex | Leadership 1 | |
| Administration | Complex | Politics 1 | |
| Propaganda† | Complex | Public Speaking 2 | Cross: Performance |
| Law | Complex | Research 2 | Cross: Scholarship |

## Athletics
| Node        | Class   | Prereq      | Notes                                   |
| ----------- | ------- | ----------- | --------------------------------------- |
| Athletics   | Simple  | —           | Trunk (new — general physical literacy) |
| ★Acrobatics | Simple  | --          |                                         |
| ★Running    | Complex | Athletics 1 |                                         |
| ★Climbing   | Complex | Athletics 1 |                                         |
| ★Swimming   | Simple  | Athletics 1 |                                         |
| ★Jumping    | Complex | Athletics 1 |                                         |
| ★Lifting    | Complex | Athletics 1 |                                         |
| ★Breaking   | Complex | Lifting 2   |                                         |

## Seafaring
| Node         | Class   | Prereq                      | Notes             |
| ------------ | ------- | --------------------------- | ----------------- |
| Seamanship   | Simple  | —                           | Trunk             |
| Shiphandling | Complex | Seamanship 2 + Navigation 1 | Cross: Wilderness |


## Scholarship
| Node         | Class   | Prereq                        | Notes                                                    |
| ------------ | ------- | ----------------------------- | -------------------------------------------------------- |
| Research     | Simple  | —                             | Trunk                                                    |
| ★History     | Complex | Research 1                    |                                                          |
| Writing      | Complex | Research 1                    |                                                          |
| Linguistics  | Complex | Research 1                    | Absorbs language skills                                  |
| Math (basic) | Simple  | Research 1                    | Prereq hub: Physics, Engineering, Astronomy, Cartography |
| Cartography  | Complex | Math (basic) 1 + Navigation 1 | Cross: Wilderness                                        |
| Teaching     | Complex | Research 2                    |                                                          |
| Archaeology  | Complex | History 2                     |                                                          |

## Arcane
| Node            | Class   | Prereq                        | Notes                                               |
| --------------- | ------- | ----------------------------- | --------------------------------------------------- |
| ★Magical Theory | Complex | Math (basic) 1                | Trunk. Feeds Spellcraft domain (flavor, not prereq) |
| Occult Lore     | Complex | Magical Theory 1 + Theology 1 | Cross: Faith. Absorbs Hidden Lore, Occultism        |


## Trade
| Node | Class | Prereq | Notes |
| --- | --- | --- | --- |
| Merchant | Simple | — | Trunk. Absorbs Haggler, Bribery Expert |
| Appraisal | Complex | Merchant 1 | |
| Gambling | Complex | Merchant 1 + Gossip 1 | Cross: Charm. Absorbs Games |

## Open Items
- Herbalist's Eye → becomes Herbalism node action (after tree is final)
- Other perk→skill conversions (First Responder, Toxicologist, Liar Liar, Comedian…) applied after tree is final
