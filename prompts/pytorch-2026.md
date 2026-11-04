>>> HOW TO RUN THIS <<<
This is the digest prompt for pytorch-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/pytorch-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/pytorch-2026.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

Below is the program for PyTorch Conference 2026. Read it and produce a digest
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
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
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
{"post": ["bgp", "optics"], "talks": {"<pick heading>": ["bgp", "network-security"], "<pick heading>": ["kubernetes", "cni"]}}
```

- "post": 3-6 topics this digest as a whole covers.
- "talks": one entry for EVERY pick you selected, keyed by its exact `###`
  heading string (copy it character for character, including any presenter
  part), with 2-4 tags naming what the talk is about - the technology or
  practice, not its tier or the conference.
- Tags are lowercase, hyphenated, single concepts. Use ONLY tags from this
  vocabulary:

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
- `kubernetes` - Kubernetes and its networking
- `cni` - container network interfaces and container networking plugins
- `containers` - containerization, images, runtimes
- `service-mesh` - service mesh (sidecars, eBPF meshes, mTLS between services)
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
conference: PyTorch Conference 2026
source_url: https://sessionize.com/api/v2/s2rq62nk/view/markdown
generated: 2026-11-04
registry_key: pytorch-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / Identity PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

### Keynote: Accelerating Open Intelligence Together
Speakers: Mark Collier
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298042
AI innovation no longer happens one layer at a time. Research breakthroughs shape models, new models push frameworks and infrastructure forward, hardware advances unlock new capabilities, and what happens in production feeds back into what gets built next. PyTorch sits at the center of this increasingly interconnected ecosystem, bringing together the researchers, maintainers, developers, infrastructure providers, hardware companies, and enterprises advancing AI in the open. Because those advances are shared, progress in one part of the ecosystem creates opportunities everywhere else. Day 1 shows what that looks like in practice, from continuous learning and new approaches to systems programming to distributed infrastructure, hardware integration, AI accelerator enablement, and production-scale inference. The result is an open ecosystem where innovation compounds and the entire community can move faster together.

### Keynote: Shopify's Continual Learning Loop with PyTorch and vLLM
Speakers: Cody Mazza-Anthony
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298072
The flywheel turns Shopify's product expertise into robust evaluations, then mines, critiques, and repairs low-scoring conversations to train better models. Using Buyer Profile as a case study, we show how small models can outperform frontier models on well-scoped tasks at a fraction of the cost, with lower latency and higher throughput.

### Keynote: MAX and Mojo: The Best Way to Extend PyTorch
Speakers: Chris Lattner
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298067
PyTorch is where the industry builds models. Chris Lattner shows what happens when you extend that foundation with MAX and Mojo.

Mojo is a systems programming language in the Python family. MAX adds model authoring plus a graph compiler that targets hardware from multiple vendors, so a kernel you write once runs across them instead of being rewritten per backend. Together, they give PyTorch developers an entrypoint into systems programming and performance optimization, so they can get more out of the hardware they already have.

### Keynote: Ray's Evolution to Support AI Workloads
Speakers: Ion Stoica
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298071
In this talk, Ion will briefly trace Ray’s full-circle journey from supporting reinforcement learning (RL) in its early days to becoming the most widely used orchestrator for today’s RL frameworks. Ion will also highlight some of the key features added to Ray to support increasingly complex, large-scale AI workloads and touch on what comes next.

### Keynote: Trainium’s Journey to Native PyTorch
Speakers: Robert Hundt
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298065
PyTorch now runs natively on Trainium with no code changes required. AWS customers are already training frontier models using standard PyTorch workflows on Trainium. In this keynote, we share how we got here: enabling eager mode and torch.compile, integrating with TorchTitan, TorchAO, and HuggingFace Transformers v5, and making our tools like Neuron Explorer work natively with PyTorch. We'll cover our upstream contributions to PyTorch and TorchTitan, and our ongoing collaboration with the PyTorch team on what comes next.

### Keynote: Beyond Brute Force: The Era of Adaptive Intelligence.
Speakers: Sara Hooker
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298060
The next generation of truly intelligent systems won't be defined by scale. The next unlock is architectural: systems that keep learning after deployment, closing the gap between a model's frozen training distribution and the evolving world it operates in.

In this talk, Sara Hooker, Co-founder of Adaption, discusses moving past static AI toward systems that are malleable by design. She'll dig into the technical foundations of continual, gradient-free learning: how models can update behavior without full retraining, without catastrophic forgetting, and without the compute cost of repeated fine-tuning cycles. Built so that AI adapts to people rather than the reverse.

### Keynote: PyTorch at Meta - From Internal Workloads to Multi-Silicon Ecosystem
Speakers: Jana van Greunen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1301820
Jana van Greunen shares how Meta uses PyTorch to power its frontier AI research and production workloads — and how that work feeds back into the open-source ecosystem. She'll cover Meta's latest PyTorch initiatives, including Helion (the kernel layer) and TorchTitan's expansion into reinforcement learning, as well as Meta's deepening collaboration with hardware partners to bring PyTorch-native support to the next generation of AI chips.

### Keynote: vLLM Update: Scaling Open Frontier Inference Infrastructure
Speakers: Simon Mo
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298061
As LLMs grow in size, context length, and architectural complexity, vLLM must evolve to meet new performance and scalability challenges. This talk presents key improvements in vLLM's core architecture and highlights major optimizations in KV cache management and GPU kernels.

### Keynote: PyTorch Performance for Agents on Vera Rubin
Speakers: Ujval Kapasi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298063
In this keynote, Ujval will explore what agentic workloads need from AI systems and how the PyTorch stack can address these needs.

Agentic systems introduce new bottlenecks and optimization opportunities. A single request can trigger long chains of reasoning, tool calls, code execution, data movement, and distributed inference.  Training and inference serving software needs to be optimized across CPUs, GPUs, memory, and networking. Using Vera Rubin as a case study, he will show how co-design across hardware and software can improve end-to-end performance, efficiency, and developer experience for agents at scale.

### Contributing to PyTorch with AI agents
Speakers: Edward Yang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1252250
How should AI agents be used productively to contribute to PyTorch? What are good things to know? How can you get someone to review your PR? Come talk about these things. A good pre-read is this devlog: https://docs.pytorch.org/devlogs/ai-agents/2026-05-30-ai-coding-playbook/

### Meet the Developers of PyTorch
Speakers: Alban Desmaison, Natalia Gimelshein, Edward Yang, Driss Guessous, Jane Xu, Will Constable, Tristan Rice
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1364540
Join PyTorch experts for an interactive “Meet the Developers” session – a chance to learn in a small group setting and ask your most pressing questions. No sign-up required – just drop in and get real answers from the people building the tools.

### Meet the Developers of Safetensor
Speakers: Luc Georges
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1340758
Join PyTorch experts for an interactive “Meet the Developers” session – a chance to learn in a small group setting and ask your most pressing questions. No sign-up required – just drop in and get real answers from the people building the tools.

### Demo Theater: Unifying Open-Source LLM Serving on Google Cloud TPUs with TorchTPU
Speakers: Rob Mulla
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1304122
See how TorchTPU provides a native, high-performance compilation path for PyTorch models on Cloud TPUs. This 10-minute demo highlights how TorchTPU serves as a unified backend for leading open-source inference engines like vLLM and SGLang, enabling deployment of state-of-the-art models with minimal code modifications.

\*******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### What's New in Inference in October
Speakers: Philip Kiely
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1317774
Keeping up with inference is a full-time job. As the field accelerates with new model architectures, inference engines, and performance techniques, it can be hard to sort out what is worth running in production. This talk provides a structured overview of the most important recent developments in inference across speculation, KV cache management, and large-scale model serving.

\***************

_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Monarch - Single-Machine DevX at Distributed Scale
Speakers: Thomas Wang, Zach DeVito
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255147
A developer’s computer is part of their identity; as unique as a fingerprint. People have their favorite tools, libraries, and agents set up for their own productivity (and happiness!). New projects that run locally are productive to work in. Unfortunately, as projects scale, we trade this development experience for more compute, using clusters with worse ergonomics.

Monarch is a library for programming an entire cluster as if it were a single machine. Imperative APIs launch processes across the cluster that communicate with fast actor-based IPC and transfer data using RDMA. This fabric lets us provide services that make it feel like all processes across the cluster are on your local machine. For instance, we use Monarch to build filesystem mounts so the local filesystem is broadcast to the entire cluster, and remote logs appear locally.

Iterating with Monarch takes seconds rather than minutes. Debugging is easier: the distributed process exits like a local process and its outputs are visible locally. This speeds up the development loop for humans and agents.

This talk will demo the experience and show how to use Monarch primitives to build large scale post training frameworks.

### How PyTorch Powers Open Foundational Models — From Language to Vision
Speakers: Songhao Jia, Laura Gustafson, Elisa Cascardi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256006
Training and open sourcing frontier foundational models presents unique challenges—scaling to trillions of tokens across thousands of GPUs, maintaining reproducibility, and enabling a global community to fine-tune and deploy models. In this session, we explore how PyTorch addresses key challenges in building and open sourcing foundational LLMs (Llama) and vision models (SAM).

We cover three angles: 1) how PyTorch-native tools like TorchTitan power pre-training through composable parallelism, torch.compile, and Float8—applied to both LLMs and vision architectures, 2) the road to open sourcing foundational models—from internal research to community-ready releases across modalities, and 3) how this foundation enables adopters in healthcare, robotics, and autonomous systems to fine-tune Llama for domain NLP and SAM for zero-shot segmentation.

We share hard-won lessons: scaling distributed training without sacrificing code clarity, designing checkpointing for interoperability, and building an open ecosystem where models train on PyTorch and millions customize them. Attendees leave with practical strategies for training, releasing, and sustaining large-scale open models with PyTorch.

### Extending TorchInductor with FlyDSL: A New MLIR-Native Backend for High-Performance GEMMs
Speakers: Liz Li, Cao Jiahui
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256835
TorchInductor is PyTorch's primary compiler backend, generating optimized kernels through graph lowering, autotuning, and backend-specific code generation. Recent efforts have expanded TorchInductor beyond Triton, demonstrating the value of a flexible multi-backend architecture.

In this talk, we present the integration of FlyDSL, AMD's Python-native and MLIR-based GPU kernel DSL, into TorchInductor's GEMM compilation pipeline. We describe how FlyDSL connects to TorchInductor's autotuning framework, covering workload analysis, candidate generation, compilation, benchmarking, caching, and runtime backend selection.

We discuss the design decisions that enable FlyDSL to coexist with existing TorchInductor backends while preserving the torch.compile user experience, along with challenges in kernel specialization, compilation latency, autotuning scalability, and backend fallback.

Finally, we present performance results for transformer training and inference on AMD Instinct GPUs, comparing Triton and FlyDSL implementations. Attendees will gain practical insights into FlyDSL kernel design, how new compiler backends can be integrated into the PyTorch stack.

### Who Owns Production When the Agent Does the Fixing? Governance in AI-Assisted SRE
Speakers: Aditi Mewada
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255337
AI agents are no longer just suggesting fixes - they're shipping them. As autonomous remediation becomes standard in SRE workflows, the industry is quietly skipping over a critical question: when an agent misconfigures a service at 3am and takes down production, who is accountable? This talk explores the governance frameworks, guardrails, and human-in-the-loop patterns that separate safe autonomy from dangerous automation. We'll examine where AI-assisted SRE is genuinely delivering with faster MTTR, reduced toil, and smarter alerting, and where unchecked agent authority creates new classes of failure. You'll leave with a practical mental model for deciding what your agents should fix, what they should flag, and what should never leave a human's hands.

### Relay and Reuse: The Dual Engine Behind PyTorch Out-of-Tree Release Readiness
Speakers: Zesheng Zong
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253488
For heterogeneous accelerators, keeping pace with PyTorch's fast bi-monthly release cycle is a constant uphill battle. This session shares how we sustain high quality while shipping stable releases within a month of each upstream update.
Test Refactoring & Device-Agnostic Reuse: We show how instantiate_device_type_tests and dynamic skipping break the tie between tests and hardware. The payoff: 580K+ community test cases become reusable out of the box, giving full API semantic parity at almost no extra cost.
Cross-Repo CI Relay (CRCR) & Quality Gates: CRCR wires every PyTorch PR directly to accelerator code, co-compiling and testing both in real time. By validating upstream changes against the backend before they merge, it catches regressions at the source, easing adaptation and locking in post-release stability.
Together, reuse and cross-repo CI let an out-of-tree backend ship high-quality releases within 30 days.
Benefits: this blueprint lowers the barrier to hardware integration, while CRCR doubles as an early-warning system for PyTorch Core — flagging regressions before they spread, so every user gets the newest features at once, with no fragmentation.

### A Developer’s Guide to Attention in vLLM
Speakers: Lucas Wilkinson, Matthew Bonanni
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1254038
Attention is no longer just “standard attention.” As models push toward longer context windows, attention has become one of the most active areas of architecture design. New schemes, including sliding windows, sparsity, compression, and linear variants, save KV-cache memory at long contexts, and nearly all modern state-of-the-art models now use hybrid attention, mixing patterns across layers to balance quality with memory use.

This talk will give developers a practical guide to how vLLM represents, serves, and optimizes this growing diversity of attention schemes. We will start by reviewing the schemes used in recent models, and then walk through the core vLLM abstractions that make them possible, including attention backends, KV-cache connectors, and the hybrid memory allocator. Together, these allow vLLM to support a wide range of attention implementations while maintaining a unified serving path, efficient batching, and high-performance memory management.

Finally, we will cover the recent overhaul of vLLM’s attention abstractions: what changed, why the old assumptions no longer hold, and how the new design makes it easier and cleaner to support emerging architectures.

### Practical GPU Programming with Triton for PyTorch Developers
Speakers: Suman Debnath, JanakiRam Goteti
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1252848
If you've used PyTorch, you've already run thousands of GPU kernels, you just never had to write one. Tools like torch.compile and Triton handle that for you. But what's actually happening underneath, and what if you wanted to write a kernel yourself?

This talk is a friendly introduction to GPU programming with Triton, an open-source tool for writing fast GPU code directly in Python, no CUDA, no C++ required. We'll start from the basics: what a GPU kernel is, why GPUs are fast, and how PyTorch quietly generates kernels for you behind the scenes.

From there, we'll write our first Triton kernel together, starting with something simple like adding two vectors, then building up to a small matrix multiplication. Along the way you'll pick up the core ideas, how a GPU moves data around, what it means to run thousands of threads at once, and how to check whether your kernel is actually fast; all through plain, readable Python.

You'll leave knowing what a GPU kernel really is, how to read the code PyTorch generates for you, and how to write a simple Triton kernel of your own. No prior GPU experience needed, just comfort with Python and PyTorch.

### Compute, Latency, and Safety: Architecting Stateful Guardrails for Multi-Agent Workflows
Speakers: Purva Chiniya
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1251388
Deploying a single LLM is a solved infrastructure problem. Deploying a multi-agent system where autonomous nodes pass state, execute external tools, and orchestrate complex workflows introduces a massive architectural bottleneck: How do you secure inter-agent handoffs without destroying real-time throughput?

In production environments serving millions of users, standard security checks fail to catch "indirect orchestration exploits" (where untrusted data corrupts downstream agent privileges). But evaluating every single state change with a massive frontier model is computationally impossible and financially ruinous.

This session breaks down the MLOps infrastructure required to secure multi-agent architectures at enterprise scale. Drawing from the development of open-source evaluation frameworks like SecRepoBench, we will detail how to build continuous, stateful red-teaming pipelines. Attendees will learn how to deploy specialized, low-latency Small Language Models (SLMs) as deterministic orchestration guardrails, routing cross-agent payloads through high-speed evaluation checks that catch prompt injection and operational drift without bottlenecking the entire system.

### Shipping PyTorch and Its Ecosystem: A Modern Release Story
Speakers: Andrey Talman
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256844
PyTorch is no longer just a framework — it's a release train that pulls Triton, vLLM, and the broader ecosystem with it. A good release isn't the day binaries land; it's whether users pick up the new version on day one and have everything just work.

This talk shares how we've reshaped that story across three threads:
\- A faster, more predictable release process — fewer manual steps, broader validation, a calendar developers can plan around.
\- Ecosystem integration as a first-class deliverable: Triton and vLLM validated continuously against PyTorch nightlies, breakage surfaced upstream early, the release branch cut with the ecosystem already green.
  \- AI in the release loop — agents triaging CI, separating noise from regressions, drafting fixes — and what we've learned about where they accelerate the team and where humans still own the call.

### TorchTPU: Running PyTorch Natively on Google TPUs
Speakers: Claudio Basile
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1251871
TPUs are the cornerstone of Google’s AI leadership and a high-performance compute pillar for Google Cloud Platform (GCP) users, yet until now their access has been limited to JAX. Enter TorchTPU, which bridges this gap, offering a high-performance, native PyTorch backend to bring TPU benefits to the PyTorch community without compromising usability.
TorchTPU foundation is an Eager-first stack supporting PyTorch idioms natively. It utilizes an ATen-to-StableHLO lowering path and "DeferAndFuse" execution to maximize hardware utilization via automated op fusion. For massive-scale workloads, our XLA stack enables compute-communication overlap through SparseCore, while bounded dynamism eliminates recompilation overhead from dynamic shapes. This architecture integrates seamlessly with standard frameworks like vLLM for serving and TorchTitan for training.
Proven through production-scale engagements with private preview partners, TorchTPU delivers a competitive advantage across training and inference. These field-validated successes underscore the stack’s readiness for the broader ecosystem as we transition to an open-source model with an upcoming public GitHub repository release.

### Helion: CuteDSL and TPU Backends for Heterogeneous Hardware, and Why It Suits Agents
Speakers: Oguz Ulgen, Dunfan Lu, Jason Ansel
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255964
Helion is a Python DSL that raises kernel authoring above languages like CUDA and Triton: you describe a kernel at a high level, and a compiler and autotuner generate the device code. This talk introduces two new compiler backends.

The motivation is hardware heterogeneity and performance. Accelerators are diverging, and reaching state-of-the-art performance on each one normally means hand-writing kernels in that vendor's low-level language. The new backends lower a Helion kernel through CuteDSL for recent NVIDIA GPUs and through Pallas for TPUs. The same source targets different hardware without giving up that performance or rewriting per vendor.

The second half covers code generation by LLM agents. Because Helion sits above the languages it compiles to, a kernel takes fewer tokens to express and offers less surface area for mistakes, and the autotuner handles the performance tuning that agents do poorly. We cover where this holds up and where it doesn't.

### Privacy-Preserving AI Across Institutions: Federated Learning Lessons for Medical Imaging
Speakers: Sudhanshu Shrivastava
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1199496
How do we build useful AI across institutions when raw data cannot be centralized? In this talk, I present a federated learning case study in glaucoma imaging using 5,550 color fundus photographs from nine datasets across seven countries. I show how site-specific fine-tuning preserved the privacy advantages of federated learning while matching central-model performance for cup segmentation across all sites and for disc segmentation in most sites, with clear gains in cross-site generalizability over local and standard federated baselines. Beyond the model results, I will discuss what this teaches us about privacy-preserving AI deployment in practice: the tradeoff between local adaptation and global robustness, the operational challenges of multi-site learning, and where secure infrastructure can complement federated approaches. Attendees will leave with a concrete research example and practical lessons for designing robust, privacy-aware AI systems in regulated settings.

### Scaling PyTorch's Compatibility Promise: A Tiered Cross-Repository CI Relay for Out-of-Tree Backends
Speakers: Subin George, Jewel K M
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1251891
The proliferation of hardware accelerators— NPUs, RISC-V processors, custom silicon— has expanded PyTorch far beyond its original foundation. Out-of-tree (OOT) backends maintain independent CI yet depend on upstream interface stability. Breaking changes are discovered only post-merge, imposing costly bisection and delayed releases. We present the Cross-Repository CI Relay (CRCR), a system that forwards PyTorch PR and push events to downstream repos in real time via a GitHub App, enabling compatibility validation before merge. A four-tier trust model (L1–L4) governs integration depth: event dispatch (L1), HUD-visible observability (L2), non-blocking PR checks (L3), and blocking merge prerequisites (L4). The architecture comprises a relay with allowlist-governed dispatch, an ingestion pipeline (DynamoDB, ClickHouse), and a Next.js visualization layer with per-backend dashboards and PR status panels. Security employs OIDC authentication, timing-safe token validation, and relay-verified trusted envelopes. Deployment with Ascend NPU and RISC-V backends reduces breakage detection from days to minutes. This pattern generalizes to any open-source ecosystem with growing out-of-tree plugins.

