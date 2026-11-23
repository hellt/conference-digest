>>> HOW TO RUN THIS <<<
This is the digest prompt for autocon-6. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/autocon-6.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/autocon-6.md
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

Below is the program for AutoCon 6. Read it and produce a digest
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
- `deepseek` - DeepSeek models, research, deployment and inference economics
- `openai` - OpenAI models, products, APIs and deployment engineering
- `anthropic` - Anthropic Claude models, agent SDKs and deployment engineering
- `z-ai` - Z.ai/Zhipu GLM models, open weights and deployment engineering
- `moonshot` - Moonshot AI Kimi models and deployment engineering
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
conference: AutoCon 6
source_url: https://networkautomation.forum/autocon6
generated: 2026-11-23
registry_key: autocon-6
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## Wednesday, 18 November 2026

### AI and Network Automation: Through the Looking Glass
Speakers: Kirk Byers
Session: Wednesday, 18 November 2026, 13:15 - 14:00 (Opening Keynote)

### NAF Framework Update
Speakers: Srividya Iyer
Session: Wednesday, 18 November 2026, 14:00 - 14:10

### 60/40: How Meta Taught AI to Triage Its Own Network
Speakers: Goutam Nalamati
Session: Wednesday, 18 November 2026, 14:10 - 14:40

### Intended Configuration as a Catalyst for Enterprise Network Automation
Speakers: Marcus Cain
Session: Wednesday, 18 November 2026, 15:35 - 16:05

### Who Builds Your Automation: NetEngs Who Learned to Code, or Developers Who Learned the Network?
Speakers: Andrew Ragusa
Session: Wednesday, 18 November 2026, 16:05 - 16:35

### Closing the skills gap: A guide to effective mentorship
Speakers: Eric Fetty
Session: Wednesday, 18 November 2026, 16:45 - 17:15

### 2026 State of Network Automation Survey Results
Speakers: Chris Grundemann
Session: Wednesday, 18 November 2026, 17:15 - 17:35

## Thursday, 19 November 2026

### Agentic Networking is here - Introducing the Tools and Techniques Required to be Successful
Speakers: John Capobianco
Session: Thursday, 19 November 2026, 9:10 - 9:45

### Human Driven AI: Who's Actually Driving Your Network's AI?
Speakers: Ryan Booth
Session: Thursday, 19 November 2026, 9:45 - 10:20

### Compliance as an Enabling Constraint: Federating Nautobot Across a Segmented Network
Speakers: Joey Coakley & Jeff Kala
Session: Thursday, 19 November 2026, 11:05 - 11:40

### Excel Is My Source of Truth: A Network Automation Horror Story
Speakers: Toni Sarađan
Session: Thursday, 19 November 2026, 11:40 - 12:15

### I 💖 YANG. Said No Python Developer Ever
Speakers: Urs Baumann
Session: Thursday, 19 November 2026, 9:10 - 10:20

### Digital Twinning at Scale
Speakers: Russ White
Session: Thursday, 19 November 2026, 11:05 - 12:15

### Every Automation Demo Lies: What Building a Disposable Network Lab Platform Taught Me
Speakers: Craig Johnson
Session: Thursday, 19 November 2026, 13:45 - 14:20

### Test Before You Touch the Network: Reproducing Real Device Behavior with Mock Devices
Speakers: Pieter van Os
Session: Thursday, 19 November 2026, 14:20 - 14:55

### From Failure to Recovery: Designing Resumable Network Upgrade Automation
Speakers: Joseph Nicholson
Session: Thursday, 19 November 2026, 15:40 - 16:15

### Let’s Rewind: A Network Automation Do-Over with the NAF Framework
Speakers: Claudia De Luna
Session: Thursday, 19 November 2026, 16:15 - 16:50

### Network Automation Agentified: Self-serving Network Deployments using AI Agents Soup to Nuts
Speakers: Senad Palislamovic
Session: Thursday, 19 November 2026, 13:45 - 14:20

### Stop Funding Hallucinations: A Seasoned Technologist's Guide to Business Success with AI Evaluation
Speakers: Eric Chou
Session: Thursday, 19 November 2026, 14:20 - 14:55

### The adoption gap is an accounting gap: how to measure what your automation returned
Speakers: Jonathon Davis
Session: Thursday, 19 November 2026, 15:40 - 16:15

### Leading Through Radical Change
Speakers: Anna Claiborne
Session: Thursday, 19 November 2026, 16:15 - 16:50

## Friday, 20 November 2026

### What Should You Build When You Can Build Anything?
Speakers: Damien Garros
Session: Friday, 20 November 2026, 9:10 - 9:55 (Closing Keynote)

### Wouldn't It Be Cool If... How One Question Guided a Journey to Governed Autonomous Delivery
Speakers: Sean Mahoney
Session: Friday, 20 November 2026, 9:55 - 10:25

### From PoC to the NOC: A Multi-Agent Network Troubleshooting Platform at Internet2
Speakers: Karl Newell
Session: Friday, 20 November 2026, 11:10 - 11:40

### Deploying IPv6 doesn’t work without automation (but that is true with other stuff too!)
Speakers: Ed Horley
Session: Friday, 20 November 2026, 11:40 - 12:30 (Lightning Talk)

### The Peanut Butter & Jelly Method: Transforming Manual Tasks into Automated Workflows
Speakers: Maximillian Francis
Session: Friday, 20 November 2026, 11:40 - 12:30 (Lightning Talk)

### Network Automation as a Series of Micro-Services
Speakers: Mark Elias
Session: Friday, 20 November 2026, 11:40 - 12:30 (Lightning Talk)

### You Do It, I Do It, Teach It To Me: Using AI To Upskill Network Engineers in Automation
Speakers: Erika Dietrick
Session: Friday, 20 November 2026, 11:40 - 12:30 (Lightning Talk)

### The Real Revolution Isn't AI - It's Us
Speakers: Lynn Gates
Session: Friday, 20 November 2026, 11:40 - 12:30 (Lightning Talk)

