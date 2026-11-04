<!--
conference: DENOG 17 (Essen)
type: operator
source_url: https://www.denog.de/de/meetings/denog17/agenda.html
generated: 2026-11-04
registry_key: denog-17
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# DENOG 17 (Essen) — Digest

## Core

### Ultra Ethernet: Addressing AI/HPC Interconnect Challenges Beyond the InfiniBand Monopoly

**Links:** [Abstract](https://pretalx.com/denog17/talk/W8W77A/) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEtherne_RJk4QyN.pdf) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEtherne_vMqLytv.pdf) · [Recording](https://www.youtube.com/watch?v=8XWOzSVJHHA)

Andreas Roeder (Nokia)

- **Why**: Ultra Ethernet is the emerging standard for AI/HPC fabrics — directly relevant to anyone working on RDMA, lossless Ethernet, and next-gen DC interconnect. The PM's interest in RDMA/lossless fabrics makes this the single most strategically important talk at the conference.
- **What**: A comprehensive technical walkthrough of the Ultra Ethernet Transport (UET) specification as published by the Ultra Ethernet Consortium (June 2025 spec), covering how it differs from RoCEv2 and InfiniBand. Covers the InfiniBand lock-in problem and how Ethernet's ecosystem advantage (multi-vendor NICs, optics, cables, tooling) positions UET for AI/HPC build-outs.
- **How**: UET reuses what works from RoCEv2 (RMA verbs, RDMA semantics via LibFabric API) and redesigns the transport: a Packet Delivery Sublayer (PDS) with four delivery modes (RUD, ROD, RUDI, UUD), packet-spraying ECMP (no long-lived flows), per-packet memory semantics (each packet carries its own memory address — no reorder buffer needed), trimmed-packet NACK for selective retransmission, and dual congestion control (NSCC for network signals + RCCC receiver-credit for incast). Runs on standard Ethernet (lossy OK — no PFC required), IPv4/IPv6, with Day-1 security.
- **Where applicable**: Any operator or architect evaluating AI/HPC fabric technology choices. The spec is vendor-neutral and multi-vendor by design. Relevant to hyperscaler-adjacent and enterprise DC operators planning GPU/XPU interconnects in the next 2–3 years. Nokia-employee speaker but content is spec-grounded, not a pitch.

### Forwarding packets at scale - Building a Cloud Data Plane using eBPF/XDP

**Links:** [Abstract](https://pretalx.com/denog17/talk/VNLHD7/) · [Slides](https://pretalx.com/media/denog17/submissions/VNLHD7/resources/slides_tUew2WC.pdf) · [Recording](https://www.youtube.com/watch?v=3G_gL7nvwVE)

Maximilian Wilhelm, Marcus Wichelmann (Hetzner)

- **Why**: Hetzner replaced an Open vSwitch-based cloud dataplane with a custom eBPF/XDP stack serving hundreds of thousands of cloud servers — a production deployment of eBPF as a cloud data plane at real scale. Directly relevant to the PM's eBPF/datapath interests.
- **What**: The `hcnet` XDP-based network stack handles public and private cloud networking (VXLAN encapsulation), stateful firewalls, DHCP, traffic capture — all in XDP with a Go control plane. Running in Hetzner's internal cloud for two years, approaching public beta. Covers architecture, challenges, and current XDP limitations (offloading, driver maturity).
- **How**: eBPF programs at the XDP hook handle ARP/NDP/ICMP responding, port security, stateful firewall (compiled from a ruleset definition into eBPF instructions via graph optimization), VXLAN VTEP, and DHCP/metadata server. Diagnostic tooling (`hcnet capture`, conntrack map inspection) provides per-interface stats and pcap capture from XDP. Self-healing design with meaningful metrics. Kernel patches submitted for tun XDP metadata support; active upstream driver bug engagement (e.g., ixgbe bonding).
- **Where applicable**: Cloud/hosting providers, large-scale Linux-based fabrics. The approach requires deep in-house eBPF expertise and willingness to maintain kernel patches. Hetzner-specific scale (hundreds of thousands of servers) but the architecture patterns (XDP gateway per node, stateful firewall in BPF, Go control plane) are broadly adoptable.

### Fun with Optics

**Links:** [Abstract](https://pretalx.com/denog17/talk/AXEKSR/) · [Slides](https://pretalx.com/media/denog17/submissions/AXEKSR/resources/2025-DENOG-Fun_wit_0buk8u3.pdf) · [Recording](https://www.youtube.com/watch?v=DVyIFddJ1p0)

Patrick Prangl (Arista Networks)

- **Why**: An excellent state-of-the-union on the optics transition to 800G/1600G — covering merchant silicon roadmaps (51.2T shipping, 102.4T this year, 204.8T in 2027), Linear Pluggable Optics (LPO), and ZR/ZR+ coherent evolution. Core physical DC optics content.
- **What**: A structured overview of switch silicon evolution (Broadcom Tomahawk/Jericho generations), 800GbE standardization (IEEE 802.3ck/df, 800GBASE-ETC-R), the 100G→200G SerDes transition, LPO vs LRO vs CPO (all are the same linear-interface technology — difference is packaging position: front-panel pluggable, near-package, or co-packaged), 800G LPO performance data (7.5W typical vs 15W DSP, <3e-10 BER, multi-vendor interop proven), and ZR/ZR+ coherent DCI evolution to 800G and 1.6T.
- **How**: LPO removes the DSP from the optics module (50%+ power reduction at 800G) by relying on the switch ASIC's high-quality SerDes to drive the optical lanes directly. CPO/NPO/LPO share the same <20dB D2D channel-loss requirement. ZR+ uses multi-rate coherent with oFEC for ROADM/metro links; Coherent Lite targets 20km DCI at 800G/1.6T.
- **Where applicable**: Any DC operator planning 800G/1600G deployments. LPO is immediately relevant for short-reach (in-rack/adjacent-rack) AI clusters where power per port is a constraint. Arista-branded but the data is vendor-neutral (MSA specs, IEEE standards, plug-fest results).

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Abstract](https://pretalx.com/denog17/talk/8N7Q3A/) · [Slides](https://pretalx.com/media/denog17/submissions/8N7Q3A/resources/Flexoptix_-_Channe_Xqpo1a5.pdf) · [Recording](https://www.youtube.com/watch?v=xrNwJZwaylE)

Thomas Weible (FLEXOPTIX)

- **Why**: A pragmatic design approach for DWDM networks moving to 400GHz channels and coherent-only superchannels — directly relevant to DC/WAN interconnect planning, especially for operators who don't want ROADMs.
- **What**: Argues for moving from 50/100GHz DWDM grids to 400GHz channels (12×400GHz in C-band vs 96×50GHz), leveraging coherent detection's "blindness" to non-own wavelengths to build filterless or simplified-filter topologies. Shows how to use cheap PLC 1×4/4×1 splitters and regular 50GHz DWDM MUX/DeMUX to combine/split subbands, enabling colorless architecture without ROADMs.
- **How**: Coherent receivers use phase- and polarization-diversity intradyne detection, making them robust to adjacent-channel interference. By running a 400GHz subband through standard 50GHz MUX/DeMUX and using PLC splitters, you get flexible bandwidth reassignment without active ROADM infrastructure. 800G Coherent ZR+ in OSFP form factor is available today for this approach.
- **Where applicable**: Medium-scale DCI operators, regional DWDM networks. Requires coherent transceivers (400G-ZR+ class or above). The 400GHz filter approach trades spectral efficiency for flexibility and simplicity — best for networks that don't need maximum fiber capacity but want to avoid ROADM capex. FLEXOPTIX-branded but content is physics/standards-based.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Abstract](https://pretalx.com/denog17/talk/NRBPX9/) · [Slides](https://pretalx.com/media/denog17/submissions/NRBPX9/resources/Flexoptix_-_Unders_DF4TtuC.pdf) · [Recording](https://www.youtube.com/watch?v=Gbrwnefa5rA)

Dr. Gerhard Stein (FLEXOPTIX Research)

- **Why**: Power consumption of optics is becoming a first-order constraint in DC operations. This talk provides real measured data on transceiver power behavior using VDM (Versatile Diagnostics Monitoring) — directly relevant to the PM's optics and DC efficiency interests.
- **What**: An empirical study of transceiver power efficiency using CMIS VDM metrics (TEC current, laser temperature, optical power) across multiple transceiver types (100G QSFP28, 400G QSFP-DD ZR, 800G QSFP-DD) and switch platforms (Cisco Nexus 93600CD-GX, C9500, Juniper QFX5120). Key finding: laser and TEC power draw is negligible — the real energy consumers are the MCU/DSP. Shutting a port forces low-power mode with 7–20× less energy.
- **How**: VDM (from CMIS spec) exposes per-transceiver laser temperature, TEC current, and optical power via memory pages 20h–2Fh. Software prototypes collect and visualize this data in Watts. Experiments include frozen transceivers (ice cubes!) to isolate TEC behavior — finding ~200mW average increase per 20°C temperature difference. Switch-level power measurement complements module-level VDM data.
- **Where applicable**: Any operator deploying 100G+ optics who wants to measure and optimize per-port power. VDM support is spotty across switch platforms (Juniper QFX5120 and Cisco C9500 don't support it; Nexus 93600CD-GX does). The measurement technique is general; the specific "TEC/laser is negligible" finding is hardware-class-specific.

### Sorry we messed up

**Links:** [Abstract](https://pretalx.com/denog17/talk/KQ9JWA/) · [Slides](https://pretalx.com/media/denog17/submissions/KQ9JWA/resources/DENOG17-lowres-com_ct1oD1K.pdf) · [Recording](https://www.youtube.com/watch?v=zCqJDD7_aic)

Stefan Funke

- **Why**: A concrete postmortem of a global route leak caused by an Arista RCF (Routing Control Functions) bug — exactly the kind of hard-won failure story that transfers across organizations. The PM's BGP and network operations interests make this directly relevant.
- **What**: The story of how renaming Arista RCF functions (to encode IP version, peer IP, and session type in function names) triggered a global route leak via Arista BUG 1060542. During RCF recompilation, BGP peers shared an "undefined" RCF function state; update-group merging caused two low-scale peers to reconcile with a high-scale peer's advertised state before the withdraw-all-routes state was processed — leaking all prefixes to those peers and causing session flaps. Fixed in EOS 4.31+ maintenance releases.
- **How**: The root cause is a race condition between the RCF agent compiling new function names and the BGP agent using those names for filtering. Workaround: duplicate the RCF function or map the new function to the old one, commit, wait for compilation, then update BGP config — or shut peers before renaming associated RCF functions. The talk covers the full deployment pipeline (Ansible-generated config, session-based commits, checkpoint with commit timer).
- **Where applicable**: Arista EOS operators using RCF for BGP route filtering. The broader lesson — automated config changes to filtering logic can have vendor-bug landmines — applies to any operator using programmable route-policy frameworks on any vendor. Org-specific to the speaker's network (34 PoPs, ~70 devices) but the failure mode is general.

### EVPN for the rest of us – what happens when software people try to use EVPN

**Links:** [Abstract](https://pretalx.com/denog17/talk/BWHD38/) · [Recording](https://www.youtube.com/watch?v=prhgpr7hcz4)

Molly Miller (Flying Circus Internet Operations)

- **Why**: A first-hand account of migrating from flat L2 to EVPN-VXLAN terminated directly on Linux hypervisors — a design choice directly relevant to the PM's cloud-native + physical DC intersection. Zero-downtime migration execution and honest pain points from a production deployment.
- **What**: A software-centric organization designed and deployed EVPN-VXLAN on Linux hypervisors over ~9 months, culminating in a week-long zero-downtime production migration. Covers debugging tales, technical decisions, unexpected surprises, and remaining pain points a year later. (from abstract and page only — no slides/PDF available)
- **How**: EVPN-VXLAN terminated directly on Linux hypervisors (rather than TOR switches), which implies FRR/Linux-based VTEPs and control plane rather than traditional NOS-based EVPN. The talk promises details on the peculiar technical decisions and ongoing operational pain.
- **Where applicable**: Small-to-mid DC operators with strong Linux/software expertise who want to modernize from flat L2 without a traditional switch-centric EVPN fabric. The "EVPN on Linux hosts" approach is broadly adoptable but requires software networking depth. Flying Circus is a German ISP/hosting provider — the pattern applies to similar-scale operators.

### EVPN Flex Cross Connect - L2 P2P VPNs can be agile as well!

**Links:** [Abstract](https://pretalx.com/denog17/talk/FNVVFQ/) · [Slides](https://pretalx.com/media/denog17/submissions/FNVVFQ/resources/DENOG17_-_Tobias_H_CTPBKn6.pdf) · [Recording](https://www.youtube.com/watch?v=r9ngEfuehck)

Tobias Heister (Plusnet)

- **Why**: RFC 9744 (EVPN Flexible Cross-Connect) is a new and important extension for L2 point-to-point service scaling in aggregation networks — directly relevant to the PM's EVPN and fabric interests.
- **What**: A practical explanation of how EVPN VPWS Flexible Cross-Connect (FXC, RFC 9744, March 2025) solves the PW scaling problem in aggregation networks where many ports/VLANs need to map to a single tunnel. Demonstrated with real deployment numbers: Plusnet's scenario (3 target categories, 12 AGGs per region, 24 ports per AGG) shows a 95% reduction in PW count (from 288 down to 3 per AGG). PoC-tested on Juniper and Arista with interop working. Deployed in production at Plusnet.
- **How**: FXC normalizes VLAN IDs across ports and maps multiple normalized VIDs to a single PW/service tunnel. Two modes: Default FXC (one route regardless of how many port/AC/VID combinations attach) vs VLAN-Signaled FXC (one route per normalized VID per instance, enabling cross-checks). This reduces both EVPN service labels and BGP signaling volume.
- **Where applicable**: Service providers and operators with large aggregation networks running L2 services (backhauling to BNGs or service routers). Requires vendor support for RFC 9744 (Juniper and Arista confirmed). The VLAN normalization part depends heavily on vendor L2 feature flexibility — Arista's Flex-Encap and "unmatched" features called out as particularly well-suited.

### Going Large: Extended Route Targets or Extended Confusion?

**Links:** [Abstract](https://pretalx.com/denog17/talk/JVGJ8S/) · [Slides](https://pretalx.com/media/denog17/submissions/JVGJ8S/resources/DENOG_Extended_Rou_arhUVKT.pdf) · [Recording](https://www.youtube.com/watch?v=Usbq3PPxraw)

Robin Christ

- **Why**: A concrete protocol design proposal addressing a real gap in EVPN-VXLAN route target encoding — relevant to the PM's BGP/EVPN protocol internals interest. Signals a potential IETF work item.
- **What**: Identifies that 32-bit ASN + 24-bit VNI doesn't fit into the 48-bit payload of standard Route Targets (based on BGP Extended Communities). Proposes "Extended Route Targets" based on BGP Large Communities (96 bits total): reserve ASN 0xFFFFFFFF for IANA-managed Large Communities, add an 8-bit type field, leaving 56 bits — a perfect fit for 32-bit AS + 24-bit VNI.
- **How**: BGP Large Communities (RFC 8092) are extended from "AS-owned" semantics to include IANA-managed types. The proposal moves ASN 0xFFFFFFFF from "NOT RECOMMENDED" to "reserved for IANA-managed BGP Large Communities" with an 8-bit type field. Currently, vendors handle the overflow poorly: Cumulus doesn't auto-generate RTs, Juniper truncates to 2 least-significant ASN bytes.
- **Where applicable**: EVPN-VXLAN fabric designers using eBGP-only designs with 4-byte ASNs. The proposal is a discussion-starter, not yet an IETF draft. Broadly relevant to anyone who's hit the RT encoding ceiling in large-scale EVPN fabrics.

### 400G ZR+ BiDi does not exist, it can't hurt you. Or can it?

**Links:** [Abstract](https://pretalx.com/denog17/talk/KLXJS8/) · [Recording](https://www.youtube.com/watch?v=eqvhn0yXT9A)

Nicola von Thadden (PFALZKOM), Arjan Koopen (i3D.net / Stichting EventInfra)

- **Why**: A creative, out-of-spec experiment building a 400G link over a single fiber pair using ZR+ optics — relevant to the PM's optics and DC interconnect interests as a proof of what's technically possible outside standards.
- **What**: For the WHY2025 hacker summer camp in the Netherlands, the speakers built a 400G link over a single fiber. Since 400G BiDi doesn't exist as a standard product, they built something out-of-spec using ZR+ coherent optics. (from abstract and page only — no slides available)
- **How**: Not specified in the abstract — presumably using two wavelengths (one per direction) with coherent ZR+ modules on a single fiber pair, a non-standard but functional configuration. The title's "Or can it?" suggests they'll discuss whether this out-of-spec approach caused problems.
- **Where applicable**: Limited direct applicability — this is a proof-of-concept in a temporary event network. But it demonstrates what coherent optics can tolerate outside their specified operating envelope, useful knowledge for DCI planning when fiber count is constrained. Event/non-profit network context.

### Th3 Flock of Bird s

**Links:** [Abstract](https://pretalx.com/denog17/talk/XRVTP3/) · [Slides](https://pretalx.com/media/denog17/submissions/XRVTP3/resources/denog-17-slides_3affe3S.pdf) · [Recording](https://www.youtube.com/watch?v=dPsfWEahn_0)

Marcel Fest

- **Why**: BIRD 3.x is a major release of the most widely-used open-source BGP daemon — directly relevant to the PM's BGP internals interest. The talk includes benchmark numbers comparing BIRD v1.6.8, v2.17.2, and v3.1.4.
- **What**: An overview of BIRD's evolution and the v3.x changes: multithreaded execution, decoupled exports from imports, unified route attribute names, separate reload command for filters and protocols. Includes convergence benchmarks (using BNGBlaster as traffic generator in a testbed): v1.6.8 (C1: 7s, C2: 6s, C3: 3s), v2.17.2 (C1: 5s, C2: 2s, C3: 4s), v3.1.4 (C1: 4s, C2: 2s, C3: 7s — suggesting a regression in C3). (from slides)
- **How**: BIRD v3's multithreading and decoupled import/export paths are the main architectural changes. The benchmark methodology uses RTBrick's BNGBlaster project to generate BGP route feeds and measure convergence across three scenarios. The testbed is published on GitHub.
- **Where applicable**: Any operator running BIRD as a route server, IXP fabric, or automation target. v3.x improvements matter most for high-scale route servers with many peers and large tables. The C3 regression suggests caution before upgrading to v3.1.4 for certain workload profiles.

### The return of EGP or the curious case of the BGP Origin attribute

**Links:** [Abstract](https://pretalx.com/denog17/talk/ASAQKE/) · [Slides](https://pretalx.com/media/denog17/submissions/ASAQKE/resources/e-wt-20250807-RIPE_kmDkegi.pdf) · [Recording](https://www.youtube.com/watch?v=lbN6HheQFBw)

Wolfgang Tremmel (DE-CIX Academy)

- **Why**: A fascinating BGP protocol internals investigation — who is setting the Origin attribute to "e" (EGP) in the global routing table, and why. Includes the discovery that Tier1 providers are rewriting Origin to win best-path selection. Directly relevant to the PM's BGP/datapath internals interest.
- **What**: While preparing BGP training slides, Tremmel found 868 prefixes with Origin "e" (EGP) — a value that should theoretically never appear since EGP is dead. Investigation shows 118 ASes (IPv4) and 19 ASes (IPv6) originating EGP-tagged prefixes, with Google (AS396982: 348 IPv4 prefixes, AS394089: 83) as the largest contributor. The key insight: Tier1 providers are rewriting Origin-Type to "IGP" to win traffic in multi-transit scenarios where LocalPref and AS-path length tie.
- **How**: BGP best-path selection step 4 prefers IGP over EGP over Incomplete origin. If a customer sets equal LocalPref for multiple transits and receives same-length AS paths, the transit that rewrites Origin to "IGP" gets more traffic. No BGP implementation can turn off Origin evaluation. Countermeasure: rewrite Origin-Type for all incoming prefixes yourself (but consult BGP customers first).
- **Where applicable**: Any network operator with multiple transit providers and no BGP customers. The finding about Google AS396982/394089 originating EGP-tagged prefixes is unusual and unexplained. This is a global routing-table observation (from DE-CIX route collectors), applicable to any operator doing BGP traffic engineering with multiple upstreams.

### IPv6 multihoming without BGP, quo vadis?

**Links:** [Abstract](https://pretalx.com/denog17/talk/QNDD3G/) · [Slides](https://pretalx.com/media/denog17/submissions/QNDD3G/resources/slides-denog17-ipv_0gJks2a.pdf) · [Recording](https://www.youtube.com/watch?v=aLwVM0TT3os)

David 'equinox' Lamparter (NetDEF / FRRouting)

- **Why**: A deep technical exploration of IPv6 multihoming using source-specific routing (SADR) instead of BGP — relevant to the PM's routing protocol internals and Linux networking interests. Written by a core FRRouting maintainer.
- **What**: A systematic walkthrough of how to achieve multihomed IPv6 connectivity without PA assignment and BGP, using: DHCPv6-PD for prefix distribution (RFC 8415 §6.3), RFC 6724 rule 5.5 for host source address selection, RFC 8028 / dst-src-routing for source-specific routes on hosts, multiple link-local addresses on routers (draft-link-6man-gulla) to differentiate which uplink advertised which prefix, and MP-QUIC (draft-ietf-quic-multipath) for connection recovery. The talk is brutally honest that "the good shit isn't quite ready yet."
- **How**: Hosts do a route lookup with `::` as source, prefer addresses advertised by the chosen gateway (identified by router link-local address), then look up the route again with the chosen source. Linux `ip route add ::/0 from <prefix>` syntax installs source-specific routes in a single table (not policy routing). Multiple LL addresses per router (one per uplink prefix) make all topologies look the same to the host. Remaining gaps: PD snooping relays, multi-IA_PD handling, and preference/de-prefer mechanisms for backup uplinks.
- **Where applicable**: End-sites too small for PA+BGP but needing multihoming. Linux hosts have the best (and worst) support. FRRouting/OpenWRT have partial implementations. Commercial CPE largely doesn't ship these features. The IETF homenet WG attempted this 2015–2018 and "went really poorly" — this talk represents the current best-thinking on a genuinely hard problem.

## Adjacent

### Fiber Testing in Data Centers – Bringing Theory and Practice Workshop

**Links:** [Abstract](https://pretalx.com/denog17/talk/UVQNPF/) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/UVQNPF/resources/High_Speed-Portfol_5MAWaFp.pdf) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/UVQNPF/resources/DENOG_Workshop_EXF_PPLOJbn.pdf)

Svetoslav Nikolov, Jürgen Rummelsberger (EXFO), Kimberley Rotolo, Markus Eilers

- **Why**: As data rates increase (400G/800G/1.6T), fiber plant testing and validation become critical. The workshop also introduces hollow-core fiber (HCF) measurement techniques — an emerging technology the PM should be tracking.
- **What**: Hands-on training in modern DC fiber testing methodologies: insertion loss/return loss measurement, transceiver validation (proactive and reactive), high-speed breakout cable testing, and DCO (coherent) transceiver BERT. Introduces HCF measurement challenges. EXFO test equipment is used (vendor-adjacent but educational in nature).
- **How**: Covers verification of link stability (Pre-FEC BER monitoring), host-to-module interoperability testing (CMIS), and 400G/800G Ethernet test suites. HCF testing is introduced as a new measurement paradigm for ultra-low-latency applications.
- **Where applicable**: DC operators deploying 400G+ where fiber plant quality directly impacts link margin. HCF content is forward-looking — signals where the industry is heading for latency-critical DCI. Vendor (EXFO) workshop but the testing principles are standards-based.

### The basics of maintaining fiber optic connections

**Links:** [Abstract](https://pretalx.com/denog17/talk/ST9LKU/) · [Slides](https://pretalx.com/media/denog17/submissions/ST9LKU/resources/Denog17workshop_11_IUdVttS.pdf)

Takaya Nakagawa, Yoshihisa Sakai, Miho Kudo (NTT Advanced Technology)

- **Why**: Connector end-face contamination is the leading cause of optical link degradation and soft failures — the Arista "Fun with Optics" talk at the same conference explicitly cites dust/contamination as the top RMA cause. This hands-on workshop covers the fundamentals the PM can apply directly.
- **What**: A structured workshop covering optical connector types (LC, SC, MPO and next-gen MMC, SN, MDC, CS), end-face geometry parameters (IEC 61755), the causes of poor optical performance (contamination, misalignment, gaps), hands-on cleaning procedures, inspection with microscope, and fiber polishing with handheld machines.
- **How**: Real measured data on contamination effects: a clean LC connection shows 52.6dB return loss / 0.05dB insertion loss, while dust contamination degrades to 22.7dB RL / 1.1dB IL. Hand oil contamination: 44.2dB RL / 0.10dB IL. A partially-inserted connector can cause multiple reflections with return light stronger than a clean air-gap reflection.
- **Where applicable**: Universally applicable to any operator touching optical fiber. The IEC grading standards and cleaning procedures are industry-standard. The hands-on polishing component is most relevant to operators who do their own fiber rework.

### Inventing the wheel - Network Orchestration at scale

**Links:** [Abstract](https://pretalx.com/denog17/talk/JECPAH/) · [Recording](https://www.youtube.com/watch?v=ZsjAQUmEPmE)

Tom Merlin Eichhorn (DE-CIX)

- **Why**: DE-CIX's ground-up rebuild of network orchestration for a global IXP — covers source-of-truth, event-driven architecture, and testing discipline that any network automation team can learn from.
- **What**: A from-first-principles orchestration stack for DE-CIX's global network, built on three pillars: a central source of truth for config management, an event-driven service orchestration architecture, and a scalable design for rapid global growth. Includes a "digital twin" (Shadow) that mirrors production for pre-deployment validation of new software iterations.
- **How**: Not specified in detail in the abstract — the talk promises architectural choices, design principles, decision-making frameworks, and testing approaches. The Shadow digital twin mirrors production to validate new software before deployment to real hardware. (from abstract only — no slides available)
- **Where applicable**: Applicable to any complex network automation project. DE-CIX-specific scale (global IXP) but the principles (SoT, event-driven orchestration, digital twin validation) are broadly transferable to DC and SP networks.

### Containerlab: A guide to building your own virtual datacenter and monitoring it

**Links:** [Abstract](https://pretalx.com/denog17/talk/FTHSAH/) · [Slides](https://pretalx.com/media/denog17/submissions/FTHSAH/resources/Containerlab_Preso_oInT61T.pdf)

Mathis Bramkamp, Gordon Gidófalvy (Nokia)

- **Why**: Containerlab has become the de-facto open-source network labbing tool. This workshop covers building EVPN-VXLAN topologies plus a full telemetry stack (gNMIc, Prometheus, Grafana) and a Kubernetes-based orchestration demo — relevant to the PM's cloud-native networking and testing interests.
- **What**: A hands-on workshop teaching containerlab topology creation, adding client traffic, setting up modern telemetry (gNMIc → Prometheus → Grafana streaming dashboard), and using Edgeshark for remote packet captures. Concludes with a Kubernetes-based network orchestrator managing the same topology. The slides cover containerlab's evolution: 300K installations, 140+ contributors, 35+ supported NOSes, 13 new NOSes in the last 12 months.
- **How**: Containerlab topology files (YAML) define nodes (containerized NOSes like cEOS, SR Linux, FRR; or VM-based via vrnetlab) and links. The API server (released May 2025) enables CI/CD pipeline integration for automated testing (deploy → validate → cleanup). Clabernetes distributes topologies across k8s clusters. NRX turns NetBox-documented networks into runnable containerlab labs.
- **Where applicable**: Any network team wanting reproducible, version-controlled lab environments. The Kubernetes orchestration section requires no prior k8s experience. Nokia-presented but containerlab is fully open-source and multi-vendor.

### "What can possibly go wrong?" Stories of peculiarities of modern server hardware

**Links:** [Abstract](https://pretalx.com/denog17/talk/VJJ9RC/) · [Slides](https://pretalx.com/media/denog17/submissions/VJJ9RC/resources/DENOG17_22What_ca_UOzA5i3.pdf) · [Recording](https://www.youtube.com/watch?v=3zFiCRMh70E)

Vladimir Smirnov (NVIDIA, personal hobby project)

- **Why**: A technical deep-dive into modern x86 server platform topology (NUMA, SNC, DDIO, PCIe lane mapping) and how to avoid catastrophic performance losses when building high-throughput network systems. Relevant to the PM's interest in high-performance networking hardware.
- **What**: A follow-up to the speaker's 1 Tbps/1 Gpps load generator talk, covering how PCIe slot placement, Intel Sub-NUMA Clustering, DDIO, and CPU core pinning can make a ~150 mpps difference in VPP performance. Includes a detailed analysis of AMD Epyc Zen5c CCD/IO-die topology and its fabric bandwidth implications.
- **How**: Breakage scenarios: VPP limited to 64 threads (mainline VPP_MAX_WORKERS); worst-case PCIe cross-connection (NICs in slots on opposite CPU dies) causing ~150 mpps loss due to DDIO/SDCI behavior across NUMA domains; re-pinning VPP workers to the correct socket recovers performance. On AMD: for pure traffic generation, CCD topology doesn't matter (fabric bandwidth 64GB/s read per CCD is sufficient) but the total machine capacity is ~1.4 Tbps.
- **Where applicable**: Anyone building high-performance Linux-based networking on modern Intel (Sapphire/Emerald Rapids) or AMD (Zen5) servers. The specific numbers are for VPP with ConnectX-7/BlueField-3 NICs, but the platform topology awareness is universally critical.

### Merging Service Provider Networks

**Links:** [Abstract](https://pretalx.com/denog17/talk/L7TDFF/) · [Slides](https://pretalx.com/media/denog17/submissions/L7TDFF/resources/denog17-merging-sp_tTpqc3X.pdf) · [Recording](https://www.youtube.com/watch?v=f7OdtmCtBhc)

Markus Jungbluth, Bastian Hoss (Xantaro)

- **Why**: German SP market consolidation makes network merging a recurring challenge. This talk covers the technical approaches (NNI, Inter-Provider options A/B/C, Seamless MPLS) and challenges (IGP merging, low-scale access devices) — relevant to the PM's broader network architecture interests.
- **What**: A technical walkthrough of IP/MPLS network integration post-acquisition: three approaches (NNIs, Inter-Provider eBGP per RFC 4364 Options A/B/C, Carrier-of-Carrier VPNs), why they're all "quick fixes" that leave networks administratively separate, and how Seamless MPLS (BGP-LU, IGP separation, route summarization) builds the real bridges. Covers low-scale access devices (~500-2k FIB) as the weakest link, and a novel ISIS LSDB simulation technique for pre-merger testing.
- **How**: BGP-LU distributes transport labels via BGP without requiring LDP/IGP, enabling low-scale devices to participate with a default route + filtered BGP-LU routes. The lab simulation technique exported ISIS LSPs from both networks, manipulated them to simulate a merged LSDB, and transmitted it to a DUT via a customized ISIS implementation — proving the DUT wouldn't fail post-merger.
- **Where applicable**: Service providers going through M&A. The Seamless MPLS toolbox and low-scale-device separation patterns apply to any large network with heterogeneous device capabilities. Xantaro-specific deployment experience but the techniques are standards-based.

### Uncovering Blackholes: Advanced Detection Techniques for Complex Networks

**Links:** [Abstract](https://pretalx.com/denog17/talk/GJNTXH/) · [Recording](https://www.youtube.com/watch?v=ubFSJZzWtM8)

Anton Elita

- **Why**: Blackholing events (traffic blackholes from routing failures) are among the most disruptive network incidents — this talk presents detection and correlation techniques relevant to network operations and monitoring.
- **What**: Methods for detecting blackholing events, identifying affected transit flows, and analyzing correlations to reduce response times. Aimed at accelerating root cause identification for events that typically require manual intervention and vendor advanced support.
- **How**: Not specified in the abstract — the talk promises multiple detection methods and correlation analysis. (from abstract only)
- **Where applicable**: Complex networks with multiple transit flows where blackholing events are hard to localize. General network operations relevance.

## Wildcard

### You can’t just model a train in Netbox: About Architecting and running modern IT Infrastructure in Trains

**Links:** [Abstract](https://pretalx.com/denog17/talk/K3HSNK/) · [Recording](https://www.youtube.com/watch?v=FLa0NYDc6TA)

Vanessa Gaube (DB Fernverkehr)

- **Why**: A genuinely novel operating environment — running "modern IT infrastructure" (passenger information, WiFi, increasingly full IT services) on a fleet of ICE high-speed trains. The constraints (no fixed racks, intermittent connectivity, hardware lifecycle in a moving vehicle) produce architectural lessons that challenge DC assumptions in productive ways.
- **What**: How IT infrastructure on ICE trains has evolved from embedded systems and WiFi to a broader "modern IT" stack including passenger information services. Covers hardware selection, lifecycle differences from DC, the network architecture, and why standard DC tools (NetBox) don't map cleanly to rolling stock.
- **How**: Not specified in the abstract. (from abstract only)
- **Where applicable**: Uniquely DB-specific in context, but the problem — modeling and operating infrastructure that doesn't fit DC patterns in standard tooling — is a thought-provoking challenge for any architect who assumes NetBox/DCIM metaphors are universal.

### Security.txt across the industry

**Links:** [Abstract](https://pretalx.com/denog17/talk/WKBJGE/) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/WKBJGE/resources/20251110_Sectxt_Sa_KOxqk21.pdf) · [Slides (PPTX)](https://pretalx.com/media/denog17/submissions/WKBJGE/resources/20251110_Sectxt_S_YeC31eD.pptx) · [Recording](https://www.youtube.com/watch?v=Xw8Rz-3K4cs)

Sascha Heinemann (EdgeOps)

- **Why**: A data-driven analysis of security.txt (RFC 9116) adoption across DENOG-attending organizations — reveals the actual state of vulnerability disclosure readiness in the German/European network industry. Signals a gap the PM should be aware of.
- **What**: An adoption survey of security.txt among organizations represented at DENOG17, broken down by industry segment. Key numbers from 239 organizations: overall adoption by segment — consulting/services 21%, carrier 17%, hosting/cloud 31%, education/research 40%, hardware 17%, datacenter/colo 25%, IXPs 43%, public authority 67%. Valid (correctly formatted) rates are much lower — 0–15% across segments. Notable adopters include Netflix, SAP, BelWü, Init7, Inter.link, KIT, and DE-CIX (www.de-cix.net has one, though with canonical URL quirks).
- **How**: The security.txt file is a simple, machine-readable standard published at `/.well-known/security.txt` with fields for contact, encryption key, expiration, and preferred languages. The analysis checked for presence, validity, and correct formatting (PGP-signed, canonical URLs, etc.).
- **Where applicable**: Any organization that operates public-facing infrastructure. The finding that only 43% of IXPs and 31% of hosting/cloud providers have security.txt (with much lower valid rates) is a direct call to action. Low-effort, high-value security hygiene.

### Slow network, fast money: How Deutsche Telekom breaks the internet

**Links:** [Abstract](https://pretalx.com/denog17/talk/8NGPVU/) · [Recording](https://www.youtube.com/watch?v=AAXwZ23YwEY)

Thomas Lohninger (Netzbremse project)

- **Why**: Not a technical talk but a data-driven policy/peering analysis documenting how Deutsche Telekom's interconnection practices cause systematic congestion — affecting QoE for millions of German users. Signals where regulatory pressure on interconnection is heading and why QoE-driven peering arguments matter.
- **What**: The Netzbremse project documents that DT refuses to expand peering capacity appropriately, causing artificial throttling — with users and content providers paying at both ends to avoid congestion. Result: degraded video streaming, gaming, and conferencing quality, especially in the evening. An alliance of consumer protection, civil society, and research is taking action against this practice under EU net neutrality law.
- **How**: Methodology not detailed in the abstract — presumably measurement-based (QoE correlation with interconnection capacity). (from abstract only)
- **Where applicable**: Relevant to any peering/interconnection strategist in Europe, particularly regarding the tension between net neutrality regulation and commercial interconnection practices. German/EU-specific regulatory context.</think><!--
conference: DENOG 17 (Essen)
type: operator
source_url: https://www.denog.de/de/meetings/denog17/agenda.html
generated: 2026-11-02
registry_key: denog-17
-->

## Core

### Ultra Ethernet: Addressing AI/HPC Interconnect Challenges Beyond the InfiniBand Monopoly

**Links:** [Abstract](https://pretalx.com/denog17/talk/W8W77A/) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEtherne_RJk4QyN.pdf) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEtherne_vMqLytv.pdf) · [Recording](https://www.youtube.com/watch?v=8XWOzSVJHHA)

Andreas Roeder (Nokia)

- **Why**: This is the clearest operator-level walkthrough of the published Ultra Ethernet (UE 1.0, June 2025) spec — the standard most likely to reshape RDMA/lossless fabric design over the next few years. For anyone whose remit covers lossless Ethernet, AI/HPC fabrics, or DC interconnect strategy, this is the session to attend.
- **What**: A structured technical introduction to the Ultra Ethernet Transport (UET) layer: how it compares to RoCEv2, what problems it solves (multipathing, relaxed ordering, rapid loss recovery, modern congestion control), and why the InfiniBand lock-in problem (switch/NIC/optics/toolchain/management all single-vendor) motivates an Ethernet-based alternative with a multi-vendor ecosystem at every layer.
- **How**: UET runs on IPv4/IPv6 and standard Ethernet (lossy operation is fine — no PFC required). The Packet Delivery Sublayer (PDS) supports four delivery modes (RUD/ROD/RUDI/UUD), selective ACK/NACK with compact SACK encoding (64 sequence numbers in 8 bytes vs TCP's 4 in 36), packet spraying instead of flow-based ECMP, per-packet memory semantics (each packet carries its own target memory address, enabling direct commit without a reorder buffer), and dual congestion control (NSCC reacting to trimmed packets/ECN/latency plus RCCC, a receiver-credit scheme aimed at incast). Ephemeral asymmetric connections replace TCP-style sessions.
- **Where applicable**: Broadly applicable to AI/HPC fabric planning in any operator or enterprise environment — the spec is vendor-neutral by design. The talk focuses on DC-internal technologies that will also influence metro/regional/WAN design. Nokia-employed speaker, but the content is grounded in the UEC specification, not a product pitch.

### Forwarding packets at scale - Building a Cloud Data Plane using eBPF/XDP

**Links:** [Abstract](https://pretalx.com/denog17/talk/VNLHD7/) · [Slides](https://pretalx.com/media/denog17/submissions/VNLHD7/resources/slides_tUew2WC.pdf) · [Recording](https://www.youtube.com/watch?v=3G_gL7nvwVE)

Maximilian Wilhelm, Marcus Wichelmann (Hetzner)

- **Why**: Hetzner replaced an Open vSwitch-based data plane connecting hundreds of thousands of cloud servers with a purpose-built eBPF/XDP stack (`hcnet`). This is a production, at-scale validation of eBPF as a cloud data plane — exactly the kind of datapath-internals work the PM cares about.
- **What**: A three-year journey resulting in `hcnet`: an XDP-based network stack handling public/private cloud networking (VXLAN encapsulation), stateful firewalls, DHCP, and packet-capture tooling, with a Go control plane. Running in Hetzner's internal cloud for two years; public beta pending full feature parity with the OVS stack.
- **How**: Each cloud node runs XDP programs at the NIC that implement ARP/NDP/ICMP responding, port security, stateful firewalls (rulesets validated, normalized, compiled into eBPF instruction sequences, then loaded as templated programs), VXLAN VTEPs, and a DHCP/metadata server. The stack self-heals where possible, exposes per-interface/per-member metrics, and provides diagnostic tooling (`hcnet describe ifaces`, `hcnet dataplane stats`, conntrack map inspection, XDP-redirect-based `hcnet capture` writing pcaps with BPF filters). Current pain points: NIC driver maturity (e.g., an ixgbe XDP-redirect bonding bug reported upstream) and lack of offloading support; kernel patches (tun XDP metadata) being upstreamed.
- **Where applicable**: Cloud/hosting providers and large Linux-based fabrics. Hetzner-scale and -specific in deployment, but the architectural patterns (XDP gateway per node, firewall-rule-to-eBPF compilation pipeline, Go control plane) are broadly adoptable for anyone with in-house eBPF expertise.

### Fun with Optics

**Links:** [Abstract](https://pretalx.com/denog17/talk/AXEKSR/) · [Slides](https://pretalx.com/media/denog17/submissions/AXEKSR/resources/2025-DENOG-Fun_wit_0buk8u3.pdf) · [Recording](https://www.youtube.com/watch?v=DVyIFddJ1p0)

Patrick Prangl (Arista Networks)

- **Why**: A concise, current state-of-the-industry view on the optics-to-1600G transition — covering 800GbE standardization, LPO/LRO/CPO, and ZR/ZR+ DCI evolution. Essential physical-layer DC context for anyone planning high-density switching and interconnect over the next 3–5 years.
- **What**: A survey covering merchant silicon roadmaps (51.2T shipping, 102.4T expected 2025, 204.8T in 2027), 800GbE standards status (IEEE 802.3ck/df, 800GBASE-ETC-R), the 50G→100G→200G SerDes transition, Linear-drive Pluggable Optics (LPO) as a 50%+ power-reduction alternative to DSP-based transceivers, and the ZR/ZR+ coherent DCI ecosystem from 100G-ZR to 1.6T.
- **How**: LPO removes the DSP from the module (typical 800G-DR8 at 7.5W vs 14–16W DSP-based), relying on clean <20dB die-to-die electrical channels — the same channel requirement as NPO and CPO, with packaging position being the only difference. At 200G-PAM4, LPO needs careful channel design (fly-over cables on switches). ZR/ZR+ coherent evolution extends from 400G-ZR (120km) through 800G-ZR/ZR+ (up to 1000+km) to 1.6T Coherent Lite, with spectrum widths growing from 75GHz to 300GHz.
- **Where applicable**: Any DC operator planning 800G/1600G port deployments, especially for AI clusters where power per port is a constraint. Arista-branded but the data draws on MSA specs, IEEE standards, and multi-vendor plug-fest results.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Abstract](https://pretalx.com/denog17/talk/8N7Q3A/) · [Slides](https://pretalx.com/media/denog17/submissions/8N7Q3A/resources/Flexoptix_-_Channe_Xqpo1a5.pdf) · [Recording](https://www.youtube.com/watch?v=xrNwJZwaylE)

Thomas Weible (FLEXOPTIX)

- **Why**: A pragmatic design approach for DCI/metro DWDM that trades narrow-grid spectral efficiency for flexibility and cost — directly relevant to DC/WAN interconnect planning for coherent-only, filterless topologies.
- **What**: An argument for moving from 50/100GHz DWDM grids to 400GHz channels (12×400GHz across the C-band vs 96×50GHz) as per-channel bandwidth grows to 800G and 1.6T. Coherent detection's "blindness" to anything but its own wavelength enables filterless topologies; 400GHz filters retain flexibility for legacy ≤10G signals while allowing easy bandwidth reassignment.
- **How**: Coherent receivers use phase- and polarization-diversity intradyne detection, tolerating adjacent-channel interference. The proposed architecture runs a 400GHz subband through regular 50GHz DWDM MUX/DeMUX and uses cheap PLC 1×4/4×1 splitters to combine TX/split RX, achieving colorless functionality without ROADMs. 800G Coherent ZR+ in OSFP form factor is available for this approach. Emphasis on thinking in THz/GHz frequency plans per span rather than nm/channel numbers.
- **Where applicable**: Medium-scale DCI and regional DWDM operators who want flexible bandwidth without ROADM capex. Requires coherent transceivers (400G-ZR+ class or above); trades spectral efficiency for flexibility. FLEXOPTIX-affiliated speaker, but the physics and standards grounding is general.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Abstract](https://pretalx.com/denog17/talk/NRBPX9/) · [Slides](https://pretalx.com/media/denog17/submissions/NRBPX9/resources/Flexoptix_-_Unders_DF4TtuC.pdf) · [Recording](https://www.youtube.com/watch?v=Gbrwnefa5rA)

Dr. Gerhard Stein (FLEXOPTIX Research)

- **Why**: Power consumption of optics is a first-order DC design constraint. This is one of the few talks with actual measured VDM data across multiple transceiver types and switch platforms — directly relevant to the PM's optics and power-efficiency interests.
- **What**: An empirical study of transceiver power behavior using Versatile Diagnostics Monitoring (VDM, the CMIS successor to DDM) metrics — particularly TEC current, laser temperature, and optical power. Key findings: laser and TEC power draw is negligible at any temperature; the real energy consumers are the MCU/DSP; and shutting a port forces low-power mode consuming 7–20× less energy.
- **How**: VDM exposes per-transceiver laser temperature, TEC current, and related telemetry via CMIS memory pages 20h–2Fh. The team built software prototypes to collect, evaluate, and visualize transceiver efficiency in Watts across DUTs including 100G QSFP28, 400G QSFP-DD Coherent ZR (120km), and 800G QSFP-DD modules, tested on Cisco Nexus 93600CD-GX, Cisco C9500, and Juniper QFX5120. An experiment with frozen transceivers showed ~200mW average increase per 20°C temperature differential. Notably, VDM support is spotty across platforms — Juniper QFX5120 and Cisco C9500 don't expose it; the Nexus does.
- **Where applicable**: Any operator deploying 100G+ optics who wants to measure per-port power in production. VDM availability depends on switch platform and CMIS version. FLEXOPTIX-affiliated but the methodology and data are vendor-agnostic in applicability.

### Sorry we messed up

**Links:** [Abstract](https://pretalx.com/denog17/talk/KQ9JWA/) · [Slides](https://pretalx.com/media/denog17/submissions/KQ9JWA/resources/DENOG17-lowres-com_ct1oD1K.pdf)

Stefan Funke

- **Why**: A concrete postmortem of a global route leak caused by a race condition in Arista's RCF (Routing Control Functions) agent — a failure mode (automated filter rename during live operation) that could happen on any programmable route-policy framework. The kind of hard-won failure story that transfers across organizations.
- **What**: How renaming RCF functions (to encode IP version, peer IP, and session type in function names) triggered a global route leak via Arista BUG 1060542. During RCF recompilation, BGP peers referenced undefined function names; update-group merging caused two low-scale peers to reconcile with a high-scale peer's advertised state — leaking all prefixes and causing session flaps via route-limit notifications. Affected a 34-PoP, ~70-device network across 15 countries.
- **How**: The root cause is a race between the RCF agent compiling new functions and the BGP agent using those names for filtering. Workaround: duplicate the RCF function or map the new one to the old, commit, wait for compilation, then update BGP config to use the new function — or shut peers before renaming. Fixed in EOS 4.31/4.32/4.33 maintenance releases and ≥4.34. The talk covers the full deployment pipeline: Ansible-generated config, session-based commits, checkpoints, commit timers.
- **Where applicable**: Arista EOS operators using RCF. The broader lesson — programmable filter renames can expose vendor-bug race conditions, and "test before deploy" doesn't catch what only manifests at scale — applies to any operator using automation to modify route policy in production.

### EVPN for the rest of us – what happens when software people try to use EVPN

**Links:** [Abstract](https://pretalx.com/denog17/talk/BWHD38/)

Molly Miller (Flying Circus Internet Operations)

- **Why**: A first-hand account of migrating from flat L2 to EVPN-VXLAN terminated directly on Linux hypervisors — zero customer downtime during a week-long production migration. Directly relevant to the PM's DC fabric and Linux networking interests.
- **What**: An ~9-month project (design started late 2023) to replace an aging flat L2 DC network with EVPN-VXLAN terminated on Linux hypervisors, culminating in an intensive week-long migration with zero downtime. The talk covers debugging tales from the lab, peculiar technical decisions, unexpected surprises, and ongoing pain points a year into operation. (from abstract only)
- **How**: Not detailed in the abstract; the key architectural decision is EVPN-VXLAN terminated directly on Linux hypervisors rather than on TOR switches — implying FRR/Linux-based VTEPs and control plane. Debugging and operational details are the substance of the talk.
- **Where applicable**: Small-to-mid DC operators with strong Linux/software expertise who want to modernize from flat L2 without a traditional switch-centric EVPN fabric. The Linux-hypervisor-terminated EVPN approach requires software networking depth but avoids dependence on switch-vendor EVPN implementations.

### EVPN Flex Cross Connect - L2 P2P VPNs can be agile as well!

**Links:** [Abstract](https://pretalx.com/denog17/talk/FNVVFQ/) · [Slides](https://pretalx.com/media/denog17/submissions/FNVVFQ/resources/DENOG17_-_Tobias_H_CTPBKn6.pdf)

Tobias Heister (Plusnet)

- **Why**: RFC 9744 (EVPN VPWS Flexible Cross-Connect, March 2025) is a fresh, immediately deployable answer to a real scaling problem: hundreds of per-port/per-VLAN pseudowires in aggregation networks collapsing into a handful of multiplexed service tunnels. Directly relevant to EVPN fabric and aggregation design.
- **What**: A practical explanation of how EVPN VPWS FXC (RFC 9744) reduces PW count in aggregation networks by ~95% (from 288 per region to 3 in Plusnet's example: 3 target categories, 12 AGGs per region, 24 ports per AGG). The mechanism: normalize VLANs across multiple physical interfaces and map them onto a single service tunnel, reducing both EVPN service labels and BGP signaling volume. Deployed in production at Plusnet; PoC-tested 2023/2024 on Juniper and Arista with interop working.
- **How**: Two modes: Default FXC (one route regardless of how many port/AC/VID combinations attach, no VID-to-instance cross-check) vs VLAN-Signaled FXC (one route per normalized VID per instance, enabling cross-checks). The critical step is VID normalization — the vendor/NOS must provide flexible L2 config options to translate port/VLAN combinations into normalized VIDs carried in the EVPN route. Arista Flex-Encap and "unmatched" features are called out as particularly well-suited.
- **Where applicable**: Service providers and operators with large L2 aggregation networks backhauling services toward BNGs or service routers. Requires vendor support for RFC 9744 (Juniper and Arista confirmed). The value depends heavily on the L2 normalization capabilities of your NOS.

### Th3 Flock of Bird s

**Links:** [Abstract](https://pretalx.com/denog17/talk/XRVTP3/) · [Slides](https://pretalx.com/media/denog17/submissions/XRVTP3/resources/denog-17-slides_3affe3S.pdf)

Marcel Fest

- **Why**: BIRD 3.x is a major architectural release (multithreaded, decoupled import/export) of the most widely-used open-source BGP daemon. This talk provides concrete convergence benchmark numbers comparing v1.6.8, v2.17.2, and v3.1.4 — directly relevant to BGP control plane evaluation.
- **What**: An overview of BIRD's evolution with performance benchmarks. v3.1.4 brings multithreaded execution, decoupled exports from imports, unified route attribute names, and separate reload for filters vs protocols. Benchmarks (using RTBrick's BNGBlaster in a published testbed) show convergence times: v1.6.8 (C1: 7s, C2: 6s, C3: 3s), v2.17.2 (C1: 5s, C2: 2s, C3: 4s), v3.1.4 (C1: 4s, C2: 2s, C3: 7s). The C3 regression for v3.1.4 (7s vs 3s in v1.6.8) is the notable outlier and a caution flag before upgrading.
- **How**: The benchmark uses BNGBlaster as a traffic generator feeding BGP sessions and measuring convergence across three scenarios; the testbed configuration is published on GitHub (rtbrick/BGP-CP-DP-Testing) for reproduction.
- **Where applicable**: Any operator running BIRD as a route server, IXP infrastructure component, or automation target. The v3 multithreading matters most for high-scale route servers with many peers and large tables. The C3 regression suggests scenario-specific testing before upgrading to v3.1.4.

### The return of EGP or the curious case of the BGP Origin attribute

**Links:** [Abstract](https://pretalx.com/denog17/talk/ASAQKE/) · [Slides](https://pretalx.com/media/denog17/submissions/ASAQKE/resources/e-wt-20250807-RIPE_kmDkegi.pdf)

Wolfgang Tremmel (DE-CIX Academy)

- **Why**: A BGP protocol-internals investigation with a genuinely surprising finding: Tier1 providers are rewriting Origin-Type to win traffic in multi-transit tie-breaks. This affects anyone with multiple upstreams and equal LocalPref — a subtle traffic-engineering dynamic that most operators don't know is happening.
- **What**: While preparing BGP training, Tremmel found 868 prefixes in the global routing table with Origin "e" (EGP) — a value that should never legitimately appear since EGP is dead. Investigation shows 118 ASes (IPv4) and 19 (IPv6) originating EGP-tagged prefixes, with AS396982 (Google) accounting for 348 IPv4 prefixes. The key insight: Origin-Type (best-path selection step 4, after LocalPref and AS-path length) is being weaponized by transit providers who rewrite it to "IGP" to attract more traffic when customers set equal LocalPref across multiple transits.
- **How**: When LocalPref and AS-path length tie between two transits, the one that rewrites Origin to "IGP" (preferred over "e" and "incomplete") wins the tie-break. No BGP implementation can turn off Origin evaluation. Countermeasure for networks with multiple transits and no BGP customers: rewrite Origin-Type uniformly for all incoming prefixes; for those with BGP customers, consult them first.
- **Where applicable**: Any network operator with multiple transit providers. The observation comes from DE-CIX's route collectors and a RIPE91 presentation by James Bensly (inter.link) — globally applicable to multi-homed networks. The Google EGP-tagged prefixes (AS396982, AS394089) remain unexplained.

### Going Large: Extended Route Targets or Extended Confusion?

**Links:** [Abstract](https://pretalx.com/denog17/talk/JVGJ8S/) · [Slides](https://pretalx.com/media/denog17/submissions/JVGJ8S/resources/DENOG_Extended_Rou_arhUVKT.pdf)

Robin Christ

- **Why**: A concrete protocol design proposal addressing a real gap in EVPN-VXLAN route target encoding that large eBGP-only fabrics hit. Signals a potential IETF work item — relevant to the PM's BGP/EVPN protocol internals interest.
- **What**: Identifies that a 32-bit ASN + 24-bit VNI (56 bits) doesn't fit into the 48-bit payload of standard Route Targets (based on BGP Extended Communities). Current vendor behavior is inconsistent: Cumulus doesn't auto-generate RTs, Juniper truncates to the 2 least-significant ASN bytes. Proposes "Extended Route Targets" based on BGP Large Communities (RFC 8092, 96-bit total): reserve ASN 0xFFFFFFFF for IANA-managed Large Communities, add an 8-bit type field, leaving exactly 56 bits — a perfect fit for 32-bit AS + 24-bit VNI.
- **How**: The proposal has two steps: (1) introduce IANA-managed BGP Large Communities by moving AS 0xFFFFFFFF from "not recommended" to "reserved for IANA managed" in an update to RFC 8092, and (2) define the Extended Route Target type using the IANA-managed Large Community space. This fits 32-bit ASN + 24-bit VNI exactly (56 bits ≤ 56 bits available after the 8-bit type field).
- **Where applicable**: EVPN-VXLAN fabric designers using eBGP-only designs with 4-byte ASNs — the situation where RT encoding ceiling is actually hit. The proposal is a discussion-starter, not yet an IETF draft; its value is in naming the problem precisely and offering a workable path forward.

### IPv6 multihoming without BGP, quo vadis?

**Links:** [Abstract](https://pretalx.com/denog17/talk/QNDD3G/) · [Slides](https://pretalx.com/media/denog17/submissions/QNDD3G/resources/slides-denog17-ipv_0gJks2a.pdf)

David 'equinox' Lamparter (NetDEF / FRRouting)

- **Why**: A deep technical exploration of source-specific routing (SADR/dst-src) as the "nice" IPv6 multihoming solution for sites too small for PA+BGP. Written by a core FRRouting maintainer with deep IETF involvement — relevant to the PM's routing internals and Linux networking interests.
- **What**: A systematic walkthrough of the deployable IPv6 multihoming path without BGP: DHCPv6-PD prefix distribution (RFC 8415 §6.3), host source address selection (RFC 6724 "rule 5.5", being upgraded to MUST in RFC 6724bis), source-specific routes on hosts (RFC 8028, draft-ietf-rtgwg-dst-src-routing), multiple link-local addresses per router to disambiguate which uplink advertised which prefix, and MP-QUIC (draft-ietf-quic-multipath) for connection recovery after failover. Honest assessment: "the good shit isn't quite ready yet."
- **How**: Hosts do a route lookup with `::` as source (step 1), prefer addresses advertised by the chosen gateway identified by link-local address (step 2), then re-lookup with the chosen source (step 3). Linux `ip route add ::/0 from <prefix>` installs source-specific routes in a single table (not policy routing with multiple tables). Multiple LL addresses per router (draft-link-6man-gulla) make all topologies look the same to the end host. Remaining gaps: hierarchical DHCPv6-PD across multiple routers (no open-source PD snooping relay), multi-IA_PD handling, and preference/de-prefer mechanisms for backup uplinks.
- **Where applicable**: End-sites too small for PA+BGP but needing genuine multihoming. Linux has both the best router support and the worst end-host behavior. OpenWRT has most features but they don't ship by default; commercial CPEs largely lack them. The IETF homenet WG attempted this 2015–2018 and failed (BABEL vs IS-IS routing protocol fight) — this talk represents current best thinking on a genuinely hard problem.

### 400G ZR+ BiDi does not exist, it can't hurt you. Or can it?

**Links:** [Abstract](https://pretalx.com/denog17/talk/KLXJS8/)

Nicola von Thadden (PFALZKOM), Arjan Koopen (i3D.net / Stichting EventInfra)

- **Why**: A creative, out-of-spec experiment: a 400G link over a single fiber using ZR+ coherent optics, since 400G BiDi doesn't exist as a product. Directly relevant to the PM's optics interests — demonstrates what coherent optics tolerate outside their specified operating envelope, useful when fiber count is constrained.
- **What**: For the WHY2025 hacker summer camp in the Netherlands, the speakers built a 400G link over a single fiber. Since 400G BiDi doesn't exist, they built something out-of-spec using ZR+ optics. A lightning talk. (from abstract and page only — no slides or detailed technical writeup available)
- **How**: Not detailed in the abstract — presumably two wavelengths (one per direction) with coherent ZR+ modules on a single fiber pair, a non-standard but functional configuration.
- **Where applicable**: Limited direct applicability — proof-of-concept in a temporary event network. The demonstrated envelope-pushing of coherent modules is useful knowledge for DCI planning where fiber count is constrained or when troubleshooting marginal coherent links.

## Adjacent

### Inventing the wheel - Network Orchestration at scale

**Links:** [Abstract](https://pretalx.com/denog17/talk/JECPAH/)

Tom Merlin Eichhorn (DE-CIX)

- **Why**: A from-first-principles rebuild of network orchestration for a global IXP — the design principles (source of truth, event-driven architecture, digital twin for pre-deployment validation) are transferable to any complex network automation project.
- **What**: DE-CIX's orchestration stack built on three pillars: a central source of truth for configuration management, an event-driven architecture for service orchestration, and a scalable design for rapid global growth. A "digital twin" (Shadow) mirrors production to validate and test new software iterations in parallel, minimizing risk before deployment to real hardware. The talk covers architectural choices, design principles, decision-making frameworks, testing rigor, and lessons learned.
- **How**: The Shadow stack mirrors the production environment so new orchestration software can be validated against a realistic copy before touching real hardware. Config management is tightly integrated with the source of truth; service orchestration is event-driven rather than batch/polling.
- **Where applicable**: Any complex network automation or orchestration project — the digital-twin validation pattern and event-driven orchestration principles are broadly transferable. DE-CIX-specific scale (global IXP) but the lessons are explicitly framed as generalizable.

### Containerlab: A guide to building your own virtual datacenter and monitoring it

**Links:** [Abstract](https://pretalx.com/denog17/talk/FTHSAH/) · [Slides](https://pretalx.com/media/denog17/submissions/FTHSAH/resources/Containerlab_Preso_oInT61T.pdf)

Mathis Bramkamp, Gordon Gidófalvy (Nokia)

- **Why**: Containerlab has become the de-facto open-source network labbing tool (300K installations, 140+ contributors, 35+ supported NOSes, 13 added in the last 12 months). The workshop goes beyond topology-building to telemetry (gNMIc/Prometheus/Grafana) and a Kubernetes-based orchestration demo — a full lab-to-automation pipeline.
- **What**: A hands-on workshop covering: (1) containerlab topology creation with recent 2025 additions, (2) traffic generation and observation including Edgeshark for remote packet captures and link impairment simulation, (3) a modern open-source telemetry stack (gNMIc → Prometheus → Grafana streaming dashboards), and (4) a Kubernetes-based network orchestrator managing the same topology. The slides also cover the new (May 2025) Containerlab API Server with RBAC, multitenancy, and CI/CD pipeline integration.
- **How**: Containerlab topology files (YAML) define nodes (containerized NOSes like SR Linux, cEOS, FRR; VM-based via vrnetlab) and links with automatic interface-name translation. The API server enables lab-as-a-service for CI/CD: deploy from a PR, run tests (config syntax, connectivity, route table), get results, cleanup. Clabernetes distributes topologies across k8s clusters. NRX turns NetBox-documented networks into runnable labs.
- **Where applicable**: Any network team wanting reproducible, version-controlled lab environments for design validation, automation testing, or training. Nokia-presented but containerlab is fully open-source and multi-vendor. The Kubernetes section requires no prior k8s experience.

### Fiber Testing in Data Centers – Bringing Theory and Practice Workshop

**Links:** [Abstract](https://pretalx.com/denog17/talk/UVQNPF/) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/UVQNPF/resources/High_Speed-Portfol_5MAWaFp.pdf) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/UVQNPF/resources/DENOG_Workshop_EXF_PPLOJbn.pdf)

Svetoslav Nikolov, Jürgen Rummelsberger (EXFO), Kimberley Rotolo, Markus Eilers

- **Why**: As speeds increase past 400G, fiber plant testing and transceiver validation become critical. The workshop also introduces measurement techniques for hollow-core fiber (HCF) — an emerging technology for ultra-low-latency DCI that the PM should be tracking as it matures.
- **What**: A theoretical and hands-on workshop covering: essential fiber testing principles (insertion loss, return loss), verification of link stability via Pre-FEC BER monitoring, host-to-module interoperability testing via CMIS, transceiver validation (proactive before install, reactive during troubleshooting), and high-speed breakout cable testing. Also introduces HCF measurement techniques — HCF is emerging for ultra-low latency and high-capacity applications, and the testing challenges differ from standard SMF.
- **How**: Testing methodologies use EXFO platforms (FTBx-88480 series and above, 800G HW-ready) for 400G/800G Ethernet, DCO BERT for 400ZR/OpenZR+ coherent modules, and CMIS testers for host-to-module interoperability. Transceiver validation distinguishes between proactive (pre-install) and reactive (troubleshooting) scenarios.
- **Where applicable**: DC operators deploying 400G+ where fiber plant quality directly impacts link margin and where transceiver validation catches defects before installation. HCF content is forward-looking for latency-critical DCI. EXFO vendor workshop but the testing principles are standards-based (IEEE, MSA, CMIS).

### The basics of maintaining fiber optic connections

**Links:** [Abstract](https://pretalx.com/denog17/talk/ST9LKU/) · [Slides](https://pretalx.com/media/denog17/submissions/ST9LKU/resources/Denog17workshop_11_IUdVttS.pdf)

Takaya Nakagawa, Yoshihisa Sakai, Miho Kudo (NTT Advanced Technology)

- **Why**: Connector end-face contamination is the leading cause of optical link degradation and RMAs (a point the Arista optics talk also makes). This hands-on workshop provides the fundamentals and measured data quantifying contamination impact — universally applicable to anyone operating optical plants.
- **What**: A workshop covering optical connector types (LC, SC, MPO, and next-generation MMC, SN-MT, MDC, CS), end-face geometry parameters per IEC 61755, causes of poor optical performance (contamination, misalignment, gaps), hands-on cleaning procedures with microscope inspection, and fiber polishing with handheld machines. Real measured data on contamination effects: clean LC connection (52.6dB RL / 0.05dB IL), hand oil (44.2dB RL / 0.10dB IL), dust (22.7dB RL / 1.1dB IL), partially-inserted connector causing multiple reflections (13.8dB RL with 0.14dB IL).
- **How**: Covers single-ferrule connectors (physical contact via spring-loaded ferrule alignment with sleeves) and multi-fiber MT ferrules (guide-pin alignment). Cleaning methods: reel cleaners (press end face perpendicularly against cloth and slide), stick cleaners (insert straight, press, rotate 4–5 times in one direction only), and pen-type for adapters. Polishing covers grades, machines, and precautions. Interferometer-based end-face geometry measurement ensures physical contact parameters (radius of curvature, apex offset, fiber height) meet IEC 61755-3-1.
- **Where applicable**: Universally applicable to any operator maintaining optical fiber plants. The IEC grading standards, cleaning procedures, and measured degradation numbers are industry-standard. The hands-on polishing component is most relevant to operators doing their own fiber rework.

### Merging Service Provider Networks

**Links:** [Abstract](https://pretalx.com/denog17/talk/L7TDFF/) · [Slides](https://pretalx.com/media/denog17/submissions/L7TDFF/resources/denog17-merging-sp_tTpqc3X.pdf)

Markus Jungbluth, Bastian Hoss (Xantaro)

- **Why**: German SP market consolidation makes network merging a recurring challenge. The talk covers three integration approaches (NNI, Inter-Provider RFC 4364 Options A/B/C, Carrier-of-Carrier VPNs), explains why they're all "quick fixes" leaving networks administratively separate, and shows how Seamless MPLS builds real bridges — plus a novel ISIS LSDB-simulation technique for pre-merger testing.
- **What**: A technical walkthrough of IP/MPLS network integration post-acquisition. Key challenges addressed: low-scale access devices (~500–2k FIB) becoming the weakest link when IGPs merge, route summarization conflicting with MPLS label distribution (which relies on exact-match /32 or /128), and harmonizing metric values/IGP settings. The lab technique: exported ISIS LSPs from both networks, manipulated them to simulate a merged LSDB, and transmitted it to a DUT via a customized ISIS software implementation — proving the DUT wouldn't fail post-merger without touching production.
- **How**: BGP-LU (BGP Labeled Unicast) distributes transport labels via BGP, allowing low-scale devices to participate with a default route + filtered BGP-LU routes instead of full IGP/LDP. This separates service and transport planes, enabling Seamless MPLS scaling to 100,000+ nodes. The toolbox: BGP-LU/BGP-CT/BGP-CAR for IGP-independent label distribution, LDP/RSVP-TE/SR for IGP-specific, and SR-TE for traffic engineering. Merging IGPs is recommended as an opportunity to implement Segment Routing (Flex Algo, TI-LFA, SR-TE).
- **Where applicable**: Service providers going through M&A or building multi-domain networks. The Seamless MPLS toolbox and low-scale-device separation patterns apply to any large network with heterogeneous device capabilities. Xantaro-specific deployment experience but the techniques are standards-based and broadly documented.

### "What can possibly go wrong?" Stories of peculiarities of modern server hardware

**Links:** [Abstract](https://pretalx.com/denog17/talk/VJJ9RC/) · [Slides](https://pretalx.com/media/denog17/submissions/VJJ9RC/resources/DENOG17_22What_ca_UOzA5i3.pdf)

Vladimir Smirnov (NVIDIA, personal project)

- **Why**: A follow-up to the speaker's 1 Tbps/1 Gpps load generator talk, covering how modern server platform topology (PCIe lane mapping, Sub-NUMA Clustering, DDIO, CCD/IO-die fabric) can silently cost ~150 mpps in VPP performance if misconfigured. Relevant to anyone building high-throughput Linux networking systems.
- **What**: Concrete breakage scenarios on Intel Emerald Rapids and AMD Epyc Zen5c: (1) VPP limited to 64 worker threads (mainline VPP_MAX_WORKERS, no configurable patch merged), (2) worst-case PCIe cross-connection (NICs in slots attached to opposite CPU dies) causing ~150 mpps loss due to DDIO/SDCI behavior across NUMA domains, (3) core pinning to the correct socket recovering performance. On AMD: Zen5c CCD topology doesn't matter for pure traffic generation (fabric bandwidth 64GB/s read per CCD is sufficient), but the whole machine caps at ~1.4 Tbps generating capacity.
- **How**: Diagnosis via lstopo topology visualization, Intel PCM memory counters, and VPP statistics. The talk shows how to verify PCIe-to-CPU-die mapping from motherboard/CPU vendor diagrams before assuming slot layout is benign.
- **Where applicable**: Anyone building high-performance Linux networking (VPP, DPDK, custom packet processing) on modern Intel Sapphire/Emerald Rapids or AMD Zen 4/5 servers. The VPP_MAX_WORKERS limit is a mainline-VPP-specific constraint. Home-lab hardware but the platform topology lessons are universal.

### 200 GbE network processing with 100 W - or "can I *make* a chip for that?"

**Links:** [Abstract](https://pretalx.com/denog17/talk/VEGBSU/) · [Slides](https://pretalx.com/media/denog17/submissions/VEGBSU/resources/network_offloading_Id8Nh2e.pdf)

Philipp Keydel (Synogate)

- **Why**: An accessible explanation of why hardware offload wins for network processing at scale, plus an introduction to Gatery — an open-source C++ hardware construction library that lowers the barrier to custom silicon/FPGA development. Relevant to the PM's interest in the hardware/software boundary of network processing.
- **What**: A talk covering: why chips beat CPUs for networking (determinism, energy efficiency, compute density, longevity), why the industry needs more chips (network evolution outpacing CPU improvements per Nielsen's Law), what can be achieved today (200 GbE stateful throughput at 240M new connections/s, 16B concurrent connections, 35W), and why making circuits is still hard (verbose tools, insufficient designers, 30-year-stagnant tooling). Introduces Gatery as an open-source (LGPL) C++ hardware construction library for rapid prototyping and iteration.
- **How**: Gatery provides a modern C++-based alternative to VHDL/Verilog for RTL design, enabling agile development with reuse of tested components, automation of boilerplate, and seamless integration into traditional toolchains. Target-hardware-agnostic. The talk covers the full flow: requirements → engineering → RTL design → testing/verification → synthesis → tape-out/FPGA.
- **Where applicable**: Teams evaluating hardware offload for TCP processing, cybersecurity, or traffic shaping. Also relevant to anyone curious about custom silicon or FPGA development with modern tooling. Vendor-agnostic (open-source framework); the specific 200G/35W figures are Synogate's product results.

## Wildcard

### Security.txt across the industry

**Links:** [Abstract](https://pretalx.com/denog17/talk/WKBJGE/) · [Slides (PDF)](https://pretalx.com/media/denog17/submissions/WKBJGE/resources/20251110_Sectxt_Sa_KOxqk21.pdf) · [Slides (PPTX)](https://pretalx.com/media/denog17/submissions/WKBJGE/resources/20251110_Sectxt_S_YeC31eD.pptx)

Sascha Heinemann (EdgeOps)

- **Why**: Not a deeply technical talk, but a data-driven survey of security.txt (RFC 9116) adoption across DENOG-attending organizations with genuinely useful findings — and a striking gap between "has security.txt" and "has a valid security.txt" that reveals how shallow security readiness is, even among network operators.
- **What**: An adoption analysis of 239 organizations across industry segments represented at DENOG17. Key findings: only 17–43% have security.txt depending on segment (carriers 17%, hosting/cloud 31%, education/research 40%, IXPs 43%, public authorities 67%); valid rates (correctly formatted, signed, canonical, with proper expiration) are far lower — 0–15%. Notable adopters include Netflix, SAP, BelWü, Init7, Inter.link, KIT, and DE-CIX (though with canonical URL quirks). The BSI's own security.txt expires in 2099.
- **How**: Analysis of `/.well-known/security.txt` presence, format validity, PGP signatures, expiration dates, and canonical URL correctness across the sampled organizations. Data as of Nov 6, 2025. An interactive checker was made available at edgeops.de/sectxt.
- **Where applicable**: Any organization operating public-facing infrastructure. The finding that even IXPs (43% adoption, 0% valid) and hosting providers (31% adoption, 5% valid) have poor readiness is a direct, low-effort call to action. Standards-based (RFC 9116), universally applicable.

### You can’t just model a train in Netbox: About Architecting and running modern IT Infrastructure in Trains

**Links:** [Abstract](https://pretalx.com/denog17/talk/K3HSNK/)

Vanessa Gaube (DB Fernverkehr)

- **Why**: A genuinely novel operating environment: running modern IT infrastructure on a fleet of ICE high-speed trains. The constraints (no racks in the traditional sense, intermittent connectivity, hardware lifecycle on a moving vehicle, NetBox not fitting the model) produce architectural lessons that productively challenge DC assumptions.
- **What**: An overview of IT infrastructure on ICE trains — evolving from embedded systems and passenger WiFi toward a broader modern IT stack including passenger information services. Covers challenges versus datacenter-built infrastructure: how to get proper internet on a train, what a network looks like in that context, hardware selection and lifecycle differences, whether racks exist, and why NetBox's model doesn't map cleanly to rolling stock.
- **How**: Not detailed in the abstract. (from abstract only)
- **Where applicable**: Uniquely DB-specific in context, but the meta-problem — modeling and operating infrastructure that doesn't fit DC patterns in standard tooling — challenges any architect who assumes NetBox/DCIM metaphors are universal. Interesting as a boundary case for infrastructure modeling and for edge-network design with highly variable connectivity.

### Slow network, fast money: How Deutsche Telekom breaks the internet

**Links:** [Abstract](https://pretalx.com/denog17/talk/8NGPVU/)

Thomas Lohninger (Netzbremse project)

- **Why**: Not a technical talk, but a data-driven analysis of how Deutsche Telekom's interconnection practices cause systematic congestion affecting millions of users — directly relevant to peering/interconnection strategy and the regulatory direction of net neutrality enforcement in the EU.
- **What**: The Netzbremse project documents that Telekom refuses to expand peering capacity appropriately, causing artificial throttling — with users and content providers paying at both ends of the line to avoid congestion. Result: massive quality losses in video streaming, gaming, and online conferencing, especially in the evening. An alliance of consumer protection, civil society, and research is taking action under EU net neutrality law against this as a violation of the open internet principle.
- **How**: Methodology not detailed in the abstract — presumably measurement-based QoE correlation with interconnection capacity. (from abstract only)
- **Where applicable**: Relevant to any peering/interconnection strategist in Europe, particularly regarding the tension between net neutrality regulation and commercial interconnection practices. German/EU-specific regulatory context but the interconnection congestion dynamics are universal. Signals where regulatory pressure on interconnection may be heading.

## Themes

- **AI/HPC is the primary driver reshaping DC fabric requirements**: Ultra Ethernet's UET spec (published June 2025), 800G/1600G optics transitions, LPO power reduction, and per-packet memory semantics all reflect AI workload demands — lossless operation without PFC, packet spraying, and incast-aware congestion control.

- **800G→1.6T transition is in full swing**: Multiple talks (Fun with Optics, Channelmania, transceiver VDM) address the SerDes transition to 200G lanes, LPO/CPO/NPO consolidation, coherent ZR/ZR+ DCI evolution to 800G and 1.6T, and DWDM grid widening to 400GHz — operators are planning for this now, not in 3 years.

- **eBPF/XDP is production-ready for cloud data planes**: Hetzner's `hcnet` demonstrates a fully-XDP cloud networking stack (VXLAN, stateful firewall, DHCP) running in production for two years — validating eBPF beyond observability into core forwarding, though driver maturity and offloading remain gaps.

- **EVPN is consolidating as the universal L2/L3 service framework**: RFC 9744 (Flex Cross-Connect), Extended Route Targets for 4-byte ASN fabrics, and Linux-hypervisor-terminated EVPN all push EVPN further into aggregation, DC, and even small-operator territory previously served by VPLS or flat L2.

- **Postmortems and failure stories remain the highest-signal content**: The Arista RCF route leak talk, the BIRD v3 benchmark regression, the server hardware peculiarities talk, and the BGP Origin-Type manipulation finding all represent hard-won operational lessons that transfer directly across organizations — the operator community values these above vendor roadmaps.

- **Power efficiency is becoming a first-class optics concern**: Transceiver power measurement via VDM (TEC current, laser temperature), LPO eliminating DSP power, and the systematic quantification of per-port Watt costs signal that optics power budget is now an explicit design constraint rather than an afterthought.
