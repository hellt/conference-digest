<!--
conference: Open Networking & Edge Summit 2025
source_url: https://onesummit2025.sched.com/list/descriptions/
generated: 2026-11-10
registry_key: onesummit-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Open Networking & Edge Summit 2025

*Note: this program is a keynote-and-telco-heavy subset — most sessions are strategy, analyst, or ecosystem talks rather than deep technical papers. The picks below reflect that reality; several are flagged as vision/survey-grade rather than results-grade. All page fetches failed (403), so all write-ups derive from the program abstracts.*

## Core

### SONiC: The Global Networking Operating System for All

**Links:** [Abstract](https://onesummit2025.sched.com/event/1xg29/sonic-the-global-networking-operating-system-for-all-michael-ma-microsoft-peter-plak-dell) · [Recording](https://www.youtube.com/watch?v=hoHknEPG8EE)

Michael Ma, Microsoft; Peter Plak, Dell

- **Why**: SONiC is the closest thing the industry has to a standard open NOS for datacenter switches, and it is the layer where the PM's physical-fabric and cloud-ops interests converge — disaggregated switch silicon, automated fleet operations, and Azure-scale production validation. Whatever SONiC's community roadmap is this cycle directly affects build-vs-buy for DC fabrics.
- **What**: A status-and-roadmap session on SONiC's evolution as a modular, hardware-agnostic open source network OS, plus the speaker's own work at Microsoft Azure on accelerating network device updates using container technologies (from abstract only).
- **How**: SONiC decouples the NOS from switch hardware via containerized subsystems and SAI as the switch-abstraction layer; the Azure-side contribution described here is using container tooling to make switch software updates faster and less disruptive — a direct operational-velocity win, though specifics (mechanism, measured update times) are not in the abstract.
- **Where applicable**: Broadly applicable across merchant-silicon datacenter fleets (broad ecosystem of ODM/merchant switch platforms via SAI). The Azure device-update experience is Microsoft-specific in scale but the technique is general. Caveat: this is a co-presented community/vendor session, so expect roadmap framing rather than empirical evaluation.

### IOWN Global Forum and Open Source - Key Enablers for Next Decade

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdf/iown-global-forum-and-open-source-key-enablers-for-next-decade-masahisa-kawashima-ntt-corporation) · [Recording](https://www.youtube.com/watch?v=Pb0eKDvgfG4)

Masahisa Kawashima, NTT Corporation

- **Why**: IOWN is one of the few serious large-scale programs pushing integrated photonics into compute and network infrastructure — photonics-based DC interconnect, high-capacity optical I/O, and energy-efficient transport. For a PM whose core is optics and physical DC/WAN systems, this is a rare look at where the optical roadmaps of a major operator actually intersect open source.
- **What**: A roadmap talk on NTT's Innovative Optical and Wireless Network (IOWN) architecture and, importantly, how IOWN is now partnering with open source communities — LFN, LF Edge, and OPI — to integrate open source software into the IOWN platform (from abstract only).
- **How**: Not a technique talk: the mechanism is cross-organizational — the IOWN Global Forum defines the photonic architecture requirements, and the partnerships with LFN/LF Edge/OPI are intended to supply the open software layer (orchestration, provisioning, DPU-adjacent compute interfaces) around it.
- **Where applicable**: NTT/IOWN-specific architecture, but the open-source integration point matters broadly — OPI in particular covers DPU/accelerator provisioning standards, which has cross-industry applicability. Expect vision and roadmap depth, not deployment results.

### AI - Lessons Learnt from World's Largest Network

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdQ/ai-lessons-learnt-from-worlds-largest-network-dr-junlan-feng-china-mobile-research-institute) · [Recording](https://www.youtube.com/watch?v=ongBnSCNlXc)

Dr. Junlan Feng, China Mobile Research Institute

- **Why**: This is the ml-for-networking slot — a decade-plus of applied AI on the world's largest operator network, from intent-based operations to autonomous networks. For a PM interested in ML for infrastructure operations, hearing what actually worked (and didn't) at China Mobile's scale is a higher-value signal than most vendor AIOps pitches.
- **What**: Lessons from China Mobile's AI journey operating the largest service-provider network: the progression from intent-based networking to automated/autonomous networks, and the role of open technology adoption in that progression (from abstract only).
- **How**: Not specified in the abstract — expect a retrospective of AI/autonomous-networking deployments (fault prediction, closed-loop operations, intent translation) rather than a single novel technique.
- **Where applicable**: Operator-scale and telecom-specific; the lessons about staging intent → automation → autonomy likely transfer, but the data and network scale are China Mobile's. Treat reported results with the usual caution until specifics appear.

## Adjacent

