<!--
conference: ACM CoNEXT 2025
type: academic
source_url: https://conferences.sigcomm.org/co-next/2025/partials/program.html
generated: 2026-11-04
registry_key: conext-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ACM CoNEXT 2025 — Digest

A note on sources: all ACM Digital Library page links returned HTTP 403 to the fetcher, so every write-up below is grounded in the conference program's abstracts only. Depth flags reflect that.

## Core

### Demystifying Performance of eBPF Network Applications

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3749216) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3749216)

Farbod Shahinfar; Sebastiano Miano (Politecnico di Milano); Aurojit Panda (NYU); Gianni Antichi (Politecnico di Milano & Queen Mary University of London)

- **Why**: eBPF is the load-bearing technology behind Cilium, service-mesh dataplanes, and a growing share of host networking. This paper asks the inverse of the usual question — not "how fast can eBPF go" but "where does eBPF actively hurt" — and the answer should change how you reason about which workloads belong on which side of the kernel boundary.
- **What**: A systematic benchmark study showing that many networked applications cannot benefit from eBPF at all, and that eBPF can create performance isolation violations between co-located applications and constrain deployment and workload choices. The paper also assesses whether in-flight kernel work (e.g., the ongoing JIT/verifier and scheduling improvements) fixes the identified limits, and proposes directions for the community (from abstract only).
- **How**: Multiple benchmarks under deliberately varied workloads with purpose-designed test cases isolating the failure modes — the methodology is the contribution as much as any single number.
- **Where applicable**: Broadly applicable to any team running eBPF in the host datapath (Kubernetes CNI dataplanes, host-LB offloads, socket-level accelerators). Treat the isolation-violation finding as a caveat for multi-tenant hosts specifically.

### Taurus: Towards A High-Performance and Generic Congestion Control Framework for Datacenter Networks

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768973) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768973)

Luyang Li et al. (ICT CAS / Chinese Academy of Sciences / Douyin Vision Co., Ltd. / HKUST)

- **Why**: Congestion-control frameworks (CCP, DOCA-PCC) are how production DCs keep RDMA/lossless-ish fabrics usable across diverse workloads, and this is one of the few papers with a real 400Gbps production deployment behind it — with authors from ByteDance's Douyin group, it carries deployment weight.
- **What**: A hardware–software co-designed CC framework that lets operators deploy varied CC algorithms at near-native performance. Reported results vs. CCP: +32.3% throughput, −96.4% latency, −158.7% CPU overhead; vs. DOCA-PCC: +9.3% throughput, −28.8% latency (from abstract only).
- **How**: Partitions CC functionality into distinct tasks and maps them onto appropriate hardware vs. software components: a collaborative signal-collection mechanism supporting diverse congestion feedback, a type-aware message report engine with two-tier aggregation to cut host↔NIC communication overhead, and software built-in handlers so new algorithms can be deployed without changing the datapath.
- **Where applicable**: Datacenter fabrics at 100–400Gbps; requires FPGA-based NICs (implementation is on commodity servers with FPGA NICs), so it presumes you control the host NIC hardware. The Douyin production deployment makes the results credible but the environment is a specific hyperscale DC — expect the tradeoffs to shift with different NIC generations.

### Secure and Efficient RDMA NIC Cryptography Offloading for Memory Disaggregation

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768991) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768991)

Wonsup Yoon; Sue Moon (KAIST)

