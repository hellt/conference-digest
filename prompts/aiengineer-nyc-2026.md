>>> HOW TO RUN THIS <<<
This is the digest prompt for aiengineer-nyc-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/aiengineer-nyc-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/aiengineer-nyc-2026.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, cloud
platforms, Kubernetes, and AI. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect); cloud infrastructure and operations (public and private
cloud, virtualization, compute/storage/networking, multi-tenancy, and
automation); Kubernetes and cloud-native systems (architecture and
operations, eBPF, Cilium, Kubernetes networking, Gateway API, service mesh,
IPAM, and BGP/datapath internals); and AI (AI/ML systems, LLMs and agents,
model training and inference, GPU/accelerator infrastructure, networking for
AI, and ML for infrastructure operations). Physical DC and WAN systems work is
CORE to this PM, not adjacent — do not down-rank a paper for being about
hardware, optics, or datacenter fabric.

Below is the program for AI Engineer New York 2026. Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

Judge each item by what it changes for a practitioner: novel techniques and
firmly substantiated results over incremental benchmark improvements, and
operational lessons, tooling, automation and postmortems that transfer across
environments over org-specific anecdotes or vendor pitches in disguise.
Treat strong empirical evaluation and real deployment experience as signals of
weight; treat unvalidated claims with caution. Note when a technique depends
on a specific operator's scale, topology or silicon.

## Enriching from the source material (best effort)

The program text gives you a title, authors, and an abstract per item, and
often links (`page:`, `pdf:`, `slides:`, `video:`). The abstract alone is thin — the full
paper has the methodology, real results, and limitations that make the What /
How / Where-applicable sections accurate instead of guessed.

If you have a tool to fetch URLs, then for EACH selected item (Core, Adjacent,
and Wildcard) try to retrieve the fuller source before writing it up:

- Prefer a `pdf:` link; else fetch the `page:` link (often has the full text or
  a longer description); a `video:` link is a last resort, don't transcribe it.
- Use what you retrieve to ground What/How/Where-applicable in the paper's
  actual contributions, evaluation, and stated constraints.

This is strictly best-effort. Many links fail or are paywalled:

- If a fetch fails, is paywalled, returns only an abstract, or you have no fetch
  tool, just fall back to the abstract already in the program text. That is
  fine and expected — do not stall or skip the item.
- NEVER invent paper contents, numbers, or findings from a failed or partial
  fetch. If you only had the abstract, write from the abstract.
- Note when an item's write-up is based only on the abstract, e.g. end its
  What line with "(from abstract only)", so the reader knows the depth.
- Do not let enrichment change which items you select or their tier; selection
  is from the program. Enrichment only deepens the write-up.

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to the PM's core interests as listed above
  (networking, cloud, Kubernetes, or AI) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title**: the `###` heading is the item's title exactly as the program
  gives it, with nothing added. Speaker(s)/author(s) with affiliation go on
  the line below it.
- No links section: the pipeline puts a links row (abstract page, paper,
  slides, recording) under every heading after you finish, from the program's
  `page:`/`pdf:`/`slides:`/`video:` lines and from verified sources. Do not
  write one, and do not link the title.
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Search keywords

The site's search indexes topic keywords per page. After the Themes section,
append ONE fenced `json` code block - the pipeline reads it machine-side and
removes it before publishing, so it is never rendered - of exactly this shape:

```json
{"post": ["cloud", "ai"], "talks": {"<pick heading>": ["cloud", "ai-networks"], "<pick heading>": ["kubernetes", "cni"]}}
```

- "post": 3-6 topics this digest as a whole covers.
- "talks": one entry for EVERY pick you selected, keyed by its exact `###`
  heading string (copy it character for character, including any presenter
  part), with 2-4 tags naming what the talk is about - the technology or
  practice, not its tier or the conference.
- Tags are lowercase, hyphenated, single concepts. Use ONLY tags from this
  vocabulary:

