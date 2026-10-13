# Source Consolidation Reconciliation — 2026-10-13

## Result

**The authoritative 2026-10-12 decklist baseline is preserved and independently verified. The full original source package is not yet fully mirrored as individual files in GitHub.** Keep those statements separate.

## Verified source-package evidence

- Source package: `Grixis_Commander_Encyclopedia_Current_Source_Package_2026-10-12(1).zip`
- Size: 4,193,697 bytes
- SHA-256: `47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`
- ZIP integrity: PASS.
- Internal package manifest: 165 listed files checked; 165 matched expected byte sizes and SHA-256 hashes; zero missing and zero mismatches.
- The four current authoritative CSV/TXT archives embedded in the package each matched the SHA-256 in `Grixis_Current_Source_Manifest_2026-10-12.json`.
- The compact repository decklist archive `source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz` contains 124 files (62 CSV and 62 TXT). Its members were compared against the current source package: all 124 files match byte-for-byte; no missing, differing, or extra files.
- The compact archive SHA-256 is `f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20`.
- The independent structural audit records 62/62 CSV/TXT quantity reconciliations, 62/62 exact 100-card main-deck-plus-commander counts, and 62/62 singleton/copy-check passes.

## What this corrects

The latest Deep Research executive summary described all 124 individual decklists as missing from GitHub. That statement is incorrect for the current repository state: the 124 exact current decklist files are present **inside the compressed archive** and their contents have been verified. They are not all committed as 124 standalone files, and the four original canonical ZIPs are not individually mirrored at the root or as the original archives in GitHub.

## Files represented in GitHub now

- Project README, operating rules, import-status report, current source manifest, independent baseline audit, hash manifest, legality/freshness notes, and automation scripts/workflow.
- Compressed archive containing the 124 current CSV/TXT decklist files and a frozen baseline manifest.
- Controlled refinement protocol, freshness report, refinement tracker, candidate decision ledger template, playtest template, finalization certificate template, Abaddon blueprint/candidate ledger, and current Scryfall audit summary/overlay.

## Remaining source-mirror gap

The full original source package's integrity has been verified in the available uploaded package, but not every original source file has been individually mirrored into GitHub. In particular, the large current card-audit/ranking datasets, deck-update/delta details, full current research inputs, and the four original ZIP archives are not all independently stored as raw current-version files in the repository. The source package remains the verified archive of those items for this session; do not claim the GitHub repository is a complete byte-for-byte mirror of the entire package.

Historical/pre-final archives and v8.1.4 research are not replacements for the current FINAL membership baseline. Preserve them as historical evidence and do not use old profiles/rankings as fresh current evidence.

## Audit freshness

The original source manifest accurately describes its own package-build-time state; its older “fresh metadata pending” fields should not be edited to pretend the package was originally built after the refresh. The later Scryfall metadata audit is a separate, newer result on the refinement branch:

- Scryfall bulk snapshot last updated: 2026-10-12 21:06:24 UTC.
- 5,964/5,964 current decklist rows exactly matched by printing/name key.
- Zero ambiguous or unmatched printings, zero missing Oracle IDs, zero blank Oracle-text rows, zero commander color-identity mismatches.
- Six official legality statuses other than ordinary `legal` remain visible and are accounted for by registered project exceptions (Lutri companion, Trade Secrets, Yawgmoth's Bargain, The Madcap Jester, Dragon's Smile, Tresserhorn's Lord, Returned).
- The metadata refresh does not certify every rules interaction, combo, strategic blueprint, or playtest result.

## Tracker correction

The active refinement tracker has been updated to reflect the completed current Scryfall Oracle/identity and legality metadata checks. The special exception decks are labelled individually. Per-deck rules/interaction, combo, strategy, testing, finalization, and user-approval fields remain separate and were not marked complete by this metadata update.

## Next actions

1. Preserve this report and the current verified baseline unchanged.
2. Mirror the remaining raw current research datasets and original archives to GitHub when a binary-safe transfer method is available; verify every imported file against the package manifest.
3. Continue Abaddon: finish the actual rules/interaction review, choose a defensible test method, and do not apply a card swap until the decision has evidence and user approval.
4. Use the controlled protocol deck-by-deck; do not mark the other 61 decks rules-audited or refined merely because their metadata checks pass.


## Additional current source files now mirrored individually

After the initial reconciliation, these four raw current source-package files were imported without semantic edits under `source-package/research/current-2026-10-12/` and their Git blob IDs were verified against the exact extracted source-package bytes:

| File | Source SHA-256 | Verification |
|---|---|---|
| `Grixis_CSV_TXT_Reconciliation_Current_2026-10-12.csv` | `05beadf19f6ca06e0825981d128af920ef6fc75dc37b78c8753392b1585b6a6c` | Exact Git blob match after correcting one filename-field transcription; 62 data rows. |
| `project_exceptions_current_2026-10-12.csv` | `166b49d92838ec66f32607e7e209bfcd52cf74aca07de8a03d8b9c00cfeaa052` | Exact Git blob match. This is the original project-source snapshot; later Scryfall/current legality results remain separately recorded. |
| `card_identity_resolution_overrides_current_2026-10-12.csv` | `cdf180717f23cdda0bd17819b334ff2c06b3280c333f5ced3bdd2e85991a5277` | Exact Git blob match. |
| `candidate_ranking_methodology.md` | `db9823247be8bc4063dbb62c8665ebc09f27e73fe0155a6e37a2fe4b5cbb2871` | Exact Git blob match; the same methodology also occurs in the v8.1.4 historical snapshot and is byte-identical there. |

The major current files still held in the verified original package rather than individually mirrored include the ~3.77 MB current card-audit table, ~4.82 MB current candidate-ranking dataset, ~39 KB current commander-strategy profiles, ~33 KB current research manifest, current deck update tracker, and current decklist delta files. The connected GitHub tools available in this session do not expose a binary-safe release-asset uploader, and the large raw data have not been reserialized or truncated. The full original ZIP remains the verified container for those files.
