"""Canonical exact Cory-approved Cormela M7 Rev2 six-swap lock, provenance and prior immutability."""
import csv,hashlib,json,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt"
ORACLE=ROOT/"refinement/verification/Cormela__Glamour_Thief_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Cormela__Glamour_Thief_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Cormela__Glamour_Thief_M7_Rev2_Approved_2026-10-23_Verification.md"
STATE=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
RAW="d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd"
PREVIOUS="80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b"
SWAPS=(
 ("Undercity Sewers","Mistrise Village"),
 ("Exotic Orchard","Underground River"),
 ("Faithless Looting","Frantic Search"),
 ("Gitaxian Probe","Twinflame"),
 ("Red Elemental Blast","Hexing Squelcher"),
 ("Preordain","Into the Flood Maw"),
)
ROCKS={"Arcane Signet","Ashnod's Altar","Chrome Mox","Lion's Eye Diamond","Lotus Petal",
       "Mana Vault","Mox Diamond","Mox Opal","Phyrexian Altar","Sol Ring",
       "Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}
PREVIOUS_M7={
 "Abaddon_the_Despoiler":"5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
 "Admiral_Beckett_Brass":"ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
 "Admiral_Brass__Unsinkable":"dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
 "Anhelo_the_Painter":"865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
 "Ashad_the_Lone_Cyberman":"352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
 "Ashnod_the_Uncaring":"a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
 "Be_lakor_the_Dark_Master":"2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
 "Cecily__Bjorna__Lutri":"e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d",
}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    counts=Counter()
    for l in lines:
        q,n=l.split("x ",1)
        assert q.isdecimal() and int(q)>0,l
        counts[n.removesuffix(" [Commander]")]+=int(q)
    return lines,counts

class CormelaM7Rev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lines,cls.counts=parse(NEW)
        cls.o=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={x["name"]:x for x in cls.o["cards"]}
        cls.reg=json.loads(STATE.read_text(encoding="utf-8"))["decks"]

    def test_exact_raw_hash_and_historical_immutability(self):
        self.assertEqual(sha(NEW),RAW)
        self.assertEqual(sha(OLD),PREVIOUS)
        self.assertTrue(NEW.read_bytes().endswith(bytes([10])))

    def test_100_singleton_single_commander(self):
        self.assertEqual((len(self.lines),len(self.counts),sum(self.counts.values())),(100,100,100))
        self.assertEqual(self.lines[0],"1x Cormela, Glamour Thief [Commander]")
        self.assertEqual(sum("[Commander]" in l for l in self.lines),1)
        self.assertTrue(all(x==1 for x in self.counts.values()))

    def test_six_exact_owner_swaps_vs_previous_approved(self):
        old,previous=parse(OLD)
        self.assertEqual(len(old),100)
        self.assertEqual(self.counts-previous,Counter({a:1 for c,a in SWAPS}))
        self.assertEqual(previous-self.counts,Counter({c:1 for c,a in SWAPS}))
        self.assertEqual(len(SWAPS),6)

    def test_current_selected_scryfall_legality_and_ubr(self):
        self.assertEqual(self.o["candidate_raw_sha256"],RAW)
        self.assertEqual(self.o["baseline_raw_sha256"],PREVIOUS)
        self.assertEqual(self.o["physical_cards"],100)
        self.assertEqual(self.o["distinct_names"],100)
        self.assertEqual(self.o["project_exceptions"],[])
        self.assertTrue(self.o["official_commander_legal_all"])
        self.assertTrue(self.o["grixis_color_identity_all"])
        self.assertEqual(len(self.cards),100)
        self.assertEqual(set(self.cards),set(self.counts))
        for n,c in self.cards.items():
            with self.subTest(name=n):
                self.assertEqual(c["quantity"],1)
                self.assertEqual(c["commander_legality"],"legal")
                self.assertLessEqual(set(c["color_identity"]),{"U","B","R"})
                self.assertTrue(c["oracle_id"])
                self.assertIsNotNone(c["oracle_text"])
                self.assertTrue(c["source"])

    def test_mana_sources_and_twenty_game_changers(self):
        self.assertEqual(self.o["normal_lands"],30)
        self.assertEqual(sum("Land" in c["type_line"] for c in self.cards.values()),30)
        self.assertEqual(len(ROCKS),13)
        self.assertEqual(ROCKS & set(self.counts),ROCKS)
        self.assertEqual(len(self.o["game_changers"]),20)
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]},set(self.o["game_changers"]))

    def test_rules_oracle_timing_and_conversions(self):
        self.assertIn("Spend this mana only to cast instant and/or sorcery spells",self.cards["Cormela, Glamour Thief"]["oracle_text"])
        self.assertIn("When Cormela dies",self.cards["Cormela, Glamour Thief"]["oracle_text"])
        self.assertIn("Untap up to three lands",self.cards["Frantic Search"]["oracle_text"])
        self.assertIn("except it has haste",self.cards["Twinflame"]["oracle_text"])
        self.assertIn("Spells you control can't be countered",self.cards["Hexing Squelcher"]["oracle_text"])
        t=self.cards["Into the Flood Maw"]
        self.assertEqual(t["mana_cost"],"{U}")
        self.assertIn("Gift a tapped Fish",t["oracle_text"])
        self.assertIn("target nonland permanent an opponent controls",t["oracle_text"])

    def test_receipt_scope_and_verification_no_overclaims(self):
        a=RECEIPT.read_text(encoding="utf-8")
        b=VERIFY.read_text(encoding="utf-8")
        for term in ("> Approve",RAW,"not a blanket approval","non-independent","six expressly approved"):
            self.assertIn(term.lower(),a.lower())
        for term in ("25 existing", "not re-sealed", "Grok", "100 physical"):
            self.assertIn(term.lower(),b.lower())

    def test_canonical_registry_prior_hash_and_current_metadata(self):
        x=self.reg["Cormela__Glamour_Thief"]
        self.assertEqual((x["approval_status"],x["lock_status"]),( "APPROVED","LOCKED"))
        self.assertTrue(x["final_gate_passed"])
        self.assertEqual(x["approved_list_sha256"],RAW)
        self.assertEqual(x["m7_final_candidate_sha256"],RAW)
        self.assertEqual(x["previous_approved_list_sha256"],PREVIOUS)
        self.assertEqual(x["approved_list_artifact"],str(NEW.relative_to(ROOT)))
        self.assertEqual(x["previous_approved_list_artifact"],str(OLD.relative_to(ROOT)))
        self.assertEqual(x["m7_archidekt_tags"],["Storm","Aristocrats","Combo"])
        self.assertEqual(x["m7_power_bracket"],"5 — cEDH")
        self.assertEqual(x["m7_project_exceptions"],[])

    def test_tracker_row_hash_approval_and_alias(self):
        with TRACKER.open(newline="",encoding="utf-8") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),62)
        r=next(x for x in rows if x["index"]=="8")
        self.assertEqual(r["deck_id"],"Cormela__Glamour_Thief")
        self.assertEqual(r["final_list_hash"],RAW)
        self.assertEqual(r["user_approval_date"],"2026-10-23")
        self.assertEqual(r["final_gate_passed"],"YES")
        self.assertIn("APPROVED / LOCKED",r["refinement_status"])
        self.assertIn("six",r["swap_decision_ledger_complete"])

    def test_eight_prior_m7_locks_remain_exact(self):
        self.assertEqual(len(self.reg),62)
        for key,digest in PREVIOUS_M7.items():
            with self.subTest(deck=key):
                x=self.reg[key]
                self.assertEqual((x["approval_status"],x["lock_status"]),("APPROVED","LOCKED"))
                self.assertEqual(x["approved_list_sha256"],digest)

if __name__=="__main__":unittest.main()
