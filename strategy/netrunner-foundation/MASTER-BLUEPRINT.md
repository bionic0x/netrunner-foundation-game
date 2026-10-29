# NETRUNNER FOUNDATION — Consolidated master blueprint v0.2

**Umbrella:** NETRUNNER FOUNDATION GAME (independent; Ante / NEXUS design references) · **Product:** CRASHOVERRIDE · **Research:** APEX COSMIC CHAOS ENGINE · **Experience:** HACK THE PLANET · **Teams:** WOLF PACK / DIA · **Capital research:** HYENA · **Governance:** LEGAL FORTRESS / DARK DAO · **Economics research:** $OVR / NFT YIELD.
**Issued:** 2026-10-29 · **Decision:** `PROCEED_WITH_CONDITIONS` for documentary, offline replay and read-only design; `HOLD` for live financial activity, token/NFT offerings, custody and deployments with real-world effects.

## 0. Interpretation and evidence contract

This blueprint **merges the concepts and terminology** of 27 supplied source documents, including a nine-source prior baseline and 18 later documents. It is **not** a merger of claims into facts or a declaration that any proposed product, DAO, token, extraction business, neural model or infrastructure exists. The material spans marketing manifestos, whitepapers, UI ASCII designs, governance/tax propositions and hypothetical code; the existence of prose or a schematic is not operational evidence. Several documents are compilations of earlier chapters and executive summaries; repetition is not independent corroboration.

Canonical epistemic classes: `EVIDENCE`, `HYPOTHESIS`, `ASSUMPTION`, `UNKNOWN`. Quantitative qualifier: `MEASURED`, `TARGET`, `ESTIMATE`, `HYPOTHESIS`. `SOURCE_ASSERTION` is a metadata label indicating what a supplied document **says**, not proof of the proposition. Every public performance number requires provenance, measurement period, denominator, chain, methodology, confidence/uncertainty and independent review. Agents cannot manufacture authority. A `HOLD` is an explicit operational boundary, not a cosmetic status.

**Source custody:** the companion `source-manifest.internal.json` contains SHA-256 hashes, file size and source aliases. It is deliberately separate from GitHub-safe documents; originals are not incorporated into the public repository by this deliverable. The original uploaded texts remain source-of-record for their own historical ideas, including rejected material.

## 1. Product thesis and strategic object

**Overarching thesis:** combine DeFi market observability, adversarial research, uncertainty-aware intelligence, simulation, evidence-first multi-agent review and a distinctive cyberpunk terminal into a product that helps real users understand transaction-ordering risk, valuation integrity, outage/recovery conditions, and economic exposures.

**Primary potential customer:** protocol risk teams, security researchers, DeFi analysts and institutions requiring evidence dossiers. **Secondary audience:** students and community users exploring synthetic scenarios in a safe educational environment. These customer and willingness-to-pay hypotheses have not been validated.

**Minimum sufficient outcome:** demonstrate, on two *separately scoped* networks, deterministic reproduction of a documented event, an explanatory dossier with the relevant alternative explanations and missing evidence, and a usable interface that never presents a synthetic opportunity as an earned return. **Non-object:** counting agents or bots, delivering fastest imagined latency, maximizing trade volume, inflating token valuation, covert market impact, or maximizing engagement via misleading expected rewards.

**Authority model:** exploration and recommendation belong to agents; legal, risk, security, financial and production decisions belong to named competent human owners acting under actual permissions. The original strategy doctrine governs seven coherence tests: governing object, causal, interactive, conversion, legitimacy, epistemic and exit. None is bypassed by a successful build or popular user interface.

## 2. Brand, product and module identity

