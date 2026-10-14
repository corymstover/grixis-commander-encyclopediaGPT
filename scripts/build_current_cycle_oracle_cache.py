#!/usr/bin/env python3
"""Build a fresh canonical Oracle cache for every card name used by current-cycle decklists.

Network design:
- The expensive Scryfall bulk download is handled by refresh_scryfall_metadata.py.
- This script reuses that validated overlay for nearly all names.
- Only names absent from the overlay are resolved with Scryfall /cards/named exact lookup.
- The resulting cache is small, committed to GitHub, and is the preferred verification input
  for chat/container environments that cannot reach Scryfall directly.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECKLIST_DIR = ROOT / "refinement" / "decklists"
META_DIR = ROOT / "refinement" / "metadata_audit"
OVERLAY = META_DIR / "Current_Scryfall_Metadata_Overlay.csv"
OVERLAY_SUMMARY = META_DIR / "Current_Scryfall_Metadata_Audit_Summary.json"
OUT_JSONL = META_DIR / "Current_Cycle_Oracle_Cache.jsonl"
OUT_SUMMARY = META_DIR / "Current_Cycle_Oracle_Cache_Summary.json"
EXCEPTIONS = ROOT / "source-package" / "research" / "Project_Exceptions_Current_2026-10-12.csv"
UA = "GrixisCommanderEncyclopedia/1.0 (github.com/corymstover/grixis-commander-encyclopediaGPT)"
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
TRAILING_ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")
TRAILING_PRINTING_RE = re.compile(r"\s+\(([^()]*)\)\s+(\S+)(?:\s+\*[^*]+\*)?\s*$")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").casefold().replace("’", "'"))


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def parse_name(line: str) -> tuple[int, str] | None:
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    m = LINE_RE.match(line)
    if not m:
        return None
    qty = int(m.group(1))
    rest = m.group(2).strip()
    rest = TRAILING_ROLE_RE.sub("", rest).strip()
    rest = TRAILING_PRINTING_RE.sub("", rest).strip()
    return qty, rest


def http_json(url: str, attempts: int = 5) -> dict:
    retryable = {408, 425, 429, 500, 502, 503, 504}
    for attempt in range(1, attempts + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except urllib.error.HTTPError as exc:
            if exc.code not in retryable or attempt == attempts:
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            try:
                delay = float(retry_after) if retry_after else min(30.0, 2 ** (attempt - 1))
            except ValueError:
                delay = min(30.0, 2 ** (attempt - 1))
            time.sleep(max(0.1, min(60.0, delay)))
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt == attempts:
                raise
            time.sleep(min(30.0, 2 ** (attempt - 1)))
    raise RuntimeError(f"request retries exhausted: {url}")


def canonical_from_overlay(row: dict, generated_at: str, bulk_updated_at: str) -> dict:
    text = row.get("oracle_text", "") or ""
    return {
        "query_name": row.get("card_name_export", ""),
        "canonical_name": row.get("scryfall_name", "") or row.get("card_name_export", ""),
        "scryfall_id": row.get("scryfall_id", ""),
        "oracle_id": row.get("oracle_id", ""),
        "type_line": row.get("type_line", ""),
        "mana_cost": row.get("mana_cost", ""),
        "oracle_text": text,
        "oracle_text_sha256": row.get("oracle_text_sha256", "") or sha256_text(text),
        "color_identity": [x for x in (row.get("color_identity", "") or "").split(",") if x],
        "commander_legality": row.get("commander_legality", "unknown"),
        "released_at": row.get("released_at", ""),
        "scryfall_uri": f"https://scryfall.com/card/{row.get('scryfall_id','')}" if row.get("scryfall_id") else "",
        "source": "validated_scryfall_bulk_overlay",
        "source_generated_at_utc": generated_at,
        "bulk_updated_at": bulk_updated_at,
    }


def canonical_from_live(card: dict, generated_at: str) -> dict:
    faces = card.get("card_faces") or []
    text = card.get("oracle_text") or ""
    if not text and faces:
        text = "\n//\n".join(f.get("oracle_text", "") for f in faces if f.get("oracle_text"))
    mana_cost = card.get("mana_cost") or ""
    if not mana_cost and faces:
        mana_cost = " // ".join(f.get("mana_cost", "") for f in faces if f.get("mana_cost"))
    return {
        "query_name": card.get("name", ""),
        "canonical_name": card.get("name", ""),
        "scryfall_id": card.get("id", ""),
        "oracle_id": card.get("oracle_id", ""),
        "type_line": card.get("type_line", ""),
        "mana_cost": mana_cost,
        "oracle_text": text,
        "oracle_text_sha256": sha256_text(text),
        "color_identity": sorted(card.get("color_identity") or []),
        "commander_legality": (card.get("legalities") or {}).get("commander", "unknown"),
        "released_at": card.get("released_at", ""),
        "scryfall_uri": card.get("scryfall_uri", ""),
        "source": "live_scryfall_named_exact",
        "source_generated_at_utc": generated_at,
        "bulk_updated_at": "",
    }


def main() -> None:
    if not DECKLIST_DIR.is_dir():
        raise RuntimeError(f"missing decklist directory: {DECKLIST_DIR}")
    if not OVERLAY.is_file() or not OVERLAY_SUMMARY.is_file():
        raise RuntimeError("validated Scryfall overlay missing; run refresh_scryfall_metadata.py first")

    generated_at = datetime.now(timezone.utc).isoformat()
    overlay_summary = json.loads(OVERLAY_SUMMARY.read_text(encoding="utf-8"))
    bulk_updated_at = overlay_summary.get("bulk_updated_at", "")
    if not bulk_updated_at:
        raise RuntimeError("overlay summary missing bulk_updated_at")

    needed: dict[str, set[str]] = defaultdict(set)
    malformed: list[dict] = []
    decklist_files = sorted(DECKLIST_DIR.glob("*.txt"))
    for path in decklist_files:
        for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.strip():
                continue
            parsed = parse_name(line)
            if not parsed:
                malformed.append({"path": str(path.relative_to(ROOT)), "line": line_no, "text": line})
                continue
            _, name = parsed
            needed[norm(name)].add(name)

    exception_names = []
    if EXCEPTIONS.is_file():
        with EXCEPTIONS.open(newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                name = (row.get("card_name") or "").strip()
                if name:
                    needed[norm(name)].add(name)
                    exception_names.append(name)

    overlay_by_norm: dict[str, list[dict]] = defaultdict(list)
    with OVERLAY.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            for key in {norm(row.get("card_name_export", "")), norm(row.get("scryfall_name", ""))}:
                if key:
                    overlay_by_norm[key].append(row)

    records: dict[str, dict] = {}
    unresolved: list[dict] = []
    ambiguous_overlay: list[dict] = []
    live_lookups = 0

    for key in sorted(needed):
        names = sorted(needed[key])
        rows = overlay_by_norm.get(key, [])
        signatures = {
            (r.get("oracle_id", ""), r.get("oracle_text_sha256", ""), r.get("commander_legality", ""), r.get("color_identity", ""))
            for r in rows
            if r.get("oracle_id")
        }
        if rows and len(signatures) == 1:
            rec = canonical_from_overlay(rows[0], generated_at, bulk_updated_at)
            rec["query_name"] = names[0]
            records[key] = rec
            continue
        if rows and len(signatures) > 1:
            ambiguous_overlay.append({"names": names, "signatures": sorted(map(list, signatures))})

        query_name = names[0]
        url = "https://api.scryfall.com/cards/named?exact=" + urllib.parse.quote(query_name)
        try:
            card = http_json(url)
            live_lookups += 1
            if card.get("object") == "error":
                raise RuntimeError(card.get("details", "Scryfall error"))
            rec = canonical_from_live(card, generated_at)
            rec["query_name"] = query_name
            records[key] = rec
            time.sleep(0.11)
        except Exception as exc:
            unresolved.append({"name": query_name, "error": f"{type(exc).__name__}: {exc}"})

    ordered = [records[k] for k in sorted(records, key=lambda k: records[k]["canonical_name"].casefold())]
    META_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSONL.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in ordered), encoding="utf-8")

    summary = {
        "generated_at_utc": generated_at,
        "overlay_generated_at_utc": overlay_summary.get("generated_at_utc"),
        "bulk_updated_at": bulk_updated_at,
        "decklist_file_count": len(decklist_files),
        "distinct_names_requested": len(needed),
        "records_written": len(ordered),
        "overlay_hits": len(ordered) - live_lookups,
        "live_named_exact_lookups": live_lookups,
        "exception_names_included": sorted(set(exception_names)),
        "malformed_decklist_lines": malformed,
        "ambiguous_overlay_entries_rechecked_live": ambiguous_overlay,
        "unresolved": unresolved,
        "cache_sha256": hashlib.sha256(OUT_JSONL.read_bytes()).hexdigest(),
        "overall_result": "PASS" if len(ordered) == len(needed) and not unresolved and not malformed else "BLOCKED",
        "design_note": "Preferred verification cache for chat/container runs. Direct Scryfall access from chat is not required when this cache is fresh and complete.",
    }
    OUT_SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if summary["overall_result"] != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
