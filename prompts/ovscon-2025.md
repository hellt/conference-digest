>>> HOW TO RUN THIS <<<
This is the digest prompt for ovscon-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ovscon-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ovscon-2025.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

Below is the program for Open vSwitch and OVN 2025 Fall Conference (Prague) (vendor). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a vendor / community program (e.g. a CNCF or vendor conference).
Separate genuine technical or strategic substance from product marketing.
Down-rank pure product pitches and sponsor slots. Up-rank end-user case studies
with real numbers (scale, latency, cost, incident detail), contributor-led
architecture and internals talks, and sessions that reveal where an open-source
project is actually heading. Be skeptical of "we adopted X and it was great"
talks with no metrics or failure discussion.

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
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
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
conference: Open vSwitch and OVN 2025 Fall Conference (Prague)
type: vendor
source_url: https://www.openvswitch.org/support/ovscon2025/
generated: 2026-11-01
registry_key: ovscon-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

### Observing Open vSwitch with native prometheus metrics
Speakers: Gaetan Rivet, NVIDIA
page: https://www.openvswitch.org/support/ovscon2025/#t1 | video: https://youtu.be/awHSbUbCNoo | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVScon25%20-%20Observing%20OVS%20with%20native%20prometheus%20metrics.pdf
Open vSwitch powers a diverse range of virtualized networking stacks, and observability remains a challenge. Existing external tools often assume a kernel datapath, introducing gaps when moving to userspace implementations. They also impose overhead by scraping internals via multiple CLI calls, which narrows what can be observed and limits measurement frequency. This talk introduces a native, Prometheus-compatible metrics framework in the OVS library. It aligns observability across kernel and userspace datapaths from an external observer perspective, providing a single access path to relevant events. The result is more accurate, granular visibility with lower footprint, enabling higher frequency measurements without distorting datapath behavior and reducing friction when integrating controllers. I will describe the Prometheus data model and the metric types implemented in the framework, then discuss trade-offs and design choices for the metric arborescence and access patterns: * Metric node types * Bounded collections for label generation * Conditional access to optional modules * Threading model Finally, I will show usage in practice with metrics defined in the common ofproto layer and specialized metrics made possible in the userspace datapath.

### When CI Shouts Back: LLMs in the OVS CI Pipeline
Speakers: Aaron Conole, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t2 | video: https://youtu.be/JCmHuCVmOVs | slides: https://www.openvswitch.org/support/ovscon2025/slides/When%20CI%20Shouts%20Back_%20LLMs%20in%20the%20OVS%20CI%20Pipeline.pdf
A lightning talk exploring recent experiments in the upstream CI pipeline using CodeRabbit, Sourcery, and Claude SONNET models for assisting with code review. We'll give an overview of our experiences with these tools, some interesting analysis results, and future steps for integrating an LLM into the CI development process.

### AI-Powered Performance Insights: Integrating OVS/OVN automatic performance regression analysis with LLMs
Speakers: Joe Talerico, Red Hat; Jose Castillo Lema, Red Hat; Mohit Sheth, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t3 | video: https://youtu.be/LT6FQG9fR3k | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVS'25_%20AI-Powered%20Performance%20Insights.pdf
Performance engineering is critical for ensuring Kubernetes networking scalability and stability, yet traditional regression analysis is slow and manual. At Red Hat, performance testing has shifted left, allowing developers to run scale workloads against pull requests early in the cycle. To accelerate feedback, we introduce Orion, a Python library for automated statistical regression detection, and Orion-MCP, an MCP server that enables Large Language Models (LLMs) to analyze results, detect anomalies, and provide natural-language insights. Together, these tools make performance data more accessible and actionable, helping developers quickly identify and address regressions in evolving Kubernetes networking code.