| Canonical namespace | Historical names and proposed capability | Decision for v0.2 |
|---|---|---|
| `NETRUNNER` | Parent program, foundation, coordination and contract plane | **Core**: governance and source traceability |
| `APEX` | Neural engine, OODA, scout/analyst swarm, pattern memory, twins, cross-chain intelligence | **Research**: evidence pipelines and optional offline model comparisons; do not assert trained models exist |
| `GIBSON` | Command core / hypercore / macro-micro fusion | **Core data plane**: read-only ingestion, indexing, versioned event normalization, reproducible analytics |
| `CRASHOVERRIDE` | Desktop terminal, mission control, tactical dashboard, forensic consoles | **Experience**: evidence viewer and simulated command surface; no transaction control |
| `HACK_THE_PLANET` | Academy, progression, visual lore, mock crew missions, skill tree | **Education**: scenario replay and knowledge checks, with honest simulation labels |
| `WOLF_PACK` | Scout, analyst, commander, hunter, guardian, tech; crew and alliance model | **Ante multi-agent**: bounded task orchestration, independent review and human escalation |
| `DIA` | Competitor forensics, validator studies, protocol change monitoring, public sentiment | **Research**: public, permissioned OSINT, protocol intelligence, reliability/attribution analysis |
| `HYENA` | Leverage tiers, recycling, flash loans, stress and circuit breakers | **Sandbox risk lab**: liquidation risk, exposure and tail-loss simulations; no account actions |
| `ZK_SHIELD` | Privacy, anonymous voting, zero-knowledge, anti-capture claims | **Optional security research**: verifiable privacy without concealment of legal responsibility |
| `HYDRA / ICP / AKASH` | Resilience, distributed nodes, canisters, failover | **Candidate infrastructure**: evaluate cost/availability/trust boundaries rather than promising immunity |
| `LEGAL_FORTRESS` | Switzerland/Singapore/Dubai/Cayman/Liechtenstein/Delaware entities | **Legal issue-spotting**: no adopted corporate structure, licence, anonymity or tax position |
| `DARK_DAO` | Private governance, reputation and ZK voting, shadow operations | **Separate governance-research concept**; no deniable unlawful operations or covert execution |
| `$OVR / $CHAOS / $HTP` | Differing token names, supplies, burns, staking, treasury allocations | **Economics study only**; no sale, custody, reward claim or launch |
| `NFT_YIELD` | Five NFT tiers with voting, yield and extraction rights | **Historical allocation proposal**; educational/nonfinancial collectibles possible later after separate review |
| `ANTI_FRAGILE` | Crash, congested network, exploit, outage and response simulations | **Defensive stress-testing**: attack-harm modeling rather than initiating disturbances |

**Canonical language:** retain the memorable design names, but rename UI verbs with real-world impact. `scan` = inspect public or synthetic evidence; `mission` = a bounded research or education task; `deploy` = run a local replay or stage a reviewed read-only connector, never activate a bot against third parties; `profit` = historical/source estimate or synthetic field with its data type prominently labeled; `attack vector` = adversarial *threat category* or isolated lab scenario.

## 3. Unified functional architecture

```text
PUBLIC / PERMISSIONED DATA                 SIMULATOR & HISTORY
  Solana event/slot evidence                 deterministic synthetic fixtures
  Arbitrum L2/receipt/feed evidence          separately licensed historical snapshots
  Protocol docs / change logs               modeled scenarios with seed + version
  Public macro indicators                   explicit scenario assumptions
               |                                         |
               +----------------+------------------------+
                                |
                         GIBSON INGEST
          source IDs | timestamps | network semantics | hashes
                                |
                     NETWORK-SPECIFIC ADAPTERS
            E1-SOL (accounts/PDA/CPI/slots)     E1-ARB (EVM/proxies/sequencer)
                                |
                    VALIDATED EVENT ENVELOPE
              accepted | stale | duplicate | missing | unknown
                                |
                  APEX RESEARCH / ANALYSIS
         models and rules | alternatives | falsifiers | calibration
                                |
                    WOLF PACK / ANTE NEXUS
          D1 provenance -> E1 domain review -> S1 security challenge
                  -> D3 claim control -> G1 decision packet
                                |
                   IMMUTABLE EVIDENCE DOSSIER
                    event IDs | data scope | claims | hashes
                                |
                   HUMAN REVIEW / RECORDING
                                |
                CRASHOVERRIDE / HACK THE PLANET UI
             Terminal | Observatory | Replay | Risk Lab | Academy

NO EGRESS TO A WALLET SIGNER, PRIVATE KEY, TRADE ENGINE,
MEMPOOL ATTACK TRANSMITTER, MARKET-MANIPULATION CHANNEL OR RAT.
```

The conceptual split is **observation ≠ detection ≠ inference ≠ policy ≠ authorization ≠ execution**. UI glyphs, agent confidence and model scores never grant privileges. For live data, retain provider terms, retention limits and attribution constraints; avoid publishing individual-wallet allegations.

