# Grixis Commander Encyclopedia — Project Source Guide (v8.1.4)

> Historical reference only. This guide predates the 2026-10-12 FINAL source refresh. Its Updated-10-11-2026 archive names describe the pre-final baseline, not the current deck-list source of truth.

## Authoritative decklists as described at the time
- `Grixis60CSVFiles-Updated-10-11-2026.zip`
- `Grixis2CSVFiles-Updated-10-11-2026.zip`
- `Grixis60TXTFiles-Updated-10-11-2026.zip`
- `Grixis2TXTFiles__Updated-10-11-2026.zip`

## Recommended generated Sources
- `deck_source_inventory.csv`: maps each deck to CSV/TXT names and commanders/companions.
- `csv_txt_reconciliation.csv`: per-deck reconciliation status.
- `deck_audit_summary.csv`: count/singleton/identity/legality audit overview.
- `deck_card_audit.csv`: per-card normalized identity, Oracle text, color identity, effective legality, and audit fields.
- `commander_strategy_profiles.csv`: commander profiles seeded from Oracle text.
- `commander_candidate_rankings_top100_per_commander.csv`: triage shortlist, not automatic recommendations or a power ranking.
- `commander_research_manifest.csv`: commander-to-EDHREC mapping and verified-page fields.
- `project_exceptions_current_v8_1_4.csv`: user-confirmed exceptions/planned future-release cards separate from official legality.
- `card_identity_resolution_overrides_v8_1_4.csv`: targeted identity disambiguation.
- `candidate_ranking_methodology.md`: ranking signals, weights, limitations.
- `grixis_audit_manifest_v8_1_4.json`: pipeline/run metadata.

## Project rules

1. Commander identity first.
2. Optimize to each commander's natural strategic ceiling.
3. Preserve distinctive strategy; no forced generic Grixis shell.
4. Verify counts, singleton/copy exceptions, identity, Oracle text, interactions, and legality before approval.
5. Do not reopen approved/locked decks without an explicit request.
6. Track official legality and project exceptions separately.

## Historical caveat

The v8.1.4 run recorded 58 mechanical passes and 4 reviews. Three were known intentional exceptions/future-release decks. The remaining review was `Starscape Cleric` in `Sol_kanar_the_Swamp_King`, where the display name matched a token and non-token with different Oracle identities. The supplied record says input set `BLB` and collector number `116` identified the non-token card. Use the current 2026-10-12 source package for present membership, not this historical run.
