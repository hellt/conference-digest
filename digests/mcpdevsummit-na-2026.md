<!--
conference: MCP Dev Summit North America 2026
source_url: https://mcpdevsummitna26.sched.com/list/descriptions/
generated: 2026-11-10
registry_key: mcpdevsummit-na-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# MCP Dev Summit North America 2026

*Note on sourcing: sched.com pages returned 403 to automated fetches and no paper/slide text was available, so every write-up below is grounded in the program abstract only; each item's What line says so explicitly. This program is an agent/MCP-infrastructure conference — nothing here touches physical DC or WAN design directly, but it is a dense look at the systems side of the agentic AI stack the PM operates in.*

## Core

### Keynote: MCP @ Amazon Scale - James Hood, Principal Software Engineer, Amazon Web Services

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2ILxf/keynote-mcp-amazon-scale-james-hood-principal-software-engineer-amazon-web-services)

James Hood, Principal Software Engineer, Amazon Web Services

- **Why**: The largest described internal MCP deployment — tens of thousands of engineers, hundreds of MCP servers — with security as a first-class constraint. If you are planning an enterprise rollout of agent tooling, this is the reference experience report.
- **What**: Amazon's account of enabling engineers to use hundreds of MCP servers (ticket/issue systems, design and architecture guidance docs, internal tools) while keeping security essential, plus the rollout lessons learned getting there (from abstract only).
- **How**: Not detailed in the abstract — this is an experience/lessons talk covering org-scale enablement, security guardrails, and rollout sequencing rather than a single mechanism.
- **Where applicable**: Very large single-organization environment; the tooling is Amazon-internal, but the rollout and security-governance lessons transfer to any enterprise running internal MCP platforms.

### Keynote: Operating MCPs at Enterprise Scale: Uber's Journey - Meghana Somasundara, Agentic AI Lead & Rush Tehrani, Head of Engineering, Agentic AI Platform, Uber Technologies, Inc.

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbf2/keynote-operating-mcps-at-enterprise-scale-ubers-journey-meghana-somasundara-agentic-ai-lead-rush-tehrani-head-of-engineering-agentic-ai-platform-uber-technologies-inc) · [Recording](https://www.youtube.com/watch?v=yVqMxBahjfA)

Meghana Somasundara, Agentic AI Lead, Uber Technologies, Inc.; Rush Tehrani, Head of Engineering, Agentic AI Platform, Uber Technologies, Inc.

- **Why**: The core problem of agent-to-microservice access at scale — how do you expose thousands of internal services to agents without hand-writing thousands of MCP servers or losing safety.
- **What**: Uber's unified MCP infrastructure with three pillars: Protobuf-driven generation of MCP servers from existing microservice definitions; "derived tools" that let developers override and refine tool descriptions per workflow because static definitions aren't enough; and a quality-evaluation loop feeding their no-code Agent Builder (from abstract only).
- **How**: Auto-generate MCP servers from existing service Protobufs so agents get safe, instant access to the microservice estate; layer developer-controlled tool-description overrides; evaluate tool quality systematically.
- **Where applicable**: The generate-don't-hand-write pattern and the eval methodology transfer to any large microservice organization with interface definitions; the specific Protobuf/Agent Builder stack is Uber's.

### Keynote: Duolingo's AI Slackbot: An Enterprise Assistant With 180+ MCP Tools - Aaron Wang, Software Engineer, Duolingo Inc

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbf5/keynote-duolingos-ai-slackbot-an-enterprise-assistant-with-180+-mcp-tools-aaron-wang-software-engineer-duolingo-inc)

Aaron Wang, Software Engineer, Duolingo Inc

