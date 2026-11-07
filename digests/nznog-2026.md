<!--
conference: NZNOG 2026
type: operator
source_url: https://www.nznog.org/conferences/nznog-2026/talks.html
generated: 2026-11-04
registry_key: nznog-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NZNOG 2026

A small, operator-heavy program (22 talks). Notable: none of the items carry paper or slide links in the material provided, so every write-up below is based on the program abstracts only. Tiers reflect the PM's core interests (physical DC/optics, cloud-native networking, network security, identity) with an operator-program lens: postmortems and adoptable tooling up-ranked, pitches down-ranked.

## Core

### Radius Futures

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=3490s)

Alan DeKok

- **Why**: RADIUS is still the default AAA protocol for network access (802.1X, Wi-Fi, VPN) and sits squarely in the PM's identity/authentication territory. Its 1993 design shows its age — known operational and security pain points — and "next-generation" standards work determines how network AAA coexists with modern identity stacks (OIDC, passkeys, workload identity).
- **What**: A survey of real-world problems affecting RADIUS deployments, and how emerging next-generation RADIUS standards can reduce them (from abstract only).
- **How**: Protocol-level standards evolution rather than a product; the abstract does not enumerate the specific extensions, so expect the detail to be in the talk itself.
- **Where applicable**: Broadly applicable — any operator or enterprise running AAA today. Protocol work, not vendor-specific. The main caveat is that the abstract stays high level; the value depends on which concrete drafts/problems get named.

### Evolving Optical Transport: 400G, Network Design, and Regional Diversity

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=9259s)

Abouzar Asadi (Chorus)

- **Why**: Coherent optics and line-system evolution are core to the PM's physical DC/WAN interconnect interests. A nationwide 400G rollout on NZ's largest open-access fibre network is one of the few talks here with real optical engineering content: line-system readiness, spectrum management, transceiver evolution, and ring diversity/protection.
- **What**: The engineering journey to 400 Gbps nationwide on Chorus's network — what had to be true about the optical line system before 400G could ride it, how spectrum is managed, and how regional fibre rings are designed for diversity and protection (from abstract only).
- **How**: Advances in coherent modulation and digital signal processing plus open optical architectures; diverse ring design and protection strategies for resiliency and service continuity.
- **Where applicable**: Chorus/NZ-specific deployment, but the engineering content (line-system readiness for higher baud, spectrum planning, ring protection) transfers directly to any long-haul or metro optical operator. Watch for whether the "open optical" framing stays vendor-neutral.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=1905s)

Thomas Weible

- **Why**: Planning DWDM channel grids for the 400G → 800G → 1.6T superchannel era is exactly the kind of physical-layer topology tradeoff the PM cares about — this is about how fibre capacity and reconfigurability interact over a 10+ year horizon.
- **What**: An argument for moving to 400GHz channel grids: how the shift from narrow grids (200/100/50/25GHz) to wide-grid superchannels changes topology economics, how coherent detection being "blind" to anything but its own wavelength enables filterless designs, and how to keep legacy ≤10G signals coexisting on the same fibre pair while avoiding expensive ROADMs (from abstract only).
- **How**: Wider fixed-grid (400GHz) filters plus coherent transceivers' tolerance of unfiltered neighbours: harvest filterless-topology cost benefits while retaining the flexibility to reassign bandwidth and carry legacy wavelengths.
- **Where applicable**: Any DWDM operator with long-haul or metro infrastructure planning a decade out. The tradeoff is explicit — reduced flexibility vs. cost — and the "keep 10G and below on the same fibre" constraint matters for networks with legacy OTN payloads. The talk may carry a vendor perspective; the physics and grid economics are general.

### Options for Data Centre Interconnect

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=45s)

Matthew Hayes

