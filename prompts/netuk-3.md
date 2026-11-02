>>> HOW TO RUN THIS <<<
This is the digest prompt for netuk-3. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/netuk-3.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/netuk-3.md
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

Below is the program for NetUK3 (The Brewery) (operator). Read it and produce a digest
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
conference: NetUK3 (The Brewery)
type: operator
source_url: https://indico.netuk.org/event/3/
generated: 2026-11-01
registry_key: netuk-3
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Sponsor-led Content
### The Great Escape from On-Prem
Speakers: Daniel, Ed (Infoblox), Cartron, Nico (Infoblox)
page: https://indico.netuk.org/event/3/contributions/66/
Modernising infrastructure isn’t simply about moving workloads to the cloud; it can also demand rethinking how foundational network services are delivered, operated, and secured. In this session, we’ll share a practical architectural pattern for transitioning from traditional on-premises deployments to a Protocol-as-a-Service model. We’ll cover migration strategy, operational transformation, and integration with modern security architectures such as SASE.

### Agentic AI Network Automation
Speakers: Taylor, Gary (Megaport)
page: https://indico.netuk.org/event/3/contributions/65/
Megaport will be presenting the move from manually depoying NaaS services via the Megaport portal to using MCP and Agentic AI to manage customer infrastructure.

## Main Session
### Data Centers in Space - The Big Picture
Speakers: Bennett, Geoff (Nokia)
page: https://indico.netuk.org/event/3/contributions/57/
Data Centers in Space Geoff Bennett Director, Solutions and Technology, Nokia The race for companies to develop the next best Artificial Intelligence model means that they need to deploy processing capacity at unprecedented scale. We are already seeing the construction of multi-gigawatt scale data centers, and this creates significant challenges to find sufficient space, power and fresh water for these facilities. In addition, the sheer scale of such data centers brings them into direct conflict with local human populations, leading to an increasing backlash against the permitting of these projects in populated areas. Beginning with remarks by Bill Gates as far back as 2014, several technology leaders have outlined plans for massive constellations of orbiting data centers. In January this year SpaceX filed plans with the US Federal Communications Commission for up to one million “orbital data scenter” satellites. Google, with its Project Suncatcher, is suggesting that space-based data centers could be a reality as soon as 2027. And multiple startups are already raising funds to develop the building blocks of these new technologies. But how realistic is the goal itself? What are the major hurdles in our way, and how easy is it to get over or around them? Are there some problems that are just insoluble? And how much damage are we likely to inflict on humanity as we chase this dream? I begin with a simple question - what problems is this idea of space-based data centers trying to solve? From there I will look at the technologies we need to develop, the scale of what would have to happen, and the unavoidable consequences of filling up space in this way.

### Hollow Core Fibre - Nothing is better than glass for guiding light
Speakers: Jones, Steve (Huber+Suhner)
page: https://indico.netuk.org/event/3/contributions/47/
The impressive advantages when using light not silicon make the promise of HCF something worth taking notice of. This presentation takes a short look at the technology behind HCF, outlines the benefits and possible applications whilst highlighting some constraints (& solutions) in market dominated with singlemode fibre & LC/APC connections

