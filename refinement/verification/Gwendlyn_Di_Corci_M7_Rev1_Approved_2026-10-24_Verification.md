# Gwendlyn Di Corci M7 Rev1 — canonical source-bound whole-100 verification

**Owner-approved raw SHA-256:** `36b76cbe47a04b7492007103e4baaad50324b3e72fb2067b28aa8bb9da70e355`; 100 physical cards / 95 named rows; one Gwendlyn commander, 2 Island, 5 Swamp; 35 lands; 64 library nonlands; exactly one card per nonbasic name.

Status of this file: pre-merge certification and reproducible gate, not an assertion about canonical `main` before merger. Its paired exact-head test `tests/test_gwendlyn_di_corci_m7_rev1_approval.py` is the executable lock evidence.

## Sources and provenance

- Owner explicit contextual “Approve” on 2026-10-24 after complete Rev1 proposal and hash.
- Proposed exact engineering file: `data/grixis/m7/independent_candidates/Gwendlyn_Di_Corci_M7_Rev1_Proposed_20261024.txt`, independent engineering PR #697 at head `ea44dbfa62391fe53c0ead6654d2565a1daf3c65`; Actions #40074265497 SUCCESS nine focused tests.
- Historical Oct14 source `refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt` SHA `9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9`; unchanged.
- Oct23 208-name live-Scryfall-seeded archive `data/grixis/m6/oracle_snapshots/Gwendlyn_Di_Corci_M7_Scryfall_20261023.json` and published Oct24 Scryfall pages for Sting, the Glinting Dagger and Misty Rainforest (new full-live-100 API collection not claimed).
- Paired canonical selected source file: `refinement/verification/Gwendlyn_Di_Corci_M7_Rev1_Scryfall_Selected_2026-10-24.json`, all 95 unique proposed names, quantities, Oracle, identity and legalities.

## Exact owner-approved additions and cuts

1. + Hymn to Tourach / − Dauthi Voidwalker: avoids exile replacement nonbo with Tergrid/Tinybones Bauble Burglar/Bloodchief; loses graveyard hate.
2. + Rings of Brighthearth / − Underworld Dreams: {2} copies commander ability; with Illusionist's Bracers exactly **three** activations, not four; wheel punishment lost.
3. + Sting, the Glinting Dagger / − The Raven Man: Gwendlyn haste and at-beginning-of-own-combat untap; Sting **equip {2}**, not 1; activated discard available only on controller's turn; tokens and Raven discard sacrificed.
4. + Misty Rainforest / − Crumbling Necropolis: untapped Island typed dual flexibility for fetch life cost, no guaranteed immediate three colors.
5. + Marsh Flats / − Drowned Catacomb: Swamp typed BR/UB dual targets for search/life cost; retained Xander's Lounge tapped option.
6. + Shivan Reef / − one Mountain: untapped U/R fixing, one fewer basic and life costs.

## Verification boundaries and quality

- Gwendlyn activated ability: {T} random discard of target player, use **only during your turn**, affected by summoning sickness absent haste; Rings and Bracers each copy nonmana activated ability independently. Sting untaps at beginning of **each combat**, but cannot let Gwendlyn tap for discard in opponents' turns.
- Preserve owner October 14 discard/wheel/activation core: Mind Twist, Magewright's Stone, Pemmin's Aura, Illusionist's Bracers, Minamo, Patriar's Seal, Thousand-Year Elixir, Lightning Greaves, Tergrid, Tinybones, Waste Not, Geth's Grimoire, Liliana's Caress, Chains, Notion Thief, all prior wheels and black tutors.
- Full selected Oracle source reports every one of 95 legal in Commander and color-identity within U/B/R; zero project exceptions; all 17 original Game Changers retained. Structural check is exact 100 cards and 35 lands.
- Nominal U/B/R sources rise [21,24,17] to [22,24,18] under caveat that fetching tapped Xander's Lounge counts all three, dual fetch targets grant two; *not* a turn-four cast probability or multiplayer win rate.
- Bracket **4 — Optimized**, tags **Discard / Wheels / Untap**. No actual games, statistical win rates, or full rules-engine simulation asserted.
- Test independently hashes all **21 previously newly-M7-locked** lists and the historical Gwendlyn file, enforces non-target registry SHA/path stability for all other 61 and validates only tracker index 21.
