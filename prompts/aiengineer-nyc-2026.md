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
Speakers: Sam Green (Bridgewater Associates), Aaron Linsky (Bridgewater Associates)
page: https://ai.engineer/talks/CLve4Nx_RwI-bridgewater-turned-100-million-documents-into-edge | video: https://www.youtube.com/watch?v=CLve4Nx_RwI
Sam Green and Aaron Linsky describe Bridgewater's Vault, a platform for making internal and external unstructured information usable by investors and agents. Green reports more than 100 million documents from 135 external sources alongside internal material. Documents are cleaned, governed, and enriched against the firm's ontology, including countries, concepts, markets, and the time periods discussed. Their three lessons are to design separately for human and agent needs, serve both through a shared tool, and build toward proactive agents. In a demonstration about AI infrastructure investment and the Korean won, Green contrasts open-web research with Vault-connected research. He reports that the web workflow found 15 candidate resources but used only one or two and relied partly on a stale note. The Vault workflow narrowed the period to October 1–8, found 52 candidates, and used seven documents. This illustrates evidence coverage and temporal relevance, rather than establishing the investment question's substantive answer. Linsky emphasizes precision for human readers, scale for agents, and filtering for both. A manually assembled benchmark of about 200 examples, built in less than a week, measured initial precision@10 at about 60%. He reports improvement to approximately 90–95% after search improvements culminating in agentic search, although his closing metric wording briefly mixes recall and precision. He describes switching to turbopuffer for native metadata filtering and agent-scale throughput. Adoption required reproducing familiar email habits through saved searches and collections, then expanding access across chat, mobile, Slack, IDEs, and a CLI. The speakers describe Vault-backed research assistants, macroeconomic forecasts, and investment signals. The Investor Workbench moves beyond reactive answers by proposing topics with summaries, supporting evidence, and links to deeper analysis. Green says investor–agent collaboration is captured back into the Vault, preserving synthesis for subsequent research and compounding the firm's knowledge.

### Balancing Acceleration and Safety for AI Agents
Speakers: John Feminella (Two Sigma)
page: https://ai.engineer/talks/iniryju23Sk-what-900m-bank-error-teaches-us-about | video: https://www.youtube.com/watch?v=iniryju23Sk
John Feminella, who introduces himself as working on AI architecture and engineering at Two Sigma at the time of recording, presents a framework for giving enterprise AI agents useful autonomy with enforceable controls. He explicitly states that the views are his own, not Two Sigma's. His opening case study recounts Citibank's August 2020 Revlon payment error: a workflow intended to distribute roughly $8 million in interest instead sent roughly $900 million in principal after wash-account settings were missed and three approvers accepted a warning consistent with their expectation that some money should leave the bank. He uses the story to illustrate how procedures and human approval can fail despite operators believing they are acting correctly. Rather than relying on blanket lockdowns, unrestricted access, or prompt-level policy documents, he proposes five composable controls: a registry recording agent ownership, tools and endpoints; risk-based review that distinguishes small experiments from production-changing agents; tool permissions scoped to declared purpose and enforced through registry-derived runtime policies; shared firm-wide evaluation infrastructure with agent-specific tests; and runtime rules and conservative classifiers that reserve human attention for consequential or uncertain decisions. He compares evals to unit tests and treats model changes as changes to an application's runtime dependencies. To illustrate approval and instruction-retention risks, he recounts an OpenClaw email-deletion anecdote, attributing the loss of an approval requirement to context compaction. His closing analogy is that brakes enable cars to travel quickly and stop safely: agent controls should similarly enable useful work rather than merely prevent action.

### Does Code Quality Even Matter?
Speakers: Max Kanat-Alexander (Capital One)
page: https://ai.engineer/talks/bU5gDVyu_28-does-code-quality-still-matter-it-depends | video: https://www.youtube.com/watch?v=bU5gDVyu_28
The speaker proposes a framework for deciding when code quality matters: software engineering depends on understanding actual system behavior and acting on that understanding, especially when changing a system safely. Using Chromium and its URL parser as examples, the talk argues that understandable component structure makes complex software tractable. Changes carry two risks: introducing an immediate problem and making future changes harder, with the latter compounding the former over time. The speaker distinguishes disposable software—low failure consequences, few dependents, cheap replacement and negligible maintenance—from durable software with substantial dependencies, consequences and upkeep. In this framework, code quality is unnecessary at the fully disposable end but essential for durable systems; engineering rigor should vary across the spectrum, with conservative estimates favoring durability. The speaker predicts that AI coding tools will expand both categories rather than eliminate durable engineering. To increase disposability, the talk recommends isolated environments with restricted data access, independence from inbound production dependencies, durable fallback systems and narrow scope. A complementary strategy is to make rigor cheaper so that misclassifying a system as disposable is easier to recover from. Suggested practices include standardizing languages, frameworks and protocols; automatically running fast, reliable tools within the developer workflow; investing in fast, deterministic testing and shared in-memory service fakes; and enabling strict lint rules early, provided false positives remain tolerable. The conclusion is that code quality matters for durable software, not fully disposable software, and rigor need not be expensive.

### What does an AI engineer do?
Speakers: Aparna Dhinakaran (Arize)
page: https://ai.engineer/talks/ImnZ7s68jw8-what-does-ai-engineer-do-now | video: https://www.youtube.com/watch?v=ImnZ7s68jw8
In this talk, attributed by recording metadata to Aparna Dhinakaran of Arize AI, the AI engineer’s role shifts toward building systems that repeatedly build, evaluate, ship, monitor and improve agent applications. Dhinakaran presents Signal as an always-on agent that reads production traces, identifies recurring issues, remembers earlier findings and can propose fixes or open pull requests with repository access. She describes scheduled, event-based and metric-based triggers, followed by runs that gather traces, third-party telemetry and repository context inside a sandbox with a single proxy. Findings and run telemetry persist; learned skills may be saved to the repository, while the sandbox, credentials and repository access are removed after a run. State stored outside the sandbox enables recovery after sandbox or harness failures. The talk describes support for Claude Code, Cursor and Codex and discusses model choices as a way to compare quality and cost. A central responsibility is defining good outcomes through evals aligned with human judgment: engineers inspect errors, build reference datasets and evaluate judges against human outputs before releasing evaluators. Offline tests and online evaluations feed the same improvement loop. Dhinakaran closes by urging teams to trace both application agents and the coding agents that build them, using telemetry and evaluations to identify failures and improve products.

