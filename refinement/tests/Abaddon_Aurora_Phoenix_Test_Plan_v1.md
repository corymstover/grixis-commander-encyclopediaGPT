# Abaddon the Despoiler — Aurora Phoenix vs Mind's Desire Test Plan v1

**Status:** PLAN REGISTERED; PERFORMANCE COMPARISON NOT RUN (Forge runtime smoke tests completed; candidate-specific behavior still unverified)  
**Registered:** 2026-10-13  
**Deck:** Abaddon the Despoiler  
**Frozen baseline TXT SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`  
**Baseline normalized card-list SHA-256:** `4af2214a2d4055f4a1a5e91dcbe50a1193e3ee27070a0d9cb1208a17d994eb53`  
**Test variant file:** [Abaddon_Aurora_Phoenix_Test_Variant_v1.txt](../variants/Abaddon_Aurora_Phoenix_Test_Variant_v1.txt)  
**Variant raw file SHA-256:** `1ad0c11d1f6a28a54f89c378428af491c6ff9929f42813692c375fb60771503b`  
**Variant normalized card-list SHA-256:** `fbc57b9eb9fcf14bd28dc3f59a73486eb78c6dc097b0102cde5178e7d5c8b862`

## Controlled difference

This is a separate test artifact, not a change to the frozen or approved list.

- IN: 1x Aurora Phoenix
- OUT: 1x Mind's Desire
- Total: 100 cards including Abaddon; singleton check passes (basic-land copies preserved); one card substituted.
- Both options have mana value six, but the color requirement changes from {4}{U}{U} to {4}{R}{R}.
- Abaddon is a five-mana commander ({2}{U}{B}{R}), mana value 5. The prior blueprint's description of him as six mana has been corrected.

## Falsifiable hypothesis

Aurora Phoenix will provide a higher floor for the cascade plan because it always has printed cascade and can return from the graveyard after subsequent cascade spells. If cast from hand when opponents have lost at least six total life this turn, Abaddon grants Aurora a second cascade instance.

Mind's Desire has the higher potential burst on spell-dense turns: its storm ability remains, and if cast from hand at the same six-life threshold it also receives one Abaddon-granted cascade. The test must measure the value of Mind's Desire's storm output as well as Aurora's cascade output and recursion. The theory of synergy alone does not decide the slot.

## Test-engine qualification gate

Do not run or report simulated results until the selected tool's support for the actual 100 card identities, their relevant current Oracle text, Commander turn/mulligan procedures, cascade, storm, escape, and graveyard/hand/exile zones has been checked. If the engine omits or approximates a relevant effect, label the result unsupported and do not use it to approve the swap.

No Forge executable or other validated MTG rules engine was found installed in the current execution environment during this review. Therefore no gameplay simulation or goldfish test has been run. A hand-written random-draw model is not an adequate substitute for the game's casting, triggers, mana, escape, and zone rules.

## Proposed benchmark

### Phase A — rules/engine support check

Confirm that all cards and relevant card text are implemented, that the selected engine can run the deck's target mode, and that the result export preserves turn/order and card-zone events. Record tool version and limitations. Abort the automated test if this gate fails.

### Phase B — pilot

Run 25 paired baseline/variant goldfish games using the same starting-library order per pair where the tool permits reproducible seeds. Keep the mulligan rule fixed. Use the pilot only to verify instrumentation and estimate variability; do not choose a winner from the pilot.

### Phase C — confirmatory comparison

Before inspecting confirmatory results, lock the sample size and success threshold informed by Phase B. If the engine passes the support check, use at least 200 paired starts as an initial confirmatory sample, with matched starting orders and the same mulligan/seat assumptions. Do not increase sample size opportunistically after seeing an unfavorable or favorable result.

Record for each run:
- Turn Abaddon is first cast and turn it first enables a qualifying hand-cast spell.
- Total opponents' life lost before each qualifying spell; cascade instances actually triggered and resolved.
- Nonland spells actually cast via cascade by turn 6 and turn 8.
- Whether Aurora returns from the graveyard, when and how often (variant); number of Mind's Desire copies and nonland spells actually played from its effect (baseline).
- Turn-6/turn-8 castability of the six-mana slot, including red/blue pip access and whether the card is functionally stranded.
- Access to the existing Underworld Breach + Lion's Eye Diamond + Brain Freeze route by turns 6 and 8, including actual prerequisites/fuel.
- Dead/low-impact high-end cards and turns without a meaningful play.
- Failures, misplays, unsupported rules, and missing log data.

### Interpretation and decision rule

Goldfish results can compare consistency and engine value, but they do not establish multiplayer win rate or resilience to interaction. If using an AI simulator, treat results as conditional on that AI's behavior and do not claim they model real opponents without calibration.

Prefer Aurora only if it shows a repeatable improvement in cascade/value output without a material regression in functional castability or access to the established combo route. The confirmatory decision should use paired differences and uncertainty intervals, not just averages. If results are within noise, disagree across metrics, or depend on unsupported rules, close the slot as inconclusive and keep the frozen baseline; do not turn the candidate variant into a final decklist.

The protocol's final gate still requires review of the full deck's nontrivial rules interactions, an appropriate performance check, a closed candidate ledger, an independently verified final 100-card list, and explicit user approval.



## Separate list-integrity verification

The isolated variant and frozen baseline were rechecked on 2026-10-13. The baseline archive/hash, both raw decklist hashes, both normalized membership hashes, exactly 100 cards per list, singleton compliance, and the single substitution (Mind's Desire out / Aurora Phoenix in) all passed. See [Abaddon_Variant_Integrity_Check_2026-10-13.json](Abaddon_Variant_Integrity_Check_2026-10-13.json). This does **not** mean a gameplay test has run; the gameplay test remains NOT RUN.


## Forge engine qualification update

A targeted source-code review found scripts for Abaddon, Aurora Phoenix, Mind's Desire, Underworld Breach, Brain Freeze, Lion's Eye Diamond, and Wild-Magic Sorcerer, but this is not a complete 94-card support audit or live engine test. Forge's own documentation warns its AI is poor at most combo decks. The engine therefore remains **NOT QUALIFIED** for the registered test; no games have been run. See [Abaddon Forge Engine Qualification](Abaddon_Forge_Engine_Qualification_2026-10-13.md).


## 8. Current engine gate update — 2026-10-13

A candidate Forge release is now pinned: `forge-2.0.15` resolving to commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`. Six high-priority scripts (Abaddon, Aurora Phoenix, Mind's Desire, Underworld Breach, Brain Freeze, Lion's Eye Diamond) were read at that commit. This remains a source sample only.

