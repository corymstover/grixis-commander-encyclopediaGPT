# M8 Mairsil, the Pretender — source-paid cage instances and mana loops

October 28, 2026. Current approved raw source `Mairsil__the_Pretender`, SHA-256 `fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad`. This is evidence-only; every approved card/lock is preserved.

The exact-current `tests/test_m8_mairsil_p1_cage_loops.py` executes **nine original deferred P1 scenarios**: K4–K7, E1–E2, W1–W2, F2, with opposing prerequisite failures and exact-source card presence. **W3 and F3 remain open**, rather than recycling a removed Mirror-Mad Phantasm claim as a win. Each case must be registered by a subsequent separate PR with the committed test blob, exact-head GitHub CI and individual finite positive/adverse assertions.

## Distinct card-object and restriction cases

- **K4 Marvin:** Marvin, Murderous Mimic gains *activated* abilities from Mairsil, including their embedded once-per-turn activation instructions; it does not inherit Mairsil's *static* ability to grant cages, nor permission to use one instance repeatedly. Mairsil and Marvin have separate activated-ability instances, one activation of a given original caged ability per instance this turn. Missing Marvin removes the second independent source. Official Duskmourn notes explain the self-name substitution and only-activated-abilities rule: https://magic.wizards.com/en/news/feature/duskmourn-house-of-horror-release-notes.
- **K5 Spark Double:** A Spark Double Mairsil copy is nonlegendary, has the copied ETB caging ability and can cage another real eligible card on entry. The copied static cage ability sees the controller's exiled cards with cage counters. Missing second card still allows copy/ETB but does not create a nonexistent new cage target.
- **K7 Wishclaw/Elixir:** Thousand-Year Elixir permits tap abilities of newly controlled Mairsil as though hasty, but **does not put a wish counter on Mairsil**. Wishclaw Talisman's copied activated cost removes a *wish counter* from itself (meaning Mairsil when copied), not a cage counter from the exiled Wishclaw card. Therefore caging Wishclaw alone is not a free tutor.
- **E1/E2:** An actual fresh Mairsil ETB after blink may cage a different eligible artifact/creature from hand or graveyard. A caged Arcanis tap ability draws three if Mairsil can legally tap now and that precise ability instance hasn't already been used; no unconditional immediate tap without haste/Elixir.
- **F2:** Graveyard hate can make graveyard caging unavailable but need not stop Mairsil exiling an eligible card from hand. An absent card in both zones means no new target.

## W1 / K6 — caged Quicksilver, Lotus and Crab actual net-blue trace

Mairsil must have *Quicksilver Elemental*, *Gilded Lotus* and *Horseshoe Crab* caged, and legal access to his tap abilities (e.g., Elixir or established haste):

1. Tap Mairsil with the caged Lotus ability for **{U}{U}{U}**.
2. Pay **{U}** using the caged Horseshoe Crab ability to untap Mairsil.
3. Pay **{U}** using the caged Quicksilver Elemental ability targeting Mairsil himself. On resolution he gains a **new set of activated ability instances**, each with an independent one-use restriction. The old used instances remain used, but the new Lotus/untap/Quicksilver instances can be used next.
4. Repeat. Each complete circuit nets **one {U}**; five iterations net 5 blue, ten net 10 blue, with new instance IDs tracked. Missing Quicksilver or Crab stops repetition after the first instance; missing Lotus or tap readiness prevents initialization.

The restrictions are not silently ignored or arbitrarily reset; they are **new granted ability instances**. CR 113.10a specifies that an ability-granting effect's activation instructions become part of the granted activated ability. This is the mechanism by which the self-target Quicksilver effect adds fresh restricted instances, rather than deleting the old ones. Official comprehensive rules: https://magic.wizards.com/en/rules (latest rules); the engineering M6 blueprint and exact-current approved source identify the physical cards.

## W2 — separate physical Rings/Alchemist/Lotus repeatable net-blue trace

This is a **separate source-supported mana engine**, not Mairsil borrowing the abilities:

1. Tap an actual untapped Gilded Lotus for three blue mana.
2. Tap a legally able-to-tap Aphetto Alchemist, targeting the tapped Lotus to untap it.
3. Rings of Brighthearth triggers from this nonmana activated ability. Pay **{2}** from the three blue and copy the activated ability; choose Aphetto itself as the copy's target. Copy untaps Alchemist; original resolves and untaps Lotus.
4. Both permanents and Rings remain in their original legal reusable state, with **one additional blue** in pool. Six cycles net six blue, twelve net twelve. Without Rings, a ready Alchemist, or a ready Lotus the required repeating start state is lost.

## Explicit certification limits

Both winning-resource cases are deterministic **finite state/repetition traces plus an inductive replay invariant**, not an entire MTG rules engine or a guarantee against priority-based disruption. The fixture assumes the identified caged or battlefield cards were legally placed, the owner is able to use tap abilities, and there is no unmodeled replacement effect or opponent interrupting the trace. No route from infinite mana to a particular opponent's defeat is automatically certified by the mana proof; the deck still needs a real payoff and legal timing. Mairsil W3 alternative finisher structures and F3 removed self-mill failure remain independently deferred, as do other decks' original P1 cases and final M8 owner acceptance.
