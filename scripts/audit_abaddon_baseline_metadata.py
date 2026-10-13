#!/usr/bin/env python3
"""Independent static audit of Abaddon baseline membership against the pinned metadata overlay.

This script deliberately does not change any decklist, infer card rules from card names,
or certify strategic optimality. It joins exact card names to the frozen 2026-10-12
Scryfall metadata overlay and verifies list counts/identity/legality/exception labels.
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
ARCHIVE = ROOT / "source-package" / "GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
OVERLAY = ROOT / "refinement" / "metadata_audit" / "Current_Scryfall_Metadata_Overlay_2026-10-12.csv"
EXCEPTIONS = ROOT / "source-package" / "research" / "current-2026-10-12" / "project_exceptions_current_v8_1_4.csv"
DECK_ID = "Abaddon_the_Despoiler"
BASELINE_SHA256 = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
ARCHIVE_SHA256 = "f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20"
REGISTERED_EXCEPTIONS = {
    "lutri, the spellchaser",
    "trade secrets",
    "yawgmoth's bargain",
    "the madcap jester",
    "dragon's smile",
    "tresserhorn's lord, returned",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()


def read_abaddon_list() -> tuple[bytes, list[dict]]:
    archive_bytes = ARCHIVE.read_bytes()
    if sha256(archive_bytes) != ARCHIVE_SHA256:
        raise ValueError(f"Compact archive hash mismatch: {sha256(archive_bytes)}")
    with tarfile.open(ARCHIVE, "r:gz") as tar:
        members = [m for m in tar.getmembers()
                   if m.isfile() and m.name.replace("\\", "/").endswith("TXT/Abaddon_the_Despoiler.txt")]
        if len(members) != 1:
            raise ValueError(f"Expected one Abaddon TXT member; found {len(members)}")
        fd = tar.extractfile(members[0])
        if fd is None:
            raise ValueError("Unable to extract Abaddon TXT")
        raw = fd.read()
    if sha256(raw) != BASELINE_SHA256:
        raise ValueError(f"Abaddon TXT hash mismatch: {sha256(raw)}")
    parsed = []
    for n, line in enumerate(raw.decode("utf-8-sig").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        m = re.fullmatch(r"(\d+)x\s+(.+)", line)
        if not m:
            raise ValueError(f"Line {n}: invalid quantity/name line: {line!r}")
        qty = int(m.group(1))
        body = m.group(2).strip()
        role_m = re.search(r"\s+\[([^\]]+)\]\s*$", body)
        role = role_m.group(1).strip() if role_m else ""
        if role_m:
            body = body[:role_m.start()].strip()
        # Strip export printing metadata only after the role tag.
        name = re.sub(r"\s+\([^)]+\)\s+\S+\s*$", "", body).strip()
        if qty < 1 or not name:
            raise ValueError(f"Line {n}: invalid quantity or card name")
        parsed.append({"line": n, "quantity": qty, "name": name, "role_tag": role})
    return raw, parsed


def load_overlay(path: Path) -> tuple[dict[str, dict], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("Scryfall metadata overlay is empty")
    fieldnames = list(rows[0].keys())
    name_field = next((f for f in ("card_name", "name", "name_in_deck", "deck_card_name") if f in fieldnames), None)
    if not name_field:
        raise ValueError(f"Could not find card-name field in metadata overlay; fields={fieldnames}")
    by_name = {}
    for row in rows:
        name = norm(row.get(name_field, ""))
        if name:
            by_name.setdefault(name, []).append(row)
    return by_name, fieldnames


def get_value(row: dict, candidates: tuple[str, ...]) -> str:
    for key in candidates:
        if key in row and row[key] is not None and str(row[key]).strip() != "":
            return str(row[key]).strip()
    return ""


def audit() -> dict:
    raw, cards = read_abaddon_list()
    counts = Counter(x["name"] for x in cards for _ in range(x["quantity"]))
    if sum(counts.values()) != 100:
        raise ValueError(f"Expected exactly 100 cards including commander, got {sum(counts.values())}")
    commander_rows = [x for x in cards if x["role_tag"].casefold().startswith("commander")]
    if len(commander_rows) != 1 or commander_rows[0]["name"] != "Abaddon the Despoiler" or commander_rows[0]["quantity"] != 1:
        raise ValueError("Commander marker/count is not exactly one Abaddon the Despoiler")
    non_singletons = {name: quantity for name, quantity in counts.items()
                      if quantity > 1 and name.casefold() not in {"island", "swamp", "mountain"}}
    if non_singletons:
        raise ValueError(f"Singleton/copy rule failures: {non_singletons}")
    overlay, fields = load_overlay(OVERLAY)
    audit_rows = []
    missing = []
    ambiguous = []
    mismatches = []
    for name, quantity in sorted(counts.items(), key=lambda x: x[0].casefold()):
        matches = overlay.get(norm(name), [])
        if len(matches) == 0:
            missing.append(name)
            audit_rows.append({"name": name, "quantity": quantity, "status": "MISSING_FROM_OVERLAY"})
            continue
        if len(matches) > 1:
            ambiguous.append({"name": name, "matches": len(matches)})
            audit_rows.append({"name": name, "quantity": quantity, "status": "AMBIGUOUS_OVERLAY_MATCH"})
            continue
        row = matches[0]
        oracle_id = get_value(row, ("oracle_id", "oracleId", "oracle_id_current"))
        identity = get_value(row, ("color_identity", "colorIdentity", "color_identity_current"))
        legality = get_value(row, ("commander_legality", "legalities_commander", "commander_status", "commander"))
        oracle_text = get_value(row, ("oracle_text", "oracle_text_current", "oracle"))
        card_type = get_value(row, ("type_line", "type_line_current", "type"))
        collector = get_value(row, ("collector_number", "collector_number_current", "number"))
        set_code = get_value(row, ("set", "set_code", "set_code_current"))
        exception_status = "NONE"
        if norm(name) in REGISTERED_EXCEPTIONS:
            exception_status = "REGISTERED_EXCEPTION — verify project deck assignment separately"
        problems = []
        if not oracle_id:
            problems.append("MISSING_ORACLE_ID")
        if not oracle_text:
            problems.append("MISSING_ORACLE_TEXT")
        if not legality:
            problems.append("MISSING_COMMANDER_LEGALITY_FIELD")
        elif legality.casefold() not in {"legal", "not_legal", "banned", "restricted", "legal with exception"}:
            problems.append("UNRECOGNIZED_COMMANDER_LEGALITY_VALUE")
        if problems:
            mismatches.append({"name": name, "problems": problems})
        audit_rows.append({
            "name": name, "quantity": quantity, "role_tag": next(x["role_tag"] for x in cards if x["name"] == name),
            "oracle_id": oracle_id, "type_line": card_type, "color_identity": identity,
            "commander_legality": legality, "set": set_code, "collector_number": collector,
            "project_exception_registry_status": exception_status,
            "oracle_text_present": bool(oracle_text), "status": "REVIEW" if problems else "METADATA_FIELDS_PRESENT",
            "field_problems": problems,
        })
    if missing or ambiguous or mismatches:
        overall = "FAIL_OR_REVIEW"
    else:
        overall = "STRUCTURAL_AND_METADATA_JOIN_PASS — strategy/rules certification remains separate"
    return {
        "deck_id": DECK_ID,
        "baseline_snapshot": "2026-10-12",
        "baseline_txt_sha256": sha256(raw),
        "compact_archive_sha256": sha256(ARCHIVE.read_bytes()),
        "total_cards_including_commander": sum(counts.values()),
        "unique_card_names": len(counts),
        "commander": commander_rows[0]["name"],
        "commander_quantity": commander_rows[0]["quantity"],
        "nonbasic_singleton_failures": non_singletons,
        "overlay_path": str(OVERLAY.relative_to(ROOT)),
        "overlay_fieldnames": fields,
        "overlay_exact_name_match_status": overall,
        "missing_from_overlay": missing,
        "ambiguous_overlay_matches": ambiguous,
        "metadata_field_issues": mismatches,
        "cards": audit_rows,
        "limitations": [
            "Metadata overlay is a dated snapshot; a current final legality checkpoint must be run before final approval.",
            "Name matching is not the same as full card-rules verification; split/DFC/alternate-name edge cases require explicit mapping if encountered.",
            "Project exception labels here are global guardrails, not evidence that a particular named exception is present in Abaddon.",
            "This script does not score strategy, establish simulator correctness, or authorize any card change.",
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
        fields = ["name", "quantity", "role_tag", "oracle_id", "type_line", "color_identity",
                  "commander_legality", "set", "collector_number", "project_exception_registry_status",
                  "oracle_text_present", "status", "field_problems"]
        with args.csv_output.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in result["cards"]:
                flat = dict(row)
                flat["field_problems"] = ";".join(flat.get("field_problems", []))
                writer.writerow({k: flat.get(k, "") for k in fields})
    if not args.json_output and not args.csv_output:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
