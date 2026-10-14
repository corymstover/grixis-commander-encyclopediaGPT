# Admiral Beckett Brass — Restart Verification Certificate

**Deck:** #2 of 62  
**Review date:** 2026-10-13  
**Status:** APPROVED / LOCKED — FRESH RESTART REVIEW PASSED  
**Frozen baseline normalized-list SHA-256:** `eb73c86e728bbb07ef0d31e23c93f4048c5ca91771de0d28899407f6f11fd51d`  
**Final list path:** `refinement/decklists/Admiral_Beckett_Brass_Restart_2026-10-13.txt`  
**Final exact list SHA-256:** `af427fabb694276c5f72d1800d330f938642195fafec0b9894f5d948f9900f3d`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| Frozen baseline / CSV-TXT reconciliation | PASS | Baseline 100 copies, 97 unique names, 35 lands; source archive remains immutable. |
| Commander-first blueprint | PASS | Same-player three-Pirate combat-damage trigger, evasion, tribal scaling, Treasure/card draw, theft and protection documented. |
| Full-list review | PASS | Matrix covers all 97 baseline names plus three additions; three cuts and three additions recorded. |
| Candidate decisions | PASS | Candidate ledger records accepted/rejected alternatives beyond inherited shortlist; rankings are discovery signals only. |
| Current Oracle, identity and legality | PASS | Baseline names covered by current Scryfall refresh recorded in prior tracker/certificate; Open into Wonder and Admiral's Order directly checked. |
| Commander legality / exceptions | PASS | Official Commander ban-list checkpoint reviewed 2026-10-13; all final cards Commander-legal, no exception used. |
| Count / singleton / color identity | PASS | Independent recount below; all cards fit UBR. |
| Rules interactions | PASS | Admiral trigger timing, Roaming Throne, Open into Wonder, Admiral's Order raid, The Indomitable graveyard permission and mandatory draw checked. |
| Consistency / multiplayer test | PASS WITH LIMITS | Full role review and combat-trigger analysis complete; no qualified matched-start multiplayer simulator available. No win-rate claim. |
| Artifact / hash integrity | PASS | Final list, full-list matrix, candidate ledger, change ledger, review and certificate versioned separately; tracker cross-check recorded. |

## Independent structural verification

- Total copies including commander: **100/100**.
- Unique names: **97**.
- Commander first, exactly once, tagged `[Commander]`: PASS.
- Repeated names only: Island ×3, Mountain ×2, Swamp ×1.
- Singleton/copy rule: PASS.
- Land count: **35**, unchanged.
- Color identity: PASS; all final cards fit UBR.
- Project exceptions: none.
- Final exact list SHA-256: `af427fabb694276c5f72d1800d330f938642195fafec0b9894f5d948f9900f3d`.

## Auto-approval rationale

The changes improve the commander’s defining combat condition: The Indomitable adds a resilient recurring draw body, Open into Wonder can make three selected Pirates unblockable and draw cards on the decisive turn, and Admiral's Order can protect the attack for one blue mana after raid is active. Trade-offs—including mandatory draw risk, Open into Wonder's five-mana one-shot cost, and Admiral's Order's higher off-turn cost—are explicitly documented. All mandatory technical gates pass; auto-approve and lock this exact revision.
