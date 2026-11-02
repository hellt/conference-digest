>>> HOW TO RUN THIS <<<
This is the digest prompt for swinog-42. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/swinog-42.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/swinog-42.md
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

Below is the program for SwiNOG #42 (operator). Read it and produce a digest
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
conference: SwiNOG #42
type: operator
source_url: https://www.swinog.ch/meetings/swinog42/
generated: 2026-11-01
registry_key: swinog-42
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Day 1
### Reality, Rewritten: AI as Forger and Investigator
Speakers: Dominik Haenni - Zurich Forensic Science Institute
What happens when the same technology can fabricate evidence and help analyse it? Generative AI can create convincing images, clone voices and produce plausible documents. For forensic science, this challenges not just how digital evidence is examined, but what can be trusted in the first place. Drawing on current examples from the Zurich Forensic Science Institute, this talk explores AI’s dual role as a tool for deception and a powerful aid to analysis, research and software development. It also looks beyond the technology. As AI makes knowledge more accessible and accelerates workflows, what happens to expert judgement, responsibility and the way organisations work? For anyone building or operating digital systems, these questions reach far beyond the forensic laboratory. When AI changes the rules, can we afford business as usual?

### Automating Target Discovery in the gNMIc Operator
Speakers: Daniel Schatzmann
slides: https://www.swinog.ch/wp-content/uploads/2026/11/BA-gNMIc-operator-swinog42.pdf
What the talk is about Network telemetry is evolving from pull‑based SNMP toward streaming‑based gNMI. The gNMIc Operator brings this model into Kubernetes, enabling declarative configuration and high availability for telemetry collectors. However, managing monitored devices (“targets”) still requires manual updates — a source of inconsistency and operational overhead. This talk introduces an automated target discovery mechanism that synchronizes gNMIc Operator targets with external sources of truth such as NetBox. The solution combines periodic synchronization with event‑driven updates, ensuring that the telemetry system always reflects the current network state. Who it’s for Network and monitoring engineers using gNMI or gNMIc DevOps and SRE teams deploying telemetry in Kubernetes Operators seeking to reduce manual configuration and improve reliability Anyone interested in bridging network automation and cloud‑native observability What the audience will walk away with The audience will understand how the gNMIc Operator can be synchronized with an external source of truth using a combination of periodic synchronization and event‑driven updates. They will see how the provider, API server, and client components interact to apply target information declaratively in Kubernetes, and how this approach reduces manual configuration effort. A live demonstration will show the synchronization workflow in practice, illustrating how changes in the external inventory system propagate to the operator. Attendees will leave with a clear picture of the architecture, its integration into the upstream gNMIc Operator project, and how it can be extended to different sources of truth.

### On-prem LLM cluster for network and security analyses
Speakers: Mischa Diehm - narrowin
slides: https://www.swinog.ch/wp-content/uploads/2026/11/swinog42-on-prem-llm-network-security.pdf | video: https://youtu.be/KHmfNnx535U
This talk shows how to run AI for network and security analysis entirely on-prem: an open stack of open-weight LLMs, open-source inference and the Model Context Protocol (MCP), integrated with the systems you already operate. No cloud calls: configs, topology, logs etc. never leave the building. At SwiNOG #41, Tobias Bühler showed us what AI can and can't do in network operations and listed hallucinations, data privacy and cost among the hard problems. The on premise stack in this talk tackles privacy and cost by design, and hallucinations by grounding every answer in real network data. The architecture has four layers, built from open components: Interaction Layer: Interface & agent: chat, web and API, plus an agent that plans tool calls AI Layer: Local LLM cluster: open-weight models (GLM, Qwen, Nemotron, DeepSeek) on a local GPU cluster connected via 400G Switch that fits on a desk; served by vLLM behind an OpenAI-compatible API Integration Layer: MCP and Skills: MCP servers exposing purpose-built tools, not raw data. Targeted skills enhance the generic LLMs Context Layer: Data & existing systems: topology data, network configs, syslog, CMDB/IPAM, monitoring, ticketing, or a single device via SSH, REST or SNMP Besides the architecture of the stack, the talk shares the network design (and its challenges) for the on prem cluster, insights on integrating and combining network data sources as well as thoughts on RBAC, least privilege and human approval. Lastly, we share the promising evaluation results. They stem from a multi-vendor IT/OT lab network built with Containerlab and from agent-driven network assessments based on production data from real networks. You leave with a reference architecture, tips & tricks for setting up a cluster and integrating your systems, and – hopefully – the motivation to start experimenting.