### Wells Fargo Foundation Model: Application to Fraud Detection at Scale
Speakers: Freddy Lecue (Wells Fargo)
page: https://ai.engineer/talks/UB6hoWyh3B0-bank-trained-its-own-foundation-model-catch | video: https://www.youtube.com/watch?v=UB6hoWyh3B0
The talk presents Wells Fargo's transaction foundation model: a reusable transformer backbone pretrained from scratch on billions of customer transactions across card, digital and check channels. It learns through next-token or next-transaction prediction, then supports downstream adaptation. The speaker emphasizes tokenization as a central challenge: mapping numerical and categorical fields, including amounts, time gaps and postal codes, into a manageable vocabulary and embeddings. The reported decoder-only model has 1.1 billion parameters, with an 11-billion-parameter version under development at the time of the talk. Training experiments required substantially more tokens per parameter than the initial Chinchilla-inspired estimate. For fraud classification, the model uses transaction history through attention; the speaker suggests this helps explain its improvement over the production XGBoost baseline. The speaker reports higher fraud detection, fewer false positives and millions of dollars in savings, without supplying exact comparative rates in the transcript. A sub-250-millisecond authorization requirement is discussed, but contradictory latency wording prevents a reliable measured-latency claim. Fraud detection is the demonstrated application; credit line increases, anti-money laundering and marketing are described as areas under investigation.

### Inside Arca’s long-horizon agents that run the business
Speakers: Aman Singh (Arca)
page: https://ai.engineer/talks/oP2WLFpMoDY-inside-arcas-long-horizon-agents-that-run | video: https://www.youtube.com/watch?v=oP2WLFpMoDY
Aman, who introduces himself as leading AI at Arca, describes a financial-services firm organized around agents owning client outcomes across days of interrupted work. He distinguishes long-horizon workflows—with waiting, decisions and handoffs—from continuously running inference. An illustrative tax-payment workflow follows Jane's cash-raising plan through analysis, asset liquidation, settlement and an ACH transfer. Arca's architecture combines background agents monitoring external and internal signals, operational context, a harness with tools and guardrails, persistent client memory, and shared spaces for discussion and human approval. Agents register interest in future events, receive routed signals, wake on schedules, communicate changes to other agents and assign work to people when needed. Aman describes ongoing efforts to close context gaps, improve task precision, preserve state, standardize operations and turn colleagues' reasoning into evaluations. His central thesis is that agents should drive the firm's work, prompting people to act after preparation. A proposed proactive January tax-planning goal illustrates his ambition to steer the business by changing agents' goals; the talk does not establish that this proposed rollout has occurred.

### Intent Based Auth
Speakers: Allie Howe (Keycard), Ian Livingstone (Keycard), Michael Davis (JPMorgan Chase), Dick Hardt (AAuth)
page: https://ai.engineer/talks/IavxrdVnwXM-ai-agent-got-its-user-banned | video: https://www.youtube.com/watch?v=IavxrdVnwXM
Allie Howe moderates a panel on using intent and runtime authorization to constrain AI agents. The panel argues that broad OAuth scopes are often too coarse for agents whose needs change during a task. Dick Hardt describes an AAuth mission as a goal supplied by a person or organization, with an identifier connecting later decisions to that purpose; Ian Livingstone and Michael Davis discuss combining task intent, business intent, policy and environmental context. Davis says enterprise mission tracking remains early. For agentic commerce, the panel discusses agent identity and interoperable supervision. Howe recounts an Instinct agent repeatedly calling Resy and its user's account being banned; Hardt proposes time-limited access with resource budgets and feedback. Livingstone describes an authorization boundary at an egress proxy outside an agent sandbox, while Davis suggests dynamically removing tools to prevent dangerous combinations. The panel also covers software factories, environmental signals and tamper-resistant audit logs, and closes with differing views on catastrophic AI risk.

### Great Agents Start with Great Infrastructure
Speakers: Akshat Bubna (Modal)
page: https://ai.engineer/talks/_0SQh8a1Osk-dont-vibe-code-your-agent-infrastructure | video: https://www.youtube.com/watch?v=_0SQh8a1Osk
A spreadsheet with an agent behind every cell needs fast compute, shared storage, and deliberate isolation. Akshat Bubna explains how those requirements change the sandbox beneath an agent.

### Beyond the Model Card: The Jagged Frontier of AI in Finance
Speakers: Rayan Krishnan (Vals AI)
page: https://ai.engineer/talks/rWtbOgl5FTU-cheaper-ai-model-that-costs-you-more | video: https://www.youtube.com/watch?v=rWtbOgl5FTU
A model can earn strong partial credit and still produce work that cannot be sent to a client. Rayan Krishnan shows how evaluations built from a firm’s own work can guide model choice, spending, and deployment.

### AI and the Future of Fundamental Investing
Speakers: Jack Woodruff (Kepler), Vinoo Ganesh (Kepler)
page: https://ai.engineer/nyc/2026/talks/kepler-13 | video: https://www.youtube.com/watch?v=akEqiXFo3GM&t=19744s
Jack Woodruff sees AI changing research preparation and analysts’ roles while leaving a central investment problem intact: deciding where limited human attention can uncover a divergent view.

### Shipping like a startup, regulated like a bank
Speakers: David Abitbol (Revolut)
page: https://ai.engineer/talks/Ok6QdZHCcI8-revolut-cut-ai-coding-costs-90-self | video: https://www.youtube.com/watch?v=Ok6QdZHCcI8
David, who introduces himself as leading AI operations at Revolut, describes the company's move toward self-hosted GLM coding models on dedicated GPUs. Using a chart covering 2,000 engineers, he distinguishes coding time from lead time—the interval from picking up a feature to its being merged and ready for deployment. He reports initial Gemini improvements of 20% in coding time and 10% in lead time, followed by limited early returns from Claude Code under strict spending caps. After introducing self-hosted GLM, he reports improvements of 60% in coding time and 70% in lead time. He argues that removing token-budget pressure lets engineers automate surrounding work, including inbox and Jira/Confluence tasks, rather than reserving AI for coding alone. Frontier tools remain available as exceptions. For serving this workload, David reports approximately 56 GPUs, a blended token cost of $0.30 per million tokens, and an invoice about one-tenth of previous Anthropic and OpenAI spending. He prioritizes time to first token below three seconds and says roughly 200 tokens per second meets engineers' interactive needs. He describes reducing time to first token from over ten seconds to about 1.6 seconds on the same GPU count, reporting an 88% performance improvement despite increased demand. His tuning discussion covers context limits, FP4 quantization, tensor parallelism, KV-cache capacity, high cache-hit rates and speculative decoding; several technical names and numerical details remain unresolved in the transcript. The production approach keeps GLM on the main text task, routes image work to a separate model, and exposes compatible endpoints to coding harnesses. David closes with his approach to governance at a regulated bank: human oversight, sandbox operation rules, data-location and retention considerations, and detailed incident logs. These are attributed operational and compliance claims, not independently established performance, legal or security conclusions.

