<!--
conference: PyTorch Conference 2026
source_url: https://sessionize.com/api/v2/s2rq62nk/view/markdown
generated: 2026-11-04
registry_key: pytorch-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# PyTorch Conference 2026

PyTorch Conference is an ML-frameworks conference, not a networking one — but this cycle its systems track is dominated by exactly the problems a networking PM owns: RDMA transports, all-to-all traffic patterns, fabric failure handling, and the infrastructure governance of autonomous agents. The picks below are filtered through that lens. All write-ups are based on the session descriptions (the program pages carry no fuller papers or slides); speaker affiliations were confirmed from the session pages.

## Core

### Future of Distributed Communication in PyTorch: New APIs for Fault Tolerance, RDMA and Extensibility

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256220)

Tristan Rice, Kapil Sharma — Meta (PyTorch Distributed)

- **Why**: `torch.distributed` is the layer where every training collective maps onto your RDMA/Ethernet fabric. These API changes define how large jobs interact with the network — fault recovery, one-sided RDMA, and observability — and they are landing upstream for everyone.
- **What**: Five new capabilities being upstreamed from TorchComms into `torch.distributed`: `torch.distributed.reconfigure()` for live process-group reconfiguration after rank failures (no job restart); window APIs for one-sided RDMA put/get (zero-copy, aimed at RL workloads); composable hooks for tracing, logging, and NaN detection on all collectives across all backends; backends shipped as pip-installable wheels via entry_points; and cleaned-up backend interfaces for vendors. (from abstract only)
- **How**: Reconfiguration treats rank failure as a recoverable event rather than a job abort; window APIs expose peer memory directly; hooks make collective traffic observable in transit — the collective-layer analogue of flow telemetry.
- **Where applicable**: Broadly applicable — hardware-agnostic by design, with backend registration as the extension point. Zero claimed migration cost for existing users.

### Demo Theater: OpenCLIC: Open Communication for Distributed Inference

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1329720)

Jesse Treger

- **Why**: This is the Ultra Ethernet / connectionless-RDMA story arriving at the framework layer — squarely in physical-fabric territory. Its core argument is that MoE inference traffic (dynamic, many-destination all-to-all) is a structural mismatch for the connection-oriented RDMA transports most AI clusters run today.
- **What**: OpenCLIC, an open communication framework for connectionless networks, being integrated with vLLM. First use case is expert-parallel dispatch/combine; planned support for one-sided operations — KV-cache transfer, cache reuse/offload, and model-state movement. It separates framework interfaces, GPU kernels, and transport implementations so inference code isn't tied to one accelerator or network stack. (from abstract only)
- **How**: Built on Ultra Ethernet Transport, modeled on HPE Slingshot: no per-peer connections, improving multipathing, loss recovery, and scalability. The initial Slingshot implementation uses kernel-initiated OpenSHMEM so GPU code drives the network directly and the CPU stays out of the critical path.
- **Where applicable**: Initial implementation is HPE Slingshot-specific (HPC heritage), with the architecture positioned to extend across accelerators and fabrics. Demo-theater short format, and the program attaches a sponsored-content notice — expect a direction statement and early integration, not a full evaluation.

### Introducing NCCL Extensions: Communication Patterns for Modern AI

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257023)

Sreeram Potluri, Artem Polyakov — NVIDIA

- **Why**: NCCL is the dominant collective library on GPU fabrics; these domain extensions change what traffic patterns the library can express — MoE dispatch/combine and cross-mesh resharding — which is precisely the traffic your inference and RL-rollout fabrics will carry.
- **What**: Two NCCL domain extensions built on NCCL's Device APIs. NCCL-EP brings MoE dispatch and combine natively into NCCL — one automatically tuned API spanning latency-optimized decode and throughput-optimized training, with GPU-initiated RDMA and NVLink out of the box. NCCL-M2N does zero-copy resharding between disjoint device meshes, moving weight snapshots from trainers to inference replicas with no CPU staging. Performance results promised in the talk. (from abstract only)
- **How**: Specialized libraries inheriting NCCL's topology awareness and transport stack, but designed for customization, kernel fusion, and rapid prototyping of emerging patterns rather than classic collectives.
- **Where applicable**: NVIDIA-centric (NCCL ecosystem), and a vendor talk by NVIDIA architects — but it defines the de-facto API surface that open alternatives (OpenCLIC, TorchComms backends) will be measured against.

