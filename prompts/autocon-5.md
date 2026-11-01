>>> HOW TO RUN THIS <<<
This is the digest prompt for autocon-5. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/autocon-5.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/autocon-5.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

Below is the program for AutoCon 5 (Munich) (operator). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is an operator program (network/infrastructure operators). Focus on
operational practice, failure stories, and techniques that transfer across
environments rather than org-specific anecdotes. Up-rank concrete postmortems,
tooling and automation that others can adopt, and hard-won lessons about
running networks at scale. Down-rank vendor-sponsored sessions that are pitches
in disguise. Note when a technique depends on a specific operator's scale or
topology.

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
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
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
conference: AutoCon 5 (Munich)
type: operator
source_url: https://networkautomation.forum/autocon5
generated: 2026-11-01
registry_key: autocon-5
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Wednesday, 10 June 2026

### The Cognitive Biases Behind Automation's Failures and Future Successes
Speakers: Michael Bushong · VP Data Center — Nokia
Session: Wednesday, 10 June 2026, 13:15 - 14:00 (Opening Keynote)
Our industry has poured billions into network automation. Most networks remain largely un-automated. This keynote argues the real obstacles aren't technical — they're psychological. Loss aversion, survivorship bias, and misframed business cases have quietly killed more automation initiatives than any protocol gap ever did.

### Standing Out in a Virtual World: Personal Branding for Engineers
Speakers: Alexis Bertholf · Global Technical Evangelist — Megaport
Session: Wednesday, 10 June 2026, 14:00 - 14:10
video: https://www.youtube.com/watch?v=YmWzaeNZnxQ
How personal branding and platforms like LinkedIn can be used as practical leadership tools to surface emerging talent, build mentorship pathways, and attract the next generation to network engineering.

### Network Operations Automation at DE-CIX
Speakers: Lucas Immanuel Nickel · Network Operations Engineer — DE-CIX
Session: Wednesday, 10 June 2026, 14:10 - 14:40
video: https://www.youtube.com/watch?v=k1TMAgNROh8
Two production-ready delivery patterns from DE-CIX's NetOps team: a gNMIc config generation job driven from Zabbix and NetBox, and a geospatial network view web service — both shipping via GitOps pipeline in under 10 minutes.

### Modernizing Workflows as Old as the Railways: Operationalizing Network Automation
Speakers: Leo Fleskes · Network Automation Architect — DB Systel GmbH
Session: Wednesday, 10 June 2026, 15:35 - 16:05
video: https://www.youtube.com/watch?v=49j4WqMxm98
Two years of data work came before any automation was possible at Deutsche Bahn — and that groundwork eventually enabled fully automated WAN workflows across 2,500+ routers. A VPN rollout that took 70 minutes across four teams now takes 25 across one.

### Meeting Automation in the Middle: Why NetOps Automation Can't Wait
Speakers: Tim Sando · Senior Network Engineer — Sony Interactive Entertainment (PlayStation)
Session: Wednesday, 10 June 2026, 16:05 - 16:35
video: https://www.youtube.com/watch?v=BMfRqkAH0c4
One script checking backbone circuit state grew into a trusted set of operational tools at PlayStation. The argument for building ops-led automation now, designed to converge with future platform capabilities — rather than waiting for top-down programmes that rarely move fast enough.

### Rethinking Network Monitoring
Speakers: Christian Adell & David Flores · CoreWeave
Session: Wednesday, 10 June 2026, 16:45 - 17:15
video: https://www.youtube.com/watch?v=F6_f1piv0LI
What network monitoring needs to look like in 2026: diverse data sources, fully integrable into the automation loop, and architecturally scalable. Not better dashboards — an active participant in how your network operates.

### NAF Network Automation Framework Update
Speakers: Claudia de Luna · EIA / NAF Architecture Group
Session: Wednesday, 10 June 2026, 17:15 - 17:35
video: https://www.youtube.com/watch?v=I_iLjkZ3F9I
A standing update from the NAF Framework team: what's new, where it's been presented, and a live walkthrough of a use case using the NAF Solution Wizard.

## Thursday, 11 June 2026

### Lessons Learned Testing Network Automation Solutions
Speakers: Ivan Pepelnjak · ipSpace.net
Session: Thursday, 11 June 2026, 9:10 - 9:45
video: https://www.youtube.com/watch?v=JuLozEjA45U
The testing procedures behind netlab — from CI/CD pipelines to pre-release integration tests — plus hard lessons: testing distributed systems is harder than it looks, takes longer than you planned, and vendor implementations will surprise you.

