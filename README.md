# Grixis Commander Encyclopedia

Version-controlled project records for the 62-deck Grixis Commander Encyclopedia.

## Project operating rules

- Each deck is commander-first and preserves that commander's identity and natural power ceiling.
- Existing approved/locked decks are preserved. Do not change a list without an explicit request and a logged review.
- The four `GrixisFINAL` archives dated 2026-10-12 are the current authoritative membership baseline; the `Updated-10-11-2026` archives are historical.
- Candidate rankings are a research shortlist, not automatic card additions.
- Approval requires an independently verified 100-card main-deck-plus-commander list, singleton and copy-rule compliance, current identity/Oracle/rulings/legality review, documented project exceptions, relevant interaction verification, and explicit user approval.
- Official Commander legality and project-authorized exceptions must be recorded separately.
- Do not claim global mathematical perfection. Finalization is an evidence-backed stopping rule with documented uncertainty and material reopen triggers.

## Latest verified checkpoint — 2026-10-12

The source ZIP's internal manifest passed 165/165 hashes; all 62 current CSV/TXT pairs independently reconcile, all 62 main-deck-plus-commander lists count to 100, and all 62 singleton scans pass. The official Commander named-ban checkpoint is complete: the only matches are the three known project-authorized Bjorna // Cecily + Lutri exceptions. Full current Oracle/rulings and exact-printing legality refresh remain open. The hash manifest and detailed independent audit are preserved on the [frozen baseline branch](https://github.com/corymstover/grixis-commander-encyclopediaGPT/tree/baseline/freeze-2026-10-12).

## Automated integrity check

Every relevant push and pull request runs [the baseline verifier](scripts/verify_baseline.py) through [GitHub Actions](.github/workflows/verify-baseline.yml). The verifier checks the 124-file archive against all 124 raw file hashes, CSV/TXT card-name quantities, 100-card counts, singleton/copy limits, and collection totals. The initial CI run passed: [view run](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38324768882).

## Start here

1. [Independent baseline audit](source-package/Grixis_Independent_Baseline_Audit_2026-10-12.json)
2. [Individual deck hash manifest](source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv)
3. [Official Commander legality checkpoint](refinement/Official_Commander_Legality_Checkpoint_2026-10-12.md)
4. [Source consolidation register](source-package/Source_Consolidation_Register_2026-10-12.md)
5. [Supplemental Starscape Cleric resolution](source-package/Supplemental_Starscape_Cleric_Resolution_2026-10-12.md)
6. [Source package import status](source-package/IMPORT_STATUS.md)
7. [Baseline & research freshness report](refinement/Baseline_And_Research_Freshness_Report_2026-10-12.md)
8. [Controlled refinement & finalization protocol](refinement/Grixis_Refinement_Protocol_v1.md)
9. [Refinement tracker](refinement/Deck_Refinement_Tracker_2026-10-12.csv)
10. [Candidate decision ledger template](refinement/Candidate_Decision_Ledger_TEMPLATE.csv)
11. [Playtest benchmark template](refinement/Playtest_Benchmark_TEMPLATE.csv)
12. [Deck finalization certificate template](refinement/Deck_Finalization_Certificate_TEMPLATE.md)

## Current baseline status

The supplied 2026-10-12 source report records 306 card-copy additions and 306 removals relative to the previous Updated archives. The independent structural audit confirms 62/62 CSV/TXT reconciliations, 62/62 exact 100-card counts, and 62/62 singleton passes. The official named Commander ban-list checkpoint is complete; the comprehensive fresh Oracle/rulings and exact-printing legality overlay remains pending. Do not treat structural success or a name-level ban-list comparison as a full present-day rules certification.

## Current repository mirror

The current CSV/TXT decklists are mirrored in [the compressed 62-deck bundle](source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz) (62 CSV + 62 TXT files; 124 files total). Their exact per-file SHA-256 values are listed in [the individual deck hash manifest](source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv).

The four original canonical FINAL ZIP archives, four historical Updated archives, and full current audit/candidate-ranking datasets are still retained in the supplied source package outside GitHub. The new tar.gz is a verified mirror bundle, not a replacement for those original archives. See [IMPORT_STATUS.md](source-package/IMPORT_STATUS.md).

## Change control

Put new refinement records in separate paths; do not silently replace historical baselines. Every approved card change must have a reason, source/date, current legality and Oracle checks, a verified new list, and user approval. Reopen a finalized deck only for the triggers in the protocol or on explicit user request.
