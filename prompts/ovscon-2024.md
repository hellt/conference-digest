>>> HOW TO RUN THIS <<<
This is the digest prompt for ovscon-2024. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ovscon-2024.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ovscon-2024.md
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

Below is the program for Open vSwitch and OVN 2024 Fall Conference (Prague) (vendor). Read it and produce a digest
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
conference: Open vSwitch and OVN 2024 Fall Conference (Prague)
type: vendor
source_url: https://www.openvswitch.org/support/ovscon2024/
generated: 2026-11-01
registry_key: ovscon-2024
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

### Running Open vSwitch on a large CPU System
Speakers: Eelco Chaudron, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t1 | video: https://www.youtube.com/watch?v=jX5dVJVSUoc | slides: https://www.openvswitch.org/support/ovscon2024/slides/Running%20OVS%20on%20a%20large%20CPU%20system.pdf
We will examine the impact of the revalidator process and the overall functionality of ovs-vswitchd on systems with a large number of CPUs. Additionally, we'll investigate the kernel's behavior, which may be a key factor influencing ovs-vswitchd's behavior.

### Low on Stack: Flexible protocols vs. Limited Memory
Speakers: Ilya Maximets, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t2 | video: https://www.youtube.com/watch?v=MpXC7CuTKMQ | slides: https://www.openvswitch.org/support/ovscon2024/slides/Low%20on%20Stack_%20Flexible%20protocols%20vs%20limited%20memory.pdf
Processing complex flexible protocols like OpenFlow or Netlink can take a lot of time and memory. Stack memory, in particular. Especially, if done recursively. In this talk we'll look at different techniques (including new ones!) that OVS employs to fight potential stack overflow conditions at many different levels. In the process, we'll look at and explain corresponding warnings and error messages that users may see in the field, like resubmit limits or deferred action limit in the kernel.

### Current Challenges with OpenStack Ironic, SR-IOV, and OVN
Speakers: Michal Nasiadka, Bartosz Bezak, StackHPC
page: https://www.openvswitch.org/support/ovscon2024/#t3 | video: https://www.youtube.com/watch?v=irHtlLm9ACw | slides: https://www.openvswitch.org/support/ovscon2024/slides/Current%20Challenges%20with%20OpenStack%20Ironic,%20SR-IOV,%20and%20OVN.odp
This talk will highlight the ongoing challenges with implementing OpenStack Neutron ML2/OVN and Ironic/SR-IOV external ports. We'll discuss the root causes of these issues, the solutions currently under development, and their status in the upstream OpenStack community (including testing and reviews). Additionally, we'll share temporary work arounds to address these challenges in production environments.

### Integrating OVN into the Network Fabric
Speakers: Felix Huettner, STACKIT GmbH & Co. KG, and Frode Nordahl, Canonical
page: https://www.openvswitch.org/support/ovscon2024/#t4 | video: https://www.youtube.com/watch?v=dCKNrAdISWY | slides: https://www.openvswitch.org/support/ovscon2024/slides/2024_ovn-con_fabric-integration.pdf
At the moment there exists a hard boundry between OVN and the attached outside network fabric. Gateway chassis connect overlay networks on the one side with the network fabric on the other side. Which networks are available via a gateway chassis and which of multiple gateway chassis is the best to reach some destination is not clear to the network fabric. There exist some solutions outside of OVN for this, most notably the ovn-bgp-agent of openstack. In this talk we want to share the current state of a new version of this network fabric integration. The goal is to make OVN feel like a natural extension of the network fabric. For this we will show: * Route advertisement and learning via BGP * Distinct route preferences for different gateway chassis * An active-active version of distributed gateway ports

### First projects as a new OVN developer
Speakers: Rosemarie O'Riorden, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t5 | video: https://www.youtube.com/watch?v=fsSiqDfI8VU | slides: https://www.openvswitch.org/support/ovscon2024/slides/Rose.pdf
I will discuss what it's like to start working as an OVN developer, highlighting two projects I've worked on since I started at Red Hat at the end of June. The first one is the commit "northd: Clean up SB MAC bindings for deleted ports." I would like to talk about navigating the nb-db schema and ovs-db schema in general, and how references can cause referential integrity violations. I will also discuss the entire process of figuring out what's actually going on, brainstorming ideas for a fix, implementing the fix and some special considerations that were made, and finally testing. The second one is the commit "northd: Respect --ecmp-symmetric-reply" for single routes. I will once again go through the entire process I went through to complete this task, but I will also explain the unusual use-case that the bug was found through, along with how ECMP works, how route flows are categorized and built, and then of course, how this fix was reflected in the unit and system tests, and what this change means.

