# Evelyn, the Covetous — Current-Cycle Whole-List Audit and Candidate Decision Record

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Deck:** #18 — Evelyn, the Covetous  
**Current status:** UNLOCKED / NOT APPROVED  
**Authoritative source TXT SHA-256:** `ad5d4297f3940ab174b5e214e7288c283cc58302f815996c050c05bc5e75fa62`  
**Standardized baseline SHA-256:** `9be69c3ee143a9e109c341fdd7a2f5bf18446bafde92cf0af35afddea7df00ea`  
**Approval-candidate SHA-256:** `1d602b5d9b2a370d3448816f593198212b2b83da74e92ccc3232798641b2588a`

## 1. Baseline reconciliation

The authoritative October 12 current CSV/TXT exports reconcile at exactly **100 cards / 97 distinct names**. Only basic lands repeat (`Island x2`, `Swamp x3`). The current exports supersede the older v8.1.4 card-audit snapshot.

The stale audit differs in five slots. Current authoritative cards:
- `Crossway Troublemakers`
- `Dusk Legion Sergeant`
- `Leyline of Anticipation`
- `Olivia's Wrath`
- `Scion of Opulence`

Stale-audit-only challengers:
- `Anowon, the Ruin Sage`
- `Kindred Dominance`
- `Nighthawk Scavenger`
- `Terminate`
- `Vampire Socialite`

None of the stale-only cards survives the natural-ceiling cEDH review.

## 2. Natural power ceiling determination

The previous baseline is optimized Vampire/ETB value, but current tournament evidence establishes that Evelyn's natural ceiling is **Bracket 5 — cEDH / fringe-competitive**, not merely Bracket 4 tribal midrange.

Current `stats.cedh.events` evidence on 2026-10-14 reports **48 Evelyn entries, 10 top cuts**, with `Worldgorger Dragon`, `Thassa's Oracle`, `Animate Dead`, `Necromancy`, `Dance of the Dead`, `Underworld Breach`, `Brain Freeze`, `Tainted Pact`, `Demonic Consultation`, and compact interaction/tutors forming the stable competitive core. Tony W top-cut a 42-player event on 2026-10-04 with Evelyn; John Weinhandl top-cut a 36-player event on 2026-07-12.

This is commander-first rather than generic Grixis homogenization: Worldgorger plus a reanimation Aura repeatedly blinks **Evelyn herself**, producing repeated collection-counter exile triggers and infinite mana. Evelyn then converts the loop into access to the exiled win card. `Leyline of Anticipation`, `Party Thrasher`, and `Saw in Half` further exploit Evelyn's own exile/ETB text.

Primary external evidence:
- https://stats.cedh.events/commanders/Evelyn%2C%20the%20Covetous
- https://www.mtgtop8.com/event?d=897298&e=91803&f=cEDH
- https://edhtop16.com/tournament/midwest-circuit-series-tropical-island
- https://commanderspellbook.com/combo/4812-4846/
- https://commanderspellbook.com/combo/1368-3518-4856/

## 3. Candidate construction

The candidate begins from the newest known Evelyn tournament top-cut shell (Tony W, 2026-10-04), then makes three evidence-based flex-slot upgrades rather than copying it blindly:

1. `Pithing Needle` -> `Swan Song`
   - Swan Song is in **89.6%** of current Evelyn cEDH lists; Pithing Needle falls below the published artifact staple cutoff.
   - Swan protects the combo and answers decisive noncreature interaction for one mana.

2. `Imposter Mech` -> `An Offer You Can't Refuse`
   - Offer appears in **77.1%** of current Evelyn cEDH lists; Imposter Mech falls below the published artifact staple cutoff.
   - The final shell values one-mana stack protection over conditional opponent-creature copying.

3. `Mockingbird` -> `Saw in Half`
   - Saw in Half appears in **62.5%** of current Evelyn cEDH lists; Mockingbird falls below the published creature staple cutoff.
   - Saw is also more commander-specific: when it successfully destroys Evelyn and she actually dies, the two Evelyn token copies enter and their ETB abilities trigger; it can also function as removal/value elsewhere.

