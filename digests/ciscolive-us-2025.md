<!--
conference: Cisco Live US 2025 (San Diego)
type: vendor
source_url: https://www.ciscolive.com/on-demand/on-demand-library.html?search.event=1748366287882001oJzH
generated: 2026-11-04
registry_key: ciscolive-us-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Cisco Live US 2025 (San Diego)

*Enrichment note: the Cisco Live on-demand library is a login-gated JavaScript app; page fetches returned only the site shell, so every write-up below is grounded solely in the program abstracts. Vendor-program caveat applies throughout — Cisco speakers presenting Cisco products — and each entry flags where the substance looks general versus product-specific.*

## Core

### 400G, 800G, and Terabit Pluggable Optics: What You Need to Know - BRKOPT-2699

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967757001zfoK)

Mark Nowell (Cisco), Errol Roberts (Cisco)

- **Why**: The optics roadmap is now the binding constraint on DC fabric design — power, reach, and breakout options determine what topologies are even buildable. Nowell is a long-standing IEEE 802.3 optics contributor, which makes this a standards-insider survey rather than a datasheet read.
- **What**: A survey of current 400G pluggable optics and their applications, next-generation 800G/1.6T form factors including breakout use cases, the status of 800 Gb/s and 1.6 Tb/s Ethernet standardization, and co-packaged optics (integrating optical interfaces into switch ASICs), framed by industry dynamics and AI-driven demand (from abstract only).
- **How**: Technology survey across form factors, IEEE standardization tracks, and co-packaging directions, covering both coherent and noncoherent optics.
- **Where applicable**: Broadly applicable to anyone specifying optical interconnect for DC or DCI — the standards and form-factor content is vendor-neutral even though the speaker is Cisco. Assumes working deployment knowledge of optical modules.

### Advancements and Applications of Coherent Pluggable Technology in High Bandwidth Transport Networks - BRKOPT-2556

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963268001zbFi)

Anuj Malik (Cisco)

- **Why**: Coherent pluggables are collapsing the boundary between the IP and optical layers — directly relevant to DC/WAN interconnect, where the same pluggable now serves router ports and line systems.
- **What**: The technical underpinnings of coherent pluggables — tunable lasers, high-speed ADC/DACs, DSP algorithms — plus performance comparisons (data rates, reach, power consumption) against traditional coherent solutions, real-world deployment scenarios, and the trend toward IP/optical convergence (from abstract only).
- **How**: Coherent DSP packaged into pluggable transceiver form factors, compared against embedded coherent line systems on rate/reach/power metrics.
- **Where applicable**: High-bandwidth transport and DCI. Vendor talk, so expect the case studies to favor Cisco outcomes, but the component physics and metric trade-offs are general.

### Ethernet Evolution and Challenges in the world of AI - BRKNWT-2504

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271973129001zVr1)

Kapil Mehta (Cisco)

- **Why**: This is the lossless-fabric problem the PM works on daily — RDMA and elephant flows breaking Ethernet's assumptions in AI back-end networks — plus a read on where Ultra Ethernet Consortium standardization is actually heading.
- **What**: Ethernet's evolution history, its current failure modes under AI switching workloads (RDMA, elephant packet flows), Cisco's solutions, and the innovations being standardized by the Ultra Ethernet Consortium (from abstract only).
- **How**: Survey of the mechanisms being applied to congestion and losslessness at AI scale, positioned against UEC's standardization work items.
- **Where applicable**: AI back-end networks generally; the problem framing is industry-wide, but the "solutions" portion will be Cisco-flavored.

### How Cisco build AI readiness IP Backbone with 8000 Series - BRKMSI-3000

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963072001z05e)

Rob Piasecki (Cisco), Ruben Lopes da Fonte (Cisco)

- **Why**: Rare config-level treatment of lossless fabric mechanics — RoCEv2, PFC, ECN — including CLI verification, which is exactly the lossless-fabric internals the PM wants, not just architecture slideware.
- **What**: How Cisco builds AI infrastructure for webscalers: the requirements, the RoCEv2/PFC/ECN technology, detailed IOS-XR configuration, CLI verification that PFC and ECN are working, and design guidance (from abstract only — note the abstract itself is typo-laden, suggesting a hands-on rather than polished session).
- **How**: Step-by-step IOS-XR configuration of PFC and ECN with CLI validation, wrapped in design recommendations for AI-ready IP backbones.
- **Where applicable**: Platform-specific to Cisco 8000-series/IOS-XR, but the design principles (ECN threshold tuning, PFC behavior verification, lossless design patterns) transfer to any RoCEv2 fabric.

