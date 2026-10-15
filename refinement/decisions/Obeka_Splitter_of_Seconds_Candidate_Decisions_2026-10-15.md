# Obeka, Splitter of Seconds — Current-Cycle Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #45 of 62  
Status: working decision closeout; not user approval

Exact candidate SHA-256: `9846e43dbe74fe49a9d356e944dc0a05d7dee30015e0d36e667fdbd01cb1ee75`

## Final 17-card delta from authoritative FINAL baseline

### Strategic changes

| Cut | Add | Decision basis |
|---|---|---|
| Blasphemous Act | Roaming Throne | Replace redundant second wipe with a four-mana creature that, choosing Ogre or Warlock, causes Obeka's defining combat-damage trigger to trigger an additional time. |
| Descent into Avernus | Palace Siege | Replace a dangerously symmetrical accelerating upkeep trigger with Dragons mode: each extra upkeep drains every opponent for 2 while gaining 2 life. |
| Lizard Blades | Mjölnir, Hammer of Thor | Replace double strike reconfigure with a current damage doubler whose worthy equip is `{1}` on red legendary non-Villain Obeka and whose ETB can remove a creature. |
| Scrawling Crawler | Hatred | Replace symmetrical opponent card refill with an instant-speed life-to-power finisher; every added point of actual combat damage becomes another Obeka upkeep. |
| Skyline Despot | Ginger, Queen of Sweets | Reduce the monarch token engine by one mana and change it to an artifact-token engine that triggers at every upkeep while monarch, directly supporting Time Sieve. |
| Strionic Resonator | Wizard's Staff | Resonator charges `{2}` for each copied trigger; Staff requires `{3}` to equip to non-Wizard Obeka but then passively causes her trigger to trigger an additional time and adds prowess. |
| Winged Boots | Dragonfire Blade | Replace redundant flying/ward equipment with `{1}` equip on three-color Obeka for +2/+2 and hexproof from monocolored, turning a base connection from 2 upkeeps into 4. |

### Mana-base changes

| Cut | Add | Decision basis |
|---|---|---|
| Dragonskull Summit | Arid Mesa | Premium fetchable typed-dual/tri-land access. |
| Drowned Catacomb | Flooded Strand | Premium fetch. |
| Shipwreck Marsh | Marsh Flats | Premium fetch. |
| Stormcarved Coast | Misty Rainforest | Premium fetch. |
| Sulfur Falls | Verdant Catacombs | Premium fetch. |
| Exotic Orchard | Wooded Foothills | Premium fetch; removes opponent-dependent fixing. |
| Reliquary Tower | Mana Confluence | Replace colorless hand-size utility with guaranteed U/B/R fixing. |
| 1x Island | City of Brass | Improve fixing while retaining three Islands. |
| 1x Mountain | Reflecting Pool | Improve fixing while retaining two Mountains. |
| Rogue's Passage | Arena of Glory | Existing evasion density makes four-mana Passage activation redundant; Arena can accelerate Obeka and grant haste when its special mana is spent on her creature spell. |

## Rules-critical conclusions

### Additional upkeeps are additional beginning phases

Obeka's trigger creates the stated number of additional upkeep steps after the current combat phase. Because upkeep exists only inside a beginning phase, each extra upkeep is effectively an additional beginning phase with untap and draw skipped. `At the beginning of your upkeep` abilities trigger in every one of these added upkeeps.

### Damage amount is the resource multiplier

Obeka counts the combat damage actually dealt. Effects that increase her power or modify dealt damage therefore directly change the number of additional upkeeps.

- **Dragonfire Blade:** Obeka is U/B/R, so its equip `{4}` costs `{1}` when targeting her. She becomes 4/7 and has hexproof from monocolored; an unmodified connection creates four additional upkeeps.
- **Mjölnir:** Obeka is legendary, red, and not a Villain, so she is worthy. Equip worthy costs `{1}`. Its damage-doubling replacement modifies the combat damage actually dealt; a base 2-power hit becomes 4 damage and therefore four additional upkeeps.
- **Hatred:** life paid as an additional casting cost becomes +X/+0. If Obeka connects, that increased power becomes increased actual combat damage and therefore increased upkeep count.
- **Combat Research / Sword / color Rings / Embercleave:** these retained cards likewise raise damage, protection, or the number of combat-damage events rather than merely adding unrelated Voltron stats.