### 3.1 Chain semantics and explicit boundaries

- **Solana:** represent slot, commitment, signature, account ownership, executable program ID, CPI path, writable/signer privileges, Token/Token-2022 and oracle adapter version. `SOL-ORD` is observable adverse ordering *hypothesis* and `SOL-ORC` is degraded valuation input *hypothesis*. No mempool equivalence with EVM is assumed.
- **Arbitrum One:** represent L2 transactions/blocks/receipts, proxy/implementation/admin, price feed consumed (units/decimals/heartbeat), sequencer state, RPC observation outage, L1/L2 recovery dependencies. `ARB-ORC` and `ARB-RES` are separately evaluated.
- **Cross-network:** share envelope fields, purpose, review procedure and epistemic vocabulary, **not** oracle staleness thresholds, ordering inference, event completeness, performance, legal status or Gate decision.

### 3.2 Data and traceability schema

Every event in an evidence artifact should expose at least: `event_id`, `network`, `protocol_scope`, `observed_at`, `source_id`, `source_digest`, `environment`, `data_freshness`, `observation_completeness`, `signal_type`, `alternative_explanations`, `claim_status`, `quantitative_status`, `reviewer`, `artifact_revision`, `decision_state`, `reason_to_hold`. An event classified `UNKNOWN` must never become `EVIDENCE` through display formatting or summing into a dashboard.

The existing `examples/netrunner-foundation/replay.py` and `fixture.json` are a minimal **offline synthetic** v0.1 implementation; they are not a deployment of the full architecture. Preserve their deterministic digest and cross-network isolation in all future migrations.

## 4. Research engines

### 4.1 APEX neural and digital twin program

Retain transformer, GNN, temporal models, model ensembles, graph route representations and protocol digital twins as **competing experimental hypotheses**, not required dependencies. Baseline first with transparent deterministic rules and simple statistical comparisons. Every candidate must be measured out-of-sample against a frozen naive baseline; measure precision, recall, calibration, data leakage, false-alert cost, p50/p95/p99 latency, drift and domain shift. A 'chaos oscillator' or hallucination generator may propose **fictional simulations** only; no ungrounded scenario may be described as discovered real-world opportunity.

### 4.2 Macro-MEV and DIA research

Market regime indicators (FCI, USD, ISM, liquidity, volatility, funding/basis) can be exploratory explanatory features. Do not infer causal signals or automatic position shifts from historical correlations. DIA can monitor public block data, governance forums, released code, official feeds and authorized research channels; private communications or insider data obtained without permission are excluded. Attribution to named funds or institutions remains `UNKNOWN` unless supported by independent primary evidence.

### 4.3 Anti-fragile stress lab

Replay *exogenous* shocks: sequencer outage, oracle staleness, liquidity impairment, gas congestion, extreme volatility, protocol incident, missing data, provider failure, regulatory/business disruption and recovery under unresolved exposure. For each scenario state the exogenous assumptions, downstream sensitivities, false-positives, reserve usage and safe-stop behavior. Do not create shocks in live markets or transmit synthetic pressure to real DEXs.

### 4.4 Hyena risk lab

Compare stress exposure at hypothetical leverage tiers (2–5×; 10–20×; 30–50×; 50–100×) **only as risk illustrations**. Report liquidation distance, funding/fees, slippage, convexity, correlated drawdown, insolvency/MEV exposure and worst-case losses. Do not imply leverage magnifies returns without magnifying losses. A zero-risk flash loan is an incorrect absolute; capital, execution, gas, counterparty and operational failures remain relevant.

## 5. WOLF PACK under Ante/NEXUS — accountabilities

