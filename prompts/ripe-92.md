>>> HOW TO RUN THIS <<<
This is the digest prompt for ripe-92. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ripe-92.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ripe-92.md
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

Below is the program for RIPE 92 (Edinburgh) (operator). Read it and produce a digest
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
conference: RIPE 92 (Edinburgh)
type: operator
source_url: https://ripe92.ripe.net/programme/meeting-plan/
generated: 2026-11-01
registry_key: ripe-92
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Tutorial - Main Room (Mon, 09:00)

### VXLAN and EVPN on Linux (with BIRD)
Speakers: Maria Matejka , BIRD | CZ.NIC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/59/7JB8K9/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/7JB8K9/resources/evpn-vxlan-tutorial_WTl2IbG.pdf | video: https://ripe92.ripe.net/media/videos/maria-matejka_vxlan-and-evpn-on-linux-with-bird_main_20260518-090103.mp4
Walking through basic setups of VXLAN and EVPN on Linux. Starting with manual setup and troubleshooting to actually understand what is happening under the hood, and slowly adding more layers to make the network scalable. While regular workshops on VXLAN and EVPN often rely on commercial technologies, we'll focus on BIRD on Linux, letting everybody keep their setup for future fiddling.

## Tutorial - Side Room (Mon, 09:00)

### RIPE Public Speaking Workshop
Speakers: Gerardo Viviers , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/60/Q7PYLQ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/Q7PYLQ/resources/RIPE_Public_Speaking_XHMFG5f.pdf
RIPE meetings rely on the open exchange of ideas, but good technical work needs good delivery. This 90-minute tutorial is the final step in our new public speaking workshop. We started the development of this workshop on the request of the RIPE Chair team. We have prepared some pre-event material to cover the theory of "storytelling" and "slide design", but in this live session what we want to do focuses entirely on delivery. We want to give the people the opportunity to practise stage presence, microphone handling, and managing nerves before the full-on RIPE meeting starts. This session is open to everyone, whether they are a first-time speaker, a Working Group Chair, or just someone that wants to work on their public speaking skills.

## Plenary - Main Room (Tue, 09:00)

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Speakers: Thomas Weible , FLEXOPTIX
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/72/Q9YPAZ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/Q9YPAZ/resources/Flexoptix_-_Channelm_4BcipnC.pdf | video: https://ripe92.ripe.net/media/videos/thomas-weible_channelmania-future-proof-your-dwdm-network-topology-while-keeping-it-flexibl_main_20260519-090025.mp4
In the old days of traditional separation of IP and DWDM, there was no need for IP folks to care about much other than what they used on their routers/switches (while the transport team ran the DWDM infra). These past DWDM infra approaches for maximizing the data capacity per fiber pair went for running more and more DWDM channels with grid spacings as small as possible. This meant that grid spacings shrank from 200GHz to 100GHz and then 50GHz with some applications even going for 25GHz. Now in the age of IPoDWDM the bandwidth per channel keeps increasing, as complex modulation schemes come into favor over ON-OFF-Keying which has been the de facto standard so far. Those increased per channel bandwidths of 400Gbps, 800Gbps and now pushing into the 1.6Tbps realm demand for larger grids to accommodate the spectrum necessary to operate such “Superchannels”. Especially the fact of coherent detection being “blind” to anything but its own wavelength has enabled interesting topologies that can omit filters altogether. Of course that comes at a cost of reduced flexibility. Which means, IP folks now will need to understand the nuances of how coherent detection works, need for larger filters for 800Gbps and higher, and how 400GHz filters (key word here being COTS) would future proof your network by not only allowing you to grow to 1.6Tbps, but also allow backwards compatibility for legacy services on 50GHz, etc. Made by FLEXOPTIX Research - Gert and Thomas.

### Transient and Drifting: packet-level identity privacy and location privacy using IPv6 addressing
Speakers: Saleem Bhatti , University of St Andrews, UK
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/72/PPRAZL/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/PPRAZL/resources/20260519_ilnp_ripe92_Zloxt6m.pdf | video: https://ripe92.ripe.net/media/videos/saleem-bhatti_transient-and-drifting-packet-level-identity-privacy-and-location-privacy-using_main_20260519-093019.mp4
Improving communication privacy for the Internet is increasingly important for users. Although there are various forms of protection for communication privacy at various communication layers, Internet communication requires packet addressing information to remain visible for correct forwarding of packets. So, address bits could be used for tracking individual users in terms of network usage and location, as well as building a picture of service usage through flow correlation. This talk describes an approach to packet-level addressing that provides enhanced protection against such privacy attacks. The approach only requires updates to the end-systems, works over existing networks and for existing applications, and can be deployed incrementally.

### Evolution of Meta's Edge and Backbone Networks
Speakers: Fredrik Korsbäck , Meta Platforms, Inc Fredrik Korsback , Meta
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/72/TBKG3W/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TBKG3W/resources/Meta_RIPE_Z6Steot.pdf | video: https://ripe92.ripe.net/media/videos/fredrik-korsback_evolution-of-metas-edge-and-backbone-networks_main_20260519-100207.mp4
This abstract explores the multifaceted evolution of Meta's network architecture—specifically the Backbone and Edge—in response to unprecedented traffic demands and the emergence of latency-sensitive AI workloads. The presentation first details the scaling journey of the Backbone network, which has achieved over 10X growth through a strategic combination of DC Metro Architecture, platform Scaling Up (e.g., faster interfaces), and Scaling Out (e.g., multiple devices per plane). A key enabler of this massive scale and efficiency is the deployment of IP and Optical Integration using ZR technology, resulting in significant power and space savings within our network sites. Next, we examine the transformation of the Edge network, driven by a shifting traffic profile heavily influenced by new AI use-cases. To meet the demand for lower-latency experiences and uncacheable, unique content generation, Meta is building an Elastic Edge that strategically moves compute resources, including a global GPU footprint, closer to end-users. This new compute locality is crucial for optimizing user experience and allows for a more efficient use of our infrastructure by reducing costly backbone traffic. Finally, we discuss updates to our Peering strategy, including a move away from Route-Server Peering and the launch of an Automated Peering Portal. We clarify that this shift to automated, bilateral peering is intended to simplify and accelerate connections for thousands of smaller networks globally, but importantly, it does not constitute a change in our fundamental peering policy or our commitment to the open Internet.

## Connect - Main Room (Wed, 09:00)

### Opening and Housekeeping
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/ZCPRZV/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ZCPRZV/resources/Connect_wg-92_Agenda_0rB03mP.pdf | video: https://ripe92.ripe.net/media/videos/na_opening-and-housekeeping_main_20260520-090011.mp4
Welcome from the WG Chairs, agenda, RIPE 91 meeting notes

### Engaging with the Product Committee
Speakers: Leo Vegoda , Co-Chair
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/VRHYLH/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/VRHYLH/resources/Engaging_with_the_Pr_TsQpq7f.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/VRHYLH/resources/20260520_RIPE_92_Co_A99am8Y.pptx | video: https://ripe92.ripe.net/media/videos/leo-vegoda_engaging-with-the-product-committee_main_20260520-090254.mp4
This talk explains how people can engage with PeeringDB's Product Committee. It describes the decision making process in high level and then looks at the hurdles and the questions the Product Committee thinks about. It then moves on how to engage with PeeringDB and how its volunteers engage with its users.

### Creating a peering portal with Peering Manager
Speakers: Guillaume Mazoyer
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/CBSJHG/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CBSJHG/resources/gmazoyer_ripe92_conn_o0J6NYA.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CBSJHG/resources/gmazoyer_ripe92_conn_JultMag.key | video: https://ripe92.ripe.net/media/videos/guillaume-mazoyer_creating-a-peering-portal-with-peering-manager_main_20260520-091340.mp4
Peering Manager is an open source project which aims to help networks with their peering workflows. It is able to record BGP sessions, usually set up on the edge of an autonomous system, to be able to automate and smooth their management. Being able to expose publicly a peering portal for others to request peering with a network has been a long-lasting feature request from Peering Manager users. This feature is now being brought to life. This talk will be about showing how to set up such a portal with Peering Manager taking care of the heavy work.

### Persistent unknown unicast - A peering-LAN case study
Speakers: James Rice , Jump Networks Ltd
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/YZVWHG/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/YZVWHG/resources/ripe92-persistent-un_bP27w0R.pdf | video: https://ripe92.ripe.net/media/videos/james-rice_persistent-unknown-unicast-a-peering-lan-case-study_main_20260520-093506.mp4
Unknown unicast on shared peering LANs is widely assumed to be transient. This case study presents the opposite: a self-perpetuating mechanism via RFC 4861 §7.3.1 forward-progress confirmation, where a single MAC change can leave a stale neighbour entry REACHABLE indefinitely while customer traffic — HTTPS SNI, signalling, residential 999 calls — is flooded to hundreds of member ports. A reproducible demonstration was published in November 2024. The talk presents the mechanism at the kernel and protocol level, a five-year timeline of reports and partial remediations at one IXP, the categories of disclosure and safety-of-life exposure at stake, and operational lessons for IXP operators and members. It closes on the speaker's open self-examination: did I do enough on behalf of my customers?

### Beyond Peering LANs: Representing IXP Services in a World That No Longer Fits the Schema
Speakers: Stefan Wahl , Route128 GmbH (CTO) and Euro-IX (Board Member)
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/TJQHUD/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TJQHUD/resources/beyond_peering_lans-_OZOmmp4.pdf | video: https://ripe92.ripe.net/media/videos/stefan-wahl_beyond-peering-lans-representing-ixp-services-in-a-world-that-no-longer-fits-th_main_20260520-095502.mp4
For most of its history, the IXP directory model has been based on the assumption that an IXP is a peering LAN. A member connects to it using an ASN and a port and the directory describes this relationship. IXPDB, PeeringDB and the tools built on top of them all reflect this model. Recent work in the Connect Working Group has rightly advocated for better authoritative IRR data in the directory layer and the IXPDB IRR implementation is one outcome of this. However, the operational reality at many IXPs is evolving faster than the schema. The recent SFMIX case study at Euro-IX Vienna demonstrated an IXP running a parallel opt-in service: a separate ASN, partial routes, hosted caches, VRF-leaking by BGP community and a distinct commercial model running alongside the traditional L2 fabric. SFMIX is far from alone; cloud on-ramps, multi-site fabrics and remote-peering arrangements are all stretching the directory model in similar ways. A consumer asking „who can I peer with at IXP X?“ increasingly receives an incomplete picture. This talk will examine the current state of the directory layer in this environment. Drawing on the IXPDB IRR work and ongoing discussions with PeeringDB, I will outline where the current schema breaks down (multi-ASN service offerings, opt-in services, service tiers, non-LAN peering at an IXP location), what concrete extensions have been prototyped or proposed and where the design choices have real consequences for downstream consumers (route server operators, member networks, automation pipelines and the BCOP work itself). The intent is to leave the Working Group with a working list of ideas that could be implemented by the directories, IXPs and with the help of the Working Group itself.

### The Value of a Full route peer for a route collector project
Speakers: Nina Bargisen , RouteViews
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/N3SND7/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/N3SND7/resources/The_Value_of_a_Full_85hOjZt.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/N3SND7/resources/RV-LightningTalk-RI_YQSt3vS.pptx | video: https://ripe92.ripe.net/media/videos/nina-bargisen_the-value-of-a-full-route-peer-for-a-route-collector-project_main_20260520-101541.mp4
RouteViews now operates 50+ collectors with hundreds of peering sessions, and every session has a storage and operational cost. This talk introduces a per-session value metric — the unique information each session adds across edges, paths, prefixes, origins, and shorter paths. Examples spanning a Tier-1, two content providers, a regional provider, and a regional peer show that edge networks with full routes carry the unique signal, while Tier-1 transit and peer-only sessions contribute less information wrt the topology of the Internet

