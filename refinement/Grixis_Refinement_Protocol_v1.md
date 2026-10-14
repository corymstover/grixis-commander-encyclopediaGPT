# Grixis Commander Encyclopedia — Controlled Refinement & Finalization Protocol

**Protocol version:** 1.0  
**Prepared against:** Current Source Package dated 2026-10-12  
**Scope:** One disciplined, evidence-led refinement cycle for the 62 current FINAL decks.

## 1. Objective and guarantee boundary

The target is not a metaphysically provable “perfect deck.” In multiplayer Magic, the result depends on hidden draws, pilot decisions, opponent choices, table composition, new cards, rules changes, and the chosen objective. No finite sample of games proves universal optimality.

The operational endpoint is stronger and testable:

> **FINAL AS OF SNAPSHOT DATE:** The deck passes every hard correctness gate; its commander-specific plan is documented; all plausible high-impact upgrades have been assessed; the best supported alternatives have been compared against their proposed cuts; testing shows no material regression; and no unreviewed candidate with credible evidence of a material improvement remains. Every rejected close alternative has a documented reason. Reopen only when a defined trigger occurs.

This endpoint is an evidence-backed stopping rule, not a claim that no better card could ever exist.

## 2. Protect the baseline before making changes

1. Treat the four `GrixisFINAL` CSV/TXT archives included in `Grixis_Commander_Encyclopedia_Current_Source_Package_2026-10-12.zip` as the current list-membership baseline.
2. Preserve the exact current FINAL lists as immutable baseline snapshots. Create a separate revision/candidate branch for the new refinement campaign; never silently overwrite the baseline.
3. The older `Grixis*Updated-10-11-2026` archives are historical pre-final lists, not current membership. The current source package reports 62/62 lists changed, with 306 card-copy additions and 306 card-copy removals relative to them.
4. Do not mistake the inherited v8.1.4 audit for a fresh audit of the current FINAL lists. The current package's structural reconciliation reports 62/62 deck pairs reconciled, correct 100-card main-deck-plus-commander counts, and singleton passes; however, it explicitly marks a fresh all-card Oracle/rulings/official-legality review as pending.
5. Preserve all recorded exceptions exactly as authorized. Record *official legality* and *project authorization* in separate fields.
6. Compute a normalized card-list hash for every baseline and every approved revision. A change to a card list, printing identity that matters to the record, or an exception must be attributable to a logged revision.

## 3. Freeze the research inputs that actually matter

For each deck, record a snapshot date and versions for: decklist source/hash; card identity and Oracle data; official Commander legality/banned-list checkpoint; commander-specific EDHREC data and retrieval date; combo/ruling references; and test protocol/random seeds. Cache data to avoid redundant searches, but re-fetch only when freshness matters or a source has changed.

### Source hierarchy

1. **Rules/card truth:** current official Commander rules and current official ban-list/announcement; Scryfall Oracle text, color identity, card identity, rulings, and printing data. If sources conflict or a name is ambiguous, mark `REVIEW` instead of guessing.
2. **Commander-specific adoption and association:** current EDHREC commander data, especially inclusion rate, Lift, sample size, and available filters. Treat these as observational signals, never as card-power proof.
3. **Rules-based combo evidence:** Commander Spellbook as a discovery index for known combos; independently confirm actual card text, prerequisites, steps, mana, and interaction points.
4. **Competitive evidence:** tournament/top-deck data for competitive commanders and relevant brackets where suitable. Do not generalize cEDH popularity to a casual/thematic deck without an explicit reason.
5. **Community lists:** targeted, well-matched public Archidekt/Moxfield lists when they answer a specific question not already answered by EDHREC or Oracle text. Do not collect lists merely to increase volume.
6. **Testing:** exact probability calculations for questions amenable to exact math; deterministic/reproducible Monte Carlo for consistency; controlled goldfish tests for sequencing; representative multiplayer games or calibrated simulations for interaction and win-rate hypotheses.

## 4. Required commander-specific blueprint

