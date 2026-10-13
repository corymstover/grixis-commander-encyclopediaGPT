# Legality & Audit Freshness Note — 2026-10-12

## What is verified in the supplied package
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

## Current public verification checkpoint recorded by the source package
Wizards' official August 10, 2026 Banned & Restricted announcement said the next announcement was scheduled for October 12, 2026:
https://magic.wizards.com/en/news/announcements/banned-and-restricted-august-10-2026

Official consolidated ban list:
https://magic.wizards.com/en/banned-restricted-list

The sources reviewed during the packaging pass did not confirm an October 12 Commander-specific change. Therefore post-announcement legality was marked **PENDING**. This is a dated statement from the supplied package, not a claim that current legality has been checked today. Do not infer no change from a search miss.

## Manually reconciled current-only card metadata reported in the package
- `Nazgûl`: black identity; rules text allows up to nine copies, legal in Commander. Reference: https://mtg.wtf/card/ltr/730/Nazgul
- `Barad-dûr`: legendary colorless land. Reference: https://cards.mtg-forum.de/magiccard.php?card=Barad-d%C3%BBr&collector_number=253&language_code=en&set=LTR

The source package's card-audit overlay includes metadata source and freshness fields row by row. If a card's identity remains unresolved in the available datasets, treat that row as unknown rather than a pass.


## Subsequent official checkpoint — 2026-10-12

Wizards has now published its October 12 Banned & Restricted announcement: https://magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026. Its listed changes are under Competitive Brawl; it does not announce a tabletop Commander change. The currently published consolidated Commander list is at https://magic.wizards.com/en/banned-restricted-list.

A fresh name-level comparison of the current 62-deck exports against the explicit named Commander bans found exactly three cards, all already authorized by project policy in the designated Bjorna/Cecily deck: Lutri, the Spellchaser (companion-only ban), Trade Secrets, and Yawgmoth's Bargain. No additional named Commander-banned card was found. These exceptions remain officially banned; project authorization is a separate status.

This closes the **official named banned-list checkpoint**. The separate Scryfall `default_cards` bulk refresh then completed on 2026-10-12, using bulk data updated at `2026-10-12T21:06:24.577Z`. It matched all 5,964 current decklist rows to exact set/collector/name records; there were zero unmatched or ambiguous printings, zero missing Oracle IDs, and zero commander color-identity mismatches. All six official banned/not-legal rows are covered by the current eight-row project exception registry and remain separately labeled. The full current Oracle/color-identity/exact-printing Commander-legality metadata gate is now closed. Per-deck rulings and rules-interaction verification remain open.
