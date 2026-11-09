<!--
conference: @Scale: AI & Data 2026
source_url: https://atscaleconference.com/events/ai-data-2026/
generated: 2026-11-09
registry_key: atscale-ai-data-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# @Scale: AI & Data 2026

This event is the AI/data arm of the @Scale family — there is no physical-networking, Kubernetes, or fabric content here (that lives in the separate August @Scale: Networking track). What it does offer is a dense, production-grounded look at the layer directly above the fabric: training/serving infrastructure for ML at hyperscale, and the fast-emerging pattern of autonomous agents operating infrastructure itself. All picks below are written from the published abstracts; the conference page links resolve to the same agenda text with no fuller papers, and no PDFs or slides were available, so nothing here is enriched beyond the abstract.

## Core

### How Meta Scaled AI Training Storage via Data Normalization

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-14) · [Recording](https://www.youtube.com/watch?v=ZyAoUSmbntI)

Sarang Masti, Weiran Liu (Meta)

- **Why**: Training-data storage is becoming a first-order cost driver as sequence-based and multimodal models inflate feature sizes 10–100x. For anyone planning storage and data-path capacity for training clusters, this is a concrete, quantified answer to the duplication problem.
- **What**: A co-designed data and infrastructure change that cut storage cost 10x for Meta's largest recommendation training feature (long user sequences) by eliminating feature duplication in training samples (from abstract only).
- **How**: Features are moved out of the per-request training rows (where a popular content feature could be duplicated a million times) into a high-performance indexing store, with model access-pattern-aware pushdown so the trainer fetches features at read time instead of materializing them per sample.
- **Where applicable**: Meta-specific production setup today, but the normalization-vs-duplication tradeoff and access-pattern pushdown idea transfer to any large-scale ML training data pipeline. The gains depend on read patterns being predictable enough to push down; highly random access would erode the win.

### Citrine: Catching Million-Dollar ML Anti-Patterns Before They Ship

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-25)

Prakash KL, Chenguang Zhu, Shyam Sundar Chandrasekaran, Jon Dyer (Meta)

- **Why**: GPU/accelerator efficiency is now measured in fleet-wide megawatts and billions of dollars, and AI coding agents are reproducing inefficiencies at machine speed. This is one of the few systems that attacks waste at code-authoring time with measured fleet-scale results, and it has a real open-source footprint.
- **What**: An always-on, zero-overhead lint-layer system detecting 45+ PyTorch and Triton anti-patterns, with 4,700+ accepted fixes in 90 days across 10+ product groups, up to 43% improvement on affected Triton kernels, and claimed millions of dollars in annual GPU savings (from abstract only; numbers are the authors' own).
- **How**: Static analysis and AST transformation via LibCST integrated into Meta's arc lint pipeline; every detector ships a deterministic AST rewriter giving one-click suggested edits. It also shifts left by injecting the same rules into LLM code-authoring agents at generation time, plus an attribution methodology tying individual fixes to fleet-scale efficiency wins.
- **Where applicable**: Broadly applicable well beyond Meta — 13 TorchFix rules and 12+ Triton-lint rules are upstreamed into open-source projects, so the pattern (and much of the rule set) is directly consumable. The Meta-specific parts are the arc lint integration and the internal attribution pipeline.

### ASEA: Autonomous Agents for ML Serving Efficiency at Scale

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-23)

Bikash Sharma, Aashik Gowda, Angineh Keshishian, Mia Gu, Michael Fulthorp, Jinfu Leng (Meta)

