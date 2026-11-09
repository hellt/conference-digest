>>> HOW TO RUN THIS <<<
This is the digest prompt for atscale-ai-data-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/atscale-ai-data-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/atscale-ai-data-2026.md
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

Below is the program for @Scale: AI & Data 2026. Read it and produce a digest
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
conference: @Scale: AI & Data 2026
source_url: https://atscaleconference.com/events/ai-data-2026/
generated: 2026-11-09
registry_key: atscale-ai-data-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## Schedule
### Keynote from Meta
Speakers: Barak Yagour (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-4 | video: https://www.youtube.com/watch?v=L0BSZb7ujC8
No abstract published; title, speakers and materials only.

### Fireside Chat with Boris Cherny, Head of Claude Code
Speakers: Boris Cherny (Anthropic), Jesse Chen (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-5 | video: https://www.youtube.com/watch?v=Z47vatpsGPI
No abstract published; title, speakers and materials only.

### Data Governance in the World of Agents
Speakers: Komal Mangtani (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-6 | video: https://www.youtube.com/watch?v=cbjagBWf5aU | materials: https://atscaleconference.com/data-governance-in-the-world-of-agents/
AI agents are rapidly moving from demos to production, acting autonomously across tools, data systems, and workflows—and in the process, they amplify data movement far beyond what traditional governance models were designed to handle. Data security controls built for humans break down when agents operate at machine speed, execute in parallel, and persist sensitive information across new data surfaces like trajectories, embeddings, logs, and tool outputs.
In this talk, we outline the emerging data governance failures in agentic architectures—identity confusion for data access, entitlement creep, recursive leakage across agent chains, new data constructs leading to old controls becoming obsolete, and why out of box agent harnesses and existing IAM are insufficient. We then present Meta’s governance-first approach for safely enabling agents at scale: a defense-in-depth stack centered on Isolation Domains (domain-scoped encryption and output closure), Agent Identity (end-to-end attribution distinct from the user), Agent-Aware Access Control (classification-aware ABAC evaluated at query time), AccessMate (zero-standing-permissions access triage and least-privilege fallback), CodeGuard (secure code generation and runtime execution guardrails), and DataVM—a unified trusted data environment that bounds inputs, tools, and outputs under one governed scope.
Attendees will leave with a concrete reference architecture for building agents that are not merely powerful, but governable, auditable, and regulatory-ready—turning governance from a blocker into the harness that safely unlocks agent autonomy.

### Bridging the Intent Gap in Agentic Systems
Speakers: Anoop Deoras (AWS)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-7 | video: https://www.youtube.com/watch?v=ILWNbbK9GCE
No abstract published; title, speakers and materials only.

### Why have we not solved security of agents?
Speakers: Ilia Shumailov (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-8 | video: https://www.youtube.com/watch?v=Eps9iGyYiBM
The security community spent decades building rules and frameworks that made systems harder to break. AI has fundamentally upended those lessons -- attackers are now more enabled than ever, and traditional defences don't translate. This talk examines prompt injections, indirect prompt injections, and jailbreaks, showing why each resists simple fixes. Drawing on hands-on experience building AI security tools, I'll demonstrate why rules-based approaches fail against systems that interpret natural language as instruction. But there is hope: I'll share defensive approaches that actually work and outline a credible path toward resilient AI systems.

### Q&A Session
Speakers: Komal Mangtani (Meta), Anoop Deoras (AWS), Ilia Shumailov (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-9 | video: https://www.youtube.com/watch?v=YwVCvjTn76Y
No abstract published; title, speakers and materials only.

### Live Panel: Agentic autonomy & evolution of software & research
Speakers: Faisal Siddiqi (Meta), Henry Eskrine Crum (Meta), Joe Spisak (Reflection AI), Jessica Fu (Meta), Xing Chen (Databricks), Matt Schlicht (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-11 | video: https://www.youtube.com/watch?v=5RyU5RyJm1w
No abstract published; title, speakers and materials only.

### Tuning Your Algorithm with MRS Memory System and Think-Then-Recommend (TTR)
Speakers: Qi Guo (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-12
Users have long wanted to understand and control the algorithms that shape their recommendations, but enabling meaningful user agency over recommendations has remained challenginging — until now. We present Tune-Your-Algorithm (TYA), an AI-powered agentic recommendation system on Instagram that gives users transparent visibility into the recommendation algorithm and the ability to tune it using natural languages.
TYA is built on two key innovations: (1) the MRS Memory System (Biography), an LLM-based framework that summarizes user engagement histories into rich, structured, and interpretable user interest and intent representations at scale; and (2) Think-Then-Recommend (TTR), a reasoning-augmented approach that decomposes user interests and complex user intents into personalized sub-goals for personalized and contextualized recommendations.
Early results show strong product-market fit with positive user feedback on transparency and user agency enabled by TYA. We discuss the end-to-end architecture, production learnings, technical challenges we are actively tackling, and the path towards our north star vision.

### Observability: Role of Evals, Benchmarks & Data in Frontier AI
Speakers: Alex Ratner (Snorkel AI)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-13 | video: https://www.youtube.com/watch?v=iX79X61Jonk
The excitement around agentic AI is real — backed by quantitative progress on model cards and genuine leaps in capability. But our ability to measure AI has been outpaced by our ability to develop it, and closing this evaluation gap is one of the most important problems facing the field. More enduring benchmarks are needed to advance the next vectors of capability and chart the path to reliable agents.
In this talk, Snorkel AI Co-Founder and CEO Alex Ratner will share insights from major research and benchmark collaborations on agentic coding and continual learning, along with practical tips from working with global frontier labs and leading academics. He'll focus on three dimensions where today's models most often break down, and where the next generation of benchmarks will need to deliver real signal: environment complexity (how dynamic and rich the operating world is), autonomy horizon (how far an agent can act independently), and output complexity (how sophisticated and verifiable the deliverable is).

### How Meta Scaled AI Training Storage via Data Normalization
Speakers: Sarang Masti (Meta), Weiran Liu (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-14 | video: https://www.youtube.com/watch?v=ZyAoUSmbntI
Training data for Meta's recommendation systems was entirely stored in Data Warehouse, structured as relational tables where each row captures labels and snapshotted features at the point of recommendation.
New modeling techniques, such as learning from user sequences and multi-modality, has led to a 10-100x increase in feature size, making the training data increasingly cost-prohibitive due to high duplication. The same user's features are stored repeatedly for every recommendation request, with highly popular content features being duplicated potentially over a million times.
We present a co-designed data and infrastructure in order to address the scaling challenge. By moving features out of training samples into a high-performance indexing storage and implementing model access pattern-aware pushdown optimizations, we have achieved a 10x storage cost reduction for the largest feature: long user sequences.

### Architecting Infrastructure for the AI Native Future: Scaling Autonomous Agents on Google TPUs
Speakers: Sabastian Mugazambi (Google)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-16 | video: https://www.youtube.com/watch?v=MUxbhxzIMpQ
As the industry pivots toward an "AI Native" paradigm, the bottleneck for innovation has shifted from algorithmic design to the underlying infrastructure's ability to handle unprecedented scale and complexity. This session explores how Google TPU (Tensor Processing Unit) infrastructure serves as the catalyst for this transformation, specifically within the domains of large-scale Recommender Systems, MoEs, LLMs and the emerging era of Autonomous Agents.We will delve into the architectural innovations of the latest TPU generations, demonstrating how their purpose-built design facilitates the massive throughput required for real-time recommendation engines and the high-speed inference necessary for agentic orchestration.

### Agentic Data at Scale: Transforming Data Experiences at Meta
Speakers: Dinkar Pataballa (Meta)
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-17 | video: https://www.youtube.com/watch?v=BQf0TxsOMUg
Every major business decision is ultimately built on data, yet getting to the right answers has long required specialized expertise, from knowing which tables to query to how to query them to building the right data applications. AI agents are fundamentally changing that equation, making data accessible to anyone who can ask a question in plain language. At Meta's scale, with millions of datasets serving tens of thousands of decision-makers, this shift creates both massive opportunity and unique challenges around trust and accuracy. This presentation will detail how we built AI-native data experiences to address two key dimensions: enabling trusted answers through agentic data consumption, and letting users create shareable agentic data applications without writing a single query.

## Poster Sessions
### Agent Memory at Meta Scale: One Query Language for Graph, Vector, and Memory
Authors: Abdullah Ozturk, Yiting Li, Vishal Gandhi, Ming Chen, Junjie Qi
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-20
Agent memory is the new scaling axis for AI assistants. Useful agents accumulate episodic conversations, semantic patterns, working state, and procedural skills — and every retrieval composes vector similarity, graph traversal, and structured filters over them. Today this lives across fragmented APIs (vector indexes, graph services, RAG frameworks, per-product memory stores), forcing every agent stack to stitch three or four services together on the critical path of every turn.
We present the Cypher Query Layer (CQL) — an AI-native, declarative query surface for agent memory built on the openCypher / GQL standard (ISO/IEC 39075:2024). CQL collapses hybrid retrieval (vector + text + graph + scope + freshness + provenance) into a single optimizable query. A pluggable backend architecture routes each query to its right-fit substrate — in-process Velox for sub-50 ms agent-loop reads — while reusing Meta's existing storage (graph, vector, hybrid). On the roadmap: composable procedure packs for memory management (distillation, consolidation, governance), and a distributed MPP backend for corpus-scale retrieval.
Unlike per-product memory SDKs, CQL treats memory as a query surface rather than an API: graph, vector, and structured filters compose in one plan, with identity-aware ACLs as first-class primitives.
We share the architecture, production patterns from an early agent-platform consumer at Meta, the design we are pursuing for bi-temporal memory to enable agent-debugging replay, and where the in-process vs distributed boundary actually falls in practice.

### Agentic Data Flywheel: A Multi-Agent System for Scalable Multimodal Training Data Production
Authors: Wendy Jiang, Selahattin Akkas, Alan Li, Antoine Simoulin
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-21
We present an agentic data flywheel that automates the production of high-quality multimodal training data at scale. The system orchestrates multiple specialized VLM agents - a labeler, parallel quality reviewers with a summarizer, and a self-correcting adjuster - to automatically annotate, review, and fix image-text annotations with minimal human intervention. When agents disagree, images and labels are escalated to human review; When the adjuster agrees with corrections, fixes are applied automatically.
The multi-agent system wraps probabilistic VLM reasoning inside deterministic scaffolding: a fine-tuned specialist VLM produces structured annotations, an ensemble of concurrent evaluators independently assess grounding quality, text accuracy, and semantic classification quality; and a thinking-model powered judge arbitrates disagreements - overruling false positives, diagnosing root causes, or applying targeted fixes to salvage otherwise-human intervention required labels. Key design principles include agent isolation to prevent confirmation bias, deterministic routing around probabilistic judgement, and structured output constraints that force closed-choice decisions with every failure mode defaulting to human escalation.
The system delivers a 3X efficiency gain: 60%+ of annotations pass with no human involvement, and remaining cases are routed to human annotators prefilled with agent corrections and targeted hints - transforming the task from annotation to verification and improving labeling quality. A key enabling capability is multilingual bootstrapping: with multilingual VLMs, the flywheel enables scaling annotation across 100+ languages, transforming what was a per-language staffing bottleneck into a prompt configuration change.
We demonstrate the end-to-end system on an image text labeling task and discuss generalization to scene understanding, chart understanding, document VQA, and grounding & localization.

### Agentic Inference Optimization for RecSys ML models
Authors: Shuyao Bi
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-22
Modern recommendation models built in PyTorch require multi-stage post-training optimization to meet production inference latency targets. Kernel fusion that replaces sequences of individual operations with a single fused kernel via Torch FX graph transformations is one of the most impactful techniques, reducing kernel launch overhead and memory transfer costs to deliver measurable throughput gains.
Traditionally, identifying fusion opportunities and authoring correct graph transformations has required deep expert knowledge and ~40 hours of manual iteration per model. Transformation choices are fragile to model updates and quickly become stale, creating a scalability bottleneck as model architectures evolve at increasing velocity.
We present an automated optimization agent that replaces this manual process: it detects fusion opportunities from GPU traces and FX graph structure, generates and validates graph transformations — all orchestrated through an iterative, self-converging workflow.

### ASEA: Autonomous Agents for ML Serving Efficiency at Scale
Authors: Bikash Sharma, Aashik Gowda, Angineh Keshishian, Mia Gu, Michael Fulthorp, Jinfu Leng
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-23
Large-scale ML serving at Meta runs hundreds of models across CPUs, GPUs, and MTIA, consuming hundreds of megawatts. Service overhead — the gap between theoretical minimum and actual resource usage — often reaches 50% of total footprint, yet the optimization loop remains human-bottlenecked: engineers manually stitch together telemetry, profiling, and capacity data in a multi-day workflow that leaves millions of dollars of efficiency on the table every quarter.
We introduce ASEA (Autonomous Agentic Platform for Large-Scale ML Serving), an AI-powered agentic platform with dozens of specialized LLM agents that autonomously orchestrates the full lifecycle of Meta's ML serving infrastructure optimization — from opportunity discovery through root-cause diagnosis, configuration generation, canary validation, and production rollout.
Each agent owns a single skill (capacity sizing, autoscaling, batching, routing, hardware migration, regression detection, etc) and shares a unified data foundation spanning the fleet. In production, ASEA has delivered tens of millions of dollars in validated efficiency savings and turned a multi-day, expert-only workflow into an autonomous, fleet-wide one.

### Cache the Session, Not the Data: 40x Faster ML Iteration with a Shared Sidecar at Meta
Authors: Rohil Bansal, Eric Fu
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-24
ML training iteration on developer workstations pays a heavy data preprocessing tax. Each launch of a model spins up its own data preprocessing client, which has to establish a session with the backend, run query optimization over the user's preprocessing plan, perform metadata lookups to translate logical queries into physical data locations, and warm up its readers. In our environment this is on the order of 5+ minutes per launch. For ML engineers iterating on trainer changes, this cold-start cost dominates the inner loop and discourages tight iteration cycles.
We present the Shared Sidecar(SSC): an out-of-process daemon that caches warmed preprocessing sessions across local runs on a developer workstation. Sessions are keyed on a hash of the input dataframe and the preprocessing plan; subsequent runs whose hash matches reuse a pre-warmed session and skip the entire startup path. The sidecar handles session lifecycle (8h idle eviction, 1h whole-process timeout), bounded memory through a warmed-session cap, and graceful degradation when the daemon is unavailable.
SSC has been rolled out to all of our developer workstations, enabled by default, with no correctness regressions. On repeat launches of the same configuration we measure roughly 40× speedup (benchmark: a click-through-rate model dropped from 391s to 9s).

### Citrine: Catching Million-Dollar ML Anti-Patterns Before They Ship
Authors: Prakash KL; Chenguang Zhu, Shyam Sundar Chandrasekaran; Jon Dyer
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-25
Ensuring ML code efficiency is a multi-million-dollar problem at Meta's scale. Common PyTorch ( https://pytorch.org ) anti-patterns such as unpinned DataLoader memory, redundant host-to-device transfers, and suboptimal optimizer configurations silently degrade training performance across thousands of jobs. Triton GPU kernel code exhibits analogous pathologies at the kernel layer, including flattened loops that forgo proper tiling. A single one-line misconfiguration can cost thousands of dollars per trainer; replicated fleet-wide — and across the broader AI industry, where hyperscalers collectively spend tens of billions of dollars annually on GPU compute and draw megawatts of grid power — the waste compounds into massive losses of capital and energy. As AI coding agents now author a growing share of production ML code, these inefficiencies are being reproduced at machine speed and at unprecedented volume, making detection at the code-authoring phase the only scalable defense.
We present Citrine , an always-on, zero-overhead efficiency system that detects 45+ ML efficiency anti-patterns spanning both PyTorch core and Triton kernel code through static analysis and AST transformation built on top of LibCST ( https://github.com/Instagram/LibCST ), and is integrated directly into Meta's arc lint pipeline. Every detector ships with a deterministic AST rewriter that surfaces a one-click suggested edit on every diff under review. In the past 90 days, Citrine has landed 4,700+ accepted fixes across 10+ product groups — including Generative AI, Reality Labs, Instagram, Monetization and Ads — saving millions of dollars annually in GPU compute waste and yielding measured improvements of up to 43% on affected Triton kernels .
Beyond Meta-internal impact, Citrine has become the de facto home for TorchFix ( https://github.com/pytorch/torchfix ), the open-source PyTorch hygiene project: 13 TorchFix rules — covering deprecated-symbol migrations, the unsafe torch.load deserialization vector, common API typos, and TorchVision migrations — now ship as first-class Citrine patterns, giving developers a single integration point for PyTorch-ecosystem hygiene alongside specific vetted efficiency rules. Through partnership with the open-source Triton compiler team ( https://github.com/triton-lang/triton ), Citrine also integrates 12+ Triton-lint rules detecting kernel-level pathologies such as missing @triton.autotune decorators, accumulator-precision regressions, warp-divergent control flow, and barrier deadlocks — unifying static analysis across the high-level PyTorch layer and the low-level GPU kernel layer in a single linter.
To address the rapid growth of agent-authored ML code, we further transformed Citrine from a reactive lint tool into a proactive efficiency system by shifting left into the model-authoring workflow. By encoding anti-pattern knowledge directly into Meta's LLM code-authoring framework, PyTorch-specific efficiency rules are injected into AI coding agents at code-generation time, ensuring that both experimental and production code is free of canonical inefficiencies before it is ever written. We present this end-to-end architecture in the context of the software development lifecycle (agentic codegen → linting → CI/Diff → ship), together with an attribution methodology that connects individual lint fixes — both human and AI-authored — to validated efficiency wins at fleet scale.
The approach Citrine pioneers — uniting static analysis with AST-driven remediation at the moment of authorship and reinforcing that knowledge in the LLM-codegen layer — generalizes well beyond Meta. As AI training infrastructure expands toward multi-gigawatt scales and agentic development becomes the standard mode of ML engineering, code-time efficiency enforcement is, in our view, a necessary layer in any sustainable AI compute stack. We continue to upstream generalizable rules through TorchFix and the Triton-lint project so the broader ecosystem benefits. We are extending Citrine in three directions: (1) coverage of emerging hardware and software stacks beyond PyTorch and Triton; (2) tighter integration with LLM coding agents so efficiency knowledge evolves alongside model capabilities; and (3) publishing the attribution methodology so independent researchers and other infrastructure teams can replicate fleet-scale efficiency measurement.

### Designing for Human Agency in AI-Augmented Software: A Quality Attribute Approach
Authors: Rohan Vardhan
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-26
As artificial intelligence becomes embedded in everyday software, a quiet architectural assumption has taken hold: that human-centeredness is a design philosophy, not a software quality attribute. This article challenges that assumption. Drawing on practitioner experience across multiple organizations and recent research in human-AI interaction, requirements engineering, and software quality models, we argue that existing frameworks, including ISO/IEC 25010:2023, do not adequately capture the properties that make AI-augmented software supportive of human judgment rather than corrosive to it. We propose four quality attributes specific to human-AI systems: Agency Preservation, Calibrated Trust, Contestability, and Learnability of Limits. Together these form the ACCL framework. For each attribute, we present architectural implications and organizational patterns grounded in field observation. We also identify three practitioner-observed failure modes not yet captured in the literature: reflexive bypass, trust debt, and the right-sized explanation problem.

### Evaluating Opsmate: Grading AI Incident Investigations at Scale
Authors: Chinmay Gandhi, Narayanan Sankaran, Khushbu Thakur, Ankit Agarwal, Vaidyanathan PK, KC Balsu, Akash Jothi
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-27
Opsmate is an autonomous agent that investigates ~1.5k incidents per day at Meta. Getting agents to run is easy; knowing if they did a good job is hard. Evaluating open-ended agent behavior on real production incidents is fundamentally hard - ground truth is expensive to curate, correctness is subjective and multi-dimensional, and agents can inadvertently introduce data leaks
Opsmate Evals solves these challenges by measuring and validating the quality of autonomous incident investigation agents at Meta that is orchestrator and model agnostic. The framework combines automated ground truth synthesis from post-incident artifacts like chat transcripts, fix diffs, and retro docs - with LLM-as-judge graders that score investigations on a calibrated 0-100 scale across root cause accuracy, investigation path logic, and mitigation actionability.

### Leading warehouse autonomy with trust
Authors: Sagie Gur-Ari
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-28
Meta operates one of the world's largest data warehouses -- millions of tables, tens of thousands of pipelines, and a constantly shifting capacity surface no human team can supervise end to end. We are transforming warehouse operations from reactive alerting to autonomous resolution: an agent control plane that detects, diagnoses, and acts on pipeline and capacity issues at scale, not just routing issues.
Trust is the foundation, not a feature. Every autonomous action is bounded by transparent guardrails, full audit history, provenance on every decision, and human-in-the-loop controls calibrated to stakes. Oversight scales with autonomy -- users always retain visibility and the ability to intervene as the system's authority grows.

### LP Planner: Synchronization-Aware Sharding Optimization for Large-Scale DLRM Model Training
Authors: Mine Su Erturk, Greg Macnamara, Caner Gocmen, Isuru Janith Ranawaka, Felicity Liao, Ahmed Shuaibi, Alireza Tehrani, Hammad Ather, Shafeeq Ibraheem, Kaustubh Vartak, Nipun Gupta
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-29
LP Planner is a novel optimization tool that generates sharding plans for Deep Learning Recommendation Models (DLRMs) to enable more efficient distributed training. LP Planner formulates the sharding problem as a linear program, jointly optimizing table placement and partitioning strategies across devices and device memory hierarchies to minimize peak memory usage and maximize training throughput.
LP Planner has been deployed to several production models across various PGs, including few of the largest models by training spend. In production, LP Planner delivers up to 8% QPS improvement and 14% peak memory reduction per model launch.
Beyond direct model launches, LP Planner has been integrated into various agentic auto-tuning pipelines saving significant engineer-hours. Ongoing work includes workload-specific critical path modeling, shard type selection, and heterogeneous hardware awareness.

### Meta-ML: Supercharging ML Productivity at Scale with AI-Native Infrastructure
Authors: Niv Taiber, Bar Ulman, Ravali Busetty, Aasim Rab, Brant Swidler
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-30
Meta operates one of the largest ML Infrastructure stacks, with thousands of Machine Learning Engineers (MLEs) across legacy systems built over years. These engineers navigate a complex landscape of legacy services spanning the full ML lifecycle—from data discovery and feature engineering through model training, experiment tracking, serving, and capacity planning—where frequent context switching introduces significant operational overhead.
In this poster, we'll share how we made this legacy ML infrastructure stack agent-callable at scale without rebuilding it, through Meta-ML—an AI-native infrastructure layer that provides programmatic access through specialized CLI tools and composable skills. We present:
* Progressive Tool Disclosure Architecture — How agents discover relevant capabilities on demand rather than loading all 200+ tools upfront, reducing context window pressure while maintaining broad infra coverage * Federated Domain-Team Ownership — How 15+ infrastructure teams expose their systems as agent-callable tools, embedding domain expertise directly into the agent interface and how tool coverage is driven by a systematic mapping of MLE jobs-to-be-done across each stage of ML lifecycle * Production-Grounded Flywheel — How we instrument real MLE sessions to extract evaluation cases grounded in actual workflows—capturing tool sequences, failure modes, and resolution paths that synthetic benchmarks miss and continuously improve our infrastructure. * Impact at Scale — Meta ML now has over 200+ tools, 7k+ installs, CLI WAU is >8k, 1,600+ WAU with ~59% adoption among power users generating 4M+ tool calls/week; debugging workflows reduced from 1.5 hours to under 10 minutes
We share architectural patterns and operational lessons for making legacy ML infrastructure agent-callable—including progressive tool disclosure, federated domain-team ownership, and production-grounded eval—that transfer to any organization operating ML systems at scale.

### Scaling Batch Graph Processing to Trillions of Edges
Authors: Sahil Gandhi, Arneish Prateek
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-31
Introducing Meta's new batch graph processing engine, built for the efficient execution of iterative graph algorithms on massive datasets (billions of nodes, trillions of edges). This engine supports various use cases at Meta scale, including LLM pre-training, recommendation systems, data deduplication, and ranking.
The engine tackles critical constraints associated with large-scale batch graph jobs—specifically memory blow-up, skewed shards, network overhead, centralized coordination, and gang-scheduling. It achieves this by reducing costs across data storage, graph partitioning, network communication, engine execution, and distributed coordination. Furthermore, its pluggable architecture accommodates diverse distributed graph processing models.

### SparkSentry: Autonomous Error Detection, Triage, and Repair for Spark at Scale
Authors: Varun Srinivas
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-32
Meta runs millions of Spark jobs daily across a fleet processing hundreds of petabytes. When failures occur, oncall engineers manually sift through Scuba dashboards, classify errors, file tasks, and investigate root causes — a process that takes hours per incident and doesn't scale with fleet growth.
SparkSentry is an autonomous monitoring pipeline that closes the loop from error detection to code fix with no human intervention. Running twice daily, it ingests thousands of job failures from Scuba, clusters them by root cause using a three-stage approach (deterministic regex matching, TF-IDF + DBSCAN for unknown errors, and LLM semantic merging via Llama 3.1-70B), then analyzes severity using rate-based regression detection scaled to fleet size. For high-severity clusters, SparkSentry creates Phabricator tasks with full investigation context — Scuba links, stack traces, affected users, and codebase-specific investigation instructions — then delegates them to AI agents that autonomously locate the bug in the Spark codebase, write a fix with tests, and submit a diff for review.
Key results: SparkSentry processes ~10K errors per run, produces ~20-50 root cause clusters, and has autonomously generated fixes for error classes affecting thousands of jobs. A multi-layer dedup system (exact cluster ID matching, flexible title matching, normalized title grouping with diff migration) prevents duplicate task creation across runs — reducing oncall noise by eliminating the 7-10 duplicate tasks per error class that manual monitoring produced. The pipeline combines deterministic classification (36+ regex patterns), unsupervised ML clustering, and LLM-powered semantic analysis, with each layer handling failures the previous layer misses.
SparkSentry demonstrates a production-grade pattern for agentic infrastructure monitoring: detect → classify → triage → fix → review, operating continuously without human initiation while maintaining human oversight at the review stage.

### The Agent Feed: A Communication Layer for Multi-Agent Collaboration
Authors: Chinmay Gandhi, Vlad Tsvang, Patrick Walsh
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-33
When multiple AI agents work on the same problem, their outputs are typically siloed—each producing findings independently with no way to build on each other's work, and no way for humans to separate agent signals from their own discussion.
We built the Agent Feed: a shared communication layer where agents publish findings, read each other's outputs, and collaborate through a standardized API. This enables a consensus-driven investigation model—specialist agents contribute domain-specific evidence, a coordinating agent ranks competing hypotheses against independent data sources, and confidence strengthens as multiple signals corroborate. Humans provide lightweight feedback (thumbs up/down) that closes the loop, shaping which findings get promoted and which agents improve over time.
To scale openly without degrading quality, a tiered channel system ranks agent output by trust level (Core > Validated > Experimental), with self-serve onboarding and quality-gated graduation. Responders always see the highest-confidence findings first.
The pattern generalizes beyond incident response: wherever multiple agents operate on a shared artifact, you need a structured communication layer, a consensus mechanism, and a trust framework.

### XStream: Meta's unified stream processing service
Authors: Stella Kaval, Zheng Zhang, Shuo Xu, Jun Fan
page: https://atscaleconference.com/events/ai-data-2026/#agenda-item-34
Real-time stream processing has become a critical infrastructure at Meta, powering a wide range of products and services including Ads, Reels, Search, Meta AI, and Graph Learning. Over the past decade, Meta developed multiple in-house stream processing systems to support fast-growing business needs. While this approach enabled rapid iteration, it increasingly caused confusion for developers, elevated maintenance burden, and reduced engineering efficiency. To address these challenges, we built XStream, a unified, fully managed stream processing service that consolidates all existing solutions onto a single platform.
XStream has been in production for about six years. It is designed around the principles of ease of authoring, language unification, operational simplicity, high performance, data freshness, and reliability. XStream supports a wide range of applications, including real-time analytics, analysis of distributed traces, and machine learning feature generation. Today, XStream processes data at O(10) TB/s throughput across 70,000+ pipelines running on O(100)k hosts.
This paper presents XStream's architecture and the key design choices behind it. We describe XStream's multi-language authoring layer (SQL, Python, and C++), its vectorized C++ execution engine built on Velox, and its service management platform, Turbine. We deep-dive into the solutions to core technical challenges: exactly-once processing, efficient large-scale shuffling via Scribe-based shuffle, scalable state management with both ZippyDB and the new RocksDB+Manifold state store, and the adoption of the Kappa architecture and Event-level Aggregation Infrastructure (EAI) for improving machine learning feature freshness. We also describe how XStream has evolved over time, including the introduction of the Unified Trigger Framework (UTF) for stateful processing and CodeX for decoupling user logic from engine execution. Finally, we share our production experience scaling XStream to support tens of thousands of pipelines with high availability, reliability, and efficiency, and discuss lessons learned along the way.

