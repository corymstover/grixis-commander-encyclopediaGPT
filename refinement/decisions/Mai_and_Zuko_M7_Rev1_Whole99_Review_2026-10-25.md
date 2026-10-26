# Deck #32 — Mai and Zuko — independent M7 Rev1 seven-swap owner candidate

**State:** APPROVED and canonically LOCKED after Cory's one “Approve” on 2026-10-25. This is the preserved preapproval strategic assessment with its final owner decision recorded.
**Source:** `corymstover/grixis-commander-encyclopediaGPT` `main`, `refinement/decklists/Mai_and_Zuko_Approved_2026-10-14.txt`; original October 14 approval preserved.
**Original exact raw SHA-256:** `aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2`.
**New exact 100-line raw SHA-256:** `8cdf614e47eadf3ec33049a770a3f0a2b84338e84c31bb26a49e6f26f5c60d97`.
**Current-cycle authority:** User must say one ordinary "Approve" to this complete candidate. Do not require a second owner utterance for routine tests, PR merges or canonical certification; preserve source evidence.

## Commander-first objective

Mai and Zuko cost `{1}{U}{B}{R}` and grant flash timing to **Ally and artifact spells**, with firebending 3 on attack. The commander changes timing, not costs; firebending mana is available only during combat and can be spent on flashed artifacts or Allies. Build an instant-speed artifact-and-Ally engine, opponent-turn value and battlefield interaction, with redundant compact artifact combo finishes. Do not convert to generic Thoracle/Consultation turbo. Natural ceiling **Bracket 4 — Optimized**; no budget ceiling.

