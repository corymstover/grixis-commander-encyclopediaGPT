#!/usr/bin/env python3
"""Rebuild the exact-source M8 release candidate with six source-approved tags.

This artifact is deliberately UNSIGNED until the distinct owner acceptance
receipt binds its exact SHA and both certification fingerprints.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import build_m8_owner_review_export as review
from verify_m8_current_certification import ROOT, inspect, read_current, verify_final_archive

METADATA = ROOT / "refinement/verification/m8_six_archidekt_metadata_reconciliation_2026-10-28.json"
ARCHIVE = ROOT / "exports/Grixis_Commander_Encyclopedia_62_M8_RELEASE_2026-10-28.zip"
PREFIX = "m8_release_2026-10-28/"
STATUS = "M8_RELEASE_CANDIDATE_AWAITING_OWNER_ACCEPTANCE"

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def metadata_map() -> dict:
    data = json.loads(METADATA.read_text(encoding="utf-8"))
    if data.get("scope") != "metadata_only_no_decklist_changes" or len(data["decks"]) != 6:
        raise ValueError("Six-deck owner-approved metadata reconciliation missing")
    result = {}
    for row in data["decks"]:
        name = row["commander"]
        if name in result or row["power_bracket"] != 4 or len(row["archidekt_tags"]) != 3:
            raise ValueError("Duplicate or incomplete six-deck metadata")
        result[name] = row
    return result

def payloads() -> dict[str, bytes]:
    result = review.files_for_review()
    index = json.loads(result["index.json"])
    summary = json.loads(result["M8_EVIDENCE_SUMMARY.json"])
    sources = {x["id"]: x for x in read_current()}
    changes = metadata_map()
    used = set()
    for row in index["decks"]:
        name = row["commander"]
        if name in changes:
            info = changes[name]
            row["power_bracket"] = "4 — Optimized"
            row["archidekt_tags"] = info["archidekt_tags"]
            row["metadata_provenance"] = str(METADATA.relative_to(ROOT))
            used.add(name)
        if not row.get("power_bracket") or len(row.get("archidekt_tags") or []) != 3:
            raise ValueError(f"Missing power bracket or 3 Archidekt tags: {name}")
        raw = result[row["archive_source"]]
        if digest(raw) != sources[row["deck_id"]]["sha256"]:
            raise ValueError(f"Approved deck source mismatch: {name}")
        if digest(result[row["archidekt_file"]]) != row["archidekt_sha256"]:
            raise ValueError(f"Archidekt import content mismatch: {name}")
    if used != set(changes) or len(index["decks"]) != 62:
        raise ValueError("Metadata reconciliation must match exactly six of 62 deck records")
    if len({r["deck_id"] for r in index["decks"]}) != 62:
        raise ValueError("Duplicate deck entry")
    index["status"] = STATUS
    index["metadata_gaps"] = []
    index["metadata_reconciliation_path"] = str(METADATA.relative_to(ROOT))
    index["release_blockers"] = [
        "Exact-source and evidence M8 acceptance must be recorded in a separate owner receipt",
        "Existing project-only exceptions must not be described as officially Commander legal",
    ]
    index["m8_owner_acceptance"] = None
    summary["status"] = STATUS
    summary["missing_bracket_or_tag_metadata"] = []
    summary["m8_owner_acceptance"] = None
    result["index.json"] = review.encode(index)
    result["M8_EVIDENCE_SUMMARY.json"] = review.encode(summary)
    result["README.txt"] = (
        "GRIXIS COMMANDER ENCYCLOPEDIA — M8 EXACT-SOURCE RELEASE CANDIDATE\n"
        "=============================================================\n"
        "62/62 approved physical lists preserved byte-for-byte; 62 Archidekt imports.\n"
        "180/180 original P1 cases accounted for, including 12 superseded cases.\n"
        "62/62 commander-first attestations. All power brackets and 3 tags/deck present.\n"
        "Six historically missing export metadata entries resolved from approval records.\n"
        "Project-only banned/future cards are documented, not officially legal.\n"
        "OWNER ACCEPTANCE IS SEPARATE: this artifact itself is not signed.\n"
    ).encode("utf-8")
    if len(result) != 129:
        raise ValueError("Expected exactly 129 archive members")
    return result

def check_archive() -> str:
    if not ARCHIVE.is_file():
        raise FileNotFoundError(ARCHIVE)
    report, register, decks = review.state()
    expected = payloads()
    with zipfile.ZipFile(ARCHIVE) as z:
        actual = z.namelist()
        if len(actual) != 129 or len(set(actual)) != 129:
            raise ValueError("Incorrect or duplicate archive members")
        if set(actual) != {PREFIX + n for n in expected}:
            raise ValueError("Archive member identity mismatch")
        for name, raw in expected.items():
            if z.read(PREFIX + name) != raw:
                raise ValueError(f"Archive content mismatch: {name}")
        manifest = json.loads(z.read(PREFIX + "index.json"))
        if (manifest["metadata_gaps"] or manifest["m8_owner_acceptance"] is not None
                or manifest["release_fingerprint"] != report["release_fingerprint"]
                or manifest["evidence_fingerprint"] != report["evidence_fingerprint"]):
            raise ValueError("Stale metadata or incorrectly signed archive")
    archive_sha = digest(ARCHIVE.read_bytes())
    verify_final_archive(str(ARCHIVE.relative_to(ROOT)), archive_sha, decks)
    print(f"M8_RELEASE_CANDIDATE_VERIFIED decks=62 cases=180 quality=62 metadata_gaps=0 owner_unsigned=1 sha256={archive_sha}")
    return archive_sha

def build() -> None:
    if ARCHIVE.exists():
        raise FileExistsError("Refusing to replace an existing release artifact")
    contents = payloads()
    with zipfile.ZipFile(ARCHIVE, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(contents.items()):
            info = zipfile.ZipInfo(PREFIX + name, date_time=(2026, 10, 28, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    check_archive()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--build", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.build:
        build()
    else:
        check_archive()
