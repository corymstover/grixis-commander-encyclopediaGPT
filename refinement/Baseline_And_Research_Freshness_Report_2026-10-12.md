# Baseline & Research Freshness Report — 2026-10-12

## What is authoritative now
The current package's `README_START_HERE.md` and project charter designate the four `GrixisFINAL` CSV/TXT archives as the only current card-membership baseline. The earlier `Grixis*Updated-10-11-2026` files are historical pre-final archives. Keep both; do not overwrite either.

## Verified from the current package
- 62 current CSV and 62 current TXT deck files.
- CSV/TXT quantities reconcile for all 62 decks.
- Total deck quantities including the documented companion: 6,201.
- Main deck plus commander: 6,200 cards across the 62 decks (62 × 100); the designated companion is tracked outside that count.
- All 62 lists changed relative to the prior Updated archives, with 306 card-copy additions and 306 card-copy removals collection-wide.
- The source package records all 62 as `FINAL / COMPLETE`, but current Oracle, rulings, comprehensive interaction, and current official Commander legality reviews were not rerun for the final exports.

## Current blockers before any deck should be declared newly verified
1. Refresh the full-list Oracle identity/color/legality overlay for the current FINAL membership, using current data and explicitly recorded data timestamps.
2. Confirm the current official Commander banned/legality checkpoint. Do not infer “no change” from a search miss.
3. Review all 62 commander blueprints. In the supplied current strategy profile file, `strategy_terms`, `negative_terms`, and `profile_notes` are blank for all 62 rows; profiles are machine-seeded from commander Oracle text. That is useful scaffolding, not a completed strategic assessment.
4. Treat candidate rankings as the starting shortlist, not as approved inclusions. The 6,200-row candidate file reuses inherited rank scores and says so. Current project deck usage counts were updated, but candidate ranking scores were not regenerated against current lists.
5. The inherited methodology uses EDHREC legacy synergy (25% score weight). EDHREC announced migration from Synergy to Lift on commander pages on October 1, 2026. Record current inclusion, current Lift and sample size explicitly in new reviews; do not present the legacy score as a current measure.

## Efficient remedy
Do **not** restart a full research pipeline just because you are reviewing one deck. Use the authoritative FINAL list and cached card data, run a focused current-list correctness pass once at the project level, then refresh only the commander-specific candidate evidence needed for the deck currently under review. Use the existing exceptions, identity overrides, candidate shortlist and cross-deck usage counts as inherited aids with their freshness labeled.

## Links consulted
- Current baseline and limitations are documented in the source package README, current status and legality-freshness note.
- EDHREC Lift migration: https://edhrec.com/articles/changelog-replacing-synergy-with-lift-on-edhrecs-card-pages
- EDHREC Lift methodology: https://edhrec.com/articles/from-synergy-to-lift-the-math-behind-edhrecs-new-era
- Scryfall bulk/API guidance: https://scryfall.com/docs/faqs/i-m-having-trouble-accessing-the-scryfall-api-or-im-blocked-17

## Addendum — independent source/banned-list checkpoint (2026-10-12)

- Source ZIP integrity passed. All 165 internal manifest-listed payload files matched both the exact recorded size and SHA-256 hash. Outer package SHA-256: `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`.
- An independent parser rechecked all 62 CSV/TXT deck pairs: 62/62 quantity reconciliations pass, 62/62 main-deck-plus-commander lists contain exactly 100 cards, and 62/62 singleton checks pass. Per-file raw hashes are preserved in `source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv`.
- Wizards' October 12 B&R announcement is now published; changes are listed under Competitive Brawl only, and the consolidated Commander ban list was checked on the same date. The only named Commander-banned cards present in current decklists are the three documented Bjorna/Cecily exceptions: Lutri as companion, Trade Secrets, and Yawgmoth's Bargain. No additional named Commander-banned cards were found.
- One blank Oracle field was individually resolved for Starscape Cleric, BLB #116. The subsequent current Scryfall `default_cards` refresh completed on 2026-10-12: 5,964/5,964 exact-printing matches, zero unmatched/ambiguous printings, zero missing Oracle IDs, and zero commander color-identity mismatches. All six current official banned/not-legal rows map to the registered project exceptions. The current Oracle/color-identity/exact-printing Commander-legality metadata gate is closed; relevant rules/rulings interactions and commander-first strategic review remain open.
