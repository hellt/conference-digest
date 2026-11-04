<!--
conference: Cisco Live Europe 2026 (Amsterdam)
type: vendor
source_url: https://www.ciscolive.com/on-demand/on-demand-library.html?search.event=1769534158486003Q4dl
generated: 2026-11-04
registry_key: ciscolive-eu-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Cisco Live Europe 2026 (Amsterdam)

**Note on sources**: all session `page:` links point to Cisco's login-gated on-demand library (a JavaScript single-page app); fetch attempts returned only the site shell, not session content. Every write-up below is therefore **(from abstract only)**. Cisco Live is a vendor conference: product positioning is the default, and the picks below were filtered for sessions with genuine technical or operational substance.

## Core

### 400G, 800G, and Terabit Pluggable Optics: What You Need to Know - BRKOPT-2699

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243062610001vhXB)

Mark Nowell (Cisco), Errol Roberts (Cisco)

- **Why**: The optics roadmap determines what DC and WAN fabrics can look like 2-3 years out — form factor, reach, power, and breakout capability constrain every topology decision. Nowell has long been one of the more credible voices on high-speed interconnect.
- **What**: A forward-looking technical survey of pluggable optics: current 400G technologies and applications, next-gen form factors for 800G and 1.6T (including breakout use cases), the 800Gb/s and 1.6Tb/s Ethernet standardization efforts, and the state of co-packaged optics for integrating optical interfaces into ASICs (from abstract only).
- **How**: Covers both coherent and noncoherent optics and frames developments around what is driving them and what must be prioritized for success — aimed at attendees who already deploy optical modules.
- **Where applicable**: Broadly applicable to anyone specifying DC/WAN interconnect; the co-packaged portion is necessarily forward-looking and standards-dependent rather than deployable today.

### Advancements and Applications of Coherent Pluggable Technology in High Bandwidth Transport Networks - BRKOPT-2556

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243062806001vUh2)

Anuj Malik (Cisco)

- **Why**: Coherent pluggables in routed ports are the mechanism behind the IP/optical convergence several operators at this conference claim as their headline win. Understanding the DSP/laser internals separates real capability from datasheet numbers.
- **What**: A technical breakdown of coherent pluggable technology: tunable lasers, high-speed ADC/DACs, and DSP algorithms, plus performance comparisons (data rate, reach, power) against traditional coherent solutions, with deployment scenarios and case studies (from abstract only).
- **How**: Component-level walkthrough of the coherent DSP chain, then comparison of metrics and discussion of the trend toward IP/optical layer convergence.
- **Where applicable**: High-bandwidth transport / WAN and DCI contexts. The "convergence" framing is vendor-aligned (Cisco Routed Optical Networking); the component physics is general.

### Lessons Navigating from Proof of Concept to Production with IP/Optical Convergence: How DT is Evolving their Transport Network with Cisco Routed Optical Networking - CSSENS-2717

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242953872001vHGs)

Nils Warnke (Deutsche Telekom), Silke Bauten (Cisco)

- **Why**: This is the standout end-user talk of the set: an operator's lead architect explaining how IP/optical convergence actually got done — the organizational and qualification friction, not the slideware. DT projects over 85% energy savings from collapsing standalone optical gear into coherent pluggables on routed ports, a number worth pressure-testing in the Q&A.
- **What**: DT's Horizontal Digital Architecture network evolution: moving from a technology vision to production, covering four readiness areas — hardware qualification of pluggables across Cisco and third-party host platforms, process automation to cut service lead time, cross-domain operations/assurance (alarm correlation), and field/capacity readiness for rollout (from abstract only).
- **How**: Real deployment narrative: integrating roles and responsibilities across IP and optical teams, and building qualification, automation, and assurance workflows around pluggable-based transport.
- **Where applicable**: DT-specific production setup, but the lessons (multi-vendor host qualification, org merging of IP and optical teams) generalize to any carrier or large DC operator pursuing convergence. Numbers are projections, not necessarily measured results.

