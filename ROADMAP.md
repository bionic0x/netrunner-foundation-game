# Game development roadmap

## Foundation — prepared

Separate the v0.2 package from Ante, retain the v0.1 deterministic replay and
six-event fixture, verify exported/embedded dossier parity, and provide one
local validation command. The private GitHub repository has been created. GitHub Actions has not yet
been verified on the remote.

## First playable mission — next

Implement one self-contained HACK THE PLANET Academy investigation based on
the existing synthetic fixture. The player selects a network, inspects an event,
chooses the claim supported by the observations, and records the evidence
still needed. Feedback explains the result and plausible alternatives.

Acceptance:

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
