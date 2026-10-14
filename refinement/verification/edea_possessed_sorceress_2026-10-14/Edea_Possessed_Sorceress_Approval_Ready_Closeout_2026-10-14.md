# Edea, Possessed Sorceress — Approval-Ready Closeout

**Date:** 2026-10-14  
**Cycle:** `global-restart-2026-10-13`  
**Deck:** #16 — Edea, Possessed Sorceress  
**Status:** **APPROVAL_READY — NOT APPROVED / NOT LOCKED**  
**Approval candidate SHA-256:** `fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`

## Final proposed changes

1. `Garland, Royal Kidnapper` -> `Thassa, Deep-Dwelling`
2. `The Beast, Deathless Prince` -> `Mass Mutiny`
3. `Coercive Recruiter` -> `Captivating Crew`
4. `Morbid Opportunist` -> `Strionic Resonator`
5. `Dictate of Erebos` -> `Full Throttle`
6. `Reliquary Tower` -> `Arcane Lighthouse`
7. `Dragonskull Summit` -> `City of Brass`
8. `Drowned Catacomb` -> `Mana Confluence`
9. `Sulfur Falls` -> `Ancient Tomb`

## Commander-first result

The revised list is more tightly centered on Edea's actual Oracle text: temporary creature theft at beginning of combat, sacrifice conversion while the creature is still controlled but not owned, and multiplication/retention of that theft event.

- `Thassa, Deep-Dwelling` converts a one-turn Edea borrow into lasting control by blinking the borrowed creature at the end step and returning it under your control as a new object.
- `Mass Mutiny` and `Captivating Crew` increase the density of creatures controlled but not owned.
- `Strionic Resonator` directly copies Edea's theft or death/draw trigger.
- `Full Throttle` creates two additional combat phases, therefore two additional Edea beginning-of-combat theft triggers.
- `Arcane Lighthouse` solves the hexproof/shroud targeting failure mode of Edea and the deck's other targeted theft effects.
- `City of Brass`, `Mana Confluence`, and `Ancient Tomb` improve speed and five-mana-commander deployment without reducing the 35-land count.

The five nonland additions and five nonland cuts have the same combined mana value (21), so the nonland curve does not increase.

## Source discrepancy resolution

The matching authoritative CSV/TXT exports define the real baseline at 100 cards / 94 distinct names. The stale card-audit snapshot differs by five names and caused several real baseline cards to appear incorrectly in candidate rankings. The matching exports were preserved as authoritative, while all five audit-only cards were still independently challenged. `Thassa, Deep-Dwelling` and `Captivating Crew` earned final slots; `Cunning Rhetoric`, `Domineering Will`, and `Nasty End` did not.

## Candidate exhaustion / red team

The project top-100 candidates, stale-audit alternatives, current EDHREC evidence, and outside commander-specific challengers were tested against exact slots.

Important rejected challengers include `Marchesa, the Black Rose`, `Conjurer's Closet`, `Chameleon, Master of Disguise`, `Irenicus's Vile Duplication`, `Quantum Misalignment`, `Éomer, Marshal of Rohan`, `Breath of Fury`, `Sothera, the Supervoid`, `Helm of Possession`, extra sacrifice outlets, `Come Back Wrong`, `Jhoira, Weatherlight Corsair`, and generic Grixis staples.

`Marchesa, the Black Rose` was specifically rejected as an Oracle-term false positive: Edea's mandatory return trigger moves a borrowed dead card before Marchesa's delayed return can cleanly reclaim that same object for you.

The final adversarial second pass produced **ZERO NEW MATERIAL IMPROVEMENTS**.

## Rules closeout

The SHA-bound rules attestation passes the material interactions, including:

- Edea target legality and Arcane Lighthouse;
- multiple Edea death triggers still drawing after the first return moves the card;
- Thassa permanently retaining an Edea-borrowed creature as a new object;
- Roaming Throne naming Warlock;
- Strionic Resonator and Gogo copying Edea triggers;
- Spark Double and Sakashima Edea copies;
- Irma's no-retroactive-trigger timing and later-combat functionality;
- Full Throttle producing two additional Edea triggers;
- Karlach producing another Edea trigger;
- outgoing Garland's sacrifice lock being actively anti-synergistic;
- Chaos Shrine's Black Crystal and Nightmare Shepherd ordering with Edea;
- Saw in Half on borrowed creatures;
- Mass Mutiny deaths satisfying Edea; and
- Captivating Crew precombat sequencing.

## Complete fail-closed gate

The exact approval candidate passed against the fresh current-cycle Oracle cache generated 2026-10-14T09:32:52Z.

- Total cards: **100**
- Distinct names: **94**
- Repeated names: `Island`, `Mountain`, `Swamp` only
- Land count: **35**
- Commander color identity: **B/R/U**
- Singleton compliance: **PASS**
- Rules gate: **PASS**
- Official Commander legality gate: **PASS**
- Project exceptions: **none**
- Errors: **0**
- Overall result: **APPROVAL_READY**

## Power classification

**Bracket 4 — Optimized**  
Archidekt tags: **Theft / Sacrifice / Extra Combats**

No current-cycle state or tracker lock mutation is authorized until explicit user approval of SHA `fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`.
