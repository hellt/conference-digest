>>> HOW TO RUN THIS <<<
This is the digest prompt for onesummit-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/onesummit-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/onesummit-2025.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, cloud
platforms, Kubernetes, and AI. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect); cloud infrastructure and operations (public and private
cloud, virtualization, compute/storage/networking, multi-tenancy, and
automation); Kubernetes and cloud-native systems (architecture and
operations, eBPF, Cilium, Kubernetes networking, Gateway API, service mesh,
IPAM, and BGP/datapath internals); and AI (AI/ML systems, LLMs and agents,
model training and inference, GPU/accelerator infrastructure, networking for
AI, and ML for infrastructure operations). Physical DC and WAN systems work is
CORE to this PM, not adjacent — do not down-rank a paper for being about
hardware, optics, or datacenter fabric.

Below is the program for Open Networking & Edge Summit 2025. Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

Judge each item by what it changes for a practitioner: novel techniques and
firmly substantiated results over incremental benchmark improvements, and
operational lessons, tooling, automation and postmortems that transfer across
environments over org-specific anecdotes or vendor pitches in disguise.
Treat strong empirical evaluation and real deployment experience as signals of
weight; treat unvalidated claims with caution. Note when a technique depends
on a specific operator's scale, topology or silicon.

## Enriching from the source material (best effort)

The program text gives you a title, authors, and an abstract per item, and
often links (`page:`, `pdf:`, `slides:`, `video:`). The abstract alone is thin — the full
paper has the methodology, real results, and limitations that make the What /
How / Where-applicable sections accurate instead of guessed.

If you have a tool to fetch URLs, then for EACH selected item (Core, Adjacent,
and Wildcard) try to retrieve the fuller source before writing it up:

- Prefer a `pdf:` link; else fetch the `page:` link (often has the full text or
  a longer description); a `video:` link is a last resort, don't transcribe it.
- Use what you retrieve to ground What/How/Where-applicable in the paper's
  actual contributions, evaluation, and stated constraints.

This is strictly best-effort. Many links fail or are paywalled:

- If a fetch fails, is paywalled, returns only an abstract, or you have no fetch
  tool, just fall back to the abstract already in the program text. That is
  fine and expected — do not stall or skip the item.
- NEVER invent paper contents, numbers, or findings from a failed or partial
  fetch. If you only had the abstract, write from the abstract.
- Note when an item's write-up is based only on the abstract, e.g. end its
  What line with "(from abstract only)", so the reader knows the depth.
- Do not let enrichment change which items you select or their tier; selection
  is from the program. Enrichment only deepens the write-up.

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to the PM's core interests as listed above
  (networking, cloud, Kubernetes, or AI) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title**: the `###` heading is the item's title exactly as the program
  gives it, with nothing added. Speaker(s)/author(s) with affiliation go on
  the line below it.
- No links section: the pipeline puts a links row (abstract page, paper,
  slides, recording) under every heading after you finish, from the program's
  `page:`/`pdf:`/`slides:`/`video:` lines and from verified sources. Do not
  write one, and do not link the title.
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Search keywords

The site's search indexes topic keywords per page. After the Themes section,
append ONE fenced `json` code block - the pipeline reads it machine-side and
removes it before publishing, so it is never rendered - of exactly this shape:

```json
{"post": ["cloud", "ai"], "talks": {"<pick heading>": ["cloud", "ai-networks"], "<pick heading>": ["kubernetes", "cni"]}}
```

- "post": 3-6 topics this digest as a whole covers.
- "talks": one entry for EVERY pick you selected, keyed by its exact `###`
  heading string (copy it character for character, including any presenter
  part), with 2-4 tags naming what the talk is about - the technology or
  practice, not its tier or the conference.
- Tags are lowercase, hyphenated, single concepts. Use ONLY tags from this
  vocabulary:

