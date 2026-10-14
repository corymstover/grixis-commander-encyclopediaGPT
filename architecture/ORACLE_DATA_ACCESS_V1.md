# Oracle Data Access Architecture v1

**Effective:** 2026-10-14

## Problem

Chat/container execution environments may not have reliable direct DNS/network access to Scryfall. A direct API failure in that environment must not repeatedly block project verification when GitHub Actions can fetch and preserve the same authoritative data reproducibly.

## Network boundary

GitHub Actions is the project's primary network boundary for fresh Scryfall card data.

1. `.github/workflows/refresh-scryfall-metadata.yml` fetches current Scryfall bulk metadata on GitHub-hosted runners.
2. `scripts/refresh_scryfall_metadata.py` produces the validated 62-deck printing overlay and summary.
3. `scripts/build_current_cycle_oracle_cache.py` builds a compact canonical Oracle cache for every card name appearing in `refinement/decklists/*.txt`, plus registered exception/companion cards.
4. The current-cycle builder reuses the validated bulk overlay whenever possible and performs live exact-name Scryfall lookups only for names missing from that overlay.
5. The workflow commits only successful outputs. Any unresolved name, malformed decklist line, stale/invalid bulk snapshot, or failed upstream validation blocks the refresh.

## Preferred verification input

Verification running from ChatGPT, a local container, or another restricted runtime should read:

- `refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl`
- `refinement/metadata_audit/Current_Cycle_Oracle_Cache_Summary.json`

Direct Scryfall access from the chat/container is optional fallback behavior, **not a prerequisite** for verification.

A cache is usable only when its summary says `overall_result: PASS`, contains every required name, has no unresolved or malformed entries, and satisfies the project's freshness thresholds. Otherwise verification fails closed and requests/causes a GitHub refresh rather than silently treating stale data as current.

## Automatic refresh policy

The refresh workflow now:

- runs daily;
- runs on `main` as well as refinement/automation branches when the refresh implementation changes;
- runs whenever a current-cycle decklist changes;
- supports manual workflow dispatch;
- preserves artifacts and diagnostics for failed runs;
- avoids refresh loops because metadata output paths are not push triggers.

## Efficiency

The expensive Scryfall bulk download occurs once per workflow run. Current-cycle coverage then reuses that overlay; only names absent from the 62-deck overlay need individual exact-name lookups. This avoids hundreds of redundant calls while still covering newly introduced refinement cards.

## Verification boundary

This architecture solves **card-data transport and freshness**, not every finalization gate. Current Oracle text/color identity/legality still must be reconciled with the official Commander banned list, project exceptions must remain separately labeled, and commander-specific rules/combo interactions still require independent review.

## Fail-closed rule

Never downgrade a missing current cache, failed GitHub refresh, unresolved card, or stale metadata into a pass. The improvement is that restricted chat networking no longer constitutes the normal data path; it should therefore no longer be the recurring blocker.
