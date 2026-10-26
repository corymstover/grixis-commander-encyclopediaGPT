# Deck #35 Marchesa, the Black Rose M7 Rev1 — owner-approved exact verification

Date: October 26, 2026 (America/Chicago).
**Approved 100-card raw SHA-256:** `c4857d176eaa6ed682da7cab974014d393fce2efe698bdca6994d77bb27ddf02`.

## Structural and official legality verification

- Exactly **100 physical cards**, commander first with `[Commander]` designation, 98 different card names, duplicates **only two Island and two Swamp basic lands**.
- All 98 names independently resolved against 2026-10-26 Scryfall current Oracle collection; **98/98 officially Commander legal and UBR color identities**, no banned/off-color cards, no exceptions or unresolved objects.
- Exactly 34 lands, preserves the commander-centered free sacrifice, +1/+1 counter, persist reset and end-step return engines.
- Historic 2026-10-15 approved original artifact and SHA `627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b` retained byte-for-byte under its prior path; seven one-for-one strategic swaps.
- No claim of formal randomized multiplayer win-rate, complete interaction engine or full historical M6 I/J replay.

## Rules caveats

- Marchesa needs a +1/+1 counter on a creature **when it dies**, and returns it only at the next end step.
- The Ooze's Mutagen activation costs 1 and activates **only as a sorcery**; not emergency instant counter protection.
- Curse-Marred Demon's ETB card search is followed by a random discard and requires RR.
- Madame Null's counters demand optional life payments equal to creature power.
- Accursed Marauder edicts **nontoken** creatures only; Voldaren Thrillseeker pays 1 to sacrifice for damage.
- Aether Channeler's white Bird token does not add white to this card's Commander color identity.

## Exact-head GitHub certification

- M7 engineering PR: https://github.com/corymstover/GrokBotMTGCompanion/pull/716 ; exact head `043646be33f37d43bb2cb4b8cabc92d6be10a8a8`; squash merge `1ebe3f1e21da36d11c43cf9aacf3a9768a103a3b`.
- Deck #35 exact workflow success: https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40283561444
- M7 decisive whole-deck decision workflow success: https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40283561282
- Source-bound finite test `tests/test_m7_marchesa_black_rose_rev1.py`; candidate schema `data/grixis/m7/decision_reviews/Marchesa__the_Black_Rose_rev1.json`; Scryfall snapshot `data/grixis/m7/oracle_snapshots/Marchesa__the_Black_Rose_Rev1_Scryfall_20261026.json`.
- Cert transfer register: `refinement/verification/m7_certification_transfer/Marchesa__the_Black_Rose_c4857d176eaa6ed6.json`.
- Historical original M6 cases retained; scoped new tests do not falsely imply broader simulation.

## Owner authorization

Cory replied **“Approve”** to the complete exact list and SHA `c4857d176eaa6ed682da7cab974014d393fce2efe698bdca6994d77bb27ddf02` on October 26, 2026; this single approval authorizes canonical replacement, merge and lock.

**Power Bracket 4 — Optimized. Tags: +1/+1 Counters / Aristocrats / Combo.**

A final post-merge remote read of `main` list, approval record, and `state/current_deck_overrides.json` is mandatory before reporting lock success.