### Networking for AI
Speakers: Remi Locherer - Arista Networks
slides: https://www.swinog.ch/wp-content/uploads/2026/11/20261020_SwiNOG-Networking-for-AI_v2.pdf
Training Large Language Models (LLMs) or running large inference workloads using XPU clusters introduces distinct challenges for the underlying network. This session explores the core concepts of AI networking, emphasizing open, Ethernet-based architectures. We will examine standard AI workloads and contrast them with traditional data center traffic. Additionally, we will analyze the resulting design principles and implementation strategies, concluding with an overview of emerging industry trends.

### Internet Domain Blocking: Current Legal Situation and Outlook on the Current Revision of the Telecommunications Act
Speakers: Simon Schlauri - Ronzani Schlauri Attorneys
slides: https://www.swinog.ch/wp-content/uploads/2026/11/20261020-Schlauri-Netzsperren-Swinog42.pdf | video: https://youtu.be/bsemYuiTfz4
Criminal prosecutors in French-speaking Switzerland have begun requiring internet access providers to block domains on the grounds of alleged violations of the law by website operators. The presentation examines specific cases from a legal perspective. We will also discuss the new proposal for regulating network blocking in the Telecommunications Act.

### From Connectivity to Cyber Resilience : Defense in Depth for the connected Enterprise
Speakers: Yannick Gautier - NI ION NOKIA
slides: https://www.swinog.ch/wp-content/uploads/2026/11/Defense-in-depth-for-connected-enterprises-Gautier_Nokia_Swinog_42_Oct20ed1f.pdf | video: https://youtu.be/xQJpbnAkCK0
The rapid progress in quantum computing and AI, along with pressure from cybersecurity authorities, requires enterprises to urgently overhaul asymmetric cryptography in vulnerable applications. While transitioning to Post-Quantum Cryptography (PQC) is essential, it alone cannot ensure security against evolving risks and unforeseen breakthroughs. Authorities emphasize the need for reinforcing cryptographic mechanisms to address emerging vulnerabilities. Companies must protect critical societal functions by ensuring confidentiality, integrity, and availability through defense in depth, particularly from secure connectivity that service providers can deliver. Key priorities include: • Adapting cryptographic mechanisms over time. • Ensuring resilience against analytical breakthroughs. • Diversifying mathematics- and physics-based trust models. • Safeguarding sovereignty with control of security and entropy . • Strengthening assurance via certifications and compliance. The ultimate challenge lies in preparing infrastructure for continuous cryptographic uncertainty, ensuring resilience not just in algorithms but in operational systems under an AI-accelerated threat landscape. Through adaptable infrastructure-level measures, service providers can play a crucial role in delivering secure connectivity as part of a comprehensive defense-in-depth strategy.

### Managing IP Allocation with an Open-Source DDI
Speakers: Marco Martinez - Swisscom
slides: https://www.swinog.ch/wp-content/uploads/2026/11/Managing-IP-Allocation-with-an-Open-Source-DDI-2.pdf | video: https://youtu.be/70M_GdX4QBA
A view of the current DDI Landscape, their advantages and drawbacks. What are alternatives to the current DDI Solutions; could it be an Open-Source DDI? Exploring the Business Use-Case and Architecture of an Open-Source DDI and a demonstration of an implementation.

## Day 2
### Beyond RPKI Origin Validation, what do we gain with RFC9234 (BGP roles) and ASPA
Speakers: Claudio Jeker - RSSF
slides: https://www.swinog.ch/wp-content/uploads/2026/11/OpenBGPD-SWINOG-42-2026.pdf | video: https://youtu.be/ECjCo7pNnyg
Exploring how all the various new BGP security extensions work and why they are important. The talk uses some real-world scenarios and looks how the various RFCs and draft work together. It tries to explain why it is important to add ROA and ASPA records for ISPs but also explain some of the traps to look out for.

### From Lab to Production: The Hard Parts of Agentic NetOps
Speakers: Tobias Bühler - NetFabric
slides: https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG_42_NetFabric_v3.pdf | video: https://youtu.be/MTVdgd6WK_8
At SwiNOG#41 we explored what agentic AI can and can't do in network operations. The talk sparked many follow-up conversations. Most of them circled the same question: what happens once you leave the lab? Based on NetFabric deployments in Swiss ISP and MSP networks, this talk walks through the main roadblocks we hit moving agentic NetOps from small-scale tests to production networks, and what it took to get past each of them. We focus on three areas: Correctness: In production, misunderstanding an interface state or firewall rule is only one of many ways an agent can fail. Issues like incomplete investigations or overconfident answers matter just as much. We highlight failure cases drawn from real deployments and show how we addressed the most pressing ones. Security: How can an agent safely consume the output of CLI commands on production devices? And what can go wrong when it has direct access to a production database? Model choice: New models and agent paradigms appear every month. We show why simple tests produce misleading results and what a robust evaluation framework looks like.