- **Why**: DCI is a named core interest, and NZ/ANZ is seeing genuine DC-to-DC demand growth from hyperscaler and AI service buildout. A structured comparison of DCI approaches is directly useful for interconnect planning.
- **What**: A survey of common DCI approaches, from physical-layer solutions (fibre/DWDM) to higher-layer technologies, with how each works and the pros and cons of each, framed by ANZ market dynamics (from abstract only).
- **How**: Comparative walkthrough of interconnect models rather than a single solution — the abstract does not name the specific technologies, so the depth depends on the talk.
- **Where applicable**: DC operators and interconnect providers generally; not org-specific. Likely most valuable as a decision framework for choosing between dark-fibre/own-optics versus higher-layer managed options at different distance/capacity points.

### Experiments in Topology Visualization using BGP-LS (RFC-8571)

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=11173s)

Rick Williamson (Helios Software AU), Rob Simpson (Kordia Networks)

- **Why**: BGP-LS is an underused source of live topology and TE data, and this is exactly the kind of experimental, adoptable tooling an operator program should surface. It ties directly to the PM's BGP/datapath-internals interest and offers hands-on access (remote lab network, iOS visualisation client) during the conference.
- **What**: An experimental journey using BGP-LS as a practical live source of topology and traffic-engineering data for visualisation — started in a greenfields Public Safety Network, evolved into an approach suitable for organically grown operational networks (from abstract only).
- **How**: BGP-LS (RFC 8571) exposes IGP link-state and TE information into BGP; a client consumes that feed to drive visual SPF computation and "what-if" simulations. The demo shows how link-state changes, failures, and metric adjustments propagate through BGP-LS in real time. They also outline a low-risk path for operators to trial BGP-LS in their own environments.
- **Where applicable**: Broadly applicable to heterogeneous, organically grown networks running IGP + BGP — which is most of them. The greenfields origin is noted but the authors explicitly generalised it. The offer of lab/client access makes this the most immediately try-it-yourself talk in the program.

### Using Open Rack V3 to Enhance your Data Centre Infrastructure

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=18434s)

Conrad Bullock

- **Why**: Rack-level power, thermal, and mechanical standards are what make high-density AI/HPC fabrics physically possible — ORv3 (and OCP generally) is core physical-DC infrastructure territory, not adjacent to it. The NZ case study gives local grounding.
- **What**: How the OCP Open Rack V3 standard improves efficiency, thermal management, and rack density, translating to lower opex, better cooling for high-density computing, and simplified maintenance — plus a New Zealand customer deployment case study with "real benefits" (from abstract only).
- **How**: ORv3's modularity and standardised rack infrastructure supporting AI/HPC workloads and future scalability; the abstract does not detail the specific mechanisms (busbars, power levels, blind-mate designs), so the depth is in the talk.
- **Where applicable**: DC operators building or refreshing high-density halls. The abstract's tone is promotional and the speaker's affiliation is not given, so assess on the day for vendor-pitch content — the case study is the part worth weighing.

### Automated Network State Checking: Insights from the Field

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=18910s)

Joe Shaw (REANNZ)

- **Why**: This is the best operational postmortem-style talk in the program: a full domestic-backhaul hardware refresh where *every* service had to be rehomed with evidence of continuity — and the response was to build a generalised, model-driven verification system rather than hand-check services. Deeply transferable to anyone doing migrations.
- **What**: REANNZ developed a generalised service model plus Python automation that reasons from live network data: it generated new configuration consistent with the new hardware and produced clear old-vs-new running-state comparisons at implementation time, iterated until it could verify even highly bespoke configurations. The talk demonstrates the system with case studies and the challenges overcome (from abstract only).
- **How**: A generalised service model driven off live network state (not hand-catalogued per-service checks), automated config generation, and diff-style continuity evidence produced at cutover — a closed feedback loop between intent, generation, and verification.
- **Where applicable**: REANNZ's R&E network context is specific, but the technique is general: any operator facing a hardware refresh, architecture change, or migration where per-service manual verification doesn't scale. Particularly relevant wherever bespoke legacy configurations make off-the-shelf assurance tools insufficient.

## Adjacent

### The Evolution of TCP Transport Protocols

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=6375s)

Geoff Huston

