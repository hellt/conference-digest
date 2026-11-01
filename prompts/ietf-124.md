>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-124. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-124.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-124.md
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

Below is the program for IETF 124 (Montreal) (standards). Read it and produce a digest
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
conference: IETF 124 (Montreal)
type: standards
source_url: https://datatracker.ietf.org/meeting/124/agenda.json
generated: 2026-11-01
registry_key: ietf-124
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Working Group: 6man

### Clarifying SRv6 SID List Processing
Draft: draft-ietf-6man-sidlist-clarification · Working group: 6man
Agenda: draft-ietf-6man-sidlist-clarification
page: https://datatracker.ietf.org/doc/draft-ietf-6man-sidlist-clarification/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-clarifying-srv6-sid-list-processing-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
Segment Routing over IPv6 (SRv6) is the instantiation of Segment Routing (SR) on the IPv6 data plane. Segments are indicated by Segment Identifiers (SIDs). SRv6 utilizes the Segment Routing Header (SRH), an IPv6 extension header, that includes a SID list indicating the sequence of segments and any additional processing to be performed. This document updates RFC 8754 by clarifying the processing of SID list entries. It does not change any elements of the SRv6 architecture.

### Carrying Network Resource (NR) related Information in IPv6 Extension Headers
Draft: draft-ietf-6man-enhanced-vpn-vtn-id · Working group: 6man
Agenda: draft-ietf-6man-enhanced-vpn-vtn-id
page: https://datatracker.ietf.org/doc/draft-ietf-6man-enhanced-vpn-vtn-id/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-carrying-network-resource-information-in-ipv6-extension-header-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
Virtual Private Networks (VPNs) provide different customers with logically separated connectivity over a common network infrastructure. With the introduction of 5G and also in some existing network scenarios, some customers may require network connectivity services with features that are more advanced compared to conventional VPN services. Such kind of network service is called enhanced VPNs. Enhanced VPNs can be used, for example, to deliver network slice services. A Network Resource Partition (NRP) is a subset of the network resources and associated policies on each of a connected set of links in the underlay network. An NRP may be used as the underlay to support one or a group of enhanced VPN services. For packet forwarding within a specific NRP, some fields in the data packet (these fields are called the NRP Selector) are used to identify the NRP to which the packet belongs. By identifying a packet with an NRP, NRP-specific processing can be performed on each node along the forwarding path in the NRP. This document specifies a new IPv6 Hop-by-Hop option to carry Network Resource related information in data packets. The new option is called the Network Resource (NR) Option. It can be used to carry an identifier of the NRP Selector, but it is designed to also be able to carry general information about network resource semantics and functions.

### YANG Data Model for IPv6 Neighbor Discovery
Draft: draft-ietf-6man-ipv6-neighbor-discovery-yang · Working group: 6man
Agenda: draft-ietf-6man-ipv6-neighbor-discovery-yang
page: https://datatracker.ietf.org/doc/draft-ietf-6man-ipv6-neighbor-discovery-yang/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-yang-data-model-for-ipv6-neighbor-discovery-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
This document defines a YANG data model to configure and manage IPv6 Neighbor Discovery (ND) and related functions, including IPv6 address resolution, redirect function, proxy Neighbor Advertisement, Neighbor Unreachability Detection (NUD), Duplicate Address Detection (DAD), and Enhanced Duplicate Address Detection.

### IPv6 Query for Enabled In-situ OAM Capabilities
Draft: draft-ietf-6man-icmpv6-ioam-conf-state · Working group: 6man
Agenda: draft-ietf-6man-icmpv6-ioam-conf-state ,
page: https://datatracker.ietf.org/doc/draft-ietf-6man-icmpv6-ioam-conf-state/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-ipv6-query-for-enabled-in-situ-oam-capabilities-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
This document describes the application of the mechanism of discovering In-situ OAM (IOAM) capabilities, described in RFC 9359 "Echo Request/Reply for Enabled In Situ OAM (IOAM) Capabilities", in IPv6 networks. IPv6 Node IOAM Query functionality uses the ICMPv6 Query messages, allowing the IOAM encapsulating node to discover the enabled IOAM capabilities of each IOAM transit and IOAM decapsulating node.

### IPv6 Node Requirements
Draft: draft-ietf-6man-rfc8504-bis · Working group: 6man
Agenda: draft-ietf-6man-rfc8504-bis
page: https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-ipv6-node-requirements-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
This document defines requirements for IPv6 nodes. It is expected that IPv6 will be deployed in a wide range of devices and situations. Specifying the requirements for IPv6 nodes allows IPv6 to function well and interoperate in a large number of situations and deployments. This document obsoletes RFC 8504, and in turn RFC 6434 and its predecessor, RFC 4294.

### Sub-Link Scoped IPv6 Multicast Addressing
Draft: draft-equinox-6man-sub-link-scope-multicast · Working group: 6man
Agenda: draft-equinox-6man-sub-link-scope-multicast
page: https://datatracker.ietf.org/doc/draft-equinox-6man-sub-link-scope-multicast/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-sub-link-scoped-ipv6-multicast-addressing-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
The IPv6 addressing architecture for multicast has the scope of a multicast group embedded in its address, with the smallest non- reserved scopes being interface-local and link-local, numbered 1 and 2. This document suggests the introduction of a scope inbetween these two, for use with lower-layer transport multicast that reaches parts of a link. Since there is no room to insert a scope value for this, a separate address block is used. A mapping for Ethernet as lower-layer transport is provided.

### Compact Routing Header (CRH) Helper Option
Draft: draft-bonica-6man-crh-helper-opt · Working group: 6man
Agenda: draft-bonica-6man-crh-helper-opt
page: https://datatracker.ietf.org/doc/draft-bonica-6man-crh-helper-opt/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-compact-routing-header-crh-helper-option-00 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
This document introduces a new IPv6 Destination Option called the CRH Helper. The CRH Helper is used with the Compact Routing Header (CRH) [RFC 9631]. It contains information required to convert a CRH SID to the IPv6 address of a interface on a packet's delivery path. Because the CRH Helper contains this information, it eliminates the need for a CRH-FIB. It also eliminates the need for CRH-FIB support in the control plane. The CRH helper is useful in underlay networks, where all interfaces are numbered from a few /112 or /96 prefixes.

### Updates to DNS64 Functionality Advertisement for DNS RA Option
Draft: draft-ma-6man-ra-dns64-flag · Working group: 6man
Agenda: draft-ma-6man-ra-dns64-flag
page: https://datatracker.ietf.org/doc/draft-ma-6man-ra-dns64-flag/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-chenhao-ma-updates-to-dns64-functionality-advertisement-for-dns-ra-option-01 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
This document defines a new flag in the DNS RA Option to advertise the DNS64 functionality. This extension enables automatic configuration of DNS64 resolution, improving deployability in IPv6 transition scenarios.

### ICMP Error Handling in SRv6 based VPN Networks
Draft: draft-ali-6man-srv6-vpn-icmp-error-handling · Working group: 6man
Agenda: draft-ali-6man-srv6-vpn-icmp-error-handling
page: https://datatracker.ietf.org/doc/draft-ali-6man-srv6-vpn-icmp-error-handling/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-6man-draft-ali-6man-srv6-vpn-icmp-error-handling-01 | video: https://youtu.be/Vqqe-L6CQdw | materials: https://datatracker.ietf.org/meeting/124/session/6man
The document specifies procedures for handling ICMP error in SRv6-based Virtual Private Network (VPN).

## Working Group: acme

### Automated Certificate Management Environment (ACME) Delay-Tolerant Networking (DTN) Node ID Validation Extension
Draft: draft-ietf-acme-dtnnodeid · Working group: acme
Agenda: draft-ietf-acme-dtnnodeid
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dtnnodeid/ | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document specifies an extension to the Automated Certificate Management Environment (ACME) protocol which allows an ACME server to validate the Delay-Tolerant Networking (DTN) Node ID for an ACME client. A DTN Node ID is an identifier used in the Bundle Protocol (BP) to name a "singleton endpoint", one which is registered on a single BP node. The DTN Node ID is encoded as a certificate Subject Alternative Name (SAN) of type otherName with a name form of BundleEID and as an ACME Identifier type "bundleEID".

### ACME Integrations for Device Certificate Enrollment
Draft: draft-ietf-acme-integrations · Working group: acme
Agenda: draft-ietf-acme-integrations
page: https://datatracker.ietf.org/doc/draft-ietf-acme-integrations/ | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document outlines multiple advanced use cases and integrations that ACME facilitates without any modifications or enhancements required to the base ACME specification. The use cases include ACME integration with EST, BRSKI and TEAP.

### Automated Certificate Management Environment (ACME) Device Attestation Extension
Draft: draft-acme-device-attest · Working group: acme
Agenda: draft-acme-device-attest
page: https://datatracker.ietf.org/doc/draft-acme-device-attest/ | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document specifies new identifiers and a challenge for the Automated Certificate Management Environment (ACME) protocol which allows validating the identity of a device using attestation.

### Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation
Draft: draft-ietf-acme-dns-persist · Working group: acme
Agenda: draft-ietf-acme-dns-persist – Henry [15 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dns-persist/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-acme-dns-persist-00 | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document specifies "dns-persist-01", a new validation method for the Automated Certificate Management Environment (ACME) protocol. This method allows a Certification Authority (CA) to verify control over a domain by confirming the presence of a persistent DNS TXT record containing CA and account identification information. This method is particularly suited for environments where traditional challenge methods are impractical, such as multi-tenant hosting platforms, enterprise DNS environments, and IoT deployments. The validation method is designed with a strong focus on security and robustness, incorporating widely adopted industry best practices for persistent domain control validation. This design aims to make it suitable for Certification Authorities operating under various policy environments, including those that align with the CA/Browser Forum Baseline Requirements.

### Automated Certificate Management Environment (ACME) Profiles Extension
Draft: draft-ietf-acme-profiles · Working group: acme
Agenda: draft-ietf-acme-profiles – Aaron [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-acme-draft-ietf-acme-profiles-00-01 | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document defines how an ACME Server may offer a selection of different certificate profiles to ACME Clients, and how those clients may indicate which profile they want.

### Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge
Draft: draft-ietf-acme-dns-account-label · Working group: acme
Agenda: draft-ietf-acme-dns-account-label ??
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dns-account-label/ | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document outlines a new DNS-based challenge type for the ACME protocol that enables multiple independent systems to authorize a single domain name concurrently. By adding a unique label to the DNS validation record name, the dns-account-01 challenge avoids CNAME delegation conflicts inherent to the dns-01 challenge type. This is particularly valuable for multi-region or multi-cloud deployments that wish to rely upon DNS-based domain control validation and need to independently obtain certificates for the same domain.

### JWTClaimConstraints profile of ACME Authority Token
Draft: draft-wendt-acme-authority-token-jwtclaimcon · Working group: acme
Agenda: draft-wendt-acme-authority-token-jwtclaimcon – Chris [15 mins]
page: https://datatracker.ietf.org/doc/draft-wendt-acme-authority-token-jwtclaimcon/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-acme-jwtclaimsconstraints-authority-token-profile-00 | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document defines an authority token profile for handling the validation of JWTClaimConstraints and EnhancedJWTClaimConstraints. This profile follows the model established in Authority Token for the validation of TNAuthList but is specifically tailored for the JWTClaimConstraints certificate extensions. The profile enables validation and challenge processes necessary to support certificates containing both TNAuthList and JWTClaimConstraints, particularly in the context of Secure Telephone Identity (STI).

### Automated Certificate Management Environment (ACME) rats Identifier and Challenge Type
Draft: draft-liu-acme-rats · Working group: acme
Agenda: draft-liu-acme-rats – Peter [15 mins]
page: https://datatracker.ietf.org/doc/draft-liu-acme-rats/ | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document describes an approach where an ACME Server can challenge an ACME Client to provide a Remote Attestation Evidence or Remote Attestation Result in any format supported by the Conceptual Message Wrapper. The ACME Server can optionally challenge the Client for specific claims that it wishes attestation for.

### Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0
Draft: draft-demarco-acme-openid-federation · Working group: acme
Agenda: draft-demarco-acme-openid-federation – Tim [15 mins]
page: https://datatracker.ietf.org/doc/draft-demarco-acme-openid-federation/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-acme-draft-demarco-acme-openid-federation-01-00 | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
The Automatic Certificate Management Environment (ACME) protocol allows server operators to obtain TLS certificates for their websites, based on a demonstration of control over the website's domain via a fully-automated challenge/response protocol. OpenID Federation 1.0 defines how to build a trust infrastructure using a trusted third-party model. It uses a trust evaluation mechanism to attest to the possession of private keys, protocol specific metadata and miscellaneous administrative and technical information related to a specific entity. This document defines how X.509 certificates associated with a given OpenID Federation Entity can be issued by an X.509 Certification Authority through the ACME protocol to the organizations which are part of a federation built on top of OpenID Federation 1.0.

### Automated Certificate Management Environment (ACME) Profile Sets
Draft: draft-davidben-acme-profile-sets · Working group: acme
Agenda: draft-davidben-acme-profile-sets - DavidBen [15 mins]
page: https://datatracker.ietf.org/doc/draft-davidben-acme-profile-sets/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-acme-acme-profile-sets-00 | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
This document defines how an ACME Server may indicate collections of related certificate profiles to ACME Clients.

### ACME-RATS
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-acme-acme-rats-for-ietf-124-00 | video: https://youtu.be/agFEJPXX1XU | materials: https://datatracker.ietf.org/meeting/124/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

## Working Group: add

### DNS-Based Service Discovery for Encrypted DNS Services
Draft: draft-liu-add-dnssd-edns · Working group: add
Agenda: Multicast DNS-Based Service Discovery for Encrypted DNS Services draft-liu-add-dnssd-edns-00 15m
page: https://datatracker.ietf.org/doc/draft-liu-add-dnssd-edns/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-add-draft-liu-add-dnssd-edns-01-00 | video: https://youtu.be/pxNm4heT8wU | materials: https://datatracker.ietf.org/meeting/124/session/add
This document defines a DNS-Based Service Discovery (DNS-SD) mechanism for discovering encrypted DNS services in local networks. It specifies new service types (_dot._tcp, _doh._tcp, _doq._udp) and associated service parameters to enable zero-configuration discovery of DNS over TLS (DoT), DNS over HTTPS (DoH), and DNS over QUIC (DoQ) resolvers. This mechanism is defined for use with multicast DNS (mDNS), addressing critical privacy gaps in local networks while maintaining backward compatibility with RFC 6763. This document leverages SVCB and HTTPS resource records (RFC 9460) for parameter negotiation, with TXT records provided for compatibility with legacy implementations.

### PPP IPCP Extensions for Encrypted DNS Server Negotiation
Draft: draft-liu-add-ppp-edns-negotiation · Working group: add
Agenda: PPP IPCP Extensions for Encrypted DNS Server Negotiation draft-liu-add-ppp-edns-negotiation-00 15m
page: https://datatracker.ietf.org/doc/draft-liu-add-ppp-edns-negotiation/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-add-draft-liu-add-ppp-edns-negotiation-01-02 | video: https://youtu.be/pxNm4heT8wU | materials: https://datatracker.ietf.org/meeting/124/session/add
This document defines extensions to the Point-to-Point Protocol (PPP) Internet Protocol Control Protocol (IPCP) for negotiating encrypted DNS resolver configurations. Two IPCP Configuration Options are defined for primary and secondary encrypted DNS resolvers. Each option carries an Authentication Domain Name (ADN), an explicit list of resolver IP addresses, and Service Parameters (SvcParams) using the wire format defined by RFC 9460. The design supports DNS over TLS (DoT), DNS over HTTPS (DoH), and DNS over QUIC (DoQ), while maintaining coexistence with the plaintext DNS configuration mechanism defined by RFC 1877.

## Working Group: anima

### Constrained BRSKI (cBRSKI) and Join Proxy
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-01-constrained-brski-cbrski-and-join-proxy-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### BRSKI Discovery update
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-02-brski-discovery-update-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### RFC8366bis WGLC update
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-rfc8366bis-wglc-update-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### BRSKI Operational Considerations
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-brski-operational-considerations-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### constrained-grasp
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-05-constrained-grasp-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Communication Considerations for AI Agents in Network Devices
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-06-communication-considerations-for-ai-agents-in-network-devices-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Automatic Network Congestion Relief in GRASP
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-anima-automatic-network-congestion-relief-in-grasp-00 | video: https://youtu.be/LA3Trf9O7h4 | materials: https://datatracker.ietf.org/meeting/124/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

## Working Group: bess

### BGP link bandwidth extended community use cases
Draft: draft-ietf-bess-ebgp-dmz · Working group: bess
Agenda: draft-ietf-bess-ebgp-dmz-08 Stephane 10 17:15 - 17:25
page: https://datatracker.ietf.org/doc/draft-ietf-bess-ebgp-dmz/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-draft-ietf-bess-ebgp-dmz-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
BGP link bandwidth extended community provides a way to signal a value along with a BGP path that can be used to perform weighted load-balancing in multipath scenarios. This document details various use cases of the BGP link bandwidth extended community. It also describes local mechanisms to dynamically adjust the BGP link bandwidth value or the multipath weights based on different considerations.

### IPv4-Only and IPv6-Only PE Design DESIGN ALL SAFI
Draft: draft-ietf-bess-v4-v6-pe-all-safi · Working group: bess
Agenda: draft-ietf-bess-v4-v6-pe-all-safi Gyan Mishra 5 17:25 - 17:30
page: https://datatracker.ietf.org/doc/draft-ietf-bess-v4-v6-pe-all-safi/ | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
As Enterprises and Service Providers upgrade their brown field or green field MPLS/SR core to an IPv6 transport, Multiprotocol BGP (MP- BGP)now plays an important role in the transition of their Provider (P) core network as well as Provider Edge (PE) Inter-AS peering network from IPv4 to IPv6. Operators must have flexiblity to continue to support IPv4 customers when both the Core and Edge networks migrate to IPv6. As well as must be able to support IPv6 networks in cases where operators decide to remain on an IPv4 network or during transition. This document details the External BGP (eBGP) PE-PE Inter-AS and PE- CE Edge peering IPv4-Only PE design where both IPv4 and IPv6 all supported SAFI NLRI can be advertised over a single IPv4 peer and IPv6-Only PE Design where all supported SAFI NLRI can be advertised over a single IPv6 peer. This document also defines a new IPv4 BGP next hop encoding standard that uses an IPv4 address as the next hop and not an IPv4 mapped IPv6 address. This document also provides vendor specific test cases for the IPv4-Only peering design and IPv6-Only PE design as well as test results for the four major vendors stakeholders in the routing and switching indusrty, Cisco, Juniper, Nokia and Huawei. With the test results provided for the IPv6-Only Edge peering design, the goal is that all other vendors around the world that have not been tested will begin to adopt and implement the design.

### EVPN Multi-Active Multihoming
Draft: draft-zzhang-bess-evpn-multi-active-multihoming · Working group: bess
Agenda: draft-zzhang-bess-evpn-multi-active-multihoming-00 Jeffery 10 17:30 - 17:40
page: https://datatracker.ietf.org/doc/draft-zzhang-bess-evpn-multi-active-multihoming/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-evpn-multi-active-multihoming-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
EVPN supports All-Active and Single-Active multihoming, where either all multihoming PEs are active or only one is active. In some situations, it is desired to support Multi-Active with multiple yet not all active PEs. This document specifies the Multi-Active multihoming - some multihoming PEs are in All-Active mode while others are in Single-Active mode on the same multihoming Ethernet Segment, and ingress PEs load-balance to those in All-Active mode.

### OAM for EVPN over SRv6
Draft: draft-zl-bess-evpn-srv6-oam · Working group: bess
Agenda: draft-zl-bess-evpn-srv6-oam-00 Xiaoqiu 10 17:40 - 17:50
page: https://datatracker.ietf.org/doc/draft-zl-bess-evpn-srv6-oam/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-ietf124-bess-evpn-srv6-oam00-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
RFC 9489 describes Operation, Administration, and Maintenance (OAM) mechanisms for detecting data plane failures using Label Switched Path (LSP) Ping in MPLS-based Ethernet VPN (EVPN) networks. However, there is no effective OAM mechanism for detecting data plane failures in SRv6-based EVPN networks. This document proposals OAM mechanisms for SRv6-based EVPN networks.

### Ingress Replication BUM flag in VXLAN
Draft: draft-rabsaj-bess-evpn-vxlan-ir-bum · Working group: bess
Agenda: draft-rabsaj-bess-evpn-vxlan-ir-bum-00 Jorge Rabadan 5 17:50 - 17:55
page: https://datatracker.ietf.org/doc/draft-rabsaj-bess-evpn-vxlan-ir-bum/ | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
This document proposes the allocation of an “Ingress Replication BUM” flag in the VXLAN Flags IANA registry and defines its use in EVPN networks that employ VXLAN tunnels with ingress replication to forward broadcast, unknown and multicast traffic.

### EVPN Inter-Domain Option-B Solution
Draft: draft-rabadan-bess-evpn-inter-domain-opt-b · Working group: bess
Agenda: draft-rabadan-bess-evpn-inter-domain-opt-b-07 Jorge Rabadan 10 17:55 - 18:05
page: https://datatracker.ietf.org/doc/draft-rabadan-bess-evpn-inter-domain-opt-b/ | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
An EVPN Inter-Domain interconnect solution is required when two or more sites of the same Ethernet Virtual Private Network (EVPN) are connected to different IGP domains or Autonomous Systems (AS) and need to communicate. The Inter-Domain Option-B connectivity model is one of the most popular solutions for this type of EVPN connectivity. While several documents address specific aspects of this interconnect approach, none provide a comprehensive overview of how Inter-Domain Option-B connectivity affects EVPN procedures. This document examines the behavior of EVPN procedures in an Inter-Domain Option-B network and proposes solutions to the identified issues.

### Proxy MAC-IP Advertisement in EVPNs
Draft: draft-rbickhart-evpn-ip-mac-proxy-adv · Working group: bess
Agenda: draft-rbickhart-evpn-ip-mac-proxy-adv-04 Wen Lin 10 18:05 - 18:15
page: https://datatracker.ietf.org/doc/draft-rbickhart-evpn-ip-mac-proxy-adv/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-proxy-mac-ip-advertisement-in-evpn-01 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
This document specifies procedures for EVPN PEs connected to a common multihomed site to generate proxy EVPN MAC-IP advertisements on behalf of other PEs to facilitate preservation of ARP/ND state across link or node failures.

### SRv6 Anycast VPN Service
Draft: draft-liu-bess-srv6-anycast-vpn-service · Working group: bess
Agenda: draft-liu-bess-srv6-anycast-vpn-service Changwang 5 18:15 - 18:20
page: https://datatracker.ietf.org/doc/draft-liu-bess-srv6-anycast-vpn-service/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-srv6-anycast-vpn-servicedraft-liu-bess-srv6-anycast-vpn-service-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
In some multihoming SRv6 L3VPN and EVPN scenarios, there are requirements for the egress PE to advertise both unicast and anycast SRv6 Service SIDs for the same service. This document defines anycast flavor for SRv6 Service SIDs carried in BGP messages.

### Layer-3 Accessible EVPN Services
Draft: draft-wang-bess-l3-accessible-evpn · Working group: bess
Agenda: draft-wang-bess-l3-accessible-evpn Aijun 10 18:20 - 18:30
page: https://datatracker.ietf.org/doc/draft-wang-bess-l3-accessible-evpn/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-updates-on-the-layer-3-accessible-evpn-service-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
This draft describes layer-3 accessible EVPN service interfaces, which aim is to connect the layer 2 customers to one EVPN backbone, via the layer 3 network, and keep the traffic isolation among different layer 2 customers. It proposes to extend the VxLAN packet format to transfer the customer's Virtual Network Identifier(VNI) information, and also the related control plane extension.

### IETF 124 BESS WG IPv4 IPv6 ALL SAFI
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-ietf-124-bess-wg-ipv4-ipv6-all-safi-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### IETF124 BESS evpn-vxlan-ir-bum00v2
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-ietf124-bess-evpn-vxlan-ir-bum00v2-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### IETF124 BESS inter-domain-opt-b07v1
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-ietf124-bess-inter-domain-opt-b07v1-00 | video: https://youtu.be/4D1ZG26KiFw | materials: https://datatracker.ietf.org/meeting/124/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

## Working Group: cose

### Use of Hybrid Public-Key Encryption (HPKE) with CBOR Object Signing and Encryption (COSE)
Draft: draft-ietf-cose-hpke · Working group: cose
Agenda: [30 min] draft-ietf-cose-hpke - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-hpke/ | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
This specification defines hybrid public-key encryption (HPKE) for use with CBOR Object Signing and Encryption (COSE). HPKE offers a variant of public-key encryption of arbitrary-sized plaintexts for a recipient public key. HPKE is a general encryption framework utilizing an asymmetric key encapsulation mechanism (KEM), a key derivation function (KDF), and an Authenticated Encryption with Associated Data (AEAD) algorithm. This document defines the use of HPKE with COSE. Authentication for HPKE in COSE is provided by COSE-native security mechanisms or by the pre-shared key authenticated variant of HPKE.

### FN-DSA for JOSE and COSE
Draft: draft-ietf-cose-falcon · Working group: cose
Agenda: [10 min] draft-ietf-cose-falcon - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-falcon/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-fn-dsa-for-jose-and-cose-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
This document specifies JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 206 (expected to be published in late 2026 early 2027). It does not define new cryptographic primitives; rather, it specifies how existing FN-DSA mechanisms are serialized for use in JOSE and COSE. This document registers signature algorithms for JOSE and COSE, specifically FN-DSA-512 and FN-DSA-1024.

### SLH-DSA for JOSE and COSE
Draft: draft-ietf-cose-sphincs-plus · Working group: cose
Agenda: [10 min] draft-ietf-cose-sphincs-plus - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-sphincs-plus/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-slh-dsa-for-jose-and-cose-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
Digital signatures are used within JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) to protect the integrity and authenticity of messages, such as JSON Web Signatures and signed COSE structures. This document specifies JOSE and COSE serializations for the Stateless Hash-Based Digital Signature Standard (SLH-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 205. The conventions for the associated algorithm identifiers, signatures, public keys, and private keys are also specified.

### Barreto-Lynn-Scott Elliptic Curve Key Representations for JOSE and COSE
Draft: draft-ietf-cose-bls-key-representations · Working group: cose
Agenda: [10 min] draft-ietf-cose-bls-key-representations - Mike Jones
page: https://datatracker.ietf.org/doc/draft-ietf-cose-bls-key-representations/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-bls-elliptic-curve-key-representations-for-jose-and-cose-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
This specification defines how to represent cryptographic keys for the pairing-friendly elliptic curves known as Barreto-Lynn-Scott (BLS), for use with the key representation formats of JSON Web Key (JWK) and COSE (COSE_Key). Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/tplooker/draft-ietf-cose-bls-key-representations.

### Composite Token Claims
Draft: draft-lemmons-cose-composite-claims · Working group: cose
Agenda: [10 min] draft-lemmons-cose-composite-claims - Chris Lemmons
page: https://datatracker.ietf.org/doc/draft-lemmons-cose-composite-claims/ | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
Composite claims are claims for CBOR Web Tokens (CWTs) and JSON Web Tokens (JWTs) that define logical relationships between sets of claims. This document also defines a CWT representation of the "crit" (Critical) claim.

### Split Signing Algorithms for COSE
Draft: draft-lundberg-cose-two-party-signing-algs · Working group: cose
Agenda: [10 min] draft-lundberg-cose-two-party-signing-algs - Mike Jones
page: https://datatracker.ietf.org/doc/draft-lundberg-cose-two-party-signing-algs/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-split-signing-algorithms-for-cose-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
This specification defines COSE algorithm identifiers for negotiating how to split a signature algorithm between two cooperating parties. Typically the first party hashes the data to be signed and the second party finishes the signature over the hashed data. This is a common technique, useful for example when the signing private key is held in a smart card or similar hardware component with limited processing power and communication bandwidth. The resulting signatures are identical in structure to those computed by a single party, and can be verified using the same verification algorithm without additional steps to preprocess the signed data.

### Test Vectors for CBOR Encoded X.509 (C509) Certificates
Draft: draft-lspm-cose-c509-test-vectors · Working group: cose
Agenda: [10 min] draft-lspm-cose-c509-test-vectors - Göran Selander
page: https://datatracker.ietf.org/doc/draft-lspm-cose-c509-test-vectors/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-test-vectors-for-c509-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
This document contains examples of CBOR encoded X.509 (C509) certificates, certificate (signing) requests, and certificate request templates.

### Use of HPKE with COSE
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-use-of-hpke-with-cose-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

### Composition Claims
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-composition-claims-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

### AOB slides for registering more Keccak-based algorithms
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-cose-aob-slides-for-registering-more-keccak-based-algorithms-00 | video: https://youtu.be/5V3q1BexGrA | materials: https://datatracker.ietf.org/meeting/124/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

## Working Group: dnsop

### Operational Guidelines for DNS Transport in Mixed IPv4/IPv6 Environments
Draft: draft-ietf-dnsop-3901bis · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-3901bis/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-3901bis/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-draft-ietf-dnsop-3901bis-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document provides guidelines and documents Best Current Practice for operating authoritative DNS servers, recursive resolvers and stub resolvers in a mixed IPv4/IPv6 environment. This document recommends that both authoritative DNS servers and recursive resolvers support IPv4 and IPv6. It also provides guidance on how recursive DNS resolvers should select upstream DNS servers, including when IPv4-embedded IPv6 addresses are available. This document obsoletes RFC 3901.

### Domain Control Validation using DNS
Draft: draft-ietf-dnsop-domain-verification-techniques · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-domain-verification-techniques/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-domain-verification-techniques/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-domain-control-validation-updates-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Many application services on the Internet need to verify ownership or control of a domain in the Domain Name System (DNS). The general term for this process is "Domain Control Validation", and it can be done using a variety of methods such as email, HTTP/HTTPS, or the DNS itself. This document focuses only on DNS-based methods, which typically involve the Application Service Provider requesting a DNS record with a specific format and content to be visible in the domain to be verified. There is wide variation in the details of these methods today. This document provides some best practices to avoid known problems.

### Integration of DNS Domain Names into Application Environments: Motivations and Considerations
Draft: draft-ietf-dnsop-integration · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-integration/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-integration/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessa-updates-to-draft-ietf-dnsop-integration-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document describes considerations when integrating a DNS domain name into an application environment. Goals of this document include minimizing conflicts between the global DNS and applications that integrate with the global DNS, providing a consistent user experience (unique identifier across environments), and avoiding impacts to the security, stability, and resiliency of the global DNS. While all sources of potential concern cannot be enumerated in one document, accounting for at least the considerations discussed here should improve the security posture of both the global DNS and integrating applications.

### Operational Recommendations for DNSSEC Delegation Signer (DS) Automation
Draft: draft-ietf-dnsop-ds-automation · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-ds-automation/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-ds-automation/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessa-05-operational-recommendations-for-ds-automation-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Enabling support for automatic acceptance of DNSSEC Delegation Signer (DS) parameters from the Child DNS operator (via RFCs 7344, 8078, 9615) requires the parental agent, often a registry or registrar, to make a number of technical decisions around acceptance checks, error and success reporting, and multi-party issues such as concurrent updates. This document describes recommendations about how these points are best addressed in practice.

### DNS Security Extensions (DNSSEC)
Draft: draft-hoffman-rfc9364bis · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-hoffman-rfc9364bis/
page: https://datatracker.ietf.org/doc/draft-hoffman-rfc9364bis/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-updates-to-dnssec-draft-hoffman-rfc9364bis-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document describes the DNS Security Extensions (commonly called "DNSSEC") that are specified in RFCs 4033, 4034, and 4035, as well as a handful of others. One purpose is to introduce all of the RFCs in one place so that the reader can understand the many aspects of DNSSEC. This document does not update any of those RFCs. A second purpose is to state that using DNSSEC for origin authentication of DNS data is the best current practice. A third purpose is to provide a single reference for other documents that want to refer to DNSSEC. This document obsoletes RFC 9364. This document is being tracked at (https://github.com/paulehoffman/ rfc9364bis).

### Documenting and Managing DNSSEC Algorithm Lifecycles
Draft: draft-crocker-dnsop-dnssec-algorithm-lifecycle · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-crocker-dnsop-dnssec-algorithm-lifecycle/
page: https://datatracker.ietf.org/doc/draft-crocker-dnsop-dnssec-algorithm-lifecycle/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessa-documenting-and-managing-algorithm-lifecycles-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Cryptographic algorithms go through multiple phases during their lifetime: experimental, adopted, generally available, in mainstream use, phasing out, deprecated, and obsoleted. This document defines phases for algorithm deployment lifecycles within DNSSEC, and criteria that the IETF and/or other Standards Development Organizations are encouraged to use when moving an algorithm from one phase to the next.

### Populating resolvers with the root zone
Draft: draft-wkumari-dnsop-localroot-bcp · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-wkumari-dnsop-localroot-bcp/
page: https://datatracker.ietf.org/doc/draft-wkumari-dnsop-localroot-bcp/ | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
DNS recursive resolver operators need to provide the best service possible for their users, which includes providing an operationally robust and privacy protecting service. Challenges to these deployment goals include difficulty of getting responses from the root servers (such as during a network attack), longer-than-desired round-trip times to the closest DNS root server, and privacy issues relating to queries sent to the DNS root servers. Resolvers can solve all of these issues by simply serving an already cached a copy of the full root zone. This document shows how resolvers can fetch, cache and maintain a copy of the root zone, how to detect if the contents becomes stale, and procedures for handling error conditions. { Editor note: This document contains a FAQ section. It will help answer questions about why this document is not a BCP but still has BCP in the name, how and why this document differs from RFC8806, etc etc etc. The FAQ section is intended to be removed before publication. }

### Announce Existence of Parent CDS/CSYNC Scanner
Draft: draft-berra-dnsop-announce-scanner · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-berra-dnsop-announce-scanner/
page: https://datatracker.ietf.org/doc/draft-berra-dnsop-announce-scanner/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-09-scanner-announce-ddns-delegation-mgmt-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
In DNS operations, automated scanners are commonly employed by the operator of a parent zone to detect the presence of specific records, such as CDS or CSYNC, in child zones, indicating a desire for delegation updates. However, the presence and periodicity of these scanners are typically implicit and undocumented, leading to inefficiencies and uncertainties. This document proposes an extension to the semantics of the DSYNC resource record, as defined in [RFC9859], allowing parent zones to explicitly signal the presence and scanning interval of such automated scanners. This enhancement aims to improve transparency and coordination between child and parent zones. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-berra-dnsop-announce-scanner (https://github.com/johanix/draft-berra-dnsop-announce-scanner). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Authoritative DNS Transport Signaling
Draft: draft-johani-dnsop-transport-signaling · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-johani-dnsop-transport-signaling/
page: https://datatracker.ietf.org/doc/draft-johani-dnsop-transport-signaling/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-dns-transport-signaling-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document proposes a mechanism for authoritative DNS servers to signal their support for alternative transport protocols (e.g., DNS over TLS (DoT), DNS over HTTPS (DoH) and DNS over QUIC (DoQ)). This signaling may either be provided within the Additional section of authoritative DNS responses or be the result of direct DNS queries. The former, "opportunistic mode" is hint-based and aims to enable resolvers to discover alternative transports efficiently and then opportunistically upgrade connections to the authoritative, thereby improving privacy, security, and performance for subsequent interactions. The mechanism is designed to not require any protocol change or additional queries. It is safe, backward-compatible, and effective even when DNSSEC validation of the hint is not possible or desired. In certain circumstances and with additional overhead it is also possible to use direct queries to securely obtain authentication information for the authoritative that can then be used to authenticate an encrypted connection. It is also possible to establish a "validated mode" where the communication between the resolver and the authoritative server is provably both secure and authentic. Validated mode may not always be possible, depending on whether the resolver is able to DNSSEC validate the signal or not. When Validated mode is possible it does provide a stronger and more trustworthy connection. This document proposes an improvement to the opportunistic (but blind) testing of alternative transports suggested in RFC9539 by providing a mechanism by which a responding authoritative server may signal what alternative transports it supports. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-johani-dnsop-transport-signaling (https://github.com/johanix/draft-johani-dnsop-transport-signaling). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Automating DNS Delegation Management via DDNS
Draft: draft-johani-dnsop-delegation-mgmt-via-ddns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-johani-dnsop-delegation-mgmt-via-ddns/
page: https://datatracker.ietf.org/doc/draft-johani-dnsop-delegation-mgmt-via-ddns/ | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Delegation information (i.e. the NS RRset, possible glue, possible DS records) should always be kept in sync between child zone and parent zone. However, in practice that is not always the case. When the delegation information is not in sync the child zone is usually working fine, but without the amount of redundancy that the zone owner likely expects to have. Hence, should any further problems ensue it could have catastropic consequences. The DNS name space has lived with this problem for decades and it never goes away. Or, rather, it will never go away until a fully automated mechanism for how to keep the information in sync automatically is deployed. This document proposes such a mechanism. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-johani-dnsop-delegation-mgmt-via- ddns (https://github.com/johanix/draft-johani-dnsop-delegation-mgmt- via-ddns). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Signalling a Zone Cut to Nowhere in the DNS
Draft: draft-jabley-dnsop-zone-cut-to-nowhere · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-jabley-dnsop-zone-cut-to-nowhere/
page: https://datatracker.ietf.org/doc/draft-jabley-dnsop-zone-cut-to-nowhere/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-signalling-a-zone-cut-to-nowhere-in-the-dns-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document defines a standard mechanism to signal the existence of a DNS zone cut without specifying authoritative nameservers for the delegated child zone. This "zone cut to nowhere" is particularly useful in split-horizon environments, allowing parent zones to explicitly signal that a child zone exists but is only resolvable within a private namespace.

### DNS Protocol Modifications for Delegation Extensions
Draft: draft-arends-dnsop-delext · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-arends-dnsop-delext/
page: https://datatracker.ietf.org/doc/draft-arends-dnsop-delext/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-draft-arends-dnsop-delext-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
The Domain Name System (DNS) protocol permits Delegation Signer (DS) records at delegation points. This document describes modifications to the Domain Name System (DNS) protocol to permit a range of resource record types at delegation points. These modifications are designed to maintain compatibility with existing DNS resolution mechanisms and provide a secure method for processing these records at delegation points.

### Multiple Algorithm Rules in DNSSEC
Draft: draft-huque-dnsop-multi-alg-rules · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-huque-dnsop-multi-alg-rules/
page: https://datatracker.ietf.org/doc/draft-huque-dnsop-multi-alg-rules/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessb-multiple-algorithm-rules-in-dnssec-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document restates the requirements on DNSSEC signing and validation and makes small adjustments in order to allow for more flexible handling of configurations that advertise multiple Secure Entry Points (SEP) with different signing algorithms via their DS record or trust anchor set. The adjusted rules allow both for multi- signer operation and for the transfer of signed DNS zones between providers, where the providers support disjoint DNSSEC algorithm sets. In addition, the proposal enables pre-publication of a trust anchor in preparation for an algorithm rollover, such as of the root zone. This document updates RFCs 4035 and 6840.

### DS support for private DNSSEC algorithms
Draft: draft-andrews-ds-support-for-private-algorithms · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-andrews-ds-support-for-private-algorithms/
page: https://datatracker.ietf.org/doc/draft-andrews-ds-support-for-private-algorithms/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-ds-and-private-algorithms-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Extend the DS digest field of the DS record to identify the private DNSSEC algorithm of the DNSKEY matching the DS record.

### DNSSEC Key Restore
Draft: draft-fobser-dnsop-dnssec-keyrestore · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-fobser-dnsop-dnssec-keyrestore/
page: https://datatracker.ietf.org/doc/draft-fobser-dnsop-dnssec-keyrestore/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessb-draft-fobser-dnsop-dnssec-keyrestore-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document describes the issues surrounding the handling of DNSSEC private keys in a DNSSEC signer. It presents operational guidance in case a DNSSEC private key becoming inoperable. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Domain Name System Operations Working Group mailing list (dnsop@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/dnsop/. Source for this draft and an issue tracker can be found at https://github.com/fobser/draft-fobser-dnsop-dnssec-keyrecovery.

### The "_for-sale" Underscored and Globally Scoped DNS Node Name
Draft: draft-davids-forsalereg · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-davids-forsalereg/
page: https://datatracker.ietf.org/doc/draft-davids-forsalereg/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessb-the--for-sale-underscored-and-globally-scoped-dns-node-name-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document defines an operational convention that uses the reserved underscored DNS leaf node name "_for-sale" to indicate the parent domain name is available for purchase. The convention can be deployed without disrupting existing operations, and it may be applied even when the domain name is still actively in use.

### A Method for Identifying the Administrative Boundaries of DNS Names
Draft: draft-yao-dbound-identify-dns-boundary · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-yao-dbound-identify-dns-boundary/
page: https://datatracker.ietf.org/doc/draft-yao-dbound-identify-dns-boundary/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-a-method-for-identifying-the-administrative-boundaries-of-dns-names-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Two or more DNS names belonging to the same registrants may share the same DNS administrative boundaries. Currently, there are no good methods to identify such shared administrative boundaries in DNS. This document adds the function of lookup of domain name administrative boundary to domain name system, which describes a new method for using dbound resource record for determining domain name administrative boundaries.

### Post-Quantum Cryptography Strategy for DNSSEC
Draft: draft-sheth-pqc-dnssec-strategy · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-sheth-pqc-dnssec-strategy/
page: https://datatracker.ietf.org/doc/draft-sheth-pqc-dnssec-strategy/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessb-post-quantum-dnssec-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
This document proposes a post-quantum cryptography (PQC) strategy for Domain Name System Security (DNSSEC) that includes two types of algorithms: one or more conservatively designed algorithms that are unlikely ever to need to be replaced, and one or more low-impact drop-in algorithms that are used the same way as a traditional signature algorithm. The conservatively designed algorithms can be used in a mode of operation that mitigates the operational impact of a large signature size. The combination provides both the routine performance of the low-impact algorithm and a resilient fallback to the conservatively designed choice. The draft outlines the strategy, provides recommendations for future testing and deployment, and highlights operational considerations in adopting PQC for DNSSEC.

### Considerations for Protective DNS Server Operators
Draft: draft-liu-dnsop-protective-dns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-liu-dnsop-protective-dns/
page: https://datatracker.ietf.org/doc/draft-liu-dnsop-protective-dns/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-considerations-for-protective-dns-server-operators-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Protective DNS is a defense mechanism deployed on recursive resolvers to prevent users from accessing malicious domains. For domain names in the blocklist, it rewrites DNS resolution responses to point to secure destinations (e.g., safe servers) to prevent users from accessing malicious entities. Owing to its effective defenses against common cyber attack behaviors—such as command-and-control (C2) communications of malware—Protective DNS deployment has surged via various initiatives. Not only have renowned DNS service providers adopted this defense, but some countries have also launched national-scale deployments. Meanwhile, studies analyzing Protective DNS have identified implementation diversity. Thus, this document aims to provide specific operational and security considerations for Protective DNS. It is intended primarily for entities seeking to deploy Protective DNS for defensive purposes, offering deployment and security considerations.

### Problems Statement and Requirements Analysis of DNS for Internet of Agents (IoA)
Draft: draft-ye-problems-and-requirements-of-dns-for-ioa · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ye-problems-and-requirements-of-dns-for-ioa/
page: https://datatracker.ietf.org/doc/draft-ye-problems-and-requirements-of-dns-for-ioa/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-sessb-11-problems-and-requirements-of-dns-for-ioa-00 | video: https://youtu.be/7eGNuHmvbXA | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
In the AI-driven era, DNS is supposed to evolve with technological advancements to accommodate the complex and diverse requirements of the IoA. This draft analyzes the issues surrounding DNS in supporting agents collaboration and explores corresponding technical requirements.

### Making LocalRoot a Best Current Practice
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-dnsop-making-localroot-a-best-current-practice-00 | video: https://youtu.be/aDZU8XThpnk | materials: https://datatracker.ietf.org/meeting/124/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

## Working Group: grow

### Generic Event Notification (GEN) for BGP Monitoring Protocol (BMP)
Draft: draft-sp-grow-bmp-gen · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-sp-grow-bmp-gen/
page: https://datatracker.ietf.org/doc/draft-sp-grow-bmp-gen/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-01-ietf124-grow-bmp-draft-gen-common-updates-multi-peer-rmon-aggregated-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
This document defines a new BMP message type: the Generic Event Notification (GEN). The BMP GEN message provides a flexible mechanism for reporting a wide variety of events related to BGP at different levels of hierarchy, such as routing instance, AFI/SAFI, or peer level. The BMP GEN message enables operators and automated systems to receive detailed context for operational events, such as policy triggers, administrative interventions, and state management notifications (e.g., RIB view unmonitor events).

### Common BMP Route-Monitoring Messages for Routes Unchanged by Policy
Draft: draft-patki-grow-bmp-common-updates · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/
page: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
A route unmodified by the inbound policy on a monitored router is included both in Pre-Policy Adj-RIB-In as well as Post-Policy Adj- RIB-In Route-Monitoring messages when both the Pre-Policy and Post- Policy Route-Monitoring modes are enabled. Similarly, a route unmodified by the outbound policy is included in Pre-Policy Adj-RIB- Out as well as Post-Policy Adj-RIB-Out Route-Monitoring messages. This document defines a method to avoid duplicate inclusion of routes unmodified by policy either in Adj-RIB-In or Adj-RIB-Out.

### Definition for Aggregated BMP Route Monitoring Message
Draft: draft-liu-grow-bmp-rm-aggregated · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
This document proposes an aggregated BMP Route Monitoring message based on the BMP Multi-Peer Header message (draft-liu-grow-bmp- multiple-peer-header). It can compress multiple BMP Route Monitoring messages into one aggregated BMP Route Monitoring message to reduce the amount of reported BMP Route Monitoring messages and reduce the network overhead.

### Definition for BMP Multiple Peer Header
Draft: draft-liu-grow-bmp-multiple-peer-header · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-multiple-peer-header/
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-multiple-peer-header/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
This document proposes a format of multiple peer header for aggregating BMP messages. It can be used to compress multiple BMP messages with per-peer header into one aggregated BMP message, which could reduce the amount of reported BMP messages and reduce network overhead.

### BGP Operations and Security
Draft: draft-ietf-grow-bgpopsecupd · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bgpopsecupd/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bgpopsecupd/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-draft-ietf-grow-bgpopsecupd-draft-ietf-grow-routing-ops-sec-inform-draft-ietf-grow-routing-ops-terms-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
The Border Gateway Protocol (BGP) is a critical component in the Internet to exchange routing information between network domains. It is important to understand the security and reliability requirements that can and should be met to prevent accidental or intentional routing disturbances. Previously, security considerations for BGP have been described in RFC7454 / BCP194. Since the publication of RFC7454, changes in operational practice have taken place, which are partially conflicting with the advice given in RFC7454. This document obsoletes RFC7454, and provides less implementation-specific best practices, with the goal of being less prone to becoming outdated or conflicting with changed operational practices.

### Current Options for Securing Global Routing
Draft: draft-ietf-grow-routing-ops-sec-inform · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-sec-inform/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-sec-inform/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
The Border Gateway Protocol (BGP) is used for exchanging routing information between Autonomous Systems in the Internet. Due to its importance, it is necessary to ensure the basic security properties for BGP and BGP speaking routers. While the general principles for securing BGP operations are outlined in RFC 7454, that document does not detail the technical and implementation options for securing BGP. This document serves as a contemporary, non-exhaustive repository of options and methods for securing BGP. This document explicitly does not make value statements on the efficacy of individual techniques, nor does it mandate or prescribe the use of specific techniques or implementation details. Operators are advised to carefully consider whether the listed methods are applicable for their use-cases. Furthermore, the options listed in this document may change over time, and should not be used as a timeless ground-truth of applicable or sufficient methods.

### Currently Used Terminology in Global Routing Operations
Draft: draft-ietf-grow-routing-ops-terms · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-terms/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-terms/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
Operating the global routing ecosystem entails a diverse set of interacting components, while operational practice evolved over time. In that time, terms emerged, disappeared, and sometimes changed their meaning. To aid operators and implementers in reading contemporary drafts, this document provides an overview of terms and abbreviations used in the global routing operations community. The document explicitly does not serve as an authoritative source of correct terminology, but instead strives to provide an overview of practice.

### Route Server Next Hop Translation
Draft: draft-marenamat-grow-route-server-nh-translation · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-marenamat-grow-route-server-nh-translation/
page: https://datatracker.ietf.org/doc/draft-marenamat-grow-route-server-nh-translation/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-draft-marenamat-grow-route-server-nh-translation-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
With the advent of RFC8950, Internet Exchange Points (IXPs) are enabled to rely solely on IPv6 addresses for adressing in their peering LANs. However, routers not supporting RFC8950 are a technical roadblock. It is easier to extend the capabilities of the IXP Route Server (RS) instead of those of every unsupporting router. Thus, this document introduces the concept of Specific Local Address Tables (SLATs). SLATs translate BGP next hops between all IXP members, regardless of their RFC8950 support, paving the way for IPv6-only IXPs. This document also introduces another, more transparent variant of BGP next hop translation applicable in IXPs which do not employ ARP and ND proxying. This document updates RFC 7947 by specifying an allowed route modification at the route server.

### BMP Snapshots
Draft: draft-lucente-grow-bmp-offline · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-lucente-grow-bmp-offline/
page: https://datatracker.ietf.org/doc/draft-lucente-grow-bmp-offline/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-draft-lucente-grow-bmp-offline-02-bmp-snapshots-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
BMP (BGP Monitoring Protocol) is perfectly suited for real-time consumption but less ideal in stream processing and off-wire historical scenarios. The issue is that the necessary information to produce a complete view and enabling correct processing of all messages in the stream, is only sent out at the beginning of the BMP session. This document introduces the concept of BMP Snapshots, enabling BMP stations to synchronize mid-stream, and, providing the basis for self-contained, time-binned archiving of BMP data.

### Storing BMP messages in MRT Format
Draft: draft-petrie-grow-mrt-bmp · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-petrie-grow-mrt-bmp/
page: https://datatracker.ietf.org/doc/draft-petrie-grow-mrt-bmp/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-draft-petrie-grow-mrt-bmp-01-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
This document extends the Multi-threaded Routing Toolkit (MRT) export format to support the storage of BMP messages.

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-bmp-v2-tlv-support-01 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
Most of the BGP Monitoring Protocol (BMP) message types make provision for data in Type, Length, Value (TLV) format. However, Route Monitoring messages (which provide a snapshot of the monitored Routing Information Base) Stats Reports (which supply periodical counters) and Peer Down messages (which indicate that a peering session was terminated) do not. Supporting (optional) data in TLV format across all BMP message types provides consistent and extensible structures that would be useful among the various use- cases where conveying additional data to a monitoring station is required. This document updates RFC 7854 [RFC7854] to support TLV data in all message types and defines some essential TLVs. Additionally, this document introduces support for enterprise- specific TLVs in the BGP Monitoring Protocol by defining an Enterprise Bit (E-bit) that allows usage of per-vendor Type values.

### Using BMP over QUIC connection
Draft: draft-liu-grow-bmp-over-quic · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-over-quic/
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-over-quic/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-using-bmp-over-quic-connection-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
The BGP Monitoring Protocol (BMP) provides a convenient interface for obtaining route views by monitoring BGP sessions. BMP operates over TCP and is unidirectional (from client to server). QUIC provides multiple simultaneous streams to carry data in one direction, enabling much better efficiency and performance for both peers, in particular unidirectional streams can provide reverse data protection for the sender. QUIC also provides shorter handshake and includes TLS. This document describes how to use BMP over the QUIC transport protocol, named BMPoQUIC.

### Peer Capability Update Notification in BGP Monitoring Protocol (BMP)
Draft: draft-lin-grow-bmp-cap-notification · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-lin-grow-bmp-cap-notification/
page: https://datatracker.ietf.org/doc/draft-lin-grow-bmp-cap-notification/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-peer-capability-update-notification-in-bgp-monitoring-protocol-bmp-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
When BGP Dynamic Capability is supported, dynamic updates of capabilities are allowed over an established BGP session. At present, after the BGP session is established, the monitored router sends a BMP Peer Up Notification message first, containing the initial capabilities. If BGP Dynamic Capability is supported, using BMP Peer Up Notification messages to report subsequent capability changes for a BGP session becomes inappropriate. This document defines a new Peer Capability Update Notification message type in BMP to report peer capability changes.

### BMP Sequence Number, Timestamp and Flags TLVs
Draft: draft-younsi-grow-bmp-snts · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-younsi-grow-bmp-snts/
page: https://datatracker.ietf.org/doc/draft-younsi-grow-bmp-snts/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
This document defines a Timestamp TLV that carries a timestamp describing one of multiple possible events related to the BMP message. It also defines a Sequence Number TLV which carries the sequence number of the BMP message for the current BMP session. Finally, this document defines an Extended Flags TLV that replaces the Flags field of the Per-Peer Header, allowing more flags to be allocated in BMP.

### BMP Loc-RIB: Peer address
Draft: draft-ietf-grow-bmp-loc-peer · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-loc-peer/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-loc-peer/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-snts-loc-peer-slides-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
BMP Loc-RIB [RFC9069] enforces that the BMP router sets the Peer Address value of a path information to zero. This document introduces the option to communicate the actual peer from which a path was received when advertising that path with BMP Loc-RIB.

### EVPN-Specific BMP RIB Statistics Extensions
Draft: draft-saum-grow-bmp-afi-safi-evpn · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/
page: https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/ | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
This document defines new EVPN-specific BGP Monitoring Protocol (BMP) statistics types. These extensions include scalar counters for EVPN route types specifically, while also keeping scope for defining counters which are EVPN route-type agnostic but related to BGP-EVPN RIB like, number of multihoming Ethernet Segments, number of multihomed EVIs, number of aliased paths, number of dynamic inter-VRF route leaking (IVRL). This revision (-06) firms up the specification for working group consideration: it adds a Relationship to Other Work section that explicitly maps this document to concurrently circulating GROW contributions on BMP statistics and TLV extensions and invites coordination with their authors, corrects the YANG alignment reference, strengthens Security Considerations, and adds a worked example. No statistics semantics, Stat Type/Subtype allocations, or wire formats defined in -05 are changed.

### EVPN-Specific-BMP-Stats
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-evpn-specific-bmp-stats-00 | video: https://youtu.be/qkDDPaLey0Q | materials: https://datatracker.ietf.org/meeting/124/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

## Working Group: httpbis

### Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-resumable-uploads-00 | video: https://youtu.be/7DizVxC9WBk | materials: https://datatracker.ietf.org/meeting/124/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Secondary Certificate Authentication of HTTP servers
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-secondary-certificate-authentication-of-http-servers-00 | video: https://youtu.be/7DizVxC9WBk | materials: https://datatracker.ietf.org/meeting/124/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Origin Bound Cookies
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-origin-bound-cookies-00 | video: https://youtu.be/7DizVxC9WBk | materials: https://datatracker.ietf.org/meeting/124/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Detecting Outdated Proxy Configuration
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-detecting-outdated-proxy-configuration-00 | video: https://youtu.be/7DizVxC9WBk | materials: https://datatracker.ietf.org/meeting/124/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Unbound DATA frames in HTTP/3
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-unbound-data-frames-in-http3-00 | video: https://youtu.be/7DizVxC9WBk | materials: https://datatracker.ietf.org/meeting/124/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP Request Smuggling Defenses
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-httpbis-http-request-smuggling-defenses-00 | video: https://youtu.be/7DizVxC9WBk | materials: https://datatracker.ietf.org/meeting/124/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

## Working Group: idr

### A Border Gateway Protocol 4 (BGP-4)
Draft: draft-ietf-idr-bgp4-rfc4271bis · Working group: idr
Agenda: draft-ietf-idr-bgp4-rfc4271bis-00
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/ | materials: https://datatracker.ietf.org/meeting/124/session/idr
This document discusses the Border Gateway Protocol (BGP), which is an inter-Autonomous System routing protocol. The primary function of a BGP-speaking system is to exchange network reachability information with other BGP systems. This network reachability information includes information on the list of Autonomous Systems (ASes) that reachability information traverses. This information is sufficient for constructing a graph of AS connectivity for this reachability from which routing loops may be pruned, and, at the AS level, some policy decisions may be enforced. BGP-4 provides a set of mechanisms for supporting Classless Inter- Domain Routing (CIDR). These mechanisms include support for advertising a set of destinations as an IP prefix, and eliminating the concept of network "class" within BGP. BGP-4 also introduces mechanisms that allow aggregation of routes, including aggregation of AS paths. This document obsoletes RFC 4271 and many other RFCs. It updates RFC 7606 by subsuming its core functionality.

### BGP Extended Communities Attribute
Draft: draft-ietf-idr-rfc4360-bis · Working group: idr
Agenda: draft-ietf-idr-rfc4360-bis-01
page: https://datatracker.ietf.org/doc/draft-ietf-idr-rfc4360-bis/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-2-bgp-extended-communities-attribute-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
This document describes the "Extended Communities" BGP-4 attribute. This attribute provides a mechanism for labeling information carried in BGP-4. These labels can be used to control the distribution of this information, or for other applications. This document obsoletes RFC 4360. This document also updates RFC 5701 by adding an "Operational Considerations" section.

### Inter Domain considerations for Constrained Route distribution
Draft: draft-litkowski-idr-rtc-interas · Working group: idr
Agenda: draft-litkowski-idr-rtc-interas-03
page: https://datatracker.ietf.org/doc/draft-litkowski-idr-rtc-interas/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-4-inter-domain-considerations-for-constrained-route-distribution-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
RFC4684 defines Multi-Protocol BGP (MP-BGP) procedures that allow BGP speakers to exchange Route Target reachability information in order to limit the propagation of Virtual Private Networks (VPN) Network Layer Reachability Information (NLRI). RFC4684 addresses both intra domain and inter domain distributions. Operational deployment experience shows that the current distribution model defined in RFC4684 for inter domain may cause some issue in specific scenarios. This document proposes alternate route distribution rules for inter domain in order to address these specific scenarios.

### BGP best path next-hop selection enhancements
Draft: draft-vroonen-idr-bgp-bestpath-nh-selection · Working group: idr
Agenda: draft-vroonen-idr-bgp-bestpath-nh-selection-00
page: https://datatracker.ietf.org/doc/draft-vroonen-idr-bgp-bestpath-nh-selection/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-5-bgp-best-path-next-hop-selection-enhancements-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
BGP [RFC4271] has originally been designed to carry IPv4 routing information over the Internet. IP routing being "hop-by-hop" in nature, NEXT_HOP which purpose is to carry the address of the next router to send the IP packet to. In BGP, the next-hop may not be a directly connected router, hence, when evaluating paths, a BGP speaker must determine if the next-hop is resolvable and, if so, determine the internal cost to reach it. The incremental use of tunneling technologies to carry traffic between routers (e.g.: GRE, MPLS, SR-MPLS, SRv6...) may violate the assumption that the address carried in the NEXT_HOP is representative of the actual forwarding next-hop. These technologies decouple the BGP control-plane's view of the next-hop from the data-plane's actual forwarding endpoint. This document describes the problems that arise from this decoupling. These problems include sub-optimal path selection, incorrect resolvability tracking of the forwarding path leading to traffic drop or misrouting, and others. This document specifies how BGP obtains resolvability, preference, metric, and tracking information from resolution of the forwarding path and uses those values as inputs to BGP path selection.

### The Key List BGP Attribute for NLRI Error handling
Draft: draft-decraene-idr-nlri-error-handling · Working group: idr
Agenda: draft-decraene-idr-nlri-error-handling-01
page: https://datatracker.ietf.org/doc/draft-decraene-idr-nlri-error-handling/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-16-the-key-list-bgp-attribute-for-nlri-error-handling-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
RFC 7606 partially revises the error handling for BGP UPDATE messages. It reduces the cases of BGP session reset by defining and using less impactful error handling approaches, such as attribute discard and treat-as-withdraw when applicable. The treat-as-withdraw approach requires that the entire NLRI field of the MP_REACH_NLRI attribute be successfully parsed. This typically means parsing errors in MP_REACH_NLRI cannot be handled by any means short of session reset. This is exacerbated by the use of non-key data within NLRI, which introduces parsing complexity and additional error cases. This specification defines a non-transitive BGP attribute, the "NLRI_KEY_LIST attribute", to encode NLRIs as per the format of MP_UNREACH_NLRI. This attribute is used to allow the treat-as- withdraw error-handling approach to be used in case an error in the MP_REACH_NLRI attribute prevents the parsing of its NLRIs. This document updates RFC 7606 by mandating that the NLRI_KEY_LIST attribute appear before the MP_REACH_NLRI (or any other) attribute in an UPDATE message.

### BGP Next Hop Dependent Characteristics Attribute
Draft: draft-ietf-idr-entropy-label · Working group: idr
Agenda: 7. Split of draft-ietf-idr-entropy-label (10 mins)
page: https://datatracker.ietf.org/doc/draft-ietf-idr-entropy-label/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-split-of-draft-ietf-idr-entropy-label-01 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
RFC 5492 allows a BGP speaker to advertise its capabilities to its peer. When a route is propagated beyond the immediate peer, it is useful to allow certain characteristics to be conveyed further. In particular, it is useful to advertise forwarding plane features. This specification defines a BGP transitive attribute to carry such information, the "Next Hop Dependent Characteristics Attribute," or NHC. Unlike the capabilities defined by RFC 5492, the characteristics conveyed in the NHC apply solely to the routes advertised by the BGP UPDATE that contains the particular NHC. This specification also defines an NHC characteristic that can be used to advertise the ability to process the MPLS Entropy Label as an egress LSR for all NLRI advertised in the BGP UPDATE. It updates RFC 6790 and RFC 7447 concerning this BGP signaling.

### BGP Next Hop Dependent Characteristics Attribute
Draft: draft-scudder-idr-nhc · Working group: idr
Agenda: draft-scudder-idr-nhc-00
page: https://datatracker.ietf.org/doc/draft-scudder-idr-nhc/ | materials: https://datatracker.ietf.org/meeting/124/session/idr
RFC 5492 allows a BGP speaker to advertise its capabilities to its peer. When a route is propagated beyond the immediate peer, it is useful to allow certain characteristics to be conveyed further. In particular, it is useful to advertise forwarding plane features. This specification defines a BGP transitive attribute to carry such information, the "Next Hop Dependent Characteristics Attribute," or NHC. Unlike the capabilities defined by RFC 5492, the characteristics conveyed in the NHC apply solely to the routes advertised by the BGP UPDATE that contains the particular NHC.

### BGP Entropy Label Characteristic
Draft: draft-scudder-idr-elc · Working group: idr
Agenda: draft-scudder-idr-elc-00
page: https://datatracker.ietf.org/doc/draft-scudder-idr-elc/ | materials: https://datatracker.ietf.org/meeting/124/session/idr
The BGP Next Hop Dependent Characteristics Attribute (NHC) provides a way for a BGP speaker to advertise certain characteristics of routes. In particular, it is useful to advertise forwarding plane features. This specification defines an NHC characteristic that can be used to advertise the ability to process the MPLS Entropy Label as an egress LSR for all NLRI advertised in the BGP UPDATE. It updates RFC 6790 and RFC 7447 concerning this BGP signaling.

### BGP Next-next Hop Nodes
Draft: draft-ietf-idr-next-next-hop-nodes · Working group: idr
Agenda: draft-ietf-idr-next-next-hop-nodes-00
page: https://datatracker.ietf.org/doc/draft-ietf-idr-next-next-hop-nodes/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-8-bgp-next-next-hop-nodes-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
BGP speakers learn their next hop addresses for NLRI in RFC 4271 in the NEXT_HOP field and in RFC 4760 in the "Network Address of Next Hop" field. Under certain circumstances, it might be desirable for a BGP speaker to know both the next hops and the next-next hops of NLRI to make optimal forwarding decisions. One such example is global load balancing (GLB) in a Clos network. Draft-ietf-idr-nhc defines the "Next Hop Dependent Characteristics Attribute" (NHC) which allows a BGP speaker to signal the forwarding characteristics associated with a given next hop. This document defines a new NHC characteristic, the Next-next Hop Nodes (NNHN) characteristic, which can be used to advertise the next- next hop nodes associated with a given next hop.

### Enhanced Dynamic Capability for BGP
Draft: draft-chen-idr-enhanced-dynamic-cap · Working group: idr
Agenda: draft-chen-idr-enhanced-dynamic-cap-01
page: https://datatracker.ietf.org/doc/draft-chen-idr-enhanced-dynamic-cap/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-enhanced-dynamic-capability-for-bgp-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
This document addresses the limitations with the BGP Dynamic Capability specification by introducing additional protocol extensions and operational procedures so that a BGP capability that requires bi-directional capability advertisement can be revised dynamically.

### Supplement of BGP-LS Distribution for SR Policies and State
Draft: draft-lp-idr-bgp-ls-sr-policy-supplement · Working group: idr
Agenda: draft-lp-idr-bgp-ls-sr-policy-supplement-03
page: https://datatracker.ietf.org/doc/draft-lp-idr-bgp-ls-sr-policy-supplement/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-supplement-of-bgp-ls-distribution-for-sr-policies-and-state-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
This document supplements additional information of the segment list in the BGP-LS advertisement for SR Policy state information. A new flag and a new sub-TLV are introduced in the SR Segment List TLV of BGP-LS SR Policy Candidate Path NLRI.

### BGP SR Policy Extensions for Path Scheduling
Draft: draft-zzd-idr-sr-policy-scheduling · Working group: idr
Agenda: draft-zzd-idr-sr-policy-scheduling-10
page: https://datatracker.ietf.org/doc/draft-zzd-idr-sr-policy-scheduling/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessa-2-2-bgp-sr-policy-extensions-for-path-scheduling-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
Segment Routing (SR) policy enables instantiation of an ordered list of segments with a specific intent for traffic steering. When using SR policy in a a network with time-variant characterics or requires high resources utilization efficiency, delivering the time-variant information associated with paths is necessary. This document proposes extensions to BGP SR Policy to deliver the schedule time information of candidate paths and segment lists.

### BGP Extensions of SR Policy for Composite Candidate Path
Draft: draft-jiang-idr-sr-policy-composite-path · Working group: idr
Agenda: draft-jiang-idr-sr-policy-composite-path-03
page: https://datatracker.ietf.org/doc/draft-jiang-idr-sr-policy-composite-path/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-bgp-extensions-of-sr-policy-for-composite-candidate-path-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
SR Policy Architecture [RFC9256] defines the concept of a Composite Candidate Path. A regular SR Policy Candidate Path outputs traffic to a set of Segment Lists, while an SR Policy Composite Candidate Path outputs traffic recursively to a set of SR Policies on the same headend. This document defines extensions to BGP to distribute SR policies carrying composite candidate path information. So that composite candidate paths can be installed when the SR policy is applied.

### Signaling Composite Candidate Path of SR Policy using BGP-LS
Draft: draft-li-idr-bgpls-sr-policy-composite-path · Working group: idr
Agenda: draft-li-idr-bgpls-sr-policy-composite-path-08
page: https://datatracker.ietf.org/doc/draft-li-idr-bgpls-sr-policy-composite-path/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-signaling-composite-candidate-path-of-sr-policy-using-bgp-ls-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
SR Policy Architecture [RFC9256] defines the concept of a Composite Candidate Path. A regular SR Policy Candidate Path outputs traffic to a set of Segment Lists, while an SR Policy Composite Candidate Path outputs traffic recursively to a set of SR Policies on the same headend. This document specifies the extensions to BGP Link State (BGP-LS) to carry composite candidate path information in the advertisement of an SR policy.

### Packet Content Filter for BGP FlowSpec
Draft: draft-cui-idr-content-filter-flowspec · Working group: idr
Agenda: draft-cui-idr-content-filter-flowspec-03
page: https://datatracker.ietf.org/doc/draft-cui-idr-content-filter-flowspec/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessa-2-5-packet-content-filter-for-bgp-flowspec-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
The BGP FlowSpec mechanism enables the distribution of traffic filter policies (traffic filters and actions) via BGP, facilitating DDoS traffic filtering. The IP filter components defined for FSv1 and the FSv2 IP Basic Filter Families primarily match fields in the IP and transport-layer headers, which may not adequately address volumetric DDoS attack traffic characterized by fixed patterns within the packet content. This document defines a Packet Content Filter Component for FSv1 and FSv2. The match is encoded using OType, Offset, Content Length, Content, and Mask fields in the FlowSpec NLRI. The FSv1 encoding additionally carries a PType field. This new component aims to leverage network devices such as routers and switches to support controlled traffic handling, traffic optimization, and mitigation of simple volumetric DDoS attacks, reducing the overall processing cost of carrier networks.

### BGP Flow Specification Extension for Feedback Binding
Draft: draft-cui-idr-flowspec-feedback-binding · Working group: idr
Agenda: draft-cui-idr-flowspec-feedback-binding-00
page: https://datatracker.ietf.org/doc/draft-cui-idr-flowspec-feedback-binding/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessa-2-6-bgp-flow-specification-extension-for-feedback-binding-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
This document specifies a BGP Flow Specification extension that conveys per-route feedback binding for a FlowSpec route using the BGP Extended Community attribute. The proposed mechanism introduces a single Feedback Action, encoded as a Generic Transitive Extended Community, which enables downstream routers to report telemetry information or operational events associated with a FlowSpec rule. The Feedback Action carries parameters including a Feedback Identifier (FID), a window exponent (WINC) that defines the periodic aggregation interval, an event flag, and a scope selector to control where feedback is generated. These parameters are attached to the FlowSpec route and are propagated across AS boundaries unchanged. This document focuses on the signaling aspect; a companion document may define how feedback information is exported as part of a network telemetry framework (e.g., leveraging the BGP Monitoring Protocol (BMP)) or equivalent mechanisms to report periodic and event-driven feedback keyed by the FID.

### BGP extensions for SRv6/MPLS Transport Interworking
Draft: draft-sa-idr-bgp-srv6-mpls-transport-iw · Working group: idr
Agenda: draft-sa-idr-bgp-srv6-mpls-transport-iw-00
page: https://datatracker.ietf.org/doc/draft-sa-idr-bgp-srv6-mpls-transport-iw/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessa-2-7-bgp-extensions-for-srv6mpls-transport-interworking-00 | video: https://youtu.be/36tw7gGeIdA | materials: https://datatracker.ietf.org/meeting/124/session/idr
This document defines the BGP extensions required to provide transport interworking between SRv6 and MPLS in SRv6 deployment.

### 1. RFC4271bis update
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-rfc4271bis-update-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### 3. BGP Link Bandwidth Extended Community Use Cases
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-3-bgp-link-bandwidth-extended-community-use-cases-00 | video: https://youtu.be/fFc0kGI5arw | materials: https://datatracker.ietf.org/meeting/124/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

## Working Group: ipsecme

### IKEv2 Support for Child SA PFS Policy Information
Draft: draft-pwouters-ipsecme-child-pfs-info · Working group: ipsecme
Agenda: draft-pwouters-ipsecme-child-pfs-info
page: https://datatracker.ietf.org/doc/draft-pwouters-ipsecme-child-pfs-info/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-child-pfs-info-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This document defines an extension for the Internet Key Exchange Protocol Version 2 (IKEv2) to support negotiation at the time of initial Child Security Association (SA) establishing of Key Exchange (KE) method that could be used in subsequent rekeys of this SA.

### Enhanced Encapsulating Security Payload (EESP)
Draft: draft-ietf-ipsecme-eesp · Working group: ipsecme
Agenda: draft-ietf-ipsecme-eesp
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp/ | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This document describes the Enhanced Encapsulating Security Payload (EESP) protocol, which builds on the existing IP Encapsulating Security Payload (ESP) protocol. It is designed to modernize and overcome limitations in the ESP protocol. EESP adds Session IDs (e.g., to support CPU pinning and QoS support based on the inner traffic flow), changes some previously mandatory fields to optional, and moves the ESP trailer into the EESP header. Additionally, EESP adds header options adapted from IPv6 to allow for future extension. New header options are defined which add a crypt- offset to allow for exposing inner flow information for middlebox use.

### IKEv2 negotiation for Enhanced Encapsulating Security Payload (EESP)
Draft: draft-ietf-ipsecme-eesp-ikev2 · Working group: ipsecme
Agenda: draft-ietf-ipsecme-eesp-ikev2
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp-ikev2/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-eesp-ikev2-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This document specifies how to negotiate the use of the Enhanced Encapsulating Security Payload (EESP) protocol using the Internet Key Exchange protocol version 2 (IKEv2). The EESP protocol, which is defined in [I-D.ietf-ipsecme-eesp], provides the same security services as Encapsulating Security Payload (ESP), but has richer functionality and provides better performance in specific circumstances. This document specifies negotiation of version 0 of EESP.

### Downgrade Prevention for the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-ietf-ipsecme-ikev2-downgrade-prevention · Working group: ipsecme
Agenda: draft-ietf-ipsecme-ikev2-downgrade-prevention
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-draft-ietf-ipsecme-ikev2-downgrade-prevention-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This document specifies an extension to the Internet Key Exchange protocol version 2 (IKEv2) in which the peers authenticate the full IKE_SA_INIT transcript. When both peers implement the extension and at least one relevant authentication credential is not compromised, this prevents certain downgrade attacks on IKEv2. This document updates RFC 7296.

### KEM-based Authentication for IKEv2 with Post-quantum Security
Draft: draft-wang-ipsecme-kem-auth-ikev2 · Working group: ipsecme
Agenda: draft-wang-ipsecme-kem-auth-ikev2
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-kem-auth-ikev2/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-kem-auth-in-ikev2-02 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This draft specifies a new authentication mechanism, called KEM (Key Encapsulation Mechanism) -based authentication, for the Internet Key Exchange Protocol Version 2 (IKEv2). This is motivated by the fact that some post-quantum KEMs (like ML-KEM) are more efficient than post-quantum signature algorithms (like ML-DSA).

### Post-quantum Hybrid Key Exchange in IKEv2 with FrodoKEM
Draft: draft-wang-ipsecme-hybrid-kem-ikev2-frodo · Working group: ipsecme
Agenda: draft-wang-ipsecme-hybrid-kem-ikev2-frodo
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-hybrid-kem-ikev2-frodo/ | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
Multiple key exchanges in the Internet Key Exchange Protocol Version 2 (IKEv2) [RFC9370] specifies a framework, which supports multiple key encapsulation mechanisms (KEMs) in IKEv2 by allowing up to 7 layers of additional KEMs to derive the final shared secret keys for IPsec protocols. The primary goal is to mitigate the “harvest now and decrypt later” threat posed by Cryptographically Relevant Quantum Computers(CRQCs). For this purpose, one or more post-quantum KEMs are usually performed in addition to the traditional (EC)DH key exchange. This draft specifies how the post-quantum KEM algorithm FrodoKEM is instantiated for IKEv2 as an additional key exchange mechanism. [EDNOTE: IANA KE code points for FrodoKEM may need to be assigned, as the code points for ML-KEM has been considered in [W-D.K25]. ]

### Using Classic McEliece in the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-smyslov-ipsecme-ikev2-mceliece · Working group: ipsecme
Agenda: draft-smyslov-ipsecme-ikev2-mceliece
page: https://datatracker.ietf.org/doc/draft-smyslov-ipsecme-ikev2-mceliece/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-using-classic-mceliece-in-ikev2-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This document specifies how Classic McEliece Key Encapsulation Mechanism (KEM) is used to generate keys in the Internet Key Exchange version 2 (IKEv2) protocol.

### A Bound End-to-End Tunnel (BEET) mode for ESP
Draft: draft-moskowitz-ipsecme-rfc7402-beet-update · Working group: ipsecme
Agenda: draft-moskowitz-ipsecme-rfc7402-beet-update
page: https://datatracker.ietf.org/doc/draft-moskowitz-ipsecme-rfc7402-beet-update/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-beet-mode-draft-moskowitz-ipsecme-rfc7402-beet-update-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
This document is an update to the Bound End-to-End Tunnel (BEET) mode for ESP in as described in [RFC7402]. It brings the description in alignment with the addition of BEET mode for IKEv2 without any processing changes as described in [RFC7402]

### Enhanced ESP
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-enhanced-esp-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### FrodoKEM for the IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-frodokem-for-the-ikev2-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Reordering impact on IPsec
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-reordering-impact-on-ipsec-00 | video: https://youtu.be/ZwfypFEEcYY | materials: https://datatracker.ietf.org/meeting/124/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

## Working Group: jose

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE
Draft: draft-ietf-jose-pqc-kem · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/ | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This document describes conventions for using Post-Quantum Key Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and Encryption (COSE).

### JSON Web Proof
Draft: draft-ietf-jose-json-web-proof · Working group: jose
Agenda: JSON Web Proofs https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-json-web-proofs-00 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
The JOSE set of standards established JSON-based container formats for Keys, Signatures, and Encryption. They also established IANA registries to enable the algorithms and representations used for them to be extended. Since those were created, newer cryptographic algorithms that support selective disclosure and unlinkability have matured and started seeing early market adoption. The COSE set of standards likewise does this for CBOR-based containers, focusing on the needs of environments which are better served using CBOR, such as constrained devices and networks. This document defines a new container format similar in purpose and design to JSON Web Signature (JWS) and COSE Signed Messages called a _JSON Web Proof (JWP)_. Unlike JWS, which integrity-protects only a single payload, JWP can integrity-protect multiple payloads in one message. It also specifies a new presentation form that supports selective disclosure of individual payloads, enables additional proof computation, and adds a Presentation Header to prevent replay.

### JSON Proof Algorithms
Draft: draft-ietf-jose-json-proof-algorithms · Working group: jose
Agenda: JSON Proof Algorithms https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/ | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
The JSON Proof Algorithms (JPA) specification registers cryptographic algorithms and identifiers to be used with the JSON Web Proof, JSON Web Key (JWK), and COSE specifications. It defines IANA registries for these identifiers.

### JSON Proof Token and CBOR Proof Token
Draft: draft-ietf-jose-json-proof-token · Working group: jose
Agenda: JSON Proof Token https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/ | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving representation of claims to be transferred between three parties. The claims in a JPT are encoded as base64url-encoded JSON objects that are used as the payloads of a JSON Web Proof (JWP) structure, enabling them to be digitally signed and selectively disclosed. JPTs also support reusability and unlinkability when using Zero-Knowledge Proofs (ZKPs). A CBOR-based representation of JPTs is also defined, called a CBOR Proof Token (CPT). It has the same properties as JPTs, but uses the JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based JWP Compact Serialization.

### Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)
Draft: draft-ietf-jose-hpke-encrypt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/ | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This specification defines how to use Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE). HPKE enables public key encryption of arbitrary-sized plaintexts to a recipient's public key, and provides security against adaptive chosen ciphertext attacks. This specification chooses a specific subset of the HPKE features to use with JWE. This specification updates RFC 7516 (JWE) to enable use of Integrated Encryption as a Key Management Mode.

### JOSE: Deprecate 'none' and 'RSA1_5'
Draft: draft-ietf-jose-deprecate-none-rsa15 · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-deprecate-none-and-rsa1-5-00 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This document updates RFC 7518 to deprecate the JWS algorithm "none" and the JWE algorithm "RSA1_5". These algorithms have known security weaknesses. It also updates the Review Instructions for Designated Experts to establish baseline security requirements that future algorithm registrations are expected to meet.

### PQ/T Hybrid Composite Signatures for JOSE and COSE
Draft: draft-prabel-jose-pq-composite-sigs · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-prabel-jose-pq-composite-sigs/
page: https://datatracker.ietf.org/doc/draft-prabel-jose-pq-composite-sigs/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-hybrid-composite-signatures-for-jose-and-cose-01 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This document describes JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for PQ/T hybrid composite signatures. The composite algorithms described combine ML-DSA as the post-quantum component and either ECDSA or EdDSA as the traditional component.

### Public Key Derived HMAC for JOSE
Draft: draft-bastian-jose-pkdh · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-bastian-jose-pkdh/
page: https://datatracker.ietf.org/doc/draft-bastian-jose-pkdh/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-public-key-derived-secrets-for-mac-based-signatures-00 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This specification defines the use of a Diffie-Hellman key agreement (DH-KA) protocol combined with a key derivation function (KDF) to derive a symmetric Message Authentication Code (MAC) key from public information conveyed within a JSON Web Signature (JWS).

### Data At Rest Envelope (DARE)
Draft: draft-hallambaker-dare · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-hallambaker-dare/
page: https://datatracker.ietf.org/doc/draft-hallambaker-dare/ | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This document describes the Data At Rest Envelope (DARE) Envelope and Sequence. The DARE Envelope syntax is used to package plaintext or encrypted content payload and metadata with JOSE decryption and signature data authenticating the payload and metadata. The DARE Sequence format comprises a sequence of DARE Envelopes. The binary encoding of DARE envelopes allows compact encoding of encrypted and signed payloads of unknown length in a single pass with minimal overhead. The binary encoding of DARE sequences is designed to support an append only write mode and efficient reading in either the forwards or backwards directions. The JSON encoding of DARE Envelopes and sequences allows envelopes and sequences to be incorporated in other JSON objects. This document does not cover construction of indexes or signatures over multiple entries in a sequence.

### Encrypted Authenticated Resource Locator
Draft: draft-hallambaker-earl · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-hallambaker-earl/
page: https://datatracker.ietf.org/doc/draft-hallambaker-earl/ | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
This document describes the Encrypted Authenticated Resource Locator (EARL) URI scheme and the encoding and decoding of the associated content data. An EARL is a bearer token that allows an encrypted data object to be located, decrypted and authenticated using a compact URI form designed for human readability. A range of work factors is supported from 2^112 to 2^252. The plaintext data format consists of an initial header section containing metadata describing the payload, the payload itself and an optional section containing signature data.

### PQ KEMs for COSE AND JOSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-pq-kems-for-cose-and-jose-00 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### Use of HPKE with JOSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-use-of-hpke-with-jose-01 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### BC on JOSE HPKE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-bc-on-jose-hpke-00 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### DARE Envelope / EARL Thumbprint
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-dare-envelope-earl-thumbprint-00 | video: https://youtu.be/WoxqyTaaI6c | materials: https://datatracker.ietf.org/meeting/124/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

## Working Group: lamps

### Guidance on End-to-End E-mail Security
Draft: draft-ietf-lamps-e2e-mail-guidance · Working group: lamps
Agenda: a) draft-ietf-lamps-e2e-mail-guidance ( RFC 9787 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-e2e-mail-guidance/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
End-to-end cryptographic protections for e-mail messages can provide useful security. However, the standards for providing cryptographic protection are extremely flexible. That flexibility can trap users and cause surprising failures. This document offers guidance for mail user agent implementers to help mitigate those risks, and to make end-to-end e-mail simple and secure for the end user. It provides a useful set of vocabulary as well as recommendations to avoid common failures. It also identifies a number of currently unsolved usability and interoperability problems.

### Header Protection for Cryptographically Protected E-mail
Draft: draft-ietf-lamps-header-protection · Working group: lamps
Agenda: b) draft-ietf-lamps-header-protection ( RFC 9788 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-header-protection/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
S/MIME version 3.1 introduced a mechanism to provide end-to-end cryptographic protection of e-mail message headers. However, few implementations generate messages using this mechanism, and several legacy implementations have revealed rendering or security issues when handling such a message. This document updates the S/MIME specification (RFC8551) to offer a different mechanism that provides the same cryptographic protections but with fewer downsides when handled by legacy clients. Furthermore, it offers more explicit usability, privacy, and security guidance for clients when generating or handling e-mail messages with cryptographic protection of message headers. The Header Protection scheme defined here is also applicable to messages with PGP/MIME cryptographic protections.

### Internet X.509 Public Key Infrastructure -- Certificate Management Protocol (CMP)
Draft: draft-ietf-lamps-rfc4210bis · Working group: lamps
Agenda: c) draft-ietf-lamps-rfc4210bis ( RFC 9810 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc4210bis/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document describes the Internet X.509 Public Key Infrastructure (PKI) Certificate Management Protocol (CMP). Protocol messages are defined for X.509v3 certificate creation and management. CMP provides interactions between client systems and PKI components such as a Registration Authority (RA) and a Certification Authority (CA). This document adds support for management of certificates containing a Key Encapsulation Mechanism (KEM) public key and use EnvelopedData instead of EncryptedValue. This document also includes the updates specified in Section 2 and Appendix A.2 of RFC 9480. The updates maintain backward compatibility with CMP version 2 wherever possible. Updates to CMP version 2 are improving crypto agility, extending the polling mechanism, adding new general message types, and adding extended key usages to identify special CMP server authorizations. CMP version 3 is introduced for changes to the ASN.1 syntax, which are support of EnvelopedData, certConf with hashAlg, POPOPrivKey with agreeMAC, and RootCaKeyUpdateContent in ckuann messages. This document obsoletes RFC 4210 and together with I-D.ietf-lamps- rfc6712bis and it also obsoletes RFC 9480. Appendix F of this document updates the Section 9 of RFC 5912.

### Internet X.509 Public Key Infrastructure -- HTTP Transfer for the Certificate Management Protocol (CMP)
Draft: draft-ietf-lamps-rfc6712bis · Working group: lamps
Agenda: d) draft-ietf-lamps-rfc6712bis ( RFC 9811 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6712bis/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document describes how to layer the Certificate Management Protocol (CMP) over HTTP. It includes the updates to RFC 6712 specified in RFC 9480 Section 3. These updates introduce CMP URIs using a Well-known prefix. It obsoletes RFC 6712 and together with I-D.ietf-lamps-rfc4210bis and it also obsoletes RFC 9480.

### Use of Password-Based Message Authentication Code 1 (PBMAC1) in PKCS #12 Syntax
Draft: draft-ietf-lamps-rfc9579bis · Working group: lamps
Agenda: e) draft-ietf-lamps-rfc9579bis ( RFC 9879 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc9579bis/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document specifies additions and amendments to RFCs 7292 and 8018. It also obsoletes the RFC 9579. It defines a way to use the Password-Based Message Authentication Code 1 (PBMAC1), defined in RFC 8018, inside the PKCS #12 syntax. The purpose of this specification is to permit the use of more modern Password-Based Key Derivation Functions (PBKDFs) and allow for regulatory compliance.

### Use of the SLH-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-sphincs-plus · Working group: lamps
Agenda: f) draft-ietf-lamps-cms-sphincs-plus ( RFC 9814 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-sphincs-plus/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
SLH-DSA is a stateless hash-based signature scheme. This document specifies the conventions for using the SLH-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### An Attribute for Statement of Possession of a Private Key
Draft: draft-ietf-lamps-private-key-stmt-attr · Working group: lamps
Agenda: g) draft-ietf-lamps-private-key-stmt-attr ( RFC 9883 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-private-key-stmt-attr/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document specifies an attribute for a statement of possession of a private key by a certificate subject. As part of X.509 certificate enrollment, a Certification Authority (CA) typically demands proof that the subject possesses the private key that corresponds to the to-be-certified public key. In some cases, a CA might accept a signed statement from the certificate subject. For example, when a certificate subject needs separate certificates for signature and key establishment, a statement that can be validated with the previously issued signature certificate for the same subject might be adequate for subsequent issuance of the key establishment certificate.

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA)
Draft: draft-ietf-lamps-dilithium-certificates · Working group: lamps
Agenda: a) draft-ietf-lamps-dilithium-certificates (RFC-to-be 9881)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Digital signatures are used within X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using FIPS 204, the Module-Lattice- Based Digital Signature Algorithm (ML-DSA) in Internet X.509 certificates and certificate revocation lists. The conventions for the associated signatures, subject public keys, and private key are also described.

