# Admiral Beckett Brass — Source Reconciliation and Quantitative Pass

**Cycle:** global-restart-2026-10-13. **Status:** PROVISIONAL / UNLOCKED.

## Critical source reconciliation

The frozen authoritative source is `GrixisFINALTXT60--2026.zip/Admiral_Beckett_Brass.txt`. The inherited `deck_card_audit.csv` does **not** describe the same exact card membership. Five cards in the frozen source but not the inherited audit are: Daring Piracy; Daring Saboteur; Dire Fleet Captain; Edward Kenway; Storm the Vault // Vault of Catlacan. Five inherited-audit cards not in the frozen source are: Captivating Crew; Departed Deckhand; Revel in Riches; Rogue's Passage; Spectral Sailor.

This is an audit-freshness discrepancy, **not** a reason to overwrite the frozen source. The five source-only cards and proposed additions are covered by the current project candidate-ranking metadata; Storm the Vault is a front-face enchantment, not a land, despite its transformed land back face.

## Exact provisional five-swap build

From the frozen source, and no other membership changes:

1. Coastal Piracy → The Indomitable.
2. Glint-Horn Buccaneer → Zephyr Singer.
3. Dire Fleet Neckbreaker → Kitesail Larcenist.
4. Captain Vargus Wrath → Slippery Scoundrel.
5. Shared Animosity → Open into Wonder.

Independent recount: 100 total; 97 distinct names; repeated cards only Island x3 and Mountain x2; 35 actual lands; 30 Pirate creatures; 65 nonland cards (including commander). Average mana value of nonland cards including commander is approximately 2.86; mana-value distribution: MV1=6, MV2=23, MV3=17, MV4=12, MV5=7. This is a descriptive curve, **not** a controlled mana-consistency simulation.

Provisional clean-list SHA-256: `0a5bb33006ffa2b1b9f2f9f26ea10a52a2c6e397a314000129a76b0509d54113`.

## Rules and role checks

Kitesail Larcenist is a flying Pirate with ward and a reversible ETB conversion of up to one other target artifact/creature per player into Treasure artifacts. Slippery Scoundrel becomes unblockable and hexproof only with the city's blessing. Open into Wonder is a sorcery, costs XUU, and makes X creatures unblockable with combat-damage draw for that turn; X=3 costs five mana. These effects directly support three distinct Pirate combat-damage connections to the same player, but the first two have sequencing/conditionality and the third is a one-shot.

Storm the Vault is not a land slot: its front face costs 2UR and creates one Treasure when one or more of your creatures deal combat damage to a player; it transforms at the beginning of your end step if you control five or more artifacts. The transformed land can generate blue mana based on artifact count. Retaining it supports a secondary Treasure engine but still warrants comparison against faster evasion or Pirate density.

## Evidence and remaining blockers

Metadata coverage exists for every name by combining the inherited audit and candidate-ranking file. **This is not the same as a fresh current-Oracle and legality check for all 100 cards.** Current card legality, double-faced card handling, mana-color source accounting, and final zero-new-material-improvement pass must still be independently verified before autonomous approval.

The inherited audit's membership mismatch must be documented rather than silently treating its 97/97 legality result as applying to the frozen source. No multiplayer win-rate claims are made.
