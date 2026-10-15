# Tetsuo Umezawa — Whole-List Audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6`

## Baseline

Authoritative frozen source: `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`, member corresponding to `Tetsuo_Umezawa.txt`.

The baseline contains exactly 100 cards including Tetsuo. This current-cycle review treats that list as immutable source evidence and evaluates all 99 noncommander copies independently.

## Commander-first slot audit

**99/99 noncommander copies adjudicated: 85 KEEP / 14 CUT.**

### 14 cuts

1. Arcane Denial — replace two-mana permission that gives an opponent cards with free protection.
2. Feed the Swarm — replace sorcery-speed removal with instant-speed creature/enchantment interaction.
3. Nightscape Familiar — Tetsuo's initial `{U}{B}{R}` cost and `{U}{B}{B}{R}` activation contain no generic mana, so Familiar does not advance the commander's central mana demands.
4. Maeve, Insidious Singer — four-mana body plus three mana per goad loses to Puppeteer as a direct tap/untap engine.
5. Backlash — three mana for one tapped target loses to Blustersquall's efficiency and mass-tap ceiling.
6. Agitator Ant — opponents may decline its counters/goad; Flood supplies deterministic repeatable target access.
7. Spectacular Showdown — one-shot high-cost overload loses to repeatable Retreat to Coralhelm tap/untap.
8. Opposition Agent — powerful but generic stax; Sting, the Glinting Dagger directly gives haste and repeatedly untaps Tetsuo at the beginning of combat.
9. Dragonskull Summit — upgrade to Badlands.
10. Drowned Catacomb — upgrade to Underground Sea.
11. Shivan Reef — convert to premium fetch access.
12. Sulfurous Springs — convert to premium fetch access.
13. Underground River — convert to premium fetch access.
14. Island — convert one of six copies into Sink into Stupor // Soporific Springs while retaining five basics.

## Key keeps

- Aphetto Alchemist / Fatestitcher / Magewright's Stone / Minamo / Thousand-Year Elixir: direct repeat activations.
- Rings of Brighthearth / Illusionist's Bracers: activated-ability copying.
- Fumiko / Disrupt Decorum / Kardur / Firkraag / Karazikar / Red Death / Bloodthirsty Blade / Sly Instigator / Geode Rager / Bothersome Quasit / Vengeful Ancestor / Shiny Impetus: forced-combat shell.
- Frozen Aether: opposing creatures enter tapped and satisfy Tetsuo's tapped target condition.
- Propaganda: shapes forced/goaded combat without pretending attack costs must be paid.
- Verity Circle / Borrowing 100,000 Arrows: convert tapped opposing boards into cards.
- Royal Assassin: redundant tapped-creature removal that keeps the deck functional without Tetsuo.
- Lightning Greaves / Swiftfoot Boots: haste is unusually valuable because Tetsuo has a tap ability; keep both while Sting replaces a generic slot.

## Mana structure

Candidate: **35 front-face lands + 1 land-capable MDFC = 36 functional land-capable slots**.

Repeated Tetsuo activations specifically require U/B/B/R, so the fetch/dual changes improve colored pip access instead of cutting lands for generic colorless acceleration.

## Late challenger closeout — Sting, the Glinting Dagger

A final red-team pass after the original 13-swap draft identified Sting as a material commander-specific improvement. Equipped Tetsuo gets haste, then untaps at the beginning of each combat. That can reset Tetsuo during each player's combat step in a multiplayer rotation and creates additional activation windows without another mana payment for the untap itself. Because this is materially more commander-native than Opposition Agent, the old 13-swap SHA is superseded and must not be approved.

## Other red-team conclusions

- **Mana Vault rejected:** cannot pay any part of the commander's first U/B/R casting cost or U/B/B/R activation because neither contains generic mana.
- **War's Toll rejected:** redundant with Fumiko/Disrupt Decorum and introduces broader generic stax without enough commander-engine gain.
- **Thornbite Staff rejected:** seven mana to cast/equip before producing untaps is materially worse than the low-cost untap package.
- **Freed from the Real / similar Aura untappers rejected:** Tetsuo cannot be the target of Aura spells.
- **Tamiyo, the Moon Sage rejected:** five-mana setup loses to lower-cost tap engines.
- **Ghoulish Impetus / Parasitic Impetus rejected:** redundant one-creature goad Auras.
- **Norritt rejected:** can untap blue Tetsuo, but four-mana 1/1 and timing-constrained attack mode lose to three-mana Puppeteer's broader tap/untap flexibility.
- **Generic cEDH conversion rejected:** Thassa's Oracle/Ad Nauseam/Breach-style shells erase Tetsuo's natural identity.

## Closeout

Candidate exhaustion and adversarial red-team review: **ZERO NEW MATERIAL IMPROVEMENTS** beyond the proposed 14-card delta.

Natural ceiling: **Power Bracket 4 — Optimized**.
