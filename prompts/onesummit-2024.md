>>> HOW TO RUN THIS <<<
This is the digest prompt for onesummit-2024. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/onesummit-2024.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/onesummit-2024.md
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

Below is the program for ONE Summit 2024. Read it and produce a digest
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
conference: ONE Summit 2024
source_url: https://onesummit2024.sched.com/list/descriptions/
generated: 2026-11-10
registry_key: onesummit-2024
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

### O-RAN-SC Workshop [Pre-Registration Required]
page: https://onesummit2024.sched.com/event/1bfAa/o-ran-sc-workshop-pre-registration-required
Registration Cost: Complimentary O-RAN-SC is organizing a workshop, as a co-located event, at the ONE Summit 2024. You will find all the details about this workshop here . This workshop focuses on how O-RAN-SC, in collaboration with other open-source initiatives such as OAI, Nephio, ONAP, etc, is building open source reference designs, which are great enablers for any new and cutting edge technology like O-RAN. Reference designs not only provide the possibility for early-stage continuous deployment and testing, but also serve as references during product development, thus accelerating commercialization. View the Agenda How to Register: Pre-registration is required as space is limited. Add the O-RAN SC Workshop to your ONE Summit registration. Have questions about the event? Contact [email protected] .

### SONiC Workshop [Additional Fee; Pre-Registration Required]
page: https://onesummit2024.sched.com/event/1Ydb4/sonic-workshop-additional-fee-pre-registration-required
Registration Cost: $15 The SONiC Foundation would like to invite you to participate in our upcoming SONiC Workshop, a co-located event at the ONE Summit on April 29, 2024. Come learn about the latest developments of SONiC from industry experts including innovations in NOS management, improvements in routing, software-defined networking, and system design. View the Agenda How to Register: Pre-registration is requested as space is limited. Add the SONiC Workshop to your ONE Summit registration. Have questions about the event? Contact [email protected] .

### Keynote: Welcome & Opening Remarks - Arpit Joshipura, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation
page: https://onesummit2024.sched.com/event/1ZLD3/keynote-welcome-opening-remarks-arpit-joshipura-the-linux-foundation

### Keynote: A Decade of Innovation - Past, Present and Future - Radia Perlman, Dell EMC; Jan Uddenfeldt, jUTechnology; Martin Casado - Andreessen Horowitz; Moderated by Arpit Joshipura, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation
page: https://onesummit2024.sched.com/event/1ZLDp/keynote-a-decade-of-innovation-past-present-and-future-radia-perlman-dell-emc-jan-uddenfeldt-jutechnology-martin-casado-andreessen-horowitz-moderated-by-arpit-joshipura-the-linux-foundation

### Keynote: Leveraging Open Source for Operational Excellence at Scale - Dave Temkin, Walmart
Speakers: Dave Temkin VP of Platform Infrastructure and Critical Facilities, Walmart As the Vice President of Platform Infrastructure at Walmart, Dave is responsible for networks, data centers, and supporting infrastructure. Previously, Dave assembled and led the team that built the world's largest Content Delivery Network, for Netflix, as well as its global studio... Read More →
page: https://onesummit2024.sched.com/event/1ahF5/keynote-leveraging-open-source-for-operational-excellence-at-scale-dave-temkin-walmart

### Keynote: Powering The Industrial Edge with Open Source Software - Michael Maxey, ZEDEDA & Jim Teal, Rockwell Automation
Speakers: Michael Maxey VP of Business Development and LF Edge Board Member, ZEDEDA Michael Maxey is the VP of Business Development at ZEDEDA, where he focuses on building and executing go-to-market (GTM) strategies with customers and partners. Maxey is also an LF Edge Governing Board Member, helping drive efforts around standardization, developer recommendations... Read More → Jim Teal Director, System Architecture Cloud & Edge, Rockwell Automation
page: https://onesummit2024.sched.com/event/1bmbo/keynote-powering-the-industrial-edge-with-open-source-software-michael-maxey-zededa-jim-teal-rockwell-automation
Rockwell Automation and ZEDEDA will illuminate best practices for industrial edge deployments, focusing on balancing the robustness required by OT with the adaptability favored by IT. This keynote spotlights how AI integration transforms edge computing into a powerhouse of predictive analytics and real-time data processing. The presenters will delve into the strategic advantage of open-source software, emphasizing how its collaborative nature not only accelerates development but also catalyzes community-driven progress. Learn how Rockwell Automation and ZEDEDA demonstrate a unified commitment to propelling the industrial sector toward a more connected and intelligent future.

### Keynote: Future of Networks: AI-Driven Network Transformation - Ankur Jain & Kandan Kathirvel, Google Cloud
Speakers: Ankur Jain Vice President, Google Cloud Ankur Jain is a Google Vice President responsible for Google Cloud’s Telecommunications Industry and product development for Google Distributed Cloud. In his current role, he heads the Engineering, Product Management, Solutions and Partnerships teams.Before this, Ankur was working... Read More → Kandan Kathirvel Group Product Manager, Google Cloud Kandan Kathirvel is a Product Management executive with over 20 years of experience in Cloud Automation, Edge, and AI infrastructure for telecommunications and various industries. Kandan currently leads his product management team at Google Cloud, where he and his product management... Read More →
page: https://onesummit2024.sched.com/event/1YVDe/keynote-future-of-networks-ai-driven-network-transformation-ankur-jain-kandan-kathirvel-google-cloud
CSPs are currently transitioning their networks towards hybrid deployments and automated operating models using cloud native architecture. By integrating AI into the core of these architectures, combined with an intent-based approach to automation like Nephio, we can transform network design, deployment, and operations. Join us for this keynote presentation and demo where we will share our perspective on the next generation of AI-native networks, drawing on our real-life experience managing a planet-scale network.

### Keynote: AI and Open Networking - Dr. Junlan Feng, China Mobile Research Institute
Speakers: Dr. Junlan Feng Chair and General Manager of AI and Intelligent, Operation R&D Center, China Mobile Research Institute Dr. Junlan Feng, Chief Scientist at China Mobile, General Manager of AI and Intelligent Operation R&D Center. Dr. Feng has led R&D of China Mobile on artificial intelligence and big data since September 2013. She had been the architect of IBM Big Data from January 2013.1 to August... Read More →
page: https://onesummit2024.sched.com/event/1aVPp/keynote-ai-and-open-networking-dr-junlan-feng-china-mobile-research-institute

### Sponsor Showcase
page: https://onesummit2024.sched.com/event/1aR4G/sponsor-showcase
The showcase will be closed during lunch from 12:40 - 2:00 pm.

### Introduction to Photonic Disaggregated Computing Architecture - Shigeru Kotabe, Fujitsu
Speakers: Shigeru Kotabe Leading Researcher, Fujitsu Shigeru Kotabe is a leading researcher for AI deployment infrastructure in Fujitsu. He has been involved in L2/L3 firmware/software development for over 10 years, and in last decade, has focused on AI-related development, serving as a leading researcher. Leveraging these experiences... Read More →
page: https://onesummit2024.sched.com/event/1bmNm/introduction-to-photonic-disaggregated-computing-architecture-shigeru-kotabe-fujitsu
The continued expansion of high-speed networks has great potential to create new value by tapping into the enormous amount of data available from interconnected endpoints. Increased computing power is required to process and analyze an unprecedented volume of data, with more accuracy and granularity than ever before, coming from the vast number of sensors and other data sources. Conventional computer architectures would require a large number of computing devices, leading to greatly increased in power consumption. Instead, we propose a photonic disaggregated computing architecture. The architecture has three key features: reconfigurable devices for flexible hardware allocation, device to device communication to reduce CPU loads, and direct photonic connections between devices. In this talk, we will describe the proposed architecture and use cases.

### Lessons Learned from Using Nephio to Manage a Real-World 5G Core - István Kispál, Nokia
Speakers: Istvan Kispal Automation Architect, DMTS, Nokia Istvan is a senior researcher and a Distinguished Member of Technical Staff in Nokia Bell Labs with 10+ years of experience in telco research. His main research focus is in cloud-native telco network automation.
page: https://onesummit2024.sched.com/event/1YUqx/lessons-learned-from-using-nephio-to-manage-a-real-world-5g-core-istvan-kispal-nokia
A case study on how we used the open source implementation of Nephio Release 2 to deploy and operate a Nokia 5G Core, that is identical to a commercial offer, on AWS. I will explain how we described the topology of Network Functions by a generic, target environment-agnostic blueprint and how we transformed this by a cooperation of automated processes and human engineers to an AWS and Nokia-specific deployment package that we eventually deployed to AWS using a GitOps tool. I will discuss how the Nephio approach is novel compared to other orchestration tools, and also what are the elements of Nephio Release 2 that we had to change in order to be able to handle this particular real-world scenario.

### Fortifying the Security of Telco Open Source Projects - Georg Kunz & Toine Siebelink, Ericsson
Speakers: Georg Kunz Director Open Source, Ericsson Georg is an Open Source advocate and a long-term contributor to a wide range of open source communities and projects in LF Networking and beyond, such as OpenStack, OPNFV/Anuket, and OpenSSF. He served for multiple terms on the Anuket Technical Steering Committee and currently serves... Read More → Toine Siebelink Developer, Ericsson Toine is a master engineer over 20 years with in Ericsson Ireland as a developer on many large telecommunication software projects. Since 4 years Toine has joined Ericsson Software Technology to work on open source in ONAP as the PTL for the Configuration Persistence Project. Toine... Read More →
page: https://onesummit2024.sched.com/event/1YUr0/fortifying-the-security-of-telco-open-source-projects-georg-kunz-toine-siebelink-ericsson
Open Source Software is the foundation for today's digital society, and thus security and sustainability have become top priorities for the telco community. Securing the open source software ecosystem is challenging due to its vast size and heterogeneity. So, the only feasible - and sustainable - path forward is a collaborative effort, jointly between the creators of open source software and their users. The Open Source Security Foundation (OpenSSF) is a Linux Foundation initiative to facilitate exactly this. In this presentation, Georg and Toine will showcase how the telco open source community can secure its critical open source projects. They will share their experiences, the results, and the lessons learned from applying OpenSSF best practices and tools to selected projects. Georg will report on how the OpenSSF Scorecard tool was used to guide open source developers in improving their project's security posture. Toine will then describe the efforts and challenges of assessing and complying with the OpenSSF criteria, which resulted in obtaining the OpenSSF Best Practices Gold Badge for the ONAP CPS project.

