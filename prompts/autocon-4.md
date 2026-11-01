>>> HOW TO RUN THIS <<<
This is the digest prompt for autocon-4. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/autocon-4.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/autocon-4.md
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

Below is the program for AutoCon 4 (Austin) (operator). Read it and produce a digest
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
conference: AutoCon 4 (Austin)
type: operator
source_url: https://networkautomation.forum/autocon4
generated: 2026-11-01
registry_key: autocon-4
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Wednesday, 19 November 2025

### Building a Network Automation Business Case that Wins at the Top
Speakers: Jeff Gray
Session: Wednesday, 19 November 2025, 13:15 - 14:00 (Opening Keynote)
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-OpeningKeynote-JeffGray.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-OpeningKeynote-JeffGray.pptx | video: https://www.youtube.com/watch?v=JTup5kS4veU
Building a Business Case for Network Automation that Wins at the Top Network automation has matured technically—but selling its value remains a major challenge, especially at the highest levels of the IT organization. CIOs, CTOs, and enterprise architects are often flooded with competing initiatives, and network automation teams struggle to communicate the urgency, ROI, and strategic potential of automation. In this session, Gluware CEO and co-founder Jeff Gray will reveal what actually resonates with executives, and what doesn’t. With decades of experience selling to Global 2000 CIOs, executive stakeholders, and investors, Jeff will walk attendees through the anatomy of a business case that works: one that speaks to cost optimization, risk mitigation, innovation velocity, and competitive advantage. #AutoCon4 #keynote #keynotespeaker #keynotespeech #networkautomation #businesscase

### Confessions of a CLI Lifer Who Learned to Love Automation
Speakers: Andy Lapteff
Session: Wednesday, 19 November 2025, 14:00 - 14:10
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-AndyLapteff-CLILifer.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-AndyLapteff-CLILifer.pptx | video: https://www.youtube.com/watch?v=tUPUlLKLrKU
I spent two decades living in the CLI, convinced automation was for “those other people.” I wore my manual chops like a badge of honor, until the industry moved on without me. Suddenly, automation wasn’t optional; it was the entry ticket. Getting laid off made that crystal clear. Faced with a choice between clinging to the past or reinventing myself, I picked up Python and never looked back. This talk is a raw, fast-paced story of what happens when a CLI diehard is forced to evolve. I’ll share the hard truths, mindset shifts, and small wins that turned fear into momentum and a career reboot. If you’re still telling yourself automation doesn’t apply to you, this session is your reality check. #networkautomation #cli #commandlineinterface #career #python

### The NAF Network Automation Framework: A Modular Reference Architecture
Speakers: Ryan Shaw
Session: Wednesday, 19 November 2025, 14:10 - 14:40
video: https://www.youtube.com/watch?v=i1eve1uB-Rs
A group network automation experts — Christian Adell, Ryan Shaw, Claudia deLuna, Damien Garros, Dinesh Dutt, and Wim Henderickx — collaborated to create the Network Automation Framework (NAF), a vendor-neutral, modular reference architecture. NAF defines the core building blocks of a flexible, scalable network automation stack, providing a common language and structure for practitioners. For many teams, knowing where to start with network automation — or how the various components fit together — can be daunting. The NAF framework addresses this by breaking down network automation into a set of well-defined, interoperable building blocks. In this session, we’ll walk through each block’s role, characteristics, and interactions, giving you a clear mental model to guide both design and implementation. Whether you’re starting from scratch or refining an existing system, you’ll gain practical insight into how to structure an automation strategy that scales. #networkautomation #framework #reference #architecture

### Overhauling Data Center Network Automation: Intel’s Data-Centric Journey
Speakers: Greg Botts
Session: Wednesday, 19 November 2025, 16:05 - 16:35
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-GregBotts-IntelsDataCentricJourney.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-GregBotts-IntelsDataCentricJourney.pptx | video: https://www.youtube.com/watch?v=wl1STXalmEQ
Embarking on the creation and deployment of a holistic network automation system can be overwhelming, regardless of the size or complexity of the environment. A data-centric approach is essential—focusing first on the network data required to drive automation. When data is treated as the foundation, other system components naturally follow, rather than forcing the data to fit the system. In this talk, we’ll present a case study of Intel’s transformation of its data center network automation system using this data-first methodology. We'll discuss the key drivers behind the change, outline our strategic data-centric approach, share insights and lessons learned along the way, and highlight what we've built to sustain and expand our automation capabilities moving forward. #networkautomation #datacentric #datacenter #intel #datacenterinfrastructure #datafirst