### How the World's Largest Backbone Provider is Leveraging the AI Opportunity - CSSAI-1596

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242951729001vb1U)

Abeel Choudry (Cisco), Dariusz Solowiej Solowiej (Arelion)

- **Why**: Arelion carries ~70% of global internet routes — backbone-scale evidence of what converged IP/optical architecture does at the extreme end of WAN. Treat the headline percentages with appropriate skepticism; the scale detail is the value.
- **What**: How Arelion claims to have achieved 66% CapEx and 95% OpEx reduction while repositioning for AI-driven traffic, via Routed Optical Networking with coherent optics, Silicon One-based Cisco 8000 routers, and automated assurance (from abstract only).
- **How**: Network convergence collapsing transport layers, plus automation/analytics for service assurance and moves toward self-healing networks and self-service capabilities.
- **Where applicable**: Arelion-specific — a single global backbone operator with twice its nearest competitor's capacity. The percentages are vendor-co-presented and unaudited; the architectural direction (coherent pluggables in routed ports, heavy automation) is where the whole industry is heading. Watch for whether they give real before/after operational detail.

### Cisco Nexus 9000 Architecture - BRKDCN-3939

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243046210001v3NV)

Faraz Taifehesmatian (Cisco)

- **Why**: ASIC architecture and forwarding mechanics of the workhorse DC switching line — exactly the "switching internals" content this PM wants, and the substrate for the VXLAN EVPN and AI-fabric sessions elsewhere in the program.
- **What**: An in-depth architecture study of the latest-generation Nexus 9000 modular and top-of-rack switches: ASIC architecture, forwarding mechanics, physical design, and hardware-enabled features (from abstract only).
- **How**: Internals-first walkthrough rather than feature marketing — how packets actually move through the silicon and what hardware capabilities the feature set leans on.
- **Where applicable**: Nexus 9000-specific, but the forwarding-model detail transfers to anyone evaluating DC switch ASICs generally.

### Everything You Ever Wanted to Know about Power in Routers and Switches (and Quite a Bit More) - PSOGRN-2161

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242974994001vIpj)

LJ Wobker (Cisco), Lane Wigley (Cisco)

- **Why**: Power and thermal are now first-order constraints in DC design — with AI racks pushing 150-250 kW, understanding what actually moves power consumption in network gear (and what doesn't) is core systems knowledge, not facilities trivia.
- **What**: A systematic treatment of power in network equipment: provisioning vs. typical vs. peak; per-component breakdowns; effects of traffic and temperature; PSU efficiency; optics power; conversion loss; redundancy models; thermals in high-power systems; and which off-peak "power saving" measures actually help — supported by system-test examples (from abstract only).
- **How**: Measurement-driven: system testing examples are used to ground claims about how load, temperature, and configuration change real draw.
- **Where applicable**: General across router/switch platforms; concrete numbers will be Cisco-specific but the methodology (typical vs. worst-case provisioning, optics power accounting) is broadly applicable.

### VXLAN EVPN: A Deep Dive into Packet Forwarding - BRKDCN-3966

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243046414001vKb8)

Lukas Krattiger (Cisco)

- **Why**: EVPN is the dominant DC overlay control plane and datapath-debugging knowledge is where most operational pain lives. This is a datapath-internals talk, not an EVPN primer.
- **What**: A packet-by-packet walkthrough of VXLAN EVPN forwarding — routing, bridging, and multi-destination handling from ingress VTEP through to egress VTEP and beyond (from abstract only).
- **How**: "Day in the life of a packet" structure following a concrete frame through the overlay.
- **Where applicable**: Any VXLAN EVPN fabric (Nexus 9K baseline is Cisco's, but the mechanics are standard). Assumes working EVPN knowledge.

### Demystifying AI Infrastructure for a Network Engineer - BRKDCN-2971

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242961568001vbki)

