<!--
conference: Open vSwitch and OVN 2025 Fall Conference (Prague)
type: vendor
source_url: https://www.openvswitch.org/support/ovscon2025/
generated: 2026-11-01
registry_key: ovscon-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# OVS + OVN 2025 Fall Conference (Prague) — Digest

This year's program is unusually dense in the PM's core territory: OVN is growing native fabric integration (BGP, BGP-EVPN, transit router), DPUs and hardware offload are driving new upstream OVN/OVS features, and AI/GPU workloads are stress-testing overlay designs. Watch for vendor framing on the NVIDIA DPU talks — several include real testbed numbers, which lifts them above pure product pitch.

## Core

### A native way of integrating OVN into the fabric through BGP-EVPN.

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t11) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/A%20native%20way%20of%20integrating%20OVN%20into%20the%20fabric%20through%20BGP-EVPN.pdf) · [Recording](https://youtu.be/KE-CF8bD1CU)

Ales Musil (Red Hat), Dumitru Ceara (Red Hat)

- **Why**: OVN deployments have historically been islands attached to the physical fabric through gateways or external controllers. With native BGP in 25.03 and experimental BGP-EVPN in 25.09, OVN logical L2 domains now stretch directly into and across the DC fabric — the concrete mechanism by which the overlay joins the EVPN fabric.
- **What**: OVN-native EVPN support: a provider logical switch's L2 domain is extended across an IP fabric via VXLAN, with the BGP-EVPN control plane (run by FRR) distributing MAC/IP (type-2) and, planned for 26.03, type-5 routes. OVN learns remote VTEPs, remote FDBs, remote IPs (with ARP suppression) and remote routes; it advertises local workload MACs/IPs, connected networks and NAT IPs back into the fabric. L2 EVPN is implemented and experimental in 25.09; L3 EVPN per-VRF is the 26.03 plan.
- **How**: The CMS pre-configures `br-$vni` / `lo-$vni` / `vxlan-$vni` interfaces in the default network namespace; OVN monitors FRR/zebra state via NetLink and programs the OVS datapath: per-VTEP OpenFlow cookies on br-int, `tun_id`/`tun_src`/`tun_dst` loads, `learn()` actions with 30s hard timeouts for dynamic FDBs, and ARP-suppression flows on logical routers. Configuration is per logical switch via `dynamic-routing-vni` plus `ovn-evpn-local-ip`.
- **Where applicable**: Any OVN deployment needing L2/L3 fabric extension; datapath-agnostic (OVS kernel or DPDK) and hardware-offload friendly since VXLAN is terminated in OVS. Constraints: at most one local IP per EVPN tunnel today, fixed host-side interface naming (fine-grain naming is an open question), needs FRR on OVN nodes, and it is explicitly experimental with the authors soliciting design feedback.

### Multiple NICs as Encapsulation Endpoints for Large Scale GPU Cloud

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t27) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/Multi-NIC%20OVSCON%202025.pdf) · [Recording](https://youtu.be/fis9WHQ6IiY)

Girish Moodalbail (NVIDIA), Han Zhou (NVIDIA)

- **Why**: In GPU servers each GPU typically has a dedicated NIC (4 GPUs = 4 NICs), so inter-node AI training traffic is multi-homed and each NIC's IP becomes an encapsulation endpoint — while vanilla OVN assumes one encap IP per chassis. This is the scaling problem AI clouds are hitting right now, and it lands squarely in physical DC / scale territory.
- **What**: Multi-NIC encap endpoint support in OVN/OVN-Kubernetes: per-VIF selection of source/destination encapsulation IPs, full-mesh tunnels (all local × all remote encap IPs), new flow programming using an Encap-ID in `REG13[16..31]`, and host-side routing fixes for both the kernel and OVS-DPDK paths. Special cases are handled: distributed gateway ports (skip pinning or fall back to default encap) and ovn-ic transit-switch ports (proposal: multiple TS-LR ports plus `/32` routes and a new `request-encap-ip`).
- **How**: `ovn-encap-ip` carries a comma-separated IP list; per-interface `encap-ip` external_ids drive `Port_Binding:Encap` in the SB DB, populated by ovn-controller. The kernel path needs source-based policy routing plus `rp_filter`/`arp_ignore`/`arp_announce` sysctls; the DPDK path required an upstreamed OVS multi-table routing fix (`ovs-router`). Egress flows scale O(E×P) — local encap IPs × remote port bindings.
- **Where applicable**: Demonstrated on NVIDIA GPU cloud / cloud gaming topologies, but the mechanism is generic OVN. Scale is the open issue: 8 NICs × 1000 chassis ≈ 64k tunnel ports per node, which stresses ovs-vswitchd. Mitigations proposed but not yet landed: flow-based tunnels (loses IPSec/BFD), a "Transport Plane" grouping that cuts 64→8 tunnels per node (87.5% fewer), and intra-node tunneling to preserve HW offload across NICs.

### The BGP Fork in the Road: A Tale of Two Implementations

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t7) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/The%20BGP%20Fork%20in%20the%20Road.pdf) · [Recording](https://youtu.be/2kYhodVu6bM)

Jaime Caamaño Ruiz (Red Hat), Patryk Diak (Red Hat), Surya Seetharaman (Red Hat)

- **Why**: Two BGP implementations were built in parallel — OVN's native dynamic routing and OVN-Kubernetes' FRR-k8s integration — and whether they converge determines how K8s clusters exchange routes with the provider network. BGP internals are squarely in the PM's interest set.
- **What**: A side-by-side anatomy. OVN: BGP-daemon-agnostic ("bring your own FRR"), routes exchanged through kernel VRFs over NetLink, with `Advertised_Route` / `Learned_Route` tables in the OVN DB; by default the VRF carries control-plane traffic only and the host routing table is untouched; `dynamic-routing-vrf-id` frees the VRF table ID from the datapath tunnel key. OVN-Kubernetes: a `RouteAdvertisements` CR generates `FRRConfiguration` for FRR-k8s; in Local Gateway mode a VRF is in the data plane, in Shared Gateway mode BGP-learned routes are copied into OVN gateway routers. Then the gap list for adopting OVN's native BGP: table-ID collisions, distinct vs shared VRFs, default VRF support, filtered learning, real next hops instead of blackhole routes, and per-LSP/per-LB `/32` advertisement.
- **How**: Concrete merge path proposed: CMS-managed table IDs (already landed in controller/northd), shared VRFs as the more efficient but harder option needing extra OVN support (filtered learning, actual next hops on advertised routes).
- **Where applicable**: OVN-Kubernetes / OpenShift clusters peering with provider networks. The merge is a proposal, not a done deal — this is an honest gap analysis, not an announcement.

### Transit router - The distributed router for OVN interconnect.

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t14) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/Transit%20router%20-%20The%20distributed%20router%20for%20OVN%20interconnect.pdf) · [Recording](https://youtu.be/Sf-I7kgc6zo)

Ales Musil (Red Hat), Mairtin O'Loingsigh (Red Hat)

- **Why**: OVN interconnect (ovn-ic) previously offered only a Transit Switch; there was no simple way to route between Availability Zones. The Transit Router fills that gap as a distributed logical router spanning AZs — and it already underpins the OVN-Kubernetes Layer2 re-architecture (see the upgrade talk below).
- **What**: A logical router instantiated across AZs in an ovn-ic deployment, behaving like OVN's distributed routers; new `ovn-ic-nbctl` verbs (`tr-add`, `trp-add`, `trp-del`, `tr-list`); per-AZ ARP learning with ARP responses flooded between AZs via specially added flows. The deck includes a full packet-level walkthrough (SNAT on the gateway router, Geneve tunnels between chassis, `lr_in_ip_routing` flow selection).
- **How**: `tr-add` allocates a unique datapath tunnel key, delegates the ICSB datapath binding, and creates a router in each AZ; `trp-add` assigns resource allocation per AZ, creates logical router ports, and syncs port binding tunnel keys.
- **Where applicable**: Multi-AZ OVN interconnect deployments, generic OVN. Open questions acknowledged: definition and synchronization of routes and route rules across the TR, and "local" TRP port semantics.

### You Want to Upgrade WHAT? A Field Guide to Risky Network Changes

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t21) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/You%20Want%20to%20Upgrade%20WHAT_%20A%20Field%20Guide%20to%20Risky%20Network%20Changes.pdf) · [Recording](https://youtu.be/Xwkwelz9ZBY)

Nadia Pinaeva (NVIDIA), Dumitru Ceara (Red Hat), Patryk Diak (Red Hat)

- **Why**: A rare, detailed production migration narrative: OVN-Kubernetes' legacy Layer2 UDN topology was redesigned around the OVN Transit Router while customers ran on it, with real failure modes and fixes documented — exactly the incident-detail-rich content worth a PM's time.
- **What**: The legacy L2 topology (node-specific gateway routers) broke VM live migration (stale ARP for the migrated gateway MAC; IPv6 RAs from multiple node gateways creating broken multipath defaults, worked around by iptables-blocking external RAs in every L2 pod), doubled maintenance for each new feature, and forced EgressIP hacks. The new topology makes a transit router the network's default gateway with the same IP and MAC on every node. The bulk of the talk walks the rolling upgrade through a half-old/half-new cluster, including hand-crafted routes and dummy IPs to bridge old and new gateway routers during the mixed state, and hand-crafted route advertisements to flush stale routes.
- **How**: Rolling per-node upgrade rewires topology while workloads are drained and rebooted; NAT moves through the transit router; explicit static routes (e.g., `100.65.0.2 via 100.88.0.5`) stitch the two topologies together.
- **Where applicable**: OVN-Kubernetes Layer2 UDNs in production; the authors note it is based on actual joint debugging sessions across the OVN and OVN-Kubernetes communities. The migration playbook generalizes to any non-disruptive OVN topology change.

### A Nightmare on Kube Street: Slicing Kubernetes Networks like Freddy Krueger

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t8) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/A%20Nightmare%20on%20Kube%20Street_%20Slicing%20Kubernetes%20Networks%20like%20Freddy%20Krueger%20-VPCs%20Lightning%20Talk%20-%20OVN_OVS%20Conf%20-%202025.pdf) · [Recording](https://youtu.be/HvmjDHWJheY)

Dave Tucker (Red Hat), Surya Seetharaman (Red Hat)

- **Why**: Kubernetes multi-tenant isolation is still flat; this talk brings cloud-provider VPC semantics to OVN-Kubernetes on top of User-Defined Networks — policy at the network-topology level rather than per-pod NetworkPolicy.
- **What**: A concept mapping of VPC constructs across AWS/Azure/GCP/VMware/OpenStack onto OVN-K8s (UDN = subnet, NetworkPolicy = security groups, OVN routers = route tables/T0-T1 gateways), then a new `ClusterNetworkConnect` CR: a group of label-selected UDNs/cluster networks connected via shared supernet CIDRs (`connectSubnets` per address family with `networkPrefix`), with explicit connectivity grants (PodNetwork, ClusterIPServiceNetwork). Working prototype demonstrated.
- **How**: Label-based `networkSelectors` match UDNs/CUDNs; east-west traffic runs over Geneve, north-south SNATs pod IPs to node IPs; OVN logical switches/routers/policies provide the segmentation.
- **Where applicable**: OVN-Kubernetes clusters needing self-service team networks with platform-team-controlled inter-network communication. Prototype-stage, but with clear forward hooks already named: RouteAdvertisements (BGP), EVPN to provider networks, and cloud-construct integration.

### OVN-Kubernetes Meets DPUs: Enabling Service Function Chaining and Shared OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t13) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/SFC,%20DPU,%20Shared%20OVN.pdf) · [Recording](https://youtu.be/Ssm4DqJ8awc)

Tim Rozet (NVIDIA)

- **Why**: Shows concretely how DPU adoption is driving new OVN features — SFC and "Shared OVN" — i.e., where the OVN architecture is heading for offloaded security/auditing pipelines, with an explicit call for contributors.
- **What**: An SFC design for OVN (RFC 7665 semantics): initially SFC-unaware service functions (no NSH), using Geneve to carry chain metadata between nodes; a new `Service_Function_Chain` NB table with two modes — `local` (no conntrack, allows packet modification, all SFs on one chassis, symmetry requires an explicit reverse chain) and `immutable-global` (conntrack-implied symmetry, chain can cross nodes, no packet modification); `Network_Function_Group` gains a `load-balance` mode for multiple SF instances. Shared OVN: one OVN instance serving multiple CMSs — one per DPU plus one for the host cluster — with RBAC separation.
- **How**: A two-cluster DPU model (Kubernetes running on the DPU) lets DPU admins enforce security at the edge by injecting SFC classifiers as ACLs into the host cluster's traffic; open questions stated plainly — is OVN RBAC secure enough for this, and does shared OVN actually reduce resource consumption?
- **Where applicable**: OVN-Kubernetes on BlueField-class DPUs; enhancement proposal under active discussion (June 2025 ovs-dev thread); single-cluster SFC targeted first, shared two-cluster second.

### Baremetal network isolation for cloud providers with OVN on DPUs

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t18) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/Bare%20Metal%20network%20isolation%20for%20cloud%20providers%20with%20OVN%20on%20DPUs.pptx) · [Recording](https://youtu.be/wDhPPEG16bQ)

Adrian Chiris (NVIDIA), Mael Kimmerlin (NVIDIA), Tarek Abu-Hariri (NVIDIA)

- **Why**: Secure multi-tenancy for bare-metal cloud nodes without per-tenant switch configuration — the DPU is the enforcement point a tenant cannot reach even with privileged host processes. Combines the PM's physical DC and network security interests, and it ships real throughput numbers.
- **What**: OVN/OVS offloaded to BlueField-3 and run in a separate trust domain under cloud-admin control; tenant VPCs (bridged L2 networks with DHCP, masquerade, external routing, floating-IP-class features) enforced transparently to the host, with declarative Kubernetes CRDs (`DPUVPC`, `DPUVirtualNetwork`, `DPUServiceInterface`) mapping bare-metal machines to tenants dynamically. Test results: node-to-node RoCE with Geneve encapsulation on BF3 with 2×200Gb/s links — 191.9 Gb/s without ECMP, 383 Gb/s with ECMP (BGP to an L3 ToR, single hop, OVS-based HBN router).
- **How**: An OVN logical structure modeled on OVN-Kubernetes, optimized for bandwidth and few hops; isolation at the PF/VF level; ECMP via BGP; HBN (host-based networking) OVS router on the DPU.
- **Where applicable**: NVIDIA BlueField-3-specific. Roadmap includes OVN-IC, BGP-EVPN integration (replacing the external router with OVN BGP), SFC, and nested OVNs; the multi-tenancy API is currently admin-only. Real numbers, but from the vendor's own testbed.

### Virtual Network Function integration in OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t12) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVN%20Conference%20-%20Network%20Function%20Insertion.pptx) · [Recording](https://youtu.be/-dxVEMlJlLE)

Sragdhara Datta Chaudhuri (Nutanix), Naveen Yerramneni (Nutanix)

- **Why**: Inserting third-party firewalls / network functions into the OVN traffic path has been a long-standing gap; this is a concrete, code-in-review design for bump-in-the-wire service insertion — network security chaining at the OVN layer.
- **What**: ACL-matched traffic is steered through a VNF's port pair (inline mode) or cloned to the VNF (tap mode); stateful symmetry via conntrack labels; VNF groups with datapath-probe health monitoring; member selection or load balancing across healthy members; configurable fail-close vs fail-open when all members are unhealthy; enforced tunneling for cross-host traffic to and from the VNF's node. Supports active/standby now, active/active planned.
- **How**: New logical-switch pipeline stages, new NB entities for network functions, a new ACL action, a new ovn-controller health-monitor type; conntrack labels redirect response packets and enforce tunnel behavior.
- **Where applicable**: OVN with either VLAN or overlay subnets, vendor-agnostic VNFs. Status: patch series in code review (July 2025 on ovs-dev). Note: the slide deck is mostly diagrams with no extractable detail, so this write-up is grounded in the abstract only.

### Revisiting checksum offloads in OVS

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t20) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/Revisiting%20checksum%20offloads%20in%20OVS.pdf) · [Recording](https://youtu.be/q5Q8v4wY3Vw)

David Marchand (Red Hat)

- **Why**: The userspace (DPDK) datapath's checksum/TSO API had grown buggy and tightly coupled to DPDK; this is a full revamp with per-NIC performance numbers — directly relevant to high-throughput OVS on real hardware.
- **What**: The OVS 3.6 redesign: a new `dp_packet::offloads` field with four-state (unknown/bad/good/partial) Rx statuses for IP and L4, tunnel encapsulation expressed as status metadata, and TSO reduced to a `tso_segsz` value. Massively expanded unit tests caught real bugs (simple-match checksums, IPv6 UDP, conntrack ICMP-embedded checksums, IP fragmentation handling). OVS 3.7 adds an outer-UDP-checksum optimization: for valid inner IPv4/TCP, the outer UDP checksum equals the inner checksum sum, so it can be derived rather than computed — plus "partial segmentation" so HW TSO packets can use it.
- **How**: Inner/outer statuses split via a 16-bit shift; netdev drivers (netdev-dpdk) translate OVS statuses into mbuf Tx flags, isolating OVS core from DPDK/kernel APIs. Measured on mlx5 CX-6 Dx: Geneve TCP 6.08 → 7.31 Gbit/s from the outer-UDP optimization, and 7.3 → 10.4 Gbit/s at 37% CPU once HW TSO works; comparative numbers across CX-6 Dx, X710 and E810, including which NICs lack outer UDP checksum offload entirely.
- **Where applicable**: OVS userspace/DPDK datapath; behavior is NIC-specific and the feature is still marked experimental (the talk asks whether to change that). The CX-6 Dx gap found here directly feeds the VDUSE talk's benchmark findings.

### OpenFlow Classifier: Arcane knowledge and common pitfalls

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t4) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OpenFlow%20Classifier_%20Arcane%20knowledge%20and%20common%20pitfalls.pdf) · [Recording](https://youtu.be/pbr2lR1wyKc)

Ilya Maximets (Red Hat)

- **Why**: The classifier is the hottest path in OVS and determines megaflow quality, which drives datapath autonomy and flow-cache effectiveness. Understanding its subtable model explains OVN pipeline performance and recent regressions and fixes — core datapath-internals material, delivered by a current maintainer.
- **What**: A deep dive: rules are grouped by match pattern into per-mask hash "subtables"; lookup iterates subtables ordered by the highest priority they contain; complexity is O(1) per subtable hit and O(n) over distinct masks. "Un-wildcarding" produces the megaflow mask — false 1-bits are allowed but degrade caching; false 0-bits are correctness bugs. Optimizations covered: staged lookup (the mask split into 4 segments with early exit, sharply reducing un-wildcarded bits for non-matching packets) and prefix tracking. Pitfalls: mask explosion from many distinct match patterns, and historically from OVN's inequality matches (single-bit masks, fixed October 2025 to use prefixes; IPv6 address pairs can still theoretically yield 128×128 masks).
- **How**: Practical do/don't guidance for OpenFlow pipeline authors: match earlier-stage fields alongside later ones where logic permits, never let struct flow dependencies cross segment boundaries, and avoid generating fragmented masks.
- **Where applicable**: Every OVS deployment; especially relevant to OVN logical-flow generation and anyone reading megaflow traces.

## Adjacent

### Beam Me Through the Datapath: VDUSE for OpenShift Virtualization

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t24) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVSOVNCON25%20-%20Beam%20Me%20Through%20the%20Datapath_%20VDUSE%20for%20OpenShift%20Virtualization.pdf) · [Recording](https://youtu.be/Tuqz3m4oH4Q)

Jakob Meng (Red Hat), Maxime Coquelin (Red Hat)

- **Why**: Completes a fully-userspace datapath (OVS-DPDK + VDUSE) for KubeVirt VMs, with unusually transparent benchmarking that includes cases where DPDK loses to the kernel datapath.
- **What**: Extends last year's container userspace work to VMs via VDUSE/vhost-vDPA (primary and secondary networks), plus new workload-partitioning knobs in OpenShift (`strict-cpu-reservation`, dedicated `CPUSet`, `irqbalanceBanned`, static PMD masks). Benchmarks (Xeon Silver 4310, CX-6 Dx, OVS 3.5+): OVS-kernel outperforms OVS-DPDK on large TCP buffers; small-buffer throughput improves with `pmd-sleep-max` (~90,000 → ~3,000 IRQs/s, QEMU 200% → 115% CPU at 128B buffers) at the cost of large-buffer performance; a virtio-net IRQ-coalescing prototype in the DPDK vhost library fixes that without sleeps. Also documents CX-6 Dx lacking outer-UDP checksum offload (which forced software segmentation — tying into the checksum-offload revamp) and KubeVirt's fixed 256-descriptor virtio rings.
- **How**: VDUSE is a purely software vDPA device implemented by a userspace application (the OVS DPDK vhost backend), attached through the vDPA bus; vhost-vDPA serves QEMU.
- **Where applicable**: OpenShift Virtualization, telco and real-time use cases. Preliminary results, explicitly framed as transparent benchmarks; the partitioning APIs are OpenShift-specific but the datapath work is upstream OVS/DPDK.

### Observing Open vSwitch with native prometheus metrics

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t1) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVScon25%20-%20Observing%20OVS%20with%20native%20prometheus%20metrics.pdf) · [Recording](https://youtu.be/awHSbUbCNoo)

Gaetan Rivet (NVIDIA)

- **Why**: OVS observability today depends on external exporters that assume the kernel datapath and scrape CLIs; a native exporter unifies kernel and userspace observability with lower footprint — practical for anyone running OVS at scale.
- **What**: A Prometheus-compatible metrics framework inside the OVS library: counter/gauge/histogram types, and a per-process metrics tree whose internal nodes mirror module structure (datapath cache/conntrack/offloads, interfaces, memory, ofproto). Node types cover subsystems, labeled collections (FOREACH), bounded collections for label generation, and conditionals (e.g., offload metrics only when `hw-offload` is on). Exposed via an `ovs-exporter` systemd service (default port 6103), `ovs-appctl metrics/show`, and Python bindings; new metrics appear automatically without new CLI plumbing.
- **How**: The tree is statically defined (API in `lib/metrics.h`), interpreted at scrape time, and rendered into the Prometheus text model — the design is deliberately output-format-agnostic so other formats could follow.
- **Where applicable**: OVS kernel and userspace datapaths alike; initial coverage: resource consumption, interface counters and link state, ofproto upcalls/revalidation, and coverage counters. Complements (rather than competes with) DOCA-Telemetry on NVIDIA kit.

### OVS-DOCA live-upgrade

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t16) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/Copy%20of%20Eli%20Britstein%20-%20ovs-doca-live-upgrade.pptx) · [Recording](https://youtu.be/k-4A8YF7aU0)

Eli Britstein (NVIDIA)

- **Why**: Upgrading ovs-vswitchd in production today means a full daemon restart — losing conntrack state (dropping TCP sessions), FDB, meters, groups, TLV-map, configured routes, and tunnel neighbor tables, plus re-initializing ports with offloads. A zero-downtime model matters for any DC or carrier SLA.
- **What**: OVS-DOCA achieves in-place upgrades by starting the new version in client mode alongside the running server: the server keeps forwarding while the new instance initializes ports and offloads in parallel; volatile state is migrated to the new instance; then a zero-time handover and server termination. Version and resource constraints, failure handling, and rollback are addressed.
- **How**: DOCA can initialize the same ports from different userspace processes and hand over between them with zero interruption.
- **Where applicable**: OVS-DOCA (NVIDIA's downstream OVS) on ConnectX/BlueField — not upstream OVS today. The state-migration problem it solves, however, is universal for production OVS. (from abstract only; the slide deck could not be extracted and the program page adds nothing beyond the abstract)

### OVS-DOCA upstream roadmap

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t17) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVS-DOCA%20upstream%20roadmap.pptx) · [Recording](https://youtu.be/3QGWH54xdfE)

Maor Dickman (NVIDIA)

- **Why**: Signals where hardware offload in upstream OVS is heading: NVIDIA is moving DOCA acceleration from a downstream fork into upstream via the dpif-netdev framework, which means new upstream OVS APIs (dpif-offload-provider, userspace CT offload).
- **What**: The plan: a new `netdev_doca` netdev class (port initialization and software slow path under dpif-netdev), a new `dpif-offload-doca` provider (offloading megaflows, based on a new dpif-offload-provider API), and a new connection-tracking offload API for the userspace datapath. Gaps are acknowledged: eswitch hierarchy (one port handling all device ports), port-init ordering, partial offload (HW-to-SW miss path), and advanced offloads (sFLOW, tunnel entropy, meters, DP_HASH). This replaces the earlier dpif-netlink-based DPIF-DOCA direction.
- **How**: Staged upstreaming steps are enumerated: offload-provider first, then the netdev, then dpif-offload-doca, then agreement on the CT offload API. DPIF-DOCA will live as a standalone open-source library while DOCA-Flow/DOCA-Eth remain closed-source.
- **Where applicable**: ConnectX/BlueField with the OVS userspace datapath. Vendor roadmap — but with concrete architectural consequences for upstream OVS; watch the dpif-offload-provider and CT-offload API discussions if you care about offload in OVS.

### Turbocharge Kubernetes with offloaded OVN-Kubernetes and OVS on DPUs

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t28) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVS%20CONFERENCE%20-%20Turbocharge%20Kubernetes.pdf) · [Recording](https://youtu.be/t-BPwTzb_1I)

Alin Serdean (NVIDIA), Amit Zala (NVIDIA), Mael Kimmerlin (NVIDIA), Igal Tsoiref (Red Hat)

- **Why**: A production-oriented, DPU-offloaded Kubernetes platform (DPF) with benchmark numbers — and a notable strategic shift: OVN-Kubernetes is moving upstream-first, reviving DPU-host mode after roughly two years dormant.
- **What**: DPF (DOCA Platform Framework) manages DPU fleets declaratively: DPUSet provisioning (BFB images), DPUService/DPUServiceChain lifecycle via ArgoCD, version-compatibility gating, and rollout-velocity budgets; service chaining runs an OpenFlow controller patch-paneling OVS ports on the DPU; OVN-Kubernetes runs in DPU mode with hardware acceleration for workload pods alongside HBN. Measured 354.92 Gbit/s iperf3 between pods across two BF3 nodes through HBN plus the service chain. Future work: OVN-K as the DPU cluster's primary CNI (dropping Flannel), 2+ OVN-K instances per host, RDMA-accelerated traffic in OpenShift, and selective pod offloading instead of "offload everything".
- **How**: Two-cluster model — host cluster plus DPU clusters run as HyperShift hosted control planes; RHCOS brought to BlueField via a custom coreos-installer flow; the SC CNI stamps DPF service metadata onto OVS ports so the chaining controller can create patch-panel rules.
- **Where applicable**: NVIDIA BlueField-3 + OpenShift. Treat the numbers as vendor-reported (some slides were marked NVIDIA confidential) — but the OVN-Kubernetes upstream-first shift, DPU-host-mode revival, and the OpenShift integration challenges (CNO, security model, RHCOS) are genuine engineering signal.

### Space - building a CMS with OVN Concepts

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t22) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/2025_ovn_con_space.pdf) · [Recording](https://youtu.be/joVVeEklhZA)

Felix Huettner (StackIt)

- **Why**: An end-user case study of a cloud provider whose requirements (policy-based routing combined with dynamic routing, deny ACLs, per-ACL logging) outgrew Neutron — and who, rather than replacing OVN, built a custom CMS layer on OVN design concepts.
- **What**: "spaced", a Go daemon using ovn-kubernetes' libovsdb, translating a custom "spacebound" OVSDB schema into the standard OVN northbound DB — effectively a custom northd. It coexists with Neutron through per-table resource ownership (either Neutron or spaced writes a given NB table), with a full migration off Neutron as the long-term goal.
- **How**: Sticks to OVN's layered model (NB/SB/northd/ovn-controller), inserting spaced between the CMS and NB; the processing engine is modeled on OVN's incremental-processing engine (not yet implemented). Challenges listed honestly: libovsdb is event-driven with no consistent-state reads, no automatic reference resolution, and no change tracking.
- **Where applicable**: StackIT / Schwarz Digits' OpenStack+OVN production environment — org-specific, but a useful template for anyone considering building a CMS directly on OVN primitives instead of adopting a full CMS.

### Programming OVS bridges using OVN Bridge Controller

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t23) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVN%20Bridge%20Controller.pdf) · [Recording](https://youtu.be/MR0pG26JsoE)

Numan Siddique (Crusoe AI)

- **Why**: New in OVN 26.03 (merged the week before the conference): program any OVS bridge using OVN logical-flow syntax instead of raw OpenFlow — motivated by a real end user (Crusoe) that needed to program provider bridges after the OVN pipeline.
- **What**: `ovn-br-controller` plus a new OVN Bridge OVSDB database; the CMS writes logical flows (bridge, table, priority, match, actions) and the controller compiles them to OpenFlow exactly as ovn-controller programs br-int. It injects physical mapping flows (loading interface ofports into registers, a NORMAL fallback) and translates logical actions into concrete rules; multiple bridges per host are supported.
- **How**: Per-hypervisor services started via ovn-ctl; `external_ids:ovn-br-remote` points the controller at the ovnbr DB; an `ovn-brctl` CLI handles bridge and flow creation.
- **Where applicable**: Anyone programming provider/physical bridges on top of OVN-based stacks. Current limitations are stated: no restriction against adding br-int, and OVN-specific controller actions (put_dhcp_opts, put_fdb) are not yet restricted; incremental processing and code-sharing with ovn-controller are future work.

## Wildcard

### OvS and Socket Maps - Beyond ports as endpoints

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t25) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OvS%20and%20Socket%20Maps.pdf) · [Recording](https://youtu.be/ONVxHA9chJU)

Aaron Conole (Red Hat)

- **Why**: A genuinely surprising datapath idea: treat application sockets as packet endpoints and skip the IP stack entirely. Measured ~1000ns of 7395ns per-packet protocol overhead in netns-to-netns forwarding — relevant to anyone watching eBPF/XDP-style bypass techniques reach general SDN tooling.
- **What**: An exploration with four prototype approaches (in-datapath table, userspace-centric, eBPF-based, plus a socket-map variant), with numbers: 7395 → 6190ns per packet (and ~23k more 65k-packets/s) using a `sock(try)` action to skip conntrack; the socket-map-style approach measured 8254ns — essentially identical to plain output, reported without spin. Difficulty is candidly labeled "very much a nightmare": tracking sockets across netns boundaries and rewriting recirc state. Preliminary patches are posted; the direction is undecided.
- **How**: OVS already knows the destination socket from tuple/conntrack state; `sock()` actions would enqueue directly to application sockets, skipping L3 routing and re-parsing inside the target netns, while trying to preserve OVS's flow-centric (megaflow) semantics.
- **Where applicable**: OVS kernel datapath with local (same-host) endpoints; experimental RFC stage (June 2025 ovs-dev thread). The eBPF variant is described as the most future-proof but hardest to integrate with OVS userspace.

### When CI Shouts Back: LLMs in the OVS CI Pipeline

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t2) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/When%20CI%20Shouts%20Back_%20LLMs%20in%20the%20OVS%20CI%20Pipeline.pdf) · [Recording](https://youtu.be/JCmHuCVmOVs)

Aaron Conole (Red Hat)

- **Why**: Not networking — but a clear signal of where core infrastructure projects are heading: LLM-assisted code review inside the OVS CI pipeline, with the friction reported honestly rather than sold.
- **What**: Experiments with CodeRabbit, Sourcery, and Claude SONNET-class models on OVS patch review. Findings: PR-based bot workflows fragment patch discussion into a second venue, branches must be kept very tightly in sync, and bots contradict themselves between runs ("suggest doing one thing then doing another"). A custom Claude-based reviewer (RFC on patchwork) offers own prompts, developer-runnable execution, and GitHub Actions integration — at real dollar cost.
- **How**: PW-CI infrastructure changes plus custom prompting instead of SaaS review bots.
- **Where applicable**: OVS CI specifically, but the lessons (bot consistency, cost, review-venue splitting) generalize to any patch-based OSS project evaluating review bots.

### AI-Powered Performance Insights: Integrating OVS/OVN automatic performance regression analysis with LLMs

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2025/#t3) · [Slides](https://www.openvswitch.org/support/ovscon2025/slides/OVS'25_%20AI-Powered%20Performance%20Insights.pdf) · [Recording](https://youtu.be/LT6FQG9fR3k)

Joe Talerico (Red Hat), Jose Castillo Lema (Red Hat), Mohit Sheth (Red Hat)

- **Why**: Shows how performance engineering for Kubernetes networking is being automated and made LLM-queryable — shift-left performance testing operating at real scale, with coverage numbers rather than claims.
- **What**: Red Hat Perf&Scale's continuous performance testing: benchmarks (k8s-netperf, ingress-perf, cluster-density-v2) run against PRs early; Orion, a Python library doing automated statistical regression detection (Apache Otava e-divisive change-point detection) over an Elastic/OpenSearch data warehouse; and Orion-MCP, an MCP server that lets LLMs answer "has my PR regressed OpenShift?", correlate regressions with PR changelogs, and surface version-tagged results (OVN, OVN-K, OVS versions per run). Scale: 5 platforms (AWS, Azure, GCP, IBM, bare metal, plus ROSA/ARO), 100+ weekly tests; 2025 added net-new workloads for UDN L2/L3, Virt UDN, NetworkPolicy, EgressIP and BGP, with 30+ downstream bugs filed.
- **How**: Fingerprint-based result retrieval (platform, node types/counts, benchmark, `networkType: OVNKubernetes`), change-point detection on the matched series, and MCP tool calls surfaced through Slack (GitHub integration next). Next steps: agentic AI for CPT and pushing a perf workload into ovn-ci upstream.
- **Where applicable**: OpenShift/OVN-Kubernetes development workflow; Red Hat-internal tooling, but the Orion + Orion-MCP pattern is directly replicable by any team with a benchmark data warehouse.

## Themes

- **OVN is growing into the physical fabric.** Native BGP (25.03), experimental BGP-EVPN (25.09, L3 EVPN planned for 26.03), and the Transit Router for inter-AZ routing all landed within a year. The overlay/underlay boundary in OVN deployments is dissolving — fabric integration is becoming an OVN-native capability rather than an external-gateway problem.
- **DPU and hardware offload work is moving upstream.** Four DPU talks (baremetal isolation, OVN-K DPU mode, SFC/Shared OVN, DPF) plus the OVS-DOCA upstream roadmap: offload architecture is being reworked into upstream OVS APIs (dpif-offload-provider, userspace CT offload) instead of living in vendor forks. Watch the OVN SFC and Shared OVN enhancement proposals — they define the next two release cycles.
- **AI/GPU workloads are reshaping overlay requirements.** Multi-NIC encapsulation endpoints, 64k-tunnel scale limits, RoCE-over-Geneve benchmarks, and RDMA enablement roadmaps: AI infrastructure is stress-testing overlay designs designed for one encap IP per chassis.
- **Kubernetes multi-tenancy is converging on cloud-provider VPC semantics.** UDNs, ClusterNetworkConnect/VPC grouping, EgressIP and RouteAdvertisements are all landing on OVN logical-topology primitives — K8s networking is catching up to AWS/NSX isolation models.
- **Unusually honest results culture.** Several talks publish negative or preliminary numbers openly (userspace DPDK losing to the kernel on large buffers; the socket-map approach measuring no better than plain output) alongside a production migration war story with real failure modes. Good signal quality for a vendor-adjacent event — weight these over the pure demo talks.
- **LLMs are entering the project maintenance loop.** CI code-review bots (with their inconsistencies) and MCP-driven performance regression analysis both appeared this year — early, imperfect, and worth tracking as an emerging subfield.
- **Zero-disruption operations are the new battleground.** OVS-DOCA live-upgrade with state migration and the OVN-K rolling topology rewire both tackle the same problem: changing the dataplane without dropping traffic — historically the weakest point of OVS/OVN in production.
