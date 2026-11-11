>>> HOW TO RUN THIS <<<
This is the digest prompt for aiengineer-europe-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/aiengineer-europe-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/aiengineer-europe-2026.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, cloud
platforms, Kubernetes, and AI. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect); cloud infrastructure and operations (public and private
cloud, virtualization, compute/storage/networking, multi-tenancy, and
automation); Kubernetes and cloud-native systems (architecture and
operations, eBPF, Cilium, Kubernetes networking, Gateway API, service mesh,
IPAM, and BGP/datapath internals); and AI (AI/ML systems, LLMs and agents,
model training and inference, GPU/accelerator infrastructure, networking for
AI, and ML for infrastructure operations). Physical DC and WAN systems work is
CORE to this PM, not adjacent — do not down-rank a paper for being about
hardware, optics, or datacenter fabric.

Below is the program for AI Engineer Europe 2026. Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

Judge each item by what it changes for a practitioner: novel techniques and
firmly substantiated results over incremental benchmark improvements, and
operational lessons, tooling, automation and postmortems that transfer across
environments over org-specific anecdotes or vendor pitches in disguise.
Treat strong empirical evaluation and real deployment experience as signals of
weight; treat unvalidated claims with caution. Note when a technique depends
on a specific operator's scale, topology or silicon.

## Enriching from the source material (best effort)

The program text gives you a title, authors, and an abstract per item, and
often links (`page:`, `pdf:`, `slides:`, `video:`). The abstract alone is thin — the full
paper has the methodology, real results, and limitations that make the What /
How / Where-applicable sections accurate instead of guessed.

If you have a tool to fetch URLs, then for EACH selected item (Core, Adjacent,
and Wildcard) try to retrieve the fuller source before writing it up:

- Prefer a `pdf:` link; else fetch the `page:` link (often has the full text or
  a longer description); a `video:` link is a last resort, don't transcribe it.
- Use what you retrieve to ground What/How/Where-applicable in the paper's
  actual contributions, evaluation, and stated constraints.

This is strictly best-effort. Many links fail or are paywalled:

- If a fetch fails, is paywalled, returns only an abstract, or you have no fetch
  tool, just fall back to the abstract already in the program text. That is
  fine and expected — do not stall or skip the item.
- NEVER invent paper contents, numbers, or findings from a failed or partial
  fetch. If you only had the abstract, write from the abstract.
- Note when an item's write-up is based only on the abstract, e.g. end its
  What line with "(from abstract only)", so the reader knows the depth.
- Do not let enrichment change which items you select or their tier; selection
  is from the program. Enrichment only deepens the write-up.

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to the PM's core interests as listed above
  (networking, cloud, Kubernetes, or AI) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title**: the `###` heading is the item's title exactly as the program
  gives it, with nothing added. Speaker(s)/author(s) with affiliation go on
  the line below it.
- No links section: the pipeline puts a links row (abstract page, paper,
  slides, recording) under every heading after you finish, from the program's
  `page:`/`pdf:`/`slides:`/`video:` lines and from verified sources. Do not
  write one, and do not link the title.
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Search keywords

The site's search indexes topic keywords per page. After the Themes section,
append ONE fenced `json` code block - the pipeline reads it machine-side and
removes it before publishing, so it is never rendered - of exactly this shape:

```json
{"post": ["cloud", "ai"], "talks": {"<pick heading>": ["cloud", "ai-networks"], "<pick heading>": ["kubernetes", "cni"]}}
```

- "post": 3-6 topics this digest as a whole covers.
- "talks": one entry for EVERY pick you selected, keyed by its exact `###`
  heading string (copy it character for character, including any presenter
  part), with 2-4 tags naming what the talk is about - the technology or
  practice, not its tier or the conference.
- Tags are lowercase, hyphenated, single concepts. Use ONLY tags from this
  vocabulary:

- `ai` - artificial intelligence systems, applications and practices not covered by a finer AI tag
- `ai-networks` - networking for AI/ML training and inference clusters (job-level load balancing, collectives, topology-aware scheduling)
- `gpu-clusters` - GPU accelerator interconnects and cluster fabrics (NVLink, scale-up vs scale-out)
- `ml-for-networking` - machine learning applied to network operation (anomaly detection, traffic prediction, AIOps)
- `data-center-fabric` - physical data-center fabric design (topologies, CLOS, buffer management, congestion)
- `optics` - optical transport, transceivers, pluggables, DWDM, LPO/CPO
- `ethernet` - Ethernet as a technology standard (P802.3 work, speeds, PHYs)
- `cabling` - structured cabling, fiber plants, MPO/MTP, copper
- `power` - power delivery and efficiency in DCs (PUE, 48V, power sourcing equipment)
- `dpu` - data processing units, SmartNICs, offload and hardware offload in general
- `rdma` - RDMA, RoCE, InfiniBand, remote memory semantics
- `load-balancing` - traffic load balancing, ECMP/adaptive hashing, LB algorithms and architectures
- `packet-scheduling` - packet scheduling and queueing disciplines (PIFO, QoS schedulers, traffic management)
- `congestion-control` - congestion control and notification (ECN, PFC, DCQCN, L4S)
- `switching` - switch hardware and forwarding architecture (ASICs, buffers, pipelines)
- `silicon` - switch/NPU ASIC design, chip roadmaps, co-packaging
- `bgp` - BGP the protocol and its operation
- `routing-protocols` - routing protocol design and operation in general (ISIS, OSPF, BGP convergence)
- `segment-routing` - SR, SRv6, SR-MPLS and network programming with them
- `ipv6` - IPv6, its deployment and transition
- `mpls` - MPLS, labels, and LDP/RSVP heritage
- `peering` - peering business and practice, IXPs, interconnection agreements
- `interconnection` - data center interconnect and carrier interconnection
- `cdn` - content delivery networks
- `address-policy` - IP address and ASN allocation policy (RIR policy processes)
- `internet-governance` - regulation, standards bodies, and geopolitics of the internet
- `kubernetes` - Kubernetes architecture, operations, workloads and networking
- `cni` - container network interfaces and container networking plugins
- `containers` - containerization, images, runtimes
- `service-mesh` - service mesh (sidecars, eBPF meshes, mTLS between services)
- `cloud` - public and private cloud infrastructure, platforms and operations
- `cloud-native` - cloud-native patterns in general (CNCF ecosystem)
- `orchestration` - workflow and device orchestration, intent-based systems, network controllers
- `automation` - network automation (tooling, pipelines, source of truth, CI/CD for networks)
- `configuration-management` - managing device configuration at scale (config generation, drift, validation)
- `gitops` - GitOps workflows and version control practices
- `p4` - the P4 language and P4-programmable targets
- `linux-networking` - the Linux kernel networking stack (TC, netlink, drivers, offloads)
- `programmable-dataplane` - programmable data planes in general (PNA, portable switch OSes, pipes)
- `ebpf` - eBPF, XDP, and kernel bypass dataplanes
- `http` - HTTP and web protocols, QUIC
- `ipam` - IP address management and allocation
- `sdn` - software-defined networking, controllers, separation of control and data plane
- `network-security` - network security topics not covered by a finer tag
- `email-security` - email security and phishing (DMARC, spam, brand abuse)
- `malware-analysis` - malware, reverse engineering, botnet takedowns
- `threat-intelligence` - threat intel, IoCs, attack tracking
- `vulnerability-management` - vulnerability disclosure, patching, CVE economy
- `offensive-security` - offensive security, red teaming, exploit development
- `privacy` - privacy engineering, tracking, anonymity, privacy-preserving systems
- `censorship` - censorship, filtering, and measurement of Internet shutdowns
- `ddos` - DDoS attack and defense
- `anomaly-detection` - detecting anomalies and attacks in traffic
- `firewall` - firewalling and network policy enforcement
- `tls` - TLS, certificates, and protocol encryption
- `encryption` - encryption of traffic and data in general (MACsec, IPsec, E2E)
- `quantum-safe` - post-quantum cryptography and migration
- `quantum-networking` - quantum networking and entanglement distribution as infrastructure
- `pki` - public key infrastructure, certificate lifecycle
- `attestation` - remote attestation, measured boot, hardware roots of trust
- `zero-trust` - zero-trust architecture and microsegmentation
- `identity` - digital identity, identity ecosystems, ID standardization
- `authentication` - authentication methods and protocols (MFA, passkeys, WebAuthn)
- `authorization` - authorization, OAuth/OIDC, access control, policy engines
- `observability` - network observability tooling, telemetry pipelines, flow data
- `telemetry` - telemetry protocols (gNMI, streaming, INT)
- `measurement` - measurement methodology, probing, active/passive measurement studies
- `benchmarking` - benchmarks, testbeds, performance evaluation of systems
- `testing` - testing and verification of networks and configs (formal verification belongs here)
- `sre` - site reliability engineering practice, incident response, operations culture
- `capacity-planning` - capacity planning and forecasting
- `troubleshooting` - troubleshooting and root-cause analysis, outages and postmortems
- `dns` - DNS, resolvers, authoritative infrastructure
- `multicast` - multicast and broadcast replication
- `wifi` - wireless and mobility
- `mobile` - mobile and cellular networks (5G, roaming, RAN)
- `iot` - Internet of Things scale problems, LPWAN
- `cxl` - CXL and memory-fabric interconnects for pooled memory
- `time-sync` - time and clock distribution (NTP/PTP, GNSS timing)
- `spectrum` - radio spectrum policy and management
- `open-source` - open-source project practice and sustainability
- `standardization` - standards processes (IETF/IEEE) and documents
- `api` - APIs for network control (REST/gRPC, schemas, contract design)

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

The digest is read on GitHub (GitHub-Flavored Markdown viewed in the repo) and
on the project's Zensical site, which renders the same file. Use only syntax
both render reliably, and follow these rules:

- Headings with `#`/`##`/`###`; bold with `**...**`; italics with `*...*`.
- Bullet lists with `-`. Put a blank line before every list, before every
  heading, and between paragraphs, or they won't render correctly.
- Indent nested lists by four spaces per level; avoid deeper nesting.
- Any link you do write is `[text](url)` — never a bare URL — and uses a URL
  exactly as the program text gives it.
- No raw HTML except the metadata comment below. Do not use heading IDs,
  footnotes, definition lists, or other non-GFM extensions.
- You may use tables and `code spans` where they genuinely help, since GitHub
  supports them; don't force them.

Begin the output with this metadata, wrapped in an HTML comment so it does not
show in the rendered view but stays in the source:

<!--
conference: AI Engineer Europe 2026
source_url: https://ai.engineer/europe/2026/sessions.json
generated: 2026-11-11
registry_key: aiengineer-europe-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## April 8
### AI Coding For Real Engineers
Speakers: Matt Pocock
Schedule: 3:45pm-5:45pm · St. James · workshop
A hands-on workshop covering the full lifecycle of AI-assisted development, from turning ambiguous requirements into agent-ready plans to running autonomous coding agents that ship production features. You'll learn to stress-test vague briefs into structured PRDs, slice work into thin "tracer bullet" vertical slices, and run an AI agent with TDD. You'll watch it select tasks, write tests, implement code, and commit. You'll then refine your prompts based on where it struggles, graduate to fully autonomous (AFK) runs, and learn to design codebases that maximize agent effectiveness. You'll walk away knowing how to: - Turn ambiguous requirements into agent-ready issues - Slice work into vertical tracer bullets an agent can grab independently - Run AI agents human-in-the-loop and autonomously with TDD - Design codebase architectures that AI agents love to work in For: Engineers ready to move beyond chat-based AI assistance and build a real workflow for shipping features with autonomous coding agents.

### Make your own event-sourced agent harness using stream processors
Speakers: Misha Kaletsky, Jonas Templestein
Schedule: 10:40am-12:00pm · Shelley · workshop
https://github.com/iterate/ai-engineer-workshop This workshop is in two parts: First, we'll show you for 10 minutes how to make a basic agent harness on top of our humble durable streams ish API . The only abstraction we'll need is a simple "stream processor", which consists of 1) Some state (e.g. "message history" and "is an llm request in progress") 2) A reducer that takes events and sometimes updates the state 3) A hook / reactor that causes side effects (such as LLM requests) after an event is added to the stream Then we'll give you an hour to build the coolest possible thing with this. You can implement from scratch - an agent that calls tools via codemode - an agent with multiple LLM calls in progress at once - agent-to-agent message capability - an agent that responds to slack messages - an agent that is deployed as a serverless function and "wakes up" when new events arrive And much more! It's kind of a wild abstraction that we started hacking on last week. Hitting all the buzzwords - event sourced - serverless - agent harness Check Second, you'll get to implement an agent harness of your dreams. You can - Implement code mode from scratch - Experiment with safety It's a bit like making pi extensions, without trying to run them all in a single process. In this workshop we'll show you how to build an AI agent like claude or pi or codex from scratch on top of this very simple abstraction.

### TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM
Speakers: Cormac Brick
Schedule: 10:40am-12:00pm · Moore · workshop
No description published; title, speakers and schedule only.

### How to Build Agents That Run for Hours (Without Losing the Plot)
Speakers: Ash Prabaker, Andrew Wilson
Schedule: 9:00-10:20am · St. James · workshop
We'll cover: why self-evaluation is a trap and adversarial evaluator agents work better; why context compaction doesn't cure coherence drift but structured handoffs do; how to decompose work into testable sprint contracts; how to grade subjective output with rubrics an LLM can actually apply; and how to read traces as your primary debugging loop. Plus the question nobody asks: which parts of your harness should you delete when the next model drops?

### Building your own software factory
Speakers: Eric Zakariasson
Schedule: 10:40am-12:00pm · St. James · workshop
Most of us are pair-programming with one agent and stopping there. There's a lot more on the table.This workshop is about going from one agent to many. We'll start with codebase setup, the foundational work that makes agents effective on their own. Then we'll scale up to running agents in parallel, kicking off async work that keeps going while you context-switch to something else, and setting up automations for the things you're still doing by hand.

### Skill Issue: How We Used AI to Make Agents Actually Good at Supabase
Speakers: Pedro Rodrigues
Schedule: 9:00-10:20am · Abbey · workshop
Writing Agent Skills is easy. Writing ones that actually improve agent performance is not. In this hands-on workshop, you’ll build, test, and iterate on Agent Skills against real Supabase workflows using a prebuilt environment with MCP, CLI tooling, and an eval harness powered by Braintrust. You’ll start by writing a simple Skill and observing how it changes agent behavior. Then we’ll push further: you’ll modify the Skill, introduce bad patterns, and see how performance shifts — sometimes improving, sometimes getting worse, and sometimes doing nothing at all. Along the way, we’ll surface common failure modes, like Skills that aren’t used, misleading instructions, or changes that look good but don’t hold up under evaluation. The core loop of the workshop is simple: write a Skill, run evals, inspect results, and iterate. By the end, you’ll have a practical understanding of how to validate Skills, how to avoid common pitfalls, and how to design Skills that actually help agents perform better in real systems. If you’re working with agents, this workshop will give you the tools to move beyond guesswork and start measuring what actually works. And if you want to see how these patterns hold up at scale, the follow-up talk on the 9th dives into our eval results and what actually moved the needle in production.

### Vibe Engineering Effect Apps
Speakers: Michael Arnaldi
Schedule: 1:15pm-3:15pm · Shelley · workshop
The workshop will focus on practical coding with LLMs when using Effect

### Let's go Bananas with GenMedia
Speakers: Guillaume Vernade
Schedule: 9:00-10:20am · Rutherford · workshop
No description published; title, speakers and schedule only.

### Codex and Subagents
Speakers: Vaibhav Srivastav
Schedule: 9:00-10:20am · Westminster · workshop
No description published; title, speakers and schedule only.

