>>> HOW TO RUN THIS <<<
This is the digest prompt for ripe-93. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ripe-93.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ripe-93.md
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

Below is the program for RIPE 93 (operator). Read it and produce a digest
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
conference: RIPE 93
type: operator
source_url: https://ripe93.ripe.net/programme/meeting-plan/
generated: 2026-11-01
registry_key: ripe-93
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Tutorial - Main Room (Mon, 09:00)

### ASPA: the new protocol for improving BGP routing security
Speakers: Ondřej Caletka , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/117/Y87HT8/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/Y87HT8/resources/RIPE93-ASPA-tutorial_1fPdvkk.pdf | video: https://ripe93.ripe.net/media/videos/ondrej-caletka_aspa-the-new-protocol-for-improving-bgp-routing-security_main_20261026-090008.mp4
In the past it was believed that network operators should periodically download clear text data from the Internet and put them into the configuration of their routers to make routing more secure. RPKI is a technology to secure routing which employs proper cryptography. For years we have used it for Route Origin Authorization. In 2026, new feature of RPKI is being deployed: Autonomous System Provider Authorization. It complements existing Route Origin validation with a (partial) path validation: each Autonomous System can declare which autonomous systems are expected to provide transit services. Network operators validating ASPA can then drop routes coming via unauthorised providers. In this tutorial we will dive deeper into the principles of ASPA, show how to create ASPA objects for the ASNs you hold and how to properly configure validation in your routers. We will also cover how to troubleshoot ASPA validation failures.

## Tutorial - Side Room (Mon, 09:00)

### Digital Coherent Optics Tutorial
Speakers: Michel Lanners , LU-CIX
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/118/SEVGKR/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/SEVGKR/resources/RIPE93_DCO_Tutorial__Ehb0qFr.pdf | video: https://ripe93.ripe.net/media/videos/michel-lanners_digital-coherent-optics-tutorial_side_20261026-090035.mp4
This tutorial, co-presented with Sven Tron and Thomas Weible of Flexoptix and Florian Hibler of Arista, aims to open the world of digital coherent optics ("DCO") for those people who never used these types of optics. We will present the physical basis of operation for coherent optics, explain the different types, form factors and interfaces, in order to enable the audience to navigate spec sheets and catalogs for these types of optics, understand their use cases, and make the right choices in network equipment.

## Plenary - Main Room (Tue, 09:00)

### Expanding Routing Visibility at IXPs with BMP
Speakers: Thomas Holterbach , bgproutes.io
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/130/LLUPSG/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/LLUPSG/resources/RIPE_2026_c23luM9.pdf | video: https://ripe93.ripe.net/media/videos/thomas-holterbach_expanding-routing-visibility-at-ixps-with-bmp_main_20261027-085952.mp4
Route-server looking glasses already provide valuable visibility into routing at Internet Exchange Points (IXPs), either by querying route-server software directly, as Alice-LG does, or through dedicated BGP collection sessions. They help operators and participants inspect exchanged prefixes, troubleshoot connectivity issues, and better understand route-server activity. In this presentation, we introduce the BGP Monitoring Protocol (BMP) as an alternative and complementary approach to monitoring routing at IXPs. BMP can provide visibility into routes at multiple stages of the routing pipeline, including pre-policy, filtered, and non-best routes. It also provides detailed information about BGP peers and session state. Both BIRD and FRRouting can export BMP data when deployed as route servers. However, deploying BMP—particularly at large IXPs—still presents several challenges. How can we process and store the large volume of data exported through BMP? How should this data be made available efficiently? And how can we provide consistent access across different collection platforms and storage architectures? We discuss the roadmap that the community could follow to enable broader adoption of BMP-based monitoring at IXPs. Finally, we present the bgproutes.io IXP Explorer as a practical example of what BMP-based routing visibility at IXPs could look like in the future.

### RootViz: visualizing real-time monitoring of Root servers
Speakers: Giovane Moura , SIDN Labs and TU Delft
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/130/HLBDWR/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/HLBDWR/resources/Moura-20261027-RIPE9_3za26CI.pdf | video: https://ripe93.ripe.net/media/videos/giovane-moura_rootviz-visualizing-real-time-monitoring-of-root-servers_main_20261027-093205.mp4
We have recently built an open dashboard called Rootviz , which visualizes in real-time measurement data produced by all Ripe Atlas probes to the Root DNS servers. It allow users to visualize real-time reachability between the probes and each Root Server, for both IPv4 and IPv6. It complements DNSMON by two ways: using industry's default time-series visualization (Grafana) and by leveraging a different dataset from DNSMON: it uses data from all Atlas probes, and not only the robust anchors.

### Detecting and Characterizing Exposed BGP Routers​
Speakers: Shyam Krishna Khadka , University of Twente
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/130/RGPF9L/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/RGPF9L/resources/Exposed_BGP_routers__z76THOA.pdf | video: https://ripe93.ripe.net/media/videos/shyam-krishna-khadka_detecting-and-characterizing-exposed-bgp-routers_main_20261027-100325.mp4
RFC 7454 on BGP operations and security recommends that network operators restrict access to TCP port 179, which routers use to receive reachability messages from their peers. However, we identify 141,313 IP addresses that accept TCP connections and exchange OPEN messages, corresponding to 20,432 routers across 4,194 Autonomous Systems (ASes). This work presents a detailed insight into how we identified such routers, ASes, and routers' deployment roles as border and internal routers. Using an external SNMPv3 dataset, we further examine vendor distribution among exposed routers. With this presentation, we seek to raise awareness among network operators about such routers and to understand the reasons for such exposure.

## Connect - Main Room (Wed, 09:00)

### Opening and House Keeping
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/142/A9XNKT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/A9XNKT/resources/cat_connect-ripe93_f_5jW1vsC.pdf | video: https://ripe93.ripe.net/media/videos/na_opening-and-house-keeping_main_20261028-090007.mp4
Welcome Agenda RIPE 92 meeting notes

### RS-API - Accept announcments as legit as possible
Speakers: Evann DREUMONT , Breizh-IX Alarig Le Lay , Breizh-IX
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/142/9BLCQT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/9BLCQT/resources/slides-short_oFD7MzQ.pdf | video: https://ripe93.ripe.net/media/videos/evann-dreumont_rs-api-accept-announcments-as-legit-as-possible_main_20261028-090549.mp4
While accepting an announcement is pretty simple, checking if it is a legit one is way more difficult. You have to look up the Internet Routing Registry (IRR) to check if the route is contained in the AS-SET of the customer, check that the amount of routes announced is coherent (especially if the AS-SET contain another AS-SET that import the whole DFZ), and last but not least, check if the customer wants to be re-announced through the route server (RS). Sounds easy right? Well, while there is plenty of tools that do part of the jobs you still have work to do: PeeringDB is the source of trust, you should have all the information you need but only if it is up-to-date and accurate, nothing stops you from having 1M routes as max-pref. The awesome bgpq4 tool let you generate filters from the IRR, but you have no clue if the AS-cone is legit or not. You can add AS-OPENTRANSIT to your AS-SET, give it to the new IXP you want to connect to, and voilà. It is something you can do manually, however each time your customers update their networks, you also need to update your filters. If it seems feasible for a few customers, it definitely does not scale. This is why we have designed RS-API, a proxy around the tools that are already available. Leveraging real life data from BGP.tools and bgproutes.io , we are able to confront the PeeringDB data to the reality. Allowing us to have up to date and accurate filters.

### The End of Prefix Filtering
Speakers: James Bensley , Inter.link
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/142/G9TM8M/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/G9TM8M/resources/RIPE93_-_The_End_of__B5eWm0u.pdf | video: https://ripe93.ripe.net/media/videos/james-bensley_the-end-of-prefix-filtering_main_20261028-092052.mp4
The overhead of generating, deploying, and maintaining prefix filters for BGP edge filtering is high. It also places financial and operation costs on edge routers. Meanwhile, ROA coverage has been steadily growing for years. When can networks remove this overhead and simplify their operations, by removing prefix filtering completely? In this talk, data from various sources is pulled together to show that we have already reached the point in time when we can finally stop deploying IRR derived prefix filtering, and make the first major step towards only using RPKI derived data for edge filtering.

### InterLAN IX Lighthouse - Yet Another Network Automation Tool
Speakers: Andrei Dinu , InterLAN IX
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/142/PCYRUS/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/PCYRUS/resources/InterLAN_Lighthouse__LM4dPhn.pdf | video: https://ripe93.ripe.net/media/videos/andrei-dinu_interlan-ix-lighthouse-yet-another-network-automation-tool_main_20261028-095036.mp4
InterLAN IX wanted a member self-service portal with every network change checked, reversible and recorded on a network running Nokia SR OS routers and Arista EOS switches together. This talk explains the choices behind it. One request touches several routers, each with its own previewed configuration, a rollback timer and confirmation one router at a time; when safe recovery cannot be proven, a human takes over. The database owns intended state, so hand-made device changes surface as deviations and are never silently adopted. A digital twin built from production snapshots lets us rehearse changes, and an AI assistant with read-only tools writes reports and migration plans without touching configuration. We close with today's limits and what comes next.

### Building a global PeeringDB mirror
Speakers: Remco van Mook
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/142/F7L3T7/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/F7L3T7/resources/building_a_peeringdb_ExSd1eC.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/F7L3T7/resources/building_a_peeringdb_Jok7V2P.key | video: https://ripe93.ripe.net/media/videos/remco-van-mook_building-a-global-peeringdb-mirror_main_20261028-100539.mp4
Brief update on the pdbfe project - building a globally distributed peeringdb mirror

### Panel: A new API for PeeringDB
Speakers: James Bensley , Inter.link Leo Vegoda , PeeringDB Andy Clyde , The Internet Society Aaron Hughes Matt Parker
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/142/3WFD8G/ | video: https://ripe93.ripe.net/media/videos/james-bensley_panel-a-new-api-for-peeringdb_main_20261028-101221.mp4
James Bensely (Inter.Link), Andy Clyde (ISOC, Pulse), and Aaron Hughes (6Connect) will discuss PeeringDB's draft spec for a new API . It's designed to be served from multiple locations, support incremental sync, daily snapshots, and new efficient queries, like an exchange with its members. Matt Parker will be moderating the panel.

## Open Source - Side Room (Wed, 09:00)

### Beyond NIS2: Software Supply Chains and the Cyber Resilience Act (CRA)
Speakers: Barry O'Donovan , INEX
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/143/AHLDQR/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/AHLDQR/resources/2026-11_RIPE93_-_INE_QUxgndJ.pdf | video: https://ripe93.ripe.net/media/videos/barry-odonovan_beyond-nis2-software-supply-chains-and-the-cyber-resilience-act-cra_side_20261028-090638.mp4
As network operators, we are all familiar with NIS2 by now, with many of us being categorised as operators of essential or important entities. However, operational resilience is only half the equation - the EU’s Cyber Resilience Act (CRA) directly targets the software supply chain that powers our infrastructure. With mandatory vulnerability reporting obligations taking effect from September 2026, where does this leave the open-source ecosystem that we rely on every day? This presentation bridges the gap between NIS2 operator obligations and CRA software requirements. We explore how the CRA categorises open-source software, breaking down the critical distinction between Commercial OSS Manufacturers (subject to full product liability, CE marking, and fines) and Open-Source Software Stewards (non-profit foundations and industry associations operating under a light-touch regime). Using familiar ecosystem tools as real-world examples, we explain what ISP and IXP operators can legally expect from their upstream maintainers regarding Software Bills of Materials (SBOMs), vulnerability disclosures, and patch timelines. By the end of this talk, you should leave with a clear roadmap for auditing your open-source dependencies under NIS2, consuming standardised security feeds, and understanding your obligations if you publish tools for the community.