- **Why**: Sits squarely at the intersection of two of your core areas — RDMA fabrics and security. Memory disaggregation is moving from research to production, and almost nobody encrypts RDMA traffic because the performance cost is brutal. This is one of the first systems to make encrypted RDMA practical by offloading crypto to the RNIC itself.
- **What**: A secure memory-disaggregation system providing confidentiality and integrity for data in transit and at memory nodes, with crypto offloaded to the RNIC. Reported result: up to 9.63× lower P99.9 latency than a CPU-based implementation on a RocksDB workload (from abstract only).
- **How**: Three key datapath designs — dynamic MKey reconfiguration, configuration-data batching, and MKey pooling — to work around RNIC hardware limits and slow on-NIC encryption. The central finding is that the win comes from overlapping CPU compute with RNIC encryption via a yielding mechanism that lets the CPU do other work while the NIC encrypts.
- **Where applicable**: Memory-disaggregated clusters with RDMA NICs that support MKey manipulation and crypto offload. Notably, the paper is candid that RNIC crypto is relatively slow — the design leans on overlap rather than raw crypto throughput. Hardware-generation-dependent; not directly portable to older RNICs.

### ASNI: Redefining the interface between SmartNICs and applications

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3730966) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3730966)

Nikita Tyunyayev; Clément Delzotti (UCLouvain); Haggai Eran (NVIDIA); Tom Barbette (UCLouvain, Belgium)

- **Why**: As NICs get "smarter," the descriptor/driver software interface is becoming the bottleneck — the paper frames it as a 300-cycle-per-packet budget at NFV speeds, of which even DPDK eats 20%. This is a proposal to redesign that boundary, which matters to anyone betting on SmartNIC-offloaded dataplanes.
- **What**: An argument and prototype for NICs adapting to application needs rather than drivers acting as translators: a datapath API that compiles into different buffer-management models per application, tailoring packet descriptors so the application receives packets precisely in the form it needs. Reported result: 2.2× more traffic served at equal loss constraints vs. state of the art (from abstract only).
- **How**: Analysis of multiple packet-buffer and data-organization models across application classes, then a minimal-driver design where packet descriptor layout is generated per application and driver work is removed from the datapath. Prototyped on NVIDIA BlueField 3.
- **Where applicable**: NFV and high-packet-rate host networking on BlueField-class SoCs. The vision is general, but the prototype is BlueField 3-specific; treat it as evidence for a design direction rather than a deployable API today.

### SwitchNIC: Tightly-Coupled Heterogeneous Platform to Accelerate Network Functions

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768993) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768993)

Yiran Lei (Carnegie Mellon University); Francisco Chamiça Pereira (INESC-ID/IST Lisboa); Arvind Krishnamurthy (University of Washington); Justine Sherry (Carnegie Mellon University)

- **Why**: The PISA-switch + general-purpose-server hybrid ("best of both worlds") keeps failing on one problem: keeping distributed state consistent across the two platforms without wrecking latency. This paper attacks exactly that, and it is the kind of result that shapes the next generation of hybrid middlebox designs.
- **What**: A tightly-coupled architecture guaranteeing consistent shared state between a Tofino switch and co-located general-purpose processors, with 6µs P99 packet latency, 5.2× better energy efficiency, and 6.4× better processing latency than server-based systems — which the authors note cannot fully/correctly support shared state between platforms (from abstract only).
- **How**: A novel "on-path" state replication protocol, with latency tightened by running the general-purpose processing on locally-integrated ARM cores rather than a separate x86 server. Prototype: Tofino + Ethernet-attached ARM-based SmartNICs.
- **Where applicable**: Network functions needing both line-rate PISA processing and complex/stateful general-purpose logic. Constrained to hardware you can pair closely (switch + ARM SmartNICs in the same box/chassis); Intel Tofino's future availability is a known ecosystem risk for PISA-based designs generally.

### Inside Job: Defending Kubernetes Clusters Against Network Misconfigurations

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3749220) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3749220)

Jacopo Bufalino (Aalto University, CNAM); Jose Luis Martin Navarro (Aalto University, Universitat Politècnica de València); Mario Di Francesco; Tuomas Aura (Aalto University)

