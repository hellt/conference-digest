<!--
conference: APRICOT 2026 (Jakarta)
type: operator
source_url: https://2026.apricot.net/
generated: 2026-11-04
registry_key: apricot-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# APRICOT 2026 (Jakarta)

A routing- and peering-heavy operator program. For this reader — physical DC/WAN systems, cloud-native networking, security, and identity — the strongest material this cycle sits in four clusters: coherent-optics/IPoDWDM (finally production-ready), SRv6/EVPN fabric migration, a coherent wave of "post-ROV" routing-security work (ASPA, MESec, BMP-based visibility), and early standards activity around agentic/attestation identity at the IETF.

## Core

### IPoDWDM in 2026

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/8fce29f4-7b55-4fe0-8181-e2e2460da097.pdf)

Mark Tinka, TransmissionCo

- **Why**: IPoDWDM failed once (2000s: proprietary, fixed, power-hungry line cards) and is now succeeding — this talk explains exactly what changed and who is deploying it, which matters for anyone planning DC/WAN interconnect on dark fiber or short DWDM spans.
- **What**: A state-of-the-market walkthrough of routed optical networking built on MSA coherent pluggables. Per CignalAI data cited, coherent pluggables outsold proprietary embedded optics 2:1 in 2025, and most 400G-ZR shipments have gone into hyperscaler IPoDWDM deployments; hyperscalers are converging on OSFP for 800G-ZR for thermal reasons. Includes a live reference network: a 130 km span in Cape Town built from a Juniper ACX7300 router with 2x 400G-ZR+ QSFP-DD plugs plus a third-party open line system — no transponder tier.
- **How**: Coherent pluggables (100G-ZR QSFP28, 400G/800G-ZR QSFP-DD/OSFP) put DWDM line-side optics directly in standard router/switch ports, on dark fiber or integrated with a line system for reach; line- and client-side mix on the same card; disaggregation removes the optic from the host platform. Pluggable transponders are positioned as the bridge for operators who still want Layer-1 aggregation/demarcation/protection.
- **Where applicable**: Broadly applicable technique, not org-specific — driven by hyperscaler economics but now accessible to any operator with dark fiber or short spans. Presented by a vendor-side MD, but the deck is grounded in third-party market data and a real multi-vendor deployment rather than a product pitch.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/b68d1d9d-d598-4afa-b5c7-d1ba53997e9d.pdf)

Thomas Weible, FLEXOPTIX

- **Why**: Choosing grid spacing and filters today determines whether your DWDM plant can carry 800G/1.6T superchannels tomorrow — a topology/spectrum planning problem IP engineers now own under IPoDWDM.
- **What**: An argument that coherent detection changes the rules: because a coherent receiver is "blind" to anything but its own wavelength, you can build filterless/colorless topologies and combine sub-bands through cheap 1x4 splitters and ordinary 50 GHz muxes. The concrete recommendation is 400 GHz COTS muxes (12 channels in C-band vs. the classic 96x50 GHz) to future-proof for 1.6T while remaining backward compatible with legacy 50 GHz services.
- **How**: Walks from OOK/direct-detection limits through higher-order modulation (16-constellation, dual-polarization, 425Gbps at 53.125 GBd), balanced receivers, phase- and polarization-diversity coherent detection, homodyne/heterodyne/intradyne tradeoffs, and ends with a "make a frequency plan for your spans" design methodology — think in THz/GHz, not nm or channel numbers.
- **Where applicable**: General DWDM design guidance for operators planning or refactoring their own optical plant; vendor-presented (FLEXOPTIX), so the COTS-component framing is self-interested, but the physics and filter-sizing argument are vendor-neutral. Assumes coherent optics end-to-end.

### IX.br São Paulo: Migration to SRv6 EVPN

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/6b3ca07b-f892-483d-b9f7-19dd727054a3.pdf)

Julio Sirota, NIC.br

