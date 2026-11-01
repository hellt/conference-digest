>>> HOW TO RUN THIS <<<
This is the digest prompt for nanog-97. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/nanog-97.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/nanog-97.md
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

Below is the program for NANOG 97 (operator). Read it and produce a digest
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
conference: NANOG 97
type: operator
source_url: https://nanog.org/events/nanog-97/agenda/
generated: 2026-11-01
registry_key: nanog-97
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Monday, June 1, 2026

### Keynote: The SRE of AI: Engineering Network Reliability for the Tokenized Era
Speakers: Dave Schaeffer – Cogent Communications
Session: Monday, June 1, 2026, 10:30 - 11:15 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5543/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5543/20260530_Schaeffer_Keynote_The_Sre_v1.pdf | video: https://www.youtube.com/watch?v=NlPo32qAio4
Network reliability is critical to ensure AI functions effectively – from training LLMs to deploying mature models for applications and end-users. Network engineers may need to redefine their Service Level Objectives to prevent network instability from throttling GPUs and reducing their performance, as well as employ monitoring tools to ensure peak performance and minimize outages. As your data volume grows, this type of data-driven approach also enables the use of automation or code to handle traffic loads. When mature models are deployed for use in applications or by end-users, reliability challenges are amplified by the need to keep geographically dispersed locations in sync and available.

### Designing for Constrained Resource Environments
Session: Monday, June 1, 2026, 11:15 - 12:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5733/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5733/20260530_White_Designing_For_Constrained_v1.pdf | video: https://www.youtube.com/watch?v=wKjeIMgqaTA
Russ White – Nokia Many protocols and networks were designed for memory and processing power constraints. These constraints drove some of the complexity we face in protocol design, network design, and network operations. While we are currently in a relative "age of plenty"--relying on relatively fast general-purpose processors, specialized forwarding engines, and generous memory--things are changing rapidly. We are clearly on the tail end of this "age of plenty," and may be facing a new age of constrained resources. If the AI craze remains solid, we face a world with long lead times, lower memory availability, and higher expectations of the network. What can we learn from the last time we designed networks for resource constraints? What new lessons can we learn?

