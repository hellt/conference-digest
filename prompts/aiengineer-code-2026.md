>>> HOW TO RUN THIS <<<
This is the digest prompt for aiengineer-code-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/aiengineer-code-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/aiengineer-code-2026.md
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

Below is the program for AI Engineer Code Summit 2026. Read it and produce a digest
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
- `deepseek` - DeepSeek models, research, deployment and inference economics
- `openai` - OpenAI models, products, APIs and deployment engineering
- `anthropic` - Anthropic Claude models, agent SDKs and deployment engineering
- `z-ai` - Z.ai/Zhipu GLM models, open weights and deployment engineering
- `moonshot` - Moonshot AI Kimi models and deployment engineering
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
conference: AI Engineer Code Summit 2026
source_url: https://ai.engineer/code/2026/sessions.json
generated: 2026-11-16
registry_key: aiengineer-code-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## Nov 10
### Light Breakfast
Schedule: 8:00am - 9:00am · Continental 5 (Breakfast & Lunch) · other
No description published; title, speakers and schedule only.

### Registration
Schedule: 8:00am - 5:30pm · Registration (outside Golden Gate) · other
No description published; title, speakers and schedule only.

### MC Intro
Speakers: Richelle Ji
Schedule: 8:55am - 9:00am · Continental 1–3 (Workshop Room 1) · workshopTalk
No description published; title, speakers and schedule only.

### From Shared Language to Enforceable Contracts: Ontologies as Guardrails for Agents.
Speakers: Frank Coyle
Schedule: 9:00am - 9:25am · Continental 1–3 (Workshop Room 1) · workshopTalk
This talk echoes Pocock’s “shared understanding” and augments it -- turning that language into a machine-checkable model: typed entities, relationships, allowed states, and inference rules.

### Machine trust
Speakers: CJ Avilla
Schedule: 9:00am - 10:00am · Continental 4 (Workshop Room 2) · workshop
Agents can now work for hours, but most of us still approve every step or skip the prompts and hope. This session asks where we are on the curve for trusting agents, and what has to be true before we hand them much more work. It draws on decades of trust research, from how societies learned to trust strangers to how pilots learned to trust the autopilot. Then we use Claude Managed Agents as a reference implementation for building systems that are safe, secure and trustworthy by default.

### New Ways of Working with Codex
Speakers: Dominik Kundel, Charlie Guo
Schedule: 9:00am - 10:00am · Continental 6 (Workshop Room 3) · workshop
Keeping up with the rapid changes in coding agents can be exhausting. Join Dominik Kundel for a practical tour of recent features and workflows to bring you up to speed, without all the noise. We'll cover with live demos and walkthroughs how you can make the most out of your ChatGPT subscription whether you are pair programming with Codex or having your dot manage your incidents.

### Build a Coding Agent Harness From an Empty Loop
Speakers: Tejas Kumar
Schedule: 9:00am - 10:00am · Continental 7–9 (Workshop Room 4) · workshop
Start with an agent that lies about finishing, and leave with a harness you'd trust with your repo. A bare agent loop ends when the model says it's done. In my AI Engineer Europe 2026 talk, that loop hit a login page and reported success anyway. The model wasn't the problem: nothing around it checked anything. In this workshop we fix that by hand, one layer at a time, in TypeScript. We build every part of an agent harness from scratch: - **The agent loop:** call the model, run the tools it asks for, feed the results back. - **Guardrails:** iteration and context limits the model can't talk its way past. - **Context management:** what stays in the window when a run gets long. - **Deterministic verification:** read the trace, run the linter and the tests, and let a failed check overrule the model's claim. - **Retries and secrets:** a loop around the loop, and credentials the model never sees. One rule for the whole session: the prompt never changes. Every fix is code. You'll leave with a working harness on your laptop and the habit of fixing the harness before the prompt. Starting repo: https://github.com/TejasQ/basically-ai-harness

### One team's path to trusting AI generated code
Speakers: Ankit Jain
Schedule: 9:30am - 9:55am · Continental 1–3 (Workshop Room 1) · workshopTalk
Our team merges 4x more pull requests than we did a year ago. Almost all of that code is AI-generated, human assisted. We tried scaling code review to match — more reviewers, AI review tools, stricter checklists — and none of it worked. What worked was stopping the fight over diffs entirely and building a verification layer around *intent*. This is the story of how one engineering team replaced the PR review bottleneck with an intent-driven verification workflow: capturing what a change *should* do before a single line is generated, encoding team standards as reusable invariants, and letting deterministic checks — not tired reviewers — produce the evidence that a change is safe to ship. I'll walk through the specific practices that made the difference — especially how we turned years of recurring review comments into machine-enforceable invariants — and share the results, the failures, and what we'd do differently.

### The True Cost of AI Coding
Speakers: Scott Tolinski
Schedule: 10:10am - 10:35am · Continental 1–3 (Workshop Room 1) · workshopTalk
After seeing the mental health effects of AI coding throughout the industry, Scott surveyed nearly 4000 developers about how agentic workflows are affecting their mental health. Hear what's happening and why.

### Forget AGI. You're Surrounded by Low-Hanging Fruit.
Speakers: Lucas Meijer
Schedule: 10:10am - 11:10am · Continental 4 (Workshop Room 2) · workshop
Software development lifecycles are full of slow processes you can automate. Let's fix those before we go pretend to be AI astronauts. We'll cover a range of easy-to-adopt techniques for that kind of automation, and for pushing back against the agent-supercharged entropy that keeps trying to make your codebase slop out of control. You'll leave with prompts, skills and workflows you can put to work the same afternoon.

### Build a Multi-Agent PR Review and Repair Workflow with Omnigent
Speakers: Elise Gonzales, Bradford Chang
Schedule: 10:10am - 11:10am · Continental 6 (Workshop Room 3) · workshop
Build a GitHub CI workflow that uses specialist agents to review pull requests, coordinate bounded repairs, and validate the resulting changes. In this hands-on workshop, you’ll connect agents across models and coding harnesses, define their roles and permissions, and test the pipeline while Omnigent handles session lifecycles, delegation, and messaging. We’ll draw on how Omnigent uses its own agents to manage incoming issues and contributions as an active open-source project, examining what it takes to turn review findings into tested changes ready for human approval. You’ll leave with version-controlled agent configurations and a runnable workflow you can adapt to your own projects.

### Stop Prompting, Start Delegating: Hand off work to a team of agents
Speakers: Ross Cefalu
Schedule: 10:10am - 11:10am · Continental 7–9 (Workshop Room 4) · workshop
Most teams still use agents one task at a time: prompt, wait, review, repeat. In this hands-on workshop, you'll go further and hand an entire stream of work to agents with Factory. Bring your laptop. We'll take a real project from goal to merged PRs, setting up the scope, guardrails, and review checkpoints that make delegation safe. You'll leave with a workstream running and a playbook for deciding what to hand off next.