### Use of the ML-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-ml-dsa · Working group: lamps
Agenda: b) draft-ietf-lamps-cms-ml-dsa (RFC-to-be 9882)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-ml-dsa/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-fn-dsa-certificates-and-cms-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
The Module-Lattice-Based Digital Signature Algorithm (ML-DSA), as defined by NIST in FIPS 204, is a post-quantum digital signature scheme that aims to be secure against an adversary in possession of a Cryptographically Relevant Quantum Computer (CRQC). This document specifies the conventions for using the ML-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### Updates to Lightweight OCSP Profile for High Volume Environments
Draft: draft-ietf-lamps-rfc5019bis · Working group: lamps
Agenda: c) draft-ietf-lamps-rfc5019bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5019bis/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This specification defines a profile of the Online Certificate Status Protocol (OCSP) that addresses the scalability issues inherent when using OCSP in large scale (high volume) Public Key Infrastructure (PKI) environments and/or in PKI environments that require a lightweight solution to minimize communication bandwidth and client- side processing. This specification obsoletes RFC 5019. The profile specified in RFC 5019 has been updated to allow and recommend the use of SHA-256 over SHA-1.

### Clarification and enhancement of RFC7030 CSR Attributes definition
Draft: draft-ietf-lamps-rfc7030-csrattrs · Working group: lamps
Agenda: d) draft-ietf-lamps-rfc7030-csrattrs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc7030-csrattrs/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document updates RFC7030, Enrollment over Secure Transport (EST), clarifying how the Certificate Signiing Request (CSR) Attributes Response can be used by an EST server to specify both CSR attribute Object IDs (OID) and also CSR attribute values, in particular X.509 extension values, that the server expects the client to include in subsequent CSR request. RFC9148 is derived from RFC7030, and it is also updated. RFC7030 (EST) is ambiguous in its specification of the CSR Attributes Response. This has resulted in implementation challenges and implementor confusion. As a result, there was not universal understanding of what was specified. This document clarifies the encoding rules. This document therefore also provides a new straightforward approach: using a template for CSR contents that may be partially filled in by the server. This also allows an EST server to specify a subject Distinguished Name (DN).

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)
Draft: draft-ietf-lamps-kyber-certificates · Working group: lamps
Agenda: e) draft-ietf-lamps-kyber-certificates
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). This document specifies the conventions for using the ML-KEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for SLH-DSA
Draft: draft-ietf-lamps-x509-slhdsa · Working group: lamps
Agenda: f) draft-ietf-lamps-x509-slhdsa
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-slhdsa/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Digital signatures are used within X.509 Public Key Infrastructure such as X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using the Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) in X.509 Public Key Infrastructure. The conventions for the associated signatures, subject public keys, and private keys are also specified.