### Network Automation BoF (Evergreen I)
Speakers: Ryan Hamel – Zayo
Session: Monday, June 1, 2026, 13:30 - 15:00 PDT, Other Locations
page: https://nanog.org/events/nanog-97/content/5732/
If you are curious about network automation and/or software development, do not miss the Network Automation BoF at NANOG 97. We'll swap stories, share lessons learned, and talk about what's working (and what we wish we'd known) in implementing network automation and software development in general.

### Lessons From Scaling BPF To Detect RDMA Device Drivers Bugs In Real Time
Speakers: Prankur Gupta – Meta Platforms, Inc
Session: Monday, June 1, 2026, 13:30 - 14:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5659/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5659/20260530_Gupta_Lessons_From_Scaling_v1.pdf | video: https://www.youtube.com/watch?v=MbPCKIDUhmo
Training large models requires significant resources, and failure of any GPU or host can significantly prolong training times. At Meta, we observed that 17% of our jobs fail due to RDMA-related syscall errors, which arise due to bugs in the RDMA driver code. Unlike other parts of the kernel, RDMA-related syscalls are opaque, and the errors create a mismatched application/kernel view of hardware resources. As a result of this opacity and mismatch, existing observability tools provided limited visibility and DevOps found it challenging to triage – we required a new scalable framework to analyze kernel state and identify the cause of this mismatch. Direct approaches like tracing the kernel calls and capturing metadata involved in the systems turned out to be prohibitively expensive. In this talk, we will describe the set of optimizations used to scale tracking kernel state and the map-based systems designed to efficiently export relevant state without impacting production workloads.

### SONiC Hands-on Workshop - Data Center leaf-spine fabric design with Community SONiC - Part 1
Speakers: Sunny Schatz – The Linux Foundation, Saju Salahudeen – NOKIA
Session: Monday, June 1, 2026, 13:30 - 15:30 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5756/
, Additional Registration is required - https://nanog.org/events/n97-sonic-workshop/ SONiC (Software for Open Networking in Cloud) is an open-source Network Operating System (NOS) used in Hyperscaler, cloud and Enterprise networks. In this hands on workshop, we introduce participants to SONiC architecture followed by a step-by-step guide on configuring a leaf-spine data center fabric using SONiC. Each participant will be provided a dedicated independant infrastracture to perform the hands on exercices using Containerlab and community SONiC. Key takeaways from this session include a basic understanding of SONiC architecture and it's different components, preparing Containerlab to run SONiC nodes, SONiC management interfaces, SONiC/FRR CLI configuration of interfaces, BGP and EVPN. This workshop is hosted by the SONiC Foundation.

### The Hidden Costs of SSH at Scale (Remote Presentation)
Speakers: Brett Lykins – Amazon
Session: Monday, June 1, 2026, 14:00 - 14:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5776/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5776/20260530_Lykins_The_Hidden_Costs_v1.pdf | video: https://www.youtube.com/watch?v=0-SJYlzcMjI
SSH is the default transport for network automation. Netmiko, Ansible, Scrapli, ncclient: they all open SSH connections. At local latencies, nobody notices the cost. But across a WAN, SSH's 10-15 round-trip handshake becomes the bottleneck. At 150ms RTT, each connection burns over a second in protocol overhead before a single command runs. The fix isn't replacing SSH. Most devices only speak SSH, and that's not changing soon. The fix is moving SSH to the edge: a lightweight proxy co-located with the devices handles SSH over a 1-2ms local link, while the automation platform talks HTTPS over the WAN. The protocol tax drops from 10-15 round trips to 3. This talk covers what SSH actually costs on the wire, measured benchmarks at realistic latencies (4.1-5.3x speedup), the proxy architecture, and a decision framework for when to use SSH direct, an edge proxy, or native HTTPS. All benchmark code is open source.

### Show Me Your PRs
Speakers: steve ulrich – nexthop.ai
Session: Monday, June 1, 2026, 14:30 - 15:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5772/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5772/20260530_Ulrich_Show_Me_Your_v1.pdf | video: https://www.youtube.com/watch?v=YS2Jga6HO04
the networking industry has an "interesting" (i mean this in the most minnesotan way possible) relationship with open network operating systems. hyperscalers have been deploying them with considerable success for several years now. vendors have made marketing noise around SONiC support, and the trade press treats disaggregation as inevitable. yet practical, operator-focused discussion of what it actually takes to build and sustain an open NOS ecosystem remains remarkably thin on the ground. this talk expands on a lightning talk originally presented at NANOG 92 and attempts to tackle the uncomfortable middle ground between the hype and the reality. we'll dig into some of the common objections that (vendors) commonly lob. examples: - "yeah, but networking's special" - "yeah, but X is only for hyperscalers" - etc. the discussion will examine where these hold up and where they don't. this is not a vendor pitch. it's a concerned and somewhat cynical observer's perspective about what a durable open NOS ecosystem requires - technically, commercially, and politically.

### Designing Cloud Workloads For LEO Satellite Internet Users
Speakers: Sid Mathur – Fastah Inc.
Session: Monday, June 1, 2026, 15:00 - 15:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5783/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5783/20260530_Mathur_Designing_Cloud_Workloads_v1.pdf | video: https://www.youtube.com/watch?v=003DkohsosM
How do you design and optimize cloud-native applications and services for Low-Earth Orbit (LEO) satellite internet users? In this talk, we cover: - Traffic routing from a satellite user terminal to the internet, for both Starlink and Amazon LEO - The difference between static users and on-the-move users (aviation, maritime, and mobile fleets) - The role of hyperscaler clouds for apps and workloads - Private Network Interconnects (PNI), including the new AWS Interconnect "Multicloud" peering between AWS and Google Cloud regions - Hosting and failover decisions for low-latency applications across AWS, Google Cloud, and the peered regions - Application-level design patterns drawn from major cloud Reference Architectures By the end of the talk, you'll have a mental model of how satellite internet traffic differs from terrestrial traffic, and a set of design patterns to architect with for lowest latency or highest availability.

### SONiC Hands-on Workshop - Data Center leaf-spine fabric design with Community SONiC - Part 2
Speakers: Saju Salahudeen – NOKIA, Sunny Schatz – The Linux Foundation
Session: Monday, June 1, 2026, 16:00 - 17:00 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5805/
, Additional Registration is required - https://nanog.org/events/n97-sonic-workshop/ SONiC (Software for Open Networking in Cloud) is an open-source Network Operating System (NOS) used in Hyperscaler, cloud and Enterprise networks. In this hands on workshop, we introduce participants to SONiC architecture followed by a step-by-step guide on configuring a leaf-spine data center fabric using SONiC. Each participant will be provided a dedicated independant infrastracture to perform the hands on exercices using Containerlab and community SONiC. Key takeaways from this session include a basic understanding of SONiC architecture and it's different components, preparing Containerlab to run SONiC nodes, SONiC management interfaces, SONiC/FRR CLI configuration of interfaces, BGP and EVPN. This workshop is hosted by the SONiC Foundation.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Session: Monday, June 1, 2026, 16:00 - 16:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5750/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5750/20260601_Weible_Channelmania_Future_v1.pdf | video: https://www.youtube.com/watch?v=5L4p1kNxmHg
Thomas Weible – Flexoptix In the old days of traditional separation of IP and DWDM, there was no need for IP folks to care about much other than what they used on their routers/switches (while the transport team ran the DWDM infra). These past DWDM infra approaches for maximizing the data capacity per fiber pair went for running more and more DWDM channels with grid spacings as small as possible. This meant that grid spacings shrank from 200GHz to 100GHz and then 50GHz with some applications even going for 25GHz. Now in the age of IPoDWDM the bandwidth per channel keeps increasing, as complex modulation schemes come into favor over ON-OFF-Keying which has been the de facto standard so far. Those increased per channel bandwidths of 400Gbps, 800Gbps and now pushing into the 1.6Tbps realm demand for larger grids to accommodate the spectrum necessary to operate such “Superchannels”. Especially the fact of coherent detection being “blind” to anything but its own wavelength has enabled interesting topologies that can omit filters altogether. Of course that comes at a cost of reduced flexibility. Which means, IP folks now will need to understand the nuances of how coherent detection works, need for larger filters for 800Gbps and higher, and how 400GHz filters (key word here being COTS) would future proof your network by not only allowing you to grow to 1.6Tbps, but also allow backwards compatibility for legacy services on 50GHz, etc. Made by FLEXOPTIX Research - Gert and Thomas.

### NANOG 97 Peering Coordination Forum
Session: Monday, June 1, 2026, 17:00 - 18:30 PDT, Regency Ballroom
page: https://nanog.org/events/nanog-97/content/5802/
The forum provides time for attendees to meet and network with others in the peering community present at NANOG. Peering Representatives, who completed and submitted the form will have a dedicated highboy table for up to 2 representatives. They will be able to distribute business cards, and provide a white paper or 1 sheet marketing page. Please note: any other type of giveaway is not allowed. Complete the form here before May 15: https://www.nanog.org/events/nanog-97/peering/

## Tuesday, June 2, 2026

### The State of the Map: Advancing IP Geolocation via Geofeeds and RIR Standards
Speakers: Matthew Wilder – TELUS, Oliver Gasser – IPinfo, Luna – MaxMind, Tony Tauber – Comcast
Session: Tuesday, June 2, 2026, 10:00 - 11:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5749/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5749/20260530_Wilder_The_State_Of_v1.pdf | video: https://www.youtube.com/watch?v=-Cm7dO2zUVQ
, , Marcus Jackson – AWS , Mark Kosters – ARIN , , While IP addresses were never designed to carry geographic context, a range of web content on the modern Internet relies on geolocation for everything from content licensing and localized routing to fraud prevention and regulatory compliance. Historically, this data has been inferred through third-party "black box" databases, often leading to "digital sinkholes" and slow correction cycles for network operators. This panel brings together key stakeholders from ISPs, Geolocation Data Providers, and ARIN to discuss the standardization and operational evolution of Geofeeds (RFC 8805 and the recently matured RFC 9632 and 9877). We will explore how the industry is harmonizing an inference-based model with an operator-declared model, the challenges of maintaining data hygiene, and the role of Regional Internet Registries (RIRs) in providing a canonical discovery mechanism. Moderator: Matthew Wilder, TELUS Panelists: Luna, MaxMind Mark Kosters, ARIN Oliver Gasser, IPinfo Marcus Jackson, Amazon Tony Tauber, Comcast

### NetOps Stack for Core/Aggregation Operators of Any Size
Speakers: Mauricio Rojas – Nokia
Session: Tuesday, June 2, 2026, 11:00 - 12:00 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5785/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5785/20260524_Rojas_Netops_Stack_For_v1.pdf | video: https://www.youtube.com/watch?v=wjl_t_ozxNw
This tutorial offers a comprehensive demonstration of how network operators can modernize infrastructure using a Kubernetes-centric, open-source approach to enhance operational efficiency, simplify resource management, and provide a unified platform for advanced observability and configuration. You will witness the deployment of a foundational lab environment using Containerlab, followed by the integration of Prometheus and Grafana for real-time telemetry. We will explore GitOps-driven management with Flux, showcasing how intent-based configuration and SDCIO manage complex network elements like a Broadband Network Gateway (BNG). The demo dives into the practicalities of handling YANG schema imports, managing gNMIc subscriptions, and automating responses to configuration drift. Finally, we will cover the implementation of a unified platform for alarms and notifications using AlertManager. This session is designed for intermediate to advanced network operators who have a foundational understanding of container orchestration.

### Beyond Geofeeds: Towards a New Standard in Data Sharing
Speakers: William Stevenson – MaxMind, Inc.
Session: Tuesday, June 2, 2026, 11:00 - 11:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5752/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5752/20260530_Stevenson_Beyond_Geofeeds_Towards_v1.pdf | video: https://www.youtube.com/watch?v=aRi9HG-2xHo
, Kevin Phair Geofeeds allow Network Operators to guide geolocation providers about the locations of their networks. While some Network Operators are already adding additional fields, RFC 8805 A Format for Self-Published IP Geolocation Feeds, does not allow for extensibility or define metadata. "Beyond Geofeeds" will describe the current standard, explore general considerations in a new version, describe a possible implementation and invite others to iterate on it.

### Towards a Non-Binary View of IPv6 Adoption
Session: Tuesday, June 2, 2026, 11:30 - 12:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5748/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5748/20260530_Thottungal_Valapu_Towards_A_Non-Binary_v1.pdf | video: https://www.youtube.com/watch?v=zyPZ9mOl2tQ
Sulyab Thottungal Valapu – University of Southern California / Information Sciences Institute Twelve years have passed since World IPv6 Launch Day, but what is the current state of IPv6 deployment? Prior work has examined IPv6 status as a binary: can a user do any IPv6? As deployment increases, we must consider a more nuanced, non-binary perspective on IPv6: How much, and how often, can a user or a service use IPv6? We consider this question as a client, server, and cloud provider. Considering the client's perspective, we observe user traffic. We see that the fraction of IPv6 traffic a user sends varies greatly, both across users and day-by-day, with a standard deviation of over 15%. We show this variation occurs for two main reasons. First, IPv6 traffic is primarily human-generated, thus showing diurnal patterns. Second, some services lead with full IPv6 adoption, while others lag with partial or no support, so as users do different things their fraction of IPv6 varies. We look at server-side IPv6 adoption in two ways. First, we expand analysis of web services to examine how many are only partially IPv6 enabled due to their reliance on IPv4-only resources. Our findings reveal that only 12.6% of top 100k websites qualify as fully IPv6-ready. Finally, we examine cloud support for IPv6. Although all clouds and CDNs support IPv6, we find that tenant deployment rates vary significantly across providers. We find that ease of enabling IPv6 in the cloud is correlated with tenant IPv6 adoption rates, and recommend best practices for cloud providers to improve IPv6 adoption. Our results suggest IPv6 deployment is growing, but many services lag, presenting a potential for improvement.

### IXP BoF (Evergreen I)
Speakers: Jonathan Black – NANOG
Session: Tuesday, June 2, 2026, 13:30 - 15:00 PDT, Other Locations
page: https://nanog.org/events/nanog-97/content/5734/
If you run a Community Internet Exchange Point (IXP) or you’ve been thinking about starting one, don’t miss the Community IXP BoF at NANOG 97. We’ll swap stories, share lessons learned, and talk about what’s working (and what we wish we’d known) in building successful IXPs. Commercial IXPs are welcome to join the BoF, but the focus will be on building up community-based IXPs.

### From CLI to AI: A Network Engineer's Guide to Building Useful Agents
Session: Tuesday, June 2, 2026, 13:30 - 14:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5687/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5687/20260601_Lightfoot_From_Cli_To_v1.pdf | video: https://www.youtube.com/watch?v=Jc6MUU1DPMg
Du'An Lightfoot Everyone's talking about AI agents. Few are building them for real network operations. This talk walks through the practical journey of building network agents. From "should I even do this?" to production tradeoffs. We'll answer three questions network engineers are actually asking: 1. Do I need to build an AI Agent? Tools like Claude Code and ChatGPT can already call APIs and parse output. When is that enough? When does it break down? I'll show where off-the-shelf tools hit their limits with real network scenarios. 2. If I build an agent should it be hosted or self-hosted? Sending packet captures to OpenAI isn't an option for most of us. But self-hosted models come with their own challenges. I'll demo the same network troubleshooting workflow with Claude Code and Llama running locally to show exactly where each succeeds and fails. 3. What are the actual tradeoffs? Cost, latency, accuracy, data privacy, and the one nobody talks about: how much of your time it takes to build and maintain. I'll share what I learned building my own network agent with a network-mcp, an open-source MCP server that gives AI agents network diagnostic tools. You'll leave with a framework for deciding what to build, what to buy, and what to skip, based on your actual operational needs, not hype.

### DWDM Optical Networking Concepts and Technologies
Speakers: Chad Lamb – XKL
Session: Tuesday, June 2, 2026, 13:30 - 15:30 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5753/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5753/20260531_Lamb_Dwdm_Optical_Networking_v1.pdf | video: https://www.youtube.com/watch?v=oiZEHalEx64
This tutorial will cover Dense Division Wave Multiplexing (DWDM) technologies and how to use them. During the class, we will be covering: DWDM fiber concepts, such as channels, fixed grid, flex grid, bandwith, and mux/demux filters and other passive devices. Transceivers, transponder, and muxponder concepts (Modulation, Baud vs bit rates, form factors) Amplifier technologies ROADMs and other optical switching technologies Troubleshooting and testing At the end of the tutorial, the attendee will have gained a good overview of these concepts and will be able to build further on the knowledge learned.

### Workshop: Seeing the Invisible: Network Observability at Scale in AWS - Part 1
Speakers: Mandar Sridhar Alankar – Amazon Web Services Inc., Venkatesh VLNP – Capital One
Session: Tuesday, June 2, 2026, 14:30 - 15:30 PDT, Regency Ballroom
page: https://nanog.org/events/nanog-97/content/5760/
, Additional Registration is required - https://nanog.org/events/n97-aws-workshop/ Modern cloud networks move fast — and when things break, they break quietly. This hands-on workshop delivers a practical, end-to-end introduction to network observability in AWS, giving attendees the tools and techniques to achieve true visibility across hybrid and distributed cloud environments. We'll start at the foundation: telemetry collection — combining CloudWatch metrics, VPC Flow Logs, Site-to-Site VPN logs, passive monitoring via Network Flow Monitor and Internet Monitor, active probing with Synthetic Network Monitor, and deep packet inspection through Traffic Mirroring to build a layered strategy that covers everything from high-level KPIs to raw packet analysis. From there, we turn raw telemetry into actionable insight using native CloudWatch dashboards and Service specific dashboards, custom Logs Insights queries, Contributor Insights, and proactive alerting with CloudWatch Alarms — including AI-powered anomaly detection for shifting from reactive to predictive operations. Finally, we apply it all to real troubleshooting scenarios: validating network paths with Reachability Analyzer, identifying performance bottlenecks with Network Flow Monitor, and capturing packets with Traffic Mirroring when other signals fall short. Whether you're an SRE, Network engineer, Security practitioner, or DevOps specialist, you'll leave with hands-on experience and a clear framework for knowing what your AWS network is doing — before your users tell you it isn't. Pre-workshop Instructions: -Please bring your laptop (preferred: personal) for the hands-on lab. -Need not install any pre-requisite softwares, as a dedicated AWS account would be pre-allocated for each workshop participant.

### From Metrics to Investigation: How Agentic SRE Could Change Network Operations
Session: Tuesday, June 2, 2026, 14:30 - 15:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5766/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5766/20260530_Mahmud_From_Metrics_To_v1.pdf | video: https://www.youtube.com/watch?v=JdQOLTqPIy8
Mohibul Mahmud – Microsoft , Shamir Abdul Aziz , Karthik Srinivas Muthuramakrishnan – Microsoft Network operators spend the majority of incident response time on investigation, not remediation. Runbooks, scripts, and alert-driven automation handle known failure modes well — but when the failure is novel, investigation remains manual, serial, and slow. This talk presents a working agentic investigation system built on Azure that addresses the unknown-failure case. It demonstrates end-to-end network failure investigation including hop-by-hop topology discovery, protocol-level diagnostics across BGP, IKE Phase 1/2, and ExpressRoute, and a real production case where the agent detected a blackhole route from a deallocated firewall in under 35 seconds. The architecture combines large language model reasoning with structured tools (Azure CLI, Resource Graph, Network Watcher) and operator-authored skills written in Markdown. The session covers four practical scenarios: live natural-language troubleshooting, scheduled monitoring with alert integration, topology discovery from minimal input, and protocol-level analysis for hybrid connectivity (ExpressRoute, VPN, vWAN). It also covers what doesn't work yet — read-only as the enterprise default, on-prem coverage requiring telemetry forwarding to Log Analytics, and human approval as a hard requirement before any write action. Attendees will leave with a concrete picture of where agentic investigation fits in network operations today, what the integration boundaries look like, and how to evaluate whether this approach belongs in their own environments.

### ARIN Update
Session: Tuesday, June 2, 2026, 15:00 - 15:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5739/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5739/20260530_Sweeting_Arin_Update_v1.pdf | video: https://www.youtube.com/watch?v=pe3HAOkK1yE
John Sweeting – American Registry for Internet Numbers Join ARIN’s Chief Experience Officer for a timely update on Internet number resources, including IPv6 adoption, IPv4 availability, and RPKI developments. Learn about current policy proposals, election participation, community programs, and how ARIN continues to support network operators and the broader Internet ecosystem.

### Workshop: Seeing the Invisible: Network Observability at Scale in AWS - Part 2
Speakers: Mandar Sridhar Alankar – Amazon Web Services Inc., Venkatesh VLNP – Capital One
Session: Tuesday, June 2, 2026, 16:00 - 18:00 PDT, Regency Ballroom
page: https://nanog.org/events/nanog-97/content/5806/
, Additional Registration is required - https://nanog.org/events/n97-aws-workshop/ Modern cloud networks move fast — and when things break, they break quietly. This hands-on workshop delivers a practical, end-to-end introduction to network observability in AWS, giving attendees the tools and techniques to achieve true visibility across hybrid and distributed cloud environments. We'll start at the foundation: telemetry collection — combining CloudWatch metrics, VPC Flow Logs, Site-to-Site VPN logs, passive monitoring via Network Flow Monitor and Internet Monitor, active probing with Synthetic Network Monitor, and deep packet inspection through Traffic Mirroring to build a layered strategy that covers everything from high-level KPIs to raw packet analysis. From there, we turn raw telemetry into actionable insight using native CloudWatch dashboards and Service specific dashboards, custom Logs Insights queries, Contributor Insights, and proactive alerting with CloudWatch Alarms — including AI-powered anomaly detection for shifting from reactive to predictive operations. Finally, we apply it all to real troubleshooting scenarios: validating network paths with Reachability Analyzer, identifying performance bottlenecks with Network Flow Monitor, and capturing packets with Traffic Mirroring when other signals fall short. Whether you're an SRE, Network engineer, Security practitioner, or DevOps specialist, you'll leave with hands-on experience and a clear framework for knowing what your AWS network is doing — before your users tell you it isn't. Pre-workshop Instructions: -Please bring your laptop (preferred: personal) for the hands-on lab. -Need not install any pre-requisite softwares, as a dedicated AWS account would be pre-allocated for each workshop participant.

### NANOG Community Meeting
Session: Tuesday, June 2, 2026, 16:00 - 16:45 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5804/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5804/20260602_Wittkop_Nanog_Community_Meeting_v1.pdf | video: https://www.youtube.com/watch?v=Nw19sfpTeQ8
Don’t miss our Community Meeting for an opportunity to hear about what is happening within the NANOG organization and the various NANOG Committees.

### What's New at the IETF
Speakers: Yingzhen Qu – Futurewei Technologies
Session: Tuesday, June 2, 2026, 16:45 - 17:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5762/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5762/20260530_Qu_What_S_New_At_v1.pdf | video: https://www.youtube.com/watch?v=wvkKX4jFvv8
, Yaroslav Rosomakho – Zscaler This presentation provides an overview of recent developments, ongoing work and emerging directions at the Internet Engineering Task Force (IETF). The talk introduces the IETF’s organizational structure—including its working groups, research activities under the Internet Research Task Force (IRTF), and architectural guidance from the Internet Architecture Board (IAB). It also covers key areas of active work across the IETF.

### Tuesday Lightning Talks
Speakers: Leslie Daigle – Thinking Cat Enterprises, Wim Henderickx – Nokia
Session: Tuesday, June 2, 2026, 17:30 - 18:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5799/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5799/20260602_Daigle_Tuesday_Lightning_Talks_v1.pdf | video: https://www.youtube.com/watch?v=nTZ7FWy1WWU
, , Esther Jang **More MANRS to Love** presented by Leslie Daigle Mutually Agreed Norms for Routing Security (MANRS) is evolving — and we want the community's eyes on what's coming. This lightning talk offers an early look at two initiatives currently in development: revised action requirements for network operators and a new MANRS Enterprise Program. We'll briefly recap the core MANRS framework before previewing the proposed netops action updates — the direction of travel, the rationale behind the changes, and where things stand today. We'll then introduce the Enterprise Program concept: who it's intended to serve, how it will differ from the existing programs, and what participation could look like. This is a work in progress. If you're an operator with a stake in how the updated actions take shape, or an enterprise network team wondering whether MANRS might soon have a home for you, come hear what's in the works and help us get it right. **Automation patterns** presented by Wim Henderickx Network automation is no longer just about generating configurations. As automation systems become larger and more collaborative, new challenges emerge: lifecycle management, customization, reconciliation, and operational change management. This talk shares two practical automation patterns that have repeatedly appeared across multiple projects: Ownership, which helps systems manage resource lifecycle and state transitions, and Overlays, which allow operators and automation systems to customize intent without creating copies or forks. Rather than proposing a new framework, this session aims to share experiences and invite discussion. What automation patterns keep appearing in your environment, and should they become first-class capabilities of our automation platforms? **Seattle Community Network** presented by Esther Jang The Seattle Community Network (SCN) project (https://seattlecommunitynetwork.org/) is a non-profit community-run internet access initiative to improve digital equity for vulnerable and low-income groups in the Puget Sound area. Our ongoing projects focus on installing and managing WiFi networks at Tiny House Villages and other homeless shelters. We also refurbish and distribute internet access devices such as laptops and phones at homeless shelters and low-income housing. In this talk I will briefly outline a vision for this organization, to bridge computer experts and hackers who are able to spend time and resources volunteering for community technology initiatives with low-income communities who have been left behind in terms of digital infrastructure.

## Wednesday, June 3, 2026

### 50 Years of Networking
Speakers: Geoff Huston – APNIC
Session: Wednesday, June 3, 2026, 10:00 - 10:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5621/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5621/20260530_Huston_50_Years_Of_v1.pdf | video: https://www.youtube.com/watch?v=Umtxxz7GyFc
Ethernet is now 50 years old. In this presentation, I will look at what the evolution of computer networking over the past 50 years has achieved, and then look at the implications of this for the coming years. While an open collaborative process of technology and standards development have been the cornerstone of the past 50 years, will they continue to be fundamental aspects of the coming decades? What factors have shaped today's environment, and how will they influence future directions?

### Adopting NETCONF on Router Side (Remote Presentation)
Speakers: Maria Matejka – BIRD | CZ.NIC
Session: Wednesday, June 3, 2026, 10:30 - 11:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5769/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5769/20260530_Matejka_Adopting_Netconf_On_v1.pdf | video: https://www.youtube.com/watch?v=SmoFF3TEZIc
NETCONF is the new standard of configuring network devices. Its adoption isn't always smooth though. The schema definition language, YANG, has its quirks and caveats, and there are also encoding problems. We'll touch some examples and describe various situations of no good solutions. In the end, all these findings made a string base for a conclusion of what the BIRD developers chose to implement.

### Versioned Services for Network Automation
Speakers: James Henderson – Ductus
Session: Wednesday, June 3, 2026, 10:30 - 11:00 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5673/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5673/20260601_Henderson_Versioned_Services_For_v1.pdf | video: https://www.youtube.com/watch?v=uai6k0JcUdk
Network automation is intended to help operators reliably manage large networks as they grow and change. In practice, however, automation systems often become difficult to reason about once standards evolve, services diverge, and production networks accumulate history. This talk presents a practical pattern for managing that complexity using versioned services, named service types, managed features, and cascading types. Using EVPN as an example, it shows how service intent can include not only service parameters, but also the version of the automation standard used to realize them.

### The Kimwolf Aftershock: Residential Proxy Botnets One Year Later
Session: Wednesday, June 3, 2026, 11:00 - 11:30 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5771/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5771/20260531_Labovitz_The_Kimwolf_Aftershock__v1.pdf | video: https://www.youtube.com/watch?v=eOmeQcwSK3o
Craig Labovitz – Nokia , Chinni Tadivaka At NANOG 94, we warned that DDoS attackers had weaponized the more than 100 million endpoints in the global residential proxy ecosystem. The following 12 months bore out that warning: Kimwolf residential proxies launched record breaking attacks in the tens of terabits per second across thousands of incidents, including several that disrupted critical infrastructure. One year on, this talk assesses what has and hasn't changed. Law enforcement actions and provider takedowns significantly degraded Kimwolf, but successor botnets rapidly filled the void using the same residential exploits. More concerning, daily active DDoS botnet endpoints climbed from roughly one million in summer 2025 to over eight million today, and aggregate bandwidth capacity remains in the hundreds of terabits per second. We close by examining the industrial-scale AI scraping demands driving residential proxy growth and what this means for defenders. This talk is joint research between Comcast Threat Research Lab (CTRL) and Nokia Emergency Response Team

### Vendor Independent Network Segmentation
Speakers: Brian Jemes – University of Idaho
Session: Wednesday, June 3, 2026, 11:00 - 12:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5777/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5777/20260530_Jemes_Vendor_Independent_Network_v1.pdf | video: https://www.youtube.com/watch?v=aNvGdvI9akE
This presentation will describe a vendor independent network segmentation architecture for the enterprise network that will 1) minimize network blast radius, 2) minimize network attack surface, and 3) minimize network cost. This presentation will share implementation details and lessons learned at the University of Idaho.

