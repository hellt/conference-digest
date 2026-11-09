<!--
conference: @Scale: Systems & Reliability 2026
source_url: https://atscaleconference.com/events/systems-reliability-2026/
generated: 2026-11-09
registry_key: atscale-systems-reliability-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# @Scale: Systems & Reliability 2026

A one-day, Meta-anchored systems event (Bellevue, June 25, 2026) with NVIDIA, Microsoft, and Pulumi guests. The 2026 program has a clear center of gravity: AI infrastructure (GPU capacity, storage, cluster operations) and AI *operating* infrastructure (agents debugging GPUs, investigating incidents, managing config). Note on sourcing: no papers or slides are published for this event; the conference page contains only the abstracts reproduced in the program, so every write-up below is **(from abstract only)**. A few sessions (the two keynotes, the Live Q&A, and the four-company panel) publish no substantive abstract and are not selected.

## Core

### Our Journey to Safely Unleash Agents at Meta Scale

**Links:** [Abstract](https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-6) · [Session recording](https://www.youtube.com/watch?v=QHg0HeqIcqY) · [Materials](https://atscaleconference.com/metas-journey-to-safely-unleash-agents-at-scale/)

David Pariag (Meta)

- **Why**: The first real deployments of AI agents that touch production infrastructure — not write code, but *operate* systems (debug GPU failures, remediate outages). The access-control and guardrail problem this creates is one any operator of a large fleet will face within a couple of years; Meta is furthest along publicly.
- **What**: Meta's program-level learnings from enabling agentic access to its systems: building internal agents, deploying third-party agents, observing how agents interact with their infrastructure, and deploying guardrails to prevent destructive actions. A journey/lessons talk rather than a single system. (from abstract only)
- **How**: Not detailed in the abstract; expect case studies of what agents did to infra when let loose, and the containment mechanisms built in response.
- **Where applicable**: Meta-specific scale and internal tooling, but the problem space — authenticated agent identity, action scoping, blast-radius limits, observability of agent behavior — is universal for anyone running cloud or Kubernetes estates.

### The Agentic Infrastructure Gap: In-Distribution Languages Make It a Coding Problem

**Links:** [Abstract](https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-7) · [Recording](https://www.youtube.com/watch?v=P4PpoTH9ADc)

Joe Duffy (Pulumi)

- **Why**: A sharp thesis on *how* agents should manage infrastructure: LLMs are trained on billions of lines of Python/TypeScript/Go and almost nothing on your bespoke DSLs, consoles, and runbooks. If agents are going to run infra, the infra's interface needs to live in the distribution the model was trained on. Directly relevant to how network automation and IaC platforms should be shaped for agent consumption.
- **What**: The argument that "assembling IKEA furniture" — consoles, API keys, copy-pasted config — is the agent blocker, and that modeling infrastructure in real programming languages reduces agent management to a coding problem, given an oracle that maps code changes back to infrastructure outcomes. Includes learnings from Pulumi's work with frontier AI companies. (from abstract only)
- **How**: Infrastructure expressed as code in mainstream languages (Pulumi's model), plus a preview/plan-style oracle that predicts infrastructure outcomes from code diffs, closing the agent's feedback loop.
- **Where applicable**: General-purpose for IaC and cloud provisioning; expect vendor framing (Pulumi CEO) but the in-distribution-language argument applies to any automation surface, including network config generation.

### Extending Meta to the Public Cloud

**Links:** [Abstract](https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-8) · [Recording](https://www.youtube.com/watch?v=p08-ef0QKYQ)

Dinesh Govindasamy (Meta), Sargun Dhillon (Meta)

- **Why**: A hyperscaler with one of the world's largest private DC footprints deliberately adopting public cloud — for GPU capacity — is a rare, high-signal data point on hybrid strategy and capacity optionality. Sargun Dhillon (long-time Meta infra) presenting adds credibility that this is engineering substance, not a partnership announcement.
- **What**: How Meta integrated public cloud into its overall infrastructure footprint: initial forays driven by GPU compute demand, multi-cloud used explicitly as optionality ("capacity hyperliquidity"), and full integration into Meta's platform, OS, and fleet management stack so internal customers see cloud capacity as ubiquitous rather than a separate silo. (from abstract only)
- **How**: Not detailed in the abstract; the interesting engineering is presumably in extending Meta's host OS, provisioning, and fleet management to cloud instances so tooling parity holds across estates.
- **Where applicable**: Meta-specific (their internal stack is not reproducible), but the strategic and integration lessons — treating cloud as a fungible capacity pool behind a uniform fleet-management abstraction — transfer to any large hybrid operator.

### Teaching AI to Fight Fires: Autonomous Reliability Agents at Meta Scale

**Links:** [Session recording](https://www.youtube.com/watch?v=irtqkj3fHxM) · [Materials](https://atscaleconference.com/teaching-ai-to-fight-fires-building-the-reliability-flywheel-at-meta/)

Gaurav Mitra (Meta)

- **Why**: The most quantitatively substantiated AIOps deployment in the program: an investigation agent that has handled 1,000+ real incidents, cut detection-to-mitigation time by 60%, and matches senior on-call engineers ~80% of the time. That is deployment evidence, not a demo — and it is squarely in the "ML for infrastructure operations" interest area.
- **What**: The "reliability flywheel": an always-on investigation copilot that encodes senior on-call engineers' investigation methods and improves with every incident, deployed across Meta's recommendation systems. The talk also lays out a staged autonomy progression: pattern identification, autonomous investigation, supervised mitigation of low-risk reversible actions, and self-healing as the end state — plus an explicit treatment of the trust boundary between agents and humans. (from abstract only; the event page's article teaser adds that the originating December 2024 config change caused a widespread routing error across every region, taking 50+ engineers and 28 hours to recover)
- **How**: Context-engineered architecture correlating time-series metrics, deployment logs, configuration changes, and infrastructure health, built on structured tool servers and reusable workflows rather than free-form prompting.
- **Where applicable**: Validated on Meta's recommendation infra (org-specific numbers), but the architecture — tool servers + reusable investigation workflows + human-in-the-loop trust ladder — is a transferable pattern for incident automation in any environment.

### Experience Productionizing and Operating GB200 clusters

**Links:** [Recording](https://www.youtube.com/watch?v=1o4emwSid78)

Ankur Srivastava (NVIDIA), Sachin Kumar Lakharia (NVIDIA), Douglas Wightman (NVIDIA)

- **Why**: Rack-scale NVLink systems (GB200 NVL72: 72 GPUs with an exascale-scale NVLink fabric in one rack) change how clusters must be scheduled and operated — fabric locality becomes the dominant scheduling constraint. First-party operational experience from NVIDIA on bringing up and running a large cluster is hard to get elsewhere.
- **What**: Production experience operating large GB200 clusters: topology-aware scheduling in Slurm to maximize NVLink fabric utilization, GPU-occupancy and scheduling recommendations validated with a Slurm simulator, and the unglamorous bring-up work — health checks, rack testing, slow-node identification, supporting large-scale training runs. Cites >2.6x MLPerf training improvement attributable to the NVL72 system. (from abstract only)
- **How**: Topology-aware Slurm scheduling (placing jobs to exploit intra-rack NVLink bandwidth) plus simulation-driven occupancy policy; operational practices for node/rack validation before admitting capacity to the pool.
- **Where applicable**: Tied to NVIDIA GB200 NVL72 silicon and Slurm specifically — the concrete recommendations don't port directly to non-NVL systems or Kubernetes schedulers. The *method* (topology as a first-class scheduling input, simulator-tuned occupancy, systematic slow-node quarantine) generalizes to any tightly-coupled accelerator fabric.

### Taming AI Infrastructure Failures with Agentic Debugging

**Links:** [Session recording](https://www.youtube.com/watch?v=9wc0556pIwg) · [Materials](https://atscaleconference.com/leveraging-agents-to-debug-nccl-watchdog-timeouts/)

Phillip Liu (Meta)

- **Why**: NCCL watchdog timeouts are the canonical "everything looks fine until a collective hangs" failure of distributed PyTorch training — anyone running GPU clusters has paid this tax. A root-cause taxonomy built from a year of internal incidents and shared with the PyTorch community is immediately actionable.
- **What**: A categorization of the major root-cause buckets behind NCCL watchdog timeouts (investigated at Meta, in partnership with the PyTorch community), distilled into a practical decision tree and runbook to compress triage time — plus early results using agents to assist root-cause analysis. The abstract openly flags that details are still TBD. (from abstract only)
- **How**: Systematic bucketing of observed failure modes into a decision tree; agent-assisted RCA layered on top of the structured workflow (a companion article describes it as "a technical, repeatable workflow").
- **Where applicable**: Broadly applicable — this failure mode affects anyone running PyTorch distributed training, not just Meta. Since NCCL timeouts are usually a *symptom* (slow node, fabric congestion, misconfigured transport, process hang), expect the taxonomy to span host, NIC/transport, and network layers.

### AI Storage Blueprint

**Links:** [Abstract](https://atscaleconference.com/events/systems-reliability-2026/#agenda-item-19) · [Recording](https://www.youtube.com/watch?v=xc_BxLsijWA)

Sidharth Bajaj (Meta), Venkatraghavan Srinivasan (Meta)

- **Why**: In training clusters, storage is frequently what gates GPU utilization (checkpoint I/O, dataset streaming, data-loading jitter). Meta re-architecting its storage stack around AI workloads is the storage-side counterpart of the GB200 scheduling talk.
- **What**: How Meta evolved its storage architecture to serve an environment where frontier models ship in weeks, framed around two explicit optimization targets: GPU utilization and research velocity. (from abstract only)
- **How**: Not detailed in the abstract; the two stated hurdles imply work on throughput/latency consistency for training data paths and on flexibility/speed of the research workflow.
- **Where applicable**: Meta-specific production setup; the framing (storage judged by GPU-hours protected and researcher iteration speed) is a useful lens for any AI-cluster storage design even before the details land.

## Adjacent

### [Almost] Fail & Tell: Stop The World

**Links:** [Session recording](https://www.youtube.com/watch?v=-0v6UUPLvF8) · [Materials](https://atscaleconference.com/almost-fail-tell-stop-the-world/)

Phil Lopreiato (Meta), Rahul Iyengar (Meta)

- **Why**: A near-miss postmortem with a genuinely unusual mechanism: re-bootstrapping the infrastructure control plane of an entire region on the fly. Control-plane recovery and DR-preparedness are underrepresented topics, and this is a real production story, told by Meta's sitewide reliability people.
- **What**: The March 2025 incident in which Meta avoided a prolonged sitewide outage, containing the issue in minutes by rebuilding the control plane for a whole region live using emergency tooling — presented as a case study in DR preparedness and calm incident command. (from abstract only)
- **How**: Not detailed in the abstract; the substance will be in what the emergency tooling does, how regional control-plane state is reconstructed, and how the response was organized.
- **Where applicable**: Meta-specific event, but the lessons — rehearsed emergency tooling, control-plane as a recoverable artifact, decisive regional action over slow diagnosis — transfer to any operator with regionalized infrastructure.

### Securing Production Debugging at Hyperscale

**Links:** [Recording](https://www.youtube.com/watch?v=UAs6-gNzFks)

Shridivya Sharma (Microsoft), Luke Kelly (Microsoft)

- **Why**: The "how do humans (and now agents) safely touch production boxes" problem, worked at Microsoft's K8s fleet scale. Relevant to anyone operating Kubernetes estates where break-glass access is the default risk story.
- **What**: Microsoft's approach to production debugging across a global fleet of Kubernetes clusters: SSH-based access integrated with just-in-time privilege elevation and task-based (rather than open-shell) execution, kept secure and auditable — then those same building blocks exposed to AI (Semantic Kernel) so on-call engineers get assisted resolution rather than raw shell. (from abstract only)
- **How**: Structured, auditable debugging primitives (JIT elevation + task-scoped SSH commands) that double as a safe action surface for AI assistance — the same "give agents constrained, task-shaped interfaces" theme running through the Meta talks.
- **Where applicable**: Microsoft's fleet, but the pattern is general for large K8s estates; the AI-assist portion is early-stage and Microsoft-stack-specific (Semantic Kernel).

## Wildcard

### Building Privacy Aware Infrastructure in the AI-Native Era

**Links:** [Recording](https://www.youtube.com/watch?v=q9RSv2ltZtU)

Rituraj Kirti (Meta)

- **Why**: Not about networking or AI infra per se — but it presents the most transferable *AI systems* architecture in the program: how to run an LLM-driven control loop in production while converging it to deterministic, auditable, near-zero-LLM operation. That pattern applies far beyond privacy, e.g., to policy enforcement and classification over network/infra assets.
- **What**: A case study in AI-native asset classification at the scale of millions of data assets: a hybrid deterministic-rules engine with LLM fallback that converts messy context (metadata, lineage, code references, scan signals) into enforceable privacy controls — with ground-truth + eval self-improvement loops and a distillation step that exports high-performing LLM behavior into an auditable `rules.yaml`, driving LLM usage toward near-zero while improving determinism, latency, and cost. (from abstract only)
- **How**: Active learning focuses human review on high-value examples; LLM-as-Judge provides scalable review signal (with kappa reliability reported); evaluation gates prevent regressions and circular reinforcement; the converged behavior is distilled into declarative rules with drift monitoring in production.
- **Where applicable**: The privacy use case is Meta-specific, but the loop design — LLM with fallback, eval gates, distillation to declarative rules, drift monitoring — is a general recipe for any "LLM in the infra control path" system where you eventually need auditability and predictable latency/cost.

## Themes

- **Agents move from writing code to operating systems.** Nearly every talk puts an agent on the production side — debugging GPU failures (Pariag), investigating incidents (Mitra), root-causing NCCL hangs (Liu), assisting on-call (Microsoft). The field's center of attention is no longer code generation; it is safe agentic *action* on live infrastructure.
- **The trust boundary is the hard problem.** Across Meta and Microsoft, the shared answer is the same shape: constrained, task-scoped, auditable action surfaces (guardrails, JIT elevation, task-based execution, supervised mitigation of low-risk reversible actions) rather than autonomous shells.
- **GPU capacity is the forcing function.** Meta going to public cloud for GPU compute, storage re-architected around GPU utilization, and GB200 operationalization all trace to the same pressure — and multi-cloud shows up explicitly as capacity optionality rather than ideology.
- **Distilling AI behavior into deterministic artifacts.** Two talks independently converge on exporting what the model learned into auditable, non-AI form: `rules.yaml` in the privacy talk, decision trees/runbooks in the NCCL talk. LLMs as a *generation* mechanism for deterministic policy, not a runtime dependency.
- **Topology-aware scheduling is now an operational discipline.** The GB200 talk treats fabric topology as the primary scheduling input, validated via simulation — a preview of how scale-up/scale-out asymmetry will dominate cluster orchestration generally.
- **Scarcity caveat**: this program publishes abstracts only, no papers or slides, and several sessions (keynotes, Q&A, panel) have no technical abstract at all. Depth here must come from the recordings and the companion articles on the @Scale site.