### Unsigned X.509 Certificates
Draft: draft-ietf-lamps-x509-alg-none · Working group: lamps
Agenda: g) draft-ietf-lamps-x509-alg-none
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-alg-none/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-media-access-control-mac-addresses-in-x509-certificates-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document defines a placeholder X.509 signature algorithm that may be used in contexts where the consumer of the certificate is not expected to verify the signature. As part of this, it updates RFC 5280.

### Use of ML-KEM in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-kyber · Working group: lamps
Agenda: h) draft-ietf-lamps-cms-kyber
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-kyber/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). Three parameter sets for the ML-KEM algorithm are specified by the US National Institute of Standards and Technology (NIST) in FIPS 203. In order of increasing security strength (and decreasing performance), these parameter sets are ML-KEM-512, ML-KEM-768, and ML-KEM-1024. This document specifies the conventions for using ML-KEM with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in "Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" (RFC 9629).

### PKCS #8 Private-Key Information Content Types
Draft: draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes · Working group: lamps
Agenda: i) draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document defines PKCS #8 content types for use with PrivateKeyInfo and EncryptedPrivateKeyInfo as specified in RFC 5958.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-sigs · Working group: lamps
Agenda: b) draft-ietf-lamps-pq-composite-sigs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document defines combinations of US NIST Module-Lattice-Based Digital Signature Algorithm (ML-DSA) in hybrid with traditional algorithms RSASSA-PKCS1-v1.5, RSASSA-PSS, ECDSA, Ed25519, and Ed448. These combinations are tailored to meet regulatory guidelines in certain regions. Composite ML-DSA is applicable in applications that use X.509 or PKIX data structures that accept ML-DSA, but where the operator wants extra protection against breaks or catastrophic bugs in ML-DSA, and where existential unforgeability (EUF-CMA) level security is acceptable.

