>>> HOW TO RUN THIS <<<
This is the digest prompt for ripe-91. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ripe-91.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ripe-91.md
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

Below is the program for RIPE 91 (Bucharest) (operator). Read it and produce a digest
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
conference: RIPE 91 (Bucharest)
type: operator
source_url: https://ripe91.ripe.net/programme/meeting-plan/
generated: 2026-11-01
registry_key: ripe-91
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Tutorial - Main Room (Mon, 09:00)

### Free and open-source network labs with Containerlab: an intro, an update, a workshop
Speakers: Gordon Gidofalvy , Nokia
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/2/9HJZQY/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/9HJZQY/resources/Containerlab_Preso_No_2MIPNyQ.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/9HJZQY/resources/Containerlab_Preso_N_lEs9jGc.pptx | video: https://ripe91.ripe.net/media/videos/gordon-gidofalvy_free-and-open-source-network-labs-with-containerlab-an-intro-an-update-a-work_main_20251020-090126.mp4
Containerlab , a free and open-source, vendor-neutral containerized network labbing tool, is turning 5 this year. This talk introduces the tool and also presents newly-added features, making it accessible to both those new to the tool and seasoned veteran users alike. We present what Containerlab is, the basic concepts behind its operation, and a selection of network OSes and software that it can run in arbitrary topologies. Following this, we show off the initial steps required to deploy your first Containerlab topology. The talk also shows off the growing Containerlab ecosystem, including a successful thesis project built on top of it, and present some use-cases that take Containerlab beyond learning & "labbing", enabled by other free and open-source community projects. Finally, we present some of the work of the Containerlab community, and end off with a few notes on what the future of Containerlab looks like with a call to action, before we head off into a 60 minute workshop session. As part of the workshop, participants will get acquainted with Containerlab, deploy their first lab featuring FRR, expand the topology, configure a network, and collaborate to build a working Internet as the last step. For the workshop, you will need access to a Linux host, running on kernel 5.4 or newer. This can be a physical or VM host, it can be a fresh install, even. The host should have access to the Internet. Hosted VMs can be arranged for those who might have more restrictive setups, but participants are encouraged to work on their own equipment, to preserve the labs and results after the workshop ends. For those who prefer a more GUI-oriented workflow, please also install VS Code on your laptops.

## Plenary - Main Room (Tue, 09:00)

### Collecting and analyzing routing information with Rotonda
Speakers: Luuk Hendriks , NLnet Labs Jasper den Hertog , NLnet Labs
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/15/CLRNRY/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/CLRNRY/resources/rotonda_ripe91_eFWBjdb.pdf | video: https://ripe91.ripe.net/media/videos/luuk-hendriks_collecting-and-analyzing-routing-information-with-rotonda_main_20251021-090048.mp4
Understanding networks' routing behavior has always been important to network operators, but has become more difficult in recent years. Not only because of ever-increasing scale, but also because the introduction of RPKI-based routing security approaches affect routes. Not all routing platforms provide detailed insights into these effects, emphasizing the need for more transparency and tools for operators to understand the full picture of their networks. With Rotonda, we introduce an open-source software package that enables high-scale, high-performance route information collection. By ingesting routing information via BMP and BGP, combined with RPKI information via RTR, it provides operators with a way to analyze and monitor their networks. Appreciating the fact that no two networks are the same, that every operator has their own specific questions about their network, route monitoring should be flexible. Our in-house developed programming language Roto provides that flexibility. With Roto scripts, operators can filter routes to be stored, and monitor events and features in a highly customizable way. Because these scripts are compiled to machine code, the flexibility comes at negligible overhead and thus enables operators insights in even the hottest parts of the collection process. Easy deployment of monitoring solutions is not always a given, and especially for smaller networks it may feel like a disproportionate effort even though their monitoring questions and needs are as valid and useful as they are for larger networks. With Rotonda being a self-contained, single (Rust) binary, we aim to facilitate operations regardless of scale, whether that's 50 or 50 million routes. In this talk, we present an overview of the components of Rotonda, and show how different combinations of these components serve typical use-cases. It will also be a call to the community, asking for input and collaborations, with the sole aim of making Rotonda as useful as can be when it comes to making sense of our networks today.

### Route Collectors: Collecting all of most of the available routes!
Speakers: Radu Anghel , TU Delft
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/15/UZ3QFZ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/UZ3QFZ/resources/20251020_RCs_4KVRWf3.pdf | video: https://ripe91.ripe.net/media/videos/radu-anghel_route-collectors-collecting-all-of-most-of-the-available-routes_main_20251021-092819.mp4
The Internet, often perceived as a single entity, is in fact a collection of smaller networks, each speaking the Border Gateway Protocol (BGP). Despite this common protocol, individual experiences of what the Internet is can vary significantly depending on the point of observation. These differences present challenges for analysis, which is typically conducted using data provided by Route Collectors (RCs). RCs act as the 'memory' of the Internet, capturing snapshots of the Global Routing Table (GRT) through Routing Information Base (RIB) dumps and incremental updates. This presentation will discuss the major RC projects, such as RIPE RIS, RouteViews, and PCH, that have extensive collections of routing information, providing researchers with diverse perspectives from different vantage points. However, some downsides of these RC projects will be discussed, including potentially unexpected or unwanted information, such as private address space or more-specific prefixes. Other included aspects refer to developments surrounding RCs, such as RIS Live, per-peer dumps, and CAIDA BGP Stream, and recent proposals advocating for semi-mandatory RC peering (MANRS VIP zones). The presentation offers suggestions for easy to implement practical improvements in RC infrastructure to support more accurate and efficient Internet measurement.

### Apple Wireless Direct Link: Apple's Network Magic or Misery
Speakers: Christoff Visser , IIJ - Research Lab
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/15/3KJJLU/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/3KJJLU/resources/RIPE_91_AWDL_-_Final__Nhu7zHJ.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/3KJJLU/resources/AWDL_-_RIPE91_wn7iago.pptx | video: https://ripe91.ripe.net/media/videos/christoff-visser_apple-wireless-direct-link-apples-network-magic-or-misery_main_20251021-095311.mp4
With over 1.5 billion iPhones around the world, Apple's impact on the mobile landscape is unquestionable. One of the key reasons for this widespread adoption is the "Apple ecosystem", with features such as AirDrop, AirPlay, and more. Apple Wireless Direct Link (AWDL) is Apple's proprietary and undocumented IEEE 802.11-based ad hoc protocol that enables seamless data sharing between Apple devices. However, the Apple ecosystem is a double-edged sword, and AWDL can introduce network jitter on Apple devices. In this talk, we will go over how AWDL can disrupt the connectivity for Apple devices on Wi-Fi, and how "bad" networking practices can improve the end-user experience for Apple devices in your network.

## Connect - Main Room (Wed, 09:00)

### Opening + Housekeeping
Speakers: Stavros Konstantaras , AMS-IX Paul Hoogsteder Will van Gulik
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/27/PENXNE/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/PENXNE/resources/Connect-wg-ripe91_H5irm2q.pdf | video: https://ripe91.ripe.net/media/videos/stavros-konstantaras_opening-housekeeping_main_20251022-090047.mp4
Welcome, agenda, RIPE90 meeting notes

### PeeringDB Update
Speakers: Leo Vegoda , PeeringDB
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/27/GJ98YB/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/GJ98YB/resources/20251022_RIPE_91_Leo__0wTo2q4.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/GJ98YB/resources/20251022_RIPE_91_Leo_P4sjpkA.pptx | video: https://ripe91.ripe.net/media/videos/leo-vegoda_peeringdb-update_main_20251022-090204.mp4
Present an update on PeeringDB including: - Update of community volunteers and new translations - MFA mandate was a success - New features, including ASN Comparison function - Update on web UI improvements

### Exploring the Blind Spot of IXP Route Server
Speakers: Stefano Servillo , Sapienza University of Rome
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/27/C3ZSGJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/C3ZSGJ/resources/RIPE_91_aFUJkm1.pdf | video: https://ripe91.ripe.net/media/videos/stefano-servillo_exploring-the-blind-spot-of-ixp-route-server_main_20251022-090928.mp4
Internet Exchange Points (IXPs) are critical components of today’s Internet, as they handle a substantial share of global traffic and enable efficient interconnection among networks. At the heart of their operation are Route Servers (RS) , which simplify public peering by allowing Autonomous Systems (ASes) to establish a single BGP session with the RS. However, a key challenge of BGP is its trust-based route sharing , which introduces vulnerabilities that can be exploited to hijack or disrupt traffic. To mitigate such risks, IXPs implement filtering policies on RS primarily based on two mechanisms: Internet Routing Registries (IRRs) and the Resource Public Key Infrastructure (RPKI) . Current RS filtering practices, however, reveal a blind spot : IRR-based filtering depends heavily on AS-SET objects , which are often outdated. Unlike RPKI, IRR validation does not bind a prefix to its legitimate owner AS , leaving room for hijacks or misconfigurations to be accepted and propagated. In this work, we analyze this vulnerability, showing how an attacker can exploit IRR-based filtering to perform prefix hijacking through IXPs . We analyzed the configuration of several IXPs in the EURO-IX community and found that most of them are affected by this vulnerability . To address it, we propose solutions that IXPs can adopt, alongside recommendations for both network operators and IXP operators to improve filtering practices. Finally, we validate our findings through an analysis of real-world data from the route server RIBs of two major European IXPs , demonstrating the practical impact of the problem.

### European Interconnection Regulation - Proposals and Impacts
Speakers: Mike Blanche
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/27/FSUDM8/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/FSUDM8/resources/RIPE_91_-_Connect-WG__osrdR3k.pdf | video: https://ripe91.ripe.net/media/videos/mike-blanche_european-interconnection-regulation-proposals-and-impacts_main_20251022-093622.mp4
An overview of IP interconnection regulation that may appear in the European Commission's upcoming Digital Networks Act, and its possible impacts on the IP interconnection ecosystem.

### How far can you get with IX Route Servers?
Speakers: Ben Cartwright-Cox , bgp.tools / Port 179 LTD
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/27/ZRGKVK/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZRGKVK/resources/How_far_can_you_go_wi_G4sXpyE.pdf | video: https://ripe91.ripe.net/media/videos/ben-cartwright-cox_how-far-can-you-get-with-ix-route-servers_main_20251022-100058.mp4
Route servers are the most important service (other than moving packets itself) on an internet exchange fabric, however in most exchanges they are not mandatory. This talk aims to answer the question of how effective route servers are and distributing routes to many networks, using the large internet exchange deployment footprint of the bgp.tools route collector network.

### The role of IXPs in South East Europe
Speakers: Jelena Cosic
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/27/PPUKYD/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/PPUKYD/resources/SEE_IXP_Report_1_CHsI6na.pdf | video: https://ripe91.ripe.net/media/videos/jelena-cosic_the-role-of-ixps-in-south-east-europe_main_20251022-101828.mp4
How do we know when an IXP is working well? What goals should it achieve, and can success be measured in the same way everywhere? Our latest report examines the current state of Internet Exchange Points (IXPs) in South East Europe (SEE) and their role in improving connectivity in the region.

## Open Source - Side Room (Wed, 09:00)

