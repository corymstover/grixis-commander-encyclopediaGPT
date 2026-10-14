# Anhelo, the Painter — Restart Verification Certificate

**Deck:** #4 of 62  
**Review date:** 2026-10-13  
**Status:** APPROVED / LOCKED — FRESH RESTART REVIEW PASSED  
**Frozen baseline normalized-list SHA-256:** `7ae557bb81a2d9d3596061c3aff8a2efa4cf3f244e628ba0f9dc50c28aaa8c5f`  
**Final list path:** `refinement/decklists/Anhelo_the_Painter_Restart_2026-10-13.txt`  
**Final exact list SHA-256:** `7836e65849bd7e4847f452f016c2204b47289bd6fb86a08edbd53e9741c9c87b`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| Baseline provenance and CSV/TXT reconciliation | PASS | Frozen source baseline is 100 copies / 94 unique names / 34 lands; source files remain immutable. |
| Commander-first blueprint | PASS | Casualty 2 on the first instant/sorcery cast each turn; copy/magecraft engines, power-2 fodder, graveyard setup and finishers reviewed. |
| Full-list review | PASS | Matrix covers all 94 baseline names plus five additions; five cuts and five additions recorded. |
| Candidate decisions | PASS | 30+ commander-specific candidates screened; inherited ranks used as discovery leads only. |
| Oracle / color identity / legality | PASS | Current Scryfall refresh for baseline; direct checks for Dogged Detective, Startle, Waste Management, Deekah and Make an Example. |
| Official Commander legality / exceptions | PASS | Official ban list checkpoint reviewed 2026-10-13; no final-list card banned, no project exception used. |
| Count / singleton / identity | PASS | Independent recount below; all cards fit UBR. |
| Rules interactions | PASS | Casualty costs, Dogged Detective return trigger, Startle copies/tokens, Waste Management kicker-copy ruling, Deekah magecraft and Make an Example copied resolution checked. |
| Consistency/performance | PASS WITH LIMITS | Exact hypergeometric draw-density analysis; no qualified matched-start multiplayer simulator, no win-rate claim. |
| Artifact/hash integrity | PASS | Final list, review matrix, candidate ledger, change ledger, review and certificate separately versioned and tracker cross-checked. |

## Independent structural verification

- Total copies including commander: **100/100**.
- Unique names: **94**.
- Commander first, exactly once, tagged `[Commander]`: PASS.
- Repeated names only: Island ×3, Mountain ×3, Swamp ×3.
- Singleton/copy rule: PASS.
- Land count: **34**, unchanged.
- Color identity: PASS; all cards fit UBR.
- Project exceptions: none.
- Final exact list SHA-256: `7836e65849bd7e4847f452f016c2204b47289bd6fb86a08edbd53e9741c9c87b`.

## Auto-approval rationale

The fresh revision retains Deekah and Make an Example after re-evaluating their direct interaction with Anhelo's cast/copy and casualty plan. It adds Dogged Detective for power-2 fodder and graveyard setup, Startle for copied card draw plus Zombie fodder, and Waste Management for scalable copied graveyard hate and Rogue token production. The lost flexible modes from Maestros Charm, the recurring token engine from Ghoulish Procession, and Preordain's one-mana scry are documented trade-offs. All mandatory gates pass; auto-approve and lock this exact list.
