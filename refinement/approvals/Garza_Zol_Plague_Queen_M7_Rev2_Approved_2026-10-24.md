# Garza Zol, Plague Queen M7 Rev2 — Cory exact owner approval receipt

Date: **2026-10-24** (America/Chicago), primary owner: **Cory Stover**, cycle global-restart-2026-10-13, tracker Deck #20 (index 19), registry Garza_Zol__Plague_Queen.

**APPROVED AND AUTHORIZED FOR CANONICAL LOCKING** only this complete 100-card raw SHA-256: **353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244**.

## Source and authorization

Cory saw the full 100-line Archidekt-ready Garza M7 Rev2 list; seven explicit replacement pairs, each benefit and opportunity cost; exactly 38 land faces, all 11 original rocks, 20 Equipment, nine Game Changers, Bracket 4 — Optimized and tags Voltron / Commander Damage / Deathtouch-Control; and [independent engineering PR #695](https://github.com/corymstover/GrokBotMTGCompanion/pull/695) with its exact-head [Actions SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40070632545).

Cory then explicitly stated on 2026-10-24: "I explicitly approve Garza Zol, Plague Queen M7 Rev2, the exact 100-card candidate with raw SHA-256 353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244. Proceed with canonical verification, approval PR, exact-head checks, merge, post-merge locking, and then Deck #21 Goro-Goro and Satoru."

- Engineering source candidate at PR #695 exact head d816097a24a4d302f50222457e6c0b21f79579e5; the source was re-fetched and separately re-hashed with sha256sum before canonical construction.
- NEW exact approved canonical file: refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt, raw **353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244**.
- Immutable original Oct14 historical source: refinement/decklists/Garza_Zol_Plague_Queen_Approved_2026-10-14.txt, raw **32c0e8049a9c8a5d238048b4f774f0457908d724f23d4597b7da93a6cba0c16f**. This is preserved, not deleted, rewritten, or retroactively disapproved.
- Grok first-pass [PR #668](https://github.com/corymstover/GrokBotMTGCompanion/pull/668) remained RESEARCH_ONLY four swaps, and was not treated as independent approval or blindly merged. PR #695 independently found and source-bound seven changes.

## Exactly seven approved substitutions

| Addition | Cut | Commander-specific case | Material opportunity cost |
|---|---|---|---|
| Lizard Blades | Scythe of the Wretched | Permanent double strike repeats Garza's combat damage and draw triggers, Kediss, poison and equipment procs; avoids Scythe attaching to a resurrected victim | Give up opponent creature theft/reanimation and +2/+2 |
| Two-Handed Axe // Sweeping Cleave | Inquisitor's Flail | Attack trigger doubles Garza's power, including later Garza-sourced noncombat damage, and red Adventure supplies double strike | +1 cast mana, colored equip cost, no pre-attack damage doubling |
| Conqueror's Flail | Robe of the Archmagi | +3/+3 from Garza's three colors and prevents opponent spells on our own turn while attached | Lose damage-scaled refill; equip can be responded to |
| Giantfall | Rapid Hybridization | Garza-sourced creature damage that can grow her with deathtouch and alternate artifact removal | Lose one-mana independent removal, including for indestructible |
| Seize the Day | Sheoldred's Edict | Flashback extra combat multiplies Garza attack triggers and Axe power doubling | Lose sacrifice-answer for hexproof, indestructible, planeswalkers; target failure risk |
| Temur Battle Rage | Psychotic Fury | Double strike plus trample at Garza's natural power 5 | Lose cantrip and multicolor-specific targeting; Rage can be redundant with Lizard |
| Malakir Rebirth // Malakir Mire | Takenuma, Abandoned Mire | {B} commander death protection can avoid tax if Garza stays in graveyard | Mire always enters tapped; no channel recursion; Garza returns tapped unequipped and without old counters |

## Canonical source-bound checks

- Exactly one Garza commander and 99 library; exactly 100 singleton names; final LF and raw SHA bound.
- Color identity UBR, Commander legality under documented Oct23 Scryfall Oracle plus three individually checked published Scryfall/Gatherer entries; no project exception.
- 38 land faces (one always-tapped black MDFC); all eleven early rocks and Exotic Orchard preserved. Grok's 0.4724 turn-six commander castability proxy is not a measured new-list outcome and does not account for the new tapped land. No statistical win rates.
- Nine Game Changers; no forced generic cEDH combo. Power Bracket 4 Optimized; three tags as above.
- Final verification manifest: refinement/verification/Garza_Zol_Plague_Queen_M7_Rev2_Scryfall_Selected_2026-10-23.json. That contains 97 archived API-origin rows and three explicitly manually source-checked published entries without invented oracle IDs. It is **not** represented as a fresh 100-card live Oct24 API pull.
- New dedicated approval unittest and exact-head Actions workflow must pass. Regression rehash of all prior 19 newly M7-locked lists required before canonical merge.
- No M6.10, overall M7 or M8 milestone acceptance inferred by this single-deck approval.

## Release protocol

The owner has approved the exact candidate but this receipt **does not pre-claim** canonical PR merge or post-merge locking. Exact PR head must pass checks; merge requires expected-head lease; re-fetch main afterwards and confirm digest, registry APPROVED/LOCKED and full prior-19 regression, then move to Deck #21.
