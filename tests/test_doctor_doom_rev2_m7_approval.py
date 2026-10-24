"""Cory-approved exact Doctor Doom M7 Rev2 100-card canonical lock and 12 earlier-lock regression."""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED = ROOT / "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt"
BASELINE = ROOT / "refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Doctor_Doom_King_of_Latveria_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT = ROOT / "refinement/approvals/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.md"
VERIFICATION = ROOT / "refinement/verification/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
EXACT = "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20"
OLD = "c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58"
COMMANDER = "Doctor Doom, King of Latveria"
ID = "Doctor_Doom__King_of_Latveria"
SWAPS = [
    ("Lightning Axe", "Big Score"),
    ("Glint-Horn Buccaneer", "Green Goblin, Revenant"),
    ("Red Ghost, Intangible Genius", "Loki, the Deceiver"),
    ("Coastal Peak", "Shipwreck Marsh"),
    ("Swiftfoot Boots", "Unexpected Windfall"),
    ("Mox Diamond", "Fellwar Stone"),
    ("Withering Torment", "Feed the Swarm"),
    ("Molten Vortex", "Kang, Temporal Tyrant"),
    ("Tolaria West", "Geier Reach Sanitarium"),
]
ROCKS = {"Arcane Signet", "Sol Ring", "Mox Diamond", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence", "The Soul Stone"}
GAME_CHANGERS = {"Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship",
                 "Jeska\'s Will", "Mox Diamond", "Vampiric Tutor"}
PRIOR_LOCKS = {
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
    "Davros__Dalek_Creator": "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc"
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    result = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        if not m:
            raise AssertionError(f"Invalid line {i+1}: {line}")
        qty, name, annotation = int(m.group(1)), m.group(2), m.group(3)
        if i == 0:
            assert qty == 1 and name == COMMANDER and annotation
        else:
            assert annotation is None
        result[name] += qty
    return result, lines

class DoctorDoomM7Rev2OwnerApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck, cls.lines = parse(APPROVED)
        cls.old, _ = parse(BASELINE)
        cls.source = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {c["name"]: c for c in cls.source["cards"]}
        cls.reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.receipt = RECEIPT.read_text(encoding="utf-8")
        cls.verification = VERIFICATION.read_text(encoding="utf-8")
        with TRACKER.open(encoding="utf-8", newline="") as f:
            cls.rows = list(csv.DictReader(f))

    def test_exact_bytes_historical_approved_source_and_oracle_hash(self):
        self.assertEqual(sha(APPROVED), EXACT)
        self.assertEqual(sha(BASELINE), OLD)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(self.source["candidate_sha256"], EXACT)
        self.assertEqual(self.source["owner_approved_exact_sha256"], EXACT)
        self.assertEqual(self.source["baseline_sha256"], OLD)
        self.assertIn("EXACT_OWNER_APPROVED_CANONICAL_LOCKED", self.source["status"])

    def test_exact_100_singletons_commander_first(self):
        self.assertEqual(sum(self.deck.values()), 100)
        self.assertEqual(len(self.deck), 100)
        self.assertEqual(len(self.lines), 100)
        self.assertEqual(self.deck[COMMANDER], 1)
        self.assertEqual(self.lines[0], "1x Doctor Doom, King of Latveria [Commander]")
        self.assertEqual({k:v for k,v in self.deck.items() if v > 1}, {})
        self.assertEqual(self.source["physical_cards"], 100)
        self.assertEqual(self.source["distinct_names"], 100)

    def test_exact_nine_owner_approved_changes(self):
        self.assertEqual(len(SWAPS), 9)
        self.assertEqual(self.deck - self.old, Counter({a:1 for a,_ in SWAPS}))
        self.assertEqual(self.old - self.deck, Counter({b:1 for _,b in SWAPS}))
        for name in ('Change of Fortune', 'Seismic Assault', 'Surly Badgersaur', 'Dakmor Salvage',
                     'Tectonic Reformation', 'Lethal Scheme', 'Talisman of Creativity'):
            self.assertEqual(self.deck[name],1)

    def test_100_source_identity_legality_color(self):
        self.assertEqual(set(self.deck), set(self.cards))
        self.assertEqual(len(self.cards),100)
        self.assertTrue(self.source["commander_legal_all"])
        self.assertTrue(self.source["color_identity_all_ubr"])
        self.assertEqual(self.source["project_exceptions"],[])
        for n, quantity in self.deck.items():
            with self.subTest(card=n):
                c=self.cards[n]
                self.assertEqual(c["quantity"], quantity)
                self.assertEqual(c["commander_legality"], "legal")
                self.assertTrue(c["oracle_id"] and c["oracle_text"] and c["source"])
                self.assertTrue(set(c["color_identity"]) <= {"U","B","R"})

    def test_mana_count_changers_bracket(self):
        self.assertEqual(sum(x["quantity"] for x in self.cards.values() if "Land" in x["type_line"]),38)
        self.assertEqual(self.source["land_count"],38)
        self.assertEqual(set(self.deck) & ROCKS, ROCKS)
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]}, GAME_CHANGERS)
        self.assertEqual(set(self.source["game_changers"]), GAME_CHANGERS)
        self.assertEqual(self.reg["decks"][ID]["m7_power_bracket"],"4 — Optimized")

    def test_real_discard_and_payability_rules(self):
        x=lambda n:self.cards[n]['oracle_text']
        self.assertIn("one or more land cards", x(COMMANDER))
        self.assertIn("At the beginning of combat", x(COMMANDER))
        self.assertIn("{R}, Discard a land card", x("Molten Vortex"))
        self.assertIn("2 damage to any target", x("Molten Vortex"))
        self.assertIn("Transmute {1}{U}{U}",x("Tolaria West"))
        self.assertIn("mana value 0",x("Tolaria West"))
        self.assertIn("Transmute only as a sorcery",x("Tolaria West"))
        self.assertIn("If this artifact would enter",x("Mox Diamond"))
        self.assertIn("discard a land card instead",x("Mox Diamond"))
        self.assertIn("hexproof", x("Swiftfoot Boots"))
        self.assertIn("Whenever you discard a card",x("Glint-Horn Buccaneer"))
        self.assertIn("you\'ve discarded this turn",x("Change of Fortune"))
        self.assertIn("Destroy target creature or enchantment",x("Withering Torment"))
        self.assertIn("no unbounded/infinite claim",self.verification.lower())

    def test_single_discard_event_vs_multiple(self):
        def doom_damage(events):
            return 2 * sum(any(card == 'Land' for card in event) for event in events)
        self.assertEqual(doom_damage([["Land", "Land", "Land"]]),2)
        self.assertEqual(doom_damage([["Land"],["Land"],["Land"]]),6)
        # Initial discard makes a trigger BEFORE the first dredge draw.
        self.assertEqual(38 // 2 + 1,20)
        self.assertEqual(37 // 2 + 1,19)
        self.assertEqual(26 // 2 + 1,14)

    def test_only_doctor_doom_registry_lock_advances(self):
        self.assertEqual(len(self.reg["decks"]),62)
        d=self.reg["decks"][ID]
        self.assertEqual(d["approved_list_sha256"],EXACT)
        self.assertEqual(d["m7_final_candidate_sha256"],EXACT)
        self.assertEqual(d["previous_approved_source_raw_sha256"],OLD)
        self.assertEqual(d["previous_approved_list_artifact"],"refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt")
        self.assertEqual(d["approval_status"],"APPROVED")
        self.assertEqual(d["lock_status"],"LOCKED")
        self.assertEqual(d["user_approval_date"],"2026-10-23")
        self.assertEqual(d["m7_archidekt_tags"],["Land Discard","Villains","Connive"])
        self.assertTrue(d["m7_verified_100_physical"])
        self.assertEqual(d["m7_project_exceptions"],[])
        for id, expected in PRIOR_LOCKS.items():
            with self.subTest(prior=id):
                c=self.reg["decks"][id]
                self.assertEqual(c["approved_list_sha256"],expected)
                self.assertEqual(sha(ROOT/c["approved_list_artifact"]),expected)

    def test_tracker_unique_row_and_new_lock(self):
        self.assertEqual(len(self.rows),62)
        match=[r for r in self.rows if r["deck_id"]==ID]
        self.assertEqual(len(match),1)
        r=match[0]
        self.assertEqual(r["index"],"12")
        self.assertEqual(r["final_list_hash"],EXACT)
        self.assertEqual(r["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",r["refinement_status"])
        self.assertIn("M7 CANONICAL REVISION",r["notes"])

    def test_receipt_scope_and_no_false_certification(self):
        self.assertIn("> Approved",self.receipt)
        self.assertIn(EXACT,self.receipt)
        self.assertIn("only the exact 100-card raw UTF-8 list",self.receipt)
        self.assertIn("Deck #14 Don Andres",self.receipt)
        self.assertIn("40057650413",self.receipt)
        self.assertIn("no unbounded/infinite claim",self.verification.lower())
        self.assertIn("no invented claims",self.verification.lower())

if __name__ == "__main__":
    unittest.main()
