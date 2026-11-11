<!--
conference: AI Engineer World's Fair 2026
source_url: https://ai.engineer/worldsfair/2026/sessions.json
generated: 2026-11-11
registry_key: aiengineer-worldsfair-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AI Engineer World's Fair 2026

The 24 items below were pre-selected from the 561-session program. Note on sourcing: this program extract carries no `page:`/`pdf:`/`slides:`/`video:` links for any item, so every write-up below is grounded in the session abstract alone — treat each as a preview, not a review of full material.

## Core

### TCP and RDMA are Killing Inference Throughput; Homa can Fix It

Speakers: John Ousterhout (keynote; affiliation not listed in program)

- **Why**: Inference traffic is shifting from bulk transfers to huge numbers of tiny, latency-critical messages (agentic workflows, disaggregated KV stores), and the transports underneath — TCP and RDMA — were not built for that mix. This is the one genuinely transport-layer talk in the set, sitting squarely in the RDMA/lossless-fabric and AI-fabric intersection.
- **What**: An argument that legacy transports are the throughput bottleneck for modern inference workloads due to poor congestion control and head-of-line blocking, plus an introduction to Homa, which cuts short-message latency by ~10x on AI-datacenter-like workloads (from abstract only).
- **How**: Homa uses receiver-driven flow control (grants) and, critically, capitalizes on priority queues in switches — SRPT-style scheduling of messages into switch priority levels so short requests don't queue behind large transfers.
- **Where applicable**: Datacenter fabrics where switches expose usable priority queues (Homa is designed around programmable queue assignment, not deep buffering). Note the framing comes from Homa's own author, so expect advocacy; the failure analysis of TCP/RDMA on mixed-size traffic stands on its own. Broadly relevant to anyone building disaggregated inference/KV fabrics.

### Can LLMs write fast multi-GPU kernels? We built a benchmark to find out.

