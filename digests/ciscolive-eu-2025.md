<!--
conference: Cisco Live Europe 2025 (Amsterdam)
type: vendor
source_url: https://www.ciscolive.com/on-demand/on-demand-library.html?search.event=1737762187215001jsy4
generated: 2026-11-06
registry_key: ciscolive-eu-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Cisco Live Europe 2025 (Amsterdam)

*Enrichment note: the Cisco Live on-demand library pages are login-gated, JavaScript-rendered views; fetches returned only the site shell, so every write-up below is based on the program abstract only.*

## Core

### Advanced Innovations in SRv6 uSID and IP Measurements - BRKSPG-3198

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161418290001NGBp)

Speakers: Alexey Gorovoy (NEBIUS), Pablo Camarillo (Cisco Systems, Inc.)

- **Why**: One of the few sessions with a real end-user architecture story (Nebius) plus hard performance numbers for a next-generation dataplane that collapses VPN, TE, and NFV into a single stateless IPv6 dataplane — directly relevant to DC/WAN interconnect and dataplane-internals interests.
- **What**: A status report on SRv6 uSID at claimed scale (85,000+ routers deployed across operators), a Nebius case study of a Frontend DC design that integrates VPN, TE, and NFV from front-end to peering on a single SRv6 uSID dataplane, and new IP Measurements (IPM) results: 14 million probes per second on Silicon One hardware for one-way loss, latency, and liveness. Also covers Path Tracing for per-hop visibility. (from abstract only)
- **How**: uSID encodes multiple micro-segments inside a single IPv6 address, letting one end-to-end header express VPN membership, traffic-engineering paths, fast reroute, and service steering without MPLS-style shim layers. IPM embeds measurement instructions in the data plane so probes follow the same path as production traffic, giving SLA measurements that correlate with actual routing.
- **Where applicable**: uSID requires SRv6-capable silicon and IOS-XR/Silicon One platforms; the IPM figure is tied to Silicon One hardware specifically. The Nebius frontend-DC design is operator-specific but the pattern (stateless end-to-end dataplane across DC-to-peering domains) is broadly transferable. Treat vendor-scale claims (85k routers) with the usual skepticism until verified.

### Ethernet Based Fabric for AI Cluster - Powered by Silicon One & SONiC, an Ultra High Performance, Scalable & Non-Blocking Ethernet Fabric - BRKCOC-3005

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279978001dSBw)

Speakers: Lieven Colman (Cisco), John Banner (Cisco)

- **Why**: AI-cluster fabric build-out is the hottest physical-DC topic right now, and this is a practitioner's account of actually standing up non-blocking Ethernet fabrics for 256- and 512-GPU training clusters — scale, config choices, and failure discussion, not just a roadmap.
- **What**: A Cisco-on-Cisco internal deployment story covering the technology stack (Silicon One switching running SONiC, Nexus-based networks), the key configuration decisions, the challenges hit, and lessons learned while building production AI-cluster fabrics. (from abstract only)
- **How**: Builds non-blocking (oversubscription-free) Ethernet fabrics for GPU compute using commodity-OS (SONiC) on Silicon One silicon, integrated with Nexus-based underlay/management networks; the abstract promises concrete design trade-offs rather than architecture diagrams alone.
- **Where applicable**: Cisco-specific silicon and NOS stack, but the design questions (buffering, congestion management, non-blocking topology at 256–512 GPU scale) apply to any Ethernet-for-AI effort. Watch for whether they discuss RoCEv2/PFC vs. alternative lossless approaches — the abstract doesn't say which they chose.

### IP/Ethernet Storage Networking for AI Infrastructure - BRKDCN-2945

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294941001dzv0)

Speakers: Paresh Gupta (Cisco)

