# Ashnod the Uncaring — Commander-First Blueprint

**Refinement date:** 2026-10-13  
**Frozen baseline:** `GrixisFINALTXT60--2026.zip`, member `Ashnod_the_Uncaring.txt`  
**Frozen baseline SHA-256:** `d1b74569999818542ec3b787499c2a9e3d8a420c617af9b883cc875c324dd684`

## Commander identity

Ashnod is a Grixis artifact-sacrifice commander whose triggered ability copies an activated ability or spell when its controller sacrifices a **nontoken permanent** to activate that ability or cast that spell. It can trigger only once each turn. The copied ability does not require paying its activation costs a second time. The deck's central task is to use nontoken artifact and creature sacrifices to generate additional value while retaining a dense artifact engine, recursion, sacrifice outlets, and artifact-death payoffs.

## Baseline identity retained

The baseline already contains a strong artifact-sacrifice shell: Altar of Dementia, Arcbound Ravager, Blasting Station, Ashnod's Altar, Krark-Clan Ironworks, Grinding Station, Time Sieve, artifact recursion (Emry, Goblin Engineer, Goblin Welder, Scrap Trawler, Scrap Welder, Myr Retriever), and death/artifact payoffs (Disciple of the Vault, Marionette Apprentice, Mayhem Devil, Reckless Fireweaver). These remain intact.

## Auto-approved refinement

**Cut Commander's Sphere; add Trading Post.** Trading Post provides four repeatable activated modes, including sacrificing a creature to return an artifact card from the graveyard to hand, or sacrificing an artifact to draw a card. Either sacrifice ability can trigger Ashnod; if it is the first such trigger that turn, Ashnod copies the activated ability, allowing two artifact cards to be returned or two cards to be drawn for one sacrificed permanent and one activation cost. Trading Post also supports artifact/creature resource conversion and can make Goat tokens.

The tradeoff is meaningful: Commander's Sphere is a three-mana mana rock and can be sacrificed for a copied draw ability; Trading Post costs four mana, does not produce mana, and its useful modes require mana and tapping. The cut is justified by the baseline's already dense ramp package and Trading Post's broader commander-specific recursion/draw utility, not popularity alone.

EDHREC's current Ashnod page reports Trading Post at roughly 52% inclusion and 45x lift in the all-decks view; the project candidate ranking placed it #2, with 52.3212% inclusion and 45.331325 lift in a 3,188-deck snapshot. No gameplay win-rate claim is made.
