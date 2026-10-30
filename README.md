# NETRUNNER FOUNDATION GAME

Standalone repository: `netrunner-foundation-game`.

An offline cyberpunk research and learning prototype: inspect six synthetic
Solana and Arbitrum One events, compare observations and hypotheses, explore
the CRASHOVERRIDE terminal, and export a reproducible evidence dossier.

## Play Ghost Signal

Open `examples/netrunner-foundation/index.html` and choose **Play Ghost Signal**
or **Academy**. Select Solana or Arbitrum One, inspect the source record, choose
a supported claim and an evidence request, then read the explanation before
continuing. Each track has three stages and a final debrief.

Training points reward claim discipline and useful evidence requests. They do
not change the research dossier, its claim states or its SHA-256 digest.
**Replay mission** returns to track selection; **Reset mission** discards the
current attempt. Progress stays in this tab and resets on page reload.

## Run locally

Playing requires a modern browser; there is no install or build step. Python
3.10+ can serve the files and run the research replay. The full development
verification command additionally requires Node.js 20+ for gameplay tests.
No third-party packages are needed.

```sh
python3 scripts/verify.py
python3 examples/netrunner-foundation/replay.py examples/netrunner-foundation/fixture.json
python3 -m http.server 8000 --bind 127.0.0.1 --directory examples/netrunner-foundation
```

Open `http://127.0.0.1:8000/`, or open
[`examples/netrunner-foundation/index.html`](examples/netrunner-foundation/index.html)
directly. The server only serves local files. Filters, evidence details, terminal
commands and JSON export operate in the browser. There is no build step.

## Current scope

- Six synthetic events across two independent network tracks.
- Deterministic Python replay with a SHA-256 dossier digest.
- CRASHOVERRIDE console with evidence inspection and JSON export.
- Ghost Signal Academy mission: three stages per network, source inspection,
  scored decisions, explanatory feedback, debrief and reset.
- Consolidated v0.2 documentation, source-claim adjudication and contracts.
- 23 existing test cases: 22 pass; one is intentionally skipped when the private
  source manifest is absent. The verification command also compares the full
  saved and embedded dossiers against a fresh replay.
- Seven additional Node.js tests cover mission completion on both networks,
  corrections, reset, input rejection, score isolation and source immutability.

This v0.3 prototype includes a complete local mission loop. Persistent saves
and a larger campaign remain future milestones in [ROADMAP.md](ROADMAP.md).
All scenarios are synthetic. Live observations and financial execution remain
outside this implementation.

## Documentation

- [Master blueprint](strategy/netrunner-foundation/MASTER-BLUEPRINT.md)
- [Architecture](strategy/netrunner-foundation/architecture.md)
- [Ante reference runbook](strategy/netrunner-foundation/ante-runbook.md)
- [Decision record](strategy/netrunner-foundation/DECISION-RECORD.md)
- [Design brief](strategy/netrunner-foundation/DESIGN-BRIEF.md)
- [Import provenance and standalone decisions](IMPORT-PROVENANCE.md)

Ante/NEXUS is an upstream design reference. This repository is independent;
it does not include Ante's agent runtime or claim that its reviews have run.
Only the prepared documentation and synthetic examples are included. Original
source documents and `source-manifest.internal.json` are excluded.

The historical `NETRUNNER FOUNDATION` replay identifier and v0.1 event schema
are preserved so the existing dossier hash stays reproducible. The project and
repository name is **NETRUNNER FOUNDATION GAME**.

No distribution licence has been selected for this new repository. Licence
selection and rights to any future imported material remain owner decisions.