| Seat / historical persona | Concrete Ante profile | Responsibility | Boundary |
|---|---|---|---|
| G1 / ZERO COOL | `specialized-chief-of-staff` | Coordinate artifacts, scope and decision packets | No live execution permission |
| Assurance | `specialized-strategic-assurance-lead` | Apply seven coherence tests; HOLD for fatal gaps | Does not overrule legal or human authority |
| P1 / Product | `product-manager` | User problem, product claims and falsifiers | No product-market validation by assertion |
| D1 / LORD NIKON | `research-synthesist` | External evidence and alternative explanations | No invented citations or privileged data |
| D3 / CEREAL KILLER | `research-proposition-citation-auditor` | Source/status/version/chain claim lineage | No chain transfer by analogy |
| S1 / GUARDIAN | `security-blockchain-security-auditor` | Independent audit and threat model | Does not certify own engineering outputs |
| E1-SOL / TECH WOLF | `engineering-solana-program-engineer` | Solana semantics and adapters | No signer or production transactions |
| E1-ARB / TECH WOLF | `engineering-solidity-smart-contract-engineer` | Arbitrum semantics and adapters | No third-party contract changes |
| G2 / LEGAL FORTRESS | `support-legal-compliance-checker` | Legal issue spotting and licensing matrix | Not formal legal advice or a signed approval |
| UX / ACID BURN | `design-ux-architect`, `design-ui-designer` | Evidence-friendly navigation, visual system, accessibility | No conversion of simulation into real gains |
| QA / THE PLAGUE | `testing-reality-checker`, `testing-test-automation-engineer` | Challenge, replay determinism, edge cases | Independent results required for claims |

These are catalog profiles that can be selected through Ante; the table **does not assert** that eleven independent model agents have already reviewed the project. Distinct personas or names do not demonstrate independent scrutiny. Follow the existing `strategy/htp-gate0/agent-mapping.md`, overlays and E1↔S1 handoffs rather than creating a competing governance path.

## 6. CRASHOVERRIDE experience: information architecture

**Product surfaces** (target, not assertion of completed build):

1. **ACCESS / JACK IN:** clear access purpose, no false 'ZK VERIFIED' unless a real verifier operates; demo requires no wallet.
2. **GIBSON TERMINAL:** command palette and read-only status; display environment badge, last update, primary sources and `HOLD` state.
3. **OBSERVATORY / MEMPOOL INTELLIGENCE:** public-data lineage, chain-specific event streams and ordering/valuation quality; partial observability signaled clearly.
4. **APEX ANALYSIS:** hypotheses, alternatives, competing models, performance on holdout evidence and falsifiers.
5. **WOLF PACK / MISSIONS:** research task assignments, artifact states, reviewer objections, scopes and deadlines; no hostile collective trading.
6. **DIA INTELLIGENCE:** authorized/public protocol change monitoring, chain coverage, entity-attribution caveats and provenance.
7. **HYENA RISK LAB:** shock and leverage stress simulations, marked `SIMULATED`; no live positions or execution button.
8. **HACK THE PLANET ACADEMY:** training levels, synthetic replay, quizzes, evidence evaluation and ethics of MEV.
9. **GOVERNANCE / DARK DAO STUDY:** authorization chains, proposal audit trail, transparent procedures, ZK voting feasibility research.
10. **LEGAL FORTRESS / COMPLIANCE:** jurisdictions and activity boundaries, accountable persons, outstanding counsel and restrictions.
11. **ECONOMICS LAB / $OVR / NFT:** scenario editor for speculative allocation and dilution; no advertised APY, sale or distributions.
12. **EVIDENCE VAULT:** versioned dossiers, hash verification, external annotations and explicit distinction between hypothetical and observed.

### 6.1 Visual specification from the two UI galleries

Keep the recognizable *Hackers*-era, ASCII/CRT, VGA, terminal, acid green and high-contrast black, red alert and amber caution, crew codenames, command-palette vocabulary and hex module codes. Provide **progressive disclosure**, readable fonts, keyboard navigation, accessible focus indicators, no seizure-triggering aggressive flashing, reduced-motion support, contrast-tested charts, copyable IDs, mobile-responsive layouts, consistent time zones and readable source/unknown badges. Avoid deceptive scarcity, FOMO countdowns, money-printing claims or variable reward conditioning in financial decision flows.

In this chat, this is a **design brief**, not a Product Design plugin prototype or visual verification. The plugin's full exploration/implementation workflow requires Work and an explicit selected visual target.

### 6.2 Essential UX stories and acceptance

- A risk researcher can follow a signal to raw observations and alternative explanations in **three or fewer purposeful navigational transitions** (design target requiring user testing).
- Any numeric figure labeled `synthetic`, `historical`, `estimate`, or `measured` retains that label in charts, exports and copies.
- A review-only operator cannot access transaction-signing, fund custody, market manipulation, or third-party intrusion functions because those capabilities **do not exist** in the product or API.
- A user can export a dossier with network-specific scope, event hashes, reviewer, open questions and reproducibility instructions.
- Each warning states the remediation task and who can resolve it; pressing a UI button cannot waive independent review.

