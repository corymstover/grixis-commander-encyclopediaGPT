# Deck Quality Gates v3

**Status:** normative quality layer above Adaptive Pipeline v2.

This layer increases confidence that a finalized 100-card list is not merely legal and coherent, but the strongest defensible commander-first configuration found by the project's bounded research process. It does not claim mathematical global optimality.

## Gate sequence

SOURCE INTEGRITY → BASELINE INTEGRITY → COMMANDER BLUEPRINT → CANDIDATE DISCOVERY → CANDIDATE EXHAUSTION → RULES/ORACLE/LEGALITY → STRUCTURAL VERIFICATION → COMMANDER-IDENTITY REVIEW → STRATEGIC COHERENCE → HYPOTHESIS-DRIVEN TESTING → RED-TEAM REVIEW → COMMANDER NECESSITY → FINAL RECOUNT → EVIDENCE/UNCERTAINTY REVIEW → USER APPROVAL → LOCK.

Adaptive Pipeline v2 remains the execution substrate. The v3 quality layer adds epistemic gates; it does not weaken any v2 hard gate.

## Candidate exhaustion

Every high-impact candidate must be ACCEPT, REJECT, or HOLD with a reason. A high-impact HOLD prevents finalization. At least one bounded discovery pass must close with zero new material candidates. This is evidence of search closure, not proof that every possible Magic card was evaluated.

## Hypothesis-driven testing

Testing is required when a material decision cannot be resolved analytically. Tests must state the hypothesis before results are evaluated, compare controlled configurations, preserve legality/rules/identity integrity, record the result, and record the resulting decision. More simulations are not automatically better; tests exist to resolve named uncertainty.

## Red-team gate

Before finalization, review the proposed list adversarially. Material unresolved findings block finalization. Required review categories include, when applicable: sacred cows, generic staples displacing identity, candidate rejection quality, tutor density, redundancy/diminishing returns, interaction density, mana/curve, win-more slots, low-frequency synergies, combo slot cost, commander dependence, resilience, and metagame assumptions.

## Commander necessity

The review must explain the commander's material contribution and the counterfactual impact of removing it from the command zone. A deck whose plan remains essentially unchanged without its commander fails this gate until the blueprint/list is reconciled.

## Evidence and uncertainty

Material conclusions are labeled VERIFIED, HIGH_CONFIDENCE, PROVISIONAL, TEST_REQUIRED, or BLOCKED. BLOCKED and TEST_REQUIRED prevent finalization. PROVISIONAL is visible and must be justified; it does not masquerade as certainty.

Recommended dimensions: commander identity, engine, mana, interaction, resilience, conversion, combo integrity, card quality, candidate exhaustion, testing, rules confidence, and source freshness.

## Encyclopedia-wide diversity audit

Periodically audit card overlap, repeated win packages, tutors, interaction packages, combo packages, mana infrastructure, archetype distribution, unique mechanical packages, and commander dependence. Common infrastructure is not itself a defect. Diversity findings are review triggers, never automatic card bans.

## Cross-deck learning

Aggregate repeated ACCEPT/REJECT outcomes to identify research leads and ranking calibration opportunities. Knowledge may transfer between decks; card choices never transfer automatically. Every commander must independently satisfy its blueprint and identity gate.

## Approval boundary

Passing every machine and quality gate makes a deck **approval eligible** only. Automation cannot set APPROVED or LOCKED. Explicit user approval remains mandatory, followed by the final lock transition.

## Reopening

A locked deck is reopened only by explicit user request or the project's documented rules for a material source/rules/legality/correctness change. Historical artifacts remain evidence and do not silently override current-cycle state.


## Mandatory whole-deck optimization audit

Candidate exhaustion is not sufficient if the search begins from only historically proposed swaps. Before a deck can become approval eligible, **every card slot in the complete current 100-card list must be challenged against the commander blueprint**.

The audit is permanent project policy and applies to every deck in every future refinement cycle. Its purpose is maximum realistic optimization, not minimum necessary modification.

Required whole-list review:

1. Inventory all 99 noncommander cards and assign their actual functions/packages. Multifunction cards may occupy multiple roles, but no card may remain unexamined.
2. Reconstruct the deck from the commander outward: determine which cards would still be selected if the deck were being built today with no attachment to the existing list.
3. Identify the weakest cards and weakest packages across the entire list, including lands, mana, interaction, tutors, protection, engines, payoffs, finishers, combo pieces, recursion, utility cards, and generic staples.
4. Challenge sacred cows. Existing inclusion, historical approval, price, popularity, staple status, candidate rank, or prior lock is not evidence that a card is optimal.
5. Quantitatively inspect mana base, curve, ramp, draw/selection, interaction/protection, engine density, payoff/conversion density, recovery and closing power where the deck makes those quantities meaningful.
6. Search broadly enough to identify credible alternatives for the actual weakest slots, including current releases and commander-specific cards absent from inherited rankings.
7. Compare candidates against the best plausible cut anywhere in the deck when roles are fungible; do not artificially restrict a candidate to a historically chosen comparison slot.
8. Continue accepting material improvements until another complete pass produces no new material swap. A one-card or zero-card result is valid only after the other slots have survived this audit.
9. Record every retained card at least at the slot/package level as CORE, STRONG RETAIN, ROLE-CONSTRAINED RETAIN, or CUT CANDIDATE, with a defensible commander-specific reason.
10. Red-team the resulting full list again after all accepted swaps because multiple individually good changes can create package imbalance.

### Whole-list closure gate

A deck fails finalization if any of the following is true:
- any card or functional package was never reviewed;
- the review merely re-validates historical proposed swaps;
- plausible weak slots remain without candidate comparison;
- a current-release search was skipped when freshness could matter;
- mana/curve/interaction/engine structure was not assessed;
- a material candidate remains HOLD/unresolved;
- a final post-swap whole-list pass has not closed with zero new material improvements.

The evidence packet must explicitly state `whole_list_audit_passed: true`, the number of noncommander slots reviewed, package coverage, the weakest retained cards/packages, accepted swaps, rejected close alternatives, and the final zero-new-improvement pass.

### Campaign correction rule

If a methodology improvement reveals that a current-cycle approval was produced without this whole-list audit, that is a documented **correctness/process trigger** under the reopening policy. Reopen that deck, audit it under this gate, and relock only after the gate passes and the user approves the resulting exact list. This does not erase historical evidence; it prevents historical conclusions from substituting for the stronger audit.
