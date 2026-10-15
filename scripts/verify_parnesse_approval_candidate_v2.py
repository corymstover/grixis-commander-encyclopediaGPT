#!/usr/bin/env python3
"""Run the Parnesse approval verifier with front-face land-slot counting.

The original verifier treated any combined DFC type line containing "Land" as a
land slot, which incorrectly counted Primal Amulet // Primal Wellspring as a
land. Commander deck construction uses the card's front face for this
human-facing land-count metric, so only the first type-line component is tested.
All other fail-closed checks remain byte-for-byte the original verifier logic.
"""
from pathlib import Path

source_path = Path(__file__).with_name("verify_parnesse_approval_candidate_once.py")
source = source_path.read_text(encoding="utf-8")
old = 'if "Land" in (rec.get("type_line") or ""):'
new = 'if "Land" in (rec.get("type_line") or "").split(" // ", 1)[0]:'
if old not in source:
    raise SystemExit("Expected original Parnesse land-count expression not found")
source = source.replace(old, new, 1)
namespace = {
    "__name__": "__main__",
    "__file__": str(source_path),
    "__package__": None,
}
exec(compile(source, str(source_path), "exec"), namespace)