### State of Open Source Networking - Arpit Joshipura & Hilary Carter, The Linux Foundation

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vDhI/state-of-open-source-networking-arpit-joshipura-hilary-carter-the-linux-foundation) · [Recording](https://www.youtube.com/watch?v=wRlx2lD-VSk)

Arpit Joshipura & Hilary Carter, The Linux Foundation

- **Why**: The ecosystem-setting keynote, and the one place in this program where survey data (LF Networking's global research survey) about real open source networking adoption and deployment will be presented — useful calibration for where open networking actually is versus the hype.
- **What**: Vision, predictions, real-world deployment examples, and results of the LF Networking global research survey (from abstract only).
- **How**: Survey methodology and sample are not described in the abstract; treat the numbers accordingly.
- **Where applicable**: Cross-industry view rather than a specific environment.

### An Industry Analyst's Perspective on Telco Cloud

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdT/an-industry-analysts-perspective-on-telco-cloud-christoforos-sarantopoulos-james-crawshaw-inderpreet-kaur-omdia) · [Recording](https://www.youtube.com/watch?v=eP8TX-aLkKk)

Christoforos Sarantopoulos, James Crawshaw & Inderpreet Kaur, Omdia

- **Why**: A condensed analyst view of telco cloud trends — operational complexity, resource-utilization architecture choices, CI/CD, and AI in cloud ops. The reskilling/data-governance/CI-CD recommendations are the transferable part for anyone running private cloud or NFV estate.
- **What**: An overview of telco cloud evolution from NFV through cloudified 5G core, with recommendations for service providers (reskilling, data governance, CI/CD) and advice for vendors on supporting open-source adoption and a common automation framework (from abstract only).
- **How**: Analyst synthesis across operators and vendors; no single mechanism.
- **Where applicable**: Telco/operator context. Analyst talks of this kind are useful for pattern-spotting but carry no empirical evaluation — and vendor-recommendation content can shade into pitch.

### Sponsored Session: Ready for Impact: EVE Steps from 10k Kubernetes Clusters to Edge AI

**Links:** [Abstract](https://onesummit2025.sched.com/event/1w8QU/sponsored-session-ready-for-impact-eve-steps-from-10k-kubernetes-clusters-to-edge-ai-erik-nordmark-zededa) · [Recording](https://www.youtube.com/watch?v=bWHSoSWJYJQ)

Erik Nordmark, ZEDEDA

- **Why**: Flagged as a sponsored session, but with a concrete production number attached: EVE (LF Edge) is claimed to run 10,000+ single-node Kubernetes clusters and VMs in production. Fleet-style Kubernetes at the edge — one-cluster-per-site, upgrade, and resiliency mechanics — is directly relevant to the PM's K8s-operations interests, and edge AI inference workflow integration is the forward-looking part.
- **What**: A status talk on EVE's graduation to LF Edge's Impact stage, the 10k-cluster production footprint, current work to enable AI inference at the edge (workflows and integrations), and new resiliency efforts (from abstract only).
- **How**: EVE is an open source edge OS providing virtualization and container runtime isolation on distributed edge nodes, orchestrated centrally (ZEDEDA's commercial orchestration sits on top). The AI-inference enablement is described as workflow/integration work rather than a new mechanism.
- **Where applicable**: Edge deployments with single-node-per-site topology — quite different constraints from a central DC cluster. The 10k figure is ecosystem-reported, not independently audited; keep in mind the speaker is ZEDEDA's CTO.

### Network Infrastructure to APIs - How Open Source Enables Speed of Innovation and Monetization

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdc/network-infrastructure-to-apis-how-open-source-enables-speed-of-innovation-and-monetization-nathan-rader-sebastian-zechlin-deutsche-telekom) · [Recording](https://www.youtube.com/watch?v=1_TimBymEaw)

Nathan Rader & Sebastian Zechlin, Deutsche Telekom

- **Why**: The CAMARA-style network-API movement is where telco network capability is being productized; understanding DT's open-source-based approach is useful context for anyone weighing API exposure as the interface layer between infrastructure and applications.
- **What**: DT's vision and journey of a fully open network spanning infrastructure through APIs (including CAMARA), framed around innovation speed, lower cost, and asset monetization, plus a roadmap for community contribution (from abstract only).
- **How**: Layered open source adoption across infrastructure, OSS, and the CAMARA API framework.
- **Where applicable**: Large-operator context; the CAMARA framework itself is multi-operator. Expect strategy and journey narrative rather than technical depth.

### A Journey Towards Automated Telco Cloud

**Links:** [Abstract](https://onesummit2025.sched.com/event/1xg45/a-journey-towards-automated-telco-cloud-mesut-soyturk-odine-labs-salih-bilge-cihan-turkcell)

Mesut Soytürk, Odine Labs & Salih Bilge Cihan, Turkcell

- **Why**: Potentially one of the few real operator-case sessions in the program — an operator-plus-vendor pair describing telco cloud automation practice.
- **What**: Unknown — the program text for this session contains no abstract, so its content cannot be characterized (abstract missing from program text).
- **How**: Unknown from the program text.
- **Where applicable**: Judging by the speakers' roles (Turkcell telco cloud engineering, Odine Labs orchestration), presumably a Turkcell telco-cloud deployment story — but this is inference from speaker bios, not stated content.

### Standards and Open Source Harmonization - Silvia Almagia, ETSI; Hui Deng, Huawei; Raúl Álvarez, Open Compute Project Foundation; Moderated by Arpit Joshipura, The Linux Foundation

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdi/standards-and-open-source-harmonization-silvia-almagia-etsi-hui-deng-huawei-raul-alvarez-open-compute-project-foundation-moderated-by-arpit-joshipura-the-linux-foundation) · [Recording](https://www.youtube.com/watch?v=PcA-bpTrf2I)

Silvia Almagia (ETSI), Hui Deng (Huawei), Raúl Álvarez (OCP Foundation), moderated by Arpit Joshipura (The Linux Foundation)

- **Why**: The standards↔open-source convergence question (ETSI/NGMN/OCP vs. LFN projects) affects interoperability roadmaps in exactly the PM's domains — cloud-native networking, green/efficiency targets, and AI infrastructure. Knowing where this harmonization effort stands after five years is cheap but valuable context.
- **What**: A moderated panel reviewing progress and upcoming requirements for harmonizing standards and open source across cloud-native, green, and AI themes (from abstract only).
- **How**: Inter-organizational alignment between standards bodies (ETSI, NGMN) and open communities (OCP, LFN); no technical mechanism.
- **Where applicable**: Ecosystem-wide but abstract-level; expect directional signals, not results.

## Wildcard

### AI-RAN and Open Source: Building Scalable Dataset Pipelines for AI Training

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdN/ai-ran-and-open-source-building-scalable-dataset-pipelines-for-ai-training-alex-jinsung-choi-softbank-corp) · [Recording](https://www.youtube.com/watch?v=ojI8g4WvXqE)

Alex Jinsung Choi, SoftBank Corp. (Chair, AI-RAN Alliance)

- **Why**: Not about the PM's domains — it's telecom RAN — but the core problem is one they know intimately from ML systems: high-quality training data is the bottleneck, and open, collaborative dataset pipelines (aggregation, curation, annotation, synthetic data, with security/compliance guardrails) are an emerging pattern for any domain where proprietary data can't be shared. Watching how the AI-RAN Alliance solves data sharing under governance constraints is a preview of how other infrastructure-ML domains will.
- **What**: How open-source tooling can build collaborative dataset pipelines for AI-driven network optimization in RAN, including AI-RAN's role in synthetic data generation and its connection to global AI governance (from abstract only).
- **How**: Open-source pipelines for data aggregation, curation, and annotation with security/compliance built in, plus synthetic data generation to compensate for scarce labeled telecom data.
- **Where applicable**: Telecom RAN domain (SoftBank/AI-RAN Alliance-specific datasets), but the dataset-governance pattern is general.

### InstantX: Vodafone's Edge Innovation for the Future of Telco

**Links:** [Abstract](https://onesummit2025.sched.com/event/1vmdZ/instantx-vodafones-edge-innovation-for-the-future-of-telco-sampada-basarkar-vodafone) · [Recording](https://www.youtube.com/watch?v=4IKGcKkc3JI)

Sampada Basarkar, Vodafone

- **Why**: Outside the PM's core, but notable as a signal: a major operator insourcing a production edge platform (V2X/A2X communication) into the open source community. When telcos start donating runtime platforms rather than just joining foundations, it says something about where edge infrastructure economics are heading.
- **What**: A keynote on Vodafone's InstantX edge platform — powering scalable V2X and A2X communication — and Vodafone's decision to insource the technology into open source, including the challenges overcome (from abstract only).
- **How**: Platform details are not given in the abstract; the mechanism of interest is the open-sourcing process itself (moving a proprietary telco platform into a community).
- **Where applicable**: Vodafone-specific production history; generalizable mainly as a precedent for operator platform contributions.

## Skipped

AI 101 for Networking & Edge (explicit beginner/buzzword tutorial), the Infosys sponsored session on AI frameworks and Responsible AI (vendor framework pitch with no validated results), Edge AI: The $100B+ Opportunity (consulting market forecast), the two AMA/panel community sessions, and the closing remarks — none offer transferable technical content.

## Themes

- **Open source networking is consolidating around SONiC + LFN as the de facto stack**, with SONiC now positioned as the "global NOS"; the interesting shift is operational maturity (faster device updates, container tooling) rather than new architecture.
- **AI is the headline everywhere, but almost always as aspiration** — only China Mobile's session promises deployment-scale lessons; most AI content here is framework, governance, or forecast talk.
- **Telco cloud's center of gravity has moved from NFV to automation and CI/CD** — the recurring threads across Omdia, Turkcell, and the DT sessions are operational complexity, resource utilization, and reskilling, not virtualization itself.
- **Edge is being redefined by AI inference and by Kubernetes-at-the-edge scale** (EVE's 10k single-node clusters being the concrete number in the program), moving edge from "IoT gateway" to "distributed K8s + inference."
- **Optics is represented by IOWN's photonics roadmap**, and its notable move is toward open source integration (LFN/LF Edge/OPI) — a signal that even hardware-centric programs now need an open software layer to be credible.
- **Standards bodies and open source communities are formally converging** (ETSI/NGMN/OCP with LFN), which will increasingly determine interop requirements in cloud-native, green, and AI infrastructure.
