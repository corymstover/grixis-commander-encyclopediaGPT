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
- 2026-10-14: refresh requested for the SHA-bound Cult of Skaro approval candidate (`4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b`).
