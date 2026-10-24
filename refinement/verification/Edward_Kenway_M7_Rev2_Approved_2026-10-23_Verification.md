# Edward Kenway M7 Rev2 — SHA-bound canonical verification

- Owner explicitly said **"Approve"** 2026-10-23 after the complete 100-card Edward list and exact SHA `8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1`.
- Historical October 14 source raw SHA `a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019` must stay exact; never overwrite.
- Engineering independent source [PR #692](https://github.com/corymstover/GrokBotMTGCompanion/pull/692) HEAD `fb13316667f4f8ccf48407a273a7be7bd0bdda87`, two focused CI runs 40062823155/40062810628 SUCCESS, archival live 2026-10-23 Scryfall. Frozen selected Oracle metadata predates owner's approval; provenance preserved.
- Counts: exactly 100 physical, 98 unique named rows, only Island and Swamp ×2; 35 lands, 13 Vehicles, 22 Pirate/Assassin creatures, seven durable rocks, ten Game Changers; Grixis identity 98/98 and official Commander legal 98/98, no exceptions.
- Exactly five substitutions against historical list. Owner protected Fateful Discovery, Imperial Seal, Time Sieve, Academy Manufactor; corrected first-pass Fellwar Stone/Captain Lannery overcuts.
- Rules: tapped qualifiers each count once for Edward's end step; Vehicle hits exile only from damaged player's library and have ordinary land/cast timing; Bats triggers creation and sacrifice of tokens; Malcolm needs second spell while on field; Mu grants Vehicle flying.
- Passive mana proxy (no mulligan/play sequencing) restores first-pass original Fellwar-based approximation but Petal loss cannot be read as zero true timing cost. No gameplay match rates, win simulation or third-model review claimed.
- Regression requirement: other 16 M7 locks exact, 62 authority records, only Edward registry and one tracker row mutate.
- Require exact-head GitHub checks, PR merge, independently refetch merged canonical main and compute `8c01f2be6190be3e3af0fc5ba45eca16faa1b9346981f840811e4b63822c5ee1` before reporting canonical lock complete.