### One Rule, One Throwaway Skill: Agent Migrations with ast-grep
Speakers: Justin Poehnelt
Schedule: 10:40am - 11:05am · Continental 1–3 (Workshop Room 1) · workshopTalk
Coding agents struggle with large migrations. A migration produces thousands of diffs, agents apply the same fix five different ways, and nobody can reliably say how much work remains. I migrated a production codebase to Effect by pairing each change with an ast-grep rule that matches the old pattern and a temporary skill that tells an agent how to fix a match. The list of matches told agents what to work on and told me how much was left. It also divided the work across parallel agents without overlap. But agents could also make a match disappear without fixing it, so I had to write rules that were hard to evade. I’ll show how the rule and skill pair worked on a real migration and what I would change next time.

### Networking Break
Schedule: 11:10am - 11:40am · Continental Foyer · other
No description published; title, speakers and schedule only.

### Inference Engineering for Coding Agents
Speakers: Philip Kiely
Schedule: 11:40am - 12:05pm · Continental 1–3 (Workshop Room 1) · workshopTalk
Coding agents are a dominant use case for LLMs, but they tend to use generalized inference setups even at large scale. Like any optimization problem, in inference you can get better results with better constraints. This talk shares specific techniques that you can apply when building an inference service for exclusive use in coding agents, including targeted quantization and pruning schemes, domain-specific post-training, KV cache management around compaction events, subagent session affinity in a world of autoscaling and load balancing, and code-specific speculative decoding techniques across both common model-based approaches (DFlash, DSpark, EAGLE) and deterministic speculation using n-grams.

### Build Your Own Agent Harness with eve and Vercel
Speakers: Owen Kephart
Schedule: 11:40am - 12:40pm · Continental 4 (Workshop Room 2) · workshop
What does it take to build an agent that works across users, tools, and shared environments? In this hands-on workshop, we’ll introduce eve, Vercel’s agent framework, and explore the fundamentals of building your own agent harness. We’ll walk through the architecture behind multiplayer agents and how Vercel’s infrastructure fits together: Workflows for durable execution, Sandbox for isolated code execution, and AI Gateway for model access. Then we’ll put these concepts into practice through a guided exercise you can adapt to your own use case. You’ll leave with a practical understanding of the pieces behind an agent harness and a starting point for building and running your own agents on Vercel. Bring your laptop for the hands-on portion.

### What Runs Where: The State of Local AI
Speakers: Ahmad Osman
Schedule: 11:40am - 12:40pm · Continental 6 (Workshop Room 3) · workshop
A look at where local AI stands today and where it might be headed. Drawing on experiences with models, hardware, and the people building with them, this session explores what’s changing, what’s becoming possible, and how local AI fits into the broader AI landscape.

### Closing the Agentic Loop: Getting Agents to Safely Build, Verify, and Ship
Speakers: Kent C. Dodds
Schedule: 11:40am - 12:40pm · Continental 7–9 (Workshop Room 4) · workshop
Agents can write code. That's not the hard part anymore. The hard part is trusting what they ship. In this hands-on workshop, I'll show you the loop I run every day: agents safely build, verify, and deploy the outcomes I want, and that loop is hooked up to signal (my own ideas, user feedback, bug reports, and friction) so it keeps itself going. I haven't read 1% of the code in my product, and agents author and merge most of the PRs. That only works because of the system around them. We'll start by running autopilot (npx kcd-skills@latest autopilot) on a real repo, yours if you want, and use the questions it asks to lay the foundation: invariants, decision records that say when it's OK to change them, a primitives catalog, and an AGENTS.md that's a router, not a novel. Then we'll get into verification. That means separate reviewer agents, PR templates that have you review systems instead of code, cloud agents with their own computers that show their work, and a control CLI your agents maintain for themselves. Finally, we'll limit the blast radius with feature flags, health checks, and backups you've actually restored, and wire up the loops that keep it all moving. Bring a laptop and a repo you own. What you'll walk away with: - An autopilot plan for your own repo, with each step your agents can take on next - A primitives catalog and invariants your agents actually follow - A PR template built around intent, one-way vs. two-way doors, and system diagrams, so you review systems instead of code - A verification setup: an AI reviewer, agents that test the running app, and a control CLI they maintain - A blast-radius checklist: flags with an owner, a metric, and a removal condition, health checks after deploy, and tested restores - The loops that keep it going: bug reports, user feedback, friction, and nightly cleanup Prerequisites: nothing to install ahead of time, but a good internet connection matters. To follow along on your own code, bring a laptop with a coding agent you already use (Cursor, Claude Code, Codex, etc.) signed in, plus a GitHub repo you own and can open pull requests on.

### Proactive Agent Engineering
Speakers: Sydney Runkle
Schedule: 12:10pm - 12:35pm · Continental 1–3 (Workshop Room 1) · workshopTalk
We’ve seen a shift in the architecture of bleeding edge agents, motivated by the design of popular personal agents like Muse and Instinct. The latest agents run in the background and make progress on much larger goals. These proactive agents use primitives like schedules and event triggers, async subagents, browser use, and integrations with Slack and other messaging channels. Perhaps most importantly, they all have robust memory systems, which I’ll argue are the key to hitting the Goldilocks standard for proactivity.

### Lunch
Schedule: 12:40pm - 1:50pm · Continental 5 (Breakfast & Lunch) · other
No description published; title, speakers and schedule only.

### What It Takes to Run a Company on Agent Swarms
Speakers: Karan Vaidya
Schedule: 1:50pm - 2:15pm · Continental 1–3 (Workshop Room 1) · workshopTalk
How harness evolved from code to Knowledge work

### AFK Engineering: From Terminal to Voice-Controlled Remote Agents (Part 1)
Speakers: Philipp Schmid, Thor Schaeff, Ivan Leo
Schedule: 1:50pm - 2:50pm · Continental 4 (Workshop Room 2) · workshop
You will move from local coding in Google Antigravity to building a sandboxed remote agent on Gemini Managed Agents with reusable skills, vaulted credentials, and remote MCP. From there, you will connect the Gemini Live API to trigger remote tasks and steer your agents by voice.

### A Field Guide to Agent Shapes: From Long-Horizon to Open-Ended
Speakers: Yacine Mahdid
Schedule: 1:50pm - 2:50pm · Continental 6 (Workshop Room 3) · workshop
Agents in 2026 split into a bunch of distinct shapes like externalized context with RLMs, agents messaging each other, harnesses the agent rewrites itself, sandboxes, orchestrators with sub-agents, and brute-force recombination. This talk goes through what each one helps with, then looks at three real deployments in industries/domains generally lagging in AI adoption that reused some of these patterns. We finish on where this is heading in 2027 with models that edit their own context, tweak other networks, get trained for exploration earlier, and learn continuously from tasks they generate themselves.

