>>> HOW TO RUN THIS <<<
This is the digest prompt for denog-18. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/denog-18.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/denog-18.md
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

Below is the program for DENOG 18 (Essen). Read it and produce a digest
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
conference: DENOG 18 (Essen)
source_url: https://www.denog.de/de/meetings/denog18/agenda.html
generated: 2026-11-22
registry_key: denog-18
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## 2026-11-15 — Floor 6, next to Hall B, south side / main station

### Packet A38 - Let's Play Internet on paper!
Speakers: Vanessa Gaube
page: https://cfp.denog.de/denog18/talk/AARUD3/
You're new at DENOG? You're new in Networking? You're doing this forever, but want to experience the internet from a whole new perspective?

Let's play a game! 
Did you already do routing tables on paper, route updates on paper or traceroutes on paper?
How fast can your group process routing updates just with some paper, a pen and a cleaning towel?
How quickly can the entire network converge?

This session is especially intended for first-time-attendees, but of course, everyone is welcome!
Feel free to join at any time, without reservation etc.!

Material will be uploaded at https://welcome.denog.de/materials/a38/ after the event.

## 2026-11-15 — Workshop Room 408

### OpenPGP Key Management Hopefully Done Right
Speakers: Marc Haber
page: https://cfp.denog.de/denog18/talk/CEXYQV/ | slides: https://cfp.denog.de/media/denog18/submissions/CEXYQV/resources/MarcHaberOpenPGP_8DPBcu3.pdf
This workshop gives an overview about modern management of OpenPGP Keys. Online documentation suggests that you have an offline key and subkeys, the latter preferably on a hardware device. But there is hardly one place where there are hands-on instructions to create those. This workshop intends to have participants aquire that experience.
This workshop will not give more than a "you know that already" appraoch to public key cryptography. It will begin with OpenPGP basics. The speaker is a Debian Developer, so his main application of OpenPGP is signing things, but of course encryption will be handled as well. The practical exercises will be done on Linux.

After an introduction into OpenPGP, the participants will get an overview about what are best practises regarding OpenPGP keys:
- an offline (certification only) primary key that will never see the internet and
- subkeys (signature, encryption, authentication) that will be created on the offline system and then transfered to a OpenPGP Smart Card (such as a Yubikey).
- how to build and use an offline, immutable Linux system (based on Debian Live on a Raspberry Pi 4)
- Introduction to OpenPGP Smart Cards
The workshop will also suggest workarounds for the numerous gotchas the speaker experienced on his own journey to OpenPGP best practises.

Af the end of the talk, participants will have a primary key with subkeys and will have had the experience of exchanging keys, signatures and encrypted messages via a pad. It is suggested to throw away all key material after the workshop and to start over again in a quiet place with lots of concentration about doing things right.

## 2026-11-15 — Workshop Room 413 / 414 / 415

### Build It. Test It. Fix It. – Datacenter-Verkabelung inklusive Messung und Fehlersuche
Speakers: Juergen Rummelsberger, Robin Bartelsen, Daniel Frowein
page: https://cfp.denog.de/denog18/talk/YYFF9Y/
Dieser praxisorientierte Workshop vermittelt den Aufbau, die Installation und die Qualifizierung moderner passiver Netzwerkinfrastrukturen in einer realitätsnahen Datacenter-Umgebung.
Die Teilnehmer planen, installieren und prüfen eigenständig eine strukturierte Verkabelung. Vom mechanischen Aufbau über das Spleissen und Patchen bis hin zur professionellen Abnahmemessung werden alle wesentlichen Arbeitsschritte praxisnah durchgeführt.
Ziel des Workshops ist es, den Teilnehmern nicht nur theoretisches Wissen zu vermitteln, sondern ihnen die Möglichkeit zu geben, typische Aufgaben aus dem Rechenzentrums-Umfeld selbstständig durchzuführen sowie moderne Mess- und Prüftechnologien in realen Anwendungsszenarien kennenzulernen.
Workshop-Konzept
Im Mittelpunkt des Workshops steht der eigenständige Aufbau eines passiven Netzwerks in einer realitätsnahen Datacenter-Umgebung. Die Teilnehmer übernehmen typische Aufgaben aus den Bereichen Spleissen, Verkabelung und Installation. Nach dem erfolgreichen Aufbau werden sämtliche Verbindungen professionell geprüft, analysiert und dokumentiert.
Dabei führen die Teilnehmer typische Abnahme-, Qualifizierungs- und Fehlersuchmaßnahmen durch, wie sie im täglichen Betrieb moderner Rechenzentren und Unternehmensnetzwerke erforderlich sind.
Gemeinsam mit ConnectCom und EXFO stellen wir die erforderliche Infrastruktur, moderne Messtechnik sowie das Expertenwissen für einen erfolgreichen Infrastrukturaufbau bereit. Die Umsetzung erfolgt anhand eines vorgegebenen Verkabelungs- und Dokumentationskonzepts.
 
Die praktischen Aufgaben umfassen unter anderem:
•	Spleissen von Glasfaserverbindungen in Patchfeldern
•	Anschließen von Netzwerkkabeln
•	Montage von Patchfeldern und Infrastrukturkomponenten
•	Patchen von Glasfaser- und Kupferverbindungen
•	Aufbau einer strukturierten passiven Verkabelung
•	Inspektion und Bewertung von Steckverbindungen
•	Dämpfungsmessungen der installierten Strecken
•	Durchführung von IOLM-Messungen zur Streckenanalyse und Fehlerlokalisierung
•	Systematische Fehlersuche und Fehlerbehebung
•	Dokumentation der aufgebauten Infrastruktur und der Messergebnisse
 
Mehrwert für die Teilnehmer
•	Praxisnahe Hands-on-Erfahrung statt reiner Theorie
•	Eigenständiger Aufbau einer passiven Netzwerkinfrastruktur
•	Kennenlernen aktueller Glasfaser- und Messtechnik
•	Durchführung realer Aufbau-, Prüf- und Abnahmeverfahren
•	Systematische Fehlersuche, Analyse und Fehlerbehebung
•	Erfahrungs- und Wissensaustausch mit Experten
•	Verständnis für Planung, Installation, Qualifizierung und Dokumentation moderner Netzwerk- und Datacenter-Infrastrukturen

## 2026-11-15 — Workshop Room 419

### Death to Perfectionism: Get unstuck!
Speakers: Susi Bauer
page: https://cfp.denog.de/denog18/talk/EA73XB/
_“I’m a perfectionist”_ is a popular humble brag answer to the classic interview question _“What’s your biggest weakness?”_ – a weakness that conveniently sounds like a strength. While perfectionism lures us in with its promise to help, most of us know that it can have some very real downsides.

In this **hands-on workshop**, we’ll unpack what we actually mean when we talk about “perfectionism”, where it might be helpful – and where it starts getting in our way. We’ll explore how perfectionism can show up as procrastination, overthinking, endless tweaking, fear of getting things wrong, or simply never feeling like something is good enough. Most importantly, we’ll look at practical tools and exercises to help break those patterns and make it easier to take action, even when things aren’t perfect.

The aim isn’t to lower your standards – it’s to become more intentional about when high standards are useful, and when they’re holding you back.
## What You’ll Learn:

- **Spotting Perfectionism in Disguise**: Recognise the less obvious ways perfectionism can show up – from procrastination and over-preparing to endlessly tweaking work that was already good enough.
- **Understanding the Cost:** Explore how perfectionism can affect productivity, confidence, creativity, decision-making, and our willingness to take risks or try something new.
- **Getting Out of the Overthinking Loop**: Learn practical techniques for making decisions, getting started, and taking action before you feel completely ready.
- **Redefining “Good Enough”**: Learn how to set more useful definitions of done, rather than relying on an impossible feeling of “perfect”.
- **Taking Imperfect Action**: Leave with a small, concrete action you can put into practice straight away – because sometimes the best way to beat perfectionism is to start.

## Why Attend?
This workshop is for anyone who has ever spent far too long tweaking something that was probably fine already, put something off because they didn’t know how to do it “right”, or found themselves stuck trying to make the perfect decision.
You’ll leave with a better understanding of your own perfectionist patterns and a toolbox of practical strategies for getting unstuck. Because the goal isn’t to stop caring about doing good work – it’s to make sure that the pursuit of perfect doesn’t stop you from doing the work at all.

### Death to Perfectionism: Get unstuck!
Speakers: Susi Bauer
page: https://cfp.denog.de/denog18/talk/3TP9RL/
_“I’m a perfectionist”_ is a popular humble brag answer to the classic interview question _“What’s your biggest weakness?”_ – a weakness that conveniently sounds like a strength. While perfectionism lures us in with its promise to help, most of us know that it can have some very real downsides.

In this **hands-on workshop**, we’ll unpack what we actually mean when we talk about “perfectionism”, where it might be helpful – and where it starts getting in our way. We’ll explore how perfectionism can show up as procrastination, overthinking, endless tweaking, fear of getting things wrong, or simply never feeling like something is good enough. Most importantly, we’ll look at practical tools and exercises to help break those patterns and make it easier to take action, even when things aren’t perfect.