- `ai` - artificial intelligence systems, applications and practices not covered by a finer AI tag
- `ai-networks` - networking for AI/ML training and inference clusters (job-level load balancing, collectives, topology-aware scheduling)
- `gpu-clusters` - GPU accelerator interconnects and cluster fabrics (NVLink, scale-up vs scale-out)
- `ml-for-networking` - machine learning applied to network operation (anomaly detection, traffic prediction, AIOps)
- `data-center-fabric` - physical data-center fabric design (topologies, CLOS, buffer management, congestion)
- `optics` - optical transport, transceivers, pluggables, DWDM, LPO/CPO
- `ethernet` - Ethernet as a technology standard (P802.3 work, speeds, PHYs)
- `cabling` - structured cabling, fiber plants, MPO/MTP, copper
- `power` - power delivery and efficiency in DCs (PUE, 48V, power sourcing equipment)
- `dpu` - data processing units, SmartNICs, offload and hardware offload in general
- `rdma` - RDMA, RoCE, InfiniBand, remote memory semantics
- `load-balancing` - traffic load balancing, ECMP/adaptive hashing, LB algorithms and architectures
- `packet-scheduling` - packet scheduling and queueing disciplines (PIFO, QoS schedulers, traffic management)
- `congestion-control` - congestion control and notification (ECN, PFC, DCQCN, L4S)
- `switching` - switch hardware and forwarding architecture (ASICs, buffers, pipelines)
- `silicon` - switch/NPU ASIC design, chip roadmaps, co-packaging
- `bgp` - BGP the protocol and its operation
- `routing-protocols` - routing protocol design and operation in general (ISIS, OSPF, BGP convergence)
- `segment-routing` - SR, SRv6, SR-MPLS and network programming with them
- `ipv6` - IPv6, its deployment and transition
- `mpls` - MPLS, labels, and LDP/RSVP heritage
- `peering` - peering business and practice, IXPs, interconnection agreements
- `interconnection` - data center interconnect and carrier interconnection
- `cdn` - content delivery networks
- `address-policy` - IP address and ASN allocation policy (RIR policy processes)
- `internet-governance` - regulation, standards bodies, and geopolitics of the internet
- `kubernetes` - Kubernetes architecture, operations, workloads and networking
- `cni` - container network interfaces and container networking plugins
- `containers` - containerization, images, runtimes
- `service-mesh` - service mesh (sidecars, eBPF meshes, mTLS between services)
- `cloud` - public and private cloud infrastructure, platforms and operations
- `cloud-native` - cloud-native patterns in general (CNCF ecosystem)
- `orchestration` - workflow and device orchestration, intent-based systems, network controllers
- `automation` - network automation (tooling, pipelines, source of truth, CI/CD for networks)
- `configuration-management` - managing device configuration at scale (config generation, drift, validation)
- `gitops` - GitOps workflows and version control practices
- `p4` - the P4 language and P4-programmable targets
- `linux-networking` - the Linux kernel networking stack (TC, netlink, drivers, offloads)
- `programmable-dataplane` - programmable data planes in general (PNA, portable switch OSes, pipes)
- `ebpf` - eBPF, XDP, and kernel bypass dataplanes
- `http` - HTTP and web protocols, QUIC
- `ipam` - IP address management and allocation
- `sdn` - software-defined networking, controllers, separation of control and data plane
- `network-security` - network security topics not covered by a finer tag
- `email-security` - email security and phishing (DMARC, spam, brand abuse)
- `malware-analysis` - malware, reverse engineering, botnet takedowns
- `threat-intelligence` - threat intel, IoCs, attack tracking
- `vulnerability-management` - vulnerability disclosure, patching, CVE economy
- `offensive-security` - offensive security, red teaming, exploit development
- `privacy` - privacy engineering, tracking, anonymity, privacy-preserving systems
- `censorship` - censorship, filtering, and measurement of Internet shutdowns
- `ddos` - DDoS attack and defense
- `anomaly-detection` - detecting anomalies and attacks in traffic
- `firewall` - firewalling and network policy enforcement
- `tls` - TLS, certificates, and protocol encryption
- `encryption` - encryption of traffic and data in general (MACsec, IPsec, E2E)
- `quantum-safe` - post-quantum cryptography and migration
- `quantum-networking` - quantum networking and entanglement distribution as infrastructure
- `pki` - public key infrastructure, certificate lifecycle
- `attestation` - remote attestation, measured boot, hardware roots of trust
- `zero-trust` - zero-trust architecture and microsegmentation
- `identity` - digital identity, identity ecosystems, ID standardization
- `authentication` - authentication methods and protocols (MFA, passkeys, WebAuthn)
- `authorization` - authorization, OAuth/OIDC, access control, policy engines
- `observability` - network observability tooling, telemetry pipelines, flow data
- `telemetry` - telemetry protocols (gNMI, streaming, INT)
- `measurement` - measurement methodology, probing, active/passive measurement studies
- `benchmarking` - benchmarks, testbeds, performance evaluation of systems
- `testing` - testing and verification of networks and configs (formal verification belongs here)
- `sre` - site reliability engineering practice, incident response, operations culture
- `capacity-planning` - capacity planning and forecasting
- `troubleshooting` - troubleshooting and root-cause analysis, outages and postmortems
- `dns` - DNS, resolvers, authoritative infrastructure
- `multicast` - multicast and broadcast replication
- `wifi` - wireless and mobility
- `mobile` - mobile and cellular networks (5G, roaming, RAN)
- `iot` - Internet of Things scale problems, LPWAN
- `cxl` - CXL and memory-fabric interconnects for pooled memory
- `time-sync` - time and clock distribution (NTP/PTP, GNSS timing)
- `spectrum` - radio spectrum policy and management
- `open-source` - open-source project practice and sustainability
- `standardization` - standards processes (IETF/IEEE) and documents
- `api` - APIs for network control (REST/gRPC, schemas, contract design)

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