Before evaluating candidate cards, complete a short blueprint for the commander. A blank machine-seeded profile is not a finished blueprint.

Required fields:
- Primary plan and how the commander advances it.
- Secondary/supporting plan (only if it genuinely supports the primary plan).
- Main routes to victory and what enables each route.
- Key commander interactions and required card packages.
- Essential functions that must be covered: mana, draw/selection, interaction/protection, recovery, and closing power, adapted to the deck (not fixed quotas).
- Cards/packages that are core to identity and the explicit reason to cut them if ever proposed.
- Strategic constraints, failure modes, natural power ceiling, expected bracket, and known project exceptions.
- What the deck should *not* become; examples of attractive but off-plan additions to reject.

Keep the blueprint concise and concrete. It is the reference frame for every later choice and prevents a generic Grixis ranking from replacing commander-first judgment.

## 5. Candidate research: one funnel, not infinite browsing

### Stage A — Generate a manageable shortlist

Use current deck-specific candidate rankings (top 100 is a discovery pool, not 100 mandatory reviews). Filter to cards that are not already present in the current build, have valid color identity, satisfy official/project legality rules, and plausibly fill a named role or improve an existing package. Keep candidates that are new or absent from popularity datasets as `unknown`, not automatically `bad`.

### Stage B — Triage

Classify each candidate as:
- `A — High-impact`: plausible core-engine, consistency, protection, interaction, or win-condition improvement; evaluate fully.
- `B — Close alternative`: plausible slot-level improvement with a real trade-off; evaluate when time permits or evidence is close.
- `C — Low-impact/speculative`: weak role fit, redundant effect, high opportunity cost, narrow condition, or no credible upside; log a rejection reason and stop researching it unless new evidence appears.

Limit detailed evaluation to the strongest 3–8 candidates per functional slot/package, with more only if meaningful alternatives remain genuinely close. The point is not to cap quality; it is to stop expanding lists after marginal candidates cease to affect the decision.

### Stage C — Use a consistent card-fit rubric

For every card considered for a slot, score each dimension from 0–5 and provide a one-sentence evidence note:
- Commander-plan contribution.
- Functional contribution at the slot/package level.
- Synergy/complementarity with the existing 99 and commander access.
- Efficiency: mana, timing, color requirements, and opportunity cost.
- Resilience/versatility (including how it performs when the ideal line is disrupted).
- Evidence strength: rules text/known interactions, commander-specific data and sample size, competitive/field evidence, and testing.

Scores organize evidence; they are not scientific truth and should not be reported to decimal precision. A legality/color-identity/count failure is a hard veto, not a penalty that a high synergy score can offset. Compare a candidate against the *best plausible cut from the same slot/package*, not against a generic average card.

### Critical ranking-method caution

The inherited v8.1.4 methodology assigns 25% weight to an EDHREC legacy synergy field. EDHREC announced the transition from Synergy to Lift on commander pages on 2026-10-01. Retain historical scores as historical evidence only; do not treat that legacy field as a current, independently valid power statistic. For new research, capture current inclusion, current Lift, sample size, retrieval date, filter/context, and their limitations. Do not re-run the entire research pipeline just for routine deck updates; refresh only the sources/joins necessary for the current card candidates and current deck membership.

## 6. Mandatory full-100-card optimization pass

Before narrowing work to proposed swaps, audit the complete deck. Every noncommander card must be assessed against the commander blueprint and its package. Do not begin from the assumption that the existing list is mostly correct, and do not stop after validating a previously proposed change.

The optimizer must:
- classify every noncommander slot by role and retention strength;
- identify the weakest retained cards/packages across the whole deck;
- challenge generic staples and historically approved cards as aggressively as thematic cards;
- inspect lands, curve, ramp, draw/selection, interaction/protection, engine density, payoffs, recursion, finishers and combo slots;
- search current commander-specific alternatives for the actual weak points;
- make every material improvement supported by the evidence, whether that means zero changes or many;
- repeat the whole-list pass after changes until a complete pass finds zero new material improvements.

A zero-change or one-change result is valid only after all other slots have survived this process. Historical approval is not optimization evidence.

