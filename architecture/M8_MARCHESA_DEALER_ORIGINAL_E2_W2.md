# M8 — Marchesa, Dealer of Death original P1 E2/W2 exact-list traces

Exact approved source: `Marchesa__Dealer_of_Death` SHA-256
`931baa2762738ab32cd274ae8e128d0e3cd1aa85e81e51c2faa4934c1c70f363`.
Original M6 design plan Git blob `03736d6379f1d8f55299118f8dac2e9ff2515e25`.
E2 and W2 were deferred in that exact M7 transfer, not passed.

## E2 — fast mana and actual draw access

Positive seven-card hand: City of Brass, Chrome Mox, Dark Ritual,
Mox Diamond, Badlands, Mana Vault, Ad Nauseam. Play City as the only
land, cast Chrome Mox at zero and **exile** the nonartifact/nonland Ritual,
cast Diamond at zero and **discard** Badlands. Tap City for Mana Vault's
`{1}`, losing one life; Vault taps for `CCC`, Chrome and Diamond each
provide `B`, paying Ad Nauseam's full `{3}{B}{B}` on turn one in the
favorable fixture. Its chosen successive 2- and 1-MV reveals move cards
to hand and cost three further life; no safe indefinite drawing is inferred.

Separate seven-card variants (with a Lotus Petal in the remaining slot)
cast Mystic Remora with a real blue, Rhystic Study with `2U`, or
Necropotence with `BBB`, using City/Chrome/Diamond. These are **different
opening hands**, not multiple simultaneous turn-one casts using one-use
land/rock mana. Opponents can pay `{4}` for Remora or `{1}` for Rhystic;
Remora needs an opponent's noncreature spell, has cumulative upkeep,
and Necropotence replaces the draw step with delayed end-step access.

Adverse seven-card fixtures without a proper Chrome imprint or a land to
discard to Diamond cannot use those three prescribed colored sources.
Mana Vault produces colorless mana, cannot itself pay BBB/U, and does not
untap automatically the next turn.

## W2 — one-card LED/Breach/Freeze loop, actual costs

The favorable starting physical 100-card allocation is: one command-zone
Marchesa, 84 cards in library, nine distinct other graveyard cards, Brain
Freeze and Thassa's Oracle in graveyard, one LED on battlefield, one
Underworld Breach on battlefield, and two tapped lands previously used to
pay Breach's `{1}{R}`. It is a staged late-game fixture, **not** a presumed
opening hand.

LED is sacrificed for **three blue**, discarding its hand. Under Breach,
Brain Freeze costs full `{1}{U}` plus exile of **three other** physical
graveyard cards; the single original spell and its real storm copies mill
our 84 cards over five finite casts, and LED returns by casting the *same*
graveyard object for `{0}` while exiling three other graveyard cards.
Every LED escape increments storm. Eleven finite Freeze casts give
2,4,6,...,22 spell objects, exhaust the example 84-card own library
and three assumed 90-card opponent libraries. Opponent milling goes to
**their** graveyards; it does not refill our escape fuel. Opponents do
not lose merely by having an empty library before a draw.

With a real, still-present Oracle in our graveyard and at least six other
grave cards, escaping LED (three exiles) and sacrificing it for UUU pays
Oracle's UU and three *different* escape exiles, leaving U. Its resolved
ETB trigger sees zero cards and sufficient devotion, yielding a conditional
win. An opponent countering that trigger, graveyard hate, insufficient
other cards, absent LED/Breach/Freeze, or an actual nonzero library breaks
the exact stated conversion. A lone Lotus Petal yields one mana; it cannot
repeatedly pay Brain Freeze's `1U` without additional real resources.

Marchesa's crime reward is not counted for storm-created spell copies:
copying a targeted spell is not casting it anew, and choosing new targets
does not retroactively change a previous crime. A qualifying original
targeted cast can cause a crime when Marchesa is alive, but her optional
`{1}` is not assumed free. This loop is available independently of the
commander, as a separate cEDH win route in her approved list.

## Limits

The executable test is `tests/test_m8_marchesa_dealer_original_e2_w2.py`.
It pins the exact raw 100 and original deferred case plan, and covers
explicit favorable/adverse states with finite physical resources. It does
**not** model arbitrary priority, removal, whole multiplayer game trees,
full draw/randomness, an automatic opponent draw loss, unconditional
infinity or real win rates. No approved card or approval flag changes.
An exact test-head GitHub CI run is required before case registration.
