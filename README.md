# Grixis Commander Encyclopedia

Version-controlled project records for the 62-deck Grixis Commander Encyclopedia.

## Project operating rules

- Each deck is commander-first and preserves that commander's identity and natural power ceiling.
- **FULL RESTART REVIEW ACTIVE — 2026-10-13:** all prior-cycle approvals were reset to historical status. Decks #1 Abaddon the Despoiler and #2 Admiral Beckett Brass have now completed fresh full-list reviews and are approved/locked at their new hashes recorded in the active tracker. 60 decks remain unapproved/unlocked; next in authoritative tracker order is #3 Admiral Brass, Unsinkable. Earlier per-deck summaries below are historical records only; the active tracker defines current-cycle approval. Continue one deck at a time.

**Historical status note (restart cycle):** The detailed per-deck approval summaries in this README reflect previous-cycle work and are not current approvals unless the active tracker marks that deck `APPROVED / LOCKED — FRESH RESTART REVIEW PASSED`. The fresh restart currently has #1 Abaddon and #2 Admiral Beckett Brass approved; all other prior approval labels are historical only.


- The active cycle may revise any deck after whole-list review. Automatically approve and lock a deck only after all required technical verification gates pass; do not require an additional user approval step. A failed or incomplete gate means no lock.
- The four `GrixisFINAL` archives dated 2026-10-12 are the current authoritative membership baseline; the `Updated-10-11-2026` archives are historical.
- Candidate rankings are a research shortlist, not automatic card additions.
- Approval requires an independently verified 100-card main-deck-plus-commander list, singleton and copy-rule compliance, current identity/Oracle/rulings/legality review, documented project exceptions, relevant interaction verification, and a recorded verification certificate. Explicit user approval is not a gate in this new cycle.
- Official Commander legality and project-authorized exceptions must be recorded separately.
- Do not claim global mathematical perfection. Finalization is an evidence-backed stopping rule with documented uncertainty and material reopen triggers.

## Latest verified checkpoint — 2026-10-12

The source ZIP's internal manifest passed 165/165 hashes; all 62 current CSV/TXT pairs independently reconcile, all 62 main-deck-plus-commander lists count to 100, and all 62 singleton scans pass. The official Commander named-ban checkpoint is complete: the only explicit banned-list matches are the three known project-authorized Bjorna // Cecily + Lutri exceptions. The initial source report marked the full current Oracle/identity/exact-printing legality refresh as pending; a subsequent Scryfall metadata refresh has since completed and is summarized below. Detailed rules/interaction verification remains open. The hash manifest and detailed independent audit are preserved on the [frozen baseline branch](https://github.com/corymstover/grixis-commander-encyclopediaGPT/tree/baseline/freeze-2026-10-12).

## Current baseline and source consolidation

- [Source consolidation reconciliation — 2026-10-13](source-package/Source_Consolidation_Reconciliation_2026-10-13.md)
- [Deep-research continuation checkpoint — 2026-10-13](source-package/Deep_Research_Continuation_Checkpoint_2026-10-13.md)
- [Abaddon Forge qualification update — distribution checksum verified, runtime gates open](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/source-package/Abaddon_Forge_Qualification_Update_2026-10-13.md)
- [Duplicate source reconciliation — 2026-10-13](source-package/Duplicate_Source_Reconciliation_2026-10-13.md)
- [Exact current source-package text copies and source hashes](source-package/reference-copies/current-package-text-2026-10-12/README.md)
- [Current project status — 2026-10-13](source-package/Grixis_Project_Current_Status_2026-10-13.md)

The 124 current decklist CSV/TXT files are verified inside the compact archive. The full original source package has been integrity/hash-checked, but not every large raw source file is individually mirrored in GitHub. See the reconciliation report for the exact boundary.

## Controlled refinement campaign — RESET 2026-10-13

**Current state:** NEW CYCLE ACTIVE. The reset began with all 62 decks UNAPPROVED / UNLOCKED; **14 decks are APPROVED / LOCKED — ALL TECHNICAL GATES PASSED**: #1–10, plus #12 Davros, #13 Doctor Doom, #14 Don Andres, and #15 Dr. Eggman. 48 decks remain. Next is deck #11, Cult of Skaro. The four later decks remain locked; only administrative numbering was corrected. Previous-cycle lock/approval flags remain historical only; source baseline exports remain immutable. Each deck is auto-approved and locked only after all technical checks pass; do not add a user-approval gate.