## 7. The atomic unit of optimization is a proposed swap

Do not ask, “What else can we improve in this deck?” Ask:

> “For this named role or package, is Candidate A a meaningful improvement over Cut B for this commander, and what evidence would change our mind?”

Every proposed swap must record:
- Candidate and proposed cut.
- Which function/package/plan is affected.
- Expected benefit and expected cost/trade-off.
- Rules text and color identity/legality check.
- Exact synergy or combo interaction, if claimed.
- Observational data and sample size, where available.
- A falsifiable prediction for testing.
- Decision: accept, reject, or unresolved; include a brief reason.

A swap is not accepted because the candidate ranks highly, is popular, appears in another project deck, has strong theoretical synergy, or performs well in one favorable goldfish. Likewise, do not cut a lower-popularity card that is essential to a distinctive plan merely to improve aggregate metrics.

## 8. Verification and testing tiers

### Tier 1 — Always required for the final 100

- Recount the actual current list independently; exactly 100 main-deck-plus-commander cards, with documented companion treatment.
- Singleton compliance, including basic lands and valid card-specific copy exceptions.
- Current card identity and Oracle text for all list cards, not just additions.
- Commander and card color identity.
- Official Commander legality checked against a current official checkpoint; separately validate every project exception and do not mislabel an exception as officially legal.
- Rules/interaction check for every combo, loop, copied ability, replacement effect, timing claim, or other nontrivial line actually relied upon.
- Commander blueprint fit, key package coverage, and natural power-ceiling rationale.
- Candidate decision ledger is closed for all high-impact opportunities.

### Tier 2 — Consistency tests

Use exact hypergeometric calculations when the question is simply the probability of drawing a number of lands/cards from a library. For more complicated draw/keep/castability questions, use a scripted Monte Carlo test with documented rules and a fixed seed. Goldfish benchmarks can include: keepable-hand rate under a defined mulligan rule, land drops by turn, colored-mana availability, commander cast turn, engine online turn, functional dead-hand rate, and turns without meaningful plays.

Compare variants using the same game assumptions and, where possible, paired random seeds so differences are less affected by luck. Report sample count and uncertainty, not just a point estimate. If a difference is within noise, do not claim one list is superior.

### Tier 3 — Interaction and win-condition tests

Goldfishing cannot establish resilience to removal, counterspells, graveyard hate, stax, board wipes, or rival combo clocks. For decisions where those factors matter, test a representative set of pod archetypes or use a simulator with a documented and validated interaction model. Treat automated AI results as evidence conditional on that AI's behavior; do not confuse many simulated games with a realistic model. Confirm high-impact conclusions with human gameplay when feasible.

### Minimal efficient test policy

- Run a baseline once for the initial candidate build.
- Test only changes that should materially change a named metric or strategic outcome.
- Batch related swaps into a variant only if their effects can be interpreted; otherwise test them singly or in a small factorial comparison.
- Use a pilot run to estimate variance, then a predeclared sample size and success threshold. Do not keep adding games until the result happens to look favorable.
- Keep the benchmark fixed across all variants of the same deck and record failures as well as wins.

## 9. Stop rule: when this deck is done

A deck may be marked `FINAL AS OF YYYY-MM-DD` only when *all* are true:

1. **Baseline locked:** source, list hash and card count are recorded.
2. **Hard gates pass:** 100 cards, singleton, identity, Oracle data, current legality, project exceptions, and relevant rules interactions are verified.
3. **Blueprint complete:** primary strategy, packages, win routes and natural ceiling are explicit.
4. **Slot review complete:** each major functional package has a defensible role allocation; no unexamined high-impact candidate remains in the shortlist.
5. **No material upgrade identified:** every proposed high-impact swap was accepted, rejected with a reason, or closed as inconclusive because the evidence did not justify a change.
6. **Performance check complete:** the resulting list meets predeclared consistency/strategy targets; there is no demonstrated material regression versus baseline; tests have known assumptions and limitations.
7. **Decision log complete:** additions/cuts, evidence, rejected close alternatives, remaining uncertainty, source dates and final list hash are preserved.
8. **User approved:** final list presented in the required one-card-per-line format and explicitly accepted.

