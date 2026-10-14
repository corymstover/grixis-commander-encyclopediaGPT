#!/usr/bin/env python3
"""Consolidate the retrospective #1-8 machine gate with the completed rules attestation.

This script is intentionally fail-closed. It does not create a rules decision. It validates the
machine-readable rules attestation against the exact human-attestation Markdown blob, confirms the
machine gate is a clean PASS for all eight expected decks, then writes one authoritative complete
retrospective status. If either layer is missing, stale, ambiguous, or non-PASS, consolidation fails.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "refinement/verification/retrospective_1_to_8"
MACHINE_JSON = OUT / "Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.json"
MACHINE_MD = OUT / "Retrospective_1_to_8_Machine_Gate_Summary_2026-10-14.md"
RULES_JSON = OUT / "Retrospective_1_to_8_Rules_Attestation_2026-10-14.json"
COMPLETE_JSON = OUT / "Retrospective_1_to_8_Complete_Gate_Summary_2026-10-14.json"
COMPLETE_MD = OUT / "Retrospective_1_to_8_Complete_Gate_Summary_2026-10-14.md"

EXPECTED = [
    (1, "Abaddon_the_Despoiler", "Abaddon the Despoiler"),
    (2, "Admiral_Beckett_Brass", "Admiral Beckett Brass"),
    (3, "Admiral_Brass__Unsinkable", "Admiral Brass, Unsinkable"),
    (4, "Anhelo_the_Painter", "Anhelo, the Painter"),
    (5, "Ashad_the_Lone_Cyberman", "Ashad, the Lone Cyberman"),
    (6, "Ashnod_the_Uncaring", "Ashnod the Uncaring"),
    (7, "Be_lakor_the_Dark_Master", "Be'lakor, the Dark Master"),
    (8, "Cecily__Bjorna__Lutri", "Bjorna // Cecily + Lutri"),
]
ALLOWED_RULES_RESULTS = {"PASS", "PASS_WITH_DOCUMENTATION_CORRECTION", "PASS_PROJECT_EXCEPTION"}


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def load_json(path: Path) -> dict:
    if not path.exists():
        raise RuntimeError(f"Required evidence missing: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    machine = load_json(MACHINE_JSON)
    rules = load_json(RULES_JSON)

    if machine.get("machine_gate_result") != "PASS":
        raise RuntimeError(f"Machine gate is not PASS: {machine.get('machine_gate_result')}")

    machine_decks = machine.get("decks") or []
    expected_ids = [x[1] for x in EXPECTED]
    machine_ids = [d.get("deck_id") for d in machine_decks]
    if machine_ids != expected_ids:
        raise RuntimeError(f"Machine deck sequence mismatch: {machine_ids!r}")
    for d in machine_decks:
        if d.get("machine_gate_result") != "PASS":
            raise RuntimeError(f"Machine deck gate is not PASS: {d.get('deck_id')} -> {d.get('machine_gate_result')}")
        if d.get("failures"):
            raise RuntimeError(f"Machine deck has failures: {d.get('deck_id')} -> {d.get('failures')}")
        if d.get("unresolved"):
            raise RuntimeError(f"Machine deck has unresolved records: {d.get('deck_id')} -> {d.get('unresolved')}")

    if rules.get("rules_gate_result") != "PASS":
        raise RuntimeError(f"Rules gate is not PASS: {rules.get('rules_gate_result')}")
    rules_decks = rules.get("decks") or []
    rules_ids = [d.get("deck_id") for d in rules_decks]
    if rules_ids != expected_ids:
        raise RuntimeError(f"Rules-attestation deck sequence mismatch: {rules_ids!r}")
    for d in rules_decks:
        if d.get("rules_result") not in ALLOWED_RULES_RESULTS:
            raise RuntimeError(f"Unacceptable rules result: {d.get('deck_id')} -> {d.get('rules_result')}")

    source_rel = rules.get("source_markdown_path")
    if not source_rel:
        raise RuntimeError("Rules attestation does not name its human source Markdown")
    source_md = ROOT / source_rel
    if not source_md.exists():
        raise RuntimeError(f"Human rules attestation missing: {source_rel}")
    actual_blob_sha = git_blob_sha1(source_md.read_bytes())
    expected_blob_sha = rules.get("source_markdown_git_blob_sha1")
    if actual_blob_sha != expected_blob_sha:
        raise RuntimeError(
            "Rules attestation source changed without rebinding machine-readable attestation: "
            f"expected blob {expected_blob_sha}, got {actual_blob_sha}"
        )

    rules_by_id = {d["deck_id"]: d for d in rules_decks}
    complete_decks = []
    for n, deck_id, display in EXPECTED:
        m = next(d for d in machine_decks if d["deck_id"] == deck_id)
        r = rules_by_id[deck_id]
        overall = "PASS_PROJECT_EXCEPTION" if r["rules_result"] == "PASS_PROJECT_EXCEPTION" else "PASS"
        complete_decks.append({
            "deck_number": n,
            "deck_id": deck_id,
            "display": m.get("display") or display,
            "machine_gate_result": "PASS",
            "rules_gate_result": r["rules_result"],
            "overall_result": overall,
            "approved_source": m.get("approved_source"),
            "approved_source_raw_sha256": m.get("approved_source_raw_sha256"),
            "main_deck_count": m.get("main_deck_count"),
            "singleton_result": m.get("singleton_result"),
            "project_exceptions": m.get("project_exceptions") or [],
        })

    generated = datetime.now(timezone.utc).isoformat()
    complete = {
        "schema_version": 1,
        "generated_at_utc": generated,
        "cycle_id": rules.get("cycle_id"),
        "authoritative_final_status": True,
        "machine_gate_result": "PASS",
        "rules_gate_result": "PASS",
        "overall_result": "PASS",
        "rules_attestation_source": source_rel,
        "rules_attestation_source_git_blob_sha1": actual_blob_sha,
        "oracle_cache_generated_at_utc": machine.get("cache_generated_at_utc"),
        "oracle_bulk_updated_at": machine.get("bulk_updated_at"),
        "oracle_cache_sha256": machine.get("cache_sha256"),
        "official_banlist_checkpoint": machine.get("official_banlist_checkpoint"),
        "decks": complete_decks,
        "notes": [
            "All eight machine gates pass with zero unresolved records and zero failures.",
            "The completed human rules attestation is SHA-bound through its exact Git blob hash.",
            "Ashnod's stale historical rules wording was corrected; no decklist change was required.",
            "Deck #8 remains project-valid under its registered Lutri / Trade Secrets / Yawgmoth's Bargain exceptions and is not represented as officially legal without qualification.",
        ],
    }
    COMPLETE_JSON.write_text(json.dumps(complete, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Reconcile the legacy machine-summary status fields so it no longer reports a stale blocker after
    # the required rules attestation has actually been completed.
    machine["rules_gate_result"] = "PASS"
    machine["overall_result"] = "PASS"
    machine["consolidated_complete_gate"] = str(COMPLETE_JSON.relative_to(ROOT))
    machine["authoritative_final_status"] = False
    machine["note"] = "Machine evidence plus rules attestation have been consolidated; use the complete-gate summary as the authoritative final status."
    MACHINE_JSON.write_text(json.dumps(machine, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    machine_lines = [
        "# Retrospective decks #1–8 — machine gate summary", "",
        f"Generated UTC: `{machine.get('generated_at_utc')}`", "",
        "| # | Deck | Count | Singleton | Oracle / CI / legality | Exceptions |",
        "|---:|---|---:|---|---|---|",
    ]
    for d in machine_decks:
        machine_lines.append(
            f"| {d['deck_number']} | {d['display']} | {d['main_deck_count']} | {d['singleton_result']} | {d['machine_gate_result']} | {len(d.get('project_exceptions') or [])} |"
        )
    machine_lines += [
        "", "**Machine gate:** PASS", "**Rules gate:** PASS", "**Overall retrospective:** PASS", "",
        f"Authoritative consolidated result: `{COMPLETE_JSON.relative_to(ROOT)}`", "",
        "The machine verifier remains a separate evidence layer; final certification is supplied by the SHA-bound complete-gate consolidation.", "",
    ]
    MACHINE_MD.write_text("\n".join(machine_lines), encoding="utf-8")

    lines = [
        "# Retrospective decks #1–8 — COMPLETE GATE", "",
        f"Generated UTC: `{generated}`", "",
        "**AUTHORITATIVE FINAL STATUS: PASS 8/8**", "",
        "| # | Deck | Machine | Rules | Final |",
        "|---:|---|---|---|---|",
    ]
    for d in complete_decks:
        lines.append(f"| {d['deck_number']} | {d['display']} | PASS | {d['rules_gate_result']} | {d['overall_result']} |")
    lines += [
        "", "## Consolidated gates", "",
        "- Structural / 100-card / singleton gate: **PASS 8/8**",
        "- Fresh Oracle / color-identity / Commander-legality gate: **PASS 8/8**",
        "- Official banned-list reconciliation: **PASS**, with deck #8's registered project exceptions explicitly preserved",
        "- Rules / material-interaction attestation: **PASS 8/8**",
        "- Unresolved card records: **0**",
        "- Machine failures: **0**",
        "- Required decklist changes from retrospective verification: **0**",
        "- Ashnod documentation correction: **recorded; list unchanged**",
        "", "## Fail-closed binding", "",
        f"The rules layer is bound to `{source_rel}` at Git blob SHA-1 `{actual_blob_sha}`. Any change to that attestation without updating its machine-readable binding causes consolidation to fail.",
        "", "**Overall retrospective result: PASS. Decks #1–8 remain approved and locked.**", "",
    ]
    COMPLETE_MD.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(complete, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