### Agentic Search for Context Engineering
Speakers: Leonie Monigatti
Schedule: 9:00-10:20am · Wordsworth · workshop
1. From RAG to Agentic Search How retrieval evolved from RAG to agentic RAG, and why agents building their own context changes everything.2. Choosing the Right Search Interface: Shell tools, dedicated database tools, file search. When each works, when each hits a ceiling, and how to combine them. 3. Building Effective Database Retrieval Tools Many search tools are usually built-in. Database tools are powerful when customized. Practical guide on how to build effective database retrieval tools, including tool scoping, descriptions, output engineering, and error handling.4. Wrap-up + Q&A

### AI SDK v6
Speakers: Nico Albanese
Schedule: 9:00-10:20am · Shelley · workshop
No description published; title, speakers and schedule only.

### Frontier AI at Home (literally)
Speakers: Alex Cheema
Schedule: 1:15pm-3:15pm · Moore · workshop
We'll walk you through running frontier AI locally at home. It's not what you think.

### Building Conversational Agents
Speakers: Thor Schaeff, Philipp Schmid
Schedule: 1:15pm-3:15pm · Rutherford · workshop
No description published; title, speakers and schedule only.

### Skills at Scale
Speakers: Nick Nisi, Zack Proser
Schedule: 10:40am-12:00pm · Abbey · workshop
Write once, run in Claude, Codex, Cursor, and your own agents Every developer using AI tools has the same problem: they prompt the same way, for the same tasks, over and over. Skills fix this. A skill is a portable unit of agent behavior that teaches any AI tool how to do a specific job. Write one, drop it into your editor, and it just works. Across tools. Across teams. Most people don't know this primitive exists. In this hands-on workshop, you'll write real skills, test them live, and see how one file can power Claude.ai, Claude Code, Cursor, and Codex without changing a line. Then we'll go deeper. You'll see how the WorkOS CLI uses this same pattern to power 15 framework integrations — each one a skill composed with others, wired into an agent that installs and configures AuthKit in under 60 seconds. That's not a demo. That's production code, shipping today. What you'll do: Write 2+ skills for tasks you actually do at work Install and test them across AI tools in real time Learn the craft of good skill writing — specificity, constraints, composability See how skills compose and scale inside a real CLI powered by the Claude Agent SDK What you'll leave with: Working skills installed in your AI tools, ready to use Monday morning A repeatable pattern for turning any recurring task into a portable skill The mental model for when a skill is enough and when you need a full agent No repos to clone. No dependencies to install. Bring a laptop with Claude Code or Claude.ai and something you're tired of doing manually.

### Mergeable by default: Building the context engine to save time and tokens
Speakers: Peter Werry
Schedule: 1:15pm-3:15pm · Wordsworth · workshop
Agents can generate code. The hard part is generating code that's right for your system, team conventions, and past decisions. That's a context problem that naive RAG, MCP servers, and bigger context windows don't solve. Without the right context, that code costs you twice: once in tokens, again in long review cycles. This session is a practitioner's guide to building a context engine: the reasoning layer that brings together your organizational context and delivers only what the agent needs for the task at hand. I'll walk through the challenges that matter: reasoning across conflicting sources, maintaining permissions, and personalizing results based on who's asking and what they're working on. Along the way, we'll go deep on specific components with live demos and technical breakdowns. Drawn from real lessons building this in production, including what we got wrong.

### Shipping complex AI applications | Braintrust & Trainline
Speakers: Giran Moodley, Mayan Soni, Oussama Hafferssas
Schedule: 1:15pm-3:15pm · Westminster · workshop
Getting a prototype working is straightforward. Making it reliable in production, especially with multi-step agents, tool use, and real users is the hard part. In this hands-on workshop, you'll work through the core parts of building production-grade AI applications with Braintrust.

### Playground in Prod - Optimising Agents in Production Environments
Speakers: Samuel Colvin
Schedule: 10:40am-12:00pm · Westminster · workshop
Deploying an agent is just the beginning. The real challenge is making it better once it's live — without redeploying, without downtime, and ideally without a human in the loop at all. In this talk I'll introduce two complementary approaches to optimising agents in production, both built on Pydantic AI and Logfire: **Managed Variables** — a new Pydantic AI feature (build on the Open Feature standard) that lets you externalise key parameters of your agent (system prompts, model configuration, tool descriptions, thresholds) and update them instantly from the Logfire UI. Change a system prompt, swap a model, or adjust a temperature parameter and see the effect on the next request — no redeploy, no restart. This turns production into a playground where you can iterate on agent behaviour in seconds based on real traffic and real feedback. **Autonomous optimisation with GEPA** — once you can update agent parameters without redeploying, the natural next step is to let an optimiser do it for you. I'll show how GEPA (Genetic-Pareto reflective text evolution) can be wired into Logfire's managed variables to create a closed loop: observe agent performance via Logfire traces, reflect on failures, evolve better prompts, and push improvements live — all without human intervention. Together these form a practical workflow: start by manually tuning your agent in production using managed variables, build up evaluation datasets from real traces, then hand the optimisation loop to GEPA to continuously improve performance. ## Outline 1. **The problem with agent deployment today** — why "deploy and forget" doesn't work for agents, and why traditional CI/CD is too slow for prompt iteration. 2. **Managed Variables in Logfire** — live demo showing how to externalise a system prompt, update it from the Logfire dashboard, and see the change take effect immediately on a running agent. 3. **From manual tuning to automated optimisation** — using Logfire's observability data (traces, evaluations, failure modes) to build the feedback signal GEPA needs. 4. **GEPA + Managed Variables** — closing the loop: GEPA reflects on agent traces, evolves better prompts, and pushes them live via managed variables. Live demo of an agent that gets measurably better over time without any code changes. 5. **Practical considerations** — guardrails, rollback, A/B testing between prompt variants, and when to trust autonomous optimisation vs. keeping a human in the loop. ## Audience Takeaways - How to set up agents so key parameters can be changed without redeployment - A practical workflow for iterating on agent behaviour using production data - How reflective prompt evolution (GEPA) works and when to use it - How to combine Pydantic AI, Logfire, and GEPA into a continuous improvement loop for production agents

### Mind the Gap (In your Agent Observability)
Speakers: Amy Boyd, Nitya Narasimhan
Schedule: 9:00-10:20am · Moore · workshop
No description published; title, speakers and schedule only.

### Building Your Own Secure AI Workflows: Human-in-the-Loop Automation with n8n
Speakers: Liam McGarrigle
Schedule: 10:40am-12:00pm · Wordsworth · workshop
Session title and abstract to be finalized by participating speaker

### Training an LLM from Scratch, Locally
Speakers: Angelos Perivolaropoulos
Schedule: 3:45pm-5:45pm · Abbey · workshop
No description published; title, speakers and schedule only.

### Build Your First Demand-Driven Context Base: Let AI Agents Tell You What They Need
Speakers: Raj Navakoti
Schedule: 3:45pm-5:45pm · Shelley · workshop
London's black cab drivers don't learn "The Knowledge" by reading a map. An examiner gives them a destination, they get lost, they discover which streets they didn't know, they go learn those streets. Each run fills gaps the previous one revealed — until they know the city. Nobody told them what to learn. The journeys told them. That's the opposite of what every enterprise team is doing with AI agents right now. We curate tribal knowledge into skills.md files and structured knowledge bases, three people argue over a Miro board about what the agent needs to know, someone screenshots it into Confluence, and we wonder why the agent still can't reason about anything domain-specific. The industry has great tools for context management — RAG, vector databases, prompt engineering. But the harder unsolved problem is context discovery: how do you even know what to curate? Without solving it, your enterprise agent is just an expensive autocomplete. In this hands-on workshop, you'll do what the cab drivers do — and what we do at IKEA Digital — give your agent destinations instead of maps. You'll build a Demand-Driven Context (DDC) base from scratch, where real problems drive what gets curated, not top-down guessing. The exercise is simple but the insight is profound: You'll get a realistic enterprise problem (we provide problem cards) You'll give it to an AI agent with zero domain context The agent will fail — and generate an information checklist of exactly what's missing You'll fill the gaps using reference material we provide The agent will try again — and succeed That moment — when the agent goes from confidently wrong to correctly reasoned — is when DDC clicks. You didn't document everything. You documented exactly what one problem demanded. Now multiply that by 30 problems and you have a better knowledge base than months of top-down curation. What you'll build: A working knowledge base repo with structured domain entities, a sandbox for problem exploration, and a repeatable process for growing the knowledge base problem-by-problem. Everything in Markdown — human-readable, machine-parseable, Git-friendly. You'll also see how to use Claude Code sub-agents to separate concerns — a curator agent that identifies what context is missing, a solver agent that uses the curated context to reason, and role-specific agents (architect, engineer, product owner) that share the same knowledge base but operate with different reasoning boundaries. No custom tooling required — just CLAUDE.md files, sub-agent task delegation, and the knowledge repo structure doing the heavy lifting. What you'll experience: The "flip" moment — agents telling you what they need instead of you guessing what to give them How learning paths emerge from problems rather than being designed upfront How different problems reveal overlapping context needs — showing you where to invest curation effort The TDD parallel — DDC is to knowledge bases what TDD is to code What you'll see from real production use: We've been running DDC at IKEA Digital against real vendor integration problems, architecture decisions, and system design tasks. The workshop includes a live walkthrough of actual DDC sessions — real enterprise problems, the information checklists agents generated, how context was curated, and the before/after of agent output quality. You'll see real numbers: knowledge base growth curves, context reuse across problems, and how agent accuracy improves from problem 1 to problem N. What you'll leave with: A working DDC knowledge base you can extend with your own domain A repeatable process for demand-driven curation A template repo with structure, formats, and agent guidance Evidence from real production use that demand-driven curation produces less volume but more signal than top-down documentation The conviction that 30 real problems beat 6 months of documentation No specific programming language required. Bring a laptop with Claude Code, Cursor, or any LLM-powered coding tool. All content is in Markdown — this is about knowledge, not code. Whether you're an engineer building enterprise agents, an architect designing knowledge systems, or a team lead who's tried and failed to curate domain knowledge for LLMs — this workshop gives you a framework you can apply the week you get home from London.

### Build & deploy AI-powered apps
Speakers: Paige Bailey
Schedule: 3:45pm-5:45pm · Rutherford · workshop
No description published; title, speakers and schedule only.

### Ship Real Agents: Hands-On Evals for Agentic Applications
Speakers: Laurie Voss
Schedule: 3:45pm-5:45pm · Westminster · workshop
You shipped an AI agent. It works great on your test queries. But how do you know it works on your users' queries? How do you know a prompt change that fixes one thing didn't break three others? And when a new model drops next quarter, how do you know whether to upgrade? If your answer to any of these is "I run it a few times and check," this workshop is for you. In this hands-on session, you'll build a complete evaluation pipeline for an AI agent from scratch. Starting with a financial analysis chatbot built on the Claude Agent SDK, you'll instrument it with tracing, run it against diverse test cases, and then do the thing most tutorials skip: actually read your data. You'll categorize failures by root cause, define success criteria, and use that analysis to decide what to measure before writing a single eval. Then you'll build three types of evaluators: fast deterministic code checks, built-in LLM-as-a-judge evals like faithfulness, and a custom rubric you design yourself. You'll validate your judges against your own human labels, because an eval you haven't tested is just a fancy way of being wrong at scale. The workshop doesn't stop at scoring. You'll save failure cases as reusable datasets, improve your agent's prompts based on what the evals told you, and run controlled experiments to prove the improvement with numbers instead of gut feel. Along the way, you'll learn practical frameworks: the impact hierarchy for prioritizing fixes, the Swiss Cheese model for layering defenses, and the eval-iterate cycle that turns a prototype into a production system. You'll leave with a working notebook, a free Phoenix Cloud account with your traces and eval results, and a repeatable process you can apply to any AI application the day you get home.

### Everything You Need To Know About Agent Observability
Speakers: Danny Gollapalli, Ben Hylak
Schedule: 3:45pm-5:45pm · Wordsworth · workshop
Let your AI agents proactively report their own failures. This workshop introduces Raindrop Self Diagnostics, showing how agents can call home, classify failures, filter noise, and alert teams when critical issues arise. Attendees will learn how to instrument self-reporting, understand the default diagnostic categories, and use agent-reported signals to improve production observability.

### Build Your Own Deep Research Agent + Technical Writer
Speakers: Louis-François Bouchard, Paul Iusztin, Samridhi Vaid
Schedule: 1:15pm-3:15pm · St. James · workshop
Deep research is one of the best ways to learn how to build real AI systems because it forces you to combine reasoning, planning, autonomy, tools, grounding, and feedback loops in a single end-to-end workflow. In this hands-on workshop, you will build an MCP-powered deep research agent that can plan a research strategy, search the web, analyze YouTube videos, gather grounded evidence, filter for relevance and trustworthiness, and synthesize its findings into a cited research artifact. Rather than treating research as just another chatbot interaction, we will frame it as a goal-directed research loop: one that can search, inspect, pivot, and progressively refine its understanding of a topic. From there, we will connect that research artifact to a lightweight technical writing workflow that turns raw findings into polished, non-sloppy technical multimodal content. This second part of the system is deliberately more constrained: you will see how research and writing require much different architectures, why exploratory work benefits from agentic behavior, and why writing quality often improves with tighter workflows, review loops, and explicit guidance. Along the way, we will show how to choose between prompts, workflows, and agents depending on the task, and how to keep the overall system practical rather than over-engineered. We will also cover observability and evaluation so the system is not only impressive in a demo, but measurable and improvable in practice. Most importantly, the workshop is grounded in experience: it distills what we learned over the past year building and using this research-and-writing pipeline internally. Attendees will leave with their own deep research agent, connecting it to a reliable technical writing workflow, and understanding the engineering tradeoffs behind both.

### Ralph Loops: Build Dumb AI Loops That Ship
Speakers: Chris Parsons
Schedule: 1:15pm-3:15pm · Abbey · workshop
Dumb loops beat clever workflows. Most teams building with AI agents reach for multi-agent orchestration, planning graphs, and elaborate tool chains. Then they spend months debugging them. A single loop that processes one ticket at a time, evaluates its own output, and improves on the next run will outperform all of it. In this hands-on workshop you will build three things. First, a working Ralph Loop that processes real tickets end-to-end. Second, a synthetic feedback loop so you can test and iterate locally without waiting on production data. Third, a self-improving cycle where the loop's output quality gets better with every run without you touching the prompt. We will also dig into what this means for teams: when one loop can clear a backlog that used to need five people, the interesting questions stop being technical. Bring your laptop. You will leave with working loops you can take back to your team.

### OpenClaw Open Hours #1
Schedule: 9:00-10:20am · Wesley · workshop
Hands-on peer-led sessions to help fellow AI Engineers set up, configure, and share their OpenClaw, NanoClaw, and other personal agent setups. Bring your laptop, ask questions, pay it forward and make friends!

### OpenClaw Open Hours #2
Schedule: 10:40am-12:00pm · Wesley · workshop
Hands-on peer-led sessions to help fellow AI Engineers set up, configure, and share their OpenClaw, NanoClaw, and other personal agent setups. Bring your laptop, ask questions, pay it forward and make friends!

### OpenClaw Open Hours #3
Schedule: 1:15pm-3:15pm · Wesley · workshop
Hands-on peer-led sessions to help fellow AI Engineers set up, configure, and share their OpenClaw and other personal agent setups. Bring your laptop, ask questions, pay it forward and make friends!

### OpenClaw Open Hours #4
Schedule: 3:45pm-5:45pm · Wesley · workshop
Hands-on peer-led sessions to help fellow AI Engineers set up, configure, and share their OpenClaw, NanoClaw, and other personal agent setups. Bring your laptop, ask questions, pay it forward and make friends!