### Self-Healing PyTorch Training Through Live GPU Migration

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1322707)

Pavneet Ahluwalia, Gavin Cohen — Microsoft Azure (product) and Clockwork Systems

- **Why**: Link flaps and node failures are the physical-fabric failure modes you live with; this talk is about the job layer's counter-move — live migration instead of checkpoint-restart. The structural diagnosis (every step ends in a collective needing all ranks; a communicator can't be rebuilt around a missing peer) is the clearest statement of why training jobs are so brittle to fabric events.
- **What**: TorchPass, a training-failover system presented jointly by Together AI and Clockwork Systems: on link degradation it reroutes traffic; on GPU/memory/component failure it live-migrates the affected rank's device and communicator state to a spare and resumes from the same step. Their claim: a single checkpoint-restart failure burns 45–90 minutes of wall-clock across every GPU in the job. Live demo with injected link flaps and GPU failures; a decision framework for when live migration beats checkpoint-restart, plus a TCO framing for recovered goodput. (from abstract only)
- **How**: End-to-end system — monitoring, health checks, failover, rank-state migration — keeping a multi-node job in continuous forward progress.
- **Where applicable**: Vendor joint presentation with a product and TCO calculator attached; the companion demo talk reports a published TorchPass benchmark at Llama 4 Scout scale on 64 H200 GPUs, independently validated by SemiAnalysis. The mechanism assumes spare capacity and their product; the accountability/verification framing (does a failure resume from the same step, does throughput ever hit zero, can the claim be verified?) transfers to any fabric.

### Scaling Foundation Models: From Broken to Near-Linear Multi-Node Training

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256382)

Sheng Huang — Pinterest

- **Why**: A measured production case of "the network is the bottleneck" — GPUs busy waiting on cross-node traffic — with a diagnosis-first playbook that any operator of multi-node training can copy. The numbers are unusually honest (they show the broken starting point).
- **What**: Pinterest's TorchRec foundation-model training went from 5x *slower* at 2 nodes and 1.21x scaling at 4 nodes to 3.9x at 4 nodes (97.5% of ideal) and 7.5x at 8 nodes (93.75%) — by attacking cross-node All-to-All from distributed embedding lookups, identified via PyTorch Profiler and NCCL traces. (from abstract only)
- **How**: Reduce bytes on the wire (FP8 communication with FBGEMM), balanced TorchRec embedding sharding and reshaping, Distributed Checkpoint for load-time resharding, and a 2D parallel topology that keeps expensive All-to-All local and syncs replicas with AllReduce — i.e., topology designed around the slowest link.
- **Where applicable**: Pinterest production on AWS (EFA networking) — org- and cloud-specific in its specifics, but the playbook (measure, cut wire bytes, checkpoint portably, design around the slowest link) is broadly transferable.

### State-of-the-Art KV Transfer for Disaggregated LLM Serving in vLLM

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255023)

Nicolò Lucchesi (Mistral AI, vLLM maintainer), Sunita Nadampalli (Amazon), Zhanqiu Hu (Red Hat)

- **Why**: P/D disaggregation turns KV-cache transfer into a first-class network workload — bidirectional, latency-sensitive, stateful — that inference fabrics must now be designed for. This is the talk defining that transfer layer's requirements.
- **What**: Developments in vLLM's disaggregated serving stack: hybrid-model transfer with heterogeneous TP (Nemotron, Qwen3.5, DeepSeek-V4 with interleaved attention, KV compression, sliding windows), bidirectional KV transfer for agentic multi-turn sessions, a KV Push connector that reduces TTFT, and KV cache leases for reliability under failures and traffic spikes. On Nemotron, disaggregated P/D Pareto-dominates co-located serving across concurrency levels. (from abstract only)
- **How**: A flexible transfer interface generalizing across diverse cache layouts/sharding semantics and heterogeneous hardware (NVIDIA GPUs, AWS Trainium), composing with prefix caching and CPU offloading.
- **Where applicable**: vLLM-specific implementation but explicitly hardware-agnostic; the cross-vendor maintainer group suggests this becomes the reference interface. The hard constraint is cache-layout diversity across hybrid model architectures.