### Keep the Harness, Own Your Inference
Speakers: Francisco Javier Arceo
Schedule: 1:50pm - 2:50pm · Continental 7–9 (Workshop Room 4) · workshop
Claude Code without Claude. Codex without an OpenAI model. We’ll put both harnesses to work on a real codebase with open-weight models running on a DGX Spark. They’ll inspect the repository, change code, and test their work. The terminal experience stays familiar. The entire stack runs on hardware you control. Drawing on our work building vLLM Agentic API, we’ll show how we’re bringing familiar coding harnesses to inference engines and distributed serving stacks including vLLM, SGLang, NVIDIA Dynamo, and llm-d. The goal is to make the harness, model, and serving infrastructure independent choices. With Codex Cloud, the coding harness itself runs remotely. Behind that harness, the Responses API adds another layer of agentic execution: the server can manage conversations, execute tools, and retrieve context. We’ll open up that machinery and explore how responsibility gets divided between the harness and the agentic server. Drawing on our work building vLLM Agentic API, we’ll dig into conversation state, memory through retrieval and file search, and compaction: what the agent remembers, how it finds what it needs, and what survives when its context fills up. As more of the agent runs on servers, owning your inference means understanding—and controlling—this execution stack. You’ll leave with the setup and verification steps to run your own coding agent backend—from a DGX Spark on your desk to a shared GPU cluster. Choose the model, choose the engine, and scale the infrastructure while keeping the coding tools you already use. Key takeaways - Run it locally: connect Codex and Claude Code to open-weight inference on an NVIDIA DGX Spark. - Take it to a cluster: connect the same agent-facing API layer to distributed serving with llm-d or NVIDIA Dynamo. - Make the whole session work: preserve conversation history, tool handoffs, and streaming across backends, then verify the result through a completed coding task.

### The new job of the data team is providing context to AI
Speakers: George Fraser
Schedule: 2:20pm - 2:45pm · Continental 1–3 (Workshop Room 1) · workshopTalk
Business intelligence is dead; long live context! The new job of every data team is to provide context to AI, so that when your head of sales asks “give me your 3 best ideas for improving pipeline conversion”, it gives 3 great answers grounded in accurate, correct queries. The tools for providing this solution are the same tools you know and love: AI is just a new consumer of the data stack. Fivetran + dbt labs CEO George Fraser will take you through how real users solve this problem today, and demo live how to connect AI to real data.

### Building a Shared AI Assistant: The Platform Challenges Beyond MCP
Speakers: Utkarsh Shrivastava
Schedule: 3:00pm - 3:25pm · Continental 1–3 (Workshop Room 1) · workshopTalk
Two years ago, teams asked our platform team to connect their data to an AI assistant. Today they ship their own MCP servers in a week. That speed is a win, and it swaps one engineering problem for a harder one: how do you decide what gets through, what gets gated, and who owns the gates? This talk gives you a way to answer that — what stays team-owned, what becomes shared platform, and how to tell whether consolidating actually helped. At Netflix, bringing these tools together creates real value. Functions like Finance and Talent can now connect information that previously lived in separate systems. A business user can ask a question in one place instead of taking it to three teams. But that same reach creates ambiguity. Multiple tools expose different versions of the same entity, or claim to answer the same question. As the catalog grows, the assistant has more ways to choose incorrectly. Sometimes a data-owning team discovers that another team has built on its data only when an evaluation fails. How do you build a shared AI assistant that brings tools and data from across a company into one place? At Netflix, product teams increasingly build their own MCP integrations. Our challenge is making those capabilities work together so employees can get answers across teams through a single assistant. This talk covers the decisions and mechanisms behind that shift: connector certification, an internal benchmark built from real employee queries that we use to evaluate routing between overlapping tools, and how we classify actions to separate what an agent can do on its own from what needs a person first. We'll examine where our initial domain boundaries broke down, what required agreement between teams, and why better tool descriptions alone couldn't resolve the conflicts. We'll close on what we haven't solved: who owns the authoritative version of an entity, how to retire a connector other teams depend on, and when the benefits of a shared capability justify the coordination it requires.

### AFK Engineering: From Terminal to Voice-Controlled Remote Agents (Part 2)
Speakers: Philipp Schmid, Thor Schaeff, Ivan Leo
Schedule: 3:00pm - 4:00pm · Continental 4 (Workshop Room 2) · workshop
You will move from local coding in Google Antigravity to building a sandboxed remote agent on Gemini Managed Agents with reusable skills, vaulted credentials, and remote MCP. From there, you will connect the Gemini Live API to trigger remote tasks and steer your agents by voice.

### Hands-on Gitar: An AI Code Verification Agent for Your CI
Speakers: Taylor Luttrell-Williams
Schedule: 3:00pm - 4:00pm · Continental 6 (Workshop Room 3) · workshop
Gitar is Sonar’s AI code verification agent, complementing SonarQube with an understanding of each change’s context and intent. In this hands-on workshop, you’ll install Gitar as a GitHub App and use it across three pull request scenarios that show how verification goes beyond code review. Gitar verifies every change against your project's context and rules, catches problems, generates working fixes, and iterates until your CI pipeline passes. You'll leave knowing how to set up Gitar on your own repositories. You'll also see how it delivers ready-to-merge, green PRs with high signal and low noise, while your team keeps control.

### Build a personal agent with Exa Search
Speakers: Jakub Hojsan
Schedule: 3:00pm - 4:00pm · Continental 7–9 (Workshop Room 4) · workshop
A personal agent gets asked everyday questions: where to eat near the office that's open late, whether it will rain on Saturday, how the Warriors did last night, what a stock did this week. Exa answers all of these through one search call. Places come back with addresses, hours and reviews; weather comes back as daily forecasts; sports come back as scores, standings and schedules. You don't need a separate API for each. In this session, Jakub Hojsan, forward deployed engineer at Exa you show you how to build a personal agent on Exa search that handles a day's worth of real requests, from finding dinner to planning around the weather. We will provide a repo to work out of as part of this workshop.

### Building World-class Agentic GTM: Learnings from Monaco for Monaco
Speakers: Mihail Eric
Schedule: 3:30pm - 3:55pm · Continental 1–3 (Workshop Room 1) · workshopTalk
Building a custom agents platform is one of the key pieces to unlocking AI for complex verticalized business workflows. Monte Carlo is the sales-specific system we've built to help scale Monaco's revenue: a platform where revenue teams encode their own playbooks as agents that run against everything we've ingested about their business, including pipeline, outbound, calls, and the CRM. Sales is a particularly complex vertical for the following reasons: no two revenue orgs look alike, the data is large and heterogeneous, and the expertise that matters lives in per-rep workflows nobody has written down. Over the last 2 years, we’ve built a custom harness and orchestration system to power our world-class GTM team. In this talk, I'll break down the components a verticalized agent platform needs in order to be fast and correct, including an execution plane, memory and curated implicit and explicit context, how expertise gets represented, and the evaluation loop, along with what is still unresolved.

### Networking Break
Schedule: 4:00pm - 4:30pm · Continental Foyer · other
No description published; title, speakers and schedule only.

### Multiplayer software factories - Leading the shift to concurrent delivery
Speakers: Patrick Debois
Schedule: 4:30pm - 4:55pm · Continental 1–3 (Workshop Room 1) · workshopTalk
Your whole team runs coding agents now, and they all land on one main. Continuous delivery wasn't built for that. This talk maps what breaks when a software factory goes multiplayer, and the patterns that fix it: one main for the agents, one board for the people.

### Our Agents Shipped 6,000 PRs to 600+ Companies in The First Month. Now They Build Features
Speakers: Alex Lebedev
Schedule: 4:30pm - 5:30pm · Continental 4 (Workshop Room 2) · workshop
PostHog Self-driving wrote 6,000+ pull requests in its first month that 600+ companies chose to merge. We showed the signal-to-PR pipeline at AI Engineer in London this April, and released it in late June. I'll show what happened since: where agents overreached, what we threw away, what's still science fiction, and the jump from fixing bugs to building features. The system now pitches features backed by your product data, builds them, and reviews them paranoidly, testing like a real customer. All open source. Real PRs, real reviews, real failures, shown live.

