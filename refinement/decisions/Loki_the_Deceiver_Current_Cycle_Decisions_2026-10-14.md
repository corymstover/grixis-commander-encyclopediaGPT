# Loki, the Deceiver — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Tracker deck id: `Loki__the_Deceiver`  
Authoritative source TXT: `Grixis_Commander_Encyclopedia_Current_Source_Package_2026-10-12 / 02_Current_Decklists/TXT/Loki__the_Deceiver.txt`  
Authoritative source TXT SHA-256: `21fbcd51f4798153c6d4cee4b63d9679589d943d75253273769a686199abf3f7`  
Normalized current-cycle baseline SHA-256: `fc260af83f9da4d5f0460f2e88b1cd8103f777c92366532a2800bfda149bc223`  
Approval-candidate SHA-256: `5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062`

## Source reconciliation

The October 12 current source package is authoritative. It contains exactly 100 cards across 95 distinct names/source rows, including 34 lands and Loki as the sole commander. The older v8.1.4 `deck_card_audit.csv` is supporting research only and is not used to overwrite current membership. In particular, the current source contains `Construct a Cosmic Cube`, `Cover of Darkness`, `Killmonger, Ruthless Usurper`, `Stilt-Man, Towering Terror`, and `Venom, Eddie Brock`, while the historical audit instead contained `Ares, God of War`, `Counterspell`, `Impostor Syndrome`, `Kindred Dominance`, and `Withering Torment`.

## Commander blueprint and natural ceiling

**Identity:** Villain-copy combat value. Loki should attack safely, clone the highest-value Villain for the combat, exploit enters/static/combat-damage text on the copied body, and convert connecting Villains into cards. Temporary-token preservation (`The Master, Multiplied`, `Sundial of the Infinite`), Villain ETB/death payoffs, evasion, and copy/typal support are identity infrastructure.

**Rules constraint:** a creature put onto the battlefield tapped and attacking was not declared as an attacker. Therefore an attack-trigger-only Villain is materially worse as a Loki copy target than an enters/static/combat-damage Villain. Candidate evaluation was weighted accordingly.

**Natural ceiling:** **Power Bracket 4 — Optimized.** Current community evidence shows a meaningful optimized Loki population but only a minimal user-labeled cEDH sample. The candidate keeps premium Grixis interaction and mana while refusing to replace the Villain-copy engine with a generic Oracle/Breach turbo shell.

## Exact proposed changes — three swaps

### 1. `Construct a Cosmic Cube` → `Red Ghost, Intangible Genius`

`Construct a Cosmic Cube` is a three-mana Plan that pays off the second card drawn each turn with 2/1 Villain tokens and slowly accumulates toward its seven-counter control effect. `Red Ghost` costs one more mana but is itself an unblockable Villain, has ward {2}, and creates a **3/3 red Ape Villain with haste** whenever the second card of a turn is drawn. Loki's combat-damage draw naturally helps turn on that trigger. Red Ghost also increases the density of legal Loki copy targets and reliable combat-damage enablers rather than occupying a noncreature payoff slot.

### 2. `The Masters of Evil` → `Titan of Littjara`

`The Masters of Evil` is a six-mana +2/+1 Villain anthem whose discard mode tutors a Plan. After the Cube cut, that tutor package becomes even narrower, while other anthem/evasion infrastructure remains. `Titan of Littjara` is a six-mana 6/6 that may choose **Villain** as it enters and then loots based on the number of other creatures sharing that type whenever it enters or attacks. Most importantly, a Loki token copying Titan receives Titan's own as-enters creature-type choice and its enters trigger, making Titan one of the strongest commander-specific copy targets in the available pool.

### 3. `Reliquary Tower` → `Hall of Echoes`

Both occupy a colorless utility-land slot, so the swap preserves the 34-land count and does not worsen colored-source density relative to baseline. Hall can become a copy of Loki before combat while suppressing the legend rule for the turn. If Hall has been under our control continuously since the beginning of the turn, the Hall-Loki can attack alongside the original Loki and produce a second Loki attack trigger. The land does not enter the battlefield when it becomes a copy, so enters abilities are not falsely credited to Hall itself.

## Whole-list audit / rejected material challengers

Every inherited slot was challenged against the commander blueprint rather than protected by baseline status. The following close calls were rejected after the second pass:

- `Kindred Dominance` over `Blasphemous Act`: the one-sided Villain wipe is more thematic, but seven mana is not a clear strict upgrade over the frequently one-to-three-mana emergency reset in a 34-land optimized list. `Toxic Deluge` already provides a second flexible reset. No swap.
- `Raise the Palisade`: cheaper asymmetric typal interaction than Kindred Dominance, but temporary bounce is not a material improvement over the selected removal suite. No swap.
- `Endless Ranks of HYDRA`: good recurring Villain production, but `Avengers: Under Siege` already supplies multiple Villains, a tribal/nontribal damage chapter, and a Treasure conversion chapter. Improvement is not large enough to force a fourth change.
- `Puppet Master, String Puller`, `Vulture, Scheming Scavenger`, and other attack-trigger-centric Villains: a Loki-created copy enters attacking and therefore does not retrigger an ability that specifically triggers when that copied creature attacks. Their ranking overstates their value as Loki copy targets.
- Generic `Thassa's Oracle` / `Demonic Consultation`, fast-combo, and sacrifice-loop packages: strong Grixis cards, but they raise generic combo density more than they strengthen Loki's own Villain-copy game plan. Rejected under no-forced-homogenization.
- Additional clone effects: `Spark Double`, `Taskmaster, Mercenary Mimic`, `Mysterio, Master of Illusion`, `Chameleon, Master of Disguise`, `Loki, Lord of Misrule`, and commander-copy infrastructure already supply substantial copy density. No extra clone displaced a weaker commander-specific slot after the three accepted swaps.

## Structural closeout before complete gate

The exact candidate is **100 cards / 95 distinct names / 34 lands**. Only basic `Island`, `Mountain`, and `Swamp` repeat. The candidate preserves the baseline's high Villain density; Red Ghost replaces a noncreature and Titan can enter as a Villain, while only `The Masters of Evil` leaves the printed Villain suite.

After baseline reconciliation, commander-blueprint review, current candidate-rank challenge, current Marvel/Reality Fracture release review, optimized-community comparison, mana-base challenge, removal challenge, attack-trigger rules red-team, and a second pass that rejected a forced fourth swap, there are **ZERO NEW MATERIAL IMPROVEMENTS** remaining under the project's commander-first stopping standard.

The candidate remains **NOT APPROVED** pending the exact SHA-bound complete fail-closed Oracle/color-identity, official Commander legality, rules, structural, and singleton gate plus explicit user approval.