**Links:** [Recording](https://www.youtube.com/watch?v=pOvWgX7IJsc)

Speakers: Simran Arora

- **Why**: Production inference is bottlenecked by communication — all-reduce alone is claimed at >20% of latency on Llama-3.3-70B — yet every existing LLM-kernel-coding benchmark is single-GPU. This is the first systematic evaluation of multi-GPU kernel generation, right at the intersection of AI codegen and GPU interconnects.
- **What**: ParallelKernelBench (PKB): 87 problems from real codebases where the task is replacing PyTorch + NCCL with a CUDA kernel that moves data directly over NVLink. Frontier models (GPT-5.5, Gemini 3 Pro, Opus 4.7) solved under a third of problems, and fewer than a quarter of those beat the naive baseline — though a few cases produced kernels faster than anything publicly available, including one for NeMo-RL's GRPO training loop with no prior optimized public reference. Open source (from abstract only).
- **How**: Benchmark plus evaluation framework measuring correctness and speedup against a naive multi-GPU baseline, with data movement over NVLink directly rather than via NCCL collectives.
- **Where applicable**: General and open source; results are a snapshot of frontier coding models at the time of the study. Most useful to teams exploring LLM-assisted performance engineering on multi-GPU nodes.

### Taking Reinforcement Learning Cross Datacenter

**Links:** [Recording](https://www.youtube.com/watch?v=maRzp4kImJ4)

Speakers: Nan Jiang

- **Why**: RL for frontier models is pinned to a single datacenter today — training and rollout generation must co-locate — which makes the whole system hostage to one site's capacity, hardware, and failures. Decoupling them changes where AI training traffic flows and what the cross-DC network has to tolerate.
- **What**: A position talk on the first steps toward cross-datacenter RL: training in one place, rollout trajectory generation elsewhere, pulling compute opportunistically from whatever cloud, region, hardware, or precision format is available — making RL capacity global and elastic rather than a reserved supercomputer (from abstract only).
- **How**: Architectural disaggregation of the RL loop (learner vs. rollout workers) so each component can live where capacity and price are best, tolerating cross-site latency and heterogeneous hardware/precision.
- **Where applicable**: Frontier-lab-scale RL today, but it directly signals future cross-DC training/rollout traffic patterns and DCI requirements. The abstract is a vision statement with no quantitative results — go for direction, not data.

### KV Cache-Aware Routing and P/D Disaggregation on Kubernetes: The Parts Public Benchmarks Don't Show

**Links:** [Recording](https://www.youtube.com/watch?v=YXowceUKYJI)

Speakers: Yuchen Fama, Ashish Kamra

- **Why**: Agentic inference breaks the core assumption of LLM serving — the server no longer controls its cache lifecycle; the client does, through prompt construction and growing multi-turn context. That pushes prefill strategy, eviction, and routing up to the scheduler layer, which is exactly the K8s-native serving-stack problem (vLLM, llm-d).
- **What**: A walkthrough of the open serving stack for agentic workloads: why KV-aware routing through a fleet-wide scheduler is the first optimization (ahead of adding capacity), when prefill/decode disaggregation actually pays off versus the workload shapes that justify its complexity, plus tiered KV offload and wide expert parallelism — demonstrated on GLM-5.2 with vLLM and llm-d. Attendees get a tuning decision framework: which lever to pull first and where more GPUs don't help (from abstract only).
- **How**: Cache-aware routing (schedule requests to replicas by prefix reuse), separation of compute-bound prefill from memory-bound decode, tiered KV cache offload, and workload-signal-driven decisions; economics framed as prefill dominating cost with cache reuse as the primary lever.
- **Where applicable**: Open-source stack on Kubernetes — broadly applicable to anyone operating inference fleets, especially prefill-heavy agentic traffic. Grounded in trace replays per the abstract, but no numbers are given, so the framework's thresholds will need the talk itself.

### Routing LLM Inference in Production: From Engine Signals to Policy

**Links:** [Recording](https://www.youtube.com/watch?v=sOB3HSiG8vo)

Speakers: Qianru Lao, Lu Zhang

- **Why**: Request-level routing across engines, clusters, and geographies is emerging as its own infrastructure layer — an inference load balancer — which is the GPU-era analog of load-balancing architecture the PM already knows well.
- **What**: A generalized Inference Load Balancer (ILB) proxy/controller architecture: a low-latency proxy applies routing weights and request-path signals, while a controller computes source-cluster-to-engine weights from demand, capacity/performance profiles, replica state, and geography cost. Includes the operational debugging patterns AI engineers actually need: reading engine signals, explaining why a request landed on a given backend, handling retries and load shedding, and keeping routing observable (from abstract only).
- **How**: Two-tier split — data-plane proxy for request-path decisions, control-plane controller for weight computation — with engine-signal feedback loops. The abstract notes the content is framed generically "without exposing OpenAI-specific internals," which strongly suggests a large-lab production origin.
- **Where applicable**: Multi-cluster, multi-engine inference fleets; the architecture pattern is general, but expect transferable patterns rather than a deep operator postmortem, since the speakers deliberately abstract away their production specifics.

### Fault-Tolerant Training at Scale: Making Hardware Failures a Non-Event

Speakers: not listed in program; presented by Crusoe (per abstract)

- **Why**: At thousands of GPUs, hardware failures happen multiple times per day; the standard response — a paged engineer SSHing in for an hour — compounds directly into wasted GPU-hours. This is the self-healing/automation story for training clusters, built on Kubernetes.
- **What**: Crusoe's self-healing platform: a managed Slurm environment running on Kubernetes with automated node-failure remediation and real-time cluster observability, designed so hardware failures become non-events; also covers open-loop remediation for teams that want full control over node replacement for application-specific workflows (from abstract only).
- **How**: Running Slurm on K8s to inherit K8s resilience primitives (health-driven node replacement) that traditional GPU clusters lack; automated hardware monitoring triggers remediation; every remediation event is observable so teams stay informed without being on-call.
- **Where applicable**: Crusoe-specific production setup, but the pattern — batch scheduler on Kubernetes plus automated node remediation plus remediation observability — transfers cleanly to any large GPU fleet. The open-loop option matters for teams with stateful, placement-sensitive training jobs.

### Running a 20T-Token Data Pipeline: Infrastructure Lessons from Production

Speakers: Bogdan Gaza (Arcee, per abstract)

- **Why**: The systems engineering that keeps curation pipelines running on petabytes and thousands of GPUs almost never gets written down; this is a rare end-to-end production account, including the operational details (metadata stalls, multi-week fault tolerance, CPU/GPU pool fragmentation) that break naive designs.
- **What**: Lessons from two production pipelines — Arcee Trinity-Large's corpus scaling 8T → 10T → 20T tokens (8T+ synthetic tokens on clusters peaking at 2,048 H100s) and a 100B-token Thomson Reuters legal mid-training corpus. Concrete findings: fetching metadata from object storage across millions of files became the dominant idle-time source (offloaded to Spark plus a lightweight file-level distribution scheme, driving idle time to near zero); one-to-one Spark↔Ray partition mapping yields idempotent, resumable execution so a node failure doesn't mean reprocessing; an in-house scheduler routes CPU-heavy Spark and GPU-heavy Ray+vLLM workloads to isolated node pools; per-model vLLM tuning (batch size, speculative decoding, n-gram sampling) yielded up to 40% throughput; and the curated corpus is treated as a versioned deployment artifact (from abstract only).
- **How**: Hybrid Spark + Ray + vLLM architecture, idempotent partition mapping for fault tolerance, isolated node pools per workload class, and per-model inference tuning rather than stack defaults.
- **Where applicable**: Trillion-token-scale synthetic data generation and mid-training pipelines; org-specific in scale, but the failure modes (metadata bottleneck, long-job resumability, resource fragmentation between CPU and GPU pools) are general.

### Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It

**Links:** [Recording](https://www.youtube.com/watch?v=AVMr9PMINyo)

Speakers: Olive Song (MiniMax, RL Lead), Dan Fu (Together AI, VP of Kernels)

- **Why**: Agentic workloads — prefill-heavy traffic, high cache hit rates, long-context inputs — break inference engines built for chat, and this pairs the model team and the serving-infrastructure team on the same open model family, showing both sides of the contract.
- **What**: Two halves: the model side (the RL decisions behind MiniMax's long-context reasoning and tool use, and what training for agentic behavior looks like in practice) and the infrastructure side (why agentic workloads break chat-era engines, and the kernel-level optimizations built for that workload profile), plus how the two teams collaborate on launches and ongoing performance work (from abstract only).
- **How**: The abstract stays at the workload-characterization level — prefill-heavy traffic, high cache hit rates, long-context inputs — without naming specific kernel techniques, so the depth will be in the talk.
- **Where applicable**: MiniMax/Together-specific production experience, but the workload-shape characterization of agentic traffic versus chat traffic is directly reusable by anyone capacity-planning an inference fleet.

### Large clusters for small models

**Links:** [Recording](https://www.youtube.com/watch?v=g4SsanB0gMc)

Speakers: Daniel Svonava

- **Why**: A wide catalog of small task-specific models is cheaper and faster than the frontier, but serving it is a different infrastructure problem: dedicated worker pools idle, request routers choke on the sheer volume of small requests, and users bring hundreds of LoRAs.
- **What**: How the speaker's team serves 1M tokens per second with small models: cluster architecture for maximum throughput and minimum latency simultaneously, plus "autoresearch" applied to their own inference code to support 10+ new models per week (from abstract only).
- **How**: The abstract is thin on mechanism — the substantive claims are the 1M tok/s figure, the joint throughput/latency cluster design, and using automated research to rewrite inference code for model-onboarding velocity. Treat the autoresearch angle as a lead to investigate, not a transferable recipe.
- **Where applicable**: Many-small-model / many-LoRA serving environments rather than frontier-model fleets; org-specific until the mechanisms are explained.

### Seeing the Plumbing: Profiling vLLM Speculative Decoding on NVIDIA Blackwell

Speakers: Sheilah Kirui (Akamai, per linked example repo)

- **Why**: Speculative decoding is usually discussed in averages; this talk shows how to actually measure its engineering trade-off — guess right and you bypass the memory-bandwidth bottleneck, guess wrong and you waste compute — with live instrumentation rather than benchmark folklore.
- **What**: A live demo routing identical workloads through baseline and speculative vLLM configurations on a single NVIDIA RTX 6000 Blackwell GPU, profiling three vectors: time-per-output-token latency delta, the exact KV-cache/VRAM tax of tracking parallel token states within a 96GB budget, and the draft-acceptance tipping point where speculation falls below baseline efficiency. Open-source example repo (in active development) (from abstract only).
- **How**: Side-by-side StreamStream — a Streamlit app and a live Grafana dashboard — instrumenting the three vectors so the memory dynamics and acceptance-rate decay are visible in real time.
- **Where applicable**: The profiling methodology (isolating TPOT, memory footprint, and acceptance rate; forcing memory pressure) transfers to any engine/GPU pair; absolute numbers are tied to one Blackwell GPU and model pair.

### AI : Learned Execution Graphs for Real-Time Anomaly Detection & Drift Classification in APIs

**Links:** [Recording](https://www.youtube.com/watch?v=u1yaOeEX4e8)

Speakers: Ritvik Pandya (sponsor session)

- **Why**: ML for infrastructure operations is one of the PM's explicit interests, and this is a production system applying learned models to API middleware pipelines — with concrete, quantified results rather than AIOps generalities.
- **What**: Models the API ingress pipeline (auth, validation, rate limiting, routing, caching) as a DAG learned from structured telemetry at 1,600+ TPS, then applies it three ways: per-node anomaly attribution (in production this pinpointed a 41x deviation at a single node invisible to service-level monitoring, cutting root-cause time from 2–3 hours to under 30 seconds); structural drift detection (missing, reordered, or injected middleware nodes that latency/error monitors reported as "healthy"); and per-client graph fingerprinting that classifies behavior change vs. configuration drift vs. infrastructure failover via KL divergence. Also a novel retry-storm detection approach using idempotency-key entropy, breaking amplification loops by returning cached responses at the specific graph node (from abstract only).
- **How**: One structured event per processing step; per-endpoint execution graphs built via sequence mining with statistical confidence thresholds; per-node baselines (latency, dependency, execution frequency) and deviation ratios; exponential moving averages for client profiles.
- **Where applicable**: Any middleware/ingress pipeline that can emit structured per-step telemetry — broadly applicable. It is a sponsor slot, so expect product framing, but the graph-construction and attribution methodology is the transferable core.

### Kubernetes Is Not Your Sandbox

Speakers: Ivan Burazin

- **Why**: Teams are reaching for Kubernetes to run agent sandboxes, and the mismatch — an orchestrator built to hold steady state versus environments that are born, forked, and killed in under a second — has a measurable, benchmarked cost. Directly relevant to K8s architecture and operations.
- **What**: A benchmark running the same 50-action bug-fix trajectory across five stacks, yielding a 12x spread — 12.9s on the fastest, 161.5s on the slowest — with the gap attributed to per-action lifecycle overhead, not compute. Every stack is named and each number's mechanism explained. The talk also frames the requirements contradiction: sandboxes went from fast code-snippet runners to stateful long-running agent boxes to ten thousand ephemeral environments that fork for RL rollouts and die in under a second — all at once (from abstract only).
- **How**: Cross-stack execution-time decomposition isolating lifecycle overhead (scheduling, environment start/teardown) per action from actual compute.
- **Where applicable**: Any team running agent or RL-rollout environments at scale; the comparison is stack-agnostic and directly informs substrate choice. The abstract closes with "wdyt?", suggesting the talk invites debate — worth attending for the numbers and mechanisms regardless.

### Sandboxes Aren't Optional: Runtime Isolation Patterns for Coding Agents at Scale

**Links:** [Recording](https://www.youtube.com/watch?v=iH_wV8BbS24)

Speakers: Robert Brennan (OpenHands, per abstract)

- **Why**: When agents write code, run tests, make API calls, and push commits, security is a runtime isolation problem, not a prompt-engineering problem — and the isolation patterns (egress control, multi-tenant RBAC, audit) map directly onto the PM's Kubernetes and multi-tenancy concerns.
- **What**: The isolation patterns OpenHands follows: Docker and Kubernetes isolation, per-agent filesystem scoping, network egress controls, RBAC for multi-tenant deployments, and full audit trails; the three most common failure modes when teams skip isolation (including an agent committing secrets to a public repo, and the opening story of an agent wiping a production database during a code freeze). Includes a live demo of 50 parallel sandboxed agents with resource limits, timeout enforcement, and graceful degradation, plus a sandbox checklist and reference Kubernetes config (from abstract only).
- **How**: Container-level isolation with scoped filesystems and egress policy, per-agent identity and permissions, audit logging, and defined degradation paths when agents hit unexpected states.
- **Where applicable**: Broadly applicable — the patterns are from an open project and reference configs are provided. Most valuable to teams running coding agents against real codebases in shared or production-adjacent infrastructure.

### Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story

**Links:** [Recording](https://www.youtube.com/watch?v=btxG75rNJC4)

Speakers: Asaf Gardin, Yuval Belfer (AI21, per abstract — Jamba models)

- **Why**: Distributed inference systems fail silently — wrong answers with perfect confidence, no stack trace, no sanitizer warning — and this is a rare debugging postmortem that teaches the instrumentation methodology, not just the war story. Promoted from adjacent: silent-failure debugging in distributed inference is core ops content for anyone running vLLM.
- **What**: Two production bugs from building Jamba models: (1) a request misclassified during scheduling loads stale state from a previous prompt-cache slot and confidently generates gibberish once every ~1,000 prompts; (2) logprob spikes during RL training that looked like training instability until they were noticed tracking rollout count, then cache size (from abstract only).
- **How**: Instrumenting vLLM to thread request IDs through the forward pass; building comparison scripts that expose logprob divergence; forcing memory pressure to surface rare bugs; shrinking a distributed RL training mystery into a reproducible single-script failure; and the generalizable lesson — search for variables that change failure *structure* rather than magnitude.
- **Where applicable**: vLLM-based serving and RL training loops specifically, but the instrumentation techniques and correlation-driven debugging method transfer to any cache-based serving system.

## Adjacent

### From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1

**Links:** [Recording](https://www.youtube.com/watch?v=OqM67QG_Ikk)

Speakers: Abhishek Bhardwaj

- **Why**: The third of the sandbox-infrastructure talks; useful as the architecture-and-trade-offs companion to the two Core picks above.
- **What**: The architectural challenges of building an agent sandbox cloud: a comparison of runtime isolation technologies and their trade-offs, persistence and storage as the next major unlock for agent capabilities, and the key decisions in orchestrating and scaling sandboxes (from abstract only).
- **How**: A design/technology comparison rather than measured results — part 1 of a two-part session.
- **Where applicable**: Teams designing sandbox infrastructure rather than consuming it; the abstract is thin (no measurements), so calibrate expectations accordingly.

### Operating Distributed Inference Systems at Scale

**Links:** [Recording](https://www.youtube.com/watch?v=7c9FSUVcXR0)

Speakers: Nishant Gupta, Naman Ahuja

- **Why**: The framing — inference as an infrastructure orchestration problem — matches the PM's view exactly, and the topic list (multi-tenant inference infrastructure, GPU scheduling, fault isolation, control loops) is squarely relevant.
- **What**: Lessons from building large-scale elastic compute and AI infrastructure: distributed inference architectures, GPU scheduling and elastic compute, multi-tenant inference infrastructure, caching/batching/latency optimization, reliability and fault isolation, observability and control loops, and cost/throughput/UX balancing (from abstract only). The abstract is a topic list with no concrete results, named systems, or affiliations — expect breadth over depth.
- **How**: Not specified at abstract level; likely an architectural-patterns survey.
- **Where applicable**: Large inference platform operators; attend if the Core inference talks leave gaps, but this is the least substantiated item in the set.

### Modular: Taming the AI Hardware Cambrian Explosion

**Links:** [Recording](https://www.youtube.com/watch?v=7BcQdtRA3Tc)

Speakers: Abdul Dakkak (Modular)

- **Why**: Rewriting kernels for every accelerator vendor is not sustainable, and performance portability across NVIDIA, AMD, Apple Silicon, and CPU is a real strategic question for heterogeneous fleets. But this is a platform session with vendor-reported numbers — adjacent, not core.
- **What**: Modular's pitch: Mojo kernels, the MAX compiler and runtime, and Modular Cloud together optimizing GenAI workloads from model graph to hardware execution, with claimed 10x lower latency on FLUX2 and 5.5x higher throughput on Kimi K2.5 over the state of the art (from abstract only). These are vendor-reported benchmarks — treat as claims to verify on your own workloads, not results.
- **How**: The genuinely transferable content is the bottleneck taxonomy for production inference — memory movement, batching, KV-cache layout, quantization, scheduling, kernel specialization — and the discussion of where performance-portability abstractions leak.
- **Where applicable**: Heterogeneous accelerator deployments; a commercial-platform session, so weigh the analysis over the multiples.

### Are LLM Performance Benchmarks Reliable?

**Links:** [Recording](https://www.youtube.com/watch?v=l1-D89bAuOA)

Speakers: Ashok Chandrasekar, Jason Kramberger

- **Why**: Public inference benchmarks disagree wildly — vLLM vs. SGLang numbers, analyst reports — and often fail under real-world conditions; measurement hygiene matters to anyone making capacity or engine decisions from published data.
- **What**: Root causes of inconsistent LLM serving benchmarks: single-process load-generation tools constrained by the Python GIL, model-level settings like temperature, undisclosed load-generation parameters (QPS, concurrency), and insufficient observability into the benchmark clients themselves. Plus Inference Perf, an open-source multi-process utility for reliable stress testing of production stacks (from abstract only).
- **How**: Multi-process load generation with explicitly reported parameters and client-side observability, so the load generator is not the bottleneck being measured.
- **Where applicable**: Universal — anyone benchmarking inference stacks; the pitfalls (GIL-bound clients, unreported concurrency) apply to every serving comparison, published or internal.

### Your LLM Stack Is a 2008 Database With Better Marketing: Why ML Security Is Dominated by Misconfiguration, Not Missing Features

**Links:** [Recording](https://www.youtube.com/watch?v=XjI-AR4pt7Y)

Speakers: Lovina Dmello (sponsor session)

- **Why**: ShadowRay exposed over a billion dollars of data through a missing default config — not a zero-day — and that pattern is the rule in production ML. Useful security context for the multi-tenant GPU infrastructure the PM operates.
- **What**: A synthesis of 139 peer-reviewed papers with five findings: misconfiguration (not missing features) is the dominant failure mode; adversarial defenses impose 15–30% inference overhead, which is why almost no production system runs them; ML-specific security tooling lags general DevOps tooling by years; security/data-science/ops expertise silos create persistent gaps; and LLM/multi-tenant GPU threats (prompt injection, RAG poisoning, GPU side channels) evolve faster than defenses. Plus a four-pillar defense-in-depth framework, a six-category threat taxonomy, and a four-level security maturity model (from abstract only).
- **How**: Literature synthesis plus framework construction; the "which 3 misconfigurations account for most of the risk" claim is a talk deliverable to verify against the slides.
- **Where applicable**: Production ML/LLM platforms generally, especially multi-tenant GPU serving; sponsor session, so expect a product tie-in, but the paper synthesis gives it substance.

### Move fast and (don't) break things

**Links:** [Recording](https://www.youtube.com/watch?v=uKUA1a0Kdfc)

Speakers: Ben Dicken (PlanetScale)

- **Why**: AI backends are being asked for 4-nines availability under unprecedented demand; database fleets already solved this class of problem, and the principles transfer to all reliable infrastructure, AI backends included.
- **What**: PlanetScale's principles of extreme fault tolerance — isolation, redundancy, static stability, and back-pressure — applied beyond databases to AI application backends, with concrete production failure modes and the patterns that prevent them (from abstract only).
- **How**: Architecture principles: isolate failure domains, redundant components, static stability (the system keeps working correctly while a dependency is failing), and back-pressure rather than collapse under overload — illustrated with production incidents.
- **Where applicable**: General backend and AI application infrastructure; not GPU- or network-specific, but the static-stability and back-pressure material is solid ops content for cloud platform work.

## Wildcard

### Computer Use at the Edge of the Statistical Precipice

**Links:** [Recording](https://www.youtube.com/watch?v=CTLa_p6iOiY)

Speakers: Pierluca D'Oro

- **Why**: A methodology bombshell: a 1MB replay script that blindly executes a recorded action sequence — never observing the screen — outperforms frontier computer-use agents on prominent static benchmarks. If the PM consumes any agent benchmarks, this changes how to read them.
- **What**: The replay script's expected success rate is proven exactly equal to the source agent's pass@k in deterministic environments — meaning static CUA benchmarks largely measure memorized trajectories, not interactive competence. The talk traces this to two root causes (unprincipled environment design; naive aggregation and pass@k misuse for stateful UI tasks), proposes the PRISM design principles, and instantiates them in DigiWorld: 15 realistic sandboxed mobile apps evaluating agents across 3.2 million verified unique configurations, plus an aggregation framework that correctly handles benchmarks' nested structure (from abstract only).
- **How**: Formal analysis of pass@k semantics in deterministic stateful environments; sandboxed, automatically verified environment construction; nested aggregation accounting.
- **Where applicable**: CUA evaluation specifically, but the pass@k-aggregation critique applies to any stateful, multi-step agent benchmark — broadly relevant to how the field measures agents.

### Beyond Static Intelligence: Evaluating Continual Learning

**Links:** [Recording](https://www.youtube.com/watch?v=iqloyWCGYQQ)

Speakers: Parth Asawa

- **Why**: The first difficult, expert-validated benchmark for whether LLM-based systems genuinely improve with experience — and the headline finding is a useful negative result: dedicated memory systems don't fix the gap.
- **What**: CL-Bench spans six expert-validated domains (software engineering, signal processing, disease outbreak forecasting, database querying, strategic game-playing, demand forecasting), each with tasks sharing learnable latent structure (codebase layout, outbreak dynamics, opponent strategies) that a stateful system can discover online but a stateless one cannot. A gain metric isolates learning from prior capability. Findings: frontier agents frequently overfit to immediate observations or fail to reuse knowledge across instances, and naive in-context learning outperforms systems dedicated to memory management (from abstract only).
- **How**: Task families with shared latent structure across instances; a gain metric separating within-benchmark learning from base model capability; comparison across architectures from naive ICL to dedicated memory systems.
- **Where applicable**: Anyone building or buying "learning" agents or memory products; the negative result on dedicated memory architectures is the signal to carry away.

### What If Your Chip Design Team Moved Like a Single Body?

**Links:** [Recording](https://www.youtube.com/watch?v=0I6aoPSRzVc)

Speakers: Khaled Alashmouny, Abduallah Mohamed

- **Why**: Multi-agent coordination applied to chip design — 30 agents across 10 disciplines on 12-month projects where one miscommunication costs $10–50M and only 14% of chips succeed on first silicon. For a PM with hardware-side interests, this is agentic AI meeting physical-engineering workflows.
- **What**: A multiplayer agent system built on the Anthropic Agent SDK with three alignment layers: a living spec graph ("System of Intent") that propagates changes and detects conflicts in real time, a tribal-knowledge memory layer compounding methodology across projects, and milestone-aware execution that drives EDA tools with full design context. Based on interviews with 15 practitioners across 8 major semiconductor and EDA companies, with the universal finding that teams need alignment infrastructure, not faster copilots — and a candid account of what broke, since coordination tax applies to AI agents too (from abstract only).
- **How**: Spec-hierarchy boundaries enforced at the API level; cross-agent invocations via structured, typed, audited tool calls; change propagation and conflict detection over the shared spec graph.
- **Where applicable**: Chip design is the demo domain and EDA specifics will be domain-locked, but the alignment-infrastructure thesis (shared intent graph + memory + enforced boundaries) generalizes to any long-horizon, multi-discipline engineering organization.

### Harnessing Collective Agent Intelligence for Open Science

**Links:** [Recording](https://www.youtube.com/watch?v=mMNkdYnIVC4)

Speakers: James Zou (Together AI, Head of Frontier Agents)

- **Why**: Agents collaborating and competing on shared infrastructure produced a genuine mathematical result — a real signal of where multi-agent systems are heading, beyond demos.
- **What**: EinsteinArena, a live platform where AI agents collaborate on unsolved mathematical problems and build on each other's results: in April 2026, 48 hours of live multi-agent collaboration improved the best known lower bound for the Kissing Number in 11 dimensions from 593 to 604, surpassing AlphaEvolve. Plus DS-Gym, a unified framework for evaluating and training data science agents, which exposed that models often rely on memorization rather than true analysis, and was used to train a 4B open-source model rivaling much larger frontier models (from abstract only).
- **How**: Shared live infrastructure for agent collaboration/competition with results compounding across agents; evaluation-driven training that separates memorization from analysis capability.
- **Where applicable**: Research-grade agent infrastructure rather than production ops — but the pattern of many agents on shared, evaluated infrastructure producing verified novel results is the direction-of-travel signal.

## Themes

- **Agentic inference breaks the serving stack's assumptions**: the client, not the server, now controls cache lifecycle — making KV cache volatile and pushing routing, eviction, and prefill strategy up to fleet-level schedulers, while tiny latency-critical metadata messages expose the limits of TCP/RDMA transports. The serving layer is being re-architected around cache economics (KV-aware routing, P/D disaggregation, tiered offload, and eventually new transports like Homa).
- **Inference has become a load-balancing and orchestration problem**: fleet-wide schedulers, two-tier inference load balancers with engine-signal feedback, multi-tenant isolation, and elastic compute across clouds and regions — cloud-platform lessons (LB architecture, multi-tenancy, control loops) being re-learned at GPU scale.
- **Failure is the steady state at GPU scale**: thousands of GPUs fail multiple times daily, so the field is converging on automation — self-healing Slurm-on-Kubernetes, idempotent resumable multi-week pipelines, remediation observability — and on *silent* failures (stale cache slots, logprob spikes) as the genuinely hard bug class.
- **The field is auditing its own benchmarks**: multi-GPU kernel codegen (PKB), the CUA replay-script result, continual-learning evaluation (CL-Bench), and LLM serving benchmark reliability (GIL-bound clients, undisclosed concurrency) all attack measurement validity — published leaderboards are no longer trusted at face value.
- **Agent sandboxes are a new infrastructure substrate**: ephemeral, forkable, isolated environments challenge Kubernetes' steady-state design (12x lifecycle-overhead spread across stacks) and pull in network egress control, multi-tenant RBAC, and audit — a genuinely new workload class for orchestrators.
- **Elasticity across silicon and across datacenters**: performance portability across NVIDIA/AMD/Apple and RL training decoupled from rollout across regions both point toward workloads that follow available hardware rather than being pinned to a single reserved cluster.
