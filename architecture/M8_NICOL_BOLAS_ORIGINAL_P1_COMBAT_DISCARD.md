# M8 — Nicol Bolas original P1 W1/W2/F3 bounded witnesses

Source identity: `Nicol_Bolas`, exact Cory-approved 100-card raw SHA-256
`a6079935a50b9469ca487e58e6bac159f8b777348b31585256b967f92c5d0df6`.
Original M6 plan Git blob `fb8641de923796d2b3b4b9de1eb76cd02367bc9d`.
Original cases were **deferred** in the pinned M7 receipt, not already passed.
The current October 27 Oracle cache is used to assert key ability wording.

## W1 — Sword/Assault combat

Finite positive: Nicol Bolas (7 power), equipped with Sword of Feast and Famine
(+2/+2), connects three times with one opponent. Each hit is 9 combat commander
damage; 9, 18, 27 reaches the official 21-damage loss threshold. The Sword
untaps **actual lands** on each hit. Two red-producing lands plus three other
one-mana lands supply the full `{3}{R}{R}` for Aggravated Assault in the
postcombat main phase after hits one and two; each successful activation untaps
creatures and creates another combat followed by a main phase. No additional
mana or combat is invented. Bolas's upkeep cost `{U}{B}{R}` is paid in this
fixture before the active turn.

Adverse: one red land, only four lands, first blocked hit, absent Sword,
absent Assault, countered Assault activation or an unpaid Bolas upkeep each
prevents the described repeat. The line is therefore a **conditional** repeatable
combat engine, not a guaranteed turn-one or uncontestable infinite loop.

## W2 — actual damage-trigger/discard finishes

Finite positive: seven combat damage from Bolas to player A with Kediss in
play makes Bolas itself deal seven **noncombat** damage to B and C. The actual
three damage events each cause that damaged opponent to discard their hand;
with Liliana's Caress, hand sizes 5/4/6 imply life totals 23/25/21 from a
40-life start. Only A accrues seven commander damage. A paid Chandra's Ignition,
an Ingris attack trigger, or a legal Quicksilver Dagger tap likewise produces
noncombat Bolas damage and the discard trigger if it hits a player. Curiosity
may draw for each appropriate damage event; it is optional, not automatic.

Torment of Hailfire is modeled as four *opponent-chosen* iterations: a player
with two nonland permanents and two cards can choose to lose **zero** life,
whereas an opponent with neither resource loses 12. Neither a generic
discard payoff nor Torment is thereby certified as inevitable lethal.

Adverse: a blocked Bolas attack cannot start Kediss's combat-damage chain;
absent Kediss affects only the actually damaged player. The original M6 W2
plan named Raiders' Wake and Viridian Longbow, but **both are absent** from
this exact owner-approved Rev1. Their lines are not simulated as live cards.
The remaining in-list pathways are evaluated directly, so retiring only those
two old cards would *not* retire all of W2.

## F3 — fast-combo counterplay

A declared hypothetical counterable opposing win spell on turn 3 beats a
Nicol Bolas game plan that would first cast its eight-mana commander on turn 4
**if** it resolves. A source-legal Force of Will, if actually in hand with a
separate blue card and enough life for the alternate cost, can counter that
specific spell. Without the actual Force, blue pitch card, sufficient life,
or counterability, that modeled protection is unavailable. Other interaction
in the exact 100 is not presumed drawn or free. The old blueprint's "no
deterministic commander win" is overbroad: an uninterrupted three-hit 21+
commander-damage line is concrete, but neither its availability nor fast-table
matchups have been assigned a fabricated win rate.

## Scope and certification boundary

- Test: `tests/test_m8_nicol_bolas_original_p1_finishes.py`.
- Current list and original deferred case IDs are asserted by raw SHA and M7
  transfer-plan Git blob. Exact cached Oracle phrases are checked.
- Finite explicit favorable/adverse states only; no arbitrary stack, targeting,
  blocker/priority tree, mana-ramp probability, card-access probability,
  infinite result, multiplayer policy or real games are simulated.
- The commander-first owner-approved 100, all locks and project exceptions
  remain unchanged. CI against the exact committed test blob is required
  *before* adding a `CURRENT_SHA_TESTED` case disposition.
