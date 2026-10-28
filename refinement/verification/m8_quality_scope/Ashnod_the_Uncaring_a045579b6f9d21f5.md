# M8 current 99-copy commander-first judgment — #6 Ashnod the Uncaring

2026-10-28. **KEEP Cory's exact approved M7 Rev2 100 unchanged.** Source `refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt`, raw SHA-256 `a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761`; one Ashnod, 100 cards, 95 names, Island x3/Mountain x2/Swamp x3, 33 lands, eight development artifacts including one-shot Lotus Petal, no legality/project exception, Bracket 4, Ability Copy / Artifact Sacrifice / Artifact Combo. Historical `f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf` remains untouched.

Authority: engineering [PR #681](https://github.com/corymstover/GrokBotMTGCompanion/pull/681), head `c7b907d4aecc97513a6ce3c28ed107aecd5a3be9`, whole-99 independent comparison `data/grixis/m7/decision_reviews/Ashnod_the_Uncaring_ChatGPT_M7_Rev2_Independent_Review.md`, Git blob `1e946ac2670801dae3c2877cac39102f6b4dabad`. [Exact Rev2 focused CI #40048290216](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40048290216) succeeded with nine new and 29 older focused methods; archived 95-name selected Oracle, eight complete researched 100s and Rev2 source-bound I/J are distinct from a full game-engine proof or an independently rerun later M8 J. October 23 approved owner receipt is in `refinement/verification/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23_Verification.md`.

Ashnod has deathtouch and copies an **activated nonmana ability of an artifact or creature** only if one or more permanents are **sacrificed to pay that activation's cost**. It is not limited to once each turn. Mana abilities (Ashnod's Altar, KCI, ordinary lands) are excluded, and creatures sacrificed while another ability *resolves* do not retroactively qualify. The original sacrificed object is still gone and only costs of the original activation are paid; targets for the copy may be changed. This specific cost/copy distinction is why Spawning Pit, Ruthless Knave, Priest, Spellbombs, Time Sieve and Trading Post matter more than generic artifacts.

## All 99 present library physical copies, individually assigned a primary role

### 33 lands: source/color access and artifact utility at the known 5-MV commander floor

- 1x Academy Ruins
- 1x Ancient Tomb
- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Buried Ruin
- 1x Command Tower
- 1x Mana Confluence
- 1x Great Furnace
- 1x Inventors' Fair
- 3x Island
- 1x Luxury Suite
- 1x Morphic Pool
- 2x Mountain
- 1x Otawara, Soaring City
- 1x Polluted Delta
- 1x Scalding Tarn
- 1x Seat of the Synod
- 1x Steam Vents
- 3x Swamp
- 1x Training Center
- 1x Treasure Vault
- 1x Underground Sea
- 1x Urza's Saga
- 1x Vault of Whispers
- 1x Volcanic Island
- 1x Watery Grave
- 1x City of Brass

Two approved land swaps replace tapped Xander's Lounge and opponent-dependent Exotic Orchard with immediate City/Confluence colors, charging life and losing cycling/opponent-dependent ceiling. Fetches can only find appropriate land types; Saga is chapter-driven, Inventors' Fair/Academy Ruins/Buried Ruin require setup and are not UBR sources. Artifact lands and Treasure Vault are themselves vulnerable to artifact hate. **33 lands** is a real tension for Ashnod plus engine pieces; modeled top-11 3+ source probability is only an access proxy, not a win-rate or cast-success statistic.

### 8 development artifacts: actual tap, color and one-use constraints

- 1x Arcane Signet
- 1x Basalt Monolith
- 1x Lotus Petal
- 1x Mind Stone
- 1x Mox Opal
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance

Basalt requires real seed mana for Rings/Gadgeteer loops, taps for **colorless** and is not a colored rock; Mox Opal requires metalcraft, Lotus Petal disappears and doesn't provide repeatable turns. Cutting Fellwar Stone/Talisman of Indulgence trades reliability for two original Ashnod-sacrifice cost engines. Cryptic source counts should not treat Petal as permanent acceleration.

### 30 sacrifice-activation, graveyard recursion and death resource engines