The resulting candidate is **100 cards / 100 distinct names**, including only one `Island` and one `Swamp`, preserving a clean `Tainted Pact` library-exile line.

## 4. Mandatory 99-slot baseline audit

Every noncommander baseline slot was independently evaluated. Quantity accounting: **99 slots = 22 retained + 77 cut**.

| Qty | Baseline card | Source role | Decision | Reason |
|---:|---|---|---|---|
| 1 | Ancient Tomb | Land | RETAIN 1 | premium fast-mana land; supports Evelyn, Ad Nauseam setup, and combo turns. |
| 1 | Animate Dead | Recursion | RETAIN 1 | primary Worldgorger Dragon reanimation loop piece and commander-specific infinite-ETB engine. |
| 1 | Arcane Signet | Ramp | RETAIN 1 | efficient three-color acceleration; present in current tournament shell. |
| 1 | Black Market Connections | Draw | CUT 1 | excellent optimized-EDH value, but three-mana/upkeep-speed accrual is too slow for Evelyn’s proven cEDH ceiling; replaced by Mystic Remora/Rhystic Study/Necropotence and compact tutors. |
| 1 | Blasphemous Act | Removal | CUT 1 | nine-mana printed sweeper is inefficient in stack-centric cEDH even when discounted; candidate uses one-mana interaction and bounce instead. |
| 1 | Blood Artist | Drain | CUT 1 | does convert Worldgorger death loops into a win, but it is a redundant dead payoff because Evelyn herself converts the loop into library exile/infinite mana and Thoracle closes cleanly. |
| 1 | Blood Crypt | Land | RETAIN 1 | untapped/fetchable B/R source. |
| 1 | Bloodghast | Recursion | CUT 1 | recursion body has insufficient standalone impact; sacrifice acceleration is covered by Culling the Weak without dedicating a low-ceiling creature slot. |
| 1 | Bloodletter of Aclazotz | Drain | CUT 1 | combat/life-pressure payoff does not advance Evelyn’s compact combo plan. |
| 1 | Bloodline Keeper // Lord of Lineage | Tokens | CUT 1 | four-mana tribal token/anthem engine is below cEDH rate. |
| 1 | Bloodline Necromancer | Recursion | CUT 1 | five-mana tribal recursion is far slower than Animate Dead/Dance of the Dead/Necromancy/Reanimate. |
| 1 | Bloodstained Mire | Land | RETAIN 1 | premium fetchland; fixes all three colors through dual/shock suite. |
| 1 | Bloodthirsty Conqueror | Lifegain | CUT 1 | high-mana lifegain combo piece is outside Evelyn’s fastest commander-native Worldgorger axis. |
| 1 | Captivating Vampire | Removal | CUT 1 | tribal anthem/theft requires board density that the cEDH shell intentionally abandons. |
| 1 | Champion of Dusk | Draw | CUT 1 | five-mana tribal draw requires Vampire density and is replaced by cheaper unconditional engines. |
| 1 | Chaos Warp | Removal | CUT 1 | three-mana broad answer is too inefficient; Chain of Vapor and stack interaction cover the relevant cEDH windows. |
| 1 | Chrome Mox | Ramp | RETAIN 1 | zero-mana acceleration essential at the cEDH ceiling. |
| 1 | Command Tower | Land | RETAIN 1 | unconditional three-color land. |
| 1 | Cordial Vampire | Counters | CUT 1 | tribal counter payoff has no role once the deck stops relying on Vampire combat. |
| 1 | Counterspell | Removal | CUT 1 | UU hard counter is playable but loses on efficiency to Flusterstorm, Swan Song, Offer, Force effects, Pact, Misstep, Mindbreak, Pyroblast/REB. |
| 1 | Crossway Troublemakers | Draw | CUT 1 | five-mana tribal combat/draw payoff is far above the cEDH curve. |
| 1 | Crumbling Necropolis | Land | CUT 1 | always enters tapped; unacceptable tempo loss at cEDH speed. |
| 1 | Cyclonic Rift | Removal | CUT 1 | strong card and serious challenger, but current Evelyn tournament aggregate is only ~42%; the final shell prioritizes Chain of Vapor plus cheaper stack interaction and combo density. |
| 1 | Demonic Tutor | Tutor | RETAIN 1 | unrestricted two-mana tutor for Worldgorger, reanimation, Thoracle, Breach, protection, or mana. |
| 1 | Dimir Signet | Ramp | CUT 1 | retained color pair is better served by Talisman of Dominance; Signet requires an activation mana and loses to free rocks/Fellwar Stone. |
| 1 | Displacer Kitten | Blink | CUT 1 | serious commander-synergy challenger and present in John Weinhandl’s July 2026 top-eight list, but four mana plus a five-mana commander is top-heavy; the newer October top-cut shell moved away from it. |
| 1 | Dominating Vampire | Removal | CUT 1 | temporary tribal theft requires Vampire board presence and does not materially advance the cEDH win plan. |
| 1 | Don Andres, the Renegade | Theft | CUT 1 | thematic theft payoff, but three-mana value after stealing cards is too slow versus direct combo/protection pieces. |
| 1 | Drana, Liberator of Malakir | Counters | CUT 1 | combat counter engine is outside the natural cEDH line. |
| 1 | Drana, the Last Bloodchief | Recursion | CUT 1 | five-mana attack recursion is too slow and combat-dependent. |
| 1 | Drowned Catacomb | Land | CUT 1 | conditional untapped land displaced by unconditional/fetchable premium fixing in the 26-land shell. |
| 1 | Dusk Legion Sergeant | Protection | CUT 1 | tribal protection/value is too narrow at cEDH speed. |
| 1 | Dusk Legion Zealot | Draw | CUT 1 | two-mana cantrip Vampire is inefficient relative to Mystic Remora/Rhystic/Necropotence and does not justify a slot solely to trigger Evelyn once. |
| 1 | Exotic Orchard | Land | RETAIN 1 | efficient untapped multiplayer fixing in the recent top-cut shell. |
| 1 | Fabled Passage | Land | CUT 1 | effectively tapped/tempo-negative early fixing; replaced by true fetchlands and premium rainbow/dual lands. |
| 1 | Feed the Swarm | Removal | CUT 1 | sorcery-speed two-mana answer is lower rate than the candidate’s stack interaction/bounce package. |
| 1 | Florian, Voldaren Scion | Draw | CUT 1 | requires combat damage and three mana before selection; too slow. |
| 1 | Ghostly Flicker | Blink | CUT 1 | blink value requires setup and does not form the chosen compact win package; Worldgorger supplies the commander-native repeatable ETB loop. |
| 1 | Glass-Cast Heart | Tokens | CUT 1 | tribal token/blood artifact is too slow and board-dependent. |
| 1 | Haunted Ridge | Land | CUT 1 | conditional untapped land displaced by fetch/dual/rainbow fast mana base. |
| 1 | Indulgent Aristocrat | Sac Outlet | CUT 1 | sacrifice/anthem Vampire lacks sufficient standalone utility. |
| 2 | Island | Land | RETAIN 1 / CUT 1 | one basic retained for resilient U access and Tainted Pact uniqueness; the second copy must leave so Tainted Pact cannot stop on duplicate basic names. |
| 1 | Izzet Signet | Ramp | CUT 1 | two-mana Signet is displaced by zero/one-mana acceleration and Fellwar Stone; color requirements do not justify the activation tax. |
| 1 | Kindred Discovery | Draw | CUT 1 | five-mana tribal draw engine is incompatible with the cEDH curve. |
| 1 | Leyline of Anticipation | Protection | RETAIN 1 | unusually commander-specific: turns Evelyn’s once-each-turn permission into opponent-turn access to noninstant collection-counter cards. |
| 1 | Lotus Petal | Ramp | RETAIN 1 | zero-mana colored acceleration and Breach resource. |
| 1 | Luxury Suite | Land | CUT 1 | playable land, but omitted in the final 26-land configuration after comparison with the October top-cut mana base; rainbow/fetch/dual/utility slots are tighter. |
| 1 | Malakir Bloodwitch | Drain | CUT 1 | five-mana tribal drain is not a competitive payoff. |
| 1 | Malakir Rebirth // Malakir Mire | Protection | CUT 1 | useful protection MDFC, but the land face enters tapped and the spell does not protect the noncreature combo pieces; free/one-mana stack protection wins the slot. |
| 1 | Markov Baron | Anthem | CUT 1 | anthem/cost-reduction tribal package is not part of the cEDH plan. |
| 1 | Master of Dark Rites | Ramp | CUT 1 | three-mana tribal ritual requires a creature sacrifice and is slower than Dark Ritual/Cabal Ritual/Culling the Weak. |
| 1 | Molten Echoes | Copy | CUT 1 | four-mana tribal copy engine is too slow; commander ETB multiplication is handled by the actual Worldgorger loop and Saw in Half. |
| 1 | Morphic Pool | Land | CUT 1 | strong multiplayer land and close challenger, but current 26-land top-cut configuration prioritizes fetchability, rainbow sources, and unique utility lands. |
| 1 | Mountain | Land | CUT 1 | no basic Mountain required; red is supplied by fetchable duals/rainbow lands, preserving singleton Tainted Pact structure while maximizing U/B access. |
| 1 | New Blood | Removal | CUT 1 | four-mana tribal theft spell is below cEDH interaction rate. |
| 1 | Olivia, Crimson Bride | Recursion | CUT 1 | six-mana attack recursion is too slow. |
| 1 | Olivia's Wrath | Removal | CUT 1 | current source-package upgrade over stale audit, but five-mana tribal sweeper is below the new natural ceiling. |
| 1 | Otawara, Soaring City | Land | CUT 1 | excellent utility land and serious challenger, but the newest October top-cut 26-land shell omitted it; Mistrise Village and compact colored/fetch density win the utility slots. |
| 1 | Panharmonicon | Blink | CUT 1 | four-mana trigger doubler is exactly the kind of powerful-but-slow optimized card that the Worldgorger loop renders unnecessary. |
| 1 | Patron of the Vein | Removal | CUT 1 | six-mana removal/tribal payoff is far above cEDH rate. |
| 1 | Polluted Delta | Land | RETAIN 1 | premium fetchland. |
| 1 | Preacher of the Schism | Draw | CUT 1 | three-mana incremental combat-state value is too slow. |
| 1 | Rakdos Charm | Removal | CUT 1 | modal utility is broad but two mana and narrow in the key stack windows; compact counters/bounce are superior. |
| 1 | Rakdos Signet | Ramp | CUT 1 | activation-taxed two-mana rock loses to Talisman/Fellwar/free mana. |
| 1 | Reanimate | Recursion | RETAIN 1 | one-mana graveyard recursion; supports Worldgorger setup/recovery and utility creatures. |
| 1 | Reflections of Littjara | Copy | CUT 1 | five-mana tribal copy enchantment is too slow. |
| 1 | Roaming Throne | Copy | CUT 1 | four-mana Evelyn trigger doubler is strong in optimized tribal but does not beat the efficiency of Worldgorger’s repeatable commander ETBs. |
| 1 | Sanctum Seeker | Drain | CUT 1 | four-mana combat drain is outside the combo plan. |
| 1 | Scalding Tarn | Land | RETAIN 1 | premium fetchland. |
| 1 | Scion of Opulence | Ramp | CUT 1 | current source-package upgrade and efficient tribal Treasure support, but combat-death dependency is below cEDH acceleration standards. |
| 1 | Shipwreck Marsh | Land | CUT 1 | conditional untapped land displaced by premium cEDH fixing. |
| 1 | Shivan Reef | Land | CUT 1 | reasonable untapped fixing, but the final 26-land package has stronger rainbow/fetch/dual utility density. |
| 1 | Smoldering Marsh | Land | CUT 1 | frequently enters tapped and is materially below cEDH mana-base standards. |
| 1 | Sol Ring | Ramp | RETAIN 1 | best generic colorless acceleration and strong for a five-mana commander. |
| 1 | Sorin, Imperious Bloodlord | Ramp | CUT 1 | powerful Vampire tribal accelerator, but the rebuilt shell contains too few Vampires and no high-value tribal cheat target. |
| 1 | Steam Vents | Land | RETAIN 1 | fetchable U/R shockland. |
| 1 | Strefan, Maurer Progenitor | Ramp | CUT 1 | four-mana tribal attack/cheat engine is too slow and combat-dependent. |
| 1 | Stromkirk Captain | Anthem | CUT 1 | tribal anthem/combat keyword has no role at the cEDH ceiling. |
| 1 | Sulfur Falls | Land | CUT 1 | conditional land displaced by fully untapped premium fixing. |
| 1 | Sulfurous Springs | Land | CUT 1 | playable untapped painland, but crowded out by the 26-land fetch/dual/rainbow/utility configuration. |
| 1 | Sunken Hollow | Land | CUT 1 | often enters tapped early and loses to Underground Sea/Watery Grave/fetches/rainbow lands. |
| 3 | Swamp | Land | RETAIN 1 / CUT 2 | one basic retained for resilient B access and Tainted Pact uniqueness; duplicate Swamps must leave. |
| 1 | Takenuma, Abandoned Mire | Land | CUT 1 | useful channel land, but final utility slots favor the tournament-tested configuration. |
| 1 | Talisman of Creativity | Ramp | CUT 1 | credible cEDH challenger (~42% aggregate inclusion), but third two-mana Talisman is below the final shell’s free-mana and colored-source priorities; Dominance/Indulgence better match black-intensive lines. |
| 1 | Talisman of Dominance | Ramp | RETAIN 1 | cEDH-rate U/B two-mana rock; 97.9% current Evelyn cEDH staple rate. |
| 1 | Talisman of Indulgence | Ramp | RETAIN 1 | cEDH-rate B/R rock; 77.1% current Evelyn cEDH staple rate. |
| 1 | Toxic Deluge | Removal | CUT 1 | efficient sweeper in slower pods, but three-mana sorcery-speed reset is not part of the final proactive/stack-interaction plan. |
| 1 | Training Center | Land | CUT 1 | strong land, but omitted by the newest top-cut 26-land shell in favor of fetch/dual/rainbow/utility density. |
| 1 | Twilight Prophet | Draw | CUT 1 | four-mana ascend value/drain is far too slow. |
| 1 | Underground River | Land | CUT 1 | playable painland but displaced by Underground Sea, Watery Grave, fetches, rainbow lands, and specialized utility. |
| 1 | Vampiric Tutor | Tutor | RETAIN 1 | one-mana instant tutor and 100% current Evelyn cEDH staple. |
| 1 | Vandalblast | Removal | CUT 1 | sorcery-speed artifact sweep is too narrow/slow; stack interaction and Chain of Vapor handle decisive turns. |
| 1 | Vein Ripper | Drain | CUT 1 | six-mana Vampire threat is not a cEDH combo or interaction piece. |
| 1 | Voldaren Epicure | Draw | CUT 1 | one-mana Vampire gives one Evelyn trigger/Blood token but insufficient ongoing value. |
| 1 | Watery Grave | Land | RETAIN 1 | fetchable U/B shockland. |
| 1 | Xander's Lounge | Land | CUT 1 | always tapped triome is too tempo-negative for the chosen cEDH shell. |

