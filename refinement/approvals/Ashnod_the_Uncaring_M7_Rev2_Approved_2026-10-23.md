# Ashnod the Uncaring — explicit M7 Rev2 owner approval and canonical lock

Date: **2026-10-23** (America/Chicago)  
Cycle: `global-restart-2026-10-13`  
Owner: **Cory Stover**  
Decision: **APPROVED / LOCKED** — exact Deck #6 ChatGPT independent M7 Rev2 nine-swap candidate, raw SHA-256 `a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761`.

## Exact authorization and scope

Cory replied to the complete 100-card approval presentation immediately:

> I approve

The preceding assistant message explicitly asked: "Do you explicitly approve Ashnod the Uncaring M7 Rev2, SHA `a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761`, for canonical locking?" That message displayed the full 100-card list, all nine changes, Power Bracket 4, three tags, exact SHA, verification and engineering PR #681.

Approval applies to the **exact 100-card raw bytes** and this one deck only. It is not an approval of the earlier GrokBot five-swap candidate, future changes, or acceptance of aggregate M6.10, M7 or M8 milestones. Cory's ordinary 'Proceed' authorizations are not deck approvals.

## Provenance and preservation

- New canonical exact approved file: `refinement/decklists/Ashnod_the_Uncaring_M7_Rev2_Approved_2026-10-23.txt`, raw SHA-256 `a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761`.
- Historical October 13 approved Ashnod file: `refinement/decklists/Ashnod_the_Uncaring_Approved_2026-10-13.txt`, raw SHA-256 `f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf`. It remains present and byte-unchanged.
- Engineering independent review: `corymstover/GrokBotMTGCompanion` PR #681, exact head `c7b907d4aecc97513a6ce3c28ed107aecd5a3be9` (stacked on saved first-pass PR #654).
- Engineering candidate source: `data/grixis/m7/candidate_lists/Ashnod_the_Uncaring_ChatGPT_M7_Rev2_Nine_Approval_Candidate.txt`.
- Exact-head GitHub Actions run #40048290216, success: 9/9 new source-bound Rev2 methods and 29/29 prior Ashnod methods.
- Oracle evidence preserved at `refinement/verification/Ashnod_the_Uncaring_M7_Rev2_Scryfall_Selected_2026-10-23.json`: 95 selected Oct 23 current Scryfall Oracle/identity/legality records, including two rainbow lands via the previously verified canonical Ashad snapshot; no fresh pipeline run.
- Formal owner-equivalent Pass C remains technically **non-independent**, under Cory's documented waiver. The newly source-bound M6 I/J certificate is scoped to a finite local full-100 pool, not a global mathematical or win-rate proof.

## Exactly nine authorized one-for-one changes

| Add | Remove |
|---|---|
| Corridor Monitor | Foundry Inspector |
| Basalt Monolith | Fellwar Stone |
| Aether Spellbomb | Talisman of Indulgence |
| Spawning Pit | Esoteric Duplicator |
| Animation Module | Reckless Fireweaver |
| Priest of Forgotten Gods | Jhoira, Weatherlight Captain |
| Ruthless Knave | Farid, Enterprising Salvager |
| City of Brass | Xander's Lounge |
| Mana Confluence | Exotic Orchard |

## Approval-ready deck identity and mechanics

- Ashnod's unlimited triggered copy applies only to **non-mana** activated abilities of artifacts or creatures for which a permanent was sacrificed to pay the activation cost. Ordinary land activations, mana abilities and resolution-only sacrifices do not qualify.
- Basalt Monolith has two existing-card infinite-colorless routes with Rings of Brighthearth and Forensic Gadgeteer; Walking Ballista stays as a deterministic mana outlet. An infinite-mana state alone is not automatically a win.
- Animation Module extends three Spellbook-indexed combos using Crime Novelist and the existing Ravager, Altar or KCI; this does not mean Ashnod copies Module's triggered ability.
- Spawning Pit + Ashnod + Crime Novelist loop is **manually derived from Oracle** and explicitly requires an initial creature and, if nonartifact, initial mana. It is not falsely presented as a Spellbook-indexed combo.
- Priest of Forgotten Gods is targeted and thus its activation is not a mana ability. Ruthless Knave creates four Treasures after Ashnod copies its paid creature-sacrifice activation; subsequent doubled draw still costs three Treasures.
- 100 physical cards; 95 distinct names; one commander; only Island (3), Mountain (2), Swamp (3) repeat; 33 lands, 8 ramp pieces counting one-use Lotus Petal, six Game Changers, all selected cards officially Commander-legal and within U/B/R, no project exceptions.

**Power Bracket:** 4 — Optimized  
**Archidekt tags:** Ability Copy / Artifact Sacrifice / Artifact Combo

## Canonical-lock constraints

Change only the Ashnod row in `state/current_deck_overrides.json` and tracker; preserve earlier five new-cycle M7 locks and historical artifacts. Independently verify new file raw bytes and source/registry/tracker/tests on PR head; merge only after CI success. Refetch canonical `main` after merge and rehash the exact 100-card file. No automatic re-opening or new approval of any other deck.
