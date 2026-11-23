>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-127. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-127.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-127.md
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

Below is the program for IETF 127 (San Francisco). Read it and produce a digest
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
conference: IETF 127 (San Francisco)
source_url: https://datatracker.ietf.org/meeting/127/agenda.json
generated: 2026-11-23
registry_key: ietf-127
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## Working Group: 6man

### IPv6 issues with 802.11 multicast reliability remain
Draft: draft-ietf-6man-ieee80211-dms · Working group: 6man
Agenda: draft-ietf-6man-ieee80211-dms
page: https://datatracker.ietf.org/doc/draft-ietf-6man-ieee80211-dms/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-ipv6-issues-with-80211-multicast-reliability-remain-dms-00 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
For the IPv6 protocol stack, while IEEE 802.11 wireless networks can on a first abstraction be considered functionally identical to wired IEEE 802 networks, there are issues regarding reliability and survivability of multicast traffic. The existence of these issues has been known for some time. This document is to state that they are still being experienced, and summarize some previous and new approaches. Additionally, this document serves to collect consensus in the IETF process to make both the IEEE and Wi-Fi Alliance aware of these issues and request they be included in consideration for future development. 802.11 Directed Multicast Service and Flexible Multicast Service are noted as existing protocol features that may warrant more consideration. However, other solutions in that space may be more appropriate and are left to the expertise of the IEEE and Wi-Fi Alliance.

### The IPv6 Loopback Address Prefix
Draft: draft-ietf-6man-loopback · Working group: 6man
Agenda: draft-ietf-6man-loopback
page: https://datatracker.ietf.org/doc/draft-ietf-6man-loopback/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-the-ipv6-loopback-prefix-00 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
This document updates the IP Version 6 Address Architecture to expand the size of the IPv6 loopback space from a single address to a /48 prefix, formally defined as Node-Local Unicast space. This change allows for a much larger number of loopback addresses and internal virtual networks within an IPv6 host, which can be used for inter-process communication, local virtualization, container networking, and diagnostics. This document updates RFC 4291 to define the prefix and its functional semantics, and updates RFC 4007 to specify how the prefix is integrated into the scoped address architecture. It also updates the IANA IPv6 Address registry, the IPv6 Special- Purpose Address registry, and the Locally-Served DNS Zone Registry.

### Enforcement of IPv6 Extension Headers Ordering and Occurrence at Destination Nodes
Draft: draft-ietf-6man-eh-occurrences · Working group: 6man
Agenda: draft-ietf-6man-eh-occurrences
page: https://datatracker.ietf.org/doc/draft-ietf-6man-eh-occurrences/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-enforcement-of-ipv6-extension-headers-ordering-and-occurrence-at-destination-nodes-00 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
Operational experience has demonstrated that permitting multiple occurrences of the same IPv6 Extension Header can create parsing ambiguity, complicate packet processing, and increase potential security risks. Although RFC 8200 recommends that senders follow a specific order of appearance and limit the occurrences of Extension Headers, receivers cannot assume that these recommendations have been followed. This document updates RFC 8200 by allowing an IPv6 destination node, namely a host (i.e., the final destination of an IPv6 packet) or an intermediate destination node addressed by an entry in a Routing header list other than the final one, to enforce strict ordering and limits on the occurrence of Extension Headers.

### Hierarchical Cryptographically Generated Addresses (HCGA)
Draft: draft-buraglio-6man-hcga · Working group: 6man
Agenda: draft-buraglio-6man-hcga
page: https://datatracker.ietf.org/doc/draft-buraglio-6man-hcga/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-hierarchical-cryptographically-generated-addresses-02 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
RFC 3972 defines Cryptographically Generated Addresses (CGA), in which the Interface Identifier (IID) of an IPv6 address is derived from a cryptographic public key. The /64 subnet prefix is supplied by network infrastructure and has no cryptographic relationship to the key. This document specifies Hierarchical CGA (HCGA), an extension to RFC 3972 that also derives part of the upper 64 bits -- specifically the bits between the organizational prefix and the /64 boundary -- from the same public key. The result is an address whose full 128-bit value is a deterministic function of a public key (typically hardware-bound), an operator-controlled aggregate prefix, and two modifiers. HCGA is a traceability component intended for use within a larger accountability architecture that supplies key attestation, parameter distribution, and source-address enforcement; that architecture is not specified here. The capability supports workload network accountability in multi-tenant environments such as Kubernetes clusters, where infrastructure-assigned prefixes provide no per-instance cryptographic binding.

### A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label
Draft: draft-hu-6man-ipv6-flowlabel-load-balancing-rdma · Working group: 6man
Agenda: draft-hu-6man-ipv6-flowlabel-load-balancing-rdma
page: https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-a-rocev2-flow-level-load-balancing-method-based-on-the-ipv6-flow-label-00 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
This document proposes a method for achieving flow-level load balancing in RoCEv2 (RDMA over Converged Ethernet version 2) networks. Traditional per-flow load balancing based on the 5-tuple cannot distinguish between different RDMA sessions that share the same 5-tuple. This causes "elephant flows" to be hashed to the same path, leading to network congestion. This method resolves this issue by having the ingress network device (e.g., a data center gateway or DCI edge router) parse the QP (Queue Pair) information from the IB BTH (Base Transport Header) and IB DETH (Datagram Extended Transport Header, when present) of the RoCEv2 packet. By combining this with portions of the IPv6 source and destination addresses as an entropy source, a CRC32 hash algorithm generates a 32-bit value, the low 20 bits of which are then written into the Flow Label field of the IPv6 header. Network devices can subsequently use the updated "5-tuple + Flow Label" for more granular flow-level load balancing, thereby effectively improving transmission efficiency in high-performance networks for workloads such as AI computing.

### ICMP Error Handling in SRv6 based VPN Networks
Draft: draft-ali-6man-srv6-vpn-icmp-error-handling · Working group: 6man
Agenda: draft-ali-6man-srv6-vpn-icmp-error-handling
page: https://datatracker.ietf.org/doc/draft-ali-6man-srv6-vpn-icmp-error-handling/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-icmp-error-handling-for-vpns-in-srv6-networks-00 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
The document specifies procedures for handling ICMP error in SRv6-based Virtual Private Network (VPN).

### AERO/OMNI Base Specification Amendments (Volume 1)
Draft: draft-templin-6man-aero-omni-amen · Working group: 6man
Agenda: draft-templin-6man-aero-omni-amen
page: https://datatracker.ietf.org/doc/draft-templin-6man-aero-omni-amen/ | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
The Automatic Extended Route Optimization (AERO) and Overlay Multilink Network (OMNI) Interface functional specifications have reached a level of maturity ready for advancement in the RFC publication process. Updates to the base specifications are documented in this first amendment and any additional future amendments as necessary.

### Automatic Extended Route Optimization (AERO)
Draft: draft-templin-6man-aero3 · Working group: 6man
Agenda: draft-templin-6man-aero3
page: https://datatracker.ietf.org/doc/draft-templin-6man-aero3/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-automatic-extended-route-optimization-and-the-overlay-multilink-network-interface-aeroomni-00 | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
This document specifies an Automatic Extended Route Optimization (AERO) and mobility service for IP internetworking over Overlay Multilink Network (OMNI) Interfaces. AERO/OMNI use IPv6 Neighbor Discovery (IPv6 ND) control plane messaging over the OMNI virtual link to support secured network admission and OMNI link forwarding. Flow-based secure multilink path selection, multinet traversal, mobility management, multicast forwarding, multihop operation and route optimization are naturally supported through dynamic neighbor cache updates. AERO is a widely-applicable service well-suited for air/land/sea/space secure global mobile Internetworking applications including aviation, intelligent transportation systems, mobile end user devices, space exploration and many others.

### Transmission of IP Packets over Overlay Multilink Network (OMNI) Interfaces
Draft: draft-templin-6man-omni3 · Working group: 6man
Agenda: draft-templin-6man-omni3
page: https://datatracker.ietf.org/doc/draft-templin-6man-omni3/ | video: https://youtu.be/nExK52_b_RE | materials: https://datatracker.ietf.org/meeting/127/session/6man
Mobile nodes that operate in air/land/sea/space domains (e.g., aircraft of various configurations, terrestrial vehicles, seagoing vessels, space systems, enterprise wireless devices, pedestrians with cell phones, etc.) configure mobile routers to connect end user network peers with Internetwork correspondents over wireless and/or wired-line data links. This document presents a multilink virtual interface specification that supports mobile node coordination with a network-based mobility service, fixed node correspondents and/or other mobile node peers. The virtual interface provides an adaptation layer service that supports secure global mobile Internetworking. This document specifies the transmission of IP packets over Overlay Multilink Network (OMNI) Interfaces.

## Working Group: bess

### EVPN multi-homing support for L3 services
Draft: draft-ietf-bess-evpn-l3mh-proto · Working group: bess
Agenda: draft-ietf-bess-evpn-l3mh-proto Patrice Brissette 10 min 09:15 - 09:25
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-l3mh-proto/ | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
This document describes the use of EVPN Ethernet Segment Link Aggregation Group (ES-LAG) technology to provide multi-homing redundancy for Layer 3 services. The solution synchronizes ARP/ND, multicast state, and IGP routes between redundant PEs without requiring Layer 2 constructs or proprietary Inter-Chassis Communication protocols.

### EVPN Anycast Multi-Homing
Draft: draft-rabnag-bess-evpn-anycast-aliasing · Working group: bess
Agenda: draft-rabnag-bess-evpn-anycast-aliasing-06 Jorge Rabadan 05 min 09:25 - 09:30
page: https://datatracker.ietf.org/doc/draft-rabnag-bess-evpn-anycast-aliasing/ | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
The current Ethernet Virtual Private Network (EVPN) all-active multi- homing procedures in Network Virtualization Over Layer-3 (NVO3) networks provide the required Split Horizon filtering, Designated Forwarder Election and Aliasing functions that the network needs in order to handle the traffic to and from the multi-homed CE in an efficient way. In particular, the Aliasing function supports load balancing of unicast traffic from remote Network Virtualization Edge (NVE) devices to NVEs that are multi-homed to the same CE, regardless of whether the CE’s MAC/IP information has been learned on all those NVEs. This document introduces an optional enhancement to the EVPN multi-homing Aliasing function, referred to as EVPN Anycast Multi- homing. This optimization is specific to EVPN deployments over NVO3 tunnels (i.e., IP-based tunnels) and may offer benefits in typical data center designs, which are discussed herein.

### Applicability of EVPN Assisted Replication to SRv6 Tunnels
Draft: draft-rabadan-bess-evpn-srv6-ar · Working group: bess
Agenda: draft-rabadan-bess-evpn-srv6-ar-00 Jorge Rabadan 10 min 09:30 - 09:40
page: https://datatracker.ietf.org/doc/draft-rabadan-bess-evpn-srv6-ar/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-ietf127-bess-evpn-srv6-ar-00-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
Assisted Replication (AR) is an optimized ingress replication solution for Ethernet VPN (EVPN) Broadcast and Multicast (BM) traffic. AR offloads the replication effort from ingress Network Virtualization Edge (NVE) devices onto Assisted Replication Replicators (AR-REPLICATORs). The base AR specification is focused on Network Virtualization Overlay (NVO) networks that use IP tunnels, and it is typically deployed for Virtual eXtensible Local Area Network (VXLAN). EVPN services can also be instantiated over Segment Routing over IPv6 (SRv6); however, the SRv6 EVPN transport specification supports only ingress replication for BUM traffic, and the AR procedures rely on IP-tunnel semantics (such as the tunnel source and destination IP addresses) that do not map exactly to an SRv6 data plane. As a result, AR cannot be readily deployed over SRv6 tunnels. This document specifies the applicability of Assisted Replication to SRv6 tunnels, for EVPN BM traffic, for selective multicast based on Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) proxy, and for EVPN IP multicast traffic based on Optimized Inter-Subnet Multicast (OISM). It defines a new SRv6 Endpoint behavior for the AR-REPLICATOR role and the associated control-plane procedures, so that the AR solution can be used with an SRv6 underlay.

### Multicast Router State Synchronization in EVPN Networks
Draft: draft-jot-bess-evpn-mcast-router-sync · Working group: bess
Agenda: draft-jot-bess-evpn-mcast-router-sync-01 Jorge Rabadan 05 min 09:40 - 09:45
page: https://datatracker.ietf.org/doc/draft-jot-bess-evpn-mcast-router-sync/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-ietf127-bess-evpn-mcast-router-sync-01-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
Ethernet VPN (EVPN) networks support multicast applications in which multicast routers and multicast hosts are attached to the same tenant. Existing specifications define how Provider Edge (PE) devices synchronize the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) membership state of multihomed multicast hosts, and how Optimized Inter-Subnet Multicast (OISM) forwarding interacts with multicast routers via PIM EVPN Gateways. However, none of the existing specifications addresses the synchronization of the state associated with a multicast router (an IGMP/MLD Querier or a Protocol Independent Multicast (PIM) router) when that router is multihomed to a set of EVPN PEs. This document specifies a new EVPN route, the Multicast Router Discovery (MRD) route, and the procedures to synchronize multicast router state across the PEs of an Ethernet Segment, for routers attached to multicast Broadcast Domains or to Layer 3 interfaces.

### EVPN Subnet Slicing
Draft: draft-sajassi-bess-evpn-subnet-slicing · Working group: bess
Agenda: draft-sajassi-bess-evpn-subnet-slicing-00 Ali Sajassi 15 min 09:45 - 10:00
page: https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-subnet-slicing/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-draft-sajassi-bess-evpn-subnet-slicing-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
Ethernet VPN (EVPN) Integrated Routing and Bridging (IRB) distributes Layer 2 and Layer 3 reachability through BGP. In a large stretched broadcast domain, traditional IRB can cause every Provider Edge (PE) to install MAC and IP addresses for every endpoint in the subnet thus resulting in exhaustion of forwarding resources (MAC-VRF and IP-VRF) on the PEs - i.e., route population is approximately proportional to the number of endpoints in every stretched subnet imported by the PE [Optimized-IRB] proposes a solution to alleviate the MAC-VRF resource consumption by terminating ARP/ND messages on the PE and providing L3 forwarding (routing) for both intra and inter subnets. Therefore, eliminating the need for MAC lookups and the maintenance of MAC addresses in MAC-VRF for IP hosts. However, this solution does not solve the IP-VRF resource consumption issue as IP host addresses still need to be maintained in IP-VRF for both the locally connected hosts and the remote hosts. This problem is particularly pronounced in campus networks where most subnets are stretched across the entire campus (and thus all access switches) and the access switches used as EVPN-IRB PE devices have significantly smaller forwarding tables and hence limit the total endpoint scale that can be attached to stretched subnets across the network. This document defines an EVPN Subnet Slicing solution to horizontally scale stretched subnets across the network without being constrained by any PE's forwarding table size. The solution enables access layer PE devices to maintain only locally attached host routes and allows host routes to be distributed across distribution or aggregation layer PE devices as opposed to each PE maintaining all host IP routes.

### EVPN Group Policy
Draft: draft-lrss-bess-evpn-group-policy · Working group: bess
Agenda: draft-lrss-bess-evpn-group-policy-03 Ali Sajassi 05 min 10:00 - 10:05
page: https://datatracker.ietf.org/doc/draft-lrss-bess-evpn-group-policy/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-draft-lrss-bess-evpn-group-policy-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
Group Based Policy can be used to achieve micro or macro segmentation of user traffic. For Group Based Policy, a Group Policy ID, also known as Group Policy Tag, is used to represent a logical group that shares the same policy and access privilege. This document defines a backward compatible extension to Virtual eXtensible Local Area Network (VXLAN) that allows a Group Policy ID to be carried for the purposes of policy enforcement at the egress Network Virtualization Edge (NVE). It also defines a new BGP Extended Community that can be used to propagate Group Policy ID through a BGP route advertisement in the control plane. This is to facilitate policy enforcement at the ingress NVE when feasible.

### L3 fast convergence for all-active multi-homing for EVPN/ MVPN Seamless interoperation
Draft: draft-vgovindan-bess-evpn-mvpn-seamles-mh-converge · Working group: bess
Agenda: draft-vgovindan-bess-evpn-mvpn-seamles-mh-converge-00 Ali Sajassi 10 min 10:05 - 10:15
page: https://datatracker.ietf.org/doc/draft-vgovindan-bess-evpn-mvpn-seamles-mh-converge/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-draft-vgovindan-bess-evpn-mvpn-seamles-mh-converge-00-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
This document specifies the procedures for achieving faster Layer-3 convergence from link/ node failures when all-active multi-homing is used with EVPN/ MVPN seamless interop [draft-ietf-bess-evpn-mvpn- seamless-interop]. Specifically, these improvements apply when L3 routed multicast services are deployed by BGP/ EVPN PEs using the procedures defined by the above draft.

### Export of BGP VPN Information in IPFIX
Draft: draft-liu-bess-ipfix-bgp-vpn · Working group: bess
Agenda: draft-liu-bess-ipfix-bgp-vpn Yao 05 min 10:15 - 10:20
page: https://datatracker.ietf.org/doc/draft-liu-bess-ipfix-bgp-vpn/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-draft-liu-bess-ipfix-bgp-vpn-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
This document introduces new IP Flow Information Export (IPFIX) information elements to carry information that can be used to identify the egress PE in BGP VPN scenarios.

### L3 Multi-homing update
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-l3-multi-homing-update-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### ietf127-bess-evpn-anycast-multihoming-06
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-ietf127-bess-evpn-anycast-multihoming-06-00 | video: https://youtu.be/nryz9SzoysI | materials: https://datatracker.ietf.org/meeting/127/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

## Working Group: cats

### CATS Metrics Definition
Draft: draft-ietf-cats-metric-definition · Working group: cats
Agenda: https://datatracker.ietf.org/doc/draft-ietf-cats-metric-definition/
page: https://datatracker.ietf.org/doc/draft-ietf-cats-metric-definition/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-cats-21-cats-metrics-definition-00 | video: https://youtu.be/0NKyw6J4pOU | materials: https://datatracker.ietf.org/meeting/127/session/cats
Computing-Aware Traffic Steering (CATS) is a traffic engineering approach that optimizes the steering of traffic to a service instance by considering the dynamic state of computing and network resources. To enable such decisions, CATS components exchange metrics that describe resource conditions affecting service instance selection. This document focuses on compute and communication metrics for CATS and defines a hierarchical abstraction of these metrics to improve interoperability, scalability, and operational simplicity. It does not aim to standardize raw infrastructure (Level 0) metrics; instead, it specifies higher-level representations that can be derived from raw measurements using aggregation and normalization functions.

### Data Model for Computing-Aware Traffic Steering (CATS)
Draft: draft-ietf-cats-data-model · Working group: cats
Agenda: https://datatracker.ietf.org/doc/draft-ietf-cats-data-model/
page: https://datatracker.ietf.org/doc/draft-ietf-cats-data-model/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-cats-23-cats-data-model-01 | video: https://youtu.be/0NKyw6J4pOU | materials: https://datatracker.ietf.org/meeting/127/session/cats
This document defines a YANG data model for the management of Computing-Aware Traffic Steering (CATS) systems.

### Protocols Applicability for Computing-Aware Traffic Steering (CATS)
Draft: draft-yxl-cats-protocols-applicability · Working group: cats
Agenda: https://datatracker.ietf.org/doc/draft-yxl-cats-protocols-applicability/
page: https://datatracker.ietf.org/doc/draft-yxl-cats-protocols-applicability/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-cats-3-cats-protocols-applicability-00 | video: https://youtu.be/0NKyw6J4pOU | materials: https://datatracker.ietf.org/meeting/127/session/cats
This document analyzes the applicability of protocols related to a CATS system, and describes how to build a CATS system by extending existing IETF protocols.

### CATS OAM Framework
Presentation · Working group: cats
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-cats-22-cats-oam-framework-00 | video: https://youtu.be/0NKyw6J4pOU | materials: https://datatracker.ietf.org/meeting/127/session/cats
Slides presented at the cats session; no Internet-Draft is linked to them.

## Working Group: ccwg

### BBR Congestion Control
Draft: draft-ietf-ccwg-bbr · Working group: ccwg
Agenda: BBRv3 , draft-ietf-ccwg-bbr , Ian Swett , onsite, 15 minutes
page: https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-analysis-for-the-differences-between-standard-congestion-control-schemes-draft-nishida-ccwg-standard-cc-analysis-01 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
This document specifies the BBR congestion control algorithm. BBR ("Bottleneck Bandwidth and Round-trip propagation time") uses recent measurements of a transport connection's delivery rate, round-trip time, and packet loss rate to build an explicit model of the network path. BBR then uses this model to control both how fast it sends data and the maximum volume of data it allows in flight in the network at any time. Relative to loss-based congestion control algorithms such as Reno [RFC5681] or CUBIC [RFC9438], BBR offers substantially higher throughput for bottlenecks with shallow buffers or random losses, and substantially lower queueing delays for bottlenecks with deep buffers (avoiding "bufferbloat"). BBR can be implemented in any transport protocol that supports packet-delivery acknowledgment. Thus far, open source implementations are available for TCP [RFC9293] and QUIC [RFC9000]. This document specifies version 3 of the BBR algorithm, BBRv3.

### Self-Clocked Rate Adaptation for Multimedia
Draft: draft-ietf-ccwg-rfc8298bis-screamv2 · Working group: ccwg
Agenda: SCReAMv2 , draft-ietf-ccwg-rfc8298bis-screamv2 , Ingemar Johansson , remote, 15 minutes
page: https://datatracker.ietf.org/doc/draft-ietf-ccwg-rfc8298bis-screamv2/ | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
This memo describes Self-Clocked Rate Adaptation for Multimedia version 2 (SCReAMv2), an update to SCReAM congestion control for media streams such as RTP [RFC3550]. SCReAMv2 includes several algorithm simplifications and adds support for L4S. The algorithm supports handling of multiple media streams, typical use cases are streaming for remote control, AR and 3D VR goggles. This specification obsoletes RFC 8298.

### Network Delivery Time Control
Draft: draft-ageneau-ccwg-ndtc · Working group: ccwg
Agenda: Network Delivery Time Control , draft-ageneau-ccwg-ndtc , Paul-Louis Ageneau , remote, 5 minutes
page: https://datatracker.ietf.org/doc/draft-ageneau-ccwg-ndtc/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-network-delivery-time-control-update-00 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
This document describes Network Delivery Time Control (NDTC), a rate adaptation algorithm for real-time video streaming suited for interactive applications like cloud gaming. NDTC leverages the Frame Dithering Available Capacity Estimation (FDACE) heuristic, which estimates available path capacity without inducing congestion. The algorithm dynamically adjusts frame sizes and transmission times to ensure timely delivery, while also responding to conventional congestion signals.

### CUBACK: CUBIC Driven by the ACK Clock
Draft: draft-kazuho-ccwg-cuback · Working group: ccwg
Agenda: CUBACK: CUBIC Driven by the ACK Clock , draft-kazuho-ccwg-cuback , Kazuho Oku , onsite, 15 minutes
page: https://datatracker.ietf.org/doc/draft-kazuho-ccwg-cuback/ | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
This document specifies Cuback, an ACK-driven reformulation of CUBIC congestion control. It simplifies implementation by replacing CUBIC's mutable time- and ACK-driven state with pure functions over immutable per-epoch parameters, for which test vectors are provided. Congestion-window growth uses the same ACK-driven mechanism as Reno, removing several sources of implementation error. When entering a high-capacity path, a newcomer converges on its share sooner than under CUBIC, so short flows complete earlier.