- **Why**: A production migration template for anyone running a large L2 fabric (IXP peering LAN or DC) on aging LDP+VPLS: flood-based MAC learning, ARP/ND storms, and unknown-unicast flooding are exactly the failure modes EVPN was built to fix.
- **What**: The completed migration of IX.br São Paulo (one of the world's largest IX fabrics) from LDP+VPLS to SRv6 EVPN. Concrete results: 84% of equipment (97% of capacity) now on EVPN CSID SRv6 with proxy ARP/ND, unknown-unicast flood eliminated, and a large measured drop in ARP/Neighbor Solicitation volume — including visible reduction in CPU load on participant routers.
- **How**: RFC 8560 "VPLS and EVPN seamless integration" allowed PE-by-PE replacement with the core forwarding both MPLS and IPv6/SRv6 labels during migration, no gateway needed. Proxy ARP/ND uses the RFC 9047 ARP/ND Extended Community with the Immutable flag so static entries prevail over dynamic ones, which both kills broadcast storms and prevents participants answering ARP/ND for IPs that are not theirs (spoofing protection).
- **Where applicable**: IX.br-specific production story, but the mechanism is standard-track (RFC 8560, RFC 9047) and broadly applicable to any VPLS estate with SRv6-capable PEs. The seamless-migration trick (dual-plane forwarding, one box at a time) is the transferable part.

### Getting 1+ Tbps from an x86 server

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/c4acd498-1fd0-463a-bf65-16044fb86d99.pdf)

Branimir Rajtar, 5x9 Networks

- **Why**: The datapath-internals story of the year at this conference — what it actually takes to make commodity x86 forward at terabit rates, relevant to anyone building or evaluating software dataplanes (vBNG, vEPC, NFV).
- **What**: The evolution of a virtualized BNG from many small 4-vCPU forwarder VMs to a single "Big VM" forwarder, ending at 200 Mpps per CPU and 1.6 Tbps on one server (~600 W). Includes an honest comparison table: ASIC white-label switching (multi-terabit, low flexibility, ~30k subscribers) vs. x86 (~1 Tbps and improving, ~200k subscribers, high flexibility, C/DPDK/eBPF/P4 development).
- **How**: SR-IOV plus Intel DPDK to bypass host kernel and drivers; systematic optimization in waves — newer hardware (+30%), deep DPDK/BIOS/PCIe/NIC tuning (+30%), then vTune-guided code-level redesigns driven by CPU cache behavior and PCIe bottlenecks. The horizontal-scaling small-VM design was abandoned because per-instance overhead dominated. CUPS architecture (dashboard/controller/forwarder) throughout.
- **Where applicable**: vBNG/BRAS is the use case and the headline numbers are tied to their specific hardware generations; the methodology (measure, profile, redesign around cache/PCIe) transfers to any DPDK dataplane effort.

### Exploring the Blind Spot of Internet Exchange Point Route Servers

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/a548a2ef-e856-451d-bfe1-fa8a5455f4cc.pdf)

Stefano Servillo, University of Rome "La Sapienza" (with Spadaccino, Konstantaras, Luciani, Cuomo)

- **Why**: A formally defined, quantified vulnerability in the IRR-based route-server filtering that most of the world's IXPs rely on — directly relevant to routing security practice.
- **What**: The blind spot: IRR validation via AS-SET expansion builds a prefix list per peer but never binds prefixes to their legitimate origin AS, so a prefix covered by a route object under any AS that appears in a member's AS-SET is accepted by the route server regardless of who really owns it. Stale AS-SETs make this worse: of ~130k allocated ASes only ~77k are active, so AS-SETs routinely contain unallocated, private, or inactive ASes whose route objects can weaponize the gap. The team demonstrates prefix hijacking through this path, quantifies prevalence across a large set of IXPs, and validates with real route-server data from AMS-IX and NAMEX.
- **How**: Feasibility analysis defines the conditions (prefix not ROA-covered, update not filtered by intermediate ASes, origin AS in a member's AS-SET but not required to be there, etc.), followed by control-plane data analysis; practical countermeasures to strengthen RS filtering are proposed.
- **Where applicable**: Applies to any IXP or operator doing IRR-based filtering anywhere; RPKI ROAs close the hole for covered prefixes, which sharpens the case for ROA coverage as hijack insurance rather than just leak hygiene. Research-grade but with production validation.

### MESec: Minimal-Exposure AS-Path Verification against BGP Post-ROV Attacks

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/d5b88c42-c664-46e1-a671-cf78b453e486.pdf)