- **Why**: "ML for infrastructure operations" is a core interest, and this is the most complete production example in the program: an agentic platform running the full optimization lifecycle over a serving fleet drawing hundreds of megawatts, with validated dollar savings.
- **What**: ASEA turns a multi-day, expert-only optimization workflow (stitching telemetry, profiling, and capacity data) into an autonomous fleet-wide loop, claiming tens of millions of dollars in validated efficiency savings; the motivating observation is that service overhead often reaches 50% of total serving footprint (from abstract only).
- **How**: Dozens of specialized single-skill LLM agents (capacity sizing, autoscaling, batching, routing, hardware migration, regression detection) share a unified fleet-wide data foundation and orchestrate discovery → root-cause diagnosis → configuration generation → canary validation → rollout.
- **Where applicable**: Meta-specific serving fleet (CPUs, GPUs, and Meta's MTIA ASICs) and the savings figures should be treated as operator-specific. The architecture — single-skill agents over a shared telemetry/profiling data plane with canary-gated rollout — is a transferable pattern for any large serving or infrastructure estate.

### LP Planner: Synchronization-Aware Sharding Optimization for Large-Scale DLRM Model Training

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-29)

Mine Su Erturk, Greg Macnamara, Caner Gocmen, Isuru Janith Ranawaka, Felicity Liao, Ahmed Shuaibi, Alireza Tehrani, Hammad Ather, Shafeeq Ibraheem, Kaustubh Vartak, Nipun Gupta (Meta)

- **Why**: Sharding embedded-table models across devices is one of the hardest practical problems in large-scale distributed training, and this is a deployed optimizer with production numbers on some of Meta's highest-spend models — exactly the kind of firmly substantiated result worth a PM's attention.
- **What**: A tool that automatically generates DLRM sharding plans, deployed on multiple production models including some of the largest by training spend, delivering up to 8% QPS improvement and 14% peak memory reduction per model launch (from abstract only).
- **How**: The sharding problem is formulated as a linear program that jointly optimizes table placement and partitioning strategy across devices and device memory hierarchies, minimizing peak memory while maximizing training throughput; the "synchronization-aware" part accounts for cross-device sync costs in the objective. It is also integrated into agentic auto-tuning pipelines.
- **Where applicable**: DLRM/embedding-table specific — directly relevant if you run recommendation-model training; less so for dense LLM training. Ongoing work (critical-path modeling, shard-type selection, heterogeneous hardware awareness) indicates current limitations. Production numbers are Meta's.

### Architecting Infrastructure for the AI Native Future: Scaling Autonomous Agents on Google TPUs

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-16) · [Recording](https://www.youtube.com/watch?v=MUxbhxzIMpQ)

Sabastian Mugazambi (Google)

- **Why**: Accelerator infrastructure is squarely in the PM's AIInfra purview, and this is the one talk on the program about purpose-built silicon and its implications for workload placement (recommenders, MoEs, LLM inference, agents).
- **What**: A Google session on how recent TPU generations' architecture supports massive real-time recommendation throughput and the high-speed inference needed for agentic orchestration (from abstract only).
- **How**: Not detailed in the abstract — it promises a walk through TPU architectural innovations and how purpose-built design maps to these workload classes. No methodology or results are stated.
- **Where applicable**: Expect a Google-flavored perspective on TPU vs. GPU tradeoffs — treat it as a vendor-adjacent view of one accelerator ecosystem rather than a neutral comparison. Useful for understanding what TPU-based infrastructure can and cannot absorb; verify claims against the recording.

### Agentic Inference Optimization for RecSys ML models

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-22)

Shuyao Bi (Meta)

- **Why**: GPU inference optimization is core AI infrastructure work, and this replaces a documented, quantified expert bottleneck (~40 hours of manual fusion work per model) with an automated agent — a pattern likely to spread to every ML platform team.
- **What**: An automated optimization agent that detects kernel-fusion opportunities in PyTorch recommendation models, generates and validates Torch FX graph transformations, and converges iteratively — removing the manual per-model fusion effort that went stale as architectures changed (from abstract only).
- **How**: Fusion opportunities are detected from GPU traces plus FX graph structure; the agent then authors graph transformations (replacing operation sequences with fused kernels to cut launch overhead and host-device transfers) and validates them in a self-converging loop.
- **Where applicable**: PyTorch/Torch FX specific, aimed at production inference latency targets for recommender-class models. No headline numbers are given in the abstract, so treat impact as directional until the full write-up; the technique itself is broadly usable wherever FX graphs apply.