- **Why**: K8s network policy and cluster networking config is a real, underserved attack surface — most K8s security work targets the API server or supply chain, not the network configuration enabling lateral movement. This is an empirical study of that gap at real-organization scale.
- **What**: A comprehensive analysis of network misconfigurations in Kubernetes deployments, focused on lateral movement risk. The authors evaluated 287 open-source applications from six organizations and found 634 misconfigurations, "well beyond" what state-of-the-art tooling catches; 30+ applications have already been fixed with their proposed mitigations after responsible disclosure (from abstract only).
- **How**: Methodology is the core: systematic auditing of cluster network configuration (policies, exposure, connectivity grants) against lateral-movement attack paths, with severity assessment discussed directly with the affected organizations.
- **Where applicable**: Broadly applicable to anyone running multi-tenant Kubernetes — the findings come from open-source production deployments across IT companies, public entities, and non-profits, not a lab cluster. Useful both as a defensive checklist and as evidence for policy-as-code investment.

### The New (Pareto) Frontier of Cloud Routing: High Availability, Precise Control, or Stable — Choose Two

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768975) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768975)

Jiangchen Zhu; Ethan Katz-Bassett (Columbia University); Tom Koch (Google); Matt Calder (Meta); Italo Cunha (UFMG); Kevin Vermeulen (CNRS, École Polytechnique); Shuyue Yu; Ilgar Mammadov (Columbia University)

- **Why**: Best Paper, and directly on the anycast-vs-DNS-redirection problem every large service faces for client-to-site mapping. It proves a structural tradeoff rather than proposing yet another mapping system — that reframing is what makes it worth a practitioner's time.
- **What**: A demonstration that general-purpose client-to-site direction methods face inevitable tradeoffs among precise control, high availability, and routing stability, plus new routing techniques that establish a better Pareto frontier than anycast or DNS-based unicast redirection. One technique speeds unicast failover by up to 5 minutes while keeping unicast's control advantages; another achieves anycast's availability with far better control (from abstract only).
- **How**: Formal analysis of the three-way tradeoff, then new mapping/failover mechanisms validated via Internet-scale experiments — not simulation. Google and Meta authorship signals access to real production constraints (failover load on healthy sites, cascading-failure risk).
- **Where applicable**: Geographically distributed, latency-sensitive services mapping clients to sites at global scale. The techniques target the largest clouds' problems; the tradeoff framing, however, applies to anyone choosing between anycast and DNS-based redirection for multi-region service frontends.

### Transient Forwarding Anomalies and How to Find Them

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3730973) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3730973)

Roland Schmid; Tibor Schneider; Georgia Fragkouli; Laurent Vanbever (ETH Zurich)

- **Why**: Transient reachability violations during BGP re-convergence are exactly the class of event that makes a mockery of tight SLAs, and no existing method measures them accurately for all prefixes without perturbing the network. TRIX is a genuinely new inference approach to a problem you live with daily in WAN operations.
- **What**: TRIX infers transient violation times for BGP events from logged routing events or collected BGP messages, reconstructing network-wide reachability violations without active probing of every destination. Validated on a testbed with 12 real routers and a programmable switch: inferred violation times average within 13–25 ms of ground truth, and the approach scales to large networks (from abstract only).
- **How**: Key insight: you don't need to probe all destinations if you can reconstruct router-local forwarding state for all of them from available information. TRIX simulates the BGP control plane, models FIB-update rate, and combines per-router state with propagation delays — overcoming the fact that logged events are inaccurate in both content and timing of forwarding updates.
- **Where applicable**: Any BGP network with routing-event logging or route-collection infrastructure; the method is passive and doesn't worsen network performance. General technique, not operator-specific, though the 13–25 ms accuracy was established on a specific testbed configuration.

### Scalable and Interpretable Overlay Network Checking via Ensemble Verification

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768974) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768974)

Xinzhe Liu; Yahui Li; Han Zhang; Xia Yin; Xingang Shi; Zhiliang Wang; Gang Ren; Jilong Wang (Tsinghua University); Jiangyuan Yao (Hainan University)