### OVS DOCA - The Evolution of hardware acceleration
Speakers: Majd Dibbiny, Maor Dickman, NVIDIA
page: https://www.openvswitch.org/support/ovscon2024/#t18 | video: https://www.youtube.com/watch?v=SpJClGod0uE | slides: https://www.openvswitch.org/support/ovscon2024/slides/OVS%20DOCA%20-%20The%20Evolution%20of%20hardware%20acceleration.pptx
Open vSwitch (OVS) has undergone significant evolution over the years. It started with a kernel-based data-path, later adopting DPDK to improve bandwidth, packet-per-second (PPS) rates, and latency (albeit with an increase in CPU consumption). To further enhance OVS hardware acceleration was introduced in the kernel data-path, improving performance while reducing CPU overhead. However, this approach brought challenges such as connection-per-second (CPS) performance, latency for non-offloaded packets, and 'slow-path' handling. To address these challenges and expand OVS's capabilities we developed OVS-DOCA, a downstream version of OVS available on the NVIDIA website. OVS-DOCA not only accelerates SDN solutions but also extends the range of use cases that OVS can address. This contributes to the broader OVS ecosystem and increasing its adoption. Additionally, we are actively working to make OVS-DOCA part of the upstream OVS project to benefit the wider community. In this talk, we will explore how OVS-DOCA improves performance metrics while maintaining compatibility with the OVS architecture. We will also demonstrate how DOCA, as an SDK, accelerates development and brings agility to OVS-driven solutions, ultimately enriching the OVS ecosystem.

### Pluggable DPIF - Unlocking accelerated OVS full potential
Speakers: Roi Dayan, Roni Bar Yanai, Eli Britstein, NVIDIA
page: https://www.openvswitch.org/support/ovscon2024/#t7 | video: https://www.youtube.com/watch?v=LukzSDekjx4 | slides: https://www.openvswitch.org/support/ovscon2024/slides/pluggable-dpif-1.pptx | slides: https://www.openvswitch.org/support/ovscon2024/slides/pluggable-dpif-2.pptx
Cloud workloads today require extremely high bandwidth and low latency. These high-performance demands make it essential for OVS to leverage hardware acceleration with specialized hardware to maintain scalability, reduce CPU load, and ensure efficient processing at speeds of hundreds of gigabits per second. In order for OVS to remain competitive in environments demanding low latency, high bandwidth, and encryption capabilities, hardware acceleration is no longer optional but essential. There have been many attempts to add hardware acceleration for both the OVS kernel version and OVS DPDK. In both cases, while some acceleration has been achieved, the real potential for performance improvements is hindered by architectural constraints. These constraints primarily arise because the hardware acceleration interface is logically positioned "below" the data path, meaning the data path structure dictates the acceleration. We have been searching for the best layer for integrating HW acceleration. Based on our experience with customized implementations and our own custom hardware-accelerated OVS, the DPIF [1] interface seems like a natural choice. We also have to remind ourselves that the original intent of it was to enable the porting of OVS to other OSs and platforms. This is already in use today, with both netdev and netlink providers using the aforementioned interface. This talk will go through the proposal of making the DPIF interface a pluggable API that can be loaded at runtime. We will walk through the architectural challenges we encounter today and showcase how the pluggable DPIF provider will aid us in the future. Each vendor would be free to implement their version and provide it as a shared object that can be loaded at runtime. Vendors can then create a hardware-accelerated OVS that fully integrates with the OVS ecosystem and control system.

