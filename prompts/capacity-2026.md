>>> HOW TO RUN THIS <<<
This is the digest prompt for capacity-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/capacity-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/capacity-2026.md
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

Below is the program for Capacity Europe 2026 (vendor). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a vendor / community program (e.g. a CNCF or vendor conference).
Separate genuine technical or strategic substance from product marketing.
Down-rank pure product pitches and sponsor slots. Up-rank end-user case studies
with real numbers (scale, latency, cost, incident detail), contributor-led
architecture and internals talks, and sessions that reveal where an open-source
project is actually heading. Be skeptical of "we adopted X and it was great"
talks with no metrics or failure discussion.

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
conference: Capacity Europe 2026
type: vendor
source_url: https://www.capacityeurope.com/agenda/
generated: 2026-11-02
registry_key: capacity-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Capacity Europe sessions
### Digital Infra Leaders' Summit Europe (By Invitation Only)
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infra-leaders-summit-europe-provisional
12 October 2026
No description published; title, speakers and stream only.

### Opening Keynote Presentation - The Convergence Moment
Speakers: Avijit Singh, Chief Strategy Officer - COLT TECHNOLOGY SERVICES
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-presentation-building-first-universal-quantum-computer
13 October 2026 · Streams: Industry Structure, Partnerships & Control, AI Revenue & Service Innovation
As AI agents rapidly reshape internet traffic, networks are entering a new era where machines generate more activity than humans. Avijit Singh explores what this shift means for digital infrastructure, from AI-optimised and autonomous networks to the security, governance, and capacity challenges providers must address to support the next wave of AI-driven growth.

### Opening Keynote Panel: Execution Matters: How to turn AI ambition into real returns
Speakers: Sam Evans, Senior Managing Director - TENEO STRATEGY (UAE) LIMITED, Valerie Cussac, CEO - ORANGE WHOLESALE INTERNATIONAL, Dimitrios Rizoulis, Senior Vice President T Wholesale Global Connectivity - T WHOLESALE, Fanan Henriques, MD Product & International Business - Vodafone Group, Enrico Bagnasco, Chief Executive Officer - SPARKLE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-panel-execution-matters-turn-ai-ambition-real-returns
13 October 2026 · Streams: Operations, Automation & Execution, Investment, Finance & Market Dynamics, AI Revenue & Service Innovation
This keynote examines where AI ambition is delivering results in connectivity & network infra, by unpacking revenue opportunities, board priorities, and the constraints around talent, productisation, partnerships, CapEx and regulation, driving sustainable growth outcomes.

### Keynote Panel: Wiring the AI Boom: Building Fibre Corridors for Training, Inference and Scale
Speakers: Nicholas Collins, Chief Strategy & Transformation Officer - O2 BUSINESS HOLDINGS LIMITED, Marisa Trisolino, CEO - EUNETWORKS, Jim Fagan, Chief Executive Officer - EXA INFRASTRUCTURE UK LTD, Jorge Alvarez, Chief Executive Officer - Retelit Digital Services S.p.A., Jeff Hulse, President - VERIZON, Amjad Arab, Chief Carrier & Wholesale Officer - SALAM
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/keynote-panel-wiring-ai-boom-building-fibre-corridors-training-inference-scale
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
AI is reshaping fibre demand across training hubs, inference and edge networks. This panel examines fast‑track corridor builds, dark fibre strategies, investment choices, network design and early engagement with customers.

### Case Study: Bare Metal Is Not Enough: How Neoclouds Win with Carrier Partnerships
Speakers: Andy Long, Enterprise Sales Director - Verda
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/case-study-bare-metal-enough-neoclouds-win-carrier-partnerships
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Investment, Finance & Market Dynamics, AI Revenue & Service Innovation
Neoclouds began as GPU stopgaps, but sustainable economics require moving up the AI stack. This case study This case study explores how telco partnerships unlock scale, talent and route‑to‑market against hyperscaler competition.

### Networking Roundtables: Networks for the AI Era: Who Builds, Who Pays, Who Wins?
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-networks-ai-era-builds-pays-wins
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), AI Revenue & Service Innovation
Format: Attendees self-select one of 3 tables. A dedicated moderator (senior operator, panellist or independent chair) runs each table for 20-30 minutes. Who Pays for AI Networks? Hubs, Inference and the Edge Building AI Corridors: Where Are the Real Capacity Bottlenecks? Carrier Relevance in the AI Stack: Where Is the Defensible Value?

### Networking Lunch
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-lunch-2
13 October 2026
No description published; title, speakers and stream only.

### Connecting Lives in Crises: Real Stories from Ukraine to TSF’s Global Missions
Speakers: Emmanuel JEAN, Head of Communications - TELECOMS SANS FRONTIERES, Sophie Terrisse, Executive Chaiman - 26FIVE Global Lab
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/connecting-lives-crises-real-stories-ukraine-tsfs-global-missions
13 October 2026
No description published; title, speakers and stream only.

### Presentation: The Automation Gap: Why Networks Outpace the Organisations Running Them
Speakers: Frank McDermott, CEO & Co-Founder - CARMA
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-automation-gap-networks-outpace-organisations-running
13 October 2026 · Streams: Operations, Automation & Execution, AI Revenue & Service Innovation
Networks are increasingly intelligent, but most organisations struggle to turn visibility into control. This session explores how digital twins and operational data can drive real automation, accelerate scaling decisions, cut costs and improve customer experience.

### Panel: Legacy vs Scale: The Automation Breaking Point
Speakers: Daniel Bar-Lev, Chief Product Officer - Mplify, Cameron Daniel, Chief Technology Officer - MEGAPORT, Azfar Aslam, Chief Technology Officer, Europe, United Kingdom - NOKIA, Tom Major, SVP Product Management - GTT AMERICAS LLC
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-legacy-vs-scale-automation-breaking-point
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Operations, Automation & Execution, AI Revenue & Service Innovation
Legacy networks are blocking automation as customer expectations accelerate. This panel examines fixes, AI agents, integration trade-offs, and who wins or loses as operators chase NaaS, edge and AI revenue.

### Networking Roundtables: Automating the Network
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-automating-network
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Operations, Automation & Execution
Why Has NaaS Not Taken Off: Legacy Tech, Culture, or Risk? Does NaaS Sell Alone, or Only When Bundled with Edge, Cloud and Security? Who Actually Makes Automation Work: Integrators or OSS/BSS Vendors?

### Panel: Beyond Infrastructure: Who Really Monetises AI?
Speakers: Sylwia Kechiche, Industry Analysis Vice President - Opensignal, Ksenija Draskovic, CEO - GlorifAI, Dr. Eva-Maria Hempe, Executive Director Public Sector EMEA - NVIDIA, Ashutosh Pateriya, EMEA technical lead - Amazon Web Services (AWS)
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-beyond-infrastructure-really-monetises-ai
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Investment, Finance & Market Dynamics, AI Revenue & Service Innovation
AI monetisation is shifting from infrastructure to outcomes. This panel explores where AI sits in the service stack, how it is productised through APIs and managed services, and which models customers will pay for.

