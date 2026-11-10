<!--
conference: ONE Summit 2024
source_url: https://onesummit2024.sched.com/list/descriptions/
generated: 2026-11-10
registry_key: onesummit-2024
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ONE Summit 2024

*Note: the conference site (sched.com) rejected automated retrieval of all session pages, so every write-up below is based on the abstract as printed in the program text — each is marked accordingly. ONE Summit is Linux Foundation Networking's operator/telco-heavy event, so the program skews toward O-RAN, 5G, and Nephio; the picks below are the sessions that genuinely touch the PM's core interests in datacenter fabric, cloud/Kubernetes infrastructure, and AI systems.*

## Core

### SONiC BGP Loading Optimization - Joy Qin & Eddie Ruan, Alibaba Cloud

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUss/sonic-bgp-loading-optimization-joy-qin-eddie-ruan-alibaba-cloud) · [Recording](https://www.youtube.com/watch?v=umt2XTQQx80)

Joy Qin, Software Engineer, and Eddie Ruan, Alibaba Cloud

- **Why**: Control-plane convergence time is a real production constraint in large SONiC fabrics — loading tens of thousands of BGP routes through SONiC's Redis-based internal state path is a known bottleneck. This is production engineering from a hyperscaler, not a benchmark exercise.
- **What**: Alibaba's work to double SONiC's route-loading throughput: a batch-publish feature that cuts FPMSyncD Redis traffic, a redesigned Redis pipeline flush policy, and a restructuring of Orchagent and Syncd around a singleton templated ring buffer with lambda-based offload of the module main thread. (from abstract only)
- **How**: Attacks the problem at three layers — reduce per-route Redis messages (batching), avoid needless pipeline flushes, and restructure the long-running SONiC daemons so their main threads can offload work generically via a ring-buffer + lambda pattern.
- **Where applicable**: SONiC NOS deployments specifically; the daemon-restructuring pattern (ring buffer + lambda offload) is a general technique for any single-threaded state-sync daemon. Alibaba-specific engineering, but on an open, widely deployed codebase.

### Non-Minimal Path Routing for AI and Cloud Computation Networks - David Wong, Claruspon Systems, Inc.

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrl/non-minimal-path-routing-for-ai-and-cloud-computation-networks-david-wong-claruspon-systems-inc) · [Recording](https://www.youtube.com/watch?v=duKmDlJUB1s)

David Wong, Founder & CEO, Claruspon Systems, Inc.

- **Why**: AI clusters are already straining single-datacenter limits (power, scale), and the field is actively debating Clos vs. Dragonfly/Dragonfly+ with non-minimal path routing for million-GPU-scale fabrics. This is exactly the topology/routing design space the PM works in.
- **What**: An analysis of Clos vs. mesh/Dragonfly topologies through a path-diversity/congestion model, a review of recent non-minimal-path-routing proposals (2023, Dragonfly/Dragonfly+) and of AI-workload topology findings (e.g., Meta/MIT), plus tentative designs for large-scale AI networks targeting low latency, low congestion, zero loss, and high bisection bandwidth. (from abstract only)
- **How**: Models path diversity as the congestion lever, examines how non-minimal routing interacts with (e)BGP as the fabric protocol, and applies those findings to propose Dragonfly/Dragonfly+ variants suited to multi-datacenter AI resource aggregation (driven by per-site power limits).
- **Where applicable**: Design-stage guidance for AI/cloud fabric architects; explicitly multi-DC-spanning AI clusters. Vendor (single-founder company) perspective with patents in this space — treat the proposals as analysis-informed design sketches rather than validated deployments.

### ALPINE - SONiC Switchstack Simulation - Sonika Jindal & Bhagat Janarthanan, Google

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUs0/alpine-sonic-switchstack-simulation-sonika-jindal-bhagat-janarthanan-google) · [Recording](https://www.youtube.com/watch?v=_ueChYi1W7U)

Sonika Jindal and Bhagat Janarthanan, Software Engineers, Google

- **Why**: Pre-production fabric testing at scale is expensive; Google open-sourcing a Kubernetes-based way to spin up 100+ virtual SONiC switches in near-production topologies is directly useful to anyone running SONiC and CI/CD for network change validation.
- **What**: Alpine, a framework for instantiating virtual SONiC switches and deploying arbitrary topologies, able to build fabrics of more than 100 virtual switches spread across multiple K8s worker nodes, with lifecycle, provisioning, and initial config handled via Kubernetes. Intended for low-cost pre-submit CI test results. (from abstract only)
- **How**: Each virtual SONiC switch runs as a containerized workload; Kubernetes manages provisioning, config, and inter-switch connectivity, so full fabrics can be stood up in CI rather than on lab hardware.
- **Where applicable**: SONiC-based networks and NOS vendors wanting cheap large-scale pre-deploy testing; general technique (containerized NOS-in-K8s for fabric simulation) transfers to any NOS with a virtual-switch image. Google-contributed and open, which adds weight.

### P4-Based Automated Reasoning - Steffen Smolka, Google

**Links:** [Abstract](https://onesummit2024.sched.com/event/1aZuC/p4-based-automated-reasoning-steffen-smolka-google) · [Recording](https://www.youtube.com/watch?v=HqsxWUt8hhY)

Steffen Smolka, Staff Software Engineer, Google (leads the P4-Based Automated Reasoning group)

- **Why**: Using P4 not to program the pipeline but as a *vendor-agnostic, machine-readable specification* that switches are automatically validated against is a genuinely different use of P4 — it addresses switch qualification and multi-vendor SDN interoperability, two chronic pains for anyone operating heterogeneous fabrics.
- **What**: Google's practice of writing P4 specs for switch pipelines (programmable or not) and building tools that (1) run high-coverage automated validation of switch behavior against the spec, and (2) let the SDN controller hold switches from different vendors accountable to the same unambiguous spec, with reported gains in reliability and development velocity. (from abstract only)
- **How**: The P4 program becomes the contract; automated reasoning tools check conformance of actual switch forwarding behavior, and the controller's interaction with each vendor's silicon is mediated by the shared machine-readable spec.
- **Where applicable**: Any multi-vendor switch fleet with an SDN controller — hyperscaler-flavored, but the spec-as-contract technique is broadly adoptable and independent of particular silicon. Attested as running at Google, but the talk abstract does not quantify coverage or results.

### How Open Programmable Infrastructure (OPI) Improves Portability of Cloud & Data Center Applications - Paul Pindell, F5

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrN/how-open-programmable-infrastructure-opi-improves-portability-of-cloud-data-center-applications-paul-pindell-f5) · [Recording](https://www.youtube.com/watch?v=TtMsnVS_L4U)

Paul Pindell, Principal Architect, F5 Networks

- **Why**: DPUs/IPUs are becoming standard in cloud and DC servers, but each vendor's provisioning and management story differs — OPI is the main open effort to standardize them, and this retrospective covers a working end-to-end demo plus the obstacles hit along the way.
- **What**: OPI's end-to-end demo: zero-touch provisioning of a DPU/IPU card using the project's adopted sZTP framework, installing an OS/container platform on the card, and running an infrastructure workload (Nginx proxy) with traffic proxied through the DPU without ever touching the host. Includes a retrospective on challenges and solutions. (from abstract only)
- **How**: Secure ZTP provisions the card; a container platform is installed on the DPU itself; the offload workload runs on-card so host CPU/OS never see the proxied traffic — the "DPU as independent server" model.
- **Where applicable**: Anyone deploying DPUs/IPUs in servers and wanting vendor-neutral provisioning and workload portability. Vendor (F5) presented, but on a Linux Foundation project with an open demo, which tempers the pitch factor.

### Introduction to Photonic Disaggregated Computing Architecture - Shigeru Kotabe, Fujitsu

**Links:** [Abstract](https://onesummit2024.sched.com/event/1bmNm/introduction-to-photonic-disaggregated-computing-architecture-shigeru-kotabe-fujitsu) · [Recording](https://www.youtube.com/watch?v=-ID6ifondfE)

Shigeru Kotabe, Leading Researcher (AI deployment infrastructure), Fujitsu

- **Why**: Direct photonic interconnect between compute devices is one of the candidate paths past power- and bandwidth-limited conventional server architectures for AI-era workloads — this is a research lab's concrete architecture proposal, squarely in the PM's optics/DC-compute interest.
- **What**: Fujitsu's "photonic disaggregated computing" architecture with three features: reconfigurable devices for flexible hardware allocation, device-to-device communication to reduce CPU load, and direct photonic connections between devices; plus use cases. (from abstract only)
- **How**: Rather than scaling by adding conventional servers, hardware is disaggregated into reconfigurable pools linked by direct photonics, letting device-to-device paths bypass host CPUs for data movement.
- **Where applicable**: Early-stage research architecture, not a shipping product — relevant as a direction signal for future AI-infrastructure interconnect; Fujitsu-specific, and no evaluation numbers are given in the abstract.

### Applying AI/ML Methods to Diagnose Network Issues Using Telemetry Data - Frank Brockners, Cisco

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUr6/applying-aiml-methods-to-diagnose-network-issues-using-telemetry-data-frank-brockners-cisco) · [Recording](https://www.youtube.com/watch?v=rF03xTqYW6Y)

Frank Brockners, Distinguished Engineer, Cisco (Outshift/CTO division)

- **Why**: ML/LLM-assisted troubleshooting is the most immediately actionable part of "AI for networking" — this grounds it in real telemetry data and explicitly discusses which techniques fit which phase of diagnosis, which is the question practitioners actually face.
- **What**: A working examination of which AI/ML approaches (including LLMs) fit problem identification vs. diagnosis phases, demonstrated on real-world network telemetry, with a candid discussion of advantages and drawbacks of each technique. (from abstract only)
- **How**: Uses real telemetry datasets as the substrate and walks diverse AI/ML methods through the diagnostic workflow end to end rather than presenting a single-point product claim.
- **Where applicable**: Network operations teams with telemetry pipelines in place; technique-level rather than org-specific. Cisco presenter, but the framing is methodology-first; no quantified accuracy figures in the abstract.

### Kubeflow & Istio, a Perfect Match! Investigating Istio’s Role in MLOps - Nina Polshakova & Peter Jausovec, Solo.io

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrs/kubeflow-istio-a-perfect-match-investigating-istios-role-in-mlops-nina-polshakova-peter-jausovec-soloio) · [Recording](https://www.youtube.com/watch?v=SAfCCpmfsTE)

Nina Polshakova, Senior Principal Software Engineer, and Peter Jausovec, Software Architect, Solo.io

- **Why**: Serving ML models reliably (canary releases, authN/Z, traffic mirroring, failover) is where service mesh and MLOps actually intersect — this explains exactly what Istio is doing under Kubeflow/KServe, which most K8s practitioners using KServe never see.
- **What**: A breakdown of how KServe's custom resources translate into Istio resources, the minimum viable Istio configuration for secure ML operations, and how to layer canary model releases, traffic mirroring, fault injection, failover, rate limiting, external auth, and BYO Wasm plugins on the generated Kubeflow/KServe config. (from abstract only)
- **How**: Demonstrates the mapping from KServe CRs to Istio CRs and shows that the "hard" MLOps requirements are mesh concerns — configuration that Kubeflow abstracts away but that you must understand to operate and extend.
- **Where applicable**: Any Kubernetes environment running Kubeflow/KServe with Istio; general cloud-native technique, not org-specific. Vendor (Solo.io) speakers, but the content is a mechanism walkthrough of widely used OSS rather than a product demo.

### Embracing a Data-Driven Approach to Network Automation - Jason Edelman, Network to Code

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrW/embracing-a-data-driven-approach-to-network-automation-jason-edelman-network-to-code) · [Recording](https://www.youtube.com/watch?v=SzMCe6HamHI)

Jason Edelman, Founder and CTO, Network to Code

- **Why**: Every network automation program lives or dies on the state model underneath it — this is a practitioner-focused treatment of source-of-truth design (what data you need, where it lives today, how to define golden state), which transfers across any environment.
- **What**: The argument that clean network data — a defined desired/"golden" state compared continuously against actual network state — is the foundation of durable automation, plus guidance on how organizations should start and what to think about when choosing a source of truth. (from abstract only)
- **How**: Treats the network as a stateful entity: consolidate the data currently scattered across spreadsheets and local databases into a documented model, then reconcile observed state against the golden truth as the automation primitive.
- **Where applicable**: Broadly applicable to any network team beginning or restarting automation; methodology, not tied to specific tooling, scale, or topology. Consultancy-presented but pattern-level rather than pitch-level.

### Keynote: Leveraging Open Source for Operational Excellence at Scale - Dave Temkin, Walmart

**Links:** [Abstract](https://onesummit2024.sched.com/event/1ahF5/keynote-leveraging-open-source-for-operational-excellence-at-scale-dave-temkin-walmart) · [Recording](https://www.youtube.com/watch?v=_5s6f-JB__Q)

Dave Temkin, VP of Platform Infrastructure and Critical Facilities, Walmart

- **Why**: Temkin runs networks, datacenters, and supporting infrastructure for Walmart and previously built Netflix's CDN — this is a rare operator keynote covering open-source adoption for physical DC and network operations at retail scale.
- **What**: An operator's perspective on using open source to run platform infrastructure and critical facilities at Walmart's scale. (from abstract only — the program gives no abstract for this keynote, only the speaker bio.)
- **How**: Not specified in the program text; expect lessons from running networks/DCs at two very large operators and where open source paid off.
- **Where applicable**: Large multi-site private infrastructure operators; the program text is thin here, so treat as a keynote to watch rather than a paper to read.

## Adjacent

### SDN Journey in Verizon: Experiences, Challenges and Path Forward - Yueping Zhang & Sanjay Nayak, Verizon

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUr8/sdn-journey-in-verizon-experiences-challenges-and-path-forward-yueping-zhang-sanjay-nayak-verizon) · [Recording](https://www.youtube.com/watch?v=BSav94evejQ)

Yueping Zhang, Associate Fellow (SDN Technology and Planning), and Sanjay Nayak, Assoc Director, Verizon

- **Why**: One of the few talks with hard operational experience running SDN across tens of thousands of live network elements — including the admission that SDN has fragmented into disjoint point solutions, which is a candid and useful takeaway for anyone building controller architectures.
- **What**: Verizon's experience deploying and scaling its Intelligent Edge Network on a full-SDN approach, the challenges of fast-growing 5G traffic, and the evolution of their SDN controller from a monolithic OpenDayLight package to a fully decoupled microservice architecture, framed as a "network factory" concept. (from abstract only)
- **How**: Decomposing the monolithic ODL controller into decoupled microservices so the control plane can adapt to business dynamics; the greenfield iEN deployment is the reference.
- **Where applicable**: Large carrier/multi-site operators; Verizon-specific in topology and scale, but the monolith-to-microservices controller lesson and the "SDN as point solutions" critique transfer well.

### Code Vs. Data: Optimizing NFV Orchestration with Nephio - Tal Liron, Google

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrx/code-vs-data-optimizing-nfv-orchestration-with-nephio-tal-liron-google) · [Recording](https://www.youtube.com/watch?v=CoUDp8LbfjY)

Tal Liron, Staff Engineer, Google (Telecom Network Automation team)

- **Why**: The "configuration-as-data vs. Helm charts" question is a live architectural debate for anyone running Kubernetes at scale — this makes the tradeoffs concrete using Nephio's KRM-based approach.
- **What**: An argument for placing code next to the data it processes, comparing management vs. workload clusters, walking through Nephio's specialization pipeline and the operator reconciliation loop, and contrasting Nephio's configuration-as-data (CaD) paradigm with Helm charts — "breaking the Helm chart apart and putting the pieces where they belong." (from abstract only)
- **How**: KRM resources as the data model, with the specialization pipeline transforming generic blueprints into environment-specific packages and reconciliation loops maintaining state continuously.
- **Where applicable**: Kubernetes orchestration design generally; the CaD-vs-Helm analysis applies beyond telco. Telco-flavored context, but the architectural argument is general.

### Lessons Learned from Using Nephio to Manage a Real-World 5G Core - István Kispál, Nokia

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUqx/lessons-learned-from-using-nephio-to-manage-a-real-world-5g-core-istvan-kispal-nokia) · [Recording](https://www.youtube.com/watch?v=rjWZQv8DkZ0)

István Kispál, Automation Architect, DMTS, Nokia Bell Labs

- **Why**: Honest "what we had to change" case studies of open-source orchestration on a production-identical workload are rarer and more useful than roadmap talks — this is one of them.
- **What**: A case study deploying a Nokia 5G core (identical to the commercial offer) on AWS via Nephio R2, describing NF topology with a target-agnostic blueprint, then transforming it through automated processes plus human engineers into an AWS/Nokia-specific package deployed with a GitOps tool — including which parts of Nephio R2 had to be modified to cope. (from abstract only)
- **How**: Generic, environment-agnostic blueprints are specialized into concrete deployment packages by a human+automation pipeline, then deployed and operated GitOps-style on AWS.
- **Where applicable**: Teams evaluating Nephio for real workloads; Nokia/AWS-specific in detail, but the "what broke and what we changed" content is exactly the transferable part.

### Overcoming Challenges for AI-Fabric with SONiC - Madhu Paluru, Aviz Networks

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUsa/overcoming-challenges-for-ai-fabric-with-sonic-madhu-paluru-aviz-networks) · [Recording](https://www.youtube.com/watch?v=sXuru247dZA)

Madhu Paluru, Director of Engineering, Aviz Networks

- **Why**: Operating the network under AI training/inference traffic (elephant flows, incast, config-error sensitivity) is a current, fast-moving problem; this collects the operational requirements and proposes SONiC-based answers.
- **What**: How GenAI training and inference workloads stress network infrastructure, and proposals to manage AI fabrics on SONiC via config automation to minimize configuration errors and deep-visibility tooling for faster troubleshooting. (from abstract only)
- **How**: SONiC's open control/data plane as the base, with automation layering to reduce human config errors and visibility tooling for diagnosis in AI-fabric conditions.
- **Where applicable**: SONiC-based AI fabrics; vendor-presented (Aviz builds a commercial SONiC stack), so treat solution specifics as a pitch-informed roadmap rather than validated deployment results.

### Real-World Network Function Chaining - Lessons Learned - Benjamin Goldstone, Dell Technologies

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrv/real-world-network-function-chaining-lessons-learned-benjamin-goldstone-dell-technologies) · [Recording](https://www.youtube.com/watch?v=3XJB8P81Uxw)

Benjamin Goldstone, Senior Network Engineer, Dell Technologies

- **Why**: Scaling network functions horizontally on standard compute with SR-IOV and standards-based L2 tricks, with open-sourced code, is directly relevant to virtualized/elastic network service design — and the "tier 1 service provider" provenance suggests real scale.
- **What**: Blueprints for building network function chaining platforms on standard compute — using Q-in-Q, VLAN translation, and SR-IOV — as delivered for real tier-1 service providers, with lessons learned and open-sourced code examples to start from. (from abstract only)
- **How**: Network functions run as scale-out software on commodity servers; L2 constructs (Q-in-Q, VLAN translation) plus SR-IOV provide the performance and multi-tenant separation needed to chain functions at provider scale.
- **Where applicable**: Service-provider and large-enterprise NFvi designs; requires SR-IOV-capable NICs and is L2-centric. The open-sourced code makes it checkable rather than anecdotal.

### Harnessing Observability with AI for Edge Applications: Innovations in APM/T - Fatih E. Nar, Red Hat

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrT/harnessing-observability-with-ai-for-edge-applications-innovations-in-apmt-fatih-e-nar-red-hat) · [Recording](https://www.youtube.com/watch?v=O7EsZriRTXo)

Fatih E. Nar, Distinguished Chief Architect, Red Hat

- **Why**: eBPF-based observability fused with LLMs for application performance monitoring is at the intersection of two of the PM's core interests (eBPF, AI for operations).
- **What**: Advances in AI-infused application performance monitoring and tracing for edge applications, centered on integrating eBPF with LLMs. (from abstract only — the program provides only this single-sentence abstract, so depth of evaluation and results cannot be assessed.)
- **How**: Not specified beyond the eBPF + LLM combination; eBPF supplies deep runtime telemetry, and LLM-based analysis turns it into actionable diagnosis, presumably.
- **Where applicable**: Edge/cloud-native application operations; flag that the abstract is unusually thin, so treat as a talk to sample rather than a paper to rely on.

### RAN-in-the-Cloud: Utilization and New Services Breakthroughs - Amar Kapadia, Aarna Networks & Shuvo Chowdhury, NVIDIA

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUs6/ran-in-the-cloud-utilization-and-new-services-breakthroughs-amar-kapadia-aarna-networks-shuvo-chowdhury-nvidia) · [Recording](https://www.youtube.com/watch?v=4cMv25sRo_A)

Amar Kapadia, Co-Founder and CEO, Aarna Networks, and Shuvo Chowdhury, Principal Product Manager, NVIDIA

- **Why**: RAN is the largest capex/opex line for operators and runs at 25–50% utilization; cloudifying it as a multi-tenant, containerized workload on shared GPU infrastructure is a notable utilization-and-monetization play relevant to anyone thinking about GPU cluster economics.
- **What**: The argument and implementation direction for running RAN as a service in multi-tenant cloud infrastructure, containerized alongside other workloads — cutting operator costs, improving sustainability, and enabling edge services such as GenAI on the same infrastructure. (from abstract only)
- **How**: RAN functions containerized on shared, multi-tenant cloud/GPU infrastructure (NVIDIA AI/5G datacenter products plus Aarna's orchestration), with utilization gains and new edge service monetization as the payoff.
- **Where applicable**: Operators and private-5G deployments with GPU-equipped edge sites; vendor-led (NVIDIA/Aarna), so the utilization claims and cost math deserve independent verification.

## Wildcard

### The Dark Side of AI: The Hidden Supply Chain Risks in Open-Source AI Models - Guy Nachshon, Checkmarx

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUqw/the-dark-side-of-ai-the-hidden-supply-chain-risks-in-open-source-ai-models-guy-nachshon-checkmarx) · [Recording](https://www.youtube.com/watch?v=PpV_7ZOwMdE)

Guy Nachshon, Security Researcher, Checkmarx

- **Why**: As the PM adopts open models and AI tooling, this is a class of supply-chain risk that most infrastructure teams haven't priced in — models themselves as a malware delivery vector, demonstrated live.
- **What**: Research on weak points in how AI models are constructed, with demos of models manipulated into malicious behavior — including a "Malicious Copilot" case study where a code-completion model is trained to target specific victims by embedding malicious code — plus practical takeaways for companies using generative AI/LLMs. (from abstract only)
- **How**: Attacks via the model artifact itself (training-data and fine-tuning manipulation) rather than the surrounding software, so standard software supply-chain controls (SBOMs, scanning) don't catch them.
- **Where applicable**: Any organization consuming open-weights models or AI IDE plugins; general risk, not org-specific. Security-vendor research, but with concrete demonstrated attacks, which is what gives it weight.

### Full Stack Explicit Confidence with Project Alvarium - Trevor Conn, Dell Technologies

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUsF/full-stack-explicit-confidence-with-project-alvarium-trevor-conn-dell-technologies) · [Recording](https://www.youtube.com/watch?v=nT0fuKnfl6c)

Trevor Conn, Distinguished Engineer, Dell Technologies

- **Why**: "Measurable, portable trust in data and systems" as a continuous score across the whole stack is an unusual primitive — it reframes zero-trust from a binary gate into quantified confidence, and Alvarium extends it below the app layer into host, OS, and CI/CD artifacts.
- **What**: Project Alvarium's framework for capturing immutable metadata to objectively quantify "data confidence" as data traverses a distributed topology, now extended to the host, OS, and CI/CD layers, and how a confidence score can be operationalized for platform-integrity outcomes such as zero trust. (from abstract only)
- **How**: Trust-aware components emit signed, immutable metadata at each handling boundary; the accumulated trail yields a computable confidence score that downstream policy can act on.
- **Where applicable**: Distributed edge/IoT topologies and multi-party data pipelines more than DC fabrics; open-source (LF Edge) and conceptually general, though adoption is still early — watch as a direction, don't expect turnkey.

### Network and Computing Infrastructure for the 2030s - Haruhisa Fukano & Inoue Reo, Fujitsu

**Links:** [Abstract](https://onesummit2024.sched.com/event/1YUrp/network-and-computing-infrastructure-for-the-2030s-haruhisa-fukano-inoue-reo-fujitsu) · [Recording](https://www.youtube.com/watch?v=kdkrP0A07dI)

Haruhisa Fukano, Manager (1Finity), and Inoue Reo, Fujitsu

- **Why**: The IOWN (photonics-first infrastructure) forum partnering with LF Edge on a joint PoC signals where physical-layer infrastructure research is heading — power-efficient photonics as the answer to bandwidth and energy walls, which is squarely worth watching even if early.
- **What**: The case that 2030s workloads require a paradigm shift in communications and computing (power consumption and bandwidth as the binding constraints), and the plan for a joint IOWN + LF Edge PoC combining next-gen photonic infrastructure with open-source edge software. (from abstract only)
- **How**: Combines IOWN's photonic network/computing technologies with LF Edge open-source stacks; the talk covers the PoC's demonstration points and future plans.
- **Where applicable**: Strategic/forward-looking rather than deployable today; PoC-stage, Fujitsu/IOWN-specific, and no results exist yet — but relevant to long-range optics and DC infrastructure planning.

## Themes

- **Telco dominates, but the DC/cloud sessions that exist are substantive**: the program is overwhelmingly O-RAN/5G/Nephio (LFN's home turf), and the strongest technical content sits in a small cluster of SONiC, P4, and DPU talks from Google, Alibaba, and the OPI ecosystem.
- **AI is the framing device everywhere, but mostly aspirational**: nearly every session title now carries "AI" or "GenAI"; the credible AI-infrastructure content (AI fabrics, non-minimal routing for million-GPU clusters) is a small subset, alongside genuinely promising but early ml-for-networking work (telemetry diagnosis, eBPF+LLM observability).
- **Nephio is the center of gravity for automation**: a half-dozen talks cover Nephio from vision to "what we had to change in R2 to run a real 5G core" — the project is clearly in its first encounter with production workloads, and the honest lessons-learned talks are the ones worth reading.
- **Kubernetes is the assumed substrate for network software**: from SONiC fabric simulation (ALPINE) to NFV orchestration, KRM/GitOps/reconciliation have become the default operating model for network function lifecycle, not just for container workloads.
- **Simulation-before-hardware is a maturing practice**: ALPINE (100+ virtual SONiC switches on K8s) and the SAI virtual switch in DentOS both push CI-grade testing of NOS control planes without lab hardware — a meaningful cost and velocity shift for fabric operators.
- **Physical-layer futures are being seeded at the edges**: photonic disaggregated computing (Fujitsu) and the IOWN/LF Edge PoC point at photonics as the escape hatch from power and bandwidth limits, while OPI works on standardizing the DPUs already arriving in servers.