### Optimizing AI-Ready WAN Infrastructure with Microsoft and Cisco - CSSENT-2100

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1758668928353001AbVz)

Sarav Subramanian (Microsoft), Ruben Lopes da Fonte (Cisco), Gaisin Rustam (Microsoft)

- **Why**: An end-user case study from Microsoft on deploying RDMA in the Azure WAN — extending lossless-network practice beyond the DC into the WAN, which few operators talk about publicly.
- **What**: How AI-ready infrastructure is being built in the Azure WAN using RDMA for high throughput, low latency, and lossless transfer with minimal CPU load, and the congestion-management strategies (Priority Flow Control, ECN) used to handle oversubscription and microbursts (from abstract only).
- **How**: RDMA across WAN infrastructure with PFC/ECN congestion control for microburst and oversubscription scenarios.
- **Where applicable**: Microsoft Azure WAN-specific setup. Joint vendor-customer session, so expect some marketing gloss, but the scenario — lossless behavior at WAN scale — is unusually candid territory for Microsoft to discuss.

### Groq: An AI Success Story - Deploying High-Performance, and Low-Latency AI Networks Using Cisco Nexus 9000 - CSSDCN-2005

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879213001zkhz)

Swetha Velamuri (Cisco), Cameron Ferdinands (Groq)

- **Why**: A real customer (Groq) describing inference-network design — inference traffic has different characteristics from training (latency-critical, bursty, iterative) and public detail on inference fabrics is scarce.
- **What**: How Groq uses Nexus 9000/NX-OS to achieve scalability, bandwidth, low latency, and congestion management for AI inference, plus how Cisco optics choices reduce cost and energy (from abstract only — the abstract makes performance and cost claims without numbers; treat specifics as unverified until seen in the recording).
- **How**: Groq's software-first hardware approach paired with Nexus congestion management and optics innovations.
- **Where applicable**: Groq-specific inference deployments; success-story framing with a Cisco co-speaker, so expect a product-friendly narrative rather than a post-mortem.

### Cisco Nexus 9000 Architecture - BRKDCN-3939

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892827001zyLO)

Faraz Taifehesmatian (Cisco)

- **Why**: Switching silicon and forwarding internals are squarely in the PM's core interest; this is the deep-dive on the ASIC generation that underpins the AI-fabric sessions above.
- **What**: An in-depth architecture study of the latest Nexus 9000 modular and top-of-rack switches: ASIC architecture, forwarding mechanics, physical design elements, and the hardware-enabled features that deliver DC network services (from abstract only).
- **How**: Architecture walkthrough from silicon to system.
- **Where applicable**: Cisco-specific silicon, but the trade-offs discussed (buffering, forwarding pipeline, physical design) are transferable to evaluating any modern DC switch ASIC.

### VXLAN EVPN: A Deep Dive into Packet Forwarding - BRKDCN-3966

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271893016001zKXr)

Lukas Krattiger (Cisco)

- **Why**: "A day in the life of a packet" is exactly the datapath-internals treatment the PM values — most EVPN content covers control plane; this follows the data plane.
- **What**: How routing and bridging actually happen across a VXLAN EVPN fabric — what occurs from the ingress VTEP through to the egress VTEP and beyond, including how multi-destination traffic is handled (from abstract only).
- **How**: Step-by-step packet walk through the overlay, ingress to egress.
- **Where applicable**: The mechanics are general to VXLAN EVPN regardless of vendor; examples will be NX-OS-based.

### SONiC Architecture and Deployment Deep Dive - BRKMSI-2004

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967174001zlt7)

Jiri Chaloupka (Cisco)

- **Why**: SONiC is where open-source NOS momentum actually is, and a Cisco deep dive covering SONiC on their own Silicon One dataplane is a strong signal about where the disaggregation story is heading — including AI back-end networks as a deployment driver.
- **What**: Part one covers SONiC's OS architecture in detail with examples of SONiC running on Cisco Silicon One NPU/data plane; part two covers deployment examples and when SONiC should be considered, including AI frontend and back-end networks (from abstract only).
- **How**: Architecture decomposition of SONiC's componentized design, followed by deployment-decision guidance.
- **Where applicable**: SONiC on Cisco hardware specifically, but the architecture content and the "when to choose SONiC" framing apply to any disaggregated-NOS evaluation.

### Deployment of Micro-Segmentation in Cisco NX-OS VXLAN EVPN Fabrics with VXLAN Group Policy Option (GPO) - BRKDCN-2633

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271884455001zrLo)

Max Ardica (Cisco)

