"""Owner-authorized Deck #30 M7 Rev1 100-card exact SHA canonical lock.

Historical October 14 artifacts are deliberately preserved; the separate
engineering Stage A mismatch annotation does not confer independent review.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = "Lord_Xander__the_Collector"
SHA = "de348618961269083a44a3f3e05a7f0be7ddbd7e943da0ac82a115e5e4aeb6cd"
OLD = "92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787"
PATH = "refinement/decklists/Lord_Xander_the_Collector_M7_Rev1_Approved_2026-10-25.txt"
OLD_PATH = "refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt"
ORACLE = "refinement/verification/Lord_Xander_the_Collector_M7_Rev1_Oracle_Identity_Index_2026-10-25.json"
RECEIPT = "refinement/approvals/Lord_Xander_the_Collector_M7_Rev1_Approved_2026-10-25.md"
ATTEST = "refinement/verification/m7_certification_transfer/Lord_Xander__the_Collector_de34861896126908.json"
SWAPS = {
    "Hellkite Courser": "Lion's Eye Diamond",
    "Syr Konrad, the Grim": "Brain Freeze",
    "Necromancy": "Underworld Breach",
    "Bloodchief Ascension": "Maddening Cacophony",
    "Irenicus's Vile Duplication": "Notion Thief",
    "Goryo's Vengeance": "Orcish Bowmasters",
    "Samut, Hazoret's Champion": "Pact of Negation",
    "Malakir Rebirth // Malakir Mire": "Force of Negation",
    "Swiftfoot Boots": "Lightning Greaves",
}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def parse(path):
    entries = []
    for line in (ROOT / path).read_text().splitlines():
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, line
        entries.append((int(m[1]), m[2], bool(m[3])))
    return entries, Counter({name: count for count, name, _ in entries})


class XanderM7Rev1Canonical(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.counts = parse(PATH)
        _, cls.old = parse(OLD_PATH)
        cls.cards = json.loads((ROOT / ORACLE).read_text())
        cls.selected = {x["name"]: x for x in cls.cards["cards"]}
        cls.state = json.loads((ROOT / "state/current_deck_overrides.json").read_text())["decks"][DECK]
        cls.transfer = json.loads((ROOT / ATTEST).read_text())
        with (ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv").open(newline="") as f:
            cls.tracker = {row["deck_id"]: row for row in csv.DictReader(f)}[DECK]

    def test_owner_approved_raw_exact_and_prior_untouched(self):
        self.assertEqual(sha(PATH), SHA)
        self.assertEqual(sha(OLD_PATH), OLD)
        self.assertEqual(self.cards["approved_candidate_raw_sha256"], SHA)
        self.assertIn("I approve Deck #30 Lord Xander M7 Rev1", (ROOT / RECEIPT).read_text())
        self.assertIn(SHA, (ROOT / RECEIPT).read_text())
        self.assertIn("preserving original evidence", (ROOT / RECEIPT).read_text())
        self.assertTrue((ROOT / PATH).read_bytes().endswith(b"\n"))

    def test_exact_100_singleton_and_nine_one_for_one_swaps(self):
        self.assertEqual(self.entries[0], (1, "Lord Xander, the Collector", True))
        self.assertEqual(sum(q for q, _, _ in self.entries), 100)
        self.assertEqual(len(self.counts), 97)
        self.assertEqual(sum(int(is_commander) for _, _, is_commander in self.entries), 1)
        self.assertEqual({k: v for k, v in self.counts.items() if v > 1},
                         {"Island": 2, "Mountain": 2, "Swamp": 2})
        self.assertEqual(self.counts - self.old, Counter({name: 1 for name in SWAPS}))
        self.assertEqual(self.old - self.counts, Counter({name: 1 for name in SWAPS.values()}))
        self.assertEqual(len(SWAPS), 9)
        for keep in ["Hall of Echoes", "Persist", "Bojuka Bog", "Karlach, Fury of Avernus",
                     "Sword of Feast and Famine", "Aggravated Assault", "Riverchurn Monument"]:
            self.assertEqual(self.counts[keep], 1, keep)
        self.assertEqual([name for _, name, _ in self.entries[1:]],
                         sorted([name for _, name, _ in self.entries[1:]], key=str.casefold))

    def test_current_oracle_legality_grixis_and_distinct_copy(self):
        self.assertEqual(self.cards["physical_cards"], 100)
        self.assertEqual(self.cards["distinct_names"], 97)
        self.assertEqual(set(self.selected), set(self.counts))
        self.assertEqual(self.cards["project_exceptions"], [])
        self.assertTrue(self.cards["all_selected_currently_commander_legal"])
        self.assertTrue(self.cards["all_selected_grixis_identity_or_colorless"])
        for name, x in self.selected.items():
            self.assertEqual(x["quantity"], self.counts[name], name)
            self.assertEqual(x["commander_legality"], "legal", name)
            self.assertTrue(set(x["color_identity"]).issubset(set("UBR")), name)
            self.assertTrue(x["oracle_id"], name)
            self.assertTrue(x["scryfall_uri"].startswith("https://scryfall.com/card/"), name)
        self.assertEqual(sum(x["game_changer"] for x in self.selected.values()), 16)
        self.assertIn("nonlegendary creature", self.selected["Persist"]["oracle_text"])
        self.assertIn("command zone", self.selected["Hellkite Courser"]["oracle_text"])
        self.assertIn("three or more quest counters", self.selected["Bloodchief Ascension"]["oracle_text"])
        self.assertIn("isn't legendary", self.selected["Irenicus's Vile Duplication"]["oracle_text"])

    def test_tracker_only_exact_active_lock(self):
        self.assertEqual(self.tracker["final_list_hash"], SHA)
        self.assertEqual(self.tracker["user_approval_date"], "2026-10-25")
        self.assertEqual(self.tracker["final_gate_passed"], "YES")
        self.assertIn("APPROVED / LOCKED", self.tracker["refinement_status"])
        self.assertEqual(self.state["approved_list_sha256"], SHA)
        self.assertEqual(self.state["approved_list_artifact"], PATH)
        self.assertEqual(self.state["previous_approved_list_sha256"], OLD)
        self.assertEqual(self.state["previous_approved_list_artifact"], OLD_PATH)
        self.assertEqual(self.state["lock_status"], "LOCKED")
        self.assertEqual(self.state["m7_archidekt_tags"], ["Mill", "Clones", "Reanimation"])
        self.assertEqual(self.state["m7_power_bracket"], "4 — Optimized")
        self.assertEqual(self.state["m7_m6_certification_transfer_artifact"], ATTEST)

    def test_exact_head_all_14_cases_and_pinned_nonindependent_source(self):
        self.assertEqual(self.transfer["approved_raw_sha256"], SHA)
        self.assertEqual(self.transfer["engineering"]["head_sha"],
                         "fcff8a8a4aa184c144daaaab4f12974d7ed486d4")
        self.assertEqual(self.transfer["engineering"]["pr_url"],
                         "https://github.com/corymstover/GrokBotMTGCompanion/pull/708")
        self.assertEqual(self.transfer["m6_transfer"]["ij_scope"], "TRANSFERRED_WITH_CASE_MAPPING")
        self.assertIn("technically_independent=false", self.transfer["engineering"]["independent_review_ref"])
        self.assertIn("PR #709", self.transfer["m6_transfer"]["revision_diff_and_validity_reason"])
        self.assertEqual(len(self.transfer["m6_transfer"]["P0"]), 5)
        self.assertEqual(len(self.transfer["m6_transfer"]["P1"]), 9)
        self.assertEqual({x["case_id"] for x in self.transfer["m6_transfer"]["P0"]},
                         {"C1", "K1", "K2", "K3", "F1"})
        self.assertEqual({x["case_id"] for x in self.transfer["m6_transfer"]["P1"]},
                         {"K4", "K5", "E1", "E2", "W1", "W2", "W3", "F2", "F3"})
        for case in self.transfer["m6_transfer"]["P0"] + self.transfer["m6_transfer"]["P1"]:
            self.assertEqual(case["status"], "PASSED")
            self.assertEqual(case["tested_raw_sha256"], SHA)
            self.assertEqual(case["scope"], "EXACT_APPROVED_100")
            self.assertEqual(case["ci_run_url"],
                             "https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40185256873")


if __name__ == "__main__":
    unittest.main()
