# Doctor Doom, King of Latveria — Current-Cycle Commander-First Blueprint

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Deck:** #13 / `Doctor_Doom__King_of_Latveria`  
**Authoritative baseline:** `refinement/decklists/Doctor_Doom_King_of_Latveria_Current_Cycle_Baseline_2026-10-14.txt`  
**Standardized baseline SHA-256:** `08825dee74f034bc38415fe7370cccc3fe69de7887769577dd32f98f5bbd4572`

## Commander identity

Current Oracle text:

> Whenever you discard one or more land cards, each opponent loses 2 life.
> At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives.

Doctor Doom therefore rewards **separate land-discard events**, not merely high discard volume. A single effect that discards several lands at once produces one Doom land-discard trigger; multiple cycling/activated-cost discards produce multiple triggers. The combat ability also makes Villain density and connive payoffs materially commander-specific.

## Primary game plan

1. Deploy Doom and cheap self-discard infrastructure.
2. Turn lands in hand into repeated, separately triggered discard events through cycling, Trade Routes, Seismic Assault, Psychic Frog, rummage effects, and Villain/connive engines.
3. Reuse discarded lands/cards with Crucible of Worlds, Moonstone, Containment Construct, Shadow of the Grave, and Dakmor Salvage.
4. Multiply Doom's triggered abilities with Chameleon, Spark Double, and Roaming Throne rather than adding generic Grixis combo packages.
5. Use the Villain/connive shell as a second axis: Lethal Scheme, Kang, Ultron, Villainous Hideout, Glorious Purpose, Norman Osborn, Prowler, Tombstone, Leader, and other Villains generate value while advancing Doom's natural game plan.
6. Close through repeated Doom drain, Cool but Rude/Monument pressure, Villain combat, or the Dakmor repeatable drain engines.

## Natural power ceiling

**Bracket 4 — Optimized.** Doom is an efficient four-mana engine with repeatable table-wide damage and access to strong Grixis interaction/tutors, but his natural win structure is multi-piece and resource-dependent. The deck is optimized aggressively without replacing its identity with generic Consultation/Oracle or unrelated cEDH packages.

## What distinguishes this deck

This is not generic Grixis discard and not a generic Villain tribal deck. Its defining resource loop is **lands as discard ammunition**: cycling/activating them one at a time, converting those discards into Doom damage and secondary mana/card/token payoffs, then recovering the lands and repeating. Villain/connive cards are selected when they reinforce that loop or multiply Doom's specific triggers.

## Source discrepancy resolved

The authoritative October CSV/TXT exports agree with one another and are used as the baseline. `deck_card_audit.csv` contains a different five-card snapshot: it has `Archnemesis`, `Chameleon, Master of Disguise`, `Crumbling Necropolis`, `Doctor Octopus, Master Planner`, and `Doom's Time Platform` where the authoritative CSV/TXT instead contain `Cool but Rude`, `Kang, Temporal Tyrant`, `Lethal Scheme`, `Moonstone, Harsh Mistress`, and `Villainous Hideout`.

This discrepancy also biases the candidate ranking pool: several cards already present in the authoritative baseline appear as candidates, while audit-only cards such as Chameleon are omitted as discovery candidates. The current refinement therefore treats CSV/TXT as authoritative and manually evaluates all five audit-only cards without rerunning the research pipeline.