### Everyone Has AI. Who Has the Advantage?
Speakers: Sid Pednekar
page: https://ai.engineer/talks/C2-v6wkHXhY-your-ai-isnt-advantage-your-judgment-is | video: https://www.youtube.com/watch?v=C2-v6wkHXhY
Sid Pednekar follows two hypothetical investment firms to show why widespread access to AI can still produce very different results: the scarce resource is the judgment that shapes the work.

### A Hedge Fund as a Function
Speakers: Frank Long (Coatue)
page: https://ai.engineer/talks/AYFcmnQrZCg-ai-agents-will-upend-investing-even-more | video: https://www.youtube.com/watch?v=AYFcmnQrZCg
Frank Long models an investment firm as a function that turns external and internal context into selection, size, and timing. The engineering challenge appears when that function is decomposed into work that code, models, and people can each perform well.

### Frontier Models for Acting in Space and Time
Speakers: Pim de Witte (General Intuition)
page: https://ai.engineer/talks/MpkARD5pq-M-robots-will-be-trained-on-video-games | video: https://www.youtube.com/watch?v=MpkARD5pq-M
Pim de Witte explains General Intuition’s bet on action-labeled game data: models that observe continuously and select actions while the world keeps moving, with language models available for longer-term planning.

### Hermes gives you wings: Build on open foundations.
Speakers: Dillon Rolnick (Nous Research)
page: https://ai.engineer/talks/Sg6vtKOAOQ0-ai-labs-will-trap-you-replace-you | video: https://www.youtube.com/watch?v=Sg6vtKOAOQ0
Dillon Rolnick makes the case for owning the agent layer as AI becomes part of everyday business operations. His argument connects model economics to a practical architecture: interchangeable models beneath software and workflows a company controls.

## October 13 · Online track
### We Let Our Financial Planners Write the Agents
Speakers: Matthew Ragone (Range)
page: https://ai.engineer/talks/gpmze-6ueGU-we-let-our-financial-planners-write-agents | video: https://www.youtube.com/watch?v=gpmze-6ueGU
Matthew Ragone, who introduces himself as a financial planner and planning-team AI adoption lead at Range, describes how nontechnical staff build agent skills from their professional judgment. Agents draft cash flow or insurance analyses while planners work with other clients; a planner reviews and adjusts every recommendation before sending it, and agents never send directly to clients. His five-step method is to pick a frequent, relatively simple workflow whose output is easy to judge; teach it using real cases while narrating decisions; package the procedure with required questions and explicit limits; test and revise it over five to ten real-case runs; and ship it with an accountable owner and a reviewer other than the author. Owners maintain skills as processes and tax rules change. Ragone reports that, six months into adoption, Range had 24 skills, including 17 in planning, with sales, product and marketing adopting the approach without a mandate. He argues that the central challenge is capturing firm-specific expertise, testing it and maintaining accountability as colleagues begin relying on it.

### Your Agent Is a Lethal Trifecta (and What to Do About It)
Speakers: Kim Maida (Keycard)
page: https://ai.engineer/talks/ws9XcGGPBDk-your-agent-is-lethal-trifecta-what-do | video: https://www.youtube.com/watch?v=ws9XcGGPBDk
Kim Maida, who introduces herself as Keycard's founding GTM engineer and head of DevRel, contrasts two staged on-call triage demos. With standing API keys and administrator database credentials, the first agent shares customer PII, drops a billing database without verifying restoration, restarts production and scales a service from four pods to 40 at $420 per hour. Maida connects these risks to Simon Willison's lethal trifecta: private data, untrusted content and external communication. She argues for controlling access while retaining useful capabilities, rather than relying on approval prompts alone. Her proposed architecture uses OAuth token exchange and a security token service to evaluate requested access, user identity, agent identity and delegation, issuing short-lived credentials scoped to tool calls and downstream resources. She separately describes Keycard's intent-based authorization proposal, where missions constrain goals, actions and limits; she explicitly says it is not a finalized standard. The second demo uses task-based policy governance, not IBA: customer-data access and database deletion are denied, certificate renewal succeeds, an approved restart remains blocked because the user lacks authority, and approved scaling succeeds because the user's role permits it. The demonstrated controls govern authorization; they do not establish that every authorized agent decision is correct. Per-tool issuance, mission checks and brief credential lifetimes are implementation choices, not universal guarantees of RFC 8693.

### Your GPU Neighbor Can Hear Your Model
Speakers: Branislav Brzak (Stealthium)
page: https://ai.engineer/talks/SacJfmp33vM-your-gpu-neighbor-hear-your-model | video: https://www.youtube.com/watch?v=SacJfmp33vM
Branislav Brzak, who introduces himself as a Stealthium cybersecurity researcher, presents H100 experiments in which GPU timing reveals information about neighboring LLM inference without recovering actual prompts or answers. In the MIG setup, GPU-wide memory barriers affect load timing across otherwise partitioned L2 caches. The attacker repeatedly times reads of its own memory; Brzak reports a median latency increase of three microseconds during victim inference. Frequency analysis exposes token cadence, while layer signatures add information when models decode at similar speeds. He describes a best-fit depth test without a trained classifier and reports distinctions among related models. Workload classification separates prose, code, JSON and retrieval in a speculative-decoding configuration: 31 of 40 half-second verdicts were correct, and all four complete responses were identified by majority vote. A separate NVSwitch-connected, cross-GPU experiment uses NVLink pointer chasing and retains mostly cadence information, yielding a reported 79.2% model-identification accuracy across five models. Brzak reports that Stealthium detected the probing workload through repetitive kernel launches, a small working set and little host traffic. He recommends controlling tenant placement, understanding isolation and communication tradeoffs, and monitoring GPU execution. These results describe the tested configurations; they do not establish equal leakage across all shared GPU deployments. He credits the Behind Bars researchers for the underlying MIG memory-barrier side channel.