### Lifecycle Automation: Troubleshooting, Upgrading & More
Speakers: Cat Gurinsky
Session: Wednesday, 19 November 2025, 16:45 - 17:15
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-CatGurinsky-LifecycleAutomation.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-CatGurinsky-LifecycleAutomation.pptx | video: https://www.youtube.com/watch?v=6Ea21gOfVKE
#networkautomation #troubleshooting

### 2025 State of Network Automation Survey Results
Speakers: Chris Grundemann
Session: Wednesday, 19 November 2025, 17:15 - 17:35
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-ChrisGrundemann-2025NetworkAutomationSurveyResults.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-ChrisGrundemann-2025NetworkAutomationSurveyResults.pptx | video: https://www.youtube.com/watch?v=DihuRAAXA0A
#networkautomation #netdevops #survey #surveyresearch #surveyresults

## Thursday, 20 November 2025

### Spectron: network orchestration in practice at scale; what works, what hurts
Speakers: Katarzyna Kurowska & Aldrin Isaac
Session: Thursday, 20 November 2025, 9:10 - 9:45
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-KatarzynaKurowska-AldrinIsaac-Spectron.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-KatarzynaKurowska-AldrinIsaac-Spectron.pptx | video: https://www.youtube.com/watch?v=RbBlNKj2IW8
Building and operating data center fabrics at scale is a complex challenge, and eBay's Spectron tackles it head-on with an intent-based, spec-driven approach to network automation and orchestration. In this session, we'll share how Spectron enables engineers to design and provision diverse topologies, validate them with digital twins, and deploy them reliably in production—all while hiding device-level complexity behind well-defined abstractions. We'll highlight what made the system successful, from extensibility and adaptability to its modern architecture, as well as the lessons we learned along the way about abstractions, orchestration, and the realities of prototyping. Expect a candid look at what worked, what hurt, and practical guidance for anyone building large-scale automation frameworks. #networkautomation #spectron #ebay #datacenter #digitaltwin

### Kubernetes Network Emulation, a standard interface to design and validate networks
Speakers: Manodipto Ghose & Ryan Elliott
Session: Thursday, 20 November 2025, 9:45 - 10:20
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ManodiptoGhose-RyanElliott-KubernetesNetworkEmulation.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ManodiptoGhose-RyanElliott-KubernetesNetworkEmulation.pptx

### From Manual to Marathon: My Automation Journey at HEB
Speakers: Erich Crosswhite
Session: Thursday, 20 November 2025, 11:05 - 11:40
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ErichCrosswhite-ManualToMarathonAtHEB.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ErichCrosswhite-ManualToMarathonAtHEB.pptx | video: https://www.youtube.com/watch?v=jhxgJNrWeY0
My talk covers my experiences at HEB of building an Infrastructure as Code (IaC) solution to support our new Arista environment, from the initial mandate of using IaC to a fully functional deployment pipeline including validation stages. Throughout the presentation I mirror the steps to show how each stage correlated to my own marathon journey. I review my early home-lab work proving out the solution as well as finding possibly career ending settings in the lab environment to showcase the importance of using a lab environment to prepare. I include our initial integration with Nautobot for access-port configurations that nearly caused an outage due to lack of proper guardrails. This lead to a move off of Nautobot not due to a fault in the product but rather my lack of controls. I finish the presentation with our current state of the environment, detailing the checks and validations we have in place, along with future improvements I want to add in. #networkautomation #deployment #nautobot #validation #arista #infrastructureascode #guardrail #marathon

