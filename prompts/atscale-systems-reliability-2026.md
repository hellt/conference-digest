>>> HOW TO RUN THIS <<<
This is the digest prompt for atscale-systems-reliability-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/atscale-systems-reliability-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/atscale-systems-reliability-2026.md
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

Below is the program for @Scale: Systems & Reliability 2026. Read it and produce a digest
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
conference: @Scale: Systems & Reliability 2026
source_url: https://atscaleconference.com/events/systems-reliability-2026/
generated: 2026-11-09
registry_key: atscale-systems-reliability-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## June 25
### Keynote from Meta
Speakers: Surupa Biswas (Meta)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-4 | video: https://www.youtube.com/watch?v=Ei4AbefZxbg
Surupa will share the latest progress from Meta's mission to build the future of human connection and the technology that makes it possible, including infrastructure for AI by leveraging agentic innovation across the stack.

### Our Journey to Safely Unleash Agents at Meta Scale
Speakers: David Pariag (Meta)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-6 | video: https://www.youtube.com/watch?v=QHg0HeqIcqY | materials: https://atscaleconference.com/metas-journey-to-safely-unleash-agents-at-scale/
Engineering at Meta is in the midst of a productivity revolution, driven by AI. Our goal is to dramatically increase engineering velocity by using agents to build new systems and operate existing ones. Teams are not just using AI to write code faster; they’re also leveraging AI to debug GPU failures, remediate system outages and more.
To unleash agentic productivity, we have embarked on a journey to safely enable agentic access to Meta’s systems. This talk will dive into what we’ve learned so far - building internal agents, deploying 3rd party agents, observing agents' interactions with our Infra, and deploying guardrails to prevent destructive actions.

### The Agentic Infrastructure Gap: In-Distribution Languages Make It a Coding Problem
Speakers: Joe Duffy (Pulumi)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-7 | video: https://www.youtube.com/watch?v=P4PpoTH9ADc
To handle the scale and velocity of AI-written code, we will have no choice but to let AI manage our infrastructure too. Yet Andrej Karpathy recently described getting an app running in production as “assembling IKEA furniture”: cloud consoles, API keys, copy-pasted config, glue, ... all things that sit outside the code an LLM can reason about. Frontier models are trained on billions of lines of real languages like Python, TypeScript, and Go, and vanishingly little bespoke DSLs and manual procedures. By modeling infrastructure in code space so the LLM can do what it does best — code — we just need an oracle that can map code changes back to infrastructure outcomes. In this talk, I’ll share what we’ve learned at Pulumi working alongside leading AI companies and frontier labs to build for a world where agents manage infrastructure. The platforms that win in this new era will look different, but many of the human-ergonomic benefits of programming languages are what will get us there.

### Extending Meta to the Public Cloud
Speakers: Dinesh Govindasamy (Meta), Sargun Dhillon (Meta)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-8 | video: https://www.youtube.com/watch?v=p08-ef0QKYQ
Meta has a massive amount of internal infrastructure, but the demand for GPU compute led us to look to the cloud to grow our footprint. This led to our initial forays into cloud, and what it took to enable and integrate into Meta’s overall infrastructure footprint. In order to create capacity hyperliquidity, we’ve leveraged multi-cloud as a form of optionality. Come learn how we’ve fully integrated cloud into our platform, OS, and fleet management stack to make the experience ubiquitous for our internal customers.

### Live Q&A Session
Speakers: David Pariag (Meta), Sargun Dhillon (Meta), Dinesh Govindasamy (Meta), Joe Duffy (Pulumi)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-9 | video: https://www.youtube.com/watch?v=ji4_8vr2UKU
No abstract published; title, speakers and materials only.

### AI Storage Blueprint
Speakers: Sidharth Bajaj (Meta), Venkatraghavan Srinivasan (Meta)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-19 | video: https://www.youtube.com/watch?v=xc_BxLsijWA
The rapid, exponential growth in model capabilities and training dataset sizes over the last few years has accelerated AI innovation. New frontier models are now being released in a matter of weeks, down from months just a year ago. This pace makes reliable, consistent fast access to storage essential for managing both the speed and cost of development. This presentation will detail how we evolved Meta's Storage Architecture to overcome two key hurdles: optimizing GPU Utilization and maximizing Research Velocity.

### LIVE PANEL WITH AURORA, GOOGLE, META AND MICROSOFT
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-15 | video: https://www.youtube.com/watch?v=HrYag7rM65s
Saad Syed (Google) Mark Jen (Meta) Viral Mehta (Aurora) Jenny Lawrance (Microsoft)

### Keynote from Meta
Speakers: Peter Hoose (Meta)
page: https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-16 | video: https://www.youtube.com/watch?v=lCgEybKXE34
Peter will share the latest progress from Meta's mission to build the future of human connection and the technology that makes it possible, including infrastructure for AI by leveraging agentic innovation across the stack.