### Can 'ofproto/trace' go live
Speakers: Adrian Moreno, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t21 | video: https://www.youtube.com/watch?v=k8MMjRrlkbc | slides: https://www.openvswitch.org/support/ovscon2024/slides/Can%20'ofproto-trace'%20go%20live.pdf
'ofproto/trace' is a super useful tool that all of us use to understand what the OpenFlow pipeline decides to do with a packet. However, it is an offline tool, the OpenFlow classification is simulated on an artificial packet that the user provides. This limits the accuracy of its results as some important information can not be simulated or guessed, e.g: conntrack state. In this lightning talk, the possibilities of making ofproto/trace work on live upcalls are explored, challenges are identified and a proof of concept is presented. The goal of this lightning talk is to discuss the idea, hopefully triggering discussions, and gather feedback on how some of the challenges can be overcome.

### OpenShift Networking Transformed: Fully Embracing DPDK Datapaths in OVN-K8s!
Speakers: Jakob Meng, Maxime Coquelin, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t8 | video: https://www.youtube.com/watch?v=KwznQq8f7LM | slides: https://www.openvswitch.org/support/ovscon2024/slides/OpenShift%20Networking%20Transformed.pdf
OpenShift is Red Hat's opinionated Kubernetes distribution for hybrid clusters on bare-metal, GCP, AWS, Azure etc. Under the hood it uses OVN-Kubernetes, OVN and OVS to provide networking to containers (pods) and virtual machines. We replaced its kernel datapaths with userspace datapaths end-to-end from NICs to containers in order to fully unleash the benefits of DPDK upon OpenShift. In our talk we will explain the current state of networking in OpenShift, outline use cases and advantages for userspace datapaths, propose our solution and provide preliminary but honest benchmark results.

### Automating Root Cause Analysis in OVS/OVN-Based Deployments Using AI/ML
Speakers: Gurpreet Singh, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t9 | video: https://www.youtube.com/watch?v=2OB29dygaH0 | slides: https://www.openvswitch.org/support/ovscon2024/slides/Automating%20Root%20Cause%20Analysis%20in%20OVS_OVN-Based%20Deployments%20Using%20AI_ML.pdf
Traditional network observability methods often rely on analytics and dashboards that do not provide adequate metrics at the Open vSwitch (OVS) or Open Virtual Network (OVN) level within virtualized shared environments. This lack of visibility, coupled with an absence of metric correlation to policies or resource allocation, makes the root cause analysis (RCA) process manual and labor-intensive. In large-scale clusters, where quick decision-making is essential, this approach is even more challenging. The integration of AI/ML offers a promising solution by automating decision-making and leveraging both historical and real-time data. This presentation explores key aspects of network observability in virtual infrastructure, demonstrating how AI/ML can enhance anomaly detection, troubleshooting, and overall efficiency in network management.

### ofproto/detrace - The missing link.
Speakers: Ales Musil, Dumitru Ceara, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t10 | video: https://www.youtube.com/watch?v=OP3F1o3ozjM | slides: https://www.openvswitch.org/support/ovscon2024/slides/ofproto_detrace%20-%20The%20missing%20link..pdf
OVS enables users to implement highly flexible and performant virtual networking solutions. The behaviour of the virtual network is often defined through (OpenFlow) rules that are configured on virtual OVS bridges. However, the actual forwarding of packets in the datapath doesn't happen by evaluating the OpenFlow rules. Instead, OpenFlow rules are translated by ovs-vswitchd to a different type of (optimized) datapath flows that do the actual matching and forwarding of packets. The relation between these datapath flows and the original OpenFlow rules that contributed to their creation is not always directly obvious to users. Especially in cases when users are debugging the forwarding plane making the link between datapath flows and OpenFlow explicit would improve the experience and reduce troubleshooting time. This talk will present a new functionality that was added to OpenvSwitch in version 3.4: the ofproto/detrace command. This command bridges the gap between the datapath forwarding rules and their OpenFlow counterpart. We will also showcase how this command can be used in conjunction with existing OVN tools in order to significantly streamline the debugging of OVN configured virtual networking forwarding rules.