### AOB and Closing
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/84/GDJUW7/ | video: https://ripe92.ripe.net/media/videos/na_aob-and-closing_main_20260520-102942.mp4
Closure

## Open Source - Side Room (Wed, 09:00)

### Web Application Security - an IXP Manager Perspective
Speakers: Barry O'Donovan , INEX
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/85/TV3Y7W/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TV3Y7W/resources/RIPE92-Edinburgh-BOD_tD5a0Rv.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TV3Y7W/resources/RIPE92-Edinburgh-BO_KD2qjVt.pptx | video: https://ripe92.ripe.net/media/videos/barry-odonovan_web-application-security-an-ixp-manager-perspective_side_20260520-090330.mp4
IXP Manager is built with a security-first, secure-by-design approach. As a 20-year-old project, we have had to regularly revisit past assumptions and update them to align with current best practices. One of the best ways of doing this is to have our work checked by independent third parties. ENISA, the European Union Agency for Cybersecurity, established the Cybersecurity Support Action Programme to provide cybersecurity services to Member States. Under this program, IXP Manager underwent a seven-day "grey-box" web application vulnerability assessment in February 2026. This presentation will discuss web application security in general, IXP Manager's experience with third-party penetration tests, the results of this specific test, and how these can be applied to web applications.

### Nominet DNS Fund - how are we adapting to what we have learnt?
Speakers: Amy O'Donnell , Nominet Dave Knight , Nominet
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/85/GLDW8A/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/GLDW8A/resources/NominetDNSFund_RIPE9_mNK9LT5.pdf | video: https://ripe92.ripe.net/media/videos/amy-odonnell_nominet-dns-fund-how-are-we-adapting-to-what-we-have-learnt_side_20260520-092624.mp4
Underfunded open source DNS projects create systemic risks, exposing millions of users to vulnerabilities and threatening the stability and security of the entire internet. The Nominet DNS Fund aims to tackle these critical gaps by investing in the security, resilience, and long-term viability of these essential open source components, recognising that a robust and secure DNS is fundamental to the internet’s continued operation and the public benefit it provides. Having completed our first round of funding in 2025 and extending in 2026, this session will share highlights including: RESEARCH Revisiting research conducted by Demos that led us to create the fund: to what extent have we addressed some of the challenges and where do we have further to go? LEARNING What did we learn from looking at other funds and how did we intentionally do some things differently from others? Did that work well or not in our pilot round? Analysis of key learning about implementing the fund, including surprises and challenges we face moving forward. ITERATE Demonstrate how our learning has shaped our future direction, as well as ideas where we'd like to improve. A chance for applicants to ask questions about funding opportunities and offer feedback or reflection on the fund.

### Developing Containerlab - an open-source success story
Speakers: Gordon Gidofalvy , Containerlab, Nokia
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/85/JDMLST/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/JDMLST/resources/Containerlab_Develop_Dk4ofH4.pdf | video: https://ripe92.ripe.net/media/videos/gordon-gidofalvy_developing-containerlab-an-open-source-success-story_side_20260520-094658.mp4
Containerlab turns 6 this year - with over half a million installs, a rich ecosystem, plenty of write-ups, blogposts and repositories using it, it has become a popular project for creating virtual network topologies. This talks is not aimed at presenting the tool itself, but rather the development process, and what worked for the project, what did not, and what challenges we faced while developing and maintaining a tool that has to support traditionally closed-source software and engage with a non-software developer userbase.

### How much of BIRD is vibecoded
Speakers: Maria Matejka , BIRD | CZ.NIC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/85/ANS3JF/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ANS3JF/resources/vibecoding-bird_zChFz02.pdf | video: https://ripe92.ripe.net/media/videos/maria-matejka_how-much-of-bird-is-vibecoded_side_20260520-100918.mp4
In BIRD, we are getting various questions and inputs from the community about using LLM assistance for BIRD development, and also sometimes (probably) LLM-generated contributions. This is a report on what worked for us so far and what not.

### Netiscope - a local network environment debugging tool
Speakers: Robert Kisteleki
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/85/Q3SBEN/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/Q3SBEN/resources/Netiscope_-_RIPE92_O_Th1j3xE.pdf | video: https://ripe92.ripe.net/media/videos/robert-kisteleki_netiscope-a-local-network-environment-debugging-tool_side_20260520-102559.mp4
Netiscope is an attempt to provide an Open Source local network issue debugging tool. It is intended to be a single tool to help the user figuring out what the local network conditions are, in case "something is off". With a modular design it is capable of including tests for connectivity issues, DNS problems, the presence of undesired firewalls or MITMs, etc.

## IPv6 - Main Room (Thu, 09:00)

### The year of IPv6-only desktop
Speakers: Ondřej Caletka , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/94/PBHCLK/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/PBHCLK/resources/RIPE_92_-_The_year_o_djkzlI7.pdf | video: https://ripe92.ripe.net/media/videos/ondrej-caletka_the-year-of-ipv6-only-desktop_main_20260521-090610.mp4
With the advent of IPv6-mostly networks, we are finally getting to a state where native IPv4 is becoming optional in access networks. What started more than a decade ago in mobile operating systems is now slowly happening in desktop computers as well - pioneered by macOS, proper IPv6-only support is now also available as a preview on Windows 11 and in the NetworkManager on Linux.

### IPv6-only Network Design
Speakers: Wilhelm Boeddinghaus , CEO Route 128 GmbH
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/94/XJWGCT/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/XJWGCT/resources/RIPE92-May-2026-IPv6_MmzPXy4.pdf | video: https://ripe92.ripe.net/media/videos/wilhelm-boeddinghaus_ipv6-only-network-design_main_20260521-093558.mp4
464XLAT is a well known technology to implement IPv6-only networks in mobile networks. This technology will now become available in mainstream enterprise networks with the introduction of the WinCLAT feature in Windows 11 Beta. Enterprises will now be able the build IPv6-only networks. This talk gives an introduction to WinCLAT and shows the advantages of running an IPv6-only network in enterprises.

### IPv6 Routing Loops Update
Speakers: Maynard Koch , TU Dresden
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/94/LXPTTU/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/LXPTTU/resources/RIPE92-routing-loops_lAElWMp.pdf | video: https://ripe92.ripe.net/media/videos/maynard-koch_ipv6-routing-loops-update_main_20260521-100933.mp4
Routing loops and the amplification of looping packets are known problems on the IPv6 Internet. In a recent measurement study, we found that both problems are still present, potentially harming Internet stability. Loops are easy to fix, but they seem to lack attention from the network operator community. In this talk, we aim to raise awareness about routing loops and amplification of looping packets. We provide an update on the current state of these issues on the IPv6 Internet, with a focus on the RIPE region. Hopefully, these misconfigurations will be solved in the future. To assist in resolving these problems, we have made our findings publicly available at https://ipv6-sra.realmv6.org/routingloops, allowing operators to check whether their networks are affected by routing loops.

### The Killer App for IPv6
Speakers: Benedikt Stockebrand
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/94/THKMSP/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/THKMSP/resources/Stockebrand-IPv6-Kil_Z5sxFZM.pdf | video: https://ripe92.ripe.net/media/videos/benedikt-stockebrand_the-killer-app-for-ipv6_main_20260521-101554.mp4
For 25 years we have been desperately searching for a Killer App for IPv6. We found it!

## Database - Side Room (Thu, 09:00)

### Welcome to the RIPE 92 Database WG
Speakers: David Tatlisu Peter Hessler
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/95/CYZP3N/ | video: https://ripe92.ripe.net/media/videos/david-tatlisu_welcome-to-the-ripe-92-database-wg_side_20260521-090030.mp4
Welcome Scribe Agenda

### NWI Update
Speakers: David Tatlisu Peter Hessler
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/95/FZKSVY/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/FZKSVY/resources/NWI_update_v1_ahy8aZ6.pdf | video: https://ripe92.ripe.net/media/videos/david-tatlisu_nwi-update_side_20260521-090228.mp4
This working group structures smaller changes to the RIPE database into numbered work items. This talk serves as a brief update on what has happened since the last RIPE meeting.

### RIPE NCC Operational Update
Speakers: Ed Shryane
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/95/WNKKMB/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/WNKKMB/resources/RIPE92_DB-WG_Operati_DQUwoGM.pdf | video: https://ripe92.ripe.net/media/videos/ed-shryane_ripe-ncc-operational-update_side_20260521-090440.mp4
Operational Update from the RIPE NCC Database team

### Reliable IRR mirroring with NRTMv4
Speakers: Sasha Romijn , Reliably Coded (IRRD, IRRexplorer, internet.nl)
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/95/N7HBNS/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/N7HBNS/resources/slides-dark-1_FdGYxS0.pdf | video: https://ripe92.ripe.net/media/videos/sasha-romijn_reliable-irr-mirroring-with-nrtmv4_side_20260521-095320.mp4
Near Real Time Mirroring (NRTM) v3 has been the standard for IRR database mirroring for decades, but it has significant problems: no integrity verification, poor scalability, no formal specification, and reliability issues that are hard to diagnose. It can break in fascinating yet invisible ways, allowing mirrors to silently run out of sync. NRTMv4 is its replacement. It uses HTTPS transport, detects and recovers from synchronization issues, uses cryptographic signing to guarantee integrity, and is designed to scale where needed. The RIPE side of this work took place under NWI-12. The draft is currently in IETF Last Call and already implemented in both the RIPE Database and IRRD. As co-author of the protocol and the author of IRRD's NRTM implementations, I'll discuss protocol design, trade-offs, how to migrate, and what you should know.

### Closing and WG chair selection
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/95/D8QHDS/ | video: https://ripe92.ripe.net/media/videos/na_closing-and-wg-chair-selection_side_20260521-101208.mp4
Closing WG chair selection AOB

## Plenary - Main Room (Fri, 09:30)

