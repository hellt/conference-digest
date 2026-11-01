>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-125. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-125.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-125.md
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

Below is the program for IETF 125 (Shenzhen) (standards). Read it and produce a digest
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
conference: IETF 125 (Shenzhen)
type: standards
source_url: https://datatracker.ietf.org/meeting/125/agenda.json
generated: 2026-11-01
registry_key: ietf-125
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Working Group: 6man

### YANG Data Model for IPv6 Neighbor Discovery
Draft: draft-ietf-6man-ipv6-neighbor-discovery-yang · Working group: 6man
Agenda: draft-ietf-6man-ipv6-neighbor-discovery-yang
page: https://datatracker.ietf.org/doc/draft-ietf-6man-ipv6-neighbor-discovery-yang/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-yang-data-model-for-ipv6-neighbor-discovery-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document defines a YANG data model to configure and manage IPv6 Neighbor Discovery (ND) and related functions, including IPv6 address resolution, redirect function, proxy Neighbor Advertisement, Neighbor Unreachability Detection (NUD), Duplicate Address Detection (DAD), and Enhanced Duplicate Address Detection.

### IPv6 Query for Enabled In-situ OAM Capabilities
Draft: draft-ietf-6man-icmpv6-ioam-conf-state · Working group: 6man
Agenda: draft-ietf-6man-icmpv6-ioam-conf-state
page: https://datatracker.ietf.org/doc/draft-ietf-6man-icmpv6-ioam-conf-state/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-ipv6-query-for-enabled-in-situ-oam-capabilities-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document describes the application of the mechanism of discovering In-situ OAM (IOAM) capabilities, described in RFC 9359 "Echo Request/Reply for Enabled In Situ OAM (IOAM) Capabilities", in IPv6 networks. IPv6 Node IOAM Query functionality uses the ICMPv6 Query messages, allowing the IOAM encapsulating node to discover the enabled IOAM capabilities of each IOAM transit and IOAM decapsulating node.

### Carrying Network Resource (NR) related Information in IPv6 Extension Headers
Draft: draft-ietf-6man-enhanced-vpn-vtn-id · Working group: 6man
Agenda: draft-ietf-6man-enhanced-vpn-vtn-id
page: https://datatracker.ietf.org/doc/draft-ietf-6man-enhanced-vpn-vtn-id/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-carrying-network-resource-nr-related-information-in-ipv6-extension-header-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
Virtual Private Networks (VPNs) provide different customers with logically separated connectivity over a common network infrastructure. With the introduction of 5G and also in some existing network scenarios, some customers may require network connectivity services with features that are more advanced compared to conventional VPN services. Such kind of network service is called enhanced VPNs. Enhanced VPNs can be used, for example, to deliver network slice services. A Network Resource Partition (NRP) is a subset of the network resources and associated policies on each of a connected set of links in the underlay network. An NRP may be used as the underlay to support one or a group of enhanced VPN services. For packet forwarding within a specific NRP, some fields in the data packet (these fields are called the NRP Selector) are used to identify the NRP to which the packet belongs. By identifying a packet with an NRP, NRP-specific processing can be performed on each node along the forwarding path in the NRP. This document specifies a new IPv6 Hop-by-Hop option to carry Network Resource related information in data packets. The new option is called the Network Resource (NR) Option. It can be used to carry an identifier of the NRP Selector, but it is designed to also be able to carry general information about network resource semantics and functions.

### IPv6 Node Requirements
Draft: draft-ietf-6man-rfc8504-bis · Working group: 6man
Agenda: draft-ietf-6man-rfc8504-bis
page: https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-ipv6-node-requirements-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document defines requirements for IPv6 nodes. It is expected that IPv6 will be deployed in a wide range of devices and situations. Specifying the requirements for IPv6 nodes allows IPv6 to function well and interoperate in a large number of situations and deployments. This document obsoletes RFC 8504, and in turn RFC 6434 and its predecessor, RFC 4294.