The aim isn’t to lower your standards – it’s to become more intentional about when high standards are useful, and when they’re holding you back.
## What You’ll Learn:

- **Spotting Perfectionism in Disguise**: Recognise the less obvious ways perfectionism can show up – from procrastination and over-preparing to endlessly tweaking work that was already good enough.
- **Understanding the Cost:** Explore how perfectionism can affect productivity, confidence, creativity, decision-making, and our willingness to take risks or try something new.
- **Getting Out of the Overthinking Loop**: Learn practical techniques for making decisions, getting started, and taking action before you feel completely ready.
- **Redefining “Good Enough”**: Learn how to set more useful definitions of done, rather than relying on an impossible feeling of “perfect”.
- **Taking Imperfect Action**: Leave with a small, concrete action you can put into practice straight away – because sometimes the best way to beat perfectionism is to start.

## Why Attend?
This workshop is for anyone who has ever spent far too long tweaking something that was probably fine already, put something off because they didn’t know how to do it “right”, or found themselves stuck trying to make the perfect decision.
You’ll leave with a better understanding of your own perfectionist patterns and a toolbox of practical strategies for getting unstuck. Because the goal isn’t to stop caring about doing good work – it’s to make sure that the pursuit of perfect doesn’t stop you from doing the work at all.

## 2026-11-15 — Workshop Room 420

### BGP for networks who peer
Speakers: Wolfgang Tremmel
page: https://cfp.denog.de/denog18/talk/M9H8P7/
Workshop about the basics of BGP. Topics include:
* Prefixes and Autonomous Systems
* Why you also need an IGP (like OSPF, IS-IS)
* iBGP: BGP within your network
* eBGP: Talking to your neighbours
* Multihoming and Peering
* BGP Best Path Selection

Bonus-Topics, if time permits:
* BGP Communities
* BGP Security

Lab experiments will be done using FRRouting, so participants do need a laptop. No special software is needed, but make sure your web-browser can access a HTTPS page on ports 7002-7099.

## 2026-11-15 — Workshop Room 421

### advanced SSH
Speakers: Felix Schüren
page: https://cfp.denog.de/denog18/talk/QWSNGK/
You already know how to generate keys and authenticate securely. But SSH can do so much more. In this advanced workshop, we'll explore the powerful features that transform SSH from a simple login tool into an essential part of your workflow—port forwarding, proxy jumping, SSH certificates, control channel reuse, and crafting bulletproof ssh_config files. Walk out with the techniques that turn SSH from a necessity into a superpower.
Many SSH users hit the same frustrations: managing dozens of hosts with repetitive parameters, struggling with multi-hop networks, or wasting time on repeated connection overhead. This workshop directly addresses these pain points.

We'll start by diagnosing the problems in a typical ssh_config, then systematically solve them through five core techniques:

Port Forwarding — Local and remote variants for securely accessing databases on private networks and exposing local services to remote machines. You'll understand when to use each and why it matters for security.

Proxy Jumping — Build practical multi-hop scenarios (2-3 hops) and see how ProxyJump eliminates the bastion-host dance.

SSH Certificates — A game-changer for teams managing multiple servers. We'll cover generation, deployment, and why they're superior to key-per-host approaches.

Control Channel Reuse — Understand connection multiplexing and how ControlMaster/ControlPath cuts SSH connection overhead dramatically.

ssh_config Mastery — Build a comprehensive config from scratch using Host patterns, wildcard matching, conditional includes, and automation that grows with your infrastructure.

By the end, you'll have working examples you can adapt immediately.

### From Networks to Products: Breaking the Consulting Mold (2026 edition)
Speakers: Thomas Weible, Moritz Frenzel
page: https://cfp.denog.de/denog18/talk/TGXGP9/
The network engineering industry is rich with technical talent but remains surprisingly underrepresented in the world of product-driven startups. In 2025 Thomas Weible (CTO and Co-Founder, FLEXOPTIX) and Moritz Frenzel (CEO and Co-Founder, EdgeOps) started to share their entrepreneurial journeys, each shaped by a deep technical background and a commitment to building products instead of pursuing the traditional consulting route.

One year later at EdgeOps (Y 2) and FLEXOPTIX (Y 18) a lot of things did happen in their product companies. The session offers an exciting journey surging awesome highlights and annoying pitfalls we've experienced in the last year timeframe. If you weren't convinced in the first edition of this workshop in 2025, maybe now?

This workshop aims to inspire and equip engineers, founders, and future entrepreneurs with the confidence and perspective to transition from services to products, still shifting from billing hours to building something that lasts, while also fostering connections between existing and aspiring founders. 

On more thing, Bernd Sontheimer (formerly sdt.net, now TNG) committed to share his experiences of the merge and acquisition process in 2023.

## 2026-11-15 — Workshop Room 505

### BGP Workshop 5.0
Speakers: Vincentz Petzholtz, Sebastian Graf, Benedikt Heuser
page: https://cfp.denog.de/denog18/talk/TEXXSQ/
Want to perform the bgp handshake in real life based on a realistic topology? We got you covered ... in this workshop for intermediates we will dive into some network basics of bgp driven networks and also explore route filtering best practices (mainly for the DfZ = default free zone).

After some theory every attendee will receive one network node to configure. The fellow participants will be your peers. You will depend on the peers to reach your goals.

Teams work together in small groups. One group jointly manages an AS consisting of 3 routers and a customer downlink router. Troubleshooting takes place across groups in order to verify the corresponding availability within the lab topology.

Warning: You will have to socialise with the peers around you!

Topics Covered:
- Introduction into Internet/Routing Hierarchy
- Routing/Announcement Basics/Strategy
- Route Filtering
- Lab Introduction

Pre-requisites:
- Network Fundamentals, user level UNIX and maybe some system administration,
- Some use of network design preferably TCP/IP-based is also helpful.
- Dynamic routing Fundamentals (BGP, ISIS/OSPF is a plus)
- Participants must have technical hands on experience of routers.

Some experience with EOS or a comparable CLI will be helpful.

## 2026-11-15 — Workshop Room 506

### WDM Basics
Speakers: Nicola 'nicoduck' von Thadden
page: https://cfp.denog.de/denog18/talk/PJYNNC/
Modern optics incorporate WDM technology out of the box, 100G-LR4, 100G-CWDM4 and other variants are common to everyone. But what does that mean and how does CWDM and DWDM work, if not already in a box.
I'll give an overview about different WDM types, channels and hardware. I'll also bring some devices to show, but I currently do not think it will be a hand-on session on some switches (that could change, if there is a benefit, which I currently do not see).

### From Netbox to Network - A Hands-On ISP Automation Workshop for Beginners
Speakers: Michael Fischer, Johannes Störmer
page: https://cfp.denog.de/denog18/talk/KGB9PT/
How can network infrastructure be described centrally, versioned consistently, and deployed automatically?

In this hands-on introductory workshop, participants build and automate a small service provider network using NetBox, Git, Ansible, and a virtual lab environment.

Working in small teams, they use **NetBox** as the Source of Truth for devices, interfaces, IP addresses, and routing information. The structured data is then transformed into network configurations using Jinja2 templates and deployed through an automated workflow.

The workshop focuses on the practical interaction between network data, templates, version control, and automation. Participants will learn about network data modeling in NetBox, create and modify existing data and templates, execute the deployment process, and validate the resulting configurations.

The workshop is explicitly designed not only for participants who already have experience with NetBox or network automation, but also for curious network engineers who want to gain their first practical experience in a guided and approachable environment. It provides an opportunity to explore the concepts hands-on, understand how the individual components interact, and experience a complete automation workflow without having to build the underlying lab platform themselves.

After this workshop, participants should be able to explain the role of a Source of Truth within a network automation workflow, model and maintain basic network data in NetBox, understand how Git, Jinja2, and Ansible work together.

Most importantly, they will leave with a practical understanding of how Source-of-Truth-driven automation can provide a foundation for more reproducible, consistent, and scalable network operations in their own environments.

This workshop is not a comprehensive NetBox, Ansible, Jinja2 or Python training, nor does it present a production-ready automation platform. Instead, it offers a guided introduction to the core principles of Source-of-Truth-driven network automation and demonstrates how the individual components work together in a simplified end-to-end workflow.

#### Topics Covered:
- Introduction to Network Source of Truth
- Netbox Data Model
- Possible Deployment Pipelines
- Jinja2 configuration templating

####  Prerequisits:
- No previous experience with NetBox or network automation is required.
- No extensive programming experience is required.
- Basic knowledge of IP networking and routing is recommended.

The lab environment and all required tools are provided.
Participents are expected to bring 
- Their own laptop with a working Browser and ssh client

## 2026-11-15 — Workshop Room 701

