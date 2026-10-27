# Deck #50 Sauron, the Dark Lord — M7 Rev1 canonical approval verification

Date: 2026-10-27 (America/Chicago)  
Cycle: `global-restart-2026-10-13`

- **Approved full UTF-8 raw SHA-256:** `266660c6a3241c07a052da7624366be1f9617cb5db4c35c422b0e8f828977d9b`.
- **Prior approved October 15 full raw SHA-256:** `fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8`. Original file and records preserved.
- **Physical list:** exactly 100 cards, one commander plus 99 library cards, 91 distinct names.
- **Deck-construction copy limits:** Nazgûl ×7 permitted by its Oracle up-to-nine text; Swamp ×3 and Mountain ×2 are basics. No unpermitted duplicates.
- **Lands:** exactly 34 physical lands including the Cavern of Souls one-for-one replacement for Rogue's Passage; sufficient colored access still depends on actual draw and sequencing.
- **Color identity:** Commander and every card within U/B/R. No designated project bans/exceptions invoked.
- **Live current Oracle and official Commander legality:** all 91 names successfully resolved and checked legal via exact-head CI live Scryfall run #40486455373, including card-specific Nazgûl construction and independent `Reanimate` identity resolution.
- **Exact delta:** ten named 1-for-1 changes from the saved October 15 list, with the original 100 unchanged.
- **Mechanics:** commander requires a legal six-mana 3UBR cast; an opponent CAST triggers Orc amass even if their spell is countered; ward requires an opposing legendary artifact or creature sacrifice to resolve a spell targeting Sauron. Army combat damage to a *player* causes a Ring temptation, then a voluntary entire-hand discard/draw four. Seven Nazgûl trigger separate Wraith-wide +1/+1 counter waves. Mauhúr adds only one counter *per qualifying placement event*; The Great Goblin delivers its target-opponent damage per event, not per counter. Arcane Adaptation Wraith typing and Wraith-named Roaming Throne can double Sauron's, Nazgûl's and Great Goblin's relevant triggers, whereas without Adaptation type choices differ. Cavern of Souls naming Avatar applies uncounterability only to a qualifying Avatar creature spell. Moonstone exiles discarded cards optionally, preventing graveyard reanimation of cards thus exiled; Bone Miser and Glint-Horn fire separately on physical discarded cards.
- **P0/P1 executable candidate-bound checks:** 15 historical named source blueprint cases plus one changed-card discarded-zone/mana/damage test, 16/16 PASS on exact head; negative scenarios include sweeper removal, invalid Soothing target, lost Goblin source after/before an event, negated mana payment, failed Army player damage, quiet opponents and source absence.
- **Local decision and alternative audit:** M7 owner-ready structural/full-deck gate passed, 18 material judgments, 16 challenged incumbent slots, complete 12-swap and early-Ring alternatives. No inflated win-rate claim or unbounded loop proof.
- **Source engineering:** [PR #731](https://github.com/corymstover/GrokBotMTGCompanion/pull/731), exact commit `beb3487d95b7e32c0b5f2279520f1686e229a97b`, merged as `2422053a1ed89895daac9f71a1ffa81bb08863b9`.
- **GitHub Actions:** [Deck #50 exact-head run #40486455373](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40486455373) SUCCESS, including source physical 100, full 91-name Scryfall, all 16 test cases, M7 decision gate; [repository-wide M7 contract run #40486455403](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40486455403) SUCCESS.
- **Owner authorization:** Cory's single exact-SHA message on 2026-10-27 explicitly approved Deck #50 and authorized engineering merge, canonical lock and post-merge verification. No additional approval requested.
- **Current canonical deck artifact:** `refinement/decklists/Sauron_the_Dark_Lord_M7_Rev1_Approved_2026-10-27.txt`. **Approval authority:** `state/current_deck_overrides.json`, entry `Sauron__the_Dark_Lord`, APPROVED/LOCKED with exact SHA.
- **Power:** Bracket 4 — Optimized. **Tags:** Amass Orcs / Ring Temptation / Wraiths.

**Boundary:** Source-bound per-deck verification does not retroactively seal the historical input-only M6 I/J Phase B, nor does it mean aggregate M6.10/M7/M8 milestone acceptance or measured multiplayer performance.