### Networking Roundtables Monetising AI at the service layer
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-monetising-ai-service-layer
13 October 2026 · Streams: Industry Structure, Partnerships & Control, AI Revenue & Service Innovation
Who owns the AI Relationship: Telcos, Platforms, or Partners? Where Does AI Actually Sit in the Telco Stack? Selling Intelligence, Not Infrastructure: What Will Customers Pay For?

### End of Conference Day 1
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/end-conference-day-1
13 October 2026
No description published; title, speakers and stream only.

### Keynote Presentation - Service Providers & Neoclouds: The Spinal Cord of the AI Era
Speakers: Johan Gustawsson, CTO and Vice President, Provider Connectivity - CISCO
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/connect-protect-power-building-infrastructure-ai-era
13 October 2026 · Streams: Operations, Automation & Execution, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), AI Revenue & Service Innovation
AI is reshaping how infrastructure creates value. As inference becomes more distributed, customers need resilience, trust, sovereignty and assurance end to end. Service providers and neoclouds occupy potential complementary positions in this evolving value chain, spanning reach, interconnection, trusted delivery and inference platforms. This session briefly examines where this shift creates opportunities for differentiated services and new revenue models.

### Opening Keynote Panel: Beyond Silos: Building Europe’s Converged Digital Infrastructure
Speakers: Anna Klaft, CEO - KLF Management, Joe Scattareggia, EVP Infrastructure & Connectivity - COLT TECHNOLOGY SERVICES, Paula Cogan, Managing Director, EMEA - DIGITAL REALTY, Brenden Rawle, Senior Business Development Director - EQUINIX, Michael Wheeler, Executive Vice President, Global IP Network - NTT DATA, Twinkle Singh, Global Technical Program Manager - Google
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-panel-beyond-silos-building-europes-converged-digital-infrastructure
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
For the first time, Europe’s colocation providers, carriers and internet exchanges share a stage, debating joint ventures, shared models, network convergence, AI delivery, and revenue opportunities across digital infrastructure stack.

### Networking Roundtables The Convergence Moment
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-convergence-moment
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea)
Attendees self-select one of 3 tables. A dedicated moderator (senior operator, panellist or independent chair) runs each table for 20-30 minutes. All Under One Roof: Does Europe Need Fully Integrated ‘Fibre & Data Center’ Hubs? Is Convergence the Cure for Capacity Constraints? Who Owns the Future: Telcos, Cloud Giants, or Neutral Hosts?

### Presentation: Connecting Continents: The New Digital Corridor Between Europe, the Middle East and Africa
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-grid-save
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Policy, Regulation & Security
Europe’s AI ambitions face a fundamental question: can the grid cope? This talk explores securing power, grid access, renewables, and solutions from utilities and energy partners to meet rising demand.

### Panel: From Grid Constraint to Competitive Growth
Speakers: Loren Long, Principal - Digital Infrastructure Advisors Limited, Camilla Carson, Senior Vice President and Chief Strategy and Marketing Officer - Geopura, David Adkins, Head of Network Architecture and Innovation - National Grid, George NOLIS, CEO - BALKAN GATE GREECE, Dominic Ward, CEO - Verne
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-grid-constraint-competitive
13 October 2026 · Streams: Power, Energy & Sustainability
Power constraints now gate data centre growth. Hear how energy providers, hyperscalers and operators secure grid access, deploy on-site power, scale renewables, and keep Europe’s digital expansion on track.

### Networking Roundtables: Power on your own Terms
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-power-terms
13 October 2026 · Streams: Power, Energy & Sustainability
The New Power Play: Should Data Centres Become Energy Producers Crunching the Kilowatts: How to Secure Grid Access Faster? Beyond Greenwashing: Real Steps to Embed Sustainability in AI Infrastructure

### Presentation: Streamlining the Unseen – Permits, Plans and Policy
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-streamlining-unseen-permits-plans-policy
13 October 2026
From Dublin to Frankfurt, projects face red tape and community pushback. This session explores permitting reform, policy alignment, and how to reduce delays while building trust to enable critical infrastructure.

### Panel: Licence to Operate: Earning Community and Government Buy-In
Speakers: Scott Roots, VP Sales, EMEA - DC Byte Limited, Mark Pestridge, Executive Vice President & General Manager - Telehouse, Allan Bosley, Director, Public Affairs - Ark Datacentres, Dan Thomas, CEO - Greenscale
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-licence-operate-earning-community-government-buy
13 October 2026 · Streams: Supply Chain & Build Constraints, Policy, Regulation & Security
Europe’s fragmented planning rules and rising opposition are slowing data centres, fibre and energy projects. Who takes the lead to fix approvals, align communities and unblock infrastructure deployment across Europe?

### Networking Roundtables Permission to Build
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-permission-build
13 October 2026 · Streams: Operations, Automation & Execution, Supply Chain & Build Constraints, Policy, Regulation & Security
Community Benefit or Box-Ticking: What really wins local support? United Front: Can industry convergence solve the social licence problem? Design Together or Fail Separately: Which early decisions make or break a project?

### End of AI Build Stage Day 1
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/end-ai-build-stage-day-1
13 October 2026
No description published; title, speakers and stream only.

### Opening Keynote Presentation: State of the European Metro Market
Speakers: Colman Deegan, Chief Executive Officer - ZAYO EUROPE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-presentation-state-european-metro-market
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
What does the next chapter of European fibre coverage look like? A data-led overview of deployment velocity, investment flows, M&A activity & the emerging gap between coverage and adoption.

### Opening Panel: What Is Fibre Really Worth? Reassessing Value in Europe's Infrastructure Market
Speakers: Kieran Smith, Telecoms & Technology Correspondent - The Financial Times, Thibault Contat Desfontaines, Co-Head of Infrastructure Equity, Europe - UBS Asset Management UK Ltd., Andrea Kraus, CCO - Eurofiber Group, Jennifer Smith, Chief Financial Officer - ZAYO EUROPE, Matteo Mallet, Strategy Director - LYNTIA, Victor Pons Mesman, CFO & CSO - LYNTIA NETWORKS
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-panel-valuations-under-pressure-europes-altnets-really-worth
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
As Europe's fibre market matures, the focus is shifting from network build to long-term value creation. From incumbents and wholesale networks to altnets, this panel explores how fibre assets are being assessed, what drives value in today's market, and where investors see the greatest opportunity.