### When UK Traffic Takes an Unplanned Detour: Routing Security for the UK Peering Community
Speakers: Mukherjee, Ritesh (Nokia)
page: https://indico.netuk.org/event/3/contributions/46/
In June 2019, a Swiss data center accidentally leaked over 70,000 routes to China Telecom in Frankfurt. Within minutes, China Telecom announced those routes globally, and for over two hours, massive volumes of European mobile traffic — destined for networks in the Netherlands, Switzerland, and France — were silently rerouted through Chinese state-controlled infrastructure. In the summer of 2025, a BGP hijack disrupted DNS root server infrastructure, shaking the foundation of global name resolution. And in between, researchers documented a new class of "stealthy" BGP hijacks where a network's RPKI checks all pass and the BGP table looks perfectly clean, yet traffic is being diverted through non-validating neighbors without the victim ever knowing. These are not abstract, far-away problems. The United Kingdom sits at the heart of global Internet interconnection. LINX is one of the largest Internet Exchange Points in the world. Traffic traversing UK peering fabrics touches networks across Europe, the Middle East, Africa, and beyond. When a route leak or hijack occurs anywhere on the planet, UK operators and their peers are in the blast radius — and when it happens to a European neighbor, the impact is immediate. The good news: the UK peering community has made real progress. LINX and LONAP both enforce RPKI validation on their route servers, filtering invalid routes before they reach members. But route server filtering is only the first line of defense. Members peering bilaterally — without the route server as an intermediary — remain exposed unless they deploy validation themselves. And even networks with full ROV enabled face blind spots: route leaks that ROV cannot detect, path manipulation attacks that require ASPA to prevent, and stealthy hijacks that demand observability tools like BMP to even notice. This presentation provides a practical, UK-focused roadmap for closing these gaps. We examine what LINX and LONAP route server filtering already protects against and where the remaining exposure lies for bilateral peers. We introduce ASPA — the emerging RPKI-based path validation standard that all five Regional Internet Registries have committed to supporting by the end of 2026 — and explain what it means for UK operators signing their first ASPA objects. And we make the case for BMP as the missing security observability layer: the tool that turns filtered invalid routes from silent discards into active threat intelligence, enabling operators to detect anomalies that neither ROV nor ASPA can surface on their own. Attendees will leave with a clear, prioritized action plan — from quick wins they can implement this quarter to strategic investments that will keep UK peering infrastructure resilient against the next generation of routing attacks.

### Autonomous System Provider Authorisation
Speakers: Smit, Ralph (RIPE NCC)
page: https://indico.netuk.org/event/3/contributions/52/
ASPA stands for Autonomous System Provider Authorisation and is a relatively new type of object standardised in the RPKI ecosystem. ASPA objects are signed by AS owners and allow an AS to declare its authorised upstream providers, which prevents route leaks, BGP path spoofing, and valley-free routing violations. They can be created in the hosted RPKI systems of ARIN and RIPE NCC, or using delegated RPKI CA software such as Krill. ASPA standard has already seen significant uptake and is supported by some of the software routers.

### Rethinking Network Monitoring
Speakers: Flores, David
page: https://indico.netuk.org/event/3/contributions/55/
Traditional network monitoring — SNMP polling, static dashboards — tells us what broke, not why. This talk reframes monitoring as an observability problem and walks through a modular, open-source stack enriched with a source of truth. We'll cover correlating metrics, logs and flows, event-driven automation, and AI-assisted root cause analysis — so you leave with a practical blueprint you can pilot yourself.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings
Speakers: Stein, Gerhard (Flexoptix)
page: https://indico.netuk.org/event/3/contributions/48/
In high-performance optical communication systems transceiver health and efficiency are critical to network reliability and energy consumption. This presentation explores the powerful capabilities of Versatile Diagnostics Monitoring (VDM) features found in modern optical transceivers (beyond the speed of 100G) with a particular focus on the Thermoelectric Cooler (TEC) current metrics. By analysing TEC current alongside temperature and cable length data we should be able to identify the optimal operating conditions that will minimise power consumption while maintaining performance. In order to prove this thesis we developed a couple of software prototypes to perform the data analysis. Using real-world VDM data this talk will demonstrate how to evaluate and visualise transceiver efficiency in terms of Watts, uncovering practical insights for engineers aiming to design or operate greener, more efficient optical networks and finally save energy.

### Data Signal-Based Distributed Fibre Optic Sensing
Speakers: Parkes, Jasmine (Comtek Network Systems and Bangor University)
page: https://indico.netuk.org/event/3/contributions/62/
Physical fibre cable problems cause roughly a third of all network outages. Reducing Mean Time to Repair (MTTR) isn’t just a technical goal-it’s an economic necessity. While Distributed Fibre Optic Sensing (DFOS) can solve this, the high cost of deploying dedicated sensing fibres or extra lasers remains a major obstacle for widespread operator adoption. To solve this, our joint R&D initiative between Bangor University’s DSP Centre of Excellence, Sorrento, and Comtek Networks has focused on developing a breakthrough "Data-Driven Sensing" architecture. By enabling the live, active data-carrying signal itself to act as the sensor, we classify and localise fibre faults with ~98% accuracy, all with no extra fibre assets, no additional lasers, and no downtime. This matters because it eliminates the massive capital overhead of traditional standalone DAS monitoring. It allows operators to protect critical backbone routes and detect "near-miss" physical threats using the active, revenue-generating fibre you already have in the ground. Finally, the presentation outlines a forward-looking research roadmap for developing this technology to simultaneously monitor the physical infrastructure running alongside most fibre networks.