Jiangou Zhan, Tsinghua University

- **Why**: With ~49% of IPv4 prefixes ROA-protected and ~37% of ASes doing ROV, attackers move to path manipulation and route leaks — but ASPA's requirement to publish customer-provider relationships globally is commercially toxic. This is the sharpest articulation of that adoption dilemma at the conference, with a real alternative.
- **What**: MEASPV, a framework that decouples path validation from topology disclosure: relationship attestations are visible only to designated trusted validators, never broadcast. Evaluation shows a security posture comparable to standard ASPA against post-ROV threats, with minimal information exposure and incremental deployability (no BGP-4 message changes).
- **How**: Validator-assisted, three phases: trust establishment (ASes share encrypted, authenticated neighbor-relationship data with chosen validators), path verification on each BGP UPDATE (validators return Type-I high-trust direct reports plus Type-II public-data checks from CAIDA/RouteViews; results aggregate into a score from Strong-Valid to Strong-Suspect), and secure route selection using the score as a BGP decision-process tie-breaker. Caching of per-pair scores (1–5 day refresh, path score = minimum) keeps latency and control traffic low. The authors also prove a lower bound: any effective defense must expose relationship data to at least one third-party verifier — the question is how few.
- **Where applicable**: Research framework, not deployed; requires a trusted-validator ecosystem. Conceptually important for anyone designing ASPA-adjacent or attestation-based path security, including in private fabrics where a neutral validator is easier to stand up.

### ASPA in the RPKI Dashboard

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/77c06f7d-00f1-4201-a963-b31cbb9be3a6.pdf)

Tim Bruijnzeels, RIPE

- **Why**: ASPA is the mechanism operators will be asked to deploy after ROV; this is the clearest available explanation of its verification semantics — what it catches, what it deliberately tolerates, and how it fails.
- **What**: A worked tutorial of ASPA (AS Provider Authorisations): objects like ROAs, signed by the customer-AS holder, authorizing one or more provider ASes. Routes learned from customers are invalid if a hop is proven "Not Provider"; the system supports partial deployment (no attestation = fail open, as does an RPKI validation problem itself), and it detects valley-free violations by constructing the longest UP ramp (customer→provider from the origin) and DOWN ramp (provider→customer from the receiver) and rejecting paths with a gap — i.e., route leaks — regardless of whether the cause is accident, leak, or spoofing.
- **How**: Object structure and path-verification logic presented through concrete examples (spoofed-origin and leaked-path cases), matching what the RIPE RPKI Dashboard now surfaces.
- **Where applicable**: Protocol-level and vendor-neutral; broadly applicable. Deployment is early (ARIN brought ASPA online for its own services 20 January 2026, per the ARIN update in the same program), so this is the right time to learn the semantics before it lands in dashboards you use.

### What’s new at the IETF?

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/2ea34790-9ba4-436d-8f0a-8fa643a6c731.pdf)

Paresh Khatri, Nokia (delivered with Warren Kumari, Dhruv Dhody, and Suresh Krishnan, IAB)

- **Why**: The standards radar this cycle is unusually relevant: three of the newly chartered working groups touch attestation, bot/agent authentication, and PKI — squarely in identity territory — alongside routing and ops topics.
- **What**: New WGs: Secure Evidence and Attestation Transport (SEAT), Domain Connection (DCONN), Open Cloud Mesh (OCM), Web Bot Auth (WEBBOTAUTH), and PKI, Logs, And Tree Signatures (PLANTS); Authenticated Transfer (ATP) in chartering. BoFs at IETF 125: CATALIST (coordinating AI agent-to-agent communications work) and ONSEN (operationalizing service abstractions). Also reports the IAB workshop on IP address geolocation concluding that IP is a weak, overloaded geolocation signal (anycast, satellite, overlays) — a useful data point for anyone building location-dependent policy.
- **How**: An operator-oriented survey of IETF structure (areas, ~125 WGs, IRTF, IAB) and where the new work landed, aimed at helping operators track what will hit their networks.
- **Where applicable**: Broadly applicable; for this reader, WEBBOTAUTH and CATALIST are the items to watch for agentic/workload identity, and SEAT/PLANTS for attestation-transport plumbing.