### OpenFlow Classifier: Arcane knowledge and common pitfalls
Speakers: Ilya Maximets, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t4 | video: https://youtu.be/pbr2lR1wyKc | slides: https://www.openvswitch.org/support/ovscon2025/slides/OpenFlow%20Classifier_%20Arcane%20knowledge%20and%20common%20pitfalls.pdf
The OpenFlow classifier is the brain and the heart of Open vSwitch, but not many people these days know how it actually works. Some of the knowledge is hidden behind the complex code, motivation for some features and optimizations is lost in time, since the original authors of this code stepped away from the project long ago. This talk is a deep dive into inner workings of the classifier, aiming to shed some light on the architecture and optimizations, explaining common "do"s and "don't"s of writing efficient OpenFlow pipelines with regards to issues that OVN faced in the recent years.

### Uncovering Testing Gaps in OVN Incremental Processing
Speakers: Jacob Tanenbaum, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t5 | video: https://youtu.be/btVAx-Er1qs | slides: https://www.openvswitch.org/support/ovscon2025/slides/Jacob%20Tanenbaum%20Presentation%20OVN_OVS%20con%202025.pdf
The incremental processing of OVN objects greatly decreases the processing time of changes to the OVN database, this leads to increases in scale and ability to handle database changes. Assuming that all the changes are handled correctly. The current state of testing for the incremental processor has a large oversight that the project needs to address. Comparing the output of the incremental processor to a forced recalculation of the database leaves room for bugs and unforeseen interactions that may not be accounted for. We need a new method of testing that can account for interactions between runs of the incremental processor that are not currently accounted for.

### Improving Retrieval from the OVS Hashmap
Speakers: Rosemarie O'Riorden, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t6 | video: https://youtu.be/sGFCU2h2mtI | slides: https://www.openvswitch.org/support/ovscon2025/slides/Improving%20Retrieval%20from%20the%20OVS%20Hashmap%20-%20Rosemarie%20O'Riorden.pdf
The OVS hashmap is used all throughout OVN and OVS for a variety of data storage. With very frequent data retrieval, any bit of performance improvement is beneficial. Valkey recently published a blog about changes they made to their hashmap, and how they saw significantly less memory usage, so I want to build off their design and implement something similar for OVS. This will hopefully lessen cache misses, thus improving overall performance.

### The BGP Fork in the Road: A Tale of Two Implementations
Speakers: Jaime Caamaño Ruiz, Red Hat; Patryk Diak, Red Hat; Surya Seetharaman, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t7 | video: https://youtu.be/2kYhodVu6bM | slides: https://www.openvswitch.org/support/ovscon2025/slides/The%20BGP%20Fork%20in%20the%20Road.pdf
In the world of networking, two paths diverged in a yellow wood, and OVN-Kubernetes took the one less traveled by. When it comes to BGP support, both OVN and OVN-Kubernetes developed their own implementations almost simultaneously. It was a classic "great minds think alike" situation, but instead of joining forces, they each went their own way. Now we're left with a tale of two distinct BGP implementations, each with its own quirks and charms. This talk will pull back the curtain on this intriguing parallel development. We'll start by exploring how OVN handles BGP, from its core design to its capabilities. Then, we'll dive into the OVN-Kubernetes approach, revealing how it provides BGP support for your workloads. We'll highlight the key differences between these two implementations and, more importantly, identify the gaps that currently prevent OVN-Kubernetes from simply adopting OVN's native BGP support. Finally, we'll get down to brass tacks: what would it take for OVN-Kubernetes to make the switch? We'll analyze the pros and cons of such a move, discussing the technical challenges and potential benefits. This talk isn't just about code; it's about the journey of open source development and the sometimes-messy reality of building great things in parallel. Join us for a fun and informative look at two BGPs, and help us decide if it's time for them to finally become one.

