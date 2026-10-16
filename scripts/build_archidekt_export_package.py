from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "state/current_deck_overrides.json"
TRACKER_PATH = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
OUT_ROOT = ROOT / "exports/archidekt_2026-10-15"
DECK_DIR = OUT_ROOT / "decks"
ZIP_PATH = ROOT / "exports/Grixis_Commander_Encyclopedia_62_Archidekt_2026-10-15.zip"
MASTER_PATH = OUT_ROOT / "Grixis_Commander_Encyclopedia_62_MASTER.txt"
MANIFEST_PATH = OUT_ROOT / "manifest.csv"
README_PATH = OUT_ROOT / "README.txt"

QTY_RE = re.compile(r"^(\d+)\s*x?\s+(.+?)\s*$", re.IGNORECASE)
CATEGORY_RE = re.compile(r"\s+\[[^\]]*\]\s*$")
SET_COLLECTOR_RE = re.compile(r"\s+\([A-Za-z0-9_]+\)\s+\S+\s*$")
SET_ONLY_RE = re.compile(r"\s+\([A-Za-z0-9_]+\)\s*$")
FOIL_RE = re.compile(r"\s+\*(?:F|E)\*\s*$", re.IGNORECASE)
SAFE_RE = re.compile(r"[^A-Za-z0-9._-]+")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_line(raw: str) -> tuple[int, str, bool, bool] | None:
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return None
    m = QTY_RE.match(raw)
    if not m:
        return None
    qty = int(m.group(1))
    rest = m.group(2).strip()
    is_commander = bool(re.search(r"\[Commander(?:\{|\]|\s)", rest, re.IGNORECASE))
    is_companion = bool(re.search(r"\[Companion(?:\{|\]|\s)", rest, re.IGNORECASE))
    while True:
        new = CATEGORY_RE.sub("", rest).strip()
        if new == rest:
            break
        rest = new
    rest = FOIL_RE.sub("", rest).strip()
    rest = SET_COLLECTOR_RE.sub("", rest).strip()
    rest = SET_ONLY_RE.sub("", rest).strip()
    return qty, rest, is_commander, is_companion


def normalize_deck(text: str) -> tuple[str, int, int, list[str]]:
    parsed: list[tuple[int, str, bool, bool]] = []
    for line in text.splitlines():
        item = parse_line(line)
        if item:
            parsed.append(item)
    if not parsed:
        raise ValueError("No parseable card lines")

    # Preserve explicit commander/companion metadata when present. Otherwise the
    # project's standard format guarantees the commander is already first.
    if any(x[2] for x in parsed):
        commanders = [x for x in parsed if x[2]]
        normal = [x for x in parsed if not x[2] and not x[3]]
        companions = [x for x in parsed if x[3]]
        parsed = commanders + normal + companions

    lines = [f"{qty}x {name}" for qty, name, _, _ in parsed]
    quantity_total = sum(qty for qty, _, _, _ in parsed)
    distinct = len({name.casefold() for _, name, _, _ in parsed})
    return "\n".join(lines) + "\n", quantity_total, distinct, lines


def load_tracker() -> list[dict[str, str]]:
    with TRACKER_PATH.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def scan_text_sources() -> dict[str, list[tuple[str, bytes]]]:
    found: dict[str, list[tuple[str, bytes]]] = {}
    for path in ROOT.rglob("*.txt"):
        if OUT_ROOT in path.parents:
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        found.setdefault(sha256_bytes(data), []).append((str(path.relative_to(ROOT)), data))

    # Also scan any source ZIPs present in the repository so canonical hashes
    # that intentionally point to a frozen TXT export can still resolve exactly.
    for zpath in ROOT.rglob("*.zip"):
        if zpath == ZIP_PATH or OUT_ROOT in zpath.parents:
            continue
        try:
            with zipfile.ZipFile(zpath) as zf:
                for name in zf.namelist():
                    if not name.lower().endswith(".txt"):
                        continue
                    data = zf.read(name)
                    label = f"{zpath.relative_to(ROOT)}::{name}"
                    found.setdefault(sha256_bytes(data), []).append((label, data))
        except (OSError, zipfile.BadZipFile):
            continue
    return found


def choose_source(matches: list[tuple[str, bytes]]) -> tuple[str, bytes]:
    def rank(item: tuple[str, bytes]) -> tuple[int, str]:
        path = item[0]
        score = 50
        if "_Approved_" in path:
            score = 0
        elif "Approval_Candidate" in path or "Approval_Ready" in path:
            score = 10
        elif "Proposed_Final" in path or "Whole_List_Approval_Candidate" in path:
            score = 20
        elif "FINALTXT" in path:
            score = 30
        return score, path
    return sorted(matches, key=rank)[0]


def safe_filename(num: int, name: str) -> str:
    cleaned = SAFE_RE.sub("_", name).strip("_")
    return f"{num:02d}_{cleaned}.txt"


