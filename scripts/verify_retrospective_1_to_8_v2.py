#!/usr/bin/env python3
"""Parser-hardening shim for verify_retrospective_1_to_8.py."""
from __future__ import annotations

import re
from pathlib import Path
import verify_retrospective_1_to_8 as base

ROLE_RE = re.compile(r"\s+\[([^\]]+)\]\s*$")
QTY_RE = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
# Source-format exports: Name (set) collector, optionally with a *tag* before the role.
PRINTING_RE = re.compile(r"^(.+?)\s+\([^()]+\)\s+\S+(?:\s+\*[^*]+\*)?\s*$")


def parse_deck(path: Path):
    rows = []
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    for line_no, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        role_match = ROLE_RE.search(line)
        role = role_match.group(1) if role_match else ""
        core = ROLE_RE.sub("", line).strip()
        qty_match = QTY_RE.match(core)
        if not qty_match:
            raise RuntimeError(f"Malformed deck line {path}:{line_no}: {line}")
        qty = int(qty_match.group(1))
        remainder = qty_match.group(2).strip()
        printing = PRINTING_RE.match(remainder)
        name = printing.group(1).strip() if printing else remainder
        rows.append({"line_no": line_no, "quantity": qty, "card_name": name, "role": role})
    return raw, rows


base.parse_deck = parse_deck
base.main()