### A Nightmare on Kube Street: Slicing Kubernetes Networks like Freddy Krueger
Speakers: Dave Tucker, Red Hat; Surya Seetharaman, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t8 | video: https://youtu.be/HvmjDHWJheY | slides: https://www.openvswitch.org/support/ovscon2025/slides/A%20Nightmare%20on%20Kube%20Street_%20Slicing%20Kubernetes%20Networks%20like%20Freddy%20Krueger%20-VPCs%20Lightning%20Talk%20-%20OVN_OVS%20Conf%20-%202025.pdf
Virtual Private Clouds (VPCs) are the network isolation dream that major cloud providers have perfected—but for those of us running Kubernetes, our networks can feel more like a nightmare. Despite recent advances in network policies and segmentation, we're still stuck in a flat network hellscape where true multi-tenant isolation feels impossibly complex. What if we could slice through this chaos like Freddy himself? What if we could give teams the power to carve out their own isolated network territories while still allowing controlled communication between them? In this talk, we'll unveil a new OVN-Kubernetes feature that brings true VPC functionality to your clusters. Building on the recently added User-Defined Networks (UDNs) foundation—which provides isolated network primitives—our VPC implementation allows you to group these networks together and define communication policies between them. Think of it as NetworkPolicy's bigger, more powerful sibling that operates at the network topology level rather than just the pod level. We'll start with a tour of VPC concepts from AWS and NSX, then dive deep into our OVN implementation. You'll see how we leverage OVN logical switches, routers, and policies to create true network segmentation that goes beyond what traditional Kubernetes networking offers. We'll demonstrate our working prototype in action, showing how development teams can own their network topology while platform teams maintain control over inter-network communication. Join us as we slice through the technical implementation details and show you how OVS and OVN make this VPC nightmare-turned-dream a reality. By the end, you'll understand the architecture, see it working, and know how this feature will transform multi-tenant Kubernetes networking. Sweet dreams are made of properly isolated networks!

### OVN and BGP: A Friendship Forged in OpenStack Neutron
Speakers: Jakub Libosvar, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t9 | video: https://youtu.be/iE_z6Fv6-PI | slides: https://www.openvswitch.org/support/ovscon2025/slides/Copy%20of%20OVN%20and%20BGP%20-%20OVSOVN%20conf%202025.pdf
This talk explores the integration of OVN's BGP capabilities within OpenStack Neutron, the networking component of the OpenStack project. We will begin with a concise overview of key Neutron components to provide essential context for attendees unfamiliar with OpenStack. Following this, we will break down the OVN logical components responsible for advertising prefixes throughout the topology. The session will also feature a short live demonstration showing the OVN BGP integration with Neutron in action. The goal of this session is to present how OVN innovations are adopted by other projects.

### A native way of integrating OVN into the fabric through BGP-EVPN.
Speakers: Ales Musil, Red Hat; Dumitru Ceara, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t11 | video: https://youtu.be/KE-CF8bD1CU | slides: https://www.openvswitch.org/support/ovscon2025/slides/A%20native%20way%20of%20integrating%20OVN%20into%20the%20fabric%20through%20BGP-EVPN.pdf
Since version 25.03, OVN has had native support for integrating with L3 fabrics through BGP. We now present the work that happened in 25.09 to extend this native support in order to stretch OVN virtual L2 domains into and across the fabric through BGP-EVPN. The talk will give an overview of the targeted use cases for BGP-EVPN in cloud deployments and of how OVN virtual L2 domains are implemented. We'll then show how the new OVN native support can be used for connecting the two. The newly added OVN BGP-EVPN support is marked as experimental in 25.09 therefore we're also seeking feedback from the audience regarding the design decisions we have made when implementing the feature. In order to facilitate that we'll go into the technical details of the solution and present: - how and where the BGP control plane is supposed to be configured and is expected to run - how OVN integrates with the BGP control plane in order to learn remote VTEPs (VXLAN tunnel endpoints) - how OVN programs its dataplane in order to forward traffic through remote VTEPs according to the BGP control plane information - how OVN learns and exposes remote and local workloads through EVPN The talk will also present the plan to extend the implementation in order to further support more ways to integrate with the fabric BGP-EVPN infrastructure.

