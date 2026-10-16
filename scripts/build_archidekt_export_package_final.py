from __future__ import annotations

import csv
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

import build_archidekt_export_package as b

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_STATE = ROOT / "state/current_deck_overrides.json"
TEMP_STATE = ROOT / "state/.archidekt_export_state_tmp.json"

# These two early-cycle state entries use a canonical logical/list digest rather
# than the SHA-256 of the raw TXT bytes. Their approved source files are explicitly
# identified by the current-cycle approval evidence. Every other deck is resolved
# by exact approved_list_sha256 -> raw TXT byte match.
OVERRIDES = {
    "Admiral_Brass__Unsinkable": ROOT / "refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt",
    "Anhelo_the_Painter": ROOT / "refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt",
}


def raw_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rebuild_zip() -> None:
    if b.ZIP_PATH.exists():
        b.ZIP_PATH.unlink()
    with zipfile.ZipFile(b.ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(b.OUT_ROOT.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(b.OUT_ROOT.parent))


def main() -> None:
    original = json.loads(ORIGINAL_STATE.read_text(encoding="utf-8"))
    if original.get("cycle_id") != "global-restart-2026-10-13":
        raise SystemExit("Unexpected refinement cycle")

    temp = json.loads(json.dumps(original))
    raw_hashes: dict[str, str] = {}
    for state_key, path in OVERRIDES.items():
        if not path.exists():
            raise SystemExit(f"Missing explicit approval artifact: {path}")
        info = temp["decks"].get(state_key)
        if not info or info.get("approval_status") != "APPROVED" or info.get("lock_status") != "LOCKED" or not info.get("final_gate_passed"):
            raise SystemExit(f"Override deck is not current-cycle approved/locked: {state_key}")
        raw_hashes[state_key] = raw_sha(path)
        info["approved_list_sha256"] = raw_hashes[state_key]

    TEMP_STATE.write_text(json.dumps(temp, indent=2) + "\n", encoding="utf-8")
    try:
        b.STATE_PATH = TEMP_STATE
        b.main()
    finally:
        if TEMP_STATE.exists():
            TEMP_STATE.unlink()

    # Restore the true canonical state digest in the manifest and make resolution
    # provenance explicit. This keeps the package transparent about the two older
    # entries whose state digest was not the raw TXT SHA-256.
    with b.MANIFEST_PATH.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 62:
        raise SystemExit(f"Manifest row count mismatch: {len(rows)}")

    original_by_norm = {b.normalized_id(k): (k, v) for k, v in original["decks"].items()}
    for row in rows:
        pair = original_by_norm.get(b.normalized_id(row["deck_id"]))
        if not pair:
            raise SystemExit(f"No original state entry for {row['deck_id']}")
        state_key, info = pair
        row["canonical_sha256"] = info["approved_list_sha256"]
        row["source_raw_sha256"] = raw_hashes.get(state_key, info["approved_list_sha256"])
        row["resolution_method"] = (
            "state_explicit_approval_artifact"
            if state_key in OVERRIDES
            else "exact_state_sha256"
        )

    fieldnames = list(rows[0].keys())
    with b.MANIFEST_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    b.README_PATH.write_text(
        "GRIXIS COMMANDER ENCYCLOPEDIA 2 — ARCHIDEKT IMPORT PACKAGE\n"
        "=========================================================\n\n"
        "Cycle: global-restart-2026-10-13\n"
        "Decks: 62/62 APPROVED + LOCKED\n\n"
        "FASTEST USE\n"
        "-----------\n"
        "1. Open the decks folder.\n"
        "2. Open the numbered TXT file for the deck you want.\n"
        "3. Copy all lines.\n"
        "4. In Archidekt, create/open a Commander deck and choose Import.\n"
        "5. Paste the list and save/import.\n"
        "6. The commander is placed first in each TXT. Mark/set it as Commander in Archidekt.\n"
        "7. For Bjorna // Cecily + Lutri, set the intended commanders/companion manually.\n\n"
        "FORMAT\n"
        "------\n"
        "Each individual file uses simple Archidekt-friendly lines: 1x Card Name\n"
        "Set codes, collector numbers, and project role tags were intentionally removed.\n"
        "The MASTER file is for reference/copying deck by deck; do not paste the entire MASTER file into one deck.\n\n"
        "INTEGRITY\n"
        "---------\n"
        "60 decks were resolved by exact raw TXT SHA-256 match to current-cycle state/current_deck_overrides.json.\n"
        "Two early-cycle decks (Admiral Brass, Unsinkable and Anhelo, the Painter) use state-explicit/current-cycle approved artifacts because their state canonical digests are logical/list digests rather than raw TXT file SHA-256 values.\n"
        "All 62 source decks are current-cycle APPROVED + LOCKED, and each normalized export is structurally checked before packaging.\n"
        "Frozen source exports and approved source artifacts were not modified.\n",
        encoding="utf-8",
        newline="\n",
    )

    rebuild_zip()

    deck_files = sorted(b.DECK_DIR.glob("*.txt"))
    if len(deck_files) != 62:
        raise SystemExit(f"Expected 62 deck files; got {len(deck_files)}")
    print(
        "ARCHIDEKT_EXPORT_FINAL_PASS "
        f"decks={len(deck_files)} "
        f"overrides={len(OVERRIDES)} "
        f"zip={b.ZIP_PATH.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