- `ai` - artificial intelligence systems, applications and practices not covered by a finer AI tag
- `ai-networks` - networking for AI/ML training and inference clusters (job-level load balancing, collectives, topology-aware scheduling)
- `gpu-clusters` - GPU accelerator interconnects and cluster fabrics (NVLink, scale-up vs scale-out)
- `ml-for-networking` - machine learning applied to network operation (anomaly detection, traffic prediction, AIOps)
- `data-center-fabric` - physical data-center fabric design (topologies, CLOS, buffer management, congestion)
- `optics` - optical transport, transceivers, pluggables, DWDM, LPO/CPO
- `ethernet` - Ethernet as a technology standard (P802.3 work, speeds, PHYs)
- `cabling` - structured cabling, fiber plants, MPO/MTP, copper
- `power` - power delivery and efficiency in DCs (PUE, 48V, power sourcing equipment)
- `dpu` - data processing units, SmartNICs, offload and hardware offload in general
- `rdma` - RDMA, RoCE, InfiniBand, remote memory semantics
- `load-balancing` - traffic load balancing, ECMP/adaptive hashing, LB algorithms and architectures
- `packet-scheduling` - packet scheduling and queueing disciplines (PIFO, QoS schedulers, traffic management)
- `congestion-control` - congestion control and notification (ECN, PFC, DCQCN, L4S)
- `switching` - switch hardware and forwarding architecture (ASICs, buffers, pipelines)
- `silicon` - switch/NPU ASIC design, chip roadmaps, co-packaging
- `bgp` - BGP the protocol and its operation
- `routing-protocols` - routing protocol design and operation in general (ISIS, OSPF, BGP convergence)
- `segment-routing` - SR, SRv6, SR-MPLS and network programming with them
- `ipv6` - IPv6, its deployment and transition
- `mpls` - MPLS, labels, and LDP/RSVP heritage
- `peering` - peering business and practice, IXPs, interconnection agreements
- `interconnection` - data center interconnect and carrier interconnection
- `cdn` - content delivery networks
- `address-policy` - IP address and ASN allocation policy (RIR policy processes)
- `internet-governance` - regulation, standards bodies, and geopolitics of the internet
- `kubernetes` - Kubernetes architecture, operations, workloads and networking
- `cni` - container network interfaces and container networking plugins
- `containers` - containerization, images, runtimes
- `service-mesh` - service mesh (sidecars, eBPF meshes, mTLS between services)
- `cloud` - public and private cloud infrastructure, platforms and operations
- `cloud-native` - cloud-native patterns in general (CNCF ecosystem)
- `orchestration` - workflow and device orchestration, intent-based systems, network controllers
- `automation` - network automation (tooling, pipelines, source of truth, CI/CD for networks)
- `configuration-management` - managing device configuration at scale (config generation, drift, validation)
- `gitops` - GitOps workflows and version control practices
- `p4` - the P4 language and P4-programmable targets
- `linux-networking` - the Linux kernel networking stack (TC, netlink, drivers, offloads)
- `programmable-dataplane` - programmable data planes in general (PNA, portable switch OSes, pipes)
- `ebpf` - eBPF, XDP, and kernel bypass dataplanes
- `http` - HTTP and web protocols, QUIC
- `ipam` - IP address management and allocation
- `sdn` - software-defined networking, controllers, separation of control and data plane
- `network-security` - network security topics not covered by a finer tag
- `email-security` - email security and phishing (DMARC, spam, brand abuse)
- `malware-analysis` - malware, reverse engineering, botnet takedowns
- `threat-intelligence` - threat intel, IoCs, attack tracking
- `vulnerability-management` - vulnerability disclosure, patching, CVE economy
- `offensive-security` - offensive security, red teaming, exploit development
- `privacy` - privacy engineering, tracking, anonymity, privacy-preserving systems
- `censorship` - censorship, filtering, and measurement of Internet shutdowns
- `ddos` - DDoS attack and defense
- `anomaly-detection` - detecting anomalies and attacks in traffic
- `firewall` - firewalling and network policy enforcement
- `tls` - TLS, certificates, and protocol encryption
- `encryption` - encryption of traffic and data in general (MACsec, IPsec, E2E)
- `quantum-safe` - post-quantum cryptography and migration
- `quantum-networking` - quantum networking and entanglement distribution as infrastructure
- `pki` - public key infrastructure, certificate lifecycle
- `attestation` - remote attestation, measured boot, hardware roots of trust
- `zero-trust` - zero-trust architecture and microsegmentation
- `identity` - digital identity, identity ecosystems, ID standardization
- `authentication` - authentication methods and protocols (MFA, passkeys, WebAuthn)
- `authorization` - authorization, OAuth/OIDC, access control, policy engines
- `observability` - network observability tooling, telemetry pipelines, flow data
- `telemetry` - telemetry protocols (gNMI, streaming, INT)
- `measurement` - measurement methodology, probing, active/passive measurement studies
- `benchmarking` - benchmarks, testbeds, performance evaluation of systems
- `testing` - testing and verification of networks and configs (formal verification belongs here)
- `sre` - site reliability engineering practice, incident response, operations culture
- `capacity-planning` - capacity planning and forecasting
- `troubleshooting` - troubleshooting and root-cause analysis, outages and postmortems
- `dns` - DNS, resolvers, authoritative infrastructure
- `multicast` - multicast and broadcast replication
- `wifi` - wireless and mobility
- `mobile` - mobile and cellular networks (5G, roaming, RAN)
- `iot` - Internet of Things scale problems, LPWAN
- `cxl` - CXL and memory-fabric interconnects for pooled memory
- `time-sync` - time and clock distribution (NTP/PTP, GNSS timing)
- `spectrum` - radio spectrum policy and management
- `open-source` - open-source project practice and sustainability
- `standardization` - standards processes (IETF/IEEE) and documents
- `api` - APIs for network control (REST/gRPC, schemas, contract design)

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