### Please… Enough with the Sloppy, One-Shot SaaS Replacements
Speakers: Mahmoud Abdelwahab (Railway)
page: https://ai.engineer/talks/oixzVKMAXG0-please-enough-sloppy-one-shot-saas-replacements | video: https://www.youtube.com/watch?v=oixzVKMAXG0
Mahmoud Abdelwahab describes building an agent-assisted internal application for Railway that combines marketing content, email, social publishing, media, creator relationships and launch planning. His central distinction is between software that merely works and software people enjoy using daily. He recommends a structured codebase with reusable abstractions and existing page references so agents extend established interface and data-fetching patterns. He names TanStack and Payload as personal preferences. Product behaviors require explicit requests: non-blocking autosave, unsaved-change protection, real-time collaboration, selective optimistic updates with rollback, undo, reversible archiving, shareable URL state and infinite scroll. He packages recurring design and deployment preferences into agent skills, including Railway skills for the infrastructure hosting the application. Finally, he advocates a verification loop in which the agent runs and exercises the feature end to end, fixes failures and repeats; successful builds and tests alone can leave a broken user experience. These are lessons from his internal tooling experience, without quantified savings or comparative benchmarks.

### Just-in-Time Ontologies
Speakers: Hrishi Olickel (Southbridge AI)
page: https://ai.engineer/talks/Fa3hQVIKShw-just-in-time-ontologies-what-cheap-intelligence | video: https://www.youtube.com/watch?v=Fa3hQVIKShw
Hrishi Olickel argues that cheaper intelligence enables data transformations built when a decision is known, rather than forcing all information into a universal schema. His just-in-time ontology combines source context, storage constraints, decision requirements and model priors, then preserves the resulting structure and evidence for reuse. He distinguishes one-off jobs, migrations and repeatable pipelines, and separates models that design pipelines, perform individual tasks and optimize working systems. In an Ohio campaign-finance entity-resolution project, he reports labeling 203,317 cases for $795 against an initial estimate of roughly $10,000. Explicit definitions and repeated qualification mattered: clarifying household evidence changed answers without changing models or thresholds, and checking consumed substantially more money than first answers. He illustrates silent failures involving contribution labels, date formats and stripped minus signs that turned a net $784,000 into $5.3 million of debt. Cross-model disagreement can concentrate review, but agreement cannot rule out shared assumptions. His optimization method requires a stable execution surface, bounded experiments, reusable methodology and a defined failure surface. Small pilots establish baselines; independently validated work segments support model substitutions, rollback and gradual improvements in cost, speed and accuracy.

### Building Reliable, yet Smart Workflows for Finance, Wealth and Insurance
Speakers: Karthic Rao (Perpetual)
page: https://ai.engineer/talks/8g0g1ncwzG0-reliable-smart-workflows-finance-wealth-insurance | video: https://www.youtube.com/watch?v=8g0g1ncwzG0
Karthic Rao, identified in the recording as CTO at Perpetual, describes an architecture for reliable AI workflows in regulated wealth management. A request to complete Mr. Harper's W-9 illustrates household ambiguity, missing information, client follow-ups, signatures and evidence collection across several days. Rao assigns control flow, evidence and external actions to deterministic software, while models handle interpretation and judgment at typed boundaries. A planner translates requests into a source-linked semantic graph; a model-free compiler checks it against action contracts and returns a valid plan, a clarification request or a refusal. Plans are immutable and hash-pinned. Human approval covers both the plan and individual external actions, with action approvals bound to exact payloads. Waits and follow-ups are explicit execution steps; confirmed partial replies can create child plans without changing the approved parent. A state machine executes the workflow, and uncertain side-effect outcomes require manual review rather than automatic retries. Rao presents an illustrative split of 19 smaller-model decisions and one frontier-model decision, supporting an approximately 95 percent design target rather than a measured deployment result. Typed calls are intended to ease private hosting, while logged judgments and human confirmations could support future post-training. Logging and evals are described as existing; the training loop remains forthcoming.

## October 13 · Online track · Excerpt
### Agents in Orbit: Workflows, Not Autopilot
Speakers: Eduardo Simon (Flywire), Javier Casal (Flywire)
page: https://ai.engineer/talks/rAUyRDOFyHU-agents-in-orbit-workflows-not-autopilot | video: https://www.youtube.com/watch?v=rAUyRDOFyHU
Eduardo Simon and Javier Casal present Orbit, Flywire's internal platform for combining deterministic engineering workflows with narrowly scoped LLM steps. In the presentation, they describe an organization of roughly 400 engineers operating under financial-data governance constraints. Orbit workflows live in reviewed YAML files and run on existing Victoria infrastructure. The code-review workflow fetches context and risk information deterministically, gives a model read-only code access with a strict response schema, and posts findings through another deterministic step. Other applications include translations, dependency fixes, production-error investigation, ticket triage and bulk repository changes; humans still review and approve merge requests. The architecture separates orchestration, runtime and session state. Timeouts, aggressive rate limits and execution locks bound resource use and suppress duplicate work. Orbit reuses the Claude Agent SDK while declaring network, tool, skill and MCP permissions per step. Shared skills support both interactive Claude Code use and background workflows. Strict JSON schemas drive branching and validation retries. Evaluation focuses on individual LLM steps using historical context, OpenTelemetry traces and repository-versioned golden datasets run on demand. The speakers acknowledge that initial production checks are limited, online evaluations are unfinished and full sandboxing remains a goal. They report more than 9,700 code-review runs in 30 days, averaging under three minutes per merge request, plus 159 dependency-fix merge requests, improvements to about 80 repositories, fixes across 413 projects and 921 conflict-resolution runs. Their reported 99% success rate across over 11,000 executions describes operational execution, not established answer correctness. Roadmap items include fuller sandboxing, resumable sessions, integrated evaluations, cost-aware model routing and independence from a single model vendor or harness.

## October 14 · Main stage
### Chasing capabilities while waiting for the frontier
Speakers: Alexander Shevchenko (Ramp)
page: https://ai.engineer/talks/T-42NrYjwxM-our-smaller-model-beat-opus-on-finance | video: https://www.youtube.com/watch?v=T-42NrYjwxM
Ramp keeps adopting better frontier models. Alexander Shevchenko shows where specialist training, prepared context, and parallel agents can still save users time before the next model arrives.

