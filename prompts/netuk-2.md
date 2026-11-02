>>> HOW TO RUN THIS <<<
This is the digest prompt for netuk-2. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/netuk-2.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/netuk-2.md
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

Below is the program for NetUK2 (The Brewery) (operator). Read it and produce a digest
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
conference: NetUK2 (The Brewery)
type: operator
source_url: https://indico.netuk.org/event/2/
generated: 2026-11-02
registry_key: netuk-2
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Workshop 2
### Introduction to Service Provider Networks
Speakers: Lister, Robert (LONAP)
page: https://indico.netuk.org/event/2/contributions/20/
**Introduction to Service Provider Networks** is a workshop for **anyone** who would like a basic understanding of networking, including: 1. Networking Principles: Protocols and the 7-layer model 2. Technical jargon explained 3. Cabling, Switching, Routing 4. Peering, Transit and the role of Internet Exchanges 5. Routing protocols 6. Where to learn more 7. A career in Service Provider Networks The workshop encourages participants to engage, ask questions, discuss and explore. It's *not* another "Death by PowerPoint".

## Main Session
### How the Internet routed around Cable Damage in the Baltic Sea
Speakers: Strachan, Alastair (RIPE NCC)
page: https://indico.netuk.org/event/2/contributions/25/
This presentation explores the impact of recent submarine cable outages in the Baltic Sea and how the Internet adapted to maintain connectivity. Using RIPE Atlas measurements, we analyze latency shifts, packet loss, and rerouting patterns following incidents affecting the BSC East-West and C-LION1 cables.

### How to wash your servers (handling extremes of weather as a WISP)
Speakers: Stockman, Oli (Fram Broadband Ltd/NGA Connect Ltd/Superhero Broadband)
page: https://indico.netuk.org/event/2/contributions/26/
A long format talk on handling extremes of weather when your network is mostly outdoors, covering the basics of wind, snow, heat and cold, and then focusing on the events of October 23 and Storm Babet and how we managed to keep our network running with our office and primary POP under 4ft of floodwater, and the lessons we learned form it

### Creating a sustainable supply chain in the network industry
Speakers: Nogradi, Nicol (Inter.link GmbH)
page: https://indico.netuk.org/event/2/contributions/27/
In response to increasing regulatory pressures, major telecommunications providers have begun to measure and report their carbon footprints. However, this initial step is just the beginning of a complex journey toward achieving sustainability. One of the most significant challenges these companies face is addressing Scope 3 emissions, which are generated by their supply chains and lie outside their direct control. In this presentation, I will discuss the current state of sustainability efforts within the telecom industry, with a particular focus on the intricacies of reducing Scope 3 emissions. Rather than offering quick fixes, I will explore practical approaches companies can consider, such as switching to more sustainable suppliers, collaborating closely with existing suppliers, and gradually introducing contractual clauses that emphasize sustainability. Attendees will gain a realistic understanding of the challenges involved and will be introduced to strategies that can help their organizations begin the process of reducing their supply chain's carbon footprint. This discussion aims to provide a balanced view, emphasizing that while these steps are crucial, they require time, commitment, and a willingness to engage in long-term efforts.

### Using Frameworks for self development
Speakers: Barnett, Andrew (BCS)
page: https://indico.netuk.org/event/2/contributions/39/
BCS, the Chartered Institute of IT talking about the use of career frameworks for self development

### NetUK2 Welcome - Day 1
Speakers: Pumford, Dave (PTX Technologies / NetUK)
page: https://indico.netuk.org/event/2/contributions/33/
Welcome to Day 1 of NetUK

### NetUK2 Welcome - Day 2
Speakers: Atkins, Megan (LINX)
page: https://indico.netuk.org/event/2/contributions/34/
Welcome to Day 2 of NetUK

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations
Speakers: Stein, Gerhard (Lead Research Engineer)
page: https://indico.netuk.org/event/2/contributions/21/
This presentation investigates the proximity to a low Signal-to-Noise Ratio (SNR) threshold that can still maintain a tolerable Bit Error Rate (BER) in 100G / 400G / 800G network links. Additionally, we account for factors such as temperature and cable length to predict the duration for which a reliable network connection can be sustained between transceivers. The analysis, based on data retrieved using a Flexbox, focuses on comparing the reliability of coherent (16QAM) and non-coherent (PAM4) transceivers, with a detailed discussion on the implications of these technologies on network performance.

### NetUK2 Close - Day 1
Speakers: Atkins, Megan (LINX)
page: https://indico.netuk.org/event/2/contributions/32/
Closing Day 1 of NetUK2