- **Why**: A rare production agentic-ops assistant with an honest failure-mode list — exactly the "agents for infrastructure operations" use case, including incident triage and debugging from Slack.
- **What**: A Slackbot built on Claude's Agent SDK and MCP connecting 180+ tools across 15+ MCP servers (GitHub, Jenkins, Sentry, Grafana, PagerDuty, Honeycomb), with standardized server patterns (stdio/HTTP, consistent config schemas), YAML-based role-gated tool allowlists, and a parallel evaluation harness validating tool usage, anti-hallucination, and response quality. The real-world challenges section is the payload: testing in production without synthetic environments, keeping customer PII out of models, fast-answer vs good-answer tradeoffs, agents hallucinating instead of calling tools, and wrong parameters causing slow queries (from abstract only).
- **How**: Standardized MCP server transports and config; RBAC via YAML tool allowlists by user role; scripted parallel evaluation of MCP tool behavior.
- **Where applicable**: Broadly transferable to mid-size orgs with a SaaS observability/CI stack; the eval framework and failure taxonomy are general, the specific server set is Duolingo's.

### Stateless: The Future of MCP Transports - Shaun Smith, Hugging Face & Kurtis Van Gent, Google

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbff/stateless-the-future-of-mcp-transports-shaun-smith-hugging-face-kurtis-van-gent-google)

Shaun Smith, Open Source Agents / MCP, Hugging Face; Kurtis Van Gent, MCP Core Maintainer (Transports Working Group lead), Google

- **Why**: Described as one of the largest protocol changes since MCP's launch — it directly determines how you deploy, scale, and operate MCP servers. The roadmap/migration content makes this planning-relevant now.
- **What**: The move to stateless MCP transports, motivated with real adoption data from Google and Hugging Face; the latest approaches for serverless Elicitation, Sampling, and Sessions; the application and infrastructure patterns that statelessness unlocks (e.g., MCP Apps); and migration timeline and approach (from abstract only).
- **How**: Removing per-connection session state from the protocol so servers become horizontally scalable and serverless-friendly; the Working Group session details what replaces session-bound semantics.
- **Where applicable**: Protocol-level and therefore broadly applicable; anyone operating remote MCP servers today needs to track the migration. Pairs directly with the Envoy/proxy talk below.

### Bridging Kernel Space and AI: Building an MCP Server for Linux Scheduler Observability - Daniel Hodges, Meta

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbgm/bridging-kernel-space-and-ai-building-an-mcp-server-for-linux-scheduler-observability-daniel-hodges-meta)

Daniel Hodges, Software Engineer (Linux team), Meta

- **Why**: The clearest example at this conference of AI applied to deep systems debugging — an MCP server that exposes kernel-level observability to agents rather than yet another wrapper over high-level APIs.
- **What**: A production MCP server implemented in `scxtop`, the observability tool for Linux's sched_ext extensible scheduler framework, letting developers ask natural-language questions like "why is my application experiencing high scheduling latency?" and get AI-driven analysis correlating kernel tracing data, hardware topology, performance counters, and scheduler internals (from abstract only).
- **How**: MCP layer over scxtop's tracing and counter data, so the agent can reason across kernel traces, CPU topology, and scheduler state jointly.
- **Where applicable**: Linux environments using sched_ext (the eBPF-based extensible scheduler framework); the tool is open source in the sched-ext/scx repo, so this is usable outside Meta, but it presumes sched_ext adoption.

### From One MCP Server To an Ecosystem: When MCP Stops Being a Server and Becomes a Platform - Vaibhav Tupe, Equinix

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbjp/from-one-mcp-server-to-an-ecosystem-when-mcp-stops-being-a-server-and-becomes-a-platform-vaibhav-tupe-equinix) · [Slides](https://hosted-files.sched.co/mcpdevsummitna26/dc/MCP-DevSummit-Final.pptx)

Vaibhav Tupe, Tech Lead - Principal Engineer, Equinix

- **Why**: Equinix's product is physical datacenter and interconnect infrastructure — this is what agent-mediated infrastructure operations looks like at a company whose domains are networking and the DC plant, which is the closest this program comes to the PM's physical-infrastructure world.
- **What**: Practical lessons from evolving a single MCP server into multiple coordinated MCP servers spanning networking and infrastructure domains: how architecture changes at ecosystem scale, design patterns to avoid tight coupling and fragmentation, approaches to tool discovery, versioning, and backward compatibility, operational lessons on reliability, rate limiting, and failure isolation, and governance practices for ownership and change management (from abstract only).
- **How**: Platform-engineering patterns for multi-server coordination, discovery, and lifecycle management rather than a single mechanism.
- **Where applicable**: Equinix-specific production experience, but explicitly framed as transferable lessons for any team turning MCP into a shared platform capability across teams and domains.

### MCP Traffic Handling at Scale: Stateless Design, Proxies, and the Road Ahead - Erica Hughberg, Tetrate & Boteng Yao, Google

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2K6kw/mcp-traffic-handling-at-scale-stateless-design-proxies-and-the-road-ahead-erica-hughberg-tetrate-boteng-yao-google)

