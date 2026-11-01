>>> HOW TO RUN THIS <<<
This is the digest prompt for apricot-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/apricot-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/apricot-2026.md
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

Below is the program for APRICOT 2026 (Jakarta) (operator). Read it and produce a digest
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
conference: APRICOT 2026 (Jakarta)
type: operator
source_url: https://2026.apricot.net/
generated: 2026-11-01
registry_key: apricot-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Opening Ceremony and Plenary (11:30–13:00, Ballroom 2)
### Welcome Remarks
Speakers: Gavin Tweedie APNOG Board
No abstract published; title, speaker and materials only.

### Welcome Remarks
Speakers: Kenny Huang APNIC EC
No abstract published; title, speaker and materials only.

### Welcome Remarks
Speakers: Muhammad Arif Angga APJII
No abstract published; title, speaker and materials only.

### Keynote: The Agentic Shift: The Internet Industry Reimagined
Speakers: Mukhammad Andri Setiawan Universitas Islam Indonesia
The Agentic Shift explores how autonomous AI agents are reshaping the foundations of digital infrastructure, operations, and the future of technical work. From the fading era of manual configuration to the rise of intelligent, self‑directing systems, the presentation highlights a seismic industry transition — networks configured by agents, code generated without SQL, and operational models shifting from hands‑on engineering to high‑level coordination. The session also examines the challenges ahead, including bias, accuracy risks, and the emerging concept of AI sovereignty, and how nations and industries may increasingly be shaped by their AI capabilities. It introduces the new roles that will define the next decade: Agent Shepherds guiding swarms of autonomous agents, Sovereignty Architects shaping ethical and policy frameworks, and Compute Brokers managing the compute resources that power the agent economy.

### Keynote: Internet History Initiative: Preserving Our Collective Data Legacy
Speakers: Jim Cowie Internet History Initiative
slides: https://conference.apnic.net/61/assets/presentation-files/5bc8e851-0b96-4ab8-961b-21f08e97c3f3.pdf
Heraclitus famously observed that you cannot step into the same river twice, because it is ever-changing. In the same sense, historical Internet measurements are precious and irreplaceable. When future historians try to understand our times, will they still have the primary data sources to understand how the Internet grew, and how it became so central to the operation of global society? In this talk, we will present an overview of the Internet's measurement history from an archival perspective, showing how Internet operators are uniquely positioned to preserve technical datasets that are in danger of being lost. We will introduce a new initiative, the Internet Data Trust, that seeks to identify and preserve Internet measurement as collective digital heritage. And we will identify some of the specific gaps that need to be filled in order to preserve our understanding of the history of the Internet in the Asia-Pacific region in particular.

## APNIC Global Reports (14:30–15:30, Ballroom 1)
### ISOC Update
Speakers: Sally Wentworth Internet Society and Internet Society Foundation
slides: https://conference.apnic.net/61/assets/presentation-files/ee669a5f-167a-45c1-9fc9-2d76b2aa85b4.pdf
No abstract published; title, speaker and materials only.

### ICANN Update
Speakers: Athena Foo ICANN
slides: https://conference.apnic.net/61/assets/presentation-files/76bdb459-4841-494d-aa26-fa64db2d43f6.pdf
No abstract published; title, speaker and materials only.

### ASO AC Update
Speakers: Akinori Maemura JPNIC, NRO NC
slides: https://conference.apnic.net/61/assets/presentation-files/c366d28b-20f6-4daa-a56e-a37870ed4e50.pdf
No abstract published; title, speaker and materials only.

### ARIN Update
Speakers: John Sweeting ARIN
slides: https://conference.apnic.net/61/assets/presentation-files/398a4000-43b1-4c50-9505-1b76f1f63e22.pdf
No abstract published; title, speaker and materials only.

### LACNIC Update
Speakers: Carlos Martinez Cagnazzo LACNIC
slides: https://conference.apnic.net/61/assets/presentation-files/31984524-2273-4523-80b7-97704090db7d.pdf
No abstract published; title, speaker and materials only.

### RIPE Update
Speakers: Alastair Strachan RIPE
slides: https://conference.apnic.net/61/assets/presentation-files/225e861e-1340-4539-b492-bdc69cea6b11.pdf
No abstract published; title, speaker and materials only.

### AFRINIC Update
Speakers: Mukom Tamon AFRINIC
slides: https://conference.apnic.net/61/assets/presentation-files/c96fbe12-396d-407d-84c0-f69b399108db.pdf
No abstract published; title, speaker and materials only.

## APRICOT Plenary (14:30–16:30, Ballroom 2)
### IP Networking in Deep Space
Speakers: Marc Blanchet Viagenie
slides: https://conference.apnic.net/61/assets/presentation-files/e2575506-e364-46f1-8b4d-cfa746bfacdf.pdf
This presentation describes the use of the Internet Protocol stack to implement a network in deep space. The architecture is presented with a list of key needed adaptations: (1) temporary buffering of IP packets on forwarders with intermittent links, (2) configuration of the QUIC transport protocol with parameters related to the expected round-trip time and (3) configuration of application timeouts. The simulations described in this paper confirmed the suitability of the IP suite in deep space. Applications and network services are also discussed. Finally, benefits of using the Internet Protocol suite are described.

### What’s new at the IETF?
Speakers: Paresh Khatri Nokia
slides: https://conference.apnic.net/61/assets/presentation-files/2ea34790-9ba4-436d-8f0a-8fa643a6c731.pdf
The Internet Engineering Task Force (IETF) works on developing the voluntary standards that underpin the global Internet. These standards often influence operational practices, network architecture, and protocol evolution across the ecosystem. This session will highlight some key developments at the IETF, including new standards proposals, newly chartered working groups, and hot topics gaining traction within the IETF community. Special attention will be given to areas of direct relevance to network operators. Whether you’re tracking standards adoption, involved in deployments and operations, or just curious about emerging protocol trends, this talk will offer a concise, operator-focused view of what’s brewing at the IETF.

### BGP in 2025
Speakers: Geoffrey Huston APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/4dffcaec-ce12-43bf-b226-202193b34a99.pdf
The BGP routing environment provides a unique insight into the behaviour of the public Internet as a whole. BGP data relates to the size of memory needed to store the routing tables oin routers that operate in the Default-Free Zone, and its rates of growth ands stability can provide useful insights into the dynamics of network growth, in both IPv4 and IPv6. The dynamics of network convergence can also tell us how the BGP routing infrastructure is coping with scaling pressures. In this presentation we will dive ito metrics of BGP, comparing the data over the past two decades to the data relating to 2025.

### Tool, Teacher or Trickster? Exploring the many faces of AI
Speakers: Yolandi Cloete DE-CIX
slides: https://conference.apnic.net/61/assets/presentation-files/4d725203-d12a-43f9-86aa-8f5028728066.pdf
Is Artificial Intelligence a cheat, a powerful tool, or something more? This presentation delves into AI's evolving role, drawing parallels to past technological shifts like calculators and Excel. We’ll explore the undeniable benefits of AI, from boosting productivity to enabling groundbreaking innovation, while critically examining its risks, including data hallucinations and the proliferation of misinformation. From AI's foundational purpose to the cutting-edge applications of generative AI in complex industries like network interconnection, join me to understand how this transformative technology acts as a tool, teaches new possibilities, and at times, plays the trickster, demanding an open yet cautious mind.

