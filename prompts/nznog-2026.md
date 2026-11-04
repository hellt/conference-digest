>>> HOW TO RUN THIS <<<
This is the digest prompt for nznog-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/nznog-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/nznog-2026.md
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

Below is the program for NZNOG 2026 (operator). Read it and produce a digest
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
conference: NZNOG 2026
type: operator
source_url: https://www.nznog.org/conferences/nznog-2026/talks.html
generated: 2026-11-04
registry_key: nznog-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Accepted talks
### Radius Futures
Speakers: Alan DeKok
RADIUS has changed a lot since it was created in 1993, but not enough.  This talk will discuss real-world problems that impact people using RADIUS, and will show how “next generation” RADIUS standards can reduce these problems.

### Optimizing Traffic Flow with Akamai
Speakers: Kams Yeung
This presentation explores the unique aspects of Akamai’s content delivery network (CDN) deployment in New Zealand and provides best practices for optimising traffic flow. We will begin by examining the structure of the Akamai network within the country and its method for mapping traffic. We’ll delve into why traditional Border Gateway Protocol (BGP) traffic engineering techniques—such as AS path prepending, Multi-Exit Discriminator (MED), and using more specific routes—are often ineffective with Akamai’s intelligent routing system.
The second half of the presentation will offer practical recommendations for network operators. Key best practices include setting up and using dedicated DNS resolvers, maintaining complete and consistent route announcements, and avoiding traffic filtering. We’ll also highlight the importance of avoiding Carrier-Grade Network Address Translation (CGNAT) and recommend the adoption of IPv6 to enhance performance and connectivity.

### Tuatahi First Fibre: Network Update
Speakers: Murray Pearson
Tuatahi First Fibre is delivering Project Manawanui, migrating our legacy Huawei GPON access network to a new Adtran-based architecture. Aggregation migration has been completed, with the programme now focused on staged regional access cutovers. Whanganui was migrated last year, with New Plymouth next as the rollout continues. This involves OLT replacement, large-scale service migration, and integration into updated operational systems while maintaining continuity across a live production network.
In parallel, we are modernising the TCFL aggregation layer to prepare the network for future service and capacity growth, including enabling service handover at Napier, Hastings, or Rotorua. We have also launched a 100G handover product on the Adtran platform, with several 100G NNI migrations already completed.
The presentation will provide a technical update on current progress, architecture changes, and migration sequencing, along with lessons learned — including the multicast replication issue encountered during Whanganui — as we execute vendor transition and scale to 100G within a regional GPON/XGS-PON network.

### Enable Network Transformation Programme & Migration Journey
Speakers: Richard Lake, Brent Williamson, Mudassar Shahzad
This talk provides a high‑level overview of Enable’s Network Transformation Programme, outlining the strategic drivers behind the transformation and the journey undertaken to modernise the network and software stack. It covers the migration approach, key milestones, and the operational and customer impacts, with a focus on how Enable is evolving its network to support future growth, resilience, and service innovation.

### Designing a Mikrotik CGNAT Solution that Scales
Speakers: Matthew Enger
After upgrading their CGNAT infrastructure in Leaptel’s main points of presence, Matthew found himself with lots of Mikrotiks and decided to take what he learnt from the commercial solutions to develop a redundant CGNAT solution that scales and does not cost the earth. This presentation takes you though step by step his solution allowing any ISP to grab some Mikrotiks and deploy while meeting their law enforcement requirements at the same time.

### Datagrid: Unlocking the Potential of New Zealand’s South Island
Speakers: Pierre Goiffon
New Zealand’s South Island is rapidly emerging as one of the most compelling locations for next-generation AI data centers. With abundant renewable energy and a naturally cool climate, the region offers a rare combination of sustainability, scalability, and resilience.
In this presentation, Datagrid will outline its vision and roadmap for a 280MW data centre in Invercargill, alongside the Tasman Ring Network submarine cable project. We will explore how Invercargill and the wider South Island can become a critical hub on the global AI infrastructure map. The session will also examine the vital role of both international and domestic connectivity in achieving this vision, and detail Datagrid’s plans to strengthen connectivity across the South Island and New Zealand as a whole.

### Rethinking NetOps with Open-Source LLMs & RAG
Speakers: Basem Al-Sabri
This session presents a practical path forward using open-source Large Language Models (LLMs) combined with Retrieval-Augmented Generation (RAG). By grounding LLM reasoning in an organisation’s own knowledge base, configurations, and logs, RAG significantly reduces hallucinations and enables accurate, context-aware responses without sending sensitive operational data to third-party vendors. The architecture leverages fully open-source components across data ingestion, vector retrieval, inference, and orchestration, giving operators full control over data sovereignty and compliance while eliminating vendor lock-in and usage-based fees.

