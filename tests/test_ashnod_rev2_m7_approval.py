"""Ashnod M7 Rev2 exact Cory-approved nine-swap canonical source and preserved locks."""
import csv,hashlib,json,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt"
OLD=ROOT/"refinement/decklists/Ashnod_the_Uncaring_Approved_2026-10-13.txt"
ORACLE=ROOT/"refinement/verification/Ashnod_the_Uncaring_M7_Rev2_Scryfall_Selected_2026-10-23.json"
RECEIPT=ROOT/"refinement/approvals/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.md"
VERIFY=ROOT/"refinement/verification/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23_Verification.md"
STATE=ROOT/"state/current_deck_overrides.json"
TRACKER=ROOT/"refinement/Deck_Refinement_Tracker_2026-10-12.csv"
RAW="a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761"
PREVIOUS="f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf"
ADDS={"Corridor Monitor","Basalt Monolith","Aether Spellbomb","Spawning Pit","Animation Module","Priest of Forgotten Gods","Ruthless Knave","City of Brass","Mana Confluence"}
CUTS={"Foundry Inspector","Fellwar Stone","Talisman of Indulgence","Esoteric Duplicator","Reckless Fireweaver","Jhoira, Weatherlight Captain","Farid, Enterprising Salvager","Xander's Lounge","Exotic Orchard"}
BASICS={"Island":3,"Mountain":2,"Swamp":3}
ROCKS={"Sol Ring","Arcane Signet","Mind Stone","Talisman of Creativity","Talisman of Dominance","Mox Opal","Lotus Petal","Basalt Monolith"}
GCS={"Ancient Tomb","Bolas's Citadel","Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Vampiric Tutor"}
PRIOR={
"Abaddon_the_Despoiler":"5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
"Admiral_Beckett_Brass":"ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
"Admiral_Brass__Unsinkable":"dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
"Anhelo_the_Painter":"865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
"Ashad_the_Lone_Cyberman":"352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267"
}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def rows(path):
    out=Counter()
    lines=path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        q,n=line.split("x ",1)
        assert q.isdecimal() and int(q)>0,line
        out[n.removesuffix(" [Commander]")]+=int(q)
    return lines,out
