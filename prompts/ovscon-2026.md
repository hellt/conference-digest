>>> HOW TO RUN THIS <<<
This is the digest prompt for ovscon-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ovscon-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ovscon-2026.md
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

Below is the program for Open vSwitch and OVN 2026 Fall Conference. Read it and produce a digest
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
conference: Open vSwitch and OVN 2026 Fall Conference
source_url: https://www.openvswitch.org/support/ovscon2026/
generated: 2026-11-09
registry_key: ovscon-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

### Lost in the Layers - Scaling OVN-Kubernetes User-Defined Networks from K8S API to the kernel
Speakers: Patryk Diak, Red Hat, LLC.; Dumitru Ceara, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t27
Scaling OVN-Kubernetes User-Defined Network workloads turned into a full-stack debugging exercise that touched every layer, from the Kubernetes API server down to the kernel. This talk is the unvarnished story of what broke, where, and why. We put each and every layer on trial and they all turned out to be guilty. They were all individually small misdemeanors but we had to address them ALL for improvements to be visible. Most of our time went into finding out which layer was failing, not into fixing it. We'll show the telemetry we wish we'd had from the start.

### A Unified Networking Fabric for VMs and Multi-Cluster Kubernetes workloads
Speakers: Sragdhara Datta Chaudhuri, Nutanix; Priyankar Jain, Nutanix
page: https://www.openvswitch.org/support/ovscon2026/#t12
Hybrid applications increasingly span virtual machines and workloads distributed across multiple Kubernetes clusters. This talk presents Nutanix’s experience building Flow CNI, a networking architecture based on OVN-Kubernetes and OVN-IC. It extends the VPC networking model across these environments, enabling VM and Kubernetes networks to participate in a common logical routing domain with federated service reachability while preserving the independent control-plane boundaries of each environment. The resulting fabric supports two related use cases: connecting VMs and Kubernetes pods within a shared VPC, and extending that VPC across multiple Kubernetes clusters. The architecture uses OVN connectivity hierarchically. Within a Kubernetes cluster, OVN-Kubernetes Interconnect mode distributes OVN control and datapath state across zones with local OVN databases. Across clusters – and between Kubernetes and the VM networks – OVN Interconnect links these independent OVN domains through transit switches and a shared interconnect database. The result is an “interconnect of interconnects”: each environment remains locally managed, while the VPC presents a unified logical network to the user. We will discuss the targeted enhancements made in OVN and OVN-kubernetes to achieve this model. Service reachability is bi-directional: OVN-IC advertises VM-side load balancer VIPs to Kubernetes and Kubernetes ClusterIP services to the VM domain. Each side forwards traffic across the OVN-IC transit path, while backend selection remains local to the destination domain. The presentation also explains cross-cluster DNS for ClusterIP services. A controller publishes service FQDNs, ClusterIPs, and VPC visibility to a shared OVSDB database, while a CoreDNS extension builds per-VPC views using the standard svc.cluster.local naming model. Attendees will leave with a practical model for building a unified networking fabric across VMs and multi-cluster kubernetes. The model federates independent OVN domains, exchanges routes and VIPs, and preserves local control-plane ownership while presenting a single VPC to users.

### One Tunnel Too Many: No-Overlay Mode in OVN-Kubernetes
Speakers: Riccardo Ravaioli, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t4
Geneve tunnels do a useful job. Sometimes, though, the network already knows the way. On fabrics that already provide an overlay, adding Geneve means sending packets out wearing two coats. This talk introduces no-overlay mode in OVN-Kubernetes, which lets the cluster default network and primary Layer 3 ClusterUserDefinedNetworks route traffic between nodes using BGP-learned routes, without Geneve encapsulation. OVN continues to provide local networking, network policy enforcement and Kubernetes Services. The choice is per network, so Geneve and no-overlay networks can coexist in the same cluster. We'll walk through the use cases, follow a packet across nodes, and compare administrator-configured BGP with the managed full-mesh option. We'll also cover the configuration choices that matter: outbound SNAT, MTU and tenant isolation. NVIDIA's DPU-based VM networking provides one concrete example. The feature is a joint effort between Red Hat and NVIDIA. Attendees will leave with an understanding of how no-overlay mode works, when to use it and which constraints shape deployment.

