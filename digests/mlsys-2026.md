<!--
conference: MLSys 2026
source_url: https://mlsys.org/virtual/2026/papers.html?filter=titles
generated: 2026-11-04
registry_key: mlsys-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# MLSys 2026

*A note on sourcing: enrichment fetches were unsuccessful for this program — OpenReview pages sat behind a bot-verification wall and the MLSys poster pages carry only a title and author. Every write-up below is therefore grounded in the abstract as printed in the program (marked where applicable), and the three poster items have no abstract at all, which is flagged explicitly.*

## Core

### fabric-lib: RDMA Point-to-Point Communication for LLM Systems

**Links:** [Abstract](https://openreview.net/forum?id=SjVa05wEiY) · [Paper](https://openreview.net/pdf?id=SjVa05wEiY)

Nandor Licker, Kevin Hu, Vladimir Zaytsev, Lequn Chen (Perplexity AI, per the paper's open-source repository)

- **Why**: Disaggregated inference, MoE expert routing, and async RL fine-tuning all need flexible point-to-point RDMA, not just collectives — but today's implementations are locked to specific NICs. This is the clearest statement of the problem at the point where RoCE fabrics and LLM serving actually meet, and it ships as open source.
- **What**: A NIC-abstraction library that exposes uniform one-sided `WriteImm` operations across heterogeneous NICs, demonstrated at 400 Gbps on both NVIDIA ConnectX-7 and AWS EFA, and proven through three production use cases: KV-cache transfer for disaggregated inference, RL weight sync (1.3 s for trillion-parameter models), and MoE dispatch/combine that beats DeepEP decode latency on ConnectX-7 — with the first viable EFA latencies (from abstract only).
- **How**: Bridges common NIC functionality behind one interface; an `ImmCounter` primitive provides completion notification without assuming transport ordering; multiple NICs per GPU are managed transparently. It complements collectives rather than replacing them.
- **Where applicable**: Any RoCEv2 or EFA environment with point-to-point LLM traffic. The headline numbers are specific to ConnectX-7 and AWS EFA, and the MoE comparison is against DeepEP — but the portability argument and the code (pplx-garden on GitHub) are broadly usable.

### SAKURAONE: An Open Ethernet–Based AI HPC System and Its Observed Workload Dynamics in a Single-Tenant LLM Development Environment

**Links:** [Abstract](https://openreview.net/forum?id=n7o6C3p3wk) · [Paper](https://openreview.net/pdf?id=n7o6C3p3wk)

Fumikazu Konishi, Yuuki Tsubouchi, Hirofumi Tsuruta (SAKURA Internet Research Center)

- **Why**: A top-100 TOP500 system built on a fully open networking stack — 800 GbE, SONiC, RoCEv2 — is the strongest public existence proof yet that vendor-neutral Ethernet fabrics scale to frontier LLM training. For anyone evaluating SONiC/white-box options for AI clusters, this matters more than another InfiniBand case study.
- **What**: A 100-node managed HPC cluster (8× H100 per node, 2 PB all-flash Lustre) on a rail-optimized 800 GbE leaf–spine fabric with RoCEv2 and SONiC, ranked 49th in ISC 2025 TOP500 (33.95 PFLOP/s HPL, 339.86 PFLOP/s FP8 HPL-MxP) — the only top-100 system using a fully open network stack. The paper also reports single-tenant workload dynamics: small jobs dominate by count, a few large jobs consume most GPU-hours, and usage shifted from large-scale training to mid-scale iterative refinement over the project's life (from abstract only).
- **How**: Built on the SAKURA KOKARYOKU PHY bare-metal GPU platform; rail-optimized leaf–spine topology; open control and data plane end to end.
- **Where applicable**: The fabric architecture and its measured scalability are broadly relevant to Ethernet-for-AI decisions. The workload observations are specific to one research project's exclusive use of the cluster — treat them as a single-tenant data point, not a general cloud workload distribution.

### Blueprint, Bootstrap, and Bridge: A Security Look at NVIDIA GPU Confidential Computing

**Links:** [Abstract](https://openreview.net/forum?id=t9RDCO1aL7) · [Paper](https://openreview.net/pdf?id=t9RDCO1aL7)

Zhongshu Gu, Enriquillo Valdez, Salman Ahmed, Julian James stephen, Michael Le, Hani Jamjoom, Shixuan Zhao, Zhiqiang Lin (affiliations not listed in the program)

- **Why**: GPU confidential computing is on the path to becoming table stakes for regulated AI workloads, and it is a proprietary, hard-to-inspect black box. A reverse-engineered architecture view plus disclosed vulnerabilities is exactly what a security PM needs to reason about the CPU–GPU trust boundary and what attestation actually covers.
- **What**: A security analysis of NVIDIA GPU-CC that reconstructs the system: its specialized architectural engines, the bootstrap process that coordinates hardware and software protections, and targeted experiments testing whether data transfers along different paths stay protected across the CPU–GPU bridge under GPU-CC's own threat model. All findings were responsibly disclosed to NVIDIA PSIRT (from abstract only).
- **How**: System reconstruction from the outside in, then directed experiments against specific transfer paths at the trust-domain boundary.
- **Where applicable**: NVIDIA-specific by definition (GPU-CC on current NVIDIA silicon), and the concrete findings apply to that stack's current generation. The methodology — treating a vendor's confidential-computing claims as something to be independently verified rather than trusted — generalizes to any TEE/hardware-root-of-trust evaluation.

### ADR: AN AGENTIC DETECTION SYSTEMFORENTERPRISE AGENTIC AI SECURITY

**Links:** [Abstract](https://openreview.net/forum?id=7B91Naeszw) · [Paper](https://openreview.net/pdf?id=7B91Naeszw)

Chenning Li, Pan Hu, Justin Xu, Baris Ozbas, Olivia Liu, Caroline Van, Manxue Li, Wei Zhou, Mohammad Alizadeh, Pengyu Zhang, KK Sriramadhesikan, Ming Zhang (deployed at Uber, per the paper; affiliations not listed in the program)

- **Why**: AI agents speaking MCP are entering enterprises with almost no dedicated security tooling — EDR sees file writes, not prompts, reasoning, or the causal chain from intent to execution. This is one of the first production-proven detection-and-response systems for agentic AI, sitting squarely at the intersection of network security and the emerging agentic-identity problem.
- **What**: A three-part system: an ADR Sensor for high-fidelity agentic telemetry (prompts, reasoning, causal chains), an Explorer for pre-deployment red teaming and hard-example generation, and a two-tier Detector that combines fast triage with context-aware reasoning to keep LLM inference costs down. Deployed at Uber for 10+ months across 7,200+ hosts and 10,000+ agent sessions daily; surfaced hundreds of credential exposures (97.2% precision). Includes ADR-Bench (302 tasks, 17 techniques, 133 MCP servers), where it detects 67% of attacks with zero false positives, beating three SOTA baselines by 2–4× F1 (from abstract only).
- **How**: EDR-style instrumentation applied to agent sessions, plus a cost-aware two-tier detection pipeline and a systematic red-team loop for generating hard examples.
- **Where applicable**: Enterprise MCP deployments. The production numbers are Uber-specific, but the architecture, the benchmark, and the credential-exposure findings generalize — and the telemetry gap it names (agents invisible to host-based tooling) is universal.

### NEST: Network- and Memory-Aware Device Placement for Distributed Deep Learning

**Links:** [Abstract](https://openreview.net/forum?id=jpIoO2zSKA) · [Paper](https://openreview.net/pdf?id=jpIoO2zSKA)

Irene Wang, Vishnu Venkata, Arvind Krishnamurthy, Divya Mahajan (affiliations not listed in the program)

- **Why**: Device placement is where ML frameworks and the physical fabric actually meet. Most placement tools treat the network as an afterthought and memory as a post-hoc fix; NEST makes topology, allreduce latency, and memory feasibility first-class joint constraints — the co-design point a fabric-owning PM cares about.
- **What**: A placement framework that unifies model parallelism (tensor, expert, sequence, context — composed with pipeline, data, and ZeRO), explicit allreduce latencies over hierarchical or arbitrary network topologies, and per-device memory/compute profiles, solved via structured dynamic programming. Up to 2.43× higher throughput over SOTA baselines across diverse hardware and networks; open source (from abstract only).
- **How**: DP over operator graphs annotated with per-op parallelism configurations and measured network latencies, jointly optimizing co-location, communication cost, and memory feasibility rather than patching feasibility after placement.
- **Where applicable**: General technique, not tied to one operator's fabric — but its quality depends on accurate allreduce-latency and memory profiles for your specific network. Most useful as a foundation for co-designing parallelization strategies with datacenter interconnects; needs real fabric measurements as input.

### SHIP: SRAM-Based Huge Inference Pipelines for Fast LLM Serving

**Links:** [Abstract](https://openreview.net/forum?id=IZaXDwDtL1) · [Paper](https://openreview.net/pdf?id=IZaXDwDtL1)

Andrew Bitar, Aravind Vayalapra, Baorui Zhou, et al. (Groq, per the paper — the deployment studied is Groq's public cloud)

- **Why**: A production counterpoint to HBM-based GPU serving: SRAM-resident weights eliminate the decode memory-bandwidth bottleneck, and the system runs at hundreds of billions of tokens daily. The interconnect story — a synchronous, low-diameter network scaling to thousands of chips — is a live example of topology choices driving serving latency.
- **What**: A review of Groq's first-generation SRAM-based inference pipelines: (1) a synchronous low-diameter interconnect enabling low-latency scaling across thousands of chips, (2) serving optimizations under tight memory capacity, and (3) large-pipeline designs that sustain efficiency and latency across varying prefill-to-decode ratios and context lengths, delivering state-of-the-art latency (from abstract only).
- **How**: Model weights and KV state live in SRAM spread across a chip fabric; deterministic, synchronous pipelining keeps communication off the critical path.
- **Where applicable**: Groq-specific silicon and interconnect — this is one vendor's architecture, not a technique you can adopt. But as a data point on how scale-up fabric topology and memory placement shape the throughput–latency frontier, it is directly relevant to anyone comparing interconnect strategies for inference.

### A Lightweight High-Throughput Collective-Capable NoC for Large-Scale ML Accelerators

**Links:** [Abstract](https://openreview.net/forum?id=VDuS8N9RCx) · [Paper](https://openreview.net/pdf?id=VDuS8N9RCx)

Luca Colagrande, Lorenzo Leone, Chen Wu, Tim Fischer, Raphael Roth, Luca Benini (affiliations not listed in the program)

- **Why**: With thousands of compute elements per die, on-chip fabrics now face the same problems as DC fabrics — collective offload, multicast, in-network reduction, buffer/area budgets. This is fabric design and in-network compute at the silicon level, and the boundary between NoC and scale-up interconnect is exactly where the field is heading.
- **What**: A lightweight NoC supporting barrier synchronization, scalable high-bandwidth multicast, and in-network reduction, co-designed for next-generation ML accelerators. Introduces Direct Compute Access (DCA), giving the interconnect direct access to the cores' computational resources for in-network reduction at a 16.5% router area overhead. Measured 2.9× and 2.5× geomean speedups on multicast and reduction (1–32 KiB), and up to 2.1× estimated end-to-end GEMM performance vs a unicast-only NoC baseline (from abstract only).
- **How**: DCA lets the fabric itself perform reductions using core compute resources, keeping communication off the critical path in GEMM-heavy workloads.
- **Where applicable**: Applies to accelerator ASIC design, not to retrofitting existing clusters — and the end-to-end GEMM gains are estimates from architectural simulation rather than silicon measurements. The in-network-reduction tradeoff (area vs throughput), however, is a broadly transferable design lesson.

### ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler

**Links:** [Abstract](https://openreview.net/forum?id=tYHWS7YPof) · [Paper](https://openreview.net/pdf?id=tYHWS7YPof)

Bohua Zou, Debayan Roy, Dhimankumar Airao, Weihao Xu, Binqi Sun, Yutao Liu, Haibo Chen (affiliations not listed in the program)

- **Why**: eBPF is in your core stack, and this paper shows its reach extending beyond networking into runtime-level observability of LLM inference — with under 4% overhead and zero source modification. The pattern (dynamic probes on runtime functions, rich derived views) transfers to other "black-box runtime, need operator-level visibility" problems.
- **What**: A fine-grained, non-intrusive profiling framework for LLM inference engines, focused on resource-constrained edge devices and exemplified by llama.cpp, exposing operator-level time, memory-vs-compute boundedness, MoE routing behavior, and operator offloading, rendered as operator graphs, timelines, and hardware-counter trends (from abstract only).
- **How**: eBPF probes dynamically attached to runtime functions across multiple layers without recompilation; collected traces are transformed into visualizations of operators, graphs, and counter trends.
- **Where applicable**: llama.cpp-class CPU/edge inference runtimes on Linux — this is not a GPU-cluster profiler, and the fidelity claims are tied to that runtime architecture. The eBPF technique itself is broadly portable.

### DreamDDP: Accelerating Low-Bandwidth Geo-Distributed LLM Training with Layer-wise Partial Synchronization

**Links:** [Abstract](https://openreview.net/forum?id=cnvw0mbZQp) · [Paper](https://openreview.net/pdf?id=cnvw0mbZQp)

Zhenheng Tang, Zichen TANG, Junlin Huang, Xinglin Pan, Rudan Yan, Yuxin Wang, Amelie Zhou, Shaohuai Shi, Xiaowen Chu, Bo Li (affiliations not listed in the program)

- **Why**: Geo-distributed training is the workload that will stress (and justify) DC-to-DC WAN interconnects. This paper quantifies how much of that WAN bottleneck can be clawed back on the ML side — directly relevant to capacity planning for AI-over-WAN before you buy bandwidth.
- **What**: A training framework that decouples model synchronization layer-wise: instead of synchronizing the whole model every N iterations (Local SGD) or every iteration (S-SGD), only a subset of layers is synchronized per iteration. Delivers 1.49×–3.91× speedups over leading baselines on 32 GPUs across ResNet-18/50, GPT-2, and Llama-2, with convergence rates theoretically comparable to S-SGD (from abstract only).
- **How**: Layer-wise partial synchronization enables overlapping parameter sync with computation without extra GPU memory; fine-grained layer-wise profiling drives the communication/computation schedule.
- **Where applicable**: Low-bandwidth geo-distributed data-parallel training. Evaluated at modest scale (32 GPUs) — frontier-scale behavior is unproven. It is an ML-side technique that complements, not replaces, WAN capacity planning; its value to a network PM is as a signal of what traffic geo-distributed training will and won't generate.

## Adjacent

### TokenWeave: Efficient Compute-Communication Overlap for Distributed LLM Inference

**Links:** [Abstract](https://openreview.net/forum?id=rh2Ylffkq6) · [Paper](https://openreview.net/pdf?id=rh2Ylffkq6)

Raja Gond, Nipun Kwatra, Ramachandran Ramjee (Microsoft, per the paper's open-source repository)

- **Why**: Tensor-parallel AllReduce costs ~20% even over NVLink, and — usefully documented here — none of the major serving engines enable overlap by default because it backfires at small token counts. This paper explains why and fixes it.
- **What**: The first system enabling efficient compute–communication overlap for tensor-parallel inference at batch sizes as small as 1024 tokens: up to 1.28× lower latency and 1.19× higher throughput across models and workloads on an 8×H100 DGX, in several settings beating an equivalent model with all communication removed. Open source (from abstract only).
- **How**: Identifies RMSNorm as the overlooked fusion partner and implements a fused AllReduce–RMSNorm kernel that exploits the NVSHARP/Multimem hardware feature, using only 2–8 SMs for communication on Hopper/Blackwell-class GPUs.
- **Where applicable**: Requires modern NVIDIA GPU interconnects (NVLink + NVSHARP/Multimem on Hopper/Blackwell) — the mechanism is silicon-specific. The diagnosis of why overlap is off by default in vLLM/SGLang/TensorRT-LLM is broadly instructive.

### GUARD: SCALABLE STRAGGLER DETECTION AND NODE HEALTH MANAGEMENT FOR LARGE-SCALE TRAINING

**Links:** [Abstract](https://openreview.net/forum?id=JFEwQ821MS) · [Paper](https://openreview.net/pdf?id=JFEwQ821MS)

guanliang liu, Abhinandan Patni, congzhu lin, et al. (affiliations not listed in the program; deployed on large-scale foundation-model pretraining)

- **Why**: NCCL tests and GPU burn-ins catch fail-stop, not fail-slow — and on multi-month, tens-of-thousands-of-GPU runs, silent stragglers quietly eat efficiency. This is operational health management for training fleets, and the approach transfers to any large fleet.
- **What**: A system combining lightweight online performance monitoring during training with an offline node-sweep mechanism that qualifies nodes before production admission. In production: up to 1.7× improvement in mean FLOPs utilization, run-to-run training-step variance reduced from 20% to 1%, higher MTTF, and reduced debugging overhead (from abstract only).
- **How**: Continuous workload-level performance signals (not synthetic micro-tests) detect both acute failures and long-running degradation; systematic sweeps pre-qualify nodes.
- **Where applicable**: The deployment is a large-scale pretraining cluster (org not fully specified in the program), so exact gains are fleet-specific. The core lesson — workload-level signal beats synthetic health checks for fail-slow detection — is broadly applicable.

### Unleashing Scalable Context Parallelism for Foundation Models Pre-Training via FCP

**Links:** [Abstract](https://openreview.net/forum?id=MPVycRsIn6) · [Paper](https://openreview.net/pdf?id=MPVycRsIn6)

Yilong Zhao, Xiaonan Nie, Kan Zhu, et al. (affiliations not listed in the program)

- **Why**: Context parallelism over variable-length training data wastes fabric capacity — over-sharding short sequences, or imbalanced bin-packing of long and short ones. FCP relaxes the rigid-ring assumption, which is a scheduling/communication co-design relevant to anyone provisioning collective fabrics.
- **What**: A flexible context-parallelism paradigm that shards and schedules sequences at block-level granularity, achieving near-linear scalability to 256 GPUs and 1.13×–2.21× improvement in attention MFU (from abstract only).
- **How**: Block-level sharding enables arbitrary peer-to-peer communication topologies (not just rings) and bin-packing of blocks from short and long sequences for balanced, communication-efficient placement.
- **Where applicable**: Foundation-model pretraining with heterogeneous sequence lengths. Evaluated at up to 256 GPUs — mid-scale by today's standards — so frontier-scale behavior is extrapolated.

### MLCommons Chakra: Advancing Performance Benchmarking and Co-design using Standardized Execution Traces

**Links:** [Abstract](https://openreview.net/forum?id=s2WcSv2Hzt) · [Paper](https://openreview.net/pdf?id=s2WcSv2Hzt)

Srinivas, Andrey Balogh, Brad B, et al. (MLCommons-led effort with industry participation from NVIDIA, AMD, Meta, Keysight, HPE, and others, per the paper)

- **Why**: There is no portable, vendor-neutral way to characterize distributed AI workloads' behavior on a fabric. Chakra's standardized execution-trace format is becoming the interchange layer for AI-cluster benchmarking and co-design — effectively the telemetry standard to watch.
- **What**: An open ecosystem whose core is Chakra Execution Traces (ETs): graph-based representations of compute, memory, and communication operations with data/control dependencies, timing, and resource constraints, plus tools for collection, analysis, generation, and replay into simulators and emulators. Includes analysis of traces from production AI clusters and real-world case studies; adopted by MLCommons (from abstract only).
- **How**: Workload traces are captured as interoperable graphs, then fed to simulators/emulators/replay tools for performance prediction and SW–HW co-design without needing the original cluster.
- **Where applicable**: Cross-vendor by construction — the whole point is portability across NVIDIA, AMD, and other stacks. Adoption is still growing; value scales with ecosystem uptake.

### CSLE: A Reinforcement Learning Platform for Autonomous Security Management

**Links:** [Abstract](https://openreview.net/forum?id=QGuRWjFsnm) · [Paper](https://openreview.net/pdf?id=QGuRWjFsnm)

Kim Hammar (affiliation not listed in the program)

- **Why**: RL for security has been stuck in toy simulators for years. CSLE's emulate→model→simulate→refine loop is a serious attempt to bridge toward operational systems, and its use cases (flow control, replication control, segmentation control, recovery control) are network-adjacent controls.
- **What**: A platform pairing an emulation system that replicates target components in a virtualized environment (used to gather measurements/logs and identify an MDP system model) with a simulation system where security strategies are learned, then validated back in emulation. Demonstrated across four use cases with near-optimal management in an environment approximating an operational system (from abstract only).
- **How**: Emulation-grounded system identification → simulation-based policy learning → emulation-based refinement, closing the sim-to-real gap that plagues pure-simulation RL security work.
- **Where applicable**: Research platform, not a production control loop — "approximates an operational system" is the honest limit. Interesting for the segmentation/recovery control formulations and the methodology, not for deployable policies.

### Optimizing Deployment Configurations for LLM Inference

**Links:** [Abstract](https://openreview.net/forum?id=gEbKQeIdxB) · [Paper](https://openreview.net/pdf?id=gEbKQeIdxB)

Sungmin Cho, Jaewon Lee, Chunqiang Tang, et al. (Meta, serving the Llama family to ~1B monthly active users, per the paper)

- **Why**: Production experience from one of the largest inference fleets in existence, systematically mined for configuration lessons — the operational counterpart to NEST-style placement search, from the team living with the results.
- **What**: A systematic approach analyzing millions of deployment configurations across hardware (H100, H200, MI300X), parallelism strategies (tensor, pipeline, expert, context, data), and runtime choices (continuous batching vs prefill–decode disaggregation) under SLO constraints. Shares lessons on runtime trade-offs, the phase-specific nature of parallelism strategies, hardware heterogeneity, scaling behaviors, and MoE system implications (from abstract only).
- **How**: Large-scale design-space search with workload-specific SLO constraints on production traffic.
- **Where applicable**: Meta-specific fleet, workloads, and SLOs — the specific optima do not transfer. The structural lessons (phase-specific parallelism, heterogeneous hardware opportunity) do.

### Beyond the Buzz: A Pragmatic Take on Inference Disaggregation

**Links:** [Abstract](https://openreview.net/forum?id=NqC5tcBsa0) · [Paper](https://openreview.net/pdf?id=NqC5tcBsa0)

Tiyasa Mitra, Ritika Borkar, Nidhi Bhatia, et al. (NVIDIA, per the paper's focus on NVIDIA Dynamo)

- **Why**: Prefill–decode disaggregation is heavily hyped but lightly deployed at scale. This is billed as the first systematic large-scale study, across hundreds of thousands of design points — useful for calibrating expectations.
- **What**: Findings: disaggregation is most effective for prefill-heavy traffic patterns and larger models; dynamic rate matching and elastic scaling are critical to reaching the Pareto frontier of throughput vs interactivity (from abstract only).
- **How**: Systematic evaluation of a huge design space across diverse workloads and hardware configurations, tied to the deployment flexibility of NVIDIA Dynamo.
- **Where applicable**: Multi-node NVIDIA inference deployments; vendor-authored (NVIDIA), so weight accordingly — though the evaluation-driven approach and the prefill-heavy-traffic finding are consistent and actionable.

### Sparing Strategies to Minimize Reliability Impact On Large Training Jobs

**Links:** [Abstract](https://openreview.net/forum?id=18jPgte2tM) · [Paper](https://openreview.net/pdf?id=18jPgte2tM)

Kevin Quirk, Matthew Lennie, Ehsan K. Ardestani, et al. (Meta, per the paper's framing around Meta's AI clusters)

- **Why**: Sparing — pre-allocated spare compute that replaces failed components — directly trades capex against goodput on multi-month training runs. Closed-form sizing guidance for that tradeoff is rare and welcome.
- **What**: An analytical framework with closed-form expressions for choosing sparing strategy — compute block size, number of spare blocks, spare GPU trays — cross-validated by simulation, and applied in Meta's hyperscale infrastructure to inform fault-tolerance, downtime, and goodput decisions (from abstract only).
- **How**: Analytical modeling of failure/replacement dynamics, plus a simulation component for validation; yields first-order production recommendations.
- **Where applicable**: The framework is generally formulated, but the optimal sparing parameters are strongly fleet-specific (Meta's failure rates, tray topology, job sizes). Use the method and the first-order rules, not Meta's numbers.

### Designing Communication-Efficient AI Systems: An Interconnect-Aware HPC Perspective

**Links:** [Abstract](https://mlsys.org/virtual/2026/poster/10169)

Jinghan Yao (poster; affiliation not listed in the program)

- **Why**: The title places it squarely in the interconnect/co-design theme running through this conference, and the poster format suggests early or in-progress work worth a hallway conversation.
- **What**: Not assessable from the program — no abstract is provided, and the MLSys poster page lists only the title and author. By title, it concerns designing AI systems that account for the characteristics of the underlying interconnect, from an HPC perspective.
- **How**: Unknown from available material.
- **Where applicable**: Unknown from available material. Flagged here so the omission is visible rather than papered over; check the poster or ask the author directly.

### Communication-Efficient Distributed Inference for Transformer Models via Vector Quantized Context

**Links:** [Abstract](https://mlsys.org/virtual/2026/poster/10180)

Xiao Liu, Lijun Zhang, Deepak Ganesan, Hui Guan (poster; affiliations not listed in the program)

- **Why**: The title signals an approach to cutting cross-node inference traffic by quantizing the KV context exchanged between pipeline stages — i.e., reducing bytes on the fabric rather than adding bandwidth.
- **What**: Not assessable from the program — no abstract is provided, and the MLSys poster page lists only title and authors. By title, it applies vector quantization to the context communicated in distributed transformer inference.
- **How**: Unknown from available material.
- **Where applicable**: Unknown from available material — likely relevant to multi-node inference fabrics, but that inference is from the title alone. Worth a hallway stop if quantization-for-communication is on your roadmap.

### LearnedCache: An eBPF-Integrated Perceptron-Based Eviction Policy for the Linux Page Cache

**Links:** [Abstract](https://mlsys.org/virtual/2026/poster/10179)

Zejia Qi (poster; affiliation not listed in the program)

- **Why**: Two of your interests in one title: eBPF as a safe extension mechanism for kernel policy, and learned replacement decisions — here applied to the Linux page cache rather than a network cache, but the architecture question (can you wire a learned policy into kernel hot paths via eBPF without killing performance?) is the same one for LRU-vs-learned eviction in CDN caches, connection tracking, and flow caches.
- **What**: Not assessable from the program — no abstract is provided, and the MLSys poster page lists only the title and author. By title: a perceptron-based (learned) eviction policy for the Linux page cache, integrated with eBPF.
- **How**: Unknown from available material.
- **Where applicable**: Unknown from available material; by construction it is Linux-kernel-specific, and the interesting question for you is the eBPF-integration pattern, not page caching per se.

## Wildcard

### Rethinking Open Source Contribution in the Age of AI Agents

**Links:** [Abstract](https://mlsys.org/virtual/2026/invited-talk/10000)

Roger Wang (vLLM core maintainer, per the talk description)

- **Why**: Not a networking talk, but a maintainer's-eye view of what AI-generated contribution pressure is doing to the maintenance economics of critical infrastructure — and vLLM is production LLM-serving infrastructure that the rest of this program depends on. If you run an open-source project or consume one, this is the operational reality arriving at your doorstep.
- **What**: A core maintainer's account of the surge of AI-generated PRs in vLLM: the cost of producing a plausible PR has collapsed while review cost has not; PRs that look correct but miss design intent; fixes that paper over deeper issues. Not anti-AI — agents are now part of how vLLM gets built — but the argument is that human leverage has shifted from producing code toward understanding systems, picking the right problems, and owning what ships (from abstract only).
- **How**: Concrete examples from vLLM's day-to-day maintainer experience, plus practical guidance for new contributors and for maintainers of critical infrastructure.
- **Where applicable**: Any OSS project, especially infrastructure projects with high PR volume and shallow review capacity.

### REPARO: LOSS-RESILIENT GENERATIVE CODEC FOR VIDEO CONFERENCING

**Links:** [Abstract](https://openreview.net/forum?id=GaBGzA7fpe) · [Paper](https://openreview.net/pdf?id=GaBGzA7fpe)

Tianhong Li, Vibhaalakshmi Sivaraman, Pantea Karimi, Lijie Fan, Mohammad Alizadeh, Dina Katabi (affiliations not listed in the program)

- **Why**: A genuinely surprising inversion of loss recovery: instead of adding redundancy (FEC) or retransmitting (impractical for real-time), *generate* the lost visual content conditioned on what did arrive. Whatever you think of the ethics of hallucinated pixels, it is a new point in the design space for real-time loss resilience.
- **What**: A video-conferencing framework where a generative model fills in missing frames or frame regions when packets are lost, conditioned on the data received so far and on learned priors of how people and objects appear and move. On public video-conferencing datasets it beats state-of-the-art FEC-based solutions on video quality (PSNR, SSIM, LPIPS) and freeze occurrence (from abstract only).
- **How**: Conditional generation over partially-received frames, exploiting the model's visual-world priors instead of parity redundancy.
- **Where applicable**: Real-time interactive video over lossy Internet paths. Research-stage, evaluated on public datasets rather than live conferencing at scale — but as a signal of where loss recovery could go beyond ARQ/FEC, it is worth ten minutes.

### SONAR: Benchmarking Topology and Collaboration in Decentralized Learning

**Links:** [Abstract](https://openreview.net/forum?id=4Bqg7Xyk5t) · [Paper](https://openreview.net/pdf?id=4Bqg7Xyk5t)

Joyce Yuan, Yichuan Shi, Abhishek Singh, et al. (affiliations not listed in the program)

- **Why**: It treats topology as a first-class, controllable variable — and finds sparse structured graphs (rings, tori) can match or beat dense ones at far lower communication cost. That finding rhymes directly with datacenter fabric intuition, even though the domain is peer-to-peer federated learning, not DC networks.
- **What**: A modular framework unifying communication, topology management, and fine-grained telemetry for topology-aware decentralized learning, enabling reproducible measurement of performance, communication, robustness, and privacy. Key findings: topology's impact amplifies with scale and data heterogeneity; sparse structured topologies sit on a better efficiency frontier than dense graphs; and it identifies "collaborator collapse," a systematic failure mode where similarity-based neighbor selection reduces diversity and degrades generalization (from abstract only).
- **How**: Controlled, reproducible evaluation across topologies under a common measurement harness spanning performance, communication, robustness, and privacy dimensions.
- **Where applicable**: Decentralized/P2P learning research settings, not datacenter fabrics — but the topology-efficiency results and the collaborator-collapse failure mode are conceptually portable to any system where participants choose communication partners adaptively.

## Themes

- **The fabric is the bottleneck**: across TokenWeave, fabric-lib, FCP, NEST, DreamDDP, the NoC paper, and SHIP, the dominant MLSys problem is moving data between compute elements — collectives, point-to-point RDMA, overlap, and topology-aware placement. Networking expertise has become the scarce input to AI systems.
- **Open stacks reaching frontier scale**: SAKURAONE proves 800 GbE + SONiC + RoCEv2 can land in the TOP500 top 100; fabric-lib abstracts NIC lock-in; Chakra standardizes traces across NVIDIA/AMD/Meta. Vendor-neutral options are moving from plausible to demonstrated.
- **Production experience reports with real numbers**: MLSys's industrial papers are unusually candid — Meta's deployment-configuration and sparing studies, Uber's ADR deployment, Groq's SHIP, and the GUARD fleet-health system all ship operational metrics, not just benchmarks. Treat the org-specific optima carefully, but the lessons transfer.
- **Security expanding to new surfaces**: GPU confidential computing (blueprint/bootstrap/bridge), enterprise agentic-AI detection via MCP telemetry (ADR), and RL-driven autonomous security management (CSLE) — the security frontier is following workloads into accelerators and agents, where existing EDR-style tooling is blind.
- **eBPF maturing beyond networking**: ProfInfer and LearnedCache both use eBPF as a safe, low-overhead mechanism for *non-network* kernel and runtime policy — observability and cache eviction — confirming eBPF's trajectory as a general kernel-extension platform.
- **Fail-slow beats fail-stop as the hard problem**: GUARD's straggler detection and Meta's sparing framework both target silent degradation and failure economics on long training runs — fleet reliability engineering is becoming a first-class systems topic, not an ops afterthought.
