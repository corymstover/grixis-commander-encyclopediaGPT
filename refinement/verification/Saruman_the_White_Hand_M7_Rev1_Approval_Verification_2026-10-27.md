# Deck #48 Saruman, the White Hand — M7 Rev1 exact approval verification

Date: 2026-10-27 (America/Chicago)
Cycle: `global-restart-2026-10-13`

- **Approved raw UTF-8 SHA-256:** `dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b`
- **Previous October 15 raw SHA-256:** `4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2`
- **100 physical cards:** PASS (one commander + 99 library cards)
- **97 distinct card names / singleton:** PASS, only Island x2, Mountain x2, Swamp x2
- **31 printed/front-face lands + four land MDFCs:** PASS, 35 functional land-capable slots
- **Commander color identity:** U/B/R PASS; Saruman itself unchanged
- **Current Scryfall collection API:** 97/97 distinct names resolved, 100 physical card identities; all Commander legal and U/B/R. Four MDFCs resolved by front-face names and full two-face Oracle objects.
- **Official Commander banned cards / exceptions:** no prohibited card; project exception none
- **Exact list diff:** seven one-for-one replacements and 92 unchanged main-deck physical card slots plus commander; approved source preserved
- **Rules:** Saruman triggers on CAST noncreature spells; copies put onto stack do not trigger. Mind's Desire storm copies may enable cast-from-exile spells; Arcane Bombardment instructs casts of card copies; Tainted Strike gives infect to the Army and Chandra's Ignition has that Army deal its damage to opponents; Valakut Awakening is an MDFC spell/land; Temporal Trespass remains MV11 despite delve (UUU floor); March of Swirling Mist phasing can protect Army and commander, X affects stack MV; Chaos Warp may replace target permanent with an opponent's new permanent. Original Blood for Blood God MV11, Volcanic Salvo locked reduction and Black Gate targeting caveats retained.
- **Commander-native preserved:** high printed mana value / reduced actual cost package (Blasphemous Act, Blood for the Blood God!, Volcanic Salvo, Dig/Cruise, Force of Will), Army protection/payoffs (Orcish Medicine, Siegemaster, Fall of Cair Andros, Soul's Fire, Chandra's Ignition, All Will Be One, The Great Goblin, Mauhúr, Harmonic Prodigy, Veyran, Wizard's Staff).
- **Strategic tradeoffs:** seven exact M7 Rev1 Commander-first decisions in engineering review; no forced count cap, no claimed multiplayer win-rate improvements. Reduced creature backups and Mana Geyser burst; new build prioritizes Army damage, free cast triggers and proactive protection.
- **Exact-head engineering gate:** [GitHub PR #729](https://github.com/corymstover/GrokBotMTGCompanion/pull/729) head `ef3bcd2d41e7212a8fd86c7c34b9745a69deefe2`, [workflow run #40476457970](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40476457970), SUCCESS. Both offline source/candidate SHA checks and live Scryfall audit passed.
- **Owner:** 2026-10-27 explicit single-message approval of exact candidate SHA and canonical lock.
- **New approved artifact:** `refinement/decklists/Saruman_the_White_Hand_M7_Rev1_Approved_2026-10-27.txt`
- **Prior approved artifact:** `refinement/decklists/Saruman_the_White_Hand_Approved_2026-10-15.txt` unchanged

This verification is a per-deck source-bound certification. It does not assert a fresh independent third-model M6 audit or completion of the overall 62-deck M7/M8 milestones.