### Scope creep in open source
Speakers: Ondrej Zajicek , CZ.NIC | BIRD
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/28/N7MBW9/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/N7MBW9/resources/slides_LZzSuzo.pdf | video: https://ripe91.ripe.net/media/videos/ondrej-zajicek_scope-creep-in-open-source_side_20251022-090243.mp4
Open source projects frequently struggle with scope creep as they evolve beyond their original vision. This talk examines the underlying forces driving scope expansion, including community pressure, architectural dependencies, and evolving user needs. We explore how implementing in-scope features often necessitates out-of-scope functionality, and how user workflows blur the boundaries between intended and unintended feature sets. Using BIRD Internet Routing Daemon as a case study, we examine tensions between developing a lightweight routing daemon and a full-fledged routing software.

### When to actually rewrite it in rust?
Speakers: Annika Hannig , Freelance Software Developer
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/28/UDQG8S/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/UDQG8S/resources/alice-ripe91_sRLtrkM.pdf | video: https://ripe91.ripe.net/media/videos/annika-hannig_when-to-actually-rewrite-it-in-rust_side_20251022-092605.mp4
This is the story of my rewrite of birdwatcher[1] in rust over a total period of three years. It all started when I tried to fix a peculiar memory deallocation problem that occurred in the original go version of birdwatcher and failed. The garbage collector was just unwilling to release a bit of memory in time. Frustrated by hours of debugging and profiling I finally thought: The estrogen is working great, let's put on that extra spinny skirt and try this again in rust. Join me on this journey through the dark world of state machines, concurrency, cache invalidation, profiling and regular expressions. [1] Birdwatcher, for the uninitiated, is a small server that interacts with the BIRD routing daemon and exports the cli output as structured json to be consumed by the Alice Looking Glass.

### Streamlining the release process from the git
Speakers: Ondřej Surý , ISC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/28/UMGVCV/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/UMGVCV/resources/open-source-release-e_GHw7Lcz.pdf | video: https://ripe91.ripe.net/media/videos/ondrej-sury_streamlining-the-release-process-from-the-git_side_20251022-095948.mp4
At ISC, we have developed a system based on git-changelog and danger that streamlines the changelog and release notes creation based on the merge request description. This in turn simplifies rebasing and merging (no more conflicts in the changelogs). We also have couple more tools that help us improve the quality of the merge requests (danger based checks, linters, SPDX checks, etc...).

## IPv6 - Main Room (Thu, 09:00)

### Welcome and announcement of the new co-chair
Speakers: Christian Seitz Raymond Jetten
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/37/RTKFBS/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/RTKFBS/resources/RIPE91-IPv6-WG-Openin_jhqZD7Z.pdf | video: https://ripe91.ripe.net/media/videos/christian-seitz_welcome-and-announcement-of-the-new-co-chair_main_20251023-090208.mp4
Welcome and announcement of the new co-chair.

### IPv6: What does it cost to do nothing?
Speakers: Dmitriy Melnik , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/37/8YZNF9/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/8YZNF9/resources/RIPE_91_-_IPv6_What_d_qRaOP3e.pdf | video: https://ripe91.ripe.net/media/videos/dmitriy-melnik_ipv6-what-does-it-cost-to-do-nothing_main_20251023-090727.mp4
This talk will explain how you can save money and where you're overspending - by not implementing IPv6! We’ll explore the hidden costs of depending on NAT, from hardware upgrades to increasing operational complexity, and show how shifting traffic to IPv6 can help cut both CAPEX and OPEX. Why keep spending more to maintain IPv4, when you could invest that money in something new for your company?

### IPv6 in large Organisations - Lessons learned
Speakers: Wilhelm Boeddinghaus , Route 128 GmbH
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/37/UEK3QK/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/UEK3QK/resources/IPv6_in_large_Organis_86rnvIe.pdf | video: https://ripe91.ripe.net/media/videos/wilhelm-boeddinghaus_ipv6-in-large-organisations-lessions-learned_main_20251023-093518.mp4
When implementing IPv6 in large organisations, it is not easy to get from "planing" to "doing". This talk gives some insights on how to speed up IPv6 in large enterprises and in public agencies, lessons we have learned working with these organisations and how to move people and networks to IPv6.

### DHCPv6 Prefix Delegation for Android
Speakers: Jen Linkova
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/37/YXRZB8/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/YXRZB8/resources/RIPE91-Host-PD_vHIIub8.pdf | video: https://ripe91.ripe.net/media/videos/jen-linkova_dhcpv6-prefix-delegation-for-android_main_20251023-101444.mp4
Some updates on DHCPv6-PD support for Android.

## Database - Side Room (Thu, 09:00)

### NWI Review
Speakers: Peter Hessler , DB-WG Chairs David Tatlisu
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/38/R7WC3F/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/R7WC3F/resources/nwi-update_PA3WUsp.pdf | video: https://ripe91.ripe.net/media/videos/peter-hessler_nwi-review_side_20251023-090339.mp4
NWI Review

### RIPE NCC Operational Update
Speakers: Ed Shryane
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/38/ASR8NC/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ASR8NC/resources/RIPE91_DB-WG_Operatio_oFguWEz.pdf | video: https://ripe91.ripe.net/media/videos/ed-shryane_ripe-ncc-operational-update_side_20251023-092031.mp4
Operational Update from the RIPE NCC Database team

## Plenary - Main Room (Fri, 09:30)

### Towards Operational and Security Best Practices for DNS in the Internet of Things
Speakers: Andrew Losty , PhD student at UCL (University College London) Dept Electronic and Electrical Engineering
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/52/TCAFQK/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/TCAFQK/resources/RIPE91-DNS-IoT_X4FNCap.pdf | video: https://ripe91.ripe.net/media/videos/andrew-losty_towards-operational-and-security-best-practices-for-dns-in-the-internet-of-thing_main_20251024-093111.mp4
The Domain Name System (DNS) underpins Internet connectivity, yet its role is often overlooked in the context of Internet of Things (IoT) devices. With IoT devices expected to increase from 19.8 billion in 2025 to over 40.6 billion by 2034, this oversight exposes significant security and operational vulnerabilities. Investigating DNS behavior in IoT is essential to safeguard the stability and resilience of this critical expanding segment. We investigate IoT DNS behavior in three areas: (1) security, assessing support for secure protocols (DoT/DoH), payload resilience, and operational vulnerabilities; (2) operational characteristics, analyzing TTL adherence, caching, server hardcoding, EDNS(0), TCP fallback, query rates, traffic-fingerprinting; and (3) regulatory frameworks, evaluating standards from IETF, ETSI, and ISO/IEC to identify existing DNS recommendations for IoT devices. We analyze DNS behavior of over 30 consumer IoT devices across 11 smart home categories within a controlled testbed featuring a dedicated Wi-Fi network, data collection server, Unbound resolver, and DNS DoS server. Active experiments simulate attacks via manipulated DNS responses, while passive measurements assess protocol compliance, operational efficiency, and support for secure DNS protocols and DNS extensions. Our analysis reveals widespread DNS vulnerabilities across IoT devices; none support encrypted protocols (DoH, DoT), or extension mechanism EDNS(0). Devices use hardcoded DNS servers, ignore TTL values, and exhibit minimal source-port and transaction-ID randomization and DNS traffic is highly 'fingerprintable'. Standardized DNS practices for IoT are urgently needed to prevent insecure implementations that threaten network integrity. We propose a Best Practice RFC (draft-mishra-iotops-iot-dns-guidelines-00 ) to guide consistent and secure DNS use across IoT platforms. This standardization is vital to ensure the long-term security, interoperability, and resilience of emerging IoT ecosystems.

### IPv4 vs. IPv6 for Authoritative DNS
Speakers: Shane Kerr , IBM NS1 Connect
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/52/WELJDM/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/WELJDM/resources/IPv4_vs._IPv6_for_Aut_oYOBTSG.pdf | video: https://ripe91.ripe.net/media/videos/shane-kerr_ipv4-vs-ipv6-for-authoritative-dns_main_20251024-100402.mp4
I did a quick measurement comparing our authoritative DNS edge in IPv4 vs. IPv6. There does not appear to be any difference in the quality of service. Is DNS ready for IPv6-only authoritative service?

### An Update on IBDNS, the Intentionally Broken DNS Server
Speakers: Marc van der Wal , Afnic
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/52/9SK7CP/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/9SK7CP/resources/IBDNS_Lightning_Talk__shR1XqB.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/9SK7CP/resources/IBDNS_Lightning_Talk_rhBj7Av.pptx | video: https://ripe91.ripe.net/media/videos/marc-van-der-wal_an-update-on-ibdns-the-intentionally-broken-dns-server_main_20251024-101247.mp4
It’s been three years since I first presented IBDNS, the Intentionally Broken DNS Server, at DNS-OARC 38. The tool is primarily developed for testing Zonemaster, helping to make sure that Zonemaster gives the correct diagnostics in the right situations. This talk focuses on a concrete use case for IBDNS that does not involve Zonemaster: help with testing the implementation of a proposal of an EDNS option, that was done during the DNS Hackathon earlier this month.

### Filter Your Things or No I don't want to use your NTP Server
Speakers: Dave Phelan , APNIC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/52/BXAUMQ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/BXAUMQ/resources/Filter_your_things-Da_nAvfmSx.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/BXAUMQ/resources/Filter_your_things-D_w6TKCpb.pptx | video: https://ripe91.ripe.net/media/videos/dave-phelan_filter-your-things-or-no-i-dont-want-to-use-your-ntp-server_main_20251024-102250.mp4
A Short presentation on Open UDP ports in the RIPE service region. Call to action for filtering and not being part of the DDoS Problem

## Plenary - Main Room (Tue, 11:00)

### What’s new at the IETF?
Speakers: Suresh Krishnan , Cisco
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/17/CGDZGZ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/CGDZGZ/resources/RIPE_IETF_Whats_New_S_AQNgBgL.pdf | video: https://ripe91.ripe.net/media/videos/suresh-krishnan_whats-new-at-the-ietf_main_20251021-110114.mp4
The Internet Engineering Task Force (IETF) works on developing the voluntary standards that underpin the global Internet. These standards often influence operational practices, network architecture, and protocol evolution across the ecosystem. This session will highlight some key developments at the IETF, including new standards proposals, newly chartered working groups, and hot topics gaining traction within the IETF community. Special attention will be given to areas of direct relevance to network operators. Whether you’re tracking standards adoption, involved in deployments and operations, or just curious about emerging protocol trends, this talk will offer a concise, operator-focused view of what’s brewing at the IETF.