### Toward Autonomy
Speakers: Scott Robohn
Session: Thursday, 20 November 2025, 11:40 - 12:15
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ScottRobohn-TowardAutonomy.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ScottRobohn-TowardAutonomy.pptx | video: https://www.youtube.com/watch?v=esVkHChgSg8
Control Plane 3.0: Scott Robohn outlines what “autonomy” in networking means, how we already rely on autonomous behaviors, and why true autonomy is a continuum rather than a feature you simply “turn on.” The talk breaks down the practical ingredients needed to move safely toward self-healing/self-optimizing networks: closed-loop control and feedback, fail-safe error handling, incremental workflow-by-workflow development, and people and trust through measurable experiments and gated rollouts. Scott also frames AI as a “how,” not a “what,” and encourages continuous evaluation, small-batch change, and strong risk management on the path to “Control Plane 3.0." #networkautomation #controlplane #autonomy #autonomous #ai

### Scaling Network Operations with Modular Ansible: A Multi-Environment Automation Framework
Speakers: Joseph Nicholson
Session: Thursday, 20 November 2025, 9:05 - 9:50
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-JosephNicholson-ScalingNetOpsWithModularAnsible.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-JosephNicholson-ScalingNetOpsWithModularAnsible.pptx | video: https://www.youtube.com/watch?v=mVq5bdkiskg
This presentation explores the evolution and practical application of Ansible within the Global IP Network (GIN) division of NTT DATA, focusing on how modular automation has scaled network operations. Drawing from over two decades of experience in network engineering, Joseph Nicholson shares insights gained over the past six years of building and managing a dynamic, scalable automation framework using Ansible in a complex, multi-vendor environment. The talk highlights how automation was integrated with an existing, internally developed change management system, and how dynamic inventories and CI/CD pipelines were leveraged to streamline operations. Attendees will gain a practical understanding of how modular task design, repository structure, and automation pipelines can reduce human error, improve maintainability, and support large-scale network environments. Lessons learned from real-world implementations-including pitfalls, testing strategies, and the importance of version control-will provide valuable guidance for engineers looking to scale their own automation efforts. #networkautomation #ansible #ansibleautomation

### From CLI to Model: Building a Foundational Source of Truth for Brownfield Networks
Speakers: Munachimso Nwaiwu
Session: Thursday, 20 November 2025, 9:50 - 10:35
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MunachimsoNwaiwu-FromCLItoModel.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MunachimsoNwaiwu-FromCLItoModel.pptx | video: https://www.youtube.com/watch?v=5iIx-PYqbBI
For network engineers managing ancient, brownfield networks, the push to innovate and automate can be daunting. The real issue is often the barrier to entry; making that first move is challenging on a legacy network with limited to no budget. This barrier to entry exists because most brownfield networks lack a foundational Source of Truth (SOT). Instead of relying on manual CLI access and spreadsheets, the best place to begin is by establishing a Source of Truth that describes the entire network. This presentation closes that gap by introducing an open-source methodology to build this reliable, model-based SOT by reverse-engineering the network's existing operational state. We will demonstrate a practical workflow that programmatically collects configuration and state data from live network devices using Python libraries. This raw CLI output is then parsed into a structured data model, creating a foundational SOT that represents the network's intended state. Attendees will leave with a clear roadmap for building their own SOT, enabling them to move beyond reactive scripting and unlock powerful, scalable automation, such as validating network changes and performing automated state audits. #networkautomation #sourceoftruth #sot

### Bridging Infrastructure and Data
Speakers: Marco Martinez
Session: Thursday, 20 November 2025, 11:05 - 11:50
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MarcoMartinez-BridgingInfrastructureAndData.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MarcoMartinez-BridgingInfrastructureAndData.pptx | video: https://www.youtube.com/watch?v=eU6-fYqch8Y
Modern infrastructure management often struggles with fragmented data and static configurations that slow down operations and decision-making. In this talk, I’ll share how integrating Infrahub with Terraform can bridge that gap—bringing real-time, data-driven insights directly into Infrastructure as Code workflows. I developed a custom Terraform provider powered by GraphQL, enabling dynamic access to infrastructure data and eliminating the need for traditional .tfvar files. This solution is supported by an automated pipeline that builds and publishes the provider, streamlining deployment and improving scalability. Along the way, I’ll discuss the challenges of working with dynamic schemas in a tool built for static definitions, and how flexibility and automation can unlock new possibilities in infrastructure design. Attendees will learn practical strategies to reduce manual overhead in their workflow, enhance automation, and make infrastructure truly data-centric. #networkautomation #data #terraform #infrahub #graphql