### Virtual Network Function integration in OVN
Speakers: Sragdhara Datta Chaudhuri, Nutanix; Naveen Yerramneni, Nutanix
page: https://www.openvswitch.org/support/ovscon2025/#t12 | video: https://youtu.be/-dxVEMlJlLE | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVN%20Conference%20-%20Network%20Function%20Insertion.pptx
This feature addresses a long-standing request in OVN by adding the ability to insert a virtual network function (VNF), such as a third-party firewall, into the traffic path. It supports both VLAN and overlay subnets and follows a "bump-in-the-wire" model. Packets matching an access list are forwarded through the port pair of a VNF. Stateful behavior is maintained by forwarding response packets through the same port pair. For cross-host communication, tunneling is enforced for traffic to and from the node hosting the VNF. Users can group multiple instances of a VNF together. The health of the group members is monitored using data path probe packets. Users have the option to either select one healthy member or load balance across all healthy members. Additionally, there is a configuration option to choose between fail-close and fail-open behavior, which dictates whether traffic will be dropped or forwarded (bypassing the VNF) when all group members are unhealthy. In addition to the inline mode VNF described above, users can alternatively create a VNF in tap mode. In this mode, packets matching an access list — and their associated responses—are cloned and forwarded to the VNF, while the original traffic continues along the normal forwarding path. The solution introduces new pipeline stages in logical switch, new northbound (NB) entities related to network function, a new action in access-list and a new type of health monitoring in ovn-controller. It also makes use of connection tracking labels to support traffic redirection for response packets and to enforce tunneling behaviour. Current status of the feature: Code review in progress - https://mail.openvswitch.org/pipermail/ovs-dev/2025-July/424718.html https://mail.openvswitch.org/pipermail/ovs-dev/2025-July/424719.html https://mail.openvswitch.org/pipermail/ovs-dev/2025-July/424720.html https://mail.openvswitch.org/pipermail/ovs-dev/2025-July/424721.html https://mail.openvswitch.org/pipermail/ovs-dev/2025-July/424722.html https://mail.openvswitch.org/pipermail/ovs-dev/2025-July/424723.html

### OVN-Kubernetes Meets DPUs: Enabling Service Function Chaining and Shared OVN
Speakers: Tim Rozet, NVIDIA
page: https://www.openvswitch.org/support/ovscon2025/#t13 | video: https://youtu.be/Ssm4DqJ8awc | slides: https://www.openvswitch.org/support/ovscon2025/slides/SFC,%20DPU,%20Shared%20OVN.pdf
Modern cloud-native environments are increasingly adopting DPUs and advanced networking architectures to deliver high-performance, secure, and flexible services. This talk will explore how OVN-Kubernetes integrates with DPUs, and how this integration is driving new feature requirements in OVN itself. One such feature, "Shared OVN", enables a single OVN instance to serve multiple control management systems (CMS), one per DPU and one for the host cluster. We will discuss why this capability is critical for the DPU use case, and how it is designed to provide isolation and scalability. Another requirement, Service Function Chaining (SFC), introduces the ability to steer traffic through a sequence of security, auditing, and accounting functions on the DPU before it leaves the host cluster. We will cover the expected architecture for SFC in OVN, along with the current status of its enhancement proposal. Attendees will gain insight into the DPU use case with OVN-Kubernetes, and new features required in OVN. This talk also serves as a call to action to help move these features forward.