### Mix and Match BGP - Another Way to Think About Architecture
Speakers: Barrie Cook – Barrie Jones Cook Consulting LLC
Session: Wednesday, June 3, 2026, 11:30 - 12:00 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5782/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5782/20260531_Cook_Mix_And_Match_v1.pdf | video: https://www.youtube.com/watch?v=E5XCCg-8Ohc
Most of us have at one point struggled with understanding all the components of layer 3 architecture, such as: why do you need an IGP in addition to iBGP and eBGP? Anyone we want to join the industry will probably have to do so too, so why not try to come up with a simpler way to think about it? We'll sift through auction sites for vintage books and toys to find an unlikely template: the mix & match character with swappable head, torso and legs that can stand in for some of the more esoteric concepts. There'll be plenty of time for discussion and Q&A, so whether you have decades of BGP experience or are actively struggling with these concepts as we speak, join us as we decide if this model really does have legs. And who knows? We may find new perspectives or mentorship along the way.

### Monitoring 2,800 BGP Sessions using BMP Protocol
Speakers: Pavel Odintsov – FastNetMon Inc
Session: Wednesday, June 3, 2026, 14:00 - 14:45 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5773/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5773/20260531_Odintsov_Monitoring_2_800_Bgp_v1.pdf | video: https://www.youtube.com/watch?v=lI5RxNt6jYc
BGP monitoring at scale breaks traditional tools. SNMP, gNMI, and full-table dumps fall short on real-time, per-peer visibility in large multi-vendor networks. This talk shows why - and backs it with production benchmarks. We then dive into BMP as a purpose-built solution for full-fidelity BGP telemetry. Finally, we share how we monitor thousands of sessions and tens of millions of routes in production using a BMP-based pipeline.