### Clarification to Processing Key Usage Values During Certificate Revocation List (CRL) Validation
Draft: draft-ietf-lamps-keyusage-crl-validation · Working group: lamps
Agenda: c) draft-ietf-lamps-keyusage-crl-validation
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-keyusage-crl-validation/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
RFC 5280 (Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile) defines the profile of X.509 certificates and CRLs for use in the Internet. Section 4.2.1.3 of RFC 5280 requires CRL issuer certificates to contain the keyUsage extension with the cRLSign bit asserted. However, the CRL validation algorithm specified in Section 6.3 of RFC 5280 does not explicitly include a corresponding check for the presence of the keyUsage certificate extension. This document updates RFC 5280 to require that check.

### Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests
Draft: draft-ietf-lamps-attestation-freshness · Working group: lamps
Agenda: b) draft-ietf-lamps-attestation-freshness (Hannes, Hendrik)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-nonce-based-freshness-for-remote-attestation-in-csrs-for-cmp-est-and-cmc-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
When an end entity includes attestation statements in a Certificate Signing Request (CSR), the freshness of the conveyed Evidence often needs to be established. A common mechanism is a nonce that is obtained from a Relying Party or Verifier and included by the Attester in the Evidence. This document specifies how an end entity requests such an attestation freshness nonce from an RA/CA when using certificate lifecycle management protocols. It defines message formats and protocol bindings for the conveyance of nonce request and response messages in the Certificate Management Protocol (CMP), Enrollment over Secure Transport (EST), and Certificate Management over CMS (CMC), including optional type-specific information needed to produce fresh Evidence for inclusion in a CSR.

### A Mechanism for X.509 Certificate Discovery
Draft: draft-ietf-lamps-certdiscovery · Working group: lamps
Agenda: c) draft-ietf-lamps-certdiscovery (Corey)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-certdiscovery/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document specifies a method to discover a referenced X.509 certificate associated with the current X.509 certificate. This enables efficient multi-certificate or fallback certificate handling in protocols. The objective is threefold: to enhance cryptographic agility, improve operational availability, and accommodate multi-key/ certificate usage. The proposed method aims to maximize compatibility with existing systems and is designed to be legacy- friendly, making it suitable for environments with a mix of legacy and new implementations. It includes mechanisms to provide a URI from which the referenced X.509 certificate can be retrieved as well as information about the target certificate's signature and public key algorithm, empowering relying parties to make informed decisions on whether to retrieve the Referenced Certificate, and a certificate hash to ensure that the correct certificate was retrieved.

### CAA Security Tag for Cryptographically-Constrained Domain Validation
Draft: draft-ietf-lamps-caa-security · Working group: lamps
Agenda: d) draft-ietf-lamps-caa-security (Henry)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-caa-security/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-caa-security-progress-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Cryptographic domain validation procedures leverage authenticated communication channels to ensure resilience against attacks by both on-path and off-path network adversaries which attempt to tamper with communications between the Certification Authority (CA) and the network resources related to the domain contained in the certificate. Domain owners can leverage "security" Property Tags specified in CAA records (defined in [RFC8659]) with the critical flag set, to ensure that CAs perform cryptographically-constrained domain validation during their issuance procedure, hence defending against global man- in-the-middle adversaries. This document defines the syntax of the CAA security Property as well as acceptable means for cryptographically-constrained domain validation procedures.

### Composite ML-KEM for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-kem · Working group: lamps
Agenda: e) draft-ietf-lamps-pq-composite-kem (Mike, John) [IN WGLC]
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-composite-signatures-and-composite-kem-01 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document defines combinations of US NIST ML-KEM in hybrid with traditional algorithms RSA-OAEP, ECDH, X25519, and X448. These combinations are tailored to meet security best practices and regulatory guidelines. Composite ML-KEM is applicable in any application that uses X.509 or PKIX data structures that accept ML- KEM, but where the operator wants extra protection against breaks or catastrophic bugs in ML-KEM.

### Certificate Renewal Recommendations for Enrollment over Secure Transport
Draft: draft-yusef-lamps-rfc7030-renewal-recommendation · Working group: lamps
Agenda: a) draft-yusef-lamps-rfc7030-renewal-recommendation (Michael, Mike, Rifaat)
page: https://datatracker.ietf.org/doc/draft-yusef-lamps-rfc7030-renewal-recommendation/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document describes an extension to RFC7030, Enrollment over Secure Transport to give an indication to a end-entity device when it should start attempting to renew its certificates. Prior art is that client decides, with a typical recommmendation to start when the remaining lifetime of the certificate is at the 50% point. As typical certificate lifetimes are reduced from years to fractions of a year, the 50% may be far too early, and this document provides a way to give alternate advice.

### Media Access Control (MAC) Addresses in X.509 Certificates
Draft: draft-housley-lamps-macaddress-on · Working group: lamps
Agenda: b) draft-housley-lamps-macaddress-on (Corey, Russ, Joe)
page: https://datatracker.ietf.org/doc/draft-housley-lamps-macaddress-on/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-media-access-control-mac-addresses-in-x509-certificates-slides-version-2-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
This document defines a new otherName for inclusion in the X.509 Subject Alternative Name (SAN) and Issuer Alternative Name (IAN) extensions to carry an IEEE Media Access Control (MAC) address. The new name form makes it possible to bind a layer-2 interface identifier to a public key certificate. Additionally, this document defines how constraints on this name form can be encoded and processed in the X.509 Name Constraints extension.

### X.509 Certificate Extended Key Usage (EKU) for Attestation Keys
Draft: draft-jpfiset-lamps-attestationkey-eku · Working group: lamps
Agenda: c) draft-jpfiset-lamps-attestationkey-eku (J.-P., Mike, Hannes)
page: https://datatracker.ietf.org/doc/draft-jpfiset-lamps-attestationkey-eku/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
X.509 certificates ([RFC5280]) defines the Extended Key Usage (EKU) extension and specifies several key purpose identifiers (KeyPurposeIds) for use with that extension. This document defines a KeyPurposeId for the purpose of signing Evidence to provide remote attestation functions as defined in the RATS Architecture ([RFC9334]).

### Use of Remote Attestation with Certification Signing Requests
Draft: draft-ietf-lamps-csr-attestation · Working group: lamps
Agenda: a) draft-ietf-lamps-csr-attestation (Mike)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/ | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Certification Authorities (CAs) issuing certificates to Public Key Infrastructure (PKI) end entities may require a certificate signing request (CSR) to include additional verifiable information to confirm policy compliance. For example, a CA may require an end entity to demonstrate that the private key corresponding to a CSR's public key is secured by a hardware security module (HSM), is not exportable, etc. The process of generating, transmitting, and verifying additional information required by the CA is called remote attestation. While work is currently underway to standardize various aspects of remote attestation, a variety of proprietary mechanisms have been in use for years, particularly regarding protection of private keys. This specification defines ASN.1 structures which may carry attestation data for PKCS#10 and Certificate Request Message Format (CRMF) messages. Both standardized and proprietary attestation formats are supported by this specification.

### Is it time for RFC7030bis?
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-is-it-time-for-rfc7030bis-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### EST Renewal Info
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-est-renewal-info-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Attestation Key EKU
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-attestation-key-eku-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Certificate Discovery
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-certificate-discovery-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Best Practices for CMS SignedData with Regards to Signed Attributes
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-best-practices-for-cms-signeddata-with-regards-to-signed-attributes-01 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### CMCbis Updates
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-cmcbis-updates-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### One Signature Certs
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lamps-one-signature-certs-00 | video: https://youtu.be/wnW-Mk61OAY | materials: https://datatracker.ietf.org/meeting/124/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

## Working Group: lsr

### IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)
Draft: draft-many-lsr-power-group · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-many-lsr-power-group/
page: https://datatracker.ietf.org/doc/draft-many-lsr-power-group/ | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
[I-D.many-teas-power-steering] introduces a Power Conserving Path Placement Strategy (PCPPS). When possible, PCPPS concentrates traffic onto a small set of network resources. When traffic is concentrated onto a small set of network resources, other network resources become idle and can be powered down until they are needed again. This conserves energy and reduces environmental impact. PCPPS uses information that is distributed by an IGP. This document specifies the IS-IS encoding for that information.

### Metric Normalize for IGP Flex-algo
Draft: draft-gl-lsr-metric-normalize · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/
page: https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-slides-124-lsr-03-metric-normalize-00-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
When multiple links in a network have the same metric, they can serve as ECMP equivalent links for load balancing during forwarding. However, slight fluctuations in metric values can prevent the formation of ECMP equivalent links, leading to the idle state of suboptimal links and thus wasting bandwidth resources. This document proposes a metric normalization method by advertising metric normalization parameters corresponding to a specific Metric- Type for Flexible Algorithm. During route calculation, slight fluctuations across multiple links are adjusted according to these normalization parameters, making the computed metric values more consistent. This approach enables the formation of ECMP equivalent links and promotes load sharing in the forwarding process.

### ISIS Hierarchical SNPs
Draft: draft-prz-lsr-hierarchical-snps · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-prz-lsr-hierarchical-snps/
page: https://datatracker.ietf.org/doc/draft-prz-lsr-hierarchical-snps/ | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
The document presents an optional new type of SNP called a Hierarchical SNP (HSNP). When feasible, it compresses traditional CSNP exchanges into a Merkle tree-like structure, which speeds up synchronization of large databases and adjacency numbers while reducing the load from regular CSNP exchanges during normal operation.

### LSR-Status
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-1-lsr-status-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### IETF124-isis-power-groups
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-ietf124-isis-power-groups-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### HSNP (updated a bit)
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-hsnp-updated-a-bit-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### Optimizing
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-optimizing-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### flood reduction measurements rerun
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-flood-reduction-measurements-rerun-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### LSR-YANG
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-lsr-5-lsr-yang-00 | video: https://youtu.be/jIDKLTd6Gzw | materials: https://datatracker.ietf.org/meeting/124/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

## Working Group: masque

### DNS and PREF64 Configuration for Proxying IP in HTTP
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-masque-dns-and-pref64-configuration-for-proxying-ip-in-http-00 | video: https://youtu.be/qkaV6behXDo | materials: https://datatracker.ietf.org/meeting/124/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### Reusable templates and checksum offload for CONNECT-IP
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-masque-reusable-templates-and-checksum-offload-for-connect-ip-00 | video: https://youtu.be/qkaV6behXDo | materials: https://datatracker.ietf.org/meeting/124/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### ECN and DSCP support for HTTPS's Connect-UDP
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-masque-ecn-and-dscp-support-for-httpss-connect-udp-00 | video: https://youtu.be/qkaV6behXDo | materials: https://datatracker.ietf.org/meeting/124/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

## Working Group: oauth

### SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)
Draft: draft-ietf-oauth-sd-jwt-vc · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-sd-jwt-vc-00 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification describes data formats as well as validation and processing rules to express Verifiable Digital Credentials with JSON payloads with and without selective disclosure based on the SD-JWT format.

### Identity Assertion JWT Authorization Grant
Draft: draft-ietf-oauth-identity-assertion-authz-grant · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-identity-assertion-authorization-grant-00 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification provides a mechanism for an application to use an identity assertion to obtain an access token for a third-party API by coordinating through an identity provider that the downstream Resource Authorization Server already trusts for single sign-on (SSO), using OAuth 2.0 Token Exchange (RFC 8693) and the JWT Profile for OAuth 2.0 Authorization Grants (RFC 7523). This pattern is informally referred to as Cross-App Access (XAA).

### Updates to OAuth 2.0 JSON Web Token (JWT) Client Authentication and Assertion-Based Authorization Grants
Draft: draft-ietf-oauth-rfc7523bis · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/ | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This document updates RFC7521, RFC7522, RFC7523 and RFC9126 with respect to the treatment of audience values in OAuth 2.0 Client Assertion Authentication and Assertion-based Authorization Grants to address a security vulnerability identified in the previous requirements for those audience values in multiple OAuth 2.0 specifications.

### The OAuth 2.1 Authorization Framework
Draft: draft-ietf-oauth-v2-1 · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-delegated-authorization-00 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
The OAuth 2.1 authorization framework enables an application to obtain limited access to a protected resource, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and an authorization service, or by allowing the application to obtain access on its own behalf. This specification replaces and obsoletes the OAuth 2.0 Authorization Framework described in RFC 6749 and the Bearer Token Usage in RFC 6750.

### Application-Agnostic Demonstration Proof of Possession (DPoP) Framework
Draft: draft-nandakumar-oauth-dpop-proof · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-nandakumar-oauth-dpop-proof/
page: https://datatracker.ietf.org/doc/draft-nandakumar-oauth-dpop-proof/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-dpop-proof-00 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This document describes a generic framework for Demonstrating Proof of Possession (DPoP) that extends beyond HTTP-specific implementations. Building upon RFC 9449, this framework provides a protocol-agnostic approach for sender-constraining tokens through cryptographic proof of possession, enabling secure token binding across various application protocols and contexts.

### OAuth 2.0 Delegated Authorization
Draft: draft-li-oauth-delegated-authorization · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-li-oauth-delegated-authorization/
page: https://datatracker.ietf.org/doc/draft-li-oauth-delegated-authorization/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-refresh-token-and-authorization-expiration-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification defines Delegated Authorization Tokens, key-bound tokens that enable an OAuth client to delegate a constrained subset of its authorization to another client without contacting the authorization server for each delegation. An authorization server issues the root token and binds it to a client key. That client can use the bound key either to prove possession when accessing a protected resource or to sign a further token bound to a delegate client's key. Resource servers validate the ordered token chain, the restrictions imposed at every delegation step, and a DPoP proof signed by the key bound to the leaf token.

### OAuth 2.0 Attestation-Based Client Authentication
Draft: draft-ietf-oauth-attestation-based-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-attestation-based-client-authentication-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification defines an extension to the OAuth 2.0 protocol (RFC 6749) that enables a client instance to include a key-bound attestation when interacting with an Authorization Server or Resource Server. This mechanism allows a client instance to prove its authenticity, as verified by a client attester, without revealing its target audience to that attester. It may also serve as a mechanism for client authentication as per OAuth 2.0.

### OAuth Client ID Metadata Document
Draft: draft-ietf-oauth-client-id-metadata-document · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-client-id-metadata-document-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification defines a mechanism through which an OAuth client can identify itself to authorization servers, without prior dynamic client registration or other existing registration. This is through the usage of a URL as a client_id in an OAuth flow, where the URL refers to a document containing the necessary client metadata, enabling the authorization server to fetch the metadata about the client as needed.

### DPoP for the OAuth 2.0 Device Authorization Grant
Draft: draft-parecki-oauth-dpop-device-flow · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-parecki-oauth-dpop-device-flow/
page: https://datatracker.ietf.org/doc/draft-parecki-oauth-dpop-device-flow/ | materials: https://datatracker.ietf.org/meeting/124/session/oauth
The OAuth 2.0 Device Authorization Grant [RFC8628] is an authorization flow for devices with limited input capabilities. Demonstrating Proof of Possession (DPoP) [RFC9449] is a mechanism to sender-constrain OAuth 2.0 tokens. This document describes how to use DPoP with the Device Authorization Grant to provide a higher level of security for clients. It binds the DPoP key to the entire transaction, from the initial device authorization request through the lifetime of the issued tokens.

### OAuth 2.0 JWT Authorization Grant with DPoP Binding
Draft: draft-parecki-oauth-jwt-dpop-grant · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-parecki-oauth-jwt-dpop-grant/
page: https://datatracker.ietf.org/doc/draft-parecki-oauth-jwt-dpop-grant/ | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification defines a new OAuth 2.0 authorization grant type for exchanging a JSON Web Token (JWT) assertion that is bound to a key for an access token. To use the assertion, the client must prove possession of that key using the Demonstrating Proof of Possession (DPoP) mechanism. Unlike the JWT bearer grant, a stolen assertion cannot be used by a party that does not hold the private key.

### OAuth 2.0 App2App Browser-less Flow
Draft: draft-zehavi-oauth-app2app-browserless · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-zehavi-oauth-app2app-browserless/
page: https://datatracker.ietf.org/doc/draft-zehavi-oauth-app2app-browserless/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-app2app-browserless-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This document describes a protocol allowing a _Client App_ to obtain an OAuth grant from an _Authorization Server's Native App_ using the [App2App] pattern, providing *native* app navigation user-experience (no web browser used), despite both apps belonging to different trust domains.

