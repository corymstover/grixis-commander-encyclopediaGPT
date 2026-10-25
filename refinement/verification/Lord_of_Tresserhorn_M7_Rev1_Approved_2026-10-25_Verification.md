# Deck #29 Lord of Tresserhorn M7 Rev1 — source-bound verification and canonical lock receipt

**Exact owner-approved source SHA-256:** `fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85`.
**Historical Oct14 SHA-256 preserved:** `95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`.
**Date:** 2026-10-25 America/Chicago.

## Exact source and mechanics
- [PASS] 100 physical / 98 distinct / one 1x commander / only 3x Swamp repeated / 35 land faces / five one-for-one swaps.
- [PASS] Exactly the five adds and cuts listed in `refinement/approvals/Lord_of_Tresserhorn_M7_Rev1_Approved_2026-10-25.md`; older Oct14 source remains unchanged.
- [PASS] All 98 selected names matched the Oct23 live Scryfall 325-name snapshot, Commander-legal and within UBR; no project exception. Source printing may include future-dated reprints of previously legal cards; a fresh 98-name Oct25 query is not claimed.
- [PASS] Three Game Changers (Demonic Tutor / Fierce Guardianship / Vampiric Tutor), Bracket 4 Optimized, tags Infect / Voltron / Aristocrats.
- [PASS] 14 exact approved list finite P0/P1 fixtures source-bound to full SHA and snapshot: C1, K1, K2, K3, F1 (P0) and K4, K5, E1, E2, W1, W2, W3, F2, F3 (P1). Research engineering PR #707 head `0d4c51d2c5756a0c6207fe4b5d47d4e8afdd0920`; CI https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40180490523. Existing Lord source/rules focused workflow https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40180490450.
- [PASS] Card interactions include actual Lord trigger/costs, regeneration versus sacrifice, suppressed ETB, Consign target, Uncaged Fury 22 combat damage, infect/Kediss noncombat spread, Gravecrawler prerequisite, BMC life, Skullclamp and owner-flagged interaction loss.

## Verification scope
Research goldfish and finite scripted rules conditions do **not** constitute multiplayer win rates, comprehensive Magic game-engine proof, mathematical optimality or independent third-model review. Historical Pass C owner-equivalent waiver remains explicitly non-independent. The original Oct14 list's complete gate is historical for that old SHA, not mistakenly transferred to this new M7 list. Canonical source, state, tracker and 61 other deck locks must remain consistent after merge.
