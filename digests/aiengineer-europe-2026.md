<!--
conference: AI Engineer Europe 2026
source_url: https://ai.engineer/europe/2026/sessions.json
generated: 2026-11-11
registry_key: aiengineer-europe-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AI Engineer Europe 2026

This program is AI engineering end to end — there is nothing here on physical datacenter networking, optics, or fabrics, so the Core picks below are the items that sit squarely at the intersection of the PM's cloud, Kubernetes, and AI-infrastructure work: agents as a new class of infrastructure workload, GPU/inference systems, and AI applied to operations.

*Sourcing note: the program text carries no links and no source documents were available, so every write-up below is based on the abstract only. Vendor-run benchmarks and unfalsified claims are flagged as such.*

## Core

### Lawrence Jones - Fighting AI with AI

Lawrence Jones — incident.io

- **Why**: The most direct instance of "ML for infrastructure operations" in the program: an autonomous AI SRE that investigates production incidents by digging through logs, metrics, traces, and code changes, plus the meta-tooling needed to operate such a system.
- **What**: incident.io's AI SRE — a deeply nested tree of agents working ambiguous problems against nondeterministic telemetry — and the internal tooling built to debug it: an eval CLI with red-green runbooks agents can follow end-to-end; agent traces serialized as markdown so other agents can reason about them (turning hour-long debugging into five-minute conversations); a pipeline of 25 parallel agents each analyzing an investigation, then clustering results to surface systemic patterns; and AI dogfooding feedback loops.
- **How**: Give agents the same debugging information engineers use, in agent-readable formats (serialized traces, structured runbooks), then use parallel AI analysis to surface patterns humans act on.
- **Where applicable**: The speaker explicitly states none of it requires exotic infrastructure — patterns transfer to any team operating complex agent systems. The product context is incident.io-specific, the meta-tooling patterns are general.

### Scaling Agents on Kubernetes with acpx and ACP

Onur Solmaz — maintainer of OpenClaw, creator of acpx

- **Why**: Running dozens of coding agents in parallel on Kubernetes is becoming a real ops pattern, and the current way teams talk to agent harnesses — scraping PTYs — is brittle. This is the agent-fleet-on-K8s problem directly.
- **What**: acpx, a headless CLI client for the Agent Client Protocol (ACP), and an architecture for massively parallel PR triage and bug fixing using disposable agent pods, with a live demo of acpx v0.4's node-based graph system driving multiple coding agents through routine engineering tasks.
- **How**: ACP replaces PTY scraping with structured, protocol-driven agent communication; acpx unifies harnesses (Claude Code, Codex, etc.) behind one interface usable from terminal, Telegram, or Discord, and a deterministic node-graph orchestrates steps across agents in disposable pods.
- **Where applicable**: Kubernetes environments running agent workloads. Protocol-based rather than tied to one harness or scale, but it depends on harnesses adopting ACP; v0.4 maturity, so treat results as early.

### CI/CD Is Dead, Agents Need Continuous Compute and Computers

Hugo Santos, Madison Faulkner — Namespace case study; backgrounds include Google microservices-scale infra (per abstract)

- **Why**: When thousands of agents continuously open PRs and trigger builds across hundreds of repos, the pipeline layer — runners, caches, registries — becomes the latency and cost bottleneck. This reframes CI/CD as a core AI-infra systems problem, squarely in cloud-ops territory.
- **What**: Concrete failure modes of traditional CI/CD under agent load (runner saturation, cache thrash, cold Docker builds, test explosion, opaque flakiness), and a blueprint for an agent-ready pipeline layer: intelligent execution over GitHub Actions, remote caching and Turbo-style Docker builds, Git-aware incrementality, and workflow analytics tying time and spend to specific jobs, repos, and agents — claimed to sustain 5–10x more changes without blowing up latency or budgets.
- **How**: Treat CI as a high-performance system: ephemeral high-performance clusters, registries optimized for build workloads, per-job cost/latency attribution, and interactive debugging for agent-authored changes.
- **Where applicable**: Orgs with high agent-driven PR volume on GitHub Actions. Namespace is the vendor and this is a product case study — the failure-mode analysis transfers broadly, the solution specifics are Namespace-shaped.

### The Embedding Infrastructure Nobody Built (So We Did)

Filip Makraduli

