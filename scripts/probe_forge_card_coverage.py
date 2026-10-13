#!/usr/bin/env python3
"""Audit Forge card-script presence at a pinned source revision.

This is a source-coverage gate only. It does not establish correct rules execution,
gameplay support, or simulator fitness.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


PINNED_RELEASE = "forge-2.0.15"
PINNED_COMMIT = "4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676"
REQUIRED_CONTROLS = (
    "Abaddon the Despoiler",
    "Aurora Phoenix",
    "Mind's Desire",  # baseline card replaced by Aurora Phoenix in the test variant
    "Underworld Breach",
    "Brain Freeze",
    "Lion's Eye Diamond",
)
NONSTANDARD_SUBTREES = {"rebalanced", "upcoming"}


def normalize_name(value: str) -> str:
    value = value.casefold()
    for source, replacement in (("æ", "ae"), ("œ", "oe"), ("ø", "o"), ("ł", "l"), ("đ", "d"), ("ð", "d"), ("þ", "th"), ("ß", "ss")):
        value = value.replace(source, replacement)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", value)


def parse_deck_names(path: Path) -> tuple[list[str], dict[str, int]]:
    """Read quantity-prefixed deck lines and return unique names plus copy counts."""
    copy_counts: dict[str, int] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        match = re.match(r"^(\d+)x\s+(.+?)\s*$", line)
        if not match:
            continue
        name = re.sub(r"\s+\[.*\]\s*$", "", match.group(2)).strip()
        if not name:
            raise ValueError(f"{path}:{line_number}: quantity line has an empty card name")
        copy_counts[name] = copy_counts.get(name, 0) + int(match.group(1))
    if not copy_counts:
        raise ValueError(f"No quantity-prefixed cards parsed from {path}")
    return list(copy_counts), copy_counts


def index_card_scripts(card_root: Path) -> tuple[dict[str, list[dict[str, Any]]], int]:
    if not card_root.is_dir():
        raise FileNotFoundError(f"Forge card-script root not found: {card_root}")
    scripts: dict[str, list[dict[str, Any]]] = {}
    script_count = 0
    for path in sorted(card_root.rglob("*.txt")):
        relative = path.relative_to(card_root)
        if relative.parts and relative.parts[0].casefold() in NONSTANDARD_SUBTREES:
            continue
        script_count += 1
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        names = [
            line.partition(":")[2].strip()
            for line in lines
            if line.startswith("Name:") or line.startswith("AlternateName:")
        ]
        oracle_lines = [line.partition(":")[2].strip() for line in lines if line.startswith("Oracle:")]
        has_oracle = any(value for value in oracle_lines)
        record = {
            "path": relative.as_posix(),
            "names": names,
            "has_nonempty_oracle": has_oracle,
        }
        for name in names:
            if name:
                scripts.setdefault(normalize_name(name), []).append(record)
    if script_count == 0:
        raise RuntimeError(
            f"No standard Forge .txt card scripts found under {card_root}; refusing a false coverage pass"
        )
    return scripts, script_count


def audit(
    variant_path: Path,
    card_root: Path,
    extra_cards: list[str] | None = None,
) -> dict[str, Any]:
    variant_names, copy_counts = parse_deck_names(variant_path)
    scripts, script_count = index_card_scripts(card_root)

    # Audit the exact test variant plus explicitly declared baseline-only comparison cards.
    checked_names = list(dict.fromkeys(variant_names + (extra_cards or []) + list(REQUIRED_CONTROLS)))
    results: list[dict[str, Any]] = []
    for name in checked_names:
        candidates = [name]
        if "//" in name:
            candidates.append(name.split("//", 1)[0].strip())
        matches_by_path: dict[str, dict[str, Any]] = {}
        for candidate in candidates:
            for record in scripts.get(normalize_name(candidate), []):
                matches_by_path[record["path"]] = record
        matches = list(matches_by_path.values())
        status = (
            "MATCH"
            if len(matches) == 1 and matches[0]["has_nonempty_oracle"]
            else "MISSING"
            if len(matches) == 0
            else "AMBIGUOUS"
            if len(matches) > 1
            else "MISSING_OR_EMPTY_ORACLE"
        )
        results.append(
            {
                "card_name": name,
                "in_test_variant": name in variant_names,
                "status": status,
                "matches": matches,
            }
        )

    by_name = {row["card_name"]: row for row in results}
    control_status = {
        name: by_name.get(name, {}).get("status", "NOT_SCANNED")
        for name in REQUIRED_CONTROLS
    }
    missing = [row["card_name"] for row in results if row["status"] != "MATCH"]
    return {
        "release": PINNED_RELEASE,
        "commit": PINNED_COMMIT,
        "scan_type": "pinned-source card-script identity and nonempty Oracle-field presence only; not rules correctness",
        "card_root": str(card_root),
        "variant_file": str(variant_path),
        "variant_line_copy_count": sum(copy_counts.values()),
        "variant_unique_card_names": len(variant_names),
        "comparison_only_cards": extra_cards or [],
        "unique_names_checked": len(checked_names),
        "standard_script_files_scanned": script_count,
        "indexed_normalized_names": len(scripts),
        "match_count": sum(row["status"] == "MATCH" for row in results),
        "missing_or_invalid_count": len(missing),
        "missing_or_invalid_cards": missing,
        "required_control_status": control_status,
        "all_required_controls_pass": all(status == "MATCH" for status in control_status.values()),
        "passes_source_coverage_gate": not missing and all(
            status == "MATCH" for status in control_status.values()
        ),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", type=Path, required=True)
    parser.add_argument("--card-root", type=Path, required=True)
    parser.add_argument("--extra-card", action="append", default=[])
    parser.add_argument("--output", type=Path, default=Path("forge-card-script-coverage.json"))
    args = parser.parse_args()

    report = audit(args.variant, args.card_root, args.extra_card)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    summary = {
        key: report[key]
        for key in (
            "release",
            "commit",
            "variant_line_copy_count",
            "variant_unique_card_names",
            "comparison_only_cards",
            "unique_names_checked",
            "standard_script_files_scanned",
            "indexed_normalized_names",
            "match_count",
            "missing_or_invalid_count",
            "required_control_status",
            "passes_source_coverage_gate",
        )
    }
    print(json.dumps(summary, indent=2))
    if not report["passes_source_coverage_gate"]:
        print("Unmatched/invalid cards:", ", ".join(report["missing_or_invalid_cards"]))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