- **Why**: Lossless Ethernet for RDMA is squarely in the PM's core, and this is one of the few sessions that grounds PFC/ECN in a concrete workload: storage I/O for AI training and inference, where a single loss can stall an entire job.
- **What**: A design-and-operations guide for storage networking under AI workloads: lossless Ethernet foundations (Priority-based Flow Control) for RoCEv2, the interaction of PFC and ECN for RoCE congestion management (RCM), QoS effects on storage traffic, and fabric designs using 100G/400G/800G Nexus switches for RDMA, iSCSI, and NVMe-over-TCP, with NVMe-oF best practices. (from abstract only)
- **How**: Explains how to engineer a lossless Ethernet class of service for RoCEv2 (PFC headroom tuning, ECN thresholds, RCM), and how to decide between dedicated and shared storage networks depending on QoS contention, plus operational tooling via Nexus Dashboard.
- **Where applicable**: Cisco Nexus switch families and UCS server connectivity; the PFC/ECN/RCM mechanics are general to any RoCEv2-over-Ethernet deployment. Org-specific parts are the Cisco product recommendations; the lossless-fabric engineering is broadly applicable.

### VXLAN EVPN: A Deep Dive into Packet Forwarding - BRKDCN-3966

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098298175001dD9t)

Speakers: Lukas Krattiger (Cisco)

- **Why**: Pure dataplane-internals material — exactly the kind of "what actually happens in the silicon" session the PM values. Krattiger's deep dives are typically among the most technically dense Cisco Live breakouts.
- **What**: A packet-by-packet walkthrough of VXLAN EVPN forwarding: how bridging and routing work, how multi-destination (BUM) traffic is handled, and what happens from ingress VTEP through the underlay to egress VTEP and beyond. (from abstract only)
- **How**: Follows a single packet's life through VTEP encapsulation, ARP/suppression behavior, routing between VNIs, and multicast/ingress-replication handling of broadcast traffic — the mechanics that determine real-world behavior such as asymmetric vs. symmetric IRB and head-end replication scaling.
- **Where applicable**: NX-OS standalone VXLAN EVPN (the session is a companion to the multi-site talk below). The forwarding concepts are generic to any VXLAN EVPN fabric, though implementation details (e.g., specific replication modes) are Cisco-specific.

### VXLAN BGP EVPN Multi-Site - BRKDCN-2913

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292962001dLLT)

Speakers: Lukas Krattiger (Cisco)

- **Why**: DC-to-DC interconnect is core to the PM's remit; this is the canonical session on how Cisco thinks separate EVPN fabrics should be stitched together, and where the approach is heading.
- **What**: The evolution of Cisco's approaches for interconnecting separate VXLAN BGP EVPN fabrics — from multi-pod to multi-fabric to the current VXLAN multi-site design, positioned as the recommended interconnect for discrete EVPN islands. (from abstract only)
- **How**: Uses the VXLAN data plane with EVPN as control plane across sites — typically via a DCI overlay where EVPN routes leak between sites with scoped route targets and designated-forwarder election extended across sites, aiming for L2 extension plus integrated L3 without full-mesh state.
- **Where applicable**: Explicitly NX-OS standalone VXLAN EVPN only — it excludes ACI's multi-pod/multi-site solutions, so multi-vendor or ACI shops get design philosophy rather than recipes. The general multi-site EVPN patterns are broadly applicable.

### Advancements and Applications of Coherent Pluggable Technology in High Bandwidth Transport Networks - BRKOPT-2556

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098359983001dTG9)

Speakers: Anuj Malik (Cisco)

- **Why**: Coherent pluggables are the driving force behind the IP/optical convergence reshaping DC-WAN interconnect economics (400G/800G ZR/ZR+ directly in router ports) — central to physical DC networking interests.
- **What**: A technical treatment of coherent pluggable transceivers: the key components (tunable lasers, high-speed ADC/DACs, DSP algorithms), performance metrics (data rates, reach, power consumption) compared with traditional line-side coherent solutions, real-world deployment scenarios, and the trend toward IP and optical layer convergence. (from abstract only)
- **How**: Covers how coherent DSP, tunable lasers, and modern ADC/DAC integration let a pluggable form factor carry coherent modulation over metro-to-long-haul distances, displacing separate transponder shelves and moving coherent optics into router/switch ports.
- **Where applicable**: Optical transport and DCI design generally; vendor-neutral in physics, though examples will skew to Cisco's pluggable portfolio. Useful for anyone deciding between pluggable-coherent and transponder-based DCI architectures.

### Designing Routed Optical Networks: IP/MPLS Considerations - BRKSPG-2029

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161413770001NO6n)

Speakers: Emerson Moura (Cisco)

