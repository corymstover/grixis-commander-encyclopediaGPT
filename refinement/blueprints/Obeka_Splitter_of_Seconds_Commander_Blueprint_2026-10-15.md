# Obeka, Splitter of Seconds — Commander-First Blueprint

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #45 of 62

## Identity

**Natural ceiling: Power Bracket 4 — Optimized.**

Primary identity: **Extra Upkeeps / Combat Damage / Upkeep Triggers**.

Obeka is a four-mana 2/5 Ogre Warlock with menace. Whenever she deals combat damage to a player, her controller gets that many additional upkeep steps after that combat phase. Under the official rules treatment, those upkeep steps occur in additional beginning phases whose untap and draw steps are skipped. The deck therefore treats **actual combat damage dealt by Obeka** and **additional instances of Obeka's combat-damage trigger** as its primary resource multipliers.

The commander-first sequence is:

1. resolve and protect Obeka;
2. force combat connection;
3. increase her actual combat damage and/or multiply her combat-damage trigger;
4. convert the resulting additional upkeeps into cards, Treasures, Clues, counters, tokens, life pressure, monarch value, suspend acceleration, artifact production, and alternate wins;
5. use Time Sieve when upkeep-generated artifacts support repeatable extra turns.

## Final engine priorities

### Damage and trigger multiplication
- **Mjölnir, Hammer of Thor** — doubles damage Obeka would deal; Obeka is worthy, so equip worthy is `{1}`.
- **Dragonfire Blade** — three-color Obeka reduces equip `{4}` to `{1}`; +2/+2 directly increases added-upkeep count while hexproof from monocolored protects the commander.
- **Hatred** — converts life into +X/+0 at instant speed; every additional point that connects becomes another upkeep.
- **Roaming Throne** — choose Ogre or Warlock; Obeka's combat-damage ability triggers an additional time.
- **Wizard's Staff** — gives Obeka prowess and causes her triggered abilities to trigger an additional time; Obeka uses normal equip `{3}` because she is a Warlock, not a Wizard.
- **Combat Research, Embercleave, Sword of Feast and Famine, Black-color Rings** and the retained equipment package continue to raise damage, create multiple damage events, or improve connection.

### Efficient upkeep engines
- **Super Intelligence** — one mana turns every upkeep of enchanted Obeka's controller into a card draw.
- **Smaug the Magnificent** — each controller upkeep creates a Treasure; Obeka-created upkeeps therefore generate one-sided artifact acceleration, and Smaug's attack trigger converts accumulated Treasures into damage.
- **Tamiyo's Journal** — each controller upkeep investigates; extra upkeeps generate Clues, which are card draw, tutor fuel, and Time Sieve material.
- **Darksteel Reactor** — every controller upkeep can add a charge counter; twenty counters win the game. Obeka can compress many Reactor counters into a single postcombat sequence.
- Retained engines include all six Courts, As Foretold, Bonehoard Dracosaur, Creeping Bloodsucker, Dragonmaster Outcast, Extravagant Replication, Mechanized Production, Phyrexian Arena, Plargg and Nassari, Replicating Ring, Thopter Spy Network, Thassa, and Twilight Prophet.

### Suspend / time-counter leverage
Ancestral Vision, Inspiring Refrain, Jhoira of the Ghitu, Profane Tutor, Rousing Refrain, Suspended Sentence, As Foretold, and Replicating Ring all improve when extra upkeeps rapidly advance time/counter-based engines.

### Artifact extra-turn package
Time Sieve remains commander-appropriate because Thopter Spy Network, Smaug, Tamiyo's Journal, Replicating Ring, Mechanized Production, Court of Vantress, and other artifacts can turn Obeka-created upkeeps into expendable artifacts. The deck does not treat Sieve as an unconditional three-card combo from an empty board; board state and artifact cadence matter.

## Identity constraints

- Do **not** convert this into generic Grixis cEDH. Project reranking and current evidence support Bracket 4, not a tournament-established cEDH ceiling.
- Do **not** add generic extra turns or Oracle/Consultation/Breach packages merely because they raise abstract power.
- Do not spend more slots on evasion once the commander already has menace plus Aqueous Form, Brotherhood Regalia, Silver Shroud Costume, Greaves, Boots, Thassa, Shizo, and Silent Arbiter.
- Prefer cards whose output scales directly with **Obeka-created upkeeps** or **Obeka's damage**.
- Keep **35 lands**; Obeka costs four and the deck retains several four-to-six-mana upkeep engines.

## Final hybrid reconciliation

Two serious working candidates existed during the current-cycle review. The earlier repository candidate emphasized Mjölnir / Dragonfire Blade / Hatred / Ginger / Palace Siege. A later challenger emphasized Smaug / Super Intelligence / Darksteel Reactor / Tamiyo's Journal / Aggravated Assault / Blackblade Reforged.

The final adversarial comparison produced a hybrid:

**Retained from the earlier candidate:** Mjölnir, Dragonfire Blade, Hatred, Roaming Throne, Wizard's Staff.  
**Adopted from the challenger:** Smaug, Super Intelligence, Darksteel Reactor, Tamiyo's Journal.  
**Rejected at final slot stage:** Ginger, Palace Siege, Aggravated Assault, Blackblade Reforged.

Reasons:
- Smaug is cheaper and one-sided compared with Ginger while generating the Treasures specifically during the controller's extra upkeeps.
- Super Intelligence costs only one mana and converts each extra upkeep directly into another card, beating the five-mana Palace Siege on rate in the final shell.
- Darksteel Reactor supplies a resilient commander-native alternate win whose counter clock is compressed by extra upkeeps.
- Tamiyo's Journal supplies both artifact generation and unrestricted tutoring from the same upkeep engine.
- Aggravated Assault + Sword of Feast and Famine is powerful but substantially more generic and did not beat a commander-native upkeep engine for the final slot.
- Blackblade Reforged is a strong damage amplifier but redundant after Mjölnir, Dragonfire Blade, Hatred, Embercleave, Combat Research, and the three scaling Rings.

## Current-cycle structure

- Baseline: **100 cards / 94 distinct names / 35 lands**.
- Final approval-ready candidate: **100 cards / 96 distinct names / 35 lands**.
- Candidate repeats: **Island x3 / Mountain x2 / Swamp x2 only**.
- Whole-list result: **80 KEEP / 19 CUT across all 99 baseline noncommander copies**.
- No project legality exception required.
- Recommended Archidekt tags: **Extra Upkeeps / Combat Damage / Upkeep Triggers**.

Candidate SHA-256: `83062ff2dbc955c628f9a6df460cf72dd5d450b6685bc4b53f63894bc8c321fb`