- **Why**: Congestion-control fundamentals cut across everything the PM touches — from lossless/DC fabrics to internet transport — and the shift from loss-based control to BBR (with ECN being reconsidered) changes how buffers should be sized and how traffic behaves on your network.
- **What**: A look at the fundamental feedback-loop problem in packet networking: various TCP flow control protocols, their relationship with network buffers, the reconsideration of explicit congestion notification, and the growth of BBR (from abstract only).
- **How**: Analysis of the design space of sender/receiver feedback loops — loss-based, delay/ECN-based, and model-based (BBR) — and how each interacts with buffer sizing in the network.
- **Where applicable**: Universal — every operator's queue/buffer behaviour is affected. Especially relevant as BBR-driven senders (large content/CDN players) increasingly set the tone for how paths are used.

### Optimizing Traffic Flow with Akamai

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=389s)

Kams Yeung

- **Why**: The core insight — that classic BGP traffic engineering (AS-path prepending, MED, more-specifics) is largely *ineffective* against a large CDN's intelligent routing — is a practical lesson for any operator peering with CDNs, and the remediation list is concrete.
- **What**: How Akamai's CDN is structured in NZ and maps traffic, why traditional BGP TE fails against it, and a set of operator best practices: dedicated DNS resolvers, complete and consistent route announcements, avoiding traffic filtering, avoiding CGNAT, and adopting IPv6 (from abstract only).
- **How**: CDN-side intelligence (mapping/routing) responds to reachability and resolver signals rather than BGP path metrics — so operators influence delivery through routing hygiene, resolver placement, and IPv6 availability rather than prepending.
- **Where applicable**: Any ISP or edge operator interconnecting with major CDNs. Akamai-specific in its mapping details but the pattern generalises to other intelligent-routing CDNs. It is an Akamai-delivered talk, so treat the "adopt IPv6 / avoid CGNAT" recommendations with the usual vendor-adjacent scepticism — though these align with broad community practice.

### Tuatahi First Fibre: Network Update

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=14069s)

Murray Pearson

- **Why**: A live production vendor transition (legacy Huawei GPON → Adtran architecture) at regional scale, plus a 100G handover product on the new platform — and it includes an actual failure story (multicast replication during the Whanganui cutover), which is exactly what an operator program should surface.
- **What**: A Project Manawanui progress update: aggregation migration complete, staged regional access cutovers underway (Whanganui done, New Plymouth next), OLT replacement, large-scale service migration, TCFL aggregation modernisation with new handover points (Napier, Hastings, Rotorua), and 100G NNI migrations — with lessons learned including the multicast replication issue (from abstract only).
- **How**: Staged regional cutover sequencing, OLT replacement with service continuity across a live network, and integration into updated operational systems.
- **Where applicable**: NZ fibre-operator-specific in its topology and regulatory context, but the migration-sequencing and multicast-replication lessons transfer to any GPON/XGS-PON operator doing vendor transition or scaling aggregation to 100G.

### Routeviews Update

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=12874s)

Philip Smith

- **Why**: RouteViews is the community's reference external view of BGP announcements, and this update covers a governance change (now run by NSRC) plus concrete new tooling — an API and a new BMP processor — that operators can directly use.
- **What**: An introduction to the new team behind RouteViews, its operation on behalf of the global Internet community by NSRC, and new developments: the API, a new BMP processor, how operators use the system, and future plans (from abstract only).
- **How**: Distributed route collectors giving operators an external perspective on their announcements; the new API and BMP processing extend how that data can be consumed programmatically.
- **Where applicable**: Broadly useful — any operator wanting third-party verification of their routing visibility, and researchers tracking global infrastructure. Community project, not vendor.

### Open Fibre Standards

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=3427s)

Warren Finch

