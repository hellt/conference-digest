<!--
conference: Open vSwitch and OVN 2026 Fall Conference
source_url: https://www.openvswitch.org/support/ovscon2026/
generated: 2026-11-09
registry_key: ovscon-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Open vSwitch and OVN 2026 Fall Conference

User-Defined Networks (UDNs) dominated this year's program: now that per-tenant virtual networks have landed in OVN-Kubernetes, the community spent 2026 discovering everything that breaks at 100s–1000s of networks — ARP fan-out, conntrack interactions, control-plane recompute costs. Alongside that, a second thread runs through the program: federating independent OVN domains (multi-cluster, VM+K8s, multi-AZ VPC peering) via OVN Interconnect, and a third: OVS reworking itself for a hardware-offloaded, Rust- and AI-adjacent future. Note: no paper or slide links were available for any item at time of writing; every write-up below is grounded in the conference abstracts only.

## Core

### Lost in the Layers - Scaling OVN-Kubernetes User-Defined Networks from K8S API to the kernel

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t27)

Patryk Diak, Red Hat, LLC.; Dumitru Ceara, Red Hat, LLC.

- **Why**: The canonical modern debugging story — a scaling problem that turned out to be distributed across every layer of the stack. This is exactly the kind of full-stack triage (K8s API → OVN NB/SB → OVS flows → kernel) the PM's world runs on, and the "telemetry we wish we'd had" is directly reusable.
- **What**: A postmortem-style account of scaling OVN-Kubernetes UDN workloads in which every layer contributed a small failure, and all of them had to be fixed before any improvement was visible. The core finding: most engineering time went to localizing the failing layer, not to fixing it. (from abstract only)
- **How**: Systematic per-layer bisection from the Kubernetes API server down to the kernel, with a retrospective on the observability gaps that made attribution slow.
- **Where applicable**: General to any OVN-Kubernetes deployment pushing UDN density; the telemetry recommendations transfer to any layered CNI debugging. Not tied to a particular operator's scale, though the pain obviously grows with network count.

### From User Defined Networks to EVPN: Scaling OVN-Kubernetes

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t2)

Mohit Sheth; Venkata Anil Kommaddi; Joe Talerico, Red Hat, LLC.

- **Why**: Firmly substantiated scale methodology, not anecdotes: OpenShift PerfScale built repeatable kube-burner workloads for UDN/CUDN density, BGP advertisement, and EVPN connectivity, and reports the bottlenecks found (OVN NB/SB, OVS) and what actually moved the needle.
- **What**: A testbed and workload-model description covering L2/L3 UDN and ClusterUDN density, churn, BGP route advertisements, and EVPN east-west/north-south connectivity — spanning 100s of CUDNs and 1000s of namespaces/pods/VMs — plus the concrete improvements that increased achievable scale and a repeatable methodology for measuring tenant networking at scale. (from abstract only)
- **How**: Multi-node testbeds with external FRR peers, VTEPs, VRFs and pod/VM traffic endpoints; kube-burner-driven density and churn workloads; measurement of CUDN allocation latency, pod-readiness latency, OVN NB/SB and OVS bottlenecks, and BGP import/export timing.
- **Where applicable**: The methodology is upstream and repeatable; the specific bottlenecks are OVN-Kubernetes/Red Hat-stack-specific but the measurement pattern transfers to any tenant-networking platform.

### One Tunnel Too Many: No-Overlay Mode in OVN-Kubernetes

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t4)

Riccardo Ravaioli, NVIDIA

- **Why**: Directly hits the PM's BGP + datapath interests. When the fabric already provides an overlay, stacking Geneve on top wastes MTU and adds encapsulation cost — this is OVN-Kubernetes learning to be fabric-aware.
- **What**: A new no-overlay mode letting the cluster default network and primary L3 ClusterUserDefinedNetworks route inter-node traffic via BGP-learned routes with no Geneve encapsulation, while OVN still handles local networking, policy, and Services. Per-network choice, so Geneve and no-overlay networks coexist in one cluster. (from abstract only)
- **How**: BGP-learned routes replace the tunnel for inter-node forwarding (administrator-configured BGP or a managed full-mesh option); the talk follows a packet across nodes and covers the config choices that matter — outbound SNAT, MTU, tenant isolation. NVIDIA's DPU-based VM networking is one concrete example.
- **Where applicable**: Clusters sitting on a fabric that already provides the overlay/underlay (typical DPU- or ToR-terminated environments). Joint Red Hat/NVIDIA effort; constraints around primary L3 networks and SNAT shape deployment.

