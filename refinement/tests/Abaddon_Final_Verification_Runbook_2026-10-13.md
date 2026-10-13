# Abaddon Final Verification Runbook — 2026-10-13

## Frozen assets

- Baseline branch: `baseline/freeze-2026-10-12`
- Work branch: `refinement/campaign-2026-10-12`
- Compact deck bundle: `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`
- Compact bundle SHA-256: `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`
- Abaddon baseline TXT SHA-256: `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`

## Read-only structural verification

Run:

```bash
python refinement/tests/Abaddon_Independent_Final_Decklist_Check_2026-10-13.py source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz
```

Expected gates: the archive digest matches; CSV/TXT quantities reconcile; the list totals 100; there is one commander marker; nonbasic singleton/copy rules pass; and the exact frozen TXT SHA-256 is printed. If this fails, stop and reconcile the discrepancy before any other action. Do not modify the baseline to make the script pass.

## Current metadata/legality evidence

The Scryfall bulk refresh generated 2026-10-13 04:36 UTC, with data last updated 2026-10-12 21:06 UTC, matched 5,964/5,964 current global list rows to exact print/name keys. For Abaddon, the static CI audit logged 94/94 exact deck-scoped metadata joins, no color-identity mismatch, 100 cards and zero nonbasic duplicate violations. This is strong historical evidence, but it is not an approval-time live refresh; repeat or explicitly document unavailable live access before issuing the final certificate.

The current official Wizards Commander banned list was checked 2026-10-13 and no card in the Abaddon baseline was identified as banned. Keep project-specific exception statuses distinct; the Abaddon baseline does not rely on the Bjorna/Cecily exceptions.

## Rules/strategic closeout

- The 94-name inventory and triage CSV now have no literal triage-queue items remaining.
- A new section in the interaction review records the 19 final role/context classifications.
- Treat this as a coverage-scoping completion, not exhaustive proof for every game state. Keep nontrivial conclusions and conditions explicit.
- Aurora Phoenix vs Mind's Desire remains inconclusive under the existing Forge AI test. Retain Mind's Desire; do not rerun the same AI comparison.
- The baseline consistency report is exact hypergeometric card-density math, not gameplay or a win-rate measurement.

## Required stop/approval rule

After structural verification and best-effort current identity/legality refresh, present the exact unchanged 100-card baseline and the closeout caveats to the user. The user must explicitly approve the exact list. Until that approval is received and recorded, keep `final_gate_passed=NO`, `user_approval_date` blank, and do not issue a finalization certificate marked complete.
