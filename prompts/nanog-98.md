>>> HOW TO RUN THIS <<<
This is the digest prompt for nanog-98. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/nanog-98.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/nanog-98.md
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

Below is the program for NANOG 98 (operator). Read it and produce a digest
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
conference: NANOG 98
type: operator
source_url: https://nanog.org/events/nanog-98/agenda/
generated: 2026-11-01
registry_key: nanog-98
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Monday, October 19, 2026

### Keynote: Global Infrastructure and Layer 3 Interconnection
Session: Monday, October 19, 2026, 10:15 - 11:15 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5853/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5853/20261018_Brodsky_Keynote_Global_Infrastructure_v1.pdf | video: https://www.youtube.com/watch?v=elmfXcclcUE
Paul Brodsky – TeleGeography Although annual international bandwidth growth rates are moderating, total used volumes continue to soar. Technological advancements have significantly reduced unit costs per bit, generating a virtuous cycle of lowered pricing and continuous investment. Major cloud hyperscalers—such as Google, Meta, Amazon, and Microsoft—increasingly dominate cable investments, though traditional carriers remain vital partners for navigating complex regulatory landscapes, route diversity, and market entry. Global network resilience is improving through broader cable landing diversity, shifting away from historical single-corridor concentrations. At the same time, geopolitical and physical risks in regions like the Red Sea and South China Sea are prompting new route developments. Geographically, the United States is no longer the sole hub of global bandwidth; regional connectivity is becoming highly distributed, with Europe and specialized regional exchanges (e.g., Miami for Latin America) taking on central roles. While emerging AI workloads introduce complex network demands—such as dataset transfers and spatial-temporal load shifting—their total long-term impact on subsea networks continues to evolve. Finally, despite substantial capital flowing into Low Earth Orbit (LEO) satellite constellations like Starlink, satellite networks function primarily as access technologies rather than replacements for submarine fiber. Ultimately, LEO systems rely on ground stations and Layer 3 interconnections to link with subsea cables, illustrating a complementary relationship in global connectivity.

### Quantum-Safe Networking Starts With the Network You Already Have
Session: Monday, October 19, 2026, 11:15 - 12:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5880/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5880/20261018_Celindro_Quantum-Safe_Networking_Starts_v1.pdf | video: https://www.youtube.com/watch?v=mYa-SCp2O0g
Vin₵ Paul Celindro – Quantum Foundry Quantum computers do not need to be operational today for network operators to have a problem. Traffic with long-term value can be captured now, stored, and attacked later—a threat commonly known as Harvest Now, Decrypt Later. Becoming quantum-safe does not require replacing IPsec, AES, or existing networks; it means modernizing the vulnerable public-key functions used for authentication and key establishment. Starting with familiar IKEv1 and IKEv2 architecture, this operator-focused session explains how Shor’s and Grover’s algorithms affect RSA, ECDSA, DH, and ECDH while AES-256-GCM remains suitable for bulk encryption. We will compare classical and quantum-safe IPsec, introduce hybrid ECDH plus ML-KEM and NIST FIPS 203–205, and explain why PQC should be deployed broadly while QKD is applied selectively. Attendees will leave with a practical migration roadmap: inventory cryptography, prioritize data by confidentiality lifetime, build crypto-agility into network designs, evaluate vendor interoperability, and begin testing quantum-resistant key establishment. Executive Order 14412 and current standards milestones will be placed in operational context. No quantum-computing background is required, and this is not a vendor pitch. The goal is to make quantum-safe networking understandable and actionable for the engineers who will ultimately deploy and operate it.

### From Testing to Reliability: Detecting Silent Failures in Production Systems
Session: Monday, October 19, 2026, 13:30 - 14:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5743/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5743/20261018_Sepuri_From_Testing_To_v1.pdf | video: https://www.youtube.com/watch?v=6Zjeo79n7JI
Shruthi Sepuri Traditional monitoring focuses on infrastructure health metrics such as uptime, latency, error rates, and resource utilization. While these indicators are essential for operational visibility, they do not always reveal when systems begin producing incorrect outcomes after configuration or logic changes. In complex production environments, services may appear fully operational while automated outputs silently drift from expected behavior. This presentation explores how reliability practices can evolve from traditional pre-release testing toward continuous validation of production behavior. As systems increasingly rely on configuration-driven logic, rule engines, and distributed service workflows, detecting these silent failures requires observability beyond infrastructure metrics. The talk examines common failure patterns where configuration changes, rule updates, or dependency interactions alter system behavior without triggering infrastructure alerts. It introduces practical techniques for improving change confidence in production systems, including monitoring automated outcomes, validating outputs against expected baselines, using synthetic production traffic for continuous verification, and detecting statistical anomalies in service behavior. Attendees will gain practical insights into how reliability teams can identify hidden failure modes earlier, extend observability beyond traditional infrastructure metrics, and strengthen change validation practices in complex production systems.

### Multi-Path Traffic Engineering Workshop
Speakers: Vishnu Pavan Kumar Beeram – HPE, Zhaohui (Jeffrey) Zhang – HPE
Session: Monday, October 19, 2026, 13:30 - 17:00 EDT, Biscayne Ballroom (Workshop)
page: https://nanog.org/events/nanog-98/content/5759/
, Kireeti Kompella – Juniper Networks , Registration Required: https://nanog.org/registration/n98-hpe-workshop/ Learn more: https://nanog.org/events/n98-hpe-workshop/ Multi-Path Traffic Engineering (MPTE) [https://datatracker.ietf.org/doc/draft-kompella-teas-mpte/] combines the best of multi-path and TE, and applies to both traditional WAN and AIDC/DCI. It provides both fine-grained traffic control and hop-by-hop multipathing, where the multipathing need not be strictly equal-cost, nor the load balancing equally weighted to each next hop. Moreover, the desired destination may be reachable via multiple egresses from multiple ingresses. Different protocols can be used to signal MPTE paths, including RSVP/BGP extensions [https://datatracker.ietf.org/doc/draft-kbr-teas-mptersvp/] [https://datatracker.ietf.org/doc/draft-zzhang-idr-mpte-signaling/] MPTE was presented at NANOG96

### https://nanog.org/events/nanog-96/content/5667/
Session: Monday, October 19, 2026, 13:30 - 17:00 EDT, Biscayne Ballroom (Workshop)
page: https://nanog.org/events/nanog-96/content/5667/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG96/5667/20260204_Kompella_Multipath_Traffic_Engineering_v1.pdf | video: https://www.youtube.com/watch?v=nYef0pTpEgs
] It was well-received, and people were eager to try it out. The workshop will provide an opportunity for interested parties to learn more details of MPTE, experience it first-hand in a virtual environment (of HPE/Juniper vMX/cRPD) - from configuration to observing the MPTE DAG calculations and RSVP/BGP signaling in both WAN and AIDC scenarios - and provide feedback for us to improve the technology and implementation.

