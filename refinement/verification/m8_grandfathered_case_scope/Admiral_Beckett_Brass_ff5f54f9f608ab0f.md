# Admiral Beckett Brass — exact-current M6 case-scope transfer for M8

Date: 2026-10-28. **Scope: bounded evidence for the owner-approved October 22 revision only.** This is neither a new owner approval nor a final M8 release certificate.

## Immutable inputs and executed proof

- Owner-approved physical 100: `refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt`, raw SHA-256 `ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000`.
- Approved/revised decision and independent limitations: `refinement/verification/Admiral_Beckett_Brass_M7_Approval_Verification_2026-10-22.md`. The previous October 13 approved deck remains intact.
- Engineering current-source material: `data/grixis/m7/decision_reviews/Admiral_Beckett_Brass_rev2.json` and `data/grixis/m7/decision_reviews/Admiral_Beckett_Brass_rev2_Original_Case_Transfer_20261028.md`, merged in engineering [PR #755](https://github.com/corymstover/GrokBotMTGCompanion/pull/755), tested PR head `981b18537737b9543c621cd275322129c0109f6b`, merge `6e3bd5ff36d053366150ad360497f8df29fe8cc1`.
- [GitHub Actions #40657037883](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40657037883): **SUCCESS**, executing `tests/test_m8_admiral_rev2_current_case_transfer.py` and original reference tests. The current adapter has 13 explicit groups, binds the exact raw SHA, checks source cards and invokes applicable original finite positive/adversarial tests. Its tested head is immutable. The broad M7 workflow on that head also succeeded (#40657037870).
- Historical original plan: `data/grixis/m6/test_blueprints/Admiral_Beckett_Brass.json`, five P0 and eight P1 groups. Its 25 previous test methods targeted an earlier 100; their historical pass must **not** be rebranded as exact-current testing. The Stage8 effect checks likewise precede the exact-current adapter.

## Original-case accounting on this exact 100

| Priority | Original case | Current bounded positive/adversarial coverage | Limits |
|---|---|---|---|
| P0 | C01 | Admiral's Oracle text, cost, commander and end-step theft window | No full stack engine |
| P0 | K01 | Three *distinct* Pirates deal combat damage to the *same* opponent; legal theft ownership | Noncombat damage, fewer sources and mismatched opponents rejected |
| P0 | K02 | Roaming Throne supplies another trigger *after* the true three-Pirate threshold | Throne never lowers threshold |
| P0 | K03 | Kari Zev is a Pirate; her Monkey is not | Monkey never supplies the third Pirate |
| P0 | F01 | Paid blockers, Fog and interaction challenge combat | No guaranteed connections |
| P1 | K04 | Changeling Outcast qualifies; damage prevention/blocks negate connection | No phantom hit |
| P1 | K05 | Retained Fiery Cannonade's instant non-Pirate damage and current Cosmotronic Wave's paid `3R` unblock effect | **Raise the Palisade is absent**. Its old bounce-specific test is historical-only, never a current pass. Wave does not bounce. |
| P1 | E01 | Two legal Throne theft triggers and separate targets | No fabricated infinite theft |
| P1 | E02 | Source-paid Lannery/Malcolm/Breeches/Ramirez draw, Treasure and exile trigger timing | Attack vs combat-damage and Fog distinguished |
| P1 | W01 | Four staged damage combats with surviving Changeling Outcast, Storm Fleet Sprinter, Spyglass Siren and Corsair Captain | **Dire Fleet Captain is absent** and no removed-card line is credited; Fog/removal still defeats a conditional win. Cloud Pirates is an additional flyer, not an identical pump replacement. |
| P1 | W02 | Port Razer extra combats require eligible player/damage/untap state | Not deterministic or unbounded |
| P1 | F02 | Paid Toxic Deluge and actual reanimation/finality/token recovery constraints | Does not promise recovery through all interaction |
| P1 | F03 | Admiral removal timing, source-paid recast and conditional Swat/Fierce/Stormtamer/Greaves | No automatic protection |

**Grandfathered-case finding:** all **5 P0** and **8 P1** original case *groups* have been accounted for at their surviving, exact-current physical card scope. The current adapter invokes reusable previously defined bounded mechanics with an exact-current roster precondition; it is **not** a new literal full-game replay or a fresh engine model of every opponent response. The Palisade-specific old branch and any removed Dire Fleet Captain-specific branch remain explicitly excluded from current pass counts. No original deferred P1 was resolved by this work: the M8 deferred-P1 register pertains to the 38 separate M7 transfer-receipt decks.

## Commander-first and release boundaries

The approved Admiral plan remains three real evasive Pirates dealing combat damage to one opponent to steal a nonland permanent at end step, with conditional Throne amplification, card flow, paid extra-combat effects and real blocker/Fog/commander-removal counterplay. The Rev2 whole-99 decision reviewed 28 substantive judgments, 16 incumbent-role challenges, seven fully specified 100-card candidates and rejected higher-swap packages when their losses exceeded their gains. No further card addition or cut is supported by the case audit.

This evidence **does not transfer or fabricate** an independent historical M6 J verdict, prove multiplayer win-rate supremacy, confer literal full rules-engine coverage, reopen Cory's approved list, or sign the 62-deck M8 release. The canonical fail-closed M8 gate must still require every other deck and every remaining deferred source-bound case.