### Demo Theater: Composable Tensor Programming Across Compiler Stages: PyTorch, TCL, and VISA
Speakers: Sol Kim
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1342322
Large fused graphs create a fundamental tension for accelerator compilers: wider fusion enables optimization across operator boundaries, but also causes a combinatorial search over execution engine, tiling, computational lowering, and memory scheduling. This talk presents furiosa-torch's approach to narrowing that search with TCL (Tensor Contraction Language) and VISA (Virtual Instruction Set Architecture), two custom-kernel DSLs whose kernels remain composable with automatically compiled ATen operators and GraphModules rather than becoming opaque boundaries to graph compilation. In our internal development workflow, we begin with automatic compilation, identify expensive or performance-critical regions, use an AI agent to write or improve their TCL implementations, validate them against the original PyTorch code, and compose them back into eager execution and torch.compile. TCL makes engine selection, tiling, and lowering explicit while leaving cross-operator memory scheduling to the compiler; VISA additionally exposes memory placement, with a type system that rejects mappings unsupported by the hardware. Using this workflow on the same fused computation, we examine how the compiler, developer, and agent can divide implementation decisions to reduce compilation time while balancing execution performance and programming effort.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies_

### Demo Theater: Your AI Model Needs More Than an API
Speakers: Mayank Debnath
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1362826
Inference, GPUs, networking, storage and scale all matter. Come see the infrastructure behind production AI workloads with Vultr.

\*****************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### vLLM Roadmap
Speakers: Zachary Xi, Nick Hill
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1355211
This talk covers the vLLM roadmap across the engine, the ecosystem, and the project’s open-source practices. On the engine side, we will walk through the Flat Model and Model Runner V2 migrations, disaggregated serving with multi-tier KV offloading, speculative decoding for low latency, and production-grade quantized KV cache compression. We will also discuss the infrastructure, CI, and security work planned to support a rapidly growing contributor base, along with the expanding ecosystem around quantization, speculation, RL frameworks, and vLLM-Omni for real-time multimodal models.

\****************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Hardware-Aware AI: Building Agentic Systems from Cloud to Edge with PyTorch, ExecuTorch
Speakers: Kavya Sri Chennoju
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291518
Large language models have transformed how developers build AI applications but the next generation of systems won't live in the cloud. They'll interact with robots, sensors, cameras, industrial equipment, and edge devices, requiring a new approach for connecting AI with the physical world.
This session explores building hardware-aware AI applications with the PyTorch ecosystem, covering how PyTorch powers model development, ExecuTorch enables efficient on-device inference, vLLM delivers scalable LLM serving, and Arm Device Connect enables AI applications to discover, understand, and interact with heterogeneous hardware.
Using a live end-to-end cloud-to-edge workflow, we'll show how foundation models reason about tasks, invoke edge models, retrieve live sensor data, and coordinate physical devices without bespoke integrations for every deployment.
Attendees will learn to architect AI applications spanning cloud, edge, and embedded systems, and learn why hardware-aware AI is the next frontier for the PyTorch ecosystem.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Closing the Confidence Gap: Making AI Output Trustworthy in Enterprise Systems
Speakers: Ravi Teja Prabhala Venkata
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256339
Every AI model produces outputs, but not every output is trustworthy. The gap between what a model generates and what's safe to use is where most AI failures happen — silently, in production. This session presents a four-layer validation architecture to close that confidence gap: type coercion (ensuring structured outputs match schemas), confidence calibration (detecting uncertainty and hallucination), contract validation (verifying outputs against business rules), and observability (monitoring AI behavior to catch drift before it becomes a crisis). The session walks through each layer with implementation details, showing how teams can wrap PyTorch models and LLM-powered services with guardrails that catch errors before reaching users. We'll examine real failure modes: plausible but fabricated data, schema drift, confidence scores that don't correlate with accuracy, and cascading failures. This approach treats AI reliability as an engineering discipline, not a research problem. Attendees will leave with actionable patterns for immediate improvements to AI system trustworthiness.

### PyTorch Generalization: A Journey Toward Write Once, Run Anywhere
Speakers: Yu Guangye, Eikan Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256608
As AI hardware continues to diversify, PyTorch faces a growing challenge: many APIs, runtime interfaces, and testing infrastructures remain fragmented and backend-specific, making it difficult for users to write portable code and for developers to support new hardware consistently.
This talk presents our ongoing generalization effort to make PyTorch truly “write once, run anywhere.” We will cover three key areas: (1) model-level API unification, including Autocast, Inductor, and graph capture/replay; (2) the introduction of torch.accelerator, a unified runtime API for device, stream, event, RNG, and memory management; and (3) the evolution of PyTorch’s test infrastructure to validate correctness consistently across backends, covering Distributed, Dynamo, Inductor, ATen operators, and more.
Together, these efforts reduce per-backend maintenance costs, improve testing consistency, and provide a scalable foundation for integrating new hardware into PyTorch. Our goal is to deliver a consistent user and developer experience across all backends—whether in-tree or out-of-tree—and to strengthen the PyTorch ecosystem through greater portability, maintainability, and community collaboration.

### The Nemotron Ecosystem: Building the Third Generation — Nano, Super, and Ultra
Speakers: Shashank Verma, Yi-Fu Wu US
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256810
The Nemotron ecosystem is NVIDIA's open-first model family and the tooling that builds it. This talk covers gen 3: Nano (31.6B-A3.6B), Super (120.6B-A12.7B), and Ultra (550B-A55B) — hybrid Mamba-Transformer MoE models spanning two orders of magnitude. Open-first means the full stack ships: weights, pre/post-training data, tech reports, reproducible recipes, and tooling — so you can rebuild, not just download. End-to-end pipelines: github.com/NVIDIA-NeMo/Nemotron.
We walk the architectures and what emerged at scale: a hybrid Mamba-Transformer MoE backbone (25T tokens, 1M context), Super's LatentMoE + multi-token prediction for hardware-aware sparse scaling, and Ultra's path to 550B with NVFP4 on Blackwell.
Then every pipeline phase and the NeMo component behind it — NeMo-Curator, DataDesigner, Megatron-Bridge/AutoModel, NeMo RL/Gym, NeMo Evaluator — one PyTorch-native flow with full artifact lineage. We show how the models diverge: Nano's single-pass multi-env GRPO+DPO, Super's six-stage RL across 21 environments (SWE-RL in sandboxes, async GRPO), Ultra's multi-teacher on-policy distillation. We close with agentic tooling for customization.

### High-Velocity GPU Kernel Authoring with CUTLASS Python
Speakers: Michael Goldfarb US, Guray Ozen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257904
CUTLASS’s CuTe DSL has recently delivered state-of-the-art GPU kernel performance in projects like FlashAttention 4, TRT-LLM, vLLM, and FlashInfer. In this talk, we present new Python-first capabilities making advanced kernel construction more accessible to PyTorch kernel developers, reducing boilerplate while maintaining the DSL's zero-cost abstractions.

We introduce three new features designed to simplify kernel development. First, CuTe DSL extensions: high-level building blocks automating complex programming tasks while maintaining optionality and zero runtime cost. Second, CUTLASS Python Primitives expose a new API for direct access to low-level hardware instructions, granting precise control for performance-critical kernels. Lastly, Resource and Task Scheduler (RTS), a zero-cost metaprogramming framework providing static verification for asynchronous primitives, simplifying writing performant, deadlock and race-free warp-specialized kernels.

Together, these features let developers work at the right level of abstraction: concise for common patterns, explicit for hardware-level control, and structured for complex asynchronous execution.

### Demo Theater: From Model to Agent: Running Agentic Coding on Open Infrastructure
Speakers: Cam Flanagan
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1347549
See how to go from a deployed model to an agent doing real work. In this live demo, we’ll deploy an open-weight model on Nscale Dedicated Inference, connect it to the open-source OpenCode coding agent, and watch it pick up and work through a real issue. It’s a practical demonstration of running agentic coding workflows on dedicated GPU infrastructure using open tooling, and a hands-on companion to our breakout session, Lessons at Scale: Building an Open PyTorch Inference Stack.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Fighting Agents with Agents Bringing Claude to PyTorch CI, triage, and PR review
Speakers: Driss Guessous
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255221
PyTorch maintainers are reviewing and ever increasing number of PRs written by AI agents. Contributors use agents. Bots use agents. Everyone uses agents. So the question for us was pretty direct: if agents are going to increase the amount of code and issues flowing into PyTorch, what tools do maintainers need to keep up without lowering the bar?

This talk is about how we brought Claude into PyTorch infra. We started with `@claude` on issues and PRs, then added automatic issue triage, reusable onboarding for `pytorch` and `meta-pytorch` repos, PR review skills, and CI/autorevert investigation.

We will walk through the workflow shape, Bedrock/OIDC setup, two-stage GitHub Actions, tool allowlists, repo-specific skills, and the adoption trend after launch. The goal is not to replace maintainers. The goal is to give maintainers agent-shaped infra for an agent-shaped world.

### Demo: Fitting Large MoE Fine-Tuning onto Few Nodes: Expert & Context Parallelism in DeepSpeed
Speakers: Suman Debnath, Jiale Huang, Daniel Shen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1317873
Fine-tuning LoRA adapters on large Mixture-of-Experts (MoE) models is often bottlenecked not by compute but by HBM capacity: expert weights, long-context activations, and optimizer state can easily exceed what a small cluster provides. In this demo, we give a quick primer on expert parallelism and context parallelism, then show how to combine them in DeepSpeed to fit large MoE fine-tuning jobs onto just a few nodes.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo: Scaling AI Across Devices: ExecuTorch Portability & Performance from Edge to Mobile, XR, & IoT
Speakers: Derrick Johnson, Felix Baum
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1347503
This session showcases how Qualcomm enables developers to build AI-accelerated applications with ExecuTorch once and seamlessly deploy them across a broad range of Qualcomm-powered devices, including compute platforms, smartphones, XR devices, and IoT form factors. By leveraging a unified PyTorch-native deployment workflow, developers can preserve portability while scaling performance and power efficiency across heterogeneous compute resources, including CPU, GPU, NPU, and Low Power AI (LPAI) accelerators.

The live demonstration features a fully on-device, agentic robotics application powered by Gemma 4, running on both a laptop and a smartphone from a common ExecuTorch deployment architecture. Using the Model Context Protocol (MCP), either device can interact with and control a robot by combining multimodal AI capabilities, including real-time perception, gesture recognition, language understanding as well as low-latency control. The robot can switch between behaviors such as Training, Follow, and Sentry modes, illustrating how a single AI application can scale across devices while taking advantage of the optimal hardware acceleration available on each platform.

Attendees will see how ExecuTorch, combined with Qualcomm AI acceleration, enables a ""build once, deploy everywhere"" approach for next-generation edge AI applications, reducing development complexity while delivering scalable performance, power efficiency, and portability across diverse device ecosystems.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: Live Post-Training with TitanRL
Speakers: Angel Li
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1362598
Reinforcement learning (RL) has become a core part of LLM post-training, but RL stacks are often stitched together from separate training and inference systems. TitanRL is TorchTitan's performant and hackable RL library that supports both async and on-policy RL with a unified model definition between the trainer and generator. It provides a consistent, shared implementation that offers batch invariance and integrates well with TorchTitan pre-training.

In this demo, we will show how to go from installing torchtitan to a post-trained model in just 10 minutes. We cover building a new task using TitanRL, a variety of observability tooling, and how to achieve batch invariance. We'll also explore how to extend this example to more complex agentic RL for frontier use cases.

\*********************
_Please note: In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: AMD Skills: From Prompt to Performance
Speakers: Daniel Holanda
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1344446
What if your AI agent knew how to get the most out of AMD hardware? Could it help you deploy a model on an AMD Instinct GPU? Find bottlenecks and optimize GPU kernels? Diagnose and fix stubborn issues on your local device? See AMD Skills in action and turn your coding assistant into an AMD expert.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: Pretraining at Scale with TorchTitan
Speakers: Elfie Guo US
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1339821
Frontier model pre-training has converged on MoE, and communication increasingly determines how efficiently models scale across thousands of GPUs. In this demo, we walk through how NVIDIA's contributions to TorchTitan unlock world-record MoE pre-training performance on NVIDIA GPUs covering the key optimizations that compound into real throughput gains you can measure and reproduce yourself.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: IBM Spyre Accelerator in The PyTorch Open Ecosystem
Speakers: Mudhakar Srivatsa
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1351816
This talk presents how IBM Spyre streamlines its AI acceleration stack by leveraging PyTorch's open-source ecosystem. We showcase how PyTorch's Inductor compiler, combined with open-source extensions, provides a unified compilation framework that enables Spyre to be registered as an out-of-tree accelerator fully aligned with PyTorch's standardized interfaces. By integrating seamlessly with vLLM and adopting broader open-source model optimization techniques, we demonstrate a cohesive opensource approach that maximizes performance across diverse AI workloads on x86, IBM Z and Power platforms.

In this expo theater presentation, we'll demonstrate the new stack through two compelling use cases. First, we'll showcase an Insurance Claim Processing system leveraging Granite and Gemma models on IBM Z with Telum II processor, performing real-time multi-model AI inference for claim analysis and damage assessment including visual damage detection. Second, we'll present Document Intelligence with AI Optimizer, featuring multi-language support through IBM Granite Embedding Models, RAG-based document processing, and intelligent summarization capabilities across enterprise documents. Both demos highlight the practical impact of seamless PyTorch ecosystem integration for accelerating production AI applications.

\*********************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Smarter Autotuning for Kernels: From Bayesian Optimization to LLM-Guided Search in Helion DSL
Speakers: Jongsok Choi, Ethan Che
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256728
Autotuning is the backbone of Helion — PyTorch's DSL for authoring performant and portable ML kernels. Every Helion kernel is tuned across a vast, high-dimensional configuration space to achieve peak performance on heterogeneous hardware. This talk presents two major leaps in autotuning that have transformed Helion's compile-time story:

LFBO (Likelihood-Free Bayesian Optimization): A machine-learning-guided search that uses a lightweight Random Forest classifier trained on-the-fly to intelligently filter candidate configurations, reducing autotuning time by 36.5% while improving kernel performance by 2.6% on NVIDIA B200.

LLM-Guided Autotuning: A novel approach that leverages LLMs' knowledge of GPU programming to propose high-quality configurations in seconds, achieving up to 10X faster tuning time on NVIDIA B200. We combine the best of both worlds with the LLM-Seeded Hybrid Search, which uses the LLM to quickly get to a performant configuration, then uses the LFBO Search for the fine-grained search.

We share the evolution from Random Search, LFBO Search, to LLM-Guided searches, with concrete results across kernel families tested on H100 and B200 GPUs.

### State-of-the-Art KV Transfer for Disaggregated LLM Serving in vLLM
Speakers: Nicolò Lucchesi, Sunita Nadampalli, Zhanqiu Hu
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255023
As LLM deployments scale, disaggregated P/D serving is emerging as a key architecture by separating compute-bound prefill from memory bandwidth-sensitive decode. An efficient KV cache transfer layer is critical to preserve disaggregation's benefits, and a flexible interface is necessary to generalize across models and heterogeneous hardware such as NVIDIA GPUs and AWS Trainium.
Agentic workloads with multi-turn conversations require state to flow bidirectionally between P and D, while production systems must remain resilient to failures and traffic spikes.
Hybrid models such as Nemotron, Qwen3.5 and DeepSeek-V4 interleave attention layers or combine KV compression and sparse sliding-window, producing diverse cache layouts and sharding semantics that interact with optimizations like prefix caching and CPU offloading.
We present developments in vLLM's disaggregated serving stack that address these challenges, including hybrid model transfer with heterogeneous TP, bidirectional KV transfer, KV Push connector, and KV cache leases for reliability. KV Push improves responsiveness by reducing TTFT, while on Nemotron disaggregated P/D Pareto-dominates co-located across concurrency levels.

### Fast, Small, Accurate: Optimizing Models for Inference using FP4 Quantization
Speakers: Zhiyu Cheng US, Trenton Starkey
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253987
FP4 quantization is one of the most promising techniques for compressing large models without sacrificing accuracy, but implementing it requires navigating new hardware formats, limited dynamic range, and layer-specific tradeoffs. In the last few years we’ve seen emerging hardware support for new low-precision 4-bit floating point formats (FP4) that deliver both time and space optimizations for computations like general matrix multiplication (GEMM). In this session, we present how FP4 formats, including MXFP4 and NVFP4, are implemented, with a focus on how block grouping and scaling factors address the limited dynamic range of 4-bit representation. We will then cover practical considerations in quantizing FP16 and FP8 models, exploring the impact on performance and accuracy when applied to model layers. We finish with a practical walkthrough of how we optimized an NVFP4 checkpoint for the Nemotron 3 Super model using the open source Model Optimizer library. This NVFP4 checkpoint stays within ~1.3 points of its BF16 counterpart's accuracy, while delivering a ~2.2x throughput speedup—demonstrating that 4-bit quantization can compress the model with virtually no accuracy loss.

### KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration
Speakers: Kaiming Cheng, Laura Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1251908
Recently, the PyTorch team released KernelAgent, an open agentic system achieving 100% correctness across all 250 L1/L2/L3 KernelBench tasks. We extend that work by adding a hardware-guided optimization layer to the existing framework. Building on the previous correctness-focused pipeline, KernelAgent integrates GPU hardware-performance signals into a closed-loop multi-agent workflow to guide the optimization for Triton Kernels.

We evaluate the kernels generated by KernelAgent on all 100 L1 KernelBench tasks. Overall, it achieved 2.02x speedup over generated kernels from earlier versions. On average, KernelAgent generated 1.56x speedup when compared to default torch.compile, outperforming 65 of 100 KernelBench L1 tasks and achieving 89% of the hardware roofline efficiency on the H100.

The optimization codebase is located at KernelAgent repo with documentation to get started. We also share a selection of end-to-end KernelAgent optimization artifacts in the open-source repo.

### Demo Theater: Where’s My Training Job?
Speakers: Marie Antons
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1314428
When a Ray training job fails, the cluster is usually already gone, and with it your evidence. We'll show what a job-centric view of distributed AI looks like, and why infrastructure-first observability keeps missing the failure.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### From Neurons to Atoms: How PyTorch Powers Open Science at Scale
Speakers: Elisa Cascardi, Hubert Banville, Ray Gao
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255173
AI for Science is fragmented—siloed tools, incompatible formats, and workflows hindering scaling. We faced this in two radically different domains: neuroscience & chemistry. We show how PyTorch became the unifying backbone to build and open source NeuralSet and UMA—a toolkit and model for interoperability and scalability, accelerating discovery worldwide.
We explore three angles: 1) how NeuralSet aligns brain recordings and stimuli into one efficient configurable PyTorch DataLoader that keeps GPUs fed on terabyte-scale datasets to train large models linking brain activity to what people see and hear, 2) how UMA's architecture harnesses PyTorch to train on 500M+ atomic structures and deliver SOTA molecular simulations, and 3) the road to open sourcing AI for Science on PyTorch.
We distill cross-domain challenges and innovations: taming heterogeneous data at scale, designing pipelines with PyTorch primitives, ensuring reproducibility, and converting research into community artifacts. These apply to any team with complex multimodal data looking to open source on PyTorch. Attendees leave with concrete strategies to bridge research and production-quality open source scientific tooling.

### From Scratch to PyTorch: Demystifying ML Frameworks by Building Your Own
Speakers: Andrea Mattia Garavagno, Vijay Janapa Reddi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256633
Most developers interact with PyTorch through its high-level API, leaving the core engine treated as magic. They don't know what happens when they call loss.backward() or why Adam needs 3× the memory of SGD. But to debug complex logic, optimize hardware, or contribute to PyTorch's backend, bridging the gap between "using" and "understanding" is mandatory.

In this session, we introduce TinyTorch: an open-source CLI application that demystifies PyTorch by guiding developers to rebuild its foundational components—tensors, autograd, optimizers, and transformers—in pure Python. We will walk through the architecture and pedagogy of the project, demonstrating our systems-first, build-to-validate methodology.