The frozen baseline is preserved on `baseline/freeze-2026-10-12`. The active, separate work branch is `refinement/campaign-2026-10-12`; no baseline decklist has been changed. All previous approvals are reset for the active cycle.

- [Abaddon the Despoiler — commander-first blueprint v1](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/blueprints/Abaddon_the_Despoiler_v1.md)
- [Abaddon candidate decision ledger](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/decisions/Abaddon_the_Despoiler_Candidate_Decisions_2026-10-12.csv)
- [Abaddon expanded interaction review — cascade, exile, damage engines, and Breach line](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md)
- [Abaddon Aurora Phoenix test plan (registered, not run)](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Aurora_Phoenix_Test_Plan_v1.md)
- [Abaddon Forge engine qualification — pinned release; gates still open](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Forge_Engine_Qualification_2026-10-13.md)
- [Abaddon test-variant integrity check (passed; not a gameplay result)](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/tests/Abaddon_Variant_Integrity_Check_2026-10-13.json)
- [Abaddon Aurora Phoenix test variant (separate, not final)](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/variants/Abaddon_Aurora_Phoenix_Test_Variant_v1.txt)
- [Campaign tracker](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/Deck_Refinement_Tracker_2026-10-12.csv)

Abaddon is deck #1 in the new-cycle pass and is approved/locked after full technical gate closeout. It added Court of Ambition and Warstorm Surge, cut Loyal Subordinate and Rakdos, Lord of Riots, as recorded in the [change ledger](refinement/Deck_Change_Ledger_2026-10-13.csv). See its [final decklist](refinement/decklists/Abaddon_the_Despoiler_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Abaddon_the_Despoiler_Verification_2026-10-13.md), and [candidate decision summary](refinement/decisions/Abaddon_the_Despoiler_Candidate_Decisions_2026-10-13.md).

Admiral Beckett Brass is deck #2 and is now approved/locked. It added The Indomitable and Zephyr Singer and cut Bident of Thassa and Daring Saboteur. See its [final decklist](refinement/decklists/Admiral_Beckett_Brass_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Admiral_Beckett_Brass_Verification_2026-10-13.md), and [candidate decision summary](refinement/decisions/Admiral_Beckett_Brass_Candidate_Summary_2026-10-13.md).

Admiral Brass, Unsinkable is deck #3 and is now approved/locked. It added Power Conduit, Nesting Grounds, and Kitesail Larcenist; it cut Dire Fleet Daredevil, Crumbling Necropolis, and Amphin Mutineer. See its [final decklist](refinement/decklists/Admiral_Brass_Unsinkable_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Admiral_Brass_Unsinkable_Verification_2026-10-13.md), and [candidate decision summary](refinement/decisions/Admiral_Brass_Unsinkable_Candidate_Summary_2026-10-13.md). Actual card changes for decks #1–3 are preserved in the same [cumulative change ledger](refinement/Deck_Change_Ledger_2026-10-13.csv).

Anhelo, the Painter is deck #4 and is approved/locked at the exact revised-list hash `7fd898ffc4c3aad208cfd33361912bfefcff4754ec662b532ec5d0a5fcefbd4a`. It added Deekah, Fractal Theorist and Make an Example and cut Talrand, Sky Summoner and Talrand’s Invocation. See its [final decklist](refinement/decklists/Anhelo_the_Painter_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Anhelo_the_Painter_Verification_2026-10-13.md), [candidate decisions](refinement/decisions/Anhelo_the_Painter_Candidate_Decisions_2026-10-13.csv), and [candidate summary](refinement/decisions/Anhelo_the_Painter_Candidate_Summary_2026-10-13.md). All four earlier deck revisions’ actual additions and cuts are recorded in the cumulative [change ledger](refinement/Deck_Change_Ledger_2026-10-13.csv).

Ashad, the Lone Cyberman is deck #5 and is approved/locked at revised-list hash `a0142c7859626b5592d4ac6ef4711232f3fc765c7e02e1ae0963aecfe16a99e6`. It added Ultron, Artificial Malevolence and cut Dalek Drone. See its [final decklist](refinement/decklists/Ashad_the_Lone_Cyberman_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Ashad_the_Lone_Cyberman_Verification_2026-10-13.md), [candidate decisions](refinement/decisions/Ashad_the_Lone_Cyberman_Candidate_Decisions_2026-10-13.csv), and [candidate summary](refinement/decisions/Ashad_the_Lone_Cyberman_Candidate_Summary_2026-10-13.md). The cumulative [change ledger](refinement/Deck_Change_Ledger_2026-10-13.csv) now contains the actual changes for decks #1–5.

