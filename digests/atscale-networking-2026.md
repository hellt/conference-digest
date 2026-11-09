<!--
conference: @Scale: Networking 2026
source_url: https://atscaleconference.com/events/networking-2026/
generated: 2026-11-09
registry_key: atscale-networking-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# @Scale: Networking 2026

A single-day program (August 25, 2026, Santa Clara) almost entirely organized around one question: how to build, transport, and physically deliver networks for frontier-scale AI training. No papers or slide decks were published with the program, and the conference page adds nothing substantive beyond the abstracts, so every write-up below is based on abstract text only (marked per item); the Meta keynote and the MetaRoCE group Q&A have no published abstracts and are not assessed. Of the four AI-agent lightning talks, *AI-Native Network Capacity Management* (Mohab Gawish, Meta) substantially overlaps *The Plan That Learns* and is covered in passing rather than as a separate pick.

## Core

### Resilient AI Supercomputer Networking using MRC and SRv6

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-18)

Jitendra Padhye (OpenAI)

- **Why**: Tail latency — not average throughput — is what stalls synchronous pretraining at frontier scale, and one colliding flow or one failed link can throttle a job of tens of thousands of accelerators. This is OpenAI's production answer, and it is a transport-plus-routing co-design rather than a tweak to either.
- **What**: MRC, a new RDMA-based transport that sprays across many paths and actively load-balances between them, eliminating flow collisions; paired with static SRv6 source routing that lets the transport bypass failures on its own. Run in production at OpenAI to train frontier models, where MRC lets training jobs ride out network failures that previously would have interrupted the run. (The abstract calls this a three-pronged approach but enumerates only two prongs; the third is not specified in the program text.) (from abstract only)
- **How**: Path spraying removes the ECMP flow-collision problem by not pinning flows to single paths; active load balancing keeps utilization even as paths churn. SRv6 segment lists encode the path, so on failure the endpoints — not the routing protocol — select alternates: failover without reconvergence.
- **Where applicable**: OpenAI's production training clusters, org-specific at extreme scale. The pattern (spray plus endpoint-controlled, source-routed failover over richly connected Ethernet) is broadly transferable, but it presumes a multipath topology and an SRv6-capable fabric.

### MetaRoCE: Meta's RDMA Transport

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-19)

Arvind Srinivasan (Meta), Kingshuk Mandal (Keysight Technologies)

- **Why**: Meta redesigned RDMA from scratch for clusters growing past a million accelerators, and its core bet — accept lossy Ethernet, push all transport intelligence into the NIC, decouple from topology — is the same architectural direction other frontier operators are taking. This is the overview talk: mechanisms, the topology it enables, and the standards push.
- **What**: MetaRoCE is a clean-sheet, multipath, out-of-order, receiver-driven RDMA transport that treats Ethernet as inherently lossy and pushes all intelligence into the NIC. Decoupling transport from topology is what makes TCO-optimized multiplane FPF topologies viable on commodity Ethernet with frictionless application adoption. A conformance suite developed with Keysight validates implementations from software reference through hardware emulation to production silicon, and Meta is opening MetaRoCE to the industry as a candidate ubiquitous RDMA transport for AI-scale networks. (from abstract only)
- **How**: NIC-resident intelligence with receiver-driven operation and out-of-order delivery, so the transport survives loss and reordering without requiring a lossless fabric underneath; multipath operation replaces fabric-wide coordination. The conformance suite is the mechanism for multi-vendor interoperability.
- **Where applicable**: Meta's accelerator clusters (million-scale, multi-region) and its multiplane FPF fabric plans — org-specific scale, but explicitly positioned for industry-wide adoption; the Keysight conformance chain signals serious intent for portability across NIC and silicon vendors.

### MetaRoCE: From Spec to NIC to Open Source

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-21)

Sandeep Nagaraja (Meta), Balakrishnan Raman (AMD)