Attendees will see how they can recreate pivotal AI breakthroughs, from the Perceptron to Transformers, and culminate in MLPerf-style benchmarking with their own code. We will share insights on common pitfalls in learning ML systems and how engineering teams can leverage this curriculum to upskill their developers.

TinyTorch is how we grow the next generation of PyTorch contributors and the engineers who will build what comes after.

Open source: mlsysbook.ai/tinytorch

### Demo Theater: Fighting RL-trained LLMs in Street Fighter III: 3rd Strike
Speakers: Andrew Hinh
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1304168
Come see me beat up an LLM in Street Fighter III live! Along the way, I'll show how Modal's infrastructure enables low-latency inference and easy LLM post-training, both of which are necessary for elite gameplay. It's not just for show though: customers like Engram, Decagon, Sierra, and Cognition use the very same infrastructure for various production-scale workloads.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### What You Cannot Profile, You Cannot Optimize: Learning to Read PyTorch Traces
Speakers: Suvaditya Mukherjee
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255448
Almost everyone knows they should profile their PyTorch code. Almost no one enjoys it. Traces are dense walls of colored rectangles with cryptic kernel names. In this talk, we attempt to lower that on-ramp.

We start with a simple workload of a matmul + bias, and learn to read what the profiler hands back: the table and the trace. Socratically, we build durable mental models covering overhead-bound vs compute-bound, the CPU→ATen→cuBLAS→GPU dispatch chain, and why the same kernel times differently across runs.

Lastly, we climb the ladder: nn.Linear, GEMM epilogues, and a real GeGLU MLP. We watch torch.compile collapse a GeLU and a multiply into one fused Triton kernel and compare it head-to-head with a hand-tuned Liger kernel from the Hugging Face Hub.

At the end of this session, we wish to leave the audience with an important habit we emphasize throughout: guess first, then look. You'll leave with the ability to parse any trace, follow a Python call down to its CUDA kernel, and understand whether your optimization actually did anything. We expect no prerequisites beyond basic PyTorch.

### Native Tiered KV Cache Offloading in vLLM: From Storage Offloading to Disaggregated Serving
Speakers: Or Ozeri
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1254938
As LLM applications shift toward long-lived agentic sessions, KV cache management becomes a critical scaling challenge. Sessions may remain idle for hours or days before a follow-up task arrives, yet their KV cache must be preserved. Offloading to cheaper storage tiers is essential to support more concurrent sessions cost-effectively. Beyond offloading, moving KV cache between instances enables load balancing and disaggregated prefill/decode.

We present vLLM's native tiered KV cache offloading framework, newly integrated upstream with no external dependencies. The key insight is routing all transfers through CPU memory as a universal transport hub, which yields multiple benefits: (1) minimal GPU overhead—each GPU performs only a simple copy to host memory; (2) consolidated I/O from a single CPU buffer rather than scattered across HBM devices; (3) hardware-agnostic design requiring no specialized transfer APIs; and (4) independence from KV cache memory layout, which varies across hardware, attention backends, parallelism schemes, and model architectures.

Join this talk to learn how to deploy, configure, and extend the framework for your own infrastructure.

### SGLang-Diffusion: High Performance Serving Framework for Offline and Real-time Diffusion Models
Speakers: Yihao Wang, Kevin Mi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1258314
SGLang-Diffusion is a high-performance serving framework for diffusion models, designed for both large-scale offline generation and latency-sensitive real-time inference. As diffusion workloads expand from image and video generation to diffusion-based world models, serving systems must handle very different constraints: maximizing GPU throughput for batch/offline jobs, while maintaining tight end-to-end latency for interactive and closed-loop environments.

This talk presents the design of SGLang-Diffusion and the PyTorch-based inference optimizations behind it, including efficient request scheduling, memory management, batching strategies, and execution-path optimizations for diffusion pipelines.

We will discuss how serving diffusion models differs from serving LLMs, why existing inference systems are often insufficient for iterative denoising workloads, and how a unified framework can support both offline generation and real-time world-model inference. The goal is to share practical lessons for building scalable, production-ready diffusion serving infrastructure.

### Scaling Foundation Models: From Broken to Near-Linear Multi-Node Training
Speakers: Sheng Huang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256382
At Pinterest, foundation models power recommendations for 600M+ MAUs. When we first tried multi-node training for a PyTorch/TorchRec model, adding a second 8-GPU node made training 5x slower than a single node. Even after Elastic Fabric Adapter (EFA) made networking viable, 4 nodes gave 1.21x scaling: 3x more GPUs for 21% more throughput. Larger model gains were out of reach.

We turned broken multi-node training into near-linear scaling. PyTorch Profiler and NCCL traces showed the bottleneck was not FLOPs, but cross-node All-to-All traffic from distributed embedding lookups: GPUs looked busy waiting on the network.

This talk covers: FP8 communication with FBGEMM, balanced TorchRec embedding sharding, embedding reshaping, Distributed Checkpoint (DCP) for load-time resharding, and a 2D parallel topology that keeps expensive All-to-All local and syncs replicas with AllReduce. Scaling improved from 1.13x to 2.0x at 2 nodes, and from 1.21x to 3.9x at 4 nodes, reaching 97.5% of ideal. It extended to 7.5x at 8 nodes, 93.75% of ideal.

Attendees leave with a playbook: measure bottlenecks, reduce bytes on the wire, checkpoint portably, and design topology around the slowest link.

### From Fragmented AI to End-to-End Radiology Reports: Scalable Clinical LLMs with TorchTitan
Speakers: J Deonarine, Khushboo Rathi, Eric Karl
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256115
Hundreds of FDA-cleared deep learning models assist radiologists, yet many clinicians report these tools increase workload and diagnostic uncertainty by producing fragmented outputs. As one clinician noted, “Now I have to review the X-ray and multiple AI outputs—this adds time and confusion.”

We present an alternative paradigm: generating a complete radiology report draft end-to-end to directly augment clinical workflow. Our initial system, a long-sequence (~500K context) ViT–RoBERTa encoder–decoder, is deployed in clinical practice with peer-reviewed validation.

We describe our transition to a decoder-only architecture built on TorchTitan, improving inference efficiency and enabling scalable training via model/data parallelism, robust checkpointing, and fault tolerance (TorchFT). By replacing image tokens with DINO-based embeddings and eliminating the encoder, we achieve comparable performance while reducing training time on tightly-optimized Dell infrastructure from ~6 weeks on 32 H100s to ~1 week on 4 H100s.

We share practical lessons on scaling multimodal training, and demonstrate improved workflow, reduced diagnostic ambiguity, and real-world clinical impact

### Crossing the Divide: Co-Evolving Kubernetes and Ray for the AI Era
Speakers: Jago Macleod, Ion Stoica
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256376
The AI workload orchestration landscape is currently split across two massive, parallel universes: the CNCF (the bedrock of cloud native and modern infrastructure) and the PyTorch Foundation (the epicenter of AI/ML innovation). While these foundations operate independently, the end user does not have the luxury of choosing just one. PyTorch Foundation contains PyTorch, vLLM, Ray, and more, while CNCF owns Kubernetes, Envoy, OpenTelemetry, llm-d, containerd and more. To build, deploy, and scale modern AI applications, users require a seamless integration of projects from both ecosystems.
In this session, Jago Macleod (Google) and Ion Stoica (Anyscale / Databricks / UC Berkeley) will explore the critical bridge connecting these communities: the co-evolution of Kubernetes and Ray into a unified OSS AI Stack. We will discuss how Google and Anyscale, together with the broader community, are actively collaborating to build an open, vertically integrated stack that prevents ecosystem fragmentation.

### Training on AWS Trainium via TorchNeuron: TorchTitan and Hugging Face Transformers v5
Speakers: Maen Suleiman, Michael Benayoun
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256874
TorchNeuron, the native PyTorch backend for AWS Trainium, makes Trainium a PyTorch device, so PyTorch training libraries run on it.

 TorchTitan, PyTorch's native distributed training framework, runs on Trainium through TorchNeuron. We show how TorchNeuron enabled that integration and the work it took to enable TorchTitan on Trainium. We then cover what TorchTitan supports there today (eager mode and torch.compile, FSDP, tensor parallelism, distributed checkpointing) and the training use cases it enables, from pre-training to post-training.

Hugging Face Transformers v5 trains on Trainium through its standard APIs. We show how to fine-tune a Hub model with Transformers, TRL and PEFT, and how kernels from the Hugging Face kernel hub apply through kernelize().

 We close on what hardware-portable training means when you actually try it.

### Understanding Modern Vision Language Models
Speakers: Aastha Jhunjhunwala, Mark Moyou
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1260323
Are you using vision-language models in your agentic applications without really understanding how they work under the hood: why two models with nearly identical benchmark scores behave nothing alike, how training and inference actually differ, or how to fine-tune them efficiently across multiple GPUs?

In this talk, we deconstruct the architectures of five distinct open source models, walking through:
\- How images are encoded into tokens
\- How vision and language are fused inside the model, and why that choice drives serving cost more than parameter count does
\- How models differ at training and inference time
\- Fine-tuning efficiently: which layers to freeze and how to scale training across GPUs
\- Serving in production: image-token blow-up, KV-cache pressure, throughput, and where tools like vLLM fit

Every design is grounded in real PyTorch. Drawing on our combined experience building, fine-tuning, and deploying these models in production, we share what the papers and model cards leave out about making VLMs work end to end.

You will leave with a solid understanding of modern vision-language models: how they work, how to customize them, and how to serve them in production.

### Faster LLM Serving Startup with fastsafetensors
Speakers: Takeshi Yoshimura
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255212
As models grow, startup time has become a bottleneck for PyTorch inference systems like vLLM. A large model can take minutes to load, which slows down experimentation, deployment, autoscaling, and failure recovery.

This talk presents fastsafetensors, an open-source library that accelerates safetensors checkpoint loading. fastsafetensors treats loading as a data-movement problem: it removes per-tensor copies, coalesces fragmented I/O, and skips host staging. The result is 4.8x to 7.5x faster model loading and up to 28 GB/s of NVMe read throughput. It already plugs into existing LLM serving systems, for example:

\`vllm serve Qwen/Qwen3-0.6B --load-format fastsafetensors`

We will highlight community contributions that have transformed fastsafetensors from its original NVIDIA GPU-specific loader into a portable framework: parallel loading, 3FS integration, ROCm support, a universal wheel with runtime CUDA/ROCm detection, Windows DirectStorage exploration, and unified-memory support.

Attendees will learn how fastsafetensors works and how to make model loading fast, portable, and practical.

URL: https://github.com/foundation-model-stack/fastsafetensors
PyPi Downloads: >1.3M (May)

### Making Enterprise Agentic Inference Production-Ready with PyTorch and vLLM
Speakers: Joseph Groenenboom, Tyler Michael Smith
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1301809
While serving AI models for research and pilot use cases is a well solved problem, moving it to 24/7 Enterprise ready systems is the next important phase in AI maturity. The reliability, observability, KV cache management, and concurrency requirements for Enterprise readiness are non-trivial problems. Rising to this challenge, PyTorch, vLLM, and the other foundation projects and broader ecosystem have begun adding Enterprise level features and enhancements.

In this session we will cover the various upstream work committed to helping PyTorch and its ecosystem support Enterprise workloads. This talk will cover a sampling of some of the project work; from core PyTorch project build infrastructure up to model serving improvements to account for tool calling support and long context multi-turn chat.

You will leave this session not only with a deeper understanding of what Enterprise ready” actually entails but also understanding how those changes can be created in a large, diverse, open source ecosystem. There will be code shown and tales shared from the engine room.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### EP-Overlap: Hiding Expert-Parallel Communication in MoE Training
Speakers: Sanket Jayant Purandare, Syed Ahmed
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257875
MoE training stalls 35-60% of every step on expert-parallel all-to-all comms, and MoE's dynamically sized activations force worst-case activation memory at every layer: O(worst_case x L).

EP-Overlap hides EP comm latency by splitting each MoE layer into independent slices and overlapping one slice's token exchange with any available compute (experts, activation recompute, weight-gradient math), forward-with-forward and backward-with-backward. Under PP it also overlaps forward with backward across microbatches, where no splitting is needed. It works under FSDP and PP across all PP phases with any schedule, not just DualPipe, running as graph passes in TorchTitan's GraphTrainer, composing with GraphPP, needing no model changes, and matching eager numerics bitwise.

The same machinery hides a second cost: page stashing, which compacts a layer's worst-case activations into a page stash, cutting activation memory to O(worst_case + actual bytes used). Its stash traffic is hidden the same way, making the savings near-free.

On DeepSeek-V3 we hide 76-86% of EP comm, giving ~1.3x throughput and +4% absolute MFU, a lower bound that sync-free routing (Hybrid-EP) and CUDA Graphs should push higher.

### Ray All the Way Down: A Heterogeneous, Elastic PyTorch Training Stack at LinkedIn
Speakers: Tommy Li, Tao Huang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257598
New to scaling PyTorch past a single box? This is a guided tour of how LinkedIn trains large recommender and LLM models on Ray, plus a blueprint you can borrow. We walk three layers from the bottom up. First, a data-loading library that runs as Ray actors and streams Avro, Parquet, and Iceberg. Second, a training framework on Ray Train, with FSDP, HSDP, elastic scaling, and async checkpointing. Third, a platform that spins up clusters on demand. One idea ties it together, and you can reuse it anywhere: keep data loading off the GPUs. Dedicated CPU nodes load and preprocess the data, then ship batches to the GPU nodes over a zero-copy bridge, so the GPUs just train. Along the way we explain the pieces you need, like actors, sharding, FSDP, and elastic clusters, and we show what actually paid off, from cutting dataloader memory by 50 to 70 percent to the time we had to work around Ray to win back 24 percent of our step time. You'll leave with a clear mental model and a real place to start.

### PerfModel: A Validation-Driven Performance Model for Triton Kernels
Speakers: Xiaohu Guo
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257198
Triton GEMM autotuning on AMD GPUs can require evaluating thousands of kernel configurations per problem shape. While effective, exhaustive benchmarking introduces significant compilation and tuning overhead for production AI workloads with diverse GEMM shapes.

We present PerfModel, an analytical performance model that predicts high-performance Triton GEMM configurations before JIT compilation. PerfModel models key architectural execution constraints and combines them with roofline and occupancy analysis to rank candidate configurations and predict kernel throughput.

A key contribution is the validation methodology used to build and maintain the model. Predictions are compared against exhaustive tuning results, generated AMDGCN code, and rocprofv3 hardware-counter traces. Each discrepancy drives model refinement through a prediction–validation–correction workflow.

Across production AI GEMM workloads in fp16 and fp8, with mxfp4 in progress, PerfModel-selected configurations consistently match or exceed Triton's autotuner. We discuss lessons learned from occupancy effects, cache-capacity limits, and multi-XCD execution.

### LMCache: a cluster-wide open-source solution for LLM prompt caching
Speakers: Kuntai Du
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256217
Agentic LLM inference is now ubiquitous, but the cost of serving these agents remains high. Prompt caching is the key technique that drastically cut down the cost of serving LLM agents, and LMCache is one of the most popular open-source solution for prompt caching. LMCache has the widest inference engine coverage (vLLM, SGLang and TensorRT-LLM) and storage solutions coverage (such as Mooncake, Redis, AWS S3 and more), allowing you to perform prompt caching without twisting your in-house inference and storage solutions. This talk includes a quick tutorial on how to deploy LMCache in your Kubernetes environment, together with the techniques and research behind LMCache.

### Keeping GPUs Busy: High-Speed Storage for PyTorch via fsspec
Speakers: Ankita Luthra, Trinadh Kotturu
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1228462
As PyTorch models scale to billions of parameters, the bottleneck has quietly shifted from compute to storage. Modern GPU clusters often sit idle, "starving" for data while waiting on legacy REST-based protocols. This talk introduces Rapid Storage: a fundamental architectural shift bringing Google’s Colossus stateful protocol (that powers many Google’s products) to PyTorch via fsspec , a common Pythonic file interface used by many frameworks within PyTorch ecosystem.
By bypassing REST APIs entirely via persistent gRPC streams to the storage layer, we significantly reduced PyTorch Lightning training and checkpointing times. In this talk, we also dive into how Rapid achieves <1ms random read/write latency, 20x faster data access, and a massive 6 TB/s of aggregate throughput with 10x lower tail latency for random I/O that often stall distributed training jobs.
Beyond raw speed, we will deconstruct the integration with gcsfs and the broader fsspec ecosystem. This ensures that high-performance I/O is available across the entire data stack including Dask, Ray, HF Datasets and vLLM etc. Join us to learn how to stop wasting GPU cycles and achieve linear scaling in the cloud.

### Gain Geospatial Understanding with the PyTorch Ecosystem
Speakers: Steven Pousty
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1258269
Just as in many other fields, Geospatial and Earth Observation have benefited greatly from the new advances in PyTorch. Furthermore, because satellites usually have sensors to capture data beyond the visual spectrum, they can also reveal the unseen.

Earth Observation and Geospatial have been combined with AI to answer practical real-world questions ranging from predicting the state of the economy based (e.g. number of shipping containers in ports) to what are the actual fire risks for different homes.

The TorchGeo organization, part of the PyTorch ecosystem, has the premier AI libraries for working with this specialized data. This lightning talk will introduce you to:
Geospatial and Earth Observation data
Some prime use cases
Using projects in the TorchGeo organization to answer your AI questions
The use of domain specific visual, LLM, and visual-language models

Attendees will go home with an expanded idea of valuable data to answer their project questions, a jumping off point to start writing code, and some Github repositories with example data.

### Book Signing with Philip Kiely
Speakers: Philip Kiely
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1354949
Join us for a meet & greet and book signing with
Philip Kiely, author of Inference Engineering. A limited number of copies will be available on a first-come, first-served basis. Attendees are also welcome to bring their own copy for signing. Don’t miss this opportunity to connect with the author!

### Guardrails at the Infrastructure Layer: Sandboxing and governing Agentic AI in production
Speakers: Sai Charan Teja Gopaluni, Aaresh Sharma
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1244699
Agentic AI systems can execute code, call tools, and take multi-step actions autonomously - so where do safety guardrails actually live? Application-level filters aren't enough when an agent has shell access or can orchestrate across services. This BoF explores infrastructure-level approaches to governing agentic AI in production. Let's discuss together:

1/ Container sandboxing for agent tool execution - network policies, seccomp profiles, and runtime isolation on Kubernetes
2/ GPU-level resource boundaries - preventing one agent's runaway inference from starving safety-critical workloads
3/ Observability as governance: audit trails, token-level logging, and kill switches for agentic chains

Located across from the PyTorch gear store.

### Meet the Developers of DeepSpeed
Speakers: Minjia Zhang, Zhipeng Wang, Tunji Ruwase, Sam Foreman, Masahiro Tanaka
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1364544
Join PyTorch experts for an interactive “Meet the Developers” session – a chance to learn in a small group setting and ask your most pressing questions. No sign-up required – just drop in and get real answers from the people building the tools.

### Meet the Developers of Ray
Speakers: Mengyin Yan, Richard Liaw, Goutam Venhkatramanan, David Dai, Robert Nishihara
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1340808
Join PyTorch experts for an interactive “Meet the Developers” session – a chance to learn in a small group setting and ask your most pressing questions. No sign-up required – just drop in and get real answers from the people building the tools.

### Demo Theater: From Prompt to Physical Action: A Live Hardware-Aware AI Demo with PyTorch, ExecuTorch
Speakers: Kavya Sri Chennoju
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291522
AI agents are increasingly expected to move beyond software and interact with the physical world. This live demonstration showcases how the PyTorch ecosystem can be used to build intelligent applications that seamlessly span cloud, edge and embedded devices.