## Network Performance (09:30–11:00, Ballroom 2)
### Debugging Routing & Forwarding Using RIPE Atlas
Speakers: Randy Bush Internet Initiative Japan
slides: https://conference.apnic.net/61/assets/presentation-files/457aa45c-b33e-4382-bff1-12e69861bfb2.pdf
Two real-world examples of using RIPE Atlas to diagnose routing/forwarding issues. And hints at other uses.

### To Space and Back: Integrating Next-Generation Terrestrial and Satellite Communication Networks
Speakers: Katarina Stefanović Telecom Serbia
slides: https://conference.apnic.net/61/assets/presentation-files/09204dc4-859e-4df7-ac9f-24a5e3bfe055.pdf
The rapid evolution of Low Earth Orbit (LEO) constellations, laser inter-satellite link (LISL), and non-terrestrial networks (NTN) is reshaping global connectivity and challenging long-established assumptions about latency, routing, and rural coverage. In this presentation, I explore how next-generation satellite systems can be integrated with terrestrial mobile networks to deliver resilient, wide-area, and performance-efficient communication services. Using real-world measurements collected through the RIPE Atlas platform, I compare end-to-end performance of Starlink LEO satellite connectivity with 4G/5G mobile networks across multiple European countries. Over a 7-day continuous measurement period, I analyzed long-haul RTT, hop-count behavior, intercontinental routing paths, and jitter distribution toward an APNIC-hosted target in Singapore. Despite longer physical paths, Starlink consistently demonstrated lower and more stable long-haul latency, enabled by backbone efficiency and evolving ISL-assisted routing, while mobile networks showed higher jitter and EPC-driven processing delays. The talk also provides a deep-dive into satellite architecture — from LEO mesh topology, ground stations, and LISL types (intra-plane, inter-plane, crossing-plane) to practical NTN–TN interoperability considerations defined in 3GPP TR 38.811. Real-world examples illustrate how geography, beam handovers, congestion, atmospheric conditions, and PoP presence influence user experience.

### Network Timing and GNSS-Independent Fact
Speakers: Kohei Suzuki SEIKO Solutions Inc.
slides: https://conference.apnic.net/61/assets/presentation-files/b6e09a51-6fee-4780-8cc1-6a136304c35e.pdf
As networks evolve toward distributed and cloud-native architectures, precise timing has become a silent enabler of digital infrastructure. However, much of today's synchronization still relies heavily on GNSS - a single external dependency that can be affected by jamming, spoofing, or regional disruptions. This session explores how network-based timing can strengthen resilience and autonomy by reducing or even eliminating satellite dependency. We'll look at practical approaches to achieving sub-microsecond accuracy over packet networks using PTP, enhanced boundary clocks, and advanced monitoring and verification tools. Drawing from real deployments across Asia's telecom and data center ecosystems, the talk highlights lessons learned, architectural trends, and key challenges in building GNSS-independent synchronization environments. Join this session to uncover the real facts behind "GNSS independence" - not as a theoretical goal, but as a practical pathway toward more secure, stable, and future-ready network timing.

### Campus Network Bandwidth and Performance Measurement Case Studies
Speakers: Mohamed Mansoor Zaheer Hussain The Open University of Sri Lanka
slides: https://conference.apnic.net/61/assets/presentation-files/3016d056-dafd-41a0-9a77-e682f09dc0dd.pdf
This presentation explores the practical challenges and solutions in accurately measuring campus network performance and Local Area Network (LAN) throughput using both manual and automated approaches. It features real-world case studies where unexplained slowdowns across campus buildings were traced to overlooked internal bandwidth, configuration, and latency issues. Three key tools are compared: iPerf3, a powerful manual benchmarking utility for detailed performance diagnostics; LibreSpeed, an automated, web-based solution for continuous throughput monitoring; and Smokeping, a latency visualization tool that helps detect micro-delays and instability within the LAN. The session demonstrates how combining these methods into a hybrid monitoring approach enhances end-to-end visibility across wired, fiber, and Wi-Fi segments, supports proactive capacity planning, and ensures efficient, data-driven network management.

## APRICOT Peering Forum 1 (11:30–13:00, Ballroom 2)
### Routing at Scale: Challenges in Indonesia’s Multi-IXP Ecosystem
Speakers: Michael Takeuchi Rapid Network
slides: https://conference.apnic.net/61/assets/presentation-files/0af02e7e-fb34-466f-8d08-0fd5d7d11643.pdf
Indonesia’s Internet ecosystem has evolved from a single Internet Exchange Point in 1997 to more than fifty IXPs nationwide, connecting over one thousand ISPs and thousands of non-ISP networks. While this growth strengthens domestic connectivity, it also creates complex routing challenges. Many ISPs now connect to multiple IXPs in Jakarta, leading to routing table bloat, suboptimal paths, inconsistent community tagging, and uneven visibility across networks. This presentation highlights real operational issues faced by Indonesian network operators, including congestion, asymmetric routing, and manual policy management caused by the absence of shared standards and unified monitoring systems. The discussion emphasises that multi-IXP routing problems are not only technical but also organisational. Achieving a stable and efficient Internet ecosystem in Indonesia requires improved communication, coordination, and transparency among ISPs, IXPs, and the broader networking community.

### Exploring the Blind Spot of Internet Exchange Point Route Servers
Speakers: Stefano Servillo The Department of Information Engineering, Electronic and  Telecommunications at the University of Rome “La Sapienza”, Italy
slides: https://conference.apnic.net/61/assets/presentation-files/a548a2ef-e856-451d-bfe1-fa8a5455f4cc.pdf
Internet Exchange Points (IXPs) are crucial components of today’s Internet ecosystem, enabling efficient interconnection among Autonomous Systems (ASes) and handling a substantial share of global Internet traffic. Their operation relies on Route Servers (RSes), which simplify public peering by allowing ASes to maintain a single Border Gateway Protocol (BGP) session rather than multiple bilateral ones. However, BGP's reliance on implicit trust exposes it to vulnerabilities that can be exploited to hijack or disrupt traffic. To mitigate these risks, IXPs commonly employ filtering mechanisms based on Internet Routing Registries (IRRs) and the Resource Public Key Infrastructure (RPKI). Current practices exhibit a critical blind spot: IRR-based filtering heavily relies on AS-SET objects, failing to explicitly bind IP prefixes to their legitimate AS, allowing misconfigurations or hijacks to evade detection. In this work, we formally define and analyse this vulnerability, demonstrating how it can be exploited to perform prefix hijacking via IXPs. We quantify its prevalence across a large set of IXPs. We further propose practical countermeasures to strengthen RS filtering and validate our findings using real-world data from the RSes of two major IXPs: AMS-IX and NAMEX.