Paresh Gupta (Cisco)

- **Why**: RDMA/lossless Ethernet is squarely this PM's core territory, and this session packages the current AI-fabric networking stack — RoCE, PFC, DC QCN, collective libraries, Spectrum-X, Ultra Ethernet — in one place. Framed as intro, but the content map is the industry's Ethernet-for-AI state of play.
- **What**: How GPUs communicate during distributed AI jobs and how that traffic differs from ordinary DC workloads; covers RoCE, PFC, DC QCN; collective operations via NCCL/RCCL/HCCL; NVIDIA Spectrum-X's problem statement and solution; and where Cisco Nexus, Hyperfabric for AI, and Ultra Ethernet fit (from abstract only).
- **How**: Fundamentals-first build-up from GPU communication patterns to lossless-fabric mechanisms and vendor approaches.
- **Where applicable**: AI/ML cluster fabric design generally. The Spectrum-X comparison is inevitably vendor-slanted; the RoCE/PFC/QCN and NCCL material is standard. Skip if you already operate RoCE fabrics day-to-day.

### Benchmarking AIML Infrastructure at Scale: AIML Architectures, AI Workloads and Reproducibility for High Performance Data Centers - BRKDCN-2651

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242961375001v37e)

Rakesh Kumar (Cisco), Ram Gandikota (Cisco)

- **Why**: The hardest open problem in AI fabrics is trustworthy, reproducible benchmarking — NCCL collective performance is dominated by network behavior and tuning is opaque. This is one of the few sessions engaging with methodology rather than just results.
- **What**: The benchmarking methodologies Cisco used across large-scale cluster engagements: alignment with open standards, reproducibility strategies, application-level KPIs like NCCL collectives, network-tuning challenges, and how packet trimming and UEC-based (Ultra Ethernet Consortium) feature alignment are reshaping Ethernet standards for AIML clusters (from abstract only).
- **How**: Case-study-driven methodology work — reducing test drift between benchmark and production, making network behavior a first-class measured variable.
- **Where applicable**: AI training/inference clusters; the UEC-alignment content matters to anyone planning Ethernet-based AI fabrics. Lessons come from Cisco cluster engagements, so some method choices will be Cisco-toolchain-specific.

### Redefining Netflix BGP Architecture with IOS-XRv 9000 Route-Reflector Appliance - CSSENS-2442

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242966722001vl2i)

Frederic Cuiller (Cisco), Elise VENNEGUES (Netflix)

- **Why**: A joint operator/vendor case study on BGP route-reflector architecture at global scale — BGP internals plus the messy realities of validation and migration, told by the operator themselves.
- **What**: How Netflix and Cisco evolved Netflix's BGP architecture around the IOS XRv9000 on a UCS M7 appliance, developed and refined against Netflix's requirements: motivations, design, validation, deployment, and migration strategy with lessons learned (from abstract only).
- **How**: Design-and-migrate narrative: technical challenges, collaborative development, validation and best practices for a seamless transition from the previous route-reflector setup.
- **Where applicable**: Netflix-specific in scale and requirements, but the route-reflector appliance pattern and migration methodology generalize to any large SP or edge network. Expect concrete only if the speakers go deep on validation data.

### Life of a Packet in Kubernetes: A Network Engineer's Guide - BRKCLD-3734

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243028083001vmAe)

Nico Vibert (Cisco)

- **Why**: This hits the PM's cloud-native interests almost exactly: Cilium as dataplane, Gateway API, BGP, egress, IPsec, DSR, BIG TCP, topology-aware routing — mapped onto a full packet journey rather than feature-by-feature.
- **What**: An advanced, demo-driven trace of a packet through a Kubernetes cluster: VXLAN/Geneve overlays, Gateway API, Egress Gateway, BGP routing, IPsec encryption, DSR, multi-cluster Cluster Mesh, plus performance features (BIG TCP, topology-aware traffic engineering) and troubleshooting with Hubble, Cilium CLI, and Wireshark (from abstract only).
- **How**: Packet-walk structure — follow real traffic through encapsulation, routing, policy, and encryption layers, correlating observed behavior with Kubernetes constructs.
- **Where applicable**: Cilium/Isovalent-specific dataplane (that's the point — it's the de facto eBPF dataplane), but the overlay/routing/egress mechanics transfer to most CNI implementations. Assumes solid IP and Kubernetes grounding.

