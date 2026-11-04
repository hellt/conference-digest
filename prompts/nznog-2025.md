>>> HOW TO RUN THIS <<<
This is the digest prompt for nznog-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/nznog-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/nznog-2025.md
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

Below is the program for NZNOG 2025 (operator). Read it and produce a digest
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
conference: NZNOG 2025
type: operator
source_url: https://www.nznog.org/conferences/nznog-2025/talks.html
generated: 2026-11-04
registry_key: nznog-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Accepted talks
### Communications Resilience
Speakers: Jon Brewer (Telco2)
This talk explores how infrastructure mapping can be used to identify vulnerabilities, assess risks, and enhance the resilience of telecommunications networks. We look at data collection and maintenance strategies, mapping dependencies such as shared power transformers and single-road access routes, and visualising hazards including fault lines, liquefaction zones, and landslide-prone areas.

### DNS Resolvers and Nameservers in New Zealand
Speakers: Geoff Huston (APNIC)
The selection of which authoritative DNS server to use by a user’s DNS resolver of choice greatly determines the user experience when accessing the Internet.
In the past some studies have looked at the behaviour of a set of implementations describing how they perform authoritative server selection and how they re-evaluate their choices in time.
Other studies have leveraged the RIPE Atlas infrastructure to observe DNS resolution of a researcher-owned domain name from various points on the Internet.
We extend and complement these studies by using APNIC’s distributed ad system to recruit several million end-users throughout the global Internet to observer the resolution selection process, and then we look at a couple of domain name sets to see how they have been provisioned against the noted reseover behaviours. The first name set we use of the top level domain name set in the root zone, and the second set is the .nz domains listed in the Tranco top 1M dpomain name set.

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations
Speakers: Thomas Weible (Flexoptix)
This presentation investigates the proximity to a low Signal-to-Noise Ratio (SNR) threshold that can still maintain a tolerable Bit Error Rate (BER) in 100G / 400G / 800G network links. Additionally, we account for factors such as temperature and cable length to predict the duration for which a reliable network connection can be sustained between transceivers. The analysis, based on data retrieved using a Flexbox, focuses on comparing the reliability of coherent (16QAM) and non-coherent (PAM4) transceivers, with a detailed discussion on the implications of these technologies on network performance.

### We’re not in Kansas anymore: my experiences with IP geolocation
Speakers: Shane Alcock (Alcock Network Intelligence, IODA)
Problems with IP geolocation are nothing new to the operator community; customers who have been incorrectly geo-blocked from content are a regular source of complaints. But what is it like to be a consumer of IP geolocation data? Are we able to get useful insights from the data? What are the issues that make this data difficult to work with? Why is it so damn hard to get IP geolocation right?
In this talk, I’ll elaborate on my experiences with IP geolocation data within the IODA (Internet Outage Detection and Analysis) system, where we try to attribute observed Internet outages to the geographic regions where they occur. I hope to both enlighten the NZNOG audience about how IP geolocation datasets are derived and document some of the many gotchas that I have encountered along the way, which may be useful to anyone else considering using geolocation data in the future.

### The Weakest Link in the Modern Cyber Threat Landscape
Speakers: Anna Lezhikova (CyberFern)
Cyber threats are scarier than ever—hackers are getting creative, and it feels like we’re one click away from disaster. But here’s the truth: the biggest threat is often the person sitting right next to you. Whether it’s falling for a phishing email, leaving passwords on sticky notes, or just not updating that software—humans are usually the weak link in the cyber chain. In this session, we’ll take a closer look at how our habits and behaviors contribute to the rise in cyber breaches, both personally and in business. It’s not all doom and gloom, though! The solution lies in cultivating a security-first mindset and fostering a culture where security is everyone’s responsibility. After all, securing our digital lives isn’t just about tech—it’s about us. Let’s explore how we can all play a part in defending against the growing wave of cyber threats.

### Passive Optical Networking
Speakers: Daniel Hutchins (Ciena)
Passive Optical Networking (PON) has become the de-facto method to deliver high speed broadband in most markets globally.
In this session we’ll recap the basics of PON, where the industry currently stands in terms of standards and deployments, and discuss how PON continues to evolve beyond 10G to enable higher speeds and support ever increasing traffic demands.

