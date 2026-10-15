# Kess, Dissident Mage — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Authoritative source: `GrixisFINAL60--2026.zip / Kess__Dissident_Mage.csv` and `GrixisFINALTXT60--2026.zip / Kess__Dissident_Mage.txt`  
Source CSV SHA-256: `b6d42012e6c7c3f9d5143d7cdb3e3608e611ae56247f2b00d13f6e87549440c7`  
Source TXT SHA-256: `b4b7c64f81689be95758e46b44f904a025370c21ea01f7a568b8a1de830a14fc`  
Baseline artifact: `refinement/decklists/Kess_Dissident_Mage_Current_Cycle_Baseline_2026-10-14.txt`  
Baseline artifact SHA-256: `49dd9a466452c2be53fa4143b0398276021c0bec22c5a9f9f5ce97a22ad5f7da`  
Approval candidate: `refinement/decklists/Kess_Dissident_Mage_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb`

## Source reconciliation

The current FINAL60 CSV and FINALTXT exports agree on the 100-card quantity/name map. The baseline is 100 cards, 94 distinct names, and 32 lands. Only basic Island, Mountain, and Swamp repeat. Older v8.1.4 rankings are supporting discovery evidence and are not automatic recommendations.

## Commander blueprint and natural ceiling

**Primary commander plan:** exploit Kess's once-per-turn graveyard casting permission to turn tutors and consultation effects into repeated resources and compact wins. Kess is strongest when cards are useful on their first cast and become materially stronger when replayed: `Demonic Consultation`, `Tainted Pact`, `Demonic Tutor`, `Demonic Counsel`, `Entomb`, `Intuition`, `Gifts Ungiven`, cheap interaction, rituals, and cantrips. Graveyard-filling creatures/spells and effects that create a new Kess object receive additional commander-specific value.

**Natural ceiling: Power Bracket 5 — fringe cEDH.** Kess remains a genuine cEDH commander with 2026 tournament representation and several strong finishes, including 5th/44 and 2nd/17 results, but contemporary conversion is materially below the format's leading commanders. The candidate therefore preserves full cEDH speed while refusing slow spellslinger payoffs that would lower the ceiling.

### Commander-specific spine

- `Demonic Consultation` and `Tainted Pact` are effectively one-card Kess win enablers when Kess is on the battlefield: cast the consultation effect from hand to obtain `Thassa's Oracle`, cast Oracle, then replay the consultation effect from the graveyard with Kess in response to the Oracle trigger.
- The candidate has **100 distinct names**, so `Tainted Pact` is not forced to stop on a duplicate name. This corrects a material baseline defect: the baseline contains three Islands, three Mountains, and three Swamps despite running Tainted Pact.
- `Intuition` with Kess can assemble `Thassa's Oracle`, `Reanimate`, and `Demonic Consultation` (or an equivalent Pact configuration) so every opponent choice leaves a winning route, subject to mana and interaction.
- `Gifts Ungiven`, now officially Commander-legal, can use a four-card `Thassa's Oracle / Reanimate / Demonic Consultation / Tainted Pact` package; when Gifts is cast from hand with Kess's graveyard permission unused, every two-and-two split leaves a winning configuration with sufficient mana.
- `Entomb` becomes a commander-specific instant-speed tutor for any instant or sorcery that Kess can then cast from the graveyard; it can also stock a creature for `Reanimate` where relevant.
- `Faithless Looting`, `Dragon's Rage Channeler`, and `Ledger Shredder` stock the graveyard while remaining efficient cEDH cards.
- `Displacer Kitten` can blink Kess after a noncreature spell is cast, creating a new Kess object and therefore a fresh once-per-turn graveyard-cast permission. This follows Kess's official ruling that a new Kess permits another graveyard spell in the same turn.
- `Snapcaster Mage` supplies graveyard access on opponents' turns, where Kess's own permission does not apply.
- `Spellseeker` finds `Demonic Consultation`, `Tainted Pact`, `Reanimate`, `Brain Freeze`, cheap interaction, and other compact lines.
- `Demonic Counsel` is accepted because this deck naturally supports delirium; before delirium it does not function as a general tutor and is evaluated with that limitation explicitly recognized.

## Exact current-cycle changes

The revision is a **41-quantity rebuild**. The commander is unchanged. Accounting is exact: **58 retained noncommander quantities + 41 cut quantities = all 99 baseline noncommander slots**, and 41 singleton additions restore the list to 100 cards.

### Cut quantities — 41

- `Aetherflux Reservoir`
- `Archmage Emeritus`
- `Baral, Chief of Compliance`
- `Birgi, God of Storytelling // Harnfel, Horn of Bounty`
- `Blightstep Pathway // Searstep Pathway`
- `Bojuka Bog`
- `Chaos Warp`
- `Clearwater Pathway // Murkwater Pathway`
- `Consider`
- `Fabled Passage`
- `Fork`
- `Frantic Search`
- `Galvanic Relay`
- `Goblin Electromancer`
- `Haunted Ridge`
- `Increasing Vengeance`
- `Island` x3
- `Jeska's Will`
- `Mizzix's Mastery`
- `Mountain` x3
- `Nightscape Familiar`
- `Past in Flames`
- `Pyretic Ritual`
- `Riverglide Pathway // Lavaglide Pathway`
- `Seething Song`
- `Sensei's Divining Top`
- `Shipwreck Marsh`
- `Sokenzan, Crucible of Defiance`
- `Storm-Kiln Artist`
- `Stormcarved Coast`
- `Swamp` x3
- `Takenuma, Abandoned Mire`
- `Tendrils of Agony`
- `Xander's Lounge`
- `Yawgmoth's Will`