### Are NTP Clients Always Right?
Speakers: Shreyas Konjerla , TU Delft
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/17/RNBMHH/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/RNBMHH/resources/RACI_7mUlSus.pdf | video: https://ripe91.ripe.net/media/videos/shreyas-konjerla_are-ntp-clients-always-right_main_20251021-113305.mp4
The Network Time Protocol (NTP) is the primary synchronization protocol for billions of devices. Although attacks on NTP servers have been well studied, attacks on NTP clients are less well understood. In this thesis, we scrutinize the 8 NTP clients across 3 Operating systems and test their resilience against attackers and malicious public time servers. We test all the clients against time manipulation, or time-shift attacks and exploit NTP protocol features to induce a denial-of-service for the client by cutting them off from legitimate time servers. We also analyze how these clients perform in normal operations or do they deviate from the NTP-specification-recommended behavior. Our research analysis reveiled 5 bugs and one vulnerabilities, which we disclose to the vendors. While most of the NTP clients follow the associated NTP standards, there exists a wide diversity in the behavior of all the time clients. While many clients follow the specification and best practices, deviations exist which make some of our attacks successful. In detail, macOS time client is vulnerable to Time Shift attacks, and NTPD-RS is vulnerable to certain Kiss-of-Death packets which causes it to flood the network with queries and OpenNTPd cannot handle the NTP timestamp rollover. We dive into the design and configuration decisions that make the clients vulnerable to different attacks, we comment of the potential harm, and we propose mitigation.

### NTPinfo - Application for measuring NTP servers accuracy and more
Speakers: Calin Olaru , Student at Delft University of Technology Horia-Andrei Botezatu Mihai Nicolae Serban Orza
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/17/8WYZGT/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/8WYZGT/resources/NTPinfo_TU_Delft_pre__0aUCWSn.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/8WYZGT/resources/NTPinfo_TU_Delft_pre_HYhbF9w.pptx | video: https://ripe91.ripe.net/media/videos/calin-olaru_ntpinfo-application-for-measuring-ntp-servers-accuracy-and-more_main_20251021-115924.mp4
My team and I (made up of 2nd year students at TU Delft) have developed a tool allowing users to measure the accuracy of NTP servers, receiving data such as offset, round-trip time, precision, stratum etc., as well as being able to see historical data of the server and compare multiple servers. The application also integrates the RIPE Atlas API to measure the NTP server from probes close to the user. We would like to present the research we've done into these topics, including mapping a domain name to different IPs, selecting the closest probes (ASN vs prefix vs country), supporting measurements through IPv6 and how to compute certain results (e.g. offset, jitter).

## Routing - Main Room (Wed, 11:00)

### Assessing the feasibility of routing security compliance tests
Speakers: Moritz Müller , SIDN Labs, University of Twente Lisa Bruder , SIDN Labs
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/30/L3FE7Y/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/L3FE7Y/resources/ripe_presentation_hLR4Uxr.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/L3FE7Y/resources/ripe_presentation_7mjXJkB.pptx | video: https://ripe91.ripe.net/media/videos/moritz-muller_assessing-the-feasibility-of-routing-security-compliance-tests_main_20251022-110409.mp4
We supported GCA in their efforts to develop an elevated tier of MANRS (MANRS+) by conducting a feasibility study on measuring routing security controls. To this end, we developed a local prototype that simulates the audit of an AS using containerlab. We audit by setting up peering sessions between the audited AS and two other local ASes. The first AS exports prefixes to the audited AS and the second AS imports prefixes received from the audited AS. We then analyse the imported prefixes to draw conclusions about the filters configured at the audited AS. Our prototype demonstrates the ability to reliably audit the correct implementation of filters. However, we expect auditing of production ASes to bring on much more complexity and the need to further develop the prototype. By presenting at the Routing WG, we aim to gather feedback from the community that can help improve the prototype as well as a provide guidance to a potential future production deployment led by GCA or similar auditing efforts. Our implementation of the local test-bed is open source.

### ASPA in the RPKI Dashboard
Speakers: Tim Bruijnzeels , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/30/VZNKWV/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/VZNKWV/resources/RIPE91-ASPA-in-the-RP_btaE9nq.pdf | video: https://ripe91.ripe.net/media/videos/tim-bruijnzeels_aspa-in-the-rpki-dashboard_main_20251022-112256.mp4
We introduced ASPA concepts at RIPE 90. By RIPE 91 we will have enabled ASPA in the UI. We would like to talk to the working group to once more share what ASPA is about for those who missed it, and then show how ASPA can be used in the RPKI Dashboard. We also want to ask for user feedback on the usability of the interface we built and plan to organise sessions for that on the Wednesday afternoon.

### What happens when you overshare? A Look into the BGP Maximum-Prefix Feature
Speakers: Orlando Eduardo Martínez-Durive , NetAI & IMDEA Networks (work done as a research intern at Cisco ThousandEyes) Antonis Chariton , Cisco
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/30/JDHZFZ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/JDHZFZ/resources/slides_UDSaivF.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/JDHZFZ/resources/slides_p7lkxZE.pptx | video: https://ripe91.ripe.net/media/videos/orlando-eduardo-martinez-durive_what-happens-when-you-overshare-a-look-into-the-bgp-maximum-prefix-feature_main_20251022-115547.mp4
The BGP protocol is a crucial component of large network systems, particularly the Internet, as it enables Autonomous Systems (ASes) to exchange information about paths. Although it is essential, BGP is relatively fragile. Sometimes, software errors, misconfigurations, and malicious actors can cause disruptions that range from minor to severe, potentially leading to large-scale outages affecting popular services or companies. Despite efforts to enhance BGP security and configuration, further improvements are necessary in several areas. One configuration that has received less attention is the Maximum-Prefix Limit, a setting used in BGP sessions to specify the maximum number of IP prefixes that a peer is expected to send. While the intended behavior is for the number of prefixes to stay within this limit, this is not always the case. The two most common ways to handle when the limit is exceeded are: ignore the increase and continue accepting additional prefixes, or temporarily drop the BGP session until the number falls within the limit or a higher value is set. The latter could lead to an outage if many peers are configured to drop sessions. To assess the likelihood of an outage caused by exceeding the limit, we analyzed 6.5 months of Routing Information Base MRT files from RIPE, from January 1 to July 25, 2025. We also used historical snapshots from PeeringDB to monitor the Maximum-Prefix Limit advertised by ASes. Our analysis examined how the Prefix Limit, the number of announced prefixes, and the number of peers change over time, while quantifying these changes. Results show that, on average, surpassing the prefix limit does not significantly increase the risk of outages. However, in some instances, it can cause a significant drop in the number of peers, exceeding 80%, which can severely impact connectivity and traffic exchange.

### Rewriting BGP Origin
Speakers: James Bensley , Inter.link
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/30/GJ8PFJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/GJ8PFJ/resources/RIPE91_-_BGP_Origin_T_HYCTVQf.pdf | video: https://ripe91.ripe.net/media/videos/james-bensley_rewriting-bgp-origin_main_20251022-120705.mp4
"This 1 trick IP transit providers don't want you to know" - would be the title of this talk if it was a Substack blog post. Everyone is playing games to attract more traffic, one of those is to rewrite the BGP origin attribute, but it's not being talked about, so let's talk about it. In this talk I will present how the largest carriers are rewriting the BGP origin attribute in order to attract more traffic to their network. It's nothing new, but anyone not doing this looses out. As an IP transit provider, we've tried to resist but the problem isn't going away, so we want to talk about it publicly. UPDATE: after giving this presentation it was discovered that AS3320 were incorrectly listed as one of the networks that rewrite the origin attribute. This is not the case. I have update the slides attached to this presentation to correct this.

## Cooperation - Side Room (Wed, 11:00)

### #LaLigaGate: private interests vs Fundamental Digital Rights
Speakers: Román Ramírez , RootedCON Association
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/31/AQBZWD/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/AQBZWD/resources/RIPE91_LaLigaGate_iBU4XIb.pdf | video: https://ripe91.ripe.net/media/videos/roman-ramirez_laligagate-private-interests-vs-fundamental-digital-rights_side_20251022-110531.mp4
Today, in Spain and in some regions of Europe, we are facing a significant conflict between Fundamental Digital Rights and Intellectual Property. The protection of football match broadcasts (managed by La Liga de Fútbol Profesional ), which undeniably provide great value to society and we respect that, has led to widespread interference resulting from the blocking of Cloudflare IP addresses. These blocks have been authorized by a court order that supposedly ensures no harm to innocent third parties ; telecommunications operators are required to comply with this order. In this talk, we will explain how this is not the case in reality— innocent third-party companies, media outlets, and citizens are indeed being affected . We will thus expose a problem that threatens citizens’ fundamental rights and that could further deteriorate, undermining a free Internet and the democratic safeguards it provides.

### Decoding the DNA - The Digital Networks Act and the Open Internet
Speakers: Mike Blanche
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/31/W7UDWP/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/W7UDWP/resources/RIPE_91_-_Cooperation_2qA2yHK.pdf | video: https://ripe91.ripe.net/media/videos/mike-blanche_decoding-the-dna-the-digital-networks-act-and-the-open-internet_side_20251022-112912.mp4
The European Commission's upcoming proposed Digital Networks Act is proposing to fundamentally reshape telecoms regulation for Europe. This has the potential to affect not just telecoms operators, but could usher new regulations and processes that affect the Open Internet more broadly. This talk will briefly describe the recent political history that has led to the DNA proposal, and highlight some of the possible changes that could impact Internet networks, services, and users.

### UN IGF Secretariat Update
Speakers: Anja Gengo , Programme Management Officer and NRIs focal point
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/31/YSFNHR/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/YSFNHR/resources/IGFSec_at_RIPE_Romani_gcnti7y.pdf | video: https://ripe91.ripe.net/media/videos/anja-gengo_un-igf-secretariat-update_side_20251022-115416.mp4
Update on IGF current activities and preparations for WSIS+20

### Making an Impact: Experiences in IETF Standards Development
Speakers: Éric Vyncke , Cisco Belgium
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/31/Z9EGV8/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/Z9EGV8/resources/RIPE-91_IETF_Panel.pp_g7ySRrn.pdf | video: https://ripe91.ripe.net/media/videos/eric-vyncke_making-an-impact-experiences-in-ietf-standards-development_side_20251022-121413.mp4
The Internet Engineering Task Force (IETF) defines the foundational standards that underpin the global Internet. Yet, it's the RIPE community that brings these standards to life through deployment, often encountering unforeseen operational challenges. This session will explore a critical question: How can the RIPE community effectively engage with the IETF to ensure that future standards are truly fit for purpose in real-world operational environments? Is active participation in the IETF a worthwhile investment for network operators? Join us to hear firsthand accounts from several experienced RIPE community members. They will share their personal journeys, practical insights, and compelling reasons why your operational perspective is vital in shaping the future of Internet standards. Éric Vyncke (moderator), IETF INT Area Director David ‘tale’ Lawrence, IETF Adaptive DNS Discovery Chair & Liaison to ICANN David 'equinox' Lamparter, NetDEF (Open Source Routing & IPv6) Jen Linkova, IPv6 Plumber at Google, IETF 6MAN WG chair, and past RIPE IPv6 WG chair Sander Steffann, RIPE NCC Exec Board Member

## Address Policy - Main Room (Thu, 11:00)

### Current ASO AC Activities
Speakers: Herve Clement , Orange SA / ASO AC Andrei Robachevsky , Global Cyber Alliance/NRO NC Constanze Buerger
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/40/M9V3QX/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/M9V3QX/resources/RIPE-91-NRO-NC-Update_MF4HerV.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/M9V3QX/resources/RIPE-91-NRO-NC-Updat_osq3Ehu.pptx | video: https://ripe91.ripe.net/media/videos/herve-clement_current-aso-ac-activities_main_20251023-110430.mp4
Recent developments around the second draft RIR governance document and what this means for the IP address community.