- **Why**: Routed Optical Networking (RON) — collapsing IP and DWDM into one managed layer — is a genuine architectural shift in WAN/DCI economics, and this is the IP-routing-layer half of the story, which is where the interesting design questions live.
- **What**: How the IP routing layer of a RON architecture works: how a simpler, IP-centric multi-service design reduces operator cost, improves asset utilization and resiliency, and enables network optimization for distributed applications, content, and peering. Includes a traditional IP/DWDM vs. RON comparison. (from abstract only)
- **How**: Rather than managing a separate optical layer with its own control plane, RON exposes optical capacity to the IP layer (coherent pluggables in routers), so routing decisions account for optical reach and spectrum directly — simplifying the architecture and letting the IGP/BGP layer drive end-to-end path selection.
- **Where applicable**: Service-provider and large DCI WANs primarily; requires coherent-pluggable-capable routers and a greenfield-ish willingness to restructure transport operations. Less applicable to enterprise campuses or small DC footprints.

### Kubernetes (K8s) Infrastructure Connectivity for ACI Network Designs for the Modern Data Center - BRKDCN-2663

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098291654001dJvz)

Speakers: Camillo Rossi (Cisco)

- **Why**: The session explicitly covers Cilium with eBGP and no overlay — the cloud-native dataplane combination the PM tracks — compared head-to-head with Cisco's ACI CNI, which is a useful lens on where vendor CNIs sit relative to generic eBPF/eBGP ones.
- **What**: An integration guide for running Kubernetes on ACI fabrics, comparing two CNI architectures: Cisco's free ACI CNI plugin versus Cilium with eBGP peering and no network overlay, ending with a demo of both. (from abstract only)
- **How**: ACI CNI bridges K8s networking into the ACI policy model (endpoint groups, contracts); the Cilium path runs eBPF dataplane in the pods with eBGP advertisements into the fabric, avoiding overlay encapsulation and keeping routing native end-to-end.
- **Where applicable**: ACI-based fabrics specifically for the first path; the Cilium/eBGP pattern generalizes to any BGP-capable underlay (including EVPN fabrics with a BGP peering policy). The comparison framing is valuable even outside ACI environments.

### Observing GenAI-Infrastructure: You Can't Protect What You Can't See - DEVNET-3310

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098450099001dFf5)

Speakers: Shannon McFarland (Cisco)

- **Why**: Directly combines the PM's cloud-native networking stack (Cilium/eBPF, Tetragon) with the emerging operational problem of GenAI workloads and agents — where runtime security and observability for LLM infrastructure is largely unsettled.
- **What**: A hands-on technical session on using OpenTelemetry, Jaeger, Cilium with eBPF, and Tetragon to observe and secure GenAI infrastructure including AI agents, with practical demos rather than slideware alone. (from abstract only)
- **How**: eBPF-based agents (Cilium/Hubble for flow-level visibility, Tetragon for policy enforcement and syscall-level runtime security) are wired to OpenTelemetry traces and Jaeger, correlating what agents are actually doing — network flows, process events, data movement — into one observability picture.
- **Where applicable**: Kubernetes-hosted GenAI/agent workloads primarily; the eBPF toolchain is open source and vendor-neutral, so this transfers outside Cisco shops. The specific value is the application to agentic/AI serving stacks, which few production runbooks cover yet.

### Deep Dive into Cisco's Use of QUIC, MASQUE and OS Native Capabilities to Deliver Frictionless Zero Trust Access - BRKSEC-3027

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098380884001dgEP)

Speakers: Vinny Parla (Cisco)

- **Why**: Sits exactly at the intersection of the PM's identity and network-security interests: standards-track access (MASQUE/QUIC) combined with passkeys/WebAuthn and OS-native clients — the credible near-term replacement for legacy VPN.
- **What**: How Cisco is building "frictionless" Zero Trust access on industry standards: MASQUE (proxying over HTTP/3/QUIC) instead of legacy tunnel protocols, WebAuthn/passkeys for user authentication, and native OS clients from Apple and Samsung alongside Cisco's Zero Trust Access module in Secure Client. (from abstract only)
- **How**: MASQUE provides an encrypted proxy over QUIC so per-app access control replaces full-tunnel VPN; authentication moves to passkeys (FIDO/WebAuthn) eliminating phishable credentials; OS-native integration makes connection as transparent as associating to Wi-Fi, with private 5G as another access path.
- **Where applicable**: Enterprise remote/hybrid access replacing or augmenting VPN. Standards-based in principle (IETF MASQUE, W3C WebAuthn), but the seamless-experience pieces depend on specific vendor partnerships (Apple, Google, Samsung) and Cisco's client — evaluate the protocol design separately from the product packaging.

