"""Canonical Jeleva M7 Rev1 exact-owner two-swap waiver and lock regression gate."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ID = "Jeleva__Nephalia_s_Scourge"
SHA = "6f2cdafa089c3e923104429f764bed66e500fe20cafb3b00dd4d29488bd52cac"
OLD_SHA = "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f"
NEW = ROOT / "refinement/decklists/Jeleva_Nephalia_s_Scourge_M7_Rev1_Approved_2026-10-24.txt"
OLD = ROOT / "refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt"
RECEIPT = ROOT / "refinement/approvals/Jeleva_Nephalia_s_Scourge_M7_Rev1_Approved_2026-10-24.md"
VERIFY = ROOT / "refinement/verification/Jeleva_Nephalia_s_Scourge_M7_Rev1_Approved_2026-10-24_Verification.md"
INDEX = ROOT / "refinement/verification/Jeleva_Nephalia_s_Scourge_M7_Rev1_Oracle_Identity_Index_2026-10-24.json"
REG = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
ADD = Counter({"Cavern of Souls": 1, "Fire Covenant": 1})
CUT = Counter({"City of Traitors": 1, "Toxic Deluge": 1})
CORE = {"Thassa's Oracle", "Demonic Consultation", "Tainted Pact", "Doomsday",
        "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze", "Mind's Desire",
        "Yawgmoth's Will", "Harmonic Prodigy", "Lightning Greaves", "Torch Courier",
        "Scroll Rack", "Sensei's Divining Top", "Mystical Tutor", "Vampiric Tutor"}
PRIOR23 = {
    "Abaddon_the_Despoiler": "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
    "Admiral_Beckett_Brass": "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
    "Admiral_Brass__Unsinkable": "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
    "Anhelo_the_Painter": "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
    "Ashad_the_Lone_Cyberman": "352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
    "Ashnod_the_Uncaring": "a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
    "Be_lakor_the_Dark_Master": "2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
    "Cecily__Bjorna__Lutri": "e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d",
    "Cormela__Glamour_Thief": "d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd",
    "Crosis__the_Purger": "a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a",
    "Cult_of_Skaro": "e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d",
    "Davros__Dalek_Creator": "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc",
    "Doctor_Doom__King_of_Latveria": "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20",
    "Don_Andres__the_Renegade": "59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f",
    "Dr__Eggman": "3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec",
    "Edea__Possessed_Sorceress": "a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54",
    "Edward_Kenway": "8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1",
    "Evelyn__the_Covetous": "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac",
    "Fire_Lord_Azula": "77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273",
    "Garza_Zol__Plague_Queen": "353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244",
    "Goro_Goro_and_Satoru": "36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c",
    "Gwendlyn_Di_Corci": "36b76cbe47a04b7492007103e4baaad50324b3e72fb2067b28aa8bb9da70e355",
    "Inalla__Archmage_Ritualist": "c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cards(path):
    return path.read_text(encoding="utf-8").splitlines()


class JelevaExactOwnerLock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(REG.read_text(encoding="utf-8"))["decks"]
        with TRACKER.open(newline="", encoding="utf-8") as f:
            cls.tracker = list(csv.DictReader(f))
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.new = cards(NEW)
        cls.old = cards(OLD)

    def test_exact_byte_hashes_and_commander_first(self):
        raw = NEW.read_bytes()
        self.assertEqual(digest(NEW), SHA)
        self.assertTrue(raw.endswith(b"\n"))
        self.assertFalse(raw.endswith(b"\n\n"))
        self.assertEqual(digest(OLD), OLD_SHA)
        self.assertFalse(OLD.read_bytes().endswith(b"\n"))
        self.assertEqual(len(self.new), 100)
        self.assertEqual(len(self.old), 100)
        self.assertEqual(self.new[0], "1x Jeleva, Nephalia's Scourge [Commander]")
        self.assertEqual(self.old[0], self.new[0])
        self.assertTrue(all(line.startswith("1x ") for line in self.new))
        self.assertEqual(len(set(self.new)), 100)
        self.assertEqual(self.new.count("1x Island"), 1)
        self.assertEqual(self.new.count("1x Swamp"), 1)

    def test_exact_two_swaps_and_jelava_spine(self):
        new = Counter(line.removeprefix("1x ") for line in self.new[1:])
        old = Counter(line.removeprefix("1x ") for line in self.old[1:])
        self.assertEqual(new - old, ADD)
        self.assertEqual(old - new, CUT)
        self.assertTrue(CORE <= set(new))
        self.assertEqual(new["Fire Covenant"], 1)
        self.assertEqual(new["Cavern of Souls"], 1)

    def test_source_bound_oracle_legality_and_counts(self):
        idx = self.index
        self.assertEqual(idx["candidate_raw_sha256"], SHA)
        self.assertEqual(idx["source_date"], "2026-10-23")
        self.assertEqual(idx["source_card_count"], 204)
        self.assertEqual(len(idx["cards"]), 99)
        by_name = {c["name"]: c for c in idx["cards"]}
        self.assertEqual(len(by_name), 99)
        actual = {s.removeprefix("1x ").removesuffix(" [Commander]") for s in self.new}
        self.assertEqual(actual - set(by_name), {"Cavern of Souls"})
        self.assertEqual(set(by_name) - actual, set())
        external = idx["external_card"]
        self.assertEqual(external["name"], "Cavern of Souls")
        self.assertEqual(external["color_identity"], [])
        for card in list(idx["cards"]) + [external]:
            with self.subTest(card=card["name"]):
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"B", "R", "U"})
        self.assertEqual(sum("Land" in c["type_line"] for c in idx["cards"]) + 1, 27)
        self.assertEqual(sum("Instant" in c["type_line"] or "Sorcery" in c["type_line"]
                             for c in idx["cards"]), 45)
        self.assertEqual(sum(bool(c["game_changer"]) for c in idx["cards"]), 20)

    def test_owner_explicit_consent_and_waiver_provenance(self):
        receipt = RECEIPT.read_text(encoding="utf-8")
        verification = VERIFY.read_text(encoding="utf-8")
        for body in (receipt, verification):
            self.assertIn(SHA, body)
            self.assertIn(OLD_SHA, body)
            self.assertIn("Cavern of Souls", body)
            self.assertIn("Fire Covenant", body)
            self.assertIn("#699", body)
        for phrase in ("Approved", "five-swap", "Jeleva-only", "waiver", "23", "loss"):
            self.assertIn(phrase.lower(), receipt.lower())
        self.assertIn("even if cast for free", receipt)

    def test_registry_and_tracker_target_new_owner_lock(self):
        self.assertEqual(len(self.registry), 62)
        self.assertEqual(len(self.tracker), 62)
        e = self.registry[ID]
        self.assertEqual((e["approval_status"], e["lock_status"], e["current_stage"]),
                         ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(e["final_gate_passed"])
        self.assertEqual((e["approved_list_sha256"], e["m7_final_candidate_sha256"]), (SHA, SHA))
        self.assertEqual((e["previous_approved_list_sha256"],
                          e["previous_approved_source_raw_sha256"]), (OLD_SHA, OLD_SHA))
        self.assertEqual(e["previous_approved_list_artifact"], OLD.relative_to(ROOT).as_posix())
        self.assertEqual(e["approved_list_artifact"], NEW.relative_to(ROOT).as_posix())
        self.assertEqual(e["m7_owner_approval_date"], "2026-10-24")
        self.assertEqual(e["m7_archidekt_tags"], ["cEDH", "Spellslinger", "Combo"])
        self.assertEqual(e["m7_power_bracket"], "5 — fringe cEDH")
        self.assertEqual(e["m7_project_exceptions"], [])
        self.assertIn("Single_Deck_Swap_Floor_Exception", e["m7_swap_floor_exception_source"])
        self.assertEqual(sum(bool(v.get("m7_final_candidate_sha256"))
                             for v in self.registry.values()), 24)
        row = next(r for r in self.tracker if r["deck_id"] == ID)
        self.assertEqual(row["index"], "23")
        self.assertEqual(row["final_list_hash"], SHA)
        self.assertEqual(row["user_approval_date"], "2026-10-24")
        self.assertEqual(row["final_gate_passed"], "YES")
        self.assertIn("waiver", row["refinement_status"])

    def test_regression_prior_23_new_m7_owner_locks(self):
        entries = list(self.registry.items())
        first = entries[:23]
        self.assertEqual(first[-1][0], "Inalla__Archmage_Ritualist")
        self.assertEqual(len(first), 23)
        for id_, e in first:
            with self.subTest(deck=id_):
                self.assertEqual(e["approved_list_sha256"], PRIOR23[id_])
                self.assertEqual((e["approval_status"], e["lock_status"]), ("APPROVED", "LOCKED"))
                self.assertEqual(e["approved_list_sha256"], e["m7_final_candidate_sha256"])
                self.assertEqual(digest(ROOT / e["approved_list_artifact"]),
                                 e["m7_final_candidate_sha256"])
        self.assertEqual(entries[23][0], ID)


if __name__ == "__main__":
    unittest.main()
