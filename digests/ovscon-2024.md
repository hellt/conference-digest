<!--
conference: Open vSwitch and OVN 2024 Fall Conference (Prague)
type: vendor
source_url: https://www.openvswitch.org/support/ovscon2024/
generated: 2026-11-01
registry_key: ovscon-2024
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Open vSwitch and OVN 2024 Fall Conference (Prague)

A single-track, contributor-heavy community conference. The center of gravity this cycle: renegotiating where hardware acceleration lives in the OVS architecture, pushing OVN out of its overlay bubble into the routed fabric, and turning observability into a datapath-native feature. Nearly everything is technical; the few vendor pitches are flagged below.

## Core

### Integrating OVN into the Network Fabric

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t4) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/2024_ovn-con_fabric-integration.pdf) · [Recording](https://www.youtube.com/watch?v=dCKNrAdISWY)

Speakers: Felix Huettner, STACKIT GmbH & Co. KG, and Frode Nordahl, Canonical

**Why**: The hard boundary between OVN overlays and the physical fabric — stretched L2, MAC-flapping failover, external BGP agents — is a problem anyone running OVN at DC scale hits. This is the most direct fabric/interconnect talk in the program.

**What**: A rearchitecture of OVN's external connectivity to replace stretched L2 with dynamic routing. A new "magic router" logical construct translates overlay L2 networks into per-chassis point-to-point networks; it is not pinned to any chassis, so egress uses ECMP across gateway chassis and ingress can enter via any of its LRPs. Failover happens by moving dynamic routes instead of MACs, so failover speed is no longer limited by routing convergence, and BFD lets the fabric pick alternate paths.

**How**: Work in flight includes exporting routes from OVN logical routers to Linux route tables, importing routes back in, auto-generating LRPs/LSPs per chassis (so the CMS needs no changes), and optimizing ingress/egress based on LRP locality. Route advertisement and learning via BGP, with distinct route preferences per gateway chassis and an active-active version of distributed gateway ports. A patchset ("OVN Fabric integration") is on patchwork.

**Where applicable**: OVN-based clouds generally — the speakers come from STACKIT (OpenStack) and Canonical, and the design supersedes the ovn-bgp-agent pattern. The stretched-L2 drawbacks it enumerates (bonding/MLAG requirements, MAC moves on failover) are universal; the fix requires upstream OVN patches that were not yet merged at talk time.

### Running Open vSwitch on a large CPU System

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t1) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/Running%20OVS%20on%20a%20large%20CPU%20system.pdf) · [Recording](https://www.youtube.com/watch?v=jX5dVJVSUoc)

Speakers: Eelco Chaudron, Red Hat, Inc.

**Why**: Modern DC hosts are 128–256 CPUs, and this is a rare measured study of what actually breaks in ovs-vswitchd and the kernel datapath at that scale — including an OOM-killer incident reproduced during testing. Directly relevant to anyone running OVS on current-generation EPYC-class compute.

**What**: On a 128-CPU EPYC 7702P (OVS 3.3, RHEL 9.5), the revalidator process stops scaling past a handful of threads: with 200k datapath flows, mean flow-dump duration goes 169.7 ms → 180.7 ms → 183.4 ms for 4/32/128 revalidator threads, due to lock contention in `nl_dump_next()` (the mutex serializes netlink dump recvs to avoid an in-kernel EINVAL race on pooled sockets). With traffic landing on many CPUs, per-CPU `sw_flow_stat` structures (32 bytes each, allocated on demand) consume 782 MB for 200k flows at 128 CPUs and 1.5 GB at 256 CPUs — the real problem is not the memory but the latency of accumulating non-linearly-stored stats, which grows dump duration until a ~1.3 s threshold forces the flow limit down. Interface-statistics sweeps (~every 5 s) take 63 ms at 64 CPUs vs 104 ms at 128, with kernel exception counters adding ~451 ns per interface at 128 CPUs.

**How**: USDT probes and bpftrace-based scripts (`reval_monitor.py`, `kernel_delay.py`), veth/netns test topologies, Scapy traffic pinned with taskset, and 1024-veth-pair configurations to isolate the statistics path. A simulated pod-churn test (128 OVN ports, continuous add/delete) shows ~50% more `recvmsg()` time at 128 cores, traced toward `netdev_get_addrs()`/`getifaddrs()` but left for further investigation.

**Where applicable**: Kernel datapath (the `sw_flow_stat` issues are OVS kmod-specific) on large-CPU hosts — K8s nodes, NFV compute. Follow-ups listed: remove the `nl_dump_next()` mutex, optimize kmod stats gathering, possibly patch glibc's `getifaddrs()` (which wastes ~6% gathering unneeded per-CPU IPv6 stats).

### Pluggable DPIF - Unlocking accelerated OVS full potential

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t7) · [Slides (PPTX)](https://www.openvswitch.org/support/ovscon2024/slides/pluggable-dpif-1.pptx) · [Slides (PPTX)](https://www.openvswitch.org/support/ovscon2024/slides/pluggable-dpif-2.pptx) · [Recording](https://www.youtube.com/watch?v=LukzSDekjx4)

Speakers: Roi Dayan, Roni Bar Yanai, Eli Britstein, NVIDIA

**Why**: This is the architectural argument for where OVS hardware acceleration is heading — a runtime-pluggable datapath interface — and it comes with the most honest enumeration of why today's "acceleration below the datapath" model is broken.

**What**: A proposal to make DPIF a loadable, vendor-implemented API (shared object loaded at runtime), so each vendor ships a datapath that co-designs fast path, slow path, and offload — instead of squeezing hardware through TC flower or rte_flow, both of which are too low-level and constrained (no `dp_hash`, no CT offload in DPDK, vendor match/action mismatches).

**How**: The slides walk through concrete failure modes of the current model: a `ct()` action placed mid-pipeline after packet modifications means a HW miss lands in SW with broken context; `dp_hash` uses Jenkins in SW while HW hashes differ, causing consistency failures and TCP disconnects; meter state split between HW and SW; megaflow aging relying on per-HW-type counters; EMC/SMC cache context invisible to the offload layer. In the proposed model, packets can be bounced back to hardware (with next recirc-id and metadata) to complete the pipeline, and vendors handle their own DPIF maintenance — formalizing what customers already do by forking dpif-netdev.

**Where applicable**: OVS community architecture decision with ecosystem-wide implications. The reference implementation is NVIDIA's DOCA DPIF, but the proposal is explicitly multi-vendor (P4 vs DOCA Flow cited as different integration styles). Watch this if you have any SmartNIC/DPU strategy.

### OpenShift Networking Transformed: Fully Embracing DPDK Datapaths in OVN-K8s!

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t8) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/OpenShift%20Networking%20Transformed.pdf) · [Recording](https://www.youtube.com/watch?v=KwznQq8f7LM)

Speakers: Jakob Meng, Maxime Coquelin, Red Hat, Inc.

**Why**: A complete userspace datapath from NIC to pod in OVN-Kubernetes — kernel bypass inside a managed Kubernetes distribution, with refreshingly honest benchmark results including where it loses.

**What**: Replaced veth-based pod connectivity with VDUSE (a purely software vDPA device: a kernel driver on the vDPA bus plus a userspace device implemented via the DPDK Vhost library). OVS reuses its `dpdkvhostuserclient` port type, so the datapath is the well-optimized Vhost-user one; OVN-K8s creates VDUSE devices instead of veth pairs when userspace bridges are detected. Motivations: partitioning (network infra isolated on dedicated CPUs), determinism, and uniformity across primary/secondary networks including KubeVirt.

**How**: Measured on Intel Xeon Gold 6438N, RHEL 9.6, isolated CPUs, 1 GB hugepages, OVS 3.4+: veth performs slightly better on small block sizes, VDUSE outperforms veth on medium sizes, and VDUSE plateaus on large blocks where ~40% of cycles on the Rx virtqueue IRQ CPU are spent in the bounce-buffer copy (100% busy). Stated cons: memory bandwidth cost from bounce buffers, operational complexity (kernel args, hugepages, NUMA tuning), higher CPU from PMDs (partially mitigated by PMD load-based sleeping at the cost of wakeup latency), and SELinux currently unsupported.

**Where applicable**: OpenShift/RHEL PoC today (activated by kernel args, `prepare-ovs.sh`, vfio-pci binding); the VDUSE technique itself is general for K8s clusters wanting partitioned, deterministic pod networking. Preliminary results, explicitly framed as a PoC with upstream productization as future work.

### (P)sampling kubernetes network policies

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t19) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/OVS_OVN%20Conf%2024_%20_%28P%29sampling%20kubernetes%20network%20policies_%20.pdf) · [Recording](https://www.youtube.com/watch?v=gLwDsaiUuN4&t=2s)

Speakers: Dumitru Ceara, Nadia Pinaeva, Adrian Moreno, Red Hat, Inc.

**Why**: "Why was this connection allowed or denied" is the top operational pain point in clusters with thousands of NetworkPolicies — and this talk shows the full cross-stack feature chain (kernel → OVS → OVN → ovn-kubernetes) that solves it at line rate.

**What**: Live NetworkPolicy visibility via OVN ACL sampling (OVN 24.09: new `Sampling_App`, `Sample_Collector`, `Sample` NB tables; per-ACL `sample_new`/`sample_est`). It replaces the OVN drop-debugging design's IPFIX export, which forced every sample through the kernel → ovs-vswitchd path, sharing a netlink socket with upcalls (packet loss) and causing IPFIX-cache contention.

**How**: The kernel's psample netlink multicast group now ships samples directly to listeners, bypassing ovs-vswitchd entirely; OVS gained a psample datapath action (integrated with `sample()` and `trunc()`, cookie support added) plus an OVS 3.4 optimization where the sample action's `obs_point` can be loaded from packet fields (`NXM_NX_CT_LABEL`). OVN encodes the observation point into `ct_label` at connection commit, collapsing the reply-direction sampling from O(number-of-ACLs) flows to exactly two flows regardless of ACL count.

**Where applicable**: OVN-Kubernetes/OpenShift deployments of any size. Note the psample action is implemented in the kernel datapath (ACL sampling itself works with either IPFIX or psample collectors). The pattern — OVN-generated metadata riding packet samples — is extensible to other observability applications.

### Low on Stack: Flexible protocols vs. Limited Memory

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t2) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/Low%20on%20Stack_%20Flexible%20protocols%20vs%20limited%20memory.pdf) · [Recording](https://www.youtube.com/watch?v=MpXC7CuTKMQ)

Speakers: Ilya Maximets, Red Hat, Inc.

**Why**: Deep OVS internals on a real correctness hazard — stack exhaustion from recursive parsing/execution of flexible protocols (Netlink actions, OpenFlow translation) — and it decodes the warnings operators actually see in the field (resubmit limits, deferred action limits).

**What**: How OVS bounds recursion on both sides of the datapath. Kernel: ~16 kB stack, so nested Netlink actions (e.g., `clone(clone(...))`, up to 64 kB of nesting in a 16-bit length field) are executed via a Deferred Actions FIFO instead of unbounded recursion. Userspace: 2–8 MB stacks, but OpenFlow translation recurses through `goto_table`/`resubmit`/`ct(table=N)`/patch-port output; the existing depth/resubmit limits work out to roughly 512 B–2 kB of stack budget per rule.

**How**: The genuinely new technique: track actual stack consumption at runtime using `__builtin_frame_address(0)` and `pthread_attr_getstacksize()`, and trigger recirculation when the frame address approaches the stack limit — an RFC patch ("ofproto-dpif-xlate: Recirculate on stack exhaustion") that turns a potential crash into a graceful recirculate-with-frozen-state.

**Where applicable**: All OVS deployments, kernel and userspace; most acute where controller-generated pipelines (OVN, or any SDN app composing deep resubmit chains) stress translation depth.

### Open vSwitch (OVS) performance case study - From software to hardware offloading, from kernel to userspace

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t6) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/ovscon24-CT-offloads.pptx) · [Recording](https://www.youtube.com/watch?v=_7YEmJrqJJE)

Speakers: Salem Sol, Gaetan Rivet, NVIDIA

**Why**: The most substantive engineering talk on connection-tracking offload — the feature OVS-DPDK lacks relative to the kernel datapath, and the reason many DPDK-shops still can't fully move off kernel OVS.

**What**: The implementation history of CT offloads in userspace OVS. A first attempt via rte_flow reused the flow-offload infrastructure but exposed real problems: thousands of offload updates against millions of connections, asynchronous TCP deletion creating a Last-ACK race (a segment acking a FIN could be fully hardware-processed if the offload isn't deleted immediately on FIN), and very short connections actually being *slowed* by offloading. The rework uses DOCA with a synchronous design: template-based API, pre-allocated pools of match/action/offload resources, static cooperative threads with minimal locking, a mempool of pre-allocated CT offloads with user-configured size, batched offloading, and a dedicated minimal CT table type.

**How**: Evaluated with CyPerf-generated HTTP traffic comparing OVS-DPDK vs OVS-DOCA: long-connection CPS (30K rate, 850 KB sessions — the favorable case) and short-connection CPS (40K/30K rates, 2 KB sessions — the worst case with ~3 offloaded packets per connection). Claimed outcomes: negligible overhead for short connections, significant improvement for long ones, better scaling/stability under concurrency. (The result charts are images; no specific figures are quotable from the extracted slides.)

**Where applicable**: NVIDIA hardware via the DOCA framework — vendor-specific. But the design lessons (offload has real per-connection cost; elephant/mice traffic distribution determines whether offloading pays; state synchronization between HW and SW is the hard part) generalize to any CT-offload strategy.

### P4OVN: Offloading OVN to Intel IPU for Intel Developer Cloud

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t23) · [Recording](https://www.youtube.com/watch?v=CgecMK9EhPU)

Speakers: Junho Suh, Intel, Inc. (from abstract only)

**Why**: A production DPU/IPU offload of OVN — not a demo — running in Intel Developer Cloud, and one of the few concrete data points on where SmartNIC-based virtual networking is actually deployed at service scale.

**What**: A hardware/software co-design: a hardware flow cache implemented in P4 on the IPU's programmable packet processing engine handles L2/L3 forwarding and connection tracking, while the IPU's compute tiles run OVS for stateful processing (ACL, NAT, LB). Covers deployment and operation for distributed virtual routers and distributed/centralized NAT gateways, plus OVN central, engineered to meet IDC scale requirements.

**How**: Partitioning by statefulness — stateless fast-path classification in programmable hardware, stateful exceptions on the IPU's ARM compute — with an explicit discussion of open-sourcing the work and encompassing other vendors' solutions.

**Where applicable**: Intel IPU-specific today; interesting as a template for the "programmable-P4 fast path + OVS slow path on DPU compute" pattern that parallels NVIDIA's DOCA DPIF and Marvell's approach.

### Composable Services in OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t22) · [Recording](https://www.youtube.com/watch?v=Gf4M-ZSmTz4)

Speakers: Mark Michelson, Red Hat, Inc. (from abstract only)

**Why**: Reveals where the core OVN team is taking the project's architecture — the session type this digest is told to up-rank.

**What**: A new proposal to extract certain functionality from existing OVN logical datapaths and implement it as standalone specialized datapaths ("composable services"), giving administrators more clarity and power over packet processing, with ACLs, NATs, and load balancers called out as beneficiaries, plus possible future offerings.

**How**: Not detailed in the available material — this is a proposal-stage design talk rather than a shipped feature.

**Where applicable**: OVN project-level direction; anyone building products on OVN should track how ACL/NAT/LB semantics change under this model.

## Adjacent

### OVS DOCA - The Evolution of hardware acceleration

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t18) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/OVS%20DOCA%20-%20The%20Evolution%20of%20hardware%20acceleration.pptx) · [Recording](https://www.youtube.com/watch?v=SpJClGod0uE)

Speakers: Majd Dibbiny, Maor Dickman, NVIDIA

**Why**: Half product pitch, but it contains the cleanest public comparison of OVS's three datapath modes and discloses NVIDIA's upstreaming intent.

**What**: A mode-by-mode accounting: kernel offload via TC flower (mature, generic, but slow control path, kernel-cycle-bound feature set, can't express `dp_hash`), OVS-DPDK via rte_flow (kernel bypass, but too low-level, no CT offload, requires cross-vendor consensus), and OVS-DOCA — a DOCA DPIF using DOCA-FLOW with hardware steering claiming 10x+ programming rate, supported with OVN 24.03 and OVN-K8s GA 1.0, based on OVS LTS 3.3.

**How**: Roadmap items disclosed: upstreaming the DOCA DPIF, live update (Nov 2024 LTS), security acceleration (IPSec and PSP), debuggability, and scale.

**Where applicable**: NVIDIA hardware; the upstream DOCA DPIF item is the one with community-wide consequences (see Pluggable DPIF).

### Current Challenges with OpenStack Ironic, SR-IOV, and OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t3) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/Current%20Challenges%20with%20OpenStack%20Ironic,%20SR-IOV,%20and%20OVN.odp) · [Recording](https://www.youtube.com/watch?v=irHtlLm9ACw)

Speakers: Michal Nasiadka, Bartosz Bezak, StackHPC (from abstract only)

**Why**: SR-IOV and bare-metal networking against OVN is an under-documented corner of the stack, told by an operator (StackHPC) rather than a vendor.

**What**: The ongoing problems implementing OpenStack Neutron ML2/OVN with Ironic/SR-IOV external ports: root causes, solutions under development and their upstream status (testing and reviews), plus temporary production workarounds.

**How / Where applicable**: No fuller source available; treat as an OpenStack-specific status report useful for anyone doing bare-metal + SR-IOV integration with OVN.

### Harnessing Marvell Accelerators with OVS Hardware Offload for Accelerated Network Performance

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t11) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/Harman-Jerin%20-%20Harnessing%20Marvell%20Accelerators%20with%20Open%20vSwitch%28OVS%29%20Hardware%20Offload%20for%20Accelerated%20Network%20Performance.pptx) · [Recording](https://www.youtube.com/watch?v=80biE5L7jqw)

Speakers: Harman Kalra, Jerin Jacob Kollanukkaran, Marvell

**Why**: Concrete DPU silicon detail (Octeon CN10K) from a vendor other than NVIDIA — useful for anyone comparing offload platforms.

**What**: An "ovs-offload-engine" alongside OVS that offloads OVS-classified flows into the CN10K's parser/CAM hardware: NIX (controller/DMA), NPC (parser forming MCAM keys, 16K entries), NPA (packet memory pointers), CPT (inline IPsec by intercepting strongSwan SA/SP policies via DPDK rte_security), conntrack-offload compensation, virtio integration up to 100 Gbps, and flow actions (RSS, VLAN strip/insert, mirroring, multicast).

**How**: Initial/exception packets processed by OVS, then installed into CAM so subsequent packets are matched in hardware; future work includes hierarchical scheduling/shaping up to five levels, LSO, and checksum generation.

**Where applicable**: Marvell Octeon CN10K-specific; the extracted slides are diagram-heavy and number-light, so treat the performance claims as vendor-stated.

### VM Migration Enhancements

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t16) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/OVN_VM_Migration_Enhancements.pptx) · [Recording](https://www.youtube.com/watch?v=aHHK5RUcRCw)

Speakers: Naveen Yerramneni, Nutanix (contributors: Naveen Yerramneni, Shibir Basak, Mansi Sharma, Nutanix)

**Why**: Live migration is where overlay networking semantics visibly break (proxy-ARP races, FDB staleness, conntrack loss) — and these are real upstream OVN features, not Nutanix-private patches.

**What**: New logical switch port options for migration: `pkt_clone_type=mc_unknown` (clone traffic to unknown ports while the destination binding is being established, fixing drops at migration start), `disable_arp_nd_rsp` (skip the ARP/ND responder so packets reach the port instead of being eaten by stale proxy ARP on the source), `force_fdb_lookup` (learn a port's additional MACs through OVN's native FDB, avoiding packet duplication when combined with cloning), and `disable_garp_rarp`. Plus FDB cleanup on port down, and controller CT-zone reservation (`external_ids:reserve_ct_zones`) so conntrack entries can be synchronized during migration — the latter two patches under review at talk time.

**How**: Each option targets a specific drop scenario demonstrated across a VXLAN-extended subnet spanning availability zones.

**Where applicable**: OVN generally (upstream options); the cross-AZ migration topology is Nutanix's use case, but the failure modes are universal to any live migration over OVN.

### ofproto/detrace - The missing link.

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t10) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/ofproto_detrace%20-%20The%20missing%20link..pdf) · [Recording](https://www.youtube.com/watch?v=OP3F1o3ozjM)

Speakers: Ales Musil, Dumitru Ceara, Red Hat, Inc.

**Why**: The debugging story across OVS/OVN's abstraction layers finally gets a one-command answer — new in OVS 3.4.

**What**: `ofproto/detrace` takes a datapath flow's UFID and outputs the OpenFlow rules and groups that contributed to its creation, bridging the gap between optimized kernel flows and the controller-configured pipeline that produced them.

**How**: The chain is: UFID → OpenFlow cookies → (with `ovn-detrace`) OVN Southbound Logical_Flows via stage-hints → Northbound objects (Port_Bindings, Load_Balancer VIP mappings, ACLs). The worked example walks a Geneve-encapsulated, DNAT'd connection from `dpctl/dump-flows` output all the way to the specific load balancer VIP.

**Where applicable**: Any OVS/OVN deployment on OVS ≥ 3.4; the mantra — "UFIDs → cookies → stage-hints → external-ids" — is worth remembering regardless of tooling.

### Tracing packets in OVS: an update on Retis

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t20) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/OVS_OVN%20Conf%2024_%20_Tracing%20packets%20in%20OVS_%20an%20update%20on%20Retis__%20.pdf) · [Recording](https://www.youtube.com/watch?v=K0ldVsWkLJw)

Speakers: Paolo Valerio, Adrian Moreno, Red Hat, Inc.

**Why**: eBPF-based packet tracing that follows packets across the kernel stack, the OVS datapath, *and* userspace upcalls — the visibility gap most tools leave.

**What**: Retis is a network tracing tool where OVS is a first-class citizen: eBPF programs on tracepoints/kprobes plus USDT probes in ovs-vswitchd (requires `--enable-usdt-probes`) to track a packet from upcall through action execution. New since last cycle: Python bindings (pyo3, on PyPI, with an embedded shell) and OVS flow enrichment — a kretprobe on `ovs_flow_tbl_lookup_stats` captures the UFID, then Retis queries ovs-vswitchd at runtime via `dpctl/get-flow` and `ofproto/detrace` (throttled and cached) to attach the full datapath and OpenFlow flows to trace events.

**How**: Event series show a single curl packet with its conntrack NAT actions annotated inline; limitations honestly stated (no reliable tracking of flow deletion/update, upcall flows not displayable).

**Where applicable**: Linux + OVS kernel datapath debugging; valuable for anyone who has tried to answer "what did OVS do to this packet" with tcpdump and failed.

### Introducing exact-match hardware offload for OVS

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t17) · [Recording](https://www.youtube.com/watch?v=bAIrGaNbBWk)

Speakers: Farhat Ullah, Farhan Tariq, Dreambig Semiconductor Inc. (from abstract only)

**Why**: Attacks the TCAM orthodoxy in DPU/SmartNIC flow lookup — power consumption and scalability — with an exact-match alternative blending micro/megaflow characteristics.

**What**: A critique that TCAM-based megaflow offload doesn't scale with ever-growing flow counts, and that TCAM alternatives complicate maintenance and hurt performance as megaflow table counts grow; the proposed solution brings exact-match hardware offload to OVS, demonstrated live.

**How / Where applicable**: Early-stage, demo-based work from a semiconductor startup; no performance numbers in the abstract. Relevant to anyone modeling DPU lookup-plane power/scalability tradeoffs.

### Scalable Multi-Node AI Workloads in Multi-Tenant AI Clouds using SDN K8s Networking

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t15) · [Slides](https://www.openvswitch.org/support/ovscon2024/Scalable%20Workloads.pptx) · [Recording](https://www.youtube.com/watch?v=68xaDx8mXqQ)

Speakers: Leonid Grossman, Girish Moodalbail, NVIDIA (from abstract only; slides link returned 404)

**Why**: AI east-west traffic between GPUs is the newest design driver for vSwitch and fabric requirements — the reason half the offload talks in this program exist.

**What**: How NVIDIA builds multi-tenant AI cloud networking on OVS/OVN/OVN-Kubernetes: network isolation via overlay virtual network topology, efficient bandwidth via end-to-end QoS, minimizing latency and jitter to prevent GPU underutilization, with much larger gains claimed when OVS-offloadable hardware is used.

**How / Where applicable**: Self-described as a "quick overview"; no metrics, methodology, or failure discussion in the available material. Treat as directional — strategically relevant to AI DC networking, but verify any claims before relying on them.

## Wildcard

### Improving megaflow cache performance in Open vSwitch with branch prediction

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t13) · [Recording](https://www.youtube.com/watch?v=hCVegvOWrqk)

Speakers: Emil Stahl, KTH Royal Institute of Technology; Q&A portion hosted by Eelco Chaudron, Red Hat (from abstract only)

**Why**: An academic outsider's angle on a practitioner problem — the PM wouldn't search for this, and it may preview where datapath caching goes next.

**What**: The argument that the slow path (datapath ↔ control plane interaction on megaflow-cache misses) is poised to become the bottleneck in high-throughput networks, and that upcalls can be reduced by *predicting imminent traffic* — using coflows to anticipate flows before they miss the cache.

**How**: Benchmarks on an OVN-simulated single-node OCP cluster, with XDP timestamping packets at ingress and egress, driven by synthetic coflow traces with varying flow-size distributions; results analyze how prediction accuracy of varying proportions of future flows affects OVS latency.

**Where applicable**: Single-node simulation with synthetic traces — research-stage, not production guidance. The idea of predictive cache warming in a vSwitch is the novel hook.

### Automating Root Cause Analysis in OVS/OVN-Based Deployments Using AI/ML

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2024/#t9) · [Slides](https://www.openvswitch.org/support/ovscon2024/slides/Automating%20Root%20Cause%20Analysis%20in%20OVS_OVN-Based%20Deployments%20Using%20AI_ML.pdf) · [Recording](https://www.youtube.com/watch?v=2OB29dygaH0)

Speakers: Gurpreet Singh, Red Hat, Inc.

**Why**: A PM-to-PM talk that is thin on its own results but signals where vendor investment is going: closed-loop, ML-driven RCA for virtualized networking.

**What**: The problem statement is real and well-framed: OVS/OVN-level metrics are missing in shared virtualized environments, nothing correlates metrics to policies or resource allocation, and RCA is manual and slow. The proposed approach: Self-Organizing-Map-based anomaly detection (citing prior published work reporting 99% accuracy on real DC data, with acknowledged processing-time and scale challenges), a fault-injection sandbox (CPU/network/memory stress, Tx/Rx queue oversubscription) for pre-training models on simulated environments, OpenTelemetry-based collection, and closed-loop anomaly mitigation.

**How**: Architecture and prior work only — no results from the authors' own deployment in the available material.

**Where applicable**: OpenStack/OCP-style virtualized infrastructure; watch with skepticism, but the "train on injected faults in a sandbox before production" pattern is a credible approach to the data-scarcity problem in network ML.

## Themes

- **The offload interface is being renegotiated**: four hardware vendors (NVIDIA twice, Marvell, Intel, DreamBig) independently argue that acceleration bolted on *below* the datapath is architecturally exhausted — the community-facing proposal is a pluggable DPIF, with NVIDIA's DOCA DPIF as the working reference. This is the single most consequential thread in the program.
- **OVN is crossing the overlay boundary**: BGP-based fabric integration, route-advertised failover instead of MAC moves, and composable services — the project is evolving from an overlay island into a fabric-aware routing participant.
- **Observability is becoming a datapath feature**: psample-based ACL sampling, `ofproto/detrace`, Retis enrichment, and live-trace POCs all push per-packet "why" metadata to line rate instead of through upcalls — a notable architectural shift for network security and policy debugging.
- **Host scale is the new pain point**: large-CPU systems expose revalidator lock contention, per-CPU flow-stat memory blowups (782 MB → 1.5 GB from 128 to 256 CPUs), and stack-exhaustion hazards — software datapaths are straining on current-generation servers.
- **Kubernetes is the dominant consumer**: OVN-K8s gets full DPDK/VDUSE userspace paths, native NetworkPolicy sampling, and multi-tenant AI cloud duty — the K8s CNI is where OVS/OVN investment is concentrated.
- **AI east-west traffic is the new design driver**: GPU-to-GPU flows, jitter, and multi-tenant isolation are repeatedly cited as the reason 100G–400G offload, QoS, and isolation work matters now.
