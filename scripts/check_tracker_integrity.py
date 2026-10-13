#!/usr/bin/env python3
"""Fail-closed structural validation for the 62-deck refinement tracker.

This catches malformed rows (including accidental unescaped quotes), duplicate deck IDs,
and impossible finalization metadata before tracker changes are accepted in CI.
"""
from __future__ import annotations
import argparse
import csv
import io
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"


def validate_tracker_text(content: str, *, expected_decks: int = 62) -> dict[str, Any]:
    errors: list[str] = []
    reader = csv.DictReader(io.StringIO(content, newline=""))
    headers = reader.fieldnames or []
    if not headers:
        return {"validation": "FAIL", "errors": ["tracker has no CSV header"], "rows": 0}
    if len(headers) != len(set(headers)):
        errors.append("tracker header contains duplicate column names")
    if any(not h.strip() for h in headers):
        errors.append("tracker header contains a blank column name")
    required = {"deck_id", "final_gate_passed", "final_list_hash", "user_approval_date"}
    missing = sorted(required - set(headers))
    if missing:
        errors.append(f"required tracker column(s) missing: {missing}")
    rows = list(reader)
    if len(rows) != expected_decks:
        errors.append(f"expected {expected_decks} data rows; found {len(rows)}")

    ids: list[str] = []
    malformed_rows: list[int] = []
    approval_errors: list[str] = []
    for line_number, row in enumerate(rows, start=2):
        if None in row and row[None]:
            malformed_rows.append(line_number)
        if any(row.get(h) is None for h in headers):
            malformed_rows.append(line_number)
        deck_id = (row.get("deck_id") or "").strip()
        if not deck_id:
            errors.append(f"blank deck_id on CSV line {line_number}")
        ids.append(deck_id)
        gate = (row.get("final_gate_passed") or "").strip().upper()
        list_hash = (row.get("final_list_hash") or "").strip()
        approval_date = (row.get("user_approval_date") or "").strip()
        if gate == "YES" and (not list_hash or not approval_date):
            approval_errors.append(f"{deck_id}: YES requires both final_list_hash and user_approval_date")
        elif gate in {"NO", "PENDING", ""} and (list_hash or approval_date):
            approval_errors.append(f"{deck_id}: {gate or 'blank'} gate must not carry approval hash/date")
        elif gate not in {"YES", "NO", "PENDING", ""}:
            approval_errors.append(f"{deck_id}: unrecognized final_gate_passed value {gate!r}")

    if malformed_rows:
        errors.append(f"malformed CSV field counts on line(s): {sorted(set(malformed_rows))}")
    duplicates = sorted({x for x in ids if x and ids.count(x) > 1})
    if duplicates:
        errors.append(f"duplicate deck_id(s): {duplicates}")
    if approval_errors:
        errors.extend(approval_errors)
    return {
        "validation": "PASS" if not errors else "FAIL",
        "expected_decks": expected_decks,
        "rows": len(rows),
        "columns": len(headers),
        "unique_deck_ids": len(set(x for x in ids if x)),
        "malformed_rows": sorted(set(malformed_rows)),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tracker", type=Path, default=TRACKER)
    parser.add_argument("--expected-decks", type=int, default=62)
    parser.add_argument("--report-output", type=Path)
    args = parser.parse_args()
    try:
        report = validate_tracker_text(args.tracker.read_text(encoding="utf-8-sig"), expected_decks=args.expected_decks)
    except OSError as exc:
        report = {"validation": "FAIL", "errors": [str(exc)]}
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    print(encoded, end="")
    if args.report_output:
        args.report_output.parent.mkdir(parents=True, exist_ok=True)
        args.report_output.write_text(encoded, encoding="utf-8")
    return 0 if report.get("validation") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
