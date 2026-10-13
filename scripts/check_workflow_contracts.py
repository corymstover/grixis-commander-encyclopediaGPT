#!/usr/bin/env python3
"""Check critical automation contracts to catch trigger/path drift."""
from pathlib import Path
import fnmatch
import sys
ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/refresh-scryfall-metadata.yml"
REQUEST_DIR = ROOT / "refinement/metadata_audit"
REQUEST_GLOB = "refinement/metadata_audit/REFRESH_REQUEST*.md"
SCRIPT = ROOT / "scripts/refresh_scryfall_metadata.py"
VALIDATOR = ROOT / "scripts/validate_scryfall_metadata_refresh.py"
TRACKER_CHECK = ROOT / "scripts/check_tracker_integrity.py"
QUALITY_WORKFLOW = ROOT / ".github/workflows/verify-baseline.yml"

def main() -> int:
    errors = []
    wf = WORKFLOW.read_text(encoding="utf-8")
    script = SCRIPT.read_text(encoding="utf-8")
    request_files = sorted(p.relative_to(ROOT).as_posix() for p in REQUEST_DIR.glob("REFRESH_REQUEST*.md") if p.is_file())
    if not request_files:
        errors.append(f"no refresh request files found under {REQUEST_DIR.relative_to(ROOT)}")
    if REQUEST_GLOB not in wf:
        errors.append(f"refresh workflow must watch the dated request glob {REQUEST_GLOB}")
    if REQUEST_GLOB not in QUALITY_WORKFLOW.read_text(encoding="utf-8"):
        errors.append(f"quality workflow push/PR filters must watch the dated request glob {REQUEST_GLOB}")
    if not any(fnmatch.fnmatchcase(path, REQUEST_GLOB) for path in request_files):
        errors.append(f"no existing refresh request file matches {REQUEST_GLOB}")
    for fragment in ("workflow_dispatch:", "schedule:", "concurrency:", "timeout-minutes:"):
        if fragment not in wf:
            errors.append(f"refresh workflow missing required control: {fragment}")
    for filename in ("Current_Scryfall_Metadata_Overlay.csv", "Current_Scryfall_Metadata_Audit_Summary.json"):
        if filename not in script or filename not in wf:
            errors.append(f"canonical current-output path is not shared by script/workflow: {filename}")
    if "validate_scryfall_metadata_refresh.py" not in wf:
        errors.append("refresh workflow does not execute the freshness validator")
    validator_start = wf.find("- name: Validate snapshot freshness and completeness")
    abaddon_start = wf.find("- name: Audit Abaddon's exact 94-name frozen list")
    if validator_start < 0 or abaddon_start < 0 or abaddon_start <= validator_start:
        errors.append("refresh validator must precede the Abaddon exact-list audit")
    else:
        validator_block = wf[validator_start:abaddon_start]
        if "if: success()" not in validator_block:
            errors.append("refresh validator must run only after the current refresh step succeeds")
        if 'RUN_STARTED_AT: ${{ github.run_started_at }}' not in validator_block:
            errors.append("refresh validator is not anchored to the current workflow start time")
        if '--not-before-utc "$RUN_STARTED_AT"' not in validator_block:
            errors.append("freshness validator is not rejecting snapshots predating this run")
    preflight_start = wf.find("- name: Verify frozen 62-deck baseline before metadata download")
    refresh_start = wf.find("- name: Refresh all 62 frozen decklists from current Scryfall bulk")
    if preflight_start < 0 or refresh_start < 0 or preflight_start >= refresh_start:
        errors.append("frozen-baseline verification must run before the large Scryfall download")
    if "scripts/verify_baseline.py" not in wf:
        errors.append("refresh workflow does not verify the source archive before downloading metadata")
    if "audit_abaddon_baseline_metadata.py" not in wf:
        errors.append("refresh workflow does not run the Abaddon exact-name audit")
    if "upload-artifact@v4" not in wf:
        errors.append("refresh workflow does not preserve run diagnostics")
    if not VALIDATOR.is_file():
        errors.append("refresh validator script is missing")
    if not TRACKER_CHECK.is_file():
        errors.append("tracker integrity checker is missing")
    if "check_tracker_integrity.py" not in QUALITY_WORKFLOW.read_text(encoding="utf-8"):
        errors.append("fast quality workflow does not run tracker integrity validation")
    if errors:
        print("FAIL: automation contract mismatch", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: watched path, weekly/manual triggers, concurrency, current-run freshness gate, Abaddon audit, tracker integrity and diagnostics are wired.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
