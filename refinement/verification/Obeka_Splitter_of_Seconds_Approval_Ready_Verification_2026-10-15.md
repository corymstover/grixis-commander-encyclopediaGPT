# Obeka, Splitter of Seconds — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #45 of 62  
Exact candidate SHA-256: `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **44 APPROVED / LOCKED decks** through Obeka, Brute Chronologist. The reconciled tracker identifies **Obeka, Splitter of Seconds** as the next unlocked deck (tracker index 44 / deck 45 of 62).

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

Older October 11 tracker/audit rows are historical evidence only. The October 12 FINAL exports control membership.

Result: **PASS**.

## 3. Commander-first blueprint / natural ceiling

Current commander identity:
- `Obeka, Splitter of Seconds` — `{1}{U}{B}{R}`
- Legendary Creature — Ogre Warlock
- Menace
- Whenever Obeka deals combat damage to a player, her controller gets that many additional upkeep steps after that phase.

Official release-note treatment establishes that these added upkeep steps occur in additional beginning phases after combat with untap and draw skipped. `At the beginning of your upkeep` abilities trigger during every added upkeep.

Final architecture:
**connect Obeka -> increase actual combat damage / multiply trigger instances -> convert added upkeeps into cards, Treasures, Clues, counters, suspend acceleration, monarch pressure, artifact production, alternate wins, and Time Sieve turns.**

Project reranking places the deck at approximately **685.66, Power Bracket 4 — Optimized**, with very high commander synergy and no usable tournament sample supporting cEDH.

Natural ceiling: **Power Bracket 4 — Optimized**.

Recommended tags: **Extra Upkeeps / Combat Damage / Upkeep Triggers**.

Result: **PASS**.

## 4. Mandatory 99-slot audit

Artifact: `refinement/verification/Obeka_Splitter_of_Seconds_Whole_List_Audit_2026-10-15.md`

- All baseline noncommander copies adjudicated: **99/99**
- Weighted result: **80 KEEP / 19 CUT**
- Strategic changes: **9**
- Mana-base changes: **10 card copies**
- Candidate SHA binding: **PASS**

Result: **PASS**.

## 5. Exact final delta

Strategic:
1. Blasphemous Act -> Roaming Throne
2. Descent into Avernus -> Darksteel Reactor
3. Generous Plunderer -> Smaug the Magnificent
4. Lizard Blades -> Mjölnir, Hammer of Thor
5. Mithril Coat -> Tamiyo's Journal
6. Scrawling Crawler -> Hatred
7. Skyline Despot -> Super Intelligence
8. Strionic Resonator -> Wizard's Staff
9. Winged Boots -> Dragonfire Blade

Mana:
10. Dragonskull Summit -> Arid Mesa
11. Drowned Catacomb -> Flooded Strand
12. Shipwreck Marsh -> Marsh Flats
13. Stormcarved Coast -> Misty Rainforest
14. Sulfur Falls -> Verdant Catacombs
15. Exotic Orchard -> Wooded Foothills
16. Reliquary Tower -> Mana Confluence
17. 1x Island -> City of Brass
18. 1x Mountain -> Reflecting Pool
19. Rogue's Passage -> Arena of Glory

Result: **PASS**.

## 6. Rules / interaction gate

### Additional-upkeep structure
PASS. Obeka-created upkeeps occur in additional beginning phases after combat; untap/draw are skipped and upkeep-triggered abilities still trigger.

### Actual damage controls upkeep count
PASS. Obeka uses the combat damage actually dealt. Power increases and damage-doubling replacement effects therefore directly change the number of additional upkeeps.

### Mjölnir, Hammer of Thor
PASS. Obeka is legendary, red, and not a Villain, so she is worthy and may use equip worthy `{1}`. Mjölnir doubles all damage equipped Obeka would deal. A base 2-power hit therefore deals 4 and produces four added upkeeps before other trigger multipliers are considered.

### Dragonfire Blade
PASS. Obeka is three colors, so equip `{4}` costs `{1}` when targeting her. +2/+2 raises base power from 2 to 4 while hexproof from monocolored adds efficient protection.

### Hatred
PASS. X life is paid as an additional casting cost and the target receives +X/+0 until end of turn. Successful combat damage converts that increased power into additional upkeeps.

### Roaming Throne / Wizard's Staff
PASS. Roaming Throne can choose Ogre or Warlock. Wizard's Staff uses normal equip `{3}` because Obeka is a Warlock, not a Wizard. Each effect causes the relevant triggered ability to trigger one additional time. With both applying, one combat-damage event generates **three total Obeka trigger instances**: original + Throne + Staff, not four.

### Combat Research
PASS. Combat Research gives legendary Obeka +1/+1 and a combat-damage draw trigger. The +1/+1 directly increases upkeep count. The granted triggered ability is an ability of the enchanted creature and is therefore also subject to applicable additional-trigger effects from Staff and correctly typed Roaming Throne.

### Double strike
PASS. Embercleave can cause Obeka to deal combat damage in first-strike and regular combat-damage steps. Each separate damage event triggers Obeka independently; Throne/Staff apply to each event.

### Super Intelligence
PASS. The Aura draws a card at the beginning of the enchanted creature controller's upkeep. Enchanting Obeka converts each normal and Obeka-created upkeep into another card while both permanents remain available.

### Smaug the Magnificent
PASS. Smaug creates a Treasure at the beginning of each controller upkeep. Obeka-created upkeeps therefore generate one Treasure each. Smaug's attack trigger deals damage equal to the number of Treasures controlled to any target. Unlike Generous Plunderer, this upkeep engine does not also give an opponent a Treasure.

### Darksteel Reactor
PASS. Reactor is indestructible, receives a charge-counter trigger during each controller upkeep, and wins once it has twenty or more charge counters. Every Obeka-created upkeep supplies another independent Reactor trigger.

### Tamiyo's Journal
PASS. Journal investigates during each controller upkeep. Extra upkeeps therefore create extra Clues. Its tap ability sacrifices three Clues to tutor any card. A given Clue cannot pay both Journal and Time Sieve costs simultaneously; artifact accounting remains explicit.

### Time Sieve / Thopter Spy Network
PASS with established-board qualification. Time Sieve itself is an artifact, so if Sieve and Thopter Spy Network are established before normal upkeep, Network's intervening-if condition is satisfied and the normal upkeep creates one Thopter.

If Obeka later connects for at least 4 damage, the four added upkeeps create four more Thopters. Those five Thopters can be sacrificed to Sieve for an extra turn while Sieve itself remains. If the same board survives and Obeka connects for 4+ again, the cadence can repeat. This is a board-dependent repeatable-turn engine, not an unconditional loop from an empty board.

Smaug and Journal supply additional artifact cadence, but Treasure/Clue expenditures must still be counted separately from Sieve or Journal activation costs.

### Arena of Glory
PASS. If any mana from the exert ability is spent to cast Obeka, the resulting creature gains haste until end of turn, giving an immediate combat window.

Result: **PASS**.

## 7. Hybrid conflict reconciliation / candidate exhaustion

Two different SHA-bound strategic concepts existed during this review. The first repository candidate (`9846e43d...`) used Ginger, Queen of Sweets and Palace Siege while retaining Generous Plunderer and Mithril Coat. A later independent challenger (`f1ce3365...`) used Smaug, Super Intelligence, Darksteel Reactor, Tamiyo's Journal, Aggravated Assault, and Blackblade Reforged but did not retain all of the stronger Mjölnir / Dragonfire Blade / Hatred package.

The candidates were not silently reconciled. Every disputed slot was re-opened and compared head-to-head.

Final hybrid decisions:
- **KEEP/ADD:** Mjölnir, Dragonfire Blade, Hatred, Roaming Throne, Wizard's Staff.
- **ADOPT:** Smaug, Super Intelligence, Darksteel Reactor, Tamiyo's Journal.
- **REJECT:** Ginger, Palace Siege, Aggravated Assault, Blackblade Reforged.

Why:
- Smaug captures the controller-upkeep cadence at four mana without gifting resources to opponents and is cheaper than Ginger.
- Super Intelligence is a one-mana draw engine for every extra upkeep; the final deck already has substantial direct life/damage upkeep pressure, so it beats five-mana Palace Siege on rate.
- Darksteel Reactor is a resilient one-sided alternate win whose counter requirement scales exactly with Obeka's extra upkeeps.
- Tamiyo's Journal converts the same upkeep volume into Clues plus unrestricted tutoring and reinforces Time Sieve.
- Aggravated Assault is highly powerful with retained Sword of Feast and Famine but constitutes a generic two-card combat loop that functions without Obeka; no commander-native engine was weak enough to justify the slot.
- Blackblade Reforged is strong pump but redundant after the final Mjölnir / Dragonfire / Hatred / Embercleave / Combat Research / Ring package.

Additional challengers rejected after full comparison include Robe of the Archmagi, The Ninth Doctor, Shadow of the Second Sun, Sphinx of the Second Sun, Bitterbloom Bearer, Genji Glove, Hall of Echoes, Aether Tunnel, Rilsa Rael, Braid of Fire, generic extra turns, generic fast mana, and Oracle/Consultation or unrelated Breach packages.

The hybrid was the final material improvement discovered. After binding it, the final serious pass produced:

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

Candidate SHA-256: `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`

Result: **PASS**.

## 9. Current official Commander legality

The current Wizards Commander banned list was checked on 2026-10-15. None of the candidate cards are on the Commander banned list. The October 12, 2026 B&R announcement concerned Competitive Brawl and did not create a Commander legality issue for this candidate.

Current additions screened as Commander-legal include Roaming Throne, Mjölnir, Dragonfire Blade, Hatred, Wizard's Staff, Smaug the Magnificent, Super Intelligence, Darksteel Reactor, Tamiyo's Journal, and Arena of Glory.

Project exception required: **NO**.

Result: **PASS**.

## 10. Final gate

- authoritative FINAL baseline: PASS
- commander-first blueprint: PASS
- 99/99 whole-list audit: PASS
- conflicting-candidate reconciliation: PASS
- candidate exhaustion: PASS
- current Oracle/rules interaction review: PASS
- Time Sieve artifact accounting: PASS
- mana/curve red-team: PASS
- exact 100-card structure: PASS
- singleton: PASS
- U/B/R identity: PASS
- current Commander legality: PASS
- project exception handling: NOT REQUIRED
- zero-new-material-improvement closure: PASS

**FINAL RESULT: APPROVAL_READY — NOT APPROVED / NOT LOCKED.**

The user's earlier `Approve` message was received **before** this exact hybrid candidate was presented and therefore is treated only as approval intent, not as approval of SHA `83062ff2...`. A new explicit approval of the exact presented candidate is required before lock/finalization.


## Approval-time SHA correction

On 2026-10-15, the fail-closed GitHub Actions finalizer recomputed the raw bytes of the unchanged approval-ready candidate as SHA-256 `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`. The previously documented `83062ff2dbc955c628f9a6df460cf72dd5d450b6685bc4b53f63894bc8c321fb` value was incorrect metadata, not a card-list change. SHA-bound artifacts were reconciled before approval state was finalized. No card membership, quantity, order, or text changed.
