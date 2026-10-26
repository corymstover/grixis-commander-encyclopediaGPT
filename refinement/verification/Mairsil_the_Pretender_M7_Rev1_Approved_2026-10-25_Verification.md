# Deck #33 Mairsil M7 Rev1 — exact approved list verification

Date October 25, 2026 (America/Chicago).

**Exact approved raw SHA-256:** `fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad`.

## PASS — physical and source reconciliation

- The approved Archidekt-ready file has **100 lines/cards, 100 distinct names, 1 commander**, 32 lands, no companion. Every line is `1x`, with `[Commander]` only on Mairsil in the first line. No singleton exception or duplicate.
- The earlier exact approved source (2026-10-14) is preserved without modification, raw SHA `51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5`.
- Exactly **6 additions/6 cuts** compared by exact card name: +Marsh Flats/−Haunted Ridge; +Misty Rainforest/−Shipwreck Marsh; +Riptide Laboratory/−Sokenzan, Crucible of Defiance; +Cavern Harpy/−Cephalid Inkshrouder; +Agatha's Soul Cauldron/−Omen Hawker; +Phyrexian Devourer/−Torchling.
- Two complete 100-card seven-swap alternatives (Sanctum over Stormcarved Coast; Strionic Resonator over Fellwar Stone) were source-checked and rejected after color/timing tradeoff review.

## PASS — legal identity and rules

- Mairsil is UBR; added Cavern Harpy is UB, Riptide Laboratory is blue **color identity** (produces colorless mana), Agatha's Soul Cauldron and Phyrexian Devourer are colorless identity, and the two fetchlands have no colored identity. All fit UBR. No project-specific exception applies.
- Existing October 14 100-card audit plus October 25 source research for the six added names and Wizards' current Commander banned list were cross-checked. All selected cards are officially legal in Commander. This is **not** a claim that a new full-100 Scryfall snapshot was fetched on October 25.
- Caging Cavern Harpy gives the activated **pay one life: return this permanent to hand** ability, not Harpy's triggered ETB bounce. This is a mana-free defensive exit but requires casting Mairsil from hand again; losing Cephalid Inkshrouder also loses its discard outlet, shroud and unblockability.
- Riptide Laboratory can target Mairsil (a Wizard) at instant speed with `{1}{U},{T}`; it replaces a red-producing land with a colorless-producing one, partially offset by two fetchland upgrades.
- When Agatha's Soul Cauldron is on the battlefield, its color-flexible activated-ability mana provision applies to your creatures. Cards exiled with Cauldron are **not** caged cards. Caging Cauldron alone does **not** inherit its static ability-sharing text.
- Caged Phyrexian Devourer provides its activated top-library-exile/+1-counter ability without inheriting its power-7 sacrifice trigger. Mairsil's own once-per-turn instance restriction continues to matter. Quicksilver-generated additional ability instances have their own timing/targeting constraints.
- Existing Quicksilver/Gilded Lotus untap and card-draw setup, Rings/Pack Rat cage interaction, Aetherling/Kitten resets and Tree of Perdition/Hateflayer damage remain intact. No unconditional infinite line is claimed without its required cards/timing.
- Commander-first bracket **4 — Optimized**; tags **Cage Toolbox / Activated Abilities / Combo**.

## PASS — owner authorization and engineering

- Cory replied **“Approve”** once to the displayed full exact 100-line candidate, SHA `fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad`.
- Engineering PR [#713](https://github.com/corymstover/GrokBotMTGCompanion/pull/713) squash-merged as `d91c528ae7081c9a67b41fc8401993ef5ebc26dc`. Source-bound M7 contract run `40271014484` SUCCESS; associated PR-head runs `40271014430`, `40271014449`, `40271014442` SUCCESS; five focused exact-deck tests PASS.
- This approval is exact-list scoped. The 2026-10-14 historical source is immutable; 61 other deck locks unchanged. No new full random multiplayer result, technically independent third-model review, or aggregate milestone acceptance is inferred.

**Result: owner approved, exact 100 verified, eligible for canonical GitHub locking and post-merge raw-byte rehash.**