### Slash your cloud network costs with eBPF network monitoring
Speakers: Macias, Mario (Grafana Labs), Grcevski, Nikola (Grafana Labs)
page: https://indico.netuk.org/event/2/contributions/28/
According to a number of cloud vendor usage studies, cross-availability zone (AZ) data transfers regularly account for at least 25% of the public cloud users’ production cost. Cutting down these costs can affect your bottom line and your application affordability. All major cloud vendors provide daily aggregated cost metrics for the cross-zone network traffic, however oftentimes, these reports lack the granularity of information to tell which pods or workloads are responsible for the elevated cross-zone traffic. We will walk through our experiences with slashing network costs at Grafana by using eBPF network monitoring. We demonstrate how we leveraged eBPF to perform packet level traffic analysis in a manner that’s performant, requires zero-code changes and has extremely low overhead. We show how by enriching the low level network data with Kubernetes pod and node information, we can effectively identify cross-AZ traffic by using only OSS tools, while gaining detailed insights into the traffic patterns of each pod. We will show you how you can build your own solution for monitoring cross-AZ network traffic and identify savings in your cloud bills, regardless of the Kubernetes CNI you are using.

### Kubus Sponsor - Accelerating AI: The Critical Role of Networking in Data Center Performance
Speakers: Bonner, Paul (Kubus), Freeman, Rob (Juniper Networks)
page: https://indico.netuk.org/event/2/contributions/42/
Kubus will present in a sponsor slot.

### NetUK2 Close - Day 2
Speakers: Irving, Richard (LONAP)
page: https://indico.netuk.org/event/2/contributions/36/
Closing NetUK2 Event

### High Level Perspectives on Artificial Intelligence Data Centers
Speakers: Bennett, Geoff (Nokia)
page: https://indico.netuk.org/event/2/contributions/23/
AI represents one of the biggest inflection points in the modern world of technology. Hyperscalers and other companies see a once-in-a-lifetime opportunity to leverage AI to enhance existing business models and create new innovations. Today the only way we know of to enhance AI performance is to use more and more compute power to train Generative AI models. This in turn seems to require astonishing amounts of electrical power that places massive strain on existing electrical grids, uses huge volumes of fresh water, and may place any chance of stemming climate change at risk. In this tutorial I look at the trends for resource use by AI data centers – especially in terms of power demands. I look at the power requirements and discuss how these match up to potential power sources and the published hyperscaler strategies for power supplies. I conclude by examining both Enhanced Geothermal and Nuclear power options.

### Power Consumption Considerations in Metro Optical Networks
Speakers: Jones, Steve (Unicorn Farmer)
page: https://indico.netuk.org/event/2/contributions/22/
Draft Powerpoint presentation attached

### Some interesting stuff I found on IX LANs
Speakers: Cartwright-Cox, Ben (bgp.tools)
page: https://indico.netuk.org/event/2/contributions/43/
Internet exchanges are mostly Ethernet broadcast domains, and while most exchanges have a policy of what is allowed and is not allowed to appear on the broadcast/multicast domain of the exchanges, in practice something very different often happens. In this talk i will share with you some of the interesting things that bgp.tools has found amongst it's membership of 100 different peering exchanges, what the overall impact of this "bad" broadcast traffic is, and how exchanges may go about fixing such problems.

### NetUK Update
Speakers: Wenban-Smith, Nick (Nominet)
page: https://indico.netuk.org/event/2/contributions/35/
Update on the state of NetUK

## Lightning Talks
### PeeringDB: The LATAM Experience
Speakers: Peirano, Elisa (Lacnic)
page: https://indico.netuk.org/event/2/contributions/31/
How peeringdb is localised in LACNIC region. Going through why localisation is important and data about how much the LAC community is using peeringdb and how much peeringdb related activities are in the region.

### Detecting Non-Spoofed Traffic at ISP Ingress Points
Speakers: Gigis, Petros (University College London)
page: https://indico.netuk.org/event/2/contributions/37/
ISPs may notice that traffic from certain sources is entering their network at an unexpected location, but it is hard to know if this represents a problem or is just normal spoofed background noise. If such traffic is not spoofed, it would be useful to generate alerts, but alerting on background noise is not useful. We describe Penny, a robust, reliable, and practical traffic checker that helps ISPs distinguish between non-spoofed traffic aggregates arriving at the wrong ingress point and spoofed ones. The idea is simple: when new traffic arrives at unexpected routers, drop a few TCP packets. Non-spoofed packets ("bad packets") will be retransmitted, while spoofed packets ("worse packets") will not. However, building a robust test around this idea requires care. We address key challenges: minimising performance degradation for legitimate flows, handling external conditions like path changes or remote packet loss, and ensuring resilience against spoofers attempting to evade detection. In this presentation, we outline our vision for Penny as an open-source tool (openPenny) that ISPs can use not only to detect routing misconfigurations, recommend policy or commercial agreement adjustments, and safeguard against security threats such as BGP hijacks, but also to identify upstream/downstream packet loss, detect abruptly terminated TCP flows, and observe load-balancing behaviour.