### Transit router - The distributed router for OVN interconnect.
Speakers: Ales Musil, Red Hat; Mairtin O'Loingsigh, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t14 | video: https://youtu.be/Sf-I7kgc6zo | slides: https://www.openvswitch.org/support/ovscon2025/slides/Transit%20router%20-%20The%20distributed%20router%20for%20OVN%20interconnect.pdf
OVN interconnect is a way to connect multiple OVN deployments in a managed way without the need to setup the tunnels manually. So far there has only been support for Transit Switch which allows the Transit Switch Ports to be part of different Availability Zones. However, there wasn't any simple way to setup routing across Availability Zones. The Transit Router aims to solve that issue. The main goal of Transit Router is to have distributed router that has ports across Availability Zones to leverage the Logical Router capabilities in ovn-ic deployment. The aim of this talk is to introduce the Transit Router capabilities and limitations. With a focus on the internal details and the configuration needed to have a working OVN IC deployment that can leverage the Transit Router. At the end we would like to discuss some open-ended questions for potential improvements.

### Multiple NICs as Encapsulation Endpoints for Large Scale GPU Cloud
Speakers: Girish Moodalbail, NVIDIA; Han Zhou, NVIDIA
page: https://www.openvswitch.org/support/ovscon2025/#t27 | video: https://youtu.be/fis9WHQ6IiY | slides: https://www.openvswitch.org/support/ovscon2025/slides/Multi-NIC%20OVSCON%202025.pdf
Multi-node AI training and inference is becoming increasingly common due to the growing size of LLMs. Within a single node, GPUs communicate through high-speed interconnects such as PCIe and NVLINK. However, communication across multiple nodes still heavily relies on Ethernet. Each GPU in a node is equipped with its own dedicated NIC, enabling direct communication with GPUs in other nodes. For example, if a node contains four GPUs, it will also have four NICs. This means AI workloads are multi-homed, and all inter-node GPU overlay traffic will be transported over the Encapsulation IP associated with each respective NIC. This means we end up with multiple-encapsulation IPs on the same node. In another scenario, cloud gaming workloads utilize dedicated NICs for different functions: one for storage access and another for streaming GPU-generated frames to end-user devices. These are used in addition to the main interface that handles the gaming control plane traffic. As a result, the storage, streaming, and primary workload traffic must each be transported over the Encapsulation IP associated with each respective NIC. In this session, we will demonstrate how multi-homed workloads can be supported on multi-NIC nodes securely using ovn-kubernetes and OVN. We will explore the fundamentals of multi-NIC support, along with the scalability challenges and solutions needed for large-scale Multi-tenant GPU cloud environments.

### OVS-DOCA live-upgrade
Speakers: Eli Britstein, NVIDIA
page: https://www.openvswitch.org/support/ovscon2025/#t16 | video: https://youtu.be/k-4A8YF7aU0 | slides: https://www.openvswitch.org/support/ovscon2025/slides/Copy%20of%20Eli%20Britstein%20-%20ovs-doca-live-upgrade.pptx
In a production environment it is required to update OVS daemon version, mainly for bug fixes. This update procedure requires to have minimal effects both for down-time and workloads interruption. Today, this requires a full restart of the daemon, which have mainly the following challenges: 1. Ports initialization, especially with offloads. 2. There are many volatile states that are gone and must be re-learned or re-configured by a controller. a. Openflow. i. Meters. ii. Groups. iii. TLV-map. iv. Rules. b. Connection tracking connections. c. FDB (MAC learning). d. User configured routes. e. Tunnel neighbour resolution tables. f. More... 3. Connection tracking TCP sessions are disconnected and must be re-established. This talk will go through how OVS-DOCA achieves that. DOCA is capable to initialize the same ports from different userspace processes and zero-time handover. The concept in OVS is to enable invoking the new version in client mode, in parallel to the existing running version (the server). While two instances are running, the following is done: 1. The server continues to handle the current workloads. 2. New instances (ports, offloads) initialization is done in parallel. 3. States are migrated to the new instance. 4. Handover. 5. Termination of the server instance. We’ll also discuss version and resource constraints, failure handling and rollback.

