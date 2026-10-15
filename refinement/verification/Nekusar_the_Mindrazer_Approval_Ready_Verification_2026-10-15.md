# Nekusar, the Mindrazer — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #40 of 62  
Exact candidate SHA-256: `bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **39 APPROVED / LOCKED decks** through Nathan Drake, Treasure Hunter. The reconciled tracker identifies **Nekusar, the Mindrazer** as the next unlocked deck (tracker index 39 / deck 40 of 62). No prior Nekusar current-cycle approval-ready artifact or lock exists.

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: current FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Nekusar__the_Mindrazer.txt`
- Raw FINAL TXT SHA-256: `02f2b89ba4234490c44b32ce767f0e5d3824ffc771ecb82f5e7e389a581f8671`
- FINAL CSV: `GrixisFINAL60--2026.zip / Nekusar__the_Mindrazer.csv`
- Raw FINAL CSV SHA-256: `a6cfca85330dab2aab8bf8fcf3e4bd4bb092695db9b3a8f69b2545a44b7c52ff`
- Baseline total: **100 cards**
- Baseline distinct names: **95**
- Baseline lands: **35**

The October 11 update tracker is historical only. Per project source-of-truth policy, the October 12 FINAL exports control membership.

Result: **PASS**.

## 3. Exact structural verification

SHA-bound candidate file: `refinement/decklists/Nekusar_the_Mindrazer_Approval_Ready_2026-10-15.txt`

- Total cards including commander: **100**
- Commander: **1x Nekusar, the Mindrazer**
- Lands: **35**
- Distinct names: **97**
- Repeated names: **Island x2, Mountain x2, Swamp x2** only
- Nonbasic/nonbasic-card singleton violations: **0**
- Baseline delta: **17 cuts / 17 additions**
- Whole-list adjudication: **82 KEEP / 17 CUT across all 99 noncommander slots**

Result: **PASS**.

## 4. Commander Oracle / color identity / legality

Current Nekusar text checked on 2026-10-15:

- `{2}{U}{B}{R}`
- Legendary Creature — Zombie Wizard
- 2/4
- At the beginning of each player's draw step, that player draws an additional card.
- Whenever an opponent draws a card, Nekusar deals 1 damage to that player.

Nekusar's color identity is **U/B/R**. Every candidate addition is within U/B/R identity or colorless/no-color-identity land.

Nekusar is currently Commander-legal. The current Wizards banned/restricted list was checked on 2026-10-15; no candidate card is a named Commander-banned card. Wizards' October 12, 2026 Banned & Restricted announcement made Competitive Brawl changes but no tabletop Commander change affecting this candidate. The February 9, 2026 Commander update unbanned Biorhythm and Lutri (Lutri still banned only as a companion) and made no new bans.

Project-specific exception required: **NONE**.

Result: **PASS**.

## 5. Wizard's Staff

Wizard's Staff costs `{1}{U}` and is Equipment. Equipped creature has prowess. If a triggered ability of equipped creature triggers, it triggers an additional time. It has `Equip Wizard {1}` and ordinary equip `{3}`.

Nekusar is a Zombie **Wizard**, so Staff equips him for `{1}`. Both of Nekusar's abilities are triggered abilities:

1. the beginning-of-draw-step trigger; and
2. the opponent-draw damage trigger.

Staff therefore adds an instance of both when they trigger. This is materially more commander-specific than the cut Psychosis Crawler, which costs five and only punishes the controller's own draws.

Result: **PASS**.

## 6. Harmonic Prodigy

Harmonic Prodigy says that if a triggered ability of a Shaman or another Wizard you control triggers, it triggers an additional time.

Nekusar is another Wizard you control relative to Harmonic Prodigy, so Prodigy adds an instance of both Nekusar triggered abilities. This stacks additively with Wizard's Staff.

Result: **PASS**.

## 7. Krang, the All-Powerful — exact scope

Krang says: if a player drawing a card causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time.

Official release notes confirm that Krang does not copy the ability; it causes another trigger and any choices are made separately for each instance.

Krang therefore adds an instance of:
- Nekusar's opponent-draw damage trigger;
- Fate Unraveler;
- Sheoldred, the Apocalypse;
- Underworld Dreams;
- Spiteful Visions;
- Phyrexian Tyranny;
- Kederekt Parasite when its condition is satisfied;
- Scrawling Crawler's opponent-draw life-loss ability; and other draw-caused triggers.

Krang **does not** add an instance of Nekusar's beginning-of-draw-step ability, because that ability is caused by the draw step beginning, not by a player drawing a card.

Result: **PASS**.

## 8. Trigger-multiplier stacking