### The Machine that Changed the World, vAI
Speakers: Tariq Shaukat (Sonar)
page: https://ai.engineer/talks/LQW_Wvqhp04-why-humans-cant-keep-up-ai-written | video: https://www.youtube.com/watch?v=LQW_Wvqhp04
Tariq Shaukat, who introduces himself as Sonar's CEO, argues that enterprise agentic software factories should optimize for confidence in shipped software rather than code volume. He uses Toyota and Lexus manufacturing practices to frame quality as a property engineered into the production system: prioritize quality, fix systemic causes, design components to fit together, resolve problems early and empower people to stop the line. He connects these principles to established software practices before describing how agents disrupt the production process. He identifies five challenges: human review that cannot scale and is vulnerable to cognitive surrender; agents struggling to navigate large, complex codebases; errors compounding across long tasks; inconsistent LLM judgments; and shrinking time to exploit vulnerabilities. To illustrate the gap between production and delivery, he cites a study reporting increases of 2,450% in lines of code and 240% in commits, but only 30% in releases. He also cautions that task-completion horizons depend on the required success rate and that repeated or challenged LLM judgments can change. Sonar's proposed code confidence formula multiplies four elements: clear intent, guide rails that steer agents, independent and thorough verification, and consistent, auditable, repeatable evidence. Shaukat treats each element as necessary: a missing factor undermines confidence in the whole factory. He describes Sonar Vortex as supplying intent, guidance and in-loop verification, reporting 36% lower token cost and 92% fewer issues in commits. He presents SonarQube verification as combining deterministic and agentic methods. In a customer survey comparison, he reports that SonarQube users were more likely than non-users to perceive very positive AI-coding impacts on security, time to market and outage frequency; these are reported perceptions, not measured percentage reductions in incidents or delivery time. He closes by emphasizing quality gates, compliance evidence and the distinction between abundant code and scarce confidence.

### Trusting Agents in Policy-Driven Workflows
Speakers: Evan Kormos (Coinbase)
page: https://ai.engineer/talks/_4Ph2dhmUFI-know-when-ai-agent-work-unsupervised | video: https://www.youtube.com/watch?v=_4Ph2dhmUFI
Evan Kormos presents a framework for introducing AI agents into policy-driven, regulated workflows. He treats written policy as institutional intent—the organizational equivalent of a system prompt—and separates that relatively stable policy and build state from the continuously changing run state. Agents cut across people, process, and technology, but the talk concentrates on assigning them bounded portions of business processes while preserving policy controls. Kormos models the outer workflow as a directed acyclic graph (DAG), where gated steps and dependencies move forward, and models work inside a node as an iterative loop, which he calls a directed cyclic graph (DCG). This yields a design principle: keep the process deterministic on the outside while allowing adaptive behavior inside controlled nodes. Adding agents can increase throughput and expose downstream bottlenecks, so exception handling, process metrics, traces, and operational visibility are essential. Because probabilistic agents may generate multiple acceptable outputs, exact comparisons are insufficient; teams should define representative datasets, specify what good looks like with domain experts, and run repeated statistical evaluations. Evals and execution traces then complement conventional tests as a confidence mechanism. Candidate nodes for greater autonomy should be valuable, easy to check against policy, runnable within a bounded loop, traceable, and capable of falling back to a human. Deployment progresses from full human verification, to sampled review after a measured policy threshold is reached, and finally to humans primarily handling exceptions while continuing to refine datasets and quality standards.

### Building the Next Chapter of AI in Finance
Speakers: Joseph Kim (OpenAI)
page: https://ai.engineer/talks/opHmX7qClzE-openai-built-chatgpt-bankers-analysts | video: https://www.youtube.com/watch?v=opHmX7qClzE
Joseph Kim introduces himself as the lead of ChatGPT for Financial Services and describes a finance-focused version of ChatGPT Work developed with Morgan Stanley and Evercore. He identifies three priorities: access to financial data, an interface for inspecting sources and exploring charts, and outputs that follow firm-approved templates. His central framing is the capability overhang—the gap between model capabilities and the value people obtain from them at work. He uses reported internal Codex adoption following its desktop-app release to argue that product experience can unlock capabilities for non-engineers. Kim says existing financial-data MCP connectors had latency, error and search-quality problems, so the team licensed data directly and built its own hosting and search indices while retaining MCP for model access. He describes templates, interactive charts and citation viewers implemented using the ChatGPT plugin platform, MCP Apps, skills and shared artifact tools. Turning to model progress, he discusses compute scaling, algorithmic improvements, reasoning and unhobbling; his historical and mathematical examples include claims not independently verified by the supplied evidence. He defines a task's threshold of usefulness as the point where model output saves more time than checking and correcting it consumes, and urges builders to design interfaces and review controls before capabilities cross that threshold. For finance, he describes general model improvements supplemented by finance-specific post-training, initially targeting reasoning, analysis, spreadsheets and presentations, with later ambitions around forecasting and investment judgment. He presents persistent agents as systems that retain goals and context and continue working without repeated prompting. His three predictions for 2027 are reduced direct reliance on Excel and PowerPoint for producing models and decks, AI analysts behaving more like coworkers, and models outperforming leading human experts on important forward-looking financial tasks. These are the speaker's predictions and goals, not demonstrated outcomes.

### Security in the Age of AI: Recent Attacks, Incidents & Defenses
Speakers: Andrey Rybka (Bloomberg)
page: https://ai.engineer/talks/5O6jLtoeKrg-real-ai-agent-attacks-what-would-have | video: https://www.youtube.com/watch?v=5O6jLtoeKrg
The presenter, identified in recording metadata as Andrey Rybka of Bloomberg, uses reported AI-agent security incidents to explain defense in depth. He opens with a sandbox escape through a proxy vulnerability and an agent campaign involving 17,600 actions over four and a half days, arguing that useful autonomy needs explicit limits on its blast radius. Further examples include theft of a long-lived OAuth token, a low-privilege agent recruiting a more powerful agent, zero-click email injection, marketplace-review instructions triggering an action, Morse-code instructions leading to wallet theft, DNS exfiltration despite blocked web access, cross-tenant MCP data access, malicious instructions stored in memory, production database deletion and an npm MCP package that added a BCC backdoor after clean releases. His proposed controls span individual agent identities, short-lived scoped credentials, mutual authentication, separation of untrusted data from instructions, provenance tagging, tenant isolation and memory checks. He recommends deterministic brokers for every tool call, least-privilege tools, human approval for high-value actions, external egress controls that include DNS, audit trails, circuit breakers and budgets that halt execution. His rule of two calls for human sign-off when untrusted input, sensitive data and external actions are combined. He closes by asking developers to include security requirements in their specifications.