- **Why**: Embedding serving is a quiet but ubiquitous piece of AI infrastructure, and existing engines (TEI, Infinity) have real operational gaps — one model per container, crashes under load, no story for multiple models contending for GPU memory.
- **What**: An embedding inference engine built around what the ecosystem lacked: models loaded at query time rather than deploy time, hot-swapping dozens of models on one GPU without restarts, LRU eviction on memory pressure instead of OOM crashes, and trying a new model without a rebuild. Includes profiler traces showing attention is only ~6% of the embedding workload — invalidating the author's own (and common) Flash-Attention-centric optimization advice.
- **How**: Query-time model lifecycle on shared GPU capacity with memory-pressure-driven eviction, grounded in actual profiling of the memory hierarchy rather than assumed bottlenecks.
- **Where applicable**: Any team serving multiple small models on shared GPU capacity — a general technique, not org-specific. It is the speaker's own product, so weigh it as vendor experience, but the profile-before-optimizing lesson is transferable.

### Everything I Learned Training Frontier Small Models

Maxime Labonne

- **Why**: Small models that reliably follow instructions and call tools while running on-device under 1 GB change where inference happens — off GPU clusters and onto edge devices — which matters for anyone planning AI infrastructure capacity.
- **What**: A post-training playbook for frontier small models using the LFM2.5 recipe: on-policy preference alignment, agentic RL, and curriculum training with iterative model merging — plus the failure modes specific to 1B scale ("doom loops", capability interference) and how to fix them. Targeted at structured data extraction and multi-turn tool use.
- **How**: Staged post-training (preference alignment → agentic RL → curriculum with iterative model merging) tuned for the constraints of sub-1B models.
- **Where applicable**: Fine-tuning and deploying small models for concrete use cases; recipe-level guidance transfers, though the exact recipe is tied to the LFM2.5 stack. Abstract-level only — expect depth in the talk itself.

### Live Demo & Q&A with Together AI

Max Ryabinin, VP of Research & Development, Together AI — expo session "Road to 5M Sequence Length: Breaking Memory Barriers in Context Parallelism"

- **Why**: Long-context training (hundreds of thousands to millions of tokens for video generation and agentic pipelines) hits the memory and compute wall of attention — context parallelism is how training clusters get past it, which is model-training infrastructure directly.
- **What**: Techniques for finding and optimizing bottlenecks in long-context training, and Untied Ulysses, Together AI's latest method claiming a ~25% boost in achievable training context length over prior approaches.
- **How**: Context parallelism — partitioning sequence/attention work across devices to break the memory barrier, with the "Untied" variant relaxing a constraint of prior Ulysses-style methods for the additional headroom. Method details beyond this are not in the abstract.
- **Where applicable**: Training and fine-tuning very-long-context transformers on multi-GPU clusters. The 25% figure is the vendor's own claim, and the 18-minute expo format means breadth over depth — worth a look, not a deep dive.

### Your Coding Agent Should Do AI System Engineering

Ben Burtenshaw — Hugging Face (per abstract)

- **Why**: If coding agents can now write CUDA kernels, fine-tune models, and run full ML experiments, that changes who does AI systems engineering — directly relevant to anyone running GPU/accelerator infrastructure or ML platform teams.
- **What**: Hugging Face's integration of agent skills into the ML stack, with concrete numbers: an agent-written RMSNorm kernel hitting 1.88x speedup on H100s, a fine-tuned Qwen3-0.6B reaching 35% on LiveCodeBench, and HF teams running 1,000+ ML experiments daily without handwritten training scripts. Includes benchmarks across six models on kernel-writing, where agents fail badly, and a trust-but-verify playbook (open-source skill files, upskill CLI).
- **How**: Loadable "skills" give coding agents (Claude Code, Codex, Gemini CLI) deep systems capabilities; the demo loop is fail → load skill → agent produces a kernel beating PyTorch's native implementation.
- **Where applicable**: ML platform and GPU/kernel work. Benchmarks are concrete (H100, six models) but vendor-run, promoting HF's skills ecosystem — treat numbers as directional.

### Lessons from Scaling GitHub's Remote MCP Server

Sam Morrow — GitHub

- **Why**: One of the most heavily used MCP servers in the ecosystem (4M+ downloads of the stdio server alone) — real production experience scaling AI-serving infrastructure, with classic cloud-ops problems: stateless horizontal scaling, distributed session storage, and observability under privacy constraints.
- **What**: The architectural decisions and lessons from initial implementation to horizontal scaling of a remote MCP server: managing tool overload, optimizing context usage, distributed session storage, observability without compromising user privacy, and concrete patterns and anti-patterns.
- **How**: Stateless, horizontally scalable server design; condensing an expansive platform (GitHub) into a coherent MCP interface; auth, security, and privacy treated as first-order concerns.
- **Where applicable**: Anyone building or operating remote MCP servers on production infrastructure — broadly applicable patterns, GitHub-specific in scale details.

