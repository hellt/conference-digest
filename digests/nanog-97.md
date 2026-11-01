<!--
conference: NANOG 97
type: operator
source_url: https://nanog.org/events/nanog-97/agenda/
generated: 2026-11-01
registry_key: nanog-97
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NANOG 97 Digest

## Core

### Lessons From Scaling BPF To Detect RDMA Device Drivers Bugs In Real Time

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5659/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5659/20260530_Gupta_Lessons_From_Scaling_v1.pdf) · [Recording](https://www.youtube.com/watch?v=MbPCKIDUhmo)

Prankur Gupta – Meta Platforms, Inc

- **Why**: RDMA driver bugs are a top cause of AI training failures at Meta — 10–20% of daily AI job crashes are RDMA-associated (not network-related), wasting 32k+ GPU hours over six months — and the RDMA control path is famously opaque to existing observability. This sits squarely at the intersection of eBPF and lossless-fabric operations.
- **What**: RDMATracer, an eBPF-based tool that detects RDMA device driver bugs in real time by tracing kernel state mismatches across the ibverbs control path. In production it cuts diagnosis from 10+ minutes to seconds, auto-classifies issues, and was used to triage a black-box vendor driver bug (a `dma_resv_wait_timeout` overflow in `ib_umem_dmabuf_map_pages` on a newly deployed NIC driver).
- **How**: fentry/fexit BPF probes on kernel functions along ibverbs ioctl paths (fexit measured at ~72% of kretprobe overhead); static analysis to prune call paths (skip reads, pure-kernel internals, cleanup/refcount functions; per-vendor focus); a ~256KB ring buffer (~8k records) exports error context to userspace; per-CPU counter maps track invocation/error/errno counts. Periodically captures "good" traces and compares against failing ones to find the bifurcation point. Measured tax: p50 88.7% lower, p99 98.9% lower `bpf_tax`; no impact on workflow QPS.
- **Where applicable**: Built for Meta's Linux/RDMA GPU training fleet (vendor-specific driver paths baked into the pruning rules), but the engineering pattern — probe-point selection via static analysis, fexit over kretprobe, ring-buffer error-context export, good-trace diffing — transfers to any operator doing eBPF-based kernel-state tracing. Directly relevant to anyone running RoCE fabrics for training.

### Gray failures in AI Fabric

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5774/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5774/20260531_Singh_Fabric_Is_Sexy_v1.pdf) · [Recording](https://www.youtube.com/watch?v=qR_Bvs3AXX0)

Navtej Singh – Clockwork

- **Why**: AI training turned the DC fabric from boring plumbing into the throughput ceiling, and the failures operators now burn hours on are invisible to standard tooling — the motivating example is a GPU cloud that spent 19 hours hunting a slow training job caused by a hot transceiver whose FEC corrections had been climbing for days while the link stayed up.
- **What**: A working taxonomy of gray failures in AI fabrics — optic degradation via rising FEC corrections, intermittent CRC below thresholds, asymmetric paths, ECMP hash polarization landing collectives on hot links, PFC headroom exhaustion, sub-poll-interval microbursts — plus three fully worked scenarios (ECMP polarization, optic degradation, PFC cascade) showing what each telemetry layer sees and what it misses.
- **How**: Three time-aligned layers: host (NCCL kernel timing, RDMA QP stats, per-rank step time), edge (PFC pause counters, queue depth, per-packet HW timestamps), fabric (gNMI/INT streaming, buffer occupancy, FEC). The proposed gap-closers are sub-microsecond PTP clock sync (software-only, no special silicon) plus an out-of-band probe mesh (<1% of link capacity, separate QoS class) for one-way delay and per-path attribution; histograms over gauges; alert on p99.9 percentile drift; the SLO becomes p99.9 collective step time.
- **Where applicable**: Aimed at RoCEv2/lossless GPU-training fabrics and deliberately vendor-agnostic (IEEE 1588, OpenConfig/gNMI, INT/P4, NCCL profiler, DCGM, Linux RDMA counters). The speaker works for a vendor (Clockwork), but the scenario walkthroughs and tool references are open and portable. Cardinality discipline is flagged as the main scaling constraint.

### Network OS Upgrades at Hyperscale

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5754/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5754/20260531_Sekar_Rajan_Network_Os_Upgrades_v1.pdf) · [Recording](https://www.youtube.com/watch?v=3LuwTsGvx8I)

Sujitha Sekar Rajan – Meta Platforms Inc

- **Why**: Upgrading NOS across tens of thousands of multi-vendor devices without either security exposure or production incidents is a recurring dilemma, and this talk ships the pipeline *and* two rare, detailed war stories.
- **What**: Meta's vendor-agnostic 5-step upgrade process (vendor testing → planning → internal testing → canary → cardinality-gated rollout) with a Testbed-as-a-Service framework: tag-driven test selection on real lab hardware across all vendors and roles (50+ test cases for backbone edge alone), automated gating so no image reaches production without a full pass, progressive canary (lab metros → low-traffic → high-traffic), and cardinality rules (per-site/per-metro/global limits, freeze periods, independent role pipelines). War story 1: a vendor code refactor truncated version numbers from 64-bit to 32-bit, desyncing RIB and FIB silently under route churn (~9 days to failure at 5k updates/sec) after ~⅓ of the fleet was upgraded — only a reboot clears corrupted forwarding state, drain does not. War story 2: a re-timer DFE re-tuning bug on one vendor's odd-numbered 100GE ports produced persistent framing errors after link flaps while the interface showed up, requiring three-vendor coordination to isolate.
- **How**: Layered defensive pipeline; automated drain→reboot→undrain remediation; permanent forwarding-discard detectors promoted from incident tooling; shift to maintenance releases; sustained route-churn/FIB-consistency checks added to qualification after story 1.
- **Where applicable**: Explicitly Meta-scale (tens of thousands of devices, 3 hardware vendors, 5+ roles, up to 1.5M-prefix tables), but the pipeline design and lessons — real hardware not emulation, vendor labs can't reproduce production-scale churn, keep the detector you built during the incident — transfer to any multi-vendor operator.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5750/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5750/20260601_Weible_Channelmania_Future_v1.pdf) · [Recording](https://www.youtube.com/watch?v=5L4p1kNxmHg)

Thomas Weible – Flexoptix

- **Why**: With IPoDWDM, IP engineers inherit the spectrum-planning problem that used to belong to the transport team, and the shift from narrow-grid channel-count thinking to wide-grid superchannels changes topology and filter decisions that lock in for a hardware generation.
- **What**: An argument that as per-channel bandwidth grows (400G/800G/1.6T coherent superchannels), 400GHz COTS muxes future-proof the C-band (12×400GHz vs 96×50GHz) while remaining backward-compatible with legacy 50GHz services. Includes a compact coherent-detection primer (DP-QAM16, 425Gbps at 53.125GBd, phase- and polarization-diversity balanced receivers), the grid math (1.6T DP-QAM16 needs ~300GHz channel bandwidth), DIY superchannels via low-cost PLC 1x4 splitters feeding regular 50GHz mux/demux, and a market snapshot (800G ZR+ in DD/OSFP, 12.8T liquid-cooled XPO approaching).
- **How**: Think in THz/GHz rather than nm and channel numbers; make a frequency plan per span; exploit the fact that coherent receivers are "blind" to foreign wavelengths to build filterless/colorless topologies — at the acknowledged cost of flexibility, which wide-grid filters win back.
- **Where applicable**: For anyone planning or refreshing DWDM plant, especially IP engineers newly owning transport decisions. Caveat: this is Flexoptix research content and the 400GHz-COTS recommendation aligns with their product line — the physics and tradeoffs are general, the shopping advice is vendor-flavored.

### Migrating From Bespoke Hardware To An Open Load Balancing For Kubernetes

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5740/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5740/20260531_Kolobov_Migrating_From_Bespoke_v1.pdf) · [Recording](https://www.youtube.com/watch?v=IOXM7ur8QS0)

Sergey Kolobov, Marcin Wojciechowski (Arista Networks, per slides)

- **Why**: Replacing a 6.4Tbps proprietary stateless L4 load balancer with MetalLB in BGP mode is exactly the BGP-native Kubernetes ingress pattern many teams are evaluating, and the talk's core contribution is the network-side fix for ECMP's nastiest gotcha: widespread connection resets when the backend set changes.
- **What**: A full migration story: a 4-node MetalLB cluster (dual E5-2650 v4, 20Gbps LACP per node) sustains 6–10k RPS and 30k+ established connections, and benchmarked identically to the hardware appliance (~80 vs ~79.6 req/sec, same latency, 100% 200s over 100k requests). The key technique is pre-provisioning *resilient ECMP* groups on the ToR (`ip hardware fib ecmp resilience <IP>/32 capacity 16 redundancy 2`) — fixed modulo duplication of next-hops so only flows hashing to the failed next-hop remap, instead of all flows rehashing.
- **How**: MetalLB/FRR mode with BFD for sub-second failover; kube-proxy conntrack headroom (32k/core → `nf_conntrack_max` of 1,572,864); NIC ring buffer tuning (512→8192) against microburst RX drops; ingress nodes spread evenly across racks; ArgoCD GitOps; `vtysh` inside the speaker pod for BGP/BFD debugging. Also candid costs: strict port exposure replaced the "widely open" old model, adding a release-review step for developers.
- **Where applicable**: The resilient-ECMP fix is switch-ASIC specific (Arista syntax shown; other vendors have analogues) — verify your ToR supports it before adopting. Otherwise broadly applicable to bare-metal Kubernetes with a BGP-capable fabric. The stated next steps (Cilium BGP vs MetalLB consolidation — noting Cilium lacks native BFD — eBPF CNI migration, IPv6 dual-stack) are a useful roadmap of where K8s edge networking is heading.

### Monitoring 2,800 BGP Sessions using BMP Protocol

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5773/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5773/20260531_Odintsov_Monitoring_2_800_Bgp_v1.pdf) · [Recording](https://www.youtube.com/watch?v=lI5RxNt6jYc)

Pavel Odintsov – FastNetMon Inc (production network: Gcore)

- **Why**: Per-peer, route-level BGP visibility at scale is something SNMP, gNMI, and periodic full-table dumps each demonstrably fail to deliver — and this talk backs the claim with numbers rather than assertion.
- **What**: Benchmarks on a ~1.04M-route table: GoBGP text dump 2.0GB/73s; JSON 543MB/75s; gRPC/protobuf 25.5–27.5s; binary NLRI 15–15.5s; Rotonda (Rust, NLnet Labs) 9.6s JSON with 6.5x lower peak memory than GoBGP. Then the case for BMP (RFC 7854): per-peer exports across pre-policy, post-policy, and Loc-RIB stages, plus per-session stats (policy-rejected prefixes, duplicate advertisements, loop-invalidated updates, adj-rib-in/loc-rib counts). Production numbers: 2,728 peers and 68.9M routes re-emitted as a 9.8GB BMP dump in ~318s.
- **How**: BMP stations configured on Nokia, Juniper, Cisco XR, and Arista (config snippets shown for all four); Rotonda used as BMP collector *and re-emitter*, so downstream consumers get one initial full-table dump plus incremental updates instead of repeated snapshots. A Netomics fork addresses Rotonda's memory wall (112GB at 80M routes) with gzip, JSON streaming, TLS, and BMP output.
- **Where applicable**: Multi-vendor networks of meaningful scale (Gcore: 210+ PoPs, 4 routing platforms, 194M routes). Open-source tooling throughout (GoBGP, Rotonda, benchmark code published). Explicitly complements rather than replaces SNMP/gNMI for session-level health and hardware counters.

### Show Me Your PRs

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5772/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5772/20260530_Ulrich_Show_Me_Your_v1.pdf) · [Recording](https://www.youtube.com/watch?v=YS2Jga6HO04)

steve ulrich – nexthop.ai

- **Why**: For a PM whose core work includes physical DC networking, the open-NOS question is a portfolio-level bet, and this is one of the few operator-perspective (not vendor-marketing) assessments of what a durable SONiC ecosystem actually requires.
- **What**: A pragmatic map of where open NOS works today — greenfield L3 leaf/spine DC, AI/GPU cluster fabrics (with PFC and new hashing capabilities), campus refresh — and where it doesn't yet: the Internet edge (open NOSes lack high-scale ACL support even where the silicon, e.g. a Q3D ASIC with DFZ-scale FIB, could support it) and legacy SP core. Plus a security-compliance argument (patch out-of-support hardware yourself, Linux-LTS analogy), a sovereign-infrastructure/supply-chain angle, a sustainability warning (durable open source isn't free; "maintenance taxes" must be paid across the community), and a due-diligence checklist.
- **How**: The actionable core: before buying, target platforms that *can* run an open NOS later, require an open-NOS offramp, verify SAI/driver status, and — the title — ask vendors to show their PRs: verifiable upstream contributions, TSC presence, bootloader availability, and the ability to build your own images.
- **Where applicable**: Not org-specific; a strategy talk for any operator. Honest limitations stated: legacy-platform transitions are mostly unrealistic (no SAI pathway), secure/measured boot adds twists, and current roadmap leverage is concentrated in a handful of large operators. Explicitly not a vendor pitch, though the speaker's affiliation is worth noting.