### IX.br São Paulo: Migration to SRv6 EVPN
Speakers: Julio Sirota NIC.br
slides: https://conference.apnic.net/61/assets/presentation-files/6b3ca07b-f892-483d-b9f7-19dd727054a3.pdf
This presentation details the journey undertaken by IX.br in migrating the São Paulo network from LDP+VPLS technology to SRv6+EVPN. With the completion of the project, we present some results and points that are still pending.

### Peering Personals Introduction
Speakers: Achie Atienza Globe
slides: https://conference.apnic.net/61/assets/presentation-files/e125d15a-895b-4ff5-bb10-c89bb439d707.pdf
What Peering Personals are and why we do them are discussed in this short talk. And then the plan for the Peering Personals sessions at APRICOT 2026 will be shared so that participants are aware of the schedule for their one minute talk.

## Optics (11:30–13:00, MR1)
### Optics101 for non-Optical (IP) folks
Speakers: Tashi Phuntsho FLEXOPTIX
slides: https://conference.apnic.net/61/assets/presentation-files/3c70dfac-4ae8-4b0a-ac2a-8b47f886080f.pdf
This talk will recap fundamental optical concepts, make an attempt to help understand coherent pluggables and how it makes IPoDWDM possible.

### IPoDWDM in 2026
Speakers: Mark Tinka TransmissionCo
slides: https://conference.apnic.net/61/assets/presentation-files/8fce29f4-7b55-4fe0-8181-e2e2460da097.pdf
This paper talks about the current state of IPoDWDM, how, where and by whom it is being deployed, as well as its future.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Speakers: Thomas Weible FLEXOPTIX
slides: https://conference.apnic.net/61/assets/presentation-files/b68d1d9d-d598-4afa-b5c7-d1ba53997e9d.pdf
In the old days of traditional separation of IP and DWDM, there was no need for IP folks to care about much other than what they used on their routers/switches (while the transport team ran the DWDM infra). These past DWDM infra approaches for maximizing the data capacity per fiber pair went for running more and more DWDM channels with grid spacings as small as possible. This meant that grid spacings shrank from 200GHz to 100GHz and then 50GHz with some applications even going for 25GHz. Now in the age of IPoDWDM the bandwidth per channel keeps increasing, as complex modulation schemes come into favor over ON-OFF-Keying which has been the de facto standard so far. Those increased per channel bandwidths of 400Gbps, 800Gbps and now pushing into the 1.6Tbps realm demand for larger grids to accommodate the spectrum necessary to operate such "Superchannels". Especially the fact of coherent detection being "blind" to anything but its own wavelength has enabled interesting topologies that can omit filters altogether. Of course that comes at a cost of reduced flexibility. Which means, IP folks now will need to understand the nuances of how coherent detection works, need for larger filters for 800Gbps and higher, and how 400GHz filters (key word here being COTS) would future proof your network by not only allowing you to grow to 1.6Tbps, but also allow backwards compatibility for legacy services on 50GHz, etc.

## APNIC IPv6 Deployment (14:30–16:00, Ballroom 1)
### Project IPv6-First: A Case Study in Achieving an 80% Native IPv6 SOHO Network
Speakers: Terry Sweetser The Internet Engineering & Infrastructure Strategic Initiative
slides: https://conference.apnic.net/61/assets/presentation-files/a027c1fb-7a36-49f9-b083-ba4980f84c33.pdf
This 16-day (and then some) project improved IPv6 usage on a home office network from a good 67% to an amazing 95%. I showed that home networks can run mostly on IPv6 in 2025 without special transition tools or massive efforts. The remaining barriers are certain devices, some websites, and ISP limitations.

### Advances in IPv6 Aliased Prefix Detection and A new Aliased Prefix Detection Approach for IPv6 Scanning
Speakers: Ren Gang Tsinghua University
slides: https://conference.apnic.net/61/assets/presentation-files/fd228702-2e8c-40cc-a7fb-6261104f91c8.pdf
IPv6 scanning is the cornerstone of next generation cyberspace mapping and cybersecurity situational awareness technologies. Aliased Prefix is an entire IPv6 prefix that is configured to map to a single network interface. Aliased prefix detection is essential to prevent severely contaminated scan results and the massive waste of probing resources on these deceptive regions, ensuring more accurate and efficient IPv6 scanning. We introduce the advances in IPv6 Aliased Prefix Detection and a new passive enhanced multi level Aliased Prefix Detection approach that can achieve both high accuracy and low overhead for IPv6 Scanning.

### A Day in the Life of IPv6 Scanning
Speakers: Yoshinobu Matsuzaki IIJ
slides: https://conference.apnic.net/61/assets/presentation-files/9948cfbe-5c2b-49fa-a99c-8fdcedd709b2.pdf
It is well known that IPv4 public addresses are routinely scanned. But what about IPv6? Researchers have already studied on methods to efficiently scan based on hint information, and in fact, such scanning is taking place. In this presentation, I will share observations of these scans within end-user networks and insights.

### Generative Al for IPv6 Renumbering: Technical Barriers or Organisational Readiness?
Speakers: Mukhammad Andri Setiawan Universitas Islam Indonesia
slides: https://conference.apnic.net/61/assets/presentation-files/1227f887-05f5-47e1-a7e2-64edb3716ae3.pdf
In this presentation we will discuss the efficacy of generative AI in mitigating the substantial cognitive load and technical complexity associated with IPv6 renumbering. Through the evaluation of "Net AI Copilot," the study demonstrates that AI-assisted automation significantly enhances configuration efficiency and eliminates the psychological barriers that typically lead to task abandonment in manual workflows. However, the analysis reveals a critical "Design-Reality Gap," where organizational readiness lags behind technical capability due to insufficient training and resource alignment. The findings conclude that while AI effectively resolves technical impediments, successful implementation is ultimately contingent upon overcoming deep-seated organizational and psychological resistance.

### Overview of Xiong'an IPv6-only Deployment
Speakers: Dr Yang Guoliang Future Network Innovation Research Institute in Xiongan New Area
slides: https://conference.apnic.net/61/assets/presentation-files/127e5df8-0684-4b24-a16a-da890b109167.pdf
As a world-class new urban area committed to high-quality digital transformation, Xiong'an has pioneered IPv6-only deployment as a core practice for building the digital infrastructure of future cities. This presentation outlines the background, objectives and overall framework of this initiative, while sharing valuable experiences in infrastructure upgrading, application scenario integration and security system enhancement. To further advance IPv6 application innovation and global collaboration, the International Smart City Innovation Technology Competition will be held in Xiong'an in June 2026. Three IPv6-linked tracks are set up – Future Network, Intelligent Terminals, and Smart City Operation – inviting global teams, researchers and enterprises to showcase innovative achievements, share cutting-edge insights, and jointly explore the development paths of smart cities.

