# Obeka, Brute Chronologist — Approval-Ready Verification

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #44 of 62  
Exact candidate SHA-256: `31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8`  
Status: **APPROVAL_READY — NOT APPROVED / NOT LOCKED**

## 1. Current-state recovery

Authoritative current-cycle repository state contains **43 APPROVED / LOCKED decks** through Norman Osborn // Green Goblin. The reconciled tracker identifies **Obeka, Brute Chronologist** as the next unlocked deck (tracker index 43 / deck 44 of 62).

No previously locked deck was modified during this refinement.

Result: **PASS**.

## 2. Authoritative baseline reconciliation

Authoritative membership source: October 12 FINAL exports.

- FINAL TXT: `GrixisFINALTXT60--2026.zip / Obeka__Brute_Chronologist.txt`
- Raw FINAL TXT SHA-256: `6d17e49e7a6d35c9be222bb7bd81f74fb5406e0d6a3102fb190c4da5c1d799c8`
- FINAL CSV: `GrixisFINAL60--2026.zip / Obeka__Brute_Chronologist.csv`
- Raw FINAL CSV SHA-256: `9db88f37351da92a08ec066b62fb3087301504a0317f2a5d626ad0d9e5ab0d24`
- Baseline total: **100 cards**
- Baseline distinct names: **100**
- Baseline lands: **34**
- Repeated names: **none**
- CSV/TXT membership reconciliation: **PASS**

Historical October 11 artifacts are evidence only. The October 12 FINAL exports control current membership.

Result: **PASS**.

## 3. Mandatory whole-list audit

Artifact: `refinement/verification/Obeka_Brute_Chronologist_Whole_List_Audit_2026-10-15.md`

- Baseline noncommander copies adjudicated: **99/99**
- KEEP: **80**
- CUT: **19**
- Proposed additions: **19**
- Candidate total: **100**
- Candidate distinct names: **100**
- Candidate lands: **34**

Result: **PASS**.

## 4. Commander-first blueprint / natural ceiling

Final identity: **Delayed Triggers / Extra Turns / Clones**.

Natural ceiling: **Power Bracket 4 — Optimized**.

Project historical review classified Obeka at Bracket 4. Current optimized Obeka evidence remains centered on commander-native risky-turn, temporary-copy, Sneak Attack/reanimation, and end-the-turn engines rather than a generic Grixis cEDH shell. The final candidate therefore strengthens the commander-specific engine while refusing unrelated Oracle/Consultation/Breach homogenization.

Recommended Archidekt tags: **Extra Turns / Delayed Triggers / Clones**.

Result: **PASS**.

## 5. Current Oracle / end-the-turn rules gate

Current Obeka text checked against Wizards' *Commander Legends Release Notes*:

`{T}: The player whose turn it is may end the turn.`

Wizards confirms that ending the turn:
1. exiles all spells and abilities from the stack;
2. removes attacking/blocking creatures from combat;
3. checks state-based actions without putting new triggers on the stack;
4. ends the current phase/step and skips to cleanup; and
5. performs cleanup in full.

Rules consequences independently applied to this candidate:

- On our turn, we may choose to end the turn. On another player's turn, **that player** chooses whether to end it.
- Ending the turn **before** a `next end step` trigger occurs does not permanently eliminate it; the skipped trigger can wait for the next turn's end step.
- The correct Obeka pattern is normally to let the delayed `next end step` ability trigger on our end step and then end the turn with that ability on the stack.
- Wizards release-note guidance confirms that once a delayed ability tied to the **next** occurrence has triggered and that triggered ability is removed/countered, it will not trigger again on the following occurrence.
- `until end of turn` effects still expire normally in cleanup; Obeka does not make those durations permanent.

Result: **PASS**.

## 6. Commander-specific interaction verification

### Isochron Scepter + Final Fortune + Obeka

EDHREC's current combo database independently records this as a three-card **infinite turns / lock** line. Scepter repeatedly casts Final Fortune; on each extra turn, Final Fortune's lose-the-game trigger is put on the stack during the end step; Obeka ends the turn and removes that trigger.

Result: **PASS**.

### Identity Thief

Wizards' *Eldritch Moon Release Notes* confirms Identity Thief exiles another target nontoken creature when it attacks and returns it at the beginning of the next end step. If that delayed return ability is on the stack during our end step, Obeka may end the turn and exile that ability. Identity Thief's copy duration is only `until end of turn` and ends during cleanup.

Result: **PASS**.

### Come Back Wrong

Wizards' *Duskmourn: House of Horror Release Notes* confirms the spell destroys the target creature, returns that card under our control, then requires it to be sacrificed at the beginning of our next end step. Obeka can remove that delayed sacrifice trigger after it triggers.

Result: **PASS**.

### Hate Mirage

Wizards' Commander 2019 notes confirm the two copied creatures gain haste and are exiled at the beginning of the next end step. Obeka can remove the delayed exile trigger after it triggers.