### Do it All with Devin
Speakers: Giovanni D'Antonio, Charlie Meyer
Schedule: 4:30pm - 5:30pm · Continental 6 (Workshop Room 3) · workshop
What is the future of post training in coding. What a modern research team looks like, and how Devin is part of it.

### Build your first Kiro Crew app: An agent that triages your backlog while you sleep
Speakers: Arundeep Nagaraj, Dan Kiuna
Schedule: 4:30pm - 5:30pm · Continental 7–9 (Workshop Room 4) · workshop
Most people meet AI agents as a chat bot. In this hands-on workshop you will build one that works while you are not watching. Starting from an empty directory, you will install Kiro Crew, an open-source orchestration layer for coding agents, and ship a working app: an agent that reads your repository’s open issues, finds the duplicates, explains why it thinks so, and posts its findings on a schedule. Along the way you will give the agent persistent memory so it stops re-reading what it already knows, fan the work out across background subagents so a thousand issues do not take a thousand turns, and set the boundary that decides what it may and may not touch. Bring a laptop and a GitHub repository you care about. You will leave with the app running, and with a clear picture of what separates a demo from something you would actually let run unattended.

### Warning: This Pull Request Contains Graphic Content
Speakers: Stephen Chin, Cassandra Chin
Schedule: 5:00pm - 5:25pm · Continental 1–3 (Workshop Room 1) · workshopTalk
AI coding agents can turn a small feature request into a substantial code change and a pull request description that reads like a short novel. Yet the decisions, failed experiments, and human interventions that shaped the result remain buried in agent sessions. Reviewers reconstruct the history, question unsupported claims, and send the PR back for another costly round. Compressing the context into fewer tokens still leaves them searching for the missing connections. TraceToon uses that history to create better PR descriptions and comics grounded in the work behind the diff. With Relate, an embedded, in-memory graph database, TraceToon connects prompts and decisions to code changes and verification runs. It retrieves the evidence neighborhood around each change and turns it into a focused brief for drafting and review. The comic makes the wrong turns and corrections visible, while the technical description explains the behavior, rationale, and checks that support the result. Following a real pull request from Claude Code, Codex, or Antigravity sessions to a finished PR and comic, we’ll show how the graph keeps the story honest: connecting sessions to branch changes, distinguishing an earlier passing test from validation of the submitted code, and preserving uncertainty when evidence is incomplete. We’ll also show how connected evidence, a tuned brief, and cost-effective reviewers work together to improve PR quality and lower total drafting cost in our benchmarks. Attendees will leave with an open source workflow and practical patterns for using graph context and visual storytelling to make agent work easier to understand and review.

### MC Outro
Speakers: Richelle Ji
Schedule: 5:25pm - 5:30pm · Continental 1–3 (Workshop Room 1) · workshopTalk
No description published; title, speakers and schedule only.

### Opening Reception
Schedule: 5:30pm - 8:30pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

## Nov 11
### Token Billionaires Lounge
Schedule: 8:00am - 5:40pm · Continental 7 (Token Billionaires Lounge) · other
No description published; title, speakers and schedule only.

### Registration
Schedule: 8:00am - 5:40pm · Registration (outside Golden Gate) · other
No description published; title, speakers and schedule only.

### MC Intro
Speakers: Corey Quinn
Schedule: 9:00am - 9:10am · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### What Will You Build When AI Is 10x Faster?
Speakers: Natalie Serrino
Schedule: 9:10am - 9:30am · Continental 4–6 (Mainstage) · talk
Many AI product decisions are influenced by how long someone will wait for an answer. Do you give an agent another pass to check its answer, or make it respond faster? Can your voice assistant finish reasoning before the pause gets awkward? Faster inference gives developers the option to build smarter, more responsive user experiences. We’ll look at what faster inference lets you build, from more responsive voice applications to agents that can try, test, and update within a few seconds. We’ll discuss when speed is worth paying for, when other parts of your application become the bottleneck, and how to use higher responsiveness. Along the way, we’ll share how Gimlet combines GPUs and specialized accelerators to make inference faster, and what that means for the developers using that speed.

### Rethinking Claude Code Best Practices
Speakers: Lydia Hallie
Schedule: 9:30am - 9:50am · Continental 4–6 (Mainstage) · talk
The models have gotten really good, and most of what we've added to our Claude Code setups over the past year is now holding them back. In this talk I'll go through what Claude Code best practices look like for the Claude 5.5 models, what's still worth keeping, and what you no longer need to think about.

### cloudflare is a neolab
Speakers: Michelle Chen
Schedule: 9:50am - 10:10am · Continental 4–6 (Mainstage) · talk
we trained some new system one models (clef, clairic). they fit perfectly within our decade-old primitives like workers, our edge latency hypothesis for workers ai, and our ambition to be the agent cloud.

### All Code Is Slop (Except Mine)
Speakers: Lauren Tan
Schedule: 10:10am - 10:30am · Continental 4–6 (Mainstage) · talk
The Grok Bot team at SpaceXAI lands hundreds of PRs a day. Nobody reads them all, yet quality goes up anyway. In this talk, we'll find out how the Grok Bot team turns slop into gold at an incredible pace.

### MC Outro
Speakers: Corey Quinn
Schedule: 10:30am - 10:40am · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### Expo Hall Hours
Schedule: 10:40am - 4:00pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### Networking Break
Schedule: 10:40am - 11:20am · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### Manage Yourself Out of the Loop
Speakers: Erik Thorelli
Schedule: 10:55am - 11:15am · Continental 1–3 (Expo Sessions) · breakout
More coding agents mostly means more tabs to watch. In the past year, one of our engineers went from about 20 merged pull requests a month to nearly 7,000. I'll show what we changed in our repos so an agent can take one small feature from prompt to merge on its own.

### I deleted 90% of my harness (And It Got Better)
Speakers: Philipp Schmid
Schedule: 11:20am - 11:40am · Continental 4–6 (Mainstage) · talk
Alt Title: Why Models Are Superhuman with Bash (Where Humans Fail) --- I spent my day to day building a agents with custom tools for everything. Every few month I decide to delete everything and see what is not needed anymore. I stripped out every dedicated tool until only Bash remained. I cut the prompt to 300 tokens and made the execution loop asynchronous. Benchmark scores jumped. Experience went up. Rich Sutton called this the Bitter Lesson: building human heuristics into AI always loses to general methods backed by compute. Models are now superhuman with the bash. A frontier model can synthesize an ad-hoc 15-line pipeline combining Python AST parsing, ripgrep, git diffs, and subshells in 200ms to make progress on a users task, there is no need for dedicated edits, search or grep tools anymore. Learn how to delete your code.