### Gray failures in AI Fabric
Speakers: Navtej Singh – Clockwork
Session: Wednesday, June 3, 2026, 14:00 - 14:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5774/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5774/20260531_Singh_Fabric_Is_Sexy_v1.pdf | video: https://www.youtube.com/watch?v=qR_Bvs3AXX0
For a decade, data center fabric was the boring part of the stack. CLOS topologies, ECMP, and 100/400G optics mostly just worked for the cloud and CDN workloads that dominated the 2010s. Then AI training arrived. A synchronous collective across tens of thousands of GPUs is gated by its slowest participant, and the fabric (long presumed healthy if every link was up and every BGP session was stable) became the throughput ceiling. This talk is about the class of failures operators are now burning hours on: gray failures. Links that are nominally up but quietly corrupting. Optics degrading through rising FEC correction counts before they ever go down. ECMP hash polarization that lands an all-reduce on a single hot path. PFC headroom exhaustion that never trips a threshold. Microbursts invisible to any 30-second SNMP poll. None of these show up on the NOC wall. All of them show up on the compute bill. Drawing on production examples from AI fabrics, this session walks through what gray failures look like in real telemetry, why standard tooling (polled SNMP, sampled flow, ping/iperf) systematically misses them, and which techniques (high-resolution synchronized timestamping, tail-latency percentiles, streaming telemetry, host-side straggler correlation) catch them before a training job silently loses throughput across a multi-week run. The operations skills this community already has are load-bearing again. This talk is about what to re-tool, and what to keep.

