# Cult of Skaro — New-Cycle Refinement & Verification Certificate

Date: 2026-10-13

## Final decision

**APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.**

- Add: Ashad, the Lone Cyberman; Death in Heaven. Cut: Canoptek Spyder; Adaptive Omnitool.
- Final list: 100 copies, 94 distinct names, 34 land copies; singleton compliance verified. Commander first.
- Revised TXT SHA-256: `292529f5c97400f523205c1a2c5d66544c39e2acaf0dcf02865a224521b81930`.
- Baseline raw CSV SHA-256: `0cc00cc4f4e142091c665dfd5d52bcfc69f40c9ee61bdbbedde2cb8f4509684d`.
- Baseline raw TXT SHA-256: `ac43453f74d7bd712355c48ffc87dd7bceaa473e043435bf69c81c5388661645`.
- Normalized baseline hash: `12ce6043e1319a8f063b95faa11f6eca96502904e7961aeadddd14c28b26486d`.

## Commander-first plan and change rationale

Cult of Skaro triggers whenever it attacks, choosing one of four modes at random: put a +1/+1 counter on each artifact creature, draw two cards, create a 3/3 black Dalek artifact creature token with menace, or have each opponent lose 4 life. The deck remains artifact creature/copy/token focused, with Cybermen and Daleks as its identity.

Ashad, the Lone Cyberman is a four-mana legendary artifact creature that gives the first nonlegendary artifact spell cast each turn casualty 2. As that spell is cast, a creature with power 2 or greater may be sacrificed; paying casualty copies the spell, and an artifact spell copy becomes a token. Cult of Skaro’s Daleks, Thopters and face-down Cybermen can provide expendable bodies. Ashad also grows when another creature is sacrificed.

Death in Heaven is a four-mana Saga. Chapters I and II make a target player mill two cards and then exile their graveyard. Chapter III puts all creature cards exiled with the Saga onto the battlefield face down under your control as 2/2 Cyberman artifact creatures. It is a direct token-generation engine, but its output depends on creature cards in the target graveyard and takes time to reach chapter III.

Canoptek Spyder is cut because its draw trigger requires another nontoken artifact creature or Vehicle to enter and it costs five mana; token entries do not trigger it. Adaptive Omnitool is cut as a three-mana equipment requiring an equip investment; the list retains extensive artifact draw and anthem effects.

Direct current Oracle / legality references: [Ashad, the Lone Cyberman](https://mtg.wtf/card/who/113/Ashad-the-Lone-Cyberman), [Death in Heaven](https://mtg.wtf/card/who/66/Death-in-Heaven), [Canoptek Spyder](https://mtg.wtf/card/40k/151/Canoptek-Spyder), [Adaptive Omnitool](https://scryfall.com/search?q=Adaptive+Omnitool), [Cult of Skaro](https://mtg.wtf/card/who/404/Cult-of-Skaro). All are Commander-legal; final list fits UBR. Official Commander banned list checked 2026-10-13; no project exception applies.

## Structural and metadata checks

- TXT: 94 lines with quantities, commander first; quantity total 100.
- CSV: 94 rows, quantity sum 100, unique names 94.
- Current project-wide Scryfall metadata refresh generated 2026-10-13T07:03:26.694525Z from bulk updated 2026-10-12T21:06:24.577Z reported 5,964/5,964 exact printing/name matches; final names reconcile against that refresh. Additions and cuts directly checked.
- Candidate triage: 16 candidates; 2 accepted, 4 retained, 1 cut, 9 rejected.
- Strategy review covers artifact-spell copying, token production, artifact creature density, draw, ramp, removal and land count. No numerical goldfish or matched-seed multiplayer test; no win-rate claim.

## Final gate

All mandatory technical gates pass. Lock the revised list; frozen baseline exports remain immutable.
