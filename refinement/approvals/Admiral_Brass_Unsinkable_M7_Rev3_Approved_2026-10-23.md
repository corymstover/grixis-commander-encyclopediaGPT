# Admiral Brass, Unsinkable — explicit M7 Rev3 approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Cycle: `global-restart-2026-10-13`  
Owner: **Cory Stover**  
Decision: **APPROVED / LOCKED**, exact single-deck M7 Rev3 candidate only.

## Exact owner authorization

> I explicitly approve and authorize canonical locking of Admiral Brass, Unsinkable M7 Rev3, exact 100-card raw SHA-256 dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7. Proceed with the canonical approval PR, verification, merge and locking, then move to Deck #4 Anhelo.

This is explicit authorization for the exact dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7 UTF-8 bytes, and no other candidate. No blanket M6.10, M7 or M8 milestone approval is inferred.

- Approved source: `refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt`; raw SHA-256: `dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7`.
- Approved engineering research source: `corymstover/GrokBotMTGCompanion:data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable_ChatGPT_Rev3.txt` on PR [#651](https://github.com/corymstover/GrokBotMTGCompanion/pull/651), head `eb40e8e965c79762d9881b1a26dfd1289c49a5eb`.
- Independent whole-deck review: `data/grixis/m7/decision_reviews/Admiral_Brass__Unsinkable_ChatGPT_Rev3_independent_review.md` in the same engineering PR.
- Prior 2026-10-13 approved-source TXT remains unchanged at `refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt`.

## Approved eight net one-for-one improvements

| Add | Cut |
| --- | --- |
| Kitesail Larcenist | Enterprising Scallywag |
| Timestream Navigator | Francisco, Fowl Marauder |
| Warkite Marauder | Fathom Fleet Captain |
| Jhoira, Weatherlight Corsair | Pitiless Plunderer |
| Siren's Ruse | Crumbling Necropolis |
| Ripples of Undeath | Forerunner of the Coalition |
| Thassa, Deep-Dwelling | Wonder |
| City of Brass | Path of Ancestry |

`Brass's Tunnel-Grinder` in the Oct13 list is represented as `Brass's Tunnel-Grinder // Tecutlan, the Searing Rift` in M7 Rev3. This is only a card-name/display-face normalization of the **same physical card**, not an additional add/cut.

**Faithless Looting remains in the deck**, with its `{2}{R}` flashback cost and deliberate discard utility. `Ripples of Undeath` is added separately. `Thassa, Deep-Dwelling` makes blink/reanimation ETB value available while respecting end-step timing and finality-counter new-object rules. `Conjurer's Closet` was assessed and excluded on comparative opportunity cost, not overlooked.

## Verification scope and provenance exception

- Exactly 100 physical cards; 97 distinct names and list rows; three basic land names appear twice each; only one commander, first line.
- Thirty-three lands by front face; eight mana rocks; 28 Pirate creatures by historical source review including commander and Changeling Outcast.
- Official Commander-legal names, Grixis U/B/R color identity, no project-specific ban exception.
- Independent focused 25-test Rev3 verification and four green exact-head GitHub Actions in engineering PR #651; see separate source-bound evidence receipt.
- Power Bracket **4 — Optimized**. Archidekt tags: **Pirates / Reanimator / Aggro**.

**Important historical mismatch retained without alteration:** Oct13 canonical registry stored digest `e66e3a59719401f41830e9938997a87a45a1b0dcaa0663b0ec7b44e10077dd39`, but the actual Oct13 approved-source TXT raw SHA-256 is `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc`. Both are preserved as independently named values in the new state; neither value is misrepresented as equal to the other. The old proposed-final TXT is not substituted as the approved baseline.

No other deck is reapproved or unlocked by this transaction; next independent M7 target is #4 Anhelo, the Painter.
