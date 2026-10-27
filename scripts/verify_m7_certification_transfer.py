#!/usr/bin/env python3
"""Fail-closed provenance gate for future Grixis canonical approval changes.

Historical locks are preserved; an altered/new approved raw SHA must carry
case-by-case M6 P0/P1 scope evidence and M7 decision-gate receipts. This gate
checks provenance structure, not the truth of external CI or Magic outcomes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("state/current_deck_overrides.json")
FROZEN = Path("refinement/verification/m7_certification_transfer/frozen_approval_snapshot_2026-10-24.json")
PLANS = Path("refinement/verification/m7_certification_transfer/m6_required_cases_2026-10-24.json")
ATTESTATIONS = Path("refinement/verification/m7_certification_transfer")
NORMAN_LEGACY_ID_RESOLUTION = ATTESTATIONS / "Goben_Norman_owner_identity_resolution_2026-10-27.json"
# Immutable source-bound authority snapshots. Moving the baseline forward to
# conceal a new approval is forbidden; an explicit Cory-approved governance
# revision must change both these pins and document why.
SNAPSHOT_SHA256 = "821468502031359c24ab92acb235ccce22c31299a0fff16a43b3bced6da491b5"
PLAN_MANIFEST_SHA256 = "195e2dd6f15aed70cc4384e68d33e200623e34e8f088da939752ea28216dcac8"
HEX64 = re.compile(r"^[0-9a-f]{64}$")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
CI_URL = re.compile(r"^https://github\.com/corymstover/(?:GrokBotMTGCompanion|grixis-commander-encyclopediaGPT)/actions/runs/[0-9]+(?:/job/[0-9]+)?$")
PR_URL = re.compile(r"^https://github\.com/corymstover/GrokBotMTGCompanion/pull/[0-9]+$")


class EvidenceError(ValueError):
    """Missing/contradictory mandatory certification evidence."""


def require(value, message: str):
    if not value:
        raise EvidenceError(message)
    return value


def load_json(root: Path, relative: Path) -> dict:
    path = root / relative
    require(path.is_file(), f"Missing evidence file: {relative}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise EvidenceError(f"Invalid JSON at {relative}: {exc}") from exc


def inside_repo(root: Path, relative: str) -> Path:
    require(isinstance(relative, str) and relative, "Missing repository-relative path")
    p = Path(relative)
    require(not p.is_absolute() and ".." not in p.parts, f"Unsafe path: {relative}")
    return root / p


def resolve_required_plan(root: Path, deck_id: str, approved: dict, plans: dict):
    """Resolve the *one* owner-approved historical roster alias, fail closed.

    The Oct24 frozen 62-key registry and pinned 61-plan manifest remain
    immutable. This only supplies Norman's preexisting plan to the legacy
    Goben registry key for a case-by-case future attestation, not a pass.
    """
    if deck_id != "Goben__Gene_Splice_Savant":
        return plans.get(deck_id)
    resolution = load_json(root, NORMAN_LEGACY_ID_RESOLUTION)
    expected = {
        "schema_version": 1,
        "historical_registry_id": "Goben__Gene_Splice_Savant",
        "actual_commander_deck_id": "Norman_Osborn_Green_Goblin",
        "approved_raw_sha256": "c002a49243bd54780bb0f4a36a3c239a00e042defa1d0c6c4b891c3c8060eef9",
        "approved_artifact": "refinement/decklists/Norman_Osborn_Green_Goblin_M7_Rev1_Approved_2026-10-26.txt",
        "commander_line": "1x Norman Osborn // Green Goblin [Commander]",
        "plan_source_path": "data/grixis/m6/test_blueprints/Norman_Osborn_Green_Goblin.json",
        "plan_blob_sha": "24c7b78a1548c7f0c9cf40931d06b13286cf0f6c",
    }
    for field, value in expected.items():
        require(resolution.get(field) == value,
                f"Goben/Norman identity resolution changed {field}; owner authorization required")
    require("2026-10-27" in str(resolution.get("owner_authorization_receipt", ""))
            and "Sure" in str(resolution.get("owner_authorization_receipt", "")),
            "Goben/Norman identity resolution lacks the exact owner authorization")
    require(approved.get("approved_list_sha256") == expected["approved_raw_sha256"]
            and approved.get("approved_list_artifact") == expected["approved_artifact"],
            "Goben/Norman alias cannot transfer to a different approved 100")
    source = inside_repo(root, expected["approved_artifact"])
    require(source.is_file(), "Goben/Norman approved Norman source file missing")
    require(hashlib.sha256(source.read_bytes()).hexdigest() == expected["approved_raw_sha256"]
            and source.read_text(encoding="utf-8").splitlines()[0] == expected["commander_line"],
            "Goben/Norman approved list bytes or commander identity changed")
    require(deck_id not in plans,
            "Goben now has a distinct source plan; do not silently use the Norman alias")
    plan = require(plans.get(expected["actual_commander_deck_id"]),
                   "Norman source plan absent from immutable 61-plan manifest")
    require(plan.get("plan_deck_id") == expected["actual_commander_deck_id"]
            and plan.get("source_path") == expected["plan_source_path"]
            and plan.get("plan_blob_sha") == expected["plan_blob_sha"],
            "Goben/Norman alias does not match immutable Norman case inventory")
    return plan


def valid_ci(value: str, label: str):
    require(isinstance(value, str) and CI_URL.fullmatch(value), f"{label}: exact GitHub Actions URL required")


def validate_case_records(tier: str, records: list, expected: list, prefix: str, candidate_sha: str):
    require(isinstance(records, list), f"{prefix}: {tier} records must be a list")
    by_id: dict[str, dict] = {}
    for entry in records:
        require(isinstance(entry, dict), f"{prefix}: malformed {tier} case")
        case_id = require(entry.get("case_id"), f"{prefix}: case without ID")
        require(case_id not in by_id, f"{prefix}: duplicate {tier} case {case_id}")
        by_id[case_id] = entry
    require(set(by_id) == set(expected),
            f"{prefix}: {tier} inventory mismatch (missing {sorted(set(expected)-set(by_id))}, "
            f"extra {sorted(set(by_id)-set(expected))})")

    for case_id, item in by_id.items():
        label = f"{prefix} {tier}/{case_id}"
        status = item.get("status")
        if status == "DEFERRED":
            require(tier == "P1", f"{label}: required P0 may not be deferred")
            for field in ("specific_reason", "coverage_consequence", "owner_visible_unresolved"):
                require(item.get(field), f"{label}: missing {field} for P1 deferral")
            require(item["owner_visible_unresolved"] is True,
                    f"{label}: P1 deferral must remain owner-visible")
            continue
        require(status == "PASSED", f"{label}: unexecuted/failed case cannot be certified")
        for field in ("test_ref", "execution_command", "oracle_source", "payable_fixture",
                      "positive_assertion", "adversarial_assertion"):
            require(isinstance(item.get(field), str) and item[field].strip(),
                    f"{label}: missing executable/source-bound {field}")
        valid_ci(item.get("ci_run_url"), label)
        scope = item.get("scope")
        if scope == "EXACT_APPROVED_100":
            require(item.get("tested_raw_sha256") == candidate_sha,
                    f"{label}: exact-100 case test SHA differs from approved candidate")
        elif scope == "REUSED_UNCHANGED":
            require(HEX64.fullmatch(str(item.get("prior_candidate_sha256", ""))),
                    f"{label}: missing original test scope SHA")
            require(isinstance(item.get("transfer_rationale"), str)
                    and len(item["transfer_rationale"].strip()) >= 35,
                    f"{label}: explain why new add/cut package does not invalidate this case")
        else:
            raise EvidenceError(f"{label}: unknown or unspecified tested scope")


def validate_attestation(root: Path, deck_id: str, approved: dict, required: dict, doc: dict):
    sha = approved.get("approved_list_sha256")
    label = f"{deck_id}@{str(sha)[:12]}"
    require(doc.get("schema_version") == 1, f"{label}: unsupported attestation version")
    require(doc.get("deck_id") == deck_id, f"{label}: attestation deck identity mismatch")
    require(doc.get("approved_raw_sha256") == sha, f"{label}: attestation SHA mismatch")
    artifact = approved.get("approved_list_artifact")
    require(doc.get("approved_artifact") == artifact, f"{label}: approved artifact mismatch")
    raw = inside_repo(root, artifact)
    require(raw.is_file(), f"{label}: approved artifact missing")
    require(hashlib.sha256(raw.read_bytes()).hexdigest() == sha,
            f"{label}: GitHub-approved raw bytes disagree with registry")

    receipt = inside_repo(root, require(doc.get("owner_approval_receipt"), f"{label}: missing owner receipt"))
    require(receipt.is_file(), f"{label}: owner approval receipt absent")
    require(sha in receipt.read_text(encoding="utf-8"),
            f"{label}: owner approval receipt does not name exact approved SHA")
    require(approved.get("approval_status") == "APPROVED"
            and approved.get("lock_status") == "LOCKED",
            f"{label}: not an APPROVED/LOCKED canonical transition")

    eng = require(doc.get("engineering"), f"{label}: missing independent engineering provenance")
    require(PR_URL.fullmatch(str(eng.get("pr_url", ""))), f"{label}: engineering PR URL required")
    require(HEX40.fullmatch(str(eng.get("head_sha", ""))), f"{label}: engineering exact head required")
    for field in ("grok_first_pass_ref", "independent_review_ref", "m7_decision_packet_ref",
                  "m7_decision_gate_command", "oracle_legality_ref"):
        require(eng.get(field), f"{label}: missing {field}")
    valid_ci(eng.get("m7_decision_gate_ci_run_url"), label)

    transfer = require(doc.get("m6_transfer"), f"{label}: missing M6 I/J transfer")
    if deck_id == "Abaddon_the_Despoiler":
        require(transfer.get("abaddon_p0_evidence") and transfer.get("ij_receipt_ref"),
                f"{label}: Abaddon-specific M6 P0/I/J evidence required")
        return
    require(required, f"{label}: missing 61-deck M6 plan; roster alias/conflict must be resolved")
    require(transfer.get("plan_source_path") == required["source_path"] and
            transfer.get("plan_blob_sha") == required["plan_blob_sha"],
            f"{label}: M6 commander-specific plan source mismatch")
    require(transfer.get("ij_receipt_ref"), f"{label}: missing I/J evidence receipt")
    require(transfer.get("ij_scope") in ("SAME_EXACT_100", "TRANSFERRED_WITH_CASE_MAPPING"),
            f"{label}: must explicitly distinguish original I/J candidate from final revision")
    if transfer["ij_scope"] == "TRANSFERRED_WITH_CASE_MAPPING":
        require(transfer.get("revision_diff_and_validity_reason"),
                f"{label}: changed-candidate I/J scope must be evaluated")
    validate_case_records("P0", transfer.get("P0"), required["required_P0"], label, sha)
    validate_case_records("P1", transfer.get("P1"), required["required_P1"], label, sha)


def validate_live_state(root: Path) -> dict:
    for rel, expected_hash in ((FROZEN, SNAPSHOT_SHA256), (PLANS, PLAN_MANIFEST_SHA256)):
        path = root / rel
        require(path.is_file(), f"Immutable authority snapshot missing: {rel}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash,
                f"Immutable authority snapshot changed without owner authorization: {rel}")
    snapshot = load_json(root, FROZEN)
    plans = load_json(root, PLANS)
    registry = load_json(root, REGISTRY)
    original = snapshot["approved_sha256_by_deck"]
    actual = registry["decks"]
    require(len(original) == 62 and set(original) == set(actual),
            "Snapshot/registry roster drift: do not silently remap any of 62 decks")
    require(len(plans["decks"]) == 61 and plans["case_totals"] == {"P0": 308, "P1": 574},
            "M6 61-deck source requirement manifest drift")
    require(snapshot["already_new_m7_locked_at_snapshot_count"] == 24,
            "Historical owner-approved lock count modified")
    changed = []
    for deck_id, deck in actual.items():
        sha = deck.get("approved_list_sha256")
        require(HEX64.fullmatch(str(sha)), f"{deck_id}: invalid current raw SHA")
        if sha == original[deck_id]:
            continue  # historical owner approval immutable; no retroactive silent invalidation
        rel = ATTESTATIONS / f"{deck_id}_{sha[:16]}.json"
        attestation = load_json(root, rel)
        required = resolve_required_plan(root, deck_id, deck, plans["decks"])
        validate_attestation(root, deck_id, deck, required, attestation)
        changed.append(deck_id)
    return {"historical_locks_preserved": len(actual) - len(changed),
            "new_or_revised_approvals_with_case_evidence": changed,
            "source_plans": len(plans["decks"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", required=True)
    args = parser.parse_args()
    assert args.check
    try:
        result = validate_live_state(ROOT)
    except (EvidenceError, KeyError, TypeError) as exc:
        parser.exit(1, f"M7 CERTIFICATION TRANSFER BLOCKED: {exc}\n")
    print("M7 certification transfer gate PASS: " + json.dumps(result, sort_keys=True))
    print("PASS covers required evidence provenance only; not actual Magic simulation, live Oracle, or owner consent.")


if __name__ == "__main__":
    main()