## APRICOT Peering Forum 2 (14:30–16:00, Ballroom 2)
### RouteViews Update
Speakers: Nina Bargisen RouteViews
slides: https://conference.apnic.net/61/assets/presentation-files/a74ff797-3c7d-4fd8-b778-370635feb8ae.pdf
RouteViews was initiated in 1995 at the University of Oregon to allow network operators see what their routing tables looked like from an external perspective. Over the years since, this community project has set up collectors in strategic locations around the world, allowing network operators a rich view of their routing announcements, and researchers a valuable resource for tracking the growth and variations in the global Internet infrastructure. This presentation introduces the new team behind RouteViews, and shares the new latest developments in the project, now operated on behalf of the global Internet community by the Network Startup Resource Center (NSRC). Some of the developments are the API, a new BMP processor, How to use the RouteViews system as a network operator and what we are working on for the future.

### bgproutes.io: A Next-Generation BGP Data Collection Platform
Speakers: Thomas Holterbach University of Strasbourg
slides: https://conference.apnic.net/61/assets/presentation-files/444b491c-a5c0-4e42-a6e0-bde2d7020557.pdf
Public BGP data provided by collection platforms such as RIPE RIS and RouteViews is essential to the Internet community. It enables operators and researchers to monitor the global routing system and underpins many widely used tools, including BGP looking glasses and hijack-detection systems. In this talk, we introduce bgproutes.io, a next-generation BGP data collection platform designed to improve routing visibility and usability. We explain how bgproutes.io differs from existing platforms, and how operators and researchers can access and explore the collected data through a public API and interactive analytical dashboards. A key focus of the talk is how bgproutes.io leverages recent BGP technologies to significantly increase data coverage. In particular, we describe how the platform uses the BGP Monitoring Protocol (BMP) to collect routing information beyond best-path announcements, enabling visibility into routes received from multiple peers and at different stages of the BGP decision process. We share operational experience showing how a small number of BMP sessions already translates into a large number of additional vantage points. We also present how bgproutes.io performs RPKI and ASPA validation on every collected route and exposes validation results to users. We argue that providing such validation data at scale can significantly help the community assess the deployment, effectiveness, and practical impact of these security mechanisms. Overall, this talk introduces not only a new BGP data collection platform, but also demonstrates how emerging technologies such as BMP and ASPA can be deployed and used in practice to improve and facilitate Internet routing monitoring. bgproutes.io is partially funded by the APNIC foundation.

### APIX Update
Speakers: Katsuyasu Toyama APIX
slides: https://conference.apnic.net/61/assets/presentation-files/d36f3e5d-3984-48be-bac3-caeff6ffd53d.pdf
The APIX is an association of Internet Exchanges in Asia Pacific region. It's been 15 years since established, and becomes over 40 member IXPs. The quick report is presented here, including recent updates and its history.

### Peering Personals Group 1
Speakers: Achie Atienza Globe
slides: https://conference.apnic.net/61/assets/presentation-files/ebe3c406-b8b7-4026-8317-0ab687f355f7.pdf
The first group of Peering Personals is introduced. (15:30-16:00) Abhinawa Networks, AiX, Biznet, Fibernet, Herza, IIX-APJII, JKT-IX, NTT, Lintasarta, Omadata Data Center, RAPIDNET, Akamai, AMS-IX, BBIX, BKNIX, Digital Realty, MC Digital Realty, Eastern, EWS-DSNi, Globe, HGC, Infinivan, JPNAP, M-Root DNS, Meta, MHK-IX, MMIX, Route Views, SGIX, SUNeVision, Tama Cable

## DNS (14:30–16:00, MR1)
### DNSSEC Implementation Journey
Speakers: Shaila Sharmin Prime Bank
slides: https://conference.apnic.net/61/assets/presentation-files/eb9c929d-8c92-4d9d-909c-4a1a2126f588.pdf
Recently DNSSEC was implemented for the .bd ccTLD and Prime Bank took the opportunity to adopt it as an early deployer. We are among the first organizations to sign a .com.bd second-level domain with DNSSEC successfully securing primebank.com.bd and myprime.com.bd.I have presented this recently on bdNOG20.

### DNS Resolvers and Nameservers
Speakers: Geoffrey Huston APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/f047807d-fd27-40e3-b43a-6d483807d5c8.pdf
The selection of which authoritative DNS server to use by a user's DNS resolver of choice greatly determines the user experience when accessing the Internet. In the past, some studies have looked at the behaviour of a set of implementations describing how they perform authoritative server selection and how they re-evaluate their choices in time. Other studies have leveraged the RIPE Atlas infrastructure to observe DNS resolution of a researcher-owned domain name from various points on the Internet. This presentation extends and complement these studies by using APNIC's distributed ad system to recruit several million end-users throughout the global Internet to observe the performance of the DNS server selection process by recursive resolvers. The presentation also profiles the DNS nameserver set for .ID domain names.

### Enabling Access to a Multilingual Internet - Deploying Domain Names and Email Addresses in Local Languages
Speakers: Champika Wijayatunga ICANN
slides: https://conference.apnic.net/61/assets/presentation-files/7b817134-2f24-446e-99fc-9afeda32aa3f.pdf
Technical standards now support domain names and email addresses in local languages. This brings new opportunities as well as promotes digital inclusion of internet users globally. This session shares the technical steps needed to host such domain names and email addresses, covering the entire journey of the registrant from registration to deployment.

### Making LocalRoot Default
Speakers: Warren Kumari Internet Standards, Google
slides: https://conference.apnic.net/61/assets/presentation-files/02170f63-eecf-43fa-898b-23d5e8b7cebd.pdf
RFC8806, also known as LocalRoot, provides a mechanism for resolvers to fetch, and cache a local copy of the IANA Root Zone. This has several benefits, including increased reliability, increased performance, improved privacy, and decreased or mitigation of the effect of some types of DoS attacks. This presentation is related to work in the IETF to expand the usage of LocalRoot (draft-wkumari-dnsop-localroot-bcp)

## APNIC Routing Security SIG (16:30–18:00, Ballroom 1)
### RPKI in INDONESIA
Speakers: Syarif Lumintarjo IDNIC
slides: https://conference.apnic.net/61/assets/presentation-files/76109e4c-dd37-4c23-a436-580458fa4193.pdf
No abstract published; title, speaker and materials only.

### ASPA in the RPKI Dashboard
Speakers: Tim Bruijnzeels RIPE
slides: https://conference.apnic.net/61/assets/presentation-files/77c06f7d-00f1-4201-a963-b31cbb9be3a6.pdf
No abstract published; title, speaker and materials only.

### RPKI APAC UPDATE
Speakers: Shane Hermoso APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/3aa4c555-8f11-4b9b-a157-151a59fdd1b1.pdf
The global RPKI adoption has increased significantly. In this session, we unfold the stats of RPKI ROA coverage in Asia-Pacific region and compare it with the global adoption rate. The talk also covers the ROV deployment status in the region and analyse the presence of any RPKI INVALID routes. Finally, we talk about the current RPKI ROA adoption and ROV status in Indonesia and end the session with some best practices of RPKI deployment by network operators.

