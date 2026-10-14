# Admiral Beckett Brass — Card-by-card legality and Oracle provenance (pass 5)

Status: **NOT YET LOCKABLE**. Frozen baseline remains unchanged; exact five-swap proposed list SHA-256 `0a5bb33006ffa2b1b9f2f9f26ea10a52a2c6e397a314000129a76b0509d54113`.

## Independently recounted structure

100 total cards across 97 card-name rows; 35 lands; 65 nonland cards including commander; 32 creatures including commander; 30 Pirate creatures including commander; no nonbasic repeats. Nonland mana-value distribution: MV1=6, MV2=23, MV3=17, MV4=12, MV5=7; average MV 2.8615 (X counted as 0 for Open into Wonder).

## Oracle and legality provenance

The original project audit supplies `effective_commander_legality=legal` and `color_identity_check=pass` for **87** of the proposed 97 distinct card names. The other **10** names were checked against accessible contemporary MTG.WTF card records with Commander legalities and their Oracle text:

- Daring Piracy (J22/33) — red enchantment, 1/1 menace/haste Pirate token at combat, exiled next end step.
- Daring Saboteur (LCC/151) — blue Pirate, 2U unblockability activation.
- Dire Fleet Captain (XLN/221) — black/red Pirate, attack power increase.
- Edward Kenway (ACR/143) — UBR Pirate, end-step Treasure creation from tapped Pirates/Assassins/Vehicles.
- Storm the Vault (RIX/173a) — UR enchantment front face, not a land slot; back face Vault of Catlacan is a land.
- The Indomitable (LCC/75) — blue legendary Vehicle; 2UU, combat-damage draw and conditional graveyard cast.
- Zephyr Singer (MOM/86) — blue flying/vigilant Pirate; convoke and flying counters.
- Kitesail Larcenist (LCI/61) — blue flying Pirate; targeted temporary Treasure conversion.
- Slippery Scoundrel (RIX/55) — blue Pirate; ascend-dependent hexproof/unblockability.
- Open into Wonder (AKH/64) — blue sorcery; XUU and X unblockable creatures for the turn.

All ten individual records report Commander legal. No metadata color identity falls outside UBR. This resolves the **five missing-source names** in the inherited audit without pretending the inherited audit matched the source.

**Limit:** the other 87 names still rely on the prior v8.1.4 legality/Oracle snapshot, not a fresh independent October 13 Oracle lookup for every one. Do not label full current Oracle gate VERIFIED until that refresh (or documented equivalent) is complete.

## Strategic next decision

Compare the three remaining provisional weak retains (Bident of Thassa, Fiery Cannonade, Storm the Vault) against current commander-specific alternatives and the full package structure. A zero-new-material-upgrade pass must be demonstrated, not asserted. Mana-color source adequacy and opening-hand risk remain to be quantified.

No deck state transition or lock is authorized until these checks close.