### Everything You Ever Wanted to Know about Power in Routers and Switches (and Quite a Bit More) - BRKGRN-2161

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098325149001dRBH)

Speakers: LJ Wobker (Cisco), Lane Wigley (Cisco)

- **Why**: Power is becoming a first-order design constraint in physical DC networking (AI racks at 150kW+ make it unavoidable), and this is a systematic, test-data-backed treatment rather than a sustainability marketing talk. Wobker is a long-time hyperscale operator voice.
- **What**: A comprehensive grounding in power behavior of routers and switches: provisioning vs. typical vs. peak power; per-component breakdowns; how traffic, temperature, and other factors change draw; PSU efficiency and conversion loss; optics power; redundancy models; thermal limits in high-power systems; power modeling; and what actually saves power off-peak — with system-testing examples. (from abstract only)
- **How**: Walks from nameplate to real-world: how to model consumption from component-level data, where losses occur (PSU conversion, optics), how load and ambient temperature shift the curve, and quantifies which operational levers (e.g., idling ports, lower speeds) do and don't move the needle.
- **Where applicable**: Broadly applicable to any DC operator doing capacity planning, power budgeting, or sustainability reporting — the physics and methodology are vendor-neutral even if examples come from Cisco gear. Especially relevant alongside the AI-rack-power trends discussed elsewhere in this program.

### Multi-Tier Fabrics: Network Designs for the Modern Data Center - BRKDCN-2999

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296558001d0ED)

Speakers: Marina Ferreira (Cisco)

- **Why**: Topology and cost-engineering of DC fabrics (fat-tree/Clos, super-spine, 400G/800G economics, fixed vs. modular) is core physical-DC design knowledge, and this session covers the modern tier-expansion beyond classic leaf/spine.
- **What**: A tour of DC fabric topologies — fat-tree, Clos, leaf/spine — extended to super-spine layers and hyperscale-plane designs, plus practical guidance on cost-effective 400G/800G adoption and where fixed versus modular switches make sense. (from abstract only)
- **How**: Builds up from fat-tree/Clos math to multi-tier (super-spine / planar) architectures that scale past single-fabric limits, and frames the fixed-vs-modular and 40G→400G/800G speed decisions as cost-per-port and cabling/practicality trade-offs.
- **Where applicable**: General DC topology design, vendor-neutral in principle; expect Cisco port-count/pricing examples. The opening is introductory (definitions of Clos), but the super-spine and 400G/800G economics material is substantive for anyone planning a fabric refresh.

### Deployment of Micro-Segmentation in Cisco NX-OS VXLAN EVPN Fabrics with VXLAN Group Policy Option (GPO) - BRKDCN-2933

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294232001dxed)

Speakers: Max Ardica (Cisco)

- **Why**: East-west micro-segmentation in DC fabrics is a core security-plus-fabric problem, and GPO is an IETF-draft-track mechanism for carrying policy through VXLAN itself — an alternative to firewall-per-everything that's worth understanding on its merits.
- **What**: How to implement micro-segmentation in NX-OS VXLAN EVPN fabrics using security groups and security group ACLs carried via VXLAN Group Policy Option (IETF draft-smith-vxlan-group-policy-05), covering control-plane and data-plane components, common use cases, and service-chaining simplification. (from abstract only)
- **How**: GPO piggybacks a group policy ID in the VXLAN header, so every packet carries its source's security group; enforcement happens on group-tagged ACLs at the destination leaf rather than mid-fabric firewalls, decoupling policy from IP/subnet and following workloads anywhere in the fabric.
- **Where applicable**: NX-OS VXLAN EVPN fabrics specifically (Cisco implementation of a draft-stage IETF mechanism — note it's not yet a ratified standard). The policy-follows-workload pattern is general, but interop across vendors is limited while the draft is immature.

### Using Ethernet for AI Networking - CISCOU-2038

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098408268001dmuN)

Speakers: Peter Jones (Cisco)