## 5. New candidate package by function

### Commander-native primary win engine
- `Worldgorger Dragon`
- retained `Animate Dead`
- `Dance of the Dead`
- `Necromancy`
- retained `Evelyn, the Covetous`

The loop repeatedly returns Evelyn, triggering collection-counter exile for each player while lands/mana rocks can be tapped between iterations for arbitrarily large mana.

### Compact win endpoints / backups
- `Thassa's Oracle`
- `Demonic Consultation`
- `Tainted Pact`
- `Underworld Breach`
- `Lion's Eye Diamond`
- `Brain Freeze`

### Worldgorger/Breach setup and tutoring
- `Entomb`
- `Unmarked Grave`
- `Faithless Looting`
- `Ripples of Undeath`
- `Imperial Seal`
- `Gamble`
- `Mystical Tutor`
- `Wishclaw Talisman`
- `Praetor's Grasp`
- retained `Demonic Tutor`
- retained `Vampiric Tutor`

### Fast mana / rituals
- `Dark Ritual`
- `Cabal Ritual`
- `Culling the Weak`
- `Rite of Flame`
- `Simian Spirit Guide`
- `Mana Vault`
- `Mox Diamond`
- `Mox Opal`
- `Fellwar Stone`
- retained `Chrome Mox`, `Lotus Petal`, `Sol Ring`, `Arcane Signet`, `Talisman of Dominance`, `Talisman of Indulgence`

