# Independent baseline audit — 2026-10-12

## Scope and source identity

- Source package: `Grixis_Commander_Encyclopedia_Current_Source_Package_2026-10-12(1).zip`
- SHA-256: `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`
- Package ZIP integrity: PASS
- Internal package manifest: 165 entries; 165 SHA-256 and size checks passed; 0 failures; 0 missing files.
- Audit scope: independently parse current FINAL CSV/TXT deck pairs and compare the current official Commander ban list as of 2026-10-12.
- Exact per-deck hashes are in `Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv`.

## Structural results

| Check | Result |
|---|---:|
| Current CSV decklists | 62 |
| Current TXT decklists | 62 |
| CSV/TXT pairs reconciled | 62/62 PASS |
| Main deck + commander | 6,200 total cards |
| Companion cards outside 100-card count | 1 (Lutri) |
| Total exported quantities including companion | 6,201 |
| Lists exactly 100 cards excluding companion | 62/62 PASS |
| Singleton / copy-rule checks | 62/62 PASS |
| Independently detected structural issues | 0 |
| Current active card rows | 5,964 |
| Unique active card names | 1,524 |

This verifies list structure and membership against the supplied package. It does not prove strategic quality or that every current Oracle/rulings record has been freshly retrieved.

## Current official Commander legality checkpoint

Checked against the official Wizards Commander banned list on 2026-10-12:
https://magic.wizards.com/en/banned-restricted-list

The October 12, 2026 general Banned & Restricted announcement made no tabletop Commander changes; its announced changes were for Competitive Brawl:
https://magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026

Three current-list entries matched the official Commander ban list, and all three are already recorded project exceptions in the designated Bjorna/Cecily deck:

| Card | Current location | Official status | Project treatment |
|---|---|---|---|
| Lutri, the Spellchaser | Companion | Banned as a companion; allowed in the 99/commander | Explicit project exception; keep companion exception distinct from official status |
| Trade Secrets | Main deck | Banned in Commander | Explicit project-authorized exception in designated Bjorna/Cecily deck |
| Yawgmoth's Bargain | Main deck | Banned in Commander | Explicit project-authorized exception in designated Bjorna/Cecily deck |

These are not newly discovered unauthorized inclusions. Preserve the existing exception registry and label official legality separately. No other official Commander banned-name matches were found by this cross-check.

## Metadata and rules work still open

- The current card audit inherits much of its Oracle/color-identity data from the 2026-10-11 snapshot. That data is useful evidence, but it is not a complete fresh Scryfall Oracle/rulings pull for the current FINAL lists.
- 188 current card rows representing 182 distinct names came from the candidate-ranking snapshot and had no reverified legality status. These are the names in `Grixis_Targeted_Card_Review_Queue_2026-10-12.csv`.
- The prior audit had a metadata gap for `Starscape Cleric` in `Sol_kanar_the_Swamp_King`. Its exact printing is `BLB` collector `116`. Current card references confirm it is a black Creature — Bat Cleric with Oracle text: “Offspring {2}{B} (You may pay an additional {2}{B} as you cast this spell. If you do, when this creature enters, create a 1/1 token copy of it.) Flying This creature can't block. Whenever you gain life, each opponent loses 1 life.” It is listed as Commander-legal. Reference: https://mtg.wtf/card/blb/116/Starscape-Cleric. This specific gap is resolved; it does not substitute for refreshing all current records.
- For all 1,524 unique current-list names, complete the intended project-wide current-data refresh/identity and legality overlay before issuing a full correctness certificate. Blank color identity by itself is not an error for a colorless card.
- Commander strategy blueprints remain incomplete for all decks. The inherited strategy profiles have blank `strategy_terms`, `negative_terms`, and `profile_notes` across all 62 rows.
- Candidate ranks are triage evidence, not mandatory additions; inherited rank scores were not recalculated against the current final lists.
- The 62 decks remain previously FINAL/approved baselines. This new audit does not reopen or alter any decklist.

## Freeze decision

**Structural baseline frozen by hash; repository content mirror incomplete.** The per-deck CSV/TXT hashes preserve the exact current list identity even though the 4 current FINAL archives, 4 historical archives, 124 individual decklists, and large research datasets have not yet been copied into GitHub. Do not call this repository a complete archive mirror until those files are transferred and verified.

## Next efficient action

1. Refresh metadata for the 182 candidate-only card names in the targeted queue.
2. Refresh and compare current identity/Oracle/legality metadata for the full 1,524-name set using one current Scryfall dataset snapshot where practical, not repeated ad hoc pipeline runs.
3. Complete commander-specific blueprints in tracker order, then assess only high-impact candidate swaps.
4. Do not change approved lists until a concrete proposal has been presented and explicitly approved.
