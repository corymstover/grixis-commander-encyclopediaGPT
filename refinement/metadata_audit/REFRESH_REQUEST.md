# Controlled Scryfall metadata refresh request

Run the current Scryfall `default_cards` bulk refresh against the frozen 124-file decklist mirror.

Scope:
- Refresh exact-printing match, Scryfall ID, Oracle ID/text, color identity, release date, and Commander legality.
- Preserve official legality separately from the project's documented exceptions.
- Do not modify decklists, the frozen hash manifest, approved deck status, or the source package.
- Treat missing/ambiguous exact printings, future-release cards, color-identity mismatches, and unexpected illegal rows as review items.
- This is metadata preflight only; relevant combo/rulings review and commander-first strategic blueprints remain separate gates.

## Refresh initiated — 2026-10-13 UTC

This commit intentionally triggers the existing GitHub Actions bulk refresh. The output should be assessed as current Scryfall bulk metadata, not as a rules-interaction or finalization pass.
