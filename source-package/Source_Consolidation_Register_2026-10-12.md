# Source Consolidation Register — 2026-10-12

## Canonical choices

The active repository now has one canonical copy of the refinement protocol, tracker, baseline/freshness report, decision ledger template, playtest template, and finalization certificate under `refinement/`. The October 12 current source package is the authoritative deck-membership baseline. Older Updated archives and v8.1.4 files remain historical evidence.

The original uploaded source package ZIP passes integrity checks. Its own SHA-256 manifest contains 165 payload entries and every entry passed exact size + SHA-256 verification. The outer package SHA-256 is:

`47892245c2cefcf528c38fa9d9e56653d6e71a0fc73fd5ea5eecdd90e2032746`

Four authoritative deck archive hashes are recorded in `Grixis_Current_Source_Manifest_2026-10-12.json`; individual current CSV/TXT hashes are now captured in `Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv`.

## Exact duplicate uploads identified locally

The following filename pairs were verified byte-for-byte identical by size and SHA-256. Their duplicate status is exact, not inferred from similar filenames.

| Duplicate group | SHA-256 | Canonical repository destination |
|---|---|---|
| `Grixis_Optimization_Kit_2026-10-12.zip` and `Grixis_Optimization_Kit_2026-10-12(1).zip` | `32e143122748c95e31a273e67be3b23806a170955f6bac0849c93a770aa3b52b` | Individual files under `refinement/` |
| `Deck_Refinement_Tracker_2026-10-12(1).csv` and `Deck_Refinement_Tracker_2026-10-12(2).csv` | `b1a6345cea002d58cddb4ae109965f0c4321f82fd39b378c713dcee8a6472eeb` | `refinement/Deck_Refinement_Tracker_2026-10-12.csv` |
| `Grixis_Refinement_Protocol_v1(1).md` and `Grixis_Refinement_Protocol_v1(2).md` | `3d12c4a206c98380a63217ff9dc73f2081aef08ac85fa18978e104e504ade90a` | `refinement/Grixis_Refinement_Protocol_v1.md` |
| `Baseline_And_Research_Freshness_Report_2026-10-12(1).md` and `Baseline_And_Research_Freshness_Report_2026-10-12(2).md` | `1f7e5fa4ce5b7375391b9324e7c05e9a9589ab5a0242bd8f1c258792105af44e` | `refinement/Baseline_And_Research_Freshness_Report_2026-10-12.md` |

## Preservation decisions

- No deck archive or decklist was deleted or overwritten.
- The four current FINAL archives and four previous Updated archives remain distinct in the source package; they are not duplicates.
- The v8.1.4 research snapshot is retained under a historical path and must not be called a fresh audit of current card membership.
- The uploaded duplicate attachments have not been physically deleted. This import workflow can consolidate the canonical repository layout and document exact duplicates; deleting project-source attachments is a separate source-management operation and is not necessary to establish a single repository path.

## What is still not mirrored in GitHub

The source package ZIP and its four canonical deck archives, four historical archives, 124 extracted list files, and full card-audit / candidate-ranking datasets are still held in the supplied source-package attachment, not committed individually into this repository. The hash manifests establish the identity of these inputs but do not mean their contents have been transferred to GitHub.