### bgproutes.io: A Next-Generation BGP Data Collection Platform

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/444b491c-a5c0-4e42-a6e0-bde2d7020557.pdf) · [Recording](https://www.youtube.com/watch?v=uktSxm_ZZs0)

Thomas Holterbach, University of Strasbourg (with Thomas Alfroy, Cristel Pelsser)

- **Why**: RIPE RIS and RouteViews only collect best-path announcements; monitoring hijacks, leaks, and policy behavior needs more, and this platform — running for a year — shows how to get it.
- **What**: A next-gen BGP collection platform prioritizing accurate real-time/short-term monitoring and perpetual retention (where RIS/RouteViews historically prioritized coverage). After one year it receives data from ~70 contributing networks and, critically, aggregates everything already collected by RIPE RIS, RouteViews, PCH, and CGTF into a single database, then exposes it via API and dashboards.
- **How**: Three coverage ingredients: (1) automated peering establishment — operators authenticate via PeeringDB and fill in a form to start a session; (2) aggregation of existing collectors; (3) BGP Monitoring Protocol to collect beyond best-path (routes from multiple peers at multiple decision-process stages) — operationally, a small number of BMP sessions already yields a large number of additional vantage points. Every collected route gets RPKI and ASPA validation, with results exposed to users, which makes the platform a live testbed for assessing whether those mechanisms actually work at scale.
- **Where applicable**: Community infrastructure, partially APNIC Foundation funded; usable by any operator or researcher today (contribute a session, or just consume). Complements rather than replaces RIS/RouteViews.

### BGP in 2025

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/4dffcaec-ce12-43bf-b226-202193b34a99.pdf)

Geoffrey Huston, APNIC

- **Why**: The annual reference for DFZ scale, churn, and the year's notable routing events — baseline data for FIB/TCAM planning and for understanding routing-system fragility.
- **What**: The IPv4 DFZ exceeded 1M entries for all BGP peers in 2025; headline events include the July 7 Ramses exchange fire in Cairo (four deaths, visible disruption in BGP), and Amazon's AS16509 swinging from 50M to 158M advertised addresses during the year — including a -15.8M withdrawal on 4 November and a +15.1M re-announcement on 10 December. The advertised IPv4 table actually shrank by 11M /32s over the year while unadvertised space grew by 10M; RIR allocations continue to be outpaced by recovery. Top churn tables (China Mobile +13k prefixes, USDA's odd 3,122-prefix behavior, Cox, Amazon) give a feel for who is re-de-aggregating.
- **How**: Longitudinal analysis across every routing peer of RouteViews and RIPE RIS: FIB counts, advertised address span, update/churn dynamics, two decades of comparison.
- **Where applicable**: Global and vendor-neutral; the numbers are what they are. Most useful as planning input (FIB growth, prefix-churn tolerance) and as a reminder that single-actor behavior can move the global table by millions of addresses in a day.

## Adjacent

### Building an OOB network

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/dd8b382e-43af-4f2b-adc8-57320445ccc2.pdf)

Phil Mawson, Vocus

- **Why**: The management plane is what saves you when the data plane is down — this is a multi-year, build-it-again carrier case study with real design decisions, prompted by exactly the class of outage (Optus AS7474 national outage, November 2023; Meta, October 2021) that makes OOB non-negotiable.
- **What**: Vocus' consolidation of many inherited bespoke OOB solutions into a dedicated national OOB MPLS network, built alongside a new zero-touch-provisioned aggregation network.
- **How**: Key rules: OOB must not rely on any founder IP network; per-state regions with route-reflector pairs; OSPF as IGP; own transmission interstate with diverse paths and metro dark-fiber rings. Equipment: Juniper ACX7024/SRX345 routers, EX3400/4100 switches, Opengear console servers. International sites use Megaport Layer-2 VXC back to an Australian headend (cheaper than 10G waves). Extras worth stealing: a third-party transit VPN concentrator as break-glass if AS4826 dies entirely, geographically diverse bastion hosts in three cities, and printed break-glass local credentials locked away for when your auth servers are unreachable.
- **Where applicable**: Vocus-specific in its parts list and assumptions (they own Australian transmission), but the design principles — independence from the production network, geographic diversity, break-glass auth — transfer to any operator or large DC operator. Budget math differs if you must buy OOB transport.

