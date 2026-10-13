# Admiral Beckett Brass — Commander-First Blueprint v1

**Review date:** 2026-10-13  
**Deck order:** #2 of 62 (tracker index 1)  
**Baseline authority:** frozen 2026-10-12 FINAL CSV/TXT exports  
**Decklist status:** unchanged; research only  
**CSV SHA-256:** `e6a2333e036935248c03705946576a461cb53bf78b30a1c6bda162e4f38c8dde`  
**TXT SHA-256:** `e9e161a015e8b86057d4d76424f901a0700715712cc542a78f9c74c6eabe21dc`

## 1. Commander identity and strategic thesis

Admiral Beckett Brass gives other Pirates +1/+1 and, at the beginning of its controller's end step, can permanently gain control of a target nonland permanent controlled by a player dealt combat damage by three or more Pirates that turn.

The deck must do more than be generic Grixis goodstuff: it needs a reliable way to connect with **three Pirates to the same opponent** while maintaining enough bodies to repeat the theft trigger. The natural plan is proactive Pirate aggro with evasive attackers and token production, backed by tribal pumps, combat-damage draw, Treasure acceleration, protection/removal, and a secondary permanent-theft package.

### Primary success conditions

1. Establish three or more Pirates that can connect with the same opponent in one turn.
2. Preserve enough Pirate density that Beckett's anthem and the theft condition remain relevant.
3. Use evasion and token production to overcome blockers; prioritize repeatable access over one-shot effects unless a one-shot effect converts a key combat into a decisive theft/finish.
4. Exploit combat damage for cards and Treasures, then use the mana and stolen resources to keep pressure on the table.
5. Retain interaction and protection so the deck can recover from blockers, removal, and sweepers without abandoning its Pirate identity.

## 2. Frozen baseline snapshot

The authoritative TXT export has 100 cards total, 97 distinct card-name rows, and three Island plus two Mountain as the only repeated quantities (the commander is included in the 100). No list changes are authorized by this blueprint.

Existing identity-bearing pieces include:
- **Evasion/connection:** Changeling Outcast, Cover of Darkness, Daring Saboteur, Fathom Fleet Captain, Siren Stormtamer, Storm Fleet Sprinter, Warkite Marauder.
- **Tokens/board development:** Daring Piracy, Kari Zev, Fathom Fleet Captain, Black Market Connections.
- **Pirate combat payoffs:** Admiral Beckett Brass, Captain Vargus Wrath, Dire Fleet Captain, Dire Fleet Neckbreaker, Shared Animosity.
- **Combat draw/value:** Bident of Thassa, Coastal Piracy, Kindred Discovery, Breeches, Brazen Plunderer, Malcolm, Alluring Scoundrel, Ramirez DePietro, Pillager.
- **Treasure/ramp:** Malcolm, Keen-Eyed Navigator, Captain Lannery Storm, Breeches, Eager Pillager, Edward Kenway, Storm the Vault, Ragavan, and conventional mana rocks.
- **Additional theft/value:** Coercive Recruiter, Don Andres, the Renegade, Hostage Taker, Zara, Renegade Recruiter.
- **Combat finisher:** Port Razer.
- **Protection/interaction:** Deflecting Swat, Fierce Guardianship, Lightning Greaves, Siren Stormtamer, efficient removal and counterspells, Fiery Cannonade, and Raise the Palisade.

## 3. Initial candidate shortlist — research queue, not recommendations

Candidate rankings are a discovery aid, not automatic additions. The following candidates deserve individual comparison because they support specific deck requirements:

| Candidate | Current ranking | Commander-specific reason to examine | Main concern to test |
|---|---:|---|---|
| Slippery Scoundrel | #11 | Pirate body that becomes unblockable and gains hexproof with the city's blessing; helps reliably connect for the three-Pirate condition. | Three-mana slot; ascend timing; compare against existing evasion density. |
| Open into Wonder | #16 | Can make multiple creatures unblockable and converts those hits into cards; directly enables the commander threshold. | One-shot sorcery and mana demand; compare against repeatable evasion already in the list. |
| Kitesail Freebooter | #17 | Evasive Pirate that disrupts a noncreature/nonland card from an opponent's hand. | Temporary disruption and body quality versus current interaction suite. |
| The Indomitable | #2 | Draws when any creature controlled deals combat damage to a player, scaling with the deck's wide attacks. | Four-mana non-Pirate Vehicle; existing Bident/Coastal Piracy/Kindred Discovery density; must demonstrate a material upgrade. |
| Fell Flagship | #4 | Three-mana Pirate anthem effect for the team plus combat-damage discard when the Vehicle connects. | Non-Pirate permanent and overlap with existing tribal pumps. |
| Gemcutter Buccaneer | #20 | Turns Pirate entries into Treasures and makes Treasures function as equipment; potential ramp and board scaling. | Four-mana cost and whether the equipment/Treasure text is more than incidental value. |
| Captain Storm, Cosmium Raider | #26 | Two-mana Pirate that grows a Pirate whenever an artifact enters; this list creates Treasures. | Counter growth does not itself solve the three-Pirate connection requirement. |
| Protean Raider | #8 | Potentially copies a high-value creature after attacking. | Raid timing and retaining Pirate type are material; verify exact current Oracle text before any recommendation. |

## 4. First cut hypotheses to scrutinize — not approved cuts

- **Glint-Horn Buccaneer:** assess whether its discard-to-damage engine has sufficient support beyond its own activated ability and whether it contributes more than another evasive Pirate or board-wide connection tool.
- **Captain Vargus Wrath / Dire Fleet Captain:** assess overlap with the existing anthem package, but do not cut a combat payoff merely because it is redundant; pumps directly support the commander's threshold and combat plan.
- **Daring Saboteur:** assess its individual activation cost and single-body draw rate against repeatable/multi-creature connection options. It is itself a low-cost Pirate and therefore has a meaningful baseline advantage.
- **Any proposed cut from removal, protection, Treasure/ramp, or theft package:** must be justified against the function it provides; do not trim interaction solely to add more Pirates.

No candidate has been approved, and no cut/add pair is selected yet. A recommendation must compare the specific slot contribution, current Oracle text, legality/color identity, and realistic effect on repeatable theft triggers.

## 5. Evidence and research notes

- Current project ranking snapshot: `commander_candidate_rankings_top100_per_commander_current_2026-10-12.csv`, Admiral Beckett Brass rows.
- Current commander strategy profile is Oracle-seeded and still marked optional manual refinement; this blueprint is the manual commander-first refinement.
- EDHREC's current Admiral Beckett Brass page emphasizes Pirate, Treasure, theft, and aggro themes; its higher-inclusion examples include Malcolm, Hostage Taker, Coercive Recruiter, Corsair Captain, Fathom Fleet Captain, and Port Razer. This list already contains those core pieces, so popularity alone does not justify changes.
- EDHREC commander page: https://edhrec.com/commanders/admiral-beckett-brass
- EDHREC optimized Pirate page: https://edhrec.com/commanders/admiral-beckett-brass/optimized/pirates
- Background strategy article on Pirate aggro, evasion, Treasure, and the difficulty of connecting with three Pirates: https://edhrec.com/articles/the-knowledge-pool-admiral-beckett-brass

## 6. Next decision step

Perform slot-by-slot review of the shortlist and weakest plausible cuts. Verify exact Oracle text and current Commander legality for each candidate, identify whether it materially improves the commander-specific plan, then present only evidence-backed add/cut pairs for user approval. Keep the frozen baseline unchanged until approval.