### OVS-DOCA upstream roadmap
Speakers: Maor Dickman, NVIDIA
page: https://www.openvswitch.org/support/ovscon2025/#t17 | video: https://youtu.be/3QGWH54xdfE | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVS-DOCA%20upstream%20roadmap.pptx
Modern cloud workloads demand extremely high bandwidth and minimal latency. To meet these requirements, it is crucial for Open vSwitch (OVS) to utilize hardware acceleration with specialized devices, which enhances scalability, lowers CPU usage, and enables efficient processing at speeds reaching hundreds of gigabits per second. OVS-DOCA, an advanced downstream version of OVS available from NVIDIA, delivers top-tier acceleration on NVIDIA network interface cards (NICs) through a userspace implementation and supports extensive offload capabilities, achieving exceptional packet-per-second (PPS) and connection-per-second (CPS) performance. This presentation will address the architectural differences between OVS-DOCA and the upstream OVS solution and will cover the plans to upstream OVS-DOCA acceleration, building on the existing dpif-netdev userspace framework. The updated architecture involves enhancing dpif-netdev in the following ways: 1. netdev_class doca_class (netdev_doca) - New netdev * Responsibilities: Port initialization and SW handling based on DOCA-ETH (slow path) 2. dpif-offload-doca - New dpif-offload-provider using on DOCA-FLOW, based on new dpif-provider API. * Responsibilities: offload megaflows. 3. CT offloads DOCA offload provider - New offload API for userspace connection tracking based DOCA connection tracking offload.

### Baremetal network isolation for cloud providers with OVN on DPUs
Speakers: Adrian Chiris, NVIDIA; Mael Kimmerlin, NVIDIA; Tarek Abu-Hariri, NVIDIA
page: https://www.openvswitch.org/support/ovscon2025/#t18 | video: https://youtu.be/wDhPPEG16bQ | slides: https://www.openvswitch.org/support/ovscon2025/slides/Bare%20Metal%20network%20isolation%20for%20cloud%20providers%20with%20OVN%20on%20DPUs.pptx
Bare-metal nodes in cloud platforms are increasingly used for workloads demanding direct hardware access paired with high performance, yet these nodes present acute challenges for secure multi-tenancy and strong network isolation. Traditional isolation approaches for Virtual Private Clouds (VPC) often rely on switch configuration management, which introduces operational complexity, exposure to configuration errors, and risks of side-channel or unauthorized cross-tenant communication. As networks scale or tenants rotate frequently, these methods quickly become bottlenecks, reducing agility and potentially compromising security. We present a network isolation architecture for VPC, that leverages the NVIDIA BlueField-3 DPU to offload Open Virtual Network (OVN) and Open vSwitch (OVS) dataplane functionalities. In this model, the DPU, under exclusive control of the cloud administrator, enforces strict network isolation for tenants in a way that is entirely transparent to the host and requires no switch-level modifications when tenants are added or reassigned. With DPUs running in a secure domain, separate from the host operating system, all network traffic enforcement, including tenant segmentation, policy enforcement, packet inspection, and line-rate forwarding is handled transparently and securely. The DPU administrator, not the node tenant or host OS, manages all network isolation mechanisms, ensuring tenant boundaries cannot be compromised even by privileged host processes. Since the DPU accelerates OVS and OVN, the cloud administrator can offer all the expected features of a VPC (external connectivity, DHCP, floating IP addresses etc.) at line-rate speed, with maximum bandwidth and minimum latency. Isolation policies and network topologies are exposed through a declarative Kubernetes API, allowing operators to map bare-metal machines to tenants dynamically without operational complexity. The solution implements a specialized OVN topology optimized for high-performance bare-metal communication, sustaining line-rate throughput both between nodes and for external communications. This approach combines the flexibility of software-defined networking with the performance of hardware offload, delivering scalable, secure, and operationally lightweight tenant isolation for bare-metal cloud environments.