### Mastering gRPC for Network Management, Monitoring and Automation
Speakers: Gordon Gidófalvy, Florian Schwarz, Mathis Bramkamp
page: https://cfp.denog.de/denog18/talk/JXFHES/ | slides: https://cfp.denog.de/media/denog18/submissions/JXFHES/resources/DENOG18-gRPC-20261115_6VxmwWD.pdf
In this workshop session, we will explore how the high-performance protocol gRPC can be used to interact with a modern network OS: monitoring, configuration, operations, and even beyond!

## Content

The workshop will touch on what gRPC is, and which gRPC services are available for managing networks. We will try out the full suite of gNxI protocols using open source tools, namely:
- **gNMI**: used for network management and monitoring
- **gNOI**: for operational tasks, like image upgrades and reboots
- **gNSI**: security-related tasks, e.g. gRPC access policy and certificate rotation
- **gRIBI**: manipulating the RIB programmatically, injecting routes on-demand

## Prerequisites

We will be providing participants with a VM pre-loaded with all necessary tools and network topology.

**No previous programming or gRPC experience required for this beginner-friendly workshop!**

## 2026-11-15 — Workshop Room 811

### poor man - great wifi
Speakers: Ulf Weikert
page: https://cfp.denog.de/denog18/talk/ASK3LK/ | slides: https://cfp.denog.de/media/denog18/submissions/ASK3LK/resources/poor-man-great-wifi_PuKCgHR.pdf
How hard can it be to NOT use wires? Sometimes pretty hard! But it doesn't need to be!

In this workshop you will learn what needs to be done to have a great wireless network. 
And how you can achieve that without getting bankrupt.
For the better half of a decade I have been doing professional work around wifi. 
WLAN on a campus or office complex, logistic warehouses, hospitals etc. have been my bread and butter for more than 5 years. 
With a change in employment my responsibilities shifted, but the passion never died. And for the last couple of years I helped with wifi deployments on smaller gigs like Nordlicht Demoparty, medium festivals like Stemweder Open Air and bigger events like Chaos Communication Congress or WHY2025. 

In this workshop I will give an overview and introduction of what is possible with today's free (and maybe open source) tools for getting great reliable wifi at home. 

My goal for the full day workshop is for you to; 

- being able to differentiate between good wifi and bad wifi
- being able to articulate your requirements for your own wifi environment
- being able to better put the big players in the market into context
- being able to successfully implement small projects (e.g. wifi at your or your friends home)
- being able to better work as an intermediary for wifi consultants in case your project got bigger

The main focus will be on practical applications. With a short sidequest on the theoretical side. 

While all of this is applicable in a broader context, we will NOT dive deep into every single nuance of wifi tuning. The tradeoff in this workshop will be to invest less of hard cash for a bit more of personal work hours.

## 2026-11-15 — Workshop Room 901

### Behind the Label: How MPLS Network Transport Really Works
Speakers: Christian Giese, Elmar Kirchner
page: https://cfp.denog.de/denog18/talk/MWJXKM/
MPLS once was the center of attention in many network talks, workshops and training. Still today it is a predominant technology in use in many networks.

However, those who joined the network community in the past years or almost a decade now from enterprise and datacenter angles, have found very little opportunity to dive into the topic of MPLS. Many perceive the communities still working with expert level MPLS topics hard to engage with.

This workshop tries to go back in time and provide a guided journey through the development of MPLS and how it evolved over the years. It wants to cover original ideas, what became of them and how various protocols over time solved problems of their time and ultimately resulted in the most modern use of MPLS and related technologies for those who were not around when all this was heavily discussed in every other training course.

This workshop is addressed to absolute beginners and those who heard little about MPLS and have a few working assumptions but no solid background.
It does not aim to go to expert level, rather give a solid structure and overview so that context exists for the concepts in play.

The talk will mainly focus on the history, theories and how protocol implemented them as well as some hands-on components of label exchange and packet forwarding in groups while applying various protocols.

Participants should be beginner level or completely new to MPLS.
Basic knowledge of networking concepts is recommended.

## 2026-11-16 — Saal A

### Retrofitting API into a routing software
Speakers: Maria Matejka
page: https://cfp.denog.de/denog18/talk/3BJJKY/ | slides: https://cfp.denog.de/media/denog18/submissions/3BJJKY/resources/retrofitting_6O6za7x.pdf
Configuring a router via text CLI and configuration file editing is not very 2026. In BIRD, we are trying to catch the departing train and implement a CORECONF variant of an IETF-standardized YANG-based API. We've created a prototype but getting things right is harder than it seems. This is a report on what has already gone wrong and what is expected to fail in the future.
While a standardized API looks simple on surface, the reality is much more convoluted. There are three standards for communication, NETCONF, RESTCONF and emerging CORECONF, each of these with slightly different semantics. Lots of the YANG modules are not yet finalized and implementation specifics  are leaking into them from their authors. In the best case, we end up with the implementations slightly differing in what is implemented, and being mostly compatible for automated access. Yet, the actual future may be much more dire, with the users having to cater for three different protocols and vastly diverse implementation status of the standardized API. All of that is spiced up by performance challenges.

With BIRD, we are kinda late to the party. Everybody has some API working. That brings a disadvantage on the market, but it also allows us to study the previous attempts, see possible problems and implement our API to our standards, including high performance and stability. We can also see emerging compatibility issues and there are some attempts to develop proxies and convertors to bridge the gaps.

### EVPN - One Control Plane to Rule Them All
Speakers: Patrick Prangl
page: https://cfp.denog.de/denog18/talk/VCQLXW/ | slides: https://cfp.denog.de/media/denog18/submissions/VCQLXW/resources/DENOG18_2026_EVPN_OneCPToRul_Zcb1Ou8.pdf
Modern service provider networks are evolving rapidly: transports like VXLAN, MPLS, Segment Routing and SRv6 are being used while many legacy control plane protocols are still in operation. This often results in unnecessary complexity, multiple signalling mechanisms and operational overhead.

In this talk, I’ll explore how BGP EVPN has evolved into a transport-agnostic control plane capable of unifying services across MPLS, VXLAN, SR, and SRv6. The goal is simple: move away from fragmented legacy protocols and toward a single, scalable control plane for L2 and L3 services.

We’ll look at recent EVPN innovations and discuss how service providers can benefit from simplifying their architectures while preparing their networks for future transport technologies.

### EVPN for humans
Speakers: Robin Christ
page: https://cfp.denog.de/denog18/talk/YTBLUH/ | slides: https://cfp.denog.de/media/denog18/submissions/YTBLUH/resources/EVPN-for-humans-live-v0.0.5_LAEltLh.pdf | slides: https://cfp.denog.de/media/denog18/submissions/YTBLUH/resources/EVPN-for-humans-full-v0.0.5_PLcEbkz.pdf
EVPN is everywhere, be it datacenter, service provider or campus - and every vendor says you need it. But EVPN rightfully has a reputation problem. It is rarely truly understood, even by vendors themselves, and often treated as a black box. The RFCs read like tax law, and the quality of vendor documentation doesn’t help either.
This talk aims to be nothing less than a gentle introduction and a deep dive into EVPN at the same time. 
We‘ll explore the abstract concepts and frequently misused terminology in order to build an intuitive mental model. 
We will also look into the often overlooked origins of EVPN, which explain many of its design decisions and behaviours.

Finally, we’ll take a look at tricky mechanisms like Anycast Gateways and Multihoming, so your next EVPN debugging session doesn’t become another unplanned nightshift.

### Beyond Bandwidth: Why it doesn't solve user experience in Wi-Fi, WAN, and LAN Environments
Speakers: Falk Bachmann
page: https://cfp.denog.de/denog18/talk/FUCBPB/ | slides: https://cfp.denog.de/media/denog18/submissions/FUCBPB/resources/DENOG18_Bandwidth_v1_Kux194k.pdf
This talk examines latency as an end-to-end property of enterprise networks, not just a wireless problem. While wireless networks often receive the most attention, the actual user experience is shaped by the interaction between radio conditions, roaming, access layer design, switching behavior, QoS handling, and overall WAN & LAN architecture.
Using Wi-Fi 7 as a current reference point, the session shows why bandwidth alone is not a meaningful success metric and why latency, jitter, and responsiveness must be evaluated across the full network path. The goal is to provide network operators and engineers with a practical lens for understanding where user experience breaks down — and how to design networks that behave well under real operational conditions.

### QoE-riosities of 2026 - What we saw on the Internet this year
Speakers: Alexander Dethof
page: https://cfp.denog.de/denog18/talk/ZCXTKW/
While everyone talked about the DENIC outage this year, we monitored the critical stuff higher up the stack. The football world championship was a challenge for streamers and network operators. So, how did they actually perform under pressure? Beyond live events, we put different access technologies to the test in our lab to analyze how factors like latency, jitter, and bandwidth caps directly impact Quality of Experience (QoE) on the web and beyond. Let's have a data-driven look at the Unexpected of 2026.