Result: **PASS**.

### Fable of the Mirror-Breaker // Reflection of Kiki-Jiki

Wizards' Kamigawa: Neon Dynasty notes confirm Reflection creates a hasty copy token and instructs its controller to sacrifice it at the beginning of the next end step. The delayed sacrifice liability is compatible with the same Obeka sequencing.

Result: **PASS**.

### Apprentice Necromancer

Wizards' Ultimate Masters notes confirm Apprentice Necromancer returns a creature with haste and creates a next-end-step sacrifice trigger. Obeka may remove that trigger after it triggers.

Result: **PASS**.

### Venser, Fervent Forger

Wizards' current *Reality Fracture Release Notes* confirm Venser's permanent-copy mode creates two copies of an opponent's permanent, grants haste, and creates a next-end-step sacrifice trigger. Obeka can remove those delayed sacrifice triggers. Venser's alternate spell-copy mode remains useful independently.

Result: **PASS**.

### Thousand-Year Elixir

Current Wizards rules text confirms we may activate abilities of creatures we control as though those creatures had haste and can pay `{1}, {T}` to untap target creature. This allows a newly controlled Obeka to use her tap ability immediately without claiming that Elixir grants actual haste.

Result: **PASS**.

### Arena of Glory

Wizards' current Oracle/update guidance confirms Arena enters untapped if we control a Mountain, taps for red, and its exert ability can produce `{R}{R}`; if any of that mana is spent on a creature spell, that spell/resulting creature gains haste. This can accelerate Obeka and permit immediate commander activation.

Result: **PASS**.

### Hellkite Courser

Red-team conclusion: KEEP. It bypasses commander tax, puts Obeka directly onto the battlefield, gives her haste, and creates a delayed return liability Obeka is built to manage. Current optimized Obeka evidence also shows Hellkite Courser as a high-lift core card. Footsteps of the Goryo was rejected rather than forcing a weaker cut.

Result: **PASS**.

## 7. Mana-base red team

Candidate remains at **34 lands**, matching baseline.

Final mana structure:
- 9 fetchlands;
- Badlands / Underground Sea / Volcanic Island;
- Blood Crypt / Steam Vents / Watery Grave;
- Xander's Lounge;
- City of Brass / Mana Confluence / Command Tower / Reflecting Pool;
- Luxury Suite / Morphic Pool / Training Center;
- Ancient Tomb;
- Arena of Glory / Minamo;
- Otawara / Takenuma / Bojuka Bog;
- Shivan Reef / Sulfurous Springs;
- Island / Mountain / Swamp.

Fast mana retained: Chrome Mox, Lotus Petal, Mana Vault, Sol Ring, Arcane Signet, Fellwar Stone, Izzet Signet, all three Talismans, Ancient Tomb, Jeska's Will.

No further land reduction is justified because Obeka costs four, commander tax matters, and the deck contains multiple five- and six-mana engines.

Result: **PASS**.

## 8. Color identity / singleton / exact structure

Exact candidate:
- **100 cards** including commander
- **100 distinct English card names**
- **34 lands**
- **no repeated card names**
- commander color identity **U/B/R**
- every nonland addition is colorless or within U/B/R
- every land addition is legal within U/B/R identity

Result: **PASS**.

## 9. Current official Commander legality

Fresh checkpoint date: **2026-10-15**.

Wizards' current banned/restricted page was reviewed for the Commander section. None of the exact candidate cards appear on the current Commander banned list. The October 12, 2026 B&R announcement made Competitive Brawl changes but did not announce a Commander ban-list change affecting this deck.

- unexpected banned card: **none**
- project exception required: **none**
- Obeka candidate official Commander legality: **PASS**

Result: **PASS**.

## 10. Candidate exhaustion / adversarial closure

The final serious pass challenged:
- all 19 proposed swaps;
- all 80 retained baseline slots;
- Hellkite Courser and The Master, Multiplied directly;
- Footsteps of the Goryo, Goryo's Vengeance, Cauldron Dance, Sedris, Dawn of the Dead, Nightscape Familiar, Face Yourself, Time Stop, Mimic Vat, Orthion, and generic extra-turn alternatives;
- delayed-trigger timing and active-player choice;
- commander-haste/untap density;
- interaction/protection density;
- all 34 lands;
- generic cEDH win packages.

Hellkite Courser survived red-team. The Master remained a cut because its strongest function substitutes for Obeka's delayed-trigger management. No rejected candidate materially improves the list without a greater opportunity cost in commander dependence, curve, mana, redundancy, or encyclopedia differentiation.

**ZERO NEW MATERIAL IMPROVEMENTS.**

Result: **PASS**.

# Final result

**APPROVAL_READY — NOT APPROVED / NOT LOCKED**

Exact candidate SHA-256:
`31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8`

Do not write current-cycle approval/lock state until explicit user approval of this exact SHA-bound candidate.