The digest is read on GitHub (GitHub-Flavored Markdown viewed in the repo) and
on the project's Zensical site, which renders the same file. Use only syntax
both render reliably, and follow these rules:

- Headings with `#`/`##`/`###`; bold with `**...**`; italics with `*...*`.
- Bullet lists with `-`. Put a blank line before every list, before every
  heading, and between paragraphs, or they won't render correctly.
- Indent nested lists by four spaces per level; avoid deeper nesting.
- Any link you do write is `[text](url)` — never a bare URL — and uses a URL
  exactly as the program text gives it.
- No raw HTML except the metadata comment below. Do not use heading IDs,
  footnotes, definition lists, or other non-GFM extensions.
- You may use tables and `code spans` where they genuinely help, since GitHub
  supports them; don't force them.

Begin the output with this metadata, wrapped in an HTML comment so it does not
show in the rendered view but stays in the source:

<!--
conference: Open Networking & Edge Summit 2025
source_url: https://onesummit2025.sched.com/list/descriptions/
generated: 2026-11-10
registry_key: onesummit-2025
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

### State of Open Source Networking - Arpit Joshipura & Hilary Carter, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation Hilary Carter SVP Research, The Linux Foundation Hilary Carter is a writer, researcher, and team leader, producing engaging, decision-useful insights that broaden the understanding of open source and emerging technologies and their impact on business, government, and society. She has contributed to books and numerous research reports... Read More →
page: https://onesummit2025.sched.com/event/1vDhI/state-of-open-source-networking-arpit-joshipura-hilary-carter-the-linux-foundation
Opening Remarks and sharing the vision of open source networking, predictions and real world deployments. Session will also provide results of LF Networking global Research survey.