### Towards a New Era of Edge Computing - Open Software on Open Hardware - Tiejun Chen, VMware & Tina Tsou, LF Edge
Speakers: Tina Tsou Lead, InfiniEdge AI, LF Edge Tina Tsou is a recognized leader in open source software, cloud infrastructure, and edge computing. She has chaired the Kubernetes Edge Day events under the Cloud Native Computing Foundation (CNCF) and served as the Board Chair of LF Edge. Tina has held significant roles, including... Read More → Tiejun Chen Individual Contributor, Individual Contributor Tiejun Chen is a seasoned technical leader. He is one RISC-V Ambassador of RISC-V International, and ever worked at several tech companies such as VMware, Intel, Wind River Systems and so on, involved in - cloud native, RISC-V, edge computing, ML/AI, etc. He joined to share many presentations... Read More →
page: https://onesummit2024.sched.com/event/1YUr3/towards-a-new-era-of-edge-computing-open-software-on-open-hardware-tiejun-chen-vmware-tina-tsou-lf-edge
The surge of edge computing is propelled by an increase in edge applications and devices, highlighting the benefits of low latency, enhanced security, and real-time responses. LF Edge, is aiming to establish an open, interoperable software framework for edge computing, independent of hardware, silicon, cloud, or operating system. Meanwhile, open-source hardware platforms are gaining ground in IoT and embedded systems, furthering the expansion of edge computing. This blend of open software and hardware can herald a new era of edge computing - Open Software on Open Hardware. While promising to expedite the adoption of edge computing, it also introduces new challenges within the edge ecosystem. We'd like to discuss the future of this open edge platform, including its current state, benefits, challenges, and problems. We also need to determine the direction for the edge community in embracing new technologies like WebAssembly, developing potential solutions, running edge-native applications, and empowering edge use cases like edge AI. Let's explore this exciting new era of open edge platforms together.

### Applying AI/ML Methods to Diagnose Network Issues Using Telemetry Data - Frank Brockners, Cisco
Speakers: Frank Brockners Distinguished Engineer, Cisco Frank is Distinguished Engineer in Cisco's Outshift/CTO division, driving software and architecture development for network AI/ML related solutions. He is involved in several open source projects and is a Linux Foundation Networking (LFN) board member. Frank is an active IETF member... Read More →
page: https://onesummit2024.sched.com/event/1YUr6/applying-aiml-methods-to-diagnose-network-issues-using-telemetry-data-frank-brockners-cisco
Troubleshooting remains largely a manual process, with substantial time devoted to diagnosing issues. This session explores how AI/ML can expedite initial diagnoses. It delves into the suitability of various AI/ML techniques for network data and different phases of analysis, such as problem identification and diagnosis. Using real-world telemetry data as a foundation, we will collectively examine and demonstrate the use of diverse AI/ML approaches, including large language models, to pinpoint and diagnose issues. Concurrently, we will discuss the advantages and drawbacks of the various technologies employed.

### Nephio & Gen AI: Empowering Efficiency in 5G/O-RAN and Beyond - Sana Tariq, Telus Canada; Alexis de Talhouët & Bala Varadaraju, Red Hat
Speakers: Sana Tariq Principal Architect - Cloud and Service Orchestration, Telus Canada Sana Tariq, Ph.D. in Computer Science and Fulbright alum, brings 15 years of telecom expertise. As TELUS's Principal Architect, shaping 5G and O-RAN automation architecture. A pioneer in cloud-native adoption through DevOps and open source, she leads initiatives with NGMN, LFN, and... Read More → Alexis de Talhouët Telco Solutions Architect, Red Hat Alexis is a Solutions Architect at Red Hat, specializing in architecting innovative solutions for telecommunication providers. With a strong background in infrastructure, development and network automation, he brings a unique blend of skills to design and implement cloud-based solutions... Read More → BV Bala Varadaraju Red Hat
page: https://onesummit2024.sched.com/event/1YUrK/nephio-gen-ai-empowering-efficiency-in-5go-ran-and-beyond-sana-tariq-telus-canada-alexis-de-talhouet-bala-varadaraju-red-hat
Nephio revolutionizes cloud-native network automation as an intent-driven 5G platform. Emphasizing simplicity and efficiency, Nephio seamlessly integrates any network functions i.e., 5G, and O-RAN components, relying on the Kubernetes Resource Model and controllers as fundamental elements. Its intent-driven methodology ensures dynamic resource allocation, reducing manual intervention and aligning network operations with GitOps principles. In this presentation, we will explore Nephio's vision in supporting cloud-native automation, the current state of Nephio, and integration within the O-RAN architecture, outlining the roadmap for O-RAN implementation in the platform. Demonstrating Nephio's capabilities, we'll showcase its proficiency in managing infrastructure and network functions throughout its lifecycle. We will also share Nephio’s vision in leveraging GenAI capabilities in closed-loop operations that derive simplicity. This involves leveraging commercial Kubernetes infrastructure and incorporating Open Source O-RAN Network Functions provided by the OpenAirInterface Software Alliance.

### How to Convince Your Security Team That Your AI App Is Secure Enough for the Edge - Erik Nordmark, ZEDEDA
Speakers: Erik Nordmark CTO and Co-Founder, ZEDEDA Erik is a co-founder and the CTO at edge orchestration company ZEDEDA, and he is an expert on architecting and implementing secure large scale software systems, with a deep understanding of the implications of the Internet on system design. Prior to co-founding ZEDEDA he was developing... Read More →
page: https://onesummit2024.sched.com/event/1YUrB/how-to-convince-your-security-team-that-your-ai-app-is-secure-enough-for-the-edge-erik-nordmark-zededa
While you’re trying to get your AI app to work with flakey connectivity on an edge server with no UPS, you may hear annoying security questions. As edge projects take off, developers must deal with challenges unique from the cloud or data center. How do we build a security framework if there is no secure perimeter & we can’t trust hardware, software, or users? How can basic lifecycle tasks be handled with diverse hardware types at scale? How do we develop for environments that may include limitations like intermittent connectivity & low bandwidth? This session will provide tips to navigate these challenges and build a secure edge app framework. Learn about EVE-OS, a lightweight, open source OS built for the distributed edge. The flexible EVE-OS addresses common edge issues such as avoiding software & firmware attacks in the field, ensuring security & environmental consistency with unsecured or flaky network connections, and deploying & updating applications with limited bandwidth.

### Cloud Native AI Plane for 6G: Visions & Explorations in Telecom Operators - Lingli Deng, China Mobile & Hui Deng, Huawei
Speakers: Hui Deng chief standard and open source engineer, Huawei Hui DENG obtained his doctoral degree at Tsinghua University in 2002. Before 2007, he was the chief researcher in Hitachi (China) R&D Cooperation. He joined China Mobile Research in 2007 and acted as CTO of network department. He was the co-chair of IETF MIF WG, the board of director... Read More → Lingli Deng Director Researcher, China Mobile Research Institute Lingli Deng, is a director researcher of China Mobile Research Institute, whose major internal responsibilities include supporting top-level design and construction practice of China Mobile's autonomous network vision, by industry standard formulation and open source collaboration... Read More →
page: https://onesummit2024.sched.com/event/1YUrE/cloud-native-ai-plane-for-6g-visions-explorations-in-telecom-operators-lingli-deng-china-mobile-hui-deng-huawei
After plentiful of passed experience of 5G SBA, NWDAF/MDAF/AI/ML, and NFV cloud native design, a couple of pain points have been identifed which could help 6G cloud native network and AI based architecture design and evolution. In the overall logic architecture of 6G, the spatial "3-body" view, describes the objective existence form of 6G network entities, which is divided into network ontology, management orchestrator and digital twin; the “4-layer” logical view, shows the structure and organization of 6G network design, which consists of a resource and computing power layer, a routing and connection layer, a service-oriented functional layer, and an capability exposing layer; the "5-facet" functional view includes control plane, user plane, data plane, intelligence plane, and security plane. This session will share operators' conceptual visions and exploration practices on 6G, and discuss how to build a 6G network technology verification prototype system with the open source orchestration engines provided by LFN as the core, so as to accelerate the innovation of mobile communication network cloud-native architecture technology and network AI standard industry collaboration.

### Lunch - Attendees On Own
page: https://onesummit2024.sched.com/event/1YVDs/lunch-attendees-on-own
The showcase will be closed during lunch from 12:40 - 2:00 pm.

### Harnessing Observability with AI for Edge Applications: Innovations in APM/T - Fatih E. Nar, Red Hat
Speakers: Fatih E. Nar Distinguished Chief Architect, Red Hat Fatih E. Nar has built a career solving complex challenges across telecom, media, and entertainment, with roles at Google, Verizon, Canonical, Ericsson, and now Red Hat. He specializes in cloud-native and AI-driven solutions for enterprises and service providers, blending AI, cloud... Read More →
page: https://onesummit2024.sched.com/event/1YUrT/harnessing-observability-with-ai-for-edge-applications-innovations-in-apmt-fatih-e-nar-red-hat
We will delve into the cutting-edge advancements in AI infused Application Performance Monitoring and Tracing (APM/T) for edge computing applications, focusing on the integration of Extended Berkeley Packet Filter (eBPF) and Large Language Models (LLM).

### SDN Journey in Verizon: Experiences, Challenges and Path Forward - Yueping Zhang & Sanjay Nayak, Verizon
Speakers: Yueping Zhang Associate Fellow, Verizon Associate Fellow for SDN Technology and Planning at Verizon. Responsible for the Verizon Software Defined Networking (SDN) architecture. Led the design, implementation and deployment of the Verizon SDN solution covering the Plan, Build and Run of Verizon’s global network. Drove Verizon... Read More → SN Sanjay Nayak Assoc Director Software architecture & development, Verizon
page: https://onesummit2024.sched.com/event/1YUr8/sdn-journey-in-verizon-experiences-challenges-and-path-forward-yueping-zhang-sanjay-nayak-verizon
Software Defined Networking (SDN) has been widely adopted by the industry due to its compelling value proposition. At the same time, it has also evolved into a large suite of disjoint point solutions. It becomes progressively unclear how the SDN promises can be fulfilled in a systemic and coherent way. Verizon embraced a full SDN approach in the greenfield deployment of Intelligent Edge Network (iEN). In this presentation, we start by sharing our experiences in developing, deploying and scaling iEN to tens of thousands of network elements, the challenges we are facing in the fast-growing 5G networks, and the evolution path we paved for the future. Then, we present Verizon’s approach to build a flexible and fungible network factory that can adapt to business dynamics and accelerate innovations. In particular, we will present the evolution of Verizon SDN controller from a monolithic OpenDayLight-based software package to a fully decoupled microservice-based architecture. We finally conclude with Verizon's SDN ecosystem vision and extend to the operators, vendors and open-source communities an open invitation to participate in this initiative and drive for collective success.

### How Open Programmable Infrastructure (OPI) Improves Portability of Cloud & Data Center Applications - Paul Pindell, F5
Speakers: Paul Pindell Principal Architect, F5 Networks
page: https://onesummit2024.sched.com/event/1YUrN/how-open-programmable-infrastructure-opi-improves-portability-of-cloud-data-center-applications-paul-pindell-f5
Open Programmable Infrastructure (OPI) Project recently debuted an end to end demo that features initial provisioning of DPU/IPUs utilizing the sZTP framework that has been adopted by the project. Once a card is provisioned, the demo will show the installation of an OS/container platform upon the card along with the installation and configuration of an infrastructure workload. In the first end to end use case that Infrastructure workload is the Nginx Open source version of a proxy. The demo will show traffic being proxied through the DPU without it ever touching the host into which the DPU/IPU is installed. This session will be a description of the OPI Project capabilities and benefits in this use case. It will also be a retrospective into the challenges and solutions found during the process to enhance the OPI project offerings.