We'll build an end-to-end workflow combining PyTorch, ExecuTorch, vLLM and Arm Device Connect. Starting with a natural language request, a large language model will reason about the task, discover available devices, invoke edge AI models where appropriate, retrieve live sensor data and coordinate real hardware through a unified programming model.
The demo highlights practical techniques for combining cloud-hosted foundation models with efficient edge inference while simplifying integration with heterogeneous hardware. Attendees will see how modern AI applications can orchestrate cameras, sensors and embedded devices without requiring device-specific programming, providing a blueprint for building scalable, hardware-aware AI systems across the entire compute continuum.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: Quantization Showdown: PyTorch Inference Optimization
Speakers: Markell Rawls
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291525
Discover how to next-level your PyTorch inference with advanced optimization techniques like quantization and speculative decoding. Learn how tools like LLM Compressor and vLLM make these techniques production-ready. The focus will be on seeing these techniques in action: we will do a live stress test these techniques under real load to understand the performance, cost, and quality trade-offs that matter for your production deployments.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Agentic RL Training in Pytorch
Speakers: Yichuan Wang, Shuhua Yu
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256335
Agentic RL introduces new systems challenges beyond traditional single-turn RL. In this talk, we discuss how to build an end-to-end agentic RL training loop in PyTorch, covering rollout infrastructure, trainer–serving interaction, environment abstractions, sandbox execution, scheduling strategies, and the tradeoffs between on-policy and off-policy training. We will examine key design choices, practical engineering considerations, and emerging techniques and recipes for scaling multi-turn agent training, drawing lessons from recent open-source and industry systems.

### One Model Definition, Many Accelerators: Scaling vLLM Across Hardware Without Forks
Speakers: Thomas Parnell, Richard Zou
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257448
Open‑source inference projects like vLLM sit at a critical crossroads. On one hand, there is intense pressure to deliver state‑of‑the‑art performance for a small set of mission‑critical “head” models on rapidly scaling GPU infrastructure. On the other, a long tail of models and a diverse hardware ecosystem depend on continued support.

Balancing these demands is challenging. The abstractions that once enabled portability across models and hardware are being reworked—or removed—to unlock peak performance for frontier workloads. At the same time, users of tail models and alternative accelerators still expect support without slowing innovation.

In this talk, we present hardware‑agnostic model definitions for vLLM: a design approach that decouples model logic from hardware execution paths, enabling the same model definition to run efficiently across accelerators without forking or per‑platform maintenance.

Our approach relies on three pillars: (1) compatibility with torch.compile, (2) well‑defined extensibility hooks, and (3) strict isolation from hardware‑specific paths. We will show how this design supports Intel Gaudi/HPU and IBM Spyre without hardware‑specific modeling code.

### Future of Distributed Communication in PyTorch: New APIs for Fault Tolerance, RDMA and Extensibility
Speakers: Tristan Rice, Kapil Sharma
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256220
As training scales to hundreds of thousands of GPUs across heterogeneous hardware, PyTorch's distributed communication layer needs new capabilities: fault tolerance without job restarts, direct memory access across nodes, observable collectives, and plug-and-play backend registration.

This talk walks through the new APIs hands-on:

\* Fault Tolerance — torch.distributed.reconfigure() enables live process group reconfiguration after rank failures, keeping jobs running.
\* Window APIs — One-sided RDMA put/get for zero-copy communication for workloads such as RL.
\* Composable Hooks — Customizable logic and logging for all collectives, collective tracing, NaN detection, and more across all backends.
\* Backend Extensibility — New backends ship as pip-installable wheels via entry_points, acting as first-class citizens without patching PyTorch.
\* Clean Interfaces — Improved backend APIs lowering the barrier for advanced users and hardware vendors.

We've incubated these features in TorchComms and are now upstreaming them directly into torch.distributed so every user benefits with zero migration cost.

### JIT Kernel Compilation: How Modular writes fast kernels for any hardware
Speakers: Stefan Lindall
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257411
H100, B200, MI300, MI355, TPU, Trainium, .... The future of AI runs on many different hardware chipsets and capabilities. This talk gives a broad overview of Modular's Mojo programming language, graph compiler, hardware abstractions, and model authoring APIs. Learn how MAX ships high performance AI models and kernels for _any_ hardware, automatically compiling fused kernels specialized for the exact model being executed and hardware available.

### Beyond Size and Stride: Unleash Performance with Device-Aware Tensor Layouts
Speakers: Olivier Tardieu, Avery Blanchard
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256241
In this talk, we review the many ways, both obvious and less obvious, that tensor layouts affect performance — spanning cache locality, memory bandwidth utilization, NUMA effects, and hardware-specific tiling constraints. PyTorch tensors encode only minimal information about these physical considerations — size, stride, and storage offset — which is insufficient to capture the hardware layouts required by modern accelerators.

To address this, we introduce a tensor layout extension that enables device-aware specialization of tensor layouts, including tiling and NUMA-aware placement. This lightweight extension preserves standard PyTorch tensor semantics by introducing a separate, more expressive physical layout, allowing precise control over these layouts without modifying existing PyTorch code.

Finally, we report our experiences using this approach in practice. We demonstrate how torch.compile (Inductor) leverages these controls to automatically adapt layouts to the target device and transparently adjust computations. We discuss the resulting performance benefits, limitations, and lessons learned.

### Observability Tooling for Cudagraph Workloads
Speakers: Natalia Gimelshein, Driss Guessous
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255975
CPU overheads have become a particularly urgent problem with the Blackwell generation of GPU hardware. One of the most common ways of alleviating it is using cudagraphs. Pytorch has been working on improving overall UX with cudagraphs, this talk will focus on observability improvements.

Cudagraph profilea look bare - just the kernels, no detailed information present in regular profiles

Cudagraphs exacerbate already existing visualization inconveniences - overlapping kernels get dropped from profiles, stream assignments are garbled. Tracking memory used by cudagraphs is inconvenient because it goes to a separate pool and existing visualizations don’t handle it properly.

Cudagraphs also have one important advantage - we replay the same captured work. If we capture enough information during graph capture time, we will be able to cross reference it later to the runtime information collected during replay.

We will discuss what utilities pytorch provides to make profiling and monitoring runtime performance and memory usage of cudagraph workloads as information-rich as possible, with as low overhead as possible, including nearly zero-overhead always on monitoring.

### Nested Graph Breaks: Reducing the Cost of Graph Breaks in torch.compile
Speakers: William Wen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256035
Graph breaks in torch.compile trade off compile errors for performance hits. Due to previous TorchDynamo technical limitations, a graph break in a function call O(N) layers deep (a nested graph break) caused O(N) duplicate graph breaks, O(N) graphs being traced, and O(N^2) frame traces. We have implemented nested graph break support in Dynamo, reducing the cost of a nested graph break to O(1) duplicate graph breaks, O(1) graphs traced, and O(N) frame traces, resulting in larger captured graphs (thus, more opportunities for optimization), fewer graph breaks, reduced Dynamo trace time, and improved debuggability.

### rocSHMEM Symmetric Memory in PyTorch for AMD GPUs
Speakers: Prachi Gupta
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256215
Mixture-of-Experts (MoE) models are increasingly bottlenecked by all-to-all token dispatch and combine rather than the expert computation. PyTorch symmetric memory addresses this by issuing communication from within device kernels, including Triton, allowing overlap with computation. To date it has been available only on NVIDIA, backed by NVSHMEM.

This work extends that capability to AMD GPUs through rocSHMEM, which is now available in upstream PyTorch. We describe how rocSHMEM's device-side OpenSHMEM API is exposed as Triton-callable primitives, including one-sided put/get, non-blocking get, put-with-signal, and wait-until, enabling a kernel to initiate its own communication. We discuss the AMD-specific engineering: per-architecture device-bitcode linking and post-compile HIP-module initialization, organized behind a backend-agnostic layer shared with NVSHMEM so that a single Triton kernel runs on both AMD and NVIDIA. Using these one-sided RMA and signal/wait primitives, all-to-all dispatch and combine are constructed within the kernel and overlapped with expert computation. We conclude with a comparison against RCCL host-driven all-to-all on representative MoE workloads.

### SkyRL: Democratizing Scalable RL Training
Speakers: Sumanth Hegde, Eric Tang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1345867
Agents have taken center stage in 2026, with ever-growing interest from companies in training custom agents with reinforcement learning. As agents shift to longer horizon, multi-turn interactions, the systems challenges and requirements on underlying training infrastructure have also evolved. SkyRL is a modular, performant RL library built to meet this growing demand for customization and scalability. This talk traces where SkyRL started — a set of modular APIs decoupling training, inference, and environments orchestrated with Ray— and where it is today. We will walk through:

 \- How SkyRL provides scalable fully async RL training on 350 billion+ parameter MoE models with Megatron and vLLM
 \- SkyRL's multi-tenant Tinker Engine, which allows researchers to efficiently use their own hardware for RL training while using Tinker's flexible training APIs to iterate on recipes
 \- SkyRL's redesign towards HTTP-based APIs for scalable inference, and our contributions of native RL APIs to vLLM
 \- Community recipes built on top of SkyRL including large MoE training on long-horizon tasks, custom recursive language models, and more.

\*******************************

_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Portable PyTorch Across AI Accelerators: A Triton Operator Stack from Eager Mode to vLLM
Speakers: Yonghua Lin
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256909
In PyTorch, deploying the same model across different AI accelerators is still far from portable. Developers still face vendor libraries, missing kernels, framework patches, runtime differences, and numerical surprises.
This talk shares lessons from building FlagOS, an open-source system stack that closes this gap with a Triton-based operator, compiler, and runtime layer for PyTorch. We will explain how FlagGems implements PyTorch eager-mode operators and LLM-critical kernels in Triton, how it integrates through the PyTorch dispatcher, how the augmented Triton compiler FlagTree enables architecture-aware performance optimization, and how the same operator layer connects to vLLM through the unified multi-backend plugin vllm-plugin-fl.
FlagOS has been tested on 20+ AI chips and architectures, including NVIDIA GPUs, non-CUDA AI accelerators, and ARM CPUs. It has enabled Day-0 adaptation of frontier open models such as Qwen3.5, MiniMax-M3, MiniCPM-5, and DeepSeek-V4, with 5–40% inference performance improvement over original vendor adaptation. Our goal is to share a practical path and lessons toward a PyTorch ecosystem where new models and accelerators can meet with much less friction.

### Efficient MoE LLM Inference on Arm with vLLM and OpenVINO
Speakers: Abhishek Jain, N Maajid Khan
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257004
vLLM is a key PyTorch Foundation component for high-throughput LLM serving via continuous batching, prefix caching, and chunked prefill. Efficient CPU deployment is vital for scalable AI but challenged by dynamic sequences, large KV caches & matrix ops. Unlocking vLLM potential on Arm CPUs demands deep hardware-aware optimization
We optimized vLLM with the OpenVINO backend for Arm CPUs, adding SVE-optimized SDPA & Paged Attention, U8 KV-cache quantization to reduce memory bandwidth, op-fusion to minimize data movement & KleidiAI integration with optimized threading for efficient 8/4-bit inference
Building on this inference stack, we target MoE models, hindered by varied expert sizes and memory bandwidth bottlenecks. We introduce a NUMA-aware GatherMatMul operator that fuses dynamic token/expert selection(gather) with MatMul, leveraging KleidiAI for 8/4-bit execution. It consumes indexed data directly, eliminating temp buffers & scaling efficiently to dual-socket systems
Benchmarks on AWS Graviton3e show ~2x throughput on GPTOSS/Llama models. In this talk, we present the unified stack integrating runtime, graph & Arm-tuned kernel optimizations for efficient, scalable LLM/MoE serving

### Integrating the IBM Spyre Accelerator
Speakers: David Grove, Antoni Viros i Martin, Avery Blanchard
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256168
Torch-Spyre is an open source project that provides a PyTorch PrivateUse1 device with OpenReg, including an Inductor backend, for the IBM Spyre Accelerator. IBM Spyre is a high-performance energy-efficient AI accelerator featuring 32 AI-optimized compute cores each with on-chip interconnect and compiler-managed scratchpad memory.

The IBM Spyre Accelerator can now run thousands of models from Hugging Face and vLLM, thanks to a deep integration with PyTorch enabled via the PrivateUse1 interface and Inductor. The talk will cover the state of the Torch-Spyre project, describe key functional enablement and performance improvements made in 2026 and contributions made back to PyTorch to enable such a tight integration.

Providing the expected PyTorch programming model and user experience on a dataflow accelerator while also achieving our performance goals was challenging.  We will discuss key items such as enabling device-specific tensor layouts and scratchpad optimized tiling, with an emphasis on how our solutions integrate with upstream PyTorch.  We hope this will be of interest to the community and enable other out-of-tree accelerators to more easily achieve deep PyTorch integration.

### Five Bottlenecks, Five Fixes: Systematic Performance Diagnosis for PyTorch Distributed Training
Speakers: Paulo Aragao, Aravind Neelakantan
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1254803
Performance tuning distributed PyTorch training shouldn't be dark art. We present a systematic diagnostic methodology backed by five real case studies: (1) DataLoader delivering 1.2% GPU utilization — 83x gain by switching to memory-mapped indexed binary format; (2) unnecessary pipeline stages in torchtitan causing 28% throughput loss; (3) why 0.4% network utilization with MoE expert parallelism is a pipeline bubble, not a network problem; (4) communication-compute overlap analysis comparing FSDP2 vs pipeline parallelism producing completely different torch.profiler traces on identical hardware; (5) achieving 6.8x end-to-end improvement through structured profiling for a production autonomous driving model.

Each case study maps to our diagnostic decision framework: compute-bound, memory-bound, communication-bound, or I/O-bound — with specific torch.profiler signatures, NCCL debug patterns, and targeted PyTorch-level fixes. You leave with a repeatable checklist applicable to any distributed training workload.

### Unlocking PyTorch for Dataflow Accelerators: An Open-Source Kernel Tile IR and Dataflow Scheduler
Speakers: Prasanth Chatarasi, Viji Srinivasan, Swagath Venkataramani
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257807
Programmable dataflow accelerators — IBM's Spyre, Meta's MTIA, Google's TPU, and Amazon's Trainium — are emerging as the dominant paradigm for AI inference. Existing tile-based IRs and schedulers lack support for distributed scratchpads, inter-tile communications, and provide no first-class model for pipelined execution across distributed, asynchronous engines — leaving teams to build custom, non-reusable solutions along with no open-source path from PyTorch's TorchInductor.

We present KTIR (Kernel Tile IR), an open-source, MLIR-based tile IR extending data-parallel abstractions with support for distributed scratchpads, inter-tile communication, and also serving as a compilation target from Triton and Helion with extensions for kernel authoring. We then introduce an open-source dataflow kernel scheduler lowering KTIR into a dataflow representation where pipelined execution across asynchronous engines is first-class. The scheduler is architecture-agnostic, driven by an architecture specification, targeting any dataflow accelerator.

KTIR and the Scheduler are being open-sourced and integrated with PyTorch via TorchInductor, powering IBM Spyre accelerator deployed in IBM's systems.

### XCCL: Scaling PyTorch Collectives to Exascale on Intel GPUs with TorchComms
Speakers: Panagiotis Kourdis, Tanima Dey
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1258012
At the 2025 PyTorch Conference, TorchComms was introduced as a next-generation distributed communication library for scalable, fault-tolerant, heterogeneous AI training. XCCL extends that vision with native Intel GPU support through a new in-tree backend built on Intel’s oneCCL library. This talk covers XCCL’s journey from backend integration to validation on Aurora, Argonne National Laboratory’s exascale supercomputer. Running TorchTitan and other AI workloads, XCCL achieved over 90% scaling efficiency across thousands of nodes, demonstrating reliable large-scale PyTorch training on Intel GPUs. We will highlight key engineering innovations, including a stream-ordered asynchronous execution model that overlaps computation and communication for improved scalability and utilization. We will also discuss bridging gaps between PyTorch collective semantics and oneCCL, plus the CI and testing strategies combining mock-based validation with real Intel hardware testing.  Attendees will gain practical insight into building a production-grade PyTorch accelerator backend. We will also compare XCCL with NCCL and RCCL and share lessons learned from deploying XCCL at exascale on Aurora.

### Static Tensor Shape Checking for PyTorch with Pyrefly
Speakers: Steven Troxler, Avik Chaudhuri
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256337
\# Abstract

Static tensor shape checking in the Pyrefly type checker: see tensor shapes as inline hints, catch mismatches immediately.

\# Why this matters

Shape errors are the #1 bug in ML: They account for 45% of
DL program failures [1], and most crashing faults only manifest at execution time [2]

torch.compile makes shapes critical: Shape mismatches commonly cause slow recompilations

Community is reaching for solutions: jaxtyping (5M+ monthly downloads) provides runtime checks. But this is slow and can interfere with torch.compile. Static analysis is near-instant.

\# Outline

\- The problem: Why shapes are hard to track
\- Demo: Immediate feedback for humans and agents.
\- The design: Symbolic integers, `Tensor` and `Dim`
  types, a shape-transform DSL
\- Evaluation: 28 real models (LLMs, vision, recommenders, RL)
\- AI-assisted annotations: A Claude skill

\# Speakers

Avik Chaudhuri: Pyrefly, Triton, Pytorch compiler

Steven Troxler: Pyrefly, PEP 698, typing summit host

\# References

\- Docs: https://pyrefly.org/en/docs/tensor-shapes/
\- [1] Chen et al., "Tensor Shape Faults in DL Systems," 2021.
\- [2] Xiao et al., "Tensfa: Repairing Tensor Shape Faults," 2021.

### vLLM KV Cache Management for Model-Specific Requirements
Speakers: Xiyuan Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253418
As model architectures become more diverse, vLLM’s KV Cache management needs to move beyond a fully generic planning strategy. Complex models such as MLA, SWA, Eagle, and DeepSeek-V4 may have different cache types, grouping rules, and tensor layouts, which are difficult to handle cleanly with one unified mechanism.

The current challenge is that model-specific requirements can easily become special branches inside core KV Cache utilities, increasing complexity. Different models may need customized spec grouping, block size derivation, cache tensor creation, and max_model_len adjustment.

To address this, vLLM can introduce a model-customized KV Cache Planner, which turns KV Cache management into an extensible “default planner plus model-specific planner” architecture. It reduces core-module complexity, improves model integration, enables more accurate memory planning, and enhances stability and scalability in long-context, high-concurrency, prefix-cache, chunked-prefill, and agentic workloads.

### TorchNeuron: Native PyTorch RL on AWS Trainium - From Research to Production Without Compromise
Speakers: Yahav Biran, Alex Nails
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1248603
TorchNeuron is an open-source native PyTorch backend for AWS Trainium preserving the complete PyTorch experience through PrivateUse1 — researchers run unmodified code by changing .to('cuda') to .to('neuron').

Attendees will learn how TorchNeuron delivers:
\- Native distributed training and inference with FSDP, DDP, and custom TP+SP parallelism via standard torch.distributed
\- Colocated TorchTitan integration — a TorchTitan learner trains eagerly and debuggably while SGLang serves a compiled engine on the same weights
\- Heterogeneous disaggregated Miles integration — an SGLang TorchNeuron worker generates rollouts while a Miles trainer takes steps on NVIDIA
\- Per-step weight sync — 29.5 GB HBM-to-HBM over EFA/RDMA each step, refit into a live engine without recompilation, and the trade-offs in each topology
\- Custom NKI kernels — flash self-attention with on-chip memory management via Higher Order Primitives

We demonstrate GRPO post-training on the DAPO Math task for Qwen3, in both the colocated TorchTitan and disaggregated Miles configurations.

### Open Source Reinforcement Learning with Agent Harnesses
Speakers: Ben Burtenshaw
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253573
I maintain OpenEnv, an interoperability layer that standardizes how reinforcement learning environments are published, deployed, and consumed. It is co-owned by Hugging Face, Meta, Unsloth, Prime Intellect, Modal, Nvidia, and Mercor, and others.

An RL environment is the system an agent acts in and gets feedback from. Like a terminal, a browser, a game, an API. Frontier labs train models with their harness, so the two fit together like hand and glove. The open ecosystem is way more diverse. Model, harness, and trainer are vendored separately, with no shared way to publish an environment and run it against an arbitrary trainer and harness combination.

OpenEnv fills that gap. Environments expose a consistent API, serve over HTTP or WebSocket, package with Docker, and speak MCP. Harness, trainer, evals, and reward definitions stay in their respective libraries, such as TRL, verifiers, and harbor.

This talk shows the interface end to end, why it stops short of reward, and how it lowers the barrier to RL. A developer with one GPU can fork an environment, run it locally, train against it, and contribute it back.

You will leave this talk able to do the same, with a demo to try out.