### Is MCP just an API Abstraction?
Speakers: William Collins
Session: Thursday, 20 November 2025, 11:50 - 12:35
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-WilliamCollins-MCP.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-WilliamCollins-MCP.pptx | video: https://www.youtube.com/watch?v=-SKWJhKseEE
APIs were architected for the web: stateless requests, URL-based routing, and built for human developers to code against. MCP arrived with considerable fanfare, but is it merely an upgraded API that facilitates inter-system communication? In this talk, we'll dissect the architectural divergence point by point – from foundations to code, and everything in-between. #networkautomation #mcp #api #artificialintelligence #aiagents

### ESnet’s new Micro-Service based Discovery Service
Speakers: Marc Koerner
Session: Thursday, 20 November 2025, 13:45 - 14:20
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-MarcKoerner-ESnetDiscoveryService.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-MarcKoerner-ESnetDiscoveryService.pptx | video: https://www.youtube.com/watch?v=AxSFCr7zo40
ESnet’s new Discovery Service: A micro-service based generic configuration repository and abstraction layer ESnet uses multiple tools to discover and extract configuration information across the network. These tools gather data for various purposes: synchronizing and validating optical circuit information with our configuration database, gathering L2 and L3 information to determine the current network topology and capacity for our L2VPN allocation tool OSCARS, etc. All these tools gather a lot of data, mainly dedicated to their specific purpose. This approach has many drawbacks regarding the global picture: redundant data collection, incoherent information across applications, unnecessary device processing, and network load. To address and mitigate the impact of this very inefficient data-gathering scheme, we decided to develop a new and innovative device abstraction layer, ESnet’s Discovery Service. #networkautomation #discovery #data

### HAWAT: An AI Assistant for Network Troubleshooting
Speakers: Karl Newell
Session: Thursday, 20 November 2025, 14:20 - 14:55
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-KarlNewell-HAWAT.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-KarlNewell-HAWAT.pptx | video: https://www.youtube.com/watch?v=nEWnIYK3koI
HAWAT (Heuristic Analysis With Adaptive Troubleshooting) is an agentic AI assistant for network troubleshooting. This presentation explores the development of a chatbot system designed to interface with network hardware, leveraging recent advances in Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Reasoning and Acting (ReAct) agentic frameworks. Our system demonstrates how agentic AI can autonomously interpret network conditions, execute commands, and provide network administrators with natural language interfaces to network infrastructure. We will detail how the system was built and present pre recorded demos of the chatbot in action. #networkautomation #ai #artificialintelligence #agenticai #chatbot

### From Band-Aids to Best Practices: USAA's Network Automation Journey
Speakers: Brandon Cavett
Session: Thursday, 20 November 2025, 15:40 - 16:15
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-BrandonCavett-BestPracticesAtUSAA.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-BrandonCavett-BestPracticesAtUSAA.pptx | video: https://www.youtube.com/watch?v=MEDwtGy99jQ
This presentation explores the evolution of network automation at USAA, highlighting the journey from manual CLI-based configuration to an automated, configuration-as-code approach. We'll delve into the initial automation efforts around end-to-end rack provisioning, while addressing its limitations in maintainability and Day 2 operations. We'll discuss the challenges encountered with standalone Ansible playbooks, including the need for extensive testing. Then, we'll cover how we started using Arista AVD (Architect, Validate, Deploy) to streamline, standardize and automate Day 2 changes, while also significantly speeding up our Day 1 provisioning efforts. The presentation will showcase the benefits of adopting AVD, and our ongoing efforts to retrofit existing environments. Looking ahead, we aim to integrate Arista Cloud Test (ACT) and Arista Network Test Automation (ANTA) into a comprehensive pipeline. We'll also discuss the challenges of training network engineers on automation tools like Ansible and Git, as well as securing management buy-in for AVD. Attendees will gain insights into our experiences, lessons learned, and practical strategies for implementing network automation at scale. #networkautomation #configurationascode #arista #avd #anta