### THE FIBRE INVESTMENT CHAT SHOW: SCALING OR SELLING?
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/fibre-investment-chat-show-scaling-selling
13 October 2026 · Streams: Investment, Finance & Market Dynamics
A series of one-to-one conversations exploring how leaders are navigating Europe’s fibre shake-out, the strategic choices facing operators and investors, and what consolidation means for the future sh …

### Chat 1 | Scaling: When Does Bigger Become Better?
Speakers: Safeer Malik, Head of Content and Insights - Capacity - Techoraco, Rajiv Datta, CEO - NEXFIBRE NETWORKS LIMITED
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/chat-1-scaling-bigger-become-better
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea)
No description published; title, speakers and stream only.

### Chat 2 | Investing: Where Is the Value in Fibre?
Speakers: Safeer Malik, Head of Content and Insights - Capacity - Techoraco, Simon Rozas, Head of European Digital Infrastructure - CVC DIF
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/chat-2-investing-value-fibre
13 October 2026 · Streams: Investment, Finance & Market Dynamics
No description published; title, speakers and stream only.

### Chat 3 | Operating: How Do You Turn Fibre into a Sustainable Business?
Speakers: Safeer Malik, Head of Content and Insights - Capacity - Techoraco, Eric Kuisch, COO - Eurofiber
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/chat-3-operating-turn-fibre-sustainable-business
13 October 2026 · Streams: Investment, Finance & Market Dynamics
No description published; title, speakers and stream only.

### Networking Roundtables: Where Does European Fibre Go From Here?
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-consolidation-moment
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
Scale: How big do you need to be to compete? Investment: Where will future growth and returns come from? Consolidation: What will Europe’s fibre market ultimately look like?

### Presentation: The Deployment Gap: What's Holding Fibre Back?
Speakers: Andrew Black, Technical Director - Fujikura Europe LTD
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-networks-built-profits-missing
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
As operators move from ambitious rollout plans to large-scale delivery, new challenges are emerging around cost, complexity, labour availability and network modernisation. This presentation examines the practical realities of fibre deployment, the lessons being learned across European markets, and what will be required to accelerate rollout in the years ahead.

### Panel: No Fibre, No AI: Is Europe Creating Its Own Bottleneck?
Speakers: Kevin Sheehan, CTO of the Americas, Vice President of Sales Engineering, and S3 - Ciena Limited, Vincent Rousseau, Deputy Director of Operations - SIPARTECH, Toby Williams, Chief Product Officer - EUNETWORKS, MONICA MARTINEZ QUERO, CMO - TELXIUS, Shaunak Thakkar, Director, Cloud Infrastructure, Network Investments, Delivery & Strategic Partnerships - Oracle
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-fibre-ai-europe-creating-bottleneck
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics, Policy, Regulation & Security
Europe’s AI ambitions risk stalling without new fibre backbones. This panel explores why core fibre lags demand, how it constrains data centres and AI clusters, and what investment, policy and partnership models unlock growth.

### Networking Roundtables The Fibre Investment Reckoning
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-fibre-investment-reckoning
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics, Policy, Regulation & Security
Future of Data Centre Fibre. Why has core fibre been overlooked, and how do we shift investment priorities? How can fibre connectivity enable truly distributed AI ecosystems? What practical steps are needed to accelerate deployment? Planning reform/Supply Chain/Collaboration models?

### Presentation: Data Center Interconnect for the AI Era: Enabling Distributed AI Infrastructure
Speakers: Nino Shaptoshvili, VP of Sales - PACKETLIGHT NETWORKS LTD
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-pays-europes-digital-ambition-policys-real-price-tag
13 October 2026 · Streams: Operations, Automation & Execution, Supply Chain & Build Constraints, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea)
As AI infrastructure expands across multiple locations, the network becomes critical. This session explores how high-performance DCI connects distributed GPU clusters, storage, and compute into a unified AI fabric. Discover how optical transport delivers the massive bandwidth, deterministic low latency, and security needed to move huge datasets, synchronize AI workloads, and scale with confidence.

### Snapshot Presentations: Key developments shaping Europe's digital infrastructure
Speakers: Sophie Greaves, Associate Director, Digital Infrastructure - TechUK, Kadir Solakoğlu, CCO - Türk Telekom International HU, Olivier Gommes, Technology & Innovation VP - MARLINK, Oscar Monteagudo, Head of Carrier Sales & Subsea Business - Vodafone Group
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/snapshot-presentations-key-developments-shaping-europes-digital-infrastructure
13 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
Three industry leaders. Three big ideas. In these short, high-impact spotlight presentations, attendees will gain rapid insights into the innovations, investments and technologies transforming connectivity across Europe and beyond. Spotlight 1: Turk Telekom: The Eastward Shift: Understanding Europe's Data Traffic Evolution Spotlight 2: Vodafone: A strategic infrastructure investment with industry-wide implications Spotlight 3: Marlink How do satellite technologies work and how to choose the right one for your customers?

### Networking Roundtables The Fibre Funding Fight: Policy, IRR and Build Risk
Speakers: Sophie Greaves, Associate Director, Digital Infrastructure - TechUK
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-fibre-funding-fight-policy-irr-build-risk
13 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics, Policy, Regulation & Security
How are investors reassessing IRR expectations as penetration rates are challenging in some markets? What role should the EU Gigabit Infrastructure Act and state aid frameworks play in bridging white spots? How are debt structures, IRUs, and wholesale agreements evolving to de-risk metro buildouts?

### End of Fibre Investment Stage Day 1
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/end-fibre-investment-stage-day-1
13 October 2026
No description published; title, speakers and stream only.

### Breakfast & Networking Round Tables
Speakers: Jennifer Parkhill, Senior Director- Program & Project Management - VERIZON PARTNER SOLUTIONS, Naaz Bax, Founder & CEO - Team Bax, Osvaldo DiCampli, GSCO Global Network Infrastructure Segment Leader - NOKIA
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/breakfast-networking-round-tables
13 October 2026
Get stuck in to the morning of Day 1 with Nokia & Verizon! Networking, a short panel on AI & Industry Transformation, followed by a choice of two interactive round table discussions: Next-Generation Leadership in Digital Infrastructure OR Talent Acquisition & Culture for Retention

### Introducing The Outlook: A new destination for leadership and influence
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/introducing-outlook-new-destination-leadership-influence
13 October 2026
Alongside the main programme, we’re launching The Outlook , a premium environment for high-level discussion, deal making and closed-door collaboration. Hosting: Digital Infra Leaders’ Summit (invitation only) Global Critical Infra Summit (new for 2026), tackling security, resilience and geopolitics in a world where infrastructure is now strategic Curated networking from private receptions to community meetups Beyond the agenda: Where the real conversations happen Capacity Europe is built as a festival, not just a conference. Expect pockets of activity across the venue , from hosted happy hours and stage receptions to private dinners, partner meetups and late-night parties. It’s continuous, high-energy networking, designed to move conversations forward and turn introductions into commercial outcomes .

