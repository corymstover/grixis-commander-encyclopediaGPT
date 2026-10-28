#!/usr/bin/env python3
"""Versioned current-list M7/M8 release gate; no legacy J or owner-approval inference."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

from build_m8_candidate_export import check as check_candidate_archive, read_current
from verify_current_62_oracle_coverage import audit as oracle_audit
from verify_m7_certification_transfer import validate_live_state

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path("refinement/verification/m8_current_release_evidence_v1.json")
RECEIPTS = ROOT / "refinement/verification/m7_certification_transfer"
EXCEPTIONS = ROOT / "source-package/research/Project_Exceptions_Current_2026-10-12.csv"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
CI = re.compile(r"^https://github\.com/corymstover/(GrokBotMTGCompanion|grixis-commander-encyclopediaGPT)/actions/runs/\d+(?:/job/\d+)?$")
ALLOWED = {"CURRENT_SHA_TESTED", "SUPERSEDED_BY_APPROVED_REVISION", "OWNER_ACCEPTED_LIMITATION"}
WHOLE_LIST_SOURCE_PREFIXES = (
    "data/grixis/m7/decision_reviews/",
    # Crosis's owner-approved exact-Rev2 whole-99 decision was filed as a packet.
    "data/grixis/m7/decision_packets/",
    # Davros, Doctor Doom and Don Andres Rev2 whole-99 research was independently
    # archived here; current-SHA, Git blob and local review SHA still mandatory.
    "data/grixis/m7/independent_reviews/",
    # Exact current-source multi-100 local-best pools were written in the M6
    # I/J research tree for certain early M7 decks (Ashad Rev3 included).
    "data/grixis/m6/ij/tested_pools/",
    "data/grixis/m7/nekusar_rev1/",
    "data/grixis/m7/rogsi_rev1/",
    "data/grixis/m7/saruman_rev1/",
    "data/grixis/m7/sauron_rev1/",
)


class CertificationError(ValueError):
    pass


def require(ok: bool, why: str) -> None:
    if not ok:
        raise CertificationError(why)


def repo_file(name: str) -> Path:
    require(isinstance(name, str) and bool(name), "Missing evidence path")
    rel = Path(name)
    require(not rel.is_absolute() and ".." not in rel.parts, f"Unsafe evidence path: {name}")
    path = (ROOT / rel).resolve()
    require(path.is_relative_to(ROOT.resolve()) and path.is_file(), f"Evidence file absent: {name}")
    return path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bound_file(path: str, expected: str) -> None:
    require(bool(HEX64.fullmatch(str(expected))), f"Missing or malformed evidence SHA: {path}")
    require(sha(repo_file(path)) == expected, f"Evidence SHA drift: {path}")


def snapshot_fingerprint(decks: list[dict]) -> str:
    """Stable release identity over exact 62 raw sources and exception policy bytes."""
    payload = {
        "schema_version": 1,
        "decks": sorted((x["id"], x["sha256"]) for x in decks),
        "exception_policy_sha256": sha(EXCEPTIONS),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def current_case_index(decks: list[dict]) -> tuple[dict[tuple[str, str], dict], int, int, int]:
    current = {x["id"]: x for x in decks}
    deferred: dict[tuple[str, str], dict] = {}
    transfer_count = p0_count = p1_pass_count = 0
    for path in sorted(RECEIPTS.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not (isinstance(data, dict) and "m6_transfer" in data and "approved_raw_sha256" in data):
            continue
        deck_id = data["deck_id"]
        require(deck_id in current, f"Unexpected transfer deck identity: {deck_id}")
        require(data["approved_raw_sha256"] == current[deck_id]["sha256"],
                f"Stale SHA-bound transfer receipt: {deck_id}")
        transfer_count += 1
        transfer = data["m6_transfer"]
        p0_count += len(transfer.get("P0", []))
        for case in transfer.get("P1", []):
            key = deck_id, case["case_id"]
            if case["status"] == "DEFERRED":
                require(key not in deferred, f"Duplicate deferred case: {key}")
                deferred[key] = case
            elif case["status"] == "PASSED":
                p1_pass_count += 1
            else:
                raise CertificationError(f"Unknown P1 status: {key}: {case['status']}")
    require(transfer_count >= 38 and p0_count >= 192 and p1_pass_count >= 193
            and len(deferred) + p1_pass_count >= 373,
            "M7 baseline case coverage regressed; explicitly version/reconcile before release")
    return deferred, transfer_count, p0_count, p1_pass_count


def validate_dispositions(rows: list[dict], deferred: dict, decks: list[dict]) -> set[tuple[str, str]]:
    current = {x["id"]: x for x in decks}
    seen: set[tuple[str, str]] = set()
    for row in rows:
        require(isinstance(row, dict), "Malformed case disposition")
        key = row.get("deck_id"), row.get("case_id")
        require(key in deferred, f"Case is not a currently deferred original P1: {key}")
        require(key not in seen, f"Duplicate case disposition: {key}")
        seen.add(key)
        source = current[key[0]]
        require(row.get("approved_raw_sha256") == source["sha256"], f"Case SHA drift: {key}")
        kind = row.get("disposition")
        require(kind in ALLOWED, f"Unknown disposition {kind}: {key}")
        require(len(str(row.get("reason", "")).strip()) >= 50, f"Insufficient case rationale: {key}")
        if kind == "CURRENT_SHA_TESTED":
            require(HEX40.fullmatch(str(row.get("engineering_commit_sha", ""))) is not None,
                    f"Missing immutable engineering commit: {key}")
            require(HEX40.fullmatch(str(row.get("test_blob_sha", ""))) is not None,
                    f"Missing exact test blob: {key}")
            require(CI.fullmatch(str(row.get("ci_run_url", ""))) is not None,
                    f"Missing exact-head test run: {key}")
            require(row.get("test_ref") and row.get("positive_assertion") and row.get("adversarial_assertion")
                    and row.get("limitations"), f"Incomplete positive/adversarial test evidence: {key}")
        else:
            bound_file(row.get("evidence_path"), row.get("evidence_sha256"))
            if kind == "SUPERSEDED_BY_APPROVED_REVISION":
                removed = row.get("removed_source_cards")
                require(isinstance(removed, list) and bool(removed), f"No obsolete source cards: {key}")
                names = {card for _, card, _ in source["cards"]}
                require(all(isinstance(name, str) and name and name not in names for name in removed),
                        f"Claimed obsolete card is still in exact 100: {key}")
                require(row.get("surviving_line_disposition"), f"Missing surviving successor reasoning: {key}")
            else:
                bound_file(row.get("owner_acceptance_path"), row.get("owner_acceptance_sha256"))
                approval = repo_file(row["owner_acceptance_path"]).read_text(encoding="utf-8")
                require(source["sha256"] in approval and key[1] in approval
                        and "limitation" in approval.lower(),
                        f"Owner has not explicitly accepted the exact-SHA case limitation: {key}")
    return seen


def validate_deck_attestations(rows: list[dict], decks: list[dict]) -> set[str]:
    current = {x["id"]: x for x in decks}
    seen: set[str] = set()
    for row in rows:
        require(isinstance(row, dict), "Malformed quality attestation")
        deck_id = row.get("deck_id")
        require(deck_id in current and deck_id not in seen, f"Unknown/duplicate deck attestation: {deck_id}")
        seen.add(deck_id)
        require(row.get("approved_raw_sha256") == current[deck_id]["sha256"],
                f"Quality review not for current 100: {deck_id}")
        require(row.get("outcome") == "KEEP_EXACT_100", f"Unresolved material change: {deck_id}")
        require(row.get("commander_first") and row.get("mana_and_protection")
                and row.get("win_lines_and_counterplay") and row.get("tested_pool_stop_reason")
                and row.get("historical_M6_case_scope"),
                f"Missing original-case/I and commander-first analytical scopes: {deck_id}")
        bound_file(row.get("review_path"), row.get("review_sha256"))
        require(HEX40.fullmatch(str(row.get("source_commit_sha", ""))) is not None,
                f"Missing pinned tested review commit: {deck_id}")
        engineering_source = row.get("engineering_review_path")
        require(isinstance(engineering_source, str)
                and any(engineering_source.startswith(prefix) for prefix in WHOLE_LIST_SOURCE_PREFIXES)
                and engineering_source.endswith((".json", ".md"))
                and ".." not in Path(engineering_source).parts,
                f"Missing exact M7 whole-list decision source: {deck_id}")
        require(HEX40.fullmatch(str(row.get("engineering_review_blob_sha", ""))) is not None,
                f"Missing Git blob commitment for M7 whole-list decision: {deck_id}")
        # The 24 original/Oct24 grandfathered locks do not have the newer
        # exact-SHA M7 P0/P1 transfer receipt. Never let a general whole-99
        # strategy paragraph silently stand in for original-case mechanics.
        transfer = RECEIPTS / f"{deck_id}_{current[deck_id]['sha256'][:16]}.json"
        if not transfer.is_file():
            require(row.get("grandfathered_case_scope_outcome") ==
                    "ALL_RELEVANT_ORIGINAL_CASES_ACCOUNTED_FOR",
                    f"Grandfathered M6 P0/P1 scope remains unverified: {deck_id}")
            bound_file(row.get("grandfathered_case_scope_path"),
                       row.get("grandfathered_case_scope_sha256"))
            mechanics = repo_file(row["grandfathered_case_scope_path"]).read_text(encoding="utf-8")
            require(current[deck_id]["sha256"] in mechanics and "P0" in mechanics and "P1" in mechanics,
                    f"Grandfathered case report must explicitly bind current SHA and P0/P1: {deck_id}")
    return seen


def evidence_fingerprint(source_fingerprint: str, register: dict) -> str:
    payload = {
        "policy": "CURRENT_SHA_CERTIFICATION_V1",
        "release_fingerprint": source_fingerprint,
        "case_dispositions": sorted(register["case_dispositions"], key=lambda x: (x["deck_id"], x["case_id"])),
        "deck_quality_attestations": sorted(register["deck_quality_attestations"], key=lambda x: x["deck_id"]),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode("utf-8")).hexdigest()


def verify_final_archive(name: str, digest: str, decks: list[dict]) -> None:
    require(isinstance(name, str) and name.startswith("exports/") and "CANDIDATE" not in name.upper(),
            "M8 final archive must be a distinct final artifact")
    bound_file(name, digest)
    with zipfile.ZipFile(repo_file(name)) as archive:
        index_names = [n for n in archive.namelist() if n.endswith("/index.json")]
        require(len(index_names) == 1, "Final archive must contain one manifest index")
        index = json.loads(archive.read(index_names[0]))
        # Artifact exists BEFORE the user accepts it, so it must not claim
        # OWNER_ACCEPTED by itself. The separate owner receipt certifies it.
        require(index.get("status") == "M8_RELEASE_CANDIDATE_AWAITING_OWNER_ACCEPTANCE",
                "Final export manifest must await explicit owner acceptance")
        records = index.get("decks") or []
        require(len(records) == 62, "Final archive manifest is not 62 decks")
        by_id = {x["id"]: x for x in decks}
        prefix = index_names[0].removesuffix("index.json")
        for row in records:
            deck_id = row.get("deck_id")
            require(deck_id in by_id and row.get("source_sha256") == by_id[deck_id]["sha256"],
                    f"Final archive includes wrong current deck: {deck_id}")
            raw_name = prefix + row["archive_source"]
            require(hashlib.sha256(archive.read(raw_name)).hexdigest() == by_id[deck_id]["sha256"],
                    f"Final archive physical source differs: {deck_id}")
            arch_name = prefix + row["archidekt_file"]
            require(hashlib.sha256(archive.read(arch_name)).hexdigest() == row["archidekt_sha256"],
                    f"Final archive Archidekt checksum drift: {deck_id}")
        require(len({x["deck_id"] for x in records}) == 62, "Final archive duplicate deck")


def inspect(register: dict, *, include_archive: bool = True) -> dict:
    require(register.get("schema_version") == 1 and register.get("policy") == "CURRENT_SHA_CERTIFICATION_V1",
            "Unsupported current-list certification register")
    require(register.get("owner_policy_authorized_on") == "2026-10-28"
            and register.get("historical_m6_j_relabelled_as_current") is False,
            "Owner-authorized versioned route may not relabel historical J")
    decks = read_current()  # 62 approved current SHA, tracker, owner receipt, 100/singleton.
    oracle = oracle_audit()  # Current pinned full Oracle, Grixis and explicit exception checks.
    transfer = validate_live_state(ROOT)  # Immutable M6 case and approval snapshots, exact M7 receipts.
    if include_archive:
        check_candidate_archive()  # Historical M8 preview still exact and explicitly NOT certified.
    deferred, receipts, p0, p1_passed = current_case_index(decks)
    resolved = validate_dispositions(register.get("case_dispositions", []), deferred, decks)
    reviewed = validate_deck_attestations(register.get("deck_quality_attestations", []), decks)
    fingerprint = snapshot_fingerprint(decks)
    evidence_hash = evidence_fingerprint(fingerprint, register)
    acceptance = register.get("m8_owner_acceptance")
    owner_signed = False
    pending_cases = len(deferred) - len(resolved)
    pending_decks = 62 - len(reviewed)
    if acceptance is not None:
        require(pending_cases == 0 and pending_decks == 0,
                "M8 owner acceptance cannot predate unresolved cases or quality reviews")
        require(isinstance(acceptance, dict), "Malformed M8 owner acceptance")
        require(acceptance.get("release_fingerprint") == fingerprint, "M8 owner approval covers another list")
        require(acceptance.get("evidence_fingerprint") == evidence_hash,
                "M8 owner acceptance covers a different set of test and judgment evidence")
        verify_final_archive(acceptance.get("final_archive_path", ""),
                             acceptance.get("final_archive_sha256"), decks)
        bound_file(acceptance.get("receipt_path"), acceptance.get("receipt_sha256"))
        receipt_text = repo_file(acceptance["receipt_path"]).read_text(encoding="utf-8")
        require(fingerprint in receipt_text and evidence_hash in receipt_text and "M8" in receipt_text
                and "project exceptions" in receipt_text.lower(),
                "Owner M8 receipt must bind current source, evidence and explicitly acknowledge exceptions")
        owner_signed = True
    complete = pending_cases == 0 and pending_decks == 0 and owner_signed
    return {
        "schema_version": 1,
        "status": "COMPLETE_CURRENT_SHA_EVIDENCE_WITH_OWNER_M8_ACCEPTANCE" if complete else "PENDING_CURRENT_SHA_EVIDENCE_NOT_M8_ACCEPTED",
        "release_fingerprint": fingerprint,
        "evidence_fingerprint": evidence_hash,
        "approved_locked_exact_decks": len(decks),
        "playable_cards": oracle["playable_cards"],
        "project_only_nonlegal_entries": oracle["nonlegal_entries_with_explicit_project_exception"],
        "current_M7_transfer_receipts": receipts,
        "historical_grandfathered_decks": 62 - receipts,
        "transferred_P0_passed": p0,
        "transferred_P1_passed": p1_passed,
        "original_deferred_P1": len(deferred),
        "current_sha_case_dispositions": len(resolved),
        "P1_pending_current_disposition": pending_cases,
        "current_sha_commander_first_attestations": len(reviewed),
        "quality_attestations_pending": pending_decks,
        "owner_M8_acceptance_present": owner_signed,
        "historical_M6_J_counted_as_current": 0,
        "structural_and_provenance_checks": "PASS",
        "ready_for_final_release": complete,
        "historical_snapshot_count": transfer["historical_locks_preserved"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", required=True)
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--evidence", default=str(EVIDENCE))
    args = parser.parse_args()
    try:
        reg = json.loads(repo_file(args.evidence).read_text(encoding="utf-8"))
        result = inspect(reg)
    except (CertificationError, ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"CURRENT-SHA CERTIFICATION INVALID: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.require_complete and not result["ready_for_final_release"]:
        parser.exit(1, "CURRENT-SHA CERTIFICATION INCOMPLETE: explicit cases, quality review, and M8 owner acceptance pending\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
