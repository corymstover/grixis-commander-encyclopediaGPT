# Obeka, Splitter of Seconds — Current-Cycle Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #45 of 62  
Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15

Exact candidate SHA-256: `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`

## Final 19-card delta from authoritative FINAL baseline

### Strategic changes

| Cut | Add | Decision basis |
|---|---|---|
| Blasphemous Act | Roaming Throne | Replace redundant second wipe with a four-mana creature that, choosing Ogre or Warlock, makes Obeka's defining combat-damage trigger trigger an additional time. |
| Descent into Avernus | Darksteel Reactor | Replace dangerous symmetrical upkeep acceleration with an indestructible one-sided alternate win whose charge-counter clock is directly compressed by Obeka's extra upkeeps. |
| Generous Plunderer | Smaug the Magnificent | Plunderer gives an opponent a tapped Treasure every time its multiplied upkeep trigger makes one for us. Smaug creates one-sided Treasures at each of our upkeeps, has flying/haste, and converts Treasure count into attack damage. |
| Lizard Blades | Mjölnir, Hammer of Thor | Mjölnir doubles all damage equipped Obeka deals, uses equip worthy `{1}`, and enters with a four-damage removal mode. It is a cleaner commander-damage multiplier than retaining the reconfigure double-strike body. |
| Mithril Coat | Tamiyo's Journal | Protection is already dense; Journal turns every added upkeep into a Clue and converts three Clues into any card, while the Clues also support Time Sieve and card draw. |
| Scrawling Crawler | Hatred | Remove symmetrical opponent card refill for an instant-speed life-to-power finisher; increased actual combat damage becomes increased upkeep count. |
| Skyline Despot | Super Intelligence | Seven-mana monarch payoff becomes a one-mana Aura that draws a card at every upkeep of enchanted creature's controller. |
| Strionic Resonator | Wizard's Staff | Resonator requires recurring `{2}` for each copied trigger. Staff's normal equip is `{3}` on Warlock Obeka, then passively adds an extra instance of her triggers and grants prowess. |
| Winged Boots | Dragonfire Blade | Redundant flying/ward becomes `{1}` equip on three-color Obeka for +2/+2 and hexproof from monocolored, directly raising the number of added upkeeps on connection. |

### Mana-base changes

| Cut | Add | Decision basis |
|---|---|---|
| Dragonskull Summit | Arid Mesa | Premium fetchable typed-dual/tri-land access. |
| Drowned Catacomb | Flooded Strand | Premium fetch. |
| Shipwreck Marsh | Marsh Flats | Premium fetch. |
| Stormcarved Coast | Misty Rainforest | Premium fetch. |
| Sulfur Falls | Verdant Catacombs | Premium fetch. |
| Exotic Orchard | Wooded Foothills | Premium fetch; removes opponent-dependent fixing. |
| Reliquary Tower | Mana Confluence | Colorless utility becomes guaranteed U/B/R fixing. |
| 1x Island | City of Brass | Improve fixing while retaining three Islands. |
| 1x Mountain | Reflecting Pool | Improve fixing while retaining two Mountains. |
| Rogue's Passage | Arena of Glory | Existing evasion makes the four-mana Passage activation redundant; Arena can accelerate Obeka and grant haste when its generated mana is spent on her spell. |

## Structural effect

- Baseline: **100 cards / 94 distinct names / 35 lands**.
- Candidate: **100 cards / 96 distinct names / 35 lands**.
- Whole-list audit: **80 KEEP / 19 CUT across all 99 noncommander copies**.
- Candidate repeats: **Island x3 / Mountain x2 / Swamp x2 only**.
- Strategic changes: **9 cuts / 9 additions**.
- Land changes: **10 cuts / 10 additions**.

## Rules-critical conclusions

### Added upkeeps
Obeka's trigger creates a number of additional upkeep steps equal to the combat damage she dealt to a player. Rules implementation places those upkeeps in additional beginning phases after the combat phase, with untap and draw skipped. `At the beginning of your upkeep` abilities trigger during each of them.