### sidrops IETF UPDATE
Speakers: Tom Harrison APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/5a8f311a-b15d-4ed8-b8ae-e64be6d17a6a.pdf
The Secure Inter-Domain Routing Operations (sidrops) working group at IETF is responsible for documents and specifications that relate to RPKI.&nbsp; This presentation will summarise some recent topics from that working group, including trust anchor constraints, the Erik synchronisation protocol, and best current practices for operating RPKI publication servers and repositories.

### Can RPKI help mitigate social engineering attacks?
Speakers: Sanjaya APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/356755e3-72be-43db-844d-98627bf845c9.pdf
A recent routing hijack incident involving IP addresses in the Americas and an ASN from Asia demonstrated how social engineering can undermine Internet routing security. An attacker convinced a multinational ISP to provide transit for hijacked IP prefixes, prompting coordination among three Regional Internet Registries (RIRs) to resolve the issue. This presentation examines whether the Resource Public Key Infrastructure (RPKI) could mitigate such attacks.

### MESec: Minimal-Exposure AS-Path Verification against BGP Post-ROV Attacks
Speakers: Jiangou Zhan Tsinghua University
slides: https://conference.apnic.net/61/assets/presentation-files/d5b88c42-c664-46e1-a671-cf78b453e486.pdf
In this presentation, we introduce MESec , a framework designed for Minimal-Exposure AS-Path Verification. Unlike existing approaches that necessitate global visibility of local adjacencies, MESec decouples the validation of path correctness from the disclosure of network topology. By confining the visibility of relationship attestations strictly to the relevant verifying entities, MESec enables networks to detect and discard anomalous paths without broadcasting their peering strategies. Our evaluation demonstrates that MESec achieves a security posture comparable to standard ASPA in mitigating Post-ROV threats, while strictly adhering to the principle of minimal exposure. This work provides a pragmatic path toward secure inter-domain routing that aligns with the economic incentives of network operators.

## APRICOT Peering Forum 3 (16:30–18:00, Ballroom 2)
### Panel: Peering Beyond the Exchange: Cloud, Edge, and the New  Interconnection Reality
Speakers: Jose Santiago GuamExchange
slides: https://conference.apnic.net/61/assets/presentation-files/f430c5fe-a529-4386-b718-a1cc14f4f7bc.pdf
Peering is no longer confined to a single building or a traditional Internet Exchange. Cloud, edge deployments, and automation are reshaping how networks discover, connect, and exchange traffic. This panel brings together IXP operators, network providers, and infrastructure connectors to explore how these shifts are changing peering models across the Asia-Pacific region and beyond. Drawing on real-world deployments and operational experience, the discussion will examine how traffic flows are moving outward from centralised hubs toward distributed, software-driven interconnection.

### Peering Asia8.0
Speakers:  Kotaro Kan
slides: https://conference.apnic.net/61/assets/presentation-files/a7055e8c-3ddf-475c-a068-67af8f499f9a.pdf
No abstract published; title, speaker and materials only.

### Peering Personals Group 2
Speakers: Jose Santiago GuamExchange
slides: https://conference.apnic.net/61/assets/presentation-files/9be7c208-57ba-4aea-b7b8-6dcd00e51959.pdf
The second group of Peering Personals is introduced. (17:30-18:00) @Tokyo, BB Backbone Japan, Cloud Telecom, CommunityIX, Open Pipes, DECIX, Guam Exchange, HomeNOC, Hurricane Electric, Internet Association of Australia, JPIX, KINX, National Telecom, ThailandIX, Softbank, STT, Taiwan Digital Streaming Co, TCC Technology, Telstra, Zenlayer

## NOG Reports (16:30–18:00, MR1)
### AusNOG
Speakers: Mark Duffell Telstra
slides: https://conference.apnic.net/61/assets/presentation-files/93ff3918-eda4-42f4-8acb-cb14b5b66de4.pdf
No abstract published; title, speaker and materials only.

### bdNOG
Speakers: Shaila Sharmin Prime Bank
slides: https://conference.apnic.net/61/assets/presentation-files/aac12fa1-e13b-4775-b9a8-3845cbf31d79.pdf
No abstract published; title, speaker and materials only.

### BTNOG
Speakers: Karma Jamyang GovTech Bhutan
slides: https://conference.apnic.net/61/assets/presentation-files/611c14aa-7143-404c-b78b-e1b6748560d9.pdf
No abstract published; title, speaker and materials only.

### HKNOG
Speakers: Maggie Lee Equinix
slides: https://conference.apnic.net/61/assets/presentation-files/a56f4ad5-5aa9-42eb-8dca-c5ac605f98e6.pdf
No abstract published; title, speaker and materials only.

### IDNOG
Speakers: Parlindungan Marius IDNOG
slides: https://conference.apnic.net/61/assets/presentation-files/216a0aeb-d599-4037-83ba-9bfd50aad5d9.pdf
No abstract published; title, speaker and materials only.

### INNOG
Speakers: Pankaj Chaturvedi Lightstorm Telecom
slides: https://conference.apnic.net/61/assets/presentation-files/c3e4a29b-f77f-49ae-ac48-b5c87cc27000.pdf
No abstract published; title, speaker and materials only.

### JANOG
Speakers: Yoshinobu Matsuzaki IIJ
slides: https://conference.apnic.net/61/assets/presentation-files/e127ae7f-2e63-451e-b63b-30d6f0913946.pdf
No abstract published; title, speaker and materials only.

### KHNOG
Speakers: Som Sodana NOG
slides: https://conference.apnic.net/61/assets/presentation-files/3418c2ff-3609-41bb-884d-b269aab6d299.pdf
No abstract published; title, speaker and materials only.

### KRNOG
Speakers: Mike Hwang SK Broadband
slides: https://conference.apnic.net/61/assets/presentation-files/68a07dd7-7a99-452c-893e-2399d82a003d.pdf
No abstract published; title, speaker and materials only.

### LANOG
Speakers: Sotsay Sengvong National University of Laos
slides: https://conference.apnic.net/61/assets/presentation-files/1ba373b4-89ab-4200-8dd8-6b2dee11ff8c.pdf
No abstract published; title, speaker and materials only.

### LKNOG
Speakers: Mohamed Mansoor Zaheer Hussain The Open University of Sri Lanka
slides: https://conference.apnic.net/61/assets/presentation-files/a34bdf22-c7d8-47ce-bd55-388dfe71b2a7.pdf
No abstract published; title, speaker and materials only.

### MMNOG
Speakers: Thein Myint Khine Myanmar Internet Exchange (MMIX)
slides: https://conference.apnic.net/61/assets/presentation-files/e84cd34a-1030-43b1-8875-1487c961e89d.pdf
No abstract published; title, speaker and materials only.

### MNNOG
Speakers: Nyamkhand Buluukhuu Mobicom Group
slides: https://conference.apnic.net/61/assets/presentation-files/83a37caa-c273-4073-b63e-7761c2b6a46a.pdf
No abstract published; title, speaker and materials only.