### The Impact of Interoperable Network APIs - Mahesh Chapalamadugu, Verizon
Speakers: Mahesh Chapalamadugu Distinguished Engineer, Verizon Mahesh is focused on the 5G edge computing and interoperable Network API ecosystem. He also represents Verizon at other global telco bodies like Linux Foundation’s CAMARA Project where he sits on the Technical Steering Committee and End User Council.
page: https://onesummit2024.sched.com/event/1YUrQ/the-impact-of-interoperable-network-apis-mahesh-chapalamadugu-verizon
This talk showcases the impact of interoperable network APIs on cutting edge 5G use cases. This session will dive into two demonstrations Verizon conducted in 2023 and their technical architecture. Developers will understand real-life use cases that are being fueled by the Open Network APIs and the future of the ecosystem. One demo hosted a world's first experience, showcasing the impact of 5G and Edge Compute on a remote music collaboration use case. Using the Edge Discovery API, which enables devices to identify and connect to the Mobile Edge Compute (MEC) site providing the lowest latency closest to them, syncing guitar players across USA (Verizon), Canada (Rogers), and England (Vodafone). The second demo showcased a first ever transatlantic real time 5G holographic meeting, connecting multiple people across continents as holograms. The EDS API amplified the product performance, enhancing holographic experience.

### Running Complex Network Function Workloads with Nephio - Ciaran Johnston, Ericsson & Stephen Wong, Google
Speakers: Stephen Wong Software Engineer, Google Stephen Wong has over ten years of open source contribution experiences. He was co-creator of project Nephio, a cloud native network automation project under LFN. Previously, He was the PTL of OPNFV Clover, which utilizes cloud native related projects for NFV use cases. He also co-founded... Read More → Ciaran Johnston Software Architect at Ericsson, Ericsson Ciaran is a senior expert in Operations Support Systems (OSS) and programmable network architecture, and the chief architect for Ericsson’s network management portfolio with responsibility for architecture governance and evolution. He represents Ericsson on the Nephio TSC and is actively... Read More →
page: https://onesummit2024.sched.com/event/1YUrU/running-complex-network-function-workloads-with-nephio-ciaran-johnston-ericsson-stephen-wong-google
Nephio’s goal is to deliver carrier-grade Kubernetes-based cloud native intent automation and common automation templates that simplify the deployment and management of multi-vendor cloud infrastructure and network functions across edge deployments. Continuous reconciliation ensures that lifecycle operations are not “fire-and-forget” as in traditional models, but desired state is continuously maintained. Gitops principles and a common packaging structure simplifies use cases that have traditionally followed siloed and often laboriously manual processes. As Nephio adoption in the telco industry widens, support for existing workloads is required. These are based on helm charts, and can be complex. The industry needs a way to support these workloads in Nephio as well as a way to easily evolve towards a pure Nephio approach. This talk will show the value that Nephio brings, through a demonstration of capabilities in LCM and the SDKs. By the end of the session, audience members will understand the effectiveness of the Nephio way of working with existing and new Network Function types, and the capability of the Nephio SDKs to simplify onboarding.

### Embracing a Data-Driven Approach to Network Automation - Jason Edelman, Network to Code
Speakers: Jason Edelman Founder and CTO, Network to Code Jason Edelman founded Network to Code in late 2014. Observing how DevOps was radically changing the IT operational models for systems administrators and developers, Jason saw an opportunity to combine existing technologies from the worlds of DevOps and software development within... Read More →
page: https://onesummit2024.sched.com/event/1YUrW/embracing-a-data-driven-approach-to-network-automation-jason-edelman-network-to-code
Network data — provided it’s clean, quality data — is the true foundation of network automation. It attacks the problem head-on and provides the path for long-term success. This session aims to explore the transformative power of a data-driven approach in streamlining network automation processes. However, the challenge is that in many environments, there is no common understanding of the full data needed to describe the current state of the network. It is usually spread across several systems — often spreadsheets and local databases — and these repositories are not documented and don't talk to each other. Through this session, attendees will gain an understanding of how the network is a stateful entity. It has a desired state, and we should define that state as a golden truth. By having the right data about the network, we can then take what the network is telling us it’s doing and compare that against the golden truth. Attendees will also understand the answers to questions such as: “How can organizations truly start to embrace network automation?” and “What should organizations be thinking about when it comes to SoT?”

### Completing OpenRan: OCP Community Delivers 1st Open 4G/5G Radio Platform, Fulfilling OpenRAN's Prom - Bijan Nowroozi, Open Compute Project Foundation
Speakers: Bijan Nowroozi CTO, Open Compute Project Foundation Bijan Nowroozi is Chief Technical Officer of Open Compute Project Foundation and has more than 28 years of experience with hardware and software development, signal processing, networking, and research with technology companies. Prior to OCP Bijan developed mission critical infrastructure... Read More →
page: https://onesummit2024.sched.com/event/1YUrZ/completing-openran-ocp-community-delivers-1st-open-4g5g-radio-platform-fulfilling-openrans-prom-bijan-nowroozi-open-compute-project-foundation
This presentation explores the transformative role of the Open Compute Project (OCP), Open RAN and Linux Foundation in reshaping 4G/5G wireless infrastructure. The OCP is working on a 4G/5G 3GPP compliant open Radio Unit with a modular, cost-effective design and a capability to enable rapid innovation to spur development of a multi-vendor supply chain. We discuss the integration of AI and its impact on radio platforms, advancing the OpenRAN concept and highlighting our experience with AI/HPC , and end to end AI/OpenRAN via open CU/DU. This presentation offers a preview of a common open platform providing an alternative to today’s proprietary ecosystem and delves into the significance of open hardware in meeting OpenRAN goals of promoting vendor neutrality, cost efficiency, and innovation in the telecom sector. We conclude by emphasizing the broader implications of open community models like the OCP and LF and others in democratizing telecom access, enhancing interoperability, and fostering sustainable and advanced development of telecom infrastructure. We close with open hardware and software, aligning with the summit's themes of innovation, efficiency, and open networking.

### Enhancing Network Stability with AI: A Novel Approach Using AI Driven Forward Erasure Coding - Fatih E. Nar, Red Hat & Peter Bech, Steinwurf
Speakers: Fatih E. Nar Distinguished Chief Architect, Red Hat Fatih E. Nar has built a career solving complex challenges across telecom, media, and entertainment, with roles at Google, Verizon, Canonical, Ericsson, and now Red Hat. He specializes in cloud-native and AI-driven solutions for enterprises and service providers, blending AI, cloud... Read More → PB Peter Bech Steinwurf
page: https://onesummit2024.sched.com/event/1YUrc/enhancing-network-stability-with-ai-a-novel-approach-using-ai-driven-forward-erasure-coding-fatih-e-nar-red-hat-peter-bech-steinwurf
This session delves into the innovative use of Artificial Intelligence (AI) in network stability, particularly emphasizing a novel approach in AI driven Forward Erasure Coding (FEC). Designed for network engineers, data scientists, and IT professionals, the presentation aims to unfold how AI can be integrated with advanced FEC techniques to significantly improve network reliability and data transmission efficiency, especially in high-loss environments.

### P4-Based Automated Reasoning - Steffen Smolka, Google
Speakers: Steffen Smolka Staff Software Engineer, Google Steffen leads the P4-Based Automated Reasoning Group (P4-BAR) at Google, a team that uses P4 as a specification language and builds and applies tools that perform automated switch validation against such a given P4 spec. He also serves as a co-chair of the P4 API Working Group and... Read More →
page: https://onesummit2024.sched.com/event/1aZuC/p4-based-automated-reasoning-steffen-smolka-google
P4 was originally designed as a language for configuring programmable network pipelines, but is gaining momentum as a specification language for network pipelines that may or may not be programmable, including at Google. I will discuss how we have been leveraging such machine-readable, unambiguous, vendor-agnostic specifications of our switches to: * Increase network reliability and development velocity through high-coverage, automated validation. * Allow our SDN controller to interoperate seamlessly with switches from different vendors, by automatically holding them accountable to the same vendor-agnostic specification.

### Anuket - More Important Than Ever - Beth Cohen, Verizon & Gergely Csatari, Nokia
Speakers: Gergely Csatari Senior Open Source Specialist, Nokia Working in the telecom industry in the last two decades it was possible for Gergely to see the evolution from vendor specific hardware to virtualisation and cloud and a to cloud native. Currently Gergely is part of the OSPO team of Nokia CTO which is reponsible for open source. In... Read More → Beth Cohen SDN Product Strategy, Verizon Beth is an Advanced Networking Product Strategist at Verizon, working on developing new SDN products and services. At Verizon, she has architected and developed several products, including Virtual Network Services, which has been driving many of the Open Source Edge projects.
page: https://onesummit2024.sched.com/event/1YUrg/anuket-more-important-than-ever-beth-cohen-verizon-gergely-csatari-nokia
The Anuket Project has been going for close to six years now, so in many ways it is an established mature project. At the same time. the entire telecom infrastructure industry is going through a massive shift as the Cloud Providers make a play for supporting telecoms on their platforms, APIs are becoming more important than ever, and the understanding of what is Cloud Native is going in many different directions. Some of the questions to be explored include: How much does CNCF need to be incorporated into Anuket Is there a place for AI and the Thoth Project? What role does infrastructure play as the CSP grow their presence? In this session leaders of the Anuket project team want to not only share Anuket's successes, but need meaningful feedback on where Anuket needs to go in the future as the industry changes.

### Network and Computing Infrastructure for the 2030s - Haruhisa Fukano & Inoue Reo, Fujitsu
Speakers: Haruhisa Fukano Manager, Promoting effective use of open communities, 1Finity Haruhisa Fukano is an architect and business planner for edge computing at 1Finity. He leads the PoC project to develop the edge computing market. He also contributes to the ecosystem and open community for the spread and evolution of edge computing. He currently serves on the Technical... Read More → Inoue Reo Network and computing infrastructure for the 2030s, Fujtisu Currently working in the field of research and development for infrastructure of 6G technology. My career has been largely centered around the development of wireless network and edge computing. Outside of work, I have a passion for marathons.
page: https://onesummit2024.sched.com/event/1YUrp/network-and-computing-infrastructure-for-the-2030s-haruhisa-fukano-inoue-reo-fujitsu
The amount of data and computation required for computing workloads is increasing at an accelerating rate, and reducing power consumption and evolving data bandwidth are becoming challenges. At the same time, fast responding time is also required. Solving these challenges and realizing future workloads in the 2030s will require a paradigm shift in communications and computing. Against this background, IOWN and LF Edge signed an MOU. IOWN(Innovative Optical and Wireless Network) Global forum are focusing on next generation communications and computing infrastructure and technology to realize future workload. LF Edge are developing software and architectures to enable our workload primarily from the edge computing side. I believe that the combination of IOWN technology and LF Edge OSS will enable future workload and improve the performance of use cases. So I'm planning a joint PoC using two community technologies. This presentation will introduce the points to be demonstrated in the PoC and future plans.