- **Why**: Overlay/underlay is the architecture of modern WANs (cloud backbones, telco SD-WAN, service overlays), and control-plane verification tools built for flat underlays choke on it. This is the first verifier purpose-built for overlay/underlay — and it has a real nationwide deployment behind it.
- **What**: MEV, a control-plane verifier for overlay/underlay networks using a novel "ensemble verification" paradigm: independent reasoning within each routing instance/protocol and within each virtual network, then composition. Deployed on FITI (Tsinghua's nationwide testbed), where it found 22 real misconfigurations that could cause isolation and reachability issues; achieves up to 10²× speedup over an extended Batfish on FITI and synthetic networks (from abstract only).
- **How**: The decomposition into per-instance/per-virtual-network verification is what buys both scalability and interpretability — errors are explained in the routing instance where they occur rather than as a flat cross-product of states.
- **Where applicable**: Networks running overlay services (VPNs, L2/L3 VPNs, cloud backbone overlays) atop a routed underlay. The deployment is FITI-specific (China's CERNET-derived infrastructure), but the method is general; interpretable counterexamples matter most where operations teams, not verification researchers, consume the output.

### Exp-PIFO: Scalable and Efficient Programmable Packet Scheduling

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3749217) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3749217)

Habib Mostafaei (TU/e); Mohammad Ezzati (TU Berlin); Pieter J. L. Cuijpers (TU/e); Stefan Schmid (TU Berlin); Gábor Rétvári (BME); Sem Borst (TU/e)

- **Why**: PIFO — the abstraction underlying ideal push-in-first-out scheduling — has been blocked from real switch silicon because it needs line-speed sorting. The approximations that fit hardware (SP-PIFO, AIFO) don't scale in queue count. This paper's approximation is startlingly cheap, and it sometimes beats the abstraction it approximates.
- **What**: A new PIFO approximation, Exp-PIFO, that tracks scheduling state with only two memory cells and uses a lookup table to avoid complex control flow. Empirically it sometimes outperforms strict PIFO on flow-completion-time metrics — and the paper explains why rather than shrugging. Proof-of-concept on Intel Tofino uses significantly less memory than SP-PIFO/AIFO implementations (from abstract only).
- **How**: Adaptive exponential prioritization: packets are prioritized by "exponential bins" — a coarse logarithmic ranking that preserves the ordering properties that matter for FCT while collapsing the state needed to maintain it.
- **Where applicable**: PISA-based programmable switches (Tofino demonstrated). Directly relevant to anyone building scheduling logic into switch pipelines or reasoning about what QoS primitives are actually implementable in merchant silicon; the two-cell state makes it deployable where nothing else fits.

## Adjacent

### MorphOS: An Extensible Networked Operating System

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768977) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768977)

Peter Okelmann; Ilya Meignan-Masson; Masanori Misono; Pramod Bhatotia (Technical University of Munich (TUM))

- **Why**: The eBPF-as-extension-mechanism idea escapes the Linux kernel: here it's used to make unikernel VNFs hot-updatable without rebuilds, restarts, or state loss. If you care about where eBPF's programming model goes next, this is a data point.
- **What**: An extensible networked OS for dynamic, stateful network functions. Integrating eBPF enables dynamic, verified code execution to update packet-processing logic live; reported results include drastically reduced reconfiguration time, amortized verification costs, and up to 3× better performance vs. Linux-based VNF deployments, while keeping unikernel lightness (from abstract only).
- **How**: eBPF plus an out-of-band verification service (so the data path doesn't pay verification cost) and hardware-assisted memory isolation via Memory Protection Keys (MPK) for execution hardening.
- **Where applicable**: VNF/NFV deployments where update frequency and state continuity matter. Research prototype; the MPK dependence ties it to specific x86 generations, and the eBPF-in-unikernel runtime is not something you can adopt today — but the architectural pattern (verified hot-patching of fast-path logic) generalizes.

### MoonEm — High-Precision Path Property Emulation using DPDK

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768976) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768976)