### OVNKubernetes Performance Workflows
Speakers: Joe Talerico; Mohit Sheth; Venkata Anil Kommaddi, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t1
In this talk we will update the community on our progress introducing performance and scale testing to the OVNKubernets upstream repository. We will share what we have built, how it works and our future plans. We would also like to use this opportunity to ask for feedback from users who have utilized the output from our continuous performance tests!

### From User Defined Networks to EVPN: Scaling OVN-Kubernetes
Speakers: Mohit Sheth; Venkata Anil Kommaddi; Joe Talerico, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t2
User Defined Networks place new scaling demands on OVN-Kubernetes. This talk presents the kube-burner workloads OpenShift PerfScale built to test L2/L3 UDN and CUDN density, churn, BGP route advertisements, and EVPN east-west and north-south connectivity. We will describe our multi-node testbeds—including external FRR peers, VTEPs, VRFs, and pod/VM traffic endpoints and a workload model spanning 100s of CUDNs, 1000s of namespaces and pods/VMs. We will cover CUDN allocation and pod-readiness latency, OVN NB/SB and OVS bottlenecks, BGP import/export timing, best practices and the improvements that increased achievable scale Attendees will leave with a repeatable methodology for measuring and troubleshooting OVN-Kubernetes tenant networking at scale.

### Two OVN-Kubernetes, One DPU
Speakers: Alin Serdean, NVIDIA; Igal Tsoiref, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t14
A DPU runs its own OS and its own Kubernetes node. Today ovn-kubernetes runs in DPU mode on the card and DPU-host mode on the host, both serving the host cluster, so pods scheduled on the DPU itself get nothing. That needs a second, full-mode instance on the same card. Each instance keeps its own OVN databases and its own Kubernetes API. Only what's actually shared gets split up. OVN has co-hosted ovn-controller since 23.03, and 26.09.0 drops the experimental tag. The hard parts: system-id is the one key that can't be made chassis-specific conntrack zones have to stay clear of the shared gateway zones management port names run out of room at 15 characters two instances can't share a gateway bridge, since ovnk owns its whole flow table bridges, nftables tables, metrics ports and socket paths all need an owner We'll walk the proposal and demo the prototype. [1] https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5861 [2] https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5354

### Ovens, freezers, and radiofrequency cavities: The ongoing migration of the CERN Cloud to OVN
Speakers: Christopher Barnes, CERN; Richard Bachmann, CERN
page: https://www.openvswitch.org/support/ovscon2026/#t25
The European Laboratory for Particle Physics (CERN) maintains a private cloud built on OpenStack to help facilitate its research and provide for much of its computational needs. This cloud comprises 1.4k hypervisors, is home to 15k virtual machines, and hosted on-site across two separate data centres at the border between France and Switzerland. At this time, the CERN cloud is in the middle of having its networking migrated from LinuxBridge to OVN. In this talk we will share our experiences from the migrations so far, which includes adjustments to our deployment made along the way, issues we ran into, and still open questions where we would appreciate input from the community.

### How we are scaling Crusoe cloud using OVN interconnect approach
Speakers: Numan Siddique, Crusoe; Ketan Supanekar, Crusoe
page: https://www.openvswitch.org/support/ovscon2026/#t15
In this talk we will cover - our present architecture using the OVN relays and briefly highlight the bottlenecks we found - the new re-architecture based on the ovn-kubernetes model of OVN Interconnect - the options we evaluated for our control plane - k8s api-server/etcd with custom CRDs and NAT KV store and which option we chose and why - And finally discuss with the community if we can solve the central OVN SB db bottlenecks by using k8s api-server/etcd, NATS KV (or other options).