### ICMP trickery in "reduced-IPv4" networks
Speakers: David 'equinox' Lamparter
page: https://cfp.denog.de/denog18/talk/ZQEANK/ | slides: https://cfp.denog.de/media/denog18/submissions/ZQEANK/resources/denog18_icmpexts_pres_DEricIf.pdf | slides: https://cfp.denog.de/media/denog18/submissions/ZQEANK/resources/denog18_icmpexts_uncut_vRwVcuo.pdf | slides: https://cfp.denog.de/media/denog18/submissions/ZQEANK/resources/denog18_icmpexts_pres_brNc3H4.odp | slides: https://cfp.denog.de/media/denog18/submissions/ZQEANK/resources/denog18_icmpexts_uncut_dc6vwLM.odp
Did you think IPv6 transition technologies were too easy? "one more" wasn't enough choices? Did you ever have to debug one of these "simple" setups? Come join for a walk through ICMP (v4 and v6) behavior and features!
This presentation will go through the various edge cases and overlaps between ICMPv4 and ICMPv6 in transition/IPv4 phase-out setups. One of these is likely applicable to most of us — hopefully you're not a poor soul for whom _all_ apply!

A rough outline:
- RFC 4884 and historic context: ICMP in MPLS networks
- convincing your tools to not hide the goods from you
- ICMP translation in NAT64 devices
- midpath ICMPv6 into NAT64
- 192.0.0.8 is love, 192.0.0.8 is life
- ICMPv4 on RFC 8950 devices
- Good thing nobody needs PMTUD, right?

### IPv6 routing loops -- A call to fix router configurations.
Speakers: Maynard Koch
page: https://cfp.denog.de/denog18/talk/PRRFUN/ | slides: https://cfp.denog.de/media/denog18/submissions/PRRFUN/resources/mkoch-denog18-ipv6-routing-l_iUlhuvs.pdf
Routing loops and the amplification of looping packets are known problems on the IPv6 Internet.
In a recent measurement study, we found that both problems are still present, potentially harming Internet stability.
Although routing loops are often easy to fix, they receive limited attention from the network operator community.
Since 2025, we aim to raise awareness of routing loops and amplification at network operator events.
In 2026, we started to weekly measure the deployment of routing loops and amplifications on the IPv6 Internet.
In this talk, we present how community outreach has helped significantly reduce the impact of these network misconfigurations. We further provide an update on the current state of these issues on the IPv6 Internet with a particular focus on the RIPE and DE region.
We hope these misconfigurations will eventually disappear and encourage the DENOG community to spread the word, check their networks, and help eliminate routing loops from the IPv6 Internet.
Until then, we will continue measuring, reporting, and raising awareness.
To assist in resolving these problems, we have made our findings publicly available at https://ipv6-sra.realmv6.org/routingloops, allowing operators to check whether their networks are affected by routing loops.

### Teach Networking!?
Speakers: Vanessa Gaube
page: https://cfp.denog.de/denog18/talk/E7UDUC/
There are many ways for career starters to get into IT: apprenticeships, university degrees, dual study programs, or through self-study.
But how do they learn networking and IT infrastructure?

With this lightning talk, I’d like to inspire you to teach young people how networking works!

What are the most difficult topics to explain? What about practical experience?
I've been teaching the basics of networking for several years now, and I'd like to share my experience with you.

### IPv4 as a service on an IPv6-only network
Speakers: Tobias Fiebig, Remco van Mook
page: https://cfp.denog.de/denog18/talk/V7Y3X9/ | slides: https://cfp.denog.de/media/denog18/submissions/V7Y3X9/resources/presentation_qhh5OYp.pdf
Routing IPv4 packets using IPv6 next-hops has been around for some time now. It offers great opportunities to reduce IPv4 address usage in the distribution and access layer, and enables providing IPv4 as a pure add-on, keeping a clean IPv6 address structure underneath.

Despite its benefits, major challenges for deploying IPv4-with-IPv6 next-hops in practice persist. While, e.g., BGP supports such routes using RFC8950, many other IGPs still lack support. Other major issues are 'the last mile', i.e., auto-configuring clients (or, for this use-case, more likely servers), and the impact of  IPv4-with-IPv6 next-hop usage on traceroutes.

In this talk, we will go over some current developments in these areas, which should make IPv4-with-IPv6 next-hops a viable option for practical deployments in the coming years. We will also expand further on possible deployment scenarios, where IPv4-with-IPv6 next-hops can remove further legacy Layer-2 infrastructure, e.g., LACP.

What actually changes in your network when you stop treating IPv4 as infrastructure and start treating it as a service?

draft-vanmook-intarea-ipv6-resolved-gateway (presented at IETF 126, WG adoption call pending) defines a single sentinel gateway address, provisionally 192.0.0.11 (requested from the IANA Special-Purpose Registry, not yet assigned), handed out as the ordinary DHCPv4 default gateway. Updated hosts resolve their first hop from the IPv6 neighbour cache; unmodified hosts ARP for the sentinel once and the router answers. That's the whole mechanism. Everything downstream of it is the interesting part.

This talk is about what that does to a running network: no IPv4 subnets anywhere, no ARP, no FHRP, IPv4 address pools that go flat — any /32 works anywhere in the footprint, nothing stranded by subnet sizing. The core forwards v4-via-v6 (RFC 8950) with no IPv4 configured on any router interface.

On the implementation side: host implementations for Linux (userspace daemon and native systemd-networkd), FreeBSD, macOS and Windows, with prebuilt packages; a namespace conformance lab with a zero-ARP assertion; verified unmodified-host behaviour across seven operating systems; and vendor configuration examples for IOS XR, JunOS, SR OS, EOS and RouterOS. On the router side, three working deployment models: a single-gateway reference, an active/active anycast VRRP pair, and a BGP-orchestrated multi-gateway fabric — fungible gateways, host /32s injected from inventory, and the entire DHCPv4 path carried as IPv4 values over IPv6 next-hops, with no IPv4 management network at all.

Plus the failure modes, the ND health prerequisites, and what breaks when you get it wrong.

No tunnels. No translation. No flag day. Keep the shape, change what it means.

## 2026-11-16 — Saal B

### Geoinformation Systems & Internet Infrastructure
Speakers: Dominik Bay
page: https://cfp.denog.de/denog18/talk/97DCW3/ | slides: https://cfp.denog.de/media/denog18/submissions/97DCW3/resources/slides_GkmWEA7.pdf
KML, KMZ, DXF - hat wahrscheinlich schon jede:r mal in der Hand gehabt, nach dem man redundante Leitungen bestellt hat. Aber was macht man eigentlich sinnvolles damit?

KML, KMZ, DXF - everyone knows or used those file formats, at least after asking the carrier where the redundant circuits are. But is there anything useful you can do with those files?
Geoinformationsdaten sind eine der Grundlagen für stabil funktionierende Infrastruktur. Egal ob Glasfasern im Boden, Glasfasern an Hochspannungsmasten oder Richtfunkstrecken. Wie funktioniert die Trassenplanung- und Instandhaltung, und welche Vorteile habe ich als Nutzer:in um meinen Netz zu verstehen und den Netzbetrieb zu optimieren?

Geo information data are the basis for reliable infrastructure. Not only for fiber in the ground, but even fiber on power lines or microwave links are planned this way. How does the planning of new fiber routes and their maintenance work, and which benefits do I get from geo data for my own network?

### IPv6 in firmware: Still booting in the wrong decade
Speakers: sinuscosinustan
page: https://cfp.denog.de/denog18/talk/XPH3W7/ | slides: https://cfp.denog.de/media/denog18/submissions/XPH3W7/resources/IPv6_in_firmware_onlineonly_2JBHNK4.pdf
Every server depends on firmware to boot and most also rely on firmware for remote management. U-Boot, EDK2 (UEFI), OpenBMC, you name it. And they all share the same issue: IPv6 support ranges from half-baked to non-existent. Why is this still the case in 2026?

In this talk I'll go into two areas of server firmware that operatores rarely look at closely: the one that boots the server, and the one that allows out-of-band management via the Baseboard Management Controller (BMC).

On the boot side: Do PXE and HTTP boot actually work over IPv6? And what unexpected side effects do you might see?

On the management side: How does IPv6 support look on a BMC today, and what's still broken?

Nobody's going to fix what nobody complains about. Let's find out how broken this is and what we can do about it.

### Ethernet Won Inside the AI Data Center. Can It Cross an Operator Boundary?
Speakers: Markus Hendrich
page: https://cfp.denog.de/denog18/talk/73Q8NL/
Inference is quietly overtaking training as the dominant AI workload, and unlike training — concentrated in a handful of hyperscale halls — inference wants to sit close to users, pulling AI capacity into distributed sites across Europe. 
The industry has spent the last two years re-engineering Ethernet (via the Ultra Ethernet Consortium and platforms like NVIDIA Spectrum-X) to match InfiniBand's performance for exactly this kind of workload, and now even ships Ethernet fabrics purpose-built to stitch multiple physical data centers into one logical AI factory. 
That's a solved problem when one company owns every site. This talk asks what happens when it isn't — when distributed inference has to span operators, jurisdictions, and ownership boundaries — and what a federated, policy-aware Ethernet fabric for that world would need to look like.
Ethernet is rapidly becoming the preferred back-end network for AI infrastructure. Technologies such as RoCE, Ultra Ethernet, NVIDIA Spectrum-X, and emerging “scale-across” architectures promise predictable, high-performance connectivity within and between AI data centers.