Stefan Lachnit et al. (Technical University of Munich)

- **Why**: Every systems evaluation you've read that used NetEm is suspect — this paper quantifies how NetEm's own performance limits distort measurements. If you run performance tests against emulated network conditions, this changes your tooling.
- **What**: A DPDK-based path property emulator that precisely controls packet transmission times on commodity hardware: 13.39 Mpps vs. NetEm's 0.98 Mpps; median latency deviation 53 ns vs. NetEm's 71.15 µs, worst case 80 ns vs. 769.26 µs (from abstract only).
- **How**: DPDK userspace packet engine with a novel, precisely timed transmission schedule — the point is that the emulator's own jitter is now orders of magnitude below the phenomena it emulates, so loss/delay/capacity injection is reproducible.
- **Where applicable**: Any lab or CI environment doing network-conditioned application testing. General-purpose tool on commodity NICs; drop-in for NetEm use cases where fidelity matters (and, per the paper, it should matter more often than assumed).

### SepaNet: Towards Practical Large-Scale Full-System Simulation for Systems Research

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768999) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768999)

Hejing Li (MPI-SWS); Marvin Meiers (Saarland University); Jialin Li (NUS); Antoine Kaufmann (MPI-SWS)

- **Why**: Their premise matches what DC practitioners know: bottlenecks today are in host software and hardware, not the wire protocol, yet most network evaluation still simulates protocols. SepaNet makes end-to-end (full-system) simulation at cluster scale tractable — a methodology shift for anyone reasoning about DC system design.
- **What**: A simulation framework that lets users navigate fidelity/time/resource tradeoffs explicitly by mixing simulation models of different fidelity with controlled parallelization, guided by a profiler that identifies bottlenecks and informs partitioning. Demonstrated: a 1200-node datacenter network running end-to-end applications, simulated in 175 minutes for 20 s of system time on 24 cores (from abstract only).
- **How**: User-specified system abstractions instantiate multiple simulations of the same system at different fidelity levels; the framework composes them and parallelizes with awareness of where fidelity actually matters.
- **Where applicable**: Research and pre-deployment evaluation of distributed/DC systems where physical testbeds at scale are out of reach. A research framework rather than product, but the mixed-fidelity idea is directly borrowable for internal evaluation tooling.

### NetFridgeS: Enabling Dynamic Frequency Scaling on Network Switches through Carbon-Aware Routing

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768984) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768984)

Zhukun Wang; Noa Zilberman (University of Oxford)

- **Why**: Switches run at max pipeline clock 24/7 because nobody can afford a drop, while traffic is strongly periodic. Energy and carbon are becoming first-order DC fabric constraints (power delivery, PUE targets), and this is a concrete mechanism, not a positioning paper.
- **What**: Dynamic frequency scaling for high-performance switch pipelines, prototyped on FPGA across three pipeline architectures: sub-microsecond frequency switching, and an average energy saving of 77.74% at minimum throughput. Combined with carbon-aware routing over real topologies: up to 22.11% lower energy consumption and 27.76% lower carbon emissions vs. current deployments (from abstract only).
- **How**: Carbon-aware routing forecasts network utilization and adjusts pipeline frequency ahead of demand, so the pipeline slows down when and where traffic forecasts permit — solving the "must not drop packets" objection by tying frequency to predicted load rather than reacting after drops.
- **Where applicable**: Switch silicon design and fabric operations. The prototype is FPGA-based; merchant-silicon switches don't expose pipeline DVFS today, so near-term this is a signal to silicon vendors (and a design input) rather than a deployable feature. The forecasting-based approach is general.

### Unveiling IPv6 Scanning Dynamics

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3749221) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3749221)

Hammas Bin Tanveer (University of Iowa) et al. (Akamai, CAIDA/UCSD, MPI-INF, IPinfo, Walton Institute, MIT; kc Claffy, UC San Diego)

