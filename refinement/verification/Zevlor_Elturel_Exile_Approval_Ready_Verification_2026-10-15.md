# Zevlor, Elturel Exile — Approval-Ready Verification — 2026-10-15

## State and authoritative baseline
- Cycle: `global-restart-2026-10-13`.
- Tracker position: index 61 / deck 62 of 62.
- Current project completion before Zevlor approval: **61/62 APPROVED / LOCKED**.
- Authoritative baseline: `GrixisFINAL2--2026.zip::Zevlor__Elturel_Exile.csv` reconciled with `GrixisFINALTXT2--2026.zip::Zevlor__Elturel_Exile.txt`.
- Baseline structural count: 100 cards / 96 distinct names / 34 lands; only Island x3, Mountain x2, Swamp x2 repeat.
- The older v8.1.4 `deck_card_audit.csv` Zevlor configuration differs from FINAL2 and is treated as historical/supporting research, not the baseline.

## Commander blueprint
Current Oracle text:
> Haste
> {2}, {T}: When you next cast an instant or sorcery spell that targets only a single opponent or a single permanent an opponent controls this turn, for each other opponent, choose that player or a permanent they control, copy that spell, and the copy targets the chosen player or permanent.

Commander rewards:
1. Instants/sorceries with exactly one chosen target, where that target is an opponent or a permanent an opponent controls.
2. Payloads whose non-targeted effects are valuable on every copied resolution.
3. Target-opponent theft/control/discard spells that become table-wide through Zevlor.
4. Cheap ways to pay, reduce, copy, or repeat Zevlor's activated ability.
5. Magecraft engines that explicitly trigger when spells are **cast or copied**.

Natural ceiling: **Power Bracket 4 — Optimized**. A generic Grixis cEDH Oracle/Consultation/Breach shell can contain Zevlor, but those wins do not require the commander. The commander-first optimized build instead maximizes target-copy payloads and activation reuse without forcing Zevlor into a commander-independent cEDH shell.

Suggested Archidekt tags: **Targeted Spells / Spell Copy / Theft-Control**.

## Whole-list audit
- 99/99 noncommander copies individually adjudicated in `Zevlor_Elturel_Exile_Whole_List_Audit_2026-10-15.csv`.
- Result: **78 KEEP / 21 CUT**.
- 21 one-for-one additions; candidate remains exactly 100 cards.
- Project top-100 candidate pool fully adjudicated.
- Meaningful outside-ranked candidates reviewed, including Force of Will, Pemmin's Aura, Swiftfoot Boots, premium fetchlands, Freed from the Real, Aphetto Alchemist, Rings of Brighthearth, additional untap artifacts, and generic cEDH packages.
- Final adversarial pass after the last Pemmin's Aura/fetchland corrections: **ZERO NEW MATERIAL IMPROVEMENTS**.

## Exact proposed changes
1. Arcane Bombardment -> Cruel Ultimatum
2. Arcane Denial -> Force of Will
3. Dauthi Voidwalker -> Rakdos Charm
4. Dualcaster Mage -> Illusionist's Bracers
5. Increasing Vengeance -> Omen Hawker
6. Ioreth of the Healing House -> Pemmin's Aura
7. Izzet Signet -> Patriar's Seal
8. Nightscape Familiar -> Acquire
9. Reverberate -> Great Intelligence's Plan
10. Stolen Goods -> River's Rebuke
11. The One Ring -> Portent
12. Lightning Greaves -> Swiftfoot Boots
13. Crumbling Necropolis -> City of Brass
14. Drowned Catacomb -> Marsh Flats
15. Shipwreck Marsh -> Misty Rainforest
16. Shivan Reef -> Arid Mesa
17. Stormcarved Coast -> Flooded Strand
18. Sulfur Falls -> Volcanic Island
19. Sulfurous Springs -> Verdant Catacombs
20. Underground River -> Wooded Foothills
21. Island -> Minamo, School at Water's Edge