### Are You Prepared for the Next Typhoon? - BRKGEN-2499

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243096256001vCJN)

Paul Giralt (Cisco)

- **Why**: Salt Typhoon is the reference event for nation-state compromise of network infrastructure, and this session goes beyond incident retelling: it previews concrete secure-by-design changes across Cisco's OSes and controllers — operational implications the PM will have to absorb regardless of vendor.
- **What**: Talos insight into Salt Typhoon's tactics against telecommunications providers, followed by Cisco's Resilient Infrastructure initiative: specific software changes across IOS XE, IOS XR, NX-OS, ISE, ASA/FTD, and controllers (Catalyst Center, Meraki Dashboard, Catalyst SD-WAN) (from abstract only).
- **How**: TTP analysis of the actual attacks, then portfolio-wide hardening changes and the operational preparation needed before deploying secure-by-default software.
- **Where applicable**: The lessons apply to networks of all types, not just SPs. The roadmap portion is Cisco-specific — but it's a preview of breaking-change-style hardening other vendors will be pushed toward.

### Designing Zero Trust Data Center Segmentation Architecture - BRKDCN-2930

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243047474001vNXj)

Cesar Obediente (Cisco), Brenden Buresh (Cisco)

- **Why**: A structured progression from traditional DC firewalling to layered zero-trust segmentation, and it notably brings DPU/SmartSwitch and host-based (Isovalent/Cilium-lineage) enforcement into the same policy model as the fabric — the network/host security convergence this PM tracks.
- **What**: How to build DC segmentation in layers on a Nexus 9K VXLAN EVPN baseline: macro-segmentation with VRFs, micro-segmentation with VXLAN GPO (L4 stateless), then adding DPU SmartSwitch and Isovalent host-based agents for L4 stateful controls, culminating in a hybrid mesh firewall concept with one central security controller authoring policy across network, host, and appliance enforcement points (from abstract only).
- **How**: Incremental architecture: each layer adds enforcement capability without discarding the previous; single policy authority distributed to multiple enforcement points.
- **Where applicable**: Nexus 9K + Cisco DPU/Isovalent stack for the full vision, but the macro/micro-segmentation layering pattern is general. The "hybrid mesh firewall" portion is Cisco's emerging architecture — treat as direction-setting rather than proven production pattern.

### The New, QUIC Based Encrypted Protocol Stack Taking over the Internet and How to Deal with It - BRKSPM-2024

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243061205001vQoo)

Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)

- **Why**: QUIC + HTTP/3 + DoH + ECH is dismantling the visibility and traffic-management assumptions most network and security infrastructure was built on. The abstract cites QUIC at ~50% of total traffic, doubling every 18 months — a structural shift, not an SP niche topic.
- **What**: How the QUIC-based encrypted stack is constructed and evolving, its behavior in terms of visibility and flow control, its impact on infrastructure elements, and the techniques providers can use to keep pace — traffic visibility, QoE monitoring/management, and efficient use of 5G spectrum (from abstract only).
- **How**: Protocol-level decomposition: TLS 1.3 encryption removing application visibility, congestion management moving into the application, applications disintermediating the network.
- **Where applicable**: Framed for service providers, but the visibility loss applies to any enterprise DC or security team doing traffic inspection, QoS, or telemetry on the wire.

### Hijacking Trust: Weaponizing Stolen Cookies and Tokens - BRKSEC-2132

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242947331001vpW4)