### PyTorch for Agentic AI: Scaling Heterogeneous Systems from CPU to XPU
Speakers: Eikan Wang, Huma Abidi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291520
As Agentic AI workloads become increasingly heterogeneous and system-intensive, performance depends on more than GPU throughput alone. These workloads require substantial CPU resources for orchestration, tool execution, scheduling, preprocessing, postprocessing, networking, memory management, and CPU-GPU coordination, driving infrastructure toward more balanced CPU/GPU configurations, often approaching a 1:1 ratio. This session highlights Intel's upstream-first strategy for enabling standard PyTorch workflows while delivering deep optimizations across Intel Xeon processors, Intel GPUs, and the software stack that connects them. We will discuss how Xeon provides the system foundation for agentic workloads, showcase Intel GPU optimizations for agentic AI, and demonstrate how Intel's open heterogeneous platform enables scalable AI deployment across data center, client, and emerging inference environments.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### From Weeks to Overnight: Autonomous Day-0 Kernel Bring-Up with Agent Pipelines
Speakers: Juan Muneton Gallego
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256713
GPU kernel development for LLM inference is repetitive yet expert-dependent: profile, analyze bottlenecks, generate code, verify correctness, and iterate. When new hardware arrives, the entire cycle restarts across dozens of operators. General-purpose AI coding agents fail here due to domain knowledge gaps, context degradation over long sessions, and rabbit-hole behaviors where a single build error dominates attention. This talk presents a pipeline-driven autonomous system that encodes the kernel optimization loop as a deterministic workflow — Profile, Analyze, CodeGen, Verify, Fix, Benchmark, Evaluate — with specialized agents at each stage operating in isolated contexts. Hardware-specific optimization knowledge is selectively injected per stage, and a long-term memory captures what worked across runs, creating a flywheel where each optimized kernel improves the next. We demonstrate the system on real vLLM inference workloads, show how context isolation eliminates the rabbit-hole problem, and report kernel bring-up and optimization cycles reduced from weeks to overnight unattended runs.

### Building Portable, Composable Local Agents with ExecuTorch
Speakers: Mergen Nachin, Digant Desai
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257786
Models are reaching an inflection point where local agents can provide genuinely useful on-device experiences, driven by privacy, cost, latency, and offline needs. At the same time, the ecosystem will not be won by one closed stack. Useful agents will be composed from open standards and open frameworks: agent harnesses, tool protocols, real-time voice interfaces, local model servers, memory systems, and sandboxed execution environments.

In this talk, we show how ExecuTorch can be a vital runtime substrate in this ecosystem: fast large-context execution, memory-efficient multi-session serving, and portability across models, hardware, and deployment targets. The value proposition is broader than running one chat model on a laptop. ExecuTorch is designed to support many model types, including multimodal experiences, across consumer devices, mobile phones, workstations, embedded systems, and future private agent appliances. The goal is to make local agents efficient, composable, and portable.

### Dist-MoE: Fused Comm-Compute Kernels & Activation Packing for Speed-of-Light MoEs
Speakers: Sanket Jayant Purandare, Shikai Li
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257887
Distributed MoE performance depends on more than GEMMs: exposed communication, irregular activation sizes, and memory movement. Dist-MoE addresses them as one GPU execution system. Fused CuTe DSL kernels combine communication and tensor-core compute, using persistent warp-group pipelines to overlap dispatch, grouped GEMM, SwiGLU, and combine at tile granularity. Its CUDA-graphable memory runtime packs dynamically sized MoE activations into stable-address arenas, manages scratch space, and makes device-side save-or-recompute decisions without changing graph topology. This sustains efficient execution under variable routing. The architecture spans BF16, MXFP8, and NVFP4, with layout-aware quantization, scale management, transposed weight paths, and FP32 accumulations where numerics require it. We explain the forward and backward pipelines from peer HBM to warp-level execution, the activation planner and dynamic recomputation protocol, and the PyTorch integration that preserves bitwise parity with the production kernels. Dist-MoE brings a production distributed expert engine to open source: fast, memory-efficient, configurable, and designed to scale without hiding its execution model.

### Before the Loss Spike: Training Alignment for Precise PyTorch Debugging at Scale
Speakers: Ziming Zhou
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1199488
Large-scale PyTorch training often fails in the most frustrating way: a tiny bug corrupts a few values, nothing obviously breaks, and only much later the run starts to drift. Loss curves tell you something changed. They rarely tell you where it first went wrong.

In practice, engineers often debug by comparing a suspect run against a known-good reference: the same checkpoint, the same seed, or a version before a stack change. But loss curves and gradient norms are still too coarse to pinpoint.

This talk introduces training alignment: a way to systematically compare two supposedly equivalent training runs and recover the longest prefix where they still compute the same tensors. The first mismatch becomes a precise debugging pivot. In OpGuard, we realize this with bitwise alignment at semantic operator boundaries, turning debugging from guesswork into finding the first wrong tensor.

I’ll show how this works in real production PyTorch systems with fused kernels, distributed collectives, async streams, graph capture, etc. With lightweight tensor fingerprints and schedule-tolerant trace alignment, we can localize semantic drift far more precisely than loss or gradient monitoring.

### Keynote: Building What’s Next in Open Source AI
Speakers: Mark Collier
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1303522
The connections across the open source AI ecosystem are getting stronger, and the possibilities are getting bigger. More hardware can participate, workloads can move across more environments, frontier models can be trained and customized at greater scale, and a growing global community can contribute to the technologies shaping what comes next. AI itself is also beginning to change how these systems are built and improved, creating a new set of opportunities and challenges for the community. Day 2 looks ahead to those next frontiers and the role open collaboration can play in reaching them. The goal isn't simply to make AI more powerful or move faster. It's to expand who can build, contribute, experiment, and shape the future of intelligence so that progress continues to come from many people, projects, and organizations rather than a few.

### Keynote: Workload Fungibility in the Agentic Era: Bringing Native PyTorch to Cloud TPUs
Speakers: Bill Jia, Zongwei Zhou
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298062
PyTorch is fundamentally designed to embrace hardware heterogeneity.
From the flexibility of eager mode to the extreme performance of torch.compile and TorchDynamo, the PyTorch stack empowers developers to build truly hardware-agnostic models. Coupled with advanced distributed APIs like FSDP2, extensive parallelism strategies, TorchTitan, inference engines such as vLLM and SGLang, and Helion, PyTorch provides the definitive ecosystem for scaling AI workloads across any silicon.
Today, we are thrilled to showcase this architectural vision in action with a deep dive and some real-world use cases of TorchTPU, now publicly available in OSS.
Co-developed in close partnership with PyTorch core maintainers, TorchTPU showcases PyTorch’s inherent workload fungibility and a production-ready lowering path. By seamlessly integrating with the core PyTorch ecosystem - from modeling in HuggingFace Transformers, training in TorchTitan, and serving in both vLLM and SGLang - TorchTPU allows teams to achieve out-of-the-box pretraining, fine-tuning, and serving performance using the PyTorch code they already know. It is already powering production workloads at top-tier AI labs globally.
To further accelerate PyTorch’s multi-hardware reality and leading position among AI practitioners, we are also introducing a new paradigm of agentic developer experiences. We will demonstrate how long-horizon agentic workflows can seamlessly migrate complex model workloads from GPUs to TPUs. Beyond migration, we’ll explore how you can leverage these agents for autonomous performance hill-climbing—tackling complex, low-level optimizations like quantization, custom kernel generation, and advanced sharding strategies to profile, debug, and extract maximum hardware utilization with minimal manual intervention.
Join us as we explore the frontier of PyTorch hardware heterogeneity, and discover how TorchTPU and agent-driven development can radically simplify your path to high-performance AI.

### Keynote: From Silicon to Models at Scale
Speakers: Priya Nagpurkar
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298073
"Enabling new hardware, supporting thousands of models, and scaling inference takes progress across the open-source AI stack. This keynote shares how IBM and Red Hat are contributing across the PyTorch ecosystem to make that happen.

We’ll highlight work bringing IBM Spyre to the PyTorch compiler and vLLM, how AI tools are helping scale model enablement to thousands of models, and a look ahead at next-generation Spyre hardware. We’ll also cover Red Hat’s contributions to PyTorch and CI/CD infrastructure for out-of-tree accelerators, helping hardware backends keep pace with the community. Finally, we will touch on our journey with the llm-d community to enable efficient distributed inference at scale."

### Keynote: Scaling Large Frontier Models Training with DeepSpeed
Speakers: Zhipeng Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1314372
DeepSpeed is among the most popular open-source training optimization libraries that enables memory efficient, scalable and most competitive distributed training performance for large models up to trillion parameters. DeepSpeed’s pioneering work on ZeRO (Zero Redundancy Optimizer) introduced a new paradigm for eliminating memory redundancy in distributed training. The techniques have since been broadly adopted across all the training ecosystem and have become foundational to the training of today’s frontier models.

In this talk, I will share some of the latest technical advances from the DeepSpeed team that continue to push the frontier of large-scale model training. In particular, I will highlight our work on model-systems co-design and optimizations, which enable DeepSpeed to deliver high performance across diverse model architectures, workloads, and accelerator platforms.

I will also discuss the continued development of the DeepSpeed open-source community and how we collaborate with model developers, hardware vendors, and AI infrastructure partners to expand DeepSpeed’s adoption and enable emerging large-scale AI workloads.

### Keynote: Open Science and AI Foundation Models: Allies in the Pursuit of Knowledge
Speakers: Rachad Alao
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298057
This talk will discuss how open science provides a powerful paradigm to ensure new AI foundation models are developed and deployed in a way that is transparent and secure, while enabling speed and scale of innovation across the ecosystem.

### Keynote: AI Model Customization Platform
Speakers: Yiwei Song
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298069
We are sharing our vision and progress of building an LLM post-training platform which allows the customers to customize the open weights models for their business usecase, to improve accuracy and reduce inference cost.

### Keynote: Linear Algebra for the Age of Research
Speakers: Mark Saroufim
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1298055
This talk introduces the linear algebra kernels we are working on and why these long-standing problems still deserve attention. I will discuss what the kernels do, where the performance bottlenecks are, and why accelerating these routines matters for research. The talk also highlights how AI tools and open technical communities are helping people make faster progress on problems studied for decades.

### Contributing to Inference OSS That Won't Stand Still: A BoF on vLLM, llm-d, and the Moving Target
Speakers: Maroon Ayoub, Nili Guy
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257610
Contributing to fast-moving inference projects like vLLM and llm-d is not like contributing to stable infrastructure. The architecture shifts under you, decisions happen across Slack threads and weekly syncs, "stable" APIs aren't, and the docs are often the code. Multiple companies have stakes, sometimes competing. Newcomers bounce off the velocity; even experienced contributors struggle to find where decisions are actually made.
This BoF gathers contributors, maintainers, and would-be contributors to compare notes on how to engage with projects that won't stand still. How do you land a first PR when main moves daily? How do maintainers onboard people without slowing down? How do cross-company projects make technical decisions in the open - and how do you get into the room where they happen? What works, what doesn't, and what nobody warns you about.

Bring your own war stories. We'll surface patterns, anti-patterns, and the unwritten rules that make these communities navigable - and leave with a shared sense of how to contribute to inference OSS without burning out or giving up.

Located across from the PyTorch gear store.

### Meet the Developers of vLLM
Speakers: George Novack, Nick Hill
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1340810
Join PyTorch experts for an interactive “Meet the Developers” session – a chance to learn in a small group setting and ask your most pressing questions. No sign-up required – just drop in and get real answers from the people building the tools.

Located in front the Meta booth.

### Demo: PyTorch Ecosystem Running Natively on Trainium: Reinforcement Learning - TorchTitan & Monarch
Speakers: Maen Suleiman
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291526
TorchNeuron, the native PyTorch backend for AWS Trainium, makes Trainium a PyTorch device, so libraries from the PyTorch ecosystem run on it. In this live demo, we run reinforcement learning on Trainium. TorchTitan trains in eager mode and with torch.compile, and vLLM-Neuron generates rollouts with torch.compile, both through TorchNeuron. Monarch orchestrates the two, and TorchStore syncs weights between them. We show how TorchNeuron enabled their integration with Trainium.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: The Engineering Behind 3-Second Video Generation
Speakers: Ali Taha
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1314406
Wan 2.2 can now generate a five-second video in less than three seconds, a 53.6x improvement over the baseline implementation. Crossing the real-time threshold turns video generation from a batch workload into an interactive creative loop. The work combines three performance techniques: timestep distillation, custom kernel engineering and four-bit quantization. This talk provides a breakdown of techniques across model, kernel, and runtime that unlock real-time inference for video generation models.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Beyond the Brrr: Building a Unified Ecosystem for Optimized Kernels
Speakers: Ben Burtenshaw
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1252682
Modern deep learning models are hitting a performance wall. While GPUs offer teraflops of compute, generic operators often utilize only 20-30% of available performance. Custom kernels—the low-level functions executing operations like matrix multiplication—can unlock this potential, but traditionally require managing CUDA toolchains, device-specific code, and complex build systems.

This talk bridges low-level optimization with high-level Python productivity. We'll explore why kernel optimization matters for real workloads, dissect the friction points that make custom kernels difficult to maintain, and introduce Hugging Face's new Kernels library—a solution that makes discovering and using optimized kernels as simple as loading model checkpoints.

Attendees will learn to identify performance bottlenecks in their models, swap generic operations for optimized kernels without writing CUDA, and leverage the Transformers integration that's already delivering 2-5x speedups in production. We'll demonstrate practical examples and discuss the architectural patterns that enable seamless hardware portability.

### FlexShard: Pluggable Sharding Placements for Matrix Optimizers and Block-wise Quantization
Speakers: Wei Feng, Anshul Sinha, Ailing Zhang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256015
FSDP1, FSDP2, and newer variants often differ mainly in sharding strategy, yet each has historically reimplemented the same runtime machinery: unshard/reshard hooks, collective scheduling, buffer management, and gradient reduction.

This talk introduces FlexShard, a prototype PyTorch abstraction that decouples parameter sharding from this runtime via a small Placement contract, where each Placement owns not just its layout but its collective lifecycle.

FlexShard provides FlatShard, row/column-wise Shard, Owned, and RaggedShard on one torch.compile-traceable runtime. Two novel use cases become possible that FSDP can't express:

(1) optimizer-aware sharding for matrix optimizers like Muon — an Owned placement keeps each matrix whole on one rank, enabling communication-free Newton-Schulz on full parameters;

(2) quantization-aligned sharding for block-wise FP8 all-gather — a tile-aligned RaggedShard quantizes before the gather, moving half the bytes. The same tile-aligned recipe can potentially be extended to FP4.

### TPU agent suite: Accelerating PyTorch Model Onboarding and Inference on Cloud TPUs
Speakers: Sandeep Pokkunuri, Chris Jones
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1301802
The *TPU agent suite* is an open-source plugin for developer environments like Claude Code and Google Antigravity that accelerates PyTorch model onboarding and inference tuning on Cloud TPU v6e and v7x. Grounded in a TPU knowledge base and empirical tuning playbooks, it compresses model onboarding from weeks to hours, unlocking measurable serving throughput gains on frontier OSS transformer architectures.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### DeepSpeed Is Not Just ZeRO: Tensor, Sequence, and Expert Parallelism with ZeRO-Level Usability
Speakers: Masahiro Tanaka
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257990
DeepSpeed is widely used for the memory efficiency and usability provided by ZeRO. While ZeRO is one of DeepSpeed's most recognized contributions, DeepSpeed also supports a broader set of parallelism techniques beyond data parallelism, including tensor, sequence, and expert parallelism.
In this talk, we will introduce DeepSpeed's AutoTP, AutoSP, and AutoEP capabilities for tensor, sequence, and expert parallelism. Like ZeRO, these features are designed to be usable with existing model implementations, including many Hugging Face models, without requiring users to rewrite the model code around a specialized parallelism stack. They can also be combined with ZeRO, allowing users to add tensor, sequence, or expert parallelism while retaining ZeRO's memory efficiency and usability. We will explain how to enable these features, how they work under the hood, and where each parallelism strategy fits. We will also share benchmark results from representative use cases, including large dense models, long-context training, and MoE workloads.

### Inside the PyTorch Ambassador Model: How Ambassadors Grow PyTorch Adoption & How You Can Become One
Speakers: Sahdev Zala, Sonny Mupfuni
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1306148
For many new contributors or adopters, the entry point into the PyTorch ecosystem is not any one resource; it’s the local community. The PyTorch Ambassador Program brings together rising community leaders from around the world to support them in activating, connecting, and growing interest in PyTorch at scale. The program was launched in 2025 by the PyTorch Foundation.

This session offers a cross-country view of the PyTorch Ambassador Program, drawn from the ambassador activity reports spanning: what ambassadors built, the challenges they hit, and the results they produced. Beyond the numbers, it distills a reproducible model: recruit, educate, level up, then help local users into upstream contributors and examines how that model adapts to different contexts, from language and local ecosystem maturity to uneven access to compute.

Attendees will gain a clear understanding of how to engage more deeply with the PyTorch community and position themselves for the Ambassador role through advocacy, education, and contribution. Whether you are an active contributor or someone looking to expand your role in the PyTorch community, this session offers actionable insights to help you take the next step to becoming a PyTorch Ambassador.

### Building Highly Efficient Inference System for Recommenders Using PyTorch
Speakers: Lu Fang, Ilina Mitra
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1243435
We discuss the design of a high-performance recommendation inference system built with PyTorch, which serves as the backbone for Meta’s most critical machine learning workloads. Powering global surfaces including Feed, Ads, Instagram, Reels, Stories, and Marketplace, the system manages a diverse array of ML architectures, ranging from sophisticated extensions of the foundational Deep Learning Recommendation Model (DLRM) to cutting-edge, novel modeling techniques such as HSTU (Hierarchical Sequential Transducer Unit), Wukong, and more.

We cover the end-to-end workflow, starting from a trained model definition and its weights, progressing through essential inference transformation steps, including graph capture, model splitting, optimizations (fusion, quantization, compilation, etc.), and serialization. We outline the requirements for a high-performance inference server, emphasizing a lightweight executor, flexible tensor-based APIs, and DAG-based execution model. Finally, we explore advanced optimization techniques crucial for high-QPS, low-latency performance, including GPU/Accelerator inference, C++ runtime, Distributed Inference, AI compilers, request coalescing, and more.

### Deploying PyTorch Models Where Failure Isn't an Option
Speakers: Sarah Mohamed, Ashvant Ram Selvam
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1251868
Your PyTorch model hits high accuracy: congratulations, but this is just the start of deploying it in an aircraft. Aviation standards for AI are still evolving, but groups such as EUROCAE WG-114 and EASA have made great headway recently. Prospective guidance goes beyond model accuracy, requiring that systems detect unfamiliar inputs at runtime, that design decisions trace back to system requirements, and that deployed code behaves the same as the original model.

Using a runway sign detection system as our case study, we'll follow a PyTorch model through the path to deployment in the safety-critical aerospace industry. We'll show how emerging certification guidelines shape each step, from training and validation through system-level simulation to verification of the deployed code.

Attendees will leave understanding what "deployment" means in regulated industries, with practical techniques they can apply outside aerospace. This includes implementing out-of-distribution detection to know when a model is operating outside its training distribution, using runtime safety monitors during system-level simulation, and using formal methods to prove properties of the AI model and system.

### Transformers.distributed: Bringing First-Class Distributed Training to 2.4M+ Hugging Face Models
Speakers: Ferdinand Mom
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253220
transformers.distributed is a new module that brings parallelism natively into Transformers. No separate config files, no wrapper classes, just a DistributedConfig object passed directly to from_pretrained. The goal is to cover the full Transformers ecosystem: 400+ architectures and 2.4M+ model checkpoints on the Hugging Face Hub, with 5D parallelism (data, tensor, pipeline, sequence, and expert) built in. This talk walks through the design decisions that make this possible at scale, how we handle the constant stream of new models being added, and how we keep bitwise correctness and throughput from falling through the cracks. Because the end goal is straightforward: one from_pretrained call that just works, without changing your training loop, whether you're on a single GPU or a multi-node cluster.

### Parametrized Dynamic Shape CUDA Graphs
Speakers: Elias Ellison, Daniel Galvez
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257948
For many CPU overhead-sensitive workloads, CUDA Graphs are a requisite tool for eliminating CPU overhead. When these workloads involve dynamism, using CUDA Graphs can require significant restrucuring, often requiring whole-model rewrites with workarounds like padding, on-device shapes, and re-recordings across a large number of potential shapes.

