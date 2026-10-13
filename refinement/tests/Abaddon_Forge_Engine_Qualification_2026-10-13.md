# Abaddon Forge Qualification — Current Evidence and Decision

**Snapshot date:** 2026-10-13  
**Candidate version pin:** Forge `forge-2.0.15`, resolved commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`  
**Current decision:** smoke checks for source presence and Commander-mode deck loading **PASS**; **NOT QUALIFIED** for rules-correctness testing or comparative gameplay.  
**Valid comparative gameplay runs:** 0 (one bounded CLI smoke match was stopped as a draw after a 10-second clock).  
**Approved card changes:** 0

> **Current-status note (2026-10-13):** Sections 1–9 below preserve the investigation chronology and include historical statuses that were accurate before the latest CI run. The authoritative current outcome is in [Section 10](#10-latest-qualified-scope-after-the-commander-mode-smoke-test) and the [smoke-test result record](Abaddon_Forge_Smoke_Test_Result_2026-10-13.md). Do not interpret the earlier pending-source-scan or no-deck-load statements as current.

## Current verified state

The exact Aurora Phoenix test variant has 100 cards including the commander, 94 distinct card names, and only one difference from the frozen baseline: Aurora Phoenix IN / Mind's Desire OUT. Its raw SHA-256 is `1ad0c11d1f6a28a54f89c378428af491c6ff9929f42813692c375fb60771503b`. The baseline TXT SHA-256 is `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.

Forge release `forge-2.0.15` was published on 2026-09-28. Its tag resolves to commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`. The annotated tag is unsigned/unverified per GitHub metadata. Release: https://github.com/Card-Forge/forge/releases/tag/forge-2.0.15. The official Forge wiki describes Forge as an independent Magic rules engine supporting up to eight players and over 99% of cards, but that general statement does not establish support for this exact list or correctness of each relevant interaction. https://github.com/Card-Forge/forge/wiki/

At that commit, source files were inspected for six key cards: Abaddon the Despoiler, Aurora Phoenix, Mind's Desire, Underworld Breach, Brain Freeze, and Lion's Eye Diamond. The script contents contain their expected names and Oracle text; this is source-level support evidence only. It is not a runtime test. Earlier source inspection found Wild-Magic Sorcerer on the moving main branch, but it has not yet been pinned/audited at this release commit.

## Qualification gates

| Gate | Evidence | Status |
|---|---|---|
| Release/version pin | Release and resolved commit recorded above | Identified |
| All 94 distinct card names matched to scripts at the pin | Only six critical cards checked at pinned commit; no complete lookup audit | **Not passed** |
| Executable installed and launched | Not done in this environment | **Not passed** |
| Exact variant loaded in Commander mode | Not done | **Not passed** |
| Abaddon-granted cascade and Aurora graveyard return observed in runtime | Script source only; no runtime events | **Not passed** |
| Trigger ordering, cascade cast-from-exile behavior, storm copies, escape and combo sequence smoke tests | No runtime test/log | **Not passed** |
| Stable seed/paired-start control and structured turn/zone event logs | Not demonstrated | **Not passed** |
| Gameplay results | None | **Not run** |

## Rules-derived expected events for later smoke tests

These are requirements for evaluating a test engine, not claims about Forge runtime behavior.

1. With Abaddon on the battlefield during its controller's turn, a spell cast from that player's hand qualifies for Abaddon's cascade grant only if its mana value is no greater than opponents' aggregate life lost that turn at the time the spell is cast.
2. If Aurora Phoenix is in its owner's graveyard immediately after a spell with cascade is cast, its graveyard ability triggers once for that cast event. Cascade can come from Abaddon or a card's printed ability. If Aurora Phoenix itself is cast from hand and meets Abaddon's life-loss threshold, its printed cascade and Abaddon's grant are separate instances.
3. Storm creates copies, not casts. Copies should not produce cast-trigger events. This distinction matters for Brain Freeze, Mind's Desire, and the deck's cast-from-exile payoffs.
4. Underworld Breach gives escape to nonland cards in the graveyard, but the LED/Brain Freeze route needs an appropriate setup and sufficient graveyard fuel. Abaddon's hand-cast cascade grant does not apply to escape spells cast from the graveyard.

The current manual interaction review remains the detailed card/rules source: https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md

## Recommended next action

In an environment that can download and execute the pinned Forge desktop/JAR build:

1. Audit all 94 card identities against scripts at commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`, handling double-faced/modal names and land-card canonical script names carefully.
2. Run the release in a reproducible environment and record Java version, artifact hash, command line, and Forge build identifier.
3. Load the exact baseline and variant under Commander mode without substitution or warnings.
4. Create minimum scenario decks/states to test the expected events above. Record raw logs and compare each event to a manually specified expectation.
5. Only after all correctness gates pass, assess whether stable paired initial library orders and structured event capture are possible. If not, the engine may be useful for exploratory testing but is not qualified for the registered paired confirmatory comparison.