### BIRD on an Open Linux Switch: Mainline Linux, switchdev and Hardware L3 Offload
Speakers: Bruno Banelli , Novarq d.o.o.
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/143/WQNNDD/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/WQNNDD/resources/RIPE93-Banelli-BIRDT_8guDtE1.pdf | video: https://ripe93.ripe.net/media/videos/bruno-banelli_bird-on-an-open-linux-switch-mainline-linux-switchdev-and-hardware-l3-offload_side_20261028-093516.mp4
BIRD is widely used in the Internet routing community, but it usually runs on servers, virtual machines, or routers where the forwarding path is abstracted away by a network operating system or vendor-specific integration layer. This talk explores a different approach: running BIRD directly on an open Linux Ethernet switch, using the Novarq TACTICAL 1000 platform based on LAN969x switching silicon and mainline Linux switchdev. The goal is to evaluate a Linux-native routing path where BIRD installs routes through standard kernel interfaces, while the Linux kernel, switchdev framework, and hardware driver handle forwarding and hardware offload. This avoids SAI, FPM, proprietary network operating systems, and vendor-specific forwarding agents in the control/data-plane path. We will present the architecture, porting approach, and practical findings from bringing BIRD up on the platform. Topics include interface modelling, VLAN-aware routing, route installation, neighbour handling, observability, hardware L3 offload expectations, and current upstream limitations. The talk is intended as a practical engineering report for the open-source networking community: what works today, what is still missing, and where collaboration between BIRD developers, Linux kernel/switchdev maintainers, and open hardware vendors could improve Linux-native switching.

### Refactoring around an open source project that goes commercial
Speakers: Victoria Risk , ISC Tomek Mrugalski , ISC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/143/PKSFWY/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/PKSFWY/resources/Refactoring2_KquEbMX.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/PKSFWY/resources/Refactoring2_6AIQDB7.pptx | video: https://ripe93.ripe.net/media/videos/victoria-risk_refactoring-around-an-open-source-project-that-goes-commercial_side_20261028-100048.mp4
ISC's Stork project is a web-based graphical management tool with a major dependency on the PrimeNG user interface library. PrimeTek, the company behind PrimeNG, made the decision to end their open source project, and relicense under a commercial license. The PrimeNG open source repository was archived on June 29, 2026. There is a group forming to support a fork of PrimeNG, and there are some alternative web user interface libraries. Given the rate at which new security vulnerabilities are being found right now, with LLM code analysis, we don't feel we have much time to adopt a new, maintained, open source user interface library. We have just started the research and evaluation of our alternatives, and the refactoring won't be over by the time of this RIPE meeting, but we are happy to share our evaluation process and the experience we are getting through this transition. This is not the first time a major open source project has had to change its business model from open source and it won't be the last.

### Closing
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/143/3FDPCN/ | video: https://ripe93.ripe.net/media/videos/na_closing_side_20261028-102326.mp4
AOB

## IPv6 - Main Room (Thu, 09:00)

### Welcome and Co-Chair change
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/152/B3UPSJ/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/B3UPSJ/resources/RIPE93-IPv6-WG-Openi_TC7LisJ.pdf | video: https://ripe93.ripe.net/media/videos/na_welcome-and-co-chair-change_main_20261029-090046.mp4
Opening and Welcome from the WG Chairs Approval of RIPE 92 Minutes Microphone Etiquette Co-Chair Change

### Using IPv6 and DNS to implement a new addressing architecture for the Internet
Speakers: Saleem Bhatti , University of St Andrews, UK
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/152/SP3LJE/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/SP3LJE/resources/20261016_ilnp_ripe93_zH6L8wG.pdf | video: https://ripe93.ripe.net/media/videos/saleem-bhatti_using-ipv6-and-dns-to-implement-a-new-addressing-architecture-for-the-internet_main_20261029-090425.mp4
A presentation on work involving the Identifier Locator Network Protocol (ILNP) at RIPE92/Edinburgh led to many discussions with attendees during the remainder of the meeting. All of them wanted to know more about ILNP. So, this talk presents the "Why?", "What?", and "How?" of ILNP: Why does ILNP exist? What exactly is it? How does it work? This talk describes how ILNP works across today's IPv6 infrastructure, how it is backwards compatible with today's IPv6 applications, and how it offers an alternative design and engineering pathway for higher-layer protocols built on top of IPv6.

### IPv6-only Network Design - follow up
Speakers: Wilhelm Boeddinghaus , Route 128 GmbH, Berlin
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/152/83WLT9/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/83WLT9/resources/RIPE93-October-2026-_2aNVZhZ.pdf | video: https://ripe93.ripe.net/media/videos/wilhelm-boeddinghaus_ipv6-only-network-design-follow-up_main_20261029-093143.mp4
After my talk at RIPE92 in Edinburgh some changes have been made to the WinCLAT feature. This talk gives a short overview of the changes made and the implications coming from this changes for the network design. Additionally, some questions came up about the DHCPv4 design in an IPv6-mosty network. The talk will show possible solutions for the DHCPv4 network design.

### Update on IPv6-related IETF Work
Speakers: Jen Linkova , google
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/152/9R9WYW/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/9R9WYW/resources/IPv6WG_JenLinkova_IE_OtmA0D8.pdf | video: https://ripe93.ripe.net/media/videos/jen-linkova_update-on-ipv6-related-ietf-work_main_20261029-094606.mp4
This is a short summary of ongoing and recently published IETF work in IPv6 area, which might be of interest (or might have direct impact) on operators running IPv6 networks.

### Nothing left to take away
Speakers: Remco van Mook
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/152/DPPNML/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/DPPNML/resources/nothing_left_to_take_G7rob7m.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/DPPNML/resources/nothing_left_to_take_rYGqKaH.key | video: https://ripe93.ripe.net/media/videos/remco-van-mook_nothing-left-to-take-away_main_20261029-100153.mp4
An update on the status of the draft-ietf-ipv6-resolved-gateway, what it does, implementations and open questions

## Database - Side Room (Thu, 09:00)

### Welcome to the RIPE 93 Database WG
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/153/YV9RXB/ | video: https://ripe93.ripe.net/media/videos/na_welcome-to-the-ripe-93-database-wg_side_20261029-090010.mp4
Welcome Scribe Agenda

### RIPE NCC Operational Update
Speakers: Ed Shryane
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/153/SZJT9W/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/SZJT9W/resources/RIPE93_DB-WG_Operati_sYomWtM.pdf | video: https://ripe93.ripe.net/media/videos/ed-shryane_ripe-ncc-operational-update_side_20261029-090206.mp4
Operational Update from the RIPE NCC Database team. What have we been working on since RIPE 92, and planned work and proposals for what to do next.

### Optional RDAP referrals for subordinate resources in the RIPE Database
Speakers: Kaveh Ranjbar , Whisper Security (viaGraph B.V.)
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/153/NKPDGM/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/NKPDGM/resources/RIPE93_DBWG_RDAP_ref_WAqfv7L.pdf | video: https://ripe93.ripe.net/media/videos/kaveh-ranjbar_optional-rdap-referrals-for-subordinate-resources-in-the-ripe-database_side_20261029-092733.mp4
We already let the registry delegate reverse DNS for the space below an allocation to the holder. This proposal asks for the same move for registration data. RDAP answers can be followed from the IANA bootstrap down to the most specific object the RIPE NCC holds, and stop there. Holders that keep registration data for more specific networks below their allocation, and publish it through a conformant RDAP service, have no discoverable referral from the RIPE response to their own server, so today they either register nothing below the allocation or bulk load objects that drift out of date. The proposal, in four parts, all opt-in: Registration of a holder RDAP base URL on the covering object, as an attribute in the spirit of geofeed:, so port 43, the REST API and RDAP all show it. Once a holder has opted in, a redirect for RDAP lookups of subordinate resources to that service, so unchanged clients land on the right record. An additive link in the RIPE response for clients that want to discover the delegation itself. What validation the NCC would do at registration, how it keeps checking, and how a referral is withdrawn when the holder's service stops working. The mechanics come from the IETF: the redirect and the noRedirects0 extension are now in draft-ietf-regext-rdap-referrals-05, the holder case is described in draft-ranjbar-regext-rdap-subordinate-referrals, and a live holder-side server answers today for 2a04:2a01::/32 (AS219419) at rdap.whisper.online. The aim of the slot is a sense of the room on whether to ask the RIPE NCC for an impact analysis and take this forward as a DB-WG work item, and which of the four parts the group wants changed.

### PSA: Removing AS-SET Ambiguity
Speakers: James Bensley , Inter.link
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/153/AJMFLA/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/AJMFLA/resources/RIPE93_-_PSA_-_Remov_n5yDfQd.pdf | video: https://ripe93.ripe.net/media/videos/james-bensley_psa-removing-as-set-ambiguity_side_20261029-093300.mp4
Various improvements are being made to IRR based prefix filtering across the industry, independently from each other. This talk brings these improvements together in a single public service announcement, so that you are aware of them, and so that you can benefit from them.

### NWI Update
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/153/P898GV/ | video: https://ripe93.ripe.net/media/videos/na_nwi-update_side_20261029-101138.mp4
This working group structures smaller changes to the RIPE database into numbered work items. This talk serves as a brief update on what has happened since the last RIPE meeting.

### Closing
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/153/NDBEV8/ | video: https://ripe93.ripe.net/media/videos/na_closing_side_20261029-101246.mp4
AOB Closing

## Plenary - Main Room (Fri, 09:30)

### From Local LANs to a Distributed IX: Lessons from Romania’s Internet Evolution
Speakers: Eric Andrei Băleanu , InterLAN-IX
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/167/QVHD7C/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/QVHD7C/resources/From_Local_LANs_to_a_JQBNVIn.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/QVHD7C/resources/From_Local_LANs_to__wOmaze4.pptx | video: https://ripe93.ripe.net/media/videos/eric-andrei-baleanu_from-local-lans-to-a-distributed-ix-lessons-from-romanias-internet-evolution_main_20261030-093138.mp4
Romania’s early Internet ecosystem developed in an unusual way. In the late 1990s and early 2000s, users built local Ethernet networks inside apartment buildings and neighbourhoods, initially for gaming, communication and file sharing. As permanent Internet access was expensive and difficult to obtain, these communities began sharing individual connections, and many of the local networks gradually became small Internet service providers. Several of these operators began interconnecting directly in Bucharest. Without initially knowing how an Internet Exchange was supposed to operate, they created what later became InterLAN-IX. The exchange developed alongside a Romanian telecommunications market that moved from more than one thousand independent ISPs to a highly concentrated market dominated by a small number of national operators. As regional operators joined the Interlan Association, geographical distance became a practical obstacle. Most meaningful interconnection still took place in Bucharest, while many smaller operators were located hundreds of kilometres away. Rather than creating separate local exchanges with only a few participants, InterLAN-IX extended the same Layer 2 exchange into regional points of presence. This presentation explains how InterLAN-IX evolved from informal local interconnections into a distributed exchange serving operators across Romania. It examines the operational, geographical and market conditions that shaped this model, the relationship between the association and the exchange, and the lessons learned while maintaining broad participation in an increasingly concentrated telecommunications market.

### KSK Rollover 2026: The Internet Didn’t Blink. Or Did It?
Speakers: João Luis Silva Damas , APNIC Geoff Huston , APNIC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/167/FKVYAN/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/FKVYAN/resources/2026-10-22-ksk-roll__7ZHbc0J.pdf | video: https://ripe93.ripe.net/media/videos/joao-luis-silva-damas_ksk-rollover-2026-the-internet-didnt-blink-or-did-it_main_20261030-095436.mp4
At APNIC Labs we carried out measurements of DNSSEC validation and the KSK sentinel signal before, during and after the recent KSK rollover, with humans proving, once again, they are humans.

### The Hidden Geography of the Borderless Internet
Speakers: Emile Aben , RIPE NCC James Cowie , Fellow, Berkman Klein Center for Internet and Society at Harvard
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/167/GSM9GE/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GSM9GE/resources/Hidden_Geography_RIP_Z3z5xW2.pdf | video: https://ripe93.ripe.net/media/videos/emile-aben_the-hidden-geography-of-the-borderless-internet_main_20261030-100632.mp4
RIRs have long realized that resources allocated to a holder in one country may be used in entirely different countries. This is normal and expected; the Internet was not designed to respect national boundaries. We examined the many ways that the registrant and the routing origin of an IPv4 prefix can differ, and developed a descriptive taxonomy to help understand the most common scenarios. Colonial history, local market competition, and IP address transfer markets and leasing are just some of the primary explanations that emerge from the data to explain cross-border Internet operations

### why you should care about the ietf
Speakers: Jen Linkova , google
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/167/KREQC9/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/KREQC9/resources/RIPE93_JenLinkova_IE_ETiUTWC.pdf | video: https://ripe93.ripe.net/media/videos/jen-linkova_why-you-should-care-about-the-ietf_main_20261030-101756.mp4
some examples why operators should care about the ietf

## Plenary - Main Room (Tue, 11:00)

