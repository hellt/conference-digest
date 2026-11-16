<!--
conference: AI Engineer Code Summit 2026
source_url: https://ai.engineer/code/2026/sessions.json
generated: 2026-11-16
registry_key: aiengineer-code-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AI Engineer Code Summit 2026

A framing note before the picks: this program is almost entirely about agentic coding — harnesses, software factories, verification, and agent ops. There is no physical-networking, optics, or Kubernetes content here at all. What it does offer the networking/cloud PM is a dense look at the *workload side* of the AI infrastructure equation: how agentic systems actually consume inference, GPUs, sandboxes, and platform services, and what operating them at scale teaches. The picks below lean into that angle.

No `page:`/`pdf:`/`slides:` links appear in the program text, so every write-up below is grounded in the published abstract only.

## Core

### Inference Engineering for Coding Agents

Philip Kiely

- **Why**: Coding agents are the dominant paying workload for LLM inference right now, yet mostly run on general-purpose serving stacks. This is one of the few talks that treats agentic inference as a distinct optimization domain — directly relevant to anyone building GPU-serving infrastructure.
- **What**: A catalogue of inference techniques specialized for coding-agent traffic: targeted quantization/pruning for code models, domain-specific post-training, KV cache management around context-compaction events, subagent session affinity under autoscaling, and code-specific speculative decoding. (from abstract only)
- **How**: Frames inference as a constrained optimization problem where the constraints (agent traffic patterns: long contexts, compaction, many small subagent sessions) are known and exploitable — e.g., pinning subagent sessions to backends for cache locality, speculating from n-grams in code rather than only model heads.
- **Where applicable**: General techniques for anyone operating an inference service dedicated to agent traffic; the speculative-decoding discussion spans both model-based approaches and deterministic n-gram speculation, so parts apply even without custom silicon or a large fleet.

### Keep the Harness, Own Your Inference

Francisco Javier Arceo

- **Why**: Speaks directly to the decoupling of agent harnesses from serving infrastructure — the same architectural question the PM faces in cloud platform work, applied to the AI stack.
- **What**: A hands-on path to running familiar coding harnesses (Claude Code, Codex) against open-weight models on self-owned hardware — from a DGX Spark on a desk to distributed serving on vLLM, SGLang, NVIDIA Dynamo, and llm-d — based on the speaker's work building the vLLM Agentic API. Also unpacks Codex Cloud's Responses API as an agentic server layer. (from abstract only)
- **How**: Standardizes an agent-facing API layer that preserves conversation state, tool handoffs, streaming, memory/retrieval, and compaction across serving backends, so harness, model, and serving infrastructure become independent choices.
- **Where applicable**: Broadly applicable to private/on-prem AI deployments; the cluster-scale portion depends on vLLM/llm-d/Dynamo-style distributed serving stacks and adequate GPU capacity. The analysis of what the server-side agentic layer owns (state, memory, compaction) generalizes regardless of backend.

### What Will You Build When AI Is 10x Faster?

Natalie Serrino (Gimlet, per abstract)

- **Why**: Inference latency is a product-design and infrastructure-planning variable. This talk connects the speed of the serving layer (GPUs plus specialized accelerators) to what agent architectures become feasible — useful input for capacity and accelerator-roadmap thinking.
- **What**: An exploration of what materially faster inference unlocks: agents that can try-test-update within seconds, voice assistants that finish reasoning before the pause, and when it is worth paying for speed versus when other parts of the application become the bottleneck. (from abstract only)
- **How**: Argues from product cases where response-time budgets shape architecture, and describes how Gimlet combines GPUs with specialized accelerators to deliver that speed.
- **Where applicable**: The product framing is general; the acceleration claims are Gimlet-specific and unquantified in the abstract — treat the "10x" as directional rather than measured.

### The Rise of the Agent Workforce: Rethinking Agent Infrastructure

Ankit Mathur

- **Why**: The infrastructure requirements of persistent, multi-agent systems (long-lived sandboxes, memory, inter-agent communication) are exactly the kind of workload shift that changes what cloud platforms must provide.
- **What**: A case that agent platforms need fundamental re-architecture as agents move from interactive chat to persistent, collaborating workforces — stateful sandboxes, persistent memory, agent-to-agent communication, and orchestration. (from abstract only)
- **How**: Examines why today's platforms (built for request/response chat) fail for long-running, multi-agent work, and sketches the emerging architecture for it.
- **Where applicable**: General architectural argument, not tied to a specific stack; the abstract stays at the pattern level, so expect concepts rather than validated numbers.

