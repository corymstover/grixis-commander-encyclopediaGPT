# Grixistax — October 2026 — Current-Cycle Refinement Decisions

Cycle: `global-restart-2026-10-13`  
Date: 2026-10-14  
Commanders: `Kraum, Ludevic's Opus // Tevesh Szat, Doom of Fools`  
Tracker deck id: `Grixistax___October_2026`  
Authoritative source TXT: `GrixisFINALTXT60--2026.zip / Grixistax___October_2026.txt`  
Authoritative source TXT SHA-256: `ac02379cf1803f317213db663129889ccae6dee9258f76607ec5420a03d1aacd`  
Current-cycle clean baseline: `refinement/verification/grixistax_october_2026_2026-10-14/Grixistax_October_2026_Current_Cycle_Baseline_2026-10-14.txt`  
Clean-baseline SHA-256: `79f7d444bea3616c497ddb922b350fc4cdbf51723bfe34fc601be1127f5ccf5e`  
Approval candidate: `refinement/decklists/Grixistax_October_2026_Approval_Candidate_2026-10-14.txt`  
Approval-candidate SHA-256: `f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c`

## Source reconciliation

The frozen source baseline contains exactly 100 cards, 100 distinct card names, two partner commanders, and 26 lands. `Tainted Pact` therefore has a fully unique-name library. No project-specific legality exception applies.

The first-pass whole-list audit is preserved at `refinement/decisions/Grixistax_October_2026_Whole_List_Audit_2026-10-14.csv`. That audit remains valid except for one explicit final red-team supersession: its `KEEP` decision for `Black Market Connections` is replaced by **CUT**, and `Necropotence` is **ADD**. The exact candidate and this closeout are authoritative for the final proposal.

## Commander blueprint and natural ceiling

**Identity:** Grixis Stax / prison-resource deception. The objective is not to rebuild the list into stock Kraum/Tevesh turbo-combo. The deck should constrict mana, searches, activated abilities, creature engines, graveyards, untaps, and card flow while exploiting commander-generated resources to break parity.

**Kraum:** evasive haste pressure and a card-advantage trigger when an opponent casts their second spell each turn. The final prison suite therefore prefers taxes and resource restrictions over a universal one-spell-per-turn lock that would make Kraum's signature trigger structurally dead.

**Tevesh Szat:** the principal parity engine. His +2 supplies two expendable Thrulls; his +1 converts creatures or planeswalkers into cards. The final list deliberately turns Thrulls into upkeep payments, mana, tutoring, card draw, and Tangle Wire fodder.

**Natural ceiling:** **Power Bracket 5 — fringe / rogue cEDH.** The exact partner pair has current cEDH representation but materially lower tournament conversion than leading partner shells. Optimization therefore retains full cEDH interaction, tutors, acceleration, and compact wins without replacing the deck's defining prison identity with a generic Grixis turbo package.

## Exact current-cycle changes — 12 swaps

### Cuts

1. `Arcane Laboratory` — hard-caps every player at one spell, suppressing Kraum's second-spell trigger and making the Breach/LED/Brain Freeze line nonfunctional while present.
2. `Black Market Connections` — useful parity engine, but final red-team research identified `Necropotence` as the materially stronger cEDH resource engine for a deck that wants to convert life rather than mana into cards after establishing a lock.
3. `Defense Grid` — better as turbo-combo protection than as persistent prison infrastructure; it also reduces opponents' ability to police one another.
4. `Grafdigger's Cage` — directly prevents casting cards from graveyards and therefore shuts off the deck's own `Underworld Breach` route.
5. `Kederekt Parasite` — conditional damage payoff that neither denies resources nor materially exploits the commanders.
6. `Nekusar, the Mindrazer` — five-mana symmetric draw engine gives opponents resources before converting them to pressure and is inefficient at the selected ceiling.
7. `Phyrexian Tyranny` — taxes the deck's own Kraum/Tevesh/Remora/Rhystic draw plan; anti-synergistic despite wheel flavor.
8. `Psychosis Crawler` — five-mana payoff-only card with no lock function and insufficient cEDH impact.
9. `Exotic Orchard` — replaced by a fetchland for deterministic typed-dual/basic access and Breach graveyard fuel.
10. `Luxury Suite` — replaced by a fetchland with broader color selection and graveyard utility.
11. `Training Center` — replaced by a fetchland that improves pre-lock sequencing and typed-dual/basic access.
12. `Urborg, Tomb of Yawgmoth` — can improve opponents' mana and is less commander-specific than `Phyrexian Tower` once `Contamination` is part of the prison package.

### Adds

1. `Damping Sphere` — anti-storm / spell-chain tax that preserves the possibility of an opponent casting a second spell, keeping Kraum's trigger live; unlike Arcane Laboratory it is not a hard one-spell cap.
2. `Necropotence` — premier life-to-cards engine that lets the deck rebuild or stockpile resources while mana is constrained. Its discard-exile tension with Breach is explicitly acknowledged and sequenced around.
3. `An Offer You Can't Refuse` — one-mana broad noncreature interaction appropriate to cEDH stack density.
4. `Contamination` — direct Tevesh engine: Thrulls sustain the upkeep sacrifice while artifact mana helps break parity under the land-mana lock.
5. `Dark Ritual` — cEDH-rate acceleration into Tevesh, tutors, or prison pieces.
6. `Force of Negation` — free noncreature protection on opposing turns without consuming another prison slot.
7. `Mindbreak Trap` — free answer to storm chains and counter-war stacks, especially useful for a slower prison deck.
8. `Skullclamp` — direct Tevesh draw engine: a 0/1 Thrull becomes 1/0, dies to state-based actions, and draws two cards.
9. `Flooded Strand` — fetch fixing, basic access, and graveyard fuel.
10. `Marsh Flats` — fetch fixing, basic access, and graveyard fuel.
11. `Arid Mesa` — fetch fixing, access to typed duals/basic Mountain, and graveyard fuel.
12. `Phyrexian Tower` — commander-specific land-slot engine converting expendable Thrulls into `{B}{B}`.