If two choices remain close and neither has reliable evidence of superiority, choose based on commander identity, resilience, versatility, and stated project values, document the tie-break, and stop. Do not reopen the slot just because another plausible card can be found.

## 10. Freeze policy: changes after finalization

A finalized deck is not re-analyzed on every new candidate list or because another deck used a card. Reopen only for one of these triggers:
- official rules, Oracle text, errata, or Commander legality changes that materially affect the deck;
- a new card or relevant release offers a credible, commander-specific material improvement;
- repeatable real-game evidence reveals a structural failure or underperforming package;
- the previously approved list has an identified error;
- the user explicitly requests a re-open.

Otherwise maintain the finalized snapshot. A newer date by itself is not a reason to reopen.

## 11. Efficient campaign sequence

1. **Project-wide preflight once:** confirm the current baseline source, refresh official legality/Oracle data and mark the data date. Do not rebuild ranking research for no reason.
2. **Per deck:** blueprint → targeted candidate triage → slot-level swaps → rules audit → tests → finalization gate → user approval → hash and lock.
3. **Do not revisit finished decks during this campaign** unless a predeclared trigger appears. Move to the next commander only after the current review is formally closed.
4. **After all 62:** preserve the final lists, finalization records, test summaries, card-data snapshot, exception registry and aggregate audit. Thereafter, run only trigger-based maintenance.

## 12. Authoritative sources and tools

- Scryfall API/bulk-data policy: https://scryfall.com/docs/faqs/i-m-having-trouble-accessing-the-scryfall-api-or-im-blocked-17
- EDHREC FAQ: https://edhrec.com/faq
- EDHREC Lift methodology: https://edhrec.com/articles/from-synergy-to-lift-the-math-behind-edhrecs-new-era
- EDHREC Oct. 1, 2026 commander-page migration: https://edhrec.com/articles/changelog-replacing-synergy-with-lift-on-edhrecs-card-pages
- Commander Spellbook (combo discovery): https://commanderspellbook.com/about/
- FreeMully (probability/consistency goldfish): https://freemully.com/
- Forge command-line simulation and its published AI limitations: https://github.com/Card-Forge/forge/blob/master/docs/AI.md
- Official Commander/B&R sources should be rechecked at each final legality checkpoint: https://magic.wizards.com/en/banned-restricted-list

These tools inform the decision. None substitutes for source verification, rules analysis or the commander-first blueprint.


## 10. Uninterrupted audit-to-approval execution standard (effective 2026-10-13)

**User directive:** For each deck, continue all research, slot and candidate reviews, rules/Oracle checks, legality and identity checks, tests and red-team passes **without interim user-facing updates or repeated 'proceed' prompts**. Stop and report only when (a) the deck is genuinely **APPROVAL_READY** with a complete verified list and explicit approval request, or (b) a **material blocking dependency** prevents completing a mandatory hard gate. Do not claim approval readiness merely because a candidate list or intermediate worksheet exists. Do not auto-approve, lock, or advance to the next deck. An exception for an actual blocker is a factual explanation of the blocker, not a routine progress update.

**Required deliverable at approval gate:** 100-card copyable commander-first list; baseline and final hashes; full 99-slot audit disposition; candidate triage and high-impact swap decisions with rejected alternatives; current Oracle/card identity/color identity/Commander legality verification (exceptions separated); relevant combo/rules verification; strategic blueprint and ceiling; consistency/regression evidence with limitations; red-team and zero-unreviewed-material-improvement closure; concise proposed swaps and explicit user approval request. Preserve all previously approved decks.

**Repository hygiene:** Store draft audits in separate refinement files. Never label an artifact AUTO-APPROVED or LOCKED absent explicit user approval. Historical labels cannot override current-cycle approval state. Do not modify immutable source archives or previously locked decks. If blocked, persist reproducible evidence and a precise checklist of the unresolved gates.
