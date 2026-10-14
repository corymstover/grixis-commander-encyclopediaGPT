# Ashnod the Uncaring — Restart Verification Certificate

**Deck:** #6 of 62  
**Review date:** 2026-10-13  
**Status:** APPROVED / LOCKED — FRESH RESTART REVIEW PASSED  
**Frozen baseline normalized-list SHA-256:** `6548ec58378b54ed366a34330e05d166147bd38828ffd1030b7f59f21d2bb91d`  
**Final list path:** `refinement/decklists/Ashnod_the_Uncaring_Restart_2026-10-13.txt`  
**Final exact-list SHA-256:** `25a17a39c0428e040a9b1014f853aec0c71ae785a53834ddcae229abe3699b01`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| Baseline provenance / CSV-TXT reconciliation | PASS | Frozen baseline 100 copies, 95 unique names, 33 lands; source archives preserved. |
| Commander-first blueprint | PASS | Activated abilities with sacrifice costs, artifact-token production, recursion, sacrifice payoffs and copy effects reviewed. |
| Full-list review | PASS | Matrix covers all 95 baseline names plus five additions; five cuts and five additions recorded. |
| Candidate decisions | PASS | 30+ commander-specific alternatives screened; rankings used as discovery leads only. |
| Oracle / identity / legality | PASS | Current Scryfall refresh for baseline; Weapons Manufacturing checked in current project card audit; new cards reviewed for Oracle text, color identity and Commander legality. |
| Official Commander legality / exceptions | PASS | Official ban-list checkpoint reviewed 2026-10-13; no final-list card banned, no exception used. |
| Count / singleton / identity | PASS | Independent recount below; all final cards fit UBR. |
| Rules interactions | PASS | Ashnod trigger/copy timing, nonmana restriction, Legion Extruder copy, Munitions tokens, Burnished Hart four-land line and existing sacrifice engines reviewed. |
| Consistency / multiplayer test | PASS WITH LIMITS | Structural and role review; no qualified matched-start multiplayer simulator, no win-rate claim. |
| Artifact/hash integrity | PASS | Final list, matrix, candidate ledger, change ledger, review and certificate separately versioned and tracker cross-checked. |

## Independent structural verification

- Total copies including commander: **100/100**.
- Unique names: **95**.
- Commander first, exactly once, tagged `[Commander]`: PASS.
- Repeated names only: Island ×3, Mountain ×2, Swamp ×3.
- Singleton/copy rule: PASS.
- Land count: **33**, unchanged.
- Color identity: PASS; all final cards fit UBR.
- Project exceptions: none.
- Final exact-list SHA-256: `25a17a39c0428e040a9b1014f853aec0c71ae785a53834ddcae229abe3699b01`.

## Auto-approval rationale

The fresh review retains Oni-Cult Anvil and Stormclaw Rager because both convert sacrifice costs into copied activated-ability value. Legion Extruder adds repeatable damage and creature fodder; Weapons Manufacturing turns the deck's nontoken artifact entries into Munitions tokens that deal damage when they leave; Burnished Hart turns one activation into four basic lands through Ashnod's copy. The trade-offs—loss of Farid's Junk engine, Pyrite Spellbomb's cheap flexible effect and Wayfarer's Bauble's lower-cost ramp—are recorded. All mandatory gates pass; auto-approve and lock this exact list.
