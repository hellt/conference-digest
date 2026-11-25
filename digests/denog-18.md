<!--
conference: DENOG 18 (Essen)
source_url: https://www.denog.de/de/meetings/denog18/agenda.html
generated: 2026-11-22
registry_key: denog-18
-->

# DENOG 18 (Essen)

## Core

### EVPN for humans

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/YTBLUH/) · [Slides 1](https://cfp.denog.de/media/denog18/submissions/YTBLUH/resources/EVPN-for-humans-live-v0.0.5_LAEltLh.pdf) · [Slides 2](https://cfp.denog.de/media/denog18/submissions/YTBLUH/resources/EVPN-for-humans-full-v0.0.5_PLcEbkz.pdf) · [Recording](https://www.youtube.com/watch?v=53cM7X9LAe4)

Robin Christ

- **Why**: EVPN’s terminology and implementation differences turn routine fabric changes into difficult debugging sessions. This is a unusually clear mental model of the protocol, with extended reference slides for the details a short talk cannot cover.
- **What**: Starting from L2VPN, L3VPN, integrated routing and bridging, and multihoming, the talk explains what EVPN instances, VNIs, VRFs, and route targets actually represent. It then works through centralized, asymmetric, and symmetric IRB, anycast gateways, silent hosts, and all-active multihoming, repeatedly distinguishing protocol behavior from vendor conventions.
- **How**: Route targets determine imports while the advertising leaf chooses the downstream VNI. Asymmetric IRB routes and bridges at the ingress but forces every leaf to know every EVI and ARP entry; symmetric IRB routes at both ends through a tenant L3VNI so leaves need only local Layer 2 services. Type 2 and Type 5 routes, designated-forwarder election, aliasing, mass withdrawal, and split horizon complete the forwarding model.
- **Where applicable**: Directly useful for EVPN-VXLAN data-center fabrics and EVPN/MPLS service-provider networks, including mixed-vendor operations. The mechanisms are standards-based, but the deck explicitly warns that implementations vary and make different hardware-driven simplifications; validate the exact behavior of the chosen NOS and ASIC.

### Ethernet Won Inside the AI Data Center. Can It Cross an Operator Boundary?

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/73Q8NL/) · [Recording](https://www.youtube.com/watch?v=BC4g_4EpK9o)

Markus Hendrich

- **Why**: Distributed inference creates demand for connectivity between GPU sites owned by different providers. The important question is not whether Ethernet can go faster, but which performance, telemetry, sovereignty, and failure-handling guarantees remain meaningful across administrative boundaries.
- **What**: The talk separates application-level distributed inference from tightly coupled GPU fabrics, then proposes verifiable, policy-aware connectivity between AI-capable sites. It treats sovereignty as a property of compute location, traffic path, operator identity, jurisdiction, key custody, and independent verification—not just where GPUs happen to sit (from abstract only).
- **How**: A higher-level coordinator requests outcomes while each operator keeps domain-local control. Domains expose abstract capabilities such as latency class, bandwidth, diversity, geography, and jurisdiction; coordinated path computation selects a path and end-to-end measurement checks the delivered service. The session tests this model against GPU timing and congestion requirements rather than assuming a continent-wide lossless fabric is practical (from abstract only).
- **Where applicable**: Most relevant to European sovereign-AI platforms, regional clouds, colocation providers, and carriers designing inter-site inference services. This is a candidate architecture, not a validated production design; request steering at the application layer remains the simpler option for workloads that do not need network-level federation.

### Wire-API: fleet-wide, vendor-neutral network automation

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/8YL9JB/) · [Slides](https://cfp.denog.de/media/denog18/submissions/8YL9JB/resources/DENOG18_b5nGHTC.pptx)

Enric Pujol, Sebastian Wagner

- **Why**: Device-oriented automation makes a simple service change a coordinated edit across leaves, firewalls, and vendor dialects. Wire-API applies Kubernetes reconciliation to network intent, with production fabrics and a concrete multi-vendor EVPN example behind the design.
- **What**: An Apache-2.0 resource model and set of controllers for declaring network functions rather than running-device configuration. Users interact with primitives such as `Network`, `RoutingDomain`, and `ExternalConnection`; continuous reconciliation, explicit status, and label-based fleet selection replace imperative per-device runbooks.
- **How**: Four layers separate concerns: `Device` and `Interface` resources describe infrastructure; an OpenConfig-inspired “bricks” layer holds vendor-neutral per-device state; a “transit” layer translates intent and allocates resources; intent resources express the user’s requested function. Provider implementations translate bricks into interfaces such as NX-OS or SR Linux gNMI, while controllers report configured, operational, and ready status.
- **Where applicable**: Best suited to teams already comfortable with Kubernetes operators and declarative infrastructure, especially multi-vendor EVPN fabrics spanning availability zones. The deck reports roughly 50 devices in three fabrics and a Containerlab demo, so it is production experience but not yet evidence of hyperscale. Lifecycle management, incident remediation, and topology-aware upgrades remain on the roadmap.

### Network Automation for the Modern Age

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/U3Q97T/) · [Slides](https://cfp.denog.de/media/denog18/submissions/U3Q97T/resources/talk_uJq4ewQ.pdf) · [Recording](https://www.youtube.com/watch?v=l9rDJdRNTR8)

Veit Heller

- **Why**: Automation estates often accumulate NetBox, Ansible, monitoring, and custom scripts, with every integration encoding a slightly different view of the network. This is a useful architectural reframing: make the operator-owned data model authoritative and treat deployment, drift detection, and migration as transformations instead of adding more point-to-point glue.
- **What**: A model-driven approach, demonstrated through the open-core alembic prototype. A typed, canonical model declares entities, fields, and references; adapters translate between that model and systems such as NetBox, Containerlab, Ansible, and Prometheus. The demo deploys a Containerlab lab from NetBox data, then detects a manual change as drift.
- **How**: Each connected system gets a transform into or out of the central model, replacing an n×m mesh of pairwise mappings with one transform—or two for bidirectional synchronization—per system. Alembic reads and maps the source data, plans creates, updates, and deletes, and then applies the result. Reversing the mapping without applying changes turns deployment into a drift check; the same pattern supports migration between sources of truth.
- **Where applicable**: Most useful to teams integrating several automation, documentation, and operations systems whose real domain concepts no longer fit a prefabricated source-of-truth schema. The architecture is general, but alembic is presented as a case study, not a turnkey answer: its model, engine, and DCIM/IPAM adapters are open core, while fabric and operations adapters are commercial. Owning the model also means owning schema and transform engineering, with a risk of design limbo and a payoff that depends on environment size.

### You can't make everybody equally happy - Measuring Anycast with AI as the Third Member of a Two-Person Team

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/MRZYPH/) · [Slides](https://cfp.denog.de/media/denog18/submissions/MRZYPH/resources/Jan_Zorz_Anycast_DENOG_Pres_8OX4Zt2.pptx) · [Recording](https://www.youtube.com/watch?v=32MDdrgAgKQ)

Jan Zorz

- **Why**: Successful DNS answers do not reveal which anycast instance served a user, whether BGP picked a sensible catchment, or where packets disappear. This combines a genuinely useful measurement primitive with a candid account of AI-assisted engineering and the review burden it creates.
- **What**: ProVision built daily visibility into a platform spanning 39 anycast nodes in 13 regions. It maps catchments, latency, loss, jitter, PMTUD black holes, TCP reachability, ECMP paths, BGP changes, and IXP visibility. The same project became a case study in two network engineers directing coding models to build roughly 40,000 lines of Bash and Python while retaining responsibility for architecture and validation.
- **How**: Probes originate from production anycast addresses; ICMP errors returning to the “wrong” node reveal the instance BGP selected for that router. Separate stats nodes generate load, production nodes only capture replies, and a central 17-stage nightly pipeline correlates the measurements. AI supplied implementation speed, but repeatable scripts, unit tests, multiple independent model reviews, monitoring, and human veto power supplied correctness checks.
- **Where applicable**: The catchment technique applies to DNS, CDN, and DDoS anycast operators able to emit probes from service addresses and collect distributed responses. The reported 117,000 probes/s and multi-million-target scans are ProVision-specific scale, not a recommended default. The AI lessons transfer broadly: generated code still needs adversarial review, operational guardrails, and repeatable—not generated—verdicts.

### IPv4 as a service on an IPv6-only network

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/V7Y3X9/) · [Slides](https://cfp.denog.de/media/denog18/submissions/V7Y3X9/resources/presentation_qhh5OYp.pdf) · [Recording](https://www.youtube.com/watch?v=bJka_8xe89Q)

Tobias Fiebig, Remco van Mook

- **Why**: Dual stack preserves IPv4 subnets, ARP, first-hop redundancy, and fragmented address pools even when IPv4 is only a residual application requirement. This presents running code and deployment models for making IPv4 an overlay-independent endpoint service on an IPv6-only operational foundation—without tunnels or translation.
- **What**: RFC 8950 carries IPv4 routes with IPv6 next hops, allowing host /32s to move with IPv6 infrastructure rather than remain tied to sized subnets. An adopted INTAREA draft adds a sentinel DHCPv4 gateway so unmodified hosts retain familiar behavior while updated hosts resolve their first hop from the IPv6 neighbor cache.
- **How**: Updated hosts use the MAC and health of their IPv6 default router; unmodified hosts ARP once for the sentinel and the router answers. Router examples cover single-gateway, active/active anycast, and BGP-orchestrated multi-gateway models. The deck includes Linux, FreeBSD, macOS, and Windows implementations, unmodified-host tests across seven operating systems, vendor configurations, and the public V4LESS-AS test service.
- **Where applicable**: Compelling for hosting, access, and cloud networks with IPv6-capable routers and a need to reclaim IPv4 infrastructure complexity. Support remains uneven: Linux, FreeBSD, FRR, BIRD, and several commercial NOSes are covered, but tooling and IGP gaps matter. ND health, ICMP/PMTUD behavior, egress filtering, and sentinel-address standardization are explicit deployment constraints.

### IPv6 routing loops -- A call to fix router configurations.

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/PRRFUN/) · [Slides](https://cfp.denog.de/media/denog18/submissions/PRRFUN/resources/mkoch-denog18-ipv6-routing-l_iUlhuvs.pdf) · [Recording](https://www.youtube.com/watch?v=9wUAC3nNn50)

Maynard Koch

- **Why**: Partially used provider-assigned IPv6 space makes packets fall back to a default route and circulate, while some routers duplicate looping packets and amplify the damage. Weekly measurements show that a basic configuration fix and operator outreach materially reduce a continuing Internet-wide problem.
- **What**: The study tracks looping subnets, router addresses, and amplification across RIR regions, with detailed DE-region reporting. It reports a reduction of 5.8 million looping subnets (6.5%) since RIPE 92, but also finds 69 of 190 ASes represented on the DENOG18 attendee list affected.
- **How**: A router with more-specific connected prefixes but no route for unused addresses inside the aggregate can send those packets back toward its default upstream. Its ICMP Time Exceeded messages expose the loop to measurement; a router duplication bug can turn that into packet and ICMP floods. A discard/null route for the covering aggregate removes both the loop and the amplification primitive.
- **Where applicable**: Universally relevant to IPv6 operators, especially networks announcing aggregates larger than their actively assigned space. The affected-device examples include confirmed Juniper, MikroTik, and older Cisco platforms, but the preventive null-route pattern is platform-independent. Operators can check their AS in the project’s weekly public data before changing filters or policy.

### ICMP trickery in "reduced-IPv4" networks

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/ZQEANK/) · [Slides 1](https://cfp.denog.de/media/denog18/submissions/ZQEANK/resources/denog18_icmpexts_pres_DEricIf.pdf) · [Slides 2](https://cfp.denog.de/media/denog18/submissions/ZQEANK/resources/denog18_icmpexts_uncut_vRwVcuo.pdf) · [Recording](https://www.youtube.com/watch?v=EbkX_kLxczg)

David 'equinox' Lamparter

- **Why**: Removing interface IPv4 addresses breaks assumptions embedded in traceroute, ICMP errors, NAT64, and PMTUD. The talk exposes where useful diagnostics vanish and gives concrete configuration changes needed to keep an IPv6-centric network operable.
- **What**: Real captures compare routers with one IPv4 loopback, no IPv4 addresses, and NAT64/CLAT paths. RFC 4884 extensions can carry interface names, next-hop information, and MPLS labels, but address reduction and translation remove or confuse exactly the context operators need.
- **How**: An IPv4-only-addressed router can choose its loopback as ICMP source; an address-free router uses the dummy source `192.0.0.8`, which NAT64 can translate into its IPv6-mapped form. Extended ICMP and proposed node-identification extensions preserve additional origin detail. The operational checklist is to permit `192.0.0.8` through source filters and RPF, enable ICMP extensions, and use tools that actually decode them.
- **Where applicable**: Important for RFC 8950, NAT64, CLAT, MPLS, and IPv6-mostly deployments, plus anyone troubleshooting PMTUD across those environments. Some traceroute output is explicitly illustrative and Linux support is incomplete, so treat the drafts and patched tools as emerging work rather than ubiquitous capabilities.

### Carrier-Scale TWAMP Monitoring with DPDK and Commodity x86 Servers

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/39VKX7/) · [Slides](https://cfp.denog.de/media/denog18/submissions/39VKX7/resources/Carrier_Scale_TWAMP_DPDK_5x9_iKYlx1v.pdf) · [Recording](https://www.youtube.com/watch?v=jauO1IjThAc)

Mario Jurcevic

- **Why**: Thousands of access destinations multiplied by per-QoS streams turn TWAMP timing precision into a packet-processing problem. The measured comparisons show where kernel bypass materially improves active monitoring without proprietary appliances.
- **What**: A DPDK-based TWAMP client architecture handles packet generation, scheduling, timestamps, and result processing on commodity x86 systems. On a low-cost Ryzen platform it increased packet rate from 10,000 to 200,000/s while reducing maximum timestamp offset from over 2 ms to under 50 µs; a larger Xeon system demonstrated 1 Mpps across 20,000 destinations and 100,000 streams.
- **How**: DPDK moves packet handling and software timestamping outside Linux, avoiding kernel timing jitter while remaining portable across supported NICs. The design uses dedicated packet-processing cores, userspace forwarding, session scheduling, CPU affinity, and NUMA-aware resource allocation. Precision was checked against an FPGA-based hardware responder in runs of at least six hours.
- **Where applicable**: Useful for transport, access, RAN/FAN SLA monitoring, and other high-rate active-measurement systems. The results are tied to the stated servers, NICs, and workload. Dedicated cores running at full utilization and greater integration complexity are the cost; smaller deployments may not justify kernel bypass.

### Route Filtering at Scale

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/KXMLXN/) · [Slides](https://cfp.denog.de/media/denog18/submissions/KXMLXN/resources/DENOG18_Route_Filtering_at_S_Rw7sgKx.pdf) · [Recording](https://www.youtube.com/watch?v=JH_7p2kUC0c)

Fedor Vompe, Sebastian Becker

- **Why**: RPKI origin validation does not replace customer-cone filtering, and bad IRR AS-Set data can silently turn a defensive filter into a route leak or blackhole. This connects registry-data quality to the production toolchain needed at tier-1 scale.
- **What**: An analysis of roughly 74,000 AS-Sets finds missing references, cycles, questionable inclusions, and explosive expansion—one added reference containing 20,000 ASNs produced more than 100,000 prefixes. The recommended posture combines AS-Set filters, RPKI ROV, ASPA, BGP roles/OTC, monitoring, and maximum-prefix limits rather than treating any one mechanism as sufficient.
- **How**: Filter generation recursively expands AS-Sets, collects IRR route objects and RPKI VRPs, summarizes prefixes, and deploys the result. RQSpec and an RPSL engine provide readable policies, exclusions, recursive resolution, and loop prevention; RIPEdiff and an internal observatory track changes and their effects on parent sets and generated filters. Comparing documentation with pre-policy BMP routes helps find missing or ineffective data.
- **Where applicable**: Directly applicable to transit providers and large peering operations generating filters from multiple IRRs. Customer AS-Sets should contain downstream customers only, not peers, upstreams, or route-server sets. ASPA adds signed AS-path validation as deployment grows, but its fail-open behavior still requires limits, and small providers may retain AS-Set filtering for the foreseeable future.

### SRv6 in the Data Center: Crazy Ideas or Real Use Cases?

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/E8TQM8/) · [Slides](https://cfp.denog.de/media/denog18/submissions/E8TQM8/resources/DENOG-SRv6-v04-dark-short_irmZx8N.pptx) · [Recording](https://www.youtube.com/watch?v=-3QXLZjK9L0)

Andreas Roeder

- **Why**: AI collectives violate the many-small-flows assumption behind ECMP, leaving elephants colliding while average utilization looks healthy. The talk’s strongest contribution is showing how compressed SRv6 moves deterministic per-packet path selection into the NIC without per-flow fabric state.
- **What**: A progression from ECMP and QP scaling through adaptive routing to NIC source routing, followed by concrete SRv6 designs for Clos fabrics, DCI, and AI backends. Micro-SIDs make the AI case technically plausible; the deck also distinguishes production SRv6 VPN/DCI uses from maturing GPU-fabric applications.
- **How**: RFC 9800 NEXT-C-SID compresses 16-bit instructions into an IPv6 destination address—six hops with a 32-bit block—so no Segment Routing Header is needed. A NIC selects plane and spine per packet, switches match local /48 locators and shift to the next instruction, and the final leaf decapsulates. MRC places packets directly in receiver memory, while identically routed probes test and quarantine individual paths.
- **Where applicable**: DCI is the least speculative starting point; source-routed AI fabrics require capable NICs, MRC-like transport, multi-plane topology, and an orchestrator that distributes the path map. Restrict SRv6 injection to trusted workloads inside one administrative domain. Six instructions fit the compressed form, longer paths need an SRH, and existing ACL, traceroute, and flow-monitoring assumptions need revision.

### Maybe it is time to consider layer 3 internet exchanges

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/EMHXW7/) · [Slides](https://cfp.denog.de/media/denog18/submissions/EMHXW7/resources/DENOG18-Rice-layer3-internet_CYbdNDJ.pdf) · [Recording](https://www.youtube.com/watch?v=R6Y8XBjJMnQ)

James Rice

- **Why**: Shared Layer 2 peering LANs can blackhole or misdeliver traffic while route-server BGP sessions remain healthy. Replacing that broadcast domain with routed ports makes forwarding faults visible and gives participants the isolation they already expect from PNIs and transit.
- **What**: A concrete proposal for an exchange router per participant port, carrying peers’ routes over one BGP session per address family. Benefits include port isolation, exchange-level RTBH, BFD, and a visible traceroute hop. Migration can run routed 802.1Q sub-interfaces alongside the existing peering LAN rather than requiring a flag day.
- **How**: Participants use a /31, /127, or RFC 8950 link-local connection to the exchange, with selective-announcement communities preserving route-server-style control. Routed forwarding eliminates unknown-unicast flooding and cross-participant ARP/ND failure modes. Existing switches may already support line-rate Layer 3, but full-table FIB capacity, blackhole routes, steering more-specifics, and FlowSpec entries require explicit planning.
- **Where applicable**: A design proposal for IXPs and their members, not a report of broad deployment. It reduces N×M BGP sessions to N but moves best-path selection and more operational responsibility onto the exchange. Direct sessions or point-to-point VLANs remain options when egress-peer control is non-negotiable; a measured parallel trial is the sensible next step.

### FSO essentials

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/BSEFX3/) · [Slides (PDF)](https://cfp.denog.de/media/denog18/submissions/BSEFX3/resources/DENOG181106_Kfu5GsI.pdf) · [Slides (PPTX)](https://cfp.denog.de/media/denog18/submissions/BSEFX3/resources/DENOG181113_ESS8kNF.pptx) · [Recording](https://www.youtube.com/watch?v=ySEgmuK2sx0)

Takaya Nakagawa

- **Why**: Free-space optics offers fiber-like directional capacity without RF interference or new ducts, making it relevant for difficult campus, metro, and temporary links. The useful lesson is the balance between greatly improved deployability and atmospheric availability constraints.
- **What**: A survey of modern compact FSO systems, now light enough for one-person installation and efficient enough for PoE power. Current systems commonly target 10+ Gbps, with automatic tracking and increasingly capable power control; the deck also covers laser classes and automatic power reduction when an object crosses the beam.
- **How**: Smaller optics, better sensors, processors, and software stabilize the laser path. AI-assisted functions track movement and adjust transmit power in near real time. Fog still scatters and absorbs the signal, while thermally driven turbulence causes scintillation, higher bit-error rates, and lower availability; mounting height can reduce exposure to some turbulence.
- **Where applicable**: Worth evaluating for clear-line-of-sight links where trenching is costly, and for satellite, drone, or temporary deployments. Do not treat FSO as a like-for-like fiber replacement without local fog/turbulence availability analysis, an engineered fallback, and a laser-safety assessment—some commercial Class 1M systems become hazardous when viewed through optical instruments.

## Adjacent

### The New Botnet Era: Rethinking Your DDoS Strategy

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/XBCBZT/) · [Slides](https://cfp.denog.de/media/denog18/submissions/XBCBZT/resources/DENOG18_Botnet_StM_20261112_qpjr2jb.pdf) · [Recording](https://www.youtube.com/watch?v=N8djU59vVTQ)

Stefan Meinders

- **Why**: Terabit-class attacks are becoming routine while residential-proxy and IoT bots make malicious traffic look like legitimate customer traffic. Defense now has to cover inbound, outbound, and cross-bound movement, not just capacity facing the public Internet.
- **What**: NETSCOUT ATLAS data shows worldwide attacks above 1 Tbps rising from 94 in H1 2025 to 1,121 in H1 2026; botnet attacks above that threshold rose from 4 to 230. Carpet bombing grew 62% over the same half-year comparison. Alongside direct-path volume, tailored application and state-exhaustion components can stay below traditional detection thresholds.
- **How**: Compromised IoT and proxy SDKs inside free applications supply distributed, trusted residential sources, undermining reputation lists and simple source filters. The recommended response combines outbound bot detection and customer cleanup, more mitigation capacity for direct and carpet-bombing attacks, continued BCP 38/84 source validation, and FlowSpec for simpler reflection/amplification vectors.
- **Where applicable**: Relevant to ISPs, hosting/cloud operators, CDNs, and large enterprises. The measurements come from NETSCOUT’s visibility and should be read as that platform’s dataset, not a neutral census; the speaker’s proposed “calibrating the cannon” explanation for record attacks is explicitly a hypothesis. The three-direction detection model is broadly transferable.

## Wildcard

### Geoinformation Systems & Internet Infrastructure

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/97DCW3/) · [Slides](https://cfp.denog.de/media/denog18/submissions/97DCW3/resources/slides_GkmWEA7.pdf) · [Recording](https://www.youtube.com/watch?v=PO9ryOzbNiI)

Dominik Bay

- **Why**: Carrier KMZ and DXF attachments usually disappear into a contract folder even though they can answer operationally valuable questions about true path diversity, expected latency, and fibre-cut location. This turns routine circuit documentation into an open-source, queryable network operations dataset.
- **What**: A practical workflow for importing circuit routes, validating coordinate systems, and linking physical infrastructure to logical inventory. Spatial queries identify “redundant” paths sharing ducts or crossings; fibre geometry improves latency estimates; OTDR distances can be mapped back to streets while accounting for slack and overlength.
- **How**: GDAL converts KML/KMZ/DXF into GeoPackage layers, QGIS visualizes them, and PostGIS performs intersection and buffer queries. Measure routes in UTM rather than Web Mercator, obtain the CRS and units for DXF files, and retain revision dates. Combining routes with roadworks, access restrictions, weather, or evacuation polygons turns alarms into ranked field investigations.
- **Where applicable**: Broadly applicable to operators buying wavelengths, dark fibre, or microwave links. Germany’s long-haul route factors of 1.3–2.0 are observations from the speaker’s own tool, not universal constants. Geodata does not prove accuracy or current as-built conditions; slack records and supplier revisions remain necessary.

### A Prosecutor in Another Country Wants Your Data in 8 Hours — Now What?

**Links:** [Abstract](https://cfp.denog.de/denog18/talk/J9DJVF/) · [Recording](https://www.youtube.com/watch?v=0SKWsKBLGqg)

Mathias Handsche

- **Why**: The EU E-Evidence Regulation turns cross-border evidence production into an on-call engineering problem, with eight-hour emergency deadlines. Logging design, retention, integrity, and ownership determine whether an ISP or cloud provider can respond without an improvised fire drill.
- **What**: An operator-focused account of European Production and Preservation Orders covering subscriber, traffic, and content data. The talk addresses legal representation, joint liability, the decentralized machine interface, and a field report from the regime’s first months (from abstract only).
- **How**: The practical evidence model is straightforward: produce the right data, demonstrate it is unchanged, anchor it in time, and trace who accessed or exported it. Common failure modes are expired logs, mutable records, screenshots instead of defensible exports, and missing audit history. The decentralized exchange’s transport format, size limits, and uneven rollout add implementation constraints (from abstract only).
- **Where applicable**: Directly relevant to EU-facing ISPs, hosting and cloud platforms, registrars, and teams owning abuse, lawful-interface, or logging systems. Legal interpretation needs qualified counsel, but the engineering checklist is general: align retention with obligations, preserve provenance and integrity, test exports against deadlines, and assign an accountable response path before the first order arrives.

## Themes

- **Path choice is moving toward the endpoints**: SRv6 source routing, anycast measurement, and routed IXPs all expose or exploit forwarding choices that a shared network previously hid.
- **IPv6-only operation is now an integration problem**: running code exists for IPv4 services over IPv6 next hops, but ICMP, autoconfiguration, neighbor discovery, tooling, and registry hygiene determine operability.
- **Automation needs an explicit model**: Wire-API reconciles declared intent into device configuration, while alembic centers an operator-owned typed model and transforms tools into and out of it. EVPN and route filtering reinforce the cost of ambiguous semantics and bad source data.
- **Measurement is part of the data plane**: carrier-scale TWAMP, anycast catchments, routing-loop surveys, and geospatial fault location turn raw network behavior into actionable operational state.
- **AI infrastructure stresses organizational boundaries as much as bandwidth**: GPU fabrics need deterministic paths, while distributed inference also demands cross-operator telemetry, verification, and sovereignty guarantees.