We show work on support for CUDA Graphs with dynamic shapes. Building upon both parametrized CUDA Graphs, and torch.compile’s symbolic tracing and guard infrastructure, we capture and re-parametrize a single CUDA Graph across dynamic shapes. We showcase both performance wins and reduced cold start times for inference serving.

### Miles: Enterprise-facing Agentic RL Framework
Speakers: Yueming Yuan
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1258156
Miles is an enterprise-facing agentic RL framework for large-scale post-training on PyTorch. As LLM post-training moves from single-turn reward optimization to multi-turn, tool-using, production-grade agents, RL systems must support larger models, longer rollouts, heterogeneous clusters, and continuous iteration without sacrificing stability or debuggability.

This talk introduces the design of Miles and the engineering lessons behind building an RL framework for real enterprise workloads. We will cover its end-to-end training stack for SFT, LoRA SFT/RL, and agentic RL; scalable rollout generation for multi-turn tool-use environments; and integrations with PyTorch, Megatron, and Ray for distributed training. We will also discuss key system techniques such as unified low-precision training across BF16/FP8/MXFP8/INT4, stable MoE RL with rollout/routing consistency, speculative rollout acceleration, and extensible plug-points for custom models, rewards, environments, and deployment pipelines.

Together these make Miles suitable for large-scale post-training and production-level agent workloads. We will share what worked, what was hard, and where Miles is headed.

### What Would a PyTorch Expert Say? Turning Tribal AI Knowledge into a Model
Speakers: Liana Koleva, Teja Pulagam
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1333197
Developing effective AI agents for machine learning requires more than code fluency: it demands the practical expertise needed to diagnose failures, navigate framework behavior, and make sound implementation decisions. This talk presents our approach to building a specialized training dataset that captures this expertise for PyTorch development. We describe how we transform heterogeneous technical records into actionable training examples, addressing challenges such as task reconstruction, solution leakage, and preparation of interaction traces. We then examine the individual contributions of different data sources through supervised fine-tuning experiments on an open-source model. We share practical lessons from dataset construction and fine-tuning, focusing on the choices that make technical knowledge useful for training specialized agents. We also outline planned reinforcement learning work and the path toward deploying the resulting model within an agent harness as an ML expert for customer workflows. Attendees will learn practical strategies for converting scattered technical knowledge into training data, evaluating its contribution to model capabilities, and connecting specialized model training to real-world PyTorch development.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Beyond Collectives: Building Fused Compute-Communication Kernels with PyTorch Symmetric Memory
Speakers: Ke Wen, Natalia Gimelshein, Kapil Sharma
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257030
Collective ops gave PyTorch portable distributed training, but they draw a hard line between compute and communication: a collective is a black box compute waits on. PyTorch Symmetric Memory erases that line, giving every rank a direct window into its peers' GPU memory so communication becomes something a kernel does inline. A practical tour across five themes:

\- Compute–communication fusion: pushing partial results to a peer from inside a kernel, hiding communication behind compute.
\- Flexible patterns: one-sided puts/gets and torch.distributed.TokenSwitch, supporting expert-parallel MoE with autograd for free.
\- DSL support: binding low-level NCCL device primitives into a CUDA DSL (cute-DSL).
\- Profiling & CUDA Graph: new device-side APIs that make fused communication observable, plus CUDA Graph capture for production loops.
\- Community adoption: where Symmetric Memory is landing today.

Attendees leave understanding the programming model and when fusing communication beats a collective. Assumes PyTorch distributed basics; deep CUDA not required.

### Precompile for Training
Speakers: Bob Ren, Aaron Orenstein
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1245005
Distributed training systems today often compile the same model independently on every GPU rank. At small scale this is mostly an inconvenience. At large scale it becomes a major operational cost: thousands of GPUs can remain idle while identical compilation work is repeated across the cluster.

Beyond startup overhead, per-rank compilation introduces deeper systems challenges:

\* Different ranks can make slightly different compiler decisions even when executing the same SPMD program, leading to NCCL hangs and job failures.
\* Large training jobs waste substantial cluster capacity performing redundant compilation work across thousands of GPUs at runtime.
\* Independent autotuning can choose different kernels on different ranks, creating numerical inconsistencies and making debugging and reproducibility much harder.

This talk introduces Precompile for Training, a new abstraction for compiling distributed SPMD programs once and reusing the resulting artifact across all ranks. If every rank shares the same compiled graph artifact, compilation can move ahead of GPU allocation while guaranteeing identical execution and kernel selection across the cluster.

### Scaling Audio AI Infrastructure: Building Voice-Native AI
Speakers: Mu Li, Huapeng Zhou, Lindsey Allen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1258143
Voice-native AI is moving from demos into production, reshaping how we build conversational systems and real-time voice agents. Yet the infrastructure for training and serving these systems still lags behind the mature ecosystem built for text-only LLMs.
This talk takes a system-level view of what it takes to build voice AI end to end.
On the training side, we will discuss the challenges of post-training and aligning voice models, as well as the scaling considerations that are unique to audio.
On the inference side, we will cover what it takes to serve full voice systems and real-time voice agents under tight latency constraints, including how we extended SGLang to support audio workloads.
We will also share practical lessons from building a voice-native stack on PyTorch: what worked, what did not, and which open problems the community still needs to solve.

### Self-Healing PyTorch Training Through Live GPU Migration
Speakers: Pavneet Ahluwalia, Gavin Cohen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1322707
Anyone running large training jobs knows the 3am page: one link flap, GPU fault, or node failure, and the entire job is down. The cause is structural — every training step ends in a collective that needs all ranks. One dead or hung rank stalls the rest until the NCCL watchdog fires, and since a communicator cannot be rebuilt around a missing peer, the whole job aborts.
The standard recovery mechanism, checkpoint and restart, carries a heavy penalty: reprovisioning nodes, restarting the job, restoring the latest checkpoint, and recomputing every step since. A single failure typically burns 45–90 minutes of wall-clock time across every GPU in the job.
Together AI and Clockwork Systems will present the TorchPass powered training failover system, which keeps training jobs running through infrastructure failures. TorchPass reroutes traffic around degraded or failed links and, when a GPU, its memory, or another component fails, live-migrates the affected rank's device and communicator state to a spare resource — resuming from the same step with just a brief pause.
We'll walk through the architecture behind TorchPass, the end to end system from monitoring, health checks to failover and then demonstrate a live multi-node training job making continuous forward progress through injected link flaps and GPU failures. You'll leave with a clear model of when live migration beats checkpoint-restart, and a way to quantify recovered goodput and its dollar value for your own cluster using the ClusterMAX TCO Calculator.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### From torch.profiler to Hardware Cycles: A Practical Profiling Playbook for AWS Trainium
Speakers: Esha Lakhotia, Pinak Panigrahi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257690
You deployed a PyTorch model on AWS Trainium, but it's not hitting the expected performance. Where's the time going? Host overhead, communication stalls, or underutilized compute? Answer these questions using the torch.profiler API, without code changes or separate tooling.

We walk through the profiling workflow:
Capture: a context manager wraps your training/inference loop. Output is a profile covering CPU dispatch, runtime orchestration, and on-device hardware execution.

Navigate from model to hardware: start from the nn.Module hierarchy, drill into which layers dominate wall-clock time. Click through a slow attention block to see the compiled ops. Trace a gap back to Python source line.

Find the bottleneck: the timeline shows hardware engines at cycle resolution. We demonstrate a debugging session where compute cycles were idle waiting on a collective. Framework traces said one thing; the device timeline showed where and why.

Get actionable next steps: AI-assisted analysis identifies  performance bottlenecks and suggests fixes without requiring hardware expertise.

Attendees leave with a playbook they can apply, going from "it's slower than expected" to "here's what to fix."

### Train the Agent, Not Just the Model
Speakers: Sergio Paniego Blanco
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255556
Frontier agents are so capable partly because the model was trained using the very harness it runs in. In this talk, we show, hands-on, how to train open agents end-to-end, using SFT and GRPO in agentic settings, with real code and examples for each stage.

We start with SFT on frontier agent traces, focusing on what agent trajectories look like and what a smaller open model learns from them. We then move to GRPO for tool use, where the model learns through real online interaction with an RL environment we run and control, guided by reward signals.

The final and main focus is harness-driven training. Instead of training the model to call tools directly, a full harness runs inside the training environment and owns its internal loop. We show how we manage episode boundaries in TRL, Hugging Face's PyTorch-native post-training library, rewarding the agent on its results.

You will leave knowing when to use each approach and how to apply it to your own agents with open tools.

### Demo Theater: WideEP NVL72 with Rust Frontend
Speakers: Rain Jiang, Kevin Li
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1361627
This demo showcases WideEP for expert-parallel MoE inference on an NVIDIA NVL72 system, using a Rust-based frontend to run and monitor the workload. It highlights token dispatch and combine across GPUs, along with end-to-end performance.

\****************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Ecosystem Working Group: Unlocking Community Impact Through the PyTorch Landscape
Speakers: Joseph Groenenboom, Chris Hoge
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253136
Created by the PyTorch Foundation in early 2025, the PyTorch Ecosystem Working Group spotlights, through inclusion in the PyTorch Landscape, projects that demonstrate technical excellence and active community engagement in their respective domains. The Landscape includes projects that are both Foundation-hosted and community-hosted. With more than 70 active Landscape projects, including Helion, SGLang, and vLLM, membership creates opportunities for broader impact and recognition within the PyTorch community. In this session, led by the Ecosystem Working Group, you will learn:
      - What the Ecosystem Landscape is and why it matters: how membership drives visibility and community engagement for independent projects
      - How to apply: a lightweight, GitHub-based process that makes it straightforward for projects to apply for ecosystem status
      - How lifecycle management works: what ongoing membership looks like and how the Working Group supports active projects

Attendees will leave with a clear understanding of the benefits of joining the Landscape, the minimum governance standards to qualify for inclusion, and will have the opportunity to meet working group members.

### Making vLLM Faster on Intel GPUs with Triton Kernels
Speakers: Whitney Tsang, Artur Fierka
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255903
vLLM is a serious inference stack for Intel GPUs, and the key open question is no longer basic enablement, but: which kernel strategies actually win on XPU? In this talk, we present our work on Triton kernels for vLLM on Intel GPUs and show where Triton can outperform SYCL on inference workloads.

We focus on the hottest serving paths: unified attention, fused MoE, batched MoE, and the benchmark infrastructure used to study kernel behavior on Intel GPUs. Rather than framing Triton as a portability layer, we treat Intel GPU architectures such as Arc as optimization targets and examine how kernel design changes when memory movement, tiling, fusion boundaries, and launch choices are tuned for XPU behavior.

The talk highlights concrete optimization themes including autotuning, tensor-descriptor-oriented kernel structure, and fusion opportunities such as QK-norm plus RoPE and RMSNorm/SiLU-gate with blockwise low-precision quantization patterns. We discuss where these choices improve end-to-end vLLM throughput and latency, where SYCL remains competitive, and what our results suggest about Triton as a high-performance kernel language for optimized inference on Intel GPUs.

### Demo Theater: dmx-compressor: Accelerating the Development of Kernels for Custom ASIC Hardware
Speakers: Tristan Webb
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1309107
dmx-compressor is a PyTorch 2.0 based quantization framework that allows ML engineers to obtain numerical reference output to validate models running on ASIC hardware. Developing AI/ML hardware involves low-level kernel programming, a very challenging process.

dmx-compressor facilitates a mapping between its own PyTorch based GPU quantization routines and kernel libraries in the d-Matrix Aviator software stack. Aviator encompasses interfaces that model block-floating point hardware circuits, core MatMul operations, as well as various SIMD kernels (such as add, sub, gelu, etc...).

dmx-compressor's PyTorch 2.0 program capture ingest modern PyTorch models, and then its FXIR interpreters substitute standard torch modules with modules from our custom DmxModules library wrapping the hardware interface. dmx-compressor then allows users to measure the numerical error between its own reference GPU implementations and the accurate model of our hardware.

Our approach finds and fixes bugs earlier in the development process, has increased our organizational velocity, and showcases how the modern PyTorch ecosystem works across all layers of the AI stack, from HuggingFace to silicon.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### FlexGEMM: Flexible PyTorch Epilogues
Speakers: Driss Guessous
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1252009
GEMM epilogues are everywhere in modern models: bias, activation, residual adds, alpha/beta accumulation, auxiliary outputs, fp8 scale computation, and gated contractions like SwiGLU. Today, PyTorch users often express these naturally as normal tensor code after an `mm`, `bmm`, or `scaled_mm`, but in eager and often even under torch.compile outputs are usually fully materialized into global memory before running the epilogue.

This talk presents FlexGEMM, a proposed PyTorch frontend for writing flexible GEMM epilogues as ordinary PyTorch functions while giving the compiler a clear contract to fuse them into the GEMM store path when safe.

I’ll cover the API shape, the fail-closed compilation contract, what kinds of epilogues are local enough to fuse, and where the wins actually come from: avoiding extra reads/writes of the GEMM output rather than magic kernel speedups. I’ll also walk through concrete cases like bias+activation, residual epilogues, fp8/scale-output epilogues, and SwiGLU-style contractions, plus the open design questions around split-K, reductions, and layout-changing epilogues.

### Demo Theater: Never Hit Zero: A Live Demo of Surviving Link and Node Failures in PyTorch Training
Speakers: Lin She
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1322762
What if you didn't have to restart from the last checkpoint, wait for minutes, and roll back steps every time your training hits a failure?

This talk shows it live, twice. Mid-run on a real cluster, we pull a network cable from a switch port, on camera, in the server room. LinkPass steers traffic onto healthy links and the job trains straight through it. Then we pull the power cable on a node running the job. TorchPass migrates the affected rank's state to a healthy node, throughput dips but never flatlines, and the job climbs back to full speed on the same training step. No restart, no lost progress, no wasted GPU hours.

The numbers behind the demo come from the published TorchPass benchmark, run at Llama 4 Scout scale on 64 H200 GPUs and independently validated by SemiAnalysis. You will leave with three checks to run on your own cluster: does a failure resume from the same step or restart from scratch, does throughput ever hit zero, and can the claim be verified the way this one was?

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: AI Playground Home Agent: Remote PyTorch AI Workflows from Your Phone
Speakers: Ashok Emani, Qiacheng Li
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291528
Experience AI Playground Home Agent, a new way to access PyTorch-powered AI workflows running on your Intel AI PC from anywhere. Generate character concepts, create 3D meshes, and interact with generative AI applications directly from your phone while computation executes locally on your AI PC.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: Agile Readiness: Leveraging CI Relay for PyTorch Workflows
Speakers: Zesheng Zong
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1361630
Keeping accelerator stacks in sync with fast-moving PyTorch upstream while preserving release quality is a persistent challenge. In this session, we share our practice to deliver stable downstream releases quickly after PyTorch updates without compromising quality. We present CRCR(Cross-Repository CI Relay), a mechanism enabling real-time co-compilation and joint testing between PyTorch pull requests and accelerator backend implementations. By detecting regressions at the PR phase, we cut down version adaptation overhead and achieve robust stability for fast-paced release cycles.

\********************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: TPU Megakernels
Speakers: George Novack
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1360619
This talk and demo introduces Inferact's work on TPU megakernels. We explain why megakernels are a good fit for TPUs, then show our Kimi K3 megakernels running inside vLLM-TorchTPU, serving real-world workloads efficiently end-to-end. We close with a brief look at what's next for TPU megakernel development, and show how you can try TPU megakernels yourself with the open-source vLLM-TorchTPU release.

\****************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Demo Theater: Why is Heterogeneous Computing So Hard and Why Does it Have To Be?
Speakers: Jay Dawani
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291533
Somewhere out there, a GPU, an NPU, and a custom accelerator walk into your ML stack — and none of them speak the same language. Every new chip shows up promising better perf-per-watt, and every time, your team ends up rewriting kernels, re-tuning schedules, and re-learning pain from scratch. It's 2026. Why are we still doing this?

Join Lemurian Labs for a talk about the actual reasons heterogeneous compute is such a nightmare — and the (surprisingly good) news that most of that pain isn't fundamental. We'll dig into where today's compiler and runtime abstractions quietly fall apart, what a truly hardware-agnostic stack has to get right, and why "write once, run fast everywhere" isn't a fantasy — it's an engineering problem we're actively solving.

Come for the hot takes on why your accelerator roadmap keeps costing you sleep. Stay for the argument that it doesn't have to.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### MXFP8/4 pretraining at scale with Torchtitan on AMD Instinct GPUs
Speakers: Liz Li, Shekhar Pandey
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256822
MXFP8 is emerging as a key low-precision format for large-scale foundation model training, delivering higher throughput while maintaining model quality. As adoption grows within the PyTorch ecosystem, enabling portable and scalable implementations across accelerator platforms becomes increasingly important.

In this talk, we present our work enabling MXFP8 training on MI355X through contributions to TorchAO and TorchTitan. MI355X provides hardware support for OCP microscaling formats, including E8M0 blockwise scaling and dedicated MFMA instructions for MXFP8 computation. We also share experiences with MXFP4 and discuss its performance and accuracy tradeoffs.

We describe the optimization of MXFP8 kernels in TorchAO, including scaled GEMM/grouped GEMM, quantization, etc. We compare Triton and FlyDSL implementations and discuss tradeoffs in programmability, portability, and performance.

Finally, we demonstrate end-to-end TorchTitan pretraining using upstream TorchAO kernels and share lessons learned in numerical validation, convergence, and performance tuning. Attendees will gain practical insights into deploying scalable low-precision LLM training with the upstream PyTorch stack.

### PyTorch-Native LLM Serving on TPU: SGLang and vLLM
Speakers: Colin Taylor, Qi Zhou, Angela Yi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256716
We're open-sourcing two platforms built on a new PyTorch native TPU backend (torch_tpu), enabling SGLang and vLLM to run on TPUs.

Rather than building a new serving stack, or porting models to JAX, we focused on making the existing SGLang and vLLM infrastructure work natively on TPU, preserving the schedulers, batching systems, OpenAI-compatible APIs, and torch.compile workflows already familiar to GPU users. Because the serving engines remain upstream, new models and features can run on TPU without requiring separate TPU-specific implementations.

In this talk, we'll cover how it works across the stacks: torch.compile lowering to TPU, Pallas attention (ragged paged attention), tensor and expert parallelism, MoE with grouped matmul, FP8 for large MoE models like Qwen3-Coder-480B, multimodal encoders, prefill/decode disaggregation, and speculative decoding. We'll also share what we learned running this in production, including compile time, device placement under tracing, KV cache layout, and cross-chip collectives.

Both platforms will be open sourced as of this talk.

### From Pixels to Physical Motion: Building World Action Models (WAM) with PyTorch & NVIDIA Cosmos
Speakers: Susie Xia, Ruijie Zheng US, George Kurian
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257041
High-quality robot action begins with a model that understands the physical world: objects, geometry, dynamics, and how actions change future states. NVIDIA Cosmos provides a world-model foundation for physical AI across robotics, autonomous systems, and vision AI. World Action Models (WAMs), e.g., NVIDIA GR00T, extend this foundation towards action, translating multimodal world understanding into executable robot motion for demanding tasks such as long-horizon manipulation and assembly.

In this talk, we will use Cosmos and GR00T as connected case studies for building physical AI systems with PyTorch, from world-model training to action-centric deployment in real robots. We will highlight real robot showcases and discuss the systems challenges that arise across the lifecycle of training and inference, and the solutions we adopted. These include methods for ingesting heterogeneous multimodal robot data, scaling distributed training jobs, diagnosing performance bottlenecks, optimizing critical computation paths, hiding checkpoint stalls, and balancing memory, throughput, latency, reliability and real-world robot performance. Attendees will leave with a working picture of how to build world foundation models in PyTorch, plus concrete optimization tactics for large-scale, multimodal, latency-sensitive AI workloads.