### Policy Update
Speakers: Angela Dall'Ara , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/40/EQNMVJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/EQNMVJ/resources/RIPE_91_Policy_Update_OLYkPVA.pdf | video: https://ripe91.ripe.net/media/videos/angela-dallara_policy-update_main_20251023-112320.mp4
Update on policy development since RIPE 90

### RIPE Docs & the Evolution of This Thing of Ours
Speakers: Ilke Ilhan , Business Data Analyst - RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/40/UJZ9N3/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/UJZ9N3/resources/RIPE_Docs__the_Evolu_sRXMG0n.pdf | video: https://ripe91.ripe.net/media/videos/ilke-ilhan_ripe-docs-the-evolution-of-this-thing-of-ours_main_20251023-114020.mp4
RIPE Documents keep our history. But history is also shaped between the docs! In this presentation, we will look at some visualisations of RIPE Docs and observe our evolution as a community.

### Registration Services Update
Speakers: Marco Schmidt , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/40/FJ7YSH/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/FJ7YSH/resources/RIPE91_Update_from_RS_GAmDwj9.pdf | video: https://ripe91.ripe.net/media/videos/marco-schmidt_registration-services-update_main_20251023-120033.mp4
Regular update from Registration Services to the Address Policy Working Group on observations relevant to RIPE policies. Topics include: RFC9663, which may impact IPv6 policy, improving accuracy for legacy resources without a contract, enhancing resource holder information, and a new request form for stopping sponsorship of independent resources.

## DNS - Side Room (Thu, 11:00)

### Welcome and announcement of the new co-chair
Speakers: Willem Toorop , NLnet Labs Yevheniya Nosyk , KOR Labs Moritz Müller , SIDN Labs, University of Twente
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/41/NSCCYE/ | video: https://ripe91.ripe.net/media/videos/willem-toorop_welcome-and-announcement-of-the-new-co-chair_side_20251023-110029.mp4
Welcome and announcement of the new co-chair

### A BCP on Hyperlocal Root
Speakers: Jim Reid
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/41/GH987G/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/GH987G/resources/Hyperlocal-RIPE91_2nowvEu.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/GH987G/resources/Hyperlocal-RIPE93_M18HDUR.key | video: https://ripe91.ripe.net/media/videos/jim-reid_a-bcp-on-hyperlocal-root_side_20251023-110343.mp4
RFC8806 introduced the concept of hyperlocal roots where resolving servers hold a copy of the root zone. This improves the overall stability and resilience of the Root Server System (RSS). The aim of draft-wkumari-dnsop-localroot-bcp is to develop RFC8806 into a Best Common Practice and encourage wider adoption. The I-D is expected to be discussed in the dnsop WG at IETF124.

### TLD Resilience in the Light of Signature Validity Constraints
Speakers: Ulrich Wisser , ICANN
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/41/8HJDVN/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/8HJDVN/resources/20251023-_RIPE91_-_RR_DeOaGYI.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/8HJDVN/resources/20251023-_RIPE91_-_R_R9e9eEB.pptx | video: https://ripe91.ripe.net/media/videos/ulrich-wisser_tld-resilience-in-the-light-of-signature-validity-constraints_side_20251023-110708.mp4
We have conducted a multi year study on RRSIG lifetimes for all Top Level Domains. This presentation will take a closer look on the interplay of RRSIG Lifetime and SOA Expire values. We will look at RFC recommendations and at different TLD's and their practices. Take-away from this study are relevant not only for TLD operators, but for any operator of DNSSEC signed zones.

### UA: XoT in practice
Speakers: Dmytro Kohmanyuk , Hostmaster.UA
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/41/YNMKZK/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/YNMKZK/resources/RIPE91_UA_XoT_2025_7PKLkNm.pdf | video: https://ripe91.ripe.net/media/videos/dmytro-kohmanyuk_ua-xot-in-practice_side_20251023-112619.mp4
I would tell a story how we (Hostmaster.UA) have switched from regular zone transfers to XoT and what lessons we have learned.

### DNS TTL Upper Limits in Practice
Speakers: Shane Kerr , IBM NS1 Connect
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/41/7Q99SU/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/7Q99SU/resources/Real-world_TTL_Limits_JWlPE8t.pdf | video: https://ripe91.ripe.net/media/videos/shane-kerr_dns-ttl-upper-limits-in-practice_side_20251023-114444.mp4
I recently ran a measurement of what the upper TTL caps are on resolvers used by RIPE Atlas probes. This talk gives the motivation of the measurement, some the results, and some analysis.

### RIPE NCC DNS Update
Speakers: Anand Buddhdev , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/41/UZSLH9/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/UZSLH9/resources/RIPE_91_DNS_Update_63qqy6z.pdf | video: https://ripe91.ripe.net/media/videos/anand-buddhdev_ripe-ncc-dns-update_side_20251023-121238.mp4
A short presentation about RIPE NCC's DNS activities

## Closing Plenary - Main Room (Fri, 11:00)

### Transparent DNS Forwarders: On the misuse potential in DNS ampliﬁcation attacks
Speakers: Maynard Koch , TU Dresden
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/3NL8EZ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/3NL8EZ/resources/mkoch-DNS-misuse-pote_2IMc7bh.pdf | video: https://ripe91.ripe.net/media/videos/maynard-koch_transparent-dns-forwarders-on-the-misuse-potential-in-dns-amplification-attacks_main_20251024-110039.mp4
The open DNS infrastructure is infamous for facilitating reflective amplification (RA) attacks. Various countermeasures, including server shielding, access control, rate limiting, and protocol restrictions, have been implemented. Still, the threat remains throughout the deployment of DNS servers. In this presentation, we report on the widely unnoticed threat that derives from transparent DNS forwarders, present our public measurement platform to monitor the current state, and discuss mitigation options. We raise awareness for the following reasons: (i) Transparent forwarders relay DNS requests as is, i.e., without rewriting the source IP address. As such, transparent forwarders feed arbitrary DNS requests that appear to be spoofed traffic into recursive resolvers, which, in the case of misuse, participate unwillingly in distributed RA attacks. (ii) Transparent forwarders scale much better in an RA attack compared to recursive forwarders and resolvers, as they only need to handle the DNS request but not the (amplified) response. (iii) Transparent forwarders redirect the resource-intense recursive workload of the DNS resolution to recursive resolvers that belong to a powerful infrastructure (e.g., Google and Cloudflare). (iv) Fingerprinting transparent forwarders reveals a broad picture of widely used vendors, ranging from CPE devices to IP cameras and powerful MikroTik Cloud-Core routers, which shows the prevalence of these devices on the Internet. The goal of this presentation is to raise awareness of the threat potential posed by transparent DNS forwarders and provide mitigation options. We publish our measurement results at https://odns.secnow.net and provide API access at https://odns-data.netd.cs.tu-dresden.de.

### Internet Resiliency Club update
Speakers: Valerie Aurora , Bow Shock Systems Consulting
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/BCMZQH/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/BCMZQH/resources/IRC_Update_RIPE_91_3iurFhR.pdf | video: https://ripe91.ripe.net/media/videos/valerie-aurora_internet-resiliency-club-update_main_20251024-112334.mp4
This talk is an update on the progress of the Amsterdam Internet Resiliency Club, a grass-roots community building a low power decentralized mesh network for disaster recovery.

### Khipu: RIPE Atlas traceroute visualisation
Speakers: Stephen Suess , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/WEGUGN/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/WEGUGN/resources/RIPE_Atlas_Khipu_pdf_JxWbZYO.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/WEGUGN/resources/RIPE_Atlas_Khipu_rlch233.key | video: https://ripe91.ripe.net/media/videos/stephen-suess_khipu-ripe-atlas-traceroute-visualisation_main_20251024-113540.mp4
An overview of the new RIPE Atlas visualisation tool, Khipu.

