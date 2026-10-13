#!/usr/bin/env python3
"""Check critical automation contracts to catch trigger/path drift."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/refresh-scryfall-metadata.yml"
REQUEST = ROOT / "refinement/metadata_audit/REFRESH_REQUEST.md"
SCRIPT = ROOT / "scripts/refresh_scryfall_metadata.py"
VALIDATOR = ROOT / "scripts/validate_scryfall_metadata_refresh.py"

def main() -> int:
    errors = []
    wf = WORKFLOW.read_text(encoding="utf-8")
    script = SCRIPT.read_text(encoding="utf-8")
    if not REQUEST.is_file():
        errors.append(f"watched request path is missing: {REQUEST.relative_to(ROOT)}")
    rel = REQUEST.relative_to(ROOT).as_posix()
    if rel not in wf:
        errors.append(f"workflow path filter does not watch {rel}")
    for fragment in ("workflow_dispatch:", "schedule:", "concurrency:", "timeout-minutes:"):
        if fragment not in wf:
            errors.append(f"refresh workflow missing required control: {fragment}")
    for filename in ("Current_Scryfall_Metadata_Overlay.csv", "Current_Scryfall_Metadata_Audit_Summary.json"):
        if filename not in script or filename not in wf:
            errors.append(f"canonical current-output path is not shared by script/workflow: {filename}")
    if "validate_scryfall_metadata_refresh.py" not in wf:
        errors.append("refresh workflow does not execute the freshness validator")
    if "audit_abaddon_baseline_metadata.py" not in wf:
        errors.append("refresh workflow does not run the Abaddon exact-name audit")
    if "upload-artifact@v4" not in wf:
        errors.append("refresh workflow does not preserve run diagnostics")
    if not VALIDATOR.is_file():
        errors.append("refresh validator script is missing")
    if errors:
        print("FAIL: automation contract mismatch", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: watched path, weekly/manual triggers, concurrency, stable outputs, freshness gate, Abaddon audit, and diagnostics are wired.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
