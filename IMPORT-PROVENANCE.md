# Import provenance and standalone decisions

Prepared: 2026-10-29.

The owner selected a new, independent repository named
`netrunner-foundation-game`. This overrides the old Ante hosting instructions
in the supplied v0.2 package. The private remote has been created; the baseline is verified locally.

## Imported baseline

The supplied offline replay, fixture, dossier and existing tests were copied
without implementation changes into `examples/netrunner-foundation/`. Their
v0.1 schema, internal project identifier and dossier hash are preserved.
Consolidated v0.2 Markdown and contract JSON live in
`strategy/netrunner-foundation/` to preserve their relative links.

Documentation hosting instructions, observed test counts and console branding
were updated for this standalone repository. Root setup instructions, a game
roadmap, the verification command and an initial GitHub Actions workflow were
added. GitHub Actions has not run yet. No original-source redistribution or
new licence has been authorised by this import.

The latest visible `MASTER-BLUEPRINT(2).md` was read for the current design;
its content and byte count are consistent with the supplied v0.2 blueprint.
The local supplied blueprint is the import baseline below.

## External dependencies and authority

Ante profile names and governance paths are design references. No Ante code,
agent catalogue or runtime is bundled or fetched. No existing Ante branch,
PR, contract or HOLD decision is changed. The seven strategic tests remain
as supplied; new game scoring must never substitute for those decisions.

The source corpus and `source-manifest.internal.json` are excluded from this
repository and from the downloadable source package. These import receipts
cover only the supplied prepared artifacts, not the original 27 sources.

## Input artifact SHA-256 receipts

```json
[
  {
    "input": "CLAIM-ADJUDICATION.md",
    "sha256": "9706f0ac88e04dc443e7fb66e9191e277b857c3794ebb4ced8b313b43a8bddec"
  },
  {
    "input": "DECISION-RECORD.md",
    "sha256": "eaa1267a192e474526bae1a3faada6ec76b78375afb663200b856d21a5cf69b7"
  },
  {
    "input": "DESIGN-BRIEF.md",
    "sha256": "030a669df33bc5732d79e4b6a551f5eb0cee358ed0274f61d69ae4294a078677"
  },
  {
    "input": "MASTER-BLUEPRINT.md",
    "sha256": "b8b7dd9f43ef08714bae3bc20641af8a21ff66ad63310212a6e9657ea6f98d63"
  },
  {
    "input": "README.md",
    "sha256": "8ea58cb7e7eece37b61b96ac21391171d16ffac42855240100b427a13a27e228"
  },
  {
    "input": "SOURCE-CROSSWALK.md",
    "sha256": "470d1d2a60430fde927460d047091baeac870336d5c097bceb986bb973c98405"
  },
  {
    "input": "START_HERE.md",
    "sha256": "cc041ef1af5c00d98e090238947e1eacf0666a223d327a16a2749f3ced2a587c"
  },
  {
    "input": "ante-runbook.md",
    "sha256": "372f09656f69840bf33223f0c6be39e5b7380c2eff9cb4830c4d4abb507bf416"
  },
  {
    "input": "architecture.md",
    "sha256": "6a1ac488b8401be9042d9939b8ad3d3d6b63ea75dc1b7314132bff36d2722847"
  },
  {
    "input": "claim-register.md",
    "sha256": "708ea8a5aafbe21c1b548bda716dfdddef06e4dbea30967951bef45f4e734e79"
  },
  {
    "input": "contracts.v0.2.json",
    "sha256": "75cd60b2ab5609691dda0b84d3bf2fed34fe6bcee919b64a3afa08b8d474ac80"
  },
  {
    "input": "fixture.json",
    "sha256": "471b4b5c856c5cc335f128b32e60774edac53f084910f18a6479bc651516ac2f"
  },
  {
    "input": "index.html",
    "sha256": "32100b9c59e2ffec28b95edaa28937ee3d5ebf6c2f7ad64e4d37b153af3a5d4c"
  },
  {
    "input": "replay.py",
    "sha256": "0581809be538b720d99bf31f112456d33dbf7922837f3fc2872298708a0c4a89"
  },
  {
    "input": "roadmap.md",
    "sha256": "bb0f3804d4b62a1f8cd08f20269b67cf1abf67e7cdcb0e225b5f9b2dd035fe2c"
  },
  {
    "input": "synthetic-dossier.json",
    "sha256": "3fc817abd609745b478a9416c8a399c737bebb071456bde7e20e667f31d9d262"
  },
  {
    "input": "test_consolidation.py",
    "sha256": "d90139558095d34743eac56ecb658194ab16a354b9644edbe06b0f1f22e18dad"
  },
  {
    "input": "test_replay.py",
    "sha256": "a89d01267f8789bea311469973e6e5f59f58bf411aca9be9819523461a029638"
  }
]
```