### MYNOG
Speakers: Paul Ooi Cong Jen Takizo Solutions Sdn Bhd
slides: https://conference.apnic.net/61/assets/presentation-files/23dd11e9-e472-471a-a3d0-905c96c059cc.pdf
No abstract published; title, speaker and materials only.

### NPNOG
Speakers: Kijush Maharjan Worldlink
slides: https://conference.apnic.net/61/assets/presentation-files/49dab94e-cd71-44ec-8771-e34fe0a876f0.pdf
No abstract published; title, speaker and materials only.

### PhNOG
Speakers: Gly Apolonio PhNOG
slides: https://conference.apnic.net/61/assets/presentation-files/86724a65-7592-47f5-beba-e46858f15aff.pdf
No abstract published; title, speaker and materials only.

### SANOG
Speakers:  Rupesh Shrestha NOG
slides: https://conference.apnic.net/61/assets/presentation-files/abeb82b2-065d-4bc8-a047-5a56a4e45e78.pdf
No abstract published; title, speaker and materials only.

### SGNOG
Speakers: Tan Shao Yi SGNOG
No abstract published; title, speaker and materials only.

### TLNOG
Speakers: Jose Dias Timor Telecom
slides: https://conference.apnic.net/61/assets/presentation-files/c7214021-e80e-4f9b-9807-8810b6c5b75a.pdf
No abstract published; title, speaker and materials only.

### TWNOG
Speakers: Jack Kwok TWNOG
No abstract published; title, speaker and materials only.

## Network Operations (09:30–11:00, Ballroom 2)
### Designing a Mikrotik CGNAT solution that scales
Speakers: Matthew Enger Leaptel
slides: https://conference.apnic.net/61/assets/presentation-files/0a88e0c5-c389-44c7-bfd5-7e9e209de793.pdf
A step by step guide on how to build a cgnat solution using Mikrotik routers that scales, is highly resiliant and includes logging for law enforcment.

### Getting 1+ Tbps from an x86 server
Speakers: Branimir Rajtar 5x9 Networks
slides: https://conference.apnic.net/61/assets/presentation-files/c4acd498-1fd0-463a-bf65-16044fb86d99.pdf
This presentation explores the journey of achieving more than 1 Tbps throughput on a single x86 server by evolving a virtualized Broadband Network Gateway (vBNG). It walks through practical lessons learned while scaling from early multi-VM designs to a high-performance, single “Big VM” forwarder capable of extreme packet rates. The talk covers the role of SR-IOV and Intel DPDK, extensive hardware tuning, deep code-level optimizations, and major redesigns driven by CPU cache behavior and PCIe bottlenecks. Real-world performance results, including achieving 200 Mpps per CPU and scaling to 1.6 Tbps, highlight how systematic optimization, modern hardware, and iterative engineering can unlock massive throughput gains on commodity servers.

### Building an OOB network
Speakers: Phil Mawson Vocus
slides: https://conference.apnic.net/61/assets/presentation-files/dd8b382e-43af-4f2b-adc8-57320445ccc2.pdf
This talk will go over Vocus' journey in the last few years about building an OOB network (yet another MPLS network), why we chose the network and hardware design and lessons we have learnt along the way.This should give participants an idea of the important of building a seperate management network, how it can be done and concerns to watch out for.

## Segment Routing a tutorial: Part 1 (09:30–11:00, MR1)
### Segment Routing: a tutorial
Speakers: Paresh Khatri Nokia
slides: https://conference.apnic.net/61/assets/presentation-files/e7a78e10-463e-40f6-9a51-bb521e227d0f.pdf | video: https://youtube.com/live/Ws9v6yopfXg?feature=share
No abstract published; title, speaker and materials only.

## APNIC Open Policy Meeting (11:30–13:00, Ballroom 1)
### Welcome Remarks
Speakers: Bikram Shrestha Nepal Internet Foundation
No abstract published; title, speaker and materials only.

### SIG Administration
Speakers: Ching-Heng Ku TWNIC
No abstract published; title, speaker and materials only.

### SIG Administration
Speakers: Shaila Sharmin Prime Bank
No abstract published; title, speaker and materials only.

### SIG Administration
Speakers: Dave Phelan APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/608d61a2-5cde-4420-b3c6-48e7cbe8fc6c.pdf
No abstract published; title, speaker and materials only.

### Policy Implementation report
Speakers: Dave Phelan APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/13ea72e6-9d70-4e27-bbb8-684810c420b9.pdf
No abstract published; title, speaker and materials only.

### Resource Change Logs
Speakers: Tom Harrison APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/536d7410-4bb8-4ea4-8f2b-7c1fb93899a9.pdf
No abstract published; title, speaker and materials only.

### Prop-164
Speakers: Christopher Hawker
slides: https://conference.apnic.net/61/assets/presentation-files/c2127a05-a91a-4924-b36d-79836ec34e1e.pdf
No abstract published; title, speaker and materials only.

### Prop-168
Speakers: Christopher Hawker
slides: https://conference.apnic.net/61/assets/presentation-files/ae180f66-3201-43a7-869d-bdc0c2e48695.pdf
No abstract published; title, speaker and materials only.

### Secretariat Impact Assessment prop-168
Speakers: Dave Phelan APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/88346ae5-f38b-4a22-b9fe-6e75c5199ab2.pdf
No abstract published; title, speaker and materials only.

## Network Management (11:30–13:00, Ballroom 2)
### What Your DNS Logs Say About CDN Efficiency
Speakers: Abu Sufian ADN Telecom Limited
slides: https://conference.apnic.net/61/assets/presentation-files/8eaca6c2-1c46-4642-99ca-cc75ecb55d66.pdf
Most ISPs in Bangladesh rely on public DNS resolvers like Google or Cloudflare. This means operators have almost no insight into where their users’ CDN traffic is really going — which cache nodes serve them, and whether those are on-net or global. This session shares a practical, low-cost approach using PowerDNS Recursor, ClickHouse, and Grafana to build local DNS visibility. We used live resolver logs to classify CDN answers (Udoy, Vendor, Global) for Facebook (FNA) and Google (GGC). Attendees will learn how to instrument DNS within their own networks, interpret query-to-CDN mapping, and use the data for routing, cache deployment, and QoE improvement.

### Grafana-Powered Traffic Dashboard for Customer Networks
Speakers: Munkhtulga Bayarkhuu Skymedia
slides: https://conference.apnic.net/61/assets/presentation-files/24ceeabd-73f3-4bfc-bd66-6327a178ccbf.pdf
This presentation explains how we built a network bandwidth monitoring solution for our enterprise users using open-source tools. The main goal was to clearly understand overall traffic usage and see how much of the bandwidth is used for local versus internet traffic. We used LibreNMS to monitor device and interface performance through SNMP, and Akvorado to collect and analyse sFlow/NetFlow traffic data from our routers.By visualising everything through a single Grafana dashboard, the solution removes the need to switch between multiple monitoring systems, making it easier to use while improving accuracy and data security.