### Trigger multipliers are additive

Roaming Throne and Wizard's Staff each say the relevant triggered ability triggers an additional time. With both affecting Obeka, a single combat-damage event produces the original Obeka trigger plus one additional instance from each effect: three Obeka trigger instances total, not four. Each instance uses the combat damage dealt by Obeka for that event.

Wizard's Staff replaced Strionic Resonator at final red-team because Staff has a higher initial setup cost but no recurring `{2}` payment and additionally grants prowess. Obeka is a Warlock, not a Wizard, so Staff's normal equip `{3}` applies.

### Combat Research with trigger multipliers

Combat Research grants the enchanted creature the combat-damage draw trigger. That makes the granted trigger a triggered ability of Obeka. Wizard's Staff and a Roaming Throne choosing Ogre or Warlock can therefore each cause that granted draw ability to trigger an additional time as well. Combat Research also gives legendary Obeka +1/+1 and ward `{1}`, so it simultaneously increases upkeep output and protection.

### Double strike

If Embercleave gives Obeka double strike and she deals combat damage in both combat-damage steps, Obeka triggers separately for each damage event. The extra beginning phases created by those triggers are inserted after the combat phase ends.

### Time Sieve / Thopter Spy Network — corrected stable loop accounting

Thopter Spy Network creates an artifact Thopter at the beginning of each of your upkeeps if you control an artifact. Time Sieve itself is an artifact, so if **Time Sieve and Thopter Spy Network are already on the battlefield as your normal upkeep begins**, Sieve satisfies Network's intervening-if condition and Network creates the first Thopter of the turn.

If Obeka then connects for at least 4 combat damage, she creates four postcombat additional upkeeps and Network creates four more Thopters. The turn has therefore generated **five expendable Thopters total**: one from the normal upkeep plus four from the added upkeeps. Time Sieve can tap and sacrifice those five Thopters to create an extra turn while remaining on the battlefield.

On the resulting extra turn, the same established board creates one Thopter in the normal upkeep and four more after another 4-damage Obeka connection, replenishing five artifacts for the next Sieve activation. Thus, once this board is established and Obeka can continue connecting for at least 4 damage each turn, the package supports repeatable extra turns without an additional expendable seed artifact. If Network or Sieve enters only after the normal upkeep, or if fewer than four postcombat added upkeeps are generated, additional artifact material is required for that turn's activation.

The deck does **not** claim that Obeka + Network + Sieve alone guarantee the loop from every board state: Obeka must actually connect for enough damage and all pieces must survive.

### Ginger / Time Sieve

Ginger enters as an artifact creature and makes its controller the monarch. At the beginning of **each** upkeep, if that player remains monarch, Ginger creates a Gingerbrute artifact-creature token. Obeka-created upkeeps therefore generate artifact material for Time Sieve. With Ginger and Sieve established before a turn and the monarch retained, the normal upkeep plus four additional upkeeps from a 4-damage Obeka hit likewise generates five Gingerbrutes for Sieve.

### Palace Siege

Dragons mode triggers at each controller upkeep; every Obeka-created upkeep causes each opponent to lose 2 life and the controller to gain 2 life. This is deliberately preferred to Descent into Avernus because it converts large upkeep counts asymmetrically rather than handing opponents accelerating Treasure resources.

## Candidate exhaustion — notable rejected alternatives