These architectures generally make one important assumption: a single organization controls the servers, switches, telemetry, congestion policies, and inter-site connectivity. Under that model, several physical data centers can be engineered to behave as one logical AI environment.

Distributed European AI infrastructure may not have that luxury. Inference capacity will increasingly be deployed across hyperscalers, regional clouds, colocation facilities, metro-edge sites, and specialist GPU providers. The networks connecting those sites may also belong to different fiber and connectivity operators. Each participant controls only part of the infrastructure, exposes limited operational information, and may operate under different commercial and jurisdictional requirements.

This creates a question that faster Ethernet alone cannot answer: what happens when an AI fabric reaches an operator boundary?

The talk begins by separating two ideas that are frequently conflated. Distributed AI services can steer requests between independent sites without extending a tightly coupled GPU fabric between them. Some workloads, however, including model distribution, distributed inference, resilience between GPU sites, and certain forms of model parallelism, place much stronger demands on inter-site connectivity. We will examine which workloads genuinely benefit from network-level federation and which should remain distributed at the application layer.

We will then look at what changes when traffic crosses a network-to-network interface. Can congestion-control assumptions survive between independently operated domains? What latency, loss, and bandwidth guarantees are technically credible? How can operators exchange useful telemetry without exposing internal topology? Who selects the end-to-end path, who responds to failures, and how can customers verify that the delivered service matches what was promised?

Sovereignty adds another dimension to this problem. A sovereign AI service is not defined solely by the location of its GPUs. Customers may also care about where their traffic travels, who owns and operates the infrastructure, which jurisdictions can exercise control over it, where encryption keys are held, and whether those claims can be independently verified. Consequently, path selection may need to consider geography, jurisdiction, operator identity, and operational control alongside conventional performance metrics.

The talk proposes a candidate architecture based on coordinated path computation with domain-local enforcement. Each operator retains control of its own network while exposing an abstract set of capabilities such as latency class, available bandwidth, path diversity, geographic scope, and jurisdictional attributes to a higher-level coordinator. The coordinator requests an outcome rather than configuring another operator’s network, while end-to-end measurement verifies whether the resulting service meets its performance and sovereignty objectives.

We will test this architecture against the timing and congestion requirements of GPU networking and identify where conventional carrier federation begins to fail. The goal is not to claim that a continent-wide lossless Ethernet fabric is immediately practical. It is to determine which multi-operator AI connectivity services are feasible, which workloads they can support, and which technical assumptions still require new standards or experimentation.

Attendees will leave with:
- A clear distinction between distributed inference services and distributed GPU fabrics.
- An understanding of what breaks when AI traffic crosses an operator boundary.
- A practical definition of sovereignty covering compute, connectivity, control, and verification.
- A candidate model for policy-aware, multi-operator AI connectivity.
- A framework for identifying which AI workloads can realistically operate across federated networks.

The commercial opportunity for operators may not be “one enormous Ethernet fabric.” It may instead be something more achievable: verifiable, policy-aware connectivity between AI-capable sites, with measurable performance, geographic, jurisdictional, and operational guarantees.

### Wire-API: fleet-wide, vendor-neutral network automation
Speakers: Enric Pujol, Sebastian Wagner
page: https://cfp.denog.de/denog18/talk/8YL9JB/ | slides: https://cfp.denog.de/media/denog18/submissions/8YL9JB/resources/DENOG18_b5nGHTC.pptx
Network operators share a vocabulary built on VRFs, EVPN-VXLAN, and BGP underlays. What doesn't travel is how it gets written down. Every vendor and orchestrator has its own dialect, and most automation tools still push device-specific config from an orchestrator down to all involved devices. Translation, not domain-specific problems, becomes a bottleneck.

We build _Wire-API_ with a different model in mind: Instead of targeting devices, operators declare the state they want and controllers work out which devices are affected and what config to push. In the case of an EVPN fabric for example: describe it with objects like `Network`, `RoutingDomain`, and `ExternalConnection`, and adding a network becomes one object rather than a coordinated change across every leaf and firewall that participates. The shift is in what gets declared: desired state instead of a device's running config. From there, drift correction and HA-aware maintenance stop being separate runbooks and become properties of the reconcile loop, and the same model extends to anything else on the network expressed as intent.

The core is Kubernetes. _Wire-API_ is a set of CRDs and controllers that reuse the contract that made Kubernetes work in "compute"—declared state, continuous reconciliation, honest status—and apply it to the network domain.

The presentation argues for the _Wire-API_ model and walks through a live EVPN-VXLAN example—one intent object, vendor-specific config on Cisco NX-OS and Nokia SR Linux—then covers design decisions and partial-failure handling. Wire-API already operates production fabrics across multiple availability zones; the model works today even as the framework continues to grow.

_Wire-API_ is Apache-2.0 and is being contributed to the NeoNephos Foundation (Linux Foundation Europe) as part of the ApeiroRA workstream under the EU IPCEI-CIS program.
Here is the link to the GitHub resources:
https://github.com/ironcore-dev/network-operator
And the detailed description on the website:
https://ironcore.dev/network-operator/

### Modular Nokia SR OS automation from scratch
Speakers: Jennifer Graul
page: https://cfp.denog.de/denog18/talk/KPYWEU/ | slides: https://cfp.denog.de/media/denog18/submissions/KPYWEU/resources/denog18-talk_H5nOvAY.pdf
Existing automation solutions are usually monolithic and require you to migrate all of your existing infrastructure at once to the automation. I wanted to introduce automation step by step and wanted to continue to use our existing sources of truth. So I have built a modular automation solution that allows us to build a completely separated automation module for everything we want to automate in our network.
Existing automation solutions are usually monolithic and require you to migrate all of your existing infrastructure at once to the automation. But I wanted to continue using our existing sources of truth and wanted to introduce automation in our network step by step and not in one big step.

Additionally, there is the security perspective: do you really want to grant an automation solution that you don't fully understand internally unrestricted access to all of your routers?

The solution: modular network automation from scratch: write a module for any aspect you want to automate in your network. Want to automate your peerings with Peering-Manager? Write a module for it. Want to automate your base router interfaces with NetBox? Write a module for it.

The modules itself are isolated from each other in the configuration by using one config group for each module (basically a separate config tree for each module). This by design eliminates the possibility of collisions between modules and makes consecutive deployments easier by fully replacing the config group on each run. It additionally allows you to minimize the permissions of an automation user to the absolute required minimum by only granting them access to the config group. Furthermore, the use of config groups allows you to override the automation on any given time in the main config tree or even exclude some parts of the main config tree from it.

Although this solution was developed for Nokia SR OS, it can in principle be extended to any platform that is transactional and supports something like config groups.

### You can't make everybody equally happy - Measuring Anycast with AI as the Third Member of a Two-Person Team
Speakers: Jan Zorz
page: https://cfp.denog.de/denog18/talk/MRZYPH/ | slides: https://cfp.denog.de/media/denog18/submissions/MRZYPH/resources/Jan_Zorz_Anycast_DENOG_Pres_8OX4Zt2.pptx
Anycast is easy to explain and notoriously difficult to observe. Announce the same IP address from multiple locations, allow BGP to choose a path, and traffic should reach the "nearest" instance, although BGP's idea of nearest often has little to do with geography.

ProVision (formerly 6connect) operates an anycast DNS platform spanning six prefixes, 39 BGP nodes, 13 regions, and five continents. For years, we knew the platform worked because queries were answered. What we could not prove was how it worked: which users reached which nodes, how quickly packets arrived, and where traffic quietly disappeared.

This presentation tells the story of how we turned one of anycast's most frustrating behaviors-ICMP replies returning to the "wrong" node-into a measurement. That insight grew into an automated pipeline running 117,000 probes per second across 2.6 million targets, measuring latency, loss, jitter, routing behavior, path MTU failures, ECMP paths, and visibility at 845 Internet Exchanges.

It is also the story of how two network engineers who are not full-time developers built the system through intensive collaboration with AI coding models. AI supplied much of the implementation capacity; the humans supplied decades of network intuition, architectural direction, validation, and the authority to say when the code was confidently wrong.
Anycast underpins critical Internet services, including DNS, content delivery networks, and DDoS mitigation platforms. The model appears simple: announce the same IP address from multiple locations and allow BGP to direct traffic toward the best available path, but the operational reality is far less transparent.