### Damage amount is the central multiplier
- **Dragonfire Blade:** Obeka has three colors, so equip `{4}` costs `{1}` when targeting her. +2/+2 raises base combat damage from 2 to 4 and therefore raises the base added-upkeep count from 2 to 4 when she connects.
- **Mjölnir:** Obeka is legendary, red, and not a Villain, so she is worthy. Equip worthy `{1}` applies. The damage-doubling replacement changes the combat damage actually dealt, so Obeka counts the doubled amount.
- **Hatred:** life paid as the additional cost becomes +X/+0 until end of turn. Successful combat damage converts that power directly into added upkeeps.
- **Combat Research / Embercleave / Sword / color Rings:** retained because they raise damage, create multiple damage events, or make future hits larger.

### Trigger multiplication
Roaming Throne and Wizard's Staff each cause the relevant triggered ability to trigger an additional time. If both apply to Obeka, one combat-damage event creates **three total Obeka trigger instances**: original + Staff + Throne. These effects are additive, not multiplicative.

Wizard's Staff also grants prowess to the equipped creature. Obeka is a Warlock, not a Wizard, so normal equip `{3}` applies.

### Double strike
If Embercleave gives Obeka double strike and she deals combat damage in both combat-damage steps, her ability triggers separately for each damage event. Trigger multipliers apply to each event independently.

### Super Intelligence
The Aura triggers at the beginning of the enchanted creature controller's upkeep. Enchanting Obeka means every normal or Obeka-created upkeep produces another draw while the Aura and creature remain on the battlefield.

### Smaug the Magnificent
Smaug creates a Treasure at the beginning of each controller upkeep. Every Obeka-created upkeep therefore creates another Treasure. Smaug's attack trigger then deals damage equal to the number of Treasures controlled to any target. Unlike Generous Plunderer, Smaug does not give an opponent a Treasure as part of that upkeep engine.

### Darksteel Reactor
Reactor is indestructible and can receive a charge counter during each controller upkeep. Obeka-created upkeeps accelerate its twenty-counter alternate win condition directly. Each resulting upkeep independently supplies another Reactor trigger.

### Tamiyo's Journal
Journal investigates at the beginning of each controller upkeep, so extra upkeeps create extra Clues. Three Clues can be sacrificed to tutor any card. A Clue cannot be sacrificed simultaneously to Journal and Time Sieve, so artifact accounting must respect the separate costs; the deck's high upkeep count can generate enough Clues for either function as board state permits.

### Time Sieve / Thopter Spy Network
Thopter Spy Network triggers at each controller upkeep if an artifact is controlled. Time Sieve itself is an artifact, so an established Sieve + Network board satisfies Network's intervening-if condition at normal upkeep.

If Obeka then connects for at least 4 damage, Network produces one Thopter at the normal upkeep plus four during the postcombat added upkeeps. Those five expendable artifacts can fuel Time Sieve for an extra turn while Sieve remains. On the extra turn, the same cadence can repeat if Obeka connects again and the permanents survive. This is an established-board repeatable-turn engine, not an unconditional loop from an empty battlefield.

Smaug and Tamiyo's Journal provide additional artifact cadence for Sieve, but their tokens must still be counted honestly against any other sacrifice/tutor costs.

### Arena of Glory
If any mana produced by its exert ability is spent on Obeka's creature spell, the resulting Obeka gains haste until end of turn, enabling immediate combat and therefore immediate extra-upkeep generation.

## Hybrid candidate reconciliation

The repository initially contained a SHA-bound working candidate at `9846e43d...` using Ginger, Queen of Sweets and Palace Siege. A later research pass independently produced a different candidate emphasizing Smaug, Super Intelligence, Darksteel Reactor, Tamiyo's Journal, Aggravated Assault, and Blackblade Reforged.

The conflict was resolved explicitly rather than silently overwriting either strategic rationale.

### Accepted from the first candidate
- Mjölnir, Hammer of Thor
- Dragonfire Blade
- Hatred
- Roaming Throne
- Wizard's Staff