### From CLI to GPT: How AI Is Rewriting the Rules of Network Automation
Speakers: John Capobianco
Session: Thursday, 20 November 2025, 16:15 - 16:50
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-JohnCapobianco-CLItoGPT.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-JohnCapobianco-CLItoGPT.pptx | video: https://www.youtube.com/watch?v=hHzN8WeQ86I
From the command line to generative AI, this talk traces my personal and professional evolution through three eras of network automation—AI 1.0 (REST APIs), AI 1.5 (RAG with network documentation), and AI 2.0 (autonomous agents with MCP). I’ll share how a kid who once worked on a factory floor became a network engineer, then a Senior Network Architect at the Parliament of Canada who embraced automation as early as 2014. That journey led to writing Automate Your Network in 2019, joining Cisco to train the next generation of engineers, co-authoring the pyATS book, and now helping lead the charge into AI-driven operations at Selector AI. Along the way I built real, working systems—from tools that generate configs from images to AI agents that troubleshoot live infrastructure—and learned what it means to push boundaries in public. But this talk isn’t just about technology—it’s about conviction. When I started fusing AI with network automation, the skepticism was fierce. Many dismissed it as hype; others told me it couldn’t work. Yet persistence turned those experiments into industry shifts: ideas like pyATS, MCP, and AI agents are now part of Cisco certifications and production networks worldwide. I’ll share what it took to keep building through doubt, the lessons learned about resilience and reinvention, and why I believe we’re living through the greatest transformation of network engineering since the CLI itself. #networkautomation #artificialintelligence #aiagents #mcp

### Beyond the Code: People-Centric Leadership for Technical Projects
Speakers: Eyvonne Sharp
Session: Thursday, 20 November 2025, 13:45 - 14:20
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-EyvonneSharp-BeyondTheCode.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-EyvonneSharp-BeyondTheCode.pptx | video: https://www.youtube.com/watch?v=z7WWCMJVgZ8
Project failure rates are high, 70% of projects fail to meet their stated objectives. Leaders with deeply technical backgrounds tend to overlook the human components of successful projects, focusing on technological systems and solutions while ignoring the human elements that drive success. When surveyed, organizations cite sociotechnical failures, not engineering challenges, as the primary reasons for project challenges. In this talk, we’ll discuss how to properly define success and the mindset shifts needed for technical contributors to lead successfully, whether in a formal leadership role or as a technical lead. We’ll discuss the key moments leaders may overlook with practical examples, both positive and negative, that illustrate how to effectively engage with people across the organization, both technical and non-technical. We’ll also share reliable approaches to deal with common people-challenges we face when leading technical teams. #networkautomation #leadership #sociotechnical #peoplecentric

### Do not start somewhere: A methodical approach to implementing Network Automation
Speakers: Srividya Iyer
Session: Thursday, 20 November 2025, 14:20 - 14:55
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-SrividyaIyer-MethodicalApproach.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-SrividyaIyer-MethodicalApproach.pptx | video: https://www.youtube.com/watch?v=RxJJaa0qzPA
Many network engineers are advised to “just start” with automation, but this approach often leads to fragmented, undocumented implementations that depend heavily on individual engineers. Without documentation, standardized processes, or dedicated staffing, the automation efforts are often abandoned. This talk will explore a framework and associated checklists we developed after seeing the same categories of problems with multiple network engineering teams. The first step is to engage stakeholders to identify existing manual workflows and define targeted use cases. The second step is to establish clear objectives, identify tools and technologies, required systems and process changes, and align staffing. The actual implementation can be tracked with a project plan and measurable milestones. #networkautomation #leadership #framework #checklist