### Add quantities — 41

- `Dragon's Rage Channeler`
- `Ledger Shredder`
- `Ragavan, Nimble Pilferer`
- `Simian Spirit Guide`
- `Displacer Kitten`
- `Valley Floodcaller`
- `Imperial Seal`
- `Personal Tutor`
- `Reanimate`
- `Demonic Counsel`
- `Windfall`
- `Beseech the Mirror`
- `Into the Flood Maw`
- `Mental Misstep`
- `Pyroblast`
- `Red Elemental Blast`
- `Borne Upon a Wind`
- `Final Fortune`
- `Force of Negation`
- `Gifts Ungiven`
- `Mindbreak Trap`
- `Mox Opal`
- `Fellwar Stone`
- `Grinding Station`
- `Talisman of Indulgence`
- `Wishclaw Talisman`
- `Arid Mesa`
- `Badlands`
- `City of Brass`
- `City of Traitors`
- `Fiery Islet`
- `Flooded Strand`
- `Gemstone Caverns`
- `Mana Confluence`
- `Marsh Flats`
- `Mistrise Village`
- `Misty Rainforest`
- `Underground Sea`
- `Verdant Catacombs`
- `Volcanic Island`
- `Wooded Foothills`

## Why the slow baseline package is removed

The baseline devotes too many slots to six-mana storm engines, redundant cost reducers, dedicated storm payoffs, and broad recursion that duplicate Kess rather than exploit her. `Thousand-Year Storm`, despite ranking first in the inherited candidate table, is likewise rejected: its six-mana ceiling is inappropriate for current cEDH. `Aetherflux Reservoir`, `Tendrils of Agony`, `Archmage Emeritus`, `Storm-Kiln Artist`, `Mizzix's Mastery`, `Past in Flames`, and similar cards can produce impressive high-mana turns but are less efficient than compact Oracle/Consultation and Breach lines.

## Adversarial second pass

- **Reanimate — ACCEPTED.** It is not generic reanimator filler here; it completes the deterministic Kess `Intuition` and `Gifts Ungiven` piles with Oracle plus a consultation effect.
- **Displacer Kitten — ACCEPTED.** Kess's official ruling explicitly gives a new Kess object another graveyard cast that turn. Kitten therefore has direct commander-specific utility beyond generic blink value.
- **Gifts Ungiven — ACCEPTED.** It was officially unbanned in Commander on 2025-04-22 and has current Kess competitive adoption. The selected pile is commander-dependent because Kess converts graveyarded pile pieces into castable resources.
- **Demonic Counsel — ACCEPTED with limitation.** Without delirium and with no Demon in the list, it is not a general tutor. The deck's artifact/creature/enchantment/instant/land/sorcery mix plus DRC, Looting, Shredder, wheels, fetches, and normal spell exchange make delirium realistic enough for the slot.
- **Valley Floodcaller — ACCEPTED.** It is current cEDH infrastructure that allows noncreature spells to be cast as though they had flash. It does not extend Kess's permission to opponents' turns; it only changes timing where Kess already permits a graveyard cast.
- **Consider — REJECTED despite high inherited rank.** The one-mana surveil cantrip is synergistic, but current cEDH slot pressure favors the denser tutor/interaction package. Candidate rankings are discovery evidence, not mandatory inclusions.
- **Jeska's Will — REJECTED narrowly.** Kess can benefit from both modes while on the battlefield, but the final list already has sufficient acceleration and prefers cheaper deterministic/tutor infrastructure.
- **Flame of Anor — REJECTED narrowly.** Kess being a Wizard makes it excellent value, but three mana for interaction/value is below the selected cEDH interaction rate.
- **Past in Flames / Yawgmoth's Will / Mizzix's Mastery — REJECTED.** They duplicate graveyard-recursion functionality at higher cost; Kess and Underworld Breach already occupy those roles more efficiently.
- **Thousand-Year Storm / Professor Onyx / Talrand / Guttersnipe / Young Pyromancer — REJECTED.** These inherited high-ranked candidates reflect spellslinger popularity rather than Kess's current cEDH ceiling.
- **Hoarding Broodlord reanimator package — REJECTED.** Successful 2026 Kess pilots have used it, but adding the full package would shift too many slots toward a generic reanimation engine. Kess's own Consultation/Intuition/Gifts lines are more commander-defining.
- **The One Ring — REJECTED.** Excellent generic value but four mana and no direct Kess/graveyard interaction.
- **Opposition Agent / Dauthi Voidwalker — REJECTED from the final 100.** Both are strong generic Grixis disruption; the final commander-first allocation instead prioritizes graveyard stocking, Kess reset, tutors, and compact spell-based interaction.
- **Cursed Totem — REJECTED.** It does not materially advance Kess and the list does not need a commander-independent stax pivot.

## Closure

The exact candidate is **100 cards / 100 distinct names / 27 lands**. Its primary identity is **Kess graveyard replay + Consultation/Pact one-card commander lines + Intuition/Gifts deterministic piles**, with Underworld Breach / Lion's Eye Diamond / Brain Freeze retained as a compact secondary cEDH route.

After the mandatory 99-slot audit, current 2026 tournament comparison, inherited candidate review, consultation-combo review, graveyard-package challenge, mana-base reconstruction, generic-staple challenge, and adversarial second pass, the candidate has **ZERO NEW MATERIAL IMPROVEMENTS** pending exact SHA-bound Oracle/color-identity, current official Commander legality, independent rules verification, and the complete fail-closed approval gate.

Candidate remains **NOT APPROVED** until those gates pass and the user explicitly approves the exact SHA-bound list.
