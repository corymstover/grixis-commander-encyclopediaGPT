# Deck #28 Loki M7 Rev1 — independent verification and canonical lock receipt

**Approved raw SHA-256:** `919734ad1f60e56a636561815d319ec1eb0fbd0c233265ad5e85064f589c7185`.

**Historical October 14 raw SHA-256, preserved:** `5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062`.

Date: 2026-10-25. Source file: `refinement/decklists/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25.txt`. Owner approval: `refinement/approvals/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25.md`.

## Exact-source findings

- [PASS] 100 physical cards including one Loki commander, 99 noncommander physical library cards, 95 distinct names, only basic Island x3 / Mountain x2 / Swamp x3 repeat.
- [PASS] Seven additions and seven cuts exactly as owner-approved; historical 2026-10-14 source not overwritten; 34 lands retained.
- [PASS] 95 of 95 names matched archived current Oracle from live Scryfall on 2026-10-23, all Commander-legal and color identity within UBR; all seven added card names have released printings as of October 25. Named Commander bans and project exception checkpoint: no exceptions.
- [PASS] Five Game Changers: Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will and Rhystic Study. Natural power ceiling Bracket 4 — Optimized; tags Villain Copies, Combat Value, Connive.
- [PASS] Independent whole-99 strategic ledger and red-team, early MV≤3 Villain targets 10→12, repeatable ETB interaction and combat draw, retained Cowl/Killmonger, clone timing and preservation constraints.
- [PASS] Engineering head `b316ce65c6355523c32169454ed51d4211d07ea0` contains source-bound independent full-list tests and the new 13-case exact candidate M6 fixtures. [Whole-99 success #40178847260](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40178847260) and [13-case success #40178847336](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40178847336) ran against this exact head.
- [PASS] All five mandatory P0 cases (C1, K1, K2, K3, F1) and all eight P1 cases (K4, K5, E1, E2, W1, W2, F2, F3) have explicit payable scenarios, positive and adversarial assertions, selected Oracle source, real exact-head CI run URL and SHA scope in `refinement/verification/m7_certification_transfer/Loki__the_Deceiver_919734ad1f60e56a.json`.
- [PASS] Source-binding and state/tracker exact SHA agreement are protected by canonical owner-lock tests. Historical frozen approval hashes and 61 non-Loki locks preserved.

## Limits, transparent costs, and source qualifiers

These finite rule/state fixtures are **not** a full Magic rules engine, do **not** establish empirical multiplayer win rates and are **not** a mathematical proof that no other upgrades exist. No research-pipeline or Colab run was performed to lock this approval. The Scryfall snapshot is current as of October 23, with 95 selected Oracle objects extracted from its larger 450-name collection; some objects refer to future reprints of already Commander-legal names. Full seven cut tradeoffs and exact timestamps are preserved in the review and owner receipt. Original October14 complete-gate artifact remains a historical gate for that older SHA; the M7 case mapping above supports only this exact revision.
