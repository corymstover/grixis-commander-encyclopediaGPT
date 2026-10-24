"""Exact Fire Lord Azula M7 Rev2 approved owner SHA; archived Oracle and 18 prior locks.

The archived card snapshot is October 23, 2026. It is NOT presented as
real-time October 24 Scryfall, a full multiplayer rules engine, or a win-rate model.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt"
BASELINE = ROOT / "refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Fire_Lord_Azula_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.md"
VERIFICATION = ROOT / "refinement/verification/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SHA = "77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273"
OLD = "b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5"
DECK_ID = "Fire_Lord_Azula"
SWAPS = [
    ("Turnabout", "Samut, Tyrant of Naktamun"),
    ("Sink into Stupor // Soporific Springs", "Exotic Orchard"),
    ("Samut, Hazoret's Champion", "Vivi Ornitier"),
    ("Flashback", "Repeal"),
    ("Electrodominance", "Redirect Lightning"),
]
PROTECTED = {"Swan Song", "Gemstone Caverns", "Big Score", "Hexing Squelcher", "Wooded Foothills",
             "Narset's Reversal", "Frantic Search", "Beseech the Mirror", "Tainted Pact", "Demonic Consultation",
             "Thassa's Oracle", "Underworld Breach", "Brain Freeze", "Lion's Eye Diamond"}
PRIOR_18 = {
  "Abaddon_the_Despoiler": [
    "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
    "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"
  ],
  "Admiral_Beckett_Brass": [
    "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
    "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt"
  ],
  "Admiral_Brass__Unsinkable": [
    "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
    "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"
  ],
  "Anhelo_the_Painter": [
    "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
    "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Ashad_the_Lone_Cyberman": [
    "352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
    "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"
  ],
  "Ashnod_the_Uncaring": [
    "a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
    "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Be_lakor_the_Dark_Master": [
    "2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
    "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Cecily__Bjorna__Lutri": [
    "e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d",
    "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Cormela__Glamour_Thief": [
    "d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd",
    "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Crosis__the_Purger": [
    "a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a",
    "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Cult_of_Skaro": [
    "e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d",
    "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Davros__Dalek_Creator": [
    "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc",
    "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Doctor_Doom__King_of_Latveria": [
    "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20",
    "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Don_Andres__the_Renegade": [
    "59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f",
    "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Dr__Eggman": [
    "3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec",
    "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Edea__Possessed_Sorceress": [
    "a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54",
    "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Edward_Kenway": [
    "8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1",
    "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt"
  ],
  "Evelyn__the_Covetous": [
    "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac",
    "refinement/decklists/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.txt"
  ]
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cards_from(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    counts = Counter()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, (i, line)
        quantity, name, tag = int(m[1]), m[2], m[3]
        if i == 0:
            assert (quantity, name, bool(tag)) == (1, "Fire Lord Azula", True)
        else:
            assert tag is None, line
        counts[name] += quantity
    return lines, counts


class FireLordAzulaM7Rev2OwnerApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.cards = cards_from(APPROVED)
        _, cls.old = cards_from(BASELINE)
        cls.snapshot = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in cls.snapshot["cards"]}
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        with TRACKER.open(newline="", encoding="utf-8") as stream:
            cls.tracker = list(csv.DictReader(stream))

    def test_exact_bytes_and_immutable_previous_approval(self):
        self.assertEqual(digest(APPROVED), SHA)
        self.assertEqual(digest(BASELINE), OLD)
        self.assertEqual(self.snapshot["candidate_raw_sha256"], SHA)
        self.assertEqual(self.snapshot["baseline_raw_sha256"], OLD)
        self.assertIn(SHA, RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(SHA, VERIFICATION.read_text(encoding="utf-8"))

    def test_singleton_100_and_owner_approved_swaps(self):
        self.assertEqual(len(self.rows), 100)
        self.assertEqual(sum(self.cards.values()), 100)
        self.assertEqual(len(self.cards), 100)
        self.assertTrue(all(q == 1 for q in self.cards.values()))
        self.assertEqual(set(self.cards) - set(self.old), {a for a,_ in SWAPS})
        self.assertEqual(set(self.old) - set(self.cards), {c for _,c in SWAPS})
        self.assertTrue(PROTECTED <= set(self.cards))
        self.assertNotIn("Mistrise Village", self.cards)  # Deliberately rejected sixth.

    def test_archive_oracle_rules_legality_and_ubr(self):
        self.assertEqual(self.snapshot["status"], "CORY_APPROVED_FIRE_LORD_AZULA_M7_REV2_CANONICAL_SOURCE_BOUND")
        self.assertEqual(self.snapshot["physical_cards"], 100)
        self.assertEqual(self.snapshot["distinct_names"], 100)
        self.assertEqual(set(self.cards), set(self.oracle))
        self.assertEqual(len(self.snapshot["cards"]), 100)
        self.assertEqual(sum("Land" in self.oracle[n]["type_line"] for n in self.cards), 26)
        self.assertEqual(sum(bool(self.oracle[n]["game_changer"]) for n in self.cards), 20)
        self.assertEqual(self.snapshot["project_exceptions"], [])
        for name, q in self.cards.items():
            c = self.oracle[name]
            self.assertEqual(c["quantity"], q)
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            self.assertTrue(c["oracle_id"], name)

    def test_critical_azula_mechanical_boundaries(self):
        text = lambda n: self.oracle[n]["oracle_text"]
        self.assertIn("Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell", text("Fire Lord Azula"))
        self.assertIn("Firebending 2", text("Fire Lord Azula"))
        self.assertEqual(self.oracle["Electrodominance"]["mana_cost"], "{X}{R}{R}")
        self.assertIn("deals X damage to any target", text("Electrodominance"))
        self.assertIn("cast a spell with mana value X or less from your hand without paying its mana cost", text("Electrodominance"))
        self.assertIn("copy target instant or sorcery spell", text("Narset's Reversal").lower())
        self.assertIn("untap all tapped permanents", text("Turnabout"))
        self.assertIn("Creatures you control have haste", text("Samut, Hazoret's Champion"))
        self.assertIn("gains flashback until end of turn", text("Flashback"))
        self.assertIn("pay 3 life", text("Sink into Stupor // Soporific Springs"))
        self.assertIn("lose life equal to its mana value", text("Ad Nauseam"))
        self.assertIn("create two Treasure tokens", text("Big Score"))
        self.assertNotIn("Samut, Tyrant of Naktamun", self.cards)

    def test_owner_registry_and_tracker_match_exact_raw_approval(self):
        self.assertEqual(len(self.registry["decks"]), 62)
        e = self.registry["decks"][DECK_ID]
        self.assertEqual((e["approval_status"], e["lock_status"], e["current_stage"]),
                         ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(e["final_gate_passed"])
        self.assertEqual(e["approved_list_sha256"], SHA)
        self.assertEqual(e["m7_final_candidate_sha256"], SHA)
        self.assertEqual(e["previous_approved_source_raw_sha256"], OLD)
        self.assertEqual(e["previous_approved_list_artifact"], str(BASELINE.relative_to(ROOT)))
        self.assertEqual(e["approved_list_artifact"], str(APPROVED.relative_to(ROOT)))
        self.assertEqual(e["user_approval_date"], "2026-10-24")
        self.assertEqual(e["m7_power_bracket"], "5 — cEDH")
        self.assertEqual(e["m7_archidekt_tags"], ["Combat-Flash", "Spell Copy", "Combo"])
        self.assertEqual(e["m7_project_exceptions"], [])
        self.assertTrue(e["m7_verified_100_physical"])
        self.assertEqual(len(self.tracker), 62)
        t = self.tracker[18]
        self.assertEqual(t["deck_id"], DECK_ID)
        self.assertEqual(t["final_list_hash"], SHA)
        self.assertEqual(t["user_approval_date"], "2026-10-24")
        self.assertEqual(t["final_gate_passed"], "YES")
        self.assertIn("M7 Rev2", t["refinement_status"])

    def test_eighteen_prior_new_cycle_approvals_untouched(self):
        self.assertEqual(len(PRIOR_18), 18)
        for deck_id, (expected_sha, path) in PRIOR_18.items():
            with self.subTest(deck_id=deck_id):
                row = self.registry["decks"][deck_id]
                self.assertEqual(row["approval_status"], "APPROVED")
                self.assertEqual(row["lock_status"], "LOCKED")
                self.assertEqual(row["approved_list_sha256"], expected_sha)
                self.assertEqual(row["approved_list_artifact"], path)
                self.assertEqual(digest(ROOT / path), expected_sha)


if __name__ == "__main__":
    unittest.main()