- **Why**: IPv6's address space was supposed to make scanning moot; this dataset shows a sustained two-year increase in IPv6 scanning anyway, and characterizes how scanners actually work — directly relevant to your network-security interests and to any assumption that v6 reachability implies obscurity.
- **What**: The largest-ever IPv6 proactive telescope, deployed in a production ISP, collecting 600M+ unsolicited packets from ~1.9k ASes over 10 months. The paper characterizes scan sources, evaluates five defense-relevant features across the stack, and reverse-engineers scanner strategies (from abstract only).
- **How**: Proactive vantage points that attract scan traffic (telescope infrastructure) plus longitudinal measurement and source/strategy classification across the dataset.
- **Where applicable**: IPv6 security posture generally — informing whether v6-only services can rely on address obscurity (spoiler: decreasingly), rate limiting, and scan-detection design. Measurement done in a production ISP but findings generalize to v6 deployments broadly.

### AraOptical System and Testbed for Long-Range, High-Capacity FSOC in Rural Wireless X-Haul Networks

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768986) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768986)

Md Nadim (Iowa State University) et al. (UC Irvine, Ohio State; Hongwei Zhang, Iowa State)

- **Why**: This is free-space optical x-haul — physical-layer transport work with real 10+ km field deployment, quantitative scintillation/weather characterization, and a publicly available testbed and dataset. Given your optics and DC/WAN-interconnect focus, this is the conference's main physical-optics presence.
- **What**: R-Optical, a first-of-its-kind 10+ km terrestrial FSOC x-haul system, permanently deployed as a public research testbed. Demonstrated 2.92 Gbps on a single channel, with a path to 160 Gbps aggregate via 16 channels of 10G SFP+ and multi-Tbps potential with 100G/400G coherent transceivers; also quantifies scintillation and weather impact on long-range FSOC (from abstract only).
- **How**: Optimized COTS components (feedback-controlled LNAs, router-compatible transceivers), a novel multi-level auto-alignment algorithm for telescope pointing, and a software framework with custom APIs for real-world experimentation.
- **Where applicable**: Rural x-haul and broadband backhaul, not datacenter interconnect — but the deployment-lessons (alignment, sun noise, weather fades at 10 km) and the open measurement data are valuable reference material for anyone evaluating FSOC's maturity. US rural-deployment context; COTS-based, so components are obtainable.

## Wildcard

### SpectraCert: A Hierarchical System for Dynamic Spectrum License Enforcement

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768980) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768980)

Ryan W. West; Dustin Maas; Jacobus Van der Merwe; David M. Johnson (University of Utah)

- **Why**: This is PKI and X.509-style hierarchical certificate derivation applied to a physical resource — spectrum. As someone working identity, you'll recognize the pattern (delegatable, revocable, attestable authority enforced by a trusted module in the endpoint) playing out in an entirely new domain, which is a sharp lens on how far the delegation-certificate model can stretch.
- **What**: A dynamic, PKI-based system for spectrum sharing: entities receive "spectracerts" — certificates encoding allowed frequencies, times, geographies, power limits, expirations — derived from parent spectracerts with increasingly limited rights. Trusted Modules inside SDRs validate certificate chains and revocations, and physically enforce radio configuration to match (from abstract only).
- **How**: Certificate hierarchy from Spectrum-Authorized Entities down to individual radios; automatic revocation/replacement propagation across the hierarchy; integration with the OpenZMS spectrum management system; spectracerts also double as verification tokens for interference/occupancy attestations.
- **Where applicable**: Regulatory/spectrum-sharing contexts (dynamic spectrum access, SDR certification). Nothing deployable for you directly, but the enforce-in-endpoint-trusted-hardware pattern is one to watch as it rhymes with SPIFFE-style workload identity for physical infrastructure.

### An Empirical Analysis of the Nostr Social Network

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768994) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768994)

Yiluo Weil; Gareth Tyson (HKUST Guangzhou)

