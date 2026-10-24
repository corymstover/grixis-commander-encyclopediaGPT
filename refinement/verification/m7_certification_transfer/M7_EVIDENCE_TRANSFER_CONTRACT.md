# M7 exact-revision mechanical evidence transfer — enforced from 2026-10-24

This is a canonical **provenance and approval-safety** gate, not a new independent gameplay engine or a new analysis pipeline. It makes the original engineering M6/I/J evidence and the final M7 decision packet explicit before another SHA lock is accepted.

## Immutable historical boundary

- `frozen_approval_snapshot_2026-10-24.json` contains the 62 canonical raw hashes as observed on October 24, including the first 24 newly M7-approved lists. Any unchanged hash passes through without retrospectively pretending it was fully recertified. The 20 documented transfer gaps remain visible, and **none** authorizes an unlock, card replacement or withdrawal.
- `m6_required_cases_2026-10-24.json` records the exact 61 committed commander test plans from engineering PR #535: **882 designed cases, 308 P0 and 574 P1**. Its Git blob SHA and original ID are retained; the plan is a specification, **not evidence that those cases executed**.
- Abaddon is excluded from that 61-deck inventory and must explicitly bind its own existing P0/I/J evidence if reopened.
- The Goben/Norman identity discrepancy remains a hard source exception requiring owner-level resolution.

## Canonical PR attestation

For any new or superseding approved raw SHA, add exactly one file:

`refinement/verification/m7_certification_transfer/<canonical_deck_id>_<approved_sha_first_16>.json`

Fields required by `scripts/verify_m7_certification_transfer.py`:

1. `schema_version: 1`, `deck_id`, `approved_raw_sha256`, `approved_artifact`, and `owner_approval_receipt`; the receipt must contain Cory's exact approved SHA, and the artifact's actual UTF-8 bytes must hash to it.
2. `engineering`: `pr_url`, exact `head_sha`, `grok_first_pass_ref`, `independent_review_ref`, `m7_decision_packet_ref`, `m7_decision_gate_command`, **actual** `m7_decision_gate_ci_run_url`, and `oracle_legality_ref`.
3. `m6_transfer`: `plan_source_path`, `plan_blob_sha`, `ij_receipt_ref`, `ij_scope` (`SAME_EXACT_100` or `TRANSFERRED_WITH_CASE_MAPPING`), and a concrete `revision_diff_and_validity_reason` for changed candidate scope.
4. **Every exact P0 case ID** must be present as `PASSED`, with `test_ref`, `execution_command`, `oracle_source`, `payable_fixture`, `positive_assertion`, `adversarial_assertion`, actual `ci_run_url`, and `scope`. An unimplemented design, inferred pass, failure or P0 deferral fails the gate.
5. **Every exact P1 case ID** must be `PASSED` with the same evidence or `DEFERRED` with a case-specific `specific_reason`, `coverage_consequence` and `owner_visible_unresolved: true`. A deferral must not be described as certified execution.
6. Case `scope` is `EXACT_APPROVED_100` with `tested_raw_sha256` exactly equal to the approved hash, or `REUSED_UNCHANGED` with the original tested `prior_candidate_sha256` and substantive `transfer_rationale` about unaffected sources, costs, targets, zones and failure cases.

The automated validator cannot independently verify the truth of an external GitHub Actions URL, rules engine, source snapshot or qualitative commander strategy. Human review must verify those underlying artifacts. The case-by-case data makes missing work explicit, reproducible and reviewable, and blocks the previously silent mistake of equating a Grok first-pass certificate with a modified ChatGPT final list.

## Required commands and review

```bash
python scripts/verify_m7_certification_transfer.py --check
python -m unittest discover -s tests -p test_m7_certification_transfer.py -v
```

The single focused `.github/workflows/verify-m7-certification-transfer.yml` runs those checks on the exact PR head and on main. Existing complete-approval tests remain separately required. No paid Grok credits, Google Colab reruns, or blanket resealing are required when genuinely reusable prior fixtures already prove a case.

Never merge a new canonical approval if this gate fails. Only Cory may approve the final exact 100-card list, authorize exceptions, or reopen an existing lock.