## Adjacent

### What if the network was the sandbox?

Speaker not listed in the program (expo session)

- **Why**: The talk's thesis is a networking one: sandboxing conflates execution isolation with access control, and the network layer — identity-based access — can be the enforcement point for what autonomous agents can reach. That is zero-trust/segmentation thinking applied to agent fleets.
- **What**: A framing that agent blast radius is a network and identity problem: identity-based access at the network layer to define precise boundaries for agent behavior, remove the need to distribute API keys and credentials, and give complete visibility into what agents are actually doing.
- **How**: Network-layer identity enforcement in place of (or alongside) runtime sandboxing, so an isolated runtime that still reaches a sensitive system is caught at the network.
- **Where applicable**: Any org letting agents touch internal systems. No speaker or affiliation is given and it reads as a sponsor expo pitch — take the pattern (network as the policy plane for agent access), not the product.

### The Missing Primitive for Agent Swarms

Lou Bichard — Ona

- **Why**: Multi-agent coordination is currently reinvented per framework with brittle scaffolding (threads, worktrees, container pools); the argument that swarms need a platform primitive — identity, isolation, lifecycle, resource limits — is a cloud-native systems question, not an application one.
- **What**: A case for treating swarms as an infrastructure category: why current approaches break at scale, what a proper swarm primitive looks like (spawnable isolated agent execution contexts with identity, resource limits, and coordination semantics), lessons from shipping this to enterprises at Ona, and the UX of interacting with fleets of agents.
- **How**: Platform-level spawn semantics for isolated execution contexts, rather than application-level thread and state management.
- **Where applicable**: Teams building multi-agent systems in production. Conceptual plus one company's enterprise experience; no published validation stated in the abstract.

### Playground in Prod - Optimising Agents in Production Environments

Samuel Colvin — Pydantic AI / Logfire (per abstract)

- **Why**: Agents in production need iteration cadences far faster than CI/CD allows — changing a prompt or model setting should not require a redeploy. This applies the feature-flag/progressive-delivery pattern to agent parameters, then automates the loop.
- **What**: Managed Variables — a Pydantic AI feature built on the OpenFeature standard that externalizes system prompts, model configuration, tool descriptions, and thresholds for instant update from the Logfire UI with no redeploy — plus GEPA (Genetic-Pareto reflective text evolution) wired into Logfire traces to form a closed loop: observe performance, reflect on failures, evolve prompts, push live without human intervention.
- **How**: Agent parameters behind an OpenFeature-style flag interface; production traces and evals serve as the fitness signal for reflective prompt evolution, with guardrails, rollback, and A/B between prompt variants.
- **Where applicable**: The tooling is Pydantic AI/Logfire-specific, but the pattern — flags for prompts plus automated prompt optimization driven by production telemetry — transfers to any agent platform. Workshop format with live demos.

### Why Your AI UX Is Broken (and It's Not the Model's Fault)

Mike Christensen

- **Why**: The transport layer (HTTP/SSE, a one-way pipe tied to a single connection) is the hidden constraint on next-generation AI UX — interruption, resume-after-disconnect, and multi-device sync are infrastructure problems, and the emerging answer borrows from durable execution.
- **What**: The pattern of the session as a durable, shared resource independent of any single connection, device, or agent instance, enabling resumable streaming, live steering and interruption, multi-device continuity, concurrent interactions, and human-in-the-loop handoff — capabilities already shipping in leading AI products.
- **How**: Decouple session state from the streaming transport, so connections can break and devices come and go while anyone who joins catches up automatically; demos on real code, independent of model or framework.
- **Where applicable**: Teams building AI product frontends; a general architectural pattern, not org-specific.

### One Login to Rule Them All: Cross-App Access for MCP

Garrett Galow

