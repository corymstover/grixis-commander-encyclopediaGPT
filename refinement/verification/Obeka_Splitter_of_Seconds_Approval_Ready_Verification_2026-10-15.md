# Obeka, Splitter of Seconds — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #45 of 62  
Exact candidate SHA-256: `9846e43dbe74fe49a9d356e944dc0a05d7dee30015e0d36e667fdbd01cb1ee75`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **44 APPROVED / LOCKED decks** through Obeka, Brute Chronologist. The tracker identifies **Obeka, Splitter of Seconds** as the next unlocked deck (tracker index 44 / deck 45 of 62).

No previously locked deck was modified during this refinement.

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: October 12 FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Obeka__Splitter_of_Seconds.txt`
- Raw FINAL TXT SHA-256: `c5bb697b0be0a06190326dd1e40971780772949b10c261be3cd83696efd68a4f`
- FINAL CSV: `GrixisFINAL60--2026.zip / Obeka__Splitter_of_Seconds.csv`
- Raw FINAL CSV SHA-256: `c09cb29e4f89ed9dd53b5974823eeb86295d46f1837dd5e3edd3002ac6f085c1`
- Baseline total: **100 cards**
- Baseline distinct names: **94**
- Baseline lands: **35**
- Repeated names: **Island x4 / Mountain x3 / Swamp x2 only**
- CSV/TXT membership reconciliation: **PASS**

Older October 11 audit/tracker rows are historical evidence only. The October 12 FINAL exports control membership and already contain Jhoira of the Ghitu, Replicating Ring, Ring of Xathrid, Thopter Spy Network, and Time Sieve.

Result: **PASS**.

## 3. Commander-first blueprint / natural ceiling

Current Oracle identity:
- `Obeka, Splitter of Seconds` — `{1}{U}{B}{R}`
- Legendary Creature — Ogre Warlock
- Menace
- Whenever Obeka deals combat damage to a player, the controller gets that many additional upkeep steps after the current phase.

Official release-note rules establish that each added upkeep is contained in an additional beginning phase after combat with untap/draw skipped, and `at the beginning of your upkeep` abilities trigger in every added upkeep.

Final architecture: **connect Obeka -> multiply actual combat damage / trigger instances -> convert added upkeeps into monarch, token, card, counter, drain, suspend, and artifact value -> leverage Time Sieve where artifact production supports repeated turns.**

Historical full-project reranking placed Obeka, Splitter of Seconds at approximately **685.66, Bracket 4 — Optimized**, with no usable tournament sample and very high commander-synergy/cohesion. Current optimized community evidence remains centered on Extra Upkeeps / Voltron / Extra Turns / Monarch rather than a stable cEDH shell.

Natural ceiling: **Power Bracket 4 — Optimized**.

Recommended tags: **Extra Upkeeps / Combat Damage / Upkeep Triggers**.

Result: **PASS**.

## 4. Mandatory 99-slot audit

Artifact: `refinement/verification/Obeka_Splitter_of_Seconds_Whole_List_Audit_2026-10-15.md`

- All baseline noncommander copies adjudicated: **99/99**
- Weighted result: **82 KEEP / 17 CUT**
- Strategic changes: **7**
- Mana-base changes: **10 card copies**
- Candidate SHA binding: **PASS**

Result: **PASS**.

## 5. Exact final delta

Strategic:
1. Blasphemous Act -> Roaming Throne
2. Descent into Avernus -> Palace Siege
3. Lizard Blades -> Mjölnir, Hammer of Thor
4. Scrawling Crawler -> Hatred
5. Skyline Despot -> Ginger, Queen of Sweets
6. Strionic Resonator -> Wizard's Staff
7. Winged Boots -> Dragonfire Blade

Mana:
8. Dragonskull Summit -> Arid Mesa
9. Drowned Catacomb -> Flooded Strand
10. Shipwreck Marsh -> Marsh Flats
11. Stormcarved Coast -> Misty Rainforest
12. Sulfur Falls -> Verdant Catacombs
13. Exotic Orchard -> Wooded Foothills
14. Reliquary Tower -> Mana Confluence
15. 1x Island -> City of Brass
16. 1x Mountain -> Reflecting Pool
17. Rogue's Passage -> Arena of Glory

Result: **PASS**.

## 6. Rules / interaction gate

### Obeka additional-upkeep structure
PASS. Additional upkeeps become additional beginning phases after combat; untap and draw are skipped; upkeep triggers still trigger.

### Roaming Throne / Wizard's Staff
PASS. Choose Ogre or Warlock for Roaming Throne. Both Throne and Staff cause Obeka's triggered ability to trigger one additional time. With both present, the original trigger plus one additional trigger from each effect yields three total trigger instances for one combat-damage event. Wizard's Staff uses normal equip `{3}` because Obeka is a Warlock, not a Wizard.

### Mjölnir
PASS. Obeka is legendary, red, and not a Villain, so she is worthy. Equip worthy `{1}` is legal. Mjölnir doubles the damage the equipped creature would deal; Obeka therefore sees the modified combat-damage amount when determining additional upkeeps.

### Dragonfire Blade
PASS. Obeka is three colors, so the equip `{4}` activation costs `{1}` when targeting her. +2/+2 turns her base 2 power into 4 and hexproof from monocolored improves protection.

### Hatred
PASS. X life is paid as an additional cost and the target gets +X/+0 until end of turn. If Obeka connects, the increased actual combat damage increases her upkeep count.

### Double strike
PASS. If Obeka deals combat damage in both first-strike and normal combat-damage steps, her ability triggers separately for each damage event.

### Palace Siege
PASS. Dragons mode triggers at every controller upkeep: each opponent loses 2 life and the controller gains 2 life. Every Obeka-created upkeep generates another trigger.

### Ginger / Time Sieve / Thopter Spy Network
PASS with resource qualification. Ginger creates a Gingerbrute artifact token at each upkeep while its controller is monarch. Thopter Spy Network creates a Thopter artifact creature at each controller upkeep if an artifact is controlled. Time Sieve requires tapping and sacrificing five artifacts for an extra turn.

A repeatable-turn engine is valid when Obeka can continue connecting for enough damage and artifact production can replace the five sacrificed artifacts. With a 4-damage Obeka connection, Network or Ginger can make four artifacts during the postcombat extra upkeeps; the normal upkeep of the next extra turn can supply a fifth. The first activation still requires sufficient seed artifacts unless at least five postcombat upkeep triggers are generated. No unconditional resource-free three-card infinite is claimed.

### Arena of Glory
PASS. It can enter untapped when a Mountain is controlled. Its exert ability produces `{R}{R}` after paying `{R}`; if any of that generated mana is spent on Obeka's creature spell, Obeka gains haste until end of turn.

Result: **PASS**.

## 7. Candidate exhaustion / adversarial red-team

The final pass challenged:
- Bitterbloom Bearer
- Genji Glove
- Hall of Echoes
- Aether Tunnel
- Rilsa Rael, Kingpin
- Sphinx of the Second Sun
- The Ninth Doctor
- Braid of Fire
- generic fast mana
- generic extra turns
- generic cEDH finishes
- all existing evasion/protection slots
- all seven proposed strategic swaps
- all 35 final lands

Wizard's Staff materially beat the first working candidate's Strionic Resonator slot and was incorporated before final binding. After that correction, no challenger produced a material improvement without a larger cost in mana, redundancy, colored consistency, commander necessity, or natural-ceiling identity.

**ZERO NEW MATERIAL IMPROVEMENTS.**

Result: **PASS**.

## 8. Structural verification

Approval-ready candidate:
- Total cards: **100**
- Distinct names: **96**
- Lands: **35**
- Repeats: **Island x3 / Mountain x2 / Swamp x2 only**
- Commander first: **PASS**
- Singleton compliance: **PASS**
- Color identity: **U/B/R — PASS**

Candidate SHA-256: `9846e43dbe74fe49a9d356e944dc0a05d7dee30015e0d36e667fdbd01cb1ee75`

Result: **PASS**.

## 9. Current official Commander legality

The current Wizards Commander banned list was checked on 2026-10-15. None of the candidate's cards appear on the Commander banned list. The October 12, 2026 general B&R announcement made Competitive Brawl changes and did not create a Commander legality issue for this candidate.

New/current additions checked as Commander-legal include Ginger, Queen of Sweets; Mjölnir, Hammer of Thor; Wizard's Staff; Dragonfire Blade; Roaming Throne; Palace Siege; Hatred; and Arena of Glory.

Project exception required: **NO**.

Result: **PASS**.

## 10. Final gate

- authoritative FINAL baseline: PASS
- commander-first blueprint: PASS
- 99/99 whole-list audit: PASS
- candidate exhaustion: PASS
- Oracle/rules interaction review: PASS
- mana/curve red-team: PASS
- exact 100-card structure: PASS
- singleton: PASS
- U/B/R identity: PASS
- current Commander legality: PASS
- project exception handling: NOT REQUIRED
- zero-new-material-improvement closure: PASS

**FINAL RESULT: APPROVAL_READY — NOT APPROVED / NOT LOCKED.**
