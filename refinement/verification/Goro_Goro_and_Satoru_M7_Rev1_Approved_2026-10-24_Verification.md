# Goro-Goro and Satoru M7 Rev1 — canonical approval verification

This evidence is bound to Cory's contextual exact owner approval on 2026-10-24 of the proposed 100 physical card list with raw SHA-256 **`36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c`**. It is a pre-merge certificate and does not itself assert that canonical main already contains the result.

- New exact-approved file: `refinement/decklists/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24.txt`; 99 list lines, 2x Island, 100 physical, Goro commander first.
- Historical approval preserved: `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt`, raw `2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf`.
- Exactly five replacements: Bitterblossom/Naga, Roaming Throne/Grim Hireling, Hanweir Garrison/Kaito Bane, Misty/Crumbling, Marsh/Fabled.
- 33 lands, 66 library nonlands, six Game Changers, B/R/U, zero project exceptions; all protected October 14 Ninja and combat-draw cards and all six original mana rocks retained.
- Power Bracket 4 — Optimized; three Archidekt tags Ninjas, Dragons, Extra Combats.

## Source evidence

[Engineering PR #696](https://github.com/corymstover/GrokBotMTGCompanion/pull/696) at exact head `1d3c45bad93e8531d4b9e5a27edb19f1b034f61b`; [GitHub Actions run #40072138305 SUCCESS](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40072138305), nine focused tests; source was independently re-fetched at exact head and hashed with external `sha256sum` to equal Cory's approved hash.

Selected 99-name Oracle manifest preserves 96 cached current-at-2026-10-23 Scryfall records from GrokBot PR #669 and three manually checked published Scryfall card pages (Roaming Throne, Marsh Flats, Misty Rainforest). The three do not receive invented Oracle UUIDs or false claims of a full-live collection. Every card Commander-legal and U/B/R compatible in that evidence. Important mechanics: Hanweir attack triggers and tapped-and-attacking 1/1 Human tokens, Roaming Throne choose Human doubling triggered abilities, one Goro trigger per damaged player per combat damage step, Tetsuko evasion, fetch typed duals and shock-life timing, Bitterblossom upkeep and haste dependency.

No actual multi-player game tests, validated win-rate estimate, complete rules engine, or external independent third-model review is claimed. Loss of Grim Hireling's independent Treasure economy and Kaito's Ninja-draw/interaction is disclosed.

## Required exact-head + postmerge checks

The new focused unittest checks exact owner-hash, original-hash, five physical substitutions, full singleton/basic/Oracle/legality, registry and tracker approval-only edits, and all **20 previous newly M7-approved canonical deck artifacts** by actual raw SHA-256. Re-run prior Garza focused regression. Preserve the previously merged 20, and only mark the NEW Goro M7 approval as canonical when the PR has passed exact-head GitHub Actions and is merged using expected head SHA; then refetch main and independently hash its bytes and verify registry/tracker fields.

No unapproved Deck #22 canonical change is authorized.
