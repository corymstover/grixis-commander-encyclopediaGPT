"""Canonical Inalla M7 Rev1 exact-owner approval regression gate, no gameplay claims."""
import csv
import hashlib
import itertools
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK_ID = "Inalla__Archmage_Ritualist"
NEW = ROOT / "refinement/decklists/Inalla_Archmage_Ritualist_M7_Rev1_Approved_2026-10-24.txt"
OLD = ROOT / "refinement/decklists/Inalla_Archmage_Ritualist_Approved_2026-10-14.txt"
REC = ROOT / "refinement/approvals/Inalla_Archmage_Ritualist_M7_Rev1_Approved_2026-10-24.md"
VERIFY = ROOT / "refinement/verification/Inalla_Archmage_Ritualist_M7_Rev1_Approved_2026-10-24_Verification.md"
ORACLE = ROOT / "refinement/verification/Inalla_Archmage_Ritualist_M7_Rev1_Scryfall_Selected_2026-10-24.json"
REG = ROOT / "state/current_deck_overrides.json"
TRACK = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SHA = "c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69"
OLD_SHA = "81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3"
ADD = Counter({"Flashback": 1, "Corpse Dance": 1, "Gifts Ungiven": 1,
               "Forbidden Orchard": 1, "Starting Town": 1})
CUT = Counter({"Kefka, Court Mage // Kefka, Ruler of Ruin": 1,
               "Final Fortune": 1, "Wheel of Fortune": 1,
               "Exotic Orchard": 1, "Island": 1})
CORE = ("Inalla, Archmage Ritualist", "Spellseeker", "Culling the Weak",
        "Unearth", "Burnt Offering", "Finale of Promise", "Entomb",
        "Reanimate", "Scholar of the Ages", "Shallow Grave",
        "Bloodline Necromancer", "Ruthless Technomancer",
        "Saw in Half", "Tainted Pact", "Thassa's Oracle",
        "Demonic Consultation", "Underworld Breach", "Lion's Eye Diamond",
        "Brain Freeze")
