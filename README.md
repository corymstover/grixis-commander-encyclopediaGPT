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

The source ZIP's internal manifest passed 165/165 hashes; all 62 current CSV/TXT pairs independently reconcile, all 62 main-deck-plus-commander lists count to 100, and all 62 singleton scans pass. The official Commander named-ban checkpoint is complete: the only explicit banned-list matches are the three known project-authorized Bjorna // Cecily + Lutri exceptions. The initial source report marked the full current Oracle/identity/exact-printing legality refresh as pending; a subsequent Scryfall metadata refresh has since completed and is summarized below. Detailed rules/interaction verification remains open. The hash manifest and detailed independent audit are preserved on the [frozen baseline branch](https://github.com/corymstover/grixis-commander-encyclopediaGPT/tree/baseline/freeze-2026-10-12).

## Current baseline and source consolidation

- [Source consolidation reconciliation — 2026-10-13](source-package/Source_Consolidation_Reconciliation_2026-10-13.md)
- [Deep-research continuation checkpoint — 2026-10-13](source-package/Deep_Research_Continuation_Checkpoint_2026-10-13.md)
- [Duplicate source reconciliation — 2026-10-13](source-package/Duplicate_Source_Reconciliation_2026-10-13.md)
- [Exact current source-package text copies and source hashes](source-package/reference-copies/current-package-text-2026-10-12/README.md)
- [Current project status — 2026-10-13](source-package/Grixis_Project_Current_Status_2026-10-13.md)

The 124 current decklist CSV/TXT files are verified inside the compact archive. The full original source package has been integrity/hash-checked, but not every large raw source file is individually mirrored in GitHub. See the reconciliation report for the exact boundary.

## Controlled refinement campaign

The frozen baseline is preserved on `baseline/freeze-2026-10-12`. The active, separate work branch is `refinement/campaign-2026-10-12`; no approved decklist has been changed.

- [Abaddon the Despoiler — commander-first blueprint v1](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/blueprints/Abaddon_the_Despoiler_v1.md)
- [Abaddon candidate decision ledger](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/decisions/Abaddon_the_Despoiler_Candidate_Decisions_2026-10-12.csv)
- [Abaddon expanded interaction review — cascade, exile, damage engines, and Breach line](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md)
- [Abaddon Aurora Phoenix test plan (registered, not run)](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Aurora_Phoenix_Test_Plan_v1.md)
- [Abaddon Forge engine qualification — pinned release; gates still open](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Forge_Engine_Qualification_2026-10-13.md)
- [Abaddon test-variant integrity check (passed; not a gameplay result)](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Variant_Integrity_Check_2026-10-13.json)
- [Abaddon Aurora Phoenix test variant (separate, not final)](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/variants/Abaddon_Aurora_Phoenix_Test_Variant_v1.txt)
- [Campaign tracker](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/Deck_Refinement_Tracker_2026-10-12.csv)

Abaddon is the first deck in the controlled pass. Its blueprint is complete; four candidates have been triaged. No swap has been accepted or applied. Testing, rules-interaction closeout, and user approval remain required before any final list change.

## Automated integrity check

Every relevant push and pull request runs [the baseline verifier](scripts/verify_baseline.py) through [GitHub Actions](.github/workflows/verify-baseline.yml). The verifier checks the 124-file archive against all 124 raw file hashes, CSV/TXT card-name quantities, 100-card counts, singleton/copy limits, and collection totals. The initial CI run passed: [view run](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38324768882).

## Current Scryfall metadata refresh — completed

The controlled refresh used Scryfall's `default_cards` bulk snapshot updated at `2026-10-12T21:06:24.577Z`. All **5,964/5,964 current decklist rows** matched an exact set + collector number + card name; there were no unmatched or ambiguous printings, no Oracle IDs missing, and no commander color-identity mismatches. All 62 decks' commander identities resolved. The six rows whose current official Commander legality is not ordinary `legal` status are fully registered project exceptions: Lutri as companion, Trade Secrets, Yawgmoth's Bargain, The Madcap Jester, Dragon's Smile, and Tresserhorn's Lord, Returned. Their official status remains visible; project authorization is not misrepresented as official legality.

- [Scryfall metadata audit summary](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/metadata_audit/Current_Scryfall_Metadata_Audit_Summary_2026-10-12.json)
- [Full exact-printing metadata overlay](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/metadata_audit/Current_Scryfall_Metadata_Overlay_2026-10-12.csv)
- [Project exception registry](source-package/research/Project_Exceptions_Current_2026-10-12.csv)
- [Refresh workflow run](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38325331651)

This closes the fresh Oracle/color-identity/exact-printing Commander-legality metadata gate. It does **not** close commander-specific rules/interaction verification, combo checks, strategic blueprints, candidate decisions, or testing.

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

The supplied 2026-10-12 source report records 306 card-copy additions and 306 removals relative to the previous Updated archives. The independent structural audit confirms 62/62 CSV/TXT reconciliations, 62/62 exact 100-card counts, and 62/62 singleton passes. The official named Commander ban-list checkpoint and current exact-printing Scryfall metadata refresh are complete. Detailed card rulings, combo/interaction verification, and commander-first strategic refinement remain pending; do not treat metadata validation as a full strategy or rules-interaction certification.

## Current repository mirror

The current CSV/TXT decklists are mirrored in [the compressed 62-deck bundle](source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz) (62 CSV + 62 TXT files; 124 files total). Their exact per-file SHA-256 values are listed in [the individual deck hash manifest](source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv).

The four original canonical FINAL ZIP archives, four historical Updated archives, and full current audit/candidate-ranking datasets are still retained in the supplied source package outside GitHub. The new tar.gz is a verified mirror bundle, not a replacement for those original archives. See [IMPORT_STATUS.md](source-package/IMPORT_STATUS.md).

## Change control

Put new refinement records in separate paths; do not silently replace historical baselines. Every approved card change must have a reason, source/date, current legality and Oracle checks, a verified new list, and user approval. Reopen a finalized deck only for the triggers in the protocol or on explicit user request.
