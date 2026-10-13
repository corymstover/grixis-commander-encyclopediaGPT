# Duplicate Source Reconciliation — 2026-10-13

## Purpose

This record distinguishes byte-identical duplicate uploads, current authoritative material, historical snapshots, and different archive wrappers of the same underlying decklists. It is a **non-destructive reconciliation**: no source uploads, original archives, historical snapshots, or repository decklists were deleted or overwritten as part of this review.

## 1. Byte-identical duplicate upload groups

The following groups were SHA-256 checked in the current working upload directory. Files within each group have identical byte counts and identical SHA-256 digests.

| File group | Copies checked | Bytes each | SHA-256 | Decision |
|---|---:|---:|---|---|
| `Grixis_Refinement_Protocol_v1.md`, `(1).md`, `(2).md` | 3 | 16,106 | `3d12c4a206c98380a63217ff9dc73f2081aef08ac85fa18978e104e504ade90a` | Keep the protocol version referenced by the operational repository; duplicate uploads are byte-identical. |
| `Baseline_And_Research_Freshness_Report_2026-10-12.md`, `(1).md`, `(2).md` | 3 | 3,213 | `1f7e5fa4ce5b7375391b9324e7c05e9a9589ab5a0242bd8f1c258792105af44e` | Keep the current report in the repository; duplicates are identical. It is still a historical October 12 report, so later metadata results are maintained separately. |
| `Deck_Refinement_Tracker_2026-10-12.csv`, `(1).csv`, `(2).csv` | 3 | 26,200 | `b1a6345cea002d58cddb4ae109965f0c4321f82fd39b378c713dcee8a6472eeb` | These are identical uploaded starting copies. The **live campaign tracker** on the refinement branch is a subsequent, deliberately updated working record and is not expected to have this hash. |
| `Candidate_Decision_Ledger_TEMPLATE.csv`, `(1).csv` | 2 | 713 | `73aca7cfb0dee3c002f040f25289085a4f350b2045e69e06b350f34f73e858fb` | One current template is sufficient in the repository; keep both upload originals until the user handles the Sources panel. |
| `Grixis_Optimization_Kit_2026-10-12.zip`, `(1).zip` | 2 | 13,781 | `32e143122748c95e31a273e67be3b23806a170955f6bac0849c93a770aa3b52b` | Byte-identical kit archives; the individual kit documents are imported in the repository. |

The newer operational tracker, the working candidate ledger, and the generated rule/test documents have their own commit history and must not be replaced with the original duplicate uploads.

## 2. Current authoritative baseline versus historical material

**Current source package:** `Grixis_Commander_Encyclopedia_Current_Source_Package_2026-10-12(1).zip`, SHA-256 `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`. Its ZIP integrity passed. The internal manifest contains 165 files and all 165 match the listed byte counts and SHA-256 hashes.

The source package separates current material from v8.1.4 historical research. These pairs are **not duplicates**: the current and historical variants differ in data and purpose, and must both be retained with provenance.

| Subject | Current authoritative source within package | Historical snapshot within package / uploaded working directory | Decision |
|---|---|---|---|
| Card audit | `03_Current_Trackers_and_Audits/Grixis_Deck_Card_Audit_Current_2026-10-12.csv` (3,771,097 bytes) | `06_Historical_v8_1_4_Research_Snapshots/deck_card_audit.csv` (3,457,576 bytes) | Current file is the baseline membership audit; historical file is retained for provenance. |
| Mechanical deck audit summary | `03_Current_Trackers_and_Audits/Grixis_Deck_Audit_Summary_Current_2026-10-12.csv` (26,763 bytes) | `06_Historical_v8_1_4_Research_Snapshots/deck_audit_summary(1).csv` (6,435 bytes) | Do not treat historical summary as the current audit. |
| Deck/source inventory | `03_Current_Trackers_and_Audits/Grixis_Deck_Source_Inventory_Current_2026-10-12.csv` (25,635 bytes) | `06_Historical_v8_1_4_Research_Snapshots/deck_source_inventory.csv` (12,552 bytes) | Current inventory wins for current membership; keep historical file. |
| Candidate rankings | `04_Current_Research_and_Rules/commander_candidate_rankings_top100_per_commander_current_2026-10-12.csv` (4,821,852 bytes) | `06_Historical_v8_1_4_Research_Snapshots/commander_candidate_rankings_top100_per_commander.csv` (4,362,396 bytes) | Use the current-named ranking as the fresh discovery pool; historical scores remain historical evidence only. |
| Strategy profiles | `04_Current_Research_and_Rules/commander_strategy_profiles_current_2026-10-12.csv` (39,044 bytes) | `06_Historical_v8_1_4_Research_Snapshots/commander_strategy_profiles(1).csv` (30,816 bytes) | Current file is the current profile dataset, but machine-seeded/incomplete profiles are scaffolding rather than finished strategic blueprints. |
| Research manifest | `04_Current_Research_and_Rules/commander_research_manifest_current_2026-10-12.csv` (33,312 bytes) | `06_Historical_v8_1_4_Research_Snapshots/commander_research_manifest.csv` (22,848 bytes) | Current manifest governs the current research batch; retain historical manifest. |
| Identity overrides | `04_Current_Research_and_Rules/card_identity_resolution_overrides_current_2026-10-12.csv` (756 bytes) | `06_Historical_v8_1_4_Research_Snapshots/card_identity_resolution_overrides_v8_1_4.csv` (595 bytes) | Use current overrides for current membership; preserve historical overrides. |
| Project exceptions | `04_Current_Research_and_Rules/project_exceptions_current_2026-10-12.csv` (4,400 bytes) | `06_Historical_v8_1_4_Research_Snapshots/project_exceptions_current_v8_1_4.csv` (2,625 bytes) | Current registry governs current exception checks; historical registry is provenance only. |
| CSV/TXT reconciliation | `03_Current_Trackers_and_Audits/Grixis_CSV_TXT_Reconciliation_Current_2026-10-12.csv` (6,717 bytes) | `06_Historical_v8_1_4_Research_Snapshots/csv_txt_reconciliation.csv` (2,861 bytes) | Use current reconciliation for current decklist membership. |
| Delta detail and summary | `03_Current_Trackers_and_Audits/Grixis_Decklist_Delta_Detail_Current_2026-10-12.csv` (32,282 bytes); `Grixis_Decklist_Delta_Summary_Current_2026-10-12.csv` (23,612 bytes) | No direct old equivalent assumed here | Preserve to explain the differences from prior snapshots; not a substitute for decklists. |

