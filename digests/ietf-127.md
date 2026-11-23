<!--
conference: IETF 127 (San Francisco)
source_url: https://datatracker.ietf.org/meeting/127/agenda.json
generated: 2026-11-23
registry_key: ietf-127
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 127 (San Francisco)

A program dominated this cycle by AI/HPC fabric problems arriving at the IETF in force — RoCEv2 load balancing, rate advice, adaptive routing, scheduler-to-network intent, and a standout OpenAI deployment talk — alongside the usual steady work on BGP/EVPN scaling, IPv6 host architecture, and telemetry.

## Core

### Resilient AI Supercomputer Networking using MRC and SRv6

**Links:** [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-srv6ops-21-resilient-ai-supercomputer-networking-using-mrc-and-srv6-01) · [Session recording](https://youtu.be/hHcPOklRq1Y) · [Materials](https://datatracker.ietf.org/meeting/127/session/srv6ops)

Mark Handley (OpenAI), presentation at srv6ops; no Internet-Draft linked.

- **Why**: A rare public look inside a production 100K+ GPU training fabric, and the clearest statement of the "dumb switches, smart NICs" architecture — the pole opposite to the network-intelligence drafts elsewhere in this program.
- **What**: OpenAI's deployed backend: a 2-tier multi-plane Clos (512 T0s × 8 planes, 256 T1s, 131,072 GPUs, full bisection within a building, T2 cross-building), with ~10 million optical links routed via SRv6 — IPv6-in-IPv6, almost all uN uSIDs, no SRH, all statically routed at commissioning and never changed. Transport is MRC (RoCE Multipath Reliable Connection, an OCP standard from AMD, Broadcom, Intel, Microsoft, OpenAI and Nvidia): packet spraying over SRv6, out-of-order delivery, adaptive load balancing, packet trimming, selective retransmission, congestion control. The explicit north star is minimizing 100th-percentile latency — medians don't matter, since any flow missing its transfer window slows the whole synchronous job.
- **How**: Sender sprays each flow round-robin across a set of 256 SRv6 paths (plus a backup path list); congested paths are evicted on ECN/Trim/NACK and replaced from backup; probes re-admit paths over time. uSID allocations encode tier/plane/port; T2 does plain IP forwarding because parallel T1–T2 paths caused unwanted path mixing (uN+uA wasn't feasible at line rate in some switches).
- **Where applicable**: OpenAI-specific production deployment, dependent on MRC-capable NICs and SRv6 uSID support across mixed silicon (TH5/TH6, Spectrum 4/5/6; EOS, Cumulus, SONiC). The transferable insight is the philosophy — keep the fabric simple and static, put adaptation in endpoints — which is directly at odds with switch-driven adaptive routing; watch which way the industry splits.

### A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-a-rocev2-flow-level-load-balancing-method-based-on-the-ipv6-flow-label-00) · [Session recording](https://youtu.be/nExK52_b_RE) · [Materials](https://datatracker.ietf.org/meeting/127/session/6man)

Jiayuan Hu (presenter), Jie Dong, Yao Liu, Xia Gong.

- **Why**: AI/HPC training increasingly spans data centers over DCI, and RoCEv2's parallel RDMA sessions from one host share an identical 5-tuple — ECMP hashes them all onto one path, the elephant-flow problem at its worst.
- **What**: The ingress network device at the DCI/WAN edge rewrites the (zero) IPv6 Flow Label so downstream ECMP can hash on "5-tuple + Flow Label". Revision -04 tightened the rules: relabeling is done by the ingress device, not the host (hosts send Flow Label 0); existing non-zero labels MUST NOT be overwritten; QP-based labeling is configurable and disabled by default. Two hash-input cases because DETH (hence Src_QP) is absent in RC service: with DETH, {Src_QP || Dst_QP || address entropy} (80 bits); without, {Dst_QP || entropy} (56 bits).
- **How**: CRC-32/ISO-HDLC (hardware-friendly) over the QP numbers plus the low 16 bits of source/destination IPv6 addresses; the low 20 bits of the hash are written into the Flow Label.
- **Where applicable**: IPv6 RoCEv2 crossing DCI/WAN edges where the edge device can parse BTH/DETH at line rate; transparent to hosts and OS stacks, touches neither addresses nor ports (NAT/firewall-safe). One documented security departure from RFC 6437 (label predictability). Intra-DC fabrics solve this differently — via NIC spraying — which limits this to the WAN/DCI edge.

### Enhanced ECMP for AI Cluster

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-14-enhanced-ecmp-for-ai-cluster-00) · [Session recording](https://youtu.be/CKWa3STuXj8) · [Materials](https://datatracker.ietf.org/meeting/127/session/rtgwg)

Weiqiang Cheng, Xiaodong Duan, Rui Zhuang (China Mobile); Changwang Lin (New H3C Technologies).

- **Why**: AI training fabrics carry few, very large flows, so per-flow ECMP hash collisions hurt disproportionately; this is the operator attempt to standardize finer-grained distribution without packet reordering.
- **What**: Two configuration-driven grouping methods (the draft was converted to informational after IETF 123/126 feedback — protocol extensions removed): (1) ingress-interface grouping, hashing within groups of ingress ports so different source interfaces land on different ECMP members, suited to balanced per-GPU traffic; (2) egress-group based, where the egress leaf signals a GroupID in routes and ingress maps flows to subgroups of ECMP ports. Requesting WG adoption.
- **How**: Pure forwarding/hashing-plane grouping plus a GroupID carried in routing; no per-packet operations, so no reordering.
- **Where applicable**: Leaf-spine AI fabrics with regular GPU attachment — the premise "traffic per GPU is relatively balanced" does real work here, and the slides carry no quantitative evaluation, so treat it as a framework proposal, not a validated technique.

### Adaptive Routing Framework

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-adaptive-routing-framework/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-13-adaptive-routing-framework-00) · [Session recording](https://youtu.be/CKWa3STuXj8) · [Materials](https://datatracker.ietf.org/meeting/127/session/rtgwg)

Weiqiang Cheng, Rui Zhuang (China Mobile); Changwang Lin (New H3C Technologies); Kevin Wang (Juniper).

- **Why**: ECMP hashing on local link quality can't see remote congestion; this framework is where multi-vendor adaptive-routing semantics — including pushing decisions to the NIC — are being negotiated.
- **What**: Revision -06 adds an Endpoint Plane: NICs/servers receive Remote Path Info (BGP next-next-hop identifiers, or IGP interface info) and congestion notifications, and can shift traffic between planes in multi-plane (dual-uplink NIC) architectures — the same "smart endpoint" direction as MRC, but standardized. Three modes: weight-based dynamic ECMP (local+remote link quality, existing flows untouched), flow redirection (rehash specific congested elephant flows), and per-packet least-loaded (may require receiver reordering). Loop-free path formation is out of scope.
- **How**: Routing plane correlates routes with remote path info; a congestion-detection component notifies neighbors; forwarding weights derive from local and remote queue state.
- **Where applicable**: Framework draft for multi-plane Clos fabrics with endpoint participation; vendor-neutral, no deployment data yet — its value is as the container in which the network-vs-endpoint-intelligence argument gets resolved.

### SCONE-Based Rate Advice for RoCEv2 Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-zz-scone-rate-advice-rocev2/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-scone-scone-based-rate-advice-for-rocev2-networks-00) · [Session recording](https://youtu.be/JAQzbGFTm90) · [Materials](https://datatracker.ietf.org/meeting/127/session/scone)

Guangyu Zhao, Cheng Zhou, Tianji Jiang (presenter).

- **Why**: DCQCN gives senders only a binary ECN mark, and over cross-DC RTTs of tens of milliseconds its reaction is too late — the slides claim throughput can drop to nearly zero at 20 ms RTT with 0.1% loss. Quantitative, network-computed rate guidance is what the SCONE WG is standardizing.
- **What**: Two complementary granularities. Solution 1: path-level (per source-IP) Rate Advice sent out-of-band as a new UDP message directly from switches to the sender — sub-RTT feedback, well-suited to inter-DC. Solution 2: per-QP Rate Signal carried in a BTH extension on the RoCEv2 data path, with the receiver returning per-QP advice (the SCONE feedback-loop model, but for RoCEv2), better suited intra-DC. Advised rates come from configured policy (SLA/TE limits) or computed from egress queue depth/delay/loss; how the sender coordinates the advised ceilings with its DCQCN target rate is still TBD.
- **How**: Sol1 message is {Version, Rate(Mbps), SourceIP} on a new UDP port; Sol2 keys advice via the BTH Src/DestQP so each queue pair gets its own rate.
- **Where applicable**: Requires a SCONE charter extension beyond QUIC (proposed at this meeting), a new IANA UDP port, and for Sol2 a NIC/protocol-stack BTH extension coordinated with IBTA — so the near-term applicable piece is Sol1 for cross-DC RoCEv2 over dedicated lines/SRv6 tunnels.

### Export of RoCEv2 Base Transport Header (BTH) Information Using IP Flow Information Export (IPFIX)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-lin-opsawg-ipfix-rocev2/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-opsawg-8-export-of-rocev2-base-transport-header-bth-information-using-ipfix-00) · [Session recording](https://youtu.be/DKWy3lZ2Yw8) · [Materials](https://datatracker.ietf.org/meeting/127/session/opsawg)

Changwang Lin (New H3C), presented by Haiyang Zhang (New H3C); Aditya Dogra (Cisco Systems).

- **Why**: AI fabrics are largely invisible to flow monitoring — IPFIX has no way to say "this is QP 0x123 on P_Key 0xffff", which makes RDMA congestion triage guesswork.
- **What**: Seven new IPFIX IEs (opcode, partition key, destination QP, PSN, plus raw octets at offsets 1/4/8), with two export profiles: per-packet observation (no flow keys, includes PSN) and aggregate-flow (flow keys are outer IP/ports, direction, P_Key and Dst QP; PSN excluded). Careful semantics throughout: recognition must validate beyond UDP 4791 (Annex A17 context, complete 12-octet BTH, version 0); a PSN gap alone does not prove loss; Dst QP is endpoint-local and must not be reversed into a Src QP.
- **How**: Registry additions plus profile rules; exporters are warned about parse cost (sampling, rate-limiting, hardware acceleration) and pointed at TLS/DTLS across trust boundaries.
- **Where applicable**: Any IPFIX deployment that wants RDMA transport context; explicitly complementary to IOAM and Alternate Marking, and pointedly not a measurement of PFC pause, loss, or delay.

### HPC/AI Scheduler Job Metadata Model

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xkk-rtgwg-hpc-scheduler-job-metadata/) · [Session recording](https://youtu.be/CKWa3STuXj8) · [Materials](https://datatracker.ietf.org/meeting/127/session/rtgwg)

Quan Xiong (ZTE); Kireeti Kompella (HPE); Daniel King (Lancaster University).

- **Why**: Before a network can admit or place AI/HPC job traffic, it needs the job context — and today that context is trapped in platform-native formats (Slurm queues, Kubernetes namespaces, Kubeflow CRDs).
- **What**: A YANG model (ietf-hpc-scheduler-job-metadata) capturing scheduler identity (Slurm, PBS, LSF, Kubernetes, Kubeflow, Ray, Volcano, Kueue, Base Command...), submitter/tenant/project/namespace, workload (type — training/inference/data movement — framework, priority, queue, correlation-id), job/task structure with roles (worker, parameter-server, master), and timing (earliest start, deadline, requested duration). It deliberately only identifies and describes the workload; a full worked example maps a Kubeflow-on-Kubernetes distributed training job onto the model.
- **How**: Platform-neutral groupings mapped from heterogeneous workload managers, with correlation identifiers tying metadata to service intents.
- **Where applicable**: Any HP-WAN or network controller consuming scheduler context; its value is realized only together with the companion service-intent model below.

### HPC/AI Service Intent Model

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xkk-rtgwg-hpc-service-intent/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-10-hpc-scheduller-job-metadata-service-intent-00) · [Session recording](https://youtu.be/CKWa3STuXj8) · [Materials](https://datatracker.ietf.org/meeting/127/session/rtgwg)

Quan Xiong (ZTE); Kireeti Kompella (HPE); Daniel King (Lancaster University) — presented jointly with the job-metadata model.

- **Why**: The other half of scheduler-network integration: how a workload manager expresses what connectivity a job needs without speaking tunnel dialects.
- **What**: A common service intent model for HPC/AI over high-performance WANs: endpoints, communication pattern, timing, performance, data movement, policy and admission requirements — "without exposing technology-specific tunnel realization details". The hierarchy is job metadata (identifies the workload) → service intent (requests the network service) → tunnel realization (network resources for the admitted intent), with controller admission state flowing back.
- **How**: Service intent instances reference job metadata via workload/job/correlation identifiers; multiple intents can attach to one workload, and one intent can be updated without touching the metadata.
- **Where applicable**: Cross-DC AI training, checkpointing and dataset movement — directly relevant to DCI strategy for AI platforms; early-stage (individual drafts, seeking comment).

### TCP Packet Trimming Extension

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-tcpm-tcp-packet-trimming-00) · [Session recording](https://youtu.be/XRBR6ORihRs) · [Materials](https://datatracker.ietf.org/meeting/127/session/tcpm)

Flavius Mazilu, Valentin Bobaru, Costin Raiciu (Politehnica University of Bucharest, UPB).

- **Why**: Modern DC switches (including those in OpenAI's MRC stack, above) already trim payloads under buffer pressure instead of dropping; TCP can't consume that explicit, sequence-numbered loss signal, so it falls back to dup-ACK/RACK inference.
- **What**: Revision -01 consolidates to a single TCP option doing both capability negotiation (in the SYN, with in-band signaling of the configured trimmable/trimmed DSCP values) and NACKs (distinguished by option length). Notable findings: trimming and TCP-AO are mutually exclusive (spoofed trims could otherwise shrink cwnd via authenticated NACKs), and the draft rejects receiver-side frame-length detection (RFC 1812 mandates discarding truncated packets) and single-DSCP+CE (would destroy ECN's early signaling). A Linux prototype shows large flow-completion-time gains for tail losses in short flows, with no measurable change where later packets already reveal the loss.
- **How**: Switch trims payload above a buffer threshold and forwards the header; receiver issues a deterministic NACK for exactly the missing range — faster, more predictable recovery than inference.
- **Where applicable**: Controlled domains (data centers) with trimming-capable switches and endpoints that support the option; the natural TCP-side companion to the trimming already deployed in RoCE fabrics.

### The Session Identifier Option (SIO)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-cmcc-tcp-sro/) · [Session recording](https://youtu.be/XRBR6ORihRs) · [Materials](https://datatracker.ietf.org/meeting/127/session/tcpm)

Zhaoyu Luo (editor), Haishuang Yan (China Mobile / CMCC).

- **Why**: Load balancers, NAT gateways and firewalls hold per-connection state the endpoints can't help them with; QUIC-LB standardized identifier-based forwarding for QUIC, but TCP and UDP had nothing — this fills the gap.
- **What**: Two self-describing transport options — LOCAL-ID (sender's identifier) and PEER-ID (the peer's) — as TCP options (negotiated in the handshake, then carried on designated segments) and UDP options (every datagram, since any datagram may follow a session loss). Uses: session recovery in LB/NAT clusters (with a companion ASRP protocol), stateless forwarding (an LB reads the backend ID from every segment and forwards with no session table), conntrack recovery after state loss, per-backend telemetry, opaque affinity, elastic VNFs. Two implementations were interoperability-tested on a three-node testbed: an eBPF/TC implementation on the endpoints and a Linux IPVS kernel-module extension on the load balancer, exercising recovery after session-table loss.
- **How**: Identifiers are opaque 0–8 octet strings with deployment-defined generation; TCP carrying modes trade overhead against function — retransmission mode (IDs only on retransmits, zero normal overhead) or per-segment mode (enables stateless forwarding).
- **Where applicable**: Designed for a single LB/NAT tier between client and server (in multi-tier deployments only the closest tier benefits); identifiers must survive reboots for recovery to work, and address-derived IDs leak internal addressing. Relevant to anyone running large LB fleets or conntrack at scale.

### EVPN Subnet Slicing

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-subnet-slicing/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-bess-draft-sajassi-bess-evpn-subnet-slicing-00) · [Session recording](https://youtu.be/nryz9SzoysI) · [Materials](https://datatracker.ietf.org/meeting/127/session/bess)

A. Sajassi, N. Malhotra, R. Kachalia (Cisco); C. Zeledon (Meta).

- **Why**: In enterprise campuses with stretched subnets, every access switch acting as EVPN-IRB PE must hold host routes for the whole subnet; Optimized-IRB fixed MAC-VRF scale but IP-VRF still exhausts small access-switch FIBs.
- **What**: Slice each subnet into pieces anchored at tier-2 anchor PE pairs; access leaves keep only locally connected hosts. The worked example (400K hosts, 8 GWs, 100 leafs) drops access-leaf L3 FIB from 400K to 4K and distribution FIB to 50K. Per-subnet choice: a network can mix traditional IRB, Optimized IRB and Subnet Slicing.
- **How**: BGP RT-2 host routes carry a per-[Slice, VRF] Route Target; only anchor PEs import their slice's RT; leaves install slice prefixes via the anchors. North-south paths stay optimal; east-west traffic transits the anchor pair (the explicit trade-off).
- **Where applicable**: Enterprise-campus EVPN with small-FIB access switches and predominantly north-south traffic; Cisco + Meta authorship signals hyperscale-campus interest. Not for east-west-heavy subnets.

### Origin-Leaf Identification in Data-Center eBGP Underlays using BGP Large Communities

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-brissette-idr-dc-origin-leaf-id/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessb-2-7-origin-leaf-identification-in-data-center-ebgp-underlays-00) · [Session recording](https://youtu.be/S3NPP_SmEV8) · [Materials](https://datatracker.ietf.org/meeting/127/session/idr)

Patrice Brissette, Krishnaswamy Ananthamurthy, Ketan Talaulikar (Cisco).

- **Why**: In hop-by-hop eBGP fabrics where leaves share an ASN, the AS_PATH can't tell you which leaf originated a prefix — blocking leaf-specific troubleshooting, maintenance drains and pod-aware policy.
- **What**: An analysis-and-recommendation document (Informational, no new protocol elements): encode the origin leaf in a BGP Large Community (RFC 8092) — either a dedicated-ASN fabric-wide encoding (pod, leaf, port packed into the two 32-bit Local Data fields) or function-based packing under a shared ASN. A comparison table walks the candidates (unique ASN, standard community, large community, SoO, generic ext-community) on value space, structure, survival across eBGP hops and best-path impact. Use cases: forwarding-by-origin policy, QoS/ACL steering, pod-aware ECMP, maintenance LOCAL_PREF handling.
- **How**: Leaves attach the community at origination; it propagates unchanged; receivers match per field.
- **Where applicable**: Any eBGP DC fabric; requires fabric-wide fixed-width encoding discipline and auditing that additive policies don't strip communities. The draft honestly flags the ADD-PATH limitation: a spine advertises one path per prefix, so origin tags can't reveal paths the spine didn't advertise — full visibility needs ADD-PATH with a distinct-origin selection policy, and enabling ADD-PATH alone is insufficient.

### BGP RR Deployment Considerations

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-smith-idr-rr-deployment-considerations/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-idr-sessa-1-4-bgp-rr-deployment-considerations-00) · [Session recording](https://youtu.be/SNsb8blw0BY) · [Materials](https://datatracker.ietf.org/meeting/127/session/idr)

David J. Smith, Serge Krier (Cisco); Spencer Gaw (CoreWeave); Israel Means (AT&T); Krzysztof G. Szarkowicz (HPE).

- **Why**: Route reflectors are the control-plane keystone of most BGP networks, and sub-optimal RR deployment is a classic stability and outage source; this collects the tribal knowledge into one vendor-agnostic document.
- **What**: A checklist-style survey of RR design and operations: cluster design (redundancy, CLUSTER_ID, sizing), multi-cluster designs (full mesh, multi-tier, multi-plane), address-family and control-plane segmentation, policy/update-group interactions, slow-peer handling, path-selection interactions (RDs, Add-Paths, ORR, PNH resolution), transport optimizations (TCP PMTU vs Ethernet MTU), plus NSR/GR/multi-hop BFD and security (authentication, prefix limits, control-plane protection). Requesting WG adoption, arguing it belongs in IDR (whose charter covers RR operation) rather than GROW.
- **How**: Informational best-practice document built from vendor and operator experience — including an AI-cloud operator (CoreWeave) among the authors.
- **Where applicable**: Broadly applicable to any BGP network using RRs; nothing novel, but as a design review checklist for RR-based fabrics it is cheap insurance against well-known failure modes.

### Hierarchical Cryptographically Generated Addresses (HCGA)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-buraglio-6man-hcga/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-hierarchical-cryptographically-generated-addresses-02) · [Session recording](https://youtu.be/nExK52_b_RE) · [Materials](https://datatracker.ietf.org/meeting/127/session/6man)

Nick Buraglio (ESnet); Josh Bailey (Overly Specific Dynamics).

- **Why**: In multi-tenant Kubernetes and AI-agent fleets, thousands of workloads hide behind infrastructure-assigned /64s with no per-instance cryptographic binding — network accountability currently requires external lookup tables.
- **What**: Extends RFC 3972 CGA so that the subnet bits between the operator's aggregate prefix and the /64 boundary are also derived from the public key (SHA-256 over aggregate || prefix modifier || key), making the entire /64 — not just the IID — a deterministic function of a key, typically hardware-bound (TPM 2.0, vTPM, SPIFFE SVID, software tiers with decreasing assurance). Per-pod/agent /64s enable per-agent policy without sidecars and forensic attribution of any packet to a hardware key; RPKI ROAs on the aggregate cover all contained HCGA /64s by containment.
- **How**: The workload derives its own /64 (no CNI assignment); Calico or Cilium in BGP mode installs it as a host route unchanged; verification is a 3-step check. IID rotation within the /64 preserves /64-level accountability while hindering traffic correlation.
- **Where applicable**: Explicitly one component of a larger accountability architecture — key attestation, parameter distribution and source-address enforcement (uRPF) are needed but not specified. A deliberate deviation from CNI-assigned prefixes; the deck's open questions (right venue? adoption interest?) mean this is early-stage but conceptually interesting for per-workload identity in Kubernetes.

### The IPv6 Loopback Address Prefix

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-6man-loopback/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-6man-the-ipv6-loopback-prefix-00) · [Session recording](https://youtu.be/nExK52_b_RE) · [Materials](https://datatracker.ietf.org/meeting/127/session/6man)

Warren Kumari & Geoff Huston (6man WG document, draft-ietf-6man-loopback).

- **Why**: ::1/128 is a single address; containers, service meshes and host-internal virtual networks need routable, sliceable host-local space — today achieved with ad-hoc private addressing.
- **What**: Expands the loopback space to a TBD/48 "Node-Local Unicast" prefix (updating RFCs 4291 and 4007 and the IANA registries), sliced into standard /64s assignable to host-internal virtual interfaces for inter-process communication, local virtualization, container networking and diagnostics. The WG discussion at this meeting resolved real issues: adopting "Node-Local Unicast" terminology (multiple local virtual interfaces, not a single loopback), choosing /48 over /96 so normal /64 boundaries work, and reworking the zone-id rule per Brian Carpenter (programmers must supply sin6_scope_id, so require a null/ignored value rather than a MUST NOT). Requesting WGLC.
- **How**: Pure address-architecture change — hosts route internally among local virtual interfaces without touching physical links.
- **Where applicable**: Any host running containers, local virtualization or service meshes (explicitly cited as motivating cases); broadly applicable and close to done.

### Routing mechanism in Dragonfly Networks Gap Analysis, Problem Statement, and Requirements

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-wang-rtgwg-dragonfly-routing-problem/) · [Session recording](https://youtu.be/CKWa3STuXj8) · [Materials](https://datatracker.ietf.org/meeting/127/session/rtgwg)

Ruixue Wang, Rui Zhuang, Wenxuan Wang, Weiqiang Cheng (China Mobile); Changwang Lin (New H3C Technologies).

- **Why**: Dragonfly-family topologies are the cost-efficient alternative to fat trees for very large HPC/AI clusters, and their routing — minimal vs non-minimal/adaptive — is exactly where multi-vendor deployments break today.
- **What**: The draft walks Dragonfly, Dragonfly+ (spine-leaf within groups, with the "down-up" detour problem: non-minimal routes sink to an intermediate group's leaves, wasting intra-group bandwidth, adding hops and deadlock risk) and a proposed Dragonfly-Ultra variant where same-index spines across groups are fully connected, keeping non-minimal routes at the spine layer and eliminating the detour topologically. The gap analysis is the actionable part: minimal routing risks load imbalance; adaptive routing exists, but congestion metrics, threshold definitions and notification formats are proprietary, so adaptive routing cannot work end-to-end in multi-vendor deployments. Requirements: low latency, load balancing, scalability, adaptability, reliability.
- **How**: Informational gap/problem/requirements document — no protocol yet; it sets up future standardization of congestion-information exchange.
- **Where applicable**: Dragonfly/Dragonfly+ fabrics for HPC and AI clusters; the multi-vendor adaptive-routing notification gap is the finding that generalizes. China Mobile/New H3C-driven.

### Current State of the Art for High Performance Wide Area Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-kcrh-hpwan-state-of-art/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-tsvwg-hpwan-state-of-art-heads-up-before-ad-sponsored-publication-00) · [Session recording](https://youtu.be/QFShsZT5rkk) · [Materials](https://datatracker.ietf.org/meeting/127/session/tsvwg)

Daniel King (Lancaster University), Tim Chown (Jisc); with Chris Rapier (PSC), Daniel Huang (ZTE), Kehan Yao (China Mobile).

- **Why**: The HP-WAN is the WAN counterpart of AI-fabric work — long-fat-pipe networks for distributed training, HPC and science data — and this survey is about to be finalized as the state-of-the-art record, with the authors actively soliciting operator input before publication.
- **What**: A survey of R&E HP-WANs (GÉANT, Internet2, Janet, ESnet, CANARIE, WLCG for CERN) and large commercial dedicated networks: few very large flows over long RTTs with planned and reserved (not contended) capacity; IPv6 carries 98%+ of WLCG transfers and PMTUD must be robust across mixed 1500/9000 MTU sites; BBRv3 would help but is not yet in standard Linux distributions; substantial unstandardized tooling in production (SENSE, AutoGOLE, NOTED, perftest RDMA); recent 800G RDMA test results to be added. The next revision tightens scope to R&E and restructures around capacity management and transport.
- **How**: Informational survey via AD sponsorship, following the HP-WAN BoF series.
- **Where applicable**: R&E-focused by scope, but the operational lessons (PMTUD across mixed MTUs, rate-based CC for giant flows, whether dynamic provisioning is actually used in production, scheduler-to-network-reservation mapping) transfer directly to any DCI carrying AI training and dataset movement.

## Adjacent

### BBR Congestion Control

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-ccwg-analysis-for-the-differences-between-standard-congestion-control-schemes-draft-nishida-ccwg-standard-cc-analysis-01) · [Session recording](https://youtu.be/pXwvZqkML7I) · [Materials](https://datatracker.ietf.org/meeting/127/session/ccwg)

Ian Swett (presenting draft-ietf-ccwg-bbr, ccwg WG document).

- **Why**: BBRv3 is on track to be the IETF's first standardized model-based congestion control, and it is the algorithm the HP-WAN community says it is waiting for on long transfers.
- **What**: BBRv3 builds an explicit model of the path (delivery rate, RTT, loss) and uses it to control both pacing rate and the volume of data in flight — substantially higher throughput than Reno/CUBIC on shallow-buffer or lossy bottlenecks, and substantially lower queueing delay on deep buffers. Implementations exist for TCP and QUIC. Note: this write-up of BBRv3 is from the draft abstract; the slide deck under this agenda slot is actually a companion analysis (draft-nishida-ccwg-standard-cc-analysis) cataloguing undocumented differences among the CC standards — initial window (2–4 vs 10 segments), loss window, minimum RTO, slow-start growth rates, ssthresh basis (cwnd vs flight size, with overshooting risk on the cwnd variant), and divergent ECN-CE responses across RFC 5681/9002/9438 — a useful reference if you run mixed TCP and QUIC fleets.
- **How**: Model-based sending-rate and in-flight bounds rather than loss-triggered AIMD.
- **Where applicable**: Any TCP/QUIC sender over WAN paths; in the DC it coexists with, rather than replaces, DCQCN/ECN RoCE stacks. Directly connected to the HP-WAN survey above, which notes BBRv3's absence from distro kernels as a current blocker.

### EVPN multi-homing support for L3 services

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-l3mh-proto/) · [Session recording](https://youtu.be/nryz9SzoysI) · [Materials](https://datatracker.ietf.org/meeting/127/session/bess)

Patrice Brissette and Michael MacKenzie, editors (Cisco); Satoru Matsushima (Softbank); Wen Lin (Juniper); Jorge Rabadan (Nokia) — bess WG document.

- **Why**: All-active L3 multihoming to a CE previously required proprietary MC-LAG/ICCP inter-chassis plumbing; this replaces it with the EVPN control plane you already run.
- **What**: Uses EVPN ES-LAG for L3 service redundancy, synchronizing ARP/ND (RT-2), IGMP/MLD state (RT-7/8) and IGP-learned CE routes (RT-5, via ESI-based or IP-gateway-based approaches) between redundant PEs. It solves the classic hashed-ARP problem (LAG hashing means only one PE ever sees ARP replies, so the other drops traffic), the dual-PIM-DR multicast problem, and IGP-adjacency-forms-on-one-PE. ESI identifies the L3 LAG; Ethernet Tag-ID carries the VLAN/sub-interface; label-1 = MPLS explicit NULL marks an RT-2 as an L3 neighbor-sync with no L2 bridging state. An optional retention timer keeps synchronized entries through peer failure for convergence. BGP PE-CE is explicitly future study.
- **How**: Existing EVPN route types only, no new ones; underlay-agnostic (MPLS, VXLAN, SRv6 L3VPN).
- **Where applicable**: L3VPN/L3 service access with dual-homed CEs — broadly applicable, WG-owned, and a clean replacement path for legacy MC-LAG.

### YANG Datastore Telemetry (YANG Push version 2)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-netconf-yang-push-2/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-netconf-5-yang-push-v2-00) · [Session recording](https://youtu.be/yFo-QPAxq_E) · [Materials](https://datatracker.ietf.org/meeting/127/session/netconf)

Rob Wilton (presenting), with contributors from Swisscom, Deutsche Telekom, EverythingOps/Arrcus, Nokia and Juniper — netconf WG document.

- **Why**: YANG Push v2 is the standards-track counterpart to gNMI for vendor-neutral streaming telemetry — the observability substrate underneath most other work in this program.
- **What**: Revision -01 simplified the update message to update/delete per target (no merge/replace choice), defined the YANG Push v2 notification envelope, clarified snapshot completion and timestamp semantics (event-time = when telemetry processing begins; observation-time = when source data was sampled), defined sequence numbering per device/subscription/publisher, tightened distributed-publisher behavior (membership changes only between collections, publisher ID 0 reserved, removed IDs never reused), and specified encodings for JSON, XML and CBOR (text IDs and SIDs).
- **How**: A lighter alternative to Subscribed Notifications + YANG Push, deliberately aligned toward gNMI behaviors — which are themselves underspecified, so this draft is effectively standardizing gNMI's target-defined semantics.
- **Where applicable**: Any network telemetry pipeline; the authors aim for the core protocol to be stable enough to implement around IETF 128, with 29 open issues (some significant) remaining.

### RIFT extensions for SRv6

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-cheng-rift-srv6-extensions/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-rift-02-rift-extensions-for-srv6-00) · [Session recording](https://youtu.be/M4AMTDaBBA4) · [Materials](https://datatracker.ietf.org/meeting/127/session/rift)

Rui Zhuang (presenter) and Weiqiang Cheng (China Mobile); Changwang Lin (New H3C Technologies); Ruixue Wang (China Mobile).

- **Why**: RIFT is the zero-touch spine-leaf routing protocol; this wires SRv6 into it so a RIFT fabric can do SR traffic steering — the same direction as the OpenAI backend, but controller-driven rather than endpoint-driven.
- **What**: Distributes SRv6 Locators, End SIDs and End.X (adjacency) SIDs via a new SRv6 Locator KV-TIE (controller-driven zero-touch provisioning) or a Locator TIE (manually configured, northbound-flooded with disaggregation rules), with End.X carried in Node TIEs. References RFC 9800 for compressed SRv6 encoding to keep DC overhead minimal. New use cases tie into the SRv6 AI-backend and hyperscale frontend/WAN drafts — e.g., a controller issues an explicit Leaf21→Spine21→TOF2→Spine12→Leaf11 path to steer around a congested node or link.
- **How**: Reuses RIFT's ZTP flooding: the controller pushes Locator/End SID/End.X configuration to the TOF, which distributes it to all routers; neighbor discovery flows back up, and the controller assigns adjacency SIDs per neighbor.
- **Where applicable**: RIFT-based fabrics (spine-leaf with zero-touch provisioning); China Mobile/New H3C ecosystem. Conceptually complementary to — and opposite from — the static, endpoint-source-routed OpenAI approach.

### Elastic Bandwidth-aware Routing Framework

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-rzz-rtgwg-inter-domain-ebr/) · [Slides](https://datatracker.ietf.org/meeting/127/materials/slides-127-rtgwg-07-bgp-based-inter-domain-elastic-bandwidth-aware-routing-framework-00) · [Session recording](https://youtu.be/CKWa3STuXj8) · [Materials](https://datatracker.ietf.org/meeting/127/session/rtgwg)

Weiqiang Cheng (China Mobile); K. Zhang, L. Zhang, J. Dong (Huawei); L. M. Contreras (Telefónica).

- **Why**: One of the few routing drafts at this meeting with production results attached — a distributed fast-congestion-relief layer that acts before centralized TE finishes its global optimization.
- **What**: EBR floods link bandwidth via existing IGP TE metric extensions (10 s statistics interval, minimum 10 s advertisement interval, 10% change threshold); nodes pre-compute disjoint SR strict-path alternates; when a link crosses the congestion threshold (80%), traffic is distributed across primary plus alternates with UCMP weights proportional to available bandwidth, reverting below a 60% post-restore threshold after a 300 s soak to prevent flapping. Deployed in China Mobile metro/BRAS (2 core devices + 28 BRAS, IS-IS + SRv6): six congestion events between December 2025 and May 2026, each resolved by a single adjustment (e.g., 100%→28%, 97%→38%, 84%→27%) with no oscillation or repeated iteration.
- **How**: Pre-computed alternates make the reaction local and immediate; weights are fixed at trigger time until new congestion appears, avoiding iterative churn; non-EBR routers can still serve as transit on the alternates.
- **Where applicable**: Production-proven, but in a China Mobile metro/BRAS context (few large aggregation links) — the pattern (IGP bandwidth advertisement + SR alternates + hysteresis thresholds) transfers to WAN and DCI edges, not to DC fabrics.

## Wildcard

### Testing of Christian's Congestion Control Code (C4)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-huitema-ccwg-c4-test/) · [Session recording](https://youtu.be/pXwvZqkML7I) · [Materials](https://datatracker.ietf.org/meeting/127/session/ccwg)

Christian Huitema (Private Octopus); Suhas Nandakumar, Cullen Jennings (Cisco).

- **Why**: Not a DC/AI topic, but one of the most complete public evaluation methodologies for a new congestion control — and the direction CC is heading for interactive media over QUIC.
- **What**: The test document for C4, a low-delay congestion control for Media over QUIC with deliberate support for application-limited senders (variable-rate encoding) and fast reaction to avoid the priority inversion that happens when CC overestimates available capacity. The methodology: every scenario run 100 times in the picoquic simulator (virtual-time, same code as production), with C4 vs BBR vs CUBIC as the main connection, measuring average and 90th-percentile completion time, RTT with standard deviation, load factor (bandwidth share under competition, judged against RFC 9743's acceptable 30–70% band) and media frame latency. Scenario families span capacity steps, black holes, GEO satellite paths with careful-resume, bufferbloat competition, a Poisson-modeled "bad Wi-Fi" jitter with 100–200 ms spikes, L4S/ECN under dualQ AQM, and a full MoQ media suite (audio plus two video encodings, QUIC priorities, simulcast-style STOP-SENDING, congested feedback path), plus live loopback tests and Webex prototype deployments in control networks.
- **How**: Repeatable virtual-time simulation benchmarked honestly against BBR and CUBIC, plus initial real deployments — a model for how CC should be evaluated.
- **Where applicable**: Real-time media over QUIC paths; but the harness itself (repeatable CC benchmarking with fairness bands) is reusable for anyone evaluating DC or WAN congestion control — that is the wildcard value.

### Cross-Publisher Causal Ordering for YANG-Push Datastore Telemetry

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-dikshit-netconf-yang-push-causal-ordering/) · [Session recording](https://youtu.be/yFo-QPAxq_E) · [Materials](https://datatracker.ietf.org/meeting/127/session/netconf)

Saumya Dikshit (Hewlett Packard Enterprise).

- **Why**: A genuinely novel bit of distributed-systems engineering surfacing inside network management: how to order telemetry updates when the "device" is actually many publishers — a multi-line-card router or a disaggregated routing stack serving one subscription.
- **What**: Revision -02 replaces an earlier Hybrid Logical Clock proposal with an opt-in, coordination-free design: the notification envelope carries a Comparability Scope (which publishers get compared), a coarse Causal-Epoch (advances only when causal state hand-off crosses a publisher boundary — e.g., a RIB install triggering a BGP update), and a per-publisher Local-Sequence-Number. Publishers stay lock-free on the export fast path; the collector reconstructs order within a bounded reordering window (a watermark timer; late arrivals are flagged, not held). No clock synchronization required. The appendix honestly compares vector clocks (exact causality, O(n) state), hybrid logical clocks (fixed size, needs loose sync) and this scheme (constant per-epoch state, partial ordering within a scope).
- **How**: A YANG module augments subscriptions (disabled by default, zero overhead for single-publisher cases) and the YANG Push v2 envelope, with RFC 9196 capability discovery; two-tier ordering at the collector — Causal-Epoch across publishers, Local-Seq for per-publisher loss/duplicate detection.
- **Where applicable**: Disaggregated and multi-line-card network elements — increasingly the norm — and a clean reference pattern for causal ordering in any multi-producer telemetry or state-streaming pipeline.

## Themes

- **AI/HPC networking has fully arrived at the IETF.** rtgwg, scone, 6man, opsawg and tsvwg all carried AI-fabric work this cycle (flow-label relabeling, enhanced ECMP, adaptive routing, rate advice, IPFIX for RDMA, HP-WAN, scheduler intent). Problems that previously lived in OCP/IBTA/vendor land are being pulled into standards bodies.
- **The program contains a live architectural argument about where intelligence sits.** OpenAI's statically-routed, dumb-switch fabric with MRC smart-NIC packet spraying is one pole; network-side adaptive routing (the rtgwg framework, SCONE rate advice, RIFT-SRv6 controller steering) is the other. Notably, the endpoint plane keeps appearing on both sides — even the network-centric drafts now push decisions into the NIC.
- **The network is learning to read RDMA.** QP parsing at the DCI edge (flow label), in the monitoring plane (IPFIX BTH IEs), and in the control loop (per-QP rate advice) — RoCEv2 semantics are being lifted into IP-layer infrastructure.
- **Job-aware networking is taking shape as a standard hierarchy** — scheduler job metadata → service intent → tunnel realization — the beginning of admission-controlled networks for AI/HPC, cross-DC training and data movement.
- **BGP/EVPN operational maturity for large fabrics**: origin-leaf tagging, RR deployment best practices, subnet slicing and L3 ES-LAG multihoming — the eBGP/EVPN stack keeps acquiring the operational polish needed for AI-era scale.
- **Host-internal IPv6 is becoming infrastructure**: the Node-Local Unicast /48 and per-workload cryptographic prefixes (HCGA) both adapt the IPv6 address architecture to containers, service meshes and agent fleets — a quiet but consequential shift in what an "address" is.