- **Bitterbloom Bearer — REJECT at final stage.** Two mana and excellent upkeep synergy, but each Obeka-created upkeep also costs life and its Faerie tokens are not artifacts. The final list already has dense token/upkeep payoffs; Ginger contributes monarch and Time Sieve material while Hatred/Dragonfire/Mjölnir directly improve Obeka's multiplier.
- **Genji Glove — REJECT.** Double strike plus an additional combat can create very large upkeep counts, but `{5}` cast plus `{3}` equip is too much setup compared with Mjölnir, Dragonfire Blade, Embercleave, and the retained cheap connection package.
- **Hall of Echoes — REJECT.** Copying Obeka is commander-relevant, but the land only produces colorless mana and needs `{5}` before combat to become a copy. That is too much color and tempo strain in a U/B/R four-mana commander deck.
- **Aether Tunnel — REJECT.** Good evasion, but the final build already has multiple unblockable/menace/protection routes and needs slots that increase the multiplier rather than simply duplicate connection.
- **Rilsa Rael, Kingpin — REJECT.** Initiative is genuine upkeep synergy and completing a dungeon can add +5/+0 to an attacker, but five-mana setup plus a contestable initiative subsystem is less direct than the finalized multipliers and upkeep engines.
- **Darksteel Reactor — REJECT at final slot stage.** Highly synergistic alternate win, but four mana produces no immediate resource or protection before twenty counters. Mechanized Production already supplies an upkeep-accelerated alternate win while generating artifact copies, and Time Sieve supplies an artifact-based turn engine.
- **Tamiyo's Journal — REJECT at final slot stage.** Excellent asymmetric upkeep artifact/tutor engine, but at five mana it loses the curve contest to two-mana Generous Plunderer, which can ramp before Obeka arrives and turns every added upkeep into immediately usable Treasure. The opponent's tapped Treasure is a real downside but does not overcome the tempo difference in this exact build.
- **Robe of the Archmagi — REJECT at final slot stage.** Obeka can equip it for `{1}` and it has a higher draw ceiling, but Combat Research costs only `{U}`, adds +1/+1 and ward `{1}`, directly raises the upkeep count, and its granted draw trigger is itself multiplied by Staff/Throne.
- **Blackblade Reforged — REJECT at final slot stage.** Powerful persistent damage boost, but Mjölnir scales multiplicatively with all other buffs and adds removal, while Sword of Feast and Famine supplies protection, pressure, and a full land untap. Blackblade is a strong alternative rather than a net upgrade.
- **Sphinx of the Second Sun — REJECT.** Eight mana for another beginning phase is too inefficient when Obeka herself creates multiple additional beginning phases from combat damage.
- **The Ninth Doctor — REJECT.** Extra upkeep support is thematic, but the final slot competition favors cheaper and higher-output commander multipliers.
- **Braid of Fire — REJECT.** Extra cumulative-upkeep triggers can create red mana, but that mana is constrained to upkeep timing and is less broadly useful than current payoff slots.
- **Additional generic fast mana — REJECT.** Mox/one-shot acceleration could improve raw speed, but the list's limiting factor is colored U/B/R access and connecting/profiting from Obeka. No generic fast-mana addition beat a finalized commander-native slot.
- **Generic extra turns / Oracle-Consultation / unrelated Breach combo — REJECT.** These increase abstract power while making Obeka less necessary and exceed the commander's natural Bracket-4 identity.

## Mana-base red team

Land count remains **35**. The final mana package uses nine fetchlands (Arid Mesa, Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills), original duals, shocks, Xander's Lounge, City of Brass, Mana Confluence, Command Tower, Reflecting Pool, multiplayer lands, Arena of Glory, Shizo, Otawara, Urborg, Ancient Tomb, and seven basics total (Island x3 / Mountain x2 / Swamp x2).

No land-count reduction survived review because the commander costs four and multiple defining upkeep engines cost four through six mana. Arena of Glory is accepted despite being red-only because its special mana can help cast Obeka and grant haste, while the rest of the upgraded base materially increases three-color consistency.

## Natural ceiling

Project reranking places Obeka, Splitter of Seconds in **Bracket 4 — Optimized**, with strong commander-synergy/cohesion but no usable tournament sample supporting a cEDH classification. Current optimized community data remains centered on Extra Upkeeps, Voltron, Extra Turns, and Monarch rather than a stable cEDH shell. The final build maximizes that natural strategy rather than overriding it.

## Final red-team result

The final serious pass challenged all 17 swaps, every baseline slot, trigger arithmetic, combat-damage modifiers, extra-upkeep phase rules, artifact-turn sequencing, evasion density, mana color requirements, current 2026 cards, Darksteel Reactor, Tamiyo's Journal, Robe of the Archmagi, Blackblade Reforged, Rilsa Rael, and generic higher-power alternatives.

Wizard's Staff produced one material improvement over the first working candidate and was incorporated. The later Time Sieve red-team produced a **documentation correction only**: the established Network + Sieve board uses Time Sieve itself to satisfy Network's artifact condition during the normal upkeep, so a 4-damage Obeka connection generates the fifth Thopter needed for Sieve without another expendable seed artifact. The 100-card candidate is unchanged.

After those corrections, no remaining challenger produced a material net improvement.

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Decision closeout: PASS — candidate is APPROVAL_READY evidence only, not approved/locked.**