The digest is read on GitHub (GitHub-Flavored Markdown viewed in the repo) and
on the project's Zensical site, which renders the same file. Use only syntax
both render reliably, and follow these rules:

- Headings with `#`/`##`/`###`; bold with `**...**`; italics with `*...*`.
- Bullet lists with `-`. Put a blank line before every list, before every
  heading, and between paragraphs, or they won't render correctly.
- Indent nested lists by four spaces per level; avoid deeper nesting.
- Any link you do write is `[text](url)` — never a bare URL — and uses a URL
  exactly as the program text gives it.
- No raw HTML except the metadata comment below. Do not use heading IDs,
  footnotes, definition lists, or other non-GFM extensions.
- You may use tables and `code spans` where they genuinely help, since GitHub
  supports them; don't force them.

Begin the output with this metadata, wrapped in an HTML comment so it does not
show in the rendered view but stays in the source:

<!--
conference: AI Engineer New York 2026
source_url: https://ai.engineer/nyc/2026
generated: 2026-11-11
registry_key: aiengineer-nyc-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## October 13 · Main stage
### Vault: Making Unstructured Data Work for Investing
Speakers: Aaron Linsky (Bridgewater), Sam Green (Bridgewater)
page: https://ai.engineer/nyc/2026/talks/bridgewater | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=442s
Investment agents need the research an investor would read—and a way to remember what the firm learns. Bridgewater’s Vault puts both into the same research loop.

### Balancing Acceleration and Safety for AI Agents
Speakers: John Feminella (Two Sigma)
page: https://ai.engineer/nyc/2026/talks/two-sigma | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=1435s
John Feminella uses a catastrophic payment mistake to explain five controls that make agents visible, constrain their access, and reserve human attention for decisions that need it.

