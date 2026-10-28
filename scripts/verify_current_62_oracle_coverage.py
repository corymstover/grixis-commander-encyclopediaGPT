#!/usr/bin/env python3
"""Audit the exact 62 approved decklists against dated Scryfall records.

The October 28 cache was built before the last Tresserhorn additions reached its
input scan. Keep those three source-checked late records in a small supplement
until the next full cache refresh. Neither a record match nor this script is an
Oracle-rulings engine, playtest, or formal M6/M8 certification.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from build_current_cycle_oracle_cache import norm, parse_name

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "refinement" / "metadata_audit"
CACHE = META / "Current_Cycle_Oracle_Cache.jsonl"
SUMMARY = META / "Current_Cycle_Oracle_Cache_Summary.json"
SUPPLEMENT = META / "Current_Cycle_Oracle_Cache_Supplement_2026-10-28.jsonl"
REGISTRY = ROOT / "state" / "current_deck_overrides.json"
EXCEPTIONS = ROOT / "source-package" / "research" / "Project_Exceptions_Current_2026-10-12.csv"


def records(path: Path) -> dict[str, dict]:
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        key = norm(record["query_name"])
        if key in result:
            raise ValueError(f"duplicate normalized Oracle key in {path.name}: {key}")
        if hashlib.sha256(record["oracle_text"].encode("utf-8")).hexdigest() != record["oracle_text_sha256"]:
            raise ValueError(f"Oracle text hash mismatch: {record['query_name']}")
        result[key] = record
    return result


def audit() -> dict:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    if hashlib.sha256(CACHE.read_bytes()).hexdigest() != summary["cache_sha256"]:
        raise ValueError("base Oracle cache has changed without summary update")
    base = records(CACHE)
    extra = records(SUPPLEMENT)
    if any(key in base for key in extra):
        raise ValueError("supplement overlaps base cache; consolidate after refresh")
    combined = base | extra

    with EXCEPTIONS.open(newline="", encoding="utf-8-sig") as f:
        allowed = {
            (row["deck_id"], norm(row["card_name"]))
            for row in csv.DictReader(f)
            if "copy" not in row["exception_type"].lower()
        }
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))["decks"]
    if len(registry) != 62:
        raise ValueError(f"expected 62 locked registry entries; found {len(registry)}")

    checked = 0
    companions = 0
    exception_hits = set()
    supplement_hits = Counter()
    for deck_id, info in registry.items():
        if info.get("approval_status") != "APPROVED" or info.get("lock_status") != "LOCKED":
            raise ValueError(f"unapproved/unlocked deck: {deck_id}")
        raw = (ROOT / info["approved_list_artifact"]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != info["approved_list_sha256"]:
            raise ValueError(f"registry SHA does not match exact approved list: {deck_id}")
        deck_cards = deck_companions = 0
        for line in raw.decode("utf-8-sig").splitlines():
            if not line.strip():
                continue
            parsed = parse_name(line)
            if parsed is None:
                raise ValueError(f"unparseable line: {deck_id}: {line}")
            quantity, name = parsed
            if quantity < 1:
                raise ValueError(f"invalid quantity: {deck_id}: {line}")
            key = norm(name)
            record = combined.get(key)
            if not record:
                raise ValueError(f"Oracle cache gap: {deck_id}: {name}")
            if not set(record["color_identity"]).issubset({"U", "B", "R"}):
                raise ValueError(f"color identity outside Grixis: {deck_id}: {name}")
            if record["commander_legality"] != "legal":
                if (deck_id, key) not in allowed:
                    raise ValueError(f"unapproved official legality exception: {deck_id}: {name}")
                exception_hits.add((deck_id, key))
            if key in extra:
                supplement_hits[name] += quantity
            if "[Companion]" in line:
                deck_companions += quantity
            else:
                deck_cards += quantity
        if deck_cards != 100:
            raise ValueError(f"incorrect playable count: {deck_id}: {deck_cards}")
        checked += deck_cards
        companions += deck_companions
    if (checked, companions) != (6200, 1):
        raise ValueError(f"unexpected totals: {checked} playable, {companions} companions")
    if set(supplement_hits) != {"Genesis Chamber", "Sengir Autocrat", "The Meathook Massacre"}:
        raise ValueError(f"supplement must correspond to late Tresserhorn additions: {supplement_hits}")
    if len(exception_hits) != 6:
        raise ValueError(f"expected six explicit nonlegal card/deck entries, got {exception_hits}")
    return {
        "status": "PASS_BOUNDED_SOURCE_COVERAGE_NOT_M6_OR_M8_CERTIFICATION",
        "exact_locked_decks": len(registry),
        "playable_cards": checked,
        "companions": companions,
        "base_cache_names": len(base),
        "supplement_names": sorted(supplement_hits),
        "nonlegal_entries_with_explicit_project_exception": len(exception_hits),
        "new_unresolved_names": 0,
        "out_of_grixis_color_identity": 0,
        "cache_bulk_updated_at": summary["bulk_updated_at"],
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
