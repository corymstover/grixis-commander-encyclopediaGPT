# Norman Osborn // Green Goblin — Current-Cycle Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #43 of 62  
Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15

Exact candidate SHA-256: `23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2`

## Final 29-card delta

| Cut | Add | Decision basis |
|---|---|---|
| Anje's Ravager | Ad Nauseam | Combat-dependent three-mana refill becomes a premier instant-speed cEDH draw engine consistent with Norman's real Bracket-5 ceiling. |
| Archfiend of Ifnir | Artist's Talent | Five-mana discard payoff becomes a two-mana repeatable discard outlet; level 2 further reduces generic costs of noncreature graveyard spells. |
| Bone Miser | Attunement | Five-mana payoff becomes a reusable three-mana draw-three/discard-four engine with exceptional commander lift. |
| Burning Vengeance | Borne Upon a Wind | Incremental burn becomes a timing engine that lets mayhem-enabled spells obey flash timing for the rest of the turn. |
| Chainer, Nightmare Adept | Breakthrough | Four-mana creature recursion becomes a one-mana draw-four / mass-discard setup spell at X=0. |
| Emet-Selch of the Third Seat | Defense Grid | Redundant four-mana graveyard engine becomes efficient protection for proactive combo turns. |
| Glint-Horn Buccaneer | Final Fortune | Combat-oriented discard payoff becomes a compact extra-turn spell used by current cEDH Norman shells to force a decisive protected window. |
| Green Goblin, Nemesis | Ghostly Pilferer | Slow four-mana conditional discard interaction becomes a two-mana free discard outlet that is strongly Norman-specific and also draws from opponents' non-hand casts. |
| Kefka, Court Mage // Kefka, Ruler of Ruin | Gitaxian Probe | Five-mana discard value becomes zero-mana information/card velocity that improves tutor/combo sequencing. |
| Laughing Mad | Grim Monolith | Medium-rate flashback draw becomes deterministic two-mana acceleration for transform/combo turns. |
| Ledger Shredder | Grinding Station | Generic connive becomes a compact Underworld Breach engine piece that also converts zero-mana artifacts into self-mill. |
| Lightning Greaves | Imperial Seal | Low-value commander protection/evasion becomes one-mana tutor consistency. |
| Likeness Looter | Into the Flood Maw | Tap-speed looting becomes one-mana broad bounce interaction with strong cEDH adoption. |
| Magmakin Artillerist | Mox Amber | Three-mana discard burn becomes zero-mana colored acceleration enabled by the legendary commander. |
| Monument to Endurance | Pyroblast | Slow discard payoff becomes one-mana stack interaction in a blue-heavy cEDH field. |
| Reanimate | Reckless Handling | Generic creature recursion becomes a two-mana artifact tutor that also randomly discards, directly connecting tutor access to mayhem setup. |
| Secrets of the Dead | Simian Spirit Guide | Three-mana incremental grave-cast draw becomes zero-card-board-state burst red mana for turbo turns. |
| Skirge Familiar | Tolarian Winds | Five-mana discard outlet becomes two-mana instant-speed hand cycling with very high Norman-specific lift. |
| Surly Badgersaur | Valley Floodcaller | Four-mana discard payoff becomes a three-mana flash creature that gives all noncreature spells flash, materially expanding mayhem timing. |
| Ultimate Green Goblin | Arid Mesa | Slow upkeep engine becomes a premium typed-dual fetch while the land count is deliberately increased by one overall. |
| Exotic Orchard | Cavern of Souls | Broad fixing becomes commander protection; naming Human can make the front-face Norman Osborn creature spell uncounterable. |
| Luxury Suite | City of Traitors | Multiplayer dual becomes explosive two-mana land for proactive cEDH sequencing. |
| Morphic Pool | Flooded Strand | Multiplayer dual becomes premium typed-dual fetch. |
| Oscorp Industries | Gemstone Caverns | Flavorful tapped land becomes high-ceiling pregame acceleration; Bracket-5 tempo outweighs Oscorp's unique Mayhem land recursion. |
| Shivan Reef | Marsh Flats | Painland becomes premium typed-dual fetch. |
| Sulfur Falls | Misty Rainforest | Checkland becomes premium typed-dual fetch. |
| Sulfurous Springs | Verdant Catacombs | Painland becomes premium typed-dual fetch. |
| Training Center | Volcanic Island | Multiplayer dual becomes untapped fetchable U/R dual. |
| Underground River | Wooded Foothills | Painland becomes premium typed-dual fetch. |

