# Don Andres, the Renegade — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Add: Decadent Dragon // Expensive Taste; Thieving Varmint. Cut: Thief of Sanity; Dire Fleet Daredevil.
- Final list: 100 copies, 99 distinct names, 35 land copies; singleton compliance verified. Commander first.
- Revised TXT SHA-256: `d76c35bf691d4082f4dec1d79a43634dc77ae47c1b648ddf03488219e93cc779`.
- Baseline raw CSV SHA-256: `2e052e06c3157297a99d3cd34bf884db07051c25af7b5cfa868bc710c8dd95af`.
- Baseline raw TXT SHA-256: `5013e0b0b035880e74f5395e55115a58eb3f60ad922cd4bd29670d5f45d0ed2e`.
- Normalized baseline hash: `0a2a36c0d4597e0b327325ccc51d775f1aa23169c5dd9f6e735d094c06090d0d`.

## Commander-first plan and change rationale

Don Andres gives creatures you control but do not own +2/+2, menace, deathtouch and the Pirate type. Whenever you cast a noncreature spell you do not own, he creates two tapped Treasures. The deck remains centered on opponent-library/graveyard theft, theft-based combat, Pirates, and Treasure conversion.

Decadent Dragon is a four-mana 4/4 with flying and trample; when it attacks it creates a Treasure. Its Expensive Taste adventure costs {2}{B}, exiles the top two cards of an opponent’s library face down, and lets you look at and play those cards while they remain exiled. The adventure itself is owned by you, so it does not trigger Don Andres; casting a noncreature spell from the opponent-owned exiled cards does trigger him.

Thieving Varmint is a two-mana 2/1 with deathtouch and lifelink. Its tap-and-pay-1-life ability adds two mana of any one color, restricted to casting spells you do not own. This is directly aligned with the deck’s main plan. Thief of Sanity is cut for the stronger body plus adventure/Treasure package; Dire Fleet Daredevil is cut for repeatable stolen-spell ramp, with the loss of a one-shot graveyard spell effect documented.

Direct current Oracle / legality references: [Decadent Dragon](https://mtg.wtf/card/pwoe/223sa/Decadent-Dragon), [Thieving Varmint](https://mtg.wtf/card/otc/59/Thieving-Varmint), [Thief of Sanity](https://mtg.wtf/card/grn/205/Thief-of-Sanity), [Dire Fleet Daredevil](https://mtg.wtf/card/rix/99/Dire-Fleet-Daredevil), [Don Andres](https://mtg.wtf/card/lcc/28/Don-Andres-the-Renegade). All are Commander-legal; all final card identities fit UBR. Official Commander banned list checked 2026-10-13; no project exception applies.

## Structural and metadata checks

- TXT: 99 lines with quantities, commander first; quantity total 100.
- CSV: 99 rows, quantity sum 100, unique names 99.
- Current project-wide Scryfall metadata refresh generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z reported 5,964/5,964 exact printing/name matches; final names reconcile against that refresh. The two accepted cards and their paired cuts directly checked.
- Candidate triage: 16 candidates; 2 accepted, 5 retained, 9 rejected with reasons.
- Strategy review covers theft effects, Treasure production, Pirate density, ramp, interaction, draw, and land count. No numerical goldfish or matched-seed multiplayer test; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock the revised list; frozen baseline exports remain immutable.