### SparkSentry: Autonomous Error Detection, Triage, and Repair for Spark at Scale

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-32)

Varun Srinivas (Meta)

- **Why**: This is the cleanest production example on the program of the full agentic-ops loop — detect → classify → triage → fix → review — running continuously on real fleet failures with concrete throughput and noise-reduction numbers. Anyone thinking about AIOps→autonomous-ops will want this pattern.
- **What**: An autonomous pipeline over Meta's millions of daily Spark jobs: twice-daily runs ingest ~10K errors, produce ~20–50 root-cause clusters, file Phabricator tasks with full investigation context, and delegate fixes to AI agents that locate the bug, write a fix with tests, and submit a diff for human review — eliminating the 7–10 duplicate tasks per error class that manual monitoring produced (from abstract only).
- **How**: A three-stage clustering stack — deterministic regex (36+ patterns), TF-IDF + DBSCAN for unknown errors, then LLM semantic merging (Llama 3.1-70B) — with rate-based severity detection scaled to fleet size, and a multi-layer dedup system (exact cluster ID, flexible title, normalized title with diff migration) to prevent duplicate tasks across runs.
- **Where applicable**: The pipeline is Meta-internal (Scuba, Phabricator), but every stage maps to standard equivalents elsewhere; the layered "deterministic first, ML for the residue, LLM for the remainder" classification and the human-review gate are directly transferable design decisions. Error-fix autonomy is bounded to the Spark codebase context.

### Data Governance in the World of Agents

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-6) · [Session recording](https://www.youtube.com/watch?v=cbjagBWf5aU) · [Materials](https://atscaleconference.com/data-governance-in-the-world-of-agents/)

Komal Mangtani (Meta)

- **Why**: Agents in production is a core interest, and this names precisely why human-era IAM breaks under machine-speed, parallel, persistent agents — identity confusion, entitlement creep, recursive leakage across agent chains — then gives a full defense-in-depth reference architecture.
- **What**: Meta's governance stack for production agents: Isolation Domains (domain-scoped encryption and output closure), Agent Identity (end-to-end attribution distinct from the user), Agent-Aware Access Control (classification-aware ABAC evaluated at query time), AccessMate (zero-standing-permissions triage), CodeGuard (secure codegen/execution guardrails), and DataVM (a unified trusted environment bounding inputs, tools, and outputs) (from abstract only).
- **How**: Rather than bolting IAM onto agent harnesses, controls are evaluated in the data path at query time with classification awareness, permissions default to least-privilege with no standing grants, and each agent action carries its own identity for audit — turning governance into the harness for autonomy.
- **Where applicable**: The named components are Meta's, but this is presented explicitly as a reference architecture, and the failure modes it catalogs (trajectory/embedding/log/tool-output persistence as new data surfaces) are universal to agentic systems. Directly reusable as a requirements checklist for any agent platform.

## Adjacent

### Meta-ML: Supercharging ML Productivity at Scale with AI-Native Infrastructure

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-30)

Niv Taiber, Bar Ulman, Ravali Busetty, Aasim Rab, Brant Swidler (Meta)

- **Why**: Making legacy infrastructure callable by agents — without rebuilding it — is the operational question every platform team now faces, and this gives the architectural patterns plus adoption numbers from a very large fleet.
- **What**: An AI-native layer exposing Meta's legacy ML stack (data discovery through serving and capacity planning) as 200+ agent-callable tools, with 59% power-user adoption, 4M+ tool calls/week, and debugging workflows cut from 1.5 hours to under 10 minutes (from abstract only).
- **How**: Three patterns: progressive tool disclosure (agents discover capabilities on demand instead of loading 200+ tools into context), federated domain-team ownership (15+ infra teams expose their systems as tools, mapped to MLE jobs-to-be-done), and a production-grounded eval flywheel instrumenting real MLE sessions for test cases synthetic benchmarks miss.
- **Where applicable**: The patterns are explicitly framed as transferring to any organization with legacy ML systems — the progressive-disclosure and federated-ownership ideas are general agent-platform design. Adoption numbers are Meta's and depend on having a large internal MLE population.