### TR 471: Automated speed test via TR 069 / TR 369
Speakers: Eric van Uden , FRITZ! ICT GmbH
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/ZTUGKE/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZTUGKE/resources/FRITZ_RIPE_2025_EvU__iZu8z9k.pdf | video: https://ripe91.ripe.net/media/videos/eric-van-uden_tr-471-automated-speed-test-via-tr-069-tr-369_main_20251024-114655.mp4
More and more countries regulators require ISP`s to show what speeds they actually deliver to their customers. But how to proof? Within the BBF, the standard TR 471 is used for this purpose. This presentation shows how this can be applied in practice.

### RIPE Code of Conduct Team Report
Speakers: Franziska Lichtblau
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/XNZ8GG/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/XNZ8GG/resources/RIPE91_CoC_Transparen_8NhO8dS.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/XNZ8GG/resources/RIPE91_CoC_Transparen_0T4Dwvu.key | video: https://ripe91.ripe.net/media/videos/franziska-lichtblau_ripe-code-of-conduct-team-report_main_20251024-115410.mp4
Report from the RIPE Code of Conduct team at RIPE 91

### RIPE 91 Tech Report
Speakers: Sjoerd Oostdijck , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/DWU8KD/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/DWU8KD/resources/RIPE_91_Tech_report_b_ThnqvW1.pdf | video: https://ripe91.ripe.net/media/videos/sjoerd-oostdijck_ripe-91-tech-report_main_20251024-120103.mp4
Report from the RIPE Meeting Tech Team

### Closing
Speakers: Mirjam Kühne , RIPE Chair
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/MNZ8LD/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/MNZ8LD/resources/RIPE_91_Closing_Plena_t8rRMmV.pdf | video: https://ripe91.ripe.net/media/videos/mirjam-kuhne_closing_main_20251024-121350.mp4
Closing presentation from the RIPE Chair Team

### Welcome to RIPE 92
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/55/ME7QRQ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ME7QRQ/resources/Hilco_RIPE92_Presenta_QZWQfx4.pdf | video: https://ripe91.ripe.net/media/videos/na_welcome-to-ripe-92_main_20251024-122318.mp4
The host of the upcoming RIPE Meeting invites you to join RIPE 92

## Newcomer's Introduction - Main Room (Mon, 11:30)

## Opening Plenary - Main Room (Mon, 14:00)

### Welcome to RIPE 91
Speakers: Mirjam Kühne , RIPE Chair
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/RWYJXJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/RWYJXJ/resources/Welcome_to_RIPE_91_IpgAHuq.pdf | video: https://ripe91.ripe.net/media/videos/mirjam-kuhne_welcome-to-ripe-91_main_20251020-140107.mp4
Welcome to RIPE 91

### Welcome from the Local Host
Speakers: Eric Andrei Băleanu , InterLAN-IX
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/9SKRMW/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/9SKRMW/resources/RIPE_91_Welcome_Inte__oTtuEQN.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/9SKRMW/resources/RIPE_91_Welcome_Inte_7JLoknJ.pptx | video: https://ripe91.ripe.net/media/videos/eric-andrei-baleanu_welcome-from-the-local-host_main_20251020-153912.mp4
Welcome to Bucharest

### Welcome from the RIPE NCC and Meeting Logistics
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/BULEDJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/BULEDJ/resources/RIPE_91_Meeting_Logis_29J44mC.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/BULEDJ/resources/RIPE_91_Meeting_Logi_XPI927a.pptx | video: https://ripe91.ripe.net/media/videos/hans-petter-holen_welcome-from-the-ripe-ncc-and-meeting-logistics_main_20251020-142219.mp4
RIPE 91 Meeting Logistics

### NRO NC Elections
Speakers: Ulka Athale , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/QCT88G/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/QCT88G/resources/NRO_NC_Voting_Present_UZgINvY.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/QCT88G/resources/NRO_NC_Voting_Presen_potZ2Cp.pptx | video: https://ripe91.ripe.net/media/videos/ulka-athale_nro-nc-elections_main_20251020-142733.mp4
During this RIPE Meeting, elections for the Number Resource Organization's Numbers Council (NRO NC) will take place. We will briefly describe the election process to you.

### Welcome from the RIPE Programme Committee
Speakers: Massimiliano Stucchi , PC Chair
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/M9HTCN/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/M9HTCN/resources/RIPE91-PC_UHwUy9q.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/M9HTCN/resources/RIPE91-PC_oLh6hKK.key | video: https://ripe91.ripe.net/media/videos/massimiliano-stucchi_welcome-from-the-ripe-programme-committee_main_20251020-143334.mp4
Welcome from the RIPE Programme Committee

### A Day in the Life of IPv6 Scanning
Speakers: Yoshinobu Matsuzaki , Internet Initiative Japan Inc. (IIJ)
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/SSJQNA/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/SSJQNA/resources/ripe91-ipv6-scanning_n7RV00Q.pdf | video: https://ripe91.ripe.net/media/videos/yoshinobu-matsuzaki_a-day-in-the-life-of-ipv6-scanning_main_20251020-144158.mp4
It is well known that IPv4 public addresses are routinely scanned. But what about IPv6? Researchers have already studied on methods to efficiently scan based on hint information, and in fact, such scanning is taking place. In this presentation, I will share observations of these scans within end-user networks and insights.

### gNMI and you: The death of SNMP was greatly exagerated
Speakers: Tom Strickx , Cloudflare
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/8/X7N8NC/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/X7N8NC/resources/gNMI_Talk_RIPE_AUJo4zH.pdf | video: https://ripe91.ripe.net/media/videos/tom-strickx_gnmi-and-you-the-death-of-snmp-was-greatly-exagerated_main_20251020-150134.mp4
Network observability and monitoring is an important responsibility of network operators. As an industry, we had settled on using SNMP as a protocol, with rrdtool to draw pretty lines. This has been changing though. New methods for observing your network have started popping up. One of those is gNMI. In this talk I'll briefly introduce gNMI, compare it with SNMP, and then go into deployments, and pitfalls that will come up. At the end, folks will hopefully have a better understanding of the evolving observability ecosystem, and be able to decide whether or not gNMI is the right call for their network.

## Plenary - Main Room (Tue, 14:00)

### The BGP Clock and the BGP Observatory: Hunting Stuck Routes
Speakers: Antonis Chariton , Cisco
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/19/87WNTB/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/87WNTB/resources/RIPE91_-_Observatory_5R1avlF.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/87WNTB/resources/RIPE91_-_Observatory_vUkJEcP.pptx | video: https://ripe91.ripe.net/media/videos/antonios-chariton_the-bgp-clock-and-the-bgp-observatory-hunting-stuck-routes_main_20251021-140237.mp4
At RIPE 89 we attempted to study and quantify the impact of stuck BGP routes across the Internet. We proposed a new method that allowed for better understanding of the situation, and it allowed pattern studying over longer time periods. This year we return with an even better, the new BGP Clock, as well as an automated tool that analyzes the results within minutes.

### Getting 1+ Tbps from an x86 server
Speakers: Branimir Rajtar , 5x9 Networks
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/19/QFTE87/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/QFTE87/resources/RIPE91_1Tbps_Branimir_JaVg5wW.pdf | video: https://ripe91.ripe.net/media/videos/branimir-rajtar_getting-1-tbps-from-an-x86-server_main_20251021-142824.mp4
We present how a virtual Broadband Network Gateway surpassed 1 Tbps on a single commodity server. By combining a control-and-user-plane separation with careful datapath tuning and continuous performance profiling, throughput grew seven-fold—from 160 Gbps to 1.2 Tbps—without specialised hardware. The talk outlines the optimisation waves, explains why shifting from many small virtual machines to one large instance unlocks efficiency, and distils practical lessons for operators seeking carrier-scale capacity while keeping costs and power per gigabit low.

### PON in the Datacenter: Hyperscale for Management and Console
Speakers: Mike Joseph , Meta
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/19/LVTBYA/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/LVTBYA/resources/RIPE_talk__PON_in_the_XJUogPt.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/LVTBYA/resources/RIPE_talk__PON_in_the_C4EG6bG.pdf | video: https://ripe91.ripe.net/media/videos/mike-joseph_pon-in-the-datacenter-hyperscale-for-management-and-console_main_20251021-145654.mp4
We share our novel approach to datacenter management connectivity using Passive Optical Network (PON) technology. Traditionally used in residential and SMB ISP access, PON offers flexibility, scale, and efficiency benefits for management and console services in Meta's hyperscale datacenters. This talk explores the rationale behind adopting PON, includes a brief overview of its fundamentals, and dives into Meta's implementation. We also discuss how we manage the whole system using our automation tools, including the end-to-end lifecycle management, starting from barcode scanning of PON assets as they enter Meta datacenters.

## RIPE NCC Services - Main Room (Wed, 14:00)

### Draft Activity Plan and Budget 2026
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/33/ENAR8C/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ENAR8C/resources/RIPE_91_Draft_Activit_QW3Srwp.pdf | video: https://ripe91.ripe.net/media/videos/hans-petter-holen_draft-activity-plan-and-budget-2026_main_20251022-140555.mp4
A straightforward run-through of the key points in the document as usual. The presentation ends with a discussion on the document itself and activity planning process more generally. It asks if there is more we could be doing to help members give feedback on our activities – in light of the fact that we’ll be redesigning the document at the start of the new strategy cycle.

### Panel: AI and the RIPE NCC
Speakers: Eleonora Pedridou , RIPE NCC Gabor de Wit , RIPE NCC Antony Gollan , RIPE NCC Robert Kisteleki , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/33/P8BNJX/ | video: https://ripe91.ripe.net/media/videos/eleonora-pedridou_panel-ai-and-the-ripe-ncc_main_20251022-142912.mp4
Moderator : János Zsakó An open and exploratory discussion on how artificial intelligence may – or may not – start to impact the RIPE NCC’s work. With staff from different areas of the organisation, the session will share some of our current thinking (and invite perspectives from the audience) on the implications that the use of AI has for our services and mission in the years ahead.

### RIPE NCC Strategy 2027-2031
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/33/J77JY7/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/J77JY7/resources/RIPE_NCC_Strategy_202_WpeioWD.pdf | video: https://ripe91.ripe.net/media/videos/hans-petter-holen_ripe-ncc-strategy-2027-2031_main_20251022-151813.mp4
A brief high-level overview of the draft strategy and also pointing people to the Strategy BoF on the Thursday evening.

## Address Policy - Main Room (Thu, 14:00)

### 2024-02: IPv6 Initial Allocations /28 and extension to /28
Speakers: Jordi Palet Martinez , The IPv6 Company Rinse Kloek
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/43/E8MVFH/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/E8MVFH/resources/RIPE91-ipv6wg-202402_5qOulMC.pdf | video: https://ripe91.ripe.net/media/videos/jordi-palet-martinez_2024-02-ipv6-initial-allocations-28-and-extension-to-28_main_20251023-140033.mp4
Updated version presentation for discussion of the policy proposal 2024-02 (IPv6 Initial Allocations /28 and extension to /28)

### 2025-01 2.0: ASN assignment criteria revisited
Speakers: Urban Suhadolnik , None Tobias Fiebig
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/43/PJKSWV/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/PJKSWV/resources/RIPE_2025-1_ver_2_kTqL9AE.pdf | video: https://ripe91.ripe.net/media/videos/urban-suhadolnik_2025-01-20-asn-assignment-criteria-revisited_main_20251023-141316.mp4
A new version of RIPE policy proposal 2025-01, "ASN assignment criteria revisited" is now available for discussion. Following the last round of discussion, this proposal has been updated and it is now at version 2.0.

### 2024-01: Revised IPv6 PI Assignment Policy
Speakers: Tobias Fiebig Clara Wade
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/43/N7MVYE/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/N7MVYE/resources/Revised_IPv6_PI_Assig_tx9ggww.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/N7MVYE/resources/Revised_IPv6_PI_Assi_GsBBxqG.pptx | video: https://ripe91.ripe.net/media/videos/tobias-fiebig_2024-01-revised-ipv6-pi-assignment-policy_main_20251023-144638.mp4
A new version of RIPE policy proposal 2024-01 "Revised IPv6 PI Assignment Policy" is now available for discussion. Following the last round of discussion, this proposal has been updated and it is now at version 2.0.

## IoT - Side Room (Thu, 14:00)

### Introduction & Housekeeping
Speakers: Peter Steinhaeuser
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/44/XV3MBK/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/XV3MBK/resources/RIPE-91-IoT-Slides_Op_27zYSdp.pdf | video: https://ripe91.ripe.net/media/videos/peter-steinhaeuser_introduction-housekeeping_side_20251023-140040.mp4
Welcome and introduction for the IoT Working Group Session.

### Cyberattack Observation Using IoT Honeypots at Yokohama National University
Speakers: Takayuki Sasaki
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/44/QBTJJJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/QBTJJJ/resources/RIPE91-XPOT-3_aav6FCr.pdf | video: https://ripe91.ripe.net/media/videos/takayuki-sasaki_cyberattack-observation-using-iot-honeypots-at-yokohama-national-university_side_20251023-140444.mp4
We developed X-POT, an adaptive HTTP honeypot that emulates a wide range of IoT devices using collected WebUI data. Our analysis pipeline combines rule-based detection and LLM-assisted automatic classification to identify new exploits and targeted devices. Through long-term operation, we captured the entire lifecycle of IoT exploits, from their emergence to decline. We also observed zero-day attacks and campaigns exploiting IoT and industrial systems such as solar power monitors. The collected data is released as a public dataset for collaborative cybersecurity research.

### IPv6’s Unintended Fingerprints: Extracting Insights from EUI-64
Speakers: Bart Batenburg , Work was done at University of Twente, currently working at Novoserve
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/44/YARYXG/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/YARYXG/resources/Slides_Bart_Batenburg_fsXUDuj.pdf | video: https://ripe91.ripe.net/media/videos/bart-batenburg_ipv6s-unintended-fingerprints-extracting-insights-from-eui-64_side_20251023-142355.mp4
The default method of Stateless Address Autoconfiguration (SLAAC) in IPv6 is EUI-64, which generates the Interface Identifier (the last 64 bits of an address) using a device’s MAC address. This approach results in a consistent Interface Identifier across different networks, allowing devices,and by extension their users, to be tracked. To mitigate this privacy risk, Privacy Extensions have been introduced to randomize the Interface Identifier. However, like many technologies on the internet, adoption is inconsistent, and many devices continue to use EUI-64, either exclusively or alongside Privacy Extensions. While earlier research has highlighted the privacy and security issues of EUI-64, little work has been done to understand the scale of its continued use or to explore the potential value of the exposed MAC addresses. This study investigates what types of devices still use EUI-64-derived addresses and what information can be extracted from them. We examine EUI-64 usage across three environments: the local IoT Lab, our university network, and the national research and education network (NREN) SURF. In the IoT Lab, we actively scanned for IPv6-capable devices using addresses we generated from their MACs. At the university, we analysed historical snapshots of router NDP tables. From SURF, we obtained EUI-64 suffixes from flow-level data. After extracting MAC addresses from the EUI-64 IPv6 addresses, we identified the associated manufacturers and examined how MAC addresses are structured. Using clustering algorithms like DBSCAN and statistical measures such as entropy, we discovered that some vendors, such as TP-Link, appear to generate MAC addresses in predictable sequences, suggesting sequential assignment practices. Our findings demonstrate that it is possible to detect patterns in MAC addresses by analysing EUI-64 IPv6 addresses. These patterns can potentially be used to accelerate the discovery of similar devices on the IPv6 side of the Internet, offering new opportunities for measurement and classification but also underscoring the importance of privacy-preserving address configuration.

### Beyond the Hype: Investigating Matter Standard’s Security and Privacy
Speakers: Andrew Losty , PhD student at UCL (University College London) Dept Electronic and Electrical Engineering
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/44/E3DKS7/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/E3DKS7/resources/RIPE91-Matter-Securit_3dpzpXH.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/E3DKS7/resources/RIPE91-Matter-Securi_JLxqPWR.pptx | video: https://ripe91.ripe.net/media/videos/andrew-losty_beyond-the-hype-investigating-matter-standards-security-and-privacy_side_20251023-144302.mp4
Matter, is a smart-home connectivity standard developed by the Connectivity Standards Alliance with Apple, Google, Amazon, and Samsung along with over 26o other vendors. It promises secure, interoperable IoT communication. This study examines Matter’s architecture—including its IPv6-based transport, Thread and Wi-Fi integration, device attestation, and certificate-based onboarding—and its interaction with existing ecosystems. The presentation critically assesses Matter’s end-to-end encryption, trust fabrics, and privacy mechanisms By analyzing these technical foundations, we explore Matter’s security and privacy claims.

### The Cyber Resilience Act: Current Status and Next Steps
Speakers: Anna Maria Mandalari , University College London
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/44/QEPU3K/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/QEPU3K/resources/Mandalari_RIPE91_21q7hb4.pdf | video: https://ripe91.ripe.net/media/videos/anna-maria-mandalari_the-cyber-resilience-act-current-status-and-next-steps_side_20251023-151724.mp4
This talk provides an overview of the progress made so far in developing standards to support the implementation of the EU Cyber Resilience Act, with a focus on the IoT ecosystem. It summarizes the ongoing work and achievements to date and highlights how the RIPE community can contribute expertise, operational experience and technical input to ensure that the emerging standards reflect real-world network practices and support a secure, resilient and interoperable Internet infrastructure.

### Closing
Speakers: Peter Steinhaeuser
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/44/TEQUHG/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/TEQUHG/resources/RIPE-91-IoT-Slides_Cl_Joq2ZKl.pdf | video: https://ripe91.ripe.net/media/videos/peter-steinhaeuser_closing_side_20251023-153125.mp4
RIPE IoT WG Session Closing

## Plenary - Main Room (Mon, 16:00)

### PQC for the RPKI
Speakers: Dirk Doesburg , Radboud University / SIDN Labs
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/10/7NJSVS/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/7NJSVS/resources/pqc-rpki-ripe91_m6SZgmM.pdf | video: https://ripe91.ripe.net/media/videos/dirk-doesburg_pqc-for-the-rpki_main_20251020-160112.mp4
The RPKI currently relies on RSA signatures, which are vulnerable to attacks by powerful quantum computers. While much research is done on post-quantum cryptography (PQC) and its application in protocols like TLS and DNSSEC, no such work has been done for the RPKI. My thesis lays the groundwork for a migration to post-quantum cryptography in the RPKI. We first show that reliance on the RPKI with insecure cryptography can be abused for severe attacks that are even more effective than original BGP attacks. We then evaluate which post-quantum signatures can be a suitable replacement for RSA in the RPKI. Next, we introduce the null scheme: a novel method to avoid redundant signatures and public keys that are present in every signed object in the RPKI. This can reduce the size and verification time of the RPKI (e.g. reducing the median ROA size from 4354 to 2295 bytes when using a hybrid of Falcon-512 and RSA-2048), largely making up for the performance cost of switching to post-quantum signatures. This is particularly useful when introduced together with post-quantum signatures, but also valuable independently. The null scheme is detailed in an Internet-Draft, with working prototypes in Krill and Routinator. Finally, we argue that the existing algorithm agility procedure (RFC6916) is impractical, and propose a simpler mixed-tree migration that (1) is not necessarily top-down, (2) requires no globally coordinated milestone days, and (3) uses simple key rollovers for individual CAs using the familiar RFC6489 key rollover procedure. In this approach, updated relying party software and trust anchors are distributed as soon as possible, while actual CA migrations can be delayed without problem. Our proof-of-concept implementation in Krill and Routinator demonstrates the feasibility of this approach. We publish this implementation to provide a starting point for further research and testing.

### Monitoring Root DNS Prefixes
Speakers: Lefteris Manassakis , Cisco
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/10/BLMLT3/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/BLMLT3/resources/Monitoring_Root_DNS_p_kXsc6Od.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/BLMLT3/resources/Monitoring_Root_DNS__6KqCOv0.pptx | video: https://ripe91.ripe.net/media/videos/lefteris-manassakis_monitoring-root-dns-prefixes_main_20251020-163206.mp4
Given BGP's inherent vulnerabilities, our team began monitoring critical Internet infrastructure for potential BGP origin hijacks. Specifically, in January 2023, we started using Code BGP to monitor root DNS prefixes. Root DNS servers are the authoritative name servers for the DNS root zone. We chose to monitor the BGP prefixes corresponding to the IP addresses of these servers for two main reasons: First, root DNS servers sit at the top of the global DNS hierarchy and represent critical Internet infrastructure that must be protected. Second, root DNS prefixes are typically heavily anycasted. We reasoned that any potential BGP anomaly affecting these prefixes might go largely unnoticed, since anycast minimizes the impact on the data plane, making it minimal or even negligible. In this presentation, we will provide details about the BGP anomaly events we have detected over the past 2.5 years involving the root DNS prefixes, including estimations of their impact on the data plane.

### Evolution of Measurement Lab platform with Host Managed deployments
Speakers: Simone Basso , Measurement Lab
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/10/X38DTU/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/X38DTU/resources/2025-10-20-mlab-ripe9_dNEcDKp.pdf | video: https://ripe91.ripe.net/media/videos/simone-basso_evolution-of-measurement-lab-platform-with-host-managed-deployments_main_20251020-165436.mp4
Measurement Lab (M-Lab) is the world’s largest open Internet measurement platform, providing open-source tools, globally distributed infrastructure, and publicly accessible datasets to advance transparency, research, and policy around Internet performance. M-Lab platform has over 500 servers across 40+ countries, hosting experiments such as NDT (network diagnostic tool), with all resulting data openly available through platforms like Google BigQuery. This presentation introduces the evolution of M-Lab’s platform through the new Host Managed Deployment model, which enables organizations to contribute physical or virtual servers—managed locally but running standardized M-Lab software—broadening M-Lab’s global footprint, reducing operational costs, and improving coverage in underrepresented regions such as the Middle East or Central Asia. We will discuss the technical and organizational requirements for participation, lessons from pilot deployments (e.g., RNP’s 27 servers in Brazil), and the roadmap toward general availability. Attendees will gain insight into how Host Managed Deployments open new opportunities for collaboration across research, industry, and public interest communities to measure and understand the Internet more effectively.

### Residential Proxies: A Double-Edged Sword for Network Research
Speakers: Christoff Visser , IIJ - Research Lab
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/10/MPWF8D/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/MPWF8D/resources/Residential_Proxies_R_IGdiEPl.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/MPWF8D/resources/Resident_Proxies_RIPE_AbtR1bm.pdf | video: https://ripe91.ripe.net/media/videos/christoff-visser_residential-proxies-a-double-edged-sword-for-network-research_main_20251020-170222.mp4
Residential proxies offer an unprecedented perspective of the Internet, with multiple providers claiming access to over 150 million real end-user vantage points. Compared to active RIPE Atlas probes, even smaller proxy providers often offer orders of magnitude more vantage points, commonly exceeding 1 million, available for use by researchers and enterprises. This raises critical questions: How are these vantage points obtained? More importantly, can we be certain that end-users have explicitly consented to their devices being used as proxies? This presentation aims to stimulate discussion about residential proxy services, exploring how the unique research insights they provide should be balanced against the ethical uncertainties and security risks they introduce.

### A Farewell to ARPs - IPv6 resolved gateways
Speakers: Remco van Mook
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/10/Y8YVLE/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/Y8YVLE/resources/ipv6_resolved_gateway_68S55oI.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/Y8YVLE/resources/ipv6_resolved_gateway_ZwyAD62.key | video: https://ripe91.ripe.net/media/videos/remco-van-mook_a-farewell-to-arps-ipv6-resolved-gateways_main_20251020-171800.mp4
From the draft I-D: This document requests the allocation of a new IPv4 special-purpose address from the IANA IPv4 Special-Purpose Address Registry. The proposed address, 192.0.0.11/32, is intended to serve as a signal to IPv4 hosts in IPv6-only networks that the link-layer resolution for the default gateway should be derived from the IPv6 default gateway learned via IPv6 Router Advertisements and Neighbor Discovery. This approach enables IPv4 communication without requiring IPv4 subnets or the use of ARP. It maintains backward compatibility with existing IPv4 host software that expects a default gateway IP address, while avoiding the need to implement legacy link-layer protocols. Importantly, this method does not require tunneling or translation. IPv4 packets remain fully native and unaltered, which simplifies deployment and ensures minimal disruption across existing infrastructure. While it's unlikely that any modern host or gateway would be unable to process a native IPv4 packet, that doesn’t mean we cannot evolve the internal mechanics of next-hop resolution.

## MAT - Main Room (Tue, 16:00)

### Network Measurement in the Dark
Speakers: Geoff Huston , APNIC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/22/DGX8XV/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/DGX8XV/resources/2025-10-21-darknetwor_R3K3kvE.pdf | video: https://ripe91.ripe.net/media/videos/geoff-huston_network-measurement-in-the-dark_main_20251021-160357.mp4
I want to highlight the amazing transformation that has happened over the past 15 years or so that has resulted in most of the network traffic being shrouded in encryption, and what this means to measurement activities.

### Disrupting the Internet in the name of copyright: An Italian Story
Speakers: Raffaele Sommese , University of Twente
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/22/WK3AQH/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/WK3AQH/resources/RIPE91_-_Piracy_Shiel_HveKWZg.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/WK3AQH/resources/RIPE91_-_Piracy_Shie_Pyv7eW1.pptx | video: https://ripe91.ripe.net/media/videos/raffaele-sommese_disrupting-the-internet-in-the-name-of-copyright-an-italian-story_main_20251021-162559.mp4
In the fight against illegal football streaming, Italy introduced Piracy Shield, a platform through which copyright holders can notify the national regulator (AGCOM), which in turn orders ISPs to block infringing resources -- such as IP addresses and Fully Qualified Domain Names (FQDNs) -- within 30 minutes. In this talk, we present the first investigation into the platform's real-world impact by reconstructing and analyzing its blocking activity. Our analysis shows that the platform causes significant collateral damage. Indiscriminate IP-level blocking has disrupted and continues to disrupt hundreds of legitimate, non-streaming websites. At the same time, the platform's effectiveness may have been undermined by streamers who evaded enforcement by migrating to new infrastructure and unfiltered IP address space. Based on these findings, we call on Italian authorities and policymakers to critically reconsider the platform's core blocking principles. The evidence suggests that its broad impact on legitimate services and the potential national security risks outweigh its intended benefits.

### An empirical evaluation of longitudinal anycast catchment stability
Speakers: Remi Hendriks , University of Twente
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/22/RQBH3N/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/RQBH3N/resources/anycast_stability_RIP_q1Xz8KX.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/RQBH3N/resources/anycast_stability_RI_fw0Yv8z.pptx | video: https://ripe91.ripe.net/media/videos/remi-hendriks_an-empirical-evaluation-of-longitudinal-anycast-catchment-stability_main_20251021-164229.mp4
Anycast is widely used to improve the availability and performance of, e.g., the DNS and content delivery networks. To use anycast one simply announces the same prefix from multiple points of presence (PoPs). BGP then takes care of routing clients to the ``nearest'' PoP. While seemingly simple, managing an anycast service is not without challenges. Factors outside operator control, such as remote peering and hidden MPLS tunnels, may route clients to suboptimal PoPs in terms of latency. To successfully manage anycast, operators map catchments: the set of prefixes that reach each PoP of a service. Due to the dynamic nature of inter-domain routing, catchments change over time. While earlier work has looked at catchment stability in the short term and in a coarse-grained manner, we lack a detailed view on catchment stability over time. Understanding this is crucial for operators as it helps schedule catchment measurements and plan interventions using traffic engineering to redistribute traffic over PoPs. In this work, we put long-term catchment stability on an empirical footing. Using an industry-grade anycast testbed with 32 globally distributed PoPs, we continuously map catchments for both IPv4 and IPv6 over a 6-month period and study catchment stability at different timescales, ranging from days to weeks and months. We show catchments are very stable in the short term, with 95% of prefixes routing to the same PoP on a one-week scale, and over 99% on a day-by-day basis. We also show, however, that sudden routing changes can have a major impact on catchments. Based on our longitudinal results, we make recommendations on the frequency with which to perform catchment analysis.

### Querying the DFZ
Speakers: Ties de Kock , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/22/3Q7AUL/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/3Q7AUL/resources/20251020_querying_the_VpHijNI.pdf | video: https://ripe91.ripe.net/media/videos/ties-de-kock_querying-the-dfz_main_20251021-165631.mp4
RIPE RIS collects BGP data from collectors worldwide, providing visibility into routing dynamics. While this data powers RIPEstat and various third-party applications, operators and researchers often need analyses beyond what standard tools offer. On the other hand, using raw data MRT directly, is challenging. It is computationally intensive and requires custom parsing scripts. To cover this gap we are now publishing RIPE RIS data as indexed Parquet files, covering recent BGP RIBs and updates. As a result you can query routing data using SQL or datascience tools rather than using MRT parsers. An analysis that previously took 10+ minutes can now be done in seconds. This approach has already proved valuable for our internal operations. When the Baltic Sea cables were damaged, we could quickly explore the BGP impact. When analysis the effects of the Iberian Peninsula power outage on BGP, we could investigate effects within minutes instead of hours. This new data makes using route collector data much faster and much more accessible. This presentation will introduce the files and show how to use these new capabilities through practical examples. I'll show how network operators can analyse bview/RIB/bgp snapshot data and BGP updates this way - from investigating routing over time, to analysing stuck prefixes, or analysing the upstreams of a network as seen by collectors. This data removes the traditional barriers of MRT processing, and makes BGP data analysis much more accessible, using much more tools and skills.

### Who is "really" running email?
Speakers: Willem Toorop , NLnet Labs
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/22/FF88V7/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/FF88V7/resources/who-is-really-running_RBdlfJO.pdf | video: https://ripe91.ripe.net/media/videos/willem-toorop_who-is-really-running-email_main_20251021-171201.mp4
Email on the internet was originally designed in a decentralized fashion. However this decentralized deployment may not be evenly distributed. There is a supposed perception that email services are increasingly serviced on hosted digital infrastructure, which are largely managed by a small number of parties. GMail, Outlook, iCloud Mail, Yandex Mail, and other brand names are supposedly increasingly responsible for email services on the internet. Earlier studies looking into centralization and consolidation of email on the internet, were based on analysis of the MX records (referring to SMTP servers) in use by lists of names, such as the Tranco list or zone files of TLDs. These studies give good insight into how many domains are serviced by email providers, but do not reveal anything about whether those providers are actually used and to what extent. For example the cloud services provider OVH is the most prevalent email provider in the .fr zone, but an MX record for OVH is automatically deployed when registering a domain name with them, even if that name will only be used for web. To get better insight into how much of those email providers are really being used, one would need access to the query volume for those MX records. In this talk we try to provide better insight into the actual usage of those email service providers, by analysis of the MX queries at one of the pops of the popular public Quad9 resolver (9.9.9.9), with which we have a partnership for this study.

## Security - Side Room (Tue, 16:00)

### Recent List Discussion
Speakers: Brian Nisbet
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/21/TYPRFW/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/TYPRFW/resources/Security_WG_Slides_Re_zFd5MPQ.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/TYPRFW/resources/Security_WG_Slides_R_1y74Y45.pptx | video: https://ripe91.ripe.net/media/videos/brian-nisbet_recent-list-discussion_side_20251021-160331.mp4
Recent List Discussion

### Policies
Speakers: Brian Nisbet
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/21/JEDGK7/ | video: https://ripe91.ripe.net/media/videos/brian-nisbet_policies_side_20251021-160418.mp4
Current policies

### Reflections on the Europol Cybercrime Conference
Speakers: Brian Nisbet
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/21/NXNJPY/ | video: https://ripe91.ripe.net/media/videos/brian-nisbet_reflections-on-the-europol-cybercrime-conference_side_20251021-160532.mp4
Reflections on the Europol Cybercrime Conference

### The File That Contained the Keys Has Been Removed: An Empirical Analysis of Secret Leaks in Cloud Buckets and Responsible Disclosure Outcome
Speakers: Yury Zhauniarovich , TU Delft
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/21/U7YLJ8/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/U7YLJ8/resources/20251021_ripe91_open__v2t77Nx.pdf | video: https://ripe91.ripe.net/media/videos/yury-zhauniarovich_the-file-that-contained-the-keys-has-been-removed-an-empirical-analysis-of-secr_side_20251021-163023.mp4
As cloud adoption accelerates, the operational risks associated with misconfigured storage services like AWS S3, Google Cloud Storage, and Azure Blob Storage continue to grow. One critical but often overlooked threat is the leakage of sensitive secrets -- such as API keys, database credentials, and access tokens -- through publicly exposed configuration files. In this talk, we present findings from a large-scale scan of publicly accessible cloud buckets, where we identified 215 real-world cases of exposed secrets. These leaks granted unauthorized access to critical infrastructure, third-party APIs, and internal services, illustrating how simple misconfigurations can lead to severe operational and reputational damage. Within this presentation, we will walk through the types of files and secrets most commonly exposed, demonstrate how they were detected non-intrusively, and share insights into the incident response patterns across different organizations. Importantly, we will discuss our coordinated disclosure efforts, which led to the remediation of 95 cases, and highlight the challenges in driving action even after vulnerabilities are reported. This session will equip operators, security teams, and cloud engineers with practical recommendations to audit their own storage environments, avoid common pitfalls, and build more resilient disclosure and remediation workflows.

### RegCheck: A Real-Time Approach for Flagging Potentially Malicious Domain Name Registrations
Speakers: Thomas Daniels , DNS Belgium & KU Leuven
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/21/K3L3HH/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/K3L3HH/resources/ripe-regcheck-present_TsImrUD.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/K3L3HH/resources/ripe-regcheck-presen_O6urpOp.pptx | video: https://ripe91.ripe.net/media/videos/thomas-daniels_regcheck-a-real-time-approach-for-flagging-potentially-malicious-domain-name-re_side_20251021-165137.mp4
Miscreants use domain names for malicious purposes such as phishing websites or fake webshops. Reactive approaches such as blocklists play an important role in fighting such abuse but have limitations, namely that the domains are typically only included in such a list after abuse has been reported (e.g., there may already be some victims). We propose RegCheck, a system designed to proactively flag suspicious domains at registration time. The core of RegCheck is a machine learning classifier that assesses the risk that the domain name will be used for malicious purposes based on characteristics known at the time of registration. Based on this assessment, it flags some registrations and requires them to undergo additional verification prior to the domain name being activated. The system has been developed collaboratively between SIDN (.nl) and DNS Belgium (.be) and has been deployed as a real-time system at the .be registry since March 2024. Since its deployment, the registry has witnessed a decrease in the number of .be domain name registrations that have been revoked for breaching the terms and conditions, indicating a decline in the number of active malicious registrations. This talk will be based on the ACM KDD 2025 paper "RegCheck: A Real-Time Approach for Flagging Potentially Malicious Domain Name Registrations".

### Agenda for RIPE 92
Speakers: Brian Nisbet
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/21/FT3V9B/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/FT3V9B/resources/Security_WG_Slides_R9_jz7Yur2.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/FT3V9B/resources/Security_WG_Slides_R_kmxVAbv.pptx | video: https://ripe91.ripe.net/media/videos/brian-nisbet_agenda-for-ripe-92_side_20251021-171605.mp4
Agenda for RIPE 92

## RIPE Community Plenary - Main Room (Thu, 16:00)

### RIPE Chair Team Update
Speakers: Mirjam Kühne , RIPE Chair
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/46/ZBTFVG/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZBTFVG/resources/RIPE_Chair_Team_Updat_kfrKuwr.pdf | video: https://ripe91.ripe.net/media/videos/mirjam-kuhne_ripe-chair-team-update_main_20251023-160229.mp4
RIPE Chair Update

### The New RIPE Fellowship: Bringing New Voices That Stay!
Speakers: Laura Lorenzo , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/46/Z77P3Z/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/Z77P3Z/resources/RIPE_91__RIPE_Fellows_p2T9FYN.pdf | video: https://ripe91.ripe.net/media/videos/laura-lorenzo_the-new-ripe-fellowship-bringing-new-voices-that-stay_main_20251023-161827.mp4
The RIPE Fellowship was introduced at RIPE 74 with the goal of bringing new voices from across the service region into the community by removing financial barriers to attendance at RIPE Meetings. Eight years on, we’re redesigning the programme with a focus on long-term engagement. In this presentation we will share the changes we have introduced and we will share further instructions for the application process.

### RIPE Community at WHY2025
Speakers: Ondřej Caletka , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/46/KMMEQA/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/KMMEQA/resources/RIPE_Community_at_WHY_9VsBdQ5.pdf | video: https://ripe91.ripe.net/media/videos/ondrej-caletka_ripe-community-at-why2025_main_20251023-163030.mp4
In August of 2025, a hacker camp called WHY2025 took place in the Netherlands. A group of RIPE NCC employees and fellows ran a RIPE community village , networking face to face with the visitors of the camp, trying to make them aware that it is actually the RIPE community that makes the rules about the Internet, hoping to bring more newcomers to the RIPE community.

### 10 years at the RIPE community - The benefits of collaboration
Speakers: Vladislav Bidikov , Faculty of computer science and engineering / IXP.mk
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/46/ZNVQLQ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZNVQLQ/resources/RIPE_91-DRAFT-v3_Comm_WiSDBtp.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZNVQLQ/resources/RIPE_91-Community_Wo_WxzAMOU.pptx | video: https://ripe91.ripe.net/media/videos/vladislav-bidikov_10-years-at-the-ripe-community-the-benefits-of-collaboration_main_20251023-164226.mp4
This will show my work in the RIPE community in the last 10. The presentation is to inspire young talent to work more in the community.

### IANA Updates: Numbers, Broader Functions, and Strategic Alignment
Speakers: Marilia Hirano , ICANN
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/46/3RJSF3/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/3RJSF3/resources/RIPE_91_-_IANA_Update_GNNiMWk.pdf | video: https://ripe91.ripe.net/media/videos/marilia-hirano_iana-updates-numbers-broader-functions-and-strategic-alignment_main_20251023-165204.mp4
This session will provide the RIPE NCC community with an update on IANA’s current priorities and how they align with the IANA 2030 strategy. Beginning with a focus on the services IANA provides to the numbers community, the discussion will place those services in the broader context of IANA’s work across names, numbers, and protocols. The session will highlight policy-driven activities, high-visibility technical projects, and how these short-term initiatives contribute to long-term service excellence, resilience, and trust.

### NRO NC: report from the ICP-2 BoF
Speakers: Herve Clement , Orange SA / ASO AC Andrei Robachevsky , Global Cyber Alliance/NRO NC Constanze Buerger
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/46/QGMUHQ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/QGMUHQ/resources/Outcomes_of_the_RIPE__7QEWONC.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/QGMUHQ/resources/Outcomes_of_the_RIPE_GCWnEsa.pptx | video: https://ripe91.ripe.net/media/videos/herve-clement_nro-nc-report-from-the-icp-2-bof_main_20251023-170506.mp4
The RIPE NRO NC representatives will report during this talk on the outputs of the Monday's BoF "Updating ICP-2: Discussing the second draft RIR Governance Document"

## BoF - Main Room (Mon, 18:00)

### Updating ICP-2: Discussing the second draft RIR Governance Document
Speakers: Herve Clement , Orange SA / ASO AC Andrei Robachevsky , Global Cyber Alliance/NRO NC Constanze Buerger
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/57/P7CTZ7/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/P7CTZ7/resources/RIPE_91_Updating_ICP-_c6YohJb.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/P7CTZ7/resources/RIPE_91_Updating_ICP_eSMacZd.pptx | video: https://ripe91.ripe.net/media/videos/herve-clement_updating-icp-2-discussing-the-second-draft-rir-governance-document_main_20251020-180153.mp4
The RIR community consultation on the second draft of the RIR Governance Document, intended to replace ICP-2, will be open during RIPE 91. We would like to hear the RIPE community’s feedback on the next draft of this important document. The RIR system faces new challenges as the Internet landscape evolves, and it is essential that we, as a community, ensure that this system is underpinned by sound governance structures and values. During this BoF, we will present the second draft and share an overview of how community feedback on the first draft was incorporated. The aim is to dedicate the majority of the session to hearing perspectives and voices from the RIPE community to help shape this draft. We will also try to answer any questions participants might have. Background Information ICP-2 is the Internet Coordination Policy developed in 2001 through the Address Supporting Organization (ASO), with the assistance of APNIC, ARIN, and RIPE NCC outlining the criteria for the recognition of new Regional Internet Registries (RIRs). The first version of the draft “RIR Governance Document” was presented at a BoF during RIPE 90. The extensive discussions that took place in the BoF were valuable for the NRO NC as input while working on the second draft. Proposed Agenda: 1. A bit of a background: From the ICP-2 to the second draft of the RIR Governance document - a short overview of the differences between the versions and the rationale for the changes 2. Presentation of the community input received during the consultation on the first draft of the RIR Governance Document 3. Open discussion

## Diversity, Equity and Inclusion in Tech - Main Room (Tue, 18:00)

### Welcome to the Diversity in Tech session
Speakers: Denesh Bhabuta
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/24/R3NE3T/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/R3NE3T/resources/DeneshBhabuta-DEI-in-_SFEXQin.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/R3NE3T/resources/DeneshBhabuta-DEI-in-_CWWLQ2J.key | video: https://ripe91.ripe.net/media/videos/denesh-bhabuta_welcome-to-the-diversity-in-tech-session_main_20251021-180134.mp4
Theme: Being Human in Tech Technology advances through human ingenuity, yet the tech industry's greatest asset isn't just innovation or efficiency - it's the diverse minds driving both forward. This session explores how embracing varied perspectives across gender, culture, background, and experience leads to meaningful impact. Through personal stories and reflections, our two speakers will share their journeys and lived experiences within their careers, exploring the obstacles encountered, victories achieved, and wisdom gained whilst navigating and reshaping a fast-moving industry. Their perspectives highlight the power of diversity not just as a value, but as a driving force for innovation and connection in the tech world. Attendees will leave understanding how different lived experiences translate into better outcomes and why cultivating truly inclusive environments remains essential for the industry's continued evolution and relevance.

### From Migration to Leadership: How life shaped an inclusive Creative Agency
Speakers: Maribel Aburto
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/24/ZVPEBK/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZVPEBK/resources/From_Migration_to_Lea_lApBKa1.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/ZVPEBK/resources/From_Migration_to_Le_SCyafuo.pptx | video: https://ripe91.ripe.net/media/videos/maribel-aburto_from-migration-to-leadership-how-life-shaped-an-inclusive-creative-agency_main_20251021-180639.mp4
This session explores the intersection between personal experience and inclusive business leadership. Maribel’s story begins with a move across continents: from Chile to the US and then New Zealand, and later to Ireland, where she built her creative agency, CREATIVA, from the ground up. Facing the challenges of being a woman of colour, a mother, and an entrepreneur in a competitive industry, and struggling with language barriers, she redefined what success and leadership could look like. Through real examples from her 11-year journey leading CREATIVA, Maribel will highlight: How diverse life experiences can shape a more inclusive and empathetic leadership style The benefits and realities of building remote, flexible teams led by women of colour and working mums The cultural challenges that small creative businesses face today, and how inclusion and collaboration can be key to resilience Simple, actionable ideas for leaders who want to make inclusion part of their everyday practice. The session combines storytelling with reflection and takeaways, inviting open discussion at the end for others to share experiences, perspectives, and ideas around DEI in their own contexts.

### Some lived career experiences - a personal journey towards duality
Speakers: Keith Mitchell , Individual
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/24/FYNFZJ/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/FYNFZJ/resources/Mitchell-RIPE91-Diver_DZLRBP7.pdf | slides: https://pretalx.ripe.net/media/ripe91/submissions/FYNFZJ/resources/RIPE91-Diversity_QDJEboc.pptx | video: https://ripe91.ripe.net/media/videos/keith-mitchell_some-lived-career-experiences-a-personal-journey-towards-duality_main_20251021-183216.mp4
I have been working in the Internet operations community for several decades, and actively involved in the RIPE community for most of that. While I'm aware that makes me very much part of the "old guard" that has long influenced and skewed our demographics, affairs, policies and culture, it's also been a journey of personal evolution and discovery as I bring some other perspectives. This presentation is a tale of that journey, with hopefully some experiences and insights that may be of value to others. Participation in the RIPE community has been an ongoing source of personal and professional development for me, and given me a safe place for self-discovery and -expression, enriched and supported by our uniquely welcoming community. Beyond being a member of the "old guard", I identify as "Bi-Gendered" and a feminist, and bring some perspectives of representing and realizing that whole self in a professional environment. I also have some (hopefully constructive) insights on participation in our community as a hearing impaired person, an immigrant, and on attitudes towards aging in the wider tech industry.

## BoF - Main Room (Thu, 18:00)

### ADoT/ADoQ: Deployment Collaboration
Speakers: Babak Farrokhi , Director of Operations @ Quad9 Sara Dickinson , Sinodun IT
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/48/YTLL37/ | slides: https://pretalx.ripe.net/media/ripe91/submissions/YTLL37/resources/adox-ripe-91_VQ0aCFq.pdf | video: https://ripe91.ripe.net/media/videos/babak-farrokhi_adotadoq-deployment-collaboration_main_20251023-180112.mp4
This session is a follow-up to a well-attended side meeting held during IETF 123, which brought together resolver operators, authoritative operators, and software vendors to discuss the current state and future of encrypted DNS transport protocols (ADoT/ADoQ). The goal of this BoF is to continue that momentum by fostering direct collaboration between different parts of the DNS ecosystem. We aim to: Share deployment plans, experiments, and experiences with ADoT/ADoQ Identify interoperability or operational challenges that need community attention Explore areas where collaboration between vendors and operators can accelerate adoption Define potential next steps, joint experiments, or coordination mechanisms

## BoF - Side Room (Thu, 18:00)

### Shaping the RIPE NCC’s Strategic Direction
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe91.ripe.net/programme/meeting-plan/sessions/49/SZ8GB3/ | video: https://ripe91.ripe.net/media/videos/hans-petter-holen_shaping-the-ripe-nccs-strategic-direction_side_20251023-180242.mp4
This BoF will be an interactive session with the community to get their thoughts and ideas about where the RIPE NCC needs to go in the next 5-6 years. This is the last RIPE Meeting before we will arrive at a final five-year strategy, so getting clear input now on what the community wants to see from its Secretariat is crucially important so we can set the direction that will serve the needs of our community. The RIPE NCC will carry out consultations with its members and community in the run-up to the RIPE Meeting, and the output from these consultations will serve as the starting point for the conversation we want to have with the community about our strategic direction. Ahead of the RIPE Meeting, we will have published our draft strategy featuring our vision of where we want to be in 2031 and the strategic focus points that will help us get there. By that time, we will have conducted a survey that will ask members where they want to see the RIPE NCC focus in the coming years, and where they want the RIPE NCC to change in order to better serve their needs. At the BoF, Hans Petter Holen will present: - An overview of the draft strategy - Preliminary results from the survey - Specific questions that the RIPE community can give guidance to us on - An interactive Q&A where we discuss the future of the RIPE NCC and what the community wants to see from it The focus will be on hearing from our community, so we expect the presentation to last approx. 15 minutes with the majority of the session focused on what the community wants from its Secretariat.

