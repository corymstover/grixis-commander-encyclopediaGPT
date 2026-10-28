# M8 — Kefka original P1 W2: source-paid Breach / Wheel

Exact owner-approved Kefka 100 SHA-256:
`14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d`.
Original M6 design-plan blob: `07efd24960263757e3dbc9177127554ce3539f14`.
W2 is the one remaining original deferred live case after K4/F3's
**Demonic Counsel-specific** retirement; the approved Rev1 has Step Through
instead. Neither prior retirement constitutes a W2 test.

## Underworld Breach + LED / Lotus Petal + Brain Freeze

The approved exact 100 contains Underworld Breach, the one Lion's Eye
Diamond, the one Lotus Petal, Brain Freeze and Thassa's Oracle. Reuse the
already exact-head-tested physical one-LED/one-Freeze trace from Marchesa,
Dealer of Death's separate W2 test, now requiring every card in this
**Kefka** approved raw source and its pinned original W2 plan. This is
shared card mechanics, not a transfer of Marchesa's approval or identity.

In its **staged late-game** 100-object fixture, one commander is outside the
library, 84 cards remain in library, nine distinct other cards in grave,
Freeze and Oracle in grave, LED and already paid Breach on battlefield,
and two tapped lands previously paid Breach's `{1}{R}`. The real LED makes
exactly three blue, while every Brain Freeze escape pays `{1}{U}` plus
three **other** graveyard cards. Escaping the same LED between Freeze casts
costs another three other cards and adds an actual cast for storm. Five
bounded self-mill casts exhaust the 84 own library cards, replenishing
our grave fuel; six more casts can exhaust three assumed opponent
90-card libraries, which **do not** replenish our grave. Empty opponent
libraries are not automatic losses until attempted draws.

If Oracle actually remains in our grave and enough separate other grave
cards exist, a further LED escape/sacrifice funds the full UU and three
exiles for escaped Oracle. Its resolving ETB on empty library can win.
Missing pieces, too few grave resources, Breach removal, an unresolving
Oracle trigger or own library still containing cards refute that exact
conversion. Recurring Lotus Petal alone only gives one mana; it cannot
by itself pay the two-mana Brain Freeze escape on each cycle.

## Wheel of Fortune / Jeska's Will / LED

The seven-card Wheel redraw is **not** extra free mana or an automatic
infinite loop. A real Wheel from hand costs `{2}{R}` **before** LED can
be activated in response. With Wheel on stack, one existing LED may
sacrifice, discard the rest of our hand and add three mana **of one
color**, then Wheel can resolve and draw seven per player from actual
libraries. Activating LED *before* casting Wheel from hand instead
discards that very Wheel, so it cannot be cast from hand using that LED
mana. Countered Wheel yields no seven-card refill.

Jeska's Will separately costs `{2}{R}` and uses the opponent's **hand
size as it resolves**, not the number assumed at casting. If the
opponent still has seven cards, its red mode produces seven R; if
Wheel remains in hand, paying its `{2}{R}` leaves four red. If the
target's hand is now empty, Will produces zero red. Controlling Kefka
when casting Will permits both modes; the other mode **exiles** up to
three cards with permission to play them, subject to normal timing and
payment. They are not drawn or automatically cast for free. Wheel first
would discard a previously held Will unless Will is subsequently
redrawn or made castable from graveyard with properly paid Breach.

Kefka's own card-type draw trigger fires on Kefka's entry or attack,
not merely on Wheel discards. Relevant Waste Not/Tinybones payoffs need
their own actual events and do not make this W2 line unconditional.

## Evidence boundary

Executable positive/adverse case:
`tests/test_m8_kefka_original_w2_breach_wheel.py`.
It pins exact source, original plan, and cached Oracle wording, reuses
the one-card LED/Breach physical ledger, and separately checks actual
Wheel/Will timing and resource failures. These are finite fixtures, not
full Magic stack/game simulation, observed wins, library probability,
infinite-resource proof or immunity to interaction. No approved card,
source hash, approval lock or project exception is changed. Exact-head
GitHub CI is mandatory before the W2 disposition may be recorded.