### The IPv6 Loopback Address Prefix
Draft: draft-kumari-ipv6-loopback · Working group: 6man
Agenda: draft-kumari-ipv6-loopback
page: https://datatracker.ietf.org/doc/draft-kumari-ipv6-loopback/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-the-ipv6-loopback-address-prefix-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
{ *Editor's note:* This document requests the allocation of a new IPv6 address prefix to be used for loopback instead of expanding into the existing ::/96. The specific prefix to be allocated is TBD/96, and the document updates the relevant RFCs and IANA registries to reflect this change. } This document updates the IP Version 6 Address Architecture to expand the size of the IPv6 loopback space from a single address to a /96 prefix. This change allows for a much larger number of loopback addresses in IPv6, which can be used for inter-process communication within a host and for network diagnostics. The document also updates the IANA IPv6 Address registry and the IPv6 Special Purpose Address registry to reflect this change. It updates RFC4291 to reflect the new loopback prefix and its functional semantics.

### Deprecating IPv6 Extension Headers on the Internet
Draft: draft-herbert-deprecate-eh · Working group: 6man
Agenda: draft-herbert-deprecate-eh/
page: https://datatracker.ietf.org/doc/draft-herbert-deprecate-eh/ | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document describes the deprecation of IPv6 extension headers on the Internet with the exception of Encapsulating Security Payload. Deprecation is motivated by three factors: 1) the data shows high discard rates for packets with extension headers sent over the Internet, 2) extension headers can be used for Denial of Service attack and are replete with other security vulnerabilities, 3) the high loss rates are a disincentive to develop new extension headers or options that might be useful or fix known problems. This document recommends that extension headers, other than Encapsulating Security Payload, be relegated to use only in limited domains and that packets with extension headers should be discarded at boundary routers of limited domains.

### Deprecate IPv6 Destination Options Before the Routing Header
Draft: draft-herbert-deprecate-destops-before-rh · Working group: 6man
Agenda: draft-herbert-deprecate-destops-before-rh
page: https://datatracker.ietf.org/doc/draft-herbert-deprecate-destops-before-rh/ | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document deprecates IPv6 Destination Options before the Routing header since there are no known deployments or uses for the Destination Options Header placed ahead in precedence of the Routing Header. It also requires that if a Routing header is present in a packet then it must immediately follow the IPv6 header or immediately follow the Hop-by-Hop Options header if an Hop-by-Hop Options header is also present in the packet. These requirements imply that at most one Routing header may be present in a packet.

### Infight Removal of IPv6 Hop-by-Hop and Routing Headers
Draft: draft-herbert-eh-inflight-removal · Working group: 6man
Agenda: draft-herbert-eh-inflight-removal
page: https://datatracker.ietf.org/doc/draft-herbert-eh-inflight-removal/ | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document specifies a method to allow intermediate nodes to remove IPv6 Hop-by-Hop Options headers and Routing headers from packets inflight. The goal is to reduce the probability of packets being dropped because they contain these extension headers without impacting functionality. An additional goal is to limit visibility of information in extension headers to those nodes that need to process the headers.

### Updates to DNS64 Functionality Advertisement for DNS RA Option
Draft: draft-ma-6man-ra-dns64-flag · Working group: 6man
Agenda: draft-ma-6man-ra-dns64-flag-01
page: https://datatracker.ietf.org/doc/draft-ma-6man-ra-dns64-flag/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-updates-to-dns64-functionality-advertisement-for-dns-ra-option-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document defines a new flag in the DNS RA Option to advertise the DNS64 functionality. This extension enables automatic configuration of DNS64 resolution, improving deployability in IPv6 transition scenarios.

### ICMP Error Handling for VPNs in SRv6 Networks
Draft: draft-varhal-6man-icmp-srv6-vpn · Working group: 6man
Agenda: draft-varhal-6man-icmp-srv6-vpn
page: https://datatracker.ietf.org/doc/draft-varhal-6man-icmp-srv6-vpn/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-icmp-error-handling-for-vpns-in-srv6-networks-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
This document specifies ICMP error handling in SRv6-based Virtual Private Networks, that support direct localization of failures. It provides a solution for connectivity check and fault localization without adding complexity to P nodes and keeps P nodes service agnostic. ICMP processing is changed only on ingress PE nodes and gains from adding VPN-specific information to the SRv6 encapsulated packet. Egress PE nodes are not involved in the forwarding of the ICMP error messages therefore, the solution provides visibility upto the failure even if ingress PE to egress PE connectivity is broken within the SR domain.

### Addressing Extension Header Vulnerabilities
Presentation · Working group: 6man
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-6man-addressing-extension-header-vulnerabilities-00 | video: https://youtu.be/A1QUaZ9HG9o | materials: https://datatracker.ietf.org/meeting/125/session/6man
Slides presented at the 6man session; no Internet-Draft is linked to them.

## Working Group: acme

### Automated Certificate Management Environment (ACME) Delay-Tolerant Networking (DTN) Node ID Validation Extension
Draft: draft-ietf-acme-dtnnodeid · Working group: acme
Agenda: RFC 9891 ( draft-ietf-acme-dtnnodeid ) 🎉
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dtnnodeid/ | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
This document specifies an extension to the Automated Certificate Management Environment (ACME) protocol which allows an ACME server to validate the Delay-Tolerant Networking (DTN) Node ID for an ACME client. A DTN Node ID is an identifier used in the Bundle Protocol (BP) to name a "singleton endpoint", one which is registered on a single BP node. The DTN Node ID is encoded as a certificate Subject Alternative Name (SAN) of type otherName with a name form of BundleEID and as an ACME Identifier type "bundleEID".

### ACME Integrations for Device Certificate Enrollment
Draft: draft-ietf-acme-integrations · Working group: acme
Agenda: draft-ietf-acme-integrations -- in MISREF
page: https://datatracker.ietf.org/doc/draft-ietf-acme-integrations/ | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
This document outlines multiple advanced use cases and integrations that ACME facilitates without any modifications or enhancements required to the base ACME specification. The use cases include ACME integration with EST, BRSKI and TEAP.

### Automated Certificate Management Environment (ACME) Device Attestation Extension
Draft: draft-acme-device-attest · Working group: acme
Agenda: draft-acme-device-attest -- past WGLC, but requires structural changes to add JSON for the two new Identifier types
page: https://datatracker.ietf.org/doc/draft-acme-device-attest/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-acme-acme-device-attestation-02 | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
This document specifies new identifiers and a challenge for the Automated Certificate Management Environment (ACME) protocol which allows validating the identity of a device using attestation.

### Automated Certificate Management Environment (ACME) Profiles Extension
Draft: draft-ietf-acme-profiles · Working group: acme
Agenda: draft-ietf-acme-profiles-01 – Aaron
page: https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-acme-automated-certificate-management-environment-acme-remote-attestation-identifier-and-challenge-type-00 | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
This document defines how an ACME Server may offer a selection of different certificate profiles to ACME Clients, and how those clients may indicate which profile they want.

### Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type
Draft: draft-ietf-acme-rats · Working group: acme
Agenda: draft-ietf-acme-rats-01 – Peter
page: https://datatracker.ietf.org/doc/draft-ietf-acme-rats/ | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
This document describes an approach where an ACME Server can challenge an ACME Client to provide Evidence, Endorsements, or Attestation Result according to the Remote ATtestation procedureS (RATS) framework in any format supported by the Conceptual Message Wrapper (CMW). The ACME Server can optionally challenge the Client for specific claims that it wishes attestation for.

### Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation
Draft: draft-ietf-acme-dns-persist · Working group: acme
Agenda: draft-ietf-acme-dns-persist – Shiloh
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dns-persist/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-acme-draft-ietf-acme-dns-persist-00 | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
This document specifies "dns-persist-01", a new validation method for the Automated Certificate Management Environment (ACME) protocol. This method allows a Certification Authority (CA) to verify control over a domain by confirming the presence of a persistent DNS TXT record containing CA and account identification information. This method is particularly suited for environments where traditional challenge methods are impractical, such as multi-tenant hosting platforms, enterprise DNS environments, and IoT deployments. The validation method is designed with a strong focus on security and robustness, incorporating widely adopted industry best practices for persistent domain control validation. This design aims to make it suitable for Certification Authorities operating under various policy environments, including those that align with the CA/Browser Forum Baseline Requirements.

### Automated Certificate Management Environment (ACME) Extension for Public Key Challenges
Draft: draft-geng-acme-public-key · Working group: acme
Agenda: draft-geng-acme-public-key-04 – Grace
page: https://datatracker.ietf.org/doc/draft-geng-acme-public-key/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-acme-acme-extension-for-public-key-challenges-slides-00 | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
The Automatic Certificate Management Environment (ACME) [RFC8555] requires a PKCS#10 Certificate Signing Request (CSR) at the finalization stage. This document defines a new ACME challenge type, "pk-01", that allows a client to prove possession of a private key directly, without constructing a CSR. The primary motivation is to support key types that cannot generate CSR self-signatures, notably post-quantum Key Encapsulation Mechanism (KEM) keys. The client declares the public key via a popKey field in the "newOrder" request; the server attaches the "pk-01" challenge to existing identifier authorizations. When all required authorizations are satisfied, the ACME server issues a certificate using the validated public key and the authorized identifiers, eliminating the need for a CSR in the finalization stage.

### ACME Profiles update for IETF 125
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-acme-acme-profiles-update-for-ietf-125-00 | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### emrtd-data-01
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-acme-emrtd-data-01-00 | video: https://youtu.be/PGZwaFRimuM | materials: https://datatracker.ietf.org/meeting/125/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

## Working Group: anima

### Constrained BRSKI and Join Proxy IETF 125
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-constrained-brski-and-join-proxy-ietf-125-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### MASA/Registrar Operational Document, overview and merge ideas
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-masaregistrar-operational-document-overview-and-merge-ideas-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### BRSKI Discovery
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-brski-discovery-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Constrained GRASP
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-constrained-grasp-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### An Intent-based Framework of Network Services Autonomic Deployment and Management
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-an-intent-based-framework-of-network-services-autonomic-deployment-and-management-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### The Autonomic Deployment Mechanism of Service Intent in Autonomic Networks
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-the-autonomic-deployment-mechanism-of-service-intent-in-autonomic-networks-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Definition of Service Intent in Autonomic Networks
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-definition-of-service-intent-in-autonomic-networks-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Considerations of AI-powered ASA Communication and Scenarios
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-considerations-of-ai-powered-asa-communication-and-scenarios-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### GRASP Objective for CATS Metrics Distribution
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-grasp-objective-for-cats-metrics-distribution-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Autonomous Bootstrap and Service Configuration in Enterprise Networks
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-anima-autonomous-bootstrap-and-service-configuration-in-enterprise-networks-00 | video: https://youtu.be/anZ90j2HzTY | materials: https://datatracker.ietf.org/meeting/125/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

## Working Group: bess

### Applications and Procedures for the Unknown MAC Route in EVPN
Draft: draft-ietf-bess-evpn-umr-mobility · Working group: bess
Agenda: draft-ietf-bess-evpn-umr-mobility-03 Krishna 05 min 9:15 - 9:20
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-umr-mobility/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-draft-ietf-bess-evpn-umr-mobility-03-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
The Interconnect Solution for Ethernet VPN defines Unknown MAC (Media Access Control) Route (UMR) utilization for Data Center Interconnect (DCI) when EVPN MPLS or EVPN VXLAN is used as an overlay network for such interconnects. The use of UMR has implications for EVPN MAC mobility procedures, for EVPN Layer 2 and IRB operations, and for EVPN Proxy ARP/ND operations. This document describes additional enhancements required to EVPN procedures and operations when using UMR. This document updates RFC9014 to clarify and extend the procedures for UMR usage.

### EVPN Interoperability Modes
Draft: draft-ietf-bess-evpn-modes-interop · Working group: bess
Agenda: draft-ietf-bess-evpn-modes-interop-03 Krishna 05 min 9:20 - 9:25
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-modes-interop/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-draft-ietf-bess-evpn-modes-interop-03-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
Ethernet VPN (EVPN) provides different functional modes in the area of Service Interface, Integrated Route and Bridge (IRB) and IRB Core connectivity. This document specifies how the different EVPN functional modes and types can interoperate with each other. This document does not redefine the existing functional modes but describes how these modes interoperate.

### EVPN L3-Optimized IRB
Draft: draft-sajassi-bess-evpn-l3-optimized-irb · Working group: bess
Agenda: draft-sajassi-bess-evpn-l3-optimized-irb-04 Krishna 05 min 9:25 - 9:30
page: https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-l3-optimized-irb/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-draft-sajassi-bess-evpn-l3-optimized-irb-04-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
Ethernet VPN Integrated Routing and Bridging (EVPN-IRB) provides dynamic and efficient intra and inter-subnet connectivity among Tenant Systems and end devices while maintaining very flexible multihoming capabilities. This document describes how EVPN-IRB can be optimized for IP hosts and devices such that PE devices only maintain MAC addresses for locally-connected IP hosts, thus improving MAC scalability of customer bridges and PE devices significantly. This document describes how such optimization is acheived while still supporting host moblity which is one of the fundamental features in EVPN and EVPN-IRB. With such optimization PE devices perform routing for both intra and inter-subnet traffic which results in some some caveats that operators and service providers need to be fully aware of.

### Domain Path (D-PATH) for Ethernet VPN (EVPN) Interconnect Networks
Draft: draft-ietf-bess-evpn-dpath · Working group: bess
Agenda: draft-ietf-bess-evpn-dpath-04 Jorge 05 min 9:30 - 9:35
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-dpath/ | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
The BGP Domain PATH (D-PATH) attribute is defined for Inter-Subnet Forwarding (ISF) BGP Sub-Address Families that advertise IP prefixes or MAC addresses. D-PATH already applies to EVPN Route Type 2 when used for ISF, to EVPN Route Type 5 (IP Prefix routes), and to IP-VPN routes. When used along with those routes, it identifies the domain(s) through which the routes have passed and that information can be used by the receiver BGP speakers to detect routing loops or influence the BGP best path selection. This document extends the use of D-PATH to EVPN Route Type 2 when not used for ISF, to EVPN Route Type 1 (Ethernet Auto-Discovery per-EVI) for EVPN VPWS, and to EVPN Route Type 3 (Inclusive Multicast Ethernet Tag routes).

### EVPN Inter-Domain Option-B Solution
Draft: draft-rabadan-bess-evpn-inter-domain-opt-b · Working group: bess
Agenda: draft-rabadan-bess-evpn-inter-domain-opt-b-08. Jorge 05 min 9:35 - 9:40
page: https://datatracker.ietf.org/doc/draft-rabadan-bess-evpn-inter-domain-opt-b/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-evpn-inter-domain-opt-b-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
An EVPN Inter-Domain interconnect solution is required when two or more sites of the same Ethernet Virtual Private Network (EVPN) are connected to different IGP domains or Autonomous Systems (AS) and need to communicate. The Inter-Domain Option-B connectivity model is one of the most popular solutions for this type of EVPN connectivity. While several documents address specific aspects of this interconnect approach, none provide a comprehensive overview of how Inter-Domain Option-B connectivity affects EVPN procedures. This document examines the behavior of EVPN procedures in an Inter-Domain Option-B network and proposes solutions to the identified issues.

### EVPN Anycast Multi-Homing
Draft: draft-rabnag-bess-evpn-anycast-aliasing · Working group: bess
Agenda: draft-rabnag-bess-evpn-anycast-aliasing-05 Jorge 10 min 9:40 - 9:50
page: https://datatracker.ietf.org/doc/draft-rabnag-bess-evpn-anycast-aliasing/ | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
The current Ethernet Virtual Private Network (EVPN) all-active multi- homing procedures in Network Virtualization Over Layer-3 (NVO3) networks provide the required Split Horizon filtering, Designated Forwarder Election and Aliasing functions that the network needs in order to handle the traffic to and from the multi-homed CE in an efficient way. In particular, the Aliasing function supports load balancing of unicast traffic from remote Network Virtualization Edge (NVE) devices to NVEs that are multi-homed to the same CE, regardless of whether the CE’s MAC/IP information has been learned on all those NVEs. This document introduces an optional enhancement to the EVPN multi-homing Aliasing function, referred to as EVPN Anycast Multi- homing. This optimization is specific to EVPN deployments over NVO3 tunnels (i.e., IP-based tunnels) and may offer benefits in typical data center designs, which are discussed herein.

### EVPN Fast Notification and Handling for Multihoming
Draft: draft-zzhang-bess-evpn-mh-fast-notification · Working group: bess
Agenda: draft-zzhang-bess-evpn-mh-fast-notification Jeffery 15 min 9:50 - 10:05
page: https://datatracker.ietf.org/doc/draft-zzhang-bess-evpn-mh-fast-notification/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-evpn-mh-fast-notification-01 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
EVPN supports powerful multihoming features, but it depends on the timely notification and handling of link going down or coming up on multihomed Ethernet Segments, which may not be guaranteed by the nature of control plane BGP signaling. When the handling is delayed, traffic duplication or loss may happen. This document specifies a UDP-based notification that can be originated and processed (near) instantly, greatly eliminate the potential traffic duplication or loss.

### Data Plane Failure Detection Mechanisms for EVPN over SRv6
Draft: draft-liu-bess-srv6-evpn-validation · Working group: bess
Agenda: draft-liu-bess-srv6-evpn-validation Yao Liu 10 min 10:05 - 10:15
page: https://datatracker.ietf.org/doc/draft-liu-bess-srv6-evpn-validation/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-draft-liu-bess-srv6-evpn-validation-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
For MPLS EVPN, RFC9489 specifies the mechanisms for detecting data plane failures using LSP Ping. This document proposes a similar mechanism to detect data plane failures for EVPN over SRv6.

### Export of BGP VPN Information in IPFIX
Draft: draft-liu-opsawg-ipfix-bgp-vpn · Working group: bess
Agenda: draft-liu-opsawg-ipfix-bgp-vpn Yso Liu 05 min 10:15 - 10:20
page: https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-bgp-vpn/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-draft-liu-opsawg-ipfix-bgp-vpn-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
This document introduces new IP Flow Information Export (IPFIX) information elements to carry information that can be used to identify the egress PE in BGP VPN scenarios.

### Signaling Alternative Labels for BGP Prefixes
Draft: draft-smm-bess-alt-label · Working group: bess
Agenda: draft-smm-bess-alt-label-00 Mankamana 10 min 10:20 - 10:30
page: https://datatracker.ietf.org/doc/draft-smm-bess-alt-label/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-draft-smm-bess-alt-label-00-01 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
A single MPLS label or a label stack is advertised along with an address prefix as part of the NLRI belonging to labeled address families such as Labeled Unicast (RFC 8277), VPN (RFC 4364), etc. This document specifies a method to advertise one or more additional, alternative labels for a set of address prefixes using the Next Hop Dependent Characteristics (NHC) attribute.

### EVPN D-PATH
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-evpn-d-path-00 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### EVPN Anycast MH
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-evpn-anycast-mh-02 | video: https://youtu.be/hr5963eGggU | materials: https://datatracker.ietf.org/meeting/125/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

## Working Group: cose

### Test Vectors for CBOR-Encoded X.509 (C509) Certificates
Draft: draft-ietf-cose-c509-test-vectors · Working group: cose
Agenda: [05 min] draft-ietf-cose-c509-test-vectors - G�ran Selander
page: https://datatracker.ietf.org/doc/draft-ietf-cose-c509-test-vectors/ | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
This document contains examples of CBOR-encoded X.509 (C509) certificates, certification requests, and certification request templates.

### FN-DSA for JOSE and COSE
Draft: draft-ietf-cose-falcon · Working group: cose
Agenda: [10 min] draft-ietf-cose-falcon and draft-ietf-cose-sphincs-plus - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-falcon/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-cose-draft-ietf-cose-falcon-and-draft-ietf-cose-sphincs-plus-00 | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
This document specifies JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 206 (expected to be published in late 2026 early 2027). It does not define new cryptographic primitives; rather, it specifies how existing FN-DSA mechanisms are serialized for use in JOSE and COSE. This document registers signature algorithms for JOSE and COSE, specifically FN-DSA-512 and FN-DSA-1024.

### SLH-DSA for JOSE and COSE
Draft: draft-ietf-cose-sphincs-plus · Working group: cose
Agenda: [10 min] draft-ietf-cose-falcon and draft-ietf-cose-sphincs-plus - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-sphincs-plus/ | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
Digital signatures are used within JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) to protect the integrity and authenticity of messages, such as JSON Web Signatures and signed COSE structures. This document specifies JOSE and COSE serializations for the Stateless Hash-Based Digital Signature Standard (SLH-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 205. The conventions for the associated algorithm identifiers, signatures, public keys, and private keys are also specified.

### Use of Hybrid Public-Key Encryption (HPKE) with CBOR Object Signing and Encryption (COSE)
Draft: draft-ietf-cose-hpke · Working group: cose
Agenda: [15 min] draft-ietf-cose-hpke - Mike Jones
page: https://datatracker.ietf.org/doc/draft-ietf-cose-hpke/ | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
This specification defines hybrid public-key encryption (HPKE) for use with CBOR Object Signing and Encryption (COSE). HPKE offers a variant of public-key encryption of arbitrary-sized plaintexts for a recipient public key. HPKE is a general encryption framework utilizing an asymmetric key encapsulation mechanism (KEM), a key derivation function (KDF), and an Authenticated Encryption with Associated Data (AEAD) algorithm. This document defines the use of HPKE with COSE. Authentication for HPKE in COSE is provided by COSE-native security mechanisms or by the pre-shared key authenticated variant of HPKE.

### Post-Quantum and Hybrid KEMs for HPKE with JOSE and COSE
Draft: draft-reddy-cose-jose-pqc-hybrid-hpke · Working group: cose
Agenda: [10 min] draft-reddy-cose-jose-pqc-hybrid-hpke - Tirumal Reddy
page: https://datatracker.ietf.org/doc/draft-reddy-cose-jose-pqc-hybrid-hpke/ | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
This document specifies the use of Post-Quantum (PQC) and Post- Quantum/Traditional (PQ/T) Hybrid Key Encapsulation Mechanisms (KEMs) within the Hybrid Public Key Encryption (HPKE) for JOSE and COSE. It defines algorithm identifiers and key formats to support pure post- quantum algorithms (ML-KEM) and their PQ/T hybrid combinations.

### Split Signing Algorithms for COSE
Draft: draft-lundberg-cose-two-party-signing-algs · Working group: cose
Agenda: [15 min] draft-lundberg-cose-two-party-signing-algs - Mike Jones
page: https://datatracker.ietf.org/doc/draft-lundberg-cose-two-party-signing-algs/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-cose-split-signing-algorithms-for-cose-00 | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
This specification defines COSE algorithm identifiers for negotiating how to split a signature algorithm between two cooperating parties. Typically the first party hashes the data to be signed and the second party finishes the signature over the hashed data. This is a common technique, useful for example when the signing private key is held in a smart card or similar hardware component with limited processing power and communication bandwidth. The resulting signatures are identical in structure to those computed by a single party, and can be verified using the same verification algorithm without additional steps to preprocess the signed data.

### Composite Token Claims
Draft: draft-lemmons-cose-composite-claims · Working group: cose
Agenda: [10 min] draft-lemmons-cose-composite-claims - Chris Lemmons
page: https://datatracker.ietf.org/doc/draft-lemmons-cose-composite-claims/ | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
Composite claims are claims for CBOR Web Tokens (CWTs) and JSON Web Tokens (JWTs) that define logical relationships between sets of claims. This document also defines a CWT representation of the "crit" (Critical) claim.

### Ascon-AEAD128 and Ascon-Hash256 for COSE
Draft: draft-ochkas-cose-ascon · Working group: cose
Agenda: [10 min] draft-ochkas-cose-ascon - Alexander Pelov
page: https://datatracker.ietf.org/doc/draft-ochkas-cose-ascon/ | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
This document describes CBOR Object Signing and Encryption (COSE) serialization with Ascon, a NIST standard for lightweight cryptography. In 2019, as a part of CAESAR competition, Ascon-128 and Ascon-128a were selected as the first choice for the lightweight authenticated encryption. After, in 2023, National Institute of Standards and Technology (NIST) selected Ascon family of cryptographic algorithms to be the standard for lightweight cryptography. In August 2025, NIST Special Publication 800-232 was released, defining Ascon-based lightweight cryptography standards for constrained devices. This recognition makes it particularly interesting to enable using Ascon with COSE structures.

### AES-CMAC for COSE
Draft: draft-sipos-cose-cmac · Working group: cose
Agenda: [10 min] draft-sipos-cose-cmac - Brian Sipos
page: https://datatracker.ietf.org/doc/draft-sipos-cose-cmac/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-cose-aes-cmac-00 | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
The CBOR Object Signing and Encryption (COSE) specification defines structures for generating, conveying, and verifying Message Authentication Code (MAC) tags. This document registers code points for using the Advanced Encryption Standard (AES) block cipher in Cipher-based Message Authentication Code (CMAC) mode within those COSE structures. Specifically, these uses are for computing MAC tag values with no additional parameters.

### COSE HPKE
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-cose-cose-hpke-00 | video: https://youtu.be/yuVzfQMXtzE | materials: https://datatracker.ietf.org/meeting/125/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

## Working Group: dnsop

### Automating DNS Delegation Management via DDNS
Draft: draft-ietf-dnsop-delegation-mgmt-via-ddns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delegation-mgmt-via-ddns/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delegation-mgmt-via-ddns/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-delegation-mgmt-via-ddns-00 | video: https://youtu.be/w-Bc2LMkVQU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
Delegation information (i.e. the NS RRset, possible glue, possible DS records) should always be kept in sync between child zone and parent zone. However, in practice that is not always the case. When the delegation information is not in sync the child zone is usually working fine, but without the amount of redundancy that the zone owner likely expects to have. Hence, should any further problems ensue it could have catastrophic consequences. The DNS name space has lived with this problem for decades and it never goes away. Or, rather, it will never go away until a fully automated mechanism for how to keep the information in sync automatically is deployed. This document proposes such a mechanism based on DNS Dynamic Updates (DDNS) secured with SIG(0) signatures, sent from the child to the parent across the zone cut. The target of the update is discovered via the DSYNC record defined in [RFC9859]. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-ietf-dnsop-delegation-mgmt-via-ddns (https://github.com/johanix/draft-ietf-dnsop-delegation-mgmt-via- ddns). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Clarifications to the DNS Ranking Data
Draft: draft-fujiwara-dnsop-ranking-data · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-ranking-data/
page: https://datatracker.ietf.org/doc/draft-fujiwara-dnsop-ranking-data/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-clarifications-to-the-dns-ranking-data-00 | video: https://youtu.be/w-Bc2LMkVQU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
This document obsoletes Section 5.4.1 (Ranking data) of RFC 2181, and specifies directives whereby the source of the data determines for what purposes it may be used.

### Considerations for Protective DNS Server Operators
Draft: draft-liu-dnsop-protective-dns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-liu-dnsop-protective-dns/
page: https://datatracker.ietf.org/doc/draft-liu-dnsop-protective-dns/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-considerations-for-protective-dns-server-operators-00 | video: https://youtu.be/w-Bc2LMkVQU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
Protective DNS is a defense mechanism deployed on recursive resolvers to prevent users from accessing malicious domains. For domain names in the blocklist, it rewrites DNS resolution responses to point to secure destinations (e.g., safe servers) to prevent users from accessing malicious entities. Owing to its effective defenses against common cyber attack behaviors—such as command-and-control (C2) communications of malware—Protective DNS deployment has surged via various initiatives. Not only have renowned DNS service providers adopted this defense, but some countries have also launched national-scale deployments. Meanwhile, studies analyzing Protective DNS have identified implementation diversity. Thus, this document aims to provide specific operational and security considerations for Protective DNS. It is intended primarily for entities seeking to deploy Protective DNS for defensive purposes, offering deployment and security considerations.

### Avoid Large Records with a Wildcard Owner Name
Draft: draft-avoid-large-wildcard-records · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-avoid-large-wildcard-records/
page: https://datatracker.ietf.org/doc/draft-avoid-large-wildcard-records/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-sessb-avoid-large-wildcard-records-00 | video: https://youtu.be/w-Bc2LMkVQU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
As DNS hosting becomes increasingly centralized, with multiple zones hosted on shared authoritative name servers, the risk of DNS amplification attacks has grown. By crafting large DNS records with wildcard owner names, attackers can exploit these shared servers to launch high-volume DDoS amplification attacks. This document provides operational guidance for DNS hosting providers to mitigate DDoS risks arising from amplification of responses derived from wildcard owner names.

### RootCache: Filling Resolver Caches with Root Zone Records
Draft: draft-hoffman-rootcache · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-hoffman-rootcache/
page: https://datatracker.ietf.org/doc/draft-hoffman-rootcache/ | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
Some DNS recursive resolver operators want to prevent snooping by third parties of requests sent to DNS root servers. Resolvers can reduce the number of queries sent to root server, and thus prevent observation of requests, by caching a copy of the full root zone. This document shows how a resolver can securely receive the full root zone and put it into the resolver's cache. This document obsoletes RFC 8806.

### Populating resolvers with the root zone
Draft: draft-wkumari-dnsop-localroot-bcp · Working group: dnsop
Agenda: draft-wkumari-dnsop-localroot-bcp / draft-hardaker-dnsop-root-zone-publication-points / draft-hardaker-dnsop-dns-xfr-scheme / draft-hardaker-dnsop-root-zone-pub-list-guidelines
page: https://datatracker.ietf.org/doc/draft-wkumari-dnsop-localroot-bcp/ | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
DNS recursive resolver operators need to provide the best service possible for their users, which includes providing an operationally robust and privacy protecting service. Challenges to these deployment goals include difficulty of getting responses from the root servers (such as during a network attack), longer-than-desired round-trip times to the closest DNS root server, and privacy issues relating to queries sent to the DNS root servers. Resolvers can solve all of these issues by simply serving an already cached a copy of the full root zone. This document shows how resolvers can fetch, cache and maintain a copy of the root zone, how to detect if the contents becomes stale, and procedures for handling error conditions. { Editor note: This document contains a FAQ section. It will help answer questions about why this document is not a BCP but still has BCP in the name, how and why this document differs from RFC8806, etc etc etc. The FAQ section is intended to be removed before publication. }

### An IANA root zone publication source list format
Draft: draft-hardaker-dnsop-root-zone-publication-points · Working group: dnsop
Agenda: draft-wkumari-dnsop-localroot-bcp / draft-hardaker-dnsop-root-zone-publication-points / draft-hardaker-dnsop-dns-xfr-scheme / draft-hardaker-dnsop-root-zone-pub-list-guidelines
page: https://datatracker.ietf.org/doc/draft-hardaker-dnsop-root-zone-publication-points/ | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
This document describes a machine readable format to be used by IANA to publish a list of sources where the contents of the IANA DNS Root Zone may be fetched from.

### The DNS XFR URI Schemes
Draft: draft-hardaker-dnsop-dns-xfr-scheme · Working group: dnsop
Agenda: draft-wkumari-dnsop-localroot-bcp / draft-hardaker-dnsop-root-zone-publication-points / draft-hardaker-dnsop-dns-xfr-scheme / draft-hardaker-dnsop-root-zone-pub-list-guidelines
page: https://datatracker.ietf.org/doc/draft-hardaker-dnsop-dns-xfr-scheme/ | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
The DNS protocol provides an in-band mechanism for transferring the contents of a zone from a server to a client. This is most frequently used when secondary servers are transferring the DNS zone content from their configured primary server. This document defines a Uniform Resource Identifier (URI) scheme for referencing DNS servers from which DNS zone contents can be transferred.

### Guidelines for IANA DNS Root Zone Publication List Providers
Draft: draft-hardaker-dnsop-root-zone-pub-list-guidelines · Working group: dnsop
Agenda: draft-wkumari-dnsop-localroot-bcp / draft-hardaker-dnsop-root-zone-publication-points / draft-hardaker-dnsop-dns-xfr-scheme / draft-hardaker-dnsop-root-zone-pub-list-guidelines
page: https://datatracker.ietf.org/doc/draft-hardaker-dnsop-root-zone-pub-list-guidelines/ | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
This document describes guidelines for entities that wish to publish a list of URLs from where the contents of the IANA DNS root zone may be obtained. These guidelines are specifically provided as guidance to IANA, but these suggestions may be applicable to any entity wishing to build a list of IANA DNS root zone sources for their own purposes.

### DNS Filtering Transparency
Draft: draft-nottingham-dnsop-censorship-transparency · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-nottingham-dnsop-censorship-transparency
page: https://datatracker.ietf.org/doc/draft-nottingham-dnsop-censorship-transparency/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-sessa-dns-filtering-transparency-00 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
[I-D.ietf-dnsop-structured-dns-error] introduces structured error data for DNS responses that have been filtered. This specification allows more specific details of filtering incidents to be conveyed. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/mnot/public-resolver-errors.

### Ordering of RRSets in DNS Message Sections
Draft: draft-jabley-dnsop-ordered-answer-section · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/
page: https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-sessa-ordering-of-rrsets-in-dns-message-sections-draft-jabley-dnsop-ordered-answer-section-00 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
The existing Domain Name System (DNS) specifications lack some clarity in their description of the process by which individual sections of a DNS message are constructed. This document updates RFC 1034 and RFC 1035 to provide a clearer specification, consistent with deployed implementations.

### ApertoDNS Protocol: A Modern Dynamic DNS Update Protocol
Draft: draft-ferro-dnsop-apertodns-protocol · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ferro-dnsop-apertodns-protocol/
page: https://datatracker.ietf.org/doc/draft-ferro-dnsop-apertodns-protocol/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-apertodns-protocol-a-modern-standard-for-dynamic-dns-updates-00 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
This document specifies the ApertoDNS Protocol, a modern RESTful protocol for dynamic DNS (DDNS) updates. It provides a secure, provider-agnostic alternative to legacy protocols, with native support for IPv4, IPv6, bulk updates, automatic IP detection, TXT record management for ACME DNS-01 challenges, and standardized authentication mechanisms. The protocol uses well-known URIs (RFC 8615), JSON payloads (RFC 8259), and bearer token authentication (RFC 6750) to enable interoperable dynamic DNS services across different providers.

### DNS for AI Discovery
Draft: draft-mozleywilliams-dnsop-dnsaid · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/
page: https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/ | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
The document standardizes an approach for publishing AI agents in the Domain Name System (DNS) so that other agents can discover them. Discovery is then initiated based on one of three generic use cases, in increasing computational and latency cost: (1) the requestor knows both the organization and agent (2) the requestor knows the organization that provides a capability, but not the specific agent (3) the requestor knows the required capability, but not the organization or agent. Of these use cases only (1) and (2) are in scope for this document, although (3) can be derived from this specification. DNS for AI Discovery (DNS-AID) is designed so that, once a client has learned an organization's agents, subsequent transactions can utilize the first use case with the benefit of cacheable connectivity information that is learnable as an agentic skill. The mechanism uses Service Binding (SVCB) records for connectivity information and key meta data, a well known entry point using DNS-Based Service Discovery (DNS-SD) labels into an organization's agent index, and optionally DNS Security Extensions (DNSSEC) and DNS-Based Authentication of Named Entities (DANE) TLSA records for trust and security. DNS-AID provides consumers of agent services with a direct connection method for agentic workloads not mediated by a third party. Organizations can use the same approach across public and private networks networks, providing consistency and common operational models, including publishing agents that are hosted in service provider domains. This document introduces no new resource record types, opcodes, or response codes.

### DNS Extensions to Energy Efficiency as a Service(EEAS)
Draft: draft-zhu-dnsop-de-eeas · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-zhu-dnsop-de-eeas/
page: https://datatracker.ietf.org/doc/draft-zhu-dnsop-de-eeas/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-dns-extensions-to-energy-efficiency-as-service-00 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
This document describes a new Mechanism and DNS resource record (RR) type to carry information about energy-related characteristics for end-to-end internet access. The "EE" ("Energy Efficiency") record allows the network to provide different levels of energy-saving service. By providing more energy information to the client before it attempts to establish a connection, these records offer potential benefits to enhancements on energy as service criteria.

### RootCache overview
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-rootcache-overview-00 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### LocalRoot documents overview
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-localroot-documents-overview-01 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### DNS-AID DNSOP
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-dnsop-update-dns-aid-dnsop-00 | video: https://youtu.be/0T9YogV43GU | materials: https://datatracker.ietf.org/meeting/125/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

## Working Group: grow

### BMP YANG Model for Network Telemetry Messages
Draft: draft-netana-nmop-message-broker-bmp-telemetry-msg · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-netana-nmop-message-broker-bmp-telemetry-msg/
page: https://datatracker.ietf.org/doc/draft-netana-nmop-message-broker-bmp-telemetry-msg/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-bmp-yang-model-for-network-telemetry-messages-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
This document defines an extensible message schema in YANG to be used at BMP collectors to transform BMP messages into messages which are consumed by external systems such as Message Brokers.

### Requirements for Monitoring RPKI-Related Processes on Routers Using BMP
Draft: draft-wang-grow-bmp-rpki-mon-reqs · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/
page: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-requirements-for-monitoring-rpki-related-processes-on-routers-using-bmp-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
This document outlines requirements for extending the BGP Monitoring Protocol (BMP) to provide comprehensive monitoring of RPKI-related processes on routers, including RPKI data acquisition, RPKI-related policy configuration, route validation, and the impact of validation on routing decisions. The proposed extensions aim to standardize router-side monitoring of RPKI within BMP, focusing specifically on RPKI's effect on BGP routing decisions while maintaining a clear scope boundary with other monitoring mechanisms such as YANG modeling and streaming telemetry for RPKI-to-Router (RTR) protocol operations.

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-bmp-v4-tlv-support-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
Most of the BGP Monitoring Protocol (BMP) message types make provision for data in Type, Length, Value (TLV) format. However, Route Monitoring messages (which provide a snapshot of the monitored Routing Information Base) Stats Reports (which supply periodical counters) and Peer Down messages (which indicate that a peering session was terminated) do not. Supporting (optional) data in TLV format across all BMP message types provides consistent and extensible structures that would be useful among the various use- cases where conveying additional data to a monitoring station is required. This document updates RFC 7854 [RFC7854] to support TLV data in all message types and defines some essential TLVs. Additionally, this document introduces support for enterprise- specific TLVs in the BGP Monitoring Protocol by defining an Enterprise Bit (E-bit) that allows usage of per-vendor Type values.

### Logging of routing events in BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-rel · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-log-more-routing-events-in-the-bgp-monitoring-protocol-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
The BGP Monitoring Protocol (BMP) does provide for BGP session event logging (Peer Up, Peer Down), state synchronization (Route Monitoring), debugging (Route Mirroring) and Statistics messages, among others. This document defines a new Route Event Logging (REL) message type for BMP with the aim of covering use cases with affinity to alerting, reporting and on-change analysis.

### Filtering Adj-Rib-In and Adj-Rib-Out to BMP receivers
Draft: draft-ietf-grow-bmp-adj-ribs-filtered · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/ | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
Filtering RIBs in BMP (BGP Monitoring Protocol) can be desirable for several use-cases like, for example, limiting the amount of data a collector station has to process or allow a sender to export only a certain afi/safi of interest. This document defines an indicator to inform a collector station that a Adj-Rib-In or Adj-Rib-Out data feed is being filtered at the BMP exporter. This document updates RFC 7854.

### Log More Routing Events in the BGP Monitoring Protocol (BMP)
Draft: draft-geng-grow-bmp-rel-enhancement · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rel-enhancement/
page: https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rel-enhancement/ | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
The Route Event Logging (REL) message is defined in [I-D.ietf-grow-bmp-rel], which enables monitored routers to report event-driven operational data to BMP collectors. This document defines additional event code points for BGP FlowSpec RFC8955 [RFC8956] and BGP SR Policies [I-D.ietf-idr-sr-policy-safi]. These extensions enhance monitoring visibility for policy execution failures and improve network operation and troubleshooting capabilities.

### BGP Monitoring Protocol (BMP) Enhancements for RIB View Synchronization and Monitoring Options Notification
Draft: draft-geng-grow-bmp-sync-options-and-state · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-geng-grow-bmp-sync-options-and-state/
page: https://datatracker.ietf.org/doc/draft-geng-grow-bmp-sync-options-and-state/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-bgp-monitoring-protocol-bmp-enhancements-for-rib-view-synchronization-and-monitoring-options-notification-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
The BGP Monitoring Protocol (BMP) is a widely deployed operational tool that allows BMP collectors to obtain per-address-family BGP Routing Information Base (RIB) entries, runtime statistics, events, and other critical BGP state data from BMP sender routers, enabling full visibility into BGP routing status and supporting core network operations such as troubleshooting, security monitoring, and traffic auditing. However, two key limitations exist in the current BMP specification during practical deployment. First, transient faults, message loss, or session interruptions may cause inconsistencies between the RIB views of the BMP sender and collector, and the existing protocol lacks a non-disruptive mechanism to resolve such mismatches. Second, there is no standardized notification mechanism for senders to inform collectors of modified or updated monitoring reporting options, leading collectors to store stale or invalid BGP information as reporting configurations change. This document defines two new backward-compatible BMP message types to address these issues: a Route-Refresh message for non-disruptive RIB view synchronization between senders and collectors, and a Monitoring Options (MO) message to notify collectors of active and disabled reporting parameters. These extensions enhance the reliability and accuracy of BMP-based BGP monitoring without disrupting existing deployment workflows.

### Extension for BMP Peer Interface
Draft: draft-lin-grow-bmp-peer-interface · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-lin-grow-bmp-peer-interface/
page: https://datatracker.ietf.org/doc/draft-lin-grow-bmp-peer-interface/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-extension-for-bmp-peer-header-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
This document proposes extending BMP to allow BMP messages with the per-peer header to carry interface information for the established peer session, especially in order to distinguish parallel link-local and unnumbered BGP peers established based on distinct interfaces.

### BMP Statistics Information TLV
Draft: draft-msri-grow-bmp-stats-informational-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-msri-grow-bmp-stats-informational-tlv/
page: https://datatracker.ietf.org/doc/draft-msri-grow-bmp-stats-informational-tlv/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-bmp-statistics-information-tlv-draft-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
The BGP Monitoring Protocol (BMP) defines statistics reports that provide periodic snapshots of various BGP-related metrics. When statistics are reported periodically, the snapshot values may not reflect the variations that occurred between reporting intervals. This document defines a Statistics Information TLV that can be used to convey additional statistical information about BMP gauge-type statistics during the reporting period. This TLV reports the minimum and maximum values observed (with timestamps indicating when they occurred), along with additional statistical measures such as average, median, or snapshot values. This enables BMP collectors to better understand the dynamics of monitored statistics even when the reported snapshot values appear constant.

### BMP Route Change Statistics Based on Routing Policy
Draft: draft-smc-grow-bmp-route-change-stats · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/
page: https://datatracker.ietf.org/doc/draft-smc-grow-bmp-route-change-stats/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-route-change-statistics-based-on-policy-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
This document defines few generic BGP Monitoring Protocol (BMP) statistics for monitoring route modifications or changes due to applying Routing Policy. These statistics are reported per BGP peer using the BMP Statistics Report message. This revision (-02) firms up the specification for working group consideration: it adds a Relationship to Other Work section that explicitly maps this document to concurrently circulating GROW contributions on BMP statistics and policy-driven telemetry and invites coordination with their authors, adds a worked example, and strengthens Security Considerations. No statistics semantics, Stat Type allocations, or wire formats defined in -01 are changed.

### EVPN-Specific BMP RIB Statistics Extensions
Draft: draft-saum-grow-bmp-afi-safi-evpn · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/
page: https://datatracker.ietf.org/doc/draft-saum-grow-bmp-afi-safi-evpn/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-evpn-specific-bmp-rib-statistics-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
This document defines new EVPN-specific BGP Monitoring Protocol (BMP) statistics types. These extensions include scalar counters for EVPN route types specifically, while also keeping scope for defining counters which are EVPN route-type agnostic but related to BGP-EVPN RIB like, number of multihoming Ethernet Segments, number of multihomed EVIs, number of aliased paths, number of dynamic inter-VRF route leaking (IVRL). This revision (-06) firms up the specification for working group consideration: it adds a Relationship to Other Work section that explicitly maps this document to concurrently circulating GROW contributions on BMP statistics and TLV extensions and invites coordination with their authors, corrects the YANG alignment reference, strengthens Security Considerations, and adds a worked example. No statistics semantics, Stat Type/Subtype allocations, or wire formats defined in -05 are changed.

### BMP Route Event Logging
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-grow-bmp-route-event-logging-00 | video: https://youtu.be/r905qPlOzq0 | materials: https://datatracker.ietf.org/meeting/125/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

## Working Group: httpbis

### HTTP Redirect Headers
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-http-redirect-headers-01 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP Signature-key Header
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-http-signature-key-header-00 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Preliminary Request Denied
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-preliminary-request-denied-00 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Unbound DATA for CONNECT in HTTP/3
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-unbound-data-for-connect-in-http3-00 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### CONNECT-TCP
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-connect-tcp-00 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-resumable-uploads-00 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### MOQPACK
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-httpbis-moqpack-00 | video: https://youtu.be/5Kqz6MJDsgM | materials: https://datatracker.ietf.org/meeting/125/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

## Working Group: idr

### YANG Model for Border Gateway Protocol (BGP-4)
Draft: draft-ietf-idr-bgp-model · Working group: idr
Agenda: draft-ietf-idr-bgp-model-19
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/ | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document defines a YANG data model for configuring and managing BGP, including protocol, policy, and operational aspects, such as RIB, based on data center, carrier, and content provider operational requirements.

### BGP Deterministic Path Forwarding (DPF)
Draft: draft-wang-idr-dpf · Working group: idr
Agenda: draft-wang-idr-dpf-00
page: https://datatracker.ietf.org/doc/draft-wang-idr-dpf/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessb-2-bgp-deterministic-path-forwarding-dpf-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
Modern data center (DC) fabrics typically employ Clos topologies with External BGP (EBGP) for plain IPv4/IPv6 routing. While hop-by-hop EBGP routing is simple and scalable, it provides only a single best- effort forwarding service for all types of traffic. This single best-effort service might be insufficient for increasingly diverse traffic requirements in modern DC environments. For example, loss and latency sensitive AI/ML flows may demand stronger Service Level Agreements (SLA) than general purpose traffic. Duplication schemes which are standardized through protocols such as Parallel Redundancy Protocol (PRP) require disjoint forwarding paths to avoid single points of failure. Congestion avoidance may require more deterministic forwarding behavior. This document introduces BGP Deterministic Path Forwarding (DPF), a mechanism that partitions the physical fabric into multiple logical fabrics. Flows can be mapped to different logical fabrics based on their specific requirements, enabling deterministic forwarding behavior within the data center.

### BGP PORT EC for AIDC
Draft: draft-zhang-idr-portid-ec · Working group: idr
Agenda: draft-zhang-idr-portid-ec-00
page: https://datatracker.ietf.org/doc/draft-zhang-idr-portid-ec/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-3-bgp-port-ec-for-aidc-pdf-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document introduces a new BGP extended community attribute for AI computing scenarios. This attribute is used to carry the port ID when advertising routes on the switch before launching AI tasks, preparing for negotiation before sending large-scale traffic.

### Fully Adaptive Routing Ethernet using BGP
Draft: draft-xu-idr-fare · Working group: idr
Agenda: draft-xu-idr-fare
page: https://datatracker.ietf.org/doc/draft-xu-idr-fare/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessb-4-1-fully-adaptive-routing-ethernet-using-bgp-01 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
Large language models (LLMs) like ChatGPT have become increasingly popular in recent years due to their impressive performance in various natural language processing tasks. These models are built by training deep neural networks on massive amounts of text data, as well as visual and video data, and often consist of billions or even trillions of parameters. However, the training process for these models can be extremely resource-intensive, requiring the deployment of thousands or even tens of thousands of GPUs in a single AI training cluster. Therefore, three-stage or even five-stage CLOS networks are commonly adopted for AI networks. The non-blocking nature of the network becomes increasingly critical for large-scale AI model training. Therefore, adaptive routing is necessary to dynamically distribute traffic to the same destination across multiple equal-cost paths, based on network capacity information along those paths.

### BGP Neighbor Discovery
Draft: draft-xu-idr-neighbor-autodiscovery · Working group: idr
Agenda: draft-xu-idr-neighbor-autodiscovery
page: https://datatracker.ietf.org/doc/draft-xu-idr-neighbor-autodiscovery/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessb-4-2-bgp-neighbor-discovery-02 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
BGP is being used as the underlay routing protocol in some large- scaled data centers (DCs). Most popular design followed is to do hop-by-hop external BGP (EBGP) session configurations between neighboring routers on a per link basis. The provisioning of BGP neighbors in routers across such a DC brings its own operational complexity. This document introduces a BGP neighbor discovery mechanism that greatly simplifies BGP operations in such DC and other networks by automatic setup of BGP sessions between neighbor routers using this mechanism.

### BGP Extensions for Inter-Domain Flexible Algorithm with Segment Routing over IPv6 (SRv6)
Draft: draft-gong-idr-inter-domain-srv6-flex-algo · Working group: idr
Agenda: draft-gong-idr-inter-domain-srv6-flex-algo-00
page: https://datatracker.ietf.org/doc/draft-gong-idr-inter-domain-srv6-flex-algo/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessb-5-bgp-extensions-for-inter-domain-flexible-algorithm-with-segment-routing-over-ipv6-srv6-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
IGP Flexible Algorithm (Flex-Algo) provides a mechanism for IGP nodes to compute the best paths according to a set of constraints in both the topology and computation metrics. Segment Routing over IPv6 (SRv6) can be used as one of the data plane of IGP Flex-Algo. In SRv6 networks, services may be carried across multiple network domains which are under the same administration. For some services, it is expected that the an end-to-end inter-domain path can be computed according to the same constraints (such as low latency) defined by Flex-Algo. This document describes BGP extensions to advertise SRv6 locators as IPv6 prefixes, together with the associated algorithm across the AS boundary.

### BGP Signaling for Multipath Traffic Engineering Junction States
Draft: draft-zzhang-idr-mpte-signaling · Working group: idr
Agenda: draft-zzhang-idr-mpte-signaling-00
page: https://datatracker.ietf.org/doc/draft-zzhang-idr-mpte-signaling/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-mpte-bgp-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
Multi-Path Traffic Engineering (MPTE) combines Traffic Engineering with Multi-Path forwarding, offering a much desired TE solution for both traditional WAN and new AIML DC/DCI. MPTE tunnels are based on MPTE Directed Acyclic Graph (DAG) and can be signaled with extensions to RSVP-TE, PCEP, BGP. This document specifies the BGP protocol extensions and procedures for signaling MPTE DAGs.

### SRv6 Policy SID List Optimization Advertisement
Draft: draft-ali-idr-srv6-policy-sl-opt-distribution · Working group: idr
Agenda: draft-ali-idr-srv6-policy-sl-opt-distribution-02
page: https://datatracker.ietf.org/doc/draft-ali-idr-srv6-policy-sl-opt-distribution/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-srv6-policy-sid-list-optimization-advertisement-draft-ali-idr-srv6-policy-sl-opt-distribution-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
In some use cases, an SRv6 policy's SID list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This draft specifies a BGP-LS extension to indicate whether the endpoint's node SID is included or excluded in installing SID list(s) of the Candidate Path (CP) of an SRv6 policy.

### BGP Communities for Security Policy Intent
Draft: draft-guo-idr-bgp-security-policy-community · Working group: idr
Agenda: draft-guo-idr-bgp-security-policy-community-01
page: https://datatracker.ietf.org/doc/draft-guo-idr-bgp-security-policy-community/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-8-bgp-communities-for-security-policy-intent-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document specifies a set of standardized BGP community to signal inter-AS routing security policy intent. The initial focus is on RPKI-based Route Origin Validation (ROV) using ROAs [RFC6482] [RFC6811] [RFC9582]. ROV produces validation outcomes such as "Valid", "Invalid", and "NotFound", but the operational treatment of "NotFound" and similar ambiguous cases is entirely a matter of local policy and often differs across networks. This document defines transitive community that allows an Origin AS to explicitly express its security policy expectations regarding how its own originated routes SHOULD be treated when downstream Autonomous Systems (ASes) perform ROA-based origin validation. A typical example is an Origin AS indicating a preference for strict handling of ambiguous validation outcomes (e.g., NotFound) for its prefixes. Unlike validation states, these community does not assert correctness, authorization, or RPKI deployment status, which is confront to [AVOID-RPKI-STATE-IN-BGP]. Instead, they communicate origin-declared policy intent to all downstream ASes, enabling them to correlate this intent with locally derived validation results. By enabling explicit signaling of security expectations without exporting validation state, this mechanism allows downstream ASes to make more informed policy decisions while reducing the risk of accidental outages caused by misalignment between origin expectations and downstream local policies. The mechanism is orthogonal to existing routing security validation technologies and does not alter their semantics or deployment models.

### BGP SR Policy Extensions for Metric
Draft: draft-ietf-idr-sr-policy-metric · Working group: idr
Agenda: draft-ietf-idr-sr-policy-metric-05
page: https://datatracker.ietf.org/doc/draft-ietf-idr-sr-policy-metric/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessa-2-1-bgp-sr-policy-extensions-for-metric-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
An SR Policy consists of one or more Candidate Paths (CPs), each comprising one or more segment lists. BGP can be used to propogate SR Policy CPs to the SR Policy headend nodes in the network. After an SR Policy CP is installed on the headend node, packets can be steered into the SR Policy. For a particular BGP destination, if there are multiple BGP routes with different next-hops, BGP best path selection is performed and the IGP metric to the next-hop node may be used for tie-breaking to select the best path. When the path to the next-hop is resolved over an SR Policy, the IGP metric of the SR policy is needed for BGP path selection. This document defines the BGP extensions to carry the IGP metric of segment lists when BGP is used to propagate SR Policy CPs.

### BGP Link-State Extensions for BGP-only Networks
Draft: draft-ietf-idr-bgp-ls-bgp-only-fabric · Working group: idr
Agenda: draft-ietf-idr-bgp-ls-bgp-only-fabric-04
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-bgp-only-fabric/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-bgp-link-state-extensions-for-bgp-only-networks-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
BGP is used as the only routing protocol in some networks today. In such networks, it is useful to get a detailed topology view similar to one available when using link state routing protocols. This document defines extensions to the BGP Link-state (BGP-LS) address- family and the procedures for advertisement of topology information in a BGP-only network.

### Interface Index Capability for BGP
Draft: draft-lin-idr-interface-index-capability · Working group: idr
Agenda: draft-lin-idr-interface-index-capability-00
page: https://datatracker.ietf.org/doc/draft-lin-idr-interface-index-capability/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-interface-index-capability-for-bgp-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
In some scenarios using unnumbered links, it is necessary for the BGP protocol to advertise the link's Interface Index and obtain the peer's Remote Interface Index. This document defines a new BGP capability, as specified in RFC 5492, for advertising local interface indexes and obtaining neighbor interface indexes.

### BGP Extensions for Network Resource Partition
Draft: draft-li-idr-bgp-nrp · Working group: idr
Agenda: draft-li-idr-bgp-nrp-00
page: https://datatracker.ietf.org/doc/draft-li-idr-bgp-nrp/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessa-2-4-bgp-extensions-for-network-resource-partition-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
Existing approaches bind a Segment Routing (SR) Policy to a Network Resource Partition (NRP) on a one-to-one basis, which lacks flexibility and introduces significant operational overhead as the number of NRPs scales, especially when multiple NRPs share the same SR Policy path. This document defines BGP extensions to advertise NRP Identifier (NRP ID) information within BGP Update messages between headend and endpoint nodes. It decouples SR Policies from NRPs, allowing multiple NRPs to share a common SR Policy path and avoiding linear growth of SR Policies. The proposed design reduces operational complexity and also applies to SR Best Effort (SR BE) scenarios.

### BGP SR Policy Extensions for BFD Configuration
Draft: draft-li-idr-bgp-sr-policy-bfd-extension · Working group: idr
Agenda: draft-li-idr-bgp-sr-policy-bfd-extension-01
page: https://datatracker.ietf.org/doc/draft-li-idr-bgp-sr-policy-bfd-extension/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessa-2-5-bgp-sr-policy-extensions-for-bfd-configuration-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
Segment Routing (SR) Policies require fast failure detection for Candidate Paths (CPs) to enable rapid rerouting and high availability. Currently, the provisioning of SR Policies and the configuration of the associated Seamless Bidirectional Forwarding Detection (S-BFD) sessions are performed independently. This often necessitates separate mechanisms (e.g., manual configuration, NETCONF, or additional signaling) to associate S-BFD sessions with the SR Policies, resulting in complex and error-prone operations. This document defines extensions to BGP SR Policy for the simultaneous provisioning of SR Policy CPs and their S-BFD configuration parameters during policy advertisement. The extensions include optional sub-TLVs within the Tunnel Encapsulation Attribute to carry S-BFD configuration parameters (e.g., discriminators, intervals, multipliers). These extensions simplify deployment in distributed or controller- based environments, reduce configuration overhead, and enhance operational efficiency for SR-based traffic engineering.

### BGP Extension for SRv6 Policy Segment List optimization
Draft: draft-liu-idr-sr-segment-list-optimize · Working group: idr
Agenda: draft-liu-idr-sr-segment-list-optimize-02
page: https://datatracker.ietf.org/doc/draft-liu-idr-sr-segment-list-optimize/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-bgp-extension-for-srv6-policy-segment-list-optimization-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
In some use cases, an SRv6 policy's segment list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This document specifies a BGP extension to indicate whether the endpoint's node SID needs to be included or excluded when installing the SRv6 Policy. This optimization can improve the forwarding efficiency of data packets when End SID and Service SID are present.

### Supplement of BGP-LS Distribution for SR Policies and State
Draft: draft-lp-idr-bgp-ls-sr-policy-supplement · Working group: idr
Agenda: draft-lp-idr-bgp-ls-sr-policy-supplement-06
page: https://datatracker.ietf.org/doc/draft-lp-idr-bgp-ls-sr-policy-supplement/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessa-7-supplement-of-bgp-ls-distribution-for-sr-policies-and-state-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document supplements additional information of the segment list in the BGP-LS advertisement for SR Policy state information. A new flag and a new sub-TLV are introduced in the SR Segment List TLV of BGP-LS SR Policy Candidate Path NLRI.

### Advertising SAV Rule-related Information using BGP Link-State
Draft: draft-tong-idr-bgp-ls-sav-rule · Working group: idr
Agenda: draft-tong-idr-bgp-ls-sav-rule-04
page: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-2-8-advertising-sav-rule-related-information-using-bgp-link-state-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document proposes extensions to the BGP Link-State protocol for advertising Source Address Validation (SAV) rule-related information for monitoring and management purposes.

### BGP Flow Specification Filtered by Destination-QP
Draft: draft-lll-idr-flowspec-filter-qp · Working group: idr
Agenda: draft-lll-idr-flowspec-filter-qp
page: https://datatracker.ietf.org/doc/draft-lll-idr-flowspec-filter-qp/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-2-8-bgp-flow-specification-filtered-by-destination-qp-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
BGP Flowspec mechanism (BGP-FS) [RFC8955] [RFC8956] propagates both traffic Flow Specifications and Traffic Filtering Actions by making use of the BGP NLRI and the BGP Extended Community encoding formats. This document specifies a new BGP-FS component type named Destination-QP (Destination Queue Pair) to support filtering by Destination-QP.

### BGP Flow Specification Extension for Feedback Binding
Draft: draft-cui-idr-flowspec-feedback-binding · Working group: idr
Agenda: draft-cui-idr-flowspec-feedback-binding-00
page: https://datatracker.ietf.org/doc/draft-cui-idr-flowspec-feedback-binding/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-2-11-bgp-flow-specification-extension-for-feedback-binding-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document specifies a BGP Flow Specification extension that conveys per-route feedback binding for a FlowSpec route using the BGP Extended Community attribute. The proposed mechanism introduces a single Feedback Action, encoded as a Generic Transitive Extended Community, which enables downstream routers to report telemetry information or operational events associated with a FlowSpec rule. The Feedback Action carries parameters including a Feedback Identifier (FID), a window exponent (WINC) that defines the periodic aggregation interval, an event flag, and a scope selector to control where feedback is generated. These parameters are attached to the FlowSpec route and are propagated across AS boundaries unchanged. This document focuses on the signaling aspect; a companion document may define how feedback information is exported as part of a network telemetry framework (e.g., leveraging the BGP Monitoring Protocol (BMP)) or equivalent mechanisms to report periodic and event-driven feedback keyed by the FID.

### Destination-IP-Origin-AS Filter for BGP Flow Specification
Draft: draft-wang-idr-flowspec-dip-origin-as-filter · Working group: idr
Agenda: draft-wang-idr-flowspec-dip-origin-as-filter-12
page: https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-dip-origin-as-filter/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessa-2-12ip-and-as-community-filters-for-bgp-flow-specification-02 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document defines an extension to the Border Gateway Protocol (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr- fsv2-ip-basic] to enable filtering based on the Origin Autonomous System (AS) of the destination IP address. This extension is particularly useful in mitigating Distributed Denial of Service (DDoS) attacks or optimizing traffic redirection where the target IP addresses are numerous or rapidly changing, but belong to a specific destination Origin AS.

### Source-IP-Origin-AS Filter for BGP Flow Specification
Draft: draft-wang-idr-flowspec-sip-origin-as-filter · Working group: idr
Agenda: draft-wang-idr-flowspec-sip-origin-as-filter-00
page: https://datatracker.ietf.org/doc/draft-wang-idr-flowspec-sip-origin-as-filter/ | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document defines an extension to the Border Gateway Protocol (BGP) Flow Specification Version 2 (FSv2) defined in [draft-ietf-idr- fsv2-ip-basic] to enable filtering based on the Origin Autonomous System (AS) of the source IP address. This extension is particularly useful in mitigating Distributed Denial of Service (DDoS) attacks where the source IP addresses are dynamic or numerous but belong to a specific source AS.

### Destination-IP-Community Filter for BGP Flow Specification
Draft: draft-wu-idr-flowspec-dip-community-filter · Working group: idr
Agenda: draft-wu-idr-flowspec-dip-community-filter-01
page: https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-dip-community-filter/ | materials: https://datatracker.ietf.org/meeting/125/session/idr
BGP Flow Specification Version 2 (FSv2) propagates both traffic Flow Specifications and Traffic Filtering Actions using an extensible TLV- based filter family architecture. This document specifies a new FSv2 component type under the Routing Filter Family to support community- level filtering. The match condition evaluates the BGP Community attribute associated with the destination IP address encoded in the Flowspec NLRI. This mechanism is intended for deployment within a single administrative domain.

### Source-IP-Community Filter for BGP Flow Specification
Draft: draft-wu-idr-flowspec-sip-community-filter · Working group: idr
Agenda: draft-wu-idr-flowspec-sip-community-filter-00
page: https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-sip-community-filter/ | materials: https://datatracker.ietf.org/meeting/125/session/idr
BGP Flow Specification Version 2 (FSv2) propagates traffic Flow Specifications and Traffic Filtering Actions using an extensible TLV- based filter family architecture. This document specifies a new FSv2 component type under the Routing Filter Family to support community- level filtering within a single administrative domain. The match condition filters traffic based on the BGP Community attributes associated with the route matching the packet's source IP address.

### BGP Failure Propagation (BGP-FP) for Enhancing Control-Plane Convergence
Draft: draft-li-idr-bgp-failure-propagation-convergence · Working group: idr
Agenda: draft-li-idr-bgp-failure-propagation-convergence-01
page: https://datatracker.ietf.org/doc/draft-li-idr-bgp-failure-propagation-convergence/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-13-bgp-failure-propagation-for-enhancing-control-plane-convergence-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
This document specifies BGP Failure Propagation (BGP-FP), an infrastructure and protocol that improves inter-domain routing convergence by accelerating the removal of stale (invalid) routes. BGP-FP uses (1) an Agent deployed per Autonomous System (AS) to detect inter-AS reachability changes and to configure local routers, (2) a logically centralized Repository to store and selectively forward AS reachability state, and (3) BGP Large Communities as a "route freshness" marker. Agents validate and apply Repository updates to filter routes that traverse AS pairs whose reachability has been lost or that violate the originating AS's forwarding intent, reducing route-flap propagation in the control plane. This document clarifies that "AS reachability" refers to the reachability between two ASes, not to the state of individual physical or logical links within an AS. If multiple links exist between two ASes, the failure of a single link that does not break overall AS-to-AS reachability does not trigger the BGP-FP mechanism. A new Repository deployment model is introduced, suggesting that the Repository be operated by a newly established organization composed of Tier-1 ASes and Regional Internet Registries (RIRs), using a distributed deployment with Byzantine fault-tolerant consensus and rotating leadership.

### 9. Signaling Alternative Labels for BGP Prefixes
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessa-9-signaling-alternative-labels-for-bgp-prefixes-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### FSv2-IETF125-side meeting
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-fsv2-ietf125-side-meeting-00 | video: https://youtu.be/a0BiAUtfF4c | materials: https://datatracker.ietf.org/meeting/125/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### 1. BGP YANG
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-bgp-yang-00 | video: https://youtu.be/yw6h3n-7qXE | materials: https://datatracker.ietf.org/meeting/125/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

## Working Group: ipsecme

### KEM-based Authentication for IKEv2 with Post-quantum Security
Draft: draft-wang-ipsecme-kem-auth-ikev2 · Working group: ipsecme
Agenda: draft-wang-ipsecme-kem-auth-ikev2
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-kem-auth-ikev2/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-kem-based-authentication-for-ikev2-with-post-quantum-security-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
This draft specifies a new authentication mechanism, called KEM (Key Encapsulation Mechanism) -based authentication, for the Internet Key Exchange Protocol Version 2 (IKEv2). This is motivated by the fact that some post-quantum KEMs (like ML-KEM) are more efficient than post-quantum signature algorithms (like ML-DSA).

### Using IKE Fragmentation for Large Messages
Draft: draft-smyslov-ipsecme-ikev2-fragm-large-msg · Working group: ipsecme
Agenda: draft-smyslov-ipsecme-ikev2-fragm-large-msg
page: https://datatracker.ietf.org/doc/draft-smyslov-ipsecme-ikev2-fragm-large-msg/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-use-of-ike-fragmentation-for-large-messages-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
This document describes describes issues with using Internet Key Exchange version 2 (IKEv2) fragmentation for transmitting large messages on unreliable transport. The document proposes several approaches for dealing with these issues: randomizing the order the fragments are sent, dispersing sending fragments over time and selective retransmission of fragments based on information from the peer about their receipt.

### PQ/T Hybrid Composite Key Exchange and Reliable Transport for IKEv2
Draft: draft-reddy-ipsecme-ikev2-hybrid-reliable · Working group: ipsecme
Agenda: draft-reddy-ipsecme-ikev2-hybrid-reliable
page: https://datatracker.ietf.org/doc/draft-reddy-ipsecme-ikev2-hybrid-reliable/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-pqt-hybrid-composite-key-exchange-reliable-transport-for-ikev2-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
The eventual transition to post-quantum key exchange will require elimination of traditional key exchange for reduced protocol complexity and efficiency. IKEv2 therefore requires a mechanism that can operate in a PQC-only environment, without depending on traditional key exchange algorithms (e.g., MODP DH or ECDH). As IKEv2 permits arbitrary combinations of algorithms, unnecessary complexity and insecure hybrid constructions are easily implemented. This document defines PQ/T hybrid composite key exchange algorithms for IKEv2 and a single combined KE payload that carries both the traditional and post-quantum components. It also leverages the existing IKEv2 reliable transport mechanism so that large PQC key exchange messages can be reliably exchanged over TCP. Together, these mechanisms enable secure and efficient PQ/T hybrid deployments today and provide a clear path for IKEv2 to operate in environments where traditional algorithms have been replaced by PQC algorithms.

### Encapsulating IPsec ESP in UDP for Load-balancing
Draft: draft-xu-ipsecme-esp-in-udp-lb · Working group: ipsecme
Agenda: draft-xu-ipsecme-esp-in-udp-lb
page: https://datatracker.ietf.org/doc/draft-xu-ipsecme-esp-in-udp-lb/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-encapsulating-ipsec-esp-in-udp-for-load-balancing-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
IPsec Virtual Private Network (VPN) is widely used by enterprises to interconnect their geographical dispersed branch office locations across the Wide Area Network (WAN) or the Internet, especially in the Software-Defined-WAN (SD-WAN) era. In addition, IPsec is also increasingly used by cloud providers to encrypt IP traffic traversing data center networks and data center interconnect WANs so as to meet the security and compliance requirements, especially in financial cloud and governmental cloud environments. To fully utilize the bandwidth available in the data center network, the data center interconnect WAN or the Internet, load balancing of IPsec traffic over Equal Cost Multi-Path (ECMP) and/or Link Aggregation Group (LAG) is much attractive to those enterprises and cloud providers. This document defines a method to encapsulate IPsec Encapsulating Security Payload (ESP) packets over UDP tunnels for improving load-balancing of IPsec ESP traffic.

### Multi-Path Secret Sharing for QKD Key Relay in IP Networks
Draft: draft-li-ipsecme-qkd-multipath-secret-sharing · Working group: ipsecme
Agenda: draft-li-ipsecme-qkd-multipath-secret-sharing
page: https://datatracker.ietf.org/doc/draft-li-ipsecme-qkd-multipath-secret-sharing/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-multi-path-secret-sharing-for-qkd-key-relay-in-ip-networks-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
Trusted relay is currently the most practical deployment model for Quantum Key Distribution (QKD) networks. However, trusted relay nodes pose inherent security vulnerabilities, as intermediate nodes can access the plaintext random number used to derive the end-to-end QKD key, leading to complete key exposure if any single relay node is compromised. To mitigate this risk, this document proposes a Multi- Path Secret Sharing (MPSS) mechanism for QKD key relay. The core idea is to split the random number into multiple shares using a threshold secret sharing scheme, distribute each share through independent QKD relay paths planned by the Key Management Plane (KMP), and reconstruct the complete random number only at the destination node. This mechanism transforms the security model from "all-or-nothing" to "threshold security". Notably, this mechanism leverages an extended IPv6 Destination Option Header (DOH) to carry key share-related metadata and utilizes Segment Routing over IPv6 (SRv6) to enforce strict path isolation.

### Multi-Authentication in IKEv2 with Post-quantum Security
Draft: draft-wang-ipsecme-multi-auth-ikev2-pq · Working group: ipsecme
Agenda: draft-wang-ipsecme-multi-auth-ikev2-pq
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-multi-auth-ikev2-pq/ | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
Motivated to mitigate security threats against quantum computers, this draft specifies a general authentication mechanism in the Internet Key Exchange Protocol Version 2 (IKEv2) [RFC7296], called Multi-Authentication. Namely, two peers can negotiate two or more authentication methods to authenticate each other. The authentication methods selected do not necessarily belong to the same category. This mechanism is achieved by adding a new value (17) (TBD) in the "IKEv2 Authentication Method" registry [IANA-IKEv2], maintained by IANA. To run Multi-Authentication, two peers send the SUPPORTED_AUTH_METHODS Notify, defined in [RFC9593], to negotiate two or more authentication methods for authentication in IKEv2. [EDNOTE: Code points for Multi-Authentication may need to be assigned in the "IKEv2 Authentication Method" registry [IANA-IKEv2], maintained by IANA]

### FrodoKEM for IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-frodokem-for-ikev2-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Multi-Authentication in IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-multi-authentication-in-ikev2-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### BEET Mode draft-moskowitz-ipsecme-rfc7402-beet-update
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-beet-mode-draft-moskowitz-ipsecme-rfc7402-beet-update-00 | video: https://youtu.be/-0_gLUb5r3c | materials: https://datatracker.ietf.org/meeting/125/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

## Working Group: jose

### Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)
Draft: draft-ietf-jose-hpke-encrypt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/ | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
This specification defines how to use Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE). HPKE enables public key encryption of arbitrary-sized plaintexts to a recipient's public key, and provides security against adaptive chosen ciphertext attacks. This specification chooses a specific subset of the HPKE features to use with JWE. This specification updates RFC 7516 (JWE) to enable use of Integrated Encryption as a Key Management Mode.

### JOSE: Deprecate 'none' and 'RSA1_5'
Draft: draft-ietf-jose-deprecate-none-rsa15 · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/ | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
This document updates RFC 7518 to deprecate the JWS algorithm "none" and the JWE algorithm "RSA1_5". These algorithms have known security weaknesses. It also updates the Review Instructions for Designated Experts to establish baseline security requirements that future algorithm registrations are expected to meet.

### JSON Web Proof
Draft: draft-ietf-jose-json-web-proof · Working group: jose
Agenda: * JSON Web Proofs https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-jose-json-web-proof-update-03 | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
The JOSE set of standards established JSON-based container formats for Keys, Signatures, and Encryption. They also established IANA registries to enable the algorithms and representations used for them to be extended. Since those were created, newer cryptographic algorithms that support selective disclosure and unlinkability have matured and started seeing early market adoption. The COSE set of standards likewise does this for CBOR-based containers, focusing on the needs of environments which are better served using CBOR, such as constrained devices and networks. This document defines a new container format similar in purpose and design to JSON Web Signature (JWS) and COSE Signed Messages called a _JSON Web Proof (JWP)_. Unlike JWS, which integrity-protects only a single payload, JWP can integrity-protect multiple payloads in one message. It also specifies a new presentation form that supports selective disclosure of individual payloads, enables additional proof computation, and adds a Presentation Header to prevent replay.

### JSON Proof Algorithms
Draft: draft-ietf-jose-json-proof-algorithms · Working group: jose
Agenda: * JSON Proof Algorithms https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/ | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
The JSON Proof Algorithms (JPA) specification registers cryptographic algorithms and identifiers to be used with the JSON Web Proof, JSON Web Key (JWK), and COSE specifications. It defines IANA registries for these identifiers.

### JSON Proof Token and CBOR Proof Token
Draft: draft-ietf-jose-json-proof-token · Working group: jose
Agenda: * JSON Proof Token https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/ | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving representation of claims to be transferred between three parties. The claims in a JPT are encoded as base64url-encoded JSON objects that are used as the payloads of a JSON Web Proof (JWP) structure, enabling them to be digitally signed and selectively disclosed. JPTs also support reusability and unlinkability when using Zero-Knowledge Proofs (ZKPs). A CBOR-based representation of JPTs is also defined, called a CBOR Proof Token (CPT). It has the same properties as JPTs, but uses the JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based JWP Compact Serialization.

### PQ/T Hybrid Composite Signatures for JOSE and COSE
Draft: draft-ietf-jose-pq-composite-sigs · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-jose-pqt-hybrid-composite-signatures-for-jose-and-cose-00 | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
This document describes JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for Post- Quantum Traditional (PQ/T) hybrid composite signatures. The composite algorithms described combine the Module-Lattice-Based Digital Signature Algorithm (ML-DSA) as the post-quantum component and either the Elliptic Curve Digital Signature Algorithm (ECDSA) or the Edwards-Curve Digital Signature Algorithm (EdDSA) as the traditional component.

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE
Draft: draft-ietf-jose-pqc-kem · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/ | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
This document describes conventions for using Post-Quantum Key Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and Encryption (COSE).

### JOSE HPKE PQ & PQ/T Algorithm Registrations
Draft: draft-skokan-jose-hpke-pq-pqt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-skokan-jose-hpke-pq-pqt/
page: https://datatracker.ietf.org/doc/draft-skokan-jose-hpke-pq-pqt/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-jose-jose-hpke-pq-pqt-algorithm-registrations-01 | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
This document registers Post-Quantum (PQ) and Post-Quantum/ Traditional (PQ/T) hybrid algorithm identifiers for use with JSON Object Signing and Encryption (JOSE), building on the Hybrid Public Key Encryption (HPKE) framework.

### PQ KEMs for COSE AND JOSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-jose-pq-kems-for-cose-and-jose-00 | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### Post-Quantum and Hybrid KEMs for HPKE with JOSE and COSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-jose-post-quantum-and-hybrid-kems-for-hpke-with-jose-and-cose-00 | video: https://youtu.be/UtOpOWqveFw | materials: https://datatracker.ietf.org/meeting/125/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

## Working Group: lamps

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA)
Draft: draft-ietf-lamps-dilithium-certificates · Working group: lamps
Agenda: a) draft-ietf-lamps-dilithium-certificates ( RFC 9881 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Digital signatures are used within X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using FIPS 204, the Module-Lattice- Based Digital Signature Algorithm (ML-DSA) in Internet X.509 certificates and certificate revocation lists. The conventions for the associated signatures, subject public keys, and private key are also described.

### Use of the ML-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-ml-dsa · Working group: lamps
Agenda: b) draft-ietf-lamps-cms-ml-dsa ( RFC 9882 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-ml-dsa/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
The Module-Lattice-Based Digital Signature Algorithm (ML-DSA), as defined by NIST in FIPS 204, is a post-quantum digital signature scheme that aims to be secure against an adversary in possession of a Cryptographically Relevant Quantum Computer (CRQC). This document specifies the conventions for using the ML-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for SLH-DSA
Draft: draft-ietf-lamps-x509-slhdsa · Working group: lamps
Agenda: c) draft-ietf-lamps-x509-slhdsa ( RFC 9909 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-slhdsa/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Digital signatures are used within X.509 Public Key Infrastructure such as X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using the Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) in X.509 Public Key Infrastructure. The conventions for the associated signatures, subject public keys, and private keys are also specified.