### Data Anonymization for Telco AI Use Cases - Sridhar Rao, The Linux Foundation
Speakers: Sridhar Rao Senior Architect, The Linux Foundation Sridhar received his Ph.D degree in computer science from National University of Singapore, in 2007. He has worked as Post-doctoral fellow at Microsoft Innovation Center, Politecnico Di Torino, Turin, Italy, senior researcher with NEC Technologies, as a research fellow at Institute... Read More →
page: https://onesummit2024.sched.com/event/1bRAE/data-anonymization-for-telco-ai-use-cases-sridhar-rao-the-linux-foundation
Data anonymization can help Telcos to share data to facilitate open innovation. Two big challenges to address while anonymizing Telco data for AI usecases are (a) fool-proof against de-anonymization (b) Not hamper the power (Ex: predictive, Classification) of the AI models. The talk we cover the following: (a) State of art of Data Anonymization applied to Telcos, including the research works, projects and specifications. (b) What constitutes the sensitive data (names, addresses, telco-specific fields, location-data, etc). in Telco scenarios (c) Anonymization categories such as (Suppression, Masking, Pseudonymization, Generalization, Swapping, Perturbation and Synthetic Data Generation). (d) Approaches/techniques ranging from classic (ex: K-Anonymity) to use of NLP to GANs (Generative Adversarial Networks). (e) Which of the above categories and techniques are applicable to Telco Data, considering the challenges of deanonymization and model-power. (f) Demonstration of the developed unified-anonymization tool. The talk will also include description of the libraries that can be used, demonstration of the techniques, and showcasing of the impact of anonymization on the AI models.

### Non-Minimal Path Routing for AI and Cloud Computation Networks - David Wong, Claruspon Systems, Inc.
Speakers: David Wong Founder & CEO, Claruspon Systems, Inc. David I-Keong Wong is the founder of Claruspon Systems, Inc., a Bay area company. He is the inventor and owner of several US patents in mesh networks and non-minimal path routing for data center, and a designer of datacenter switch product. He built a datacenter mini pod using datacenter... Read More →
page: https://onesummit2024.sched.com/event/1YUrl/non-minimal-path-routing-for-ai-and-cloud-computation-networks-david-wong-claruspon-systems-inc
There are several factors to drive AI networks to expand from supporting 25 thousand GPUs to 1 million GPUs, from interconnecting clusters within a datacenter to interconnecting clusters spanning across tens of datacenters, these include 1) the sustainable power that can be delivered to a single datacenter 2) the growing number of homogenous and heterogenous AI clusters and the desire to bring AI resources together to higher aggregated performance. In the 2nd half of year 2023, non-minimal path routing in Dragonfly and Dragonfly+ topologies were proposed. In this talk we analyze Clos and Mesh topologies based on a model of path diversity from network congestion point of view. We review the findings from AI workload optimization (such as the one from Meta and MIT). We also review the two facets of the non-minimal path routing on (e)BGP protocol. Finally, we come back to work on the Dragonfly and Dragonfly+ topologies with what we just learned in this talk and tentatively propose several large-scale AI networks with likely good characteristics to meet the needs of low network latency, low congestion, zero packet loss, and large bisectional bandwidth.

### Harmonising Disparate Components: Navigating Dependencies in Automated K8s Deployments - Wim Henderickx, Nokia
Speakers: Wim Hendrerickx CTO IP Division, nokia Wim is head of technology and architecture in Nokia’s IP division, where he works with partners and customers to provide consultancy advise in IP technology, Cloud and Automation. He has over 25 years of experience in the telco and enterprise communication and networking industry... Read More →
page: https://onesummit2024.sched.com/event/1YUrm/harmonising-disparate-components-navigating-dependencies-in-automated-k8s-deployments-wim-henderickx-nokia
We inhabit a world characterised by disaggregation, wherein diverse components essential for deploying a system originate from various actors (vendors/integrators/etc). A prime illustration of this scenario involves a Network Function (NF) like UPF/SMF/CU/DU, which requires deployment on a Kubernetes (k8s) cluster and exhibits dependencies on elements like the kernel, networking, software packages, and more. Complicating matters further, these diverse components are often overseen by distinct teams within an organisation. In this session, we will elucidate effective strategies for managing dependencies when dealing with multiple Kubernetes Resource Model (KRM) resources, showcasing an automated approach to streamline the process handled by various teams in an organization.

### First Steps Toward Community-Driven Edge Service Design - Colin Peters, Fujitsu
Speakers: Colin Peters Software Architect, Fujitsu Colin Peters is a software architect for edge computing at Fujitsu. He is currently leading a PoC project to expand and develop the edge computing market. He also contributes to the ecosystem and open community for the spread and evolution of edge computing. He is the Project Technical... Read More →
page: https://onesummit2024.sched.com/event/1YUri/first-steps-toward-community-driven-edge-service-design-colin-peters-fujitsu
Edge services have the potential to offer lower latency to end users and more efficient use of computing and networking resources. Creating an edge service requires expertise in a wide variety of technologies, from mobile networks, to sensors, robotics, cloud computing, and AI. This complexity can be a significant barrier for people who want to create a new service. The Edge Service Enabling Platform, or ESPF, is an open-source effort to support the creation and operation of edge services by allowing designers, operators, and infrastructure developers to collaborate, and by simplifying each contributor's view of the edge service by leveraging the expertise of the other contributors. This talk describes the first steps towards building the platform, specifically our efforts over the past year to improve the tooling available for edge service design to move towards our vision of a collaborative, modular approach.

### Kubeflow & Istio, a Perfect Match! Investigating Istio’s Role in MLOps - Nina Polshakova & Peter Jausovec, Solo.io
Speakers: Peter Jausovec Software Architect, Solo.io Peter Jausovec is a software architect at Solo.io. He has over 18 years of experience in the field of software development and technology. Peter maintains the kagent project and has been at the forefront of AI gateway and agent development at Solo. His recent work bridges traditional... Read More → Nina Polshakova Senior Principal Software Engineer, Solo.io Nina is a software engineer at Solo.io, working on AI Gateway projects. She contributes to open source projects, including Kubernetes, Istio, kagent, agentgateway, and kgateway. A CNCF Ambassador and former Kubernetes v1.33 Release Lead, she’s also a member of the Cloud Native AI... Read More →
page: https://onesummit2024.sched.com/event/1YUrs/kubeflow-istio-a-perfect-match-investigating-istios-role-in-mlops-nina-polshakova-peter-jausovec-soloio
When operating Machine Learning workflows there are many moving pieces that are required to serve ML models. When models change, it is challenging to generate the logic for shifting to a new model, while ensuring that security and resiliency is maintained. If using Kubeflow and KServe, things that need to be considered such as security, routing, and observability, are abstracted away. Under the hood, Istio is doing all the heavy lifting, handling the configuration needed for everything from security with AuthN and AuthZ policies to canary deployments. We will cover topics including: - How Istio can help with exposing existing and canary releasing newer models. - The minimum viable Istio configuration to allow for secure ML operations. - How KServe’s CRs are translated into Istio resources - Configuration for traffic mirroring, fault injection, failover, rate-limit, external authentication, and BYO wasm plugins with Istio alongside the generated Kubeflow and KServe configurations

### Real-World Network Function Chaining - Lessons Learned - Benjamin Goldstone, Dell Technologies
Speakers: Benjamin Goldstone Senior Network Engineer - Dell Technologies, Dell Technologies Ben works as a senior network engineer for Dell Technologies working with top customers to architect and deliver business critical network solutions. He has a background in networking, cybersecurity, software development, network automation, and DevOps and has worked for technology... Read More →
page: https://onesummit2024.sched.com/event/1YUrv/real-world-network-function-chaining-lessons-learned-benjamin-goldstone-dell-technologies
Building solutions on top of network hardware appliances can leave you wanting more flexibility and requiring forklift upgrades when you outrun the capacity provided. Many network providers are instead leveraging network functions running on standard compute to scale out network processing capabilities as their needs increase. Learn how we've helped real-world tier 1 service providers build out networks that leverage standards-based technologies such as Q-in-Q and VLAN translation coupled with SR-IOV to deliver this at scale to numerous customers. You'll come away with blueprints and strategies for how to build your own network function chaining platform as well as with real code examples we've open sourced to get you started.

### Code Vs. Data: Optimizing NFV Orchestration with Nephio - Tal Liron, Google
Speakers: Tal Liron Staff Engineer, Google Tal has been working in the telco orchestration space for the last decade, on a range of open source projects (Nephio, ONAP, OPEN-O, OpenStack) and open standards (TOSCA, O-RAN). At Google he is in the TNA (Telecom Network Automation) development team, which provides a supported downstream... Read More →
page: https://onesummit2024.sched.com/event/1YUrx/code-vs-data-optimizing-nfv-orchestration-with-nephio-tal-liron-google
Code is expensive and fragile. Data is plentiful and chaotic. And NFV orchestration involves automating both at scale. A rule of thumb for efficiency and responsiveness is that code should live next to the data it processes. However, the complexity of off-the-shelf large-scale compute and data platforms (“cloud”) has presented the telco industry with architectural challenges for optimization. On the one hand our systems have made hard things easy, while on the other hand they have made easy things hard. Let’s take a look at how Nephio and Kubernetes can help us reduce complexity by enabling simple, straightforward engineering decisions for the placement of code and data. We will look at the choice between management clusters vs. workload clusters, delve into the Nephio specialization pipeline and the Kubernetes operator reconciliation loop, and compare Nephio’s configuration-as-data (CaD) paradigm to the more limited capabilities of Helm charts. With Nephio, we’re essentially breaking the Helm chart apart and putting the pieces where they belong.

### ALPINE - SONiC Switchstack Simulation - Sonika Jindal & Bhagat Janarthanan, Google
Speakers: Bhagat Janarthanan Software Engineer, Google Bhagat Janarthanan leads SONiC/PINS at Google. Sonika Jindal Software Engineer, Google Working at Network Infrastructure group in Google, on the development and maintenance of software running on network switches supporting Google's datacenters.
page: https://onesummit2024.sched.com/event/1YUs0/alpine-sonic-switchstack-simulation-sonika-jindal-bhagat-janarthanan-google
Alpine is a framework for running virtual SONiC (Software for Open Networking in the Cloud) network switches. It provides a standard model for instantiating SONiC virtual switches and deploying various topologies. Alpine leverages Kubernetes to build large-scale fabrics (more than 100 virtual switches) spread across multiple worker nodes. Kubernetes is a container orchestration platform that provides a scalable and reliable way to deploy and manage containerized applications. Alpine uses Kubernetes to manage the lifecycle of virtual switches, including provisioning, initial configuration, and connectivity. Alpine provides a scalable, reliable, and cost-effective way to build and test near-production topologies. Integration with CI/CD pipelines will provide low-cost pre-submit test results. Alpine has the potential to accelerate the adoption of SONiC-based networks by making it easier for vendors to develop and deploy SONiC-based products.

### Keynote: O-RAN Alliance + Linux Foundation - Dr. Alex Jinsung Choi, Deutsche Telekom
Speakers: Dr. Alex Jinsung Choi Senior Vice President, Head of T-Labs, Deutsche Telekom Dr. Alex Jinsung Choi is Chairman of the O-RAN ALLIANCE and Senior Vice President, Group Technology and Head of T-Labs, which is the central Research & Development division of Deutsche Telekom. In addition, he is member of the Technology & Innovation management board, where he has... Read More →
page: https://onesummit2024.sched.com/event/1YVDd/keynote-o-ran-alliance-+-linux-foundation-dr-alex-jinsung-choi-deutsche-telekom

### Keynote: Türk Telekom Access Domain Evolution with SEBA - Ahmet Fethi Ayhan, Türk Telekom
Speakers: Ahmet Fethi Ayhan Senior Network Director, Türk Telekom Ahmet Fethi Ayhan joined in Türk Telekom in 1998 and he is Senior Network Director. Leading fix & mobile core & Access network planning and investment, network architecture, and operations. He started his career as ne network engineer and worked in different roles, Network Operation... Read More →
page: https://onesummit2024.sched.com/event/1bvFI/keynote-turk-telekom-access-domain-evolution-with-seba-ahmet-fethi-ayhan-turk-telekom
Türk Telekom is the first Operator deployed SEBA on live network.In my presentation,  I will explain main benefits, deployment story and future plans of SEBA for Turk Telekom.