- **Why**: East-west segmentation enforced in the fabric itself — the intersection of the PM's network security and DC overlay interests — and grounded in an IETF draft rather than a purely proprietary mechanism.
- **What**: Micro-segmentation using security groups and security group ACLs in NX-OS VXLAN EVPN fabrics via VXLAN Group Policy Option (IETF draft-smith-vxlan-group-policy-05), covering the control- and data-plane components of the implementation and common use cases including service-chaining simplification (from abstract only).
- **How**: Group policy conveyed in the VXLAN header so per-application policy follows the workload anywhere in the fabric, replacing perimeter-centric inspection.
- **Where applicable**: NX-OS EVPN fabrics; the mechanism follows an IETF draft so the concept is portable, but the described implementation is Cisco-specific.

### Security superpowers with eBPF and Tetragon - BRKSEC-2167

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272001166001zXE7)

Liz Rice (Cisco)

- **Why**: Liz Rice is one of the leading voices in eBPF/Cilium, and Tetragon is the open-source enforcement engine underneath Cisco's Hypershield — this session reveals where a major vendor's security stack is actually being built, from a contributor rather than a marketer.
- **What**: A deep dive into Tetragon: YAML tracing policies mapped to eBPF programs attached to a variety of event types, multi-program "following" of a series of events to pinpoint likely-malicious behavior, and in-kernel event aggregation/filtering to minimize observability overhead (from abstract only).
- **How**: eBPF programs attached at kernel event points; policy-based correlation across event sequences; in-kernel aggregation and filtering to keep overhead low.
- **Where applicable**: Linux hosts and Kubernetes broadly — Tetragon is open source and vendor-neutral in applicability, while also being the substrate for Cisco's commercial Hypershield.

### The Swiss Army Knife of Cloud Native Networking - BRKCLD-1012

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845187001zhhH)

Raymond De Jong (Cisco)

- **Why**: Hits the PM's Cilium/BGP/IPAM interests directly — BGP from Cilium and LB IPAM for multi-tenant pools are the operational pieces most teams hit in production.
- **What**: Cilium's advanced features — BGP, load balancing, LB IPAM, and network policies — for multi-cloud and multi-tenancy networking, including routing/connectivity between Kubernetes clusters and external networks, BGP setup across different topologies, and multi-tenant routing with multiple IP pools for LoadBalancer IP assignment (from abstract only).
- **How**: eBPF datapath (Cilium) with a BGP control plane for external reachability, and LB IPAM pools giving platform engineers per-tenant LB IP allocation.
- **Where applicable**: General Cilium/Kubernetes environments; mechanisms are open source even though the speaker is Cisco.

### Are You Prepared for the Next Typhoon? - BRKSEC-2499

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272003117001zp8C)

Paul Giralt (Cisco), Steve Nowell (Cisco)

- **Why**: Salt Typhoon is the defining nation-state compromise of network infrastructure in this era, and this session combines Talos threat insight with concrete hardening guidance plus Cisco's "secure by default" roadmap — with an explicit feedback opportunity on that roadmap.
- **What**: The nature of the 2024 Salt Typhoon intrusions across multi-vendor infrastructure at major telecoms as understood by Talos, specific hardening steps available today, and planned future "secure by default" enhancements to network infrastructure (from abstract only).
- **How**: Attack-surface analysis followed by hardening best practices and defensive-design changes.
- **Where applicable**: Broadly applicable to network infrastructure security; telecom operators are the most-affected vertical, but the hardening lessons apply to any operator of carrier or enterprise network gear.

### Innovative Authentication: Beyond Passwords - BRKSEC-2584

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272010780001zHEa)

Stefan Duernberger (Cisco)

- **Why**: Directly the identity stack the PM tracks — passkeys, OAuth 2.0/OIDC — plus two genuinely emerging items (Google's Device-Bound Session Credentials and Shared Signals and Events) that sit beyond the basics.
- **What**: The role and implementation of passkeys, OAuth 2.0 and OIDC for cross-platform authentication, Google DBSC, Cisco Duo Passport, and an overview of Shared Signals and Events — all framed within a Zero Trust architecture (from abstract only).
- **How**: Protocol survey connecting credential technology (passkeys/WebAuthn) to authorization frameworks (OAuth/OIDC) to session-integrity (DBSC) and continuous-signal (SSSE) mechanisms.
- **Where applicable**: General web and enterprise authentication; the Duo Passport portion is Cisco product content, but the protocol material is standards-based and general.

### Deep Dive into Cisco's Use of QUIC, MASQUE and OS Native Capabilities to Deliver Frictionless Zero Trust Access - BRKSEC-3027

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272012757001zOOu)