### Measuring Propagation Time of RPKI Validity Changes on the Dataplane
Speakers: Alexander Männel , TU Dresden
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/132/M9LAQ9/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/M9LAQ9/resources/RIPE93-Slides_eqnTvwv.pdf | video: https://ripe93.ripe.net/media/videos/alexander-mannel_measuring-propagation-time-of-rpki-validity-changes-on-the-dataplane_main_20261027-110203.mp4
In this presentation, we investigate how fast the data plane converges when RPKI security attestations change. Our method covers all RIPE IP prefixes that are part of the RPKI hosted model and allows us to study the full propagation timeline. Our results reveal that RPKI propagation is at least one order of magnitude slower than plain BGP. Invalid-to-valid transitions require 9–12 minutes, valid-to- invalid transitions need 30–42 minutes to be effective at 50% of our vantage points. We present the public measurement platform ReRPKI that allows network operators to observe how RIPE Atlas probes connected through their AS experience reachability during ROA changes. This platform can help the operators and the community understand how the current RPKI and ROV deployments behave at Internet-wide scale.

### When Routing Evidence Conflicts: Measuring IRR and RPKI for BGP Filtering
Speakers: Antonis Chariton Usama Ejaz , CISCO ThousandEyes
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/132/JBBTFH/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JBBTFH/resources/RIPE93_irr_rpki_filt_1LcO0UB.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JBBTFH/resources/RIPE93_irr_rpki_fil_gDZKfQW.pptx | video: https://ripe93.ripe.net/media/videos/antonis-chariton_when-routing-evidence-conflicts-measuring-irr-and-rpki-for-bgp-filtering_main_20261027-112800.mp4
Network operators use customer AS-SETs and Internet Routing Registry (IRR) route objects to construct prefix filters, and Resource Public Key Infrastructure (RPKI) data to validate route origins. These sources represent different forms of routing evidence and may produce conflicting results for the same BGP announcement. We present a time-aligned comparison of BGP, IRR, and RPKI from 8–14 August 2026. The analysis covers public BGP prefix-origin pairs observed by 57 RIPE RIS and RouteViews collectors, objects from 19 IRR sources, and validated VRP sets from 17 RPKI relying-party views available throughout the week, with an additional view included on 8 August. We also conduct a separate 8 August replay by recursively expanding PeeringDB-declared AS-SETs through their selected IRR sources. Across the weekly union, 64.4% of observed prefix-origin pairs had an exact IRR match, and 79.9% of those matches appeared in only one IRR source. Among the exact matches, 786 remained RPKI Invalid throughout the week: 371 due to maxLength and 415 due to wrong-origin. We also identify 140,360 retained broader-object candidates. The PeeringDB AS-SET replay retained 99.27% of exact IRR matches, while incomplete or unresolved expansions required further review. The results show that an exact IRR match does not imply an RPKI Valid state and that incomplete AS-SET evidence cannot justify excluding an origin ASN from a filter. We conclude with operational guidance for investigating conflicting evidence before changing route filters.

### With Or Without RPKI: Measuring the Impact of RPKI on the BGP Updates Volume
Speakers: Samuele Quinzi , Roma Tre University (PhD) / UCLouvain (current)
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/132/JMUXFC/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JMUXFC/resources/with-or-without-rpki_LJNbt4c.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JMUXFC/resources/with-or-without-rpk_rT0Qb9F.pptx | video: https://ripe93.ripe.net/media/videos/samuele-quinzi_with-or-without-rpki-measuring-the-impact-of-rpki-on-the-bgp-updates-volume_main_20261027-115607.mp4
The Resource Public Key Infrastructure (RPKI) is the primary defense against BGP route misorigination. It offers a shield against origin hijacks, flavors of route leaks, and misconfigurations. Since its deployment in 2011, the adoption of RPKI by Internet Service Providers has shown continuous growth, a trend that persists to this day. As this growth continues it is important to measure its effect on BGP stability. BGP is a chatty protocol with many updates that can result from a single configuration change on one router. For instance, the addition of a new Route Origin Authorization in the RPKI may result in a change in the validity of a route advertised in BGP, and consequently in different routing decisions that are then propagated in BGP. Here we aim to estimate the volume of updates observed in BGP upon such changes. We identify events resulting from ROA changes and estimate the amount of BGP updates observed in a public BGP repository during these events. We observe that as RPKI adoption rises, the volume of updates generated by RPKI-related changes grows at a similar rate. This growth also mirrors the expansion of the routing table, increasing as more address space is announced and protected by RPKI. However, we also have good news: despite this growth, RPKI-induced updates remain only a very small fraction, corresponding to less than 1% of the total volume of updates.

## Routing - Main Room (Wed, 11:00)

### Intro/Opener
Speakers: Sebastian Becker
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/145/JREZ3H/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JREZ3H/resources/Routing_WG_-_RIPE93_N21JEHd.pdf | video: https://ripe93.ripe.net/media/videos/sebastian-becker_introopener_main_20261028-110020.mp4
Welcome to the Routing Working Group session!

### Topology + Traffic: Real-Time BGP Anomaly Detection from RIPE RIS Raw Data
Speakers: Shadi Motaali , Universidad Autónoma de Madrid (UAM), Spain
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/145/TMMTR8/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/TMMTR8/resources/ShadiMotaali_Topolog_qRizeU9.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/TMMTR8/resources/ShadiMotaali_submit_y0wZw4w.pptx | video: https://ripe93.ripe.net/media/videos/shadi-motaali_topology-traffic-real-time-bgp-anomaly-detection-from-ripe-ris-raw-data_main_20261028-110412.mp4
Machine learning approaches to BGP anomaly detection face a fundamental limitation in operational settings: models trained at one vantage point generalize poorly to another. This presentation reports on a doctoral research project, conducted entirely on RIPE RIS data, that quantifies this limitation and proposes a topology-aware approach to address it. Three results are presented. First, a systematic benchmark of thirteen synthetic-traffic generators demonstrates that detection performance degrades substantially under cross-collector evaluation; notably, the generator with the highest same-collector fidelity exhibits the largest degradation, with 35–41% of anomalies going undetected. Second, augmenting UPDATE-stream statistics with AS-level topology derived from RIB snapshots restores robustness, and a density-based criterion determines the appropriate model class for each network. Third, the resulting detector is validated on two real-world events: it identified the April 2025 Iberian power outage within ten minutes of the onset of its BGP signal, at a 1.3% false-alarm rate, using a model trained five months earlier without retraining; and in a blind evaluation on AS766 (RedIRIS), network operators independently confirmed a detected 65-minute routing episode based on timestamps alone.

### Anycast 101: Load balancing for fun and sometimes profit
Speakers: Tom Strickx , Cloudflare
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/145/LN3EZG/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/LN3EZG/resources/How_not_to_anycast_PB56bn9.pdf | video: https://ripe93.ripe.net/media/videos/tom-strickx_anycast-101-load-balancing-for-fun-and-sometimes-profit_main_20261028-112328.mp4
In this talk, I will walk the audience through the evolution of load-balancing used at Cloudflare, and how these changes influenced the network we design. I'll discuss the technologies we used to use, and still do, while outlining some of the decisions we made to make all of this work together.

### RIPE NCC RPKI Update
Speakers: Tim Bruijnzeels , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/145/DGGEGJ/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/DGGEGJ/resources/RIPE93_-_RIPE_NCC_RP_L5RuALd.pdf | video: https://ripe93.ripe.net/media/videos/tim-bruijnzeels_ripe-ncc-rpki-update_main_20261028-113633.mp4
In this talk, we will provide an update on recent, ongoing, and upcoming developments for the RIPE NCC RPKI service. First, we will give a quick update on the work that was done to implement the 2025-02 'Removal of non-functional CAs' policy, the SOC2 type II audit 2026, and BGPsec Router Key Certificates in the API. Second, we will discuss the upcoming migration of RPKI API keys. The main focus of this talk will be on our plans to improve ROA and ASPA suggestions. While current ROA suggestions focus primarily on making intended announcements ROV valid, we see that there are many ROAs that have some issues. In particular, they may be stale (no longer needed) or too permissive. Additionally, we will address the current lack of ASPA suggestions in the dashboard. Initial data analysis indicates that up to 9% of provider ASNs are omitted from ASPA objects presumably because they were overlooked or because assumed peers are actually acting as providers without the operator's knowledge.

### Elections
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/145/DP7XL8/ | video: https://ripe93.ripe.net/media/videos/na_elections_main_20261028-121615.mp4
Routing WG co-chair elections

### Closing notes
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/145/3LCDBG/ | video: https://ripe93.ripe.net/media/videos/na_closing-notes_main_20261028-122432.mp4
AOB

## Cooperation - Side Room (Wed, 11:00)

### Municipalytics: Mapping the Digital Infrastructure of Municipalities Across GDPR Countries
Speakers: Florian Holzbauer , Interdisciplinary Transformation University Austria (IT:U)
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/146/AMKGUB/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/AMKGUB/resources/RIPE93_Municipalytic_d46ZZTV.pdf | video: https://ripe93.ripe.net/media/videos/florian-holzbauer_municipalytics-mapping-the-digital-infrastructure-of-municipalities-across-gdpr_side_20261028-110537.mp4
Providing statistical data on European municipalities is well established through demographic and socioeconomic indicators. However, comparable visibility into their digital infrastructure remains limited. To address this gap, Municipalytics presents the first comprehensive measurement study of 95,498 municipalities across 30 European countries, combining Eurostat data with 88,948 Wikidata entries for municipal websites to systematically map the Internet-facing infrastructure of local governments. Our analysis reveals clear country-specific patterns in municipal digital infrastructure, including differences in where websites, email services, and DNS are hosted, which types of providers dominate across countries, and how strongly municipal infrastructure is centralized or distributed. We make our results publicly available through an interactive map at municipalytics.internetwarte.eu. This provides a new empirical basis for researchers, policymakers, and operators to study municipal digitalization, infrastructure dependencies, privacy, and related questions of resilience and digital sovereignty across Europe.

### Update on the Multi-Stakeholder Forum on Internet Standards Deployment
Speakers: Rüdiger Martin , Policy Officer, European Commission
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/146/GBAWEA/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GBAWEA/resources/MS_Forum_-_RIPE93_-__wZvoaGW.pdf | video: https://ripe93.ripe.net/media/videos/rudiger-martin_update-on-the-multi-stakeholder-forum-on-internet-standards-deployment_side_20261028-112808.mp4
Update on the Multi-Stakeholder Forum on Internet Standards Deployment

### Evolution of the European regulatory framework on interconnection and peering: prospects and risks
Speakers: Innocenzo Genna , Namex
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/146/3YKB8P/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/3YKB8P/resources/Genna_Sofia_Ripe93_W3G05TS.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/3YKB8P/resources/Genna_Sofia_Ripe93_CM2OXOB.pptx | video: https://ripe93.ripe.net/media/videos/innocenzo-genna_evolution-of-the-european-regulatory-framework-on-interconnection-and-peering-p_side_20261028-114552.mp4
The European Commission’s proposal for a Digital Networks Act (DNA) largely preserves the existing EU approach to IP interconnection, despite the intense political debate on “fair share” and sender-pays models that preceded it. Commercial negotiation remains the default, while specific interconnection obligations continue to depend on the public character of the networks concerned. The proposal does not introduce general network usage fees or mandatory settlement regimes. Instead, Articles 191–192 provide for voluntary ecosystem cooperation and non-binding conciliation on IP interconnection matters outside the public-network interconnection framework. The legislative debate, however, has introduced a potentially significant change of direction. The European Parliament rapporteur’s draft report proposes extending public-network interconnection obligations to “significant traffic providers”, including cloud, CDN and other OTT networks accounting for at least 2% of downstream traffic in the EU. This could bring these actors within a framework of mandatory negotiation and regulatory intervention in interconnection disputes. Although such an extension would not, by itself, establish a sender-pays regime, it could open a new avenue for claims seeking interconnection payments and generate substantial legal uncertainty and litigation. Against this background, the presentation distinguishes between three legally different developments: the proposed extension of public-network interconnection obligations; voluntary cooperation and conciliation mechanisms; and the broader general authorisation framework envisaged by Article 9(2). In particular, it explains why extending regulatory oversight to digital infrastructure does not automatically confer public-network status or trigger mandatory interconnection and payment obligations. The presentation also examines the DNA’s treatment of net neutrality, including specialised services and proposed amendments concerning equal treatment and traffic differentiation. It concludes by identifying the legislative choices that matter most to the RIPE community, explaining how amendments to the public-network boundary could reshape the European interconnection ecosystem even without an explicit “fair share” provision.