### XStream: Meta's unified stream processing service

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-34)

Stella Kaval, Zheng Zhang, Shuo Xu, Jun Fan (Meta)

- **Why**: A six-year production consolidation story at O(10) TB/s across 70,000+ pipelines — rare, honest material on unifying fragmented internal platforms and the operational lessons of keeping a managed stream service reliable at that scale.
- **What**: XStream consolidates all of Meta's in-house stream processing onto one fully managed service supporting SQL, Python, and C++ authoring, with exactly-once processing, Scribe-based shuffle, ZippyDB and RocksDB+Manifold state stores, and Kappa architecture for ML feature freshness (from abstract only).
- **How**: A vectorized C++ execution engine built on Velox under a multi-language authoring layer, a service management platform (Turbine), a Unified Trigger Framework for stateful processing, and CodeX decoupling user logic from engine execution.
- **Where applicable**: Meta-specific stack decisions throughout; the value is the consolidation playbook and production experience (scaling, availability, efficiency lessons), which transfer to any operator running multiple parallel stream-processing systems. Velox's appearance here and in the agent-memory poster is a notable shared-substrate trend.

### Scaling Batch Graph Processing to Trillions of Edges

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-31)

Sahil Gandhi, Arneish Prateek (Meta)

- **Why**: Graph jobs at billions of nodes/trillions of edges (LLM pretraining, recommendations, dedup) stress exactly the distributed-systems pathologies — memory blow-up, skewed shards, network overhead, gang scheduling — that any large-scale batch infrastructure has to engineer around.
- **What**: Meta's new batch graph processing engine for iterative graph algorithms at trillion-edge scale, designed around reducing cost across data storage, graph partitioning, network communication, execution, and distributed coordination (from abstract only).
- **How**: The abstract names the constraint set and a pluggable architecture accommodating diverse distributed graph processing models; mechanism-level detail (partitioning scheme, coordination design) is not given in the abstract.
- **Where applicable**: Graph-workload specific; the network-overhead and skew-handling concerns will resonate with anyone operating large sharded data systems. Thin abstract — worth checking the poster or recording for the actual partitioning and coordination design.

### Agent Memory at Meta Scale: One Query Language for Graph, Vector, and Memory

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-20)

Abdullah Ozturk, Yiting Li, Vishal Gandhi, Ming Chen, Junjie Qi (Meta)

- **Why**: Agent memory is becoming a real infrastructure layer, and today's stacks stitch vector indexes, graph services, and RAG frameworks together on the critical path of every agent turn. This proposes treating memory as a query-surface problem — a genuinely architectural move.
- **What**: The Cypher Query Layer (CQL): a declarative query surface over agent memory built on the openCypher/GQL ISO standard, collapsing hybrid retrieval (vector + text + graph + scope + freshness + provenance) into one optimizable query, with identity-aware ACLs as first-class primitives (from abstract only).
- **How**: A pluggable backend routes each query to a right-fit substrate — in-process Velox for sub-50 ms agent-loop reads, reusing Meta's existing graph/vector/hybrid stores — with bi-temporal memory on the roadmap to enable agent-debugging replay, and procedure packs for distillation/consolidation/governance.
- **Where applicable**: The standard-based query surface is broadly interesting; the substrate choices are Meta's. The in-process vs. distributed boundary discussion is exactly the kind of design decision that transfers. Early-stage — production patterns come from one early internal consumer.