- **Why**: Cyclone Gabrielle exposed what happens when nobody has a shared, structured view of physical fibre — shared corridors, thin diversity, no cross-operator picture. An open, machine-readable fibre data schema matters for resilience planning and is conceptually adjacent to how the PM thinks about infrastructure-as-data (and useful for DC site/diversity analysis).
- **What**: An introduction to the Open Fibre Data Standard (OFDS): a common, open schema for describing terrestrial fibre infrastructure — routes, nodes, ownership attributes — interoperable and machine-readable, presented from a New Zealand resilience-planning perspective (from abstract only).
- **How**: A standardised data model that lets fibre data be shared, analysed, and reused across operators, regulators, researchers, and emergency planners, supporting coordination and post-incident analysis.
- **Where applicable**: The schema is general; the *value* depends on operators actually publishing their data, which is the hard part. Relevant wherever physical-route diversity is a resilience question — NZ context is the motivating case, not a constraint.

### Designing a Mikrotik CGNAT Solution that Scales

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=4918s)

Matthew Enger (Leaptel)

- **Why**: CGNAT at small/mid-ISP scale is a recurring pain point — statefulness, redundancy, and lawful-enforcement logging requirements all at once — and this is a from-the-field design others can replicate on a budget, distilled from commercial-solution experience.
- **What**: A step-by-step redundant, scalable CGNAT solution built from Mikrotik hardware, informed by what the author learned from commercial CGNAT deployments in Leaptel's main POPs, while meeting law-enforcement (logging/accountability) requirements (from abstract only).
- **How**: The abstract does not detail the mechanism (stateful NAT distribution, redundancy model, logging pipeline), so the design specifics are in the talk.
- **Where applicable**: Small-to-medium ISPs; explicitly scale- and budget-constrained, and Mikrotik-specific — not a technique for large operators, but directly copyable for its target audience.

### Comfortable Complexity of Network Overlays

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=1852s)

Claudiu Captari

- **Why**: Using EVPN as a single consistent service layer across carrier core, DC, and campus — over VXLAN, MPLS, or SRv6 — is a significant architectural trend that collapses the "snowflake per domain" problem, and it directly touches the PM's fabric/overlay territory.
- **What**: An argument for network transformation through protocol reduction and consistent operational models, with EVPN as the key to delivering consistent L2 and L3 services across any transport and across core, DC, and campus environments (from abstract only).
- **How**: EVPN as a unified control plane abstracted from the underlying transport (VXLAN/MPLS/SRv6), replacing per-domain bespoke protocols and skill sets.
- **Where applicable**: Large multi-domain operators get the most from it. The abstract is architectural advocacy rather than a case study with results, and the speaker's affiliation is unstated — treat as a persuasive framing talk and weigh it for vendor-transformation-pitch content on the day.

### The Evolution of Network Configuration Management

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=17412s)

Tim Raphael

- **Why**: Config management is where the PM's declarative/intent-driven world (Kubernetes-style APIs) meets traditional networking — a well-structured survey of the evolution from hand-crafted configs to intent-driven operations is useful context for anyone building network tooling.
- **What**: A journey through the evolution of configuration technologies and lessons learned: scripting, imperative operations, workflows, playbooks, APIs, RPCs, declarative models, and intent-driven operations — and how networks *should* be configured going forward (from abstract only).
- **How**: Conceptual/survey talk tracing the maturity curve rather than a single tool or case study.
- **Where applicable**: Broadly applicable; most valuable as a shared-vocabulary framing for where an organisation sits on the imperative-to-declarative spectrum.

### Datagrid: Unlocking the Potential of New Zealand's South Island

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=16692s)

Pierre Goiffon

- **Why**: A 280MW AI datacentre in Invercargill plus the Tasman Ring submarine cable project is a material signal for the NZ DC/WAN interconnect landscape — relevant market intelligence for anyone in DC networking, even if the talk itself is a roadmap.
- **What**: Datagrid's vision and roadmap for the Invercargill AI DC, the role of renewable energy and climate advantages, and the international and domestic connectivity plans (Tasman Ring) needed to make the South Island a global AI infrastructure hub (from abstract only).
- **How**: As a company roadmap pitch: capacity, site, and connectivity plans rather than engineering detail.
- **Where applicable**: This is vision/roadmap content, not an engineering talk — value it as infrastructure and market intelligence on where new DC and submarine capacity will land, not as technique.

## Wildcard

### Rethinking NetOps with Open-Source LLMs & RAG