## Delegated automatic approval and locking

Effective 2026-10-13, the user delegated final deck approval and lock decisions to the assistant. Explicit user approval is no longer a finalization gate. The assistant may approve and lock a deck only after all mandatory technical gates pass and its final list, verification certificate, decision record, and hash are recorded and cross-checked. Any unresolved count, identity, Oracle text, color identity, legality, material rules interaction, or evidence gap blocks that deck; the status must remain unapproved/unlocked or blocked. Zero changes is a valid outcome when supported by the evidence. See the [Automated Approval and Lock Policy v1](refinement/AUTOMATED_APPROVAL_AND_LOCK_POLICY_v1.md).

This policy changes who makes the final decision, not the correctness bar. Historical source files and frozen baselines remain immutable; active refinement records are updated in tracker order. Current cycle state must be read from the dated status/tracker records rather than inferred from earlier approval history.

## Full-strength deck refinement standard

The user has directed that deck reviews must not be conservative about changes. Reassess the entire 99 plus commander, challenge inherited inclusions, research a broad commander-specific candidate pool, evaluate packages and plausible cuts, and make all changes the evidence supports—many, few, or none. No target swap count; no keeping a card just because it was in the baseline; no adding a card just because it's highly ranked or generically powerful. Reassess overall curve, engines, interaction, resilience, win conditions, and commander synergy after proposed changes. Follow the [Automated Approval and Lock Policy v1](refinement/AUTOMATED_APPROVAL_AND_LOCK_POLICY_v1.md), including every mandatory correctness gate before auto-approval.

## Strict one-deck-at-a-time workflow

Refine exactly one deck at a time in authoritative tracker order. Complete the current deck's full-list review, commander-specific research, decisions, rules and legality verification, final count/hash, verification certificate, decklist, and tracker update before beginning substantive review of the next deck. If a mandatory gate blocks the current deck, stay on it for bounded remediation; record a blocker rather than silently skipping it. Do not batch superficial reviews or optimize multiple decks in parallel. Shared data refreshes/reusable rules research are allowed, but they do not count as finishing a deck. The next deck may be selected only after the current deck's final disposition and artifacts have been re-fetched and cross-checked. Details: [Automated Approval and Lock Policy v1](refinement/AUTOMATED_APPROVAL_AND_LOCK_POLICY_v1.md).


## Full campaign restart — review again from deck #1

The active refinement cycle has been reset at the user's direction. Every prior approval is historical only; all 62 decks require a new full re-review under the full-strength, one-deck-at-a-time policy. Frozen baseline exports and historical artifacts remain preserved. Active campaign order restarts with Abaddon the Despoiler (#1); complete and document its new review before starting deck #2. Auto-approval/locking is permitted only after all current mandatory gates and final artifact/hash checks pass. Current progress is defined by the active refinement tracker, not prior-cycle statuses.

## Automated integrity check

Every relevant push and pull request runs [the baseline verifier](scripts/verify_baseline.py) through [GitHub Actions](.github/workflows/verify-baseline.yml). The verifier checks the 124-file archive against all 124 raw file hashes, CSV/TXT card-name quantities, 100-card counts, singleton/copy limits, and collection totals. The initial CI run passed: [view run](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38324768882).

## Current Scryfall metadata refresh — completed

The controlled refresh used Scryfall's `default_cards` bulk snapshot updated at `2026-10-12T21:06:24.577Z`. All **5,964/5,964 current decklist rows** matched an exact set + collector number + card name; there were no unmatched or ambiguous printings, no Oracle IDs missing, and no commander color-identity mismatches. All 62 decks' commander identities resolved. The six rows whose current official Commander legality is not ordinary `legal` status are fully registered project exceptions: Lutri as companion, Trade Secrets, Yawgmoth's Bargain, The Madcap Jester, Dragon's Smile, and Tresserhorn's Lord, Returned. Their official status remains visible; project authorization is not misrepresented as official legality.

