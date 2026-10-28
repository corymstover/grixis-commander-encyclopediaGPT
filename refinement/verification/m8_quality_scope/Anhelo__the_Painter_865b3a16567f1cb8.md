# M8 exact-current commander-first whole-99 review — Anhelo, the Painter (#4)

2026-10-28. **Decision: KEEP owner-approved M7 Rev2 exact 100 unchanged.** Canonical `refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt`, raw SHA-256 `865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77`. 100 physical; 94 names; Island/Mountain/Swamp three each, no nonbasic duplicates, no exception; 34 lands, seven static rocks, Bracket 4; Spell Copy / Casualty Aristocrats / Spellslinger Combo. This is the locked **Rev2**, not the working October 13 source, Grok five-swap research candidate or an unapproved hypothetical.

## Source-based evidence and substantive quality conclusion

- Exact owner authorization and prior hash discrepancy preservation: `refinement/verification/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23_Verification.md`. Engineering [PR #652](https://github.com/corymstover/GrokBotMTGCompanion/pull/652), head `ceeda7b280f378a2f195fd15005268080f5cb09a`, pinned entire-list analysis `data/grixis/m7/decision_reviews/Anhelo__the_Painter_ChatGPT_Rev2_independent_comparison.md`, blob `44f7f4a7063949e8fd125a17a0139abd656a10e6`. [Rev2 focused CI #40043498281](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498281), [Grok research #40043498183](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498183), [J provenance #40043498257](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498257), and [M7 contract #40043498172](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498172) were reported successful. Scope is source-bound finite/snapshot rules and strategic judgment, *not* new independent J or measured games.
- Commander costs `{U}{B}{R}`; **the first instant or sorcery cast by its controller each turn** gains casualty 2 while Anhelo is present. The controller must sacrifice a creature with power at least two **as an additional cost**; a copy appears on stack but **was not cast**. Earlier spells on that turn consume first-spell eligibility even if Anhelo arrived later. Each other player's turn can offer a fresh first spell if timing/costs align. The game plan is recurring expendable two-power bodies, not mere generic magecraft; no spell is copied for free without actual fodder.
- Strongest genuine concern: the compact **34 lands + seven static rocks** after cutting both Talisman of Indulgence and Fellwar Stone for repeatable casualty creatures. The engine can stall without land three/available body plus spell. Seven Game Changers do not alone prove consistency, and the independent engine combos can win *without* Anhelo—a qualitative weakness under a strict commander-first ideal. Conversely Miner, Shade, Concierge, Fable, Case, Cryptic Pursuit, Bloodghast, and several token makers make casualty a real repeated resource conversion, while the final card pool preserves stack answers and high-ceiling copy spells. These are concrete reasons to retain Rev2, with the mana risk explicit.

## Exact noncommander 99-copy ledger, one primary job per physical slot

### 34 lands — typed Grixis fixing, landfall sacrifice fuel and deliberate life costs

- 1x Badlands
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Cascade Bluffs
- 1x Command Tower
- 1x Exotic Orchard
- 1x City of Brass
- 3x Island
- 1x Luxury Suite
- 1x Mana Confluence
- 1x Morphic Pool
- 3x Mountain
- 1x Otawara, Soaring City
- 1x Polluted Delta
- 1x Scalding Tarn
- 1x Misty Rainforest
- 1x Shivan Reef
- 1x Steam Vents
- 1x Stormcarved Coast
- 1x Sulfur Falls
- 3x Swamp
- 1x Training Center
- 1x Undercity Sewers
- 1x Underground Sea
- 1x Urborg, Tomb of Yawgmoth
- 1x Volcanic Island
- 1x Watery Grave
- 1x Xander's Lounge

The two mana-base swaps, Haunted Ridge → City and Shipwreck Marsh → Misty, improve turn-one any-color and Island-typed dual selection/landfall but lose damage-free later black/red fixing; City pings each tap and Misty requires fetch life and sometimes shock. Misty **cannot** fetch any land without Forest/Island basic land types and cannot fetch an arbitrary utility land. Bloodghast/Shade landfall is not guaranteed by simply having fetches in the list.

### 7 static rocks — colored development, not sufficient by themselves

- 1x Arcane Signet
- 1x Dimir Signet
- 1x Izzet Signet
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance

The lost black-red Talisman and Fellwar Stone improve reusable casualty material but lower the number of independent durable mana producers from nine to seven versus the October 13 physical source. Sol Ring alone cannot pay UBR and signets require starting mana. The 41 lands-plus-rocks static source heuristic from PR #652 is not the probability of a **color-functional, casualty-ready** opening hand; time/life/resource sequencing matters.

### 16 primary casualty fuel sources — mostly power two or repeatable token makers

- 1x Army of the Damned
- 1x Baral and Kari Zev
- 1x Black Market Connections
- 1x Bloodghast
- 1x Cryptic Pursuit
- 1x Deekah, Fractal Theorist
- 1x Sinister Concierge
- 1x Jadar, Ghoulcaller of Nephalia
- 1x Ghoulish Procession
- 1x Judith, Carnage Connoisseur
- 1x Fable of the Mirror-Breaker // Reflection of Kiki-Jiki
- 1x Case of the Stashed Skeleton
- 1x Poppet Stitcher // Poppet Factory
- 1x Forsaken Miner
- 1x Skyclave Shade
- 1x Talrand, Sky Summoner

These are **sources**, not sixteen immediately available 2-power creatures. Army costs eight and tapped Zombies arrive after resolution; Baral/Kari and Talrand produce creature tokens when spells are actually cast, not on Anhelo's copies; Deekah's token power equals relevant mana value and a cheap spell can create a too-small Fractal; Ghoulish Procession only triggers when a **nontoken** creature dies and has a once-each-turn limit. Cryptic Pursuit `{2}{U}{R}` manifests a new 2/2 only for hand-cast instant/sorceries, *not* their copies or graveyard casts; the face-down card recovered upon death only if its front is instant/sorcery and must be cast in the allowed window. Case creates a suspected Skeleton then must meet solve timing before paying for sorcery-speed tutor. Fable's Chapter I Goblin can support casualty; Reflection appears after Saga latency, is not an immediate generic body. Sinister Concierge's death delays a creature via suspend/time counters but is temporary, not permanent removal. Skyclave Shade requires own-turn landfall to cast from grave; Bloodghast landfall returns directly. Forsaken Miner `{B}` recurrence needs an actual crime targeting opponents/their cards or game objects; per official Thunder Junction ruling it can trigger on the same spell to which it was sacrificed as casualty cost if that spell commits the crime, but not every sacrifice constitutes a crime.

### 12 copy engines, payoffs and spell finishing sources

- 1x Crackle with Power
- 1x Dualcaster Mage
- 1x Galvanic Iteration
- 1x Narset's Reversal
- 1x Ral, Storm Conduit
- 1x Reiterate
- 1x Storm-Kiln Artist
- 1x Time Warp
- 1x Torment of Hailfire
- 1x Twinflame
- 1x Twinning Staff
- 1x Veyran, Voice of Duality

Copying Time Warp can queue actual extra turns; copies of Crackle and Torment must retain real paid `{X}` values, and the latter may overwhelm opponents only with actual mana. Storm-Kiln and Ral care about cast **or copy**, unlike Talrand/Baral/Pursuit's **cast-only** triggers. Veyran multiplies qualifying triggered abilities but does not turn copied spell objects into cast spells. Twinning Staff adds one copy per copy event and does not create exponential identical copies by itself. The actual Dualcaster + Twinflame creature target/stack route can create a loop of hasty Dualcaster copies when an initial legal creature and mana exist; they expire at the scheduled next end step and do not imply instantaneous game win without damage/finish conditions. Reiterate buyback `{4}{R}{R}` on a still-live Mana Geyser or Jeska's Will requires real mana; it is net positive only if a repeated copy creates at least seven red, and is otherwise mana-neutral/negative. Narset's Reversal plus Staff/Reiterate is a **conditional stack copy chain**, not an unconditional costless infinite without a legal original spell and stack ordering.

### 10 answers, protection and reset buttons

- 1x An Offer You Can't Refuse
- 1x Chaos Warp
- 1x Counterspell
- 1x Cyclonic Rift
- 1x Deadly Rollick
- 1x Deflecting Swat
- 1x Feed the Swarm
- 1x Fierce Guardianship
- 1x Mana Drain
- 1x Toxic Deluge

Counterspell/Mana Drain need `{U}{U}`, Offer gives opposing Treasures, and free Rollick/Guardianship/Swat depend on control of the actual commander. Feed the Swarm handles an enchantment at life cost; stripping it for Bedevil would weaken that coverage. Deluge shrinks our casualty producers too, Cyclonic overload is seven mana, and graveyard hate defeats Miner/Shade/Kess/Breach attempts. A card existing in the 99 is no proof it is drawn when the combo is threatened.

### 20 burst mana, access, cost relief, filtering and recursion sources

- 1x A Little Chat
- 1x Archmage Emeritus
- 1x Big Score
- 1x Cormela, Glamour Thief
- 1x Dark Ritual
- 1x Demonic Tutor
- 1x Dig Through Time
- 1x Frantic Search
- 1x Goblin Electromancer
- 1x Jeska's Will
- 1x Kess, Dissident Mage
- 1x Maestros Charm
- 1x Mana Geyser
- 1x Mystical Tutor
- 1x Preordain
- 1x Snapcaster Mage
- 1x Startle
- 1x Thunderclap Drake
- 1x Underworld Breach
- 1x Vampiric Tutor

A Little Chat has native casualty and may receive a **second, distinct** casualty ability from Anhelo; paying both requires two eligible sacrifices rather than reusing a creature. Kess normally recasts only on our turns and exiles its cast spell on later graveyard movement, Snapcaster flashback is one-shot and Breach escape exiles other cards; none becomes Cryptic Pursuit *hand-cast* by recasting from grave. Cormela dies to return a spell but cannot return herself as a spell. Storm mana Geyser counts actual opponents' tapped lands; Jeska's Will counts a chosen opponent's cards in hand for its mana mode and requires commander control for both options. Thunderclap Drake's discount/copy grant is source-bound and cannot override actual cast restrictions. Archmage can trigger on copies, but it is a value piece whose sacrifice to pay casualty costs a future engine.

## Original M6 conceptual tests: 5 P0 + 9 P1 exact-current bounded dispositions

Source `data/grixis/m6/test_blueprints/Anhelo__the_Painter.json`, design-only blueprint, historic basis. Its main failing assumption for Rev2 is **E2's Maestros Ascendancy branch**: that enchantment is **removed**, replaced by Case of the Stashed Skeleton. The source's historical `Primal Wellspring + Frantic Search` backup combo is also **removed** by replacing Primal Amulet with Miner. Their specific old loops do **not** inherit a present-list PASS. New canonical `tests/test_m8_anhelo_painter_current.py` SHA-binds and tests each surviving/retired original group as bounded finite conditions. They are not a stack-engine exhaustive replay or new independent third-model/J pass.

| Original | Scoped current positive / finite case | Adversarial condition, historical-only branch |
|---|---|---|
| **P0 C1** | Anhelo deathtouch and first own cast instant/sorcery may receive casualty 2, with real eligible body. | No Anhelo or no appropriate cast: no granted casualty. |
| **P0 K1** | Sacrifice an actual power-2+ creature when casting a qualified spell: one casualty copy, no extra cast. | No body, 1-power body, already-spent cast, or omitted sacrifice: zero grant-derived copies. |
| **P0 K2** | On each controller turn, first instant/sorcery tracks from that turn's beginning. | Spell cast **before Anhelo entered** still occupies the turn's first-cast slot, so next spell has no newly granted casualty. |
| **P0 K3** | Archmage/Storm-Kiln magecraft each see cast plus copy; Talrand is cast-only. | A casualty copy by itself does not create Talrand token or Cryptic Pursuit manifest. |
| **P0 F1** | 2/2 expendable creature supports casualty copy. | No expendable power-2+ creature means a critical spell resolves without casualty copy. |
| **P1 K4** | Staff replacement adds a second copy to one real casualty copy event. | No Staff, no eligible sacrifice or copy event: no extra Staff copy. |
| **P1 K5** | First turn spell A Little Chat may have its printed casualty plus Anhelo-granted casualty. | Two bodies/costs needed for two copies; no twice-paid body, and copy isn't cast. |
| **P1 E1** | Real 2-power fodder and first-spell-per-turn timing can feed Archmage/Storm-Kiln/Deekah repeated value. | Cannot sacrifice a single body more than once; opponent turns need legal timing/spell/mana and another fodder. |
| **P1 E2** | Actual Kess, Snapcaster and Breach grave casting remain conditional spell recursion. | **Maestros Ascendancy removed**: its sacrifice-to-recast branch is retired, not passed; graveyard exile stops surviving options. |
| **P1 W1** | Reversal/Staff/Reiterate copy stack states have real targets and can generate extra spell copies/qualified payoffs. | No original live target/mana/priority: no assumed infinite Reversal chain; exact arbitrary-copy loop is not a proof from this bounded fixture. |
| **P1 W2** | Twinflame targeting existing own creature, flash Dualcaster and new ETB copy of Twinflame targeting Dualcaster can repeat. | No initial creature, no Dualcaster mana or countered Twinflame prevents setup; tokens leave at end step. |
| **P1 W3** | Reiterate 4RR buyback repeatedly copying live Geyser/Will can net red if each copied ritual makes at least seven. | Output six merely breaks even, less loses resources; target/cast/payability conditions cannot be skipped. |
| **P1 F2** | Sacrifice a small disposable 2-power fodder, preserving Talrand/Archmage. | If only an engine creature is available, paying casualty kills its future triggers. |
| **P1 F3** | Live grave/stack/target plus paid protection allow a bounded combo line. | Opponent removal/countering, grave exile and no protection stop it; presence of a listed answer is not guaranteed access. |

All **14 original conceptual case groups** are individually accounted for under exact Rev2 source, with removed-card E2 and older Wellspring assertions quarantined; they are **not** historic I/J promoted to current. Fourteen finite bounded fixtures + one roster/ledger fixture are separate from historical [engineering focused success #40043498281](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40043498281).

## Incumbent-challenge and explicit stop decision

The seven owner-approved swaps were Miner/Primal Amulet, Shade/Talisman of Indulgence, Concierge/Fellwar Stone, Case/Maestros Ascendancy, Fable/Lagomos, City/Haunted Ridge and Misty/Shipwreck Marsh. In the pinned Rev2 pool, original source had 34 lands and nine static rocks, Grok's proposed five had 33/6, selected Rev2 34/7, and high-mana seven 34/8. Static 3+ mana sources among top nine of 99 were estimated in that fixed non-mulligan hypergeometric abstraction at 83.94% baseline, 76.85% Grok, 80.60% Rev2 and 82.32% high-mana; color/timing/payment are omitted. They are **not** game win-rates.

| Full 100-card alternative | Why seriously consider it | Current Rev2 preference and cost to admit |
|---|---|---|
| Replace Sinister Concierge → Fellwar Stone | Regain the eighth static rock; better Anhelo plus answer hand smoothing | Concierge is a recurring, low-curve 2-power casualty sacrifice with temporary exile tempo, and seven permanent rocks are supported by cheap rituals; however a slow/mana-tight pod may reasonably reverse this call. |
| Replace Deekah → Fellwar Stone (prior full high-mana seven variant) | 34 lands/eight rocks, stronger third-source odds | Loses Fractal fodder created by **cast or copy**, one of the strongest Anhelo-specific engines; current favors higher ceiling over 1.7-point top-nine static-source difference. |
| Replace Forsaken Miner → Primal Amulet and Skyclave Shade → Talisman of Indulgence | Two durable spell/mana engines, closer original static nine | Delayed Wellspring setup costs four mana and loses criminal target-recurrence, plus replacing Shade weakens power-2 body availability; without fodder, Amulet duplicates only under its own flip constraints. |
| Replace City → Haunted Ridge and Misty → Shipwreck Marsh | Less self-inflicted life loss and fewer fetch/shock costs | Sacrifices turn-one UBR and typed Island dual selection/extra two-step Bloodghast landfall. Rev2's improvement is color agility rather than raw mana counts. |

**Stop reason:** Anhelo is more than incidental: 16 distinct repeatable/potential body sources are deliberately paired with 12 copy/finisher tools, including expensive spells worth copying, and direct recast plus mana payoffs. Yet the commander-independent Twinflame and Reiterate combo finishes and lost rocks are transparent weaknesses. The candidate pool includes complete alternate 100s, costed mana probabilities and removed-engine checks; none shows a clear consistent win in the requested **Anhelo first** resource-conversion balance. The present exact locked 100 is preferred. **No new change recommended; no mathematical optimality, new win-rate or final M8 acceptance claimed.**