Wizard's Staff, Harmonic Prodigy, and Krang each say that qualifying abilities trigger an additional time. These are additive additional-trigger effects, not a chain that repeatedly doubles previous doublers.

With Nekusar equipped with Wizard's Staff and both Harmonic Prodigy and Krang present:

- Nekusar's draw-step trigger: **base + Staff + Prodigy = 3 instances**.
- Nekusar's damage trigger from each opponent draw: **base + Staff + Prodigy + Krang = 4 instances**.

The three draw-step trigger instances are additional to the turn-based card draw, so an ordinary opponent draw step can produce four actual draws before other draw effects are considered.

This interaction was reviewed explicitly to avoid unsupported multiplicative trigger counts.

Result: **PASS**.

## 9. Ghyrson Starn / Solphim correction

Ghyrson Starn triggers whenever another source you control deals **exactly 1 damage** to a permanent or player, then Ghyrson deals 2 more damage to that object/player.

Nekusar's printed damage event is exactly 1, so each resolved Nekusar damage trigger can trigger Ghyrson.

Solphim, Mayhem Dominus instead creates a replacement effect: if a source you control would deal noncombat damage to an opponent or an opponent's permanent, it deals double that damage instead. With Solphim present, Nekusar's would-be 1 becomes 2; Ghyrson therefore does not see an event in which Nekusar dealt exactly 1.

This is a genuine internal anti-synergy. Cutting Solphim for Krang removes the conflict while increasing the number of Nekusar/draw-punishment triggers.

Result: **PASS**.

## 10. Curiosity with Nekusar

Curiosity enchants a creature and says whenever enchanted creature deals damage to an opponent, you may draw a card.

If Curiosity enchants Nekusar, every resolved Nekusar damage event to an opponent can trigger Curiosity and offer the controller an optional card draw. Those controller draws do not themselves trigger Nekusar's opponent-draw ability, so this is a powerful value engine rather than a self-loop.

Curiosity costs one mana and is more commander-specific than the cut Megrim, while Liliana's Caress remains as the cheaper discard-punishment effect.

Result: **PASS**.

## 11. Curiosity with Niv-Mizzet, Parun

Niv-Mizzet, Parun says whenever you draw a card, Niv deals 1 damage to any target. If Curiosity enchants Niv and Niv's damage is directed to an opponent, Curiosity may draw another card, which triggers Niv again.

Because Curiosity uses **may**, the controller can stop the sequence. The sequence is also bounded by the library unless another effect prevents decking/recycles cards. It is therefore documented as a repeatable optional draw/damage loop rather than an unsupported literal mathematical infinity.

This secondary line does not justify Curiosity by itself: Curiosity is already directly strong on Nekusar.

Result: **PASS**.

## 12. Winds of Change

Winds of Change costs `{R}` and has each player shuffle the cards from their hand into their library, then draw that many cards.

It does not discard and therefore does not trigger Waste Not/Liliana's Caress from those hand changes, but it is an exceptionally mana-efficient way to create many actual draws for Nekusar, Fate Unraveler, Underworld Dreams, Sheoldred, Krang, and other draw punishers.

It replaces Dictate of Kruphix because this list prioritizes controllable burst draw over giving opponents an extra card every turn indefinitely.

Result: **PASS**.

## 13. Molten Psyche

Molten Psyche costs `{1}{R}{R}`. Each player shuffles their hand into their library and draws that many cards. With metalcraft, it also deals damage to each opponent equal to the number of cards that opponent has drawn that turn.

The candidate contains at least thirteen artifacts/artifact creatures, including Anvil of Bogardan, Arcane Signet, Chrome Mox, Grim Monolith, Krang, Mana Vault, Scrawling Crawler, Sol Ring, all three Talismans, Teferi's Puzzle Box, and Wizard's Staff. Metalcraft is therefore a realistic payoff rather than a speculative splash condition.

Official rulings confirm that the metalcraft damage counts all cards each opponent drew that turn, not only the cards drawn from Molten Psyche.

Result: **PASS**.

## 14. Toxic Deluge

Toxic Deluge is a three-mana sweeper that gives all creatures -X/-X for the turn after paying X life as an additional cost.

The baseline relied heavily on spot/free interaction and Cyclonic Rift without a comparably efficient unconditional creature reset. Deluge gives Nekusar a low-cost reset that can be cast and followed by redeployment sooner than six-mana value engines such as The Locust God.

Result: **PASS**.

## 15. Mikokoro, Center of the Sea

Mikokoro taps for colorless and has `{2}, {T}: Each player draws a card.`