## Commander-specific rate changes

Green Goblin's cost reduction applies to spells cast from the graveyard and reduces `{2}` of generic mana. Mayhem supplies the permission/alternative cost; normal timing still applies.

Consequences used in slot evaluation:

- **Big Score:** if discarded this turn while Green Goblin is active, its mayhem cost `{3}{R}` is reduced to `{1}{R}`; its additional discard cost still must be paid. With Artist's Talent at level 2, the remaining generic mana can also be reduced, leaving `{R}`.
- **Dark Deal:** if discarded this turn, its mayhem cost `{2}{B}` becomes `{B}` under Green Goblin.
- **Unstable Experiment:** if discarded this turn, `{1}{U}` becomes `{U}` under Green Goblin, producing a draw plus connive effect from the graveyard.
- **Shadow of the Goblin:** remains both a discard outlet and a payoff for spells cast outside the hand, including mayhem/graveyard casts.

These cards are intentionally retained despite lower raw inclusion than some generic Grixis staples because the commander changes their actual rate and function.

## Timing package

Mayhem does not override timing restrictions. Two additions specifically address that limitation:

- **Borne Upon a Wind** lets the controller cast spells that turn as though they had flash.
- **Valley Floodcaller** lets noncreature spells be cast as though they had flash, including spells another effect allows from non-hand zones.

This prevents a card discarded on an opponent's turn from being stranded merely because it is a sorcery or other normally sorcery-speed noncreature spell.

## Compact win package

### Thassa's Oracle + Consultation / Tainted Pact

The list retains Thassa's Oracle, Demonic Consultation, and Tainted Pact. The candidate contains **100 distinct card names**, so Tainted Pact has no duplicate-name stopping point created by deck construction.

### Underworld Breach + LED + Brain Freeze

The classic Breach line remains. Green Goblin can additionally reduce the generic component of Brain Freeze when it is cast from the graveyard, but the line does not depend on the commander to function.

### Underworld Breach + Grinding Station + Mox Amber

Grinding Station can sacrifice Mox Amber to mill three cards. Underworld Breach can then allow Mox Amber to be escaped for zero mana by exiling three other graveyard cards; the artifact re-entering untaps Grinding Station. With Norman/Green Goblin on the battlefield, Mox Amber can produce colored mana before being sacrificed. The loop is treated as a self-mill/mana engine whose exact starting graveyard resources and finishing line matter; the documentation does **not** claim the three cards alone always create a resource-free deterministic win from an empty graveyard.

## Candidate exhaustion — notable rejected alternatives