Erica Hughberg, Envoy AI Gateway Maintainer, Tetrate; Boteng Yao, Senior Envoy Maintainer, Google

- **Why**: The data-plane view of MCP — session management across fleets, policy enforcement for agents, proxy architecture. This is the talk that maps agent infrastructure onto classic proxy/load-balancer concerns.
- **What**: How proxies currently handle stateful MCP sessions, how stateless designs dramatically simplify scaling and operations, and how proxies like Envoy enforce authorization, tool safety, and policy without becoming bottlenecks; plus a forward look at emerging proposals (stateless transports, async tasks, server discovery) and why protocol/proxy alignment matters (from abstract only).
- **How**: Proxy-level session handling and policy enforcement via Envoy and Envoy AI Gateway, evolving in step with the protocol's stateless direction.
- **Where applicable**: Anyone fronting MCP servers with a gateway; Envoy-centric (speakers are Envoy maintainers) but the session-state and policy-enforcement mechanics generalize to any proxy stack.

### Durable, Asynchronous, and Tricky: Implementing MCP Tasks in Practice - Cornelia Davis, Temporal

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbg9/durable-asynchronous-and-tricky-implementing-mcp-tasks-in-practice-cornelia-davis-temporal)

Cornelia Davis, Developer Advocate, Temporal

- **Why**: MCP Tasks (introduced Nov 2025) add first-class async semantics to the protocol — the distributed-systems hard part of agent infrastructure, and the piece anyone running long-lived operations (deploys, batch jobs, remediation) will hit first.
- **What**: What the Tasks spec requires and deliberately leaves open (how durability is achieved), and the hard corners in practice: clients or servers restarting mid-task, stable task identity and rediscovery via tasks/list, mismatched sync/async expectations, idempotency, polling, backpressure, error handling across retries, and human-in-the-loop on input_required without tight client-server coupling (from abstract only).
- **How**: Durable state behind ephemeral connections plus idempotent task design — concrete implementation practices layered on the Task lifecycle, TTL, and state model the spec defines.
- **Where applicable**: Anyone building long-running MCP clients or servers; protocol-level practices, though note the speaker's employer (Temporal) sells durable execution, so expect that lens on the durability gap the spec leaves open.

### Kubernetes-Native Agent Discovery: A Unified Registry for MCP Servers and Skills - Carlos Santana, AWS

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2HbjX/kubernetes-native-agent-discovery-a-unified-registry-for-mcp-servers-and-skills-carlos-santana-aws)

Carlos Santana, Sr. Kubernetes Specialist SA, AWS

- **Why**: As agents enter Kubernetes clusters, hardcoded MCP endpoints and skill definitions become the new brittleness — this proposes the K8s-native answer using familiar primitives.
- **What**: A cluster-scoped registry that exposes both MCP servers and Skills through a unified API, built with CRDs and proven service-discovery patterns, so agents can query available capabilities by metadata, handle lifecycle changes gracefully, and dynamically assemble their toolset based on cluster state; includes a working implementation demo (from abstract only).
- **How**: CRDs representing MCP servers and Skills as first-class cluster objects, plus Kubernetes service-discovery patterns applied to agent capability discovery.
- **Where applicable**: Kubernetes environments where services scale and evolve continuously; AWS SA-led but blueprint-style and generalizable to any cluster; treats MCP servers and Skills as complementary discovery targets.