### Sorry we messed up
Speakers: Funke, Stefan (Inter.link)
page: https://indico.netuk.org/event/2/contributions/24/
How we route-leaked everything to everyone due to a fun Arista bug. A post-mortem kind of story about us changing Arista RCF function names, resulting in a global route leak. The talk includes the history of why we intended to make a change, how we rollout configurations, why it resulted in an unexpected behavior and how it was fixed.

### RIPE92 Coming to You!
Speakers: Shannon, Linda (Hilco Streambank)
page: https://indico.netuk.org/event/2/contributions/38/
I would like to give a very short, approximately 2 minute, lightning talk to let the NetUK audience know of a relevant event coming to the United Kingdom next year. I was recently successful in my proposal for one of the upcoming RIPE Meetings to come to the United Kingdom with the UK being selected over other countries in a competitive process. RIPE92 in May 2026 is coming to Edinburgh, hosted by the Scottish office of Hilco Global as the "Local Host". RIPE is the Regional Internet Registry for Europe, Middle East and Central Asia. A RIPE Meeting is a five-day event where Internet Service Providers (ISPs), network operators and other interested parties from all over the world gather. RIPE Meetings are held in locations around RIPE's service region. It has been years since a RIPE Meeting has been held in the UK and we are very excited! Many NetUK attendees are members or may be interested parties. I hope this will be of benefit to the UK Internet community and hope to briefly let attendees know of the opportunity to attend or to be involved in other ways (speaking, sponsoring etc.).

### PeeringDB update
Speakers: Peirano, Elisa (Lacnic), Vegoda, Leo (PeeringDB)
page: https://indico.netuk.org/event/2/contributions/30/
PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions. We give regular updates at Internet related events to make people aware about this valuable resource and let our users know about the newest features and developments.

### Carbon-Aware Routing: Metrics and Challenges
Speakers: El Zahr, Sawsan (University of Oxford)
page: https://indico.netuk.org/event/2/contributions/29/
Every click, swipe and scroll leaves an impact on the environment. As we rely more on the Internet in many sectors and for many applications, the carbon footprint of the internet is rising, and it is unclear if we can achieve the net zero goals by 2050. Introducing carbon awareness to computer networks is one promising solution, yet with many challenges. The work presented in this talk is in the context of fixed wired networks, where accounting for their emissions is hard, requires changes to deployed equipment, and has contentious benefits. The talk has shed light on the benefits of carbon aware networks, by exploring a set of potential carbon-related metrics and their use to define link-cost in carbon-aware link-state routing algorithms. Using realistic network topologies, traffic patterns and grid carbon intensity, it identified useful metrics and limitations to carbon emissions reduction. Consequently, a new heuristic carbon-aware traffic engineering algorithm, CATE, was proposed. CATE takes advantage of carbon intensity and routers’ dynamic power consumption, combined with ports power down, to minimize carbon emissions. The presented results show that there is no silver bullet to significant carbon reductions, yet there are promising directions without changes to existing routers’ hardware. The talk uncovered some of the challenges that Internet Service Providers (ISPs) will need to face as we move towards net-zero networks.

### NetUK - Meet the Programme Committee
Speakers: Wilson, Dave (Glide / NetUK)
page: https://indico.netuk.org/event/2/contributions/41/
Meet the NetUK Programme Committee and learn about what we do.

## Sponsor-led Content
### Arista Sponsor - 10+ Years of EVPN
Speakers: Nichol, Alex (Arista)
page: https://indico.netuk.org/event/2/contributions/40/
- A short history of L2 and L3 VPNs and the drivers towards EVPN - Overview of EVPN and the market dynamics driving it - EVPN in the DC - Why VXLAN and not MPLS? - EVPN Multicast - EVPN Gateways

## Workshop 1
### BNG Blaster Hands-On Training
Speakers: Le Heux, Alex, Giese, Christian
page: https://indico.netuk.org/event/2/contributions/19/
This workshop is designed to provide participants with a practical introduction and best practices for using the [BNG Blaster][1] for testing. Each participant will be provided with a test environment that includes a pre-configured DUT (Device Under Test) for the workshop duration. There will be various exercises available in areas such as Access (PPPoE, L2TP, etc.) and Routing (ISIS, BGP, etc.), which participants can utilize. These exercises can be customized, or participants can develop their own tests. Participants with their own test environments are welcome to use them and will receive support from us in using these environments effectively. **Requirements:** 1. Participants must bring their own laptops to access the test environment via SSH. 2. Basic knowledge of networking concepts is recommended. **Note:** A brief introduction to the BNG Blaster will be provided, but it is recommended that attendees watch one of the previous talks on this topic beforehand ([DKNOG14][2] / [DENOG15][3]). [1]: https://rtbrick.github.io/bngblaster/ [2]: https://www.youtube.com/live/WdATdbaveRI?si=lgw1W-HckormViK9&t=13599 [3]: https://youtu.be/4rmwf6livyI