That ability converts a land slot into an instant-speed, repeatable each-player draw event. With Nekusar or other draw punishers present, it becomes part of the deck's primary engine. The candidate retains six basics and substantially improves the rest of the mana base, so one colorless utility land is acceptable.

Result: **PASS**.

## 16. Mana-base red team

The candidate remains at **35 lands**.

Key upgrades:
- Crumbling Necropolis → Mana Confluence
- Dragonskull Summit → Arid Mesa
- Drowned Catacomb → Flooded Strand
- Shipwreck Marsh → Marsh Flats
- Shivan Reef → Volcanic Island
- Stormcarved Coast → Misty Rainforest
- Sulfur Falls → Verdant Catacombs
- Sulfurous Springs → Underground Sea
- Underground River → Wooded Foothills
- one Island → City of Brass
- one Swamp → Mikokoro, Center of the Sea

The final mana base has **nine useful fetchlands** and retains/fetches Badlands, Underground Sea, Volcanic Island, Blood Crypt, Steam Vents, Watery Grave, Xander's Lounge, and six basics. This materially improves the ability to cast both Nekusar and the retained UUU/RRR Niv-Mizzet, Parun.

Mikokoro, Geier Reach Sanitarium, Reliquary Tower, Ancient Tomb, and Otawara remain the principal utility/colorless-pressure lands; their strategic upside is justified by the improved colored-source infrastructure around them.

Result: **PASS**.

## 17. Candidate exhaustion and red-team conclusions

Project top-100 candidates, historical P-006, current optimized Nekusar evidence, September 2026 Nekusar-specific research, new 2026 cards, wheel density, forced-draw engines, draw punishers, trigger multipliers, protection, sweepers, alternate kills, and mana-base challengers were reviewed.

Notable rejected alternatives:
- Historical Krang over Fate Unraveler: wrong cut after whole-list review; Solphim is weaker in this exact shell.
- Naktamun Lorespinner // Wheel of Fate: current Nekusar-specific research identifies a hand-size tension/nonbo.
- Master of the Feast, Seizan, Prosperity, Vision Skeins, Temple Bell: additional draw exists but does not beat current retained slots after rate/setup comparison.
- The Master of Lake-town: adds a mill subtheme and feeds opposing graveyards.
- Tomik, Izzet Sparkmage / Ojer Axonil: alter Nekusar's original 1-damage events and conflict with Ghyrson's exact-1 condition.
- Narset / Notion Thief wheel locks: powerful but suppress the actual opponent draws the commander wants to punish.
- Infect shortcuts: effective but identity-distorting.
- Mindcrank: Bloodchief combo is commander-independent and pushes toward mill.
- Generic Oracle/Consultation or unrelated deterministic Breach lines: not required for Nekusar's natural ceiling.
- More expensive wheels: current low-cost wheel density is sufficient.

Commander-necessity test: the refined package materially increases Nekusar's importance. Wizard's Staff and Harmonic Prodigy multiply his own triggers, Krang increases his draw-caused damage triggers, Curiosity converts his damage into cards, Winds/Molten create low-cost draw bursts for him to punish, and Mikokoro supplies a repeatable land-based draw event.

Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**.

Result: **PASS**.

## 18. Mandatory gate summary

- Current repository state recovered: **PASS**
- Current-cycle locked decks before Nekusar approval: **39/62**
- Nekusar correctly identified as next unlocked deck: **PASS**
- Authoritative FINAL baseline reconciled: **PASS**
- Mandatory 99-slot audit: **99/99 PASS**
- Whole-list result: **82 KEEP / 17 CUT**
- Candidate-ranking exhaustion: **PASS**
- Outside-ranking/current-2026 alternatives reviewed: **PASS**
- Commander Oracle text: **PASS**
- Color identity: **PASS**
- Current official Commander legality checkpoint: **PASS**
- Project exceptions: **NONE REQUIRED**
- Relevant rules/interactions: **PASS**
- Trigger-multiplier arithmetic: **PASS**
- Ghyrson/Solphim red-team correction: **PASS**
- Mana-base red team: **PASS**
- Commander-first coherence: **PASS**
- Natural power ceiling: **Power Bracket 4 — Optimized**
- Exact 100-card count: **PASS**
- Singleton compliance: **PASS**
- Final serious pass: **ZERO NEW MATERIAL IMPROVEMENTS**

Recommended Archidekt tags: **Wheels / Draw Punishment / Group Slug**.

## Final gate

**APPROVAL_READY — PASS**

Exact approval-ready candidate SHA-256: `bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1`.

This record is working verification evidence only. Nekusar, the Mindrazer remains **UNAPPROVED / UNLOCKED** until the user explicitly approves this exact candidate.