### Stack interaction / protection / disruptive bodies
- `Force of Will`
- `Force of Negation`
- `Pact of Negation`
- `Flusterstorm`
- `Swan Song`
- `An Offer You Can't Refuse`
- `Mental Misstep`
- `Mindbreak Trap`
- `Pyroblast`
- `Red Elemental Blast`
- `Redirect Lightning`
- `Stifle`
- `Chain of Vapor`
- `Defense Grid`
- `Spellskite`
- `Hexing Squelcher`
- `Dauthi Voidwalker`
- `Opposition Agent`
- `Orcish Bowmasters`

### Commander-specific timing/exile/ETB exploitation
- retained `Leyline of Anticipation`
- `Borne Upon a Wind`
- `Valley Floodcaller`
- `Party Thrasher`
- `Saw in Half`

`Party Thrasher` is especially identity-positive: Evelyn plays cards from exile, and Party Thrasher grants convoke to noncreature spells cast from exile.

### Competitive draw/selection
- `Mystic Remora`
- `Rhystic Study`
- `Necropotence`
- `Ad Nauseam`
- `Faerie Mastermind`
- `Wan Shi Tong, Librarian`
- `Notion Thief`
- `Windfall`
- `Gitaxian Probe`

## 6. Serious challengers rejected after second pass

