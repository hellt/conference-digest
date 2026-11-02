>>> HOW TO RUN THIS <<<
This is the digest prompt for swinog-41. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/swinog-41.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/swinog-41.md
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

Below is the program for SwiNOG #41 (operator). Read it and produce a digest
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
conference: SwiNOG #41
type: operator
source_url: https://www.swinog.ch/meetings/swinog41/
generated: 2026-11-01
registry_key: swinog-41
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Program
### Rethinking Network Strategy & Building Resilience Through PNIs, Peering and Smart Geographical Expansion
Speakers: Wouter Van Renterghem - RETN GmbH
slides: https://www.swinog.ch/wp-content/uploads/2026/03/Rethinking-Network-Strategy-Building-Resilience.pdf
This presentation explores the evolution of RETN’s underlying network, tracing the full journey from early architectural decisions to its current position as 11th biggest IP network in the world. It will candidly address the milestones, trade-offs, and course corrections encountered along the way, offering both a technical and strategic perspective, providing practical insights for network operators seeking to build robust, future-proof infrastructure in an increasingly interconnected and complex ecosystem that navigates through decreasing prices and growing customers' expectations.

### bgproutes.io: A next-gen BGP data collection platform
Speakers: Thomas Holterbach - University of Strasbourg
slides: https://www.swinog.ch/wp-content/uploads/2026/04/Thomas_Holterbach-University_of_Strasbourg-next-gen_BGP_data_collection.pdf | video: https://youtu.be/_OgWAjyxDGU
Public BGP data provided by collection platforms such as RIPE RIS and RouteViews is essential for monitoring and analysing BGP and Internet routing. In this talk, we introduce bgproutes.io, a next-generation BGP data collection platform designed to improve routing visibility and monitoring. We explain how bgproutes.io differs from existing platforms and how operators and researchers can access and explore the collected data through a public API and interactive analytical dashboards. We then show how bgproutes.io uses the BGP Monitoring Protocol (BMP) to collect routing information beyond best-path announcements, enabling visibility into routes received from multiple peers and at different stages of the BGP decision process. Finally, we present how bgproutes.io performs RPKI Route Origin Validation (ROV) and ASPA validation on every collected route, and how these validation results are exposed to users through both the API and the dashboards.

### Understanding and optimising transceiver power consumption using internal metrics
Speakers: Gerhard Stein - Flexoptix GmbH
slides: https://www.swinog.ch/wp-content/uploads/2026/03/Flexoptix_Transceiver_improved_power_savings_SWINOG41-3.pdf | video: https://youtu.be/whrtvO4Z01M
In high-performance optical communication systems, transceiver health and efficiency are critical to network reliability and energy use. This presentation explores Versatile Diagnostics Monitoring (VDM) features in modern transceivers (>100G), focusing on Thermoelectric Cooler (TEC) current metrics. By analysing TEC current alongside temperature and cable length, we identify optimal operating conditions that minimise power consumption without sacrificing performance. Using software prototypes and real-world VDM data, this talk demonstrates how to evaluate and visualise transceiver efficiency in watts, providing practical insights for designing and operating more energy-efficient optical networks.

### Shared Spectrum & MOFN
Speakers: Liam Taylor - EXA Infrastructure
slides: https://www.swinog.ch/wp-content/uploads/2026/04/Liam_Taylor-EXA-Shared_Spectrum_and_MOFN.pdf | video: https://youtu.be/c9LmnTkqkag
As network demand grows operators are looking at ways of scaling beyond individual wavelength services. The costs and complexities of building and maintaining a full DWDM network can however be prohibitive. In recent years shared spectrum and MOFN have arisen to seek to address these challenges and bridge the gap.

### 25 Years of SwissIX – A Quarter Century of Peering in Switzerland
Speakers: Arist Volger - SwissIX
slides: https://www.swinog.ch/wp-content/uploads/2026/03/20260428_SwissIX_SwiNOG41_V1.01.pdf | video: https://youtu.be/EDQPZvfBxvk
SwissIX was launched in 2001 – right after the burst of the Internet bubble – with a handful of ISPs and a simple mission: keep local traffic local. Twenty-five years later, the exchange carries more than a terabit per second of traffic, connects hundreds of networks, and has become a key part of Switzerland’s Internet infrastructure. This talk takes a look back at how we got here: from the spirit of the early days – when Nokia was not primarily known for its routers – to the evolution of today’s high-capacity peering fabric. Along the way, we will revisit some of the technical and operational milestones that shaped SwissIX and reflect on how we see the role of SwissIX in the years to come. SwissIX Update The usual quick update from SwissIX before lunch. Not 73 and not “six seven” either, but 77!