### Where Is My Network Model? When Network Engineering Fused Software Development
Speakers: Antonio Óscar Balmaseda Blanco & David Cornejo · Roche Farma
Session: Thursday, 11 June 2026, 9:45 - 10:20
How Roche broke the "perfect data model" paralysis using Scrum of Scrums methodology, adopted Nautobot, and built a custom ETL pipeline to migrate years of network data — iteratively, in working increments.

### Reaching Fully Automated Backbone Networks: A Network Developer's Journey
Speakers: Eugen Serban & Bartek Bacal · Swisscom
Session: Thursday, 11 June 2026, 11:05 - 11:40
video: https://www.youtube.com/watch?v=d4yRszRS6FI
10,000 devices running SRv6, orchestrated by NSO with zero manual intervention, serving 100,000+ service instances — and a candid look at what the four-year journey actually looked like versus what the architectural PowerPoints promised.

### Choose Your Own AI Adventure: A Guide to the LLM Landscape for Networking
Speakers: Eric Chou · Network to Code
Session: Thursday, 11 June 2026, 11:40 - 12:15
video: https://www.youtube.com/watch?v=3WqUh7rIXI8
A practical map of the current AI landscape for network engineers: when to use OpenAI versus local models, how to build a Network Co-Pilot with LangChain and Streamlit, and how to keep sensitive config data off the public cloud.

### NAF Framework — Deep Dive (Parts 1 & 2)
Speakers: Christian Adell & Damien Garros · CoreWeave / NAF
Session: Thursday, 11 June 2026, 9:10 - 10:20
video: https://www.youtube.com/watch?v=d-kjSJxJVKk
A two-part deep dive into the NAF Network Automation Map — how to use the reference architecture to build vendor-agnostic solutions with clear scope boundaries that you own and can evolve.

### NAF Framework Use Case #1
Speakers: Claudia de Luna · EIA / NAF Architecture Group
Session: Thursday, 11 June 2026, 11:05 - 11:35
video: https://www.youtube.com/watch?v=yrab1N4YbNk
A concrete worked example of the NAF Framework applied to a real problem, showing how the reference architecture translates from concept to practical solution.

### Plan First: Applying the NAF Framework to Real Projects
Speakers: Christian Drefke · Bechtle
Session: Thursday, 11 June 2026, 11:35 - 12:05
video: https://www.youtube.com/watch?v=cqEf8LLvKlY
First-hand experience blending the NAF Framework with software architecture frameworks like arc42 — from high-level design through to implementation on real automation projects.

### Resources & Feedback — Then off to the BoF
Speakers: Wim Henderickx · NAF Architecture Group
Session: Thursday, 11 June 2026, 12:05 - 12:15
Closing the morning framework track: resources, Q&A, and transition to the Birds of a Feather session.

### Succeed with Test-Driven Automation
Speakers: Juulia Santala · Cisco
Session: Thursday, 11 June 2026, 13:45 - 14:20
video: https://www.youtube.com/watch?v=RLOVyEA6I98
Three validation layers — configuration, functional, and SLA — with practical pytest and pyATS examples structured so any network engineer can start writing meaningful automated tests from day one.

### How Workflow-Driven Automation Becomes Operable Under Air Gap & Compliance Constraints
Speakers: Henry Ölsner — NTT Germany & Christian Miene — 50Hertz
Session: Thursday, 11 June 2026, 14:20 - 14:55
video: https://www.youtube.com/watch?v=zBvGy34XRUI
A case study building sustainable automation for a German critical infrastructure operator where always-on connectivity is not a given — including the Workflow Definition Document as a formal, auditable contract.

### Ten Years of Network Automation at LINX
Speakers: Riccardo Verzeni · Director of Software Engineering — LINX
Session: Thursday, 11 June 2026, 15:40 - 16:15
video: https://www.youtube.com/watch?v=MRyNX4gDSfI
LINX went from no automation to fully automated end-to-end service provisioning — step by step, over a decade. The argument for incremental over big-bang, grounded in what actually survived contact with production.

