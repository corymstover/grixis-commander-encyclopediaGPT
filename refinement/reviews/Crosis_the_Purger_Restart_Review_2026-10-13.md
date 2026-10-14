# Crosis, the Purger — Fresh Restart Review

**Deck:** #9 of 62  
**Review date:** 2026-10-13 (America/Chicago)  
**Frozen baseline:** October 12 FINAL TXT/CSV archives in `GrixisFINALTXT60--2026.zip` and `GrixisFINAL60--2026.zip`  
**Normalized baseline hash:** `11f7ac19d46c1caae2e598307f78f5f00f2dc8885a57d9d87e19f44c646cb848`  
**Fresh restart final exact-TXT hash:** `449d7c02655713e05cc1051c8461dd36061ae1b85eaa9a8bef6595198b36dfc3`

## Disposition

**APPROVED / LOCKED — FRESH RESTART REVIEW PASSED.** The prior-cycle revision was not inherited as approval; its two swaps were reconsidered against the immutable baseline, current Oracle references and Crosis’s commander-first strategy. Both remain after fresh review. The list, tracker and cumulative change log are synchronized.

## Commander-first blueprint

- **Primary plan:** deal combat damage with Crosis, then optionally pay `{2}{B}` to choose a color and force the damaged player to reveal their hand and discard all cards of that color. Plan attacks and reserve activation mana.
- **Support plan:** evasive Specters create independent combat-damage discard/tempo triggers. Wheels and repeatable discard pressure deplete hands; Megrim, Liliana’s Caress, Waste Not, Geth’s Grimoire, Tinybones, Fell Specter and related payoffs convert resource loss into damage, cards, bodies or mana.
- **Control shell:** removal, counters and sweepers protect the pressure engine. Recoil is a synergy-weighted bounce answer, not hard removal.
- **Win routes:** attrition from repeated color-based discard and payoff triggers; flying combat pressure; incremental advantage from wheels and resource denial.
- **Essential functions retained:** 36 lands, fast mana, fixing, tutors, draw/wheels, permanent and stack interaction, evasion, discard payoffs and recursion.
- **Natural ceiling:** optimized high-power Grixis discard/control (Bracket 4). Fast mana, tutors, premium interaction and discard payoffs create pressure, but Crosis depends on combat connection and another `{2}{B}` payment; no deterministic infinite combo is relied upon.
- **What this deck should not become:** generic wheel-combo Grixis or creature-goodstuff detached from combat and hand disruption.

## Candidate and swap decisions

Sixteen commander-specific candidates were triaged. The October 12 ranking snapshot is discovery evidence, not a card-strength metric; current EDHREC Crosis discard data were consulted only as adoption context. Two additions were accepted, two existing cards retained, eleven candidates rejected, with both paired cuts logged.

1. **Add Blizzard Specter; cut Specter’s Shroud.** Blizzard Specter is a flying 2/3 Snow Specter whose combat-damage trigger chooses between discard or returning a permanent the damaged player controls to its owner’s hand. The bounce is tempo—not removal—and that player chooses the permanent. Shroud is cheaper and grants a discard trigger to an equipped creature, but costs both the equipment slot and equip investment. Fresh review prefers a self-contained evasive body and flexible trigger.
2. **Add Recoil; cut Chaos Warp.** Recoil returns any target permanent to its owner’s hand and then makes that player discard, combining interaction with Crosis’s core plan. A bounced permanent can be recast; Chaos Warp can shuffle a target away and may replace it with a random permanent. Bedevil, Feed the Swarm, Cyclonic Rift, Damnation, Toxic Deluge and other answers remain. This is a synergy-weighted trade, not universal removal superiority.

**Close alternatives rejected:** Guul Draz Specter and Abyssal Specter overlap existing Specters; Doomsday Specter has an entry tempo cost; Dimir Cutpurse needs to connect without native evasion; Urgoros is expensive and hits one player; Hypnotic Specter and Liliana’s Specter overlap current discard; Hollow Specter needs extra mana after combat; Needle Specter is fragile and lacks evasion; Sangromancer’s life gain is off-plan; Perplex does not justify a cut. Dream Salvage and The Raven Man stay because they are already present and reward opposing discards.

## Full-list audit

- Current Scryfall metadata refresh covers all **90 retained baseline names**. Blizzard Specter and Recoil were directly checked; Specter’s Shroud and Chaos Warp were rechecked.
- The matrix covers all **92 final distinct names**, with Oracle text, color identity, legality, functional role, commander-plan assessment and copy compliance.
- Final count: **100 copies including Crosis**, **92 distinct names**, **36 lands**. Only basics repeat: Island ×4, Mountain ×3, Swamp ×4. Commander is first and marked; TXT/CSV quantities match.
- All final cards fit UBR. Retained baseline names and both additions pass Commander legality; no project exception applies.
- Official Commander banned list reviewed 2026-10-13; no final-list card is banned.
- Crosis optional payment/color choice, Blizzard Specter’s choose-one trigger and player-selected bounce, and Recoil’s bounce-then-discard sequence were checked. No deterministic infinite combo is added or required.
- Exact hypergeometric probability of at least two lands in an opening seven with 36 lands in 100 cards is **79.26%**, before mulligan decisions. This does not establish keepability, color castability, sequencing or win rate.
- No qualified matched-seed multiplayer simulator or before/after sample was available. No performance superiority or win-rate claim is made.

## Evidence

- [EDHREC current Crosis discard page](https://edhrec.com/commanders/crosis-the-purger/discard)
- [Official Commander banned list](https://mtgcommander.net/index.php/banned-list/) — checkpoint reviewed 2026-10-13
- [Crosis, the Purger — Scryfall](https://scryfall.com/card/inv/242/crosis-the-purger)
- [Blizzard Specter — Scryfall](https://scryfall.com/card/ima/194/blizzard-specter)
- [Recoil — Scryfall](https://scryfall.com/card/dmr/197/recoil)
- [Specter’s Shroud — Scryfall](https://scryfall.com/card/dst/142/specters-shroud)
- [Chaos Warp — Scryfall](https://scryfall.com/card/cmm/243/chaos-warp)

## Artifacts

- Final list: `refinement/decklists/Crosis_the_Purger_Restart_2026-10-13.txt`
- Matching CSV: `refinement/decklists/Crosis_the_Purger_Restart_2026-10-13.csv`
- Full-list matrix: `refinement/reviews/Crosis_the_Purger_Full_List_Review_2026-10-13.csv`
- Candidate ledger: `refinement/decisions/Crosis_the_Purger_Restart_Candidate_Decisions_2026-10-13.csv`
- Change ledger: `refinement/changes/Crosis_the_Purger_Restart_Change_Ledger_2026-10-13.csv`
- Verification: `refinement/verification/Crosis_the_Purger_Restart_Verification_2026-10-13.md`