### Network OS Upgrades at Hyperscale
Session: Wednesday, June 3, 2026, 14:30 - 15:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5754/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5754/20260531_Sekar_Rajan_Network_Os_Upgrades_v1.pdf | video: https://www.youtube.com/watch?v=3LuwTsGvx8I
Sujitha Sekar Rajan – Meta Platforms Inc Large-scale network operators running multi-vendor environments face a recurring challenge: how to upgrade network operating systems across thousands of devices without compromising reliability. Upgrade too slowly and you accumulate security exposure, vendor end-of-life risk, and missing capabilities. Upgrade too fast and vendor regressions, configuration incompatibilities, and multi-vendor interaction failures can cause production incidents. Therefore, managing network OS upgrades across tens and thousands of multi-vendor devices demands a disciplined approach to testing, deployment, and incident response.This talk walks through the system we built to do it safely and repeatedly: a vendor-agnostic qualification pipeline, an automated test framework with tag-driven selection for both routine releases and emergency response, progressive canary deployment gated by automated health checks, and a severity-calibrated emergency rollout process. We share two production war stories that shaped the pipeline, covering silent forwarding plane failures and a multi-vendor optics interoperability issue spanning three vendors on a single link.

### Paraglider: Streamlining Cloud Networking
Session: Wednesday, June 3, 2026, 14:45 - 15:30 PDT, Grand Ballroom H-K
page: https://nanog.org/events/nanog-97/content/5770/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5770/20260531_Mcclure_Paraglider_Streamlining_Cloud_v1.pdf | video: https://www.youtube.com/watch?v=WCwhY4D3eKA
Sarah McClure – UC Berkeley As multi-cloud deployments become the standard, network operators are increasingly burdened by the manual, error-prone task of managing disparate, vendor-specific, and low-level networking primitives. Paraglider addresses this challenge directly; what began as a UC Berkeley research project focused on defining the right cloud networking abstractions has evolved into a collaborative open-source project with contributors from several major cloud providers. In this talk, we explore Paraglider’s architecture and demonstrate how it enables operators to manage connectivity through high-level intent and policy rather than fragmented configurations. To make the the benefits of the Paraglider abstractions more concrete, we will feature a demo showcasing how Paraglider automates the orchestration of complex inter-cloud topologies.