### Surviving in the cyber landscape
Speakers: Fredrik Lindeberg , Netnod
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/146/E8GWZ9/ | video: https://ripe93.ripe.net/media/videos/fredrik-lindeberg_surviving-in-the-cyber-landscape_side_20261028-121625.mp4
The risk-management toolkit most operators still use was built for a world of stochastic failure, but today the shift to deliberate, state-backed adversaries breaks the core assumptions. Probability is no longer a property of the world derived from history, but a property of someone else’s intent; redundancy that halves the risk of random failure offers no protection when an adversary hunts for the shared weakness, and “low probability × high impact = accept” decisions made years ago are now wrong but rarely revisited. The talk layers on three accelerants: the move from digital complements to digital dependencies, AI that compresses the attack timeline so that response plans built on business-day clocks become irrelevant, and AI agents that act as insiders whose attack surface is defined by permissions rather than model capability. A live dependency measurement of europa.eu and regeringen.se illustrates that “sovereignty” is not captured by origin requirements but by dependency analysis. No organisation can secure itself in isolation, since everyone is one link in chains that run through others.

## Address Policy - Main Room (Thu, 11:00)

### Policy Update
Speakers: Angela Dall'Ara , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/155/ZN3C3B/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/ZN3C3B/resources/RIPE_93_Policy_Updat_9BO2Hiw.pdf | video: https://ripe93.ripe.net/media/videos/angela-dallara_policy-update_main_20261029-110528.mp4
Update on policy development since RIPE 92

### ASO AC Regular Update
Speakers: Herve Clement , ASO AC / Orange SA
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/155/3NEP37/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/3NEP37/resources/RIPE_93_ASO_AC_Regul_nXt77Ui.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/3NEP37/resources/RIPE_93_ASO_AC_Regu_t7C4G8E.pptx | video: https://ripe93.ripe.net/media/videos/herve-clement_aso-ac-regular-update_main_20261029-112311.mp4
This presentation is about the report the Number Resource Organization Number Council (NRO NC) serving as the Address Supporting Organization Address Council (ASO AC) performs regularly on its yearly activities.

### Registration Services Update
Speakers: Marco Schmidt , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/155/UWJ7CF/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/UWJ7CF/resources/Update_from_Registra_gmA7jcI.pdf | video: https://ripe93.ripe.net/media/videos/marco-schmidt_registration-services-update_main_20261029-113339.mp4
To share observations and potential policy challenges identified by the RIPE NCC Registration Services team. Key topics include the IXP policies, the Legacy Verification Project, and the IPv4 waiting list policy.

### IPv6 Policy clarification
Speakers: Marco Schmidt , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/155/ZFPKGE/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/ZFPKGE/resources/IPv6_Post-Provisioni_lEfPCTk.pdf | video: https://ripe93.ripe.net/media/videos/marco-schmidt_ipv6-policy-clarification_main_20261029-121234.mp4
To present motivation and background of the policy proposal 2026-03 "Clarifying Audit and Policy Compliance Frameworks for IPv6 policies"

### 2026-01: Simplify assignment of first ASN
Speakers: Leo Vegoda Urban Suhadolnik
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/155/MEL99L/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/MEL99L/resources/RIPE_93_-_2026-01_WhvLOvS.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/MEL99L/resources/RIPE_93_-_2026-01_pUzmWZX.odp | video: https://ripe93.ripe.net/media/videos/leo-vegoda_2026-01-simplify-assignment-of-first-asn_main_20261029-115837.mp4
This talk will summarise the problem being addressed, describe the scope of the proposal, and the discussion during the Discussion Phase.

## DNS - Side Room (Thu, 11:00)

### Post-Quantum DNSSEC at Cloudflare
Speakers: Joe Abley , Cloudflare
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/156/Z8RVVH/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/Z8RVVH/resources/RIPE93_dns-wg_PQ_DNS_25I6IcZ.pdf | video: https://ripe93.ripe.net/media/videos/joe-abley_post-quantum-dnssec-at-cloudflare_side_20261029-110226.mp4
Cloudflare is working to implement its first post-quantum DNSSEC algorithm, namely ML-DSA-44 (algorithm 18). We will present our progress to date in implementing algorithm 18 in a large-scale distributed public resolver (1.1.1.1), its use in online signing, considerations around validation policy and downgrade attacks through a PQ lens and gaps we have found in the surrounding landscape of domain registries and registrars.

### PQC for DNSSEC: a format size analysis on Falcon signatures
Speakers: Ginevra Fabrizio , University of Twente
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/156/NA9WQA/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/NA9WQA/resources/RIPE_93_-_Falcon_DNS_8RRQL0Z.pdf | video: https://ripe93.ripe.net/media/videos/ginevra-fabrizio_pqc-for-dnssec-a-format-size-analysis-on-falcon-signatures_side_20261029-113336.mp4
Falcon is a post-quantum signature algorithm recently chosen for standardization by the National Institute of Standards and Technology (NIST). Its official implementation has two different signature formats that differ in size. In this paper, we measure the impact of the two different formats of Falcon signatures on DNSSEC-signed zones and on DNSSEC queries, based on real-world traffic for a large country-code Top Level Domain (ccTLD). We take into consideration Falcon’s two signature formats, called padded and compressed, and evaluate their effects on DNSSEC signature sizes. We pro- vide a signature size distribution for each format, using data obtained from a DNSSEC-signed ccTLD zone and queries for this zone. We use the results to study whether there are advantages to choosing one of the two signature formats. Our results show that the difference in DNS message size between padded and compressed signatures is small. Therefore, while in theory smaller signatures are favorable, the use of the compressed signature format does not have tangible real-world benefits. As our results show, the use of compressed signatures does not lead to a significant shift in message size such that more DNSSEC answers would fit within MTU limits. These results provide useful input for the discussion on Falcon signature standardization in DNSSEC, concluding that standardization of a fixed-size padded format may be preferable for its predictability and to avoid potential implementation errors.