### NetUK Welcome
Speakers: Pumford, Dave (PTX Technologies / NetUK)
page: https://indico.netuk.org/event/3/contributions/50/
Welcome to NetUK3!

### Evaluation of BGP Roles (RFC 9234) with the aid of an AI Assistant
Speakers: Lucek, Julian (HPE)
page: https://indico.netuk.org/event/3/contributions/51/
LLMs have greatly improved recently with the advent of reasoning models. We will set the scene by showing the results of LLM benchmarking tests against networking certification exams. We will then show an example in which an LLM, in conjunction with a Junos MCP server, configures, tests and documents BGP Roles (RFC 9234).

### Telecoms Inventory for GPON using Kuwaiba
Speakers: Maltby, Corey (Solent University), Gallen, Craig (Entimoss and Solent University)
page: https://indico.netuk.org/event/3/contributions/59/
[Kuwaiba][1] is an open source telecoms inventory solution which originated in South America but is increasingly gathering attention from service providers globally. It provides the power of many commercial systems which model network physical and logical resources and services at a significantly lower cost. Recently a group of students from Solent University did an industrial consulting project to evaluate how easy it would be to design and model a city wide GPON network in Kuwaiba using data imported from UK UPRNs and OpenStreetmap GIS information. This talk will provide a fascinating introduction to what the Kuwaiba project is and how it could be adopted as a tool by ISPs and service providers in the UK. [1]: https://www.kuwaiba.org/

### Building a National NOG Community
Speakers: Mitchell, Keith
page: https://indico.netuk.org/event/3/contributions/44/
netUK's predecessor organisation, the United Kingdom Network Operators' Forum (UKNOF), ran over 50 conferences and operated community platforms for British Internet infrastructure providers and professionals between 2005 and 2023. This talk, by UKNOF's founder, is a retrospective of that time, from UKNOF's early volunteer high-energy ad-hoc formation, through its growth and success, to one of the largest national Network Operator Groups (NOGs) globally, by way of pandemic adaptions, and latterly sustainability challenges. As well as looking at some high-note presentations, tools, fun anecdotes and various numbers, the theme of professional development through community building runs through everything that UKNOF did. Another important thread is openness of participation to all, in the true spirit of international Internet bodies such as RIPE and IETF. There will also be reflections on what worked, and what didn't, including the benefits and limitations of a strongly pragmatic approach to governance, together with some lessons learned for the long-term sustainability of nonprofit entities in the Internet operations space.

### LON2 Network Refresh
Speakers: Kayser, Jan (LINX)
page: https://indico.netuk.org/event/3/contributions/58/
LON2 was originally launched in 2002 following LON1’s increasing popularity and was created to ensure there was no critical single point of failure in the UK’s internet connectivity. LINX’s dual LAN infrastructure design in London has been something that sets us apart over the years from other Internet Exchange Points. Operating a redundant, diverse and resilient solution in house for members means not having to look elsewhere for this critical capability. In 2018 LINX announced that they were the world’s first IXP to deploy a disaggregated network using EVPN, with hardware and software sourced from alternative vendors. However, with end of life equipment, how did LINX refresh a LAN with 1/3 of its membership on without issues... or was there?

### NetUK Update
Speakers: Wenban-Smith, Nick (Nominet)
page: https://indico.netuk.org/event/3/contributions/49/
Updates about NetUK including the finances

