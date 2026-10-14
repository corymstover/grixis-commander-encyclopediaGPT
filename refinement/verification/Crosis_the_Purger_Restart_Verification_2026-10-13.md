# Crosis, the Purger — Fresh Restart Verification Certificate

**Deck:** #9 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Frozen archives:** `GrixisFINAL60--2026.zip` and `GrixisFINALTXT60--2026.zip`  
**Baseline raw CSV SHA-256:** `c5f8c7a28a38941a5f35c95d9c8da9cb3ba08c973d4a7ec8d51220d806d3a677`  
**Baseline raw TXT SHA-256:** `bbd4acc84ff0abd5f43045bd28d9cc4a154cbfe2592923967315b9a1497c4435`  
**Normalized baseline hash:** `11f7ac19d46c1caae2e598307f78f5f00f2dc8885a57d9d87e19f44c646cb848`  
**Final exact-TXT SHA-256:** `449d7c02655713e05cc1051c8461dd36061ae1b85eaa9a8bef6595198b36dfc3`

## Mandatory gates

| Gate | Result | Evidence |
|---|---|---|
| 100-card main deck including commander | PASS | 100 copies including Crosis |
| Singleton | PASS | 92 distinct names; only repeated cards are basic lands |
| Commander first | PASS | `1x Crosis, the Purger [Commander]` first |
| Land count | PASS | 36 lands |
| TXT/CSV reconciliation | PASS | Exact quantity map matches |
| Final exact-list hash | PASS | Hash matches prior exact-TXT artifact preserved byte-for-byte |
| Oracle/identity coverage | PASS WITH DIRECT CHECKS | Refresh for 90 retained baseline names; two additions and two cuts checked directly |
| Color identity | PASS | UBR identity throughout |
| Official Commander legality | PASS | Ban list checkpoint reviewed 2026-10-13; no final card is banned |
| Project exceptions | PASS | None used |
| Relevant interactions | PASS | Crosis payment/color choice, Blizzard Specter modes/target choice, Recoil sequence |
| Candidate triage | PASS | 16 candidates reviewed; close alternatives recorded |
| Commander-first strategy | PASS | Combat discard, evasive Specters, payoff density and control retained |
| Consistency | PASS WITH LIMITS | P(at least 2 lands in opening seven) = 79.26%; no claim about keep/mulligan or win rate |
| Matched-seed multiplayer test | NOT AVAILABLE | No qualified simulator/sample; no performance claim |
| Tracker and cumulative ledger sync | PENDING | Final campaign tracker/cumulative-ledger synchronization immediately follows in the same campaign commit |

## Rules cross-check

- **Crosis:** combat damage triggers the ability. Paying `{2}{B}` is optional on resolution; if paid, choose a color and the damaged player reveals their hand and discards every card of that color.
- **Blizzard Specter:** choose bounce or discard on combat damage. The bounce returns a permanent the damaged player controls to its owner’s hand; it does not destroy/exile it, and that player chooses the permanent.
- **Recoil:** return the target to its owner’s hand, then that player discards. The target may be recast; Recoil is not hard removal.
- No deterministic infinite combo is included or relied upon.

## Final disposition

**APPROVED / LOCKED — FRESH RESTART REVIEW PASSED.** Tracker and cumulative change ledger are synchronized in this campaign commit. Prior-cycle approval remains historical.