def main() -> None:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if state.get("cycle_id") != "global-restart-2026-10-13":
        raise SystemExit(f"Unexpected cycle: {state.get('cycle_id')}")
    decks_state = state.get("decks", {})
    tracker = load_tracker()
    if len(tracker) != 62:
        raise SystemExit(f"Expected 62 tracker rows; got {len(tracker)}")

    # Fail closed unless all 62 tracker decks are current-cycle locked and SHA-bound.
    missing_state: list[str] = []
    for row in tracker:
        deck_id = row["deck_id"]
        info = decks_state.get(deck_id)
        if not info:
            missing_state.append(f"{deck_id}: missing state entry")
            continue
        if info.get("approval_status") != "APPROVED" or info.get("lock_status") != "LOCKED" or not info.get("final_gate_passed"):
            missing_state.append(f"{deck_id}: not APPROVED/LOCKED/final_gate_passed")
        if not info.get("approved_list_sha256"):
            missing_state.append(f"{deck_id}: missing approved_list_sha256")
    if missing_state:
        raise SystemExit("State gate failed:\n" + "\n".join(missing_state))

    sources = scan_text_sources()
    unresolved: list[str] = []
    resolved: list[tuple[dict[str, str], dict, str, bytes]] = []
    for row in tracker:
        deck_id = row["deck_id"]
        info = decks_state[deck_id]
        expected = info["approved_list_sha256"]
        matches = sources.get(expected, [])
        if not matches:
            unresolved.append(f"{row['index']} {deck_id} {expected}")
            continue
        source_path, data = choose_source(matches)
        if sha256_bytes(data) != expected:
            raise SystemExit(f"Internal SHA mismatch for {deck_id}")
        resolved.append((row, info, source_path, data))

    if unresolved:
        raise SystemExit("Could not resolve canonical SHA to exact TXT bytes for:\n" + "\n".join(unresolved))
    if len(resolved) != 62:
        raise SystemExit(f"Resolved {len(resolved)} decks, expected 62")

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    DECK_DIR.mkdir(parents=True, exist_ok=True)
    ZIP_PATH.parent.mkdir(parents=True, exist_ok=True)

    manifest_rows: list[dict[str, str | int]] = []
    master_chunks: list[str] = []

    for n, (row, info, source_path, data) in enumerate(resolved, start=1):
        text = data.decode("utf-8-sig")
        normalized, card_count, distinct, lines = normalize_deck(text)
        commander_name = row["commander_names"]
        filename = safe_filename(n, commander_name)
        out_path = DECK_DIR / filename
        out_path.write_text(normalized, encoding="utf-8", newline="\n")

        # Basic fail-closed checks. Companion deck may intentionally export one
        # extra companion outside the 100-card library; every other deck must be 100.
        expected_count = 101 if row["deck_id"] == "Cecily__Bjorna__Lutri" and card_count == 101 else 100
        if card_count != expected_count:
            raise SystemExit(f"Unexpected normalized count for {deck_id}: {card_count}")

        master_chunks.append(
            f"===== {n:02d}/62 — {commander_name} =====\n"
            + normalized
            + "\n"
        )
        manifest_rows.append({
            "deck_number": n,
            "deck_id": row["deck_id"],
            "commander_names": commander_name,
            "archidekt_file": f"decks/{filename}",
            "card_quantity_total": card_count,
            "distinct_names": distinct,
            "canonical_sha256": info["approved_list_sha256"],
            "matched_source": source_path,
        })

    MASTER_PATH.write_text("".join(master_chunks), encoding="utf-8", newline="\n")

    with MANIFEST_PATH.open("w", encoding="utf-8", newline="") as fh:
        fieldnames = [
            "deck_number", "deck_id", "commander_names", "archidekt_file",
            "card_quantity_total", "distinct_names", "canonical_sha256", "matched_source",
        ]
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest_rows)

    README_PATH.write_text(
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
        "6. The commander line is first. Mark that card as Commander in Archidekt.\n"
        "7. For the Bjorna/Cecily/Lutri project deck, also set the intended commanders/companion manually as appropriate.\n\n"
        "FORMAT\n"
        "------\n"
        "Each individual file uses simple Archidekt-friendly lines: 1x Card Name\n"
        "Set codes, collector numbers, and project role tags were intentionally removed.\n"
        "The MASTER file is for convenient reference/copying deck by deck; do not paste the entire MASTER file into a single deck.\n\n"
        "INTEGRITY\n"
        "---------\n"
        "Every deck was resolved by matching the authoritative current-cycle approved_list_sha256 in\n"
        "state/current_deck_overrides.json to exact repository TXT bytes before normalization.\n"
        "Frozen source exports and approved lists were not modified.\n",
        encoding="utf-8",
        newline="\n",
    )

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(OUT_ROOT.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(OUT_ROOT.parent))

    # Post-build verification.
    deck_files = list(DECK_DIR.glob("*.txt"))
    if len(deck_files) != 62:
        raise SystemExit(f"Built {len(deck_files)} individual deck files, expected 62")
    print(f"ARCHIDEKT_EXPORT_PASS decks={len(deck_files)} zip={ZIP_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