ProVision (formerly 6connect operates an anycast DNS platform built around six prefixes announced by 39 BGP nodes in 13 regions across five continents. The platform answered queries reliably, yet ordinary service monitoring could reveal only part of the story. It could tell us that a DNS request succeeded, but not always which node handled it, whether BGP selected the node we expected, how latency differed across the catchment, or where packets were being lost without causing a visible outage.

Measuring the network from inside the platform created a chicken-and-egg problem. Anycast is designed to make many distributed instances appear to be one destination, so the topology we wanted to study was the same topology the service was designed to conceal. We could not simply ask the Internet which node it would reach. We needed a way to make the network reveal its own routing decisions.

The breakthrough came from a behavior that initially appeared to undermine the measurements. We sent probes from the production anycast source addresses and observed that ICMP errors frequently returned to the "wrong" node rather than the node that originated the probe. That wrong node was the answer.

The node receiving the ICMP response was the node BGP had selected as the return path for the router generating it. By recording those responses across the network, we could begin mapping real anycast catchments from the perspective of the infrastructure itself. The apparent flaw became the core measurement primitive. From that insight, we built a fully automated daily measurement pipeline capable of:

Running 117,000 probes per second across 2.6 million targets Measuring round-trip time, packet loss, and jitter for 1.4 million addresses Detecting path MTU discovery black holes Performing ECMP-aware traceroutes Correlating active measurements with BGP monitoring Measuring platform visibility at 845 Internet Exchanges

Attendees will leave with a practical understanding of why anycast is so difficult to measure, how asymmetric ICMP routing can reveal real BGP catchments, and what it takes to turn that observation into a large-scale monitoring system. They will also see a grounded example of AI-assisted engineering in which coding models expanded the capacity of a very small team without replacing the network judgment required to build something trustworthy.

### How Deutsche Telekom Built a Carrier-Grade Virtual PoP on AWS: A PoC Review
Speakers: Gabor Adam, Holger Thösink, Adam Orosz
page: https://cfp.denog.de/denog18/talk/SUN8ER/
Physical points of presence (PoPs) are expensive to deploy and often limit how quickly service providers can respond to customer demand in new regions. To address this challenge, Deutsche Telekom developed a virtual PoP architecture that extends carrier-grade MPLS L3VPN services into AWS.

This talk presents the technical architecture behind the solution, including AWS Direct Connect Gateway, Cisco 8000v virtual routers, MP-BGP, and VPNv4/VPNv6 integration. We explain the design decisions, operational considerations, and routing principles that enabled the realization of a cloud-based PoP.

Attendees will learn how cloud infrastructure can be integrated into a traditional service provider network while maintaining routing control, operational standards, and rapid service deployment.
Customer demand increasingly requires network services in regions where no physical Point of Presence exists. Building new PoPs is costly and time-consuming, making it difficult to respond to short-term requests.

In this session, we present how Deutsche Telekom designed a vPoP architecture running in AWS that extends the MPLS backbone into cloud regions while preserving carrier-grade routing and operational principles.

We will discuss the architecture, including AWS Direct Connect Gateway, Cisco 8000v virtual routers, MP-BGP (VPNv4/VPNv6), IPv4/IPv6 routing, management separation, and throughput considerations. Particular attention will be given to the design choices that enabled regional routing while avoiding AWS transit and maintaining full control over the routing domain.

The talk also covers the practical experience gained during the project, including proof of concept implementation, operational challenges, automation aspects, and lessons learned from integrating cloud infrastructure into a service provider environment.

The session is aimed at network operators, architects, and engineers interested in MPLS, BGP, cloud networking, and carrier-grade network design. Attendees will gain practical insights into extending traditional backbone services into hyperscaler environments.

## 2026-11-16 — WG Room 901

### Welcome Group WG - public meeting
Speakers: Vanessa Gaube
page: https://cfp.denog.de/denog18/talk/XPYRCH/
Public Meeting of the Welcome Group WG
Public Meeting of the Welcome Group WG

### OT/IoT Networking Meetup
Speakers: Jadyn Jäger, Lara Hallaczek
page: https://cfp.denog.de/denog18/talk/9EX3PF/
At recent DENOG Meetups a small group of people working in OT-Networking, -Ops and -security found each other and started talking. We want to continue the exchange of ideas, experiences, advise and discussions of OT specific topics at DENOG18. Let's get to know each other and build a community around this ever growing topic.
The [OT](https://en.wikipedia.org/wiki/Operational_technology) and IT worlds are growing closer and the line between these fields is getting more blured. What are the differences? Which issues do we face when IT people encounter electricians and their systems. Devices in our networks that were last patched 15 years ago? How do we deal with systems offering  a 10 Mbit/s "Ethernet" interface at most?

We want to build a community to discuss such topics.
- How do we build networks, where the hardware is old and *very* insecure?
- How do we deal with an environment where the bandwidth is low and the casualties may be high?
- How can we improve the security of our OT networks without impacting their reliability?

We'd love to hear your (horror) stories, thoughts, ideas and problems.
We hope that this meeting will be the start of a mailing list or a working group at DENOG.

### Routing WG
Speakers: Vincentz Petzholtz, Andreas Kimpfler
page: https://cfp.denog.de/denog18/talk/VFDAFV/
Meeting of the Routing WG
Meeting of the Routing WG

## 2026-11-17 — Saal A

### Optical Foundations for IP Engineers: From Fiber Basics to DWDM and Link Budgeting
Speakers: Thomas Weible
page: https://cfp.denog.de/denog18/talk/J3QAZC/ | slides: https://cfp.denog.de/media/denog18/submissions/J3QAZC/resources/FLEXOPTIX_-_Optical_Foundati_GnSQqg8.pdf
IP engineers still view transceivers as plug & forget - something that just converts electrical to optical signal and vice versa. This talk provides a concise introduction to essential optical fundamentals for IP networking newcomers and professionals, covering topics such as single-mode and multi-mode fiber and their structural and operational differences, common connector types and their usage, and a detailed look at optical losses. In particular, it explains how attenuation accumulates across fibers, connectors, and splices, and how to perform optical link calculations and budgeting to ensure sufficient transmission margins. The talk also introduces wavelength-division multiplexing technologies—CWDM and DWDM—explaining their characteristics, channel spacing, use cases, and relevance in modern packet-optical networks. Made by FLEXOPTIX Technical Customer Support - Andreas and Thomas

### Enjoying BMP with Rotonda in 600 seconds
Speakers: Luuk Hendriks
page: https://cfp.denog.de/denog18/talk/E7HWCA/ | slides: https://cfp.denog.de/media/denog18/submissions/E7HWCA/resources/enjoying_bmp_luuk_hendriks_r0spprB.pdf
With BMP (BGP Monitoring Protocol) readily available on all major routing
platforms, operators have the opportunity to get a view of their networks
that's more comprehensive than ever before.
Crucially, one needs to collect all this information and make sense of
it, ideally without having to invest too much time. In this lightning talk, we
present Rotonda, enabling operators to do just that: get started with BMP
effortlessly, while providing the scalability and flexibility to monitor any
network, any use case.

Rotonda is free and open source route collection and analysis software
developed by NLnet Labs. We'll introduce BMP, highlight and showcase the main
features of Rotonda, and hopefully spark interest to continue the conversation
afterwards.

### IPv6-Mostly - A Pretty Little Update
Speakers: Robin Därmann
page: https://cfp.denog.de/denog18/talk/L9LFQC/ | slides: https://cfp.denog.de/media/denog18/submissions/L9LFQC/resources/IPv6-Mostly_DENOG18_v2_JAP7AK0.pdf
IPv6-Mostly is an interesting approach to save IPv4 addresses. I will give a short update of my talk about it DENOG15, especially about the support of operating systems.

### Ein Jahr DENOG WG Access: Was wir erreicht haben und wo es hingeht
Speakers: Christian Giese, Andreas Kimpfler
page: https://cfp.denog.de/denog18/talk/XMLPRE/ | slides: https://cfp.denog.de/media/denog18/submissions/XMLPRE/resources/DENOG18_WG-Access_Ein-Jahr_CJI1WwN.pdf
Seit unserer Gründung auf der DENOG17 ist ein Jahr vergangen – ein Jahr voller spannender Themen! 

In dieser Session blicken wir auf die bisherigen Erfolge und Meilensteine der Working Group Access zurück. Gleichzeitig richten wir den Blick nach vorn: Welche Herausforderungen und Projekte stehen im neuen Jahr auf unserer Agenda? Ein kompaktes Update für alle, die auf dem Laufenden bleiben oder die Arbeit der WG zukünftig mitgestalten wollen.

### Route Filtering at Scale
Speakers: Fedor Vompe, Sebastian Becker
page: https://cfp.denog.de/denog18/talk/KXMLXN/ | slides: https://cfp.denog.de/media/denog18/submissions/KXMLXN/resources/DENOG18_Route_Filtering_at_S_Rw7sgKx.pdf
BGP routing security relies on many technologies, both old and new, such as IRR-based Route Filters and RPKI Technologies like Route Origin Authorizations (ROAs) or Autonomous System Provider Authorization (ASPA-s). While these technologies are well-known, they are still used together, and accurate route filter generation remains a challenging task with significant operational implications for large-scale router filter generation at major tier-1 ISPs.

We show that AS-Set documentation in RIR databases is still critical yet systematically overlooked. We evaluate the scope and patterns of these issues - including missing documentation, AS-Set explosive expansion, and cyclic dependencies - demonstrating that accurate AS-Set documentation remains a foundational requirement for operational filtering.

We present the toolchain and technologies like Route Query Specification (RQSpec) we use for route filter generation at scale, compensating for the complexity introduced by poor documentation.

### AI’s impact on bandwidth and automation in optical networks
Speakers: Kent Lidstrom
page: https://cfp.denog.de/denog18/talk/DRTW8K/
Overview of AI's impact on the optical industry and why scale across will driving an insane bandwidth increase in optical networks.  
The presentation will also cover how we expect that AI agents will impact how service providers manage & automate their networks in a near future.

### FSO essentials
Speakers: Takaya Nakagawa
page: https://cfp.denog.de/denog18/talk/BSEFX3/ | slides: https://cfp.denog.de/media/denog18/submissions/BSEFX3/resources/DENOG181106_Kfu5GsI.pdf | slides: https://cfp.denog.de/media/denog18/submissions/BSEFX3/resources/DENOG181113_ESS8kNF.pptx
Free-Space Optical (FSO) communication is a wireless technology that uses laser beams to provide high-speed data transmission between two locations with a clear line of sight.
 This presentation introduces the evolution of FSO from large-scale experimental systems in the 1970s to modern commercial and mission-critical applications such as satellite, military, and drone communications.
 Advances in optical components, sensors, control technologies, and software have significantly improved system performance, reliability, and usability.
 Current FSO systems are compact, lightweight, support automatic tracking, and typically achieve data rates of 25 Gbps.
Contents
- What is FSO
- History of FSO 
- Current FSO Technology
- Progress in Enabling Technologies
- Key Features of Today's FSO System
- Things to Keep in Mind When Using Lasers

### IXP Update
Speakers: Tim Kleefass
page: https://cfp.denog.de/denog18/talk/LEHAXX/ | slides: https://cfp.denog.de/media/denog18/submissions/LEHAXX/resources/IXP_Update_DENOG_18_-_2026__C7fk0dL.pptx
News from IXPs in Germany
As introduced 2021 we collect some parameters from all IXPs, which are active in Germany.
This talk aggregates the Updates for all the IXPs in a common format and will be presented in a neutral way.

### Do not look into beam with remaining eye
Speakers: Nicola 'nicoduck' von Thadden
page: https://cfp.denog.de/denog18/talk/EVWTHX/
Laser safety is important for everyone, yet knowledge widely differs on what's applicable and and required to do before conducting work on live fibers. This talk will give a brief introduction into laser classes in networking equipment and safety equipment.

### The New Botnet Era: Rethinking Your DDoS Strategy
Speakers: Stefan Meinders
page: https://cfp.denog.de/denog18/talk/XBCBZT/ | slides: https://cfp.denog.de/media/denog18/submissions/XBCBZT/resources/DENOG18_Botnet_StM_20261112_qpjr2jb.pdf
DDoS defense strategies must evolve because modern botnet campaigns combine high-volume, direct-path pressure with stealthier tailored attack components that attempt to overload and evade mitigation systems. 

In the past, most DDoS attacks were easier for ISPs to identify and block. The hardest cases were botnet-based Layer 7 attacks because they were more difficult to detect and mitigate. 

Successfully blocking DDoS attacks today requires more than the techniques that worked in the past. Over the past months, botnet size and firepower have increased dramatically. These botnets now drive some of the largest and most effective attacks, not only against individual applications but also against entire network infrastructures, cloud providers, and CDNs. 

At the end of 2025, we observed record-breaking attacks. This talk explains why we believe those attacks happened, why they continue, and what they reveal about the evolution of botnet-driven DDoS campaigns. 

Multi-terabit attacks have become much more common, but it is not just the volume of DDoS traffic that is taking down web sites and other targets around the world. The real problem is the tailored, targeted, and dynamic attack components that knock servers offline while remaining below the visibility threshold of many traditional defenses.  
Today’s large-scale, direct-path attacks increasingly include multiple attack vectors, blending volumetric, state-exhaustion and application-layer components. These botnet-based attacks are designed to overload mitigation capabilities and resources.  
  
This talk explains what enabled the expansion of botnets behind today’s attack campaigns and where these new bots are located. For network operators, this matters because these bots now require inbound, outbound, and cross-bound DDoS detection and mitigation.  
These insights are based on ATLAS, our worldwide DDoS monitoring system.  
Attendees will leave with a clearer understanding of why botnet-driven DDoS campaigns now demand mitigation strategies that account for visible volumetric pressure and lower-profile attack components at the same time.

### Network Automation for the Modern Age
Speakers: Veit Heller
page: https://cfp.denog.de/denog18/talk/U3Q97T/ | slides: https://cfp.denog.de/media/denog18/submissions/U3Q97T/resources/talk_uJq4ewQ.pdf
In the last two decades network automation has gone from a fringe concept reserved for global players to the industry standard at almost every system size. The tooling and concepts have evolved and grown, and an ecosystem has formed and normalized around a few core systems.

In this talk, we want to propose a natural next step in the evolution from manual work over templating to driving the system with sources of truth. As the technological and business complexity of networks grows, the data model becomes more and more of a focal point of how we look at the reality of our system. We need to understand our data and our models better than ever before, and make our decisions based on how we model the world, without being constrained by the limits of our pre-fabricated documentation systems.

We will speak about what it means for an automation to be driven by your actual data model and how you conceptualize the network, motivated by an actual software system. Over the course of the talk, we will not just talk about concepts, but anchor our ideas in concrete implementation.

Nonetheless, this is not a talk about a solution. It’s a talk about an idea and an approach, and, hopefully, the start of a conversation.
The talk builds on our previous work and talks around network automation and data modeling. We want to make the case that “source of truth” is a useful step, but not the end state: the more interesting question is whether the model itself can become the driver of automation.

The talk will use alembic (https://github.com/cyberwitchery/alembic) as the concrete anchor. We plan to show how a model-first system can represent network concepts, derive operational artifacts, and fit alongside existing DCIM/IPAM/source-of-truth tools without being constrained by their object model.

Expected structure:
- short history: from manual work to templates to source-of-truth automation
- why we end up with our own data model most of the time and what that means
- concrete examples from alembic
- trade-offs, open questions, and caveats

The talk is intended for network engineers, automation engineers, and people maintaining source-of-truth or orchestration systems.

## 2026-11-17 — Saal B

### Maybe it is time to consider layer 3 internet exchanges
Speakers: James Rice
page: https://cfp.denog.de/denog18/talk/EMHXW7/ | slides: https://cfp.denog.de/media/denog18/submissions/EMHXW7/resources/DENOG18-Rice-layer3-internet_CYbdNDJ.pdf
Internet exchanges have presented as shared layer 2 networks for thirty years. I will show the mechanisms that silently blackhole exchange traffic or forward it to the wrong port: missing or incorrect neighbour entries, and unknown unicast flooding. In each case BGP stays established to the route servers and nothing reports a fault.

A large exchange stated in writing that it gives no guarantee traffic sent to a peering LAN goes to, and only to, the port of the network it was meant for, and that it knows of no exchange that does. I do not know how many members expect that answer.

The rest of the industry has spent years dismantling large layer 2 domains in favour of routed ones. Perhaps it is time for internet exchanges to forward at layer 3, rather than running a layer 2 forwarding domain with a route server making routing decisions.

In many cases this needs no new hardware. The switches already used to build exchange fabrics forward at layer 2 and at layer 3 at line rate. Route scale is where careful consideration is needed.

The shape of a layer 3 internet exchange switch is already commonplace: each PNI switch a CDN or ISP operates is a routed exchange with several settlement-free peers and one customer on it.

Running at layer 3 gives participants complete isolation between ports, the same model that already applies to every other upstream connection that networks buy. RTBH works at the exchange rather than depending on a peer to honour it. Debugging becomes possible from the participant side, because traceroute shows the exchange hop.

### You Want EGP? You Get EGP! - DENOG Mad Scientist Edition
Speakers: Tobias Heister
page: https://cfp.denog.de/denog18/talk/YUWRSZ/ | slides: https://cfp.denog.de/media/denog18/submissions/YUWRSZ/resources/You_Want_EGP_-_You_get_EGP_exjDxDl.pdf
We are all well aware of BGP as our protocol to run the Internet. As we sometimes notice (e.g. in the Talk by Wolfgang Tremmel at DENOG17) BGP still has ties to its predecessor EGP and can still claim it learned things from that protocol (Sometimes for nefarious reasons).

Follow me on a journey to find out what we need to do in order to still run the EGP Protocol in 2026. How far back in time do we need to go in order to legitimately put the E into the Origin of BGP updates?

Why? Because We do what we must because we can!

### Quo Vadis IPv6 in Germany?
Speakers: Wilhelm  Boeddinghaus
page: https://cfp.denog.de/denog18/talk/G37JXN/ | slides: https://cfp.denog.de/media/denog18/submissions/G37JXN/resources/Quo-Vadis-IPv6-Boeddinghaus-_uFwPidr.pdf
IPv6 deployment is well underway in Germany—some of it visible, much of it happening behind the scenes. So, what’s actually going on? How much progress has the public sector made? Where does our economy stand? And what does having IPv6 at home really means for users?

This talk provides an overview of IPv6 deployment across Germany. Here’s a little preview: we’re doing better than you might think.

### Post Quantum Secure Networking
Speakers: Lara Hallaczek
page: https://cfp.denog.de/denog18/talk/HJXTTT/ | slides: https://cfp.denog.de/media/denog18/submissions/HJXTTT/resources/pqc-networking_7dt13sD.pdf
Securing our Infrastructure against Cryptoanalysis with Quantum Computers

This talk gives an overview of the topic of post quantum cryptography. It explains the problem these algorithms try to solve, shows underlying mechanisms and takes a look at developments of the past few years. The presentation is intended as a summary of the of the topic from a network engineer's point of view: what's going to be on our schedules in the not too distant future? Which solutions are already available, which topics are still under discussion, and what will be required from our infrastructure by industry standards and  regulatory bodies?

### I Accidentally Built the Internet (as a Cartoon)
Speakers: Frederic Jung
page: https://cfp.denog.de/denog18/talk/QR89BD/ | slides: https://cfp.denog.de/media/denog18/submissions/QR89BD/resources/Series-of-Tubes-lightning-t_wCg06W1.pptx
On a Thursday afternoon I had a dumb idea: a browser game where you build the internet. The next morning it was live. 25 days later it has 1,257 commits, 80 releases, satellites called pies, federated multiplayer and more than 30 contributors. This is how that happened, and what made it possible.
Series of Tubes is a free cartoon browser game about how the internet really works. You start with one router in one city and grow into a Tier 1 network, while a chaos monkey snips your tubes to see what breaks. This lightning talk tells the story of its first three weeks: the first prompt, strangers sending pull requests on day two, three major versions on three Fridays, and the tests, release automation and AI pairing that kept it shippable. Play it at seriesoftub.es.

### A Prosecutor in Another Country Wants Your Data in 8 Hours — Now What?
Speakers: Mathias Handsche
page: https://cfp.denog.de/denog18/talk/J9DJVF/
Since 18 August 2026, a prosecutor in another EU country can demand your users' data directly from you — ten days to comply, eight hours if they're in a hurry. No mutual legal assistance, no local court in between: just an order in your inbox and a clock. This talk is the E-Evidence Regulation for the people who actually run the infrastructure: which data you can be forced to produce, how fast, and whether the systems you already operate could even answer in time. A few months in, we'll look at what's working, what's on fire, and what you should have built before the first order arrives.
Most coverage of the EU E-Evidence Regulation is written for lawyers. This one isn't. If you operate an ISP, a hosting platform, a cloud, or a registrar, you are the *addressee* of these orders — and the obligations are technical and time-boxed long before they're legal.

We'll start with the 90-second operator edition: European Production Orders (EPOC) and European Preservation Orders (EPOC-PR), who can issue them, which data categories are in play (subscriber, traffic, content), and the deadlines that turn this into an on-call problem rather than a policy memo. Then we get to the parts nobody warns you about: that you must designate an establishment or legal representative, that liability is joint and several with fines reaching into a percentage of global turnover, and that there's an actual machine interface behind all this — a decentralised IT system, a transport spec, a hard size limit, and a rollout that may not be finished when the orders start arriving.

The practical core is simpler than the crypto-heavy forensics literature suggests. Evidence just needs to be trustworthy: the right data, demonstrably unchanged, anchored in time, and traceable back to where it came from. You don't need a forensics lab for that — you need to know whether the logs and exports you already produce would survive someone asking "how do you know this is genuine?" We'll cover the idea at a level you can act on, then look at how it usually falls apart in practice: data that's already been rotated away, mutable logs, a screenshot instead of a record, no idea who pulled what or when.

We close with a field report from the first months of the regime — readiness across the EU, what early orders actually look like, and a pragmatic checklist so that when (not if) one lands in your inbox, you can produce the right data, in a defensible form, within the deadline — without it turning into a fire drill every time.

This session is for ISP, hosting, cloud, and registrar engineers, DevOps, abuse/LI-interface teams, and anyone who owns logging or will be the one woken up at 2 a.m. by an 8-hour emergency order. No legal background required; bring your healthy disrespect for bureaucracy.

### Carrier-Scale TWAMP Monitoring with DPDK and Commodity x86 Servers
Speakers: Mario Jurcevic
page: https://cfp.denog.de/denog18/talk/39VKX7/ | slides: https://cfp.denog.de/media/denog18/submissions/39VKX7/resources/Carrier_Scale_TWAMP_DPDK_5x9_iKYlx1v.pdf
Modern telco operators increasingly require continuous active performance monitoring across thousands or even tens of thousands of access nodes. While TWAMP has become the de facto standard for active IP performance measurements, implementing it at carrier scale is far from trivial.

This presentation explains how a carrier-scale TWAMP monitoring platform can be built using commodity x86 servers together with DPDK-based userspace packet processing that completely bypasses the Linux networking stack.

The talk discusses the architectural decisions required to support massive numbers of concurrent TWAMP sessions, including packet processing, session scheduling, timer management, CPU affinity, NUMA awareness and resource optimization.

Real benchmark results and operational experience from large-scale deployments demonstrate the achievable scalability and identify the practical limitations of this approach.

Attendees will gain practical insight into designing highly scalable active monitoring systems without relying on proprietary hardware appliances.
**Why carrier-scale TWAMP is difficult**

Most existing TWAMP implementations are designed for relatively small deployments. Scaling active measurements to tens of thousands of simultaneously monitored access nodes introduces significant challenges in packet processing, timing accuracy, scheduling and resource management.

**Why DPDK**
The presentation explains why bypassing the Linux kernel networking stack is essential for achieving deterministic latency and high packet processing rates. It discusses how DPDK enables direct NIC access, reduces interrupt overhead and provides predictable packet forwarding performance.

**System architecture**
Topics include:
- Userspace packet processing architecture 
- DPDK forwarding engine and application-to-engine communication 
- TWAMP session management 
- Timestamping offload and packet pacing 
- Multi-core scalability on commodity x86 hardware


**Performance**
Real benchmark results will be presented, including:
- maximum number of concurrent TWAMP sessions
- packets per second
- CPU utilisation
- memory consumption
- scaling across multiple CPU cores
- practical deployment limits

**Operational lessons learned**
The presentation concludes with practical experience gained from deploying large-scale active monitoring systems in carrier environments, including common pitfalls, optimisation techniques and recommendations for future deployments.

### The Leak-Proof Routing Table: Mastering BGP Roles, ROAs, and ASPA
Speakers: Anton Elita
page: https://cfp.denog.de/denog18/talk/3FWLT7/
The global routing system was built on a foundation of trust — often exploited by route leaks and hijacks. This session breaks down how a trio of complementary security mechanisms shifts the internet from a model of blind faith to strict verification. We will examine how BGP Roles and the Only-To-Customer (OTC) attribute proactively block leaks multiple hops from the source. Next, we will cover how RPKI Route Origin Authorizations (ROAs) secure the origin point, and how Autonomous System Provider Authorization (ASPA) ensures the entire AS_PATH remains valley-free. Attendees will leave understanding exactly how these tools turn the hope that "BGP speakers behaved" into proof that they did.

### SRv6 in the Data Center: Crazy Ideas or Real Use Cases?
Speakers: Andreas Roeder
page: https://cfp.denog.de/denog18/talk/E8TQM8/ | slides: https://cfp.denog.de/media/denog18/submissions/E8TQM8/resources/DENOG-SRv6-v04-dark-short_irmZx8N.pptx
SRv6 divides opinion — somewhere between visionary promises and the suspicion that it's yet another overly complex protocol the world doesn't need. This talk cuts through both extremes and uses concrete scenarios to show where SRv6 actually delivers today.

We start with a compact overview of SRv6 fundamentals: segment types, uSID encoding, and what structurally sets SRv6 apart from MPLS and VXLAN — and when those differences actually matter. Building on that, we examine three practical use cases: routing in the DC fabric (Clos/spine-leaf with BGP underlay), seamless data center interconnect without MPLS overlay complexity, and SRv6 as the transport plane for AI/GPU cluster fabrics with demanding requirements around load spreading and low latency.

The throughline: what is production-ready today, what remains theoretical — and where is the added complexity actually worth it?
The Goal of this talk is to give a Technology Introduction into SRv6 and how this will be applicable for DataCenter Usecases and compares towards existing Technologies like EVPN/VXLAN. The Goal is to educate the audience about this technology and provide examples of usecases.

## 2026-11-17 — WG Room 901

### WG Meetup
Speakers: Carsten Schiefner, Michael Gross
page: https://cfp.denog.de/denog18/talk/EZAW3S/
WG Meetup
WG Meetup

### Access WG
Speakers: Andreas Kimpfler, Christian Giese
page: https://cfp.denog.de/denog18/talk/ZLEHXD/
Access WG
Access WG

