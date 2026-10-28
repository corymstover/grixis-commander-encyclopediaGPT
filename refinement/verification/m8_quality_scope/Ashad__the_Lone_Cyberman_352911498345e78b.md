# M8 exact-current whole-99 review — Ashad, the Lone Cyberman (#5)

2026-10-28. **KEEP the owner-approved M7 Rev3 exact 100, with no proposed changes.** Canonical raw file `refinement/decklists/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23.txt`, SHA-256 `352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267`. 100 physical, 95 names, only Island x3/Mountain x2/Swamp x3 repeated, 32 actual lands, eight static rocks; official Grixis Commander legal, no project exception, Bracket 4, Artifact Copy / Casualty Aristocrats / Artifact Combo. This is not the Oct13 source or research-only five/nine alternatives.

## Authority and relevant independent boundaries

The exact October 23 owner approval and preserved predecessor source are in `refinement/verification/Ashad_the_Lone_Cyberman_M7_Rev3_Approved_2026-10-23_Verification.md`. Engineering [PR #653](https://github.com/corymstover/GrokBotMTGCompanion/pull/653), head `ef7a1f726f26648886cf9b44069f2c8e205df189`, has strict local-best I and technical-provenance-disciplined J for the **Rev3 candidate**, 118-name Oracle/Scryfall research, five complete 100s, eight focused finite tests and seven reported green exact-head checks. A useful pinned source is `data/grixis/m6/ij/tested_pools/Ashad__the_Lone_Cyberman_M7_Rev3_tested_configurations_20261023.json`, Git blob `5cbdc1a5a80912e64fa86de5d81eb5e59617b0b6`. Its five-list alternatives and review result were **candidate-only** when authored; Cory's later exact SHA approval is separately documented. Historic Grok research I/J and owner-equivalent Pass C must **not** be mislabeled a freshly technically independent third-model verdict; no measured win rate was produced. There is also a checked selected-card Scryfall snapshot `refinement/verification/Ashad_the_Lone_Cyberman_M7_Rev3_Scryfall_Selected_2026-10-23.json`. No new live Oracle sweep is claimed on October 28.

**Commander-first mechanism:** Ashad gives casualty 2 only to the **first nonlegendary artifact spell you cast each turn**, allowing a paid power-2+ creature sacrifice to copy it. The copy of an artifact *spell* becomes a token permanent on resolution, but the token is **not created**, so Worldwalker Helm's would-create-token replacement does not add a Map to that event. Sacrificing another creature for casualty or to other outlets grows Ashad by one +1/+1 counter. Opponent-turn value needs a truly permitted artifact cast: Shimmer Myr and Liberator permit flash, and Unwinding Clock helps recharge actual artifact resources. Liberator is **legendary**, begins at **power one**, and cannot itself receive Ashad's casualty 2 or pay it without a buff. Iron Man, Bleeding Edge can copy an artifact spell even if legendary and makes its copy nonlegendary once per turn; this is *not* Ashad making legendary artifacts eligible. Twinning Staff's first replacement adds an extra copy to **artifact-spell copying as well as instant/sorcery copying**; the activated second ability is narrower.

## Every approved noncommander physical slot, each counted exactly once

### 32 lands — Grixis and artifact restrictions, flash-play timing

- 1x Academy Ruins
- 1x Blood Crypt
- 1x Bloodstained Mire
- 1x Command Tower
- 1x City of Brass
- 1x Ancient Tomb
- 1x Exotic Orchard
- 1x Great Furnace
- 1x Inventors' Fair
- 3x Island
- 1x Luxury Suite
- 1x Morphic Pool
- 2x Mountain
- 1x Polluted Delta
- 1x Seat of the Synod
- 1x Mana Confluence
- 1x Steam Vents
- 1x Stormcarved Coast
- 3x Swamp
- 1x Mishra's Workshop
- 1x Training Center
- 1x Underground Sea
- 1x Urza's Saga
- 1x Vault of Whispers
- 1x Volcanic Island
- 1x Watery Grave
- 1x Xander's Lounge

Source count 32 is the real high-risk constraint for an artifact deck with six-to-nine-mana finishers. The ten Rev3 changes replace Crumbling Necropolis/Shipwreck Marsh with untapped City/Mana Confluence; `Delete` and Tezzeret were replaced with restricted artifact acceleration Ancient Tomb/Workshop. **Mishra's Workshop mana can only be spent to cast artifact spells**, not on Ashad, holding up counterspells, generic Helm activation, equip or mana abilities. Ancient Tomb gives colorless at life cost; City and Confluence cost life; legendary/utility and artifact lands can be destroyed as artifacts or otherwise restricted. The 32-land/eight-rock source mix has enough artifact discount/tutoring to justify a bounded local-best choice, but not guaranteed colored access, land drops or recovery after a Vandalblast. This risk is greater than in a generic 36-land casual build and openly remains.

### 8 mana artifacts — real activation/payment constraints

- 1x Arcane Signet
- 1x Cursed Mirror
- 1x Mox Opal
- 1x Rakdos Signet
- 1x Sol Ring
- 1x Talisman of Creativity
- 1x Talisman of Dominance
- 1x Talisman of Indulgence

Cursed Mirror is temporary copy utility and produces red; Opal requires metalcraft, signets need input mana, Tomb/Workshop cannot single-handedly guarantee UBR. Losing Fellwar Stone for Skullclamp costs a source but adds card-flow and changes 1-power bodies into two-power sacrificial candidates. Exiling/destroying artifacts attacks both mana and synergy.

### 19 valuable copy objects, artifact spell bodies, and their output

- 1x Auton Soldier
- 1x Baleful Strix
- 1x Brudiclad, Telchor Engineer
- 1x Cyberdrive Awakener
- 1x Cybermen Squadron
- 1x Ichor Wellspring
- 1x Iron Man, Bleeding Edge
- 1x Solemn Simulacrum
- 1x Necron Deathmark
- 1x Phyrexian Metamorph
- 1x Piggy Bank
- 1x Portal to Phyrexia
- 1x Royal Warden
- 1x Razorlash Transmogrant
- 1x Sculpting Steel
- 1x Simulacrum Synthesizer
- 1x The Cyber-Controller
- 1x Thought Monitor
- 1x Wurmcoil Engine

Ichor Wellspring is a copyable two-mana ETB/death draw engine, although it needs a separate power-2+ creature to fund its own casualty. Royal Warden makes actual 2-power artifact bodies; the unearth version is exiled on leaving battlefield but still grows Ashad when sacrificed. Piggy Bank is 3/2 and supplies Treasure on death. Necron Deathmark has flash, a real creature-destroying ETB and conditional mill; replaces non-flash Noxious Gearhulk at the cost of Gearhulk's life gain and different targeted conditions. Wurmcoil Engine and Portal to Phyrexia are enormous copy ceilings but demand six/nine mana or recursion and can be removed. Auton Soldier copy enters as nonlegendary while its myriad/artifact relationships need exact token events; Brudiclad and Cyberdrive convert already-present token artifact resources into pressure, not immediate deterministic wins. Iron Man's ability is **once per turn**, not an extra casualty grant.

### 20 engine sources — artifact casts, sacrifice, drain, recursion, token copy conversion

- 1x Artificer Class
- 1x Ashnod's Altar
- 1x Biotransference
- 1x Disciple of the Vault
- 1x Emry, Lurker of the Loch
- 1x Esoteric Duplicator
- 1x Goblin Welder
- 1x Ingenious Artillerist
- 1x Krark-Clan Ironworks
- 1x Marionette Master
- 1x Mayhem Devil
- 1x Phyrexian Altar
- 1x Pitiless Plunderer
- 1x Poetic Ingenuity
- 1x Scrap Trawler
- 1x Unwinding Clock
- 1x Urza, Lord High Artificer
- 1x Worldwalker Helm
- 1x Twinning Staff
- 1x Jhoira, Weatherlight Captain

Poetic Ingenuity creates **3/1** Dinosaurs from qualifying once-each-turn artifact casts, so those bodies actually meet casualty 2; its Treasures require Dinosaur attacks. Biotransference can make creature spells artifact spells but Ashad still checks **nonlegendary** and true first-artifact cast of the turn. Ashnod's Altar, KCI and Phyrexian Altar make different mana; none is free sacrifice of noncreatures under a creature-only condition. Disciple triggers on artifact entering a graveyard, not on every artifact token disappearing via exile; Artillerist triggers on artifacts entering, Marionette Master checks artifact departures and its own power, and Mayhem Devil on sacrifices. The retained Marionette Master prevents loss of a critical drain axis from earlier research. Razorlash/Plunderer/Phyrexian Altar requires actual opponent with four nonbasic lands to bring Razorlash back for discounted `{B}{B}`; Altar plus Treasure yields a **mana-neutral** loop, not standalone infinite mana, and a damage payoff or actual Ashad counters are still necessary. Urza + Helm + Artificer Class combo is source-identified, but exact cost, board, targets and untapped artifact resources must be legal in the play; it is not free just because all names are in this list.

### 8 interaction and battlefield protection sources

- 1x Arcane Denial
- 1x Chaos Warp
- 1x Cyber Conversion
- 1x Cyclonic Rift
- 1x Deflecting Swat
- 1x Fierce Guardianship
- 1x Mana Drain
- 1x Their Name Is Death

Arcane Denial and Mana Drain cost colored blue, free Swat/Fierce require a commander, and Cyber Conversion depends on legal targets and the actual disguise/face-down text. Their Name Is Death is a nontrivial board reset and can destroy own artifact engine if relevant; counterspells, Collector Ouphe/Stony Silence and artifact sweepers are real vulnerabilities. The list is not proof that protection is available on demand.

### 12 copy-enabling access, cost reduction, flash and survival

- 1x Demonic Tutor
- 1x Fabricate
- 1x Skullclamp
- 1x Lightning Greaves
- 1x Shimmer Myr
- 1x Liberator, Urza's Battlethopter
- 1x Enthusiastic Mechanaut
- 1x Etherium Sculptor
- 1x Foundry Inspector
- 1x Mystic Forge
- 1x Padeem, Consul of Innovation
- 1x Uthros Research Craft

Shimmer Myr plus Liberator's second broad flash permission is the distinct *Ashad-per-turn* justification for its last approved replacement of Kappa Cannoneer. Losing Kappa's improvise/ward/unblockable pressure is a serious combat-tempo cost; against removal-light combat pods the old Kappa could outperform. The retained 2-mana/3-mana artifact reducers, Forge and card draw help recover from running only 32 lands, but do not create colored mana. Uthros must actually be stationed by sorcery-speed tap of another creature to achieve charge thresholds and card-draw ability; it is not an immediately active free draw artifact. Padeem, Greaves and tutors add different kinds of access/protection, each with timing and payment conditions.

## Original M6 conceptual case accounting on actual Rev3 cards

The original `data/grixis/m6/test_blueprints/Ashad__the_Lone_Cyberman.json` is **DESIGN_ONLY**: five P0 (`C1`, `K1`, `K2`, `K3`, `F1`) and nine P1 (`K4`, `K5`, `E1`, `E2`, `W1`, `W2`, `W3`, `F2`, `F3`). The October 23 strict SHA-bound Rev3 I/J and selected 95 names are genuine scoped supporting evidence, but do not turn that historical design-only blueprint itself into a current independent blanket PASS. New canonical `tests/test_m8_ashad_lone_cyberman_current.py` guards this exact raw 100 and exercises all fourteen **bounded** positive/adverse groups, not a full stack or game implementation.

| Group | Current finite positive case | Adverse/removed-card disposition |
|---|---|---|
| **P0 C1** | First nonlegendary artifact cast can gain casualty 2; sacrifice of another creature grows Ashad. | Legendary or nonartifact spell, absent commander, no eligible power-2 fodder yields no copy. |
| **P0 K1** | Original artifact spell cast once plus paid legal casualty gives a token copy on resolution. | No real sacrifice/previous eligible artifact spell means no additional copy, and no fake cast trigger. |
| **P0 K2** | Spell copy token appears on resolution but is not “created” for Helm's replacement. | Actual separate token *creation* does generate a Map if Helm remains; cannot conflate these. |
| **P0 K3** | Staff's broad first replacement yields two artifact-spell copies from one real casualty. | No live copy event/Staff or eligible source: no multiplier; activated Staff second ability is narrower. |
| **P0 F1** | Protected artifact resources let a copied value artifact resolve. | Artifact sweeper or Ouphe denial can cut rock/artifact board; named cards alone do not protect. |
| **P1 K4** | Biotransference makes nonlegendary creature spells artifacts in zones, allowing qualifying first-cast. | Legendary remains legendary; no first-spell eligibility after prior eligible artifact. |
| **P1 K5** | Iron Man once-per-turn can copy an actual artifact spell except copy isn't legendary. | Ashad itself still can't casualty a legendary original; Iron Man absent/trigger spent means no such copy. |
| **P1 E1** | Real 3/1 Poetic Dinosaur, 3/2 Piggy Bank, 2/2 Solemn, 2/2 Royal Warden bodies pay casualty. | No body or previously spent artifact cast denies copying; artifact-only Mana Workshop cannot pay general cost. |
| **P1 E2** | Shimmer Myr or Liberator allow genuinely flash-cast artifacts on opponents' turns, reusing first-each-turn. | Unwinding Clock untaps resources but does *not itself grant flash*, nor is Liberator's legendary cast eligible. |
| **P1 W1** | Urza, Helm and Artificer Class are all physically present and a finite copy/untap engine step is conditional. | Lack of actual token target, mana, untapped legal resources or active Class level disrupts the claimed loop; no automatic infinity from names. |
| **P1 W2** | Retained Disciple/Mayhem/Marionette/Artillerist receive proper artifact sacrifice/damage events. | Historic *Reckless Fireweaver* part is **SUPERSEDED (removed)**; token exile isn't an artifact-to-grave death, different payoffs trigger differently. |
| **P1 W3** | Wurmcoil and Portal can be copied at full paid mana and 2-power fodder; flash Deathmark gives new ETB pressure. | Historic *Noxious Gearhulk* branch is **SUPERSEDED (removed)**; no unpaid nine-drop or extra Helm Map from copied permanent spell. |
| **P1 F2** | Actual available power-2+ body can fund copy. | Liberator starts power one and 1/1 artifact tokens cannot by themselves pay casualty 2. |
| **P1 F3** | Nonlegendary artifact qualifies. | Legendary artifacts or second qualifying artifact of same turn don't receive Ashad's casualty even if Iron Man would copy them. |

These groups are **accounted for**, not claimed independently full-executed in a Magic engine. Historical W2 Fireweaver and W3 Gearhulk assertions are specifically retired. The earlier Ashad baseline audit's claims that Staff doesn't affect artifact spells, Poetic Dinosaurs are 3/3, or Canoptek Scarab Swarm is 4/4 were **corrected before Rev3**; none is reintroduced as a current fact. Actual Rev3 engineering independent scope remains pinned and clearly distinguished from this bounded canonical M8 family.

## Counterfactual complete-100 pool and stop reason

The full approved ten one-for-one deltas: Crumbling Necropolis → City; Delete → Ancient Tomb; Fellwar Stone → Skullclamp; Kappa Cannoneer → Liberator; Noxious Gearhulk → Necron Deathmark; Reckless Fireweaver → Piggy Bank; Shipwreck Marsh → Mana Confluence; Tezzeret, Master of the Bridge → Mishra's Workshop; Thopter Spy Network → Royal Warden; Thoughtcast → Razorlash Transmogrant. Old alternatives have real strengths (Kappa's evasive pressure, Tezzeret finisher, Fellwar fixing, instant draw), not dismissible as bad cards.