### A Switch, a Load Balancer, and an ACL Walk into a Pipeline…. And Conntrack Ruins Everything

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t10)

Surya Seetharaman, Red Hat, LLC.; Nadia Pinaeva, NVIDIA

- **Why**: UDN isolation is not the end state — address-space exhaustion and inter-team service access require controlled connectivity between tenant islands. This is the API (ClusterNetworkConnect in ovn-k v1.3) doing that, plus a genuinely instructive conntrack/ACL evaluation-order puzzle.
- **What**: ClusterNetworkConnect, a declarative admin API connecting isolated UDNs with full pod-to-pod, service-only, or both; symmetric but non-transitive connectivity. Plus the war story of how load balancers on switches interact with conntrack and ACL evaluation order to break the "allow service, drop pod-to-pod" intent, the shipped workaround, and why the long-term fix is hard. (from abstract only)
- **How**: A distributed transit router peers with each connected network's router via point-to-point subnets carved deterministically from a user-configured CIDR; load balancers are placed on connected networks' switches so cross-network DNAT works with existing routing.
- **Where applicable**: OVN-Kubernetes v1.3+ with UDNs; the conntrack/ACL ordering lesson applies to anyone designing stateful policy over OVN load balancers generally.

### A Unified Networking Fabric for VMs and Multi-Cluster Kubernetes workloads

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t12)

Sragdhara Datta Chaudhuri, Nutanix; Priyankar Jain, Nutanix

- **Why**: Multi-cluster K8s + VMs in one VPC with local control planes is the shape of most real hybrid estates. This is a working architecture ("interconnect of interconnects") rather than a proposal, built from OVN-IC primitives a PM could reproduce.
- **What**: Nutanix Flow CNI, built on OVN-Kubernetes and OVN-IC, extends the VPC model across VM and multi-cluster Kubernetes environments: shared logical routing domain, bi-directional federated service reachability (VM VIPs ↔ K8s ClusterIPs), and cross-cluster DNS for ClusterIP services — all while each environment keeps its own control plane. (from abstract only)
- **How**: Hierarchical OVN connectivity — OVN-Kubernetes Interconnect mode distributes control/datapath state within a cluster; OVN-IC links independent OVN domains via transit switches and a shared interconnect DB. Backend selection stays local to the destination domain. A controller publishes service FQDNs/ClusterIPs to a shared OVSDB and a CoreDNS extension builds per-VPC views on the `svc.cluster.local` model.
- **Where applicable**: The architecture is Nutanix Flow CNI-specific in its packaging, but the federation pattern (independent OVN domains, exchanged routes/VIPs, shared OVSDB for service discovery) is general to any OVN-IC-based multi-cluster fabric.

### How we are scaling Crusoe cloud using OVN interconnect approach

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t15)

Numan Siddique, Crusoe; Ketan Supanekar, Crusoe

- **Why**: Crusoe is an AI-cloud operator re-architecting its OVN control plane — and it's led by Numan Siddique, OVN's longtime maintainer. A production AI-cloud at the point where the central Southbound DB becomes the bottleneck is a rare, candid data point.
- **What**: The current OVN-relay architecture and its bottlenecks, a re-architecture modeled on OVN-Kubernetes Interconnect, and an evaluation of control-plane backing stores — k8s api-server/etcd with custom CRDs vs. NATS KV — with the chosen option and rationale. The talk explicitly asks the community whether the central OVN SB DB can be replaced by api-server/etcd or NATS KV. (from abstract only)
- **How**: Moving from relayed central OVSDB to the ovn-kubernetes-style Interconnect decomposition (per-zone local state, IC database at the top), and re-homing control-plane persistence on a different storage substrate.
- **Where applicable**: Crusoe-specific production constraints, but the SB-DB bottleneck and the storage-backend question generalize to any large single-tenant-scale OVN cloud. Watch for whether the community adopts the experimental backend.

### Route scope delimitation as a control plane scalability mechanism for OVN Interconnect using route tags

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t9)

Lucas Vargas Dias, Magalu Cloud; Julio Cesar Vanti, Magalu Cloud

