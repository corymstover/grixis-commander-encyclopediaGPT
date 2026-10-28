# M8 exact-current whole-99 commander-first review — #10 Crosis, the Purger

2026-10-28. **KEEP Cory's owner-approved M7 Rev2 nine-swap exact 100 unchanged.** Source `refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt`, raw SHA-256 `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a`. 100 physical, 95 distinct names, Island x3/Mountain x2/Swamp x3 only repeats, 36 lands, twelve repeatable-or-burst acceleration artifacts, fourteen Game Changers, legal Grixis/no project exception, Bracket 4, Discard / Dragons / Extra Combats. Historical Oct14 raw `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1` remains preserved and its inaccurate older Regalia/Blizzard tracker note is not retroactively rewritten.

Evidence: engineering [PR #685](https://github.com/corymstover/GrokBotMTGCompanion/pull/685), exact head `6bc6ff135e90db1237c0dd9881017aaf36e249fe`, complete nine-swap decision `data/grixis/m7/decision_packets/Crosis__the_Purger_M7_Rev2_ChatGPT_Independent_20261023.md`, Git blob `d871426afc67626f87a6b47f0bc46139e6fd518a`, four scope-specific GitHub workflows SUCCESS on that head. All 95 selected current October 23 Oracle names resolved from archived Crosis plus Cecily channel-land data in `refinement/verification/Crosis__the_Purger_M7_Rev2_Approved_2026-10-23_Verification.md`. The earlier Grok five-swap M6 J is historical, not newly re-sealed on current Rev2 SHA, and no tournament win rates or current full-stack Magic simulator are claimed.

**Commander identity:** Crosis costs `{3}{U}{B}{R}`, has flying and needs to deal actual **combat damage to a player**. Its trigger lets you pay **{2}{B} on resolution**, then choose one color and make that player reveal/discard all cards of that color. **Painter's Servant** names a color for all cards in all zones, potentially making a successful paid purge empty the full hand even if cards were originally colorless. *The ability is not a free Mind Twist and not an ETB*. It requires a connection, surviving commander/source, payment and real opposing cards; empty hands limit repeat value. Sword of Feast and Famine can untap lands to fund payment/Assault, but if Painter names black, it turns Sword **black**, and Sword-granted protection from black can make the Sword detach from its own equipped creature. Source-specific protection/attachment matters.

## The exact current 99-library physical ledger — each copy assigned once

### 36 lands: payable UBR six-drop and `{2}{B}` combat resolution

- 1x Ancient Tomb
- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Cavern of Souls
- 1x City of Brass
- 1x Command Tower
- 1x Exotic Orchard
- 1x Geier Reach Sanitarium
- 3x Island
- 1x Luxury Suite
- 1x Mana Confluence
- 1x Marsh Flats
- 1x Misty Rainforest
- 1x Morphic Pool
- 2x Mountain
- 1x Otawara, Soaring City
- 1x Plaza of Heroes
- 1x Polluted Delta
- 1x Scalding Tarn
- 1x Shizo, Death's Storehouse
- 1x Sokenzan, Crucible of Defiance
- 1x Steam Vents
- 3x Swamp
- 1x Takenuma, Abandoned Mire
- 1x Training Center
- 1x Underground Sea
- 1x Verdant Catacombs
- 1x Volcanic Island
- 1x Watery Grave
- 1x Xander's Lounge

Rev2 replaces one basic Island/Swamp/Mountain with Otawara/Takenuma/Sokenzan. These preserve untapped U/B/R respectively, give real paid channel blocker bounce/grave recovery/raid attackers, but increase nonbasic-hate exposure and remove fetchable basics. Sokenzan is the weakest optional upgrade in heavy Back to Basics/Blood Moon pods, a real potential reversion—not a universal cut. City/Confluence life costs, Ancient Tomb colorless, Cavern restricted to chosen creature type, and Plaza's legend conditions matter. Thirty-six lands provide more six-drop stability than 30-land turbo builds but cannot ensure `{2}{B}` is left after casting six-MV commander plus equipment.

### 12 acceleration artifacts (some one-shot/colored-restricted)

- 1x Arcane Signet
- 1x Chrome Mox
- 1x Dimir Signet
- 1x Izzet Signet
- 1x Lotus Petal
- 1x Mana Vault
- 1x Mox Diamond
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence

Keeping Izzet Signet is a deliberate correction to Grok's five-swap cut: Crosis needs real U/R pips and cannot pay `{2}{B}` with Sol Ring alone. Jet Medallion was removed for Megrim and its black cost reduction is lost; Mox Diamond needs a land discarded, Chrome needs imprint, Mana Vault untaps at cost, Petal disappears. The “twelve” count is not twelve repeatable colored rocks or a guaranteed early Crosis.

### 7 commander-connection, copy/discard enablement and repeat-combat pieces

- 1x Aggravated Assault
- 1x Brotherhood Regalia
- 1x Lightning Greaves
- 1x Painter's Servant
- 1x Reanimate
- 1x Swiftfoot Boots
- 1x Sword of Feast and Famine

Regalia's unblockable restriction depends on relevant defender, equip and ward payment; Greaves grants haste/shroud (can obstruct future own targets), Boots haste/hexproof after cost. Sword untaps lands on actual equipped-creature damage; it does not pay the `{2}{B}` Crosis cost automatically, nor ensure color. Aggravated Assault activation `{3}{R}{R}` in **main phase** needs five usable mana, and an additional full purge requires **three more** including black (at least eight usable mana per connected combat when doing both). Even Sword+Assault repeat combats end on Fog, blocker, removal or a failed hit. Reanimate pays Crosis's mana value in life if it's actually in grave; cannot retrieve from command zone.

### 26 opponent-card discard and per-card payoff engines

- 1x Bandit's Talent
- 1x Black Market Connections
- 1x Bloodchief Ascension
- 1x Dark Deal
- 1x Geth's Grimoire
- 1x Hymn to Tourach
- 1x Kroxa, Titan of Death's Hunger
- 1x Liliana's Caress
- 1x Megrim
- 1x Mind Twist
- 1x Notion Thief
- 1x Orcish Bowmasters
- 1x Raiders' Wake
- 1x Rankle, Master of Pranks
- 1x Sedraxis Specter
- 1x Syphon Mind
- 1x Teferi's Puzzle Box
- 1x Tergrid, God of Fright // Tergrid's Lantern
- 1x The Raven Man
- 1x Tinybones, Bauble Burglar
- 1x Tinybones, Pocket Nuisance
- 1x Tinybones, Trinket Thief
- 1x Tourach, Dread Cantor
- 1x Waste Not
- 1x Wheel of Fortune
- 1x Windfall

Megrim deals **2 actual damage per discarded opponent card**, Caress/Raiders each cause 2 life loss. With all three active a paid Painter purge of five real cards can cause 10 damage plus 20 life loss (30 life change absent damage prevention), but no empty-hand lethal assumption; active Bloodchief adds life drain only **after its three qualifying quest counters** are present and affected cards actually go to graveyard. Rankle chooses modes affecting **each player**, including us, and is not asymmetric; Raiders' Wake's raid discard requires its combat/attack condition, not a permanent Oppression-like tax. Tergrid responds to opponent discard of **permanent cards** and can return them if actually graveyard-eligible; Geth's Grimoire depends on cards really discarded, Tinybones variants have different activation and timing triggers. Notion Thief+Puzzle Box can replace opposing draw-step draws for a lock if both survive, not deal automatic damage. Wheel/Dark Deal/Windfall refill opponents to punish, but can also give them answers. Black Market Connections costs recurring life and is not a generic discard spell. Losing Bottomless Pit and Oppression removes preemptive symmetric hand tax, a genuine defensive loss but improves Crosis's ability to hit a **full** opponent hand.

### 18 interaction, tutoring, removal and source safety

- 1x Chaos Warp
- 1x Cyclonic Rift
- 1x Damnation
- 1x Dark Ritual
- 1x Deadly Rollick
- 1x Deflecting Swat
- 1x Demonic Tutor
- 1x Drown in the Loch
- 1x Feed the Swarm
- 1x Fierce Guardianship
- 1x Force of Will
- 1x Gamble
- 1x Mana Drain
- 1x Mystical Tutor
- 1x Recoil
- 1x Swan Song
- 1x Toxic Deluge
- 1x Vampiric Tutor

Rollick's free mode depends on controlling Crosis, and removing Fell Specter for it reduces extra discard-drain bodies but clears real blockers/creatures while preserving `{2}{B}`. Force needs a blue pitch or full mana, Swat/Fierce actual commander, and Mana Drain UU. Damnation/Deluge sweep our creatures and may reset Crosis, Drown depends on target/grave size, Recoil returns a permanent and separately discards only if opponent has cards. Vampiric/Gamble tutor at life/discard risk; Dark Ritual is one-shot black burst, not a rock. Do not infer on-demand protection by merely counting these 18 names.

## Original M6 source cases, exact present 100: five P0 / nine P1

Original blueprint `data/grixis/m6/test_blueprints/Crosis__the_Purger.json` is design-only, with **P0 five** `C1 K1 K2 K3 F1` and **P1 nine** `K4 K5 E1 E2 W1 W2 W3 F2 F3`. The old K5 *Oppression* symmetric branch is now **source-removed**; it is retired rather than marked current test PASS. New finite source-conditioned checks test surviving assertions/adversarial negatives, not technically independent J or complete combat stack modeling.

| Group | Current positive and paid condition | Adverse/removed source |
|---|---|---|
| **P0 C1** | Actual combat damage to player, optional `{2}{B}` payment, choose one color on resolution. | Blocked/removed/insufficient pay leaves hand; no combat hit/trigger. |
| **P0 K1** | Lands/rocks can pay black and two generic when trigger resolves. | Mana unavailable at resolution cannot be backdated from cast phase. |
| **P0 K2** | Painter names an actual color and makes all hand cards that color, including originally colorless cards. | Painter removed or different color choice: only matching printed/modified hand cards discard. |
| **P0 K3** | Sword trigger can untap actual lands before Crosis paid trigger by controller stack ordering. | Painter names black and makes Sword black while Crosis has pro-black, potentially detaching it; no free purge on disconnection. |
| **P0 F1** | Evasion/haste/protection can permit an actual combat hit. | Flying/reach blockers, Fog, response removal or theft prevents connect. |
| **P1 K4** | Tergrid/Tinybones triggers from real opponent discard may be legally ordered. | No graveyard permanent or opponent empty hand; ordering does not create cards. |
| **P1 K5** | Current Raiders' Wake/Bloodchief provide asymmetric follow-up to purge. | Historical Oppression symmetric spell-cast discard **removed**—no current-Oppression test/pass. |
| **P1 E1** | Crosis+Painter+evasion+payable trigger can purge multiple real cards. | No Painter or only partial color card hand reduces burst. |
| **P1 E2** | Waste Not/Grimoire/Tinybones/Tergrid/Caress convert real opponent discards into different values. | No discarded cards means no trigger/resource fountain. |
| **P1 W1** | Caress/Megrim/Wake and other discard payoffs can deal conditional finite lethal. | Enchantments removed, empty hands or prevented damage weaken kill. |
| **P1 W2** | Crosis with Sword/Regalia/Boots can pressure for commander combat damage. | Sword attack must actually connect; Assault requires extra mana. |
| **P1 W3** | Notion Thief replaces opposing Puzzle Box draw-step draws. | Missing/bounced source or timing replacement changes the state; it's not instant damage. |
| **P1 F2** | Available `{2}{B}` at trigger resolution permits purge. | Tapped-out Crosis can hit without discarding anyone. |
| **P1 F3** | Empty-hand opponents face Crosis/Rankle/Specter combat finish. | Hand-denial can outpace kill and invite topdecked answer; no guaranteed clock. |

## Nine approved swap challenge: four legal complete-100 alternatives

Current nine swaps: Megrim/Jet Medallion, Rankle/Blizzard Specter, Aggravated Assault/Dream Salvage, Raiders' Wake/Oppression, Deadly Rollick/Fell Specter, Bloodchief Ascension/Bottomless Pit, and Otawara/Takenuma/Sokenzan for one Island/Swamp/Mountain. Alternative **Jet back for Megrim** restores discount but loses 2 damage/card, reducing signature Crosis payoff; **Dream Salvage back for Assault + Fell Specter back for Rollick** restores card flow and discard threat but eliminates extra combat Sword ceiling and emergency free blocker removal; **Bottomless Pit back for Bloodchief + Oppression back for Raiders' Wake** restores symmetrical stax but strips our own spells and depletes target hands before Crosis hits; **Sokenzan → Mountain** is a real single-slot basic-land-resilience improvement but loses a paid instant-speed two-attacker option that turns on raid while retaining red source. Other screened alternatives (Court of Ambition, Painful Quandary, Dauthi Voidwalker, Rogue's Passage, Counterspell) sacrifice actual card discard, graveyard theft synergy, mana efficiency or direct connection. Current ninth swap retained. **No more change is clearly stronger for Crosis; no win-rate claim, historical J transfer, or final M8 signoff.**
