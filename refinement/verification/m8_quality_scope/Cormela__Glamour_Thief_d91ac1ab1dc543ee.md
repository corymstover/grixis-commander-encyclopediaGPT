# M8 exact-current high-power commander-first review — #9 Cormela, Glamour Thief

2026-10-28. **KEEP Cory's explicit M7 Rev2 six-swap locked 100 unchanged.** Source `refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt`; raw SHA-256 `d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd`. Exactly 100 unique singleton physical names, one commander plus 99 library, 30 lands, 13 mana artifacts including one-shot and sacrifice-only access, 20 Game Changers, official Commander legal/Grixis identity/no exception, **Bracket 5 — cEDH**, Storm / Aristocrats / Combo. Oct14 baseline `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b` preserved.

Evidence: engineering [PR #684](https://github.com/corymstover/GrokBotMTGCompanion/pull/684), exact head `6a267c9f38f8e8d610e1ac8f2f7bc69dbe0bb56b`, current source reviewed in `data/grixis/m7/decision_reviews/Cormela__Glamour_Thief_ChatGPT_M7_Rev2_Independent.md`, Git blob `50c24bf04d463988b47ba4cdbb1f72eda63c5e5d`, [exact scoped CI #40052202543](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40052202543) SUCCESS. All 100 Oct23 selected Oracle/legality rows preserved in `refinement/verification/Cormela__Glamour_Thief_M7_Rev2_Approved_2026-10-23_Verification.md`. That is source-bound, **not** an exhaustive newly rerun Spellbook search, updated tournament win-rate sample or new independent I/J for the six-swap owner lock.

**Commander-first mechanical bottleneck:** Cormela has haste, and `{1},{T}` makes **{U}{B}{R} that can only cast instant/sorcery spells**. It cannot pay creature/artifact costs, generic ability activation, or a flashback unless casting a real instant/sorcery. Her **death** returns *up to one* targeted instant/sorcery card already in graveyard when the trigger goes on stack. Choosing the command zone after death does not erase the death trigger; keeping her in grave enables separate Goryo/Shallow/reanimate lines. Sacrificing Cormela to altars or copying her via Twinflame/Saw/Molten gives deaths and graveyard recasts under actual spell-payment/legend/timing boundaries. This is why free mana, actual targets, graveyard resilience and one-mana hate answers matter more here than generic Grixis midrange.

## Exactly 99 library physical slots, one primary role each

### 30 lands — colored cEDH tempo and restricted-activation conversion

- 1x Ancient Tomb
- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x City of Brass
- 1x Command Tower
- 1x Flooded Strand
- 1x Gemstone Caverns
- 1x Island
- 1x Luxury Suite
- 1x Mana Confluence
- 1x Marsh Flats
- 1x Mistrise Village
- 1x Misty Rainforest
- 1x Morphic Pool
- 1x Mountain
- 1x Otawara, Soaring City
- 1x Phyrexian Tower
- 1x Polluted Delta
- 1x Scalding Tarn
- 1x Shivan Reef
- 1x Steam Vents
- 1x Sulfurous Springs
- 1x Swamp
- 1x Training Center
- 1x Underground River
- 1x Underground Sea
- 1x Volcanic Island
- 1x Watery Grave
- 1x Wooded Foothills

Underground River replaces opponent-dependent Exotic Orchard with reliable untapped U/B at pain cost; Mistrise Village replaces tapped Undercity Sewers (loses black and surveil) with blue plus a spell-uncounterable mode only if actual land/timing conditions are met. Seven real typed-fetches cannot fetch arbitrary nonbasic utility lands. Cormela's mana may be converted into **unrestricted** land mana by a legally paid Frantic Search untapping up to three **already tapped** lands, but source count/tap state can make the exchange mana-negative. Thirty lands is aggressive even for low-curve cEDH; rituals and one-shot rocks help until hate/wipes tax the commander. City/Confluence and Ad Nauseam/Necropotence make own life a finite budget.

### 13 mana artifacts — conditional, temporary and sacrifice resource access

- 1x Arcane Signet
- 1x Ashnod's Altar
- 1x Chrome Mox
- 1x Lion's Eye Diamond
- 1x Lotus Petal
- 1x Mana Vault
- 1x Mox Diamond
- 1x Mox Opal
- 1x Phyrexian Altar
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence

The altars require real creatures and don't produce mana without sacrificing; LED requires discarding the hand and cannot be held as free protection forever; Opal has metalcraft, Chrome/Mox Diamond discard or imprint a real resource, Vault creates untap costs and Lotus Petal is one use. Thirteen artifacts do not all provide persistent two-mana acceleration. Null Rod/Collector Ouphe/Force of Vigor are significant vulnerabilities. Cormela's own UBR can pay Frantic Search/Saw/Into only while casting, never these artifact activation costs.

### 27 combo, real ritual, sacrifice/reanimation and source-paid finishers

- 1x Birgi, God of Storytelling // Harnfel, Horn of Bounty
- 1x Borne Upon a Wind
- 1x Brain Freeze
- 1x Cabal Ritual
- 1x Culling the Weak
- 1x Dark Ritual
- 1x Demonic Consultation
- 1x Demonic Gifts
- 1x Dualcaster Mage
- 1x Entomb
- 1x Frantic Search
- 1x Goryo's Vengeance
- 1x Jeska's Will
- 1x Intuition
- 1x Molten Duplication
- 1x Reanimate
- 1x Rite of Flame
- 1x Saw in Half
- 1x Seething Song
- 1x Shallow Grave
- 1x Simian Spirit Guide
- 1x Tainted Pact
- 1x Tendrils of Agony
- 1x Thassa's Oracle
- 1x Twinflame
- 1x Underworld Breach
- 1x Wishclaw Talisman

Wishclaw is a targeted **tutor artifact**, not a static mana rock; it consumes mana/activation and may give an opponent the Claw. Thassa Oracle with Consultation/Tainted Pact is a genuine counterable source-paid win, and singleton Tainted Pact may exile cards until needed; no claim of guaranteed protected Oracle. Breach/Brain Freeze/LED needs actual cast/escape/fuel, and opponent graveyard hate or Rule of Law can stop it. Twinflame+Dualcaster can be repeatable with a real initial creature/spell target and mana. Cormela+Saw/Molten/Twinflame can recur resolved spells through actual death-trigger timing, but neither Frantic Search alone nor an unassisted Cormela legend loop is an infinite-mana machine. With Cormela and Birgi, casting relevant red spells can provide `{R}` to pay each next `{1}` permission on a properly staged loop, subject to copy death and stack. Goryo/Shallow require Cormela actually in grave and are limited by exile/delayed sacrifice. Tendrils' storm copies are not casts. These 27 favor actual combo density, with real life/yard/mana costs.

### 14 stack/control/protection answers — actual hostile spell classes

- 1x An Offer You Can't Refuse
- 1x Chain of Vapor
- 1x Deflecting Swat
- 1x Fierce Guardianship
- 1x Flusterstorm
- 1x Force of Negation
- 1x Force of Will
- 1x Hexing Squelcher
- 1x Mental Misstep
- 1x Mindbreak Trap
- 1x Pact of Negation
- 1x Into the Flood Maw
- 1x Pyroblast
- 1x Swan Song

The sixth Rev2 change deliberately cuts Preordain for Into the Flood Maw: without gifting a tapped Fish it targets **an opponent's creature only**, but with the gift promise it targets **an opponent's nonland permanent** including hate enchantment/artifact for `{U}`. It does **not** bounce our own permanent and grants opponent a token. REB's loss for Hexing Squelcher shifts to protecting spell casts and giving ward that costs opponents life; a creature cannot answer a spell by merely being in the list and can die before the combo turn. Free Swat/Fierce have commander-control requirements, Force requires pitch resource/alternate payment, Pact creates future mana payment unless winning first, and Flusterstorm answers actual instant/sorcery on stack, not Null Rod permanent already resolved. Multiple answers in 99 do not imply they appear in hand during the window.

### 15 selection, draw, card-flow punishment and wheel recovery

- 1x Ad Nauseam
- 1x Brainstorm
- 1x Demonic Tutor
- 1x Diabolic Intent
- 1x Gamble
- 1x Imperial Seal
- 1x Mystic Remora
- 1x Mystical Tutor
- 1x Necropotence
- 1x Orcish Bowmasters
- 1x Ponder
- 1x Rhystic Study
- 1x Vampiric Tutor
- 1x Wheel of Fortune
- 1x Windfall

Tutor restrictions matter (Imperial/Vampiric top of library at life cost, Gamble random discard, Intent sacrifice). Ad Nauseam/Nausing changes life totals and requires actual low curve; Mystic/Rhystic depend on opponents, Necropotence exiles discarded cards, Orcish punishes extra draws under actual trigger conditions. Windfall and Wheel fill Breach but can also draw opponents into stack answers. Removing Gitaxian Probe sacrifices free hand inspection/cantrip, removing Faithless Looting reduces graveyard sculpt and removes flashback access; Frantic Search addresses *Cormela* restricted-mana conversion differently. This is risked knowingly, not hidden.

## Original design-only M6 P0/P1 cases, all current-source reconciled

Original `data/grixis/m6/test_blueprints/Cormela__Glamour_Thief.json`: **P0 five** `C1 K1 K2 K3 F1`, **P1 eight** `K4 E1 E2 W1 W2 W3 F2 F3`. This 13-group bounded accounting and exact-source fixtures do **not** relabel the older Grok five-swap formal I/J as a fresh six-swap I/J, or prove an exhaustive current stack engine.

| Group | Current source-positive proposition | Adverse/cost rule |
|---|---|---|
| **P0 C1** | Hasty paid `{1},{T}` creates restricted UBR and dying may return a spell. | No legal activation, non-I/S spending or non-graveyard target: fail. |
| **P0 K1** | Three restricted colors can pay casting cost of an actual I/S in proper zone. | Cannot pay Wishclaw activation or generic artifact/creature cost. |
| **P0 K2** | Commander can die and owner keep her in grave for reanimation; death trigger still exists if moved to zone. | Choosing command zone removes grave body for Goryo until it changes zones again. |
| **P0 K3** | Saw in Half destroys the original and creates two legendary token copies; one dies to the legend rule, with corresponding real death triggers. | Original Saw doesn't enter grave until it resolves; illegal target/legend exceptions cannot be invented. |
| **P0 F1** | Actual protection can win a stack war if payable/drawn. | Unanswered enemy counter or Silence/Rule of Law stops line; Squelcher not immunity to all triggers. |
| **P1 K4** | Bowmasters sees opponents' extra draws during Wheel/Windfall. | Does not punish our own wheel-drawn cards just by being present; self-harm is opponent controlling other Bowmasters. |
| **P1 E1** | Restricted UBR can cast Frantic Search, untapping real tapped lands. | No tapped lands or insufficient mana for activation: no arbitrage guarantee. |
| **P1 E2** | Sacrifice altars/Tower produce mana and real Cormela death-recovery. | Returning spell requires target already in grave when trigger put on stack. |
| **P1 W1** | Saw in Half with actual recursion/rituals and proper legend-state trigger can replay. | Solo Cormela cycle needs payable `{1}`; Birgi/ritual conditional, not automatic infinity. |
| **P1 W2** | Goryo/Shallow plus sacrifice outlet reanimate when commander is in grave. | Command-zone choice or grave exile prevents target; temporary haste/cleanup matters. |
| **P1 W3** | Molten Duplication plus Birgi/Cormela, or Dualcaster copy line, real target/stack. | Copy spell is not cast; no enemy-proof loop without cost/zone preservation. |
| **P1 F2** | Breach/recursion require available grave source. | Dauthi/Rest in Peace/other grave removal can stop in response. |
| **P1 F3** | Ad Nauseam/Ancient Tomb/City/Confluence are paid resource engines. | Paying too much life or dying to opponent damage turns a win attempt into loss. |

## Tested challenger opportunity stop: six, not a quota

Approved swaps: Mistrise/Undercity Sewers, Underground River/Exotic Orchard, Frantic Search/Faithless Looting, Twinflame/Gitaxian Probe, Hexing Squelcher/Red Elemental Blast, Into the Flood Maw/Preordain. Actual costs: fewer one-mana selection/deliberate discard spells, no free hand peek, lost cheap anti-blue Blast, no black surveil land. Four concrete complete 100 challenges: **Abrade rather than Into** (permanent artifact destruction but fails enchantment/other nonland hate), **Snap rather than Into** (two-land untap but cannot remove Null Rod/Rule of Law), **Burnt Offering over Windfall** (unrestricted life/mana through Cormela death but loses draw/Breach/Opponent-Bowmasters fuel and the offering spell itself cannot be returned by death trigger before resolving), and **Dramatic Reversal over Ponder or an existing combo slot** (untaps Cormela/rocks, but no self-recast and weak vs Ouphe). None clearly wins the cEDH commander's *cheap anti-hate and mana conversion* needs over its real incumbent. Thirty lands and life liability remain deliberate high-power risks. **No new card change, no fabricated win-rate, no final M8 signoff.**
