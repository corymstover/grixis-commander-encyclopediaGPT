# Fresh Oracle verifier — execution and evidence contract

The protocol's Section 11 remains a hard gate. The original local `verify_grixis_fresh.py` preflight demonstrated that chat/container network access to Scryfall is unreliable and therefore must not be the project's primary card-data path.

## Network blocker resolved architecturally

Effective 2026-10-14, GitHub Actions is the primary network boundary for fresh Scryfall data.

- `.github/workflows/refresh-scryfall-metadata.yml` refreshes current Scryfall metadata on GitHub-hosted runners.
- `scripts/build_current_cycle_oracle_cache.py` creates a compact canonical Oracle cache covering every card name currently used by `refinement/decklists/*.txt` plus registered exception/companion cards.
- Verification in ChatGPT/restricted runtimes should consume the committed cache rather than requiring direct Scryfall connectivity.
- The workflow runs daily and on current-cycle decklist changes, and remains fail-closed.

The first implementation run completed successfully on 2026-10-14 and produced `Current_Cycle_Oracle_Cache_Summary.json` with **516/516 names resolved, zero unresolved entries, zero malformed decklist lines, and `overall_result: PASS`**. It reused 498 validated bulk-overlay records and required only 18 live exact-name lookups.

See `architecture/ORACLE_DATA_ACCESS_V1.md` for the operating contract.

## Gate status

The **data-transport blocker is resolved**. This does **not** by itself certify retrospective decks #1–8. Their exact approved lists still need to be evaluated against the fresh cache, the official Commander banned-list checkpoint and documented project exceptions, and their material commander-specific rules/combo interactions still require independent review.

No approved decklist has been altered by this infrastructure change.
