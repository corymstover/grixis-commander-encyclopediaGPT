#!/usr/bin/env python3
"""Verify the isolated Abaddon Aurora Phoenix test variant.

This checks list integrity only. It does not simulate gameplay or approve a swap.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_ARCHIVE = ROOT / "source-package" / "GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
MANIFEST_PATH = ROOT / "source-package" / "Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv"
VARIANT_PATH = ROOT / "refinement" / "variants" / "Abaddon_Aurora_Phoenix_Test_Variant_v1.txt"

EXPECTED_ARCHIVE_SHA256 = "f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20"
EXPECTED_BASELINE_TXT_SHA256 = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
EXPECTED_VARIANT_RAW_SHA256 = "1ad0c11d1f6a28a54f89c378428af491c6ff9929f42813692c375fb60771503b"
EXPECTED_BASELINE_NORMALIZED_SHA256 = "4af2214a2d4055f4a1a5e91dcbe50a1193e3ee27070a0d9cb1208a17d994eb53"
EXPECTED_VARIANT_NORMALIZED_SHA256 = "fbc57b9eb9fcf14bd28dc3f59a73486eb78c6dc097b0102cde5178e7d5c8b862"

BASIC_LANDS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_membership_hash(cards: Counter[str]) -> str:
    body = "\n".join(
        f"{quantity}x {name}"
        for name, quantity in sorted(cards.items(), key=lambda pair: pair[0].casefold())
    ) + "\n"
    return sha256(body.encode("utf-8"))


def read_variant(data: bytes) -> tuple[Counter[str], int, list[str]]:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"Variant is not valid UTF-8: {exc}") from exc

    cards: Counter[str] = Counter()
    commander_markers = 0
    errors: list[str] = []
    for line_number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        match = re.fullmatch(r"(\d+)x\s+(.+)", line)
        if not match:
            errors.append(f"Line {line_number}: invalid quantity/name format: {line!r}")
            continue
        quantity = int(match.group(1))
        name = match.group(2).strip()
        if quantity <= 0:
            errors.append(f"Line {line_number}: nonpositive quantity")
        if "[Commander]" in name:
            commander_markers += 1
            if name != "Abaddon the Despoiler [Commander]":
                errors.append(f"Line {line_number}: unexpected commander marker: {name}")
            name = name.removesuffix(" [Commander]").strip()
        if not name:
            errors.append(f"Line {line_number}: empty card name")
        cards[name] += quantity
    return cards, commander_markers, errors


def main() -> int:
    problems: list[str] = []

    archive_bytes = BASELINE_ARCHIVE.read_bytes()
    archive_hash = sha256(archive_bytes)
    if archive_hash != EXPECTED_ARCHIVE_SHA256:
        problems.append(f"Baseline archive SHA-256 mismatch: {archive_hash}")

    with MANIFEST_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        manifest_rows = list(csv.DictReader(handle))
    manifest_row = next((r for r in manifest_rows if r.get("deck_id") == "Abaddon_the_Despoiler"), None)
    if manifest_row is None:
        problems.append("Abaddon row missing from the independent deck hash manifest")
        expected_csv_hash = ""
        expected_txt_hash = EXPECTED_BASELINE_TXT_SHA256
    else:
        expected_csv_hash = manifest_row.get("csv_sha256", "")
        expected_txt_hash = manifest_row.get("txt_sha256", "")
        if expected_txt_hash != EXPECTED_BASELINE_TXT_SHA256:
            problems.append("Manifest's Abaddon TXT hash differs from the pinned baseline hash")

    try:
        with tarfile.open(BASELINE_ARCHIVE, "r:gz") as archive:
            members = archive.getmembers()
            csv_matches = [m for m in members if m.isfile() and m.name.endswith("/CSV/Abaddon_the_Despoiler.csv")]
            if not csv_matches:
                # The compact archive's top-level layout may be CSV/ and TXT/.
                csv_matches = [m for m in members if m.isfile() and m.name.endswith("CSV/Abaddon_the_Despoiler.csv")]
            txt_matches = [m for m in members if m.isfile() and m.name.endswith("/TXT/Abaddon_the_Despoiler.txt")]
            if not txt_matches:
                txt_matches = [m for m in members if m.isfile() and m.name.endswith("TXT/Abaddon_the_Despoiler.txt")]
            if len(csv_matches) != 1 or len(txt_matches) != 1:
                raise ValueError(f"Expected one CSV and one TXT for Abaddon; found {len(csv_matches)} CSV and {len(txt_matches)} TXT")
            csv_file = archive.extractfile(csv_matches[0])
            txt_file = archive.extractfile(txt_matches[0])
            if csv_file is None or txt_file is None:
                raise ValueError("Could not read Abaddon baseline members")
            baseline_csv_bytes = csv_file.read()
            baseline_txt_bytes = txt_file.read()
    except (tarfile.TarError, OSError, ValueError) as exc:
        problems.append(f"Could not read authoritative baseline archive: {exc}")
        baseline_csv_bytes = b""
        baseline_txt_bytes = b""

    if not baseline_txt_bytes:
        problems.append("Baseline Abaddon TXT member is empty")
    elif sha256(baseline_txt_bytes) != EXPECTED_BASELINE_TXT_SHA256:
        problems.append(f"Baseline TXT SHA-256 mismatch: {sha256(baseline_txt_bytes)}")

    if expected_csv_hash and baseline_csv_bytes and sha256(baseline_csv_bytes) != expected_csv_hash:
        problems.append(f"Baseline CSV SHA-256 mismatch: {sha256(baseline_csv_bytes)}")

    baseline_cards: Counter[str] = Counter()
    try:
        reader = csv.reader(io.StringIO(baseline_csv_bytes.decode("utf-8-sig")))
        for row_number, row in enumerate(reader, 1):
            if not row:
                continue
            if len(row) < 2:
                raise ValueError(f"CSV row {row_number} has fewer than two fields")
            quantity = int(row[0])
            name = row[1].strip()
            if quantity <= 0 or not name:
                raise ValueError(f"CSV row {row_number} has invalid quantity/name")
            baseline_cards[name] += quantity
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        problems.append(f"Cannot parse baseline CSV: {exc}")

    variant_bytes = VARIANT_PATH.read_bytes()
    variant_hash = sha256(variant_bytes)
    if variant_hash != EXPECTED_VARIANT_RAW_SHA256:
        problems.append(f"Variant raw SHA-256 mismatch: {variant_hash}")

    try:
        variant_cards, commander_markers, variant_errors = read_variant(variant_bytes)
        problems.extend(variant_errors)
    except ValueError as exc:
        problems.append(str(exc))
        variant_cards, commander_markers = Counter(), 0

    baseline_total = sum(baseline_cards.values())
    variant_total = sum(variant_cards.values())
    if baseline_total != 100:
        problems.append(f"Baseline list has {baseline_total} card copies, not 100")
    if variant_total != 100:
        problems.append(f"Variant has {variant_total} card copies, not 100")
    if baseline_cards.get("Abaddon the Despoiler", 0) != 1:
        problems.append("Baseline must contain exactly one Abaddon the Despoiler")
    if variant_cards.get("Abaddon the Despoiler", 0) != 1 or commander_markers != 1:
        problems.append("Variant must have one Abaddon commander, marked exactly once")
    if len(variant_cards) != 94:
        problems.append(f"Expected 94 distinct variant names; found {len(variant_cards)}")

    duplicates = {
        name: quantity
        for name, quantity in variant_cards.items()
        if quantity > 1 and name not in BASIC_LANDS
    }
    if duplicates:
        problems.append(f"Variant has unexpected duplicate nonbasic cards: {duplicates}")

    removed = baseline_cards - variant_cards
    added = variant_cards - baseline_cards
    if removed != Counter({"Mind's Desire": 1}):
        problems.append(f"Variant must cut only Mind's Desire; actual cuts: {dict(removed)}")
    if added != Counter({"Aurora Phoenix": 1}):
        problems.append(f"Variant must add only Aurora Phoenix; actual adds: {dict(added)}")

    baseline_normalized = normalized_membership_hash(baseline_cards)
    variant_normalized = normalized_membership_hash(variant_cards)
    if baseline_normalized != EXPECTED_BASELINE_NORMALIZED_SHA256:
        problems.append(f"Normalized baseline hash mismatch: {baseline_normalized}")
    if variant_normalized != EXPECTED_VARIANT_NORMALIZED_SHA256:
        problems.append(f"Normalized variant hash mismatch: {variant_normalized}")

    result = {
        "status": "PASS" if not problems else "FAIL",
        "check_type": "decklist integrity only; no gameplay testing",
        "baseline_archive_sha256": archive_hash,
        "baseline_txt_sha256": sha256(baseline_txt_bytes) if baseline_txt_bytes else None,
        "baseline_csv_sha256": sha256(baseline_csv_bytes) if baseline_csv_bytes else None,
        "variant_raw_sha256": variant_hash,
        "baseline_card_count": baseline_total,
        "variant_card_count": variant_total,
        "baseline_distinct_names": len(baseline_cards),
        "variant_distinct_names": len(variant_cards),
        "removed": dict(removed),
        "added": dict(added),
        "baseline_normalized_membership_sha256": baseline_normalized,
        "variant_normalized_membership_sha256": variant_normalized,
        "problems": problems,
    }
    print(json.dumps(result, indent=2))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