- **Why**: Agent-to-service authentication is heading for a credential-management mess — a dozen OAuth consent screens and token lifecycles per agent. Cross-App Access is the standards-level fix, and agent identity beyond MCP is an emerging infrastructure topic.
- **What**: Cross-App Access leveraging three-way trust between MCP client, MCP server, and the organization's IdP: the IdP brokers a token exchange from the user's initial SSO login, so one sign-in yields access tokens across every MCP server. Includes an end-to-end demo of the Identity Assertion Authorization Grant flow.
- **How**: OAuth token exchange brokered by the IdP (the Identity Assertion Authorization Grant), extending SSO across the MCP tool ecosystem.
- **Where applicable**: A standards-level (OAuth/OIDC ecosystem) pattern, broadly applicable wherever agents consume APIs; no affiliation given in the program.

### Scaling the Next Paradigm of Heterogeneous Intelligence

Adrian Bertagnoli

- **Why**: The homogeneous-scaling era — monolithic models on identical GPU clusters — is showing its limits; purpose-matched models and silicon per sub-task is a plausible next scaling axis, relevant to accelerator-infrastructure planning.
- **What**: The "Heterogeneous Intelligence" thesis with early findings: exploiting heterogeneity across workflows, model architectures, and hardware for simultaneous cost, speed, and task-performance gains — e.g., automated payment workflows executing reliably at reduced compute cost, and higher accuracy on long-document reasoning by specializing sub-tasks across purpose-matched chips and models — plus a frontier view of hardware-algorithm co-evolution.
- **How**: Heterogeneous optimization — decompose workflows and route sub-tasks to purpose-matched models and silicon.
- **Where applicable**: Strategy-level. "Early findings" with no stated methodology or evaluation — treat as a directional thesis to pressure-test, not validated results. No affiliation given; likely vendor-adjacent.

### Lobster Trap: OpenClaw in Containers from Local to K8s and Back

Sally Ann O'Malley

