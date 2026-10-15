# Tetsuo Umezawa — Whole-List Audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `53215af902bfab2640d80c4abb733e6fb66ddaea2de183ae7635d3f197890e72`

## Baseline

Authoritative frozen source: `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz`, member corresponding to `Tetsuo_Umezawa.txt`.

The baseline contains exactly 100 cards including Tetsuo. The prior project baseline and CSV/TXT reconciliation checks were PASS. This current-cycle review treats that list as immutable source evidence and evaluates all 99 noncommander copies independently.

## Commander-first slot audit

**99/99 noncommander copies adjudicated: 86 KEEP / 13 CUT.**

The deck's established untap/copy core is retained. The changes remove cards that are lower-efficiency versions of the same commander job, generic acceleration that does not help Tetsuo's colored costs, or clearly inferior mana slots.

### 13 cuts

1. Arcane Denial — replace two-mana permission that gives an opponent cards with free protection.
2. Feed the Swarm — replace sorcery-speed removal with instant-speed creature/enchantment interaction.
3. Nightscape Familiar — Tetsuo's initial `{U}{B}{R}` cost has no generic component, so Familiar does not reduce the commander's first cast; it also does not help `{U}{B}{B}{R}` activation.
4. Maeve, Insidious Singer — four-mana body plus three mana per goad is inefficient relative to a repeatable one-mana tap/untap activation.
5. Backlash — flavorful but three mana merely to create one tapped target and deal power to its controller; Blustersquall is dramatically more efficient and scales to the full opposing board.
6. Agitator Ant — opponents may simply decline the counters/goad; Flood supplies deterministic repeatable target access.
7. Spectacular Showdown — powerful at overload seven, but a one-shot goad/double-strike effect is less central than repeatable landfall tap/untap.
8. Dragonskull Summit — inferior to untapped typed Badlands.
9. Drowned Catacomb — inferior to untapped typed Underground Sea.
10. Shivan Reef — convert to premium fetch access.
11. Sulfurous Springs — convert to premium fetch access.
12. Underground River — convert to premium fetch access.
13. Island — convert one basic slot into Sink into Stupor // Soporific Springs while preserving a functional land slot.

## Key keeps

- Aphetto Alchemist / Fatestitcher / Magewright's Stone / Minamo / Thousand-Year Elixir: direct repeat activations.
- Rings of Brighthearth / Illusionist's Bracers: activated-ability copying.
- Fumiko / Disrupt Decorum / Kardur / Firkraag / Karazikar / Red Death / Bloodthirsty Blade / Sly Instigator / Geode Rager / Bothersome Quasit / Vengeful Ancestor / Shiny Impetus: forced-combat shell.
- Frozen Aether: opposing creatures enter tapped and immediately satisfy Tetsuo's tapped target condition.
- Propaganda: makes goaded/forced attackers prefer other opponents without requiring attack costs to be paid.
- Verity Circle / Borrowing 100,000 Arrows: convert the tapped-creature board state into cards.
- Royal Assassin: cheap redundant tapped-creature removal that keeps the deck functioning without Tetsuo.
- Lightning Greaves / Swiftfoot Boots: haste is unusually valuable because Tetsuo has a tap ability.
- Opposition Agent: retained as a high-impact interaction slot; no commander-specific challenger beat it without reducing overall deck strength.

## Mana structure

Candidate: **35 front-face lands + 1 land-capable MDFC = 36 functional land-capable slots**.

The revised land suite keeps the baseline's high land count because repeated Tetsuo activations are mana-intensive and specifically require U/B/B/R. The fetch/dual changes improve access to those colored pips rather than reducing lands for generic acceleration.

## Red-team conclusions

- **Mana Vault rejected:** cannot pay any part of the commander's first U/B/R casting cost or U/B/B/R activation because both lack generic mana; primarily helps commander tax and unrelated spells.
- **War's Toll rejected:** redundant with Fumiko/Disrupt Decorum and introduces a broader land-tapping stax effect without improving the activation engine enough to justify a slot.
- **Thornbite Staff rejected:** commander-specific in theory, but seven mana to cast/equip before producing untaps is materially worse than the retained low-cost untap package.
- **Freed from the Real / similar Aura untappers rejected:** Tetsuo cannot be the target of Aura spells.
- **Tamiyo, the Moon Sage rejected:** relevant but five-mana planeswalker is slower than the retained/enhanced one-to-three-mana tap engines.
- **Ghoulish Impetus / Parasitic Impetus rejected:** additional one-creature goad Auras are redundant with the existing forced-combat density.
- **Generic cEDH conversion rejected:** Thassa's Oracle/Ad Nauseam/Breach-style shells would raise generic power while erasing Tetsuo's natural identity.

## Closeout

Candidate exhaustion and adversarial red-team review: **ZERO NEW MATERIAL IMPROVEMENTS** beyond the proposed 13-card delta.

Natural ceiling: **Power Bracket 4 — Optimized**.