A card-script directory scan or a large claimed coverage percentage is not enough to certify interactions. Do not infer game performance from script presence. Do not use simplified random-draw models as a substitute for rules-resolved game play.

## Project control

The frozen baseline remains authoritative and untouched. The Aurora Phoenix variant is a test-only artifact and remains unapproved. There is no reason to advance to another deck until Abaddon's rules review, testing-method decision, candidate ledger, independent final verification, and explicit approval gates are resolved.


## 6. Automated pinned-release source audit — 2026-10-13

The 94 distinct card names in the isolated variant were extracted from the version-controlled test list. Six core card scripts were independently fetched at the pinned Forge commit listed above; a batch attempt to fetch the entire set did **not** complete because the GitHub connector imposed a tool-call limit. Therefore full release-specific script coverage remains **unverified**. Do not describe the card inventory as passed or fully audited.

This is an execution constraint, not evidence that the cards are unsupported. The next effective step is to run a repository checkout and a local path/name scanner in an environment able to fetch or clone the pinned Forge source (or query the pinned Git tree) without one remote tool call per card. The scanner must handle split/modal card names and confirm each card is mapped to a nonempty script, then produce a machine-readable coverage report with missing/ambiguous entries for manual review.

The remote docs establish that Forge supports CLI AI games in Commander mode but specifically say AI is "pretty bad for most combo decks"; that supports only an exploratory-AI warning, not the proposed controlled paired-start comparison. The documented CLI examples show repeat counts but do not establish matched library orders, deterministic seeds, or a structured event-log API. Those controls remain unproven and are independent gates even if card support passes. [Official Forge AI/CLI documentation](https://github.com/Card-Forge/forge/blob/master/docs/AI.md)

**Current qualification conclusion:** release pinned and key source scripts inspected; 94-card coverage scan incomplete; executable/list import/runtime interactions not tested; controlled paired-run support not established; no gameplay results. Forge remains not qualified.

### Partial card-identity audit detail

A pinned script read was also confirmed for the six cards listed above; their declared script names and Oracle lines were present in the returned source. This does not establish coverage for the other 88 names. A second, bulk fetch attempt of 94 source paths was blocked by the connector's tool-call limit before a complete result could be collected. The report intentionally leaves the 94-card coverage gate as pending rather than presenting a partial scan as a pass.



## 7. Runtime probe result — Forge starts, but no game was run

GitHub Actions run [38333900815](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38333900815) completed successfully. Its log confirms:

- Java runtime: OpenJDK 17.0.20.1 (Temurin).
- The checksum-verified `forge-installer-2.0.15.tar.bz2` was extracted successfully.
- The desktop JAR `forge-gui-desktop-2.0.15-jar-with-dependencies.jar` was found and invoked.
- Forge printed `APP: Forge v.2.0.15-SNAPSHOT-09.28`, confirming the binary starts.
- Invoking the JAR with `--help` returned exit code 0 but printed `Unknown mode. Known modes are 'sim', 'parse', 'server'`. This is a successful JVM/application startup probe, **not** a successful help-command probe.

The run uploaded a short log artifact, `forge-2.0.15-runtime-probe` (artifact ID 11784126985; SHA-256 digest of the ZIP recorded by GitHub as `34550c1a1bb053957e1d09efad21465dac29139d29f1af8b003d588dd2be1c70`). The output artifact confirms startup only.

### Updated status

| Qualification gate | Status |
|---|---|
| Pinned archive SHA-256 and extraction | PASS |
| Forge JAR JVM startup | PASS |
| Valid command invocation/usable CLI arguments | Pending; `--help` is not a supported mode |
| Full 94-card script coverage scan | Not run |
| Exact deck import / Commander mode | Not run |
| Required interaction smoke tests | Not run |
| Fixed/paired starting orders and structured logs | Not demonstrated |
| Gameplay runs | 0 |

The runtime probe's workflow intentionally does not import the deck or play games. The engine remains **not qualified** for exploratory or confirmatory gameplay testing. The next probe must call a documented mode (`parse` or `sim`) with the correct syntax, establish how the release loads `.dck` input, and scan its extracted card script tree. Any subsequent gameplay should wait until the import and rules interactions are validated.


## 8. Follow-up: pinned Forge CLI startup (2026-10-13)

The revised workflow used Forge's documented `parse` mode without input instead of the unsupported `--help` argument. GitHub Actions run [38334035177](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38334035177) completed successfully, with the variant integrity verifier passing and the pinned release downloaded and extracted after its SHA-256 check. The JAR starts on OpenJDK 17.0.20.1 and reports `Forge v.2.0.15-SNAPSHOT-09.28`. The `parse` invocation returned exit code 0 without the earlier `Unknown mode` message.

This confirms the pinned desktop distribution can start and accept a recognized mode in a GitHub Actions runner. It does **not** yet demonstrate deck parsing because no deck input was provided, nor does it validate Commander setup or rules interactions.

- Runtime startup: **PASS**
- Correct CLI mode accepted: **PASS**
- Exact deck parsed/imported: **NOT TESTED**
- 94-card script audit: **NOT TESTED**
- Runtime rules smoke tests: **NOT TESTED**
- Paired starts / structured event logs: **NOT DEMONSTRATED**
- Gameplay tests: **0**

The next step is to use Forge's parse command with a minimal, known-valid input and inspect the documented expected output, then test the exact deck importer format. Do not submit actual baseline-vs-variant games until list loading and interaction smoke tests are validated. Forge is still **not qualified** for either exploratory gameplay or confirmatory paired testing.


## 9. Automated card-script presence scan — 2026-10-13

The new coverage scan ran in GitHub Actions [run 38334295959](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38334295959), at Forge release commit `4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676`. The workflow passed its release archive SHA-256 check, extraction, and JAR startup; the script scanner found the `res/cardsfolder` tree and read the deck variant as **94 distinct names**.

**Initial scan result: 0 matches / 94 missing / 0 ambiguous.** This does *not* mean all cards are unsupported. The scanner compared each deck name to the script `Name:` field using overly strict normalized full-name matching; Forge’s card scripts commonly use front-face canonical names and filenames, so double-faced cards and name conventions may differ. This result is a scanner false-negative risk, not evidence of actual missing support.

The scan did successfully exercise a key workflow capability: the release tree and all card-script text are available locally inside CI, so the coverage audit can now be corrected and rerun without 94 remote fetch calls. The raw JSON and startup logs are preserved in artifact `forge-2.0.15-runtime-probe`, ID `11783883372`, SHA-256 `0a289c0bb076a9c6cc7059c971e20f69a9d8f682f57917c3bf46e305bece805c`.

### Coverage-audit follow-up

1. Inspect the script text and naming pattern for a sample of ordinary names, split/modal cards, and the deck's double-faced Birgi // Harnfel card.
2. Adjust the scanner to compare both Forge `Name:` aliases and actual script file stems, using the front-face name as an explicit DFC candidate while preserving full original names in the report.
3. Add unit checks for known positive mappings (e.g. Abaddon, Aurora Phoenix, Mind's Desire, Underworld Breach, Brain Freeze, Lion's Eye Diamond) so a zero-match regression fails the audit instead of silently reporting 94 missing.
4. Rerun. Manually resolve every missing/ambiguous row. A script-presence match still does not demonstrate runtime rules correctness.

Current qualification remains **NOT QUALIFIED**. The deck has not been imported; no card-specific interaction smoke tests or gameplay have run; paired starts and structured event logs remain unproven.


## 10. Latest qualified scope after the Commander-mode smoke test

The latest workflow [run 38338464845](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338464845) supersedes the earlier statements in this report that the full card-script audit and exact deck-load test were still pending.

- The pinned card-script scan matched **95/95** names: 94 unique names in the isolated variant plus Mind's Desire as the baseline-only comparison card; zero missing/invalid rows; all required controls passed.
- The frozen baseline archive/hash was verified, and the exact baseline and isolated test variant were converted to Forge Commander `.dck` inputs. Both lists retained exactly 100 cards; only Mind's Desire was replaced with Aurora Phoenix.
- The Forge 2.0.15 CLI launched the Commander simulation using both deck files. That is a successful deck-load/runtime smoke test.
- The game was forcibly stopped as a draw under its 10-second per-game clock. The log also contained contradictory winner lines and repeated Steam Vents activator warnings. Therefore the output is **not a valid gameplay result**, and no comparison or card decision may be inferred from it.
- Deterministic/paired starting orders, structured event logging, and runtime validation of Abaddon's cascade grant, Aurora's graveyard trigger, storm/copy behavior, and the Breach line remain unproven.

See [Abaddon Forge Smoke-Test Result](Abaddon_Forge_Smoke_Test_Result_2026-10-13.md) for the full evidence and exact gate status. The overall decision remains **NOT QUALIFIED for comparative gameplay testing**; the Aurora Phoenix proposal remains separate from the baseline and unapproved. The registered baseline-versus-variant performance test remains **NOT RUN**.


## 10. Latest runtime and source-coverage evidence — 2026-10-13

This section supersedes earlier status statements that the source scan, CLI launch, and deck import had not been tested. Historical attempts above are retained as audit history.

### Passed gates

- **Pinned executable:** Forge forge-2.0.15; installer SHA-256 verified by the workflow, and the runtime reports Forge v.2.0.15-SNAPSHOT-09.28 on OpenJDK 17.0.20.1.
- **Exact source revision:** 4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676 was checked out and verified.
- **Card-script source coverage:** GitHub Actions [run 38338154797](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338154797) scanned 33,405 standard card-script files. The 94 unique names in the Aurora variant plus baseline-only Mind's Desire produced 95/95 unique-name matches to a nonempty Oracle field, with zero missing, ambiguous, or empty-Oracle matches. This checks card-script presence/name mapping only; it does not verify the implementation of each card's rules.
- **Baseline-preserving smoke fixture:** GitHub Actions [run 38338464845](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338464845) verified the archived baseline TXT SHA-256, both 100-card lists, and the exact one-card difference. A subsequent fixture update places Aurora Phoenix in Mind's Desire's original main-deck slot, keeping all other main-deck card positions aligned for seeded comparisons. Neither frozen nor approved deck membership changed.
- **Actual Commander-mode smoke game:** Forge loaded both DCK files and played a complete head-to-head game. In that smoke match, the log showed cascade resolutions on spells cast by the Abaddon deck after opponents had lost life that turn, and an Imperial Seal cast via Underworld Breach escape. This is useful runtime evidence for basic card-engine operation. It is not a controlled validation of the complete combo line or a performance result.
- **Forge RNG seed support:** In the pinned source, forge-gui-desktop/src/main/java/forge/view/SimulateMatch.java parses the -s seed option and calls MyRandom.setRandom(new Random(seed)). The source CLI therefore has an explicit RNG seed option. See [pinned Forge source](https://github.com/Card-Forge/forge/blob/4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676/forge-gui-desktop/src/main/java/forge/view/SimulateMatch.java).

### Still open

- **Aurora-specific interaction:** The smoke games did not cast Aurora Phoenix, so no runtime observation established its cascade/recursion behavior. The Aurora Phoenix vs Mind's Desire hypothesis remains untested.
- **Full combo:** The smoke games did not demonstrate the entire Underworld Breach + Lion's Eye Diamond + Brain Freeze route.
- **Paired-start equivalence:** The input card order is now aligned except for the exact Mind's Desire/Aurora Phoenix slot, and replaying the same command with seed 20261013 produced identical normalized match-event lines when the game section is compared from match header to result. This establishes observed log repeatability for one fixture, not independently observed identity of opening hands or library permutations. The original automation compared full process logs and counted variable engine-initialization/timing lines; the CI normalizer has been corrected to compare only normalized match-event sections. The corrected run is tracked in [run 38338912312](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38338912312).
- **AI validity:** Forge's own [AI documentation](https://github.com/Card-Forge/forge/blob/4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676/docs/AI.md) warns that its AI is poor at most combo decks. Therefore a Forge AI win rate is conditional on Forge's heuristic choices and must not be presented as real-world Commander win rate.
- **Confirmatory comparison:** Not run. No 25-game pilot or 200-pair confirmatory comparison has been counted as complete. No candidate swap is approved.

### Updated decision

Forge is now useful for **exploratory rules-resolved smoke tests and event-log inspection**, so there is no need to abandon it at the startup/import stage. It remains **unqualified for deciding the Aurora Phoenix slot** until the exact variant-specific behavior is observed and the event metrics needed by the registered plan are shown to be reliable. Any small pilot must use a fixed opponent set, fixed seat assignment and declared seeds, compare baseline and variant in separate but matched games, and preserve logs. A one-game variant-versus-baseline duel is never comparative evidence.

The frozen baseline stays authoritative and untouched. The Aurora Phoenix list stays a test-only artifact.