Stefan Duernberger (Cisco)

- **Why**: Session-token theft via adversary-in-the-middle proxies is now the dominant bypass of password- and MFA-based authentication. For an identity-focused PM, the defensive side here — device-bound credentials and shared signals — is the current frontier.
- **What**: Real-world session hijacking techniques using tools like Evilginx and EvilnoVNC to steal authentication cookies, then the defensive stack: OAuth 2.0/OIDC mechanics, Google's Device-Bound Session Credentials (DBSC), Cisco Duo Passport, and the Shared Signals and Events framework for continuous authentication trust (from abstract only).
- **How**: Offense-then-defense: demonstrate the cookie-theft flow, then show how device-bound session credentials and shared-signals eventing close it.
- **Where applicable**: Broadly applicable to web authentication generally; DBSC is browser-dependent (Chromium lineage) and Duo Passport is Cisco product, but the protocol analysis is vendor-neutral.

### Rethinking Identity, Policy, and Access Control (IPAC) for Agentic AI - BRKETI-2623

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242993932001vjug)

Marcelo Yannuzzi (Cisco)

- **Why**: Agentic identity is where the PM's identity work is heading, and this is one of the first vendor architectures that names the actual problem: current IAM scopes, scopes authorization around humans and static service accounts, not autonomous NL-driven entities acting at machine speed.
- **What**: The technology gaps in today's IAM for agentic AI, and a proposed IPAC architecture covering: dynamic trust establishment among users, agents, and MCP servers (Just-In-Time identification, Multi-Factor Verification across domains), policy that defines what autonomous entities may do without a human in the loop, and granular authorization for entities communicating in natural language — with a demo and pointers to Cisco's open-source efforts (from abstract only).
- **How**: Architecture-plus-demo: identify the gaps (static identity, human-in-loop assumptions), then layer JIT identification and policy enforcement over agent/MCP interactions.
- **Where applicable**: Early-stage/forward-looking — this is where the field is going rather than where it is. Note the SPIFFE/SPIRE-shaped hole: workload-identity primitives would be the natural substrate, worth probing in Q&A. Cisco "innovations and open source efforts" means expect some product framing.

### Enterprise-Ready Agentic Workflows: Hardening MCP with Policy-as-Code - DEVNET-2685

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242992480001vsg9)

Lori Jakab (Cisco)

- **Why**: MCP is spreading into network automation exactly where this PM operates, and its security model is genuinely immature. Applying OPA/Rego to JSON-RPC MCP traffic is a concrete, standards-agnostic pattern — policy-as-Code spanning agents and traditional automation is a real near-term need.
- **What**: Why MCP's current authentication mechanisms fall short of enterprise requirements, and how to harden MCP servers with Policy-as-Code: OPA and Rego applied to JSON-RPC messages between MCP clients and servers, unifying access control across agentic workflows and existing API/script-based automation (from abstract only).
- **How**: Extend policy enforcement from traditional API payloads to MCP JSON-RPC messages via OPA, with demonstrations including real-world Cisco deployment scenarios.
- **Where applicable**: General technique (OPA/Rego are open source; MCP is an open protocol), not locked to Cisco infrastructure — though demos are Cisco-centric. Requires comfort with automation tooling.

## Adjacent

### Cisco Nexus One: An Architecture for your Cisco Datacenter of Tomorrow - BRKDCN-2602

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243043040001vJvO)

Max Ardica (Cisco)

- **Why**: Signals how Cisco plans to reconcile its two competing DC architectures (Nexus VXLAN/EVPN and ACI) — relevant strategic context for anyone operating or evaluating either.
- **What**: Nexus One: a new architecture integrating Nexus VXLAN/EVPN fabrics with ACI, with seamless traffic flow between the two and single-pane management built around automation and orchestration (from abstract only).
- **How**: Integration layer plus unified management/automation across both architectures.
- **Where applicable**: Cisco-shop specific and new/unproven; this is architecture direction, not battle-tested deployment. Treat as a roadmap read on vendor convergence strategy.