- 1x Altar of Dementia
- 1x Arcbound Ravager
- 1x Ashnod's Altar
- 1x Oni-Cult Anvil
- 1x Blasting Station
- 1x Trading Post
- 1x Crime Novelist
- 1x Disciple of the Vault
- 1x Dockside Chef
- 1x Dross Scorpion
- 1x Dross Skullbomb
- 1x Emry, Lurker of the Loch
- 1x Spawning Pit
- 1x Executioner's Capsule
- 1x Forensic Gadgeteer
- 1x Goblin Engineer
- 1x Goblin Welder
- 1x Grinding Station
- 1x Krark-Clan Ironworks
- 1x Krark-Clan Shaman
- 1x Myr Retriever
- 1x Nim Deathmantle
- 1x Priest of Forgotten Gods
- 1x Pyrite Spellbomb
- 1x Retrofitter Foundry
- 1x Rings of Brighthearth
- 1x Scrap Trawler
- 1x Scrap Welder
- 1x Time Sieve
- 1x Wayfarer's Bauble

Each has a nonidentical boundary. Time Sieve's paid sacrifice **of five artifacts** can double the extra-turn ability with Ashnod, without getting the five back. Altar of Dementia/Blasting Station use sacrificed creature last-known information; Ashnod's Altar/KCI are **mana** abilities and are *not* copied, although the sacrifices still fuel other triggers. Goblin Welder's artifact exchange sacrifices during resolution and thus **does not** itself qualify for Ashnod's copied ability. Rings' payment of `{2}` is a distinct copy option, not the same source as Ashnod. Pit/Crime Novelist needs an initial creature, counters on Pit and 1 starting generic if no artifact creature, then a produced 2/2 Spawn artifact can feed subsequent paid Pit activations; no free infinite mana is thereby produced. Dross Scorpion/Foundry require real untaps and token costs; Scrap Trawler/Myr Retriever require appropriate mana values/zones. Executioner's Capsule/Pyrite Spellbomb/Aether Spellbomb use their actual targeted versus card-draw costs, not interchangeable text. Priest can double sacrifice/life/mana/draw modes only after sacrificing **two other creatures** and tapping an eligible Priest; its targeted effect is not a mana ability. This is central Ashnod engineering, not mere artifact density.

### 16 copy beneficiaries, extra activated-cost tools, real win outlets

- 1x Clan Crafter
- 1x Corridor Monitor
- 1x Marionette Apprentice
- 1x Mayhem Devil
- 1x Sai, Master Thopterist
- 1x Urza, Lord High Artificer
- 1x Walking Ballista
- 1x Animation Module
- 1x Ruthless Knave
- 1x Repurposing Bay
- 1x Moonsilver Key
- 1x Mishra's Bauble
- 1x Mnemonic Sphere
- 1x Kuldotha Forgemaster
- 1x Bolas's Citadel
- 1x Aether Spellbomb

