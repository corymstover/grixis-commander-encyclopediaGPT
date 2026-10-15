# Sedris, the Traitor King — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #51 of 62  
Status: working audit; not user approval

Authoritative baseline: FINAL TXT member `Sedris__the_Traitor_King.txt` from the frozen October 12 source package.

Candidate: `refinement/decklists/Sedris_the_Traitor_King_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365`

## Audit result

- Commander: **Sedris, the Traitor King**.
- Noncommander copies adjudicated: **99/99**.
- Result: **91 KEEP / 8 CUT**.
- Baseline: **100 cards / 99 distinct names / 31 lands**.
- Candidate target: **100 cards / 99 distinct names / 31 lands**.
- Candidate repeats: **Swamp x2 only**.
- Singleton: **PASS target** — only a basic land repeats.
- Commander color identity target: **U/B/R**.
- Project legality exception required: **NO**.
- Per-copy adjudication ledger: `refinement/decisions/Sedris_the_Traitor_King_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final eight-card delta

1. Counterspell -> Force of Will
2. Underworld Breach -> Ripples of Undeath
3. Fellwar Stone -> Grim Monolith
4. Blightstep Pathway // Searstep Pathway -> Badlands
5. Clearwater Pathway // Murkwater Pathway -> Flooded Strand
6. Riverglide Pathway // Lavaglide Pathway -> Misty Rainforest
7. Fabled Passage -> Marsh Flats
8. Bojuka Bog -> Undercity Sewers

## Commander-first findings

- **Ripples of Undeath** supplies repeatable first-main-phase self-mill and optional card selection, directly feeding Sedris's graveyard resource every turn. It replaces Underworld Breach, whose escape costs consume the same graveyard Sedris wants populated.
- **Force of Will** protects six-mana Sedris and large unearth/reanimation turns without reserving {U}{U}; the final gate must independently verify a sufficient blue pitch pool.
- **Grim Monolith** converts the weakest generic two-mana rock slot into burst acceleration toward Sedris's six-mana commander cost. It is not being used to force a separate Monolith combo package.
- **Undercity Sewers** is fetchable as both Island and Swamp and surveils on entry, making its tapped-land cost commander-positive rather than merely a tempo loss.
- **Badlands plus three additional fetchlands** materially improve the premium typed-dual manabase while preserving exactly 31 lands.
- **Obeka, Brute Chronologist; Sundial of the Infinite; Teferi's Veil; Deadeye Navigator; Panharmonicon; Convergence of Dominion; River Kelpie; Twilight Diviner; and the Deadeye Navigator + Peregrine Drake package are all preserved.**

## Source reconciliation

The frozen FINAL TXT is decklist truth. Historical October 11 work is supporting evidence only. That prior pass correctly established Convergence of Dominion, River Kelpie, Corpse Connoisseur, Metamorphosis Fanatic and Twilight Diviner as strong Sedris-specific additions, and the later full-62 review correctly rejected Embalmer's Tools as redundant once Convergence already reduces Sedris-granted unearth to the one-mana floor. This refinement therefore leaves those decisions intact and addresses different weaknesses: graveyard setup quality, tap-out protection, commander acceleration, and mana-base efficiency.

## Candidate exhaustion

Material challengers reviewed include Embalmer's Tools; Phyrexian Delver; Bladewing, Deathless Tyrant; Diluvian Primordial; Ancient Brass Dragon; Gravebreaker Lamia; Mulldrifter; Obsessive Stitcher; Combustible Gearhulk; Noxious Gearhulk; Stitch Together; Grave Researcher // Reanimate; Conjurer's Closet; Thassa, Deep-Dwelling; Ghostly Flicker; Wonder; Altar of Dementia; Incarnation Technique; Tomb Fortress; Dance of the Dead; Curse-Marred Demon; and generic Oracle/Breach combo conversion.

- **Embalmer's Tools:** rejected as redundant. Convergence already reduces Sedris's {2}{B} unearth to {B}; another reducer cannot push that activation below one mana.
- **Phyrexian Delver:** strong commander-compatible reanimation body, but no creature slot clears the bar. Dread Return remains valuable because it can be milled and cast from the graveyard, while the current creature suite has stronger immediate ETB/attack outputs.
- **Bladewing / Ancient Brass Dragon / Diluvian Primordial:** powerful unearth targets, but combat dependence or opponent-resource dependence does not displace Archon, Rune-Scarred/Burning-Rune Demon, Massacre Wurm, Sepulchral Primordial, Jin-Gitaxias, Etali, Grave Titan, or Metamorphosis Fanatic.
- **Conjurer's Closet / Thassa / Ghostly Flicker:** legitimate unearth-rescue cards, but the baseline already has Obeka, Sundial, Teferi's Veil and Deadeye Navigator. A fifth rescue package is less valuable than repeatable graveyard setup.
- **Wonder:** attractive evasion from the graveyard, but this deck earns more from ETB/reanimation value than from adding another combat dependency.
- **Curse-Marred Demon:** current 2026 card and a legal Sedris target, but its tutor-plus-random-discard ETB does not beat the deterministic tutor package already present.
- **Generic Oracle/Breach conversion:** rejected under no-forced-homogenization; Sedris remains an unearth/reanimation deck rather than a Grixis graveyard shell with Sedris in the command zone.

After the full 99-copy audit, current-card challenger review, optimized-Sedris comparison, mana-base red team, graveyard-resource review, unearth-rescue redundancy review and generic-combo homogenization challenge:

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
