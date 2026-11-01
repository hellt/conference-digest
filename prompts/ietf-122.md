>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-122. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-122.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-122.md
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

Below is the program for IETF 122 (Bangkok) (standards). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a standards program: working-group sessions and Internet-Drafts. Judge
what is moving toward consensus, what is newly adopted by a working group, and
what would affect implementations the PM cares about. The draft titles and
abstracts carry the substance; the sessions themselves are thin, so reason from
the drafts. Up-rank drafts that change wire formats, security properties, or
identity/authorization mechanisms; note when something is early (individual
draft) versus mature (WG last call, IETF stream).

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
conference: IETF 122 (Bangkok)
type: standards
source_url: https://datatracker.ietf.org/meeting/122/agenda.json
generated: 2026-11-01
registry_key: ietf-122
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Working Group: 6man

### Internet Control Message Protocol (ICMPv6) Reflection
Draft: draft-ietf-6man-icmpv6-reflection · Working group: 6man
Agenda: draft-ietf-6man-icmpv6-reflection
page: https://datatracker.ietf.org/doc/draft-ietf-6man-icmpv6-reflection/ | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
This document specifies the ICMPv6 Reflection utility. The ICMPv6 Reflection utility is a diagnostic tool, similar to Ping and the ICMPv6 PROBE utility. It is similar to Ping and PROBE in that it relies on a stateless message exchange between a probing node and a probed node. The probing node sends a request to the probed node and the probed node responds to the request. The ICMPv6 Reflection utility differs from Ping and PROBE because, in the ICMPv6 Reflection utility, the probing node requests a snapshot of the message that it sent, as it was when arrived at the probed node. The probed node returns the requested snapshot. The ICMPv6 Reflection utility is useful because it can allow the user to see how the network modified the request as it traveled from the probing node to the probed node.

### Improving the Robustness of Stateless Address Autoconfiguration (SLAAC) to Flash Renumbering Events
Draft: draft-ietf-6man-slaac-renum · Working group: 6man
Agenda: draft-ietf-6man-slaac-renum
page: https://datatracker.ietf.org/doc/draft-ietf-6man-slaac-renum/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-improving-the-robustness-of-stateless-address-autoconfiguration-slaac-to-flash-renumbering-events-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
In scenarios where network configuration information becomes invalid without explicit notification to the local network, local hosts may end up employing stale information for an unacceptably long period of time, thus resulting in interoperability problems. This document improves the reaction of IPv6 Stateless Address Autoconfiguration to such configuration changes. It formally updates RFC 4191, RFC 4861, RFC 4862, RFC 8106, RFC 8781, RFC 9096, and RFC 9463.

### IPv6 Node Requirements
Draft: draft-ietf-6man-rfc8504-bis · Working group: 6man
Agenda: draft-ietf-6man-rfc8504-bis
page: https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-ipv6-node-requirements-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
This document defines requirements for IPv6 nodes. It is expected that IPv6 will be deployed in a wide range of devices and situations. Specifying the requirements for IPv6 nodes allows IPv6 to function well and interoperate in a large number of situations and deployments. This document obsoletes RFC 8504, and in turn RFC 6434 and its predecessor, RFC 4294.

### Clarifying SRv6 SID List Processing
Draft: draft-farrel-6man-sidlist-clarification · Working group: 6man
Agenda: draft-farrel-6man-sidlist-clarification ,
page: https://datatracker.ietf.org/doc/draft-farrel-6man-sidlist-clarification/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-clarifying-srv6-sid-list-processing-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
Segment Routing over IPv6 (SRv6) is the instantiation of Segment Routing (SR) on the IPv6 data plane. Segments are indicated by Segment Identifiers (SIDs). SRv6 utilizes the Segment Routing Header (SRH), an IPv6 extension header, that includes a SID list indicating the sequence of segments and any additional processing to be performed. This document updates RFC 8754 by clarifying the processing of SID list entries. It does not change any elements of the SRv6 architecture.

### Using Prefix-Specific Link-Local Addresses to Improve SLAAC Robustness
Draft: draft-link-6man-gulla · Working group: 6man
Agenda: draft-link-6man-gulla
page: https://datatracker.ietf.org/doc/draft-link-6man-gulla/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-using-prefix-specific-link-local-addresses-to-improve-slaac-robustness-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
When an IPv6 prefix assigned to a link changes, hosts may not be explicitly notified about the change. Similarly, in some scenario a link attachement for the host may change without the host detecting it. In both cases the host does not receive any signals to trigger the network stack configuration refresh, so it may continue to use "old" addresses which are not valid for the link. This leads to packet loss and service disruption. This document proposes a mechanism to mitigate this issue. Routers are advised to send Router Advertisements containing distinct Prefix Information Options (PIOs) from different link-local addresses. This, in conjunction with RFC6724 (Default Source Address Selection) Rule 5.5 and RFC8028 (first-hop selection requirements), enables hosts to detect prefix changes more rapidly and select the correct source address, thereby improving the robustness of SLAAC.

### Transmission of IP Packets over Overlay Multilink Network (OMNI) Interfaces
Draft: draft-templin-6man-omni3 · Working group: 6man
Agenda: draft-templin-6man-omni3
page: https://datatracker.ietf.org/doc/draft-templin-6man-omni3/ | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
Mobile nodes that operate in air/land/sea/space domains (e.g., aircraft of various configurations, terrestrial vehicles, seagoing vessels, space systems, enterprise wireless devices, pedestrians with cell phones, etc.) configure mobile routers to connect end user network peers with Internetwork correspondents over wireless and/or wired-line data links. This document presents a multilink virtual interface specification that supports mobile node coordination with a network-based mobility service, fixed node correspondents and/or other mobile node peers. The virtual interface provides an adaptation layer service that supports secure global mobile Internetworking. This document specifies the transmission of IP packets over Overlay Multilink Network (OMNI) Interfaces.

### Deterministic Routing Header
Draft: draft-pb-6man-deterministic-crh · Working group: 6man
Agenda: draft-pb-6man-deterministic-crh
page: https://datatracker.ietf.org/doc/draft-pb-6man-deterministic-crh/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-crh-20-deterministic-routing-header-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
This document introduces a new IPv6 Routing Header used for deterministic forwarding wihch is generally a strict explicit path. This Routing Header will contain the decoupled topology instructions and deterministic forwarding resource indications. The target is low cost of encapasultion and less amount of allocated SIDs.

### Problem Statement with Aggregate Header Limit for IPv6
Draft: draft-liu-6man-aggregate-header-limit-problem · Working group: 6man
Agenda: draft-liu-6man-aggregate-header-limit-problem
page: https://datatracker.ietf.org/doc/draft-liu-6man-aggregate-header-limit-problem/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-problem-statement-with-aggregate-header-limit-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
This document first proposes the concept of "Aggregate header limit for IPv6"(IPv6-AHL) to indicate the total header size that a router is able to process at full forwarding rate for IPv6 packets. Then this document describes the problems for path calculation and function enablement without the awareness of IPv6-AHL, and the considerations for IPv6-AHL collection are also included.

### Extending ICMPv6 for SRv6-related Information Validation
Draft: draft-liu-6man-icmp-verification · Working group: 6man
Agenda: draft-liu-6man-icmp-verification
page: https://datatracker.ietf.org/doc/draft-liu-6man-icmp-verification/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-extending-icmpv6-for-srv6-related-information-validation-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
This document introduces the mechanism to verify the data plane against the control plane and detect data plane failures in IPv6/SRv6 networks by extending ICMPv6 messages.

### Terminal Identity Authentication Based on Address Label
Draft: draft-guan-6man-ipv6-id-authentication · Working group: 6man
Agenda: draft-guan-6man-ipv6-id-authentication
page: https://datatracker.ietf.org/doc/draft-guan-6man-ipv6-id-authentication/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-terminal-identity-authentication-based-on-address-label-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
This document proposes an IPv6-based address label terminal identity authentication architecture, which tightly binds identity information to the source address of data packets. This approach enables hop-by- hop identity authentication while ensuring source address verification. The mechanism facilitates user identity verification, ensuring privacy protection, security, and efficient auditing. Additionally, this document details the implementation of address label authentication within the IPv6 extension header.

### IPv6 Reflection Utility
Presentation · Working group: 6man
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-ipv6-reflection-utility-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
Slides presented at the 6man session; no Internet-Draft is linked to them.

### Send/CGA for OMNI Links
Presentation · Working group: 6man
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-6man-sendcga-for-omni-links-00 | video: https://www.youtube.com/watch?v=HAx8kDFp2TE | materials: https://datatracker.ietf.org/meeting/122/session/6man
Slides presented at the 6man session; no Internet-Draft is linked to them.

## Working Group: acme

### ACME ARI and Profiles
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-acme-ari-and-profiles-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### DTN Node ID Validation
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-dtn-node-id-validation-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### ACME DNS Update
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-acme-dns-update-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### ACME-RATS
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-ietf-122-acme-rats-presentation-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### authority token stir jwt claim constraints
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-authority-token-stir-jwtclaimconstraints-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### ACME PK Challenges
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-acme-pk-challenges-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### The bigger, Huger, Mega Slide Deck
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-acme-the-bigger-huger-mega-slide-deck-00 | video: https://www.youtube.com/watch?v=_y8oN9p-xHI | materials: https://datatracker.ietf.org/meeting/122/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

## Working Group: anima

### cBRSKI / Join Proxy for cBRSKI
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-anima-cbrski-join-proxy-for-cbrski-00 | video: https://www.youtube.com/watch?v=k7tllOsxIE8 | materials: https://datatracker.ietf.org/meeting/122/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### RFC8366bis - updates and extensions (2)
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-anima-rfc8366bis-updates-and-extensions-2-00 | video: https://www.youtube.com/watch?v=k7tllOsxIE8 | materials: https://datatracker.ietf.org/meeting/122/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Lightweight GRASP
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-anima-lightweight-grasp-01 | video: https://www.youtube.com/watch?v=k7tllOsxIE8 | materials: https://datatracker.ietf.org/meeting/122/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### ANIMA interim 2025 01 summary
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-anima-04-anima-interim-2025-01-summary-00 | video: https://www.youtube.com/watch?v=k7tllOsxIE8 | materials: https://datatracker.ietf.org/meeting/122/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### ANI without ACP
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-anima-ani-without-acp-00 | video: https://www.youtube.com/watch?v=k7tllOsxIE8 | materials: https://datatracker.ietf.org/meeting/122/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Mobility Management & Capability Negotiation (MMCN)
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-anima-mobility-management-capability-negotiation-mmcn-00 | video: https://www.youtube.com/watch?v=k7tllOsxIE8 | materials: https://datatracker.ietf.org/meeting/122/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

## Working Group: bess

### BGP Usage for SD-WAN Overlay Networks
Draft: draft-ietf-bess-bgp-sdwan-usage · Working group: bess
Agenda: draft-ietf-bess-bgp-sdwan-usage Linda 10 13:35 - 13:45
page: https://datatracker.ietf.org/doc/draft-ietf-bess-bgp-sdwan-usage/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-draft-ietf-bess-bgp-sdwan-usage-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This document illustrates how a BGP-based control plane can be used to manage large scale Software Defined WAN (SD-WAN) overlay networks by distributing edge service reachability information, WAN port attributes, and underlay path details, thereby minimizing manual provisioning. In such deployments, BGP can provide a standards-based mechanism for distributing information that may otherwise be exchanged using proprietary SD-WAN control-plane mechanisms. However, extensions to BGP are needed to achieve that goal.

### BGP MPLS-Based Ethernet VPN
Draft: draft-ietf-bess-rfc7432bis · Working group: bess
Agenda: draft-ietf-bess-rfc7432bis Ali Sajassi 5 13:45 - 13:50
page: https://datatracker.ietf.org/doc/draft-ietf-bess-rfc7432bis/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-draft-ietf-bess-rfc7432bis-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This document describes procedures for Ethernet VPN (EVPN), a BGP MPLS-based solution which addresses the requirements specified in the corresponding RFC - "Requirements for Ethernet VPN (EVPN)". This document obsoletes RFC7432 (BGP MPLS-Based Ethernet VPN) and updates RFC8214 (Virtual Private Wire Service Support in Ethernet VPN).

### EVPN Support for L3 Fast Convergence and Aliasing/Backup Path
Draft: draft-ietf-bess-evpn-ip-aliasing · Working group: bess
Agenda: draft-ietf-bess-evpn-ip-aliasing Jorge 5 13:50 - 13:55
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-ip-aliasing/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-ietf122-bess-evpn-ip-aliasing02-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This document proposes an EVPN extension to allow several of its multi-homing functions, fast convergence, and aliasing/backup path, to be used in conjunction with inter-subnet forwarding. The extension is limited to All-Active and Single-Active redundancy modes.

### Domain Path (D-PATH) for Ethernet VPN (EVPN) Interconnect Networks
Draft: draft-ietf-bess-evpn-dpath · Working group: bess
Agenda: draft-ietf-bess-evpn-dpath Jorge 5 13:55 - 14:00
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-dpath/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-ietf122-bess-evpn-dpath-02-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
The BGP Domain PATH (D-PATH) attribute is defined for Inter-Subnet Forwarding (ISF) BGP Sub-Address Families that advertise IP prefixes or MAC addresses. D-PATH already applies to EVPN Route Type 2 when used for ISF, to EVPN Route Type 5 (IP Prefix routes), and to IP-VPN routes. When used along with those routes, it identifies the domain(s) through which the routes have passed and that information can be used by the receiver BGP speakers to detect routing loops or influence the BGP best path selection. This document extends the use of D-PATH to EVPN Route Type 2 when not used for ISF, to EVPN Route Type 1 (Ethernet Auto-Discovery per-EVI) for EVPN VPWS, and to EVPN Route Type 3 (Inclusive Multicast Ethernet Tag routes).

### BGP Encodings and Procedures for Multicast in MPLS/BGP IP VPNs
Draft: draft-zzhang-bess-rfc6514bis · Working group: bess
Agenda: draft-zzhang-bess-rfc6514bis Mankamana 8 14:00 - 14:08
page: https://datatracker.ietf.org/doc/draft-zzhang-bess-rfc6514bis/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-draft-zzhang-bess-rfc6514bis-00-02 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
RFC 6514 describes the BGP encodings and procedures for exchanging the information elements required by Multicast in MPLS/BGP IP VPNs, as specified in RFC 6513. This document updates and obsoletes RFC 6514. The original authors of RFC 6514 are listed at the end of this document.

### Ethernet VPN Virtual Private Wire Services Gateway Solution
Draft: draft-sr-bess-evpn-vpws-gateway · Working group: bess
Agenda: draft-sr-bess-evpn-vpws-gateway Jorge 5 14:15 - 14:20
page: https://datatracker.ietf.org/doc/draft-sr-bess-evpn-vpws-gateway/ | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
Ethernet Virtual Private Network Virtual Private Wire Services (EVPN VPWS) need to be deployed in high scale multi-domain networks, where each domain can use a different transport technology, such as MPLS, VXLAN or Segment Routing with MPLS or IPv6 Segment Identifiers (SIDs). While transport interworking solutions on border routers spare the border routers from having to process service routes, they do not always meet the multi-homing, redundancy, and operational requirements, or provide the isolation that each domain requires. This document analyzes the scenarios in which an interconnect solution for EVPN VPWS using EVPN Domain Gateways is needed, and adds the required extensions to support it.

### EVPN Multicast Forwarding for EVPN to EVPN Gateways
Draft: draft-rabnic-bess-evpn-mcast-eeg · Working group: bess
Agenda: draft-rabnic-bess-evpn-mcast-eeg Jorge 5 14:20 - 14:25
page: https://datatracker.ietf.org/doc/draft-rabnic-bess-evpn-mcast-eeg/ | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This document proposes an EVPN (Ethernet Virtual Private Network) extension to allow IP multicast forwarding on Service Gateways that interconnect two or more EVPN domains.

### Dynamic Overlay Load Balancing
Draft: draft-zzhang-bess-dynamic-overlay-lb · Working group: bess
Agenda: draft-zzhang-bess-dynamic-overlay-lb Jeffery 10 14:25 - 14:35
page: https://datatracker.ietf.org/doc/draft-zzhang-bess-dynamic-overlay-lb/ | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This document specifies a mechanism for an overlay service ingress PE to dynamically load-balance traffic to Multi-Homing PEs based on near real-time access link information advertised by those PEs.

### Per-Flow EVPN Designated Forwarder Election
Draft: draft-kriswamy-bess-evpn-perflow-df · Working group: bess
Agenda: draft-kriswamy-bess-evpn-perflow-df Krishnaswamy 10 14:35 - 14:45
page: https://datatracker.ietf.org/doc/draft-kriswamy-bess-evpn-perflow-df/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-draft-kriswamy-bess-evpn-perflow-df-01 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
The Ethernet Virtual Private Network (EVPN) solution offers procedures for electing a Designated Forwarder (DF) for multihomed Ethernet Segments. In this context, the Provider Edge (PE) router is responsible for sending Broadcast, Unknown Unicast, and Multicast (BUM) traffic to a multihomed device or network. This applies in cases of an all-active multihomed Ethernet Segment (ES) as well as for BUM and unicast traffic in the case of single-active multihoming. While the Default Algorithm provides an efficient and automated mechanism for selecting the DF across Ethernet Tags within an Ethernet Segment, it does not provide Per-flow DF selection within an EVPN Instance (EVI). This document defines a new DF Election Algorithm that performs Per- flow DF selection by defining a new DF Algorithm value.

### Layer-3 Accessible EVPN Services
Draft: draft-wang-bess-l3-accessible-evpn · Working group: bess
Agenda: draft-wang-bess-l3-accessible-evpn Aijun 5 14:45 - 14:50
page: https://datatracker.ietf.org/doc/draft-wang-bess-l3-accessible-evpn/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-l3-accessible-evpn-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This draft describes layer-3 accessible EVPN service interfaces, which aim is to connect the layer 2 customers to one EVPN backbone, via the layer 3 network, and keep the traffic isolation among different layer 2 customers. It proposes to extend the VxLAN packet format to transfer the customer's Virtual Network Identifier(VNI) information, and also the related control plane extension.

### BGP Extensions for the Mobile User Plane (MUP) SAFI
Draft: draft-mpmz-bess-mup-safi · Working group: bess
Agenda: draft-mpmz-bess-mup-safi-05 Keyur 5
page: https://datatracker.ietf.org/doc/draft-mpmz-bess-mup-safi/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-draft-mpmz-bess-mup-safi-05-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
This document defines a new SAFI known as a BGP Mobile User Plane (BGP-MUP) SAFI to support MUP Extensions and a extended community for BGP. This document also provides BGP signaling and procedures for the new SAFI to convert mobile session information into appropriate IP forwarding information. These extensions can be used by operators between a PE, and a Controller for integrating mobile user plane into BGP MUP network using the IP based routing.

### SRv6 Service SID Anycast Flag
Draft: draft-liu-bess-srv6-service-sid-anycast-flag · Working group: bess
Agenda: draft-liu-bess-srv6-service-sid-anycast-flag Changwang 5
page: https://datatracker.ietf.org/doc/draft-liu-bess-srv6-service-sid-anycast-flag/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-srv6-service-sid-anycast-flag-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
In some multihoming SRv6 L3VPN and EVPN scenarios, there are requirements for the egress PE to advertise both unicast and anycast SRv6 Service SIDs for the same service. This document defines the Anycast-flag for SRv6 Service SIDs carried in BGP messages.

### IETF122 BESS bess-evpn-vpws-gateway06
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-ietf122-bess-bess-evpn-vpws-gateway06-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### IETF122 BESS evpn-mcast-egg05
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-ietf122-bess-evpn-mcast-egg05-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### Dynamic GLB for Overlay Jeffrey
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-bess-dynamic-glb-for-overlay-jeffrey-00 | video: https://www.youtube.com/watch?v=KqA5__fJw3g | materials: https://datatracker.ietf.org/meeting/122/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

## Working Group: cose