class AshnodRev2CanonicalApproval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.card={x["name"]:x for x in cls.oracle["cards"]}
        cls.state=json.loads(STATE.read_text(encoding="utf-8"))["decks"]
    def test_exact_100_sha_singleton_mana_and_bracket(self):
        self.assertEqual(sha(NEW),RAW)
        ls,c=rows(NEW)
        self.assertEqual(ls[0],"1x Ashnod the Uncaring [Commander]")
        self.assertEqual((len(ls),len(c),sum(c.values())),(95,95,100))
        self.assertEqual(sum("[Commander]" in x for x in ls),1)
        self.assertEqual({n:q for n,q in c.items() if q>1},BASICS)
        self.assertEqual(sum(q for n,q in c.items() if "Land" in self.card[n]["type_line"]),33)
        self.assertEqual(sum(c[n] for n in ROCKS),8)
        self.assertEqual({n for n in c if self.card[n]["game_changer"]},GCS)
        self.assertTrue({"Walking Ballista","Krark-Clan Shaman","Forensic Gadgeteer","Rings of Brighthearth",
                         "Arcbound Ravager","Crime Novelist","Lotus Petal","Time Sieve"}.issubset(c))
    def test_prior_approved_source_and_nine_one_to_one(self):
        self.assertEqual(sha(OLD),PREVIOUS)
        _,a=rows(OLD);_,b=rows(NEW)
        self.assertEqual(set((b-a).elements()),ADDS)
        self.assertEqual(set((a-b).elements()),CUTS)
        self.assertEqual(sum((b-a).values()),9)
        self.assertEqual(sum((a-b).values()),9)
    def test_all_current_oracle_records_legality_ub_identity(self):
        s=self.oracle;_,c=rows(NEW)
        self.assertEqual((s["candidate_raw_sha256"],s["physical_cards"],s["distinct_card_names"]),(RAW,100,95))
        self.assertEqual((s["land_count"],s["static_rock_count"],s["game_changers_count"]),(33,8,6))
        self.assertEqual((len(self.card),set(self.card)),(95,set(c)))
        self.assertTrue(s["all_selected_commander_legal"])
        self.assertTrue(s["all_selected_grixis_identity"])
        self.assertEqual(s["project_exceptions"],[])
        for n,q in c.items():
            x=self.card[n]
            self.assertEqual(x["quantity"],q,n)
            self.assertEqual(x["commander_legality"],"legal",n)
            self.assertTrue(set(x["color_identity"]) <= {"U","B","R"},n)
            self.assertTrue(x["oracle_id"] and isinstance(x["oracle_text"],str),n)
    def test_copy_rules_basalt_module_and_manual_pit_are_disclosed(self):
        o=self.card
        self.assertIn("if one or more permanents were sacrificed to activate it",o["Ashnod the Uncaring"]["oracle_text"])
        self.assertIn("Sacrifice a creature: Put a charge counter",o["Spawning Pit"]["oracle_text"])
        self.assertIn("Whenever you sacrifice an artifact",o["Crime Novelist"]["oracle_text"])
        self.assertIn("Whenever one or more +1/+1 counters",o["Animation Module"]["oracle_text"])
        self.assertIn("{T}: Add {C}{C}{C}",o["Basalt Monolith"]["oracle_text"])
        self.assertIn("cost {1} less",o["Forensic Gadgeteer"]["oracle_text"])
        self.assertIn("Any number of target players",o["Priest of Forgotten Gods"]["oracle_text"])
        self.assertIn("Sacrifice three Treasures: Draw a card",o["Ruthless Knave"]["oracle_text"])
        receipt=RECEIPT.read_text()
        self.assertIn("manually derived from Oracle",receipt)
        self.assertIn("non-independent",receipt)
        self.assertIn("not automatically a win",receipt)
    def test_owner_receipt_does_not_auto_accept_milestone(self):
        a=RECEIPT.read_text();v=VERIFY.read_text()
        self.assertIn("> I approve",a)
        self.assertIn(RAW,a)
        self.assertIn("PR #681",a)
        self.assertIn("40048290216",a+v)
        self.assertIn("9/9",a+v)
        self.assertIn("29/29",a+v)
        self.assertIn("not an approval",a)
        self.assertIn("M8",a)
    def test_registry_exact_lock_historical_provenance_and_prior_five(self):
        c=self.state["Ashnod_the_Uncaring"]
        self.assertEqual(c["approved_list_sha256"],RAW)
        self.assertEqual(c["approved_list_artifact"],str(NEW.relative_to(ROOT)))
        self.assertEqual(c["previous_approved_list_sha256"],PREVIOUS)
        self.assertEqual(c["previous_approved_list_artifact"],str(OLD.relative_to(ROOT)))
        self.assertEqual(c["user_approval_date"],"2026-10-23")
        self.assertEqual((c["approval_status"],c["lock_status"],c["current_stage"]),("APPROVED","LOCKED","LOCKED"))
        self.assertEqual(c["m7_archidekt_tags"],["Ability Copy","Artifact Sacrifice","Artifact Combo"])
        self.assertEqual(c["m7_power_bracket"],"4 — Optimized")
        for deck,digest in PRIOR.items():
            self.assertEqual(self.state[deck]["approved_list_sha256"],digest,deck)
            self.assertEqual((self.state[deck]["approval_status"],self.state[deck]["lock_status"]),("APPROVED","LOCKED"),deck)
    def test_tracker_62_other_records_intact_ashnod_only_new_hash(self):
        with TRACKER.open(encoding="utf-8",newline="") as stream:
            rows=list(csv.DictReader(stream))
        self.assertEqual(len(rows),62)
        r=next(x for x in rows if x["deck_id"]=="Ashnod_the_Uncaring")
        self.assertEqual(r["index"],"5")
        self.assertEqual(r["final_list_hash"],RAW)
        self.assertEqual(r["user_approval_date"],"2026-10-23")
        self.assertIn("APPROVED / LOCKED",r["refinement_status"])
        self.assertIn("nine",r["swap_decision_ledger_complete"])
        self.assertIn("Spawning Pit",r["swap_decision_ledger_complete"])
        self.assertEqual(sum(x["final_list_hash"]==RAW for x in rows),1)
if __name__=="__main__":unittest.main()