### Updates to Lightweight OCSP Profile for High Volume Environments
Draft: draft-ietf-lamps-rfc5019bis · Working group: lamps
Agenda: a) draft-ietf-lamps-rfc5019bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5019bis/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This specification defines a profile of the Online Certificate Status Protocol (OCSP) that addresses the scalability issues inherent when using OCSP in large scale (high volume) Public Key Infrastructure (PKI) environments and/or in PKI environments that require a lightweight solution to minimize communication bandwidth and client- side processing. This specification obsoletes RFC 5019. The profile specified in RFC 5019 has been updated to allow and recommend the use of SHA-256 over SHA-1.

### Clarification and enhancement of RFC7030 CSR Attributes definition
Draft: draft-ietf-lamps-rfc7030-csrattrs · Working group: lamps
Agenda: b) draft-ietf-lamps-rfc7030-csrattrs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc7030-csrattrs/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document updates RFC7030, Enrollment over Secure Transport (EST), clarifying how the Certificate Signiing Request (CSR) Attributes Response can be used by an EST server to specify both CSR attribute Object IDs (OID) and also CSR attribute values, in particular X.509 extension values, that the server expects the client to include in subsequent CSR request. RFC9148 is derived from RFC7030, and it is also updated. RFC7030 (EST) is ambiguous in its specification of the CSR Attributes Response. This has resulted in implementation challenges and implementor confusion. As a result, there was not universal understanding of what was specified. This document clarifies the encoding rules. This document therefore also provides a new straightforward approach: using a template for CSR contents that may be partially filled in by the server. This also allows an EST server to specify a subject Distinguished Name (DN).

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)
Draft: draft-ietf-lamps-kyber-certificates · Working group: lamps
Agenda: c) draft-ietf-lamps-kyber-certificates
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). This document specifies the conventions for using the ML-KEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Unsigned X.509 Certificates
Draft: draft-ietf-lamps-x509-alg-none · Working group: lamps
Agenda: d) draft-ietf-lamps-x509-alg-none
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-alg-none/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document defines a placeholder X.509 signature algorithm that may be used in contexts where the consumer of the certificate is not expected to verify the signature. As part of this, it updates RFC 5280.

