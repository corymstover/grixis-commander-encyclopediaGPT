# Controlled metadata refresh request

This file is the exact push-trigger path watched by .github/workflows/refresh-scryfall-metadata.yml. Update this file to request a fresh Scryfall default-cards bulk scan across the frozen 62-deck source package.

## Scope
- Refresh exact printing match, Scryfall ID, Oracle ID/text, color identity, release date and official Commander legality.
- Preserve official legality separately from project-authorized exceptions.
- Do not edit the frozen decklists, baseline hashes, or user approval markers.
- Do not accept a stale cache as fresh if Scryfall is unavailable.
- Run the 62-deck metadata validator and the Abaddon-specific 94-name audit before generated data is committed.
- Keep rules/combo review, strategic approval, and user final approval as separate gates.

The refresh can also be started from GitHub Actions by manually running “Refresh current Scryfall card metadata.” The weekly schedule refreshes the shared metadata snapshot without requiring a manual request.

## Current request
- 2026-10-14: refresh requested for the SHA-bound Edward Kenway approval candidate (`a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019`) after the complete gate identified unresolved current-cycle Oracle-cache records. This request is metadata-only and must not alter any decklist or approval state.