### Agile Services Networking: Scaling Across Data Centers and Workloads - PSOMSI-1186

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243010508001vGHC)

Krithika Moorthy (Cisco), Tim Hu (Cisco)

- **Why**: The newsworthy part is not the router — it's SONiC running on Cisco Silicon One hardware for DCI. A major incumbent shipping its own silicon with a disaggregated NOS is a real shift in the DC/WAN interconnect market.
- **What**: The Cisco 8223 router and Silicon One P200 processor positioned for Data Center Interconnect: deep-buffer architecture to minimize congestion and packet loss for latency-sensitive and bandwidth-heavy workloads, plus SONiC OS on the 8223 for AI networking and disaggregated architectures (from abstract only).
- **How**: Deep-buffer P200-based system design, SONiC as the OS layer, framed under Cisco's Agile Services Networking architecture.
- **Where applicable**: Largely a product launch session — throughput and efficiency claims will be vendor numbers. Worth attending for the SONiC-on-Silicon-One angle and buffer-architecture rationale, not for neutral evaluation data.

### Designing Next-Generation DC and WAN Networks for the Neo-Cloud Era with Cisco 8000, SONiC and XR - BRKMSI-1471

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243009711001vm1L)

Krithika Moorthy (Cisco), Jiri Chaloupka (Cisco)

- **Why**: The IOS XR (WAN/backbone) + SONiC (DC) split as a deliberate two-NOS operating model is a useful reference pattern, even if presented through Cisco's reference-architecture lens.
- **What**: The Neo-Cloud reference architecture: IOS XR for backbone roles, SONiC for data center functions, unified operations across DC and WAN; high-performance interconnect design, multi-vendor interoperability, capacity planning, redundancy, and traffic optimization, illustrated with real-world use cases (from abstract only).
- **How**: Role-based OS assignment across domains with an operations layer aimed at consistency between them.
- **Where applicable**: Cisco reference architecture; the pattern (split NOS by domain, unified ops) generalizes, but specifics are Cisco 8000-family-bound.

### Introduction to eBPF - BRKSEC-2169

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243084108001vpus)

Liz Rice (Cisco)

- **Why**: Liz Rice is the most credible popularizer of eBPF, and her presence on the Cisco roster (via Isovalent) reflects how deeply eBPF is being absorbed into Cisco's security and networking strategy. For a PM already fluent in eBPF/Cilium, the technology content will be familiar — the signal is the messenger and venue.
- **What**: An in-depth introduction to eBPF: origins, rewards, challenges, with live demos of what eBPF is and how it enables high-performance security, networking, and observability capabilities (from abstract only).
- **How**: Live demonstration-driven explanation of eBPF's mechanics and why it has been called "superpowers for Linux."
- **Where applicable**: Foundational and vendor-neutral in content. Skip if you already work with eBPF daily; useful for onboarding colleagues or calibrating how a major vendor is positioning the technology.

## Wildcard

### How to Network LLMs. Splitting Large Language Models Running on GPUs Across a Network - BRKOPS-2931

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243092340001vR9F)

Dave Zacks (Cisco), Patrick leMaistre (Cisco)

- **Why**: Not a core interest for this PM, but inverts the usual AI-fabric question: instead of "what network does training need," it asks "what the network must look like to host disaggregated inference/models across hosts" — on-prem, with private local datasets. A different lens on why DC fabric design is changing.
- **What**: How LLMs that don't fit in one GPU or one server are split across multiple hosts and linked by the network, focusing on what a properly designed network must provide for distributed, on-premises AI model hosting (from abstract only).
- **How**: Deep-dive walkthrough (by two veteran Cisco Live speakers) of model partitioning across systems and the network requirements that result.
- **Where applicable**: On-prem AI model hosting scenarios; likely conceptual rather than benchmarked, and inevitably Cisco-portfolio-flavored. The abstraction transfers to any fabric supporting split models.