### Apply to Attend The Global Critical Infrastructure Summit
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/apply-attend-global-critical-infrastructure-summit-96c4
13 October 2026 · Streams: Policy, Regulation & Security
This is an application-only session, available to registered attendees of Capacity Europe. Places are limited to 100 senior delegates from network operators/cloud infrastructure owners, government and regulation, cloud/hyperscale/neocloud providers. To register your interest, contact liss.boothandford@techoraco.com

### Opening Keynote: Protecting Critical Infrastructure in an Era of Hybrid Threats
Speakers: Laurie Walker, Team Lead - Critical Undersea Infrastructure Coordination Cell - NATO
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-resilience-imperative
13 October 2026 · Streams: Policy, Regulation & Security
Critical infrastructure is increasingly at the centre of geopolitical competition, economic resilience, and international security. This keynote explores the evolving threat landscape facing critical networks, the Alliance's role in protecting vital infrastructure, and the actions governments and industry must take to strengthen resilience against emerging hybrid threats.

### Panel 1: Threats at the National Level
Speakers: Johanna Karvonen, Senior Specialist, Critical Infrastructure Protection & EU Project Coordinator VIGIMARE & NEPTUNE Project - Laurea University of Applied Sciences, Chase Clowser, Global Network Intelligence Lead - Recorded Future, Sarah Austerberry CSyP, FSyI, Principal RSES, CEO - The Security Institute, John Wrottesley, Executive Director, European Subsea Cables Association (ESCA) & GM - International Cable Protection Committee (ICPC)
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-1-threats-national-level
13 October 2026 · Streams: Policy, Regulation & Security
Geopolitical risk, hybrid warfare and physical exposure As cyber, physical, climate and hybrid threats converge, this panel explores Europe’s resilience gaps, evolving security responsibilities, and whether governments and operators are prepared for the realities of critical infrastructure protection.

### Panel 2: Fibre, Routes & the Fragility of Global Connectivity
Speakers: Marc Halbfinger, Managing Director - Red HMH, Steve Roberts, SVP Network Investment & Product Management - EXA INFRASTRUCTURE UK LTD, Andy Palmer-Felgate, Submarine Cable Engineer - Meta, Paul Gabla, Chief Sales & Marketing Officer - Alcatel Submarine Networks
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-2-fibre-routes-fragility-global-connectivity
13 October 2026 · Streams: Policy, Regulation & Security
Resilience by design: securing Europe's connectivity routes As AI adoption, cloud growth and digital sovereignty reshape infrastructure priorities, route diversity has become a strategic imperative. This panel examines how the industry is building resilient fibre and subsea networks to support Europe's next era of connectivity, compute and data growth.

### Closing Remarks
Speakers: Sam Evans, Senior Managing Director - TENEO STRATEGY (UAE) LIMITED
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/closing-remarks-end-global-critical-infrastructure-summit
13 October 2026 · Streams: Policy, Regulation & Security
No description published; title, speakers and stream only.

### Networking Coffee & End of Global Critical Infrastructure Summit
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/coffee-break
13 October 2026 · Streams: Policy, Regulation & Security
No description published; title, speakers and stream only.

### GLF Lounge
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/glf-lounge
13 October 2026 · Streams: GLF Activities
No description published; title, speakers and stream only.

### VIP Mixer
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/vip-mixer
13 October 2026 · Streams: Social Agenda
No description published; title, speakers and stream only.

### Official Day 1 Reception
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/official-day-1-reception
13 October 2026 · Streams: Social Agenda
No description published; title, speakers and stream only.

### Keynote Presentation: The End of Neutral Infrastructure: Trust, Risk and Control in Europe
Speakers: Michael Trabbia, CEO - ORANGE WHOLESALE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-end-neutral-infrastructure-trust-risk-control-europe
14 October 2026
Network design is no longer driven by efficiency alone. Security mandates, national sovereignty and geopolitical risk now dictate where, how and with whom digital infrastructure is built. So, who really gets to shape Europe’s digital future?

### Panel: The New Rules of Network Design
Speakers: Rajesh Sennik, Senior Advisor - Roland Berger, Vilas Thawale, Director - Network Development & Strategy (Subsea Networks) - TATA COMMUNICATIONS, Tony O'Sullivan, CEO - RETN, John Fitzgibbon, Senior Manager Network Planning & Acquisition - AWS, Younès Stouky, Head of Capacity Services & Infrastructure - ORANGE WHOLESALE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-new-rules-network-design
14 October 2026
Security, resilience and sovereignty are reshaping how networks are routed, located and interconnected, driving higher costs and trade-offs across fibre, datacentres and subsea as operators balance risk, speed and returns.

### Networking Roundtables Networks You Can Trust: Security in a Geopolitical Age
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-networks-trust-security-geopolitical-age
14 October 2026
What Has to Stay Local, and What Can Stay Global? Is Route Redundancy Insurance or Overengineering? Are Interconnection Choices Creating Hidden Risk?

### Panel: Hybrid networks or higher risk? Why Satellite is becoming mission-critical
Speakers: Safeer Malik, Head of Content and Insights - Capacity - Techoraco, Kyle Whitehill, Chief Executive Officer - AVANTI COMMUNICATIONS, Eva Bisgaard, President of the Connectivity Business Unit - Eutelsat S.A., Jean-Philippe Gillet, President Fixed Vertical - SES, Abdullah Zubailah, GM, Technology & Project Management - Carrier & Wholesale - STC, Denis Chahabadi, VP Inflight Services & Satellite Innovation Hub - T WHOLESALE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/hybrid-networks-higher-risk-satellite-becoming-mission-critical
14 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea)
As demand for resilient hybrid networks grows, this panel examines satellite–terrestrial partnerships, addressing last-mile gaps, mobile backhaul, interoperability challenges, evolving low-latency tech, and secure, scalable collaboration models for operators worldwide.

### Presentation: Boom or Bottleneck? An Update on Global Subsea Connectivity
Speakers: Stacey Parker, Research Analyst - TELEGEOGRAPHY
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-subsea-bottleneck-europes-cables-cap-ai-boom-
14 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics, Policy, Regulation & Security
Despite headlines warning of a global capacity squeeze, unprecedented infrastructure investments are driving massive network growth and route diversity. This session explores current market constraints along with the latest bandwidth, infrastructure, and pricing data to provide a realistic outlook on European supply and demand.