### OAuth 2.0 Refresh Token and Authorization Expiration
Draft: draft-watson-oauth-refresh-token-expiration · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-watson-oauth-refresh-token-expiration/
page: https://datatracker.ietf.org/doc/draft-watson-oauth-refresh-token-expiration/ | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification extends OAuth 2.0 [RFC6749] by adding new token endpoint response parameters to specify refresh token expiration and user authorization expiration.

### Separating DPoP Bindings for Access and Refresh Tokens
Draft: draft-rosomakho-oauth-dpop-rt · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-rosomakho-oauth-dpop-rt/
page: https://datatracker.ietf.org/doc/draft-rosomakho-oauth-dpop-rt/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-separating-dpop-bindings-for-access-and-refresh-tokens-01 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This document defines an extension to OAuth 2.0 Demonstrating Proof- of-Possession at the application level (DPoP, RFC 9449) that allows refresh tokens to be bound to a different proof-of-possession key than access tokens. In the existing specification, a single DPoP proof is used to bind both tokens to the same key material. However, in many deployments, refresh tokens and access tokens are stored and managed in different security contexts. To support this operational separation, this document introduces a new HTTP header field, DPoP- RT, and corresponding DPoP-RT-Nonce mechanism, enabling independent proof-of-possession for refresh token use while preserving compatibility with existing DPoP-bound access tokens.

### OAuth SPIFFE Client Authentication
Draft: draft-schwenkschuster-oauth-spiffe-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/
page: https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-oauth-spiffe-client-authentication-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
This specification profiles the Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants [RFC7521] and JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants [RFC7523] to enable the use of SPIFFE Verifiable Identity Documents (SVIDs) as client credentials in OAuth 2.0. It defines how OAuth clients with SPIFFE credentials can authenticate to OAuth authorization servers using their JWT-SVIDs or X.509-SVIDs without the need for client secrets. This approach enhances security by enabling seamless integration between SPIFFE-enabled workloads and OAuth authorization servers while eliminating the need to distribute and manage shared secrets such as static client secrets.

### Transaction Tokens
Draft: draft-ietf-oauth-transaction-tokens · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-transaction-tokens-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Transaction Tokens (Txn-Tokens) are designed to maintain and propagate user identity, workload identity and authorization context throughout the Call Chain within a trusted domain during the processing of external requests (e.g. such as API calls) or requests initiated internally within the Trust Domain. Txn-Tokens ensure that this context is preserved throughout the Call Chain thereby enhancing security and consistency in complex, multi-service architectures.

### Chais Slides
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-chais-slides-01 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### rfc7523bis
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-rfc7523bis-01 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### OAuth 2.1
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-oauth-21-00 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Browser Swapping
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-browser-swapping-01 | video: https://youtu.be/jSC4rGzkoh8 | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### DPoP Stuff
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-dpop-stuff-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### JSON Web Token Best Current Practices
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-json-web-token-best-current-practices-00 | video: https://youtu.be/lT_E5vbqAyc | materials: https://datatracker.ietf.org/meeting/124/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

## Working Group: pquip

### Hash-based Signatures: State and Backup Management
Draft: draft-ietf-pquip-hbs-state · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-ietf-pquip-hbs-state/
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-hbs-state/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-pquip-stateful-hash-based-signatures-backup-and-state-management-update-00 | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
Stateful Hash-Based Signature Schemes (Stateful HBS) such as Leighton-Micali Signature (LMS), Hierarchical Signature System (HSS), eXtended Merkle Signature Scheme (XMSS), and XMSS^MT combine Merkle trees with One-Time Signatures (OTS) to provide signatures that are resistant against attacks using large-scale quantum computers. Unlike conventional stateless digital signature schemes, Stateful HBS have a state to keep track of which OTS keys have been used, as double-signing with the same OTS key allows forgeries. This document provides guidance and catalogs security considerations for the operational and technical aspects of deploying systems that rely on Stateful HBS. Management of the state of the Stateful HBS, including any handling of redundant key material, is a sensitive topic. This document describes some approaches to handle the associated challenges. It also describes the challenges that need to be resolved before certain approaches should be considered.

### Adapting Constrained Devices for Post-Quantum Cryptography
Draft: draft-ietf-pquip-pqc-hsm-constrained · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-pquip-adapting-constrained-devices-for-post-quantum-cryptography-draft-ietf-pquip-pqc-hsm-constrained-00 | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
This document provides guidance on integrating Post-Quantum Cryptography (PQC) into resource-constrained devices, such as IoT nodes and dedicated key-storage hardware. These systems often operate with strict limitations on processing power, RAM, and flash memory, and may even be battery-powered. The document emphasizes the role of hardware security as the basis for secure operations, supporting features such as seed-based key generation to minimize persistent storage, efficient handling of ephemeral keys, and the offloading of cryptographic tasks in low-resource environments. It also explores the implications of PQC on firmware update mechanisms in such constrained systems.

### Post-Quantum Algorithms guidance
Draft: draft-prabel-pquip-pqc-guidance · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-prabel-pquip-pqc-guidance/
page: https://datatracker.ietf.org/doc/draft-prabel-pquip-pqc-guidance/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-pquip-post-quantum-algorithms-guidance-00 | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
This document provides general information (such as parameter sizes, security assumptions, and targeted security models) on a range of widely studied post-quantum cryptographic algorithms, including Key Encapsulation Mechanisms (KEMs) and digital signature schemes. The cryptographic schemes described in this document are among those recommended by major security agencies and/or standardization bodies, and are believed to be secure against Cryptographically Relevant Quantum Computer (CRQC). The goal of this document is to offer a high-level overview of these schemes and their distinguishing features, to help implementers, protocol designers, standards developers, and policymakers in understanding and selecting appropriate post-quantum cryptographic primitives for use in protocols and systems. By aggregating and presenting this information in a unified format, this document aims to facilitate informed decision-making and interoperability during the migration to post-quantum cryptography, and to encourage consistent practices when evaluating and deploying Post-Quantum Cryptography (PQC) schemes in cryptographic protocols.

### Guidance for Migration to Composite, Dual, or PQC Authentication
Draft: draft-reddy-pquip-pqc-signature-migration · Working group: pquip
Agenda: draft-reddy-pquip-pqc-signature-migration
page: https://datatracker.ietf.org/doc/draft-reddy-pquip-pqc-signature-migration/ | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
This document provides guidance for migration from traditional digital signature algorithms to post-quantum cryptographic (PQC) signature algorithms. It compares three models under discussion in the IETF for PKI-based protocols: composite certificates, dual certificates, and PQC certificates. The goal is to help operators and engineers working on cryptographic libraries, network security, and PKI/key management infrastructure select an approach that balances interoperability, security, and operational efficiency during the transition to post-quantum authentication.

### Guidance for migration to Post-Quantum Cryptography
Draft: draft-kwiatkowski-pquip-pqc-migration · Working group: pquip
Agenda: draft-kwiatkowski-pquip-pqc-migration
page: https://datatracker.ietf.org/doc/draft-kwiatkowski-pquip-pqc-migration/ | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
This document provides guidance on migration to post-quantum cryptography (PQC) in internet protocols. It outlines the challenges and considerations that protocol designers and implementers should take into account when transitioning from traditional cryptographic algorithms to PQC algorithms, which are designed to be secure against quantum computer attacks. It is intended for cryptographic protocol designers within the IETF community, as well as technology developers and implementers responsible for deploying PQC standards.

### A Mechanism for Encoding Differences in Paired Certificates
Draft: draft-bonnell-lamps-chameleon-certs · Working group: pquip
Agenda: draft-bonnell-lamps-chameleon-certs
page: https://datatracker.ietf.org/doc/draft-bonnell-lamps-chameleon-certs/ | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
This document specifies a method to efficiently convey the differences between two certificates in an X.509 version 3 extension. This method allows a relying party to extract information sufficient to reconstruct the paired certificate and perform certification path validation using the reconstructed certificate. In particular, this method is especially useful as part of a key or signature algorithm migration, where subjects may be issued multiple certificates containing different public keys or signed with different CA private keys or signature algorithms. This method does not require any changes to the certification path validation algorithm as described in RFC 5280. Additionally, this method does not violate the constraints of serial number uniqueness for certificates issued by a single certification authority.

### Root CA Certificate Rekeying in the Scenario of Post Quantum Migration
Draft: draft-wang-lamps-root-ca-cert-rekeying · Working group: pquip
Agenda: draft-wang-lamps-root-ca-cert-rekeying
page: https://datatracker.ietf.org/doc/draft-wang-lamps-root-ca-cert-rekeying/ | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
In the public key infrastructures (PKIs), root certification authority (CA) certificate rekeying is crucial to guarantee business continuity. Two approaches are given in [RFC4210] for entities which are belonging to different generations to verify each other's certificate chain. However, these approaches rely on the assumption that the old entities can be updated. In this draft, we propose a One-way Link Certificate based solution such that old entities are transparent to root CA certificate rekeying. Namely, during the overlapping lifetime of two root CA certificates, without any update in old entities, old and new entities can verify each other's certificate chain smoothly. Furthermore, the proposed solution works in both traditional PKIs, and post-quantum (PQ) PKIs, where the certificate can be pure PQ or hybrid ones.

### PQC migration use cases for the telecom network
Draft: draft-li-pquip-teleco-pqc-migration · Working group: pquip
Agenda: draft-li-pquip-teleco-pqc-migration
page: https://datatracker.ietf.org/doc/draft-li-pquip-teleco-pqc-migration/ | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
Telecommunications (Telecom) networks are important infrastructure. 3rd Generation Partnership Project (3GPP) provides security specifications for telecom networks, including network devices and user terminals. Meanwhile, the security protocols from IETF widely used in telecom systems. This docuemnt presents some post-quantum risks and assessments that exist in current telecom network, analyzes possible post-quantum migration cases and potential strategy in typical telecom network, the strategy includes the suggestion of related IETF protocols and profiles.

### PQC Escape Message for Dynamic Migration
Draft: draft-li-pquip-escape-message · Working group: pquip
Agenda: draft-li-pquip-escape-message
page: https://datatracker.ietf.org/doc/draft-li-pquip-escape-message/ | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
In this contribution, a design of escape message mechanism is proposed, where the service provider sends an escape message to the service consumer using existing non-PQC connection and then starts to re-establish the quantum-safe protocol. The proposed escape message can potentially be used in a variety of protocols, including IPsec, TLS, or between the air interface of a cellphone and a network device. We believe that for largely deployed networks and entities, escape messages can be provided as a plan B for always-live devices of service provider and consumer that cannot complete post-quantum migration in advance and mitigates negative impacts after potential Q-days occur. Different protocols and devices may be implemented escape mechanism in different sepcific ways.

### PQUIP-ETSI-CAMPAGNA
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-pquip-pquip-etsi-campagna-00 | video: https://youtu.be/vCt3-x0_bhU | materials: https://datatracker.ietf.org/meeting/124/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

## Working Group: quic

### Qlog
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-quic-qlog-00 | video: https://youtu.be/NIlCm62G0V8 | materials: https://datatracker.ietf.org/meeting/124/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### QUIC Packet Receive Timestamps
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-quic-quic-packet-receive-timestamps-00 | video: https://youtu.be/NIlCm62G0V8 | materials: https://datatracker.ietf.org/meeting/124/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Qmux
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-quic-qmux-00 | video: https://youtu.be/NIlCm62G0V8 | materials: https://datatracker.ietf.org/meeting/124/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### New Preferred Address
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-quic-new-preferred-address-00 | video: https://youtu.be/NIlCm62G0V8 | materials: https://datatracker.ietf.org/meeting/124/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Exchanging CC data in QUIC
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-quic-exchanging-cc-data-in-quic-01 | video: https://youtu.be/NIlCm62G0V8 | materials: https://datatracker.ietf.org/meeting/124/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

## Working Group: rats

### Concise Reference Integrity Manifest
Draft: draft-ietf-rats-corim · Working group: rats
Agenda: (10+5 min) Yogesh Deshpande - draft-ietf-rats-corim
page: https://datatracker.ietf.org/doc/draft-ietf-rats-corim/ | materials: https://datatracker.ietf.org/meeting/124/session/rats
Remote Attestation Procedures (RATS) enable Relying Parties to assess the trustworthiness of a remote Attester and therefore to decide whether or not to engage in secure interactions with it. Evidence about trustworthiness can be rather complex and it is deemed unrealistic that every Relying Party is capable of the appraisal of Evidence. Therefore that burden is typically offloaded to a Verifier. In order to conduct Evidence appraisal, a Verifier requires not only fresh Evidence from an Attester, but also trusted Endorsements and Reference Values from Endorsers and Reference Value Providers, such as manufacturers, distributors, or device owners. This document specifies the information elements for representing Endorsements and Reference Values in CBOR format.

### Evidence Encoding for Hardware Security Modules
Draft: draft-ietf-rats-pkix-key-attestation · Working group: rats
Agenda: (10+5 min) Jean-Pierre Fiset - draft-ietf-rats-pkix-key-attestation
page: https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-integration-of-remote-attestation-with-key-negotiation-and-distribution-00 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
This document specifies a vendor-agnostic format for Evidence produced and verified within a PKIX context. The Evidence produced this way includes claims collected about a cryptographic module, such as a Hardware Security Module (HSM), and elements found within it such as cryptographic keys. One scenario envisaged is that the state information about the cryptographic module can be securely presented to a remote operator or auditor in a vendor-agnostic verifiable format. A more complex scenario would be to submit this Evidence to a Certification Authority to aid in determining whether the storage properties of this key meet the requirements of a given certificate profile.

### Remote Attestation with Multiple Verifiers
Draft: draft-deshpande-rats-multi-verifier · Working group: rats
Agenda: (15+5 min) Jun Zhang - draft-deshpande-rats-multi-verifier
page: https://datatracker.ietf.org/doc/draft-deshpande-rats-multi-verifier/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-remote-attestation-with-multiple-verifiers-01 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
IETF RATS Architecture, defines the key role of a Verifier. In a complex system, this role needs to be performed by multiple Verfiers coordinating together to assess the full trustworthiness of an Attester. This document focuses on various topological patterns for a multiple Verifier system. It only covers the architectural aspects introduced by the Multi Verifier concept, which is neutral with regard to specific wire formats, encoding, transport mechanisms, or processing details.

### Integration of Remote Attestation with Key Negotiation and Key Distribution mechanisms
Draft: draft-xia-rats-key-negotiation-integration · Working group: rats
Agenda: (10+5 min) Jun Zhang - draft-xia-rats-key-negotiation-integration
page: https://datatracker.ietf.org/doc/draft-xia-rats-key-negotiation-integration/ | materials: https://datatracker.ietf.org/meeting/124/session/rats
This document describes a generic way to integrate Remote Attestation (RA) with key distribution and key negotiation, so that cryptographic keys are only released to or accepted from attested and policy- compliant environments. It defines an attestation-bound key management mechanism that can be applied on top of existing secure channel and key management protocols, and illustrates it with three representative scenarios: public-cloud KMS, end-user to AI data- center communication, and enterprise-operated KMS. A format-agnostic key binding claim is introduced to express the binding between an Attester’s environment, its public keys, and a session identifier, enabling Relying Parties to use Attestation Results as an input to key distribution and key agreement decisions without changing underlying protocols.

### Taxonomy of Composite Attesters
Draft: draft-richardson-rats-composite-attesters · Working group: rats
Agenda: (15+5 min) Michael Richardson - draft-richardson-rats-composite-attesters
page: https://datatracker.ietf.org/doc/draft-richardson-rats-composite-attesters/ | materials: https://datatracker.ietf.org/meeting/124/session/rats
This document was attempting to clarifys and extends the meaning of Composite Attester from RFC9334. It has since been moved into the RATS wiki, and this I-D serves as a tombstone. A system of annotated diagram components is defined as a small language to explain the different ways that components can interact to form composites. These diagram components are then used to define a few popular classes of composites.

### Guidelines for Security Considerations of RATS
Draft: draft-rats-sardar-sec-cons · Working group: rats
Agenda: (15 min) Usama Sardar - https://datatracker.ietf.org/doc/draft-rats-sardar-sec-cons/
page: https://datatracker.ietf.org/doc/draft-rats-sardar-sec-cons/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-guideline-for-security-considerations-of-rats-00 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
This document aims to provide guidelines and best practices for writing security considerations for technical specifications for RATS targeting the needs of implementers, researchers, and protocol designers.

### Concise Selector for Endorsements and Reference Values
Draft: draft-ietf-rats-coserv · Working group: rats
Agenda: (10+5 min) Paul Howard - draft-ietf-rats-coserv
page: https://datatracker.ietf.org/doc/draft-ietf-rats-coserv/ | materials: https://datatracker.ietf.org/meeting/124/session/rats
In the Remote Attestation Procedures (RATS) architecture, Verifiers require Endorsements and Reference Values to assess the trustworthiness of Attesters. This document specifies the Concise Selector for Endorsements and Reference Values (CoSERV), a structured query/result format designed to facilitate the discovery and retrieval of these artifacts from various providers. CoSERV defines a query language and corresponding result structure using CDDL, which can be serialized in CBOR format, enabling efficient interoperability across diverse systems.

### Geographic Attestation Results
Draft: draft-richardson-rats-geographic-results · Working group: rats
Agenda: (15 min) Michael Richardson, Ramki Krishnan - draft-richardson-rats-geographic-results
page: https://datatracker.ietf.org/doc/draft-richardson-rats-geographic-results/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-geographic-attestation-results-ways-forward-slides-124-rats-geographic-attestation-results-ways-forward-00 | video: https://youtu.be/N4xkqwPrTJw | materials: https://datatracker.ietf.org/meeting/124/session/rats
Many workloads have limitations on what geography they are allowed to operate in. This is often due to a regulation that requires that the computation occur in a particular jurisdiction. There are many mechanisms by which Evidence of location may be created and then evaluated by a Verifier. No matter which mechanism is appropriate for a given situation, the result of the Verification can be expressed in a similiarly defined EAT Attestation Result. This document is about encoding a variety of geographical conclusions conclusions in an Attestation Result. In addition, one mechanism of directly creating a geographic result in the form of an Endorsement is described in an appendix.

### Remote Attestation for Trustworthy Workload Identity
Draft: draft-novak-twi-attestation · Working group: rats
Agenda: (30 min) Mark Novak - draft-novak-twi-attestation
page: https://datatracker.ietf.org/doc/draft-novak-twi-attestation/ | materials: https://datatracker.ietf.org/meeting/124/session/rats
Trustworthy Workloads are workloads that operate in environments that provide isolation of data in use. This document describes how Trustworthy workloads can acquire credentials containing stable identifiers, upon proving the trust in the environments in which they operate via Remote Attestation.

### IETF 124 CoRIM Slides
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-ietf-124-corim-slides-00 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### PKIX Evidence for HSMs
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-pkix-evidence-for-hsms-00 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Composite Attester
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-sessa-composite-attester-00 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### TWI and RATS Harmonization
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-twi-and-rats-harmonization-01 | video: https://youtu.be/TDtDVy9q704 | materials: https://datatracker.ietf.org/meeting/124/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### CoSERV Progress Update
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-coserv-progress-update-00 | video: https://youtu.be/N4xkqwPrTJw | materials: https://datatracker.ietf.org/meeting/124/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Guideline for Security consideration of RATS
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rats-sessb-guideline-for-security-consideration-of-rats-00 | video: https://youtu.be/N4xkqwPrTJw | materials: https://datatracker.ietf.org/meeting/124/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

## Working Group: rtgwg

### Multicast use case in LLM MoE
Draft: draft-zhang-rtgwg-llmmoe-multicast · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-zhang-rtgwg-llmmoe-multicast/
page: https://datatracker.ietf.org/doc/draft-zhang-rtgwg-llmmoe-multicast/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-02-llm-moe-multicast-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Large Language Models (LLMs) have been widely used in recent years. The Mixture of Experts (MoE) architecture is one of the features of LLMs that enables efficient inference and cost-effective training. With the MoE architecture, there are potential multicast use cases such as tokens dispatching. This draft attempts to analyze these use cases.

### Distributed Inference Network (DIN) Problem Statement, Use Cases, and Requirements
Draft: draft-song-rtgwg-din-usecases-requirements · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-song-rtgwg-din-usecases-requirements/
page: https://datatracker.ietf.org/doc/draft-song-rtgwg-din-usecases-requirements/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-distributed-inference-network-din-problem-statement-use-cases-and-requirements-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This document describes the problem statement, use cases, and requirements for a "Distributed Inference Network" (DIN) in the era of pervasive AI. As AI inference services become widely deployed and accessed by billions of users, applications and devices, traditional centralized cloud-based inference architectures face challenges in scalability, latency, security, and efficiency. DIN aims to address these challenges by leveraging distributed edge-cloud collaboration, intelligent scheduling, and enhanced network security to support low- latency, high-concurrency, and secure AI inference services.

### Agents Networking Architecture for Enterprise and Broadband
Draft: draft-zl-agents-networking-architecture · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-zl-agents-networking-architecture/
page: https://datatracker.ietf.org/doc/draft-zl-agents-networking-architecture/ | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This document introduces agents networking architecture and defines the core components of agent networking, as well as typical interactions among these key components.

### Scheduling Network Resources for Machine Learning Clusters
Draft: draft-kompella-rtgwg-mlnwsched · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-kompella-rtgwg-mlnwsched/
page: https://datatracker.ietf.org/doc/draft-kompella-rtgwg-mlnwsched/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-05-scheduling-network-resources-for-machine-learning-clusters-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Large Language Models (LLMs) are pushing the boundaries of technology. The scale that they have reached currently vastly exceeds the capacity of any single compute unit (XPU); this requires a distributed approach where multiple XPUs are connected via a "backend" network, sometimes in a single data center, but increasingly in multiple data centers connected by a "data center interconnect" (DCI). We are approaching the point where the scale exceeds that of a single data center, thus requiring multiple such data centers connected via a "data center interconnect" network. Training and inferencing are expensive and critical operations, thus they are typically scheduled, i.e., the (compute) resources they need are carefully estimated, allocated and deployed so that these resources are efficiently used. However, while compute investment in these LLM processing clusters dwarfs that of networks, it is becoming increasingly clear that the latter can greatly impact the former. This has been the focus of recent conferences, including the fantel Birds of a Feather meeting in IETF 123, @Scale: Networking 2025 and Open Compute Project 2025. This memo proposes that the same care that is taken regarding allocation of compute resources to jobs be taken with networking resources: that they are estimated, allocated and deployed alongside compute resources; that they have contingency plans in case of network glitches; and that a holistic view be taken in order to optimize job completion times of training and inferencing jobs.