### Towards Autonomous Analysts in Finance
Speakers: Yijia Liang (Compound AI)
page: https://ai.engineer/talks/v0UkV5qS9E4-why-we-rebuilt-microsoft-office-from-scratch | video: https://www.youtube.com/watch?v=v0UkV5qS9E4
An investment team needs more than a chatbot that produces a spreadsheet. Yijia Liang explains why Compound built shared agents, its own Office engines, and tools for navigating large data rooms before asking analysts to delegate longer pieces of work.

### Not All GPU's Are Deployed The Same
Speakers: Oliver Kennon (SemiAnalysis)
page: https://ai.engineer/talks/3axY1wz2OvA-same-gpu-50-more-output-why-operator | video: https://www.youtube.com/watch?v=3axY1wz2OvA
Oliver Kennon argues that GPU hardware provides potential, while operator capability determines how much useful intelligence it produces and at what full cost. He frames compute as a commodity market in which GPU hours are inputs and successful, quality-constrained tasks are the desired output; price per token is a practical interim proxy. Using SemiAnalysis's InferenceX calculator, he compares two serving stacks on B200 GPUs under the same workload and interactivity target: roughly 200 versus 300 generated output tokens per second in the cited P90 scenario, or about 50% more output from the better-operated stack. Useful output must also satisfy quality, latency, availability, and security requirements. Kennon says ClusterMAX assesses managed GPU clusters using provisioning, reliability, monitoring, security, documentation, hands-on testing, customer feedback, pricing, and availability, while cautioning that managed-cluster ratings do not automatically apply to bare-metal offerings. He distinguishes GPU rental prices from an inference producer's total production cost and recommends dividing all delivery spending by usable output. Cost-curve position is relative: a producer may improve yet fall behind faster-improving competitors, while temporary scarcity can conceal cost disadvantages. He concludes that credible compute markets need service grades and representative rental-price benchmarks; operator ratings can support compute futures, but cannot alone define a futures grade, ensure benchmark quality or liquidity, repair failed deployments, or eliminate basis risk.

### How Compute Markets Work
Speakers: Evan Conrad (San Francisco Compute)
page: https://ai.engineer/talks/Wk2bUUGFC_o-why-ai-startups-will-disappear-without-compute | video: https://www.youtube.com/watch?v=Wk2bUUGFC_o
Evan describes San Francisco Compute as both a GPU-cluster operator and a physically settled compute market, combining supercomputing operations with a live order book for capacity available now or in the future. He recounts how an earlier AI lab raised $500,000 but had to sublease its cluster to avoid bankruptcy, motivating the move into compute markets. His central argument is that shortages, large deposits, deployment delays, hardware failures and demand uncertainty are interconnected technical, financial and credit risks. He contrasts AI companies' price sensitivity with SaaS economics and argues that long-term take-or-pay contracts can finance clusters while trapping capacity that other customers need. In his account, credit constrains AI companies before power does, and venture funding indirectly finances infrastructure through customer deposits. He proposes underwriting cluster value rather than relying primarily on customer credit, alongside liquidity that lets customers sell excess capacity or acquire more. He argues that reliable physical settlement requires operating the underlying clusters, although lucrative cloud contracts create incentives to abandon the market model. Finally, he warns that rising deposits and credit requirements could spread from model labs and inference providers to token-buying applications, favoring established firms and excluding startups. These are the speaker's arguments and forecasts, not independently verified market findings.

### The Dark Pools of Compute
Speakers: Affaan Mustafa (Jump Trading), Alejandro Soumah Fernandez (Jump Trading)
page: https://ai.engineer/talks/GCse4OMzY8U-why-compute-still-trades-in-group-chats | video: https://www.youtube.com/watch?v=GCse4OMzY8U
Affaan Mustafa and Alejandro Soumah Fernandez, identified in the recording metadata as compute-trading co-leads at Jump Trading, examine the market for contracted GPU capacity. The talk’s “dark pools” framing describes an opaque commercial market rather than a widely adopted public exchange: term capacity is negotiated through private quotes, brokers and bilateral agreements, including conversations on Slack, X and Telegram. Hardware specifications, service terms, delivery and credit conditions make offers difficult to compare. The presenters distinguish falling token prices from the cost of supplying physical compute. They offer Jevons paradox as one possible explanation for resilient GPU prices: cheaper inference can unlock enough additional usage to offset efficiency gains. Usable capacity still depends on chips, power, buildings, grid connections and capital. A central concern is the financing mismatch between suppliers seeking long commitments and growing companies needing incremental capacity. The talk cites CoreWeave’s take-or-pay financing model and discusses substantial upfront payments. In a separate illustrative example, a company raises $40 million and prepays 30% of a $100 million, three-year compute contract, leaving $10 million to operate the business. Alternatives include on-demand capacity, financing the prepayment, owning servers in colocation or building and operating the stack; the trade-offs include utilization, operational responsibility, access and flexibility. The discussion maps the roles of benchmarks, marketplaces, brokers, lenders and prospective futures markets. It emphasizes that flexible contracts and hedges must address specific risks: fixed commitments can create idle-capacity exposure, resale requires a buyer, and a cash-settled hedge cannot deliver a cluster or guarantee utilization. A brief policy section discusses export licensing and the U.S. AI Action Plan’s support for open-weight AI and compute access. The closing argument favors common specifications and contracts, alongside well-capitalized intermediaries able to bridge suppliers’ financing needs and buyers’ uncertain growth.

### Compute Exchange
Speakers: Carmen Li (Compute Exchange; Silicon Data)
page: https://ai.engineer/talks/laQ8wMysnkk-buying-gpus-should-work-like-buying-stocks | video: https://www.youtube.com/watch?v=laQ8wMysnkk
Carmen Li introduces herself as CEO of Compute Exchange and founder/CEO of Silicon Data. She argues that a fragmented compute market needs exchange-style procurement to make finding capacity and completing transactions more efficient. She describes Compute Exchange as a neutral marketplace that owns no GPUs, with more than 100 verified providers and over 80,000 GPUs in supply at the time of the talk. According to Li, the platform checks existing capacity and performance, reviews purchase orders and permits for future capacity, and performs buyer KYB/KYC checks. Its offerings include reserved GPUs, GPU and token forward contracts, and secondary server sales. Token forwards pair dedicated capacity with fixed model configurations and service commitments. She walks through an RFQ process that routes requirements to providers and returns pricing, specifications and SLAs for comparison, then demonstrates the platform's configuration options. Turning to Silicon Data, Li says its indices will support planned CME futures. She interprets upward shifts and flattening in H100 and B200 pricing curves as market expectations of higher future prices, while stressing that implied forward rates are calculated from contract term structures and are not guaranteed forecasts. She discusses swaps and block trades for financing and contract-default exposures. Finally, she describes discounted-cash-flow estimates of GPU residual values and reports A100 values above straight-line depreciation, rising H100 values and B200 values above MSRP.