### Can RPKI help mitigate social engineering attacks?

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/356755e3-72be-43db-844d-98627bf845c9.pdf)

Sanjaya, APNIC (with Carlos Martinez, LACNIC)

- **Why**: A rare public postmortem of a hijack executed through humans, not protocol weakness — and a direct answer to whether RPKI would have stopped it.
- **What**: LACNIC address space was hijacked intermittently in July 2025 by a rogue AS with a repeat-offender history across multiple RIR regions. The investigation (LACNIC → APNIC → APJII/IDNIC) found the bad actor had hijacked the ASN itself and convinced a multinational transit provider to provision transit using forged company letterhead and a faked domain — short random BGP advertisements followed. The transit provider terminated service on the victim's report; the case was jointly written up as a community case study.
- **How**: Incident timeline and escalation-path walkthrough; the stated lessons map the defenses: a ROA with correct maxlength prevents the prefix hijack, and ASPA blocks unauthorized upstream providers — the exact door the attacker walked through.
- **Where applicable**: General — any resource holder. Its main value is the honest gap analysis: ROV stops origin forgery but not social engineering at your transit provider; ASPA (or contractual LOA verification) is the missing control.

### sidrops IETF UPDATE

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/5a8f311a-b15d-4ed8-b8ae-e64be6d17a6a.pdf)

Tom Harrison, APNIC

- **Why**: The plumbing of RPKI distribution is being redesigned; if you operate relying parties or a publication point, this affects you.
- **What**: Three sidrops work items: the Erik synchronization protocol (draft-ietf-sidrops-rpki-erik-protocol), NRO Trust Anchor Constraints, and Best Current Practices for RPKI publication servers.
- **How**: Erik is the interesting one — today every relying party fetches from every publication point (an M:N problem that worsens over time, where one slow PP holds up an RP's whole validation run). An Erik relay, runnable by anybody, fetches from PPs and serves RPs over the new protocol: PPs go from handling thousands of RPs to ~20 relays in full deployment. It also fixes RRDP's encoding waste (base64 adds 33%, XML another ~10%), serves raw DER objects, and uses Merkle trees to support cheap diffs and individual-file repair — eliminating the "delta failed, re-fetch a 100 MB snapshot" thundering herd (the deck shows a 102 MB snapshot vs. a 68 KB delta).
- **Where applicable**: All RPKI operators; deployable incrementally alongside rsync/RRDP. Reference implementations exist (rpkitouch relay, public relay instance).

### Debugging Routing & Forwarding Using RIPE Atlas

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/457aa45c-b33e-4382-bff1-12e69861bfb2.pdf)

Randy Bush, Internet Initiative Japan

- **Why**: Two real cases where external vantage points found in minutes what provider NOCs couldn't find in weeks — cheap, adoptable debugging technique.
- **What**: Case 1: a serial-console server on a colo LAN became unreachable; the provider's week of debugging failed, one Atlas global/random traceroute found the problem (with hover-text and clickable hop detail as the "smoking gun"), fixed within an hour. Case 2: a friend's IPv6 was unrouted for months while the ISP NOC saw nothing; 15 Atlas probes inside that same ISP exposed the internal routing problem to a senior engineer within hours.
- **How**: RIPE Atlas (12,000+ probes) one-off measurements and traceroute visualizations, plus the measurement API for automation. Bush closes with a challenge: build an AI front-end that takes a problem description and drives the Atlas API to diagnose it — a nice framing of where troubleshooting tooling is heading.
- **Where applicable**: Anyone; free to use if you host a probe (membership not required). Scale- and vendor-agnostic.

### Conference Network Report

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/c2e37815-ae9e-4a8e-940f-c61ac8672a3c.pdf)

Yoshinobu Matsuzaki, IIJ (APRICOT Technical Committee)

