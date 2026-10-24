# Don Andres, the Renegade M7 Rev2 — exact owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Owner: **Cory Stover**  
Cycle: `global-restart-2026-10-13`  
Decision: **APPROVED / LOCKED**, Deck #14 / tracker index 13, exact raw SHA-256 `59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f`.

## Explicit owner authorization

After being shown the complete 100-card Don Andres M7 Rev2 decklist, seven explicit add/cut substitutions, proposed exact raw SHA-256, Bracket 4 / Theft / Pirates / Treasure labels, and [engineering PR #689](https://github.com/corymstover/GrokBotMTGCompanion/pull/689) with exact-head CI SUCCESS, Cory expressly replied:

> Approve

Owner approval covers **only this exact 100-card UTF-8 LF-terminated source**, raw SHA-256 `59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f`, and its canonical lock. It does not approve Deck #15 Dr. Eggman or any future revisions to any earlier locked deck.
Approved canonical file: `refinement/decklists/Don_Andres_the_Renegade_M7_Rev2_Approved_2026-10-23.txt`, 100 physical cards / 99 named entries, only Island 2x.
Historical October14 owner-approved file `refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt` is preserved byte-exact at raw `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`. Keep its historical approved changes and original exports as evidence; no silent overwrite.

## Seven exact approved substitutions

| Added | Removed | On-theme benefit and actual cost |
|---|---|---|
| Gríma, Saruman's Footman | Professional Face-Breaker | Free casts of opposing instant/sorcery on unblockable combat damage, including Dilation/Background payoff. Face-Breaker created early Treasures and own impulse draw; loss explicitly acknowledged. |
| Fallen Shinobi | Seize the Spotlight | Ninjutsu attack enables two opposing top cards played without paying and stolen creature ownership under our control. Ninjutsu/damage must connect; Spotlight offered opponent choice. |
| Treachery | Blasphemous Act | Persistent theft and five-land untap **only when Aura enters**; loses cheap creature sweep in go-wide table, retains Toxic Deluge and Cyclonic Rift. |
| Gloomlake Verge | Shipwreck Marsh | Early always untapped U, conditional B with Island or Swamp. Important correction: Shipwreck Marsh actually enters untapped after two **other** lands of any type, so this is a sequencing tradeoff, not blanket upgrade. |
| Blazemire Verge | Smoldering Marsh | Early untapped B, conditional R when controlling Swamp or Mountain; loses fetchable Swamp Mountain and unconditional late R. Smoldering genuinely needs two **basic** lands to enter untapped. |
| Mind's Dilation | Stolen Strategy | Responds to opponents' first spells on each turn with possible free nonland cast; lost own-upkeep three top exiles to pay. Seven mana versus five and depends on opponent activity. |
| Passionate Archaeologist | Breeches, Eager Pillager | Legal two-mana Background in the library; grants Don mana-value damage on spells cast from exile. Replaces Pirate first-strike attack Treasure, blocker control and own impulse draw; triggers only while our commander creature is on field. |

## Exact mechanical, legality and power gates

- 100 physical / 99 unique name rows: commander 1, Island 2, all other singleton. **35 lands, nine mana rocks**, nine 100-card bounded alternatives archived.
- Current source-bound Scryfall Oracle, name and color identity and Commander legality: 99/99 unique names, official UBR Commander legal, no project exceptions. One off-archive direct Scryfall named API for Passionate Archaeologist Oracle ID `6299d18e-a6a7-414c-85c0-d57a8e7d2627`. Wizards official Background mechanics confirms it can be included in library without choose a Background.
- Five Game Changers: Ancient Tomb, Cyclonic Rift, Fierce Guardianship, Opposition Agent and Vampiric Tutor. **Bracket 4 — Optimized**, tags **Theft / Pirates / Treasure**.
- Don's +2/+2 menace deathtouch Pirate buff affects **creatures we control but another player owns**; a token we create is ours and isn't automatically buffed. Opponent library-card manifests through Thieving Amalgam are opponents' cards, not ours.
- Don triggers on **cast** noncreature opponent-owned spells; copies of spells placed on stack aren't cast. It produces **two tapped Treasure** tokens that cannot pay for the spell just cast or later same-turn stolen spells unless untapped.
- Background grants Don triggered noncombat damage from each **cast spell from exile**, even our own. Damage doesn't count as 21-point combat commander damage. Mind's Dilation allows casts during its trigger resolution but legal targets/mandatory additional costs still apply.
- Gríma's free stolen spell is cast from exile; Fallen Shinobi's land plays follow normal timing, while casts of noncreatures from exile trigger Don and Background.
- Treachery must resolve and enter attached to a legal creature before untapping up to five lands. Existing typed-land count and source restrictions remain materially relevant to 8-mana RRR Insurrection.
- **Corrected erroneous Grok assertion**: Shipwreck Marsh needs two OTHER lands, not basic lands; Smoldering Marsh does require two basics. This was verified from the original archive and preserved as a regression in tests.
- No deterministic infinite, no matched-opening gameplay sample, and **no measured multiplayer win-rate**. Previous owner-equivalent Pass C is not claimed newly independent or re-sealed.

## Exact-head evidence and expected canonical merge steps

- Independent [engineering PR #689](https://github.com/corymstover/GrokBotMTGCompanion/pull/689), exact head `3fc6011ec261e6ecc4f9365b503633b7559a7ab1`; focused [workflow #40058523937](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40058523937) **SUCCESS**, full 100 UTF-8 bytes re-fetched and re-hashed `59c62e50874816a434e0198e272084a3aad619a4eff2e374fc9b38fbdaf62f8f`.
- Registry changes only `Don_Andres__the_Renegade` among 62. Tracker changes only index13. Prior 13 new-cycle M7 locks and historical Oct14 Don source remain byte-exact.
- Canonical PR exact-head workflows must be green, then merge; independently fetch main and rehash exact file and registry/tracker. The approval receipt is not proof of post-merge success until that readback occurs.