### Coding Agents and How to Tame Them

Ivan Leo (Google DeepMind, per abstract)

- **Why**: One of the few sessions with large-scale, systematic evidence — a trace-by-trace audit of 50+ coding benchmarks and a platform for evaluating frontier agents — plus hard operational lessons from air-gapped sandbox construction.
- **What**: Findings from auditing 50+ coding benchmarks trace by trace with Kaggle, including weird real-world failure modes, and lessons for building harnesses, verifiers, and coding environments. (from abstract only)
- **How**: Benchmarks treated as measurable artifacts: audit the traces, not the scores; build isolated (air-gapped) evaluation environments; derive harness/verifier design from observed failure modes rather than assumptions.
- **Where applicable**: The failure-mode and verifier-design lessons transfer to any team evaluating agents; the air-gapped sandbox work is Google-scale but the isolation principles are general. Short format (18 min), so expect density over depth.

### Scaling Your Agent Workforce: Lessons from Inside Cognition

Theodor Marcu (Cognition, per abstract)

- **Why**: A concrete production data point on fully-autonomous agent operation: 92% of merged PRs written by Devin, 9 of 10 sessions starting without a human. That level of autonomy is where the whole field is heading, and this reports what it took.
- **What**: How Cognition scaled to agents writing most merged code: cloud agents working in parallel, nightly automations, and autonomous feature development — turned into a playbook covering governance of what agents can reach, model routing for cost, and per-session ROI tracking to merged PR. (from abstract only)
- **How**: Parallel cloud agent execution plus event-driven automations, with cost control via routing work across models and measurement discipline (every session traced to a merged PR so ROI is measured, not guessed).
- **Where applicable**: Cognition-specific numbers reflect a company whose product *is* the agent; the governance/routing/measurement playbook is transferable, but expect the 92% figure to depend on Cognition's own codebase and tooling.

### Building a Shared AI Assistant: The Platform Challenges Beyond MCP

Utkarsh Shrivastava (Netflix, per abstract)

- **Why**: This is a platform-engineering talk in disguise, and a good one: what happens when a large org moves from team-owned integrations to a shared, multi-tenant AI assistant — the same questions of ownership, gating, and federation any cloud-platform PM deals with, now for tool access.
- **What**: Netflix's experience as product teams ship their own MCP servers: the resulting entity-version conflicts and routing ambiguity, and the mechanisms built in response — connector certification, an internal benchmark built from real employee queries to evaluate routing between overlapping tools, and action classification separating what an agent may do autonomously from what needs a human. (from abstract only)
- **How**: Moves the control point from tool descriptions to platform mechanisms: certification of connectors, benchmark-driven routing decisions, and explicit action-gating, with honest coverage of unsolved problems (authoritative entity ownership, connector retirement).
- **Where applicable**: Netflix-specific in scale and org structure, but the pattern — shared platform vs. team-owned tools, who owns the gate — is a general federated-platform problem. The open questions at the end are as valuable as the solutions.

### Heal Your Agents, Don't Just Grade Them

Khasimul Asif Mohammad, Sudhir Tonse

