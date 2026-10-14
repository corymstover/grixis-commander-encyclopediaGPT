#!/usr/bin/env python3
"""Retrospectively verify current-cycle approved decks #1-8 against the fresh GitHub Oracle cache.

This is the machine gate only: exact list structure, canonical Oracle resolution, color identity,
Commander legality, project exceptions, companion treatment, and reproducible evidence. Nontrivial
rules/interaction attestation is a separate human gate and is intentionally not invented here.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache.jsonl"
CACHE_SUMMARY = ROOT / "refinement/metadata_audit/Current_Cycle_Oracle_Cache_Summary.json"
EXCEPTIONS = ROOT / "source-package/research/Project_Exceptions_Current_2026-10-12.csv"
STATE = ROOT / "state/current_deck_overrides.json"
OUT = ROOT / "refinement/verification/retrospective_1_to_8"

DECKS = [
    {
        "number": 1,
        "id": "Abaddon_the_Despoiler",
        "display": "Abaddon the Despoiler",
        "path": "refinement/decklists/Abaddon_the_Despoiler_Approved_2026-10-13.txt",
        "approval_evidence": "state/current_deck_overrides.json; refinement/verification/Abaddon_Approved_Source_SHA_Reconciled_2026-10-14.md",
    },
    {
        "number": 2,
        "id": "Admiral_Beckett_Brass",
        "display": "Admiral Beckett Brass",
        "path": "refinement/decklists/Admiral_Beckett_Brass_Approval_Ready_2026-10-13.txt",
        "approval_evidence": "state/current_deck_overrides.json; refinement/verification/Admiral_Beckett_Brass_Approval_Ready_Closeout_2026-10-13.md",
    },
    {
        "number": 3,
        "id": "Admiral_Brass__Unsinkable",
        "display": "Admiral Brass, Unsinkable",
        "path": "refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt",
        "approval_evidence": "state/current_deck_overrides.json; refinement/verification/Admiral_Brass_Unsinkable_Whole_List_Closeout_2026-10-13.md",
    },
    {
        "number": 4,
        "id": "Anhelo_the_Painter",
        "display": "Anhelo, the Painter",
        "path": "refinement/decklists/Anhelo_the_Painter_Approval_Ready_2026-10-13.txt",
        "approval_evidence": "state/current_deck_overrides.json; refinement/verification/Anhelo_the_Painter_Approval_Ready_Closeout_2026-10-13.md",
    },
    {
        "number": 5,
        "id": "Ashad_the_Lone_Cyberman",
        "display": "Ashad, the Lone Cyberman",
        "path": "refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt",
        "approval_evidence": "state/current_deck_overrides.json; refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md",
    },
    {
        "number": 6,
        "id": "Ashnod_the_Uncaring",
        "display": "Ashnod the Uncaring",
        "path": "refinement/decklists/Ashnod_the_Uncaring_Approved_2026-10-13.txt",
        "approval_evidence": "refinement/approvals/Ashnod_the_Uncaring_Approved_2026-10-13.md",
    },
    {
        "number": 7,
        "id": "Be_lakor_the_Dark_Master",
        "display": "Be'lakor, the Dark Master",
        "path": "refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt",
        "approval_evidence": "refinement/approvals/Be_lakor_the_Dark_Master_Approved_2026-10-13.md",
    },
    {
        "number": 8,
        "id": "Cecily__Bjorna__Lutri",
        "display": "Bjorna, Nightfall Alchemist // Cecily, Haunted Mage + Lutri companion",
        "path": "refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt",
        "approval_evidence": "refinement/approvals/Cecily__Bjorna__Lutri_Approved_2026-10-13.md",
        "companions": ["Lutri, the Spellchaser"],
    },
]

BASIC_NAMES = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes", "Snow-Covered Plains", "Snow-Covered Island", "Snow-Covered Swamp", "Snow-Covered Mountain", "Snow-Covered Forest"}
LINE_RE = re.compile(r"^\s*(\d+)x\s+(.+?)(?:\s+\[[^\]]+\])?\s*$")
ROLE_RE = re.compile(r"\s+\[([^\]]+)\]\s*$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm_name(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.casefold().replace("’", "'"))


def parse_deck(path: Path):
    rows = []
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    for line_no, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        role_match = ROLE_RE.search(line)
        role = role_match.group(1) if role_match else ""
        m = LINE_RE.match(line)
        if not m:
            raise RuntimeError(f"Malformed deck line {path}:{line_no}: {line}")
        qty = int(m.group(1))
        name = m.group(2).strip()
        rows.append({"line_no": line_no, "quantity": qty, "card_name": name, "role": role})
    return raw, rows


def load_cache():
    cache = {}
    collisions = {}
    for line in CACHE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        for key_name in {rec.get("query_name", ""), rec.get("canonical_name", "")}:
            if not key_name:
                continue
            key = norm_name(key_name)
            if key in cache and cache[key].get("oracle_id") != rec.get("oracle_id"):
                collisions.setdefault(key, []).append(rec)
            else:
                cache[key] = rec
    if collisions:
        raise RuntimeError(f"Ambiguous cache keys: {sorted(collisions)}")
    return cache


def load_exceptions():
    out = {}
    with EXCEPTIONS.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            out[(row["deck_id"], norm_name(row["card_name"]))] = row
    return out


def is_copy_exception(name: str, rec: dict) -> bool:
    if name in BASIC_NAMES:
        return True
    text = (rec.get("oracle_text") or "").casefold()
    return "a deck can have" in text and "cards named" in text


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if not CACHE.exists() or not CACHE_SUMMARY.exists():
        raise RuntimeError("Fresh current-cycle Oracle cache is missing")
    cache_summary = json.loads(CACHE_SUMMARY.read_text(encoding="utf-8"))
    if cache_summary.get("overall_result") != "PASS" or cache_summary.get("unresolved"):
        raise RuntimeError("Current-cycle Oracle cache is not a clean PASS")
    cache = load_cache()
    exceptions = load_exceptions()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"decks": {}}
    generated = datetime.now(timezone.utc).isoformat()
    project_summary = {
        "generated_at_utc": generated,
        "cache_generated_at_utc": cache_summary.get("generated_at_utc"),
        "bulk_updated_at": cache_summary.get("bulk_updated_at"),
        "cache_sha256": cache_summary.get("cache_sha256"),
        "official_banlist_checkpoint": "refinement/verification/Retrospective_1_to_8_Official_Banlist_Checkpoint_2026-10-14.md",
        "decks": [],
        "machine_gate_result": "PASS",
        "rules_gate_result": "PENDING_HUMAN_ATTESTATION",
        "overall_result": "BLOCKED_PENDING_RULES_ATTESTATION",
    }

    for deck in DECKS:
        path = ROOT / deck["path"]
        if not path.exists():
            raise RuntimeError(f"Approved source missing: {deck['path']}")
        raw, entries = parse_deck(path)
        raw_sha = sha256_bytes(raw)
        total = sum(x["quantity"] for x in entries)
        commander_entries = [x for x in entries if "Commander" in x["role"]]
        if not commander_entries:
            raise RuntimeError(f"No commander marker in {deck['path']}")
        commander_ci = set()
        card_rows = []
        unresolved = []
        failures = []
        project_exceptions = []
        counts = Counter()
        for entry in entries:
            name = entry["card_name"]
            rec = cache.get(norm_name(name))
            if rec is None:
                unresolved.append(name)
                continue
            counts[name] += entry["quantity"]
            if "Commander" in entry["role"]:
                commander_ci.update(rec.get("color_identity") or [])
        if unresolved:
            failures.append(f"unresolved cache records: {unresolved}")

        for entry in entries:
            name = entry["card_name"]
            rec = cache.get(norm_name(name))
            if rec is None:
                continue
            ci = set(rec.get("color_identity") or [])
            color_ok = ci.issubset(commander_ci)
            legality = rec.get("commander_legality", "unknown")
            exc = exceptions.get((deck["id"], norm_name(name)))
            if legality == "legal":
                legality_result = "PASS"
            elif exc and str(exc.get("project_status", "")).startswith("INTENTIONAL"):
                legality_result = "PROJECT_EXCEPTION"
                project_exceptions.append({"card_name": name, "official_status": legality, "exception_type": exc.get("exception_type")})
            else:
                legality_result = "FAIL"
                failures.append(f"unexpected Commander legality {legality} for {name}")
            if not color_ok:
                failures.append(f"color identity mismatch for {name}: {sorted(ci)} not subset of {sorted(commander_ci)}")
            card_rows.append({
                "deck_number": deck["number"],
                "deck_id": deck["id"],
                "card_name_export": name,
                "quantity": entry["quantity"],
                "role": entry["role"],
                "canonical_name": rec.get("canonical_name", ""),
                "scryfall_id": rec.get("scryfall_id", ""),
                "oracle_id": rec.get("oracle_id", ""),
                "source_generated_at_utc": rec.get("source_generated_at_utc", ""),
                "bulk_updated_at": rec.get("bulk_updated_at", ""),
                "type_line": rec.get("type_line", ""),
                "mana_cost": rec.get("mana_cost", ""),
                "color_identity": ",".join(rec.get("color_identity") or []),
                "commander_color_identity": ",".join(sorted(commander_ci)),
                "color_identity_result": "PASS" if color_ok else "FAIL",
                "commander_legality": legality,
                "project_exception_type": exc.get("exception_type", "") if exc else "",
                "verification_result": "FAIL" if not color_ok or legality_result == "FAIL" else legality_result,
                "oracle_text": rec.get("oracle_text", ""),
                "scryfall_uri": rec.get("scryfall_uri", ""),
            })

        singleton_failures = []
        for name, qty in counts.items():
            if qty <= 1:
                continue
            rec = cache.get(norm_name(name)) or {}
            if not is_copy_exception(name, rec):
                singleton_failures.append({"card_name": name, "quantity": qty})
        if singleton_failures:
            failures.append(f"singleton violations: {singleton_failures}")
        if total != 100:
            failures.append(f"main-deck count is {total}, expected 100")

        companion_rows = []
        for companion in deck.get("companions", []):
            rec = cache.get(norm_name(companion))
            exc = exceptions.get((deck["id"], norm_name(companion)))
            if rec is None:
                failures.append(f"companion unresolved: {companion}")
                continue
            legality = rec.get("commander_legality", "unknown")
            # Lutri is officially prohibited as companion even if a database's generic Commander field is phrased differently.
            if companion == "Lutri, the Spellchaser":
                official_status = "banned_as_companion"
            else:
                official_status = legality
            if not exc or not str(exc.get("project_status", "")).startswith("INTENTIONAL"):
                failures.append(f"companion lacks documented project exception: {companion}")
                result = "FAIL"
            else:
                result = "PROJECT_EXCEPTION"
                project_exceptions.append({"card_name": companion, "official_status": official_status, "exception_type": exc.get("exception_type")})
            companion_rows.append({
                "deck_number": deck["number"], "deck_id": deck["id"], "card_name_export": companion,
                "quantity": 1, "role": "Companion (outside 100)", "canonical_name": rec.get("canonical_name", ""),
                "scryfall_id": rec.get("scryfall_id", ""), "oracle_id": rec.get("oracle_id", ""),
                "source_generated_at_utc": rec.get("source_generated_at_utc", ""), "bulk_updated_at": rec.get("bulk_updated_at", ""),
                "type_line": rec.get("type_line", ""), "mana_cost": rec.get("mana_cost", ""),
                "color_identity": ",".join(rec.get("color_identity") or []), "commander_color_identity": ",".join(sorted(commander_ci)),
                "color_identity_result": "PASS" if set(rec.get("color_identity") or []).issubset(commander_ci) else "FAIL",
                "commander_legality": official_status, "project_exception_type": exc.get("exception_type", "") if exc else "",
                "verification_result": result, "oracle_text": rec.get("oracle_text", ""), "scryfall_uri": rec.get("scryfall_uri", ""),
            })

        # Lutri companion condition: every nonland card in the 100-card starting deck has a different name.
        companion_condition = "N/A"
        if deck.get("companions"):
            nonland_dupes = []
            for name, qty in counts.items():
                if qty <= 1:
                    continue
                rec = cache.get(norm_name(name)) or {}
                if "Land" not in (rec.get("type_line") or ""):
                    nonland_dupes.append({"card_name": name, "quantity": qty})
            companion_condition = "PASS" if not nonland_dupes else "FAIL"
            if nonland_dupes:
                failures.append(f"Lutri companion condition failed due to nonland duplicates: {nonland_dupes}")

        out_rows = card_rows + companion_rows
        csv_path = OUT / f"Card_Verification_{deck['id']}_2026-10-14.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
            w.writeheader(); w.writerows(out_rows)

        state_entry = state.get("decks", {}).get(deck["id"], {})
        result = "PASS" if not failures else "FAIL"
        if result != "PASS":
            project_summary["machine_gate_result"] = "FAIL"
            project_summary["overall_result"] = "FAIL"
        dsum = {
            "deck_number": deck["number"], "deck_id": deck["id"], "display": deck["display"],
            "approved_source": deck["path"], "approval_evidence": deck["approval_evidence"],
            "approved_source_raw_sha256": raw_sha,
            "historical_state_approved_list_sha256": state_entry.get("approved_list_sha256"),
            "main_deck_count": total, "commander_count": sum(x["quantity"] for x in commander_entries),
            "distinct_names": len(counts), "commander_color_identity": sorted(commander_ci),
            "singleton_result": "PASS" if not singleton_failures else "FAIL",
            "companion_condition": companion_condition,
            "project_exceptions": project_exceptions,
            "unresolved": unresolved, "failures": failures, "machine_gate_result": result,
        }
        project_summary["decks"].append(dsum)

        md = [
            f"# Fresh Oracle/legality gate — #{deck['number']} {deck['display']}", "",
            f"- Generated UTC: `{generated}`",
            f"- Approved source: `{deck['path']}`",
            f"- Approved source SHA-256 (raw bytes): `{raw_sha}`",
            f"- Approval evidence: {deck['approval_evidence']}",
            f"- Oracle cache generated UTC: `{cache_summary.get('generated_at_utc')}`",
            f"- Scryfall bulk updated UTC: `{cache_summary.get('bulk_updated_at')}`",
            f"- 100-card count: **{'PASS' if total == 100 else 'FAIL'}** ({total})",
            f"- Singleton: **{'PASS' if not singleton_failures else 'FAIL'}**",
            f"- Commander color identity: `{','.join(sorted(commander_ci))}`",
            f"- Per-card canonical Oracle/color/legality gate: **{result}**",
        ]
        if deck.get("companions"):
            md.append(f"- Companion condition: **{companion_condition}**; companion remains outside the 100-card count")
        if project_exceptions:
            md += ["", "## Project exceptions"] + [f"- **{x['card_name']}** — official status `{x['official_status']}`; project authorization `{x['exception_type']}`." for x in project_exceptions]
        if failures:
            md += ["", "## Failures"] + [f"- {x}" for x in failures]
        md += ["", "## Gate boundary", "This report passes only the machine-verifiable structural, current Oracle, color-identity, legality, singleton and documented-exception layer. Nontrivial rules/interaction claims require the separate rules attestation before retrospective certification is complete.", ""]
        (OUT / f"Verification_Gate_{deck['id']}_2026-10-14.md").write_text("\n".join(md), encoding="utf-8")

    (OUT / "Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.json").write_text(json.dumps(project_summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Retrospective decks #1–8 — machine gate summary", "", f"Generated UTC: `{generated}`", "", "| # | Deck | Count | Singleton | Oracle / CI / legality | Exceptions |", "|---:|---|---:|---|---|---|"]
    for d in project_summary["decks"]:
        lines.append(f"| {d['deck_number']} | {d['display']} | {d['main_deck_count']} | {d['singleton_result']} | {d['machine_gate_result']} | {len(d['project_exceptions'])} |")
    lines += ["", f"**Machine gate:** {project_summary['machine_gate_result']}", f"**Rules gate:** {project_summary['rules_gate_result']}", f"**Overall retrospective:** {project_summary['overall_result']}", "", "Machine PASS is necessary but not sufficient: the rules-interaction attestation must be completed separately.", ""]
    (OUT / "Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(project_summary, indent=2, ensure_ascii=False))
    if project_summary["machine_gate_result"] != "PASS":
        raise SystemExit(2)

if __name__ == "__main__":
    main()
