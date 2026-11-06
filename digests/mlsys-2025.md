<!--
conference: MLSys 2025
source_url: https://mlsys.org/virtual/2025/papers.html?filter=titles
generated: 2026-11-05
registry_key: mlsys-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# MLSys 2025

MLSys 2025 is a machine-learning-systems conference, not a networking one, so the picks below are the minority of the program where the work intersects physical datacenter fabric, interconnect engineering, network security, or ML-assisted operations at production scale. The striking thing for a networking PM: nearly every hard problem on this program now routes through communication — and several papers show the algorithms bending to fit commodity interconnects rather than assuming RDMA-class fabrics. OpenReview page fetches were blocked by bot verification, so all write-ups are grounded in the program abstracts (marked accordingly).

## Core

### Context Parallelism for Scalable Million-Token Inference

**Links:** [Abstract](https://openreview.net/forum?id=Vmf09yVJhT) · [Paper](https://openreview.net/pdf?id=Vmf09yVJhT) · [Recording](https://slideslive.com/39042979)

Amy Yang, Jingyi Yang, Aya Ibrahim, Xinfeng Xie, Bangsheng Tang, Grigory Sizov, Jongsoo Park, Jianyu Huang (Meta / NVIDIA collaboration per author roster)

- **Why**: This is the paper at the intersection of long-context inference and datacenter interconnect reality. It directly answers a fabric-planning question: how much inter-host bandwidth does million-token prefill actually need, and does it need RDMA or does TCP suffice?
- **What**: A context-parallelism scheme for long-context LLM inference that achieves near-linear scaling of prefill latency up to 128 H100 GPUs across 16 nodes — 1M-token prefill with Llama3 405B in 77 seconds at 93% parallelization efficiency and 63% FLOPS utilization; 128K context in 3.8s. (from abstract only)
- **How**: Two lossless exact ring-attention variants — pass-KV and pass-Q — covering full prefill, persistent-KV prefill, and decode. Ring attention turns the inter-node fabric into a circulating KV/Q pipeline, so the bandwidth demand is per-link and steady rather than bursty all-to-all.
- **Where applicable**: The headline empirical result for a fabric PM: benchmarks on H100 hosts interconnected with both RDMA and TCP show *similar* scalability, i.e. the method works over medium-to-low inter-host bandwidth common in commercial datacenters. Ring attention does impose a fixed, latency-sensitive communication pattern across nodes, so node placement and hop count matter. Evaluated on H100 clusters; the RDMA-vs-TCP equivalence is the transferable finding, not the absolute latencies.

### COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts

**Links:** [Abstract](https://openreview.net/forum?id=fGgQS5VW09) · [Paper](https://openreview.net/pdf?id=fGgQS5VW09) · [Recording](https://slideslive.com/39043017)

Shulai Zhang, Ningxin Zheng, Haibin Lin, Ziheng Jiang, Wenlei Bao, Chengquan Jiang, Qi Hou, Weihao Cui, Size Zheng, Li-Wen Chang, Quan Chen, Xin Liu (ByteDance-style production-infra author roster)

- **Why**: MoE routing is the dominant source of bursty, hard-to-balance east-west traffic in modern AI clusters, and this paper quantifies it brutally — inter-device communication of a MoE layer can occupy 47% of total model execution time. This is the traffic pattern your fabric has to survive.
- **What**: An optimized MoE runtime with fine-grained computation-communication overlap: single MoE layer execution 1.96× faster, 1.71× average end-to-end speedup. Deployed in production on ten-thousand-GPU-scale clusters with claimed savings of millions of GPU hours — a real deployment claim, not just a testbed result. (from abstract only)
- **How**: Data-dependency analysis and task rescheduling to overlap communication with computation at fine granularity, plus adaptive workload assignment to eliminate per-rank communication bottlenecks. The communication volume itself isn't reduced — it's hidden behind compute, which changes the latency-sensitivity profile the fabric sees rather than the load.
- **Where applicable**: The 47% communication figure and speedups come from "popular models and frameworks" on large GPU clusters — the technique is general for distributed MoE, but the absolute gains depend on the compute-to-communication ratio of your specific model and interconnect (faster links shrink the hideable bubble). Production validation at ten-thousand-GPU scale is a strong transferability signal, but it is a single operator's stack.

### Photon: Federated LLM Pre-Training

**Links:** [Abstract](https://openreview.net/forum?id=AQgYcfg5EI) · [Paper](https://openreview.net/pdf?id=AQgYcfg5EI) · [Recording](https://slideslive.com/39043026)

Lorenzo Sani, Alex Iacob, Zeyu Cao, Royson Lee, Bill Marino, Yan Gao, Wanru Zhao, Dongqi Cai, Zexi Li, Xinchi Qiu, Nic Lane (Oxford / Cambridge / UCL-style FL collaboration)

- **Why**: A counter-current to the "ever-fatter fabric" narrative: this trains 7B-parameter LLMs from scratch across weakly connected, geographically dispersed GPU silos over the internet. If viable, it changes WAN/interconnect economics for training — less dependence on a single specialized DC, compute sourcing that follows electricity prices, and far lower inter-silo bandwidth requirements.
- **What**: The first complete system for federated, from-scratch, end-to-end LLM pre-training. Trains models up to 7B federatively with perplexity *better* than centralized pre-training; communicates 64×–512× less than baselines and beats baseline distributed-training wall-time by 35%; converges twice as fast as DiLoCo and is robust to data heterogeneity across silos. (from abstract only)
- **How**: Cross-silo federated learning: local training with small client batch sizes at extremely high learning rates, with periodic federated averaging — the surprising claim is that FedAvg's robustness to hyperparameters is what unlocks the aggressive data efficiency. Communication happens only at synchronization rounds, which is where the 64–512× reduction comes from.
- **Where applicable**: Cross-silo settings with internet-class (not datacenter-class) links between participants. Data heterogeneity and non-IID silo datasets are explicitly addressed. The result is pre-training only — fine-tuning and RLHF stages aren't covered in the abstract. Most relevant to anyone thinking about geo-distributed training capacity and WAN procurement; it lowers the interconnect bar rather than raising it.

### Supply-Chain Attacks in Machine Learning Frameworks

**Links:** [Abstract](https://openreview.net/forum?id=EH5PZW6aCr) · [Paper](https://openreview.net/pdf?id=EH5PZW6aCr) · [Recording](https://slideslive.com/39043032)

Yue Gao, Ilia Shumailov, Kassem Fawaz (UW-Madison / Oxford lineage)

- **Why**: The ML OSS ecosystem is a supply-chain security disaster zone — enormous transitive dependency graphs, unpinned artifacts in model repos, and Python's import-time execution model. For anyone responsible for network/security policy around ML infrastructure, this is the emerging attack surface paper.
- **What**: Introduces a new class of supply-chain attack specific to ML models: innocuous-looking code injected via traditional supply-chain vectors that *weakens model robustness* rather than exfiltrating data — the payload is a degraded or subtly sabotaged model. Complements the attack with an LLM-assisted analysis of security discussions across the top 50 ML projects on GitHub, finding ML contributors' security awareness is no better than the general OSS population. (from abstract only)
- **How**: Exploits inherent insecurities of Python as the deployment language for models — the same mechanism as classic dependency/pickling attacks, but with an ML-robustness payload that evades functionality testing. The empirical study mines maintainer discussions for security posture.
- **Where applicable**: Broadly applicable — any organization consuming open-source ML models or frameworks (which is all of them). The attack class is not tied to specific operator scale. Note it is a vulnerability class + measurement paper, not a deployed defense; the mitigations it implies (artifact scanning, sandboxed loading, model provenance/attestation) are left to the reader's roadmap.

## Adjacent

### TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives

**Links:** [Abstract](https://openreview.net/forum?id=ccjvBkTRRe) · [Paper](https://openreview.net/pdf?id=ccjvBkTRRe) · [Recording](https://slideslive.com/39043016)

Size Zheng, Jin Fang, Xuegui Zheng, Qi Hou, Wenlei Bao, Ningxin Zheng, Ziheng Jiang, Dongyang Wang, Jianxi Ye, Haibin Lin, Li-Wen Chang, Xin Liu

- **Why**: Overlapping intra-layer communication with compute is where GPU-cluster performance now lives, and today it's hand-written by kernel experts. This is a compiler approach to that problem — relevant background for anyone whose fabric teams collaborate with ML-infra teams on collective performance.
- **What**: A kernel-generation system that composes communication and compute into overlapped kernels via "tile-centric primitives": the frontend decouples the communication and computation design spaces and links them via tiles; the backend lowers primitives into low-level communication instructions for fused, overlapped execution. 1.17×–20.76× speedup over non-overlapping baselines, performance comparable to state-of-the-art hand-tuned overlapping libraries. (from abstract only)
- **How**: Tile-level abstraction — computation and communication are each expressed over tiles, and the compiler schedules them to overlap, avoiding the suboptimality of operator decomposition and the expertise barrier of manual kernel fusion.
- **Where applicable**: General technique for distributed intra-layer parallel operators on GPUs; the very wide 1.17–20.76× range says gains depend heavily on the operator and topology. Evaluated on GPUs; the communication backend targets standard collectives, so it complements rather than replaces whatever interconnect you run.

### ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments

**Links:** [Abstract](https://openreview.net/forum?id=44PwmgOpAt) · [Paper](https://openreview.net/pdf?id=44PwmgOpAt) · [Recording](https://slideslive.com/39043022)

YOUHE JIANG, Fangcheng Fu, Xiaozhe Yao, Taiyi Wang, Bin CUI, Ana Klimovic, Eiko Yoneki

- **Why**: LLM serving in *heterogeneous* cloud environments — mixed GPU types and, critically, *diverse network bandwidth conditions* — is the realistic deployment case for anyone not operating a homogeneous in-house cluster. The scheduling algorithm here explicitly reasons about network bandwidth as a placement constraint.
- **What**: An LLM serving system for heterogeneous clouds: a scheduling algorithm that optimizes the deployment plan under heterogeneous resource and network-bandwidth conditions, plus a lightweight re-scheduling mechanism that adapts to node failures and workload shifts without restarting services. Up to 2.1× throughput (1.7× average) and up to 2.5× better latency-deadline attainment vs. state of the art at the same price budget. (from abstract only)
- **How**: Network- and resource-aware deployment planning, then live re-sharding/reallocation of serving capacity as conditions change — the re-scheduling-without-restart piece is the operational lesson, since costly restarts are what usually kill adaptive placement in production.
- **Where applicable**: Cloud deployments with mixed GPU generations and variable inter-host bandwidth; also validated in homogeneous in-house environments. The headline numbers are cloud-price-relative, so they translate as "cloud can beat in-house at equal budget" rather than absolute performance claims.

### AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds

**Links:** [Abstract](https://openreview.net/forum?id=3EXBLwGxtq) · [Paper](https://openreview.net/pdf?id=3EXBLwGxtq) · [Recording](https://slideslive.com/39042984)

Yinfang Chen, Manish Shetty, Gagan Somashekar, Minghua Ma, Yogesh Simmhan, Jonathan Mace, Chetan Bansal, Rujia Wang, S R (Microsoft Research / academic collaboration)

- **Why**: This is the "AgentOps" position paper — LLM agents autonomously handling fault localization, root-cause analysis, and incident response through the full incident lifecycle. For a networking PM whose world is increasingly AI-assisted operations, this frames the evaluation problem: how would you even know if an ops agent is any good?
- **What**: A framework that deploys diverse cloud environments, injects faults, generates workloads, and exports telemetry, then orchestrates it all behind interfaces for driving and evaluating agents end-to-end. Includes a benchmark built on it, and empirical findings on where state-of-the-art LLM agents succeed and fail at complex operational tasks. (from abstract only)
- **How**: Reproducible environment + fault injection + workload generation + telemetry export + agent interaction/evaluation interfaces — i.e., the missing harness that isolated single-task AIOps benchmarks never had.
- **Where applicable**: General-purpose and open-ended; the fault taxonomy and environments are cloud/DevOps-flavored rather than network-device-specific, so network ops teams would need to add their own scenarios. The capability/limitation findings for current agents are the immediately useful part.

### LAVA: Lifetime-Aware VM Allocation with Learned Distributions and Adaptation to Mispredictions

**Links:** [Abstract](https://openreview.net/forum?id=9vyyfVNW1E) · [Paper](https://openreview.net/pdf?id=9vyyfVNW1E) · [Recording](https://slideslive.com/39043031)

Jianheng Ling, Pratik Worah, Yawen Wang, Yunchuan Kong, Chunlei Wang, Clifford Stein, Diwakar Gupta, Jason Behmer, Logan Bush, Prakash Ramanan, Rajesh Kumar, Thomas Chestna, Yajing Liu, Ying Liu, Ye Zhao, Kathryn S. McKinley, Meeyoung Park, Martin Maas (anonymized hyperscaler "AnonCorp")

- **Why**: Hyperscale bin-packing is the canonical capacity-planning problem, and this comes with something rare: fleet-wide production deployment numbers and an honest treatment of what happens when your ML predictions are wrong — the part most papers skip.
- **What**: VM-to-host allocation using *reprediction* with lifetime distributions (vs. one-shot point prediction), with algorithms that adapt when mispredictions surface; also novel defragmentation and maintenance handling, which prior academic work ignored. In production at a hyperscaler: ~3% and ~2% reductions in stranded compute and memory, 2.3–9.2 percentage-point increase in empty hosts (helping large-VM availability and system updates), plus fewer migrations. (from abstract only)
- **How**: Predict full lifetime distributions rather than point estimates; re-predict and re-schedule as evidence accumulates; treat prediction error as a first-class input to the allocation and defrag algorithms rather than an afterthought.
- **Where applicable**: Org-specific in the sense that gains are calibrated to one hyperscaler's fleet and VM size mix, but the method (distributional prediction + misprediction-adaptive scheduling) is general to any workload-placement problem with lifetimes. The "repredictions beat one-shot predictions" finding is the transferable lesson.

### A Bring-Your-Own-Model Approach for ML-Driven Storage Placement in Warehouse-Scale Computers

**Links:** [Abstract](https://openreview.net/forum?id=JuGWOSB68T) · [Paper](https://openreview.net/pdf?id=JuGWOSB68T) · [Recording](https://slideslive.com/39043002)

Chenxi Yang, Yan Li, Martin Maas, Mustafa Uysal, Ubaid Hafeez, Arif Merchant, Richard McDougall (anonymized hyperscaler "AnonCorp")

- **Why**: Less about storage than about *why ML-for-infra hasn't shipped* — the paper diagnoses the failure modes of a decade of academic ML-placement papers in a real hyperscale environment. That diagnosis transfers to every "why doesn't anyone deploy this" ML-for-networking idea a PM has ever sponsored.
- **What**: A cross-layer design: ML prediction moves *out* of the storage layer and into the application above it ("bring your own model"), with a co-designed heuristic in the storage layer that consumes those predictions. Small interpretable application-level models + adaptive storage-layer scheduling, tested in a production distributed-computation framework at a hyperscaler; up to 3.47× TCO savings over state-of-the-art baselines in test deployment and production-trace simulations. (from abstract only)
- **How**: Prior work assumed a monolithic model resident inside the storage system — unrealistic in real deployments. Instead, the application provides predictions as hints; the storage layer runs a scheduling algorithm robust to online drift and heterogeneous model quality.
- **Where applicable**: The specific TCO numbers are hyperscaler- and trace-specific, but the architectural pattern — predictions as hints from the layer that has the data, heuristics as the enforcement point that must stay robust — is broadly applicable, including to ML-driven network traffic engineering. Proof-of-concept stage, not full production.

### Radius: Range-based Gradient Sparsity for Large Foundation Model Pre-training

**Links:** [Abstract](https://openreview.net/forum?id=UCQPWBOWb6) · [Paper](https://openreview.net/pdf?id=UCQPWBOWb6) · [Recording](https://slideslive.com/39042988)

Mingkai Zheng, Zhao Zhang

- **Why**: A communication-volume play: if you can cut the bits moved per training step, you relax pressure on the interconnect that carries data-parallel gradients. Useful input for anyone doing capacity math on training-fabric uplinks.
- **What**: A gradient-sparsity algorithm that accelerates large-FM pre-training while preserving downstream task quality — 40% sparsity on GPT-2.0B across 64 A100s cuts per-step training time 21% and total pre-training time 19% with no downstream-task degradation. Notably shows that the obvious prior approach (top-k sparsity with AdamW) *fails to converge*, so the win is not free. (from abstract only)
- **How**: Two insights: only a small fraction of gradients contribute per iteration, and the spatial distribution of large-magnitude gradients is stable over time — so sparsity structure is maintained, avoiding the dense-communication blowup that top-k methods hit in later training phases.
- **Where applicable**: Data-parallel pre-training of GPT-family models; evaluated at 355M–2.0B scale on A100s. The time savings come from reduced gradient communication, so gains scale with interconnect contention. Convergence claims are pre-training-specific; not yet shown for RLHF or other finetuning regimes.

## Wildcard

### AI Metropolis: Scaling Large Language Model-based Multi-Agent Simulation with Out-of-order Execution

**Links:** [Abstract](https://openreview.net/forum?id=fsMImmI1TE) · [Paper](https://openreview.net/pdf?id=fsMImmI1TE)

Zhiqiang Xie, Hao Kang, Ying Sheng, Tushar Krishna, Kayvon Fatahalian, Christos Kozyrakis

- **Why**: Borrowing out-of-order execution — a CPU pipeline idea any dataplane person knows cold — to schedule LLM agent simulations. Seeing hardware-execution concepts reappear at the agent-simulation layer is a genuinely interesting signal of where systems thinking is heading.
- **What**: A simulation engine for LLM multi-agent simulations that uses out-of-order scheduling to break the false-dependency bottleneck: standard parallel simulations synchronize globally, serializing agents that don't actually depend on each other. 1.3×–4.15× speedup over globally-synchronized parallel simulation, approaching optimal as agent counts grow. (from abstract only)
- **How**: Dynamically tracks the *real* dependency graph between agents and issues agent "instructions" out of order when they're independent — a scoreboard/Tomasulo-style idea applied to inference calls instead of µops.
- **Where applicable**: LLM-agent simulation platforms (social-science simulations, game NPC orchestration); the dependency-tracking idea generalizes to any DAG-of-interdependent-tasks executor. Evaluated in simulation settings, not production.

### VoLUT: Efficient Volumetric streaming enhanced by LUT-based super-resolution

**Links:** [Abstract](https://openreview.net/forum?id=EKcNxabscU) · [Paper](https://openreview.net/pdf?id=EKcNxabscU) · [Recording](https://slideslive.com/39043033)

Chendong Wang, Anlan Zhang, Yifan Yang, Lili Qiu, Yuqing Yang, XINYANG JIANG, Feng Qian, Suman Banerjee (networking-community author roster)

- **Why**: A bandwidth-vs-compute trade made explicit: ship downsampled volumetric (3D) video and reconstruct with lookup-table super-resolution at the receiver — 70% bandwidth reduction at line rate on commodity mobile devices. It's the classic edge/cdn rate-adaptation problem with a novel twist, from a networking research group.
- **What**: The first system enabling high-quality 3D super-resolution of volumetric streams on commodity mobile devices at line rate: LUT-based upscaling of pre-downsampled content, plus an adaptive bitrate loop that picks the downsampling rate based on network conditions. 70% bandwidth reduction, 36.7% QoE improvement, 8.4× faster 3D super-resolution with no quality loss. (from abstract only)
- **How**: Precomputed LUTs map low-resolution volumetric values to high-resolution reconstructions, replacing expensive on-device SR inference with fast table lookups; ABR logic sits on top, treating fidelity level like a video bitrate ladder.
- **Where applicable**: Volumetric/immersive media delivery over constrained last-mile networks to mobile receivers; the LUT-for-neural-SR substitution pattern generalizes to any receiver-side computationally-bound reconstruction. Evaluation is on mobile devices, not datacenter delivery.

### Extreme PyTorch: Inside the Most Demanding ML Workloads—and the Open Challenges in Building AI Agents to Democratize Them

**Links:** [Abstract](https://mlsys.org/virtual/2025/invited-talk/2886)

Soumith Chintala (PyTorch)

- **Why**: The best panoramic view of what "planetary-scale training on interactive supercomputers" and ultra-efficient real-time inference actually demand from the underlying stack — and an honest framing of the AI-agents-for-systems-work idea from someone who sees every exotic deployment. Useful calibration for a PM deciding how much of the AI-agents-for-ops wave is real.
- **What**: A survey talk on the extreme edge cases of PyTorch usage — the workloads that break the framework and define its roadmap — followed by a candid assessment of the open problems in building agents that automate the work cutting-edge users do today, with the stated position that this vision is "far from realized." (from abstract only)
- **How**: Experience-driven: the demands of the most extreme users are used as a window onto the field's hardest systems problems, then mapped to concrete open collaboration opportunities for SysML agents.
- **Where applicable**: A keynote, not a results paper — no evaluation to check; treat it as direction-setting. Its value is the curated view of where systems pain actually is at the frontier, and the explicit list of gaps between the "AI agents automate infra work" pitch and current reality.

## Themes

- **Communication is the bottleneck, and the field knows it.** Context Parallelism, COMET, TileLink, Radius, ScaleFusion, and Photon all attack the same wall from different directions: inter-device/inter-node communication dominating execution time at scale. For fabric people, this means job-level traffic patterns (MoE routing bursts, ring-attention pipelines) — not just collective volume — are what your network must be designed around.
- **Algorithms are starting to bend toward commodity interconnects.** The RDMA≈TCP scalability result in Context Parallelism and Photon's 64–512× communication reduction over internet-class links both point the same way: the software stack is becoming bandwidth-tolerant. That is a real input to "how fancy does the fabric need to be" debates.
- **Production-deployment evidence is finally arriving for ML-driven resource management.** LAVA, the storage-placement paper, COMET, and (in the program but not picked) ProtoRAIL all ship in hyperscale production — and each one's main contribution is explaining why the clean academic version failed and what pragmatic redesign (hints not control, distributions not point predictions, cross-layer not monolithic) made it deployable.
- **Agentic operations ("AgentOps") is being formalized.** AIOpsLab provides the evaluation harness, Extreme PyTorch names the gap honestly, and AI Metropolis supplies a scheduling engine — an emerging stack for agents that run infra, worth tracking before it arrives in your on-call tooling.
- **The ML software supply chain is a recognized but unmitigated attack surface.** The supply-chain paper shows ML-specific payload attacks and measurably complacent security culture in top OSS ML projects; Ling Liu's keynote covers the adjacent finetuning-time robustness problem. Both signal that security investment here is lagging capability investment by a wide margin.
- **Serving-system research is converging on stage-awareness.** Seesaw, SOLA, Marconi, and Context Parallelism all reject static parallelism/scheduling across prefill-vs-decode — a lesson that generalizes to any tiered-latency system, including network QoS design.