### SLH-DSA for JOSE and COSE
Draft: draft-ietf-cose-sphincs-plus · Working group: cose
Agenda: [10 min] draft-ietf-cose-sphincs-plus & draft-ietf-cose-falcon - Brent Zundel
page: https://datatracker.ietf.org/doc/draft-ietf-cose-sphincs-plus/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-sphincs-plus-and-falcon-for-jose-and-cose-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
Digital signatures are used within JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) to protect the integrity and authenticity of messages, such as JSON Web Signatures and signed COSE structures. This document specifies JOSE and COSE serializations for the Stateless Hash-Based Digital Signature Standard (SLH-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 205. The conventions for the associated algorithm identifiers, signatures, public keys, and private keys are also specified.

### FN-DSA for JOSE and COSE
Draft: draft-ietf-cose-falcon · Working group: cose
Agenda: [10 min] draft-ietf-cose-sphincs-plus & draft-ietf-cose-falcon - Brent Zundel
page: https://datatracker.ietf.org/doc/draft-ietf-cose-falcon/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-ml-dsa-for-jose-and-cose-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This document specifies JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 206 (expected to be published in late 2026 early 2027). It does not define new cryptographic primitives; rather, it specifies how existing FN-DSA mechanisms are serialized for use in JOSE and COSE. This document registers signature algorithms for JOSE and COSE, specifically FN-DSA-512 and FN-DSA-1024.

### ML-DSA for JOSE and COSE
Draft: draft-ietf-cose-dilithium · Working group: cose
Agenda: [10 min] draft-ietf-cose-dilithium - Brent Zundel
page: https://datatracker.ietf.org/doc/draft-ietf-cose-dilithium/ | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This document specifies JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for Module- Lattice-Based Digital Signature Standard (ML-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 204.

### AES-GMAC for COSE
Draft: draft-sipos-cose-gmac · Working group: cose
Agenda: [10 min] draft-sipos-cose-gmac-00 - Brian Sipos
page: https://datatracker.ietf.org/doc/draft-sipos-cose-gmac/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-aes-gmac-in-cose-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This document registers COSE algorithm code points for using the Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM) to generate a Message Authentication Code (AES-GMAC). The security strength provided by these registrations is identical to existing COSE registrations for AES-GCM authenticated encryption.

### CBOR Encoded X.509 Certificates (C509 Certificates)
Draft: draft-ietf-cose-cbor-encoded-cert · Working group: cose
Agenda: [15 min] draft-ietf-cose-cbor-encoded-cert-12 - John Mattsson
page: https://datatracker.ietf.org/doc/draft-ietf-cose-cbor-encoded-cert/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-cbor-encoded-x509-c509-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This document specifies a CBOR encoding of X.509 certificates. The resulting certificates are called C509 certificates. The CBOR encoding supports a large subset of RFC 5280 and common certificate profiles, and it is extensible. Two types of C509 certificates are defined. One type is an invertible CBOR re-encoding of DER-encoded X.509 certificates with the signature field copied from the DER encoding. The other type is identical except that the signature is computed over the CBOR encoding instead of the DER encoding, thereby avoiding the use of ASN.1. Both types of certificates have the same semantics as X.509 while providing comparable size reduction. This document also specifies CBOR-encoded data structures for certification requests and certification request templates, new COSE headers, as well as a TLS certificate type and a file format for C509. This document updates RFC 6698 by extending the TLSA selectors registry to include C509 certificates.

### Use of Hybrid Public-Key Encryption (HPKE) with CBOR Object Signing and Encryption (COSE)
Draft: draft-ietf-cose-hpke · Working group: cose
Agenda: [20 min] draft-ietf-cose-hpke - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-hpke/ | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This specification defines hybrid public-key encryption (HPKE) for use with CBOR Object Signing and Encryption (COSE). HPKE offers a variant of public-key encryption of arbitrary-sized plaintexts for a recipient public key. HPKE is a general encryption framework utilizing an asymmetric key encapsulation mechanism (KEM), a key derivation function (KDF), and an Authenticated Encryption with Associated Data (AEAD) algorithm. This document defines the use of HPKE with COSE. Authentication for HPKE in COSE is provided by COSE-native security mechanisms or by the pre-shared key authenticated variant of HPKE.

### COSE Hash Envelope
Draft: draft-ietf-cose-hash-envelope · Working group: cose
Agenda: [30 min] draft-ietf-cose-hash-envelope - Steve Lasker
page: https://datatracker.ietf.org/doc/draft-ietf-cose-hash-envelope/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-cose-hash-envelope-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This document defines new COSE header parameters for signaling a payload as an output of a hash function. This mechanism enables faster validation, as access to the original payload is not required for signature validation. Additionally, hints of the hashed payload's content format and availability are defined, providing references to optional discovery mechanisms that can help to find original payload content.

### Split Signing Algorithms for COSE
Draft: draft-lundberg-cose-two-party-signing-algs · Working group: cose
Agenda: [15 min] draft-lundberg-cose-two-party-signing-algs - Mike Jones
page: https://datatracker.ietf.org/doc/draft-lundberg-cose-two-party-signing-algs/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-cose-algorithms-for-two-party-signing-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
This specification defines COSE algorithm identifiers for negotiating how to split a signature algorithm between two cooperating parties. Typically the first party hashes the data to be signed and the second party finishes the signature over the hashed data. This is a common technique, useful for example when the signing private key is held in a smart card or similar hardware component with limited processing power and communication bandwidth. The resulting signatures are identical in structure to those computed by a single party, and can be verified using the same verification algorithm without additional steps to preprocess the signed data.

### COSE HPKE
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-cose-hpke-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

### COSE Header Parameters for Carrying and Referencing Chains of CWTs
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-cose-cose-header-parameters-for-carrying-and-referencing-chains-of-cwts-00 | video: https://www.youtube.com/watch?v=i5qjHm-cU9U | materials: https://datatracker.ietf.org/meeting/122/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

## Working Group: dnsop

### Clarifications on CDS/CDNSKEY and CSYNC Consistency
Draft: draft-ietf-dnsop-cds-consistency · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-cds-consistency/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-cds-consistency/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-update-on-draft-ietf-dnsop-cds-consistency-00 | video: https://www.youtube.com/watch?v=6s0Q5oiydzc | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
Maintenance of DNS delegations requires occasional changes of the DS and NS record sets on the parent side of the delegation. For the case of DS records, "Automating DNSSEC Delegation Trust Maintenance" (RFC 7344) provides automation by allowing the child to publish CDS and/or CDNSKEY records holding the prospective DS parameters which the parent can ingest. Similarly, "Child-to-Parent Synchronization in DNS" (RFC 7477) specifies CSYNC records to indicate a desired update of the delegation's NS (and glue) records. Parent-side entities (e.g., Registries and Registrars) can query these records from the child and, after validation, use them to update the parent- side Resource Record Sets (RRsets) of the delegation. This document specifies under which conditions the target states expressed via CDS/CDNSKEY and CSYNC records are considered "consistent". Parent-side entities accepting such records from the child have to ensure that update requests retrieved from different authoritative nameservers satisfy these consistency requirements before taking any action based on them. This document updates RFC 7344 and RFC 7477.

### Domain Control Validation using DNS
Draft: draft-ietf-dnsop-domain-verification-techniques · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-domain-verification-techniques/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-domain-verification-techniques/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessb-domain-control-validation-using-dns-00 | video: https://www.youtube.com/watch?v=6s0Q5oiydzc | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
Many application services on the Internet need to verify ownership or control of a domain in the Domain Name System (DNS). The general term for this process is "Domain Control Validation", and it can be done using a variety of methods such as email, HTTP/HTTPS, or the DNS itself. This document focuses only on DNS-based methods, which typically involve the Application Service Provider requesting a DNS record with a specific format and content to be visible in the domain to be verified. There is wide variation in the details of these methods today. This document provides some best practices to avoid known problems.

### DNS Filtering Details for Applications
Draft: draft-nottingham-public-resolver-errors · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-nottingham-public-resolver-errors/
page: https://datatracker.ietf.org/doc/draft-nottingham-public-resolver-errors/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessb-dns-filtering-details-for-applications-01 | video: https://www.youtube.com/watch?v=6s0Q5oiydzc | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
[I-D.ietf-dnsop-structured-dns-error] introduces structured error data for DNS responses that have been filtered. This specification allows more specific details of filtering incidents to be conveyed. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/mnot/public-resolver-errors.

### Clarifications to the DNS Ranking Data
Draft: draft-fujiwara-dnsop-ranking-data · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-ranking-data/
page: https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-ranking-data/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessb-clarifications-to-the-dns-ranking-data-00 | video: https://www.youtube.com/watch?v=6s0Q5oiydzc | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document obsoletes Section 5.4.1 (Ranking data) of RFC 2181, and specifies directives whereby the source of the data determines for what purposes it may be used.

### Signaling Zone Owner Intent
Draft: draft-leon-dnsop-signaling-zone-owner-intent · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-leon-dnsop-signaling-zone-owner-intent/
page: https://datatracker.ietf.org/doc/draft-leon-dnsop-signaling-zone-owner-intent/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-signaling-zone-owner-intent-via-dns-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document introduces a standardized mechanism for zone owners to signal their intent regarding DNS provider responsibilities through DNS itself. It defines two new DNS RRtypes -- HSYNC (Horizontal Synchronization, per-provider enrollment) and HSYNCPARAM (zone-wide multi-provider policy) -- that together enable zone owners to designate which Providers are authorized to serve and/or sign their zones, control whether Providers or the zone owner manages the NS RRset, and specify zone transfer chain configurations. The HSYNC and HSYNCPARAM records allow DNS Providers to discover each other and establish secure communication, either using the JOSE framework over DNS or via a RESTful API secured by TLS. This provider-to-provider communication enables automated coordination for tasks such as NS RRset management and DNSSEC-related operations. The document describes how the Providers discover one another, establish secure communication, and maintain it with periodic keep-alives; this specification covers those discovery and communication-establishment aspects, while the on-the-wire framing of the messages the Providers exchange is defined in a companion document. While a distributed DNSSEC multi-signer architecture (similar to "model 2" in [RFC8901]) is an important application of this framework, the HSYNC-based signaling supports broader provider synchronization needs. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-leon-dnsop-signaling-zone-owner- intent (https://github.com/johanix/draft-leon-dnsop-signaling-zone- owner-intent). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Signaling Key State Via a DNS EDNS(0) Option
Draft: draft-berra-dnsop-keystate · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-berra-dnsop-keystate/
page: https://datatracker.ietf.org/doc/draft-berra-dnsop-keystate/ | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document introduces the KeyState EDNS(0) option, to enable a child operator to query a parent UPDATE Receiver about the state of a SIG(0) key used to secure cross-zone-cut DNS UPDATE messages. The KeyState option allows the child to include a key state inquiry in its DNS query, and the parent to include the corresponding key state in its response. This addresses the challenge of maintaining synchronization of SIG(0) keys between the child and the parent UPDATE Receiver: the child can become aware of any issue with its SIG(0) key in advance, before attempting the next operational DNS UPDATE. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-berra-dnsop-keystate (https://github.com/johanix/draft-berra-dnsop-keystate). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Automating DNS Delegation Management via DDNS
Draft: draft-johani-dnsop-delegation-mgmt-via-ddns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-johani-dnsop-delegation-mgmt-via-ddns/
page: https://datatracker.ietf.org/doc/draft-johani-dnsop-delegation-mgmt-via-ddns/ | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
Delegation information (i.e. the NS RRset, possible glue, possible DS records) should always be kept in sync between child zone and parent zone. However, in practice that is not always the case. When the delegation information is not in sync the child zone is usually working fine, but without the amount of redundancy that the zone owner likely expects to have. Hence, should any further problems ensue it could have catastropic consequences. The DNS name space has lived with this problem for decades and it never goes away. Or, rather, it will never go away until a fully automated mechanism for how to keep the information in sync automatically is deployed. This document proposes such a mechanism. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-johani-dnsop-delegation-mgmt-via- ddns (https://github.com/johanix/draft-johani-dnsop-delegation-mgmt- via-ddns). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### DNS Update with JSON
Draft: draft-hoffman-duj · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-hoffman-duj/
page: https://datatracker.ietf.org/doc/draft-hoffman-duj/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-dns-update-with-json-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
It is common for service providers such as certificate authorities and social media providers to want users to update the users' zones to prove that they control those zones, or to add other features. Currently, service providers tell users to do this using human language describing the resource record type and data values to enter into the zone. This document describes a text format, called "DNS update with JSON" or "DUJ", for such a service provider to give to a user, with the expectation that the user would copy and paste the text to their DNS operator to update the user's zone. DNS operators who know how to handle DUJ strings will make the update process easier and more predictable for their users.

### Domain Name System (DNS) Public Key Based Request and Transaction Authentication ( SIG(0) )
Draft: draft-eastlake-dnsop-rfc2931bis-sigzero · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-eastlake-dnsop-rfc2931bis-sigzero/
page: https://datatracker.ietf.org/doc/draft-eastlake-dnsop-rfc2931bis-sigzero/ | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document specifies use of the Domain Name System (DNS) SIG Resource Record (RR) to provide a public key based authentication of DNS requests and transactions. Such a resource record, because it has a "type covered" field of zero, is frequently called a "SIG(0)". This document obsoletes RFC 2931.

### Collision Free Keytags for DNSSEC
Draft: draft-huque-dnsop-keytags · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-huque-dnsop-keytags/
page: https://datatracker.ietf.org/doc/draft-huque-dnsop-keytags/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessa-collision-free-key-tags-for-dnssec-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
DNSSEC employs a Key Tag field in the RRSIG and DS resource records in order to efficiently identify the key that produced a DNSSEC signature and the key that should be used as a secure entry point into a delegated zone. The Key Tag was not intended to be a unique identifier. Key tag collisions can occur in practice for keys in the same zone, though they are relatively rare in normal operation. Colliding key tags impose additional work on a validating resolver because it then has to check signatures for each of the candidate set of keys identified by the Key Tag. Furthermore, they open up resolvers to computational denial of service attacks by adversaries deploying specially crafted zones with many intentionally colliding key tags. This document specifies updates to the DNSSEC protocol and the process of key generation to avoid colliding key tags.

### dry-run DNSSEC
Draft: draft-yorgos-dnsop-dry-run-dnssec · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-yorgos-dnsop-dry-run-dnssec/
page: https://datatracker.ietf.org/doc/draft-yorgos-dnsop-dry-run-dnssec/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-dry-run-yorgos-ietf122-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document describes a method called "dry-run DNSSEC" that allows for testing DNSSEC deployments without affecting the DNS service in case of DNSSEC errors. It accomplishes that by introducing new DS Type Digest Algorithms that when used in every record of a DS RRset, referred to as dry-run DS, signal to validating resolvers that dry- run DNSSEC is used for the zone. DNSSEC errors are then reported with DNS Error Reporting, but any bogus responses to clients are withheld. Instead, validating resolvers fallback from dry-run DNSSEC and provide the response that would have been answered without the presence of the dry-run DS. A further EDNS option is presented for clients to opt-in for dry-run DNSSEC errors and allow for end-to-end DNSSEC testing.

### A Top-level Domain for Private Use
Draft: draft-davies-internal-tld · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-davies-internal-tld/
page: https://datatracker.ietf.org/doc/draft-davies-internal-tld/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessa-draft-davies-internal-tld-a-top-level-domain-for-private-use-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document describes the "internal" top-level domain for use in private applications.

### Standardized Query Name for DNS Resolver Reachability Probes
Draft: draft-sst-dnsop-probe-name · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-sst-dnsop-probe-name/
page: https://datatracker.ietf.org/doc/draft-sst-dnsop-probe-name/ | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This specification standardizes DNS names that should be used for checking connectivity to a DNS server. About This Document This note is to be removed before publishing as an RFC. Status information for this document may be found at https://datatracker.ietf.org/doc/draft-sst-dnsop-probe-name/. Source for this draft and an issue tracker can be found at https://github.com/bemasc/probe-name.

### Service Binding Mapping for Service Levels
Draft: draft-gakiwate-dnsop-svcb-sla-parameter · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-svcb-sla-parameter/
page: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-svcb-sla-parameter/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-service-binding-mapping-for-service-levels-01 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
This document defines a new SvcParamKey for use in Service Binding (SVCB) and HTTPS DNS resource records which enables authoritative DNS servers to indicate that a service should be used by clients having specific service levels or use types, such as "interactive", "background" or "realtime". By providing this information, clients can make informed decisions about which service endpoints to use based on specific applications needs at that time of making connections.

### DNS SIG(0)
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessa-dns-sig0-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### probe.resolver.arpa
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-dnsop-sessa-proberesolverarpa-00 | video: https://www.youtube.com/watch?v=CbEVXo07KS8 | materials: https://datatracker.ietf.org/meeting/122/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

## Working Group: grow

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-tlv · Working group: grow
Agenda: 15 Paolo Lucente draft-ietf-grow-bmp-tlv
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-sessa-draft-ietf-grow-bmp-tlv-draft-ietf-grow-bmp-rel-draft-ietf-grow-bmp-tlv-ebit-draft-pcmy-grow-bmp-adj-ribs-filtered-00 | video: https://www.youtube.com/watch?v=UNKy2dcgD5E | materials: https://datatracker.ietf.org/meeting/122/session/grow
Most of the BGP Monitoring Protocol (BMP) message types make provision for data in Type, Length, Value (TLV) format. However, Route Monitoring messages (which provide a snapshot of the monitored Routing Information Base) Stats Reports (which supply periodical counters) and Peer Down messages (which indicate that a peering session was terminated) do not. Supporting (optional) data in TLV format across all BMP message types provides consistent and extensible structures that would be useful among the various use- cases where conveying additional data to a monitoring station is required. This document updates RFC 7854 [RFC7854] to support TLV data in all message types and defines some essential TLVs. Additionally, this document introduces support for enterprise- specific TLVs in the BGP Monitoring Protocol by defining an Enterprise Bit (E-bit) that allows usage of per-vendor Type values.

### Logging of routing events in BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-rel · Working group: grow
Agenda: draft-ietf-grow-bmp-rel
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/ | materials: https://datatracker.ietf.org/meeting/122/session/grow
The BGP Monitoring Protocol (BMP) does provide for BGP session event logging (Peer Up, Peer Down), state synchronization (Route Monitoring), debugging (Route Mirroring) and Statistics messages, among others. This document defines a new Route Event Logging (REL) message type for BMP with the aim of covering use cases with affinity to alerting, reporting and on-change analysis.

### Support for Enterprise-specific TLVs in the BGP Monitoring Protocol
Draft: draft-ietf-grow-bmp-tlv-ebit · Working group: grow
Agenda: draft-ietf-grow-bmp-tlv-ebit
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv-ebit/ | materials: https://datatracker.ietf.org/meeting/122/session/grow
Message types defined by the BGP Monitoring Protocol (BMP) do provision for data in TLV - Type, Length, Value - format, either in the shape of a TLV message body, ie. Route Mirroring and Stats Reports, or optional TLVs at the end of a BMP message, ie. Peer Up and Peer Down. However the space for Type value is unique and governed by IANA. To allow the usage of vendor-specific TLVs, a mechanism to define per-vendor Type values is required. In this document we introduce an Enterprise Bit, or E-bit, for such purpose.

### Filtering Adj-Rib-In and Adj-Rib-Out to BMP receivers
Draft: draft-pcmy-grow-bmp-adj-ribs-filtered · Working group: grow
Agenda: draft-pcmy-grow-bmp-adj-ribs-filtered
page: https://datatracker.ietf.org/doc/draft-pcmy-grow-bmp-adj-ribs-filtered/ | materials: https://datatracker.ietf.org/meeting/122/session/grow
Filtering RIBs in BMP (BGP Monitoring Protocol) can be desirable for several use-cases like, for example, limiting the amount of data a collector station has to process or allow a sender to export only a certain afi/safi of interest. This document defines a light way to inform a collector station that a Adj-Rib-In / Adj-Rib-Out data feed is being filtered.

### Advanced BGP Monitoring Protocol (BMP) Statistics Types
Draft: draft-ietf-grow-bmp-bgp-rib-stats · Working group: grow
Agenda: 05 Mukul Srivastava draft-ietf-grow-bmp-bgp-rib-stats
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-bgp-rib-stats/ | materials: https://datatracker.ietf.org/meeting/122/session/grow
RFC 7854 defines different BGP Monitoring Protocol (BMP) statistics message types to observe events that occur on a monitored router. This document defines new statistics type to monitor BMP Adj-RIB-In and Adj-RIB-Out Routing Information Bases (RIBs).

### Common BMP Route-Monitoring Messages for Routes Unchanged by Policy
Draft: draft-patki-grow-bmp-common-updates · Working group: grow
Agenda: 15 Prasad Narasimha draft-patki-grow-bmp-common-updates
page: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-sessa-05-bmp-rib-view-purge-and-common-updates-00 | video: https://www.youtube.com/watch?v=UNKy2dcgD5E | materials: https://datatracker.ietf.org/meeting/122/session/grow
A route unmodified by the inbound policy on a monitored router is included both in Pre-Policy Adj-RIB-In as well as Post-Policy Adj- RIB-In Route-Monitoring messages when both the Pre-Policy and Post- Policy Route-Monitoring modes are enabled. Similarly, a route unmodified by the outbound policy is included in Pre-Policy Adj-RIB- Out as well as Post-Policy Adj-RIB-Out Route-Monitoring messages. This document defines a method to avoid duplicate inclusion of routes unmodified by policy either in Adj-RIB-In or Adj-RIB-Out.

### Support for BMP RIB Purge Notification
Draft: draft-spd-grow-bmp-purge · Working group: grow
Agenda: draft-spd-grow-bmp-purge
page: https://datatracker.ietf.org/doc/draft-spd-grow-bmp-purge/ | materials: https://datatracker.ietf.org/meeting/122/session/grow
This document describes a mechanism to notify a BMP collector of the need to purge the state associated with a RIB view of a specific peer. This is useful, for example, when the BMP sender decides to stop exporting a specific RIB view after providing an initial export. The BMP collector can use the per-peer Purge message to take appropriate action to remove the stale state and avoid holding on to irrelevant network data.

### BMP Loc-RIB: Peer address
Draft: draft-ietf-grow-bmp-loc-peer · Working group: grow
Agenda: 15 Maxence Younsi draft-ietf-grow-bmp-loc-peer
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-loc-peer/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-sessa-bmp-loc-peer-00 | video: https://www.youtube.com/watch?v=UNKy2dcgD5E | materials: https://datatracker.ietf.org/meeting/122/session/grow
BMP Loc-RIB [RFC9069] enforces that the BMP router sets the Peer Address value of a path information to zero. This document introduces the option to communicate the actual peer from which a path was received when advertising that path with BMP Loc-RIB.

### BMP Snapshots
Draft: draft-lucente-grow-bmp-offline · Working group: grow
Agenda: 10 Luuk Hendrinks draft-lucente-grow-bmp-offline
page: https://datatracker.ietf.org/doc/draft-lucente-grow-bmp-offline/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-bmp-state-summaries-draft-lucente-grow-bmp-offline-00 | video: https://www.youtube.com/watch?v=Cdf-11JCs0U | materials: https://datatracker.ietf.org/meeting/122/session/grow
BMP (BGP Monitoring Protocol) is perfectly suited for real-time consumption but less ideal in stream processing and off-wire historical scenarios. The issue is that the necessary information to produce a complete view and enabling correct processing of all messages in the stream, is only sent out at the beginning of the BMP session. This document introduces the concept of BMP Snapshots, enabling BMP stations to synchronize mid-stream, and, providing the basis for self-contained, time-binned archiving of BMP data.

### BGP Operations and Security
Draft: draft-ietf-grow-bgpopsecupd · Working group: grow
Agenda: 10 Tobias Fiebig draft-ietf-grow-bgpopsecupd et al.
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bgpopsecupd/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-draft-ietf-grow-bgpopsecupd-et-al-00 | video: https://www.youtube.com/watch?v=Cdf-11JCs0U | materials: https://datatracker.ietf.org/meeting/122/session/grow
The Border Gateway Protocol (BGP) is a critical component in the Internet to exchange routing information between network domains. It is important to understand the security and reliability requirements that can and should be met to prevent accidental or intentional routing disturbances. Previously, security considerations for BGP have been described in RFC7454 / BCP194. Since the publication of RFC7454, changes in operational practice have taken place, which are partially conflicting with the advice given in RFC7454. This document obsoletes RFC7454, and provides less implementation-specific best practices, with the goal of being less prone to becoming outdated or conflicting with changed operational practices.

### Using BMP over QUIC connection
Draft: draft-liu-grow-bmp-over-quic · Working group: grow
Agenda: 10 Yisong Liu draft-liu-grow-bmp-over-quic-02
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-over-quic/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-using-bmp-over-quic-connection-00 | video: https://www.youtube.com/watch?v=Cdf-11JCs0U | materials: https://datatracker.ietf.org/meeting/122/session/grow
The BGP Monitoring Protocol (BMP) provides a convenient interface for obtaining route views by monitoring BGP sessions. BMP operates over TCP and is unidirectional (from client to server). QUIC provides multiple simultaneous streams to carry data in one direction, enabling much better efficiency and performance for both peers, in particular unidirectional streams can provide reverse data protection for the sender. QUIC also provides shorter handshake and includes TLS. This document describes how to use BMP over the QUIC transport protocol, named BMPoQUIC.

### Source Address Validation Deployment Status
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-source-address-validation-deployment-status-01 | video: https://www.youtube.com/watch?v=Cdf-11JCs0U | materials: https://datatracker.ietf.org/meeting/122/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

### Requirements for Monitoring RPKI-Related Processes on Routers Using BMP
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-grow-requirements-for-monitoring-rpki-related-processes-on-routers-using-bmp-00 | video: https://www.youtube.com/watch?v=Cdf-11JCs0U | materials: https://datatracker.ietf.org/meeting/122/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

## Working Group: httpbis

### QUERY Method
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessa-query-method-00 | video: https://www.youtube.com/watch?v=1oT5rpKmj_s | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessa-resumable-uploads-00 | video: https://www.youtube.com/watch?v=1oT5rpKmj_s | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### CONNECT-TCP
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-connect-tcp-00 | video: https://www.youtube.com/watch?v=1oT5rpKmj_s | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Security Considerations for Optimistic Protocol Transitions in HTTP/1.1
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessa-security-considerations-for-optimistic-protocol-transitions-in-http11-00 | video: https://www.youtube.com/watch?v=1oT5rpKmj_s | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Secondary Certificate Authentication of HTTP Servers
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessa-secondary-certificate-authentication-of-http-servers-00 | video: https://www.youtube.com/watch?v=1oT5rpKmj_s | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Unencoded Digest
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-unencoded-digest-00 | video: https://www.youtube.com/watch?v=1oT5rpKmj_s | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Incremental HTTP Messages
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessb-incremental-http-messages-00 | video: https://www.youtube.com/watch?v=lUlULz14uL4 | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Unencoded Digest
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessb-unencoded-digest-00 | video: https://www.youtube.com/watch?v=lUlULz14uL4 | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP Client Hints Reliability
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-httpbis-sessb-http-client-hints-reliability-01 | video: https://www.youtube.com/watch?v=lUlULz14uL4 | materials: https://datatracker.ietf.org/meeting/122/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

## Working Group: idr

### Guidance for Authors writing text for the BGP Tunnel Encapsulation Attribute
Draft: draft-hares-idr-bess-tea-templates · Working group: idr
Agenda: draft-hares-idr-bess-tea-templates-00
page: https://datatracker.ietf.org/doc/draft-hares-idr-bess-tea-templates/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-01-guidance-for-authors-writing-text-for-the-bgp-tunnel-encapsulation-attribute-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
The BGP (RFC4271) Tunnel Encapsulation Attribute (TEA) is defined in RFC9012. Currently proposed BGP specifications in the IDR and BESS Working groups have defined new tunnels and new parameters for these tunnels in Sub-TLV. The Segment Routing usage of the TEA has suggested a number of new Sub-TLVs. This document provides guidelines to help authors quickly write correct text for new tunnels (defined in tunnel TLVs) and new Sub-TLVs. These guidelines are given as "templates" to aid new authors. More experience authors should view these templates as a list of expected content. One additional challenge for tunnels using the PMSI tunnels is to carefully define the interaction between PMSI tunnels and TEA tunnels.

### BGP Link Bandwidth Extended Community
Draft: draft-ietf-idr-link-bandwidth · Working group: idr
Agenda: draft-ietf-idr-link-bandwidth-11
page: https://datatracker.ietf.org/doc/draft-ietf-idr-link-bandwidth/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-02-bgp-link-bandwidth-extended-community-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
This document defines a BGP Extended Community, the Link Bandwidth Extended Community, which carries bandwidth information to enable weighted load-balancing in multipath scenarios. It specifies the format and processing rules for this extended community type.

### BGP SR Policy Extensions for Path Scheduling
Draft: draft-zzd-idr-sr-policy-scheduling · Working group: idr
Agenda: draft-zzd-idr-sr-policy-scheduling-08
page: https://datatracker.ietf.org/doc/draft-zzd-idr-sr-policy-scheduling/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-03-bgp-sr-policy-extensions-for-path-scheduling-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
Segment Routing (SR) policy enables instantiation of an ordered list of segments with a specific intent for traffic steering. When using SR policy in a a network with time-variant characterics or requires high resources utilization efficiency, delivering the time-variant information associated with paths is necessary. This document proposes extensions to BGP SR Policy to deliver the schedule time information of candidate paths and segment lists.

### SRv6 Policy SID List Optimization Advertisement
Draft: draft-ali-idr-srv6-policy-sl-opt-distribution · Working group: idr
Agenda: draft-ali-idr-srv6-policy-sl-opt-distribution-00
page: https://datatracker.ietf.org/doc/draft-ali-idr-srv6-policy-sl-opt-distribution/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-04-srv6-policy-sid-list-optimization-advertisement-01 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
In some use cases, an SRv6 policy's SID list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This draft specifies a BGP-LS extension to indicate whether the endpoint's node SID is included or excluded in installing SID list(s) of the Candidate Path (CP) of an SRv6 policy.

### BGP SR Policy Extensions for Administrative Flags
Draft: draft-lin-idr-sr-policy-admin-flags · Working group: idr
Agenda: draft-lin-idr-sr-policy-admin-flags-01
page: https://datatracker.ietf.org/doc/draft-lin-idr-sr-policy-admin-flags/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-05-bgp-sr-policy-extensions-for-administrative-flags-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
Segment Routing is a source routing paradigm that explicitly indicates the forwarding path for packets at the ingress node. An SR Policy is a set of candidate paths, each consisting of one or more segment lists. This document defines an extension to the BGP SR Policy that sets the administrative state of the candidate path or segment list, facilitating the operation and maintenance of the SR Policy.

### BGP Flow Specification Version 2 - for Basic IP
Draft: draft-ietf-idr-fsv2-ip-basic · Working group: idr
Agenda: draft-ietf-idr-fsv2-ip-basic-03
page: https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-06-bgp-flow-specification-version-2-01 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC 8956, and RFC 9117, describes the distribution of traffic filter policy (traffic filters and actions) distributed via BGP. During the deployment of BGP FSv1 a number of issues were detected, so version 2 of the BGP flow specification (FSv2) protocol addresses these issues. In order to provide a clear demarcation between FSv1 and FSv2, a different NLRI encapsulates FSv2. The IDR WG requires two implementation. Early feedback on implementations of FSv2 indicate that FSv2 has a correct design direction, but that breaking FSv2 into a progression of documents would aid deployment of the draft (basic and adding user ordered actions). This document specifies the basic FSv2 NLRI with user ordering of filters added to FSv1 IP Filters and FSv2 actions.

### BGP Flowspec for Computing-Aware Traffic Steering
Draft: draft-lin-idr-cats-flowspec-ts · Working group: idr
Agenda: draft-lin-idr-cats-flowspec-ts-01
page: https://datatracker.ietf.org/doc/draft-lin-idr-cats-flowspec-ts/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-07-bgp-flowspec-for-computing-aware-traffic-steering-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
A BGP Flow Specification is an n-tuple consisting of several matching criteria that can be applied to IP traffic. Computing-Aware Traffic Steering (CATS) is a framework which optimizes traffic steering to a given service instance by taking into account the dynamic nature of both computing and network resources. This document specifies a new BGP Flow Spec Component Type in order to support CATS traffic forwarding.

### A profile for FC path attribute
Draft: draft-wang-idr-fc-path-attribute · Working group: idr
Agenda: draft-wang-idr-fc-path-attribute-00
page: https://datatracker.ietf.org/doc/draft-wang-idr-fc-path-attribute/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-08-a-profile-for-fc-path-attribute-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
This document specifies a mechanism for embedding a new path attribute, known as the FC path attribute, into BGP UPDATE messages. The FC (Forwarding Commitment) is a cryptographically signed object to certify an AS's routing intent on its directly connected hops. By incorporating the FC path attribute into BGP UPDATE messages. This mechanism provides enhanced route authenticity and lays the groundwork for improved data-plane forwarding verification. This mechanism is backward compatible, which means a router that supports the attribute can interoperate with a router that doesn't, allowing partial deployment across the Internet.

### Connecting IPv4 Islands over IPv6 Core using IPv4 Provider Edge Routers (4PE)
Draft: draft-mishra-idr-v4-islands-v6-core-4pe · Working group: idr
Agenda: draft-mishra-idr-v4-islands-v6-core-4pe-09
page: https://datatracker.ietf.org/doc/draft-mishra-idr-v4-islands-v6-core-4pe/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-09-connecting-ipv4-islands-over-ipv6-core-using-ipv4-provider-edge-routers-4pe-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
As operators migrate from an IPv4 core to an IPv6 core for global table routing over the internet, the need arises to be able provide routing connectivity for customers IPv4 only networks. This document provides a solution called 4Provider Edge, "4PE" that connects IPv4 islands over an IPv6-Only network.

### Dynamic Capability for BGP-4
Draft: draft-ietf-idr-dynamic-cap · Working group: idr
Agenda: draft-ietf-idr-dynamic-cap-16
page: https://datatracker.ietf.org/doc/draft-ietf-idr-dynamic-cap/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessb-3-dynamic-capability-for-bgp-4-00 | video: https://www.youtube.com/watch?v=UkLOWYrUBHQ | materials: https://datatracker.ietf.org/meeting/122/session/idr
This document defines a new BGP capability termed "Dynamic Capability", which would allow the dynamic update of capabilities over an established BGP session. This capability would facilitate non-disruptive capability changes by BGP speakers.

### BGP Extension for SRv6 Policy Segment List optimization
Draft: draft-liu-idr-sr-segment-list-optimize · Working group: idr
Agenda: draft-liu-idr-sr-segment-list-optimize-01
page: https://datatracker.ietf.org/doc/draft-liu-idr-sr-segment-list-optimize/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-srv6-segment-list-optimization-01 | video: https://www.youtube.com/watch?v=UkLOWYrUBHQ | materials: https://datatracker.ietf.org/meeting/122/session/idr
In some use cases, an SRv6 policy's segment list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This document specifies a BGP extension to indicate whether the endpoint's node SID needs to be included or excluded when installing the SRv6 Policy. This optimization can improve the forwarding efficiency of data packets when End SID and Service SID are present.

### BGP-Link State (BGP-LS) Advertisement of Flow Queue
Draft: draft-li-idr-bgpls-flow-queue · Working group: idr
Agenda: draft-li-idr-bgpls-flow-queue-00
page: https://datatracker.ietf.org/doc/draft-li-idr-bgpls-flow-queue/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessb-5-bgp-link-state-bgp-ls-advertisement-of-flow-queue-00 | video: https://www.youtube.com/watch?v=UkLOWYrUBHQ | materials: https://datatracker.ietf.org/meeting/122/session/idr
In the traffic congestion management of routers, queueing technology is generally used to classify and transmit traffic. Therefore, queue information indirectly reflects the congestion status of the router. This document makes the necessary expansion of the BGP-LS mechanism to send queue information to the network controller in a scalable way, enabling the network controller to understand the router's traffic congestion status and make appropriate adjustments to the network traffic.

### 2-Jeff’s Commentary on FC-BGP Attribute
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessa-08-2-jeffs-commentary-on-fc-bgp-attribute-00 | video: https://www.youtube.com/watch?v=SqZIL7TDQIk | materials: https://datatracker.ietf.org/meeting/122/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### BGP Flowspec for Computing-Aware Traffic Steering
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessb-1-bgp-flowspec-for-computing-aware-traffic-steering-00 | video: https://www.youtube.com/watch?v=UkLOWYrUBHQ | materials: https://datatracker.ietf.org/meeting/122/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### Connecting IPv4 Islands over IPv6 Core using IPv4 Provider Edge Routers (4PE)
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-idr-sessb-2-connecting-ipv4-islands-over-ipv6-core-using-ipv4-provider-edge-routers-4pe-00 | video: https://www.youtube.com/watch?v=UkLOWYrUBHQ | materials: https://datatracker.ietf.org/meeting/122/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

## Working Group: ipsecme

### Enhanced Encapsulating Security Payload (EESP)
Draft: draft-klassert-ipsecme-eesp · Working group: ipsecme
Agenda: draft-klassert-ipsecme-eesp
page: https://datatracker.ietf.org/doc/draft-klassert-ipsecme-eesp/ | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document describes the Enhanced Encapsulating Security Payload (EESP) protocol, which builds on the existing IP Encapsulating Security Payload (ESP) protocol. It is designed to modernize and overcome limitations in the ESP protocol. EESP adds Session IDs (e.g., to support CPU pinning), changes some previously mandatory fields to optional, and moves the ESP trailer into the EESP header. Additionally, EESP adds header options adapted from IPv6 to allow for future extension. New header options are defined which add Flow IDs (e.g., for CPU pinning and QoS support), and a crypt-offset to allow for exposing inner flow information for middlebox use.

### IKEv2 negotiation for Enhanced Encapsulating Security Payload (EESP)
Draft: draft-klassert-ipsecme-eesp-ikev2 · Working group: ipsecme
Agenda: draft-klassert-ipsecme-eesp-ikev2
page: https://datatracker.ietf.org/doc/draft-klassert-ipsecme-eesp-ikev2/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-ikev2-negotiation-for-eesp-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document specfies how to negotiate the use of the Enhanced Encapsulating Security Payload (EESP) protocol using the Internet Key Exchange protocol version 2 (IKEv2). The EESP protocol, which is defined in draft-klassert-ipsecme-eesp, provides the same security services as Encapsulating Security Payload (ESP), but has richer functionality and provides better performance in specific circumstances. This document specifies negotiation of version 0 of EESP.

### Use of Variable-Length Output Preudo-Random Functions (PRFs) in the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-smyslov-ipsecme-ikev2-prf-plus · Working group: ipsecme
Agenda: draft-smyslov-ipsecme-ikev2-prf-plus
page: https://datatracker.ietf.org/doc/draft-smyslov-ipsecme-ikev2-prf-plus/ | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document specifies the use of variable-length output Preudo- Random Functions (PRFs) in the Internet Key Exchange Protocol Version 2 (IKEv2). Current IKEv2 specification relies on traditional PRFs with fixed output length for key derivation and uses iterative application of a PRF (called "prf+") in cases when longer output is required. Appearance of PRFs that can output as much bits as requested allows to streamline the key derivation functions of IKEv2. This document updates RFCs 5723, 6617, 6631, 7296, 8784, 9370 for the cases when variable-length output Preudo-Random Functions are used in IKEv2 and its extensions.

### Optimized Rekeys in the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt · Working group: ipsecme
Agenda: draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt/ | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document describes a method for reducing the size of the Internet Key Exchange version 2 (IKEv2) CREATE_CHILD_SA exchanges used for rekeying of the IKE or Child SA by replacing the SA and TS payloads with a Notify Message payload. Reducing size and complexity of IKEv2 exchanges is especially useful for low power consumption battery powered devices.

### IKEv2 Support for Child SA PFS Policy Information
Draft: draft-pwouters-ipsecme-child-pfs-info · Working group: ipsecme
Agenda: draft-pwouters-ipsecme-child-pfs-info
page: https://datatracker.ietf.org/doc/draft-pwouters-ipsecme-child-pfs-info/ | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document defines an extension for the Internet Key Exchange Protocol Version 2 (IKEv2) to support negotiation at the time of initial Child Security Association (SA) establishing of Key Exchange (KE) method that could be used in subsequent rekeys of this SA.

### IKEv2 support for specifying a Delete notify reason
Draft: draft-pwouters-ipsecme-delete-info · Working group: ipsecme
Agenda: draft-pwouters-ipsecme-delete-info
page: https://datatracker.ietf.org/doc/draft-pwouters-ipsecme-delete-info/ | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document defines the DELETE_REASON Notify Message Status Type Payload for the Internet Key Exchange Protocol Version 2 (IKEv2) to support adding a reason for the deletion of the IKE or Child SA(s).

### Post-quantum Hybrid Key Exchange in IKEv2 with FrodoKEM
Draft: draft-wang-ipsecme-hybrid-kem-ikev2-frodo · Working group: ipsecme
Agenda: draft-wang-ipsecme-hybrid-kem-ikev2-frodo
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-hybrid-kem-ikev2-frodo/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-post-quantum-hybrid-key-exchange-in-the-ikev2-with-frodokem-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
Multiple key exchanges in the Internet Key Exchange Protocol Version 2 (IKEv2) [RFC9370] specifies a framework, which supports multiple key encapsulation mechanisms (KEMs) in IKEv2 by allowing up to 7 layers of additional KEMs to derive the final shared secret keys for IPsec protocols. The primary goal is to mitigate the “harvest now and decrypt later” threat posed by Cryptographically Relevant Quantum Computers(CRQCs). For this purpose, one or more post-quantum KEMs are usually performed in addition to the traditional (EC)DH key exchange. This draft specifies how the post-quantum KEM algorithm FrodoKEM is instantiated for IKEv2 as an additional key exchange mechanism. [EDNOTE: IANA KE code points for FrodoKEM may need to be assigned, as the code points for ML-KEM has been considered in [W-D.K25]. ]

### KEM-based Authentication for IKEv2 with Post-quantum Security
Draft: draft-wang-ipsecme-kem-auth-ikev2 · Working group: ipsecme
Agenda: draft-wang-ipsecme-kem-auth-ikev2
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-kem-auth-ikev2/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-kem-based-authentication-for-the-ikev2-with-post-quantum-security-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This draft specifies a new authentication mechanism, called KEM (Key Encapsulation Mechanism) -based authentication, for the Internet Key Exchange Protocol Version 2 (IKEv2). This is motivated by the fact that some post-quantum KEMs (like ML-KEM) are more efficient than post-quantum signature algorithms (like ML-DSA).

### Post-quantum Hybrid Key Exchange with ML-KEM in the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-kampanakis-ml-kem-ikev2 · Working group: ipsecme
Agenda: draft-kampanakis-ml-kem-ikev2
page: https://datatracker.ietf.org/doc/draft-kampanakis-ml-kem-ikev2/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-ml-kem-ikev2-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
NIST recently standardized ML-KEM, a new key encapsulation mechanism, which can be used for quantum-resistant key establishment. This draft specifies how to use ML-KEM as an additional key exchange in IKEv2 along with traditional key exchanges. This Post-Quantum Traditional Hybrid Key Encapsulation Mechanism approach allows for negotiating IKE and Child SA keys which are safe against cryptanalytically-relevant quantum computers and theoretical weaknesses in ML-KEM.

### Lightweight Authentication Methods for IP Header
Draft: draft-dunbar-ipsecme-ligthtweight-authenticate · Working group: ipsecme
Agenda: draft-dunbar-ipsecme-ligthtweight-authenticate
page: https://datatracker.ietf.org/doc/draft-dunbar-ipsecme-ligthtweight-authenticate/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-lightweight-authentication-methods-for-ip-encapsulation-header-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
This document describes lightweight authentication methods to prevent malicious actors tampering with the IP encapsulation headers or metadata carried by the UPD Option Header.

### Enhanced ESP (slides-122-ipsecme-enhanced-esp)
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-enhanced-esp-slides-122-ipsecme-enhanced-esp-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Use of Variable-Length Output PRFs in IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-use-of-variable-length-output-prfs-in-ikev2-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Optimized Rekey in the IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-optimized-rekey-in-the-ikev2-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Delete Reasons & Initial Child PFS
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-ipsecme-delete-reasons-initial-child-pfs-00 | video: https://www.youtube.com/watch?v=zzw8Y5IltUI | materials: https://datatracker.ietf.org/meeting/122/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

## Working Group: jose

### Fully-Specified Algorithms for JOSE and COSE
Draft: draft-ietf-jose-fully-specified-algorithms · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-fully-specified-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-fully-specified-algorithms/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-jose-fully-specified-algorithms-for-jose-and-cose-00 | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
This specification refers to cryptographic algorithm identifiers that fully specify the cryptographic operations to be performed, including any curve, key derivation function (KDF), and hash functions, as being "fully specified". It refers to cryptographic algorithm identifiers that require additional information beyond the algorithm identifier to determine the cryptographic operations to be performed as being "polymorphic". This specification creates fully-specified algorithm identifiers for registered JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) polymorphic algorithm identifiers, enabling applications to use only fully-specified algorithm identifiers. It deprecates those polymorphic algorithm identifiers. This specification updates RFC 7518, RFC 8037, and RFC 9053. It deprecates polymorphic algorithms defined by RFC 8037 and RFC 9053 and provides fully-specified replacements for them. It adds to the instructions to designated experts in RFC 7518 and RFC 9053.

### Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)
Draft: draft-ietf-jose-hpke-encrypt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/ | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
This specification defines how to use Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE). HPKE enables public key encryption of arbitrary-sized plaintexts to a recipient's public key, and provides security against adaptive chosen ciphertext attacks. This specification chooses a specific subset of the HPKE features to use with JWE. This specification updates RFC 7516 (JWE) to enable use of Integrated Encryption as a Key Management Mode.