### AI-RAN and Open Source: Building Scalable Dataset Pipelines for AI Training - Alex Jinsung Choi, SoftBank Corp.
Speakers: Alex Jinsung Choi Principal Fellow & Chair of the AI-RAN Alliance, SoftBank Corp. Dr. Alex Jinsung Choi, a South Korean luminary in the global mobile telecommunications sector, boasts over three decades of industry experience. Currently, Dr. Choi is working at SoftBank Corp.’s Research Institute of Advanced Technology and continues to champion innovation at the... Read More →
page: https://onesummit2025.sched.com/event/1vmdN/ai-ran-and-open-source-building-scalable-dataset-pipelines-for-ai-training-alex-jinsung-choi-softbank-corp
AI-RAN relies on high-quality datasets for effective model training, but accessing and standardizing telecom data remains a challenge. Open-source initiatives provide a solution by enabling collaborative dataset pipelines for AI-driven network optimization. This presentation explores how open-source tools can facilitate data aggregation, curation, and annotation while ensuring security and compliance. We will also discuss AI-RAN’s role in synthetic data generation and global AI governance. By leveraging open-source methodologies, telecom stakeholders can accelerate AI model training and drive next-generation AI-powered networks.

### AI - Lessons Learnt from World's Largest Network - Dr. Junlan Feng, China Mobile Research Institute
Speakers: Dr. Junlan Feng Chair and General Manager of AI and Intelligent, Operation R&D Center, China Mobile Research Institute Dr. Junlan Feng, Chief Scientist at China Mobile, General Manager of AI and Intelligent Operation R&D Center. Dr. Feng has led R&D of China Mobile on artificial intelligence and big data since September 2013. She had been the architect of IBM Big Data from January 2013.1 to August... Read More →
page: https://onesummit2025.sched.com/event/1vmdQ/ai-lessons-learnt-from-worlds-largest-network-dr-junlan-feng-china-mobile-research-institute
Lessons learnt from the AI journey at world's largest Service Provider. From Intent Based to Automated Networks China Mobile has been in the forefront of Open Technology Adoption. Session explores lessons from their AI journey.

### An Industry Analyst's Perspective on Telco Cloud - Christoforos Sarantopoulos, James Crawshaw & Inderpreet Kaur, Omdia
Speakers: Christoforos Sarantopoulos Senior Analyst, Omdia Christoforos is a senior analyst who specializes in telco cloud and network automation. His main field of research is the implementation of orchestration and automation in telco networks.Before joining Omdia, Christoforos worked as a network designer for BT, designing network monitoring... Read More → James Crawshaw Principal Analyst, Omdia James leads Omdia’s service provider transformation team, which covers telco IT (operations support systems, business support systems, and analytics) and telco cloud & automation (software-defined networking, network function virtualization, etc.). James’ own research focuses on operations... Read More → Inderpreet Kaur Senior Analyst, Omdia Inderpreet is Omdia’s Senior Analyst for telco cloud. Her research focuses on communications service providers’ (CSP) adoption of cloud computing and relevant technologies across fixed and mobile network infrastructure. She tracks and monitors key providers across the network domain... Read More →
page: https://onesummit2025.sched.com/event/1vmdT/an-industry-analysts-perspective-on-telco-cloud-christoforos-sarantopoulos-james-crawshaw-inderpreet-kaur-omdia
Omdia analysts have been following the evolution of Telco Cloud from the early days of NFV through to the cloudification of 5G packet core and experiments with softwarizing other network functions. This presentation will provide an overview of the key trends in telco cloud including managing the operational complexity, architectural choices to improve resource utilization, the importance of CI/CD, and integrating AI into telco cloud operations and network management. We will provide recommendations for service providers around reskilling, data governance and CI/CD. We will also provide advice for vendors such as how they can help telcos to adopt open-source technology and adopt a common framework for automation.

### Edge AI: The $100 billion + Opportunity - Tilly Gilbert, STL Partners
Speakers: Tilly Gilbert Director, Consulting & Edge Practice Lead, STL Partners As a Director in STL's consulting business Tilly has more than five years of experience leading growth projects for technology and telecoms firms. She heads up our research and consulting practice focused on edge and cloud computing and was nominated for Edge Computing Woman of the... Read More →
page: https://onesummit2025.sched.com/event/1vmdW/edge-ai-the-100-billion-+-opportunity-tilly-gilbert-stl-partners
The huge wave of AI has accelerated demand for cloud, but it has also triggered questions on whether deploying in centralised environments is always suitable, or if enterprises should instead consider the edge. Our edge AI forecast identifies the value of this opportunity, pointing to the use cases and the verticals that are driving growth, and determining the extent to which AI will stimulate more revenue at the edge.