### Crossing the Divide: Co-Evolving Kubernetes and Ray for the AI Era

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256376)

Jago Macleod (Google, Kubernetes & GKE), Ion Stoica (Anyscale / UC Berkeley)

- **Why**: Kubernetes is where your cloud-native world has to absorb AI workloads; this session is the strategic map of how K8s and Ray are converging rather than fragmenting — directly relevant to K8s networking, scheduling, and resource-management roadmaps.
- **What**: A discussion of the co-evolution of Kubernetes and Ray into a unified open-source AI stack, spanning the PyTorch Foundation side (PyTorch, vLLM, Ray) and the CNCF side (Kubernetes, Envoy, OpenTelemetry, llm-d, containerd), with Google and Anyscale actively collaborating to prevent ecosystem fragmentation. (from abstract only)
- **How**: A jointly built, open, vertically integrated stack rather than parallel universes users must bridge themselves.
- **Where applicable**: Vision/direction session by engineering leadership — expect roadmap-level framing, not implementation detail. Useful for planning where AI workload requirements will pull K8s networking and scheduling next.

### Guardrails at the Infrastructure Layer: Sandboxing and governing Agentic AI in production

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1244699)

Sai Charan Teja Gopaluni, Aaresh Sharma — AWS

- **Why**: Agent governance is moving down from application-layer filters to infrastructure controls — K8s network policies, seccomp, runtime isolation — which is exactly the cloud-native security surface you work on. This is the zero-trust/microsegmentation conversation applied to agents.
- **What**: A BoF on infrastructure-level governance of agentic AI: container sandboxing for agent tool execution (network policies, seccomp profiles, runtime isolation on Kubernetes); GPU-level resource boundaries so one agent's runaway inference can't starve safety-critical workloads; and observability as governance — audit trails, token-level logging, kill switches for agentic chains. (from abstract only)
- **How**: Discussion format with a three-part agenda; no finished system or results — this is a community working session.
- **Where applicable**: Kubernetes-centric and generalizable across environments; a good venue to contribute a networking/identity practitioner's lens to an emerging practice.

### Compute, Latency, and Safety: Architecting Stateful Guardrails for Multi-Agent Workflows

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1251388)

Purva Chiniya — Amazon Ads

- **Why**: Securing inter-agent handoffs is the agentic analogue of service-to-service authentication and authorization — your workload/agentic-identity interest. The threat model here (untrusted data corrupting downstream agent privileges) is a delegation/privilege-escalation problem, not just an ML one.
- **What**: MLOps infrastructure for securing multi-agent systems at enterprise scale: continuous, stateful red-teaming pipelines built on the open-source SecRepoBench evaluation framework, and specialized low-latency SLMs deployed as deterministic orchestration guardrails — cross-agent payloads routed through high-speed checks that catch prompt injection ("indirect orchestration exploits") and operational drift without frontier-model cost or throughput collapse. (from abstract only)
- **How**: Small, fast validators placed in-line on the agent-to-agent data path, evaluating state changes continuously — architecturally the same shape as a sidecar policy check in a service mesh.
- **Where applicable**: Enterprise multi-agent deployments; abstract-level with no scale numbers given, so treat the effectiveness claims with caution. The enforcement pattern is the transferable part.

## Adjacent

### Beyond Collectives: Building Fused Compute-Communication Kernels with PyTorch Symmetric Memory

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257030)

Ke Wen (NVIDIA), Natalia Gimelshein (Meta), Kapil Sharma (Meta, PyTorch Distributed)