- **Into the Flood Maw (58.3% cEDH aggregate):** excellent one-mana tempo interaction, but the candidate already has Chain of Vapor and unusually dense stack protection. `Stifle` appears in both the July and October top-cut Evelyn lists and covers triggered/activated windows bounce cannot. No clean material upgrade established.
- **Wheel of Fortune (56.3%):** strong Breach card, but `Windfall` is the newest top-cut choice and increases blue pitch density for Force of Will/Force of Negation while still functioning as a wheel. No decisive upgrade.
- **Beseech the Mirror (52.1%):** powerful tutor, but black-intensive and bargain-dependent. The candidate already has Demonic Tutor, Vampiric Tutor, Imperial Seal, Gamble, Mystical Tutor, Wishclaw, Entomb, Unmarked Grave and Praetor's Grasp. No need to add another four-mana tutor.
- **Dragon's Rage Channeler (52.1%):** strong Breach enabler, but Faithless Looting + Ripples + Brain Freeze provide graveyard loading while the creature suite prioritizes interaction and exile-specific utility.
- **The One Ring (50.0%):** high raw power, but four mana is slow here and worsens Ad Nauseam pressure; newest top-cut Evelyn omitted it.
- **Hoarding Broodlord (43.8%):** valid reanimation/tutor package, but adds another very high-mana dead draw and a separate line when Evelyn already has a compact commander-native Worldgorger engine.
- **Cyclonic Rift (~41.7%):** baseline card and legitimate cEDH option, but current shell prefers cheaper Chain of Vapor/stack interaction.
- **Talisman of Creativity (~41.7%):** close mana challenger; Dominance/Indulgence better support black-intensive combo/tutor lines and the candidate already has sufficient U/R lands plus free mana.
- **Deflecting Swat (~35.4%):** five-mana commander means it is often not free during the early combo turns where protection matters most.
- **Displacer Kitten:** highly synergistic and present in John Weinhandl's July top-eight list, but the four-mana setup plus five-mana commander is slower than the newest October configuration; Worldgorger already supplies repeatable Evelyn ETBs.
- **Project top-100 Vampire package:** Vampire of the Dire Moon, Anje, Vito, Bloodtithe Harvester, Maskwood Nexus, Arcane Adaptation, etc. are appropriate optimized-tribal candidates but do not compete with the established cEDH engine once Evelyn's actual natural ceiling is recognized.
- **Stale-audit-only five cards:** Anowon, Kindred Dominance, Nighthawk Scavenger, Terminate, Vampire Socialite do not regain entry.