### Panel: Chokepoints & Shockwaves: Protecting the Cables Europe Can’t Lose
Speakers: Martin Prins, Ambassador - Dutch Subsea Cable Coalition, Ugne Kleinauskaite, Network Investments Manager - Meta, Martin Dowling, CTO - Midgard Infra, Andy Bax, Strategic Cable Builds - EXA INFRASTRUCTURE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-chokepoints-shockwaves-protecting-cables-europe-t-lose
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Policy, Regulation & Security
Hyperscalers and global crises are reshaping Europe’s subsea connectivity and exposing its fragility. This discussion charts how new partnerships, diversified routes and sovereignty moves can safeguard Europe’s vital undersea lifelines against capacity bottlenecks and geopolitical shocks.

### Networking Roundtables: Global Capacity for the AI Era
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Policy, Regulation & Security
Hyperscalers or Homegrown: Who Should Control Europe’s Critical Cables? One Cut from Chaos: Does Europe Have Enough Route Resilience? Edge vs. Atlantic – Will Distributed AI Ease Global Traffic or Exacerbate It?

### Panel: The CX Revolution ' Turning networks into experience platforms
Speakers: Prianca Ravichander, Cco - Tecnotree, Ivana Dragovic, Marketing and Customer Experience Director - E&, Binod Sriwastav, EVP & Chief Business Officer - AIRTEL BUSINESS, Nuria Gonzalez, Head of Customer Operationss - TELEFÓNICA, Veer Passi, Group CEO - Kalaam Telecom
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-cx-revolution-turning-networks-experience-platforms
14 October 2026 · Streams: Operations, Automation & Execution, AI Revenue & Service Innovation
Enterprises judge connectivity on experience, not price. This panel explores how operators use automation and network intelligence to deliver cloud‑like CX, faster provisioning and transparency without driving up operating costs.

### From Fragmented to Frictionless: Ending the Broken Way We Buy and Sell Digital Infrastructure
Speakers: Mike Hiatt, Vice President | Partnerships - Inflect, Inc., Peter Coppens, VP Product - COLT TECHNOLOGY SERVICES, Cameron Daniel, Chief Technology Officer - MEGAPORT
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables
14 October 2026
Every infrastructure deal has a yes buried in it. Getting there takes months of manual research, unverified data and human bottlenecks. Experts in site selection, financing and data center operations examine what really slows deals down, and how a marketplace with intelligence built in compresses months into minutes.

### Panel: Reclaiming the voice opportunity with voice AI
Speakers: Isabelle Paradis, President - Hot Telecom, Burak Enseren, Director of Global Deployment - TELNYX, Yogesh Lulla, CEO - Telecom Services - -, John Kennedy, VP, Operations - Enea, Guillaume Klein, EVP, Product Strategy - IBASIS
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-reclaiming-voice-opportunity-voice-ai
14 October 2026 · Streams: Operations, Automation & Execution, Policy, Regulation & Security, AI Revenue & Service Innovation
Voice is becoming an AI‑driven, high‑value service, but fraud is accelerating. This discussion explores how operators integrate identity, analytics and CX data to monetise voice beyond minutes while protecting customers.

### Voice & Messaging Networking Roundtable: Building Trusted Communications in the AI Era
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-controls-voice-ai-world
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Policy, Regulation & Security, AI Revenue & Service Innovation
Can Business Messaging Become the Next Major Growth Engine for Operators? Fighting AI with AI: How Do Operators Stay Ahead of Messaging and Voice Fraud? Who Will Own Trusted Communications: Networks, OTTs, CPaaS Platforms or AI Assistants?

### End of Conference Day 2
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/end-conference-day-2
14 October 2026
No description published; title, speakers and stream only.

### Networking Reception
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-reception
14 October 2026
No description published; title, speakers and stream only.

### Exhibition Closes
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/exhibition-closes-ya3c
14 October 2026
No description published; title, speakers and stream only.

### Keynote Presentation: The €100 Billion Question: Who Funds Europe’s AI Infrastructure?
Speakers: Mehdi Paryavi, Chairman & CEO - International Data Center Authority
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/keynote-presentation-100-billion-question-funds-europes-ai-infrastructure
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
Building Europe’s AI-ready digital infrastructure will cost hundreds of billions by 2030. This session examines who funds it, from private capital to public support, and how models make projects bankable.

### Panel: Capital at Risk: Navigating investment and returns in the AI Era
Speakers: Venessa Moffat, Managing Director - The DCA - Data Centre Alliance, David Bloom, Executive Chairman - Kao Data and Goldacre, Dharman Sury, Senior Advisor - BGO, Oliver Felice-Owens, VP Telecom and Digital Infrastructure - Guggenheim, Zach Gellman, Managing Director - DigitalBridge, Paul McNally, VP of Investment - Echelon Data Centres
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-capital-risk-navigating-investment-returns-ai-era
14 October 2026 · Streams: Power, Energy & Sustainability, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics
AI infrastructure demands unprecedented capital amid uncertain returns. Financiers and operators reveal deal structures, risk strategies, green financing, incentives, and what conditions will unlock investment to sustain Europe’s digital growth.

### Networking Roundtables Financing European AI Builds
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-financing-european-ai-builds
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Investment, Finance & Market Dynamics
Is Europe’s AI infrastructure boom an investor’s dream or a bubble? Public Money, Private Projects: What role should governments play? New Models for New Builds: From JVs to hyperscaler pre-deals

### Presentation: The Sovereignty Dilemma: Europe’s AI Workloads and Where to Host Them
Speakers: Emmanuel Becker, CEO - MEDITERRA
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-sovereignty-dilemma-europes-ai-workloads-host
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Policy, Regulation & Security
As AI services boom, Europe must decide where compute sits. This session examines latency, sovereignty and power proximity, showing how policy and customer demand are redrawing Europe’s data centre geography.

### Panel: From FLAP to Frontier: Rethinking Europe’s footprint for AI
Speakers: Dame Dawn Childs, Chief Executive Officer - nLighten, Ivo Ivanov, CEO - DE-CIX, Amar Khan, Head of Network Site Investments - Meta, Falk Weinreich, CEO - PORTUS DATA CENTERS, Giancarlo Giacomello, CEO - ARUBA DC & INFRASTRUCTURES
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-flap-frontier-rethinking-europes-footprint-ai
14 October 2026 · Streams: Operations, Automation & Execution, Policy, Regulation & Security
Europe’s landscape is decentralising. This panel examines emerging AI hubs, edge growth, and how policy, sovereignty and latency shape location decisions, and who will host Europe’s billion-euro AI factories.

### Networking Roundtables Where AI Lives: Location & Latency
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-ai-lives-location-latency
14 October 2026
Core vs Edge: Which workloads go where? Nordics vs FLAP: Is cheap power beating low latency? Sovereignty: Real concern or red herring?