The 94-name release-specific script coverage audit was attempted using remote calls but could not be completed within the connector's tool-call budget. The engine has not been installed, the variant has not been loaded into Forge, runtime smoke tests have not been run, and the required paired-start/event-log controls have not been demonstrated. Thus the test plan is still **REGISTERED — NOT RUN**, and the engine gate is **NOT PASSED**.

Forge CLI docs support Commander-format AI self-play, but the documented AI explicitly has poor performance in most combo decks. CLI repeat count does not by itself establish matched library order, deterministic seeds, or adequate structured per-event output. Even if a runtime smoke test passes, these separate protocol requirements must be tested before labeling Forge results a confirmatory paired comparison. If a suitable execution environment or reproducibility controls are unavailable, record the performance comparison as not feasible with this engine and make a decision from rules/strategic evidence only, without claiming statistical playtest support.

See the [consolidated Forge qualification report](Abaddon_Forge_Engine_Qualification_2026-10-13.md).

## Engine smoke-test update — 2026-10-13

The pinned Forge 2.0.15 workflow [run 38338464845](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338464845) passed the full card-script identity/Oracle-field scan for 95 names (the variant's 94 names plus baseline-only Mind's Desire), verified the frozen baseline hash, generated the baseline/variant Commander deck files, and launched one Commander-mode simulation.

This **does not change the registered test status**: the 10-second match clock stopped the game as a draw, output included contradictory winner lines and repeated Steam Vents activator warnings, and no paired/reproducible gameplay comparison was run. Do not record the variant as a win or use these logs to choose between Aurora Phoenix and Mind's Desire. Rules-event smoke tests and evidence of matched/random-seed controls remain open. The complete evidence is in [Abaddon Forge Smoke-Test Result](Abaddon_Forge_Smoke_Test_Result_2026-10-13.md).


## 10. Runtime smoke update — 2026-10-13

The earlier NOT RUN entries above document the state at initial plan registration and before the pinned executable was tested. Current status:

- Forge forge-2.0.15 starts in recognized CLI parse mode.
- The full 94-card variant identity set plus Mind's Desire as baseline-only candidate matched 95/95 pinned-source card scripts with nonempty Oracle fields.
- The frozen 100-card baseline and test-only 100-card variant were imported as Forge Commander DCK files. Their input order is aligned except that Aurora Phoenix occupies Mind's Desire's original slot.
- A complete head-to-head Commander smoke game ran with full logs. In that game, the log showed Abaddon-granted cascade resolutions on other spells and an Imperial Seal escaped with Underworld Breach. It did not cast Aurora Phoenix, did not demonstrate Aurora's graveyard-return ability, and did not execute the full Breach/LED/Brain Freeze route.
- The same seeded command ran twice. The exact match-event portions were identical after timestamp and duration normalization, as independently checked from the captured logs. The fixed workflow normalizer has been updated to compare only the match event section; see [the corrected repeatability workflow run](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338912312).
- This is an engine/import/replay smoke test only. It does not count as the registered 25-pair pilot and does not determine whether Aurora Phoenix is better than Mind's Desire. Forge's own AI limitations remain relevant.

### Phase A status

| Check | Status |
|---|---|
| Pinned release and archive checksum | PASS |
| 94 variant identities + baseline comparison card found in pinned scripts | PASS (95/95 name/script/Oracle-field matches) |
| Exact 100-card DCK import into Commander-mode game | PASS |
| Seed flag accepted and repeat event log observed | PASS in captured smoke logs; corrected workflow confirmation pending |
| Aurora Phoenix's printed cascade and graveyard recursion exercised | NOT TESTED |
| Abaddon threshold edge cases and double-cascade Aurora scenario | NOT TESTED |
| Storm copies vs cast-trigger distinctions | NOT TESTED |
| Full Breach + LED + Brain Freeze line | NOT TESTED |
| Suitable comparative metrics and interpretation controls | NOT QUALIFIED yet |
| 25 paired pilot games | NOT RUN |
| 200-pair confirmatory benchmark | NOT RUN |

Do not choose the card slot from the smoke result. Continue with a targeted Aurora interaction test and decide whether Forge's observable logs can support the pre-registered metrics. If not, close the performance comparison as infeasible with this engine and make the slot decision only from the documented Oracle/rules/strategy evidence, explicitly recording that limitation.