### Toward Agentic Network Operations: What AI Can (and Can’t) Do
Speakers: Tobias Bühler - netfabric.ai
slides: https://www.swinog.ch/wp-content/uploads/2026/04/Tobias_Buhler-NetFabric-Agentic_Network_Ops_-_What_AI_Can_and_Cant_Do.pdf | video: https://youtu.be/lFyXsezhDW8
Agentic AI is revolutionizing fields like software development, knowledge work, and customer support. In networking, it promises the same potential: a shift toward "virtual operators" capable of reasoning across infrastructure with the precision of a senior engineer. Drawing on NetFabric's deployments in diverse environments, this talk provides a fact-driven exploration of this promise. We move beyond the hype to discuss the tangible potential of an AI-first approach while surfacing the practical limitations and technical roadblocks. By specifically examining the challenges of high-volume log analysis, we demonstrate what it takes to move from human-first monitoring to AI-first systems that deliver meaningful, autonomous actions.

### An Introduction to ASPA – Validating AS-Paths with the help of RPKI
Speakers: Max Stucchi - SwiNOG
slides: https://www.swinog.ch/wp-content/uploads/2026/04/Max_Stucchi-SwiNOG-An_Introduction_to_ASPA.pdf | video: https://youtu.be/MmxbGUU8U1Q
This presentation will introduce ASPA, a new object in RPKI to help with AS-Path validation. It will begin with a quick refresher on RPKI, discussing the role of ROAs, and then the focus will be on ASPAs, what the object looks like, what is required as actions from operators, and a brief discussion about how validation works. We will also show what other objects are available these days in RPKI, to round up the presentation.

### EVPN Unleashed: Scaling Multi-Domain Fabrics with EVPN Gateways
Speakers: Remi Locherer - modus one ag with Arista Networks
slides: https://www.swinog.ch/wp-content/uploads/2026/04/Remi_Locherer-Arista-EVPN_Unleashed_-_Multi-Domain_Fabrics.pdf | video: https://youtu.be/d2f9ttGe2kk
Learn how to break the barriers of flat EVPN designs by leveraging a hierarchical gateway architecture to scale multi-site networks. This session explores how to isolate fault domains and optimize control plane state while maintaining seamless Layer 2 and Layer 3 connectivity across data centers.

### SCION Inter-Domain Routing
Speakers: Tilmann Zäschke - ETH Zürich
slides: https://www.swinog.ch/wp-content/uploads/2026/04/Tilmann_Zaschke-ETH_Zurich-SCION_Inter-Domain_Routing.pdf | video: https://youtu.be/_xg5LNhLeZE
SCION is a path-aware inter-domain network architecture designed for high security and resilience.

### The Network Automation Map: Navigate Your Journey with the NAF Automation Framework
Speakers: Damien Garros - OpsMill
slides: https://www.swinog.ch/wp-content/uploads/2026/05/Damien_Garros-OpsMill-Network_Automation_Map_and_NAF_Framework.pdf | video: https://youtu.be/WpTHsS_HWbY
Modern networks demand automation that teams can trust, understand, and safely evolve. Yet many organizations still struggle to move beyond ad-hoc scripts, brittle workflows, and unclear architectural models. This session introduces the NAF Automation Framework, a modular reference architecture designed by practitioners for practitioners. We will walk through its core building blocks—Intent, Observability, Collector, Executor, Orchestrator, and Presentation—and explore what makes them reliable, predictable, and scalable. By establishing a shared mental model and common lexicon, this framework helps teams align on concepts, compare architectures, and collaborate more effectively across tools, vendors, and organizational boundaries. Attendees will leave with clearer language, stronger architectural intuition, and practical patterns to accelerate automation in their own environments.

### Building a Vendor-Agnostic E2E Testing Ecosystem with Netlab
Speakers: Leandro Lerena & Andy Griesbeck - Zebbra AG
slides: https://www.swinog.ch/wp-content/uploads/2026/05/zebbra_SwiNOG_20260428_v1.3_PDF.pdf | video: https://youtu.be/tK5VOWVgw4M
Network automation has a habit of failing in surprising ways the moment it hits a production network. To prevent these surprises, we integrated on-demand virtual topologies into daily development using netlab, as presented at SwiNOG 40. In our talk we present a comprehensive end-to-end automation testing ecosystem bridging code authoring and safe deployment and how we moved from monolithic scripts to reusable automation building blocks with a vendor-agnostic interface. At its core is an automated validation pipeline, built around a custom Remote Lab service: a FastAPI-driven orchestrator leveraging netlab and Containerlab to provision topologies on the fly. We demonstrate how engineers test automation logic against virtual devices (like FRR and Cisco IOL) with one line of code, guaranteeing changes are proven safe before touching a production network.

### Introduction to CHNUG
Speakers: Severin Dellsperger - OST University
slides: https://www.swinog.ch/wp-content/uploads/2026/05/Severin-Dellsperger-OST-Introduction_to_CHNUG.pdf | video: https://youtu.be/tjy-r9qjWpc
This session provides an overview of the Swiss Network User Group (CHNUG), a community-driven initiative dedicated to fostering collaboration within the Swiss networking landscape.

### SwiNOG #41 Closing Remarks
Speakers: Simon Ryf & Steven Glogger - SwiNOG
slides: https://www.swinog.ch/wp-content/uploads/2026/05/Goodbye_v2.pdf | video: https://youtu.be/nsNaOTVy4tw
No abstract published; title, speakers and materials only.