### Vendor Independent Network Segmentation

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5777/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5777/20260530_Jemes_Vendor_Independent_Network_v1.pdf) · [Recording](https://www.youtube.com/watch?v=aNvGdvI9akE)

Brian Jemes – University of Idaho

- **Why**: Network segmentation designs usually collapse under vendor churn or rule-count growth; this is a concrete, numbers-backed architecture that survived six major vendor changes in 20 years — directly relevant to the PM's network-security interest.
- **What**: Subnet-level segmentation at the University of Idaho: 425 policy-enforced subnets (110 service-consumer, 190 service-provider, 120 behind the border), 230 router-ACL interfaces, 195 NGFW-interfaces carrying 840 rules, 10 router VRFs, 6 firewall virtual instances. The key policy insight is that provider subnets get "standalone" O(n) policies (inbound default-deny exposing only the services offered, outbound default-allow) referenced by subnet *groups*, avoiding O(n²) mesh rules.
- **How**: Consumers sorted into subnets via RADIUS-assigned VLANs (802.1X/MAB) from IdP user/device groups; dedicated VRF per consumer group with router ACLs blocking east-west; per-group virtual NGFWs; uRPF on every subnet; L2 ACLs for same-subnet traffic. Hard-won lessons: VRF-lite doesn't scale past ~3 VRFs, PBR isn't operationally scalable, DHCP relay in firewalls silently drops at enterprise scale, aggregate the address plan by type *before* geography, and use hub-spoke virtual cloud architecture because clouds aren't structured for subnet segmentation.
- **Where applicable**: Mid-size enterprise (12k students, ~70k WiFi endpoints, ~800 switches) but the pattern is deliberately vendor-independent and generalizes. The tradeoff is explicit: middleboxes in all internal traffic flows complicate intranet routing and troubleshooting; app-layer authn/authz is out of scope.

### The Kimwolf Aftershock: Residential Proxy Botnets One Year Later

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5771/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5771/20260531_Labovitz_The_Kimwolf_Aftershock__v1.pdf) · [Recording](https://www.youtube.com/watch?v=eOmeQcwSK3o)

Craig Labovitz – Nokia; Chinni Tadivaka (joint Comcast Threat Research Lab / Nokia ERT research)

- **Why**: Residential-proxy-driven DDoS is now a backbone-scale security problem — attacks saturating transit and POP links, not just enterprise targets — and this is the rare talk with a year of longitudinal data on what disruption actually achieved.
- **What**: The follow-up to NANOG 94's warning: law-enforcement and provider takedowns measurably cut US outbound DDoS, but Kimwolf metastasized into 21+ successor botnets ("ResHydra") reusing the same ADB-based residential exploits; daily active DDoS botnet endpoints climbed from ~1M (summer 2025) to 8M+ (2026), aggregate capacity in the hundreds of Tbps, with 100+ Tbps rated as a potential threat to most national networks. The economics: 75% of res-proxy attacks originate from US or Brazilian homes; the multi-billion-dollar proxy market is now funded largely by AI scraping demand; and gigabit symmetric broadband keeps raising upstream capacity.
- **How**: Measurement via large-scale crawling, a botnet security range, licensed third-party data, and collaborating ISPs/hosting providers. The concrete remedy demonstrated: one LATAM ISP enabling C2-blocking ACLs on May 7, 2026 saw an immediate multi-Tbps drop in outbound DDoS — infrastructure reliability genuinely equals disrupting botnet C2 in your network.
- **Where applicable**: Most relevant to ISPs/backbones and anyone operating consumer-facing access networks. Research artifacts are published (github.com/deepfield/public-research). The C2-disruption remedy is real but constrained by accuracy, policy, and legal concerns — which is exactly why NA adoption lags.

## Adjacent

### Paraglider: Streamlining Cloud Networking

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5770/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5770/20260531_Mcclure_Paraglider_Streamlining_Cloud_v1.pdf) · [Recording](https://www.youtube.com/watch?v=WCwhY4D3eKA)

Sarah McClure – UC Berkeley (LF Networking project with Google, Microsoft, IBM)

- **Why**: A research-to-production attempt to fix the core pain of cloud networking — low-level, vendor-specific primitives — with a high-level connectivity abstraction; relevant context for anyone working on cloud-native networking intent models.
- **What**: Evolved from Berkeley's NSDI'22 "Invisinets" into an LF project with cloud-provider contributors. The model: basic reachability is provisioned for you; connectivity is expressed as permit lists on resources (default-off), with tags naming/grouping resources across clouds. The demo makes the value concrete: connecting three VMs across Azure and GCP auto-generated 3 NSGs, 4 subnets, 3 VNets + 1 VPC, 3 peerings, 2 VPN gateways, a cloud router, and a VPN tunnel.
- **How**: A `glide` CLI (create/attach resources, tag them, add permit rules) driving an orchestrator with per-cloud plugins (Azure, GCP, IBM; AWS in roadmap); the controller provisions peerings, VPN tunnels, and BGP underneath; supports Kubernetes clusters and private endpoints; permit lists auto-update as tag membership changes.
- **Where applicable**: Multicloud operators, especially greenfield. Honest open problems stated: brownfield compatibility and deployment validation still in progress, private IP-space management across clouds, "the cloud is a moving, obscured target," and cloud customers are entrenched in existing APIs. Simplicity is an explicit compromise (boilerplate with escape hatches).

### The Hidden Costs of SSH at Scale (Remote Presentation)

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5776/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5776/20260530_Lykins_The_Hidden_Costs_v1.pdf) · [Recording](https://www.youtube.com/watch?v=0-SJYlzcMjI)

Brett Lykins – Amazon

- **Why**: SSH is the default automation transport, and this talk quantifies — with open-source benchmarks — what its 10–15 round-trip handshake actually costs across a WAN, then gives an adoptable fix that requires no device changes.
- **What**: Measured with `tc netem` at 150ms RTT: SSH PTY (Netmiko-style) takes 2,565ms before/around 5 commands vs 151ms for batched HTTPS — 17x. An edge proxy (SSH local at 1–2ms, HTTPS over the WAN) reaches 5.3x on new connections and 14.7x with reuse; a transparent tunnel (SSH on both ends, HTTPS only on the WAN segment) gets 12.7x with *zero* code changes to existing Ansible/Nornir. At 100k devices with 100 parallel lanes: 42.8 minutes down to 8.1.
- **How**: NAAS (Netmiko-as-a-Service) — a lightweight proxy co-located with devices, deployable via docker compose, 100+ platforms; device SSH keys never cross the WAN; treat it like a bastion (hardening, rotation, session logging). Migration path: tunnel first (no changes), proxy second, native HTTPS (eAPI/NX-API/RESTCONF) where supported. Decision framework included: <5ms RTT don't bother; 5–30ms measure first.
- **Where applicable**: Any WAN-distributed automation estate. Broadly applicable, no vendor dependence, benchmark and tool code open source (github.com/lykinsbd/clibench, /naas).

### Crafting Network Configurations at Meta

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5671/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5671/20260531_Munoz_Rodriguez_Crafting_Network_Configurations_v1.pdf) · [Recording](https://www.youtube.com/watch?v=LaElarEazy4)

Santiago Alfonso Munoz Rodriguez – Meta

- **Why**: How a hyperscaler generates config for thousands of multi-vendor backbone devices daily is a useful reference point for anyone designing (or buying) network automation — and the compiler framing is genuinely clarifying.
- **What**: Meta's stack — FBNet object store, Skynet Thrift API, Jinja2 config generation — extended with Skypath, a minimal query DSL embedded directly in templates (`{$ Router[name={dev}]/asn $}`), which turns templates into self-contained specifications that engineers can reason about close to plain CLI. The multi-vendor layer is a "Confpiler": vendor-agnostic IR (OpenConfig-like), frontend authoring/analysis, backend IR→vendor-YANG schema translation separated from serialization — so delivery protocol (CLI for humans, NETCONF/gNMI for machines) can switch on the fly, and the multi-vendor network is operated as if single-vendor.
- **How**: Lazy-evaluating interpreter preprocesses templates; compile-time static blueprint with runtime-rendered dynamic values (a Java bytecode analogy); versioned packages pin code commits so rollback knows which implementation to return to.
- **Where applicable**: Meta-scale backbone with daily change volume. The stated lessons temper transfer: "our ability to be declarative can only be as good as our database models," there's a limited budget for tooling change, and "abstraction only makes sense when behavior is portable." Concepts transfer; the surrounding systems are the hard part.

### What's New at the IETF

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5762/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5762/20260530_Qu_What_S_New_At_v1.pdf) · [Recording](https://www.youtube.com/watch?v=wvkKX4jFvv8)

Yingzhen Qu – Futurewei Technologies; Yaroslav Rosomakho – Zscaler

- **Why**: Standards-watch with an unusually dense set of identity-relevant items for this program: the wimse WG (Workload Identity in Multi-System Environments) adopted its Workload Identifier draft and split service-to-service credentials and authentication mechanisms into separate drafts; the OAuth WG adopted OAuth SPIFFE Client Authentication and published RFC 9901 (selective disclosure for JWTs); plus ECH RFCs (9848/9849), ML-KEM/SLH-DSA identifiers for X.509, and the new "plants" WG on Merkle Tree Certificates for post-quantum PKI.
- **What**: A survey of IETF/IRTF/IAB structure and active work across areas — routing (BGP-4 4271bis, ASPA verification, RPKI-to-router 8210bis), QUIC multipath and MoQT, DELEG for DNS, NEMOPS-derived service abstractions (ONSEN BoF), and agentic coordination work (CATALIST).
- **How**: Overview format; the useful artifact is the map of where each effort sits and which drafts are newly adopted vs published.
- **Where applicable**: Broad relevance; for this PM, the wimse, OAuth-SPIFFE, and post-quantum PKI threads are the take-homes for workload/agentic identity planning.

### Versioned Services for Network Automation

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5673/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5673/20260601_Henderson_Versioned_Services_For_v1.pdf) · [Recording](https://www.youtube.com/watch?v=uai6k0JcUdk)

James Henderson – Ductus

- **Why**: Automation systems are usually written as if the standards they implement never change; this offers a clean, adoptable pattern for managing service intent across time — with EVPN as the running example.
- **What**: A pattern combining named service *types*, semantic *versions*, and *managed features* — where a feature is a flag with metadata (introduced-in, standard-in, when-disabled fallback behavior, conflicts-with) rather than a bare code switch — plus cascading (hierarchical) types that control which features a service may use. Versioned packages pin each service version to an exact code commit, so rollbacks know which implementation to return to, and individual features can migrate independently across services (the talk shows a mid-migration state where one customer's RT is migrated and another's RD is not).
- **How**: Semantic versioning for services (major = breaking contract change, minor = golden-config update with new feature, patch = code fix); the type carries classification, the version carries which flags apply.
- **Where applicable**: General technique for any golden-config/automation platform, org-agnostic despite the EVPN examples. Also argued (briefly) as a prerequisite for safe AI agents in network ops — reversibility and transparency — which pairs naturally with the agentic sessions below.

### From Metrics to Investigation: How Agentic SRE Could Change Network Operations

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5766/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5766/20260530_Mahmud_From_Metrics_To_v1.pdf) · [Recording](https://www.youtube.com/watch?v=JdQOLTqPIy8)

Mohibul Mahmud, Shamir Abdul Aziz, Karthik Srinivas Muthuramakrishnan – Microsoft

- **Why**: A working — not aspirational — agentic investigation system for network incidents, with an honest list of what still doesn't work; for anyone thinking about agentic identity and trust boundaries, this is the ground truth from an early deployment.
- **What**: An LLM-driven investigation agent on Azure (Claude Opus-based, configurable) that handles the unknown-failure case runbooks can't: hop-by-hop topology discovery, protocol-level diagnostics across BGP, IKE Phase 1/2, and ExpressRoute, and a production case where it detected a blackhole route from a deallocated firewall in under 35 seconds. Four scenarios covered: live NL troubleshooting, scheduled monitoring with alert integration, topology discovery from minimal input, hybrid-connectivity analysis.
- **How**: LLM reasoning + structured tools (Azure CLI, Resource Graph, Network Watcher) + operator-authored skills written in Markdown + governance (RBAC, isolated compute, safety hooks, human approval). The stated non-negotiables: read-only as the enterprise default, human approval required before any write action, and on-prem coverage only via telemetry forwarding to Log Analytics.
- **Where applicable**: Demoed on Azure, but the pattern (reasoning layer + read-only tools + knowledge base + safety harness) is explicitly presented as generic. Azure-centric in tooling; the write-action approval gate is the identity/trust boundary worth watching as these systems mature.

## Wildcard

### Towards a Non-Binary View of IPv6 Adoption

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5748/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5748/20260530_Thottungal_Valapu_Towards_A_Non-Binary_v1.pdf) · [Recording](https://www.youtube.com/watch?v=zyPZ9mOl2tQ)

Sulyab Thottungal Valapu – University of Southern California / Information Sciences Institute (with John Heidemann)

- **Why**: Not about any of the PM's core areas, but the results reframe a long-running debate with measurement: IPv6 adoption isn't binary, and the "how much" numbers are surprising.
- **What**: Client-side: 9 months of flow data from 5 dual-stacked LA residences shows daily IPv6 fraction varies enormously (a single application can swing a site between an 11% day and a 91% day), with per-site medians diverging widely. Server-side: a browser-based crawl (dependencies resolved to arbitrary depth) of the Tranco top 100k finds only 12% fully IPv6-loadable — 42% have v6 enabled but 30% of the total still require IPv4 to fully load; fixing the top 5% of popular v4-only resources would fix over 25% of partial sites. Cloud-side: same-tenant paired comparisons (Wilcoxon) show deployment *mechanics* dominate — CloudFront's automatic v6 hit 71% while S3's opt-in dualstack-URL requirement yields 0.4%; Azure Front Door shows 100% is possible with no opt-out.
- **How**: Passive flow capture (no payload) for clients; OpenWPM crawl with link-clicking for servers; n×n tenant-pair grid to separate cloud support from tenant choice.
- **Where applicable**: The cloud recommendations (deploy v6 transparently rather than opt-in) are actionable for any platform provider; the client/server figures are bounded by US broadband and top-100k methodology but the non-binary framing generalizes.

### Designing Cloud Workloads For LEO Satellite Internet Users

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5783/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5783/20260530_Mathur_Designing_Cloud_Workloads_v1.pdf) · [Recording](https://www.youtube.com/watch?v=003DkohsosM)

Sid Mathur – Fastah Inc.

- **Why**: LEO connectivity is quietly becoming a real user population, and it breaks assumptions (stable egress, stable IP geo, predictable RTT) that most cloud architecture takes for granted.
- **What**: A mental model and design-pattern set for LEO-served users: traffic lands at ~200 (Starlink) / 300+ planned (Amazon LEO) ground gateways mapped to IX/PoPs; static users behave like fixed broadband, while in-motion users (aviation, maritime) change egress mid-session — the talk traces one flight's IP geolocation through Qatar, Kuwait, Jordan, Bulgaria, Hungary, Germany, and France, with all the GDPR/jurisdiction questions that implies. Amazon LEO B2B rides AWS Direct Connect, so once traffic lands it's ordinary VPC traffic; new multicloud interconnects (AWS Interconnect Multicloud, GCP Cross-cloud Interconnect) enable cross-cloud failover patterns.
- **How**: Three patterns — pin static low-latency users to the nearest region with PNI for predictable RTT; build in-motion users as multi-region active-active with stateless services and HTTP/3 tolerance for TLS/TCP resets; use cross-cloud interconnects for "too expensive to fail" B2B workloads. Decision inputs: user-population geography, data sovereignty, egress cost, latency budget, failover topology.
- **Where applicable**: Teams building applications for LEO user populations; the interconnect specifics are AWS/GCP-specific. Key takeaway: the routing path is the only truly different part.

### 50 Years of Networking

**Links:** [Abstract](https://nanog.org/events/nanog-97/content/5621/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5621/20260530_Huston_50_Years_Of_v1.pdf) · [Recording](https://www.youtube.com/watch?v=Umtxxz7GyFc)

Geoff Huston – APNIC

- **Why**: Not a technique talk — a direction-of-field argument from one of the Internet's longest-running observers, and the argument lands squarely on questions this PM cares about (openness, centralization, what the AI build-out means).
- **What**: Why Ethernet won (open, cheap, simple, self-operating, and — crucially — an invariant frame format that preserved capital across 50 years of speed and medium changes); IP as "large-scale Ethernet" pushing complexity to the edge. Then the uncomfortable present: name-based service delivery has replaced hop-by-hop address networking, the Internet's "core" is now private CDN feeder systems, and transit is dead. The alternate tomorrow: if Moore's Law stalls, the AI build-out looks like a return to centralized, expensive, specialized compute — and Huston's real warning is the resurgence of closed, black-box platforms whose applications deliberately avoid standard open technologies, making open standards the endangered species.
- **How**: Historical analysis and argument; no mechanism to evaluate.
- **Where applicable**: Speculative and big-picture, but a useful stress test for any strategy that assumes the next 50 years look like the last 50.

## Themes

- **AI training fabrics are re-making DC network operations.** Gray failures, RDMA driver observability, and SLOs expressed as p99.9 collective step time (Gray failures, BPF/RDMA at Meta, the keynote) are the new operational frontier — the techniques are physical-layer-adjacent (FEC counters, PFC headroom, transceiver health) and directly in this program's wheelhouse.
- **BGP is the Kubernetes-native integration point.** MetalLB/BGP ECMP ingress, BMP-based per-peer telemetry at 2,800 sessions, and BGP-datapath tooling (GoBGP, Rotonda) all show classic BGP internals moving into product conversations around cloud-native platforms.
- **Open NOS / disaggregation is maturing unevenly.** Strong in greenfield DC and AI fabrics, explicitly not ready for the Internet edge (Show Me Your PRs), while Meta's talk shows the operational price of multi-vendor at scale — qualification pipelines, canary discipline, and cross-vendor interop war stories.
- **Agentic network ops is arriving with explicit trust boundaries.** Both agent talks converge on the same governance model — read-only by default, allowlisted tools, human approval before writes — which makes the identity/authorization story for agents (who may act, on what) the open design problem, echoed by wimse and OAuth-SPIFFE work at the IETF.
- **Telemetry beyond polling.** Streaming (gNMI), high-resolution time-aligned measurement, histograms and percentile drift instead of gauges and thresholds, and BMP instead of SNMP — a consistent shift across the fabric, BGP, and observability sessions.
- **AI's externalities are showing up on the security side.** The residential-proxy botnet economy is now measurably funded by AI scraping demand (Kimwolf), while AI workloads themselves demand lossless-fabric reliability — two sides of the same cycle, both landing on network operators.