- **Why**: A compact live postmortem from running a real network under load — including an IPv6-mostly deployment with measured client behavior and a genuinely unusual BGP debugging story.
- **What**: The APRICOT 2026 NOC ran dual transit (Lintasarta, Envision) plus Starlink backup, Akvorado NetFlow analysis, and an IPv6-mostly design: 609 unique MACs, 70% of clients (431) operated IPv6-only via NAT64 (DHCPv4 option 108 signaling), 30% dual-stack, 300 Mbps peak. Incidents and fixes: WiFi channel overload at the opening plenary; a BGP "ghost route" — their prefixes showed globally reachable via route-views/RIS but lacked actual reachability, traced to a longer-than-expected AS_PATH left over from an earlier temporary announcement, cleared by contacting ASes on the path (one had a config bug); a rogue AP broadcasting the same SSID/password outside controller management, fixed by a reset; and intermittent public-DNS resolution failures on IPv4 queries with RD=1, fixed by offering local resolvers via RDNSS/DHCP.
- **How**: Straightforward ops: PREF64/NAT64 for the v6-only tier, per-incident triage with community help on the ghost route.
- **Where applicable**: Conference scale, but the lessons — IPv6-mostly is now viable for 70% of unmanaged clients, stale AS_PATHs can linger as ghost routes after withdrawals, rogue APs happen even with a controller — transfer directly to enterprise and campus networks.

### Authenticating networks with RPKI RSC

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/3cdf15ce-8dae-491a-a93f-cfda8a601638.pdf)

Arnold Nipper, DE-CIX (with Yolandi Cloete)

- **Why**: Machine-verifiable proof that the party you're talking to controls the network resources it claims — network identity, which rhymes with the workload-identity problem in other domains.
- **What**: PeeringDB is introducing signup authentication for networks via RPKI RSC (RPKI Signed Checklists) in March 2026, and the talk solicits community input on follow-on features: whether to surface how and when a network authenticated, and whether to support periodic re-authentication.
- **How**: RSC objects let a resource holder sign an arbitrary checklist of their holdings; PeeringDB will use them to verify that a PeeringDB record is created by whoever actually holds the ASN/prefixes. (APNIC's annual report in the same program notes RSC objects are now provided in its RPKI services too.)
- **Where applicable**: PeeringDB-specific rollout, but the pattern — cryptographic resource-holder authentication replacing manual LOA/email verification — is general, and directly relevant to anyone building inter-org trust flows. Caveat: this is a thin lightning talk and the deck ends with a sponsorship pitch; the signal is the feature, not the depth.

## Wildcard

### IP Networking in Deep Space

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/e2575506-e364-46f1-8b4d-cfa746bfacdf.pdf)

Marc Blanchet, Viagenie

- **Why**: Not operationally relevant, but the most instructive stress test of the IP suite's assumptions you'll read this year — what breaks when RTT is minutes and links vanish for hours.
- **What**: An architecture for Moon and Mars networks in which every link carries IP: 3GPP (5G/6G) and 802.11/WiFi on the surface, CCSDS for deep space, spacecraft onboard networks also IP — creating a single Layer-3 network end to end, aligned with NASA's LunaNet interoperability specification. The core problems: Earth-Moon ~2 s one-way delay, Earth-Mars 4–22 minutes, and intermittence (an orbiter passing behind a body turns a 2-second path into a 2-hour gap; until full laser-linked constellations exist, disruptions are the norm).
- **How**: Three key adaptations, with simulations confirming suitability: (1) temporary buffering of IP packets on forwarders with intermittent links; (2) configuring QUIC with parameters matching the expected round-trip time; (3) configuring application timeouts. Everything else follows from accepting asynchronous operation as the paradigm — no interactivity, no fast remote management.
- **Where applicable**: Space-specific by subject, but the delay/disruption-tolerance findings translate to any store-and-forward or high-latency environment, and the QUIC-parameter work is a concrete example of transport tuning under extreme RTT.

### Keynote: The Agentic Shift: The Internet Industry Reimagined

Mukhammad Andri Setiawan, Universitas Islam Indonesia