### Use of ML-KEM in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-kyber · Working group: lamps
Agenda: e) draft-ietf-lamps-cms-kyber
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-kyber/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). Three parameter sets for the ML-KEM algorithm are specified by the US National Institute of Standards and Technology (NIST) in FIPS 203. In order of increasing security strength (and decreasing performance), these parameter sets are ML-KEM-512, ML-KEM-768, and ML-KEM-1024. This document specifies the conventions for using ML-KEM with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in "Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" (RFC 9629).

### PKCS #8 Private-Key Information Content Types
Draft: draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes · Working group: lamps
Agenda: f) draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document defines PKCS #8 content types for use with PrivateKeyInfo and EncryptedPrivateKeyInfo as specified in RFC 5958.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-sigs · Working group: lamps
Agenda: a) draft-ietf-lamps-pq-composite-sigs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-pq-composite-kem-and-cms-composite-kem-00 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document defines combinations of US NIST Module-Lattice-Based Digital Signature Algorithm (ML-DSA) in hybrid with traditional algorithms RSASSA-PKCS1-v1.5, RSASSA-PSS, ECDSA, Ed25519, and Ed448. These combinations are tailored to meet regulatory guidelines in certain regions. Composite ML-DSA is applicable in applications that use X.509 or PKIX data structures that accept ML-DSA, but where the operator wants extra protection against breaks or catastrophic bugs in ML-DSA, and where existential unforgeability (EUF-CMA) level security is acceptable.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-composite-sigs · Working group: lamps
Agenda: b) draft-ietf-lamps-cms-composite-sigs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-sigs/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) defines combinations of ML-DSA with RSA, ECDSA, and EdDSA. This document specifies the conventions for using Composite ML-DSA algorithms within the Cryptographic Message Syntax (CMS).