### JSON Web Proof
Draft: draft-ietf-jose-json-web-proof · Working group: jose
Agenda: JSON Web Proofs https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-jose-json-web-proofs-specifications-00 | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
The JOSE set of standards established JSON-based container formats for Keys, Signatures, and Encryption. They also established IANA registries to enable the algorithms and representations used for them to be extended. Since those were created, newer cryptographic algorithms that support selective disclosure and unlinkability have matured and started seeing early market adoption. The COSE set of standards likewise does this for CBOR-based containers, focusing on the needs of environments which are better served using CBOR, such as constrained devices and networks. This document defines a new container format similar in purpose and design to JSON Web Signature (JWS) and COSE Signed Messages called a _JSON Web Proof (JWP)_. Unlike JWS, which integrity-protects only a single payload, JWP can integrity-protect multiple payloads in one message. It also specifies a new presentation form that supports selective disclosure of individual payloads, enables additional proof computation, and adds a Presentation Header to prevent replay.

### JSON Proof Algorithms
Draft: draft-ietf-jose-json-proof-algorithms · Working group: jose
Agenda: JSON Proof Algorithms https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/ | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
The JSON Proof Algorithms (JPA) specification registers cryptographic algorithms and identifiers to be used with the JSON Web Proof, JSON Web Key (JWK), and COSE specifications. It defines IANA registries for these identifiers.