**Links:** [Recording](https://www.youtube.com/watch?v=_qzUslAh9M8&t=15823s)

Basem Al-Sabri

- **Why**: LLM copilots for network operations are an emerging subfield, and the data-sovereignty framing (no sensitive configs/logs leaving the organisation) is the specific angle that makes this credible for network operators rather than hype.
- **What**: A practical architecture combining open-source LLMs with retrieval-augmented generation, grounding model reasoning in the organisation's own knowledge base, configurations, and logs to reduce hallucinations and produce context-aware responses (from abstract only).
- **How**: Fully open-source components across data ingestion, vector retrieval, inference, and orchestration — giving operators control over data sovereignty and compliance while avoiding vendor lock-in and usage-based fees.
- **Where applicable**: Any operator, in principle. Early-stage — the abstract describes the architecture and its promises rather than measured results, so the proof will be in any demonstrated accuracy/evaluation shown live.

### AST Space Mobile

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=7224s)

Simon Allard (2degrees)

- **Why**: Direct-to-device satellite is a genuine architectural shift in coverage economics — a terrestrial mobile operator integrating an LEO constellation via its *own* ground station is novel infrastructure work outside the PM's usual beat but worth seeing.
- **What**: How AST SpaceMobile's satellite array provides mobile coverage where terrestrial networks can't, and how 2degrees is integrating the service into its network, including a 2degrees-built ground station (from abstract only).
- **How**: The technical detail (spectrum sharing with terrestrial LTE, ground-station integration, handover behaviour) is promised in the talk; the abstract stays at the "how it works" overview level.
- **Where applicable**: Mobile operators; NZ-specific integration but representative of a global D2D trend.

### Defending Multistakeholder Internet Governance

**Links:** [Recording](https://www.youtube.com/watch?v=zHCJov9WM-c&t=5253s)

Jodi Anderson

- **Why**: Not technical, but WSIS+20's outcome shapes the regulatory environment in which every technical decision in this program is made — governance developments increasingly reach into routing, security, and identity requirements.
- **What**: Where WSIS+20 ended up and how, what happens next, how it sits in the geopolitical context, and where the technical community has opportunities to defend and promote multistakeholder Internet governance (from abstract only).
- **How**: Policy/governance analysis rather than a technique.
- **Where applicable**: Global, not NZ-specific; relevant to anyone whose products touch regulated infrastructure or identity.

## Themes

- **The optical race to 400G and beyond**: Three talks (Chorus's nationwide 400G, DWDM grid planning for 1.6T superchannels, and DCI options) all sit on the same curve — coherent modulation, DSP, and open line systems are the shared engine, and topology/grid decisions made now determine flexibility for a decade.
- **AI as both workload and tool**: AI is reshaping the program from two directions — AI/HPC buildout driving physical infrastructure (Datagrid's 280MW DC, ORv3 for high-density racks, DCI demand) and AI entering operations itself (open-source LLM + RAG NetOps with a data-sovereignty angle).
- **From scripts to state**: A visible maturity arc in network automation — config management evolving from hand-crafting to declarative/intent models, REANNZ's model-driven migration verification reasoning from live data, and BGP-LS mining the control plane for live topology — operators are converging on closed-loop, model-based practice.
- **Resilience as a data problem**: Post-Cyclone Gabrielle, the program treats physical diversity not just as building more fibre (Chorus's diverse rings) but as sharing structured fibre data (OFDS) so that fragility is visible *before* the next event.
- **Modernizing 1990s protocols in place**: RADIUS next-generation standards and TCP's evolution toward BBR/ECN both acknowledge that the installed base won't be replaced — it gets upgraded in place, with all the compatibility friction that implies.

*Deliberately not covered: Enable's Network Transformation talk (high-level strategic overview with little transferable technical content in the abstract), "Life in a '90s ISP" (nostalgia), and the NZ IPv6 landscape update (abstract is a one-line pointer to a refreshed 2023 deck). The Akamai session is vendor-delivered but was kept for its actionable CDN/BGP traffic-engineering lessons.*