### Refactor or Rot: Building a self-improving codebase
Speakers: Jacob Prall
Schedule: 11:20am - 11:40am · Continental 1–3 (Expo Sessions) · breakout
Your coding agents run in loops: plan, implement, test, repeat. This inner loop focuses on completing a task, and it tends to get all the attention. But there’s an outer loop, too. Each agent builds on the codebase the last one left behind, inheriting its patterns, abstractions, and shortcuts. Those patterns can make the codebase easier to understand, maintain, and extend, or compound complexity and make future changes riskier. In this talk, I’ll show you how to build an outer loop that reinforces code quality and counteracts decay. Drawing on classic software design and refactoring techniques, we’ll equip an agent with skills to identify code smells, reason about coupling and module boundaries, and recommend refactors that make future changes easier. We’ll wire that analysis into the development lifecycle, running on PRs and across the codebase, weighing each recommendation’s benefit against its cost and risk. You’ll learn when to refactor, when to leave working code alone, and how to make refactoring part of your development workflow, so your coding agents leave behind codebases that are better, not just bigger.

### The Rise of the Agent Workforce: Rethinking Agent Infrastructure
Speakers: Ankit Mathur
Schedule: 11:45am - 12:05pm · Continental 4–6 (Mainstage) · talk
The next generation of agents won't just answer questions. They'll work autonomously, collaborate with other agents, and learn from experience. As we move from interactive chatbots to persistent agent workforces, the infrastructure powering them needs to fundamentally evolve. In this talk, we'll explore the emerging architecture of agentic systems, from stateful sandboxes and persistent memory to agent communication and orchestration. We'll examine why today's agent platforms aren't built for this future, and what it will take to power a world where teams of agents can tackle complex, long-running work together.

### Heal Your Agents, Don't Just Grade Them
Speakers: Khasimul Asif Mohammad, Sudhir Tonse
Schedule: 11:45am - 12:05pm · Continental 1–3 (Expo Sessions) · breakout
Your evals are green, and users are still hitting failures. The evals aren't wrong. They test what you anticipated, and production at millions of sessions a day keeps inventing failures nobody wrote a test for, many visible only as a pattern across sessions. Detecting those failures continuously is a hard problem in its own right. Every agent fails differently, the failures that matter are rare, and a detector that flags everything is as useless as one that flags nothing. We've been working on this with customers running agents at scale and by running it on our own agents, learning which failures are worth surfacing and which are just noise. Along the way, three engineering problems kept coming up: Economics: you can't afford to run a reasoning model over every session, so what do you screen with, and what earns a closer look? Noise: a thousand flagged sessions are usually a handful of root causes. How do you collapse them and decide which to fix first? Trust: when a coding agent proposes the fix as a pull request, what has to be true before you merge it? How do you verify each fix and expand to cover every failure you find so it stays caught? You'll leave with the tradeoffs that matter when you move from grading agents to healing them, drawn from teams doing it today

### Building a Safe Software Factory
Speakers: Andrew Finch
Schedule: 12:10pm - 12:30pm · Continental 4–6 (Mainstage) · talk
Coding agents have made code cheap to write, and teams are shipping 10× more changes than they did two years ago. Human review was built for human speed, so the industry is moving from reviewed PRs to automated software factories. At Gitar and Sonar, we are learning how to build a safe software factory, with layers of verification across the system. We'll share what we've been learned so far, and where we think this trend is headed.

### How to build agents over your own data
Speakers: Aamir Shakir
Schedule: 12:10pm - 12:30pm · Continental 1–3 (Expo Sessions) · breakout
The biggest bottleneck to building powerful internal agents is giving them the right organizational context. When agents can reliably find that context, they can answer questions, review code, investigate incidents, and automate workflows across the company. But company knowledge is scattered across Slack, email, Google Drive, code repositories, Linear, internal documentation, and multiple versions of the same information. Putting everything into the model’s context is expensive, risky, and often reduces answer quality. Connecting every source through separate MCP servers creates another bottleneck: the agent must make numerous tool calls while inheriting each service’s latency, rate limits, and uneven search quality. This talk shows how to separate retrieval from reasoning by giving internal agents a unified search layer for company knowledge. We’ll explore how a search subagent breaks down complex tasks, combines semantic and exact retrieval across systems, preserves source permissions, verifies freshness and versions, and returns compact, cited evidence to the acting agent. Through realistic internal workflows, we’ll demonstrate how better retrieval makes agents more accurate, traceable, and useful while reducing tool calls, latency, and cost.

### Earning Autonomy: From Missions to Workstreams
Speakers: Luke Alvoeiro
Schedule: 12:35pm - 12:55pm · Continental 4–6 (Mainstage) · talk
Seven months ago, Factory introduced Missions, an orchestrator that ran worker agents through a full project with validation at every milestone. Real customer projects showed its limits. It only handled code, it was built for older models, and its context belonged to one person instead of the team. Luke Alvoeiro explains how Factory rebuilt it. A more token-efficient Droid made running many agents affordable. Environments let agents scale out inside a customer's own VPC. The new Missions gives each project a long-lived home with one orchestrator, shared context, and more autonomy as validation earns trust. When a project moves into maintenance, its mission graduates into a workstream: agents that turn bug reports, alerts, and ideas into validated, shipped software.

### The Software Factory That Needs Zero FDEs
Speakers: Raz Berman Gold
Schedule: 12:35pm - 12:55pm · Continental 1–3 (Expo Sessions) · breakout
Working alone with Claude feels like a superpower. You open a session, give it the right context, and watch it ship. Scaling that to a whole engineering org is where it breaks. One agent with more context, more tools and more responsibility starts drifting, costs climb, and nobody can tell which part failed. So most "AI software factories" quietly ship with a team of forward-deployed engineers who wire up every customer by hand. We built Overcut so a factory doesn't need them. Instead of one big agent, it uses small agents with clear jobs: triage, root-cause analysis, implementation, code review and verification. Each one has its own context, model and memory, so it can be measured and improved on its own. Orchestration connects them. Workflows react to events in GitHub, Jira and Slack, run in parallel, and stop at human approval gates where it matters. Because every piece is a reusable building block, teams assemble their factory from ready-made parts instead of waiting for someone to build it for them. Then we'll prove it live. Starting from an empty project, we'll build the factory on stage: a production alert in Slack becomes a Jira ticket with a root-cause analysis, the ticket becomes a pull request, and the PR is reviewed and fixed until it's ready to merge. No FDEs, no hand-wiring. You'll leave with architecture patterns you can apply tomorrow , whether you're one developer or rolling out agents across a whole company.

### Lunch
Schedule: 12:55pm - 2:05pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### I love you so jevving much
Speakers: Diogo Almeida
Schedule: 2:05pm - 2:23pm · Continental 4–6 (Mainstage) · talk
Let's talk about the state of AI, how something like jev stayed under the radar for years, how we made it, and most importantly: what comes next! I've been told that this crowd is the absolute best of any conference for building the future, so let's jam about sci-fi and finally build some sick smart software.

### Coding Agents and How to Tame Them
Speakers: Ivan Leo
Schedule: 2:05pm - 2:25pm · Continental 1–3 (Expo Sessions) · breakout
Coding agents are remarkably capable one minute and burning 50,000 tokens in a broken loop the next. Over the past few months at Google DeepMind, I've worked with Kaggle to audit over 50 coding benchmarks trace by trace and build a platform to evaluate frontier agents at scale. In this short 18-minute talk, we'll cover the weird failure modes we caught in the wild, the lessons we learned building air-gapped sandboxes, and how to take those same lessons to design better harnesses, verifiers, and coding environments for your own agents.