### Analysis for the Differences Between Standard Congestion Control Schemes
Draft: draft-nishida-ccwg-standard-cc-analysis · Working group: ccwg
Agenda: Analysis for the Differences Between Standard Congestion Control Schemes , draft-nishida-ccwg-standard-cc-analysis , Yoshifumi Nishida , onsite, 15 minutes
page: https://datatracker.ietf.org/doc/draft-nishida-ccwg-standard-cc-analysis/ | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
The IETF currently has three Standards Track specifications of loss- based congestion control: Reno-based congestion control for TCP (RFC 5681), its counterpart for QUIC (RFC 9002), and CUBIC (RFC 9438), which updates RFC 5681. They are intended to follow the same congestion control principles, but they differ in their mechanisms, parameters, and normative requirements, and these differences have not been reconciled with each other. This document identifies such differences, summarizes whether and how each of them is documented in the specifications, and asks the IETF to determine for each difference whether to work toward convergence or accept it as is.

### Specification of Christian's Congestion Control Code (C4)
Draft: draft-huitema-ccwg-c4-spec · Working group: ccwg
Agenda: C4 , draft-huitema-ccwg-c4-spec , draft-huitema-ccwg-c4-design , draft-huitema-ccwg-c4-test , Christian Huitema , remote, 15 minutes
page: https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-spec/ | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Christian's Congestion Control Code is a new congestion control algorithm designed to support Real-Time applications such as Media over QUIC. It is designed to drive towards low delays, with good support for the "application limited" behavior frequently found when using variable rate encoding, and with fast reaction to congestion to avoid the "priority inversion" happening when congestion control overestimates the available capacity. The design emphasizes simplicity and avoids making too many assumptions about the "model" of the network.

### Design of Christian's Congestion Control Code (C4)
Draft: draft-huitema-ccwg-c4-design · Working group: ccwg
Agenda: C4 , draft-huitema-ccwg-c4-spec , draft-huitema-ccwg-c4-design , draft-huitema-ccwg-c4-test , Christian Huitema , remote, 15 minutes
page: https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-design/ | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Christian's Congestion Control Code is a new congestion control algorithm designed to support Real-Time applications such as Media over QUIC. It is designed to drive towards low delays, with good support for the "application limited" behavior frequently found when using variable rate encoding, and with fast reaction to congestion to avoid the "priority inversion" happening when congestion control overestimates the available capacity. It pays special attention to the high jitter conditions encountered in Wi-Fi networks. The design emphasizes simplicity and avoids making too many assumption about the "model" of the network. The main control variables are the estimate of the data rate and of the maximum path delay in the absence of queues.

### Testing of Christian's Congestion Control Code (C4)
Draft: draft-huitema-ccwg-c4-test · Working group: ccwg
Agenda: C4 , draft-huitema-ccwg-c4-spec , draft-huitema-ccwg-c4-design , draft-huitema-ccwg-c4-test , Christian Huitema , remote, 15 minutes
page: https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-test/ | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Christian's Congestion Control Code is a new congestion control algorithm designed to support Real-Time applications such as Media over QUIC. It is designed to drive towards low delays, with good support for the "application limited" behavior frequently found when using variable rate encoding, and with fast reaction to congestion to avoid the "priority inversion" happening when congestion control overestimates the available capacity. The design was validated by series of simulations, and also by initial deployments in control networks. We describe here these simulations and tests.

### BBR at CCWG
Presentation · Working group: ccwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-bbr-at-ccwg-00 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Slides presented at the ccwg session; no Internet-Draft is linked to them.

### SCReAM V2
Presentation · Working group: ccwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-scream-v2-00 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Slides presented at the ccwg session; no Internet-Draft is linked to them.

### Cuback
Presentation · Working group: ccwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-cuback-00 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Slides presented at the ccwg session; no Internet-Draft is linked to them.

### C4: control without delay
Presentation · Working group: ccwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-c4-control-without-delay-00 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Slides presented at the ccwg session; no Internet-Draft is linked to them.

### C4: control without delay (PPT)
Presentation · Working group: ccwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-c4-control-without-delay-ppt-00 | video: https://youtu.be/pXwvZqkML7I | materials: https://datatracker.ietf.org/meeting/127/session/ccwg
Slides presented at the ccwg session; no Internet-Draft is linked to them.

## Working Group: dnsop

### DNS Protocol Modifications for Delegation Extensions
Draft: draft-ietf-dnsop-delext · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delext/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
The Domain Name System (DNS) protocol permits Delegation Signer (DS) records at delegation points. This document specifies modifications to the DNS protocol to permit a range of Resource Record types at delegation points. These modifications are designed to maintain compatibility with existing DNS resolution mechanisms and provide a secure method for processing these records at delegation points. This document updates RFCs 1034, 4035, 6672, 6840, 6895, and 9824.

### Extensible Delegation for DNS
Draft: draft-ietf-deleg · Working group: dnsop
Agenda: Not presented here; deferred to the DELEG WG session (Thursday, 11:00-12:30), together with draft-ietf-deleg
page: https://datatracker.ietf.org/doc/draft-ietf-deleg/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
This document specifies a new extensible method for the delegation of authority for a domain in the Domain Name System (DNS) using DELEG and DELEGPARAM records. A delegation in the DNS enables efficient and distributed management of the DNS namespace. The traditional DNS delegation is based on NS records which contain only hostnames of servers and no other parameters. In classic DNS, both parent and child zones contain copies of NS delegation records, which can potentially be out of sync and confusing. The new delegation records are extensible, can be secured with DNSSEC, and eliminate the problem of having two sources of truth for delegation information.