- **Why**: The direction-of-field keynote: autonomous agents as operators of infrastructure — the world the IETF's WEBBOTAUTH and CATALIST efforts (see the IETF update above) are being chartered for.
- **What**: An argument that the industry is shifting from manual configuration to networks configured by agents, code generated without SQL, and ops moving from hands-on engineering to high-level coordination — with roles emerging for the next decade: "Agent Shepherds" guiding agent swarms, "Sovereignty Architects" for ethical/policy frameworks, and "Compute Brokers" managing agent-economy compute. Also covers bias and accuracy risks, and "AI sovereignty" as a national capability.
- **How**: Futures-style synthesis rather than a technical method; the same speaker's IPv6-renumbering study elsewhere in the program grounds the claim empirically (AI-assisted configuration cut measured cognitive workload ~65–72% and task time dramatically in a small within-subjects experiment, while organizational readiness lagged).
- **Where applicable**: Broad and speculative, but the trajectory it names — identity, authorization, and supervision for non-human actors — is exactly where the identity portion of this reader's portfolio is heading. *(from abstract only)*

### To Space and Back: Integrating Next-Generation Terrestrial and Satellite Communication Networks

**Links:** [Slides](https://conference.apnic.net/61/assets/presentation-files/09204dc4-859e-4df7-ac9f-24a5e3bfe055.pdf)

Katarina Stefanović, Telecom Serbia

- **Why**: A surprising measured result: LEO satellite paths, though physically longer, can beat terrestrial mobile networks on long-haul latency and stability — with real data, not vendor claims.
- **What**: A 7-day continuous RIPE Atlas measurement campaign comparing Starlink LEO connectivity against 4G/5G mobile networks across multiple European countries, targeting an APNIC-hosted host in Singapore: Starlink consistently showed lower and more stable long-haul RTT (enabled by backbone efficiency and evolving inter-satellite-laser routing), while mobile networks showed higher jitter and EPC-driven processing delays despite shorter physical paths.
- **How**: Atlas probes measuring long-haul RTT, hop-count behavior, intercontinental routing paths, and jitter distribution; plus an architecture deep-dive into LEO mesh topology, ground stations, laser inter-satellite link types (intra-plane, inter-plane, crossing-plane), and NTN–TN interoperability per 3GPP TR 38.811 — including how beam handovers, congestion, atmosphere, and PoP presence shape user experience.
- **Where applicable**: Results are European-vantage and Starlink-specific; the framework (measurement-based comparison rather than assumptions) is general. Relevant to anyone evaluating LEO as a WAN or resilience path, and to the interconnection-panel question of whether LEO edges change regional peering economics.

## Themes

- **Routing security enters the post-ROV era.** With ROV widely deployed, the program's center of gravity moved to path verification: ASPA semantics and tooling (RIPE, ARIN, bgproutes.io validating every collected route), MESec's minimal-disclosure alternative, the IXP route-server IRR blind spot, and a social-engineering hijack that RPKI origin validation alone could not stop. ASPA is the thing to learn this year.
- **Coherent pluggables made IPoDWDM real.** After the 2000s failure, hyperscaler-driven disaggregation (coherent pluggables outselling embeddeds 2:1) puts DWDM line-side optics in ordinary router ports — and pushes spectrum/grid planning (400 GHz muxes for 1.6T superchannels) onto IP teams. The two optics talks and Tinka's Cape Town reference network are the evidence.
- **Beyond best-path visibility.** bgproutes.io's BMP-based collection, RouteViews' new BMP processor and API, Erik relays fixing RPKI distribution, and RIPE Atlas as a debugging instrument — collectively, the community is instrumenting the routing system at finer granularity than best-path snapshots.
- **EVPN/SRv6 is displacing LDP/VPLS in production.** IX.br São Paulo's seamless RFC 8560 migration is the template, showing per-device replacement, flood elimination, and proxy ARP/ND as both a scale and a security win.
- **IPv6-mostly crossed from experiment to default.** The conference NOC ran 70% of clients IPv6-only via NAT64/DHCPv4 option 108, a SOHO network hit 90% IPv6 traffic, and Windows CLAT progress was cited — operators are now planning for the IPv4-absent end state rather than dual-stack forever.
- **Agents are showing up in the infrastructure stack.** The IETF chartered WEBBOTAUTH, SEAT, and CATALIST; the keynote named the agentic operating model; and the IPv6-renumbering study quantified AI assistance reducing engineer workload while organizational readiness lagged. The identity/authorization problem for non-human actors is now on the standards agenda, not just the vendor one.