### SCION: Secure Path-Aware Internet Routing for Critical Infrastructures
Speakers: Meynell, Kevin (SCION Association)
page: https://indico.netuk.org/event/3/contributions/45/
The Internet routing system (BGP) is rarely considered when discussing cybersecurity even though this remains an insecure aspect of the network and is increasingly used as an attack vector. Even though measures such as RPKI have been developed in recent years to improve routing security, adoption has been limited and still do not address the fundamental issue of limited control over where data is transiting. SCION is a secure path-aware Internet architecture designed to address many of the limitations of BGP by offering high resilience to routing attacks and path selection for Internet users and operators. The ability to use Internet connections from different ISPs can be more flexible and cost effective than relying on dedicated point-to-point links, but the commodity Internet is not able to provide sufficiently trustworthy, reliable and resilient connections for many critical infrastructures, especially those with safety critical traffic. Having the ability to control the paths that traffic is sent through intermediate networks, is also important for reducing the possibilities for traffic interception, reconnaissance, man-in-the-middle and denial-of-service attacks, as well as ensuring that data can be geofenced especially looking towards a post-quantum world. SCION addresses many of the existing issues with how traffic is sent over the Internet, including the issues of network trust, path selection, fast failover, and control over where data is transiting. It implements a trust model based around logical groupings of networks sharing a common jurisdiction with agreed trust policies and a standalone trust root (i.e. one that is not reliant on third-party Certificate Authorities) to validate the networks. This ensures that traffic is only exchanged between networks that are members of a trust domain, except that traffic which is explicitly allowed to be exchanged with other trust domains and the rest of the Internet. In particular, this allows truly sovereign networks to be built and operated. SCION has commercial and open-source implementations and is already in production use in the Swiss financial services, healthcare and power utility industries, as well as being evaluated by other sectors (e.g. defence) running critical infrastructures. It is also being developed as an vendor-neutral IETF specification. This proposed talk will discuss the use cases and the SCION design, architecture and trust mode. It will also discuss how SCION is deployed and how it compares with other current and proposed solutions such as RPKI, MPLS, SD-WAN, Segment Routing and BGPSEC.

### Edge Network Evolution
Speakers: Ryall, Ben (Meta), Cleary, Ian (Meta)
page: https://indico.netuk.org/event/3/contributions/60/
This short talk outlines how Meta's edge infrastructure is evolving to meet the demands of changing workloads — from traditional content delivery to emerging AI-driven experiences. The speaker explains how Meta's network topology is being reshaped to solve for both efficiency and quality of experience, ensuring that networks of all sizes continue to have access to direct, 1:1 peering relationships with Meta. The speaker demonstrates how these architectural shifts help connect people with Meta's apps and services while landing optimisations that enable operators to defer or avoid capital expenditure and deliver quality improvements for ISPs

### Which in my switch? LPO, CPO, XPO optics. What are they, when to use
Speakers: Friskney, Robert (Arista)
page: https://indico.netuk.org/event/3/contributions/61/
I will first detail what LPO (linear-drive pluggable optics) are versus traditional pluggables, and contrast CPO (co-packaged optics) with this, and their respective practical benefits such as cost, latency, power. I will talk about switch/routing use-cases where LPO wins over traditional pluggables today and vice versa - plus how this will evolve as port data-rates increase. Then I will talk about possible future evolution to much higher density with CPO and the benefits and challenges this brings, plus the alternative approach of XPO (extra-dense pluggable optics).

### The Network Automation Forum Framework: A vendor-neutral reference model for building automation at scale
Speakers: Crocker, Pete (OpsMill)
page: https://indico.netuk.org/event/3/contributions/63/
The Network Automation Forum spent the last year developing a common reference architecture that network engineers, vendors, consultants, and end-users can actually use. This talk walks through the framework architecture, explains why we needed standardised language around network automation, and shows how you can apply it whether you're starting from scratch or trying to make sense of what you already built. Reference: https://reference.networkautomation.forum/Framework/Framework/#presentation

## Lightning Talks
### Engaging with PeeringDB's Product Committee
Speakers: Vegoda, Leo (PeeringDB)
page: https://indico.netuk.org/event/3/contributions/64/
PeeringDB is both a directory of interconnection opportunities and an API enabling automation. Decisions on which features should be developed, improved, or changed sits with its volunteer Product Committee. But the Product Committee relies on PeeringDB's users to inform its decisions. This presentation will explain how and why to engage with the Product Committee. Attendees will then be asked to discuss how or why they'd use a feature or change currently being discussed. The specific issue to be discussed will be decided nearer the time as it is several months in the future.