### InstantX: Vodafone's Edge Innovation for the Future of Telco - Sampada Basarkar, Vodafone
Speakers: Sampada Basarkar Executive Director of Products and Platform Engineering, Vodafone Sampada Basarkar is an Executive Director of Products and Platform Engineering in Vodafone Business. She is a senior executive with a passion for building high-performing teams and delivering results in complex and high-ambiguity environments. Focused on vision, execution, and operational... Read More →
page: https://onesummit2025.sched.com/event/1vmdZ/instantx-vodafones-edge-innovation-for-the-future-of-telco-sampada-basarkar-vodafone
As telco networks evolve to meet the demands of 5G, IoT, and AI-driven applications, edge computing has become a critical enabler of real-time, high-performance services. Vodafone's InstantX platform has been at the forefront of this transformation, powering scalable V2X and A2X communication enabling intelligent edge solutions. In this keynote,  I will explore how InstantX is setting new avenue for openness, automation, and performance at the edge. We'll discuss why Vodafone is insourcing this technology into the open-source community, the challenges we overcame, and how InstantX is poised to drive the next wave of innovation in edge computing. Join us as we build the future of telco-together, in the open.

### Network Infrastructure to APIs - How Open Source Enables Speed of Innovation and Monetization - Nathan Rader & Sebastian Zechlin, Deutsche Telekom
Speakers: Nathan Radar VP Service and Capability Exposure, Deutsche Telekom Sebastian Zechlin Lead Architect OSS, Deutsche Telekom Sebastian Zechlin is Head of OSS Architecture & Innovation at Deutsche Telekom. He is based in Bonn, Germany. After graduating in Computer Science from the Technical University of Braunschweig, Sebastian has worked in the telecommunications industry for 15 years. At Deutsche Telekom... Read More →
page: https://onesummit2025.sched.com/event/1vmdc/network-infrastructure-to-apis-how-open-source-enables-speed-of-innovation-and-monetization-nathan-rader-sebastian-zechlin-deutsche-telekom
Session covers DT's vision of a fully open network enabled by open source projects in infrastructure to APIs including CAMARA resulting in speed of innovation, lower cost and monetization of assets. It covers the successfull journey and provides a roadmap for the community to build off.

### IOWN Global Forum and Open Source - Key Enablers for Next Decade - Masahisa Kawashima, NTT Corporation
Speakers: Masahisa Kawashima IOWN Technology Director, IOWN Development Office, R&D Planning Department, NTT Masahisa Kawashima is currently leading NTT's R&D of Innovative Optical and Wireless Network (IOWN) as the IOWN Technology Director. He is also serving as the Chair of the Technology Working Group at IOWN Global Forum. He has been working as a bridge between technologies and businesses... Read More →
page: https://onesummit2025.sched.com/event/1vmdf/iown-global-forum-and-open-source-key-enablers-for-next-decade-masahisa-kawashima-ntt-corporation
IOWN Global Forum is working to accelerate the development of integrated photonic network architecture, now partnering with Open Source communities like LFN, LF Edge, OPI and more. Together, the organizations are working to create a smarter, more connected world. Learn how the latest progress and roadmap on how open source software is being integrated into the IOWN platform for comprehensive and accessible next-generation infrastructure for future use cases and business impacts.

### Standards and Open Source Harmonization - Silvia Almagia, ETSI; Hui Deng, Huawei; Raúl Álvarez, Open Compute Project Foundation; Moderated by Arpit Joshipura, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation
page: https://onesummit2025.sched.com/event/1vmdi/standards-and-open-source-harmonization-silvia-almagia-etsi-hui-deng-huawei-raul-alvarez-open-compute-project-foundation-moderated-by-arpit-joshipura-the-linux-foundation
Harmonizing Standards and Open Source was a vision laid out over 5 years ago. See the progress and upcoming requirements in the world of Cloud Native, Green, AI and more, featuring leadership from ETSI, NGMN and Open Compute Project.