### Keynote: Revolutionizing Connectivity: Unleashing the Potential of Network APIs - Alicia Miller, Verizon & CAMARA Project
Speakers: Alicia Miller Network API Ecosystem Development Lead & CAMARA Treasurer, Verizon & CAMARA Project Alicia Miller leads Network API Ecosystem Development within the Corporate Strategy team at Verizon, including Verizon's participation in GSMA's Open Gateway and CAMARA, where she currently serves as Treasurer. As an active participant in these global organizations, Ms. Miller is... Read More →
page: https://onesummit2024.sched.com/event/1bvFG/keynote-revolutionizing-connectivity-unleashing-the-potential-of-network-apis-alicia-miller-verizon-camara-project

### Keynote: Broadband As A Utility - Arun Bhikshesvaran, Radisys
Speakers: Arun Bhikshesvaran CEO, Radisys Arun serves as Radisys CEO where he is responsible for the vision, strategies, and execution to further Radisys’ role in transforming the telecom industry. He brings to Radisys a wide range of industry experience and a proven track record of leadership. Most recently as Chief Marketing... Read More →
page: https://onesummit2024.sched.com/event/1ccYV/keynote-broadband-as-a-utility-arun-bhikshesvaran-radisys

### Keynote: Open RAN Reference Platforms at a Crossroads - Leendert van Doorn, Qualcomm
Speakers: Leendert van Doorn Senior Vice President, Qualcomm Leendert van Doorn holds the position of Senior Vice President at Qualcomm, where he leads the Central Software Engineering (CSE) organization. In this capacity, he oversees Qualcomm's software strategy and spearheads the company's AI Software initiatives. Before that, he was a Distinguished Engineer/VP in Microsoft Azure Core team where he is best known for his work to enable ARM64 servers as first-class citizens in Microsoft Azure datacenters. He has also been working on disaggregation computing and he represented Microsoft on the... Read More →
page: https://onesummit2024.sched.com/event/1aVQC/keynote-open-ran-reference-platforms-at-a-crossroads-leendert-van-doorn-qualcomm

### Keynote: United States Government: 6G RAN and OSS Security - Thomas Rondeau, Department of Defense
Speakers: TR Thomas Rondeau P PhD
page: https://onesummit2024.sched.com/event/1aVQ0/keynote-united-states-government-6g-ran-and-oss-security-thomas-rondeau-department-of-defense

### Sponsor Showcase
page: https://onesummit2024.sched.com/event/1aR43/sponsor-showcase
The showcase will be closed during lunch from 12:40 - 2:00 pm.

### 6G Innovation Day: Goals, Objectives & Agenda - Arpit Joshipura, The Linux Foundation; Thomas Rondeau, DoD
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation Thomas Rondeau, PhD Principal Director for the FutureG Office, Department of Defense Dr. Tom Rondeau is the Principal Director for the FutureG Office for the US Department of Defense, serving in the Office of the Undersecretary of Defense for Research and Engineering (OUSD(R&E)). In this role, Dr. Rondeau is responsible for the research, funding, and execution of... Read More →
page: https://onesummit2024.sched.com/event/1cfit/6g-innovation-day-goals-objectives-agenda-arpit-joshipura-the-linux-foundation-thomas-rondeau-dod

### Zero Trust Architecture for AI Workload on Edge - Wenhui Zhang, Bytedance & Ken Lu, Intel
Speakers: Ken Lu Cloud Software Architect, Intel System Architect for confidential computing, cloud native solutions and sustainable computing; Technology Enthusiast for many industry standards like UEFI, Intel TDX; Creator for many solutions like object analytics in ROS and cloud native inference pipeline for confidential and sustainable... Read More → Wenhui Zhang Researcher/Software Engineer, Bytedance Wenhui Zhang is a Researcher/Software Engineer at Bytedance, where she has been there since 2021. She holds PhD from Penn State. Wenhui’s research interests include operating systems and runtimes, security, architecture, compiler optimization, and concurrency. Her recent work has... Read More →
page: https://onesummit2024.sched.com/event/1YUs1/zero-trust-architecture-for-ai-workload-on-edge-wenhui-zhang-bytedance-ken-lu-intel
Leveraging Intel TDX to protect AI workloads, encompassing AI models, parameters, and customer data, from three primary entities—vendors, cloud service providers, and prompt requesters—is a critical aspect of implementing a Zero Trust Architecture for AI Workloads on the Edge. Zero Trust Architecture entails the concept of validating every user and device attempting to access resources on a network, irrespective of their location. When applied to AI workloads on the Edge, Intel TDX serves as a foundational technology to ensure robust security measures. It can safeguard sensitive components such as AI models, parameters, and customer data from potential threats or unauthorized access by any involved party. By employing Intel TDX, which provides hardware-based isolation and security features, it becomes feasible to establish an environment where trust is not assumed, and every access attempt is verified and authenticated. This helps in securing the AI workload against vulnerabilities or breaches that could compromise critical data or models.

### Cloud Native YANG Mgmt - Wim Henderickx, Nokia
Speakers: Wim Hendrerickx CTO IP Division, nokia Wim is head of technology and architecture in Nokia’s IP division, where he works with partners and customers to provide consultancy advise in IP technology, Cloud and Automation. He has over 25 years of experience in the telco and enterprise communication and networking industry... Read More →
page: https://onesummit2024.sched.com/event/1YUs3/cloud-native-yang-mgmt-wim-henderickx-nokia
The session aims to describe how we can manage YANG based systems in a declarative and cloud native way. We will discuss challenges and solutions to handle multi-vendor YANG based schema systems and how we unite the world of YANG with the world of Kubernetes/KRM.

### Nimbus: Intent Driven Security Automation for Telco/5G Security - Rahul Jadhav, Accuknox
Speakers: Rahul Jadhav Cofounder, CTO, AccuKnox An avid coder, a systems engineer working on solutions involving security and performance of cloud-native tech. Contributed towards several open sources including Linux Kernel and worked closely with IETF Standards (such as ROLL, 6lo, LWIG) and Linux Foundation. Taken several projects... Read More →
page: https://onesummit2024.sched.com/event/1YUs4/nimbus-intent-driven-security-automation-for-telco5g-security-rahul-jadhav-accuknox
The talks highlights the work done in the context of NSF convergence accelerator track for 5G security. Nimbus is a Intent driven security automation operator designed for kubernetes. The aim of the talk is to explain how Security Intent is modeled, how security use-cases are templatized, and then a k8s-native design to automate generation of policy/rules from these intents in a scalable way. The talk will explain how O-RAN Threat Model was taken as input to identify the set of Intents and subsequently Nimbus operated on these Intents to provide security policies and rules in the context. The talk will also provide a demo of a security use-case handled using Intents considering Nephio as the multi-cluster orchestration solution.

### RAN-in-the-Cloud: Utilization and New Services Breakthroughs - Amar Kapadia, Aarna Networks & Shuvo Chowdhury, NVIDIA
Speakers: Amar Kapadia Co-Founder and CEO, Aarna Networks Amar Kapadia is the CEO and Co-Founder of Aarna Networks, a SaaS solutions provider that offers zero-touch edge and 5G services orchestration and management at scale. Amar has over 20 years of experience in networking, storage, server, and I/O technologies through marketing and engineering... Read More → Shuvo Chowdhury Principal Product Manager, NVIDIA Shuvo Chowdhury is responsible for building AI and 5G datacenter products and serves as Principal Product Manager at Nvidia. Prior to joining Nvidia, Shuvo worked as Director of Product Management at Casa systems and Director of Solutions at Huawei Technologies, focusing on 5G Core... Read More →
page: https://onesummit2024.sched.com/event/1YUs6/ran-in-the-cloud-utilization-and-new-services-breakthroughs-amar-kapadia-aarna-networks-shuvo-chowdhury-nvidia
Innovation across the networking stack takes many forms and the dawn of GenAI has opened up some unexpected opportunities. The RAN portion of networks constitutes the largest resource allocation (both CapEx and OpEx) for network operators and is vastly underutilized (25-50% capacity). Cloudifying the RAN as a service in multi-tenant cloud infrastructure and running it as a containerized solution alongside other applications cuts operators costs, represents a leap forward for sustainability, and perhaps most significantly, allows for the monetization of new edge applications and services, such as GenAI.

### Whole of Government Vision for Open Source and Open RAN Networking - Amanda Toman, NTIA; Richard Rouil, NIST; Dr. Sudharman K. Jayaweera, NSF; Dr. Martin Weiss, DoD; Sridhar Kowdley, DHS
Speakers: Dr. Sudharman K. Jayaweera Program Director, National Science Foundation (NSF) Dr. Sudharman K. Jayaweera is currently a Program Director at the National Science Foundation (NSF) in the Emerging Technologies section of the Division of Innovation Technology and Ecosystems in the Directorate of Technology, Innovation and Partnerships, or TIP, with responsibility... Read More → Sridhar Kowdley Technical Manager, U.S. Department of Homeland Security (DHS) Sridhar Kowdley is a Technical Manager at the U.S. Department of Homeland Security (DHS) Science and Technology Directorate Office for Interoperability and Compatibility Technology Center. With over 30 years of experience in communications and networking, he works and leads programs to help DHS... Read More → Martin Weiss Director for FutureG Applied Research, US Dept of Defense (OUSD R&E FutureG) Dr. Martin Weiss is currently the Director for FutureG Applied Research, and Technical Lead for Resilient and Open Commercial Solutions within the Office of the Under Secretary of Defense for Research and Engineering. In this capacity, Dr. Weiss oversees multiple efforts to promote FutureG applied... Read More → Amanda Toman Director Public Wireless Supply Chain Innovation Fund, National Telecommunications and Information Administration, U.S. Department of Commerce Ms. Amanda Toman is the Director for the Public Wireless Supply Chain Innovation Fund at the National Telecommunications and Information Administration within the Department of Commerce.  With over 20 years of experience in research and development in the Department of Defense, Ms... Read More → Richard Rouil Division Chief, NIST Richard Rouil is Chief of the Wireless Networks Division in the Communications Technology Laboratory at the National Institute of Standards and Technology (NIST). In his role, Dr. Rouil overseas a research portfolio ranging from channel measurement and physical layer performance to... Read More →
page: https://onesummit2024.sched.com/event/1cfiw/whole-of-government-vision-for-open-source-and-open-ran-networking-amanda-toman-ntia-richard-rouil-nist-dr-sudharman-k-jayaweera-nsf-dr-martin-weiss-dod-sridhar-kowdley-dhs

