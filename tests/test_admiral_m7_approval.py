"""Guard Cory's exact Admiral Beckett Brass M7 owner approval and immutable predecessor."""
import csv
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = "Admiral_Beckett_Brass"
FINAL = ROOT / "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt"
PRIOR = ROOT / "refinement/decklists/Admiral_Beckett_Brass_Approval_Ready_2026-10-13.txt"
EXPECTED = "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000"
PRIOR_HASH = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
ADDS = {
    "City of Brass", "Departed Deckhand", "Cloud Pirates",
    "Skyship Plunderer", "Broadside Bombardiers", "Cosmotronic Wave",
}
CUTS = {
    "Crumbling Necropolis", "Daring Saboteur", "Dire Fleet Captain",
    "Dire Fleet Poisoner", "Forerunner of the Coalition", "Raise the Palisade",
}


def cards(path):
    out = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        count, name = line.split("x ", 1)
        out[name.removesuffix(" [Commander]")] += int(count)
    return lines, out


class AdmiralM7ApprovalTests(unittest.TestCase):
    def test_exact_source_hash_and_full_physical_deck(self):
        self.assertEqual(hashlib.sha256(FINAL.read_bytes()).hexdigest(), EXPECTED)
        lines, counts = cards(FINAL)
        self.assertEqual(lines[0], "1x Admiral Beckett Brass [Commander]")
        self.assertEqual(len(lines), 97)
        self.assertEqual(sum(counts.values()), 100)
        self.assertEqual(counts["Admiral Beckett Brass"], 1)
        self.assertEqual(len(counts), 97)
        self.assertTrue(all(n == 1 or card in {"Island", "Mountain", "Swamp"}
                            for card, n in counts.items()))

    def test_precisely_six_strategic_replacements_from_preserved_source(self):
        self.assertEqual(hashlib.sha256(PRIOR.read_bytes()).hexdigest(), PRIOR_HASH)
        _, original = cards(PRIOR)
        _, approved = cards(FINAL)
        self.assertEqual(set((approved - original).elements()), ADDS)
        self.assertEqual(set((original - approved).elements()), CUTS)
        self.assertEqual(sum((approved - original).values()), 6)
        self.assertEqual(sum((original - approved).values()), 6)

    def test_registry_and_tracker_bind_exact_owner_approval(self):
        state = json.loads((ROOT / "state/current_deck_overrides.json").read_text(encoding="utf-8"))
        record = state["decks"][DECK]
        self.assertEqual(record["approved_list_sha256"], EXPECTED)
        self.assertEqual(record["previous_approved_list_sha256"], PRIOR_HASH)
        self.assertEqual(record["approval_status"], "APPROVED")
        self.assertEqual(record["lock_status"], "LOCKED")
        self.assertEqual(record["user_approval_date"], "2026-10-22")
        self.assertEqual(record["approved_list_artifact"], str(FINAL.relative_to(ROOT)))
        self.assertEqual(record["m7_final_candidate_sha256"], EXPECTED)
        self.assertEqual(len(state["decks"]), 62)
        self.assertEqual(sum(v["approval_status"] == "APPROVED" and
                             v["lock_status"] == "LOCKED"
                             for v in state["decks"].values()), 62)
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 62)
        row = next(r for r in rows if r["deck_id"] == DECK)
        self.assertEqual(row["final_list_hash"], EXPECTED)
        self.assertEqual(row["user_approval_date"], "2026-10-22")

    def test_owner_receipt_scope(self):
        receipt = (ROOT / "refinement/approvals/Admiral_Beckett_Brass_M7_Approved_2026-10-22.md").read_text(encoding="utf-8")
        self.assertIn(EXPECTED, receipt)
        self.assertIn("Approved", receipt)
        self.assertIn("M6.10", receipt)
        evidence = (ROOT / "refinement/verification/Admiral_Beckett_Brass_M7_Approval_Verification_2026-10-22.md").read_text(encoding="utf-8")
        self.assertIn(EXPECTED, evidence)


if __name__ == "__main__":
    unittest.main()