- **Why**: The companion deep-dive with the evidence: real-world performance results across multiplane topologies, tail latency, and long-distance RDMA, plus the open-source release (specification, reference implementation, compliance suites) at OCP. For anyone deciding whether MetaRoCE matters beyond Meta, this is the talk with numbers.
- **What**: MetaRoCE's journey from specification to silicon: a reference software implementation on AMD programmable NICs, demonstrated scaling out within a cluster and scaling across fabrics for diverse deployment needs. Performance results span multiplane FPF topologies, tail-latency optimization, and long-distance RDMA. First look at Meta's open-source release of the specification, reference implementation, and compliance suites at OCP. (from abstract only)
- **How**: Reference software implementation on AMD programmable NIC hardware; the scaling and performance claims are demonstrated on that stack rather than only asserted.
- **Where applicable**: The reference implementation is tied to AMD programmable NIC silicon — an implementation constraint, not a protocol one — and the performance results come from Meta's multiplane FPF deployment context. The open spec and compliance suites are aimed at portable adoption by others.

### Virgo: scale-out data center network for AI

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-40)

Jeongkeun "JK" Lee (Google)

- **Why**: Google splitting AI east-west traffic onto a purpose-built fabric — separate from Jupiter, which is retained for north-south — is a major architectural datapoint. Virgo will carry production ML traffic for Google Cloud's A5x bare-metal instances (NVIDIA Vera Rubin NVL72) and is a building block for next-gen TPUs, so its design choices will be exercised at frontier scale.
- **What**: Virgo, a dedicated accelerator-to-accelerator east-west fabric optimized for massive horizontal scale, engineered for deterministic latency and maximum resilience to deliver high goodput for ML workloads. Design principles: resilience, observability, deployability, and multi-building scale. (from abstract only)
- **How**: Optimized for the traffic shape of ML workloads (tightly coupled horizontal collectives) rather than general datacenter traffic; deterministic latency and resilience are stated design goals, but the mechanisms are not detailed in the abstract.
- **Where applicable**: Google production and Google Cloud A5x instances; multi-building scale implies campus-scale cross-building connectivity. Google-specific build, but the split of "dedicated AI scale-out fabric beside the general-purpose fabric" mirrors choices at Meta and OpenAI and is an industry-direction signal.

### Fiber Networks Innovations for AI at Scale

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-39) · [Materials](https://atscaleconference.com/building-the-backbone-of-ai-inside-the-nao-mega-clusters-fiber-revolution/)

Fabrice Ouandji (Meta), Sebastian Gault (Meta)

- **Why**: Once transports and fabrics are sorted, the binding constraint for mega clusters is the physical fiber plant: exploding fiber counts, demand landing in unpredictable places, and compressed delivery timelines. This is the physical-layer heart of the program — the PM's cabling and fiber-plant territory — and the conference site pairs it with a featured article on the NAO mega cluster's fiber build.
- **What**: The connectivity challenge created by Prometheus: significantly higher fiber count requirements, highly dynamic demand location, and compressed delivery timelines, and the innovations required to meet that demand across multiple data centers in the cluster. (from abstract only)
- **How**: Not specified in the abstract — the talk covers the fiber-plant and delivery innovations themselves; no mechanism detail is available from the program.
- **Where applicable**: Meta's Prometheus/NAO mega-cluster build — org-specific scale and timelines, but the problem (fiber-count explosion plus unpredictable demand placement across a multi-building campus) is universal for anyone building AI campuses.

### Physical Network Design at Scale + 3 min Q&A

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-36) · [Materials](https://atscaleconference.com/physical-network-design-at-scale/)

Richard Cziva (Meta), Brandon Premo (Meta)

- **Why**: Physical network design — placing thousands of devices and planning millions of fibers under failure-domain constraints — has been stubbornly manual, and AI demand makes that manual process the bottleneck. Loom is a concrete, deployed system that compressed end-to-end design from months to hours. Squarely in the PM's physical-datacenter plus automation interests.
- **What**: Loom, Meta's system for automating the end-to-end physical network design pipeline, orchestrating two components: Planogram, which places network devices across the physical floorplan subject to dimensional and failure-domain constraints, and a fiber design component that generates end-to-end fiber connectivity across the variety of connectivity patterns driven by physical constraints. Together they cut design time from months to hours and produce more complex, more efficient designs with fewer resources. (from abstract only)
- **How**: Constraint-based device placement plus automated fiber connectivity generation, orchestrated as a pipeline — cleanly decomposing "where devices go" from "how everything gets cabled."
- **Where applicable**: Built against Meta's floorplans, fabric families, and failure-domain rules — the constraints are Meta-specific — but the decomposition (constrained placement plus automated fiber path design) transfers to any large operator and is a strong candidate pattern for vendor tooling roadmaps.

### Co-Designing Communication for AI Accelerators

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-41)

