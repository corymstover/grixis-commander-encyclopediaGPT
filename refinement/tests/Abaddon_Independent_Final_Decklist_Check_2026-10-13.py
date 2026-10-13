#!/usr/bin/env python3
"""Independent read-only integrity check for the frozen Abaddon decklist.

Usage:
  python refinement/tests/Abaddon_Independent_Final_Decklist_Check_2026-10-13.py path/to/GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz

This script never modifies the archive or baseline. It verifies the archive digest,
locates Abaddon's canonical CSV/TXT pair, compares quantities, counts 100 cards,
checks one commander and singleton rules (with basic-land exceptions), and emits
the exact TXT hash. It deliberately does not certify live Oracle/rulings.
"""
from __future__ import annotations

import csv
import hashlib
import io
import sys
import tarfile
from collections import Counter
from pathlib import Path

EXPECTED_ARCHIVE_SHA256 = "f2f46436c3514ecf8412d1fe1f9926919d8d1a3d7a2f938ffee7efce073b2b20"
EXPECTED_TXT_SHA256 = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
CSV_NAME = "Abaddon_the_Despoiler.csv"
TXT_NAME = "Abaddon_the_Despoiler.txt"
BASIC_LANDS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_csv(data: bytes) -> Counter[str]:
    text = data.decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(text, newline="")))
    header_idx = next((i for i, row in enumerate(rows) if row and any("name" in c.lower() for c in row)), None)
    if header_idx is None:
        raise ValueError("No card-name header found in CSV.")
    header = [v.strip().lower() for v in rows[header_idx]]
    name_i = next((i for i, x in enumerate(header) if x in {"name", "card name", "card_name"}), None)
    qty_i = next((i for i, x in enumerate(header) if x in {"quantity", "qty", "count"}), None)
    if name_i is None or qty_i is None:
        raise ValueError(f"Could not resolve name/quantity columns: {header}")
    counts: Counter[str] = Counter()
    for row in rows[header_idx + 1:]:
        if not row or len(row) <= max(name_i, qty_i):
            continue
        name, qty = row[name_i].strip(), row[qty_i].strip()
        if not name:
            continue
        try:
            n = int(qty)
        except ValueError:
            continue
        if n > 0:
            counts[name] += n
    if not counts:
        raise ValueError("CSV parsed to zero cards.")
    return counts


def parse_txt(data: bytes) -> tuple[Counter[str], int]:
    text = data.decode("utf-8-sig")
    counts: Counter[str] = Counter()
    commander_count = 0
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("//") or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            continue
        try:
            qty = int(parts[0].rstrip("xX"))
        except ValueError:
            continue
        card_field = parts[1].strip()
        # Remove role tags commonly appended by the export while retaining the card face name.
        card_name = card_field.split(" [", 1)[0].strip()
        if not card_name:
            continue
        if "[Commander]" in card_name:
            commander_count += qty
            card_name = card_name.replace("[Commander]", "").strip()
        # Remove // comments only when visually separated by the common export delimiter.
        counts[card_name] += qty
    return counts, commander_count


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python Abaddon_Independent_Final_Decklist_Check_2026-10-13.py <archive.tar.gz>", file=sys.stderr)
        return 2
    archive_path = Path(sys.argv[1])
    archive = archive_path.read_bytes()
    archive_sha = digest(archive)
    print(f"archive_sha256={archive_sha}")
    if archive_sha != EXPECTED_ARCHIVE_SHA256:
        raise SystemExit("FAIL: compact archive hash does not match frozen package.")

    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as tf:
        members = {Path(m.name).name: m for m in tf.getmembers() if m.isfile()}
        if CSV_NAME not in members or TXT_NAME not in members:
            raise SystemExit(f"FAIL: expected pair not found; CSV={CSV_NAME in members}, TXT={TXT_NAME in members}")
        csv_bytes = tf.extractfile(members[CSV_NAME]).read()
        txt_bytes = tf.extractfile(members[TXT_NAME]).read()

    csv_counts = parse_csv(csv_bytes)
    txt_counts, commander_count = parse_txt(txt_bytes)
    csv_hash, txt_hash = digest(csv_bytes), digest(txt_bytes)
    print(f"csv_sha256={csv_hash}")
    print(f"txt_sha256={txt_hash}")
    print(f"csv_cards={sum(csv_counts.values())}")
    print(f"txt_cards={sum(txt_counts.values())}")
    print(f"csv_unique_names={len(csv_counts)}")
    print(f"txt_unique_names={len(txt_counts)}")
    print(f"commander_markers={commander_count}")
    if txt_hash != EXPECTED_TXT_SHA256:
        raise SystemExit("FAIL: Abaddon TXT hash does not match the frozen baseline.")
    if csv_counts != txt_counts:
        print("CSV/TXT quantity differences:")
        for name in sorted(set(csv_counts) | set(txt_counts)):
            if csv_counts[name] != txt_counts[name]:
                print(f"  {name}: CSV={csv_counts[name]} TXT={txt_counts[name]}")
        raise SystemExit("FAIL: CSV/TXT card quantities do not reconcile.")
    if sum(txt_counts.values()) != 100:
        raise SystemExit(f"FAIL: expected 100 cards, found {sum(txt_counts.values())}.")
    if commander_count != 1:
        raise SystemExit(f"FAIL: expected exactly 1 commander marker, found {commander_count}.")
    duplicates = {n: q for n, q in txt_counts.items() if q > 1 and n not in BASIC_LANDS}
    if duplicates:
        raise SystemExit(f"FAIL: nonbasic duplicate(s): {duplicates}")
    print("csv_txt_reconciliation=PASS")
    print("100_card_count=PASS")
    print("singleton_copy_check=PASS")
    print("frozen_baseline=UNCHANGED")
    print("NOTE: no claim made about live Oracle identity, legality, rulings, or strategy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
