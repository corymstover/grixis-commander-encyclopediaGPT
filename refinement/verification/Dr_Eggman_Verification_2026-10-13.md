# Dr. Eggman — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Add: Ruin Grinder. Cut: Megrim.
- Final list: 100 copies, 97 distinct names, 31 lands; repeated basics are intentional. Commander first.
- Revised TXT SHA-256: `5efe92126b9919edd8c798938be9e03af397d3af94627b372d3fdec420c5fe4c`.
- Baseline raw CSV SHA-256: `e4bc5c40451b258d57648233f0d296f05272ee5a40b6644da52055808416dd50`.
- Baseline raw TXT SHA-256: `35406415bee72bd3b92e7639314bcdd1e2404d2cf713e103e8c20c2f27eea607`.
- Normalized baseline-name SHA-256: `ce05fbe109f514f9e6b907448397e32b80bd40dfedaaaee9a3f382828b7ad2ec`.

## Commander-first plan and change rationale

Dr. Eggman draws at each end step and makes opponents choose between discarding a card or allowing the controller to put a Construct, Robot, or Vehicle from hand onto the battlefield. The list remains an artifact/Robot/Vehicle engine with a secondary discard package. Ruin Grinder is a Construct and a 7/4 menace artifact creature. When it dies, each player may discard their hand and draw seven; the effect supports Waste Not, Geth’s Grimoire and Liliana’s Caress, but may also refill opponents, so timing matters.

Megrim and Liliana’s Caress both deal 2 damage per card an opponent discards; Megrim costs {2}{B} while Caress costs {1}{B}. Cutting the less mana-efficient duplicate preserves a discard damage payoff while adding an artifact creature and wheel engine.

Direct current Oracle / legality references: [Ruin Grinder](https://mtg.wtf/card/fic/297/Ruin-Grinder), [Megrim](https://mtg.wtf/card/m10/104/Megrim), [Dr. Eggman](https://mtg.wtf/card/sld/2084/Dr-Eggman). All are Commander-legal; all final cards fit UBR. Official Commander ban list checked 2026-10-13; no project exception applies.

## Structural and metadata checks

- TXT: 100 lines, one copy per line, commander first.
- CSV: 100 rows, quantity sum 100, 100 unique names.
- Current project-wide Scryfall metadata report generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z reported 5,964/5,964 exact printing/name matches; current list names reconcile against that refresh. Ruin Grinder and Megrim directly checked against current Oracle and legality references.
- Candidate review: 16 candidates; 1 accepted, 5 already-included cards retained, 10 rejected with reasons.
- Strategy and consistency review: discard payoff density, artifact/Construct/Robot/Vehicle count, removal, draw, ramp and high-mana threats reviewed. No matched-seed multiplayer test or numerical goldfish was run; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock the revised list; frozen baseline exports remain immutable.