## 7. Economics, tokenomics, NFT and DAO research

The original corpus gives several **incompatible** financial designs: $CHAOS, $HTP and $OVR tokens, revenue forecasts ranging from $4M/day to $25M/day and beyond, multiple profit splits, five NFT tiers and overlapping treasury/DAO rewards. **No token supply, price, future return, ownership claim or entitlement is adopted.** The canonical v0.2 artifact is a **non-financial model** that tests the arithmetic, dilution, insolvency, treasury accounting, issuance and compliance requirements of hypothetical schemes.

In the $OVR draft the stated 100M token allocation sums to 100% (50% staking, 10% treasury, 10% team, 10% liquidity, 10% NFT/gaming, 10% initial sale), but percentages are only a distribution proposal. The `50% of $25M/day` staker allocation equals $12.5M/day, or $4.5625B per 365-day year **before any costs**. This does not prove the revenue exists or a sustainable APY; the APY depends on circulating/staked units, price, expense and actual distributable cash. The NFT proposal references extraction *revenue* (gross) and additional entitlements; its allocations cannot be simply added to token profit splits without testing overlap and double counting.

**Economic gates:** verified source of gross revenue; net realized cashflow ledger; full liabilities; distinct gross/net allocation waterfall; insolvency and counterparty risk; participant rights and marketing claims review; counsel opinion as relevant; anti-money-laundering and market abuse controls; tax/accounting review. No investment offering or payments until separate authorized project approval. Gamified XP and fictional points can be modeled without implying cash value.

## 8. Security, privacy, law and prohibited operations

**Retained:** access control, least privilege, cryptographic audit trails, explicit keys/roles, resilient infrastructure, threat modeling, incident response, segregated duties, disaster recovery, cautious ZK research and legitimate governance processes.

**Not implemented:** covert RAT deployment, unauthorized intrusion or exfiltration, impersonation, insider-data acquisition, botnet infiltration, malicious social campaigns, wash trading, spoofing, market manipulation, sandwich attacks against real users, engineered liquidation cascades, forced reorgs, validator corruption, false identities, evidence destruction, evasion of lawful oversight, deceptive treasury laundering or guaranteed financial returns. These concepts remain in the source catalogue as **risks to detect, model in isolation, or explicitly reject**.

**Legal policy:** Swiss/Singapore/Dubai/Cayman/Liechtenstein/Delaware structures are alternative source proposals, not an incorporated group. Corporate separation does not inherently prevent lawful investigation, establish tax exemption, eliminate beneficial ownership disclosure, or grant regulatory immunity. A location-specific legal analysis must map services, clients, custody, market abuse, licensing, advertising, AML/KYC, consumer/investor protection, tax, data protection and sanctions before live launch. No statement here constitutes a legal conclusion.

## 9. Contradictions and reconciliation decisions

| Conflict class | Source observations | Canonical resolution |
|---|---|---|
| Version & narrative | 'Already live', prototype, planning, and past-dated milestones all appear | Treat as chronological **source assertions**, not verified operational status |
| Claimed speed | 0.3ms APEX OODA, 30ms ZK, 1.2ms ICP bot, 89.5ms HTP and different per-bot latencies | Each is a distinct unverified measurement hypothesis with incompatible boundaries; no single performance spec |
| Claimed scale | 240 / 250 / 1,050 / 5,000 nodes; 10k / 250k bots/operators/participants | Different units/time horizons, not interchangeable actual inventory |
| Economics | $3.5M/day market in some drafts, $25M/day capture; $4M/day diversified business; $1B/day endgame | Explicit business scenarios only; `profitability_established=false` |
| APY | 100% guaranteed vs five-digit annual NFT ROI figures | Reject investment guarantees, require net-cashflow/accounting and legal gate |
| AI | '98.5% accuracy', 'self-learning' and neural topology | Candidate experiments with held-out evaluation and rollbacks |
| Infrastructure | 'Uncensorable', invisible, zero attack surface, quantum-proof | Replace absolutes with scoped fault model and evidence |
| Entity legal plan | Three, four and seven-jurisdiction variants | No selection; single legal issue matrix with jurisdiction-specific counsel |
| Purpose | Protect retail users vs manufacture price moves / institutional losses | Governing object is user/risk decision benefit; manipulative courses rejected |
| DAO | Community/transparent vs untraceable/deniable | Study accountable, privacy-preserving governance; exclude deniability for unlawful behavior |