## Oracle / rules red-team
- Wizards' Commander Legends: Battle for Baldur's Gate release notes confirm Zevlor's Oracle correction adds **"only"**. A spell with multiple chosen targets does not trigger Zevlor even if one target qualifies. A spell capable of multiple targets does qualify if exactly one target was actually chosen as it was cast.
- Zevlor's copies are created on the stack and are not cast. Cast-only triggers do not trigger from those copies; magecraft abilities worded "cast or copy" do.
- Zevlor's delayed trigger can copy the qualifying spell even if the original has already been countered when the delayed trigger resolves.
- Modal spell copies keep the original mode(s), copied X values remain the same, and additional costs paid for the original are treated as paid for the copies.
- Multiple Zevlor activated abilities resolved before a qualifying spell create independent delayed triggers. The same next qualifying spell is the "next" spell for each of them, so all trigger on that cast.
- **Illusionist's Bracers** copies Zevlor's nonmana activated ability. The copied activated ability and original resolve separately, each creating its own delayed trigger.
- **Twinning Staff** is a replacement effect. If a Zevlor delayed trigger would copy a spell one or more times, Staff creates one additional copy for that copy event; it does not recursively trigger itself.
- **Training Grounds** reduces Zevlor's {2} activation to {1}, respecting the minimum-one-mana rule.
- **Omen Hawker** adds {C}{U} restricted to activating abilities; because Zevlor's activation requires generic {2}, that mana can pay the entire activation.
- **Pemmin's Aura** can untap enchanted Zevlor repeatedly for {U} in the same turn. Its own untap ability does not target. Its {U} shroud ability can protect Zevlor; while shroud is active, external targeted untap effects such as Minamo or Patriar's Seal cannot target Zevlor.
- **Swiftfoot Boots** is deliberately used instead of Lightning Greaves: hexproof stops opponents' targeting but still permits the controller's Minamo/Patriar's Seal and Aura interactions. Greaves' shroud would block those targets.
- **Minamo, School at Water's Edge** and **Patriar's Seal** each legally target and untap Zevlor because it is a legendary creature/permanent.
- **Jeska's Will** qualifies when both modes are chosen while controlling Zevlor: it has exactly one target opponent. Zevlor's copies retain both chosen modes, so each copy can generate mana from a different opponent and exile three additional cards from the controller's library.
- **Rakdos Charm** qualifies in its first mode (target player's graveyard) and second mode (target artifact), allowing Zevlor to scale those modes across opponents. Its third mode has no target and does not trigger Zevlor.
- **Cyclonic Rift** qualifies in normal single-target mode. If overloaded, overload replaces "target" with "each", so it no longer targets and does not trigger Zevlor.
- **Cruel Ultimatum** targets one opponent. At a four-player table, one Zevlor activation produces one resolution aimed at each opponent: each opponent sacrifices/discards/loses 5, while the controller can draw nine total cards and gain 15 life across the three resolutions.
- **Great Intelligence's Plan** targets one opponent and draws three before the villainous choice. Three resolutions draw nine total cards. A player may choose a villainous-choice option even if that option is impossible.
- **River's Rebuke** targets one player, so Zevlor can create copies aimed at the other opponents and produce a one-sided table-wide nonland bounce sequence.
- **Acquire** targets one opponent, allowing a Zevlor copy for each other opponent and potentially putting one artifact from each opponent's library onto the battlefield under your control.
- **Portent** targets one player. Each resolving spell/copy creates its own delayed draw trigger for the controller at the beginning of the next turn's upkeep, so three resolutions yield three delayed draws.
- **Blue Sun's Twilight**, **Electrodominance**, **Rakdos's Return**, and other X spells retain the original X value on Zevlor copies.
- **Worst Fears** remains a high-end identity finisher: one Zevlor activation can create one resolution for each opponent, allowing control of each opponent during their next turn.

## Mana-base red-team
- Final candidate remains **34 lands**.
- Nine usable fetchlands: Bloodstained Mire, Polluted Delta, Scalding Tarn, Marsh Flats, Misty Rainforest, Flooded Strand, Arid Mesa, Verdant Catacombs, Wooded Foothills.
- Typed premium targets include Badlands, Underground Sea, Volcanic Island, Blood Crypt, Watery Grave, Steam Vents, and Xander's Lounge.
- City of Brass, Mana Confluence, Command Tower and Exotic Orchard reinforce the demanding U/B/R activation-plus-payload turns.
- Minamo is both an untapped blue source and commander untap engine.
- Two Islands, two Mountains and two Swamps remain for basic-land resilience.
- Ancient Tomb is retained because repeated Zevlor activations and high-impact sorceries are mana-intensive.

## Legality / color identity
- Commander color identity: **U/B/R**.
- All candidate additions are colorless, blue, black, red, U/B/R-compatible multicolor cards, or lands with legal U/B/R Commander identity.
- Current official Wizards Commander banned list checked 2026-10-15; none of the candidate cards is on the Commander banned list.
- Force of Will is Commander-legal despite being banned in Brawl; those are different formats.
- No project exception applies to Zevlor.

## Structural verification
- Total cards: **100**.
- Commander copies: **1**.
- Distinct names: **97**.
- Repeated names: **Island x2, Mountain x2, Swamp x2 only**.
- Nonbasic singleton compliance: **PASS**.
- Land count: **34**.
- U/B/R color identity: **PASS**.
- Current official Commander legality: **PASS**.
- Relevant rules/combo interactions: **PASS**.
- Whole-list audit: **PASS**.
- Candidate exhaustion: **PASS**.
- Commander-necessity/differentiation: **PASS**.
- Mana-base red-team: **PASS**.
- Adversarial red-team: **PASS**.
- Zero-new-material-improvement closure: **PASS**.

## SHA binding
Approval-candidate SHA-256 (exact UTF-8 bytes, including final newline):
`d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9`

## Status
**APPROVAL_READY — not yet approved or locked.** Explicit user approval is required before state/tracker lock updates.