Rajeev Nair (Meta), Wes Bland (Meta)

- **Why**: MTIA 300 treats communication as a first-class architectural citizen — dedicated message engines — and introduces "network fungibility," where the same NIC hardware flexes between scale-up and scale-out roles. That flexibility is a genuinely different point in the accelerator interconnect design space, relevant both to AI networking and to how non-GPU accelerators change fabric requirements.
- **What**: The communications architecture of MTIA 300, Meta's custom AI training and inference accelerator: dedicated message engines offload communication workloads, decoupling communication from the primary compute grid, minimizing resource contention and raising both compute and network efficiency. "Network fungibility" lets the same NICs adapt to scale-up or scale-out configurations depending on production needs, within a tight co-design loop across hardware, software, and models. (from abstract only)
- **How**: Communication offload into dedicated engines rather than shared-resource handling on the compute grid; NIC role flexibility instead of parts hard-partitioned into scale-up-only or scale-out-only.
- **Where applicable**: Meta's MTIA custom silicon — the specific implementation is Meta-specific, but the principles (offload communication from the compute grid; don't hard-partition NICs by role) transfer to any accelerator program, and the scale-up/scale-out fungibility question is live for GPU fleets too.

### Building scalable AI cloud interconnects with SRv6 + 3 min Q&A

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-37)

Alexey Gorovoy (Nebius)

- **Why**: AI-cloud tenants need predictable bandwidth into their virtual networks and services that behave identically from the virtual edge out to the WAN. Nebius' answer — SRv6 as the single architectural building block across both domains — removes the protocol-translation seam that plagues multi-domain interconnects. Directly relevant to the PM's cloud, interconnect, and segment-routing interests.
- **What**: Nebius' evolving architecture for customer cloud interconnects: SRv6 bridges the virtual cloud environment with the physical network edge, enabling end-to-end VPN and traffic-engineering services without protocol translation between datacenter and WAN domains, with latest implementation experience shared. (from abstract only)
- **How**: SRv6 network programming — segment-encoded service instructions — applied uniformly from the cloud edge across datacenter and WAN, so one forwarding architecture carries customer VPNs and traffic engineering end to end instead of stitching per-domain protocols.
- **Where applicable**: Nebius' AI cloud — a single-operator, SRv6-capable fabric is required end to end, so it is operator-specific. The unifying pattern (one overlay architecture across domains instead of DC/WAN protocol stitching) applies to any provider or large enterprise building multi-domain interconnects.

### Lightning Talk - The Plan That Learns

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-31)

Ben Vallis (Meta)