### Beyond Generation: Fast, Structured AI Decisions with Jev at Glean
Speakers: Chinmay Goyal
Schedule: 2:30pm - 2:43pm · Continental 4–6 (Mainstage) · talk
Not every step in an AI product needs a full generative LLM call. Many are bounded decisions, like understanding what a user is asking for, picking the best suggestion to show, checking whether an answer's citations hold up, routing to the right tool or model, or deciding if a request needs a guardrail. In this session, I'll walk through how Glean has been exploring Jev across these decisions, what we learned about where fast, confidence-scored decisions shine, and how we evaluate these models before they reach users.

### More Checks, Less Noise: Layered Security for AI-Assisted Development
Speakers: Taylor Luttrell-Williams, Killian Carlsen-Phelan
Schedule: 2:30pm - 2:50pm · Continental 1–3 (Expo Sessions) · breakout
More security checks should mean more confidence, not more alerts to ignore. As AI accelerates code production, how do we add independent verification without turning development into an obstacle course? This session explores two dimensions of application security: using complementary analysis methods and placing checks at useful points throughout the software development lifecycle. We’ll examine where deterministic analysis provides repeatable checks, where probabilistic, AI-powered review can add context-sensitive reasoning, and why simply stacking tools can create more noise than assurance. We’ll start with a vendor-neutral framework for choosing checks, prioritizing findings, and keeping review actionable. Then, a live demo will bring three complementary approaches together: static application security testing (SAST), software composition analysis (SCA), and AI-powered analysis of logic-level vulnerabilities. You’ll leave with a practical way to evaluate layered verification: what each check contributes, where it belongs, and how to turn its findings into manageable work rather than another queue of alerts.

### Your Automation Is Overthinking It
Speakers: Chibi Vikram, Kevin Bernstein
Schedule: 2:48pm - 3:01pm · Continental 4–6 (Mainstage) · talk
Enterprise automation gets hard to maintain when a single agent is responsible for understanding a request, finding evidence, and deciding what happens next. Drawing on two decades of experience automating business processes, we'll show how to break that work into steps a team can understand, test, and change. We'll explore when a focused judgment is enough, when a generative model should investigate, and when a person should step in. We'll share what we learned about accuracy, speed, and cost so you can make those choices in your own workflows.

### Ground Truth or Dare: Using Oracles to Make Postgres Reactive
Speakers: James Arthur
Schedule: 2:55pm - 3:15pm · Continental 1–3 (Expo Sessions) · breakout
Live SQL is the holy grail of realtime. Subscribe to any SQL query, with joins, aggregates and ordering, and the result stays live as your data changes. It’s easy to describe but very hard to build. At Electric, we spent years chasing it. Then we joined Neon and built it in weeks with coding agents, inside Postgres. Live queries are database infrastructure. This isn’t code you hand to an agent and hope for the best. So we used Postgres’s own query engine as an oracle. Once the agents had the ability to verify their own work, they could go super fast and burn down through the featue requirements. In this talk, I’ll cover what we built, how we built it and how oracles let us have both truth and dare: to get it right and ship fast with agents.

### Your Judge Is Hallucinating Too
Speakers: Brian Kennedy
Schedule: 3:06pm - 3:19pm · Continental 4–6 (Mainstage) · talk
Every step an agent takes in ZoomInfo's Agent Teams is graded by another model. Then we ran Jev beside it and found the grader was passing work that never happened. This talk is about what we found, what we replaced, and why "did the agent do a good job?" is the wrong question to ask a model.

### CVE remediation with Factory: from finding to merged PR
Speakers: Nikhil Harithas
Schedule: 3:20pm - 3:40pm · Continental 1–3 (Expo Sessions) · breakout
Description TBD

### Autocomplete for Actions: System One from the UI to the DB
Speakers: Scott Roberts
Schedule: 3:24pm - 3:37pm · Continental 4–6 (Mainstage) · talk
Search guesses your next word. Workday's Sana guesses your next task. Millions of people use Workday to check their pay, book time off and find their team, and most of those requests are too simple to wait on a full LLM turn. I'll show how we use Jev as a System One model from the UI to the DB: picking the right action card while you type, and running inside DuckDB as a SQL filter.

### Leaving Localhost: Building an Agent-Native Dev Environment
Speakers: Sajid Mehmood
Schedule: 3:45pm - 4:05pm · Continental 1–3 (Expo Sessions) · breakout
Why is it that Anthropic can port Bun from Zig to Rust in 11 days, while most teams still struggle to make sweeping changes to production software? Bun is complex, but it turns out its verification loop is actually quite clear: there's a well-defined TypeScript spec, and a huge battery of tests the agent can iterate against. This talk will explore techniques to build agent-native dev environments in the cloud that allow for these kinds of tight verification loops for software that's traditionally much harder to verify: tax accounting, vertical AI agents, robotics control systems, etc. We'll discuss how to manage stateful dependencies (databases, queues, caches), third-party services, and seed data so you can focus on architecture & product while your agents handle implementation & testing in the cloud.

### Afternoon Break / Keynote Reset
Schedule: 3:45pm - 4:05pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### MC Intro
Speakers: Corey Quinn
Schedule: 4:20pm - 4:30pm · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### What it takes to set intelligence free
Speakers: Fabian Hedin
Schedule: 4:30pm - 4:50pm · Continental 4–6 (Mainstage) · talk
Models keep getting better and the systems we build around them need to keep up. This talk goes inside Lovable’s engineering: forkable computers that give agents room to experiment, persistent histories that let them continue longer work, and durable communication that lets them coordinate. We’ll explore what it takes to give agents more independence, and how these foundations could help them build, ship, learn from feedback, and keep improving a product.

### How to build an agent that builds the culture
Speakers: Zach Bruggeman
Schedule: 4:50pm - 5:10pm · Continental 4–6 (Mainstage) · talk
Ramp built its own coding agent, Inspect, which writes ~75% of merged PRs. At the start of 2026, the technology was the novel part, but today, it's commonplace. In this talk, Zach will talk about how Inspect has evolved this year, and re-shaped the culture of engineering at Ramp around agent-driven development.

### Software Factories: Escape from Trash Mountain
Speakers: Steve Yegge
Schedule: 5:10pm - 5:30pm · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### 2026 in LLMs
Speakers: Simon Willison
Schedule: 5:30pm - 5:50pm · Continental 4–6 (Mainstage) · talk
2026 has been a wild year for LLMs. Simon will recap everything that's happened since last November's coding agent inflection point: January's OpenClaw craze, the rise and fall of tokenmaxxing, US export controls on frontier AI, open weights that can compete with the best, cyberattacks by rogue agents, Fable-class models, and the recent wave of 3D modeling and vibe-coded games. And the year's not over yet!

### MC Outro
Speakers: Corey Quinn
Schedule: 5:50pm - 6:00pm · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

## Nov 12
### Token Billionaires Lounge
Schedule: 8:00am - 5:40pm · Continental 7 (Token Billionaires Lounge) · other
No description published; title, speakers and schedule only.

### Registration
Schedule: 8:00am - 5:40pm · Registration (outside Golden Gate) · other
No description published; title, speakers and schedule only.