- **Why**: One-sided RMA issued from inside GPU kernels is the biggest change in how accelerators use the fabric since collectives; this is the guided tour of the programming model, and it pairs directly with the new `torch.distributed` window APIs.
- **What**: PyTorch Symmetric Memory gives every rank a direct window into its peers' GPU memory, erasing the compute/communication boundary. A practical tour across five themes: compute–communication fusion (pushing partial results to a peer from inside a kernel), one-sided puts/gets plus `torch.distributed.TokenSwitch` supporting expert-parallel MoE with autograd, binding NCCL device primitives into a CUDA DSL (cute-DSL), device-side profiling plus CUDA Graph capture, and community adoption. (from abstract only)
- **How**: Communication becomes something a kernel does inline, hidden behind compute, instead of a black-box collective the compute waits on.
- **Where applicable**: NVIDIA-backed (NVSHMEM) today, with the AMD rocSHMEM counterpart covered separately; relevant to anyone reasoning about when fused communication beats a collective — and about what next-gen RDMA APIs need to expose.

### rocSHMEM Symmetric Memory in PyTorch for AMD GPUs

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256215)

Prachi Gupta — AMD

- **Why**: Ports of GPU-initiated one-sided RMA to a second vendor are evidence this is becoming a cross-vendor fabric primitive rather than an NVIDIA trick — worth tracking for multi-vendor estate planning.
- **What**: rocSHMEM backend for PyTorch symmetric memory, now upstream: the device-side OpenSHMEM API (one-sided put/get, non-blocking get, put-with-signal, wait-until) exposed as Triton-callable primitives so a kernel initiates its own communication. MoE all-to-all dispatch and combine are constructed within the kernel and overlapped with expert compute; comparison against RCCL host-driven all-to-all on representative MoE workloads promised. (from abstract only)
- **How**: AMD-specific engineering — per-architecture device-bitcode linking and post-compile HIP-module initialization — organized behind a backend-agnostic layer shared with NVSHMEM so a single Triton kernel runs on both AMD and NVIDIA.
- **Where applicable**: AMD GPUs (ROCm); the transferable design is the backend-agnostic layering that keeps one kernel portable across vendors.

### MCCL: Fault-Tolerant Collective Communication for Large-Scale GPU Training

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1256858)

Ben Carver — Meta

- **Why**: Dynamic communicator membership — shrinking and growing as ranks fail or recover — is the collective layer learning what routing protocols learned decades ago about membership churn. Pairs directly with `torch.distributed.reconfigure()` and the TorchPass work.
- **What**: MCCL, Meta's open-source fault-tolerant C++ collective library: hardware failure treated as a first-class design principle, with dynamic communicator reconfiguration that doesn't interrupt the training job. Production-grade AllReduce and Send/Recv via TorchComms integration, with claimed performance parity with NCCL. (from abstract only)
- **How**: Redefines the communication lifecycle around failure and recovery instead of static membership and full-job restarts.
- **Where applicable**: Aimed at tens-of-thousands-of-GPU fleets where failure is routine; open source, so broadly inspectable — but the parity claim is from the abstract, with numbers presumably in the talk.

### EP-Overlap: Hiding Expert-Parallel Communication in MoE Training

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1257875)

Sanket Jayant Purandare (PyTorch Distributed and Compilers), Syed Ahmed (NVIDIA, PyTorch Core)

- **Why**: MoE expert-parallel all-to-all is the dominant new traffic pattern on AI fabrics; knowing how much of it can be hidden by framework-level scheduling tells you how much fabric headroom a MoE fleet actually needs.
- **What**: Graph passes that hide EP communication by splitting each MoE layer into independent slices and overlapping token exchange with any available compute (experts, recompute, weight-gradient math), forward-with-forward and backward-with-backward. The same machinery also hides "page stashing," compacting worst-case activation memory from O(worst_case × L) to O(worst_case + actual). On DeepSeek-V3: 76–86% of EP comm hidden, ~1.3x throughput, +4% absolute MFU — and the authors call that a lower bound. (from abstract only)
- **How**: Implemented as graph passes in TorchTitan's GraphTrainer, working under FSDP and PP with any schedule (not just DualPipe), no model changes, bitwise-matching eager numerics — overlap rather than wire-byte reduction.
- **Where applicable**: DeepSeek-V3-scale MoE training; a framework-level (TorchTitan) technique that generalizes across schedules and parallelism strategies.

