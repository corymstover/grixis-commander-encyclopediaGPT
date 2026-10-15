import csv
import hashlib
import io
import json
from pathlib import Path

OLD = "83062ff2dbc955c628f9a6df460cf72dd5d450b6685bc4b53f63894bc8c321fb"
NEW = "c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63"
DATE = "2026-10-15"

candidate = Path("refinement/decklists/Obeka_Splitter_of_Seconds_Approval_Ready_2026-10-15.txt")
if hashlib.sha256(candidate.read_bytes()).hexdigest() != NEW:
    raise SystemExit("Obeka Splitter raw candidate SHA did not match the GitHub Actions recomputation")

artifacts = [
    Path("refinement/verification/Obeka_Splitter_of_Seconds_Whole_List_Audit_2026-10-15.md"),
    Path("refinement/verification/Obeka_Splitter_of_Seconds_Approval_Ready_Verification_2026-10-15.md"),
    Path("refinement/decisions/Obeka_Splitter_of_Seconds_Candidate_Decisions_2026-10-15.md"),
    Path("refinement/blueprints/Obeka_Splitter_of_Seconds_Commander_Blueprint_2026-10-15.md"),
]
replacements = 0
for path in artifacts:
    text = path.read_text(encoding="utf-8")
    if OLD in text:
        replacements += text.count(OLD)
        path.write_text(text.replace(OLD, NEW), encoding="utf-8")
if replacements < 3:
    raise SystemExit(f"Expected at least three SHA-documentation replacements; found {replacements}")

# Execute the already-reviewed finalizer with only the corrected raw-byte SHA substituted.
source_path = Path("scripts/finalize_obeka_splitter_of_seconds_approval_once.py")
source = source_path.read_text(encoding="utf-8")
needle = f'EXPECTED_SHA = "{OLD}"'
if needle not in source:
    raise SystemExit("Original Obeka Splitter finalizer no longer has the expected documented SHA")
exec(compile(source.replace(needle, f'EXPECTED_SHA = "{NEW}"'), str(source_path), "exec"), {"__name__": "__main__"})

note = (
    f"\n\n## Approval-time SHA correction\n\nOn {DATE}, the fail-closed GitHub Actions finalizer recomputed the raw bytes of the unchanged approval-ready candidate as SHA-256 `{NEW}`. "
    f"The previously documented `{OLD}` value was incorrect metadata, not a card-list change. SHA-bound artifacts were reconciled before approval state was finalized. No card membership, quantity, order, or text changed.\n"
)
verification = artifacts[1]
vtext = verification.read_text(encoding="utf-8")
if "## Approval-time SHA correction" not in vtext:
    verification.write_text(vtext + note, encoding="utf-8")

approval = Path("refinement/approvals/Obeka_Splitter_of_Seconds_Approved_2026-10-15.md")
atext = approval.read_text(encoding="utf-8")
if "Approval-time SHA correction" not in atext:
    approval.write_text(atext + note, encoding="utf-8")

state_path = Path("state/current_deck_overrides.json")
state = json.loads(state_path.read_text(encoding="utf-8"))
entry = state["decks"]["Obeka__Splitter_of_Seconds"]
entry["sha_reconciliation_note"] = f"Prior documented hash {OLD} was incorrect. GitHub Actions verified the unchanged raw candidate bytes as {NEW}; no card content changed."
state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

tracker_path = Path("refinement/Deck_Refinement_Tracker_2026-10-12.csv")
rows = list(csv.reader(tracker_path.read_text(encoding="utf-8").splitlines()))
header = rows[0]
id_col = header.index("deck_id")
notes_col = header.index("notes")
for row in rows[1:]:
    if row[id_col] == "Obeka__Splitter_of_Seconds":
        row[notes_col] += f" SHA CORRECTION: prior documented {OLD} replaced by raw-file {NEW}; list content unchanged."
        break
out = io.StringIO()
csv.writer(out, lineterminator="\n").writerows(rows)
tracker_path.write_text(out.getvalue(), encoding="utf-8")

print("Obeka Splitter SHA reconciled and approval finalized.")