- **Why**: One of the few talks with a hard quantified result: topological isolation (per-peering transit switch) costs **2.56x** the Southbound logical flows of tag-based route scoping for identical connectivity. That's a real, transferable design trade-off for anyone building multi-AZ VPC peering on OVN-IC.
- **What**: A comparison of two ways to bound route exchange between peered VPCs in OVN Interconnect: a transit switch per peering (data-plane isolation, expensive) vs. one shared transit switch with declarative scoping via `ic-route-tag` / `ic-route-learn-tag-rules` / `ic-route-filter-tag` (control-plane isolation, substantially cheaper in memory, in northd full-recompute latency, in flow installation after reconnect, and in every unrelated NB write). The trade-off is stated plainly: tag scoping constrains route learning only; a manual static route can still cross the shared L2 domain, so per-pair topology remains necessary where data-plane isolation must hold. (from abstract only)
- **How**: Measurement-driven comparison of lflow-node recomputes, flow counts, and operation latency between the two topologies on identical connectivity.
- **Where applicable**: Any OVN-IC VPC-peering deployment; the technique is upstream OVN configuration (general), the numbers come from Magalu Cloud's production-derived testing. Isolation requirements (control-plane-only vs. data-plane) decide which option is valid.

### One Shared Gateway, a Thousand Routers: Scaling ARP/NDP in OVN-Kubernetes

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t11)

Jaime Caamano, Red Hat, LLC.; Matteo Dallaglio, Red Hat, LLC.; Tim Rozet, NVIDIA

- **Why**: A beautiful datapath pathology: with hundreds/thousands of UDNs sharing one uplink/IP/MAC, ARP replies can't be mapped back to their originating router (conntrack can't track them), so OVN-Kubernetes fans them out to every patch port — duplicating neighbor state, ballooning the OpenFlow footprint, and eventually exceeding OVS recirculation limits. This is exactly the "K8s networking meets datapath internals" intersection.
- **What**: The full arc of an ARP storm at UDN scale: how fan-out surfaced, the constraints any fix must preserve, a short-term flow fix constraining fan-out on the shared gateway bridge, a mid-term prototype steering discovery through the default gateway router, and the resulting upstream OVN feature — Shared MAC-binding scopes, letting related logical router ports share one set of learned neighbor bindings instead of per-router duplication. (from abstract only)
- **How**: Learn through a single gateway router and steer ARP/NDP to it, propagating learned bindings to the UDNs, rather than fanning discovery traffic to every gateway router.
- **Where applicable**: OVN-Kubernetes shared-gateway deployments at high UDN count; the Shared MAC-binding scope is a general OVN feature usable beyond ovn-k. Red Hat/NVIDIA collaboration shaping the fix at the right layer.

### Two OVN-Kubernetes, One DPU

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t14)

Alin Serdean, NVIDIA; Igal Tsoiref, Red Hat, LLC.

- **Why**: DPU-mode ovn-kubernetes today serves only the host cluster — pods scheduled on the DPU's own node get nothing. Running two full ovn-k instances on one card, sharing only what must be shared, is a concrete step toward DPUs as first-class compute, which matters for accelerator-adjacent infrastructure.
- **What**: A proposal and working prototype for a second, full-mode ovn-kubernetes instance on the same DPU, each instance keeping its own OVN databases and Kubernetes API, with the genuinely shared resources carefully partitioned. Built on co-hosted ovn-controller (experimental since 23.03, untagged in 26.09.0). (from abstract only)
- **How**: The enumerated hard parts: `system-id` as the one key that can't be chassis-specific, conntrack zones staying clear of shared gateway zones, 15-character management-port name limits, two instances can't share a gateway bridge (ovnk owns its whole flow table), and ownership assignment for bridges, nftables tables, metrics ports and socket paths. Prototype demo; PRs referenced.
- **Where applicable**: DPU-accelerated Kubernetes (NVIDIA BlueField-class cards, Red Hat + NVIDIA joint work). The resource-partitioning lessons generalize to any two network stacks sharing one host.

### ovn-local: A new proposed architecture for OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t26)

Mark Michelson; Ilya Maximets; Dumitru Ceara; Ales Musil, Red Hat, LLC.

