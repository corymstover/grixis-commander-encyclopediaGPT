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