The uploaded top-level historical files were checked against the corresponding entries in the package's historical v8.1.4 directory. These checked copies are byte-identical to their matching package historical entries: source guide; candidate-ranking methodology; identity overrides; candidate ranking dataset; research manifest; strategy profiles; CSV/TXT reconciliation; deck-audit summary; deck card audit; source inventory; audit manifest; and v8.1.4 exception registry. The current authoritative data must be selected from the package's explicitly labeled current subdirectories, not inferred from whichever similarly named file is easiest to find.

## 3. Current decklist archive formats

- The four canonical current ZIP archives identified in `Grixis_Current_Source_Manifest_2026-10-12.json` are the authoritative archive artifacts and were verified against their exact SHA-256 values.
- `GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz` is the compact repository mirror, containing the exact same 124 CSV/TXT file contents. All 124 were independently compared byte-for-byte against the current source package: no missing, differing, or extra files. Its SHA-256 is `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`.
- A separate `.zip` wrapper and the `.tar.gz` wrapper are not byte-identical archive files, but their decklist members are the same. Keep the compact `.tar.gz` as the current GitHub baseline archive to avoid multiplying equivalent archive formats unnecessarily.
- The four originals are retained in the uploaded full source package; they have **not** all been transferred as individual ZIP assets to GitHub. The GitHub repository is consequently a verified decklist-baseline mirror, but not yet a complete per-file mirror of the entire original research package.

## 4. Operational canonical copies

The active project uses these current operational records:
- `README.md` and `source-package/IMPORT_STATUS.md` on `main` for project status and source-consolidation boundary.
- `source-package/Grixis_Current_Source_Manifest_2026-10-12.json` and `source-package/Grixis_Independent_Baseline_Audit_2026-10-12.json` for current source manifest and independent structural audit.
- `source-package/Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv` plus the compact tar archive for frozen decklist bytes.
- `baseline/freeze-2026-10-12` for the protected baseline branch.
- `refinement/campaign-2026-10-12` for work in progress, including current Scryfall metadata output, live tracker, Abaddon blueprint, candidate ledger, interaction review, test plan, and isolated variant.

The uploaded tracker/protocol/report/template duplicates have not been deleted. The original source ZIP also remains available as the integrity-verified package record.

## 5. Source file transfer limitations and next order

The source package contains several raw research files of multiple megabytes, including the current full card-audit overlay (~3.77 MB) and commander candidate rankings (~4.82 MB), plus the four original ZIP archives. The available connected GitHub actions expose text-file creation/update and file reads, but do not expose a binary repository-release-asset uploader in the currently available action set. These large raw files should not be hand-truncated or reserialized. If a binary-safe upload route becomes available, upload and re-hash them; until then the exact source package remains the verified store for those datasets, while their current names/hashes and provenance should be tracked in this repo.

No source deletions are authorized by this report. Any later cleanup should be a separate, reversible action after the Source panel is reconciled and a backup is confirmed.


## Additional exact source mirrors — 2026-10-13

After the initial duplicate-source report, seven more files from the verified current source package were individually mirrored under `source-package/reference-copies/current-package-text-2026-10-12/` and checked by Git blob SHA against the packaged source bytes:

- `README_START_HERE.md` — source SHA-256 `3644e39719fdc16035b1b56ac107ef4228fe64c84bcc766dadaf0d7ffa49e84e`.
- `Grixis_Project_Charter_Current_2026-10-12.md` — `57d5c4aba3a6b7abec5305c2de2f53efdd354361d74c0f3559458d4bfdd16aa5`.
- `Grixis_Continuation_Progress_Current_2026-10-12.md` — `544676bf173a056e31f641fc27826d5caef7cf0c7b0a4be776be973babaf85ae`.
- `Grixis_Source_Package_Build_Validation_2026-10-12.json` — `fe35338dab567c72c21ac369ffb1036c213689a79f696ac025e44f7fc6d45052`.
- `Legality_and_Audit_Freshness_Note.md` — `3737de8aacaee97f27e9547a66aef2926b4222f0ca27c6be9d66c78767ba4783`.
- `Grixis_Project_Current_Status_2026-10-12.md` — `d7cf8a7ea1a3332ab96b1d5290953766a5ac30e30b6f5f18c520f87aab0928c6`.
- `Grixis_Current_Source_Manifest_2026-10-12.json` — `f3e4562987052ce7123d08a048be491ee42def53042ec1b0e937da8857ec4896`.

The exact-file inventory README is in that directory. These are package-time source records and are preserved unchanged; the later Scryfall report and active tracker supersede their dated pending-status statements. The package's internal 165-entry SHA-256 manifest, the large raw card audit/rankings, current mid-sized audit/research tables, and original current/historical ZIP archives remain in the verified source ZIP but not all as individual GitHub files. No source files were deleted.
