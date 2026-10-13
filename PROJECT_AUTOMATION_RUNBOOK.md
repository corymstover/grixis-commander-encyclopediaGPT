# Project Automation Runbook

**Scope:** operational workflow for the 62-deck Grixis Commander Encyclopedia. This document describes automation and gates; it does not authorize decklist changes or approval.

## Source-of-truth rules

- Treat the 2026-10-12 frozen source-package archive and hash manifest as immutable membership baseline.
- Treat the latest supplied FINAL CSV/TXT exports as decklist truth. Never infer decklist edits from candidate rankings, metadata overlays, or audit output.
- Keep official Commander legality separate from documented project exceptions.
- Preserve approved/locked decks. Only the user can reopen or approve a deck.
- Candidate screening and static metadata checks do not replace card-by-card rules review or the user approval gate.

## Automated jobs

### 1. Current Scryfall metadata refresh

Workflow: `.github/workflows/refresh-scryfall-metadata.yml`

Triggers:
- Weekly, Monday at 08:23 UTC.
- A push to `refinement/**` or `automation/**` touching the refresh script, validator, Abaddon audit, dependencies, workflow, or any `refinement/metadata_audit/REFRESH_REQUEST*.md` file.
- Manual `workflow_dispatch`.

Sequence:
1. Verify frozen archive/hash/count/singleton integrity before downloading card data.
2. Download and stream-parse Scryfall `default_cards` bulk data.
3. Validate that generated metadata belongs to the current run, is no older than two hours, and the source bulk timestamp is within 72 hours.
4. Require all 62 decks / 5,964 rows, exact printing matches, Oracle IDs/text, resolved color identities, and no unresolved or unexpected legality/exception rows.
5. Independently audit Abaddon's 94 distinct names, UBR identity compatibility, and Commander legality.
6. Commit generated metadata only if every validation gate passes.
7. Preserve a diagnostic artifact and a job-summary report even on failure.

The refresh is fail-closed. A failed or stale run does not replace validated metadata and does not approve a deck. Transient HTTP failures receive bounded retries; permanent access/response errors stop the job and remain visible in logs.

### 2. Fast project quality gates

Workflow: `.github/workflows/verify-baseline.yml`

On relevant pushes and pull requests, it runs:
- Repository unit tests.
- Workflow trigger/path contract checks.
- Tracker CSV schema, unique deck ID, and approval metadata validation.
- Frozen 62-deck source archive verification.

This is the fast regression layer. It should catch request-glob drift, stale or malformed tracker edits, and accidental baseline changes before the project proceeds.

## Requesting a refresh

Preferred for a traceable one-off request: add a short dated Markdown file named `REFRESH_REQUEST-YYYY-MM-DD-<reason>.md` under `refinement/metadata_audit/`. The request must be plain text and must not include card-list changes. The wildcard trigger should start the refresh automatically.

The scheduled run is the routine freshness mechanism. Do not rerun Google Colab or a separate research pipeline for ordinary deck updates. Use manual workflow dispatch only when a refresh is needed immediately or a failed run needs a deliberate retry.

## How to respond to results

- **PASS:** use the generated overlay and summary as current metadata evidence, record its timestamp and bulk timestamp, and keep rules/strategy/approval gates separate.
- **FAIL/blocked:** inspect the workflow summary and artifact first. Identify whether the failure is a source-integrity issue, stale bulk data, exact-printing mismatch, missing Oracle data, identity mismatch, legality/exception issue, or transient network error. Retry only when justified; do not weaken validation thresholds to force a pass.
- **Abaddon-specific:** the 2026-10-13 refresh verified all 94 distinct names against current Scryfall metadata; the official ban-list checkpoint and bounded interaction review are separately recorded. The final gate remains NO until the exact unchanged 100-card list is explicitly approved by the user.
- **Performance tests:** do not repeat an inconclusive Forge comparison with the same uninformative setup. Treat card-density math as descriptive, never as a win-rate estimate.

## Change safety

- Automation may refresh metadata and validation reports; it must never rewrite decklists.
- A proposed deck swap must be logged as a decision and separately approved.
- Never set `final_gate_passed=YES`, fill an approval date/hash, or issue a finalization certificate before explicit user approval.
- Any new official illegality, color-identity mismatch, unresolved printing, missing Oracle text/ID, stale source, or baseline hash discrepancy is a stop condition, not a warning to ignore.
