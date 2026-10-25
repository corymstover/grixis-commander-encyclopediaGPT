"""Canonical Gwendlyn Di Corci M7 Rev1 exact owner-approval source-bound gate."""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Gwendlyn_Di_Corci"
APPROVED = ROOT / "refinement/decklists/Gwendlyn_Di_Corci_M7_Rev1_Approved_2026-10-24.txt"
BASELINE = ROOT / "refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Gwendlyn_Di_Corci_M7_Rev1_Scryfall_Selected_2026-10-24.json"
RECEIPT = ROOT / "refinement/approvals/Gwendlyn_Di_Corci_M7_Rev1_Approved_2026-10-24.md"
VERIFICATION = ROOT / "refinement/verification/Gwendlyn_Di_Corci_M7_Rev1_Approved_2026-10-24_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SHA = "36b76cbe47a04b7492007103e4baaad50324b3e72fb2067b28aa8bb9da70e355"
OLD = "9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9"
SWAPS_ADDS = Counter({"Hymn to Tourach": 1, "Rings of Brighthearth": 1,
                       "Sting, the Glinting Dagger": 1, "Misty Rainforest": 1,
                       "Marsh Flats": 1, "Shivan Reef": 1})
SWAPS_CUTS = Counter({"Dauthi Voidwalker": 1, "Underworld Dreams": 1,
                       "The Raven Man": 1, "Crumbling Necropolis": 1,
                       "Drowned Catacomb": 1, "Mountain": 1})