### Clarification to Processing Key Usage Values During Certificate Revocation List (CRL) Validation
Draft: draft-ietf-lamps-keyusage-crl-validation · Working group: lamps
Agenda: c) draft-ietf-lamps-keyusage-crl-validation
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-keyusage-crl-validation/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
RFC 5280 (Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile) defines the profile of X.509 certificates and CRLs for use in the Internet. Section 4.2.1.3 of RFC 5280 requires CRL issuer certificates to contain the keyUsage extension with the cRLSign bit asserted. However, the CRL validation algorithm specified in Section 6.3 of RFC 5280 does not explicitly include a corresponding check for the presence of the keyUsage certificate extension. This document updates RFC 5280 to require that check.

### Media Access Control (MAC) Addresses in X.509 Certificates
Draft: draft-ietf-lamps-macaddress-on · Working group: lamps
Agenda: d) draft-ietf-lamps-macaddress-on
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-macaddress-on/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document defines a new GeneralName.otherName for inclusion in the X.509 Subject Alternative Name (SAN) and Issuer Alternative Name (IAN) extensions to carry an IEEE Media Access Control (MAC) address. The new name form makes it possible to bind a layer-2 interface identifier to a public key certificate. Additionally, this document defines how constraints on this name form can be encoded and processed in the X.509 Name Constraints extension (NCE).

### Use of Remote Attestation with Certification Signing Requests
Draft: draft-ietf-lamps-csr-attestation · Working group: lamps
Agenda: a) draft-ietf-lamps-csr-attestation (Mike)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-csr-attestation-00 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Certification Authorities (CAs) issuing certificates to Public Key Infrastructure (PKI) end entities may require a certificate signing request (CSR) to include additional verifiable information to confirm policy compliance. For example, a CA may require an end entity to demonstrate that the private key corresponding to a CSR's public key is secured by a hardware security module (HSM), is not exportable, etc. The process of generating, transmitting, and verifying additional information required by the CA is called remote attestation. While work is currently underway to standardize various aspects of remote attestation, a variety of proprietary mechanisms have been in use for years, particularly regarding protection of private keys. This specification defines ASN.1 structures which may carry attestation data for PKCS#10 and Certificate Request Message Format (CRMF) messages. Both standardized and proprietary attestation formats are supported by this specification.

### Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests
Draft: draft-ietf-lamps-attestation-freshness · Working group: lamps
Agenda: b) draft-ietf-lamps-attestation-freshness (Hannes, Hendrik)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
When an end entity includes attestation statements in a Certificate Signing Request (CSR), the freshness of the conveyed Evidence often needs to be established. A common mechanism is a nonce that is obtained from a Relying Party or Verifier and included by the Attester in the Evidence. This document specifies how an end entity requests such an attestation freshness nonce from an RA/CA when using certificate lifecycle management protocols. It defines message formats and protocol bindings for the conveyance of nonce request and response messages in the Certificate Management Protocol (CMP), Enrollment over Secure Transport (EST), and Certificate Management over CMS (CMC), including optional type-specific information needed to produce fresh Evidence for inclusion in a CSR.

### A Mechanism for X.509 Certificate Discovery
Draft: draft-ietf-lamps-certdiscovery · Working group: lamps
Agenda: c) draft-ietf-lamps-certdiscovery (Corey)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-certdiscovery/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-draft-ietf-lamps-certdiscovery-00 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document specifies a method to discover a referenced X.509 certificate associated with the current X.509 certificate. This enables efficient multi-certificate or fallback certificate handling in protocols. The objective is threefold: to enhance cryptographic agility, improve operational availability, and accommodate multi-key/ certificate usage. The proposed method aims to maximize compatibility with existing systems and is designed to be legacy- friendly, making it suitable for environments with a mix of legacy and new implementations. It includes mechanisms to provide a URI from which the referenced X.509 certificate can be retrieved as well as information about the target certificate's signature and public key algorithm, empowering relying parties to make informed decisions on whether to retrieve the Referenced Certificate, and a certificate hash to ensure that the correct certificate was retrieved.

### CAA Security Tag for Cryptographically-Constrained Domain Validation
Draft: draft-ietf-lamps-caa-security · Working group: lamps
Agenda: d) draft-ietf-lamps-caa-security (Henry)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-caa-security/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Cryptographic domain validation procedures leverage authenticated communication channels to ensure resilience against attacks by both on-path and off-path network adversaries which attempt to tamper with communications between the Certification Authority (CA) and the network resources related to the domain contained in the certificate. Domain owners can leverage "security" Property Tags specified in CAA records (defined in [RFC8659]) with the critical flag set, to ensure that CAs perform cryptographically-constrained domain validation during their issuance procedure, hence defending against global man- in-the-middle adversaries. This document defines the syntax of the CAA security Property as well as acceptable means for cryptographically-constrained domain validation procedures.

### Composite ML-KEM for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-kem · Working group: lamps
Agenda: e) draft-ietf-lamps-pq-composite-kem (Mike, John)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document defines combinations of US NIST ML-KEM in hybrid with traditional algorithms RSA-OAEP, ECDH, X25519, and X448. These combinations are tailored to meet security best practices and regulatory guidelines. Composite ML-KEM is applicable in any application that uses X.509 or PKIX data structures that accept ML- KEM, but where the operator wants extra protection against breaks or catastrophic bugs in ML-KEM.

### Composite ML-KEM for use in Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-composite-kem · Working group: lamps
Agenda: f) draft-ietf-lamps-cms-composite-kem (Daniel)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-kem/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Composite ML-KEM defines combinations of Module-Lattice-based Key Encapsulation Mechanism (ML-KEM) with RSA-OAEP, ECDH, X25519, and X448. This document specifies the conventions for using Composite ML-KEM algorithms with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in “Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)” (RFC 9629).

### Best Practices for Signed Attributes in CMS SignedData
Draft: draft-ietf-lamps-cms-euf-cma-signeddata · Working group: lamps
Agenda: g) draft-ietf-lamps-cms-euf-cma-signeddata (Daniel, Falko)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-euf-cma-signeddata/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-best-practices-for-signed-attributes-in-cms-signeddata-00 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
The Cryptographic Message Syntax (CMS) has different signature verification behaviour based on whether signed attributes are present or not. This results in a potential existential forgery vulnerability in CMS and protocols which use CMS. This document describes the vulnerability and lists mitigations and best practices to avoid it. This document updates RFC 5652 by prohibiting the use of the id-data content type for new uses of the CMS SignedData type.

### X.509 Certificate Extended Key Usage (EKU) for Attestation Keys
Draft: draft-jpfiset-lamps-attestationkey-eku · Working group: lamps
Agenda: a) draft-jpfiset-lamps-attestationkey-eku (J.-P., Mike, Hannes)
page: https://datatracker.ietf.org/doc/draft-jpfiset-lamps-attestationkey-eku/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
X.509 certificates ([RFC5280]) defines the Extended Key Usage (EKU) extension and specifies several key purpose identifiers (KeyPurposeIds) for use with that extension. This document defines a KeyPurposeId for the purpose of signing Evidence to provide remote attestation functions as defined in the RATS Architecture ([RFC9334]).

### One Signature Certificates
Draft: draft-santesson-one-signature-certs · Working group: lamps
Agenda: b) draft-santesson-one-signature-certs (Stefan) [ADOPTION CALL]
page: https://datatracker.ietf.org/doc/draft-santesson-one-signature-certs/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-one-signature-certificates-01 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
This document defines a profile for certificates that are issued for validation of the digital signature produced by a single signing operation. Each certificate is created at the time of signing and bound to the signed content. The associated signing key is generated, used to produce a single digital signature, and then immediately destroyed. The certificate never expires and is never revoked, which simplifies long-term validation.

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for FrodoKEM
Draft: draft-smyslov-lamps-frodokem-certificates · Working group: lamps
Agenda: c) draft-smyslov-lamps-frodokem-certificates (Valery)
page: https://datatracker.ietf.org/doc/draft-smyslov-lamps-frodokem-certificates/ | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
FrodoKEM is an unstructured lattice-based Key Encapsulation Mechanism (KEM). Compared to ML-KEM, FrodoKEM is considered as having more conservative design. This document specifies the conventions for using FrodoKEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Use of FrodoKEM in the Cryptographic Message Syntax
Draft: draft-chen-lamps-cms-frodokem · Working group: lamps
Agenda: d) draft-chen-lamps-cms-frodokem (Meiling)
page: https://datatracker.ietf.org/doc/draft-chen-lamps-cms-frodokem/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-frodokem-in-cms-00 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
FrodoKEM is a quantum-resistant key encapsulation mechanism (KEM) based on the standard Learning With Errors (LWE) problem，standardized by ISO. FrodoKEM offers multiple parameter sets, with the recommended sets for general use including (e)FrodoKEM-976-AES and (e)FrodoKEM-976-SHAKE for security level 3, and (e)FrodoKEM-1344-AES and (e)FrodoKEM-1344-SHAKE for security level 5. This document specifies the conventions for using FrodoKEM in the Cryptographic Message Syntax (CMS), using the KEMRecipientInfo structure defined in "Use of Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" [RFC9629].

### Attestation Key EKU
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-attestation-key-eku-01 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Algorithm Identifiers for FrodoKEM
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-algorithm-identifiers-for-frodokem-00 | video: https://youtu.be/RyqnmLpaRBw | materials: https://datatracker.ietf.org/meeting/125/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

## Working Group: lsr

### LSR-Status
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-01-lsr-status-01 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### Advertisement of Remote Interface Identifiers for Layer 2 Bundle Members
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-5-advertisement-of-remote-interface-identifiers-for-layer-2-bundle-members-00 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### LSR YANG Update
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-03-lsr-yang-update-00 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### flood reduction update measurements
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-flood-reduction-update-measurements-00 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### A Power Conserving Path Placement Strategy (PCPPS)
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-a-power-conserving-path-placement-strategy-pcpps-00 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### Advertising IGP Measurement Groups
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-advertising-igp-measurement-groups-00 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### IGP Extensions for Sub-interface Relationship Information
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-lsr-08-igp-extensions-for-sub-interface-relationship-information-01 | video: https://youtu.be/cgcJ2xdCAuU | materials: https://datatracker.ietf.org/meeting/125/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

## Working Group: masque

### Extensions to Compress and Derive Fields in HTTP Datagrams
Draft: draft-rosomakho-masque-connect-ip-optimizations · Working group: masque
Agenda: draft-rosomakho-masque-connect-ip-optimizations-01 by Yaroslav Rosomakho (30 minutes)
page: https://datatracker.ietf.org/doc/draft-rosomakho-masque-connect-ip-optimizations/ | video: https://youtu.be/snheAPwx2yw | materials: https://datatracker.ietf.org/meeting/125/session/masque
This document defines extensions for HTTP Datagram-based protocols that improve transmission efficiency by introducing templates for compressing or deriving datagram fields. These templates allow endpoints to define parts of datagrams that are static and can be removed, and other parts that can be derived (such as packet lengths and checksum values). Additionally, this document defines a checksum offload procedure enabling receivers to complete Internet checksums using sender- provided partial values. These optimisations reduce per-packet overhead, processing cost, and increase the effective maximum transmission unit (MTU) when datagrams are encapsulated in QUIC DATAGRAM frames.

### HTTP Datagram Compression
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-masque-http-datagram-compression-00 | video: https://youtu.be/snheAPwx2yw | materials: https://datatracker.ietf.org/meeting/125/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### The MASQUE Architecture
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-masque-the-masque-architecture-00 | video: https://youtu.be/snheAPwx2yw | materials: https://datatracker.ietf.org/meeting/125/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### ECN and DSCP support for HTTPS's Connect-UDP
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-masque-ecn-and-dscp-support-for-httpss-connect-udp-00 | video: https://youtu.be/snheAPwx2yw | materials: https://datatracker.ietf.org/meeting/125/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

## Working Group: oauth

### The OAuth 2.1 Authorization Framework
Draft: draft-ietf-oauth-v2-1 · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-identity-assertion-authorization-grant-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
The OAuth 2.1 authorization framework enables an application to obtain limited access to a protected resource, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and an authorization service, or by allowing the application to obtain access on its own behalf. This specification replaces and obsoletes the OAuth 2.0 Authorization Framework described in RFC 6749 and the Bearer Token Usage in RFC 6750.

### OAuth Client ID Metadata Document
Draft: draft-ietf-oauth-client-id-metadata-document · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-client-id-metadata-document-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This specification defines a mechanism through which an OAuth client can identify itself to authorization servers, without prior dynamic client registration or other existing registration. This is through the usage of a URL as a client_id in an OAuth flow, where the URL refers to a document containing the necessary client metadata, enabling the authorization server to fetch the metadata about the client as needed.

### OAuth 2.0 for First-Party Applications
Draft: draft-ietf-oauth-first-party-apps · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-first-party-apps/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-first-party-apps/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-for-first-party-apps-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This document defines the Authorization Challenge Endpoint, which supports clients that want to control the process of obtaining authorization from the user using a native experience. In many cases, this can provide an entirely browserless OAuth 2.0 experience suited for native applications, only delegating to the browser in unexpected, high-risk, or error conditions.

### Identity Assertion JWT Authorization Grant
Draft: draft-ietf-oauth-identity-assertion-authz-grant · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/ | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This specification provides a mechanism for an application to use an identity assertion to obtain an access token for a third-party API by coordinating through an identity provider that the downstream Resource Authorization Server already trusts for single sign-on (SSO), using OAuth 2.0 Token Exchange (RFC 8693) and the JWT Profile for OAuth 2.0 Authorization Grants (RFC 7523). This pattern is informally referred to as Cross-App Access (XAA).

### Updates to OAuth 2.0 Security Best Current Practice
Draft: draft-ietf-oauth-security-topics-update · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-security-topics-update/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-security-topics-update/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-updates-to-oauth-20-security-best-current-practice-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This document updates the set of best current security practices for OAuth 2.0 by extending the security advice given in RFC 6749, RFC 6750, and RFC 9700, to cover new threats that have been discovered since the former documents have been published.

### OAuth SPIFFE Client Authentication
Draft: draft-schwenkschuster-oauth-spiffe-client-auth · Working group: oauth
Agenda: https://www.ietf.org/archive/id/draft-schwenkschuster-oauth-spiffe-client-auth-00.html
page: https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-spiffe-client-authentication-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This specification profiles the Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants [RFC7521] and JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants [RFC7523] to enable the use of SPIFFE Verifiable Identity Documents (SVIDs) as client credentials in OAuth 2.0. It defines how OAuth clients with SPIFFE credentials can authenticate to OAuth authorization servers using their JWT-SVIDs or X.509-SVIDs without the need for client secrets. This approach enhances security by enabling seamless integration between SPIFFE-enabled workloads and OAuth authorization servers while eliminating the need to distribute and manage shared secrets such as static client secrets.

### OAuth 2.0 RAR Metadata and Error Remediation
Draft: draft-zehavi-oauth-rar-metadata · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-zehavi-oauth-rar-metadata/
page: https://datatracker.ietf.org/doc/draft-zehavi-oauth-rar-metadata/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-rar-metadata-and-error-signaling-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
OAuth 2.0 Rich Authorization Requests (RAR) [RFC9396] standardizes the exchange and processing of authorization details but does not define metadata for describing authorization details types. In addition, no interoperable guidance is offered to clients, to remediate failures by resource servers due to insufficient authorization details. This document addresses this interoperability challenge, allowing clients to dynamically discover metadata instead of relying on out- of-band agreements, as well as standardizes failure signaling including interoperable remediation when insufficient authorization details are the cause of failure.

### OAuth 2.0 direct interaction for native clients using federation
Draft: draft-zehavi-oauth-native-clients-federation · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-zehavi-oauth-native-clients-federation/
page: https://datatracker.ietf.org/doc/draft-zehavi-oauth-native-clients-federation/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-20-for-native-clients-with-federation-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
OAuth 2.0 for First-Party Applications (FiPA) [I-D.ietf-oauth-first-party-apps] defined a native OAuth 2.0 *direct interaction*, whereby clients call authorization server's _Native Authorization Endpoint_ as an HTTP REST API, whose response instructs client what information to collect from end-user to satisfy authorization server's policies and requirements. While FiPA [I-D.ietf-oauth-first-party-apps] focused on a one-to-one relationship between client and authorization server, this document is an *extension profile* adding support for authorization servers to federate the interaction to a downstream authorization server, instruct collection of additional information from users to guide request routing or instruct the usage of another native app for user interaction.

### Additional Hash Algorithms for OAuth 2.0 PKCE and Proof-of-Possession
Draft: draft-skokan-oauth-additional-hashes · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-skokan-oauth-additional-hashes/
page: https://datatracker.ietf.org/doc/draft-skokan-oauth-additional-hashes/ | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This document defines SHA-512 as an additional hash algorithm for OAuth 2.0 Proof Key for Code Exchange (PKCE), mutual-TLS certificate- bound access tokens, and Demonstrating Proof of Possession (DPoP), for use in deployments operating under security policies that prohibit the use of SHA-256, which is otherwise mandated or the only option in these mechanisms.

### OAuth2.0 Extension for Multi-AI Agent Collaboration
Draft: draft-song-oauth-ai-agent-collaborate-authz · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-song-oauth-ai-agent-collaborate-authz/
page: https://datatracker.ietf.org/doc/draft-song-oauth-ai-agent-collaborate-authz/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth20-extension-for-multi-ai-agent-collaboration-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This method extends OAuth 2.0 by adding fields to token and message flows, enabling sub-agents to act as a task group. It simplifies authorization for task groups, avoids repeated interactions between sub-agents and the authorization server, and bounds the authority delegated to the group and to each member while maintaining compatibility with existing OAuth 2.0 workflows.

### Agent-to-Agent (A2A) Profile for OAuth Transaction Tokens
Draft: draft-liu-oauth-a2a-profile · Working group: oauth
Agenda: https://www.ietf.org/archive/id/draft-liu-oauth-a2a-profile-00.html
page: https://datatracker.ietf.org/doc/draft-liu-oauth-a2a-profile/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-a2a-profile-for-oauth-transaction-tokens-02 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This document defines a profile for using OAuth Transaction Tokens in Agent-to-Agent (A2A) communication scenarios. The profile specifies how A2A call chain context can be embedded within Transaction Tokens to maintain agent identity, authorization context, and execution flow across distributed agent workloads within trusted domains.

### Agent Operation Authorization
Draft: draft-liu-agent-operation-authorization · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/html/draft-liu-agent-operation-authorization-01
page: https://datatracker.ietf.org/doc/draft-liu-agent-operation-authorization/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-agent-operation-authorization-02 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This document specifies the Agent Operation Authorization framework — a structured mechanism that enables verifiable delegation of actions from human principals to autonomous AI agents with fine-grained agent operation authorization. The framework introduces two distinct phases: * Agent Operation Authorization Request: A structured proposal of operations converted to a JSON Web Token (JWT) without including the user's original natural language input. * Agent Operation Authorization Token: A JSON Web Token representing confirmed authorization for a specific agent operation, enforceable at runtime by agents and verifiers. It cryptographically verifies user intent, prevents unauthorized or hallucinated actions, and ensures auditable traceability of each authorized operation.

### Policy, Lifecycle, and Intent Extensions for OAuth Rich Authorization Requests
Draft: draft-chen-oauth-rar-agent-extensions · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-chen-oauth-rar-agent-extensions/
page: https://datatracker.ietf.org/doc/draft-chen-oauth-rar-agent-extensions/ | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
OAuth 2.0 Rich Authorization Requests (RAR) [RFC9396] defines a syntax for clients to request fine-grained permissions. While powerful, this mechanism lacks standardized methods for clients to express three critical contextual dimensions prevalent in modern automated systems: the high-level user intent driving the request, the required security policy under which the request should be evaluated, and the binding of the authorization's lifecycle to an external process. This document extends the RAR framework to address these gaps. It first defines a new authorization_details type, *intent_request*, to facilitate goal-oriented authorization. Second, it introduces two new parameters for the authorization_details object: *policy_context*, to request authorization under a specific assurance level, and *lifecycle_binding*, to tie the validity of the authorization grant to the state of an external entity. These extensions enable authorization servers to make more intelligent, secure, and context-aware decisions, particularly in ecosystems involving autonomous agents and complex, long-running tasks.