Vinny Parla (Cisco)

- **Why**: Shows where identity and transport converge: MASQUE/QUIC-based access proxied through OS-native clients from Apple, Google, and Samsung, with WebAuthn and passkeys in the loop — a credible picture of how frictionless ZTNA gets to Wi-Fi-level ubiquity.
- **What**: How industry-standard protocols (MASQUE, QUIC, WebAuthn, passkeys, private 5G) can deliver Zero Trust Access with minimal user/admin friction; how native OS clients from Apple and Samsung and the Cisco Zero Trust Access module in Cisco Secure Client leverage MASQUE and QUIC for a seamless experience (from abstract only).
- **How**: MASQUE-style proxying over QUIC tunnels integrated with OS-native network clients and passkey-based user identity.
- **Where applicable**: Enterprise and consumer device access; heavily ecosystem-dependent (collaboration with Apple, Google, Samsung), so the OS-client pieces are platform-specific while the protocol layer is standard.

## Adjacent

### Impact of AI Traffic in Transport Networks - BRKSPG-1180

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963873001z5j7)

Virginia Teixeira (Cisco)

- **Why**: Near-core for anyone responsible for DC/WAN interconnect: AI traffic patterns (RAG, grounding, agents, edge distribution) change DCI and WAN dimensioning assumptions in ways transport teams haven't absorbed yet.
- **What**: An analysis of AI traffic characteristics across a set of AI use cases and their impact on WAN and DCI design requirements (from abstract only).
- **How**: Traffic-pattern characterization mapped onto transport network design levers.
- **Where applicable**: Service-provider and large-enterprise transport. The speaker's own framing is honest that AI deployment models are still settling, so expect early directional analysis rather than settled engineering rules.

### Multi-Tier Fabrics: Network Designs for the Modern Data Center - BRKDCN-2999

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892264001zRcH)

Marina Ferreira (Cisco)

- **Why**: The back half of this session is genuinely relevant physical-DC content — super-spine and hyperscale plane designs, where 400G/800G is cost-effective, fixed vs. modular trade-offs, and routed fabrics for cloud-native applications. The front half is Clos 101, which the PM doesn't need; hence adjacent rather than core.
- **What**: Fat-tree, Clos, and leaf/spine foundations extended to super-spine and hyperscale plane designs, cost-effective use of 400G/800G, fixed-vs-modular switch decisions, and a review of self-organized routed fabrics for cloud-native applications (from abstract only).
- **How**: Design-pattern survey with cost/scale reasoning.
- **Where applicable**: General data center design, vendor-neutral in principle; the routed-fabric segment connects to the same IP-underlay-for-cloud trend the PM sees in Kubernetes environments.

### Connecting Your Data to LLMs: Identity, Functions and Agents are all you Need - BRKETI-2411

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271915660001znU9)

Guillaume De Saint Marc (Cisco)

- **Why**: Agentic identity is one of the PM's explicit interests and almost absent from vendor programs — this is the closest hit: per-request authorization deciding which data an agent may fetch and serve.
- **What**: Architectures and tools for connecting enterprise data (including on-prem) to LLMs without data migration, including real-time prompt inspection to identify the data required by a request, determine whether the user has rightful access, and serve only authorized data (from abstract only).
- **How**: Prompt-time authorization — mapping an incoming prompt to data requirements and checking entitlements before data is served to the model.
- **Where applicable**: Enterprise GenAI deployments; Cisco brings product positioning, but the underlying pattern — entitlement-aware data serving for agent requests — is broadly relevant to anyone designing agentic identity.

### EVPN Fabric in the Real World: Securing Critical Infrastructure in Finance and Aviation - BRKENS-2655

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271921837001zgvo)

Daniel Cantor (Fiserv), Ekta Ghosh (Adani Airports Holding Limited), Rahul Kachalia (Cisco)

- **Why**: Two real end users (Fiserv, Adani Airports) discussing EVPN-fabric modernization under regulatory pressure. Worth a look for the case-study value, but the abstract is executive-framed ("high-impact executive session") and offers no metrics, failure discussion, or technical depth — approach with skepticism.
- **What**: How Fiserv and Adani Airports used Catalyst networking and EVPN fabric as the foundation for automated, always-on infrastructure, with claimed reductions in downtime and improved security posture (from abstract only — no numbers in the abstract; verify specifics in the recording).
- **How**: Executive discussion/Q&A format per the abstract.
- **Where applicable**: Regulated enterprise environments (financial services, aviation/airports); campus and DC-edge scale rather than hyperscale.

## Wildcard

