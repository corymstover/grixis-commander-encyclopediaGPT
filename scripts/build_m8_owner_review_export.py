#!/usr/bin/env python3
"""Build/verify the unsigned exact-62 M8 owner-review archive.

This is deliberately NOT the M8 owner-accepted release and must never modify
the 62 original approved source bytes, the 180-case register, or accept for Cory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

from build_m8_candidate_export import ARCHIVE as PREVIEW_ZIP, OUTPUT as PREVIEW_DIR
from verify_m8_current_certification import (
    EVIDENCE, ROOT, inspect, read_current, snapshot_fingerprint,
    verify_final_archive,
)


ARCHIVE = ROOT / "exports/Grixis_Commander_Encyclopedia_62_M8_OWNER_REVIEW_2026-10-28.zip"
PREFIX = "m8_owner_review_2026-10-28/"
STATUS = "M8_RELEASE_CANDIDATE_AWAITING_OWNER_ACCEPTANCE"


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def state() -> tuple[dict, dict, list[dict]]:
    register = json.loads((ROOT / EVIDENCE).read_text(encoding="utf-8"))
    result = inspect(register)
    decks = read_current()
    if (result["current_sha_case_dispositions"] != 180
            or result["P1_pending_current_disposition"] != 0
            or result["current_sha_commander_first_attestations"] != 62
            or result["quality_attestations_pending"] != 0
            or register["m8_owner_acceptance"] is not None
            or result["owner_M8_acceptance_present"]
            or result["ready_for_final_release"]):
        raise ValueError("Owner review requires all evidence and no owner acceptance")
    if result["release_fingerprint"] != snapshot_fingerprint(decks):
        raise ValueError("Current approved raw-source release fingerprint drift")
    return result, register, decks


def encode(obj: dict) -> bytes:
    return (json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def files_for_review() -> dict[str, bytes]:
    report, register, decks = state()
    with zipfile.ZipFile(PREVIEW_ZIP) as original:
        root = PREVIEW_DIR.name + "/"
        index = json.loads(original.read(root + "index.json"))
        source_files = {}
        for item, row in zip(decks, index["decks"]):
            if item["id"] != row["deck_id"] or item["sha256"] != row["source_sha256"]:
                raise ValueError("Preview deck identity changed")
            canon = original.read(root + row["archive_source"])
            arch = original.read(root + row["archidekt_file"])
            if sha(canon) != item["sha256"] or sha(arch) != row["archidekt_sha256"]:
                raise ValueError("Source or Archidekt bytes changed in previous preview")
            source_files[row["archive_source"]] = canon
            source_files[row["archidekt_file"]] = arch
        source_files["MASTER.txt"] = original.read(root + "MASTER.txt")

    metadata_gaps = [r["deck_id"] for r in index["decks"]
                     if not r.get("power_bracket") or not r.get("archidekt_tags")]
    index.update({
        "status": STATUS,
        "release_fingerprint": report["release_fingerprint"],
        "evidence_fingerprint": report["evidence_fingerprint"],
        "original_deferred_p1": 180,
        "original_p1_dispositions": 180,
        "original_p1_pending": 0,
        "commander_first_attestations": 62,
        "m8_owner_acceptance": None,
        "official_commander_legality_certified": False,
        "metadata_gaps": metadata_gaps,
        "release_blockers": [
            "Cory's explicit exact-source and exact-evidence M8 owner acceptance remains unsigned",
            "Six project-only nonofficial Commander legality entries require explicit owner acknowledgment",
            f"Power-bracket or Archidekt-tag metadata remains unfilled on {len(metadata_gaps)} approved decks",
        ],
    })
    summary = {
        "status": STATUS,
        "approved_locked_decks": 62,
        "playable_cards": 6200,
        "original_deferred_p1": 180,
        "original_dispositions_current": 180,
        "original_dispositions_retired": sum(r["disposition"] == "SUPERSEDED_BY_APPROVED_REVISION"
                                             for r in register["case_dispositions"]),
        "original_unresolved": 0,
        "commander_first_quality_attestations": 62,
        "historical_m6_j_relabelled_as_current": False,
        "m8_owner_acceptance": None,
        "release_fingerprint": report["release_fingerprint"],
        "evidence_fingerprint": report["evidence_fingerprint"],
        "official_commander_legality_certified": False,
        "project_only_nonlegal_entries": report["project_only_nonlegal_entries"],
        "missing_bracket_or_tag_metadata": metadata_gaps,
    }
    readme = (
        "GRIXIS COMMANDER ENCYCLOPEDIA — M8 OWNER REVIEW / UNSIGNED\n"
        "=========================================================\n\n"
        "Exactly 62 source-hash-locked, previously owner-approved commander-first decks,\n"
        "62 Archidekt import lists and a full master list are reproduced unchanged.\n"
        "There are 180/180 dispositions of original deferred P1 cases (168 tested\n"
        "against exact source, 12 retired due to approved revisions); all 62 current\n"
        "quality attestations are recorded. This is evidence coverage, not a\n"
        "claim that all Magic gameplay or every opponent matchup is simulated.\n\n"
        "M8 OWNER ACCEPTANCE IS NOT SIGNED. DO NOT CALL THIS A CERTIFIED RELEASE.\n"
        "The existing project-only banned/future cards are NOT represented as\n"
        "officially Commander legal. Read each index.json project_exceptions and\n"
        "the M8_EVIDENCE_LEDGER.json; the file also notes metadata gaps.\n\n"
        "For review, compare release_fingerprint and evidence_fingerprint in\n"
        "index.json and M8_EVIDENCE_SUMMARY.json. Cory must explicitly accept\n"
        "the exact evidence and project exceptions in a distinct M8 receipt.\n"
        "No draft receipt or owner signature is included in this ZIP.\n"
    ).encode("utf-8")
    return {**source_files, "index.json": encode(index),
            "M8_EVIDENCE_SUMMARY.json": encode(summary),
            "M8_EVIDENCE_LEDGER.json": encode(register), "README.txt": readme}


def build() -> None:
    if ARCHIVE.exists():
        raise FileExistsError("Preserve existing owner-review archive: " + str(ARCHIVE))
    payloads = files_for_review()
    with zipfile.ZipFile(ARCHIVE, "x", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as zipped:
        for rel, body in sorted(payloads.items()):
            info = zipfile.ZipInfo(PREFIX + rel, date_time=(2026, 10, 28, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zipped.writestr(info, body, compress_type=zipfile.ZIP_DEFLATED,
                            compresslevel=9)
    check()


def check() -> None:
    # This gate deliberately accepts the unsigned archive *structure* without
    # claiming owner M8 acceptance, exactly as the release verifier expects.
    report, register, decks = state()
    verify_final_archive(str(ARCHIVE.relative_to(ROOT)),
                         sha(ARCHIVE.read_bytes()), decks)
    with zipfile.ZipFile(ARCHIVE) as zipped:
        summary = json.loads(zipped.read(PREFIX + "M8_EVIDENCE_SUMMARY.json"))
        ledger = json.loads(zipped.read(PREFIX + "M8_EVIDENCE_LEDGER.json"))
        if (summary["release_fingerprint"] != report["release_fingerprint"]
                or summary["evidence_fingerprint"] != report["evidence_fingerprint"]
                or ledger != register or summary["m8_owner_acceptance"] is not None
                or len(zipped.namelist()) != 129):
            raise ValueError("Unsigned owner-review evidence or contents mismatch")
    print(f"M8_OWNER_REVIEW_UNSIGNED_PASS decks=62 cases=180 quality=62 archive_sha256={sha(ARCHIVE.read_bytes())}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build() if args.build else check()