### Structured and Constraint Extensions for OAuth Scopes
Draft: draft-chen-oauth-scope-agent-extensions · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-chen-oauth-scope-agent-extensions/
page: https://datatracker.ietf.org/doc/draft-chen-oauth-scope-agent-extensions/ | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This specification defines an extension to the OAuth 2.0 scope parameter, as specified in RFC 6749, which is used to express the permissions granted to an access token. The proposed extension introduces a structured syntax for scope values to enable fine- grained authorization for the installation and execution of Modular Capability Units (encapsulated and reusable functional modules such as skills) within Agent ecosystems. However, current mechanisms for authorizing such modules generally lack a standardized way to express and obtain consent for the complex, fine-grained permissions they require during installation. This document addresses this limitation by defining a structured format for the scope parameter. The format extends the simple space- delimited strings with a colon-separated syntax: [resource_type]:[action]:[target][:constraints]. This syntax allows for the precise description of permissions for operations such as file system access, command-line execution, network access, tool invocation, and scheduled tasks. These extensions provide a standardized, machine-readable way to request, convey, and validate detailed permissions, thereby enhancing users' security control over their resources while maintaining compatibility with the existing OAuth token issuance and validation flows.

### OAuth 2.0 Scope Aggregation for Multi-Step AI Agent Workflows
Draft: draft-jia-oauth-scope-aggregation · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-jia-oauth-scope-aggregation/
page: https://datatracker.ietf.org/doc/draft-jia-oauth-scope-aggregation/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-20-scope-aggregation-for-multi-step-ai-agent-workflows-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
This document describes a scope-aggregated OAuth 2.0 authorization pattern for multi-step AI agent workflows. An AI agent aggregates the scopes required across a workflow and only initiates a single authorization procedure for the aggregated scope. This reduces repeated user consents and multiple authorization round-trips, improving authorization efficiency.

### OAuth 2.1
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-21-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Additional Hash Algorithms for OAuth 2.0
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-additional-hash-algorithms-for-oauth-20-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### OAuth RAR and Scope Extensions
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-rar-and-scope-extensions-00 | video: https://youtu.be/C72Saxe03tk | materials: https://datatracker.ietf.org/meeting/125/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

## Working Group: quic

### Media over QUIC Transport (MOQT) over QMux
Draft: draft-nandakumar-moq-qmux-moqt · Working group: quic
Agenda: 5 min - Media over QUIC Transport over QMux https://datatracker.ietf.org/doc/draft-nandakumar-moq-qmux-moqt/ slides
page: https://datatracker.ietf.org/doc/draft-nandakumar-moq-qmux-moqt/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-quic-moqt-over-qmux-01 | video: https://youtu.be/ITeRnPrkUvk | materials: https://datatracker.ietf.org/meeting/125/session/quic
This document specifies how Media over QUIC Transport (MOQT) can operate over QMux, enabling MOQT applications to function over reliable byte-oriented streams such as TCP with TLS. By utilizing QMux as an intermediate layer, MOQT deployments gain the ability to fall back to TCP-based transport when UDP is blocked or unreliable, while maintaining API compatibility with QUIC-native implementations. This document analyzes the benefits and trade-offs of this approach and provides implementation guidance for deploying MOQT over QMux.

### Minimum RTT Estimation Under Low ACK Frequency
Draft: draft-li-quic-minimum-rtt-estimation · Working group: quic
Agenda: 10 min - Minimum RTT estimation draft-li-quic-minimum-rtt-estimation slides
page: https://datatracker.ietf.org/doc/draft-li-quic-minimum-rtt-estimation/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-quic-calibrating-minimum-rtt-under-low-ack-frequency-00 | video: https://youtu.be/ITeRnPrkUvk | materials: https://datatracker.ietf.org/meeting/125/session/quic
In traditional acknowledgment mechanisms, the sender frequently "pulls" ACK packets, resulting in significant protocol control overhead. This leads to wasted CPU and I/O resources, contention for packet spectrum on half-duplex links (e.g., WLAN), and reverse-path congestion in asymmetric links (e.g., satellite network). Reducing the number of ACKs is essential in scenarios where ACK overhead is non-negligible. However, a lower ACK frequency can introduce biases in delay estimation, such as overestimating the minimum round-trip time (minRTT). This document proposes how to calibrate the estimation of the minRTT under low ACK frequency conditions.

### Application of Explicit Measurement Techniques for QUIC Troubleshooting
Draft: draft-mdt-quic-explicit-measurements · Working group: quic
Agenda: 10 min - SCONE-inspired measurement bits draft-mdt-quic-explicit-measurements slides
page: https://datatracker.ietf.org/doc/draft-mdt-quic-explicit-measurements/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-quic-application-of-explicit-measurement-techniques-for-quic-troubleshooting-00 | video: https://youtu.be/ITeRnPrkUvk | materials: https://datatracker.ietf.org/meeting/125/session/quic
This document defines a protocol that can be used by QUIC endpoints to signal packet loss in a way that can be used by network devices to measure and locate the source of the loss. Discussion of this work is encouraged to happen on the QUIC IETF mailing list quic@ietf.org (mailto:quic@ietf.org) or on the GitHub repository which contains the draft: https://github.com/igorlord/ draft-mdt-quic-explicit-measurements (https://github.com/igorlord/ draft-mdt-quic-explicit-measurements).

### QMux
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-quic-qmux-00 | video: https://youtu.be/ITeRnPrkUvk | materials: https://datatracker.ietf.org/meeting/125/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

## Working Group: rats

### Concise Selector for Endorsements and Reference Values
Draft: draft-ietf-rats-coserv · Working group: rats
Agenda: (15 min) Paul Howard - draft-ietf-rats-coserv
page: https://datatracker.ietf.org/doc/draft-ietf-rats-coserv/ | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
In the Remote Attestation Procedures (RATS) architecture, Verifiers require Endorsements and Reference Values to assess the trustworthiness of Attesters. This document specifies the Concise Selector for Endorsements and Reference Values (CoSERV), a structured query/result format designed to facilitate the discovery and retrieval of these artifacts from various providers. CoSERV defines a query language and corresponding result structure using CDDL, which can be serialized in CBOR format, enabling efficient interoperability across diverse systems.

### Concise Reference Integrity Manifest
Draft: draft-ietf-rats-corim · Working group: rats
Agenda: (15 min) Yogesh Deshpande - draft-ietf-rats-corim
page: https://datatracker.ietf.org/doc/draft-ietf-rats-corim/ | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Remote Attestation Procedures (RATS) enable Relying Parties to assess the trustworthiness of a remote Attester and therefore to decide whether or not to engage in secure interactions with it. Evidence about trustworthiness can be rather complex and it is deemed unrealistic that every Relying Party is capable of the appraisal of Evidence. Therefore that burden is typically offloaded to a Verifier. In order to conduct Evidence appraisal, a Verifier requires not only fresh Evidence from an Attester, but also trusted Endorsements and Reference Values from Endorsers and Reference Value Providers, such as manufacturers, distributors, or device owners. This document specifies the information elements for representing Endorsements and Reference Values in CBOR format.

### Evidence Encoding for Hardware Security Modules
Draft: draft-ietf-rats-pkix-key-attestation · Working group: rats
Agenda: (10 min) Jean-Pierre Fiset - draft-ietf-rats-pkix-key-attestation
page: https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/ | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
This document specifies a vendor-agnostic format for Evidence produced and verified within a PKIX context. The Evidence produced this way includes claims collected about a cryptographic module, such as a Hardware Security Module (HSM), and elements found within it such as cryptographic keys. One scenario envisaged is that the state information about the cryptographic module can be securely presented to a remote operator or auditor in a vendor-agnostic verifiable format. A more complex scenario would be to submit this Evidence to a Certification Authority to aid in determining whether the storage properties of this key meet the requirements of a given certificate profile.

### Epoch Markers
Draft: draft-ietf-rats-epoch-markers · Working group: rats
Agenda: (15 min) Henk Birkholz - draft-ietf-rats-epoch-markers
page: https://datatracker.ietf.org/doc/draft-ietf-rats-epoch-markers/ | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
This document defines Epoch Markers as a means to establish a notion of freshness among actors in a distributed system. Epoch Markers are similar to "time ticks" and are produced and distributed by a dedicated system known as the Epoch Bell. Systems receiving Epoch Markers do not need to track freshness using their own understanding of time (e.g., via a local real-time clock). Instead, the reception of a specific Epoch Marker establishes a new epoch that is shared among all recipients. This document defines Epoch Marker types, including CBOR time tags, RFC 3161 TimeStampToken, and nonce-like structures. It also defines a CWT Claim to embed Epoch Markers in RFC 8392 CBOR Web Tokens, which serve as vehicles for signed protocol messages. Finally, it registers RATS Conceptual Message Wrapper (CMW) Indicators for Epoch ID and Nonce.

### Remote Attestation with Multiple Verifiers
Draft: draft-deshpande-rats-multi-verifier · Working group: rats
Agenda: (10+5 min) Jun Zhang - draft-deshpande-rats-multi-verifier
page: https://datatracker.ietf.org/doc/draft-deshpande-rats-multi-verifier/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-remote-attestation-with-multiple-verifiers-00 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
IETF RATS Architecture, defines the key role of a Verifier. In a complex system, this role needs to be performed by multiple Verfiers coordinating together to assess the full trustworthiness of an Attester. This document focuses on various topological patterns for a multiple Verifier system. It only covers the architectural aspects introduced by the Multi Verifier concept, which is neutral with regard to specific wire formats, encoding, transport mechanisms, or processing details.

### Privacy Preserving Verifiable Geofencing with Residency Proofs for Sovereign Workloads
Draft: draft-lkspa-wimse-verifiable-geo-fence · Working group: rats
Agenda: (15 min) Diego Lopez - draft-lkspa-wimse-verifiable-geo-fence
page: https://datatracker.ietf.org/doc/draft-lkspa-wimse-verifiable-geo-fence/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-privacy-preserving-verifiable-geofencing-with-residency-proofs-for-sovereign-workloads-00 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Modern cloud and distributed computing rely heavily on software-only identities and bearer tokens that are easily stolen, replayed, or used from unauthorized locations. Furthermore, traditional methods of location verification - such as IP-address-based geolocation - are easily spoofed via VPNs or proxies and significantly compromise infrastructure security and privacy for *Sovereign Workloads* and high-assurance environments. This document defines a *High-Assurance Profile* designed to solve these challenges through hardware-rooted cryptographic verifiability. A host machine runs a workload identity agent for managing the workload identities on that platform. This proposal replaces implicit trust and spoofable indicators with cryptographically verifiable hardware-rooted evidence of integrity and location for this agent. Critically, this framework prioritizes *Location Privacy* by utilizing Zero-Knowledge Proofs (ZKP), allowing a workload to prove it is within a compliant "Sovereign Zone" without disclosing precise coordinates that could be used for tracking or exploitation. By binding software identities to persistent silicon identities and verified physical residency, this solution establishes a "Silicon-to- Workload" chain of trust. It ensures that sensitive operations are only performed by authorized workloads running on untampered hardware in cryptographically verified, privacy-preserving geographic boundaries, fulfilling the high-assurance requirements of the *WIMSE Architecture* [[I-D.ietf-wimse-architecture]].

### Proof of Process (PoP): Architecture and Evidence Format
Draft: draft-condrey-rats-pop-protocol · Working group: rats
Agenda: (15 min) David Condry - draft-condrey-rats-pop-protocol
page: https://datatracker.ietf.org/doc/draft-condrey-rats-pop-protocol/ | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
This document specifies the Proof of Process (PoP) Evidence Framework, a specialized profile of Remote Attestation Procedures (RATS) designed to validate the provenance of effort in digital authorship. Unlike traditional provenance, which tracks file custody, PoP attests to the continuous physical process of creation. The protocol defines a cryptographic mechanism for generating Evidence Packets utilizing a composite Sequential Work Function (SWF) based on Proof of Biological Space-Time (PoBST) to enforce temporal monotonicity and Cross-Domain Constraint Entanglement (CDCE) to bind behavioral entropy (human jitter) and physical state to the document. Technical specifications for wire formats, sequential work functions, and hardware-anchored trust are provided.

### CoSERV Progress Update
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-coserv-progress-update-00 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### CoRIM
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-corim-00 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Evidence Encoding for HSMs
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-evidence-encoding-for-hsms-01 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Reference Interaction Model & Epoch Marker
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-reference-interaction-model-epoch-marker-00 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Secure Wasm App Provisioning with VERAISON: Design Insights
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rats-secure-wasm-app-provisioning-with-veraison-design-insights-00 | video: https://youtu.be/uNLHwnJRSCI | materials: https://datatracker.ietf.org/meeting/125/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

## Working Group: rift

### Bidirectional Forwarding Detection (BFD) for Routing in Fat Trees (RIFT)
Draft: draft-zhou-rift-bfd · Working group: rift
Agenda: - https://www.ietf.org/archive/id/draft-zhou-rift-bfd-00.txt
page: https://datatracker.ietf.org/doc/draft-zhou-rift-bfd/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rift-bidirectional-forwarding-detection-bfd-for-routing-in-fat-trees-rift-00 | video: https://youtu.be/6OZQK4oz48c | materials: https://datatracker.ietf.org/meeting/125/session/rift
This document specifies the use of Bidirectional Forwarding Detection (BFD) for fast failure detection of Routing in Fat Trees (RIFT) adjacencies. RIFT is specified in RFC 9692. While RFC 9692 describes interactions with BFD, it does not define normative behavior. This document specifies the use of single-hop BFD, as defined in RFC 5881, for RIFT adjacencies, including behavior for parallel links and multiple RIFT instances.

### rift-df-topo
Presentation · Working group: rift
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rift-rift-df-topo-00 | video: https://youtu.be/6OZQK4oz48c | materials: https://datatracker.ietf.org/meeting/125/session/rift
Slides presented at the rift session; no Internet-Draft is linked to them.

## Working Group: rtgwg

### A YANG Data Model for Quality of Service (QoS) in IP Networks
Draft: draft-ietf-rtgwg-qos-model · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-qos-model/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-qos-model/ | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
This document describes a YANG data model for management of Quality of Service (QoS) in IP networks.

### Fast Network Notifications Problem Statement
Draft: draft-ietf-rtgwg-net-notif-ps · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-rtgwg-net-notif-ps-00
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-net-notif-ps/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-03-fast-network-notifications-problem-statement-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
Many network applications, ranging from Artificial Intelligence (AI) /Machine Learning (ML) training or inference to cloud services, require high bandwidth, low delay, low jitter and minimal packet loss in data transfer, which requires that the networks can be adaptive in the presence of faults, degradations, or congestion. However, existing traffic management mechanisms often face limitations in responsiveness, coverage, and operational complexity, particularly in high-speed and large-scale network environments. A good and timely understanding of network operational status can help to enable faster response to critical events, so as to enable the selection of paths with reduced latency and improve network utilization. This document describes the existing problems and the need for fast network notification.

### IP Fast Reroute for AI/ML Fabrics
Draft: draft-clad-rtgwg-ipfrr-aiml · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-clad-rtgwg-ipfrr-aiml/
page: https://datatracker.ietf.org/doc/draft-clad-rtgwg-ipfrr-aiml/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-07-ip-fast-reroute-for-aiml-fabrics-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
This document describes the requirements and mechanisms for achieving sub-100 microsecond convergence in Artificial Intelligence (AI) Data Center (DC) fabrics and Data Center Interconnect (DCI) environments. It explores the limitations of current IP Fast Reroute (RFC 5714) capabilities, such as ECMP, LFA, and TI-LFA, particularly in the context of large-scale, multi-tier Clos topologies and BGP-only fabrics. The draft highlights the requirements for hardware- accelerated network notification mechanisms and congestion-aware remote protection strategies to address the stringent performance demands of AI workloads.

### Efficient Remote Protection
Draft: draft-clad-rtgwg-efficient-remote-protection · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-clad-rtgwg-efficient-remote-protection/
page: https://datatracker.ietf.org/doc/draft-clad-rtgwg-efficient-remote-protection/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-05-efficient-remote-protection-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
This document specifies Efficient Remote Protection (ERP), a mechanism for IP Fast Reroute (IP-FRR) that utilizes network notifications to activate pre-computed backup paths at nodes multiple hops upstream of a failure. ERP addresses scenarios where local protection mechanisms, such as Loop-Free Alternates (LFA) or Topology-Independent LFA (TI-LFA), result in suboptimal paths, specifically traffic hairpinning. By activating protection at strategically selected upstream nodes rather than at the node immediately adjacent to the failure, ERP preserves routing optimality and prevents bandwidth waste. ERP applies to both complete link/node failures and performance degradations such as congestion or reduced link capacity. This makes ERP particularly beneficial in networks with high link utilization, such as AI data centers and Data Center Interconnect (DCI) networks.

### Fully Adaptive Routing Ethernet in Scale-Up Networks
Draft: draft-xu-rtgwg-fare-in-sun · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-xu-rtgwg-fare-in-sun/
page: https://datatracker.ietf.org/doc/draft-xu-rtgwg-fare-in-sun/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-06-xu-fare-in-sun-01 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
The Mixture of Experts (MoE) has become a dominant paradigm in transformer-based artificial intelligence (AI) large language models (LLMs). It is widely adopted in both distributed training and distributed inference. To enable efficient expert parallelization and even tensor parallelization across dozens or even hundreds of Graphics Processing Units (GPUs) in MoE architectures, an ultra-high- throughput, ultra-low-latency AI scale-up network (SUN) is critical. This document describes how to extend the Weighted Equal-Cost Multi- Path (WECMP) load-balancing mechanism, referred to as Fully Adaptive Routing Ethernet (FARE), which was originally designed for scale-out networks, to scale-up networks.

### Use cases and Requirement for Flow Control Collaboration Across DCNs and WAN
Draft: draft-han-rtgwg-codeployment-pfc-fgfc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-han-rtgwg-codeployment-pfc-fgfc/
page: https://datatracker.ietf.org/doc/draft-han-rtgwg-codeployment-pfc-fgfc/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-07-use-cases-and-requirement-for-flow-control-collaboration-across-dcns-and-wan-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
The demand for lossless network transmission and the application of flow control mechanisms have expanded from DCNs (Data Center Networks) to WANs(Wide Area Networks). To mitigate PFC - related issues in WANs, the fine - grained flow control is proposed. This mechanism aims to achieve precise control at flow / tenant levels, limits flow control to specified paths and slices, and provides intelligent congestion backpressure. As current DCN already adopts PFC mechanisms, the fine-grained flow control in WANs needs to work with PFC in DCNs to achieve end-to-end flow control. This document describes the use cases and requirements for the collaboration of flow control mechanisms across DCNs and WANs.

### Multicast Use Cases for Large Language Model Synchronization
Draft: draft-liu-rtgwg-llmsync-multicast · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-liu-rtgwg-llmsync-multicast/
page: https://datatracker.ietf.org/doc/draft-liu-rtgwg-llmsync-multicast/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-multicast-use-cases-for-large-language-model-synchronization-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
Large Language Models (LLMs) deployments are becoming increasingly widespread, with inference services being the most common application. This draft will discuss multicast use cases for inference cloud services.

### Requirements and Gap Analysis of Multicast in AI Data Centers
Draft: draft-zhang-rtgwg-multicast-requirements-gaps-aidc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-zhang-rtgwg-multicast-requirements-gaps-aidc/
page: https://datatracker.ietf.org/doc/draft-zhang-rtgwg-multicast-requirements-gaps-aidc/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-09-requirements-and-gap-analysis-of-multicast-in-ai-data-centers-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
Multicast has the potential to be applied in Artificial Intelligence Data Centers (AIDCs) to improve the efficiency of point-to-multipoint data transmission during large language model training and inference. This document identifies key requirements of multicast in AIDCs, and analyzes the gaps between these requirements and the capabilities of existing multicast technologies.

### Symmetry-Driven Asynchronous Forwarding with Fast Reroute for LEO Satellite Networks (SDAF)
Draft: draft-luan-rtgwg-sdaf · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-luan-rtgwg-sdaf/
page: https://datatracker.ietf.org/doc/draft-luan-rtgwg-sdaf/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-symmetry-driven-asynchronous-forwarding-with-fast-reroute-for-leo-satellite-networks-sdaf-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
Interior Gateway Protocols (IGPs) such as OSPF are commonly employed in satellite networks to address topology awareness and autonomous routing in response to link interruptions, link/node failures, and subsequent repairs. However, IGP-based approaches suffer from inherent limitations. Synchronization delays between the control plane and the forwarding plane can cause routing black holes, while asynchronous convergence across nodes may induce micro-loops (as described in prior work), leading to packet loss and congestion. These issues are particularly exacerbated in satellite networks characterized by highly dynamic topologies, long inter-satellite propagation delays, and constrained on-board computing resources. This document describes the Symmetry-Driven Asynchronous Forwarding (SDAF) mechanism, which leverages the intrinsic symmetry of toroidal topologies in satellite networks. Low Earth Orbit (LEO) satellite constellations are typically composed of multiple circular orbital planes, forming a toroidal topology by inter-satellite links. SDAF autonomously triggers and processes reverse flows based solely on local link-state information, without requiring control-plane convergence, protocol extensions, or packet header modifications. SDAF is fully compatible with existing protocols and technologies such as OSPFv3, IS-IS, and MPLS, and is specifically tailored to the resource-constrained nature of satellite systems. It achieves microsecond-scale convergence and low packet loss under failure conditions. Simulation results and tests conducted on actual satellite routers demonstrate that the SDAF mechanism significantly suppresses packet loss caused by routing black holes and micro-loops, while also alleviating link congestion and packet reordering issues.

