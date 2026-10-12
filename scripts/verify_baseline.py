#!/usr/bin/env python3
"""Verify the frozen Grixis CSV/TXT decklist mirror against its hash manifest."""
import csv
import hashlib
import io
import re
import sys
import tarfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "source-package" / "GrixisFINAL_62Decks_CSV_TXT_2026-10-12.tar.gz"
MANIFEST = ROOT / "source-package" / "Grixis_Independent_Deck_Hash_Manifest_2026-10-12.csv"
TXT_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s+\(([^()]*)\)\s+(\S+)\s+(?:\*[^*]+\*\s+)?\[([^\]]*)\]\s*$")
BASICS = {"plains", "island", "swamp", "mountain", "forest", "wastes",
          "snow-covered plains", "snow-covered island", "snow-covered swamp",
          "snow-covered mountain", "snow-covered forest"}


def norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.casefold().replace("’", "'"))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not ARCHIVE.is_file() or not MANIFEST.is_file():
        fail("baseline archive or hash manifest is missing")
    with MANIFEST.open(newline="", encoding="utf-8-sig") as f:
        expected = {r["deck_id"]: r for r in csv.DictReader(f)}
    with tarfile.open(ARCHIVE, "r:gz") as tf:
        members = {m.name: m for m in tf.getmembers() if m.isfile()}
        csv_paths = sorted(p for p in members if p.startswith("CSV/") and p.endswith(".csv"))
        txt_paths = sorted(p for p in members if p.startswith("TXT/") and p.endswith(".txt"))
        if len(csv_paths) != 62 or len(txt_paths) != 62 or len(members) != 124:
            fail(f"expected 124 files (62 CSV + 62 TXT); found {len(members)} total, {len(csv_paths)} CSV, {len(txt_paths)} TXT")
        seen = set()
        total_main = total_companion = 0
        for cp in csv_paths:
            deck_id = Path(cp).stem
            tp = f"TXT/{deck_id}.txt"
            if tp not in members:
                fail(f"missing TXT partner for {deck_id}")
            if deck_id not in expected:
                fail(f"deck {deck_id} absent from hash manifest")
            cb = tf.extractfile(members[cp]).read()
            tb = tf.extractfile(members[tp]).read()
            row = expected[deck_id]
            if sha256(cb) != row["csv_sha256"] or sha256(tb) != row["txt_sha256"]:
                fail(f"raw SHA-256 mismatch for {deck_id}")
            crows = list(csv.reader(io.StringIO(cb.decode("utf-8-sig"))))
            csv_counts = Counter()
            csv_qty = 0
            for cr in crows:
                if len(cr) < 2:
                    fail(f"malformed CSV row in {deck_id}: {cr}")
                try:
                    q = int(cr[0])
                except ValueError:
                    fail(f"invalid CSV quantity in {deck_id}: {cr}")
                if q < 1:
                    fail(f"non-positive quantity in {deck_id}: {cr}")
                csv_counts[norm(cr[1].strip())] += q
                csv_qty += q
            txt_counts = Counter()
            txt_qty = companions = 0
            for line in tb.decode("utf-8-sig").splitlines():
                if not line.strip():
                    continue
                m = TXT_RE.match(line)
                if not m:
                    fail(f"malformed TXT row in {deck_id}: {line}")
                q, name, _set, _collector, role = m.groups()
                q = int(q)
                txt_counts[norm(name.strip())] += q
                txt_qty += q
                if "Companion" in role:
                    companions += q
            if csv_counts != txt_counts:
                fail(f"CSV/TXT card quantities disagree for {deck_id}")
            main_count = txt_qty - companions
            if main_count != 100:
                fail(f"{deck_id} has {main_count} main-deck-plus-commander cards")
            for name, q in csv_counts.items():
                if name in {norm(x) for x in BASICS}:
                    continue
                limit = 9 if name == norm("Nazgûl") else 1
                if q > limit:
                    fail(f"singleton/copy-rule violation in {deck_id}: {name} has {q}, limit {limit}")
            if csv_qty != int(row["csv_quantity"]) or txt_qty != int(row["txt_quantity"]):
                fail(f"quantity metadata mismatch in manifest for {deck_id}")
            seen.add(deck_id)
            total_main += main_count
            total_companion += companions
    if seen != set(expected):
        fail(f"manifest/deck mismatch; missing from archive={sorted(set(expected)-seen)}; missing from manifest={sorted(seen-set(expected))}")
    if len(seen) != 62 or total_main != 6200 or total_companion != 1:
        fail(f"unexpected totals: decks={len(seen)}, main={total_main}, companions={total_companion}")
    print("PASS: 62 decks; 124 files; every CSV/TXT SHA-256 matches; 62 quantity reconciliations; 62 exact 100-card counts; 62 singleton/copy checks; 6,200 main-deck-plus-commander cards; 1 separate companion.")


if __name__ == "__main__":
    main()