### Deployment automation using SoT tool
Speakers: Ulsbold Enkhtaivan Mobicom
slides: https://conference.apnic.net/61/assets/presentation-files/55c0c1b7-cac2-429c-9939-56292845c6de.pdf
The paper introduces ZTP like automation using SoT tool(Netbox). Due to lack of out of band network accessibility of remote site we developed own version of automate config to new device. It was helped to faster a network rollout process and tried less human interaction. Also integrated monitoring and configuring device using python.

### The Evolution of Network Configuration Management
Speakers: Tim Raphael Nokia
slides: https://conference.apnic.net/61/assets/presentation-files/67aa5ba5-737d-4c60-b2c1-a3d36af521b2.pdf
Network configuration was once a hand-crafted task when protocols were relatively simple and topologies infrequently changed. Now we're building massive, highly resilient and operationally complex networks that demand consistency at scale. During this talk we’ll take a journey through the evolution of configuration technologies and what we learned along the way. I'll cover how we started to solve these problems and how we should be configuring networks into the future. We’ll be discussing scripting, imperative operations, workflows, playbooks, APIs, RPCs, declarative models, and intent-driven operations.

## Segment Routing a tutorial: Part 2 (11:30–13:00, MR1)
## APNIC NIR SIG (14:30–16:00, Ballroom 1)
### TWNIC Update
Speakers: Tim Wang  TWNIC
slides: https://conference.apnic.net/61/assets/presentation-files/26ff2588-3d47-4dd8-8f55-52a40ca3959a.pdf
No abstract published; title, speaker and materials only.

### JPNIC Update
Speakers: Koki Nakagawa JPNIC
slides: https://conference.apnic.net/61/assets/presentation-files/1cb92684-a879-418a-baf4-009e313d7140.pdf
No abstract published; title, speaker and materials only.

### CNNIC Update
Speakers: Zhen Yu CNNIC
slides: https://conference.apnic.net/61/assets/presentation-files/385bb449-fde3-40d8-8832-2013e58ea879.pdf
No abstract published; title, speaker and materials only.

### VNNIC Update
Speakers: Oanh Nguyen VNNIC
slides: https://conference.apnic.net/61/assets/presentation-files/4832663f-a405-445f-b6af-804ad9fdf839.pdf
No abstract published; title, speaker and materials only.

### APJII/IDNIC Update
Speakers: Syarif Lumintarjo IDNIC
slides: https://conference.apnic.net/61/assets/presentation-files/761fb3b3-4514-4461-96e1-090b5eab8c9c.pdf
No abstract published; title, speaker and materials only.

### NIXI Update
Speakers: Nittin Prakash NIXI
slides: https://conference.apnic.net/61/assets/presentation-files/1d7e7147-fc82-4d2d-8b21-9f4266a95887.pdf
No abstract published; title, speaker and materials only.

### KISA/KRNIC Update
Speakers: Han Sang Lee KISA
slides: https://conference.apnic.net/61/assets/presentation-files/9031893c-eeb6-425a-be36-3daf5f0a11cf.pdf
No abstract published; title, speaker and materials only.

### Using APNIC’s Resource Explorer (REx) to Visualise NIR-Specific Statistics
Speakers: Rafael Cintra APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/e6646ad2-1fcf-422a-962e-235d258c8618.pdf
In this talk, we will demonstrate how to use APNIC’s Resource Explorer (REx) to: Visualise resource delegation statistics Review current delegations for specific National Internet Registries (NIRs) Explore Internet measurement data for selected economies The session will include a live demo showcasing practical use cases and insights that REx can provide.

### NIR SIG Charter Review
Speakers: Oanh Nguyen VNNIC
slides: https://conference.apnic.net/61/assets/presentation-files/1cafcb25-b792-4a3d-a62f-c1a9d252f582.pdf
The NIR SIG Chairs will provide an overview of the proposed updates to the NIR SIG Charter, followed by an open mic discussion. Attendees are invited to share their views on the proposed changes, including the broader inclusion of NIR members alongside APNIC and the NIRs. Ideas on how to better involve NIR members in the SIG, and how the NIR SIG can be improved in the future, both during APNIC meetings and through other engagement approaches, will be discussed during the open mic session.

## Lightning Talks (14:30–16:00, Ballroom 2)
### Using open data and tools to explore the Indonesian market
Speakers: Jon Brewer Telco2 Limited
slides: https://conference.apnic.net/61/assets/presentation-files/e9063b49-eda8-4663-a7d9-51afd2841ebd.pdf
No abstract published; title, speaker and materials only.

### Engaging Future Network Engineers Through Simulation
Speakers: Yolandi Cloete DE-CIX
slides: https://conference.apnic.net/61/assets/presentation-files/aa17ca44-18e2-40df-9b76-49b9d87ef9c5.pdf
No abstract published; title, speaker and materials only.

### A Comparative Analysis of the IRR Landscape
Speakers: Christoph Dietzel
slides: https://conference.apnic.net/61/assets/presentation-files/99288224-ed0e-4e8d-8528-5455d974ebea.pdf
No abstract published; title, speaker and materials only.

### Equipping students with BGP Skills
Speakers: Achmad Husni Thamrin
slides: https://conference.apnic.net/61/assets/presentation-files/ef91bcef-37e7-4158-8e5b-84f60c42aac2.pdf
No abstract published; title, speaker and materials only.

### Best Current Practice for ROA Issuance Restrictions
Speakers: Yingfei Sun CNNIC
slides: https://conference.apnic.net/61/assets/presentation-files/779a3a04-2b7f-4d20-81e5-9aaf076d5bff.pdf
No abstract published; title, speaker and materials only.

### Authenticating networks with RPKI RSC
Speakers: Arnold Nipper DE-CIX
slides: https://conference.apnic.net/61/assets/presentation-files/3cdf15ce-8dae-491a-a93f-cfda8a601638.pdf
No abstract published; title, speaker and materials only.

### Botnet Tracking with Honeypots
Speakers: Adli Wahid APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/1ef1842f-0d38-466c-b034-b22cacaa63ac.pdf
No abstract published; title, speaker and materials only.

### Challenge for ISPs & Telecoms - IP Blacklisted
Speakers: Samarjit Biswas
slides: https://conference.apnic.net/61/assets/presentation-files/ebb15309-c9e4-4775-a7e4-e92f50aef141.pdf
No abstract published; title, speaker and materials only.

### KSK TCR
Speakers: George Michaelson
slides: https://conference.apnic.net/61/assets/presentation-files/f517e8b2-9b3c-4218-986e-73720704d315.pdf
No abstract published; title, speaker and materials only.

