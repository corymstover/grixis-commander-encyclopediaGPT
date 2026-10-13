# Ashad, the Lone Cyberman — New-Cycle Refinement & Verification Certificate

**Deck:** #5 of 62  
**Verification date:** 2026-10-13 (America/Chicago)  
**Baseline source:** immutable `GrixisFINALTXT60--2026.zip` and `GrixisFINAL60--2026.zip` from the October 12 source package  
**Baseline raw TXT SHA-256:** `2ec9953fe019c05fec1fcc40085b025ac52ead53f332a731365b900e5688ba75`  
**Baseline raw CSV SHA-256:** `10789c18f9fcd80bffc4a428b0982c25420000406716750ccc97b9627ca411fe`  
**Normalized baseline-list SHA-256:** `7d2f6231a8eeba1513b69a955001aac540337ab6ef674d5807e37766e69ef53b`  
**Revised exact-TXT SHA-256:** `a0142c7859626b5592d4ac6ef4711232f3fc765c7e02e1ae0963aecfe16a99e6`

## 1. Structural integrity

- Baseline CSV rows: 95; total copies: 100; distinct card names: 95.
- Revised TXT lines: 95; total copies: 100; distinct card names: 95.
- Commander marker: exactly one, on the first line.
- Singleton/copy compliance: PASS. Repeated card names are basic lands only: Island x3, Mountain x2, Swamp x3. No nonbasic duplicate.
- Land count: 30, unchanged from baseline.
- CSV/TXT reconciliation: PASS; the revised CSV and TXT represent the same 100 copies.
- Actual list delta: +1 Ultron, Artificial Malevolence; −1 Dalek Drone; no other card membership changes.

## 2. Card identity, Oracle, and legality

- Commander Oracle text and identity checked against current published card reference: [Ashad, the Lone Cyberman](https://mtg.wtf/card/who/113/Ashad-the-Lone-Cyberman). Identity is UBR.
- Project-wide current Scryfall default-cards refresh documented by the active-cycle status reports generated `2026-10-13T07:03:26.694525Z` from data bulk-updated `2026-10-12T21:06:24.577Z`; reported 5,964/5,964 exact printing/name matches, with no unresolved Oracle IDs/text, commander identity mismatches, or unexpected illegal statuses outside registered exceptions.
- The inherited deck audit’s three entries marked “not reverified in candidate-ranking table”—Uthros Research Craft, Iron Man, Bleeding Edge, and Poetic Ingenuity—were checked against current published card references. [Uthros Research Craft](https://mtg.wtf/card/eoc/7/Uthros-Research-Craft), [Iron Man, Bleeding Edge](https://mtg.wtf/card/msc/626/Iron-Man-Bleeding-Edge), [Poetic Ingenuity](https://mtg.wtf/card/lci/161/Poetic-Ingenuity).
- Addition Ultron, Artificial Malevolence: current reference reports colorless identity and Commander legal. [Ultron](https://mtg.wtf/card/msh/252/Ultron-Artificial-Malevolence).
- Cut Dalek Drone: current reference reports black identity and Commander legal. [Dalek Drone](https://mtg.wtf/card/who/64/Dalek-Drone).
- The official [Commander banned list](https://mtgcommander.net/index.php/banned-list/) was checked 2026-10-13. The [October 12, 2026 Wizards announcement](https://www.magic.wizards.com/en/news/announcements/banned-and-restricted-october-12-2026) changed Competitive Brawl only; no tabletop Commander change applies to this list.
- No project-specific exception applies.

## 3. Rules and interaction verification

- Ashad casualty 2 requires sacrificing one creature with power 2 or greater as an additional casting cost. If paid, the spell copy resolves before the original; the copy is not cast. The artifact copy becomes a token. [Ashad Oracle/rulings](https://mtg.wtf/card/who/113/Ashad-the-Lone-Cyberman).
- Ultron triggers when another **nontoken** artifact enters under its controller’s control. Its 2 payment creates a token copy. Because the copy is a token, it does not satisfy Ultron’s nontoken-entry condition; this line does not self-loop. [Ultron Oracle](https://mtg.wtf/card/msh/252/Ultron-Artificial-Malevolence).
- When an artifact spell is copied by Ashad, the copy is a token spell copy that resolves before the original. Ultron does not trigger from that token entering, but can trigger when the original artifact permanent enters; this is the relevant sequencing distinction.
- No deterministic infinite combo is added or claimed.

## 4. Candidate and strategic gates

- 16 candidate options reviewed and documented: 1 accepted/implemented, 4 already-included options retained, and 11 rejected with reasons.
- The accepted swap advances the artifact-copy engine and lowers the mana value of the engine piece; the cut’s immediate removal/drain value and Ultron’s 2 trigger cost are explicitly recorded.
- The baseline already contains strong draw, recursion, artifact cost reduction, removal, token production, and copy support. Candidate ranking alone was not treated as an instruction to add a card.

## 5. Consistency and gameplay evidence

No qualified matched-start multiplayer simulator or representative game sample was available for a before/after performance comparison. No win-rate, gameplay superiority, or empirical consistency claim is made. The change is supported by current card text, rules interaction, role fit, and documented opportunity cost rather than invented playtest results.

## 6. Verification gates

| Gate | Outcome | Evidence / limits |
|---|---|---|
| Structural count and singleton | **PASS** | 100 copies; 95 names; 30 lands; commander first; only basic lands repeat. |
| CSV/TXT reconciliation | **PASS** | Exact revised quantity map matches. |
| Identity, Oracle, current legality | **PASS** | Project-wide exact-printing refresh plus direct checks for flagged rows and the add/cut pair. |
| Official Commander banned-list checkpoint | **PASS** | Official list checked 2026-10-13; October 12 B&R changes were Competitive Brawl only. |
| Commander-first blueprint | **PASS** | Artifact casualty, sacrifice triggers, artifact tokens/copies and recursion preserved. |
| Candidate coverage | **PASS** | 16 decisions recorded with rejected alternatives explained. |
| Rules interactions | **PASS** | Casualty copy timing and Ultron nontoken trigger checked. |
| Multiplayer performance | **NOT AVAILABLE** | No qualified matched-start test sample; no win-rate claim. |
| Revision hash and record | **PASS** | Exact TXT hash, candidate ledger, change rows and certificate recorded separately from baseline. |
| Automatic finalization | **PASS** | All mandatory technical gates pass; no separate user-approval gate under the active-cycle protocol. |

**Final status: `APPROVED / LOCKED — ALL TECHNICAL GATES PASSED`.** This status applies only to the exact revised TXT bytes with SHA-256 `a0142c7859626b5592d4ac6ef4711232f3fc765c7e02e1ae0963aecfe16a99e6`. Any later card-list change requires a new verification revision.