### ovn-cp-bench: A Single-Host Testbench for OVN Control-Plane Scale
Speakers: Vinicius Marques Rodrigues, CERN
page: https://www.openvswitch.org/support/ovscon2026/#t20
Every change to a large OVN deployment, whether an upgrade, a backport or a new network feature, raises the same question: what will it cost the control plane at scale? Answering it usually means a multi-host fleet or a production canary. ovn-cp-bench reproduces cloud-scale control-plane load on a single host. Most chassis are simulated as Southbound rows, invisible to ovn-northd yet free at runtime, while a few real ovn-controllers measure the controller hop. Any OVN build can be compared on the same state, with controlled, statistically sound trials. We present the design, what a single host can and cannot measure, and first case studies across releases and topologies. We also show how the testbench is meant to evolve alongside the platform it models.

### A Switch, a Load Balancer, and an ACL Walk into a Pipeline…. And Conntrack Ruins Everything
Speakers: Surya Seetharaman, Red Hat, LLC.; Nadia Pinaeva, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t10
User Defined Networks (UDNs) in OVN-Kubernetes provide strong tenant isolation — each UDN is an independent OVN topology island. However, isolation is not always the end state: address space exhaustion, inter-team service access, and platform migrations all require controlled connectivity between these islands. ClusterNetworkConnect (CNC) is a new admin API added in OVN-Kubernetes v1.3 that declaratively connects isolated UDNs — with full pod-to-pod connectivity, service-only access, or both. Connectivity is symmetric but non-transitive. This talk covers the design in three parts. First, the OVN topology: a distributed transit router is peered with each connected network's router using point-to-point subnets carved deterministically from a user-configured CIDR. Second, services across networks: load balancers are added to the switches of connected networks so cross-network DNAT works with the existing routing. Third, an ACL puzzle: you can easily allow service traffic while dropping direct pod-to-pod with a pass action, right? Join our talk to see how interaction between load balancers on switches, conntrack, and ACL evaluation order has other ideas. We walk through what breaks, the workaround we shipped, and why finding the long-term fix isn't easy.

### Stateless Load Balancing in OVN
Speakers: Alexandra Rukomoinikova, K2 Cloud
page: https://www.openvswitch.org/support/ovscon2026/#t24
Stateless load balancing in OVN is not a new idea: the use_stateless_nat option already exists, but its limitations (reply traffic is SNATed 1:1 to the VIP, so a backend cannot serve more than one VIP) kept it from solving the real problem - conntrack state on the gateway chassis pins every connection to one node and prevents gateways from scaling horizontally. This talk is the story of how we got from there to the new "deferred-nat" load balancer option: the approaches we considered (conntrack synchronization, extending use_stateless_nat, cross-AZ backends, moving the NAT off the gateway) and why we settled on the last one. The backend is selected statelessly per packet on the router, the packet is delivered to it by MAC, and the DNAT and conntrack state are created on the backend's own hypervisor. To keep established sessions alive when backends change, select groups are updated incrementally instead of being rebuilt. Finally, how we use this in production and what is left to do.

### OVN Network Function Enhancements - VTAP and Active-Active Load Balancing
Speakers: Sragdhara Datta Chaudhuri, Nutanix; Naveen Yerramneni, Nutanix; Aditya Mehakare, Nutanix
page: https://www.openvswitch.org/support/ovscon2026/#t5
This talk covers recent and ongoing work that extends OVN’s network function capabilities with Virtual TAP (VTAP) and active-active load balancing. VTAP, available in OVN 26.09, enables users to mirror selected traffic to a Virtual Network Function (VNF). Traffic matching a configured access list, along with the corresponding response traffic, is cloned and delivered to the VNF, while the original traffic continues through the normal logical-switch pipeline. This provides a flexible mechanism for use cases such as traffic inspection, network monitoring, intrusion detection, and passive security analysis. Active-active load balancing is being added for both inline and VTAP mode VNFs. The proposed approach allows traffic to be distributed across multiple healthy VNF members instead of selecting a single member. Flows are consistently mapped to the same VNF instance in both directions, ensuring that request and response traffic are processed by the same service instance. Existing connections remain associated with their original VNF even when the set of active VNF members changes. Together, these enhancements provide better traffic visibility and improve the scalability of OVN network function.

