# Cult of Skaro — Final Verification

Date: 2026-10-13  
Status: AUTO-APPROVED AND LOCKED under the user's standing instruction to auto-approve recommendations after verification. The user explicitly authorized reopening all previously approved/locked decks for this refinement cycle.

## Change
- Cut: 1x Skorpekh Lord
- Add: 1x Ashad, the Lone Cyberman

## Commander-first rationale
Cult of Skaro attacks to generate one of four random payoffs: team-wide +1/+1 counters, two cards, a 3/3 Dalek artifact creature token with menace, or 4 life loss to each opponent. Ashad adds a separate artifact-spell-copy engine to the artifact-creature/token strategy: the first nonlegendary artifact spell cast each turn has casualty 2, allowing a creature of power 2 or greater to be sacrificed to copy that spell. Ashad also grows whenever another creature is sacrificed. The list has artifact density and potential casualty fodder, including Dalek tokens and artifact creatures.

Skorpekh Lord's anthem (+1/+0 and menace for other artifact creatures) is useful, but overlaps with Steel Overseer, Master of Etherium, The Cyber-Controller, and Cult's own counter mode. This is a role tradeoff, not a claim that Skorpekh Lord is intrinsically weak.

## Card verification
- Cult of Skaro: {1}{U}{B}{R}, legendary artifact creature — Dalek, 4/4; current Oracle text reviewed. Source: https://mtg.wtf/card/who/722/Cult-of-Skaro
- Ashad, the Lone Cyberman: {1}{U}{B}{R}, legendary artifact creature — Cyberman, 3/3; Oracle text and casualty rulings reviewed. Official Wizards release notes: https://magic.wizards.com/en/news/feature/magic-the-gathering-doctor-who-release-notes. Card reference/legality: https://mtg.wtf/card/who/113/Ashad-the-Lone-Cyberman
- Skorpekh Lord: {2}{B}, artifact creature — Necron Noble, 3/2; gives other artifact creatures +1/+0 and menace and has unearth. Oracle text and Commander legality reviewed: https://mtg.wtf/card/40k/58/Skorpekh-Lord
- Ashad's UBR color identity fits the commander's UBR identity. Ashad and Skorpekh Lord are listed legal in Commander; no project exception is involved.
- The frozen baseline metadata/legality checkpoint remains supporting evidence for unchanged cards. The frozen CSV/TXT exports are not modified.

## Structural checks
- Total: 100 cards including commander.
- Distinct names: 94.
- Commander: exactly one, first line.
- Singleton: PASS; only basic lands repeat (Island x3, Mountain x3, Swamp x3).
- Delta: one-for-one only; Skorpekh Lord out, Ashad, the Lone Cyberman in.
- Clean-list SHA-256: cc2f7a54479dbe166ada8253d42cc1ac9ebc7b3fdf229d9572f5631f269f3b6f
- Frozen baseline exports remain unchanged.

## Rules and limitations
- Casualty 2 means an additional cost of sacrificing a creature with power 2 or greater; if paid, Ashad copies the artifact spell. The copy is created on the stack and is not cast. An artifact spell copy becomes a token as it resolves.
- Ashad's sacrifice trigger puts a +1/+1 counter on Ashad when another creature is sacrificed. The casualty payment can satisfy this trigger if a creature is sacrificed to pay for a spell.
- This is not a deterministic combo claim. No gameplay win-rate or performance claim is made.

## Final gate
PASS for structural integrity, singleton, commander color identity, candidate Oracle text, candidate Commander legality, and relevant rules interaction review. No representative multiplayer testing or matched-start simulator evidence is available, and no performance claim is made.