### Panel: Scaling Under Scarcity: Delivering Projects Amid Shortages
Speakers: Simon Allen, Global Ambassador - Nomad Futurist, Justin Ryburn, Field CTO & VP of Global Solutions Engineering - Kentik, Miriam van Kooperen, Senior Director Supply Chain - Greenscale DC, Mohammed Alqahtani, CTO - CENTER3, Ozgur Duzgunoglu, Head of Engineering & Design - Telehouse, Nelson Pinto de Magalhaes, Director, PMO & Procurement - Start Campus
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-scaling-under-scarcity-delivering-projects-amid-shortages
14 October 2026 · Streams: Supply Chain & Build Constraints
Rapid build collides with shortages of power equipment, chips and cooling. This panel shares supplier and operator strategies, from standardisation to alternative sourcing, to keep Europe’s infrastructure projects on track.

### Networking Roundtables
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-wc92
14 October 2026
GPUs, switches, and the elephant in the room: which shortage hurts most? Europe’s Dependency Dilemma: Can we build resilience into our supply chains? Speed vs. Spec: Should we build fast or wait for the best tech?

### Panel: Built on Time: Best Practices for On Schedule Delivery
Speakers: Mike Meyer, Executive Director - Data Centre Alliance Ltd, Adam Gibson, Managing Partner - techvox, Sarah Davey, Director EMEA Digital Infrastructure - EQUINIX, Alex Thomas, Data Centre Associate Director - Savills, Julian Hennessy, Project Director, Development & Construction - Telehouse, Ken Dalton, Director, Operations - Global Switch Limited
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-built-time-best-practices-schedule-delivery
14 October 2026 · Streams: Supply Chain & Build Constraints
AI demand is outpacing supply, making speed critical. This panel reveals how builders and customers compress timelines through design coordination, demand forecasting and early procurement to gain competitive advantage.

### AI Build Stage Networking Reception & end of Conference Day 2
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/ai-build-stage-networking-reception-end-conference-day-2
14 October 2026
No description published; title, speakers and stream only.

### Panel: Beyond Copper: Fibre, Hollow Core & What's Next
Speakers: Daniel Rowan - Independant, Christoph Glingener, CEO - ADTRAN, INC., Danny Preston, Co-founder & CEO - NETWORK PLANNING SOLUTIONS LTD, Jussi Tolvanen, CEO - DNA Ltd, Colin Bannon, CTO BT Business - BT PLC, Lee Myall, CEO - Neos Networks
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-switch-done-right-lessons-europes-front-runners
14 October 2026 · Streams: Operations, Automation & Execution, Investment, Finance & Market Dynamics, Policy, Regulation & Security
As copper networks are retired across Europe, operators are investing in the next generation of connectivity. From fibre expansion and migration strategies to innovations such as hollow core fibre and advanced optical networks, this panel explores how leading markets are modernising infrastructure and preparing for future demand.

### Networking Roundtables: Switch-Off at Scale: Migration, Mistakes and Customer Impact
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-switch-scale-migration-mistakes-customer-impact
14 October 2026 · Streams: Operations, Automation & Execution, Policy, Regulation & Security
Who Gets Left Behind in Copper Switch‑Off, and Who Is Responsible? What Actually Speeds Migration: Regulation, Incentives or Pain? Which Nordic Lessons Travel, and Which Don’t?

### Panel: From Best Practice to Critical Infrastructure: Rethinking Fibre Resilience
Speakers: Felix Seda, Chief Revenue Officer - NJFX, Gilles Calligaro, CEO - ARTERIA, Tom Ronan, Senior Director, Fiber Systems - VIAVI SOLUTIONS, Salman Alomiri, HyperScaler Advisor - MOBILY, Dave Ferry, CSO - ITS
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-best-practice-critical-infrastructure-rethinking-fibre-resilience
14 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Investment, Finance & Market Dynamics, Policy, Regulation & Security
As businesses become increasingly dependent on digital infrastructure, network resilience is becoming a key differentiator. This panel explores how operators strengthen reliability, improve visibility across their networks, minimise disruption, and build the resilient infrastructure needed to meet rising customer expectations.

### Networking Roundtables Networks Under Threat: Resilience in a Hostile World
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-roundtables-networks-under-threat-resilience-hostile-world
14 October 2026 · Streams: Core Infrastructure & Capacity (Fibre, Data Centres, Subsea), Policy, Regulation & Security
Beyond Compliance: What Does Real Metro Resilience Look Like? Who Knows What, When? Making Threat Intelligence Actionable Who Pays for Resilience When Customers Don’t See It?

### Panel: Banking Fibre Beyond Tier One: What Actually Works?
Speakers: Darren Shenkin, Founder & Principal Consultant - SHENKIN Advisory, Buddy Bayer, Chief Operating Officer - COLT TECHNOLOGY SERVICES, Matt Partridge, Managing Director – Enterprise & Wholesale - LightSpeed Networks, Sally-Anne Skinner, CEO - Ogi
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-banking-fibre-beyond-tier-one-actually-works
14 October 2026
Outside major metros, fibre economics tighten fast. This panel explores how operators make secondary markets viable, which deployment and wholesale models succeed, and when public subsidy remains essential.

### Closing Keynote Panel: Digital Infrastructure in 2029: Who Captures the Next Wave of Value?
Speakers: Naaz Bax, Founder & CEO - Team Bax, Jeroen Kleinjan, Managing Director - ING, Jennifer Holmes, CEO & Board Director - LONDON INTERNET EXCHANGE (LINX), Hamish Macleod, Chief Executive - Mobile UK, Paul Abfalter, CRO - FLAG
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/closing-keynote-panel-digital-infrastructure-2029-captures-next-wave-value
14 October 2026 · Streams: Industry Structure, Partnerships & Control, Investment, Finance & Market Dynamics, AI Revenue & Service Innovation
AI, new traffic patterns and accelerating compute demand are reshaping digital infrastructure economics. This closing panel examines which revenue pools will grow or shrink, how investment priorities will shift, and where operators, platforms and investors must position now to win the next three years.

### End of Fibre Investment Stage Day 2
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/end-fibre-investment-stage-day-2
14 October 2026
No description published; title, speakers and stream only.

### Voice & Messaging Happy Hour
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/voice-messaging-happy-hour
14 October 2026 · Streams: Social Agenda
No description published; title, speakers and stream only.

### Exhibition Extended Networking Reception
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/exhibition-extended-networking-reception
14 October 2026 · Streams: Social Agenda
No description published; title, speakers and stream only.

### Opening Networking and Coffee
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-session-setting-scene
14 October 2026
The chair opens the session with a concise picture of where the industry stands today: the scale of public scrutiny, the planning challenges facing projects across Europe, and why a unified response i …

### Leadership View
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/roundtable-session-one
14 October 2026 · Streams: Policy, Regulation & Security
Presentation of our findings from the leadership survey & overview of leadership discussion from the Digital Infrastructure Leaders' session held on Monday