### 99 Patches, but Reviews Ain't One
Speakers: Eelco Chaudron, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t16
Ever wondered what happens after you send a patch to ovs-dev at openvswitch.org? This lightning talk follows a patch from submission to merge, and takes an honest look at who is doing the reviewing along the way. We will share some numbers on the current review workload, show where the bottlenecks are, and make the case that community review is not just helpful but essential to keep OVS healthy, get patches merged faster, and spread knowledge across the project. Whether you are a first-time contributor or a seasoned developer, there is a role for you in the review process, and it is easier to get started than you might think.

### Keep Calm and Learn Autotest! Or should you..?
Speakers: Ilya Maximets, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t21
CI takes a long time. Especially the OVS and OVN system tests. In this talk we explore ways to make it faster by doing less and running more things in parallel, perhaps even hot-swapping the entire engine!

### One API to Rule Them All: Reworking the OVS Hardware Offload Layers
Speakers: Eelco Chaudron, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t22
Open vSwitch (OVS) historically supported hardware offload through implementations tightly coupled to the dpif-provider layer. While this approach worked, it led to a rigid model where each provider integrated offload capabilities in its own way, making it harder to extend and share functionality across vendors. OVS supported multiple backends for offload: the kernel datapath leveraged the TC flower classifier, while the userspace datapath integrated with DPDK using rte_flow. Both paths exposed their functionality through the netdev-offload APIs, but the design resulted in duplicated logic and limited opportunities for consistency and reuse. Vendor-specific capabilities had to be reimplemented in each provider, and adding new offload features required invasive changes in multiple places. This talk presents the new dpif-offload API layer that has since landed in OVS. It provides a unified and more flexible abstraction for hardware offload that sits above the provider-specific implementations. By centralizing offload handling, we have simplified vendor integration, reduced duplication, and enabled more extensible offload pipelines. We will walk through the architecture, cover the migration from the old netdev-offload model, and look at what this foundation enables going forward.

### Conntrack: Semantics and Scale
Speakers: Aaron Conole, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t23
Conntrack was introduced to Open vSwitch in 2014 and 2015 to provide stateful flow processing, grouping related packets together and as a result, reducing the amount of flows in the flow table through this grouping. However, it has evolved over the years into a way to provide a useful L3/L4 interface into the OpenFlow pipeline. In this talk we'll explore the questions that are currently being asked of conntrack: What behaviors need to be common across all conntrack implementations? How can the userspace implementation scale to meet the modern demands placed on it? How can it work with hardware to extend the ct() interface through an acceleration path? In this talk, we'll look at how conntrack has changed over the last decade, and the ongoing work to answer the above questions. We'll look at what work has been done, and what remains to be merged upstream, and we'll show how others can get involved.

### dpdk conntrack performance
Speakers: Felix Huettner, Schwarz Digits
page: https://www.openvswitch.org/support/ovscon2026/#t19
In the previous talk we moved from kernel based ovs to dpdk and found that conntrack was the performance wise most problematic part of ovs. We will take a look at the different problems we observed as well as improvements made.

### Same Flow, Same Path: Software/Hardware Hash Alignment
Speakers: Eli Britstein, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t13
In this brief talk, I will cover a long-standing hardware-offload problem in OVS: software and hardware can compute different values for the UDP tunnel source port (VXLAN, Geneve) and for dp_hash used in select-group load balancing. This happens whenever a flow is handled by both paths — the first packet of a flow is by definition processed in software before the flow gets offloaded, and later packets take the hardware path, and similarly when flows are only partially offloaded. The result is inconsistent ECMP, asymmetric traffic, and steering that can fail to converge. I'll briefly recount the history, including why earlier attempts to solve this in the kernel datapath never went through, and show how the userspace datapath, the dpif-offload provider framework, and DOCA offload finally make a clean solution possible via optional provider callbacks. The patches were implemented by Eelco Chaudron.

