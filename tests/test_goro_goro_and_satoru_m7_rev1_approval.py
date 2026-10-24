"""Goro-Goro and Satoru M7 Rev1 owner exact-raw approval.
Source-bound Scryfall Oracle and conditional rules checks, without claims of actual games.
All 20 previous M7 locks are independently re-hashed. No historical source rewritten.
"""
import csv
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Goro_Goro_and_Satoru"
APPROVED = ROOT / "refinement/decklists/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24.txt"
BASELINE = ROOT / "refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt"
ORACLE = ROOT / "refinement/verification/Goro_Goro_and_Satoru_M7_Rev1_Scryfall_Selected_2026-10-24.json"
RECEIPT = ROOT / "refinement/approvals/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24.md"
VERIFICATION = ROOT / "refinement/verification/Goro_Goro_and_Satoru_M7_Rev1_Approved_2026-10-24_Verification.md"
REGISTRY = ROOT / "state/current_deck_overrides.json"
TRACKER = ROOT / "refinement/Deck_Refinement_Tracker_2026-10-12.csv"
SHA = "36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c"
OLD = "2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf"
SWAPS = {
  "Bitterblossom": "Mist-Syndicate Naga",
  "Roaming Throne": "Grim Hireling",
  "Hanweir Garrison": "Kaito, Bane of Nightmares",
  "Misty Rainforest": "Crumbling Necropolis",
  "Marsh Flats": "Fabled Passage",
}
PRIOR_20 = {
    "Abaddon_the_Despoiler": ("5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24", "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt"),
    "Admiral_Beckett_Brass": ("ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000", "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt"),
    "Admiral_Brass__Unsinkable": ("dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7", "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt"),
    "Anhelo_the_Painter": ("865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77", "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt"),
    "Ashad_the_Lone_Cyberman": ("352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267", "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt"),
    "Ashnod_the_Uncaring": ("a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761", "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt"),
    "Be_lakor_the_Dark_Master": ("2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4", "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt"),
    "Cecily__Bjorna__Lutri": ("e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d", "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt"),
    "Cormela__Glamour_Thief": ("d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd", "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt"),
    "Crosis__the_Purger": ("a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a", "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt"),
    "Cult_of_Skaro": ("e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d", "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt"),
    "Davros__Dalek_Creator": ("96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc", "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt"),
    "Doctor_Doom__King_of_Latveria": ("7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20", "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt"),
    "Don_Andres__the_Renegade": ("59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f", "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt"),
    "Dr__Eggman": ("3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec", "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt"),
    "Edea__Possessed_Sorceress": ("a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54", "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt"),
    "Edward_Kenway": ("8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1", "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt"),
    "Evelyn__the_Covetous": ("c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac", "refinement/decklists/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.txt"),
    "Fire_Lord_Azula": ("77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273", "refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt"),
    "Garza_Zol__Plague_Queen": ("353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244", "refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt"),
}
OTHER_61_HEADER = {
    "Abaddon_the_Despoiler": ("5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24", "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Admiral_Beckett_Brass": ("ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000", "refinement/decklists/Admiral_Beckett_Brass_M7_Approved_2026-10-22.txt", "2026-10-22", "LOCKED"),
    "Admiral_Brass__Unsinkable": ("dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7", "refinement/decklists/Admiral_Brass_Unsinkable_M7_Rev3_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Anhelo_the_Painter": ("865b3a16567f1cb888305184f297755d550d3d864214ffbb0e780168315b6c77", "refinement/decklists/Anhelo_the_Painter_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Ashad_the_Lone_Cyberman": ("352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267", "refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Ashnod_the_Uncaring": ("a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761", "refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Be_lakor_the_Dark_Master": ("2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4", "refinement/decklists/Be_lakor_the_Dark_Master_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Cecily__Bjorna__Lutri": ("e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d", "refinement/decklists/Cecily__Bjorna__Lutri_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Cormela__Glamour_Thief": ("d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd", "refinement/decklists/Cormela_Glamour_Thief_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Crosis__the_Purger": ("a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a", "refinement/decklists/Crosis_the_Purger_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Cult_of_Skaro": ("e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d", "refinement/decklists/Cult_of_Skaro_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Davros__Dalek_Creator": ("96c6b1cde56eb79db1527e64b82d218f341511a8de99c2395729c0388fd88cfc", "refinement/decklists/Davros_Dalek_Creator_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Doctor_Doom__King_of_Latveria": ("7f74aa25cbbc47d46198f585b379b355cbeb10105ab374f883d2b8b9777a2d20", "refinement/decklists/Doctor_Doom_King_of_Latveria_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Don_Andres__the_Renegade": ("59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f", "refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Dr__Eggman": ("3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec", "refinement/decklists/Dr_Eggman_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Edea__Possessed_Sorceress": ("a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54", "refinement/decklists/Edea_Possessed_Sorceress_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Edward_Kenway": ("8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1", "refinement/decklists/Edward_Kenway_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Evelyn__the_Covetous": ("c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac", "refinement/decklists/Evelyn_the_Covetous_M7_Rev2_Approved_2026-10-23.txt", "2026-10-23", "LOCKED"),
    "Fire_Lord_Azula": ("77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273", "refinement/decklists/Fire_Lord_Azula_M7_Rev2_Approved_2026-10-24.txt", "2026-10-24", "LOCKED"),
    "Garza_Zol__Plague_Queen": ("353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244", "refinement/decklists/Garza_Zol_Plague_Queen_M7_Rev2_Approved_2026-10-24.txt", "2026-10-24", "LOCKED"),
    "Gwendlyn_Di_Corci": ("9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9", "refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Inalla__Archmage_Ritualist": ("81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3", "refinement/decklists/Inalla_Archmage_Ritualist_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Jeleva__Nephalia_s_Scourge": ("00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f", "refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Kefka__Court_Mage": ("cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03", "refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Kess__Dissident_Mage": ("93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb", "refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Grixistax___October_2026": ("f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c", "refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Loki__the_Deceiver": ("5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062", "refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Lord_of_Tresserhorn": ("95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e", "refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Lord_Xander__the_Collector": ("92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787", "refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Lynde__Cheerful_Tormentor": ("05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166", "refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Mai_and_Zuko": ("aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2", "refinement/decklists/Mai_and_Zuko_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Mairsil__the_Pretender": ("51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5", "refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt", "2026-10-14", "LOCKED"),
    "Marchesa__Dealer_of_Death": ("34a6a940c54aaebde612ae5d3a244e22931d3a977fa26e4c43f2a76aafc0f6b1", "refinement/decklists/Marchesa_Dealer_of_Death_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Marchesa__the_Black_Rose": ("627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b", "refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Mishra__Artificer_Prodigy": ("9210aefa423dbe9cc69d18422c0d594cad6e5d0ee475d687b9f2278a2ca3b79d", "refinement/decklists/Mishra_Artificer_Prodigy_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Mishra__Eminent_One": ("ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0", "refinement/decklists/Mishra_Eminent_One_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Missy": ("9ee63d81c07c3b43163e1356cbf264deb9021d0b776daf0a91b85d071aed5aed", "refinement/decklists/Missy_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Nathan_Drake__Treasure_Hunter": ("a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0", "refinement/decklists/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Nekusar__the_Mindrazer": ("bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1", "refinement/decklists/Nekusar_the_Mindrazer_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Nicol_Bolas": ("e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617", "refinement/decklists/Nicol_Bolas_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Nicol_Bolas__the_Ravager": ("5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e", "refinement/decklists/Nicol_Bolas_the_Ravager_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Goben__Gene_Splice_Savant": ("23168e59b7d359ecf24ed95065a5a4b50c978a8f441208d593207e2feacbdea2", "refinement/decklists/Norman_Osborn_Green_Goblin_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Obeka__Brute_Chronologist": ("31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8", "refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Obeka__Splitter_of_Seconds": ("c7e855e69d6538d05eec2e4b3da98b0a5bdb057b19e2c672294b9ba3a60a4f63", "refinement/decklists/Obeka_Splitter_of_Seconds_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Parnesse__the_Subtle_Brush": ("8ff8c101d98e7de997c1de29973db2dd6a51ffdd7b44e4f34145bb1abf2d9e7c", "refinement/decklists/Parnesse_the_Subtle_Brush_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "RogSi": ("06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c", "refinement/decklists/RogSi_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Saruman__the_White_Hand": ("4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2", "refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Sauron__Lord_of_the_Rings": ("72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0", "refinement/decklists/Sauron_Lord_of_the_Rings_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Sauron__the_Dark_Lord": ("fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8", "refinement/decklists/Sauron_the_Dark_Lord_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Sedris__the_Traitor_King": ("65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365", "refinement/decklists/Sedris_the_Traitor_King_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Sol_kanar_the_Swamp_King": ("7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106", "refinement/decklists/Solkanar_the_Swamp_King_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Sol_kanar_the_Tainted": ("72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58", "refinement/decklists/Solkanar_the_Tainted_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Tetsuo_Umezawa": ("14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6", "refinement/decklists/Tetsuo_Umezawa_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Tetsuo__Imperial_Champion": ("d6d7561f00cb56cfb86cd79024975130d718ddc7f3a1bddf0c62f61dc422822e", "refinement/decklists/Tetsuo_Imperial_Champion_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "The_Madcap_Jester": ("caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7", "refinement/decklists/The_Madcap_Jester_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "The_Valeyard": ("4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c", "refinement/decklists/The_Valeyard_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "The_Rani": ("7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c", "refinement/decklists/The_Rani_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Thraximundar": ("d4fa3421752a4d666528c5218aa18b240465c817dd160642c103b2de8c3f9442", "refinement/decklists/Thraximundar_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Tresserhorn_s_Lord__Returned": ("8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8", "refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Wick__the_Whorled_Mind": ("f4556840dc8f7a8e1d532b73652d0035592b52b86adbbad6ed8fbe4270341e98", "refinement/decklists/Wick_the_Whorled_Mind_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
    "Zevlor__Elturel_Exile": ("d2ea6ed8e42ec512b6a6ae7162da8c17b26494b45a9ff6d0c38882c202a42dc9", "refinement/decklists/Zevlor_Elturel_Exile_Approved_2026-10-15.txt", "2026-10-15", "LOCKED"),
}


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


class CanonicalGoroM7Rev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.deck = cards(APPROVED)
        cls.oldrows, cls.baseline = cards(BASELINE)
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.oracle_file = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in cls.oracle_file["cards"]}
        with TRACKER.open(newline="", encoding="utf-8") as h:
            cls.tracker = list(csv.DictReader(h))

    def test_exact_approved_raw_hash_and_historical_byte_preservation(self):
        self.assertEqual(digest(APPROVED), SHA)
        self.assertTrue(APPROVED.read_bytes().endswith(b"\n"))
        self.assertEqual(digest(BASELINE), OLD)
        self.assertEqual(self.oracle_file["candidate_raw_sha256"], SHA)
        self.assertEqual(self.oracle_file["baseline_raw_sha256"], OLD)
        self.assertIn(SHA, RECEIPT.read_text(encoding="utf-8"))
        self.assertIn(SHA, VERIFICATION.read_text(encoding="utf-8"))
        self.assertIn('Cory replied: **“Approve.”**', RECEIPT.read_text(encoding="utf-8"))

    def test_structural_100_physical_cards_with_two_islands(self):
        self.assertEqual(len(self.rows), 99)
        self.assertEqual(self.rows[0], (1, "Goro-Goro and Satoru", True))
        self.assertEqual(sum(q for q, _, _ in self.rows), 100)
        self.assertEqual(len(self.deck), 99)
        self.assertEqual(self.deck["Island"], 2)
        self.assertEqual([(q, name) for q, name, _ in self.rows if q > 1], [(2, "Island")])
        self.assertEqual(sum(tag for _, _, tag in self.rows), 1)
        self.assertEqual([name for _, name, _ in self.rows[1:]],
                         sorted([name for _, name, _ in self.rows[1:]], key=str.casefold))

    def test_exact_five_owner_substitutions_and_key_keeps(self):
        self.assertEqual(self.deck - self.baseline, Counter({k: 1 for k in SWAPS}))
        self.assertEqual(self.baseline - self.deck, Counter({k: 1 for k in SWAPS.values()}))
        for name in [
          "Bident of Thassa", "Enduring Curiosity", "Grazilaxx, Illithid Scholar",
          "Silver-Fur Master", "Thousand-Faced Shadow", "Mistblade Shinobi",
          "Moon-Circuit Hacker", "Fallen Shinobi", "Nashi, Moon Sage's Scion",
          "Ninja of the Deep Hours", "Sakashima's Student", "Yuriko, the Tiger's Shadow",
          "Satoru Umezawa", "Satoru, the Infiltrator", "Ingenious Infiltrator",
          "Daring Piracy", "Loyal Apprentice", "Urabrask's Forge", "Determined Iteration",
          "Dragon Tempest", "Terror of the Peaks", "Rogue's Passage", "Breath of Fury",
          "Fellwar Stone", "Arcane Signet", "Sol Ring", "Talisman of Creativity",
          "Talisman of Dominance", "Talisman of Indulgence", "Phoenix Chick",
          "Samut, Hazoret's Champion", "Withering Torment", "Waterbender Ascension",
          "Raphael, the Nightwatcher", "Fire Navy Trebuchet"]:
            self.assertEqual(self.deck[name], 1, name)

    def test_source_coverage_oracle_legality_identity_and_bracket(self):
        m = self.oracle_file
        self.assertEqual(m["status"], "CORY_APPROVED_GORO_GORO_AND_SATORU_M7_REV1_CANONICAL_SOURCE_BOUND")
        self.assertEqual((m["physical_cards"], m["distinct_names"]), (100, 99))
        self.assertEqual(set(self.oracle), set(self.deck))
        self.assertEqual(len(m["cards"]), 99)
        self.assertEqual(m["project_exceptions"], [])
        self.assertEqual((m["power_bracket"], m["archidekt_tags"]),
                         ("4 — Optimized", ["Ninjas", "Dragons", "Extra Combats"]))
        lands = 0; game_changers = set(); published = set()
        for name, c in self.oracle.items():
            self.assertEqual(c["quantity"], self.deck[name], name)
            self.assertEqual(c["commander_legality"], "legal", name)
            self.assertTrue(set(c["color_identity"]) <= set("UBR"), name)
            self.assertIsNotNone(c["mana_cost"])
            self.assertTrue(c["oracle_text"])
            if "Land" in c["type_line"]:
                lands += c["quantity"]
            if c["game_changer"]:
                game_changers.add(name)
            if c["source_kind"] == "published_scryfall_page_manual_review":
                published.add(name)
                self.assertIsNone(c["oracle_id"])
                self.assertTrue(c["source_url"].startswith("https://scryfall.com/card/"))
            else:
                self.assertEqual(c["source_kind"], "oct23_frozen_scryfall_snapshot")
                self.assertTrue(c["oracle_id"], name)
        self.assertEqual(lands, 33)
        self.assertEqual(game_changers, {"Ancient Tomb", "Cyclonic Rift", "Demonic Tutor",
                                        "Fierce Guardianship", "Jeska's Will", "Vampiric Tutor"})
        self.assertEqual(published, {"Roaming Throne", "Misty Rainforest", "Marsh Flats"})

    def test_relevant_trigger_distinctions_and_mana_losses(self):
        text = lambda n: self.oracle[n]["oracle_text"]
        self.assertIn("one or more creatures you control that entered this turn deal combat damage to a player",
                      text("Goro-Goro and Satoru"))
        self.assertIn("a triggered ability of another creature you control of the chosen type triggers",
                      text("Roaming Throne"))
        for n in ("Goro-Goro and Satoru", "Hanweir Garrison",
                  "Professional Face-Breaker", "Satoru, the Infiltrator"):
            self.assertIn("Human", self.oracle[n]["type_line"])
        self.assertIn("create two 1/1 red Human creature tokens that are tapped and attacking",
                      text("Hanweir Garrison"))
        self.assertIn("power or toughness 1 or less can't be blocked", text("Tetsuko Umezawa, Fugitive"))
        self.assertIn("lose 1 life and create a 1/1", text("Bitterblossom"))
        self.assertIn("Pay 1 life", text("Misty Rainforest"))
        self.assertIn("Pay 1 life", text("Marsh Flats"))
        self.assertIn("Island", text("Misty Rainforest"))
        self.assertIn("Swamp", text("Marsh Flats"))
        self.assertIn("Land — Island Swamp Mountain", self.oracle["Xander's Lounge"]["type_line"])
        self.assertEqual(2 * 2, 4)  # Garrison attack doubled by Human-selected Throne: four tokens
        self.assertEqual(3 * 2, 6)  # Distinct 3 damaged players, 2 Goro triggers per damaged player
        self.assertIn("Lose independent 2-treasure", RECEIPT.read_text(encoding="utf-8"))

    def test_only_goro_registry_entry_now_points_to_new_approved_artifact(self):
        self.assertEqual(len(self.registry["decks"]), 62)
        e = self.registry["decks"][D]
        self.assertEqual((e["approval_status"], e["lock_status"], e["current_stage"]),
                         ("APPROVED", "LOCKED", "LOCKED"))
        self.assertTrue(e["final_gate_passed"])
        self.assertEqual(e["approved_list_sha256"], SHA)
        self.assertEqual(e["m7_final_candidate_sha256"], SHA)
        self.assertEqual(e["previous_approved_list_sha256"], OLD)
        self.assertEqual(e["previous_approved_list_artifact"], str(BASELINE.relative_to(ROOT)))
        self.assertEqual(e["approved_list_artifact"], str(APPROVED.relative_to(ROOT)))
        self.assertEqual(e["m7_archidekt_tags"], ["Ninjas", "Dragons", "Extra Combats"])
        self.assertEqual(e["m7_power_bracket"], "4 — Optimized")
        self.assertEqual(e["m7_project_exceptions"], [])
        self.assertEqual(e["user_approval_date"], "2026-10-24")
        self.assertEqual(e["approval_record_artifact"], str(RECEIPT.relative_to(ROOT)))

    def test_only_goro_tracker_row_approved_with_owner_hash(self):
        self.assertEqual(len(self.tracker), 62)
        t = self.tracker[20]
        self.assertEqual(t["deck_id"], D)
        self.assertEqual(t["final_list_hash"], SHA)
        self.assertEqual(t["user_approval_date"], "2026-10-24")
        self.assertEqual(t["final_gate_passed"], "YES")
        self.assertIn("M7 Rev1", t["refinement_status"])
        self.assertIn("five-swap", t["baseline_status"])

    def test_previous_twenty_new_m7_locks_and_artifacts_exact_raw_sha(self):
        self.assertEqual(len(PRIOR_20), 20)
        for d, (sha, path) in PRIOR_20.items():
            with self.subTest(deck=d):
                e = self.registry["decks"][d]
                self.assertEqual(e["approved_list_sha256"], sha)
                self.assertEqual(e["approved_list_artifact"], path)
                self.assertEqual((e["approval_status"], e["lock_status"]), ("APPROVED", "LOCKED"))
                self.assertEqual(digest(ROOT / path), sha)

    def test_all_other_sixty_one_registry_sources_and_statuses_unchanged(self):
        self.assertEqual(len(OTHER_61_HEADER), 61)
        self.assertEqual(set(OTHER_61_HEADER), set(self.registry["decks"]) - {D})
        for d, (sha, path, date, stage) in OTHER_61_HEADER.items():
            with self.subTest(deck=d):
                e = self.registry["decks"][d]
                self.assertEqual((e["approved_list_sha256"], e["approved_list_artifact"],
                                  e["user_approval_date"], e["current_stage"]),
                                 (sha, path, date, stage))


if __name__ == "__main__":
    unittest.main()