### RNG: Flat Datacenter Networks at Scale
Speakers: Ratul Mahajan – AWS
Session: Monday, October 19, 2026, 13:30 - 14:15 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5894/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5894/20261018_Mahajan_Rng_Flat_Datacenter_v1.pdf | video: https://www.youtube.com/watch?v=AVKZmklWsAQ
We designed and deployed at Amazon the world's first flat datacenter networks. Our design, called RNG, is based on quasi-random graphs. While the cost and fault-tolerance benefits of such topologies have been long known, their practical realization has been hampered by a lack of scalable routing and cabling approaches. RNG has a new distributed routing protocol that exploits the properties of random graphs to find a large number of edge disjoint paths between pairs of endpoints. It uses a novel passive optical device that internally shuffles cables, which makes its cabling complexity similar to that of fat trees. We show that RNG matches or exceeds the performance of fat trees for a range of traffic patterns, despite being up to 45% cheaper. RNG is now the default datacenter network for most workloads at Amazon.

### NOG (Network Operator's Group) BoF
Session: Monday, October 19, 2026, 13:30 - 15:00 EDT, Michelangelo
page: https://nanog.org/events/nanog-98/content/5854/
Vin₵ Paul Celindro – Quantum Foundry Do you run a NOG? Are you part of a NOG and want to get more involved? Interested in running a NOG? This BoF will be an open discussion for anyone and everyone who is already running or is interested in running a NOG or just helping out. - Regional NOG updates - Mutual challenges and concerns - What can we do to help the NOG communities as a whole

### What Building a Network Emulation Platform Taught Me About Digital Twins
Speakers: Craig Johnson – Forward Networks
Session: Monday, October 19, 2026, 14:00 - 14:45 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5893/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5893/20261018_Johnson_What_Building_A_v1.pdf | video: https://www.youtube.com/watch?v=ImAvxShPst8
Modern network engineers have more options than ever for testing changes before they reach production: virtual network operating systems, containerized labs, topology-as-code, CI/CD pipelines, and increasingly, network digital twins. But these approaches don’t all answer the same questions. Over the past year, I built an internal network emulation platform designed to create realistic, multi-vendor network environments on demand. The goal was straightforward: make it easy to reproduce networks, test changes, inject failures, and validate behavior before touching production. Building it exposed an important distinction between emulating a network and modeling one. This session explores that distinction through practical examples and lessons learned. We’ll look at where network emulation works exceptionally well, where its fidelity begins to break down, and why simply running more realistic virtual devices doesn’t necessarily produce a better model of production behavior. We’ll then examine how behavioral modeling and digital twins approach the problem differently, particularly for questions such as reachability, policy changes, failure impact, and predicting the consequences of configuration changes. Rather than arguing that one approach replaces the other, this talk will show how emulation, automated validation, and network modeling can complement each other—and what I learned trying to build a system that uses all three.

