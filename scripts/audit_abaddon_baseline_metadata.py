#!/usr/bin/env python3
"""Independent static audit of Abaddon's frozen list against the pinned Scryfall overlay.

No card changes are made. Metadata checks do not replace a current legality checkpoint,
rules interaction review, or explicit user approval.
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
OVERLAY = ROOT / "refinement/metadata_audit/Current_Scryfall_Metadata_Overlay.csv"
SUMMARY = ROOT / "refinement/metadata_audit/Current_Scryfall_Metadata_Audit_Summary.json"
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
    archive_bytes = ARCHIVE.read_bytes()
    actual_archive = sha256(archive_bytes)
    if actual_archive != EXPECTED_ARCHIVE_SHA256:
        raise ValueError(f"Compact archive SHA-256 mismatch: {actual_archive}")
    with tarfile.open(ARCHIVE, "r:gz") as tar:
        members = [
            m for m in tar.getmembers()
            if m.isfile() and m.name.replace("\\", "/").endswith("TXT/Abaddon_the_Despoiler.txt")
        ]
        if len(members) != 1:
            raise ValueError(f"Expected exactly one Abaddon TXT member; found {len(members)}")
        fd = tar.extractfile(members[0])
        if fd is None:
            raise ValueError("Unable to extract Abaddon TXT member")
        raw = fd.read()
    actual_txt = sha256(raw)
    if actual_txt != EXPECTED_ABADDON_TXT_SHA256:
        raise ValueError(f"Abaddon TXT SHA-256 mismatch: {actual_txt}")
    parsed = []
    for line_no, raw_line in enumerate(raw.decode("utf-8-sig").splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        match = re.fullmatch(r"(\d+)x\s+(.+)", line)
        if not match:
            raise ValueError(f"Invalid decklist line {line_no}: {line!r}")
        qty = int(match.group(1))
        body = match.group(2).strip()
        role_match = re.search(r"\s+\[([^\]]+)\]\s*$", body)
        role = role_match.group(1).strip() if role_match else ""
        if role_match:
            body = body[:role_match.start()].strip()
        name = re.sub(r"\s+\([^)]+\)\s+\S+\s*$", "", body).strip()
        if qty < 1 or not name:
            raise ValueError(f"Invalid quantity/name on line {line_no}")
        parsed.append({"line": line_no, "quantity": qty, "name": name, "role_tag": role})
    return raw, parsed

def read_overlay() -> tuple[dict[tuple[str, str], list[dict]], list[str], str]:
    raw = OVERLAY.read_bytes()
    overlay_hash = sha256(raw)
    with OVERLAY.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        name_field = next((candidate for candidate in NAME_FIELDS if candidate in columns), None)
        if "deck_id" not in columns or not name_field:
            raise ValueError(f"Overlay must contain deck_id and a supported card name field; columns={columns}")
        by_deck_name: dict[tuple[str, str], list[dict]] = {}
        for row in reader:
            key = (norm(row.get("deck_id", "")), norm(row.get(name_field, "")))
            if key[0] and key[1]:
                by_deck_name.setdefault(key, []).append(row)
    return by_deck_name, columns, overlay_hash

def validate_bulk_summary(summary: dict) -> dict:
    required = {
        "bulk_type": "default_cards",
        "deck_count": 62,
        "decklist_rows": 5964,
        "exact_matches": 5964,
        "name_variant_reviews": 0,
        "not_found": 0,
        "ambiguous": 0,
        "blank_oracle_text_rows": 0,
        "missing_oracle_id": 0,
    }
    issues = [f"{key} expected {expected!r}, got {summary.get(key)!r}"
              for key, expected in required.items() if summary.get(key) != expected]
    if not summary.get("generated_at_utc"):
        issues.append("missing generated_at_utc")
    if not summary.get("bulk_updated_at"):
        issues.append("missing bulk_updated_at")
    if summary.get("color_identity_mismatches"):
        issues.append("nonempty color_identity_mismatches")
    if summary.get("unresolved_printing_rows"):
        issues.append("nonempty unresolved_printing_rows")
    if summary.get("decks_with_unresolved_commander_identity"):
        issues.append("nonempty decks_with_unresolved_commander_identity")
    if summary.get("unresolved_project_exception_rows"):
        issues.append("nonempty unresolved_project_exception_rows")
    if summary.get("unexpected_official_illegal_rows"):
        issues.append("nonempty unexpected_official_illegal_rows")
    if summary.get("overall_result") != "METADATA_REFRESH_PASS — registered exceptions remain separately labeled; rules-interaction review remains separate":
        issues.append(f"unexpected overall_result: {summary.get('overall_result')!r}")
    if issues:
        raise ValueError("Current Scryfall bulk summary failed preflight: " + "; ".join(issues))
    return summary


def read_bulk_summary() -> dict:
    return validate_bulk_summary(json.loads(SUMMARY.read_text(encoding="utf-8")))


def audit() -> dict:
    bulk_summary = read_bulk_summary()
    raw, parsed = read_abaddon_list()
    counts: Counter[str] = Counter()
    for row in parsed:
        counts[row["name"]] += row["quantity"]
    total = sum(counts.values())
    commanders = [row for row in parsed if "commander" in row["role_tag"].casefold()]
    if total != 100:
        raise ValueError(f"Expected 100 cards including commander; got {total}")
    if len(commanders) != 1 or commanders[0]["name"] != COMMANDER or commanders[0]["quantity"] != 1:
        raise ValueError("Expected exactly one Abaddon commander marker/copy")
    singleton_violations = {
        name: qty for name, qty in counts.items()
        if qty > 1 and norm(name) not in BASIC_LANDS
    }
    if singleton_violations:
        raise ValueError(f"Singleton/copy-rule violations: {singleton_violations}")

    overlay, columns, overlay_hash = read_overlay()
    deck_id = norm("Abaddon_the_Despoiler")
    records, missing, ambiguous, field_issues = [], [], [], []
    for name, qty in sorted(counts.items(), key=lambda pair: pair[0].casefold()):
        rows = overlay.get((deck_id, norm(name)), [])
        if len(rows) == 0:
            missing.append(name)
            continue
        if len(rows) != 1:
            ambiguous.append({"name": name, "match_count": len(rows)})
            continue
        row = rows[0]
        fields = {
            "oracle_id": first(row, ORACLE_ID_FIELDS),
            "oracle_text": first(row, ORACLE_FIELDS),
            "scryfall_id": first(row, ("scryfall_id",)),
            "released_at": first(row, ("released_at",)),
            "bulk_updated_at": first(row, ("bulk_updated_at",)),
            "color_identity": first(row, IDENTITY_FIELDS),
            "commander_color_identity": first(row, ("commander_color_identity",)),
            "color_identity_check": first(row, ("color_identity_check",)),
            "commander_legality": first(row, LEGALITY_FIELDS),
            "project_exception_status": first(row, ("project_exception_status",)),
            "type_line": first(row, ("type_line", "type_line_current", "type")),
            "set_code": first(row, ("set_code", "set", "set_code_current")),
            "collector_number": first(row, ("collector_number", "collector_number_current", "number")),
            "printing_match_status": first(row, ("printing_match_status",)),
            "scryfall_name": first(row, ("scryfall_name",)),
        }
        # Blank color identity is the correct representation for colorless cards.
        # For Commander legality, rely on a populated official status field; exceptions stay separate.
        problems = []
        for key in ("oracle_id", "oracle_text", "commander_legality", "printing_match_status", "scryfall_id", "released_at", "bulk_updated_at"):
            if not fields[key]:
                problems.append(f"missing_{key}")
        if fields["bulk_updated_at"] != bulk_summary["bulk_updated_at"]:
            problems.append("row_bulk_timestamp_does_not_match_summary")
        if fields["commander_legality"].casefold() != "legal":
            problems.append("abaddon_card_not_ordinary_commander_legal")
        if not fields["color_identity_check"]:
            problems.append("missing_color_identity_check")
        elif fields["color_identity_check"].casefold() != "pass":
            problems.append("color_identity_check_not_pass")
        if fields["printing_match_status"] and fields["printing_match_status"].upper() != "EXACT_SET_COLLECTOR_AND_NAME":
            problems.append("printing_match_not_exact")
        if fields["commander_legality"].casefold() in {"banned", "not_legal", "banned_as_companion"}:
            if not fields["project_exception_status"] or fields["project_exception_status"].casefold() in {"none", "not_registered", "unresolved"}:
                problems.append("nonlegal_without_recorded_exception")
        if problems:
            field_issues.append({"name": name, "issues": sorted(set(problems))})
        records.append({
            "name": name,
            "quantity": qty,
            "source_role_tag": next(x["role_tag"] for x in parsed if x["name"] == name),
            **fields,
            "metadata_fields_complete": not problems,
        })
    passed = not missing and not ambiguous and not field_issues and not singleton_violations and total == 100
    return {
        "deck_id": "Abaddon_the_Despoiler",
        "snapshot": {"refresh_generated_at_utc": bulk_summary["generated_at_utc"], "scryfall_bulk_updated_at": bulk_summary["bulk_updated_at"], "bulk_type": bulk_summary["bulk_type"]},
        "archive_sha256": sha256(ARCHIVE.read_bytes()),
        "baseline_txt_sha256": sha256(raw),
        "overlay_sha256": overlay_hash,
        "global_scryfall_refresh_overall_result": bulk_summary["overall_result"],
        "global_scryfall_refresh_row_count": bulk_summary["decklist_rows"],
        "global_scryfall_refresh_unexpected_illegal_rows": bulk_summary["unexpected_official_illegal_rows"],
        "total_cards_including_commander": total,
        "unique_card_names": len(counts),
        "commander": COMMANDER,
        "commander_marker_count": len(commanders),
        "singleton_violations": singleton_violations,
        "overlay_columns": columns,
        "matched_unique_names": len(records),
        "missing_overlay_names": missing,
        "ambiguous_overlay_names": ambiguous,
        "metadata_field_issues": field_issues,
        "records": records,
        "status": "PASS — exact deck-scoped metadata join; rules/strategy/current legality approval gates remain separate" if passed else "REVIEW_REQUIRED",
        "limitations": [
            "Freshness is gated by validate_scryfall_metadata_refresh.py; rules and approval remain independent gates.",
            "Metadata joining does not independently verify every card interaction or establish deck optimization.",
            "Project exception statuses are recorded separately from official format status and still require designated-deck assignment review.",
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
        fieldnames = [
            "name", "quantity", "source_role_tag", "oracle_id", "oracle_text", "scryfall_id", "released_at", "bulk_updated_at",
            "color_identity", "commander_color_identity", "color_identity_check",
            "commander_legality", "project_exception_status", "type_line", "set_code",
            "collector_number", "printing_match_status", "scryfall_name", "metadata_fields_complete",
        ]
        with args.csv_output.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in result["records"]:
                writer.writerow({key: row.get(key, "") for key in fieldnames})
    if not args.json_output and not args.csv_output:
        print(json.dumps(result, indent=2))
    return 0 if str(result.get("status", "")).startswith("PASS") else 1

if __name__ == "__main__":
    raise SystemExit(main())