### Using Open Rack V3 to Enhance your Data Centre Infrastructure
Speakers: Conrad Bullock
This session explores how the Open Compute Project, and in particular the Open Rack V3 (ORv3) standard offers a transformative approach for building Data Centres.
We will cover ORv3’s innovative design, which significantly improves efficiency, thermal management, and rack density. These features translate to lower operational costs, enhanced cooling for high-density computing, and simplified maintenance. ORv3’s modularity and flexibility directly support demanding workloads like AI and HPC, enabling seamless scalability and future-proofing your critical infrastructure.
We’ll also look at a case study of a New Zealand customer that has deployed ORv3 and achieved some real benefits.

### Comfortable Complexity of Network Overlays
Speakers: Claudiu Captari
Traditionally, network domains like the Carrier Core, Data Center, Campus, and Branch have been managed as isolated “snowflakes,” each relying on unique protocols and bespoke skill sets. This fragmentation leads to increased operational complexity, slower service deployment, and higher costs.
A “network transformation” focused on simplifying the architecture through protocol reduction and consistent operational models is required. eVPN becomes key to deliver consistent L2 and L3 services across any transport including VXLAN, MPLS, or SRv6, across all environments: Core, DC and Campus.

### The Evolution of Network Configuration Management
Speakers: Tim Raphael
Network configuration was once a hand-crafted task when protocols were relatively simple, and topologies infrequently changed. Now we’re building massive, highly resilient, and operationally complex networks that demand consistency at scale. During this talk we’ll take a journey through the evolution of configuration technologies and what we learned along the way. I’ll cover how we started to solve these problems and how we should be configuring networks into the future. We’ll be discussing scripting, imperative operations, workflows, playbooks, APIs, RPCs, declarative models, and intent-driven operations.

### Life in a ’90s ISP. VUW Internetworking Group and NetLink, 1992-1997
Speakers: Don Stokes
Early Internet development in NZ was spearheaded by Universities and the research and education community. As Internet services moved from experimental to commercial operations, most institutions moved away from providing Internet services outside of their own needs.
At Victoria University of Wellington, things went a little differently.
This is a little reminiscence of life when data rates were measured in kilobits per second, bandwidth costs in dollars per megabyte, modems sang, equipment was new and shiny (and often didn’t work), and there was a good chance that whatever you were working just hadn’t been done before - at least, not by anyone you knew that you could ask.

### Automated Network State Checking: Insights from the Field
Speakers: Joe Shaw
Dependability is the watchword for any telecommunications operator. Sound monitoring goes a long way to ensure continuity of service, but typically this relies on known existing metrics to be effective. When the network changes and these metrics are invalidated, it can be challenging to confirm there is no ongoing service impact for the end user.
This was the challenge that REANNZ faced in the past year as we undertook a hardware refresh affecting our entire domestic backhaul. Every service we deliver was required to be rehomed and reimplemented according to a new network architecture. To catalogue every possible service and establish individually, the evidence that would be required to prove their continuity after migration, would require an enormous time-investment and be prone to error. So instead, we developed a generalised service model and implemented automation with Python to reason from live data pulled from our network. New configuration was generated consistent with the requirements of our new hardware, and feedback produced at the time of implementation describing in clear detail a comparison between old and new running state. This model was iterated upon based on our learnings over time, until it could accurately verify even highly bespoke configurations.
In this presentation, I propose to demonstrate the workings of this system with case studies from our experience. I will explain the challenges we encountered and how they were overcome, and conclude how ultimately this work proved its worth for our membership.

### The Evolution of TCP Transport Protocols
Speakers: Geoff Huston
One of the fundamental challenges in packet-switched networking is the crafting of a feedback loop between the receiver and the sender to allow the sender to make efficient use of the available network resource. This presentation delves into this topic looking at various TCP flow control protocols and the relationship between the flow control protocol and network buffers. This has led to the reconsideration of explicit congestion notification and the growth of the BBR protocol.

### IPv6 Landscape in NZ : Has it Changed
Speakers: Dave Phelan
This will be an update from my 2023 deck that will track and highlight any changes with the operators in NZ.