## Mandatory whole-list audit and parity review

Every baseline slot was challenged rather than treating inherited cards as protected. The following apparent tensions are intentional and must be sequenced rather than ignored:

- `Damping Sphere` reduces `Ancient Tomb` to one colorless mana and taxes spell chains, including a Breach turn. It is retained because the prison value exceeds the sequencing cost; the lock can be removed or played around before the finish.
- `Trinisphere` can make ostensibly free spells cost three mana. `Chalice of the Void` can counter the deck's own zero- or one-mana spells. Both are retained as high-impact prison pieces with explicit deployment sequencing requirements.
- `Blood Moon` plus `Back to Basics` can heavily constrain the deck's own nonbasics. Fetches, basics, fast artifact mana, and ordering are the parity tools.
- `Necropotence` exiles discarded cards and can reduce Breach fuel. It is still the stronger resource engine, but wheels and end-step hand management must account for that replacement effect.
- `Overburden` is retained because it triggers on nontoken creatures; Tevesh's Thrulls bypass it.
- `Tangle Wire` is retained because Thrulls absorb its tap requirement and the controller can order the Wire triggers to remove a fade counter before the tap trigger resolves.
- `Karn, the Great Creator` is retained for its static ability. The deck does **not** rely on Karn's outside-the-game -2 as though Commander had a normal sideboard.

## Win packages

The candidate keeps two compact closing packages that fit the prison shell:

1. `Helm of Obedience` + `Leyline of the Void` or `Dauthi Voidwalker`.
2. `Underworld Breach` + `Lion's Eye Diamond` + `Brain Freeze`, with self-lock sequencing explicitly required.

A third generic `Thassa's Oracle` / `Demonic Consultation` package was rejected. `Ad Nauseam`, `Rite of Flame`, `Cabal Ritual`, `Simian Spirit Guide`, `Final Fortune`, and `Borne Upon a Wind` were likewise rejected as moves toward stock turbo rather than improvements to this deck's commander-first prison identity.

## Candidate exhaustion / rejected challengers

The inherited top-100 candidate table was used as discovery evidence, not an automatic shopping list. High-impact current and inherited challengers were individually considered.

**Accepted from current/inherited evidence:** `Marsh Flats`, `Flooded Strand`, `Arid Mesa`, `Force of Negation`, `Mindbreak Trap`, `Skullclamp`, `Phyrexian Tower`, `An Offer You Can't Refuse`, `Dark Ritual`, and `Necropotence`.

**Accepted from commander/stax red-team rather than inherited ranking pressure:** `Contamination` and `Damping Sphere`.

**Rejected after challenge:**

- `Thassa's Oracle` / `Demonic Consultation` — redundant third win package and a direct move toward generic Grixis turbo.
- `Ad Nauseam` — excellent generic cEDH engine but pushes the deck away from persistent resource denial into turbo sequencing.
- `Gilded Drake` — powerful but substantially weaker through the deck's own `Torpor Orb` and not more important than the chosen lock density.
- `Dress Down` — efficient interaction, but temporary and can also blank Kraum; final slots favor persistent denial/free countermagic.
- `Mnemonic Betrayal` / broad graveyard recursion alternatives — overlap the Breach spell-chain axis rather than increasing prison density.
- `The One Ring` — excellent generic value, but four mana and less commander-specific than the selected resource engines.
- `Hullbreaker Horror` and other high-mana generic control closers — unnecessary with two compact existing wins.
- `Stranglehold` — strong but four-mana redundant search denial alongside `Ashiok, Dream Render` and `Opposition Agent`.
- `Vexing Bauble` — clashes with the deck's own free interaction and zero-mana acceleration.
- `Chains of Mephistopheles` — powerful draw suppression but hostile to Kraum and the deck's own draw engines.
- `Nether Void`, `Smokestack`, and additional broad symmetrical taxes — either overly hostile to deploying two five-mana commanders or too slow relative to the selected prison pieces.

## Closure

The exact candidate is **100 cards / 100 distinct names / 26 lands**, with two legal partner commanders and a fully unique-name `Tainted Pact` configuration.

After source reconciliation, mandatory 99-slot audit, commander-parity review, inherited top-100 candidate challenge, current 2026 exact-pair cEDH comparison, mana-base reconstruction, win-package review, self-lock analysis, and a second adversarial pass that produced the final `Black Market Connections` → `Necropotence` correction, there are **ZERO NEW MATERIAL IMPROVEMENTS** remaining under the project's commander-first stopping standard.

The candidate remains **NOT APPROVED** pending the exact SHA-bound complete fail-closed Oracle/color-identity, official Commander legality, rules, structural, and singleton gate plus explicit user approval.