### Harnessing Marvell Accelerators with OVS Hardware Offload for Accelerated Network Performance
Speakers: Harman Kalra, Jerin Jacob Kollanukkaran, Marvell
page: https://www.openvswitch.org/support/ovscon2024/#t11 | video: https://www.youtube.com/watch?v=80biE5L7jqw | slides: https://www.openvswitch.org/support/ovscon2024/slides/Harman-Jerin%20-%20Harnessing%20Marvell%20Accelerators%20with%20Open%20vSwitch%28OVS%29%20Hardware%20Offload%20for%20Accelerated%20Network%20Performance.pptx
This paper explores the synergy of Marvell hardware accelerators with Open vSwitch (OVS) hardware offloading to achieve enhanced network performance. The solution employs an OVS-offload-engine, an application designed to configure hardware and optimize software to deliver advanced features, which works in tandem with OVS. This engine offloads flows classified by OVS into dedicated Marvell Parser and CAM hardware. Initial or exceptional packets are processed by OVS, identified, and then installed into the CAM hardware, enabling subsequent packets to be matched and processed at the hardware level for optimal fast path performance. This offloading significantly reduces CPU load, resulting in faster and more efficient network operations. Marvell’s System on Chip (SoC) features various hardware accelerators, including the Network Interface Controller Unit (NIX), which provides controller and DMA engines for efficient packet processing. The NIX interfaces with the Network Parser and CAM Unit (NPC) block, parsing both standard and custom headers to form Match Content-Addressable Memory (MCAM) keys for match actions across 16K MCAM entries. The Network Pool Allocator (NPA) block manages memory pointers for packets, while the Cryptographic Acceleration Unit (CPT) offers inline IPsec by encrypting egress traffic and decrypting ingress traffic. OVS + offloading engine offers following advantages: Flow-based actions such as RSS, VLAN stripping/insertion, packet mirroring, and multicasting. Efficient IPsec Processing To leverage the inline IPsec capability of the Marvell SoC, the ovs-offload-engine intercepts SA/SP policies configured via strongSwan and offloads them to the hardware using DPDK rte_security APIs, enhancing OVS IPsec offloading capabilities. Connection Tracking offloading: The ovs-offload-engine efficiently compensates for the lack of offloading support for connection tracking in OVS DPDK Virtio Integration enables high-performance network throughput, achieving speeds of up to 100Gbps. Optimized Service Function Chaining Efficiently steering traffic through a sequence of service functions, such as firewalls, load balancers, and intrusion detection systems. Future Enhancements: NIX hardware supports hierarchical scheduling, shaping, coloring (up to five levels), and flexible packet formatting like LSO and checksum generation, enhancing OVS hardware offloading viz currently managed by software. These performance gains highlight the substantial benefits of integrating Marvell hardware accelerators with OVS hardware offloading, demonstrating the potential for enhanced speed, efficiency, and scalability in modern network environments.

### Inclusive Naming
Speakers: Simon Horman, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t12 | video: https://www.youtube.com/watch?v=WXrN1noYEs0 | slides: https://www.openvswitch.org/support/ovscon2024/slides/2024-11-21%20OVS%20Inclusive%20Naming.pdf
Language shapes our communication, and there are few things as important to a community as communication. This also applies to Open Source communities like Open vSwitch and OVN. Over time, for a variety of reasons, our community has normalised the use of various terms that on examination are not inclusive, which is not in keeping with the values of our community. This presentation will explore what steps OVS has taken towards acknowledging this problem, using more inclusive language. And what further steps could be taken.

### Improving megaflow cache performance in Open vSwitch with branch prediction
Speakers: Emil Stahl, KTH Royal Institute of Technology; Q&A portion hosted by Eelco Chaudron, Red Hat.
page: https://www.openvswitch.org/support/ovscon2024/#t13 | video: https://www.youtube.com/watch?v=hCVegvOWrqk
The evolution of software-defined networking has increasingly favored hardware implemen- tations for packet processing in data planes. Despite these advancements, optimizing the interaction between the data plane and the control plane, referred to as the slow path, re- mains a critical challenge. This interaction is poised to become a significant bottleneck in high-throughput networks. This talk explores potential optimizations of Open vSwitch (OVS) by employing coflows to anticipate imminent network traffic, thus reducing the latency-inducing upcalls to the control plane, which are typically triggered by cache misses in the OVS megaflow cache. The study involves a series of benchmarks conducted on an OVN-simulated, single-node OCP cluster. These benchmarks utilize XDP to timestamp packets at both ingress and egress points of the cluster, measuring latency across various traffic scenarios. These scenarios are generated using synthetic coflow traffic traces, which vary in flow size distribution. The findings provide a comprehensive analysis of how OVS’s performance is influenced by accurately predicting varying proportions of future flows under different traffic conditions.