### MC Intro
Speakers: Corey Quinn
Schedule: 9:00am - 9:10am · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### Ambition in AI
Speakers: Jason Liu
Schedule: 9:10am - 9:30am · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### The Software Atelier
Speakers: Armin Ronacher
Schedule: 9:30am - 9:50am · Continental 4–6 (Mainstage) · talk
On the way to the software factory, let's build an atelier first. Drawing on the last year of working with and on Pi, this talk argues for using our new tools to craft better software, not just more of it.

### Software Engineering Is Becoming Factory Engineering
Speakers: Zach Lloyd
Schedule: 9:50am - 10:10am · Continental 4–6 (Mainstage) · talk
Warp founder and CEO Zach Lloyd explores the rise of software factories: systems that coordinate AI agents across the entire development lifecycle, from triage and specification to implementation, review, and monitoring. He’ll explain how engineering teams can build factories that improve with every run, where human judgment remains essential, and why the next frontier of software engineering may be less about writing code and more about engineering the systems that build it.

### Let's Open Source the World
Speakers: Brandon Thomas
Schedule: 10:10am - 10:30am · Continental 4–6 (Mainstage) · talk
From open-source alternatives to Adobe Photoshop and Microsoft Office to the SaaSpocalypse, it’s clear that software’s moats aren’t where they used to be. Take a look inside ArtCraft, a project aiming to become the Wikipedia of open source by recreating every category of software in modern, high-quality Rust. We’re building open-source applications and infrastructure to make every platform open - tearing down moats by turning platforms into protocols. We’ll tour fully agentic software factories and the engineering behind them - pushing the limits of Git and GitHub, tackling Rust build and CI bottlenecks, automating triage and testing, and building high-quality shared libraries and UI/UX components for the interfaces and user experiences of today and tomorrow, and beyond.

### MC Outro
Speakers: Corey Quinn
Schedule: 10:30am - 10:40am · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### Expo Hall Hours
Schedule: 10:40am - 4:00pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### Networking Break
Schedule: 10:40am - 11:20am · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### A New Age of Software Engineering
Speakers: Walden Yan
Schedule: 11:20am - 11:40am · Continental 4–6 (Mainstage) · talk
Skip the basics and go straight to the frontier. Walden Yan, cofounder and CPO of Cognition, dives into the most advanced ways teams are using AI today, with bleeding-edge techniques from real company use cases.

### Connect Agents to Reality: The Context Engine Powering Your Software Factory
Speakers: Brandon Waselnuk
Schedule: 11:20am - 11:40am · Continental 1–3 (Expo Sessions) · breakout
Our goal is to drive business outcomes and increase shareholder value. We do it through code. Increasingly agents are writing more, if not all, of our code and running more of the SDLC through software factories. Unfortunately they keep getting things wrong, are misaligned, or hallucinate facts leading to wasted human and agent cycles. It doesn't have to be this way. By connecting agents to the reality of your business through a context engine you can improve every step of your factory. This drastically increases the quality of agent outputs which compounds into driving the business outcomes and value we dream of. In this talk I'll show: how to accomplish this, why context != context, and 3 lessons we learned delivering a context engine at scale in case you want to build your own. Whether you believe one agent can run it all or a bespoke software factory is the right approach, you'll discover that ambient context is what your system is missing.

### What Your AI Doesn't Know: The latest trends in agent searches
Speakers: Jeffrey Pinner
Schedule: 11:45am - 12:05pm · Continental 4–6 (Mainstage) · talk
An agent only searches when it doesn’t know something. In other words, every search is a confession, and Exa has been collecting them from thousands of agents for two years. Read together, those searches form a map of how AI agents like to work, and where their knowledge ends. There’s clear evidence of growing expertise. Coding agents used to search for examples and tutorials, now they go straight to the source, searching for code repos, issues and API references. Searches for mature frameworks like React, Next.js, and the rest of the “vibe code stack” are fading, not because they’re falling out of use, but because models already know them cold. Instead agents are searching for their own tools: MCPs, skills, agent instruction files and the latest models. But even as their knowledge and capability grows, agents still need to search. Models still take months to train, but the coding frontier now turns over every quarter, and AI is speeding that up. This knowledge cutoff won’t be fixed by the next big model release. In this keynote, Jeff Pinner, CTO of Exa, shares what we’ve learned from agents telling us what they don’t know, what it means for anyone who maintains a library, ships an agent or relies on one, and why search is an Agent’s best gateway to the present.

### Talk But Verify: human-in-the-loop for agents that actually matter
Speakers: Michael Liendo
Schedule: 11:45am - 12:05pm · Continental 1–3 (Expo Sessions) · breakout
AI agents are getting good at taking action. The hard part isn't making them capable, it's knowing when to make them stop. In this talk we'll walk through the full spectrum of human-in-the-loop patterns, from lightweight inline confirmations to out-of-band permission gates to handing your agent a wallet with real money in it and more. Each pattern fits a different level of consequence, and knowing which to reach for is what separates demo agents from production ones. We'll cover the honest tradeoffs of latency, user experience, and trust so you can make the right call for your specific use case. The entire talk is built around various live demos that escalate in stakes with every step. You'll leave with a mental model and working reference architecture you can apply the same day.

### Ship more as a team with Kiro Crew
Speakers: Doug Clauson
Schedule: 12:10pm - 12:30pm · Continental 4–6 (Mainstage) · talk
Coding has gotten cheaper, but shipping hasn't. See how one engineer built a build, review, and ship loop with Kiro Crew, and learn the traps that cost hours along the way (reviews that never end, agent loops that balloon a ten-line fix into a whole subsystem, saying yes to everything because code felt free). You'll leave with five concrete habits to try Monday morning with the tools you already use.

### Let the Agent Cook: From APIs to Answers
Speakers: Arsalan Bashir
Schedule: 12:10pm - 12:30pm · Continental 1–3 (Expo Sessions) · breakout
Abstract: Give an agent a pile of APIs. Can it figure out what to query, connect the dots, and check its own answers? I’ll share practical lessons on building agents that explore data across services—from discovering tools and navigating schemas to following leads and knowing when they have enough evidence.

### Exploring Claude’s frontier
Speakers: Lance Martin
Schedule: 12:35pm - 12:55pm · Continental 4–6 (Mainstage) · talk
In this talk, we explore Claude’s frontier capabilities in memory and multi-agent coordination.

### Code review without reviewing code
Speakers: Daniel Tao
Schedule: 12:35pm - 12:55pm · Continental 1–3 (Expo Sessions) · breakout
While authoring code has become virtually instantaneous, reviewing and verifying that code in an enterprise environment remains constrained by human cognitive capacity. At scale, this becomes a painful bottleneck: pull request volume and size are growing rapidly, review latency is increasing, and 10,000-line diffs can all too easily burn through finite reserves of human attention. How do engineering organizations scale trust and quality at the speed of AI generation? I won’t pretend we’ve fully slain this dragon, but in this session I’ll walk through a few different approaches we’re taking and what we’ve learned within Atlassian: Inner Loop: Building confidence through automated local AI review and skills for catching anti-patterns and contract violations before code ever reaches a human teammate. Outer Loop: How tools like Taro spin up live environments, simulate user interactions, and provide tangible evidence (narrated videos) directly to reviewers. A New Lens on Code: Aggregating quality signals like CI, agentic evaluations, and risk scoring to allow reviewers to “zoom out” and reason about the value and implications of a change without having to read the diff line-by-line. Rethinking the Unit of Change: Why the traditional single-ticket micro-PR is an artifact of human typing limits, and how we can shift human expertise to where it matters most. Attendees will leave with concrete architectural patterns, lessons learned from real-world rollouts, and a blueprint for evolving their team’s code review practices for the AI era.

