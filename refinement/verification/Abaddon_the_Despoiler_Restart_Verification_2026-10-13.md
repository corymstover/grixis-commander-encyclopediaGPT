# Abaddon the Despoiler — Restart Verification Certificate

**Deck:** #1 of 62  
**Review date:** 2026-10-13  
**Status:** APPROVED / LOCKED — FRESH RESTART REVIEW PASSED  
**Frozen baseline normalized SHA-256:** `a58b6ad5499596eb64af79a83b210641e4e097c79803de87cca3ba2244fab91f`  
**Final decklist:** `refinement/decklists/Abaddon_the_Despoiler_Restart_2026-10-13.txt`  
**Final exact list SHA-256 (UTF-8, LF, trailing newline):** `fd66ea20135a77322113f69cd6ac583fde381a1af08ffac348c9f1f4d8227e15`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| Frozen baseline/export reconciliation | PASS | Authoritative Abaddon CSV/TXT: 100 copies, 94 unique names; frozen sources unchanged. |
| Commander-first blueprint | PASS | Threshold-cascade, early life-loss setup, exile payoffs, token engine, and Breach backup documented. |
| Full-list card review | PASS | Matrix covers all 94 baseline unique names plus three additions; 3 additions and 3 cuts recorded. |
| Candidate decisions | PASS | Accepted/rejected alternatives documented; rankings are discovery leads only. |
| Current Oracle, identity and rules | PASS | Existing names covered by the 2026-10-13 Scryfall refresh noted in the prior tracker record; new candidates directly checked. Ancient Cellarspawn text discrepancy corrected. |
| Commander legality and exceptions | PASS | Protection Racket, Ancient Cellarspawn and Aurora Phoenix are Commander-legal; official ban-list checkpoint reviewed 2026-10-13. No exception used. |
| Count/singleton/color identity | PASS | Independent count below; all final cards fit UBR. |
| Rules and combo functionality | PASS | Abaddon threshold, Protection Racket choice, Cellarspawn trigger, Aurora Phoenix recursion, Bloodletter replacement effect, and Breach/LED/Brain Freeze constraints checked. |
| Consistency / multiplayer test | PASS WITH LIMITS | Role and engine-density review complete; no qualified matched-start multiplayer simulator. No win-rate claim. Prior six-game Aurora Phoenix/Mind's Desire comparison is inconclusive and not used. |
| Artifact/hash integrity | PASS | Final list, full-list matrix, candidate ledger, change ledger, review report and this certificate are separate dated artifacts; tracker cross-check follows writes. |

## Independent structural verification

- Total cards including commander: **100/100**.
- Unique names: **94**.
- Commander first, exactly once, tagged `[Commander]`: **PASS**.
- Repeats: Island ×3, Mountain ×3, Swamp ×3 only.
- Singleton/copy rule: **PASS**.
- Lands: **34**.
- Color identity: **PASS**; Protection Racket and Ancient Cellarspawn are black, Aurora Phoenix red, all within UBR.
- Project exceptions: none.
- Final hash: `fd66ea20135a77322113f69cd6ac583fde381a1af08ffac348c9f1f4d8227e15`.

## Auto-approval decision

The three swaps improve Abaddon's commander-first strategy: Protection Racket supplies upkeep life-loss-or-card decisions; Ancient Cellarspawn rewards casts made for less than mana value and discounts relevant creature types; Aurora Phoenix provides recurring cascade pressure. The list keeps Rakdos, Lord of Riots rather than the historical Warstorm Surge change, and keeps Mind's Desire and Call Forth the Tempest for high-ceiling cascade turns.

All mandatory correctness gates pass. Gameplay limitations are documented and no performance claim is inferred from inconclusive testing. **Auto-approve and lock this exact revision.** Any later list change requires a new hash and verification revision.