### Userspace segmentation and checksum offload
Speakers: Mike Pattrick, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t14 | video: https://www.youtube.com/watch?v=UKcec6IgCvQ
In the past year there has been major progress towards improving support for segmentation and checksum offload in the userspace datapath. This support brings a sizable performance benefit, but also comes with several caveats and limitations. This presentation will discuss the current extent of this feature including version information and hardware support, performance across a variety of configurations, and possible future work.

### Tracing packets in OVS: an update on Retis
Speakers: Paolo Valerio, Adrian Moreno, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t20 | video: https://www.youtube.com/watch?v=K0ldVsWkLJw | slides: https://www.openvswitch.org/support/ovscon2024/slides/OVS_OVN%20Conf%2024_%20_Tracing%20packets%20in%20OVS_%20an%20update%20on%20Retis__%20.pdf
This presentation will explore Retis, a network debugging tool designed to track and visualize packets in Linux where OVS is a first class citizen. Integrating Retis with OVS has lots of challenges since part of OVS packet processing happens in userspace. We will introduce the latest advancements of Retis, especially focusing on those that enhance the visibility of traffic flowing through OVS. A demo will showcase the tool's capabilities and its newest features with particular emphasis on Open vSwitch. We will also present our future plans regarding OVS support for an open discussion.

### VM Migration Enhancements
Speakers: Naveen Yerramneni, Nutanix
page: https://www.openvswitch.org/support/ovscon2024/#t16 | video: https://www.youtube.com/watch?v=aHHK5RUcRCw | slides: https://www.openvswitch.org/support/ovscon2024/slides/OVN_VM_Migration_Enhancements.pptx
Contributors: Naveen Yerramneni, Shibir Basak, Mansi Sharma, Nutanix
There are multiple enhancements added to upstream recently which are helpful for VM migration use cases. In this talk, we want to explain in detail how these enhancements are useful during VM migration. * Logical Switch Port options: * pkt_clone_type * disable_arp_nd_rsp * force_fdb_lookup * disable_garp_rarp * Controller: Ability to reserve CT zone for ports which will useful to sync CT entries during VM migration.

### Introducing exact-match hardware offload for OVS
Speakers: Farhat Ullah, Farhan Tariq, Dreambig Semiconductor Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t17 | video: https://www.youtube.com/watch?v=bAIrGaNbBWk
The introduction of megaflows in OVS datapath was designed to increase flow lookup performance and avoid the slower exception path. OVS lookup is a compute intensive process. Offloading OVS lookup to the DPU is key to achieving high-speed networking in cloud computing environments. Currently, OVS offloads megaflows to hardware. While this offloading provides benefits, supporting the ever-growing number of megaflows in hardware poses challenges. Generally, a DPU would use TCAM for megaflows, but TCAMs have drawbacks when evaluated for power consumption and scalability. Alternative approaches to TCAM complicate maintenance and negatively affect performance, especially with increasing number of megaflow tables. In our talk, we present a solution that brings exact-match hardware offload in OVS, the best of micro and mega flows in OVS. We will showcase the potential of offload with a demonstration. We hope this approach helps to improve OVS data path lookup performance in DPU/SmartNIC environments.

### Composable Services in OVN
Speakers: Mark Michelson, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t22 | video: https://www.youtube.com/watch?v=Gf4M-ZSmTz4
Composable services are a new proposal from the core OVN team. The proposal seeks to extract certain functionality from existing OVN logical datapaths and implement them as standalone specialized datapaths. This talk will go over how composable services are expected to work, how they give administrators more clarity and power for processing packets with OVN, and how ACLs, NATs, and Load Balancers will be improved by this new functionality. We will also go over possible future offerings from composable services.