### Packet Buddy - Chatting with your PCAPs, via the Cloud or Locally on Your Own Machine! - AIHUB-2000

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271926126001z8AP)

Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco)

- **Why**: LLM-assisted packet analysis is a genuinely new tool category, and the PM lives in PCAPs — this is the kind of thing worth knowing exists before it lands in a commercial product.
- **What**: An open-source solution ("PACKET BUDDY") that lets you chat with your own Wireshark captures via a choice of LLMs — asking what traffic is present, what errors it sees, and getting help understanding packets and flows — deployable via cloud or locally on your own machine (from abstract only).
- **How**: PCAP ingestion fed to an LLM with conversational querying; the local deployment option is the privacy-relevant detail.
- **Where applicable**: Any environment; open source, with the obvious caveat that feeding captures to cloud LLMs has data-exposure implications — the local mode matters.

### Packets in Space: Networking for the Final Frontier - CISCOU-1057

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271840075001zf1I)

Lexie Cooper (Blue Origin), Eric Peterson (Blue Origin), Patrick Garggan (Cisco)

- **Why**: Designing networks where failure is not an option and latency requirements are extreme forces first-principles thinking that is useful calibration for anyone building "critical" terrestrial infrastructure.
- **What**: A moderated Q&A with Blue Origin "rocket network engineers" on designing mission-critical networks for rockets and spacecraft — real-time telemetry, low-latency requirements, and extreme environmental conditions (from abstract only — note the program abstract is truncated mid-sentence, so the full scope of the session is unclear from the text alone).
- **How**: Q&A format rather than a prepared technical talk.
- **Where applicable**: Aerospace-specific, but the deterministic, failure-intolerant design lessons generalize to any network with hard availability and timing requirements.

### An Introduction to Quantum Mechanics, Computing, and Networking - BRKETI-1401

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271916244001zYZ1)

Tim Szigeti (Cisco)

- **Why**: Cisco is making a serious R&D bet on quantum networking, and this is the clearest signal in the program of where the long-horizon network and security landscape may move (distributed quantum computing, entanglement-based secure communications, clock sync).
- **What**: An introduction to quantum mechanics focused on qubits and their special properties — superposition, entanglement, no-cloning, including mathematical proofs — an overview of quantum computing's impact on network communications and security, and the building blocks, opportunities, and challenges of quantum networks, plus Cisco's current work (from abstract only).
- **How**: Tutorial format; foundational science first, then networking implications.
- **Where applicable**: Nothing here is deployable today — it is forward-looking R&D context, useful for spotting the trajectory rather than near-term engineering.

## Themes

- **AI fabrics are the gravitational center of the entire program.** Optics, Ethernet standards, switch ASICs, IOS-XR configuration, WAN design, and even coherent transport are all being reframed around AI training/inference traffic. The lossless-Ethernet problem (RoCEv2, PFC/ECN, microbursts, elephant flows) and the Ultra Ethernet Consortium's standardization work are the technical through-line — and notably, the lossless conversation has moved from the DC back-end into the WAN (Microsoft's Azure RDMA session).
- **Optics is now a first-class systems constraint.** 800G/1.6T pluggables, breakout economics, 800 Gb/s and 1.6 Tb/s Ethernet standardization, and early co-packaged optics show the industry treating the optical module — its power, reach, and form factor — as a determinant of fabric topology rather than a pluggable afterthought.
- **eBPF has crossed from OSS novelty to vendor substrate.** Liz Rice presenting Tetragon at Cisco Live, Tetragon powering Hypershield, and a full session on Cilium BGP/LB IPAM indicate that eBPF-based networking and security is now the foundation of a major vendor's cloud-native and security strategy — a meaningful trajectory signal for the ecosystem.
- **Identity is converging on session-bound credentials and continuous signals.** Passkeys/WebAuthn, OAuth/OIDC, Google's Device-Bound Session Credentials, Shared Signals and Events, and MASQUE/QUIC-based zero trust collectively point away from one-time login events toward continuous, protocol-level session integrity — with agentic/LLM data-access authorization just beginning to appear at the edge of the program.
- **Nation-state infrastructure threat is driving a "secure by default" agenda.** Salt Typhoon gets a full session combining Talos threat detail, concrete hardening steps, and a vendor roadmap for secure-by-default network devices — network device security is being treated as a lifecycle discipline, not a hardening checklist.
- **Open NOS momentum keeps building.** A SONiC architecture deep dive on Cisco's own Silicon One dataplane — with AI back-end networks named as a key deployment driver — shows even incumbent vendors treating disaggregated operating systems as a primary path, not an experiment.
