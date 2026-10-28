# M8 original-P1 bounded batch B — exact-current adversarial witnesses

October 28, 2026. This candidate adds **28 individually executable positive/adversarial finite tests** across five current approved deck sources. A separate, subsequent evidence-register commit must pin the exact tested Git commit, Git blob and successful CI run before any status advances. No deck, approval, exception or lock is changed.

| Approved source | Original deferred P1 candidate IDs | Not proven here |
|---|---|---|
| Sauron, Lord of the Rings `c427805f...` | K4–K7, E1–E2, F2–F3 (8) | W1–W3; opponent graveyard and grave-hate trees |
| Obeka, Splitter of Seconds `f80d8829...` | K4–K6, E1–E2, F2–F3 (7) | W1–W3; recurring extra turns, Reactor absent |
| The Rani `924296ed...` | K4–K5, E1–E3, F3 (6) | W1–W2, F2; multiplayer combat and no-kill claim |
| Sol'kanar the Swamp King `2bd99c56...` | K4–K5, E1–E2, F2 (5) | W1–W3; full loop and library state execution |
| Tetsuo, Imperial Champion `36890584...` | F2–F3 (2) | W1–W3; comprehensive combat, stack and cost trees |

## Scope details

- **Sauron:** On-cast trigger persists when the spell itself is countered. The existing grave creature, Fanatic ETB follow-up, ≤9 Nazgûl exception (four in current source), both Anger/Mountain and Wonder/Island, grave-hate preconditions, and Living Death's pre-exile/sacrifice ordering have bounded opposing witnesses. Living Death affects all players; no opponent response or full battlefield simulation is asserted.
- **Obeka:** Combat damage gives that number of extra upkeep steps; qualifying Roaming Throne doubles the trigger. Time Sieve requires five actual sacrificial artifact permanents; Mechanized Production needs eight same-name artifacts and its upkeep check, not a premature alternate win. Extravagant Replication costs `{4}{U}{U}` and cannot be paid by a six-mana pool short on blue. Darksteel Reactor is absent from the approved source.
- **The Rani:** Another legal target creature is needed for a Mark, actual goaded-combat damage to another opponent for investigation, Academy Manufactor provides one of each artifact token, and a genuine blink may create another Mark. The commander's `{1}{U}{B}{R}` cost is colored. Opponent choices and strategic F2 remain deferred.
- **Sol'kanar:** The two opposite directional gain/loss effects must both be online for a positive lifegain feedback witness, and Top/Citadel repetition needs payable life and live pieces. Commander gains only one life per actual black cast; Coffers requires its two-mana activation and Swamps. No multi-turn winning loop is proven by a one-step predicate. Former Force of Will pitching critique is obsolete if the separately verified M7 current-source absence is accepted as a superseded disposition.
- **Tetsuo:** An equipped attack creates the trigger; removing Tetsuo after it triggered does not by itself undo the trigger. Free-cast option requires a suitable spell in hand of no higher mana value than the Equipment maximum. Former Sword of Wealth and Power critique is obsolete because that card is absent, pending a separate exact-current supersession receipt.

## Certification semantics

The test runner confirms **source SHA and inventory**, original M7 P1 `DEFERRED` status, each included source card and one favorable plus one negated precondition for each selected case. These are narrow **finite mechanics/prerequisite witnesses**, not a Magic rules engine, comprehensive Oracle/stack implementation, simulated multiplayer games, an independently executed win-loop test, or a certificate that all 180 original P1 cases are complete. The remaining W cases and any strategic claims not bounded here stay deferred.

Only a subsequent GitHub evidence PR with the **successful exact-head CI run URL and test blob SHA** can call these 28 `CURRENT_SHA_TESTED`; all other M8 gates remain fail-closed.