After this challenger pass, **ZERO NEW MATERIAL IMPROVEMENTS** remained.

## 7. Rules red-team conclusions

### Worldgorger + reanimation Aura + Evelyn
`Worldgorger Dragon` plus `Animate Dead`, `Dance of the Dead`, or `Necromancy` generates repeatable permanent blinks and mana. With Evelyn among the returned permanents, each cycle produces a fresh Evelyn ETB trigger and exiles the top card of each player's library with collection counters.

**Mandatory-loop caveat:** if the returning Aura has no creature card other than Worldgorger Dragon available to enchant, the loop cannot simply be stopped by choice; absent outside interruption, it can force a draw. The pilot must establish another legal creature card in a graveyard (or another valid break mechanism) before executing the loop to a deterministic win.

### Evelyn endpoint
Evelyn's static permission is not linked to one specific Evelyn object: it asks whether the collection-counter card was exiled by an ability you controlled. After the Worldgorger loop is broken with Evelyn on the battlefield, one qualifying exiled card may be played that turn. If `Thassa's Oracle` was exiled during the loop, infinite mana allows it to be cast from exile; with the library emptied, its ETB can win.

### Thoracle backup
`Thassa's Oracle` + `Demonic Consultation` is a compact independent win. `Tainted Pact` also functions because the exact candidate has **100 distinct card names**; naming a card absent from the deck can exile the entire remaining library without encountering duplicate names.