### Constructive Communication: How we change perception
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/framing-presentation-changing-minds-starts-within
14 October 2026 · Streams: AI Revenue & Service Innovation
Discover how data centre operators can turn community engagement from a planning challenge into a strategic advantage through clearer, more transparent and more human communication.

### External View - Changing Minds Starts from Within
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/framing-presentation-building-narrative-lands
14 October 2026 · Streams: Policy, Regulation & Security
A leading communications professional shares what effective industry storytelling looks like in practice. Not theory, not aspiration: the specific choices that determine whether a message reaches and …

### Media View - The View From Outside: Why the Industry's Story Isn't Landing
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/roundtable-breakout-3
14 October 2026 · Streams: AI Revenue & Service Innovation
Despite powering the digital economy, the data centre industry continues to face growing public scrutiny and resistance. Drawing on experience from media, public affairs and other highly scrutinised s …

### Group debate questions
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/framing-presentation-view-outside
14 October 2026 · Streams: AI Revenue & Service Innovation
Is the data centre industry suffering from a communication problem, or a trust problem? What can the data centre industry learn from sectors that have faced public scrutiny before it? What should mean …

### Close
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/close
14 October 2026
Chair closes. The key takeaways are confirmed as a post-event publication. Next steps communicated: how the outputs will be shared, who will be credited, and how the work continues beyond October.

### GrowthX @ Capacity Europe: Build what customers will buy next
Speakers: Carl Roberts, Partner - Hadaara Consulting, Dawane M. Young, VP Marketing - VERIZON PARTNER SOLUTIONS, Antonella Sanguineti, Head of Marketing & Product Management Networking, Cloud Security & Identity - SPARKLE, Nico Walters, MD - Matchpoint Telecom Advisory, Amy Cameron, MD, Research - STL Partners, Franck Morales, SVP Marketing & Business Development - ORANGE, Peter Coppens, VP Product - COLT TECHNOLOGY SERVICES, Ryan Tollofson, Director, Products & Services - TELUS Partner Solutions
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-capacity-europe-build-customers-buy-next
15 October 2026 · Streams: GrowthX
A curated space where telco product leads and innovators pressure‑test roadmaps, evaluate emerging business models and monetisation strategies and form the partnerships that generate new revenues and solve customer pain points. Join the Dragons’ Den, demos and roundtables at GrowthX - Apply to speak or showcase your solution by contacting marketing@capacitymedia.com

### GrowthX Welcome
Speakers: Carl Roberts, Partner - Hadaara Consulting
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-welcome
15 October 2026
No description published; title, speakers and stream only.

### Presentation: New control points, new telco value in an AI world
Speakers: Amy Cameron, MD, Research - STL Partners
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-presentation
15 October 2026
How AI agents will change customer relationships: The true catalysts of NaaS? Capturing new network control points: Observability, voice records, sensing

### GrowthX Dragons Round Table
Speakers: Carl Roberts, Partner - Hadaara Consulting, Dawane M. Young, VP Marketing - VERIZON PARTNER SOLUTIONS, Antonella Sanguineti, Head of Marketing & Product Management Networking, Cloud Security & Identity - SPARKLE, Franck Morales, SVP Marketing & Business Development - ORANGE, Ryan Tollofson, Director, Products & Services - TELUS Partner Solutions, Peter Coppens, VP Product - COLT TECHNOLOGY SERVICES, Nico Walters, MD - Matchpoint Telecom Advisory
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-round-table
15 October 2026
No description published; title, speakers and stream only.

### GrowthX Dragons Den Pitch 1
Speakers: Marc Soulacroup, Business Development Director - LATENCETECH
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-1
15 October 2026
Measure it, predict it, sell it: turning QoS into contracts, not complaints.

### GrowthX Dragons Den Pitch 2
Speakers: Robert Lee, Founder - PANOPTES INTELLIGENCE LTD
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-2
15 October 2026
One profile, connect to all: independently verified compliance for wholesale carriers, built once, checked by any counterparty in minutes

### GrowthX Dragons Den Pitch 3
Speakers: Eli Karpilovski, CEO - insidepacket inc
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-3
15 October 2026
Who owns the on-ramp to intelligence? AI capacity lands as islands. The road to it is the bottleneck.

### GrowthX Dragons Den Pitch 4
Speakers: Tema Hassan, Director, Product Development - ZAYO EUROPE
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-4
15 October 2026
The market has solved connectivity - not simplicity.

### GrowthX Dragons Den Pitch 5
Speakers: Inthujan Rasalingam, CEO & Co-Founder - Capacity Connect
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-5
15 October 2026
Capacity Connect is agentic transaction infrastructure for data center capacity: AI agents turn one buyer requirement into an RFP, match it to verified operators, draft the proposals and run the deal to close in one streamlined process.

### GrowthX Dragons Den Pitch 6
Speakers: Joseph Bondi, VP Innovation & Ecosystem Alliances - Ni2
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-6
15 October 2026
Turning the Digital Twin into an agentic growth engine… helping operators automate decisions, accelerate service delivery and unlock new revenue while working in real time across the systems that power what customers will buy next.

### GrowthX Dragons Den Pitch 7
Speakers: Ahsan Khan, CTO - VELINKX LTD
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-7
15 October 2026
VeLinkX is developing digital twin-assisted AI agents to rehearse network changes, test 5G service performance and investigate failures using existing network data.

### GrowthX Dragons Den Pitch 8
Speakers: Ksenija Draskovic, CEO - GlorifAI
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-8
15 October 2026
GlorifAI turns telecom data into customer intent predictions that AI agents can act on in every conversation, lifting retention and revenue.

### GrowthX Closing Remarks
Speakers: Carl Roberts, Partner - Hadaara Consulting
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-closing-remarks
15 October 2026
No description published; title, speakers and stream only.

### Digital Infrastructure Finance & Investment Summit
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-finance-investment-summit
15 October 2026 · Streams: Investment, Finance & Market Dynamics
The Fibre Investment Summit is an invitation-only, Chatham House discussion bringing together 100 senior digital infrastructure executives for an interactive, boardroom-style exchange. Through expert-led debate, live audience participation and exclusive research insights, the session will explore investment strategies, deployment opportunities, risk and underwriting, platform consolidation, and the evolving pathways to value creation and exit across digital infrastructure. For information on how to attend The Digital Infrastructure Finance & Investment Summit, please email: alex.radford@techoraco.com

### Event Arrival & Networking
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/event-arrival-networking
15 October 2026
No description published; title, speakers and stream only.

### Opening Remarks
Speakers: Sam Evans, Senior Managing Director - TENEO STRATEGY (UAE) LIMITED
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-investment-summit/opening-remarks
15 October 2026 · Streams: Investment, Finance & Market Dynamics
Data center-related capex will maintain its vigorous pace in 2026 and take-up is forecast to continue to exceed new supply and provide immense opportunities for investment. An expert macro-analysis will kick off the summit, delve into global headwinds and highlight the strongest growth areas; seeded with headline findings from the Digital Infra Leaders & Fibre Leaders sentiment surveys.