### Migrating From Bespoke Hardware To An Open Load Balancing For Kubernetes
Speakers: Sergey Kolobov, Marcin Wojciechowski
Session: Wednesday, June 3, 2026, 15:00 - 15:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5740/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5740/20260531_Kolobov_Migrating_From_Bespoke_v1.pdf | video: https://www.youtube.com/watch?v=IOXM7ur8QS0
, This presentation outlines the technical journey and operational best practices for migrating from a high-throughput, bespoke stateless HW load balancer to an open, standardized solution using MetalLB in BGP mode for Kubernetes LoadBalancer services. We detail the architecture of using BGP to advertise service IPs and leverage Equal-Cost Multi-Path (ECMP) routing across the network fabric for per-connection load balancing. The core focus is on solving the critical networking challenge inherent to stateless ECMP: mitigating the widespread connection resets that occur when a backend node is removed. We present the network-side solution, including the implementation of resilient ECMP configuration on ToR switches to stabilize the hashing algorithm, alongside essential operational considerations for ingress node physical distribution and the resultant shift to a stricter port exposure security model. This talk provides actionable insights for network engineers and Kubernetes platform teams seeking to build scalable, production-ready, BGP-native load balancing infrastructure.

### Boring is Good: Removing Emotion from Incident Response
Speakers: Ryan Hamel – Zayo
Session: Wednesday, June 3, 2026, 16:00 - 16:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5737/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5737/20260603_Hamel_Boring_Is_Good__v2.pdf | video: https://www.youtube.com/watch?v=L6SRQ5RCMSo
We've all been there: it's 3AM, the pager fires, and the only person who knows what to do is asleep in another timezone. If your incident response looks different depending on who's on call or what time it is, that's not a staffing problem, it's a systems problem. This talk argues that "boring" is the highest compliment you can pay your operations. Drawing from hands-on experience automating a Tier-1 IP backbone, I'll walk through a practical framework built on three pillars: architecture that isolates failure domains so outages stay small, automation that actually heals infrastructure instead of just screaming about it, and documentation that lives in runbooks, not in someone's head. The goal is simple: the same incident should produce the same response whether it's a Tuesday afternoon or Christmas morning. I'll also talk about tabletop exercises, chaos engineering, and how to get your org to treat reliability as a first-class investment rather than an afterthought. The benchmark I keep coming back to: if a junior engineer three months into the job can't handle the same incident as your senior DBA, you have homework to do. Boring isn't lazy, it's disciplined, and it's how your team sleeps through the night.

