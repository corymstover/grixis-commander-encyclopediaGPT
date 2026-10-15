# Sauron, Lord of the Rings — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #49 of 62  
Status: working audit; not user approval

Authoritative baseline: FINAL TXT member `Sauron__Lord_of_the_Rings.txt` from the frozen October 12 source package.

Candidate: `refinement/decklists/Sauron_Lord_of_the_Rings_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0`

## Audit result

- Commander: **Sauron, Lord of the Rings**.
- Noncommander copies adjudicated: **99/99**.
- Result: **87 KEEP / 12 CUT**.
- Baseline: **100 cards / 93 distinct names / 32 lands**.
- Candidate target: **100 cards / 96 distinct names / 32 lands**.
- Candidate repeats: **Nazgûl x4 / Swamp x2 only**.
- Singleton: **PASS target** — Nazgûl's own deck-construction text permits up to nine copies; only basic Swamp otherwise repeats.
- Commander color identity target: **U/B/R**.
- Project legality exception required: **NO**.
- Per-copy adjudication ledger: `refinement/decisions/Sauron_Lord_of_the_Rings_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final twelve-card delta

1. Knollspine Dragon -> Metamorphosis Fanatic
2. Notion Thief -> Mana Vault
3. In the Darkness Bind Them -> Grim Monolith
4. Stitch Together -> Dance of the Dead
5. Counterspell -> Force of Will
6. Crumbling Necropolis -> Volcanic Island
7. Drowned Catacomb -> City of Brass
8. Sulfurous Springs -> Flooded Strand
9. Underground River -> Marsh Flats
10. Island -> Misty Rainforest
11. Mountain -> Command Beacon
12. Swamp -> Phyrexian Tower

## Commander-first findings

- **Metamorphosis Fanatic** is unusually strong with Sauron: if Sauron's cast trigger returns the Fanatic, its ETB can return a second creature, converting one commander cast into a two-creature reanimation sequence.
- **Mana Vault** and **Grim Monolith** address the commander's defining constraint—an eight-mana casting cost—without forcing a commander-independent combo package.
- **Command Beacon** turns a taxed commander-zone Sauron into a hand cast. The hand cast still triggers Sauron's cast ability while avoiding commander tax on that cast.
- **Dance of the Dead** is deterministic two-mana reanimation and improves reliability over Stitch Together's threshold-dependent battlefield mode.
- **Force of Will** protects tap-out commander/reanimation turns better than holding up Counterspell.
- **Phyrexian Tower** is both a burst-mana land and a sacrifice outlet that has real interaction with Living Death and recursive creature lines.
- The land count stays at 32 while replacing slower/less flexible sources with fetches, premium fixing, Command Beacon, and Phyrexian Tower.
- The Ring/Nazgûl package is preserved: Call of the Ring, four Nazgûl, Sauron, the Dark Lord, The One Ring, The Black Gate, and other LOTR cards remain central.

## Source reconciliation

The current FINAL TXT is the decklist source of truth. Historical October 11 optimization and later full-62 review are supporting evidence only. The historical review already recognized the list as a dense reanimator shell and rejected adding slow high-cost theft/value cards without a clear role. This refinement therefore targets the commander's casting bottleneck and reanimation reliability rather than adding more expensive haymakers.

## Candidate exhaustion

Material challengers reviewed include Shelob, Dread Weaver; Treasure Nabber; Worn Powerstone; Wake the Dragon; Lord of the Nazgûl; Fact or Fiction; Deep Analysis; Decree of Pain; Incarnation Technique; Dread Return; Sepulchral Primordial; Chainer, Nightmare Adept; Intuition; Unmarked Grave; Avacyn, Angel of Horror; The Soul Stone; Geode Golem; Heartless Summoning; and additional generic combo conversions. None beats the selected configuration without slowing Sauron, diluting graveyard quality, or reducing commander identity.

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