### Targeted Megaflow Revalidation in Open vSwitch
Speakers: Gaetan Rivet, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t28
Open vSwitch revalidators keep datapath megaflows consistent with the OpenFlow tables and the switch state. Periodic revalidation is inexpensive, as xcache allows statistics to be updated without retranslation. After a configuration change, however, all megaflows are translated again, whether or not the change can affect them. In large deployments, this cost adds to the pressure on flow-capacity control and can lead to the eviction of useful datapath flows. In some cases, this added pressure can destabilize the revalidators and lead to a megaflow population collapse. The cache must then be rebuilt while the system is already overloaded. This problem has limited the scale of our Open vSwitch deployments at NVIDIA. This talk presents targeted megaflow revalidation, a feature implemented in the OVS-DOCA fork. It records the reasons for each revalidation and extends xcache to track the dependencies of each megaflow, so that only the megaflows affected by a change are translated again. We will explain the design and the challenge of tracking megaflow dependencies completely, including indirect and negative dependencies such as watched ports and missing groups. We will describe how AI-assisted testing helped cover the dependency matrix. Furthermore, this feature gives controller developers a way to structure their OpenFlow pipeline to bound the impact of changes to its configuration. Finally, we will place this work in the wider effort to stabilize revalidation. We intend to propose the existing implementation upstream, while work continues on an improved control law for the remaining flow-capacity instability.

### Upgrading network control plane and ovs-vswitchd with kernel datapath without impacting users
Speakers: Aleksandr Ankudinov, Nebius
page: https://www.openvswitch.org/support/ovscon2026/#t6
When using a large public cloud, users do not want to know about or feel the impact of the upgrades of the infrastructure underneath. We have 3 main components: Our vpc-agent, that programs ovs-vswitchd ovs-vswitchd ovs kernel module In this talk we discuss: several simple, but clever tricks we use to let restarting vpc-agent syncronize openflow tables and groups into desired state, while current flows allows traffic to continue working, including: using cookies to store "version" to easily clean up flows, that are not actual anymore storing information that must be saved between restarts using openflow note action allocating group IDs thinking about the future when allocating things with limited bits doing the forbidden: running two ovs-vswitchd in parallel during upgrade (using flow-restore-wait flag): how to make ovs-vswitchd fight each other, and how to make them stop funny things that happen when you forget to create internal port for the bridge how we do all of this in Kubernetes, which adds its own share of oddities. or nobody guarantees that new container will start in reasonable time (Un)fortunately, we do not hot-upgrade OVS kernel module. But as a bonus, if you happen to need to and we have time, I have one crazy scheme with loading two OVS modules at once, that might theoretically work. Bonus #2: what about local services? See the next talk.

### ovn-local: A new proposed architecture for OVN
Speakers: Mark Michelson; Ilya Maximets; Dumitru Ceara; Ales Musil, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t26
Since the creation of OVN, its feature set has ballooned, and its most common deployment types have changed drastically. The result is that the current architecture may not be the best fit any longer. This talk proposes a new way by which OVN will be deployed. It proposes a leaner footprint, with fewer processes and fewer databases. The benefits would mean easier deployment and upgrades, faster processing, and reduced memory and disk space requirements.

### Rebuilding an OpenFlow Controller in Rust
Speakers: Or Mazza, NVIDIA; Quentin Barrand, NVIDIA; Alin Serdean, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t17
HBN turns a BlueField DPU into a hardware-accelerated switching and routing platform. Its controller translates routing, switching, security, and NAT configuration into OpenFlow rules for Open vSwitch. We rewrote this controller from C to Rust while preserving binary compatibility. Our goals were better memory safety, concurrency, and testability, along with easier maintenance. The rewrite also delivered measurable performance gains: insertion rates increased by 8%, deletion rates by 14%, and flow statistics collection became 57% faster. In this talk, we’ll explore why we chose Rust, how we introduced it without disrupting users, and practical lessons learned from running HBN in a real DPU networking platform. We would also like to open the debate on implementing parts of OVS in Rust. We’ll discuss where it might fit, what bindings to existing C code would be required, and whether the benefits we saw in HBN could carry over to OVS.

