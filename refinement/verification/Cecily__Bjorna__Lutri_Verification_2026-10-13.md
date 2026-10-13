# Bjorna, Nightfall Alchemist // Cecily, Haunted Mage + Lutri — New-Cycle Refinement & Verification Certificate

**Deck:** #8 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline source:** immutable October 12 source package plus `GrixisFINAL60--2026.zip` / `GrixisFINALTXT60--2026.zip`  
**Baseline raw CSV SHA-256:** `6741400f0a68a0a790db89c395554e3440d25e43c32f30002749e5659e950534`  
**Baseline raw TXT SHA-256:** `4e10f9fcc2e8ec230cf7627d9f32eb4693b45c1af7a5a104d14f878e39f99a2f`  
**Normalized baseline-list SHA-256:** `e882e3729b6d0baf4d06e280ff4cb877653e0b8cc7afcfee493f68f91ba20743`  
**Revised exact-TXT SHA-256:** `5dd99905c7281a1fad8f0173e73413954f5fe390bfa64b1048d63ac38916cf46`

## 1. Structural integrity

- Frozen baseline files are extracted from the October 12 package and match the named FINAL archives; raw source hashes are recorded above.
- Baseline contains 100 main-deck copies plus Lutri as companion (101 total copies in the export); revised list likewise contains 100 main-deck copies plus the companion. The two commanders are counted within the 100-card main deck; Lutri is outside it.
- Revised output: 100 lines, 101 total copies including companion, 100 distinct card names across main deck and companion; main deck excluding Lutri is 100 copies / 99 distinct names.
- Commander markers: Bjorna and Cecily are marked `[Commander]`; Lutri is marked `[Companion]`.
- Singleton compliance: **PASS**. Only Island repeats (x2); no nonbasic duplicate.
- Land count: 33 main-deck land copies, unchanged.
- CSV/TXT reconciliation: **PASS**; the files represent the same card quantities.
- Actual delta: +Cryogen Relic, +Galazeth Prismari; −Ichor Wellspring, −Seething Song; no other main-deck membership changes.

## 2. Identity, Oracle and official legality

- Bjorna is blue-red and Cecily is blue-black-red; the command-zone pair’s combined identity is UBR. Lutri’s identity is blue-red. Both additions fit UBR; both cuts are identity-compatible.
- Active-cycle project-wide Scryfall refresh is documented as generated `2026-10-13T07:03:26.694525Z` from bulk data updated `2026-10-12T21:06:24.577Z`; the project report states 5,964/5,964 exact printing/name matches. This supports baseline metadata but is not a substitute for interaction verification.
- **Cryogen Relic** current card reference: https://scryfall.com/card/eoe/52/cryogen-relic. Oracle: when it enters or leaves the battlefield, draw a card; `{1}{U}, Sacrifice this artifact` puts a stun counter on a target tapped creature. Commander-legal; blue identity.
- **Galazeth Prismari** current card reference: https://scryfall.com/card/soc/311/galazeth-prismari. Oracle: flying; creates a Treasure on entry; artifacts you control have `{T}: Add one mana of any color. Spend this mana only to cast an instant or sorcery spell.` Commander-legal; blue-red identity.
- **Ichor Wellspring** current card reference: https://scryfall.com/card/fdc/265/ichor-wellspring. Draws on entry and when put into a graveyard from the battlefield.
- **Seething Song** current card reference: https://scryfall.com/card/c21/179/seething-song. Adds `{R}{R}{R}{R}{R}`.
- Official [Commander banned list](https://mtgcommander.net/index.php/banned-list/) checked 2026-10-13. **Lutri, the Spellchaser is banned as a companion; Trade Secrets and Yawgmoth’s Bargain are banned cards.** The project registry explicitly authorizes all three for this designated deck. They remain project exceptions and are not described as officially legal. No unregistered exception is introduced.

## 3. Rules and interaction verification

- **Bjorna + Cryogen Relic:** activate Bjorna’s `{T}, Sacrifice an artifact` ability and sacrifice Cryogen Relic to pay the cost. Bjorna’s ability goes on the stack; Relic’s leave-the-battlefield draw trigger also triggers and resolves above it. You draw a card, then Bjorna’s ability can deal 1 damage and goad the target creature. The Relic’s own `{1}{U}` stun ability is not being activated in this line; the artifact is sacrificed as Bjorna’s cost.
- **Galazeth Prismari:** the Treasure enters and can be tapped for instant/sorcery-only mana or sacrificed to Bjorna while untapped. Galazeth’s granted tap-for-mana ability is a mana ability and does not use the stack; it does not interfere with Bjorna’s activated ability. Once tapped for mana, the Treasure remains on the battlefield and may later be sacrificed if untapped status is irrelevant to the sacrifice cost.
- No deterministic infinite combo is added or claimed.

## 4. Commander-first strategic assessment

The deck remains a high-hand-size instant/sorcery value engine backed by an artifact-sacrifice control package. Cryogen Relic improves Bjorna’s sacrifice conversion without giving up the cantrip role. Galazeth changes a one-shot ritual into sustained mana from artifacts, while the Treasure remains relevant to Bjorna. This is a modest optimization, not a forced archetype change. The main trade-off is slower ramp in exchange for ongoing artifact mana.

## 5. Candidate and performance gates

- 16 candidates reviewed: two additions implemented, two existing candidates retained, twelve rejected with reasons.
- Ranking and EDHREC metrics are discovery/association signals from the October 12 project snapshot, not proof of card strength.
- No qualified matched-start multiplayer simulator or representative game sample was available for before/after comparison. No win-rate or empirical superiority claim is made.

## 6. Verification gates

| Gate | Outcome | Evidence / limits |
|---|---|---|
| 100-card main deck and singleton | PASS | 100 main-deck copies, including both commanders; Lutri companion tracked separately; Island x2 is the only repeated name. |
| CSV/TXT reconciliation | PASS | Both final files have identical quantities and final TXT hash recorded above. |
| Commander identity | PASS | UBR pair identity; additions/cuts fit UBR. |
| Oracle/rules interactions | PASS | Current references for both additions and cuts; Bjorna sacrifice trigger and Galazeth mana ability checked. |
| Official legality | PASS WITH DOCUMENTED EXCEPTIONS | Lutri companion, Trade Secrets, and Yawgmoth’s Bargain remain explicit project exceptions; official bans accurately disclosed. |
| Commander-first strategic fit | PASS | Artifact-sacrifice utility and sustained artifact mana support both commanders. |
| Candidate decision ledger | PASS | 16 decisions with two additions, two retained, twelve rejected. |
| Empirical performance test | NOT AVAILABLE | No qualified matched-start simulator/sample; no performance claim. |
| Final technical gate | PASS | All required checks complete; exceptions documented separately. |

**Final status:** APPROVED / LOCKED — ALL TECHNICAL GATES PASSED.