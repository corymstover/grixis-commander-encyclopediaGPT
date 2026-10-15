#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from build_current_cycle_oracle_cache import http_json, canonical_from_live

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "refinement/decklists/Solkanar_the_Swamp_King_Approval_Ready_2026-10-15.txt"
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
SUMMARY = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache_Summary.json"
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
ROLE_RE = re.compile(r"\s+\[[^\]]+\]\s*$")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").casefold().replace("’", "'"))


def candidate_names() -> list[str]:
    names = []
    for line in CANDIDATE.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        m = LINE_RE.match(line)
        if not m:
            raise RuntimeError(f"Malformed candidate line: {line}")
        names.append(ROLE_RE.sub("", m.group(2)).strip())
    return sorted(set(names), key=str.casefold)


def load_records() -> tuple[list[dict], dict[str, dict]]:
    rows, by = [], {}
    for line in CACHE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        rows.append(r)
        for key in {r.get("query_name"), r.get("canonical_name")}:
            if key:
                by[norm(key)] = r
    return rows, by


def live_card(name: str) -> dict:
    if name == "Starscape Cleric":
        # Resolve the documented BLB #116 card/token name collision to the exact source printing.
        return http_json("https://api.scryfall.com/cards/blb/116", attempts=5)
    url = "https://api.scryfall.com/cards/named?exact=" + urllib.parse.quote(name)
    return http_json(url, attempts=5)


def main() -> None:
    if not CACHE.exists() or not SUMMARY.exists():
        raise RuntimeError("Current-cycle Oracle cache missing")
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    if summary.get("overall_result") != "PASS" or summary.get("unresolved"):
        raise RuntimeError("Existing current-cycle cache is not a clean PASS")
    generated = datetime.fromisoformat(summary["generated_at_utc"].replace("Z", "+00:00"))
    age_hours = (datetime.now(timezone.utc) - generated.astimezone(timezone.utc)).total_seconds() / 3600
    if age_hours > 24:
        raise RuntimeError(f"Existing cache is older than targeted-refresh allowance: {age_hours:.2f}h")

    rows, by = load_records()
    names = candidate_names()
    # Force-refresh Starscape Cleric even if a stale normalized record exists.
    missing = [n for n in names if norm(n) not in by or n == "Starscape Cleric"]
    now = datetime.now(timezone.utc).isoformat()
    added = []
    for name in missing:
        card = live_card(name)
        if card.get("object") == "error":
            raise RuntimeError(f"Scryfall unresolved: {name}: {card.get('details')}")
        rec = canonical_from_live(card, now)
        rec["query_name"] = name
        if not rec.get("oracle_id") or not rec.get("scryfall_id") or not rec.get("oracle_text"):
            raise RuntimeError(f"Incomplete live Oracle record: {name}")
        if rec.get("commander_legality") != "legal":
            raise RuntimeError(f"Unexpected Commander legality for {name}: {rec.get('commander_legality')}")
        # Replace any older normalized record for this query name.
        rows = [r for r in rows if norm(r.get("query_name") or "") != norm(name)]
        rows.append(rec)
        by[norm(name)] = rec
        added.append(name)

    unresolved = [n for n in names if norm(n) not in by]
    if unresolved:
        raise RuntimeError("Candidate cache remains unresolved: " + ", ".join(unresolved))

    star = by[norm("Starscape Cleric")]
    if star.get("canonical_name") != "Starscape Cleric" or star.get("commander_legality") != "legal":
        raise RuntimeError("Starscape Cleric exact-printing override failed")
    if "Bat Cleric" not in (star.get("type_line") or "") or "Whenever you gain life" not in (star.get("oracle_text") or ""):
        raise RuntimeError("Starscape Cleric did not resolve to BLB #116 card object")

    rows.sort(key=lambda r: (r.get("canonical_name") or r.get("query_name") or "").casefold())
    cache_text = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows)
    CACHE.write_text(cache_text, encoding="utf-8")
    summary["generated_at_utc"] = now
    summary["records_written"] = len(rows)
    summary["distinct_names_requested"] = max(int(summary.get("distinct_names_requested") or 0), len(rows))
    summary["targeted_candidate_refresh"] = {
        "deck": "Sol'kanar the Swamp King",
        "candidate_path": str(CANDIDATE.relative_to(ROOT)),
        "missing_or_forced_names_resolved_live": added,
        "prior_cache_age_hours": round(age_hours, 3),
        "method": "reuse clean same-day cache; exact live Scryfall lookup for absent candidate names; force BLB/116 for Starscape Cleric identity collision",
    }
    summary["unresolved"] = []
    summary["overall_result"] = "PASS"
    summary["cache_sha256"] = hashlib.sha256(cache_text.encode("utf-8")).hexdigest()
    SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "resolved_live": added, "records": len(rows), "cache_sha256": summary["cache_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
