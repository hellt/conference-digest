>>> HOW TO RUN THIS <<<
This is the digest prompt for atscale-product-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/atscale-product-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/atscale-product-2026.md
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

Below is the program for @Scale: Product 2026. Read it and produce a digest
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
conference: @Scale: Product 2026
source_url: https://atscaleconference.com/events/product-2026/
generated: 2026-11-09
registry_key: atscale-product-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## Event Agenda
### Keynote: Creativity in the Age of AI
Speakers: Yair Livne (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-11
No abstract published; title, speakers and materials only.

### The future is products that grow themselves!
Speakers: Jubin Chheda (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-14
Wally is a self-learning loop of agents - an optimizer, verifier and learner loop that identifies opportunities to save CPU or GPU cycles, verifies it for correctness, safety, etc, runs a public A/B test with the solution and then launches a win. The fundamental component is the self-learning loop that updates the harness based on wins/fails. Wally has run 1000s of public tests with a 30% success rate and has saved several millions of dollars.

### World Models for Robotics from Reactor
Speakers: Alberto Taiuti (Reactor)
page: https://atscaleconference.com/events/product-2026/#agenda-item-15
No abstract published; title, speakers and materials only.

### Flywheel of Media Models & Product Velocity
Speakers: Rushaan Mahajan (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-16 | materials: https://atscaleconference.com/flywheel-of-ai-media-models-and-product-velocity/
The best AI media models have crossed the photorealism threshold. The real competitive advantage now lies in how rapidly a model recipe can adapt to product and user feedback.
Log files and traditional metrics solved evaluation for LLMs, but visual breaks those frameworks. A video generation pipeline can run with zero software errors, perfect resolution, and flawless prompt adherence, yet still fail completely. The camera crop might feel off, the motion might stutter, or a ‘cinematic lighting’ edit might accidentally turn skin into unnatural plastic. Visual quality is fundamentally perceptual.
This is where Visual Judges - powered by Visual Language Models (VLMs) - enter the stack.
Novel innovations are driving a flywheel that can accelerate products with media at the center!

### Agentic Product Safety from Pindrop
Speakers: Nicholas Holland (Pindrop)
page: https://atscaleconference.com/events/product-2026/#agenda-item-13
No abstract published; title, speakers and materials only.

### Live Panel: AI Generated Media Provenance at Scale
Speakers: Steve Dilla (Meta), Mohit Diwan (Meta), Sai Chandramouli (Meta), Karthic Veera (Meta), Alexandre Mourachko (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-19
Steve Dilla (Moderator) Mohit Diwan (Panelist) Sai Chandramouli (Panelist) Karthic Veera (Panelist) Alexandre Mourachko (Panelist)

### Content Accessibility at Scale: AI Voice Translations at Meta
Speakers: Esra Cansizoglu (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-29 | materials: https://atscaleconference.com/learn-more-the-research-behind-ai-voice-translations-at-meta/
Language is one of the last boundaries on human connection — and translation blurs it. This talk covers how Meta produces and distributes AI voice-translated Reels at scale: streaming speech translation that improves accuracy and latency at once, and the retrieval-side exploration that solves cold start so a dubbed render actually finds its audience.

### ML Video Codec (MLVC): Research to Product
Speakers: Nabakumar Khongbantabam (Microsoft)
page: https://atscaleconference.com/events/product-2026/#agenda-item-21
Machine learning is opening a new chapter in video compression, with the potential to improve quality, reduce bandwidth, and enable better video experiences across diverse devices and network conditions. But taking ML-powered codecs from research to real-world products requires navigating tough tradeoffs in latency, compute cost, hardware acceleration, compatibility, and quality measurement. This talk shares the product and engineering considerations behind developing and scaling ML Video Codec (MLVC) in Microsoft Teams, and what it takes to turn a promising model into durable product impact.

### Preview Player Reliability and the Agentic Defense Loop on Edits
Speakers: Ravi Shah (Meta), Bhumi Sabarwal (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-22
When you're creating Media in Edits, it should just work — you hit preview and it plays back instantly, captions land accurately, no hiccups while you edit your media. That's been our north star, and we want to share what we did to get there. We improved creation reliability across the full stack — iOS, Android, and the server-side — and users can feel the difference. The big unlock? We built AI agents that basically run our reliability loop for us. They catch regressions, triage the alerts, and trace issues across client and server all the way down to the offending diff — often before the problem even hits production. The results speak for themselves: preview playback failures improved by 88%, which translates to a noticeably smoother creation experience for millions of people.

### Rhythm - Anticipatory Intelligence for Organizations
Speakers: Sundararajan Subramanian (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-24 | materials: https://atscaleconference.com/rhythm-ai-building-anticipatory-intelligence-without-breaking-information-boundaries/
No abstract published; title, speakers and materials only.

### Scaling Media AI: From Pixel-Level Enhancement to Actionable Intelligence on Intel® Xeon®
Speakers: Arnaud Perrier (Intel), Richard Chuang (Intel)
page: https://atscaleconference.com/events/product-2026/#agenda-item-25
Deploying AI video at scale often introduces severe infrastructure bottlenecks and cost challenges, driven primarily by heavy reliance on GPUs alone, leaving CPU cycles underutilized, even as AI is rapidly expanding across all tiers of infrastructure. By leveraging latest-generation Intel® Xeon® processors with Intel® Advanced Matrix Extensions (Intel® AMX), organizations can rebalance their AI workloads by executing compute-intensive workloads such as Video Super-Resolution, inverse tone mapping, and bitrate optimization directly on the CPU alongside encoding pipelines.
Building on this efficient compute foundation, the Intel® Media AI Framework transforms raw media into trusted, searchable AI-ready intelligence, while simplifying deployment of media workloads. Through agentic orchestration, intelligent model routing, reusable MCP tools, and video RAG, the framework powers configurable workflows like semantic search, summarization, metadata enrichment, contextual ad placement, and other MCP-based agent flows. This session demonstrates the larger value of bringing Xeon-based acceleration through the Intel® Media AI Framework to improve user experience, convert media into actionable intelligence, and empower customers to build and scale cost effective media AI pipelines optimized for Intel® Xeon®.

### Fireside Chat: Designing for the Agentic Era
Speakers: Michael Martinez (Meta), Alex Cornell (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-26
AI is shifting from assistant to agent, and that changes what we design. Alex Cornell joins Michael Martinez to trace Muse from inspiration to mainstream, what it took to make an agent feel universal, the use cases nobody predicted, and what happens when users control the experience. Is this the end of designing one product for everybody?

## Video On Demand Sessions
### Adopting AV1 for Real-Time Communication (RTC) at Scale
Speakers: Yu-Chen (Eric) Sun (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-5 | materials: https://atscaleconference.com/adopting-av1-for-real-time-communication-rtc-at-scale/
Adopting AV1 for real-time communication at Meta has been a multi-year effort spanning codec selection, device eligibility, rate control, and error resilience. We’re sharing the technical and operational challenges while deploying AV1 and expanding coverage, and how we addressed them for real-time communication. We’re presenting several technologies for improving AV1 call quality, including rate control and error resilience.Test Ref: https://engineering.fb.com/2026/06/22/video-engineering/adopting-av1-for-real-time-communication-rtc-meta/

### From On-Call to Always-On
Speakers: Sumeet Arora (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-6 | materials: https://atscaleconference.com/from-on-call-to-always-on/
Maintaining products at scale means continually investigating bugs, responding to regressions, and finding problems before users report them. This talk explores how AI agents can support a continuous maintenance loop, from discovering and triaging issues to proposing fixes and verifying outcomes. We’ll examine the engineering challenges behind these systems: providing the right product context, coordinating specialized agents, following work through to completion, and measuring quality. We’ll also discuss how to expand autonomy as reliability improves, while keeping engineers in control of consequential decisions. Attendees will leave with practical design principles for bringing agentic maintenance into their own engineering workflows.

### Beyond “Good Enough”: How deployments accelerate research at the Audio AI Frontier
Speakers: Shaheen Lavie-Rouse (ElevenLabs)
page: https://atscaleconference.com/events/product-2026/#agenda-item-30
As audio AI models saturate traditional benchmarks like word error rate, what comes next? ElevenLabs is scaling a learning loop across research, product, and forward deployed engineering to find the new frontier: emotional intelligence and taste — audio that carries the speaker’s intent and conviction. Drawing on ElevenLabs’ work dubbing Reels, this talk shows how deployments revealed a trade-off between preserving a speaker’s own voice and sounding like a native speaker in the target language, and the new cloning strength control built to manage it.

### Ship Fast, Break Nothing: How AI Tests What AI Builds
Speakers: Sophie Zeng (Meta), Sreeja Thummala (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-7
Shipping faster at scale requires AI not just writing code, but catching the bugs that would slow you down. This talk explores Meta's Just-in-Time (JiT) Catching Test system — where AI autonomously generates tests designed to fail, surfacing bugs before code lands. At Meta, AI now powers every stage of the quality gate — from generating code-change-aware catching tests, to LLM-based assessors that select which catches deserve human attention. In our presentation, we'll show how this system — deployed across hundreds of millions of lines of code — proactively prevents serious production failures while enabling engineers to ship with speed and confidence.

### AI compression for AOM from NVIDIA
Speakers: Manindra Parhy (NVIDIA)
page: https://atscaleconference.com/events/product-2026/#agenda-item-31
No abstract published; title, speakers and materials only.

### Chasing a Moving Target: Going AI-Native on Edits' Video Seek Engine
Speakers: Boris Baracaldo (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-8
Scrubbing a video looks trivial, but the real problem is showing correct frames, frequently, while the user keeps moving the target across compositions of overlapping tracks and effects, under hard mobile device limits. A scrub is a continuous stream of seek requests of different shapes, fast or slow, forward or backward, each resolving the same decisions differently: distance to the nearest keyframe, which frame to show and how soon, when to abandon work already in flight; across device tiers, content, and composition shape, no fixed policy covers that space. In Edits we engineered an engine that serves frames fast, smoothly and accurately while requests keep arriving, interrupting stale work to render at every transition, seeking GOP-aware off a keyframe list, tracking the finger on backward scrubs while decoding runs the other way, and trading precision for speed where the user cannot tell; it delivered a 10x improvement on seek latency and frames shown per second. No single policy covers the breadth, so we are going AI-native: refactoring into a portable system that plugs into Meta's Family of Apps, developing agentic just-in-time observability into production behavior and skills that help coding agents extend the engine and validate their own work. The vision is an agentic system that profiles production data at scale, generates algorithmic variations, and experiments to to evaluate what can ship, with a human on the loop.

### How to Discover the Future
Speakers: Matt Schlicht (Meta)
page: https://atscaleconference.com/events/product-2026/#agenda-item-32
No abstract published; title, speakers and materials only.