### Fast Network Notifications Problem Statement
Draft: draft-dong-fantel-problem-statement · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-dong-fantel-problem-statement/
page: https://datatracker.ietf.org/doc/draft-dong-fantel-problem-statement/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-06-network-notifications-problem-statement-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Modern network applications, ranging from Artificial Intelligence (AI) /Machine Learning (ML) training to large-scale cloud services, require adaptive networks to ensure reliable and congestion-free data transfer within or across multiple data centers. A good and timely understanding of network operational status can help to enable faster response to critical events, so as to enable the selection of paths with reduced latency and improve network utilization. This document describes the existing problems and the need of fast network notification solutions.

### Advertising Router Information
Draft: draft-zzhang-rtgwg-router-info · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-zzhang-rtgwg-router-info/
page: https://datatracker.ietf.org/doc/draft-zzhang-rtgwg-router-info/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-draft-zzhang-rtgwg-router-info-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This document specifies a generic mechanism for a router to advertise some information to its neighbors. One use case of this mechanism is to advertise link/path information so that a receiving router can better react to network changes.

### Fast Congestion Notification Packet (CNP) with Proxy
Draft: draft-xiao-rtgwg-proxy-congestion-notification · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-xiao-rtgwg-proxy-congestion-notification/
page: https://datatracker.ietf.org/doc/draft-xiao-rtgwg-proxy-congestion-notification/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-08-proxy-congestion-notification-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This document describes the necessity and feasibility to introduce a proxy network node between the congested network node and the traffic sender. The proxy network node is used to translate the congestion notification. The congested network node sends the congestion notification to the proxy network node in a format defined in this document, and then the proxy network node translates the received congestion notification to a format known by the traffic sender and resends the translated congestion notification to the traffic sender.

### Congestion Control Based on SRv6 Path
Draft: draft-liu-rtgwg-srv6-cc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-liu-rtgwg-srv6-cc/
page: https://datatracker.ietf.org/doc/draft-liu-rtgwg-srv6-cc/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-congestion-control-based-on-srv6-path-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This document describes a congestion control solution based on SRv6. It defines mechanisms for congestion notification and flow control within an SRv6-based network, optimizing congestion handling through hierarchical congestion control messages along SRv6 paths.

### Fast Notification for tunnel-based lossless RDMA transmission in WAN
Draft: draft-hzh-fantel-wan-tunnel · Working group: rtgwg
Agenda: https://www.ietf.org/archive/id/draft-hzh-fantel-wan-tunnel-01.txt
page: https://datatracker.ietf.org/doc/draft-hzh-fantel-wan-tunnel/ | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
With the rapid development of Large Language Models (LLMs), many emerging AI services require lossless transmission of RDMA traffic over tunnels in Wide Area Network(WAN). Existing network mechanisms were not designed for the responsiveness and scale required by these dynamic services. WAN should support the real-time, lightweight network notification to enhance the responsiveness for traffic engineering, congestion mitigation, and failure protection. This document analyzes typical scenarios where RDMA traffic need to be tunneled across WAN, and proposes fast network notification solutions based on ICMPv6 or UDP.

### Credit-based Flow Control Based on RSVP for RDMA transmission in WAN
Draft: draft-hu-rtgwg-cbfc-rsvp · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-hu-rtgwg-cbfc-rsvp/
page: https://datatracker.ietf.org/doc/draft-hu-rtgwg-cbfc-rsvp/ | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This draft defines the Credit-based flow control mechanism for WAN based on the RSVP protocol. With the increasing demand for AI computing power, the computing power of a single AIDC can no longer meet the needs of large model training. This has given rise to cross-AIDC distributed model training, driving the demand for transmitting RDMA packets over WAN networks. AI training is extremely sensitive to network packet loss, and even a small amount of packet loss may lead to a significant decline in training efficiency. In addition, the elephant flow and extreme concurrent traffic also place higher demands on network performance. Credit- based flow control is a Backpressure-based traffic management technology, which has high reliability and stability in practical applications. It can provide high-throughput and zero-packet-loss transmission guarantees for RDMA traffic, effectively ensuring the efficiency of cross-data center AI training. This draft focuses on the scenario where RDMA packets are transmitted through SRv6 tunnels in the WAN and further expands the capabilities of the RSVP protocol in WAN. This draft introduces the Credit-based flow control mechanism into the RSVP protocol to achieve precise traffic control and provides processing analysis.

### Kademlia-directed ID-based Routing Architecture (KIRA)
Draft: draft-bless-rtgwg-kira · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-bless-rtgwg-kira/
page: https://datatracker.ietf.org/doc/draft-bless-rtgwg-kira/ | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
This document describes the Kademlia-directed ID-based Routing Architecture KIRA. KIRA is a scalable zero-touch distributed routing solution that is tailored to control planes. It prioritizes scalable and resilient connectivity over route efficiency (stretched paths are accepted as trade-off against routing protocol overhead). KIRA's self-assigned, topologically independent IDs can be embedded into IPv6 addresses. Combined with further self-organization mechanisms from Kademlia, KIRA achieves a zero-touch solution that provides scalable IPv6 connectivity without requiring any manual configuration. For example, it can connect hundreds of thousands of routers and devices in a single network without requiring any form of hierarchy (like areas). It works well in various topologies and is loop-free even during convergence. This self-contained solution, and especially the independence from any manual configuration, make it suitable as a resilient base for all management and control tasks, allowing the network to recover from the most complex failure scenarios. The architecture consists of the ID-based network layer routing protocol R²/Kad in its Routing Tier (using source routing) and a PathID-based Forwarding Tier (using PathIDs as labels for paths). KIRA’s tightly integrated add-on services (e.g., name resolution as well as fast and efficient topology discovery) provide a perfect basis for autonomic network management solutions.

### Agent networking use cases, requirements, and architecture
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-04-agent-networking-use-cases-requirements-and-architecture-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### FANTEL for RDMA transmission in WAN
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-fantel-for-rdma-transmission-in-wan-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### KIRA
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-kira-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### 031-Distributed Inference Network (DIN) Problem Statement, Use Cases, and Requirements 01
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-distributed-inference-network-din-problem-statement-use-cases-and-requirements-01-00 | video: https://youtu.be/cFekE0TpHng | materials: https://datatracker.ietf.org/meeting/124/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

## Working Group: savnet

### Problem Statement, Gap Analysis, and Requirements for Intra-domain Source Address Validation
Draft: draft-ietf-savnet-intra-domain-problem-statement · Working group: savnet
Agenda: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-problem-statement/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-source-address-validation-in-intra-domain-networks-gap-analysis-problem-statement-and-requirements-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Source address validation (SAV) is an important means to mitigate IP source address spoofing [RFC2827]. This document analyzes the gaps in current operational mechanisms for intra-domain SAV. It also identifies the properties that new intra-domain SAV mechanisms are expected to provide.

### Intra-domain Source Address Validation Architecture
Draft: draft-ietf-savnet-intra-domain-architecture · Working group: savnet
Agenda: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-intra-domain-source-address-validation-savnet-architecture-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document describes a generic architecture for intra-domain Source Address Validation (SAV). It provides a common framework for developing new intra-domain SAV mechanisms and describes the conditions under which this architecture can improve SAV accuracy and operational efficiency with respect to existing intra-domain SAV mechanisms.

### Source Prefix Advertisement for Intra-domain SAVNET
Draft: draft-li-savnet-source-prefix-advertisement · Working group: savnet
Agenda: https://datatracker.ietf.org/doc/draft-li-savnet-source-prefix-advertisement/
page: https://datatracker.ietf.org/doc/draft-li-savnet-source-prefix-advertisement/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-source-prefix-advertisement-for-intra-domain-savnet-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document describes a mechanism for generating interface-based prefix allowlists for intra-domain source address validation (SAV) on external interfaces facing directly connected hosts or non-BGP customer networks. The mechanism derives source prefixes from routing information and combines them with source prefixes provisioned by the AS operator. Routers use the combined source prefixes to generate SAV allowlists.

### General Source Address Validation Capabilities
Draft: draft-ietf-savnet-general-sav-capabilities · Working group: savnet
Agenda: Draft link: draft-ietf-savnet-general-sav-capabilities-02
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-general-sav-capabilities/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-updates-on-general-source-address-validation-capabilities-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
The SAV rules of existing source address validation (SAV) mechanisms are derived from other core data structures (e.g., FIB-based uRPF) that are not dedicatedly designed for source filtering. Consequently, these mechanisms have limitations in deployable scenarios and traffic handling policies. To overcome these limitations, this document introduces general SAV capabilities from a data plane perspective. How to implement the capabilities and how to generate SAV rules are not in the scope of this document.

### Provider Interface SAV for Customer Cone Sources
Draft: draft-huang-savnet-pi-sav-for-cc · Working group: savnet
Agenda: Draft link: draft-huang-savnet-pi-sav-for-cc-00
page: https://datatracker.ietf.org/doc/draft-huang-savnet-pi-sav-for-cc/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-provider-interface-sav-for-customer-cone-sources-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Current source address validation (SAV) on an AS's provider interfaces mainly relies on loose uRPF, which cannot defend against IP spoofing using routable prefixes and is ineffective when a default route is present. This document describes a *framework* for provider interface source address validation against spoofing of customer cone source prefixes (PI-SAV for CC). Two architectural approaches are presented: * *PI-SAV for Standalone CC*: a static solution that builds a blocklist based on topology information from BGP RIBs, RPKI ASPA, and local configuration (SLURM) etc. It requires no inter-AS communication. * *PI-SAV for Standalone+ CC*: an enhanced solution that uses lightweight query-response coordination between the top AS and member ASes to identify sub-cones that do not actually cause traffic detours, thereby enlarging the effective blocklist. This document is *informational* and provides only the framework, conceptual procedures, and requirements for future protocol specifications. Detailed wire protocols (e.g., for partial transit information provisioning or for query-response messaging) are out of scope and will be defined in separate documents.

### Path Computation Element Communication Protocol for Source Address Validation
Draft: draft-song-pce-pcep-sav · Working group: savnet
Agenda: https://datatracker.ietf.org/doc/draft-song-pce-pcep-sav/ Time needed
page: https://datatracker.ietf.org/doc/draft-song-pce-pcep-sav/ | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document presents a method of Path Computation Element (PCE) for Source Address Validation (SAV) in networks. It extends Path Computation Element Communication Protocol (PCEP) to support SAV policy distribution and synchronization between PCEP speakers for threat mitigation for source address spoofing.

### A Profile for Traffic Origin Authorizations (TOAs)
Draft: draft-qin-savnet-toa · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-qin-savnet-toa/
page: https://datatracker.ietf.org/doc/draft-qin-savnet-toa/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-a-profile-for-traffic-origin-authorizations-toas-01 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document defines a standard profile for Traffic Origin Authorizations (TOAs), a Cryptographic Message Syntax (CMS) protected content type for use with the Resource Public Key Infrastructure (RPKI). A TOA is a digitally signed object that provides a means of verifying that an IP address block holder has authorized an Autonomous System (AS) to originate traffic using source IP addresses within the address block.

### Advertising SAV Rule-related Information using BGP Link-State
Draft: draft-tong-idr-bgp-ls-sav-rule · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/
page: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/ | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document proposes extensions to the BGP Link-State protocol for advertising Source Address Validation (SAV) rule-related information for monitoring and management purposes.

### Export of Source Address Validation (SAV) Information in IPFIX
Draft: draft-cao-opsawg-ipfix-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-cao-opsawg-ipfix-sav/
page: https://datatracker.ietf.org/doc/draft-cao-opsawg-ipfix-sav/ | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document specifies the IP Flow Information Export Information Elements to export the context and outcome of Source Address Validation enforcement data. These SAV-specific Information Elements provide detailed insight into why packets are identified as spoofed by capturing the specific SAV rules that triggered validation decisions. This operational visibility is essential for network operators to observe SAV enforcement behavior and analyze source address spoofing events detected by SAV.

### YANG Data Model for Intra-domain and Inter-domain Source Address Validation (SAVNET)
Draft: draft-li-savnet-sav-yang · Working group: savnet
Agenda: https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/ Time needed
page: https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-yang-data-model-for-intra-domain-and-inter-domain-source-address-validation-savnet-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document describes a YANG data model for Intra-domain and Inter-domain Source Address Validation (SAVNET). The model serves as a base framework for configuring and managing an SAV subsystem, including SAV rule and SAV Tables, and expected to be augmented by other SAV technology models accordingly. Additionally, this document also specifies the model for the SAV Static application.

### Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation
Draft: draft-chen-bmwg-savnet-sav-benchmarking · Working group: savnet
Agenda: https://datatracker.ietf.org/doc/draft-chen-bmwg-savnet-sav-benchmarking/ Time
page: https://datatracker.ietf.org/doc/draft-chen-bmwg-savnet-sav-benchmarking/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-the-updates-on-the-benchmarking-methodology-for-intra-domain-and-inter-domain-source-address-validation-01 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
This document defines methodologies for benchmarking the performance of intra-domain and inter-domain source address validation (SAV) mechanisms. SAV mechanisms are utilized to generate SAV rules to prevent source address spoofing, and have been implemented with many various designs in order to perform SAV in the corresponding scenarios. This document takes the approach of considering a SAV device to be a black box, defining the methodology in a manner that is agnostic to the mechanisms. This document provides a method for measuring the performance of existing and new SAV implementations.

### Simulations of RPF SAV Methods(uRPF and BAR-SAV)
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-simulations-of-rpf-sav-methods-urpf-and-bar-sav-01 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### PCEP for SAV
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-07-pcep-for-sav-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Advertisement of Multi-Sourced SAV Rules using BGP Link-State
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-advertisement-of-multi-sourced-sav-rules-using-bgp-link-state-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Export of SAV Information in IPFIX
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-export-of-sav-information-in-ipfix-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Simulations of uRPF and BAR-SAV
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-savnet-simulations-of-urpf-and-bar-sav-00 | video: https://youtu.be/s0dL2xhpVzE | materials: https://datatracker.ietf.org/meeting/124/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

## Working Group: scitt

### Receipt Profiles Final
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-scitt-receipt-profiles-final-00 | video: https://youtu.be/Xds5RbciaxM | materials: https://datatracker.ietf.org/meeting/124/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

### SCITT and OCP Case Study
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-scitt-scitt-and-ocp-case-study-00 | video: https://youtu.be/Xds5RbciaxM | materials: https://datatracker.ietf.org/meeting/124/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

### FDA cyber security use case
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-scitt-fda-cyber-security-use-case-01 | video: https://youtu.be/Xds5RbciaxM | materials: https://datatracker.ietf.org/meeting/124/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

## Working Group: spice

### Use Cases for SPICE
Draft: draft-ietf-spice-use-cases · Working group: spice
Agenda: "Use Cases for SPICE" draft-ietf-spice-use-cases (Brent Zundel) - 5 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-use-cases/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spice-spice-use-cases-00 | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
This document describes various use cases related to credential exchange in a three party model (issuer, holder, verifier). These use cases aid in the identification of which Secure Patterns for Internet CrEdentials (SPICE) are most in need of specification or detailed documentation.

### GLobal Unique Enterprise (GLUE) Identifiers
Draft: draft-ietf-spice-glue-id · Working group: spice
Agenda: "GLobal Unique Enterprise (GLUE) Identifiers" draft-ietf-spice-glue-id (Brent Zundel) - 15 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-glue-id/ | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
This specification establishes a URI scheme for GLobal Unique Enterprise (GLUE) Identifiers. This enables URI identifiers to be used for businesses and organizations. It enables organizational identities from existing authorities to be represented within this URI scheme.

### OpenID Connect Standard Claims Registration for CBOR Web Tokens
Draft: draft-ietf-spice-oidc-cwt · Working group: spice
Agenda: "OpenID Connect standard claims registration for CBOR Web Tokens" draft-ietf-spice-oidc-cwt (Beltram Maldant) - 15 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-oidc-cwt/ | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
This document registers OpenID Connect standard claims already used in JSON Web Tokens for use in CBOR Web Tokens.

### Selective Disclosure CBOR Web Tokens (SD-CWT)
Draft: draft-ietf-spice-sd-cwt · Working group: spice
Agenda: "SPICE SD-CWT" draft-ietf-spice-sd-cwt 15+10 min (Rohan Mahy/Henk Birkholz) - 15 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spice-sd-cwt-update-for-ietf124-00 | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
This specification describes a data minimization technique for use with CBOR Web Tokens (CWTs). The approach is inspired by the Selective Disclosure JSON Web Token (SD-JWT), with changes to align with CBOR Object Signing and Encryption (COSE) and CWTs.

### A reference architecture for direct presentation credential flows
Draft: draft-johansson-direct-presentation-arch · Working group: spice
Agenda: Call for adoption: "A reference architecture for direct presentation credential flows' draft-johansson-direct-presentation-arch (Leif Johansson) - 15 min
page: https://datatracker.ietf.org/doc/draft-johansson-direct-presentation-arch/ | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
This document defines a reference architecture for direct presentation flows of digital credentials. The architecture introduces the concept of a presentation mediator as the active component responsible for managing, presenting, and selectively disclosing credentials while preserving a set of security and privacy promises that will also be defined. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/leifj/wallet-refarch.

### GLUE Identifiers
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spice-glue-identifiers-00 | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

### Slides OIDC claims
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spice-slides-oidc-claims-00 | video: https://youtu.be/O-wPFMHLDrI | materials: https://datatracker.ietf.org/meeting/124/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

## Working Group: spring

### Segment Routing over IPv6 (SRv6) Security Considerations
Draft: draft-ietf-spring-srv6-security · Working group: spring
Agenda: draft-ietf-spring-srv6-security
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-srv6-security-considerations-updates-for-ietf-124-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
Segment Routing over IPv6 (SRv6) is the instantiation of Segment Routing on the IPv6 data plane, using IPv6 addresses to identify segments. This document discusses security considerations in SRv6 networks, including the potential threats and the possible mitigation methods. The document does not define any new security protocols or extensions to existing protocols.

### SRv6 for Redundancy Protection
Draft: draft-ietf-spring-sr-redundancy-protection · Working group: spring
Agenda: draft-ietf-spring-sr-redundancy-protection
page: https://datatracker.ietf.org/doc/draft-ietf-spring-sr-redundancy-protection/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-srv6-for-redundancy-protection-pdf-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
Redundancy Protection is a generalized protection mechanism to achieve high reliability for services provided in Segment Routing networks. The mechanism uses the "Live-Live" methodology, i.e., multiple copies of the data packets are sent on different paths to provide protection. This document introduces one new SRv6 Segment Endpoint Behavior, the associated Headend Encapsulation Behaviors and the associated Redundancy Policy to provide replication and elimination functions on specific network nodes by leveraging SRv6 Network Programming capabilities.

### Export of Segment Routing Path Segment Identifier (PSID) Information in IPFIX
Draft: draft-ietf-opsawg-ipfix-path-segment · Working group: spring
Agenda: draft-ietf-opsawg-ipfix-path-segment
page: https://datatracker.ietf.org/doc/draft-ietf-opsawg-ipfix-path-segment/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-export-of-path-segment-identifier-information-in-ipfix-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
This document introduces new IPFIX Information Elements to identify the Segment Routing (SR) Path Segment Identifier (PSID) for SR-MPLS and SRv6 path identification.

### Segment Routing Policy Extension for Network Resource Partition
Draft: draft-jiang-spring-sr-policy-nrp · Working group: spring
Agenda: draft-jiang-spring-sr-policy-nrp
page: https://datatracker.ietf.org/doc/draft-jiang-spring-sr-policy-nrp/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-segment-routing-policy-extension-for-network-resource-partition-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
Segment Routing (SR) Policy is a set of candidate paths, each consisting of one or more segment lists and the associated information. A Network Resource Partition (NRP), is a subset of the resources and associated policies in the underlay network. In SR networks with multiple NRPs, an SR Policy can be associated with a particular NRP. In that case, SR Policy can be used for steering and forwarding traffic which is mapped to the NRP, so that the packets can be processed with the subset of network resources and policy of the NRP for guaranteed performance. Thus the association between SR Policy and NRP needs to be specified. This document defines extensions to the SR Policy Architecture to allow the association of the SR Policy candidate paths with NRPs.

