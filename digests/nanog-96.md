<!--
conference: NANOG 96
type: operator
source_url: https://nanog.org/events/nanog-96/agenda/
generated: 2026-11-01
registry_key: nanog-96
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NANOG 96

## Core

### Keynote: Beyond the Chip: The Unprecedented Infrastructure Demands of AI and HPC

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5612/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5612/20260202_Conrades_Keynote_Beyond_The_v1.pdf) · [Recording](https://youtu.be/4LAzF7f81ws)

Bill Conrades, Chris Stewart, Michael Balasko — AHEAD

- **Why**: The most concrete "facility-to-fabric" framing of AI datacenter buildouts at this meeting. For anyone whose remit includes physical DC design, this maps how power and cooling constraints now dictate network architecture choices — the limiting factors are no longer transistors but power delivery, cooling, and system-level architecture.
- **What**: A structured survey of AI/HPC infrastructure: rack density evolution from air-cooled (<10-15kW) through hybrid/liquid (30-80kW+) to liquid-everything (100-150kW+); a cooling technology ladder (perimeter CRAC → containment → rear-door heat exchange → direct-to-chip → immersion) with capacity bands per technology; and the networking backbone — AI backend (East/West, 1:1 oversubscription) vs frontend (North/South) reference architecture, rail-optimized topology for AllReduce collectives, and a useful comparative table of Ethernet variants (standard ECMP → enhanced ECMP+advanced LB → scheduled packet-spraying/VOQ → Ultra Ethernet) with honest cluster-size and losslessness trade-offs.
- **How**: Built around AHEAD's own 10MW specialized integration facility case study (permitting timelines, hybrid air + facility-water cooling, D2C and RDHx plans) plus a Gartner impact radar for timing investments (DLC and AI Ethernet fabrics rated "act now"; in-package microfluidics, HVDC, 800V distribution on longer horizons). Includes physical-layer detail: MPO/xPC/breakout planning, 800G still riding 100G SerDes with 200G SerDes emerging, DC bus bar and ORv3/MGX rack standards.
- **Where applicable**: Broadly applicable planning guidance for AI-era facilities, though presented by a systems integrator (with Cisco-credited diagrams and NVIDIA NVL72 examples), so expect consultative framing rather than an operator postmortem. The cooling-capacity numbers and Ethernet-variant table transfer to any AI DC program.

### Keynote: AI Data Center Networking: Lessons from Meta's Evolution

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5638/) · [Recording](https://youtu.be/EmTP6YHovCM)

Omar Baldonado — Meta

- **Why**: Meta operates some of the largest AI clusters in the world and, unusually for a hyperscaler, shares openly (FBOSS, TorchComms, OCP). A cross-generation retrospective on AI fabric design from the person who runs Meta's global DC networks is the highest-signal keynote on the program for physical DC networking.
- **What**: A retrospective through successive AI network deployments — what each iteration taught and where false starts occurred — framed as a stack: PyTorch/framework behavior shapes xPU selection, accelerator traffic patterns drive topology choices, NIC capabilities enable or constrain operations. Also covers network automation at scale, density constraints (power, cooling, space), telemetry for AI workloads, and managing rapid technology transitions without destabilizing production, with gigawatt-scale clusters on the roadmap.
- **How**: Lessons-learned format across production generations rather than a single architecture pitch; the value is in the cascade framing (framework → hardware → topology → operations) and the operational truths behind open-sourced artifacts like FBOSS and TorchComms.
- **Where applicable**: Explicitly Meta-scale — multi-gigawatt buildouts, custom switch OS, OCP hardware. The layer-interaction reasoning transfers to anyone designing AI clusters, but the specific density and automation numbers are org-specific (from abstract only; the NANOG content page could not be retrieved and no slides were published in the source material).

### AI Backend: Deploying SRv6 uSID and SONiC for Deterministic Load Balancing

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5611/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5611/20260202_Camarillo_Ai_Backend_Deploying_v1.pdf) · [Recording](https://youtu.be/yB-_4lkSsEs)

Pablo Camarillo — Cisco Systems; Rita Hui — Microsoft

- **Why**: The AI backend load-balancing problem is the defining fabric issue of this cycle: synchronized, bursty, low-entropy training flows destroy ECMP hash assumptions, and congestion/loss stalls GPU collectives. This is a production answer from one of the world's largest AI infrastructures, not a whitepaper.
- **What**: Microsoft's deployment of SRv6 uSID strict source routing in the AI backend for deterministic, conflict-free traffic placement, implemented in SONiC. The deck grounds it in real cost data (Llama3 406B: 6k GPUs, 54 days, 419 unplanned interruptions; a single job crash loses 15-30 minutes of compute since the last checkpoint) and includes a taxonomy of every LB approach attempted — switch-based (flowlet, adaptive routing, packet spray) and NIC-based (oblivious spray, entropy recycling) — and why probabilistic entropy-value switching can't guarantee a new path.
- **How**: GPU/NIC controls the full end-to-end path by encoding a uSID list in the packet header; on congestion or failure the NIC swaps SIDs and the path changes immediately with no state propagation through the fabric. The backend runs as a statically provisioned fabric with static SIDs and static routes — no dynamic routing, avoiding the ~120,000 packets lost when an ECMP group updates after a link flap on a fully utilized 400G link. Also covers tenancy/slicing via SRv6 policy without DPU cycles, and the SONiC SRv6 ecosystem (uN/uDT functions, FRR, contributors incl. Microsoft, Alibaba, Broadcom, Nvidia). The Alibaba eCore SRv6 DCI design is shown as the scale-across analog.
- **Where applicable**: Microsoft-scale AI backends on SONiC whiteboxes; requires SRv6-capable NICs/DPUs and merchant silicon (Broadcom/G400-class). The "deterministic path placement" idea is also feeding UEC standardization, so the architecture is transferable even where the exact stack is not. Co-presented by Cisco's SRv6 lead — expect enthusiasm — but the operational data and failure math are the substance.

### From Datacenter to AI Center, building the networks that build AI

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5627/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5627/20260202_Conrad_From_Datacenter_To_v1.pdf) · [Recording](https://youtu.be/CDJZk2SjKfw)

Tyler Conrad — Arista Networks

- **Why**: The best single "orientation map" for engineers moving from general-compute DC design to AI backends. Vendor-presented, but dense with concrete numbers you can reuse in capacity planning, and refreshingly honest about failure rates.
- **What**: A design guide across topology (single-box vs 2-tier vs 3-tier with GPU-count ceilings per form factor; rail-isolated vs rail-optimized vs fat-tree; multi-plane scaling by port-speed fan-out — 1x800G/2x400G/4x200G), subscription ratios (target 1:1 or better), optics economics, load balancing and congestion control (ECMP hashing vs RDMA-aware static hashing vs DLB vs packet spraying vs SRv6 steering), RoCEv2 mechanics (DCQCN, PFC victim flows, ECN/ECT tuning, a concrete QoS queue design with CNP in SP queues), and segmentation options from VLANs to VRFs to SRv6 uSID.
- **How**: Prescriptive with arithmetic: for a hypothetical 100k-GPU back-end, 257,904 links and 515,808 optics; at 2.3M-hour MTBF that is one optic failure roughly every 4.45 hours — about five per day. LPO optics (no DSP, DSP moved into switch silicon) claimed at ~0.5x power, ~0.7x cost, ~0.01x latency. Includes a common-failure checklist (QoS mismatch, dirty fiber, FEC/autoneg mismatch, MMU tuning) that mirrors what real AI-cluster escalations look like.
- **Where applicable**: Greenfield AI back-end builds; the talk's own takeaway is that back-end reuse of existing gear is unlikely and power/heat is usually the first constraint. Arista perspective throughout, so silicon-specific framing (radix/speed tables) should be re-derived for other vendors.

### Multipath Traffic Engineering for WAN & AIDC

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5667/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5667/20260204_Kompella_Multipath_Traffic_Engineering_v1.pdf) · [Recording](https://youtu.be/nYef0pTpEgs)

Zhaohui (Jeffrey) Zhang — HPE (with Kireeti Kompella)

- **Why**: Challenges a 25-year-old either/or — you could have ECMP load balancing *or* fine-grained TE with bandwidth control, not both. Kompella (co-author of the original MPLS TE RFCs) proposing a unified construct for both WAN and AI datacenters is a notable architectural signal, and the IETF drafts are live.
- **What**: MPTE programs an optimally weighted load-balancing DAG (MPTED) across the network: a single construct with per-junction split ratios replaces the many parallel LSPs that conventional TE needs to fill fat pipes (their example: 1600 Gbps R1→R12 needs four LSP constructs conventionally, one MPTED with 25/25/50/50 splits under MPTE). Link failure adjusts junction ratios without reshaping the DAG; multiple ingresses and multiple egresses (multi-egress load spreading, not multicast) are supported with far less state than per-path tunnels.
- **How**: Junction state = incoming bandwidth + previous-hops + next-hops with weighted load shares; signaling via RSVP-TE (prototype), with BGP/PCEP/programmable-API (gRPC, YANG-backed) prototypes underway. Contextualized against the existing toolkit (auto-bandwidth, container LSPs/TE++, cBPS AI/ML bandwidth prediction, tactical TE), and connected to the new IETF RTGWG conversation on ML network scheduling (`draft-kompella-rtgwg-mlnwsched`) — reserving and isolating network resources per inference/training task, since TE only makes sense in an ML cluster when it is split among multiple tenants/tasks.
- **Where applicable**: WAN/MAN/DCI and multi-tenant AI clusters; assumes MPLS or IP-tunnel data planes and a controller/computer to originate MPTEDs. IETF draft-stage — conceptual architecture now, not shipping broadly. HPE/Juniper-heritage perspective.

### EVPN Interconnect Architecture for Resilient Multi-Domain Fabrics

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5646/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5646/20260203_Brissette_Evpn_Interconnect_Architecture_v1.pdf) · [Recording](https://youtu.be/BvTKsAk47o8)

Patrice Brissette — Cisco Systems

- **Why**: Multi-site EVPN over heterogeneous underlays (IPv4 WAN meeting IPv6 DC fabrics) is exactly the DC/WAN interconnect problem the PM owns. This is a coherent answer to the two failure modes that plague DCI overlays: control-plane stability during fabric isolation, and L2 loops across sites.
- **What**: A hierarchical multi-site design where each fabric stays an independent EVPN domain and Border Gateways provide DCI: dual physical-IP VTEPs per BGW (one for the DC domain, one for the WAN domain) so tunnels are terminated and re-originated at the BGW — creating a clean scaling and policy boundary. Key mechanics: Inter-site ESI for all-active BGW multi-homing, DF/NDF election with local-bias BUM forwarding rules and explicit per-bridge egress filtering to prevent loops, Normalized-VNI translation to resolve overlapping VNIs between independently administered sites, downstream-assigned VNI option, host mobility via /32 advertisement re-origination, and step-by-step packet walks for L2 unicast, BUM, and L3 flows.
- **How**: Failure-isolation walkthroughs for both WAN loss and DC loss show the alternate BGW-to-BGW path preserving host reachability; decoupling DC from WAN VTEP space means either side can change without re-coordinating.
- **Where applicable**: Any multi-site EVPN/VXLAN program; not tied to specific silicon, though presented by Cisco's lead EVPN architect (and SONiC routing workgroup chair), so feature availability on non-Cisco gear (I-ESI, normalized VNI) should be verified. Concepts (re-origination boundary, VNI normalization, DF local-bias) transfer across vendors.

### Decentralizing Software Defined Networking: The Hidden Complexities of SDN & What We Can Do About Them

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5681/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5681/20260202_Krentsel_Decentralizing_Software_Defined_v1.pdf) · [Recording](https://youtu.be/X1n-xOrCa-k)

Alexander Krentsel — Google / UC Berkeley

- **Why**: A rare quantified indictment of centralized SDN: at Google, >50% of large outages are root-caused to the control plane itself — the dedicated controller infrastructure, control-plane network, instrumentation services, and fallback protocols that SDN drags in. For anyone building WAN control systems, this is the architecture conversation to have.
- **What**: Decentralized SDN (dSDN): run the operator's SDN control program as a container on every router instead of on external servers. Each node floods its local state (topology, link capacities, demand), each node independently computes all paths with the operator's TE algorithm, and traffic follows strict source routes programmed at the ingress. This removes central/regional controller jobs, dedicated servers, the control-plane network, instrumentation services, and traditional fallback protocols from the critical path while keeping SDN's benefits (operator-defined code, global-view TE, consensus-free path selection) and restoring fate-sharing between control and data planes.
- **How**: Enabled by three industry shifts: on-router third-party containers, standardized APIs (gRIBI, gNMI, OF/P4), and multi-core router CPUs. Source routing makes decentralization simple — historically infeasible in WANs due to path length in the header, now practical via hardware advances and a novel encoding (details in the paper). Evaluation: a production-grade implementation on real routers, fed live B4 topology and demand, replaying production failure events — convergence 120-150x faster than centralized SDN (faster propagation and programming outweigh slightly slower local computation) with markedly lower convergence impact on low-priority traffic.
- **Where applicable**: Global WAN operators (Google B4-class). Requires vendor on-router container support and vendor-neutral programmatic APIs — realistic on modern platforms but a real dependency. Research-to-production direction from Berkeley NetSys + Google, not a deployable product; the simplification argument (fewer components on the critical path → fewer complex cascading outages) generalizes to any control-plane design review.

### Redefining Netflix BGP architecture

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5574/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5574/20260202_Cuiller_Redefining_Netflix_Bgp_v1.pdf) · [Recording](https://youtu.be/LOZDX7BlO74)

Fred Cuiller — Cisco; Elise Vennegues — Netflix

- **Why**: A large, real BGP architecture migration with the validation methodology, defect discovery, and phased cutover shown — the parts that usually get omitted. Netflix's edge is 400+ PoPs, 19,000+ OCAs, ~175 countries, 20,000+ eBGP sessions to 2,800+ ASNs; moving that off iBGP full-mesh is a serious operational story.
- **What**: Replacement of iBGP full mesh between Edge Switches and Provider Edge routers with a route-reflector hierarchy built on Cisco IOS XRv9000 UCS M7 appliances (chosen over traditional routers and VNFs on integrated TPM, CoPP, operational simplicity). RRs placed in six global sites; production scale runs to 37M IPv4 paths / 300+ clients in North America, 20M paths / 250+ clients in EMEA. Interesting appliance-selection comparison table (router vs VNF vs appliance across scale, CoPP, security, cost).
- **How**: Early Field Trial with the vendor caught real defects before deployment (early-release memory leak, BGP process rlimit misassignment, duplicated LLDP entries on Mellanox NICs); one miss escaped lab — telemetry YANG path performance at scale with sub-60s polling, discovered only in pre-production, reinforcing that production churn/scale is unique. Migration: phased per-device (staging RR peering with pilot prefixes → release prefixes to RR → per-device depref-then-pref-up → remove mesh), driven by internal tooling with a per-device migration tag; telemetry dashboards track CPU/memory, session counts, and received paths per address family. BMP activation is the stated next step.
- **Where applicable**: The Cisco appliance choice is Netflix/Cisco-specific, but the RR placement reasoning, EFT-style validation discipline, phased-migration mechanics, and telemetry checklist transfer to any iBGP-mesh-to-RR program at hundreds-of-PoPs scale.

### Lightning Talk: Seeing Through the RDMA Fog: Monitoring RoCEv2 with sFlow

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5718/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5718/20260204_Phaal_Seeing_Through_The_v1.pdf) · [Recording](https://youtu.be/vM-M0vtvxLI)

Peter Phaal — InMon Corp.

- **Why**: AI/RDMA clusters create a genuine blind spot: kernel bypass means tcpdump, wireshark, and even eBPF-based host agents see nothing. For a PM who tracks both lossless fabrics and host-based observability (eBPF), this is the counterpoint — some visibility has to come from the switch ASIC.
- **What**: A demonstration, on SDSC's Expanse production cluster (93k cores, 208 GPUs, 100G hybrid fat-tree), of sFlow-based RoCEv2 monitoring: RDMA I/O operations decoded from sampled packet headers (opcode, queue pair, PSN, DMA length, virtual address), ECN/CNP congestion-message rates, RoCE ack-credit tracking, per-link queue depth and transit delay, and — critically — immediate notification of every dropped packet with where/why/who.
- **How**: Standard sFlow agents in leaf/spine switches stream sampled headers and counters over the out-of-band management network (no interference with RoCE); three lines of SONiC config enable it (`sflow collector`, `sflow drop-monitor-limit 50`, `sflow enable`), similar on Arista/Cisco/Dell/NVIDIA. `sflowtool` + `tshark` decode the InfiniBand transport headers from samples; new extensions add per-sample transit delay/queue depth and per-discard reports (reason-coded, e.g. `dst_net_unknown`). Ultra Ethernet is just another header format for the pipeline — no agent change needed.
- **Where applicable**: Broadly applicable — this is a standard switch feature, not new silicon, and the technique covers exactly the visibility gap that host tooling cannot. Drop-notification support requires current releases (202511 SONiC for drop-monitor). The one honest caveat: sampling-based, so it complements rather than replaces per-flow precision.

### Shaping the Future of BGP Observability: BMP Evolution at IETF

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5660/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5660/20260202_S_Shaping_The_Future_v1.pdf) · [Recording](https://youtu.be/jH_vtDDX9sQ)

Narasimha Prasad S — Cisco (with Paolo Lucente, NTT DATA; Thomas Graf, Swisscom)

- **Why**: BMP is quietly becoming the vendor-neutral BGP telemetry substrate, and its IETF evolution this cycle is substantial. If the PM's world includes BGP monitoring pipelines (and the Netflix talk explicitly names BMP activation as next), this is the standards map.
- **What**: A structured tour of the foundational RFCs (7854 Adj-RIB-In, 9069 Loc-RIB, 8671 Adj-RIB-Out — including the useful correction that pre-policy Adj-RIB-Out is *not* the Loc-RIB) and then the active drafts: BMPv4 TLV-ization making all message types extensible; Path Marking, which exports the best-path decision outcome per path with reason codes (finally answering "why wasn't this path installed" without memorizing the 13-step selection process); structured timestamps separating trigger time from export time; Generic Event Notification for non-route events; Route Event Logging for alerting on policy discards and validation failures; Snapshots for mid-stream collector sync and time-binned archives; ~20 new statistics types; and a YANG model for managing what gets exported.
- **How**: Performance drafts attack BMP's high-scale cost — Route Monitoring Aggregation across peers, Common Updates across RIB-views (up to 4x), and Multi-Peer headers — claiming up to n-fold reduction in router/collector CPU and message volume. Security: TCP-AO as the RFC 7854 IPsec alternative, plus early BMP-over-QUIC (multi-streaming + TLS) and BMP-for-RPKI-monitoring proposals.
- **Where applicable**: Standards-track and vendor-agnostic; directly relevant to anyone building or buying BGP observability. Implementation timing varies by draft status (some are WG documents, some proposed work) — the talk's own closing point is that operator use cases should drive which drafts advance.

### RoVista+: Mapping Real ROV Deployments, Dependencies, and Delays

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5544/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5544/20260204_Chung_Rovista_Mapping_Real_v1.pdf) · [Recording](https://youtu.be/dvB_Nt8z2yg)

Tijay Chung — Virginia Tech

- **Why**: "Do you filter RPKI-invalids?" has always been hard to answer honestly — prior methods couldn't tell local enforcement from an upstream doing it for you. This work separates the two, and the findings about RP (relying-party) concentration are a systemic-risk result every operator should see.
- **What**: A measurement framework that runs its own ASN and its own RPKI publication points, serving different test ROAs to specific relying parties, then probing the Internet to see who drops the route. Results across 21,827 measured ASes: 1,127 self-deploy ROV while 1,815 ASes rely entirely on upstream filtering — and 69.6% of those "protected" ASes remain vulnerable to local hijacks. 52% of ROV-deploying ASes depend on exactly one RP server (only 14% use multiple RPs in different ASNs, contra RFC 7115). Router enforcement lags ROA updates by ~37 minutes (60-120 minutes end-to-end). Simulation: ROV in the top 100 ASes protects 27.6% of networks; disabling it in Tier-1s exposes 23.8% to hijacks. ~74% of top-5,000 ASes self-deploy; smaller networks overwhelmingly depend on upstreams.
- **How**: Dynamic publication points + controlled test-ROA-to-specific-RP delivery + Internet-wide ping/traceroute scanning. Timing-based inference distinguishes upstream filtering (downstreams drop in synchronized clusters when the upstream filters) from self-deployment (independent drop times due to unaligned RTR polling) — validated against Comcast (private RP, synchronized), Cloudflare (public RP, varied), and NTT (both patterns).
- **Where applicable**: The tooling and datasets are open-sourced, and the operational lessons are immediate for everyone: diversify your RPs across ASNs, and understand your ROV posture may be inherited rather than enforced. The methodology (selectively invalidating to one RP at a time) also generalizes to AS-path exploration. Research-grade but production-relevant.

## Adjacent

### Removing Barriers to RPKI Adoption

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5355/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5355/20260202_Testart_Removing_Barriers_To_v1.pdf) · [Recording](https://youtu.be/GSG4dxbbrnw)

Cecilia Testart — Georgia Institute of Technology

- **Why**: ROA coverage passed 50% but adoption is uneven, and this is a rigorous answer to *why*: it identifies planning complexity — not awareness — as the choke point, with numbers on where the remaining headroom is.
- **What**: Combines 13 semi-structured operator interviews with BGP/WHOIS/delegation/RIR data analysis, framed by a technology-adoption model (RPKI is in the late-majority phase). Four barrier areas: IP resource management (years of poor recordkeeping), awareness/training, RPKI software, and monitoring/incident tooling. The core contribution is a systematic ROA-planning framework — who can issue, which more-specifics are routed, which delegations/other orgs are involved — made concrete via `ru-RPKI-ready`, a platform characterizing unrouted space: 47% of IPv4 and 71% of IPv6 prefixes not in RPKI could be covered with minimal technical effort, and if just ten organizations acted, global coverage would rise 7% (IPv4) and 19% (IPv6).
- **How**: Worked examples show a single /20 requiring 7 ROAs across 7 origin ASNs and two organizations — the realistic complexity that scares operators off. RIRs are identified as pivotal actors across all four barrier areas.
- **Where applicable**: Most actionable for small/mid-size operators and RIR outreach programs; the planning framework and tool are directly usable for anyone with messy, inherited address space.

### Improving Routing Security for Global Research and Education

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5650/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5650/20260202_Wallace_Improving_Routing_Security_v1.pdf) · [Recording](https://youtu.be/fYwv5X4eCZw)

steven wallace — Internet2.edu (with CAIDA, per ROOTBEER/NSF CICI)

- **Why**: R&E networks deterministically prefer R&E routes over commodity, which makes their route leaks high-impact (US scientific traffic transiting unintended international paths). Beyond the R&E story, this is a template for measuring local-pref policies you cannot see in public BGP views.
- **What**: A measurement system that announces the *same* prefix from two origins — one via an R&E path (Internet2), one via commodity transit — with varying AS-path prepends, then pings responsive hosts to infer which route each of ~2,600 R&E ASes actually chose. June 2025 results: 80.8% of prefixes/75.3% of ASes always used the R&E route regardless of prepending; 7% always commodity; ~9% switch by AS-path length (implying equal local-pref). Real 2024 incidents documented: a South American R&E network leaking commercial routes (traffic rerouted through South America) and a Middle East member leaking R&E routes to a commercial provider (cloud return traffic transiting the Middle East, some members withdrawing specifics defensively).
- **How**: Building on this, the ROOTBEER project is constructing an operational routing-security observatory at Internet2 — leak detection between R&E and commodity, a stakeholder dashboard, and a move toward an actively maintained public route filter on all peers, shareable by other R&E transit networks.
- **Where applicable**: R&E-specific topology (route-preference policy), and public BGP visibility is thin here (only 27 of 2,659 R&E ASes provide RouteViews/RIS views). The dual-origin measurement technique, though, transfers to any policy-visibility problem, and the public-filter approach is a model for any community network with trusted transit.

### BGP in 2025

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5629/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5629/20260204_Huston_Bgp_In_2025_v1.pdf) · [Recording](https://youtu.be/Sm1HjdmoeeA)

Geoff Huston — APNIC

- **Why**: The annual ground truth on DFZ health — directly relevant to FIB sizing, deaggregation trends, and (this year) a genuinely new datapoint: the IPv4 routing table and the advertised address span are now moving in opposite directions.
- **What**: IPv4 FIB passed 1M entries for all peers, yet the *advertised address span* shrank by 11M /32s during 2025 (3.1B advertised vs 580M unadvertised, +10M) — IPv4 use declining in access networks (notably the US) while cloud use still grows. Biggest movers: China Mobile (+13,382 prefixes), Amazon (+14,004), AT&T (−2,605, echoing its consolidation described in the Ukraine talk), IPXO broker growth visible. Amazon's super-aggregate games through the year (+4.3M, −15.8M, +15.1M address swings). IPv6: ~20k entries/year (~10%) growth with 45% of prefixes being /48s; 2,096 new IPv6 advertisers vs 956 departing. Projections: best 5-year fit still polynomial for IPv4 but a 3-year linear fit is competing; IPv6 growth model highly uncertain.
- **How**: Longitudinal analysis across Route-Views/RIPE RIS peers; churn (updates/withdrawals) notably stable — the IPv4 network is "surprisingly stable" with withdrawals flat for ~15 years.
- **Where applicable**: Universal for capacity planning and RIB/FIB trend work. The headline nuance — prefix count growing while address span shrinks — matters for anyone modeling router table growth or arguing about IPv4 scarcity.

### Automation for Operations -- T-Mobile Journey

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5556/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5556/20260204_Abu_Eid_Automation_For_Operations_v1.pdf) · [Recording](https://youtu.be/kb9DMzX9134)

Issa Abu Eid, Udaya Tadikonda — T-Mobile USA

- **Why**: A Tier-1 operator's account of moving from manual workflows to automation-first operations, with the guardrail design spelled out — the "how do we make automated actions safe" question is where most automation programs actually fail, and this addresses it head-on.
- **What**: Reactive and proactive automation categories: alert correlation/deduplication and auto-created tickets with SLA clocks starting at detection, multi-signal service-aware outage detection with impact identification before customers notice, guarded break/fix (explicitly *not* automating ambiguous failures or one-off fixes; every automated action gated by redundancy-aware checks, capacity validation, audit trail, and rollback), pre/post-change validation with policy-driven rollback evaluation, continuous compliance/drift/EOL-EOS monitoring, and capacity early-warning with trend analysis. A maturity model — Visibility → Intelligence → Enablement — with the honest sequencing rule that automation cannot succeed without reliable state and that early efforts must focus on visibility, not action. AI is framed as an assistive layer on top of strong automation foundations, not a replacement for operator judgment.
- **How**: Automation treated as production software; one deliverable described is a centralized internal platform used by 1,300+ engineers with incident correlation across multi-vendor networks.
- **Where applicable**: T-Mobile US Tier-1 scale (org-specific tooling and metrics), but the guardrail taxonomy, the "explicitly not automated" list, and the visibility-first phasing are directly transferable patterns for any operations organization, including much smaller ones.

### Exodus of IPv4 from War-torn Ukraine

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5635/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5635/20260202_Madory_Exodus_Of_Ipv4_v1.pdf) · [Recording](https://youtu.be/7P_ybLSEQlw)

Doug Madory — Kentik

- **Why**: A striking data story about IPv4 as a war-driven national commodity, with direct consequences for anyone reasoning about IP address markets, proxy abuse, and routing-table hygiene — it also explains several of the movers in this year's BGP table.
- **What**: Four years of war produced a ~20% reduction in Ukraine's footprint in the global routing table. Ukrtelecom's AS6849 dropped from 4,728 to 1,377 /24s (−71%), with the space leased via brokers (IPXO) and re-originated by Amazon, Windstream, NTT, Lumen, Orange; sister ASN AS6877 vanished from the table entirely. Mariupol's Trinity (AS43554) space popped up under as many as 54 foreign ASes and was confirmed in use as residential-proxy infrastructure. The second act is AT&T's 2025 BGP housekeeping: AS7018 collapsed from 3,200+ IPv4 routes to 641 via super-aggregation and a new policy requiring customers to originate from their own ASN — which chased out the proxy services; the displaced prefixes scattered across ~150 new origins. Also covers AWS's Dec 2024 move to originating 1,000+ super-aggregates (IPv4 footprint 49M → 157M addresses, absorbing space from Volia and legacy ranges) and similar patterns in Iran (Hetzner as recipient).
- **How**: Longitudinal BGP/WHOIS analysis; RIPE database version-diffing to document the "Russification" of registrations and subsequent purging of records; proxy-use confirmation via Krebs's investigation.
- **Where applicable**: Global — this is analysis anyone can replicate with public data, and the lessons (origin-ASN policy as abuse defense, prefix-count consolidation, broker-mediated leasing risks) apply to any large origin AS.

## Wildcard

### End-system controlled, dynamic multihoming and multipath transport

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5628/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5628/20260203_Bhatti_End-System_Controlled_Dynamic_v1.pdf) · [Recording](https://youtu.be/4Va3xvNleWE)

Saleem Bhatti — University of St Andrews, Scotland, UK.

- **Why**: Multipath today means MPTCP or waiting on QUIC multipath. This demonstrates generic, end-system-controlled multipath for *any* transport — with working code, real transatlantic tests, and no changes to routers, applications, DNS infrastructure beyond what exists, or routing. It is a genuinely different architectural bet worth knowing about even if you never deploy it.
- **What**: ILNP (Identifier-Locator Network Protocol, RFCs 6740-6748) reuses IPv6 address syntax but splits semantics: the routing prefix acts as a mutable *Locator* while the remaining bits become a stable end-system *Identifier* — only end systems examine the Identifier bits, so IPv6 routers forward unchanged. Transport state is keyed on the Identifier (not the address), so a connection survives locator changes; dynamic multihoming and multipath are signaled end-to-end via ICMPv6 Locator Updates, no NAT, tunnels, or proxies.
- **How**: A FreeBSD 14 implementation tested between IETF 124 in Montreal and St Andrews: dynamic 4-way multipath with TCP CUBIC over iperf3, and DASH video streaming over nginx + Firefox with 3-way multipath — using standard, unmodified applications and libraries. Supporting ecosystem exists: DNS NID/L64 records (RFC 6742) in BIND, Unbound, Knot; a Wireshark dissector (v4.6+); FreeBSD binaries published.
- **Where applicable**: Research testbed; IPv6-only; requires ILNP-aware end-system stacks (FreeBSD today). No network-side prerequisites, which is the interesting inversion — the network stays dumb and the edge controls path selection. Position this as a direction signal for edge-controlled multipath rather than a deployable capability.

### IP Geofeeds: Trust, Accuracy, and Abuse

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5678/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5678/20260202_Ardi_Ip_Geofeeds_Trust__v1.pdf) · [Recording](https://youtu.be/fip6Y2SLdvU)

Calvin Ardi — IPinfo (with Oliver Gasser, William Leung)

- **Why**: Self-published IP geolocation (RFC 8805) is now consumed by every major geolocation provider and feeds compliance decisions (gambling law, content geo-blocking) — and this is the first large-scale measurement of whether geofeeds are *true*, plus documentation of active adversarial abuse of the format. Not a typical PM search topic, but the findings are broadly useful.
- **What**: Validation via two methods: RTT multilateration from a ~1,300-probe global network (27.7M RTTs covering 205k IPv4 / 74.5k IPv6 prefixes) and GPS ground truth from mobile devices. Results: country-level consistency 92% (96.6% IPv4, 79.6% IPv6), but city-level only 79.6% for infrastructure measurements (median error a startling 759 km) and just 29.9% on mobile networks — the gap between infrastructure location and actual user location. Top mismatch sources: CDNs, tier-1s, VPNs, cellular, IP leasing. Adversarial geofeeds are real and quantified: one maps ~101k IPv6 prefixes to 249 countries and ~80k cities (including Antarctica and North Korea); 17 of 20 popular VPN providers had exit traffic in a different country than claimed; public guides exist for crafting metadata to manipulate geolocation databases.
- **How**: Proposals to fix the ecosystem: format updates (validity periods/TTL, standardized location identifiers such as H3), validation and feedback mechanisms (geofeed-validator, OpenGeoFeed), and public/private hosting options — with an IAB workshop and possible future IETF WG.
- **Where applicable**: Anyone publishing geofeeds (the companion best-practices talk gives authoring guidance) or consuming geolocation for compliance/security. The mobile-network city-level number is the one to remember when someone proposes city-level geo-enforcement.

### The BGP Clock and the BGP Observatory: Hunting Stuck Routes​

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5599/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5599/20260204_Sanjta_The_Bgp_Clock_v1.pdf) · [Recording](https://youtu.be/nrQppEUZJO4)

Kemal Sanjta — Cisco ThousandEyes

- **Why**: BGP zombies — routes that persist in RIBs long after withdrawal because a router lost the UPDATE — happen hundreds of times a day on the public Internet and quietly direct traffic onto dead or congested links. Prior work showed withdrawn-and-RPKI-invalid prefixes persisting for *months*; this is the follow-up operational tool, and it's free.
- **What**: The BGP Clock: a continuously running beacon that advertises a fresh prefix every 10 minutes and withdraws it, encoding time in the prefix itself (IPv6 `2a0d:3dc1:NNNN::/48`, N = 10-minute index since Jan 1, recycled yearly; IPv4 `147.189.(216+N).0/24`, N = hour mod 8, recycled every 8 hours — details retrievable via `whois`). Anyone can check their own RIBs for stale entries. On top of it, the Stuck Route Observatory: a free, no-login web tool where you search by AS and see whether stuck routes are present in your paths, plus a heuristic guess at whether the failure to propagate a withdrawal is yours or an upstream's. RFC 9687 is the new standards attempt at reducing impact — the presenters explicitly ask operators to request vendor support for it.
- **How**: Beacon advertise/withdraw cycles correlated against RIPE RIS, RouteViews, and Cisco's near-real-time monitors. Honest limitations: direct visibility covers ~1,500 ASNs (~1% of all), extended to >50% via customer-cone inference; IXP route servers can misattribute blame; intra-AS inconsistency (only some routers in a large AS holding the stuck route — found cases with just 5% of a Tier-1's downstreams seeing it) makes root-causing genuinely hard, with BMP named as the partial future fix.
- **Where applicable**: Universal — any operator can check their AS in the Observatory today and grep their RIBs for the clock prefixes tonight. The measurement-visibility limits mean absence of evidence isn't evidence of absence, but it's the best available Internet-scale stuck-route diagnostic.

