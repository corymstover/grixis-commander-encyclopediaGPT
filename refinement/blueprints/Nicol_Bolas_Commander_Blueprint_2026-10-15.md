# Nicol Bolas — Commander-First Blueprint

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #41 of 62  
Status: working refinement evidence; not user approval

## Commander identity

Current Oracle:

- `{2}{U}{U}{B}{B}{R}{R}`
- Legendary Creature — Elder Dragon
- Flying
- At the beginning of your upkeep, sacrifice Nicol Bolas unless you pay `{U}{B}{R}`.
- Whenever Nicol Bolas deals damage to an opponent, that player discards their hand.
- 7/7

The critical rules fact is that Nicol Bolas's discard ability triggers from **damage for any reason**, not only combat damage.

## Commander-first plan

1. **Accelerate an eight-mana, color-intensive commander.** The deck needs unusually high mana quality because casting Bolas requires UUBBRR plus two generic and maintaining him asks for UBR each upkeep.
2. **Make Bolas himself deal damage immediately or to multiple opponents.** Haste/evasion is useful, but direct commander-sourced damage is stronger because it bypasses combat and still empties a hand.
3. **Convert hand destruction into resources.** Waste Not, Geth's Grimoire, Tergrid, both Tinybones cards, Liliana's Caress, Raiders' Wake, and Sangromancer make the discard event more than one-for-one attrition.
4. **Protect the commander at low opportunity cost.** Free stack interaction, Greaves/Boots, Regalia, Cavern, and Command Beacon are justified because losing an eight-mana commander before it deals damage is catastrophic tempo.
5. **Retain a compact combat finisher.** Aggravated Assault + Sword of Feast and Famine remains a repeatable extra-combat line when a creature can connect and five lands can fund another Assault activation.

## Signature commander-sourced damage engines

- **Dragon Tempest:** Nicol enters as a flying Dragon, gains haste, and the entering Dragon itself deals at least 1 damage to a chosen target. If an opponent is targeted, that opponent discards their hand before combat.
- **Ingris Stingerquill:** whenever Nicol attacks, Ingris causes **Nicol** to deal 1 damage to each opponent. Each opponent therefore discards their hand before blockers.
- **Kediss, Emberclaw Familiar:** after Nicol deals combat damage to one opponent, Nicol deals that much noncombat damage to every other opponent. One connection becomes table-wide hand destruction.
- **Chandra's Ignition:** Nicol deals damage equal to his power to every opponent and each other creature. At printed power this is 7 to each opponent plus a broad creature sweep, and every opponent hit discards their hand.
- **Pain for All:** enchanting Nicol immediately has Nicol deal damage equal to his power to another target; if Nicol is later dealt damage, Nicol deals that much to each opponent.
- **Quicksilver Dagger:** gives Nicol a tap ability through which Nicol deals 1 to a player and then draws a card.
- **Viridian Longbow:** durable Equipment version of a Nicol-sourced one-damage tap ability.

## Discard payoff network

- **Waste Not:** converts each discarded card into cards, mana, or bodies.
- **Geth's Grimoire:** draws for each opponent discard.
- **Tergrid, God of Fright:** can return discarded permanent cards to your battlefield.
- **Tinybones, Bauble Burglar:** can stash discarded cards still in opponents' graveyards and let you play them later.
- **Tinybones, Trinket Thief:** draws after a discard turn and punishes empty hands with its activated ability.
- **Sangromancer:** gains 3 life per opponent card discarded, providing stabilization proportional to the commander's success.
- **Liliana's Caress / Raiders' Wake:** convert discarded cards into direct life loss.

### Tergrid / Bauble Burglar ordering

If an opponent discards a permanent while Tergrid and Tinybones, Bauble Burglar are controlled by the same player, both triggers can exist. Their controller chooses the order. If Tergrid resolves first and moves the permanent out of the graveyard, Tinybones cannot exile that card from the graveyard; if Tinybones resolves first, Tergrid cannot later return that card. This is flexible overlap, not automatic double value.

## Natural power ceiling

**Power Bracket 4 — Optimized.**

The commander costs eight mana, has a recurring upkeep cost, and does not itself provide a deterministic command-zone combo. The strongest realistic build is therefore high-powered optimized control/discard with explosive commander-sourced hand-wipe sequences—not a forced generic cEDH Oracle/Breach shell.

## Deliberate differentiation from #42 Nicol Bolas, the Ravager

The project immediately follows this deck with **Nicol Bolas, the Ravager // Nicol Bolas, the Arisen**. High-ranked Bolas planeswalkers are therefore not automatically imported here. The original Nicol Bolas deck is defined by **Bolas himself dealing damage to empty hands**; the Ravager deck can own the stronger Superfriends / transform-planeswalker / Bolas-tribal identity.

Recommended Archidekt tags: **Discard / Commander Damage / Control**.