### Native Tiered KV Cache Offloading in vLLM: From Storage Offloading to Disaggregated Serving

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1254938)

Or Ozeri — IBM

- **Why**: Long-lived agentic sessions turn KV-cache preservation into a storage/I-O tiering problem with idle sessions holding state for hours or days — the memory-side complement to the KV-transfer talk, and a new consumer of fabric bandwidth.
- **What**: vLLM's native tiered KV-cache offloading framework, newly integrated upstream with no external dependencies. The key design choice: all transfers route through CPU memory as a universal transport hub. (from abstract only)
- **How**: Routing through host memory yields minimal GPU overhead (a simple copy), consolidated I/O from a single CPU buffer, hardware-agnostic operation with no specialized transfer APIs, and independence from KV cache memory layout (which varies across hardware, attention backends, parallelism schemes, and model architectures).
- **Where applicable**: vLLM deployments generally — the design is deliberately layout- and hardware-agnostic; deployment and extension guidance promised.

### Five Bottlenecks, Five Fixes: Systematic Performance Diagnosis for PyTorch Distributed Training

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1254803)

Paulo Aragao, Aravind Neelakantan — AWS

- **Why**: A repeatable diagnostic methodology for the question you get paged about — "is it the network?" Case 3 in particular (0.4% network utilization with MoE expert parallelism turning out to be a pipeline bubble, not a network problem) is exactly the misattribution pattern that wastes fabric-engineering time.
- **What**: Five real case studies mapped onto a decision framework (compute-, memory-, communication-, or I/O-bound), each with specific `torch.profiler` signatures, NCCL debug patterns, and targeted fixes. Headline results: 83x data-loading gain (1.2% → usable GPU utilization), 28% throughput recovered from pipeline stages, and 6.8x end-to-end improvement on a production autonomous-driving model. (from abstract only)
- **How**: Structured profiling → classify the bottleneck → apply the matched fix; delivered as a repeatable checklist for any distributed training workload.
- **Where applicable**: Workload-agnostic methodology from AWS architects; the case studies are customer-specific but the framework and profiler signatures transfer cleanly.

### XCCL: Scaling PyTorch Collectives to Exascale on Intel GPUs with TorchComms

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1258012)

Panagiotis Kourdis, Tanima Dey — Intel

- **Why**: A rare, detailed account of building and validating a new accelerator's collective backend at exascale — including the CI and testing strategy — useful as the reference playbook for any multi-vendor comm-stack work.
- **What**: XCCL, an in-tree Intel-GPU backend for TorchComms built on oneCCL, validated on Aurora (Argonne's exascale supercomputer): over 90% scaling efficiency across thousands of nodes running TorchTitan and other AI workloads. Covers bridging PyTorch collective semantics to oneCCL, a stream-ordered asynchronous execution model that overlaps compute and communication, CI combining mock-based validation with real Intel hardware, and comparisons against NCCL and RCCL. (from abstract only)
- **How**: Backend integration plus semantic bridging between PyTorch's collective API and oneCCL's execution model.
- **Where applicable**: Intel GPUs on Aurora — a specific supercomputer deployment; the transferable content is the backend-building and validation methodology, not the silicon.

### Monarch - Single-Machine DevX at Distributed Scale

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255147)

Thomas Wang, Zach DeVito — Meta

- **Why**: An RDMA fabric used as a general-purpose actor IPC substrate to make a cluster feel like a laptop — a use of RDMA well beyond collectives, and a credible answer to the ergonomics gap that pushes developers away from clusters.
- **What**: Monarch, a library for programming an entire cluster as if it were a single machine: imperative APIs launch processes across the cluster communicating via fast actor-based IPC, with data transfer over RDMA. Services built on the fabric include broadcasting the local filesystem to the whole cluster and surfacing remote logs locally; iteration takes seconds rather than minutes, and distributed processes exit like local ones. (from abstract only)
- **How**: The RDMA-backed actor fabric supports local-feeling services; the talk demos the experience and how to build post-training frameworks on the primitives.
- **Where applicable**: A Meta project aimed at post-training development loops (including for coding agents); assumes a cluster with RDMA and capacity for interactive use.