### IP Quirks and Features
Speakers: Mark Smith
The Internet Protocols have evolved over many years since the original “A Protocol for Packet Network Intercommunication” paper in May 1974, by Vint Cerf and Bob Kahn.
In my time with IP, since the early 1990s, having used it, deployed it and taught it, I’ve found knowing some of the history of IP’s features and evolution both interesting and quite useful to know when operating IP networks. It can help explain why some things are far more complex than you would think they should have ever been designed to be.
I was also involved in networking in the 1990s multi-protocol era when other layer 3 protocols such as Novell’s IPX and Apple’s Appletalk were widely deployed.
I’ve been involved in the two main IPv6 working groups in the IETF since 2002. Knowing about the design and evolution of IP and other 1980s/90s protocols like Novell’s IPX have helped me better understand IPv6’s design goals and also how it was designed to be deployed.
In this presentation I’ll cover these sorts of past IP and similar protocol evolutions and features, in a broader context of and related to IPv6. Some examples of the topics - Why did it take 825 RFCs before ARP was developed? Why did IPv4 addressing become so complicated? How come IPv6 addresses became 128 bits when its ancestor, the Simple Internet Protocol, was 64 bits, and that was considered big enough?

### Resilient and Inclusive Networks: Ensuring communication for all in all times
Speakers: Craig Young, Vivian Chandra (TUANZ)
In an increasingly interconnected world, networks are essential for our daily lives. We rely on them for everything from basic communication to essential services such as healthcare, education, and emergency response. When disaster strikes, resilient networks become even more critical. They enable us to stay in touch with loved ones, access vital information, and coordinate relief efforts.
It is not enough for networks to be resilient; they must also be inclusive. This means that they must be accessible and usable by all members of society, regardless of their background, abilities, or location.
This presentation will explore the challenges that some communities and populations face in accessing and using networks. It will also discuss the steps that network operators can take to make their networks more inclusive.

### Implementing Precision Timing / Sync as a Service in a Telecommunications Network
Speakers: Phil Carlisle (Chorus)
The availability of an accurate clock source is becoming critical to a many industries.
These include Mobile Telecommunication networks, Power networks, financial
institutions among others.
To date, most applications use a GNSS (GPS + other navigation systems) receiver to
provide an accurate source of frequency and or time. There are two potential issues with
this approach: cost and vulnerability.
Deploying GNSS clocks can involve the installation of a clock device as well as an
antenna and associated cabling. This can be expensive – especially when deployed on a
large scale such as with mobile or power networks. GNSS Clocks are vulnerable to
jamming and spoofing, Space weather and other threats.
Another approach, to provide access to an accurate clock source, is via a robust
terrestrial network using IEEE1588v2 and SyncE.
Chorus has been investigating this concept as well as conducting laboratory and customer trials. This presentation looks at the implications of rolling out precision timing across the Chorus Network.

### DNSSEC for .nz: post-incident recovery and improvement (or, how to see the train coming down the tunnel next time. For sure.)
Speakers: Paul Radford (InternetNZ)
The .nz DNSSEC incident brought home how little observability we really had of our .nz zone output. We had checks that proved every zone file was internally consistent, but none of those checks took into account how caching recursive DNS servers affected queries and DNSSEC validation in the real world. InternetNZ has since built a comprehensive “fake root” validation system with caching recursive servers involved, so that we can validate our zone outputs in scenarios that closely match real-world scenarios, thereby ensuring our zone files won’t have negative side effects before they are released into the wild.