### Automating DNS Delegation Management via DDNS
Draft: draft-ietf-dnsop-delegation-mgmt-via-ddns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delegation-mgmt-via-ddns/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delegation-mgmt-via-ddns/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
Delegation information (i.e. the NS RRset, possible glue, possible DS records) should always be kept in sync between child zone and parent zone. However, in practice that is not always the case. When the delegation information is not in sync the child zone is usually working fine, but without the amount of redundancy that the zone owner likely expects to have. Hence, should any further problems ensue it could have catastrophic consequences. The DNS name space has lived with this problem for decades and it never goes away. Or, rather, it will never go away until a fully automated mechanism for how to keep the information in sync automatically is deployed. This document proposes such a mechanism based on DNS Dynamic Updates (DDNS) secured with SIG(0) signatures, sent from the child to the parent across the zone cut. The target of the update is discovered via the DSYNC record defined in [RFC9859]. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-ietf-dnsop-delegation-mgmt-via-ddns (https://github.com/johanix/draft-ietf-dnsop-delegation-mgmt-via- ddns). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### A Top-level Domain for Private Use
Draft: draft-davies-internal-tld · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-davies-internal-tld/
page: https://datatracker.ietf.org/doc/draft-davies-internal-tld/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessa-a-top-level-domain-for-private-use-internal-00 | video: https://youtu.be/0AQ_CI7xQP0 | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
This document describes the "internal" top-level domain for use in private applications.

### Optimistic DNS
Draft: draft-gakiwate-dnsop-optimistic-dns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-optimistic-dns/
page: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-optimistic-dns/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessa-optimistic-dns-updates-00 | video: https://youtu.be/0AQ_CI7xQP0 | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
DNS lookups introduce user-visible delay, particularly when cached records have expired and must be refreshed from the network. This document describes Optimistic DNS, a client-side stub resolver mechanism that immediately returns expired cached DNS records to applications while simultaneously refreshing them with a network query. The application receives an answer in microseconds rather than milliseconds, and if the data has changed receives an updated answer shortly thereafter. Optimistic DNS is complementary to RFC 8767, which addresses serving stale data at recursive resolvers. This document focuses exclusively on client-side stub resolver behavior, including explicit signaling from the application to inform the stub resolver that the application is able to handle old and possibly incorrect information.

### Signer-Zone Containment for DNSSEC Wildcard Validation
Draft: draft-zhang-dnssec-wildcard-validation · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-zhang-dnssec-wildcard-validation/
page: https://datatracker.ietf.org/doc/draft-zhang-dnssec-wildcard-validation/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessa-signer-zone-containment-for-dnssec-wildcard-validation-00 | video: https://youtu.be/0AQ_CI7xQP0 | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
Validators for the DNS Security Extensions (DNSSEC) reconstruct the original owner name of a signed resource record set (RRset) using the RRSIG Labels field. This document updates RFC 4035 to make explicit how its existing signing-zone authority requirement applies to that reconstructed owner, and updates RFC 8198 to preserve the authenticated association between wildcard data, its original owner, and its signing zone during cache reuse. These clarifications prevent cryptographically correct signatures from being treated as authenticating wildcard sources outside the signing zone. They do not change DNS wildcard matching or synthesis rules, or DNS message formats.

### Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC
Draft: draft-kaizer-dnsop-ml-dsa-mtl-dnssec · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/
page: https://datatracker.ietf.org/doc/draft-kaizer-dnsop-ml-dsa-mtl-dnssec/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
This document describes how to apply the Module-Lattice-Based Digital Signature Algorithm (ML-DSA) and Merkle Tree Ladders (MTL) as a conservative post-quantum cryptographic algorithm for DNS Security Extensions (DNSSEC). This combination is referred to as the ML-DSA- MTL Signature scheme. This document describes how to specify ML-DSA- MTL keys and signatures in DNSSEC, specifically for ML-DSA-44 with SHAKE-128.

### Module-Lattice-Based Signatures with Merkle Tree Ladders (ML-DSA-MTL) for DNSSEC with SigTag Extension
Draft: draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext/
page: https://datatracker.ietf.org/doc/draft-hdong-dnsop-ml-dsa-mtl-dnssec-sigtag-ext/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
This document describes a mechanism to reduce post-quantum cryptographic (PQC) network transmission overhead when using Merkle Tree Ladders (MTL) in DNS Security Extensions (DNSSEC). This document refers to this as SigTag and describes the use of EDNS(0) to enable its use. SigTag allows a client to indicate its knowledge of a specific MTL ladder. The DNS server can then use this signal to determine if it can omit the full underlying signature in its response, thereby reducing the message payload.

### The MERKLE3 Incremental Scheme for ZONEMD
Draft: draft-aklpdw-dnsop-zonemd-incremental · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-aklpdw-dnsop-zonemd-incremental/
page: https://datatracker.ietf.org/doc/draft-aklpdw-dnsop-zonemd-incremental/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessa-the-merkle3-incremental-scheme-for-zonemd-00 | video: https://youtu.be/0AQ_CI7xQP0 | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
The ZONEMD Resource Record affirms the integrity of whole DNS zones and helps verify their authenticity. It embeds a cryptographic hash of the zone data, collated in a configurable way. It is used as a checksum for zone transfers between name servers. [RFC8976] defined a single ZONEMD collation scheme, SIMPLE. It is sufficient for small and infrequently updated zones. This document introduces the MERKLE3 scheme, targeting large, dynamic zones. It uses a Merkle tree to enable parallelism and incremental computation.

### Refusing DNS Queries That Have QTYPE=RRSIG
Draft: draft-sury-dnsop-rrsig-refused · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-sury-dnsop-rrsig-refused/
page: https://datatracker.ietf.org/doc/draft-sury-dnsop-rrsig-refused/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessb-01-refusing-dns-queries-that-have-qtyperrsig-00 | video: https://youtu.be/QA-JGOL-e7w | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
The Domain Name System (DNS) allows a query with QTYPE=RRSIG. Such a query has no useful answer. RRSIG resource records are meaningful only together with the resource records they cover, so a response can carry no more than an arbitrary subset of the signatures present at the query name. This document specifies that DNS responders refuse queries with QTYPE=RRSIG, and that DNS requestors do not send them. It supplies the guidance that [RFC8482] left unspecified.

### Continuing to Reduce Support for ANY Queries in the DNS
Draft: draft-jabley-dnsop-no-longer-support-any · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-jabley-dnsop-no-longer-support-any/
page: https://datatracker.ietf.org/doc/draft-jabley-dnsop-no-longer-support-any/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
The DNS specification from its earliest day supported a special query type (QTYPE) ANY. The handling of queries with QTYPE=ANY is observed to vary between implementations. Queries with QTYPE=ANY are known to facilitate amplification that can be abused and used by malicious actors to attack third parties, and minimally-sized responses are often constructed in order to mitigate those security risks. While queries with QTYPE=ANY can be used for troubleshooting in some cases, the substantial inconsistency in how such queries are handled makes them at best an unreliable signal. This document continues a careful and gradual process of dropping support for QTYPE=ANY from the DNS.

### Ordering of RRSets in CNAME Responses in the DNS
Draft: draft-jabley-dnsop-ordered-answer-section · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/
page: https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessb-draft-jabley-dnsop-ordered-answer-section-02-00 | video: https://youtu.be/QA-JGOL-e7w | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
In the DNS, recursive resolvers receive queries and formulate corresponding responses by reference to data obtained from authoritative servers. In the case where the query name (QNAME) and class (QCLASS) in the query matches an owner name in the DNS where a canonical name (CNAME) resource record is published, the response includes both the CNAME record and the resource record set corresponding to the request's query type (QTYPE) published at the CNAME target. The ordering of these two different RRSets has not previously been clearly specified, but operational experience based on real-world client implementations confirms that the order is important. This document updates RFC 1034 1035 to provide a clearer specification, consistent with deployed implementations.

### The Domain Set Discovery Protocol (domain-set)
Draft: draft-barrett-dnsop-domain-set · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-barrett-dnsop-domain-set/
page: https://datatracker.ietf.org/doc/draft-barrett-dnsop-domain-set/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessb-domain-set-declaring-in-the-dns-which-domains-one-organization-operates-01 | video: https://youtu.be/QA-JGOL-e7w | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
Organizations commonly operate under multiple domain names: a primary website, legacy names, defensive registrations, divisional brands, and names in restricted or verified top-level domains. No standard mechanism exists for a domain owner to declare, in a machine-readable and verifiable way, which domains belong to the same organization. This document defines "domain-set", a protocol by which domain operators publish membership in a set of domains using a DNS TXT record as the discovery mechanism. The record either lists the members directly or references an extensible Domain Set Manifest retrieved over HTTPS. Mutual attestation is the validation requirement: a link between two domains is valid only when both domains independently publish records naming each other. Every direction of a link MUST be retrieved over an authenticated channel, by DNSSEC or by the Web PKI. The protocol enables browsers, security tooling, and AI systems to answer the question "are these two domains operated by the same organization?" from first-party, owner-published data rather than inference.

### Globally Relevant HTTPS RRs
Draft: draft-kinnear-dnsop-globally-relevant · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-kinnear-dnsop-globally-relevant/
page: https://datatracker.ietf.org/doc/draft-kinnear-dnsop-globally-relevant/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessb-globally-relevant-records-00 | video: https://youtu.be/QA-JGOL-e7w | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
DNS answers for SVCB and HTTPS resource records are typically treated as scoped to the network on which they were obtained. This requires clients to re-resolve DNS when changing network attachments, adding latency to connection establishment. This document defines a new SvcParamKey, "globally-relevant", for use in SVCB and HTTPS DNS resource records as defined in [RFC9460]. When present, this boolean flag indicates that the service binding parameters in the record are valid regardless of the client's network attachment point. Clients that observe this flag can reuse cached SVCB and HTTPS records across network changes, subject to normal TTL expiry.

### Using Secure DNS for Originator Profile
Draft: draft-shigeya-dns-opkey · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-shigeya-dns-opkey/
page: https://datatracker.ietf.org/doc/draft-shigeya-dns-opkey/ | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
The Originator Profile Framework (OPF) provides information about the origin of content, together with a verifiable binding of the content to that origin, in digital media, advertising, and email ecosystems. In the framework, an originator holds an Originator Profile (OP): a Core Profile (CP) issued by a CP issuer, and Profile Annotations (PA) issued by PA issuers. The CP carries the public keys with which the originator signs the data it originates; a PA annotates the CP with validated attributes about the originator. Verifiers need an authenticated way to confirm that the public keys used by an originator and by the issuers of these documents are currently valid, that the originator's CP has not been revoked by its CP issuer, and that a PA has not been revoked by its PA issuer. This document defines the OPKEY DNS resource record, which associates a public key with a DNS name under the _op label. Its wire and presentation formats are those of the TLSA record. The DNS does not carry the CP or the PAs themselves; it carries records that identify their keys by digest, and it signals, through the presence or absence of OPKEY records, whether a CP has been revoked. The document specifies where OPKEY records are located, how a verifier uses them, and how DNSSEC is used to authenticate them. It also specifies two further records under _op, of existing types: an SVCB record by which an originator names the CP issuers it accepts, and a TXT record whose presence signals that a PA issuer has revoked a PA. Operational aspects of the framework, such as registration, key rollover procedures, and revocation timing, are outside the scope of this document.

### Update on Merkle Tree Ladders for PQC DNSSEC
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessa-update-on-merkle-tree-ladders-for-pqc-dnssec-00 | video: https://youtu.be/0AQ_CI7xQP0 | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### Stop ANYthing
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessa-stop-anything-00 | video: https://youtu.be/QA-JGOL-e7w | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### OPKEY: DNSSEC-signed key digests and revocation signals for Originator Profile
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-dnsop-sessb-opkey-dnssec-signed-key-digests-and-revocation-signals-for-originator-profile-01 | video: https://youtu.be/QA-JGOL-e7w | materials: https://datatracker.ietf.org/meeting/127/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

## Working Group: grow

### BGP Message Counters for BGP Monitoring Protocol (BMP)
Draft: draft-choudhary-grow-bmp-bgp-msg-stats · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-choudhary-grow-bmp-bgp-msg-stats/
page: https://datatracker.ietf.org/doc/draft-choudhary-grow-bmp-bgp-msg-stats/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-01-slides-draft-choudhary-grow-bmp-bgp-msg-stats-ietf127-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
The BGP Monitoring Protocol (BMP) [RFC7854] Statistics Report carries RIB occupancy, policy, and route-processing metrics. Some existing types count UPDATE messages, but only as special cases grouped by result (duplicates, loops, and errors). No statistic gives a total count of each BGP message type. This document defines those totals as new BMP Statistics Types (UPDATE, KEEPALIVE, NOTIFICATION, ROUTE-REFRESH, and all BGP PDUs in each direction), states the operational use cases that motivate them, and records explicit non-goals so that last-error content, negotiated timer values, and implementation-specific internals remain out of scope.

### Efficient BMP Route Monitoring Messages
Draft: draft-liu-grow-bmp-rm-aggregated · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-02-update-on-the-proposed-merge-of-bmp-aggregated-route-monitoring-and-common-updates-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
This document proposes two complementary optimizations for the BGP Monitoring Protocol (BMP) Route Monitoring message to significantly reduce network overhead and improve monitoring efficiency. The first optimization defines an aggregated BMP Route Monitoring message based on the Multi-Peer Header mechanism, which compresses multiple BMP Route Monitoring messages into a single aggregated message by leveraging BGP group packaging technology. The second optimization introduces a Common Update TLV that eliminates redundant transmission of routes unchanged by inbound or outbound policies across different RIB views. These optimizations work together to reduce the number of reported BMP messages, decrease bandwidth consumption, and improve processing efficiency for both monitored routers and monitoring stations.

### Common BMP Route-Monitoring Messages for Routes Unchanged by Policy
Draft: draft-patki-grow-bmp-common-updates · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/
page: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/ | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
A route unmodified by the inbound policy on a monitored router is included both in Pre-Policy Adj-RIB-In as well as Post-Policy Adj- RIB-In Route-Monitoring messages when both the Pre-Policy and Post- Policy Route-Monitoring modes are enabled. Similarly, a route unmodified by the outbound policy is included in Pre-Policy Adj-RIB- Out as well as Post-Policy Adj-RIB-Out Route-Monitoring messages. This document defines a method to avoid duplicate inclusion of routes unmodified by policy either in Adj-RIB-In or Adj-RIB-Out.

### Generic Event Notification (GEN) for BGP Monitoring Protocol (BMP)
Draft: draft-sp-grow-bmp-gen · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-sp-grow-bmp-gen/
page: https://datatracker.ietf.org/doc/draft-sp-grow-bmp-gen/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-03-tentative-directional-update-on-the-proposed-bmp-event-framework-merge-gen-and-rel-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
This document defines a new BMP message type: the Generic Event Notification (GEN). The BMP GEN message provides a flexible mechanism for reporting a wide variety of events related to BGP at different levels of hierarchy, such as routing instance, AFI/SAFI, or peer level. The BMP GEN message enables operators and automated systems to receive detailed context for operational events, such as policy triggers, administrative interventions, and state management notifications (e.g., RIB view unmonitor events).

### Logging of routing events in BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-rel · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/ | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
The BGP Monitoring Protocol (BMP) does provide for BGP session event logging (Peer Up, Peer Down), state synchronization (Route Monitoring), debugging (Route Mirroring) and Statistics messages, among others. This document defines a new Route Event Logging (REL) message type for BMP with the aim of covering use cases with affinity to alerting, reporting and on-change analysis.

### BMP Statistics Information TLV
Draft: draft-ietf-grow-bmp-stats-informational-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-stats-informational-tlv/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-stats-informational-tlv/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-04-bmp-statistics-information-tlv-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
The BGP Monitoring Protocol (BMP) defines statistics reports that provide periodic snapshots of various BGP-related metrics. When statistics are reported periodically, the snapshot values may not reflect the variations that occurred between reporting intervals. This document defines a Statistics Information TLV that can be used to convey additional statistical information about BMP gauge-type statistics during the reporting period. This TLV reports the minimum and maximum values observed (with timestamps indicating when they occurred), along with additional statistical measures such as average, percentiles, or snapshot values. This enables BMP collectors to better understand the dynamics of monitored statistics even when the reported snapshot values appear constant.

### Requirements for Monitoring RPKI-Related Processes on Routers Using BMP
Draft: draft-wang-grow-bmp-rpki-mon-reqs · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/
page: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-05-requirements-for-monitoring-rpki-related-processes-on-routers-using-bmp-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
This document outlines requirements for extending the BGP Monitoring Protocol (BMP) to provide comprehensive monitoring of RPKI-related processes on routers, including RPKI data acquisition, RPKI-related policy configuration, route validation, and the impact of validation on routing decisions. The proposed extensions aim to standardize router-side monitoring of RPKI within BMP, focusing specifically on RPKI's effect on BGP routing decisions while maintaining a clear scope boundary with other monitoring mechanisms such as YANG modeling and streaming telemetry for RPKI-to-Router (RTR) protocol operations.

### A YANG Data Model for BMP
Draft: draft-ietf-grow-bmp-yang · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-yang/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-yang/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-06-a-yang-data-model-for-bmp-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
This document defines a YANG data model for the configuration and monitoring of the BGP Monitoring Protocol (BMP).

### Filtering Adj-Rib-In and Adj-Rib-Out to BMP receivers
Draft: draft-ietf-grow-bmp-adj-ribs-filtered · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-07-filtering-adj-rib-in-and-adj-rib-out-to-bmp-receivers-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
Filtering RIBs in BMP (BGP Monitoring Protocol) can be desirable for several use-cases like, for example, limiting the amount of data a collector station has to process or allow a sender to export only a certain afi/safi of interest. This document defines an indicator to inform a collector station that a Adj-Rib-In or Adj-Rib-Out data feed is being filtered at the BMP exporter. This document updates RFC 7854.

### BMP Loc-RIB: Peer address
Draft: draft-ietf-grow-bmp-loc-peer · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-loc-peer/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-loc-peer/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-08-09-bmp-loc-rib-peer-address-bmp-local-path-id-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
BMP Loc-RIB [RFC9069] enforces that the BMP router sets the Peer Address value of a path information to zero. This document introduces the option to communicate the actual peer from which a path was received when advertising that path with BMP Loc-RIB.

### BMP Local Path-ID
Draft: draft-younsi-grow-local-path-id · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-younsi-grow-local-path-id/
page: https://datatracker.ietf.org/doc/draft-younsi-grow-local-path-id/ | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
Intelligence is required to track BGP paths throughout the various RIBs and VRFs of a routing platform, due to potential attribute modifications and the use of BGP multipath. This document introduces the option to identify a path within a router in order to ease correlation in monitoring. A BMPv4 TLV is defined in order to communicate this locally significant identifier in monitoring messages.

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-10-bmp-v4-extended-tlv-support-for-bgp-monitoring-protocol-bmp-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
Most of the BGP Monitoring Protocol (BMP) message types make provision for data in Type, Length, Value (TLV) format. However, Route Monitoring messages (which provide a snapshot of the monitored Routing Information Base) Stats Reports (which supply periodical counters) and Peer Down messages (which indicate that a peering session was terminated) do not. Supporting (optional) data in TLV format across all BMP message types provides consistent and extensible structures that would be useful in the various use cases where conveying additional data to a monitoring station is required. This document updates RFC 7854 [RFC7854] to support TLV data in all message types and defines some essential TLVs. Additionally, this document introduces support for enterprise- specific TLVs in the BGP Monitoring Protocol by defining an Enterprise Bit (E-bit) that allows usage of per-vendor Type values.

### EVPN-Specific BMP RIB Statistics Extensions
Draft: draft-saum-grow-bmp-afi-safi-evpn · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/
page: https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/ | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
This document defines new EVPN-specific BGP Monitoring Protocol (BMP) statistics types. These extensions include scalar counters for EVPN route types specifically, while also keeping scope for defining counters which are EVPN route-type agnostic but related to BGP-EVPN RIB like, number of multihoming Ethernet Segments, number of multihomed EVIs, number of aliased paths, number of dynamic inter-VRF route leaking (IVRL). This revision (-06) firms up the specification for working group consideration: it adds a Relationship to Other Work section that explicitly maps this document to concurrently circulating GROW contributions on BMP statistics and TLV extensions and invites coordination with their authors, corrects the YANG alignment reference, strengthens Security Considerations, and adds a worked example. No statistics semantics, Stat Type/Subtype allocations, or wire formats defined in -05 are changed.

### BMP Route Change Statistics Based on Routing Policy
Draft: draft-smc-grow-bmp-route-change-stats · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/
page: https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/ | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
This document defines few generic BGP Monitoring Protocol (BMP) statistics for monitoring route modifications or changes due to applying Routing Policy. These statistics are reported per BGP peer using the BMP Statistics Report message. This revision (-02) firms up the specification for working group consideration: it adds a Relationship to Other Work section that explicitly maps this document to concurrently circulating GROW contributions on BMP statistics and policy-driven telemetry and invites coordination with their authors, adds a worked example, and strengthens Security Considerations. No statistics semantics, Stat Type allocations, or wire formats defined in -01 are changed.

### Route-Distinguisher-Scoped BMP RIB Statistics
Draft: draft-dikshit-grow-bmp-rd-scoped-rib-stats · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-dikshit-grow-bmp-rd-scoped-rib-stats/
page: https://datatracker.ietf.org/doc/draft-dikshit-grow-bmp-rd-scoped-rib-stats/ | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
[RFC7854] defines the BGP Monitoring Protocol (BMP) and its Statistics Report message. [I-D.ietf-grow-bmp-bgp-rib-stats] (published as [RFC9972]) extended that message with a set of advanced, per-AFI/SAFI BGP RIB statistics types. Several ongoing individual contributions independently define additional per- address-family, per-instance, or per-Route-Distinguisher (RD) statistics on top of that base (for example, EVPN-specific RIB statistics and VRF Loc-RIB monitoring enhancements), each proposing its own ad hoc Stat Data encoding. This document defines a single, address-family-agnostic Stat Data container -- the "RD-Scoped Statistics" format -- for BMP statistics that are naturally scoped below the per-AFI/SAFI level, to a specific Route Distinguisher (VRF instance, EVPN Instance, MVPN instance, or equivalent). Address-family-specific documents, such as EVPN- specific BMP RIB statistics, are expected to become thin "profiles" of this container rather than defining their own wire format, reducing duplication and Stat Type registry fragmentation across the GROW working group's BMP statistics work.

### Three BMP Statistics Drafts, One Shared Problem
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-grow-11-three-bmp-statistics-drafts-one-shared-problem-00 | video: https://youtu.be/M6qMXffo7i0 | materials: https://datatracker.ietf.org/meeting/127/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

## Working Group: httpbis

### Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-resumable-uploads-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Secondary Certificate Authentication of HTTP servers
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-secondary-certificate-authentication-of-http-servers-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP Signature Keys
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-http-signature-keys-01 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Redirect-By
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-redirect-by-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### 402 (Payment Required)
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-402-payment-required-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Parallel Appends for Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-parallel-appends-for-resumable-uploads-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Authenticating HTTP Tunnels with HTTP Message Signatures
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-authenticating-http-tunnels-with-http-message-signatures-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Unbound DATA - if time allows
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-httpbis-unbound-data-if-time-allows-00 | video: https://youtu.be/ePj9ZNp8f8s | materials: https://datatracker.ietf.org/meeting/127/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

## Working Group: idr

### A Border Gateway Protocol 4 (BGP-4)
Draft: draft-ietf-idr-bgp4-rfc4271bis · Working group: idr
Agenda: draft-ietf-idr-bgp4-rfc4271bis-05
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/ | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document discusses the Border Gateway Protocol (BGP), which is an inter-Autonomous System routing protocol. The primary function of a BGP-speaking system is to exchange network reachability information with other BGP systems. This network reachability information includes information on the list of Autonomous Systems (ASes) that reachability information traverses. This information is sufficient for constructing a graph of AS connectivity for this reachability from which routing loops may be pruned, and, at the AS level, some policy decisions may be enforced. BGP-4 provides a set of mechanisms for supporting Classless Inter- Domain Routing (CIDR). These mechanisms include support for advertising a set of destinations as an IP prefix, and eliminating the concept of network "class" within BGP. BGP-4 also introduces mechanisms that allow aggregation of routes, including aggregation of AS paths. This document obsoletes RFC 4271 and many other RFCs. It updates RFC 7606, RFC 7607 and RFC 9774 by subsuming their functionality as relates to RFC 4271.

### BGP over TLS/TCP
Draft: draft-wirtgen-bgp-tls · Working group: idr
Agenda: draft-wirtgen-bgp-tls-05
page: https://datatracker.ietf.org/doc/draft-wirtgen-bgp-tls/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-2-bgp-over-tlstcp-00 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document specifies the use of TLS over TCP to support BGP. The Border Gateway Protocol (BGP) relies on TCP to establish sessions between routers. While the TCP Authentication Option (TCP-AO) provides transport-layer integrity protection against spoofing and reset attacks, it does not provide confidentiality, cryptographic peer identity, or scalable key management. This document specifies a method for establishing a secure BGP session by running BGP over a TLS 1.3 session. The underlying TCP transport MUST be protected using TCP-AO. An "Implicit TLS" model on TCP port 179 is specified as the preferred mechanism.

### BGP Signaling of MASQUE Tunnel Encapsulation
Draft: draft-rosomakho-idr-bgp-masque-tunnel · Working group: idr
Agenda: draft-rosomakho-idr-bgp-masque-tunnel-01
page: https://datatracker.ietf.org/doc/draft-rosomakho-idr-bgp-masque-tunnel/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-3-bgp-signaling-of-masque-tunnel-encapsulation-00 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines BGP Tunnel Encapsulation Attribute tunnel types for MASQUE CONNECT-TCP, CONNECT-UDP, CONNECT-IP, and CONNECT- ETHERNET. It also defines URI Template and SVCB Parameters Sub-TLVs for advertising the MASQUE proxy endpoint, the HTTP request target template, and extensible connection parameters used to establish the corresponding MASQUE tunnel.

### BGP RR Deployment Considerations
Draft: draft-smith-idr-rr-deployment-considerations · Working group: idr
Agenda: draft-smith-idr-rr-deployment-considerations-01
page: https://datatracker.ietf.org/doc/draft-smith-idr-rr-deployment-considerations/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-4-bgp-rr-deployment-considerations-00 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
In BGP networks, Route Reflectors (RRs) simplify the provisioning of the Internal BGP (IBGP) control plane and mitigate the scaling challenges of maintaining a full mesh of IBGP sessions among border routers. Because of these operational benefits, RRs are widely deployed in modern networks utilizing BGP. This document describes common RR design options, their associated trade-offs, and deployment best practices based on industry operational experience. Operators should consider these suggestions when designing and operating BGP networks because BGP control plane stability is essential to overall network stability.

### BGP best path next-hop selection enhancements
Draft: draft-ietf-idr-bgp-bestpath-nh-selection · Working group: idr
Agenda: draft-ietf-idr-bgp-bestpath-nh-selection-00
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-bestpath-nh-selection/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-5-2-bgp-best-path-next-hop-selection-enhancements-00 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
BGP [RFC4271] has originally been designed to carry IPv4 routing information over the Internet. IP routing being "hop-by-hop" in nature, NEXT_HOP which purpose is to carry the address of the next router to send the IP packet to. In BGP, the next-hop may not be a directly connected router, hence, when evaluating paths, a BGP speaker must determine if the next-hop is resolvable and, if so, determine the internal cost to reach it. The incremental use of tunneling technologies to carry traffic between routers (e.g.: GRE, MPLS, SR-MPLS, SRv6...) may violate the assumption that the address carried in the NEXT_HOP is representative of the actual forwarding next-hop. These technologies decouple the BGP control-plane's view of the next-hop from the data-plane's actual forwarding endpoint. This document describes the problems that arise from this decoupling. These problems include sub-optimal path selection, incorrect resolvability tracking of the forwarding path leading to traffic drop or misrouting, and others. This document specifies how BGP obtains resolvability, preference, metric, and tracking information from resolution of the forwarding path and uses those values as inputs to BGP path selection.

### SD-WAN Edge and Underlay Tunnel Discovery Using BGP
Draft: draft-ietf-idr-sdwan-edge-discovery · Working group: idr
Agenda: draft-ietf-idr-sdwan-edge-discovery-32
page: https://datatracker.ietf.org/doc/draft-ietf-idr-sdwan-edge-discovery/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-6-sd-wan-edge-and-underlay-tunnel-discovery-using-bgp-00 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document specifies BGP mechanisms for SD-WAN (Software-Defined Wide Area Network) edge node attribute discovery. These mechanisms comprise a new tunnel type and associated Sub-TLVs for the BGP Tunnel Encapsulation Attribute, and a new Subsequent Address Family Identifier (SAFI) carrying a typed NLRI for advertising SD-WAN underlay tunnel information.

### Strict Only to Customer (OTC) Verification on Route Server Sessions
Draft: draft-herdes-idr-otc-rs-verification · Working group: idr
Agenda: draft-herdes-idr-otc-rs-verification-01
page: https://datatracker.ietf.org/doc/draft-herdes-idr-otc-rs-verification/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-7-strict-only-to-customer-otc-verification-on-route-server-sessions-00 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
RFC 9234 specifies how an AS receiving a route from a lateral Peer can check if a route was leaked, but doesn't specify any checks for routes received from a Route Server (RS). This makes the quality of filtering dependent on whether the RS implements RFC 9234. This document updates RFC 9234 by adding a complementary ingress check by an RS-Client.

### BGP Unreachable Prefix Announcement (UPA)
Draft: draft-krierhorn-idr-upa · Working group: idr
Agenda: draft-krierhorn-idr-upa-03
page: https://datatracker.ietf.org/doc/draft-krierhorn-idr-upa/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-1-bgp-unreachable-prefix-announcement-upa-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
Summarization is often used in multi-domain networks to improve network efficiency and scalability. With summarization in place, there is a need to signal loss of reachability to an individual prefix covered by the summary. This enables fast convergence by steering traffic away from the node which owns the prefix and is no longer reachable. This document specifies the mechanism, referred to as Unreachable Prefix Announcement (UPA), for networks where BGP is used to carry summary routes. It is also equally beneficial for operators to share the unreachable prefixes.

### BGP Extension for 5G Edge Service Metadata
Draft: draft-ietf-idr-5g-edge-service-metadata · Working group: idr
Agenda: draft-ietf-idr-5g-edge-service-metadata-34
page: https://datatracker.ietf.org/doc/draft-ietf-idr-5g-edge-service-metadata/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-2-bgp-extension-for-5g-edge-service-metadata-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
This draft describes a new Edge Metadata Path Attribute and some Sub- TLVs for egress routers to advertise the Edge Metadata about the attached edge services (ES). The edge service Metadata can be used by the ingress routers in the 5G Local Data Network to make path selections not only based on the routing cost but also the running environment of the edge services. The goal is to improve latency and performance for 5G edge services. The extension enables an edge service at one specific location to be more preferred than the others with the same IP address (ANYCAST) to receive data flow from a specific source, like a specific User Equipment (UE).

### BGP Extended Community for Identifying the Target Nodes
Draft: draft-ietf-idr-node-target-ext-comm · Working group: idr
Agenda: draft-ietf-idr-node-target-ext-comm-04
page: https://datatracker.ietf.org/doc/draft-ietf-idr-node-target-ext-comm/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-3-bgp-extended-community-for-identifying-the-target-nodes-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
BGP has been used to distribute different types of routing and policy information. In some cases, the information distributed may be only intended for one or a particular group of BGP nodes in the network. Currently BGP does not have a generic mechanism to designate the target nodes of the routing information. This document defines a new type of BGP Extended Community called "Node Target" for this purpose.

### Advertisement of SR Policy Operational States using BGP Link-State
Draft: draft-ietf-idr-bgp-ls-sr-policy-admin-flags · Working group: idr
Agenda: draft-ietf-idr-bgp-ls-sr-policy-admin-flags
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-sr-policy-admin-flags/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-4-advertisement-of-sr-policy-operational-states-using-bgp-link-state-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines the extension of BGP Link-State to advertise the operational state of the candidate path or segment list, facilitating the operation and maintenance of the SR Policy.

### BGP CT - Adaptation to SRv6 and Other dataplanes
Draft: draft-ietf-idr-bgp-ct-srv6 · Working group: idr
Agenda: draft-ietf-idr-bgp-ct-srv6-08
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ct-srv6/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-5-bgp-ct-adaptation-for-srv6-and-other-data-planes-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document specifies how the mechanisms for "Intent Driven Service Mapping" defined in [RFC9832] are applied to non-MPLS dataplanes. The extensions needed for SRv6 dataplane operations are specified. Base procedures of BGP CT are followed unaltered. Illustration of how BGP CT procedures work in SRv6 dataplane is provided in this document.

### BGP MultiNexthop Attribute
Draft: draft-ietf-idr-multinexthop-attribute · Working group: idr
Agenda: draft-ietf-idr-multinexthop-attribute
page: https://datatracker.ietf.org/doc/draft-ietf-idr-multinexthop-attribute/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-6-bgp-multinexthop-attribute-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
Today, a BGP speaker can advertise one nexthop for a set of NLRIs in an Update message. This nexthop can be encoded in either the top- level BGP-Nexthop attribute (code 3), or inside the MP_REACH_NLRI attribute (code 14). Forwarding information related to the nexthop is scattered across various attributes, extended communities or the NLRI field. This document defines a new optional non-transitive BGP attribute called "MultiNexthop (MNH)" with IANA code TBD. The MNH provides two things: it allows carrying the Nexthop and related forwarding information in one BGP attribute. The MNH also enables carrying an ordered set of multiple Nexthops in the same attribute, with forwarding information scoped on a per Nexthop basis.

### Origin-Leaf Identification in Data-Center eBGP Underlays using BGP Large Communities
Draft: draft-brissette-idr-dc-origin-leaf-id · Working group: idr
Agenda: draft-brissette-idr-dc-origin-leaf-id-00
page: https://datatracker.ietf.org/doc/draft-brissette-idr-dc-origin-leaf-id/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-7-origin-leaf-identification-in-data-center-ebgp-underlays-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
Data-center fabrics that run hop-by-hop eBGP routing frequently need to identify the originating node (leaf) of a prefix as it is propagated through the fabric. The BGP AS_PATH attribute provides loop prevention and identifies the originating Autonomous System (AS), but under common AS numbering models an AS does not map to a single leaf. While several BGP community mechanisms could carry such an identifier, there is no documented practice describing the mechanism and encoding choices for underlay origin-leaf tagging. This document analyzes the problem, states the requirements, and surveys candidate BGP mechanisms for carrying an origin-leaf identifier. It recommends encoding the identifier in a BGP Large Community (RFC 8092), describes how the identifier is allocated within the Large Community namespace, and describes how it is originated, propagated unchanged across the fabric, and consumed at receiving leaves. It also describes an optional profile for locally significant route-attachment metadata. This document is Informational and defines no new protocol elements.

### BGP Extension for Distributing CP Threshold Constraints of SR Policy
Draft: draft-liu-idr-bgp-sr-policy-cp-threshold · Working group: idr
Agenda: draft-liu-idr-bgp-sr-policy-cp-threshold-03
page: https://datatracker.ietf.org/doc/draft-liu-idr-bgp-sr-policy-cp-threshold/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-8-bgp-extension-for-distributing-cp-threshold-constraints-of-sr-policy-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines the extension of BGP to distribute the threshold constraint parameters of candidate paths for SR Policy to achieve flexible path selection.

### BGP-LS Advertisement of SR Policy Performance Metric
Draft: draft-lin-idr-bgpls-te-policy-pm · Working group: idr
Agenda: draft-lin-idr-bgpls-te-policy-pm-10
page: https://datatracker.ietf.org/doc/draft-lin-idr-bgpls-te-policy-pm/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-9-bgp-ls-advertisement-of-sr-policy-performance-metric-00 | video: https://youtu.be/S3NPP_SmEV8 | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document describes a way to advertise the performance metrics for Traffic Engineering (TE) Policy using BGP Link State (BGP-LS).

### BGP Flow Specification Version 2 - for Basic IP
Draft: draft-ietf-idr-fsv2-ip-basic · Working group: idr
Agenda: draft-ietf-idr-fsv2-ip-basic-10
page: https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-1-bgp-flow-specification-version-2-for-basic-ip-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC 8956, and RFC 9117, describes the distribution of traffic filter policy (traffic filters and actions) distributed via BGP. During the deployment of BGP FSv1 a number of issues were detected, so version 2 of the BGP flow specification (FSv2) protocol addresses these issues. In order to provide a clear demarcation between FSv1 and FSv2, a different NLRI encapsulates FSv2. The IDR WG requires two implementation. Early feedback on implementations of FSv2 indicate that FSv2 has a correct design direction, but that breaking FSv2 into a progression of documents would aid deployment of the draft (basic and adding user ordered actions). This document specifies the basic FSv2 NLRI with user ordering of filters added to FSv1 IP Filters and FSv2 actions.

### BGP Flow Specification Version 2 - More IP Actions
Draft: draft-hares-idr-fsv2-more-ip-actions · Working group: idr
Agenda: draft-hares-idr-fsv2-more-ip-actions-04
page: https://datatracker.ietf.org/doc/draft-hares-idr-fsv2-more-ip-actions/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-2-bgp-flow-specification-version-2-more-ip-actions-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
The BGP flow specification version 2 (FSv2) for Basic IP defines user ordering of filters along with FSv1 IP Filters and FSv2 actions in Extended Communites. This draft suggests a method of encoding user ordered actions in a community attribute in BGP.

### BGP Flow-Spec Traffic Compress Action
Draft: draft-shen-idr-flowspec-traffic-compress-action · Working group: idr
Agenda: draft-shen-idr-flowspec-traffic-compress-action-05
page: https://datatracker.ietf.org/doc/draft-shen-idr-flowspec-traffic-compress-action/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-3-bgp-flow-spec-traffic-compress-action-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
BGP Flow Specification Version 2 (FSv2) provides an extensible framework for disseminating traffic flow specification rules and associated actions. While traditional Flow-spec actions cover rate- limiting, redirecting, and marking, emerging applications require dynamic bandwidth optimization. This document specifies a new traffic filtering action to support selective, on-demand traffic compression across network domains using BGP Extended Communities aligned with the FSv2 architecture.

### A YANG Data Model for Flow Specification
Draft: draft-wu-idr-flowspec-yang-cfg · Working group: idr
Agenda: draft-wu-idr-flowspec-yang-cfg-04
page: https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-yang-cfg/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-4-flow-specification-yang-modules-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines a YANG data model for Flow Specification implementations. The data model includes configuration data and state data.

### YANG Model for BGP Flow Specification
Draft: draft-lin-idr-bgp-flowspec-yang · Working group: idr
Agenda: draft-lin-idr-bgp-flowspec-yang-00
page: https://datatracker.ietf.org/doc/draft-lin-idr-bgp-flowspec-yang/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-5-yang-model-for-bgp-segment-routing-policy-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines a YANG data model for the BGP Flow Specification (Flowspec) address families. The model augments the BGP YANG model to add all Flow Specification address families, including Flowspec-specific configuration, the Flow Specification RIB, and per-neighbor Adj-RIBs, and defines notifications for the prefix limit exceeded and route state change events.

### YANG Model for BGP Segment Routing Policy
Draft: draft-lin-idr-bgp-sr-policy-yang · Working group: idr
Agenda: draft-lin-idr-bgp-sr-policy-yang-00
page: https://datatracker.ietf.org/doc/draft-lin-idr-bgp-sr-policy-yang/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-6-a-yang-data-model-for-bgp-ls-segment-routing-policy-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines a YANG data model for the BGP Segment Routing (SR) Policy address families (RFC 9830). The model augments the BGP YANG model to add the IPv4 SR Policy (AFI, SAFI = 1, 73) and IPv6 SR Policy (AFI, SAFI = 2, 73) address families, including SR Policy- specific configuration, the SR Policy RIB, per-neighbor Adj-RIBs, the decoded SR Policy candidate path information, such as preference, Binding SID, and segment lists, and defines notifications for the prefix limit exceeded and candidate path state change events.

### A YANG Data Model for BGP-LS Segment Routing Policy
Draft: draft-aravind-idr-bgp-ls-sr-policy-yang · Working group: idr
Agenda: draft-aravind-idr-bgp-ls-sr-policy-yang-00
page: https://datatracker.ietf.org/doc/draft-aravind-idr-bgp-ls-sr-policy-yang/ | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines a YANG data model for the operational state of Segment Routing (SR) Policy candidate paths that are advertised using BGP - Link State (BGP-LS). The model augments the read-only BGP-LS Link-State Database with the SR Policy Candidate Path Network Layer Reachability Information (NLRI) and the associated BGP-LS Attribute TLVs specified in RFC 9857.

### BGP Extended Communities for SR Policy Performance Metrics
Draft: draft-he-idr-bgp-ec-sr-pm · Working group: idr
Agenda: draft-he-idr-bgp-ec-sr-pm-01
page: https://datatracker.ietf.org/doc/draft-he-idr-bgp-ec-sr-pm/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-7-bgp-extended-communities-for-sr-policy-performance-metrics-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
Traffic scheduling and optimization have become routine network operation and maintenance tasks for operators. The operators need to select a path that can meet the Qality of Service (QoS) reqiurements of the traffic to be scheduled. This document defines four BGP extended communities for Segment Routing (SR) candidate path performance metric: the Available Bandwidth Extended Community, the Unidirectional Delay Extended Community, the Unidirectional Delay Variation Extended Community and the Unidirectional Loss Extended Community, which carry SR Policy candidate path performance parameters for the operators to select a preferred path for traffic scheduling and optimization. It also specifies the format and processing rules for these extended community types.

### BGP node-ID EC extension
Draft: draft-qwz-idr-nodeid-ec · Working group: idr
Agenda: draft-qwz-idr-nodeid-ec-00
page: https://datatracker.ietf.org/doc/draft-qwz-idr-nodeid-ec/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-8-bgp-node-id-ec-extension-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document describes a new BGP extended community attribute for advertising the node-ID.

### Path Attribute Outbound Route Filter (PA-ORF) for BGP-4
Draft: draft-wang-idr-path-attribute-orf · Working group: idr
Agenda: draft-wang-idr-path-attribute-orf-00
page: https://datatracker.ietf.org/doc/draft-wang-idr-path-attribute-orf/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-9-path-attribute-outbound-route-filter-pa-orf-for-bgp-4-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
This document defines a family of Outbound Route Filter (ORF) Types for controlling the propagation of BGP Path Attributes. The Path Attribute ORFs (PA-ORFs) enable a BGP speaker to dynamically request that a peer suppress, remove, refine, or constrain the propagation of selected BGP Path Attributes when constructing outbound UPDATE messages for a given AFI/SAFI. This document defines four ORF Types: Path Attribute Type ORF; Path Attribute Subtype ORF; Unknown Path Attribute ORF; and Path Attribute Propagation Scope ORF. These ORF Types reuse the ORF Capability and ROUTE-REFRESH procedures defined in [RFC5291]. No new BGP Path Attribute or BGP message type is introduced. PA-ORFs are intended to reduce unintended propagation of BGP Path Attributes, especially Optional Transitive attributes whose semantics are valid only within a limited administrative, service, or technology domain.

### Source-Directed Propagation of VPN Prefix ORF for BGP-4
Draft: draft-wang-idr-vpn-prefix-orf-propagation · Working group: idr
Agenda: draft-wang-idr-vpn-prefix-orf-propagation-00
page: https://datatracker.ietf.org/doc/draft-wang-idr-vpn-prefix-orf-propagation/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessc-3-10-source-directed-propagation-of-vpn-prefix-orf-for-bgp-4-00 | video: https://youtu.be/U4-J8t6Jqpk | materials: https://datatracker.ietf.org/meeting/127/session/idr
The Virtual Private Network (VPN) Prefix Outbound Route Filter (ORF) [I-D.ietf-idr-vpn-prefix-orf] mechanism allows a Border Gateway Protocol (BGP) speaker to request that an adjacent peer filter matching VPN routes. In deployments using Route Reflectors (RRs) or Autonomous System Border Routers (ASBRs), the adjacent peer may not be the source of the affected routes. This document specifies when an intermediate router may send an ordinary VPN Prefix ORF to the upstream peer from which the affected routes were received. Upstream transmission is permitted only after the intermediate router determines that no relevant downstream router requires the affected routes. This document also defines an Interest Query/Response procedure for making that determination.

### 1. RFC4271bis Update
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-1-rfc4271bis-update-01 | video: https://youtu.be/SNsb8blw0BY | materials: https://datatracker.ietf.org/meeting/127/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

## Working Group: lsr

### IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)
Draft: draft-ietf-lsr-pcpps · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ietf-lsr-pcpps/
page: https://datatracker.ietf.org/doc/draft-ietf-lsr-pcpps/ | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
[I-D.many-teas-power-steering] introduces a Power Conserving Path Placement Strategy (PCPPS). When possible, PCPPS concentrates traffic onto a small set of network resources. When traffic is concentrated onto a small set of network resources, other network resources become idle and can be powered down until they are needed again. This conserves energy and reduces environmental impact. PCPPS uses information that is distributed by an IGP. This document specifies the IS-IS encoding for that information.

### Advertising IGP Active Measurement Groups in Router Capabilities
Draft: draft-admnr-lsr-igp-measurement-group · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/
page: https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/ | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
This document defines IGP capability advertisements for measurement group membership for Active Measurement Protocols (AMPs) such as TWAMP and STAMP. An IS-IS capability sub-TLV is defined for IS-IS and an OSPF Router Information (RI) LSA TLV is defined for OSPFv2 and OSPFv3. The mechanism allows IGP routers to discover other routers participating in different measurement groups, enabling automatic discovery of measurement endpoints throughout an IS-IS or OSPF routing domain. The solution uses a Group ID to identify measurement group membership, where the same interface address (IPv4 or IPv6) may be used for multiple measurement groups. A corresponding BGP - Link State (BGP-LS) node-level attribute is defined to distribute measurement group membership beyond a single IGP domain.

### Deprecation of the IPsec Authentication Header (AH) for OSPFv3 Authentication
Draft: draft-acee-lsr-ospfv3-deprecate-ah · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-acee-lsr-ospfv3-deprecate-ah/
page: https://datatracker.ietf.org/doc/draft-acee-lsr-ospfv3-deprecate-ah/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-ospfv3-deprecate-ipsec-ah-04 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
RFC 4552 specifies the use of the IPsec Authentication Header (AH) and the Encapsulating Security Payload (ESP) to provide authentication and confidentiality for OSPFv3. This document deprecates the use of AH for OSPFv3 and updates RFC 4552 accordingly. Operators are encouraged to use either ESP with NULL encryption, as specified in RFC 4552, or the OSPFv3 Authentication Trailer, as specified in RFC 7166.

### IS-IS Hello Capability
Draft: draft-ginsberg-lsr-hello-capability · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ginsberg-lsr-hello-capability/
page: https://datatracker.ietf.org/doc/draft-ginsberg-lsr-hello-capability/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-05-hello-capability-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Advertisement of capabilities in Hellos is useful to allow support of optional features in establishing and maintaining adjacencies. This document defines a new TLV to be sent in hellos to advertise such capabilities.

### IS-IS Reliable SNP
Draft: draft-ginsberg-lsr-reliable-snp · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ginsberg-lsr-reliable-snp/
page: https://datatracker.ietf.org/doc/draft-ginsberg-lsr-reliable-snp/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-06-reliable-snp-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Complete Sequence Number PDUs (CSNPs) are exchanged as part of adjacency bringup on point-to-point interfaces. However, this exchange is unreliable. This document defines protocol extensions to support reliable exchange of CSNPs as well as optimizations to the encoding of advertisements in Sequence Number PDUs.

### Retransmission Indication for IS-IS Fast Flooding
Draft: draft-przygienda-lsr-fast-flooding-rtx-indication · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-przygienda-lsr-fast-flooding-rtx-indication/
page: https://datatracker.ietf.org/doc/draft-przygienda-lsr-fast-flooding-rtx-indication/ | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
[RFC9681] defines a Flooding Parameters TLV. Among other things, it lets an IS-IS node advertise two values to a neighbor. The Receive Window (RWIN) bounds the number of unacknowledged Link State PDUs (LSPs) the neighbor may have outstanding. The LSPs-per-PSNP (LPP) threshold triggers immediate acknowledgment. Together they form a credit-based flow-control window and an acknowledgment cadence. These are the parts of [RFC9681] that are most important, most useful, and most likely to be implemented at scale. The sender-side congestion-control algorithms in that document are described only as optional, local choices. No single algorithm is mandatory. A credit-based window alone does not signal congestion. As long as acknowledgments keep freeing credit, a sender may keep refilling the window up to RWIN. It does so even while it is actively retransmitting LSPs on that adjacency. Without an explicit, normatively specified reaction to observed retransmission, fast flooding at scale can degenerate into sustained retransmission storms that serve only to keep the window full. This document specifies a local backoff. A node reduces the effective outstanding-LSP ceiling it uses against a neighbor's advertised RWIN by a meaningful fraction. The trigger is a count of LSP retransmissions generated toward that neighbor within a trailing time window exceeding a threshold. This backoff applies unconditionally. It does not depend on whether the condition is signaled to the neighbor, or understood by it. This document also defines a lightweight Retransmission (RTX) indication. It is a new flag in the existing Flags sub-TLV of the Flooding Parameters TLV. A node advertises it to a neighbor while it is retransmitting LSPs toward that neighbor. The flag reports only the advertising node's own retransmissions, that is, its own congestion. A node never sets it in reaction to a neighbor's flag. The flag lets the neighbor adjust its own advertised RWIN in turn. The adjacency then converges toward a stable operating point at the highest speed it can sustain. Neither side needs prior knowledge of the other's characteristics or of the link. This document further clarifies how concurrent versions of the same LSP fragment are counted against RWIN, LPP, and the retransmission threshold. [RFC9681] leaves that case undefined, and it arises routinely at fast flooding rates.

### IS-IS Aggregated SNP Hash Packets
Draft: draft-prz-lsr-ash-packets · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/
page: https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/ | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
The document presents an optional new type of database synchronization packet called an Aggregated SNP Hash (ASH). When feasible, it compresses traditional SNP exchanges into a dynamic Merkle tree-like structure, which speeds up synchronization of large databases and adjacency numbers while reducing the load from regular CSNP exchanges during normal operation. Just like CSNPs and PSNPs, ASH packets come in two flavors, called Complete ASH (CASH) and Partial ASH (PASH). ASH also provides a graceful restart architecture that addresses scaling limitations by distributing recovery work among helpers under the restarting router's orchestration.

### IS-IS Originating Generation Identifier (OGID) TLV
Draft: draft-asw-lsr-isis-ogid · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-asw-lsr-isis-ogid/
page: https://datatracker.ietf.org/doc/draft-asw-lsr-isis-ogid/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-09-isis-ogid-01 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
This document introduces a new top-level TLV in IS-IS, the Originating Generation Identifier (OGID) TLV, which is carried in every Link State PDU (LSP) fragment originated by a node. The OGID identifies the logical transaction to which a set of LSP fragment updates belongs. When accompanied by a Fragment Count greater than one, it additionally allows a receiving node to determine when all fragments participating in that transaction have been received. This enables receivers to process multi-fragment updates atomically, avoiding the transient Link State Database (LSDB) inconsistencies that can otherwise occur when logically related LSP fragment updates are flooded and processed independently.

### IS-IS Database Fingerprinting
Draft: draft-westphal-lsr-isis-database-checksumming · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-westphal-lsr-isis-database-checksumming/
page: https://datatracker.ietf.org/doc/draft-westphal-lsr-isis-database-checksumming/ | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
In large IS-IS networks it is useful to quickly verify whether the link-state databases on all routers have synchronized properly and to derive a rough metric of flooding diffusion behavior. This document proposes a lightweight database fingerprinting mechanism for IS-IS along with YANG model extensions providing easy access to such information. For fast verification against a peer, an optional TLV carrying the database fingerprint is defined for inclusion in IIH and CSNP PDUs.

### Detection of Router-ID Conflicts in IGPs
Draft: draft-lg-lsr-router-id-conflict-detect · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-lg-lsr-router-id-conflict-detect/
page: https://datatracker.ietf.org/doc/draft-lg-lsr-router-id-conflict-detect/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-11-detection-of-router-id-conflicts-in-igps-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
In link-state Interior Gateway Protocols (IGPs) such as OSPF and IS- IS, the router ID (or system ID) serves as a unique identifier for routers within a routing domain. Duplicate router IDs can lead to severe network instability, including persistent Link State Advertisement (LSA/LSP) flooding, inconsistent Link State Databases (LSDBs), and permanent forwarding loops. This document defines mechanisms for detecting such conflicts between non-adjacent routers and proposes procedures to alert network operators, along with defining the corresponding YANG interface and event YANG notifications for OAM operations.

### Metric Normalize for IGP Flex-algo
Draft: draft-gl-lsr-metric-normalize · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/
page: https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-12-metric-normalize-for-igp-flex-algo-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
When multiple links in a network have the same metric, they can serve as ECMP equivalent links for load balancing during forwarding. However, slight fluctuations in metric values can prevent the formation of ECMP equivalent links, leading to the idle state of suboptimal links and thus wasting bandwidth resources. This document proposes a metric normalization method by advertising metric normalization parameters corresponding to a specific Metric- Type for Flexible Algorithm. During route calculation, slight fluctuations across multiple links are adjusted according to these normalization parameters, making the computed metric values more consistent. This approach enables the formation of ECMP equivalent links and promotes load sharing in the forwarding process.

### Export of IGP Algorithm Information in IPFIX
Draft: draft-liu-opsawg-ipfix-igp-algo · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-igp-algo/
page: https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-igp-algo/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-14-export-of-igp-algorithm-information-in-ipfix-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
This document introduces two IPFIX information elements (IEs) to identify the IGP Algorithm and Multi-Topology Identifier associated with the forwarding entry used for an observed packet.

### lsr-status
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-01-lsr-status-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### pcpps
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-02-pcpps-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### IGP Measurement Groups
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-igp-measurement-groups-01 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### Fast Flood RTX Indication
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-fast-flood-rtx-indication-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### ASH Update/ASH GR
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-ash-updateash-gr-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### DB Fingerprinting Update
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-lsr-db-fingerprinting-update-00 | video: https://youtu.be/UJOPXPHVgTY | materials: https://datatracker.ietf.org/meeting/127/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

## Working Group: masque

### QUIC-Aware Proxying Using HTTP
Draft: draft-ietf-masque-quic-proxy · Working group: masque
Agenda: draft-ietf-masque-quic-proxy by Eric Rosenberg (15 minutes)
page: https://datatracker.ietf.org/doc/draft-ietf-masque-quic-proxy/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-masque-quic-aware-proxying-using-http-00 | video: https://youtu.be/xc8lv9s8qUs | materials: https://datatracker.ietf.org/meeting/127/session/masque
This document extends UDP Proxying over HTTP to add optimizations for proxied QUIC connections. Specifically, it allows a proxy to reuse UDP 4-tuples for multiple proxied connections, and adds a mode of proxying in which QUIC short header packets can be forwarded and transformed through an HTTP/3 proxy rather than being fully re- encapsulated and re-encrypted.

### DNS and PREF64 Configuration for Proxying IP in HTTP
Draft: draft-ietf-masque-connect-ip-dns · Working group: masque
Agenda: draft-ietf-masque-connect-ip-dns by Yaroslav Rosomakho (15 minutes)
page: https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip-dns/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-masque-connect-ip-qlog-00 | video: https://youtu.be/xc8lv9s8qUs | materials: https://datatracker.ietf.org/meeting/127/session/masque
Proxying IP in HTTP allows building a VPN through HTTP load balancers. However, at the time of writing, that mechanism lacks a way to communicate network configuration details such as DNS information or IPv6 NAT64 prefixes (PREF64). In contrast, most existing VPN protocols provide mechanisms to exchange such configuration information. This document defines extensions that convey DNS and PREF64 configuration using HTTP capsules. This mechanism supports encrypted DNS transports and can be used to inform peers about network translation prefixes for IPv6/IPv4 synthesis.

### Extensions to Compress and Derive Fields in HTTP Datagrams
Draft: draft-ietf-masque-http-datagram-compression · Working group: masque
Agenda: draft-ietf-masque-http-datagram-compression by Yaroslav Rosomakho (15 minutes)
page: https://datatracker.ietf.org/doc/draft-ietf-masque-http-datagram-compression/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-masque-http-datagram-compression-00 | video: https://youtu.be/xc8lv9s8qUs | materials: https://datatracker.ietf.org/meeting/127/session/masque
This document defines extensions for HTTP Datagram-based protocols that improve transmission efficiency by introducing templates for compressing or deriving datagram fields. These templates allow endpoints to define parts of datagrams that are static and can be removed, and other parts that can be derived (such as packet lengths and checksum values). Additionally, this document defines a checksum offload procedure enabling receivers to complete Internet checksums using sender- provided partial values. These optimisations reduce per-packet overhead and processing cost. Compression can allow larger original packets to fit in QUIC DATAGRAM frames, depending on the applicable processing context and path maximum transmission unit (MTU).

### qlog Definitions for CONNECT-IP
Draft: draft-seemann-masque-connect-ip-qlog · Working group: masque
Agenda: draft-seemann-masque-connect-ip-qlog by Marten Seemann (10 minutes)
page: https://datatracker.ietf.org/doc/draft-seemann-masque-connect-ip-qlog/ | video: https://youtu.be/xc8lv9s8qUs | materials: https://datatracker.ietf.org/meeting/127/session/masque
This document defines qlog events for CONNECT-IP packet processing and representations for its capsules, including the DNS and PREF64 configuration extensions. It extends the HTTP event schema defined in the HTTP/3 qlog document.

### DNS and PREF64 Configuration
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-masque-dns-and-pref64-configuration-01 | video: https://youtu.be/xc8lv9s8qUs | materials: https://datatracker.ietf.org/meeting/127/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### QUIC-Aware Proxying and SCONE coexistence
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-masque-quic-aware-proxying-and-scone-coexistence-00 | video: https://youtu.be/xc8lv9s8qUs | materials: https://datatracker.ietf.org/meeting/127/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

## Working Group: netconf

### List Pagination for YANG-driven Protocols
Draft: draft-ietf-netconf-list-pagination · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-list-pagination-15
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-list-pagination-for-yang-driven-protocols-01 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
In some circumstances, instances of YANG modeled "list" and "leaf- list" nodes may contain numerous entries. Retrieval of all the entries can lead to inefficiencies in the server, the client, and the network in between. This document defines a model for list pagination that can be implemented by YANG-driven management protocols such as NETCONF and RESTCONF. The model supports paging over optionally filtered and/or sorted entries. The solution additionally enables servers to constrain query expressions on some "config false" lists or leaf- lists.

### NETCONF Extensions to Support List Pagination
Draft: draft-ietf-netconf-list-pagination-nc · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-list-pagination-nc-14
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-nc/ | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
This document defines a mapping of the list pagination mechanism defined in [I-D.ietf-netconf-list-pagination] to NETCONF [RFC6241]. This document updates [RFC6241], to augment the <get> and <get- config> "rpc" statements, and [RFC8526], to augment the <get-data> "rpc" statement, to define input parameters necessary for list pagination.

### RESTCONF Extensions to Support List Pagination
Draft: draft-ietf-netconf-list-pagination-rc · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-list-pagination-rc-13
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-list-pagination-rc/ | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
This document defines a mapping of the list pagination mechanism defined in [I-D.ietf-netconf-list-pagination] to RESTCONF [RFC8040]. This document updates RFC 8040, to declare "list" and "leaf-list" as valid resource targets for the RESTCONF GET operation, to define GET query parameters necessary for list pagination, and to define a media-type for XML-based lists.

### YANG Groupings for QUIC clients and QUIC servers
Draft: draft-ietf-netconf-quic-client-server · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-quic-client-server-09
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-client-server/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-2-yang-groupings-for-quic-clients-and-quic-servers-00 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
This document defines three YANG 1.1 modules to support the configuration of QUIC clients and QUIC servers. The common YANG module defines reusable groupings for setting parameters imported from the QUIC version and QUIC transport IANA YANG modules. The two QUIC client and server YANG modules define reusable groupings for QUIC connection settings, including the common QUIC parameters, for protocol implementation. Furthermore two initial YANG 1.1 modules for the IANA registries "QUIC Versions" and "QUIC Transport Parameters" are included in Appendix.

### Error List and Error Identities Registries for YANG-driven protocols
Draft: draft-ietf-netconf-error-registries · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-error-registries-01
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-error-registries/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-3-error-list-and-error-identities-registries-for-yang-driven-protocols-00 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
This document defines IANA registries for the YANG Protocol Error List and YANG Protocol Error Identities.

### NETCONF Call Home and RESTCONF Call Home Using QUIC
Draft: draft-ietf-netconf-quic-call-home · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-quic-call-home-02
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-quic-call-home/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-4-netconf-call-home-and-restconf-call-home-using-quic-02 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
This RFC extends NETCONF Call Home and RESTCONF Call Home [RFC 8071] to support the QUIC protocol [RFC 9000].

### YANG Datastore Telemetry (YANG Push version 2)
Draft: draft-ietf-netconf-yang-push-2 · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-netconf-yang-push-2-01
page: https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-push-2/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-5-yang-push-v2-00 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
YANG Push version 2 is a YANG datastore telemetry solution, as an alternative lightweight specification to the Subscribed Notifications and YANG Push solution, specifically optimized for the efficient observability of operational data.

### YANG path format (ypath)
Draft: draft-jgc-netmod-yang-path · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-jgc-netmod-yang-path-00
page: https://datatracker.ietf.org/doc/draft-jgc-netmod-yang-path/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-yang-path-format-ypath-00 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
This document defines ypath (YANG path), a single-line, self- describing path format for referencing nodes in YANG schema trees, YANG instance data, and data filters. A ypath identifies YANG nodes using module-qualified names and list key predicates. The format is closely related to the YANG instance-identifier built-in type but additionally supports schema paths, filter wildcards, regular expression key matching, key value sets, and path enumeration.

### Cross-Publisher Causal Ordering for YANG-Push Datastore Telemetry
Draft: draft-dikshit-netconf-yang-push-causal-ordering · Working group: netconf
Agenda: https://datatracker.ietf.org/doc/html/draft-dikshit-netconf-yang-push-causal-ordering-00
page: https://datatracker.ietf.org/doc/draft-dikshit-netconf-yang-push-causal-ordering/ | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
In YANG-Push version 2, each publisher numbers its own notifications, and the numbers of two publishers are not comparable. When a single subscription is served by several publishers, for example on a multi- line-card router or a disaggregated routing stack, a collector cannot order updates across those publishers from the sequence numbers alone. This document defines an opt-in, coordination-free mechanism that carries a Comparability Scope, a coarse Causal-Epoch, and a per- publisher Local-Sequence-Number in the notification envelope. Publishers stay lock-free on the export fast path, and a collector reconstructs cross-publisher order within a bounded reordering window. A companion YANG module adds the subscription controls, the envelope metadata, and the capability discovery. The mechanism does not require synchronized clocks across publishers.

### Comparable Sequence Numbers Across Publishers in YANG Datastore Telemetry
Presentation · Working group: netconf
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-7-comparable-sequence-numbers-across-publishers-in-yang-datastore-telemetry-01 | video: https://youtu.be/yFo-QPAxq_E | materials: https://datatracker.ietf.org/meeting/127/session/netconf
Slides presented at the netconf session; no Internet-Draft is linked to them.

## Working Group: netmod

### YANG Next Agreement
Draft: draft-ietf-netmod-yang-next-agreement · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-next-agreement/00/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-next-agreement/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-02-yang-next-agreement-01 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
The purpose of this document is to discuss and hopefully find agreement on the scope and shape of the next version of YANG.

### XML Encoding of Data Modeled with YANG
Draft: draft-ietf-netmod-yang-xml · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-xml/01/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-xml/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-03-xml-encoding-of-data-modeled-with-yang-00 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
This document defines encoding rules for representing YANG modeled configuration data, state data, parameters of Remote Procedure Call (RPC) operations or actions, and notifications defined using XML.

### The YANG 2.0 Data Modeling Language
Draft: draft-ietf-netmod-yang2 · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang2/01/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang2/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-04-the-yang-20-data-modeling-language-00 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
YANG is a data modeling language used to model configuration data, operational state data, Remote Procedure Calls, and notifications for network management protocols. This document describes the syntax and semantics of version 2.0 of the YANG language. YANG version 2.0 is a major release of the YANG language, addressing issues found in the original specification.

### YANG Packages
Draft: draft-ietf-netmod-yang-packages · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-packages/11/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-packages/ | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
This document defines YANG packages: versioned organizational structures used to manage the schema and conformance of a set of YANG modules as a cohesive unit.

### Guidance for Managing YANG Modules in RFCs and IANA Registries
Draft: draft-ietf-netmod-iana-yang-guidance · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-iana-yang-guidance/04/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-iana-yang-guidance/ | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
This document provides guidance to the RFC Editor and IANA on managing YANG modules in RFCs and IANA registries, ensuring consistent application of YANG Semantic Versioning rules.

### YANG Schema Comparison
Draft: draft-ietf-netmod-yang-schema-comparison · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-schema-comparison/10/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-schema-comparison/ | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
This document specifies an algorithm with two input variants for comparing revisions of a YANG schema to determine the scope of changes and produce a list of the changes between the revisions. The output of the algorithm can be used to help select an appropriate YANG semantic version number for a new YANG Module revision. It also specifies a YANG module for YANG-structured output of these algorithms, that can be easily consumed in a machine-readable way.

### YANG Schema Selection
Draft: draft-ietf-netmod-yang-ver-selection · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-ver-selection/00/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-ver-selection/ | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
This document defines a mechanism to allow clients, using NETCONF or RESTCONF, to configure and select YANG schema for interactions with a server. This functionality can help servers support clients using older revisions of YANG modules even if later revisions contain non- backwards-compatible changes. It can also be used to allow clients to select between YANG schema defined by different organizations. This draft provides a solution to YANG versioning requirements 3.1 and 3.2.

### YANG Configuration Templates
Draft: draft-ietf-netmod-yang-config-templates · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-config-templates/00/
page: https://datatracker.ietf.org/doc/draft-ietf-netmod-yang-config-templates/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-06-yang-configuration-templates-01 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
This document defines a YANG-based configuration template mechanism whereby repetitive configuration data can be factored out into templates and applied where needed. This avoids the redundant definition of identical configuration and ensures the consistency of it, thus allowing configuration data to be managed more conveniently and efficiently.

### Extending Normalized Forms to String-Derived Types
Draft: draft-fedyk-netmod-yang-normal-form · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-fedyk-netmod-yang-normal-form/01/
page: https://datatracker.ietf.org/doc/draft-fedyk-netmod-yang-normal-form/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-07-extending-normalized-forms-to-string-derived-types-00 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
YANG models frequently define identifiers using string or string- derived types whose lexical space permits multiple representations of the same underlying value. This can lead to incorrect behavior when semantically equivalent values are compared lexically. This document adds an optional extension to the existing YANG concept of normalized form to string-derived types whose lexical space permits multiple representations of the same underlying value.

### Validating anydata in YANG Library context
Draft: draft-netana-netmod-yang-anydata-validation · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-netana-netmod-yang-anydata-validation/00/
page: https://datatracker.ietf.org/doc/draft-netana-netmod-yang-anydata-validation/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-08-validating-anydata-in-yang-library-context-00 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
The YANG "anydata" statement carries data whose data model is not known when the module is designed. This document defines the context that is needed to validate such content: the schema context, the "anydata" node, a schema anchor, and the datastore. It describes how this context is obtained for the uses of "anydata" in IETF YANG modules, how the schema node of each node in the content is found, and which YANG constraints are checked.

### A YANG Extension for Declaring the Comparability Scope of Operational State
Draft: draft-dikshit-netmod-comparability-scope-extension · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/02/
page: https://datatracker.ietf.org/doc/draft-dikshit-netmod-comparability-scope-extension/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-10-a-yang-extension-for-comparability-scope-of-operational-state-01 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
A value exported from a YANG data tree is often unique only within its parent, for example an entry numbered 0 under two different parents. Once the value is exported without the parent's key, a collector cannot tell whether two such values refer to the same thing, and no collector-side normalization can recover the missing key. YANG (RFC 7950) has no way to state this dependency in the schema. This document defines a YANG extension statement, "csc:comparability-scope", a four-level scope lattice, a compatibility rule, and an export rule, so that the key needed to compare a value travels with it, and a schema-aware tool can detect an invalid comparison before any data is exported.

### Problem Statement: YANG Modeling for Protocol Buffer Based Network APIs
Draft: draft-ali-netmod-yang-protobuf-problem-statement · Working group: netmod
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ali-netmod-yang-protobuf-problem-statement/00/
page: https://datatracker.ietf.org/doc/draft-ali-netmod-yang-protobuf-problem-statement/ | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
Network devices increasingly expose operational APIs using gRPC and Protocol Buffers. Many of these APIs provide ephemeral or runtime state whose lifetime is limited to a process, service, session, or device runtime. At the same time, the IETF has standardized YANG as a data modeling language for network management and has defined encodings for YANG data, including JSON and CBOR. This document describes the problem space and identifies questions for the IETF community regarding standards-based gRPC APIs for ephemeral operational state. The scope is limited to ephemeral operational state. Configuration data and configuration management operations are out of scope.

### Yang Versioning Update
Presentation · Working group: netmod
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-05-yang-versioning-update-00 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
Slides presented at the netmod session; no Internet-Draft is linked to them.

### YANG path format (ypath)
Presentation · Working group: netmod
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-netmod-09-yang-path-format-ypath-00 | video: https://youtu.be/DCIGgML0pnk | materials: https://datatracker.ietf.org/meeting/127/session/netmod
Slides presented at the netmod session; no Internet-Draft is linked to them.

## Working Group: opsawg

### Generic MPLS Information Elements for Ordered Export in IPFIX
Draft: draft-claise-opsawg-ipfix-ordered-mpls-ie · Working group: opsawg
Agenda: Ordered Information Element Export in IP Flow Information Export (IPFIX)\& draft-claise-opsawg-ipfix-ordered-mpls-ie
page: https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-mpls-ie/ | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document defines new generic IPFIX Information Elements for MPLS label stacks and label attributes, intended for use with the ordered set mechanisms that provide an explicit ordering guarantee for repeated Information Elements.

### Export of ECN Information in IPFIX
Draft: draft-ietf-opsawg-ipfix-ecn · Working group: opsawg
Agenda: Reading Material: draft-ietf-opsawg-ipfix-ecn
page: https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-ecn/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-export-of-ecn-information-in-ipfix-04 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document defines a set of IPFIX Information Elements for monitoring Explicit Congestion Notification (ECN). These Information Elements allow network operators to observe ECN codepoint usage across network traffic and evaluate the corresponding traffic performance.

### A YANG Data Model for Network Diagnosis using Scheduled Sequences of OAM Tests
Draft: draft-ietf-opsawg-scheduling-oam-tests · Working group: opsawg
Agenda: Reading Material: draft-ietf-opsawg-scheduling-oam-tests
page: https://datatracker.ietf.org/doc/draft-ietf-opsawg-scheduling-oam-tests/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-3-a-yang-data-model-for-network-diagnosis-using-scheduled-sequences-of-oam-tests-01 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document defines two YANG Data Models to support scheduled network diagnosis using Operations, Administration, and Maintenance (OAM) tests. This document defines both 'oam-unitary-test' and 'oam- sequence-test' YANG modules to manage the lifecycle of network diagnosis procedures, intended for use by external management and orchestration systems (including SDN controllers and network orchestrators), rather than by individual network nodes.

### YANG deVELpment PrOCEss and maintenance (VELOCE)
Draft: draft-ietf-opsawg-veloce-yang · Working group: opsawg
Agenda: Reading Material: draft-ietf-opsawg-veloce-yang
page: https://datatracker.ietf.org/doc/draft-ietf-opsawg-veloce-yang/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-4-yang-development-process-and-maintenance-veloce-00 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document describes a YANG deVELopment PrOCEss and maintenance (VELOCE) that is more suitable for the development of YANG modules or YANG modules update within the IETF. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/ietf-opsawg-wg/veloce/tree/main.

### Applying COSE Signatures for YANG Data Provenance
Draft: draft-ietf-opsawg-yang-provenance · Working group: opsawg
Agenda: Reading Material: draft-ietf-opsawg-yang-provenance
page: https://datatracker.ietf.org/doc/draft-ietf-opsawg-yang-provenance/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-5-applying-cose-signatures-for-yang-data-provenance-00 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document defines a mechanism based on CBOR Object Signing and Encryption (COSE) signatures to provide and verify the provenance of YANG data, so it is possible to verify the origin and integrity of a dataset, even when those data are going to be processed and/or applied in workflows where a crypto-enabled data transport directly from the original data source is not available. As the application of evidence-based OAM automation and the use of tools such as AI/ML grow, provenance validation becomes more relevant in all scenarios, in support of the assuring the origin and integrity of data. The use of compact signatures facilitates the inclusion of provenance strings in any YANG schema requiring them.

### Normalized Representation of YANG Data for Equivalence Evaluation
Draft: draft-mendez-opsawg-yang-normalization · Working group: opsawg
Agenda: Reading Material: draft-mendez-opsawg-yang-normalization
page: https://datatracker.ietf.org/doc/draft-mendez-opsawg-yang-normalization/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-normalized-representation-of-yang-data-for-equivalence-evaluation-01 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document defines a normalization procedure for YANG-modeled information. The procedure enables different serialized representations conveying equivalent information to produce the same normalized representation independently of the input encoding and applicable representation conventions. The normalized representation is intended to support comparison, hashing, integrity verification, provenance, and other procedures that require consistent representation of equivalent YANG-modeled information.

### Export of RoCEv2 Base Transport Header (BTH) Information Using IP Flow Information Export (IPFIX)
Draft: draft-lin-opsawg-ipfix-rocev2 · Working group: opsawg
Agenda: Reading Material: draft-lin-opsawg-ipfix-rocev2
page: https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-rocev2/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-8-export-of-rocev2-base-transport-header-bth-information-using-ipfix-00 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
This document defines a new set of IP Flow Information Export (IPFIX) Information Elements (IEs) for exporting Base Transport Header (BTH) information for Remote Direct Memory Access (RDMA) over Converged Ethernet version 2 (RoCEv2) traffic. These extensions enable network monitoring systems to collect and analyze the characteristics of RDMA traffic widely used in high-performance computing, storage, and artificial intelligence applications.

### Ordered Information Element Export in IP Flow Information Export (IPFIX)
Draft: draft-claise-opsawg-ipfix-ordered-ie · Working group: opsawg
Agenda: Reading Material: draft-claise-opsawg-ipfix-ordered-ie \& draft-claise-opsawg-ipfix-ordered-mpls-ie
page: https://datatracker.ietf.org/doc/draft-claise-opsawg-ipfix-ordered-ie/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-ordered-information-element-export-in-ip-flow-information-export-ipfix-00 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
The IP Flow Information Export (IPFIX) protocol allows the same Information Element to appear multiple times in a Template Record. RFC 7011 states that multiple occurrences of the same Information Element SHOULD follow the logical order of their treatments by the Metering Process; however, no protocol mechanism exists for the Exporting Process to explicitly signal to the Collecting Process that this ordering is guaranteed. Without such a guarantee, the Collecting Process cannot safely interpret repeated Information Elements as ordered observations. This document describes the problem, presents use cases, analyzes candidate solutions, and specifies a mechanism, a new Ordered Set type, that establishes an end-to-end ordering guarantee: the Metering Process records repeated Information Element values in the order the corresponding observations are made, the Exporting Process preserves and signals this guarantee, and the Collecting Process interprets the n-th occurrence of an Information Element as corresponding to the n-th observation by the Metering Process at the Observation Point. This document updates RFC 7011, RFC 5476, and RFC 6183.

### Export of BGP FlowSpec Treatment Information in IPFIX
Draft: draft-gao-opsawg-flowspec-ipfix · Working group: opsawg
Agenda: Reading Material: draft-gao-opsawg-flowspec-ipfix
page: https://datatracker.ietf.org/doc/draft-gao-opsawg-flowspec-ipfix/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-10-export-of-bgp-flowspec-treatment-information-in-ipfix-00 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
BGP Flow Specification (FlowSpec) is commonly used to distribute traffic filtering and traffic treatment rules. Operational monitoring of FlowSpec deployments may require information from multiple sources, including BGP control-plane telemetry, operational state, and forwarding-plane observations. This document defines IP Flow Information Export (IPFIX) Information Elements that add FlowSpec context to IPFIX Flow Records. The exported information enables a Collector to correlate exported Flow Records with a FlowSpec rule in the scope of an Observation Domain and to identify the action classes reported by the Exporter.

### SSH Public Key Distribution for Device Administration using Terminal Access Controller Access-Control System Plus (TACACS+)
Draft: draft-dahm-opsawg-tacacs-sshpk · Working group: opsawg
Agenda: Reading Material: draft-dahm-opsawg-tacacs-sshpk
page: https://datatracker.ietf.org/doc/draft-dahm-opsawg-tacacs-sshpk/ | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
SSH [RFC4251] provides a robust and reliable mechanism to connect to network devices for administration. Conventionally, the public keys required to authenticate SSH sessions are provisioned directly on the network devices. This document adds an extension to Terminal Access Controller Access-Control System Plus (TACACS+) to eliminate the need for the direct provisioning of SSH public keys onto the Network Devices.

### Export of IGP Algorithm Information in IPFIX
Presentation · Working group: opsawg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-6-export-of-igp-algorithm-information-in-ipfix-00 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
Slides presented at the opsawg session; no Internet-Draft is linked to them.

### SSH Public Key Distribution via TACACS+
Presentation · Working group: opsawg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-11-ssh-public-key-distribution-via-tacacs-01 | video: https://youtu.be/DKWy3lZ2Yw8 | materials: https://datatracker.ietf.org/meeting/127/session/opsawg
Slides presented at the opsawg session; no Internet-Draft is linked to them.

## Working Group: quic

### Delegating QUIC Stateless Resets
Draft: draft-kazuho-quic-delegated-stateless-reset · Working group: quic
Agenda: draft-kazuho-quic-delegated-stateless-reset
page: https://datatracker.ietf.org/doc/draft-kazuho-quic-delegated-stateless-reset/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-delegated-stateless-resets-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
This document specifies how a QUIC endpoint can delegate sending Stateless Resets to a component that outlives its connection state. It also defines a frame for clients using zero-length Connection IDs to advertise a Stateless Reset Token and a transport parameter for servers to indicate support for receiving the frame.

### Exchanging Congestion Control Data in QUIC
Draft: draft-yuan-quic-congestion-data · Working group: quic
Agenda: draft-yuan-quic-congestion-data
page: https://datatracker.ietf.org/doc/draft-yuan-quic-congestion-data/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-exchanging-cc-data-in-quic-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
This draft defines a new transport frame which enables consenting endpoints to share congestion control state about the network connection for various purposes, including client-side adaptive bitrate selection during an ongoing connection. It also allows an endpoint's own congestion control state to be echoed back to it by a peer for consideration at the beginning of a future connection.

### QUIC Alternative Server Address Frames
Draft: draft-munizaga-quic-alternative-server-address · Working group: quic
Agenda: draft-munizaga-quic-alternative-server-address
page: https://datatracker.ietf.org/doc/draft-munizaga-quic-alternative-server-address/ | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
This document specifies an extension to QUIC that allows a server to advertise a prioritized set of alternative addresses. This allows a client to migrate the connection as the availability of, or preference among, server addresses changes.

### Using QUIC to traverse NATs
Draft: draft-seemann-quic-nat-traversal · Working group: quic
Agenda: draft-seemann-quic-nat-traversal
page: https://datatracker.ietf.org/doc/draft-seemann-quic-nat-traversal/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-quic-nat-traversal-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
This document specifies a QUIC extension for traversing Network Address Translators (NATs). Endpoints use an existing proxied QUIC connection to coordinate path validation attempts that create the NAT bindings needed for a direct path and test its connectivity. Application data can be exchanged over the proxied path while NAT traversal is in progress. Once a suitable direct path has been validated, the connection can migrate to it.

### QUIC-LB Update
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-quic-lb-update-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### qlog
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-qlog-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Receive timestamps
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-receive-timestamps-01 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Cuback
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-cuback-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### SQUAD Report
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-quic-squad-report-00 | video: https://youtu.be/Tklq_kw86zg | materials: https://datatracker.ietf.org/meeting/127/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

## Working Group: rift

### RIFT KV extensions for address block
Draft: draft-zdx-rift-addsblock-extensions · Working group: rift
Agenda: - https://datatracker.ietf.org/doc/draft-zdx-rift-addsblock-extensions/, Sandy Zhang, 10 minutes
page: https://datatracker.ietf.org/doc/draft-zdx-rift-addsblock-extensions/ | video: https://youtu.be/M4AMTDaBBA4 | materials: https://datatracker.ietf.org/meeting/127/session/rift
This document describes a method for extending the address blocks carried within Key/Value extensions in data centers where RIFT (Routing in Fat Trees) is deployed.

### RIFT extensions for SRv6
Draft: draft-cheng-rift-srv6-extensions · Working group: rift
Agenda: - https://datatracker.ietf.org/doc/draft-cheng-rift-srv6-extensions/, Weiqiang Cheng/Rui Zhuang, 10 minutes
page: https://datatracker.ietf.org/doc/draft-cheng-rift-srv6-extensions/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rift-02-rift-extensions-for-srv6-00 | video: https://youtu.be/M4AMTDaBBA4 | materials: https://datatracker.ietf.org/meeting/127/session/rift
The Segment Routing (SR) architecture allows a flexible definition of the end-to-end path by encoding it as a sequence of topological elements called segments. It can be implemented over an MPLS or IPv6 data plane. This document describes the RIFT extensions required to support Segment Routing over the IPv6 data plane (SRv6).

### Multicast Routing In Fat Trees
Draft: draft-zzhang-rift-multicast · Working group: rift
Agenda: - https://datatracker.ietf.org/doc/draft-zzhang-rift-multicast/, Jeffrey Zhang, 20 minutes
page: https://datatracker.ietf.org/doc/draft-zzhang-rift-multicast/ | video: https://youtu.be/M4AMTDaBBA4 | materials: https://datatracker.ietf.org/meeting/127/session/rift
This document specifies multicast procedures with RIFT. Multicast in RIFT is similar to Bidirectional Protocol Independent Multicast (PIM- Bidir), with the Rendezvous Point Link (RP-Link) simulated by a spanning tree of some Top of Fabric (TOF) nodes and sub-TOF nodes.

### RIFT-KV-addressblock
Presentation · Working group: rift
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rift-01-rift-kv-addressblock-00 | video: https://youtu.be/M4AMTDaBBA4 | materials: https://datatracker.ietf.org/meeting/127/session/rift
Slides presented at the rift session; no Internet-Draft is linked to them.

### RIFT Multicast
Presentation · Working group: rift
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rift-rift-multicast-00 | video: https://youtu.be/M4AMTDaBBA4 | materials: https://datatracker.ietf.org/meeting/127/session/rift
Slides presented at the rift session; no Internet-Draft is linked to them.

## Working Group: rtgwg

### A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network
Draft: draft-ietf-rtgwg-atn-bgp · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-atn-bgp/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-02-bgp-based-mobile-routing-system-for-the-aeronautical-telecommunications-network-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
The International Civil Aviation Organization (ICAO) is investigating mobile routing solutions for a worldwide Aeronautical Telecommunications Network with Internet Protocol Services (ATN/IPS). The ATN/IPS will eventually augment existing communication services with an IP-based service supporting pervasive Air Traffic Management (ATM) for Air Traffic Controllers (ATC), Airline Operations Controllers (AOC), and all commercial aircraft worldwide. This informational document describes a simple and extensible mobile routing service based on the industry-standard Border Gateway Protocol (BGP) and Domain Name System (DNS) to address the ATN/IPS requirements.

### Multi-segment SD-WAN via Cloud Backbone
Draft: draft-ietf-rtgwg-multisegment-sdwan · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/ | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
This document describes a method for seamlessly interconnecting geographically separated SD-WAN segments via a Cloud Backbone without requiring Cloud Gateways (GWs) to decrypt and re-encrypt traffic. By encapsulating IPsec- encrypted payloads within GENEVE headers (RFC 8926), the approach enables Cloud GWs to forward encrypted traffic directly between distant Customer Premises Equipment (CPEs). This reduces processing overhead, improves scalability, and preserves the confidentiality of enterprise data while ensuring secure and efficient multi-segment SD-WAN connectivity.

### The IGP is not a Dump Truck
Draft: draft-halpern-rtgwg-not-a-dump-truck · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-halpern-rtgwg-not-a-dump-truck/
page: https://datatracker.ietf.org/doc/draft-halpern-rtgwg-not-a-dump-truck/ | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
This document explores addressing the problem of using an IGP to carry arbitrary information, often referred to using the phrase "the IGP is not a dump truck". It describes the kinds of information carried in an IGP and proposes an approach to changing the system.

### Elastic Bandwidth-aware Routing Framework
Draft: draft-czz-rtgwg-elastic-bandwidth-routing · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/
page: https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-05-elastic-bandwidth-routing-framework-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
IGP normally computes the shortest paths in a network for packet forwarding, without taking the traffic demands and available bandwidth into consideration. When there is a link degradation or partial link failure in a network which causes throughput reduction, or the volume of specific traffic flows increase dramatically, unexpected congestion may happen if only the shortest paths are used for IP forwarding. Conventional centralized Traffic Engineering (TE) focuses on long- term bandwidth and routes planning based on traffic demands, which can not react to the congestions in networks timely. This document describes a distributed path computation and load balancing mechanism named Elastic Bandwidth-aware Routing (EBR), which can alleviate congestions timely before TE finishes the global optimization. It allows IGP-enabled nodes which face congestion to distribute traffic among the shortest paths and load-balancing alternate paths through Segment Routing (SR) strict path, with weights determined based on the bandwidth utilization and available bandwidth of these paths. It provides an efficient, accurate and backward compatible approach for dynamic link congestion avoidance.

### Common Approaches to Link Overload Alleviation
Draft: draft-li-rtgwg-overload-alleviation · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-li-rtgwg-overload-alleviation/
page: https://datatracker.ietf.org/doc/draft-li-rtgwg-overload-alleviation/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-06-common-approaches-to-link-overload-alleviation-01 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Network links may become degraded because of physical conditions or owing to partial link failure: this can result in a reduction of available bandwidth. Alternatively, traffic volume may increase significantly and unexpectedly. These circumstances may lead to links becoming overloaded which can result in dropped packets or degraded delivery such as increased delay. Traffic adjustment techniques can be applied to alleviate these link- overload situations by steering some of the traffic onto other paths that are less loaded and have available bandwidth. This document examines the scenarios in which links can become overloaded, the requirements for steering traffic to reduce link- overload, and the techniques that can be applied to alleviate overloaded links.

### BGP-based Inter-domain Elastic Bandwidth-aware Routing Framework
Draft: draft-rzz-rtgwg-inter-domain-ebr · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-rzz-rtgwg-inter-domain-ebr/
page: https://datatracker.ietf.org/doc/draft-rzz-rtgwg-inter-domain-ebr/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-07-bgp-based-inter-domain-elastic-bandwidth-aware-routing-framework-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Although operators typically consider redundant capacity during network design, link congestion may still occur under specific scenarios, such as link degradation or traffic bursts. Several congestion mitigation mechanisms have been proposed for intra-domain links, but congestion is not limited to intra-domain links, it can also occur on inter-domain links. Since changes of available bandwidth do not trigger updates to BGP route selection, BGP cannot alleviate inter-domain link congestion automatically, causing packet loss or increased delay. This document defines a BGP-based inter-domain elastic bandwidth- aware routing (BEBR) mechanism, to alleviate inter-domain link congestion. To avoid the dependency on cross-domain deployment, this document proposes both inbound BEBR and outbound BEBR, designed to address inbound and outbound traffic congestion, respectively. Thus, the congestion on both directions of inter-domain links can be mitigated by deploying BEBR on only one side of the inter-domain link.

### Congestion Avoidance Using Segment Routing
Draft: draft-he-rtgwg-sr-ca · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-he-rtgwg-sr-ca/
page: https://datatracker.ietf.org/doc/draft-he-rtgwg-sr-ca/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-08-congestion-avoidance-using-segment-routing-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
This document describes a generic solution of congestion avoidance, which is aimed at providing local link congestion avoidance within the Segment Routing (SR) framework. Based on the concept of Topology Independent Loop-Free Alternate (TI- LFA) Fast Reroute (FRR), the selected shortest path can bypass the congested link while avoiding the formation of micro-loops. The advantage of this solution is that it does not require any protocol extension.

### Routing mechanism in Dragonfly Networks Gap Analysis, Problem Statement, and Requirements
Draft: draft-wang-rtgwg-dragonfly-routing-problem · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-wang-rtgwg-dragonfly-routing-problem/
page: https://datatracker.ietf.org/doc/draft-wang-rtgwg-dragonfly-routing-problem/ | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
This document provides the gap analysis of existing routing mechanism in Dragonfly networks, describes the fundamental problems, and defines the requirements for technical improvements.

### HPC/AI Scheduler Job Metadata Model
Draft: draft-xkk-rtgwg-hpc-scheduler-job-metadata · Working group: rtgwg
Agenda: https://www.ietf.org/archive/id/draft-xkk-rtgwg-hpc-scheduler-job-metadata-00.txt
page: https://datatracker.ietf.org/doc/draft-xkk-rtgwg-hpc-scheduler-job-metadata/ | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
This document defines a scheduler-facing metadata model for High Performance Computing (HPC) and AI workloads. The model captures common job, workload, scheduler, tenant, timing, and task metadata that can be mapped from heterogeneous workload managers and orchestration platforms and used as context for network service intent.

### HPC/AI Service Intent Model
Draft: draft-xkk-rtgwg-hpc-service-intent · Working group: rtgwg
Agenda: https://www.ietf.org/archive/id/draft-xkk-rtgwg-hpc-service-intent-00.txt
page: https://datatracker.ietf.org/doc/draft-xkk-rtgwg-hpc-service-intent/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-10-hpc-scheduller-job-metadata-service-intent-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
This document defines a common service intent model for High Performance Computing (HPC) and AI workloads over High Performance Wide Area Networks (HP-WANs). The model allows heterogeneous workload managers and orchestration platforms to express endpoint, communication pattern, timing, performance, data movement, policy, and admission requirements for network services without exposing technology-specific tunnel realization details.

### A Framework for SRv6-Based Trusted Key Relay in Quantum Key Distribution Networks
Draft: draft-chen-rtgwg-framework-srv6-trusted-relay-qkd · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-chen-rtgwg-framework-srv6-trusted-relay-qkd/
page: https://datatracker.ietf.org/doc/draft-chen-rtgwg-framework-srv6-trusted-relay-qkd/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-11-a-framework-for-srv6-based-trusted-key-relay-in-quantum-key-distribution-networks-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Quantum Key Distribution (QKD) links generate symmetric key material between directly connected QKD nodes. Trusted relay is commonly used to extend key delivery beyond the reach of a single QKD link. A complete trusted-relay service requires the network to collect QKD link and node quantum capability information, compute a relay path according to service requirements, translate the result into a network forwarding path, and carry the relayed key information in an IPv6/UDP packet steered by that path. This document describes an architectural framework for such a service. Each QKD link provides its link quantum capability such as available quantum key rate capacity, and each relay node provides its node quantum capability . A controller uses these inputs together with application requirements to calculate a relay path. The path- computation algorithm is not standardized and may be selected or defined by the user, operator, or implementation. The calculated relay sequence is represented as an SRv6 path, and UDP packets following that path carry the key-relay information. This document identifies the protocol extension points needed to support the framework. The detailed encodings, message formats, TLVs, and signaling procedures are left for future work and are marked as TBD.

### Scenarios and Routing Requirements for Mega-Constellation LEO Satellite Networks
Draft: draft-miao-rtgwg-satellite-routing-reqs · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-miao-rtgwg-satellite-routing-reqs/
page: https://datatracker.ietf.org/doc/draft-miao-rtgwg-satellite-routing-reqs/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-12-scenarios-and-routing-requirements-for-mega-constellation-leo-satellite-networks-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Large-scale Low Earth Orbit (LEO) satellite constellations equipped with optical Inter-Satellite Links (ISLs) are evolving toward multi- hop spaceborne transport networks. Multi-vendor constellation deployments, interconnection with terrestrial networks, and potential interconnection among heterogeneous satellite systems introduce requirements for interoperable routing behavior and reachability exchange. At the same time, large constellation size, time-varying topology, unplanned link disruptions, and constrained on-board resources raise scalability and stability challenges for routing mechanisms. This document describes representative deployment and interoperability scenarios, examines the limitations of network-wide fine-grained link-state distribution and existing mitigation approaches, and identifies routing requirements for scalable state management, topology-change handling, fast recovery, and inter- network reachability.

### Adaptive Routing Framework
Draft: draft-cheng-rtgwg-adaptive-routing-framework · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-adaptive-routing-framework/
page: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-adaptive-routing-framework/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-13-adaptive-routing-framework-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
In many cases, ECMP (Equal-Cost Multi-Path) flow-based hashing leads to high congestion and variable flow completion time. This reduces applications performance. Load balancing based on local link quality is not always optimal, A global view of congestion, with information from remote links, is needed for optimal balancing. Adaptive routing is a technology that makes dynamic routing decision based on changes in traffic load and network topology. This document describes a framework for Adaptive Routing. Specifically, it identifies a set of adaptive routing components, explains their interactions, and exemplifies the workflow mechanism.

### Enhanced ECMP for AI Cluster
Draft: draft-cheng-rtgwg-enhanced-ecmp · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/
page: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-14-enhanced-ecmp-for-ai-cluster-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
In AI training scenarios, per-flow ECMP is the mainstream load balancing technology deployed in current networks. However, inherent hash collision issues of traditional ECMP lead to imbalanced traffic distribution, adversely affecting application performance. To address this problem, this document proposes an enhanced ECMP method that resolves load imbalance caused by hash collisions. The proposed solution effectively improves load balancing efficiency, reduces network congestion, and enhances overall network performance.

### multi-segment-sdwan
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-03-multi-segment-sdwan-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### Problem Statement for Moving Some Information Out of the IGP
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-04-problem-statement-for-moving-some-information-out-of-the-igp-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### Routing Mechanism in Dragonfly Networks
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-09-routing-mechanism-in-dragonfly-networks-00 | video: https://youtu.be/CKWa3STuXj8 | materials: https://datatracker.ietf.org/meeting/127/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

## Working Group: savnet

### Inter-domain Source Address Validation (SAVNET) Architecture
Draft: draft-ietf-savnet-inter-domain-architecture · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-architecture/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-architecture/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-the-updates-on-the-inter-domain-source-address-validation-architecture-01 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
This document specifies an architecture for inter-domain source address validation (SAV). The architecture provides a common framework for collecting SAV-specific and SAV-related information from multiple sources, determining the legitimate incoming directions of source prefixes, and using this information to generate SAV table for inter-domain SAV. A SAV agent maintains the collected information in a SAV Information Base (SIB), and the SAV Information Base Manager (SIM) uses the available information to determine the corresponding prefix and legitimate incoming-direction mappings and generate or update the SAV table. This document also defines the architectural components and communication framework of inter-domain SAV, and discusses deployment, operation, convergence, manageability, security, and privacy considerations. It does not define a specific SAV protocol, protocol extension, or SAV table generation algorithm.

### Intra-domain Source Address Validation Architecture
Draft: draft-ietf-savnet-intra-domain-architecture · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-updates-on-intra-domain-source-address-validation-architecture-00 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
This document describes a generic architecture for intra-domain Source Address Validation (SAV). It provides a common framework for developing new intra-domain SAV mechanisms and describes the conditions under which this architecture can improve SAV accuracy and operational efficiency with respect to existing intra-domain SAV mechanisms.

### IntraSAV - A Solution for Intra-Domain Source Address Validation
Draft: draft-sriram-savnet-intrasav-solution · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-sriram-savnet-intrasav-solution/
page: https://datatracker.ietf.org/doc/draft-sriram-savnet-intrasav-solution/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-intrasav-a-solution-for-intra-domain-source-address-validation-01 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
This document specifies a solution, named IntraSAV, for intra-domain source address validation (SAV). This solution addresses the problem stated in the ietf-savnet-intra-domain-problem-statement (RFC-to-be) document. This document updates BCP 38 ([RFC2827]) and BCP 84 ([RFC3704], [RFC8704]) by providing a more comprehensive solution methodology and accommodating prefixes that are not routed but used for sourcing traffic originating from an AS.

### Bicone Source Address Validation
Draft: draft-qin-savnet-bicone-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-qin-savnet-bicone-sav/
page: https://datatracker.ietf.org/doc/draft-qin-savnet-bicone-sav/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-updates-on-bicone-source-address-validation-00 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
Source address validation (SAV) aims to detect source-spoofed traffic while avoiding improper blocking of legitimate traffic. Existing SAV mechanisms commonly rely on ingress allowlist filters on interfaces facing customer or lateral peer Autonomous Systems (ASes). When such an allowlist is incomplete, a source address not covered by the allowlist cannot be conclusively identified as spoofed, because legitimate source prefixes may be missing from the allowlist. This document describes Bicone SAV, which jointly uses an allowlist derived from customer-cone information and a blocklist containing prefixes that can be positively identified as inappropriate on the corresponding ingress interface. When the allowlist is incomplete, packets matching the allowlist are permitted, packets matching the blocklist are discarded, and packets matching neither list are permitted with logging or other monitoring for subsequent analysis. The blocklist can be constructed from provider-cone information and augmented with denylist information derived from customer cones.

### Export of Source Address Validation (SAV) Information in IPFIX
Draft: draft-cao-savnet-ipfix-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-cao-savnet-ipfix-sav/
page: https://datatracker.ietf.org/doc/draft-cao-savnet-ipfix-sav/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-export-of-sav-information-in-ipfix-00 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
This document specifies the IP Flow Information Export Information Elements to export the context and outcome of Source Address Validation enforcement data. These SAV-specific Information Elements provide detailed insight into why packets are identified as spoofed by capturing the specific SAV rules that triggered validation decisions. This operational visibility is essential for network operators to observe SAV enforcement behavior and analyze source address spoofing events detected by SAV.

### Currently Used Terminology Related to Source Address Validation
Draft: draft-gq-savnet-sav-terms · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-gq-savnet-sav-terms/02/
page: https://datatracker.ietf.org/doc/draft-gq-savnet-sav-terms/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-currently-used-terminology-related-to-source-address-validation-00 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
This document provides an overview of terms and abbreviations related to Source Address Validation (SAV). Its purpose is to establish a common and consistent set of terminology for use across SAV-related discussions and documents. This document explicitly does not serve as an authoritative source of correct terminology.

### HPE IPFIX behavior for SAV
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-savnet-hpe-ipfix-behavior-for-sav-00 | video: https://youtu.be/BRTmg4CpK5I | materials: https://datatracker.ietf.org/meeting/127/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

## Working Group: scone

### Manageability Considerations for SCONE
Draft: draft-ietf-scone-applicability-manageability · Working group: scone
Agenda: draft-ietf-scone-applicability-manageability-03
page: https://datatracker.ietf.org/doc/draft-ietf-scone-applicability-manageability/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-scone-draft-ietf-scone-applicability-manageability-03-00 | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
This document describes the manageability considerations for network operators for providing throughput advice to application endpoints. This guidance is specifically addressed within the context of communication networks utilizing the Standard Communication with Network Elements (SCONE) protocol [SCONE].

### In-Band SCONE Reporting over QUIC
Draft: draft-duke-scone-scone-echo · Working group: scone
Agenda: draft-duke-scone-scone-echo-03
page: https://datatracker.ietf.org/doc/draft-duke-scone-scone-echo/ | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
The SCONE protocol relies on the receiver of SCONE packets to send bandwidth estimates back to the sender via unspecified application- layer messages. In some cases, a peer might have SCONE receive capability at the QUIC layer but not implement the necessary application level functionality. A new QUIC frame that directly reports the contents of received SCONE packets can address these use cases. There are no changes in the interaction with SCONE Network Elements.

### SCONE Applicability for IEEE 802.11 Access Networks
Draft: draft-gundavelli-scone-wifi-applicability · Working group: scone
Agenda: draft-gundavelli-scone-wifi-applicability-01
page: https://datatracker.ietf.org/doc/draft-gundavelli-scone-wifi-applicability/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-scone-scone-applicability-for-ieee-80211-access-networks-00 | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
This document describes the applicability of the Standard Communication with Network Elements (SCONE) protocol to IEEE 802.11 based access networks. SCONE defines a mechanism by which an on-path network element can provide advisory downlink throughput guidance to QUIC endpoints. The SCONE protocol is access agnostic and does not assume any specific access technology. In IEEE 802.11 deployments, such constraints may be derived at access points or controllers that combine policy awareness, with visibility into access network conditions. This document explains how existing SCONE roles and throughput advice semantics apply in these deployments without assuming any specific IEEE 802.11 MAC or PHY behavior. This document does not define new protocol extensions and does not modify SCONE behavior. Its purpose is to clarify deployment considerations for IEEE 802.11 environments.

### QUIC Logging for the SCONE Protocol
Draft: draft-kejriwal-scone-scone-qlog · Working group: scone
Agenda: draft-kejriwal-scone-scone-qlog-00
page: https://datatracker.ietf.org/doc/draft-kejriwal-scone-scone-qlog/ | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
This document defines qlog events for the Standard Communication with Network Elements (SCONE) protocol. The events record the sending and reception of SCONE packets and changes to throughput advice.

### SCONE-Based Rate Advice for RoCEv2 Networks
Draft: draft-zz-scone-rate-advice-rocev2 · Working group: scone
Agenda: draft-zz-scone-rate-advice-rocev2-01
page: https://datatracker.ietf.org/doc/draft-zz-scone-rate-advice-rocev2/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-scone-scone-based-rate-advice-for-rocev2-networks-00 | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
This document describes the applicable scenarios of the Standard Communication Protocol for Network Elements (SCONE) in RoCEv2 networks. SCONE defines a mechanism that enables network elements on the forwarding path to deliver throughput guidance to RoCEv2 endpoints. This document further specifies the method for carrying Rate Advice in RoCEv2 networks. The Rate Advice is generated by network nodes (e.g., switches), which can be either rate limits defined by network policies or quantitative rate adjustment recommendations derived from network status information. This document specifies two implementation solutions with different granularities. Solution 1 provides path-granularity (source-IP- based) Rate Advice through out-of-band UDP messages sent directly from network elements to senders; a single advised rate applies to all active Queue Pairs (QPs) originating from the same source IP, providing sub-RTT feedback. Solution 2 provides per-flow (per-QP) Rate Advice through an on-path Rate Signal with endpoint feedback, reusing the RoCEv2 data path and following the feedback loop model of the SCONE protocol; each QP receives its own advised rate.

### SCONE-ECHO
Presentation · Working group: scone
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-scone-scone-echo-00 | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
Slides presented at the scone session; no Internet-Draft is linked to them.

### slides-ietf127-scone-qlog
Presentation · Working group: scone
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-scone-slides-ietf127-scone-qlog-00 | video: https://youtu.be/JAQzbGFTm90 | materials: https://datatracker.ietf.org/meeting/127/session/scone
Slides presented at the scone session; no Internet-Draft is linked to them.

## Working Group: spring

### ICMP Error Handling for VPNs in SRv6 Networks
Draft: draft-alivar-6man-icmp-error-srv6-vpn · Working group: spring
Agenda: draft-alivar-6man-icmp-error-srv6-vpn
page: https://datatracker.ietf.org/doc/draft-alivar-6man-icmp-error-srv6-vpn/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-icmp-error-handling-for-vpns-in-srv6-networks-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
The document specifies procedures for handling ICMP error messages in SRv6-based Virtual Private Network (VPN). It describes three methods to improve the ICMP Error Handling for SRv6-VPNs.

### Flexible Candidate Path Selection of SR Policy
Draft: draft-ietf-spring-sr-policy-flexible-cp-selection · Working group: spring
Agenda: draft-ietf-spring-sr-policy-flexible-cp-selection
page: https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-flexible-cp-selection/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-flexible-candidate-path-selection-of-sr-policy-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
This document describes a flexible method for selecting candidate Segment Routing (SR) policy paths. Based on the real-time resource usage and forwarding quality of candidate paths, the head node can perform dynamic path switching among multiple candidate paths in the SR policy.

### Signaling RSVP-TE Tunnels on an SR-MPLS Forwarding Plane Using Adjacency Segment Identifiers
Draft: draft-beeram-mpls-rsvp-sr · Working group: spring
Agenda: draft-beeram-mpls-rsvp-sr
page: https://datatracker.ietf.org/doc/draft-beeram-mpls-rsvp-sr/ | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
RFC 8577 introduced the concept of signaling RSVP-TE tunnels on a shared MPLS forwarding plane using preinstalled "TE link labels". Those labels are functionally equivalent to Segment Routing (SR) Adjacency Segment Identifiers (Adj-SIDs) but are allocated and distributed solely via RSVP-TE signaling. This document extends RFC 8577 so that RSVP-TE tunnels can use Segment Routing over MPLS (SR-MPLS) Adj-SIDs, as specified in RFC 8402 and RFC 8660, in place of TE link labels. It restricts scope to Adj-SIDs attached to a single unidirectional adjacency and defines the signaling procedures and protocol extensions required to couple the RSVP-TE control plane with the SR-MPLS data plane.

### Signaling RSVP-TE Tunnels on an SRv6 Forwarding Plane Using End.X Segment Identifiers
Draft: draft-beeram-teas-rsvp-srv6 · Working group: spring
Agenda: draft-beeram-teas-rsvp-srv6
page: https://datatracker.ietf.org/doc/draft-beeram-teas-rsvp-srv6/ | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
RFC 8577 defines mechanisms to signal RSVP-TE tunnels on a shared MPLS forwarding plane by introducing the notion of per-TE link labels that are functionally equivalent to SR-MPLS adjacency segments. This document extends that work to the SRv6 data plane, defining the signaling extensions and procedures necessary to establish RSVP-TE tunnels that utilize SRv6 Segment Identifiers (SIDs) for forwarding. This document specifies how SRv6 End.X SIDs that are advertised in the IGP serve as TE link SIDs, defines new RSVP signaling extensions for carrying SRv6 SIDs and for influencing the endpoint behavior flavors of the SIDs, describes TE path segment-list construction procedures at the ingress (including NEXT-CSID compressed segment lists), adapts the delegation mechanisms of RFC 8577 to use SRv6 Binding SIDs, and describes the termination of the tunnel at the egress. The result couples the traffic engineering capabilities of the RSVP-TE control plane with the native IPv6 forwarding of SRv6.

### BGP SR Policy Extensions for BFD Configuration
Draft: draft-li-idr-bgp-sr-policy-bfd-extension · Working group: spring
Agenda: draft-li-idr-bgp-sr-policy-bfd-extension
page: https://datatracker.ietf.org/doc/draft-li-idr-bgp-sr-policy-bfd-extension/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-bgp-sr-policy-extensions-for-bfd-configuration-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
Segment Routing (SR) Policies require fast failure detection for Candidate Paths (CPs) to enable rapid rerouting and high availability. Currently, the provisioning of SR Policies and the configuration of the associated Seamless Bidirectional Forwarding Detection (S-BFD) sessions are performed independently. This often necessitates separate mechanisms (e.g., manual configuration, NETCONF, or additional signaling) to associate S-BFD sessions with the SR Policies, resulting in complex and error-prone operations. This document defines extensions to BGP SR Policy for the simultaneous provisioning of SR Policy CPs and their S-BFD configuration parameters during policy advertisement. The extensions include optional sub-TLVs within the Tunnel Encapsulation Attribute to carry S-BFD configuration parameters (e.g., discriminators, intervals, multipliers). These extensions simplify deployment in distributed or controller- based environments, reduce configuration overhead, and enhance operational efficiency for SR-based traffic engineering.

### Distributed Bandwidth Management for Segment Routing
Draft: draft-hegde-spring-sr-distributed-bw · Working group: spring
Agenda: draft-hegde-spring-sr-distributed-bw
page: https://datatracker.ietf.org/doc/draft-hegde-spring-sr-distributed-bw/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-distributed-bandwidth-management-for-segment-routing-draft-hegde-spring-sr-distributed-bw-00-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
This document defines an architecture for distributed bandwidth management in Segment Routing (SR) networks. Distributed bandwidth management is a model in which the bandwidth required by each SR Policy is computed and reserved in a distributed manner by the network nodes themselves, rather than by a centralized controller, so that path computation, admission control, and bandwidth accounting for SR Policies are performed by the head-end and transit nodes along the path.

### SRv6 for Multipath Traffic Engineering
Draft: draft-ajp-spring-srv6-mpte · Working group: spring
Agenda: draft-ajp-spring-srv6-mpte
page: https://datatracker.ietf.org/doc/draft-ajp-spring-srv6-mpte/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-srv6-for-multipath-traffic-engineering-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel is a Traffic Engineering (TE) construct that enables weighted load balancing of unicast traffic across a constrained set of paths optimized for an objective. This document is informational and describes one realization approach for applying SRv6 semantics to MPTE, based on the Multipath Traffic Engineering as described in Internet-Draft (draft-kompella-teas- mpte). It summarizes associated procedures, lifecycle, management, and forwarding behavior. This document applies existing SRv6 architecture and semantics to MPTE without defining new SRv6 Endpoint Behaviors or signaling protocols. It focuses on data-plane realization using existing forwarding instructions.

### Framework for Time-Scheduled Color based SR Policy Selection
Draft: draft-huang-spring-time-scheduled-color-framework · Working group: spring
Agenda: draft-huang-spring-time-scheduled-color-framework
page: https://datatracker.ietf.org/doc/draft-huang-spring-time-scheduled-color-framework/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-framework-for-time-scheduled-color-based-sr-policy-selection-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
In Segment Routing (SR) based VPN services, the BGP Color Extended Community is used by the egress Provider Edge (PE) router to steer VPN traffic into an SR Policy at the ingress PE. In many deployment scenarios, a customer requires different Service Level Agreements (SLAs) during different time periods of a day. For example, during business hours (e.g., 06:00 to 02:00 the next day) a best-effort, lower-cost SLA is sufficient for normal office traffic, while during the early morning hours (e.g., 02:00 to 06:00) a high-bandwidth, low-latency SLA is required for massive data transmission such as scientific computing. This document presents a framework for time-scheduled Color based SR Policy selection. The mechanism allows the egress PE to advertise multiple (Color, Color Schedule) pairs for the same VPN routes, enabling the ingress PE to select the appropriate SR Policy based on the current time. The time-to-Color mapping is configured per VPN instance (VRF/VSI), so each customer can have an independent time-varying SLA policy. This document is an Informational framework that describes the problem and the overall architecture. The advantages of the proposed mechanism and the comparison with alternative approaches are provided in Appendix A. The normative specifications of the protocol extensions, data models, and other components are described in Appendix B.

### SR-TE Path Based on Quality-Aware Dynamic Adaptive Adjustment
Draft: draft-cheng-spring-srpolicy-ar-framework · Working group: spring
Agenda: draft-cheng-spring-srpolicy-ar-framework
page: https://datatracker.ietf.org/doc/draft-cheng-spring-srpolicy-ar-framework/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-sr-te-path-based-on-quality-aware-dynamic-adaptive-adjustment-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
This document defines a framework for quality-aware dynamic adaptive adjustment of Segment Lists within an SR-TE Candidate Path. It addresses the limitation of static weight assignment, which cannot adapt to dynamic changes in path quality (e.g., latency, loss, utilization). The framework enables continuous monitoring of end-to- end metrics for each Segment List, computation of updated weights proportional to their relative quality, and application at the policy head-end. This allows the Candidate Path to autonomously optimize traffic distribution towards higher-quality paths, enhancing performance without altering the SR-Policy architecture.

### YANG Data Model for SR Policy Group
Draft: draft-gong-spring-sr-policy-group-yang · Working group: spring
Agenda: draft-gong-spring-sr-policy-group-yang
page: https://datatracker.ietf.org/doc/draft-gong-spring-sr-policy-group-yang/ | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
This document defines a YANG data model for Segment Routing (SR) Policy Group that can be used for configuring, instantiating, and managing SR Policy groups. The model is generic and applies equally to the MPLS and SRv6 instantiations of SR Policy groups.

### Distributed Bandwidth Management in Segment Routing Networks using RSVP-TE
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-spring-distributed-bandwidth-management-in-segment-routing-networks-using-rsvp-te-00 | video: https://youtu.be/UAT93gqW_Xg | materials: https://datatracker.ietf.org/meeting/127/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

## Working Group: srv6ops

### SRv6 Deployment Options
Draft: draft-ietf-srv6ops-srv6-deployment · Working group: srv6ops
Agenda: draft-ietf-srv6ops-srv6-deployment
page: https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6-deployment/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-37-srv6-sfc-deployment-options-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
When deciding to migrate a network from existing data-plane technologies (e.g. MPLS, SR-MPLS or overlay encapsulations such as VXLAN) to SRv6, common questions involve how to perform the migration, how to minimize impact to the existing network and what techniques are available to support a smooth transition. This document presents various deployment and migration options for networks evolving toward SRv6 from prior transport or overlay technologies.

### Addressing Recommendations for SRv6
Draft: draft-ietf-srv6ops-srv6addressing · Working group: srv6ops
Agenda: draft-ietf-srv6ops-srv6addressing
page: https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6addressing/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-32-addressing-recommendations-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
This document provides recommendations for addressing SRv6 locators format. It introduces concepts of Blocks, Sets, and Node IDs, and explains how summarization boundaries and flexible algorithm support can be implemented for both small and large networks.

### Operational Guidance for Protection Mechanisms in SRv6 Networks
Draft: draft-liu-srv6ops-sr-protection · Working group: srv6ops
Agenda: draft-liu-srv6ops-sr-protection
page: https://datatracker.ietf.org/doc/draft-liu-srv6ops-sr-protection/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-33-operational-guidance-for-protection-mechanisms-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
This document describes the Operational Guidance for protection of Segment Routing Over IPv6 (SRv6) networks.

### Operational Guidelines for BFD Monitoring in SRv6 Policies
Draft: draft-liu-srv6ops-bfd-srv6-policy-encap · Working group: srv6ops
Agenda: draft-liu-srv6ops-bfd-srv6-policy-encap
page: https://datatracker.ietf.org/doc/draft-liu-srv6ops-bfd-srv6-policy-encap/ | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
This document provides operational guidelines for Bidirectional Forwarding Detection (BFD) when applied to Segment Routing over IPv6 (SRv6) Policies. While the packet encapsulation mechanisms are standardized, this document focuses on the decisions network operators must make regarding mode selection, address management, traffic engineering integration, and troubleshooting strategies to ensure reliable service protection and efficient resource utilization. It addresses practical challenges such as handling diverse tail-end node capabilities (IPv4/IPv6), managing BFD session overhead in large-scale segment lists, and diagnosing failure detection anomalies in source-routed paths.

### SRv6-based Rate Control
Draft: draft-lx-srv6ops-srv6-rate-control · Working group: srv6ops
Agenda: draft-lx-srv6ops-srv6-rate-control
page: https://datatracker.ietf.org/doc/draft-lx-srv6ops-srv6-rate-control/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-35-srv6-based-rate-control-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
This document describes a deployment model and operational considerations for rate control in Segment Routing over IPv6 (SRv6) network slices. It leverages a token-bucket scheduler to differentiate Committed Information Rate (CIR) and Peak Information Rate (PIR) traffic, and describes how a headend may enforce a rate profile on an SR Policy and adjust the PIR based on network conditions. It addresses the operational trade-off between resource utilization and congestion avoidance in over-committed slice deployments.

### SRv6 SFC Deployment Options
Draft: draft-ye-srv6ops-sfc-deployment · Working group: srv6ops
Agenda: draft-ye-srv6ops-sfc-deployment
page: https://datatracker.ietf.org/doc/draft-ye-srv6ops-sfc-deployment/ | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
This document outlines the critical factors for deploying Service Function Chaining (SFC) using Segment Routing over IPv6 (SRv6). It addresses deployment architectures, including both SRv6-aware and SRv6-unaware scenarios, and details the end-to-end provisioning lifecycle. Furthermore, it proposes reliability mechanisms and provides strategic recommendations for network operators transitioning from legacy NSH-based SFC to a modern, scalable SRv6 framework.

### Resilient AI Supercomputer Networking using MRC and SRv6
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-21-resilient-ai-supercomputer-networking-using-mrc-and-srv6-01 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 Powered Backbone Networks
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-22-srv6-powered-backbone-networks-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 for AI Backend
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-23-srv6-for-ai-backend-01 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Deployment Options
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-31-deployment-options-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### BFD Encapsulation in SRv6 Policy
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-34-bfd-encapsulation-in-srv6-policy-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### VXLAN and SRv6 Gateway
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-36-vxlan-and-srv6-gateway-00 | video: https://youtu.be/hHcPOklRq1Y | materials: https://datatracker.ietf.org/meeting/127/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

## Working Group: tcpm

### Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO
Draft: draft-ietf-tcpm-tcp-ao-algs · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tcpm-tcp-ao-future-three-drafts-00 | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
RFC 5926 established a registry of cryptographic algorithms that can be used with TCP-AO. This document expands that registry, adding two Message Authentication Code (MAC) algorithms, HMAC-SHA256-128 and KMAC256-128. For each MAC algorithm, a corresponding Key Derivation Function (KDF) is also added. The MAC algorithms described by this document produce 128-bit (i.e., 16-byte) MACs. When 16-byte MACs are encoded in TCP-AO, the TCP-AO consumes 20 of the 40 bytes available for TCP options.

### Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO
Draft: draft-bonica-tcpm-tcp-ao-long-algs · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/ | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
RFC5926 creates a registry of cryptographic algorithms that can be used with TCP-AO. This document expands that registry, adding two Message Authentication Code (MAC) algorithms, HMAC-SHA256 and KMAC256. The MAC algorithms described by this document produce 256-bit (i.e., 32-byte) MACs. When 32-byte MACs are encoded in TCP-AO, the TCP-AO consumes 36 of the 40 bytes available for TCP options.

### An Upgraded TCP Session Type
Draft: draft-bonica-tcpm-extended-options · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/ | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
Currently, TCP maintains ordinary sessions (SES-O) in which ordinary segments (SEG-O) are exchanged. Each SEG-O can accommodate up to 40 octets of options. In the future, applications may require more than 40 octets of options. For example, an application may use a 36-byte TCP Authentication Option (TCP-AO), leaving insufficient space for other required options. Therefore, this document describes an experiment in which upgraded sessions (SES-U) and upgraded segments (SEG-U) are introduced. Each SEG-U can accommodate up to 1,016 octets of Individual Options.

### The Session Identifier Option (SIO)
Draft: draft-cmcc-tcp-sro · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-cmcc-tcp-sro/
page: https://datatracker.ietf.org/doc/draft-cmcc-tcp-sro/ | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
This document defines the Session Identifier Option (SIO), carried as a TCP option for TCP connections and as a UDP option for UDP datagrams. The option lets the endpoints of a connection or flow publish identifiers at the transport layer, where network functions on the path - load balancers, NAT gateways, firewalls - can read them without per-flow state and without payload inspection. Network functions of all kinds can benefit from it: session recovery in load- balancing and NAT clusters, stateless forwarding, connection-tracking recovery, and telemetry. The option adds only a few octets, and only to the packets that carry it; which packets carry it is a deployment choice. Endpoints that do not support it behave as if the option did not exist.

### TCP Packet Trimming Extension
Draft: draft-mazilu-tcpm-packet-trimming · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/
page: https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tcpm-tcp-packet-trimming-00 | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
This document specifies a TCP extension that enables TCP endpoints in data center networks or similarly controlled administrative domains to use packet trimming information when it is available. When switch buffers exceed a threshold, rather than silently dropping a packet, the switch trims the payload and forwards the header. This allows the destination to issue a deterministic Negative Acknowledgment (NACK), enabling faster, more deterministic loss recovery.

### Ghost ACK Issues
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tcpm-ghost-ack-issues-01 | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### The Session Recovery (SR) Option
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tcpm-the-session-recovery-sr-option-01 | video: https://youtu.be/XRBR6ORihRs | materials: https://datatracker.ietf.org/meeting/127/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

## Working Group: teas

### Applicability of IETF-Defined Service and Network Data Models for Network Slice Service Management
Draft: draft-ietf-teas-ns-models-applicability · Working group: teas
Agenda: Draft: draft-ietf-teas-ns-models-applicability
page: https://datatracker.ietf.org/doc/draft-ietf-teas-ns-models-applicability/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessb-04-applicability-of-ietf-defined-service-and-network-data-models-for-network-slice-service-management-00 | video: https://youtu.be/tQRiYo0IcOA | materials: https://datatracker.ietf.org/meeting/127/session/teas
This document describes how IETF-defined YANG data models can be used together to manage RFC 9543 Network Slice Services. It explains how a Network Slice Controller (NSC) translates a customer-facing Network Slice Service request into requests based on network models, such as the L3VPN and L2VPN Network Models, and how these relate to the corresponding service models. The document compares these models against Network Slice Service requirements, identifies gaps, and shows how the models apply in different controller architectures, including multi-domain deployments.

### Applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) for Packet Optical Integration (POI) service assurance
Draft: draft-ietf-teas-actn-poi-assurance · Working group: teas
Agenda: Draft: draft-ietf-teas-actn-poi-assurance-06
page: https://datatracker.ietf.org/doc/draft-ietf-teas-actn-poi-assurance/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessb-05-actn-poi-assurance-00 | video: https://youtu.be/tQRiYo0IcOA | materials: https://datatracker.ietf.org/meeting/127/session/teas
This document extends the analysis of the applicability of Abstraction and Control of Traffic Engineered Networks (ACTN) architecture to Packet Optical Integration (POI) to cover multi-layer service assurance scenarios. Specifically, the ACTN architecture is analyzed to support service assurance for end-to-end IP services such as L2VPN or L3VPN connectivity services, with specific Service Level Agreement (SLA) requirements, through the detection and correlation of failures across the optical and packet layers, done by the relevant Provisioning Network Controller (PNC) in coopearation with the Multi- Domain Service Coordinator (MDSC). Existing IETF protocols and data models are identified for each multi-layer (packet over optical) service assurance scenario with a specific focus on the Multi-Domain Service Coordinator to Provisioning Network Controllers Interface (MPI) in the ACTN architecture.

### ACTN Extensions for Inter-Operator Coordination
Draft: draft-miyatoch-teas-actn-inter-operator-extension · Working group: teas
Agenda: Draft: draft-miyatoch-teas-actn-inter-operator-extension-01
page: https://datatracker.ietf.org/doc/draft-miyatoch-teas-actn-inter-operator-extension/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessb-06-actn-extensions-for-inter-operator-coordination-00 | video: https://youtu.be/tQRiYo0IcOA | materials: https://datatracker.ietf.org/meeting/127/session/teas
This document specifies an extension to the ACTN framework (RFC 8453) that enables coordination between the MDSCs of different operators, so that they can establish and operate end-to-end TE services cooperatively while each operator keeps full control of its own network and keeps its internal details private. As its concrete realization within ACTN, the extension defines the MDSC-MDSC Interface (MMI), a symmetric peer interface between the MDSCs of different operators, in which neither MDSC has authority over the other, and which complements rather than modifies the CMI and the MPI. The extension is independent of the underlying switching technology and applies to packet, optical, and multi-layer TE networks.

### Multipath Traffic Engineering
Draft: draft-kompella-teas-mpte · Working group: teas
Agenda: Drafts: draft-kompella-teas-mpte-04 , draft-kbr-teas-mptersvp-06 , and draft-beeram-teas-yang-mpted-05
page: https://datatracker.ietf.org/doc/draft-kompella-teas-mpte/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessa-07-multipath-traffic-engineering-architecture-rsvp-signaling-and-data-model-01 | video: https://youtu.be/Vc4IbkxnAEA | materials: https://datatracker.ietf.org/meeting/127/session/teas
Shortest path routing offers an easy-to-understand, easy-to-implement method of establishing loop-free connectivity in a network, but offers few other features. Equal-cost multipath (ECMP), a simple extension, uses multiple equal-cost paths between any two points in a network: at any node in a path (really, Directed Acyclic Graph), traffic can be (typically equally) load-balanced among the next hops. ECMP is easy to add on to shortest path routing, and offers a few more features, such as resiliency and load distribution, but the feature set is still quite limited. Traffic Engineering (TE), on the other hand, offers a very rich toolkit for managing traffic flows and the paths they take in a network. A TE network can have link attributes such as bandwidth, colors, risk groups and alternate metrics. A TE path can use these attributes to include or avoid certain links, increase path diversity, manage bandwidth reservations, improve service experience, and offer protection paths. However, TE typically doesn't offer multipathing as the tunnels used to implement TE usually take a single path. This memo proposes multipath traffic-engineering (MPTE), combining the best of ECMP and TE. The multipathing proposed here need not be strictly equal-cost, allowing for some "slack" to admit more paths. The load balancing at each hop is optimally weighted to each next hop rather than always being equally weighted. Moreover, traffic can enter and leave an MPTE construct via multiple ingresses and egresses. The proposal includes several choices of control and data planes.

### RSVP-TE Extensions for Multipath Traffic Engineered Directed Acyclic Graph Tunnels
Draft: draft-kbr-teas-mptersvp · Working group: teas
Agenda: Drafts: draft-kompella-teas-mpte-04 , draft-kbr-teas-mptersvp-06 , and draft-beeram-teas-yang-mpted-05
page: https://datatracker.ietf.org/doc/draft-kbr-teas-mptersvp/ | materials: https://datatracker.ietf.org/meeting/127/session/teas
A Multipath Traffic Engineered Directed Acyclic Graph (MPTED) tunnel is a Traffic Engineering (TE) construct that facilitates weighted load balancing of unicast traffic across a constrained set of paths optimized for a specific objective. This document describes the provisioning of an MPTED tunnel in a TE network using RSVP-TE.

### A YANG Data Model for Multipath Traffic Engineering Directed Acyclic Graph (MPTED) Tunnels and Junctions
Draft: draft-beeram-teas-yang-mpted · Working group: teas
Agenda: Drafts: draft-kompella-teas-mpte-04 , draft-kbr-teas-mptersvp-06 , and draft-beeram-teas-yang-mpted-05
page: https://datatracker.ietf.org/doc/draft-beeram-teas-yang-mpted/ | materials: https://datatracker.ietf.org/meeting/127/session/teas
This document defines a YANG data model for representing, retrieving, and manipulating Multipath Traffic Engineering Directed Acyclic Graph (MPTED) tunnels and junctions. The model includes two YANG modules, one for managing MPTED tunnels on an MPTED tunnel originator node and the other for managing MPTED junctions on an MPTED junction node.

### RSVP-TE Resource Notifications
Draft: draft-beeram-teas-rsvp-resource-notifications · Working group: teas
Agenda: Draft: draft-beeram-teas-rsvp-resource-notifications-00
page: https://datatracker.ietf.org/doc/draft-beeram-teas-rsvp-resource-notifications/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessa-08-rsvp-te-resource-notifications-00 | video: https://youtu.be/Vc4IbkxnAEA | materials: https://datatracker.ietf.org/meeting/127/session/teas
In scaled Resource Reservation Protocol - Traffic Engineering (RSVP- TE) networks, a single network resource event (such as a link failure or bandwidth reduction) can trigger a storm of PathErr messages, one for each affected Label Switched Path (LSP). This document introduces RSVP Resource Notifications, a mechanism that reduces the number of per-LSP error messages by sending summarized per-source resource-level notifications in a new RSVP message, ResourceNotify. This reduces the control-plane message load from O(LSPs) to O(sources), significantly improving convergence in networks with a large number of RSVP-TE LSPs. The mechanism applies to LSPs whose source is reachable by the transit node within the same domain, and uses a Resource Notification Request Object carried in PATH messages. Two types of resource notifications are defined in this document: Resource Unavailable (for link failures) and Resource Degraded (for bandwidth reduction events).

### Power Transition Framework for TE Resources
Draft: draft-many-teas-rsvp-power · Working group: teas
Agenda: Draft: draft-many-teas-rsvp-power-00
page: https://datatracker.ietf.org/doc/draft-many-teas-rsvp-power/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessa-10-power-transition-framework-for-te-resources-00 | video: https://youtu.be/Vc4IbkxnAEA | materials: https://datatracker.ietf.org/meeting/127/session/teas
Traffic-engineered networks are commonly provisioned for peak demand. However, during off-peak periods, some traffic-engineered resources in the network may be lightly used. This leads to unnecessary power consumption. A coordinated power transition can reduce power consumption while preserving the control-plane and traffic- engineering state needed to restore service safely. This document defines a generic power management framework for coordinating power-sleep and wakeup transitions between adjacent nodes. It defines the roles, resource scope, procedures, collision handling, failure behavior, and traffic-engineering preservation requirements. It then specifies an RSVP-TE signaling extension for supporting the power management framework.

### An Architecture for Distributed Bandwidth Management Using TE Tunnels and Policies
Draft: draft-smjh-teas-dist-bw-mgmt-arch · Working group: teas
Agenda: Draft: draft-smjh-teas-dist-bw-mgmt-arch-00
page: https://datatracker.ietf.org/doc/draft-smjh-teas-dist-bw-mgmt-arch/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessa-11-an-architecture-for-distributed-bandwidth-management-using-te-tunnels-and-policies-00 | video: https://youtu.be/Vc4IbkxnAEA | materials: https://datatracker.ietf.org/meeting/127/session/teas
Traffic Engineering (TE) deployments steer traffic over provisioned TE constructs and associate bandwidth with them. Examples include point-to-point and point-to-multipoint (P2MP) Resource Reservation Protocol - Traffic Engineering (RSVP-TE) tunnels, Segment Routing (SR) Policies, and Multipath TE (MPTE) constructs that are provisioned as directed acyclic graphs (DAGs). As demand changes, operators automatically resize the bandwidth allocated to each construct based on measured traffic, a function commonly called auto- bandwidth, but no common description of this practice exists across TE technologies. This document defines an architecture for distributed bandwidth management, in which the originator of each TE construct evaluates and adjusts its bandwidth without central coordination, and can offload computation and bandwidth estimation to an external entity. The architecture is independent of the forwarding plane and assumes a signaling plane, such as RSVP-TE, that provides per-link bandwidth accounting, admission control, and preemption. It covers traffic measurement, bandwidth estimation, adjustment, periodic and event- driven evaluation, and the management of a service carried by multiple concurrently usable tunnels (Container Tunnel management). Technology-specific signaling, data models, path computation, and estimation algorithms are outside its scope. This document defines no new protocol extension or wire encoding.

### Problem Statement and Gap Analysis of Fine-Grained QoS Assurance for 6G Scenarios
Draft: draft-miao-teas-6g-fine-grained-qos-gap-analysis · Working group: teas
Agenda: Draft: draft-miao-teas-6g-fine-grained-qos-gap-analysis-00
page: https://datatracker.ietf.org/doc/draft-miao-teas-6g-fine-grained-qos-gap-analysis/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessa-12-problem-statement-and-gap-analysis-of-fine-grained-qos-assurance-for-6g-scenarios-00 | video: https://youtu.be/Vc4IbkxnAEA | materials: https://datatracker.ietf.org/meeting/127/session/teas
The evolution toward 6G introduces demanding applications such as holographic communications, tactile internet, digital twins, and semantic communications, which may require fine-grained, per-packet Quality of Service (QoS) assurance. In these scenarios, 5QI may continue to be useful, but it may also need to be complemented by richer service QoS requirement information. Meanwhile, transport networks have developed powerful QoS technologies including FlexE hard slicing, Deterministic Networking (DetNet), Time-Sensitive Networking (TSN), and SRv6 Traffic Engineering policies, enabling per-packet scheduling precision at microsecond levels. However, several gaps remain. First, while 6G scenarios may require richer service QoS requirement information, current IP transport networks still rely on DSCP as the QoS handling mechanism. This could underutilize many effective fine-grained QoS assurance mechanisms already available in transport networks. Second, transport networks lack service-aware perception of upper-layer application attributes. Third, there is no cross-domain information synchronization mechanism between radio access and transport segments, preventing the formation of an end-to-end, full-link QoS assurance mechanism for 6G. This document provides a gap analysis structured around three core gaps: (1) the potential need to complement 5QI with richer service QoS requirement information for 6G and the potential underutilization of fine-grained transport QoS mechanisms due to continued reliance on DSCP in IP transport; (2) lack of service awareness in transport; and (3) missing cross-domain information exchange for end-to-end 6G full- link QoS assurance.

### Signaling RSVP-TE Tunnels on an SRv6 Forwarding Plane Using End.X Segment Identifiers
Presentation · Working group: teas
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-teas-sessa-09-signaling-rsvp-te-tunnels-on-an-srv6-forwarding-plane-using-endx-segment-identifiers-01 | video: https://youtu.be/Vc4IbkxnAEA | materials: https://datatracker.ietf.org/meeting/127/session/teas
Slides presented at the teas session; no Internet-Draft is linked to them.

## Working Group: tls

### The Datagram Transport Layer Security (DTLS) Protocol Version 1.3
Draft: draft-ietf-tls-rfc9147bis · Working group: tls
Agenda: draft-ietf-tls-rfc9147bis
page: https://datatracker.ietf.org/doc/draft-ietf-tls-rfc9147bis/ | materials: https://datatracker.ietf.org/meeting/127/session/tls
This document specifies version 1.3 of the Datagram Transport Layer Security (DTLS) protocol. DTLS 1.3 allows client/server applications to communicate over the Internet in a way that is designed to prevent eavesdropping, tampering, and message forgery. The DTLS 1.3 protocol is based on the Transport Layer Security (TLS) 1.3 protocol and provides equivalent security guarantees with the exception of order protection / non-replayability. Datagram semantics of the underlying transport are preserved by the DTLS protocol. This document obsoletes RFC 6347.

### TLS Trust Anchor Identifiers
Draft: draft-ietf-tls-trust-anchor-ids · Working group: tls
Agenda: draft-ietf-tls-trust-anchor-ids
page: https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-trust-anchor-ids-00 | video: https://youtu.be/diDKZuSn--M | materials: https://datatracker.ietf.org/meeting/127/session/tls
This document defines the TLS Trust Anchors extension, a mechanism for a TLS client or server to select a certificate to present based on the peer's trusted certification authorities. It describes certification authorities more succinctly than the TLS Certificate Authorities extension.

### A Password Authenticated Key Exchange Extension for TLS 1.3
Draft: draft-ietf-tls-pake · Working group: tls
Agenda: draft-ietf-tls-pake
page: https://datatracker.ietf.org/doc/draft-ietf-tls-pake/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-a-password-authenticated-key-exchange-extension-for-tls-13-00 | video: https://youtu.be/diDKZuSn--M | materials: https://datatracker.ietf.org/meeting/127/session/tls
The pre-shared key mechanism available in TLS 1.3 is not suitable for usage with low-entropy keys, such as passwords entered by users. This document describes an extension that enables the use of password-authenticated key exchange protocols with TLS 1.3.

### Extended Key Update for Transport Layer Security (TLS) 1.3
Draft: draft-ietf-tls-extended-key-update · Working group: tls
Agenda: draft-ietf-tls-extended-key-update
page: https://datatracker.ietf.org/doc/draft-ietf-tls-extended-key-update/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-sessa-extended-key-update-for-tls-13-00 | video: https://youtu.be/INPphAvqSQE | materials: https://datatracker.ietf.org/meeting/127/session/tls
TLS 1.3 ensures forward secrecy by performing an ephemeral Diffie- Hellman key exchange during the initial handshake, protecting past communications even if a party's long-term keys (typically a private key with a corresponding certificate) are later compromised. While the built-in KeyUpdate mechanism allows application traffic keys to be refreshed during a session, it does not incorporate fresh entropy from a new key exchange and therefore does not provide post- compromise security. This limitation can pose a security risk in long-lived sessions, such as those found in industrial IoT or telecommunications environments. To address this, this specification defines an extended key update mechanism that performs a fresh execution of the key exchange negotiated during the initial handshake within an active session to support post-compromise security. By forcing attackers to exfiltrate new key material repeatedly, this approach mitigates the risks associated with static key compromise. Regular renewal of session keys helps contain the impact of such compromises. The extension is applicable to both TLS 1.3 and DTLS 1.3.

### Use of Composite ML-DSA in TLS 1.3
Draft: draft-ietf-tls-composite-mldsa · Working group: tls
Agenda: draft-ietf-tls-composite-mldsa
page: https://datatracker.ietf.org/doc/draft-ietf-tls-composite-mldsa/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-sessa-composite-ml-dsa-in-tls-13-00 | video: https://youtu.be/INPphAvqSQE | materials: https://datatracker.ietf.org/meeting/127/session/tls
Compositing the post-quantum ML-DSA signature with traditional signature algorithms provides protection against potential breaks or critical bugs in ML-DSA or the ML-DSA implementation. This document specifies how such a composite signature can be formed using ML-DSA with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide authentication in TLS 1.3, including use in certificates.

### Secondary Client Authentication in TLS 1.3
Draft: draft-rosomakho-tls-secondary-client-auth · Working group: tls
Agenda: draft-rosomakho-tls-secondary-client-auth
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-secondary-client-auth/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-sessa-secondary-client-authentication-00 | video: https://youtu.be/INPphAvqSQE | materials: https://datatracker.ietf.org/meeting/127/session/tls
Some deployments authenticate a client using two certificates, such as one identifying a device and another identifying its user. This document defines the secondary_client_certificate TLS flag to negotiate one additional client authentication exchange as part of connection establishment. The server sends an additional CertificateRequest immediately after its Finished, and the client responds after its own handshake Finished and before sending application data. Either certificate response can be empty, and the server determines whether the resulting authentication state satisfies its policy. This document updates RFC 9846 to permit the additional request before the server receives the client's Finished. It also updates RFCs 9001 and 9113 to permit this negotiated exchange with QUIC and HTTP/2.

### An HSTS-like Header for Secure PQ Migration
Draft: draft-sheffer-tls-pq-hsts · Working group: tls
Agenda: draft-sheffer-tls-pq-hsts
page: https://datatracker.ietf.org/doc/draft-sheffer-tls-pq-hsts/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-sessa-pq-hsts-00 | video: https://youtu.be/INPphAvqSQE | materials: https://datatracker.ietf.org/meeting/127/session/tls
This document defines an HTTP response header field, Require-PQ-Auth, that instructs user agents to require a quantum-resistant certificate chain in subsequent connections. This is a short-term, opt-in mechanism for HTTP origins to protect against legacy classical trust anchors. It will become unnecessary when UAs remove these trust anchors.

### XOF-based key schedules for TLS 1.3
Draft: draft-sullivan-tls-xof-schedule · Working group: tls
Agenda: draft-sullivan-tls-xof-schedule
page: https://datatracker.ietf.org/doc/draft-sullivan-tls-xof-schedule/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-sessa-one-xof-for-the-whole-tls-13-key-schedule-00 | video: https://youtu.be/INPphAvqSQE | materials: https://datatracker.ietf.org/meeting/127/session/tls
TLS 1.3 runs its entire key schedule on HKDF over SHA-2. This document defines an extension that replaces that schedule with one built on an extendable-output function (XOF): the negotiated KDF governs every derivation, the Finished and binder MACs, and the transcript hash, so no SHA-2 remains in the key schedule. The cipher suites, AEAD algorithms, state machine, and record layer are unchanged, and a connection without the extension uses HKDF as today. Two KDFs are defined, SHAKE256 and the reduced-round TurboSHAKE256. This document updates RFC 9147, RFC 9258, RFC 9261, and RFC 9849.

### Workload Identifier Origin Hint for TLS ClientHello
Draft: draft-rosomakho-tls-wimse-cert-hint · Working group: tls
Agenda: draft-rosomakho-tls-wimse-cert-hint
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-workload-identifier-origin-hint-00 | video: https://youtu.be/diDKZuSn--M | materials: https://datatracker.ietf.org/meeting/127/session/tls
This document defines a TLS extension that allows clients to indicate one or more workload identifier origins in the ClientHello message. Each origin consists of a URI scheme and trust domain component, representing the administrative domain and identifier namespace in which the client operates. These identifier origins serve as hints to enable the server to determine whether client authentication is required and which policies or trust anchors should apply. This mechanism improves efficiency in mutual TLS deployments while minimising the exposure of sensitive identifier information. To protect confidentiality, this extension can be used in conjunction with Encrypted Client Hello (ECH).

### DTLS 1.3 ClientHello Fragmentation
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tls-dtls-13-clienthello-fragmentation-00 | video: https://youtu.be/diDKZuSn--M | materials: https://datatracker.ietf.org/meeting/127/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

## Working Group: tsvwg

### Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-ietf-tsvwg-sctp-dtls-chunk · Working group: tsvwg
Agenda: SCTP/DTLS progress and actions required - Magnus (20 min) - https://www.ietf.org/archive/id/draft-ietf-tsvwg-sctp-dtls-chunk-06.html and https://www.ietf.org/archive/id/draft-porfiri-tsvwg-sctp-dtls-h
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-dtls-protected-sctp-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
This document describes a method for adding Datagram Transport Layer Security (DTLS) based authentication and cryptographic protection to the Stream Control Transmission Protocol (SCTP). This SCTP extension is intended to enable communication privacy for applications that use SCTP as their transport protocol and allows applications to communicate in a way that is designed to prevent eavesdropping and detect tampering or message forgery. Once enabled, this also applies to the SCTP payload as well as the SCTP control information. Applications using this SCTP extension can use most of the transport features provided by SCTP and its other extensions. The use of the SCTP Authentication extension defined in RFC 4895 is incompatible with the extension defined in this document but would not provide any additional service. This implies that the Dynamic Address Reconfiguration as specified in RFC 5061 can only be used as described in this document. This document obsoletes RFC 6083 and updates RFC 5061.

### Transport Layer Security (TLS) based Key Management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-porfiri-tsvwg-sctp-dtls-handshake · Working group: tsvwg
Agenda: SCTP/DTLS progress and actions required - Magnus (20 min) - https://www.ietf.org/archive/id/draft-ietf-tsvwg-sctp-dtls-chunk-06.html and https://www.ietf.org/archive/id/draft-porfiri-tsvwg-sctp-dtls-h
page: https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/ | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
This document defines how Transport Layer Security (TLS) 1.3 is used as a key management method for the SCTP DTLS Chunk mechanism. It specifies how a TLS handshake establishes the initial security context for an SCTP association and how subsequent TLS handshakes provide key updates and re-authentication. The goal is to enable authenticated and confidential communication over SCTP using the DTLS Chunk, leveraging standardized TLS 1.3 features for key management and rekeying.

### Static Rate Management (SRM) for Low Latency, Low Loss, and Scalable Throughput (L4S)
Draft: draft-deschepper-tsvwg-srm · Working group: tsvwg
Agenda: Static Rate Management (SRM) for Low Latency, Low Loss, and Scalable Throughput (L4S) - Miroslav Vrana (20 min) - https://www.ietf.org/archive/id/draft-deschepper-tsvwg-srm-00.html
page: https://datatracker.ietf.org/doc/draft-deschepper-tsvwg-srm/ | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
This document describes the Static Rate Management (SRM) solution for L4S (Low Latency, Low Loss, Scalable Throughput) rate control. SRM utilizes a Two-Rate, Three-Color Marker (trTCM) policer in conjunction with a dual-queue mechanism to provide low latency and low loss for L4S flows in environments where a fixed, safe rate can be reliably defined for a network link or segment. This approach offers an alternative to Active Queue Management (AQM)-based L4S solutions, particularly for high-speed and aggregated networks with limited packet processing capabilities. This document details the operation, advantages, disadvantages, and configuration guidelines for SRM.

### 443 is Enough: Guidance on Port Allocation for HTTP-based Services
Draft: draft-trammell-tsvwg-443-is-enough · Working group: tsvwg
Agenda: Guidance on Port Allocation for HTTP-based Services - Brian Trammell (10 min) - https://www.ietf.org/archive/id/draft-trammell-tsvwg-443-is-enough-00.html
page: https://datatracker.ietf.org/doc/draft-trammell-tsvwg-443-is-enough/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-443-is-enough-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
[RFC7605] provides guidance on the use of port numbers and the criteria for new port assignments, including a test for whether a proposed service is distinct from an existing service. It gives the example that "an automated system that happens to use HTTP framing -- but is not primarily accessed by a browser -- might be a new service." It also might not. This document clarifies the application of the distinct-protocol test in [RFC7605] Section 7.1 to services built on HTTP as a substrate, in light of HTTP's evolution since its publication, and provides guidance to applicants and reviewers on when an HTTP-based service qualifies for a new port assignment and when it does not.

### TCP and UDP checksum calculations for ILNP
Draft: draft-bhatti-ilnp-tcp-udp-checksums · Working group: tsvwg
Agenda: TCP and UDP checksum calculations for ILNP - Saleem Bhatti (15 min) - https://www.ietf.org/archive/id/draft-bhatti-ilnp-tcp-udp-checksums-00.html
page: https://datatracker.ietf.org/doc/draft-bhatti-ilnp-tcp-udp-checksums/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-tcp-and-udp-checksum-calculations-for-ilnp-01 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
The Identifier Locator Network Protocol (ILNP) for IPv6 is described in Experimental RFCs 6740-6744. ILNP defines the use of an Identifier-Locator Vector (I-LV) with a zero value L64 value and a relevant Node Identifier (NID) value in place of an IPv6 address in the pseudo-header for transport protocol checksum computations. However, as TCP and UDP predate ILNP, this change causes TCP and UDP checksum values to be generated for ILNP flows that are different to the same flows on IPv6. This document changes the checksum computation for TCP and UDP with ILNP so that the checksum values are the same for ILNP and IPv6. This document updates the checksum processing for TCP and UDP described in RFC6740 and RFC6741, and the way the checksum processing should be applied for TCP and UDP in RFC6748.

### SCTP Negotiation Acceleration Protocol
Draft: draft-hancke-tsvwg-snap · Working group: tsvwg
Agenda: SCTP Negotiation Acceleration Protocol (SNAP) for WebRTC - Philipp Hancke (05 min) https://www.ietf.org/archive/id/draft-hancke-tsvwg-snap-01.html
page: https://datatracker.ietf.org/doc/draft-hancke-tsvwg-snap/ | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
WebRTC Data Channels use the Stream Control Transmission Protocol (SCTP) over a Datagram Transport Layer Security (DTLS) association. The standard SCTP connection establishment requires a handshake that introduces latency. This document specifies a method to accelerate the datachannel establishment by embedding the SCTP initialization parameters within the Session Description Protocol (SDP) offer/answer exchange. This reduces the time required to open a data channel by up to two network round-trip times.

### Current State of the Art for High Performance Wide Area Networks
Draft: draft-kcrh-hpwan-state-of-art · Working group: tsvwg
Agenda: HPWAN - state-of-art: heads-up before AD-sponsored publication- Daniel King (05 min) https://www.ietf.org/archive/id/draft-kcrh-hpwan-state-of-art-04.html
page: https://datatracker.ietf.org/doc/draft-kcrh-hpwan-state-of-art/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-hpwan-state-of-art-heads-up-before-ad-sponsored-publication-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
High Performance Wide Area Networks (HP-WANs) provide infrastructure for the modern global Research and Education (R&E) community, facilitating collaboration across national and international boundaries. These networks include global education and research networks, such as GÉANT, Internet2, Janet, ESnet, CANARIE, CERNET, and others, and also refer to large-scale commercial dedicated networks built by hyperscalers and operators. They are designed to support the transfer of data generated by scientific research, high- performance computing, distributed AI-training, and large-scale simulations. This document provides an overview of the terminology and techniques used for existing HP-WANs. It also explores the technological advancements, operational tools, and future directions for HP-WANs, including their use in scientific research, AI training, and large- scale R&E data analysis.

### Controlling IP Fragmentation on Common Platforms
Draft: draft-seemann-tsvwg-udp-fragmentation · Working group: tsvwg
Agenda: Controlling IP Fragmentation on Common Platforms - Marten Seemann (05 min) https://www.ietf.org/archive/id/draft-seemann-tsvwg-udp-fragmentation-03.html
page: https://datatracker.ietf.org/doc/draft-seemann-tsvwg-udp-fragmentation/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-udp-fragmentation-01 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
When performing Path MTU Discovery (PMTUD) over UDP, applications must prevent fragmentation of UDP datagrams both by the sender's kernel and during network transit. This document provides guidance for implementers on configuring socket options to prevent fragmentation of IPv4 and IPv6 packets across commonly used platforms.

### SNAP updates
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-snap-updates-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### QUIC Transport Parameters and protocol designer thoughts
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-quic-transport-parameters-and-protocol-designer-thoughts-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### Android TCP receive-side L4S
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-android-tcp-receive-side-l4s-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### SRM for L4S
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-srm-for-l4s-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### L4S in Cellular Networks
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-l4s-in-cellular-networks-00 | video: https://youtu.be/QFShsZT5rkk | materials: https://datatracker.ietf.org/meeting/127/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

## Working Group: v6ops

### Basic Requirements for IPv6 Customer Edge Routers
Draft: draft-ietf-v6ops-rfc7084bis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/ | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document specifies requirements for an IPv6 Customer Edge (CE) router. Specifically, the current version of this document focuses on the basic provisioning of an IPv6 CE router and the provisioning of IPv6 hosts attached to it. The document obsoletes RFC 7084.

### Using Dummy IPv4 Address and Node Identification Extensions for IP/ICMP translators (XLATs)
Draft: draft-ietf-v6ops-icmpext-xlat-v6only-source · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-icmpext-xlat-v6only-source/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-icmpext-xlat-v6only-source/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-using-dummy-ipv4-address-and-node-identification-extensions-for-ipicmp-translators-xlats-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document suggests that when a source IPv6 address of an ICMPv6 message can not be translated to an IPv4 address, and the protocol translator does not have any public IPv4 addresses available to source the translated packet from, the translator uses the dummy IPv4 address (192.0.0.8) to translate the IPv6 source address. This document updates RFC6791, Stateless Source Address Mapping for ICMPv6 Packets, and RFC7915, IP/ICMP Translation Algorithm, by proposing to utilize the ICMP extension for Node Identification (draft-ietf- intarea-extended-icmp-nodeid) to carry the original IPv6 source address of ICMPv6 messages.

### Considerations of IPv6-only Deployment in 5G Mobile Networks
Draft: draft-ietf-v6ops-5g-ipv6only · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-5g-ipv6only/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-5g-ipv6only/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-03-chenhao-ma-considerations-of-ipv6-only-deployment-in-5g-mobile-networks-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document describes a practical guide of deploying 464XLAT based IPv6-only technology on user plane in 3GPP 5G networks. It also covers key 5G concepts and architectures, configuration methods and operational challenges.

### A recommendation for filtering address records in stub resolvers
Draft: draft-ietf-v6ops-aaaa-filtering · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-aaaa-filtering/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-aaaa-filtering/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-04-jen-linkova-aaaa-filtering-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
Since IPv4 and IPv6 addresses are represented by different resource records in the Domain Name System, operating systems capable of running both IPv4 and IPv6 need to execute two queries when resolving a host name. This document discusses the conditions under which a stub resolver can optimize the process by not sending one of the queries if the host is connected to a single-stack network.

### Enhanced Dual Stack: Connection-Informed IPv6/IPv4 Selection
Draft: draft-xiao-v6ops-eds · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/
page: https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/ | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document describes Enhanced Dual Stack (EDS), a framework intended to reduce the operational risk and upfront workload of introducing IPv6 into existing IPv4 networks. EDS provides a connection-informed method for implementing RFC 6724 Rule 1, "Avoid unusable destinations", by remembering recent TCP/QUIC connection- establishment failures and avoiding repeated selection of affected IPv6 destinations. It also provides operational diagnostics so administrators can identify and correct IPv6 problems. EDS is complementary to Happy Eyeballs and does not require connection racing. By starting with selected EDS-capable pioneer hosts, performing practical validation, and expanding IPv6 gradually, EDS can be deployed incrementally without requiring all hosts to support EDS. With EDS, enterprises' IPv6 introduction can change from a heavy upfront validation process toward an incremental improvement process.

### First Hop Redundancy in IPv6 Networks: Operational Considerations
Draft: draft-calink-v6ops-fhrd · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-calink-v6ops-fhrd/
page: https://datatracker.ietf.org/doc/draft-calink-v6ops-fhrd/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-06-first-hop-redundancy-in-ipv6-networks-operational-considerations-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document provides operational guidance for configuring first-hop routers and first-hop redundancy in IPv6 networks. It also discusses design choices for improving recovery time after a renumbering event.

### Considerations for Happy Eyeballs Error Reporting
Draft: draft-palet-happy-reporting-considerations · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-palet-happy-reporting-considerations/
page: https://datatracker.ietf.org/doc/draft-palet-happy-reporting-considerations/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-07-philipp-happy-eyeballs-reporting-considerations-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document introduces different aspects to be considered for the Happy Eyeballs error reporting.

### IPv6 Deployment Statistics and Analysis
Draft: draft-pang-v6ops-ipv6-deployment-stats-analysis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-deployment-stats-analysis/
page: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-deployment-stats-analysis/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-08-jingzhao-ipv6-deployment-statistics-and-analysis-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
This document explains why existing observations of IPv6 deployment are often insufficient to identify the operational gaps and bottlenecks that limit IPv6 utilization and service quality. It describes the need for correlated analysis across different parts of the service path and discusses examples of statistical evidence that can support such analysis.

### IPv6 Path Performance Degradation in Dual-Stack Networks
Draft: draft-pang-v6ops-ipv6-path-degradation · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/html/draft-pang-v6ops-ipv6-path-degradation-00
page: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-path-degradation/ | slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-08-jingzhao-ipv6-path-performance-degradation-in-dual-stack-networks-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
The document analyzes contributing factors across the content service layer and the network transport layer, and discusses why existing mechanisms such as RFC 6724 and Happy Eyeballs do not fully address performance failures that appear after connection establishment. This document is limited to problem analysis, scope clarification, and areas for further study. It does not define new network-to-host signaling mechanisms or require hosts to use network-provided information when making address-family or path selection decisions.

### 7084bis
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-7084bis-00 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Xipeng - Enhanced Dual Stack EDS
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/127/materials/slides-127-v6ops-05-xipeng-enhanced-dual-stack-eds-01 | video: https://youtu.be/bsQV2o5noZ4 | materials: https://datatracker.ietf.org/meeting/127/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