- **Why**: A panel proposing to re-architect OVN itself — fewer processes, fewer databases — because a decade of feature growth and changed deployment patterns (smaller, more distributed footprints à la ovn-k IC) has left the original centralized architecture a poor fit. Architecture-level signals like this are rare and worth a PM's attention.
- **What**: A proposal for a leaner OVN deployment model with a smaller footprint, promising easier deployment and upgrades, faster processing, and reduced memory and disk requirements. (from abstract only)
- **How**: Consolidating the process/database structure of OVN (details are the panel's subject); positioned as the direction future OVN releases will take.
- **Where applicable**: Every OVN deployment if it lands — this is upstream-project direction-setting by the core maintainers, not an operator-specific design. Watch this one for the following release cycle.

### Upgrading network control plane and ovs-vswitchd with kernel datapath without impacting users

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t6)

Aleksandr Ankudinov, Nebius

- **Why**: Live-upgrading the network data plane of a large public cloud without user-visible impact is one of the hardest ops problems in the field. Nebius shares the actual tricks — including running two ovs-vswitchd in parallel, "doing the forbidden" — which is gold for anyone operating OVS-based infrastructure in Kubernetes.
- **What**: Techniques for restarting/replacing the three components (vpc-agent, ovs-vswitchd, OVS kernel module) while existing flows keep traffic flowing: flow cookies as version tags for cleanup, OpenFlow `note` actions as cross-restart storage, disciplined group-ID allocation, and the parallel-vswitchd upgrade dance with `flow-restore-wait` — including how to make two daemons fight and how to make them stop. Plus the Kubernetes-specific oddities, and a theoretical scheme for loading two OVS kernel modules at once. (from abstract only)
- **How**: Desired-state reconciliation over versioned flows, plus dual-daemon handover during upgrade; kernel module itself is not hot-upgraded today.
- **Where applicable**: Nebius public-cloud specifics (kernel datapath, agent-based control), but the versioning/reconciliation patterns apply to any OVS/OpenFlow deployment. The parallel-daemon scheme carries real risk — treat as inspiration, not recipe.

### Targeted Megaflow Revalidation in Open vSwitch

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t28)

Gaetan Rivet, NVIDIA

- **Why**: A diagnosed failure mode that "has limited the scale of our Open vSwitch deployments at NVIDIA": after any configuration change, OVS revalidates *all* megaflows, which can cascade into flow eviction, revalidator destabilization, and megaflow population collapse — a rebuild under overload. A concrete fix with a dependency-tracking design, implemented and running in production fork form.
- **What**: Targeted megaflow revalidation, implemented in the OVS-DOCA fork: record the reason for each revalidation and extend xcache to track each megaflow's dependencies, so only affected megaflows are retranslated after a change. Also gives controller authors a way to structure OpenFlow pipelines so configuration changes have bounded impact; upstreaming is intended. (from abstract only)
- **How**: Dependency tracking including indirect and negative dependencies (watched ports, missing groups), with AI-assisted testing used to cover the dependency matrix; part of a wider revalidation-stabilization effort that continues with a better flow-capacity control law.
- **Where applicable**: Any large OVS deployment, but the current implementation lives in NVIDIA's OVS-DOCA fork (DOCA/BlueField context) — upstream availability is the thing to watch. The dependency-completeness caveat is the main risk.

### Teaching AI to Debug OVN: Layer-Aware Troubleshooting with the ovn-kubernetes MCP Server

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t8)

Keshav Kabra, NVIDIA; Surya Seetharaman, Red Hat, LLC.

- **Why**: Sits squarely on the PM's AI-for-infrastructure interest: a community MCP server that exposes OVN/OVS/K8s/kernel layers to AI agents as structured tools, with an honest accounting of where AI triage helps and where humans still must check.
- **What**: The ovn-kubernetes MCP server: read-only, structured tools wrapping ovn-nbctl, ovn-sbctl, ovn-trace, ovs-ofctl, ovs-appctl plus Kubernetes and kernel-networking state — working on live clusters and offline on must-gather/sos-report artifacts. Includes a demo of an agent tracing a symptom from pod to logical/physical datapath to root cause. (from abstract only)
- **How**: Deliberate design choices: wrapper tools rather than generic exec, least-privilege access, tools grouped by network layer — a reusable pattern for exposing infrastructure primitives to LLM agents safely.
- **Where applicable**: General to OVN-Kubernetes clusters today; the MCP-wrapping pattern transfers to any layered system. Triage-assist, not autonomous repair.

