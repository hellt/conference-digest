<!--
conference: FOSDEM 2026
type: vendor
source_url: https://fosdem.org/2026/schedule/xml
generated: 2026-11-04
registry_key: fosdem-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# FOSDEM 2026

FOSDEM 2026's Network, eBPF, Security, Identity, and Confidential Computing devrooms carry an unusually high density of contributor-led internals talks this year, several with hard production numbers (Cisco's 50K-tunnel IPsec deployment, Meta's RDMA failure telemetry, IIT Bombay's FLASH benchmarks). Identity content is similarly strong, with passkeys-on-Linux and attested-TLS standardization both moving from ideas to shipping code. Picks below are grouped by relevance; note that the OpenPERouter and EVPN/KubeVirt talks are companion sessions from the same Red Hat team.

## Core

### Harnessing Hardware for High-Performance Traffic Management in FD.io/VPP

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/TWNGYR-vpp-hardware-traffic-management/) · [Slides](https://fosdem.org/2026/events/attachments/TWNGYR-vpp-hardware-traffic-management/slides/266735/fosdem_2_pgf5byb.pptx) · [Recording](https://video.fosdem.org/2026/h1302/TWNGYR-vpp-hardware-traffic-management.mp4)

Venkata Ravichandra Mynidi, Alok Mishra

- **Why**: VPP does all traffic management (shaping, scheduling, policing) in software today, and CPU cost grows with traffic classes — a real SLA risk at 100G/200G+. This is the project's answer for QoS at 400G/800G, directly relevant to physical DC/telco datapaths.
- **What**: A vendor-neutral, capability-based framework that offloads VPP's TM to hardware TM engines in NICs, SmartNICs, and DPUs. Software TM remains fully supported; upstream patches are planned (the slides also reference Marvell DPU/adapter solutions).
- **How**: Hardware advertises TM capabilities; VPP adapts. Flows are classified in software (coupled with VPP's classifier, driven via binary APIs) and steered to hardware queues where hierarchical scheduling, dual-rate shaping (committed/peak, per the abstract RFC 2698-compliant), strict priority + weighted fairness, and line-rate policing are enforced. TM nodes support runtime add/update/suspend/resume/delete.
- **Where applicable**: Any VPP deployment needing per-tenant SLAs at high bandwidth; the API is designed to be silicon-agnostic, but real support depends on NICs/DPUs exposing TM engines. Caveat: the slides are mostly architecture diagrams — no benchmark numbers were presented, so treat the performance claims as directionally right but unproven.

### Scaling Secure Network Functions: High-Performance IPsec with FD.io VPP for VNFs and CNFs

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/Y9EZ9G-scaling_secure_network_functions/) · [Slides](https://fosdem.org/2026/events/attachments/Y9EZ9G-scaling_secure_network_functions/slides/266891/presentat_7vkk4dv.pdf) · [Recording](https://video.fosdem.org/2026/h1302/Y9EZ9G-scaling_secure_network_functions.mp4)

Benoît Ganne (Cisco, VPP committer)

- **Why**: One of the few IPsec talks with real production scale behind it: Cisco runs 50K tunnels, 7 PB/month, 10 trillion packets/month on VPP IPsec. The benchmarks are concrete and actionable.
- **What**: A deep dive into VPP's IPsec implementation plus 2024–2025 improvements (unified crypto+HMAC single-op-per-packet, template-based ESP, full IPv6 NAT-T, async handoff tuning), with a decision framework for the three tunnel modes.
- **How**: Key measured results (FD.io CSIT, 10K tunnels, AES-256-GCM, Intel ICX): policy-based IPsec is unusable without the flow cache (which is ~40x faster); with it, 1–4 cores deliver 20–49 Gbps; route-based P2P reaches 78 Gbps on 100G. Async crypto decouples crypto from packet processing, enabling 70 Gbps on a *single* tunnel (2.5x sync) and preventing noisy-neighbor starvation. For 1000+ VRFs, switching the IPv4 FIB mtrie from 16-8-8 to 8-8-8-8 cuts memory 41x (330 MB → 8 MB) at the cost of one extra lookup step.
- **Where applicable**: SD-WAN, 5G UPF (N3/N9), edge, and large DC VPN gateways. Kernel-IPsec shops hitting per-tunnel interface or memory ceilings are the natural audience. No kernel modules, so it runs cleanly in containers.

### So you want to do RDMA programming? RTRS: An easy to use, reliable high speed transport library over RDMA

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/RLNUAB-rtrs/) · [Slides](https://fosdem.org/2026/events/attachments/RLNUAB-rtrs/slides/266906/rtrs_reli_jcbogzl.pdf) · [Recording](https://video.fosdem.org/2026/h1302/RLNUAB-rtrs.mp4)

Haris, Jinpu Wang

- **Why**: RDMA programming is notoriously harder than sockets, yet it's now the default fabric for AI training and lossless DC workloads. RTRS is battle-tested infrastructure (5,000+ servers) that hides most of that complexity.
- **What**: A reliable high-speed transport library over RDMA, already in the mainline kernel (`drivers/infiniband/ulp/rtrs` as of v6.17.7), presenting a socket-like abstraction with production-grade reliability features.
- **How**: Establishes stateful sessions with heartbeats and multipath (selectable policies) with I/O failover and load balancing; sizes the connection count to CPU count with IRQ pinning for data transfers; accepts scatter-gather lists directly; and pre-allocates/pre-maps DMA buffers on the server side to shorten the data path.
- **Where applicable**: Building blocks for any module that wants RDMA without verbs-level expertise — the speakers call out ML/AI training as a beneficiary of the pre-mapping work. Being an in-tree kernel ULP, it constrains you to its session model. (The event page adds nothing beyond the abstract, which this write-up is based on.)

### Lessons from scaling BPF to detect RDMA Device Drivers Bugs in real time

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/HAWVVD-rdmatracer/) · [Slides](https://fosdem.org/2026/events/attachments/HAWVVD-rdmatracer/slides/266686/final_bpf_yeejdwk.pdf) · [Recording](https://video.fosdem.org/2026/h1308/HAWVVD-rdmatracer.mp4)

Prankur Gupta, Maksim Samoilov (Meta)

- **Why**: RDMA driver bugs are a top killer of AI training jobs — 10–20% of Meta's daily AI job crashes are RDMA-related (syscall errors), wasting 32K+ GPU-hours in six months, 5K+ attributable to the RDMA subsystem. This is the eBPF observability answer, with measured production overhead.
- **What**: RDMATracer, an eBPF-based framework that detects RDMA driver bugs in real time by tracing the opaque control path between verbs ioctls and the NIC, then differring live traces against known-good ones. Diagnosis time dropped from 10+ minutes to seconds.
- **How**: Since all RDMA interactions map to one syscall, they use static analysis to prune the traced call graph (skip reads, pure-kernel internals, refcount/cleanup functions; focus per-vendor driver calls). They chose fexit over kretprobes (~72% of the overhead), shared maps with a ~256KB ring buffer for error context, per-CPU counters for syscall/error/errno tracking, and a reactive "collect on error" design. Production impact: `bpf_tax` p50 down 88.7%, p99 down 98.9%, no measurable QPS change.
- **Where applicable**: Any large RDMA fleet (Meta-scale, but the static-analysis pruning idea generalizes to other opaque syscall interfaces). Notably it triaged a bug in a black-box vendor driver that dmesg alone couldn't localize.

### Extending AF_XDP for fast co-located packet transfer

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/E8RFHV-flash-afxdp/) · [Slides (PDF)](https://fosdem.org/2026/events/attachments/E8RFHV-flash-afxdp/slides/266831/fosdem26-_n5vpfki.pdf) · [Slides (PPTX)](https://fosdem.org/2026/events/attachments/E8RFHV-flash-afxdp/slides/266831/fosdem26_8t3qcla.pptx) · [Recording](https://video.fosdem.org/2026/h1308/E8RFHV-flash-afxdp.mp4)

Debojeet Das (IIT Bombay, SynerG)

- **Why**: AF_XDP has no efficient way to forward packets between sockets — even localhost redirection today needs SR-IOV or an external switch. This closes the gap and keeps AF_XDP competitive with DPDK-style chaining. Also a published SoCC'25 paper.
- **What**: FLASH, a ~700-LoC kernel extension enabling low-overhead, in-kernel packet transfer between AF_XDP sockets: zero-copy for sockets sharing a UMEM, single-copy otherwise. Measured 1.1–2.5x higher throughput than SR-IOV-based approaches, with the lowest latency among all compared options (baseline: OpenNetVM/DPDK chaining).
- **How**: Backward-compatible MP/MC lockless rings (CAS serialization in-kernel, SP/SC preserved for userspace, no API changes); batched redirections with partial-TX + descriptor buffering to handle capacity changing mid-batch; smart polling with early backpressure (POLLOUT blocking, MSG_MORE wakeups) extending hybrid interrupt/busy-poll across the redirection path; a sysfs interface (`/sys/kernel/flash`) for chaining rules; and a Rust runtime + FLASH monitor for multi-tenant isolation.
- **Where applicable**: Co-located network functions (firewall → LB → router chains) on one host. Driver support already exists for ixgbe, i40e, ice, and mlx5. Roadmap replaces sysfs with an XDP_EGRESS hook, making steering programmable via eBPF.

### Rich Packet Metadata - The Saga Continues

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/DSC9L3-rich-packet-metadata/) · [Slides](https://fosdem.org/2026/events/attachments/DSC9L3-rich-packet-metadata/slides/267695/2026_fosd_vdfxkjo.pdf) · [Recording](https://video.fosdem.org/2026/ua2114/DSC9L3-rich-packet-metadata.mp4)

Jakub Sitnicki (Cloudflare)

- **Why**: The Linux network stack gives packets only 32 bits of sticky metadata (`SO_MARK`), and everyone is fighting over them. Cloudflare wants 128+ bytes for config consistency across layers, XDP classification, and drop attribution — and this is the unvarnished three-year engineering history, dead ends included.
- **What**: A progress report on three successive designs: (1) SKB Traits, a per-packet key-value store — abandoned ("don't introduce a second metadata area"); (2) XDP/skb metadata via a new `bpf_dynptr_from_skb_meta()` kfunc (v6.18), with helpers preserving metadata (v6.15) and metadata tracking decoupled from MAC-header offsets (v6.19) — necessary because L2 tunnels and header pushes corrupt or strand metadata otherwise; (3) the current idea: an `skb_ext` extension backed by BPF local storage (`BPF_MAP_SKB_STORAGE`), which lives separately from packet headers.
- **How**: Approach 3 reuses the existing `bpf_local_storage` machinery (flexible-array elements, map-backed) attached to `sk_buff` via the skb extension mechanism. The unsolved problem is memory allocation on the hot path — which is exactly why approaches 1 and 2 were tried first.
- **Where applicable**: Anyone building multi-layer in-kernel pipelines (XDP → TC → netfilter → socket) that need per-packet context to survive. Watch this if you do XDP classification or drop accounting; the landing kernel version will determine what's expressible.

### Optimizing eBPF loading with reachability analysis

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/79EHZ7-optimizing_ebpf_loading_with_reachability_analysis/) · [Slides](https://fosdem.org/2026/events/attachments/79EHZ7-optimizing_ebpf_loading_with_reachability_analysis/slides/266727/fosdem_20_ii0pquo.pdf) · [Recording](https://video.fosdem.org/2026/h1308/79EHZ7-optimizing_ebpf_loading_with_reachability_analysis.mp4)

Dylan Reemerink (Isovalent/Cisco; Cilium committer, ebpf-go maintainer)

- **Why**: Cilium still ships a compiler and builds eBPF on-target — the last major project not on CO-RE. The blocker is a genuine kernel bug class: with load-time config, dead code still creates maps and tail calls because the verifier increments map refcounts before dead-code elimination runs. This is the fix that unlocks Cilium's CO-RE migration.
- **What**: A userspace reachability analysis (in ebpf-go) that predicts, given a set of global constants, which eBPF instructions are unreachable — so unused maps are never created and unused tail calls never loaded. The analysis has false negatives but no false positives.
- **How**: Builds a basic-block graph over the program's instructions, evaluates branches on `.rodata`-backed config variables, and handles the hard cases: backtracking through stack spills, sign extensions (including the new ISAv3 32-bit forms), bitmask/shift patterns, 64-bit immediates beyond branch-imm width, and more. Cilium has 94 datapath settings, so the payoff is large: smaller images, faster loads, less attack surface.
- **Where applicable**: Cilium first, but the technique applies to any CO-RE project with heavy feature toggles. The speaker also flags that the verifier's map-refcount handling could be improved in-kernel. Watch the Cilium roadmap: this is a direct signal of the project's pre-compiled future.

### Scaling GoBGP: Lessons from Building a Dynamic, API‑Driven BGP Control Plane

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/EYAYCF-scaling-gobgp/) · [Slides](https://fosdem.org/2026/events/attachments/EYAYCF-scaling-gobgp/slides/267027/fosdem_98e8cma.pptx) · [Recording](https://video.fosdem.org/2026/h1302/EYAYCF-scaling-gobgp.mp4)

Maxime Peim (Cisco)

- **Why**: Real lessons from running GoBGP as a multi-tenant, API-driven control plane at fabric scale — including an honest comparison showing GoBGP scales worse than Bird/FRR, and what's being done about it upstream.
- **What**: Architecture and operational patterns for a multi-tenant BGP daemon: per-tenant BGP servers, route policies, and address families sharing one control plane; tenant lifecycle (create/update/delete) handled via gRPC without disrupting existing sessions.
- **How**: GoBGP was chosen for its API dynamism, path manipulation strength, and Go integration (goroutine-native, Go package + gRPC interfaces), against Bird 3.0 (now multi-threaded, fast, but static config) and FRR (multi-threaded, static). Scaling targets: tens of thousands of peers per region, hundreds of thousands of routes. The deck includes benchmark methodology and results (mostly graphs), and reports that v4.2.0 shipped some contention fixes; PR #3303 (global mutex relaxation) improves benchmarks significantly in the same configuration — an explicit call for contributors.
- **Where applicable**: Service-provider-style fabrics, SD-WAN control planes, or any system needing programmatic BGP (service discovery, orchestration feedback). If you need raw route-processing throughput, Bird/FRR still win; the value here is the API surface.

### OpenPERouter: Turning Your Kubernetes Nodes into a Provide Edge Router

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/TUEQCR-openperouter_turning_your_kubernetes_nodes_into_a_provide_edge_router/) · [Slides](https://fosdem.org/2026/events/attachments/TUEQCR-openperouter_turning_your_kubernetes_nodes_into_a_provide_edge_router/slides/266993/openperou_qpsl5ce.pdf) · [Recording](https://video.fosdem.org/2026/h1302/TUEQCR-openperouter_turning_your_kubernetes_nodes_into_a_provide_edge_router.mp4)

Miguel Duarte, Federico Paolinelli (Red Hat)

- **Why**: Bridges the PM's two worlds directly: it moves VPN/EVPN termination from the ToR leaves onto Kubernetes nodes, resolving the classic "who configures the fabric" friction between networking and cloud teams.
- **What**: A lightweight open-source Provider Edge router running on Linux hosts / K8s nodes in a separate network namespace, with FRR as the control plane. The host sees normal interfaces and BGP peers — anything that can talk to a router can talk to OpenPERouter. Configuration is CR-driven (Underlay, L3VNI, L2VNI CRDs).
- **How**: EVPN-VXLAN tunnels are created dynamically per VNI; L3 routes (including MetalLB's, translated to EVPN Type 5) propagate over the corresponding veth session; L2 domains are exposed as veth legs bridgeable to any virtual switch. Underlay to the ToR is set up either by moving the interface into the namespace or via Multus. The result: leaves get "dumber" — no per-network tunnel config, no networking-team ticket for each new overlay.
- **Where applicable**: Bare-metal K8s clusters that need L3VPN/L2VPN integration with an existing EVPN fabric. Integrations documented for MetalLB, Calico, and KubeVirt. Roadmap: SR-IOV interface handling, a Day-0 standalone systemd mode, SRv6 as just another VPN type, and a pluggable faster datapath (kernel today, DPDK-based Grout later).

### Weaving the Fabric: EVPN overlays for multi-cluster KubeVirt deployments

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/3BXRZM-evpn-overlays-for-multi-cluster-kubevirt/) · [Slides](https://fosdem.org/2026/events/attachments/3BXRZM-evpn-overlays-for-multi-cluster-kubevirt/slides/266844/weaving-t_74snbna.pdf) · [Recording](https://video.fosdem.org/2026/h2213/3BXRZM-evpn-overlays-for-multi-cluster-kubevirt.mp4)

Miguel Duarte, Federico Paolinelli (Red Hat)

- **Why**: The companion session to OpenPERouter, focused on the fabric problem: stretched L2 for cross-cluster VM live migration, DR, and hybrid cloud — done with open components rather than a proprietary DCI.
- **What**: Multi-cluster KubeVirt L2/L3 overlays built from OpenPERouter + KubeVirt + any bridge-based CNI (OVS-CNI, bridge-cni, macvlan, ipvlan). L2VNI stretches a Layer 2 domain across clusters with a distributed anycast gateway and live-migration support; L3VNI (EVPN Type 5) gives VMs direct routed ingress from provider networks — no Kubernetes Services, no NAT.
- **How**: Declarative CRDs configure VTEPs (Underlay CRD with `vtepcidr`), MAC VRFs (L2VNI), and routing domains (L3VNI); FRR advertises Type 2 (MAC/IP) and Type 5 (prefix) routes. VMs attach via a bridge on the host defined with a standard `NetworkAttachmentDefinition`. A public demo repo and asciinema recording accompany the talk.
- **Where applicable**: Multi-cluster or multi-site KubeVirt estates needing VM mobility, legacy broadcast/multicast workloads, or direct fabric ingress into VMs. Requires an EVPN-capable underlay and OpenPERouter on each participating cluster — this is a design-patterns talk on top of the architecture session above.

### Building Cloud Infrastructure for AI

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/AEVDAU-building_cloud_infrastructure_for_ai/) · [Slides](https://fosdem.org/2026/events/attachments/AEVDAU-building_cloud_infrastructure_for_ai/slides/266874/cloud_inf_0cluewl.pdf) · [Recording](https://video.fosdem.org/2026/h2213/AEVDAU-building_cloud_infrastructure_for_ai.mp4)

Dave Hughes, Lukas Stockner (Stelia)

- **Why**: Most "GPU clouds" are really HPC clusters with a portal. This is a full-stack recipe for an actual elastic multi-tenant GPU cloud from open-source parts — including the parts vendors never discuss (PCIe P2P through the IOMMU, RDMA partitioning, firmware).
- **What**: An end-to-end architecture: standard OEM 8-way GPU servers, K8s used internally only (customer workloads run in containerized VMs for real isolation), ephemeral nodes imaged via mkosi + UEFI HTTP netboot, and a performance-focused storage split (local NVMe via SPDK at ~26 GB/s / 98% of raw throughput; Ceph for durable networked storage via virtio-fs/SPDK/Rook).
- **How**: Networking is the highlight: SONiC underlay with routing-to-host, VXLAN/EVPN overlays isolated in their own namespaces (cluster / public / per-tenant), and a custom SDN where endpoints announce prefixes via K8s CRDs that a daemon translates to BGP for hardware edge routers — IPv6-first public overlay, with per-instance port slices of a shared IPv4 address. RDMA: one NIC per GPU (3.6 Tbit/s, no sharing), InfiniBand partitioned via PKeys + GUID/VF assignment, or RoCE isolated at the switches. Virtualization: plain QEMU wrapper (KubeVirt rejected as integration-first rather than isolation-first), NUMA-local GPU/CPU selection, and PCIe topology modeled through QEMU — with the pitfall that IOMMU forces GPU-NIC P2P through the CPU root complex unless you use ATS on the NIC and ACS Direct Translation on the PLX.
- **Where applicable**: Anyone building or evaluating GPU cloud infrastructure. Explicitly not hyperscaler-specific — the entire point is reproducibility with open source — but it does assume you control the physical fleet and fabric.

### Going full IPv6 in Kubernetes: No limits, just 128 bits!

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/DGRKSQ-going-full-ipv6-in-kubernetes/) · [Slides](https://fosdem.org/2026/events/attachments/DGRKSQ-going-full-ipv6-in-kubernetes/slides/267075/ipv6_in_k_jakg2fw.pdf) · [Recording](https://video.fosdem.org/2026/h1302/DGRKSQ-going-full-ipv6-in-kubernetes.mp4)

Ole Mathias Heggem (Redpill Linpro)

- **Why**: IPv4 scarcity is now a cost line item (AWS public IPv4 charges, RIPE waiting list, CGNAT). IPv6-only Kubernetes with Cilium is newly practical, and this is a practitioner's account including the failure modes.
- **What**: The current state of K8s IPv6 (IPv6-only since 1.9, dual-stack GA since 1.23), a production IPv6-only deployment on Cilium, and the honest challenges: organizational readiness, apps/libraries that assume IPv4, managed services (LBs, storage, monitoring) that are IPv4-only, and lagging tooling.
- **How**: Concrete design choices — public prefix (requires ISP/cloud allocation and BGP to route to the cluster; per-node /64s from a pod /60; hardening via ACLs since pods are globally addressable) vs. ULA private prefixes (NAT66 or proxies for egress). Cilium 1.18 supports IPv6 underlay (example Helm/k3s config given: `ipam: kubernetes`, `ipv6.enabled`, `underlayProtocol: ipv6`, masquerade settings). IPv4-only services are reached via NAT64 + DNS64 or pull-through caches.
- **Where applicable**: Greenfield clusters, internal/server-facing estates, and anyone paying real money for IPv4. Client-facing services still need dual-stack; cloud provider maturity is mixed (Azure AKS uses NAT66). The numbers are operational guidance rather than benchmarks.

### Suricata 8 - shaping the future of network detection and prevention

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/YCYWGM-suricata/) · [Slides](https://fosdem.org/2026/events/attachments/YCYWGM-suricata/slides/266795/suricata8_4qjn5lu.pdf) · [Recording](https://video.fosdem.org/2026/h1302/YCYWGM-suricata.mp4)

Eric Leblond, Peter Manev (OISF / Stamus Networks)

- **Why**: Suricata 8 is two years of work (160K lines inserted) and materially changes what the engine can do — including two new deployment modes that signal where open-source network security is heading.
- **What**: Contributor-led overview of the release: 107 new rule keywords (a 38% increase, under the motto "if you log it, you can use it in a rule") for LDAP, MIME/email, DNS, SMTP, FTP, TLS, WebSocket, and DoH; transactional rules that match both stream directions in one signature (fixing a long-standing false-negative class); and datasets with JSON context so IoC matches carry attribution instead of bare values.
- **How**: New protocol decoders (WebSocket, LDAP, ARP, DoH/DoH2, SIP over TCP, SDP, POP3, mDNS); 27% of the codebase is now Rust (libhtp built-in and no longer a dependency, plus FTP, ENIP, MIME); Lua 5.4 vendored and sandboxed. Two structural additions: a **firewall** runmode (`suricata --firewall`, drop rules keyed on e.g. JA4 hashes — AWS reportedly runs it this way) and **Suricata-as-a-library**, where embedders bring their own packets/threads and register parsers, loggers, and keywords at runtime.
- **Where applicable**: NDR/IPS vendors, appliance builders, and any SOC running high-volume monitoring (100G is described as common, 400G on a single server as achievable). The library mode is the one to watch for product people — it changes the build-vs-embed calculus for detection engines.

### The Russian Censorship Circumvention, Tom's Traps, and Jerry's VPN: A 5-Year Journey

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/LJDUCD-rus-censorship-2026-fosdem/) · [Slides](https://fosdem.org/2026/events/attachments/LJDUCD-rus-censorship-2026-fosdem/slides/266923/fosdem-vp_0eoesvl.pdf) · [Recording](https://video.fosdem.org/2026/h1302/LJDUCD-rus-censorship-2026-fosdem.mp4)

Vitaly Repin

- **Why**: A rare first-hand, five-year longitudinal account of state-level DPI censorship versus a commercial VPN provider (150+ servers, millions of users) — and the speaker expects these techniques to spread to other states. Directly relevant to anyone thinking about protocol fingerprinting and traffic obfuscation defensively.
- **What**: The evolution of the "Great Russian Firewall": pre-2022 no VPN blocks → 2022–23 DNS/IP blocks → 2023 DPI blocking of standard VPN protocols (PPTP, L2TP, OpenVPN) → 2025 DPI detection of OpenVPN-with-XOR obfuscation within hours → 2025 white lists (only pre-approved IP/port traffic allowed). Non-technical pressure runs in parallel: app-store deplatforming, hosting bans, ad/payment cutoffs, and a 2024 law criminalizing VPN promotion.
- **How**: Detection mechanisms detailed: SNI-based blocking (with ECH declared illegal in Russia in Nov 2024), DNS/reputation-driven detection of VPN infrastructure (services like spur.us flagging IPs), and partial blocks (all ports except 443) that reveal the censor's confidence level. The speaker frames evasion as statistical hypothesis testing — the provider's goal is maximizing the censor's false-negative rate — and notes that user reports from "unimportant" regions are early-warning telemetry for new blocking capabilities being beta-tested.
- **Where applicable**: Censorship circumvention design, and more broadly any protocol that must resist adversarial traffic classification. The provider withheld current evasion methods, so this is a threat-model history, not a how-to.

### Credentials for Linux: Bringing Passkeys to the Linux desktop

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/838A8N-credentials-for-linux-bringing-passkeys-to-linux/) · [Slides](https://fosdem.org/2026/events/attachments/838A8N-credentials-for-linux-bringing-passkeys-to-linux/slides/267430/fosdem_ravbuub.pdf) · [Recording](https://video.fosdem.org/2026/h2214/838A8N-credentials-for-linux-bringing-passkeys-to-linux.mp4)

Alfie Fresta, Martin Sirringhaus

- **Why**: Windows, macOS, Android, and iOS all have platform FIDO2 APIs; Linux has none, leaving browsers and sandboxed apps with no standard way to do passkeys. This is the cross-desktop effort to fix it, with working code.
- **What**: Two components: `libwebauthn` (a Rust FIDO2/U2F platform library with pluggable transports — USB HID, BLE, NFC, and hybrid/QR "caBLE" all supported today, TPM 2.0 platform authenticator planned) and `credentialsd` (a D-Bus service and proposed XDG portal for credential management, with a reference UI, a Firefox web extension, a patched Flatpak Firefox build, and Fedora/openSUSE packages).
- **How**: The portal design separates frontend (protocols, devices, credential providers) from backend (trusted UX prompt owned by the desktop environment), request verification in portal style, and integration work is underway with xdg-desktop-portal (WIP PR) plus Chromium/Firefox/WebKit/Servo. The hard open problems are Linux-specific: origin scoping (how do you determine the requesting origin?) and app identity verification (Linux has no app signing keys, unlike Android/iOS), leading to a privileged-vs-unprivileged API split.
- **Where applicable**: Desktop Linux identity broadly — distro engineers, browser maintainers, and anyone whose passkey strategy must include Linux clients. Third-party credential providers (Bitwarden is among the contributors) are an explicit design goal.

### Keeping applications secure by evolving OAuth 2.0 and OpenID Connect

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/ZRDQYN-keep-applications-secure-by-evolving-oidc-oauth2/) · [Slides](https://fosdem.org/2026/events/attachments/ZRDQYN-keep-applications-secure-by-evolving-oidc-oauth2/slides/267300/keeping_a_pgafvua.pdf) · [Recording](https://video.fosdem.org/2026/h2214/ZRDQYN-keep-applications-secure-by-evolving-oidc-oauth2.mp4)

Alexander Schwartz (Keycloak maintainer)

- **Why**: OAuth 2.0/OIDC are being actively hardened — FAPI 2.0 (2025), RFC 9700 Best Current Practice, and the OAuth 2.1 draft — and this maps exactly what changes for real applications, with Keycloak as the enforcement vehicle.
- **What**: A standards-evolution walkthrough anchored in the FAPI 2.0 attacker models (what's assumed safe — TLS, JWKS, browsers, sessions — vs. what attackers can do), followed by the concrete practice set: PAR (pushed authorization requests) to keep flow parameters out of URLs, PKCE S256, private-key JWT (no public clients), no wildcard redirect URIs, and sender-constrained tokens.
- **How**: Deep, current treatment of DPoP (demonstrating proof-of-possession): ephemeral client key pairs bind access and refresh tokens so stolen tokens are unusable — including the HTTP method/URI/proof/nonce alignment that makes or breaks a DPoP request — and mTLS-bound tokens with their operational constraints. Keycloak implements all of this via client profiles/policies validated on client update, login, and token issuance (FAPI 2.0 and OAuth 2.1 draft both supported). Migration tactics are practical: enforce one practice at a time, then "brownouts" (temporary enforcement windows) to force cleanup before permanent cutoffs.
- **Where applicable**: Any IAM rollout — the migration playbook is vendor-neutral even where the demos are Keycloak. Especially relevant if you operate public clients or SPAs, where DPoP changes the threat model for token theft.

### The invisible key: Securing the new attack vector of OAuth tokens

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/DMVVQ9-securing-new-attack-vector-oauth-tokens/) · [Recording](https://video.fosdem.org/2026/ub5132/DMVVQ9-securing-new-attack-vector-oauth-tokens.mp4)

Gianluca Varisco

- **Why**: OAuth tokens have become the de facto target of choice for serious attackers — they bypass MFA by design and their usage is opaque to security monitoring. The PM's identity scope makes this the current-state threat talk.
- **What**: The OAuth token lifecycle as an attack surface, real-world attack vectors, and actionable protection strategies — grounded in the observed TTPs of groups like ShinyHunters and Scattered Spider, including the 2025 Salesforce intrusions.
- **How**: (From the program: lifecycle analysis of tokens from issuance through use, the monitoring blind spot created by opaque token activity, and defensive strategies for protecting issued tokens.)
- **Where applicable**: Broadly applicable to any organization issuing OAuth/OIDC tokens; pairs naturally with the previous talk's sender-constrained-token (DPoP/mTLS) remedies. (from abstract only — no slides or paper were available)

### Standardization and Open-source Implementation of Attested TLS for Confidential Computing

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/GHGFBM-attestedtls/) · [Slides](https://fosdem.org/2026/events/attachments/GHGFBM-attestedtls/slides/267432/20260201_60u9e0n.pdf) · [Recording](https://video.fosdem.org/2026/ud6215/GHGFBM-attestedtls.mp4)

Muhammad Usama Sardar (TU Dresden), peg (Peg Jones, Flashbots)

- **Why**: Attested TLS is becoming the identity primitive of confidential computing, and it's being standardized *right now* in the new IETF SEAT WG. This talk comes from the people driving it, with formal proofs of why the obvious designs are broken.
- **What**: A taxonomy of attested TLS — pre-handshake, intra-handshake, post-handshake attestation — plus formal-analysis results: replay attacks on pre-handshake attestation (including Intel's RA-TLS), diversion and relay attacks on intra-handshake designs (one shown to break Cocos AI), leading to a post-handshake candidate draft built on exported authenticators (RFC 9261) with a `cmw_attestation` extension carrying RATS evidence in the Certificate message.
- **How**: The WiP implementation is Rustls-based, transport-agnostic (QUIC included, tested with Intel TDX), supports one-way and mutual attestation, and supports both the RATS "passport" and "background check" models. Notable engineering friction: Rustls deliberately doesn't expose handshake internals, and there's essentially one partial open-source reference for exported authenticators — so they implemented it from scratch.
- **Where applicable**: Server-to-server attested channels where you control both ends (Flashbots uses a similar protocol for TEE-based Ethereum block building), and proxies that terminate attestation for naive clients. Explicitly not yet: browsers (APIs don't expose TLS keying material) or paths through TLS-terminating proxies — many deployments paper over this with nested encryption.

### SSH logins in practice: certificates vs. OPKSSH

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/ST9D39-ssh-logins-cert-vs-opkssh/) · [Slides](https://fosdem.org/2026/events/attachments/ST9D39-ssh-logins-cert-vs-opkssh/slides/267594/fosdem26_4nsj85m.pdf) · [Recording](https://video.fosdem.org/2026/h2214/ST9D39-ssh-logins-cert-vs-opkssh.mp4)

Erich Birngruber

- **Why**: SSH access at scale with unmanaged clients is an identity problem most enterprises have and few solve well — private keys on unmanaged endpoints, server-side key sprawl, awkward MFA. This is a hands-on comparison of the two leading answers from a real multi-user cluster evaluation.
- **What**: OpenSSH certificates versus OpenPubKey/OPKSSH, evaluated for a compute cluster of dozens of machines and hundreds of unmanaged clients, with live demos of both from client and server perspectives (lab environment: Kanidm as IDM/OAuth provider, step-ca as CA).
- **How**: Both deliver short-lived credentials via an OAuth flow. Certificates add host validation and stay within core SSH features (forwarding, agent control), but require CA setup and lifecycle. OPKSSH offers highly customizable policies (including claims-based) and works with multiple existing IdPs, but does not cover host verification — you need a third-party tool beyond the SSH client for that.
- **Where applicable**: Any multi-user SSH estate, HPC clusters, and organizations wanting OAuth-bound short-lived SSH access. The comparison table is a useful decision matrix if you're weighing these two today.

## Adjacent

### Path Safety in the Trenches

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/H39QZD-path_safety_in_the_trenches/) · [Slides](https://fosdem.org/2026/events/attachments/H39QZD-path_safety_in_the_trenches/slides/266828/path-safe_nqr2ibp.pdf) · [Recording](https://video.fosdem.org/2026/ua2118/H39QZD-path_safety_in_the_trenches.mp4)

Aleksa Sarai (runc maintainer, cyphar)

- **Why**: The most bang-for-the-buck container runtime exploits for a decade have been filesystem confused-deputy attacks, including the November 2025 runc CVEs. This is the definitive taxonomy and the state of kernel-side fixes.
- **What**: A walkthrough of "regular" path safety (TOCTOU on path components) versus "strict" path safety (exact-path requirements for procfs, magic links, and overmounts), cataloguing ~15 years of CVEs, and the migration of runc's codebase to a path-safe, file-descriptor-centric design.
- **How**: The kernel primitives are `openat2(2)` with `RESOLVE_IN_ROOT`/`RESOLVE_BENEATH`/`RESOLVE_NO_SYMLINKS`, plus the new mount API (`fsopen`/`fsmount`/`open_tree`) to create a private, validated procfs. `libpathrs` (Rust with C/Go/Python bindings) packages it all. The November 2025 CVEs (CVE-2025-31133, CVE-2025-52565, CVE-2025-52881) are dissected concretely: racing a bind-mount source swap to turn `/volume` into a writable bind of `/proc/sys/kernel/core_pattern`, and chained mounts faking `/proc/.../attr/apparmor` paths.
- **Where applicable**: Container runtime and daemon authors, and honestly any privileged Unix program that operates on paths. Also a candid threat-model discussion: runc has no formal threat model, and most of these bugs live in the "misconfiguration" gray zone.

### Demystifying Post-Quantum Cryptography: The Hybrid Approach

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/8MEPV3-demystifying_post-quantum_cryptography/) · [Slides](https://fosdem.org/2026/events/attachments/8MEPV3-demystifying_post-quantum_cryptography/slides/266703/pqc_fosde_kqchfmr.pdf) · [Recording](https://video.fosdem.org/2026/ub5132/8MEPV3-demystifying_post-quantum_cryptography.mp4)

Rutvik Kshirsagar, Shreyas Mahangade, Clemens Lang (Red Hat)

- **Why**: PQC migration is shifting from "someday" to procurement requirements, and hybrid classical+PQC is the only deployment path that doesn't break interoperability. This is the practical migration talk with a live TLS demo.
- **What**: The hybrid transition using NIST's standardized algorithms — ML-KEM (FIPS 203) for key exchange, ML-DSA (FIPS 204) and SLH-DSA (FIPS 205) for signatures — where hybrid applies only to the key exchange (X25519MLKEM768), keeping TLS 1.3's cipher-suite agility intact, plus PQC signatures for software supply chain (hybrid EdDSA/ML-DSA OpenPGP signing of RPMs via Sequoia).
- **How**: Deployment math: time-to-transition (standards → vendor support → upgrades → decommissioning) must be shorter than the time data must remain secret — hence harvest-now-decrypt-later concern. Momentum numbers: ~60% of Cloudflare's human TLS traffic already negotiates hybrid ML-KEM, Chrome 116+ by default, OpenSSL 3.5+ native support, Fedora 43, IBM z16 firmware.
- **Where applicable**: Any TLS-terminating service, PKI, or signing pipeline with long-lived artifacts (firmware, root certs, package signing). The guidance on ML-KEM/ML-DSA variant selection (fast handshakes vs. long-term margins) is directly usable.

### BPF Tokens in Linux Distributions: A Path to Safe User-Space eBPF

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/3LLHG9-bpf-tokens-safe-userspace-ebpf/) · [Recording](https://video.fosdem.org/2026/h1308/3LLHG9-bpf-tokens-safe-userspace-ebpf.mp4)

Daniel Mellado

- **Why**: eBPF's privileged-by-default model has blocked unprivileged-but-legitimate uses (observability agents, service meshes) in containers and distros for years; BPF tokens are the kernel's new delegation mechanism, and this is about how distributions adopt them.
- **What**: An explanation of BPF tokens as a kernel mechanism for delegating restricted eBPF privileges to unprivileged processes, plus how distros (Fedora is the example) can package token policies to give users tracing/observability/networking tools without root or `CAP_SYS_ADMIN`.
- **How**: (From the abstract: walkthrough of real token policies, the delegation model, and the implications for developer workflows, container runtimes, and system services in Fedora and other distros.)
- **Where applicable**: Distro and platform teams designing safe eBPF access for non-root users; relevant to anyone running eBPF-based networking in multi-tenant or least-privilege environments. (from abstract only — no slides available)

### Lima v2.0: expanding the focus to hardening AI

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/RGCTDY-lima/) · [Slides](https://fosdem.org/2026/events/attachments/RGCTDY-lima/slides/266976/lima_yjbsxrd.pdf) · [Recording](https://video.fosdem.org/2026/h2213/RGCTDY-lima.mp4)

Akihiro Suda (NTT)

- **Why**: Interesting signal for agentic-workload isolation: Lima (now a CNCF incubating project) repositioned around sandboxing AI coding agents in VMs — a stronger boundary than the deprecated `sandbox-exec` approaches agents ship with.
- **What**: Lima v2.0 (Nov 2025): plugin infrastructure (VM driver, CLI, URL-schema plugins), GPU acceleration via the krunkit driver (virtio-GPU → MoltenVK/Metal on Apple silicon, e.g. for llama.cpp), an MCP server exposing sandboxed tools (`list_directory`, `read_file`, `run_shell_command`) to host-side agents, and CLI improvements.
- **How**: Agents run inside the VM with only the working directory mounted read-write; alternatively host-side agents connect through Lima's MCP server, whose tools are strongly sandboxed by the VM boundary. v2.1 (ETA March 2026) adds "sync mode": synced directories are written back only after explicit user confirmation, preventing "Sorry I removed everything including .git dir" incidents.
- **Where applicable**: Developer-workstation AI-agent isolation. It's a VM-per-agent hammer, not a production workload-identity answer — but the MCP-server pattern (sandboxed tool exposure to agents) is a model worth watching for anyone working on agentic identity and access.

## Wildcard

### A Toolset for the Internet of Threads (IoTh): Fine-Grained IPv6 Networking in User Space

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/T8YMSX-a_toolset_for_the_internet_of_threads_ioth_fine-grained_ipv6_networking_in_user_/) · [Slides](https://fosdem.org/2026/events/attachments/T8YMSX-a_toolset_for_the_internet_of_threads_ioth_fine-grained_ipv6_networking_in_user_/slides/267109/ioth_tool_old4dff.pdf)

Renzo Davoli

- **Why**: A genuinely novel networking model: instead of containers or VMs, assign full IPv6 identities — addresses, routing, protocol stacks — to individual processes or threads, using user-space TCP/IP stacks. Not on any roadmap you'd be reading, but it reframes what "identity" means at the network layer.
- **What**: A complete toolchain: `libioth` (pluggable user-space stack framework with a Berkeley-sockets API where the stack is chosen at runtime — stacks include vdestack, which recycles the kernel TCP/IP stack via a dedicated netns thread + TUN/TAP, a picoTCP-ng-based stack, and a lwIP proof of concept), netlink configuration libraries (`libnlq`, and `nlinline` implemented entirely in a header file), one-string stack configuration (`iothconf`: `"stack=vdestack,vnl=...,eth,dhcp"`), plus DNS tooling.
- **How**: The DNS layer is the interesting part: hash-based IPv6 addressing (names deterministically hash to addresses within a prefix, with reverse DNS), OTIP one-time IPv6 addresses for privacy, and `namedhcp`, a DHCPv6 server that assigns addresses by looking up the node's FQDN in DNS — so a node's identity is its name, and addressing follows.
- **Where applicable**: Experimental/research; useful today for sandboxed per-service networking, testing, and VDE-based virtual labs. The FQDN-as-address-source idea and the netlink-configuration libraries are the transferable bits.

### Open Source Security in spite of AI

**Links:** [Abstract](https://fosdem.org/2026/schedule/event/B7YKQ7-oss-in-spite-of-ai/) · [Recording](https://video.fosdem.org/2026/janson/B7YKQ7-oss-in-spite-of-ai.mp4)

Daniel Stenberg (curl)

- **Why**: Not a core-interest topic, but a field-level signal you wouldn't search for: the maintainer of curl describing how AI is simultaneously degrading and improving open-source security work.
- **What**: Two-sided evidence from one project: large volumes of low-quality AI-generated "security reports" acting as a denial-of-service on maintainers (plausible-looking rubbish that must be triaged), alongside genuinely new AI-powered code analysis finding real flaws in curl in ways no previous analyzer could — some findings "feels almost human."
- **How**: (From the abstract: concrete examples of both the slop reports and the AI-found bugs, named tools, and the operational impact on a small maintainer team.)
- **Where applicable**: Every open-source project your supply chain depends on — if you run a security or PSIRT function, expect report volume to keep climbing while triage cost shifts to you. (from abstract only — no slides available)

## Themes

- **eBPF is hitting its scaling limits, and the community is engineering around them**: RDMATracer's static-analysis probe pruning, reachability analysis to fix verifier map-refcount waste, BPF tokens for safe unprivileged loading, FLASH extending AF_XDP beyond its socket semantics, and Cloudflare's three-year metadata saga — all are responses to eBPF/kernel primitives not quite meeting production needs.
- **VPP/FD.io is positioning itself as the 400G/800G open datapath**: hardware TM offload with a vendor-neutral API, IPsec with measured 70 Gbps/tunnel and 41x memory scaling tricks, plus its appearance inside the Stelia GPU-cloud stack. The project is visibly courting telco *and* datacenter workloads.
- **EVPN/BGP is bleeding into Kubernetes**: OpenPERouter (twice), GoBGP's multi-tenant control plane, Cilium IPv6 underlay, and the Stelia SONiC/VXLAN-EVPN design all converge on the same idea — the fabric's control plane terminating on (or near) the nodes, declaratively configured, with dumber leaves.
- **AI training economics are driving infrastructure decisions**: three talks center RDMA (RTRS as an abstraction, RDMATracer for failure cost — 32K+ wasted GPU-hours, Stelia for full-stack GPU cloud design), and Lima's repositioning toward AI-agent sandboxing shows the pull extending down to the laptop.
- **Identity is converging on tokens, attestation, and platform authenticators**: OAuth token theft TTPs vs. FAPI 2.0/DPoP sender-constrained tokens, passkeys finally reaching the Linux desktop via portal APIs, SSH access adopting OAuth flows, and attested TLS entering IETF standardization with formal proofs — a coherent story about binding credentials to something stronger than possession.
- **The adversarial internet is intensifying on two fronts**: state censorship is now DPI-driven, statistical, and escalating to white lists (with the Russian playbook expected to spread), while PQC migration deadlines are already written into procurement — both forcing protocol design to assume sophisticated traffic analysis.