- **Why**: The Ethernet-vs-InfiniBand question for AI clusters is the defining physical-DC debate of this cycle, and Peter Jones is a long-time standards hand at Cisco; this frames what Ethernet still needs to solve to win the AI fabric.
- **What**: A short strategic session on the unprecedented GenAI-driven build-out of AI-focused datacenters, InfiniBand's incumbency, and what it will take for standards-based Ethernet to displace it — a requirements list for Ethernet-based AI networking. (from abstract only)
- **How**: Expected to cover the well-known gaps (lossless behavior without fabric-wide PFC pathology, congestion control, multi-job performance isolation, scale-out topology) and how standards efforts (e.g., the Ultra Ethernet direction) aim to close them; the abstract itself is short, so depth must be verified from the recording.
- **Where applicable**: Strategic rather than a how-to; relevant to anyone planning AI-cluster fabrics or evaluating vendor AI-Ethernet offerings. Cisco-employee speaker means expect a pro-Ethernet (and pro-Cisco) framing.

## Adjacent

### Connecting Your Data to LLMs: Identity, Functions and Agents are all you Need - BRKETI-2411

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098315547001dOiX)

Speakers: Marcelo Yannuzzi (Cisco)

- **Why**: Agentic identity — who is allowed to touch which data when an LLM acts on a user's behalf — is squarely in the PM's identity wheelhouse, and this session describes an authorization architecture for LLM data access, albeit with heavy Cisco product framing.
- **What**: Architectures and tools for connecting enterprise data to LLMs without migrating it: real-time prompt inspection that identifies what data a request needs, determines whether the user has rightful access to it, and serves only authorized data — plus Cisco's products in this space. (from abstract only)
- **How**: Prompt-time analysis extracts data requirements from the user's natural-language request, then an authorization decision (presumably against existing identity/entitlement systems) gates which data the LLM is actually allowed to retrieve and serve, keeping data on-prem under enterprise control.
- **Where applicable**: Enterprises bringing GenAI to their own data rather than moving data to public clouds. Cisco-specific tooling is the demo vehicle, but the access-control-on-top-of-LLM-retrieval pattern is the generalizable part. Skeptic's note: expect product positioning; the identity architecture questions are the substance worth extracting.

### The New, Encrypted Protocol Stack Taking over the Internet and How to Deal with It - BRKSPM-2024

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161419037001N347)

Speakers: Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)

- **Why**: The QUIC/HTTP-3/DoH/ECH transition obsoletes core assumptions about network visibility and congestion management — a structural shift any network-security-literate PM should understand even if the session's remediation focus is service-provider oriented.
- **What**: How the new encrypted stack (QUIC + HTTP/3 + DoH + ECH/eSNI) is constructed and evolving, its measured share of traffic (claimed ~50% and doubling every 18 months), how it changes flow behavior and visibility, and what techniques SPs can use to keep pace on visibility, QoE, and spectrum efficiency. (from abstract only)
- **How**: Walks the protocol stack mechanics (QUIC's UDP-based encrypted transport, DNS encryption, encrypted client hello) and their consequences: application disintermediation of the network, loss of flow-level visibility, and congestion control moving to endpoints — then surveys SP countermeasures.
- **Where applicable**: Service-provider networks primarily (5G spectrum, QoE management), but the visibility-loss analysis applies to enterprise security monitoring too. Traffic-share figures are the speakers' claims; worth sanity-checking against independent measurements.

### QKD Impact on Optical System and PQC Solution - BRKOPT-3086

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098360722001d3sU)

Speakers: Maurizio Gazzola (Cisco)

- **Why**: Sits at the junction of optics and security: what hosting quantum key distribution channels would actually mean for optical transport design, and how that trade-off plays against post-quantum cryptography.
- **What**: The system-level implications for an optical transport network of hosting quantum channels (QKD), and an overview of Cisco's strategy favoring PQC. (from abstract only)
- **How**: Examines what co-hosting QKD requires of the optical layer (wavelength planning, attenuation budgets, coexistence with high-speed data channels), implicitly comparing that cost/complexity against a software-based PQC migration path.
- **Where applicable**: Optical transport operators and DCI planners weighing long-term cryptographic risk; the abstract is thin, so treat this as a strategy overview rather than a deep design session. Relevant background for the PMI's network-security + optics intersection, but not a working guide.