### Does Code Quality Even Matter?
Speakers: Max Kanat-Alexander (Capital One)
page: https://ai.engineer/nyc/2026/talks/capital-one | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=2631s
Cheap code makes some programs disposable. For the systems people will keep changing, Max Kanat-Alexander argues that AI should make engineering rigor cheaper too.

### What does an AI engineer do?
Speakers: Aparna Dhinakaran (Arize AI)
page: https://ai.engineer/nyc/2026/talks/arize | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=3643s
Arize Signal reads traces, finds recurring problems, and can propose fixes. Building that loop requires decisions about memory, temporary access, recovery, and what counts as a good fix.

### Wells Fargo Foundation Model: Application to Fraud Detection at Scale
Speakers: Freddy Lecue (Wells Fargo)
page: https://ai.engineer/nyc/2026/talks/wells-fargo | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=5321s
Freddy Lecue explains why Wells Fargo trained a transformer on transactions rather than text, how it tokenizes heterogeneous banking data, and how the resulting representation supports fraud detection.

### Inside Arca’s long-horizon agents that run the business
Speakers: Aman Singh (Arca)
page: https://ai.engineer/nyc/2026/talks/arca | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=6803s
Aman Singh follows one client’s tax payment across days of analysis, approval, trading, and settlement to show how Arca’s agents keep work moving between human decisions.

### Intent Based Auth
Speakers: Allie Howe (Keycard), Ian Livingstone (Keycard), Michael Davis (JPMC), Dick Hardt (AAuth)
page: https://ai.engineer/nyc/2026/talks/auth-panel | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=8183s
Permission to call a payment API cannot tell an agent whether it should pay this invoice again. This panel explores how mission history, budgets, and changing conditions can inform each authorization decision.

### Great Agents Start with Great Infrastructure
Speakers: Akshat Bubna (Modal)
page: https://ai.engineer/nyc/2026/talks/modal | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=16931s
A spreadsheet with an agent behind every cell needs fast compute, shared storage, and deliberate isolation. Akshat Bubna explains how those requirements change the sandbox beneath an agent.

### Beyond the Model Card: The Jagged Frontier of AI in Finance
Speakers: Rayan Krishnan (Vals AI)
page: https://ai.engineer/nyc/2026/talks/vals | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=18418s
A model can earn strong partial credit and still produce work that cannot be sent to a client. Rayan Krishnan shows how evaluations built from a firm’s own work can guide model choice, spending, and deployment.

### AI and the Future of Fundamental Investing
Speakers: Jack Woodruff (Kepler), Vinoo Ganesh (Kepler)
page: https://ai.engineer/nyc/2026/talks/kepler-13 | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=19744s
Jack Woodruff sees AI changing research preparation and analysts’ roles while leaving a central investment problem intact: deciding where limited human attention can uncover a divergent view.

### Shipping like a startup, regulated like a bank
Speakers: David Abitbol (Revolut)
page: https://ai.engineer/nyc/2026/talks/revolut | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=20214s
David Abitbol describes Revolut’s move toward self-hosted coding models, the inference tuning that made them practical, and the operational controls used around a regulated engineering organization.

### Everyone Has AI. Who Has the Advantage?
Speakers: Sid Pednekar
page: https://ai.engineer/nyc/2026/talks/sid-pednekar | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=21724s
Sid Pednekar follows two hypothetical investment firms to show why widespread access to AI can still produce very different results: the scarce resource is the judgment that shapes the work.

### A Hedge Fund as a Function
Speakers: Frank Long (Coatue)
page: https://ai.engineer/nyc/2026/talks/coatue | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=24466s
Frank Long models an investment firm as a function that turns external and internal context into selection, size, and timing. The engineering challenge appears when that function is decomposed into work that code, models, and people can each perform well.

### Frontier Models for Acting in Space and Time
Speakers: Pim de Witte (General Intuition)
page: https://ai.engineer/nyc/2026/talks/general-intuition | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=25339s
Pim de Witte explains General Intuition’s bet on action-labeled game data: models that observe continuously and select actions while the world keeps moving, with language models available for longer-term planning.