### JSON Proof Token and CBOR Proof Token
Draft: draft-ietf-jose-json-proof-token · Working group: jose
Agenda: JSON Proof Token https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/ | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving representation of claims to be transferred between three parties. The claims in a JPT are encoded as base64url-encoded JSON objects that are used as the payloads of a JSON Web Proof (JWP) structure, enabling them to be digitally signed and selectively disclosed. JPTs also support reusability and unlinkability when using Zero-Knowledge Proofs (ZKPs). A CBOR-based representation of JPTs is also defined, called a CBOR Proof Token (CPT). It has the same properties as JPTs, but uses the JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based JWP Compact Serialization.

### JOSE: Deprecate 'none' and 'RSA1_5'
Draft: draft-ietf-jose-deprecate-none-rsa15 · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-jose-deprecate-none-rsa-00 | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
This document updates RFC 7518 to deprecate the JWS algorithm "none" and the JWE algorithm "RSA1_5". These algorithms have known security weaknesses. It also updates the Review Instructions for Designated Experts to establish baseline security requirements that future algorithm registrations are expected to meet.

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE
Draft: draft-ietf-jose-pqc-kem · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/ | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
This document describes conventions for using Post-Quantum Key Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and Encryption (COSE).

### Enhanced JWE Security with Detached Additional Authenticated Data (AAD)
Draft: draft-reddy-jose-detached-aad · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-reddy-jose-detached-aad/
page: https://datatracker.ietf.org/doc/draft-reddy-jose-detached-aad/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-jose-enhanced-jwe-security-with-detached-aad-00 | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
This draft introduces a mechanism to support detached Additional Authenticated Data (AAD) in JWE (JSON Web Encryption), allowing the AAD to be derived from context-specific information, such as session identifiers, algorithm identifiers, and identifiers of communication endpoints, rather than being transmitted in-band. This mechanism strengthens security by mitigating risk against unknown-key-share attacks and/or other exploitation techniques that depend on some type of confusion over the role played by each party. The document explains how to integrate this functionality into JWE, covering both JWE JSON Serialization and JWE Compact Serialization.

### Post-Quantum and Hybrid KEMs for HPKE with JOSE and COSE
Draft: draft-reddy-cose-jose-pqc-hybrid-hpke · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-reddy-cose-jose-pqc-hybrid-hpke/
page: https://datatracker.ietf.org/doc/draft-reddy-cose-jose-pqc-hybrid-hpke/ | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
This document specifies the use of Post-Quantum (PQC) and Post- Quantum/Traditional (PQ/T) Hybrid Key Encapsulation Mechanisms (KEMs) within the Hybrid Public Key Encryption (HPKE) for JOSE and COSE. It defines algorithm identifiers and key formats to support pure post- quantum algorithms (ML-KEM) and their PQ/T hybrid combinations.

### Use of HPKE with JOSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-jose-use-of-hpke-with-jose-00 | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### Modern Algorithms in the Web Cryptography API
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-jose-modern-algorithms-in-the-web-cryptography-api-00 | video: https://www.youtube.com/watch?v=YN1yuGjQQ-k | materials: https://datatracker.ietf.org/meeting/122/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

## Working Group: lamps

### Use of the RSA-KEM Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-rfc5990bis · Working group: lamps
Agenda: a) draft-ietf-lamps-rfc5990bis ( RFC 9690 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5990bis/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-use-of-the-ml-dsa-signature-algorithm-in-the-cryptographic-message-syntax-cms-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
The RSA Key Encapsulation Mechanism (RSA-KEM) Algorithm is a one-pass (store-and-forward) cryptographic mechanism for an originator to securely send keying material to a recipient using the recipient's RSA public key. The RSA-KEM Algorithm is specified in Clause 11.5 of ISO/IEC: 18033-2:2006. This document specifies the conventions for using the RSA-KEM Algorithm as a standalone KEM algorithm and the conventions for using the RSA-KEM Algorithm with the Cryptographic Message Syntax (CMS) using KEMRecipientInfo as specified in RFC XXXX. This document obsoletes RFC 5990. RFC EDITOR: Please replace XXXX with the RFC number assigned to draft-ietf-lamps-cms-kemri.

### Use of the SHA3 One-way Hash Functions in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-sha3-hash · Working group: lamps
Agenda: b) draft-ietf-lamps-cms-sha3-hash ( RFC 9688 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-sha3-hash/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document describes the conventions for using the one-way hash functions in the SHA3 family with the Cryptographic Message Syntax (CMS). The SHA3 family can be used as a message digest algorithm, as part of a signature algorithm, as part of a message authentication code, or part of a key derivation function.

### Encryption Key Derivation in the Cryptographic Message Syntax (CMS) using HKDF with SHA-256
Draft: draft-ietf-lamps-cms-cek-hkdf-sha256 · Working group: lamps
Agenda: c) draft-ietf-lamps-cms-cek-hkdf-sha256 ( RFC 9709 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-cek-hkdf-sha256/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document specifies the derivation of the content-encryption key or the content-authenticated-encryption key in the Cryptographic Message Syntax (CMS) using HMAC-based Extract-and-Expand Key Derivation Function (HKDF) with SHA-256. The use of this mechanism provides protection against where the attacker manipulates the content-encryption algorithm identifier or the content-authenticated- encryption algorithm identifier.

### Use of the HSS/LMS Hash-Based Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-rfc8708bis · Working group: lamps
Agenda: d) draft-ietf-lamps-rfc8708bis ( RFC 9708 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc8708bis/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document specifies the conventions for using the Hierarchical Signature System (HSS) / Leighton-Micali Signature (LMS) hash-based signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided. The HSS/LMS algorithm is one form of hash-based digital signature; it is described in RFC 8554. This document obsoletes RFC 8708.

### X.509 Certificate Extended Key Usage (EKU) for Instant Messaging URIs
Draft: draft-ietf-lamps-im-keyusage · Working group: lamps
Agenda: e) draft-ietf-lamps-im-keyusage ( RFC 9734 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-im-keyusage/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
RFC 5280 specifies several extended key purpose identifiers (KeyPurposeIds) for X.509 certificates. This document defines Instant Messaging (IM) identity KeyPurposeId for inclusion in the Extended Key Usage (EKU) extension of X.509 v3 public key certificates

### Guidance on End-to-End E-mail Security
Draft: draft-ietf-lamps-e2e-mail-guidance · Working group: lamps
Agenda: a) draft-ietf-lamps-e2e-mail-guidance (DKG)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-e2e-mail-guidance/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
End-to-end cryptographic protections for e-mail messages can provide useful security. However, the standards for providing cryptographic protection are extremely flexible. That flexibility can trap users and cause surprising failures. This document offers guidance for mail user agent implementers to help mitigate those risks, and to make end-to-end e-mail simple and secure for the end user. It provides a useful set of vocabulary as well as recommendations to avoid common failures. It also identifies a number of currently unsolved usability and interoperability problems.

### Updates to Lightweight OCSP Profile for High Volume Environments
Draft: draft-ietf-lamps-rfc5019bis · Working group: lamps
Agenda: b) draft-ietf-lamps-rfc5019bis (Tadahiko)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5019bis/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This specification defines a profile of the Online Certificate Status Protocol (OCSP) that addresses the scalability issues inherent when using OCSP in large scale (high volume) Public Key Infrastructure (PKI) environments and/or in PKI environments that require a lightweight solution to minimize communication bandwidth and client- side processing. This specification obsoletes RFC 5019. The profile specified in RFC 5019 has been updated to allow and recommend the use of SHA-256 over SHA-1.

### Related Certificates for Use in Multiple Authentications within a Protocol
Draft: draft-ietf-lamps-cert-binding-for-multi-auth · Working group: lamps
Agenda: c) draft-ietf-lamps-cert-binding-for-multi-auth
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cert-binding-for-multi-auth/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document defines a new CSR attribute, relatedCertRequest, and a new X.509 certificate extension, RelatedCertificate. The use of the relatedCertRequest attribute in a CSR and the inclusion of the RelatedCertificate extension in the resulting certificate together provide additional assurance that two certificates each belong to the same end entity. This mechanism is particularly useful in the context of non-composite hybrid authentication, which enables users to employ the same certificates in hybrid authentication as in authentication done with only traditional or post-quantum algorithms.

### Header Protection for Cryptographically Protected E-mail
Draft: draft-ietf-lamps-header-protection · Working group: lamps
Agenda: d) draft-ietf-lamps-header-protection
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-header-protection/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
S/MIME version 3.1 introduced a mechanism to provide end-to-end cryptographic protection of e-mail message headers. However, few implementations generate messages using this mechanism, and several legacy implementations have revealed rendering or security issues when handling such a message. This document updates the S/MIME specification (RFC8551) to offer a different mechanism that provides the same cryptographic protections but with fewer downsides when handled by legacy clients. Furthermore, it offers more explicit usability, privacy, and security guidance for clients when generating or handling e-mail messages with cryptographic protection of message headers. The Header Protection scheme defined here is also applicable to messages with PGP/MIME cryptographic protections.

### Use of the HSS and XMSS Hash-Based Signature Algorithms in Internet X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-x509-shbs · Working group: lamps
Agenda: f) draft-ietf-lamps-x509-shbs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-shbs/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document specifies algorithm identifiers and ASN.1 encoding formats for the stateful hash-based signature (HBS) schemes Hierarchical Signature System (HSS), eXtended Merkle Signature Scheme (XMSS), and XMSS^MT, a multi-tree variant of XMSS. This specification applies to the Internet X.509 Public Key infrastructure (PKI) when those digital signatures are used in Internet X.509 certificates and certificate revocation lists.

### Internet X.509 Public Key Infrastructure -- Certificate Management Protocol (CMP)
Draft: draft-ietf-lamps-rfc4210bis · Working group: lamps
Agenda: g) draft-ietf-lamps-rfc4210bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc4210bis/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document describes the Internet X.509 Public Key Infrastructure (PKI) Certificate Management Protocol (CMP). Protocol messages are defined for X.509v3 certificate creation and management. CMP provides interactions between client systems and PKI components such as a Registration Authority (RA) and a Certification Authority (CA). This document adds support for management of certificates containing a Key Encapsulation Mechanism (KEM) public key and use EnvelopedData instead of EncryptedValue. This document also includes the updates specified in Section 2 and Appendix A.2 of RFC 9480. The updates maintain backward compatibility with CMP version 2 wherever possible. Updates to CMP version 2 are improving crypto agility, extending the polling mechanism, adding new general message types, and adding extended key usages to identify special CMP server authorizations. CMP version 3 is introduced for changes to the ASN.1 syntax, which are support of EnvelopedData, certConf with hashAlg, POPOPrivKey with agreeMAC, and RootCaKeyUpdateContent in ckuann messages. This document obsoletes RFC 4210 and together with I-D.ietf-lamps- rfc6712bis and it also obsoletes RFC 9480. Appendix F of this document updates the Section 9 of RFC 5912.

### Internet X.509 Public Key Infrastructure -- HTTP Transfer for the Certificate Management Protocol (CMP)
Draft: draft-ietf-lamps-rfc6712bis · Working group: lamps
Agenda: h) draft-ietf-lamps-rfc6712bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6712bis/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document describes how to layer the Certificate Management Protocol (CMP) over HTTP. It includes the updates to RFC 6712 specified in RFC 9480 Section 3. These updates introduce CMP URIs using a Well-known prefix. It obsoletes RFC 6712 and together with I-D.ietf-lamps-rfc4210bis and it also obsoletes RFC 9480.

### Clarification and enhancement of RFC7030 CSR Attributes definition
Draft: draft-ietf-lamps-rfc7030-csrattrs · Working group: lamps
Agenda: a) draft-ietf-lamps-rfc7030-csrattrs (Michael)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc7030-csrattrs/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document updates RFC7030, Enrollment over Secure Transport (EST), clarifying how the Certificate Signiing Request (CSR) Attributes Response can be used by an EST server to specify both CSR attribute Object IDs (OID) and also CSR attribute values, in particular X.509 extension values, that the server expects the client to include in subsequent CSR request. RFC9148 is derived from RFC7030, and it is also updated. RFC7030 (EST) is ambiguous in its specification of the CSR Attributes Response. This has resulted in implementation challenges and implementor confusion. As a result, there was not universal understanding of what was specified. This document clarifies the encoding rules. This document therefore also provides a new straightforward approach: using a template for CSR contents that may be partially filled in by the server. This also allows an EST server to specify a subject Distinguished Name (DN).

### Use of Password-Based Message Authentication Code 1 (PBMAC1) in PKCS #12 Syntax
Draft: draft-ietf-lamps-rfc9579bis · Working group: lamps
Agenda: b) draft-ietf-lamps-rfc9579bis (Alicja)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc9579bis/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document specifies additions and amendments to RFCs 7292 and 8018. It also obsoletes the RFC 9579. It defines a way to use the Password-Based Message Authentication Code 1 (PBMAC1), defined in RFC 8018, inside the PKCS #12 syntax. The purpose of this specification is to permit the use of more modern Password-Based Key Derivation Functions (PBKDFs) and allow for regulatory compliance.

### Use of the SLH-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-sphincs-plus · Working group: lamps
Agenda: c) draft-ietf-lamps-cms-sphincs-plus (Russ, Scott, Panos, Bas)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-sphincs-plus/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
SLH-DSA is a stateless hash-based signature scheme. This document specifies the conventions for using the SLH-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA)
Draft: draft-ietf-lamps-dilithium-certificates · Working group: lamps
Agenda: a) draft-ietf-lamps-dilithium-certificates (Jake, Panos, Sean, Bas)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Digital signatures are used within X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using FIPS 204, the Module-Lattice- Based Digital Signature Algorithm (ML-DSA) in Internet X.509 certificates and certificate revocation lists. The conventions for the associated signatures, subject public keys, and private key are also described.

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)
Draft: draft-ietf-lamps-kyber-certificates · Working group: lamps
Agenda: b) draft-ietf-lamps-kyber-certificates (Sean, Panos, Jake, Bas)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). This document specifies the conventions for using the ML-KEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Use of Remote Attestation with Certification Signing Requests
Draft: draft-ietf-lamps-csr-attestation · Working group: lamps
Agenda: c) draft-ietf-lamps-csr-attestation (Mike)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Certification Authorities (CAs) issuing certificates to Public Key Infrastructure (PKI) end entities may require a certificate signing request (CSR) to include additional verifiable information to confirm policy compliance. For example, a CA may require an end entity to demonstrate that the private key corresponding to a CSR's public key is secured by a hardware security module (HSM), is not exportable, etc. The process of generating, transmitting, and verifying additional information required by the CA is called remote attestation. While work is currently underway to standardize various aspects of remote attestation, a variety of proprietary mechanisms have been in use for years, particularly regarding protection of private keys. This specification defines ASN.1 structures which may carry attestation data for PKCS#10 and Certificate Request Message Format (CRMF) messages. Both standardized and proprietary attestation formats are supported by this specification.

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for SLH-DSA
Draft: draft-ietf-lamps-x509-slhdsa · Working group: lamps
Agenda: d) draft-ietf-lamps-x509-slhdsa (Kaveh, Scott, Stefan-Lukas, Daniel, Stavros)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-slhdsa/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-internet-x509-public-key-infrastructure-algorithm-identifiers-for-slh-dsa-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Digital signatures are used within X.509 Public Key Infrastructure such as X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using the Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) in X.509 Public Key Infrastructure. The conventions for the associated signatures, subject public keys, and private keys are also specified.

### Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests
Draft: draft-ietf-lamps-attestation-freshness · Working group: lamps
Agenda: e) draft-ietf-lamps-attestation-freshness (Hannes, Hendrik)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
When an end entity includes attestation statements in a Certificate Signing Request (CSR), the freshness of the conveyed Evidence often needs to be established. A common mechanism is a nonce that is obtained from a Relying Party or Verifier and included by the Attester in the Evidence. This document specifies how an end entity requests such an attestation freshness nonce from an RA/CA when using certificate lifecycle management protocols. It defines message formats and protocol bindings for the conveyance of nonce request and response messages in the Certificate Management Protocol (CMP), Enrollment over Secure Transport (EST), and Certificate Management over CMS (CMC), including optional type-specific information needed to produce fresh Evidence for inclusion in a CSR.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-sigs · Working group: lamps
Agenda: f) draft-ietf-lamps-pq-composite-sigs (Mike, John, Max, Jan, Scott)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document defines combinations of US NIST Module-Lattice-Based Digital Signature Algorithm (ML-DSA) in hybrid with traditional algorithms RSASSA-PKCS1-v1.5, RSASSA-PSS, ECDSA, Ed25519, and Ed448. These combinations are tailored to meet regulatory guidelines in certain regions. Composite ML-DSA is applicable in applications that use X.509 or PKIX data structures that accept ML-DSA, but where the operator wants extra protection against breaks or catastrophic bugs in ML-DSA, and where existential unforgeability (EUF-CMA) level security is acceptable.

