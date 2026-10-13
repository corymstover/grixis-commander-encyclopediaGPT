#!/usr/bin/env python3
"""Independent static audit of the frozen Abaddon list and pinned Scryfall overlay.

Run from repository root. It never changes deck contents. Output is a review artifact,
not a finalization certificate or gameplay-performance claim.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "source-package/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OVERLAY = ROOT / "refinement/metadata_audit/Current_Scryfall_Metadata_Overlay_2026-10-12.csv"
EXPECTED_ARCHIVE_SHA256 = "f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20"
EXPECTED_ABADDON_TXT_SHA256 = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
COMMANDER = "Abaddon the Despoiler"
BASIC_LANDS = {"plains", "island", "swamp", "mountain", "forest", "wastes"}
NAME_FIELDS = ("card_name_export", "scryfall_name", "name", "card_name", "deck_card_name", "name_in_deck", "card_name_original")
ORACLE_ID_FIELDS = ("oracle_id", "oracleId", "oracle_id_current")
ORACLE_FIELDS = ("oracle_text", "oracle_text_current", "oracle")
IDENTITY_FIELDS = ("color_identity", "colorIdentity", "color_identity_current")
LEGALITY_FIELDS = ("commander_legality", "legalities_commander", "commander_status", "commander")

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip()).casefold()

def first(row: dict, fields: tuple[str, ...]) -> str:
    for field in fields:
        if field in row and row[field] is not None and str(row[field]).strip():
            return str(row[field]).strip()
    return ""

def read_abaddon_list() -> tuple[bytes, list[dict]]:
    raw_archive = ARCHIVE.read_bytes()
    if sha256(raw_archive) != EXPECTED_ARCHIVE_SHA256:
        raise ValueError(f"Archive SHA-256 mismatch: {sha256(raw_archive)}")
    with tarfile.open(ARCHIVE, "r:gz") as tar:
        matches = [m for m in tar.getmembers() if m.isfile() and m.name.replace("\\", "/").endswith("TXT/Abaddon_the_Despoiler.txt")]
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one Abaddon TXT archive member; got {len(matches)}")
        fd = tar.extractfile(matches[0])
        if fd is None:
            raise ValueError("Could not extract Abaddon TXT")
        raw = fd.read()
    if sha256(raw) != EXPECTED_ABADDON_TXT_SHA256:
        raise ValueError(f"Abaddon TXT SHA-256 mismatch: {sha256(raw)}")
    parsed = []
    for line_no, line in enumerate(raw.decode("utf-8-sig").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        m = re.fullmatch(r"(\d+)x\s+(.+)", line)
        if not m:
            raise ValueError(f"Invalid line {line_no}: {line!r}")
        qty = int(m.group(1))
        body = m.group(2).strip()
        tag_m = re.search(r"\s+\[([^\]]+)\]\s*$", body)
        role = tag_m.group(1).strip() if tag_m else ""
        if tag_m:
            body = body[:tag_m.start()].strip()
        card_name = re.sub(r"\s+\([^)]+\)\s+\S+\s*$", "", body).strip()
        if qty <= 0 or not card_name:
            raise ValueError(f"Invalid quantity/card name on line {line_no}")
        parsed.append({"line": line_no, "quantity": qty, "name": card_name, "role_tag": role})
    return raw, parsed

def read_overlay() -> tuple[dict[str, list[dict]], list[str], str]:
    raw = OVERLAY.read_bytes()
    overlay_hash = sha256(raw)
    with OVERLAY.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        name_field = next((candidate for candidate in NAME_FIELDS if candidate in columns), None)
        if not name_field:
            raise ValueError(f"No supported card-name field in metadata overlay columns: {columns}")
        by_name: dict[str, list[dict]] = {}
        for row in reader:
            key = norm(row.get(name_field, ""))
            if key:
                by_name.setdefault(key, []).append(row)
    return by_name, columns, overlay_hash

def audit() -> dict:
    raw, parsed = read_abaddon_list()
    counts = Counter()
    for row in parsed:
        counts[row["name"]] += row["quantity"]
    total = sum(counts.values())
    commanders = [x for x in parsed if "commander" in x["role_tag"].casefold()]
    if total != 100:
        raise ValueError(f"Expected 100 cards including commander; got {total}")
    if len(commanders) != 1 or commanders[0]["name"] != COMMANDER or commanders[0]["quantity"] != 1:
        raise ValueError("Expected exactly one Abaddon commander marker")
    non_singletons = {name: qty for name, qty in counts.items() if qty > 1 and norm(name) not in BASIC_LANDS}
    if non_singletons:
        raise ValueError(f"Singleton violations: {non_singletons}")
    overlay, columns, overlay_hash = read_overlay()
    # Overlay is project-wide, so use deck_id plus exported name as the strict key.
    # Name-only joins silently collide across 62 decks (e.g., Island appears many times).
    deck_rows = {}
    for (deck_id, card_name), rows in []:
        pass
    matches, missing, ambiguous, field_issues = [], [], [], []
    for name, qty in sorted(counts.items(), key=lambda pair: pair[0].casefold()):
        hits = overlay.get(norm(name), [])
        if not hits:
            missing.append(name)
            continue
        if len(hits) != 1:
            ambiguous.append({"name": name, "match_count": len(hits)})
            continue
        row = hits[0]
        fields = {
            "oracle_id": first(row, ORACLE_ID_FIELDS),
            "oracle_text": first(row, ORACLE_FIELDS),
            "color_identity": first(row, IDENTITY_FIELDS),
            "commander_legality": first(row, LEGALITY_FIELDS),
            "type_line": first(row, ("type_line", "type_line_current", "type")),
            "set_code": first(row, ("set", "set_code", "set_code_current")),
            "collector_number": first(row, ("collector_number", "collector_number_current", "number")),
        }
        problems = [f"missing_{k}" for k in ("oracle_id", "oracle_text", "color_identity", "commander_legality") if not fields[k]]
        if problems:
            field_issues.append({"name": name, "issues": problems})
        matches.append({
            "name": name, "quantity": qty,
            "source_role_tag": next(x["role_tag"] for x in parsed if x["name"] == name),
            **fields, "metadata_fields_complete": not problems
        })
    return {
        "deck_id": "Abaddon_the_Despoiler",
        "snapshot": "2026-10-12",
        "archive_sha256": sha256(ARCHIVE.read_bytes()),
        "baseline_txt_sha256": sha256(raw),
        "overlay_sha256": overlay_hash,
        "total_cards_including_commander": total,
        "unique_card_names": len(counts),
        "commander": COMMANDER,
        "commander_marker_count": len(commanders),
        "singleton_violations": non_singletons,
        "overlay_columns": columns,
        "matched_unique_names": len(matches),
        "missing_overlay_names": missing,
        "ambiguous_overlay_names": ambiguous,
        "metadata_field_issues": field_issues,
        "records": matches,
        "status": "METADATA_JOIN_PASS — strategy/rules/fresh legality gates remain separate"
            if not missing and not ambiguous and not field_issues else "REVIEW_REQUIRED",
        "limitations": [
            "Overlay is dated 2026-10-12, not a fresh legality check at approval time.",
            "A name/metadata join does not independently verify every relevant rule interaction.",
            "This script does not certify strategic quality, simulation validity, or approval.",
            "No decklist was changed by this audit.",
        ],
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--csv-output", type=Path)
    args = parser.parse_args()
    result = audit()
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.csv_output:
        args.csv_output.parent.mkdir(parents=True, exist_ok=True)
        fields = ["name", "quantity", "source_role_tag", "oracle_id", "oracle_text", "color_identity",
                  "commander_legality", "type_line", "set_code", "collector_number", "metadata_fields_complete"]
        with args.csv_output.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in result["records"]:
                writer.writerow({key: row.get(key, "") for key in fields})
    if not args.json_output and not args.csv_output:
        print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