## April 10 — GPUs & LLM Infrastructure
### You Might Not Need 50 Diffusion Steps
Speakers: Ziv Ilan
Schedule: 2:30-2:50pm · Abbey · talk
No description published; title, speakers and schedule only.

### Scaling Reinforcement Learning: Lessons from Trillion-Token Deployments at Fortune 500s
Speakers: Alessandro Cappelli
Schedule: 11:40am-12:00pm · Abbey · talk
Building production-ready agents with Reinforcement Learning (RL) requires significantly more than a standard RFT (Rejection Fine-Tuning) API. To move beyond the "Assistant" hype and unlock true agentic impact, enterprises must adopt a holistic RLOps approach. In this session, Alessandro Cappelli (Co-founder & Chief Customer Officer, Adaptive ML) explains what is needed to deploy Enterprise AI at scale. * Synthetic Data Generation Strategies: How to bootstrap specialized models using your own proprietary datasets to create high-fidelity training signals. * Self-Play & Mock Environments: Building the "digital playgrounds" where agents can fail safely and learn exponentially. * Aligned AI Judges: Moving past the "human-in-the-loop" bottleneck by deploying specialized models to maintain quality and alignment at scale. Attendees will learn how a unified RLOps pipeline bridges the gap towards business value, turning generalist models into specialized, high-performance assets for complex organizations.

### The Embedding Infrastructure Nobody Built (So We Did)
Speakers: Filip Makraduli
Schedule: 12:00-12:20pm · Abbey · talk
I wrote an article about making embedding inference fast. Flash Attention, memory hierarchy, all the usual advice. Then I posted it, and the internet told me I was wrong attention is 6% of the workload, my optimization advice was backwards, and I'd never actually profiled the thing I was writing about. Here's the thing: we were building an embedding inference engine when this happened. And the corrections didn't just fix my article — they exposed gaps in everything we'd seen in the ecosystem. TEI gives you one model per container, so five models means five deployments. Infinity crashes under load. Everyone assumes you know exactly which model you want before you start the server. Nobody handles what happens when you're running three models and memory fills up. So we built what we actually needed: an inference engine where you load models at query time, not deploy time. Where you can hot-swap between dozens of models on one GPU without restarting anything. Where memory pressure triggers LRU eviction instead of an OOM crash. Where trying a new embedding model doesn't mean a rebuild. This talk is the story of how internet feedback reshaped both an article and a product. I'll show you the profiler traces that proved the commenters right, the infrastructure gaps we found when we looked harder, and how we filled them. Small-model inference is the infrastructure nobody built. So we did.

### The Missing Primitive for Agent Swarms
Speakers: Lou Bichard
Schedule: 12:20-12:40pm · Abbey · talk
Everyone's building swarms. Few are asking what infrastructure they actually need. Most agent frameworks treat multi-agent coordination as an application-level concern - spawn threads, manage state, hope for the best. This works on demos. It falls apart when you need ten agents exploring a codebase in parallel, each with their own environment, tools, and context. The problem is that we're missing a platform primitive: the ability to spawn isolated agent execution contexts on demand, with their own identity, resource limits, and coordination semantics. Without this, every swarm implementation reinvents the same brittle scaffolding. In this talk, I'll cover: - Why current approaches (threads, worktrees, container pools) break down at scale - What a proper swarm primitive looks like: identity, isolation, lifecycle, coordination - How we're building this at Ona and what we've learned shipping it to enterprises - The UX implications: how users interact with fleets of agents, not just one Swarms aren't a feature. They're an infrastructure category. It's time we built them that way.

### Scaling the Next Paradigm of Heterogeneous Intelligence
Speakers: Adrian Bertagnoli
Schedule: 12:40-1:00pm · Abbey · talk
To date, the dominant trajectory of AI progress has been defined by a homogeneous paradigm: capturing performance gains by scaling uniformity at both the architectural level (monolithic models) and the hardware level (identical GPU clusters). But it is becoming increasingly clear that real-world intelligence demands multi-agent systems, where specialised components must collaborate to solve long-horizon, multi-turn, and multi-task problems. In this talk, we outline how a new paradigm - Heterogeneous Intelligence - is the essential scaling paradigm for this emerging era. We present early findings demonstrating how heterogeneity across workflows, model architectures, and hardware can be exploited as a source of advantage rather than treated as complexity to be minimised. For example, heterogeneous optimisation yields simultaneous improvements in cost, speed, and task performance such as enabling automated payment workflows to execute reliably at reduced compute cost or achieving higher accuracy in deep context reasoning over long documents by specialising sub-tasks across purpose-matched chips and models. We conclude with what we believe to be promising frontiers in this direction, including how new systems of intelligence will be discovered through iterative, symbiotic hardware-algorithm co-evolution.

### Beyond Code Coverage: Functionality Testing with Playwright
Speakers: Marlene Mhangami
Schedule: 2:50-3:10pm · Abbey · talk
AI has gotten faster at writing application code and to keep up many developers have let AI write their tests as well. Those tests might pass from a code coverage perspective but the final test is whether or not the application works functionally as expected. Now more than ever AI generated projects require end to end testings to help verify that applications work beyond self affirming unit tests created by LLMs. In this talk we'll understand how to build tests with Playwright. We'll discuss what Playwright is, how to set it up in Agentic workflows and walkthrough some examples of how developers are using it locally and in CI. We'll also look at best practices for using Playwright and accessing it through the new MCP server.

### Don't Build Slop (4 Levels of AI Agent Maturity)
Speakers: Ara Khan
Schedule: 3:10-3:30pm · Abbey · talk
Everyone and their grandmother is building an agent, most of them badly. This talk breaks the problem into four levels, from framework prototyping to cloud-native agent fleets that scale to millions of tasks. Each level is harder and one step closer to something that actually works in production.

## April 9
### Opening Address
Speakers: AIE Welcome
Schedule: 9:00-9:10am · Keynote · keynote
No description published; title, speakers and schedule only.

### The New Application Layer
Speakers: Malte Ubl
Schedule: 9:10-9:30am · Keynote · keynote
AI engineering is the legitimate successor to web development and the mainstream discipline that will define the next decade. Drawing on Vercel's own experience, Malte explores what it means to build infrastructure and applications in a world where agents are both the builders and users of software. In a future where the major AI labs commoditize, the real value will sit with the engineers building on top. The application layer is where the innovation happens, and AI engineers are the ones who will shape it.

### Frontier AI and the Future of Intelligence
Speakers: Raia Hadsell
Schedule: 9:30-9:50am · Keynote · keynote
No description published; title, speakers and schedule only.

### Harness Engineering: How to Build Software When Humans Steer and Agents Execute
Speakers: Ryan Lopopolo
Schedule: 9:50-10:10am · Keynote · keynote
No description published; title, speakers and schedule only.

### OpenClaw update
Speakers: Peter Steinberger
Schedule: 10:10-10:30am · Keynote · keynote
No description published; title, speakers and schedule only.

### It Ain't Broke: Why Software Fundamentals Matter More Than Ever
Speakers: Matt Pocock
Schedule: 5:20-5:40pm · Keynote · keynote
AI coding tools are overhyped and powerful at the same time. Used well, they're extraordinary. Used badly, they'll bury you in spaghetti code faster than any human team could. The difference isn't the tool. It's the process. After 18 months of teaching developers to build with AI agents, Matt Pocock has watched the same patterns emerge: the devs who succeed aren't the ones who delegate everything or nothing. They're the ones who fall back on engineering fundamentals. In this talk, he shares the iterative process his students use to ship high-quality applications with AI agent swarms, and why the principles that make it work (ubiquitous language, vertical slices, TDD, deep modules) are decades-old ideas that didn't break. They got more important.

### Kitze - Keynote
Speakers: Kitze
Schedule: 5:00-5:20pm · Keynote · keynote
No description published; title, speakers and schedule only.

### Sunil Pai - Keynote
Speakers: Sunil Pai
Schedule: 5:40-6:00pm · Keynote · keynote
No description published; title, speakers and schedule only.

### Software Engineering + AI = ?
Speakers: Gergely Orosz, swyx
Schedule: 4:30-5:00pm · Keynote · keynote
No description published; title, speakers and schedule only.

## April 10
### Running AI Engineer with AI
Speakers: swyx
Schedule: 5:50-6:00pm · Keynote · keynote
No description published; title, speakers and schedule only.

### Gemma, DeepMind's Family of Open Models
Speakers: Omar Sanseviero
Schedule: 9:00-9:20am · Keynote · keynote
Google DeepMind’s Gemma family is expanding. Join us for a deep dive into the latest models of the Gemma ecosystem. From vibe fine-tuning to Sovereign AI, you'll learn about the latest model capabilities, how to build high-performance applications, and how to get started with open models.

### AgentCraft: Putting the Orc in Agent Orchestration
Speakers: Ido Salomon
Schedule: 9:40-9:50am · Keynote · keynote
As we run more agents in parallel, it becomes clear: we are the bottleneck.Luckily, the skills we need for effective multi-agent orchestration aren’t entirely new, they’ve just been hiding in unexpected places.Through AgentCraft, the game-inspired agent orchestrator, I’ll explore how we can raise the ceiling of human-agent collaboration without burning out in the process.

### Building pi in a World of Slop
Speakers: Mario Zechner
Schedule: 9:50-10:10am · Keynote · keynote
All I wanted was a shitty coding agent that is truly mine. And I’d have loved to just tell you why and how I built pi. But then Peter decided to make it the agentic core of OpenClaw. And now pi is collateral. So yes, this is a talk about pi. But it is also a talk about how agents are destroying OSS, how I deal with that, and a plea to slow the fuck down.

### The Future of MCP
Speakers: David Soria Parra
Schedule: 9:20-9:40am · Keynote · keynote
In this Keynote, I will lay out what I believe will be true for agents in 2026 and how MCP plays a part in this. Let's take a look what connectivity for agents might look like.

### Agents need more than a chat
Speakers: Jacob Lauritzen
Schedule: 5:10-5:30pm · Keynote · keynote
No description published; title, speakers and schedule only.

### Fireside Chat with Gergely Orosz and Linear's Tuomas Artman
Speakers: Gergely Orosz, Tuomas Artman
Schedule: 4:30-5:00pm · Keynote · keynote
No description published; title, speakers and schedule only.

### The Friction Is Your Judgment
Speakers: Armin Ronacher, Cristina Poncela Cubeiro
Schedule: 10:10-10:30am · Keynote · keynote
No description published; title, speakers and schedule only.

### What Do Models Still Suck At?
Speakers: Peter Gostev
Schedule: 5:30-5:50pm · Keynote · keynote
What type of real world model responses do users still hate? We get to see millions of user's prompts - and we let users 'dislike both' on the Arena. We'll show you trends and examples of the tasks that LLMs still suck at despite the relentless hillclimbing.

## April 9 — Claws & Personal Agents
### OpenClaw AMA
Speakers: Peter Steinberger, swyx
Schedule: 11:15-11:40am · Fleming · track_keynote
No description published; title, speakers and schedule only.

### Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff
Speakers: Vincent Koc
Schedule: 11:40am-12:00pm · Fleming · talk
When your open-source project hits 320k+ stars and hundreds of daily commits, you stop managing contributions and start engineering the factory itself. I'll share how OpenClaw's team rebuilt around a plugin architecture, modular security boundaries, and a development model where agents and humans ship side by side, and why the real lesson for anyone building AI infrastructure is that process scales harder than code.

### I Gave an AI Agent the Keys to My Life (Here's What Happened)
Speakers: Radek Sienkiewicz
Schedule: 12:00-12:20pm · Fleming · talk
My AI agent reads my email, backs up its own memory and configuration at 2am, monitors its own health, and drafts replies to business proposals. I didn't plan any of this. It happened one permission at a time. This talk is an honest walkthrough of what it actually looks like to live with a personal AI agent running around the clock. Not a demo of what's possible but a story of what happened. I'll cover: - The permission creep timeline: from "read my files" to "handle my communications" over several months - What the agent does at 3am: the real cron ecosystem, what I wake up to, what it produces overnight - How it monitors itself, recovers from failures, updates itselft - The trust that emerged: what it can do without asking, what requires permission, how that boundary gets enforced - Why I gave my agent a personality file that tells it to disagree with me (this helps a lot!) This talk is for anyone building or thinking about building personal AI agents. No theory, no frameworks. Just real lessons from months of running one in production against my actual life. It's still (and always) a work in progress.

### Lobster Trap: OpenClaw in Containers from Local to K8s and Back
Speakers: Sally Ann O'Malley
Schedule: 12:20-12:40pm · Fleming · talk
You’ve spent hours building the right AI agent setup: the right model, the right tools and skills, AGENTS.md with your team’s conventions, and the workflows that actually work. Then your teammates want the same thing. Do you hand them a pile of markdown, config files, and YAML, or do you give them a working baseline? In this demo, I’ll take OpenClaw from a stock local Podman setup to a deployment with a curated agent bundle, then lift that same baseline into Kubernetes. Along the way, I’ll show a pragmatic secret story: Podman secrets for local development, Vault for cluster deployments, and the same agent baseline moving between both. The payoff is simple: your best engineer’s setup just became your team standard. Containers make that setup reproducible, Kubernetes makes it distributable, and “back to local” means the baseline is a starting point, not a cage. Everything runs on a laptop with local containers and a Kind cluster, and you’ll leave with a reproducible tutorial repo.

### Viktor — AI Coworker That Lives in Slack
Speakers: Fryderyk Wiatrowski
Schedule: 3:10-3:30pm · Fleming · talk
No description published; title, speakers and schedule only.

### Open-Source Agents Ecosystem
Speakers: Merve Noyan
Schedule: 2:50-3:10pm · Fleming · talk
In this session I will talk about anything and everything open-source around open agents and tools. We will not only touch on agentic coding, but also vision language agents, building gaming environments and agent fine-tuning!

### Claws Out: Securing and Building with OpenClaw
Speakers: Nick Taylor
Schedule: 12:40-1:00pm · Fleming · talk
Running OpenClaw without hardening access to it is a bad idea. We'll cover how I secured my OpenClaw, McClaw, contributed trusted-proxy auth mode to the OpenClaw project, and how I use it to build tools. We're going to build something live during the talk using OpenClaw, the same way I built Clawspace, a browser-based file explorer/editor for your OpenClaw workspace. feat(gateway): add trusted-proxy auth modegiithub.com/nickytonline/clawspace, a browser-based file explorer/editor for an OpenClaw workspace.github.com/pomerium/pomerium, an open core Identity-Aware Proxy

### Scaling Agents on Kubernetes with acpx and ACP
Speakers: Onur Solmaz
Schedule: 2:30-2:50pm · Fleming · talk
What happens when you stop using one coding agent at a time and start running dozens in parallel on Kubernetes? Onur Solmaz, maintainer of OpenClaw and creator of acpx, walks through the architecture behind massively parallel PR triage and bug fixing using disposable agent pods. He introduces acpx — a headless CLI client for the Agent Client Protocol (ACP) — and shows how it replaces brittle PTY scraping with structured, protocol-driven communication between agents. The talk covers how ACP enables harness interoperability in OpenClaw, letting users drive Claude Code, Codex, and other coding agents through a single unified interface — whether from a terminal, Telegram, or Discord. Expect a live demo of agentic workflows orchestrated through acpx v0.4's node-based graph system, where deterministic steps drive multiple coding agents through routine engineering tasks at scale.

## April 9 — Harness Engineering
### OpenAI Symphony & Harness Engineering AMA
Speakers: Ryan Lopopolo, Vibhu Sapra
Schedule: 11:15-11:40am · Westminster · track_keynote
No description published; title, speakers and schedule only.