### SRv6 SFC Architecture with SR-aware Functions
Draft: draft-watal-spring-srv6-sfc-sr-aware-functions · Working group: spring
Agenda: draft-watal-spring-srv6-sfc-sr-aware-functions
page: https://datatracker.ietf.org/doc/draft-watal-spring-srv6-sfc-sr-aware-functions/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-srv6-sfc-architecture-with-sr-aware-functions-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
This document describes the architecture of Segment Routing over IPv6 (SRv6) Service Function Chaining (SFC) with SR-aware functions. This architecture provides the following benefits: * Comprehensive Management: a centralized controller for SFC, handling SR Policy, link-state, and network metrics. * Simplicity: no SFC proxies, which reduces the number of nodes and address resource consumption. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Source Packet Routing in Networking Working Group mailing list (spring@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/spring/. Source for this draft and an issue tracker can be found at https://github.com/watal.

### Flexible Candidate Path Selection of SR Policy
Draft: draft-liu-spring-sr-policy-flexible-path-selection · Working group: spring
Agenda: draft-liu-spring-sr-policy-flexible-path-selection
page: https://datatracker.ietf.org/doc/draft-liu-spring-sr-policy-flexible-path-selection/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-flexible-candidate-path-selection-of-sr-policy-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
This document describes a flexible method for selecting candidate Segment Routing (SR) policy paths. Based on the real-time resource usage and forwarding quality of candidate paths, the head node can perform dynamic path switching among multiple candidate paths in the SR policy.

### SRv6 Policy SID List Optimization
Draft: draft-ali-spring-srv6-policy-sid-list-optimization · Working group: spring
Agenda: draft-ali-spring-srv6-policy-sid-list-optimization
page: https://datatracker.ietf.org/doc/draft-ali-spring-srv6-policy-sid-list-optimization/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-draft-ali-spring-srv6-policy-sid-list-optimization-01-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
Segment Routing (SR) allows a node to steer a packet flow along any path. SR Policy is an ordered list of segments (i.e., instructions) that represent a source-routed policy. The packets steered into an SR Policy carry an ordered list of segments associated with that SR Policy. An SR Policy can be instantiated SR-MPLS and SRv6 data planes. In some use cases, an SRv6 Policy's SID list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This draft specifies procedures to indicate whether the endpoint's node SID needs to be included or excluded when installing the SRv6 Policy.

### OAM for Service Programming with Segment Routing
Draft: draft-ali-spring-sr-service-programming-oam · Working group: spring
Agenda: draft-ali-spring-sr-service-programming-oam
page: https://datatracker.ietf.org/doc/draft-ali-spring-sr-service-programming-oam/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-draft-ali-spring-sr-service-programming-oam-08-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
This document defines the Operations, Administrations and Maintenance (OAM) for service programming in SR-enabled MPLS and IP networks.

### ICMP Error Handling in SRv6 based VPN Networks
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-draft-ali-6man-srv6-vpn-icmp-error-handling-01-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

### Multipath Traffic Engineering for Segment Routing
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-spring-multipath-traffic-engineering-for-segment-routing-00 | video: https://youtu.be/m9Mgfp3orlA | materials: https://datatracker.ietf.org/meeting/124/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

## Working Group: srv6ops

### SRv6 Deployment Options
Draft: draft-ietf-srv6ops-srv6-deployment · Working group: srv6ops
Agenda: draft-ietf-srv6ops-srv6-deployment
page: https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6-deployment/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-srv6-deployment-00 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
When deciding to migrate a network from existing data-plane technologies (e.g. MPLS, SR-MPLS or overlay encapsulations such as VXLAN) to SRv6, common questions involve how to perform the migration, how to minimize impact to the existing network and what techniques are available to support a smooth transition. This document presents various deployment and migration options for networks evolving toward SRv6 from prior transport or overlay technologies.

### Operational Guidance for Protection Mechanisms in SRv6 Networks
Draft: draft-liu-srv6ops-sr-protection · Working group: srv6ops
Agenda: draft-liu-srv6ops-sr-protection
page: https://datatracker.ietf.org/doc/draft-liu-srv6ops-sr-protection/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-operational-guidance-for-protection-mechanisms-in-srv6-networks-01 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
This document describes the Operational Guidance for protection of Segment Routing Over IPv6 (SRv6) networks.

### SRv6 OAM Deployment Consideration
Draft: draft-gong-srv6ops-srv6-oam-deployment · Working group: srv6ops
Agenda: draft-gong-srv6ops-srv6-oam-deployment
page: https://datatracker.ietf.org/doc/draft-gong-srv6ops-srv6-oam-deployment/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-33-srv6-oam-deployment-01-00 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
This document introduces common issues to consider when implementing SRv6 OAM, as well as various solutions.

### SR Policy Selector
Draft: draft-yang-srv6ops-policy-selector · Working group: srv6ops
Agenda: draft-yang-srv6ops-policy-selector
page: https://datatracker.ietf.org/doc/draft-yang-srv6ops-policy-selector/ | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
Segment routing (SR) [RFC8402] is a source routing paradigm that explicitly indicates the forwarding path for packets at the ingress node. An SR Policy is associated with one or more candidate paths, and each candidate path is either dynamic, explicit or composite. This document describes a policy selection mechanism among the candidate SR Policies based on network quality.

### Addressing Recommendations for SRv6
Draft: draft-horn-srv6ops-srv6addressing · Working group: srv6ops
Agenda: draft-horn-srv6ops-srv6addressing
page: https://datatracker.ietf.org/doc/draft-horn-srv6ops-srv6addressing/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-slides-124-srv6ops-draft-horn-srv6ops-srv6addressing-00 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
This document provides recommendations for addressing SRv6 locators format. It introduces concepts of Blocks, Sets, and Node IDs, and explains how summarization boundaries and flexible algorithm support can be implemented for both small and large networks.

### Introduction
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-1-introduction-01 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Move to the Host
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-verizon-ietf-srv6-on-hosts-00 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 as a Catalyst for Network Shift
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-22-srv6-as-a-catalyst-for-network-shift-01 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 policy selection
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-srv6ops-34-srv6-policy-selection-00 | video: https://youtu.be/RY76B-Vb4zc | materials: https://datatracker.ietf.org/meeting/124/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

## Working Group: tcpm

### More Accurate Explicit Congestion Notification (AccECN) Feedback in TCP
Draft: draft-ietf-tcpm-accurate-ecn · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-accurate-ecn-34
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-accurate-ecn/ | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
Explicit Congestion Notification (ECN) is a mechanism where network nodes can mark IP packets instead of dropping them to indicate incipient congestion to the endpoints. Receivers with an ECN-capable transport protocol feed back this information to the sender. ECN was originally specified for TCP in such a way that only one feedback signal can be transmitted per Round-Trip Time (RTT). Recent new TCP mechanisms like Congestion Exposure (ConEx), Data Center TCP (DCTCP) or Low Latency, Low Loss, and Scalable Throughput (L4S) need more Accurate ECN (AccECN) feedback information whenever more than one marking is received in one RTT. This document updates the original ECN specification in RFC 3168 to specify a scheme that provides more than one feedback signal per RTT in the TCP header. Given TCP header space is scarce, it allocates a reserved header bit previously assigned to the ECN-Nonce. It also overloads the two existing ECN flags in the TCP header. The resulting extra space is additionally exploited to feed back the IP-ECN field received during the TCP connection establishment. Supplementary feedback information can optionally be provided in two new TCP option alternatives, which are never used on the TCP SYN. The document also specifies the treatment of this updated TCP wire protocol by middleboxes.

### TCP RST Diagnostic Payload
Draft: draft-boucadair-tcpm-rst-diagnostic-payload · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-boucadair-tcpm-rst-diagnostic-payload-12
page: https://datatracker.ietf.org/doc/draft-boucadair-tcpm-rst-diagnostic-payload/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-ietf-124-draft-boucadair-tcpm-rst-diagnostic-payload-00 | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
This document specifies an experimental diagnostic payload format returned in TCP RST segments. Such payloads are used to share with an endpoint the reasons for which a TCP connection has been reset. Sharing this information is meant to ease diagnostic and troubleshooting. This specification builds on provisions that are already present in RFC 9293 "Transmission Control Protocol (TCP)". As such, this document does not require any change to RFC 9293.

### TCP ETS: Extensible Timestamp Options
Draft: draft-yang-tcpm-ets · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-yang-tcpm-ets-01
page: https://datatracker.ietf.org/doc/draft-yang-tcpm-ets/ | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
This document presents ETS: an Extensible TimeStamps option for TCP. It allows hosts to use microseconds as the unit for timestamps to improve the precision of timestamps, and extends the information provided in the [RFC7323] TCP Timestamps Option by including the receiver delay in the TSecr echoing, so that the receiver of the ACK is able to more accurately estimate the portion of the RTT that resulted from time traveling through the network. The ETS option format is extensible, so that future extensions can add further information without the overhead of extra TCP option kind and length fields.

### An Upgraded TCP Session Type
Draft: draft-bonica-tcpm-extended-options · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-bonica-tcpm-extended-options-02
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/ | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
Currently, TCP maintains ordinary sessions (SES-O) in which ordinary segments (SEG-O) are exchanged. Each SEG-O can accommodate up to 40 octets of options. In the future, applications may require more than 40 octets of options. For example, an application may use a 36-byte TCP Authentication Option (TCP-AO), leaving insufficient space for other required options. Therefore, this document describes an experiment in which upgraded sessions (SES-U) and upgraded segments (SEG-U) are introduced. Each SEG-U can accommodate up to 1,016 octets of Individual Options.

### SCONE TCP Option
Draft: draft-eddy-tcpm-scone · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-eddy-tcpm-scone-00
page: https://datatracker.ietf.org/doc/draft-eddy-tcpm-scone/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-scone-for-tcp-00 | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
This document describes a TCP option that permits network elements to provide TCP endpoints advice on rate limits within the network. The functionality for TCP is analogous to SCONE packets within the QUIC protocol.

### AccECN
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-accecn-00 | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### AccECNSec
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-accecnsec-00 | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### tcp-ets
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-tcp-ets-00 | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### ext-options
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-ext-options-00 | video: https://youtu.be/Z1qVCrIBVqQ | materials: https://datatracker.ietf.org/meeting/124/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

## Working Group: tls

### A well-known URI for publishing service parameters
Draft: draft-ietf-tls-wkech · Working group: tls
Agenda: draft-ietf-tls-wkech
page: https://datatracker.ietf.org/doc/draft-ietf-tls-wkech/ | materials: https://datatracker.ietf.org/meeting/124/session/tls
We define a well-known URI at which an HTTP origin can inform an authoritative DNS server, or other interested parties, about its Service Bindings. Service binding data can include Encrypted ClientHello (ECH) configurations, that may change frequently. This allows the HTTP origin, in collaboration with DNS infrastructure elements, to publish and rotate its own ECH keys. Other service binding data such as information about TLS supported groups is unlikely to change quickly, but the HTTP origin is much more likely to have accurate information when changes do occur. Service data published via this mechanism is typically available via an HTTPS or SVCB resource record.

### Extended Key Update for Transport Layer Security (TLS) 1.3
Draft: draft-ietf-tls-extended-key-update · Working group: tls
Agenda: draft-ietf-tls-extended-key-update
page: https://datatracker.ietf.org/doc/draft-ietf-tls-extended-key-update/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-draft-ietf-tls-extended-key-update-06-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
TLS 1.3 ensures forward secrecy by performing an ephemeral Diffie- Hellman key exchange during the initial handshake, protecting past communications even if a party's long-term keys (typically a private key with a corresponding certificate) are later compromised. While the built-in KeyUpdate mechanism allows application traffic keys to be refreshed during a session, it does not incorporate fresh entropy from a new key exchange and therefore does not provide post- compromise security. This limitation can pose a security risk in long-lived sessions, such as those found in industrial IoT or telecommunications environments. To address this, this specification defines an extended key update mechanism that performs a fresh execution of the key exchange negotiated during the initial handshake within an active session, thereby ensuring post-compromise security. By forcing attackers to exfiltrate new key material repeatedly, this approach mitigates the risks associated with static key compromise. Regular renewal of session keys helps contain the impact of such compromises. The extension is applicable to both TLS 1.3 and DTLS 1.3.

### Large Record Sizes for TLS and DTLS with Reduced Overhead
Draft: draft-ietf-tls-super-jumbo-record-limit · Working group: tls
Agenda: draft-ietf-tls-super-jumbo-record-limit
page: https://datatracker.ietf.org/doc/draft-ietf-tls-super-jumbo-record-limit/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-large-record-sizes-for-tls-and-dtls-with-reduced-overhead-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
TLS 1.3 records limit the inner plaintext (TLSInnerPlaintext) size to 2^14 + 1 bytes, which includes one byte for the content type. DTLS 1.3 uses the same plaintext size limit. This document defines a TLS extension that allows endpoints to advertise larger per-direction maximum inner plaintext sizes, up to 2^30 - 256 bytes, while reducing overhead in TLS 1.3 and DTLS 1.3 record headers.

### ML-KEM Post-Quantum Key Agreement for TLS 1.3
Draft: draft-ietf-tls-mlkem · Working group: tls
Agenda: draft-ietf-tls-mlkem
page: https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-ml-kem-post-quantum-key-agreement-for-tls-13-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as NamedGroups and registers IANA values in the TLS Supported Groups registry for use in TLS 1.3 to achieve post-quantum (PQ) key establishment.

### A Password Authenticated Key Exchange Extension for TLS 1.3
Draft: draft-ietf-tls-pake · Working group: tls
Agenda: draft-ietf-tls-pake
page: https://datatracker.ietf.org/doc/draft-ietf-tls-pake/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-draft-ietf-tls-pake-01 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
The pre-shared key mechanism available in TLS 1.3 is not suitable for usage with low-entropy keys, such as passwords entered by users. This document describes an extension that enables the use of password-authenticated key exchange protocols with TLS 1.3.

### The Datagram Transport Layer Security (DTLS) Protocol Version 1.3
Draft: draft-ietf-tls-rfc9147bis · Working group: tls
Agenda: draft-ietf-tls-rfc9147bis
page: https://datatracker.ietf.org/doc/draft-ietf-tls-rfc9147bis/ | materials: https://datatracker.ietf.org/meeting/124/session/tls
This document specifies version 1.3 of the Datagram Transport Layer Security (DTLS) protocol. DTLS 1.3 allows client/server applications to communicate over the Internet in a way that is designed to prevent eavesdropping, tampering, and message forgery. The DTLS 1.3 protocol is based on the Transport Layer Security (TLS) 1.3 protocol and provides equivalent security guarantees with the exception of order protection / non-replayability. Datagram semantics of the underlying transport are preserved by the DTLS protocol. This document obsoletes RFC 6347.

### PEM file format for ECH
Draft: draft-farrell-tls-pemesni · Working group: tls
Agenda: draft-farrell-tls-pemesni
page: https://datatracker.ietf.org/doc/draft-farrell-tls-pemesni/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-pem-file-format-for-ech-01 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
Encrypted ClientHello (ECH) key pairs need to be configured into TLS servers, which can be built using different TLS libraries. This document specifies a file format to use, similar to how RFC 7468 defines other PEM file formats.

### Authenticated ECH Config Distribution and Rotation
Draft: draft-sullivan-tls-signed-ech-updates · Working group: tls
Agenda: draft-sullivan-tls-signed-ech-updates
page: https://datatracker.ietf.org/doc/draft-sullivan-tls-signed-ech-updates/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-draft-sullivan-tls-signed-ech-updates-00-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
Encrypted ClientHello (ECH) requires clients to have the server's ECH configuration before connecting. Currently, when ECH fails, servers can send updated configurations but clients cannot authenticate them unless the server has a valid certificate for the public name, limiting deployment flexibility. This document specifies a new mechanism for authenticating ECH configurations. Servers include additional information in their initial ECH configurations, which enables clients to authenticate updated configurations without relying on a valid certificate for the public name.

### Service Affinity Solution based on Transport Layer Security (TLS)
Draft: draft-wang-tls-service-affinity · Working group: tls
Agenda: draft-wang-tls-service-affinity
page: https://datatracker.ietf.org/doc/draft-wang-tls-service-affinity/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-service-affinity-solution-based-on-transport-layer-security-tls-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
This draft proposes a service affinity solution between client and server based on Transport Layer Security (TLS). It defines a minimal extension to TLS 1.3 by which a server instance can authorize a client to resume an established session on a different instance of the same service (for example, another node of a load-balanced cluster) and request, in band, that the client do so. The relocation authorization is carried inside the server's own session ticket, so it inherits the security properties of TLS 1.3 ticket-based resumption. The relocation target is an opaque value that either directly carries the switchover address (for example, an IP address and port) or is an identifier resolved by the application or control plane. This document also introduces a Reliable Framing Layer that operates above the TLS record layer to provide message framing, sequence numbering, acknowledgment tracking, and automatic retransmission. The Framing Layer ensures zero application data loss during TLS session migration by buffering unacknowledged data frames and retransmitting them to the new server endpoint after migration completes.

### WKECH
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-wkech-01 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### TLS Registries Update
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-tls-registries-update-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### -rfc9147bis (aka DTLS)
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tls-rfc9147bis-aka-dtls-00 | video: https://youtu.be/zTAuEx9Otys | materials: https://datatracker.ietf.org/meeting/124/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

## Working Group: tsvwg

### Proposal for Updates to Guidance on Packet Reordering
Draft: draft-white-intarea-reordering · Working group: tsvwg
Agenda: 1515-1520 intarea reordering draft (Greg) draft-white-intarea-reordering-02
page: https://datatracker.ietf.org/doc/draft-white-intarea-reordering/ | video: https://youtu.be/5zx9U6mxbFQ | materials: https://datatracker.ietf.org/meeting/124/session/tsvwg
Several link technology standards mandate that equipment guarantee in-order delivery of layer 2 frames, apparently due to a belief that this is required by higher layer protocols. To meet this requirement they implement a "resequencing" operation to restore the original packet order. This can introduce delays that result in net degradation of performance. Modern TCP and QUIC implementations support features that significantly improve their tolerance to out- of-order delivery. This draft is intended to provide new information for layer 2 technology standards regarding the need to assure in- order delivery to support IETF protocols.

### Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm
Draft: draft-tahiliani-tsvwg-fq-pie · Working group: tsvwg
Agenda: 1520-1540 FQ-PIE (Mohit) draft-tahiliani-tsvwg-fq-pie-02
page: https://datatracker.ietf.org/doc/draft-tahiliani-tsvwg-fq-pie/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tsvwg-fq-pie-00 | video: https://youtu.be/5zx9U6mxbFQ | materials: https://datatracker.ietf.org/meeting/124/session/tsvwg
This document presents Flow Queue Proportional Integral controller Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue Management (AQM) algorithm to isolate flows and tackle the problem of bufferbloat. FQ-PIE uses hashing to classify incoming packets into different queues and provide flow isolation. Packets are dequeued by using a variant of the round robin scheduler. Each such flow is managed by the PIE algorithm to maintain high link utilization while controlling the queue delay to a target value.

### Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-ietf-tsvwg-sctp-dtls-chunk · Working group: tsvwg
Agenda: 1540-1600 DTLS Chunk (Michael/Magnus) draft-ietf-tsvwg-sctp-dtls-chunk-01
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/ | slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tsvwg-dtls-chunk-00 | video: https://youtu.be/5zx9U6mxbFQ | materials: https://datatracker.ietf.org/meeting/124/session/tsvwg
This document describes a method for adding Datagram Transport Layer Security (DTLS) based authentication and cryptographic protection to the Stream Control Transmission Protocol (SCTP). This SCTP extension is intended to enable communication privacy for applications that use SCTP as their transport protocol and allows applications to communicate in a way that is designed to prevent eavesdropping and detect tampering or message forgery. Once enabled, this also applies to the SCTP payload as well as the SCTP control information. Applications using this SCTP extension can use most of the transport features provided by SCTP and its other extensions. The use of the SCTP Authentication extension defined in RFC 4895 is incompatible with the extension defined in this document but would not provide any additional service. This implies that the Dynamic Address Reconfiguration as specified in RFC 5061 can only be used as described in this document. This document obsoletes RFC 6083 and updates RFC 5061.

### L4S Interops
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tsvwg-l4s-interops-00 | video: https://youtu.be/5zx9U6mxbFQ | materials: https://datatracker.ietf.org/meeting/124/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### Intarea Reordering Draft
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tsvwg-intarea-reordering-draft-00 | video: https://youtu.be/5zx9U6mxbFQ | materials: https://datatracker.ietf.org/meeting/124/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### Koen L4S Update
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-tsvwg-koen-l4s-update-00 | video: https://youtu.be/5zx9U6mxbFQ | materials: https://datatracker.ietf.org/meeting/124/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

## Working Group: v6ops

### Tim Winters - Basic Requirements for IPv6 Customer Edge Routers - 7084bis
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-tim-winters-basic-requirements-for-ipv6-customer-edge-routers-7084bis-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jen Linkova - IPv6-Mostly Networks Deployment and Operations Considerations - 02
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-jen-linkova-ipv6-mostly-networks-deployment-and-operations-considerations-02-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Fan Zhang - YANG Data Model for IPv6 Neighbor Discovery
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-fan-zhang-yang-data-model-for-ipv6-neighbor-discovery-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jordi Palet - RFC6146-bis and others
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-jordi-palet-rfc6146-bis-and-others-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Philipp S. Tiesel - draft-tiesel-v6ops-ipv6-app-testing
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-philipp-s-tiesel-draft-tiesel-v6ops-ipv6-app-testing-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jordi Palet - draft-palet-v6ops-prefix-assignment-00
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-jordi-palet-draft-palet-v6ops-prefix-assignment-00-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Chenhao Ma-Considerations of Gradual IPv6-only Deployment in 5G Mobile Networks
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-chenhao-ma-considerations-of-gradual-ipv6-only-deployment-in-5g-mobile-networks-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jing Zhao-IPv6 Network Deployment Monitoring and Analysis
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-jing-zhao-ipv6-network-deployment-monitoring-and-analysis-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jen Linkova - NAT64 and the WKP
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-v6ops-jen-linkova-nat64-and-the-wkp-00 | video: https://youtu.be/hUJLeQxfZl4 | materials: https://datatracker.ietf.org/meeting/124/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

## Working Group: wimse

### WIMSE Workload Credentials
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-workload-credentials-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Workload Proof Token
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-workload-proof-token-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Authentication with HTTP Signatures
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-authentication-with-http-signatures-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload Authentication Using Mutual TLS
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-workload-authentication-using-mutual-tls-01 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Architecture
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-architecture-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload Identifier
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-workload-identifier-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload Identity Practices WGLC
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-workload-identity-practices-wglc-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Applicability for AI Agents
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-applicability-for-ai-agents-02 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Delegated Authorization
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-delegated-authorization-00 | video: https://youtu.be/0UaVPLO_9Xk | materials: https://datatracker.ietf.org/meeting/124/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