- **Why**: Capacity planning is where years-ahead commitments meet guaranteed-wrong forecasts, and this talk applies agents not to forecast accuracy but to decision quality under uncertainty — positioning capacity to keep options open — which is a more defensible use of ML than "better predictions." Core to the PM's ML-for-infrastructure-operations interest.
- **What**: Agents applied to the judgment-heavy decisions that stayed manual: acting inside narrow buy windows (continuous signal triage surfacing the handful of truly novel sites, weeks down to minutes); trusting data across systems that disagree on basic definitions (a measure-enrich-regrade loop); and choosing among coupled, timing-sensitive levers (a ranked, costed menu of moves with the reasoning attached). The stated frontier: agents that remember every decision and its outcome, so judgment compounds instead of resetting with each planner. (from abstract only)
- **How**: Agentic triage over continuous signal streams, a cross-system data-trust reconciliation loop, and decision memory — explicitly framed as buying optionality under wrong forecasts, not improving the forecast.
- **Where applicable**: Meta's capacity planning (years-ahead commitments, correlated demand shocks) — org-specific context and lightning-talk-stage maturity, but the optionality framing and decision-memory idea transfer to any large operator. The companion talk *AI-Native Network Capacity Management* covers the same lifecycle pipeline stage-by-stage with agents as first-class participants.

### Lightning Talk - AI4NI @Runtime

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-34)

YuLing Chen (Meta)

- **Why**: Most AI-for-networking content in this program targets planning and design time; this is the runtime side — agents embedded in live operations for reliability, performance, and efficiency, with production trials behind it. That is the closest thing to deployable ML-for-networking evidence in the program.
- **What**: AI4NI @Runtime: AI agents across three dimensions — reliability, performance, and efficiency — with the solution architecture, example agentic systems, initial findings from production trials, and the key technical challenges and planned directions. (from abstract only)
- **How**: Agent architecture embedded in runtime operations; the mechanisms are not detailed in the abstract, but production trials are cited as the evidence base.
- **Where applicable**: Meta's production network serving billions of users; early-stage, org-specific results — the value is the architecture and the honest challenge list, not yet-transferable outcomes.

## Adjacent

### Anatomy of @scale Machine Learning Network Operations

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-20)

Jim Julson (Coreweave)

- **Why**: Operating — not just designing — ML networks is where transferable lessons live, and Coreweave runs GPU infrastructure at AI-cloud scale. Caveat: the published abstract is contentless ("a journey through the operational challenges and nuances"), so substance cannot be assessed from the program; included for topic relevance and speaker position.
- **What**: The operational challenges and nuances of machine learning and AI infrastructure networks at Coreweave — no specifics beyond that framing are available. (from abstract only)
- **How**: Not described in the abstract.
- **Where applicable**: Coreweave's GPU cloud — expect operator-specific experience. Worth attending for potential postmortem and operational content, but nothing in the program substantiates it yet; judge from the recording.

### Live Panel: Scale-Out Networking for AI Supercomputers

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-29)

Rajiv Krishnamurthy (Meta), Joseph Provine (Meta), Andrew Dickinson (Oracle), Jim Julson (Coreweave), Jitendra Padhye (OpenAI)

- **Why**: The architects behind this cycle's individual talks (MetaRoCE, MRC) plus Oracle and Coreweave in one room, comparing topology choices, congestion control at extreme scale, and network/training-framework co-design — useful as the cross-operator synthesis of the Core talks.
- **What**: Practitioner panel on connecting tens of thousands of accelerators into a single tightly coupled fabric: architectures, transport protocols, and operational lessons behind supercomputer-scale AI training networks. (from abstract only)
- **How**: Live discussion, not a presented technique.
- **Where applicable**: Frontier-lab and hyperscaler scale; expect org-specific positions. The value is comparative — where the panelists' approaches converge (multipath, endpoint intelligence) and where they genuinely disagree — rather than new techniques.

### Lightning Talk - 10x Network Design Engineer

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-32)

Maaz Mohiuddin (Meta)