### Congestion Control Based on SRv6 Path
Draft: draft-liu-rtgwg-srv6-cc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-liu-rtgwg-srv6-cc/01/
page: https://datatracker.ietf.org/doc/draft-liu-rtgwg-srv6-cc/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-congestion-control-based-on-srv6-path-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
This document describes a congestion control solution based on SRv6. It defines mechanisms for congestion notification and flow control within an SRv6-based network, optimizing congestion handling through hierarchical congestion control messages along SRv6 paths.

### QoS YANG
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-02-qos-yang-00 | video: https://youtu.be/nzitn4M1Tc8 | materials: https://datatracker.ietf.org/meeting/125/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

## Working Group: savnet

### Problem Statement, Gap Analysis, and Requirements for Inter-Domain Source Address Validation
Draft: draft-ietf-savnet-inter-domain-problem-statement · Working group: savnet
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-intra-domain-savnet-problem-statement-00 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
This document analyzes the problem space and provides a gap analysis of existing inter-domain source address validation (SAV) mechanisms. Based on these findings, it outlines the technical requirements for future improvements.

### Considerations on Authoritative Information for Source Address Validation
Draft: draft-qin-savnet-authoritative-information · Working group: savnet
Agenda: Draft: https://datatracker.ietf.org/doc/draft-qin-savnet-authoritative-information/
page: https://datatracker.ietf.org/doc/draft-qin-savnet-authoritative-information/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-considerations-on-authoritative-information-for-source-address-validation-01 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
Source Address Validation (SAV) prevents source address spoofing. This document explains that SAVNET relies on authoritative information. It also describes how to handle missing or conflicting data. The guidance minimizes improper blocks and improper permits while supporting reliable SAV enforcement.

### A Profile for Traffic Origin Authorizations (TOAs)
Draft: draft-qin-savnet-toa · Working group: savnet
Agenda: Draft: https://datatracker.ietf.org/doc/draft-qin-savnet-toa/
page: https://datatracker.ietf.org/doc/draft-qin-savnet-toa/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-traffic-origin-authorizations-toas-01 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
This document defines a standard profile for Traffic Origin Authorizations (TOAs), a Cryptographic Message Syntax (CMS) protected content type for use with the Resource Public Key Infrastructure (RPKI). A TOA is a digitally signed object that provides a means of verifying that an IP address block holder has authorized an Autonomous System (AS) to originate traffic using source IP addresses within the address block.

### Problem Statement, Gap Analysis, and Requirements for Intra-domain Source Address Validation
Draft: draft-ietf-savnet-intra-domain-problem-statement · Working group: savnet
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-problem-statement/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-the-updates-on-the-gap-analysis-problem-statement-and-requirements-for-inter-domain-sav-00 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
Source address validation (SAV) is an important means to mitigate IP source address spoofing [RFC2827]. This document analyzes the gaps in current operational mechanisms for intra-domain SAV. It also identifies the properties that new intra-domain SAV mechanisms are expected to provide.

### Source Address Validation Deployment Status
Draft: draft-wang-sav-deployment-status · Working group: savnet
Agenda: Draft: https://datatracker.ietf.org/doc/draft-wang-sav-deployment-status/
page: https://datatracker.ietf.org/doc/draft-wang-sav-deployment-status/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-source-address-validation-deployment-status-00 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
This document provides a summary of methods for measuring the deployment status of source address validation, with an overview of its deployment status. It reviews various methods for measuring outbound and/or inbound source address validation, including established tools like CAIDA Spoofer, as well as recently proposed remote measurement methods. By combining results from these different methods, the document offers a comprehensive overview of the status of source address validation deployment across the Internet.

### Analysis of TOA vs. ROA for Prefixes Not Announced in BGP but Used for Source Addresses
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-analysis-of-toa-vs-roa-for-prefixes-not-announced-in-bgp-but-used-for-source-addresses-00 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Traffic Origin Authorization
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-savnet-traffic-origin-authorization-00 | video: https://youtu.be/PcewC9NYpXk | materials: https://datatracker.ietf.org/meeting/125/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

## Working Group: spice

### Selective Disclosure CBOR Web Tokens (SD-CWT)
Draft: draft-ietf-spice-sd-cwt · Working group: spice
Agenda: "SPICE SD-CWT" draft-ietf-spice-sd-cwt 15+10 min (Rohan Mahy/Henk Birkholz) - 10 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spice-update-on-sd-cwt-00 | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
This specification describes a data minimization technique for use with CBOR Web Tokens (CWTs). The approach is inspired by the Selective Disclosure JSON Web Token (SD-JWT), with changes to align with CBOR Object Signing and Encryption (COSE) and CWTs.

### A reference architecture for direct presentation credential flows
Draft: draft-johansson-direct-presentation-arch · Working group: spice
Agenda: Call for adoption: "A reference architecture for direct presentation credential flows' draft-johansson-direct-presentation-arch (Brent Zundel) - 10 min
page: https://datatracker.ietf.org/doc/draft-johansson-direct-presentation-arch/ | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
This document defines a reference architecture for direct presentation flows of digital credentials. The architecture introduces the concept of a presentation mediator as the active component responsible for managing, presenting, and selectively disclosing credentials while preserving a set of security and privacy promises that will also be defined. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/leifj/wallet-refarch.

### Traceability Claims
Draft: draft-prorock-spice-cwt-traceability-claims · Working group: spice
Agenda: Call for adoption: "Traceability Claims" draft-prorock-spice-cwt-traceability-claims (Mike Jones) - 5 min
page: https://datatracker.ietf.org/doc/draft-prorock-spice-cwt-traceability-claims/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spice-traceability-claims-00 | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
This document defines claims to support traceability of physical goods across supply chains, focusing on items such as bills of lading, transport modes, and container manifests. These claims standardize the encoding of essential logistics and transport metadata, facilitating enhanced transparency and accountability in global supply chains. These claims are registered for use in both CBOR Web Tokens (CWTs) and JSON Web Tokens (JWTs).

### A Public Key Service Provider for Verification in Multiple Issuers and Verifiers
Draft: draft-wang-spice-public-key-service-provider · Working group: spice
Agenda: "A Public Key Service Provider for Verification in Multiple Issuers and Verifiers” https://datatracker.ietf.org/doc/draft-wang-spice-public-key-service-provider - Yuning Jiang - 10 min
page: https://datatracker.ietf.org/doc/draft-wang-spice-public-key-service-provider/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spice-a-public-key-service-provider-for-verification-in-multiple-issuers-and-verifiers-00 | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
SPICE provides a selective disclosure mechanism of credentials from issuer. However, future network services may be built on the trust between multiple entities. Obtaining the public key of multiple issuers for a verifer from potential multiple sources can be complex. In this contribution, an optional public key service is proposed in SPICE architecture for the issue of obtaining the public keys of the issuers from multiple trusted entities. The basic function of public key service is proposed including public key registration, token verification, and a potential implementation such as the distributed ledger. We hope that the proposed contribution can be used as infomative for SPICE regarding to the token validation procedure.

### Cryptographically Verifiable Actor Chains for OAuth 2.0 Token Exchange
Draft: draft-mw-spice-actor-chain · Working group: spice
Agenda: "Cryptographically Verifiable Actor Chain for OAuth 2.0 Token Exchange," https://datatracker.ietf.org/doc/draft-mw-spice-actor-chain/ - Ramki Krishnan- 10 min
page: https://datatracker.ietf.org/doc/draft-mw-spice-actor-chain/ | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
Multi-hop service-to-service and agentic workflows need a standardized way to preserve and validate delegation-path continuity across successive token exchanges. This document defines six actor- chain profiles for OAuth 2.0 Token Exchange [RFC8693]. [RFC8693] permits nested act claims, but prior actors remain informational only and token exchange does not define how a delegation path is preserved and validated across successive exchanges. This document profiles delegation-chain tokens and defines profile- specific processing for multi-hop workflows. The six profiles are: Declared Full Disclosure; Declared Subset Disclosure; Declared Actor- Only Disclosure; Verified Full Disclosure; Verified Subset Disclosure; and Verified Actor-Only Disclosure. These profiles preserve the existing meanings of sub, act, and may_act. They support same-domain and cross-domain delegation and provide different tradeoffs among visible chain-based authorization, cryptographic accountability, auditability, privacy, and long-running workflow support. Plain RFC 8693 impersonation-shaped outputs remain valid RFC 8693 behavior but are outside this profile family.

### Credential Presentation Architecture
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spice-credential-presentation-architecture-00 | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

### Cryptographically Verifiable Actor Chains
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spice-cryptographically-verifiable-actor-chains-01 | video: https://youtu.be/T43MLoaWsbI | materials: https://datatracker.ietf.org/meeting/125/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

## Working Group: spring

### Path Segment Identifier (PSID) in SRv6 (Segment Routing in IPv6)
Draft: draft-ietf-spring-srv6-path-segment · Working group: spring
Agenda: draft-ietf-spring-srv6-path-segment
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-path-segment/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-path-segment-identifier-psid-in-srv6-segment-routing-in-ipv6-01 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
Segment Routing (SR) allows for a flexible definition of end-to-end paths by encoding an ordered list of instructions, called "segments". The SR architecture can be implemented over an MPLS data plane as well as an IPv6 data plane. Currently, Path Segment Identifier (PSID) has been defined to identify an SR path in SR-MPLS networks, and is used for various use- cases such as end-to-end SR Path Protection and Performance Measurement (PM) of an SR path. This document defines the PSID to identify an SRv6 path in an IPv6 network.

### SRv6 for Redundancy Protection
Draft: draft-ietf-spring-sr-redundancy-protection · Working group: spring
Agenda: draft-ietf-spring-sr-redundancy-protection
page: https://datatracker.ietf.org/doc/draft-ietf-spring-sr-redundancy-protection/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-srv6-for-redundancy-protection-00 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
Redundancy Protection is a generalized protection mechanism to achieve high reliability for services provided in Segment Routing networks. The mechanism uses the "Live-Live" methodology, i.e., multiple copies of the data packets are sent on different paths to provide protection. This document introduces one new SRv6 Segment Endpoint Behavior, the associated Headend Encapsulation Behaviors and the associated Redundancy Policy to provide replication and elimination functions on specific network nodes by leveraging SRv6 Network Programming capabilities.

### SRv6 for Inter-Layer Network Programming
Draft: draft-ietf-spring-srv6-inter-layer-programming · Working group: spring
Agenda: draft-ietf-spring-srv6-inter-layer-programming
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-inter-layer-programming/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-srv6-for-inter-layer-network-programming-00 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
The Segment Routing over IPv6 (SRv6) Network Programming framework enables a network operator or an application to specify a packet processing program by encoding a sequence of instructions in the IPv6 packet header. Following the SRv6 Network Programming concept, this document defines SRv6 based mechanisms for inter-layer network programming, which can help to integrate the packet network layer with its underlying layers efficiently. For inter-layer path programming, a new SRv6 behavior is defined for steering packets to underlay network connections. The applicability of this new SRv6 behavior in typical scenarios is illustrated.

### SRv6 Path Verification
Draft: draft-yang-spring-srv6-verification · Working group: spring
Agenda: draft-yang-spring-srv6-verification
page: https://datatracker.ietf.org/doc/draft-yang-spring-srv6-verification/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-srv6-path-verification-slides-125-spring-srv6-path-verification-04-00 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. However, we have also observed that SRv6 is beginning to extend toward customer site devices, e.g., SD-WAN and enterprise network deployments. Both of the scenarios can be deployed in third-party clouds or at customer sites. This introduces certain security risks, such as packet injection and path manipulation attacks. Section 6 of [I-D.draft-ietf-spring-srv6-security] identifies these risks as well, including Section 6.2.1 on Modification Attacks and Section 6.2.3 on Packet Insertion. This proposal mitigates these risks by enhancing the HMAC mechanism defined in [RFC8754].

### SID as source address in SRv6
Draft: draft-yang-spring-sid-as-source-address · Working group: spring
Agenda: draft-yang-spring-sid-as-source-address
page: https://datatracker.ietf.org/doc/draft-yang-spring-sid-as-source-address/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-sid-as-source-address-in-srv6-00 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. Both the carrier market and the enterprise market are adopting SRv6 for end-to-end service delivery. However, if a firewall exists along an SRv6 path, not only legitimate SRv6 traffic but also ICMP packets generated on SRv6 transit node will be dropped. This proposal addresses this issue by using SID as source address in SRv6 packets.

### 4map6 Segments for IPv4 Service delivery over IPv6-only underlay networks
Draft: draft-dong-spring-sr-4map6-segments · Working group: spring
Agenda: draft-dong-spring-sr-4map6-segments
page: https://datatracker.ietf.org/doc/draft-dong-spring-sr-4map6-segments/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-4map6-segments-for-ipv4-service-delivery-over-ipv6-only-underlay-networks-00 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
This document defines a new type of segment for Segment Routing, 4map6 segment, along with its corresponding End.4map6 endpoint behavior. This behavior performs stateless IPv4/IPv6 translation or encapsulation at PE nodes based on stateless mapping rules, thereby enabling the delivery of IPv4 services over an IPv6-only network. At the same time, the BGP Prefix-SID attribute SRv6 Service TLVs is extended to transmit IPv4/IPv6 address mapping rules in IPv6-only domain and cross-domain.

### Encapsulation of BFD for SRv6 Policy
Draft: draft-liu-spring-bfd-srv6-policy-encap · Working group: spring
Agenda: draft-liu-spring-bfd-srv6-policy-encap
page: https://datatracker.ietf.org/doc/draft-liu-spring-bfd-srv6-policy-encap/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-encapsulation-of-bfd-for-srv6-policy-00 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
Bidirectional Forwarding Detection (BFD) mechanisms can be used for fast detection of failures in the forwarding path of SR Policy. This document describes the encapsulation of BFD for SRv6 Policy. The BFD packets may be encapsulated in Insert-mode or Encaps-mode.

### Linking BGP SR-TE to Spring concepts
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-spring-linking-bgp-sr-te-to-spring-concepts-01 | video: https://youtu.be/JCOybI34REs | materials: https://datatracker.ietf.org/meeting/125/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

## Working Group: srv6ops

### SRv6 Deployment Options
Draft: draft-ietf-srv6ops-srv6-deployment · Working group: srv6ops
Agenda: draft-ietf-srv6ops-srv6-deployment
page: https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6-deployment/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-srv6-deployment-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
When deciding to migrate a network from existing data-plane technologies (e.g. MPLS, SR-MPLS or overlay encapsulations such as VXLAN) to SRv6, common questions involve how to perform the migration, how to minimize impact to the existing network and what techniques are available to support a smooth transition. This document presents various deployment and migration options for networks evolving toward SRv6 from prior transport or overlay technologies.

### Considerations for traffic steering to SRv6
Draft: draft-geng-srv6ops-traffic-steering-to-srv6 · Working group: srv6ops
Agenda: draft-geng-srv6ops-traffic-steering-to-srv6
page: https://datatracker.ietf.org/doc/draft-geng-srv6ops-traffic-steering-to-srv6/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-considerations-for-traffic-steering-to-srv6-01 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
This document primarily describes the traffic steering towards SRv6- BE and SRv6-TE respectively, providing an overview of the main traffic steering methods for these two approaches. Furthermore, it discusses the recommended traffic steering methods for various typical scenarios.

### Addressing Recommendations for SRv6
Draft: draft-horn-srv6ops-srv6addressing · Working group: srv6ops
Agenda: draft-horn-srv6ops-srv6addressing
page: https://datatracker.ietf.org/doc/draft-horn-srv6ops-srv6addressing/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-sessa-23-addressing-recommendations-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
This document provides recommendations for addressing SRv6 locators format. It introduces concepts of Blocks, Sets, and Node IDs, and explains how summarization boundaries and flexible algorithm support can be implemented for both small and large networks.

### Service Interworking between SRv6
Draft: draft-cheng-spring-service-interworking-srv6 · Working group: srv6ops
Agenda: draft-cheng-spring-service-interworking-srv6
page: https://datatracker.ietf.org/doc/draft-cheng-spring-service-interworking-srv6/ | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
When operators provide services through SRv6, such as L3VPN and L2VPN, there may be cross-domain scenarios of multiple ASs, or multiple admin domain scenarios within the same AS. This document describes how to implement interworking of services for such scenarios.

### QP-based SRv6 Load Balancing Deployment
Draft: draft-lll-srv6ops-qp-aware-srv6-lb · Working group: srv6ops
Agenda: draft-lll-srv6ops-qp-aware-srv6-lb
page: https://datatracker.ietf.org/doc/draft-lll-srv6ops-qp-aware-srv6-lb/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-25-qp-based-srv6-load-balancing-deployment-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
This document describes the use of Segment Routing over IPv6 (SRv6) path selection based on Queue Pair (QP) in Intelligent Computing Wide Area Network (WAN) for Data Center Interconnection (DCI), optimizing load balancing for predictable workloads.

### SR Policy Selector
Draft: draft-yang-srv6ops-policy-selector · Working group: srv6ops
Agenda: draft-yang-srv6ops-policy-selector
page: https://datatracker.ietf.org/doc/draft-yang-srv6ops-policy-selector/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-26-srv6-policy-selectorslides-125-sr-policy-selector-02-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
Segment routing (SR) [RFC8402] is a source routing paradigm that explicitly indicates the forwarding path for packets at the ingress node. An SR Policy is associated with one or more candidate paths, and each candidate path is either dynamic, explicit or composite. This document describes a policy selection mechanism among the candidate SR Policies based on network quality.

### ESP Protection for Services over SRv6
Draft: draft-wdh-srv6ops-secservice · Working group: srv6ops
Agenda: draft-wdh-srv6ops-secservice
page: https://datatracker.ietf.org/doc/draft-wdh-srv6ops-secservice/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-sessa-271-esp-protection-for-services-over-srv6-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
This document describes a mechanism for protecting selected service traffic using IPsec ESP while transporting the traffic over an SRv6 domain. The approach enables service payloads to be encrypted prior to SRv6 encapsulation, allowing the SRv6 header to remain visible for segment-based forwarding within the provider network. This mechanism supports services or applications that require additional confidentiality and integrity protection, even when carried over an operator-managed SRv6 domain.

### Introduction
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-1-introduction-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Service Interworking
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-sessa-24-service-interworking-00 | video: https://youtu.be/UO-pii-vFT0 | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### IPv6&SRv6 Powering Alibaba Cloud AI Computing (Alibaba)
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-21-ipv6srv6-powering-alibaba-cloud-ai-computing-alibaba-02 | video: https://youtu.be/GwiJ_zFmewE | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6-Driven Security Resource Pools （China Mobile）V1
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-22-srv6-driven-security-resource-pools-china-mobilev1-00 | video: https://youtu.be/GwiJ_zFmewE | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 for End-to-End Services (Guangdong Power Grid)
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-srv6ops-23-srv6-for-end-to-end-services-guangdong-power-grid-01 | video: https://youtu.be/GwiJ_zFmewE | materials: https://datatracker.ietf.org/meeting/125/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

## Working Group: tcpm

### TCP ACK Rate Request Option
Draft: draft-ietf-tcpm-ack-rate-request · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-ietf-tcpm-ack-rate-request/
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-ack-rate-request/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tcpm-tcp-ack-rate-request-tarr-00 | video: https://youtu.be/tCm6YuAsA7I | materials: https://datatracker.ietf.org/meeting/125/session/tcpm
TCP Delayed Acknowledgments (ACKs) is a widely deployed mechanism that allows reducing protocol overhead in many scenarios. However, Delayed ACKs may also contribute to suboptimal performance. When a relatively large congestion window (cwnd) can be used, less frequent ACKs may be desirable. On the other hand, in relatively small cwnd scenarios, eliciting an immediate ACK may avoid unnecessary delays that may be incurred by the Delayed ACKs mechanism. This document specifies the TCP ACK Rate Request (TARR) option. This option allows a sender to request the ACK rate to be used by a receiver, and it also allows to request immediate ACKs from a receiver.

### TCP RST Diagnostic Payload
Draft: draft-boucadair-tcpm-rst-diagnostic-payload · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-boucadair-tcpm-rst-diagnostic-payload/
page: https://datatracker.ietf.org/doc/draft-boucadair-tcpm-rst-diagnostic-payload/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tcpm-ietf-125-draft-boucadair-tcpm-rst-diagnostic-payload-00 | video: https://youtu.be/tCm6YuAsA7I | materials: https://datatracker.ietf.org/meeting/125/session/tcpm
This document specifies an experimental diagnostic payload format returned in TCP RST segments. Such payloads are used to share with an endpoint the reasons for which a TCP connection has been reset. Sharing this information is meant to ease diagnostic and troubleshooting. This specification builds on provisions that are already present in RFC 9293 "Transmission Control Protocol (TCP)". As such, this document does not require any change to RFC 9293.