### Aether: Private 5G for Industry 4.0 - Larry Peterson, Princeton University / Systems Approach LLC
Speakers: Larry Peterson Professor Emeritus & Author, Princeton University / Systems Approach LLC Larry Peterson is Chief Architect at the Open Networking Lab, and prior to that, the Robert E. Kahn Professor of Computer Science at Princeton University, where he directed the PlanetLab Consortium. Peterson co-founded CoBlitz LLC to commercialize CDN technology developed on PlanetLab... Read More →
page: https://onesummit2024.sched.com/event/1Yai0/aether-private-5g-for-industry-40-larry-peterson-princeton-university-systems-approach-llc
Introduce the new Aether Project (moving from ONF to LF), with a focus how Aether empowers enterprises to deploy 5G on-prem, with support for local breakout. The presentation will include (1) an overview of the Aether architecture; (2) the key innovations of Aether's two major subsystems (SD-Core and SD-RAN); and (3) a description of Aether's deployment machinery (OnRamp) that makes it possible to start small and scale up to multi-site deployments.

### Automating Private 5G Network Functions and Infra with Nephio - Amar Kapadia, Aarna Networks; Soubhagya Panda, Tata Communications
Speakers: Amar Kapadia Co-Founder and CEO, Aarna Networks Amar Kapadia is the CEO and Co-Founder of Aarna Networks, a SaaS solutions provider that offers zero-touch edge and 5G services orchestration and management at scale. Amar has over 20 years of experience in networking, storage, server, and I/O technologies through marketing and engineering... Read More → SP Soubhagya Panda Director - Product Management (Private 5G and Edge computing, Tata Communications
page: https://onesummit2024.sched.com/event/1YUsC/automating-private-5g-network-functions-and-infra-with-nephio-amar-kapadia-aarna-networks-soubhagya-panda-tata-communications
Private 5G networks require end-to-end automation of Infrastructure and Network Functions that include 5G Core and RAN functions from different vendors. There may be a need to orchestrate other applications such as Computer Vision on these networks. They also need Day-N management that includes Configuration Management, among other FCAPS operations. This requires an Orchestrator that can perform Day-0 Orchestration of both Infrastructure and Network functions, and the subsequent Day-N configuration management. In this session, we will explain how LFN Nephio is ideally suited for this functionality.

### Full Stack Explicit Confidence with Project Alvarium - Trevor Conn, Dell Technologies
Speakers: Trevor Conn Distinguished Engineer, Dell Technologies Trevor Conn is a Distinguished Engineer working in the CTO Advanced Hardware Lab at Dell. Trevor has served in leadership roles for open source projects such as Project Alvarium and EdgeXFoundry. Current areas of focus and expertise include edge/IoT, Confidential Computing and platform... Read More →
page: https://onesummit2024.sched.com/event/1YUsF/full-stack-explicit-confidence-with-project-alvarium-trevor-conn-dell-technologies
Project Alvarium was the first solution for capturing immutable metadata to objectively measure and quantify "data confidence", or the level of trust one can have in application data that has been captured and handled through a distributed topology. The project has recently evolved this concept to include supporting layers of the stack such as the host, OS and CI/CD artifacts. This talk will explain how we capture and link confidence metadata through these various layers and how a confidence score can be operationalized for platform integrity outcomes such as ZeroTrust.

### DENT Features Roadmap for Disaggregated Enterprise Networks - Taskin Ucpinar, Amazon
Speakers: Taskin Ucpinar Senior TPM, Amazon Taskin Ucpinar is a Senior TPM at Amazon, where he leads and coordinates Amazon Just Walk Out Networking software development activities for next generation consumer stores, using Dent as NOS. Taskin has worked for small to large organizations, including Amazon, EdgeCore, Cisco, Symantec... Read More →
page: https://onesummit2024.sched.com/event/1YUsI/dent-features-roadmap-for-disaggregated-enterprise-networks-taskin-ucpinar-amazon
As a Linux Foundation project, Dent utilizes the Linux Kernel, switchDev and SAI, and other Linux based projects as the basis for building a new standardized enterprise network operating system without an overhead. During this presentation, we will discuss how the Dent community envisions to unify the community of Silicon Vendors, ODMs, SI, and OEMs to provide and enhance Distributed Enterprise Edge functionality, enable wider adaptation of disaggregated enterprise networks, and cover expanded use cases.

### Lunch - Attendees On Own
page: https://onesummit2024.sched.com/event/1YVDv/lunch-attendees-on-own
The showcase will be closed during lunch from 12:40 - 2:00 pm.

### 6G Innovation Day: Working Lunch - Arpit Joshipura, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation
page: https://onesummit2024.sched.com/event/1cfjK/6g-innovation-day-working-lunch-arpit-joshipura-the-linux-foundation

### 6G: Reimagining RAN through Open Innovation - Ganesh Shenbagaraman, Radisys
Speakers: Ganesh Shenbagaraman Head of Standards, Regulatory Affairs & Ecosystems, Radisys Ganesh heads Radisys' integrated solutions across wireless, wireline and media processing domains. Named in 2020 as the recipient of the Small Cell Forum Chair's Award, he leads 4G and 5G wireless product development, drives collaboration with industry partners and performs key leadership... Read More →
page: https://onesummit2024.sched.com/event/1cxCW/6g-reimagining-ran-through-open-innovation-ganesh-shenbagaraman-radisys

### 6G RAN's "Linux Kernel" - Paul Sutton, Software Radio Systems
Speakers: Paul Sutton CEO, Software Radio Systems Paul is co-founder and CEO of Software Radio Systems, the team behind the open-source srsRAN Project, now the OCUDU Project. Used in research and development by thousands of developers worldwide across government, industry and academia, the srsRAN Project became OCUDU in early 2026... Read More →
page: https://onesummit2024.sched.com/event/1cwwh/6g-rans-linux-kernel-paul-sutton-software-radio-systems

### Wireless Evolution - Phil DiGuglielmo, Jabil
Speakers: Phil DiGuglielmo R&D Director, Jabil Phil DiGuglielmo is an R&D Director in Jabil’s Wireless Engineering Organization. In his role at Jabil, Phil interacts closely with customers to understand and fulfil their product requirements and he leads design services in the areas of Software Development and Test. Phil has over... Read More →
page: https://onesummit2024.sched.com/event/1d4UK/wireless-evolution-phil-diguglielmo-jabil

### Harnessing AI for Smarter Networking: Strategies and Innovations - Tina Tsou, Lead, Arm
Speakers: Tina Tsou Lead, InfiniEdge AI, LF Edge Tina Tsou is a recognized leader in open source software, cloud infrastructure, and edge computing. She has chaired the Kubernetes Edge Day events under the Cloud Native Computing Foundation (CNCF) and served as the Board Chair of LF Edge. Tina has held significant roles, including... Read More →
page: https://onesummit2024.sched.com/event/1YUsJ/harnessing-ai-for-smarter-networking-strategies-and-innovations-tina-tsou-lead-arm
In this session, we will explore the transformative role of AI in networking. We’ll discuss cutting-edge AI strategies that are reshaping network management, security, and efficiency. The talk will cover practical applications of AI in predictive analytics, automated troubleshooting, and network optimization. We aim to provide insights on leveraging AI for more intelligent, resilient, and efficient network infrastructures.

### Cloud Native ORAN Testing in Your Pipeline - W. Watson, Vulk Cooperative & Andre Puschmann, Software Radio Systems Ltd
Speakers: W. Watson Principal, Vulk Cooperative W. Watson has been professionally developing software for 30 years. He has spent numerous years studying game theory and other business expertise in pursuit of the perfect organizational structure for software co-operatives. He also founded the Austin Software Cooperatives meetup... Read More → Andre Puschmann VP Engineering, Software Radio Systems Andre has over 15 years of experience in developing software implementations of radio communications protocols and over 20 years in developing open-source software. Before working at SRS he was a postdoctoral researcher at Trinity College Dublin, Ireland, and Ilmenau University of... Read More →
page: https://onesummit2024.sched.com/event/1YUsM/cloud-native-oran-testing-in-your-pipeline-w-watson-vulk-cooperative-andre-puschmann-software-radio-systems-ltd
This presentation demonstrates the integration of cloud-native testing for the ORAN E2 interface using the CNF Test Suite. The ORAN E2 interface is a key component of Radio Intelligent Controllers (RIC) and XApps, which are important elements of the ORAN architecture. The CNF Test Suite is used for this testing process, employing tools like SRSRAN to validate the e2 traffic between the DU and the RIC. These tools are designed to test cloud-native network functions (CNFs) in a Kubernetes environment, evaluating them against various characteristics such as configuration, compatibility, state management, resilience, and security in your CI/CD pipeline.

### Innovative Commercial Ecosystem & Open Innovation - Ganesh Shenbagaraman, Radisys; Paul Sutton, Software Radio Systems; Amanda Toman, NTIA; Phil DiGuglielmo, Jabil
Speakers: Paul Sutton CEO, Software Radio Systems Paul is co-founder and CEO of Software Radio Systems, the team behind the open-source srsRAN Project, now the OCUDU Project. Used in research and development by thousands of developers worldwide across government, industry and academia, the srsRAN Project became OCUDU in early 2026... Read More → Amanda Toman Director Public Wireless Supply Chain Innovation Fund, National Telecommunications and Information Administration, U.S. Department of Commerce Ms. Amanda Toman is the Director for the Public Wireless Supply Chain Innovation Fund at the National Telecommunications and Information Administration within the Department of Commerce.  With over 20 years of experience in research and development in the Department of Defense, Ms... Read More → Ganesh Shenbagaraman Head of Standards, Regulatory Affairs & Ecosystems, Radisys Ganesh heads Radisys' integrated solutions across wireless, wireline and media processing domains. Named in 2020 as the recipient of the Small Cell Forum Chair's Award, he leads 4G and 5G wireless product development, drives collaboration with industry partners and performs key leadership... Read More → Phil DiGuglielmo R&D Director, Jabil Phil DiGuglielmo is an R&D Director in Jabil’s Wireless Engineering Organization. In his role at Jabil, Phil interacts closely with customers to understand and fulfil their product requirements and he leads design services in the areas of Software Development and Test. Phil has over... Read More →
page: https://onesummit2024.sched.com/event/1cfiz/innovative-commercial-ecosystem-open-innovation-ganesh-shenbagaraman-radisys-paul-sutton-software-radio-systems-amanda-toman-ntia-phil-diguglielmo-jabil

### SBOMs for Telco - Jimmy Ahlberg, Ericsson AB
Speakers: Jimmy Ahlberg Expert & Senior Legal Counsel, Ericsson Currently Mr Ahlberg is the Director of Open Source Policy with the Ericsson OSPO. Prior to the inception of the Ericsson OSPO he worked in different roles with various aspects of Open Source in the Ericsson organization, This included consumption of and contribution to Open Source... Read More →
page: https://onesummit2024.sched.com/event/1YUsO/sboms-for-telco-jimmy-ahlberg-ericsson-ab
What does the Telco industry need in terms of Software Bill of Material, what should vendors and other suppliers provide and can MNO's unite on what they need? By agreeing on what's needed and wanted in the ecosystem in terms of data we will be able to generate higher quality data, at a lower cost, quicker, that with a divergence in requirements on data structure and granularity. Please join this session to discuss your needs, hear the latest thinking from industry leaders on what desirable vs what's needed for your SBOM generation and your SBOM consumption.

### Introduction to CAMARA, the Global Telco API Alliance - Mahesh Chapalamadugu, Verizon
Speakers: Mahesh Chapalamadugu Distinguished Engineer, Verizon Mahesh is focused on the 5G edge computing and interoperable Network API ecosystem. He also represents Verizon at other global telco bodies like Linux Foundation’s CAMARA Project where he sits on the Technical Steering Committee and End User Council.
page: https://onesummit2024.sched.com/event/1cRyK/introduction-to-camara-the-global-telco-api-alliance-mahesh-chapalamadugu-verizon

### Update From NTIA Wireless Innovation Fund Awards - Amanda Toman, NTIA, Michele Polese, Northeastern Univ.; Ravinder Jarral, DISH Wireless; Lingjia Liu, Virginia Tech; Ian Wong, VIAVI Solutions; Alex Stancu, Highstreet Technologies
Speakers: Michele Polese INSI Technical Director, Northeastern University Michele Polese is a Research Assistant Professor at Northeastern University and the Technical Director of the Institute for Intelligent Networked Systems at Northeastern. He is also the chair for the AI-and-RAN working group of the AI-RAN Alliance and a co-founder at zTouch Networks... Read More → Alex Stancu Senior Software and Telecommunications Engineer, Highstreet Technologies Alex Stancu is a Senior Software and Telecommunications Engineer in highstreet technologies. He received his PhD from University POLITEHNICA of Bucharest in 2018, with a thesis on simulators for Software Defined Networking. He currently serves as a Project Technical Lead in the Simulations... Read More → Ravinder Jarral VP of 5G Wireless Partner Engagement and Delivery, DISH Wireless As VP of 5G Wireless Partner Engagement and Delivery at DISH Wireless, Ravinder Jarral is a key driver for the implementation of DISH’s cloud-native Open RAN 5G network. In his current role, he leads partner engagement, lab and test environments and release management. Launching his... Read More → Lingjia Liu Professor and Bradley Senior Faculty Fellow, Electrical and Computer Engineering Department, Virginia Tech Lingjia Liu is a Professor and Bradley Senior Faculty Fellow in the Electrical and Computer Engineering Department at Virginia Tech. Currently, he serves as the Director of Wireless@Virginia Tech, a university center dedicated to comprehensive research on wireless technology. At the... Read More → Dr. Ian C. Wong VIAVI Solutions, Director of RF and Wireless Architecture Dr. Ian C. Wong is currently the Director of RF and Wireless Architecture reporting to the CTO at VIAVI Solutions, where he is leading RF and wireless technology strategy, architectures, and standards.  He is the co-chair of the Test and Integration Focus Group (TIFG) in the O-RAN... Read More → Amanda Toman Director Public Wireless Supply Chain Innovation Fund, National Telecommunications and Information Administration, U.S. Department of Commerce Ms. Amanda Toman is the Director for the Public Wireless Supply Chain Innovation Fund at the National Telecommunications and Information Administration within the Department of Commerce.  With over 20 years of experience in research and development in the Department of Defense, Ms... Read More →
page: https://onesummit2024.sched.com/event/1cfj2/update-from-ntia-wireless-innovation-fund-awards-amanda-toman-ntia-michele-polese-northeastern-univ-ravinder-jarral-dish-wireless-lingjia-liu-virginia-tech-ian-wong-viavi-solutions-alex-stancu-highstreet-technologies

### SONiC and AI - Xin Liu, Microsoft & Wei Bai, Nvidia
Speakers: Xin Liu Principal Product Manager, Microsoft Wei Bai Principal Software Research Architect, Nvidia
page: https://onesummit2024.sched.com/event/1YUsU/sonic-and-ai-xin-liu-microsoft-wei-bai-nvidia
In this session, we will talk about unleashing the power of generative AI and levering open-source networking technologies for the Future.

### Putting AI to Use: Vendor Agnostic SONiC Migration - Vishal Shukla, Aviz Networks
Speakers: Vishal Shukla CEO, Aviz Networks Vishal has 20+ years of experience in the IT Networking Industry. Prior to founding Aviz, Vishal held various leadership roles at Nvidia/Mellanox, IBM, BNT, Cisco, and Nortel Networks. He holds 30+ patents in the field of Software-defined Networking (SDN), IoT, Cloud Orchestration... Read More →
page: https://onesummit2024.sched.com/event/1YUse/putting-ai-to-use-vendor-agnostic-sonic-migration-vishal-shukla-aviz-networks
In this presentation, Vishal will explore the process of transitioning to SONiC in a way that's independent of hardware vendors, applicable to both current infrastructure and new AI networking fabrics. He'll detail essential strategies for ensuring quality, choosing the right vendors, and tools for managing operations from day 0 to day 1, including integration with current toolsets. Additionally, Vishal will highlight how AI can facilitate a smoother migration process.

### Designing Best-in-Class Next Generation Telco Cloud Enabling 3GPP Non-Terrestrial Networks (NTN) - Shujaur Mufti, RedHat
Speakers: Shujaur Mufti Global Head of Telco Partner Solutions, RedHat Inc. Shujaur is a Head of Global Telco at Red Hat, responsible for managing a team of technical professionals to co-develop and enable Cloud technologies utilizing Red Hat products in customer networks. Shujaur has 20+ years of Telco experience. Previously, he spent 14 years at T-Mobile... Read More →
page: https://onesummit2024.sched.com/event/1YUsX/designing-best-in-class-next-generation-telco-cloud-enabling-3gpp-non-terrestrial-networks-ntn-shujaur-mufti-redhat
Designing and operating a cloud-native Telco Cloud for 3GPP 5GA and Non-Terrestrial Networks (NTN) involves a complex and multi-disciplinary effort that requires expertise in networking, cloud computing, virtualization, security, and emerging technologies. The session includes the guiding principles to deploy the right design enhancements to the large scale NFV/Clout-native Telco cloud with Multi-cloud portability, Observability, HA and resiliency, and other areas of cloud enablement. Key highlights of the session include: 5G architecture encompassing virtual RAN, Converged and unified 5G/IMS Core, Network Slicing, API driven design to leverage the capabilities of 3GPP Network Exposure Function, 5G Roaming, and other 5G monetization functions Leveraging cutting-edge technologies and architectural principles to deliver efficient, scalable, and high-performance communication services.

### Overcoming Challenges for AI-Fabric with SONiC - Madhu Paluru, Aviz Networks
Speakers: Madhu Paluru Director of Engineering, Aviz Networks Madhu is a distinguished technology leader with a rich history spanning over two decades in Cloud, Data Networking, and Open Source. Currently spearheading the development of a cutting-edge Gen AI-powered Network 3.0 stack at Aviz, he holds a pivotal role in democratizing Open Networking... Read More →
page: https://onesummit2024.sched.com/event/1YUsa/overcoming-challenges-for-ai-fabric-with-sonic-madhu-paluru-aviz-networks
The increasing use of Gen AI training and inference workloads has posed unique requirements to network infrastructure. SONiC as a Open Networking Platform provides all the necessary control and data plane support to handle these AI workloads and we will propose solutions to efficiently manage and operate these AI fabrics by minimizing the configuration errors by config automation and improved troubleshooting by providing deep visibility into the network.

### Lifecycle Management of OAI O-RAN Network Functions via Nephio - Sagar Arora, OpenAirInterface Software Alliance; Alexis de Talhouët, Red Hat; Sana Tariq, Telus Canada
Speakers: Sana Tariq Principal Architect - Cloud and Service Orchestration, Telus Canada Sana Tariq, Ph.D. in Computer Science and Fulbright alum, brings 15 years of telecom expertise. As TELUS's Principal Architect, shaping 5G and O-RAN automation architecture. A pioneer in cloud-native adoption through DevOps and open source, she leads initiatives with NGMN, LFN, and... Read More → Alexis de Talhouët Telco Solutions Architect, Red Hat Alexis is a Solutions Architect at Red Hat, specializing in architecting innovative solutions for telecommunication providers. With a strong background in infrastructure, development and network automation, he brings a unique blend of skills to design and implement cloud-based solutions... Read More → Sagar Arora Solutions Architect, OpenAirInterface Software Alliance Sagar Arora is a Solutions Architect at OpenAirInterface and TSC lead for the LFN Duranta Project. Sagar holds a Ph.D. in Mobile Communications from Sorbonne University, France. His doctoral thesis, titled “Cloud-Native Network Slice Orchestration in 5G and Beyond,” focused on the... Read More →
page: https://onesummit2024.sched.com/event/1YUsb/lifecycle-management-of-oai-o-ran-network-functions-via-nephio-sagar-arora-openairinterface-software-alliance-alexis-de-talhouet-red-hat-sana-tariq-telus-canada
Join us for an insightful session on the groundbreaking advancements showcased in Nephio Release 2. Our demonstration will unveil the seamless orchestration of O-RAN Network Functions (O-DU, O-CU-CP, O-CU-UP) and 3GPP Release 16 5G Core Network Functions (AMF, SMF, UPF, NRF, UDR, AUSF, UDM), using the OpenAirInterface Software Alliance implementation. Building upon this foundation, we will extend the setup by incorporating a physical O-RU, not managed by Nephio, creating a comprehensive environment. Witness the real-world scenario as we establish an end-to-end call Over The Air (OTA) using 5G User equipment. Dive into the technical intricacies with a setup description encompassing three deployment sites or Nephio workload clusters—Core, Regional, and Edge. Each site is a Single Node Openshift (SNO) cluster, interconnected through a Backhaul switch, while the Edge cluster is seamlessly linked using a FrontHaul switch, offering PTP support to O-DU and O-RU. This session promises to unravel the future of network orchestration and interconnectivity, providing a glimpse into the cutting-edge technology shaping the telecommunications landscape.

### SEDIMENT for IoT Device Security and Authentication - Zahir Patni, Peraton Labs
Speakers: Zahir Patni Research Science, Senior Advisor, Peraton Labs A Senior Advisor for Research Science at Peraton Labs with over a decade of experience in the Telecom, Networking, and Software Engineering industries.
page: https://onesummit2024.sched.com/event/1YUsm/sediment-for-iot-device-security-and-authentication-zahir-patni-peraton-labs
SEDIMENT (SEcure DIstributed IoT ManagemENT) uses a combination of software root of trust, remote attestation (RA), and resource-efficient cryptography, to build a security system that operates across the entire scale of IoT devices, with special emphasis on resource-constrained endpoints. The attestation, which appraises the integrity and trustworthiness of devices, can be integrated with the 5G ONAP AMF to control network/application access. An RA use case with the SEDIMENT RA Verifier detecting a corrupted device will be shown.

### Evolving Together: Cloud Native Telecom's Journey Forward - Olivier Smith, MATRIXX & W. Watson, Vulk Coop
Speakers: W. Watson Principal, Vulk Cooperative W. Watson has been professionally developing software for 30 years. He has spent numerous years studying game theory and other business expertise in pursuit of the perfect organizational structure for software co-operatives. He also founded the Austin Software Cooperatives meetup... Read More → Olivier Smith Director, Office of the CTO, MATRIXX A member of the CTO Office at MATRIXX Software, Olivier is responsible for identifying emerging trends, driving technology strategy, and delivering thought leadership. Olivier is actively engaged in open source communities in the Linux Foundation where he helps advance and promote... Read More →
page: https://onesummit2024.sched.com/event/1YUsR/evolving-together-cloud-native-telecoms-journey-forward-olivier-smith-matrixx-w-watson-vulk-coop
In our upcoming April session, we'll reflect on LF Networking’s Cloud Native Telecom program journey since our pivotal launch in November. LFN introduced a Test Catalog and Certification Program then, marking key milestones in telecom's cloud native transition. Now, we're looking ahead. The future holds exciting updates: new versions of our certification, expansions to the Test Catalog, and integration of additional tools and resources. We're also focused on collaborating with downstream projects to consume and expand the outputs from our initiatives. This session is an invitation to learn about and join the community in this ongoing evolution. Whether you're a developer, a telecom professional, or an enthusiast in cloud-native technologies, your contribution can drive significant advancements in this field. Be a part of shaping telecom's cloud-native future!

### NSF Initiatives: Open-Source, O-RAN & The Big Picture in Next-G Wireless - Sudharman K. Jayaweera, NSF
Speakers: Dr. Sudharman K. Jayaweera Program Director, National Science Foundation (NSF) Dr. Sudharman K. Jayaweera is currently a Program Director at the National Science Foundation (NSF) in the Emerging Technologies section of the Division of Innovation Technology and Ecosystems in the Directorate of Technology, Innovation and Partnerships, or TIP, with responsibility... Read More →
page: https://onesummit2024.sched.com/event/1cfj8/nsf-initiatives-open-source-o-ran-the-big-picture-in-next-g-wireless-sudharman-k-jayaweera-nsf

### Tackling Next G Challenges - Sudharman Jayaweera, NSF; Amanda Toman, NTIA; Thomas Rondeau, DoD
Speakers: Thomas Rondeau, PhD Principal Director for the FutureG Office, Department of Defense Dr. Tom Rondeau is the Principal Director for the FutureG Office for the US Department of Defense, serving in the Office of the Undersecretary of Defense for Research and Engineering (OUSD(R&E)). In this role, Dr. Rondeau is responsible for the research, funding, and execution of... Read More → Dr. Sudharman K. Jayaweera Program Director, National Science Foundation (NSF) Dr. Sudharman K. Jayaweera is currently a Program Director at the National Science Foundation (NSF) in the Emerging Technologies section of the Division of Innovation Technology and Ecosystems in the Directorate of Technology, Innovation and Partnerships, or TIP, with responsibility... Read More → Amanda Toman Director Public Wireless Supply Chain Innovation Fund, National Telecommunications and Information Administration, U.S. Department of Commerce Ms. Amanda Toman is the Director for the Public Wireless Supply Chain Innovation Fund at the National Telecommunications and Information Administration within the Department of Commerce.  With over 20 years of experience in research and development in the Department of Defense, Ms... Read More →
page: https://onesummit2024.sched.com/event/1cfj5/tackling-next-g-challenges-sudharman-jayaweera-nsf-amanda-toman-ntia-thomas-rondeau-dod

### SAI Virtual Switch in DentOS - Taras Chornyi & Leonid Khedyk, PLVision
Speakers: Leonid Khedyk Chief Technology Officer, PLVision Leonid Khedyk is Chief Technology Officer at PLVision, a software product development company focused on open networking. He has been working in networking and embedded systems for over 17 years. With his diverse technical background, Leonid leads PLVision's contribution to open networking... Read More → Taras Chornyi Director of Open Networking Solutions and Strategy, PLVision Taras Chornyi is a Director of Open Networking Solutions and Strategy at PLVision, a software product development company focused on open networking. He is a General Member Governing Board Representative for the SONiC and DENT projects. Taras has dedicated 15 years of his career to... Read More →
page: https://onesummit2024.sched.com/event/1YUsk/sai-virtual-switch-in-dentos-taras-chornyi-leonid-khedyk-plvision
In this presentation, we'll walk you through our experience of using the SONiC SAI Virtual Switch (VS) in DentOS. Throughout the development and testing phases of the NOS, we leverage virtualization to simulate a streamlined yet authentic data center switch environment. This approach allows the comprehensive testing of the control plane applications without the need for physical hardware. By enabling the virtual switch, you gain the power to emulate multiple switches in complex networking setups in virtual environments. This provides businesses with the flexibility to streamline their development and testing even before a fully deployed physical device is at their disposal, contributing to the rapid emergence of innovations. We'll show you how to use the SONiC SAI Virtual Switch in DentOS and guide you in building a DENT Virtual Switch.

### How Generative AI Collaboration in Open Source Communities Empowers Telecommunications Intelligent ? - ChangJin Wang & Jie Hu, ZTE Corporation
Speakers: Jie Hu Senior Engineer, ZTE CORPORATION Jie has worked for ZTE for over 2 decades. He is familiar with Telecom services and related architectures. 长金 王 Engineer, ZTE Corporation Changjin is the chief engineer of Computing & Cloud Core planning at ZTE Corporation. With over 15 years experience in telecom core network and cloud computing. He has extensive practical experience in the open source , cloud native and AI fields of telecom cloud.He is also actively... Read More →
page: https://onesummit2024.sched.com/event/1YUsh/how-generative-ai-collaboration-in-open-source-communities-empowers-telecommunications-intelligent-changjin-wang-jie-hu-zte-corporation
The Trends of Generative AI,The characteristics in the telecommunications industry,Open Source LLM training proposal for telecommunications,Consideration on LLM Collaboration in Open Source Communities.

### NanoMQ + EKuiper: Unify Real-Time Messaging & Streaming for Internet of Vehicles - Jielin Yu, EMQ Technologies
Speakers: Jaylin Yu Solution VP, EMQ Jaylin Yu graduated from CUHK and previously worked as a GIS analyst at UN ESCAP. Published several academic papers and held IoT patents. He has devoted himself to IoT and edge computing for more than ten years as a professional and has rich experience in the collaborative development... Read More →
page: https://onesummit2024.sched.com/event/1YUsv/nanomq-+-ekuiper-unify-real-time-messaging-streaming-for-internet-of-vehicles-jielin-yu-emq-technologies
The tide is shifting, world is embracing open source solution, and we are taking it seriously by contributing to it! Learn about the trending of Software Defined Vehicles, how the automotive industry uses open-source products from EMQ Technologies to create cutting-edge solutions for connected vehicles. With NanoMQ our messaging middleware built for running on the edge and eKuiper a lightweight data analytics and stream processing engine running on resource-constraint edge devices. We'll also discuss QUIC , a performant transport layer created for Internet of Vehicle applications, as well as EMQX - the #1 open-source MQTT broker for IoT. This session will cover a few real world example solutions for ingesting, processing, and transmitting data at scale from remote locations. If you have an interest in industrial, vehicle, or home automation and data, then this presentation is for you.

### Revolutionizing Open Source Networking with AI-Powered Repository Evaluation and Repair - Brian Hill, Merly AI
Speakers: Brian Hill Machine Programming Researcher, Merly AI Brian is Chief of Staff and Machine Programming Researcher at Merly AI, leveraging expertise in computer science research. Formerly with SAIL (Stanford AI Lab) under Andrew Ng, exploring Data-Centric AI. Holds an engineering degree from Berkeley and a Statistics/Data Science Masters... Read More →
page: https://onesummit2024.sched.com/event/1YUsq/revolutionizing-open-source-networking-with-ai-powered-repository-evaluation-and-repair-brian-hill-merly-ai
The intersection of AI and open source networking is an area of tremendous opportunity. In my lightning talk, I will delve into the realm of "AI for Network" through the lens of Mentor, a cutting-edge tool redefining how we evaluate and enhance open source repositories. Mentor serves as an innovative solution, leveraging advanced AI/ML algorithms to meticulously scrutinize, understand, and repair repositories. By making use of Mentor's capabilities, the community is able to fortify the security layers, elevate the quality of service, and enhance the reliability of open source networking solutions. We can also understand where we should be prioritizing development, and which dependencies may lead to problems. This novel approach not only streamlines operations but also paves the way for a robust infrastructure capable of meeting the demands of 5G deployment, government infrastructure development, and business automation—while fostering a collaborative environment for industry-wide learning and advancement.

### Ecosystem Collaboration Logistics - Government Repository Development - Dr. Michael G. Anderson, US Navy
Speakers: DM Dr. Michael G Anderson Project Manager, US Navy Dr. Anderson is a project manager for the US Navy where he leads multiple efforts focused on the use of commercial technologies for tactical applications. His research interests include software defined radios and technology trust. Dr. Anderson has over 25 years of experience in the... Read More →
page: https://onesummit2024.sched.com/event/1cfjB/ecosystem-collaboration-logistics-government-repository-development-dr-michael-g-anderson-us-navy

### RIC Forum Readout - Ted K. Woodward, Ph.D., FutureG Office, U. S. DoD
Speakers: TK Ted K. Woodward P PhD
page: https://onesummit2024.sched.com/event/1cfjE/ric-forum-readout-ted-k-woodward-phd-futureg-office-u-s-dod

### The Dark Side of AI: The Hidden Supply Chain Risks in Open-Source AI Models - Guy Nachshon, Checkmarx
Speakers: Guy Nachshon Security Researcher, Checkmarx I'm Guy Nachshon, a Security Researcher at Checkmarx, specializing in Supply Chain Security. My work includes Security Research and coding in multiple language, design and AI Security Research, where I focus on safeguarding AI systems. My portfolio includes groundbreaking research... Read More →
page: https://onesummit2024.sched.com/event/1YUqw/the-dark-side-of-ai-the-hidden-supply-chain-risks-in-open-source-ai-models-guy-nachshon-checkmarx
Explore the dark side of powerful AI tools and the burning question: Are they truly secure? Join me as we unravel the construction of AI models, focusing on their weak spots. Through multiple demos, witness how AI models can be manipulated to become malicious. This session offers a deep dive into a case study on the "Malicious Copilot" IDE plugin will showcase how a code-completion model can be trained to target specific victims, embedding malicious code within models, and more. Additionally, we'll tackle practical takeaways for companies utilizing generative AI and LLMs.

### SONiC BGP Loading Optimization - Joy Qin & Eddie Ruan, Alibaba Cloud
Speakers: Joy Qin Software Engineer, Alibaba Cloud US LLC Software Engineer in Alibaba Cloud AIS team ER Eddie Ruan Alibaba
page: https://onesummit2024.sched.com/event/1YUss/sonic-bgp-loading-optimization-joy-qin-eddie-ruan-alibaba-cloud
This talk introduces Alibaba's recent work on accelerating SONiC NOS BGP Routes Loading Workflow. Apart from the batch publish feature which decreases FPMSyncD Redis traffic and a new design of the Redis pipeline flush policy, this talk also introduces how Alibaba restructures SONiC submodules such as Orchagent and Syncd with a Singleton version templated ring buffer data structure. It utilizes the lambda function to enable general and flexible offload for the module main thread, and eventually double the loading performance.

### Creating an Open Ecosystem for Public Private Development - Arpit Joshipura & Mike Woster, The Linux Foundation
Speakers: Arpit Joshipura GM of Networking, The Linux Foundation Mike Woster CRO, The Linux Foundation Mike Woster is the Chief Revenue Officer of The Linux Foundation and was a founding executive team member. He joined the Foundation in 2008, when it had only a handful of employees. Mike and his team have been the engine for growth and sustainability at The Linux Foundation. He has developed a unique strategy to expand the Foundation from a membership organization exclusively focused on the kernel to a high-growth business that provides strategic advice and key... Read More →
page: https://onesummit2024.sched.com/event/1cfjH/creating-an-open-ecosystem-for-public-private-development-arpit-joshipura-mike-woster-the-linux-foundation