- **Necropotence — REJECT despite high generic cEDH inclusion.** Whenever you discard, Necropotence triggers and attempts to exile that card from your graveyard when the trigger resolves. Because mayhem still obeys timing rules, this sharply interferes with the normal sorcery-speed discard-then-cast pattern: sorcery-speed mayhem cards usually cannot be cast while the Necropotence trigger is waiting on the stack. Instant-speed or flash-enabled lines can sometimes use the card before that trigger resolves, so the interaction is tension rather than an absolute prohibition. The commander-first build still rejects Necropotence because it systematically works against the intended graveyard resource loop.
- **Skirge Familiar — REJECT at final slot stage.** It has genuine Norman-specific lift and becomes cheaper if itself discarded and mayhem-cast, but five mana from hand / three after Green Goblin is too slow once the final list has many cheaper discard outlets.
- **Kefka, Court Mage — REJECT at final slot stage.** Tournament-playable and synergistic, but five mana loses the slot competition to one-/two-mana setup and compact cEDH infrastructure.
- **Chainer, Nightmare Adept — REJECT.** Strong commander lift is acknowledged, but four-mana creature-only recursion is slower than the final graveyard plan.
- **Secrets of the Dead — REJECT.** Exact commander text synergy, but three mana with no immediate effect is too slow at Bracket 5.
- **The One Ring — REJECT.** Strong generic draw, but four mana and no commander-specific graveyard/discard role; Remora/Rhystic/Ad Nauseam and native discard engines are preferred.
- **Mnemonic Betrayal — REJECT at final slot stage.** Powerful generic graveyard burst, but not more necessary than the finalized commander-native discard/timing package.
- **Diabolic Intent — REJECT at final slot stage.** Efficient tutor, but the deck already contains very high tutor density and does not want to increase dependence on expendable creatures.
- **Force of Negation — REJECT at final slot stage.** Strong, but stack-interaction density is already high; another free counter would displace a commander-native engine.
- **Putrid Imp — REJECT.** Free discard is relevant, but final outlet density is already sufficient and Ghostly Pilferer/Artist's Talent/Attunement provide more value.
- **Firestorm — REJECT.** Discards are useful, but target-count constraints and card disadvantage make it less reliable than the chosen outlets.
- **Bazaar of Baghdad — REJECT.** Powerful discard/draw engine but produces no mana; a 23-land turbo shell cannot comfortably give up another colored/mana-producing land slot.
- **Cephalid Coliseum — REJECT.** Strong threshold utility, but color/life/sacrifice requirements lose to the premium fetch/turbo-land configuration.
- **Urza's Saga — REJECT.** Excellent artifact tutor land, but colorless production and self-sacrifice create tension in an extremely color-intensive U/B/R turbo shell.
- **Oscorp Industries — REJECT after commander-first review.** Its own mayhem is flavorful and unique, but entering tapped is too costly at the natural cEDH ceiling.
- **Additional generic Oracle/Consultation or Breach redundancies — REJECT where they displaced identity pieces.** The deck already has compact generic wins; further homogenization is unnecessary.

## Mana-base red team

The authoritative baseline has 22 lands. The candidate deliberately rises to **23 lands** rather than cutting further.

Final lands:

- Ancient Tomb
- Arid Mesa
- Badlands
- Blood Crypt
- Bloodstained Mire
- Cavern of Souls
- City of Brass
- City of Traitors
- Command Tower
- Flooded Strand
- Gemstone Caverns
- Mana Confluence
- Marsh Flats
- Misty Rainforest
- Otawara, Soaring City
- Polluted Delta
- Scalding Tarn
- Steam Vents
- Underground Sea
- Verdant Catacombs
- Volcanic Island
- Watery Grave
- Wooded Foothills

The mana package also adds Mox Amber, Grim Monolith, and Simian Spirit Guide while retaining the existing fast mana. Cavern of Souls naming **Human** can make the front-face Norman Osborn creature spell uncounterable; the Green Goblin back face is not separately cast.

## Final red-team result

The final pass challenged all 29 swaps, low-inclusion identity pieces, current tournament Norman shells, interaction density, compact win density, graveyard timing, fast mana, all 23 lands, and the temptation to restore Necropotence or generic high-power cards at the expense of Mayhem.

No challenger produced a material improvement without a greater cost in speed, commander dependence, mana quality, or internal graveyard synergy.

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Decision closeout: PASS — candidate is APPROVAL_READY evidence only, not approved/locked.**

## Approval closeout

- Explicit user approval received: **2026-10-15**
- Canonical approved SHA-256: `23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2`
- Exact approved artifact: `refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt`
- Current-cycle state: **APPROVED / LOCKED**
- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + approval-ready verification**
- Next unlocked deck in tracker order: **Obeka, Brute Chronologist (index 43 / deck 44 of 62)**.