### Hermes gives you wings: Build on open foundations.
Speakers: Dillon Rolnick (Nous Research)
page: https://ai.engineer/nyc/2026/talks/nous | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=26480s
Dillon Rolnick makes the case for owning the agent layer as AI becomes part of everyday business operations. His argument connects model economics to a practical architecture: interchangeable models beneath software and workflows a company controls.

## October 13 · Online track
### We Let Our Financial Planners Write the Agents
Speakers: Matt Ragone (Range)
page: https://ai.engineer/nyc/2026/talks/range | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=10811s
At Range, financial planners write and maintain the skills that draft their work. Matt Ragone explains how to turn professional judgment into a repeatable process without handing client communication to an agent.

### Your Agent Is a Lethal Trifecta (and What to Do About It)
Speakers: Kim Maida (Keycard)
page: https://ai.engineer/nyc/2026/talks/keycard | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=11367s
An on-call agent can be useful and dangerously overprivileged at the same time. Kim Maida follows the same incident queue before and after adding identity, token exchange, and task-scoped policy.

### Your GPU Neighbor Can Hear Your Model
Speakers: Branislav Brzak (Stealthium)
page: https://ai.engineer/nyc/2026/talks/stealthium | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=12897s
Branislav Brzak demonstrates how timing on shared GPUs can reveal model behavior even when memory and compute are partitioned, then explains what operators can control.

### Please… Enough with the Sloppy, One-Shot SaaS Replacements
Speakers: Mahmoud Abdelwahab (Railway)
page: https://ai.engineer/nyc/2026/talks/railway | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=13720s
A working internal app can still be unpleasant to use. Mahmoud Abdelwahab walks through the product details, reusable patterns, and verification loop behind Railway’s agent-built marketing tools.

### Just-in-Time Ontologies
Speakers: Hrishi Olickel (Southbridge)
page: https://ai.engineer/nyc/2026/talks/southbridge | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=14548s
The meaning of a customer depends on the decision being made. Hrishi Olickel explains why data pipelines need contextual schemas, distinct model roles, and bounded experiments that can trade cost against quality.

### Building Reliable, yet Smart Workflows for Finance, Wealth and Insurance
Speakers: Karthic Rao (Perpetual)
page: https://ai.engineer/nyc/2026/talks/perpetual | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=15828s
A request to complete one form can become a process lasting days. Karthic Rao follows that request through Perpetual’s compiler, approval gates, and typed model calls.

## October 13 · Online track · Excerpt
### Agents in Orbit: Workflows, Not Autopilot
Speakers: Eduardo Simon (Flywire), Javier Casal (Flywire)
page: https://ai.engineer/nyc/2026/talks/flywire | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=16766s
Flywire’s Orbit brings engineering agents into an existing GitLab and AWS environment. This opening excerpt covers the company’s infrastructure and privacy constraints before the livestream returns to the live stage.

## October 14 · Main stage
### Chasing capabilities while waiting for the frontier
Speakers: Alexander Shevchenko (Ramp)
page: https://ai.engineer/nyc/2026/talks/ramp | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=1229s
Ramp keeps adopting better frontier models. Alexander Shevchenko shows where specialist training, prepared context, and parallel agents can still save users time before the next model arrives.

### The Machine that Changed the World, vAI
Speakers: Tariq Shaukat (Sonar)
page: https://ai.engineer/nyc/2026/talks/sonar | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=2100s
Agents can produce code much faster than a company can ship it. Tariq Shaukat uses factory design to explain where guidance, independent verification, and evidence belong in an agentic development process.

### Trusting Agents in Policy-Driven Workflows
Speakers: Evan Kormos (Coinbase)
page: https://ai.engineer/nyc/2026/talks/coinbase | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=3124s
A regulated workflow can move forward through fixed approval stages while agents iterate inside each stage. Evan Kormos explains how to choose those stages, evaluate the work, and reduce supervision only when measured confidence supports it.

