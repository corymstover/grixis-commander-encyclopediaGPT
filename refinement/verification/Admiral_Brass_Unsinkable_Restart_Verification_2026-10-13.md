# Admiral Brass, Unsinkable — Restart Verification Certificate

**Deck:** #3 of 62  
**Review date:** 2026-10-13  
**Status:** APPROVED / LOCKED — FRESH RESTART REVIEW PASSED  
**Frozen baseline normalized-list SHA-256:** `59dd38f44624572817cfb562a92debbb177a0ca4ddfe84405a1f2f3d41d0f570`  
**Final list path:** `refinement/decklists/Admiral_Brass_Unsinkable_Restart_2026-10-13.txt`  
**Final exact list SHA-256:** `a0ded044af9998345769af6ba1cf908c1ed4b46418df598ce6288e8b3f5aa942`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| Frozen baseline / CSV-TXT reconciliation | PASS | Baseline 100 copies, 97 unique names, 34 lands; source archive remains immutable. |
| Commander-first blueprint | PASS | Mill-four, beginning-combat Pirate reanimation with finality counter, 4/4 base stats and haste; counter mitigation and high-impact ETB targets documented. |
| Full-list review | PASS | Matrix covers all 97 baseline names plus five additions; five cuts and five additions recorded. |
| Candidate decisions | PASS | 30+ commander-specific candidates and comparisons reviewed; rankings are discovery signals only. |
| Current Oracle, identity and legality | PASS | Baseline names covered by current Scryfall refresh; new candidates directly checked against current references. |
| Commander legality / exceptions | PASS | Official Commander ban-list checkpoint reviewed 2026-10-13; all final cards legal, no exception used. |
| Count / singleton / color identity | PASS | Independent recount below; all cards fit UBR. |
| Rules interactions | PASS | Finality-counter removal/transfer, Roaming Throne double triggers, Dire Fleet Ravager repeated life loss, Skeleton Crew triggers, Timestream Navigator and Kitesail Larcenist checked. |
| Consistency / multiplayer test | PASS WITH LIMITS | Independent count, role review and prior hypergeometric density calculations; no qualified matched-start multiplayer simulator. No win-rate claim. |
| Artifact / hash integrity | PASS | Final list, matrix, candidate ledger, change ledger, review and certificate versioned separately; tracker cross-check recorded. |

## Independent structural verification

- Total copies including commander: **100/100**.
- Unique names: **97**.
- Commander first, exactly once, tagged `[Commander]`: PASS.
- Repeated names only: Island ×2, Mountain ×2, Swamp ×2.
- Singleton/copy rule: PASS.
- Land count: **34**, unchanged.
- Color identity: PASS; all final cards fit UBR.
- Project exceptions: none.
- Final exact list SHA-256: `a0ded044af9998345769af6ba1cf908c1ed4b46418df598ce6288e8b3f5aa942`.

## Auto-approval rationale

Power Conduit and Nesting Grounds preserve the repeatable finality-counter engine; Kitesail Larcenist adds efficient multi-permanent disruption; Timestream Navigator creates a high-impact extra-turn line from a hasty reanimation when City's Blessing and four mana are available; Dire Fleet Ravager adds an ETB life-loss payoff that Roaming Throne can double. Trade-offs are explicitly recorded, including symmetric life loss, extra-turn setup/cost, and losing the prior draw vehicle/damage doubler. All mandatory correctness gates pass; auto-approve and lock this exact revision.