### Breach backup
`Underworld Breach` + `Lion's Eye Diamond` + `Brain Freeze` is a standard near-infinite storm/self-mill engine with the documented graveyard-card prerequisite. It provides an independent cEDH finish if Worldgorger is disrupted.

### Vexing Bauble
Vexing Bauble is symmetrical. While it remains on the battlefield it can counter the candidate's own no-mana-spent spells such as free-cast Force/Pact lines and zero-cost spells cast without mana spent. Its `{1}, T, sacrifice: draw` ability is therefore an intentional escape valve before committing a protected combo turn.

### Saw in Half + Evelyn
Saw in Half creates two token copies only if Evelyn is actually destroyed and **dies**. If a commander replacement moves Evelyn directly to the command zone instead of the graveyard, that condition is not satisfied. If she dies, the two Evelyn copies enter simultaneously. Each token sees itself and the other entering Vampire, so four Evelyn triggers trigger in total. Before those triggers are put on the stack, state-based actions apply the legend rule and one token is kept; the already-triggered abilities are then put on the stack and can resolve.

## 8. Structural target

- Total: **100**
- Distinct names: **100**
- Commander: **1**
- Candidate lands: **26**
- Duplicate names: **0**
- Color identity target: **B/R/U**
- Official Commander legality target: **PASS**
- Project exceptions: **none**
- Natural ceiling: **Bracket 5 — cEDH**
- Proposed Archidekt tags: **Worldgorger / Exile / Combo**

## 9. Approval state

This record does **not** approve or lock Evelyn. The candidate must still pass the fresh SHA-bound Oracle/color-identity/official-legality/rules/structural complete gate, and explicit user approval is required afterward.
