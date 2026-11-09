>>> HOW TO RUN THIS <<<
This is the digest prompt for atscale-networking-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/atscale-networking-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/atscale-networking-2026.md
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

Below is the program for @Scale: Networking 2026. Read it and produce a digest
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
conference: @Scale: Networking 2026
source_url: https://atscaleconference.com/events/networking-2026/
generated: 2026-11-09
registry_key: atscale-networking-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## August 25
### Keynote from Meta
Speakers: Omar Baldonado (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-17
No abstract published; title, speakers and materials only.

### Resilient AI Supercomputer Networking using MRC and SRv6
Speakers: Jitendra Padhye (OpenAI)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-18
Tail latency dominates the performance of synchronous pretraining jobs when running at very large scales. We describe a three-pronged approach: (1) a new RDMA-based transport protocol, MRC, sprays across many paths and actively load-balances between them, eliminating the issue of flow collisions and (2) the use of static source-routing using SRv6 to allow MRC the freedom to bypass failures by itself. We describe our experiences running MRC and static SRv6 routing in production in OpenAI, where it has been used to train frontier models. We demonstrate how MRC allows AI training jobs to ride out many network failures that previously would have interrupted training.

### MetaRoCE: Meta's RDMA Transport
Speakers: Arvind Srinivasan (Meta), Kingshuk Mandal (Keysight Technologies)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-19
At Meta's scale — clusters growing to over a million accelerators across regions — the network is in the critical path of every AI training step, and traditional RDMA was never built for it.
MetaRoCE is Meta's clean-sheet RDMA transport: a multipath, out-of-order, receiver-driven protocol that treats Ethernet as inherently lossy and pushes all intelligence into the NIC. By shifting intelligence to the edge, the transport decouples from topology — enabling TCO-optimized multiplane FPF topologies with frictionless application adoption on commodity Ethernet.
This talk covers MetaRoCE's core mechanisms and Meta's commitment to open standards, including a companion conformance suite developed with Keysight that validates implementations from software reference through hardware emulation to production silicon.
Meta is opening MetaRoCE to the industry and inviting broader collaboration to establish it as the ubiquitous RDMA transport for AI-scale networks.

### Anatomy of @scale Machine Learning Network Operations
Speakers: Jim Julson (Coreweave)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-20
As machine learning continues to grow in scale, so too do the challenges of operating these mission critical networks. Join me in a journey through the operational challenges, and nuances found in Machine Learning and AI at scale around Infrastructure Networks.

### MetaRoCE: From Spec to NIC to Open Source
Speakers: Sandeep Nagaraja (Meta), Balakrishnan Raman (AMD)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-21
As AI and distributed workloads push datacenter fabrics to their limits, Meta's answer is MetaRoCE — a multipath, out-of-order, receiver-driven protocol that treats Ethernet as inherently lossy and pushes all intelligence into the NIC. This talk traces MetaRoCE's journey from specification to silicon, showcasing its implementation on AMD Programmable NICs via reference software implementation and demonstrating how the architecture elegantly scales out within a cluster and scales across fabrics to meet diverse deployment needs. We present real-world performance results spanning multiplane FPF topologies, tail-latency optimization, and long-distance RDMA — proving MetaRoce approach solves AI data center requirements. Finally, we present a first look at Meta's upcoming open-source release of the MetaRoCE specification, reference implementation, and compliance suites at OCP — inviting the industry to build, extend, and innovate on MetaRoCE.

### Group Q&A with Speakers
Speakers: James Zeng (Meta), Arvind Srinivasan (Meta), Kingshuk Mandal (Keysight Technologies), Sandeep Nagaraja (Meta), Balakrishnan Raman (AMD)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-22
No abstract published; title, speakers and materials only.

## August 25 — Track 1 (Mission City Ballroom)
### Live Panel: Scale-Out Networking for AI Supercomputers
Speakers: Rajiv Krishnamurthy (Meta), Joseph Provine (Meta), Andrew Dickinson (Oracle), Jim Julson (Coreweave), Jitendra Padhye (OpenAI)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-29
Live Panel with Coreweave, Meta, OpenAI, Oracle
Moderated by Rajiv Krishnamurthy
Speakers: Joseph Provine, Andrew Dickinson, Jim Julson, Jitendra Padhye
Training frontier AI models requires connecting tens of thousands of accelerators into a single, tightly coupled fabric — pushing scale-out network design into uncharted territory. This panel brings together engineers building some of the world's largest AI training networks to discuss the architectures, transport protocols, and operational lessons behind today's supercomputer-scale fabrics. Topics will include topology choices, congestion control at extreme scale, and the co-design between network infrastructure and distributed training frameworks. Expect a practitioner-level conversation on what it takes to keep massive AI clusters connected, fast, and reliable.

### Lightning Talk - The Plan That Learns
Speakers: Ben Vallis (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-31
Network capacity planning is high-stakes and unforgiving: capacity is committed years ahead, every long-range forecast is guaranteed to be wrong, and the costliest surprises are correlated demand shocks that defeat traditional risk-pooling. Much of the pipeline is already automated — but the decisions that take real judgment have stayed manual, and those are the ones that decide whether a wrong forecast corners you. This talk is about applying AI to exactly those decisions — not to chase a more accurate forecast, but to position capacity so it keeps our options open no matter how demand breaks. We show how agents are beginning to crack the three that matter most: acting inside narrow buy windows (triaging signals continuously to surface the handful of truly novel sites, weeks down to minutes), trusting data across systems that disagree on even basic definitions (a measure-enrich-regrade loop), and choosing among coupled, timing-sensitive levers (a ranked, costed menu of moves with the reasoning attached). The real frontier is a plan that learns — agents that remember every decision and how it turned out, so human judgment compounds over time instead of resetting with each planner.

### Lightning Talk - 10x Network Design Engineer
Speakers: Maaz Mohiuddin (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-32
Designing a datacenter network is where a capacity requirement becomes a blueprint: assigning device roles, wiring the interconnect, laying out addressing and failure domains, and producing the bill of materials — all while keeping the design constrained, connected, and correct. It is some of the most judgment-heavy work in network engineering, and until recently it resisted automation. This talk walks through how that is starting to change. Today, agents assist with discrete steps — sizing a fabric, proposing a topology, analyzing a change — but the trajectory points toward a single agent that can own the design end-to-end. Drawing on real waypoints from Meta's fabrics, Maaz shows what already works, where the hard problems remain (validation, above all), and how the engineer's role shifts from author to approver. The through-line: humans still make the call — they just no longer have to draw every line.

### Lightning Talk - AI-Native Network Capacity Management
Speakers: Mohab Gawish (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-33
The network capacity lifecycle, from demand signal to production operations, is a pipeline. Each stage consumes the output of the previous one, and failures compound downstream. A bad forecast leads to a bad design; a bad design leads to a painful deployment; a painful deployment leads to operational fragility.
The AI-native effort asks: what if every stage of this pipeline had an AI agent as a first-class participant? An AI agent can act as a force multiplier, automating the mechanical, surfacing the non-obvious, and closing feedback loops that today take weeks or months.

### Lightning Talk - AI4NI @Runtime
Speakers: YuLing Chen (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-34
When operating a large-scale production network serving billions of users, we face daily challenges in running network infrastructure reliably and efficiently. AI4NI @Runtime tackles these challenges across three dimensions: reliability, performance, and efficiency. At Meta, we’ve begun developing AI agents in each area and have seen promising early results. In this talk, we’ll share our solution architecture, example agentic systems, and initial findings from production trials, along with the key technical challenges and our planned directions to address them.

### Fiber Networks Innovations for AI at Scale
Speakers: Fabrice Ouandji (Meta), Sebastian Gault (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-39 | materials: https://atscaleconference.com/building-the-backbone-of-ai-inside-the-nao-mega-clusters-fiber-revolution/
Prometheus introduced significant complexity for connectivity. We were faced with significantly higher fiber count requirements, highly dynamic demand location, and compressed timelines for delivery. Tune in to find out the innovations required to meet the demand across multiple data centers in the cluster.

### Virgo: scale-out data center network for AI
Speakers: Jeongkeun "JK" Lee (Google)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-40
To address the unique requirements of AI networking, we leverage our proven Jupiter network for north-south traffic and are introducing Virgo, a new fabric for east-west scale-out communication. Virgo is a dedicated accelerator-to-accelerator fabric optimized for massive horizontal scale. It is engineered for deterministic latency and maximum resilience to provide high goodput for the ML workload. Virgo will enable the new Google Cloud's A5x bare-metal instances, which run the NVIDIA Vera Rubin NVL72 platform. It is also a key building block for next-gen TPUs. This talk will discuss Virgo's design principles for resilience, observability, deployability, and multi-building scale.

### Co-Designing Communication for AI Accelerators
Speakers: Rajeev Nair (Meta), Wes Bland (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-41
This presentation details how Meta is addressing the massive compute and data demands of modern generative AI workloads by co-designing hardware, software, and models. The talk highlights the communications architecture of MTIA 300, Meta's custom-designed AI training and inference accelerator featuring dedicated message engines to efficiently offload communication workloads. By decoupling communication from the primary compute grid, the system minimizes resource contention and substantially drives up both compute and network efficiency. Additionally, the speakers explore how "network fungibility" allows the same network interface cards (NICs) to flexibly adapt to both scale-up and scale-out configurations depending on production needs. Ultimately, the presentation demonstrates how a tight co-design loop across infrastructure layers provides a scalable, future-ready roadmap for Meta’s rapidly evolving AI demand.

### Live Panel: Building at the Roofline — Planning and Delivering Gigawatt-Scale AI Infrastructure
Speakers: Omar Baldonado (Meta), Amrita Kenue (Meta), Lucas Benson (Microsoft), Nikita Parikh (Google)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-42
Live Panel with Google, Meta, Microsoft Moderated by Omar Baldonado
Speakers: Amrita Kenue, Lucas Benson, Nikita Parikh
Today's largest AI fleets span multiple generations of technology — from power and buildings to fiber and accelerators — and must be delivered at a pace that pushes the entire supply ecosystem to its limits. This panel brings together leaders from hyperscaler infrastructure planning and technical sourcing organizations to discuss how they navigate this complexity. The conversation will explore long-range fleet strategy, multi-vendor orchestration, and the engineering realities of operating at the roofline of industry capacity. Expect a candid discussion on what it takes to plan and deliver AI infrastructure at gigawatt scale.

## August 25 — Track 2 (Exhibit Hall A)
### Physical Network Design at Scale + 3 min Q&A
Speakers: Richard Cziva (Meta), Brandon Premo (Meta)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-36 | materials: https://atscaleconference.com/physical-network-design-at-scale/
Physical network design—deciding how thousands of network devices and millions of fibers are distributed across data centers, racks, and failure domains—has traditionally been a manual, time-consuming process performed by design engineers. Yet we are seeing exponentially increasing demand to fulfill the capacity required by AI workloads. At Meta, we developed Loom, a system to automate and optimize the end-to-end physical network design pipeline. Loom orchestrates two core components: a device placement component (Planogram) which places network devices across the physical floorplan subject to dimensional and failure-domain constraints; and a fiber design component, which generates end-to-end fiber connectivity satisfying the variety of connectivity patterns driven by physical constraints. Together, these components accelerate end-to-end physical network design from months to hours, allowing us to produce more complex and efficient designs with fewer resources.

### Building scalable AI cloud interconnects with SRv6 + 3 min Q&A
Speakers: Alexey Gorovoy (Nebius)
page: https://atscaleconference.com/events/networking-2026/#agenda-item-37
Large-scale customer interconnects place new demands on network architectures, requiring predictable bandwidth, integrated network services, and consistent operation across data center and WAN domains. In this session, we present Nebius' evolving architecture for customer cloud interconnects, using SRv6 as the fundamental architectural building block to bridge virtual cloud environment with the physical network edge. We will show how this approach enables end-to-end VPN and Traffic Engineering services without protocol translation between data center and WAN domains, and share our latest implementation experience.

