>>> HOW TO RUN THIS <<<
This is the digest prompt for itnog-10. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/itnog-10.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/itnog-10.md
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

Below is the program for ITNOG10. Read it and produce a digest
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
conference: ITNOG10
source_url: https://www.itnog.it/itnog10
generated: 2026-11-04
registry_key: itnog-10
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / Identity PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## ITNOG program
### HaliveOS: da operatore a innovatore
Speakers: WIC powered by Hal
No abstract published; title, speakers and materials only.

### OTN oltre il trasporto: reti programmabili, latenze garantite e architetture quantum-safe
Speakers: OPNET
No abstract published; title, speakers and materials only.

### Migrazione del nostro Backbone a SR-MPLS perdendo pochi ping...
Speakers: Denis Corradini
slides: https://www.itnog.it/itnog10/files/1-2_Il nostro Backbone - ITNOG10.pdf
No abstract published; title, speakers and materials only.

### National Layer-2 wholesale FWA leveraging VxLAN
Speakers: Christian Biasibetti
slides: https://www.itnog.it/itnog10/files/1-3_202604-cbiasibetti-L2FWA-ITNOG10-Public.pdf
No abstract published; title, speakers and materials only.

### Integration of Security Functions in EVPN/VXLAN Using Group-Based Policy
Speakers: Nicola Modena
slides: https://www.itnog.it/itnog10/files/1-4_202604-nmodena-EVPN-VXLAN-Group-Based-Policy-ITNOG10.pdf
No abstract published; title, speakers and materials only.

### Coffee break
No abstract published; title, speakers and materials only.

### Transforming BGP operations to serve the best prefix out of 26 million
Speakers: Alessandro D'Eliseo Antonio Prado
slides: https://www.itnog.it/itnog10/files/1-5_Transforming BGP Operations.pdf
No abstract published; title, speakers and materials only.

### Diffusione Edge Computing nelle reti Telco: local break traffico
Speakers: Fabio Randone
slides: https://www.itnog.it/itnog10/files/1-6_Edge Computing in Telco Networks Fabio Randone_final.pdf
No abstract published; title, speakers and materials only.

### Reimagining Networking in the Age of AI: Empowering Engineers to Shape the Future
Speakers: Giampaolo Panariello
slides: https://www.itnog.it/itnog10/files/1-7_Reimagining Networking in the Age of AI Empowering Engineers to Shape the Future v5 - Giampaolo Panariello.pdf
No abstract published; title, speakers and materials only.

### MIX DC3
Speakers: Mauro Magrassi
slides: https://www.itnog.it/itnog10/files/1-8_MIX-ITNOG10-DC3.pdf
No abstract published; title, speakers and materials only.

### Inside Seabone: experiences of a Tier-1 Backbone
Speakers: Gabriele Laghi Patrizia Rossi Antonio Ferretti
slides: https://www.itnog.it/itnog10/files/1-9_ITNOG_ Inside Seabone - Experiences of a Tier-1 Backbone.pdf
No abstract published; title, speakers and materials only.

### IXP Updates
Speakers: Various
slides: https://www.itnog.it/itnog10/files/1-9_ixp_updates.pdf
No abstract published; title, speakers and materials only.

### Hollow Core Fibre - Nothing is better than glass for guiding light
Speakers: Steve Jones
slides: https://www.itnog.it/itnog10/files/1-11_ITNOG_hollowcorefiber.pdf
No abstract published; title, speakers and materials only.

### Building the longest SR-TE lsp in the world
Speakers: Umberto M
slides: https://www.itnog.it/itnog10/files/1-12_longesttunnel-itnog_26_um_2.pdf
No abstract published; title, speakers and materials only.

### SRv6 uSID: Deterministic AI Backend Networking and Unified DC Frontend Design
Speakers: Alberto Donzelli
slides: https://www.itnog.it/itnog10/files/1-13_2026_ITNOG_adonzell_Cisco-final.pdf
No abstract published; title, speakers and materials only.