### Preparing for AI Workloads: Options for Integrated Rack Power and Cooling Systems - BRKCOM-2530

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770242962555001v9Nz)

Christopher Liljenstolpe (Cisco), Fabio Gori (Cisco)

- **Why**: Per-rack power planning jumping from 16-30 kW to 150-250+ kW in two years is the physical constraint that will reshape DC topology, cabling, and even optics choices — this is adjacent to the PM's physical-DC world but its consequences land squarely in it.
- **What**: The impact of rack power and thermal density choices on AI-ready facilities, how AI can optimize cooling energy and workload distribution across servers, and how to select cooling systems that prioritize energy efficiency without compromising performance (from abstract only).
- **How**: Options analysis across integrated rack power/cooling approaches, with AI-assisted optimization of cooling and workload placement.
- **Where applicable**: New AI build-outs and retrofits; the 150-250+ kW/rack figures are hyperscale/AI-cluster-specific. Liljenstolpe's DC background suggests this will be more grounded than a facilities-vendor pitch.

### Preparation Guide to Emergency Comms and Networking using Amateur Radios (HAM) - BRKGEN-1012

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1770243096853001vcsF)

Jimmy Alignay (Cisco)

- **Why**: Genuinely off-pattern for a vendor conference: packet radio's role in the origins of IP networking (ALOHAnet → ARPANET lineage), plus practical emergency-comms deployments from hurricanes Helene and Milton 2024. A reminder of what "carrier-free" networking looks like and why foundational comms matter in disaster ops.
- **What**: The history of packet switching from ALOHAnet through amateur packet radio to modern IP, real-world emergency communications deployments supporting first responders and network operations after the 2024 hurricanes, and how modern amateur radio integrates Layer 2/Layer 3 networking with Cisco gear and Starlink (from abstract only).
- **How**: Historical narrative plus tactical deployment case studies and practical guidance for getting started.
- **Where applicable**: Emergency-preparedness and remote-site contexts; the historical networking content (ALOHAnet's influence on Ethernet's CSMA lineage) is a genuinely interesting wildcard for anyone who cares about where the technology came from.

## Themes

- **Ethernet-for-AI is the dominant DC fabric driver**: RoCE/PFC/DC QCN, NCCL-driven benchmarking, UEC alignment, and packet trimming recur across sessions — lossless-fabric work has moved from niche to the center of the DC track.
- **IP/optical convergence is now operator-proven, not vendor theory**: DT and Arelion both present production migrations to coherent pluggables in routed ports, with the interesting content in qualification, operations, and organizational lessons rather than the (vendor-co-presented) savings percentages.
- **Co-packaged optics and 1.6T Ethernet are the next planning horizon**: the optics sessions treat 800G as "current" and 1.6T standardization plus co-packaging as the forward agenda — optics roadmaps now gate fabric design.
- **Power and thermal became network engineering problems**: per-rack power footprints of 150-250+ kW mean power modeling, buffer/thermal design, and cooling choices now appear in routing and switching sessions, not just facilities tracks.
- **Agentic AI identity/policy is emerging as a real IAM subfield**: two sessions tackle trust, authorization, and policy for autonomous agents (MCP, OPA/Rego, JIT identification) — the identity track is visibly retooling around non-human actors.
- **Secure-by-default is turning into breaking-change management**: the Salt Typhoon response session previews portfolio-wide hardening changes across IOS/NX-OS/controllers — expect operational-preparation work wherever infrastructure defaults shift.
- **Cisco absorbed Isovalent and is distributing it everywhere**: eBPF/Cilium now appears in the K8s networking track, DC segmentation architecture, and security sessions — the acquisition is visibly reshaping the vendor's DC strategy, and SONiC-on-Silicon-One signals a parallel disaggregation hedge.