- **Why**: Nostr is a rare production system where identity is purely cryptographic (public keys and signatures, no central accounts) and storage is delegated to interchangeable relays — a live, at-scale experiment in key-based decentralized identity and data replication, which touches your identity interests from an angle you wouldn't have searched for.
- **What**: The first large-scale study of Nostr, covering relays and post-replication strategies across 100M+ posts. Findings: Nostr achieves better decentralization than Fediverse alternatives, but relay availability is a persistent problem driven by free-to-use relays' financial unsustainability, and aggressive replication improves censorship resistance at significant overhead. The authors propose and evaluate two improvements to trim replication overhead without hurting availability (from abstract only).
- **How**: Longitudinal measurement of relay ecosystems and replication behavior, followed by data-driven evaluation of proposed mitigation strategies.
- **Where applicable**: Decentralized/peer infrastructure design — the relay-sustainability and replication-cost findings are early evidence on the operational economics of key-centric, server-agnostic architectures.

### T(SN)-Ray: Gauging TAS and PSFP Delays of TSN Switches for Predictable Deterministic Networking

**Links:** [Abstract](https://dl.acm.org/doi/10.1145/3768996) · [Paper](https://dl.acm.org/doi/pdf/10.1145/3768996)

Manuel Eppler (Siemens AG, University of Tuebingen) et al. (University of Tuebingen, Siemens AG, University of Kassel)

- **Why**: A black-box method to measure what switch datasheets never tell you: per-switch internal forwarding delays at nanosecond granularity — the numbers you need before you can compute valid TAS gate schedules or PSFP configurations at all. As switching-hardware work with an industrial-metrology flavor, it's a methodology you'd want your vendors measured with.
- **What**: A delay model for TSN switches plus a measurement methodology to quantify its parameters on any given switch — the first known approach to deriving these delays. Applied to switches from Kontron and Relyum, it reveals significantly different operational delays between vendors (from abstract only).
- **How**: Black-box gauging: carefully timed probe traffic isolates the components of switch-internal delay (queueing, gate mechanics, forwarding), fitting them to the proposed model without switch cooperation.
- **Where applicable**: Time-Sensitive Networking deployments — industrial Ethernet, automotive, and increasingly deterministic-Ethernet in DCs. The methodology is general (any TSN switch); the measured values are per-vendor/per-product and the results show you cannot port schedules between switches without re-gauging.

## Themes

- **Hardware–software co-design is back in the datapath**: Taurus (FPGA NIC CC), ASNI (SmartNIC interfaces), SwitchNIC (switch + ARM), Exp-PIFO (Tofino scheduling), and the RNIC crypto paper all push functionality to the edge silicon while conceding that software must orchestrate it — the field has stopped treating offload as all-or-nothing.
- **Honest negative and structural results carry weight**: the eBPF limits paper and the best-paper cloud-routing tradeoff (control/availability/stability — pick two) both shape design reasoning more than another benchmark win would; expect these to be cited as constraint arguments in architecture reviews.
- **Measurement of things vendors don't document**: T(SN)-Ray on switch-internal delays, NetFridgeS on pipeline energy, IPv6 telescopes on scanners, and QUIC backscatter analysis all extract ground truth about production systems from outside — a strong methodological streak this cycle.
- **Kubernetes/network security is maturing from cluster-hardening to network-config-hardening**: Inside Job's 634 misconfigurations across 287 real deployments mark lateral movement via network config as a measurable, disclosed, fixed-in-practice problem class.
- **BGP-based operations get verification and inference tooling**: MEV verifies overlay/underlay control planes on a nationwide network; TRIX infers transient reachability violations passively — both target the operational middle ground between simulators and active probing.
- **Physical/field-deployed systems work remains a first-class citizen**: long-range FSOC x-haul, TSN delay gauging, and 400G DC congestion control in production reflect CoNEXT continuing to publish on deployed hardware and physics, not just software layers.