### News and How to be involved in PeeringDB
Speakers: Livio Morina
slides: https://www.itnog.it/itnog10/files/1-14_20260421_ITNOG10_Morina_Livio.pdf
No abstract published; title, speakers and materials only.

### Improve IPv6 Peering
Speakers: Federico Paesani
slides: https://www.itnog.it/itnog10/files/1-15_Presentazione improveipv6peeringITNOG10 Paesani v2.0.pdf
No abstract published; title, speakers and materials only.

### Coffee Break
No abstract published; title, speakers and materials only.

### HERABIT - Interprovider VPN
Speakers: Fabio Moglia
slides: https://www.itnog.it/itnog10/files/1-16_HERABIT_InterproviderVPN_INOG10.pptx.pdf
No abstract published; title, speakers and materials only.

### BGP nell'underlay multi-cloud: resilienza e simmetria tra on-prem e public cloud
Speakers: Carlo Pio Luigi Ciciriello
slides: https://www.itnog.it/itnog10/files/1-17_ITNOG10-BGPunderlayMultiCloud-CPLC-20260421.pdf
No abstract published; title, speakers and materials only.

### Open Lab: A collaborative multi-vendor platform for experimentation and validation of next-generation networking
                                        technologies
Speakers: Flavio Luciani
slides: https://www.itnog.it/itnog10/files/1-18_A collaborative multi-vendor platform for experimentation and validation of next-generation networking technologies.pdf
No abstract published; title, speakers and materials only.

### ITNOG Updates
Speakers: Marco Marzetti
No abstract published; title, speakers and materials only.

### The Network Automation Map: Navigate Your Journey with the NAF Automation Framework
Speakers: Christian Adell
slides: https://www.itnog.it/itnog10/files/2-11_ITNOG - The Network Automation Map.pdf
No abstract published; title, speakers and materials only.

### Antares: Multi-Agent AI for Automated Network Analysis and Troubleshooting in GARR Data Centers
Speakers: Francesco Lombardo
slides: https://www.itnog.it/itnog10/files/2-12_Antares-ITNOG10.pdf
No abstract published; title, speakers and materials only.

### AS/IXP Traffic Observability / Osservabilità del traffico AS/IXP
Speakers: Luca Deri Federico Santulli
slides: https://www.itnog.it/itnog10/files/2-13_trafficobservabilityITNOG_0426_FINALE.pdf
No abstract published; title, speakers and materials only.

### Semplificare l'automazione multi-vendor: Client RESTCONF auto-generati dai moduli YANG
Speakers: Matteo Colantonio
slides: https://www.itnog.it/itnog10/files/2-14_Matteo Colantonio semplificare automazione multivendor ITNOG10.pdf
No abstract published; title, speakers and materials only.

### Measuring the public Internet
Speakers: João Damas
slides: https://www.itnog.it/itnog10/files/2-15_APNIC ITNOG 10.pdf
No abstract published; title, speakers and materials only.

### Deep Dive nei KPI della Telefonia - Modelli Matematici e Architetture Dati per la Fraud Detection e la Revenue
                                        Assurance
Speakers: Emanuela Bevilacqua
slides: https://www.itnog.it/itnog10/files/2-16_kpi_ITNOG_EmanuelaBevilacqua_final.pdf
No abstract published; title, speakers and materials only.

### Open Networking and IPoDWDM in Production: Operational Lessons from European Networks
Speakers: Alessandro Giudice
slides: https://www.itnog.it/itnog10/files/2-17_IPoDWDM 400G ZR+ ITNOG10 v1.pdf
No abstract published; title, speakers and materials only.

### Splitting ottico passivo per ridondanza link
Speakers: Mirko Mosca
slides: https://www.itnog.it/itnog10/files/2-18_itnog10.2026-mosca-splitting-ottico.pdf
No abstract published; title, speakers and materials only.