- **Why**: Once one engineer's agent setup works, teams want to replicate it — the packaging and distribution problem for agent environments, including the local↔cluster secrets parity question.
- **What**: A demo taking OpenClaw from a stock local Podman setup to a curated agent bundle, then lifting that same baseline into Kubernetes, with a pragmatic secrets story: Podman secrets for local development, Vault for cluster deployments, and the same agent baseline moving between both. Everything runs on a laptop with local containers and a Kind cluster, with a reproducible tutorial repo.
- **How**: Containers make the setup reproducible (your best engineer's setup becomes the team standard), Kubernetes makes it distributable, and "back to local" keeps the baseline a starting point rather than a cage.
- **Where applicable**: Teams standardizing shared agent setups. Hands-on and 101-leaning (laptop + Kind scale), but the "agent baseline as a distributable artifact with portable secrets" pattern transfers.

### One Developer, Two Dozen Agents, Zero Alignment: Why we Need Collaborative AI Engineering

Maggie Appleton — GitHub Next

- **Why**: Solo agent use at team scale produces duplicate work, conflicting changes, and surprise features — the coordination gap is real, and multiplayer agent environments point at a solution, including infra-adjacent micro VM sandboxing.
- **What**: A critique of solo agentic engineering and a demo of Ace, GitHub Next's multiplayer agent environment: real-time collaboration, proactive agents, and sandboxed micro VMs for rapid prototyping and exploration, built so teams can plan and think critically together with shared context.
- **How**: A multiplayer environment where humans and agents share context and plan together, with micro VM sandboxing per exploration.
- **Where applicable**: Team-scale agentic development. Ace is a GitHub Next prototype — expect research-grade exploration rather than a finished product.

### How to Build Agents That Run for Hours (Without Losing the Plot)

Ash Prabaker, Andrew Wilson

- **Why**: Long-running agents fail differently — coherence drift, self-evaluation traps — and the harness techniques here are the reliability engineering of agentic systems.
- **What**: A workshop covering: why adversarial evaluator agents beat self-evaluation; why structured handoffs beat context compaction for coherence; decomposing work into testable sprint contracts; grading subjective output with LLM-applicable rubrics; traces as the primary debugging loop; and which harness parts to delete when the next model drops.
- **How**: Adversarial evaluation, contract-based decomposition, rubric grading, and trace-first debugging, as listed in the abstract.
- **Where applicable**: General agent-harness engineering; no affiliations given and abstract-level detail only — the workshop itself is where the substance will be.

### How Building with AI Can Double the Throughput of Your Engineering Team

Brian Scanlan — Intercom

- **Why**: The org-level question underneath all the infra talks: does agent-assisted development actually double engineering throughput on a large existing SaaS codebase? Intercom's in-progress attempt is a data point worth calibrating against.
- **What**: Lessons from Intercom's 2025 effort to double engineering-team throughput using AI tooling to get real features (not demos) into a large existing SaaS codebase and out to paying customers — what has and hasn't worked on the road toward 2x productivity.
- **How**: Organizational adoption story; the abstract does not give method detail beyond AI-tooling-assisted development.
- **Where applicable**: One company's experience — an org-specific case study rather than a validated technique; useful as calibration for what "2x" actually takes.

## Wildcard

### Two Roads to Durable Agents: Replay vs. Snapshot

Eric Allam — Trigger.dev

- **Why**: Durable execution for agents today means application-level replay with determinism constraints; OS-level process snapshot/restore is an alternative almost nobody in AI engineering is using — a genuinely different systems approach from the virtualization/checkpointing world.
- **What**: An honest comparison of the two durability models: replay (record every step, replay on recovery, code must be deterministic, can't capture everything a running process holds in memory) versus OS-level snapshot (freeze the entire process, free resources, restore exactly where it left off — no replay log, no determinism requirement, no step boundaries). Live demo on Trigger.dev: checkpoint mid-execution, suspend at zero cost while waiting on a human, resume from snapshot.
- **How**: OS-level process checkpoint/snapshot mechanics applied to agent processes, versus event-sourced replay.
- **Where applicable**: Long-running agent platforms; the snapshot approach depends on runtime checkpoint support (demoed on Trigger.dev, so vendor origin), and the honest where-each-breaks comparison is the real content.

### I Gave an AI Agent the Keys to My Life (Here's What Happened)

Radek Sienkiewicz

- **Why**: One of the few genuine "ran it in production against my actual life" accounts: a months-long, 24/7 personal-agent deployment with self-monitoring, scheduled jobs, and graded trust — field-report operational lessons rather than a demo of what's possible.
- **What**: What living with an always-on personal agent looks like: the permission-creep timeline from "read my files" to "handle my communications" over months; the 2am cron ecosystem (backing up its own memory and configuration, health monitoring, overnight output); self-recovery and self-update; how the trust boundary is defined and enforced; and why the agent has a personality file instructing it to disagree with its owner.
- **How**: Incremental permission grants over months, cron-driven autonomous routines, self-monitoring and self-recovery, and explicit trust tiers for what requires asking.
- **Where applicable**: Personal-agent deployment at single-user scale; no frameworks or generality claims — an honest field report.

### Reverse engineering a Viking VOIP phone protocol with Claude Code

Speaker not listed in the program (expo session)

- **Why**: For anyone from the networking world, LLM-assisted protocol reverse engineering is the crossover: black-box traffic analysis is a classic network-engineering skill, and here an AI agent does it against undocumented hardware — a signal of where agent capabilities are heading.
- **What**: A walkthrough of dissecting and reconstructing the protocol behind a Viking VoIP phone: capturing traffic, identifying patterns, using Claude Code to accelerate understanding and implementation, and turning the black-box device into a programmable interface.
- **How**: Traffic capture plus pattern identification, with an LLM coding agent accelerating the low-level protocol analysis and the implementation of the reconstructed protocol.
- **Where applicable**: Legacy and embedded device integration anywhere; the technique is general even though the case study is a single device. Short expo format and no named speaker — expect a compact story.

## Themes

- **Agents as a new infrastructure workload class**: disposable agent pods on Kubernetes, ephemeral CI runners, swarm execution primitives, horizontally scaled MCP servers — the field is starting to treat agents like multi-tenant cloud workloads with identity, isolation, and lifecycle needs.
- **The delivery pipeline is the new bottleneck**: multiple talks argue CI/CD, eval harnesses, and debug loops must become high-throughput systems as machine-authored change volume grows 5–10x.
- **The agent protocol and identity stack is forming this cycle**: ACP for agent↔harness, MCP for agent↔tools, Cross-App Access OAuth grants for agent↔identity — the interop layer is being standardized in real time.
- **Production iteration without redeploy**: managed variables / feature flags for prompts, automated prompt evolution from production traces, durable sessions — progressive-delivery patterns arriving in AI engineering.
- **Agents taking over deep-specialist systems work**: CUDA kernels, ML experiments, and protocol reverse engineering — the frontier moved from "writes my app code" to "does my systems engineering," with measurable (if vendor-reported) results.
- **Durability and long-running execution are a live architectural debate**: replay versus OS-level snapshots, hours-long coherence, durable sessions — state management for agents is unsettled and worth watching.