### Cisco 8000 and OVHcloud a Successful Adoption since 2020 - CSSSPG-2389

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098421931001dlr5)

Speakers: Antoine Petit (Cisco Systems, Inc.), Laurent Galais (Cisco), Simon Peccaud (OVHcloud)

- **Why**: A multi-year end-user deployment at Europe's largest cloud provider is the kind of case study the triage rules favor — but the abstract reads as a partnership success story with no scale, performance, or cost numbers disclosed, so keep expectations measured.
- **What**: The OVHcloud deployment of Cisco 8000 Series (Silicon One) routers since 2020: deployment process, collaboration with Cisco support, integration into the existing network, and lessons learned. (from abstract only)
- **How**: A narrative walkthrough of a large European cloud provider adopting Silicon One-based routing across its infrastructure, emphasizing operational efficiency and the support relationship.
- **Where applicable**: Large cloud/SP operators. The useful content depends entirely on whether the recorded session includes real deployment figures (scale, migration friction, power/TCO outcomes) — the abstract's absence of any numbers is a warning sign that this may be closer to a customer-appreciation slot than an engineering case study.

### Secure Operations for an IPv6 Network - BRKSEC-2044

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098365329001d8Rq)

Speakers: Eric Vyncke (Cisco)

- **Why**: Authored by an author of RFC 9099 (IPv6 Security Operations), this is the authoritative treatment of the IPv6-specific security deltas — practical and standards-grounded rather than vendor-feature-driven.
- **What**: What changes between IPv4 and IPv6 security operations: attack surfaces specific to IPv6 (extension headers, NDP/RA issues, L2 threats), prevention techniques, and how to run audit and event correlation in dual-stack environments from DC to wireless. (from abstract only)
- **How**: A structured walk through the IPv6 security differences — extension header filtering dilemmas, link-layer attack mitigation (RA guard, SEND considerations), address-scan resistance that changes attacker recon, and dual-stack logging/correlation practice — grounded in RFC 9099.
- **Where applicable**: Any dual-stack network; vendor-neutral in content since it follows the RFC. Adjacent rather than core for this PM only because IPv6 ops hardening is steady-state practice rather than a new frontier — but high quality within that lane.

### AI-Ready Data Center - Sustainability vs. Infrastructure Requirements - How to get your Data Center Ready for the Coming AImagedon - BRKGRN-2419

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098326253001dF62)

Speakers: Christopher Liljenstolpe (Cisco), Heiko Ebermann (Vertiv), John Bean (GR Cooling)

- **Why**: The facility-side constraint on everything else in this program: the cited trajectory from 16–30 kW to 150–250 kW per rack over two years is an order-of-magnitude shift that reshapes what network (and compute) designs are even buildable.
- **What**: An exploration of how choices in rack power and thermal density ripple through facility design, and how AI can be used to optimize cooling energy, workload placement, and operating conditions — plus guidance on modernizing toward energy-efficient hardware and cooling systems. (from abstract only)
- **How**: A panel-style session (network vendor + cooling/infrastructure vendors) working through the power/thermal design space of AI-ready facilities and where energy-efficiency optimization (including AI-driven workload distribution and cooling control) can pay off.
- **Where applicable**: Datacenter planning and facilities engineering; the power trajectory figures are the transferable datapoints. Adjacent for this PM (facility, not network, engineering), but it's the physical envelope the AI-fabric sessions above must live within.

## Wildcard

### Packet Buddy - Chatting with your PCAPs, via the Cloud or Locally on Your Own Machine! - AIHUB-2000

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161392766001Nu0p)

Speakers: Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco)

- **Why**: Not a core interest, but a genuinely novel application of LLMs to a networking-native workflow — querying packet captures conversationally — and it's open source, so it can be inspected and run locally rather than just watched.
- **What**: An open-source tool ("Packet Buddy") that lets an LLM analyze your own Wireshark captures: answering what traffic is present, what errors it detects, and explaining packet flows — deployable either in the cloud or locally. (from abstract only)
- **How**: Feeds pcap data to a choice of LLMs and lets the analyst interrogate it in natural language; the local-deployment option keeps sensitive captures on-prem.
- **Where applicable**: Any network operator doing packet-level troubleshooting; most valuable as a signal of where LLM-assisted network diagnostics is heading. Note the privacy/trust question of sharing captures with cloud models — the local mode exists precisely because of it.

