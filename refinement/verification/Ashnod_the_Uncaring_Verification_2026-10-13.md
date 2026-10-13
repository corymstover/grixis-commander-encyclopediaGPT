# Ashnod the Uncaring — New-Cycle Refinement & Verification Certificate

**Deck:** #6 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline source:** immutable October 12 source package plus `GrixisFINAL60--2026.zip` / `GrixisFINALTXT60--2026.zip`  
**Baseline raw TXT SHA-256:** `d1b74569999818542ec3b787499c2a9e3d8a420c617af9b883cc875c324dd684`  
**Baseline raw CSV SHA-256:** `ffa46ec76b6fcd3f34d726dc124ba92edddcc189bbb749e3ff745916cf78c32b`  
**Normalized baseline-list SHA-256:** `6548ec58378b54ed366a34330e05d166147bd38828ffd1030b7f59f21d2bb91d`  
**Revised exact-TXT SHA-256:** `35f55432f14f70bc3eb70412ea8cad7520363740e240531ff7122d2d8980dcc6`

## 1. Structural integrity

- Frozen baseline CSV/TXT are byte-identical between the current source package and the named FINAL archives.
- Baseline: 100 card copies, 95 distinct names. Revised: 100 card copies, 95 distinct names, 95 lines.
- Commander marker: exactly one, on the first line.
- Singleton/copy compliance: **PASS**. Only basic lands repeat: Island x3, Mountain x2, Swamp x3. No nonbasic duplicates.
- Land count: 33, unchanged.
- CSV/TXT reconciliation: **PASS**; the revised CSV and TXT represent the same 100 card copies.
- Actual list delta: +Oni-Cult Anvil, +Stormclaw Rager; −Commander's Sphere, −Dockside Chef; no other membership changes.

## 2. Card identity, Oracle and legality

- Commander Oracle text and identity checked: [Ashnod the Uncaring](https://mtg.wtf/card/brc/4/Ashnod-the-Uncaring). Identity is UBR. Her ability copies an activated ability of an artifact or creature that is not a mana ability when one or more permanents were sacrificed to pay that ability’s costs.
- Project-wide current Scryfall default-cards refresh, documented in active-cycle records, generated `2026-10-13T07:03:26.694525Z` from bulk data updated `2026-10-12T21:06:24.577Z`; reported 5,964/5,964 exact printing/name matches, with no unresolved Oracle IDs/text, commander identity mismatches or unexpected illegal statuses outside registered exceptions. Ashnod’s 95 baseline card names are covered by this refresh.
- **Oni-Cult Anvil**: current reference confirms BR identity and Commander legality. [Oracle/legal status](https://mtg.wtf/card/neo/230/Oni-Cult-Anvil).
- **Stormclaw Rager**: current reference confirms BR identity and Commander legality. [Oracle/legal status](https://mtg.wtf/card/mom/254/Stormclaw-Rager).
- **Commander's Sphere** and **Dockside Chef** cut references were checked; both are Commander-legal and their current Oracle text matches the tradeoffs recorded. [Sphere](https://mtg.wtf/card/fic/339/Commanders-Sphere), [Chef](https://mtg.wtf/card/neo/93/Dockside-Chef).
- The official [Commander banned list](https://mtgcommander.net/index.php/banned-list/) was checked 2026-10-13. The [October 12, 2026 Wizards B&R announcement](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026) changed Competitive Brawl only; no tabletop Commander change applies.
- No project-specific exception applies.

## 3. Rules and interaction verification

- **Oni-Cult Anvil:** activating `{T}, Sacrifice an artifact` qualifies for Ashnod because an artifact is sacrificed to pay the cost. Ashnod may copy the activated ability; the copy does not require a second artifact sacrifice. Each ability resolution deals 1 damage to each opponent and gains 1 life, so one activation plus the copy yields 2 damage to each opponent and 2 life gained. The sacrificed artifact leaving during your turn also triggers Anvil’s first ability, which can create one Construct; that trigger is limited to once each turn.
- **Stormclaw Rager:** its `{1}, Sacrifice another creature or artifact` ability qualifies for Ashnod. One activation and one sacrificed permanent can yield two draw-card resolutions and two +1/+1 counters on Rager. The ability is sorcery-speed, which is a meaningful restriction; the copy does not ask for a second sacrificed permanent.
- No deterministic infinite combo is added or claimed.

## 4. Commander-first strategic assessment

Ashnod’s unique payoff is doubling activated abilities that require a permanent sacrifice. The two additions each make that precise interaction productive: Anvil converts an artifact into repeated table-wide drain and a Construct trigger, while Rager turns one sacrificed artifact/creature into two cards and two counters. The cuts reduce a slower three-mana ramp piece and a redundant instant-speed draw outlet; color fixing, ramp and instant-speed sacrifice options remain elsewhere in the deck. The list remains an optimized artifact-sacrifice engine/value-combo deck, with the commander’s five-mana deployment and removal vulnerability as real constraints. No exception or forced archetype shift applies.

## 5. Candidate and performance gates

- 16 candidates reviewed: two additions implemented, two existing core candidates retained, and twelve rejected alternatives with reasons.
- Ranking/EDHREC inclusion and Lift data are treated as discovery/association signals from the October 12 project snapshot, not proof of card strength. Legacy synergy is not treated as a current score.
- No qualified matched-start multiplayer simulator or representative game sample was available for a before/after comparison. No win-rate or empirical superiority claim is made. The performance evidence is therefore limited to rules, role fit and transparent opportunity-cost analysis.

## 6. Verification gates

| Gate | Outcome | Evidence / limits |
|---|---|---|
| Baseline preservation | **PASS** | Frozen source package files byte-match the named FINAL archives; baseline hashes recorded. |
| Structural count and singleton | **PASS** | 100 copies; 95 names; 33 lands; commander first; only basics repeat. |
| CSV/TXT reconciliation | **PASS** | Revised quantity maps match exactly. |
| Identity, Oracle, current legality | **PASS** | Current project-wide exact-printing refresh plus direct checks for both additions and cuts. |
| Official Commander banned-list checkpoint | **PASS** | Official list checked 2026-10-13; October 12 changes were Competitive Brawl only. |
| Commander-first blueprint | **PASS** | Sacrifice-cost activated abilities, copy trigger, recursion, artifact tokens and drain routes documented. |
| Candidate decision coverage | **PASS** | 16 decisions; 2 accepted, 2 existing cards retained, 12 rejected with reasons. |
| Rules interactions | **PASS** | Anvil drain-copy and Rager double-draw/counter interactions checked. |
| Multiplayer performance | **NOT AVAILABLE** | No qualified matched-start test sample; no win-rate claim. Explicitly disclosed. |
| Revision hash and record | **PASS** | Exact TXT hash, candidate ledger, actual change rows and certificate recorded separately from baseline. |
| Automatic finalization | **PASS** | All mandatory technical gates pass; active-cycle protocol does not require a separate approval gate. |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`.** This status applies only to the exact revised TXT bytes with SHA-256 `35f55432f14f70bc3eb70412ea8cad7520363740e240531ff7122d2d8980dcc6`. Any later membership change requires a new verification revision.