## Adjacent

### MCP at 18 Months: Protocols, Patterns, and What We Didn't See Coming - Shaun Smith, Hugging Face

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2HbfE/mcp-at-18-months-protocols-patterns-and-what-we-didnt-see-coming-shaun-smith-hugging-face)

Shaun Smith, Open Source Agents / MCP, Hugging Face

- **Why**: Hugging Face runs thousands of AI applications with MCP interconnectivity and supports Remote MCP via Inference Providers — a useful vantage point on where agentic inference, compute, and storage workloads are actually shifting.
- **What**: An experience-based session covering how ACP and Open Responses work within HF's MCP infrastructure, where Skills and code generation fit, multi-model environments and why subagent patterns matter for certain tasks, observed trends in agentic and inference workloads, and multimodal/mixed-content demands (from abstract only).
- **How**: Operating 1000s of MCP-connected applications and reporting on what the deployment experience shows about protocol coexistence and workload drift.
- **Where applicable**: HF-specific deployment scale, but the workload-trend observations are ecosystem-wide signal for anyone capacity-planning AI serving infrastructure.

### One Spec, Ten SDKs, Zero Excuses: Conformance Testing MCP - Paul Carleton, Anthropic

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbfu/one-spec-ten-sdks-zero-excuses-conformance-testing-mcp-paul-carleton-anthropic)

Paul Carleton, Member of Technical Staff, Anthropic

- **Why**: "Compatibility without coordination" is MCP's core promise; this is the testing infrastructure that keeps ten SDK implementations honest, and a good template for conformance testing any protocol.
- **What**: MCP's conformance testing infrastructure: real SDK implementations (Python, TypeScript, C#, Go) run against scenarios exercising specific protocol interactions — OAuth flows, Client ID Metadata Documents, resource metadata discovery — with analysis of behavior and conformance; including what running it across SDKs found, how it changed spec development, and how it enables attack simulation and evidence-based SDK tiering (from abstract only).
- **How**: Scenario-based behavioral conformance harness that runs actual SDKs, not paper checks against the spec.
- **Where applicable**: Directly relevant to MCP implementation maintainers; the conformance-harness pattern generalizes to any multi-implementation protocol effort.

### Evolution, Not Revolution: How MCP Is Reshaping OAuth - Aaron Parecki, Okta

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2HbfQ/evolution-not-revolution-how-mcp-is-reshaping-oauth-aaron-parecki-okta)

Aaron Parecki, Director of Identity Standards, Okta

- **Why**: Auth is the make-or-break layer for enterprise MCP adoption, and this maps the concrete OAuth extensions agents need — from someone editing the relevant OAuth specifications.
- **What**: How MCP adapts OAuth rather than replacing it: Client ID Metadata Documents (CIMD) letting agents bring their own identity to arbitrary servers as an improvement on Dynamic Client Registration, Protected Resource Metadata (RFC 9728) for dynamic auth-server discovery so MCP servers need not be authorization servers, and the Identity Assertion Authorization Grant moving consent to the enterprise policy layer to stop click-through fatigue (from abstract only).
- **How**: Incremental extensions to standard OAuth trust relationships rather than a rewritten auth stack for agents.
- **Where applicable**: Any enterprise MCP deployment with an existing IdP; standards-track and broadly applicable, not operator-specific.

### Interceptors for MCP: A Production-Tested Standard for Agentic Middleware - Kurt Degiorgio & Cannis Chan, Bloomberg

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbic/interceptors-for-mcp-a-production-tested-standard-for-agentic-middleware-kurt-degiorgio-cannis-chan-bloomberg)

Kurt Degiorgio, Senior Engineer, Bloomberg; Cannis Chan, Technical Product Manager, Bloomberg