### Securing the Olympics: The Cybersecurity Architecture for Paris 2024 - BRKSEC-2019

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098364965001duar)

Speakers: Piotr Jarzynka (Cisco)

- **Why**: A one-of-a-kind adversarial environment — a globally targeted, time-boxed, sprawling venue network — with real lessons on architecture for ephemeral, high-threat deployments that no vendor lab can simulate.
- **What**: The cybersecurity architecture actually implemented for the Paris 2024 Olympics and Paralympics: the governance, prevention, detection, and response design, lessons learned, and best practices extracted. (from abstract only)
- **How**: A holistic architecture spanning governance to response, built to protect competitions against a wide range of threat actors for the duration of the event; the value is in the incident-informed design decisions rather than any single product.
- **Where applicable**: Large temporary events and any environment requiring a complete, from-scratch security posture on a hard deadline; generalized best practices rather than a repeatable blueprint. Worth a skim for the operational design constraints alone.

### Using Agentic IaC for Managing Infrastructure: the Good, the Bad, and the Ugly - BRKETI-2286

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098315199001droG)

Speakers: Peter Bosch (Cisco)

- **Why**: Agentic AI operating infrastructure-as-code is arriving fast in exactly the network/security ops domain this PM owns — and the promising "good, bad, ugly" framing plus an explicit open call for contributors suggests honest failure discussion rather than triumphalism.
- **What**: An approach where agentic AI teams create, validate, replicate, review, and approve infrastructure changes autonomously — capturing cloud-native and network state in GitHub as source of truth, managing it through GitHub, reducing PR-review overhead (claimed up to 30% of team time) while maintaining governance, and auto-writing Terraform/IaC/network config from natural language. Includes worked use cases and demos of what works and what doesn't. (from abstract only)
- **How**: Infrastructure and network state is mirrored in GitHub; agents propose changes against it, learn from review outcomes, and validate updates automatically — aiming to shift humans from reviewing routine PRs to supervising agent teams.
- **Where applicable**: Teams already running Terraform/IaC with GitHub-centric workflows. Explicitly experimental (the speaker asks the audience to help test and contribute). Caution: autonomous PR approval for network changes is a governance and safety frontier — the "ugly" section is likely the most valuable part.

## Themes

- **Ethernet for AI is the dominant physical-DC thread**: at least five sessions (AI fabrics on Silicon One/SONiC, storage/RoCEv2 lossless Ethernet, Ethernet-vs-InfiniBand strategy, AI-rack power and cooling) converge on the same question — can standard Ethernet deliver InfiniBand-class lossless performance, and what does the facility have to look like to host it.
- **Power and optics are the binding constraints**: per-rack power moving from 16–30 kW to 150–250 kW in two years, coherent pluggables collapsing IP/optical layers, and a full session just on power behavior of routers/switches — physical-layer engineering is where the hard problems have returned.
- **EVPN/VXLAN remains the workhorse fabric, now maturing into multi-site**: the dataplane-internals and multi-site deep dives show the ecosystem consolidating on EVPN for fabric interconnect, plus standards-track micro-segmentation (GPO) baked into the encapsulation.
- **The encrypted-protocol transition (QUIC/MASQUE/ECH) is reshaping both access and visibility**: zero-trust access rebuilt on QUIC/MASQUE with passkeys, while SP-side visibility assumptions are being obsoleted — identity (WebAuthn/FIDO) is becoming the durable anchor as network-layer visibility disappears.
- **GenAI infrastructure is pulling the cloud-native stack into new territory**: Cilium/eBPF/Tetragon observability for AI agents, identity-aware data access for LLMs, and agentic AI writing and approving infrastructure changes — the same eBPF and identity primitives the PM already tracks, aimed at workloads that didn't exist two years ago.
- **Selection note**: BRKSEC-2144 (Modern Authentication Explained to the Network Professional) was pre-selected as core but dropped — it's a well-regarded bridging explainer, yet for a PM with 15 years across networking and identity, OAuth/OIDC/SAML/FIDO fundamentals are redundant; nothing in the abstract signals novel attack or protocol content beyond standard MFA-fatigue/session-hijacking material.