### Deprecating Code
Speakers: Simon Horman, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t19 | video: https://youtu.be/PcBnkClg3Lw | slides: https://www.openvswitch.org/support/ovscon2025/slides/2025-11-20%20Deprecating%20Code.pdf
OVS is a long running project. In time it has accumulated many features contributed by a large number of developers. However, as time has moved on, some features have become unused, while their maintenance burden remains. This presentation aims to explore options for deprecating such code. As well as suggesting some code to which this may apply. It is intended to be interactive, soliciting input from the audience on an appropriate way forward.

### Revisiting checksum offloads in OVS
Speakers: David Marchand, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t20 | video: https://youtu.be/q5Q8v4wY3Vw | slides: https://www.openvswitch.org/support/ovscon2025/slides/Revisiting%20checksum%20offloads%20in%20OVS.pdf
OVS checksum offloads API and TSO support for the userspace datapath was introduced in multiple steps over several years and has grown more complex with the addition of tunnel support recently. The close ties with the DPDK checksum offloads API resulted in complex operations in OVS packet processing. And here complex means bugs were present. This talk will present the recent revamp of this API: from the initial fixes and the unit tests coverage additions, to the new API, its enhanced readbility and the (hopefully) easier maintenance such as better isolation of the API from the DPDK and Linux kernel offloads API. As part of this talk, performance numbers with some popular nics will be discussed.

### You Want to Upgrade WHAT? A Field Guide to Risky Network Changes
Speakers: Nadia Pinaeva, NVIDIA; Dumitru Ceara, Red Hat; Patryk Diak, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t21 | video: https://youtu.be/Xwkwelz9ZBY | slides: https://www.openvswitch.org/support/ovscon2025/slides/You%20Want%20to%20Upgrade%20WHAT_%20A%20Field%20Guide%20to%20Risky%20Network%20Changes.pdf
Every active project accumulates technical debt. For OVN-Kubernetes, our Layer2 network topology, a result of incremental additions and unfortunate design choices, had hit its limit. Not only did it make different topologies support more complicated than it should be, it also imposed feature limitations for EgressIP, Virtual Machines live migration and Network Interconnect. A re-architecture was unavoidable. This session details how we leveraged the OVN Transit Router to redesign our L2 network from the ground up for stability and scale. But the real story isn’t just the new design: having customers already using this feature in production introduced an interesting set of network engineering challenges to solve. If you have never: * Connected the same switch and router with 2 links * Copied the same MAC on multiple ports * Generated dummy IPs just to fix routing * Hand-crafted Route Advertisements to remove stale routes Join our session and follow along on our topology upgrade adventure!

### Space - building a CMS with OVN Concepts
Speakers: Felix Huettner, StackIt
page: https://www.openvswitch.org/support/ovscon2025/#t22 | video: https://youtu.be/joVVeEklhZA | slides: https://www.openvswitch.org/support/ovscon2025/slides/2025_ovn_con_space.pdf
When our existing OpenStack Neutron deployment could no longer meet new requirements, we decided to build an additional CMS based on OVN design concepts. In this talk we will share how we adapted these concepts to our implementation of "spaced". We will walk through the core components of our system: a new "spacebound" OVSDB for defining resources and "spaced" that acts as a custom northd. Spaced translates our high-level requirements into the standard OVN northbound database. It thereby integrates with the Resources that OpenStack Neutron is still managing in northbound. If you were hoping that this talk is actually about running OVN in space, then sorry for making you excited.

### Programming OVS bridges using OVN Bridge Controller
Speakers: Numan Siddique, Crusoe AI
page: https://www.openvswitch.org/support/ovscon2025/#t23 | video: https://youtu.be/MR0pG26JsoE | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVN%20Bridge%20Controller.pdf
If an external controller wants to program an OVS bridge, it has to either talk OpenFlow protocol or make use of ovs-ofctl utility. With the proposed new service OVN bridge controller, a user can program an OVS bridge using the OVN logical flow syntax. This new service will convert these logical flows to Open Flow rules and program the OVS bridges just like ovn-controller programs br-int. This talk gives an overview of how to use this service and shows how it becomes easier to program the OVS bridges.

