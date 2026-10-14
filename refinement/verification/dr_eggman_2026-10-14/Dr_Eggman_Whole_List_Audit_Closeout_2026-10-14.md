# Dr. Eggman — Whole-List Audit Closeout

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Status:** **APPROVAL CANDIDATE FROZEN — FINAL GATE PENDING**  
**Deck:** #15 — Dr. Eggman  
**Authoritative frozen TXT source SHA-256:** `35406415bee72bd3b92e7639314bcdd1e2404d2cf713e103e8c20c2f27eea607`  
**Clean current-cycle baseline SHA-256:** `395dacb0238fa92407af5ba55ed2b01905b2cda585f1ffaa248f1201b4644463`  
**Approval candidate SHA-256:** `ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3`

## Audit scope

All 99 noncommander slots were challenged for mana efficiency, curve, mana production, hand replenishment, interaction, protection, recursion, artifact density, Construct/Robot/Vehicle density, villainous-choice leverage, discard conversion, artifact-enter synergy, cast-only anti-synergy, commander trigger multiplication, high-impact deployment targets, finishers, commander dependence, and realistic outside alternatives.

The audit preserves Dr. Eggman's defining play pattern: stock the hand with desirable Construct/Robot/Vehicle cards, make each opponent choose between actual discard and free artifact deployment, and multiply the commander's end-step trigger without replacing that strategy with generic Grixis artifact combo.

## Authoritative source discrepancy

The matching CSV/TXT exports remain authoritative. `deck_card_audit.csv` differs in exactly five names.

**Authoritative export-only baseline cards:**
- Big Mother Mouser
- Curie, Emergent Intelligence
- Mechan Assembler
- Megrim
- The Valeyard

**Audit-snapshot-only names:**
- Imposter Mech
- Mirrorworks
- Scrawling Crawler
- Thopter Fabricator
- Torrential Gearhulk

The audit-only cards were still evaluated as challengers. `Thopter Fabricator` earned a final slot; the other four did not. No stale audit row was silently substituted for the authoritative baseline.

## Final proposed 12-card delta

1. `Megrim` -> `Tinybones, Bauble Burglar`
2. `Great Intelligence's Plan` -> `Y'shtola Rhul`
3. `Steel Overseer` -> `Roaming Throne`
4. `Efficient Construction` -> `Strionic Resonator`
5. `Mechanized Production` -> `Spark Double`
6. `Big Mother Mouser` -> `Thopter Fabricator`
7. `Reaver Titan` -> `Vision, Spectral Synthezoid`
8. `Thopter Spy Network` -> `One with the Machine`
9. `Etherium Sculptor` -> `Scrapyard Recombiner`
10. `Dragonskull Summit` -> `City of Brass`
11. `Drowned Catacomb` -> `Mana Confluence`
12. `Sulfur Falls` -> `Spire of Industry`

## Swap reasoning

### Megrim -> Tinybones, Bauble Burglar
`Megrim` is a redundant three-mana punishment enchantment that only converts actual opposing discard into damage. `Tinybones` converts those same Eggman discard outcomes into opponent-owned cards that can be played later and adds a repeatable table-wide discard activation. It preserves the discard-pressure side of the commander while materially increasing card access and agency.

### Great Intelligence's Plan -> Y'shtola Rhul
`Great Intelligence's Plan` is a six-mana one-shot villainous-choice event focused on one opponent. `Y'shtola Rhul` creates an additional end step on the first end step when its target remains legal, which retriggers Eggman and every other beginning-of-end-step engine. Its blink mode also reuses relevant ETB bodies. The replacement is substantially more commander-dependent and repeatable.

### Steel Overseer -> Roaming Throne
`Steel Overseer` is a slow generic artifact anthem. `Roaming Throne` choosing Scientist directly causes Eggman's triggered ability to trigger an additional time and also improves `Davros, Dalek Creator`. This is a direct commander multiplier rather than generic board scaling.