KEY_KEEPS = [
    "Mind Twist", "Magewright's Stone", "Pemmin's Aura",
    "Illusionist's Bracers", "Minamo, School at Water's Edge",
    "Patriar's Seal", "Thousand-Year Elixir", "Lightning Greaves",
    "Waste Not", "Geth's Grimoire", "Liliana's Caress",
    "Tinybones, Trinket Thief", "Tinybones, Bauble Burglar",
    "Tinybones, Pocket Nuisance", "Bloodchief Ascension",
    "Tergrid, God of Fright // Tergrid's Lantern",
    "Chains of Mephistopheles", "Notion Thief", "Oppression",
    "Bottomless Pit", "Wheel of Fortune", "Windfall", "Timetwister",
    "Underworld Breach", "Lion's Eye Diamond", "Yawgmoth's Will",
]
PRIOR_21 = json.loads(r'''{
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
  ],
  "Fire_Lord_Azula": [
    "77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273",
    "refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt"
  ],
  "Garza_Zol__Plague_Queen": [
    "353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244",
    "refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt"
  ],
  "Goro_Goro_and_Satoru": [
    "36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c",
    "refinement/decklists/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24.txt"
  ]
}''')
OTHER_61 = json.loads(r'''{
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
  "Inalla__Archmage_Ritualist": [
    "c9f35cac41a7717ef49b4dd3cb4f6031c2795a0082b31b54a13e645652df9b69",
    "refinement/decklists/Inalla_Archmage_Ritualist_M7_Rev1_Approved_2026-10-24.txt",
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
    "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166",
    "refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt",
    "2026-10-14",
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
    "refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt",
    "2026-10-15",
    "LOCKED"
  ],
  "Obeka__Splitter_of_Seconds": [
    "c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63",
    "refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt",
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

def cards(path):
    rows = []
    quantities = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        assert m, line
        q, name, tag = int(m[1]), m[2], bool(m[3])
        rows.append((q, name, tag))
        quantities[name] += q
    return rows, quantities

class CanonicalGwendlynM7Rev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.deck = cards(APPROVED)
        cls.oldrows, cls.baseline = cards(BASELINE)
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.oracle_file = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in cls.oracle_file["cards"]}
        with TRACKER.open(newline="", encoding="utf-8") as f:
            cls.tracker = list(csv.DictReader(f))

    def test_exact_hash_and_historical_preservation(self):
        self.assertEqual(digest(APPROVED), SHA)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(digest(BASELINE), OLD)
        self.assertFalse(BASELINE.read_bytes().endswith(b"\n"))
        self.assertEqual(self.oracle_file["candidate_raw_sha256"], SHA)
        self.assertEqual(self.oracle_file["baseline_raw_sha256"], OLD)
        self.assertIn(SHA, RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(SHA, VERIFICATION.read_text(encoding="utf-8"))
        self.assertIn("“Approve.”", RECEIPT.read_text(encoding="utf-8"))

    def test_structural_100_physical_95_names_35_lands(self):
        self.assertEqual(len(self.rows), 95)
        self.assertEqual(self.rows[0], (1, "Gwendlyn Di Corci", True))
        self.assertEqual(sum(q for q, _, _ in self.rows), 100)
        self.assertEqual(len(self.deck), 95)
        self.assertEqual(self.deck["Island"], 2)
        self.assertEqual(self.deck["Swamp"], 5)
        self.assertEqual(self.deck["Mountain"], 1)
        self.assertEqual([(q,n) for q,n,_ in self.rows if q>1],
                         [(2,"Island"), (5,"Swamp")])
        self.assertEqual(sum(tag for _,_,tag in self.rows), 1)
        self.assertEqual([n for _,n,_ in self.rows[1:]],
                         sorted([n for _,n,_ in self.rows[1:]], key=str.casefold))

    def test_exact_six_approved_swaps_and_old_owner_keeps(self):
        self.assertEqual(self.deck - self.baseline, SWAPS_ADDS)
        self.assertEqual(self.baseline - self.deck, SWAPS_CUTS)
        for name in KEY_KEEPS:
            self.assertEqual(self.deck[name], 1, name)
        self.assertEqual(sum(self.deck.values()), sum(self.baseline.values()))

    def test_complete_oracle_coverage_legality_colors_game_changers(self):
        m = self.oracle_file
        self.assertEqual(m["status"], "CORY_APPROVED_GWENDLYN_DI_CORCI_M7_REV1_CANONICAL_SOURCE_BOUND")
        self.assertEqual((m["physical_cards"], m["distinct_names"]), (100,95))
        self.assertEqual(set(self.oracle), set(self.deck))
        self.assertEqual(len(m["cards"]), 95)
        self.assertEqual(m["project_exceptions"], [])
        self.assertEqual((m["power_bracket"],m["archidekt_tags"]),
                         ("4 — Optimized", ["Discard","Wheels","Untap"]))
        lands=0; game_changers=set(); manually=set()
        for name, c in self.oracle.items():
            self.assertEqual(c["quantity"], self.deck[name], name)
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            self.assertIsNotNone(c["mana_cost"])
            self.assertTrue(c["oracle_text"], name)
            if "Land" in c["type_line"]:
                lands+=c["quantity"]
            if c["game_changer"]:
                game_changers.add(name)
            if c["source_kind"]=="published_scryfall_page_manual_review":
                manually.add(name)
                self.assertIsNone(c["oracle_id"])
                self.assertTrue(c["source_url"].startswith("https://scryfall.com/card/"))
            else:
                self.assertEqual(c["source_kind"],"oct23_frozen_scryfall_snapshot")
                self.assertTrue(c["oracle_id"],name)
        self.assertEqual(lands,35)
        self.assertEqual(len(game_changers),17)
        self.assertEqual(manually,{"Sting, the Glinting Dagger","Misty Rainforest"})

    def test_commander_sting_rings_bracers_timing_no_infinite_claim(self):
        oracle=self.oracle
        self.assertIn("Activate only during your turn.",oracle["Gwendlyn Di Corci"]["oracle_text"])
        sting=oracle["Sting, the Glinting Dagger"]
        self.assertIn("At the beginning of each combat, untap equipped creature.",sting["oracle_text"])
        self.assertIn("has haste",sting["oracle_text"])
        self.assertIn("Equip {2}",sting["oracle_text"])
        self.assertEqual(sting["mana_cost"],"{2}")
        rings=oracle["Rings of Brighthearth"]["oracle_text"]
        self.assertIn("pay {2}",rings)
        self.assertIn("copy that ability",rings)
        self.assertIn("copy that ability",oracle["Illusionist's Bracers"]["oracle_text"])
        self.assertIn("discards two cards at random",oracle["Hymn to Tourach"]["oracle_text"])
        self.assertIn("from a graveyard",oracle["Tergrid, God of Fright // Tergrid's Lantern"]["oracle_text"])
        for text in (RECEIPT.read_text(encoding="utf-8"),VERIFICATION.read_text(encoding="utf-8")):
            self.assertIn("three",text.lower())
            self.assertIn("Sting",text)
            self.assertIn("Dauthi",text)

    def test_registry_lock_exact_entry_and_61_other_decks_preserved(self):
        entries=self.registry["decks"]
        self.assertEqual(len(entries),62)
        g=entries[D]
        self.assertEqual(g["approval_status"],"APPROVED")
        self.assertEqual(g["lock_status"],"LOCKED")
        self.assertTrue(g["final_gate_passed"])
        self.assertEqual(g["user_approval_date"],"2026-10-24")
        self.assertEqual(g["approved_list_sha256"],SHA)
        self.assertEqual(g["approved_list_artifact"],str(APPROVED.relative_to(ROOT)))
        self.assertEqual(g["previous_approved_list_sha256"],OLD)
        self.assertEqual(g["previous_approved_list_artifact"],str(BASELINE.relative_to(ROOT)))
        self.assertEqual(g["approval_record_artifact"],str(RECEIPT.relative_to(ROOT)))
        self.assertEqual(g["m7_scryfall_selected_artifact"],str(ORACLE.relative_to(ROOT)))
        self.assertEqual(g["m7_archidekt_tags"],["Discard","Wheels","Untap"])
        self.assertEqual(g["m7_power_bracket"],"4 — Optimized")
        self.assertEqual(set(entries)-{D},set(OTHER_61))
        for deck_id, (sha,artifact,date,lock) in OTHER_61.items():
            other=entries[deck_id]
            # Jeleva is the subsequent independently owner-approved M7 lock.
            # Retain its prior October 14 bytes rather than weakening this regression.
            # Deck #26 later advanced by Cory's separate exact five-swap M7 approval.
            # Retain and hash the original October 14 source, as with Jeleva.
            # Cory's subsequent explicit Deck #27 M7 Rev1 approval supersedes
            # only the registry pointer; the original 2026-10-14 file is immutable.
            # Deck #29's later exact owner-approved M7 replacement; preserve Oct14 bytes.
            if deck_id == "Lord_of_Tresserhorn" and other.get("m7_owner_approval_date") == "2026-10-25":
                self.assertEqual(other["previous_approved_list_sha256"], sha)
                self.assertEqual(other["previous_approved_list_artifact"], artifact)
                self.assertEqual(digest(ROOT / artifact), sha)
                self.assertEqual((other["approved_list_sha256"], other["approved_list_artifact"],
                                  other["user_approval_date"], other["lock_status"]),
                                 ("fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85", "refinement/decklists/Lord_of_Tresserhorn_M7_Rev1_Approved_2026-10-25.txt", "2026-10-25", "LOCKED"))
                self.assertEqual(digest(ROOT / "refinement/decklists/Lord_of_Tresserhorn_M7_Rev1_Approved_2026-10-25.txt"), "fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85")
                continue
            if deck_id == "Grixistax___October_2026" and other.get("m7_owner_approval_date") == "2026-10-25":
                self.assertEqual(sha, "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c")
                self.assertEqual(other["previous_approved_list_sha256"], sha)
                self.assertEqual(other["previous_approved_list_artifact"], artifact)
                self.assertEqual(digest(ROOT / artifact), sha)
                self.assertEqual((other["approved_list_sha256"], other["approved_list_artifact"],
                                  other["user_approval_date"], other["lock_status"]),
                                 ("70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e", "refinement/decklists/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25.txt", "2026-10-25", "LOCKED"))
                self.assertEqual(digest(ROOT / "refinement/decklists/Grixistax_October_2026_M7_Rev1_Approved_2026-10-25.txt"), "70b48148409e849e38d7189bcda032d1c98d74329302563a005f86a86b81279e")
                continue
            if deck_id == "Kess__Dissident_Mage" and other.get("m7_owner_approval_date") == "2026-10-24":
                self.assertEqual(other["previous_approved_source_raw_sha256"], sha)
                self.assertEqual(other["previous_approved_list_artifact"], artifact)
                self.assertEqual(digest(ROOT / artifact), sha)
                self.assertEqual((other["approved_list_sha256"], other["approved_list_artifact"],
                                  other["user_approval_date"], other["lock_status"]),
                                 ("11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4", "refinement/decklists/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.txt", "2026-10-24", "LOCKED"))
                self.assertEqual(digest(ROOT / "refinement/decklists/Kess_Dissident_Mage_M7_Rev1_Approved_2026-10-24.txt"), "11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4")
                continue
            if deck_id == "Jeleva__Nephalia_s_Scourge" and other.get("m7_owner_approval_date") == "2026-10-24":
                expected_sha = "6f2cdafa089c3e923104429f764bed66e500fe20cafb3b00dd4d29488bd52cac"
                expected_path = "refinement/decklists/Jeleva_Nephalia_s_Scourge_M7_Rev1_Approved_2026-10-24.txt"
                self.assertEqual(other["previous_approved_source_raw_sha256"], sha)
                self.assertEqual(other["previous_approved_list_artifact"], artifact)
                self.assertEqual(digest(ROOT/artifact), sha)
                self.assertEqual((other["approved_list_sha256"], other["approved_list_artifact"],
                                  other["user_approval_date"], other["lock_status"]),
                                 (expected_sha, expected_path, "2026-10-24", "LOCKED"))
                self.assertEqual(digest(ROOT/expected_path), expected_sha)
                continue
            if deck_id == "Loki__the_Deceiver" and other.get("m7_owner_approval_date") == "2026-10-25":
                newsha = "919734ad1f60e56a636561815d319ec1eb0fbd0c233265ad5e85064f589c7185"
                newpath = "refinement/decklists/Loki_the_Deceiver_M7_Rev1_Approved_2026-10-25.txt"
                self.assertEqual(other["previous_approved_list_sha256"], sha)
                self.assertEqual(other["previous_approved_list_artifact"], artifact)
                self.assertEqual(digest(ROOT / artifact), sha)
                self.assertEqual((other["approved_list_sha256"], other["approved_list_artifact"],
                                  other["user_approval_date"], other["lock_status"]),
                                 (newsha, newpath, "2026-10-25", "LOCKED"))
                self.assertEqual(digest(ROOT / newpath), newsha)
                continue
            if deck_id == "Lord_Xander__the_Collector" and other.get("m7_owner_approval_date") == "2026-10-25":
                newsha = "de348618961269083a44a3f3e05a7f0be7ddbd7e943da0ac82a115e5e4aeb6cd"
                newpath = "refinement/decklists/Lord_Xander_the_Collector_M7_Rev1_Approved_2026-10-25.txt"
                self.assertEqual(other["previous_approved_list_sha256"], sha)
                self.assertEqual(other["previous_approved_list_artifact"], artifact)
                self.assertEqual(digest(ROOT / artifact), sha)
                self.assertEqual((other["approved_list_sha256"], other["approved_list_artifact"],
                                  other["user_approval_date"], other["lock_status"]),
                                 (newsha, newpath, "2026-10-25", "LOCKED"))
                self.assertEqual(digest(ROOT / newpath), newsha)
                continue
            self.assertEqual((other["approved_list_sha256"],
                              other["approved_list_artifact"],
                              other["user_approval_date"],
                              other["lock_status"]),
                             (sha,artifact,date,lock),deck_id)

    def test_previously_new_m7_21_raw_sha_locks_unchanged(self):
        self.assertEqual(len(PRIOR_21),21)
        for deck_id,(sha,path) in PRIOR_21.items():
            self.assertNotEqual(deck_id,D)
            f=ROOT/path
            self.assertTrue(f.is_file(),path)
            self.assertEqual(digest(f),sha,path)
            self.assertEqual(self.registry["decks"][deck_id]["approved_list_sha256"],sha,deck_id)
            self.assertEqual(self.registry["decks"][deck_id]["approved_list_artifact"],path,deck_id)

    def test_tracker_only_target_row_expected_and_next_inalla(self):
        self.assertEqual(len(self.tracker),62)
        gw=[r for r in self.tracker if r["deck_id"]==D]
        self.assertEqual(len(gw),1)
        r=gw[0]
        self.assertEqual(r["index"],"21")
        self.assertEqual(r["final_list_hash"],SHA)
        self.assertEqual(r["final_gate_passed"],"YES")
        self.assertEqual(r["user_approval_date"],"2026-10-24")
        self.assertIn("M7 Rev1",r["refinement_status"])
        self.assertIn("six",r["high_impact_candidate_triage_complete"].lower())
        self.assertIn("Gwendlyn",r["notes"])
        nxt=[z for z in self.tracker if z["index"]=="22"]
        self.assertEqual(len(nxt),1)
        self.assertEqual(nxt[0]["deck_id"],"Inalla__Archmage_Ritualist")
        self.assertEqual(nxt[0]["user_approval_date"],"2026-10-24")

if __name__=="__main__":
    unittest.main()
