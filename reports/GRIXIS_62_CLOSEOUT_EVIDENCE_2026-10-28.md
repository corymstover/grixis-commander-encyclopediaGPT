# Grixis Commander Encyclopedia — decision-grade closeout inventory

**Snapshot:** 2026-10-28. **Status:** OPEN, not an M6/M7/M8 milestone certificate.
**Scope:** 62 current, owner-approved/locked exact raw TXT artifacts in `state/current_deck_overrides.json`.

This is a finite gap inventory, not a request to repeat all reviews or generate another round of blind candidate rankings. Preserve all 62 approved SHA-bound lists. Any exact addition/cut goes back to Cory for approval before a source edit. None is authorized here.

## Source integrity and legality: completed, within stated limits

- All 62 exact registry SHA-256 values and approved raw files match; all have 100 playable cards, totaling **6,200** playable cards and **one separate Lutri companion**. The M8 **candidate** ZIP plus normalized Archidekt versions, manifest, exact-source comparison, and CI are in draft PR #119. This is not the M8 final acceptance.
- `scripts/verify_current_62_oracle_coverage.py` checks all exact approved contents against the canonical 2026-10-27 Scryfall bulk-derived Oracle cache, plus **three named-exact Scryfall lookups dated 2026-10-28** for `Genesis Chamber`, `Sengir Autocrat`, and `The Meathook Massacre` (latest Tresserhorn additions). Result: **zero unresolved card names, zero color-identity breaches**. Fail-closed tests cover missing coverage and unauthorized illegality. This does not simulate card interactions or assert that the rules data will never change.
- **Six nonlegal card/deck entries, all individually authorized and disclosed:** Bjorna/Cecily `Lutri, the Spellchaser` (companion), `Trade Secrets`, `Yawgmoth's Bargain`; The Madcap Jester `The Madcap Jester` and `Dragon's Smile` (future/unreleased); Tresserhorn's Lord, Returned (future/unreleased). No project exception changes official legality. The last two decks remain planning lists until release legality is established.
- The existing canonical integrity scripts, 62-list archival preview, M7 transfer validator, and their exact-head PR CI are separate checks; passing them does **not** close M6 I/J or prove multiplayer performance.

## Exact M6 case-transfer ledger: what is still unresolved

`refinement/verification/m7_certification_transfer/` contains **38** exact-list transfer receipts for the newer approval cohort, plus the frozen 2026-10-24 owner-approval snapshot. The other **24** approvals are preserved under the grandfather rule; they are *not* thereby newly certified under the later full M6 contract.

Within the 38 mapped receipts: **192 P0 passed, 193 P1 passed, 180 P1 deferred**. This is **385** evidenced passed cases out of **565** mapped cases. **16** of the 38 have no deferred P1; **22** have one or more. A deferred test is not a pass. The 180 deferred cases comprise **59 K** mechanic cases, **34 E** engine cases, **48 W** finish/win cases, and **39 F** failure/counterplay cases.

The source planning index `m6_required_cases_2026-10-24.json` describes **882 designed cases across 61 source identities**, not 882 executed tests. The Norman Osborn / Goben roster-source mismatch is explicitly called out there; do not infer the 62nd current deck is automatically covered. The engineering repository contains only **two formal M6 bundle files** as of this snapshot. Therefore we cannot honestly stamp **62/62 M6 I/J certified**.

### Owners of outstanding source-mapped P1 cases