### Advancing torch.compile for Verifiable Precision & Dynamic Shapes
Speakers: Xiyuan Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1253426
This talk presents our work on two challenges for torch.compile with LLMs and multimodal models: precision verification — ensuring numerical consistency with eager execution over long training — and dynamic shape compilation — multimodal models use variable-length text, image, and audio inputs. We share our Ascend NPU benchmarks.
When torch.compile fuses and lowers operators, numerical differences can degrade model quality. Our three-level toolchain catches them: at the kernel level, we reconstruct fused kernels' FX graphs for bitwise comparison; at the module level, we instrument nn.Module hierarchies; at the full-model level, we support online training comparison. The toolchain auto-generates minimal reproducing test cases, cutting debugging from days to under a person-day. Dynamic shapes pervade multimodal models. On GPU, Inductor uses a single compilation pass with runtime dispatch. We integrate a Dynamic Virtual Machine (DVM) into Inductor: it compiles operators into compact bytecode at runtime in microseconds while preserving operator fusion. This allows multimodal models and LLMs with varying input lengths to enjoy full torch.compile optimization.

### Demo Theater: Beyond torch.compile: Reducing Data Movement with Device-Persistent Tensors in PyTorch
Speakers: Minwook Ahn
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1291535
Data movement between host and device is often overlooked in accelerator integration, quietly eating into LLM serving performance. In this talk, we share how we extended PyTorch's device abstraction to support device-persistent tensors, invoked simply via Tensor.to('rbln'), to keep tensors resident on-device and minimize costly HtoD/DtoH transfers alongside our torch.compile-based integration for pre-compiled graph execution.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Clearing the Path Towards an ABI Stable PyTorch C++ Extension Ecosystem
Speakers: Sean McGovern, Chris Leonard, Jane Xu
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1252992
Every PyTorch release risks breaking C++ extensions. Projects like vLLM, SGLang, and FlashAttention would pin specific PyTorch versions, creating a fragile ecosystem where upgrades cascade into rebuild cycles, CI failures, and delayed adoption of new features.

PyTorch's stable ABI offers a way out: a binary-compatible C interface that extensions can target once and run across PyTorch versions without recompilation. However, migrating from internal APIs (at::Tensor, c10::, ATen/) to stable equivalents touches every file in an extension's C++ codebase and is a daunting though mostly trivial task, especially for large libraries.

We present a set of complementary tools to facilitate this migration. These tools can identify and inventory the use of unstable API usage, including the types, macros, method calls, and headers to change. Afterwards, source-to-source conversion can be applied mechanically with LLM-assisted follow-up to implement the actual migration.

We demonstrate these tools on real-world libraries like vLLM and SGLang, showing our process, learnings, and results. We hope they will vastly accelerate making many more libraries in the ecosystem ABI stable!

### From Full DTensor to spmd\_types: Making Parallelism Explicit in TorchTitan
Speakers: Chien-Chin Huang, Pian Pawakapan
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257076
Writing parallelism code is hard. TorchTitan adopted DTensor to ease the pain, but not everywhere: a tensor might be a plain local tensor or a DTensor sharded on some axes, and code could not tell which. Worse, the sharding layout and pending gradient reductions were implicit, so bugs followed.

We wanted full SPMD: every tensor has one clear distributed meaning, from a per-model sharding config and one parallelize() call.

Our first version made every tensor a DTensor on all axes, with local_map for the gaps. This removed the ambiguity, but DTensor inserts collectives implicitly that power users want to control, needs side-channels for gradient sharding, and adds dispatch overhead.

The final solution we are adopting is spmd_types, a lightweight type system with zero runtime overhead. Collectives are explicit, returning control to power users. Backward follows from forward, so gradient sharding and communication are predictable. It has two modes: global SPMD, where sharding is part of the type and checked across ranks, and local SPMD, where we drop to per-rank compute when the global view fails and the type gives the backward. We share the design, integration, and what we learned.

### Demo Theater: OpenCLIC: Open Communication for Distributed Inference
Speakers: Jesse Treger
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1329720
Distributed inference is changing what AI frameworks need from RDMA networking. Mixture-of-Experts models repeatedly dispatch and combine tokens across GPUs, creating dynamic, latency-sensitive all-to-all traffic unlike the large-message xCCL collectives of distributed training. Current solutions lower latency through tightly integrated GPU, communication, and networking stacks built around connection-oriented RDMA transports, trading portability and developer choice for performance. These approaches remain a poor structural match for the many-destination communication patterns of expert-parallel inference, often consuming GPU execution resources for communication that could otherwise be devoted to inference.

A more open and scalable path starts from a different question: what should inference communication look like if it were designed for connectionless RDMA networks from the ground up, rather than adapted from connection-oriented ones? The emerging Ultra Ethernet Transport—modeled on the HPE Slingshot interconnect deployed in many of the world’s most powerful supercomputers—avoids per-peer connections to improve multipathing, loss recovery, and scalability. It provides an open foundation for innovation across accelerators, networks, and software.

This presentation will introduce OpenCLIC, an open inference communication framework for connectionless networks being integrated with vLLM. Expert-parallel dispatch and combine are its first use case, with broader support planned for one-sided operations such as KV-cache transfer, cache reuse and offload, and model-state movement. OpenCLIC separates framework interfaces, GPU kernels, and transport implementations so developers can use a common interface for adding communication-aware inference capabilities without tying them to a single accelerator or network stack.

Its initial HPE Slingshot implementation uses kernel-initiated OpenSHMEM communication to expose network resources directly to GPU code and keep the CPU out of the critical path. Designed to extend across accelerators and fabrics, OpenCLIC demonstrates how portable GPU-initiated communication and scalable connectionless networking can support expert parallelism and the data-movement needs of distributed inference. By separating communication algorithms from transport implementations,OpenCLIC preserves flexibility in hardware choices while creating a path for inference software to exploit more capable communication architectures as they emerge.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### HiFloat: Democratizing Ultra-Low Precision Training and Inference in PyTorch Ecosystems
Speakers: Yun Zhao, Haonan Zhang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1206584
Standard FP8 formats suffer from frequent gradient overflows and a heavy reliance on complex Delayed Scaling, leading to training instabilities in large-scale PyTorch workflows. This session introduces HiFloat8 and HiFloat4 — an innovative family of tapered precision formats natively designed to match the distribution of neural network weights and gradients. By eliminating aggressive scaling factors, HiFloat enables stable model training and aggressive quantization.
We will demonstrate how we deeply integrated HiFloat into the PyTorch ecosystem, leveraging PyTorch custom ops, Triton-based kernels, and torch.compile for seamless acceleration. Attendees will see live demonstrations of HiFloat-accelerated LLM workflows within DeepSpeed and vLLM on current-gen GPUs. We analyze real-world benchmarks showing that HiF8 achieves final loss parity with FP16 while delivering a 1.5x–1.7x GEMM speedup. Finally, we will outline the open-source PyTorch API roadmap for HiFloat, encouraging community collaboration for next-generation hardware alignment.

### Elastic Expert Parallelism in vLLM
Speakers: Itay Alroy
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1252137
Expert parallelism (EP) is fundamental to efficient serving for Mixture-of-Experts (MoE) models. WideEP, where EP spans many workers, expands KV cache capacity and enables high concurrency and long-context workloads. Until recently, EP in vLLM was static: once a deployment started, it could not scale up to handle higher load or scale down to reduce GPU usage without a restart. Elastic Expert Parallelism addresses this by letting vLLM add or remove workers at runtime and redistribute experts across the updated worker set with minimal interruption to serving.

This session will present the design of Elastic EP in vLLM: architecture, key implementation details, open challenges, and future roadmap. It will examine what must happen when EP size changes: communication topologies must be reconfigured, CUDA graphs recaptured, expert placement rebalanced through the EP Load Balancer (EPLB), and weights transferred to new GPUs. The talk will also describe how reconfiguration is coordinated with model forward execution, how Elastic EP lays the groundwork for fault-tolerant MoE deployments, and how NIXL EP enables grow/shrink under live traffic, fault detection, reporting, and recovery.

### Native DSL Operators in PyTorch Core
Speakers: Simon Layton
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255976
Domain-specific-languages (DSLs) allowing developers to write performant kernels in high-level languages have become ubiquitous in the past few years. They have been used to great effect in libraries such as FlashAttention, but have remained outside of PyTorch's core.

Now that has all changed - this talk presents our work towards adding DSL-authored operators as first-class citizens of PyTorch core, tying into dispatch, testing, and allowing for brand new operators, highly-optimized implementations, and spot-fixes for awkward, specialized performance cliffs.

### Beyond AdamW: A Practical PyTorch Walkthrough of Muon, Dion, and Orthogonalized Optimizer Variants
Speakers: Jennifer Wei
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1248446
AdamW is the default optimizer for many PyTorch training workflows, but its memory-heavy optimizer state and scaling costs become increasingly important as models grow. This talk uses Muon, Dion, and related orthogonalized optimizer variants as a practical case study in moving beyond default optimizer choices.

I will walk through why Muon matters, how it applies matrix orthogonalization to hidden-layer updates, and how to implement the core ideas in PyTorch: momentum, Newton-Schulz iteration, parameter grouping, and AdamW compatibility. The talk then bridges from single-GPU implementation to distributed training, covering communication bottlenecks, optimizer state, parameter sharding, benchmarking, and reproducibility.

The material is based on my Muon tutorial/reproducitivity series: `muon-tutorial`, `muon-distributed`, and `muon-distributed-reproducibility`. I will also discuss newer developments such as Dion/Dion2, connect the ideas to production-oriented systems like AI2’s OLMo-core, and include early Dion mini-pretraining results if available.

Code can be found here 👇
https://huggingface.co/bird-of-paradise

### From PyTorch to Production: Serving a Physics-Constrained Generative Model with ONNX, Ray, and vLLM
Speakers: Arun Sharma
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256403
Generative downscaling turns coarse climate fields into kilometer-scale maps, but diffusion and flow-matching models routinely break the physics they should respect: winds that diverge, negative rainfall, precipitation totals that drift from the coarse input. PC-RF is a conditional rectified-flow model in PyTorch that bakes three conservation constraints (divergence-free wind, non-negative precipitation, domain mass balance) straight into the training objective and fuses ERA5 atmosphere with Sentinel-2 imagery.

This talk follows one model from torch training to a served stack, and the engineering that broke along the way: exporting a U-Net with attention two ways (torch.onnx and AOTInductor) and why both specialized shapes until coaxed, running the rectified-flow ODE sampler outside the graph, enforcing physics at inference so non-negativity and mass-conservation errors hit exactly zero, and a Ray Train recipe for scaling. The serving path is polyglot: ONNX Runtime in Rust, Temporal in Go, and a vLLM agent that calls the downscaler as a tool. You leave with patterns for shipping scientific generative models, plus three physics-validity metrics worth adding to your eval.

### Agentic Inference on Rubin: Challenges and Optimizations
Speakers: Alex Settle
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1337217
As enterprise AI transitions from single-turn LLM inference to agentic, it introduces dynamic execution graphs, branching sub-tasks, and variable-length tool loops. These complex workflows require targeted LLM framework optimizations in vLLM/SGLang focusing on advanced prefix caching and dynamic KV-cache management. Emerging benchmarks such as AgentX and AgentPerf provide crucial, vendor-neutral frameworks to accurately measure such agentic inference. We show how the NVIDIA Rubin architecture and its integration to LLM frameworks solves this complexity, delivering unprecedented speed, throughput and efficiency across the pareto, establishing itself as the definitive platform for production-grade agentic AI.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### TorchJD: Training PyTorch Models with Multiple Losses
Speakers: Valérian Rey, Khush Patel
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256805
In this session, we will show how TorchJD (now part of the PyTorch ecosystem) can be used to train models with multiple losses.

In particular, we will talk about:
1\) Jacobian descent, a method where the Jacobian (i.e. the matrix containing the gradient of each loss) is computed and aggregated so that the parameter update is beneficial to all losses.

2\) Scalarization methods, where the losses are combined into a single scalar loss, to be optimized with gradient-based methods.

3\) Applications: Multitask learning (1 loss per task), instance-wise risk minimization (1 loss per batch element), class-wise risk minimization (1 loss per class), regularized learning (main loss & regularization term), Machine unlearning (forgetting loss & retention loss), federated / distributed learning (1 gradient per node), adversarial fairness (main loss & fairness loss), etc.

Library: https://github.com/SimplexLab/TorchJD
Paper: https://arxiv.org/abs/2406.16232

### Efficient Pretraining of LLMs in NVFP4
Speakers: Anjulie Agrusa US, Ryan Spring US, Bruce Zitelli
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256332
Training frontier LLMs is expensive: both model scale and token horizon drive costs. Peak throughput on GB200 and GB300 is 2x and 3x higher, respectively, between FP4 and FP8 GEMMs. Pretraining with weights, activations, and gradients in NVFP4 accelerates all three GEMMs in the forward and backward passes. Large-scale stable and accurate pretraining in NVFP4 has been demonstrated across dense and Mixture-of-Experts workloads, yet quality gaps persist between models trained in NVFP4 and BF16, particularly at small and medium model sizes. Recent work from the NVFP4 research community has focused on reducing quantization error, including methods that address backward pass bias without the increased error associated with stochastic rounding. We leverage such techniques and present an improvement to the NVFP4 pretraining recipe that significantly closes the quality gap to BF16 across multiple LLM workloads. We are upstreaming these recipes into the PyTorch ecosystem through TorchAO and TorchTitan: dense linear NVFP4 training is available in TorchAO today. The talk covers recipe design, kernel choices, and the API surface needed to bring NVFP4 training into native PyTorch workflows.

### Building a Post-Training Platform for Teams That Don't Own the Training Loop
Speakers: Gaurav Arora, Shunyao Li, Eric Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257963
As post-training expanded across teams at Pinterest (SFT, DPO, GRPO on vision-language models), each built its own stack: different frameworks, data formats, and distributed strategies. Teams spent weeks integrating OSS frameworks with internal infra before training a single step. Our traditional ML platform (MLEnv) owned the PyTorch training loop and reached 95% adoption. Post-training broke that: the loop now lives inside fast-moving OSS frameworks releasing monthly with new techniques. We built PTEnv — a lifecycle harness for PyTorch-based post-training, owning everything around the loop (data, orchestration, scaling, eval, export) while delegating the inner loop to OSS frameworks. The same interface supports subprocess execution with Ray for RL and in-process with MS-Swift using PyTorch FSDP/DDP for SFT — framework choice is a config line, not a rewrite. This talk covers the harness architecture, production gotchas training VLMs at scale (weight sync bottlenecks, MoE workarounds), post training optimization on real workloads, and framework-agnostic eval with LLM-as-judge. A practical talk for platform teams supporting multiple post-training workloads.

### Boosting PyTorch’s Heterogeneous Compute Ecosystem: Optimizing LLM Training and Serving on NPU
Speakers: Fred Li
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1348281
Modern large language model workflows rely on a rich ecosystem built atop PyTorch, yet many of these toolchains are primarily validated on GPU hardware. This creates adoption friction for users on accelerators other than GPU rolling out pre-training, fine-tuning, and high-throughput inference pipelines.

In this talk, we will dive into how community-led enhancements to PyTorch and its surrounding ecosystem enable robust end-to-end LLM deployment on NPU. We will walk through kernel optimizations, parallelism strategy tuning, and compiler-based improvements that unlock competitive performance for LLM workloads, and wrap up with practical guidance for developers building on NPU platforms benifit both NPU users and also users on other accelerator that are looking forward to enhance thier usability on PyTorch.

\************************

_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### TorchTitan GraphTrainer: LLM Distributed Training with PyTorch's Compiler Toolkit
Speakers: Sanket Jayant Purandare, Sherlock Huang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257898
LLM training in PyTorch relies on eager mode or selective torch.compile, with tangled interactions between hooks, autograd, and compilation that resist customization, and on distributed plans hand-picked layer by layer from FSDP, TP, SP, and EP recipes.

GraphTrainer uses a minimal dispatcher-based tracer to capture the full training step (forward, loss, backward) as an FX graph. With compute and communication both explicit, it enables per-tensor activation checkpointing and offloading, fine-grained comp/comm overlap, CUDA Graphs, bitwise-preserving regional Inductor compilation, rank-agnostic precompilation, and graph-based pipeline parallelism, for dense and MoE models on heterogeneous accelerators.

Parallelism comes in two modes over this shared graph substrate. Manual uses TorchTitan-native strategies. Auto uses AutoParallel: given only a device mesh, memory budget, and sample batch, it solves for a strategy directly on the graph via ILP and fast approximations, handles non-SPMD ops like MoE routing through local_map, and auto-fuses collectives. On LLaMA-3 8B (128 H100s) it matches SimpleFSDP+TP latency at 12% less memory, finding strategies nobody writes by hand.

### Deploying Robot Policies Across Many Targets with ExecuTorch
Speakers: Anthony Shoumikhin, Jacob Szwejbka
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257831
Robotics teams are rapidly adopting learned policies like ACT, diffusion policies, and compact Vision-Language-Action models. The bottleneck is shifting from training to deployment: getting a PyTorch policy into a real control loop demands predictable latency, bounded memory, and hardware-specific acceleration, and today that usually means custom export scripts, Python services, ROS glue, and per-target rework for every accelerator.
This talk presents ExecuTorch as a production deployment layer for robot policies. You keep policy creation in ecosystems like LeRobot, Physical AI Studio, OpenVLA, and Octo, and use ExecuTorch for portable artifacts, backend delegation, memory planning, and runtime integration. We take one policy end-to-end, then show the same recipe transfers across common robotics hardware through existing backends: TensorRT/CUDA for NVIDIA and Jetson, OpenVINO for Intel edge, XNNPACK for CPU and ARM fallback, and Cortex-M for microcontroller-class components.
The result is a deployment path you can follow without rebuilding the stack for every robot: train or fine-tune, export, run locally, measure real latency and memory, and integrate into the runtime.

### Portable Paged Attention: From Triton to Helion
Speakers: Burkhard Ringlein
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255851
Recently, the PyTorch team released Helion, a new domain-specific PyTorch-based language for developing high-performing, portable kernels. With extensive autotuning and broader backend support, Helion promises to advance performance portability beyond Triton.

To test this, we took on the challenge of writing one of AI's most performance-critical kernels in Helion: Paged Attention, the core of vLLM.

Building on our expertise creating the state-of-the-art portable Triton attention backend in vLLM, we developed the experimental Helion attention backend for vLLM.

In this talk, we will present the differences between paged attention in Triton and Helion, what changes to the algorithm of the kernel were necessary to achieve matching performance, and how Helion enables optimizations that were not possible with Triton. Then, we will share lessons we learned along the way and extensive benchmark results that show that Helion kernels can, in many scenarios, even outperform our optimized Triton kernels. Our early results indicate the experimental Helion attention backend can reduce the latency by up to 50% and improve the end-to-end throughput vs. Triton by up to 10%.

### “What Do I Do Now?” Bridging the ExecuTorch Adoption Gap Through Developer Learning
Speakers: Matt Cossins
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255970
ExecuTorch is evolving rapidly, but developers can encounter challenges when moving from introductory demos to practical deployment. Drawing from experience creating hands-on learning material for ExecuTorch workflows on Arm, this session brings together developers, educators, ecosystem contributors, and practitioners to discuss how developers successfully learn and adopt ExecuTorch workflows.

We will explore what works well today, and where developers encounter learning gaps or “cliff edges,” across model preparation workflows (AOT compilation and optimization) and deployment into on-device applications. Discussion topics include onboarding patterns, reproducible tutorials and labs, effective approaches for teaching best practices, and helping developers progress from isolated examples to complete edge AI applications.

Participants will share experiences from teaching, learning, deploying, or experimenting with ExecuTorch across different hardware targets and use cases. Attendees will leave with practical insights, a clearer understanding of priorities for ExecuTorch developer education going into 2027, and new connections for collaboration on tutorials and learning resources.

Located across from the PyTorch gear store.

### Meet the Developers of Helion
Speakers: Jason ANSEL, Jongsok CHOI, Yarong Mu, Freya Azad, Theotime Combes, Ethan Che, Dunfan Lu, Shangdi Yu, Oguz Ulgen, Emilio Cota, Karthick Panner Selvam
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1340815
Join PyTorch experts for an interactive “Meet the Developers” session – a chance to learn in a small group setting and ask your most pressing questions. No sign-up required – just drop in and get real answers from the people building the tools.

Located in front the Meta booth.

