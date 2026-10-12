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

## Start here

1. [Source package import status](source-package/IMPORT_STATUS.md)
2. [Baseline & research freshness report](refinement/Baseline_And_Research_Freshness_Report_2026-10-12.md)
3. [Controlled refinement & finalization protocol](refinement/Grixis_Refinement_Protocol_v1.md)
4. [Refinement tracker](refinement/Deck_Refinement_Tracker_2026-10-12.csv)
5. [Candidate decision ledger template](refinement/Candidate_Decision_Ledger_TEMPLATE.csv)
6. [Playtest benchmark template](refinement/Playtest_Benchmark_TEMPLATE.csv)
7. [Deck finalization certificate template](refinement/Deck_Finalization_Certificate_TEMPLATE.md)

## Current baseline status

The supplied 2026-10-12 source report records 62 current CSV/TXT pairs reconciled, all 62 at exactly 100 main-deck-plus-commander cards, and 306 additions / 306 cuts relative to the previous Updated archives. It also explicitly says the comprehensive fresh Oracle/rulings and current official Commander legality review was not rerun across all current lists. Those gates remain pending; the historic 62/62 structural pass must not be treated as a full present-day rules certification.

## Import policy

Canonical ZIP archives, all 124 individual decklist files, and the larger card-audit/candidate research datasets have **not yet been transferred into this repository**. They remain in the supplied source package outside this repository. See [IMPORT_STATUS.md](source-package/IMPORT_STATUS.md). Do not assume their presence here or substitute a reconstructed copy for the authoritative baseline.

## Change control

Put new refinement records in separate paths; do not silently replace historical baselines. Every approved card change must have a reason, source/date, current legality and Oracle checks, a verified new list, and user approval. Reopen a finalized deck only for the triggers in the protocol or on explicit user request.