### How to Build a CFO-Worthy Business Case for Network Automation
Speakers: Alex Henthorn-Iwane
Session: Thursday, 20 November 2025, 15:40 - 16:15
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-AlexHenthornIwane-CFO-WorthyBusinessCase.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-AlexHenthornIwane-CFO-WorthyBusinessCase.pptx | video: https://www.youtube.com/watch?v=mpkClYI9j3w
A common challenge facing network automation initiatives and the engineers behind them is a lack of sponsorship and financial support from the larger organization. This presentation will lay out practical steps that help network engineers, managers, and directors create a winning business case so they can face and win over stakeholders, including the ""final boss""-the CFO. We’ll cover the journey to establishing trust, tuning into your business, gaining sponsorship, building a business value narrative, covering sample drivers for different industries, running the numbers people care about, and connecting the metric dots to operational metrics. Finally, we’ll talk about how to keep good company along the way. #networkautomation #leadership #businesscase #cfo

### Building an Enterprise Automation Platform in Banking
Speakers: Sujit Gangadharan
Session: Thursday, 20 November 2025, 16:15 - 16:50
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-SujitGangadharan-VisionToReality.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_Leadership-Track/AC4-SujitGangadharan-VisionToReality.pptx | video: https://www.youtube.com/watch?v=b8DZzlM0beo
From Vision to Reality: Building an Enterprise Automation Platform in Banking - A Credit Union's Journey with Red Hat Ansible In the heavily regulated environment of banking, driving automation is as much about culture as technology. This session shares the early stages of a credit union’s journey in adopting Red Hat Ansible Automation Platform as its enterprise automation solution. With the platform in place for only 4–6 months, the focus has been on laying the foundation, choosing the right initial use cases, and building confidence through early wins on non-critical systems. We will discuss how the team navigated cultural resistance, balanced vendor expertise with internal capability-building, and identified key lessons learned that are shaping the path forward. Attendees will gain insight into the practical realities of beginning an enterprise infrastructure automation journey, and how to prepare for the cultural and technical challenges ahead. #networkautomation #leadership #ansible #culture

## Friday, 21 November 2025

### The NetDevOps Journey: Manual Firefighting to Agentic Autonomy
Speakers: Greg Freeman
Session: Friday, 21 November 2025, 9:10 - 9:55 (Closing Keynote)
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-ClosingKeynote-GregFreeman.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-ClosingKeynote-GregFreeman.pptx | video: https://www.youtube.com/watch?v=woGsjPS7cro
The NetDevOps Journey: From Manual Firefighting to Agentic Autonomy #networkautomation #autocon4 #keynote

### The Secret to Network Config & Security Compliance at Scale
Speakers: Vincent Phelan
Session: Friday, 21 November 2025, 9:55 - 10:25
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-VincentPhelan-Compliance.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-VincentPhelan-Compliance.pptx | video: https://www.youtube.com/watch?v=nSlSDb8B2Ks
Running Network Compliance at scale by marrying Architecture and Automation together – two often distinct disciplines that are very powerful when combined. In network management, architecture and automation are two key pieces that often handled by different teams and people without the needed integration or collaboration. But when you bring these two together, they become incredibly powerful and they complement each other. Network Architecture provides the necessary framework and sets rules, guidelines and most importantly constraints; creating a clear and singular structure on how to perform design. It acts as blueprint to avoid design sprawl by enforcing constraints. Network Automation is all about creating the ability to execute on a large scale, delivers precise and consistent results while minimizing/avoiding human error. It essentially enables Architecture that would never be able to deployed if done manually without automation. Without a solid architecture, automation tends to become fragile and can lead to a messy and unstable network. When combined, architecture gives automation a clear path to follow, resulting in automation that drives the architecture guided design delivery making it a reality. This talk will show how we are combining the two to perform network configuration compliance at scale as a tangible example amongst other initiatives. #networkautomation #cybersecurity #compliance #networkarchitecture