- **Why**: Pairs with Loom (Core): where Loom automates physical design as a constraint system, this talk is about agents owning design judgment end-to-end, and it is candid about what still fails — validation above all. The "engineer as author-to-approver" framing is where design automation is heading industry-wide.
- **What**: Agent-assisted steps in datacenter network design today — sizing a fabric, proposing a topology, analyzing a change — with the trajectory toward a single agent owning design end-to-end, real waypoints from Meta's fabrics, what already works, and where the hard problems remain (validation, above all). Humans still make the call; they no longer draw every line. (from abstract only)
- **How**: Agents assist discrete steps within the design pipeline with human approval gates; the mechanism detail is not in the abstract.
- **Where applicable**: Meta's fabrics — org-specific waypoints. The author-to-approver shift and the validation bottleneck are general to any design-automation effort, which is why this earns a slot despite overlapping Loom.

## Wildcard

### Live Panel: Building at the Roofline — Planning and Delivering Gigawatt-Scale AI Infrastructure

**Links:** [Abstract](https://atscaleconference.com/events/networking-2026/#agenda-item-42)

Omar Baldonado (Meta), Amrita Kenue (Meta), Lucas Benson (Microsoft), Nikita Parikh (Google)

- **Why**: Not a networking session — power, buildings, fiber, and accelerators sourced at the edge of what the supply ecosystem can deliver — but it defines the envelope every network design in this program lives inside: rack power, building capacity, multi-generation fleets, and component lead times bound what fabrics can even be built. The panel composition makes it concrete: per the conference page, the Microsoft panelist leads strategic sourcing for optics and switches supporting Azure's AI fleet, and the Google panelist is a next-generation networking sourcing lead — this is the layer above the network roadmap.
- **What**: Panel with infrastructure planning and technical sourcing leaders from Google, Meta, and Microsoft on long-range fleet strategy across multiple technology generations, multi-vendor orchestration, and the engineering realities of delivering AI infrastructure at gigawatt scale at the roofline of industry capacity.
- **How**: Live discussion, not a presented technique.
- **Where applicable**: Hyperscaler fleets, but the constraints discussed — power, lead times, multi-generation estates — are industry-wide. Any roadmap that assumes unconstrained optics, switch, or fiber supply should watch this.

## Themes

- **The scale-out AI fabric is now its own network class.** Google's Virgo (dedicated east-west accelerator fabric beside Jupiter), Meta's MetaRoCE-plus-multiplane-FPF, and OpenAI's MRC all encode the same split: general-purpose datacenter networking and accelerator scale-out networking are designed separately, with different latency, resilience, and goodput requirements.
- **Transport intelligence is moving to the endpoint.** MRC and MetaRoCE both treat the fabric as commodity, inherently lossy Ethernet and push multipath, out-of-order, actively load-balanced behavior into the NIC/endpoints — a decisive move away from lossless-fabric-era RDMA assumptions.
- **Static source routing is the resilience and unification mechanism of choice.** OpenAI pairs MRC with static SRv6 so the transport bypasses failures without waiting for reconvergence; Nebius uses SRv6 as one building block across DC and WAN. Endpoint-controlled path selection looks like a recurring pattern.
- **The AI transport is becoming an open standards battleground.** Meta is releasing the MetaRoCE specification, a reference implementation on AMD NICs, and a Keysight-built conformance suite at OCP, explicitly aiming for it to become the ubiquitous RDMA transport for AI-scale networks — the obvious comparison point for anyone tracking the Ultra Ethernet space.
- **The physical plant is the scaling constraint, and it is getting automated.** Fiber counts, demand placement, and delivery timelines for mega clusters (NAO/Prometheus) are the hard problems, and Loom (constrained placement plus automated fiber design, months to hours) shows the automation response; MTIA 300 shows the same pressure pushing communication into accelerator silicon.
- **AI agents are entering the network lifecycle end-to-end.** Four lightning talks cover agents in capacity planning, the capacity pipeline, physical design, and runtime operations — early results and Meta-internal today, but a collective bet that the next automation frontier in networking is agentic, with validation named as the open hard problem.