### Operators Checklist for the October 11th DNSSEC KSK Rollover
Speakers: Groves, David (Nominet), Arends, Roy (ICANN)
page: https://indico.netuk.org/event/3/contributions/56/
This presentation explains what will happen on October 11th, and how to make sure your validating resolvers are up to date and ready for the event. The attached slide deck is based on Roy Arends from ICANN and is used with his permission. I will present his material, with a couple of modifications of my own.

### Everything is Fine and Our Automation Works Perfectly
Speakers: Funke, Stefan (Inter.link)
page: https://indico.netuk.org/event/3/contributions/67/
...as long as you update your IRR, give us RTBH fields, and fill out this survey.

## Workshop 2
### Workshop: Open Source Data Management Platform - Infrahub
Speakers: Gittings, Alex (OpsMill), Crocker, Pete (OpsMill)
page: https://indico.netuk.org/event/3/contributions/54/
Open-Source Infrastructure Data Management : Infrahub Workshop Infrahub reimagines infrastructure automation by combining Git-like version control capabilities on top of a graph database. The platform's three pillars - flexible schema, native version control, and unified storage - create an ideal teaching environment where participants can experiment with real-world scenarios in this hands-on workshop. Module 1: Foundation (40 minutes) establishes core concepts. Participants begin with Infrahub's sandbox environment, creating their first network objects and understanding the relationship between schema, data, and version control. This foundation addresses the immediate need for practical source of truth implementation. Lab 1: Network Source of Truth Setup (20 minutes) introduces participants to Infrahub's interface through basic device and IP address management tasks. Beginners focus on GUI navigation while advanced users explore CSV imports and API interactions. This foundational lab establishes confidence and familiarity with core concepts. Module 2: Config Generation (40 minutes) builds on foundational knowledge by connecting Infrahub to existing automation tools. After covering concepts around GraphQL queries and Jinja2 templating, we will cover generating device configurations. Lab 2: GraphQL Mastery (20 minutes) transforms participants from consumers to creators of network data queries. Using the built-in GraphiQL explorer, attendees progress from simple device queries to complex relationship traversals, preparing them for real-world data extraction and integration scenarios.

## Workshop 1
### Workshop: An Introduction to Data Centre Networks
Speakers: Mannay, Foeh (Xantaro), Shah, Utkarsh (Xantaro)
page: https://indico.netuk.org/event/3/contributions/53/
Given the rapid pace at which technology is evolving, there is a growing gap between fresh graduates and the expectations of entry- to mid-level roles. Many positions that previously required highly specialised expertise now demand a broader and more diverse skill set. At the same time, data centres networks have rapidly evolved for almost every type of organisation—including enterprises, colocation and service providers. Changes in business requirements, traffic types, patterns, applications and increased availability has redefined data centre architectures. In this context, we would like to propose a workshop that introduces the key concepts behind modern data centre networks and campus fabrics. The session would explore the inner workings of modern data centre fabrics, how interconnections extend across different environments, and the role telecommunications providers play within this ecosystem. We would also provide a brief overview of common tools and traffic flows. As data centres are now classified as Critical National Infrastructure (CNI) in the UK, we believe it is important to highlight their real-world importance and the need for designing highly available, high uptime and highly resilient architectures. As part of the workshop, we would present three practical real-world use cases to demonstrate how end-to-end networks operate in modern data centre environments. These examples would help illustrate the critical nature of these mission-critical systems and provide attendees with a clearer understanding of the broader picture. We would also briefly discuss the evolution of modern data centre networking, giving participants insight into how architectures have developed to support today’s scale, resilience, and performance requirements. To make the workshop engaging and interactive, we propose having two speakers, each covering a different dimension of the topic. Three real world case studies would further help tie theoretical concepts with real life applications for these architectures. These examples would help illustrate the critical nature of these mission-critical systems and provide attendees with a clearer understanding of the broader picture. We would also actively involve the audience throughout the session to ensure participants remain engaged and enthusiastic. There are no prerequisite requirements for the audience and we believe our talk will cover audiences with limited experience to computer networking as well as entry-level to mid-level network engineers.