### Building AI with AI
Speakers: Senad Palislamovic
Session: Friday, 21 November 2025, 11:10 - 11:40
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-SenadPalislamovic-BuildingAIwithAI.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-SenadPalislamovic-BuildingAIwithAI.pptx | video: https://www.youtube.com/watch?v=x2uRzsD4fE8
Building AI with AI: Developing a vendor-agnostic network automation platform by leveraging an LLM/AI-native toolkit to streamline deployments across multi-vendor networks, including, but not limited to AI clusters. #networkautomation #artificialintelligence #aiinfrastructure

### Battle of the Bots: Which AI Models Actually Work for Network Engineering Tasks
Speakers: Eric Chou
Session: Friday, 21 November 2025, 11:50 - 12:20 (Lightning Talk)
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-EricChou-BattleOfAIBots.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-EricChou-BattleOfAIBots.pptx | video: https://www.youtube.com/watch?v=77doPhGapwE
Battle of the Bots: Which AI Model Actually Work for Network Engineering Tasks As AI models evolve at breakneck speed, network engineers face a critical challenge: how do we determine which AI tools actually work for our specific tasks? While researching my upcoming book on AI-assisted network automation, I discovered that simply asking ""which model is best?"" is the wrong question. Instead, we need a systematic evaluation framework to make informed decisions about when and how to deploy AI in our workflows. This talk introduces a pragmatic approach to AI adoption in network engineering: building a decision tree that calculates the expected value of using AI for specific tasks (like generating MOPs, writing automation code, or analyzing configurations), combined with a structured AI evaluation system. I'll demonstrate three practical evaluation methods—expert reviews, automated code validation, and AI-assisted evaluation—that help you quantify the probability of success for different AI models on different tasks. By the end, you'll have a framework to answer not just ""which AI is best?"" but more importantly: ""should I use AI for this task, and if so, which one?”" #networkautomation #artificialintelligence #aimodel #aimodels

### A Harmonized, Standards-based Ontology for Telco-grade Agents
Speakers: Dave Duggal
Session: Friday, 21 November 2025, 11:50 - 12:20 (Lightning Talk)
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-DaveDuggal-Graphs.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-DaveDuggal-Graphs.pptx | video: https://www.youtube.com/watch?v=LydZQboIm5E
Telcos seek to be “AI-native”. It’s part of 3GPP’s emerging 6G vision. The TM Forum is already racing ahead with Autonomous Networking maturity models. Expectations are high, but Telcos have to look before they leap. As compelling as GenAI and Agentic AI can be, they are inaccurate, inconsistent, inexplicable, inefficient and unsecure. They are tools, not solutions. Language Models and Agents need to be isolated and contained elements of solution architecture. Most initiatives are disjointed; isolated experiments which risk reinforcing siloed domains and stovepiped teams. To fully leverage AI telcos need unified abstractions that provide primitives, building blocks and services that ease and speed the development of Telco-grade AI use-cases and wrap them in strong governance. #networkautomation #graph

### Network Troubleshooting Automation
Speakers: Joshua McNamara
Session: Friday, 21 November 2025, 11:50 - 12:20 (Lightning Talk)
slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-JoshuaMcNamara-TroubleshootingAutomation.pdf | slides: https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-JoshuaMcNamara-TroubleshootingAutomation.pptx | video: https://www.youtube.com/watch?v=VoMPsTpvnvU
The Network Troubleshooter is a GlobalNOC tool that creates time saving efforts for network engineers in debugging alarms. Alerts are created in Nagios which generates tickets in ServiceNow. ServiceNow then calls an AWX Job Template that determines which Workflows to run based on the alarm data (BGP, INTF, etc). These Workflows contain Ansible playbooks that are customized to fetch any kind of data from any source. This could be getting logs or interface status from the network device or displaying Grafana graphs by utilizing iframes in the web UI. It becomes a central viewing spot for initial debugging for engineers. The ultimate goal is to save network engineers time during on-call events when they have to wake up, log onto the network, run some initial commands, just to figure out what is going on. The Network Troubleshooter can do all of this by the time the network engineer is called. Ideas for the future to better enhance this experience is to implement a chat bot AI that knows the Network Troubleshooter and can provide suggestions on things to check based on the alarm data provided. #networkautomation #troubleshooting