### Peering risk Intelligence (Remote Presentation)
Speakers: Jay Dave
Session: Wednesday, June 3, 2026, 16:30 - 17:00 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5692/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5692/20260531_Dave_Peering_Risk_Intelligence_v1.pdf | video: https://www.youtube.com/watch?v=z8enyVSHf7A
Network operators make peering decisions based on incomplete information - PeeringDB profiles, gut feel, and word of mouth. But what if you could answer "Is this network safe to peer with?" using data? This talk introduces Route Sherlock, an open-source CLI tool that provides Peer Risk Intelligence for network operators. It combines data from RIPEstat, PeeringDB, and BGPStream to generate a quantified risk score for any ASN, helping you make informed peering decisions before establishing BGP sessions. Key features demonstrated: - Peer risk scoring algorithm (stability, incident history, network maturity) - Historical incident backtesting against real BGP archives - AI-powered synthesis of complex routing data - Practical safeguards based on risk level (prefix limits, IRR filtering) A demo includes scoring real networks and backtesting against the June 2024 Cloudflare 1.1.1.1 route leak. Attendees leave with a free, open-source tool they can use immediately.

### Crafting Network Configurations at Meta
Speakers: Santiago Alfonso Munoz Rodriguez – Meta
Session: Wednesday, June 3, 2026, 17:00 - 17:30 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5671/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5671/20260531_Munoz_Rodriguez_Crafting_Network_Configurations_v1.pdf | video: https://www.youtube.com/watch?v=LaElarEazy4
Running Meta’s backbone involves managing updates to the configuration of thousands devices spread across different roles and vendors on a daily basis. The rapid capacity growth increases the need for more hardware, vendor diversity and new topologies with tight time-to-market constraints, meaning we need to be able to onboard new platforms and changes to existing ones in record timelines. This talk describes how Meta’s configuration systems handle the complexity of authoring, validating and generating the payloads that are delivered to the fleet at scale. In particular, we will show how we streamline traditional network engineering functions to provide the benefits of automation without needing to deploy new processes or write code, and how we leverage concepts from the compiler world to operate a multi-protocol, multi-vendor network as if it were a single-vendor one.

### Wednesday Lightning Talks
Speakers: Oliver Gasser – IPinfo, John van Oppen – JvO Squared
Session: Wednesday, June 3, 2026, 17:30 - 17:50 PDT, Grand Ballroom A-G
page: https://nanog.org/events/nanog-97/content/5800/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG97/5800/20260603_Gasser_Wednesday_Lightning_Talks_v1.pdf | video: https://www.youtube.com/watch?v=zliJCs4ZExE
, **Signaling end-user prefix sizes using prefixlen files** presented by Oliver Gasser IP addresses or prefixes are often times used as a proxy to identify users. When multiple users are sharing a prefix or even an IP address in the case of Carrier Grade NAT, this can have negative consequences for other users, such as being detected as a bot, needing to solve CAPTCHAs, or their access simply being blocked. In this lightning talk I'll present prefixlen files as a way to solve this. Prefixlen files have been recently (last week) standardized by the IETF as RFC 9977. The talk's goal is to make network operators as well as service providers aware of prefixlen files. **Nerds tour a datacenter!** presented by John van Oppen We toured a datacenter and colo with John van Oppen! For those who didn't get to go, John will explain the tour - but the catch is, he hasn't seen these slides.

