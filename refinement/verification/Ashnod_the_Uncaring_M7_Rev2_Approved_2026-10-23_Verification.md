# Ashnod M7 Rev2 — bounded approval-ready verification and exact-source handoff

Expected raw SHA-256: `a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761`; historical approved raw SHA-256: `f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf`. No alteration to historical source exports or saved Grok five-swap proposal.

## Official legality and mechanics

- Source: engineering PR #681 immutable exact head `c7b907d4aecc97513a6ce3c28ed107aecd5a3be9`, engineering selected Oracle snapshot (95 names, 100 physical). Current as of October 23, 2026; zero differences were reported relative to research archive for selected names.
- 95 distinct card names, 100 physical cards, one Ashnod commander, 33 lands, 8 rocks/ramp including the one-use Lotus Petal, Island 3 / Mountain 2 / Swamp 3, correct singleton.
- Every selected card has current Oracle ID/text, official Commander legality `legal`, UBR-subset color identity; no documented project exceptions are needed for Ashnod.
- Six unchanged Game Changers: Ancient Tomb, Bolas's Citadel, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor. Bracket 4 — Optimized.
- Ashnod's nonmana artifact/creature activated-ability copy applies to **cost sacrifices**, not sacrifices performed upon resolving another ability, mana abilities or abilities of ordinary lands.
- Existing Rings of Brighthearth or Forensic Gadgeteer with added Basalt Monolith permits colorless infinite mana, with activation/seeding and protection caveats. Walking Ballista remains as direct outlet.
- Added Animation Module completes three previously almost-included archived Spellbook lines. Spawning Pit's loop is independently reasoned from Oracle with a starting creature and first-mana caveat, not attributed to Spellbook.
- Ruthless Knave's first copied sacrifice activation creates four Treasures; its separate sacrifice-three-treasures card-draw activation is also doubled, but retains real token cost. Priest's ability targets players and therefore is not a mana ability.

## Source-bound engineering test evidence

- `corymstover/GrokBotMTGCompanion` PR #681, head `c7b907d4aecc97513a6ce3c28ed107aecd5a3be9`: exact-head Actions run #40048290216 **SUCCESS**, new Rev2 methods 9/9, older #654 methods 29/29.
- Separate Rev2 M6 I/J source-bound certificate and strict bundle validated, eight complete 100-card comparisons. These are finite deterministic evidence; neither full-game modeling nor a mathematical proof of absolute optimality.
- Hypergeometric source-card access proxy among first 11 of 99: 42/99 baseline yields 53.74%; Grok first-pass 40/99 yields 47.89%; Rev2 41/99 yields 50.83%. Lotus Petal and Basalt are not ordinary repeatable on-curve mana; results are not commander cast probabilities or win rates.

## Canonical side effects permitted

New exact approved Ashnod file, owner receipt, audit evidence, Ashnod-only override entry, tracker row #6, source-bound regression test and approval workflow. No other canonical 100-card deck, older historical approval or owner status changed. CI success does not substitute for explicit owner approval; Cory's approval is separately recorded in the companion receipt.

**Post-merge operator action:** fetch canonical `main`, independently recompute raw SHA, verify registry approved/locked and tracker exact hash, verify five earlier current-cycle M7 SHA locks, and retain October 13 historical artifact unchanged.
