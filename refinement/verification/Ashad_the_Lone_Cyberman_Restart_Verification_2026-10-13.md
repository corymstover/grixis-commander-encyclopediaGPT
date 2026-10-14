# Ashad, the Lone Cyberman — Restart Verification Certificate

**Deck:** #5 of 62  
**Review date:** 2026-10-13  
**Status:** APPROVED / LOCKED — FRESH RESTART REVIEW PASSED  
**Frozen baseline normalized-list SHA-256:** `7d2f6231a8eeba1513b69a955001aac540337ab6ef674d5807e37766e69ef53b`  
**Final list path:** `refinement/decklists/Ashad_the_Lone_Cyberman_Restart_2026-10-13.txt`  
**Final exact-list SHA-256:** `3c53a84348f479371facae9ae6829c5389dc5cc2c700a33456e98b23e1950f1f`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| Baseline provenance / CSV-TXT reconciliation | PASS | Frozen baseline 100 copies, 95 unique names, 30 lands; source archives preserved. |
| Commander-first blueprint | PASS | First nonlegendary artifact spell each turn gets casualty 2; artifact copy, sacrifice payoffs and recursion reviewed. |
| Full-list review | PASS | Matrix covers all 95 baseline names plus four additions; four cuts and four additions recorded. |
| Candidate decisions | PASS | 30+ commander-specific alternatives screened; ranks used as discovery leads, not mandates. |
| Oracle / identity / legality | PASS | Current Scryfall refresh for baseline; direct checks for Canoptek Spyder, Cryptothrall and Technomancer. |
| Official Commander legality / exceptions | PASS | Official ban list checkpoint reviewed 2026-10-13; no final-list card banned, no exception used. |
| Count / singleton / identity | PASS | Independent recount below; all cards fit UBR. |
| Rules interactions | PASS | Casualty timing, copied artifact spell resolution, Cryptothrall hexproof, Canoptek Spyder draw condition, Technomancer ETBs and Ultron trigger bounded. |
| Consistency / multiplayer test | PASS WITH LIMITS | Structural, curve and role review; no qualified matched-start multiplayer simulator, no win-rate claim. |
| Artifact/hash integrity | PASS | Final list, matrix, candidate ledger, change ledger, review and certificate stored separately and tracker cross-checked. |

## Independent structural verification

- Total copies including commander: **100/100**.
- Unique names: **95**.
- Commander first, exactly once, tagged `[Commander]`: PASS.
- Repeated names only: Island ×3, Mountain ×2, Swamp ×3.
- Singleton/copy rule: PASS.
- Land count: **30**, unchanged.
- Color identity: PASS; all final cards fit UBR.
- Project exceptions: none.
- Final exact-list SHA-256: `3c53a84348f479371facae9ae6829c5389dc5cc2c700a33456e98b23e1950f1f`.

## Auto-approval rationale

Ultron remains from the previous pass because it is a repeatable artifact-copy engine. Canoptek Spyder adds draw from future nontoken artifact-creature entries and is a casualty-copy target. Cryptothrall protects the artifact-creature board and can be copied to create overlapping hexproof coverage. Technomancer adds a high-ceiling artifact recursion ETB that can resolve twice when copied by Ashad. The cost is a higher curve and the loss of a rock, an instant/sorcery copy multiplier and a slow token/draw enchantment. The deck's artifact cost reducers and existing token/draw engines support this trade-off. All mandatory gates pass; auto-approve and lock this exact list.