### Provenance Identifier TCP Option
Draft: draft-liang-tcpm-provenance-option · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-liang-tcpm-provenance-option/
page: https://datatracker.ietf.org/doc/draft-liang-tcpm-provenance-option/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tcpm-tcp-provenance-identifier-option-00 | video: https://youtu.be/tCm6YuAsA7I | materials: https://datatracker.ietf.org/meeting/125/session/tcpm
This document describes a TCP option that carries a Provenance Identifier (ProvID) to enable correlation of TCP connections when transport-layer identifiers change along the path.

### Applicability of TCP-AO for Securing NETCONF and gNMI
Draft: draft-bedford-tcpm-ao-for-gnmi-netconf · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-bedford-tcpm-ao-for-gnmi-netconf/
page: https://datatracker.ietf.org/doc/draft-bedford-tcpm-ao-for-gnmi-netconf/ | video: https://youtu.be/tCm6YuAsA7I | materials: https://datatracker.ietf.org/meeting/125/session/tcpm
This document analyzes the applicability of the TCP Authentication Option (TCP-AO) to secure TCP-based network management protocols, specifically NETCONF and gNMI. It describes deployment profiles in which TCP-AO provides per-connection integrity and peer authentication with low operational overhead, either as an alternative to or in combination with TLS/SSH. This document gives guidance on key management (e.g., static keys and operational "key chains") and documents expected behaviors and benefits. No new protocol bits are defined and there are no IANA actions.

### An Upgraded TCP Session Type
Draft: draft-bonica-tcpm-extended-options · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/ | video: https://youtu.be/tCm6YuAsA7I | materials: https://datatracker.ietf.org/meeting/125/session/tcpm
Currently, TCP maintains ordinary sessions (SES-O) in which ordinary segments (SEG-O) are exchanged. Each SEG-O can accommodate up to 40 octets of options. In the future, applications may require more than 40 octets of options. For example, an application may use a 36-byte TCP Authentication Option (TCP-AO), leaving insufficient space for other required options. Therefore, this document describes an experiment in which upgraded sessions (SES-U) and upgraded segments (SEG-U) are introduced. Each SEG-U can accommodate up to 1,016 octets of Individual Options.

### tcp-ao
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tcpm-tcp-ao-00 | video: https://youtu.be/tCm6YuAsA7I | materials: https://datatracker.ietf.org/meeting/125/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

## Working Group: tls

### Use of ML-DSA in TLS 1.3
Draft: draft-ietf-tls-mldsa · Working group: tls
Agenda: draft-ietf-tls-mldsa
page: https://datatracker.ietf.org/doc/draft-ietf-tls-mldsa/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-hollebeek-use-of-ml-dsa-in-tls-13-00 | video: https://youtu.be/iAxTRFKY1Pc | materials: https://datatracker.ietf.org/meeting/125/session/tls
This memo specifies how the post-quantum signature scheme ML-DSA (FIPS 204) is used for authentication in TLS 1.3.

### A Password Authenticated Key Exchange Extension for TLS 1.3
Draft: draft-ietf-tls-pake · Working group: tls
Agenda: draft-ietf-tls-pake
page: https://datatracker.ietf.org/doc/draft-ietf-tls-pake/ | materials: https://datatracker.ietf.org/meeting/125/session/tls
The pre-shared key mechanism available in TLS 1.3 is not suitable for usage with low-entropy keys, such as passwords entered by users. This document describes an extension that enables the use of password-authenticated key exchange protocols with TLS 1.3.

### ML-KEM Post-Quantum Key Agreement for TLS 1.3
Draft: draft-ietf-tls-mlkem · Working group: tls
Agenda: draft-ietf-tls-mlkem
page: https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/ | materials: https://datatracker.ietf.org/meeting/125/session/tls
This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as NamedGroups and registers IANA values in the TLS Supported Groups registry for use in TLS 1.3 to achieve post-quantum (PQ) key establishment.

### PQC Continuity: Downgrade Protection for TLS Servers Migrating to PQC
Draft: draft-sheffer-tls-pqc-continuity · Working group: tls
Agenda: draft-sheffer-tls-pqc-continuity
page: https://datatracker.ietf.org/doc/draft-sheffer-tls-pqc-continuity/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-pqc-continuity-00 | video: https://youtu.be/iAxTRFKY1Pc | materials: https://datatracker.ietf.org/meeting/125/session/tls
As the Internet transitions toward post-quantum cryptography (PQC), many TLS servers will continue supporting traditional certificates to maintain compatibility with legacy clients. However, this coexistence introduces a significant vulnerability: an undetected rollback attack, where a malicious actor strips the PQC or composite certificate and forces the use of a classical certificate once quantum-capable adversaries exist. To defend against this, this document defines a TLS extension that allows a TLS client to cache a server's declared commitment to present PQC or composite certificates for a specified duration. On subsequent connections, the client enforces that cached commitment and rejects traditional-only certificates that conflict with it. This mechanism, inspired by HTTP Strict Transport Security (HSTS) but operating at the TLS layer, provides PQC downgrade protection without requiring changes to certificate authority (CA) infrastructure.

### Extended Key Update for Transport Layer Security (TLS) 1.3
Draft: draft-ietf-tls-extended-key-update · Working group: tls
Agenda: draft-ietf-tls-extended-key-update
page: https://datatracker.ietf.org/doc/draft-ietf-tls-extended-key-update/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-sessa-extended-key-update-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
TLS 1.3 ensures forward secrecy by performing an ephemeral Diffie- Hellman key exchange during the initial handshake, protecting past communications even if a party's long-term keys (typically a private key with a corresponding certificate) are later compromised. While the built-in KeyUpdate mechanism allows application traffic keys to be refreshed during a session, it does not incorporate fresh entropy from a new key exchange and therefore does not provide post- compromise security. This limitation can pose a security risk in long-lived sessions, such as those found in industrial IoT or telecommunications environments. To address this, this specification defines an extended key update mechanism that performs a fresh execution of the key exchange negotiated during the initial handshake within an active session, thereby ensuring post-compromise security. By forcing attackers to exfiltrate new key material repeatedly, this approach mitigates the risks associated with static key compromise. Regular renewal of session keys helps contain the impact of such compromises. The extension is applicable to both TLS 1.3 and DTLS 1.3.

### Larger Data in TLS 1.3 Handshake
Draft: draft-wagner-tls-keysharepqc · Working group: tls
Agenda: draft-wagner-tls-keysharepqc
page: https://datatracker.ietf.org/doc/draft-wagner-tls-keysharepqc/ | materials: https://datatracker.ietf.org/meeting/125/session/tls
This memo discusses possible modifications of TLS 1.3, aimed to allow trasferring data larger than 64 Kbytes in handshake messages. One possible application for this feature is to allow using post-quantum Key Encapsulation Method that have large public key or ciphertext size (like Classic McEliece).

### Proposed Document Template for TLS FATT Process
Draft: draft-usama-tls-fatt-extension · Working group: tls
Agenda: draft-usama-tls-fatt-extension
page: https://datatracker.ietf.org/doc/draft-usama-tls-fatt-extension/ | materials: https://datatracker.ietf.org/meeting/125/session/tls
This document applies only to non-trivial extensions of TLS, which require formal analysis. FATT process has successfully discovered CVEs of *CVSS 7.5* and most recently expected *CVSS 9.1* in the *production* implementations of the drafts proposed for adoption in the TLS WG. To achieve high cryptographic assurances, this document proposes the drafts specify a clear threat model and informal security goals in the Security Considerations section, as well as motivation and a protocol diagram in the draft.

### Authenticated ECH Config Distribution and Rotation
Draft: draft-sullivan-tls-signed-ech-updates · Working group: tls
Agenda: draft-sullivan-tls-signed-ech-updates
page: https://datatracker.ietf.org/doc/draft-sullivan-tls-signed-ech-updates/ | materials: https://datatracker.ietf.org/meeting/125/session/tls
Encrypted ClientHello (ECH) requires clients to have the server's ECH configuration before connecting. Currently, when ECH fails, servers can send updated configurations but clients cannot authenticate them unless the server has a valid certificate for the public name, limiting deployment flexibility. This document specifies a new mechanism for authenticating ECH configurations. Servers include additional information in their initial ECH configurations, which enables clients to authenticate updated configurations without relying on a valid certificate for the public name.

### Workload Identifier Origin Hint for TLS ClientHello
Draft: draft-rosomakho-tls-wimse-cert-hint · Working group: tls
Agenda: draft-rosomakho-tls-wimse-cert-hint
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-workload-identifier-origin-hint-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
This document defines a TLS extension that allows clients to indicate one or more workload identifier origins in the ClientHello message. Each origin consists of a URI scheme and trust domain component, representing the administrative domain and identifier namespace in which the client operates. These identifier origins serve as hints to enable the server to determine whether client authentication is required and which policies or trust anchors should apply. This mechanism improves efficiency in mutual TLS deployments while minimising the exposure of sensitive identifier information. To protect confidentiality, this extension can be used in conjunction with Encrypted Client Hello (ECH).

### FATT report on EKU
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-sessa-fatt-report-on-eku-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Beyond the 64K Limit  in TLS 1.3 Handshake
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-sessa-beyond-the-64k-limit-in-tls-13-handshake-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### TLS FATT Extensions
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-tls-fatt-extensions-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### ECH Tests
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-sessa-ech-tests-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### ECH Measurements
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-sessa-ech-measurements-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Signed ECH Configs
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-signed-ech-configs-00 | video: https://youtu.be/2GkmQmRlkto | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### TLS PAKE
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-sessb-tls-pake-00 | video: https://youtu.be/iAxTRFKY1Pc | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### ML-KEM for TLS 1.3
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-ml-kem-for-tls-13-00 | video: https://youtu.be/iAxTRFKY1Pc | materials: https://datatracker.ietf.org/meeting/125/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

## Working Group: tsvwg

### Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-ietf-tsvwg-sctp-dtls-chunk · Working group: tsvwg
Agenda: 0915-0935 DTLS Chunk (Magnus) https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tsvwg-dtls-chunk-for-sctp-00 | video: https://youtu.be/NoAoWNJ5y7Y | materials: https://datatracker.ietf.org/meeting/125/session/tsvwg
This document describes a method for adding Datagram Transport Layer Security (DTLS) based authentication and cryptographic protection to the Stream Control Transmission Protocol (SCTP). This SCTP extension is intended to enable communication privacy for applications that use SCTP as their transport protocol and allows applications to communicate in a way that is designed to prevent eavesdropping and detect tampering or message forgery. Once enabled, this also applies to the SCTP payload as well as the SCTP control information. Applications using this SCTP extension can use most of the transport features provided by SCTP and its other extensions. The use of the SCTP Authentication extension defined in RFC 4895 is incompatible with the extension defined in this document but would not provide any additional service. This implies that the Dynamic Address Reconfiguration as specified in RFC 5061 can only be used as described in this document. This document obsoletes RFC 6083 and updates RFC 5061.

### Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm
Draft: draft-ietf-tsvwg-fq-pie · Working group: tsvwg
Agenda: 0945-0955 FQ-PIE (Mohit) https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tsvwg-fq-pie-00 | video: https://youtu.be/NoAoWNJ5y7Y | materials: https://datatracker.ietf.org/meeting/125/session/tsvwg
This document presents Flow Queue Proportional Integral controller Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue Management (AQM) algorithm to isolate flows and tackle the problem of bufferbloat. FQ-PIE uses hashing to classify incoming packets into different queues and provide flow isolation. Packets are dequeued by using a variant of the round robin scheduler. Each such flow is managed by the PIE algorithm to maintain high link utilization while controlling the queue delay to a target value.

### Export of ECN Information in IPFIX
Draft: draft-song-opsawg-ipfix-ecn · Working group: tsvwg
Agenda: 1000-1010 IP-FIX ECN (Xueyan) https://datatracker.ietf.org/doc/draft-song-opsawg-ipfix-ecn/
page: https://datatracker.ietf.org/doc/draft-song-opsawg-ipfix-ecn/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tsvwg-export-of-ecn-information-in-ipfix-00 | video: https://youtu.be/NoAoWNJ5y7Y | materials: https://datatracker.ietf.org/meeting/125/session/tsvwg
This document defines a set of IPFIX Information Elements for monitoring Explicit Congestion Notification (ECN), specifically in the context of the Low Latency, Low Loss, and Scalable Throughput (L4S) service. These Information Elements allow network operators to observe ECN codepoint usage within L4S deployments and evaluate the corresponding traffic performance.

### Available Session Recovery Protocol
Draft: draft-cmcc-asrp · Working group: tsvwg
Agenda: 1015-1030 Available Session Recovery Protocol (Zhaoyu Luo) https://datatracker.ietf.org/doc/draft-cmcc-asrp/
page: https://datatracker.ietf.org/doc/draft-cmcc-asrp/ | video: https://youtu.be/NoAoWNJ5y7Y | materials: https://datatracker.ietf.org/meeting/125/session/tsvwg
This document describes an experimental protocol, the Available Session Recovery Protocol (ASRP), for high-availability clusters that provide stateful network services - load balancing, Network Address Translation (NAT [RFC4787]), and other layer-4 stateful network functions, including their virtualized (NFV) forms. ASRP backs up the session state at the session's own endpoints, so that the cluster nodes hold no replicated state: no inter-node synchronization, no backup node, and no state warm-up for a newly added node. The document defines the procedures and message formats for session backup and recovery. In contrast to traditional high-availability techniques that back up session state within the cluster itself, the core innovation of ASRP lies in its distributed backup of state information to the client or server side. This approach offers multiple advantages: theoretically unlimited elastic scaling capacity; support for rapid recovery from multi-point failures; reduction of resource redundancy through the elimination of centralized backup nodes; and significant simplification of cluster implementation complexity. The ASRP protocol provides a standardized method for constructing elastic service clusters, facilitating broader participation from software and hardware developers in building elastic cloud network service clusters.

### L4S Update - Livingood
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-tsvwg-l4s-update-livingood-00 | video: https://youtu.be/NoAoWNJ5y7Y | materials: https://datatracker.ietf.org/meeting/125/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

## Working Group: v6ops

### Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses
Draft: draft-ietf-v6ops-nat64-wkp-1918 · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-01-jen-linkova-draft-ietf-v6ops-nat64-wkp-1918-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document modifies the deployment guidance provided in Section 3.1 of RFC 6052 (IPv6 Addressing of IPv4/IPv6 Translators) that IPv4/IPv6 Translators must not use the Well-Known Prefix 64:ff9b::/96 to represent non-globally reachable IPv4 addresses, such as those defined in RFC 1918 (Address Allocation for Private Internets) or listed in Section 2.2.2 of RFC 6890 (Special-Purpose IP Address Registries). This change enables IPv6-only nodes to reach IPv4-only services with specific non-globally reachable addresses by leveraging the Well-Known Prefix. This document updates RFC 6052 to allow packets in which an address is composed of the Well-Known Prefix and specific non-globally reachable IPv4 addresses to be translated.

### Stateful NAT64: Network Address and Protocol Translation from IPv6 Clients to IPv4 Servers
Draft: draft-ietf-v6ops-rfc6146-bis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc6146-bis/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc6146-bis/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-02-1-jordi-palet-rfc6146-bis-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document specifies a stateful NAT64 translation, which allows IPv6-Only clients to contact IPv4 servers using unicast UDP, TCP, or ICMP. One or more public IPv4 addresses assigned to a stateful NAT64 translator are shared among several IPv6-Only clients. Stateful NAT64 translation also supports IPv4-initiated communications to a subset of the IPv6 hosts through configured bindings in the stateful NAT64 translator. When the stateful NAT64 translation is used in conjunction with DNS64, no changes are required in either the IPv6 client or the IPv4 server. This document obsoletes RFC 6146.

### IP/ICMP Translation Algorithm
Draft: draft-ietf-v6ops-rfc7915-bis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7915-bis/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-02-2-jordi-palet-rfc7915-bis-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document describes the Stateless IP/ICMP Translation Algorithm (SIIT), which translates between IPv4 and IPv6 packet headers (including ICMP headers). This document obsoletes RFC 7915.

### Basic Requirements for IPv6 Customer Edge Routers
Draft: draft-ietf-v6ops-rfc7084bis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-basic-requirements-for-ipv6-customer-edge-routers-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document specifies requirements for an IPv6 Customer Edge (CE) router. Specifically, the current version of this document focuses on the basic provisioning of an IPv6 CE router and the provisioning of IPv6 hosts attached to it. The document obsoletes RFC 7084.

### Measurement and Analysis of IPv6 Interface Identifier Patterns in the Real World
Draft: draft-ren-v6ops-ipv6-iid-patterns-measurement · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ren-v6ops-ipv6-iid-patterns-measurement/
page: https://datatracker.ietf.org/doc/draft-ren-v6ops-ipv6-iid-patterns-measurement/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-04-zhang-wei-measurement-and-analysis-of-ipv6-interface-identifier-patterns-in-the-real-world-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
Interface Identifiers (IIDs) are critical components of IPv6 addresses, significantly impacting user privacy and the feasibility of network reconnaissance. RFC 7707 previously provided a comprehensive analysis of IID patterns based on data from the early stages of IPv6 deployment. However, with the widespread adoption of privacy-enhancing standards such as RFC 7217, historical data no longer accurately reflects the current IPv6 ecosystem. This document provides updated measurements of IID patterns by utilizing an improved pattern recognition method and incorporating novel data sources, such as public mailing lists. The measurement data reveals that while "Low-byte" patterns have decreased significantly in server addresses, a substantial number of seemingly random addresses actually belong to non-random, specific patterns, implying that heuristic scanning remains a viable vector. Meanwhile, client devices have widely adopted randomized addresses, effectively enhancing privacy. This document aims to update the statistics and analysis regarding IID pattern distribution found in RFC 7707, providing essential insights for modern network defense strategies and standard compliance.

### IPv6 Prefix Assignment to end-users
Draft: draft-palet-v6ops-prefix-assignment · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-palet-v6ops-prefix-assignment/
page: https://datatracker.ietf.org/doc/draft-palet-v6ops-prefix-assignment/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-05-1-jordi-palet-ipv6-prefix-assignment-to-end-users-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document describes different alternatives and best current practices for assignment of IPv6 prefixes for end-user broadband networks, including considerations about point-to-point links, their size, numbering choices, pool choices, customer prefix assignment size and persistance of those assignments.

### IPv6-only and IPv6-Mostly Terminology Definitions
Draft: draft-palet-v6ops-ipv6-only · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-palet-v6ops-ipv6-only/
page: https://datatracker.ietf.org/doc/draft-palet-v6ops-ipv6-only/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-05-02-jordi-palet-ipv6-only-terminology-definition-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document defines the terminology regarding the usage of expressions such as "IPv6-only" and "IPv6-Mostly", in order to avoid confusions when using them in IETF and other documents. The goal is that the reference to "IPv6-only" describes the actual native functionality being used, not the actual protocol support.

### IPv6 Network Deployment Monitoring and Analysis
Draft: draft-pang-v6ops-ipv6-monitoring-deployment · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-monitoring-deployment/
page: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-monitoring-deployment/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-06-jing-zhao-ipv6-network-deployment-monitoring-and-analysis-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document addresses key operational challenges in large-scale IPv6 deployment and proposes an architecture for IPv6 deployment monitoring and analysis. It describes an architectural approach and comprehensive metrics to provide end-to-end visibility across network infrastructure, cloud services, edge computing, and end-user domains.

### Considerations of IPv6-only Deployment in 5G Mobile Networks
Draft: draft-ma-v6ops-5g-ipv6only · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/
page: https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-07-considerations-of-gradual-ipv6-only-deployment-in-5g-mobile-networks-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
This document describes a practical guide of deploying 464XLAT based IPv6-only technology on user plane in 3GPP 5G networks. It also covers key 5G concepts and architectures, configuration methods and operational challenges.

### Capabilities and Future Requirements of IPv6 for the Internet of Agents (IoA)
Draft: draft-yc-ipv6-for-ioa · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-yc-ipv6-for-ioa/
page: https://datatracker.ietf.org/doc/draft-yc-ipv6-for-ioa/ | slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-08-jiaming-ye-08-slide-draft-yc-ipv6-for-ioa-00 | video: https://youtu.be/eAcZXJI89rU | materials: https://datatracker.ietf.org/meeting/125/session/v6ops
In the coming years, the accelerating proliferation of agentic AI is anticipated to drive the number of intelligent agents to reach the scale of hundreds of billions. IPv6, with vast address space, native end-to-end connectivity and rich built-in functionalities, serves as the critical infrastructure underpinning the development of the Internet of Agents (IoA). This draft systematically analyzes the foundational capabilities that IPv6 can provide for the IoA at the current stage, and further explores the evolutionary requirements that the IoA imposes on the future IPv6 development.

## Working Group: wimse

### WIMSE Workload Credentials
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-wimse-workload-credentials-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### HTTP Signatures
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-http-signatures-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### IETF 125 WIMSE Architecture
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-ietf-125-wimse-architecture-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Identifier
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-wimse-identifier-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Workload Identity Practices
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-wimse-workload-identity-practices-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Architecture (update)
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-wimse-architecture-update-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Workload Proof Token
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/125/materials/slides-125-wimse-wimse-workload-proof-token-00 | video: https://youtu.be/JdQD94OdcI8 | materials: https://datatracker.ietf.org/meeting/125/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