### Open vSwitch (OVS) performance case study - From software to hardware offloading, from kernel to userspace
Speakers: Salem Sol, Gaetan Rivet, NVIDIA
page: https://www.openvswitch.org/support/ovscon2024/#t6 | video: https://www.youtube.com/watch?v=_7YEmJrqJJE | slides: https://www.openvswitch.org/support/ovscon2024/slides/ovscon24-CT-offloads.pptx
Open vSwitch (OVS) has multiple ways in which it can be deployed and used, each mode has their own pros and cons in terms or performance. In this talk we will be demonstrating and comparing the key differences in performance (PPS, throughput, CPS) between each working mode (ovs-kernel/ovs-dpdk/ovs-doca) with and without offloads and highlighting their differences. This talk also describes an implementation of CT offloads using the DOCA framework [1]. The concept, requirements and limitations of the feature are explained as well as a short history of their integration in userspace OVS (OVS-DPDK). Each iterations of their implementation over the available DPDK or DOCA APIs are then compared using relevant metrics.

### (P)sampling kubernetes network policies
Speakers: Dumitru Ceara, Nadia Pinaeva, Adrian Moreno, Red Hat, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t19 | video: https://www.youtube.com/watch?v=gLwDsaiUuN4&t=2s | slides: https://www.openvswitch.org/support/ovscon2024/slides/OVS_OVN%20Conf%2024_%20_%28P%29sampling%20kubernetes%20network%20policies_%20.pdf
OVN drop debugging mode (introduced in OVN 23.03) demonstrated how OVN-driven per-flow sampling can enable a new kind of visibility applications based on packet samples that carry OVN-generated metadata providing crucial context: why OVN decided to do something. However, a key architectural aspect of the solution was limiting its use for general cluster observability: the use of IPFIX as export format requires samples to go from the kernel through ovs-vswitchd compromising the scalability of the system. A recent joint effort between OVS, OVN and OpenShift Networking teams, has enabled a new way of generating and consuming samples while overcoming the performance limitation. This technique has been used to improve observability of a common pain point in kubernetes deployments: Network Policies. In this presentation, speakers explain the recent changes in the kernel, Open vSwitch, OVN and ovn-kubernetes that have enabled live Network Policy visibility, show the feature in action and discuss how this technology can be used to implement other observability applications.

### Scalable Multi-Node AI Workloads in Multi-Tenant AI Clouds using SDN K8s Networking
Speakers: Leonid Grossman, Girish Moodalbail, NVIDIA
page: https://www.openvswitch.org/support/ovscon2024/#t15 | video: https://www.youtube.com/watch?v=68xaDx8mXqQ | slides: https://www.openvswitch.org/support/ovscon2024/Scalable%20Workloads.pptx
Within AI workloads, a few key traffic flows drive significant data movement between GPUs across nodes. Optimizing these flows for efficient bandwidth, low latency, and minimal jitter is critical to prevent GPU underutilization. Additionally, in the context of AI Cloud infrastructure, accommodating numerous users and concurrent AI workloads introduces competition for shared network resources, potentially impacting application performance. Hence, ensuring isolation between workloads within and across tenants is paramount. In this talk we will provide a quick overview of how we achieve network isolation (overlay virtual network topology) and efficient bandwidth (end-to-end QoS) between AI workloads using Open Source SDN solution, namely, Open vSwitch (OVS), Open Virtual Network (OVN), and OVN-Kubernetes CNI. Furthermore, with OVS-offloadable hardware the gains are much more significant.

### P4OVN: Offloading OVN to Intel IPU for Intel Developer Cloud
Speakers: Junho Suh, Intel, Inc.
page: https://www.openvswitch.org/support/ovscon2024/#t23 | video: https://www.youtube.com/watch?v=CgecMK9EhPU
In this talk, I will present P4OVN, a co-design of hardware and software to offload OVN into Intel IPU. For this, we implement a hardware flow cache in IPU's programmable packet processing engine for L2/L3 forwarding and connection tracking written in P4, and use IPU's compute tiles to run OVS for processing stateful packet processing such as ACL, NAT, LB. I also cover how we deploy and operate P4OVN for distributed virtual router, distributed NAT gateway and centralized NAT gateway in our networking service, plus OVN central to meet IDC scale requirements. Finally, I want to discuss how this work could be open-sourced to the community and how we encompass other vendors' solutions.