### One Control Plane Away: Are Cloud Providers Critical Infrastructure
Session: Monday, October 19, 2026, 14:15 - 14:45 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5884/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5884/20261018_Tzvetanov_One_Control_Plane_v1.pdf
Krassimir Tzvetanov – Purdue University Recent incidents — most visibly the December 2025 Cloudflare outage — show that a single provider's control-plane failure can take a measurable fraction of the web offline at once. We present a measurement study of provider concentration across the Tranco top 10,000 domains that separates three dependency layers usually conflated: who fronts a site's traffic (CDN/edge), who hosts its origin, and who serves its authoritative DNS. Using layered evidence — CNAME chains for apex and www, provider-published service ranges (e.g., AWS's CLOUDFRONT vs EC2 tags), HTTP and TLS fingerprints, and BGP origin data — we first show that naive IP-to-ASN attribution, still common in public statistics, undercounts CNAME-deployed CDNs by up to 2.7x (Akamai) while overcounting cloud providers by conflating hosting with fronting. Findings: concentration increases down-rank. Cloudflare fronts 28.5% of classified top-1,000 domains but 45.7% of the top-10,000 — the biggest properties diversify (13% of strongly-fronted domains are demonstrably multi-CDN) while the mid-tail single-homes. Authoritative DNS is separately concentrated: Route 53 serves 22% and Cloudflare 26% of live domains; only 14% self-host DNS. Combining layers, 21.9% of live top-10k domains depend on Cloudflare for both DNS and delivery — one control-plane event from total unavailability — and 37.9% are double-dependent on some single organization. We close with week-over-week change data from our ongoing weekly measurement pipeline (running since August 2026) and a practical exposure-assessment recipe operators can apply to their own dependency chains. The measurement tool and dataset will be released at publication

### Managing Risk for Internet2's Network Services Group
Session: Monday, October 19, 2026, 14:45 - 15:30 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5907/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5907/20261018_Thaxton_Managing_Risk_For_v1.pdf | video: https://www.youtube.com/watch?v=vzeLbURjkb4
Adair Thaxton – Internet2 Nobody likes talking about risk, but we all have to deal with it. Internet2 has been working to expand and improve our risk management processes for our network devices.

### Your Change Deserves a Dress Rehearsal: Digital Twins from Production State with Containerlab and OTG
Speakers: Brad Tarno – The Walt Disney Company
Session: Monday, October 19, 2026, 14:45 - 15:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5865/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5865/20261018_Tarno_Your_Change_Deserves_v1.pdf | video: https://www.youtube.com/watch?v=633Z0dxvMzg
Syntax checks, peer review, and even LLM-based review all share the same blind spot: none of them evaluate a change against live routing state. Every operator has seen where that leads. A one-line, syntactically valid change reads perfectly in review and behaves very differently on the wire. We rehearse almost everything else we do that is risky. Network changes usually meet production for the first time in production. This talk describes a platform we built to close that gap. A self-service lab-as-a-service system that builds disposable digital twins from what production actually runs. It harvests device configurations across a multi-vendor network, transforms them per platform to boot on virtual NOS images, deploys the topology with containerlab, and wraps the twin in a validation harness. Open Traffic Generator flows graded convergence-aware, emulated BGP peers replaying real routes with full attributes including communities, and Batfish+hier_config differential analysis of the predicted post-change config. We will walk the architecture, replay a real incident-class scenario that the platform now catches as a permanent regression test, and share hard-won lessons from live-fire use. Every load-bearing component is open source, so attendees will leave with the recipe.

### Building Community Owned Critical Infrastructure
Speakers: Matt Griswold – 20C, Open Pipes
Session: Monday, October 19, 2026, 16:00 - 16:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5864/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5864/20261018_Griswold_Building_Community_Owned_v1.pdf | video: https://www.youtube.com/watch?v=6eQ-EfYEi6g
Open Pipes addresses the fragility of commercial critical infrastructure by introducing a community-owned, non-profit model for Internet Exchanges. By prioritizing community governance and self-sustainability, the Open Pipes framework prevents the misalignment of incentives common in commercial ownership, ensuring that assets remain dedicated to the community they serve. The project provides a structured, replicable approach to IXP design -- currently piloted in Chicago -- that integrates automated infrastructure, neutral oversight, and local self-governance. Beyond physical connectivity, Open Pipes aims to preserve collective industry expertise through its open knowledge documentation and a newly launched Mentor Network designed to foster professional growth and community engagement for the next generation of Internet engineers.

### A Blueprint for Securing Networks for AI : From Architecture to Operations
Speakers: Saju Salahudeen – NOKIA, Reda Laichi – NOKIA
Session: Monday, October 19, 2026, 16:00 - 16:30 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5869/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5869/20261018_Salahudeen_A_Blueprint_For_v1.pdf | video: https://www.youtube.com/watch?v=MqnHA9hBX5M
, As demand for high-performance AI clusters outpaces deployment speed, securing the underlying infrastructure has become a critical operational priority. Because traditional security boundaries blur at the data center fabric, the network must serve as the primary line of defense against modern threats. This session introduces a holistic blueprint for securing AI network infrastructure from the ground up. Walking through the complete network lifecycle, we will break down essential, multi-vendor security measures across Day 0, Day 1, and Day 2 phases. Attendees will leave with a practical framework to isolate backend GPU fabrics, mitigate data exfiltration risks, and protect massive AI workloads without sacrificing performance.

### The Evolution of Internet Exchanges through the eyes of CANIX
Speakers: Karl Morin – CANIX
Session: Monday, October 19, 2026, 16:30 - 17:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5825/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5825/20261018_Morin_The_Evolution_Of_v1.pdf | video: https://www.youtube.com/watch?v=QSXzCKHCfG0
An overview of how IXs have been run and how CANIX sees their future from a technical, organizational and and service offering point of view .

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings
Speakers: Gerhard Stein – Flexoptix GmbH
Session: Monday, October 19, 2026, 16:30 - 17:00 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5852/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5852/20261019_Stein_Understanding_And_Optimising_v1.pdf | video: https://www.youtube.com/watch?v=GSSMEH9adUg
, Thomas Weible – Flexoptix In high-performance optical communication systems transceiver health and efficiency are critical to network reliability and energy consumption. This presentation explores the powerful capabilities of Versatile Diagnostics Monitoring (VDM) features found in modern optical transceivers (beyond the speed of 100G) with a particular focus on the Thermoelectric Cooler (TEC) current metrics. By analysing TEC current alongside temperature and cable length data we should be able to identify the optimal operating conditions that will minimise power consumption while maintaining performance. In order to prove this thesis we developed a couple of software prototypes to perform the data analysis. Using real-world VDM data this talk will demonstrate how to evaluate and visualise transceiver efficiency in terms of Watts, uncovering practical insights for engineers aiming to design or operate greener, more efficient optical networks and finally save energy.

### NANOG 98 Peering Coordination Forum
Session: Monday, October 19, 2026, 17:00 - 18:30 EDT, Chopin Ballroom
page: https://nanog.org/events/nanog-98/content/5924/
The forum provides time for attendees to meet and network with others in the peering community present at NANOG. Peering Representatives, who completed and submitted the form will have a dedicated highboy table for up to 2 representatives. They will be able to distribute business cards, and provide a white paper or 1 sheet marketing page. Please note: any other type of giveaway is not allowed. Complete the form here before October 9: https://www.nanog.org/events/nanog-98/peering/

## Tuesday, October 20, 2026

### Keynote: Why Do We Have Self-Driving Cars, But Not Autonomous Networks?
Speakers: John Evans – Independent
Session: Tuesday, October 20, 2026, 10:00 - 11:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5738/ | slides: https://www.nanog.org/sites/default/files/1_Kompella_The_Networking_Grand_Challenge.pdf | video: https://www.youtube.com/watch?v=Jf_2t1GF9mA
Self-driving cars were imagined as early as 1918 [1], accelerated by the DARPA Grand Challenge era (2004–2007) [2], and are now beginning to operate at commercial scale. Self-driving networks were framed as an industry ambition in Kireeti Kompella’s 2017 NANOG talk [3]. But in networking, “driving” has come to mean several different things: configuration automation, network control, or automated operations. The industry has made significant progress in configuration automation and network control, including traffic engineering and VPN control. Yet most network operations still live in an alert → ticket → operator loop, assisted by runbooks and, increasingly, copilots and agents. This talk focuses on autonomous network operations, the missing piece for network autonomy. So, nearly ten years on, why are self-driving cars becoming reality at scale, while autonomous network operations is still an industry ambition? The answer isn’t that networks are somehow harder than cars. The issue is more fundamental. Networking is approaching autonomous operations as an observability and workflow problem, building on the systems we already have. That is the natural first step when applying AI to network operations. But self-driving cars have shown that autonomy is not simply another AI capability added to existing systems. It requires a paradigm shift in architecture, signals, models and control. In this keynote, we apply the control-system approach used in self-driving cars and robotics to autonomous network operations, assess what is missing today, show where autonomy can be deployed safely first, and describe a realistic path for the industry to move from assisted operations towards autonomous control. [1] Apex.AI — “The Driverless Car Era Began 100 Years Ago” https://www.apex.ai/post/the-history-of-automated-driving-part-one-the-driverless-car-era-began-100-years-ago [2] DARPA — “The DARPA Grand Challenge: 10 Years Later” https://www.darpa.mil/news/2014/grand-challenge-ten-years-later [3] Kireeti Kompella (NANOG, June 2017) — “The Self-Driving Network™: How to Realize It” https://www.nanog.org/sites/default/files/1_Kompella_The_Networking_Grand_Challenge.pdf

### IXP BoF
Speakers: Matt Griswold – 20C, Open Pipes
Session: Tuesday, October 20, 2026, 11:00 - 12:00 EDT, Michelangelo
page: https://nanog.org/events/nanog-98/content/5861/
Chris Malayter – CoreSite , , Martin Hannigan – Lightboard If you run a Internet Exchange Point (IXP) or you’ve been thinking about starting one, don’t miss the IXP BoF at NANOG 98. We’ll swap stories, share lessons learned, and talk about what’s working (and what we wish we’d known) in building successful IXPs.

### IPv6 Routing Loops -- A Call to Fix Router Configurations
Session: Tuesday, October 20, 2026, 11:00 - 11:30 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5876/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5876/20261018_Koch_Ipv6_Routing_Loops_v1.pdf | video: https://www.youtube.com/watch?v=OpjHdWE8es8
Maynard Koch Routing loops and the amplification of looping packets are known problems on the IPv6 Internet. In a recent measurement study, we found that both problems are still present, potentially harming Internet stability. Although routing loops are often easy to fix, they receive limited attention from the network operator community. Since 2025, we aim to raise awareness of routing loops and amplification at network operator events. In 2026, we started to weekly measure the deployment of routing loops and amplifications on the IPv6 Internet. In this talk, we present how community outreach has helped significantly reduce the impact of these network misconfigurations in the RIPE NCC and APNIC region -- which motivates to reach out to other regions as well. We provide detailed insights on the current state of these issues on the IPv6 Internet with a particular focus on the ARIN region. We hope these misconfigurations will eventually disappear and encourage the NANOG community to spread the word, check their networks, and help eliminate routing loops from the IPv6 Internet. Until then, we will continue measuring, reporting, and raising awareness. To assist in resolving these problems, we have made our findings publicly available at https://ipv6-sra.realmv6.org/routingloops, allowing operators to check whether their networks are affected by routing loops.

### When the World Cup Moved to YouTube: 416 Gbps and the Limits of Local Delivery in Brazil
Session: Tuesday, October 20, 2026, 11:00 - 11:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5895/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5895/20261018_Ornelas_When_The_World_v1.pdf | video: https://www.youtube.com/watch?v=g7DKhsfdY2M
Renato Ornelas – OpenX (Brazil) In 2022 Globo, which had broadcast every World Cup in Brazil since 1970, gave up its digital transmission rights in a mid-pandemic renegotiation. A YouTube channel picked them up. By 2026 that channel was the only Brazilian outlet carrying all 104 matches — which meant an entire nation's World Cup arrived over a single CDN, with no paywall, no dedicated app, and no delivery infrastructure of its own. This talk presents traffic telemetry from OpenX (AS263444), a Brazilian wholesale transit operator with 60+ downstream ASNs and 1–3 million broadband subscribers behind it, across all 34 match nights. The tournament peaked at 416 Gbps from Google alone and added roughly 12 PB above equivalent football-free windows. More interesting than the peak is where it came from: at the tournament maximum, embedded cache was pinned at its 79 Gbps ceiling and the Cotia PNI at 200 Gbps, and 40% of delivered traffic — 165 of 409 Gbps — arrived over international transit from North America and Europe. We also show a behavioral signature visible only at half-time, where Google, Meta and Netflix move in three different directions within the same fifteen minutes, and why kickoff hour predicted peak traffic better than audience size did.

### When BGP Graceful Restart Wasn't Graceful
Speakers: Marian Rychtecky – NIX.CZ
Session: Tuesday, October 20, 2026, 11:30 - 12:00 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5897/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5897/20261018_Rychtecky_When_Bgp_Graceful_v1.pdf | video: https://www.youtube.com/watch?v=eQM-un3K_yA
BGP Graceful Restart should reduce traffic impact during short control-plane interruptions. During our firewall HA upgrade, we expected it to hide the failover. Instead, after GR was enabled, the failover caused almost two minutes of traffic loss. This talk walks through the troubleshooting: Established BGP sessions with zero prefixes, delayed End-of-RIB, different IPv4 and IPv6 behavior, packet captures, vendor logs and a small BIRD lab test. The takeaway is simple: GR is only graceful when the implementation matches real HA behavior. Otherwise, it can make an outage longer instead of shorter.

### Stop using 100GBASE-LR4
Session: Tuesday, October 20, 2026, 11:30 - 12:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5859/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5859/20261018_Steenbergen_Stop_Using_100Gbase-Lr4_v1.pdf | video: https://www.youtube.com/watch?v=2Uz7HqLGhcs
Richard Steenbergen – Petabit Scale A guide to modern 100G optical technologies

### SRv6 and MRC for AI Data Centers
Session: Tuesday, October 20, 2026, 13:30 - 14:15 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5846/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5846/20261018_Styszynski_Srv6_And_Mrc_v1.pdf | video: https://www.youtube.com/watch?v=ze3ORk9sGrI
Michal Styszynski – Juniper Networks The AI DC extends the SRv6 use-cases in order to improve the ROCEv2 with a reliable connection and deterministic transport. The session will deep-dive into the new MRC (Mulitipath Reliable Connection) use-cases where the SRv6 is used at the GPU server NIC card and at the AI Ethernet switches. It will include the architecture and implementation perspective for the new AI DC use cases where MRC and SRv6 are used.

### Installing, configuring, and using the open source Kea DHCP server
Session: Tuesday, October 20, 2026, 13:30 - 17:00 EDT, Biscayne Ballroom (Workshop)
page: https://nanog.org/events/nanog-98/content/5828/
Darren Ankney – ISC , Doug Freed – ISC , Eddy Winstead – ISC Registration Required: https://nanog.org/registration/n98-isc-workshop/ Learn more: https://nanog.org/events/n98-isc-workshop/ This workshop is for people who want to run DHCP servers for their network who want to get some quick exposure to the Kea DHCP system. Participants should be familiar with the Linux CLI, novice level is ok, and should have access to an ssh client. Users will be given VMs and walked through the installation of two Kea DHCP servers and a client simulator, which will generate traffic. - After installation, we will configure the Kea servers, establishing one as the primary and the other as a backup system, and adding a subnet, a pool and some logging. - After starting everything up, we will run a few tests to determine that everything is operational, including generating some client traffic to see addresses assigned. - We will then install the Stork graphical management system and the Stork agent, authorize our Kea servers for monitoring and allow everyone time to explore the interface. - Depending on the group's progress, we will trigger a failover event, to test the high availability set-up. - After testing the high availability setup, we will then demonstrate and allow users time to follow along with editing the configuration.

### Panel: 2026 NANOG Board Candidate Forum
Speakers: Leif Sawyer – GCI Communication Corp (AS8047), Tom Beecher – Yahoo
Session: Tuesday, October 20, 2026, 13:30 - 15:00 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5872/
, , Marlin Martes , Michael Still – Myriad360 , Adair Thaxton – Internet2 Hear from candidates as they answer questions asked by panel moderator Leif Sawyer. Remote attendees are invited to join the session live via the zoom link sent to NANOG Members. NANOG Members are invited to leave Statements of Support for the candidates from 15-September-2026 through the end of the election cycle. Voting will open after the conclusion of this Candidate Forum.

### Auto-bandwidth for Segment Routing
Speakers: Dmytro Shypovalov – Vegvisir Systems
Session: Tuesday, October 20, 2026, 14:15 - 14:45 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5866/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5866/20261018_Shypovalov_Auto-Bandwidth_For_Segment_v1.pdf | video: https://www.youtube.com/watch?v=zxytzHQHEe8
Many ISP use MPLS-TE auto-bandwidth to balance traffic in their network. With transition to Segment Routing, there is a challenge of implementing a similar solution due to the stateless nature of SR. The presentation describes challenges of auto-bandwidth implementation for SR and demonstrates a working prototype.

### ARIN Update: What’s Changing and What’s Next for Network Operators
Speakers: Matthew Wilder – TELUS
Session: Tuesday, October 20, 2026, 14:45 - 15:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5871/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5871/20261018_Diego_Arin_Update_What_S_v1.pdf | video: https://www.youtube.com/watch?v=gZxE7cN3WB0
Edward Diego – American Registry for Internet Numbers (ARIN) , Douglas Camin , , alison wood , Joe Westover – ARIN What’s happening at ARIN, and what does it mean for the networks and organizations that rely on Internet number resources? This session begins with an update on ARIN’s current activities, services, and initiatives that are relevant to the network operator community. From there, we’ll turn to the policies that shape how Internet number resources are managed and distributed - and how those policies can affect the organizations that use them. We’ll explore the issues behind these proposals, what they could mean for organizations seeking or holding number resources, and the questions the community should be considering as the policies evolve. Attendees will also get a practical look at how to engage in the ARIN policy development process and provide feedback while proposals are still being shaped.

### Interplanetary Internet Architecture, Addressing, and Routing
Session: Tuesday, October 20, 2026, 15:00 - 15:30 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5890/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5890/20261018_Eddy_Interplanetary_Internet_Architecture__v1.pdf | video: https://www.youtube.com/watch?v=DW_7xwPLIT8
Wesley Eddy – Aalyria Several different countries and private companies are now engaged in space missions to the Moon and Mars. Mission systems increasingly make use of IP and Internet protocols, and standards have been developed that include support for IP on typical space mission data links. Recently, the IETF formed a working group on Taking IP To Other Planets (TIPTOP), that is creating an architecture for the use of IP-based protocol stacks in networks spanning the Earth and Lunar or Mars domains. There are many aspects to this, including configuration of QUIC and other protocols, but this presentation will summarize the architecture and then focus on topics of IP addressing and routing. It includes a summary of multiple active proposals for IP prefix allocation management policies, as well as discussion of approaches and technologies for routing and network orchestration for deep space systems with very long delays and periods of disconnection.

### Wireshark - From Banned Application to an Everyday Tool
Speakers: Annika Snead – Hibbett
Session: Tuesday, October 20, 2026, 16:00 - 17:00 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5887/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5887/20261018_Snead_Wireshark_-_From_v1.pdf | video: https://www.youtube.com/watch?v=Yi6j4ZTIVng
In its beginning as Ethereal, Wireshark was banned on most networks and was a reason to be fired, due to its power to reverse captured traffic back into a human readable format without being part of the TCP/UDP session itself. Nowadays it's a basic tools a lot of professionals throughout Security, Network and Server teams are using. Many know about it, can install and capture, but then are lost when it comes to interpreting the output. Packet capturing has become a standard installment in a lot of systems, it's available on PaloAlto and Cisco Firewalls, Meraki Dashboard and many more. I will be going over how important the OSI model and it's purpose. How to use Wireshark to run captures, using filters, interpreting the output and, depending on time, running a demo on how easy it can be used.

### ASPA la vista.. Route leaks
Session: Tuesday, October 20, 2026, 16:00 - 16:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5878/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5878/20261018_Strachan_Aspa_La_Vista__v1.pdf | video: https://www.youtube.com/watch?v=ZjrwHTfzRmk
Alastair Strachan – RIPE NCC ASPA stands for Autonomous System Provider Authorisation and is a relatively new type of object standardised in the RPKI ecosystem. ASPA objects are signed by AS owners and allow an AS to declare its authorised upstream providers, which prevents route leaks, BGP path spoofing, and valley-free routing violations. They can be created in the hosted RPKI systems of ARIN and RIPE NCC, or using delegated RPKI CA software such as Krill. ASPA standard has already seen significant uptake and is supported by some of the software routers.

### Network Automation BoF
Speakers: Ryan Hamel – Zayo
Session: Tuesday, October 20, 2026, 16:00 - 17:30 EDT, Michelangelo
page: https://nanog.org/events/nanog-98/content/5837/
If you are curious about network automation and/or software development, do not miss the Network Automation BoF at NANOG 98. We'll swap stories, share lessons learned, and talk about what's working (and what we wish we'd known) in implementing network automation and software development in general.

### False Immunity: long prefixes that bypass ROV
Speakers: Bryton Herdes – Cloudflare
Session: Tuesday, October 20, 2026, 16:30 - 17:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5843/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5843/20261018_Herdes_False_Immunity_Long_v1.pdf | video: https://www.youtube.com/watch?v=iLgvebGwlpw
There has been significant progress in the realm of Resource Public Key Infrastructure (RPKI) for BGP routing security. We’ve reached over 50% of BGP prefixes having Route Origin Authorizations (ROAs) signed by resource holders. Also, most major networks have already implemented Route Origin Validation (ROV) based on those ROAs. However, we’re still falling short of secure BGP routing, even against hijacks, which ROV is meant to prevent. In this presentation, I will talk about flaws that still exist in even major networks who have otherwise implemented ROV. There exists critical edge-cases that allow networks who do not own IP prefixes to still hijack or blackhole traffic toward them in large networks. One of these edge-cases comes down to poor practices by some operators pertaining to long prefix (>/24, or >/48) announcements, and the other is a more systemic vulnerability of a specific type of blackhole route filtering. I will cover both cases in detail to show how ROV has provided us with a false sense of immunity against route hijacks.

### Your Route Was Dropped—But Where and Why? Closing RPKI’s Operational Feedback Gap
Session: Tuesday, October 20, 2026, 17:00 - 17:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5874/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5874/20261018_Kang_Your_Route_Was_v1.pdf | video: https://www.youtube.com/watch?v=LVeD2_QLZCk
Min Suk Kang – KAIST Route Origin Validation (ROV) helps prevent prefix hijacking by allowing networks to reject BGP routes that are inconsistent with published Route Origin Authorizations (ROAs). For prefix owners, however, such rejection is largely silent: an announcement may be filtered somewhere on the Internet, yet the owner has no direct way to learn where it was rejected, how much reachability was lost, or whether the invalid route resulted from an attack or the owner’s own operational action. This lack of feedback matters because not every ROV-invalid route is malicious. Benign invalid routes can arise from configuration mistakes or urgent routing changes, such as redirecting traffic to a mitigation provider during a DDoS attack before the corresponding ROA update has propagated. In this talk, we characterize these benign-invalid scenarios and use measurement data and large-scale simulations to show how silent filtering can delay diagnosis and impair reachability. We then present interactive ROV (iROV) as one possible direction for closing this feedback gap. iROV allows a validating network to obtain just-in-time authorization from the prefix owner while notifying the owner of the invalid announcement and its observed impact. Our evaluation shows that this approach can increase reachability for urgent route changes from 23% to nearly 90%, while bounding query load through validity stapling and probabilistic querying. We present iROV as a concrete starting point for discussion with the operator community: What feedback should ROV provide, and how could such feedback be introduced without creating unacceptable operational or security risks?

### Affogatos: Navigating Intergenerational Working Relationships
Speakers: Kelly Sieben – DE-CIX, Steve Feldman – Paramount
Session: Tuesday, October 20, 2026, 17:00 - 18:00 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5841/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5841/20261018_Sieben_Affogatos_Navigating_Intergenerational_v1.pdf | video: https://www.youtube.com/watch?v=3YoQC3SxfHc
, Paul Kaiser , Pyper Scharer , Rina Tajvar , malinda walters , From early-career engineers and business professionals to industry veterans, the internet community depends on cross-generational collaboration. This panel will explore how we can bridge generational differences, create inclusive workplace cultures, and leverage diverse perspectives to strengthen our teams and community. Through candid discussion and personal stories, panelists will share lessons learned, strategies for effective communication, and ways to foster mutual respect and knowledge transfer in our rapidly evolving industry.

### Builder Bof: Bringing Back The Hack
Session: Tuesday, October 20, 2026, 17:30 - 17:40 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5957/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5957/20261020_Woodfield_Builder_Bof_Bringing_v1.pdf | video: https://www.youtube.com/watch?v=19ZNAvYRQd8
Chris Woodfield It’s a new format for today’s NANOG, with a Birds of a Feather (BoF) event in Boston that will let you share the projects you’re passionate about with others who love doing the same. It’s a chance to build community as well as networks, and to make new contacts and catch up with old ones. The main part of the BoF will be a "lightning demos" round, where attendees can submit projects for consideration to present, similar to a lightning talk.

### Updating MANRS Routing Security Guidance
Speakers: Tony Tauber – Comcast
Session: Tuesday, October 20, 2026, 17:40 - 17:50 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5958/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5958/20261020_Tauber_Updating_Manrs_Routing_v1.pdf | video: https://www.youtube.com/watch?v=G54ZEevAI8g
In 2014, a group of Network Operators developed consensus baselines with the aim to improve security of the global BGP routing system. This guidance became what is called MANRS (Mutually Accepted Norms for Routing Security). Technology and the broader landscape have changed; the time has come to reexamine the baselines for possible changes. That process is now entering the stage for feedback on the proposed updates from the broader community. Andrei Robachevsky and Andrew Gallo are co-Chairs of the Working Group that is developing the updates. They could not attend in person but wanted this information presented to the NANOG98 audience on their behalf.

### Enforcing the First AS in BGP AS_PATHs
Speakers: Bryton Herdes – Cloudflare
Session: Tuesday, October 20, 2026, 17:50 - 18:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5956/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5956/20261020_Herdes_Enforcing_The_First_v1.pdf | video: https://www.youtube.com/watch?v=cqA3_-aEdZ8
We have RPKI-ROV that helps to reject blatant BGP origin hijacks. We will soon have RPKI-ASPA which prevents many forged-origin hijacks from having wide impact. However, there exists one hijack that neither ROV or ASPA will be able to account for. A hijacker may strip enough information from a network path that neither ROV or ASPA are effective. In an experiment we ran, we found that half of the Tier-1 networks are vulnerable to this type of attack and the problem is largely caused by bad defaults in vendor BGP implementations. The good news is there is a simple, existing, solution and configuration to remove the vulnerability in your network. Networks should enforce the "First AS" in BGP, requiring that in almost all situations the First AS of the AS_PATH match the adjacent peer's AS.

## Wednesday, October 21, 2026

### Salvaged Silicon: Building an Open Network OS for a Switch the Industry Left for Dead
Session: Wednesday, October 21, 2026, 10:00 - 10:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5870/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5870/20261018_Wright_Salvaged_Silicon_Building_v1.pdf | video: https://www.youtube.com/watch?v=NN5yK6MDkQo
Christopher Wright Whitebox switching promised to break the vendor NOS monopoly: buy the hardware, pick your OS. But go actually do it, and you hit the fine print — the practical, supported NOS options are licensed. A subscription, a support contract, or a compatibility list sits between you and a running switch. “Open” turned out to mean disaggregated, not free and open source. That gap is where EdgeNOS starts: a from-scratch, genuinely free-and-open-source network OS — no license, no contract, no vendor firmware — built to bring end-of-life switches and routers back to life. The hardware is fine; only the software support ran out. The design treats the box as an ordinary Linux router: the kernel FIB is the source of truth, and a userspace agent mirrors it into the switch ASIC’s tables. The payoff for operators — it’s just Linux, the same commands, tools, and routing daemons you already run, but the forwarding happens in silicon at line rate.

### Is Traceroute Lying or Does it Just Hate Me? An Intermediate-to-Advanced Traceroute Tutorial
Session: Wednesday, October 21, 2026, 10:00 - 11:30 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5856/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5856/20261018_Sinatra_Is_Traceroute_Lying_v1.pdf | video: https://www.youtube.com/watch?v=UytibfNaQko
Michael Sinatra – Energy Sciences Network This tutorial attempts to provide a comprehensive look at how to use some of the more modern (and traditional) tools and correctly interpret the results. Traceroute, and related tools like tracepath, MTR, Paris traceroute, etc. (I call them "trace-tools"), all look easy (and fun!) to use and understand, but dragons lurk within. This talk builds on the excellent tutorials given by Richard A. Steenbergen in venues like NANOG and RIPE, and, as a special form of recognition, I steal some of his slides! The talk builds further, though, examining the use of trace-tools to diagnose network issues with a specific emphasis on modern networks and their use of traffic-engineering, plus L3VPN and MPLS technologies--all of which make trace-tools behave rather differently than in the networks for which they were originally developed. The talk concludes with some recent real-life use of trace-tools and the inferences that we can make from their results. Optional Prerequisite: Attendees are encouraged to view Richard A. Steenbergen's traceroute tutorial from NANOG 80 (

### https://nanog.org/events/nanog-80/content/2259/
Session: Wednesday, October 21, 2026, 10:00 - 11:30 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-80/content/2259/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG80/2259/20201020_Steenbergen_Troubleshooting_With_Traceroute_v1.pdf | video: https://www.youtube.com/watch?v=L0RUI5kHzEQ
) as this presentation will be extending some of that content.

### A Journey of Accelerating and Offloading OVS with a DPU
Session: Wednesday, October 21, 2026, 10:30 - 11:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5886/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5886/20261018_Sevincer_A_Journey_Of_v1.pdf | video: https://www.youtube.com/watch?v=3Pg7atxbx6U
Abdullah Sevincer – Crusoe , Alex Bortok – NVIDIA Every host CPU cycle spent processing network traffic is a cycle that isn't available for customer workloads. This talk tells the story of how we moved OVN/OVS networking off the host entirely — in two deliberate steps, not one big leap. We started on a standard kernel datapath, where sustained connection rates topped out in the low thousands per second and instability grew with load. The first step was moving to a hardware-accelerated OVS datapath on the host: dedicated poll-mode driver threads and hardware connection-tracking offload took the same hardware to an order-of-magnitude higher connection rate with near-zero failures — at the cost of reserving host CPU cores and memory that used to be free for VMs. The second step went further: offloading the OVS/OVN control plane itself onto a DPU, freeing 100% of host CPU for customer workloads. This step came with its own lesson — the DPU's cores aren't identical to host cores, so getting the right thread count mattered more than simply adding more. We'll walk through real production benchmark data from each stage, the tradeoffs at each step, and what this means for running SDN at fleet scale — a practical, numbers-backed account of the path from kernel networking to a fully offloaded, DPU-based control plane.

### Is This Application IPv6 Ready?
Speakers: Sávyo de Morais – NIC.br
Session: Wednesday, October 21, 2026, 11:30 - 12:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5903/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5903/20261018_De_Morais_Is_This_Application_v1.pdf | video: https://www.youtube.com/watch?v=zjE5IHdO5iU
IPv6 deployment is increasingly revealing a problem beyond routers, BGP and addressing: applications that have never actually been validated for dual-stack or native IPv6 operation. A service may possess an AAAA record, accept inbound connections, and appear completely ready while masking deep-seated architectural dependencies on IPv4. Dual-stack environments frequently hide these problems because IPv4 acts as an invisible safety net or silent fallback. The core question facing any app developer, maintainer, or operator is deceptively simple: "If I enable IPv6 and dual-stack in this application today, will it actually work properly?" This presentation looks at IPv6 readiness from the application and operations perspective. We will how to proactively test whether an application can successfully run across diverse network topologies — including dual-stack, NAT64, and strict IPv6-only environments. The talk will also share NIC.br's experience that led us to develop V6bench, an open-source tool originally created for API testing. Rather than focusing on the tool itself, we will use it as a case study of the challenges involved in making repeatable IPv6 application testing accessible to developers, SREs, system administrators and network operators.

### ESnet’s Discovery Service: A generic configuration repository and abstraction layer
Session: Wednesday, October 21, 2026, 11:30 - 12:00 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5735/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5735/20261018_Koerner_Esnet_S_Discovery_Service__v1.pdf | video: https://www.youtube.com/watch?v=0bqb5VPSX5g
Marc Koerner – ESnet Building an application that collects an up-to-date network view can take time and effort, especially in addressing mundane issues such as differing protocol types, multiple information models, a lack of change notification, and related tasks such as augmenting discovered data with manually maintained information from other systems. Now imagine developing a handful of applications that need to perform the same functions but solve the problem independently of each other. The ESnet software team is developing a new event-driven, low-friction discovery service and document repository to address these common data discovery issues. This repository will provide a unified and coherent view of network configuration, including a raw and a normalized ontology-based representation of this discovered data (inventory, topology) while keeping interested applications in sync via message bus-driven notifications. In this talk, we will introduce the overall problem space, discuss our normalized ontology, and provide an overview of the current state of development. We will further discuss the advantages and give an outlook on future features and potential extensions.

### Routing Security Workshop - ARIN Deep Dive on RPKI
Session: Wednesday, October 21, 2026, 14:00 - 17:00 EDT, Biscayne Ballroom (Workshop)
page: https://nanog.org/events/nanog-98/content/5835/
Brad Gorman – American Registry for Internet Numbers (ARIN) Registration Required: https://nanog.org/registration/n98-arin-workshop/ Learn More: https://nanog.org/events/n98-arin-workshop/ Routing Security Workshop - ARIN Deep Dive on RPKI This hands-on workshop is limited to 50 attendees. Session sign-up is required prior to the workshop taking place. After 50 attendees register, a wait list will be created. Come with a laptop and be prepared to use the ARIN OT&E environment - learning as you go. Join us to learn how your organization can implement ARIN routing security services such as Resource Public Key Infrastructure (RPKI) and more. Whether you’re looking to shore up your foundational knowledge or wade into the currents of routing security, this expert-led session will provide you with the insights and skills you need. Program topics include routing security fundamentals, ARIN’s RPKI services, understanding relying party validators, and best practices for managing RPKI for your resources. A laptop will be required for this event.

### Building a Network Troubleshooting Agent: Architecture, Tools, Guardrails, and Lessons Learned
Session: Wednesday, October 21, 2026, 14:00 - 14:45 EDT, Trianon (Breakout)
page: https://nanog.org/events/nanog-98/content/5892/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5892/20261018_Muthuramakrishnan_Building_A_Network_v1.pdf | video: https://www.youtube.com/watch?v=eC-W7yGgXC4
Karthik Srinivas Muthuramakrishnan – Microsoft AI agents are rapidly moving beyond chat-based assistants toward systems that can reason over data, interact with tools, and automate operational workflows. But applying these capabilities to network troubleshooting introduces unique challenges: network state is distributed across multiple systems, telemetry may be incomplete or stale, and an incorrect action can have significant operational impact. This talk walks through the design and implementation of an AI agent for network troubleshooting, using a virtual router environment as a practical example. We will explore how to define the right problem for an agent, design its architecture, expose network capabilities through tools, and enable the agent to investigate routing and connectivity issues using real network state. The talk will also focus on the engineering considerations that become critical when deploying agents in network operations, including tool selection, context management, deterministic workflows versus LLM-driven reasoning, guardrails, permissions, human approval, failure handling, and evaluation.

### Beyond Speed: Measuring Last-Mile Broadband Consistency​
Session: Wednesday, October 21, 2026, 14:00 - 14:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5898/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5898/20261018_Paul_Beyond_Speed_Measuring_v1.pdf | video: https://www.youtube.com/watch?v=FDt6q9K1nKA
Udit Paul – Cisco ThousandEyes Advertised speed is a poor proxy for what subscribers actually experience. For example, a gigabit customer can pass a speed test and still see video calls freeze and pages stall. This talk presents a large-scale measurement study of broadband consistency and outages, taken directly from agents embedded in home-gateway CPE (a vantage point that avoids the Wi-Fi contention and device-side noise that distort user-run speed tests). The dataset spans 500M+ scheduled tests across U.S. markets and every major access technology (DOCSIS/HFC, fiber, DSL, fixed wireless, and LEO satellite). We use a simple, tier-independent reliability metric (each household's average download speed over its own 95th-percentile speed (Avg/P95)) and share findings operators can act on: DOCSIS consistency plateaus with higher tiers while fiber keeps improving; some providers' apparent low consistency is a legacy-DSL artifact, not a fiber limitation; off-peak measurement understates real volatility, with peak-evening consistency collapsing most on shared media; and LEO/Starlink trails terrestrial fiber and cable on consistency while competing on availability. We close with an outage case study where a geographically bounded fiber cut detected from CPE failure signatures and publicly corroborated showing how the same estate separates provider-wide, regional, and premises-level events. Methodology and sampling caveats are discussed throughout.

### BGP Role model: tracking the adoption of RFC 9234
Speakers: Bryton Herdes – Cloudflare, Iliana Xygkou – Georgia Institute of Technology
Session: Wednesday, October 21, 2026, 14:30 - 15:00 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5899/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5899/20261018_Herdes_Bgp_Role_Model__v1.pdf | video: https://www.youtube.com/watch?v=MCjUYIF2Axo
, Route leaks occur when a route is propagated along a path that violates the business relationships between networks. As a result, traffic follows an unintended set of links that is not suitable to handle its volume and often leads to performance degradation or even unreachability. RFC 9234 introduces Roles that assign business relationships to BGP sessions. Role configurations automatically attach the Only to Customer (OTC) attribute to routes, which help detect and prevent route leaks. In this presentation, we will cover the essentials of route leaks and their prevention through RFC 9234, and will explore the new solution’s adoption. We developed a unique method of tracking OTC-setting ASes based on our peering with thousands of ASes, and identified major ASes stripping the attribute and compromising its effectiveness, and provide guidelines to encourage adoption of RFC 9234.

### RIPE RIS - What We Collect, And What We Will Collect In The Future
Speakers: Ties de Kock – RIPE NCC
Session: Wednesday, October 21, 2026, 15:00 - 15:30 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5891/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5891/20261018_De_Kock_Ripe_Ris_-_v1.pdf | video: https://www.youtube.com/watch?v=5hH_yr76XsE
RIPE RIS has been collecting BGP data for more than 25 years. We maintain a long-term archive, and that comes with its own challenges: the volume only grows, and noisy or low-value data stays with us forever. In recent years, we have therefore been quite selective about accepting new peering sessions. We now want to reconsider that approach: collecting data from more peers, while keeping the long-term volume manageable. In this talk, I will recap the data RIS has been collecting and show some of the results --- and artifacts --- we see in the archive, including noisy peers, unstable sessions, and the growth of BGP attributes over time. I will then present ideas for a new peering policy that would allow us to be more open to new peers while keeping the resulting archival volume manageable. We get a lot of input from researchers about RIS, but we also want to hear from network operators: what data is useful to you, and what should we avoid collecting? We would particularly like feedback on these ideas before turning them into a new RIS peering policy, which we hope to publish later this year.

### AI Training Parallelism, From a Network Engineer's Point of View
Session: Wednesday, October 21, 2026, 16:00 - 16:45 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5868/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5868/20261018_Iazzag_Ai_Training_Parallelism__v1.pdf | video: https://www.youtube.com/watch?v=Xk2yoQhWPnI
Adel Iazzag – NVIDIA AI training runs across thousands of GPUs, and how you split the work decides what shows up on your network. This talk covers the main ways to split it : data, pipeline, tensor and mixture of experts. From a network engineer's point of view, not an ML one. For each one: what it does to the model, what it puts on the wire, and what we do about it. Rail optimization, one-to-one subscription, lossless fabrics, load balancing, incast, all-to-all, and where scale-up stops and scale-out starts. Then how a real job runs all of them at once on the same wires. The techniques come from the ML world. The network side comes from four years of building and running AI fabrics. If you build or run one, you will walk out knowing why your traffic looks the way it does, and how to design for it on purpose.

### Digital coherent optics - Deployment and operation
Speakers: Philip Bedard – Cisco
Session: Wednesday, October 21, 2026, 16:45 - 17:15 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5851/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5851/20261018_Bedard_Digital_Coherent_Optics_v1.pdf | video: https://www.youtube.com/watch?v=bRXl2WIcmZk
Pluggable digital coherent optics have led to major changes in how networks are deployed. The CapEx and OpEx cost savings of using these optics to interconnect routers and switches is well proven in some networks, but others are still hesitant to deploy them due to perceived complexity. This talk will walk through common real-world deployments of coherent optics, how they are managed from low-level optics control standards to end to end multi-layer automation, and common telemetry used to monitor deployment health.

### Botnet.cl - Live Botnet Monitoring and BGP Feed
Session: Wednesday, October 21, 2026, 17:15 - 17:25 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5955/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5955/20261021_Pe_a_Botnet_Cl_-_Live_v1.pdf | video: https://www.youtube.com/watch?v=VPDNg37Awm4
Rodrigo Peña – Bitred Group SpA AI has made it easier than ever to build things that once required large teams and resources. At Botnet.cl, we’re using it to discover emerging botnets, track their activity, and identify C2 infrastructure. In just two months, over 100 ISPs have subscribed to our BGP blackhole feed to help disrupt botnets on residential networks. We’ll share how we built it, what we’ve learned, and the results so far.

### Provisioning Your Network with AI, An introduction
Speakers: Bryan Fields
Session: Wednesday, October 21, 2026, 17:25 - 17:35 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5954/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5954/20261021_Fields_Provisioning_Your_Network_v1.pdf | video: https://www.youtube.com/watch?v=tAXt-L3-Y8Y
This is a short introduction to getting started managing your network with AI. I present what's worked for me as base to get anyone started managing their network using the same tools.

### RPKI's Misalignment and How to Fix It
Session: Wednesday, October 21, 2026, 17:35 - 17:45 EDT, Versailles (General Session)
page: https://nanog.org/events/nanog-98/content/5960/ | slides: https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5960/20261021_Kim_Rpki_S_Misalignment_And_v1.pdf | video: https://www.youtube.com/watch?v=skMzbxZnHbE
Younsoo Kim RPKI suffers from the misalignment between its goal and its operation, which manifests in the form of network overhead and potential security risks. To resolve this issue, I propose a new form of RPKI information distribution. I aim to raise awareness on RPKI's goal-operation misalignment and solicit community feedback on this proposal through this talk.

