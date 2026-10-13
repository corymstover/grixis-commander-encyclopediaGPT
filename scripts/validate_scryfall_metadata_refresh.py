#!/usr/bin/env python3
"""Fail-closed freshness/completeness validation for project Scryfall metadata.

This validates generated summary data before it is accepted as current evidence.
It does not establish card rulings or replace commander-specific rules review.
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_timestamp(value: str, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} is missing")
    try:
        result = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{field} is not ISO-8601: {value!r}") from exc
    if result.tzinfo is None:
        raise ValueError(f"{field} has no timezone offset")
    return result.astimezone(timezone.utc)


def validate_summary(summary: dict[str, Any], *, now: datetime | None = None,
                     max_generated_age_hours: float = 2, max_bulk_age_hours: float = 72,
                     expected_decks: int = 62) -> dict[str, Any]:
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    errors: list[str] = []
    try:
        generated = parse_timestamp(summary.get("generated_at_utc"), "generated_at_utc")
        generated_age = (now - generated).total_seconds() / 3600
        if generated_age < -0.0833:
            errors.append(f"generated_at_utc is more than 5 minutes in the future ({generated.isoformat()})")
        elif generated_age > max_generated_age_hours:
            errors.append(f"snapshot is stale: generated {generated_age:.2f} hours ago; maximum is {max_generated_age_hours}")
    except ValueError as exc:
        generated_age = None
        errors.append(str(exc))
    try:
        bulk_updated = parse_timestamp(summary.get("bulk_updated_at"), "bulk_updated_at")
        bulk_age = (now - bulk_updated).total_seconds() / 3600
        if bulk_age < -0.0833:
            errors.append(f"bulk_updated_at is more than 5 minutes in the future ({bulk_updated.isoformat()})")
        elif bulk_age > max_bulk_age_hours:
            errors.append(f"bulk data is stale: updated {bulk_age:.2f} hours ago; maximum is {max_bulk_age_hours}")
    except ValueError as exc:
        bulk_age = None
        errors.append(str(exc))
    if summary.get("bulk_type") != "default_cards":
        errors.append(f"expected bulk_type=default_cards, found {summary.get('bulk_type')!r}")
    if summary.get("deck_count") != expected_decks:
        errors.append(f"expected {expected_decks} decks, found {summary.get('deck_count')!r}")
    decklist_rows = summary.get("decklist_rows")
    rows_written = summary.get("rows_written")
    exact_matches = summary.get("exact_matches")
    if not isinstance(decklist_rows, int) or decklist_rows <= 0:
        errors.append(f"decklist_rows must be a positive integer; found {decklist_rows!r}")
    if rows_written != decklist_rows:
        errors.append(f"rows_written ({rows_written!r}) does not equal decklist_rows ({decklist_rows!r})")
    if exact_matches != decklist_rows:
        errors.append(f"exact_matches ({exact_matches!r}) does not equal decklist_rows ({decklist_rows!r})")
    count_aliases = {
        "not_found": ("not_found",), "ambiguous": ("ambiguous",),
        "name_variant_reviews": ("name_variant_reviews",),
        "missing Oracle text": ("missing_oracle_text", "blank_oracle_text_rows"),
        "missing Oracle IDs": ("missing_oracle_id",),
    }
    for label, keys in count_aliases.items():
        value = next((summary[k] for k in keys if k in summary), 0)
        if value != 0:
            errors.append(f"{label} count must be zero; found {value!r}")
    list_failures = {
        "color identity mismatches": ("color_identity_mismatches",),
        "unresolved printing rows": ("unresolved_printing_rows",),
        "unresolved project exceptions": ("unresolved_project_exception_rows",),
        "unexpected official-illegal rows": ("unexpected_official_illegal_rows",),
        "unresolved commander identities": ("decks_with_unresolved_commander_identity",),
    }
    for label, keys in list_failures.items():
        value = next((summary[k] for k in keys if k in summary), [])
        if value:
            count = len(value) if isinstance(value, list) else value
            errors.append(f"{label} must be empty; found {count!r}")
    result = str(summary.get("overall_result", ""))
    if not result.startswith("METADATA_REFRESH_PASS"):
        errors.append(f"overall_result is not a metadata pass: {result!r}")
    return {
        "validation": "PASS" if not errors else "FAIL",
        "generated_at_utc": summary.get("generated_at_utc"),
        "bulk_updated_at": summary.get("bulk_updated_at"),
        "generated_age_hours": round(generated_age, 3) if generated_age is not None else None,
        "bulk_age_hours": round(bulk_age, 3) if bulk_age is not None else None,
        "expected_decks": expected_decks, "deck_count": summary.get("deck_count"),
        "decklist_rows": decklist_rows, "rows_written": rows_written, "exact_matches": exact_matches,
        "errors": errors,
        "interpretation": "Metadata freshness/completeness only; rules interactions, project exceptions, and deck approval are separate gates.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--report-output", type=Path)
    parser.add_argument("--max-generated-age-hours", type=float, default=2)
    parser.add_argument("--max-bulk-age-hours", type=float, default=72)
    parser.add_argument("--expected-decks", type=int, default=62)
    args = parser.parse_args()
    try:
        summary = json.loads(args.summary.read_text(encoding="utf-8"))
        if not isinstance(summary, dict):
            raise ValueError("summary root must be a JSON object")
        report = validate_summary(summary, max_generated_age_hours=args.max_generated_age_hours,
                                  max_bulk_age_hours=args.max_bulk_age_hours, expected_decks=args.expected_decks)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        report = {"validation": "FAIL", "errors": [str(exc)]}
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    print(encoded, end="")
    if args.report_output:
        args.report_output.parent.mkdir(parents=True, exist_ok=True)
        args.report_output.write_text(encoded, encoding="utf-8")
    return 0 if report.get("validation") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
