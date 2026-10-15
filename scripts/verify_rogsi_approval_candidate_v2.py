#!/usr/bin/env python3
"""Normalize comma-bearing RogSi ledger card names, then run the fail-closed verifier.

The initial human-authored CSV left three comma-bearing card names unquoted.
Only CSV serialization is repaired here; deck membership, decisions, and reasons
are unchanged. The underlying candidate verifier remains authoritative.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ledger = ROOT / "refinement/decisions/RogSi_Whole_List_Decision_Ledger_2026-10-15.csv"
text = ledger.read_text(encoding="utf-8")
repairs = {
    "Otawara, Soaring City,KEEP,": '"Otawara, Soaring City",KEEP,',
    "Ragavan, Nimble Pilferer,KEEP,": '"Ragavan, Nimble Pilferer",KEEP,',
    "Samut, Tyrant of Naktamun,KEEP,": '"Samut, Tyrant of Naktamun",KEEP,',
}
for old, new in repairs.items():
    if old in text:
        text = text.replace(old, new, 1)
ledger.write_text(text, encoding="utf-8")

source_path = Path(__file__).with_name("verify_rogsi_approval_candidate_once.py")
source = source_path.read_text(encoding="utf-8")
namespace = {
    "__name__": "__main__",
    "__file__": str(source_path),
    "__package__": None,
}
exec(compile(source, str(source_path), "exec"), namespace)