### SONiC: The Global Networking Operating System for All - Michael Ma, Microsoft & Peter Plak, Dell
Speakers: Peter Plak Networking Sales Engineering Lead, Netherlands, Belgium, and Luxembourg, Dell Peter Plak is an accomplished leader with over 20 years of experience in Networking Sales Engineering, currently overseeing the Netherlands, Belgium, and Luxembourg regions. Throughout his career, Peter has built a deep expertise in networking technologies, driving innovative solutions... Read More → Michael Ma Principal SDE Manager, Microsoft Michael Ma is a Principal Software Engineer Manager in Microsoft Azure Networking team, driving the effort of accelerating Azure network device update through container related technologies. Previously he worked in Microsoft, AliCloud and Databricks for 18 years, focusing on the cloud... Read More →
page: https://onesummit2025.sched.com/event/1xg29/sonic-the-global-networking-operating-system-for-all-michael-ma-microsoft-peter-plak-dell
SONiC is the most advanced open source network operating system, driving global adoption with its modular, scalable, and hardware-agnostic architecture. Join this session to hear the latest updates on SONiC’s evolution and what’s next for the community.

### AI 101 for Networking & Edge - Fatih Nar, Red Hat & Ranny Haiby, The Linux Foundation
Speakers: Fatih E. Nar Distinguished Chief Architect, Red Hat Fatih E. Nar has built a career solving complex challenges across telecom, media, and entertainment, with roles at Google, Verizon, Canonical, Ericsson, and now Red Hat. He specializes in cloud-native and AI-driven solutions for enterprises and service providers, blending AI, cloud... Read More → Ranny Haiby CTO Networking, Edge and Access, The Linux Foundation
page: https://onesummit2025.sched.com/event/1wTZR/ai-101-for-networking-edge-fatih-nar-red-hat-ranny-haiby-the-linux-foundation
This session will provide a quick tutorial on the latest buzzwords related to AI. It will then explain how all these technologies are applicable to networking. An experimental Telco AI project will be referenced as an example to highlight how theory can be put into practice.

### Sponsored Session: AI Frameworks for Networking and Responsible AI - Sreekanth Sasidharan, Infosys
Speakers: Sreekanth Sasidharan AVP and Technology Head of Network Engineering Services, Infosys Sreekanth Sasidharan is currently the Unit Technology Officer & Associate Vice President at Infosys, leading its Network & Communication Engineering Technology practice globally. In this role, he is responsible for the technology, architecture, consultancy, partnerships and innovation... Read More →
page: https://onesummit2025.sched.com/event/1xg3D/sponsored-session-ai-frameworks-for-networking-and-responsible-ai-sreekanth-sasidharan-infosys
Operators and vendors are building networking AI applications but the lack of a common framework and trustworthy models have been slowing down adoption. This session will present a new open framework for networking AI that will serve as an accelerator and enable efficient development and quick time to market. An additional platform for deploying AI guardrails removes barriers for deploying AI applications and increases their trustworthiness.

### Spotlight on Innovation: The Latest Developments Shaping Open Source Networking - Olaf Renner, Nokia; Lingli Deng, China Mobile; Ciaran Johnston, Ericsson; Ranny Haiby, The Linux Foundation
Speakers: Lingli Deng Director Researcher, China Mobile Research Institute Lingli Deng, is a director researcher of China Mobile Research Institute, whose major internal responsibilities include supporting top-level design and construction practice of China Mobile's autonomous network vision, by industry standard formulation and open source collaboration... Read More → Olaf Renner Senior Specialist Open Source, Nokia Olaf Renner is working as a Senior Expert in Nokia Open Source Program Office and acts a chairman of the LFN Technical Advisory Council. Being in the telecommunications industry for 17+ years in various roles in research, standardization and open source his focus is on networking... Read More → Ciaran Johnston Software Architect at Ericsson, Ericsson Ciaran is a senior expert in Operations Support Systems (OSS) and programmable network architecture, and the chief architect for Ericsson’s network management portfolio with responsibility for architecture governance and evolution. He represents Ericsson on the Nephio TSC and is actively... Read More → Ranny Haiby CTO Networking, Edge and Access, The Linux Foundation
page: https://onesummit2025.sched.com/event/1vqSg/spotlight-on-innovation-the-latest-developments-shaping-open-source-networking-olaf-renner-nokia-lingli-deng-china-mobile-ciaran-johnston-ericsson-ranny-haiby-the-linux-foundation
A conversation with community leaders about the state of innovation in open source networking. Our panelists will discuss how they see the current and future of open source networking, what are the opprotunities and some of the chllenges that lie ahead.