## Wildcard

### Who Owns Production When the Agent Does the Fixing? Governance in AI-Assisted SRE

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1255337)

Aditi Mewada — Apple

- **Why**: Not a networking topic, but a direct signal of where operations are heading: agents shipping fixes autonomously into production — the same production your change-management, automation guardrails, and identity controls govern. The accountability question ("an agent misconfigures a service at 3am — who is answerable?") will land on security and identity teams first.
- **What**: Governance frameworks, guardrails, and human-in-the-loop patterns for AI-assisted SRE: where autonomy genuinely delivers (faster MTTR, less toil, smarter alerting), where unchecked agent authority creates new failure classes, and a practical mental model for what agents should fix vs. flag vs. never touch. (from abstract only)
- **How**: A patterns-and-mental-model talk rather than a system; no empirical evaluation claimed.
- **Where applicable**: Any operations organization adopting autonomous remediation; conceptual, so weigh it as a framing device rather than validated practice.

### Precompile for Training

**Links:** [Abstract](https://sessionize.com/api/v2/s2rq62nk/view/markdown/session/1245005)

Bob Ren; Aaron Orenstein (Meta)

- **Why**: A genuinely surprising distributed-systems failure mode: in nominally identical SPMD programs, per-rank compilers and autotuners can diverge — choosing different kernels on different ranks, causing NCCL hangs, numerical inconsistencies, and hard-to-debug job failures. Anyone who has chased a "one rank hung" incident will recognize the shape of this problem.
- **What**: Precompile for Training, an abstraction that compiles a distributed SPMD program once and reuses the resulting graph artifact across all ranks — guaranteeing identical execution and kernel selection cluster-wide, moving compilation ahead of GPU allocation, and eliminating redundant compile work across thousands of GPUs. (from abstract only)
- **How**: All ranks share one compiled graph artifact; compilation is decoupled from GPU provisioning so idle-GPU-during-compile waste disappears.
- **Where applicable**: Large SPMD training fleets, vendor-agnostic in principle; short talk with abstract-level detail — the rank-divergence problem statement is the durable takeaway.

## Themes

- **Communication is the workload**: nearly every systems talk is about data movement — hiding it behind compute (EP-Overlap, Symmetric Memory, rocSHMEM), shrinking it on the wire (FP8), or specializing the transport for it (NCCL-EP, OpenCLIC). The field has stopped treating the fabric as a solved substrate.
- **Failure is being redesigned as live reconfiguration**: dynamic communicator membership (MCCL, `torch.distributed.reconfigure`, Elastic EP) and live rank migration (TorchPass) are displacing checkpoint-restart, because at 10k-GPU scale one failure costs 45–90 minutes across the whole fleet. The collective layer is (re)inventing membership protocol semantics.
- **Transport diversification is real**: connectionless RDMA (Ultra Ethernet/Slingshot via OpenCLIC) is being positioned against connection-oriented transports, while GPU-initiated one-sided RMA (NVSHMEM/rocSHMEM/OpenSHMEM) moves communication from host-driven collectives into kernels — with a shared abstraction layer spanning vendors.
- **Inference traffic diverges from training traffic**: MoE dispatch/combine (dynamic many-destination all-to-all) and P/D-disaggregated KV transfer (bidirectional, stateful, lease-governed) are new fabric workloads that bulk-collective designs fit poorly — with agentic sessions adding long-lived idle state that must be tiered and moved.
- **Agent governance is moving down the stack**: from application-layer filters to K8s network policy, seccomp, runtime isolation, audit trails, and kill switches — microsegmentation and zero-trust ideas being re-applied to autonomous agents, with the same old accountability questions resurfacing in SRE.
- **CNCF and the AI foundations are converging**: Kubernetes and Ray co-evolving into a unified stack is being driven jointly by Google and Anyscale — AI workload requirements (scheduling at 10k-node scale, GPU-direct transports) are now K8s roadmap items, not adjacent concerns.