### Death by Kernel locks: Hyperscalers road to DPDK
Speakers: Florian Werner, Schwarz Digits; Felix Huettner, Schwarz Digits
page: https://www.openvswitch.org/support/ovscon2026/#t18
We are migrating all of our OVN gateway chassis from kernel based netlink bridges to dpdk bridges. In this talk we will share what brought us on this path, pitfalls we found during migration and fancy performance comparisons between the two.

### Route scope delimitation as a control plane scalability mechanism for OVN Interconnect using route tags
Speakers: Lucas Vargas Dias, Magalu Cloud; Julio Cesar Vanti, Magalu Cloud
page: https://www.openvswitch.org/support/ovscon2026/#t9
When VPCs must be peered across availability zones with OVN Interconnect, the obvious way to keep each pair's routes to itself is topological: give every peering its own transit switch, so that route distribution is bounded by who is attached to which L2 domain. The alternative is to put every router on a single shared transit switch and scope route exchange declaratively, with options:ic-route-tag on the advertising side and options:ic-route-learn-tag-rules=allow:<tags> or ic-route-filter-tag on the learning side. The first approach is intuitive and provides isolation in the data plane. It is possible to show that it also produces 2.56x as many Southbound logical flows for identical connectivity, and that this increase results in additional latency on every operation where northd's engine falls back to a full recompute of the lflow node. The practical conclusion is that route scoping lets an operator buy isolation in the control plane instead of in the topology, and that doing so is substantially cheaper - not only in memory, but in the latency of every unrelated northbound write, in flow-installation time after a reconnect, and in the cost of the full recomputes. The trade-off must be stated plainly: on a shared transit switch, tag-based scoping constrains route learning only. The VPCs share one L2 domain, so a manually configured static route can still reach across it. Where isolation must hold in the data plane, the per-pair topology remains necessary, and our measurements quantify what that guarantee costs.

### One Shared Gateway, a Thousand Routers: Scaling ARP/NDP in OVN-Kubernetes
Speakers: Jaime Caamano, Red Hat, LLC.; Matteo Dallaglio, Red Hat, LLC.; Tim Rozet, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t11
This talk tells the story of an ARP and NDP scaling problem uncovered while scaling user-defined networks in OVN-Kubernetes. A cluster may have hundreds or thousands of user-defined networks, each with its own gateway router, while those routers share the same physical uplink, IP address, and MAC address. On the shared gateway bridge, OVN-Kubernetes must deliver neighbor-discovery traffic between the physical network and many logical-router patch ports. These packets do not carry enough context to identify the originating user-defined network. In particular, an ARP reply cannot be tracked with conntrack and mapped back to the router that sent the request. The historically safe option has therefore been to fan the traffic out to every relevant patch port. At scale, a single reply can pass through several router pipelines, duplicate learned neighbor states, expand the OpenFlow footprint, and eventually exceed OVS recirculation limits. We will trace how this behavior surfaced at scale, the constraints that any solution must preserve, and the approaches explored in OVN-Kubernetes to reduce fan-out without changing neighbor-resolution semantics. We will cover the short-term flow fix that constrains ARP/NDP fan-out on the shared gateway bridge, and the mid-term prototype that steers discovery through the default gateway router and propagates the learned bindings to the user-defined networks. Finally, we will present OVN’s Shared MAC-binding scopes. Related logical router ports can use a common set of learned neighbor bindings, avoiding per-router duplication. This allows OVN-Kubernetes to learn through a single gateway router and steer ARP/NDP traffic to it instead of fanning that traffic out to every gateway router. Join us to trace an ARP storm from the OpenFlow tables where it started to an emerging OVN feature, shaped by the OVN and OVN-Kubernetes communities working together to solve it at the right layer.

