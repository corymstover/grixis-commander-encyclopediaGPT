# Sauron, the Dark Lord — mandatory whole-list audit

Date: 2026-10-15  
Cycle: `global-restart-2026-10-13`  
Deck: #50 of 62  
Status: working audit; not user approval

Authoritative baseline: FINAL TXT member `Sauron__the_Dark_Lord.txt` from the frozen October 12 source package.

Candidate: `refinement/decklists/Sauron_the_Dark_Lord_Approval_Ready_2026-10-15.txt`  
Candidate SHA-256: `fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8`

## Audit result

- Commander: **Sauron, the Dark Lord**.
- Noncommander copies adjudicated: **99/99**.
- Result: **91 KEEP / 8 CUT**.
- Baseline: **100 cards / 90 distinct names / 34 lands**.
- Candidate target: **100 cards / 91 distinct names / 34 lands**.
- Candidate repeats: **Nazgûl x7 / Swamp x3 / Mountain x2 only**.
- Singleton: **PASS target** — Nazgûl's own deck-construction text permits up to nine copies; only basic lands otherwise repeat.
- Commander color identity target: **U/B/R**.
- Project legality exception required: **NO**.
- Per-copy adjudication ledger: `refinement/decisions/Sauron_the_Dark_Lord_Whole_List_Decision_Ledger_2026-10-15.csv`.

## Final eight-card delta

1. Warg Rider -> Great Goblin, Foul-Hearted
2. Notion Thief -> Roaming Throne
3. Fellwar Stone -> Mana Vault
4. Counterspell -> Force of Will
5. Drowned Catacomb -> Minas Morgul, Dark Fortress
6. Sulfurous Springs -> Volcanic Island
7. Underground River -> Flooded Strand
8. Island -> Misty Rainforest

## Commander-first findings

- **Great Goblin, Foul-Hearted** upgrades the five-mana Army slot: it amasses Goblins 3 immediately on entry and again whenever it attacks, while giving Armies trample. That directly helps Sauron's Army connect and trigger Ring temptation.
- **Roaming Throne** is a true commander multiplier. Choosing Avatar doubles Sauron's creature-triggered abilities; choosing Wraith instead doubles each Nazgûl's Ring-tempt counter trigger. It preserves the deck's identity rather than adding a commander-independent combo.
- **Minas Morgul, Dark Fortress** is unusually specific here: it can give the Army shadow and make it a Wraith, enabling combat damage while also letting subsequent Nazgûl triggers place counters on that Army.
- **Mana Vault** improves access to a six-mana commander. The selected list does not add a Monolith/Vault combo package; this is acceleration, not strategy replacement.
- **Force of Will** better protects a tap-out Sauron turn while retaining enough blue cards to function as free interaction.
- **Volcanic Island / Flooded Strand / Misty Rainforest** improve untapped fixing and typed-land access while the land count remains 34 and the deck retains Island and Mountain sources for Wonder and Anger.
- The Ring/Nazgûl core remains untouched: Call of the Ring, seven Nazgûl, Claim the Precious, In the Darkness Bind Them, Witch-king of Angmar, Bilbo, The One Ring, The Black Gate, and the Sauron/Saruman package remain central.

## Source reconciliation

The current FINAL TXT is the decklist source of truth. Historical October 11 optimization and the later full-62 review are supporting evidence only. The historical review already rejected One Ring to Rule Them All and generic additional value pieces when they did not beat the established Army/Ring engine. Current optimized EDHREC evidence reinforces the existing Wraith/Army package while surfacing Minas Morgul and newer Hobbit-era Army support as high-fit challengers.

## Candidate exhaustion

Material challengers reviewed include One Ring to Rule Them All; Inherited Envelope; Grishnákh, Brash Instigator; The Mouth of Sauron; Lord of the Nazgûl; Bothersome Noisemaker; My Precious; Moonstone, Harsh Mistress; Smaug, Wicked Worm; Chandra's Ignition; All Will Be One; Shadowspear; Command Beacon; Phyrexian Tower; and generic Oracle/Breach/turbo-combo conversions. None beats the selected configuration without weakening an existing commander-specific role, creating unnecessary redundancy, or diluting the Ring/Army plan.

**Whole-list audit result: PASS FOR CANDIDATE CONSTRUCTION — exact Oracle/legality/rules gate remains required before approval-ready presentation.**
