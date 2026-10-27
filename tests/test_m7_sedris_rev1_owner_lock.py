#!/usr/bin/env python3
"""Exact Sedris #51 M7 owner lock, not a global 62-deck re-certification."""
import csv
import hashlib
import json
import os
from collections import Counter
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
KEY = "Sedris__the_Traitor_King"
OLD_SHA = "65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365"
NEW_SHA = "b0aa141fe5d27b1e0d0bc804e692d56ae645c74de4bd6777c501b1ae057969da"
ORIGINAL = ROOT / "refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt"
FINAL_REL = "refinement/decklists/Sedris_the_Traitor_King_M7_Rev1_Approved_2026-10-27.txt"
FINAL = ROOT / FINAL_REL
SWAPS = {
    "Ashnod's Altar": "Altar of Dementia",
    "Chainer, Nightmare Adept": "Thassa, Deep-Dwelling",
    "Feldon of the Third Path": "Agadeem's Awakening // Agadeem, the Undercrypt",
    "Gifts Ungiven": "Cephalid Coliseum",
    "Jin-Gitaxias, Core Augur": "Gyruda, Doom of Depths",
    "Likeness Looter": "Careful Study",
    "Sepulchral Primordial": "Agent of Treachery",
    "Sheoldred, Whispering One": "Phyrexian Delver",
    "Windfall": "Intuition",
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def physical(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        n, name = line.split("x ", 1)
        rows.append((int(n), name.removesuffix(" [Commander]")))
    return Counter({name: n for n, name in rows}), rows

class SedrisExactOwnerLock(unittest.TestCase):
    def test_new_and_historical_raw_sha(self):
        self.assertEqual(digest(FINAL), NEW_SHA)
        self.assertEqual(digest(ORIGINAL), OLD_SHA)

    def test_exact_100_singleton_and_all_nine_changes(self):
        prior, prior_rows = physical(ORIGINAL)
        current, rows = physical(FINAL)
        self.assertEqual(rows[0], (1, "Sedris, the Traitor King"))
        self.assertEqual(sum(q for q, _ in rows), 100)
        self.assertEqual(len(rows), 99)
        self.assertEqual(len(current), 99)
        self.assertEqual({n: q for n, q in rows if q > 1}, {"Swamp": 2})
        self.assertEqual(set(prior) - set(current), set(SWAPS))
        self.assertEqual(set(current) - set(prior), set(SWAPS.values()))
        self.assertEqual(set((prior-current).elements()), set(SWAPS))
        self.assertEqual(set((current-prior).elements()), set(SWAPS.values()))

    def test_approved_authority_and_tracker(self):
        data = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        sedris = data["decks"][KEY]
        self.assertEqual(sedris["approved_list_sha256"], NEW_SHA)
        self.assertEqual(sedris["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(sedris["approval_status"], "APPROVED")
        self.assertEqual(sedris["lock_status"], "LOCKED")
        self.assertTrue(sedris["final_gate_passed"])
        self.assertEqual(sedris["approved_list_artifact"], FINAL_REL)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(newline="", encoding="utf-8") as f:
            records = {row["deck_id"]: row for row in csv.DictReader(f)}
        self.assertEqual(records[KEY]["final_list_hash"], NEW_SHA)
        self.assertEqual(records[KEY]["user_approval_date"], "2026-10-27")
        self.assertEqual(records[KEY]["final_gate_passed"], "YES")

    def test_approved_receipts_agree(self):
        s = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))["decks"][KEY]
        for name in ["approval_record_artifact", "verification_artifact"]:
            body = (ROOT / s[name]).read_text(encoding="utf-8")
            self.assertIn(NEW_SHA, body)
            self.assertIn(OLD_SHA, body)
            self.assertIn("40490678017", body)

    def test_other_61_authorities_unchanged_against_pr_base(self):
        base = os.environ.get("BASE_REF_SHA")
        self.assertTrue(base and len(base) == 40, "Require exact PR base SHA")
        before = json.loads(subprocess.check_output(
            ["git", "show", f"{base}:state/current_deck_overrides.json"], cwd=ROOT))
        after = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(set(after["decks"]), set(before["decks"]))
        for name, entry in before["decks"].items():
            if name != KEY:
                self.assertEqual(after["decks"][name], entry, name)

if __name__ == "__main__":
    unittest.main()
