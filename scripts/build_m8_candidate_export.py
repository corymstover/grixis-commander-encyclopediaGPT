"""Create a non-certified M8 preview from the exact current owner-locked 62.

This script deliberately does not infer M6/M7 milestone acceptance, produce a
Commander-legal replacement for project exceptions, or rewrite canonical lists.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
OUTPUT = ROOT / "exports/m8_candidate_2026-10-28"
ARCHIVE = ROOT / "exports/Grixis_Commander_Encyclopedia_62_M8_CANDIDATE_2026-10-28.zip"
LINE = re.compile(r"^(\d+)x\s+(.+?)(?:\s+\[(Commander|Companion)\])?$")
BASICS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
EXCEPTIONS = {
    "Cecily__Bjorna__Lutri": [
        "Lutri, the Spellchaser (banned as companion; project-only)",
        "Trade Secrets (Commander banned; project-only)",
        "Yawgmoth's Bargain (Commander banned; project-only)",
    ],
    "Sauron__Lord_of_the_Rings": ["Nazgûl copies permitted by card text"],
    "Sauron__the_Dark_Lord": ["Nazgûl copies permitted by card text"],
    "The_Madcap_Jester": [
        "The Madcap Jester (future-release/project commander)",
        "Dragon's Smile (future-release/project card)",
    ],
    "Tresserhorn_s_Lord__Returned": [
        "Tresserhorn's Lord, Returned (future-release/project commander)",
    ],
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_cards(raw: bytes, deck_id: str) -> tuple[list[tuple[int, str, str]], int]:
    cards: list[tuple[int, str, str]] = []
    counts: Counter[str] = Counter()
    for line in raw.decode("utf-8-sig").splitlines():
        if not line.strip():
            continue
        match = LINE.fullmatch(line.strip())
        if not match:
            raise ValueError(f"{deck_id}: unparseable line {line!r}")
        qty, name, zone = int(match.group(1)), match.group(2), match.group(3) or "Main"
        if qty < 1 or zone != "Main" and qty != 1:
            raise ValueError(f"{deck_id}: invalid quantity/zone for {name}")
        cards.append((qty, name, zone))
        counts[name] += qty

    commanders = [entry for entry in cards if entry[2] == "Commander"]
    companions = [entry for entry in cards if entry[2] == "Companion"]
    if len(commanders) not in (1, 2):
        raise ValueError(f"{deck_id}: expected 1 or 2 commanders, got {len(commanders)}")
    if bool(companions) != (deck_id == "Cecily__Bjorna__Lutri"):
        raise ValueError(f"{deck_id}: unexpected companion configuration")
    playable = sum(q for q, _, zone in cards if zone != "Companion")
    if playable != 100:
        raise ValueError(f"{deck_id}: expected 100 playable cards, got {playable}")
    for name, qty in counts.items():
        allowed = 9 if name == "Nazgûl" else float("inf") if name in BASICS else 1
        if qty > allowed:
            raise ValueError(f"{deck_id}: illegal copy count {qty}x {name}")
    if len(companions) + playable != sum(q for q, _, _ in cards):
        raise ValueError(f"{deck_id}: companion accounting failed")
    return cards, playable


def read_current() -> list[dict]:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    decks = state["decks"]
    normalized = {re.sub(r"_+", "_", key).casefold(): key for key in decks}
    if len(normalized) != len(decks):
        raise ValueError("Ambiguous normalized deck IDs")
    with TRACKER.open(encoding="utf-8", newline="") as file:
        tracker = list(csv.DictReader(file))
    if len(tracker) != 62 or len(decks) != 62:
        raise ValueError("Expected exactly 62 tracker and registry entries")
    result = []
    for row in tracker:
        tracker_id = row["deck_id"]
        deck_id = normalized[re.sub(r"_+", "_", tracker_id).casefold()]
        data = decks[deck_id]
        if (data.get("approval_status"), data.get("lock_status"), data.get("final_gate_passed")) != ("APPROVED", "LOCKED", True):
            raise ValueError(f"{deck_id}: not owner approved, locked and final-gate-passed")
        path = ROOT / data["approved_list_artifact"]
        raw = path.read_bytes()
        digest = sha256(raw)
        if digest != data["approved_list_sha256"] or digest != data.get("m7_final_candidate_sha256"):
            raise ValueError(f"{deck_id}: live source SHA mismatch")
        if row["final_list_hash"] != digest:
            raise ValueError(f"{deck_id}: tracker hash mismatch")
        approval = ROOT / data["approval_record_artifact"]
        if not approval.is_file() or digest not in approval.read_text(encoding="utf-8"):
            raise ValueError(f"{deck_id}: missing exact-SHA owner approval receipt")
        cards, playable = parse_cards(raw, deck_id)
        result.append({"id": deck_id, "row": row, "record": data, "raw": raw, "cards": cards,
                       "playable": playable, "sha256": digest})
    if len({item["id"] for item in result}) != 62:
        raise ValueError("Duplicate roster ID")
    return result


def build() -> None:
    decks = read_current()  # fail before creating anything
    if OUTPUT.exists() or ARCHIVE.exists():
        raise FileExistsError("M8 candidate already exists; preserve it and review before regenerating")
    (OUTPUT / "decks").mkdir(parents=True)
    (OUTPUT / "canonical_sources").mkdir()
    manifest = []
    master = []
    for idx, item in enumerate(decks, start=1):
        deck_id = item["id"]
        data = item["record"]
        cards = item["cards"]
        title = item["row"]["commander_names"]
        name = re.sub(r"[^A-Za-z0-9._-]+", "_", title).strip("_")
        filename = f"{idx:02d}_{name}.txt"
        source = f"canonical_sources/{filename}"
        export = f"decks/{filename}"
        (OUTPUT / source).write_bytes(item["raw"])
        commanders = [entry for entry in cards if entry[2] == "Commander"]
        main = [entry for entry in cards if entry[2] == "Main"]
        companions = [entry for entry in cards if entry[2] == "Companion"]
        ordered = commanders + main + companions
        archidekt = "".join(f"{qty}x {card}\n" for qty, card, _ in ordered)
        (OUTPUT / export).write_text(archidekt, encoding="utf-8", newline="\n")
        master.append(f"===== {idx:02d}/62 — {title} =====\n{archidekt}\n")
        manifest.append({
            "number": idx, "deck_id": deck_id, "commander": title,
            "commander_cards": [name for _, name, _ in commanders],
            "companion_cards": [name for _, name, _ in companions],
            "playable_cards": item["playable"],
            "source_file": data["approved_list_artifact"],
            "source_sha256": item["sha256"], "owner_approval_date": data["user_approval_date"],
            "owner_receipt": data["approval_record_artifact"],
            "archive_source": source, "archive_source_sha256": sha256(item["raw"]),
            "archidekt_file": export, "archidekt_sha256": sha256(archidekt.encode("utf-8")),
            "power_bracket": data.get("m7_power_bracket"),
            "archidekt_tags": data.get("m7_archidekt_tags"),
            "project_exceptions": EXCEPTIONS.get(deck_id, []),
        })

    (OUTPUT / "MASTER.txt").write_text("".join(master), encoding="utf-8", newline="\n")
    metadata_gaps = [d["deck_id"] for d in manifest if not d["power_bracket"] or not d["archidekt_tags"]]
    index = {
        "schema_version": 1,
        "status": "M8_CANDIDATE_NOT_CERTIFIED_OR_OWNER_ACCEPTED",
        "source": "corymstover/grixis-commander-encyclopediaGPT/main",
        "source_cycle": "global-restart-2026-10-13",
        "decks": manifest,
        "release_blockers": [
            "Formal M6 and aggregate M7 milestone acceptance not demonstrated",
            "Original M6 I/J Phase B and final 62-deck certificates not fully completed",
            "Fresh current Oracle/official legality and named exceptions require final signoff",
            "Bjorna/Cecily derived official-legal projection not yet regenerated from current exact source",
            f"Missing power-bracket/tag metadata for {len(metadata_gaps)} decks: {', '.join(metadata_gaps)}",
        ],
    }
    (OUTPUT / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUTPUT / "README.txt").write_text(
        "GRIXIS COMMANDER ENCYCLOPEDIA — M8 CANDIDATE (NOT CERTIFIED)\n"
        "==========================================================\n\n"
        "Exactly 62 owner-approved source lists are present. Each source is SHA-bound to the "
        "live canonical repository. The 62 decks in decks/ are normalized for Archidekt "
        "paste/import; choose the commander(s) and, when applicable, the separately shown "
        "Lutri companion manually. See index.json for official-vs-project exception labels.\n\n"
        "This package is NOT formal M6, M7, or M8 milestone acceptance, full Magic gameplay "
        "certification, or an official Commander-legal projection for project-only exceptions. "
        "Do not distribute as the certified final edition until release_blockers are resolved.\n",
        encoding="utf-8", newline="\n",
    )
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as file:
        for path in sorted(OUTPUT.rglob("*")):
            if path.is_file():
                file.write(path, path.relative_to(OUTPUT.parent))
    print(f"M8_CANDIDATE_BUILT decks={len(manifest)} metadata_gaps={len(metadata_gaps)} archive={ARCHIVE.relative_to(ROOT)}")


def check() -> None:
    current = read_current()
    if not ARCHIVE.is_file():
        raise FileNotFoundError(ARCHIVE)
    with zipfile.ZipFile(ARCHIVE) as zf:
        root = OUTPUT.name + "/"
        index = json.loads(zf.read(root + "index.json"))
        if len(index["decks"]) != 62:
            raise ValueError("Not 62 entries in archive index")
        for item, record in zip(current, index["decks"]):
            if item["id"] != record["deck_id"] or item["sha256"] != record["source_sha256"]:
                raise ValueError("Index order or source identity mismatch")
            if sha256(zf.read(root + record["archive_source"])) != item["sha256"]:
                raise ValueError(f"{item['id']}: packaged canonical source changed")
            if sha256(zf.read(root + record["archidekt_file"])) != record["archidekt_sha256"]:
                raise ValueError(f"{item['id']}: packaged Archidekt export changed")
        if index["status"] != "M8_CANDIDATE_NOT_CERTIFIED_OR_OWNER_ACCEPTED":
            raise ValueError("Unsafe final certification assertion")
    print("M8_CANDIDATE_CHECK_PASS decks=62 exact_sources=62 exports=62 no_certification_claim")


def main() -> None:
    parser = argparse.ArgumentParser()
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--build", action="store_true")
    actions.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build() if args.build else check()


if __name__ == "__main__":
    main()