### Efficient Construction -> Strionic Resonator
`Efficient Construction` triggers only when an artifact spell is cast; it does not trigger from Eggman's signature put-onto-the-battlefield deployment. `Strionic Resonator` directly copies Eggman's triggered ability, producing another draw plus another complete set of villainous choices.

### Mechanized Production -> Spark Double
`Mechanized Production` is slow, upkeep-based copy value with an incidental alternate win condition. `Spark Double` can immediately enter as a nonlegendary copy of Dr. Eggman, coexist with the commander, and create an independent Eggman end-step trigger every turn.

### Big Mother Mouser -> Thopter Fabricator
`Big Mother Mouser` is an Eggman-compatible Robot but requires combat/death sequencing for meaningful output. `Thopter Fabricator` is an Eggman-compatible Vehicle whose second-card-drawn trigger naturally turns on during a normal turn when the draw-step card is followed by Eggman's end-step draw. It provides repeatable evasive artifact bodies without requiring the Fabricator to attack.

### Reaver Titan -> Vision, Spectral Synthezoid
Both are legal Eggman deployment targets. `Reaver Titan` is principally a large combat/crew body. `Vision` is a Robot that converts each of your turns into a free noncreature-or-Robot cast from hand, substantially increasing post-Eggman hand conversion and preserving the Robot identity.

### Thopter Spy Network -> One with the Machine
`Thopter Spy Network` is slower upkeep/combat value. `One with the Machine` immediately refills the hand according to the greatest mana value among artifacts you control; Eggman's preferred deployment targets routinely make this a large draw spell. Immediate refill is particularly valuable because one Eggman trigger can potentially remove multiple legal targets from hand across opponents' choices.

### Etherium Sculptor -> Scrapyard Recombiner
`Etherium Sculptor` reduces the cost of artifact spells you actually cast but does nothing to improve Eggman's free placement. `Scrapyard Recombiner` is itself a legal Construct target and can sacrifice an artifact to search a Construct directly into hand, stocking future Eggman choices. `Foundry Inspector` remains as one generic artifact-cost reducer, avoiding total loss of that role.

### Mana-base upgrades
`City of Brass`, `Mana Confluence`, and `Spire of Industry` replace three conditional check lands. The candidate stays at 31 lands but improves access to all three colors; `Spire of Industry` is especially reliable in this artifact-dense list.

## Important retained decisions

### Discard branch
- `Liliana's Caress` remains as the most efficient retained direct discard punishment.
- `Waste Not` remains because it converts different discarded card types into cards, mana, or bodies and therefore creates broad pressure on Eggman's discard branch.
- `Geth's Grimoire` remains because actual opponent discards replenish the hand from which Eggman deploys his legal targets.
- `The Valeyard` remains because it increases each villainous-choice event rather than merely increasing generic discard density.

### Artifact-enter infrastructure
- `Mechan Assembler`, `Simulacrum Synthesizer`, `Weapons Manufacturing`, `Master Transmuter`, and `Ultron, Artificial Malevolence` remain because they function with artifacts entering or being put onto the battlefield rather than requiring every artifact to be cast.
- `Ultron, Artificial Malevolence` makes `Mirrorworks` redundant: it already offers a `{2}` copy trigger for another nontoken artifact entering and additionally turns copied noncreatures into 2/2 Robot Villains.

### Eggman targets and finishers
The candidate retains **28 Construct / Robot / Vehicle cards that Eggman can legally put from hand onto the battlefield**. High-impact retained targets include `Cityscape Leveler`, `Coalstoke Gearhulk`, `Combustible Gearhulk`, `Depthshaker Titan`, `Entropic Battlecruiser`, `Krang, Utrom Warlord`, `Metalwork Colossus`, `Myr Battlesphere`, `Nautiloid Ship`, `Noxious Gearhulk`, `Oildeep Gearhulk`, `Thunderhawk Gunship`, both Ultrons, and the new `Vision`, `Thopter Fabricator`, and `Scrapyard Recombiner`.