### An Attribute for Statement of Possession of a Private Key
Draft: draft-ietf-lamps-private-key-stmt-attr · Working group: lamps
Agenda: h) draft-ietf-lamps-private-key-stmt-attr
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-private-key-stmt-attr/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-draft-ietf-lamps-private-key-stmt-attr-00-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document specifies an attribute for a statement of possession of a private key by a certificate subject. As part of X.509 certificate enrollment, a Certification Authority (CA) typically demands proof that the subject possesses the private key that corresponds to the to-be-certified public key. In some cases, a CA might accept a signed statement from the certificate subject. For example, when a certificate subject needs separate certificates for signature and key establishment, a statement that can be validated with the previously issued signature certificate for the same subject might be adequate for subsequent issuance of the key establishment certificate.

### Unsigned X.509 Certificates
Draft: draft-ietf-lamps-x509-alg-none · Working group: lamps
Agenda: i) draft-ietf-lamps-x509-alg-none
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-alg-none/ | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document defines a placeholder X.509 signature algorithm that may be used in contexts where the consumer of the certificate is not expected to verify the signature. As part of this, it updates RFC 5280.

### Use of ML-KEM in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-kyber · Working group: lamps
Agenda: a) draft-ietf-lamps-cms-kyber (Ludovic, Julien, Mike)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-kyber/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-use-of-ml-kem-in-the-cryptographic-message-syntax-cms-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). Three parameter sets for the ML-KEM algorithm are specified by the US National Institute of Standards and Technology (NIST) in FIPS 203. In order of increasing security strength (and decreasing performance), these parameter sets are ML-KEM-512, ML-KEM-768, and ML-KEM-1024. This document specifies the conventions for using ML-KEM with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in "Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" (RFC 9629).

### Composite ML-KEM for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-kem · Working group: lamps
Agenda: b) draft-ietf-lamps-pq-composite-kem (Mike, John)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-composite-ml-dsa-composite-ml-kem-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document defines combinations of US NIST ML-KEM in hybrid with traditional algorithms RSA-OAEP, ECDH, X25519, and X448. These combinations are tailored to meet security best practices and regulatory guidelines. Composite ML-KEM is applicable in any application that uses X.509 or PKIX data structures that accept ML- KEM, but where the operator wants extra protection against breaks or catastrophic bugs in ML-KEM.

### Use of the ML-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-ml-dsa · Working group: lamps
Agenda: c) draft-ietf-lamps-cms-ml-dsa (Ben, Adam, Daniel)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-ml-dsa/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-ml-kem-ml-dsa-certificates-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
The Module-Lattice-Based Digital Signature Algorithm (ML-DSA), as defined by NIST in FIPS 204, is a post-quantum digital signature scheme that aims to be secure against an adversary in possession of a Cryptographically Relevant Quantum Computer (CRQC). This document specifies the conventions for using the ML-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### Best Practices for CMS SignedData with Regards to Signed Attributes
Draft: draft-vangeest-lamps-cms-euf-cma-signeddata · Working group: lamps
Agenda: b) draft-vangeest-lamps-cms-euf-cma-signeddata
page: https://datatracker.ietf.org/doc/draft-vangeest-lamps-cms-euf-cma-signeddata/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-euf-cma-for-cms-signeddata-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
The Cryptographic Message Syntax (CMS) has different signature verification behaviour based on whether signed attributes are present or not. This results in a potential existential forgery vulnerability in CMS and protocols which use CMS. This document describes the vulnerability and lists best practices and mitigations for such a vulnerability.

### PKCS #8 Private-Key Information Content Types
Draft: draft-mandel-lamps-pkcs8-prikeyinfo-contenttypes · Working group: lamps
Agenda: d) draft-mandel-lamps-pkcs8-prikeyinfo-contenttypes
page: https://datatracker.ietf.org/doc/draft-mandel-lamps-pkcs8-prikeyinfo-contenttypes/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-pkcs-8-private-key-info-content-types-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
This document defines PKCS #8 content types for use with PrivateKeyInfo and EncryptedPrivateKeyInfo as specified in RFC 5958.

### CSR Attest
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-csr-attest-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### KEM based Authentication for the IKEv2 with Post-quantum Security
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-kem-based-authentication-for-the-ikev2-with-post-quantum-security-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### CMCbis
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-cmcbis-00 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Related Certificate Descriptor
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lamps-sessa-related-certificate-descriptor-01 | video: https://www.youtube.com/watch?v=gGhv22SsL1w | materials: https://datatracker.ietf.org/meeting/122/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

## Working Group: lsr

### Flooding Reduction Algorithms Framework
Draft: draft-prz-lsr-interop-flood-reduction-architecture · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-prz-lsr-interop-flood-reduction-architecture/
page: https://datatracker.ietf.org/doc/draft-prz-lsr-interop-flood-reduction-architecture/ | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
This document introduces a framework to deploy multiple flood reduction algorithms within the same IGP domain in an interoperable fashion.

### IGP Reverse Prefix Metric
Draft: draft-li-lsr-igp-reverse-prefix-metric · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-li-lsr-igp-reverse-prefix-metric/
page: https://datatracker.ietf.org/doc/draft-li-lsr-igp-reverse-prefix-metric/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lsr-04-lsr-igp-reverse-prefix-metric-03 | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
This document defines a method for calculating reverse paths by advertising reverse prefix costs. This method aims to solve the problem of strict RPF (Reverse Path Forwarding) check failure caused by mismatched bidirectional path costs in multi-area IGP scenarios.

### IS-IS Extensions for Load Balancing Alternates
Draft: draft-dong-lsr-load-balancing-alternate · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/html/draft-dong-lsr-load-balancing-alternate-00
page: https://datatracker.ietf.org/doc/draft-dong-lsr-load-balancing-alternate/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lsr-5-load-balancing-alternate-00 | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
IGP normally computes the shortest paths in the network based on the IGP metric, without taking the link utilization into consideration. In network scenarios where there is link degradation or failure which causes link throughput reduction, or the volume of specific traffic flows increase dramatically, congestion can happen if only the best path is used for forwarding. This document describes IS-IS extensions for the computation of alternate traffic engineering paths which can be used for traffic load balancing when the shortest path is becoming congested.

### Flexible Algorithms for Energy Efficiency
Draft: draft-li-lsr-flex-algo-energy-efficiency · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-li-lsr-flex-algo-energy-efficiency/
page: https://datatracker.ietf.org/doc/draft-li-lsr-flex-algo-energy-efficiency/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lsr-7-flex-algo-for-energy-efficiency-00 | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
[draft-liu-spring-sr-policy-energy-efficiency-00] describes how energy consumption information is utilized for path selection in Segment Routing (SR) networks. This document elaborates on extending IGP protocols to carry energy consumption information, enabling its dissemination within the IGP domain and ultimately transmitting it to the controller. This allows the controller to perform routing calculations based on energy consumption metrics.

### FR architecture
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lsr-2-fr-architecture-00 | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### Leader leaderless thoughts
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lsr-3-leader-leaderless-thoughts-00 | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### LSR YANG Update
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-lsr-6-lsr-yang-update-00 | video: https://www.youtube.com/watch?v=LBMJQGqmgaI | materials: https://datatracker.ietf.org/meeting/122/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

## Working Group: masque

### CONNECT-UDP Bind
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-masque-connect-udp-bind-ietf122-00 | video: https://www.youtube.com/watch?v=1yQLxBGFkOI | materials: https://datatracker.ietf.org/meeting/122/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### QUIC-Aware Proxying
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-masque-quic-aware-proxying-00 | video: https://www.youtube.com/watch?v=1yQLxBGFkOI | materials: https://datatracker.ietf.org/meeting/122/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### MASQUE CONNECT-ETHERNET
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-masque-masque-connect-ethernet-at-ietf-122-00 | video: https://www.youtube.com/watch?v=1yQLxBGFkOI | materials: https://datatracker.ietf.org/meeting/122/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### connect-ip-dns
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-masque-slides-for-connect-ip-dns-draft-00 | video: https://www.youtube.com/watch?v=1yQLxBGFkOI | materials: https://datatracker.ietf.org/meeting/122/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### The MASQUE Proxy
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-masque-the-masque-proxy-00 | video: https://www.youtube.com/watch?v=1yQLxBGFkOI | materials: https://datatracker.ietf.org/meeting/122/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

## Working Group: oauth

### Token Status List (TSL)
Draft: draft-ietf-oauth-status-list · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-token-status-list-00 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This specification defines a status mechanism called Token Status List (TSL), data structures and processing rules for representing the status of tokens secured by JSON Object Signing and Encryption (JOSE) or CBOR Object Signing and Encryption (COSE), such as JWT, SD-JWT, CBOR Web Token, and ISO mdoc. It also defines an extension point and a registry for future status mechanisms.

### OAuth 2.0 Attestation-Based Client Authentication
Draft: draft-ietf-oauth-attestation-based-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-attestion-based-client-authentication-00 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This specification defines an extension to the OAuth 2.0 protocol (RFC 6749) that enables a client instance to include a key-bound attestation when interacting with an Authorization Server or Resource Server. This mechanism allows a client instance to prove its authenticity, as verified by a client attester, without revealing its target audience to that attester. It may also serve as a mechanism for client authentication as per OAuth 2.0.

### The OAuth 2.1 Authorization Framework
Draft: draft-ietf-oauth-v2-1 · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessb-updating-jwt-profile-for-oauth-20-client-authentication-and-authorization-grants-00 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
The OAuth 2.1 authorization framework enables an application to obtain limited access to a protected resource, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and an authorization service, or by allowing the application to obtain access on its own behalf. This specification replaces and obsoletes the OAuth 2.0 Authorization Framework described in RFC 6749 and the Bearer Token Usage in RFC 6750.

### OAuth 2.0 for First-Party Applications
Draft: draft-ietf-oauth-first-party-apps · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-first-party-apps/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-first-party-apps/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessa-oauth-for-first-party-apps-00 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This document defines the Authorization Challenge Endpoint, which supports clients that want to control the process of obtaining authorization from the user using a native experience. In many cases, this can provide an entirely browserless OAuth 2.0 experience suited for native applications, only delegating to the browser in unexpected, high-risk, or error conditions.

### OAuth 2.0 Client ID Scheme
Draft: draft-parecki-oauth-client-id-scheme · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-parecki-oauth-client-id-scheme/
page: https://datatracker.ietf.org/doc/draft-parecki-oauth-client-id-scheme/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessa-oauth-client-id-scheme-01 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This specification defines the concept of a Client Identifier Scheme to enable Authorization Servers and Clients to use more than one mechanism to obtain and validate Client metadata.

### Selective Disclosure for JWTs (SD-JWT)
Draft: draft-ietf-oauth-selective-disclosure-jwt · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/ | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This specification defines a mechanism for the selective disclosure of individual elements of a JSON data structure used as the payload of a JSON Web Signature (JWS). The primary use case is the selective disclosure of JSON Web Token (JWT) claims.

### SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)
Draft: draft-ietf-oauth-sd-jwt-vc · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessb-sd-jwt-02 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This specification describes data formats as well as validation and processing rules to express Verifiable Digital Credentials with JSON payloads with and without selective disclosure based on the SD-JWT format.

### Updates to OAuth 2.0 JSON Web Token (JWT) Client Authentication and Assertion-Based Authorization Grants
Draft: draft-ietf-oauth-rfc7523bis · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/ | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This document updates RFC7521, RFC7522, RFC7523 and RFC9126 with respect to the treatment of audience values in OAuth 2.0 Client Assertion Authentication and Assertion-based Authorization Grants to address a security vulnerability identified in the previous requirements for those audience values in multiple OAuth 2.0 specifications.

### Transaction Tokens
Draft: draft-ietf-oauth-transaction-tokens · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessa-ietf-122-transaction-tokens-00 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Transaction Tokens (Txn-Tokens) are designed to maintain and propagate user identity, workload identity and authorization context throughout the Call Chain within a trusted domain during the processing of external requests (e.g. such as API calls) or requests initiated internally within the Trust Domain. Txn-Tokens ensure that this context is preserved throughout the Call Chain thereby enhancing security and consistency in complex, multi-service architectures.

### OAuth Identity and Authorization Chaining Across Domains
Draft: draft-ietf-oauth-identity-chaining · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessb-oauth-identity-and-authorization-chaining-across-domains-01 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
This specification describes a mechanism for preserving identity and authorization information across trust domains that use the OAuth 2.0 Framework. A JSON Web Token (JWT) authorization grant, obtained through an intra-domain OAuth 2.0 Token Exchange, facilitates the cross-domain acquisition of an access token. The relevant identity and authorization information is chained throughout the flow by being conveyed in the respective artifacts exchanged at each step of the process. Chaining across multiple domains is achieved by using the same protocol every time a trust domain boundary is crossed.

### Deferred Key Binding for OAuth
Draft: draft-richer-oauth-tmb-claim · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/html/draft-richer-oauth-tmb-claim
page: https://datatracker.ietf.org/doc/draft-richer-oauth-tmb-claim/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessb-deferred-key-binding-for-oauth-tokens-01 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Sometimes you want to get a token that's tied to a public key but you can't prove possession of that public key. That's when you need to trust me, bruh.

### OAuth 2.1
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessa-oauth-21-00 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Security BCP Update
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessa-security-bcp-update-00 | video: https://www.youtube.com/watch?v=0mfln_LvCJU | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### OAuth Token Exchange Extensions
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-oauth-token-exchange-extensions-00 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Transaction Tokens
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessb-transaction-tokens-00 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### SD-JWT VC
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-oauth-sessb-sd-jwt-vc-00 | video: https://www.youtube.com/watch?v=8nHAIs-Jg9Y | materials: https://datatracker.ietf.org/meeting/122/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

## Working Group: pquip

### Terminology for Post-Quantum Traditional Hybrid Schemes
Draft: draft-ietf-pquip-pqt-hybrid-terminology · Working group: pquip
Agenda: draft-ietf-pquip-pqt-hybrid-terminology
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqt-hybrid-terminology/ | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
One aspect of the transition to post-quantum algorithms in cryptographic protocols is the development of hybrid schemes that incorporate both post-quantum and traditional asymmetric algorithms. This document defines terminology for such schemes. It is intended to be used as a reference and, hopefully, to ensure consistency and clarity across different protocols, standards, and organisations.

### Hybrid signature spectrums
Draft: draft-ietf-pquip-hybrid-signature-spectrums · Working group: pquip
Agenda: draft-ietf-pquip-hybrid-signature-spectrums
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-hybrid-signature-spectrums/ | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
This document describes classification of design goals and security considerations for hybrid digital signature schemes, including proof composability, non-separability of the component signatures given a hybrid signature, backwards/forwards compatibility, hybrid generality, and simultaneous verification.

### Post-Quantum Cryptography for Engineers
Draft: draft-ietf-pquip-pqc-engineers · Working group: pquip
Agenda: draft-ietf-pquip-pqc-engineers
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-engineers/ | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
The advent of a cryptographically relevant quantum computer (CRQC) would render state-of-the-art, traditional public key algorithms deployed today obsolete, as the mathematical assumptions underpinning their security would no longer hold. To address this, protocols and infrastructure must transition to post-quantum algorithms, which are designed to resist both traditional and quantum attacks. This document explains why engineers need to be aware of and understand post-quantum cryptography (PQC), detailing the impact of CRQCs on existing systems and the challenges involved in transitioning to post-quantum algorithms. Unlike previous cryptographic updates, this shift may require significant protocol redesign due to the unique properties of post-quantum algorithms.

### Hash-based Signatures: State and Backup Management
Draft: draft-wiggers-hbs-state · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-wiggers-hbs-state/
page: https://datatracker.ietf.org/doc/draft-wiggers-hbs-state/ | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
Stateful Hash-Based Signature Schemes (S-HBS) such as LMS, HSS, XMSS and XMSS^MT combine Merkle trees with One-Time Signatures (OTS) to provide signatures that are resistant against attacks using large- scale quantum computers. Unlike conventional stateless digital signature schemes, S-HBS have a state to keep track of which OTS keys have been used, as double-signing with the same OTS key allows forgeries. This document provides guidance and documents security considerations for the operational and technical aspects of deploying systems that rely on S-HBS. Management of the state of the S-HBS, including any handling of redundant key material, is a sensitive topic, and we discuss some approaches to handle the associated challenges. We also describe the challenges that need to be resolved before certain approaches should be considered.

### Adapting Constrained Devices for Post-Quantum Cryptography
Draft: draft-reddy-pquip-pqc-hsm · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-reddy-pquip-pqc-hsm/
page: https://datatracker.ietf.org/doc/draft-reddy-pquip-pqc-hsm/ | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
This document offers guidance on incorporating Post-Quantum Cryptography (PQC) into resource-constrained devices, including IoT devices and lightweight Hardware Security Modules (HSMs), which operate under tight limitations on compute power, memory, storage, and energy. It highlights the role of the Root of Trust in enabling secure operations, including seed-based key generation to reduce the need for persistent storage, efficient approaches to managing ephemeral keys, and methods for offloading cryptographic tasks in low-resource environments. Additionally, it examines how PQC affects firmware update mechanisms in such constrained systems.

### S-HBS state management update
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-pquip-s-hbs-state-management-update-00 | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

### Adapting HSMs for PQC
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-pquip-adapting-hsms-for-pqc-00 | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

### Efficient (!) PQ through Hybrids
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-pquip-efficient-pq-through-hybrids-00 | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

### The Great Private Key War of '25
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-pquip-the-great-private-key-war-of-25-02 | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

### IETF is Quantum-Fragile
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-pquip-ietf-is-quantum-fragile-01 | video: https://www.youtube.com/watch?v=qIA2nN4o3mc | materials: https://datatracker.ietf.org/meeting/122/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

## Working Group: quic