## Security (14:30–16:00, MR1)
### From Compromise to Resilience: A Practical Journey of Security Transformation
Speakers: Mahedi Hasan University of Dhaka
This presentation shares a real-world case study of how I transformed University of Dhaka's security posture following a cyberattack in late 2024. I demonstrate how academic institutions can build enterprise-grade resilience using open-source technologies (CrowdSec WAF, Wazuh SIEM, OPNsense, Proxmox) without massive budgets. Key topics include: incident response and recovery, implementing behavior-based WAF with community threat intelligence, SIEM integration for unified monitoring, network segmentation strategies, and cost-effective security architecture. The session covers both technical implementation details and organizational lessons learned, making it valuable for institutions facing similar budget constraints. Attendees will learn practical approaches to security transformation, including specific tool configurations, integration patterns, and how to leverage open-source solutions for comprehensive protection. I emphasize that effective security requires strategic thinking and community collaboration rather than expensive commercial solutions.

### DDoS in Indonesia - Has it improved
Speakers: Dave Phelan APNIC
An update on a deck I presented at IDNOG9 in 2024. Looking at the DDoS sources and whether things have improved or not

### Tales from Incident Responses
Speakers: Abu Baker YOTTABYTE PVT LTD
I wanted to deliver this talk to engineers and sysadmins of the community to show that incident response is not magic as well as what impact AI has on infections. Lastly discussing how correctly architecting the environment impacts attack chain. The purpose of this talk is share my experience with IR cases from vulnerability and TTP perspective.

## Closing Plenary (16:30–18:00, Ballroom 2)
### Keynote: IPv6 in Enterprise Networks
Speakers: Jen Linkova Google
slides: https://conference.apnic.net/61/assets/presentation-files/07905055-3f90-48af-ac5e-097b9ff91621.pdf
This talk explores the practical realities of deploying IPv6 and transitioning away from IPv4 in enterprise networks. While we will cover the essential underlying concepts, the primary focus is on the "why, how, and what to expect" based on real-world success stories. We will examine the current state of transition technologies and how modern operating systems perform in the absence of IPv4. The session aims to provide a broader perspective on the implementation landscape, supported by actionable deployment guidance and resources for further reading.

### Conference Network Report
Speakers: Yoshinobu Matsuzaki IIJ
slides: https://conference.apnic.net/61/assets/presentation-files/c2e37815-ae9e-4a8e-940f-c61ac8672a3c.pdf
No abstract published; title, speaker and materials only.

### Closing Remarks
Speakers: Syarif Lumintarjo IDNIC-APJII
No abstract published; title, speaker and materials only.

### Closing Remarks
Speakers: Jia Rong Low APNIC
No abstract published; title, speaker and materials only.

### Vote of Thanks
Speakers: Philip Smith APNOG
No abstract published; title, speaker and materials only.

### Welcome to APRICOT 2027
Speakers: Philip Smith APNOG
No abstract published; title, speaker and materials only.

## APNIC AGM 1 (09:30–11:00, Ballroom 1)
### Welcome Remarks and Introductions
Speakers: Kenny Huang APNIC EC
No abstract published; title, speaker and materials only.

### APNIC EC Election Procedures and By-laws Reform Voting
Speakers: Jeremy Harrison APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/b4d2acbe-8394-4337-ae39-d9b61c1a0fba.pdf
No abstract published; title, speaker and materials only.

### Introduction of EC Election Nominees
Speakers: Wahyoe Prawoto
No abstract published; title, speaker and materials only.

### APNIC EC Report
Speakers: Kenny Huang APNIC EC
slides: https://conference.apnic.net/61/assets/presentation-files/a1cbb1c3-5998-4b7c-b608-314ff103ea40.pdf
No abstract published; title, speaker and materials only.

### APNIC Treasurer Report
Speakers: Yoshinobu Matsuzaki APNIC EC
slides: https://conference.apnic.net/61/assets/presentation-files/0f788c63-d559-468d-833d-526ad8531117.pdf
No abstract published; title, speaker and materials only.

### APNIC Annual Report 2025
Speakers: Tony Smith APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/eb9dd8c0-51e0-4af5-8549-476032953ad0.pdf
No abstract published; title, speaker and materials only.

## APNIC AGM 2 (11:30–13:00, Ballroom 1)
### DG Report and 2026 Plan
Speakers: Jia Rong Low APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/fd2b68e2-c871-4985-8d11-74ff8e330cf7.pdf
No abstract published; title, speaker and materials only.

### APNIC Foundation Update
Speakers: Raj Singh APNIC Foundation
slides: https://conference.apnic.net/61/assets/presentation-files/a6265677-66a7-4bee-acbc-dfec78669e0b.pdf
No abstract published; title, speaker and materials only.

### ASO AC Report
Speakers: Nicole T.I Chan NRO NC
slides: https://conference.apnic.net/61/assets/presentation-files/11b60a43-c4dd-4af0-b051-753f1b447f11.pdf
No abstract published; title, speaker and materials only.

### Routing Security SIG Report
Speakers: Terry Sweetser The Internet Engineering & Infrastructure Strategic Initiative
slides: https://conference.apnic.net/61/assets/presentation-files/ba75b9f2-ee66-4c09-8bcc-934ffca1366a.pdf
No abstract published; title, speaker and materials only.

### Cooperation SIG Report
Speakers: Joy Chan TWNIC
slides: https://conference.apnic.net/61/assets/presentation-files/651f6367-2d2a-47b2-aecc-92d8505140fd.pdf
No abstract published; title, speaker and materials only.

### Reminder: APNIC EC and By-laws Reform Voting
Speakers: Melody Bendindang APNIC
No abstract published; title, speaker and materials only.

## APNIC AGM 3 (15:00–16:00, Ballroom 1)
### Reminder: APNIC EC and By-laws Reform Voting Close
Speakers: Melody Bendindang APNIC
No abstract published; title, speaker and materials only.

### NIR SIG Report
Speakers: Oanh Nguyen VNNIC
slides: https://conference.apnic.net/61/assets/presentation-files/10774b74-2c2d-4cbf-871d-eadf1c97aea2.pdf
No abstract published; title, speaker and materials only.

### Policy SIG Report and Consensus
Speakers: Bikram Shrestha Nepal Internet Foundation
slides: https://conference.apnic.net/61/assets/presentation-files/21da744a-6440-496f-ac4a-11ef11cea40a.pdf
No abstract published; title, speaker and materials only.

### Joint SIGs Report - SIGs Guidelines Review
Speakers: Terry Sweetser Routing Security SIG
slides: https://conference.apnic.net/61/assets/presentation-files/81dffc37-37dc-4506-808f-0b35b124a65d.pdf
No abstract published; title, speaker and materials only.

### Invitation to APNIC 62
Speakers: Devesh Tyagi NIXI
No abstract published; title, speaker and materials only.

### APNIC EC Election Results
Speakers: Wahyoe Prawoto
No abstract published; title, speaker and materials only.

### Official close of AGM
Speakers: Kenny Huang APNIC EC
No abstract published; title, speaker and materials only.

### Vote of Thanks
Speakers: Jia Rong Low APNIC
slides: https://conference.apnic.net/61/assets/presentation-files/5f4ba841-6282-4d5c-84f4-540fef309571.pdf
No abstract published; title, speaker and materials only.