### Building the Justice AI Unit: Shipping Production AI Inside Government
Speakers: William Tarr
Schedule: 12:40-1:00pm · Westminster · talk
Building the Justice AI Unit (https://ai.justice.gov.uk/) — forward-deployed engineers, entrepreneurial model, shipping production AI every day, but inside government.

### What the Best Agents Share
Speakers: Mardu Swanepoel
Schedule: 12:00-12:10pm · Westminster · lightning
What do AI agents from Harvey, Cursor, Manus, and Anthropic have in common despite serving drastically different domains? They all incorporate 4 core patterns that support user trust and adoption, whether in high-stakes environments like law and engineering or everyday workflows. In this session we'll explore these four core patterns to better understand what each entails, when to apply each, and how they drive impact. We'll examine specific examples from Harvey, Cursor, Manus, and Claude Cowork to see how each company applies these patterns and what tangible outcomes they deliver for usage and adoption.

### Why (Senior) Engineers Struggle to Build AI Agents
Speakers: Philipp Schmid
Schedule: 12:10-12:20pm · Westminster · lightning
No description published; title, speakers and schedule only.

### Building a Chess Coach
Speakers: Anant Dole, Asbjørn Steinskog
Schedule: 12:20-12:40pm · Westminster · talk
Take Take Take is the chess app founded by World Champion Magnus Carlsen. Our goal is to turn play into progress by helping players better understand their games.In this talk, we will share how we built Game Review, a feature that explains what happened in your games and surfaces meaningful playing stats after every game. The challenge is that LLMs can communicate clearly, but they cannot reliably explain chess on their own. We built a system that combines chess engine analysis with tactical and positional detectors that extract chess concepts, while the LLM turns those signals into clear, useful coaching.We will cover the pipeline behind Game Review, including Stockfish evaluations, concept extraction, prompt design, and how we use chess-aware skills and evals to iterate on the system. We will share a short live demo and practical patterns for consumer AI teams building AI features.

### Agents on the Canvas in tldraw
Speakers: Steve Ruiz
Schedule: 11:40am-12:00pm · Westminster · talk
At tldraw, we've been bringing agents to our infinite canvas. In December 2025, we ran a one-month experiment named Fairydraw where users could work with three fairies—virtual collaborators who work with you, with your human collaborators, and coordinate together on large tasks. Learn what we learned.

### Why Your AI UX Is Broken (and It's Not the Model's Fault)
Speakers: Mike Christensen
Schedule: 2:50-3:10pm · Westminster · talk
AI interfaces are moving fast. The single-shot prompt box is already feeling dated. The products pulling ahead let users steer responses mid-stream, interrupt and redirect when the agent goes off track, pick up conversations across devices, send follow-up messages without waiting for the current response to finish, and hand off seamlessly between AI and human support. These aren't speculative features. They're already shipping in the best AI products, and users are starting to expect them everywhere. Building these experiences is hard, and not for the reasons you might think. The problem is not model intelligence or agent capabilities. It is that most AI sessions are ephemeral, tied to a single connection, device, or agent instance. Most AI apps stream responses over HTTP or SSE, a one way pipe from server to client tied to a single connection. That works for streaming a single response to a single client on a single device. But the moment you want to interrupt a response, resume after a disconnect, or sync across devices, you are fighting the transport at every step. A user switches tabs, refreshes the page, or hits a network blip, and the in-progress response disappears. Teams end up building their own fragile plumbing - message buffering, replay logic, and state recovery - instead of shipping their actual product. As teams push the limits of AI UX, a pattern is starting to emerge. The most advanced AI products treat the session itself as a durable, shared resource, independent of any single connection, device, or agent instance. Connections break. Devices come and go. The session persists, and anyone who joins catches up automatically. This is what durable execution did for backend workflows. A similar shift is now happening at the experience layer. This talk explores the UX capabilities defining the next generation of AI products: resumable streaming, live steering and interruption, multi-device continuity, concurrent interactions, and human-in-the-loop handoff. I will show how leading AI products use durable sessions to enable these experiences - with demos built on real code. You will walk away with a clear picture of the UX bar being set right now, and practical patterns for building these experiences, regardless of which model, framework, or infrastructure you use.

### The Production AI Playbook: Deploying Agents at Enterprise Scale
Speakers: Sandipan Bhaumik
Schedule: 3:10-3:30pm · Westminster · talk
Every AI engineer knows the demo-to-production gap. Few cross it systematically. This workshop reveals playbook for taking agents from "it works!" to production systems generating measurable value. You'll build three artifacts: an evaluation framework for your use case, a production readiness assessment, and a 90-day deployment plan. We'll cover the Production AI Program's five pillars separating POCs from production, hands-on evaluation design using your actual project, and multi-agent orchestration patterns. No vendor pitches—just frameworks from deploying agents in financial services, healthcare, and enterprise environments where failure costs millions.

### Harnesses in AI: A Deep Dive
Speakers: Tejas Kumar
Schedule: 2:30-2:50pm · Westminster · talk
No description published; title, speakers and schedule only.

## April 9 — Voice & Vision
### Beyond Transcription: Building Voice AI That Actually Understands Conversations
Speakers: Hervé Bredin
Schedule: 11:15-11:40am · Abbey · track_keynote
Most Voice AI pipelines stop at transcription. That's the wrong place to stop. Without knowing who's speaking, when they spoke, and how turns relate to each other, even the best STT model produces output that downstream LLMs can't reliably use. This talk covers what's missing in most Voice AI stacks: speaker diarization, conversation structure, and context-aware processing. Hervé will show why raw transcripts fail in real-world scenarios: multi-speaker calls, interruptions, overlapping speech, and what it takes to build a pipeline that performs at production quality.

### Mainstream TTS model architecture
Speakers: Samuel Humeau
Schedule: 11:40am-12:00pm · Abbey · talk
This talk is directed at builders who want an insight on how TTS model operate, how they can stream audio and clone voices. It will discuss about the dominant architectural pattern in TTS in 2026, taking Mistral's latest released TTS as an example.

### What's new in AI Audio?
Speakers: Thor Schaeff
Schedule: 3:10-3:30pm · Abbey · talk
A look at the latest updates on AI Audio from the Google DeepMind team. We'll be looking at the latest capabilities in audio understanding, speech generation, real-time multimodal agents, and music generation.

### How Transformers Finally Ate Vision
Speakers: Isaac Robinson
Schedule: 12:00-12:20pm · Abbey · talk
Transformers have dominated language for years. Vision transformers were introduced in 2020. But only now are transformers beating CNNs in vision approaches. Why gives? We'll discuss why transformer-based architectures are, only now, beating prior approaches in vision. We'll use RF-DETR, the first realtime instance segmentation transformer that beats CNNs like ResNet and YOLO for object detection and instance segmentation introduced in 2025, as example. Learn what's coming in for VLMs, "physical AI," and VLAs.

### Give Your Chat Agent a Voice
Speakers: Luke Harries
Schedule: 12:40-1:00pm · Abbey · talk
No description published; title, speakers and schedule only.

### You can't just one shot it
Speakers: Mehedi Hassan
Schedule: 2:50-3:10pm · Abbey · talk
No description published; title, speakers and schedule only.

### Neil Zeghidour - Voice AI: when is the "Her" moment?
Speakers: Neil Zeghidour
Schedule: 2:30-2:50pm · Abbey · talk
As natural language becomes our primary interface with machines, voice is having a moment, from customer support to NPCs to “voicecoding.” Yet it’s still far from truly human. We’ll look back at how voice AI has evolved, the technical hurdles ahead, and where we’re taking the field to.

## April 9 — Evals & Observability
### Why building eval platforms is hard
Speakers: Phil Hetzel
Schedule: 11:15-11:40am · Moore · track_keynote
An eval platform is not just a test runner. You are building shared definitions of "good," reliable data pipelines, labelling workflows, versioning, and trust in results across many teams and model changes. This session breaks down the hidden complexity, the common failure modes, and the design principles that make evals credible and usable in day-to-day engineering.

### LLM codegen fails and how to stop 'em
Speakers: Danilo Campos
Schedule: 11:40am-12:00pm · Moore · talk
Let's talk about the most common pitfalls of generating code with autonomous LLM agents, and the strategies we use to erase them altogether. This is battle-tested wisdom from a system operating at scale, earning constant accolades. But you can absolutely match our performance, as long as you've got the playbook. Here's the story: The PostHog wizard helps over 5,000 users monthly to integrate our tools into their project code, giving them the best possible start on their journey into product engineering. From a brand perspective, this is a high-risk, high-reward exercise: if our LLM code generation is bad or stupid, *we* look bad AND stupid. But if it works, we look like miracle workers who protect our customers' time. Good news: it works really well. Why? Because we've isolated multiple categories of failure modes for LLM tools, and designed strategies over hundreds of carefully-observed iterations to mitigate them. I'll walk you through the failure modes, and the path to maximal correctness.

### Skill issue: Lessons from skilling up coding agents to use Langfuse
Speakers: Marc Klingen
Schedule: 12:20-12:40pm · Moore · talk
We built a Langfuse Skill, a reusable capability that enables coding agents to implement Langfuse tracing, prompt management and more autonomously. In this talk, we share our journey from a simple baseline all the way to attempting a full auto-research/improvement loop, powered by the very traces the Skill generates. The core insight: you can't improve what you don't trace and the Langfuse Skill is the proof of concept. We share honest learnings from what worked, what didn't, and what it reveals about the future of Skills as a foundation for scalable, self-improving agents.

### The Art & Science of Benchmarking Agents
Speakers: Vincent Chen
Schedule: 12:40-1:00pm · Moore · talk
Our ability to measure AI has been outpaced by our ability to develop it, and this eval gap is one of the most important problems in AI. We need more enduring benchmarks to close this gap, and consequently advance entire new vectors of capabilities for the field. In this talk, I'll share our learnings evaluating agents, drawing from experience working with nearly all global frontier labs and leading academics. We'll discuss the science (i.e., mechanics that make benchmarks rigorous and effective) and art (i.e., intangibles driving ambitious and enduring benchmarks) of building great benchmarks. I'll close by sharing some of the learnings from Open Benchmarks Grants— a $3M initiative in partnership with Hugging Face, Together AI, Prime Intellect, Factory, and others— and highlighting some of the projects we're most excited about funding.

### Evals Are Broken, Use Them Anyway
Speakers: Ara Khan
Schedule: 2:30-2:50pm · Moore · talk
This talk explains why I went from "evals are useless" to using them as a core part of my agent improvement loop. I share practical heuristics for interpreting, running, and creating evals, and why doing them anyway is better than pure "vibes".

### Self Driving Products: Engineering the Pipeline from Product Signals to Pull Requests
Speakers: Joshua Snyder
Schedule: 2:50-3:10pm · Moore · talk
Every product generates a firehose of signals; users rage-clicking through broken flows, error spikes at 2am, experiments that quietly tank a metric, a customer complaining in Slack. Today, a human has to notice, triage and eventually write the fix. We're building a system at PostHog that automatically collapses that entire chain. I'll cover how we ingest and normalize signals across very different sources; session replays, error tracking, analytics, logs, experiments, and third-party tools like Slack. How we convert noisy, unstructured signals into well-scoped coding tasks with enough context for an agent to act on. How we orchestrate agents against real codebases, run them in secure sandboxed environments, and decide what's worth shipping.

### SWE-rebench: Lessons from Evaluating Coding Agents on Real Software Engineering Tasks
Speakers: Ibragim Badertdinov
Schedule: 3:10-3:30pm · Moore · talk
Coding agents are evolving fast, and simple vibe checks are no longer enough to evaluate them. In this talk, I will share how we built the SWE-rebench leaderboard, which we update every month with fresh, real-world software engineering tasks and use to evaluate 30+ leading open and closed models. I will also share practical lessons on how to build your own benchmark, along with common ways models can cheat during evaluation.

### Everything I Learned Training Frontier Small Models
Speakers: Maxime Labonne
Schedule: 12:00-12:20pm · Moore · talk
A new class of small models is emerging with the ability to reliably follow instructions and call tools while running on-device under 1 GB of memory. In this talk, we'll break down how to post-train frontier small models using the LFM2.5 recipe: on-policy preference alignment, agentic reinforcement learning, and curriculum training with iterative model merging. We'll cover training challenges unique to the 1B scale, like doom loops, capability interference, and how to fix them. The goal is to give you a concrete playbook to fine-tune and deploy small models for your own use cases, from structured data extraction to multi-turn tool use.

## April 9 — Context Engineering
### One Developer, Two Dozen Agents, Zero Alignment: Why we Need Collaborative AI Engineering
Speakers: Maggie Appleton
Schedule: 11:15-11:40am · St. James · track_keynote
Agentic engineering so far has been a solo story: one developer and a dozen agents moving at warp speed. But speed without thoughtful planning and team alignment is just wasting tokens. When everyone on a team is directing agents alone in their personal CLI tools with no shared context, you get duplicate work, conflicting changes, poorly-designed solutions, surprise features nobody else agreed to build, and everyone pulling in different directions. Serious software still requires serious collaboration. You need multiple perspectives and types of expertise to build great things. We need agentic environments where people can plan together, think critically together, and share the same context. In this talk I'll demo how we've tackled these design problems in Ace, a multiplayer agent environment from GitHub Next that uses real-time collaboration, proactive agents, and sandboxed micro VMs for rapid prototyping and exploration.

### Teaching Coding Agents to do Spreadsheets
Speakers: Nuno Campos
Schedule: 11:40am-12:00pm · St. James · talk
Full content available here https://github.com/witanlabs/research-log

### Hierarchical Memory: Context Management in Agents
Speakers: Sally-Ann Delucia
Schedule: 12:00-12:20pm · St. James · talk
An emerging pattern is clear: the best agent memory systems aren't built top-down; they emerge bottom-up from composable primitives. Whether it's grep piping to sort, table previews pointing to full spans, or databases feeding file systems, the winning architecture is always a hierarchy of tools that agents can chain together. The Unix philosophy – small, focused tools that do one thing well and compose infinitely – turns out to be exactly what LLMs need to make 200k tokens feel like 200 trillion. Fifty years later, the lessons still hold: make memory feel infinite by making it hierarchical, and make it hierarchical by making it composable. In this presentation, we’ll outline new findings/data on AI memory from working on thousands of deployed agents.

### Personalization in the Era of LLMs
Speakers: Shivam Verma
Schedule: 12:20-12:40pm · St. James · talk
Streaming platforms serve hundreds of millions of users across a catalog of 100M+ items that changes daily. Classical recommender systems rank well but can't explain, converse, or generalize across surfaces. LLMs can — but they don't know your catalog, and they definitely don't know your user. In this talk, I'll walk through how we bridge that gap at Spotify: teaching open-weight LLMs to be catalog-aware and user-aware without full fine-tuning. I'll cover three building blocks: (1) learned user representations that transfer across search, and recommendation; (2) Semantic IDs — discrete token sequences that let generative models reason over catalog entities the way they reason over words; and (3) parameter-efficient conditioning methods that inject user context into frozen LLMs — from single-token to multi-token projections that give the model a richer "user prompt" to attend over. I'll share what actually worked, what didn't, and the engineering tradeoffs of serving personalized LLMs at web scale.

### What Breaks When You Build AI Under Sovereignty Constraints
Speakers: Bilge Yücel
Schedule: 12:40-1:00pm · St. James · talk
Regulatory and jurisdictional constraints are no longer an edge case in AI system design; they now shape architectural decisions as much as model quality does. From European efforts like “Eurostack” to sovereign cloud offerings by hyperscalers, sovereignty is becoming a practical engineering constraint, pushing teams to design systems that operate within defined boundaries. What changes when your AI system can’t send data outside a region, rely on external APIs, or depend on infrastructure you don’t control? More importantly, what breaks? This talk explores sovereign AI as a system design problem, focusing on the hidden assumptions in modern AI architectures that fail under real-world constraints. Many production systems rely on external dependencies, from embedding APIs to evaluation tools, that make them difficult to audit, reproduce, or control. We’ll examine what breaks in these architectures and how sovereignty requirements reshape core design decisions: where models run, how data flows, and how systems remain observable, auditable, and replaceable. To make this concrete, we’ll walk through a reference architecture using an open, modular orchestration approach (with Haystack as an example), and show how to:design pipelines that run across cloud, on-prem, and hybrid environmentsswap models without redesigning the systemkeep sensitive data local while integrating external capabilities when allowedmaintain full visibility into data flow and system behaviorThe focus is on building systems that remain flexible under constraints with replaceable components, explicit data flows, and control staying within your boundary.

### Connecting the Dots with Context Graphs
Speakers: Stephen Chin
Schedule: 2:30-2:50pm · St. James · talk
AI systems need more than intelligence; they need context that persists. Without it, even strong models can misinterpret information, lose decision rationale, or repeat the same mistakes. Context Graphs have emerged as a practical pattern for agentic AI: a living graph that captures not only what was retrieved or known, but how context led to actions through tool calls, constraints, policies, and outcomes, stitched across entities and time so precedent becomes searchable. This talk explores context engineering as the discipline of designing that context layer, and shows how context graphs complement retrieval by enabling multi-hop, structured context assembly (building on GraphRAG-style hierarchical summaries) while improving explainability and evaluation. Attendees will leave with a practical understanding of how to build context pipelines that combine contextual retrieval with persistent memory and provenance, and why context graphs are becoming central to trustworthy, enterprise-ready AI systems.

### Context Graphs for Explainable, Decision-Aware AI Agents
Speakers: Andreas Kollegger, Zaid Zaim
Schedule: 2:50-3:10pm · St. James · talk
AI agents can follow prompts and use tools, but often lack the institutional context needed to explain why a decision is made. That reasoning: policies, precedents, and past outcomes are usually scattered across systems and human memory. Context graphs capture this missing layer by modeling decision traces over time, including causality and context. By giving agents access to just enough historical and organizational knowledge, context graphs enable more explainable, consistent, and auditable decisions.

### Combine Skills and MCP to Close the Context Gap
Speakers: Pedro Rodrigues
Schedule: 3:10-3:30pm · St. James · talk
Agents don’t fail because they’re weak — they fail because they lack the right context. Even when working with something as well-known as PostgreSQL, agents regularly produce insecure queries, inefficient patterns, or incorrect migrations. Not because they can’t reason, but because their knowledge is outdated, generic, or misaligned with the specific environment they’re operating in. In this talk, we explore how Agent Skills and MCP work together to close that gap. Using real-world Postgres workflows — from writing secure RLS policies to debugging slow queries and fixing broken migrations — we’ll show what actually breaks when agents operate without structured context, and what changes when you introduce the right abstractions. MCP provides the safe, auditable interface to interact with the system, while Agent Skills inject domain-specific guidance tailored to the actual environment, including Supabase-specific patterns and constraints. But the results aren’t as straightforward as “more context = better agents.” We’ll share findings from our internal benchmarks comparing agent performance across different setups, showing that Skills don’t replace MCP — they amplify it — and that poorly designed or untested Skills can have little impact or even degrade performance. We’ll also dig into how we structure Skills for real systems (not just isolated tasks), and how we use evals to measure their impact across realistic workflows. You’ll see how different combinations of Skills, MCP, and CLI-based interaction affect agent behavior, reliability, and outcomes. Because once agents touch production systems like Postgres, the problem isn’t intelligence — it’s having the right context, delivered in the right way.

## April 10 — AI Architects
### The Domain-Native AI Organization: How to Leverage Domain Expertise
Speakers: Chris Lovejoy
Schedule: 12:20-12:40pm · Westminster · talk
Vertical AI is a multi-trillion-dollar opportunity. But you can't win by grabbing the latest LLMs off-the-shelf: you need to embed domain expertise into your organisation, and use it to build a domain-native application. Most teams get this wrong: they either don't hire the right domain experts or don't leverage them correctly to build a differentiated product. In this talk, I'll share a framework for building a domain-native AI organisation, drawing on case studies from healthcare, productivity, and legal. I'll share: three models for embedding domain expertise (the Oracle, the Evaluator, and the Architect) - and how to choose which fits your stage and use case who to hire and how to evolve their role over time the most common org-building failure modes (and how to avoid them)

### Rewiring the State
Speakers: Eoin Mulgrew
Schedule: 11:40am-12:00pm · Westminster · talk
In No10 we're building what should be one of the most elite technical teams of any central government. We are taking engineers and devs from AI labs, big tech, YC founder etc. and deploying them to rewire the UK state. This session would include demos and act as a call to arms for people to join us.

### Context Is the New Code
Speakers: Patrick Debois
Schedule: 11:15-11:40am · Westminster · track_keynote
We version control code, review it, test it, and observe it in production. We spent two decades building rigorous lifecycles around it. Now look at how we treat the context that drives AI coding agents: rules files copy-pasted from blog posts, prompts edited by hand, memory nobody audits. We’re in the cowboy coding era of context. If context is the primary lever determining what agents produce, it deserves the same engineering rigor we give code. The Context Development Lifecycle (Generate, Evaluate, Distribute, Observe) gives us the stages. The process practices wrap around it: version control, peer review, CI/CD pipelines, and the team workflows to make context a shared engineering responsibility. Then there’s the bigger picture: the context flywheel. As agents consume context and produce results, every observation feeds back into better context, which produces better results. The teams that get this loop spinning build a compounding advantage that becomes their moat. This is not a solved problem. It’s a journey we’ve already started, and if the DevOps transition taught us anything, the teams that figure out the lifecycle first will pull ahead fast.

### Most Enterprise Agentic Projects Are Doomed — Here’s Why
Speakers: Jess Grogan-Avignon, Jack Wang
Schedule: 12:00-12:20pm · Westminster · talk
Explore real-life blood and tears in agentic delivery experience for large enterprises, where most of the normal people live and breath outside of Silicon Valley.

### CI/CD Is Dead, Agents Need Continuous Compute and Computers
Speakers: Hugo Santos, Madison Faulkner
Schedule: 12:40-1:00pm · Westminster · talk
What happens when thousands of agents try to edit source code at once? Merge chaos, slow builds, and stacks of pull requests for engineers to review. While agentic software development has never been so promising, traditional CI/CD solutions threaten to constrain the agentic software transformation. In this session, we’ll unpack what happens when autonomous coding agents continuously open PRs, modify infrastructure, and trigger workflows across hundreds of repos: traditional CI/CD systems, tuned for infrequent human changes, become the latency and cost bottleneck in the SDLC. We’ll discuss concrete failure modes including runner saturation, cache thrash, cold Docker builds, test explosion, and opaque flakiness and show why treating CI/CD as a high-performance system (with specialized hardware, incremental execution, and fine-grained observability) is now a core AI infra problem, not a DevOps afterthought. Using Namespace as a case study, we’ll go deep on how to architect an agent-ready pipeline layer: intelligent execution over GitHub Actions, remote caching and Turbo-style Docker builds, Git-aware incrementality, and workflow analytics that tie time and spend directly to specific jobs, repos, and agents. We’ll also cover operational requirements including ephemeral, high-performance clusters; private registries optimized for build workloads; and interactive debugging for both human and agent-authored changes—and how these design choices emerged from running microservices-scale infra at Google and beyond. Attendees will leave with a concrete blueprint for turning CI/CD into a throughput- and reliability-optimized substrate that can safely sustain 5–10x more changes from humans and agents without blowing up latency or cloud budgets.

### Software Engineering Is Becoming Plan and Review
Speakers: Louis Knight-Webb
Schedule: 2:30-2:50pm · Westminster · talk
AI eats the middle, software engineers are spending all their time planning and reviewing the work of AI. If all humans are going to do is plan and review the work of AI, the biggest lever you have to ship more is to speed up planning and review. And some examples of how teams and individuals are adapting: - What tools are people spending their time in - How much time are teams spending reviewing code, how has this changed since AI - What are different approaches to planning work - Is agile and scrum dead? Are most product teams moving faster

### How Building with AI Can Double the Throughput of Your Engineering Team
Speakers: Brian Scanlan
Schedule: 2:50-3:10pm · Westminster · talk
In 2025, Intercom took on an ambitious goal to double the throughput of their engineering team by going beyond building fancy demos, and instead taking advantage of AI tooling to get real features and large existing SaaS codebase into the hands of paying customers. While this transformation is still a work in progress, Intercom's pace of innovation has always been a competitive strength. In this talk Brian will share his lessons and learnings when building with AI agents – what has and hasn't worked when faced with scaling towards 2x productivity

### Agents Don't Do Standups: Building the Post-Engineer Engineering Org
Speakers: Mike Spitz
Schedule: 3:10-3:30pm · Westminster · talk
For decades our engineering organisations have run on the same ritutals designed for engineers. Standups, sprint planning/refinement, retros. What happens when humans are no longer the ones a company needs to cater for but agents? We did a simple thought exercise at PFF, what happens when we stop asking "how do we help engineers output more?" and started asking "how can we make the agents faster?". Over the last few months, we dismantled our entire development lifecycle — CI/CD, code review, architecture, deployment and rebuilt it around agent-first principles. Our results speak for ourselves: 10x developer output, deploy cycles compressed from 5 days to multiple shipments per day, and customer satisfaction scores of 79%. This talk is a field report from the post-engineer engineering org. I'll cover the framework we used to decide what to hand to agents, the guardrail architecture that replaced human review gates (layered agent evaluation, agent-on-agent review, and tiered human-in-the-loop for high-risk only), and the uncomfortable truth about what happened to team size. Scrum didn't survive. Neither did most of the processes you're running today. I'll share exactly what replaced them, and the concrete metrics that prove it works. This is a framework that should inspire conversation on what needs to change at companies struggling to understand how to adopt AI in the new engineering world. You'll leave with an opinionated, practical playbook: how to evaluate your own pipelines for agent-first redesign, what guardrail patterns actually work in production, and why the biggest mistake you can make right now is moving too slowly.

## April 9 — Leadership Lunch
### Leadership Lunch
Speakers: swyx, Igor Karpovich
Schedule: 1:00-2:00pm · Keynote · keynote
Leadership Addon and Max attendees: Moderated by swyx. swyx will facilitate the discussion with Igor Karpovich on Skyscanner's journey making agentic development work at scale, followed by peer-to-peer chats with leadership attendees.

## April 10 — Generative Media
### Think You Can Build a Game with AI? Think Again! The New Games Are Just Being Invented!
Speakers: Danielle An, David Hoe
Schedule: 12:40-1:00pm · Moore · talk
With the recent development of AI, either you or your friend probably vibe coded a game using Gemini, on Three.js. But that is old news now. If everyone can do that, what is next? The next massive hit, the one that millions of people across the world will play, is just about to be born. Wanna know more? Come see this talk!

### Bounded Autonomy: Between Free Will and Determinism
Speakers: Angus J. McLean
Schedule: 12:20-12:40pm · Moore · talk
In the world of AI engineering, it always feels like the ground is moving underneath your feet. Every few weeks, a new concept, tool, or framework is released, forcing you to rethink your entire stack.Everything around us has changed, and yet, to most of us, it all feels strangely familiar. Increasingly we are seeing a move away from higher level orchestration, and a return to underlying principles, not just of LLMs, but of the operating system itself. Because, in many ways, there are only two things we can really change: the prompt and the context.As systems become more intelligent, the way we design them starts to shift. As human and machine converge, philosophy starts to matter more than control or implementation.

### Black Forest Labs: FLUX, Open Research, and the Future of Visual AI
Speakers: Stephen Batifol
Schedule: 11:15-11:40am · Moore · track_keynote
Black Forest Labs started with FLUX.1 - the open-weights image model that changed what people could do - and hasn't slowed down since. FLUX.1 Kontext, FLUX.2, FLUX.2 Klein. Each release pushed the frontier further, each one shipped in the open.This talk traces that arc, pulls back the curtain on the research happening behind the scenes, and gets into where BFL is actually going: building the standard for visual intelligence. Not better image generators - models that understand and simulate the physical world. Multimodal by design, everything in, everything out. The foundation for generative UIs, simulation, and agents that reason over the physical world.BFL's moat is velocity. They own the full stack from research to API, ship faster than anyone, and do it in the open. This talk is about how - and what comes next.

### MLX Genmedia
Speakers: Prince Canuma
Schedule: 11:40am-12:00pm · Moore · talk
No description published; title, speakers and schedule only.

### What is state-of-the-art AI model?
Speakers: Bertrand Charpentier
Schedule: 12:00-12:20pm · Moore · talk
No description published; title, speakers and schedule only.

## April 9 — Google DeepMind/Gemini
### The agent-ready web: Simplify user actions with WebMCP
Speakers: Tara Agyemang
Schedule: 11:15-11:40am · Rutherford · talk
No description published; title, speakers and schedule only.

### AI on Android: Ask me Anything
Speakers: Florina Muntenescu, Oli Gaymond
Schedule: 12:20pm-12:40pm · Rutherford · talk
No description published; title, speakers and schedule only.

### Agentic Evaluations at Scale — For Everybody
Speakers: Nicholas Kang, Michael Aaron
Schedule: 12:00-12:20pm · Rutherford · talk
AI evaluations today are broken. They're decentralized, opaque, and in the hands of a few. But AI should benefit all of humanity, and therefore evals should reflect the diversity of work that AI needs to undertake - and be transparent and reproducible so we can trust them. Join us as we talk about how we're trying to solve these issues and the problems we're facing.

### Build & deploy AI-powered apps
Speakers: Paige Bailey
Schedule: 11:40-12:00pm · Rutherford · talk
Got a massive idea but stuck in the "just talking about it" phase? Let’s fix that. In this session, we’re cutting the fluff and diving straight into how to actually build and prototype at lightning speed using AI Studio Build and Antigravity - for 100% free. We’ll be breaking down Google DeepMind's AI tech stack so you know exactly what tools to grab. You'll learn when to use heavyweights like Gemini 3.1 Pro or the brand-new Gemma 4 (huge shoutout to it being fully open and Apache 2.0 licensed 🔓), and when to keep things hyper-fast with Gemini 3 Flash and Flash-Lite. Plus, we’ll be messing around with Veo 3.1 Lite for video generation, NanoBanana 2, Lyria 3 for music generation, Genie 3 for world model building, and OpenClaw with Gemini to see what happens when you really push the limits of your prototypes. TL;DR: basically zero slides, more shipping. I'll be running live demos to show you how to take your side quests from "just an idea" to a fully working prototype, show you how to add new features to existing codebases, and we'll save time for a live Q&A to troubleshoot your builds and ideas. Let's build! 🚀

### TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM
Speakers: Cormac Brick
Schedule: 12:40-1:00pm · Rutherford · talk
No description published; title, speakers and schedule only.

### Sovereign Escape Velocity: AI Ownership with Open Models
Speakers: Ian Ballantyne, Gus Martins
Schedule: 2:30-2:50pm · Rutherford · talk
No description published; title, speakers and schedule only.

### Any-to-Any: Building Native Multimodal Agents
Speakers: Patrick Löber
Schedule: 2:50-3:10pm · Rutherford · talk
No description published; title, speakers and schedule only.

### Text Diffusion
Speakers: Brendon Dillon
Schedule: 3:10-3:30pm · Rutherford · talk
No description published; title, speakers and schedule only.

## April 10 — Coding Agents
### Replacing 12K LoC with a 200 LoC Skill
Speakers: David Gomes
Schedule: 11:15-11:40am · Fleming · track_keynote
TODO

### A Piece of PI – Embedding The OpenClaw Coding Agent In Your Product
Speakers: Matthias Luebken
Schedule: 11:40am-12:00pm · Fleming · talk
When people use OpenClaw, they're amazed. It auto-discovers new capabilities, explores available data sources, stitches components together, and dynamically builds new solutions. It feels like the system is learning. It feels magical. At its core, OpenClaw is powered by pi.dev: a deliberately simple coding agent built on a small set of powerful primitives. PI's "radical extensibility" turns out to be a strong architectural fit for the kinds of composable, evolving use cases OpenClaw is designed to support. In this talk, we'll take a closer look at what's actually happening under the hood at the agent layer. This session is aimed at a technically curious audience — especially those who want to look beyond the surface and consider working with OpenClaw seriously.

### Fast Models Need Slow Developers
Speakers: Sarah Chieng
Schedule: 12:00-12:20pm · Fleming · talk
In the past few years, we've developed a series of 'bad habits' as a consequence of slow AI code generation. We write huge prompts, generate massive code diffs, or create 10 parallel sessions because each response takes so long. Codex Spark represents a genuine paradigm shift in AI capabilities and use cases: 1,200+ tokens/second enables real-time collaboration that requires a new approach to work. This talk is a practical playbook for working in this new regime, where the AI is faster than we can keep up with.

### Lawrence Jones - Fighting AI with AI
Speakers: Lawrence Jones
Schedule: 12:20-12:40pm · Fleming · talk
At incident.io we're building AI SRE: a system that investigates production incidents autonomously, digging through logs, metrics, traces and code changes to tell you what's gone wrong and how to fix it. It's one of the most complex AI products out there: a deeply nested tree of agents, extremely ambiguous problems, integrating with nondeterministic telemetry systems. When something breaks, you can't just look at a prompt and its output — you need to trace through the entire chain to find where reasoning went sideways. Our answer to this complexity has been to fight AI with AI — building internal tools where AI agents help us understand, debug, and improve our own AI systems. This talk walks through the specific tools and workflows we've built: Evals that actually work: a CLI and red-green runbook that turns "this interaction went wrong" into a proven fix, structured so AI agents can follow the process end-to-end Filesystem downloads: serialising complex agent traces as markdown that AI agents can read and reason about, turning hour-long debugging sessions into 5-minute conversations Analysis at scale: a pipeline where 25 parallel AI agents each analyse an investigation, then cluster results to surface systemic patterns across a customer's incidents AI-powered feedback loops: using AI agents to dogfood our own tools, submitting structured feedback that feeds directly into what we build next None of this requires exotic infrastructure. The patterns are straightforward: give AI agents access to the same debugging information your engineers use, but in a format they can read. Write runbooks they can follow. Build pipelines where AI does the repetitive analysis and surfaces the patterns for humans to act on. If you're building AI products and finding the complexity is outpacing your ability to debug and improve them, this talk will give you concrete strategies to close that gap.

### Your Coding Agent Should Do AI System Engineering
Speakers: Ben Burtenshaw
Schedule: 2:30-2:50pm · Fleming · talk
We gave Claude Code, Codex, and Gemini CLI the ability to build CUDA kernels, fine-tune models, and run full ML experiments. The results were real speedups and performance boosts. An agent-written RMSNorm kernels hit 1.88x speedups on H100s. Fine-tuned Qwen3-0.6B hit 35% on livecodebench. Hugging Face teams are now running 1,000+ ML experiments daily without writing training scripts. This talk is a live walkthrough of where Hugging Face has integrated agent skills into the ML stack, so that agentic coders can go deeper than ever. I'll demo the full loop: giving an agent a task it can't do, watching it fail, loading a skill, and watching it produce a kernel that beats PyTorch's native implementation. I'll share benchmarks across six models on kernel writing, show where agents still fail badly, and give you a concrete playbook for using skills to tackle the hardest systems problems in AI engineering today. I'll briefly highlight the practical tools that we're using to build skills and release agents on the Hub. But the real takeaway isn't the tools. It's what this means for your career as an engineer, and/or engineering team you lead. CUDA programming, ML training pipelines, RL alignment, these were deep specializations that took years to develop. Agent skills compress that timeline from years to hours. Leave with: the open-source skill files, the upskill CLI, and a framework for knowing when to trust (and when to verify) your agent on hard systems tasks.

### Let’s Talk About FOMAT – Fear of Missing Agent Time
Speakers: Michael Richman
Schedule: 2:50-3:10pm · Fleming · talk
You know FOMO – you also know FOMAT, you just didn’t have a name for it. Fear of Missing Agent Time. That nagging suspicion that the agent you kicked off 30 minutes ago is sitting there blocked, waiting for your input, while you’re off grabbing coffee. We want our agents working and unblocked around the clock, but today we’re still chained to our desks to keep them humming along. This talk introduces Cmd+Ctrl – a system that lets you unblock, monitor, and launch coding sessions from your phone, from your watch, from anywhere. Live demo included. Cmd+Ctrl is coding tool agnostic – it works with Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, OpenCode, and more.

### Cooking with Agents in VS Code
Speakers: Liam Hampton
Schedule: 3:10-3:30pm · Fleming · talk
This is a demo driven talk that explores how AI agents are shaping modern developer workflows inside VS Code. This session introduces attendees to local, remote, and worktree based agents, explaining how each agent path works, the trade offs involved, and when to use each of them effectively. Attendees will leave with a clear mental model for agent based development in VS Code, an understanding of emerging agent patterns

### Factory Missions - Multi-Agent Systems That Ship for Days
Speakers: Matan Grinberg, Luke Alvoeiro
Schedule: 12:40-1:00pm · Fleming · talk
Everyone's building multi-agent systems, but nobody agrees on how. This talk proposes a taxonomy of five frontier multi-agent strategies and shows what happens when you compose them into a single architecture. Drawing from production data at Factory, we walk through a three-role system (orchestrator, workers, validators) that uses validation contracts, structured agent handoffs, and adversarial verification. We cover the case for serial over parallel execution, why model selection per role is a compounding advantage, and how to design systems that get better with each model generation instead of being made obsolete by them.

## April 10 — MCP
### Lessons from Scaling GitHub's Remote MCP Server
Speakers: Sam Morrow
Schedule: 2:30-2:50pm · St. James · talk
GitHub operates one of the most heavily-utilised MCP servers in the ecosystem, with over 4 million downloads of the stdio server alone. Discover the architectural decisions, technical challenges and lessons learned while building and scaling a remote MCP server on production infrastructure. The session walks through the journey from initial implementation to horizontal scaling, covering the specific challenges of condensing a platform as expansive as GitHub into a coherent MCP interface. Attendees will learn practical strategies for managing tool overload, optimizing context usage, implementing distributed session storage, and maintaining observability without compromising user privacy. Whether building a first remote server or optimizing an existing implementation, attendees will gain concrete patterns, anti-patterns, and architectural guidance from real production experience. Key Takeaways • Architecture patterns for stateless, horizontally scalable remote MCP servers • Practical approaches to tool proliferation and context window constraints • Why a focus on auth, security and privacy is essential to success

### Why MCP and ChatGPT Apps Use Double Iframes (And What That Means for Your App)
Speakers: Frédéric Barthelet
Schedule: 12:20-12:40pm · St. James · talk
Always wanted to understand why both ChatGPT Apps and MCP Apps require a double iframe architecture? This talk is for you. We'll dive into the whys of this sandboxing architecture. We'll review the existing security policy options and sandbox attributes you can tune today to unlock features like nested iframes or external API calls We'll then dive into what additional Policy allow attribute enables (camera, microphone, geolocation, clipboard, payment) that isn't yet exposed in the spec. We'll focus on use cases they'd unlock (voice apps, location-aware widgets, checkout flows) I'd also make sure people learn about what could go wrong: Why allow-scripts + allow-same-origin is the classic sandbox escape, and what happens if hosts open permissions too liberally

### MCP Apps - Extending the frontier
Speakers: Liad Yosef, Ido Salomon
Schedule: 12:00-12:20pm · St. James · talk
Session title and abstract to be finalized by participating speaker

### Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents
Speakers: Michael Hablich
Schedule: 11:40am-12:00pm · St. James · talk
Last year, my team shipped Chrome DevTools MCP—and immediately learned we'd built it wrong. Our first version had one giant "debug_webpage" tool that tried to do everything. Agents couldn't compose behaviors. They failed silently when parts worked but others didn't. We had to rethink our entire architecture mid-project, decomposing that single tool into 26 focused, composable tools (click, screenshot, evaluate_script, get_network_requests, etc.). That wasn't our only mistake. Our error messages were written for humans: "Unable to navigate back in currently selected page." An agent reads that and... what? Does it retry? Give up? We rewrote them three times before agents could self-recover: "Cannot navigate back, no previous page in history." Explicit. Actionable. Machine-parseable. Then came production reality. Real web pages make hundreds of network requests. We returned them all. Agents hit context limits and failed silently. We added pagination we hadn't planned for, learned token costs the hard way, and realized that token efficiency isn't an optimization—it's a core requirement. Every agent developer hits these problems. The architecture patterns that work for human APIs break for agents. If you're building MCP servers, REST APIs, or any interface agents will use, you'll face similar challenges: - **Architecture decisions**: Monolithic vs. composable tools, and when granularity becomes overhead - **Error recovery**: How to write error messages that enable agents to self-heal without human intervention - **Token efficiency**: Real costs, pagination strategies, and when to truncate vs. summarize - **Testing without user research**: How we learned from telemetry, failure patterns, and developer proxies - **MCP protocol choices**: Why we chose MCP, what it enabled, and where it constrained us This talk shares specific implementation patterns from Chrome DevTools MCP—including the mistakes. I'll show code examples, error message transformations, and architecture decisions from our actual production system. Whether you're building MCP servers, or any agent-facing API, these patterns apply.

### Beyond Components: Designing Generative UI for MCP Apps
Speakers: Ruben Casas
Schedule: 12:40-1:00pm · St. James · talk
Most early interactions with large language models were limited to plain text. As agent systems evolved, chat interfaces gained richer interactions from tool-driven components to fully embedded third-party MCP applications. While these advances significantly improve usability, they still rely on a familiar paradigm: invoking pre-built, static UI components. Meanwhile, modern code-oriented models have become remarkably capable of generating high-quality frontend code in real time. Together, these trends unlock a new design space: generative user interfaces that are created dynamically, personalised per interaction, and still predictable, performant, and trustworthy. In this talk, we’ll explore how MCP applications enable this shift, using concrete examples and live demos to map the emerging spectrum of generative UI patterns, including: * Static UI templates exposed through MCP tools and resources * Declarative and configuration-driven interfaces assembled at runtime * Fully generative interfaces authored on the fly by LLMs enabled by the “reverse agent” and sampling We’ll discuss the trade-offs of each approach, when they make sense in production systems, and how MCP Apps helps balance flexibility with control. Attendees will leave with a practical framework for thinking about generative UI in MCP and a clearer sense of how to move beyond static components without sacrificing reliability or user trust.

### Every API Is a Tool for Agents
Speakers: Matt Carey
Schedule: 11:15-11:40am · St. James · track_keynote
The best MCP server is the one you didn't have to build. At Cloudflare we have a lot of products. Our REST OpenAPI spec is over 2.3 million tokens. When teams started building MCP servers, they did what everyone does: cherry-picked important endpoints for their product, wrote some tool definitions and shipped a separate service that covered a small fraction of their API. This was driven by a fundamental context limit of the end users' agent. And tools use a bunch of context just to describe themselves. MCP felt like a Mega Context Problem (and a separate service to maintain). I think we got it all wrong. The context limit is not an MCP problem. It's an agent problem. Tools should probably be discovered on demand and clients are coming around to this. But maybe we can also do it on the server? CLIs get this for free, self-discoverable and documented by design. APIs just need a little help. This talk will cover some of the techniques we've been exploring at Cloudflare, such as codemode and tool search, to make complete APIs accessible to agents through MCP. I'll also cover some of the work we are doing with the MCP Typescript SDK to make stateless servers the default.

### Your Agent Is an Infinite Canvas
Speakers: RL Nabors
Schedule: 2:50-3:10pm · St. James · talk
Right now, most agents interact with users in text/markdown. Chat has been heralded as the one-size fits all UI of the future. But we’ve had an interface like this before that was never adopted by the mainstream: the terminal. Programmers can type out their intentions, but “point and grunt” interfaces win with end users. Fortunately, we solved rich interactive UI thirty years ago with CSS, HTML, and JavaScript. These technologies are well rounded and feature complete, and thanks to MCP Apps and WebMCP, your agent just inherited the entire web platform as its rendering surface. MCP Apps embed full HTML, CSS, and JavaScript inside agent interfaces, not as a hack, but as a standard. WebMCP, a W3C community incubation led by the Chrome and Edge teams, is bringing structured tool calling directly into the browser. Together, they turn your agent from a text-in-text-out pipe into an infinite canvas: interactive forms, data visualizations, image galleries, approval workflows. Anything the web can render, your agent can now surface. This talk demos the full stack live. You'll watch me browse, search, and read a 23-year-old web comic archive entirely through an agent: no browser tabs, no screen scraping, no DOM wrangling. What you'll walk away with: - How MCP Apps and WebMCP actually work (iframes, postMessage, and a W3C spec you should be tracking) - When to return text vs. structured data vs. rendered UI from your MCP server - How to make existing web content agent-native without a rewrite - Why the web platform is the most powerful and underused primitive in the MCP ecosystem

### Bringing MCPs to the Enterprise
Speakers: Karan Sampath
Schedule: 3:10-3:30pm · St. James · talk
MCPs are often flaky, face multiple security vulnerabilities, and are generally hard to scale. Most enterprises struggle to use more than single digit numbers of MCPs due to issues with security, observability, and access control. In this talk, we'll explore the approaches and learnings we at Anthropic have been taking to solve this, and make MCPs more enterprise ready.

## April 10 — GPUs & LLM Infra
### One Login to Rule Them All: Cross-App Access for MCP
Speakers: Garrett Galow
Schedule: 11:15-11:40am · Abbey · track_keynote
Imagine connecting your coding agent to a dozen services you use every day. That's a dozen OAuth consent screens, a dozen token lifecycles, a dozen chances for something to break. If we already have Single Sign-On, why are users signing in so many times? Cross-App Access solves this by leveraging the three-way trust between the MCP client, the MCP server, and the organization's Identity Provider. The IdP brokers a token exchange from the user's initial login. One sign-in, access to all of their applications. I'll demo the Identity Assertion Authorization Grant flow end to end, showing how a single SSO login turns into access tokens across every MCP server. I'll also cover what this pattern unlocks for agent identity beyond MCP.

## April 10 — Google DeepMind/Gemini
### Open Models at Google DeepMind
Speakers: Cassidy Hardin
Schedule: 11:15-11:40am · Rutherford · talk
No description published; title, speakers and schedule only.

### Q&A (continuation of Open Models at Google DeepMind session)
Speakers: Cassidy Hardin
Schedule: 11:40am-12:00pm · Rutherford · talk
No description published; title, speakers and schedule only.

### What goes into building generative image and video models at scale
Speakers: Sander Dieleman
Schedule: 12:00-12:40pm · Rutherford · talk
No description published; title, speakers and schedule only.

### Agentic Panel with KP Sawhney
Speakers: KP Sawhney, Ian Ballantyne
Schedule: 12:40-1:00pm · Rutherford · talk
No description published; title, speakers and schedule only.

### Accelerating AI on Edge
Speakers: Chintan Parikh, Weiyi Wang
Schedule: 2:30-2:50pm · Rutherford · talk
No description published; title, speakers and schedule only.

### "Demo Slam" by Google DeepMind @ Expo Floor 3
Speakers: Google DeepMind team
Schedule: 2:50-3:30pm · Rutherford · talk
No description published; title, speakers and schedule only.

## April 9 — Expo Sessions (Shelley)
### How Encord Leverages AI to Stay Customer-Focused
Schedule: 10:30-10:48am · Shelley · expo_session
Diarmuid, Lead Customer Engineer at Encord, shares how the company leverages AI to transform customer support. From automating tickets, calls, and documentation to generating internal workflows and insights, AI enables the team to scale efficiently. But even with automation, relationships remain central - ensuring every customer interaction is personal, responsive, and impactful. Attendees will learn practical strategies for balancing AI-driven efficiency with human connection, and how this approach has helped Encord grow support capabilities while keeping customers at the heart of everything they do.

### Your Agent's Biggest Lie: "I Searched the Web"
Speakers: Rafael Levi
Schedule: 10:50-11:08am · Shelley · expo_session
AI agents get blocked by anti-bot systems, served fake pages, and hit with CAPTCHAs - but report back as if everything worked fine. I'll walk through why this happens and demo the same agent on the same sites with and without Bright Data's Web MCP. Talking points: - Cloudflare AI Labyrinth actively feeds fake content to AI agents - Cloudflare blocks AI crawlers by default on 20% of the web - Columbia/Tow Center: 60%+ citation failure across 8 AI search engines - AWS built an IETF protocol (Web Bot Auth) to address the problem - Live demo: same agent, same sites - blocked vs clean data - How Bright Data's Web MCP handles anti-bot, CAPTCHAs, and JS rendering transparently

### Reverse engineering a Viking VOIP phone protocol with Claude Code
Schedule: 1:05-1:23pm · Shelley · expo_session
If you’ve ever tried to integrate with legacy hardware, you’ll know the frustration of opaque protocols, missing documentation, and devices that were never meant to be extended. But what if you could systematically reverse engineer and control these systems anyway? Enter AI-assisted protocol analysis with Claude Code. In this talk, we’ll walk through how to dissect and reconstruct the protocol behind a Viking VoIP phone—capturing traffic, identifying patterns, and using Claude Code to accelerate understanding and implementation. You’ll learn practical techniques for reverse engineering networked devices, how to leverage LLMs to speed up low-level analysis, and how to turn a black-box device into a programmable interface.

### From MCP to Scale: Pipelines That Build Themselves
Speakers: Rafael Levi
Schedule: 1:25-1:43pm · Shelley · expo_session
An agent with Bright Data's MCP can do more than fetch data - it can build and maintain entire data pipelines. I'll show an agent that uses MCP to explore a target site, understand its structure, then autonomously writes a production script using Bright Data's APIs for scale processing. The site changes? The agent updates the pipeline. No human scraper maintenance. Talking points: - The agent as pipeline builder: MCP to explore and understand, API scripts for scale execution - Pre-recorded demo: agent explores site via MCP, detects structure, handles JS rendering - Agent writes production code using Bright Data's APIs for batch processing at scale - Agent maintains the pipeline - when the site changes, the agent fixes it - Bright Data as the complete toolkit the agent needs: MCP for intelligence, APIs for execution

### BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike
Schedule: 1:45-2:03pm · Shelley · expo_session
Codex and Claude Code are magically productive if they do the right thing, don’t overstep boundaries and keep architecture consistent. But through the narrow window of a prompt it’s almost impossible to keep even small projects consistent as the code base grows. Human code review becomes impossible when PRs get to 10,000 lines with regularity. Spec-driven Development is a great step in the right direction, but it’s logical to go way further. In this talk we cover our evolving approaches to development that use machine readable specs, Architectural Decision Records (ADRs), and closed testing loops to get increasingly tight control of agentic coding. The talk will include plenty of real examples from the techniques we use to ship production products at Safe Intelligence.

### How Lovable self-improves every hour
Schedule: 2:05-2:23pm · Shelley · expo_session
What if you gave your agent a way to learn from its mistakes? When software engineers get stuck using AI, they can generally unblock it with some effort. If they face an issue repeatedly they may even figure out a way to automate it or fix it once and for all. When non-technical users get stuck, they often abandon their projects and leave in frustration. At Lovable we are working towards a vision where every solvable issue should only cause friction once. This talk covers two automated continual improvement loops we built that move us towards that reality, including a non-traditional way for the agent to complain about its working conditions Presented by Benjamin Verbeek, MoTS at Lovable

### How agent o11y differs from traditional o11y
Speakers: Phil Hetzel
Schedule: 3:45-4:03pm · Shelley · expo_session
Traditional observability tells you if a system is up and where it failed, but not whether it's actually delivering value to users. The best agent observability tools create a "flywheel" that connects observability and evals into a continuous improvement loop. This talk will show how agent observability drives not just uptime, but real agent quality, and how both technical and non-technical teams can power the flywheel together.

### Live Demo & Q&A with Qodo
Schedule: 4:05-4:23pm · Shelley · expo_session
No description published; title, speakers and schedule only.

## April 9 — Expo Sessions (Wesley)
### Live Demo & Q&A with Arize
Schedule: 10:30-10:48am · Wesley · expo_session
No description published; title, speakers and schedule only.

### How We Built Zeta2: Training an Edit Prediction Model in Production
Schedule: 1:05-1:23pm · Wesley · expo_session
Zeta2 is the edit prediction model that powers tab-completion in Zed. It watches your recent edits, cursor position, and surrounding code, then predicts what you'll change next. This talk walks through how we built it. We'll cover knowledge distillation from a frontier teacher into a small, fast model, why we abandoned synthetic GitHub commit data for real opt-in edit traces, and how we diagnosed a reversal problem where the model kept undoing the user's work. We'll also talk about choosing a new base model, figuring out when to stop tuning and ship, and what we're still working on.

### Untethered Productivity
Schedule: 1:25-1:43pm · Wesley · expo_session
I do my best thinking away from a keyboard. Walking, specifically. So I rebuilt my entire development workflow around that fact. When I'm at my desk, I'm reviewing diffs, approving PRs, checking on running agents. That's maybe 30% of my day. The rest — the architecture, the decomposition, the hard thinking — happens on trails or in the backyard, on my phone. Here's the actual loop: I voice-dictate a brief at 179 WPM. I dispatch it to an agent running in an isolated git worktree — its own branch, its own checkout, no interference with my main workspace. I close my laptop and walk. From my phone I check on progress through Remote Control, or fire off a new task via Dispatch. When I sit back down, there are diffs waiting for review in a hardened CI pipeline that catches anything an agent got wrong before it merges. Your best thinking doesn't happen at a keyboard. The keyboard is for reviewing what your thinking produced. I'll walk you through the tools that make this real — Dispatch, Remote Control, Channels, git worktrees, and agent teams. All of these shipped in Claude Code between February and March 2026. Every demo comes from my actual daily workflow. You'll leave with: - The full untethered loop: voice brief → dispatch → worktree → remote check-in → diff review - How Dispatch, Remote Control, and Channels work and when to use each - The prompt structure that lets you walk away from a running agent and trust the output - How a hardened CI pipeline is what makes the speed safe — and what happens when you skip it

### Engineering voice agents: Latency, quality, and scale
Schedule: 1:45-2:03pm · Wesley · expo_session
Name: Rishabh Bhargava Job title: Director, EngineeringCompany: Together AI Voice agent infrastructure has reached an inflection point. Text-to-speech sounds human, speech-to-text error rates are decreasing, and smaller LLMs can reliably tool-call and follow complex instructions. The convergence of these breakthroughs in 2026 makes voice agents a viable production surface for AI. But great voice agents require great engineering execution. This session walks through the full STT → LLM → TTS pipeline with a focus on what actually matters in production: Latency: Users notice above 500ms, hang up above 1s; we’ll cover real-time APIs, and model colocation. Intelligence: Context handling, tool calling, and complex multi-step workflows Naturalness: Why voice quality directly impacts user trust, especially when serving users across languages and in use cases where emotion matters Reliability: Observability, graceful degradation, and maintaining 99.9% uptime at scale

### Live Demo & Q&A with Cloudflare
Schedule: 2:05-2:23pm · Wesley · expo_session
No description published; title, speakers and schedule only.

### From Writing Code to Designing Systems: How the Developer Role Has Changed
Schedule: 3:45-4:03pm · Wesley · expo_session
For decades, developers have been valued primarily for how much code they could write and how quickly they could write it. That model no longer scales. As AI becomes a first-class collaborator, the bottleneck is no longer syntax or implementation speed—it’s clarity of intent, architectural thinking, and the ability to coordinate work across many autonomous contributors. Today’s challenge is not "How do I write this code?" but "How do I ensure this system is built correctly, consistently, and to company standards—across dozens of moving parts?" Without structure, AI-assisted development risks fragmentation: inconsistent patterns, duplicated logic, and solutions that technically work but fail architectural, security, or organizational expectations. This talk introduces a new mental model for modern development: the developer as planner, system designer, and orchestrator of agents. Using GitHub Copilot, GitHub Copilot CLI, and custom Copilot agents driven by agents.md, we’ll explore how developers can decompose large problems, delegate implementation to specialized AI agents, and encode standards, constraints, and intent directly into the workflow. Instead of prompting ad-hoc, we define explicit instructions per layer—frontend, backend, infrastructure, testing—so every agent builds the right thing in the right way. The result is not less control, but more leverage: faster delivery, higher consistency, and systems that reflect deliberate design rather than accidental outcomes. What you’ll learn: How the developer role is shifting from code producer to system designer, planner, and agent orchestrator How to structure projects for agent-driven development, using GitHub Copilot CLI, Copilot Chat, and agents.md to encode standards and intent How to ensure architectural consistency and quality at scale by giving agents clear responsibilities, constraints, and ownership boundaries

### RunPod Serverless Deep Dive
Schedule: 4:05-4:23pm · Wesley · expo_session
No description published; title, speakers and schedule only.

### RAG is dead, right??
Schedule: 10:50-11:08am · Wesley · expo_session
"RAG is dead" has been an enduring hot take in AI engineering. But in practice, what’s actually dying is the idea that retrieval equals "just embed and run vector search and call it a day". What’s thriving is a broader, more capable set of search behaviors inside agents. In this session, we’ll define RAG and agentic search in the specific context of code retrieval, then use real-world patterns from modern coding assistants to show why both approaches keep showing up in successful systems. You’ll walk away with a clearer mental model for when embeddings help, when to use structured/lexical search, and why hybrid, tool-rich retrieval is quickly becoming the default for serious codebase navigation.

## April 9 — Expo Sessions (Wordsworth)
### Stop babysitting your agents: building a context engine for mergeable code
Speakers: Brandon Walsenuk
Schedule: 10:30-10:48am · Wordsworth · expo_session
AI coding agents are fast, capable, and context-blind. They generate code that compiles but miss your team's conventions, ignores past decisions, and breaks patterns— because they don't understand how your system actually works. The fix most teams try (more MCP servers, more rules files, team skills, bigger context windows) gives agents access to information without giving them understanding. This talk shows what changes when you close that gap with a context engine. I'll reference a real coding task run without and with organizational context: the first took 2.5 hours and 20.9M tokens with multiple rounds of human correction, the other took 25 minutes and 10.8M tokens and produced mergeable code on the first pass. Same agent, same model. Includes a short demo showing the moment organizational context changes the agent's approach. You'll see the three problems a context engine solves — quality, efficiency, and autonomy — and the hard lessons we learned getting it wrong before we got it right.

### Context Graphs 101: What They Are and How to Get Started in 5 Minutes
Schedule: 10:50-11:08am · Wordsworth · expo_session
"Most agent failures aren't model failures - they're context failures. A Context Graph gives your agents structured knowledge, situational data, past decisions, and the reasoning traces behind them. It's queryable, traversable, and unlike a static knowledge base, it gets smarter as your agents use it. In this 18-minute session, we'll show you what a Context Graph actually looks like, how it connects to your agent stack via MCP and the `neo4j-agent-memory` package, and how to get one running in 5 minutes."

### The maturity phases of running evals
Speakers: Phil Hetzel
Schedule: 1:05-1:23pm · Wordsworth · expo_session
Most teams start with ad hoc spot-checks and end up needing a repeatable system that prevents regressions. This session walks through the maturity curve from manual examples, to automated test sets, to continuous evaluation tied to releases and real user traffic. You will leave with a clear model for what to do next at each stage, and what to avoid as you scale.

### Make Your Coding Agents Reliable (and Prove It with Evals)
Schedule: 1:25-1:43pm · Wordsworth · expo_session
AI coding agents promise speed, but often miss intent, break existing code, or waste tokens. In this session, we’ll show how to make agents more reliable and efficient by giving them the right context. Through a live, end-to-end demo, you’ll see how to generate, version, and distribute skills across your organization, so your agents produce better quality code, without the rework. Practical, hands-on, and focused on real development workflows. Speaker: Simon Maple, Head of DevRel at Tessl

### Getting Started with RunPod
Schedule: 1:45-2:03pm · Wordsworth · expo_session
No description published; title, speakers and schedule only.

### Building Interactive UIs in VS Code with MCP Apps
Schedule: 2:05-2:23pm · Wordsworth · expo_session
MCP Apps combine MCP tools with HTML resources to display rich, interactive content. When a host calls an MCP tool, the server returns both data and a UI that renders the result. VS Code supports rendering MCP App elements directly in your IDE. In this talk we’ll walk through what parts of the MCP spec need to be implemented for an MCP App to work and how to build an MCP App and use it in VS Code. We will also discuss security considerations when working with MCP and how we recommend mitigating them.

### Why Rust is the Ideal Language for Vibe-Coding
Speakers: Daniel Szoke
Schedule: 3:45-4:03pm · Wordsworth · expo_session
What language would you use to vibe-code a new app? If you ask ChatGPT this very question, it will probably enthusiastically suggest TypeScript and possibly Python; if Rust is mentioned, there might be a note saying to use it "if you enjoy suffering beautifully" (yes, I actually got this response). In fact, Rust is the ideal programming language for vibe-coding. The language itself deterministically enforces rules to ensure correctness (e.g. memory safety and safe concurrency) and best practice. When agents code in other languages, often all that prevents them from shipping broken code is some easily-forgotten agent instructions; possibly another independent, but fallible, review agent; and in the worst-case scenario, nothing but hope. When violating a rule in Rust, agents reliably receive error messages that explain exactly what is wrong and point them in the right direction. Rust's tooling-enforced invariants provide a natural agentic feedback loop, lowering reliance on model skill and instead introducing guardrails for your code.

### Building safe Payment Infrastructure for the autonomous economy
Speakers: Steve Kaliski
Schedule: 4:05-4:23pm · Wordsworth · expo_session
Agents are evolving from calling free APIs to executing real transactions, creating a new challenge: how do we let software spend money autonomously without catastrophic risk? This talk presents Stripe's approach to solving the dual problems of secure credential transmission and making businesses discoverable to agents. Through live code examples, we'll explore how to build guardrails that make autonomous spend safe and examine what infrastructure is needed as agents purchasing becomes a core capability. Whether you're building agent frameworks or enabling your business to work with agents, you'll learn how to make agent transactions both powerful and safe.

## April 10 — Expo Sessions (Wesley)
### Two Roads to Durable Agents: Replay vs. Snapshot
Speakers: Eric Allam
Schedule: 10:50-11:08am · Wesley · expo_session
AI agents that run for hours, wait on humans, and call dozens of tools need durability. Today the default answer is application-level replay: record every step, replay the log on recovery, require your code to be deterministic. It works, but it constrains how you write agents and can't capture everything a running process actually holds in memory. There's a second approach that almost nobody in the AI engineering world is using yet: OS-level snapshot/restore. Freeze the entire process. Free all resources. Restore it exactly where it left off, with no replay log, no determinism requirements, and no step boundaries in your code. In this talk I'll compare both approaches honestly, where each one wins and where each one breaks, then demo a live agent on Trigger.dev that checkpoints mid-execution, suspends at zero cost while waiting on a human, and resumes from snapshot. You'll leave with a clear framework for choosing the right durability model for your agents.

### Your Agent's Biggest Lie: "I Searched the Web"
Speakers: Rafael Levi
Schedule: 3:45-4:03pm · Wesley · expo_session
AI agents get blocked by anti-bot systems, served fake pages, and hit with CAPTCHAs - but report back as if everything worked fine. I'll walk through why this happens and demo the same agent on the same sites with and without Bright Data's Web MCP. Talking points: - Cloudflare AI Labyrinth actively feeds fake content to AI agents - Cloudflare blocks AI crawlers by default on 20% of the web - Columbia/Tow Center: 60%+ citation failure across 8 AI search engines - AWS built an IETF protocol (Web Bot Auth) to address the problem - Live demo: same agent, same sites - blocked vs clean data - How Bright Data's Web MCP handles anti-bot, CAPTCHAs, and JS rendering transparently

### Building AI Systems That Ship
Schedule: 10:30-10:48am · Wesley · expo_session
Most agent demos break the moment they leave a controlled environment. The model works fine. The systems around it don't. In this talk, I'll walk through what "agent-ready" means from two sides: a codebase agents can safely change, and a product agents can reliably use. I'll use two real projects as examples: Case, a harness for orchestrating coding agents, and the WorkOS CLI. Together, they show how to give agents real freedom while keeping quality high through clear constraints, machine-friendly interfaces, and feedback loops that compound over time.

### Live Demo & Q&A with Arize
Schedule: 1:05-1:23pm · Wesley · expo_session
No description published; title, speakers and schedule only.

### Stop babysitting your agents: building a context engine for mergeable code
Speakers: Brandon Walsenuk
Schedule: 1:25-1:43pm · Wesley · expo_session
AI coding agents are fast, capable, and context-blind. They generate code that compiles but miss your team's conventions, ignores past decisions, and breaks patterns— because they don't understand how your system actually works. The fix most teams try (more MCP servers, more rules files, team skills, bigger context windows) gives agents access to information without giving them understanding. This talk shows what changes when you close that gap with a context engine. I'll reference a real coding task run without and with organizational context: the first took 2.5 hours and 20.9M tokens with multiple rounds of human correction, the other took 25 minutes and 10.8M tokens and produced mergeable code on the first pass. Same agent, same model. Includes a short demo showing the moment organizational context changes the agent's approach. You'll see the three problems a context engine solves — quality, efficiency, and autonomy — and the hard lessons we learned getting it wrong before we got it right.

### Mastering AI Pricing: Flexible & Agile Monetization for your AI solutions
Speakers: Mayank Pant
Schedule: 1:45-2:03pm · Wesley · expo_session
Monetizing AI is hard. Rising GPU and inference costs are squeezing margins, and traditional SaaS pricing simply does not work for the unpredictable compute demands of new-age AI companies. With models constantly shifting across credits, tokens, and seats, a new challenge emerges: how do we charge for AI without stalling growth? This talk presents a framework for solving the dual problems of aligning charge metrics with true customer value and balancing predictable revenue with rapid adoption. Through real-world examples, we'll explore how to build guardrails that protect your margins and see how Stripe’s world-class usage-based billing solution helps AI companies launch quickly and monetize with ultimate agility. Whether you're launching your first AI product or revamping your current model, you'll learn how to make your pricing strategy both profitable and adaptable.

### What if the network was the sandbox?
Schedule: 2:05-2:23pm · Wesley · expo_session
Every agent needs a sandbox” is quickly becoming the default way we think about running agents. Give it an environment. Isolate it. Control the blast radius. That works…to a point.But as agents move from acting as the user to operating more autonomously, the real problem isn’t just where they run. It’s what they can reach, what they can do, and how you can see it.Sandboxing is trying to solve two different problems at once: execution isolation & access control. You can fully isolate an agent’s runtime and still have it incorrectly access sensitive systems.In this session, we’ll explore what’s possible if the network becomes the sandbox. We’ll show how identity-based access at the network layer can: define precise boundaries for agent behavior, remove the need to distribute API keys and credentials, and give you complete visibility into what agents are actually doing.

## April 10 — Expo Sessions (Shelley)
### Building an ACP-Compatible Agent Live
Schedule: 3:45-4:03pm · Shelley · expo_session
In this session, we'll be building a coding agent that implements ACP — covering protocol design, session lifecycle management, and handling tool calls. The session ends with a live demo of the finished agent running inside Zed, showing what ACP looks like in practice from both sides of the protocol.

### Spec-Driven Testing for Agents With A Brain the Size of A Planet
Schedule: 10:50-11:08am · Shelley · expo_session
Your agent is ready to deploy: running on the latest frontier model with a layer cake of fine-tunes and carefully engineered system prompts. But is it committed to the cause? Will it play its role without getting hijacked, distracted or just confused by minor input variations? Can we even specify what “good” looks like outside of a few prompt examples? Unfortunately testing agents can be harder than actually building them. In this talk, we’ll cover practical ways to define agent behavior as a set of specs and automate testing beyond running the same canned prompts every time. You’ll learn how to write and apply different types of specs (red/gold team sets, rules, constraints, policies), and on the testing side we’ll cover robustness checks based on lightweight formal methods, and fuzzing with plenty of examples along the way.

### Live Demo & Q&A with Together AI
Schedule: 1:05-1:23pm · Shelley · expo_session
Name: Max RyabininJob title: Vice President of Research & DevelopmentCompany: Together AI Expo session title: Road to 5M Sequence Length: Breaking Memory Barriers in Context ParallelismAbstract/tralking points: Many advanced AI applications, such as video generation and agentic pipelines, require models that could operate with hundreds of thousands or even millions of tokens. However, training Transformer models to process context lengths of this size is challenging due to the memory and compute constraints of attention. In this talk, we'll outline the techniques for finding and optimizing bottlenecks in long-context training. We will also present Untied Ulysses, the latest research technique from Together AI that presents an approach that boosts the potential training context length by 25% compared to prior methods.

### Task Fidelity Scaling Laws
Schedule: 1:25-1:43pm · Shelley · expo_session
Most teams trying to improve LLM agents reach for bigger models, better RL, or more data. This talk is on a lever that often dominates all three: task fidelity. In controlled TerminalBench experiments, fine-tuning on a small set of well-posed, non-trivial tasks dramatically outperforms training on an equal number of low-fidelity tasks with the same model and compute. The gap isn't cosmetic. Ambiguous or misaligned specs systematically push agents into confident but fundamentally wrong strategies. The model doesn't just fail more — it internalizes the wrong behavior. So what makes a task actually train an agent? From large-scale trace analysis, we distill practical criteria you can apply immediately: how to write objectives that are precise without being trivial, how to align tests with intended strategy, and how to detect when a task is generating noise instead of signal. Small spec changes materially alter what the model learns. The takeaway: for agent fine-tuning, task fidelity behaves like a scaling law. Before increasing model size or RL budget, fix your tasks.

### Comprehend First, Code Later: The AI Skill I Rely On Daily
Speakers: Priscila Andre de Oliveira
Schedule: 1:45-2:03pm · Shelley · expo_session
Literally everyone is vibe coding. It's about letting AI write, commit, and ship code you never even read. Perfect for prototypes and side projects - no argument there. But what happens when you're working in a million-line codebase where you need to understand before you change? Quality code still matters. It is widely stated in the software development community that developers spend 70–80% of their time reading and understanding existing code, not writing new code. We now have an incredibly smart tool - so why not use it for exactly that? So I went straight to the data - 239 of my own messages from daily work at Sentry. What I found flipped the narrative: my #1 use of AI wasn't generation. It was comprehension. Whether navigating unfamiliar code or reconstructing past decisions from commit history - AI became the teammate who never gets tired of my questions. In this talk, I'll show you the loop that actually makes me productive in a large, complex codebase: understand first, then code.

### Why Can't Anyone Answer Questions About the Business?
Schedule: 2:05-2:23pm · Shelley · expo_session
At WorkOS, answering non-trivial questions about our customers was hard. Customer production data required writing SQL with context awareness of how our data is structured, which most of our team is not well versed in. You often needed data from multiple sources. Further, each teammate was going about this their own way, so it was hard to manage or control. We had Mode queries shared in Notion and not everything warranted an admin dashboard in Retool. Questions that actually drove decisions (""how many customers are doing X,"" ""what does usage look like for this cohort"") required someone specialized set aside time to answer the question to get back to the person who needed the info. We built Studio to serve as a knowledge layer that connects an LLM directly to our production data sources and lets anyone on the team ask these questions in natural language, in the tool or via Slack. The model queries Snowflake with knowledge of how our data is organized and can cross-reference that with other sources like Salesforce, Linear, and Gong. I'll show how we use Studio to generate answers and lightweight shareable tools, and walk through the challenges in building a platform knowledge layer that knows how to get the right data. I'll cover the specific guidance patterns that made the difference between useful and unreliable, and share what generalizes to any AI product that needs to work over company data.

### Does GenAI "belong" to data scientists?
Speakers: Phil Hetzel
Schedule: 10:30-10:48am · Shelley · expo_session
GenAI work sits at the intersection of modelling, product, and software engineering, and many orgs are still arguing about ownership. This session explores what data scientists uniquely contribute, what has shifted toward application engineering, and how teams can split responsibilities without creating bottlenecks. The goal is a practical operating model that ships features faster while improving quality and safety.

### Build an Aura Agent in 10 Minutes — From Unstructured Content to Knowledge Graphs
Schedule: 4:05-4:23pm · Shelley · expo_session
"Databases, documents, APIs, notes—your data is everywhere, but your AI agent only understands a fraction of it. Most agents can query structured data, yet struggle to make sense of unstructured content and the relationships within it. But what if you could turn that raw content into a knowledge graph—and plug it directly into your agent? In this session, we’ll build an Aura Agent in under 10 minutes, starting with natural language interaction over structured data. We’ll then use LLMs to extract entities and relationships from unstructured content, generate a graph schema, and build a knowledge graph. Finally, we connect it back to the agent—enabling richer, context-aware responses powered by both structured and unstructured data."

## April 10 — Expo Sessions (Wordsworth)
### Benchmarking semantic code retrieval on Claude Code
Schedule: 4:05-4:23pm · Wordsworth · expo_session
Claude Code, unlike Cursor, does not use semantic search for code retrieval. There are good reasons for this, but Cursor has consistently demonstrated that semantic retrieval can materially improve code search to improve answer accuracy, increase code retention, and reduce token usage. In this session, we’ll introduce a Claude Code plugin for semantic codebase search alongside other modalities (BM25, regex/globbing/grep, filtering), and demonstrate how an agent can choose the right tool for the job. We’ll share benchmark-style results that compare answer quality and token consumption with and without semantic retrieval across a small set of representative tasks.

### How to talk to statues
Schedule: 10:50-11:08am · Wordsworth · expo_session
Museums and public spaces are full of stories—but they’re locked behind plaques, audio guides, and one-way experiences that rarely adapt to the person in front of them. But what if you could just… talk to them? Enter multimodal AI agents powered by ElevenLabs. In this talk, we’ll walk through how to build an app that lets users point their phone at a statue, identify it with computer vision, and bring it to life with a real-time voice conversation. We’ll cover the full stack—from visual recognition to conversational agents to expressive voice synthesis—and show how tools like ElevenAgents enable low-latency, human-like interactions across modalities. By the end, you’ll understand how to design and ship immersive, multimodal experiences that turn static objects into interactive characters.

### Live Demo & Q&A with Qodo
Schedule: 1:05-1:23pm · Wordsworth · expo_session
No description published; title, speakers and schedule only.

### What Lies Beneath the API: when should you tune your own model?
Schedule: 1:25-1:43pm · Wordsworth · expo_session
Frontier model APIs have changed the tech startup landscape forever. But as companies mature and get larger contracts, their product needs change, often specializing. When is it worth it to start training your own model?

### Common Pitfalls of Skills Development (And How to Fix Them)
Schedule: 1:45-2:03pm · Wordsworth · expo_session
Why do skills fail, and how do you fix them? This session dives into real data from skill evaluations to uncover the most common pitfalls when building for AI agents. We’ll walk through examples of where things break (validation issues, activation issues, security triggers) and show how to systematically improve performance using evaluation and optimzation loops. Think of it as a practical clinic for making your agents more accurate, efficient, and production-ready. Speaker: Maria Gorinova, AI Researcher at Tessl

### Malleable Evals: Why Are We Still Evaluating Adaptive Systems with Static Tests?
Speakers: Vincent Koc
Schedule: 2:05-2:23pm · Wordsworth · expo_session
No description published; title, speakers and schedule only.

### Stop Making Models Bigger. Make Them Behave
Schedule: 3:45-4:03pm · Wordsworth · expo_session
Everyone knows bigger models reason better. What’s less obvious is that they often behave worse, especially when tools are involved. In this talk showing a practical application of research around task fidelity, we’ll show how a 4B model was fine-tuned to beat a 235B model on real financial analysis tasks – not by adding more reasoning, but by enforcing tool discipline. Using reinforcement learning with the open-source rLLM framework, the model learned to explore schemas, validate outputs, and retry failures instead of hallucinating confident nonsense. The key surprise: training on simple tool interactions transferred cleanly to much harder, multi-step problems. If you’re building LLM systems that touch things like databases, APIs, or internal tools, this talk focuses on the behaviors that actually matter — and how to teach them without frontier-scale compute.

### Can LLMs generate Enterprise Quality Code?
Schedule: 10:30-10:48am · Wordsworth · expo_session
We all know how fast it is to create an app with modern AI agents but how do we ensure the code is reliable, maintainable and secure enough to be used by enterprises? In this talk we’ll share a benchmark from our testing of 50+ (and growing) of the latest and highest performing large language models and show how they compare not just on task completion but on the quality of the code they create. You’ll see that models are not the same and that some produce more than 2x the issues of others. Once you understand your model how do you protect yourself from its weaknesses? We’ll show how you can integrate AI Agents with deterministic static analysis to ensure enterprise level quality without killing the AI Productivity gains.

## April 10 — Expo Sessions (Moore)
### AMA + Feedback + Brainstorm: Improving AI Engineer
Speakers: swyx
Schedule: 4:05-4:23pm · Moore · expo_session
No description published; title, speakers and schedule only.

## April 10 — Hallway Track
### Running Gemma 4 On-Device: 40 Tokens/s on iPhone with MLX
Speakers: Adrien Grondin
Schedule: 2:30-2:40pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### Frontier AI at Home (literally)
Speakers: Alex Cheema
Schedule: 2:40-2:50pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### Your agent is blindfolded. How giving it (good) eyes multiplies performance and trust
Speakers: Johan Lajili
Schedule: 2:50-3:00pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### WolfBench: Why one score is not enough & why thinking can make agents dumber
Speakers: Wolfram Ravenwolf
Schedule: 3:00-3:10pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### Your coding agent doesn't always follow your rules. An agent harness makes sure it does, in real-time, every time.
Speakers: Talha Sheikh
Schedule: 3:10-3:20pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### Nono.sh: Run Claude in dangerous mode
Speakers: Stephen Parkinson
Schedule: 3:20-3:30pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### remobi.app: Don't change your terminal workflow for mobile. Swipe between agents, unblock when stuck.
Speakers: Connor Adams
Schedule: 3:30-3:40pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

### Daily chess puzzle explanations on YouTube: Our agent analyzes and describes chess puzzles in an accessible way - arrows included!
Speakers: Stephan Steinfurt
Schedule: 3:40-3:50pm · Moore · lightning
Hallway Track: Attendees propose lightning talks, peers vote, and the best talks get to go onstage as impromptu lightning talks. Check the AIE attendee Slack for signup and voting instructions.