### Automation at Scale Across Domains: DC, Campus, and WAN
Speakers: Christian Breunig · Network Architect — Rohde & Schwarz
Session: Thursday, 11 June 2026, 16:15 - 16:50
video: https://www.youtube.com/watch?v=seiputEwZVg
From zero to 500+ devices under unified Git/Ansible/GitLab CI automation spanning data center, campus, and WAN — what it feels like to stop chasing the network and start conducting it.

### Practical Network Reliability Engineering
Speakers: John Howard · Head of Network Infrastructure — Proton AG
Session: Thursday, 11 June 2026, 13:45 - 14:20
video: https://www.youtube.com/watch?v=I2thHjtCXzM
How NRE has enhanced Proton's network team over four years — shifting focus from individual device health to the services and capabilities end users depend on, reducing alert fatigue and service sprawl.

### "A Computer Must Never Make a Management Decision." Can We Let AI Run Our Infrastructure?
Speakers: Marc Stadtherr · Kumorai Inc.
Session: Thursday, 11 June 2026, 14:20 - 14:55
The industry can change infrastructure faster than it can explain, govern, or secure it — and is now handing that environment to AI. The missing piece isn't another tool; it's a governing model of what infrastructure actually is.

### Demos, Docs, and Dialogue: How I Got Buy-In for Ansible Automation
Speakers: Joseph Nicholson · Network Operations Engineer — NTT DATA
Session: Thursday, 11 June 2026, 15:40 - 16:15
video: https://www.youtube.com/watch?v=kLYYGBgTiDY
What it took to deploy Ansible router upgrades in a live NOC — shift-specific demos, transparent documentation, and ride-along pilots that turned resistant technicians into enthusiastic adopters.

### The ROI of Network Autonomy: Building the Business Case for Agentic Tool-Chaining
Speakers: Justin Ryburn · Field CTO — Kentik
Session: Thursday, 11 June 2026, 16:15 - 16:50
A technically successful self-healing network nearly died because no one translated it into business language — and six months of re-engineering the story, not the code, is what finally got it funded.

## Friday, 12 June 2026

### How NetOps Can Embrace AI to Lead Enterprise Innovation
Speakers: Chris Wade · CTO — Itential
Session: Friday, 12 June 2026, 9:10 - 9:55 (Closing Keynote)
Real-world AI initiatives in network operations — architectures, spec files, agents, and what it takes to apply software engineering discipline to a technology where everyone, everywhere, is learning simultaneously.

### From Data to Decisions: Real-Time Network Context
Speakers: Víctor Fernández · Senior Network & Systems Architect — Colt Technology Services
Session: Friday, 12 June 2026, 9:55 - 10:25
video: https://www.youtube.com/watch?v=GvZjayObzWQ
A real-time platform unifying configs, telemetry, BGP data, service relationships, and events into a single live model — enabling smarter automation, faster troubleshooting, and the shift from reactive to proactive operations.

### Network Automation Graveyard: Field-Tested Anti-Patterns to Kill Your Project
Speakers: Constantin Vurli · Network Automation Engineer — CNS Communications
Session: Friday, 12 June 2026, 11:10 - 11:40
video: https://www.youtube.com/watch?v=q79Tu7T9FcA
Five years of consulting has surfaced three recurring failure modes: automation islands that never connect, tool-first thinking that picks the wrong stack, and dead ends from following the path of least resistance past the point of no return.

### AI-Assisted Catalog Modeling for Multi-Vendor Networks
Speakers: Nikolina Grahovac
Session: Friday, 12 June 2026, 11:40 - 12:30 (Lightning Talk)
video: https://www.youtube.com/watch?v=6cZt3qqphCU
Network abstraction is the first step in almost every project we deliver, and it's rarely fast. After many projects building TMF-aligned solutions, we started asking why, and what the best network abstractions had in common. This talk shares how we captured the implicit knowledge of our domain experts, built an AI tool that helps them model better, faster, across multiple vendors and business contexts, and integrated this approach into building products on top of a real orchestration platform. All of that without offloading everything to an agent and expecting it to grasp the full complexity of the problem domain. #AutoCon5 #ai #artificialintelligence