### Lazy Eye Inspection: Capturing the State of Happy Eyeballs Implementations
Speakers: Patrick Sattler , Technical University of Munich
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/109/ADKYKR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ADKYKR/resources/slides_pENQGHL.pdf | video: https://ripe92.ripe.net/media/videos/patrick-sattler_lazy-eye-inspection-capturing-the-state-of-happy-eyeballs-implementations_main_20260522-092948.mp4
During the transitioning to an IPv6-only communication, many devices and networks settled on a dual-stack setup. IPv4 and IPv6 are available to these hosts for new connections. Happy Eyeballs (HE) describes a mechanism to prefer IPv6 for such hosts while ensuring a fast fallback to IPv4 when IPv6 fails. The IETF is currently working on the third version of HE which includes more connection setup parameters (e.g., ALPN). While the standards include recommendations for HE parameter choices, it is up to the client and OS to implement HE. This talk presents the state of HE in various clients, particularly web browsers. Measuring and evaluating these properties help to find and understand IPv6 deployment hurdles. We introduced a framework to analyze and measure clients’ HE implementations and parameter choices. Additionally, we implemented a web-based measurement tool. This tool is publicly available to the community (https://www.happy-eyeballs.net) and measures the browser’s HE behavior. According to our evaluation, only Safari supports all HE v1 and v2 features. Safari is also the only client implementation in our study that uses a dynamic IPv4 connection attempt delay, a resolution delay, and interlaces addresses. We further show that problems with the DNS A record lookup can even delay and interrupt the network connectivity despite a fully functional IPv6 setup with Chrome and Firefox. All major browser engine developer teams claim to work on implementing the HEv3 draft. We are currently extending our measuring tool to support HEv3 measurements. Our tool and evaluation is not only useful for browser vendors but also to network operators and content providers. The results can help to understand and identify user complains related to IPv4/IPv6 connectivity.

### IAB Workshop Report on IP Address Geolocation
Speakers: Dhruv Dhody , IAB Chair Warren Kumari , Google LLC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/109/ALJTW7/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ALJTW7/resources/RIPE92-IPGeo-Lightni_tvmmRN9.pdf | video: https://ripe92.ripe.net/media/videos/dhruv-dhody_iab-workshop-report-on-ip-address-geolocation_main_20260522-095800.mp4
The IAB IP Address Geolocation Workshop examined how IP-based geolocation is widely used across content delivery, compliance, and network optimization, despite well-known limitations in accuracy, transparency, and privacy. This presentation summarizes key findings from the workshop, including gaps in current practices, architectural implications of relying on IP-derived location, and emerging directions such as alternative signals and improved data distribution mechanisms.

### Do not drop ASPA invalids of the last resort
Speakers: Ondřej Caletka , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/109/ZT9NYU/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ZT9NYU/resources/RIPE_92_-_Do_not_dro_d1CHONF.pdf | video: https://ripe92.ripe.net/media/videos/ondrej-caletka_do-not-drop-aspa-invalids-of-the-last-resort_main_20260522-101213.mp4
During RIPE 92, we did ASPA validation and dropped invalid paths in the meeting network. During that we discovered some reachability issues that have not been considered by us before.

## Plenary - Main Room (Tue, 11:00)

### RPKI: Do we need Garbage Collection now?
Speakers: Antonis Chariton , AS4601 | Cisco
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/74/HD3MND/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/HD3MND/resources/rpki-gc-merge-emoji_FTR8fda.pdf | video: https://ripe92.ripe.net/media/videos/antonios-chariton_rpki-do-we-need-garbage-collection-now_main_20260519-110128.mp4
After getting a new ASN assigned by RIPE NCC that had pre-existing ROAs authorizing it to originate other people's IPv4 addresses I set out to discover how prevalent this problem is. Was it luck, or are we re-assigning previously used numbers that come with RPKI luggage frequently? As it turns out, new assignments with valid ROAs are common. What do we do now? Do we have to worry, or is this acceptable? Will RPKI eventually accumulate garbage like IRR has? This Plenary session will have a followup discussion with more results and conversation in the Address Policy WG under title "Discussion on AS Reallocation".

### OpenPenny: Identifying Legitimate Traﬃc to Reduce Monitoring Noise
Speakers: Petros Gigis , UCL
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/74/UWTWQR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/UWTWQR/resources/openpenny-slides-rip_N1gyaTN.pdf | video: https://ripe92.ripe.net/media/videos/petros-gigis_openpenny-identifying-legitimate-traffic-to-reduce-monitoring-noise_main_20260519-113501.mp4
To perform day-to-day network monitoring and understand where traffic enters and traverses their networks, operators rely on packet counters (e.g., sFlow) and control-plane data. Although these tools can detect traffic, they cannot determine the true origin of the observed traffic. This observability limitation creates uncertainty: when ISPs detect unexpected changes in traffic, they cannot know if this change is due to a routing misconfiguration, a policy violation, a stealthy hijack, or is just spoofed background noise. As a result, many alerts are noisy and not actionable. In this talk, we present OpenPenny, an open-source tool that introduces a new data-plane primitive for validating whether traffic aggregates are non-spoofed. OpenPenny builds on Penny, a research prototype that exploits TCP’s reliable retransmission mechanism. In any legitimate TCP connection, when packets are lost, the receiver notifies the sender after a few RTTs, and the sender eventually retransmits them (closed-loop behavior). In contrast, spoofed traffic is open-loop: there is no interaction between the sender and the receiver, and thus it cannot react to missing data and retransmit it. Based on this observation, OpenPenny carefully drops a few packets and waits to see whether they are retransmitted, in order to infer whether the traffic is closed-loop and genuine. We then present OpenPenny’s design for deployment in ISPs. It runs on commodity x86 hardware and uses frameworks such as XDP/AF_XDP and DPDK. In addition to the direct inference (active) mode, we support a passive mode that does not affect traffic and only collects signals (e.g., per-packet load balancing). We also describe how these two modes, in combination, enable operators to build trustworthy ingress maps, reduce false routing alerts, and uncover data-plane path anomalies that are invisible to control-plane monitoring alone. Finally, we present a demo of OpenPenny running on a real testbed in UCL.

### Redefining Netflix BGP architecture
Speakers: Elise VENNEGUES Frederic Cuiller
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/74/RKCTUA/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/RKCTUA/resources/Redefining_Netflix_B_2YNNG4M.pdf | video: https://ripe92.ripe.net/media/videos/elise-vennegues_redefining-netflix-bgp-architecture_main_20260519-115725.mp4
Scaling a global streaming platform like Netflix requires a robust, agile, and future-ready network infrastructure. In close collaboration, Netflix and Cisco embarked on a journey to evolve Netflix's BGP architecture, leveraging Cisco's advanced IOS XRv9000 UCS M7 appliance — a solution developed and refined to meet Netflix's unique requirements. This joint presentation will introduce the Netflix network, discuss the motivations for architectural evolution, and detail how both teams worked together to design, validate, and deploy a cutting-edge route reflector solution. Attendees will gain a behind-the-scenes look at the technical challenges, the collaborative innovation process, and the operational benefits realized by both organizations. We'll share the validation, best practices and migration strategies that ensured a seamless transition, as well as the lessons learned that can inform similar projects. Whether you're a network operator, architect, or technology partner, join us to discover how strategic collaboration can drive both technical excellence and business value.

## Routing - Main Room (Wed, 11:00)

### Intro/Opener
Speakers: Sebastian Becker Ignas Bagdonas Ben Cartwright-Cox , bgp.tools / routing-wg
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/87/VNMFNM/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/VNMFNM/resources/Routing_WG_-_RIPE92_YHosuNS.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/VNMFNM/resources/Routing_WG_-_RIPE92_rFNY0nG.key | video: https://ripe92.ripe.net/media/videos/sebastian-becker_introopener_main_20260520-110045.mp4
Welcome to the Routing Working Group session!

### Non-functional Delegated RPKI CAs
Speakers: Tim Bruijnzeels , RIPE NCC Bart Bakker , RIPENCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/87/XPYQWF/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/XPYQWF/resources/RIPE-92___Non-Functi_xYeqnM9.pdf | video: https://ripe92.ripe.net/media/videos/tim-bruijnzeels_non-functional-delegated-rpki-cas_main_20260520-110312.mp4
Policy 2025-02 requires that the RIPE NCC revokes persistently non-functional delegated RPKI CAs. This seemingly simple request gets quite interesting when one zooms in on the details: how do we actually determine that a CA is non-functional? And how can we help operators of delegated CAs to identity and fix their issues? In this talk we will explain: * the various moving parts of delegated CAs, publication servers, and RPKI validation interconnect * how we monitor delegated CAs, and * what troubleshooting tools we can provide delegated CAs operators with

### Six Months of ASPA
Speakers: Tim Bruijnzeels , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/87/KBUQLT/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/KBUQLT/resources/RIPE92_-_Six_Months__rq1HNsx.pdf | video: https://ripe92.ripe.net/media/videos/tim-bruijnzeels_six-months-of-aspa_main_20260520-122846.mp4
ASPA was enabled on the RIPE NCC RPKI Dashboard on 26 November 2025. Since then we have seen the creation of over 1000 ASPA objects in the RIPE region alone. In this presentation we will talk about the uptake and lessons learned so far. We will zoom in on the curious case of AS0 ASPA objects. And we will talk about 'effective' ASPA signing and validation..

### Weird things in the RPKI
Speakers: Job Snijders
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/87/CVV98B/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CVV98B/resources/RIPE92_Weird_things__6H7jVIP.pdf | video: https://ripe92.ripe.net/media/videos/job-snijders_weird-things-in-the-rpki_main_20260520-115841.mp4
Weird things happen from time to time in the RPKI! Today I cover a bizarre ROA propagation issue which was the result from an unfortunate alignment of various factors.

### Closing notes
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/87/JYMF9P/ | video: https://ripe92.ripe.net/media/videos/na_closing-notes_main_20260520-122746.mp4
AOB

## Cooperation - Side Room (Wed, 11:00)

### Survival Tools for Internet Resilience (or) Where Does the Policy Step In
Speakers: Eliza Rohotska , Attorneys Association “Axon”
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/88/8CJ398/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/8CJ398/resources/fin_Coop_WG_Rohotska_XJfVgI3.pdf | video: https://ripe92.ripe.net/media/videos/eliza-rohotska_survival-tools-for-internet-resilience-or-where-does-the-policy-step-in_side_20260520-110503.mp4
Ukraine has become a global benchmark for Internet resilience, but the factors that enabled this survival are now facing some unexpected challenges. This presentation explores the tension between the technical necessity of decentralization and the growing drive for regulatory and fiscal centralization. We will examine the operational realities of maintaining a fragmented market under extreme pressure and ask a critical question whether the very ecosystem that kept a nation online can survive the transition to standardized peace-time regulations

### Shared Points of Failure How Widespread Vulnerabilities and Overlap Between Organisations Impacts Cyber Resilience
Speakers: Martin Price , Lancaster University Edward Austin , Lancaster University
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/88/T8ZNGJ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/T8ZNGJ/resources/RIPE_EASM_gIghtPZ_JoqUNyH.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/T8ZNGJ/resources/RIPE_EASM_gIghtPZ_Ph6PvXw.pptx | video: https://ripe92.ripe.net/media/videos/martin-price_shared-points-of-failure-how-widespread-vulnerabilities-and-overlap-between-orga_side_20260520-112817.mp4
Traditionally, Attack Surface Mapping (ASM) is performed by an organisation seeking to identify its own cyber vulnerabilities, and protect against them. Driven by society’s growing dependence on digital systems, there has been an interest at the government level in the vulnerabilities that affect organisations across a sector, or nationally. External Attack Surface Mapping (EASM) provides a way for government agencies to gather information about the vulnerabilities of organisations at this scale, and this talk covers our ongoing work in partnership with them to identify and visualise widespread vulnerabilities and shared risks. Our research is also investigating how EASM can go beyond the standard lens of vulnerability assessment and can be used to find weaknesses across cyber supply chains, or identify common dependencies between multiple organisations that an adversary could exploit. Detecting and mitigating these weaknesses is therefore crucial for ensuring resilience of the UK’s digital infrastructure, and this talk will present an example highlighting how EASM can be used for this application.

### What's in the Digital Networks Act and what should you do about it?
Speakers: Mike Blanche
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/88/UPKB9J/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/UPKB9J/resources/RIPE_92_-_DNA_-_mbla_uqazIi2.pdf | video: https://ripe92.ripe.net/media/videos/mike-blanche_whats-in-the-digital-networks-act-and-what-should-you-do-about-it_side_20260520-114943.mp4
The European Commission's draft text of the Digital Networks Act was released in January 2026, and contains substantial proposed changes to the regulatory landscape for operators of all types of networks across the EU. This talk explains the changes proposed for: - Scope: who is to be regulated - Replacing the Open Internet Regulation - New regulator involvement in "ecosystem cooperation" and "voluntary conciliation" across a broad range of technology companies, not just networks - Changes to IP interconnection regulation The presentation concludes with how you can get involved and feedback to policymakers on these proposals.

### RIPE NCC Engagements in Public Policy and Internet Governance
Speakers: Hisham Ibrahim , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/88/A7BPZT/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/A7BPZT/resources/RIPE_NCC_Engagements_RTLGgtK.pdf | video: https://ripe92.ripe.net/media/videos/hisham-ibrahim_ripe-ncc-engagements-in-public-policy-and-internet-governance_side_20260520-121755.mp4
From public consultations and intergovernmental processes to regional engagement, partnerships and law enforcement dialogue

## Address Policy - Main Room (Thu, 11:00)

### Co-chair selection
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/97/BJN9WV/ | video: https://ripe92.ripe.net/media/videos/na_co-chair-selection_main_20260521-110504.mp4
Selection of the co-chair

### ASO AC Update
Speakers: Andrei Robachevsky , Global Cyber Alliance Herve Clement , ASO AC Constanze Buerger
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/97/VBJADC/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/VBJADC/resources/2026_05_21_RIPE-92-_yG6Pdcq.pptx | video: https://ripe92.ripe.net/media/videos/andrei-robachevsky_aso-ac-update_main_20260521-110628.mp4
This presentation is about the report the Number Resource Organization Number Council (NRO NC) serving as the Address Supporting Organization Address Council (ASO AC) performs regularly on its yearly activities.

### Policy Update
Speakers: Angela Dall'Ara , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/97/CHDGUX/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CHDGUX/resources/RIPE_92_Policy_Updat_ZmfVksX.pdf | video: https://ripe92.ripe.net/media/videos/angela-dallara_policy-update_main_20260521-112121.mp4
Update on policy development since RIPE 91

### Registration Services Update
Speakers: Marco Schmidt , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/97/JZ3KEL/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/JZ3KEL/resources/RIPE_92_Update_from__23Km8Xv.pdf | video: https://ripe92.ripe.net/media/videos/marco-schmidt_registration-services-update_main_20260521-113720.mp4
To provide a regular update on observations and trends identified by Registration Services. Topics will include legacy resources without contracts and data on address space that some parties describe as leased.

### IP Address space for Outer Space
Speakers: Tony Li
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/97/RHW7DB/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/RHW7DB/resources/RIPE_address_space.k_740WWva.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/RHW7DB/resources/RIPE_address_space_FWRbbyo.key | video: https://ripe92.ripe.net/media/videos/tony-li_ip-address-space-for-outer-space_main_20260521-120023.mp4
The exploration of outer space depends heavily upon communications technology and in many cases, uses IP. IP address allocation has been formally assigned to Regional Internet Registries (RIRs), but there is no formal allocation of address space for networks in outer space.

## DNS - Side Room (Thu, 11:00)

### Welcome and announcement of the new co-chair
Speakers: Moritz Müller
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/MQCJJ8/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/MQCJJ8/resources/ripe92-dnswg-agenda_BkFGNxO.pdf | video: https://ripe92.ripe.net/media/videos/moritz-muller_welcome-and-announcement-of-the-new-co-chair_side_20260521-105952.mp4
Welcome and announcement of the new co-chair

### DNS, Transitive Trust and How Many is Many
Speakers: Ondřej Surý , ISC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/ATVK7Z/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ATVK7Z/resources/DNS_Transitive_Trus_2ntoCpt.pdf | video: https://ripe92.ripe.net/media/videos/ondrej-sury_dns-transitive-trust-and-how-many-is-many_side_20260521-110213.mp4
How many DNS queries does it take to resolve a single domain name? The answer might really surprise you and perhaps even alarm you. Depending on a specifici delegation, CNAME chains that CDNs love so much, and cross-domain dependencies, a single cold-cache lookup can trigger hundreds of outgoing queries from a recursive resolver, creating latency for end users and amplifying load on both the resolver and the authoritative DNS servers. This talk will deep dive into different DNS delegation types - in-domain, in-bailiwick, out-of-bailiwick - and explain how each type of the delegations affects the resolver query chain when the cache is cold. I will show how combining delegations across different TLDs and different domain increase the strain on the DNS ecosystem, and how combining this with CNAME chains leads to explosion of transitive trust dependencies that resolvers must chase before returning a single answer.

### Black Holes and Prisoners: Understanding AS112 Deployment Characteristics
Speakers: Elizabeth Boswell , University of Glasgow
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/RATHUR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/RATHUR/resources/black-holes-prisoner_V7ki2VH.pdf | video: https://ripe92.ripe.net/media/videos/elizabeth-boswell_black-holes-and-prisoners-understanding-as112-deployment-characteristics_side_20260521-112544.mp4
AS112 is an anycast DNS deployment that responds to junk queries, i.e. leaked queries from internal networks, which should have been handled locally. This includes reverse DNS queries for RFC1918 and link local addresses, and queries for home.arpa and service.arpa. Unlike other anycast deployments, AS112 is volunteer-run and uncoordinated. Anyone can contribute to AS112 by setting up a DNS server, announcing the AS112 anycast prefixes, and responding to queries. AS112 helps protect important parts of the Internet infrastructure, but there has been no comprehensive study of who runs the AS112 servers, where they are located, and whether they effectively capture leaked queries. Using RIPE Atlas and 33646 open recursive resolvers, we detect 469 AS112 sites, run by 97 operators, and compare the response time and query distances of AS112 to root server queries. AS112 performs well, with 23.21% lower median response times and 36.11% lower median distances than the root. However, AS112 is largely dependent on few large operators (one operator serves 41.71% of probes in our study), limiting its resilience.

### DNS TAPIR POP – Managing Multiple RPZ Inputs
Speakers: Lars-Johan Liman , Netnod
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/ZV8NA8/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ZV8NA8/resources/dns-tapir-RIPE92-202_jKMuHMT.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ZV8NA8/resources/dns-tapir-RIPE92-20_hgL2Svw.pptx | video: https://ripe92.ripe.net/media/videos/lars-johan-liman_dns-tapir-pop-managing-multiple-rpz-inputs_side_20260521-114030.mp4
Administrators of DNS resolvers with large internet service providers often have multiple inputs for managing the response policy, ranging from legal filters to commercial recommendations from various sources. The open source DNS TAPIR Policy Processor (POP) is a new tool for managing this – both with static inputs and with dynamic rulesets which can be updated over an MQTT message bus. These features are used in the DNS TAPIR platform, but POP can be used as a stand-alone service to simplify administration of the input data streams that influence response policy setup. POP is a service that feeds the resolver with policy settings, typically by providing an RPZ zone that can be imported as such in the resolver configuration. It can handle multiple input sources via different means (static files in different formats, RPZ streams, MQTT). A very simplistic policy language describes the logic for selecting what's being sent as instructions to the resolver in the form of an outgoing RPZ. The code is open source, and available on Github. The policy language could benefit from more discussion by more people.

### Overdoing NSEC3 Hurts
Speakers: Petr Špaček , Internet Systems Consortium
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/HW3LJG/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/HW3LJG/resources/presentation_dzewVOT.pdf | video: https://ripe92.ripe.net/media/videos/petr-spacek_overdoing-nsec3-hurts_side_20260521-120328.mp4
An NSEC3 configuration with too many iterations leads to excessive work on authoritative servers and resolvers, can be used for DoS attacks, and even opens a downgrade attack path which is not well documented. In this brief talk we want to alert operators to this danger and evangelize Best Current Practice RFC 9276 which shows how to use NSEC3 in a safe (or less harmful) way.

### RIPE NCC DNS Update
Speakers: Florian Obser , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/WVWVFD/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/WVWVFD/resources/ripe92_-_RIPE_NCC_DN_gZ9K5F8.pdf | video: https://ripe92.ripe.net/media/videos/florian-obser_ripe-ncc-dns-update_side_20260521-121456.mp4
A short presentation about RIPE NCC's DNS activities.

### Measuring Resilience of Recursive Resolvers
Speakers: Maynard Koch , TU Dresden
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/98/8TCKVY/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/8TCKVY/resources/RIPE92-DNS-Resilienc_82gEwNw.pdf | video: https://ripe92.ripe.net/media/videos/maynard-koch_measuring-resilience-of-recursive-resolvers_side_20260521-122416.mp4
A resilient Internet requires a resilient Domain Name System (DNS). A resilient DNS ensures the continuous availability of many services and should withstand outages (e.g., power outages or cable cuts), attacks (e.g., DDoS), and technical disruptions while still maintaining integrity and confidentiality. In this talk, we introduce the ISOC project to measure DNS resilience. The Internet standards community (IETF) has published several operational best practices to improve DNS resilience, but operators must make their own decisions that tradeoff security, cost, and complexity. Since these decisions can impact the security of billions of Internet users, recently ICANN has proposed an initiative to codify best practices into a set of global norms to improve security: the Knowledge-Sharing and Instantiating Norms for DNS and Naming Security (KINDNS). The goal of this project is to conduct an independent study on the measurable practices of the KINDNS framework, as well as other important DNS resilience practices. We aim to develop a DNS resilience observatory that collects information from public sources together with Internet-wide measurements to provide a longitudinal view of the evolution and adoption of DNS best practices globally. In the early stages of this project, we would like to ask for feedback and contributions from the community.

## Closing Plenary - Main Room (Fri, 11:00)

### Measuring The Impact of Post-Quantum Cryptography on Complex Applications: A Case Study on Federated Identity Management
Speakers: Ginevra Fabrizio , University of Twente
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/112/3XVHEJ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/3XVHEJ/resources/RIPE_92_-_FIdM_PQC-2_q0fHRKb.pdf | video: https://ripe92.ripe.net/media/videos/ginevra-fabrizio_measuring-the-impact-of-post-quantum-cryptography-on-complex-applications-a-cas_main_20260522-110043.mp4
The arrival of quantum computers will significantly impact our current Internet infrastructures as quantum computers will be able to break current public key cryptography. This means that we need to replace cryptographic algorithms by quantum-safe alternatives, also known as Post Quantum Cryptography (PQC). Many protocols and architectures need to make this transition. While the Internet community is making steady progress on transitioning TLS to PQC, there are still many protocols for which action needs to be taken, especially in more complex scenarios where protocols span multiple layers of the stack. In this paper, we study such a complex scenario: Federated Identity architectures. The objective of these architectures is to allow access to multiple services using a single set of login credentials, improving convenience and security across different organizations or domains. In particular we examine the Hub’n’Spoke model, where multiple parties exchange data through a central hub. This hub manages most of the infrastructure workload and deals with many heterogeneous devices and protocols, making it a perfect test case for the PQC transition. Using real-world data from an operator of a large academic identity federation, we benchmark five PQC algorithms finalized by NIST. We also quantify the toll this transition imposes on computational efficiency and hardware capacity. We show that while there is an ever increasing interest towards PQC adoption, many technical challenges remain unaddressed, showing that the Post Quantum transition process is fragmented, with many components of the ecosystem that are still insufficiently taken into consideration.

### Hilby - Hilbert Interactive Prefix Plots
Speakers: Alexander Männel , TU Dresden
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/112/ZUFGSN/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ZUFGSN/resources/ripe_raci_hilby_shor_Sq7dK3f.pdf | video: https://ripe92.ripe.net/media/videos/alexander-mannel_hilby-hilbert-interactive-prefix-plots_main_20260522-112827.mp4
Effective visualization of the IP address space is important for navigating the scale and complexity of modern network data. Hilbert curves are a common method to map one-dimensional address spaces into 2D images. In this talk, we present Hilby, an open-source React framework for rendering interactive Hilbert maps for both IPv4 and IPv6. Unlike statically rendered images Hilby supports dynamic aggregation and deaggregation of prefixes, allowing users to seamlessly transition between macroscopic overviews and microscopic details in real-time. By combining this with other features like coloring and text, Hilby can display both fine details and coarse overviews of large amounts of networking data in the same frame without sacrificing performance or user experience. Hilby focuses on developer experience in allowing the simple integration of a Hilbert curve by abstracting the complexities of the mapping behind a simple API. We showcase Hilby through real-world use cases in research and operational settings and release a playground environment for experimenting with user-provided data.

### BitSquatting... ...or the infinite monkeys theorem...
Speakers: Warren Kumari , Google LLC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/112/MFPHZ7/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/MFPHZ7/resources/bitsquatting-2026-ri_HV5VAoi.pdf | video: https://ripe92.ripe.net/media/videos/warren-kumari_bitsquatting-or-the-infinite-monkeys-theorem_main_20260522-113721.mp4
This is an update on "bitsquatting", a form of cybersquatting that exploits hardware bit-flip errors—often caused by cosmic rays or faulty components—during DNS requests. It explores how these random memory corruptions can inadvertently redirect legitimate network traffic to attacker-controlled domains that differ by only a single binary bit from the intended address. The briefing emphasizes the operational risks this vulnerability poses to security of the web, and the somewhat scary information leakage that occurs.

### RIPE Code of Conduct Team Report
Speakers: Andrew McConachie
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/112/AUKFZB/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/AUKFZB/resources/RIPE92_CoC_Transpare_47dYGsV.pdf | video: https://ripe92.ripe.net/media/videos/andrew-mcconachie_ripe-code-of-conduct-team-report_main_20260522-114908.mp4
Report from the RIPE Code of Conduct team at RIPE 92

### RIPE 92 Tech Report
Speakers: Rob de Meester , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/112/YPEYH7/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/YPEYH7/resources/RIPE_92_Tech_Report_ZlaYarV.pdf | video: https://ripe92.ripe.net/media/videos/rob-de-meester_ripe-92-tech-report_main_20260522-115819.mp4
Report from the RIPE Meeting Tech Team

### Closing
Speakers: Mirjam Kühne , RIPE Community
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/112/JQKURD/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/JQKURD/resources/RIPE_92_Closing_Plen_2zIrmBn.pdf | video: https://ripe92.ripe.net/media/videos/mirjam-kuhne_closing_main_20260522-121147.mp4
Closing presentation from the RIPE Chair Team

## Newcomer's Introduction - Main Room (Mon, 11:30)

### Newcomers introduction
Speakers: Mirjam Kühne , RIPE Community Anna Wilson Hans Petter Holen , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/62/FFCUX3/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/FFCUX3/resources/RIPE_92_Newcomers_-__i7UPWQe.pdf | video: https://ripe92.ripe.net/media/videos/mirjam-kuhne_newcomers-introduction_main_20260518-112828.mp4
Is this one of your first RIPE Meetings? Join the Newcomer's Introduction to get an introduction to the RIPE community and learn how things are organised at a RIPE Meeting. The RIPE Chair team will give you an overview of what you can expect at the meeting. RIPE NCC CEO and Managing Director, Hans Petter Holen, will introduce you to the RIPE NCC and its work.

## Opening Plenary - Main Room (Mon, 14:00)

### Welcome to RIPE 92
Speakers: Mirjam Kühne , RIPE Community
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/65/WZRYHA/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/WZRYHA/resources/Welcome_to_RIPE_92_WN4fu4d.pdf | video: https://ripe92.ripe.net/media/videos/mirjam-kuhne_welcome-to-ripe-92_main_20260518-135933.mp4
Welcome from the RIPE Chair

### Welcome to Edinburgh
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/65/7WAX3R/ | video: https://ripe92.ripe.net/media/videos/na_welcome-to-edinburgh_main_20260518-140952.mp4
Welcome by the Lord Provost of Edinburgh

### Welcome from the Local Host
Speakers: Linda Shannon
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/65/REZATJ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/REZATJ/resources/RIPE_92_Welcome_Deck_3XCRQGf.pdf | video: https://ripe92.ripe.net/media/videos/linda-shannon_welcome-from-the-local-host_main_20260518-141742.mp4
Welcome to Edinburgh

### Welcome from the RIPE NCC and Meeting Logistics
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/65/Q9DLXR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/Q9DLXR/resources/RIPE_92_Welcome_from_Lp785Xf.pdf | video: https://ripe92.ripe.net/media/videos/hans-petter-holen_welcome-from-the-ripe-ncc-and-meeting-logistics_main_20260518-142215.mp4
RIPE 92 Meeting Logistics

### Manipulating RPKI (and more) with marquees in TLS certificates (and more)
Speakers: Sasha Romijn , Reliably Coded (IRRD, IRRexplorer, internet.nl)
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/65/YHQY7N/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/YHQY7N/resources/Manipulating_RPKI___1zypS0J.pdf | video: https://ripe92.ripe.net/media/videos/sasha-romijn_manipulating-rpki-and-more-with-marquees-in-tls-certificates-and-more_main_20260518-143021.mp4
What if someone could disrupt your RPKI configuration or take over your RIPE Database objects? All because you clicked a single link to a RIPE NCC website? I've spent the past year putting marquee tags and XSS injection payloads into every protocol field I control: TLS certificate SANs, DNS NSID and version.bind responses, HTTP Server headers, RIPE Database objects, wifi SSIDs, and much more. Many tools that display these fields treat them as safe data. And some of these share a trust boundary with more critical systems. So far, my findings span two RIRs, several hosting providers, router firmware, DNS tooling, and more. The impacts range from funny, to taking over hosting customer accounts to rooting OpenWRT routers wirelessly. At the most serious end, I found multiple paths via the RIPE NCC single sign-on session. From a single click, on a real ripe.net link, I could modify your RPKI ROAs, and you would not even know it happened until your packets started to drop. And I'd have taken over your RIPE Database objects too. The common thread: some of our critical infrastructure turns out to be just a website with a login. RPKI has HSMs and key ceremonies, but the thing that actually changes your ROAs is a web app authenticated by a cookie. This talk covers patterns across all my findings, with a detailed walkthrough of the RPKI attack chain. And if you run any kind of tooling on your own network, I'll show you what to watch out for.

### Why is ASPA still a draft
Speakers: Maria Matejka , BIRD | CZ.NIC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/65/TDYAZY/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TDYAZY/resources/why-is-aspa-still-a-_7WvkFjh.pdf | video: https://ripe92.ripe.net/media/videos/maria-matejka_why-is-aspa-still-a-draft_main_20260518-150332.mp4
The ASPA technology for authorizing BGP AS Paths has been in the draft state for a long time and it's almost done. This talk reminds the audience about the ASPA technology and sheds some light on the implementation and deployment questions which have repeatedly impeded the way forward for this set of drafts.

## Plenary - Main Room (Tue, 14:00)

### It's coming: Time for IPv6 in the DNS
Speakers: Tobias Fiebig , TU Wien
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/76/UW7HFC/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/UW7HFC/resources/presentation_vqIpUmU.pdf | video: https://ripe92.ripe.net/media/videos/tobias-fiebig_its-coming-time-for-ipv6-in-the-dns_main_20260519-140127.mp4
Since RFC3901 from 2004, it is clear that in the DNS IPv4 is a MUST. IPv6, however is a MAY IF YOU FEEL LIKE IT YOU KNOW IF IT VIBES. Since 2023, work was ongoing in the IETF DNSOP working group to change that with a 3901bis document. This document has passed the IESG in February, and is now in the RFC editors queue, bound to be the new Best Current Practice for "doing DNS". This time with IPv6. In this talk, we will go over what this document now recommends, what operators should do to follow this new recommendation, and also look at some corner case culprits nobody expected to make DNS worse: IPv4 (with a cameo from CGN). Be ready. IPv6 ready.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings
Speakers: Gerhard Stein , Flexoptix GmbH
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/76/EAF87P/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/EAF87P/resources/Flexoptix_-_RIPE92_3WzSdf9.pdf | video: https://ripe92.ripe.net/media/videos/gerhard-stein_understanding-and-optimising-transceiver-efficiency-using-internal-metrics-for-i_main_20260519-143142.mp4
In high-performance optical communication systems transceiver health and efficiency are critical to network reliability and energy consumption. This presentation explores the powerful capabilities of Versatile Diagnostics Monitoring (VDM) features found in modern optical transceivers (beyond the speed of 100G) with a particular focus on the Thermoelectric Cooler (TEC) current metrics. By analysing TEC current alongside temperature and cable length data we should be able to identify the optimal operating conditions that will minimise power consumption while maintaining performance. In order to prove this thesis we developed a couple of software prototypes to perform the data analysis. Using real-world VDM data this talk will demonstrate how to evaluate and visualise transceiver efficiency in terms of Watts, uncovering practical insights for engineers aiming to design or operate greener, more efficient optical networks and finally save energy.

### A study on the Global Scale and Nature of Technology-facilitated Child Sexual Exploitation and Abuse
Speakers: James Stevenson , Childlight- Global Child Safety Institute, University of Edinburgh
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/76/8WYEAL/ | video: https://ripe92.ripe.net/media/videos/james-stevenson_a-study-on-the-global-scale-and-nature-of-technology-facilitated-child-sexual-ex_main_20260519-145618.mp4
Childlight, based at the University of Edinburgh, is a research centre dedicated to uncovering the scale, prevalence, and nature of global child sexual exploitation and abuse (CSEA). Its inaugural Global Index focuses specifically on technology facilitated CSEA, recognising the central role that digital systems, platforms, and connectivity infrastructures play in enabling or interrupting harm. This May, Childlight will publish updated global data on technology facilitated CSEA. The report highlights how technology companies and online service providers can reduce risk, strengthen user trust, and contribute to safer online environments. Using large scale datasets as proxy indicators of different forms of harm, the report examines global patterns in CSEA content availability and distribution, and considers what these patterns suggest about the types of responses required. Although platform level interventions play a critical role, the findings indicate that broader coordinated action across sectors and jurisdictions is also required. The presentation will outline how data on CSEA file sharing and availability can serve as evidence to guide policy, technical safeguards, and operational decision making. It will also describe the development of the global technology-facilitated child sexual exploitation and abuse (TF-CSEA) data landscape, including how iterative feedback and methodological refinement have strengthened the resulting recommendations. These recommendations are intended as a starting point for discussion. Some proposals are immediately actionable, while others will require further evidence, technical exploration, or collaborative refinement. At Childlight we have worked with technology partners to help utilise their data to highlight safeguarding efforts as well as need for further investment into response. This presentation is hoped to encourage potential future partnerships with other attendees by showing our academic rigour and understanding of this complex issue.

### Brace for Upgrades - Plural
Speakers: Petr Špaček , Internet Systems Consortium
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/76/T7NMB8/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/T7NMB8/resources/presentation_qJAmu19.pdf | video: https://ripe92.ripe.net/media/videos/petr-spacek_brace-for-upgrades-plural_main_20260519-151338.mp4
Security researchers equipped with LLMs are finding security issues in various software components at an unprecedented pace, and open-source projects are scrambling to fix them all. The old “enterprise” model of carefully deciding whether to upgrade or delay each software release is becoming problematic.

### ECH is supported in OpenSSL v4.0.0
Speakers: Stephen Farrell
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/76/NAUBEY/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/NAUBEY/resources/ech-is-ripe_WDBaZJS.pdf | video: https://ripe92.ripe.net/media/videos/stephen-farrell_ech-is-supported-in-openssl-v400_main_20260519-153007.mp4
Encrypted Client Hello (ECH, RFC9849, March 2026) is now supported in OpenSSL v4.0.0. Proposed presentation briefly explains ECH; motivates its use; identifies support in a number of libraries, as also in client and server codes; and lists resources to support deployment.

## RIPE NCC Services - Main Room (Wed, 14:00)

### RIPE NCC Strategy 2027-2031
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/90/ZCSWAA/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/ZCSWAA/resources/RIPE_NCC_Strategy_20_TCR3ICi.pdf | video: https://ripe92.ripe.net/media/videos/hans-petter-holen_ripe-ncc-strategy-2027-2031_main_20260520-140412.mp4
A high-level overview of the RIPE NCC’s strategic focus areas for the period 2027-31. This strategy will inform the delivery of RIPE NCC services, starting with the Activity Plan and Budget for 2027.

### Rebuilding Our Technical Infrastructure
Speakers: Hans Petter Holen , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/90/S9GKWB/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/S9GKWB/resources/RIPE_92_-_IT_Infrast_ivv7sqd.pdf | video: https://ripe92.ripe.net/media/videos/hans-petter-holen_rebuilding-our-technical-infrastructure_main_20260520-142220.mp4
An overview and assessment of the current technical infrastructure at the RIPE NCC and looking at the plans ahead.

### Operational Review of Public ENUM under e164.arpa
Speakers: Hisham Ibrahim , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/90/YBYU78/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/YBYU78/resources/Operational_Review_o_oR6Na7M.pdf | video: https://ripe92.ripe.net/media/videos/hisham-ibrahim_operational-review-of-public-enum-under-e164arpa_main_20260520-150456.mp4
A review of ENUM, the stakeholders involved and the current discussion about its operation.

### Multiple LIRs, PI and Legacy
Speakers: Gabor de Wit , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/90/WSJJRR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/WSJJRR/resources/Multiple_LIRs_PI_an_JZUkzLp.pdf | video: https://ripe92.ripe.net/media/videos/gabor-de-wit_multiple-lirs-pi-and-legacy_main_20260520-152152.mp4
This presentation looks at the history of Multiple LIRs, PI, and Legacy resources and explores today’s operational realities and emerging challenges.

## Address Policy - Main Room (Thu, 14:00)

### Discussion on AS Reallocation
Speakers: Antonis Chariton , AS4601 | Cisco
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/100/S3BFX8/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/S3BFX8/resources/RIPE92-APWG-RPKI_fnqzmaw.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/S3BFX8/resources/RIPE92-APWG-RPKI_WJmAJng.key | video: https://ripe92.ripe.net/media/videos/antonis-chariton_discussion-on-as-reallocation_main_20260521-140013.mp4
Currently when RIPE NCC re-assigns an AS to another entity after the 6 month waiting period, there's an IRR cleanup process but not an RPKI one, which leads to many newly assigned ASNs coming with pre-existing ROAs[1]. In this session we'll go over some of the results and data found by studying past assignments, the impact to business operations, and then spend most of the slot discussing potential solutions or future actions that may be needed. 1: Plenary, "RPKI: Do we need Garbage Collection now?"

### RIPE Policy Proposal 2024-01: Revised IPv6 PI Assignment Policy
Speakers: Tobias Fiebig , TU Wien
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/100/JBGK7J/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/JBGK7J/resources/presentation_eW5Gbno.pdf | video: https://ripe92.ripe.net/media/videos/tobias-fiebig_ripe-policy-proposal-2024-01-revised-ipv6-pi-assignment-policy_main_20260521-142726.mp4
This presentation will discuss the current state of 2024-01, revisit the changes and history, and outline the authors' perspective on how the document should proceed following the PDP.

### Upcoming AP Policy Proposal: Loss of legacy status upon transfer
Speakers: Clara Wade , AWS Peter Hessler
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/100/DJQKBJ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/DJQKBJ/resources/Upcoming_Policy_Prop_gVdrFHs.pdf | video: https://ripe92.ripe.net/media/videos/clara-wade_upcoming-ap-policy-proposal-loss-of-legacy-status-upon-transfer_main_20260521-144556.mp4
We are seeking early community feedback on an upcoming policy proposal to remove the option of retaining legacy status after a transfer, to address the increasing overhead for the RIPE NCC, the increasing market speculation around a scarce resource and the impact on the adoption of best practices like RPKI. This talk will briefly present on the issues we are trying to address, report the data we've found to support this and allot time to engage the community in a discussion on some concerns that have been expressed on the mailing list so far, as well as provide a space to surface any other questions or comments.

## IoT - Side Room (Thu, 14:00)

### Introduction & Housekeeping
Speakers: Peter Steinhaeuser
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/101/HPECWQ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/HPECWQ/resources/RIPE-92-IoT-Slides_O_ZP1wiSB.pdf | video: https://ripe92.ripe.net/media/videos/peter-steinhaeuser_introduction-housekeeping_side_20260521-140039.mp4
Welcome and introduction for the IoT Working Group Session.

### IoT DNS Security and Privacy Guidelines Update
Speakers: Jim Mozley , Infoblox, University College London and Inria
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/101/CKFRQY/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CKFRQY/resources/RIPE92_IoT_DNS_Secur_lKacBky.pdf | video: https://ripe92.ripe.net/media/videos/jim-mozley_iot-dns-security-and-privacy-guidelines-update_side_20260521-140356.mp4
This talk will provide an update on the Internet Draft "IoT DNS Security and Privacy Guidelines" and seek to get working group input on the draft’s topics. The draft is based on research into the DNS behaviour of IoT devices that aims to mitigate the security risks identified by the research. The draft is intended as a best current practice that can be used by manufacturers and referenced by standards organisations. It can also be useful content for network operators who might be involved in some of the mitigations due to the nature of DNS resolution and who have an interest in network security in this area.

### Designing IoT Honeypots: Lessons from Seven Years of Architectural Challenges
Speakers: Robert Thomas , Global Cyber Alliance
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/101/JTERJS/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/JTERJS/resources/ProxyPot_RIPE_92_qqXBfyj.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/JTERJS/resources/ProxyPot_RIPE_92_Wnr9eAR.pptx | video: https://ripe92.ripe.net/media/videos/robert-thomas_designing-iot-honeypots-lessons-from-seven-years-of-architectural-challenges_side_20260521-141858.mp4
Our presentation examines the architectural challenges encountered over seven years of building ProxyPot, a honeypot designed for modern Internet of Things (IoT) environments. Unlike traditional systems focused on HTTP traffic, IoT devices expose a diverse attack surface across protocols such as Telnet, SSH, FTP, SMTP, and DNS, requiring fundamentally different design approaches. We highlight the challenges of supporting multiple protocols within a unified architecture, including maintaining consistency, scalability, and realistic service emulation, while accommodating protocol-specific attacker behaviour. These challenges shape how effective IoT honeypots are designed and directly impact their ability to capture meaningful threat activity and support robust detection and defence strategies.

### Traffic-Level In-Depth Profiling of Smart Home Events, Devices, and Cross-Device Interactions
Speakers: François De Keersmaeker , UCLouvain
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/101/WH7RWA/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/WH7RWA/resources/slides_no-animation_xmrt4rW.pdf | video: https://ripe92.ripe.net/media/videos/francois-de-keersmaeker_traffic-level-in-depth-profiling-of-smart-home-events-devices-and-cross-device_side_20260521-144327.mp4
The widespread use of Smart Home devices has attracted significant research interest in understanding their behavior within home networks, notably to enhance their security. Unlike general-purpose computers, these devices exhibit relatively simple and bounded network activity patterns. The IETF's MUD standard was a leap towards their profiling, providing a format to express those patterns. However, it lacks expressiveness in modeling communications taking place in an actual Smart Home network, mainly due to its inability to express dependencies between subsequent traffic patterns, something usual in Smart Homes as part of home automation routines. We propose a new format, inspired by MUD, overcoming this limitation. Afterwards, we tackle the problem of the automated generation of MUD-like traffic profiles. While various works have studied this, they have always considered normal network conditions, overlooking potential hidden patterns that emerge under non-standard conditions. Discovering the latter is crucial to provide an exhaustive profile of the device's traffic. We propose a mostly automated framework able to extract such patterns in a more exhaustive way than existing works, steadily uncovering more traffic flows, mostly hidden ones. Additionally, we leverage the latter as a measure of the devices' robustness, and provide guidelines towards enhancing it. We envision such guidelines could be used in the future to label devices put on the market, in order to provide the customer with a more enlightened choice.

### State of Device Identities
Speakers: Michael Richardson , Sandelman Software Works Inc
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/101/KPKG3D/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/KPKG3D/resources/DeviceID-Update_fm9kNOQ.pdf | video: https://ripe92.ripe.net/media/videos/michael-richardson_state-of-device-identities_side_20260521-151331.mp4
At RIPE90, the launch of IoTSF's Device ID Forum was announced. Since then there have been some work and some progress, and this talk is an update on where things stand a year later.

### Co-Chair Selection & Closing
Speakers: Peter Steinhaeuser
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/101/FZGTCB/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/FZGTCB/resources/RIPE-92-IoT-Slides_C_DKkzuz1.pdf | video: https://ripe92.ripe.net/media/videos/peter-steinhaeuser_co-chair-selection-closing_side_20260521-152719.mp4
Closing & Selection of the new WG Co-Chair

## Plenary - Main Room (Mon, 16:00)

### Noisy Routers: Investigating the Make-up route collector data
Speakers: Ebrima Jaw , University of Twente
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/67/FUMCAA/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/FUMCAA/resources/noisy.routers.RIPE92_ynkaGfY.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/FUMCAA/resources/noisy.routers.RIPE9_tr0GhWu.pptx | video: https://ripe92.ripe.net/media/videos/ebrima-jaw_noisy-routers-investigating-the-make-up-route-collector-data_main_20260518-160009.mp4
The Border Gateway Protocol (BGP) is a crucial inter-domain routing protocol that uses update messages to enable Autonomous Systems (ASes) to share network reachability information. Typically, ASes should only trigger update messages to reflect configuration changes and link failures for optimal path selection. However, we have identified recurring patterns of high-frequency repeated updates without any topological changes, which consume unnecessary resources of the route collectors for archiving and storage, and complicate downstream analysis. Although the phenomenon of noisy BGP peers and prefixes is known, current work has not quantified its scope and characteristics. This study fills this gap and analyzes over 80 billion update messages from multiple RouteViews collectors spanning several years. We identify and characterize high-frequency repeated updates driven by a small fraction of sessions and prefixes. For instance, fewer than 2\% of the prefixes accounted for over 90\% of update messages in some BGP update traces.

### Route Filtering at Scale
Speakers: Fedor Vompe , Deutsche Telekom Sebastian Becker
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/67/EDRJ39/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/EDRJ39/resources/RIPE_92_Route_Filter_Jl2GqKT.pdf | video: https://ripe92.ripe.net/media/videos/fedor-vompe_route-filtering-at-scale_main_20260518-163214.mp4
BGP routing security relies on many technologies, both old and new, such as IRR-based Route Filters and RPKI Technologies like Route Origin Authorizations (ROAs) or Autonomous System Provider Authorization (ASPA-s). While these technologies are well-known, they are still used together, and accurate route filter generation remains a challenging task with significant operational implications for large-scale router filter generation at major tier-1 ISPs. We show that AS-Set documentation in RIR databases is still critical yet systematically overlooked. We evaluate the scope and patterns of these issues - including missing documentation, AS-Set explosive expansion, and cyclic dependencies - demonstrating that accurate AS-Set documentation remains a foundational requirement for operational filtering. We present the toolchain and technologies like Route Query Specification (RQSpec) we use for route filter generation at scale, compensating for the complexity introduced by poor documentation.

### NetUK Introduction
Speakers: Matthew Jepp , NetUK
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/67/TKU9HD/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TKU9HD/resources/NetUK_RIPE92_P3w1IYQ_rugAtPc.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TKU9HD/resources/NetUK_RIPE92_P3w1IY_WKxnaz8.pptx | video: https://ripe92.ripe.net/media/videos/matthew-jepp_netuk-introduction_main_20260518-170405.mp4
An introduction to NetUK, the fresh non-profit community that aims to drive discussion and collaboration about the United Kingdom’s network infrastructure. The presentation covers the founding of NetUK, reasons to attend the event and information about the 2026 dates.

### Anycast in underserved regions
Speakers: Remi Hendriks , University of Twente
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/67/CHDADD/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CHDADD/resources/ripe92-anycast-under_LtWwwq0.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/CHDADD/resources/ripe92-anycast-unde_RzfuNGL.pptx | video: https://ripe92.ripe.net/media/videos/remi-hendriks_anycast-in-underserved-regions_main_20260518-171118.mp4
Anycast is a replication technique where a single IP address is made available at multiple geographic locations. Users connecting to such a replicated service are routed to the best replica using BGP. This replication allows for bringing services closer to users, and provides resilience by automatically redirecting users when one replica becomes unavailable. Due to these benefits, anycast is widely used for critical Internet infrastructure like the DNS (e.g., used by all root-letter operators). However, anycast deployments often lack coverage in formerly colonized nations in Africa and central America. As a result, the resilience of anycast is lessened for users in these regions. Problems such as colonial routing further complicate this issue as, for example, former French colonies may prefer a long route to a replica in Paris instead of nearby replicas in former British colonies. This talk will shed light on these problems and shares preliminary results of our measurements on anycast connectivity in such regions. Our goal is to reach operators that are willing to help us deploy in these regions to further measure this problem and assess the improvements possible when operators deploy in these regions.

### Update on Cascade Funding for Open Source
Speakers: Niall O'Reilly , (see title slide)
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/67/KCT8EK/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/KCT8EK/resources/Cascade-Funding_1T1Iq7S.pdf | video: https://ripe92.ripe.net/media/videos/niall-oreilly_update-on-cascade-funding-for-open-source_main_20260518-172257.mp4
Cascade Funding offers FOSS developers a means to access EU funding with reduced overhead and with more frequent proposal opportunities. The proposed talk updates material presented to the Open-Source WG at RIPE86 with a status update on NGI-0 (2018-2027) and its successors, NGO Fediversity (2024-2029) and OIS Restack (2026 onwards), all co-ordinated by the NLnet Foundation.

## MAT - Main Room (Tue, 16:00)

### Measuring DNS over IPv6
Speakers: Geoff Huston , APNIC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/78/AF9FFQ/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/AF9FFQ/resources/2026-05-14-v6-dns_EYFYQFT.pdf | video: https://ripe92.ripe.net/media/videos/geoff-huston_measuring-dns-over-ipv6_main_20260519-160707.mp4
This is a talk on the measurement techniques that can be used to undertake a large-scale measurement of the use of IPv6 as the IP underlay for DNS queries and responses. The presentation looks at the issues relating to measurement of DNS behaviours and the associated uncertainty of the measurement outcomes.

### Scanning the IPv6 Internet Using Subnet-Router Anycast Probing
Speakers: Maynard Koch , TU Dresden
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/78/UJPUPM/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/UJPUPM/resources/RIPE92-SRA-probing-f_zlDu1q4.pdf | video: https://ripe92.ripe.net/media/videos/maynard-koch_scanning-the-ipv6-internet-using-subnet-router-anycast-probing_main_20260519-162639.mp4
Identifying active IPv6 addresses is challenging. Various methods emerged to master the measurement challenge in this huge address space, including hitlists, new probing techniques, and AI-generated target lists. In this presentation, we apply active Subnet-Router anycast (SRA) probing, a commonly unused method to explore the IPv6 address space. We compare our results with lists of active IPv6 nodes obtained from prior methods and with random probing. Our findings indicate that probing an SRA address reveals on average 10% more router IP addresses than random probing and is far less affected by ICMP rate limiting. Compared to targeting router addresses directly, SRA probing discovers 80% more addresses. We conclude that SRA probing is an important addition to the IPv6 measurement toolbox and may improve the stability of results significantly. We also find evidence that some active scans can cause harmful conditions in current IPv6 deployments, which we started to fix in collaboration with network operators. All used tools are publicly available and we publish measurement results once a week under https://ipv6-sra.realmv6.org with detailed reports.

### Lots of free data! The RPKISPOOL format for data materialization as used in RPKIViews
Speakers: Job Snijders
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/78/J3DLVL/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/J3DLVL/resources/RIPE92_The_RPKISPOOL_Jf4bZdv.pdf | video: https://ripe92.ripe.net/media/videos/job-snijders_lots-of-free-data-the-rpkispool-format-data-materialization-as-used-in-rpkiview_main_20260519-164047.mp4
RPKIViews discovers and stores all the world's RPKI data. The guiding principle is to support future and unforeseen use cases by making the world's RPKI data easily accessible in original form. RPKI material is collected globally from multiple topologically and geographically diverse vantages points using both rsync and RRDP synchronization. In this talk we'll cover how researchers & analysts can make use of the new "RPKISPOOL" storage technique, as used in RPKIViews.

### Detecting and Characterizing DDoS Scrubbing from Global BGP Routing:​ Insights from Five Leading Scrubbers​
Speakers: Shyam Krishna Khadka , University of Twente
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/78/QKVKRR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/QKVKRR/resources/Detecting-scrubbing-_x1a5m3Q.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/QKVKRR/resources/Detecting-scrubbing_PF3bIfl.pptx | video: https://ripe92.ripe.net/media/videos/shyam-krishna-khadka_detecting-and-characterizing-ddos-scrubbing-from-global-bgp-routing-insights_main_20260519-170727.mp4
Many scrubbers use the Border Gateway Protocol (BGP) to route Distributed Denial of Service (DDoS) traffic to their infrastructure, allowing them to drop the DDoS traffic and forward legitimate traffic to the Autonomous Systems (ASes) the scrubber protects. Despite their importance, the prevalence and operational behaviors of BGP-based DDoS scrubbing services remain poorly understood, such as the extent to which protected ASes always have a scrubber on their path or activate a scrubber on-demand when an attack occurs. We bridge this gap by detecting scrubbing activations and deactivations in public BGP data, where they manifest themselves as a scrubber dynamically appearing as the first upstream of an origin AS or as an origin AS for a particular prefix. We use 30 days of BGP data from the RIS route collectors, focusing on the global top five scrubbing providers, such as Cloudflare and Akamai. We also characterize their behavior, including protection modes, on-demand mitigation strategies, and RPKI/IRR practices. We find that prefixes that always use a scrubber are dominant compared to those that activate a scrubber on-demand. We also observe that 48% of the prefixes that scrubbers temporarily originate during an attack are not covered by valid RPKI ROAs (12.5% Invalid and 35.5% Notfound), which highlights a potential operational gap in current scrubbing practices regarding routing security. These insights are conservative because we only consider public BGP data and AS path changes that are most likely to be scrubbing events (e.g., those observed by two or more route collector peers). We believe our work is useful for security researchers and policymakers, for instance, to better understand DDoS protection levels of ASes in a particular country or region.

### Exploring Iran's Internet Shutdowns Using Cloudflare Radar
Speakers: David Belson , Cloudflare David Belson
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/78/W398FN/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/W398FN/resources/Exploring_the_Iran_I_dS6bEAq.pdf | video: https://ripe92.ripe.net/media/videos/david-belson_exploring-irans-internet-shutdowns-using-cloudflare-radar_main_20260519-171654.mp4
Iranian citizens spent a large percentage of the first quarter of 2026 offline, or with severely limited connectivity, due to two extended nationwide Internet shutdowns. Traffic, DNS, BGP, and other data sets available through Cloudflare Radar can be used to better understand the impact of these events.

### Closing notes
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/78/93EHFH/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/93EHFH/resources/mat_ripe92_chair_clo_iI7rutv.pdf | video: https://ripe92.ripe.net/media/videos/na_closing-notes_main_20260519-173521.mp4
Closing notes from the WG Chairs

## Security - Side Room (Tue, 16:00)

### Security WG RIPE 92 Intro
Speakers: Brian Nisbet
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/E8PQP9/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/E8PQP9/resources/Security_WG_RIPE_92__BWezegx.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/E8PQP9/resources/Security_WG_Slides__CgDs9PC.pptx | video: https://ripe92.ripe.net/media/videos/brian-nisbet_security-wg-ripe-92-intro_side_20260519-160052.mp4
Welcome Scribe, Chat, Stenography MeetEcho, Mic & Chat Etiquette Code of Conduct Ratings Where Appropriate Approve Minutes from RIPE 91 New Meeting System - Pretalx Finalise agenda

### LEA report 2025 and eEvidence implementation
Speakers: Franca Bosompim , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/HLSCFD/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/HLSCFD/resources/RIPE_92_-_LEA_REPORT_jgCODTI.pdf | video: https://ripe92.ripe.net/media/videos/franca-bosompim_lea-report-2025-and-eevidence-implementation_side_20260519-160515.mp4
Presentation of the LEA report 2025 and the implementation of eEvidence regulation by the RIPE NCC

### Residential Proxies and Infecting Infrastructure Working Session
Speakers: Leslie Daigle
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/J7DTZA/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/J7DTZA/resources/Residential_Proxies__3NNJTl2.pdf | video: https://ripe92.ripe.net/media/videos/leslie-daigle_residential-proxies-and-infecting-infrastructure-working-session_side_20260519-162149.mp4
This 10-minute report will offer a summary of conclusions of the 4-h working session on residential proxies that the Global Cyber Alliance will host on May 18, as a parallel event of RIPE 92. The session will focus on the growing challenge of “infecting infrastructure”—compromised devices, abused services, and proxy endpoints embedded within legitimate networks that enable large-scale cyberattacks. Building on prior similar workshops on actionable data and collective defense, the discussion will examine how fragmented detection and response mechanisms allow infected infrastructure to persist as a systemic threat. Particular attention will be given to residential proxy abuse, whether driven by infected consumer devices or commercial proxy networks, as a rapidly expanding enabler of fraud, malware delivery, account takeover, exploitation, and security control evasion. Participants in the session will explore the operational realities of this threat landscape, including uneven visibility, uncertain attribution, limited incentives for remediation, and persistent coordination failures across stakeholders, trying to move beyond broad problem statements towards practical mitigation strategies. Key themes will include assessing current collective knowledge and blind spots surrounding residential proxy abuse, defining a realistic “good state” focused on faster detection, containment and harm reduction, and identifying which actors are best positioned to influence outcomes. The session will also examine the resources, partnerships, and policy mechanisms needed to close existing coordination gaps, with the final objective to highlight concrete, achievable actions for the next 6–12 months

### The Moving Parts of Copyright and Cybercrime
Speakers: Lee Kent
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/QQVGMV/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/QQVGMV/resources/The_Moving_Parts_of__XYdiZLk.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/QQVGMV/resources/The_Moving_Parts_of_5Ctnk8r.pptx | video: https://ripe92.ripe.net/media/videos/lee-kent_the-moving-parts-of-copyright-and-cybercrime_side_20260519-163602.mp4
How ASN’s identified facilitating copyright infringement are commonly associated with other criminal activity.

### The €30 attack box: inside the Android TV botnet ecosystem
Speakers: Jérôme Meyer , Nokia
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/7AETZG/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/7AETZG/resources/RIPE_92_-_Nokia_Deep_T2jCpjR.pdf | video: https://ripe92.ripe.net/media/videos/jerome-meyer_the-30-attack-box-inside-the-android-tv-botnet-ecosystem_side_20260519-164530.mp4
In October 2025, Nokia Deepfield observed a 33 Tbps DDoS attack against a gaming provider. Terabit-scale attacks are now daily. The botnets behind them no longer scan for exposed IoT devices; they recruit from residential proxy networks with over 100 million consumer endpoints. Your subscribers bought a €30 streaming box to cut the cord; what they got was a proxy node. Budget Android TV devices ship with proxy software pre-installed, and botnet operators exploit it. They route a request to 0.0.0.0 through the proxy SDK, which resolves to the device's own loopback, where an unauthenticated ADB shell is listening. No scanning, no CVE. The proxy SDK delivers the victim. Starting from Kimwolf (three million active bots, ENS-based C2), we traced shared code, cryptographic fingerprints, and co-located infrastructure across six botnet families. What looked like independent campaigns turned out to be DDoS-for-hire and residential proxy monetisation running on the same plumbing. CECbot weaponises HDMI-CEC to survive factory resets. Katana ships a C compiler and compiles its own rootkit on-device. The outbound attack traffic from infected subscribers causes CGNAT device failures and congests peering links. Your subscribers are the attack infrastructure, and your network takes the collateral damage. The presentation walks through how we linked these families, how they turn proxy SDKs into an infection vector, and what C2 signals operators can look for before attacks start. Based on original lab analysis, reverse engineering of six malware families, and Netflow telemetry from Nokia Deepfield ERT.

### Trust but Verify: An Assessment of Vulnerability Tagging Services
Speakers: Szu-Chun Huang , TU Delft
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/PKWTAR/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/PKWTAR/resources/20260519_RIPE-SzuChu_vq1HsEn.pdf | video: https://ripe92.ripe.net/media/videos/szu-chun-huang_trust-but-verify-an-assessment-of-vulnerability-tagging-services_side_20260519-170856.mp4
Internet-wide scanning services are widely used for attack surface discovery across organizations and the Internet. Enterprises, government agencies, and researchers rely on these tools to assess risks to Internet-facing infrastructure. However, their reliability and trustworthiness remain largely unexamined. This work addresses this gap by comparing results from three commercial scanners – Shodan, ONYPHE, and LeakIX – with findings from our independent experiments using verified Nuclei templates, designed to identify specific vulnerabilities through crafted benign requests. We found that the payload-based detections of Shodan are mostly confirmed. Yet, Nuclei finds many more vulnerable endpoints, so defenders might face massive underreporting. For Shodan’s banner-based detections, the opposite issue arises: a significant overreporting of false positives. This indicates that banner-based detections are unreliable. Moreover, three commercial services and Nuclei scans exhibit significant discrepancies. Our work has implications for industry users, policymakers, and the many academic researchers who rely on the results provided by these attack surface management services. By highlighting their shortcomings in vulnerability monitoring, this work serves as a call for action to advance and standardize such services to enhance their trustworthiness.

### Security WG RIPE 92 Outro
Speakers: Brian Nisbet
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/79/3DE9KC/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/3DE9KC/resources/Security_WG_RIPE_92__LBialY1.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/3DE9KC/resources/Security_WG_Slides__h4PMfgt.pptx | video: https://ripe92.ripe.net/media/videos/brian-nisbet_security-wg-ripe-92-outro_side_20260519-171742.mp4
A.O.B. Agenda for RIPE 93

## RIPE Community Plenary - Main Room (Thu, 16:00)

### RIPE Chair Team Update
Speakers: Mirjam Kühne , RIPE Community Anna Wilson
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/103/AJJJAE/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/AJJJAE/resources/RIPE_92_Community_Pl_lxz6gx3.pdf | video: https://ripe92.ripe.net/media/videos/mirjam-kuhne_ripe-chair-team-update_main_20260521-160020.mp4
Updating the community on activities since the last RIPE Meeting.

### ICP2 - Approaching the Finish Line: Key Issues and Next Steps
Speakers: Andrei Robachevsky , Global Cyber Alliance Herve Clement , ASO AC Constanze Buerger
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/103/QPWF7G/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/QPWF7G/resources/RIPE_92_ICP-2_Presen_GBj2dJ0.pdf | video: https://ripe92.ripe.net/media/videos/andrei-robachevsky_icp2-approaching-the-finish-line-key-issues-and-next-steps_main_20260521-163416.mp4
As the work on the RIR Governance document is in its final stage the NRO NC would like to present the latest status update and provide insight into key issues brought up by the community, which are being finalised. In the presentation we will share an overview of topics that have been discussed by the NRO NC since RIPE 91 – at its workshop in Montevideo in November 2025 and at ICANN 85 in March 2026. These topics include, among others, defining the threshold to recognise a new RIR, the audit and compliance requirements and mechanisms for emergency continuity. We will also outline the next steps leading to the publication of the final version of the document and its adoption. Since it took on the work of updating ICP-2 in 2023, the NRO NC has successfully held three consultations with the RIR and ICANN communities, including holding sessions at RIPE Meetings. Community feedback has been incorporated extensively to give the document its current shape, with work under way towards the final version of the RIR Governance Document.

### RIPE NCC and EU Competition Law
Speakers: Athina Fragkouli , RIPE NCC
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/103/EDZJ8Z/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/EDZJ8Z/resources/EU_Competition_law_a_Cegnfm7.pdf | video: https://ripe92.ripe.net/media/videos/athina-fragkouli_ripe-ncc-and-eu-competition-law_main_20260521-165241.mp4
Presentation of the legal analysis on EU Competition law aspects of the RIPE NCC as an RIR

### Personal Continuity Plans (Digital Legacy)
Speakers: Robert Kisteleki
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/103/7PEF7V/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/7PEF7V/resources/92_Kisteleki_-_RIPE__0aq4LIf.pdf | video: https://ripe92.ripe.net/media/videos/robert-kisteleki_personal-continuity-plans-digital-legacy_main_20260521-170745.mp4
Members of the network community quite often provide services to each other, also in their personal capacities. In some cases our (unplanned) inability to maintain these can cause issues beyond our control. This talk is about the idea of a possible RIPE document / BCP to describe what aspects one could or should plan in advance for such events.

### Secret WG Survey
Speakers: Remco van Mook
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/103/73SL3M/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/73SL3M/resources/swg_survey_results_oiIr2Ey.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/73SL3M/resources/swg_survey_results_I6wOmG5.key | video: https://ripe92.ripe.net/media/videos/remco-van-mook_secret-wg-survey_main_20260521-171612.mp4
Presenting of the results of the Secret WG survey from RIPE91, and exploring a path forward.

## BoF - Main Room (Mon, 18:00)

### Bridging IETF and RIPE - From Standards to Operations and back
Speakers: Dhruv Dhody , IAB Chair
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/69/MSEYVY/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/MSEYVY/resources/RIPE_92_BoF.pptx_jShlLw0.pdf | video: https://ripe92.ripe.net/media/videos/dhruv-dhody_bridging-ietf-and-ripe-from-standards-to-operations-and-back_main_20260518-180009.mp4
Description The Internet Engineering Task Force (IETF) works on developing the voluntary standards that underpin the global Internet. These standards influence operational practices, network architecture, and protocol evolution. Yet, it is the RIPE community that brings these standards to life through deployment, often encountering unforeseen operational challenges. This session will begin with a concise overview of key new developments at the IETF, including drafts, BoFs, new working groups, and topics currently gaining traction within the community. Special attention will be given to areas of direct relevance to network operators, such as security, DNS, IPv6, and routing. Building on this, the session will then explore a central question: how can the RIPE community and the IETF improve coordination and cooperation? Confirmed participants include members of IETF leadership: IAB (Dhruv, Yaroslav, Mathew) & IESG (Gorry, Éric)—who will deliver the overview, along with contributors active in both the IETF and RIPE communities who will participate in the discussion. Discussion Focus This BoF aims to facilitate an open discussion around: How can operational experience from the RIPE community better inform IETF work? How can feedback loops from deployment back into standards be improved? What are effective channels for sharing IETF developments with operators at RIPE? Is deeper participation in the IETF a worthwhile investment for network operators, and how can barriers be reduced? How should IETF and RIPE coordinate in Internet Governance (IG) spaces when representing the technical community? The goal is not to reach consensus, but to better understand expectations, identify gaps, and explore practical ways to strengthen engagement between the two communities.

## Diversity, Equity and Inclusion in Tech - Main Room (Tue, 18:00)

### Introduction to session "I Want To Break Free" & Presentation: "You are Not Alone"
Speakers: Denesh Bhabuta
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/81/7PRGSE/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/7PRGSE/resources/DeneshBhabuta-DEI-in_bNJclqc.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/7PRGSE/resources/DeneshBhabuta-DEI-in_AC7QITD.pdf | video: https://ripe92.ripe.net/media/videos/denesh-bhabuta_introduction-to-session-i-want-to-break-free-presentation-you-are-not-alon_main_20260519-175932.mp4
Session Theme: I Want To Break Free At RIPE 91, the DEI session focussed on the "D" in the acronym. Diversity. This time, at RIPE 92, we move on to the "E". Equity. And we are continuing with the human stories. This session brings together three talks that each explore what equity actually looks like in practice, from three very different angles. Toxic workplace dynamics, and the silence that allows them to persist. What genuine employment inclusion looks like when an employer gets it right. And the largely hidden weight of Rejection Sensitivity Dysphoria, and what it costs the people in our community who live with it every day. Three talks. One thread. The quieter, harder work of making sure that technical spaces are ones where everyone genuinely belongs. Abstract for the first talk: You Are Not Alone Toxic workplaces do not announce themselves. They seep in quietly, through cancelled meetings, ignored ideas, and a slow erosion of confidence that makes you wonder whether you are imagining things. Until one day you realise you are not. This talk grew out of a short essay written by a close friend, and from conversations with them and with others across this industry, people who recognised themselves in it immediately. It is about patterns that are far more common than most of us admit, and about the silence that allows them to continue. It is about what it feels like to be in it, what you can do if you are, and why speaking up, or simply showing up for someone else, matters more than you might think. This is not a talk about blame. It is a call to recognition, to solidarity, and to action.

### A Different Way to Success
Speakers: Peter Madsen , Norlys Henrik Haue Pedersen
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/81/9FGBJV/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/9FGBJV/resources/A_Different_Way_To_S_azLhB2b.pdf | video: https://ripe92.ripe.net/media/videos/peter-madsen_a-different-way-to-success_main_20260519-182534.mp4
This talk is a story about Henrik, a disabled person, managed to land his dream job as a network engineer in Norlys in Denmark. The talk highlights the challenges he has faced along the way, along with his view on why it is so hard to find a job when you cannot work full time. The talk also includes the perspective of Henriks manager. How is it to manage a flex jobber? What to consider as a manager, when flex jobbers apply for your full time positions. How to tailor the work environment to flex jobbers. Lastly the hidden truth, about how most network engineers suffer from some kind of disability, is reviled and how we all benefit from the working environment that we have stup in regarding flex jobbers. Finally Henrik presents the kind of work that he have been doing during his time in Norlys, to inspire both workers and managers.

### Rejection Sensitivity Dysphoria and Accommodations in the Workplace
Speakers: Robert Lister Paul Ginsberg , ADHD Life Coach
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/81/TUP98E/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/TUP98E/resources/rsd-ripe92-1_5Yq5dCH.pdf | video: https://ripe92.ripe.net/media/videos/robert-lister_rejection-sensitivity-dysphoria-and-accommodations-in-the-workplace_main_20260519-184638.mp4
Rob Lister returns to discuss ADHD, this time bringing along with friend and ADHD Coach Paul Ginsberg, to explore a dirty secret that 99% of ADHDers struggle with, as well as others: Rejection Sensitivity Dysphoria. You’ll come out knowing more about this topic, the warning signs, the impact and how to support colleagues. Hopefully. Unless the talk is a disaster… Rob will also be sharing his own experience of RSD and also an update about reasonable accommodations in the workplace. Hint: they are still keeping him on.

## BoF - Main Room (Thu, 18:00)

### Practical AI BoF
Speakers: Sander Steffann , ProVision David Verolme , VeroCon
page: https://ripe92.ripe.net/programme/meeting-plan/sessions/105/3Q9Y9H/ | slides: https://pretalx.ripe.net/media/ripe-92/submissions/3Q9Y9H/resources/2026-05-21_Practical_vBPcSLe.pdf | slides: https://pretalx.ripe.net/media/ripe-92/submissions/3Q9Y9H/resources/ripe92_ai_bof_usecas_egRvQPT.pdf | video: https://ripe92.ripe.net/media/videos/sander-steffann_practical-ai-bof_main_20260521-180046.mp4
AI is getting more and more attention, part of it hype, part of it real. This BoF focuses on the real and practical applications for network engineers and ISPs that are usable today. Focus points: - assisted deployment - log file analysis - traffic analysis - routing reports - knowledge retrieval using internal documentation and RAG - call and ticket analysis for ISP support teams