| Alternative complete legal 100 | Most credible upside | Why Rev3 is retained here |
|---|---|---|
| Replace Liberator → Kappa Cannoneer (prior nine-swap) | Strong ward-4 unblockable late finisher, improvise supports tight mana | Removes the second flash-artifact permission on opposing turns, materially reducing Ashad's unique first-each-turn copying ceiling. |
| Replace Ichor Wellspring → Cyberman Patrol (tested ten Patrol) | Adds an immediate afflict damage body and casualty fodder | Removes cheap two-ETB/death draw and copyable card-recovery engine, worse when artifact sacrifice is plentiful. |
| Replace Liberator → Technomancer (tested ten Technomancer) | Copied large ETB may recover many artifacts after wipe | Seven-mana/double-black and graveyard stock requirement are much harder with 32 lands than three-mana reusable flash permission. |
| Replace Skullclamp → Fellwar Stone, Mishra's Workshop → Tezzeret, Master of the Bridge | Regain durable mana fixing plus alternate big artifact-finisher | Reintroduces a six-mana high-color/payoff hand burden while losing card draw and artifact spell burst; mostly attractive in slow controlling pods rather than the intended sacrifice-copy cadence. |

The five-list exact-source Rev3 tested pool (old, nine, ten Patrol, ten Liberator, ten Technomancer) also judged reversion of costed roles, and excluded illegal/off-identity research hits. **The most important acknowledged remaining risk is 32 lands** when artifact hate destroys colored sources/rock acceleration; a slower table may prefer the Kappa version. The owner-approved ten nevertheless maximize repeatable **Ashad-specific artifact copying per turn**, while keeping Wellspring, Poetic 3/1 fodder, Marionette drain and copyable high-end permanents. Under the currently documented evidence no replacement convincingly wins both that ceiling and resilience. **No add/cut recommendation; final M8 is not yet accepted.**
