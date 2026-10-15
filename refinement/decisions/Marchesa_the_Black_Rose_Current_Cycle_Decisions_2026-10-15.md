# Marchesa, the Black Rose — Current-Cycle Decision Closeout

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Candidate SHA-256: `39f02b53cda066484a0546803d8526564f351b65f857ea8a5b1b25703106872a`  
Status: **APPROVAL CANDIDATE — NOT APPROVED / NOT LOCKED**

## Source reconciliation

The authoritative current FINAL CSV/TXT exports reconcile at exactly 100 cards. The raw FINAL TXT source SHA-256 is `d292b21d373085ebe83ddea091bc7f51cf8f59048c987deca5fee2395205cdc9`. The normalized current-cycle project-format baseline SHA-256 is `2e8a3fec0749abe153cc2be45ca89f65a6f9634376f7740a9ff63633a15d3ab7`.

The inherited `deck_card_audit.csv` is stale membership evidence for this commander. Compared with the current FINAL baseline, it incorrectly contains Counterspell, Dusk Legion Zealot, Morbid Opportunist, Sage of Fables, and Solemn Simulacrum while omitting Herald of Secret Streams, Midnight Reaper, Scorn-Blade Berserker, Uncivil Unrest, and Yahenni, Undying Partisan. Current FINAL exports therefore control membership; inherited audit metadata is used only where names still reconcile.

## Commander blueprint and natural ceiling

Marchesa's identity is a +1/+1-counter, sacrifice, death/ETB recursion engine:
1. Put +1/+1 counters on creatures through dethrone and dedicated counter engines.
2. Sacrifice those creatures for mana, cards, interaction, or deterministic win conditions.
3. Use Marchesa's delayed return trigger to recur them at the next end step.
4. Exploit persist and ETB/death triggers while counter placement cancels -1/-1 counters.
5. Close through compact commander-native loops rather than a generic Grixis combo shell.

Natural ceiling: **Power Bracket 4 — Optimized**.

## Exact proposed changes

### Nonland
1. Animate Dead -> Sneak Attack
2. Arcane Denial -> Flare of Denial
3. Black Market Connections -> Agatha's Soul Cauldron
4. Bloodghast -> Twilight Diviner
5. Cauldron of Souls -> Sage of Fables
6. Gray Merchant of Asphodel -> Spark Double
7. Herald of Secret Streams -> Danny Pink
8. Midnight Reaper -> Satoru, the Infiltrator
9. Pawn of Ulamog -> Gev, Scaled Scorch
10. Reassembling Skeleton -> Imperial Recruiter
11. The Ozolith -> Altar of Dementia
12. Village Rites -> Vampiric Tutor

### Lands
13. Crumbling Necropolis -> Badlands
14. Fabled Passage -> City of Brass
15. Haunted Ridge -> Mana Confluence
16. Smoldering Marsh -> Underground Sea
17. Sunken Hollow -> Volcanic Island
18. Xander's Lounge -> Forge of Heroes

## Material decisions

- **Sage of Fables** is restored despite being absent from the ranked candidate file because the stale inherited audit incorrectly treated it as incumbent. It is a high-value Marchesa card: Wizard counter placement, Glen Elendra persist support, and counter-to-card conversion.
- **Gev, Scaled Scorch** converts opponent life loss into +1/+1 counters on entering creatures and directly supports Murderous Redcap persist loops.
- **Satoru, the Infiltrator** draws from creatures entering without being cast, including Marchesa and persist returns.
- **Spark Double** is both flexible copy utility and a deterministic-loop component with Glen Elendra Archmage and Ashnod's Altar.
- **Imperial Recruiter** finds a large share of the compact creature engine and combo package.
- **Twilight Diviner** copies a qualifying creature entering from a graveyard once each turn, directly exploiting Marchesa and persist recursion.
- **Danny Pink** turns the deck's routine +1/+1 counter placement into card draw without requiring a death first.
- **Agatha's Soul Cauldron** supplies instant-speed counter placement, targeted graveyard interaction, and activated-ability reuse; it beats Black Market Connections and The Ozolith on commander-specific function.
- **Altar of Dementia** is a free sacrifice outlet and deterministic mill payoff for loops.
- **Sneak Attack** supplies haste, attack/dethrone access, ETB deployment, and a delayed sacrifice that can be exploited by Marchesa.
- **Flare of Denial** preserves premium interaction while its alternate cost can sacrifice a blue nontoken creature.
- **Forge of Heroes** is retained over a sixth colored-land upgrade because a commander that entered this turn can receive an immediate +1/+1 counter, giving Marchesa her own recursion insurance.
- **Vampiric Tutor** is generic power, but at this optimized ceiling its assembly consistency materially improves the commander-native engine rather than replacing it.

Rejected or deprioritized challengers include Madame Null, Pensive Professor, First Day of Class, Dauthi Voidwalker, Grave Betrayal, Avacyn-style high-mana protection, and theft/value packages that dilute the counter-sacrifice-return plan.

## Mana-base red team

The candidate keeps 34 lands. Five entering-untapped premium colored sources replace slower lands, compensating for Forge of Heroes being colorless while materially improving early U/B/R requirements.

## Closure

- Mandatory 99-slot whole-list audit: **COMPLETE**
- Current FINAL membership reconciliation: **COMPLETE**
- Candidate exhaustion: **COMPLETE**
- Commander-identity review: **PASS**
- Adversarial red-team: **COMPLETE**
- Final serious strategic pass: **ZERO NEW MATERIAL IMPROVEMENTS**
- Exact structural target: **100 cards / 34 lands**
- Complete fail-closed Oracle/rules/legality gate: **PENDING**

No approval or lock may be written until the exact SHA-bound candidate passes the complete gate and the user explicitly approves it.