### The Cloud-Native Advantage: Intent-based Network Automation
Speakers: Alexander North - Swisscom (Schweiz) AG
slides: https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG-42-–-The-Cloud-Native-Advantage.pdf | video: https://youtu.be/WmebR1Lf5lE
As the industry is quickly moving towards adopting and deploying their infrastructure and products in the cloud-native way, network devices are starting to be left behind. These often rely on imperative, one-shot approaches to be configured. This gap is what Schema Driven Configuration (SDC) is trying to fill. SDC provides an intent-based and YANG backed interface to configure network devices and functions over either NETCONF or gNMI, and at Swisscom we have started to use SDC to configure our 5G mobile core functions. The self-healing and reconciliation abilities of SDC ensure that the configuration running on the device reflects the desired state, fixing deviations if necessary without human intervention, as well as providing visibility into the live configuration state. This is key when it comes to larger and increasingly complex network setups such as those we are running at Swisscom, where the core alone has over 5000 configuration parameters over 14 network functions.

### The Accidental Platform Team: Kubernetes Operators at Swisscom
Speakers: Fabian Schulz - Swisscom
slides: https://www.swinog.ch/wp-content/uploads/2026/11/2026-10-21-swinog-accidental-platform-team.pdf | video: https://youtu.be/7kWNTz5mPek
What happens when Operators outgrow their original scope? At Swisscom, our Operators for network automation are now used both by the 5G Core team to automate the mobile core and by our platform team to power Kubernetes-as-a-Service. Suddenly, we found ourselves running “Operators as a Service,” sitting between networking and application teams, defining boundaries, and scaling a model that spans domains. In this session, we’ll share what worked, and what didn’t. How we convinced teams with little kubernetes know-how to adopt our Operators, designing interfaces that hide complexity, and keeping reliability high without slowing teams down. Most importantly, we’ll highlight why staying close to our users, understanding their needs, workflows, and limits, was critical to building Operators they actually wanted to use.

### FRRouting Open Discussion
Speakers: Martin Winter - NetDEF / FRRouting
slides: https://www.swinog.ch/wp-content/uploads/2026/11/FRRouting-–-Open-Discussion-·-SwiNOG-42.pdf | video: https://youtu.be/ivgjZ7B6Xo8
Usually, a talk presents the latest & greatest of some products and tries to convince you to buy or use it. This isn't that kind of talk. We'll start with a quick introduction, but be prepared to some interactive discussion. We are an Open Source Product and we know we are not perfect. We want to hear the good and bad of your experience, the reason why you love us or hate us, what you think is missing or not working as you need it. Where can we improve? How can we help you? How can we work together?

### Small BNGs
Speakers: Fiona Weber - WDZ GmbH // Wobcom GmbH
slides: https://www.swinog.ch/wp-content/uploads/2026/11/202610xx_FW_Small-BNGs.pdf | video: https://youtu.be/hnC82wCm0mY
The telco industry trend over the last few years shifted to terminating subscribers on big central routers. At AS9136 we decided to do the opposite and brought small white-box BNGs out in the field. Now, with the migration nearing completion, we'll look back at our experience and where other networks could benefit from similar architectures.

### Retro Networks
Speakers: Gianpaolo Del Matto - THE PHINTAGE COLLECTOR
slides: https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG-Oct.-2026-V3.pdf | video: https://youtu.be/L4rc3l15crM
Old network tech at a glance: A glaring trip down memory lane

### CommunityRack – New focus, new projects, more bits!
Speakers: Andrew Vieyra - CommunityRack.org
slides: https://www.swinog.ch/wp-content/uploads/2026/11/2026-10-21-CommunityRack.org-More-Bits.pdf
A lightning update on CommunityRack.org, some new faces in the organisation, and new community projects we're working on!

### Rheintal IX Update
Speakers: Thomas Fritz - Rheintal IX
slides: https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG42_handout.pdf | video: https://youtu.be/XLkEQ7LQsrM
It is about what happened at the Rheintal IX in the last two years and what will come in the near future: 15 years anniversary Closing the network ring around the Lake Constance new PoP in Friedrichshafen (DE) several new peers IXP Update with a great new feature new PoP in Winterthur 2027 RFC8950 project started

### SwissIX – the mandatory 5′ update before lunch
Speakers: Arist Volger - SwissIX Internet Exchange
slides: https://www.swinog.ch/wp-content/uploads/2026/11/20261020_SwissIX_SwiNOG42_V1.01.pdf | video: https://youtu.be/kXgiEIkOwac
A quick update on the latest developments at SwissIX – right before lunch.