## Adjacent

### Stateless Load Balancing in OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t24)

Alexandra Rukomoinikova, K2 Cloud

- **Why**: Horizontal gateway scaling is blocked by conntrack pinning every connection to one gateway chassis. Rather than sync conntrack (the usual answer), this moves the NAT to the backend's hypervisor — a different architectural point in the design space, in production at a cloud provider.
- **What**: The story of the new "deferred-nat" load balancer option: backend selected statelessly per packet on the router, packet delivered by MAC, DNAT and conntrack state created on the backend's own hypervisor; established sessions survive backend changes via incremental select-group updates instead of rebuilds. Includes why conntrack synchronization, extending `use_stateless_nat`, and cross-AZ backends were rejected. (from abstract only)
- **How**: NAT deferred to the backend hypervisor, eliminating per-gateway conntrack state as the horizontal-scaling bottleneck.
- **Where applicable**: OVN deployments needing horizontally scalable load-balancer gateways (public/private cloud). K2 Cloud runs it in production; work remains (per the speakers). Requires OVN support for the deferred-nat option.

### Death by Kernel locks: Hyperscalers road to DPDK

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t18)

Florian Werner, Schwarz Digits; Felix Huettner, Schwarz Digits

- **Why**: Kernel-lock contention is the classic reason large OVN gateway deployments give up on netlink/kernel bridges. This is a full-fleet migration to DPDK bridges with pitfalls and before/after performance comparisons — a decision many operators are facing with the same data.
- **What**: The migration of all Schwarz Digits OVN gateway chassis from kernel netlink bridges to DPDK bridges: motivations (kernel-lock pathologies), migration pitfalls, and performance comparisons between the two. (from abstract only)
- **How**: Fleet-wide bridge-type migration on OVN gateway chassis; pairs with the follow-up `dpdk conntrack performance` talk on the conntrack problems they found.
- **Where applicable**: Schwarz Digits' environment (their silicon, their workloads) — treat the direction and pitfalls as transferable, the numbers as org-specific. Relevant wherever kernel-datapath scaling limits bite.

### Ovens, freezers, and radiofrequency cavities: The ongoing migration of the CERN Cloud to OVN

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t25)

Christopher Barnes, CERN; Richard Bachmann, CERN

- **Why**: A 1.4k-hypervisor, 15k-VM private OpenStack cloud migrating LinuxBridge → OVN across two datacenters is a serious private-cloud migration at research-lab scale — squarely the PM's virtualization/private-cloud territory, told with open questions rather than a victory lap.
- **What**: Mid-migration experience report: deployment adjustments made along the way, issues encountered, and open questions the CERN team wants community input on. (from abstract only)
- **How**: Incremental migration of a two-datacenter OpenStack cloud from LinuxBridge networking to OVN.
- **Where applicable**: OpenStack-based private clouds; CERN's scale and two-site layout are specific, but the LinuxBridge→OVN migration playbook is broadly reusable.

### One API to Rule Them All: Reworking the OVS Hardware Offload Layers

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t22)

Eelco Chaudron, Red Hat, LLC.

- **Why**: Offload in OVS was historically duplicated per provider (kernel TC flower vs. DPDK rte_flow via netdev-offload), making vendor integration invasive. The new `dpif-offload` API layer that has landed upstream unifies this — foundational plumbing for every DPU/SmartNIC story elsewhere in the program.
- **What**: The dpif-offload API layer now in OVS: a unified abstraction for hardware offload sitting above provider implementations, centralizing offload handling, simplifying vendor integration, and reducing duplicated logic — plus the migration story from the old netdev-offload model and what it enables next. (from abstract only)
- **How**: A single offload API above provider-specific implementations (kernel TC flower and DPDK rte_flow behind it), so new offload features land in one place instead of N.
- **Where applicable**: Anyone building or consuming OVS hardware offload (TC flower, DPDK rte_flow, DOCA-style providers); landed upstream, so this is the new baseline architecture rather than a fork.

### Conntrack: Semantics and Scale

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t23)

Aaron Conole, Red Hat, LLC.