### The State of the Market: The Analyst View
Speakers: Brian Coulton, Chief Economist - Fitch Ratings
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-investment-summit/macroeconomic-overview-state-global-digital-infrastructure-sovereignty-vs-global-interconnection
15 October 2026 · Streams: Investment, Finance & Market Dynamics
Data center-related capex will maintain its vigorous pace in 2026 and take-up is forecast to continue to exceed new supply and provide immense opportunities for investment. An expert macro-analysis will kick off the summit, delve into global headwinds and highlight the strongest growth areas; seeded with headline findings from the Digital Infra Leaders & Fibre Leaders sentiment surveys.

### Fund or Platform: What are the vehicles, and what's for sale?
Speakers: Sam Evans, Senior Managing Director - TENEO STRATEGY (UAE) LIMITED, Thibault Contat Desfontaines, Co-Head of Infrastructure Equity, Europe - UBS Asset Management UK Ltd., Dmitriy Antropov, Head of Infrastructure Partnerships - Partners Group
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-investment-summit/evolving-investment-strategy-behind-digital-infrastructure-private-platfroms-public-giants
15 October 2026 · Streams: Investment, Finance & Market Dynamics
Everybody claims to have “powered land.” What does investment grade actually mean when the market is moving faster than lenders can define it? Why are the biggest allocators building their own vehicles rather than deploying through GPs? Crucially, hearing directly from the allocators setting them up — not just the platforms they've spun out. We will discuss where the large public players fit in and what structures offer the best for various classes of capital owners. Customer type, powered access, contracted revenue quality — the real variables Hyperscaler vs neoscale finance: How do you match 20-year debt with 10-year DC contracts?

### Institutional  Investor Perspectives: Current demands vs. reliable long-term  ROI
Speakers: Jessica Nassar, Management Consultant - Teneo, James Harraway, Head of Value Creation, Infrastructure - GLIL Infrastructure (Local Pensions Partnership Investments), Cengiz Oztelcan, TMT Investor - Qatar Investment Authority (QIA), Andriy Gostik, Principal, Private Equity - EBRD
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-investment-summit/institutional-investor-perspectives-current-demands-vs-reliable-long-term-roi
15 October 2026 · Streams: Investment, Finance & Market Dynamics
LPs from pension, sovereign wealth, private capital and insurance discuss amongst peers how they build conviction. Regulatory, geopolitical and data sovereignty pose risks - as do power shortfalls and increasingly complex fund structures, what factors will decide realistic ROI in the next 5-10 years and how these challenges can unlock new growth opportunities. How are LPs evaluating AI infrastructure risk vs opportunity? Is the GP-LP relationship shifting decisively to dedicated platforms?

### Exit Strategies for a Maturing Asset Class
Speakers: Marin Le Corre, CEO - Alma Capital, Bill Davis, Partner, Digital Infrastructure Global, Investment Management - Ares Management, Charlie Garrood, M&A Leader, UK - AON, Patrik Czornik, Managing Director, Co-Head of EMEA TMT Investment Banking - Bank of America Securities
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-investment-summit/exit-strategies-maturing-asset-class
15 October 2026 · Streams: Investment, Finance & Market Dynamics
Are platforms becoming too large to exit cleanly? What should we read into the recent LLM IPOs — and the nervousness they created? Which pools of capital will actually be there for the next cycle? Do we need to recycle capital faster?

### Closing Remarks: Key Takeaways
Speakers: Sam Evans, Senior Managing Director - TENEO STRATEGY (UAE) LIMITED
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/digital-infrastructure-investment-summit/closing-remarks-key-takeaways
15 October 2026 · Streams: Investment, Finance & Market Dynamics
A closing synthesis of the day's discussions, distilling the most important lessons on investability, platform strategy and exit readiness for the next investment cycle.

### Welcome to the World of Digital Infrastructure
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/welcome-world-digital-infrastructure
15 October 2026
Meet the group at reception, enjoy light refreshments, and prepare for an exciting day exploring digital infrastructure.

### Networking Skills & Personal Branding: Making the Most of Industry Events
Speakers: Ruth Redding, Leadership & Teams Coach - Ruth Redding ltd
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/networking-skills-personal-branding-making-industry-events
15 October 2026
Practical tips on introducing yourself to employers, building confidence, creating a strong LinkedIn profile, and making meaningful connections when meeting companies throughout the day.

### Keynote Panel: Careers You Didn't Know Could Lead to Meta and TikTok!
Speakers: Kyle Hegarty, Managing Director - Leadership Nomad pte ltd, Scott Cowling, Director, Network Investments - Meta, David Saidden, Global Head of Product Partnerships - TIKTOK INC.
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/keynote-panel-careers-know-lead-netflix-meta-tiktok
15 October 2026
Senior leaders from OpenAI, Meta and TikTok discuss the career journeys that led them to some of the world's most sought-after technology companies, and why roles in telecoms and digital infrastructur …

### Exhibition Networking
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/exhibition-networking
15 October 2026
Dedicated time to visit exhibition stands, speak with employers, meet speakers, explore career opportunities and build professional connections across the industry.

### Presentation: So… What Actually Is Digital Infrastructure?
Speakers: Will Rhodes, Head of EMEA Partners - CIENA
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/closing-presentation-ai-anything-industry-need-more-people
15 October 2026
From social media and gaming to streaming and AI, discover the hidden infrastructure that keeps our digital world connected and what it actually takes to make it all work.

### Digital Infrastructure Careers That Don't Require Coding
Speakers: Kyle Hegarty, Managing Director - Leadership Nomad pte ltd, Emily Newman, Marketing Director - NJFX, Sophie Levett, Senior Associate - A&O Shearman, Mark Daley, Director, Digital Strategy & Business Development - EPSILON TELECOMMUNICATIONS
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/tech-careers-require-coding
15 October 2026
Explore opportunities in business, marketing, project management, finance and operations. From securing major deals to managing global projects, discover the diverse careers shaping the digital world …

### Panel: Starting Out in Digital Infrastructure
Speakers: Rebecca Nottingham, Director of Bright Subsea Consulting - SubOptic Foundation, Ellie Skinner, Bid Manager - XTERA, Hasan Salman, System Engineer - XTERA, Henry el Bahnasawy, Emerging Professional - Oceanic Environmental Cables
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-starting-out-digital-infrastructure
15 October 2026
Recent graduates and apprentices share their experiences joining the industry, what they learned during their first roles, and advice for students considering similar career paths.

### Closing Statements & Lunch Break
page: https://www.capacityeurope.com/agenda/capacity-europe-2026/lunch-break
15 October 2026
No description published; title, speakers and stream only.