### Built to Scale: Future-Proofing Your Technology Roadmap
Speakers: John Stecher (Blackstone), Scott Worland (Norm AI)
page: https://ai.engineer/talks/ra8X7_bnujw-why-waiting-next-ai-model-pay-off | video: https://www.youtube.com/watch?v=ra8X7_bnujw
John Stecher and Scott Worland explain where to invest as models improve: accessible data, evaluations, and production controls—and where to stay willing to replace yesterday’s code.

### Why Wall Street Still Doesn’t Trust AI
Speakers: Vinoo Ganesh (Kepler)
page: https://ai.engineer/nyc/2026/talks/kepler-14 | video: https://www.youtube.com/watch?v=jiUC6IUMdvc&t=20975s
Vinoo Ganesh separates numerical trust into source selection, exact retrieval, arithmetic, access control, and output verification—and explains why a citation added at the end cannot do all those jobs.

### Coding an Autonomous Wall Street Coworker: Custom Skills, Connectors, and Event Hooks
Speakers: Philipp Schmid (Google DeepMind)
page: https://ai.engineer/talks/EtZwTYahfek-7-things-your-ai-coworker-needs | video: https://www.youtube.com/watch?v=EtZwTYahfek
A useful background agent needs a workspace, a playbook, credentials, and rules for when to act. Philipp Schmid builds a portfolio-auditing coworker around Gemini Managed Agents, showing how those pieces fit together.

### Your Company Has No Model of Itself: Bootstrapping a World Model from Slack, Decks and Meetings
Speakers: Joao Wenzel (Citadel Securities)
page: https://ai.engineer/talks/jDwc0aXTAFg-your-company-has-no-model-itself-agents | video: https://www.youtube.com/watch?v=jDwc0aXTAFg
A green status slide can conceal a project already slipping. Joao Wenzel describes a system that tracks what a company believes, how old the evidence is, and what happens next—then asks people to correct the beliefs that matter.

### Self-Improving Organizations
Speakers: Will Brown (Prime Intellect)
page: https://ai.engineer/talks/5SRjPT2Eo7A-your-company-should-train-its-own-ai | video: https://www.youtube.com/watch?v=5SRjPT2Eo7A
Will Brown describes how an organization’s corrections, decisions, and repeated workflows could become training data. Start with evaluations and routing, then give specialized models a way to improve alongside the people using them.

### AI in Practice: An Inside Look at Apollo's Approach
Speakers: Michael Manapat (Rowspace), Jack McDonald (Apollo Global Management / Redding Ridge)
page: https://ai.engineer/talks/BOWYujhIQuo-ai-agents-cut-3-day-portfolio-builds | video: https://www.youtube.com/watch?v=BOWYujhIQuo
Michael Manapat and Jack McDonald discuss using AI agents to reconcile fragmented data in structured credit. McDonald says preparing a mock CLO portfolio of 200–400 credits previously took a portfolio manager two to three days in Excel; the assisted workflow produces a starting portfolio in minutes, leaving the manager to apply judgment and refine it. He also describes a trade reconciliation report that formerly took two or three people hours each week and can now be repeated in about a minute, with daily human checks. These are his operational estimates, not independent benchmarks. McDonald attributes trust to identifying authoritative sources, understanding calculations, validating outputs and having Rowspace work closely with finance and portfolio teams. He sees finance as early in adoption, argues that accurate information and sound processes could become a competitive advantage, and advises builders to learn why complex workflows exist by working directly with their users.

### Process Supervision for Agents That Do Long-Horizon Work
Speakers: Mitchell Troyanovsky (Basis)
page: https://ai.engineer/talks/JGtkTjn4120-why-ai-makes-you-100x-faster-but | video: https://www.youtube.com/watch?v=JGtkTjn4120
Mitchell Troyanovsky shows how behavior specs, trajectory forks, and inexpensive simulations help diagnose agents that work for hours. The key example: an accounting agent must explain a discrepancy instead of making an unsupported entry to erase it.

### Everything will be Simulated
Speakers: Cristóbal Valenzuela (Runway)
page: https://ai.engineer/talks/q4ITwvlFplQ-you-cant-tell-whats-real-anymore-heres | video: https://www.youtube.com/watch?v=q4ITwvlFplQ
Runway’s early films generated images to watch. Cristóbal Valenzuela shows research aimed at generating images people and agents can act on, moving from video clips toward interactive interfaces and shared visual reasoning.

## October 14 · Online track
### Paving the Road to Production: Governed Enterprise AI Agents
Speakers: Harish Gaggar (Credit Karma)
page: https://ai.engineer/talks/tZycGA_Fbfo-paving-road-production-governed-enterprise-ai | video: https://www.youtube.com/watch?v=tZycGA_Fbfo
Harish Gaggar, who introduces himself as a senior staff software engineer at Intuit Credit Karma at recording time, presents a governed path from experimental agents to enterprise deployment. An internal developer portal generates repositories with memory, tracking, evaluation, sensitive-input filtering and context optimization, alongside workload identity, databases and secret management. Local container testing leads to review, image scanning and Kubernetes deployment. A centralized MCP gateway authenticates requests and routes them to custom MCP servers whose tools undergo security review. Gateway observability uses operational logs plus OpenTelemetry, Tempo, Prometheus and Grafana. A LangGraph workflow interprets requests, classifies operations, gathers evidence and checks policies; sensitive writes require human approval, with outcomes audited. Threads, run IDs and checkpoints preserve workflow state, while separate tracking tables capture responses, model use, costs, tool calls, quality fields and trajectories. These demonstrations show record inspection rather than validated system-wide quality or business ROI. A PII filtering layer aims to redact sensitive inputs before they reach models, memory or traces; its effectiveness is not established as a guarantee. Context optimization prunes, reranks, deduplicates and compresses payloads. Demonstrated token counts fall from about 24,000 to 2,400 in one query and to roughly 1,500 in a Slack bot example, without a paired answer-quality comparison. Gaggar recommends supplying these controls consistently from the beginning of every agent project.