- [Scryfall metadata audit summary](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/metadata_audit/Current_Scryfall_Metadata_Audit_Summary_2026-10-12.json)
- [Full exact-printing metadata overlay](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/refinement/campaign-2026-10-12/refinement/metadata_audit/Current_Scryfall_Metadata_Overlay_2026-10-12.csv)
- [Project exception registry](source-package/research/Project_Exceptions_Current_2026-10-12.csv)
- [Refresh workflow run](https://github.com/corymstover/grixis-commander-encyclopediaGPT/actions/runs/38325331651)

This closes the fresh Oracle/color-identity/exact-printing Commander-legality metadata gate. It does **not** close commander-specific rules/interaction verification, combo checks, strategic blueprints, candidate decisions, or testing.

## Start here

1. [Independent baseline audit](source-package/Grixis_Independent_Baseline_Audit_2026-10-12.json)
2. [Individual deck hash manifest](source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv)
3. [Official Commander legality checkpoint](refinement/Official_Commander_Legality_Checkpoint_2026-10-12.md)
4. [Source consolidation register](source-package/Source_Consolidation_Register_2026-10-12.md)
5. [Supplemental Starscape Cleric resolution](source-package/Supplemental_Starscape_Cleric_Resolution_2026-10-12.md)
6. [Source package import status](source-package/IMPORT_STATUS.md)
7. [Baseline & research freshness report](refinement/Baseline_And_Research_Freshness_Report_2026-10-12.md)
8. [Controlled refinement & finalization protocol](refinement/Grixis_Refinement_Protocol_v1.md)
9. [Refinement tracker](refinement/Deck_Refinement_Tracker_2026-10-12.csv)
10. [Candidate decision ledger template](refinement/Candidate_Decision_Ledger_TEMPLATE.csv)
11. [Playtest benchmark template](refinement/Playtest_Benchmark_TEMPLATE.csv)
12. [Deck finalization certificate template](refinement/Deck_Finalization_Certificate_TEMPLATE.md)

## Current baseline status

The supplied 2026-10-12 source report records 306 card-copy additions and 306 removals relative to the previous Updated archives. The independent structural audit confirms 62/62 CSV/TXT reconciliations, 62/62 exact 100-card counts, and 62/62 singleton passes. The official named Commander ban-list checkpoint and current exact-printing Scryfall metadata refresh are complete. Detailed card rulings, combo/interaction verification, and commander-first strategic refinement remain pending; do not treat metadata validation as a full strategy or rules-interaction certification.

## Current repository mirror

The current CSV/TXT decklists are mirrored in [the compressed 62-deck bundle](source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz) (62 CSV + 62 TXT files; 124 files total). Their exact per-file SHA-256 values are listed in [the individual deck hash manifest](source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv).

The four original canonical FINAL ZIP archives, four historical Updated archives, and full current audit/candidate-ranking datasets are still retained in the supplied source package outside GitHub. The new tar.gz is a verified mirror bundle, not a replacement for those original archives. See [IMPORT_STATUS.md](source-package/IMPORT_STATUS.md).

## Change control

Put new refinement records in separate paths; do not silently replace historical baselines. Every card change must have a reason and source/date, current legality and Oracle checks, a verified new list, and a recorded decision. Auto-approve/lock only after all technical gates pass; user approval is not required in this cycle. Reopen a finalized deck only for the triggers in the protocol or on explicit user request.


## Automated quality and metadata refresh

The repository uses a scheduled Scryfall bulk refresh plus fail-closed freshness and exact-list verification. See [Automation Operations Guide](refinement/Automation_Operations_Guide.md). Pull requests run the unit suite, workflow-contract checks, and frozen 62-deck hash/count/singleton verification. The large metadata download is serialized and runs weekly or on an explicit refresh request; it is not repeated for ordinary text-only edits.

Ashnod the Uncaring is deck #6 and is approved/locked at revised-list hash `35f55432f14f70bc3eb70412ea8cad7520363740e240531ff7122d2d8980dcc6`. It added Oni-Cult Anvil and Stormclaw Rager and cut Commander's Sphere and Dockside Chef. See its [final decklist](refinement/decklists/Ashnod_the_Uncaring_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Ashnod_the_Uncaring_Verification_2026-10-13.md), [candidate decisions](refinement/decisions/Ashnod_the_Uncaring_Candidate_Decisions_2026-10-13.csv), and [candidate summary](refinement/decisions/Ashnod_the_Uncaring_Candidate_Summary_2026-10-13.md). The cumulative [change ledger](refinement/Deck_Change_Ledger_2026-10-13.csv) now contains the actual changes for decks #1–6.

Be'lakor, the Dark Master is deck #7 and is approved/locked at revised-list hash `f48359f816498b386b085db60f0456576c8af9b055408685df71f0d1db448545`. It added Demonic Covenant and Ardyn, the Usurper and cut Reaper from the Abyss and Archfiend of Depravity. See its [final decklist](refinement/decklists/Be_lakor_the_Dark_Master_Refined_2026-10-13.txt), [verification certificate](refinement/verification/Be_lakor_the_Dark_Master_Verification_2026-10-13.md), [candidate decisions](refinement/decisions/Be_lakor_the_Dark_Master_Candidate_Decisions_2026-10-13.csv), and [candidate summary](refinement/decisions/Be_lakor_the_Dark_Master_Candidate_Summary_2026-10-13.md). The cumulative [change ledger](refinement/Deck_Change_Ledger_2026-10-13.csv) now contains the actual changes for decks #1–7.

Bjorna, Nightfall Alchemist // Cecily, Haunted Mage + Lutri is deck #8 and is approved/locked at revised-list hash `5dd99905c7281a1fad8f0173e73413954f5fe390bfa64b1048d63ac38916cf46`. It adds Cryogen Relic and Galazeth Prismari and cuts Ichor Wellspring and Seething Song. See [final TXT](refinement/decklists/Cecily__Bjorna__Lutri_Refined_2026-10-13.txt), [final CSV](refinement/decklists/Cecily__Bjorna__Lutri_Refined_2026-10-13.csv), [verification certificate](refinement/verification/Cecily__Bjorna__Lutri_Verification_2026-10-13.md), [candidate decisions](refinement/decisions/Cecily__Bjorna__Lutri_Candidate_Decisions_2026-10-13.csv), and [candidate summary](refinement/decisions/Cecily__Bjorna__Lutri_Candidate_Summary_2026-10-13.md). Lutri, Trade Secrets and Yawgmoth's Bargain remain registered project exceptions; their official banned status is distinct.

Deck #9 Cormela, Glamour Thief: [final list](refinement/decklists/Cormela_Glamour_Thief_Refined_2026-10-13.txt), [verification](refinement/verification/Cormela_Glamour_Thief_Verification_2026-10-13.md); added Galvanic Iteration, cut Grapeshot. Deck #10 Dr. Eggman: [final list](refinement/decklists/Dr_Eggman_Refined_2026-10-13.txt), [verification](refinement/verification/Dr_Eggman_Verification_2026-10-13.md); added Ruin Grinder, cut Megrim. Deck #11 Davros, Dalek Creator: [final list](refinement/decklists/Davros_Dalek_Creator_Refined_2026-10-13.txt), [verification](refinement/verification/Davros_Dalek_Creator_Verification_2026-10-13.md); added Cybermat, cut Counterspell. Current-cycle total: 11/62 locked; next is #12 Doctor Doom, King of Latveria.

Deck #12 Doctor Doom, King of Latveria: [final list](refinement/decklists/Doctor_Doom_Refined_2026-10-13.txt), [verification](refinement/verification/Doctor_Doom_Verification_2026-10-13.md); added Glorious Purpose, cut The Soul Stone. Current-cycle total: 12/62 locked; next is #13 Don Andres, the Renegade.

**Tracker-order correction (2026-10-13):** the authoritative order places Crosis, the Purger at #10 and Cult of Skaro at #11. The already verified/locked later decks retain their lists and locks but use the corrected tracker numbering: Davros #12, Doctor Doom #13, Don Andres #14, Dr. Eggman #15. Candidate and change-row identifiers and cumulative ledger deck numbers were aligned to that order. Next work resumes at Crosis #10.

Deck #10 Crosis, the Purger: [final list](refinement/decklists/Crosis_Refined_2026-10-13.txt), [verification](refinement/verification/Crosis_Verification_2026-10-13.md); added Blizzard Specter and Recoil, cut Specter's Shroud and Chaos Warp. Current-cycle total: 14/62 locked; next is #11 Cult of Skaro.