- **Why**: Conntrack quietly became the L3/L4 interface of the OpenFlow pipeline, and this year's program shows it breaking things in at least three other talks (ACL ordering, ARP tracking, DPDK performance). This is the framing talk on what conntrack must guarantee across implementations and how it scales — including hardware acceleration paths.
- **What**: A decade-look at conntrack in OVS and the open questions: which behaviors must be common across all conntrack implementations, how the userspace implementation scales to modern demands, and how `ct()` can be extended through a hardware acceleration path — with what is done, what remains unmerged, and how to contribute. (from abstract only)
- **How**: Retrospective plus forward-looking work items on common semantics, userspace scaling, and hardware `ct()` acceleration.
- **Where applicable**: All of OVS/OVN — conntrack semantics constrain every stateful feature above them. Particularly relevant to userspace/DPDK and offload users.

## Wildcard

### Rebuilding an OpenFlow Controller in Rust

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t17)

Or Mazza, NVIDIA; Quentin Barrand, NVIDIA; Alin Serdean, NVIDIA

- **Why**: Not a networking-technique talk but a direction signal: a C→Rust rewrite of a production OpenFlow controller (HBN on BlueField) with binary compatibility preserved and *measured* gains — 8% faster insertion, 14% faster deletion, 57% faster flow-statistics collection — plus an explicit debate about rewriting parts of OVS itself in Rust.
- **What**: The HBN controller rewrite from C to Rust for memory safety, concurrency, and testability, delivered without disrupting users, with the above performance numbers and practical lessons from running it in a real DPU platform. The speakers open the question of where Rust fits in OVS proper and what C bindings would be required. (from abstract only)
- **How**: Incremental Rust introduction behind a binary-compatible interface; measurable before/after flow-operation benchmarks.
- **Where applicable**: The results are HBN/BlueField-specific; the rewrite pattern and the OVS-in-Rust debate generalize to the whole project — which is why it's worth a PM's attention even beyond the immediate platform.

### 99 Patches, but Reviews Ain't One

**Links:** [Abstract](https://www.openvswitch.org/support/ovscon2026/#t16)

Eelco Chaudron, Red Hat, LLC.

- **Why**: Not about networking at all — about the OVS project's review bottleneck, with numbers on review workload and where patches stall. For anyone whose product depends on OVS/OVN landing features (and whose teams could review), this is the health-of-the-substrate talk.
- **What**: A patch's journey from ovs-dev to merge, an honest look at who actually reviews, numbers on current review workload and bottlenecks, and the case that community review is essential to merge speed and knowledge spread. (from abstract only)
- **How**: Lightning-talk analysis of review statistics across the project's patch flow.
- **Where applicable**: The OVS/OVN contributor and dependent-vendor ecosystem generally; lightning-talk depth, so expect data over solutions.

## Themes

- **UDNs grew up and broke everything**: User-Defined Networks moved from headline feature to scaling liability — ARP/NDP fan-out, conntrack/ACL interactions, control-plane recomputes, and inter-UDN connectivity (ClusterNetworkConnect) dominate the program. Tenant-network density is now OVN-Kubernetes's central stress test.
- **"Interconnect of interconnects" is the federation pattern**: Nutanix (VM+multi-cluster VPC), Crusoe (AI-cloud re-architecture), and Magalu (multi-AZ VPC peering) all converge on the same idea — federate independent OVN domains via OVN-IC while keeping control planes local, with the VPC as the unit of federation.
- **Control-plane costs are being quantified, finally**: the 2.56x lflow cost of topological vs. tag-based route scoping, ovn-cp-bench's single-host cloud-scale testbench, PerfScale's repeatable UDN/EVPN workloads, and targeted megaflow revalidation all treat control-plane cost as a measurable, optimizable quantity rather than folklore.
- **Fabric-aware OVN-Kubernetes**: no-overlay mode (BGP-learned routes instead of Geneve) and EVPN testing reflect clusters increasingly deployed onto fabrics that already know how to route — the CNI stops re-solving problems the underlay solved.
- **OVS retooling for a hardware datapath**: the dpif-offload API consolidation, software/hardware hash alignment, two-ovn-on-one-DPU, and megaflow-revalidation work in the DOCA fork all point at a future where the software datapath is the exception, not the rule.
- **Rust and AI entering the toolchain**: a production OpenFlow controller rewritten in Rust with measured gains (and an OVS-in-Rust debate opened), an MCP server teaching AI agents to debug OVN, and AI-assisted testing of revalidation dependencies — both technologies arriving in the project's core workflows, not just its keynotes.