OTHER61 = json.loads(r'''{
  "Abaddon_the_Despoiler": [
    "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24",
    "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Admiral_Beckett_Brass": [
    "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000",
    "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt",
    "2026-10-22",
    "LOCKED"
  ],
  "Admiral_Brass__Unsinkable": [
    "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7",
    "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Anhelo_the_Painter": [
    "865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77",
    "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Ashad_the_Lone_Cyberman": [
    "352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
    "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Ashnod_the_Uncaring": [
    "a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761",
    "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Be_lakor_the_Dark_Master": [
    "2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4",
    "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Cecily__Bjorna__Lutri": [
    "e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d",
    "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Cormela__Glamour_Thief": [
    "d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd",
    "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Crosis__the_Purger": [
    "a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a",
    "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Cult_of_Skaro": [
    "e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d",
    "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Davros__Dalek_Creator": [
    "96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc",
    "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Doctor_Doom__King_of_Latveria": [
    "7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20",
    "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Don_Andres__the_Renegade": [
    "59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f",
    "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Dr__Eggman": [
    "3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec",
    "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Edea__Possessed_Sorceress": [
    "a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54",
    "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Edward_Kenway": [
    "8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1",
    "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Evelyn__the_Covetous": [
    "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac",
    "refinement/decklists/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.txt",
    "2026-10-23",
    "LOCKED"
  ],
  "Fire_Lord_Azula": [
    "77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273",
    "refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt",
    "2026-10-24",
    "LOCKED"
  ],
  "Garza_Zol__Plague_Queen": [
    "353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244",
    "refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt",
    "2026-10-24",
    "LOCKED"
  ],
  "Goro_Goro_and_Satoru": [
    "36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c",
    "refinement/decklists/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24.txt",
    "2026-10-24",
    "LOCKED"
  ],
  "Gwendlyn_Di_Corci": [
    "36b76cbe47a04b7492007103e4baaad50324b3e72fb2067b28aa8bb9da70e355",
    "refinement/decklists/Gwendlyn_Di_Corci_M7_Rev1_Approved_2026-10-24.txt",
    "2026-10-24",
    "LOCKED"
  ],
  "Jeleva__Nephalia_s_Scourge": [
    "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f",
    "refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Kefka__Court_Mage": [
    "cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03",
    "refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Kess__Dissident_Mage": [
    "93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb",
    "refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Grixistax___October_2026": [
    "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c",
    "refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Loki__the_Deceiver": [
    "5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062",
    "refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Lord_of_Tresserhorn": [
    "95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e",
    "refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Lord_Xander__the_Collector": [
    "92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787",
    "refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Lynde__Cheerful_Tormentor": [
    "6e088891b3c92b632d95e4b6dbd83ffedb06834f812e6728cc5bfa7bdc13556e",
    "refinement/decklists/Lynde_Cheerful_Tormentor_M7_Rev1_Approved_2026-10-25.txt",
    "2026-10-25",
    "LOCKED"
  ],
  "Mai_and_Zuko": [
    "aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2",
    "refinement/decklists/Mai_and_Zuko_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Mairsil__the_Pretender": [
    "51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5",
    "refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt",
    "2026-10-14",
    "LOCKED"
  ],
  "Marchesa__Dealer_of_Death": [
    "34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1",
    "refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Marchesa__the_Black_Rose": [
    "627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b",
    "refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Mishra__Artificer_Prodigy": [
    "9210aefa423dbe9cc69d18422c0d594cad6e5d0ee475d687b9f2278a2ca3b79d",
    "refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Mishra__Eminent_One": [
    "ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0",
    "refinement/decklists/Mishra_Eminent_One_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Missy": [
    "9ee63d81c07c3b43163e1356cbf264deb9021d0b776daf0a91b85d071aed5aed",
    "refinement/decklists/Missy_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Nathan_Drake__Treasure_Hunter": [
    "a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0",
    "refinement/decklists/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Nekusar__the_Mindrazer": [
    "bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1",
    "refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Nicol_Bolas": [
    "e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617",
    "refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Nicol_Bolas__the_Ravager": [
    "5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e",
    "refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Goben__Gene_Splice_Savant": [
    "23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2",
    "refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Obeka__Brute_Chronologist": [
    "31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8",
    "refinement/decklists/Obeka_Brute_Chronologist_Approval_Ready_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Obeka__Splitter_of_Seconds": [
    "c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63",
    "refinement/decklists/Obeka_Splitter_of_Seconds_Approval_Ready_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Parnesse__the_Subtle_Brush": [
    "8ff8c101d98e7de997c1de29973db2dd6a51ffdd7b44e4f34145bb1abf2d9e7c",
    "refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "RogSi": [
    "06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c",
    "refinement/decklists/RogSi_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Saruman__the_White_Hand": [
    "4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2",
    "refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Sauron__Lord_of_the_Rings": [
    "72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0",
    "refinement/decklists/Sauron_Lord_of_the_Rings_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Sauron__the_Dark_Lord": [
    "fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8",
    "refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Sedris__the_Traitor_King": [
    "65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365",
    "refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Sol_kanar_the_Swamp_King": [
    "7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106",
    "refinement/decklists/Solkanar_the_Swamp_King_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Sol_kanar_the_Tainted": [
    "72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58",
    "refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Tetsuo_Umezawa": [
    "14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6",
    "refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Tetsuo__Imperial_Champion": [
    "d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e",
    "refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "The_Madcap_Jester": [
    "caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7",
    "refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "The_Valeyard": [
    "4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c",
    "refinement/decklists/The_Valeyard_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "The_Rani": [
    "7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c",
    "refinement/decklists/The_Rani_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Thraximundar": [
    "d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442",
    "refinement/decklists/Thraximundar_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Tresserhorn_s_Lord__Returned": [
    "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8",
    "refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Wick__the_Whorled_Mind": [
    "f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98",
    "refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Zevlor__Elturel_Exile": [
    "d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9",
    "refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ]
}''')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse_deck(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    cards = Counter()
    for line in lines:
        match = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert match, (path, line)
        cards[match[2]] += int(match[1])
    return cards, lines

class InallaM7Rev1Approval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new, cls.lines = parse_deck(NEW)
        cls.old, cls.old_lines = parse_deck(OLD)
        cls.registry = json.loads(REG.read_text(encoding="utf-8"))["decks"]
        cls.source = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards = {x["name"]: x for x in cls.source["cards"]}
        cls.receipt = REC.read_text(encoding="utf-8")
        cls.verify = VERIFY.read_text(encoding="utf-8")
        with TRACK.open(encoding="utf-8", newline="") as f:
            cls.tracker = list(csv.DictReader(f))

    def test_owner_authority_and_exact_raw_100_bytes(self):
        self.assertEqual(digest(NEW), SHA)
        self.assertEqual(digest(OLD), OLD_SHA)
        self.assertTrue(NEW.read_bytes().endswith(b"\n"))
        self.assertFalse(OLD.read_bytes().endswith(b"\n"))
        self.assertEqual((len(self.lines), sum(self.new.values()), len(self.new)), (100, 100, 100))
        self.assertEqual((len(self.old_lines), sum(self.old.values()), len(self.old)), (100, 100, 100))
        self.assertEqual(self.lines[0], "1x Inalla, Archmage Ritualist [Commander]")
        self.assertEqual(sum("[Commander]" in l for l in self.lines), 1)
        self.assertEqual(self.new - self.old, ADD)
        self.assertEqual(self.old - self.new, CUT)
        self.assertEqual(len(self.new & self.old), 95)
        self.assertIn('“Approve”', self.receipt)
        self.assertIn(SHA, self.receipt)
        self.assertIn(OLD_SHA, self.receipt)
        self.assertIn("five owner-approved", self.receipt.lower())
        self.assertIn(SHA, self.verify)
        self.assertIn("Pre-merge", self.verify)

    def test_scryfall_oracle_current_legal_identity_and_game_changers(self):
        s = self.source
        self.assertEqual(s["approved_candidate_raw_sha256"], SHA)
        self.assertEqual(s["historical_baseline_raw_sha256"], OLD_SHA)
        self.assertEqual((s["physical_cards"], s["distinct_names"], s["lands"]), (100, 100, 27))
        self.assertEqual(set(self.new), set(self.cards))
        self.assertEqual(s["game_changers"], 19)
        self.assertEqual(s["project_exceptions"], [])
        self.assertEqual(len(self.cards), 100)
        lands = gc = 0
        for name, qty in self.new.items():
            c = self.cards[name]
            self.assertEqual(c["quantity"], qty, name)
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            self.assertTrue(c["oracle_text"], name)
            lands += int("Land" in c["type_line"])
            gc += bool(c["game_changer"])
        self.assertEqual((lands, gc), (27, 19))
        flash = self.cards["Flashback"]
        self.assertEqual((flash["mana_cost"], flash["cmc"], flash["oracle_id"]), ("{R}", 1, None))
        self.assertIn("gains flashback", flash["oracle_text"])
        self.assertIn("wizards.com", flash["published_origin"])
        self.assertIn("not in Oct23", flash["source_limit"])
        self.assertTrue(self.cards["Gifts Ungiven"]["game_changer"])
        self.assertNotIn("Samut, Tyrant of Naktamun", self.new)

    def test_commander_first_core_and_spell_rules(self):
        for name in CORE:
            self.assertEqual(self.new[name], 1)
        self.assertIn("nontoken Wizard", self.cards["Inalla, Archmage Ritualist"]["oracle_text"])
        self.assertIn("mana value 2 or less", self.cards["Spellseeker"]["oracle_text"])
        self.assertIn("top creature card", self.cards["Corpse Dance"]["oracle_text"])
        self.assertIn("Buyback {2}", self.cards["Corpse Dance"]["oracle_text"])
        self.assertEqual(self.cards["Scholar of the Ages"]["cmc"], 7)
        self.assertIn("sacrificed creature's mana value",
                      self.cards["Burnt Offering"]["oracle_text"])
        self.assertEqual(7 - 1 - 5, 1)
        self.assertIn("exiled after", self.verify)
        self.assertIn("normal timing", self.verify)
        self.assertIn("top creature card", self.verify)

    def test_gifts_exact_six_opponent_splits(self):
        pile = ("Spellseeker", "Step Through", "Reanimate", "Unearth")
        gifts = self.cards["Gifts Ungiven"]["oracle_text"]
        self.assertIn("up to four cards with different names", gifts)
        self.assertIn("Target opponent chooses two", gifts)
        possibilities = set()
        for grave in itertools.combinations(pile, 2):
            grave = frozenset(grave)
            hand = frozenset(pile) - grave
            self.assertTrue("Spellseeker" in hand or (
                "Spellseeker" in grave and
                bool({"Reanimate", "Unearth"} & hand)), (grave, hand))
            possibilities.add(grave)
        self.assertEqual(len(possibilities), 6)
        self.assertIn("mana value 3 or less", self.cards["Unearth"]["oracle_text"])
        self.assertIn("life equal to that card's mana value", self.cards["Reanimate"]["oracle_text"])

    def test_mana_tradeoffs_burnt_and_archidekt_tags(self):
        self.assertIn("target opponent creates a 1/1",
                      self.cards["Forbidden Orchard"]["oracle_text"])
        self.assertIn("first, second, or third turn", self.cards["Starting Town"]["oracle_text"])
        self.assertIn("Pay 1 life", self.cards["Starting Town"]["oracle_text"])
        self.assertEqual(self.new["Swamp"], 1)
        self.assertEqual(self.new["Island"], 0)
        self.assertEqual(self.source["power_bracket"], "5 — cEDH")
        self.assertEqual(self.source["archidekt_tags"], ["Spellseeker Combo", "Reanimator", "Turbo"])
        self.assertIn("Wheel", self.receipt)
        self.assertIn("Final Fortune", self.receipt)

    def test_inalla_registry_and_one_tracker_row(self):
        d = self.registry[DECK_ID]
        self.assertEqual((d["approval_status"], d["lock_status"], d["current_stage"]),
                         ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(d["final_gate_passed"])
        self.assertEqual((d["approved_list_sha256"], d["m7_final_candidate_sha256"]), (SHA, SHA))
        self.assertEqual(d["previous_approved_list_sha256"], OLD_SHA)
        self.assertEqual(d["previous_approved_source_raw_sha256"], OLD_SHA)
        self.assertEqual(d["approved_list_artifact"], NEW.relative_to(ROOT).as_posix())
        self.assertEqual(d["previous_approved_list_artifact"], OLD.relative_to(ROOT).as_posix())
        self.assertEqual(d["m7_owner_approval_date"], "2026-10-24")
        self.assertEqual(d["m7_archidekt_tags"], ["Spellseeker Combo", "Reanimator", "Turbo"])
        self.assertEqual(d["m7_project_exceptions"], [])
        self.assertEqual((len(self.tracker), len(self.registry)), (62, 62))
        ours = [r for r in self.tracker if r["deck_id"] == DECK_ID]
        self.assertEqual(len(ours), 1)
        t = ours[0]
        self.assertEqual(t["index"], "22")
        self.assertEqual(t["final_list_hash"], SHA)
        self.assertEqual(t["user_approval_date"], "2026-10-24")
        self.assertIn("APPROVED / LOCKED", t["refinement_status"])
        self.assertIn("five", t["notes"].lower())
        self.assertTrue(all(r["deck_id"] != DECK_ID or r["final_list_hash"] == SHA
                            for r in self.tracker))

    def test_all_61_other_approved_decks_exact_bytes_and_registry_unchanged(self):
        self.assertEqual(len(OTHER61), 61)
        self.assertEqual(set(self.registry) - {DECK_ID}, set(OTHER61))
        for deckid, (sha, path, approved_date, lock_status) in OTHER61.items():
            with self.subTest(deck=deckid):
                r = self.registry[deckid]
                # Jeleva advanced later by explicit owner approval and a narrowly
                # authorized two-swap waiver. Keep the October 14 source attested.
                # Deck #26 later advanced by Cory's separate exact five-swap M7 approval.
                # Retain and hash the original October 14 source, as with Jeleva.
                # Cory's subsequent explicit Deck #27 M7 Rev1 approval supersedes
                # only the registry pointer; the original 2026-10-14 file is immutable.
                # Deck #29's later exact owner-approved M7 replacement; preserve Oct14 bytes.
                if deckid == "Lord_of_Tresserhorn" and r.get("m7_owner_approval_date") == "2026-10-25":
                    self.assertEqual(r["previous_approved_list_sha256"], sha)
                    self.assertEqual(r["previous_approved_list_artifact"], path)
                    self.assertEqual(digest(ROOT / path), sha)
                    self.assertEqual((r["approved_list_sha256"], r["approved_list_artifact"],
                                      r["user_approval_date"], r["lock_status"]),
                                     ("fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85", "refinement/decklists/Lord_of_Tresserhorn_M7_Rev1_Approved_2026-10-25.txt", "2026-10-25", "LOCKED"))
                    self.assertEqual(digest(ROOT / "refinement/decklists/Lord_of_Tresserhorn_M7_Rev1_Approved_2026-10-25.txt"), "fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85")
                    continue
                if deckid == "Grixistax___October_2026" and r.get("m7_owner_approval_date") == "2026-10-25":
                    self.assertEqual(sha, "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c")
                    self.assertEqual(r["previous_approved_list_sha256"], sha)
                    self.assertEqual(r["previous_approved_list_artifact"], path)
                    self.assertEqual(digest(ROOT / path), sha)
                    self.assertEqual((r["approved_list_sha256"], r["approved_list_artifact"],
                                      r["user_approval_date"], r["lock_status"]),
                                     ("70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e", "refinement/decklists/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25.txt", "2026-10-25", "LOCKED"))
                    self.assertEqual(digest(ROOT / "refinement/decklists/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25.txt"), "70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e")
                    continue
                if deckid == "Kess__Dissident_Mage" and r.get("m7_owner_approval_date") == "2026-10-24":
                    self.assertEqual(r["previous_approved_source_raw_sha256"], sha)
                    self.assertEqual(r["previous_approved_list_artifact"], path)
                    self.assertEqual(digest(ROOT / path), sha)
                    self.assertEqual((r["approved_list_sha256"], r["approved_list_artifact"],
                                      r["user_approval_date"], r["lock_status"]),
                                     ("11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4", "refinement/decklists/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.txt", "2026-10-24", "LOCKED"))
                    self.assertEqual(digest(ROOT / "refinement/decklists/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.txt"), "11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4")
                    continue
                if deckid == "Jeleva__Nephalia_s_Scourge" and r.get("m7_owner_approval_date") == "2026-10-24":
                    expected_sha = "6f2cdafa089c3e923104429f764bed66e500fe20cafb3b00dd4d29488bd52cac"
                    expected_path = "refinement/decklists/Jeleva_Nephalia_s_Scourge_M7_Rev1_Approved_2026-10-24.txt"
                    self.assertEqual(r["previous_approved_source_raw_sha256"], sha)
                    self.assertEqual(r["previous_approved_list_artifact"], path)
                    self.assertEqual(digest(ROOT / path), sha)
                    self.assertEqual((r["approved_list_sha256"], r["approved_list_artifact"],
                                      r["user_approval_date"], r["lock_status"]),
                                     (expected_sha, expected_path, "2026-10-24", "LOCKED"))
                    self.assertEqual(digest(ROOT / expected_path), expected_sha)
                    continue
                if deckid == "Loki__the_Deceiver" and r.get("m7_owner_approval_date") == "2026-10-25":
                    newsha = "919734ad1f60e56a636561815d319ec1eb0fbd0c233265ad5e85064f589c7185"
                    newpath = "refinement/decklists/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25.txt"
                    self.assertEqual(r["previous_approved_list_sha256"], sha)
                    self.assertEqual(r["previous_approved_list_artifact"], path)
                    self.assertEqual(digest(ROOT / path), sha)
                    self.assertEqual((r["approved_list_sha256"], r["approved_list_artifact"],
                                      r["user_approval_date"], r["lock_status"]),
                                     (newsha, newpath, "2026-10-25", "LOCKED"))
                    self.assertEqual(digest(ROOT / newpath), newsha)
                    continue
                if deckid == "Lord_Xander__the_Collector" and r.get("m7_owner_approval_date") == "2026-10-25":
                    newsha = "de348618961269083a44a3f3e05a7f0be7ddbd7e943da0ac82a115e5e4aeb6cd"
                    newpath = "refinement/decklists/Lord_Xander_the_Collector_M7_Rev1_Approved_2026-10-25.txt"
                    self.assertEqual(r["previous_approved_list_sha256"], sha)
                    self.assertEqual(r["previous_approved_list_artifact"], path)
                    self.assertEqual(digest(ROOT / path), sha)
                    self.assertEqual(r["approved_list_sha256"], newsha)
                    self.assertEqual(r["approved_list_artifact"], newpath)
                    self.assertEqual(r["user_approval_date"], "2026-10-25")
                    self.assertEqual(r["lock_status"], "LOCKED")
                    self.assertEqual(digest(ROOT / newpath), newsha)
                    continue
                # A later, separately owner-approved M7 SHA may supersede this
                # historical pointer only when prior exact bytes and the new receipt verify.
                if r.get("previous_approved_list_sha256") == sha and r.get("previous_approved_list_artifact") == path and r.get("m7_owner_approval_date", "") > approved_date:
                    self.assertEqual(digest(ROOT / path), sha)
                    fresh = r["approved_list_sha256"]
                    self.assertEqual(digest(ROOT / r["approved_list_artifact"]), fresh)
                    self.assertIn(fresh, (ROOT / r["approval_record_artifact"]).read_text(encoding="utf-8"))
                    self.assertEqual(r["lock_status"], "LOCKED")
                    continue
                self.assertEqual(r["approved_list_sha256"], sha)
                self.assertEqual(r["approved_list_artifact"], path)
                self.assertEqual(r["user_approval_date"], approved_date)
                self.assertEqual(r["lock_status"], lock_status)
                self.assertEqual(r["approval_status"], "APPROVED")
                self.assertEqual(digest(ROOT / path), sha)

    def test_first_23_m7_lock_count_and_no_new_unapproved(self):
        first = list(self.registry)[:23]
        self.assertEqual(first[-1], DECK_ID)
        self.assertEqual(sum(bool(self.registry[k].get("m7_final_candidate_sha256"))
                             for k in first), 23)
        self.assertGreaterEqual(sum(bool(v.get("m7_final_candidate_sha256"))
                                    for v in self.registry.values()), 24)
        for deckid in first:
            self.assertEqual(self.registry[deckid]["lock_status"], "LOCKED")

if __name__ == "__main__":
    unittest.main()