### AI Networking, UltraEthernet, the road to 1.6T and beyond.
Speakers: Matthew Thurbon (Arista)
The critical networking demands of AI applications are driving the requirements for high bandwidth, large-scale, low latency, and energy-efficient networks. This presentation explores the key design requirements for AI and HPC networking, and the emergence of UltraEthernet as an open-standards driven solution by the UltraEthernet Consortium (UEC). The latest advancements in optics will be explored, focusing on the transformative impact of standards based LPO (Linear Optical Pluggable) transceivers and the latest advancements in 800GbE and 1.6TbE that enable next-generation AI Interconnect performance. This presentation is designed for networking architects, data center operators, and AI/HPC infrastructure teams seeking to understand how AI network fabrics are built, and the technical advancements shaping the future of high-performance Ethernet networking.

### AI-Powered Telco SecOps Use Cases
Speakers: Rusdy Krisman (Fortinet)
Traditional ways of dealing with security incidents and remediations are no longer meeting the scope, complexity, and regulatory response timeframes. AI-powered SecOps enables telco operators and service providers to deliver faster incident detection, response, and reporting for better visibility, detection, and compliance.

### Challenges in simulating LEO satellite networks like Starlink
Speakers: Wayne Reiher (UoA)
Simulating Geostationary Earth Orbit (GEO) satellites is relatively straightforward, as these satellites appear stationary from a ground station’s perspective, resulting in constant data rates and latency. Similarly, Medium Earth Orbit (MEO) satellites exhibit generally stable latencies and data rates, though with lower overall latency than GEO systems. In contrast, Low Earth Orbit (LEO) satellite networks present more complex simulation challenges due to their dynamic characteristics. Multiple factors contribute to their variable latencies and data rate profiles, including continuous satellite movement, frequent client handovers between satellites, inter-satellite link switchovers, fluctuating satellite load due to changing ground client sets, complex routing, algorithms, constellation design, etc. Our current initiative focuses on enhancing our existing hardware-based GEO and MEO satellite simulator to accommodate LEO network simulation. This requires continuous updates to netem delay and token bucket filter parameters in real time to replicate the changing latencies and data rates that ground stations experience. This talk discusses the challenge this poses in an extensive physical hardware setup with around 150 devices.

### Chorus is going boost fibre plans for over 700,000 Kiwi homes – find out how we will technically deliver the upgrade and how you can get the best performance out of Chorus’ services 😮‍💨
Speakers: Brent Marquis (Chorus)
Chorus has announced free speed upgrades to some of its most popular wholesale plans, in anticipation of New Zealand’s ever-growing demand for high-speed internet.
From June 2025, the fast-growing 50/10Mbps plan will have double the download and upload speeds to 100/20Mbps; while the most popular residential plan, 300/100Mbps, will see a significant boost to 500/100Mbps.
In this presentation, Brent will talk about the technical details of how Chorus will apply those speed upgrades to the network without impacting your customer’s services. The work will occur during a complex web of systems and in-flight work.
The specific topics covered will be:
High-level overview of the systems interactions and how to decouple the network change. How the Chorus network configuration allows us to make modifications like this Information about the process and scripts we use to perform the service migration How you, as RSPs and customers, can ensure you get the best performance out of our services.

### KINDNS: Promoting DNS Security Best Practices
Speakers: Champika Wijayatunga (ICANN)
DNS itself and all the security measures that support its operation are based on open standards. As it is typically the case with security in general, getting all DNS operators and others in the DNS ecosystem to implement security features at the same level has been challenging. Smaller operators struggle to follow the continuous evolution of security measures, while large operators may choose and implement only the measures that are most helpful to their business goals. Meanwhile, this patchwork of varying security levels leads to vulnerabilities that malicious actors leverage for their attacks. Knowledge-Sharing and Instantiating Norms for DNS and Naming Security (KINDNS) is a framework that aims to identify sets of simple and straightforward measures that DNS operators of any size can implement in order to mitigate those exploits and focus on the most important operational best practices.

### Internet Governance
Speakers: Jodi Anderson (InternetNZ)
This presentation is an update and a “going deeper” on the presentation of last year, and will focus on the upcoming “WSIS+20” negotiations in the United Nations and why this is important to Internet governance and the global, interoperable Internet as we know it. It will update listeners on the work of the Technical Community Coalition for Multistakeholdersim which InternetNZ helped establish last year to input the voice of the Internet technical community into negotiations like WSIS+20.