### Interaction / protection
The premium interaction suite remains intact: `Fierce Guardianship`, `Mana Drain`, `Deflecting Swat`, `Deadly Rollick`, `Cyclonic Rift`, `Toxic Deluge`, `Blasphemous Act`, `Chaos Warp`, `Withering Torment`, plus removal-bearing artifact targets. `Padeem` and `Lightning Greaves` continue to protect key permanents/commander.

### Mana and artifact infrastructure
`Sol Ring`, `Arcane Signet`, `Fellwar Stone`, `Mox Opal`, the three Talismans, `Foundry Inspector`, `Tezzeret`, artifact lands, `Inventors' Fair`, `Academy Ruins`, `Urza's Saga`, and the premium Grixis land suite remain. The list deliberately stays at the established 31-land count rather than cutting another land while adding a five-mana commander multiplier package.

## Challenger exhaustion

The project top-100 candidate ranking was used as discovery evidence, not as an instruction list. The following notable challengers were individually tested against exact slots:

- `Ruin Grinder` — legal Construct target, but its wheel is death-dependent and symmetrical; it did not beat the retained always-live engines.
- `Mirrorworks` — rejected as redundant with superior baseline `Ultron, Artificial Malevolence`.
- `Torrential Gearhulk` — legal Construct target but the exact list has too few instants to make its graveyard-dependent ETB consistently superior to retained targets/infrastructure.
- `Imposter Mech` — legal Vehicle target but opponent-board dependent and lower floor than the selected commander multipliers/targets.
- `Scrawling Crawler` — legal Construct, but refilling opponents' hands works against the deck's discard-pressure branch and the life-loss rate is insufficient to offset that tension.
- `Pinnacle Emissary` — cast-trigger wording does not reward Eggman's free placement enough.
- `Damocles Base, Sword of Kang` — thematic Vehicle with villainous choice, but combat-damage dependency and permissive choice outcomes make it less reliable than the final target package.
- `Tri-Sentinel` — strong Robot ETB removal, but the deck already has substantial removal density and it did not create enough net improvement over the retained target suite.
- `Chameleon, Master of Disguise`, `Auton Soldier`, `Sakashima of a Thousand Faces` — copy options considered; `Spark Double` is the cleanest immediate nonlegendary Eggman duplicate for this exact list.
- `Darksteel Forge` — powerful but generically defensive, very expensive, and less commander-specific than the chosen upgrades.
- `Phyrexian Metamorph` — efficient copy card but less directly multiplicative than the final Eggman trigger package.
- `Chief of the Foundry` and other anthem effects — rejected because generic artifact-creature scaling is not the primary bottleneck.
- `Raiders' Wake` / additional discard punishment — rejected to avoid overcommitting to generic discard at the expense of the commander deployment engine.

## Final adversarial pass

A second full pass specifically challenged:

- every cast-only artifact payoff against Eggman's put-onto-battlefield wording;
- every selected copy/trigger-multiplier for redundancy;
- every low-impact Eggman target against current Construct/Robot/Vehicle alternatives;
- the 31-land structure after adding three unconditional/near-unconditional fixing upgrades;
- discard-payoff density versus artifact-target density;
- removal/protection density after all cuts.

`Mirrorworks`, `Torrential Gearhulk`, and `Ruin Grinder` were re-opened during this pass and rejected for the reasons above. No selected card was displaced.

**Closure result: ZERO NEW MATERIAL IMPROVEMENTS.**

## Candidate structure

- Total cards: **100**
- Distinct names: **97**
- Repeated names: `Island`, `Mountain`, `Swamp` only
- Lands: **31**
- Eggman-compatible Construct / Robot / Vehicle targets: **28**
- Commander color identity target: **B/R/U**
- Candidate SHA-256: `ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3`

## Power classification

**Bracket 4 — Optimized**  
Tags: **Villainous Choice / Robots / Artifact Cheat**

Final approval remains contingent on the SHA-bound fresh Oracle, rules, official Commander legality, color-identity, singleton, and 100-card complete gate. Explicit user approval is still required after that gate passes.