### Evaluating Opsmate: Grading AI Incident Investigations at Scale

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-27)

Chinmay Gandhi, Narayanan Sankaran, Khushbu Thakur, Ankit Agarwal, Vaidyanathan PK, KC Balsu, Akash Jothi (Meta)

- **Why**: Everyone is deploying incident-investigation agents; almost nobody can answer "did it do a good job?" This tackles the evaluation gap for an agent handling ~1.5K incidents/day — the hard prerequisite for trusting autonomous ops.
- **What**: Opsmate Evals: an orchestrator- and model-agnostic framework for scoring autonomous incident investigations, combining automated ground-truth synthesis from post-incident artifacts with LLM-as-judge graders scoring 0–100 on root-cause accuracy, investigation path logic, and mitigation actionability (from abstract only).
- **How**: Ground truth is synthesized from chat transcripts, fix diffs, and retro docs rather than hand-curated, sidestepping the expensive-labeling problem; calibrated judge graders cover the multi-dimensional, subjective notion of "correct."
- **Where applicable**: General pattern for any org running incident agents — the ground-truth-synthesis idea works wherever post-incident artifacts exist. Calibration and judge reliability are the unvalidated parts; treat scores as a starting point, not ground truth.

### Cache the Session, Not the Data: 40x Faster ML Iteration with a Shared Sidecar at Meta

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-24)

Rohil Bansal, Eric Fu (Meta)

- **Why**: A small, sharply executed piece of systems engineering with a measured ~40x improvement (391s → 9s) on the developer inner loop — the kind of operational win that transfers to any ML platform with a preprocessing cold-start tax.
- **What**: The Shared Sidecar (SSC), an out-of-process daemon caching warmed data-preprocessing sessions across local runs, rolled out to all Meta developer workstations by default with no correctness regressions (from abstract only).
- **How**: Sessions are keyed on a hash of input dataframe + preprocessing plan; matching reuses a pre-warmed session and skips session setup, query optimization, metadata lookup, and reader warm-up. Lifecycle is bounded (8h idle eviction, 1h process timeout, capped session count) with graceful degradation if the daemon dies.
- **Where applicable**: General technique, not Meta-specific — any environment where preprocessing startup dominates iteration. The 5-minute cold start is environment-dependent, so measure your own baseline first. Single-benchmark evidence (a CTR model); the "no correctness regressions" claim is the authors'.

## Wildcard

### Designing for Human Agency in AI-Augmented Software: A Quality Attribute Approach

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-26)

Rohan Vardhan

- **Why**: Not infrastructure at all — but a genuinely novel framing: treating human-centeredness as a measurable software quality attribute (like performance or security) rather than a design philosophy, which changes how AI features would be specified and tested.
- **What**: An argument that ISO/IEC 25010:2023 and similar quality models don't capture what makes AI-augmented software supportive rather than corrosive to human judgment, proposing the ACCL framework — Agency Preservation, Calibrated Trust, Contestability, Learnability of Limits — plus three previously undocumented failure modes: reflexive bypass, trust debt, and the right-sized explanation problem (from abstract only).
- **How**: For each attribute, architectural implications and organizational patterns grounded in field observation across multiple organizations; the failure modes come from practitioner experience rather than formal study.
- **Where applicable**: Conceptual/framework work rather than a deployed system — no empirical validation claimed. Useful as a vocabulary for anyone writing requirements for AI-assisted internal tools (including agent platforms of the kind the rest of this program deploys).

### Agentic Data Flywheel: A Multi-Agent System for Scalable Multimodal Training Data Production

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-21)

Wendy Jiang, Selahattin Akkas, Alan Li, Antoine Simoulin (Meta)