### Beam Me Through the Datapath: VDUSE for OpenShift Virtualization
Speakers: Jakob Meng, Red Hat; Maxime Coquelin, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t24 | video: https://youtu.be/Tuqz3m4oH4Q | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVSOVNCON25%20-%20Beam%20Me%20Through%20the%20Datapath_%20VDUSE%20for%20OpenShift%20Virtualization.pdf
Last year, we replaced the kernel-based networking stack in OpenShift – Red Hat's Kubernetes distribution for hybrid clusters – with OVS-DPDK and VDUSE: Traffic between NICs and containers is handled end-to-end entirely in userspace. This year, we are closing the gap for virtual machines: We extended OVN-Kubernetes and KubeVirt to use userspace datapaths exclusively with VDUSE and vhost-vDPA. In our talk, we propose a new network architecture for KubeVirt VMs, provide a deep dive into OVS-DPDK performance tuning in OpenShift, and once again share preliminary but transparent benchmark results.

### OvS and Socket Maps - Beyond ports as endpoints
Speakers: Aaron Conole, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t25 | video: https://youtu.be/ONVxHA9chJU | slides: https://www.openvswitch.org/support/ovscon2025/slides/OvS%20and%20Socket%20Maps.pdf
Open vSwitch provides an implementation of a layer 2 switch, with some awareness of both layer 3 and layer 4 networking details. This awareness can be considered a violation of concerns, but with the trade off that Open vSwitch can provide a greater flexibility when authoring network policies for end users. Here we propose a new layer violation - using application ports as packet endpoints. Existing kernel datapath accelerations, ie XDP, can be made aware of application details for endpoints. This, combined with a socket enqueue support, allows for much higher throughput by skipping those layer processing details that aren't needed (for example, routing in layer 3, and the subsequent additional layer 3 + 4 processing inside a target netns). By focusing on the packet movement rather than strict layer adherence, we show that Open vSwitch can provide an accelerated packet forwarding path, and can do so in cooperation with the existing forwarding path.

### Turbocharge Kubernetes with offloaded OVN-Kubernetes and OVS on DPUs
Speakers: Alin Serdean, NVIDIA; Amit Zala, NVIDIA; Mael Kimmerlin, NVIDIA; Igal Tsoiref, Red Hat
page: https://www.openvswitch.org/support/ovscon2025/#t28 | video: https://youtu.be/t-BPwTzb_1I | slides: https://www.openvswitch.org/support/ovscon2025/slides/OVS%20CONFERENCE%20-%20Turbocharge%20Kubernetes.pdf
Running Kubernetes workloads with hardware-accelerated networking is challenging, as existing CNIs either offer limited features, low performance, or impose heavy resource overhead on hosts. Similarly, Service Function Chaining (SFC) in cloud-native environments commonly relies on software-based forwarding on general-purpose CPUs, which restricts scalability and performance. We present a Kubernetes-native platform that offloads both orchestration and service execution to NVIDIA BlueField-3 (BF3) Data Processing Units (DPUs). Our approach extends Kubernetes APIs with CRDs for declarative configuration, allowing services such as OVS, OVN-Kubernetes, routing, storage, and security functions to be deployed and chained directly on the DPU. By combining the programmability of OVS with BF3 hardware acceleration and DOCA capabilities, traffic steering and service execution are fully offloaded from the host. We ran a performance evaluation on BlueField 3 cards. Our open-source platform integrates seamlessly into DevOps workflows through Kubernetes-native interfaces and Infrastructure-as-Code practices, while also integrating with enterprise-grade platforms such as OpenShift. The result is a production-ready, DPU-accelerated networking solution that combines high performance, scalability, and simplified orchestration for next-generation cloud-native and AI workloads.
To reach the organizers, email ovscon@openvswitch.org . For general discussion of the conference, please use the ovs-discuss mailing list .