### Local root: the traffic trade-off between root queries and root zone distribution
Speakers: Willem Toorop , NLnet Labs Ilyas Rahimi , University of Amsterdam
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/156/FWEFY9/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/FWEFY9/resources/local-root-ripe93.pp_PHd8fu0.pdf | video: https://ripe93.ripe.net/media/videos/willem-toorop_local-root-the-traffic-trade-off-between-root-queries-and-root-zone-distributio_side_20261029-114253.mp4
Populating resolvers with the root zone improves operational robustness of the resolver and the privacy of its users. There is currently an Internet Draft proposal to make it a best current practice (see https://datatracker.ietf.org/doc/draft-wkumari-dnsop-localroot-bcp/07/ ). What is less clear in practice is how this impacts traffic. Moving from query-driven interaction with the root to an update-driven model replaces many small queries with fewer, larger transfers of zone data, and the net effect depends on how often the root zone changes and how resolvers obtain updates. Ilyas Rahimi quantified that trade-off using a measurement-based approach for his master thesis Security and Network Engineering at the University of Amsterdam (see https://nlnetlabs.nl/downloads/publications/DNS_Local_ROOT_ResearchProject2.pdf ). We will present Ilyas’ research showing that traffic increases under the current root zone’s signing and updating scheme. We will show how incrementally signing the root zone would change that to less traffic. Finally we present a wild speculation how some protocol extensions could reduce traffic to almost negligible amounts while retaining all the resilience, privacy and security benefits.

### RIPE NCC DNS Update
Speakers: Leon Grasmeijer , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/156/9NHT3A/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/9NHT3A/resources/DNS_Update_RIPE_NCC_eccOqSA.pdf | video: https://ripe93.ripe.net/media/videos/leon-grasmeijer_ripe-ncc-dns-update_side_20261029-120858.mp4
A short presentation about RIPE NCC's DNS activities.

## Closing Plenary - Main Room (Fri, 11:00)

### How safe are our domain names from US sanctions? Time for discussion
Speakers: Timo Hilbrink
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/170/ZW9ZCZ/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/ZW9ZCZ/resources/how-safe-are-our-dom_8As1ts0.pdf | video: https://ripe93.ripe.net/media/videos/timo-hilbrink_how-safe-are-our-domain-names-from-us-sanctions-time-for-discussion_main_20261030-110050.mp4
Following my Lightning Talk on Tuesday about the effects of US sanctions on domain names and other parts of the internet, we have some extra time for further discussion

### Debugging Stupid Things: If it only was DNS for once...
Speakers: Tobias Fiebig , TU Wien
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/170/JLVACT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JLVACT/resources/presentation_AVV6CdU.pdf | video: https://ripe93.ripe.net/media/videos/tobias-fiebig_debugging-stupid-things-if-it-only-was-dns-for-once_main_20261030-112621.mp4
Running production systems on the Internet tends to be full of surprises. After all, "the Internet is a collection of corner cases". One of the hardest tasks in keeping systems running is debugging such corner cases. In this talk, we will go over a couple of weird corner case bugs, and the process taken for debugging them. Each case will also be accompanied by a brief 'lessons learned', that touch on often held believes that may stand in one's way when trying to understand why a system does not do what it was told (or rather: Why one has not yet understood what one told said system). Hopefully, this talk let's you get a better handle on how to ask a system what it was told. And if not, it shares at least some fun stories. (No DNS packets were the root-cause in any of the cases discussed.)

### RIPE Code of Conduct Team Report
Speakers: Sebastian Becker
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/170/JPLEZA/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JPLEZA/resources/RIPE93_CoC_Transpare_MlqPHYj.pdf | video: https://ripe93.ripe.net/media/videos/sebastian-becker_ripe-code-of-conduct-team-report_main_20261030-115135.mp4
Report from the RIPE Code of Conduct team at RIPE 93

### RIPE 93 Tech Report
Speakers: Menno Schepers
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/170/VYXCP7/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/VYXCP7/resources/RIPE_93_Tech_Report__DS1J9z4.pdf | video: https://ripe93.ripe.net/media/videos/menno-schepers_ripe-93-tech-report_main_20261030-115617.mp4
Report from the RIPE Meeting Tech Team

### Closing
Speakers: Mirjam Kühne , RIPE Chair
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/170/SXQYZD/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/SXQYZD/resources/RIPE_93_Closing_Plen_w3j37Bc.pdf | video: https://ripe93.ripe.net/media/videos/mirjam-kuhne_closing_main_20261030-121349.mp4
Closing presentation from the RIPE Chair Team

### Welcome to RIPE 94
Speakers: Paulius Judickas
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/170/AEQV9T/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/AEQV9T/resources/RIPE_94_-_Vilnius_-__S0Z0JGu.pdf | video: https://ripe93.ripe.net/media/videos/paulius-judickas_welcome-to-ripe-94_main_20261030-122456.mp4
Welcome to RIPE 94!

## Newcomers' Introduction - Main Room (Mon, 11:30)

### Newcomers' Introduction
Speakers: Mirjam Kühne , RIPE Chair Hans Petter Holen , RIPE NCC Anna Wilson , RIPE Vice Chair
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/120/GCYT7Y/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GCYT7Y/resources/RIPE_93_Newcomers_In_U1HnKPx.pdf | video: https://ripe93.ripe.net/media/videos/mirjam-kuhne_newcomers-introduction_main_20261026-113320.mp4
Is this one of your first RIPE Meetings? Join the Newcomer's Introduction to get an introduction to the RIPE community and learn how things are organised at a RIPE Meeting. The RIPE Chair team, Mirjam Kühne and Anna Wilson will give you an overview of what you can expect at the meeting. RIPE NCC CEO and Managing Director, Hans Petter Holen, will introduce you to the RIPE NCC and its work.

## Opening Plenary - Main Room (Mon, 14:00)

### Welcome to RIPE 93
Speakers: Mirjam Kühne , RIPE Chair
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/123/VDL3R9/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/VDL3R9/resources/Welcome_to_RIPE_93_-_bUaNgrq.pdf | video: https://ripe93.ripe.net/media/videos/mirjam-kuhne_welcome-to-ripe-93_main_20261026-140237.mp4
Welcome to RIPE 93

### Welcome from the Local Host
Speakers: Ivo Ivanov , CEO of DE-CIX
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/123/C7LE7E/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/C7LE7E/resources/hostspeech-image-bac_VhJnR1V.pdf | video: https://ripe93.ripe.net/media/videos/ivo-ivanov_welcome-from-the-local-host_main_20261026-141305.mp4
Welcome to Sofia

### Welcome from the RIPE NCC and Meeting Logistics
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/123/JYFM3A/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/JYFM3A/resources/RIPE_93_Welcome_from_Ooju2bD.pdf | video: https://ripe93.ripe.net/media/videos/hans-petter-holen_welcome-from-the-ripe-ncc-and-meeting-logistics_main_20261026-141920.mp4
RIPE 93 Meeting Logistics

### Welcome from the RIPE Programme Committee
Speakers: Massimiliano Stucchi , RIPE PC Chair
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/123/TPQVQV/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/TPQVQV/resources/RIPE93-PC_cMgr03R.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/TPQVQV/resources/RIPE93-PC_n6xfVXv.key | video: https://ripe93.ripe.net/media/videos/massimiliano-stucchi_welcome-from-the-ripe-programme-committee_main_20261026-142732.mp4
Welcome from the RIPE Programme Committee

### On the Importance of Telling Your Friends to fsck.ofs
Speakers: Tobias Fiebig , TU Wien Franziska Lichtblau
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/123/F9ASLT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/F9ASLT/resources/presentation_sgTzvsR.pdf | video: https://ripe93.ripe.net/media/videos/tobias-fiebig_on-the-importance-of-telling-your-friends-to-fsckofs_main_20261026-143734.mp4
The stereotype of 'the' grumpy Operator-from-Hell is probably as old as the Internet. Still, arguably, system and network engineers have a tendency of 'being right'; Which often makes them grumpy, especially when management yet-again does the wrong thing. Most operators know at least one person that used to be young and enthusiastic, pushing [$NEW_TECH] into an organization, slowly advancing to become the utmost expert on it. They made the right call, at the right time. Then they start to fend off attempts to replace or improve [$NO_LONGER_REALLY_NEW_TECH], also becoming irreplaceable by fighting the fires caused by said technology. Then, with the bus factor converging to 1, they converge to burn out. While burning out they will drag down the team, and discourage junior operators on their journey. In this talk, we revisit this pattern; We take a look at why people seem to always be right, what negative impact it has, and what it takes to accept being wrong. As one usually does not know when they stand in that corner, we also provide a How To guide for the most important thing: Telling our friends to fsck.ofs (when it is necessary).

### Is this application IPv6 ready?
Speakers: Sávyo de Morais , NIC.br
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/123/RUAZLC/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/RUAZLC/resources/ipv6_l7_ripe_SYs3PuW.pdf | video: https://ripe93.ripe.net/media/videos/savyo-de-morais_is-this-application-ipv6-ready_main_20261026-151155.mp4
IPv6 deployment has reached a point where the hardest problems are no longer necessarily in routers and access networks. Increasingly, the question is whether the applications running on those networks have actually been tested without IPv4. For many years, "IPv6 support" could mean that an application worked on a dual-stack host. But as IPv6-only networks and transition mechanisms such as NAT64 become increasingly common, applications need to remain functional when IPv4 is unavailable. This is particularly important for public digital services: governments may mandate IPv6 support for public-facing services, but network-level IPv6 connectivity does not guarantee that the application itself will work correctly. This presentation will look at IPv6 application readiness from an operational perspective: what should actually be tested, which failure modes are commonly missed, and how to test applications across IPv4-only, dual-stack, IPv6-only with NAT64, and strict IPv6-only environments. We will also share our experience developing V6bench at NIC.br, an open-source tool created to help setting up a laboratory to test applications' IPv6 readiness. Rather than presenting it as a product, we will use it as a practical example of how operators, developers and SRE teams can build repeatable IPv6 application-testing environments and invite the community to help evolve the approach.

## Plenary - Main Room (Tue, 14:00)

### Testing an Upstream Intervention: The Impact of Category 1 Safeguards on DNS Abuse
Speakers: Carlos Gañan , ICANN
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/134/EZQEVH/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/EZQEVH/resources/RIPE93_cat1_NkjB5QO.pdf | video: https://ripe93.ripe.net/media/videos/carlos-ganan_testing-an-upstream-intervention-the-impact-of-category-1-safeguards-on-dns-abu_main_20261027-135955.mp4
Identity and registrant verification are becoming a more prominent part of Internet security policy. The premise is intuitive: make malicious registration harder, and less abuse should enter the ecosystem. Yet evidence that these controls measurably reduce abuse remains limited. For operators who ultimately absorb the consequences through DNS, hosting, threat intelligence, incident response, and takedown, this is not only a policy question. It is an operational one. We test this premise using ICANN’s Category 1 safeguards as a real-world case study. Category 1 applies additional requirements to gTLDs associated with regulated or sensitive sectors. Importantly, the framework includes different registration models, from open registration with self-certification to restricted registration with eligibility or credential verification. We analyze 1,106 new gTLDs monthly from 2023 through 2025. Rather than asking only whether safeguarded namespaces have "less abuse," we separate two processes that conventional abuse rates combine: whether maliciously registered domains appear at all, and how large campaigns become once they appear. The result challenges a simple prevention story. After accounting for gTLD size, registry architecture, and common monthly conditions, Category 1 gTLDs are associated with abuse appearing in more months, but with substantially smaller campaigns when abuse occurs. The combined model predicts lower malicious-domain volume overall. The strongest difference is within Category 1 itself: restricted Level 8 gTLDs show lower occurrence, lower scale, and lower overall volume than the more open, self-certified Level 3 group. These findings raise a broader question for the RIPE community. As verification and other upstream safeguards become more common, what evidence should demonstrate that they work? Our results suggest that aggregate abuse rates are not enough. Evaluating upstream interventions requires distinguishing prevention, containment, and response, and connecting those outcomes to operational data on verification, rejected registrations, campaigns, and remediation.

### Networks as Sensors: Passive Measurement as a Lens on Society, A case study on two European elections
Speakers: Orlando Eduardo Martínez-Durive , IMDEA Networks Institute & Net AI
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/134/DLCKAN/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/DLCKAN/resources/Elections__Apps____Z7QvTZO.pdf | video: https://ripe93.ripe.net/media/videos/orlando-eduardo-martinez-durive_networks-as-sensors-passive-measurement-as-a-lens-on-society-a-case-study-on-t_main_20261027-143022.mp4
Mobile operators, ISPs, and IXPs run passive measurements for engineering, which can also be used as complementary vantage points on how society behaves online: mobility, application consumption, disruptions, and how all of these vary across space and time. The community already reads major events off this infrastructure, i.e., shutdowns, cable cuts, and wartime rerouting, through RIPE RIS and Atlas, IODA, and OONI. We argue that the same passive vantage reaches subtler social signals, such as political alignment during elections. We analyze passive mobile metadata from a major French operator across urban and suburban France during the 2019 and 2024 European Parliament elections. We align per-antenna demand for tens of mobile services with socioeconomic indicators at the commune (municipality) level, and model vote shares. We find that digital consumption carries an independent signal about political alignment that, for several parties, matches or exceeds traditional socioeconomic indicators; combining both increases explanatory ability by up to 28.23%. The associations are consistent across both elections. The broader point is that each MNO, ISP, and IXP vantage point trades spatial resolution for reach and diversity, and together they could form a platform-independent instrument for observing the digital society, one that does not depend on APIs that platforms can withdraw. This talk is also an invitation: I am looking to open collaborations with researchers and with MNO, ISP, and IXP operators to map what each vantage point can measure and to build this instrument together.

### Multi-Layer Routing Domain Protection at Hyperscale: From Route Leak to Automated Enforcement
Speakers: Daria Shantalova , Express Backbone Team, Meta
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/134/TN3ZHZ/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/TN3ZHZ/resources/RIPE_93_-_Multi-Laye_wyACzkg.pdf | video: https://ripe93.ripe.net/media/videos/daria-shantalova_multi-layer-routing-domain-protection-at-hyperscale-from-route-leak-to-automate_main_20261027-150238.mp4
Operating a global backbone connecting dozens of data centers requires strict enforcement of which prefixes are allowed to cross domain boundaries. A single misconfiguration — a wrong BGP community tag or an unregistered prefix — can cascade into widespread service disruption across multiple network domains. This talk presents our journey building a multi-layered defence system against routing domain violations at scale. After a major routing incident exposed gaps in our boundary protection, we developed three independent, complementary layers: (1) ID Communities — a tagging system assigning each prefix a unique identity that defines its origination and propagation scope across domain boundaries. (2) Route Registry — a source of truth defining which prefixes are explicitly permitted at each boundary, deployed as inbound prefix-lists with a freshness SLA. (3) Control Plane Health Monitoring — an automated system that continuously validates the routing state against intent, detecting community mismatches and unregistered prefixes before they become incidents. We share how this system exposed pervasive violations across production, prefixes crossing boundaries without correct identity, and how we eliminated nearly all of them within months through systematic remediation. Automated enforcement now prevents recurrence.The talk concludes with lessons learned on making routing domains self-protecting at hyperscale. Relevant to operators managing multi-domain networks, backbone/DC boundary protection, and anyone interested in intent-based routing verification.

### How safe are our domain names from US sanctions?
Speakers: Timo Hilbrink
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/134/HXFYTB/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/HXFYTB/resources/how-safe-are-our-dom_QTwoK56.pdf | video: https://ripe93.ripe.net/media/videos/timo-hilbrink_how-safe-are-our-domain-names-from-us-sanctions_main_20261027-151329.mp4
Recently, sanctions imposed by the US Department of the Treasury, took an .org domain out of the DNS. In theory, the same could happen to any .net or .com domains, are we prepared for this? What can we do to minimise the damage?

### Updating the MANRS Network Operators Baseline: Progress and Impact
Speakers: Andrei Robachevsky , Global Cyber Alliance/MANRS
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/134/E7MZLT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/E7MZLT/resources/202610-RIPE93-MANRS_omAcDUi.pptx | video: https://ripe93.ripe.net/media/videos/andrei-robachevsky_updating-the-manrs-network-operators-baseline-progress-and-impact_main_20261027-152520.mp4
The MANRS Actions for network operators have not been substantially revised since 2014. Meanwhile, the adoption of RPKI has grown significantly, its operational experience has deepened, and new routing security technologies are being tested and increasingly deployed. A 2026 MANRS community survey identified clarity of implementation and auditing requirements, and alignment with current practices as the top priorities for review. This talk presents the progress of the MANRS Network Operators Program Review Working Group, which is developing an updated normative specification through an open, consensus-based process. It will cover the key areas that were under discussion – including Route Origin Validation, registration in the IRR and RPKI, prefix filtering and anti-spoofing – and the reasoning behind decisions about what belongs in a base standard versus best current practices and implementation guidelines. The talk will also present an impact assessment: how the revised baseline would impact current MANRS participants, and how the updated actions position MANRS globally against common operational practice. Community input is welcome as the document moves toward the final call.

## RIPE NCC Services - Main Room (Wed, 14:00)

### Welcome, admin matters
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/148/VEAFBV/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/VEAFBV/resources/ncc-services-agenda-_qVy7wWx.pdf | video: https://ripe93.ripe.net/media/videos/na_welcome-admin-matters_main_20261028-140115.mp4
Welcome to your favourite working group.

### RIPE NCC Draft Activity Plan and Budget 2027
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/148/HFKVUM/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/HFKVUM/resources/A._Draft_Activity_Pl_RwZ8xdE.pdf | video: https://ripe93.ripe.net/media/videos/hans-petter-holen_ripe-ncc-draft-activity-plan-and-budget-2027_main_20261028-140526.mp4
The Draft RIPE NCC Activity Plan and Budget 2027 sets out the activities we plan to carry out in the first year of our 2027–2031 strategy, along with the resources would need to deliver them. In this session, we will present our main priorities for 2027, including the work planned across our Registry, Technology, External Engagement and Community, and Organisational Sustainability activities. The Draft Activity Plan and Budget is open for consultation, and we welcome feedback from the RIPE community on our plans and priorities before the final document is approved and published in December.

### Renewing Our Technical Infrastructure
Speakers: Sjoerd Wolthers
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/148/SNSVJF/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/SNSVJF/resources/B._Infrastructure_Up_M7gBo5Z.pdf | video: https://ripe93.ripe.net/media/videos/sjoerd-wolthers_renewing-our-technical-infrastructure_main_20261028-143919.mp4
The RIPE NCC is beginning a project to renew our technical infrastructure. We will explain why this investment is needed and share our thinking on how we will build a more resilient, independent and secure infrastructure.

## Address Policy - Main Room (Thu, 14:00)

### Moving to a RIPE policy manual
Speakers: Remco van Mook
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/158/RMKKMS/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/RMKKMS/resources/kitchen_sink_proposa_mITJQaq.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/RMKKMS/resources/kitchen_sink_proposa_WXjSeIX.key | video: https://ripe93.ripe.net/media/videos/remco-van-mook_moving-to-a-ripe-policy-manual_main_20261029-140051.mp4
RIPE address policy is not described by any single, consistent body of text. The current stack works because we are incredibly nice people and because the RIPE NCC absorbs the ambiguity. That is not a stable arrangement but an undocumented dependency, and it is one this working group can no longer afford. The population that sustains our consensus process has shrunk by a factor of three over the past decade, while the same definitional gaps keep resurfacing as full proposal cycles, multi-month threads and NCC feedback rounds. This is the fourth talk in a series (Why-PI at RIPE 82, Why-PI Redux at RIPE 88, Simplifying Assignment Status at RIPE 89). This time it comes with a concrete, evolutionary path rather than a diagnosis: - an indexed manual that initially just points at the current documents; - per-resource chapters re-homed one at a time, verbatim, starting with the already-consolidated transfer policy. One chapter per proposal.

### IPv6 and extra-terrestrial networks
Speakers: Remco van Mook
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/158/8GFPTK/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/8GFPTK/resources/RIPE93_AP_-_ipv6_and_oFmUrMN.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/8GFPTK/resources/RIPE93_AP_-_ipv6_and_UtizOBC.key | video: https://ripe93.ripe.net/media/videos/remco-van-mook_ipv6-and-extra-terrestrial-networks_main_20261029-142954.mp4
Current work within the IETF raises concerns about a workable outcome for IPv6 allocations when/if new IPv6 space gets allocated by IANA for extra terrestrial networks. This proposal aims to ring-fence the current global IPv6 unicast space for terrestrial use only, and ensure that when that new space gets allocated, it will be used for its purpose and that it has sufficient guidance on how to be used.

### Users of IPv4 PA block in the RIPE Database
Speakers: James Kennedy , KIPA.global
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/158/GWRM7L/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GWRM7L/resources/KIPA_RIPE93_final_5fa0GMe.pdf | video: https://ripe93.ripe.net/media/videos/james-kennedy_users-of-ipv4-pa-block-in-the-ripe-database_main_20261029-145803.mp4
The RIPE Database Requirements Task Force recommended that address space an LIR issues to another organisation be documented in the RIPE Database. This talk looks at how registration practices today under the current policy (ripe-826) meet that recommendation, where they fall short, and the impact that has on those who rely on the Database.

## IoT - Side Room (Thu, 14:00)

### Introduction & Housekeeping
Speakers: Ramona Marfievici
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/159/VJAHYD/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/VJAHYD/resources/RIPE-93-IoT-Slides_KCp34oL.pptx | video: https://ripe93.ripe.net/media/videos/ramona-marfievici_introduction-housekeeping_side_20261029-140016.mp4
Welcome and introduction for the IoT Working Group Session.

### Internet-Scale Classification of IoT and Non-IoT Devices from a Single Packet
Speakers: Muhammad Sangeen , PhD Candidate, University of Twente
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/159/HNPU8U/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/HNPU8U/resources/RIPE-talk-v2_8tKxUCT.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/HNPU8U/resources/RIPE-talk-v2_ELL2ygu.pptx | video: https://ripe93.ripe.net/media/videos/muhammad-sangeen_internet-scale-classification-of-iot-and-non-iot-devices-from-a-single-packet_side_20261029-140423.mp4
Internet scanning is a key signal for threat intelligence, but existing measurement approaches reveal where scans originate, not what kind of device is behind them, limiting the ability to distinguish IoT-botnet activity from general-purpose scanning at the network-operator level. We develop a methodology to classify IoT and non-IoT devices from a single TCP SYN packet, requiring neither active probing nor flow reconstruction. This gives operators device-level visibility into traffic, enabling them to flag IoT devices appearing on infrastructure where they are not expected, such as cameras or smart appliances communicating from networks where only servers or user devices are expected. Because it relies only on a single TCP SYN packet, the approach can be deployed at any vantage point observing TCP traffic, including CGNAT borders and IXP mirrors. We build a multi-source fingerprint dataset from 224 IoT devices across six testbeds, combined with a non-IoT fingerprint database. We show that a small set of SYN header fields, primarily related to TCP receive-buffer configuration, separates the two populations. Our approach combines exact fingerprint matching with a classifier that generalises to previously unseen devices, correctly classifying over 90% of them at a false positive rate below 0.2%. We apply this approach to 30 days of traffic from the University of California, San Diego (UCSD) Network Telescope, comprising 3.2 trillion packets from 10.8 million distinct sources. We find that IoT devices constitute approximately 6% of scanning hosts but contribute under 1% of total scan volume. Non-IoT hosts account for most scan traffic, driven by few high-volume scanners. IoT contributes to Internet scanning by breadth rather than volume: many devices each scan slowly, a pattern consistent with IoT botnet behaviour. We also characterise differences in target ports, scanning behaviour, and geographic origin between IoT and non-IoT devices. These results provide operators with device-level insight into the sources and behaviour of Internet scanning activity.

### DNS Privacy Enhancements for the Constrained IoT: DNS over CoAP
Speakers: Martine Sophie Lenders , TU Dresden
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/159/EJYWK3/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/EJYWK3/resources/main_vnki7hN.pdf | video: https://ripe93.ripe.net/media/videos/martine-sophie-lenders_dns-privacy-enhancements-for-the-constrained-iot-dns-over-coap_side_20261029-142733.mp4
The Internet of Things (IoT) is a common attack vector and cause for privacy concerns. Protecting against such attacks while also protecting the privacy of its users often conflicts with constrained resources we find in the IoT. We present DNS over the Constrained Application Protocol (CoAP), a new protocol to counter such attacks by encrypting queries, similar to DNS over TLS, HTTPS, or QUIC. In contrast to those protocols for the "big" Internet, DNS over CoAP is designed to encrypt queries from constrained IoT devices. It only requires a handful of kilobytes of working and perstistant flash memory and can be sent over small link layer PDUs. All while offering the same security properties as the other DNS over X protocols.

### Cyber Resilience Act: Implementation update for the RIPE community
Speakers: Ramona Marfievici
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/159/PZZD9E/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/PZZD9E/resources/RIPE93_CRA_Update_hJnUW6s.pdf | video: https://ripe93.ripe.net/media/videos/ramona-marfievici_cyber-resilience-act-implementation-update-for-the-ripe-community_side_20261029-145008.mp4
Implementation update for the RIPE community of the CRA standards.

### Closing
Speakers: Ramona Marfievici
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/159/N3ZKNX/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/N3ZKNX/resources/RIPE-93-IoT-Slides_WT5CEEU.pptx | video: https://ripe93.ripe.net/media/videos/ramona-marfievici_closing_side_20261029-150139.mp4
AOB and Closing

## Plenary - Main Room (Mon, 16:00)

### Embracing NETCONF
Speakers: Maria Matejka , BIRD | CZ.NIC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/125/AA9HSF/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/AA9HSF/resources/embracing-netconf-v2_jGfVge2.pdf | video: https://ripe93.ripe.net/media/videos/maria-matejka_embracing-netconf_main_20261026-160213.mp4
The NETCONF API has been specified for 20 years and it's time to look at all the zoo of protocols, formats and schemas available for use. Is it mature? Can we rely on it? Is it efficient? Have you read the fine print?

### Aligning Path Changes with Measured Impact in R&E Networks
Speakers: Petya Vasileva , Plovdiv University / University of Michigan
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/125/BVCKV3/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/BVCKV3/resources/RIPE_93_16_iZ045oE.pdf | video: https://ripe93.ripe.net/media/videos/petya-vasileva_aligning-path-changes-with-measured-impact-in-re-networks_main_20261026-163029.mp4
Large R&E networks are full of partial signals: traceroutes show path changes, OWAMP tests show delay and loss, iperf3 shows throughput - each running at its own cadence, inspected with its own tool. When a data transfer slows down, the real question is simple but hard to answer fast: did the path change, and does that explain it? We built a routing-aware incident triage tool on top of perfSONAR data from the WLCG/OSG mesh (170+ sites, ~4M tests/day). For each monitored corridor (source-destination pair), it detects routing shifts using graph-based path embeddings scored against that corridor's own recent baseline, then aligns them with delay, loss, and throughput evidence. Finally, each pair is assigned to an operator-facing class - confirmed impact, routing change with no measurable effect, tests interrupted, or needs review - so operators get a prioritized list. We will walk through how the routing representation and alignment stage work, then through real incidents: a submarine cable fault the tool caught live - where the emergency path halved the latency while throughput collapsed, exactly the case a latency-only monitor misreads, and months of bursty, low-level loss into a single site that the shared-path evidence localizes to one ingress element. The method is perfSONAR-native: no BGP feeds, no additional probing, no labelled training data - and directly reusable on any comparable measurement mesh.

### RISwhois - Past, Present, Future
Speakers: Sam van Kampen , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/125/ZJNCYX/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/ZJNCYX/resources/RISwhois-rs_5_MxwJMgv.pdf | video: https://ripe93.ripe.net/media/videos/sam-van-kampen_riswhois-past-present-future_main_20261026-165317.mp4
In the past few months, we have built a successor to the classic RISwhois service. In this talk, I briefly discuss the history of RISwhois, and then detail the improvements we have made in RISwhois-rs, and end by looking to the potential future improvements to RISwhois-rs.

### RIPE RIS - what we collect, and what we will collect in the future
Speakers: Ties de Kock , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/125/UJMQDA/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/UJMQDA/resources/202610_RIPE_93_-_RIS_lGVnirt.pdf | video: https://ripe93.ripe.net/media/videos/ties-de-kock_ripe-ris-what-we-collect-and-what-we-will-collect-in-the-future_main_20261026-170444.mp4
RIPE RIS has been collecting BGP data for more than 25 years. We maintain a long-term archive, and that comes with its own challenges: the volume only grows, and noisy or low-value data stays with us forever. In recent years, we have therefore been quite selective about accepting new peering sessions. We now want to reconsider that approach: collecting data from more peers, while keeping the long-term volume manageable. In this talk, I will recap the data RIS has been collecting and show some of the results --- and artifacts --- we see in the archive, including noisy peers, unstable sessions, and the growth of BGP attributes over time. I will then present ideas for a new peering policy that would allow us to be more open to new peers while keeping the resulting archival volume manageable. We get a lot of input from researchers about RIS, but we also want to hear from network operators: what data is useful to you, and what should we avoid collecting? We would particularly like feedback on these ideas before turning them into a new RIS peering policy, which we hope to publish later this year.

### TTL Jumps: Unexpected TTL Rewrites Impacting Inferences from Traceroutes
Speakers: Tobias Fiebig , TU Wien Johannes Zirngibl , Max Planck Institute for Informatics
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/125/9388Q3/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/9388Q3/resources/presentation_8QIVkpM.pdf | video: https://ripe93.ripe.net/media/videos/tobias-fiebig_ttl-jumps-unexpected-ttl-rewrites-impacting-inferences-from-traceroutes_main_20261026-171559.mp4
Traceroute is an important Internet measurement tool used to infer the Internet’s topology and to identify middleboxes. It relies on network devices decrementing the Time to Live (TTL) in IP packet headers by one at each hop and sending Internet Control Message Protocol (ICMP) Time Exceeded error messages if the TTL reaches zero. However, we show that TTL jumps exist on the Internet: some devices rewrite the TTL, often to larger value of up to 255. These rewrites hide the remaining path from traceroute and can lead to incorrect inferences like spurious router and Autonomous System (AS) links. Based on controlled experiments and public data from RIPE Atlas and CAIDA Ark, we show that at least 47 ASes are impacted by path-impairing devices that rewrite the TTL. A prominent example is AT&T where more than 90 % of outgoing IPv6 paths from CAIDA Ark nodes are affected since 2023.

## MAT - Main Room (Tue, 16:00)

### The Internet’s Path MTUs: How Big Can You Go?
Speakers: Tobias Fiebig , TU Wien Vaishnavi Raghavajosyula , Max Planck Institute for Informatics
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/9W9JWP/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/9W9JWP/resources/RIPE93-4_hPMXiyh.pdf | video: https://ripe93.ripe.net/media/videos/tobias-fiebig_the-internets-path-mtus-how-big-can-you-go_main_20261027-160734.mp4
Efficient network transmission, especially in IPv6 since on-path fragmentation is not possible, depends on selecting the right packet size. The Maximum Transmission Unit (MTU) determines the largest packet size that can traverse a link and the Path MTU (PMTU) determines the size for an end-to-end path without fragmentation. Due to frequent failures in Path MTU Discovery (PMTUD), protocols must fall back to conservative packet sizes to ensure reachability, sacrificing potential throughput. This creates a need for inference based approaches that estimate a suitable path size. Existing PMTU studies are outdated, limited in scope, and rely on indirect MSS inference or PMTUD-dependent signals, offering little insight into where MTU bottlenecks occur along the path. This paper presents a measurement study of PMTUs using RIPE Atlas to characterize their behavior in general, across protocol layers (IPv4/IPv6) and network locations thus covering 76,700 paths across access networks, the Internet core, and web-serving infrastructure. We observe 97 distinct PMTUs, though a small set:[1500 B (80.5%), 1492 B (11.7%), and 1480 B (1.5%)], dominates. PMTU distributions differ across IP versions: while 99% of IPv4 paths support at least 1420 B, IPv6 paths commonly operate at 1280 B. We further show that sub-1500 B PMTUs are primarily located near network edges, while core paths rarely exhibit such constraints. Finally, we measure PMTU vs. Maximum Segment Size (MSS)-inferred PMTU mismatches in 18.5% of paths.

### LightScope: Turning Production Machines into Telescopes and Honeypots
Speakers: Eric Kapitanski , USC Information Sciences Institute
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/PJAQUT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/PJAQUT/resources/RIPE93_sxF8Por.pdf | video: https://ripe93.ripe.net/media/videos/eric-kapitanski_lightscope-turning-production-machines-into-telescopes-and-honeypots_main_20261027-161855.mp4
Traffic to unused IP addresses (dark spaces), including passive and reactive network telescopes and honeynets, has traditionally been used to study malicious activities. However, attackers may avoid known dark space sensors and preferentially target endpoints hosting legitimate services. We present LightScope, a lightweight application that unifies passive observation at Layer 4 with selective proxying to a remote Layer 7 honeypot. LightScope does this by leveraging a subset of the unused ports on production servers. By embedding measurement on the production hosts themselves, LightScope creates a new vantage point for observing various scanner populations, port-targeting profiles, and post-login behaviors that are only partially visible from dark-space telescopes and honeynets. In this paper we analyze two months of data collected from 235 LightScope deployments. We show that LightScope contributes new knowledge about widely observed scanners, their port scan strategies and their post-exploit activities. These scanners interact with production endpoints running LightScope differently than they do with other vantage points. In our study period, LightScope also exclusively observes 64,686 scanners not present at other vantage points. By instrumenting production machines, LightScope provides complementary visibility to existing telescopes and honeynets.

### The State of ECN Adoption in the Internet
Speakers: Danesh Zeynali , Max Planck Institute for Informatics
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/38HZHM/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/38HZHM/resources/ECN-RIPE93-2026_v2_fyEOjnK.pdf | video: https://ripe93.ripe.net/media/videos/danesh-zeynali_the-state-of-ecn-adoption-in-the-internet_main_20261027-163400.mp4
Explicit congestion notification (ECN) is a signaling mechanism that enables a router along the network path between a sender and receiver to mark packets for signaling incipient congestion. More than a decade ago, Bauer et al. characterized the extent of ECN adoption on the Internet and a few years later Trammell et al. extended that analysis. Since then, the Internet has evolved substantially. Today, most operating systems support ECN, IPv6 has been widely deployed, and new technologies that build on ECN, such as L4S, have emerged. These changes naturally motivate the need to revisit the study of ECN adoption. We, hence, revisit and extend the two key ECN characterization efforts. We find that the majority of Internet service infrastructures are ECN-aware, although a nontrivial fraction of hosts, routers, and middleboxes bleach ECN bits. Many hyper-giants, unfortunately, bleach ECN bits along the path, which has substantial implications for the use of technologies such as L4S. In this study, we also note that IPv6 endpoints and paths generally show stronger support for ECN than those using IPv4.

### BigTime: Characterizing Large Time Service Providers
Speakers: Pascal Huppert , University of Twente
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/R3CHBN/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/R3CHBN/resources/Presentation_BigTime_RoAClZp.pdf | video: https://ripe93.ripe.net/media/videos/pascal-huppert_bigtime-characterizing-large-time-service-providers_main_20261027-164759.mp4
The Network Time Protocol (NTP) keeps the clocks of Internet-connected devices synchronized, which core applications and protocols depend on for proper functioning, including DNS caches, RPKI, and TLS. Next to free time servers (NIST, NTP Pool), large cloud providers and OS vendors such as Microsoft, Apple, and Google have begun operating their own time services and setting their billions of systems/devices to use their NTP servers by default. This creates a level of service centralization around these providers, and yet there has been little scrutiny of these services and their characteristics. In our paper, we characterize seven large time service providers in terms of replication architecture, client mapping, accuracy and service provided. We found a large variation in service replication (DNS and anycast), how they map clients to servers, and in their accuracy and (security) feature support. This includes violations of best practices, servers clocks being incorrect by up to 50ms on one occasion, the use of outdated NTP versions, and a lack of support for NTS, RPKI, and DNSSEC.

### Rooting Out Incorrect RIPE Atlas Probe Geolocations
Speakers: Katherine Izhikevich , University of California, San Diego - Computer Science Department
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/99HGKD/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/99HGKD/resources/ripe_ripe93_OzFJcHP.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/99HGKD/resources/ripe_ripe93_TfKzAv1.pptx | video: https://ripe93.ripe.net/media/videos/katherine-izhikevich_rooting-out-incorrect-ripe-atlas-probe-geolocations_main_20261027-170242.mp4
Geolocation plays a critical role in understanding the Internet. In this work, we analyze and fix operator-misreported geolocation. Using DNS root servers to detect speed of Internet violations, we conservatively infer that at least 2% of vantage points in the largest community-vantage point collection, RIPE Atlas, were not located at their operator-reported geolocation between January 2019 and April 2026. To increase the accuracy of future studies that use operator-reported geolocation, we open source our simple methodology, implement a reporting campaign of violating probes within RIPE, work with operators to fix the misreported geolocations, and release a continually updated dataset of RIPE vantage points that likely misreport geolocation.

### RIPE NCC Update
Speakers: Robert Kisteleki
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/NN8WJV/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/NN8WJV/resources/RIPE93-MAT-tools-upd_iugGxv4.pdf | video: https://ripe93.ripe.net/media/videos/robert-kisteleki_ripe-ncc-update_main_20261027-171256.mp4
This is a "regular" RIPE NCC update covering important changes since last time and a projection on what's to come regarding RIPE Atlas, RIPEstat and RIS.

### Closing notes
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/136/MCEU3B/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/MCEU3B/resources/mat_ripe93_chair_ope_HUR27iq.pdf | video: https://ripe93.ripe.net/media/videos/na_closing-notes_main_20261027-172434.mp4
Closing notes from the WG Chairs

## Security - Side Room (Tue, 16:00)

### Safety in Name Only - A Longitudinal Measurement Study of the .kids TLD
Speakers: Matteo Liberato , University of Twente
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/137/GQJZAR/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GQJZAR/resources/RIPE_RACI_Slides_fin_1S1PW0k.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GQJZAR/resources/RIPE_RACI_Slides_fi_tmWqe2S.pptx | video: https://ripe93.ripe.net/media/videos/matteo-liberato_safety-in-name-only-a-longitudinal-measurement-study-of-the-kids-tld_side_20261027-160524.mp4
The .kids top-level domain was delegated with an explicit mission: To provide a trusted, age-appropriate namespace for children, backed by a Registry Agreement that makes policy violations grounds for suspension or cancellation. We present the first longitudinal measurement study of .kids, covering its full operational lifetime from May 2022 through March 2026 across roughly 1,400 daily snapshots. We combine active DNS measurements from OpenINTEL, ICANN registry transaction reports, VirusTotal, Cloudflare Radar, Internet.nl, and abuse blocklists. Our results show the zone has not lived up to its mandate. Growth was driven by coordinated bulk-registration events rather than organic demand, over 85% of registrations use the minimum one-year term, and over 30% of the zone is non-operational at any given point. Among active domains, policy-violating content is disproportionately present. VirusTotal flags 3.7% of domains as malicious or suspicious, dominated by phishing that exploits the trust the .kids name conveys. Inspection of domain name strings alone reveals 176 apparent Registry Agreement violations. Of the 44 .kids domains that ever reached the Tranco top 1M, 23 are piracy or unauthorized streaming services and only 5 plausibly serve child-safe content. Blocklist-flagged domains persist in the zone for a median of 34 days, showing that the signal for harmful content is available but remediation is slow. Our findings illustrate that a policy framework is only as effective as its implementation, and speaks directly to the RIPE community's ongoing discussions on DNS operations, abuse handling, and Internet governance. We will discuss what these results mean for registries operating purpose-driven namespaces, for operators handling abuse reports, and for the policy debate around child safety online.

### Early Attestation is Very Harmful. Why is it Required?
Speakers: Muhammad Usama Sardar , GA4GH
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/137/GJXMGP/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/GJXMGP/resources/20261027_RIPE_93_Sec_e4tTL66.pdf | video: https://ripe93.ripe.net/media/videos/muhammad-usama-sardar_early-attestation-is-very-harmful-why-is-it-required_side_20261027-162413.mp4
Transport Layer Security (TLS) is a widely used protocol for secure channel establishment. However, it lacks an inherent mechanism for validating the security state of the workload and its platform. To address this, remote attestation can be integrated into TLS, which is referred to as attested TLS. At a high level, there are two key approaches for this integration, namely early (intra-handshake) and standard (post-handshake) attestation. We present insights from formal verification using the state-of-the-art symbolic security analysis tool ProVerif that led to the discovery of the critical- and high-severity CVEs in early attestation, potentially exposing the health data of more than 40 million Germans. In particular, we share our discovered critical-severity CVEs on two main concerns in early attestation, namely relay and diversion attacks. The root cause of these attacks is lack of binding to the connection and hardware, respectively. Examples include CVE-2026-33697, CVE-2026-100835, CVE-2026-112377, CVE-2026-108362, CVE-2026-108265 till CVE-2026-108269, CVE-2026-92701, CVE-2026-92702, CVE-2026-100835, each of CVSS 9.1, and other critical- and high-severity security concerns. The attendees will gain technical insights into the latest developments of standardization of attested TLS protocols in the IETF, and will be able to provide feedback on the standardization effort of attested TLS. Our analysis shows that: Early attestation generally reveals hardware-level information of the server, decreasing the security and privacy properties of the TLS connections, leading to a violation of the IETF SEAT charter. Early attestation can typically provide information about only boot-time Claims. Given the need for re-attestation, early attestation adds unnecessary complexity in the handshake. Early attestation leads to high handshake latency, timeouts, and failures. All use cases of early attestation can be handled with standard attestation while offering better security properties. Because of critical-severity CVEs and fundamental architecture problems in early attestation, we believe early attestation is very harmful to the TEE attestation ecosystem. We would like to discuss with the community whether it is necessary. References Internet-Draft: https://datatracker.ietf.org/doc/draft-intra-handshake-fail/ EarlyAttestationBleed paper: https://www.researchgate.net/publication/414529199_EarlyAttestationBleed_Three_Critical-severity_Vulnerabilities_of_CVSS_90_in_Confidential_Computing

### Running a CNA in the time of AI: A Language Community with a Package Manager (EEF)
Speakers: Alistair Woodman , Erlang Ecosystem Foundation (EEF)
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/137/UTNEPB/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/UTNEPB/resources/RIPE_93_-_EEF_AI_Vu__RFBpATu.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/UTNEPB/resources/RIPE_93_-_EEF_AI_Vu_hXUTu9m.pptx | video: https://ripe93.ripe.net/media/videos/alistair-woodman_running-a-cna-in-the-time-of-ai-a-language-community-with-a-package-manager-ee_side_20261027-163952.mp4
The Erlang Ecosystem Foundation (EEF) is the CNA (and EU CRA Steward] for > 20K Elixir, Erlang and Gleam FOSS packages. We have been a CNA for almost two years now. The talk will go through the evolution of our CNA from being ‘a quiet place prior to AI vuln scanning’ to what it is like today. We have seen an increase of over 50x in our CVEs load.

### Policy Proposal 2026-02 "Contractual Accountability Framework for Infrastructure-Level Network Abuse"
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/137/38XGJD/ | video: https://ripe93.ripe.net/media/videos/na_policy-proposal-2026-02-contractual-accountability-framework-for-infrastructure_side_20261027-165641.mp4
Discussion on Policy Proposal 2026-02 "Contractual Accountability Framework for Infrastructure-Level Network Abuse" - https://www.ripe.net/community/policies/proposals/2026-02/

### Security WG RIPE 93 Outro
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/137/S9XAP3/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/S9XAP3/resources/Security_WG_Slides_C_r5i228g.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/S9XAP3/resources/Security_WG_Slides__1lV5fVt.pptx | video: https://ripe93.ripe.net/media/videos/na_security-wg-ripe-93-outro_side_20261027-172904.mp4
A.O.B. Agenda for RIPE 94

## RIPE Community Plenary - Main Room (Thu, 16:00)

### RIPE Chair Team Update
Speakers: Mirjam Kühne , RIPE Chair
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/161/7DNKRN/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/7DNKRN/resources/RIPE_93_Community_Pl_IerzwCj.pdf | video: https://ripe93.ripe.net/media/videos/mirjam-kuhne_ripe-chair-team-update_main_20261029-160101.mp4
Updating the community on activities since the last RIPE Meeting.

### RIR Governance Document Update
Speakers: Andrei Robachevsky , Global Cyber Alliance/MANRS Constanze Buerger Herve Clement , ASO AC / Orange SA
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/161/UYCYH8/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/UYCYH8/resources/RIPE_93_RIR_Gov_Doc__086K4nY.pdf | video: https://ripe93.ripe.net/media/videos/andrei-robachevsky_rir-governance-document-update_main_20261029-162152.mp4
The NRO NC* started the process of updating and strengthening ICP-2: Criteria for Establishment of New Regional Internet Registries in 2024. In August this year, the NRO NC delivered its recommended draft document, the "ASO AC Recommended Draft RIR Governance Document", marking an important milestone in the work to update ICP-2. This document is the result of multiple global consultations with the RIR communities and ICANN stakeholders. NRO NC members Hervé Clément, Constanze Bürger and Andrei Robachevsky will provide an overview of the rationale for the latest draft and explain the key changes from Version 2, including updates to the Recognition and Derecognition processes, audit and compliance review provisions, emergency continuity arrangements, decision-making thresholds, ICANN’s role, and new safeguards for transparency and accountability. We invite you to join this session to understand how the proposed governance framework aims to support the stability, accountability, and self-governance of the Internet numbers registry system. *The Number Resource Organization Number Council (NRO NC) is also known as the Address Supporting Organization Address Council (ASO AC) within ICANN, where it serves as the body responsible for overseeing global policy development related to Internet number resources.

### RIPE Fellowship - Update about the new Programme
Speakers: Michela Galante , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/161/KQV3K8/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/KQV3K8/resources/The_RIPE_Fellowship__FFj92lr.pdf | video: https://ripe93.ripe.net/media/videos/michela-galante_ripe-fellowship-update-about-the-new-programme_main_20261029-164934.mp4
One year into the revamped RIPE Fellowship Programme, this presentation looks at why it was redesigned, what we have learned, and what comes next. The new three months journey aims to bring new voices into the RIPE Community and foster meaningful, longer term engagement, supported by a dedicated RIPE Coach. After two editions, one still ongoing, we will share early results, the diversity of RIPE Fellows selected through an external review process, and the challenges that remain, including geopolitical and visa related barriers. The success of the Programme depends on the RIPE Community. Help us spread the word and share the opportunity with your network: your friend or colleague could be the next one to join the RIPE Community.

### Open Mic.
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/161/YD3XV7/ | video: https://ripe93.ripe.net/media/videos/na_open-mic_main_20261029-171851.mp4
Any other business

## BoF - Main Room (Mon, 18:00)

### Let's talk about some topics of interest at the IETF
Speakers: Suresh Krishnan , Internet Architecture Board
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/127/QKQXWT/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/QKQXWT/resources/RIPE_93_IETF_v6_EBjRjjA.pdf | video: https://ripe93.ripe.net/media/videos/suresh-krishnan_lets-talk-about-some-topics-of-interest-at-the-ietf_main_20261026-180151.mp4
We go over a list of key topics that have been recently discussed in the IETF and have relevance to the RIPE operator community. The goal of the session is to inform and to collect feedback from the operator community and feed it into the IETF process. The session will be less about presentation and more about interaction. Topics include Agentic AI, Post Quantum Cryptography, Energy Efficiency, DNS etc.

## BoF - Side Room (Mon, 18:00)

### Maybe it is time to consider layer 3 internet exchanges
Speakers: James Rice , Jump Networks Ltd
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/245/MVTX9A/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/MVTX9A/resources/layer_3_ix_presentin_9tu0wAm.pdf | video: https://ripe93.ripe.net/media/videos/james-rice_maybe-it-is-time-to-consider-layer-3-internet-exchanges_side_20261026-175849.mp4
A panel and audience discussion with James Bensley (inter.link), Richard Petrie (LINX), Tom Strickx (Cloudflare), Paul Thornton (Lightning Fibre), Chris Van Fossen (Google) and Blake Willis (Zayo), opened by James Rice (Jump Networks) with the case for layer 3 internet exchanges. Internet exchanges have presented as shared layer 2 networks for thirty years, while the rest of the industry has replaced large layer 2 domains with routed ones. The case: forwarding at layer 3, with each port a point-to-point link to the exchange’s routers in place of a shared broadcast domain with route servers, for correct forwarding, shorter paths and transit-standard features, with a worked example from this year of where a shared peering LAN falls short. The rest of the hour is for the panel and the audience: given the choice, would your network prefer a layer 3 exchange port to a layer 2 one, and which exchanges would want to offer it?

## Diversity, Equity and Inclusion in Tech - Main Room (Tue, 18:00)

### Welcome and Introduction. Session Theme: Can You Hear Me? (Being heard: the I in DEI)
Speakers: Denesh Bhabuta
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/139/J33PTJ/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/J33PTJ/resources/DeneshBhabuta-DEI-in_1IPHqVI.pdf | video: https://ripe93.ripe.net/media/videos/denesh-bhabuta_welcome-and-introduction-session-theme-can-you-hear-me-being-heard-the-i-in_main_20261027-180001.mp4
Session Theme: Can You Hear Me? Being heard: the I in DEI At RIPE 91 this session looked at diversity: who is in the room. At RIPE 92 we turned to equity: who can get to the room, and what stands in their way. At RIPE 93 we reach the last letter of DEI, and perhaps the hardest to see. Inclusion is not just being present. It is being heard. Do you feel you belong? Does anyone listen when you speak? Can you shape what happens next, including who leads? Diversity you can count. Inclusion you mostly feel… and the people who feel it least are often the ones we rarely hear from. As before, we start with human stories. Two short talks look at whose voices go unheard in our community. One raises a need many people quietly share but seldom speak about. The other asks who gets heard once they are here, and who gets trusted to lead. Then the floor is yours. Bring an experience, an idea or a question… and be heard.

### I sent my children around the city without supervision. This is what happened.
Speakers: Maria Matejka , BIRD | CZ.NIC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/139/HALSRM/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/HALSRM/resources/meeting-with-kids_eIeq60d.pdf | video: https://ripe93.ripe.net/media/videos/maria-matejka_i-sent-my-children-around-the-city-without-supervision-this-is-what-happened_main_20261027-180434.mp4
We have childcare for parents with little ones but when the children get too old, there is nothing. One can't leave them alone at home for multiple days yet, but they would overwhelm the available childcare. Recently, I did an experiment, and this is what happened. Maybe I'm not the only one looking for options. Let's share.

### From Seat to Say: Inclusion and the boards that lead us
Speakers: Denesh Bhabuta
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/139/C7MXVN/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/C7MXVN/resources/DeneshBhabuta-DEI-in_eEuktre.pdf | video: https://ripe93.ripe.net/media/videos/denesh-bhabuta_from-seat-to-say-inclusion-and-the-boards-that-lead-us_main_20261027-183621.mp4
When we elect the boards of our Internet organisations, how do we decide? For many of us, it is the names we recognise. But being recognisable depends on being able to travel, being free to leave home, already being in the network, and having enough time to decide whether to stand. This talk doesn’t offer a single fix. Instead it follows the journey from seat to say and asks questions we rarely ask out loud. What would make it easier for someone new to stand? Once people are on a board, are they heard, or simply present? And how do members stay involved between elections, when oversight often rests on a single annual meeting? Along the way it shares ideas others in the sector have tried. The rest is over to you.

### Open microphone
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/139/GKXUFM/
Any other business

## BoF - Main Room (Thu, 18:00)

### Connecting Research and Operations
Speakers: Jelena Cosic , RIPE NCC
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/163/KMXXGU/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/KMXXGU/resources/In_the_age_of_AI_-_R_4866HgC.pdf | slides: https://pretalx.ripe.net/media/ripe-93/submissions/KMXXGU/resources/BoF_Opening_slides_-_e9tyAOn.pdf | video: https://ripe93.ripe.net/media/videos/jelena-cosic_connecting-research-and-operations_main_20261029-180047.mp4
Agenda: Welcome 5 min Research collaborations – in the Era of AI 10min Daniela Brauner, GÉANT Industry-Academia collaboration: a small tech company perspective 10min Giovane C. M. Moura, SIDN Labs and TU Delf Open Discussion 35min Researchers and network operators within the RIPE community share a common goal: understanding and improving how the Internet works. Researchers bring analytical methods and time to investigate complex problems, while operators have first-hand experience running networks and understanding the practical challenges of deployment. Although these perspectives are highly complementary, collaboration between the two communities often relies on existing personal contacts or chance encounters. Researchers may struggle to find operational partners, datasets, or opportunities to validate their work, while operators may have important research questions but lack the time, resources, or academic connections to investigate them. Building on discussions and a flip-chart experiment conducted at RIPE 92 that explored opportunities for research–operations collaboration, this BoF session will explore how the RIPE community can make collaboration between researchers and operators easier. The goal is to understand existing barriers, gather experiences from both communities, and discuss what kinds of support mechanisms, if any, would be valuable. To help ground the discussion in practical experience, we have invited representatives from GÉANT's FAIR Data Portal to briefly share lessons learned from building a community initiative around responsible operational data sharing. While operational data sharing is an important aspect of collaboration, the discussion is intentionally broader and will also cover identifying research questions, validating results in operational environments, establishing long-term partnerships, and improving communication between the two communities. Discussion Focus The BoF will be an open discussion centred around questions such as: - What are the biggest obstacles to collaboration between researchers and network operators? - How can researchers better communicate their needs for data and operational feedback? - What practical, technical, legal, or organisational barriers make operational data difficult to share? - Would the community benefit from lightweight mechanisms such as recurring matchmaking sessions, shared repositories of datasets or research questions, reusable data-sharing frameworks, or other forms of coordination? - What role, if any, should the RIPE NCC play in supporting these activities? Participants are encouraged to share concrete experiences, successful collaborations, challenges, and ideas for improving these valuable connections. Format The session is intended to be discussion-driven rather than presentation-heavy. Intended Audience Network operators Internet and networking researchers NREN representatives Everyone interested in collaboration between research and operations Expected Outcome The BoF aims to better understand the challenges that currently limit collaboration between researchers and network operators, identify areas where the RIPE community could lower these barriers, and assess whether there is interest in developing mechanisms to facilitate future collaboration. The discussion will help inform any future initiatives by the RIPE community or the RIPE NCC in this area. Moderation: The session will be moderated by Jelena and Ulka from the RIPE NCC.

## BoF - Side Room (Thu, 18:00)

### Practical AI BoF (Part 2)
Speakers: David Verolme , Solcon Sander Steffann , Hilco ProVision Anna Wilson , RIPE Vice Chair Stefan Wahl , ROUTE 128
page: https://ripe93.ripe.net/programme/meeting-plan/sessions/164/QM3GCC/ | slides: https://pretalx.ripe.net/media/ripe-93/submissions/QM3GCC/resources/RIPE93_Practical_AI_NsHvplq.pptx | slides: https://pretalx.ripe.net/media/ripe-93/submissions/QM3GCC/resources/Ripe93-ai-bof-qf32_1CQTFme.key | video: https://ripe93.ripe.net/media/videos/david-verolme_practical-ai-bof-part-2_side_20261029-180014.mp4
AI is getting a lot of attention, but not everything being discussed is useful in practice. This BoF focuses on real-world AI use cases for network engineers, operators, and ISPs that can be applied today. Through practical examples, we’ll look at what works, what doesn’t, and what lessons people have learned while putting AI into production.