## June 25 — Track 1 (Level 1 Stage)
### Teaching AI to Fight Fires: Autonomous Reliability Agents at Meta Scale
Speakers: Gaurav Mitra (Meta)
video: https://www.youtube.com/watch?v=irtqkj3fHxM | materials: https://atscaleconference.com/teaching-ai-to-fight-fires-building-the-reliability-flywheel-at-meta/
In December 2024, a single config change at Meta took 50+ engineers and 28 hours to recover from. What if an AI agent had detected the cascade in seconds and proposed the rollback before it propagated?
Over the past year, we've been building exactly that. This talk introduces the reliability flywheel: a system that encodes the best on-call engineer's investigation methods into an always-on copilot that gets sharper with every incident. Our investigation agent has handled 1,000+ incidents across Meta's recommendation systems, cutting detection-to-mitigation time by 60% and matching senior on-call engineers ~80% of the time. It correlates signals across time-series metrics, deployment logs, configuration changes, and infrastructure health through a context-engineered architecture: structured tool servers and reusable workflows.
We'll trace the full progression: (1) pattern identification across hundreds of incidents, (2) autonomous investigation that matches human accuracy, (3) supervised mitigation for low-risk reversible actions, and (4) self-healing as the long-term outcome.
You'll leave with what worked, what didn't, and how we think about the trust boundary between autonomous agents and human engineers in production.

### Experience Productionizing and Operating GB200 clusters
Speakers: Ankur Srivastava (NVIDIA), Sachin Kumar Lakharia (NVIDIA), Douglas Wightman (NVIDIA)
video: https://www.youtube.com/watch?v=1o4emwSid78
The NVIDIA GB200 NVL72 functions as an exascale computer within a single rack. Maximizing the utilization of its NVLink fabrics through proper scheduling allows AI training jobs to significantly leverage the substantial networking bandwidth this system offers. Notably, recent MLPerf training results (>2.6x improvement with recent MLPerf training) confirm that GB200 NVL72 provides substantial performance gains across all AI workloads. This presentation will cover key topics related to operating and optimizing large GB200 clusters, including: Topology-aware scheduling within Slurm. Recommendations for optimal GPU occupancy and scheduling (slurm simulator). Our experience bringing up and running a large GB200 cluster. (Healtch checks, Supporting large scale training experience, scheduling, rack testing, slow nodes etc)

### Building Privacy Aware Infrastructure in the AI-Native Era
Speakers: Rituraj Kirti (Meta)
video: https://www.youtube.com/watch?v=q9RSv2ltZtU
Building privacy-aware infrastructure in the AI-native era requires systems that can learn, evaluate, and operationalize improvements continuously—at the scale of millions of data assets. This talk presents an AI-native approach through a case study of AI-native asset classification: a hybrid deterministic rules engine with LLM fallback that transforms messy context (metadata, lineage, code references, scan signals) into enforceable privacy controls. We’ll highlight ground truth (GT) + evaluation (eval) self-improvement loops, where active learning focuses human review on high-value examples, an LLM-as-Judge provides scalable review signal (including kappa reliability), and evaluation gates prevent regressions and circular reinforcement. Finally, we’ll show how high-performing LLM behavior is distilled into auditable rules.yaml, driving LLM usage toward near-zero while improving determinism, latency, and cost. Attendees will leave with practical patterns for building privacy-by-design infrastructure that converges, exports human-readable logic, and monitors drift in production.

## June 25 — Track 2 (Level 4 Stage)
### [Almost] Fail & Tell: Stop The World
Speakers: Phil Lopreiato (Meta), Rahul Iyengar (Meta)
video: https://www.youtube.com/watch?v=-0v6UUPLvF8 | materials: https://atscaleconference.com/almost-fail-tell-stop-the-world/
In March 2025, Meta avoided an major outage that would have resulted in prolonged sitewide unavailability. Instead, we were able to quickly contain the issue in a matter of minutes and avoid the worst case scenario. This is a story of how we re-bootstrapped the infrastructure control plane in an entire region, on the fly, using emergency tooling. It's a showcase of how to put DR-preparedness and calm incident response into practice. And it's a pretty cool story.

### Securing Production Debugging at Hyperscale
Speakers: Shridivya Sharma (Microsoft), Luke Kelly (Microsoft)
video: https://www.youtube.com/watch?v=UAs6-gNzFks
This presentation will go over how Microsoft uses SSH to debug across our global fleet of K8s clusters at hyperscale. We'll cover how we integrate that with JIT elevations and Task-Based Execution in a secure and auditable way. We will alsogo over how we use these building blocks to engage AI and the Semantic Kernel to empower our on-call engineers to resolve issues quickly.

### Taming AI Infrastructure Failures with Agentic Debugging
Speakers: Phillip Liu (Meta)
video: https://www.youtube.com/watch?v=9wc0556pIwg | materials: https://atscaleconference.com/leveraging-agents-to-debug-nccl-watchdog-timeouts/
NCCL watchdog timeouts are a common failure mode in distributed AI model training. They impact not only Meta, but broadly affect anyone running PyTorch distributed training—and they’re notoriously hard to debug: even experts can spend hours triaging a single incident, and non-experts may be unable to root-cause them at all. Over the past year, we investigated NCCL watchdog timeouts internally at Meta and partnered with the PyTorch community to categorize the major root-cause buckets. We then distilled these learnings into a practical decision tree and runbook to speed up triage and make debugging more accessible. We also explored using agent-based approaches to assist root-cause analysis and saw strong early results. (More details TBD.)