- **Why**: Middleware is the next standardization battleground — without it, the M×N integration problem just moves from the data layer to a fragmented landscape of bespoke sidecars and proxies.
- **What**: A protocol-in-depth walkthrough of SEP-1763 (Interceptors), a proposal for protocol-native interception, validation, and transformation of messages across the MCP lifecycle: capability negotiation, hook points and invocation models, deterministic ordering/composition, enforcement semantics, error handling, and observability — motivated by Bloomberg's production use in a regulated financial environment and mapped against AWS Bedrock AgentCore Gateway Interceptors and OpenAI Guardrails (from abstract only).
- **How**: Elevates middleware to a first-class protocol capability with defined hook points and composition semantics, so controls between model and data are interoperable rather than bespoke.
- **Where applicable**: Enterprises needing policy control between model and data; the semantics are being standardized for interoperability but note it is a SEP proposal, not yet shipped spec, and the production grounding is Bloomberg's regulated environment.

### Every API Is a Tool for Agents - Matt Carey, Cloudflare

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2HbiN/every-api-is-a-tool-for-agents-matt-carey-cloudflare)

Matt Carey, Agents and MCP, Cloudflare; maintainer of the official MCP TypeScript SDK

- **Why**: Reframes the context-limit problem in a way that changes build-vs-expose decisions: the context limit is an agent problem, not an MCP problem — so you shouldn't hand-build cherry-picked MCP servers at all.
- **What**: Cloudflare's techniques (codemode, tool search) for making complete APIs accessible to agents through MCP without hand-writing tool definitions — motivated by their REST OpenAPI spec being over 2.3 million tokens — plus TypeScript SDK work making stateless servers the default (from abstract only).
- **How**: Server-side on-demand tool discovery, treating APIs like CLIs (self-discoverable and documented by design) so the full API surface becomes agent-accessible.
- **Where applicable**: Any organization with large REST APIs it wants agents to use; Cloudflare-scale motivation but the pattern is general. Complements the stateless-transports keynote.

### MCP Servers in the Wild: Managing Tool Complexity at Scale - Arnav Balyan, Concierge AI

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2HbjC/mcp-servers-in-the-wild-managing-tool-complexity-at-scale-arnav-balyan-concierge-ai)

Arnav Balyan, CEO, Concierge AI

- **Why**: At high tool counts, agents make wrong calls, burn tokens, and skip required call sequences — a reliability and compliance risk precisely in the high-stakes domains the PM cares about (infrastructure, finance).
- **What**: A server design pattern called "progressive tool exposure": the MCP server actively controls which tools are visible to the agent at each point in execution, refreshing and scoping tools as the agent progresses, directing the action space and enforcing runbooks; the server also tracks state so backtracking reverts server-side state, making agent behavior transactional. Claims: fewer invalid tool calls, lower inference cost, improved determinism (from abstract only).
- **How**: Server-driven tool visibility plus stateful workflow scoping — the server shapes what the agent can see and do at each step.
- **Where applicable**: Tool-heavy, high-stakes MCP systems; the vendor manages 400+ public MCP deployments (real data, but also product positioning — treat the claims as directionally interesting until details land). The pattern itself is implementation-agnostic.

### Towards Building Safe & Secure Agentic AI - Dawn Song, UC Berkeley; UC Berkeley Center for Responsible Decentralized Intelligence & Matt White, Linux Foundation/PyTorch Foundation

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbh1/towards-building-safe-secure-agentic-ai-dawn-song-uc-berkeley-uc-berkeley-center-for-responsible-decentralized-intelligence-matt-white-linux-foundationpytorch-foundation)

Dawn Song, Professor, UC Berkeley; Co-Director, Berkeley RDI; Matt White, Global CTO of AI, The Linux Foundation / Executive Director, PyTorch Foundation

