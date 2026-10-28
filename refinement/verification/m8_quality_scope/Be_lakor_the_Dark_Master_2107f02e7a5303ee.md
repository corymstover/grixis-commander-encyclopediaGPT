# M8 exact-current commander-first adjudication — #7 Be'lakor, the Dark Master

2026-10-28. **KEEP Cory's M7 Rev2 exact 100, no changes.** Locked source `refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt`, raw SHA-256 `2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4`. Exactly 100 physical / 94 names; Island x3, Mountain x2, Swamp x4; 36 lands, seven durable rocks, 25 printed Demons **including commander**, Bracket 4 — Demon Tribal / ETB Damage / Reanimator, no project exception. Previous Oct13 approved raw `3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e` remains immutable.

Source context: engineering [PR #682](https://github.com/corymstover/GrokBotMTGCompanion/pull/682), head `bcf3e8fc40f1084c0a612c368b1ecba5899be884`, pinned `data/grixis/m7/decision_reviews/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Independent.md`, blob `5749389d2541de2c770ea7457d758349174edf33`, [exact focused CI #40050434686](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40050434686) SUCCESS. All 94 selected October 23 Scryfall IDs/legalities were archived in `refinement/verification/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23_Verification.md`; no newly live-queried full Oracle collection or multiplayer win rate is asserted. The engineering review was only a *candidate* when authored, but Cory's subsequent exact-SHA approval and canonical lock are separate facts.

**Core identity:** Be'lakor costs six and has flying. *Prince of Chaos* on Be'lakor entering counts Demons **when that ability resolves**, including Be'lakor, and draws/loses life equal to that count. *Lord of Torment* triggers whenever **another** Demon enters under our control and that creature deals damage equal to its power to any target. Copies/cheat/reanimation create real extra Demon ETBs; enter simultaneously and legend-rule events still create appropriate triggers, but do not make a deterministic infinite. Heartless Summoning reduces small Demons' power and Lord-source damage; lower power and Prince's own life loss are honest costs. This is an ETB damage and Demon-density deck, not generic Grixis reanimator.

## The exact 99 physical main-deck copy ledger (one role per slot)

### 36 lands — six-mana triple-color Demon and later paid recursion

- 1x Ancient Tomb
- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Bojuka Bog
- 1x Cavern of Souls
- 1x Command Tower
- 1x City of Brass
- 1x Dragonskull Summit
- 1x Drowned Catacomb
- 1x Exotic Orchard
- 1x Mana Confluence
- 3x Island
- 1x Luxury Suite
- 1x Morphic Pool
- 2x Mountain
- 1x Otawara, Soaring City
- 1x Path of Ancestry
- 1x Polluted Delta
- 1x Scalding Tarn
- 1x Steam Vents
- 1x Sulfur Falls
- 1x Sunken Hollow
- 4x Swamp
- 1x Training Center
- 1x Underground Sea
- 1x Urborg, Tomb of Yawgmoth
- 1x Volcanic Island
- 1x Watery Grave
- 1x Xander's Lounge

City and Confluence replace tapped Crumbling Necropolis and conditional Foreboding Ruins, giving immediate all-color fixing but paying life atop Prince/Belzenlok/Annex/Vilis life liabilities. Bojuka Bog gives real on-entry graveyard hate at a tapland cost, Path of Ancestry taps, Ancient Tomb is colorless, and Cavern naming Demon helps casting but does not make a cost-free removal shield. Thirty-six lands is structurally sensible for six-to-eight-mana Demons, but color/land draws still vary.

### 7 repeatable static mana artifacts

- 1x Arcane Signet
- 1x Cursed Mirror
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence

Cursed Mirror pays `{2}{R}` and provides red, but when entering *as a creature copy* it temporarily has the copied characteristics instead of its normal mana tap ability. As a temporary copy of a Demon it supplies an extra Lord ETB but can die to legend rule when copying our own legendary Demon; it is not always a 3-mana untapped red rock. Swapping from Fellwar Stone costs one mana on curve, gains board-specific Lord/ETB ceiling. Dark Ritual belongs to a separate burst role and is not eighth static rock.

### 24 printed Demon creatures — primary Lord entry, Prince life and combat pressure

- 1x Abyssal Harvester
- 1x Archfiend of Depravity
- 1x Archfiend of Despair
- 1x Curse-Marred Demon
- 1x Bloodletter of Aclazotz
- 1x Shadowgrange Archfiend
- 1x Burning-Rune Demon
- 1x Chaos Defiler
- 1x Demon of Dark Schemes
- 1x Great Unclean One
- 1x Gyruda, Doom of Depths
- 1x Herald of Slaanesh
- 1x Kardur, Doomscourge
- 1x Lord of Change
- 1x Orcus, Prince of Undeath
- 1x Rakdos, Lord of Riots
- 1x Demonlord Belzenlok
- 1x Rakdos, the Showstopper
- 1x Desecration Demon
- 1x Doom Whisperer
- 1x Rune-Scarred Demon
- 1x Sower of Discord
- 1x Valgavoth, Terror Eater
- 1x Vilis, Broker of Blood

These are *not* a single interchangeable six-drop column: Curse-Marred 4/4 ETB tutors then discards **a card at random**, so the searched card is not secured; Shadowgrange removes highest-power creature **per opponent** and gains life equal to the **maximum** sacrificed power, not a sum. Desecration Demon has powerful four-mana 6/6 Lord ETB but opponents can tap it by sacrificing a creature at combat. Belzenlok offers an immediate, sometimes short, exile/draw-and-self-damage ETB rather than old Rakdos Patron's slower opponent-choice end step. Bloodletter can double life loss under its real predicates, Archfiend of Despair closes the end-step loss range, Sower spreads damage to chosen players, and Vilis turns life payments into draw only while truly present. Showstopper can randomly destroy non-Demons, Gyruda requires deck parity/actual library cards, Burning-Rune/Runescarred searches need actual library contents. Six-to-eight-mana bodies are slow without ramp/cheat, and self-life loss must be paid; their different on-entry power, draw, removal, tax and evasion functions make them preferable to further undifferentiated big Demons.

### 15 copy, cheat, creature-type and repeated-ETB enablers

- 1x Spark Double
- 1x Ghostly Flicker
- 1x Kindred Discovery
- 1x Molten Echoes
- 1x Panharmonicon
- 1x Patriarch's Bidding
- 1x Reanimate
- 1x Reflections of Littjara
- 1x Rite of Replication
- 1x Roaming Throne
- 1x Sneak Attack
- 1x Whip of Erebos
- 1x Urza's Incubator
- 1x Warstorm Surge
- 1x Heartless Summoning

Spark Double can copy a legendary Be'lakor while specifically **not legendary**, but Cursed Mirror lacks that permission. Throne chooses Demon to amplify commander triggers, Panharmonicon doubles suitable artifact/creature ETBs only and Reflections' spell copies aren't casts. Whip can exile its reanimated body at end step, Sneak Attack sacrifices at end step, and Bidding gives opponents type choices too. Rite of Replication kicked targeting Be'lakor produces five legendary token copies simultaneously: five original Lord triggers plus 5×4 token triggers = **25** source-damage triggers before legal doublers; state-based legend rule and stacked Prince life-loss triggers matter. No fake automatic 150 lethal damage against every opponent. Kindred Discovery's chosen type and source cast/ETB attack conditions matter; Heartless Summoning's -1/-1 has an explicit per-Demon opportunity cost. Reanimate's life loss is proportional to actual target mana value.

### 17 selection, answers, payoffs and flexible protection

- 1x Ancient Cellarspawn
- 1x Bedevil
- 1x Kindred Dominance
- 1x Chaos Warp
- 1x Cyclonic Rift
- 1x Dark Ritual
- 1x Deadly Rollick
- 1x Deflecting Swat
- 1x Demonic Counsel
- 1x Demonic Tutor
- 1x Feed the Swarm
- 1x Fierce Guardianship
- 1x Mana Drain
- 1x Liliana's Contract
- 1x Toxic Deluge
- 1x Unholy Annex // Ritual Chamber
- 1x Vampiric Tutor

Dominance protects one chosen creature type from its nonchosen-type wipe at **seven mana**; it is not universal one-sided if our support is outside Demon. Bedevil/Chaos/Feed handle different permanent classes; Deluge shrinks *our* Demons if overpaid, and Mana Drain requires `{U}{U}`. Liliana's Contract draws/charges four life and requires **four differently named Demons under control** at own upkeep to win, not four tokens named Be'lakor. Ancient Cellarspawn is a high-lift non-Demon role, not counted in the 24 printed Demons. Unholy Annex and Demonic Counsel have actual alternative/delirium conditions; no unconditional tutoring or safe life payment is inferred. Free Rollick, Swat, Fierce require their actual commander/hand setup.

## Original M6 conceptual P0/P1 — explicit present-source disposition

Original `data/grixis/m6/test_blueprints/Be_lakor__the_Dark_Master.json` has **five P0** `C1 K1 K2 K3 F1` and **nine P1** `K4 K5 E1 E2 W1 W2 W3 F2 F3`. They are individually reconciled with the present Rev2 source. Current bounded tests and the pinned prior focused suite do not prove a fresh independent third-model J or complete tabletop simulation.

| Case | Present legal condition | Adverse/failure bound |
|---|---|---|
| **P0 C1** | Actual Be'lakor ETB counts current Demons for Prince; another Demon ETB sources Lord. | No commander/no Demon/empty library or self-life burden limits payout. |
| **P0 K1** | Prince X determined as trigger resolves, **including** Be'lakor if still Demon controlled. | Removal of Demons before resolution lowers X; no prelocked count. |
| **P0 K2** | Entering Demon is damage source, power/LKI available to Lord trigger. | Removal or -1/-1 changes actual damage; Lord isn't Be'lakor damage. |
| **P0 K3** | Spark Double's explicit nonlegendary exception supports two Be'lakor roles. | Normal Mirror or Rite legend copies don't inherit exception. |
| **P0 F1** | On-curve fixing plus cheat can make expensive Demon line. | Six/eight-MV hands without early rocks/cheat and multiple life costs fail tempo. |
| **P1 K4** | Heartless discount helps heavy Demons. | -1/-1 lowers Lord damage and may kill weak utility creatures. |
| **P1 K5** | Bloodletter, Sower and Vilis can turn real damage/life loss into pressure/draw. | Life-loss ≠ damage, and without source/payee conditions no double trigger. |
| **P1 E1** | Throne choosing Demon, Panharmonicon and Spark source trigger multipliers. | Wrong chosen type or absent enabler yields normal single trigger. |
| **P1 E2** | Sneak Attack, Molten Echoes, Reflections, Whip and Bidding create conditional entries. | End-step sacrifice/exile and opponent Bidding effects remain. |
| **P1 W1** | Kicked Rite on Be'lakor gives 25 finite Lord triggers when intact. | Legend rule, self-damage, mana nine and target/opponent prevention stop guarantee. |
| **P1 W2** | Multiple other Demon enters can stack Lord damage and Archfiend/Bloodletter pressure. | No board, surviving targets or adequate life prevent a deterministic kill. |
| **P1 W3** | Contract needs four differently named Demons at upkeep. | Four identically named copies do not win; opponents may remove a Demon. |
| **P1 F2** | Prince draws X, pays X life on actual resolution. | Belzenlok, Annex, City and Vampiric consume life; no all-safe refill. |
| **P1 F3** | Six-MV commander can be recast with enough real mana. | Incremental command tax can outpace seven rocks; no free repeated Be'lakor. |

## Counterfactual complete-100 challenges and preference

Eight approved changes, charged for removed roles: Desecration Demon/Dream Devourer, Kindred Dominance/Blasphemous Act, Demonlord Belzenlok/Rakdos Patron of Chaos, Shadowgrange Archfiend/Bloodthirster, Cursed Mirror/Fellwar Stone, Curse-Marred Demon/Balor, City/Crumbling Necropolis, Confluence/Foreboding Ruins. Not every loss is superficial: Bloodthirster could provide extra combats, Fellwar was a cheaper colored rock, Dream Devourer smoothed enormous hands, Blasphemous Act cleared at 1 red in creature-dense games. Four complete 100 contenders were considered: **Fellwar over Cursed Mirror** (faster rock, loses copy ETB), **Bloodthirster over Shadowgrange plus Blasphemous over Dominance** (more extra combats/cheaper wipe but loses immediate simultaneous opponent edict plus selective Demon preservation), **Balor over Curse-Marred** (attrition vs cheaper card search), and **Dream Devourer over Desecration** (foretell smoothing vs six-power low-MV source). The selected Rev2 remains better on immediate copyable Demon ETBs and Lord-source damage. Shadowgrange's one-black pip reduces BBB curve pressure; Mirror and new untapped colors support a six-drop. A 36-land, seven-rock build can still be slow and suffer self-damage. **No new add/cut justified; no universal optimality or final M8 approval claimed.**