### Lunch
Schedule: 12:55pm - 2:05pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### Jarred Sumner, Founder of Bun, Anthropic / Bun
Speakers: Jarred Sumner
Schedule: 2:05pm - 2:50pm · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### Scaling Your Agent Workforce: Lessons from Inside Cognition
Speakers: Theodor Marcu
Schedule: 2:05pm - 2:25pm · Continental 1–3 (Expo Sessions) · breakout
Most companies have turned coding agents on. Few can say what those agents do or what they return. At Cognition, Devin wrote 92% of merged PRs in September, and 9 out of 10 Devin sessions start without a human. Theodor Marcu shows how we got there: cloud agents working in parallel, automations that run every night, and how engineering and research use Devin to autonomously drive feature development. He then turns that into a playbook for your teams: govern what agents can reach, route work across models to cut cost, and follow every session to a merged PR so ROI is measured instead of guessed.

### The first Grounded Decision Model
Speakers: Devin Gupta
Schedule: 2:30pm - 2:50pm · Continental 1–3 (Expo Sessions) · breakout
Decision models only read. They never generate a token, which is why they cost roughly 240x less per token read than a frontier LLM — and why they are only as good as the state you hand them. For most judgments worth making, that state lives on the live web, not in your database. This talk re-costs the stack with measured numbers. On PWS-Decisions, our open 300-question benchmark, the question is 104 tokens and the evidence needed to answer it is 4,777. Two years ago the model was 86% of the bill for a grounded answer; today it is 17%. Intelligence stopped being the bottleneck. Context became it. We will cover what that inversion changes architecturally, a live demo that grounds 18 typed questions against 4,270 businesses in a single call, and the entity-resolution failure that quietly breaks grounded decisions in production. You will leave able to run the benchmark against your own model.

### Judgement is the Last Job
Speakers: Ishaan Dey
Schedule: 2:55pm - 3:15pm · Continental 4–6 (Mainstage) · talk
If agents can build anything, what's left? Building Antigravity, we work at the frontier of AI, ship products at the scale of Google, and iterate quickly to harness new model capabilities. This talk dives into that feedback loop, and what that taught us about building with agents while keeping human judgement at the center.

### Your agent pays twice for every search: how we cut token spend by 90+% with better accuracy
Speakers: Louis Walsh
Schedule: 2:55pm - 3:15pm · Continental 1–3 (Expo Sessions) · breakout
Every agent that searches the web pays twice: once for the search call, and again for the tokens that search puts into the model's context. The answer is usually a few sentences. The agent pays for the whole page, and in a multi-step loop it pays for it again on every turn. We'll show real production traces of where the tokens go and why retrieval, not generation, is the biggest line on most agent bills. Then we'll show what we changed: return the passages a query needs instead of whole pages, tune extraction to the question, and cap how much context the agent can take. We tested this across 12 frontier models and 11,000 blind-graded answers. Token spend fell by more than 90% while accuracy went up. You get a metric (cost per correct answer, not cost per request), an open calculator to run the numbers on your own traffic, and a five-point checklist for finding token waste in your pipeline.

### Brownfield Factories
Speakers: Justin McCarthy
Schedule: 3:20pm - 3:40pm · Continental 4–6 (Mainstage) · talk
Brownfield applications are clearly ideal for Software Factories! Brownfield applications provide all the specification and telemetry you need to build validation harnesses and loops. Make a lump sum payment on your technical debt, reduce costs, increase performance, and purge vulnerabilities once and for all. Rewrite that boat anchor to Rust, Elixir or BF today!

### Agents That Don't Clock Out
Speakers: Erik Hanchett
Schedule: 3:20pm - 3:40pm · Continental 1–3 (Expo Sessions) · breakout
My coding agents are fast, but speed isn't the whole story. The real question is where they run: the CLI, the IDE, or something else entirely? In this session, I'll break down which tool fits which job and why that choice makes or breaks your workflow. I'll show you how I organize skills and custom agents so they're reusable instead of one-off, then close with a demo of a persistent agent setup in Kiro Crew — one that keeps grinding away long after I've logged off. Walk away knowing how to match the right agent to the right environment and build setups that work while you sleep.

### Afternoon Break / Keynote Reset
Schedule: 3:45pm - 4:05pm · Golden Gate (Expo Hall, Lunch & Reception) · other
No description published; title, speakers and schedule only.

### MC Intro
Speakers: Corey Quinn
Schedule: 4:20pm - 4:30pm · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### Post-Training Gemini 4 for Real Engineering Work
Speakers: Melvin Johnson
Schedule: 4:30pm - 4:50pm · Continental 4–6 (Mainstage) · talk
Real software engineering tasks are not asking a model to write a function, but long tasks (o(hours) reading unfamiliar code, running tools, recovering from wrong turns, and knowing when the job is actually done. In this keynote, Melvin Johnson (VP, Google DeepMind) covers how we post-trained for long-horizon agentic coding: - Hard tasks. Popular benchmarks saturate, so we built internal realistic, multi-step software tasks. - Graders that can't be gamed. When agents learn to satisfy unit tests without solving the problem, you need graders that check the work the way a reviewer would. - Model behavior. An agent that says "fixed it" when it didn't is worse than no agent. We reward models for reporting accurately what they did and didn't do. - Efficiency over long horizons. Finishing more of the task with fewer tokens and stable behavior across very long contexts. - Shipping weekly. Modular improvements and dogfooding with Google engineers let us release in weeks instead of quarters.

### A Company Built Around the Agent
Speakers: Quinn Slack
Schedule: 4:50pm - 5:10pm · Continental 4–6 (Mainstage) · talk
You might know Amp as one of the agent products, but we're really a 21-cofounder team figuring out how to build our entire company around the agent. We don't have traditional roles, everyone pushes to main, we have one meeting per week, we're very profitable and above $100M ARR, and we haven't hired anyone (yet). See how we use the agent to do everything, with high quality, and what relics of the old tech company world we ditched.

### 12-Factor-Factories: Design Patterns for Agentic Coding
Speakers: Dexter Horthy
Schedule: 5:10pm - 5:30pm · Continental 4–6 (Mainstage) · talk
Every AI lab is building full stack cloud agents. Every enterprise is building their own software factory. We've worked with a lot of teams adopting all flavors in every combination. In this talk we'll distill out the core principles and design patterns we've seen across factories, and make a case for why the AI-native forge will be composable and built on open primitives.

### Thariq Shihipar, Independent
Speakers: Thariq Shihipar
Schedule: 5:30pm - 5:50pm · Continental 4–6 (Mainstage) · talk
No description published; title, speakers and schedule only.

### Something to Celebrate
Speakers: swyx
Schedule: 5:50pm - 6:00pm · Continental 4–6 (Mainstage) · talk
To close Code Summit 2026, swyx invites everyone to celebrate together: three days of talks, workshops, hallway conversations and the AI engineers who made them happen. Stay for the finale and celebrate with us.