### Demo Theater: Evolving Ray Core for Post-Training at Scale
Speakers: Mengjin Yan, Joshua Lee
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1345871
Before a post-training job trains a single step, its trainers and inference engines must be scheduled onto the cluster, and every step after that, fresh weights must move between them. We evolve Ray Core by starting from the workloads it runs, and for post-training, the trends point to two needs: better scalability and better performance. We have been improving Ray Core on both fronts. This talk starts with a quick introduction to Ray Core, the open source runtime underneath post-training frameworks like SkyRL, Miles, and NeMo RL, and how its building blocks map onto a post-training loop. We then cover scalability, including scaling Ray's scheduling to 10,000-node clusters, and performance, including moving PyTorch tensors directly between GPUs with Ray Direct Transport (RDT). We close with where Ray Core is heading next and how to get involved.

\*******
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### Prefix Caching for Autoregressive Stages in Multi-Stage Pipelines
Speakers: Ricardo Noriega, Alex Brooks
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255511
In autoregressive generation, caching is critical to avoid redundant computation. Transformer-based models benefit greatly from the KV cache, which has since been extended for multi-request serving systems, such as prefix caching in vLLM.

However, these approaches are largely designed to support transformer-based models that generate outputs autoregressively. Integrating such approaches into systems generating multimodal outputs, e.g., vLLM-Omni, is nontrivial, since models may be composed of multi-stage pipelines, and prefix caching may not be directly applicable to all approaches (e.g., diffusion).

This talk explores "Automatic Prefix Caching for Stage Outputs" in vLLM-Omni, a non-invasive approach for extending vLLM's prefix caching in the context of multi-stage models while minimizing GPU memory cost. This is done by aligning external CPU tensor caches with vLLM's native block management. We also show how vLLM-Omni dynamically discovers cacheable tensors, removing the need for manual configurations.

Attendees will gain insights into multi-stage inference memory management and how prefix caching of autoregressive stage outputs can accelerate multi-stage pipelines.

### Primus Tuning: Hybrid Projection and Agentic Search for Distributed Training
Speakers: Anshu Raina, Peyman Razaghi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256459
Configuring distributed LLM training is a combinatorial nightmare: TP, PP, EP, CP, DP, micro-batch, recomputation, sharding, and overlap all interact, and one wrong byte of activation accounting separates best-in-class throughput from OOM, yet good recipes are still found by burning multi-node GPU-hours on crashes. The Primus Tuning Agent closes that loop on a single node: its hybrid projection engine measures compute, communication, and memory on as few as one GPU, then analytically reconstructs cross-node collectives, FSDP overlap, and the pipeline schedule to project throughput and peak memory at the multi-node target, with a CPU-only mode for pre-silicon planning. Scoring any candidate in seconds, it also drives a search loop where a seed planner sweeps single axes, an LLM phase proposes cross-axis combinations, and the memory projection pre-filters OOM candidates before any GPU runs. On Llama 3.1 and Mixtral 8x22B across two GPU generations, projections stay within ~10% of measured throughput, and on Mixtral 8x22B the agent beats the published 4-node BF16 reference by +27% in under 30 minutes on a single node, with no hand-written configs and no full-cluster profiling.

### From Bytes to Tensors: Efficient Media Processing with PyTorch in 2026
Speakers: Nicolas Hug, Scott Schneider
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1254966
Multimodal models have become the default: even text-only LLMs are expected to understand images, video, and audio. As a result, efficient media ingestion is a first-class concern for ML practitioners. Images, video, and audio must be decoded and transformed before being passed to a model, and doing this fast is critical for both training throughput and inference latency. Video decoding in particular is frequently a bottleneck that starves GPUs and caps end-to-end performance.

TorchVision, TorchCodec, and TorchAudio together cover the full media preprocessing pipeline from raw encoded bytes to model-ready tensors.

In this talk we'll first map this ecosystem as it has evolved in 2026: what each library owns and how they fit together into an efficient end-to-end pipeline. We'll then show how to squeeze maximum throughput out of the stack with techniques that have landed in the libraries over the past year: including CUDA-accelerated decoding, SIMD-optimized and decoder-native transforms, pre-computed frame indices, and approximate seeking modes.

Attendees will leave with a clear picture of the PyTorch media stack and patterns to eliminate preprocessing bottlenecks.

### Torchtitan RL: A Unified and Extensible Training Framework for Agentic Tasks
Speakers: Felipe Mello, Jiani Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256870
Asynchronous RL is fundamental for training agents to invoke tools, execute code, and learn over long horizons. Yet such systems are notoriously unstable at frontier scale. The instability stems from two systemic problems: keeping training and generation numerically aligned, and keeping this sophisticated distributed stack easy to reason about and experiment with.

For numerical mismatch, TorchTitan RL starts from first principles: one model definition for training and generation. Many RL stacks decouple them into separate implementations with different parallelism, kernels and definitions; even synchronized weights can produce different token probabilities. A shared definition enables an on-policy, bitwise-reproducible mode, so researchers can isolate reward and task design from system artifacts.

To address infrastructure complexity, TorchTitan RL provides a hackable, forkable stack. Grounded in the expertise from TorchTitan’s large-scale trainer, we design for cleanness and extensibility. This improves research velocity by making it easier to focus on the task at hand.

In this talk, we will cover the system design, results and evaluation methodology.

### NVFP4 Training Tips and Tricks
Speakers: Paul Chang, Erik Schultheis
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1347085
This session shares practical lessons from training dense LLMs on a GB300 with NVFP4, covering hyperparameter tuning, optimiser choice and training recipes.

\*************************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### From Backed to Unbacked: Sound, Predictable, and Controllable Dynamic Shapes in PyTorch
Speakers: Laith Sakka
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1260092
Dynamic shapes originally solved a practical torch.compile problem: avoiding a new graph for every input size. Backed shapes did this by keeping sizes symbolic while using example-input hints to pick branches and add guards. This works well for drop-in JIT compilation; occasional recompilation is acceptable and graph coverage can be discovered incrementally at runtime.

However, for explicit graph-capture workflows such as vLLM, export, and pre-compilation — and for JIT deployments where dynamic-shape recompilation is not acceptable — users need graphs whose valid input space is decided ahead of time.

Unbacked shapes provide that contract by disallowing implicit guards on dynamic shapes: the compiler must prove a path is valid generally, take a general implementation, or rely on explicit user assumptions.

This talk will argue why unbacked shapes are better for these workflows, then cover the work done over the past year and a half to make them ready for real use and user-friendly; handling data-dependent errors and branching, closing the performance gap with backed shapes across TorchBench and vLLM, and building APIs for shape constraints and dispatch across compiled artifacts.

### Building Cost-Efficient Mixture-of-Models on AMD GPUs with vLLM Semantic Router
Speakers: Mahdi Ghodsi
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1333195
No single language model is the best choice for every request. Large frontier models offer strong reasoning but carry higher cost and latency, while smaller or specialized models can handle many workloads more efficiently. A Mixture-of-Models system turns these different models into one unified model by intelligently selecting, escalating, or combining them according to each request.

In this session, we introduce Mixture-of-Models and show how vLLM Semantic Router provides the programmable control layer between agent harness and heterogeneous model backends. We will explain how its signals, projections, decisions, algorithms, and plugins address practical requirements including quality, cost, latency, safety, privacy, modality, and domain specialization.

\******************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### PyTorch-Native Feature Transformation and Training Framework for Uber Eats Recommendation
Speakers: Peng Zhang, Ke Chen, Xandra Zhu
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1241540
Modern ML systems need preprocessing pipelines that are scalable, GPU-friendly, and consistent across training and serving. In this talk, we share how Uber migrated the Eats recommendation model stack from TensorFlow/Horovod to PyTorch/DDP/DeepSpeed and built a PyTorch-native feature transformation framework on Ray to replace legacy Spark-based preprocessing. With a unified PyTorch-first architecture, we achieved a 5x speedup and 90% lower memory usage for data transformation, along with a 20x improvement in training throughput.

We’ll cover how declarative transform DAGs are compiled into reusable PyTorch modules, how Ray Data enables distributed feature-stat computation and zero-copy batch transformations, and how preprocessing graphs can be fused directly with model inference for Triton serving. We’ll also discuss how we enable model parallelism and GPU optimization techniques, and lessons from running multi-billion-row production workloads, including performance improvements, reduced resource overhead, and simplified developer workflows.

This session is designed for ML platform engineers and practitioners building scalable PyTorch and distributed ML pipelines.

### Speeding Up torch.compile: A New FakeTensor
Speakers: Angel Li
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257046
FakeTensor is used as a lightweight substitute of regular tensors used by Dynamo and Inductor when building FX graphs. These FX graphs are then used to optimize user code by fusing ops, planning memory, etc.

One downside of torch.compile is the amount of time it takes (especially on cold start) and a big reason is because of FakeTensor. One FakeTensor propagation today takes around 20% of the entire Dynamo tracing time and running aten.mm with a Python FakeTensor takes around 225us. However if we run the same op with a C++ FakeTensor, we can see a 30x speedup.

In this talk, we'll be announcing a new FakeTensor in C++ that has allowed us to see orders of magnitudes of speedup. We'll go over key changes, design decisions, performance benchmarks, and integrations with torch.compile's ecosystem.

### When Rollout and Training Disagree: Lessons from Building a Mismatch-Free RL Engine
Speakers: Neiwen Ling, Tianle Zhong
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257767
Modern LLM reinforcement learning systems often split rollout generation and policy optimization across different execution stacks: inference engines generate samples, while training stacks such as FSDP recompute log-probabilities and update the policy. This separation improves throughput, but it can introduce Training–Inference Mismatch (TIM), where rollout and training paths assign different token probabilities to the same sequence under the same model weights.

In this talk, we share lessons from building VeXact, an open-source, a mismatch-free rollout backend used by verl-based LLM RL training to align rollout log-probabilities with the training path. Using VeXact as a diagnostic baseline, we show that small token-level numerical disagreements are not benign: they can independently destabilize LLM RL, alter the effective PPO/GRPO optimization objective. We will discuss practical takeaways for developers building RL post-training systems, including how to reason about numerical consistency, batch-invariant kernels, rollout/training alignment, and the limits of post-hoc algorithmic fixes.

### Introducing NCCL Extensions: Communication Patterns for Modern AI
Speakers: Sreeram Potluri, Artem Polyakov
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257023
Sparse MoE, disaggregated inference, and RL weight rollout require communication patterns that collective libraries were never designed for. NCCL domain extensions are NCCL's answer: a family of specialized libraries built on NCCL's Device APIs --designed for customization, kernel fusion, and rapid prototyping of emerging communication patterns -- while inheriting NCCL's topology awareness and transport stack.

We debut two extensions. NCCL-EP brings MoE dispatch and combine natively into NCCL: a single, automatically tuned API spanning latency-optimized inference decode and throughput-optimized training, bringing GPU-initiated RDMA and NVLink to MoE workloads out of the box. NCCL-M2N enables zero-copy resharding between disjoint device meshes -- moving weight snapshots from trainers to inference replicas for RL rollout with no CPU staging.

We walk through the design rationale, API, and performance results. Together, these extensions signal a new direction: NCCL as a platform for the real and diverse communication demands of modern AI, not just a collective library.

### Scaling PyTorch Dataloaders 10x: A Case Study
Speakers: Ian Stenbit, Christine Cheng, Dylan Doblar
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1243544
The autonomous vehicles team at NVIDIA is using PyTorch for training end-to-end models on thousands of GPUs across heterogenous training clusters.

In this talk, we'll discuss how we scaled out what started as a research project to full production scale, and what we learned about optimizing large-scale throughput of distributed dataloaders. We'll touch on topics including
\- Profiling training and dataloading performance with torch profiling, Nsight, and cprofiler
\- Dealing with distributed filesystems
\- Pipelining CUDA operations between the dataloader and the model
\- Efficiently scaling video decoding
\- Identifying sources of tail latency in a large distributed setting

Over the course of two years, we've sped up training throughput by 10x, and we're eager to share what we've learned along the way.

### Lightweight FX Tracing in PyTorch
Speakers: Yidi Wu, Richard Zou
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256183
Dynamo is the frontend for torch.compile. It captures graphs by tracing Python bytecode execution, allowing it to handle arbitrary PyTorch models by falling back to graph breaks when it encounters unsupported behavior. This flexibility is useful to support a multitude of PyTorch models, but we’ve received feedback that Dynamo is too heavy for use cases where users require a full graph.
In this talk, we present a lightweight FX tracer based on make_fx. Instead of trying to capture the full semantics of Python, this tracer targets functionally pure PyTorch code. In exchange for that restriction, it is much simpler than Dynamo and provides a more learnable programming model, inspired by JAX-style tracing.
You’ll learn how the lightweight tracer API works, what guarantees it provides, how it differs from Dynamo, and how it interacts with other APIs.

### Integrating TorchTPU into TorchTitan and Optimizing Models for TPUs
Speakers: Aleksey Vlasenko, Will Constable
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1246272
Describe the process team took to add TorchTPU support into TorchTitan and optimizing select models to run on TPU.
We'll also demonstrate performance of the models on TPU and how that compares to GPU performance.

### From PyTorch to the Edge: Agentic Synthesis of Inference Runtimes for Heterogeneous Hardware
Speakers: Thomas Cottenier
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257310
For years we have built LLM inference runtimes as general-purpose infrastructure: a single stack, hand-tuned over many engineer-years, meant to serve every model and every target. This talk takes the opposite bet for the edge. We present an agentic harness that synthesizes bespoke runtimes per target, transforming PyTorch models through whatever pipeline the target requires: torch.export and ExecuTorch backends where they fit, torchao quantization and direct kernel generation where they do not. Each experiment is logged and reused, building a knowledge base that accelerates subsequent runs. We validate on Apple silicon, a heterogeneous CPU+GPU+NPU platform with strong optimized references (llama.cpp, MLX) to compare against. Agent-generated runtimes prove competitive across inference phases on Qwen 3; reproducing on Gemma 4 confirms the pipeline generalizes across models and lands faster using accumulated logs. We then target Arm hardware lacking any baseline, including Vulkan ML paths. Frameworks remain the substrate agents lower through, and bespoke generated runtimes reach targets specialization never could.

### Scaling PyTorch on Intel XPU: Field Notes from AI for Science on Aurora
Speakers: Sam Foreman, Panagiotis Kourdis, Tanima Dey
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257912
Bringing a new accelerator up as a first-class PyTorch backend at scale takes more than vendor patches. It requires reproducible benchmarking, portable training code, and operational machinery that survives long-running jobs. This lightning talk shares experiences from training scientific foundation models in production on 63K+ XPUs on ALCF's Aurora system.

We cover three things:

\- What was needed: the XPU integration path (torch.xpu, the IPEX-to-xccl transition, distributed primitives, collective tuning) and the cross-vendor abstractions that let identical training code run on Intel, NVIDIA, and AMD hardware.

\- What was accomplished: migrating our production training stack from a Megatron-DeepSpeed fork to torchtitan + DTensor + FSDP2, with optimization and testing at every layer; from fused kernels and collectives up through distributed orchestration.

\- What remains: fused kernels, async checkpointing, fault tolerance, and the operational layer long jobs require (silent-hang detection, bad-node failover, layered restart loops), plus what the next accelerator team should expect.

The takeaway: Patterns for anyone running PyTorch at scale on a new accelerator.

### Unlocking the Full Potential of TorchDynamo: Accelerating, Comparing, and Debugging ML Systems
Speakers: Yi Pan, Stephanie Wang
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257418
TorchDynamo is widely recognized as the frontend of the torch.compile pipeline, yet its capacity to intercept and decouple computational graphs remains underutilized. In this talk, we present recent work from our research group that leverages it to solve critical bottlenecks across AI infrastructure through acceleration, differential comparison, and numerical debugging.

We begin by demonstrating how we use TorchDynamo to accelerate execution by cleanly decoupling logical model definition from physical execution. DynaFlow leverages this mechanism to transparently integrate intra-device parallelism into existing systems without invasive rewrites, and Piper targets flexible inter- and intra-device parallelism for complex strategies like DualPipe. Digging into the operator level, we introduce differential comparison in Magneton by leveraging the graph tracing ability. By automatically mapping equivalent operations across competing systems, Magneton identifies the superior implementation regarding latency or energy consumption. Finally, we extend the comparison to debug numerical correctness by capturing and comparing intermediate tensors at matched subgraph boundaries.

### Lessons at Scale: Building a PyTorch Inference Stack with Open-Source Components
Speakers: Oscar Savolainen
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1347541
Taking a PyTorch model into production introduces new challenges around performance, scalability and serving infrastructure. In this session, Nscale shares practical lessons from building and operating open-source inference stacks with vLLM and SGLang at scale. We’ll explore model deployment, GPU utilization, KV-cache management, autoscaling and performance optimization, before looking beneath the serving layer at the large-scale infrastructure that makes it possible - including how inference workloads run across multi-node GPU fabrics and hierarchical storage. Attendees will leave with practical insights for building an open, portable path from model to production that can scale with increasingly demanding inference workloads.

\*********************
_In order to facilitate networking and business relationships at the event, you may choose to visit a third party’s booth or access sponsored content. You are never required to visit third party booths or to access sponsored content. When visiting a booth or participating in sponsored activities, the third party will receive some of your registration data. This data includes your first name, last name, title, company, address, email, standard demographics questions (i.e. job function, industry), and details about the sponsored content or resources you interacted with. If you choose to interact with a booth or access sponsored content, you are explicitly consenting to receipt and use of such data by the third-party recipients, which will be subject to their own privacy policies._

### MCCL: Fault-Tolerant Collective Communication for Large-Scale GPU Training
Speakers: Ben Carver
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256858
As AI training workloads scale to tens of thousands of GPUs, hardware failure has become a routine operating condition rather than an exception. Traditional collective communication libraries, which rely on static communicator membership, force costly, full-job restarts whenever a failure occurs. This talk introduces the topic of large-scale training using the Meta Collective Communication Library (MCCL), an open-source, fault-tolerant C++ library designed and developed at Meta to address these challenges.

MCCL redefines the communication lifecycle by treating hardware failure as a first-class design principle, enabling dynamic communicator reconfiguration (shrinking and growing as ranks fail or recover) without interrupting the overall training job. We will demonstrate how MCCL integrates with Torchcomms to provide production-grade, fault-tolerant collective operations, including AllReduce and Send/Recv, while maintaining performance parity with industry standards like NCCL. Attendees will learn about MCCL’s architecture and how to implement robust training loops that recover gracefully from infrastructure instability.

### Multimodal Dataloaders for Physical AI
Speakers: Peter Prettenhofer
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257585
Physical AI requires temporal streams of multi-modal data: mixing image (or video) observations, textual descriptions and scalar measurements. Managing these various data sources and efficiently preparing tensors from them is critical for developing robotics foundations models. PyTorch dataloaders and the surrounding ecosystem provides many utilities to simplify preparing data, however when datasets exceed disk size for a single host balancing network bandwidth, host or accelerator decoding, and various data types there are a larger variety of tradeoffs to consider in the design space.

This talk describes the challenges associated with preparing and loading large robotics datasets.
We’ll walk through:
\* Overview of data sources
\* Wrangling data into a format usable for training
\* Different data access patterns required by various model types (VLAs, World Models)
\* Building PyTorch datasets/dataloaders on top of that data to avoid starving your GPUs

This talk is for PyTorch users training large robotics models or developers supporting infrastructure for training large robotics models.

### AI Community Bash featuring DE LA SOUL
Speakers: DE LA SOUL
page: https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1311946
Close out PyTorch Conference with a night worth sticking around for.

We’re bringing the AGNTCon + MCPCon and PyTorch communities together for an evening of food, drinks, great company—and a live concert from legendary hip-hop group DE LA SOUL.

Celebrate with fellow developers, maintainers, founders and contributors from across the AI ecosystem, then stick around as DE LA SOUL takes the stage.

One last night. Two AI communities. One unforgettable show.

Let us know you’re joining when you register for the PyTorch Conference so we hold you a spot! Space is limited!

MENU
\-Dino Nuggets (Vegan Option Available)
\-Pepperoni Bagel Bites
\-Curly Fries (Vegan, GF, Vegetarian)
\-Frito Pie in a Bag (GF, Vegan Options Available)
\-Soft Pretzels with Mustard (Vegetarian)
\-Dunk-A-Roo Style Veggie Cups (Vegan/GF/Vegetarian)
\-Popcorn (GF, Vegan, Vegetarian) with a Variety of Toppings
\-Beer, Wine, Assorted Sodas + Waters

\-Ice Cream Sandwich with a variety of toppings
\-90s Candy: Ring Pops, Airheads, Now & Later, Warheads