### Lightning Talk: You Don't Need The DNS Root Server System

**Links:** [Abstract](https://nanog.org/events/nanog-96/content/5731/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5731/20260204_Hardaker_You_Don_T_Need_v1.pdf) · [Recording](https://youtu.be/xog1Uerjq8g)

Wes Hardaker — Google (with Geoff Huston, Warren Kumari, Jim Reed)

- **Why**: A DNS root server operator standing up at NANOG to ask you to *stop sending him traffic* is the most memorable pitch on the program, and it's technically sound: your resolver can hold the entire signed root zone locally (RFC 7706/8806). Root query load grew ~40% in two years to 130B queries/day — for data resolvers could already have.
- **What**: The case for LocalRoot: fetch the ~1.5MB signed root zone 2-3x/day from IANA/CDN sources, serve it locally. Security improves (DNSSEC validation of unmodified data, ZONEMD integrity), robustness improves (multiple sources and protocols; survives a 24h+ DDoS of the root system), privacy improves (no queries to root at all), and performance improves (root RTT = 0, ~1.5-2.4MB/day of bandwidth).
- **How**: Trivial deployment paths shown for the three major resolvers: Knot Resolver's `prefill` module, BIND `type mirror`, Unbound `auth-zone` with the IANA root-zone URL and prefetch. AXFR adoption to B-Root already visible and growing. Active IETF drafts (`draft-wkumari-dnsop-localroot-bcp`, publication-point and transfer-scheme drafts) aim to standardize and default this in 2026.
- **Where applicable**: Any recursive-resolver operator, from enterprise to ISP; no client-side changes. The one cultural hurdle is accepting that the root system becomes an emergency backup rather than the bootstrap queried every time — exactly the inversion the talk argues for.

## Themes

- **AI back-end networking has absorbed the datacenter track.** Keynotes (AHEAD, Meta), the SRv6/SONiC deployment, the Arista AI-center guide, MPTE, and RDMA observability all attack the same problem: synchronized, low-entropy GPU collectives break hash-based assumptions that general-compute DC design relied on for 20 years.
- **Determinism is displacing ECMP.** Across Microsoft's SRv6 path pinning, Kompella's weighted MPTE DAGs, dSDN's ingress-authoritative source routes, and the load-balancing taxonomies in two other talks, the convergent answer is explicit path control — in the packet header — instead of hoping hashes spread traffic.
- **Routing security is moving past "deploy RPKI" to measuring who actually filters.** RoVista+ (single-RP concentration, 37-minute enforcement lag), the RPKI adoption-barrier study, ROOTBEER's local-pref inference, and root-prefix hijack monitoring collectively show the community auditing the *quality and fragility* of protections already nominally in place.
- **Observability is chasing new blind spots.** Kernel bypass blinds host tools to RDMA (sFlow from the switch ASIC is the answer), BMP is being upgraded to answer "why was this path not chosen," and stuck-route beacons expose withdrawal loss invisible to public collectors — three different layers, same pattern.
- **Physical constraints are the binding resource again.** Power delivery, cooling technology ladders, optics failure arithmetic (a 100k-GPU back-end implies ~5 optic failures/day), LPO economics, and 800V/HVDC distribution appear across both keynotes — facility and fabric design have re-converged into one problem.
- **IPv4 scarcity economics are now visible in the routing table itself.** Ukraine's address exodus, AT&T's origin-policy cleanup, cloud-provider super-aggregation, and BGP-in-2025's finding that the advertised IPv4 address span shrank 11M addresses while prefix count grew all describe the same late-IPv4 market dynamics.
