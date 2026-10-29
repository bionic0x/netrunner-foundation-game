# Game development roadmap

## Foundation — implemented

Separate the v0.2 package from Ante, retain the v0.1 deterministic replay and
six-event fixture, verify exported/embedded dossier parity, and provide one
local validation command. The standalone GitHub repository has been created.
Its first CI run was blocked before execution by the account's billing or
spending limit; remote validation must be reported separately from local tests.

## First playable mission — v0.3 implemented

Ghost Signal is a self-contained HACK THE PLANET Academy investigation based
on the existing synthetic fixture. The player selects a network, inspects
three events in sequence, chooses the supported claim and requests missing
evidence. Feedback explains each result and plausible alternatives.

Implemented acceptance criteria:

- A complete start → investigation → decision → explanation → replay loop.
- A hypothesis and an unknown cannot be presented as verified evidence.
- Solana and Arbitrum observations remain independently scoped.
- Scoring rewards supported reasoning and recognising uncertainty.
- Mission reset works, all interactions are keyboard-accessible, and the
  mission remains usable on a narrow screen.
- Game progress is separate from the immutable research dossier; no score
  changes its claims or digest.

## Later iterations

Add scenario selection, local progress with an explicit reset control, richer
recovery investigations, and a versioned content format. Evaluate usability
before expanding the number of missions. Historical data and read-only pilots
remain separate research gates in the consolidated blueprint.
