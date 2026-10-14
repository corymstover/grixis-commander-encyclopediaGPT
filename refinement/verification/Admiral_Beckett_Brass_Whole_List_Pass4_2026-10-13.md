# Admiral Beckett Brass — Whole-list audit continuation

**Status:** IN PROGRESS / UNLOCKED under the new mandatory whole-list standard.

## Current candidate

Current 100-card provisional list SHA-256: `02b62b9424f6a8cb0337eb9b4286557d5cddb5150acb26b744a8ed9bc0d68d7d`. Exactly 100 cards, 97 distinct names, no repeated nonbasic card names. This is a three-swap revision of the previously approved two-swap v3 list:

- Dire Fleet Neckbreaker → Kitesail Larcenist
- Captain Vargus Wrath → Slippery Scoundrel
- Shared Animosity → Open into Wonder

The earlier two substitutions (Coastal Piracy → The Indomitable; Glint-Horn Buccaneer → Zephyr Singer) remain in this provisional build.

## Card/rules review

Kitesail Larcenist ({2}{U}, 2/3 flying Pirate, ward {1}) temporarily transforms selected artifacts/creatures into Treasure artifacts for as long as it stays on battlefield. It can eliminate a blocker, but may grant an opponent a mana resource, and the effect is reversible. Commander legal; blue identity.

Slippery Scoundrel ({2}{U}, 2/2 Pirate) has ascend and becomes hexproof/unblockable only after its controller receives the city's blessing (ten permanents). The blessing is permanent once earned. It is a delayed enabler, not unconditional early evasion. Commander legal; blue identity.

Open into Wonder ({X}{U}{U}, sorcery) makes X target creatures unblockable this turn and grants combat-damage card draw. X=3 costs five mana; if three Pirates deal combat damage to the same player, Beckett's end-step theft condition is satisfied. It is a one-shot payoff and does not create Pirates. Commander legal; blue identity.

Beckett's trigger is at the beginning of its controller's end step and targets a nonland permanent controlled by a player dealt combat damage by three or more Pirates that turn. Beckett need not have attacked or dealt damage.

## Full-list challenge

The working inventory covers all 100 cards and identifies six weak slots, of which three are provisionally replaced. Bident of Thassa, Fiery Cannonade and Storm the Vault are provisionally retained with documented draw-density, Pirate-sparing sweeper and Treasure/mana reasons. These retains are not yet conclusively demonstrated superior to all plausible alternatives.

EDHREC commander data supports these candidates as commander-specific research leads, not proof of performance. Current overall commander sample is approximately 4.74K decks; narrowly filtered subsets are substantially smaller and cannot justify strong conclusions.

## Gates still open

- Fresh current Oracle/color-identity/Commander legality audit of all 100 final cards; older inherited card audits alone do not satisfy this gate.
- Quantitative mana-value/colored-source and opening-hand consistency comparison, with actual card metadata.
- Full post-swap comparison that closes with zero additional material improvements, including the three contested retains.
- Explicit red-team of interactions and possible material regressions.
- Final evidence packet with whole_list_audit_passed true only if substantiated.

Do not auto-lock until these requirements are completed, despite standing autonomous authorization.