- **Why**: Operating agents at millions of sessions per day is an observability and anomaly-detection problem — detecting rare, novel failure patterns across sessions is structurally the same problem as network anomaly detection, and the economics discussion (what to screen with, what earns a closer look) maps directly onto tiered telemetry pipelines.
- **What**: The engineering tradeoffs in moving from eval-based grading to continuous failure detection and repair at production scale: screening economics (you can't run a reasoning model over every session), collapsing thousands of flagged sessions into root causes, and verifying agent-proposed fixes before merge. (from abstract only)
- **How**: A tiered detection pipeline — cheap screening over all sessions, deeper analysis for flagged ones, root-cause clustering to rank fixes — plus trust criteria for merging agent-generated remediation PRs.
- **Where applicable**: General pattern for anyone running agents in production; drawn from "customers running agents at scale" and the speakers' own agents, so specific thresholds will be org-dependent but the architecture transfers.

## Adjacent

### cloudflare is a neolab

Michelle Chen (Cloudflare, per talk content)

- **Why**: Signals where one of the major edge-cloud operators is placing bets: trained "system one" models integrated into a decade-old Workers/edge primitive set, aiming to be the "agent cloud."
- **What**: A short keynote positioning new small/fast models (clef, clairic) inside Cloudflare's existing edge platform, connecting the edge-latency hypothesis for Workers AI to an ambition of being the default execution substrate for agents. (from abstract only)
- **How**: Edge inference: small models colocated with existing compute primitives so agent decisions happen close to users and data.
- **Where applicable**: Cloudflare-specific strategy talk; the abstract is thin, so treat it as directional signal about edge-vs-central inference economics rather than substantiated results.

### 2026 in LLMs

Simon Willison

- **Why**: Reliable annual field recap from a consistently grounded observer — useful calibration on model releases, open-weights competitiveness, export controls, and agent-era security incidents.
- **What**: A recap of the year since the coding-agent inflection point: the OpenClaw craze, tokenmaxxing's rise and fall, US export controls on frontier AI, competitive open weights, cyberattacks by rogue agents, and new model classes. (from abstract only)
- **How**: Wide survey talk, not a technical deep-dive.
- **Where applicable**: General-audience overview; worth 20 minutes for the export-control and open-weights threads alone, which bear directly on accelerator supply and model strategy.

### Multiplayer software factories

Patrick Debois

- **Why**: When every engineer runs agents that all land on one main, continuous delivery itself becomes the bottleneck — this maps the failure modes and fixes, which is CI/CD and release-engineering territory any platform PM lives in.
- **What**: An analysis of what breaks when a software factory goes "multiplayer" (many concurrent agents producing changes against shared trunk), and the patterns that fix it — summarized as "one main for the agents, one board for the people." (from abstract only)
- **How**: Separates the agents' integration plane from the humans' coordination plane, reworking CD assumptions built for human-speed, serial merge queues.
- **Where applicable**: General delivery-pipeline patterns; the abstract is brief, so expect principles rather than a validated mechanism catalogue.

### Post-Training Gemini 4 for Real Engineering Work

Melvin Johnson (VP, Google DeepMind, per program text)

- **Why**: A rare inside view of post-training for long-horizon agentic work — the recipe decisions (graders that can't be gamed, rewarding honest self-reporting) shape what the models your infrastructure serves will actually be like.
- **What**: How Gemini was post-trained for multi-hour coding tasks: internal realistic multi-step benchmarks beyond saturated public ones, game-resistant graders that check work like a reviewer, rewards for accurately reporting what was and wasn't done, and token-efficiency across very long contexts, shipped on weekly cycles. (from abstract only)
- **How**: Benchmark construction (internal, realistic, multi-step) plus grader design that detects agents satisfying unit tests without solving the problem — a concrete instance of the verifier-is-the-bottleneck theme.
- **Where applicable**: Google-specific post-training practice; the grader-design and honest-reporting lessons transfer to anyone building evaluation or verification for agents.

### I deleted 90% of my harness (And It Got Better)

Philipp Schmid

- **Why**: A Bitter-Lesson argument applied to agent harness design — that hand-built tools and elaborate prompts lose to general capability plus compute. This shapes what harness/agent platforms should even provide, and by extension what infrastructure layers matter.
- **What**: The speaker's practice of periodically deleting everything: stripping an agent to Bash as the only tool, cutting the prompt to 300 tokens, making the loop asynchronous — and reporting that benchmark scores and experience both improved. (from abstract only)
- **How**: Relies on frontier models synthesizing ad-hoc pipelines (AST parsing, ripgrep, git, subshells) in real time instead of using dedicated edit/search tools — general methods backed by compute beating encoded human heuristics.
- **Where applicable**: Applies to harness design on any strong frontier model; the premise is model-dependent — the argument strengthens as models improve, so it may not hold for smaller/self-hostated open-weight models, which is a real caveat for the self-owned-inference path.

### Your agent pays twice for every search: how we cut token spend by 90+% with better accuracy

Louis Walsh

- **Why**: One of the better-substantiated cost results in the program: 12 frontier models, 11,000 blind-graded answers, >90% token-spend reduction with accuracy gains. Inference cost is a first-order constraint on agent workloads, and this quantifies where it actually goes.
- **What**: Production traces showing that retrieval, not generation, dominates agent token bills (agents pay for whole pages when they need sentences, and re-pay on every loop turn), and the changes that fixed it. (from abstract only)
- **How**: Return query-relevant passages instead of pages, tune extraction to the question, cap how much context the agent can take; measure cost per correct answer rather than per request, with an open calculator for readers to run on their own traffic.
- **Where applicable**: General technique for any agent pipeline; the numbers are the speakers' own product but the methodology (blind grading across 12 models, cost-per-correct-answer) is the transferable part.

## Wildcard

### Ground Truth or Dare: Using Oracles to Make Postgres Reactive

James Arthur (Electric → Neon, per abstract)

- **Why**: Not about agents per se — it's database infrastructure (live, reactive SQL queries inside Postgres) built largely by coding agents, with correctness guaranteed by using Postgres's own query engine as a verification oracle. A genuinely different pattern: the target system verifies its own construction.
- **What**: The story of building live SQL queries (subscribe to any query with joins/aggregates/ordering, results stay live) — years of failed hand-building at Electric, then weeks with agents at Neon once agents could check their own work against the database engine as ground truth. (from abstract only)
- **How**: Agents iterate against an oracle (the real query engine) that deterministically validates behavior, letting them move fast on infrastructure-grade code where "hope for the best" is unacceptable.
- **Where applicable**: The oracle principle generalizes to any system with a checkable specification (protocols, configs, network behaviors are obvious candidates); the specific achievement is Postgres-internal and Neon-specific.

### Autocomplete for Actions: System One from the UI to the DB

Scott Roberts (Workday, per abstract)

- **Why**: A surprising architectural placement of small models: not behind an API, but embedded in the database — running as a SQL filter inside DuckDB to pick the next user action while they type. Signals a direction where tiny models become a query-plan component.
- **What**: How Workday's Sana uses a small "System One" model at two ends of the stack: choosing the right action card in the UI as the user types, and executing inside DuckDB as a SQL filter — skipping full LLM turns for simple requests entirely. (from abstract only)
- **How**: Route bounded decisions (too simple for a generative turn) to fast, cheap models colocated with the data, reserving LLM turns for genuinely open-ended work.
- **Where applicable**: Workday-scale product context, but the pattern — small models executing in-process where the data lives — is broadly adoptable and relevant to anyone weighing inference placement.

### The True Cost of AI Coding

Scott Tolinski

- **Why**: Not infrastructure, but a ~4,000-respondent survey of developers on how agentic workflows affect mental health — the human cost side of the software-factory trend everyone else at this conference is celebrating.
- **What**: Survey results from nearly 4,000 developers on the mental-health effects of AI coding workflows, with analysis of what is happening and why. (from abstract only)
- **How**: Survey methodology; details of sampling and questions aren't published in the abstract.
- **Where applicable**: Industry-wide rather than org-specific; treat as one data point — the abstract doesn't describe methodology, so weight accordingly.

## Themes

- **Verification is the new bottleneck**: across the program, generation is solved and trust is not — oracles, deterministic checks, layered security, benchmark audits, and "review systems, not diffs" appear in nearly every strong session.
- **Inference economics inverted**: multiple talks converge on the same finding — the model is no longer the cost; context, retrieval, and tool plumbing are. That inversion drives architectural choices (passages not pages, System One models in the DB, screening tiers for observability).
- **Software factories are an infrastructure story**: stateful sandboxes, persistent memory, environments inside customer VPCs, orchestrators with shared context — the agent-workforce literature reads like a cloud-platform requirements doc.
- **Harness minimalism vs. platform build-out**: a visible tension between deleting the harness (Bitter Lesson: give the model Bash and get out of the way) and building ever-richer platform layers (memory, orchestration, certification) around agents.
- **Autonomy is earned and measured**: the credible production reports (Cognition's 92% of merged PRs, PostHog's 6,000 PRs, Netflix's shared assistant) all pair increased autonomy with explicit measurement, gating, and rollback discipline — ROI measured per session, not guessed.
- **Zero networking content**: nothing on fabrics, optics, Kubernetes, or serving-network internals — a reminder that the AI-systems conversation at the application layer has not yet absorbed infrastructure concerns, which is arguably the gap this PM's domain occupies.
