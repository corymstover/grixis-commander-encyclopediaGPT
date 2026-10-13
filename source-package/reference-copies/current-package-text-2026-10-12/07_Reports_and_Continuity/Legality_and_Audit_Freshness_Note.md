# Legality & Audit Freshness Note — 2026-10-12

## What is verified in this package
- Current FINAL CSV and TXT archives were parsed.
- Current CSV/TXT card-name quantities were compared deck by deck.
- Main deck + commander total was recalculated with companion cards excluded from the 100-card count.
- Basic lands and explicit card-specific multiple-copy rules were treated separately in singleton scans.
- Existing card metadata was matched to current list membership, with its provenance retained.
- Candidate cross-deck usage counts were recomputed from current FINAL deck lists.

## What is not certified
- This is **not** a complete fresh Scryfall Oracle/rulings pull for the 62 new final exports.
- This is **not** a comprehensive rules-interaction re-review for all 62 decks.
- Inherited legality statuses are from a dataset generated on 2026-10-11 and must not be called a fresh October 12 legality audit.
- Power score and Archidekt tags are carried forward; the deck scores were not regenerated.

## Current public verification checkpoint
Wizards' official August 10, 2026 Banned & Restricted announcement says the next announcement was scheduled for October 12, 2026: https://magic.wizards.com/en/news/announcements/banned-and-restricted-august-10-2026
Official consolidated ban list: https://magic.wizards.com/en/banned-restricted-list
The sources reviewed during this packaging pass did not confirm an October 12 Commander-specific change. Therefore post-announcement legality remains **PENDING** until the official page is confirmed updated. Do not infer no change from a search miss.

## Manually reconciled current-only card metadata
Two current-list names did not resolve to the supplied prior audit or candidate rankings and were given a narrowly scoped public-reference reconciliation:
- `Nazgûl`: black identity; its rules text allows up to nine copies, legal in Commander. Reference: https://mtg.wtf/card/ltr/730/Nazgul
- `Barad-dûr`: legendary colorless land. Reference: https://cards.mtg-forum.de/magiccard.php?card=Barad-d%C3%BBr&collector_number=253&language_code=en&set=LTR

The card-audit overlay includes metadata source and freshness fields row by row. If a card's identity remains unresolved in the available datasets, treat that row as unknown rather than a pass.