- **Why**: Off the PM's beaten path (data annotation), but a well-instrumented multi-agent design with a surprising result: multilingual bootstrapping turned a per-language staffing bottleneck into a prompt configuration change across 100+ languages.
- **What**: A multi-agent annotation pipeline — specialist VLM labeler, parallel quality reviewers with summarizer, self-correcting adjuster, and a thinking-model judge — delivering a 3x efficiency gain with 60%+ of annotations needing no human involvement; remaining cases go to humans prefilled with agent corrections (from abstract only).
- **How**: Probabilistic VLM reasoning wrapped in deterministic scaffolding: agent isolation to prevent confirmation bias, deterministic routing around probabilistic judgment, and structured closed-choice output constraints with every failure mode defaulting to human escalation.
- **Where applicable**: Demonstrated on image-text labeling with claimed generalization to scene understanding, chart/document VQA, and grounding. The escalation-defaults-to-human principle is the transferable design lesson for any probabilistic-agent pipeline.

### The Agent Feed: A Communication Layer for Multi-Agent Collaboration

**Links:** [Abstract](https://atscaleconference.com/events/ai-data-2026/#agenda-item-33)

Chinmay Gandhi, Vlad Tsvang, Patrick Walsh (Meta)

- **Why**: Signals where multi-agent systems are heading: when many agents work the same problem, the missing primitive is a shared, trust-ranked communication layer — an early stab at what agent-to-agent interoperability might look like.
- **What**: A standardized API where agents publish findings, read each other's outputs, and collaborate: specialist agents contribute evidence, a coordinating agent ranks competing hypotheses against independent sources, and human thumbs-up/down feedback shapes which findings and agents get promoted (from abstract only).
- **How**: A tiered channel system ranks agent output by trust level (Core > Validated > Experimental) with self-serve onboarding and quality-gated graduation, so responders always see highest-confidence findings first; consensus strengthens as independent signals corroborate.
- **Where applicable**: Built for incident-response context at Meta but explicitly generalized: wherever multiple agents operate on a shared artifact, you need a structured communication layer, a consensus mechanism, and a trust framework. Early-stage pattern, no scale numbers given.

## Themes

- **Agents have moved into infrastructure operations.** ASEA, SparkSentry, Opsmate, the warehouse-autonomy work, and Meta-ML collectively show the loop from detection to root-cause to fix to rollout closing with humans moved to review and feedback positions. The recurring design questions are no longer "can the agent do it" but guardrails, trust tiering, auditability, and — hardest — evaluation of open-ended agent behavior.
- **Efficiency is the headline metric, in dollars and megawatts.** With serving fleets drawing hundreds of megawatts and industry GPU spend in the tens of billions, nearly every infrastructure pick frames its contribution as waste eliminated: Citrine (fleet-wide GPU waste), ASEA (50% service overhead), LP Planner (memory/QPS), storage normalization (10x), inference fusion (latency). Code-time efficiency enforcement is pitched as a necessary layer of the AI compute stack, precisely because agent-authored code now reproduces inefficiencies at machine speed.
- **Co-design with model access patterns.** The strongest infra results come from shaping storage and execution around how models actually read: feature normalization with access-pattern-aware pushdown, session-keyed caching, synchronization-aware sharding, and Fusion detection from GPU traces. Generic capacity-add scaling is explicitly out of fashion.
- **Identity and governance are being rebuilt for machine-speed actors.** Both the governance talk and the agent-memory work treat attribution, classification-aware access control, and ACLs as first-class platform primitives rather than add-ons — the IAM concepts a networking/infra PM knows, re-derived for agents.
- **Platform consolidation behind single interfaces.** XStream (unifying stream processors), Meta-ML (unifying ML tooling), and CQL (unifying memory retrieval) all reflect the same hyperscaler reflex: federate the backends, expose one query/tool/authoring surface.
- **A gap worth naming for this audience:** nothing on physical DC, fabrics, optics, Kubernetes, or dataplane internals — the AI infra conversation at this event sits entirely above the accelerator cluster boundary, and the networking-side content is deferred to the separate @Scale: Networking event.