### Evolving Optical Transport: 400G, Network Design, and Regional Diversity
Speakers: Abouzar Asadi
Optical transport has evolved rapidly, pushing the limits of physics to deliver ever increasing capacity over optical fibre. Advances in coherent modulation, digital signal processing, and open optical architectures are enabling higher capacity services across national and regional networks.
This session will showcase how Aotearoa New Zealand’s largest open access fibre network is delivering 400 Gbps optical capability nationwide, and outline the future technologies and innovations that will enable even higher capacity.
The presentation will unpack the engineering journey to 400G, including optical line system readiness, spectrum management, and coherent transceiver evolution. It will also highlight regional network developments at Chorus, focusing on diverse fibre ring design and protection strategies that strengthen resiliency and service continuity.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Speakers: Thomas Weible
Past approaches for maximizing the data capacity per fiber pair went for running more and more DWDM channels with grid spacings as small as possible. This meant that grid spacings shrank from 200GHz to 100GHz and then 50GHz with some applications even going for 25GHz. In recent years the bandwidth per channel kept increasing, as complex modulation schemes came into favor over ON-OFF-Keying which has been a staple in fiber optic communication for decades. Those increased per channel bandwidths of 400Gbps, 800Gbps and now pushing into the 1.6Tbps realm demand for larger grids to accommodate the spectrum necessary to operate such “Superchannels”. Especially the fact of coherent detection being “blind” to anything but its own wavelength has enabled interesting topologies that can omit filters altogether. Of course that comes at a cost of reduced flexibility. Learn how you can harvest some of those benefits by moving to 400GHz filters while keeping a lot of your flexibility. Keep your 10Gbps and below legacy signals on the same fiber as your fast stuff and easily reassign your bandwidth without the cost ROADMs.

### AST Space Mobile
Speakers: Simon Allard
2degrees has partnered with AST SpaceMobile, one of the leading companies in the satellite connectivity race. AST SpaceMobile’s array of satellites will provide mobile coverage where territorial networks can’t. 
This talk will outline how the technology works, how 2degrees is integrating the service into its network via a 2degrees built ground station, and more.

### Routeviews Update
Speakers: Philip Smith
RouteViews was initiated in 1995 at the University of Oregon to allow network operators see what their routing tables looked like from an external perspective. Over the years since, this community project has set up collectors in strategic locations around the world, allowing network operators a rich view of their routing announcements, and researchers a valuable resource for tracking the growth and variations in the global Internet infrastructure.
This presentation introduces the new team behind RouteViews, and shares the new latest developments in the project, now operated on behalf of the global Internet community by the Network Startup Resource Center (NSRC). Some of the developments are the API, a new BMP processor, How to use the RouteViews system as a network operator and what we are working on for the future.

### Open Fibre Standards
Speakers: Warren Finch
Extreme weather events such as Cyclone Gabrielle in February 2023 exposed the fragility of New Zealand’s communications infrastructure, particularly where fibre routes followed shared transport corridors or relied on limited physical diversity. While operators worked quickly to restore services, the event highlighted a broader challenge: the lack of a shared, open and structured view of national fibre infrastructure that could support resilience planning, coordination and post-incident analysis.
The Open Fibre Data Standard (OFDS) provides a common, open schema for describing terrestrial fibre infrastructure, including routes, nodes and ownership attributes, in a way that is interoperable and machine-readable. This presentation introduces how OFDS provides an open, consistent data model for describing terrestrial fibre networks in a way that can be shared, analysed, and reused across operators, regulators, researchers, and emergency planners. This presentation introduces OFDS from a New Zealand perspective, focusing on why open, standardised fibre data matters for operators and network engineers.

### Defending Multistakeholder Internet Governance
Speakers: Jodi Anderson
Updating on where WSIS+20 ended up and how we got there, and looking at what happens next, how it sits in the geopolitical context, and where the key opportunities are for the technical community to defend and promote MS Internet governance going forward

### Options for Data Centre Interconnect
Speakers: Matthew Hayes
With the rapid growth of data centres worldwide — including across New Zealand — the demand for connectivity between facilities is increasing. This presentation will outline several common approaches to Data Centre Interconnect (DCI), from physical-layer solutions to higher-layer technologies, explaining how each works and examining the pros and cons of each approach.  These models are critical to the success and growth of operators within the ANZ market as we start to experience the uptake of new services paradigms driven by Hyperscaler and Ai penetration.

### Experiments in Topology Visualization using BGP-LS (RFC-8571)
Speakers: Rick Williamson / Rob Simpson,
Rick Williamson (Helios Software AU) and Rob Simpson (Kordia Networks) will share their recent experimental journey with using BGP-LS (RFC 8571) as a practical source of live topology and Traffic Engineering data for network visualisation. The work began in a greenfields Public Safety Network based on coherent design rules but quickly evolved into an approach suitable for existing operational networks.
The session explores why BGP-LS exists, what operational problems it can solve for heterogeneous and organically grown networks, and how its data structures behave in real time. Through a demonstration on a remote lab network, we’ll show how link-state changes, failures, and metric adjustments propagate through BGP-LS and drive visual SPF and “what-if” simulations. We’ll also outline a low-risk approach for operators to trial BGP-LS in their own environments, and provide access to our experimental network and iOS visualisation client for hands-on exploration during the conference.