Ruthless Knave's first **paid** `{2}{B}` sacrifice activation creates four Treasures with Ashnod; its second *three-Treasure* activation draws two rather than one, with a genuine three-token cost. Animation Module and Crime Novelist give real +1/+1-counter/creation/sacrifice linkages, but unbounded loops need initial artifact creatures, costs and legal timing. Walking Ballista actually converts unlimited **colorless** Basalt/Rings or Gadgeteer mana into removal/life loss only after casting/activation payment, not a simultaneous free win. Marionette Apprentice and Mayhem Devil trigger on source-specific death/sacrifice events, while Sai's 1/1 Thopters cannot themselves pay any nonexistent Ashad casualty (this is Ashnod's ability-copy deck). Repurposing Bay/Forge/Crafter/Moosilver Key have tap, lookup or artifact-exile costs. Citadel and Time Sieve demand actual library/topdeck, mana and artifact-board conditions; no boardless Citadel certainty.

### 12 interaction, tutoring and discounts

- 1x An Offer You Can't Refuse
- 1x Chaos Warp
- 1x Cyclonic Rift
- 1x Deflecting Swat
- 1x Demonic Tutor
- 1x Enthusiastic Mechanaut
- 1x Etherium Sculptor
- 1x Fierce Guardianship
- 1x Mana Drain
- 1x Toxic Deluge
- 1x Vampiric Tutor
- 1x Vandalblast

Cost reducers accelerate artifact casts but are not sacrifice targets by themselves; the protection pieces have normal legal spell timing or commander-control prerequisites and can be disrupted by artifact-mana shutdown. The loss of Foundry Inspector leaves two reducers. Artifact board wipes/Collector Ouphe/Stony Silence are a real vulnerability; Vandalblast overload can destroy opposing artifacts but cannot recover our own if opponents cast it first.

## M6 original P0/P1 group accounting on current Rev2

Original `data/grixis/m6/test_blueprints/Ashnod_the_Uncaring.json`: **P0 five** `C1 K1 K2 K3 F1`; **P1 nine** `K4 K5 E1 E2 W1 W2 W3 F2 F3`. This blueprint is design-only and several named sources were cut in Rev2. Bounded current-source adapter tests and exact physical 99 reconciliation are a new scoped check; their success does not relabel the historic Grok I/J or prove a full Magic stack/third-party independent replay.

| Group | Actual current legal proposition | Negative case / historical branch |
|---|---|---|
| **P0 C1** | Activated artifact/creature, nonmana and sacrifice in activation *cost*: optional copy, new targets. | Mana ability, resolution-time sacrifice or no Ashnod does not qualify. |
| **P0 K1** | Several separate qualifying activations on one turn may each copy. | Copy is an ability, not fresh activation; can't repeatedly pay the same permanent. |
| **P0 K2** | Ashnod's Altar and KCI sacrifice creatures/artifacts and make mana. | Their mana abilities are **not** doubled by Ashnod. |
| **P0 K3** | Time Sieve original activation consumes five artifacts and can yield two actual extra turns with Ashnod. | No five artifacts, tapped Sieve, removed commander or activation interrupted: no free extra turns. |
| **P0 F1** | Artifact answer/protection can interact with hate when drawn. | Stony Silence/Vandalblast-style disruption shuts down many engines; list inclusion ≠ access. |
| **P1 K4** | Rings plus Ashnod can produce distinct copies of a paid nonmana sacrifice activation. | Rings itself needs `{2}` and actual triggering activation; no automatic chain. |
| **P1 K5** | Altar of Dementia and Blasting Station use actual sacrificed creature information in their copies. | No legal original object/target and new target legality stop a fictional free hit. |
| **P1 E1** | Trading Post, Spellbombs, Capsule and Bauble have real sacrifice-cost copies. | Different modes include target and cost restrictions; Bauble's sacrificed artifact isn't restored. |
| **P1 E2** | Current Disciple, Mayhem Devil and Marionette Apprentice reward proper artifacts and deaths. | **Reckless Fireweaver removed**; old artifact-ETB damage branch is retired. |
| **P1 W1** | Trawler/Myr Retriever/Altar/cost reduction form a conditional resource-conserving recursion engine. | Must conserve grave/hand cost, not assume all artifact sacrifices return a Retriever. |
| **P1 W2** | Nim Deathmantle plus artifact sacrifice remains a conditional reanimation asset. | **Farid, Enterprising Salvager removed**; its token/Deathmantle variant is retired. |
| **P1 W3** | Dross Scorpion / Retrofitter Foundry / Altar/KCI can untap only after real events. | No initial artifact token/tap resources prevents an assumed autonomous loop. |
| **P1 F2** | Five-mana Ashnod enters with available mana, can amplify subsequent paid activations. | Thirty-three lands and one-shot Petal can strand five-mana commander. |
| **P1 F3** | Citadel/Time Sieve depend on a stocked artifact board and payable activation. | Empty board, hate or lethal Citadel life loss shut down. |

## Whole-100 counterfactual opportunity challenge

Nine approved additions/cuts are independently sourced: Monitor/Foundry Inspector, Basalt/Fellwar, Aether Spellbomb/Talisman Indulgence, Spawning Pit/Esoteric Duplicator, Animation Module/Fireweaver, Priest/Jhoira, Ruthless Knave/Farid, City/Xander and Confluence/Orchard. The eight researched complete 100s were not universal optimality proof. Challengers include **restore Fellwar for Basalt** (colored reliability but lose two independent artifact infinite-colorless pairings), **restore Talisman for Aether Spellbomb and Duplicator for Pit** (two additional resource pieces but lose copied bounce/draw and central Ashnod-specific Pit loop), **restore Jhoira/Farid for Priest/Knave** (historic draw and Scrap/Deathmantle, lose commander-paid doubling), and **restore two rainbow land cuts** (save life but add tap/opponent constraints). Each is a legal 100-slot one-/two-card or package exchange with an actual loss; none plainly improves this specific commander beyond the accepted Rev2. Best warning: 33 lands/eight artifacts and five-mana commander, plus artifact hate. The selected exact 100 still wins local commander-specific value-per-sacrifice after costed alternatives. **No new add/cut proposed; M8 owner acceptance still pending.**
