# The Valeyard — Candidate Decisions

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c`

Status: **APPROVED / LOCKED** — explicit user approval received 2026-10-15

## Commander-first blueprint

The Valeyard has two unusually narrow commander hooks: opponents face each Villainous Choice an additional time, and its controller gets an additional vote while voting. The optimized shell should therefore maximize real Villainous Choice cards, real Magic voting cards, and effects that create additional Valeyards without immediately losing them to the legend rule. Generic political "choose one" effects do not qualify as voting unless the rules text actually uses vote, and generic Grixis control is secondary to protecting and exploiting the commander.

Natural ceiling remains **Power Bracket 4 — Optimized**. The five-mana commander and mechanic-specific high-mana-value engines reward powerful protection, tutors, fixing, and interaction, but the commander does not naturally support a compact deterministic cEDH shell strongly enough to justify erasing its Villainous Choice / voting identity.

## Final proposed delta

1. Counterspell -> Force of Will
2. The Toymaker's Trap -> Messenger Jays
3. Paradox Haze -> Spark Double
4. Prisoner's Dilemma -> Quantum Misalignment
5. Dalek Drone -> Sakashima of a Thousand Faces
6. Seize the Spotlight -> Auton Soldier
7. Windswept Heath -> Arid Mesa
8. Dragonskull Summit -> City of Brass
9. Drowned Catacomb -> Mana Confluence

## Accepted changes

- **Force of Will:** protects a five-mana commander or a high-leverage political spell while tapped out. The candidate retains **26 other blue cards** that can pay Force's alternate cost, so the protection upgrade is sufficiently supported.
- **Messenger Jays:** Council's dilemma explicitly instructs every player to *vote* for feather or quill. This is direct commander text, not merely a political choice, and therefore converts Valeyard's extra-vote line into additional looting/counters.
- **Spark Double:** can enter as a copy of Valeyard while becoming nonlegendary. This permanently adds another Villainous Choice replacement effect and another extra-vote permission while both survive.
- **Quantum Misalignment:** creates a nonlegendary token copy of Valeyard and has rebound, giving the deck another direct way to stack the commander's two abilities without a legend-rule collision.
- **Sakashima of a Thousand Faces:** can enter as another Valeyard and carries the static ability that the legend rule does not apply to permanents you control. It is one of the cleanest persistent commander-multiplication pieces available in Grixis.
- **Auton Soldier:** can enter as a nonlegendary artifact copy of Valeyard with myriad. When it attacks, the myriad tokens copy the listed nonlegendary/artifact/myriad exceptions, producing temporary additional Valeyard effects for the combat window.
- **Arid Mesa:** corrects a hard mana-base defect. Windswept Heath had no Forest or Plains target in the current list; Arid Mesa has five Mountain-typed targets.
- **City of Brass / Mana Confluence:** unconditional three-color fixing replaces two checklands that can enter tapped. The land count stays at 36.

## Cuts

- **Counterspell:** strong but replaceable. Force of Will preserves the counterspell role while adding zero-mana commander protection when necessary.
- **The Toymaker's Trap:** flavorful political guessing, but it never uses *vote* and does not create a Villainous Choice. Messenger Jays occupies the same broad political space while directly engaging Valeyard's voting text.
- **Paradox Haze:** creates an extra upkeep; it does not copy or multiply either Valeyard ability. It is useful only through other upkeep engines and can increase Mystic Remora's cumulative-upkeep burden. Spark Double is far more commander-direct.
- **Prisoner's Dilemma:** current Oracle has opponents secretly *choose* silence or snitch. Under current Comprehensive Rule 701.38c, that is not an actual vote because the rules text does not use the word "vote." Its original 2024 release-note explanatory bullets used secret-vote terminology, but current Oracle plus current CR govern the interaction. Quantum Misalignment therefore produces materially more Valeyard-specific value.
- **Dalek Drone:** five-mana ETB removal attached to a Dalek is serviceable flavor support, but it neither creates Villainous Choices nor votes nor copies the commander. The deck retains its stronger Dalek/Villainous Choice core.
- **Seize the Spotlight:** opponents choose fame or fortune, but the card never says *vote*; 701.38c therefore prevents it from using Valeyard's extra-vote ability. Auton Soldier is a dramatically more commander-specific political-engine slot.
- **Windswept Heath:** has zero legal fetch targets in the current list.
- **Dragonskull Summit / Drowned Catacomb:** functional lands, but they are the cleanest two remaining mana cuts once the dead fetch is corrected; City of Brass and Mana Confluence enter untapped regardless of board state and fix all three colors.

## Ranked-candidate reconciliation

The local v8.1.4 ranking placed **Auton Soldier #9**, **Quantum Misalignment #10**, **Spark Double #24**, and **Sakashima of a Thousand Faces #48** for The Valeyard. Their acceptance is not based on rank alone: each produces a legally coexisting Valeyard copy or otherwise suppresses the legend-rule problem and therefore multiplies the commander's exact text.

**Messenger Jays** was not available as a normal ranked add because the inherited audit treated it as already present, while the authoritative current FINAL CSV/TXT does not contain it. FINAL CSV/TXT membership controls, so Jays was restored to candidate consideration manually and accepted on commander-text merit.

## Retained commander-specific core

All 13 noncommander Villainous Choice sources from the authoritative baseline are retained: Damocles Base, Sword of Kang; Davros, Dalek Creator; Dr. Eggman; Ensnared by the Mara; Genesis of the Daleks; Great Intelligence's Plan; Hunted by The Family; Midnight Crusader Shuttle; Missy; Sycorax Commander; The Dalek Emperor; The Master, Gallifrey's End; and This Is How It Ends.

The retained voting/political package includes the actual voting cards and payoffs already present rather than replacing the deck with generic Grixis combo-control. The accepted package strengthens the commander's two native axes simultaneously.

## Material challengers rejected

- **Irenicus's Vile Duplication:** good nonlegendary copy effect at four mana, but the accepted copy package is already dense; Quantum's rebound, Spark's permanent body, Sakashima's legend-rule text, and Auton's myriad ceiling each provide a stronger differentiated role.
- **Nanogene Conversion:** potentially explosive by turning all other creatures into nonlegendary Valeyards until end of turn, but it is temporary and board-dependent. It is strongest only after establishing a creature board and then resolving a follow-up Villainous Choice/vote spell in the same turn.
- **Tempt with Reflections:** standalone copies of Valeyard remain legendary, so without a separate legend-rule workaround it cannot leave multiple Valeyards in play. That dependency makes it weaker than the accepted clone suite.
- **Tempt with Mayhem:** political spell-copying is useful, but it does not itself vote or present a Villainous Choice and does not multiply Valeyard's static abilities.
- **Dalek Squadron / Exterminate! / Cyberman support:** thematic and playable, but the current deck already preserves the stronger Doctor Who villain package. None displaces an accepted commander-copy, direct voting, protection, or mana-base upgrade.
- **Propaganda:** strong generic defense, but not a material commander-specific improvement over the retained shell.

## Rules attestation

- Rule 701.38c: "voting" means an actual vote and excludes ordinary choices/decisions that do not use "vote."
- Rule 701.55c: if replacement effects make a player face a Villainous Choice additional times, the full choice process is performed the appropriate number of times **one at a time**.
- Multiple Valeyard permanents therefore stack additively rather than exponentially: each supplies one additional replacement effect for Villainous Choice and one additional vote permission.
- Auton Soldier's myriad copies retain its listed copy exceptions, including being nonlegendary, so a Valeyard-copy Auton can produce temporary nonlegendary Valeyard tokens.
- No infinite combo is asserted from the accepted copy package.

## Closeout

Whole-list audit: **99/99 noncommander copies adjudicated; 90 KEEP / 9 CUT**.

Candidate exhaustion/red-team: **ZERO NEW MATERIAL IMPROVEMENTS** after reviewing the ranked list, manual voting correction, copy-engine alternatives, mana-base defects, and generic-power challengers.

Candidate state: **100 cards / 96 distinct names / 36 lands / basic lands only repeated**.

Natural ceiling: **Power Bracket 4 — Optimized**.

Proposed Archidekt tags: **Villainous Choice / Voting / Political Control**.

## Approval closeout

- Explicit user approval received: **2026-10-15**
- Canonical approved SHA-256: `4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c`
- Exact approved artifact: `refinement/decklists/The_Valeyard_Approved_2026-10-15.txt`
- Current-cycle state: **APPROVED / LOCKED**
- Project exceptions: **none**
- Next unlocked: **Thraximundar (index 58 / deck 59 of 62)**.