- **Why**: Before wiring agents into production infrastructure, you need the systematized attack-surface map — this is the heavyweight academic overview of agent security, with real incidents behind it.
- **What**: A system-level security landscape for agentic AI: how increasing agent flexibility expands attack surfaces (prompt injection, memory poisoning, unsafe data flows, credential leakage, unauthorized execution), illustrated with real-world incidents and CVE analyses; plus a systematic overview of end-to-end automatic red teaming and a defense-in-depth framework spanning runtime guardrails, access control, information-flow tracking, privilege separation, and secure-by-design architecture (from abstract only).
- **How**: Comprehensive systematization of attacks and defenses across modern agent architectures rather than a single defense.
- **Where applicable**: Architecture-level and general; applies to any organization deploying agents against sensitive systems — a risk-assessment checklist more than an implementation guide.

## Wildcard

### MCPwned: Hacking MCP Servers With One Skeleton Key Vulnerability - Jonathan Leitschuh, Independent

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2Hbj3/mcpwned-hacking-mcp-servers-with-one-skeleton-key-vulnerability-jonathan-leitschuh-independent)

Jonathan Leitschuh, Open Source Security Researcher, Independent

- **Why**: A genuinely surprising cross-layer attack: the browser's same-origin model meets the new local agent-port surface. It's the one talk here where the exploitation primitive is classic network-level technique applied to AI infrastructure.
- **What**: Weaponizes a widely overlooked MCP-spec weakness — browser-based DNS rebinding — against SSE and streaming-HTTP MCP servers to exfiltrate data and escalate access; visiting a malicious website can compromise a locally running MCP server (from abstract only).
- **How**: DNS rebinding defeats same-origin protections to let attacker pages talk to localhost MCP servers over SSE/streaming HTTP, then abuse the server's access to data and credentials.
- **Where applicable**: Any locally running HTTP/SSE MCP server (the Cursor/Claude Desktop deployment pattern). Drives home why the proxy and transport-hardening patterns in the core talks are not optional.

### What if MCP was Symmetric? - Jerome Swannack, Anthropic

**Links:** [Abstract](https://mcpdevsummitna26.sched.com/event/2HbfB/what-if-mcp-was-symmetric-jerome-swannack-anthropic)

Jerome Swannack, Member of Technical Staff, Anthropic (helped build MCP at Anthropic)

- **Why**: A protocol-design thought experiment from one of MCP's builders — the kind of "what if" that occasionally becomes the next protocol revision, and useful for anyone who has to reason about where MCP goes next.
- **What**: An exploration of what would become possible if servers could call tools from clients — inverting MCP's current asymmetric model where only clients invoke server tools (from abstract only; the program description is a single line, so depth is unknown).
- **How**: Conceptual/speculative session on protocol symmetry, not a deployed feature.
- **Where applicable**: Protocol watchers and anyone designing MCP-adjacent infrastructure; no immediate operational applicability.

## Themes

- **MCP is going through infrastructure adolescence**: stateless transports, async Tasks, proxy handling, and a middleware standard (SEP-1763 Interceptors) are all on the same trajectory web protocols took — shedding per-connection state, adding intermediaries, and defining durable execution semantics. This cycle's protocol talks are the ones to track for deployment planning.
- **Scale operators converge on the same pain points**: Amazon, Uber, Equinix, Bloomberg, and Duolingo all report the same wall — tool discovery at scale, governance and ownership, evaluation of tool quality, and policy enforcement between model and data. The patterns differ (Protobuf generation, registries, interceptors) but the problem shape is identical.
- **Context-window economics is the new capacity planning**: tool search, codemode, progressive tool exposure, and metadata summarization are all attacks on the same constraint — token cost of describing capabilities. This is where agent infrastructure design decisions are being made this cycle.
- **Agents are moving from chat to operations**: kernel scheduler observability (scxtop/MCP), incident triage and Jenkins debugging from Slack, autonomous detect→fix loops — the ML-for-infrastructure-operations trend is real and showing up in production tooling, not just demos.
- **Security is playing catch-up on multiple fronts at once**: DNS rebinding against local servers, shadow MCP deployments invisible to traditional controls, prompt injection/memory poisoning systematization, and identity work (CIMD, RFC 9728, ID-JAG) — a signal that agent access to infrastructure needs a security architecture before, not after, rollout.