## 10. Five-gate implementation decision tree

**Gate 0 — doctrine and corpus:** 27-document archive fingerprinted; source claims, object/non-object, safety and legal boundaries declared. Gate owner to ratify; no financial authority.

**Gate 1 — synthetic research product:** use existing offline replay + fixture, schema contracts, deterministic hashes, negative/error tests, accessible navigation specifications. This v0.2 deliverable adds source/claims/design/architecture unification but no proof of real chain behavior.

**Gate 2 — historical reconstruction:** select one protocol and explicit markets per chain. Pin contracts, event ranges, feeds, source revisions and allowed data rights. Prove complete/partial observation accounting and implement separate E1→S1 review tracks. Compare detector output to credible human-reviewed labels and alternative explanations.

**Gate 3 — read-only shadow pilot:** invite a real protocol risk team; run alerting silently with no writes or custody; pre-register accepted false-positive rates, review latency, data availability and whether users make better decisions than baseline. Resolve data/privacy controls and legal review.

**Gate 4 — controlled read-only product:** publish the observability dashboard under a supportable SLA derived from measurements, human incident workflow and independent security assessments. Feature-by-feature approvals; separate business-case re-evaluation if a financial service is proposed in the future.

**Explicitly outside this roadmap:** autonomous market trading, live extraction swarms, treasury custody, issuing yield rights, aggressive financial leverage and unlicensed market services. Such ventures require their own legal and safety determination; the research roadmap cannot pre-authorize them.

## 11. Acceptance and falsification matrix

| Question | Current assessment | Specific evidence needed |
|---|---|---|
| Is the synthetic replay deterministic? | Existing v0.1 tests report pass | Re-run tests and compare output hashes after every change |
| Can Solana adverse ordering be meaningfully identified? | `HYPOTHESIS` | Frozen relevant slot / account data, alternatives, labels, known missingness |
| Can Arbitrum recovery exposure be meaningfully identified? | `HYPOTHESIS` | Sequencer/RPC/feed distinctions and review of historical event windows |
| Does APEX outperform simpler methods? | `UNKNOWN` | Independent unseen data, pre-specified baseline, calibration and error costs |
| Is claimed performance submillisecond? | `UNKNOWN` | Hardware/chain boundary, p50/p95/p99, cold/warm and adverse load tests |
| Does user observation improve real risk decisions? | `HYPOTHESIS` | Named user, observable decisions and counterfactual comparison |
| Are project returns/revenue realized? | `UNKNOWN` | External independent accounts and consistent net cash flows |
| Is legal/DAO/NFT structure approved? | `UNKNOWN` | Human counsel and regulator/activity-specific resolution |
| Can real funds be controlled by this package? | **No**, intentionally | Any new design requires separate charter; not inferred from this one |

**Stop / redesign triggers:** untraceable claim inflation, chain-evidence leakage, forced attribution, rights violations, non-reproducible historical result, false reassurance leading to greater loss, and absence of customer value despite technically correct alerts. A functioning simulator is **not** sufficient success.

## 12. Repository integration and authorship

The chosen standalone repository is `bionic0x/netrunner-foundation-game` (private remote created). This owner decision supersedes the previous hosting plan under `bionic0x/Ante-agency-agents`. Ante and its `strategy/htp-gate0` remain external references; their runtime and decisions are not imported. A public PR should contain **new project documentation and benign examples only**, not raw source uploads or invalid claims recast as deployment instructions. Preserve existing Ante releases/tests and do not merge protected governance changes without review. The master package's content is suitable for `strategy/netrunner-foundation/` and the existing synthetic prototype under `examples/netrunner-foundation/`; any CI integration should be a separate reviewed PR.

**Owner decisions pending:** name the product/risk owner, consent for any original-source publication, target customer/protocol and data rights, host of design workflow, future handling of token/NFT concepts, legal jurisdiction/activity scoping, and independent security reviewers. These do not block archival consolidation and offline product planning.