### Building the Next Chapter of AI in Finance
Speakers: Joseph Kim (OpenAI)
page: https://ai.engineer/nyc/2026/talks/openai | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=4203s
A capable model still needs financial data, familiar outputs, and a way to check its work. Joseph Kim explains the product choices behind ChatGPT for Financial Services and the thresholds he expects finance agents to cross next.

### Security in the Age of AI: Recent Attacks, Incidents & Defenses
Speakers: Andrey Rybka (Bloomberg)
page: https://ai.engineer/nyc/2026/talks/bloomberg | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=5361s
Andrey Rybka follows failures from stolen credentials to poisoned memory. His defense starts with what an agent can actually do: short-lived identities, checks outside the model, and limits that stop execution.

### Towards Autonomous Analysts in Finance
Speakers: Yijia Liang (Compound AI)
page: https://ai.engineer/nyc/2026/talks/compound | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=7177s
An investment team needs more than a chatbot that produces a spreadsheet. Yijia Liang explains why Compound built shared agents, its own Office engines, and tools for navigating large data rooms before asking analysts to delegate longer pieces of work.

### Not All GPU's Are Deployed The Same
Speakers: Oliver Kennon (SemiAnalysis)
page: https://ai.engineer/nyc/2026/talks/semianalysis | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=8700s
Two deployments of the same GPU can produce different amounts of useful output. Oliver Kennon separates chip rental prices from production costs, then explains why operators, service definitions, and benchmarks matter to the compute market.

### How Compute Markets Work
Speakers: Evan Conrad (San Francisco Compute Company)
page: https://ai.engineer/nyc/2026/talks/sf-compute | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=10186s
Evan Conrad traces compute markets back to a startup’s inability to buy the right amount of reliable capacity—and explains why his company ended up operating both the exchange and the hardware.

### The Dark Pools of Compute
Speakers: Affaan Mustafa (Jump Trading), Alejandro Soumah Fernandez (Jump Trading)
page: https://ai.engineer/nyc/2026/talks/jump-trading | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=11709s
Affaan Mustafa and Alejandro Soumah Fernandez map the financing, delivery, and price risks hidden inside a GPU-hour quote—and the market structures needed to separate them.

### Compute Exchange
Speakers: Carmen Li (Compute Exchange / Silicon Data)
page: https://ai.engineer/nyc/2026/talks/compute-exchange | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=13174s
Carmen Li demonstrates a neutral market for reserved GPUs, forward contracts, and used hardware, then connects procurement terms to forward curves and residual asset value.

### Built to Scale: Future-Proofing Your Technology Roadmap
Speakers: John Stecher (Blackstone), Scott Worland (Norm.ai)
page: https://ai.engineer/nyc/2026/talks/blackstone-norm | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=19345s
John Stecher and Scott Worland explain where to invest as models improve: accessible data, evaluations, and production controls—and where to stay willing to replace yesterday’s code.

### Why Wall Street Still Doesn’t Trust AI
Speakers: Vinoo Ganesh (Kepler)
page: https://ai.engineer/nyc/2026/talks/kepler-14 | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=20975s
Vinoo Ganesh separates numerical trust into source selection, exact retrieval, arithmetic, access control, and output verification—and explains why a citation added at the end cannot do all those jobs.

### Coding an Autonomous Wall Street Coworker: Custom Skills, Connectors, and Event Hooks
Speakers: Philipp Schmid (Google DeepMind)
page: https://ai.engineer/nyc/2026/talks/deepmind | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=22308s
A useful background agent needs a workspace, a playbook, credentials, and rules for when to act. Philipp Schmid builds a portfolio-auditing coworker around Gemini Managed Agents, showing how those pieces fit together.

### Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings
Speakers: Joao Wenzel (Citadel Securities)
page: https://ai.engineer/nyc/2026/talks/citadel | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=23913s
A green status slide can conceal a project already slipping. Joao Wenzel describes a system that tracks what a company believes, how old the evidence is, and what happens next—then asks people to correct the beliefs that matter.

### Self-Improving Organizations
Speakers: Will Brown (Prime Intellect)
page: https://ai.engineer/nyc/2026/talks/prime-intellect | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=25528s
Will Brown describes how an organization’s corrections, decisions, and repeated workflows could become training data. Start with evaluations and routing, then give specialized models a way to improve alongside the people using them.

### AI in Practice: An Inside Look at Apollo's Approach
Speakers: Michael Manapat (Rowspace), Jack McDonald (Apollo Global Management)
page: https://ai.engineer/nyc/2026/talks/apollo-rowspace | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=28203s
Michael Manapat and Jack McDonald explain how agents turn fragmented credit data into usable workflows: prepare a portfolio, reconcile financing activity, and leave investment judgment with the people responsible for it.

### Process Supervision for Agents That Do Long-Horizon Work
Speakers: Mitchell Troyanovsky (Basis)
page: https://ai.engineer/nyc/2026/talks/basis | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=29362s
Mitchell Troyanovsky shows how behavior specs, trajectory forks, and inexpensive simulations help diagnose agents that work for hours. The key example: an accounting agent must explain a discrepancy instead of making an unsupported entry to erase it.

### Everything will be Simulated
Speakers: Cristóbal Valenzuela (Runway)
page: https://ai.engineer/nyc/2026/talks/runway | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=30551s
Runway’s early films generated images to watch. Cristóbal Valenzuela shows research aimed at generating images people and agents can act on, moving from video clips toward interactive interfaces and shared visual reasoning.

## October 14 · Online track
### Paving the Road to Production: Governed Enterprise AI Agents
Speakers: Harish Gaggar (Intuit Credit Karma)
page: https://ai.engineer/nyc/2026/talks/credit-karma | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=14322s
Harish Gaggar follows an enterprise agent from registration and deployment through authenticated tool calls, checkpoints, evaluation records, privacy controls, and context optimization.

### The Agent Works. Does Anyone Trust It?
Speakers: Michele Grant (Leading at Scale)
page: https://ai.engineer/nyc/2026/talks/michele-grant | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=16107s
Michele Grant follows an acquisition-reporting agent from a successful pilot to the evidence, ownership, and review practices needed for greater autonomy.

### Tokens Are the Cheap Part
Speakers: Steve Jamison (Jellyfish)
page: https://ai.engineer/nyc/2026/talks/jellyfish | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=17029s
A rising AI bill can accompany a falling cost of delivery. Steve Jamison combines salary and token spending to examine the cost of a merged pull request—and checks whether the apparent gains hide smaller changes or worse quality.

### The Cost of Accessibility in AI
Speakers: Jemima Abu (CAIS)
page: https://ai.engineer/nyc/2026/talks/cais | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=26765s
Jemima Abu uses a small coding-agent experiment to show how missing accessibility requirements create extra code, extra repair work, and products people cannot use.

## October 14 · Online track · Excerpt
### The Automated Security Master: keeping your master database clean with agents
Speakers: Amol Kapoor (Nori Agentic), Clifford Ressel (Nori Agentic)
page: https://ai.engineer/nyc/2026/talks/nori | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=18098s
In this livestream excerpt, Amol Kapoor and Clifford Ressel explain how cloud agents can trace a changed security-master cell back to its evidence—and why the person who understands the discrepancy still matters.

### Your AI Isn’t the Problem. Your Infrastructure Is.
Speakers: Jiachen Jiang (Coder)
page: https://ai.engineer/nyc/2026/talks/coder | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=27389s
This livestream excerpt captures Jiachen Jiang’s opening argument: an instruction to avoid destructive work is weaker than infrastructure that prevents the action.