| Exact approved deck | P1 deferred | Evidentiary next move |
| --- | ---: | --- |
| Saruman, the White Hand | 13 | Core mechanic, finisher, resilience fixtures |
| Goben, Gene-Splice Savant | 11 | Resolve Norman/Goben source mapping before exact-hash tests |
| Mairsil, the Pretender | 11 | Cage/activation, repeatability, counterplay fixtures |
| Marchesa, the Black Rose | 11 | Counters, death triggers, recursion; remap obsolete fixtures |
| Missy | 11 | Villainous choice, face-up/down, trigger fixtures; remap removed cards |
| Parnesse, the Subtle Brush | 11 | Copying/ward-like choices, payment and opponent agency |
| Rograkh/Silas Renn (RogSi) | 11 | Partner timing, compact wins, adverse play |
| Nekusar, the Mindrazer | 10 | Wheel/punisher, discard-vs-shuffle, self-damage, opposing locks |
| Nicol Bolas | 10 | Damage/discard and finisher fixtures |
| Nicol Bolas, the Ravager | 10 | Transformation, discard and win-line fixtures |
| Obeka, Splitter of Seconds | 10 | Upkeep multiplication and failure/counterplay |
| Sauron, Lord of the Rings | 10 | Ring/Orc engines and stack/turn sequencing |
| Sol'kanar the Swamp King | 9 | Damage/lifegain, control and attrition fixtures |
| The Rani | 9 | Goad/opponent-choice and resilient finishers |
| Mishra, Eminent One | 8 | Warform copies, leaves-battlefield, finishers; remap removed cards |
| Thraximundar | 8 | Forced sacrifice, timing, closing speed |
| The Madcap Jester | 5 | Future-card text and finish/failure cases; pre-release caveat |
| Kefka, Court Mage | 3 | Two obsolete Counsel-specific cases need disposition; Breach-loop W2 remains unverified |
| Marchesa, Dealer of Death | 3 | Discard-cost and stack/engine case mapping |
| Tetsuo, Imperial Champion | 3 | Equipment/spell and failure cases |
| Nathan Drake, Treasure Hunter | 2 | Opponent-dependent wins and multiplayer attrition cannot be guaranteed by static fixtures |
| Mishra, Artificer Prodigy | 1 | Failure/counterplay case |

Counts and precise individual rationales are in the existing hash-bound receipt JSON files. Some deferred cases reference cards **removed from the approved deck** and should be explicitly dispositioned as inapplicable with a revised-100 explanation; others need positive/adversarial executable tests; stochastic multiplayer/win-rate claims need clearly bounded manual evidence, not fictional simulation. Their `owner_visible_unresolved=true` values must stay visible until disposition.

## Strategic judgment, formal acceptance, and remaining release work

1. **Decision-relevant commander-first red-team pass.** Use the 62 original commander blueprints, M6 review packet, prior GrokBot and Josh-Lee-Kwai judgments, current approved changes, and existing source-bound tests. Investigate *actual unresolved* combo, mana/protection, weak-card, and commander-dependence questions. Overlap (for example, Kefka/Kess sharing many efficient Grixis cards) is a *review prompt*, not evidence of a necessary swap. Propose exact additions/cuts only with a concrete causal win for that commander's strategy and a stated tradeoff; Cory decides.
2. **Resolve the 22 P1-deferral sets by consequence.** First correct inapplicable old-card scenarios, then test real mechanical/rules disputes and material finishers/counterplay on the **exact current SHA**, then expressly disclose non-computable multiplayer limits. Do not blanket-re-run clean cases. Preserve positive and adversarial fixture/Oracle provenance.
3. **M6 I tested-pool / J reproducibility closeout.** Reconcile existing reviews and all 62 original-versus-current source identities, adjudicate untested case obligations, prove only the finite tested-pool no-further-improvement condition actually supported, and produce verifiable J receipts. Two pre-existing formal bundles are not 62. The Josh-Lee-Kwai **formal Pass C owner-equivalence** route is valid under Cory's 2026-10-20 policy but is expressly **not an independent third model**; no new third-model purchase is required to meet that waived qualification.
4. **Administrative M7 reconciliation.** Preserve all **62/62 individual owner deck approvals** while syncing stale milestone-level M6/M7/M8 registry/subtracker statuses only *after* their actual gates pass. Complete six missing bracket/tag metadata entries (Abaddon, Admiral Beckett Brass, Admiral Brass Unsinkable, Anhelo, Parnesse, The Rani) with factual/current project classifications, not guessed bracket endorsements. Stale open PRs must not overwrite exact locked heads.
5. **M8 acceptance.** Re-run all-62 exact-source archive, exception and manifest checks at the final head; attach all bounded evidence and unresolved limitations; request one explicit Cory release acceptance for **M8**. Only then label the final export certified and archive the authoritative artifact. Draft PR #119 is deliberately labeled `M8_CANDIDATE_NOT_CERTIFIED_OR_OWNER_ACCEPTED`.

### Decision now

**No card addition/cut is justified by this provenance audit alone.** No sealed list should be reopened to make progress on a paperwork counter. The open questions are measurable evidence/strategy questions above, not a license to keep tweaking decks forever. The goal is a truthful, finite final approval, not an impossible claim of globally provable optimality or 100% multiplayer win certainty.