### QUIC Extended Acknowledgement for Reporting Packet Receive Timestamps
Draft: draft-smith-quic-receive-ts · Working group: quic
Agenda: 20 min - QUIC Ack Receive Timestamps / Extended ACKs draft-smith-quic-receive-ts [slides] ()
page: https://datatracker.ietf.org/doc/draft-smith-quic-receive-ts/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-quic-quic-packet-receive-timestamps-via-extended-ack-00 | video: https://www.youtube.com/watch?v=9NR_MndcJIY | materials: https://datatracker.ietf.org/meeting/122/session/quic
This document defines an extension to the QUIC transport protocol which supports reporting multiple packet receive timestamps for post- handshake packets. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the QUIC Working Group mailing list (quic@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/quic/. Source for this draft and an issue tracker can be found at https://github.com/wcsmith/draft-quic-receive-ts.

### Extended Key Update for QUIC
Draft: draft-rosomakho-quic-extended-key-update · Working group: quic
Agenda: 20 min - Extended Key Update draft-rosomakho-quic-extended-key-update slides
page: https://datatracker.ietf.org/doc/draft-rosomakho-quic-extended-key-update/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-quic-extended-key-update-slides-00 | video: https://www.youtube.com/watch?v=9NR_MndcJIY | materials: https://datatracker.ietf.org/meeting/122/session/quic
This document specifies an Extended Key Update mechanism for the QUIC protocol, building on the foundation of the TLS Extended Key Update. The TLS Extended Key Update specification enhances the TLS protocol by introducing key updates with forward secrecy, eliminating the need to perform a full handshake. This feature is particularly beneficial for maintaining security in scenarios involving long-lived connections. This specification replaces the QUIC Key Update mechanism described in the "Using TLS to Secure QUIC" specification.

### Source Buffer Management
Draft: draft-cheshire-sbm · Working group: quic
Agenda: 10 min - Source Buffer Management draft-cheshire-sbm slides
page: https://datatracker.ietf.org/doc/draft-cheshire-sbm/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-quic-ietf-122-stuart-cheshire-source-buffer-management-00 | video: https://www.youtube.com/watch?v=9NR_MndcJIY | materials: https://datatracker.ietf.org/meeting/122/session/quic
In the past decade there has been growing awareness about the harmful effects of bufferbloat in the network, and there has been good work on developments like L4S to address that problem. However, bufferbloat on the sender itself remains a significant additional problem, which has not received similar attention. This document offers techniques and guidance for host networking software to avoid network traffic suffering unnecessary delays caused by excessive buffering at the sender. These improvements are broadly applicable across all datagram and transport protocols (UDP, TCP, QUIC, etc.) on all operating systems.

### QUIC on Streams
Draft: draft-kazuho-quic-quic-on-streams · Working group: quic
Agenda: 15 min - Stream multiplexing draft-kazuho-quic-quic-on-streams slides
page: https://datatracker.ietf.org/doc/draft-kazuho-quic-quic-on-streams/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-quic-qmux-formerly-quic-on-streams-01 | video: https://www.youtube.com/watch?v=9NR_MndcJIY | materials: https://datatracker.ietf.org/meeting/122/session/quic
This document specifies a polyfill of QUIC version 1 that runs on top of bi-directional streams such as TLS. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the QUIC Working Group mailing list (quic@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/quic/. Source for this draft and an issue tracker can be found at https://github.com/kazuho/draft-kazuho-quic-quic-on-streams.

### Multipath QUIC
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-quic-multipath-quic-00 | video: https://www.youtube.com/watch?v=9NR_MndcJIY | materials: https://datatracker.ietf.org/meeting/122/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### QUIC Address Discovery
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-quic-quic-address-discovery-00 | video: https://www.youtube.com/watch?v=9NR_MndcJIY | materials: https://datatracker.ietf.org/meeting/122/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

## Working Group: rats

### RATS Conceptual Messages Wrapper (CMW)
Draft: draft-ietf-rats-msg-wrap · Working group: rats
Agenda: (10 min) Thomas Fossati - https://datatracker.ietf.org/doc/draft-ietf-rats-msg-wrap/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-msg-wrap/ | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
The Conceptual Messages introduced by the RATS architecture (RFC 9334) are protocol-agnostic data units that are conveyed between RATS roles during remote attestation procedures. Conceptual Messages describe the meaning and function of such data units within RATS data flows without specifying a wire format, encoding, transport mechanism, or processing details. The initial set of Conceptual Messages is defined in Section 8 of RFC 9334 and includes Evidence, Attestation Results, Endorsements, Reference Values, and Appraisal Policies. This document introduces the Conceptual Message Wrapper (CMW) that provides a common structure to encapsulate these messages. It defines a dedicated CBOR tag, corresponding JSON Web Token (JWT) and CBOR Web Token (CWT) claims, and an X.509 extension. This allows CMWs to be used in CBOR-based protocols, web APIs using JWTs and CWTs, and PKIX artifacts like X.509 certificates. Additionally, the draft defines a media type and a CoAP content format to transport CMWs over protocols like HTTP, MIME, and CoAP. The goal is to improve the interoperability and flexibility of remote attestation protocols. Introducing a shared message format such as CMW enables consistent support for different attestation message types, evolving message serialization formats without breaking compatibility, and avoiding the need to redefine how messages are handled within each protocol.

### Entity Attestation Token (EAT) Measured Component
Draft: draft-ietf-rats-eat-measured-component · Working group: rats
Agenda: (10 min) Thomas Fossati - https://datatracker.ietf.org/doc/draft-ietf-rats-eat-measured-component/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-eat-measured-component/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-eat-measured-components-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
The term "measured component" refers to an object within the attester's target environment whose state can be sampled and typically digested using a cryptographic hash function. Examples of measured components include firmware stored in flash memory, software loaded into memory at start time, data stored in a file system, or values in a CPU register. This document provides the information model for the "measured component" and two associated data models. This separation is intentional: the JSON and CBOR serializations, coupled with the media types and associated Constrained Application Protocol (CoAP) Content-Formats, enable the immediate use of the semantics within the Entity Attestation Token (EAT) framework. Meanwhile, the information model can be reused in future specifications to provide additional serializations, for example, using ASN.1.

### Concise Reference Integrity Manifest
Draft: draft-ietf-rats-corim · Working group: rats
Agenda: (15 + 5 min) Yogesh Deshpande - https://datatracker.ietf.org/doc/draft-ietf-rats-corim/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-corim/ | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Remote Attestation Procedures (RATS) enable Relying Parties to assess the trustworthiness of a remote Attester and therefore to decide whether or not to engage in secure interactions with it. Evidence about trustworthiness can be rather complex and it is deemed unrealistic that every Relying Party is capable of the appraisal of Evidence. Therefore that burden is typically offloaded to a Verifier. In order to conduct Evidence appraisal, a Verifier requires not only fresh Evidence from an Attester, but also trusted Endorsements and Reference Values from Endorsers and Reference Value Providers, such as manufacturers, distributors, or device owners. This document specifies the information elements for representing Endorsements and Reference Values in CBOR format.

### Evidence Encoding for Hardware Security Modules
Draft: draft-ietf-rats-pkix-key-attestation · Working group: rats
Agenda: (20 min) Mike Ounsworth - https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-pkix-key-attestation-02 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
This document specifies a vendor-agnostic format for Evidence produced and verified within a PKIX context. The Evidence produced this way includes claims collected about a cryptographic module, such as a Hardware Security Module (HSM), and elements found within it such as cryptographic keys. One scenario envisaged is that the state information about the cryptographic module can be securely presented to a remote operator or auditor in a vendor-agnostic verifiable format. A more complex scenario would be to submit this Evidence to a Certification Authority to aid in determining whether the storage properties of this key meet the requirements of a given certificate profile.

### Reference Interaction Models for Remote Attestation Procedures
Draft: draft-ietf-rats-reference-interaction-models · Working group: rats
Agenda: (10 + 5 min) Henk Birkholz - https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-reference-interaction-models-network-device-subscription-for-charra-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
This document describes interaction models for remote attestation procedures (RATS) [RFC9334]. Three conveying mechanisms -- Challenge/Response, Uni-Directional, and Streaming Remote Attestation -- are illustrated and defined. Analogously, a general overview about the information elements typically used by corresponding conveyance protocols are highlighted.

### Attestation Event Stream Subscription
Draft: draft-ietf-rats-network-device-subscription · Working group: rats
Agenda: (5 + 5 min) Henk Birkholz - https://datatracker.ietf.org/doc/draft-ietf-rats-network-device-subscription/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-network-device-subscription/ | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
This document defines how to subscribe to YANG Event Streams for Remote Attestation Procedures (RATS). Specifically, this document defines a YANG module that augments the YANG module for Trusted Platform Module (TPM)-based Challenge-Response Remote Attestation (CHARRA), enabling subscription to RATS Conceptual Messages of the Evidence type and auxiliary Event Logs as part of that Evidence. The module defined requires at least one Trusted Platform Module (TPM) 1.2 or TPM 2.0 (or equivalent hardware implementation providing the same protected capabilities as a TPM) must be available on the Attester on which the YANG server is running.

### Evidence Transformations
Draft: draft-smith-rats-evidence-trans · Working group: rats
Agenda: (5 + 5 min) Ned Smith - https://datatracker.ietf.org/doc/draft-smith-rats-evidence-trans/
page: https://datatracker.ietf.org/doc/draft-smith-rats-evidence-trans/ | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Remote Attestation Procedures (RATS) enable Relying Parties to assess the trustworthiness of a remote Attester to decide if continued interaction is warrented. Evidence structures can vary making appraisals challenging for Verifiers. Verifiers need to understand Evidence encoding formats and some of the Evidence semantics to appraise it. Consequently, Evidence may require format transformation to an internal representation that preserves original semantics. This document specifies Evidence transformation methods for DiceTcbInfo, concise evidence, and SPDM measurements block structures. These Evidence structures are converted to the CoRIM internal representation and follow CoRIM defined appraisal procedures.

### MUD-Based RATS Resources Discovery
Draft: draft-birkholz-rats-mud · Working group: rats
Agenda: (5 + 5 min) Henk Birkholz - https://datatracker.ietf.org/doc/draft-birkholz-rats-mud/
page: https://datatracker.ietf.org/doc/draft-birkholz-rats-mud/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-mud-based-rats-resource-discovery-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Manufacturer Usage Description (MUD) files and the MUD URIs that point to them are defined in RFC 8520. This document introduces a new type of MUD file to be delivered in conjunction with a MUD file signature and/or to be referenced via a MUD URI embedded in other documents or messages, such as an IEEE 802.1AR Secure Device Identifier (DevID) or a CBOR Web Token (CWT). These signed documents can be presented to other entities, e.g., a network management system or network path orchestrator. If this entity also takes on the role of a verifier as defined by the IETF Remote ATtestation procedureS (RATS) architecture, this verifier can use the references included in the MUD file specified in this document to discover, for example, appropriate reference value providers, endorsement documents or endorsement distribution APIs, trust anchor stores, remote verifier services (sometimes referred to as Attestation Verification Services), or transparency logs. All theses references in the MUD file pointing to resources and auxiliary RATS services can satisfy general RATS prerequisite by enabling discovery or improve discovery resilience of corresponding resources or services.

### EAT Attestation Results
Draft: draft-fv-rats-ear · Working group: rats
Agenda: (5 + 5 min) Thomas Fossati - https://datatracker.ietf.org/doc/draft-fv-rats-ear/
page: https://datatracker.ietf.org/doc/draft-fv-rats-ear/ | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
This document defines the EAT Attestation Result (EAR) message format. EAR is used by a verifier to encode the result of the appraisal over an attester's evidence. It embeds an AR4SI's "trustworthiness vector" to present a normalized view of the evaluation results, thus easing the task of defining and computing authorization policies by relying parties. Alongside the trustworthiness vector, EAR provides contextual information bound to the appraisal process. This allows a relying party (or an auditor) to reconstruct the frame of reference in which the trustworthiness vector was originally computed. EAR supports simple devices with one attester as well as composite devices that are made of multiple attesters, allowing the state of each attester to be separately examined. EAR can also accommodate registered and unregistered extensions. It can be serialized and protected using either CWT or JWT.

### CMW
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-cmw-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### CoRIM@IETF122
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-corimietf122-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Evidence Transformation
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-evidence-transformation-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### AR4SI and EAR
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rats-ar4si-and-ear-00 | video: https://www.youtube.com/watch?v=mLeNiPlo8pU | materials: https://datatracker.ietf.org/meeting/122/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

## Working Group: rtgwg

### Networks to Cloud DCs: Challenges and Mitigation Practices
Draft: draft-ietf-rtgwg-net2cloud-problem-statement · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-net2cloud-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-net2cloud-problem-statement/ | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
This document describes a set of network-related problems enterprises face when interconnecting their branch offices with dynamic workloads in third-party data centers (DCs) (a.k.a. Cloud DCs). These challenges are particularly relevant to enterprises with conventional VPN services that want to leverage those networks (instead of altogether abandoning them). The document also outlines various mitigation approaches, including those already developed within the IETF. For challenges that do not yet have established solutions, it identifies the IETF drafts that have been proposed to address these issues. The intent is to provide a cohesive view of problems and solution approaches that have been documented or proposed within the IETF.

### Multi-segment SD-WAN via Cloud Backbone
Draft: draft-ietf-rtgwg-multisegment-sdwan · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-multisegment-sdwan/ | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
This document describes a method for seamlessly interconnecting geographically separated SD-WAN segments via a Cloud Backbone without requiring Cloud Gateways (GWs) to decrypt and re-encrypt traffic. By encapsulating IPsec- encrypted payloads within GENEVE headers (RFC 8926), the approach enables Cloud GWs to forward encrypted traffic directly between distant Customer Premises Equipment (CPEs). This reduces processing overhead, improves scalability, and preserves the confidentiality of enterprise data while ensuring secure and efficient multi-segment SD-WAN connectivity.

### YANG Data Model for IPv6 Neighbor Discovery
Draft: draft-ietf-rtgwg-ipv6-address-resolution-yang · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-ipv6-address-resolution-yang/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-ipv6-address-resolution-yang/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-04-ipv6-address-resolution-yang-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
This document defines a YANG data model to configure and manage IPv6 Neighbor Discovery (ND) and related functions, including IPv6 address resolution, redirect function, proxy Neighbor Advertisement, Neighbor Unreachability Detection (NUD), Duplicate Address Detection (DAD), SEcure Neighbor Discovery (SEND), and Secure ND Proxy.

### Fast failure detection in VRRP with Point to Point BFD
Draft: draft-ietf-rtgwg-vrrp-bfd-p2p · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-bfd-p2p/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-bfd-p2p/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-05-vrrp-bfd-02 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
This document describes how Point to Point Bidirectional Forwarding Detection (BFD) can be used to support sub-second detection of a Active Router failure in the Virtual Router Redundancy Protocol (VRRP).

### SR Policy Programming RPC
Draft: draft-ali-spring-sr-policy-programming-rpc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ali-spring-sr-policy-programming-rpc/
page: https://datatracker.ietf.org/doc/draft-ali-spring-sr-policy-programming-rpc/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-06-sr-policy-programming-rpc-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
The document specifies a Remote Procedure Call (RPC) for programming ephemeral states associated with an SR Policy.

### The Challenges and Requirements for Routing in Computing Cluster network
Draft: draft-li-rtgwg-computing-network-routing · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-li-rtgwg-computing-network-routing/
page: https://datatracker.ietf.org/doc/draft-li-rtgwg-computing-network-routing/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-07-challenges-and-requirements-for-routing-in-computing-cluster-network-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
This document explores the characteristics of computing cluster network and analyzes the challenges of employing the traditional distributed or centralized routing mechanisms in it. In order to achieve the enhanced scalability, improved resilience and optimized performance simultaneously, hybrid routing is briefly examined as a potential way to combine the advantages of distributed and centralized mechanisms. The document further shows the possible future work.

### Routing in Satellite Networks: Challenges & Considerations
Draft: draft-lj-rtgwg-sat-routing-consideration · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-lj-rtgwg-sat-routing-consideration/
page: https://datatracker.ietf.org/doc/draft-lj-rtgwg-sat-routing-consideration/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-08-routing-in-satellite-networks-challenges-considerations-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
The SDO 3GPP has done tremendous work to either standardize or study various types of wireless services that would depend on the satellite constellation network. While the ISLs, or Inter-Satellite Links, along with the routing scheme(s) over them are critical to help fullfil the satellite services, the 3GPP considers them out-of-scope. This leaves the significant work to be explored in the IETF domain. This draft stems from the 3GPP satellite use cases that have been studied for many years up to now, across a couple of releases, and lands on summarizing the challenges & considerations of the satellite-based routing. Based on some unique & advantageous characteristics associated with satellite networks, the draft raises briefly the general routing considerations for the integrated Non- Terrestrial & Terrestial Networks.

### IGP Color-Aware Shortcut
Draft: draft-cheng-lsr-igp-shortcut-enhancement · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-cheng-lsr-igp-shortcut-enhancement/
page: https://datatracker.ietf.org/doc/draft-cheng-lsr-igp-shortcut-enhancement/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-9-rtgwg-igp-color-aware-shortcut-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
IGP shortcut mechanism allows calculating routes to forward traffic over Traffic Engineering tunnels. This document specifies the enhancement of IGP shortcut which can steer routes onto TE-tunnels based on colors.

### Artificial Intelligence (AI) for Network Operations
Draft: draft-king-rokui-ainetops-usecases · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-king-rokui-ainetops-usecases/
page: https://datatracker.ietf.org/doc/draft-king-rokui-ainetops-usecases/ | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
This document explores the role of the IETF and IRTF in advancing Artificial Intelligence for network operations (AINetOps), focusing on requirements for IETF protocols and architectures. AINetOps applies AI/ML techniques to automate and optimize network operations, enabling use cases such as reactive troubleshooting, proactive assurance, closed-loop optimization, misconfiguration detection, and virtual operator assistance. The document addresses AINetOps for both single-layer IP or Optical networks and multi-layer IP/Optical networks. It defines the concept of AINetOps for networking and provides its operational benefits such as network assurance, predictive analytics, network optimization, multi-layer planning, and more. It aims to guide the evolution of IETF protocols to support AINetOps-driven network management.

### Scenarios and Protocol Extension Requirements of a Generalized IPv6 Tunnel
Draft: draft-li-rtgwg-gip6-protocol-ext-requirements · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-li-rtgwg-gip6-protocol-ext-requirements/
page: https://datatracker.ietf.org/doc/draft-li-rtgwg-gip6-protocol-ext-requirements/ | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
IPv6 provides extension header mechanism for additional functions. There are emerging features based on the extension headers, such as SRv6, Network Slicing, Alternate Marking, iOAM, DetNet etc. In some networks, the operators might want to leverage these new features but since the network system still using some lagecy encapsulations other than IPv6 (e.g. VxLAN, GRE etc.), these features are just not applicable for them. This document introduces some cases of such scenarios, and discusses the potential requirement of defining a new Generalized IPv6 Tunnel (GIP6). With GIP6, all the additional functions defined as IPv6 extension headers could be easily supported, so that the legacy encapsulations could migrate to a unified solution rather than sccaterred upgrade in each legacy technologies, which is heavy burden for the industry. Considering network devices have different capabilities of IPv6 extension header processing, this document also analyses the issues found during the deployment of the above new features using IPv6 extension headers and the protocol extension requirements for IPv6 capability advertisement are defined.

### SR based Loop-free implementation
Draft: draft-deng-rtgwg-sr-loop-free · Working group: rtgwg
Agenda: https://www.ietf.org/archive/id/draft-deng-rtgwg-sr-loop-free-01.txt
page: https://datatracker.ietf.org/doc/draft-deng-rtgwg-sr-loop-free/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-12-sr-loop-free-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
Microloops are transient packet loops that occur in the network following a topology change (link down, link up, node fault, or metric change events). Microloops are caused by the non-simultaneous convergence of different nodes in the network. If nodes converge and send traffic to a neighbor node that has not converged yet, traffic may be looped between these two nodes, resulting in packet loss, jitter, and out-of-order packets. This document presents some optional implementation methods aimed at providing loop avoidance in the case of IGP network convergence event in different scenarios.

### Net2Cloud
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-02-net2cloud-02 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### multi-segment-sdwan
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-03-multi-segment-sdwan-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### AINetOps
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-10-ainetops-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### Scenarios and Gaps towards a Generalized IPv6 Tunnel
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-rtgwg-scenarios-and-gaps-towards-a-generalized-ipv6-tunnel-00 | video: https://www.youtube.com/watch?v=GA0cPZfLO8Q | materials: https://datatracker.ietf.org/meeting/122/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

## Working Group: savnet

### Source Address Validation Deployment Status
Draft: draft-wang-sav-deployment-status · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-wang-sav-deployment-status/
page: https://datatracker.ietf.org/doc/draft-wang-sav-deployment-status/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-source-address-validation-deployment-status-01 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This document provides a summary of methods for measuring the deployment status of source address validation, with an overview of its deployment status. It reviews various methods for measuring outbound and/or inbound source address validation, including established tools like CAIDA Spoofer, as well as recently proposed remote measurement methods. By combining results from these different methods, the document offers a comprehensive overview of the status of source address validation deployment across the Internet.

### General Source Address Validation Capabilities
Draft: draft-huang-savnet-sav-table · Working group: savnet
Agenda: Draft link: draft-huang-savnet-sav-table-08
page: https://datatracker.ietf.org/doc/draft-huang-savnet-sav-table/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-general-source-address-validation-capabilities-01 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
The SAV rules of existing source address validation (SAV) mechanisms, are derived from other core data structures, e.g., FIB-based uRPF, which are not dedicatedly designed for source filtering. Therefore there are some limitations related to deployable scenarios and traffic handling policies. To overcome these limitations, this document introduces the general SAV capabilities from data plane perspective. How to implement the capabilities and how to generate SAV rules are not in the scope of this document.

### Intra-domain Source Address Validation Architecture
Draft: draft-ietf-savnet-intra-domain-architecture · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-a-summary-of-discussions-on-intra-domain-savnet-architecture-00 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This document describes a generic architecture for intra-domain Source Address Validation (SAV). It provides a common framework for developing new intra-domain SAV mechanisms and describes the conditions under which this architecture can improve SAV accuracy and operational efficiency with respect to existing intra-domain SAV mechanisms.

### Intra-domain Source Address Validation (SAV) Solution Based on BM-SPF
Draft: draft-wang-savnet-intra-domain-solution-bm-spf · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-wang-savnet-intra-domain-solution-bm-spf/
page: https://datatracker.ietf.org/doc/draft-wang-savnet-intra-domain-solution-bm-spf/ | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This draft proposes a new intra-domain Source Address Validation (SAV) solution. This solution leverages the Bidirectional Metric- based Shortest Path First (BM-SPF) mechanism to avoid the complexity introduced by asymmetric routing for source address validation. It allows intra-domain routers to generate directly the SAV rule from the router's FIB table, based on the reality that the source and destination interface will be same if the IGP domain is symmetric assured.

### Problem Statement, Gap Analysis, and Requirements for Inter-Domain Source Address Validation
Draft: draft-ietf-savnet-inter-domain-problem-statement · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-source-address-validation-in-inter-domain-networks-gap-analysis-problem-statement-and-requirements-01 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This document analyzes the problem space and provides a gap analysis of existing inter-domain source address validation (SAV) mechanisms. Based on these findings, it outlines the technical requirements for future improvements.

### Inter-domain Source Address Validation (SAVNET) Architecture
Draft: draft-ietf-savnet-inter-domain-architecture · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-architecture/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-architecture/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-inter-domain-source-address-validation-savnet-architecture-01 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This document specifies an architecture for inter-domain source address validation (SAV). The architecture provides a common framework for collecting SAV-specific and SAV-related information from multiple sources, determining the legitimate incoming directions of source prefixes, and using this information to generate SAV table for inter-domain SAV. A SAV agent maintains the collected information in a SAV Information Base (SIB), and the SAV Information Base Manager (SIM) uses the available information to determine the corresponding prefix and legitimate incoming-direction mappings and generate or update the SAV table. This document also defines the architectural components and communication framework of inter-domain SAV, and discusses deployment, operation, convergence, manageability, security, and privacy considerations. It does not define a specific SAV protocol, protocol extension, or SAV table generation algorithm.

### Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)
Draft: draft-ietf-sidrops-bar-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-sidrops-bar-sav/
page: https://datatracker.ietf.org/doc/draft-ietf-sidrops-bar-sav/ | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
Designing an efficient source address validation (SAV) filter requires minimizing false positives (i.e., avoiding blocking legitimate traffic) while maintaining directionality (see RFC8704). This document advances the technology for SAV filter design through a method that makes use of BGP UPDATE messages, Autonomous System Provider Authorization (ASPA), and Route Origin Authorization (ROA). The proposed method's name is abbreviated as BAR-SAV. BAR-SAV can be used by network operators to derive more robust SAV filters and thus improve network resilience. This document updates RFC8704.

### Inter-domain Source Address Validation based on AS relationships
Draft: draft-rly-savnet-inter-domain-as-relationships · Working group: savnet
Agenda: Draft link: draft-rly-savnet-inter-domain-as-relationships-02
page: https://datatracker.ietf.org/doc/draft-rly-savnet-inter-domain-as-relationships/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-inter-domain-source-address-validation-based-on-as-relationships-00 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This draft introduces a distributed inter-domain source address validation scheme based on AS relationships named AS Relationship Based Inter-domain Filtering (ARBIF). It primarily describes this method from seven aspects: a brief introduction to the scheme, an overview of the AS relationship classification and acquisition methods, the architecture of the ARBIF system, implementation based on BGP extension, typical use cases, experiments of ARBIF, and considerations for deployability.

### BGP Extensions for Source Address Validation Networks (BGP SAVNET)
Draft: draft-geng-idr-bgp-savnet · Working group: savnet
Agenda: Title: Inter-Domain SAVNET Solution (draft-geng-idr-bgp-savnet, will be divided
page: https://datatracker.ietf.org/doc/draft-geng-idr-bgp-savnet/ | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
Many source address validation (SAV) mechanisms have been proposed for preventing source address spoofing. However, existing SAV mechanisms are faced with the problems of inaccurate validation or high operational overhead in some scenarios. This document proposes BGP SAVNET by extending BGP protocol for SAV. This protocol can propagate SAV-related information through BGP messages. The propagated information will help edge/border routers automatically generate accurate SAV rules. These rules construct a validation boundary for the network and help check the validity of source addresses of arrival data packets.

### Advertising SAV Rule-related Information using BGP Link-State
Draft: draft-tong-idr-bgp-ls-sav-rule · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/
page: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/ | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This document proposes extensions to the BGP Link-State protocol for advertising Source Address Validation (SAV) rule-related information for monitoring and management purposes.

### YANG Data Model for Intra-domain and Inter-domain Source Address Validation (SAVNET)
Draft: draft-li-savnet-sav-yang · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/
page: https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-yang-data-model-for-intra-domain-and-inter-domain-source-address-validation-savnet-02 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
This document describes a YANG data model for Intra-domain and Inter-domain Source Address Validation (SAVNET). The model serves as a base framework for configuring and managing an SAV subsystem, including SAV rule and SAV Tables, and expected to be augmented by other SAV technology models accordingly. Additionally, this document also specifies the model for the SAV Static application.

### New Intra-domain SAV Solution
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-new-intra-domain-sav-solution-01 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### An update on the  SAV using BGP UPDATE messages, ASPA, and ROA (BAR-SAV)
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-an-update-on-the-sav-using-bgp-update-messages-aspa-and-roa-bar-sav-00 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Inter-domain SAVNET solution
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-inter-domain-savnet-solution-00 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Advertisement of Multi-Sourced SAV Rules using BGP Link-State
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-savnet-advertisement-of-multi-sourced-sav-rules-using-bgp-link-state-01 | video: https://www.youtube.com/watch?v=L-zx1H0ZcPQ | materials: https://datatracker.ietf.org/meeting/122/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

## Working Group: scitt

### IETF-122-SCITT
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-scitt-ietf-122-scitt-01 | video: https://www.youtube.com/watch?v=MQQYFC3n1a4 | materials: https://datatracker.ietf.org/meeting/122/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

### IETF-122-SCITT-final
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-scitt-ietf-122-scitt-final-00 | video: https://www.youtube.com/watch?v=MQQYFC3n1a4 | materials: https://datatracker.ietf.org/meeting/122/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

## Working Group: secdispatch

### Recommendations for Key Directories over HTTP
Draft: draft-darling-key-directory-over-http · Working group: secdispatch
Agenda: draft-darling-key-directory-over-http
page: https://datatracker.ietf.org/doc/draft-darling-key-directory-over-http/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-secdispatch-recommendations-for-key-directories-over-http-02 | video: https://www.youtube.com/watch?v=toh48rM6EJM | materials: https://datatracker.ietf.org/meeting/122/session/secdispatch
This document defines recommendations for protocols that expose public keys over HTTP.

### Organization Trust Relationship Protocol
Draft: draft-org-trust-relationship-protocol · Working group: secdispatch
Agenda: draft-org-trust-relationship-protocol
page: https://datatracker.ietf.org/doc/draft-org-trust-relationship-protocol/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-secdispatch-organization-trust-relationship-protocol-00 | video: https://www.youtube.com/watch?v=toh48rM6EJM | materials: https://datatracker.ietf.org/meeting/122/session/secdispatch
This document specifies the "Organization Trust Relationship Protocol" method for service owners (organizations) to express in a standard format their trusted relationships with other organizations, as well as identify the social networks they control. This method was originally defined by Scott Yates in 2020 for this purpose.

### Lightweight Directory Access Protocol (LDAP): Additional Syntaxes
Draft: draft-codere-ldapsyntax · Working group: secdispatch
Agenda: draft-codere-ldapsyntax
page: https://datatracker.ietf.org/doc/draft-codere-ldapsyntax/ | video: https://www.youtube.com/watch?v=toh48rM6EJM | materials: https://datatracker.ietf.org/meeting/122/session/secdispatch
This document registers additional syntax definitions for use in Lightweight Directory Access Protocol (LDAP) directory and Directory services series X.500. This includes widely used datatypes and syntaxes.

### LDAP Additional syntaxes
Presentation · Working group: secdispatch
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-secdispatch-ldap-additional-syntaxes-00 | video: https://www.youtube.com/watch?v=toh48rM6EJM | materials: https://datatracker.ietf.org/meeting/122/session/secdispatch
Slides presented at the secdispatch session; no Internet-Draft is linked to them.

## Working Group: spice

### Selective Disclosure CBOR Web Tokens (SD-CWT)
Draft: draft-ietf-spice-sd-cwt · Working group: spice
Agenda: - SPICE SD-CWT - https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/ - 15 min (Mike Prorock)
page: https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spice-sessa-sd-cwt-update-for-ietf122-00 | video: https://www.youtube.com/watch?v=HFA7cQvJTxU | materials: https://datatracker.ietf.org/meeting/122/session/spice
This specification describes a data minimization technique for use with CBOR Web Tokens (CWTs). The approach is inspired by the Selective Disclosure JSON Web Token (SD-JWT), with changes to align with CBOR Object Signing and Encryption (COSE) and CWTs.

### SPICE GLUE: GLobal Unique Enterprise (GLUE) Identifiers
Draft: draft-zundel-spice-glue-id · Working group: spice
Agenda: - SPICE GLUE: GLobal Unique Enterprise Identifiers - https://datatracker.ietf.org/doc/draft-zundel-spice-glue-id/ - 10 min (Brent Zundel)
page: https://datatracker.ietf.org/doc/draft-zundel-spice-glue-id/ | materials: https://datatracker.ietf.org/meeting/122/session/spice
This specification establishes an IETF URN namespace for GLobal Unique Enterprise (GLUE) Identifiers. It also establishes an IETF URN namespace for identifiers defined by the IETF Secure Patterns for Internet CrEdentials (SPICE) working group. The GLUE URN namespace is within the SPICE URN namespace.

### OpenID Connect standard claims registration for CBOR Web Tokens
Draft: draft-maldant-spice-oidc-cwt · Working group: spice
Agenda: - OpenID Connect standard claims registration for CBOR Web Tokens - https://datatracker.ietf.org/doc/draft-maldant-spice-oidc-cwt/ - 5 min (Beltram Maldant)
page: https://datatracker.ietf.org/doc/draft-maldant-spice-oidc-cwt/ | materials: https://datatracker.ietf.org/meeting/122/session/spice
This document registers OpenId Connect standards claims already used in JSON Web Tokens for CBOR Web Tokens.

### A Public Key Service Provider for Verification in Multiple Issuers and Verifiers
Draft: draft-wang-spice-public-key-service-provider · Working group: spice
Agenda: - A Public Key Service Provider for Verification in Multiple Issuers and Verifiers - https://datatracker.ietf.org/doc/draft-wang-spice-public-key-service-provider/ - 5 min (Donghui Wang)
page: https://datatracker.ietf.org/doc/draft-wang-spice-public-key-service-provider/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spice-a-public-key-service-provider-for-verification-in-multiple-issuers-and-verifiers-00 | video: https://www.youtube.com/watch?v=HFA7cQvJTxU | materials: https://datatracker.ietf.org/meeting/122/session/spice
SPICE provides a selective disclosure mechanism of credentials from issuer. However, future network services may be built on the trust between multiple entities. Obtaining the public key of multiple issuers for a verifer from potential multiple sources can be complex. In this contribution, an optional public key service is proposed in SPICE architecture for the issue of obtaining the public keys of the issuers from multiple trusted entities. The basic function of public key service is proposed including public key registration, token verification, and a potential implementation such as the distributed ledger. We hope that the proposed contribution can be used as infomative for SPICE regarding to the token validation procedure.

### SPICE GLUE
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spice-spice-glue-00 | video: https://www.youtube.com/watch?v=HFA7cQvJTxU | materials: https://datatracker.ietf.org/meeting/122/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

### OIDC claims registration
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spice-sessa-oidc-claims-registration-00 | video: https://www.youtube.com/watch?v=HFA7cQvJTxU | materials: https://datatracker.ietf.org/meeting/122/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

## Working Group: spring

### Segment Routing over IPv6 (SRv6) Security Considerations
Draft: draft-ietf-spring-srv6-security · Working group: spring
Agenda: draft-ietf-spring-srv6-security
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-segment-routing-ipv6-security-considerations-00 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
Segment Routing over IPv6 (SRv6) is the instantiation of Segment Routing on the IPv6 data plane, using IPv6 addresses to identify segments. This document discusses security considerations in SRv6 networks, including the potential threats and the possible mitigation methods. The document does not define any new security protocols or extensions to existing protocols.

### Circuit Style Segment Routing Policies with Optimized SID List Depth
Draft: draft-karboubi-spring-sidlist-optimized-cs-sr · Working group: spring
Agenda: draft-karboubi-spring-sidlist-optimized-cs-sr
page: https://datatracker.ietf.org/doc/draft-karboubi-spring-sidlist-optimized-cs-sr/ | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
Service providers require delivery of circuit-style transport services in a segment routing based IP network. This document introduces a solution that supports circuit style segment routing policies that allows usage of optimized SID lists (i.e. SID List that may contain non-contiguous node SIDs as instructions) and describes mechanisms that would allow such encoding to still honor all the requirements of the circuit style policies notably traffic engineering and bandwidth requirements.

### Eligibility Concept in Segment Routing Policies
Draft: draft-karboubi-spring-sr-policy-eligibility · Working group: spring
Agenda: draft-karboubi-spring-sr-policy-eligibility
page: https://datatracker.ietf.org/doc/draft-karboubi-spring-sr-policy-eligibility/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-eligibility-concept-in-sr-policies-00 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
Segment Routing (SR) introduces new challenges for pinning candidate paths on their intended paths (the path the PCE computed based on provided intent and may have made bandwidth reservations on). The actual path through a network can change or no longer meet the required constraints if a SID list of an SR Policy candidate path is not fully expressed as a list of adjacency SIDs or when a change in the topology does happen. The introduction of the new candidate path eligibility concept permits a path to be signaled and established as operationally up, but controls whether the path is eligible to carry traffic, thus influencing its active state. The eligibility concept allows a system (operator, pce, headend, etc.) to set eligibility as false when path deviations may have occurred, or path constraints are no longer met for one or more SID lists of a candidate path and clear it when candidate path deviations are removed or constraints are met again.

### Flexible Candidate Path Selection of SR Policy
Draft: draft-liu-spring-sr-policy-flexible-path-selection · Working group: spring
Agenda: draft-liu-spring-sr-policy-flexible-path-selection
page: https://datatracker.ietf.org/doc/draft-liu-spring-sr-policy-flexible-path-selection/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-flexible-candidate-path-selection-of-sr-policy-00 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
This document describes a flexible method for selecting candidate Segment Routing (SR) policy paths. Based on the real-time resource usage and forwarding quality of candidate paths, the head node can perform dynamic path switching among multiple candidate paths in the SR policy.

### SR-MPLS Aggregation Segment
Draft: draft-decraene-spring-sr-mpls-aggregation-segment · Working group: spring
Agenda: draft-decraene-spring-sr-mpls-aggregation-segment
page: https://datatracker.ietf.org/doc/draft-decraene-spring-sr-mpls-aggregation-segment/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-6-sr-mpls-aggregation-segment-01 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
One of the key features of IP that has helped IP Routing to scale is aggregation of IP prefixes. This is made possible with longest-match lookup in IP forwarding. Contrary to this, MPLS forwarding works on exact match on MPLS labels. This poses a challenge in aggregation of IP prefixes when the forwarding is based on the MPLS labels associated with those IP prefixes. This document introduces an Aggregation Segment for Segment Routing with MPLS data plane which can be used to aggregate IP prefixes along with their SR Prefix Segments. Aggregation Segments enable aggregation of IP prefixes to be performed at border routers to improve scalability of MPLS networks.

### SRv6 SFC Architecture with SR-aware Functions
Draft: draft-watal-spring-srv6-sfc-sr-aware-functions · Working group: spring
Agenda: draft-watal-spring-srv6-sfc-sr-aware-functions
page: https://datatracker.ietf.org/doc/draft-watal-spring-srv6-sfc-sr-aware-functions/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-srv6-sfc-architecture-with-sr-aware-functions-01 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
This document describes the architecture of Segment Routing over IPv6 (SRv6) Service Function Chaining (SFC) with SR-aware functions. This architecture provides the following benefits: * Comprehensive Management: a centralized controller for SFC, handling SR Policy, link-state, and network metrics. * Simplicity: no SFC proxies, which reduces the number of nodes and address resource consumption. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Source Packet Routing in Networking Working Group mailing list (spring@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/spring/. Source for this draft and an issue tracker can be found at https://github.com/watal.

### Advertise SRv6 Locator Information by IPv6 Neighbor Discovery
Draft: draft-gong-spring-nd-advertise-srv6-locator · Working group: spring
Agenda: draft-gong-spring-nd-advertise-srv6-locator
page: https://datatracker.ietf.org/doc/draft-gong-spring-nd-advertise-srv6-locator/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-advertise-srv6-locator-information-by-ipv6-neighbor-discovery-00 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
In an SRv6 network, each SRv6 segment endpoint has at least one SRv6 Locator. Through the SRv6 locator routes, other SRv6 segment nodes can steer traffic to that node. This document describes a method for an SRv6 endpoint (e.g., a host or a customer provider edge (CPE)) to advertise its SRv6 locator to a neighboring SRv6-aware router using extensions to the IPv6 Neighbor Discovery (ND) protocol. This approach eliminates the need to run a full routing protocol stack on simple endpoints, facilitating SRv6 deployment in controlled, trusted domains such as data centers and managed access networks.

### SRv6 Path Verification
Draft: draft-yang-spring-srv6-verification · Working group: spring
Agenda: draft-yang-spring-srv6-verification
page: https://datatracker.ietf.org/doc/draft-yang-spring-srv6-verification/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-srv6-path-verification-01 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. However, we have also observed that SRv6 is beginning to extend toward customer site devices, e.g., SD-WAN and enterprise network deployments. Both of the scenarios can be deployed in third-party clouds or at customer sites. This introduces certain security risks, such as packet injection and path manipulation attacks. Section 6 of [I-D.draft-ietf-spring-srv6-security] identifies these risks as well, including Section 6.2.1 on Modification Attacks and Section 6.2.3 on Packet Insertion. This proposal mitigates these risks by enhancing the HMAC mechanism defined in [RFC8754].

### Benchmarking Methodology for Segment Routing (SR) Forwarding
Draft: draft-ietf-bmwg-sr-bench-meth · Working group: spring
Agenda: draft-ietf-bmwg-sr-bench-meth
page: https://datatracker.ietf.org/doc/draft-ietf-bmwg-sr-bench-meth/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-benchmarking-methodology-for-segment-routing-updated-slides-00 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
This document defines a methodology for benchmarking Segment Routing (SR) forwarding performance for Segment Routing over IPv6 (SRv6) and MPLS (SR-MPLS).

### Export of Path Segment Identifier Information in IPFIX
Draft: draft-liu-opsawg-ipfix-path-segment · Working group: spring
Agenda: draft-liu-opsawg-ipfix-path-segment
page: https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-path-segment/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-export-of-path-segment-identifier-information-in-ipfix-01 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
This document introduces new IPFIX Information Elements to identify the Path Segment Identifier(PSID)s for SR-MPLS and SRv6 paths identification.

### CS-SR Policies with Optimized SID List Depth
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-spring-cs-sr-policies-with-optimized-sid-list-depth-00 | video: https://www.youtube.com/watch?v=jZy7g1U8GHU | materials: https://datatracker.ietf.org/meeting/122/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

## Working Group: srv6ops

### SRv6 Deployment and Operation Problem Summary
Draft: draft-liu-srv6ops-problem-summary · Working group: srv6ops
Agenda: draft-liu-srv6ops-problem-summary
page: https://datatracker.ietf.org/doc/draft-liu-srv6ops-problem-summary/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-srv6-deployment-and-operation-problem-summary-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
This document aims to provide a concise overview of the common problems encountered during SRv6 deployment and operation, which provides foundations for further work, including for example of potential solutions and best practices to navigate deployment.

### SRv6 Deployment Options
Draft: draft-mcbride-srv6ops-srv6-deployment · Working group: srv6ops
Agenda: draft-mcbride-srv6ops-srv6-deployment
page: https://datatracker.ietf.org/doc/draft-mcbride-srv6ops-srv6-deployment/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-32-deployment-options-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
When deciding to migrate a network from MPLS/SR-MPLS to SRv6, common questions involve how to go about performing the migration, what's the least amount of impact to an existing network and what existing techniques are available. This document presents various options for networks being migrated from MPLS/SR-MPLS to SRv6.

### IPv6 Address Assignment for SRv6
Draft: draft-liu-srv6ops-sid-address-assignment · Working group: srv6ops
Agenda: draft-liu-srv6ops-sid-address-assignment
page: https://datatracker.ietf.org/doc/draft-liu-srv6ops-sid-address-assignment/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-ipv6-address-assignment-for-srv6-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
This document provides detailed SRv6 SID assignment considerations, which could be a comprehensive guide for optimizing SRv6 SID allocation in diverse deployment scenarios.

### SID Space (5f00::/16) Inter-domain Addressing Recommendations
Draft: draft-eknb-srv6ops-interdomain-sidspace · Working group: srv6ops
Agenda: draft-eknb-srv6ops-interdomain-sidspace
page: https://datatracker.ietf.org/doc/draft-eknb-srv6ops-interdomain-sidspace/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-sid-space-experiment-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
This specification recommends a specific structured use of the SRv6 SIDs prefix in support of Inter-Domain SRv6 networks. The core of the proposal is to structure the address space by Autonomous System Number (ASN). Use of this proposed structure is entirely voluntary. Voluntary use of this structure aids SRv6 operations while preserving the ability to use this prefix across cooperating SRv6 domains, but not across the general Internet.

### Operational Guidance for Protection Mechanisms in SRv6 Networks
Draft: draft-liu-srv6ops-sr-protection · Working group: srv6ops
Agenda: draft-liu-srv6ops-sr-protection
page: https://datatracker.ietf.org/doc/draft-liu-srv6ops-sr-protection/ | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
This document describes the Operational Guidance for protection of Segment Routing Over IPv6 (SRv6) networks.

### Introduction
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-intro-01 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 @ Turkcell
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-21-srv6-turkcell-01 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 Practice in China Telecom
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-22-srv6-practice-in-china-telecom-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Benchmarking Methodolog
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-benchmarking-methodology-for-segment-routing-updated-slides-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Best Practices for Protection of SRv6 Networks
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-srv6ops-36-best-practices-for-protection-of-srv6-networks-00 | video: https://www.youtube.com/watch?v=2yzDrQEdAXU | materials: https://datatracker.ietf.org/meeting/122/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

## Working Group: tcpm

### Proportional Rate Reduction
Draft: draft-ietf-tcpm-prr-rfc6937bis · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-prr-rfc6937bis-13
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-prr-rfc6937bis/ | video: https://www.youtube.com/watch?v=QcT5sHT8umw | materials: https://datatracker.ietf.org/meeting/122/session/tcpm
This document specifies a standards-track version of the Proportional Rate Reduction (PRR) algorithm that obsoletes the experimental version described in RFC6937. PRR regulates the amount of data sent by TCP or other transport protocols during fast recovery. PRR accurately regulates the actual flight size through recovery such that at the end of recovery it will be as close as possible to the slow start threshold (ssthresh), as determined by the congestion control algorithm.

### TCP ACK Rate Request Option
Draft: draft-ietf-tcpm-ack-rate-request · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-ack-rate-request-07
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-ack-rate-request/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tcpm-tcp-ack-rate-request-tarr-option-00 | video: https://www.youtube.com/watch?v=QcT5sHT8umw | materials: https://datatracker.ietf.org/meeting/122/session/tcpm
TCP Delayed Acknowledgments (ACKs) is a widely deployed mechanism that allows reducing protocol overhead in many scenarios. However, Delayed ACKs may also contribute to suboptimal performance. When a relatively large congestion window (cwnd) can be used, less frequent ACKs may be desirable. On the other hand, in relatively small cwnd scenarios, eliciting an immediate ACK may avoid unnecessary delays that may be incurred by the Delayed ACKs mechanism. This document specifies the TCP ACK Rate Request (TARR) option. This option allows a sender to request the ACK rate to be used by a receiver, and it also allows to request immediate ACKs from a receiver.

### TCP RST Diagnostic Payload
Draft: draft-boucadair-tcpm-rst-diagnostic-payload · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-boucadair-tcpm-rst-diagnostic-payload-11
page: https://datatracker.ietf.org/doc/draft-boucadair-tcpm-rst-diagnostic-payload/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tcpm-tcp-rst-diagnostic-payload-00 | video: https://www.youtube.com/watch?v=QcT5sHT8umw | materials: https://datatracker.ietf.org/meeting/122/session/tcpm
This document specifies an experimental diagnostic payload format returned in TCP RST segments. Such payloads are used to share with an endpoint the reasons for which a TCP connection has been reset. Sharing this information is meant to ease diagnostic and troubleshooting. This specification builds on provisions that are already present in RFC 9293 "Transmission Control Protocol (TCP)". As such, this document does not require any change to RFC 9293.

### prr
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tcpm-prr-00 | video: https://www.youtube.com/watch?v=QcT5sHT8umw | materials: https://datatracker.ietf.org/meeting/122/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### IETF 122 Stuart Cheshire Source Buffer Management
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tcpm-ietf-122-stuart-cheshire-source-buffer-management-00 | video: https://www.youtube.com/watch?v=QcT5sHT8umw | materials: https://datatracker.ietf.org/meeting/122/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### close
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tcpm-close-00 | video: https://www.youtube.com/watch?v=QcT5sHT8umw | materials: https://datatracker.ietf.org/meeting/122/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

## Working Group: tls

### A Password Authenticated Key Exchange Extension for TLS 1.3
Draft: draft-bmw-tls-pake13 · Working group: tls
Agenda: -draft-bmw-tls-pake13 Chris Wood
page: https://datatracker.ietf.org/doc/draft-bmw-tls-pake13/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-draft-bmw-tls-pake13-01-rev1-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
The pre-shared key mechanism available in TLS 1.3 is not suitable for usage with low-entropy keys, such as passwords entered by users. This document describes an extension that enables the use of password-authenticated key exchange protocols with TLS 1.3.

### Post-Handshake Authentication via PAKE for TLS 1.3
Draft: draft-guo-pake-pha-tls · Working group: tls
Agenda: -draft-guo-pake-pha-tls Liang Xia
page: https://datatracker.ietf.org/doc/draft-guo-pake-pha-tls/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-post-handshake-authentication-via-pake-for-tls-13-01 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
This document provides a mechanism that uses password-authenticated key exchange (PAKE) as a post-handshake authentication for TLS 1.3, and that supports PAKE algorithms negotiation and optional channel binding.

### Request mTLS
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-request-mtls-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### FATT Report: -rfc8773bis
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-fatt-report-rfc8773bis-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Trust Anchor IDs
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-trust-anchor-ids-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Identity Crisis
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-identity-crisis-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### ECH Public Names
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-ech-public-names-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Implicit ECH
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-implicit-ech-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Anonymity Sets in ECH
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-anonymity-sets-in-ech-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### TLS 1.3 PAKE authentication Extension
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tls-tls-13-pake-authentication-extension-00 | video: https://www.youtube.com/watch?v=bQ-Bz60AppI | materials: https://datatracker.ietf.org/meeting/122/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

## Working Group: tsvwg

### Datagram PLPMTUD for UDP Options
Draft: draft-ietf-tsvwg-udp-options-dplpmtud · Working group: tsvwg
Agenda: draft-ietf-tsvwg-udp-options-dplpmtud Shepherd: Marten
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-udp-options-dplpmtud/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document specifies how a UDP Options sender implements Datagram Packetization Layer Path Maximum Transmission Unit Discovery (DPLPMTUD) as a robust method for Path Maximum Transmission Unit discovery. This method uses the UDP Options packetization layer. It allows an application to discover the largest size of datagram that can be sent across a network path. It also provides a way to allow the application to periodically verify the current maximum packet size supported by a path and to update this when required.

### DCCP Extensions for Multipath Operation with Multiple Addresses
Draft: draft-ietf-tsvwg-multipath-dccp · Working group: tsvwg
Agenda: draft-ietf-tsvwg-multipath-dccp Shepherd: Gorry
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-multipath-dccp/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Datagram Congestion Control Protocol (DCCP) communications, as defined in RFC 4340, are inherently restricted to a single path per connection, despite the availability of multiple network paths between peers. The ability to utilize multiple paths simultaneously for a DCCP session can enhance network resource utilization, improve throughput, and increase resilience to network failures, ultimately enhancing the user experience. Use cases for Multipath DCCP (MP-DCCP) include mobile devices (e.g., handsets, vehicles) and residential home gateways that maintain simultaneous connections to distinct network types, such as cellular and Wireless Local Area Networks (WLANs) or cellular and fixed access networks. Compared to existing multipath transport protocols, such as Multipath TCP (MPTCP), MP-DCCP is particularly suited for latency- sensitive applications with varying requirements for reliability and in-order delivery. This document specifies a set of protocol extensions to DCCP that enable multipath operations. These extensions maintain the same service model as DCCP while introducing mechanisms to establish and utilize multiple concurrent DCCP flows across different network paths.

### Transport Options for UDP
Draft: draft-ietf-tsvwg-udp-options · Working group: tsvwg
Agenda: draft-ietf-tsvwg-udp-options Shepherd: Gorry
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-udp-options/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Transport protocols are extended through the use of transport header options. This document updates RFC 768 (UDP) by indicating the location, syntax, and semantics for UDP transport layer options within the surplus area after the end of the UDP user data but before the end of the IP datagram.

### A Non-Queue-Building Per-Hop Behavior (NQB PHB) for Differentiated Services
Draft: draft-ietf-tsvwg-nqb · Working group: tsvwg
Agenda: draft-ietf-tsvwg-nqb Shepherd: Gorry (next: AD Review)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-nqb/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document specifies characteristics of a Non-Queue-Building Per- Hop Behavior (NQB PHB). The NQB PHB provides a shallow-buffered, best-effort service as a complement to a Default deep-buffered best- effort service for Internet services. The purpose of this NQB PHB is to provide a separate queue that enables smooth (i.e. non-bursty), low-data-rate, application-limited traffic microflows, which would ordinarily share a queue with bursty and capacity-seeking traffic, to avoid the delay, delay variation and loss caused by such traffic. This PHB is implemented without prioritization and can be implemented without rate policing, making it suitable for environments where the use of these features is restricted. The NQB PHB has been developed primarily for use by access network segments, where queuing delay and queuing loss caused by Queue-Building protocols are manifested, but its use is not limited to such segments. In particular, the application of NQB PHB to cable broadband links, Wi-Fi links, and mobile network radio and core segments are discussed. This document recommends a specific Differentiated Services Code Point (DSCP) to identify Non-Queue-Building microflows, and updates the RFC8325 guidance on mapping differentiated services (Diffserv) to IEEE 802.11 for this codepoint. [NOTE (to be removed by RFC-Editor): This document references an ISE submission draft (I-D.briscoe-docsis-q-protection) that is approved for publication as an RFC. This draft should be held for publication until the queue protection RFC can be referenced.]

### Convergence of Congestion Control from Retained State
Draft: draft-ietf-tsvwg-careful-resume · Working group: tsvwg
Agenda: draft-ietf-tsvwg-careful-resume Shepherd: Marten (next: WG Chair Follow-Up)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-careful-resume/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-sessa-33-qlog-for-careful-resume-01 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document specifies a cautious method for Internet transports that enables fast startup of congestion control for a wide range of connections, known as "Careful Resume". It reuses a set of computed congestion control parameters that are based on previously observed path characteristics between the same pair of transport endpoints. These parameters are saved, allowing them to be later used to modify the congestion control behaviour of a subsequent connection. It describes assumptions and defines requirements for how a sender utilises these parameters to provide opportunities for a connection to more rapidly get up to speed and rapidly utilise available capacity. It discusses how use of this method impacts the capacity at a shared network bottleneck and the safe response that is needed after any indication that the new rate is inappropriate.

### User Ports and Port Identifiers for Experiments
Draft: draft-ietf-tsvwg-usr-exp · Working group: tsvwg
Agenda: draft-ietf-tsvwg-usr-exp Shepherd: David (next: Shepherd Writeup)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-usr-exp/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-sessa-12-wglc-tsvwg-usr-exp-00 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document defines user ports for experiments using transport protocols and the use of experiment identifiers to enable shared use of these ports. It updates RFC 4727 to recommend the use of these experimental identifiers for the system ports for experiments in the same manner.

### Configuring UDP Sockets for ECN for Common Platforms
Draft: draft-ietf-tsvwg-udp-ecn · Working group: tsvwg
Agenda: draft-ietf-tsvwg-udp-ecn
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-udp-ecn/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-udp-ecn-00 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Explicit Congestion Notification (ECN) applies to all transport protocols in principle. However, it had limited deployment for UDP until QUIC became widely adopted. As a result, documentation of UDP socket APIs for ECN on various platforms is sparse. This document records the results of experimenting with these APIs in order to get ECN working on UDP for Chromium on Apple, Linux, and Windows platforms. This document provides a snapshot of ECN state of affairs as supported by these platforms at the time of writing. Readers should refer to the documentations of the various platforms for an up-to- date information on the matter.

### Operational Guidance on Coexistence with Classic ECN during L4S Deployment
Draft: draft-ietf-tsvwg-l4sops · Working group: tsvwg
Agenda: draft-ietf-tsvwg-l4sops
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document provides guidance in order to ensure successful deployment of Low Latency Low Loss Scalable throughput (L4S) in the Internet. Other L4S documents provide guidance for running an L4S experiment, but this document is focused solely on potential interactions between L4S flows and flows using the original ('Classic') ECN over a Classic ECN bottleneck. The document discusses the potential outcomes of these interactions, describes mechanisms to detect the presence of Classic ECN bottlenecks, and identifies opportunities to prevent and/or detect and resolve fairness problems in such networks. This guidance is aimed at operators of end-systems, operators of networks, and researchers.

### 5QI to DiffServ DSCP Mapping Example for Enforcement of 5G End-to-End Network Slice QoS
Draft: draft-cbs-teas-5qi-to-dscp-mapping · Working group: tsvwg
Agenda: draft-cbs-teas-5qi-to-dscp-mapping
page: https://datatracker.ietf.org/doc/draft-cbs-teas-5qi-to-dscp-mapping/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
5G End-to-End Network Slice QoS is an essential aspect of network slicing, as described in both IETF drafts and the 3GPP specifications. Network slicing allows for the creation of multiple logical networks on top of a shared physical infrastructure, tailored to support specific use cases or services. The primary goal of QoS in network slicing is to ensure that the specific performance requirements of each slice are met, including latency, reliability, and throughput.

### IKEv2 Link Maximum Atomic Packet and Packet Too Big Notification Extension
Draft: draft-liu-ipsecme-ikev2-mtu-dect · Working group: tsvwg
Agenda: draft-liu-ipsecme-ikev2-mtu-dect
page: https://datatracker.ietf.org/doc/draft-liu-ipsecme-ikev2-mtu-dect/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-ikev2-link-maximum-atomic-packet-and-packet-too-big-notification-extension-00 | video: https://www.youtube.com/watch?v=8BAV1DrgtnM | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document defines the IKEv2 Link Maximum Atomic Packet and Packet Too Big Extension to limit reassembly operations being performed by the egress security gateway. This extension enables an egress security gateway to notify its ingress counterpart that fragmentation is happening or that the received (and potentially reassembled) ESP packet is too big and thus cannot be decrypted. In both cases, the egress node provides Maximum Transmission Unit (MTU) information. Such information enables the ingress node to configure appropriately its Tunnel Maximum Transmission Unit - also designated as MTU or Tunnel MTU (TMTU) - to prevent fragmentation or too big packets to be transmitted.

### Proposal for Updates to Guidance on Packet Reordering
Draft: draft-white-intarea-reordering · Working group: tsvwg
Agenda: draft-white-intarea-reordering (to be presented in INTAREA)
page: https://datatracker.ietf.org/doc/draft-white-intarea-reordering/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Several link technology standards mandate that equipment guarantee in-order delivery of layer 2 frames, apparently due to a belief that this is required by higher layer protocols. To meet this requirement they implement a "resequencing" operation to restore the original packet order. This can introduce delays that result in net degradation of performance. Modern TCP and QUIC implementations support features that significantly improve their tolerance to out- of-order delivery. This draft is intended to provide new information for layer 2 technology standards regarding the need to assure in- order delivery to support IETF protocols.

### Quic Logging for Convergence of Congestion Control from Retained State
Draft: draft-custura-tsvwg-careful-resume-qlog · Working group: tsvwg
Agenda: draft-custura-tsvwg-careful-resume-qlog
page: https://datatracker.ietf.org/doc/draft-custura-tsvwg-careful-resume-qlog/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document specifies a logging format for a cautious method for Careful Resume when using the IETF quic transport protocol. It defines the logging format for qlog.

### Datagram Transport Layer Security (DTLS) over Stream Control Transmission Protocol (SCTP)
Draft: draft-ietf-tsvwg-dtls-over-sctp-bis · Working group: tsvwg
Agenda: draft-ietf-tsvwg-dtls-over-sctp-bis
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-dtls-over-sctp-bis/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-dtls-for-sctp-01 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document describes the usage of the Datagram Transport Layer Security (DTLS) protocol to protect user messages sent over the Stream Control Transmission Protocol (SCTP). It is an improved alternative to the existing RFC 6083. DTLS over SCTP provides mutual authentication, confidentiality, integrity protection, and partial replay protection for applications that use SCTP as their transport protocol and allows client/server applications to communicate in a way that is designed to give communications privacy and to prevent eavesdropping and detect tampering or message forgery. Applications using DTLS over SCTP can use almost all transport features provided by SCTP and its extensions. This document is an improved alternative to RFC 6083 and removes the 16 kbytes limitation on protected user message size by defining a secure user message fragmentation so that multiple DTLS records can be used to protect a single user message. It further contains a large number of security fixes and improvements. It updates the DTLS versions and SCTP-AUTH HMAC algorithms to use. It mitigates reflection attacks of data and control chunks and replay attacks of data chunks. It simplifies secure implementation by some stricter requirements on the establishment procedures as well as rekeying to align with zero trust principles.

### Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm
Draft: draft-tahiliani-tsvwg-fq-pie · Working group: tsvwg
Agenda: draft-tahiliani-tsvwg-fq-pie
page: https://datatracker.ietf.org/doc/draft-tahiliani-tsvwg-fq-pie/ | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
This document presents Flow Queue Proportional Integral controller Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue Management (AQM) algorithm to isolate flows and tackle the problem of bufferbloat. FQ-PIE uses hashing to classify incoming packets into different queues and provide flow isolation. Packets are dequeued by using a variant of the round robin scheduler. Each such flow is managed by the PIE algorithm to maintain high link utilization while controlling the queue delay to a target value.

### Controlling IP Fragmentation on Common Platforms
Draft: draft-seemann-tsvwg-udp-fragmentation · Working group: tsvwg
Agenda: draft-seemann-tsvwg-udp-fragmentation
page: https://datatracker.ietf.org/doc/draft-seemann-tsvwg-udp-fragmentation/ | slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-udp-fragmentation-00 | video: https://www.youtube.com/watch?v=8BAV1DrgtnM | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
When performing Path MTU Discovery (PMTUD) over UDP, applications must prevent fragmentation of UDP datagrams both by the sender's kernel and during network transit. This document provides guidance for implementers on configuring socket options to prevent fragmentation of IPv4 and IPv6 packets across commonly used platforms.

### 3.2: Observed ECN Codepoints (Martin Duke)
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-duke-observed-ecn-codepoints-00 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### Jason Livingood: Update on Deployment
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-41-jason-livingood-update-on-deployment-00 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### L4S Operational Guidance
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-sessa-42-l4s-operational-guidance-00 | video: https://www.youtube.com/watch?v=c3BOUmDE1lU | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### Mohit P. Tahiliani: Flow Queue
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-sessb-71-mohit-p-tahiliani-flow-queue-00 | video: https://www.youtube.com/watch?v=8BAV1DrgtnM | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### TCP REPLENISH TIME / Source Buffer Management
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-sessb-73-tcp-replenish-time-source-buffer-management-01 | video: https://www.youtube.com/watch?v=8BAV1DrgtnM | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### 5QI to DiffServ DSCP Mapping
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-75-5qi-to-diffserv-dscp-mapping-00 | video: https://www.youtube.com/watch?v=8BAV1DrgtnM | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### STAMP Extension for DSCP and ECN Traversal Measurement
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-tsvwg-sessb-8-stamp-extension-for-dscp-and-ecn-traversal-measurement-00 | video: https://www.youtube.com/watch?v=8BAV1DrgtnM | materials: https://datatracker.ietf.org/meeting/122/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

## Working Group: v6ops

### Tommy Jensen - CLAT Recommendations
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-v6ops-clat-recommendations-00 | video: https://www.youtube.com/watch?v=QHHnTFGw4-4 | materials: https://datatracker.ietf.org/meeting/122/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Chongfeng - Framework for Multi-domain IPv6-only Underlay  Network and IPv4-as-a-Service
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-v6ops-framework-for-multi-domain-ipv6-only-underlay-network-and-ipv4-as-a-service-00 | video: https://www.youtube.com/watch?v=QHHnTFGw4-4 | materials: https://datatracker.ietf.org/meeting/122/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jen Linkova - Prefer use of RFC8781 for Discovery of IPv6 Prefix Used for IPv6 Address Synthesis
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-v6ops-prefer-use-of-rfc8781-for-discovery-of-ipv6-prefix-used-for-ipv6-address-synthesis-00 | video: https://www.youtube.com/watch?v=QHHnTFGw4-4 | materials: https://datatracker.ietf.org/meeting/122/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jen Linkova - Using Dummy IPv4 Address and Node Identification Extensions for IP/ICMP translators (XLATs)
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-v6ops-using-dummy-ipv4-address-and-node-identification-extensions-for-ipicmp-translators-xlats-00 | video: https://www.youtube.com/watch?v=QHHnTFGw4-4 | materials: https://datatracker.ietf.org/meeting/122/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Fernando Gont - draft-gont-v6ops-multi-ipv6
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-v6ops-fernando-gont-draft-gont-v6ops-multi-ipv6-00 | video: https://www.youtube.com/watch?v=QHHnTFGw4-4 | materials: https://datatracker.ietf.org/meeting/122/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### IPv6 Network Deployment Monitoring and Analysis
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-v6ops-ipv6-network-deployment-monitoring-and-analysis-00 | video: https://www.youtube.com/watch?v=QHHnTFGw4-4 | materials: https://datatracker.ietf.org/meeting/122/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

## Working Group: wimse

### WIMSE architecture
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-wimse-architecture-00 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload to workload protocol
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-workload-to-workload-protocol-00 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload Identity Practices
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-workload-identity-practices-draft-slides-00 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Credential Exchange
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-credential-exchange-00 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Identity Crisis
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-identity-crisis-00 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Trustworthy Workload Identity [TWI]
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-trustworthy-workload-identity-twi-00 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE impact on Data residency requirements for handling sensitive data
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/122/materials/slides-122-wimse-wimse-impact-on-data-residency-requirements-for-handling-sensitive-data-01 | video: https://www.youtube.com/watch?v=7FUaIYiGzQs | materials: https://datatracker.ietf.org/meeting/122/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