### Architecting Network Automation with Software Engineering Principles
Speakers: Leandro Lerena
Session: Friday, 12 June 2026, 11:40 - 12:30 (Lightning Talk)
video: https://www.youtube.com/watch?v=HI1SM9RBLJU
Every network automation journey begins with a focused script that effectively solves an immediate problem. However, as infrastructure and automation demands scale, the traditional scripting approach reaches its structural limits. Standalone scripts make automated testing, CI/CD integration, robust connection handling, and secure execution inherently difficult, and expanding support for multiple vendors organically leads to complex, monolithic codebases. In this session, we will share our journey of pushing standard scripting to its limits, and how reaching those natural boundaries became the catalyst for evolving our entire approach. To break this cycle, we stopped searching for a silver-bullet solution and looked for paradigms instead. We will present how we successfully transitioned from isolated, fragile scripts to a robust, trustworthy automation ecosystem by integrating core Software Engineering principles. By abstracting complexity away, we created a 'Lego-brick' developer experience built on modularity. This allows teams to easily author safe, vendor-agnostic function blocks for complex workflows while providing a framework to elegantly craft specialized vendor plugins. What You Will See: * Achieving Transactional Trust: How to implement pessimistic locking for strong auditability, prevent race conditions, and determine workflow safety profiles. * Establishing Implementation Trust: Practical ways to bring DevOps practices, CI/CD, and validation against virtual labs in

### Automating firewall rule deployment in a highly regulated environment
Speakers: João Soares
Session: Friday, 12 June 2026, 11:40 - 12:30 (Lightning Talk)
video: https://www.youtube.com/watch?v=PZUpC_SVAsk
Firewall rule requests have always been one of the most inefficient IT processes across the highly regulated enterprise landscape. A simple firewall request can traditionally take several weeks to be fully resolved, from requesting, validation, security approval, change management to implementation, testing and verification. In large enterprises, this process can involve multiple teams for something as routine as a port opening. At Ørsted we realized this was not just impacting progress and project delivery times. Developers had already internalized slow delivery as a fact and such a tedious process was silently decreasing ambition and driving up project estimates and cost. To solve this, we built what we called DRAGØN - Ørsted's self-service automation platform for managing and deploying firewall rules. This product allows our internal customers to define, validate, and deploy their own firewall policies through either a simple request form or a complete GitOps workflow, without involving any firewall team in the process. The core idea is that DRAGØN is compliant-by-design: firewall rules are validated automatically, according to policies provided by security teams that have been modularized and exposed via an API, security is involved in the process automatically when necessary and change management is followed strictly. At the end, Terraform deploys the policies to our firewall management platform, and Ansible commits them to the firewalls. Everything is orchestrated throu

### GitOps the Hard Way: Rebuilding a Source of Truth (Three Times)
Speakers: Radim Roška
Session: Friday, 12 June 2026, 11:40 - 12:30 (Lightning Talk)
video: https://www.youtube.com/watch?v=Bv5WSaNfblE
We built a Network Source of Truth for a production dual-DC EVPN/VXLAN fabric — 40 switches, automated from day one with Arista AVD, Git, and GitLab CI/CD. The hard part was not the automation framework. It was designing the data model itself: extracting a coherent service model from a network that had no SOT, discovering that vendor-provided data models did not fit our operational requirements, and rebuilding the schema three times before it worked in production. We also built operational tooling — a CLI editor, validation, and search tools — to make the SOT usable by junior engineers. After one year, the operations team uses it daily. Their biggest takeaway: not speed, but a shift in how they think about network configuration. Three lessons. All learned the hard way. #AutoCon5 #sourceoftruth #sot #gitlab #cicd

### Migrating the GÉANT Network to a new vendor
Speakers: Simone Spinelli
Session: Friday, 12 June 2026, 11:40 - 12:30 (Lightning Talk)
video: https://www.youtube.com/watch?v=UlbrvLODuNg
Over a two-year period, the pan-European research and education network GÉANT successfully migrated its infrastructure from Juniper to Nokia while simultaneously building an in-house automation platform—the GÉANT Automation Platform (GAP)—leveraging open-source tools. Specifically, Workflow Orchestrator (https://workfloworchestrator.org) and Ansible. This short talk shares the key technical and organizational decisions behind that effort, including why an open, community-driven approach was chosen and how the platform’s design, modeling, and team structure enabled large-scale change without service disruption. We will highlight practical lessons learned: the importance of starting small while maintaining a clear long-term vision, treating design as the primary source of truth for automation, and focusing on functional outcomes rather than low-level configuration. Finally, we demonstrate how developing and owning high-quality software in-house can accelerate innovation and extend value across the organization. This experience shows that meaningful automation is achievable at any level of technical maturity and delivers benefits for both engineers and the wider organization. #AutoCon5 #networkmigration #networkautomation #softwaredevelopment

