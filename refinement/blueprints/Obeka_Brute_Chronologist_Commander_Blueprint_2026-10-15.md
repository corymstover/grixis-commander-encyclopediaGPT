# Obeka, Brute Chronologist — Commander-First Blueprint

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #44 of 62

## Identity

**Natural ceiling: Power Bracket 4 — Optimized.**

Primary identity: **Delayed Triggers / Extra Turns / Clones**.

Obeka is not generic Grixis control. Her tap ability lets the player whose turn it is end that turn. On our own turn, that converts otherwise temporary or lethal-risk effects into permanent advantage by allowing their delayed `at the beginning of the next end step` liabilities to trigger, then exiling those liabilities from the stack. The deck should therefore maximize effects whose printed drawback is a delayed trigger, plus reliable ways to deploy and activate Obeka immediately.

## Rules-critical sequencing

- Obeka is controlled by us, but **the player whose turn it is chooses whether to end the turn**. On an opponent's turn, that opponent can simply decline; the deck must not depend on Obeka to erase our liabilities during another player's turn.
- For `at the beginning of the next end step` drawbacks, the preferred line is generally to let the trigger go onto the stack during **our** end step and activate Obeka in response. Ending the turn before the end step merely skips that end step; the delayed trigger can then wait for the next turn's end step.
- Ending the turn exiles all spells and abilities currently on the stack, removes creatures from combat, skips to cleanup, and causes `this turn` / `until end of turn` effects to expire normally in cleanup.
- A delayed ability tied to the **next** occurrence does not trigger again after it has triggered once and then been removed from the stack.

Primary rules source: Wizards, *Commander Legends Release Notes* (Obeka). Delayed-trigger behavior cross-checked against Wizards release notes for `next end step` abilities.

## Commander-native engine priorities

### Risky extra turns

- Final Fortune
- Last Chance
- Warrior's Oath
- Alchemist's Gambit
- Glorious End
- Isochron Scepter

`Isochron Scepter + Final Fortune + Obeka` is a recognized three-card infinite-turn/lock engine: cast a Final Fortune copy each turn, then exile its lose-the-game trigger with Obeka during the extra turn's end step.

### Temporary creature/token effects turned permanent

- Fable of the Mirror-Breaker // Reflection of Kiki-Jiki
- Flameshadow Conjuring
- Delina, Wild Mage
- Jaxis, the Troublemaker
- Rionya, Fire Dancer
- Saheeli, the Sun's Brilliance
- Hate Mirage
- Venser, Fervent Forger
- Identity Thief
- Come Back Wrong
- Apprentice Necromancer
- Feldon of the Third Path
- Puppeteer Clique
- Sneak Attack / Purphoros, Bronze-Blooded / Ilharg lines where applicable

These effects either create a delayed sacrifice/exile/return trigger that Obeka can remove, or create the battlefield state from which such a trigger becomes profitable.

### Commander deployment and activation

- Lightning Greaves
- Swiftfoot Boots
- Thousand-Year Elixir
- Arena of Glory
- Minamo, School at Water's Edge
- Hellkite Courser

Hellkite Courser is explicitly retained after red-team review: it bypasses escalating commander tax, gives the commander haste, and creates a delayed return-to-command-zone trigger that Obeka can erase. Current optimized Obeka evidence also treats Hellkite Courser as a high-lift core card.

## Natural-ceiling evidence

Project historical review classified Obeka at **Bracket 4 — Optimized**. Current EDHREC optimized evidence likewise centers the commander around Last Chance, Sundial of the Infinite, Final Fortune, Warrior's Oath, Sneak Attack, Kiki-Jiki, Ideas Unbound, Glorious End, Alchemist's Gambit, and Hellkite Courser rather than a generic cEDH shell.

Current optimized Obeka evidence also supports Identity Thief, Come Back Wrong, Hate Mirage, Isochron Scepter, Swiftfoot Boots, and the newly released Venser, Fervent Forger. This supports a strong combo/engine deck without artificially promoting Obeka into a Grixis turbo-cEDH shell.

## Identity constraints

- Do not add generic Oracle/Consultation or unrelated Breach combo packages merely to inflate abstract power.
- Preserve Underworld Breach only as powerful recursion for the deck's own risky-turn / interaction package; it is not the deck's identity-defining win condition.
- Do not retain generic extra-combat or five-to-seven-mana extra-turn cards when a commander-specific delayed-trigger card produces more leverage.
- Do not overuse cards such as The Master, Multiplied that solve delayed-token liabilities independently of Obeka and thereby reduce commander necessity.
- Do not end the turn prematurely and accidentally push a `next end step` liability into an opponent's end step.

## Final approval-ready architecture

- 100 cards
- 100 distinct names
- 34 lands
- 80 baseline noncommander slots retained
- 19 baseline noncommander slots cut
- no project legality exception required
- recommended Archidekt tags: **Extra Turns / Delayed Triggers / Clones**

Candidate SHA-256: `31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8`