### Teaching AI to Debug OVN: Layer-Aware Troubleshooting with the ovn-kubernetes MCP Server
Speakers: Keshav Kabra, NVIDIA; Surya Seetharaman, Red Hat, LLC.
page: https://www.openvswitch.org/support/ovscon2026/#t8
Diagnosing OVN-Kubernetes incidents means connecting state across many layers: Kubernetes objects, OVN Northbound and Southbound databases, OVS flow tables, and kernel networking. Failed port bindings, broken Geneve tunnels, MTU mismatches and misapplied ACLs often show up only as indirect symptoms. Engineers then have to piece together the cause by hand from logs and CLI output. This talk introduces the ovn-kubernetes MCP server, a community project that exposes these layers to AI agents as structured, read-only tools. The tools wrap ovn-nbctl, ovn-sbctl, ovn-trace, ovs-ofctl and ovs-appctl, plus Kubernetes and kernel-networking state. The server works on live clusters and also offline, by parsing must-gather and sos-report artifacts. We cover the design choices behind it: wrapper tools instead of generic exec, least-privilege access, and grouping tools by layer. We then show an agent tracing a symptom from a pod to its logical and physical data path to find the root cause. Attendees will learn practical patterns for exposing OVN/OVS primitives through MCP. They will also see where AI-assisted triage helps and where human checking is still needed.

### Network Security with Address-set synchronisation across Kubernetes Clusters and VMs
Speakers: Sragdhara Datta Chaudhuri, Nutanix; Mansi Sharma, Nutanix
page: https://www.openvswitch.org/support/ovscon2026/#t7
Security policies become difficult to express and enforce when applications span VM networks and Kubernetes workload across multiple clusters. Administrators want to express policy using stable workload identities–such as Kubernetes labels and VM categories–while the data plane must enforce those policies against ever-changing IP address states distributed across independent OVN domains. In this model, a VPC is a single logical routing, service-discovery, and security-policy domain for workloads distributed across multiple Kubernetes clusters and VM environments, while each environment retains its own control plane. The talk focuses on applying a consistent security policy across this shared VPC even though each control plane has visibility into workloads in its own domain. OVN Interconnect provides the federation substrate while ACLs keep the enforcement local. A central management service (CMS) creates only high-level, static policy intent: Kubernetes pod and service selectors and VM categories or tags identify the endpoints. Each control plane independently resolves those selectors and VM attributes into local OVN address-sets. Selected local address-sets are then advertised and learned across control planes through OVN Interconnect, preserving local ownership of endpoint discovery and policy enforcement. The talk concludes with a concrete example of a unified policy matching applications across different Kubernetes clusters and VMs. We show how that policy is implemented using OVN ACLs together with local Address_Sets and learned Address_Sets, and how membership changes propagate without requiring the CMS to manage individual workload IP addresses. This model is well suited to production environments because the security policy remains stable as pods are rescheduled, clusters scale out, or workloads move between nodes—the relevant address sets are updated automatically while the ACL itself remains unchanged.

### HBN: Hardware-Accelerated DPU Networking with Open vSwitch
Speakers: Emeel Hakin, NVIDIA; Quentin Brrand, NVIDIA; Alin Serdean, NVIDIA
page: https://www.openvswitch.org/support/ovscon2026/#t3
NVIDIA’s Host-Based Networking (HBN) [1]turns the BlueField DPU into a hardware-accelerated router and network-services platform. It combines Cumulus Linux and the FRR BGP daemon to deliver a proven control plane backed by hardware-accelerated packet processing in OVS-DOCA. At its core, HBN is an OpenFlow controller that translates control-plane events, from BGP updates to configuration changes, into OpenFlow flows and groups. Extensions to Open vSwitch (OVS) make it possible to support switching, routing, VRFs, VXLAN, ECMP, ACLs, and traffic shaping within a single packet-processing pipeline. HBN can run independently as an underlay router or alongside other OpenFlow controllers, including OVN. By connecting separate OVS bridges, it enables service chaining and lets operators combine HBN with other networking services. In this talk, we’ll look inside HBN’s architecture, trace how control-plane updates become hardware-accelerated forwarding decisions, and explore the OVS extensions that make it all work. We’ll also share HBN’s scale and performance results, including OpenFlow flow-insertion rates and statistics.