### Accepted from the later challenger
- Smaug the Magnificent
- Super Intelligence
- Darksteel Reactor
- Tamiyo's Journal

### Rejected after head-to-head comparison
- **Ginger, Queen of Sweets:** powerful and valid, but six mana and monarch dependency lose to four-mana Smaug for the final artifact-upkeep slot. Ginger triggers on all players' upkeeps, but Obeka specifically creates additional upkeeps for her controller; Smaug captures the commander-created cadence at materially lower mana.
- **Palace Siege:** excellent five-mana drain engine, but Super Intelligence turns every extra upkeep into another card for only one mana, while the deck already has Court of Ire, Court of Ambition, Creeping Bloodsucker, and other ways to convert upkeep volume into pressure.
- **Aggravated Assault:** strong with retained Sword of Feast and Famine and extra combats naturally retrigger Obeka. However, the Assault/Sword loop is a generic two-card combat engine that works without Obeka; no commander-native engine was weaker enough to justify the homogenizing slot.
- **Blackblade Reforged:** efficient large pump on a legendary creature, but redundant with Mjölnir, Dragonfire Blade, Hatred, Embercleave, Combat Research, and the three Rings, all of which already create a dense damage-growth package.
- **Robe of the Archmagi:** Obeka is a Warlock so Robe equips for `{1}` and can draw cards equal to damage, but it does not itself increase combat damage/upkeep count. Combat Research costs one mana, gives legendary Obeka +1/+1, and therefore directly increases commander output while still drawing.
- **The Ninth Doctor / Shadow of the Second Sun / Sphinx of the Second Sun:** each can add beginning-phase/upkeep value, but they are materially more expensive for only one additional upkeep/beginning phase compared with Obeka's scalable trigger.

## Mana-base red team

Land count remains **35**.

Final premium structure includes:
- nine fetchlands: Arid Mesa, Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Verdant Catacombs, Wooded Foothills;
- original duals Badlands, Underground Sea, Volcanic Island;
- shocks Blood Crypt, Steam Vents, Watery Grave;
- Xander's Lounge;
- City of Brass, Mana Confluence, Command Tower, Reflecting Pool;
- Luxury Suite, Morphic Pool, Training Center;
- Ancient Tomb, Arena of Glory, Shizo, Otawara, Urborg;
- Island x3, Mountain x2, Swamp x2.

No land-count reduction survived review because Obeka costs four and several defining upkeep engines cost four through six mana.

## Natural ceiling

Project reranking places Obeka, Splitter of Seconds in **Power Bracket 4 — Optimized** with very high commander-synergy/cohesion and no usable tournament sample supporting cEDH. The finalized package therefore maximizes the natural extra-upkeep strategy instead of importing a generic Oracle/Consultation or Breach shell.

## Final red-team result

The final serious pass challenged:
- all 99 baseline slots;
- both conflicting working candidates;
- every final strategic swap;
- damage and trigger arithmetic;
- upkeep-phase structure;
- Time Sieve artifact accounting;
- protection/evasion density;
- interaction density;
- mana requirements and all 35 lands;
- current 2026 additions;
- generic extra-combat, generic extra-turn, and cEDH alternatives.

The material improvement discovered by the conflict review was the **final hybrid** now bound to SHA `83062ff2...`. After incorporating Smaug, Super Intelligence, Darksteel Reactor, and Tamiyo's Journal while preserving the stronger Mjölnir/Dragonfire/Hatred package, no remaining challenger produced a material net improvement.

**ZERO NEW MATERIAL IMPROVEMENTS.**

**Decision closeout: PASS — candidate is APPROVAL_READY evidence only, not approved/locked.**

## Approval closeout

- Explicit user approval received: **2026-10-15**
- Canonical approved SHA-256: `c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63`
- Exact approved artifact: `refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt`
- Current-cycle state: **APPROVED / LOCKED**
- Quality gate: **Deck Quality Gates v3 + mandatory whole-list audit + hybrid reconciliation + approval-ready verification**
- Next unlocked deck in tracker order: **Parnesse, the Subtle Brush (index 45 / deck 46 of 62)**.