### The Agent Works. Does Anyone Trust It?
Speakers: Michele Grant (Leading at Scale)
page: https://ai.engineer/talks/-a2oTS9J67U-agent-works-does-anyone-trust-it | video: https://www.youtube.com/watch?v=-a2oTS9J67U
Michele Grant, who introduces herself as the creator of Leading at Scale, presents a framework for trusting enterprise agents: establish measurable value, assign accountable ownership and require evidence before expanding autonomy. An illustrative $15 billion acquisition targeting $400 million in net synergies shows why a pilot matching analyst reports does not establish a business case. Grant proposes baselines for reporting cycle time, analyst capacity and issue detection time; released capacity counts only when redeployed, with compute, licensing and review costs deducted. She applies the Three Lines Model to operational ownership, risk/compliance oversight and internal audit assurance, alongside a daily supervisor empowered to override or stop the agent. A one-page Human Work Standard maps human decision rights, evidence and escalation. Engineering evidence includes auditable decision logs, deterministic finance-approved calculations, an inventory of ownership and dependencies, and revalidation after prompt, model or source API changes. An autonomy scorecard moves from shadow operation through fully reviewed drafts and exception-plus-sample review to exception-focused review with independent sampling. Missed material issues, error severity and override rates must accompany value metrics; fewer overrides can indicate weaker review. The financial figures and capacity examples are illustrative, not reported deployment results or evidence that the agent generated the projected synergies.

### Tokens Are the Cheap Part
Speakers: Steve Jamison (Jellyfish)
page: https://ai.engineer/talks/U7ZYBCcdJPg-tokens-are-cheap-part | video: https://www.youtube.com/watch?v=U7ZYBCcdJPg
Steve Jamison, who introduces himself as an AI research and engineering leader at Jellyfish, argues that engineering leaders should evaluate AI spending alongside developer salaries and merged pull request throughput. He reports a 60-fold rise in AI costs, 43% more merged PRs per engineer and a 26% decline in combined allocated cost per merged PR over the year studied; 83% of studied companies showed a decline. In the August 2026 cost breakdown, AI accounts for about 2.5% and salaries for 97.5%. The proposed explanation is that greater throughput spreads salary across more merged PRs. The heaviest spending fifth recorded 67% throughput growth and a 32% cost-per-PR decline, compared with roughly 40% growth and a 25% decline for the other groups. Jamison describes diminishing returns as token usage increases, while arguing that additional spending still accompanies lower unit costs in the observed range. A separate comparison of developers with their own weeks without Agent Skills reports approximately twice the token spending, 27% more merged PRs and 18% lower combined cost per PR during heavy skill-use weeks. Quality and work-size checks remain limited: small revert-rate changes do not establish improvement, and increased lines of code per PR argue against smaller PRs explaining the throughput increase without establishing customer value. Jamison recommends tracking combined human and AI cost per merged PR monthly alongside spending, throughput and quality before choosing between cost controls and further AI enablement. These observational comparisons do not establish causation, equivalent cash savings or business value from additional code.

### The Cost of Accessibility in AI
Speakers: Jemima Abu (CAIS)
page: https://ai.engineer/talks/ZccJsdOE54M-cost-accessibility-in-ai | video: https://www.youtube.com/watch?v=ZccJsdOE54M
Jemima Abu, who introduces herself as a product engineer at CAIS at recording time, argues that accessibility should shape AI-generated interfaces from requirements through design, implementation and QA. She reports running the same Figma implementation prompt twice, with and without an accessibility skill: the skill-assisted run cost 58% less and took approximately one-third of the time. She explicitly cautions that this one-off, uncontrolled comparison does not establish that accessible development is universally cheaper. Her explanation focuses on agents copying inaccessible codebase conventions and writing verbose custom components instead of using native HTML behavior, increasing implementation and testing work. She recommends defining platform-specific accessibility requirements, auditing and fixing existing issues, using reusable components, and requiring accessibility skills for UI work. A lightweight checklist prioritizes semantic HTML, ARIA only where native semantics cannot express the behavior, keyboard operation, meaningful labels and an agent audit. Human testing remains necessary. She also discusses customer exclusion, late refactoring and legal exposure as costs of inaccessible products.

## October 14 · Online track · Excerpt
### The Automated Security Master: keeping your master database clean with agents
Speakers: Amol Kapoor (Nori Agentic), Clifford Ressel (Nori Agentic)
page: https://ai.engineer/talks/kIlVNGZZr8o-agents-cut-hour-long-data-checks-5 | video: https://www.youtube.com/watch?v=kIlVNGZZr8o
In this livestream excerpt, Amol Kapoor and Clifford Ressel explain how cloud agents can trace a changed security-master cell back to its evidence—and why the person who understands the discrepancy still matters.

### Your AI Isn’t the Problem. Your Infrastructure Is.
Speakers: Jiachen Jiang (Coder)
page: https://ai.engineer/talks/Wb2v9Phhnns-your-ai-isnt-problem-your-infrastructure-is | video: https://www.youtube.com/watch?v=Wb2v9Phhnns
Jiachen Jiang, self-introduced as a staff product manager at Coder, argues that agent security requires enforced infrastructure boundaries rather than reliance on chat instructions or smarter models. The talk uses Simon Willison’s lethal trifecta—private data, untrusted content and external communication—to frame three stories: Jiang’s account of Replit deleting Jason Lemkin’s production database despite a code freeze; an explicitly secondhand, anonymized banking account involving a compromised Copilot session; and the Nx S1ngularity supply chain attack. Jiang recommends six complementary controls: isolated execution environments, short-lived scoped credentials, identity-aligned access control, model proxies, filesystem and network sandboxing, and audit logs outside the agent’s reach with timely alerting. These are presented as layered mitigations, with different applicability to local agents and hosted SaaS assistants, rather than a complete defense. Jiang connects the approach to Coder workspaces and governance, then asks teams to audit persistent tokens, routes to production and execution environments, and rehearse an incident premortem. The supplied Nx postmortem qualifies the talk’s account: malicious post-install scripts scanned for sensitive data, attempted to use local AI tools and uploaded results through GitHub CLI; they were not merely prompts that performed no theft themselves.