The complete 99 has been challenged by role: 31 land faces (including Sink's land half), high-density no-budget artifact accelerants and colored fixing, 10 Ally creatures including commander, 33 artifact spells, card draw, blue stack protection, temporary and permanent removal, combat mana/firebending, flash token engines, tutors, and three retained combo families. All baseline names were compared to their role replacements; cuts below are neither unquestioned nor imposed by a five-swap cap.

## Exactly seven changes relative to the preserved approved list

| Addition | Cut | Commander-first value and honest opportunity cost |
|---|---|---|
| Verdant Catacombs | Sulfurous Springs | Fetches an untapped typed Grixis dual/shock, chooses two colors based on hand, fills graveyard for Breach. Loses unconditional BR tapping land with no shuffle/life beyond tapping. |
| Spire of Industry | Path of Ancestry | Artifact-rich field reliably supports untapped any-color mana; removes an unconditional tapland. Loses free scry on Ally casts and demands an artifact/one life for color. |
| Sink into Stupor // Soporific Springs | Xander's Lounge | Pay 3 life to make a blue land untapped when needed, otherwise a flexible spell/permanent bounce effect. Loses a three-color typed triome, fetch target and cycling. Sink is tempo, not permanent exile/removal. |
| Jeska's Will | Chaos Warp | Commander-present main-phase mana burst plus exiled three-card impulse access can convert into artifact sequences or Breach/Forge storm. The real loss is unconditional instant catch-all removal of problematic enchantments/permanents; must be countered or bounced instead. |
| Pact of Negation | Lightning Greaves | Zero-mana protection for a decisive combo or counter war; keeping colored interaction available while casting artifacts can matter. Loses haste plus proactive shroud on Mai and Zuko; failure to pay `{3}{U}{U}` on upkeep loses the game. |
| **Fire Nation Turret** | **Avatar Roku, Firebender** | 3-mana **flashable artifact** that starts each combat giving a creature +2/+0 and firebending 2. Target Mai and Zuko to yield **five red mana** when their two firebending abilities trigger on attack; this is a repeatable, earlier-stage commander payoff. Loses Roku's remarkable six red on every player's attack and its red pump sink; late-game ceiling decreases. |
| **Forensic Gadgeteer** | **Tundra Tank** | Artifact casts investigate (including opponents' turns when Mai and Zuko are out), and artifact activated abilities cost `{1}` less down to one. **Basalt Monolith's `{3}` untap becomes `{2}`**, so tap for three, pay two to untap, repeat for net +1 colorless **without Rings**; improves combo redundancy and Clue economy. Loses the flashable Tank's ETB creature indestructibility and crew-dependent firebending 1. |

The last two upgrades are independent challenges to the saved five-swap Grok WIP draft PR #680, **not** copied automatic candidate-rank additions. Seven is the quality-derived count, not a new mandated swap number.

## Full-list and candidate triage

**Protected:** Ally Encampment; Fire Lord Azula (copies spells cast while attacking); Fire Nation Occupation (opponent-turn token engine); Firebender Ascension (copies combat-attack triggers after four counters); Zuko, Firebending Master (experience-to-firebending); Katara; Boiling Rock Rioter graveyard interaction; The Blue Spirit; Roaming Throne on Ally; The Mechanist clue engine; Bender's Waterskin; Unwinding Clock; Emry, Jhoira, Sai, Urza, and Uthros Research Craft; the existing mana and combo suites.

**Most credible rejected alternatives:**

- `Grim Monolith` over `Fellwar Stone`: Grim offers colorless opponent-turn bursts with Unwinding Clock, but does **not** itself loop profitably with Rings (tap 3, untap cost 4 reduced by no Gadgeteer unless it is on board; with Gadgeteer cost 3, net zero); cutting a two-mana colored source hurts the commander. Saved WIP's 20k finite goldfish put T4 commander deployment 52.42% in its six-swap Grim portfolio versus 54.49% in its five-swap portfolio; these are only a simplified proxy, not win rates.
- `Arid Mesa` over `Bojuka Bog`: faster untapped source, but removes standalone graveyard hate, which matters in Breach/Reanimate pods. A 20k goldfish with a different Bog-cut package suggested improved T4 deployment but did not model enemy graveyard lines; the evidence cannot justify sacrificing that interaction.
- `Whir of Invention` over `Wishclaw Talisman`: artifact-only instant tutoring is excellent, but `{U}{U}{U}` is awkward in a deck often floating red combat mana. Wishclaw costs less blue and finds any piece, though its activation is sorcery-speed and gives away the artifact.
- `Mox Amber` over a Talisman: Commander and many legend permanents make Amber live sometimes, but it can be dead before a legend, sacrificing consistent fixing. Saved baseline goldfish rejected it.
- `Kappa Cannoneer` over `Toxic Deluge`: a growing evasive artifact threat but loss of essential board control. Rejected.
- `Fire Nation Turret` was omitted from the saved five-swap WIP as a `Talisman of Dominance` cut. **Reconsidered with a different cut**, Avatar Roku; preserve colored acceleration.
- `Forensic Gadgeteer` was surfaced by commander-specific EDHREC optimized High Lift and an off-rank combo challenge. **Reconsidered with Tundra Tank as cut**, not the artifact ramp or combo pieces.


### Two actual higher-count complete-100 alternatives

- **Eight-swap land alternative:** the seven selected changes **plus Arid Mesa / minus Bojuka Bog**, staged as a separate exactly 100-card file, raw SHA-256 `a73ac5672bd890b25c3e12454804bf705711482b696e72f5dc39972fe1d88ece`. Better untapped acceleration, but surrendering targeted graveyard-exile land in a Breach-heavy pod loses a real matchup tool.
- **Eight-swap acceleration alternative:** seven changes **plus Grim Monolith / minus Fellwar Stone**, staged separately, raw SHA-256 `4922e70ed3e38bba38bc85ad4e689d8ff2e3957c63ba0244d4f047ca2161f39f`. Its colorless burst and Clock synergy do not replace Fellwar's early UBR fixing, and saved finite proxy cases for analogous Grim package depressed T4 commander access.

Both alternatives have full physical 100s and precise seven-plus-one deltas. The seven-swap selection wins on balanced color, graveyard defense and direct commander payoff; **eight was considered rather than assumed better**.

## Structural and rules verification

- One commander, 99 other physical cards, **100 distinct names**, 31 cards usable as lands including Sink MDFC, and no duplicates or companion.
- Exactly seven adds and seven cuts relative to source; every selected name within U/B/R. Selected 99 names matched saved Scryfall Oct 23 Oracle/legality archive; **Forensic Gadgeteer** separately checked against the official Wizards release notes and Scryfall card as of Oct 25. Official Wizards October 12, 2026 banned-list announcement and current Commander list checked for unexpected bans; no project exception used.
- Basalt + Rings yields unbounded colorless: with tapped Basalt, pay three to untap and two to copy; copy untaps, tap for three, original untaps, tap for three = six produced for five paid, net +1. With Gadgeteer present, Basalt alone nets one per untap cycle. **Grim plus Rings by itself is not unbounded mana**.
- Walking Ballista converts unbounded colorless into an actual kill. Bolas's Citadel + Top + Aetherflux Reservoir remains a scalable kill line; `Underworld Breach` + LED + Brain Freeze remains the compact storm line. Longshot/Rebel Bowman, Mystic Forge, Top and reducers remain a separate artifact storm axis.
- The Turret buff must exist when the start-of-combat ability triggers (or resolve before attacks); flashing it in **after** the beginning of combat does not retroactively trigger it. Its granted firebending is separate from Mai and Zuko's innate ability. Roaming Throne choosing Ally can double the commander's attack triggers; Firebender Ascension can copy qualifying attacking-creature triggered abilities.
- Pact upkeep payment is a live `{3}{U}{U}` requirement; it is not a permanently free counterspell. Jeska's Will is a sorcery and **does not** benefit from Mai and Zuko's flash permission.
- Tundra Tank's creature-saving ETB and Roku's six-red multiplayer ceiling are genuinely surrendered. The package is not strictly dominating on every board. Retained 31-land count means the opening land/mox decisions remain unusually tight.

**Bounded evidence limitation:** PR #680 provides 20,000 fixed-seed paired goldfish hands and finite rules grids for the *shared five-swap* land/Jeska/Pact package and larger Monolith alternative. The saved model has simplifying assumptions and does not simulate actual multiplayer wins. The two independently selected engine swaps were audited via exact Oracle and finite mana/combat states, **not** by pretending those previous draws measured their effect. No invented win rate or complete randomized multiplayer simulation.

**Review disposition:** Seven meaningful, identity-specific changes; all seven necessary named tradeoffs documented, no material stronger eighth named. Proposed **Power Bracket 4 — Optimized**; **Archidekt tags: Artifacts / Flash / Firebending**. **OWNER APPROVED 2026-10-25**. M7 Rev1 exact SHA is the newly canonical locked list, while the October 14 prior approval is preserved in its original artifact.