### Sponsored Session: Ready for Impact: EVE Steps from 10k Kubernetes Clusters to Edge AI - Erik Nordmark, ZEDEDA
Speakers: Erik Nordmark CTO and Co-Founder, ZEDEDA Erik is a co-founder and the CTO at edge orchestration company ZEDEDA, and he is an expert on architecting and implementing secure large scale software systems, with a deep understanding of the implications of the Internet on system design. Prior to co-founding ZEDEDA he was developing... Read More →
page: https://onesummit2025.sched.com/event/1w8QU/sponsored-session-ready-for-impact-eve-steps-from-10k-kubernetes-clusters-to-edge-ai-erik-nordmark-zededa
EVE, the open source operating system built for the distributed edge, recently progressed to the Impact Stage within LF Edge, driven by its growing maturity and widespread adoption across industries. Today EVE is used to run more than 10k single-node Kubernetes clusters and VMs in production and is becoming the standard for edge computing deployments. Now with the adoption of AI technologies accelerating edge projects, what’s next for EVE? This session will examine how the project is working to further enable AI inference at the edge, including the workflows and integrations required. We’ll also discuss new efforts driving increased resiliency. Finally, learn about new EVE capabilities and how to get involved.

### A Journey Towards Automated Telco Cloud - Mesut Soytürk, Odine Labs & Salih Bilge Cihan, Turkcell
Speakers: Mesut Soytürk Cloud, Virtualization & Orchestration Director, Odine Labs Cloud, Virtualization & Orchestration Director at Odine Labs, two decades of leadership in telecommunications, software development, and project management. My career spans large-scale R&D initiatives as well as hands-on roles as a project manager, product manager, and software architect... Read More → Salih Bilge Cihan Lead Telco Cloud Engineer, Turkcell Salih Bilge Cihan is working as a Lead Telco Cloud Engineer in Turkcell Network Planning department. Having been in the Telecommunications industry for 8+ years, he has worked at Mobile Packet Core Network and Telco Cloud operation roles. Salih Bilge Cihan has graduated from Istanbu... Read More →
page: https://onesummit2025.sched.com/event/1xg45/a-journey-towards-automated-telco-cloud-mesut-soyturk-odine-labs-salih-bilge-cihan-turkcell

### LF Networking Governing Board: Ask the Experts - Dr. Junlan Feng, China Mobile Research Institute; Jonne Soininen, Nokia; Christian Olrog, Ericsson; Moderated by Arpit Joshipura, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation
page: https://onesummit2025.sched.com/event/1vmdl/lf-networking-governing-board-ask-the-experts-dr-junlan-feng-china-mobile-research-institute-jonne-soininen-nokia-christian-olrog-ericsson-moderated-by-arpit-joshipura-the-linux-foundation
LF Networking is the largest open source foundation enabling LFN as a collaboration and innnovation hub. Some of the Founding Governing Board Members will answer audience questions on past successes, current priorities and where global collaboration is heading. This is the first time members of the LFN governing board will take audience questions in this unique session called "ask me anything" so please be ready with questions to the senior most experts in our industry.

### Closing Remarks - Arpit Joshipura, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation
page: https://onesummit2025.sched.com/event/1vDtF/closing-remarks-arpit-joshipura-the-linux-foundation

