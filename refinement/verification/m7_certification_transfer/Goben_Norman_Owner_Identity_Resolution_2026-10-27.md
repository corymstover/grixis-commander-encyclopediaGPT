# Owner resolution — Deck #43 Goben / Green Goblin (2026-10-27)

**Owner's explicit clarification:** “Goben IS Green Goblin, theyre the same CARD.”

This addresses the existing canonical registry/engineering-plan ID discrepancy. It does **not** unlock, replace, or rename an approved card or modify any of the original 62 deck IDs.

- Historical canonical registry key: `Goben__Gene_Splice_Savant`.
- Already owner-approved printed commander / first deck line: `1x Norman Osborn // Green Goblin [Commander]`.
- Exact approved raw source: `refinement/decklists/Norman_Osborn_Green_Goblin_M7_Rev1_Approved_2026-10-26.txt`.
- Owner approval receipt: `refinement/approvals/Norman_Osborn_Green_Goblin_M7_Rev1_Approved_2026-10-26.md`.
- Exact locked SHA-256: `c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9`.
- Original frozen 61-deck engineering test-plan identity: `Norman_Osborn_Green_Goblin`, plan blob SHA `24c7b78a1548c7f0c9cf40931d06b13286cf0f6c`.
- Original required case inventory: P0 `C1`, `K1`, `K2`, `K3`, `F1`; P1 `K4`–`K7`, `E1`–`E2`, `W1`–`W3`, `F2`–`F3`.

The two pinned October 24 manifests remain **byte-for-byte unchanged**, as do all 62 approved raw decklist bytes and SHA registry values. In the verifier, only the specified canonical registry key and current exact approved SHA may map to the Norman plan key. It additionally checks the printed commander line and the existing matching approval receipt. A future Goben or Norman cardlist revision must be explicitly certified at its own exact SHA; this alias cannot bypass a new review.

The original M6 cases were design-only and did not constitute an executed Phase B. Engineering source-bound P0 checks were newly implemented for the actual approved Norman 100; P1 cases remain separately deferred if untested. Neither this identity decision nor the finite tests constitutes complete multiplayer simulation or independent milestone acceptance.
