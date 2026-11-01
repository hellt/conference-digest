>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-123. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-123.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-123.md
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

Below is the program for IETF 123 (Madrid) (standards). Read it and produce a digest
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
conference: IETF 123 (Madrid)
type: standards
source_url: https://datatracker.ietf.org/meeting/123/agenda.json
generated: 2026-11-01
registry_key: ietf-123
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Working Group: 6man

### IPv6 Node Requirements
Draft: draft-ietf-6man-rfc8504-bis · Working group: 6man
Agenda: draft-ietf-6man-rfc8504-bis
page: https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-6man-ipv6-node-requirements-01 | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
This document defines requirements for IPv6 nodes. It is expected that IPv6 will be deployed in a wide range of devices and situations. Specifying the requirements for IPv6 nodes allows IPv6 to function well and interoperate in a large number of situations and deployments. This document obsoletes RFC 8504, and in turn RFC 6434 and its predecessor, RFC 4294.

### Internet Control Message Protocol (ICMPv6) Reflection
Draft: draft-ietf-6man-icmpv6-reflection · Working group: 6man
Agenda: draft-ietf-6man-icmpv6-reflection
page: https://datatracker.ietf.org/doc/draft-ietf-6man-icmpv6-reflection/ | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
This document specifies the ICMPv6 Reflection utility. The ICMPv6 Reflection utility is a diagnostic tool, similar to Ping and the ICMPv6 PROBE utility. It is similar to Ping and PROBE in that it relies on a stateless message exchange between a probing node and a probed node. The probing node sends a request to the probed node and the probed node responds to the request. The ICMPv6 Reflection utility differs from Ping and PROBE because, in the ICMPv6 Reflection utility, the probing node requests a snapshot of the message that it sent, as it was when arrived at the probed node. The probed node returns the requested snapshot. The ICMPv6 Reflection utility is useful because it can allow the user to see how the network modified the request as it traveled from the probing node to the probed node.

### Problem Statement with Aggregate Header Limit for IPv6
Draft: draft-liu-6man-aggregate-header-limit-problem · Working group: 6man
Agenda: draft-liu-6man-aggregate-header-limit-problem
page: https://datatracker.ietf.org/doc/draft-liu-6man-aggregate-header-limit-problem/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-6man-problem-statement-with-aggregate-header-limit-for-ipv6-00 | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
This document first proposes the concept of "Aggregate header limit for IPv6"(IPv6-AHL) to indicate the total header size that a router is able to process at full forwarding rate for IPv6 packets. Then this document describes the problems for path calculation and function enablement without the awareness of IPv6-AHL, and the considerations for IPv6-AHL collection are also included.

### ICMP Error Handling in SRv6 based VPN Networks
Draft: draft-ali-6man-srv6-vpn-icmp-error-handling · Working group: 6man
Agenda: draft-ali-6man-srv6-vpn-icmp-error-handling
page: https://datatracker.ietf.org/doc/draft-ali-6man-srv6-vpn-icmp-error-handling/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-6man-icmp-error-handling-in-srv6-based-vpn-networks-00 | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
The document specifies procedures for handling ICMP error in SRv6-based Virtual Private Network (VPN).

### IPv6 wants 802.11 Flexible Multicast Service
Draft: draft-equinox-6man-ieee80211-fms · Working group: 6man
Agenda: draft-equinox-6man-ieee80211-fms
page: https://datatracker.ietf.org/doc/draft-equinox-6man-ieee80211-fms/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-6man-ipv6-wants-80211-flexible-multicast-service-00 | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
IEEE 802.11 Flexible Multicast Service (FMS) addresses reliability issues in IPv6 due to aggressive powersave optimizations in 802.11 client devices. The intent of this document is to collect consensus in the IETF 6man (IPv6 Maintenance) working group to request either/both the IEEE 802.11 Working Group and/or the Wifi Alliance's certification process to make implementing FMS a requirement.

### IPv6 Reflection Utility
Presentation · Working group: 6man
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-6man-ipv6-reflection-utility-00 | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
Slides presented at the 6man session; no Internet-Draft is linked to them.

### Off-link Prefixes vs. Neighbor Discovery Protocol
Presentation · Working group: 6man
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-6man-off-link-prefixes-vs-neighbor-discovery-protocol-00 | video: https://www.youtube.com/watch?v=TkcJ0JhgqBQ | materials: https://datatracker.ietf.org/meeting/123/session/6man
Slides presented at the 6man session; no Internet-Draft is linked to them.

## Working Group: acme

### Automated Certificate Management Environment (ACME) Delay-Tolerant Networking (DTN) Node ID Validation Extension
Draft: draft-ietf-acme-dtnnodeid · Working group: acme
Agenda: draft-ietf-acme-dtnnodeid
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dtnnodeid/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document specifies an extension to the Automated Certificate Management Environment (ACME) protocol which allows an ACME server to validate the Delay-Tolerant Networking (DTN) Node ID for an ACME client. A DTN Node ID is an identifier used in the Bundle Protocol (BP) to name a "singleton endpoint", one which is registered on a single BP node. The DTN Node ID is encoded as a certificate Subject Alternative Name (SAN) of type otherName with a name form of BundleEID and as an ACME Identifier type "bundleEID".

### ACME Integrations for Device Certificate Enrollment
Draft: draft-ietf-acme-integrations · Working group: acme
Agenda: draft-ietf-acme-integrations
page: https://datatracker.ietf.org/doc/draft-ietf-acme-integrations/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document outlines multiple advanced use cases and integrations that ACME facilitates without any modifications or enhancements required to the base ACME specification. The use cases include ACME integration with EST, BRSKI and TEAP.

### Automated Certificate Management Environment (ACME) Device Attestation Extension
Draft: draft-acme-device-attest · Working group: acme
Agenda: draft-acme-device-attest -- Brandon Weeks [15 mins]
page: https://datatracker.ietf.org/doc/draft-acme-device-attest/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document specifies new identifiers and a challenge for the Automated Certificate Management Environment (ACME) protocol which allows validating the identity of a device using attestation.

### ACME End User Client and Code Signing Certificates
Draft: draft-ietf-acme-client · Working group: acme
Agenda: draft-ietf-acme-client -- Kathleen Moriarty [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-client/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-acme-client-challenge-types-acme-end-user-client-and-code-signing-certificates-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
Automated Certificate Management Environment (ACME) core protocol addresses the use case of web server certificates for TLS. This document extends the ACME protocol to add 3 challenge types that may support service account authentication credentials, micro-service accounts credentials, device client, code signing, document signing certificates and keys.

### Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge
Draft: draft-ietf-acme-dns-account-label · Working group: acme
Agenda: draft-ietf-acme-dns-account-label -- ??
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dns-account-label/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document outlines a new DNS-based challenge type for the ACME protocol that enables multiple independent systems to authorize a single domain name concurrently. By adding a unique label to the DNS validation record name, the dns-account-01 challenge avoids CNAME delegation conflicts inherent to the dns-01 challenge type. This is particularly valuable for multi-region or multi-cloud deployments that wish to rely upon DNS-based domain control validation and need to independently obtain certificates for the same domain.

### Automated Certificate Management Environment (ACME) Extension for Public Key Challenges
Draft: draft-geng-acme-public-key · Working group: acme
Agenda: draft-geng-acme-public-key -- Xialiang Frank [10 mins]
page: https://datatracker.ietf.org/doc/draft-geng-acme-public-key/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-acme-extension-for-public-key-challenges-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
The Automatic Certificate Management Environment (ACME) [RFC8555] requires a PKCS#10 Certificate Signing Request (CSR) at the finalization stage. This document defines a new ACME challenge type, "pk-01", that allows a client to prove possession of a private key directly, without constructing a CSR. The primary motivation is to support key types that cannot generate CSR self-signatures, notably post-quantum Key Encapsulation Mechanism (KEM) keys. The client declares the public key via a popKey field in the "newOrder" request; the server attaches the "pk-01" challenge to existing identifier authorizations. When all required authorizations are satisfied, the ACME server issues a certificate using the validated public key and the authorized identifiers, eliminating the need for a CSR in the finalization stage.

### Automated Certificate Management Environment (ACME) rats Identifier and Challenge Type
Draft: draft-liu-acme-rats · Working group: acme
Agenda: draft-liu-acme-rats -- Peter Liu [10 mins]
page: https://datatracker.ietf.org/doc/draft-liu-acme-rats/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document describes an approach where an ACME Server can challenge an ACME Client to provide a Remote Attestation Evidence or Remote Attestation Result in any format supported by the Conceptual Message Wrapper. The ACME Server can optionally challenge the Client for specific claims that it wishes attestation for.

### Auto-discovery mechanism for ACME authorized clients
Draft: draft-vanbrouwershaven-acme-client-discovery · Working group: acme
Agenda: draft-vanbrouwershaven-acme-client-discovery , draft-vanbrouwershaven-acme-auto-discovery -- Mike Ounsworth [10 mins]
page: https://datatracker.ietf.org/doc/draft-vanbrouwershaven-acme-client-discovery/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
A significant challenge in the widespread adoption of the Automated Certificate Management Environment (ACME) [RFC8555] is the trust establishment between ACME servers and clients. While ACME clients can automatically discover the URL of the ACME server through ACME Auto Discovery [I-D.vanbrouwershaven-acme-auto-discovery], they face difficulty in identifying authorized clients. This draft proposes a solution to this problem by allowing Certification Authority (CA) customers to specify which ACME keys are authorized to request certificates on their behalf by simply providing the domain name of the service provider. Specifically, this document registers the URI "/.well-known/acme- keys" at which all compliant service providers can publish their ACME client public keys. This mechanism allows the ACME server to identify the specific service provider, enhancing the trust relationship. Furthermore, it provides flexibility to service providers as they can use multiple keys and rotate them as often as they like, thereby improving security and control over their ACME client configurations while giving CA customers the ability to specifically authorize which service providers can request certificates on their behalf.

### Auto-discovery mechanism for ACME servers
Draft: draft-vanbrouwershaven-acme-auto-discovery · Working group: acme
Agenda: draft-vanbrouwershaven-acme-client-discovery , draft-vanbrouwershaven-acme-auto-discovery -- Mike Ounsworth [10 mins]
page: https://datatracker.ietf.org/doc/draft-vanbrouwershaven-acme-auto-discovery/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-acme-auto-discovery-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
A significant impediment to the widespread adoption of the Automated Certificate Management Environment (ACME) [RFC8555] is that ACME clients need to be pre-configured with the URL of the ACME server to be used. This often leaves domain owners at the mercy of their hosting provider as to which Certification Authorities (CAs) can be used. This specification provides a mechanism to bootstrap ACME client configuration from a domain's DNS CAA Resource Record [RFC8659], thus giving control of which CA(s) to use back to the domain owner. Specifically, this document specifies two new extensions to the DNS CAA Resource Record: the "discovery" and "priority" parameters. Additionally, it registers the URI "/.well-known/acme" at which all compliant ACME servers will host their ACME directory object. By retrieving instructions for the ACME client from the authorized CA(s), this mechanism allows for the domain owner to configure multiple CAs in either load-balanced or fallback prioritizations which improves user preferences and increases diversity in certificate issuers.

### JWTClaimConstraints profile of ACME Authority Token
Draft: draft-wendt-acme-authority-token-jwtclaimcon · Working group: acme
Agenda: draft-wendt-acme-authority-token-jwtclaimcon-04 -- Chris Wendt [10 mins]
page: https://datatracker.ietf.org/doc/draft-wendt-acme-authority-token-jwtclaimcon/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-ietf123-jwtclaimcon-authority-token-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document defines an authority token profile for handling the validation of JWTClaimConstraints and EnhancedJWTClaimConstraints. This profile follows the model established in Authority Token for the validation of TNAuthList but is specifically tailored for the JWTClaimConstraints certificate extensions. The profile enables validation and challenge processes necessary to support certificates containing both TNAuthList and JWTClaimConstraints, particularly in the context of Secure Telephone Identity (STI).

### Automated Certificate Management Environment (ACME) Profiles Extension
Draft: draft-aaron-acme-profiles · Working group: acme
Agenda: draft-aaron-acme-profiles -- Aaron Gable [10 mins]
page: https://datatracker.ietf.org/doc/draft-aaron-acme-profiles/ | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
This document defines how an ACME Server may offer a selection of different certificate profiles to ACME Clients, and how those clients may indicate which profile they want.

### Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0
Draft: draft-demarco-acme-openid-federation · Working group: acme
Agenda: draft-demarco-acme-openid-federation -- Leif Johansson
page: https://datatracker.ietf.org/doc/draft-demarco-acme-openid-federation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-acme-openid-federation-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
The Automatic Certificate Management Environment (ACME) protocol allows server operators to obtain TLS certificates for their websites, based on a demonstration of control over the website's domain via a fully-automated challenge/response protocol. OpenID Federation 1.0 defines how to build a trust infrastructure using a trusted third-party model. It uses a trust evaluation mechanism to attest to the possession of private keys, protocol specific metadata and miscellaneous administrative and technical information related to a specific entity. This document defines how X.509 certificates associated with a given OpenID Federation Entity can be issued by an X.509 Certification Authority through the ACME protocol to the organizations which are part of a federation built on top of OpenID Federation 1.0.

### ACME RATS SLIDES
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-acme-rats-slides-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### Persistent DNS Validation in the ACME protocol
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-birgelee-acme-dns-persist-01-validation-method-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### The Bigger, Huger, Combined Slide Deck
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-acme-the-bigger-huger-combined-slide-deck-00 | video: https://www.youtube.com/watch?v=ALdH73WYSVw | materials: https://datatracker.ietf.org/meeting/123/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

## Working Group: add

### Encrypted DNS Server Redirection
Presentation · Working group: add
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-add-encrypted-dns-server-redirection-00 | video: https://www.youtube.com/watch?v=3WIr5SXXBMQ | materials: https://datatracker.ietf.org/meeting/123/session/add
Slides presented at the add session; no Internet-Draft is linked to them.

## Working Group: anima

### Constrained BRSKI (cBRSKI) and Join Proxy
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-constrained-brski-cbrski-and-join-proxy-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### BRSKI Discovery
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-02-brski-discovery-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### RFC8366bis (VOUCHER) status
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-03-rfc8366bis-voucher-status-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### slides-123-anima-the-constrained-grasp-01
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-slides-123-anima-the-constrained-grasp-01-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Operational Considerations Documents
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-05-operational-considerations-documents-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### ACP free “automation Network Infrastructure” (aNI)
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-06-acp-free-automation-network-infrastructure-ani-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Summary of ANIMA 2025 INTERIM 1
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-anima-07-summary-of-anima-2025-interim-1-00 | video: https://www.youtube.com/watch?v=9DuS3wHLm8w | materials: https://datatracker.ietf.org/meeting/123/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

## Working Group: bess

### BGP MPLS-Based Ethernet VPN
Draft: draft-ietf-bess-rfc7432bis · Working group: bess
Agenda: draft-ietf-bess-rfc7432bis-13 Krishnaswamy 10 14:45 - 14:55
page: https://datatracker.ietf.org/doc/draft-ietf-bess-rfc7432bis/ | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
This document describes procedures for Ethernet VPN (EVPN), a BGP MPLS-based solution which addresses the requirements specified in the corresponding RFC - "Requirements for Ethernet VPN (EVPN)". This document obsoletes RFC7432 (BGP MPLS-Based Ethernet VPN) and updates RFC8214 (Virtual Private Wire Service Support in Ethernet VPN).

### AC-Aware Bundling Service Interface in EVPN
Draft: draft-ietf-bess-evpn-ac-aware-bundling · Working group: bess
Agenda: draft-ietf-bess-evpn-ac-aware-bundling Mankamana 05 14:55 - 15:00
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-ac-aware-bundling/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-ietf-bess-evpn-ac-aware-bundling-01 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
An EVPN (Ethernet VPNs) provides an extensible and flexible multihoming VPN solution over an MPLS/IP network for intra-subnet connectivity among Tenant Systems and End Devices that can be physical or virtual. EVPN multihoming with Integrated Routing and Bridging (IRB) is one of the common deployment scenarios. Some deployments requires the capability to have multiple subnets designated with multiple VLAN IDs in the single broadcast domain. EVPN technology defines three different types of service interface which serve different requirements but none of them address the requirement of supporting multiple subnets within a single broadcast domain. In this document, we define a new service interface type to support multiple subnets in the single broadcast domain. Service interface proposed in this document will be applicable to multihoming cases only.

### Per multicast flow Designated Forwarder Election for EVPN
Draft: draft-ietf-bess-evpn-per-mcast-flow-df-election · Working group: bess
Agenda: draft-ietf-bess-evpn-per-mcast-flow-df-election Mankamana 05 15:00 - 15:05
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-per-mcast-flow-df-election/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-ietf-bess-evpn-per-mcast-flow-df-election-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
This document defines an enhancement to the Designated Forwarder (DF) election process in Ethernet Virtual Private Network (EVPN) environments. While traditional DF election operates at a per Virtual Local Area Network (VLAN) or per group of VLANs (in case of VLAN bundle or VLAN-aware bundle service) level, such granularity may not be sufficient for applications requiring optimized or isolated multicast forwarding. This specification introduces a refined DF election mechanism that extends existing hash-based methods to operate at a more granular level specifically at the tuple of Ethernet Segment Identifier (ESI), VLAN, and multicast flow. This approach enables improved traffic distribution, enhanced load balancing, and greater deployment flexibility for multicast delivery in EVPN based networks. The proposed method is designed to remain compatible with existing DF election procedures while offering targeted improvements for multicast scenarios.

### Weighted Multi-Path Procedures for EVPN Multi-Homing
Draft: draft-ietf-bess-evpn-unequal-lb · Working group: bess
Agenda: draft-ietf-bess-evpn-unequal-lb Neeraj 05 15:05 - 15:10
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-unequal-lb/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-ietf-bess-evpn-unequal-lb-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
Ethernet VPN (EVPN) provides all-active multi-homing for Customer Equipment (CE) devices connected to multiple Provider Edge (PE) devices, enabling equal cost load balancing of both bridged and routed traffic across the set of multi-homing PEs. However, existing procedures implicitly assume equal access bandwidth distribution among the multi-homing PEs, which can constrain link additions or removals and may not handle unequal PE-CE link bandwidth following link failures. This document specifies extensions to EVPN procedures to support weighted multi-pathing in proportion to PE-CE link bandwidth or operator-defined weights, thereby providing greater flexibility and resilience in multi-homing deployments. The extensions include signaling mechanisms to distribute traffic across egress PEs based on relative bandwidth or weight, and enhancements to Broadcast, Unknown Unicast, and Multicast (BUM) designated forwarder (DF) election to achieve weighted DF distribution across the multi- homing PE set.

### EVPN L3-Optimized IRB
Draft: draft-sajassi-bess-evpn-l3-optimized-irb · Working group: bess
Agenda: draft-sajassi-bess-evpn-l3-optimized-irb Chuanfa 05 15:10 - 15:15
page: https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-l3-optimized-irb/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-sajassi-bess-evpn-l3-optimized-irb-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
Ethernet VPN Integrated Routing and Bridging (EVPN-IRB) provides dynamic and efficient intra and inter-subnet connectivity among Tenant Systems and end devices while maintaining very flexible multihoming capabilities. This document describes how EVPN-IRB can be optimized for IP hosts and devices such that PE devices only maintain MAC addresses for locally-connected IP hosts, thus improving MAC scalability of customer bridges and PE devices significantly. This document describes how such optimization is acheived while still supporting host moblity which is one of the fundamental features in EVPN and EVPN-IRB. With such optimization PE devices perform routing for both intra and inter-subnet traffic which results in some some caveats that operators and service providers need to be fully aware of.

### EVPN Underlay Network Migration From IPv4 to IPv6
Draft: draft-sajassi-bess-evpn-fabric-migration · Working group: bess
Agenda: draft-sajassi-bess-evpn-fabric-migration Chuanfa 05 15:15 - 15:20
page: https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-fabric-migration/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-sajassi-bess-evpn-fabric-migration-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
EVPN [RFC7432] and [RFC8365] has become the standard defacto technology/solution used in Enterprise, Data Center, and Service Provider networks because of its multi-tenancy, flexible multi-homing capabilities, efficient utilization of network bandwidth, support of workload mobility, flexible workload placement, etc. across many different types of services/VPNs. Some operators have deployed IPv4 underlay network/fabric and now plan to migrate to IPv6. This document describes the procedures to achieve such migration seamlessly.

### Applications and Procedures for Unknown MAC Route in EVPN
Draft: draft-sajassi-bess-evpn-umr-mobility · Working group: bess
Agenda: draft-sajassi-bess-evpn-umr-mobility-03 Krishnaswamy 10 15:20 - 15:30
page: https://datatracker.ietf.org/doc/draft-sajassi-bess-evpn-umr-mobility/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-sajassi-evpn-umr-mobility-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
The Interconnect Solution for Ethernet VPN defines Unknown MAC (Media Access Control) Route (UMR) utilization for Data Center Interconnect (DCI) when EVPN MPLS or EVPN VXLAN is an overlay network for such interconnects. This scenario impacts MAC mobility procedures and needs to be addressed. This document describes additional changes and enhancements required for MAC mobility procedures when using UMR..

### EVPN Anycast Multi-Homing
Draft: draft-rabnag-bess-evpn-anycast-aliasing · Working group: bess
Agenda: draft-rabnag-bess-evpn-anycast-aliasing-04 Jorge 10 15:30 - 15:40
page: https://datatracker.ietf.org/doc/draft-rabnag-bess-evpn-anycast-aliasing/ | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
The current Ethernet Virtual Private Network (EVPN) all-active multi- homing procedures in Network Virtualization Over Layer-3 (NVO3) networks provide the required Split Horizon filtering, Designated Forwarder Election and Aliasing functions that the network needs in order to handle the traffic to and from the multi-homed CE in an efficient way. In particular, the Aliasing function supports load balancing of unicast traffic from remote Network Virtualization Edge (NVE) devices to NVEs that are multi-homed to the same CE, regardless of whether the CE’s MAC/IP information has been learned on all those NVEs. This document introduces an optional enhancement to the EVPN multi-homing Aliasing function, referred to as EVPN Anycast Multi- homing. This optimization is specific to EVPN deployments over NVO3 tunnels (i.e., IP-based tunnels) and may offer benefits in typical data center designs, which are discussed herein.

### EVPN Inter-Domain Option-B Solution
Draft: draft-rabadan-bess-evpn-inter-domain-opt-b · Working group: bess
Agenda: draft-rabadan-bess-evpn-inter-domain-opt-b-06 Jorge 05 15:40 - 15:45
page: https://datatracker.ietf.org/doc/draft-rabadan-bess-evpn-inter-domain-opt-b/ | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
An EVPN Inter-Domain interconnect solution is required when two or more sites of the same Ethernet Virtual Private Network (EVPN) are connected to different IGP domains or Autonomous Systems (AS) and need to communicate. The Inter-Domain Option-B connectivity model is one of the most popular solutions for this type of EVPN connectivity. While several documents address specific aspects of this interconnect approach, none provide a comprehensive overview of how Inter-Domain Option-B connectivity affects EVPN procedures. This document examines the behavior of EVPN procedures in an Inter-Domain Option-B network and proposes solutions to the identified issues.

### BGP Extensions for the Mobile User Plane (MUP) SAFI
Draft: draft-mpmz-bess-mup-safi · Working group: bess
Agenda: draft-mpmz-bess-mup-safi Keyur Patel 10 15:45 - 15:55
page: https://datatracker.ietf.org/doc/draft-mpmz-bess-mup-safi/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-mpmz-bess-mup-safi-01 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
This document defines a new SAFI known as a BGP Mobile User Plane (BGP-MUP) SAFI to support MUP Extensions and a extended community for BGP. This document also provides BGP signaling and procedures for the new SAFI to convert mobile session information into appropriate IP forwarding information. These extensions can be used by operators between a PE, and a Controller for integrating mobile user plane into BGP MUP network using the IP based routing.

### SRv6 Service SID Anycast Flag
Draft: draft-liu-bess-srv6-service-sid-anycast-flag · Working group: bess
Agenda: draft-liu-bess-srv6-service-sid-anycast-flag Changwang Lin 05 15:55 - 16:00
page: https://datatracker.ietf.org/doc/draft-liu-bess-srv6-service-sid-anycast-flag/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-srv6-service-sid-anycast-flag-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
In some multihoming SRv6 L3VPN and EVPN scenarios, there are requirements for the egress PE to advertise both unicast and anycast SRv6 Service SIDs for the same service. This document defines the Anycast-flag for SRv6 Service SIDs carried in BGP messages.

### Layer-3 Accessible EVPN Services
Draft: draft-wang-bess-l3-accessible-evpn · Working group: bess
Agenda: draft-wang-bess-l3-accessible-evpn Wei 05 16:00 - 16:05
page: https://datatracker.ietf.org/doc/draft-wang-bess-l3-accessible-evpn/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-layer-3-accessible-evpn-services-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
This draft describes layer-3 accessible EVPN service interfaces, which aim is to connect the layer 2 customers to one EVPN backbone, via the layer 3 network, and keep the traffic isolation among different layer 2 customers. It proposes to extend the VxLAN packet format to transfer the customer's Virtual Network Identifier(VNI) information, and also the related control plane extension.

### draft ietf bess rfc 7432 bis
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-draft-ietf-bess-rfc-7432-bis-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### IETF123 BESS bess-evpn-anycast-aliasing04
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-ietf123-bess-bess-evpn-anycast-aliasing04-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

### IETF123 BESS inter-domain-opt-b06
Presentation · Working group: bess
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-bess-ietf123-bess-inter-domain-opt-b06-00 | video: https://www.youtube.com/watch?v=GZUbiMY8VlY | materials: https://datatracker.ietf.org/meeting/123/session/bess
Slides presented at the bess session; no Internet-Draft is linked to them.

## Working Group: cose

### Use of Hybrid Public-Key Encryption (HPKE) with CBOR Object Signing and Encryption (COSE)
Draft: draft-ietf-cose-hpke · Working group: cose
Agenda: [30 min] draft-ietf-cose-hpke - Hannes Tschofenig
page: https://datatracker.ietf.org/doc/draft-ietf-cose-hpke/ | video: https://www.youtube.com/watch?v=NX4g4oUJFPw | materials: https://datatracker.ietf.org/meeting/123/session/cose
This specification defines hybrid public-key encryption (HPKE) for use with CBOR Object Signing and Encryption (COSE). HPKE offers a variant of public-key encryption of arbitrary-sized plaintexts for a recipient public key. HPKE is a general encryption framework utilizing an asymmetric key encapsulation mechanism (KEM), a key derivation function (KDF), and an Authenticated Encryption with Associated Data (AEAD) algorithm. This document defines the use of HPKE with COSE. Authentication for HPKE in COSE is provided by COSE-native security mechanisms or by the pre-shared key authenticated variant of HPKE.

### CBOR Encoded X.509 Certificates (C509 Certificates)
Draft: draft-ietf-cose-cbor-encoded-cert · Working group: cose
Agenda: [15 min] draft-ietf-cose-cbor-encoded-cert - John Mattsson
page: https://datatracker.ietf.org/doc/draft-ietf-cose-cbor-encoded-cert/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-cose-cbor-encoded-x509-certificates-00 | video: https://www.youtube.com/watch?v=NX4g4oUJFPw | materials: https://datatracker.ietf.org/meeting/123/session/cose
This document specifies a CBOR encoding of X.509 certificates. The resulting certificates are called C509 certificates. The CBOR encoding supports a large subset of RFC 5280 and common certificate profiles, and it is extensible. Two types of C509 certificates are defined. One type is an invertible CBOR re-encoding of DER-encoded X.509 certificates with the signature field copied from the DER encoding. The other type is identical except that the signature is computed over the CBOR encoding instead of the DER encoding, thereby avoiding the use of ASN.1. Both types of certificates have the same semantics as X.509 while providing comparable size reduction. This document also specifies CBOR-encoded data structures for certification requests and certification request templates, new COSE headers, as well as a TLS certificate type and a file format for C509. This document updates RFC 6698 by extending the TLSA selectors registry to include C509 certificates.

### COSE HPKE
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-cose-cose-hpke-00 | video: https://www.youtube.com/watch?v=NX4g4oUJFPw | materials: https://datatracker.ietf.org/meeting/123/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

### Dmytro Ochkas - Ascon-AEAD128 for JOSE and COSE
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-cose-dmytro-ochkas-ascon-aead128-for-jose-and-cose-00 | video: https://www.youtube.com/watch?v=NX4g4oUJFPw | materials: https://datatracker.ietf.org/meeting/123/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

### Split Signing Algorithms for COSE
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-cose-split-signing-algorithms-for-cose-01 | video: https://www.youtube.com/watch?v=NX4g4oUJFPw | materials: https://datatracker.ietf.org/meeting/123/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

## Working Group: dnsop

### DNS Filtering Details for Applications
Draft: draft-nottingham-public-resolver-errors · Working group: dnsop
Agenda: Structured Error Data for Filtered DNS / draft-nottingham-public-resolver-errors
page: https://datatracker.ietf.org/doc/draft-nottingham-public-resolver-errors/ | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
[I-D.ietf-dnsop-structured-dns-error] introduces structured error data for DNS responses that have been filtered. This specification allows more specific details of filtering incidents to be conveyed. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/mnot/public-resolver-errors.

### Structured Error Data for Filtered DNS
Draft: draft-ietf-dnsop-structured-dns-error · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-structured-dns-error/ / https://datatracker.ietf.org/doc/draft-nottingham-public-resolver-errors/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-structured-dns-error/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-structured-data-for-filtered-dns-00 | video: https://www.youtube.com/watch?v=cNvR4VuFwMc | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
DNS filtering is widely deployed for various reasons, including network security and policy enforcement. However, filtered DNS responses lack structured information for end users to understand the reason for the filtering. Existing mechanisms to provide explanatory details to end users cause harm especially if the blocked DNS response is for HTTPS resources. This document updates RFC 8914 by signaling client support for structuring the EXTRA-TEXT field of the Extended DNS Error to provide details on the DNS filtering. Such details can be parsed by the client and displayed, logged, or used for other purposes.

### Operational Guidelines for DNS Transport in Mixed IPv4/IPv6 Environments
Draft: draft-ietf-dnsop-3901bis · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-3901bis/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-3901bis/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-draft-ietf-dnsop-3901bis-status-and-next-steps-00 | video: https://www.youtube.com/watch?v=cNvR4VuFwMc | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This document provides guidelines and documents Best Current Practice for operating authoritative DNS servers, recursive resolvers and stub resolvers in a mixed IPv4/IPv6 environment. This document recommends that both authoritative DNS servers and recursive resolvers support IPv4 and IPv6. It also provides guidance on how recursive DNS resolvers should select upstream DNS servers, including when IPv4-embedded IPv6 addresses are available. This document obsoletes RFC 3901.

### Domain Control Validation using DNS
Draft: draft-ietf-dnsop-domain-verification-techniques · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-domain-verification-techniques/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-domain-verification-techniques/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-domain-control-validation-next-steps-00 | video: https://www.youtube.com/watch?v=cNvR4VuFwMc | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
Many application services on the Internet need to verify ownership or control of a domain in the Domain Name System (DNS). The general term for this process is "Domain Control Validation", and it can be done using a variety of methods such as email, HTTP/HTTPS, or the DNS itself. This document focuses only on DNS-based methods, which typically involve the Application Service Provider requesting a DNS record with a specific format and content to be visible in the domain to be verified. There is wide variation in the details of these methods today. This document provides some best practices to avoid known problems.

### Best Practices for Persistent References in DNS
Draft: draft-sheth-identifiers-dns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-sheth-identifiers-dns/
page: https://datatracker.ietf.org/doc/draft-sheth-identifiers-dns/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-best-practices-for-persistent-references-in-dns-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This document details some best practices for Application Service Providers who allow associations between a global DNS domain name and use case specific references using DNSSEC to provide a globally consistent, cryptographically verifiable association. Such a mechanism is needed when nonce-based domain control validation is not practical, such as use cases where each participant wants to confirm the association independently. As such, no single Application Service Provider exists to provide and validate a nonce to prove domain control that would satisfy other participating Application Service Providers.

### Operational Recommendations for DS Automation
Draft: draft-shetho-dnsop-ds-automation · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-shetho-dnsop-ds-automation/
page: https://datatracker.ietf.org/doc/draft-shetho-dnsop-ds-automation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-sessa-operational-recommendations-for-ds-automation-01 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
Enabling support for automatic acceptance of DS parameters from the Child DNS operator (via RFCs 7344, 8078, 9615) requires the parent operator, often a registry or registrar, to make a number of technical decisions. This document describes recommendations for new deployments of such DS automation.

### Service Binding Mapping for Service Levels
Draft: draft-gakiwate-dnsop-svcb-sla-parameter · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-svcb-sla-parameter/
page: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-svcb-sla-parameter/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-service-binding-mapping-for-background-requests-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This document defines a new SvcParamKey for use in Service Binding (SVCB) and HTTPS DNS resource records which enables authoritative DNS servers to indicate that a service should be used by clients having specific service levels or use types, such as "interactive", "background" or "realtime". By providing this information, clients can make informed decisions about which service endpoints to use based on specific applications needs at that time of making connections.

### Multiple Algorithm Rules in DNSSEC
Draft: draft-huque-dnsop-multi-alg-rules · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-huque-dnsop-multi-alg-rules/
page: https://datatracker.ietf.org/doc/draft-huque-dnsop-multi-alg-rules/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-sessa-multiple-algorithm-rules-in-dnssec-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This document restates the requirements on DNSSEC signing and validation and makes small adjustments in order to allow for more flexible handling of configurations that advertise multiple Secure Entry Points (SEP) with different signing algorithms via their DS record or trust anchor set. The adjusted rules allow both for multi- signer operation and for the transfer of signed DNS zones between providers, where the providers support disjoint DNSSEC algorithm sets. In addition, the proposal enables pre-publication of a trust anchor in preparation for an algorithm rollover, such as of the root zone. This document updates RFCs 4035 and 6840.

### Standardized Query Name for DNS Resolver Reachability Probes
Draft: draft-sst-dnsop-probe-name · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-sst-dnsop-probe-name/
page: https://datatracker.ietf.org/doc/draft-sst-dnsop-probe-name/ | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This specification standardizes DNS names that should be used for checking connectivity to a DNS server. About This Document This note is to be removed before publishing as an RFC. Status information for this document may be found at https://datatracker.ietf.org/doc/draft-sst-dnsop-probe-name/. Source for this draft and an issue tracker can be found at https://github.com/bemasc/probe-name.

### Signalling a Zone Cut to Nowhere in the DNS
Draft: draft-jabley-dnsop-zone-cut-to-nowhere · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-jabley-dnsop-zone-cut-to-nowhere/
page: https://datatracker.ietf.org/doc/draft-jabley-dnsop-zone-cut-to-nowhere/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-zone-cut-to-nowhere-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This document defines a standard mechanism to signal the existence of a DNS zone cut without specifying authoritative nameservers for the delegated child zone. This "zone cut to nowhere" is particularly useful in split-horizon environments, allowing parent zones to explicitly signal that a child zone exists but is only resolvable within a private namespace.

### Synchronizing caches of DNS resolvers
Draft: draft-bortzmeyer-dnsop-poisonlicious · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-bortzmeyer-dnsop-poisonlicious/
page: https://datatracker.ietf.org/doc/draft-bortzmeyer-dnsop-poisonlicious/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-synchronizing-caches-of-dns-resolvers-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
Networks of cooperating and mutually trusting DNS resolvers could benefit from cache sharing, where one resolver would distribute the result of a resolution to other resolvers. This document standardizes a protocol to do so.

### Announce Existence of Parent CDS/CSYNC Scanner
Draft: draft-berra-dnsop-announce-scanner · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-berra-dnsop-announce-scanner/
page: https://datatracker.ietf.org/doc/draft-berra-dnsop-announce-scanner/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-announce-scanner-dns-opportunistic-transport-signaling-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
In DNS operations, automated scanners are commonly employed by the operator of a parent zone to detect the presence of specific records, such as CDS or CSYNC, in child zones, indicating a desire for delegation updates. However, the presence and periodicity of these scanners are typically implicit and undocumented, leading to inefficiencies and uncertainties. This document proposes an extension to the semantics of the DSYNC resource record, as defined in [RFC9859], allowing parent zones to explicitly signal the presence and scanning interval of such automated scanners. This enhancement aims to improve transparency and coordination between child and parent zones. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-berra-dnsop-announce-scanner (https://github.com/johanix/draft-berra-dnsop-announce-scanner). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Authoritative DNS Transport Signaling
Draft: draft-johani-dnsop-transport-signaling · Working group: dnsop
Agenda: Datatracker URL: https://datatracker.ietf.org/doc/draft-johani-dnsop-transport-signaling/
page: https://datatracker.ietf.org/doc/draft-johani-dnsop-transport-signaling/ | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
This document proposes a mechanism for authoritative DNS servers to signal their support for alternative transport protocols (e.g., DNS over TLS (DoT), DNS over HTTPS (DoH) and DNS over QUIC (DoQ)). This signaling may either be provided within the Additional section of authoritative DNS responses or be the result of direct DNS queries. The former, "opportunistic mode" is hint-based and aims to enable resolvers to discover alternative transports efficiently and then opportunistically upgrade connections to the authoritative, thereby improving privacy, security, and performance for subsequent interactions. The mechanism is designed to not require any protocol change or additional queries. It is safe, backward-compatible, and effective even when DNSSEC validation of the hint is not possible or desired. In certain circumstances and with additional overhead it is also possible to use direct queries to securely obtain authentication information for the authoritative that can then be used to authenticate an encrypted connection. It is also possible to establish a "validated mode" where the communication between the resolver and the authoritative server is provably both secure and authentic. Validated mode may not always be possible, depending on whether the resolver is able to DNSSEC validate the signal or not. When Validated mode is possible it does provide a stronger and more trustworthy connection. This document proposes an improvement to the opportunistic (but blind) testing of alternative transports suggested in RFC9539 by providing a mechanism by which a responding authoritative server may signal what alternative transports it supports. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-johani-dnsop-transport-signaling (https://github.com/johanix/draft-johani-dnsop-transport-signaling). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### probe.resolver.arpa
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-sessa-proberesolverarpa-00 | video: https://www.youtube.com/watch?v=bpqr1HhVNPM | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### Censorship Transparency
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-dnsop-sessb-censorship-transparency-00 | video: https://www.youtube.com/watch?v=cNvR4VuFwMc | materials: https://datatracker.ietf.org/meeting/123/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

## Working Group: grow

### Peering API
Draft: draft-ietf-grow-peering-api · Working group: grow
Agenda: 10 Arturo Servin draft-ietf-grow-peering-api
page: https://datatracker.ietf.org/doc/draft-ietf-grow-peering-api/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-peering-api-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
We propose an API standard for BGP Peering, also known as interdomain interconnection through global Internet Routing. This API offers a standard way to request public (settlement-free) peering, verify the status of a request or BGP session, and list potential connection locations. The API is backed by PeeringDB OIDC, the industry standard for peering authentication. We also propose future work to cover private peering, and alternative authentication methods.

### Support for BMP RIB Purge Notification
Draft: draft-spd-grow-bmp-purge · Working group: grow
Agenda: 15 Prasad Narasimha draft-spd-grow-bmp-purge
page: https://datatracker.ietf.org/doc/draft-spd-grow-bmp-purge/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-03-ietf123-bmp-rmon-aggregated-multi-peer-common-updates-rib-purge-01 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
This document describes a mechanism to notify a BMP collector of the need to purge the state associated with a RIB view of a specific peer. This is useful, for example, when the BMP sender decides to stop exporting a specific RIB view after providing an initial export. The BMP collector can use the per-peer Purge message to take appropriate action to remove the stale state and avoid holding on to irrelevant network data.

### Common BMP Route-Monitoring Messages for Routes Unchanged by Policy
Draft: draft-patki-grow-bmp-common-updates · Working group: grow
Agenda: draft-patki-grow-bmp-common-updates
page: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
A route unmodified by the inbound policy on a monitored router is included both in Pre-Policy Adj-RIB-In as well as Post-Policy Adj- RIB-In Route-Monitoring messages when both the Pre-Policy and Post- Policy Route-Monitoring modes are enabled. Similarly, a route unmodified by the outbound policy is included in Pre-Policy Adj-RIB- Out as well as Post-Policy Adj-RIB-Out Route-Monitoring messages. This document defines a method to avoid duplicate inclusion of routes unmodified by policy either in Adj-RIB-In or Adj-RIB-Out.

### Definition for Aggregated BMP Route Monitoring Message
Draft: draft-liu-grow-bmp-rm-aggregated · Working group: grow
Agenda: draft-liu-grow-bmp-rm-aggregated
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
This document proposes an aggregated BMP Route Monitoring message based on the BMP Multi-Peer Header message (draft-liu-grow-bmp- multiple-peer-header). It can compress multiple BMP Route Monitoring messages into one aggregated BMP Route Monitoring message to reduce the amount of reported BMP Route Monitoring messages and reduce the network overhead.

### BGP Operations and Security
Draft: draft-ietf-grow-bgpopsecupd · Working group: grow
Agenda: 15 Tobias Fiebig draft-ietf-grow-bgpopsecupd
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bgpopsecupd/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-draft-ietf-grow-bgpopsecupd-et-al-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
The Border Gateway Protocol (BGP) is a critical component in the Internet to exchange routing information between network domains. It is important to understand the security and reliability requirements that can and should be met to prevent accidental or intentional routing disturbances. Previously, security considerations for BGP have been described in RFC7454 / BCP194. Since the publication of RFC7454, changes in operational practice have taken place, which are partially conflicting with the advice given in RFC7454. This document obsoletes RFC7454, and provides less implementation-specific best practices, with the goal of being less prone to becoming outdated or conflicting with changed operational practices.

### Current Options for Securing Global Routing
Draft: draft-ietf-grow-routing-ops-sec-inform · Working group: grow
Agenda: draft-ietf-grow-routing-ops-sec-inform
page: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-sec-inform/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
The Border Gateway Protocol (BGP) is used for exchanging routing information between Autonomous Systems in the Internet. Due to its importance, it is necessary to ensure the basic security properties for BGP and BGP speaking routers. While the general principles for securing BGP operations are outlined in RFC 7454, that document does not detail the technical and implementation options for securing BGP. This document serves as a contemporary, non-exhaustive repository of options and methods for securing BGP. This document explicitly does not make value statements on the efficacy of individual techniques, nor does it mandate or prescribe the use of specific techniques or implementation details. Operators are advised to carefully consider whether the listed methods are applicable for their use-cases. Furthermore, the options listed in this document may change over time, and should not be used as a timeless ground-truth of applicable or sufficient methods.

### Currently Used Terminology in Global Routing Operations
Draft: draft-ietf-grow-routing-ops-terms · Working group: grow
Agenda: draft-ietf-grow-routing-ops-terms
page: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-terms/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
Operating the global routing ecosystem entails a diverse set of interacting components, while operational practice evolved over time. In that time, terms emerged, disappeared, and sometimes changed their meaning. To aid operators and implementers in reading contemporary drafts, this document provides an overview of terms and abbreviations used in the global routing operations community. The document explicitly does not serve as an authoritative source of correct terminology, but instead strives to provide an overview of practice.

### A YANG Data Model for BMP
Draft: draft-ietf-grow-bmp-yang · Working group: grow
Agenda: 15 Camilo Cardona draft-ietf-grow-bmp-yang
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-yang/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
This document defines a YANG data model for the configuration and monitoring of the BGP Monitoring Protocol (BMP).

### BMP Extension for Path Status TLV
Draft: draft-ietf-grow-bmp-path-marking-tlv · Working group: grow
Agenda: draft-ietf-grow-bmp-path-marking-tlv
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-path-marking-tlv/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
The BGP Monitoring Protocol (BMP) provides an interface for obtaining BGP path information, which is conveyed through BMP Route Monitoring (RM) messages. This document specifies a BMP extension to convey the status of a path after being processed by the BGP process.

### A YANG Data Model for BGP Communities
Draft: draft-ietf-grow-yang-bgp-communities · Working group: grow
Agenda: 10 Martin Pels draft-ietf-grow-yang-bgp-communities
page: https://datatracker.ietf.org/doc/draft-ietf-grow-yang-bgp-communities/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-draft-ietf-grow-yang-bgp-communities-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
This document defines a YANG data model for the structured specification of BGP communities. The model provides operators with a way to publish their locally defined BGP communities in a standardized format. Two YANG modules are defined in this document. The first is designed for stand-alone usage. The second is used to augment the "ietf-bgp" YANG module[I-D.ietf-idr-bgp-model] with BGP community annotations. Additionally, this document provides an optional discovery mechanism based on publishing of community definition locations through the Resource Public Key Infrastructure (RPKI).

### BMP Snapshots
Draft: draft-lucente-grow-bmp-offline · Working group: grow
Agenda: 10 Luuk Hendriks draft-lucente-grow-bmp-offline
page: https://datatracker.ietf.org/doc/draft-lucente-grow-bmp-offline/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-draft-lucente-grow-bmp-offline-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
BMP (BGP Monitoring Protocol) is perfectly suited for real-time consumption but less ideal in stream processing and off-wire historical scenarios. The issue is that the necessary information to produce a complete view and enabling correct processing of all messages in the stream, is only sent out at the beginning of the BMP session. This document introduces the concept of BMP Snapshots, enabling BMP stations to synchronize mid-stream, and, providing the basis for self-contained, time-binned archiving of BMP data.

### Logging of routing events in BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-rel · Working group: grow
Agenda: 15 Paolo Lucente draft-ietf-grow-bmp-rel
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
The BGP Monitoring Protocol (BMP) does provide for BGP session event logging (Peer Up, Peer Down), state synchronization (Route Monitoring), debugging (Route Mirroring) and Statistics messages, among others. This document defines a new Route Event Logging (REL) message type for BMP with the aim of covering use cases with affinity to alerting, reporting and on-change analysis.

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-tlv · Working group: grow
Agenda: draft-ietf-grow-bmp-tlv
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-draft-ietf-grow-bmp-tlv-and-draft-ietf-grow-bmp-tlv-ebit-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
Most of the BGP Monitoring Protocol (BMP) message types make provision for data in Type, Length, Value (TLV) format. However, Route Monitoring messages (which provide a snapshot of the monitored Routing Information Base) Stats Reports (which supply periodical counters) and Peer Down messages (which indicate that a peering session was terminated) do not. Supporting (optional) data in TLV format across all BMP message types provides consistent and extensible structures that would be useful among the various use- cases where conveying additional data to a monitoring station is required. This document updates RFC 7854 [RFC7854] to support TLV data in all message types and defines some essential TLVs. Additionally, this document introduces support for enterprise- specific TLVs in the BGP Monitoring Protocol by defining an Enterprise Bit (E-bit) that allows usage of per-vendor Type values.

### Support for Enterprise-specific TLVs in the BGP Monitoring Protocol
Draft: draft-ietf-grow-bmp-tlv-ebit · Working group: grow
Agenda: draft-ietf-grow-bmp-tlv-ebit
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv-ebit/ | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
Message types defined by the BGP Monitoring Protocol (BMP) do provision for data in TLV - Type, Length, Value - format, either in the shape of a TLV message body, ie. Route Mirroring and Stats Reports, or optional TLVs at the end of a BMP message, ie. Peer Up and Peer Down. However the space for Type value is unique and governed by IANA. To allow the usage of vendor-specific TLVs, a mechanism to define per-vendor Type values is required. In this document we introduce an Enterprise Bit, or E-bit, for such purpose.

### Requirements for Monitoring RPKI-Related Processes on Routers Using BMP
Draft: draft-wang-grow-bmp-rpki-mon-reqs · Working group: grow
Agenda: 05 Shuhe Wang draft-wang-grow-bmp-rpki-mon-reqs
page: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-requirements-for-monitoring-rpki-related-processes-on-routers-using-bmp-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
This document outlines requirements for extending the BGP Monitoring Protocol (BMP) to provide comprehensive monitoring of RPKI-related processes on routers, including RPKI data acquisition, RPKI-related policy configuration, route validation, and the impact of validation on routing decisions. The proposed extensions aim to standardize router-side monitoring of RPKI within BMP, focusing specifically on RPKI's effect on BGP routing decisions while maintaining a clear scope boundary with other monitoring mechanisms such as YANG modeling and streaming telemetry for RPKI-to-Router (RTR) protocol operations.

### BMP Sequence Number, Timestamp and Flags TLVs
Draft: draft-younsi-grow-bmp-snts · Working group: grow
Agenda: 15 Pierre Francois draft-younsi-grow-bmp-snts
page: https://datatracker.ietf.org/doc/draft-younsi-grow-bmp-snts/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-ietf123-grow-bmp-snts-and-loc-peer-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
This document defines a Timestamp TLV that carries a timestamp describing one of multiple possible events related to the BMP message. It also defines a Sequence Number TLV which carries the sequence number of the BMP message for the current BMP session. Finally, this document defines an Extended Flags TLV that replaces the Flags field of the Per-Peer Header, allowing more flags to be allocated in BMP.

### The Next Generation of Looking Glass Querying Delegation Platform
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-the-next-generation-of-looking-glass-querying-delegation-platform-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

### Camilo yang
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-camilo-yang-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

### Camilo path marking
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-grow-camilo-path-marking-00 | video: https://www.youtube.com/watch?v=48uXUkRGRvM | materials: https://datatracker.ietf.org/meeting/123/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

## Working Group: httpbis

### CONNECT-TCP
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessa-connect-tcp-00 | video: https://www.youtube.com/watch?v=jd9sGfn0zbM | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP Version Translation of the Capsule Protocol
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessa-http-version-translation-of-the-capsule-protocol-00 | video: https://www.youtube.com/watch?v=jd9sGfn0zbM | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Secondary Certificate Authentication of HTTP Servers
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessa-secondary-certificate-authentication-of-http-servers-00 | video: https://www.youtube.com/watch?v=jd9sGfn0zbM | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Template-Driven HTTP Request Proxying
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessa-template-driven-http-request-proxying-00 | video: https://www.youtube.com/watch?v=jd9sGfn0zbM | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessb-resumable-uploads-00 | video: https://www.youtube.com/watch?v=nIrqcUMvhAk | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Layered Cookies
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-layered-cookies-00 | video: https://www.youtube.com/watch?v=nIrqcUMvhAk | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Incremental HTTP Messages
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessb-incremental-http-messages-00 | video: https://www.youtube.com/watch?v=nIrqcUMvhAk | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Detecting Outdated Proxy Configuration
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-detecting-outdated-proxy-configuration-00 | video: https://www.youtube.com/watch?v=nIrqcUMvhAk | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### Unencoded Digests
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-httpbis-sessb-unencoded-digests-00 | video: https://www.youtube.com/watch?v=nIrqcUMvhAk | materials: https://datatracker.ietf.org/meeting/123/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

## Working Group: idr

### BGP Flowspec Redirects to SR Policy
Draft: draft-li-idr-flowspec-sr-policy · Working group: idr
Agenda: draft-li-idr-flowspec-sr-policy-01
page: https://datatracker.ietf.org/doc/draft-li-idr-flowspec-sr-policy/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-1-bgp-flowspec-redirects-to-sr-policy-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
Extensions to BGP Flowspec Version 1 (FSv1) support steering traffic into a Segment Routing (SR) Policy. This document extends BGP Flowspec Version 2 (FSv2) to provide the same capability of steering traffic into a SR Policy. Using the Community Container attribute, this document defines two new standard actions for FSv2: the Redirect to SR Policy Action and the SRv6 SID Action. The former instructs headend node to direct traffic to a designated SR Policy, while the latter supports simultaneously encapsulating an additional SRv6 SID as required during redirection. The Redirect to SR Policy Action may be used either independently or in conjunction with the SRv6 SID Action, depending on the specific application scenario. In addition, the SRv6 SID Action can be combined with other actions supported by FSv2, such as the Redirect to IPv6 Action.

### BGP SR Policy Extensions for Performance-Aware Path Selection
Draft: draft-li-idr-sr-policy-metric · Working group: idr
Agenda: draft-li-idr-sr-policy-metric-01
page: https://datatracker.ietf.org/doc/draft-li-idr-sr-policy-metric/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-bgp-ls-advertisement-of-sr-policy-performance-metric-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
To enable the headend node to do performance-aware path selection, this document proposes an extension to the BGP SR Policy protocol by defining a new optional Metric Sub-TLV within the BGP Tunnel Encapsulation Attribute. The introduced Metric Sub-TLV encodes performance parameters (such as latency, bandwidth, reliability, etc.) for SR Policy paths. This specification also updates the BGP route selection procedures in RFC4271, modifying the Breaking Ties (Phase 2) logic to prioritize the metrics for SR Policy paths. Key contributions include: * Introduce Metric Sub-TLV in BGP SR Policy * Update the tie-breaking procedure for BGP route selection

### BGP-LS Advertisement of SR Policy Performance Metric
Draft: draft-lin-idr-bgpls-te-policy-pm · Working group: idr
Agenda: draft-lin-idr-bgpls-te-policy-pm-06
page: https://datatracker.ietf.org/doc/draft-lin-idr-bgpls-te-policy-pm/ | materials: https://datatracker.ietf.org/meeting/123/session/idr
This document describes a way to advertise the performance metrics for Traffic Engineering (TE) Policy using BGP Link State (BGP-LS).

### BGP SR Policy Extensions for Path Scheduling
Draft: draft-zzd-idr-sr-policy-scheduling · Working group: idr
Agenda: draft-zzd-idr-sr-policy-scheduling-09
page: https://datatracker.ietf.org/doc/draft-zzd-idr-sr-policy-scheduling/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-1-4-bgp-sr-policy-extensions-for-path-scheduling-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
Segment Routing (SR) policy enables instantiation of an ordered list of segments with a specific intent for traffic steering. When using SR policy in a a network with time-variant characterics or requires high resources utilization efficiency, delivering the time-variant information associated with paths is necessary. This document proposes extensions to BGP SR Policy to deliver the schedule time information of candidate paths and segment lists.

### SRv6 Policy SID List Optimization Advertisement
Draft: draft-ali-idr-srv6-policy-sl-opt-distribution · Working group: idr
Agenda: draft-ali-idr-srv6-policy-sl-opt-distribution-01
page: https://datatracker.ietf.org/doc/draft-ali-idr-srv6-policy-sl-opt-distribution/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-5-srv6-policy-sid-list-optimization-advertisement-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
In some use cases, an SRv6 policy's SID list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This draft specifies a BGP-LS extension to indicate whether the endpoint's node SID is included or excluded in installing SID list(s) of the Candidate Path (CP) of an SRv6 policy.

### Distribution of Device Discovery Information in NVMe Over RoCEv2 Storage Network Using BGP
Draft: draft-wang-idr-bgp-nof-nlri · Working group: idr
Agenda: draft-wang-idr-bgp-nof-nlri-03
page: https://datatracker.ietf.org/doc/draft-wang-idr-bgp-nof-nlri/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-1-6-distribution-of-device-discovery-information-in-nvme-over-rocev2-storage-network-using-bgp-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
This document proposes a method of distributing device discovery information in NVMe over RoCEv2 storage network using the BGP routing protocol. A new BGP Network Layer Reachability Information (NLRI) encoding format, named NoF NLRI, is defined.

### Fully Adaptive Routing Ethernet using BGP
Draft: draft-xu-idr-fare · Working group: idr
Agenda: draft-xu-idr-fare-03
page: https://datatracker.ietf.org/doc/draft-xu-idr-fare/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-7-fully-adaptive-routing-ethernet-using-bgp-02 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
Large language models (LLMs) like ChatGPT have become increasingly popular in recent years due to their impressive performance in various natural language processing tasks. These models are built by training deep neural networks on massive amounts of text data, as well as visual and video data, and often consist of billions or even trillions of parameters. However, the training process for these models can be extremely resource-intensive, requiring the deployment of thousands or even tens of thousands of GPUs in a single AI training cluster. Therefore, three-stage or even five-stage CLOS networks are commonly adopted for AI networks. The non-blocking nature of the network becomes increasingly critical for large-scale AI model training. Therefore, adaptive routing is necessary to dynamically distribute traffic to the same destination across multiple equal-cost paths, based on network capacity information along those paths.

### BGP Performance-aware Routing Mechanism
Draft: draft-ietf-idr-performance-routing · Working group: idr
Agenda: draft-ietf-idr-performance-routing-04
page: https://datatracker.ietf.org/doc/draft-ietf-idr-performance-routing/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-8-bgp-performance-aware-routing-mechanism-01 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
The current Border Gateway Protocol (BGP) specification does not incorporate network performance metrics, such as network latency, into its route selection process. This document outlines a performance-aware BGP routing mechanism that integrates network latency as a critical criterion for route selection. This innovative approach is particularly beneficial for server providers with a global presence, enabling them to offer low-latency network connectivity service as a value-added service to their customers.

### BGP Neighbor Discovery
Draft: draft-xu-idr-neighbor-autodiscovery · Working group: idr
Agenda: draft-xu-idr-neighbor-autodiscovery-12
page: https://datatracker.ietf.org/doc/draft-xu-idr-neighbor-autodiscovery/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-9-bgp-neighbor-discovery-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
BGP is being used as the underlay routing protocol in some large- scaled data centers (DCs). Most popular design followed is to do hop-by-hop external BGP (EBGP) session configurations between neighboring routers on a per link basis. The provisioning of BGP neighbors in routers across such a DC brings its own operational complexity. This document introduces a BGP neighbor discovery mechanism that greatly simplifies BGP operations in such DC and other networks by automatic setup of BGP sessions between neighbor routers using this mechanism.

### Accumulated Metric in NHC attribute
Draft: draft-ietf-idr-bgp-generic-metric · Working group: idr
Agenda: draft-ietf-idr-bgp-generic-metric-01
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-generic-metric/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-10-accumulated-metric-in-nhc-attribute-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
RFC7311 describes mechanism for carrying accumulated IGP cost across BGP domains however it limits to IGP-metric only. There is a need to accumulate and propagate different types of metrics as it will aid in intent-based end-to-end path across BGP domains. This document defines BGP extensions for generic metric sub-types that enable different types of metrics to be accumulated and carried in BGP. This is applicable when multiple domains exchange BGP routing information.

### BGP Specific Route Refresh
Draft: draft-lin-idr-refresh-enhance · Working group: idr
Agenda: draft-lin-idr-refresh-enhance-00
page: https://datatracker.ietf.org/doc/draft-lin-idr-refresh-enhance/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-bgp-specific-route-refresh-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
In certain scenarios, a BGP router may not require its peer to update all routes within an address family, but rather only the specific routes it needs. For example, in an EVPN network, a router might only require updates for all MAC/IP Advertisement Routes or all IP Prefix Advertisement Routes, or even just a subset of IP Prefix routes. This document presents a method for requesting the update of specific routes from a peer, thereby minimizing the impact of additional BGP updates.

### BGP-4 Path Attribute Filtering Capability
Draft: draft-haas-idr-path-attribute-filtering · Working group: idr
Agenda: draft-haas-idr-path-attribute-filtering-00
page: https://datatracker.ietf.org/doc/draft-haas-idr-path-attribute-filtering/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessb-2-2-bgp-4-path-attribute-filtering-capability-00 | video: https://www.youtube.com/watch?v=0ZS7AVUo7aA | materials: https://datatracker.ietf.org/meeting/123/session/idr
Path Attributes in the BGP-4 protocol (RFC 4271) carry data associated with BGP routes. Many of the Path Attributes carried in BGP are intended for limited scope deployment. However, the extension mechanism defined by BGP that carries these attributes often carries them farther than necessary, sometimes with unfortunate results. This document defines a mechanism using BGP Capabilities (RFC 5492) that permits eBGP speakers to determine what Path Attributes should be permitted to cross external BGP routing boundaries.

### Dynamic Capability for BGP-4
Draft: draft-ietf-idr-dynamic-cap · Working group: idr
Agenda: draft-ietf-idr-dynamic-cap-17
page: https://datatracker.ietf.org/doc/draft-ietf-idr-dynamic-cap/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessb-2-3-dynamic-capability-for-bgp-4-00 | video: https://www.youtube.com/watch?v=0ZS7AVUo7aA | materials: https://datatracker.ietf.org/meeting/123/session/idr
This document defines a new BGP capability termed "Dynamic Capability", which would allow the dynamic update of capabilities over an established BGP session. This capability would facilitate non-disruptive capability changes by BGP speakers.

### The Secondary Label and its applications
Draft: draft-mohanty-idr-secondary-label · Working group: idr
Agenda: draft-mohanty-idr-secondary-label-01
page: https://datatracker.ietf.org/doc/draft-mohanty-idr-secondary-label/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-draft-mohanty-idr-secondary-label-00 | video: https://www.youtube.com/watch?v=0ZS7AVUo7aA | materials: https://datatracker.ietf.org/meeting/123/session/idr
This draft utilizes the concept of a secondary label to solve few cases in L3VPN Deployments.In BGP VPN networks, BGP speakers associate a local MPLS label when the next-hop is reset and advertise that label to other peers. The receiving peer installs this "received" label in the forwarding and forwards traffic to the sending router using this label. In some deployments, there arises need where a different label is required to be sent. We illustrate with two use-cases. This draft presents a method where this label is encoded in a newly defined attribute that is advertised with the BGP updates targeting these specified use-cases

### BGP Extensions to Enable BGP FlowSpec based IFIT
Draft: draft-he-idr-bgp-flowspec-ifit · Working group: idr
Agenda: draft-he-idr-bgp-flowspec-ifit-00
page: https://datatracker.ietf.org/doc/draft-he-idr-bgp-flowspec-ifit/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-bgp-extensions-to-enable-bgp-flowspec-based-ifit-01 | video: https://www.youtube.com/watch?v=0ZS7AVUo7aA | materials: https://datatracker.ietf.org/meeting/123/session/idr
Border Gateway Protocol (BGP) Flow Specification (FlowSpec) is an extension to BGP that supports the dissemination of traffic flow specifications and resulting actions to be taken on packets in a specified flow. In-situ Flow Information Telemetry (IFIT) denotes a family of flow-oriented on-path telemetry techniques, which can provide high-precision flow insight and real-time network issue notification. This document defines BGP extensions to distribute BGP FlowSpec based traffic filtering carrying IFIT information. Therefore, IFIT behavior can be automatically applied to the matched flow to capture real-time network dynamics.

### BGP Unreachable Prefix Announcement (UPA)
Draft: draft-krierhorn-idr-upa · Working group: idr
Agenda: draft-krierhorn-idr-upa-00
page: https://datatracker.ietf.org/doc/draft-krierhorn-idr-upa/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessb-2-6-srv6-bgp-unreachable-prefix-announcement-upa-00 | video: https://www.youtube.com/watch?v=0ZS7AVUo7aA | materials: https://datatracker.ietf.org/meeting/123/session/idr
Summarization is often used in multi-domain networks to improve network efficiency and scalability. With summarization in place, there is a need to signal loss of reachability to an individual prefix covered by the summary. This enables fast convergence by steering traffic away from the node which owns the prefix and is no longer reachable. This document specifies the mechanism, referred to as Unreachable Prefix Announcement (UPA), for networks where BGP is used to carry summary routes. It is also equally beneficial for operators to share the unreachable prefixes.

### 2. BGP SR Policy Extensions for Performance-Aware Path Selection
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-sessa-1-2-bgp-sr-policy-extensions-for-performance-aware-path-selection-00 | video: https://www.youtube.com/watch?v=10IP5tTucEU | materials: https://datatracker.ietf.org/meeting/123/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### 1. Making BGP an Internet Standard ("rfc4271bis")
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-idr-making-bgp-an-internet-standard-rfc4271bis-00 | video: https://www.youtube.com/watch?v=0ZS7AVUo7aA | materials: https://datatracker.ietf.org/meeting/123/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

## Working Group: ipsecme

### Enhanced Encapsulating Security Payload (EESP)
Draft: draft-ietf-ipsecme-eesp · Working group: ipsecme
Agenda: draft-ietf-ipsecme-eesp - Steffen Klassert - 10 minutes
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp/ | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document describes the Enhanced Encapsulating Security Payload (EESP) protocol, which builds on the existing IP Encapsulating Security Payload (ESP) protocol. It is designed to modernize and overcome limitations in the ESP protocol. EESP adds Session IDs (e.g., to support CPU pinning and QoS support based on the inner traffic flow), changes some previously mandatory fields to optional, and moves the ESP trailer into the EESP header. Additionally, EESP adds header options adapted from IPv6 to allow for future extension. New header options are defined which add a crypt- offset to allow for exposing inner flow information for middlebox use.

### Optimized Rekeys in the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt · Working group: ipsecme
Agenda: draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt - Wei Pan - 10 minutes
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-sa-ts-payloads-opt/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-use-of-sha-3-in-the-internet-key-exchange-protocol-version-2-ikev2-and-ipsec-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document describes a method for reducing the size of the Internet Key Exchange version 2 (IKEv2) CREATE_CHILD_SA exchanges used for rekeying of the IKE or Child SA by replacing the SA and TS payloads with a Notify Message payload. Reducing size and complexity of IKEv2 exchanges is especially useful for low power consumption battery powered devices.

### ESP Echo Protocol
Draft: draft-ietf-ipsecme-encrypted-esp-ping · Working group: ipsecme
Agenda: draft-ietf-ipsecme-encrypted-esp-ping + BEET mode -= Anthony - 15 minutes
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-encrypted-esp-ping/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-esp-ping-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document defines the ESP Echo Protocol, an extension to the ESP AGGFRAG protocol [RFC9347] that provides an Echo Request and Echo Reply mechanism for IP Security (IPsec) link diagnostics. It enables endpoints to assess end-to-end path reachability, and it defines probe packets that can be used for path Maximum Transmission Unit (MTU) discovery, using Encapsulating Security Payload (ESP) packets. The protocol supports two modes of operation: an encrypted mode used over established IPsec Security Associations (SAs), with an option to specify a preferred reply path when multiple SAs exist between the peers, and an unencrypted mode used outside the context of a negotiated ESP SA. In addition to bidirectional echo probing, the protocol supports sending one-way ESP packets without eliciting a reply, primarily for keepalives, NAT and firewall pinhole maintenance, and unidirectional link diagnostics. A peer can announce support for ESP Echo using a new IKEv2 Status Notification ESP_ECHO_SUPPORTED.

### Prevention Downgrade Attacks on the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-smyslov-ipsecme-ikev2-downgrade-prevention · Working group: ipsecme
Agenda: draft-smyslov-ipsecme-ikev2-downgrade-prevention - Valery / Chris Patton - 15 minutes
page: https://datatracker.ietf.org/doc/draft-smyslov-ipsecme-ikev2-downgrade-prevention/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-draft-smyslov-ipsecme-ikev2-downgrade-prevention-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document describes an extension to the Internet Key Exchange protocol version 2 (IKEv2) that aims to prevent some kinds of downgrade attacks on this protocol by having the peers confirm they have participated in the same conversation.

### Use of SHA-3 in the Internet Key Exchange Protocol Version 2 (IKEv2) and IPsec
Draft: draft-salter-ipsecme-sha3 · Working group: ipsecme
Agenda: draft-salter-ipsecme-sha3 - Ben Salter - 10 minutes
page: https://datatracker.ietf.org/doc/draft-salter-ipsecme-sha3/ | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document specifies the use of KMAC128 and KMAC256 within the Internet Key Exchange Version 2 (IKEv2), Encapsulating Security Payload (ESP), and Authentication Header (AH) protocols. These algorithms can be used as integrity protection algorithms for ESP, AH and IKEv2, and as Pseudo-Random Functions (PRFs) for IKEv2. Requirements for supporting signature algorithms in IKEv2 that use SHA3-256, SHA3-384, SHA3-512, SHAKE128 and SHAKE256 are also specified.

### Post-Quantum Traditional (PQ/T) Hybrid PKI Authentication in the Internet Key Exchange Version 2 (IKEv2)
Draft: draft-hu-ipsecme-pqt-hybrid-auth · Working group: ipsecme
Agenda: draft-hu-ipsecme-pqt-hybrid-auth - Jun Hu - 10 minutes
page: https://datatracker.ietf.org/doc/draft-hu-ipsecme-pqt-hybrid-auth/ | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
One IPsec area that would be impacted by Cryptographically Relevant Quantum Computer (CRQC) is IKEv2 authentication based on traditional asymmetric cryptographic algorithms: e.g RSA, ECDSA, which are widely deployed authentication options of IKEv2. There are new Post-Quantum Cryptographic (PQC) algorithms for digital signature like NIST [ML-DSA], However, it takes time for new cryptographic algorithms to mature, There is security risk to use only the new algorithm before it is field proven. This document describes a hybrid PKI authentication scheme for IKEv2 that incorporates both traditional and PQC digital signature algorithms, so that authentication is secure as long as one algorithm in the hybrid scheme is secure.

### Post-quantum Hybrid Key Exchange with NTRU in the Internet Key Exchange Protocol Version 2 (IKEv2)
Draft: draft-skyline-ipsecme-ntru-ikev2 · Working group: ipsecme
Agenda: draft-skyline-ipsecme-ntru-ikev2 - Yuta Fukagawa - 15 minutes
page: https://datatracker.ietf.org/doc/draft-skyline-ipsecme-ntru-ikev2/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-draft-skyline-ipsecme-ntru-ikev2-00-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document specifies the use of NTRU in the Internet Key Exchange Protocol Version 2 (IKEv2), following the framework defined in RFC 9370. RFC 9370 introduces a mechanism that enables multiple key encapsulation mechanisms (KEMs) to be used within IKEv2, allowing up to seven additional key exchange methods to be negotiated alongside the initial key exchange. This document defines how NTRU can be used as an additional key exchange method to improve the post-quantum security of IKEv2 by broadening algorithmic diversity. [EDNOTE: IANA KE code points for NTRU will be needed to be assigned. ]

### Stateless Encryption Profile for Enhanced Encapsulating Security Payload (EESP)
Draft: draft-xia-ipsecme-eesp-stateless-encryption · Working group: ipsecme
Agenda: draft-xia-ipsecme-eesp-stateless-encryption - Liang Xia - 15 minutes
page: https://datatracker.ietf.org/doc/draft-xia-ipsecme-eesp-stateless-encryption/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-stateless-encryption-scheme-of-eesp-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document specifies a stateless encryption profile for Enhanced Encapsulating Security Payload (EESP). The profile is intended for large-scale deployment scenarios in which maintaining per-flow or per-session encryption state is operationally expensive or infeasible. Instead of storing a distinct data key for each secure flow, endpoints derive per-packet or per-context data keys from a smaller set of provisioned root keying material together with packet- carried context. The document describes the deployment motivation, the stateless keying model, the mapping of required fields onto EESP extension points, context construction rules, data-key derivation processing, IV construction requirements, security considerations, and operational considerations. The intent is to realize stateless encryption as an extension profile over EESP, rather than as a parallel encapsulation format.

### PQuAKE - Post-Quantum Authenticated Key Exchange
Draft: draft-uri-lake-pquake · Working group: ipsecme
Agenda: draft-uri-lake-pquake - Uri Blumenthal - 15 minutes
page: https://datatracker.ietf.org/doc/draft-uri-lake-pquake/ | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
This document defines the Post-Quantum Authenticated Key Exchange (PQuAKE) protocol that addresses the needs of bandwidth- and/or power-constrained environments, while maintaining strong security guarantees. It accomplishes that by minimizing the number of bits that need to be exchanged and by utilizing an implicit peer authentication approach similar to Menezes-Qu-Vanstone (MQV) design. This protocol is suitable for integration into protocols that establish dynamic secure sessions, such as Extensible Authentication Protocol (EAP), Internet Key Exchange Version 2 (IKEv2), or Secure COmmunications Interoperability Protocol (SCIP). This protocol has proofs in the verifiers Verifpal and CryptoVerif for security properties such as secrecy of the session key, mutual authentication, identity hiding with a preshared secret, and forward secrecy of the session key. The authors are in the process of publishing the proofs.

### Enhanced ESP
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-enhanced-esp-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Optimized Rekey in IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-optimized-rekey-in-ikev2-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### IKEv2 BEET Mode
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-ikev2-beet-mode-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Post-Quantum Traditional Hybrid PKI Authentication in IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-post-quantum-traditional-hybrid-pki-authentication-in-ikev2-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### PQuAKE
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-ipsecme-pquake-00 | video: https://www.youtube.com/watch?v=4J49EyZ8kAQ | materials: https://datatracker.ietf.org/meeting/123/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

## Working Group: jose

### Fully-Specified Algorithms for JOSE and COSE
Draft: draft-ietf-jose-fully-specified-algorithms · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-fully-specified-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-fully-specified-algorithms/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This specification refers to cryptographic algorithm identifiers that fully specify the cryptographic operations to be performed, including any curve, key derivation function (KDF), and hash functions, as being "fully specified". It refers to cryptographic algorithm identifiers that require additional information beyond the algorithm identifier to determine the cryptographic operations to be performed as being "polymorphic". This specification creates fully-specified algorithm identifiers for registered JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) polymorphic algorithm identifiers, enabling applications to use only fully-specified algorithm identifiers. It deprecates those polymorphic algorithm identifiers. This specification updates RFC 7518, RFC 8037, and RFC 9053. It deprecates polymorphic algorithms defined by RFC 8037 and RFC 9053 and provides fully-specified replacements for them. It adds to the instructions to designated experts in RFC 7518 and RFC 9053.

### JSON Web Proof
Draft: draft-ietf-jose-json-web-proof · Working group: jose
Agenda: JSON Web Proofs https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-json-web-proof-00 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
The JOSE set of standards established JSON-based container formats for Keys, Signatures, and Encryption. They also established IANA registries to enable the algorithms and representations used for them to be extended. Since those were created, newer cryptographic algorithms that support selective disclosure and unlinkability have matured and started seeing early market adoption. The COSE set of standards likewise does this for CBOR-based containers, focusing on the needs of environments which are better served using CBOR, such as constrained devices and networks. This document defines a new container format similar in purpose and design to JSON Web Signature (JWS) and COSE Signed Messages called a _JSON Web Proof (JWP)_. Unlike JWS, which integrity-protects only a single payload, JWP can integrity-protect multiple payloads in one message. It also specifies a new presentation form that supports selective disclosure of individual payloads, enables additional proof computation, and adds a Presentation Header to prevent replay.

### JSON Proof Algorithms
Draft: draft-ietf-jose-json-proof-algorithms · Working group: jose
Agenda: JSON Proof Algorithms https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
The JSON Proof Algorithms (JPA) specification registers cryptographic algorithms and identifiers to be used with the JSON Web Proof, JSON Web Key (JWK), and COSE specifications. It defines IANA registries for these identifiers.

### JSON Proof Token and CBOR Proof Token
Draft: draft-ietf-jose-json-proof-token · Working group: jose
Agenda: JSON Proof Token https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving representation of claims to be transferred between three parties. The claims in a JPT are encoded as base64url-encoded JSON objects that are used as the payloads of a JSON Web Proof (JWP) structure, enabling them to be digitally signed and selectively disclosed. JPTs also support reusability and unlinkability when using Zero-Knowledge Proofs (ZKPs). A CBOR-based representation of JPTs is also defined, called a CBOR Proof Token (CPT). It has the same properties as JPTs, but uses the JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based JWP Compact Serialization.

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE
Draft: draft-ietf-jose-pqc-kem · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This document describes conventions for using Post-Quantum Key Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and Encryption (COSE).

### JOSE: Deprecate 'none' and 'RSA1_5'
Draft: draft-ietf-jose-deprecate-none-rsa15 · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This document updates RFC 7518 to deprecate the JWS algorithm "none" and the JWE algorithm "RSA1_5". These algorithms have known security weaknesses. It also updates the Review Instructions for Designated Experts to establish baseline security requirements that future algorithm registrations are expected to meet.

### Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)
Draft: draft-ietf-jose-hpke-encrypt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This specification defines how to use Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE). HPKE enables public key encryption of arbitrary-sized plaintexts to a recipient's public key, and provides security against adaptive chosen ciphertext attacks. This specification chooses a specific subset of the HPKE features to use with JWE. This specification updates RFC 7516 (JWE) to enable use of Integrated Encryption as a Key Management Mode.

### Post-Quantum and Hybrid KEMs for HPKE with JOSE and COSE
Draft: draft-reddy-cose-jose-pqc-hybrid-hpke · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-reddy-cose-jose-pqc-hybrid-hpke/
page: https://datatracker.ietf.org/doc/draft-reddy-cose-jose-pqc-hybrid-hpke/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This document specifies the use of Post-Quantum (PQC) and Post- Quantum/Traditional (PQ/T) Hybrid Key Encapsulation Mechanisms (KEMs) within the Hybrid Public Key Encryption (HPKE) for JOSE and COSE. It defines algorithm identifiers and key formats to support pure post- quantum algorithms (ML-KEM) and their PQ/T hybrid combinations.

### Public Key Derived HMAC for JOSE
Draft: draft-bastian-jose-dvs · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-bastian-jose-dvs/
page: https://datatracker.ietf.org/doc/draft-bastian-jose-dvs/ | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This specification defines the use of a Diffie-Hellman key agreement (DH-KA) protocol combined with a key derivation function (KDF) to derive a symmetric Message Authentication Code (MAC) key from public information conveyed within a JSON Web Signature (JWS).

### PQ/T Hybrid Composite Signatures for JOSE and COSE
Draft: draft-prabel-jose-pq-composite-sigs · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-prabel-jose-pq-composite-sigs/
page: https://datatracker.ietf.org/doc/draft-prabel-jose-pq-composite-sigs/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-pqt-hybrid-composite-signatures-for-jose-and-cose-00 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
This document describes JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for PQ/T hybrid composite signatures. The composite algorithms described combine ML-DSA as the post-quantum component and either ECDSA or EdDSA as the traditional component.

### PQ KEMs for COSE AND JOSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-pq-kems-for-cose-and-jose-01 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### BC on JOSE HPKE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-bc-on-jose-hpke-00 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### JOSE HPKE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-jose-hpke-00 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### PQ/T Hybrid KEM: HPKE with JOSE/COSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-pqt-hybrid-kem-hpke-with-josecose-00 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

### Designated Verifier Signatures for JOSE
Presentation · Working group: jose
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-jose-designated-verifier-signatures-for-jose-00 | video: https://www.youtube.com/watch?v=2o7rRgUJjKc | materials: https://datatracker.ietf.org/meeting/123/session/jose
Slides presented at the jose session; no Internet-Draft is linked to them.

## Working Group: lamps

### Related Certificates for Use in Multiple Authentications within a Protocol
Draft: draft-ietf-lamps-cert-binding-for-multi-auth · Working group: lamps
Agenda: a) draft-ietf-lamps-cert-binding-for-multi-auth (RFC 9763)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cert-binding-for-multi-auth/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document defines a new CSR attribute, relatedCertRequest, and a new X.509 certificate extension, RelatedCertificate. The use of the relatedCertRequest attribute in a CSR and the inclusion of the RelatedCertificate extension in the resulting certificate together provide additional assurance that two certificates each belong to the same end entity. This mechanism is particularly useful in the context of non-composite hybrid authentication, which enables users to employ the same certificates in hybrid authentication as in authentication done with only traditional or post-quantum algorithms.

### Use of the HSS and XMSS Hash-Based Signature Algorithms in Internet X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-x509-shbs · Working group: lamps
Agenda: b) draft-ietf-lamps-x509-shbs (RFC 9802)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-shbs/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document specifies algorithm identifiers and ASN.1 encoding formats for the stateful hash-based signature (HBS) schemes Hierarchical Signature System (HSS), eXtended Merkle Signature Scheme (XMSS), and XMSS^MT, a multi-tree variant of XMSS. This specification applies to the Internet X.509 Public Key infrastructure (PKI) when those digital signatures are used in Internet X.509 certificates and certificate revocation lists.

### Guidance on End-to-End E-mail Security
Draft: draft-ietf-lamps-e2e-mail-guidance · Working group: lamps
Agenda: a) draft-ietf-lamps-e2e-mail-guidance (RFC-to-be 9787)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-e2e-mail-guidance/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
End-to-end cryptographic protections for e-mail messages can provide useful security. However, the standards for providing cryptographic protection are extremely flexible. That flexibility can trap users and cause surprising failures. This document offers guidance for mail user agent implementers to help mitigate those risks, and to make end-to-end e-mail simple and secure for the end user. It provides a useful set of vocabulary as well as recommendations to avoid common failures. It also identifies a number of currently unsolved usability and interoperability problems.

### Header Protection for Cryptographically Protected E-mail
Draft: draft-ietf-lamps-header-protection · Working group: lamps
Agenda: b) draft-ietf-lamps-header-protection (RFC-to-be 9788)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-header-protection/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
S/MIME version 3.1 introduced a mechanism to provide end-to-end cryptographic protection of e-mail message headers. However, few implementations generate messages using this mechanism, and several legacy implementations have revealed rendering or security issues when handling such a message. This document updates the S/MIME specification (RFC8551) to offer a different mechanism that provides the same cryptographic protections but with fewer downsides when handled by legacy clients. Furthermore, it offers more explicit usability, privacy, and security guidance for clients when generating or handling e-mail messages with cryptographic protection of message headers. The Header Protection scheme defined here is also applicable to messages with PGP/MIME cryptographic protections.

### Updates to Lightweight OCSP Profile for High Volume Environments
Draft: draft-ietf-lamps-rfc5019bis · Working group: lamps
Agenda: c) draft-ietf-lamps-rfc5019bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5019bis/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This specification defines a profile of the Online Certificate Status Protocol (OCSP) that addresses the scalability issues inherent when using OCSP in large scale (high volume) Public Key Infrastructure (PKI) environments and/or in PKI environments that require a lightweight solution to minimize communication bandwidth and client- side processing. This specification obsoletes RFC 5019. The profile specified in RFC 5019 has been updated to allow and recommend the use of SHA-256 over SHA-1.

### Internet X.509 Public Key Infrastructure -- Certificate Management Protocol (CMP)
Draft: draft-ietf-lamps-rfc4210bis · Working group: lamps
Agenda: d) draft-ietf-lamps-rfc4210bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc4210bis/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document describes the Internet X.509 Public Key Infrastructure (PKI) Certificate Management Protocol (CMP). Protocol messages are defined for X.509v3 certificate creation and management. CMP provides interactions between client systems and PKI components such as a Registration Authority (RA) and a Certification Authority (CA). This document adds support for management of certificates containing a Key Encapsulation Mechanism (KEM) public key and use EnvelopedData instead of EncryptedValue. This document also includes the updates specified in Section 2 and Appendix A.2 of RFC 9480. The updates maintain backward compatibility with CMP version 2 wherever possible. Updates to CMP version 2 are improving crypto agility, extending the polling mechanism, adding new general message types, and adding extended key usages to identify special CMP server authorizations. CMP version 3 is introduced for changes to the ASN.1 syntax, which are support of EnvelopedData, certConf with hashAlg, POPOPrivKey with agreeMAC, and RootCaKeyUpdateContent in ckuann messages. This document obsoletes RFC 4210 and together with I-D.ietf-lamps- rfc6712bis and it also obsoletes RFC 9480. Appendix F of this document updates the Section 9 of RFC 5912.

### Internet X.509 Public Key Infrastructure -- HTTP Transfer for the Certificate Management Protocol (CMP)
Draft: draft-ietf-lamps-rfc6712bis · Working group: lamps
Agenda: e) draft-ietf-lamps-rfc6712bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc6712bis/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document describes how to layer the Certificate Management Protocol (CMP) over HTTP. It includes the updates to RFC 6712 specified in RFC 9480 Section 3. These updates introduce CMP URIs using a Well-known prefix. It obsoletes RFC 6712 and together with I-D.ietf-lamps-rfc4210bis and it also obsoletes RFC 9480.

### Use of Password-Based Message Authentication Code 1 (PBMAC1) in PKCS #12 Syntax
Draft: draft-ietf-lamps-rfc9579bis · Working group: lamps
Agenda: f) draft-ietf-lamps-rfc9579bis
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc9579bis/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document specifies additions and amendments to RFCs 7292 and 8018. It also obsoletes the RFC 9579. It defines a way to use the Password-Based Message Authentication Code 1 (PBMAC1), defined in RFC 8018, inside the PKCS #12 syntax. The purpose of this specification is to permit the use of more modern Password-Based Key Derivation Functions (PBKDFs) and allow for regulatory compliance.

### Use of the SLH-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-sphincs-plus · Working group: lamps
Agenda: g) draft-ietf-lamps-cms-sphincs-plus
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-sphincs-plus/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
SLH-DSA is a stateless hash-based signature scheme. This document specifies the conventions for using the SLH-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### Clarification and enhancement of RFC7030 CSR Attributes definition
Draft: draft-ietf-lamps-rfc7030-csrattrs · Working group: lamps
Agenda: a) draft-ietf-lamps-rfc7030-csrattrs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc7030-csrattrs/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document updates RFC7030, Enrollment over Secure Transport (EST), clarifying how the Certificate Signiing Request (CSR) Attributes Response can be used by an EST server to specify both CSR attribute Object IDs (OID) and also CSR attribute values, in particular X.509 extension values, that the server expects the client to include in subsequent CSR request. RFC9148 is derived from RFC7030, and it is also updated. RFC7030 (EST) is ambiguous in its specification of the CSR Attributes Response. This has resulted in implementation challenges and implementor confusion. As a result, there was not universal understanding of what was specified. This document clarifies the encoding rules. This document therefore also provides a new straightforward approach: using a template for CSR contents that may be partially filled in by the server. This also allows an EST server to specify a subject Distinguished Name (DN).

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA)
Draft: draft-ietf-lamps-dilithium-certificates · Working group: lamps
Agenda: b) draft-ietf-lamps-dilithium-certificates
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
Digital signatures are used within X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using FIPS 204, the Module-Lattice- Based Digital Signature Algorithm (ML-DSA) in Internet X.509 certificates and certificate revocation lists. The conventions for the associated signatures, subject public keys, and private key are also described.

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)
Draft: draft-ietf-lamps-kyber-certificates · Working group: lamps
Agenda: c) draft-ietf-lamps-kyber-certificates
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). This document specifies the conventions for using the ML-KEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for SLH-DSA
Draft: draft-ietf-lamps-x509-slhdsa · Working group: lamps
Agenda: d) draft-ietf-lamps-x509-slhdsa
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-slhdsa/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
Digital signatures are used within X.509 Public Key Infrastructure such as X.509 certificates, Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using the Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) in X.509 Public Key Infrastructure. The conventions for the associated signatures, subject public keys, and private keys are also specified.

### An Attribute for Statement of Possession of a Private Key
Draft: draft-ietf-lamps-private-key-stmt-attr · Working group: lamps
Agenda: f) draft-ietf-lamps-private-key-stmt-attr
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-private-key-stmt-attr/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document specifies an attribute for a statement of possession of a private key by a certificate subject. As part of X.509 certificate enrollment, a Certification Authority (CA) typically demands proof that the subject possesses the private key that corresponds to the to-be-certified public key. In some cases, a CA might accept a signed statement from the certificate subject. For example, when a certificate subject needs separate certificates for signature and key establishment, a statement that can be validated with the previously issued signature certificate for the same subject might be adequate for subsequent issuance of the key establishment certificate.

### Use of the ML-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-ml-dsa · Working group: lamps
Agenda: g) draft-ietf-lamps-cms-ml-dsa
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-ml-dsa/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
The Module-Lattice-Based Digital Signature Algorithm (ML-DSA), as defined by NIST in FIPS 204, is a post-quantum digital signature scheme that aims to be secure against an adversary in possession of a Cryptographically Relevant Quantum Computer (CRQC). This document specifies the conventions for using the ML-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier and public key syntax are provided.

### Unsigned X.509 Certificates
Draft: draft-ietf-lamps-x509-alg-none · Working group: lamps
Agenda: h) draft-ietf-lamps-x509-alg-none
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-x509-alg-none/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document defines a placeholder X.509 signature algorithm that may be used in contexts where the consumer of the certificate is not expected to verify the signature. As part of this, it updates RFC 5280.

### Use of ML-KEM in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-kyber · Working group: lamps
Agenda: i) draft-ietf-lamps-cms-kyber
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-kyber/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). Three parameter sets for the ML-KEM algorithm are specified by the US National Institute of Standards and Technology (NIST) in FIPS 203. In order of increasing security strength (and decreasing performance), these parameter sets are ML-KEM-512, ML-KEM-768, and ML-KEM-1024. This document specifies the conventions for using ML-KEM with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in "Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" (RFC 9629).

### Use of Remote Attestation with Certification Signing Requests
Draft: draft-ietf-lamps-csr-attestation · Working group: lamps
Agenda: a) draft-ietf-lamps-csr-attestation (Mike)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-csr-attestation-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
Certification Authorities (CAs) issuing certificates to Public Key Infrastructure (PKI) end entities may require a certificate signing request (CSR) to include additional verifiable information to confirm policy compliance. For example, a CA may require an end entity to demonstrate that the private key corresponding to a CSR's public key is secured by a hardware security module (HSM), is not exportable, etc. The process of generating, transmitting, and verifying additional information required by the CA is called remote attestation. While work is currently underway to standardize various aspects of remote attestation, a variety of proprietary mechanisms have been in use for years, particularly regarding protection of private keys. This specification defines ASN.1 structures which may carry attestation data for PKCS#10 and Certificate Request Message Format (CRMF) messages. Both standardized and proprietary attestation formats are supported by this specification.

### Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests
Draft: draft-ietf-lamps-attestation-freshness · Working group: lamps
Agenda: b) draft-ietf-lamps-attestation-freshness (Hannes, Hendrik)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
When an end entity includes attestation statements in a Certificate Signing Request (CSR), the freshness of the conveyed Evidence often needs to be established. A common mechanism is a nonce that is obtained from a Relying Party or Verifier and included by the Attester in the Evidence. This document specifies how an end entity requests such an attestation freshness nonce from an RA/CA when using certificate lifecycle management protocols. It defines message formats and protocol bindings for the conveyance of nonce request and response messages in the Certificate Management Protocol (CMP), Enrollment over Secure Transport (EST), and Certificate Management over CMS (CMC), including optional type-specific information needed to produce fresh Evidence for inclusion in a CSR.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-sigs · Working group: lamps
Agenda: c) draft-ietf-lamps-pq-composite-sigs (Mike, John, Max, Jan, Scott)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-composite-sigs-and-kems-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document defines combinations of US NIST Module-Lattice-Based Digital Signature Algorithm (ML-DSA) in hybrid with traditional algorithms RSASSA-PKCS1-v1.5, RSASSA-PSS, ECDSA, Ed25519, and Ed448. These combinations are tailored to meet regulatory guidelines in certain regions. Composite ML-DSA is applicable in applications that use X.509 or PKIX data structures that accept ML-DSA, but where the operator wants extra protection against breaks or catastrophic bugs in ML-DSA, and where existential unforgeability (EUF-CMA) level security is acceptable.

### Clarification to Processing Key Usage Values During Certificate Revocation List (CRL) Validation
Draft: draft-ietf-lamps-keyusage-crl-validation · Working group: lamps
Agenda: d) draft-ietf-lamps-keyusage-crl-validation (Corey)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-keyusage-crl-validation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-draft-ietf-lamps-keyusage-crl-validation-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
RFC 5280 (Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile) defines the profile of X.509 certificates and CRLs for use in the Internet. Section 4.2.1.3 of RFC 5280 requires CRL issuer certificates to contain the keyUsage extension with the cRLSign bit asserted. However, the CRL validation algorithm specified in Section 6.3 of RFC 5280 does not explicitly include a corresponding check for the presence of the keyUsage certificate extension. This document updates RFC 5280 to require that check.

### A Mechanism for X.509 Certificate Discovery
Draft: draft-ietf-lamps-certdiscovery · Working group: lamps
Agenda: e) draft-ietf-lamps-certdiscovery (Corey)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-certdiscovery/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-draft-ietf-lamps-certdiscovery-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document specifies a method to discover a referenced X.509 certificate associated with the current X.509 certificate. This enables efficient multi-certificate or fallback certificate handling in protocols. The objective is threefold: to enhance cryptographic agility, improve operational availability, and accommodate multi-key/ certificate usage. The proposed method aims to maximize compatibility with existing systems and is designed to be legacy- friendly, making it suitable for environments with a mix of legacy and new implementations. It includes mechanisms to provide a URI from which the referenced X.509 certificate can be retrieved as well as information about the target certificate's signature and public key algorithm, empowering relying parties to make informed decisions on whether to retrieve the Referenced Certificate, and a certificate hash to ensure that the correct certificate was retrieved.

### CAA Security Tag for Cryptographically-Constrained Domain Validation
Draft: draft-ietf-lamps-caa-security · Working group: lamps
Agenda: f) draft-ietf-lamps-caa-security (Henry)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-caa-security/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-updates-to-draft-ietf-lamps-caa-security-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
Cryptographic domain validation procedures leverage authenticated communication channels to ensure resilience against attacks by both on-path and off-path network adversaries which attempt to tamper with communications between the Certification Authority (CA) and the network resources related to the domain contained in the certificate. Domain owners can leverage "security" Property Tags specified in CAA records (defined in [RFC8659]) with the critical flag set, to ensure that CAs perform cryptographically-constrained domain validation during their issuance procedure, hence defending against global man- in-the-middle adversaries. This document defines the syntax of the CAA security Property as well as acceptable means for cryptographically-constrained domain validation procedures.

### Composite ML-KEM for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-kem · Working group: lamps
Agenda: a) draft-ietf-lamps-pq-composite-kem (Mike, John)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document defines combinations of US NIST ML-KEM in hybrid with traditional algorithms RSA-OAEP, ECDH, X25519, and X448. These combinations are tailored to meet security best practices and regulatory guidelines. Composite ML-KEM is applicable in any application that uses X.509 or PKIX data structures that accept ML- KEM, but where the operator wants extra protection against breaks or catastrophic bugs in ML-KEM.

### PKCS #8 Private-Key Information Content Types
Draft: draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes · Working group: lamps
Agenda: b) draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes (Joe)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pkcs8-prikeyinfo-contenttypes/ | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document defines PKCS #8 content types for use with PrivateKeyInfo and EncryptedPrivateKeyInfo as specified in RFC 5958.

### Certificate Renewal Recommendations for Enrollment over Secure Transport
Draft: draft-yusef-lamps-rfc7030-renewal-recommendation · Working group: lamps
Agenda: a) draft-yusef-lamps-rfc7030-renewal-recommendation
page: https://datatracker.ietf.org/doc/draft-yusef-lamps-rfc7030-renewal-recommendation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-yusef-lamps-rfc7030-renewal-recommendation-est-renewal-recommendations-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
This document describes an extension to RFC7030, Enrollment over Secure Transport to give an indication to a end-entity device when it should start attempting to renew its certificates. Prior art is that client decides, with a typical recommmendation to start when the remaining lifetime of the certificate is at the 50% point. As typical certificate lifetimes are reduced from years to fractions of a year, the 50% may be far too early, and this document provides a way to give alternate advice.

### Simple Local Web PKI Certificate Resource Preservation Management for Internet Browser
Draft: draft-liu-lamps-browser-webpki-cert-preservation · Working group: lamps
Agenda: b) Penghui Liu's three drafts (draft-liu-lamps-browser-webpki-cert-preservation, draft-liu-lamps-certification-path-validation, draft-liu-lamps-mechanism-updates-to-rfc-5280)
page: https://datatracker.ietf.org/doc/draft-liu-lamps-browser-webpki-cert-preservation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-framework-and-requirements-for-localized-management-of-trusted-web-pki-certificate-supporting-fine-grained-configuration-for-int-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
The management of Web PKI certificate resources presents a challenge when the misalignment of ownership and management rights over certificate resources of one organization creating a risk of unilateral suspension and revocation by another competing organizations. This situation undermines the stability of critical infrastructure and affects the integrity of authentication systems. To address these concerns, this document proposes a mechanism that allows Internet browsers to create a customized management view of certificate resources, enabling them to override the verification results from specific certification authorities as needed. This approach enhances security, facilitates stakeholder collaboration, and preserves the operational integrity of foundational industry systems.

### Technical guidelines of Web server certification path validation for Interent browser
Draft: draft-liu-lamps-certification-path-validation · Working group: lamps
Agenda: b) Penghui Liu's three drafts (draft-liu-lamps-browser-webpki-cert-preservation, draft-liu-lamps-certification-path-validation, draft-liu-lamps-mechanism-updates-to-rfc-5280)
page: https://datatracker.ietf.org/doc/draft-liu-lamps-certification-path-validation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-draft-liu-lamps-certification-path-validationupdate-01 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
In Web PKI, certificate path construction and validation are crucial security review processes. At present, there are many Internet browser manufacturers around the world. With the change of security practices and the development of technology, the certificate validation process in Internet browser industry is relatively messy, including various private implementations of manufacturers. It is a typical patching improvement method, and the implementation of process functions is relatively arbitrary. This document provides a technical guide for certification path validation of web server certificates during Internet SSL/TLS protocol communication for Web PKI, including the basic path verification process, as well as reference procedures, guidance and suggestions for input, initialization, and basic certificate processing in the verification process. This document is applicable to the development and application of Internet browsers, as well as other similar digital certificate authentication systems requiring SSL/TLS security protocol secure communication.

### Certificate Status Information Mechanism Description Updates to RFC 5280
Draft: draft-liu-lamps-mechanism-updates-to-rfc-5280 · Working group: lamps
Agenda: b) Penghui Liu's three drafts (draft-liu-lamps-browser-webpki-cert-preservation, draft-liu-lamps-certification-path-validation, draft-liu-lamps-mechanism-updates-to-rfc-5280)
page: https://datatracker.ietf.org/doc/draft-liu-lamps-mechanism-updates-to-rfc-5280/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-draft-liu-lamps-mechanism-updates-to-rfc-5280update-01 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
The updates to RFC 5280 described in this document provide alignment with the 2013 specification for the X.509 Internet Public Key Infrastructure Online Certificate Status Protocol-OCSP [RFC6960].

### Falko: Discussion of PKCS#11 v3.2 proposal
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lamps-falko-discussion-of-pkcs11-v32-proposal-00 | video: https://www.youtube.com/watch?v=YrP-zck5z0E | materials: https://datatracker.ietf.org/meeting/123/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

## Working Group: lsr

### Flooding Reduction Algorithms Framework
Draft: draft-ietf-lsr-isis-flood-reduction-arch · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-flood-reduction-arch/
page: https://datatracker.ietf.org/doc/draft-ietf-lsr-isis-flood-reduction-arch/ | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
This document introduces a framework to deploy multiple flood reduction algorithms within the same IGP domain in an interoperable fashion.

### IS-IS Distributed Flooding Reduction
Draft: draft-ietf-lsr-distoptflood · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ietf-lsr-distoptflood/
page: https://datatracker.ietf.org/doc/draft-ietf-lsr-distoptflood/ | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
In dense topologies (such as data center fabrics based on the Clos and butterfly though not limited to those; in fact any large topology or one with relatively high degree of connectivity qualifies here) IGP flooding mechanisms designed originally for rather sparse topologies can "overflood", or in other words generate too many identical copies of same information arriving at a given node from other devices. This normally results in longer convergence times and higher resource utilization to process and discard the superfluous copies. Flooding algorithm extensions that restrict the amount of flooding performed can be constructed and can reduce resource utilization significantly, while improving convergence performance. One such flooding modification (based on previous art) optimized for operational considerations, described further in Section 2, is described in this document.

### ISIS Hierarchical SNPs
Draft: draft-prz-lsr-hierarchical-snps · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-prz-lsr-hierarchical-snps/
page: https://datatracker.ietf.org/doc/draft-prz-lsr-hierarchical-snps/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-hierarchical-snps-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
The document presents an optional new type of SNP called a Hierarchical SNP (HSNP). When feasible, it compresses traditional CSNP exchanges into a Merkle tree-like structure, which speeds up synchronization of large databases and adjacency numbers while reducing the load from regular CSNP exchanges during normal operation.

### Energy-aware Routing Using Flex-Algo in Segment Routing
Draft: draft-ralc-lsr-energy-aware-routing · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ralc-lsr-energy-aware-routing/
page: https://datatracker.ietf.org/doc/draft-ralc-lsr-energy-aware-routing/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-05-energy-aware-routing-using-flex-algo-in-segment-routing-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
This document proposes enhancements to the Segment Routing (SR) Flexible Algorithm (Flex-Algo) framework by integrating power consumption metrics into routing decisions. It introduces metrics encompassing both node-level and link-level energy consumption attributes and proposes dynamic energy-aware path computation. By incorporating these metrics alongside traditional routing parameters, the enhanced Flex-Algo framework can enable networks to optimize routing paths for energy efficiency, and then leverage on advances router capabilities to further reduce operational costs as well as supporting sustainability objectives.

### Flexible Algorithms for Energy Efficiency
Draft: draft-li-lsr-flex-algo-energy-efficiency · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-li-lsr-flex-algo-energy-efficiency/
page: https://datatracker.ietf.org/doc/draft-li-lsr-flex-algo-energy-efficiency/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-flexible-algorithms-for-energy-efficiency-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
[draft-liu-spring-sr-policy-energy-efficiency-00] describes how energy consumption information is utilized for path selection in Segment Routing (SR) networks. This document elaborates on extending IGP protocols to carry energy consumption information, enabling its dissemination within the IGP domain and ultimately transmitting it to the controller. This allows the controller to perform routing calculations based on energy consumption metrics.

### Advertising SRv6 SIDs for Layer 2 Bundle Member Links in IGP
Draft: draft-dong-lsr-l2bundle-srv6 · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-dong-lsr-l2bundle-srv6/
page: https://datatracker.ietf.org/doc/draft-dong-lsr-l2bundle-srv6/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-07-srv6-sid-l2bundle-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
There are deployments where the Layer-3 interface on which IGP operates is a Layer-2 interface bundle. Existing IGP advertisements only support advertising link attributes of the Layer-3 interface. If entities external to IGP wish to control traffic flows on the individual physical links that comprise the Layer-2 interface bundle, link attribute information about the bundle members is advertised by IGP extensions for Layer-2 (L2) bundle. When Segment Routing over IPv6 (SRv6) is used with Layer-2 interface bundle to control traffic flows on the individual member links, the SRv6 SIDs which represent the Layer 2 member links of the L2 bundle needs to be advertised in IGP. This document proposes the IGP extensions to advertise the SRv6 SIDs of the Layer 2 (L2) bundle member links.

### OSPF Adjacency Suppression
Draft: draft-cheng-lsr-ospf-adjacency-suppress · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-cheng-lsr-ospf-adjacency-suppress/
page: https://datatracker.ietf.org/doc/draft-cheng-lsr-ospf-adjacency-suppress/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-08-ospf-adjacency-suppression-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
This document describes a mechanism for a router to instructs its neighbors to suppress advertising the adjacency to it until link- state database synchronization and LSA reoriginating are complete. This minimizes transient routing disruption when a router restarts from unplanned outages.

### Problem Statement, Gap Analysis, and Requirements for Intra-domain Source Address Validation
Draft: draft-ietf-savnet-intra-domain-problem-statement · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-problem-statement/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-09-source-address-validation-in-intra-domain-networks-gap-analysis-problem-statement-and-requirements-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
Source address validation (SAV) is an important means to mitigate IP source address spoofing [RFC2827]. This document analyzes the gaps in current operational mechanisms for intra-domain SAV. It also identifies the properties that new intra-domain SAV mechanisms are expected to provide.

### LSR status
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-01-lsr-status-02 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### distributed flood reduction measurements
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-distributed-flood-reduction-measurements-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### distributed flood reduction update
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-lsr-distributed-flood-reduction-update-00 | video: https://www.youtube.com/watch?v=YdkfNAYJz24 | materials: https://datatracker.ietf.org/meeting/123/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

## Working Group: masque

### QUIC-Aware Proxying Using HTTP
Draft: draft-ietf-masque-quic-proxy · Working group: masque
Agenda: IPR Disclosure related to draft-ietf-masque-quic-proxy
page: https://datatracker.ietf.org/doc/draft-ietf-masque-quic-proxy/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-masque-quic-aware-proxying-using-http-00 | video: https://www.youtube.com/watch?v=N4yhFyITbJo | materials: https://datatracker.ietf.org/meeting/123/session/masque
This document extends UDP Proxying over HTTP to add optimizations for proxied QUIC connections. Specifically, it allows a proxy to reuse UDP 4-tuples for multiple proxied connections, and adds a mode of proxying in which QUIC short header packets can be forwarded and transformed through a HTTP/3 proxy rather than being fully re- encapsulated and re-encrypted.

### CONNECT-UDP Bind
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-masque-connect-udp-bind-00 | video: https://www.youtube.com/watch?v=N4yhFyITbJo | materials: https://datatracker.ietf.org/meeting/123/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### CONNECT-ETHERNET
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-masque-connect-ethernet-00 | video: https://www.youtube.com/watch?v=N4yhFyITbJo | materials: https://datatracker.ietf.org/meeting/123/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### DNS Configuration for Proxying IP in HTTP
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-masque-dns-configuration-for-proxying-ip-in-http-01 | video: https://www.youtube.com/watch?v=N4yhFyITbJo | materials: https://datatracker.ietf.org/meeting/123/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### ECN and DSCP for Connect-UDP
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-masque-ecn-and-dscp-for-connect-udp-01 | video: https://www.youtube.com/watch?v=N4yhFyITbJo | materials: https://datatracker.ietf.org/meeting/123/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

### The MASQUE Proxy
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-masque-the-masque-proxy-00 | video: https://www.youtube.com/watch?v=N4yhFyITbJo | materials: https://datatracker.ietf.org/meeting/123/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

## Working Group: oauth

### SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)
Draft: draft-ietf-oauth-sd-jwt-vc · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessb-sd-jwt-vc-02 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification describes data formats as well as validation and processing rules to express Verifiable Digital Credentials with JSON payloads with and without selective disclosure based on the SD-JWT format.

### Updates to OAuth 2.0 JSON Web Token (JWT) Client Authentication and Assertion-Based Authorization Grants
Draft: draft-ietf-oauth-rfc7523bis · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/ | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This document updates RFC7521, RFC7522, RFC7523 and RFC9126 with respect to the treatment of audience values in OAuth 2.0 Client Assertion Authentication and Assertion-based Authorization Grants to address a security vulnerability identified in the previous requirements for those audience values in multiple OAuth 2.0 specifications.

### Updates to OAuth 2.0 Security Best Current Practice
Draft: draft-wuertele-oauth-security-topics-update · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-wuertele-oauth-security-topics-update/01/
page: https://datatracker.ietf.org/doc/draft-wuertele-oauth-security-topics-update/ | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This document updates the set of best current security practices for OAuth 2.0 by extending the security advice given in RFC 6749, RFC 6750, and RFC 9700, to cover new threats that have been discovered since the former documents have been published.

### JSON Web Token Best Current Practices
Draft: draft-sheffer-oauth-rfc8725bis · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-sheffer-oauth-rfc8725bis/
page: https://datatracker.ietf.org/doc/draft-sheffer-oauth-rfc8725bis/ | materials: https://datatracker.ietf.org/meeting/123/session/oauth
JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security tokens that contain a set of claims that can be signed and/or encrypted. JWTs are being widely used and deployed as a simple security token format in numerous protocols and applications, both in the area of digital identity and in other application areas. This Best Current Practices document updates RFC 7519 to provide actionable guidance leading to secure implementation and deployment of JWTs.

### OAuth Identity and Authorization Chaining Across Domains
Draft: draft-ietf-oauth-identity-chaining · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessb-oauth-identity-and-authorization-chaining-across-domains-00 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification describes a mechanism for preserving identity and authorization information across trust domains that use the OAuth 2.0 Framework. A JSON Web Token (JWT) authorization grant, obtained through an intra-domain OAuth 2.0 Token Exchange, facilitates the cross-domain acquisition of an access token. The relevant identity and authorization information is chained throughout the flow by being conveyed in the respective artifacts exchanged at each step of the process. Chaining across multiple domains is achieved by using the same protocol every time a trust domain boundary is crossed.

### OAuth 2.0 Client ID Prefix
Draft: draft-parecki-oauth-client-id-prefix · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-parecki-oauth-client-id-prefix/
page: https://datatracker.ietf.org/doc/draft-parecki-oauth-client-id-prefix/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessb-client-id-prefix-02 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification defines the concept of a Client Identifier Prefix to enable Authorization Servers and Clients to use more than one mechanism to obtain and validate Client metadata.

### OAuth 2.0 Dynamic Client Registration with Trusted Issuer Credentials
Draft: draft-kasselman-oauth-dcr-trusted-issuer-token · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-kasselman-oauth-dcr-trusted-issuer-token/
page: https://datatracker.ietf.org/doc/draft-kasselman-oauth-dcr-trusted-issuer-token/ | materials: https://datatracker.ietf.org/meeting/123/session/oauth
An OAuth 2.0 client requires specific information to interact with an authorization server, including a client identifier registered with the authorization server. The OAuth 2.0 Dynamic Client Registration Protocol [RFC7591] defines a mechansim for dynamic client registration that removes the need for manual registration. This provides a more scalable mechanism that can be used by clients that do not have a pre-existing relationship with an authorization server, or where manually configuring such relationships is prohibitive from a cost and scale perspective. Examples of deployments that benefit from dynamic client registration includes modern cloud architectures where microservices are created on demand to meet scale requirements or for use with emerging protocols like the Model Context Protocol (MCP) [MCP] which requires clients to register with an authorization server even if they do not have a predefined relationship with the authorization server. Similar to modern cloud native workloads, MCP service integrations may be ephemeral in nature. The OAuth 2.0 Dynamic Client Registration Protocol [RFC7591] defines a software statement that includes metadata about the client and is signed by a developer or trusted third party. This specification describes the use of specific third party credentials issued to workloads and applications as software statements. The specification describes two types of credentials that may be used as software statements. The first is Secure Production Identity Framework For Everyone (SPIFFE) credentials. The second is the use of JWT representation of a Verifiable Credentials [VC-JWT]

### OAuth Client Registration on First Use with SPIFFE
Draft: draft-kasselman-oauth-spiffe · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-kasselman-oauth-spiffe/
page: https://datatracker.ietf.org/doc/draft-kasselman-oauth-spiffe/ | materials: https://datatracker.ietf.org/meeting/123/session/oauth
The OAuth framework is a widely deployed authorization protocol standard that enables applications to obtain limited access to user resources. OAuth clients must be registered with the OAuth authorization server, which poses significant operational challenges in dynamically scaling environments. The Secure Production Identity Framework For Everyone (SPIFFE) is a graduated Cloud Native Compute Foundation project designed to dynamically attest and verify workload identity. This draft describes how workloads with SPIFFE credentials can be used with OAuth to lessen the operational burden of client registration through a "register on first use" principle.

### OAuth SPIFFE Client Authentication
Draft: draft-schwenkschuster-oauth-spiffe-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/
page: https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-oauth-spiffe-client-authentication-01 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification profiles the Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants [RFC7521] and JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants [RFC7523] to enable the use of SPIFFE Verifiable Identity Documents (SVIDs) as client credentials in OAuth 2.0. It defines how OAuth clients with SPIFFE credentials can authenticate to OAuth authorization servers using their JWT-SVIDs or X.509-SVIDs without the need for client secrets. This approach enhances security by enabling seamless integration between SPIFFE-enabled workloads and OAuth authorization servers while eliminating the need to distribute and manage shared secrets such as static client secrets.

### Token Status List (TSL)
Draft: draft-ietf-oauth-status-list · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessa-ietf-123-token-status-list-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification defines a status mechanism called Token Status List (TSL), data structures and processing rules for representing the status of tokens secured by JSON Object Signing and Encryption (JOSE) or CBOR Object Signing and Encryption (COSE), such as JWT, SD-JWT, CBOR Web Token, and ISO mdoc. It also defines an extension point and a registry for future status mechanisms.

### OAuth 2.0 Attestation-Based Client Authentication
Draft: draft-ietf-oauth-attestation-based-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessa-ietf-123-attestation-based-client-authentication-01 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification defines an extension to the OAuth 2.0 protocol (RFC 6749) that enables a client instance to include a key-bound attestation when interacting with an Authorization Server or Resource Server. This mechanism allows a client instance to prove its authenticity, as verified by a client attester, without revealing its target audience to that attester. It may also serve as a mechanism for client authentication as per OAuth 2.0.

### Transaction Tokens
Draft: draft-ietf-oauth-transaction-tokens · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-ietf-123-transaction-tokens-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Transaction Tokens (Txn-Tokens) are designed to maintain and propagate user identity, workload identity and authorization context throughout the Call Chain within a trusted domain during the processing of external requests (e.g. such as API calls) or requests initiated internally within the Trust Domain. Txn-Tokens ensure that this context is preserved throughout the Call Chain thereby enhancing security and consistency in complex, multi-service architectures.

### OAuth 2.0 Refresh Token and Authorization Expiration
Draft: draft-watson-oauth-refresh-token-expiration · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-watson-oauth-refresh-token-expiration/
page: https://datatracker.ietf.org/doc/draft-watson-oauth-refresh-token-expiration/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-refresh-token-expiration-rich-errors-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification extends OAuth 2.0 [RFC6749] by adding new token endpoint response parameters to specify refresh token expiration and user authorization expiration.

### OAuth 2.0 App2App Browser-less Flow
Draft: draft-zehavi-oauth-app2app-browserless · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-zehavi-oauth-app2app-browserless/
page: https://datatracker.ietf.org/doc/draft-zehavi-oauth-app2app-browserless/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-app2app-browser-less-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This document describes a protocol allowing a _Client App_ to obtain an OAuth grant from an _Authorization Server's Native App_ using the [App2App] pattern, providing *native* app navigation user-experience (no web browser used), despite both apps belonging to different trust domains.

### OAuth 2.0 client extension claims
Draft: draft-lombardo-oauth-client-extension-claims · Working group: oauth
Agenda: https://github.com/identitymonk/draft-lombardo-oauth-client-extension-claims
page: https://datatracker.ietf.org/doc/draft-lombardo-oauth-client-extension-claims/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-ietf123-draft-oauth-client-extension-claims-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification defines new claims for JWT profiled access tokens [RFC9068] so that resource providers can benefit from more granular information about the client: its authentication methods as well as the grant flow and the grant flow extensions used as part of the issuance of the associated tokens.

### OAuth 2.0 step-up authorization challenge proto
Draft: draft-lombardo-oauth-step-up-authz-challenge-proto · Working group: oauth
Agenda: https://github.com/identitymonk/draft-lombardo-oauth-step-up-authz-challenge-proto
page: https://datatracker.ietf.org/doc/draft-lombardo-oauth-step-up-authz-challenge-proto/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-ietf123-draft-oauth-step-up-authorization-challenge-protocol-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
It is not uncommon for resource servers to require additional information like details of delegation authorization, or assurance proof of the delegation of authorization mechanism used according to the characteristics of a request. This document introduces a mechanism that resource servers can use to signal to a client that the data and metadata associated with the access token of the current request does not meet its authorization requirements and, further, how to meet them. This document also codifies a taxonomy to guide the client into starting a new request towards the authorization server in order to get issued, if applicable, a new set of tokens matching the requirements.

### OAuth Pushed Client Registration
Draft: draft-richer-oauth-pushed-client-registration · Working group: oauth
Agenda: https://www.ietf.org/archive/id/draft-richer-oauth-pushed-client-registration-00.html
page: https://datatracker.ietf.org/doc/draft-richer-oauth-pushed-client-registration/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-pushed-client-registration-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
This specification provides a way for an ephemeral or transactional OAuth 2.0 client to signal to the AS that the client does not need or expect to have an identified state outside the existence of any issued access and refresh tokens. The specification also enables a client to push its registration information to the AS during a pushed authorization request.

### Deferred Key Binding for OAuth
Draft: draft-richer-oauth-tmb-claim · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-richer-oauth-tmb-claim/
page: https://datatracker.ietf.org/doc/draft-richer-oauth-tmb-claim/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-deferred-token-binding-trust-me-bruh-00 | video: https://www.youtube.com/watch?v=rsPrpr-5MPI | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Sometimes you want to get a token that's tied to a public key but you can't prove possession of that public key. That's when you need to trust me, bruh.

### AI Authorization (aauth)
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-ai-authorization-aauth-00 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Updates to Audience Values
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessb-updates-to-audience-values-00 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Security BCP Updates
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-sessb-security-bcp-updates-00 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### JWT BCP
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-jwt-bcp-01 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Refresh Token and Consent Expiration
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-refresh-token-and-consent-expiration-00 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Automatic OAuth Client Registration - Final
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-oauth-automatic-oauth-client-registration-final-00 | video: https://www.youtube.com/watch?v=2XQVPrNdDtc | materials: https://datatracker.ietf.org/meeting/123/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

## Working Group: pquip

### Hybrid signature spectrums
Draft: draft-ietf-pquip-hybrid-signature-spectrums · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-ietf-pquip-hybrid-signature-spectrums/
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-hybrid-signature-spectrums/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-pquip-ietf-123-signature-spectrums-slides-01 | video: https://www.youtube.com/watch?v=vLlekahKwx4 | materials: https://datatracker.ietf.org/meeting/123/session/pquip
This document describes classification of design goals and security considerations for hybrid digital signature schemes, including proof composability, non-separability of the component signatures given a hybrid signature, backwards/forwards compatibility, hybrid generality, and simultaneous verification.

### Post-Quantum Cryptography for Engineers
Draft: draft-ietf-pquip-pqc-engineers · Working group: pquip
Agenda: draft-ietf-pquip-pqc-engineers
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-engineers/ | video: https://www.youtube.com/watch?v=vLlekahKwx4 | materials: https://datatracker.ietf.org/meeting/123/session/pquip
The advent of a cryptographically relevant quantum computer (CRQC) would render state-of-the-art, traditional public key algorithms deployed today obsolete, as the mathematical assumptions underpinning their security would no longer hold. To address this, protocols and infrastructure must transition to post-quantum algorithms, which are designed to resist both traditional and quantum attacks. This document explains why engineers need to be aware of and understand post-quantum cryptography (PQC), detailing the impact of CRQCs on existing systems and the challenges involved in transitioning to post-quantum algorithms. Unlike previous cryptographic updates, this shift may require significant protocol redesign due to the unique properties of post-quantum algorithms.

### Hash-based Signatures: State and Backup Management
Draft: draft-ietf-pquip-hbs-state · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-ietf-pquip-hbs-state/
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-hbs-state/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-pquip-draft-ietf-pquip-hbs-state-00 | video: https://www.youtube.com/watch?v=vLlekahKwx4 | materials: https://datatracker.ietf.org/meeting/123/session/pquip
Stateful Hash-Based Signature Schemes (Stateful HBS) such as Leighton-Micali Signature (LMS), Hierarchical Signature System (HSS), eXtended Merkle Signature Scheme (XMSS), and XMSS^MT combine Merkle trees with One-Time Signatures (OTS) to provide signatures that are resistant against attacks using large-scale quantum computers. Unlike conventional stateless digital signature schemes, Stateful HBS have a state to keep track of which OTS keys have been used, as double-signing with the same OTS key allows forgeries. This document provides guidance and catalogs security considerations for the operational and technical aspects of deploying systems that rely on Stateful HBS. Management of the state of the Stateful HBS, including any handling of redundant key material, is a sensitive topic. This document describes some approaches to handle the associated challenges. It also describes the challenges that need to be resolved before certain approaches should be considered.

### Adapting Constrained Devices for Post-Quantum Cryptography
Draft: draft-ietf-pquip-pqc-hsm-constrained · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/
page: https://datatracker.ietf.org/doc/draft-ietf-pquip-pqc-hsm-constrained/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-pquip-draft-ietf-pquip-pqc-hsm-constrained-02 | video: https://www.youtube.com/watch?v=vLlekahKwx4 | materials: https://datatracker.ietf.org/meeting/123/session/pquip
This document provides guidance on integrating Post-Quantum Cryptography (PQC) into resource-constrained devices, such as IoT nodes and dedicated key-storage hardware. These systems often operate with strict limitations on processing power, RAM, and flash memory, and may even be battery-powered. The document emphasizes the role of hardware security as the basis for secure operations, supporting features such as seed-based key generation to minimize persistent storage, efficient handling of ephemeral keys, and the offloading of cryptographic tasks in low-resource environments. It also explores the implications of PQC on firmware update mechanisms in such constrained systems.

### Post-Quantum Algorithms guidance
Draft: draft-prabel-pquip-pqc-guidance · Working group: pquip
Agenda: https://datatracker.ietf.org/doc/draft-prabel-pquip-pqc-guidance/
page: https://datatracker.ietf.org/doc/draft-prabel-pquip-pqc-guidance/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-pquip-post-quantum-algorithms-guidance-01 | video: https://www.youtube.com/watch?v=vLlekahKwx4 | materials: https://datatracker.ietf.org/meeting/123/session/pquip
This document provides general information (such as parameter sizes, security assumptions, and targeted security models) on a range of widely studied post-quantum cryptographic algorithms, including Key Encapsulation Mechanisms (KEMs) and digital signature schemes. The cryptographic schemes described in this document are among those recommended by major security agencies and/or standardization bodies, and are believed to be secure against Cryptographically Relevant Quantum Computer (CRQC). The goal of this document is to offer a high-level overview of these schemes and their distinguishing features, to help implementers, protocol designers, standards developers, and policymakers in understanding and selecting appropriate post-quantum cryptographic primitives for use in protocols and systems. By aggregating and presenting this information in a unified format, this document aims to facilitate informed decision-making and interoperability during the migration to post-quantum cryptography, and to encourage consistent practices when evaluating and deploying Post-Quantum Cryptography (PQC) schemes in cryptographic protocols.

### Much Ado About Encodings
Presentation · Working group: pquip
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-pquip-much-ado-about-encodings-01 | video: https://www.youtube.com/watch?v=vLlekahKwx4 | materials: https://datatracker.ietf.org/meeting/123/session/pquip
Slides presented at the pquip session; no Internet-Draft is linked to them.

## Working Group: quic

### Multipath extension for QUIC
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-multipath-extension-for-quic-02 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Extended Key Update in QUIC
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-extended-key-update-in-quic-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Ack Frequency
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-ack-frequency-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### QUIC Packet Receive Timestamps
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-quic-packet-receive-timestamps-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### QMux comparing wire protocols
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-qmux-comparing-wire-protocols-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Deadline-aware streams
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-deadline-aware-streams-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### QUIC OACK
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-quic-oack-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Instant Acknowledgments in QUIC Handshakes
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-quic-instant-acknowledgments-in-quic-handshakes-00 | video: https://www.youtube.com/watch?v=8OSthhkL2qk | materials: https://datatracker.ietf.org/meeting/123/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

## Working Group: rats

### Concise Reference Integrity Manifest
Draft: draft-ietf-rats-corim · Working group: rats
Agenda: (20 min) Yogesh Deshpande and TBD - https://datatracker.ietf.org/doc/draft-ietf-rats-corim/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-corim/ | materials: https://datatracker.ietf.org/meeting/123/session/rats
Remote Attestation Procedures (RATS) enable Relying Parties to assess the trustworthiness of a remote Attester and therefore to decide whether or not to engage in secure interactions with it. Evidence about trustworthiness can be rather complex and it is deemed unrealistic that every Relying Party is capable of the appraisal of Evidence. Therefore that burden is typically offloaded to a Verifier. In order to conduct Evidence appraisal, a Verifier requires not only fresh Evidence from an Attester, but also trusted Endorsements and Reference Values from Endorsers and Reference Value Providers, such as manufacturers, distributors, or device owners. This document specifies the information elements for representing Endorsements and Reference Values in CBOR format.

### Reference Interaction Models for Remote Attestation Procedures
Draft: draft-ietf-rats-reference-interaction-models · Working group: rats
Agenda: (10 min) Henk Birkholz - https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-reference-interaction-models/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-reference-interaction-models-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
This document describes interaction models for remote attestation procedures (RATS) [RFC9334]. Three conveying mechanisms -- Challenge/Response, Uni-Directional, and Streaming Remote Attestation -- are illustrated and defined. Analogously, a general overview about the information elements typically used by corresponding conveyance protocols are highlighted.

### Integration of Remote Attestation with Key Negotiation and Key Distribution mechanisms
Draft: draft-xia-rats-key-negotiation-integration · Working group: rats
Agenda: (10 minutes) Frank XiaLiang - https://datatracker.ietf.org/doc/draft-xia-rats-key-negotiation-integration/
page: https://datatracker.ietf.org/doc/draft-xia-rats-key-negotiation-integration/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-integration-of-remote-attestation-with-key-negotiation-and-distribution-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
This document describes a generic way to integrate Remote Attestation (RA) with key distribution and key negotiation, so that cryptographic keys are only released to or accepted from attested and policy- compliant environments. It defines an attestation-bound key management mechanism that can be applied on top of existing secure channel and key management protocols, and illustrates it with three representative scenarios: public-cloud KMS, end-user to AI data- center communication, and enterprise-operated KMS. A format-agnostic key binding claim is introduced to express the binding between an Attester’s environment, its public keys, and a session identifier, enabling Relying Parties to use Attestation Results as an input to key distribution and key agreement decisions without changing underlying protocols.

### Concise Selector for Endorsements and Reference Values
Draft: draft-howard-rats-coserv · Working group: rats
Agenda: (15 min) Paul Howard and Thomas Fossati - https://datatracker.ietf.org/doc/draft-howard-rats-coserv/
page: https://datatracker.ietf.org/doc/draft-howard-rats-coserv/ | materials: https://datatracker.ietf.org/meeting/123/session/rats
In the Remote Attestation Procedures (RATS) architecture, Verifiers require Endorsements and Reference Values to assess the trustworthiness of Attesters. This document specifies the Concise Selector for Endorsements and Reference Values (CoSERV), a structured query/result format designed to facilitate the discovery and retrieval of these artifacts from various providers. CoSERV defines a query language and corresponding result structure using CDDL, which can be serialized in CBOR format, enabling efficient interoperability across diverse systems.

### RATS Conceptual Messages Wrapper (CMW)
Draft: draft-ietf-rats-msg-wrap · Working group: rats
Agenda: (15 min) Thomas Fossati - https://datatracker.ietf.org/doc/draft-ietf-rats-msg-wrap/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-msg-wrap/ | materials: https://datatracker.ietf.org/meeting/123/session/rats
The Conceptual Messages introduced by the RATS architecture (RFC 9334) are protocol-agnostic data units that are conveyed between RATS roles during remote attestation procedures. Conceptual Messages describe the meaning and function of such data units within RATS data flows without specifying a wire format, encoding, transport mechanism, or processing details. The initial set of Conceptual Messages is defined in Section 8 of RFC 9334 and includes Evidence, Attestation Results, Endorsements, Reference Values, and Appraisal Policies. This document introduces the Conceptual Message Wrapper (CMW) that provides a common structure to encapsulate these messages. It defines a dedicated CBOR tag, corresponding JSON Web Token (JWT) and CBOR Web Token (CWT) claims, and an X.509 extension. This allows CMWs to be used in CBOR-based protocols, web APIs using JWTs and CWTs, and PKIX artifacts like X.509 certificates. Additionally, the draft defines a media type and a CoAP content format to transport CMWs over protocols like HTTP, MIME, and CoAP. The goal is to improve the interoperability and flexibility of remote attestation protocols. Introducing a shared message format such as CMW enables consistent support for different attestation message types, evolving message serialization formats without breaking compatibility, and avoiding the need to redefine how messages are handled within each protocol.

### Entity Attestation Token (EAT) Measured Component
Draft: draft-ietf-rats-eat-measured-component · Working group: rats
Agenda: (10 min) Thomas Fossati - https://datatracker.ietf.org/doc/draft-ietf-rats-eat-measured-component/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-eat-measured-component/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-eat-measured-components-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
The term "measured component" refers to an object within the attester's target environment whose state can be sampled and typically digested using a cryptographic hash function. Examples of measured components include firmware stored in flash memory, software loaded into memory at start time, data stored in a file system, or values in a CPU register. This document provides the information model for the "measured component" and two associated data models. This separation is intentional: the JSON and CBOR serializations, coupled with the media types and associated Constrained Application Protocol (CoAP) Content-Formats, enable the immediate use of the semantics within the Entity Attestation Token (EAT) framework. Meanwhile, the information model can be reused in future specifications to provide additional serializations, for example, using ASN.1.

### Remote attestation over EDHOC
Draft: draft-song-lake-ra · Working group: rats
Agenda: (10 min) Yuxuan Song - https://datatracker.ietf.org/doc/draft-song-lake-ra/
page: https://datatracker.ietf.org/doc/draft-song-lake-ra/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-remote-attestation-over-edhoc-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
This document specifies how to perform remote attestation as part of the lightweight authenticated Diffie-Hellman key exchange protocol EDHOC (Ephemeral Diffie-Hellman Over COSE), based on the Remote ATtestation procedureS (RATS) architecture.

### Distributed Remote Attestation
Draft: draft-wang-rats-distributed-remote-attestation · Working group: rats
Agenda: (10 minutes) Donghui Wang - https://datatracker.ietf.org/doc/draft-wang-rats-distributed-remote-attestation/
page: https://datatracker.ietf.org/doc/draft-wang-rats-distributed-remote-attestation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-distributed-remote-attestation-01 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
In many deployments, remote attestation is performed within separate administrative and trust domains. Each domain typically operates its own management plane and a Remote Attestation Service (RAS) to obtain verifier inputs (e.g., endorsement material and reference values) and produce attestation results. At scale, cross-domain scenarios face two recurring challenges: (1) enabling policy-controlled transparency so that verifiers or relying parties in one domain can discover and retrieve selected attestation artifacts from other domains; and (2) supporting many-to-many distribution and reuse of verifier inputs and verifier outputs without requiring point-to-point integrations. This document describes Distributed Remote Attestation (DRA) patterns that use a shared publication channel for selected artifacts with provenance and access control in mind. A Distributed Ledger (DL) is discussed as one concrete instantiation of such a publication channel, including an option to host verification logic on the DL. The described patterns are intended to complement existing RATS procedures and conceptual messages, and can be realized by other tamper-evident publication channels with comparable properties.

### Remote Posture Assessment for Systems, Containers, and Applications at Scale
Draft: draft-ietf-rats-posture-assessment · Working group: rats
Agenda: (10 min) - Derek Welski - https://datatracker.ietf.org/doc/draft-ietf-rats-posture-assessment/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-posture-assessment/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-rats-posture-assessment-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
This document establishes an architectural pattern whereby Attestation Results could be produced for a complete set of benchmarks or controls that are defined and grouped by an external entity, eliminating the need to convey individual Evidence items for each item within a benchmark or control framework. This document establishes a pattern to list sets of benchmarks and controls within CWT and JWT formats for use as an Entity Attestation Token (EAT). While the discussion below pertains mostly to TPM, other Roots of Trust such as TCG DICE and non-TCG defined components will also be included.

### Extending Trusted Path Routed: Issues in Runtime Trust Assessment and Monitoring
Draft: draft-rats-runtime-tpr · Working group: rats
Agenda: (10 min) Ioannis Krontiris - https://datatracker.ietf.org/doc/draft-rats-runtime-tpr-00
page: https://datatracker.ietf.org/doc/draft-rats-runtime-tpr/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-runtime-tpr-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
This document outlines architectural challenges and open issues in extending the Trusted Path Routing model to include runtime trust assessment and monitoring. It is intended as input to ongoing discussions within the RATS and Trusted Path Routing work.

### Evidence Encoding for Hardware Security Modules
Draft: draft-ietf-rats-pkix-key-attestation · Working group: rats
Agenda: (10 minutes) Jean-Pierre Fiset - https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/
page: https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-pkix-evidence-for-remote-attestation-of-hsms-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
This document specifies a vendor-agnostic format for Evidence produced and verified within a PKIX context. The Evidence produced this way includes claims collected about a cryptographic module, such as a Hardware Security Module (HSM), and elements found within it such as cryptographic keys. One scenario envisaged is that the state information about the cryptographic module can be securely presented to a remote operator or auditor in a vendor-agnostic verifiable format. A more complex scenario would be to submit this Evidence to a Certification Authority to aid in determining whether the storage properties of this key meet the requirements of a given certificate profile.

### Proof of Position for Auditor managed Endorsements
Draft: draft-richardson-rats-pop-endorsement · Working group: rats
Agenda: (10 min) Michael Richardson and Liu (Peter) Chunchi - https://datatracker.ietf.org/doc/draft-richardson-rats-pop-endorsement-00
page: https://datatracker.ietf.org/doc/draft-richardson-rats-pop-endorsement/ | materials: https://datatracker.ietf.org/meeting/123/session/rats
Some aspects of a device can not be intuited by the device itself. For instance, a router platform may have no way to know what color the case is, where in a cabinet it is located, or which electrical circuit it is connected to. This kind of information must be provided through an Endorsement: a statement from a third party. These statements may require human audiitors to inspect the device physically. But, which device is really in front of an auditor? This document describes a mechanism by which an auditor can make physical contact with a device and collect information to identify the device in a cryptographically strong manner. This protocol is not designed to run over Internet Protocol cabling, but rather over mechanisms such as USB cables, or serial consoles.

### Remote Attestation with Exported Authenticators
Draft: draft-fossati-tls-exported-attestation · Working group: rats
Agenda: (5 minutes) Muhammad Usama Sardar - https://datatracker.ietf.org/doc/draft-fossati-tls-exported-attestation
page: https://datatracker.ietf.org/doc/draft-fossati-tls-exported-attestation/ | materials: https://datatracker.ietf.org/meeting/123/session/rats
This specification defines a method for two parties in a communication interaction to exchange Evidence and Attestation Results using exported authenticators, as defined in RFC 9261. Additionally, it introduces the cmw_attestation extension, which allows attestation credentials to be included directly in the Certificate message sent during the Exported Authenticator-based post-handshake authentication. The approach supports both the passport and background check models from the RATS architecture while ensuring that attestation remains bound to the underlying communication channel.

### Update on CoRIM Progress
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-update-on-corim-progress-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### CoSERV Call for Adoption
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-coserv-call-for-adoption-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### RATS Key Negotiation Integration
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-rats-key-negotiation-integration-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Attested TLS
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-attested-tls-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Conceptual Message Wrappers
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-conceptual-message-wrappers-01 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Zero-Trust Sovereign AI – RATS impact
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-zero-trust-sovereign-ai-rats-impact-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Remote Attestation with Multiple Verifiers
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-remote-attestation-with-multiple-verifiers-01 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Proof of Presence: Endorsement of Location
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-proof-of-presence-endorsement-of-location-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### Terminology: Target Environments vs Attesting Environment vs HSMs
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rats-terminology-target-environments-vs-attesting-environment-vs-hsms-00 | video: https://www.youtube.com/watch?v=kUyqSvsX-QU | materials: https://datatracker.ietf.org/meeting/123/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

## Working Group: rift

### RIFT in Dragonfly Topologies
Draft: draft-przygienda-rift-dragonfly · Working group: rift
Agenda: https://www.ietf.org/archive/id/draft-przygienda-rift-dragonfly-01.html
page: https://datatracker.ietf.org/doc/draft-przygienda-rift-dragonfly/ | video: https://www.youtube.com/watch?v=MwBFiCYPCmA | materials: https://datatracker.ietf.org/meeting/123/session/rift
RIFT extensions for dragonfly topologies.

### Multicast use case in LLM MoE
Draft: draft-zhang-rtgwg-llmmoe-multicast · Working group: rift
Agenda: https://datatracker.ietf.org/doc/draft-zhang-rtgwg-llmmoe-multicast/
page: https://datatracker.ietf.org/doc/draft-zhang-rtgwg-llmmoe-multicast/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rift-llm-moe-multicast-00 | video: https://www.youtube.com/watch?v=MwBFiCYPCmA | materials: https://datatracker.ietf.org/meeting/123/session/rift
Large Language Models (LLMs) have been widely used in recent years. The Mixture of Experts (MoE) architecture is one of the features of LLMs that enables efficient inference and cost-effective training. With the MoE architecture, there are potential multicast use cases such as tokens dispatching. This draft attempts to analyze these use cases.

### df++
Presentation · Working group: rift
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rift-df-00 | video: https://www.youtube.com/watch?v=MwBFiCYPCmA | materials: https://datatracker.ietf.org/meeting/123/session/rift
Slides presented at the rift session; no Internet-Draft is linked to them.

### KV status
Presentation · Working group: rift
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rift-kv-status-00 | video: https://www.youtube.com/watch?v=MwBFiCYPCmA | materials: https://datatracker.ietf.org/meeting/123/session/rift
Slides presented at the rift session; no Internet-Draft is linked to them.

### df++ annotated
Presentation · Working group: rift
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rift-df-annotated-00 | video: https://www.youtube.com/watch?v=MwBFiCYPCmA | materials: https://datatracker.ietf.org/meeting/123/session/rift
Slides presented at the rift session; no Internet-Draft is linked to them.

## Working Group: rtgwg

### Destination/Source Routing
Draft: draft-ietf-rtgwg-dst-src-routing-revive · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-dst-src-routing-revive/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-dst-src-routing-revive/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-02-dst-src-routing-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document specifies using packets' source addresses in route lookups as additional qualifier to be used in hop-by-hop routing decisions. The proposed mechanism applies to IPv6 [RFC8200] in general with specific considerations for routing protocols.

### YANG Data Model for IPv6 Neighbor Discovery
Draft: draft-ietf-rtgwg-ipv6-address-resolution-yang · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-ipv6-address-resolution-yang/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-ipv6-address-resolution-yang/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-03-ipv6-address-resolution-yang-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document defines a YANG data model to configure and manage IPv6 Neighbor Discovery (ND) and related functions, including IPv6 address resolution, redirect function, proxy Neighbor Advertisement, Neighbor Unreachability Detection (NUD), Duplicate Address Detection (DAD), SEcure Neighbor Discovery (SEND), and Secure ND Proxy.

### SRv6 Path Egress Protection
Draft: draft-ietf-rtgwg-srv6-egress-protection · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-srv6-egress-protection/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-srv6-egress-protection/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-4-srv6-path-egress-protection-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document describes the mechanism and operational considerations for fast protecting the egress node and link of a Segment Routing for IPv6 (SRv6) path. Topology Independent Loop-Free Alternate (TI-LFA) specifies fast protections for transit nodes and links of an SR path, but does not present protections for the egress node. The solution uses a Mirror SID (End.M) behavior to steer traffic to a protector egress upon failure of the primary egress. The Interior Gateway Protocol (IGP) (IS-IS/OSPFv3) extensions used to advertise the Mirror SID and protected locators are specified in [I-D.ietf-lsr-srv6-mirror-sid-igp-encoding]; they build on the IS-IS and OSPFv3 SRv6 extensions defined in [RFC9352] and [RFC9513].

### Fast failure detection in VRRP with Point to Point BFD
Draft: draft-ietf-rtgwg-vrrp-bfd-p2p · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-bfd-p2p/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-vrrp-bfd-p2p/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-051-p2mp-bfd-vrrp-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document describes how Point to Point Bidirectional Forwarding Detection (BFD) can be used to support sub-second detection of a Active Router failure in the Virtual Router Redundancy Protocol (VRRP).

### Lightweight Host Routing using LLDP
Draft: draft-filsfils-rtgwg-lightweight-host-routing · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-filsfils-rtgwg-lightweight-host-routing/
page: https://datatracker.ietf.org/doc/draft-filsfils-rtgwg-lightweight-host-routing/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-lightweight-host-routing-using-lldp-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
Link Layer Discovery Protocol (LLDP) is widely deployed today for discovery of information across network elements like routers, switches, and hosts. This document extends LLDP to allow hosts to advertise their IP prefixes to their attached routers which can then propagate the reachability of these host prefixes into routing protocols for enabling network-wide connectivity.

### A YANG Module for SRv6 Next-Hop RIB Extensions
Draft: draft-lin-rtgwg-srv6-nexthop-yang · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-lin-rtgwg-srv6-nexthop-yang/
page: https://datatracker.ietf.org/doc/draft-lin-rtgwg-srv6-nexthop-yang/ | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document defines a YANG data module for configuring and managing SRv6 next hop information for Routing, which augments the YANG data model for Routing Management (RFC8349).

### Enhanced ECMP for AI Cluster
Draft: draft-cheng-rtgwg-enhanced-ecmp · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/
page: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-enhanced-ecmp-for-ai-cluster-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
In AI training scenarios, the current mainstream load balancing technology is per-flow ECMP. However, hash collision issues lead to imbalanced traffic distribution, adversely affecting application performance. To address this problem, this document proposes an enhanced ECMP method that resolves load imbalance caused by hash collisions. The proposed solution effectively improves load balancing efficiency, reduces network congestion, and enhances overall network performance.

### SR based Loop-free implementation
Draft: draft-deng-rtgwg-sr-loop-free · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-deng-rtgwg-sr-loop-free/
page: https://datatracker.ietf.org/doc/draft-deng-rtgwg-sr-loop-free/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-09-sr-loop-free-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
Microloops are transient packet loops that occur in the network following a topology change (link down, link up, node fault, or metric change events). Microloops are caused by the non-simultaneous convergence of different nodes in the network. If nodes converge and send traffic to a neighbor node that has not converged yet, traffic may be looped between these two nodes, resulting in packet loss, jitter, and out-of-order packets. This document presents some optional implementation methods aimed at providing loop avoidance in the case of IGP network convergence event in different scenarios.

### Use Cases and Requirements for Implementing Lossless Techniques in Wide Area Networks
Draft: draft-hs-rtgwg-wan-lossless-uc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-hs-rtgwg-wan-lossless-uc
page: https://datatracker.ietf.org/doc/draft-hs-rtgwg-wan-lossless-uc/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-10-use-casesrequirements-and-framework-for-implementing-lossless-techniques-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document outlines the use cases and requirements for implementing lossless data transmission techniques in Wide Area Networks (WANs), motivated by the increasing demand for high- bandwidth and reliable data transport in applications such as high- performance computing (HPC), genetic sequencing, multimedia content production and distributed training. The challenges associated with existing data transport protocols in WAN environments are discussed, along with the proposal of requirements for enhancing lossless transmission capabilities to support emerging data-intensive applications.

### Use cases and Requirement for Flow Control Collaboration Across DCNs and WAN
Draft: draft-han-rtgwg-codeployment-pfc-fgfc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-han-rtgwg-codeployment-pfc-fgfc/
page: https://datatracker.ietf.org/doc/draft-han-rtgwg-codeployment-pfc-fgfc/ | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
The demand for lossless network transmission and the application of flow control mechanisms have expanded from DCNs (Data Center Networks) to WANs(Wide Area Networks). To mitigate PFC - related issues in WANs, the fine - grained flow control is proposed. This mechanism aims to achieve precise control at flow / tenant levels, limits flow control to specified paths and slices, and provides intelligent congestion backpressure. As current DCN already adopts PFC mechanisms, the fine-grained flow control in WANs needs to work with PFC in DCNs to achieve end-to-end flow control. This document describes the use cases and requirements for the collaboration of flow control mechanisms across DCNs and WANs.

### SRv6 behavior extention for Flow Control in WAN
Draft: draft-ruan-spring-priority-flow-control-sid · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ruan-spring-priority-flow-control-sid/
page: https://datatracker.ietf.org/doc/draft-ruan-spring-priority-flow-control-sid/ | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
In the wake of the continuous emergence of novel AI technologies, including collaborative training, distributed inference and the like, the scenario in which different data centers communicate via the RDMA (Remote Direct Memory Access) protocol has emerged as a new requirement. similar to data center networks, wide area networks (WANs) should also be equipped with certain flow control capabilities, nodes in the wide area network (WAN) need to quickly and accurately notify upstream traffic nodes of their congestion status. Upon receiving the congestion notification, upstream nodes can take responsive actions to mitigate network congestion. By extending SRv6[RFC 8986] technology, specific services can be carried over SRv6 policies, which enables the precise delivery and response of congestion signals. For traffic carried over SRv6 policies, the service traffic path is explicitly orchestrated via the Segment List in the SRH header. By parsing the sequence of the Segment List, downstream nodes or controllers can accurately identify the upstream nodes and interfaces corresponding to the current traffic, thus enabling the rapid notification of congestion information to the upstream. Since each SID in the Segment List is a 128-bit IPv6 address that represents a specific behaviour (e.g., End, End.X), extending existing behaviours to mark their capability to receive and process congestion signals allows flexible control over the delivery mode of congestion signals in the WAN. The specific packet formats and contents of congestion signals vary in various ways and are continuously being updated. This document takes the most commonly used PFC backpressure notification mechanism as an example to elaborate on the overall workflow of WAN congestion information notification and the extensions to the SRv6 protocol. PFC technology is widely deployed in RoCEv2 networks within data centers to report congestion signals. By leveraging SRv6 and NRP technologies, it is possible to effectively control the propagation range and path of PFC backpressure signals in wide area networks, thereby avoiding issues such as deadlocks and the excessive propagation of congestion scope.

### Framework for Implementing Lossless Techniques in Wide Area Networks
Draft: draft-hs-rtgwg-wan-lossless-framework · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-hs-rtgwg-wan-lossless-framework/
page: https://datatracker.ietf.org/doc/draft-hs-rtgwg-wan-lossless-framework/ | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document proposes a comprehensive framework to address the challenges of efficient, reliable, and cost-effective large volume data transmission over Wide Area Networks (WANs). The framework focuses on planning and managing traffic paths, network slicing, and utilizing multi-level network buffers. It introduces dynamic path scheduling and advanced resource allocation techniques to optimize network resouce and minimize congestion. By leveraging cross-device buffer coordination and real-time adjustments, the framework ensures high throughput and low latency, meeting the demands of modern, data- intensive applications while providing a robust solution for large- scale data transmission.

### Fully Adaptive Routing Ethernet in Scale-Up Networks
Draft: draft-xu-rtgwg-fare-in-sun · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-xu-rtgwg-fare-in-sun/
page: https://datatracker.ietf.org/doc/draft-xu-rtgwg-fare-in-sun/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-11-fare-in-sun-02 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
The Mixture of Experts (MoE) has become a dominant paradigm in transformer-based artificial intelligence (AI) large language models (LLMs). It is widely adopted in both distributed training and distributed inference. To enable efficient expert parallelization and even tensor parallelization across dozens or even hundreds of Graphics Processing Units (GPUs) in MoE architectures, an ultra-high- throughput, ultra-low-latency AI scale-up network (SUN) is critical. This document describes how to extend the Weighted Equal-Cost Multi- Path (WECMP) load-balancing mechanism, referred to as Fully Adaptive Routing Ethernet (FARE), which was originally designed for scale-out networks, to scale-up networks.

### Kademlia-directed ID-based Routing Architecture (KIRA)
Draft: draft-bless-rtgwg-kira · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-bless-rtgwg-kira/
page: https://datatracker.ietf.org/doc/draft-bless-rtgwg-kira/ | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
This document describes the Kademlia-directed ID-based Routing Architecture KIRA. KIRA is a scalable zero-touch distributed routing solution that is tailored to control planes. It prioritizes scalable and resilient connectivity over route efficiency (stretched paths are accepted as trade-off against routing protocol overhead). KIRA's self-assigned, topologically independent IDs can be embedded into IPv6 addresses. Combined with further self-organization mechanisms from Kademlia, KIRA achieves a zero-touch solution that provides scalable IPv6 connectivity without requiring any manual configuration. For example, it can connect hundreds of thousands of routers and devices in a single network without requiring any form of hierarchy (like areas). It works well in various topologies and is loop-free even during convergence. This self-contained solution, and especially the independence from any manual configuration, make it suitable as a resilient base for all management and control tasks, allowing the network to recover from the most complex failure scenarios. The architecture consists of the ID-based network layer routing protocol R²/Kad in its Routing Tier (using source routing) and a PathID-based Forwarding Tier (using PathIDs as labels for paths). KIRA’s tightly integrated add-on services (e.g., name resolution as well as fast and efficient topology discovery) provide a perfect basis for autonomic network management solutions.

### 052-vrrp-p2p
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-052-vrrp-p2p-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### YANG Data Model for SRv6 Next Hop of Route
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-yang-data-model-for-srv6-next-hop-of-route-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### LLM-MoE-Multicast
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-12-llm-moe-multicast-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

### KIRA - Scalable Zero-Touch Routing
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-rtgwg-kira-scalable-zero-touch-routing-00 | video: https://www.youtube.com/watch?v=x3CtfyNyKO4 | materials: https://datatracker.ietf.org/meeting/123/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

## Working Group: savnet

### General Source Address Validation Capabilities
Draft: draft-ietf-savnet-general-sav-capabilities · Working group: savnet
Agenda: Draft link: draft-ietf-savnet-general-sav-capabilities-01
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-general-sav-capabilities/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-general-source-address-validation-capabilities-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
The SAV rules of existing source address validation (SAV) mechanisms are derived from other core data structures (e.g., FIB-based uRPF) that are not dedicatedly designed for source filtering. Consequently, these mechanisms have limitations in deployable scenarios and traffic handling policies. To overcome these limitations, this document introduces general SAV capabilities from a data plane perspective. How to implement the capabilities and how to generate SAV rules are not in the scope of this document.

### Intra-domain Source Address Validation (SAV) Solution Based on BM-SPF
Draft: draft-wang-savnet-intra-domain-solution-bm-spf · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-wang-savnet-intra-domain-solution-bm-spf/
page: https://datatracker.ietf.org/doc/draft-wang-savnet-intra-domain-solution-bm-spf/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-intra-domain-source-address-validation-sav-solution-based-on-bm-spf-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This draft proposes a new intra-domain Source Address Validation (SAV) solution. This solution leverages the Bidirectional Metric- based Shortest Path First (BM-SPF) mechanism to avoid the complexity introduced by asymmetric routing for source address validation. It allows intra-domain routers to generate directly the SAV rule from the router's FIB table, based on the reality that the source and destination interface will be same if the IGP domain is symmetric assured.

### Intra-Domain On-Demand Source Address Validation(SAV) Mechanism
Draft: draft-li-savnet-intra-domain-od-sav · Working group: savnet
Agenda: Related draft title/link: https://datatracker.ietf.org/doc/draft-li-savnet-intra-domain-od-sav/
page: https://datatracker.ietf.org/doc/draft-li-savnet-intra-domain-od-sav/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-slides-123-intra-domain-on-demand-source-address-validationsav-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Source Address Validation (SAV) mechanisms, such as uRPF, ACLs, and BM-SPF, are applied to prevent IP source address spoofing. However, these mechanisms are typically designed for static routing scenarios and deployed at fixed network boundaries. With the increasing adoption of dynamic forwarding technologies such as SRv6 Policy and Fast Reroute (TI-FRR), the network's actual forwarding path may change frequently due to policy-based traffic steering or link failures. In such cases, statically deployed SAV rules may fail to validate traffic on newly activated or alternate paths, creating validation blind spots or even leading to false positives that block legitimate traffic. This draft proposes an On-Demand Source Address Validation Activation mechanism. It enables routers to dynamically activate or update SAV rules on specific interfaces only when the interface becomes part of an active forwarding path due to policy or failover triggers. This approach enhances SAV coverage, avoids unnecessary resource consumption, and ensures SAV correctness under dynamic path switching scenarios driven by SRv6-policy and TI-FRR.

### Problem Statement, Gap Analysis, and Requirements for Inter-Domain Source Address Validation
Draft: draft-ietf-savnet-inter-domain-problem-statement · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-problem-statement/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-updates-on-source-address-validation-in-intra-domain-networks-gap-analysis-problem-statement-and-requirements-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document analyzes the problem space and provides a gap analysis of existing inter-domain source address validation (SAV) mechanisms. Based on these findings, it outlines the technical requirements for future improvements.

### Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)
Draft: draft-ietf-sidrops-bar-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-bar-sav-06
page: https://datatracker.ietf.org/doc/draft-ietf-sidrops-bar-sav/ | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Designing an efficient source address validation (SAV) filter requires minimizing false positives (i.e., avoiding blocking legitimate traffic) while maintaining directionality (see RFC8704). This document advances the technology for SAV filter design through a method that makes use of BGP UPDATE messages, Autonomous System Provider Authorization (ASPA), and Route Origin Authorization (ROA). The proposed method's name is abbreviated as BAR-SAV. BAR-SAV can be used by network operators to derive more robust SAV filters and thus improve network resilience. This document updates RFC8704.

### A Profile for Traffic Origin Authorizations (TOAs)
Draft: draft-qin-sidrops-toa · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-qin-sidrops-toa/
page: https://datatracker.ietf.org/doc/draft-qin-sidrops-toa/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-considerations-for-sav-specific-information-and-the-need-of-traffic-origin-authorizations-toas-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document defines a standard profile for Traffic Origin Authorizations (TOAs), a Cryptographic Message Syntax (CMS) protected content type for use with the Resource Public Key Infrastructure (RPKI). A TOA is a digitally signed object that provides a means of verifying that an IP address block holder has authorized an Autonomous System (AS) to originate traffic using source IP addresses within the address block.

### Bicone Source Address Validation
Draft: draft-li-sidrops-bicone-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-li-sidrops-bicone-sav/
page: https://datatracker.ietf.org/doc/draft-li-sidrops-bicone-sav/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-updates-on-bicone-source-address-validation-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
The primary design goal of source address validation (SAV) is avoiding improper blocks (i.e., blocking legitimate traffic) while maintaining directionality (see [I-D.ietf-savnet-inter-domain-problem-statement] and [RFC8704]). Existing advanced SAV solutions (e.g., EFP-uRPF [RFC8704]) for an Autonomous System (AS) typically generate ingress SAV allowlist filters on interfaces facing a customer or lateral peer AS. This document analyzes the potential improper block problems when using an allowlist. To avoid improper blocks, this document proposes a new SAV solution by generating an ingress SAV blocklist filter which contains prefixes exclusively belonging to the provider cone. In practice, network operators can flexibly decide to use a blocklist or an allowlist according to their requirements and actual conditions.

### Inter-domain Source Address Validation based on AS relationships
Draft: draft-rly-savnet-inter-domain-as-relationships · Working group: savnet
Agenda: Draft link: draft-rly-savnet-inter-domain-as-relationships-04 - Inter-domain Source Address Validation based on AS relationships
page: https://datatracker.ietf.org/doc/draft-rly-savnet-inter-domain-as-relationships/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-inter-domain-source-address-validation-based-on-as-relationships-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This draft introduces a distributed inter-domain source address validation scheme based on AS relationships named AS Relationship Based Inter-domain Filtering (ARBIF). It primarily describes this method from seven aspects: a brief introduction to the scheme, an overview of the AS relationship classification and acquisition methods, the architecture of the ARBIF system, implementation based on BGP extension, typical use cases, experiments of ARBIF, and considerations for deployability.

### Source Prefix Advertisement for Inter-domain SAVNET
Draft: draft-geng-savnet-inter-domain-spa · Working group: savnet
Agenda: Link: https://datatracker.ietf.org/doc/draft-geng-savnet-inter-domain-spa/
page: https://datatracker.ietf.org/doc/draft-geng-savnet-inter-domain-spa/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-source-prefix-advertisement-spa-for-inter-domain-savnet-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document proposes a mechanism that enables a Source AS to actively advertise their locally observed Customer Cone and prefix information to the adjacent Validating AS via a new inter-domain message called Source Prefix Advertisement (SPA). The Validating AS then combines this SPA-carried information with local source address validation-related information to construct more accurate prefix allowlists for interfaces connected to Source ASes.

### Advertising SAV Rule-related Information using BGP Link-State
Draft: draft-tong-idr-bgp-ls-sav-rule · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/
page: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/ | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document proposes extensions to the BGP Link-State protocol for advertising Source Address Validation (SAV) rule-related information for monitoring and management purposes.

### Benchmarking Methodology for Intra-domain and Inter-domain Source Address Validation
Draft: draft-chen-bmwg-savnet-sav-benchmarking · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-chen-bmwg-savnet-sav-benchmarking/
page: https://datatracker.ietf.org/doc/draft-chen-bmwg-savnet-sav-benchmarking/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-yang-data-model-for-intra-domain-and-inter-domain-source-address-validation-savnet-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document defines methodologies for benchmarking the performance of intra-domain and inter-domain source address validation (SAV) mechanisms. SAV mechanisms are utilized to generate SAV rules to prevent source address spoofing, and have been implemented with many various designs in order to perform SAV in the corresponding scenarios. This document takes the approach of considering a SAV device to be a black box, defining the methodology in a manner that is agnostic to the mechanisms. This document provides a method for measuring the performance of existing and new SAV implementations.

### YANG Data Model for Intra-domain and Inter-domain Source Address Validation (SAVNET)
Draft: draft-li-savnet-sav-yang · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/
page: https://datatracker.ietf.org/doc/draft-li-savnet-sav-yang/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-the-update-on-the-source-address-validation-in-inter-domain-networks-gap-analysis-problem-statement-and-requirements-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document describes a YANG data model for Intra-domain and Inter-domain Source Address Validation (SAVNET). The model serves as a base framework for configuring and managing an SAV subsystem, including SAV rule and SAV Tables, and expected to be augmented by other SAV technology models accordingly. Additionally, this document also specifies the model for the SAV Static application.

### Inter-domain scaling considerations for source address validation (SAV)
Draft: draft-haas-savnet-inter-domain-scaling · Working group: savnet
Agenda: Draft link: draft-haas-savnet-inter-domain-scaling-00
page: https://datatracker.ietf.org/doc/draft-haas-savnet-inter-domain-scaling/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-inter-domain-sav-scaling-considerations-01 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Source address validation (SAV) covers the general techniques to prevent IP source address spoofing, which is often used in networking attacks. Two primary problem spaces addressed in work on SAV include building the "source of truth" for what IP networks should be permitted to source IP traffic behind a set of network interfaces, and implementing the data plane enforcement for the validation. Implementing data plane enforcement, especially for inter-domain networking for the Internet carried by BGP-4 [RFC 4271] has a number of scaling considerations. One consideration is the potentially large and often asymmetric sizes of the per-interface SAV tables vs. the Forwarding Information Base (FIB). A second consideration is synchronization issues between SAV enforcement mechanisms and the forwarding state for the FIB where a lack of coordination may result in dropped or mis-forwarded traffic. This draft explores these two considerations under the title, "The asymmetric contract, and the broken promise."

### Path Computation Element Communication Protocol for Source Address Validation
Draft: draft-song-pce-pcep-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-song-pce-pcep-sav/
page: https://datatracker.ietf.org/doc/draft-song-pce-pcep-sav/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-15-policy-computing-element-communication-protocol-for-source-address-validation-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
This document presents a method of Path Computation Element (PCE) for Source Address Validation (SAV) in networks. It extends Path Computation Element Communication Protocol (PCEP) to support SAV policy distribution and synchronization between PCEP speakers for threat mitigation for source address spoofing.

### Update on the BAR-SAV Draft
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-update-on-the-bar-sav-draft-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Source Prefix Advertisement for Inter-domain SAVNET
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-source-prefix-advertisement-for-inter-domain-savnet-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Advertisement of Multi-Sourced SAV Rules using BGP Link-State
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-advertisement-of-multi-sourced-sav-rules-using-bgp-link-state-01 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### The Updates on the Benchmarking Methodology for Source Address Validation
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-savnet-the-updates-on-the-benchmarking-methodology-for-source-address-validation-00 | video: https://www.youtube.com/watch?v=5pCyPcIQcAY | materials: https://datatracker.ietf.org/meeting/123/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

## Working Group: scitt

### Supply Chain Use Cases to Design Secure Computing Systems for SCITT Extension
Draft: draft-nobuo-scitt-use-cases-extension · Working group: scitt
Agenda: https://github.com/aoki-n1/draft-nobuo-scitt-use-cases-extension.git (Aoki Nobuo) 10 minutes
page: https://datatracker.ietf.org/doc/draft-nobuo-scitt-use-cases-extension/ | video: https://www.youtube.com/watch?v=OEQSKN7jcNk | materials: https://datatracker.ietf.org/meeting/123/session/scitt
This document includes a collection of representative Computational Supply Chain Use Cases. These use cases aim to identify computational supply chain problems that the industry faces today and act as a guideline for developing a comprehensive security architecture and solutions for these scenarios.

### Main slides
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-scitt-main-slides-01 | video: https://www.youtube.com/watch?v=OEQSKN7jcNk | materials: https://datatracker.ietf.org/meeting/123/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

### Aligning RESCALE with SCITT
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-scitt-aligning-rescale-with-scitt-00 | video: https://www.youtube.com/watch?v=OEQSKN7jcNk | materials: https://datatracker.ietf.org/meeting/123/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

### Main Slides SCITT 123
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-scitt-main-slides-scitt-123-00 | video: https://www.youtube.com/watch?v=OEQSKN7jcNk | materials: https://datatracker.ietf.org/meeting/123/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

## Working Group: spice

### Use Cases for SPICE
Draft: draft-ietf-spice-use-cases · Working group: spice
Agenda: "Use Cases for SPICE" draft-ietf-spice-use-cases (Brent Zundel) - 10 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-use-cases/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spice-spice-use-cases-00 | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
This document describes various use cases related to credential exchange in a three party model (issuer, holder, verifier). These use cases aid in the identification of which Secure Patterns for Internet CrEdentials (SPICE) are most in need of specification or detailed documentation.

### Traceability Claims
Draft: draft-prorock-spice-cwt-traceability-claims · Working group: spice
Agenda: "Traceability Claims" draft-prorock-spice-cwt-traceability-claims (Brent Zundel) - 10 min
page: https://datatracker.ietf.org/doc/draft-prorock-spice-cwt-traceability-claims/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spice-traceability-claims-registration-00 | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
This document defines claims to support traceability of physical goods across supply chains, focusing on items such as bills of lading, transport modes, and container manifests. These claims standardize the encoding of essential logistics and transport metadata, facilitating enhanced transparency and accountability in global supply chains. These claims are registered for use in both CBOR Web Tokens (CWTs) and JSON Web Tokens (JWTs).

### GLobal Unique Enterprise (GLUE) Identifiers
Draft: draft-ietf-spice-glue-id · Working group: spice
Agenda: "GLobal Unique Enterprise (GLUE) Identifiers" draft-ietf-spice-glue-id (Brent Zundel) - 10 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-glue-id/ | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
This specification establishes a URI scheme for GLobal Unique Enterprise (GLUE) Identifiers. This enables URI identifiers to be used for businesses and organizations. It enables organizational identities from existing authorities to be represented within this URI scheme.

### OpenID Connect Standard Claims Registration for CBOR Web Tokens
Draft: draft-ietf-spice-oidc-cwt · Working group: spice
Agenda: "OpenID Connect standard claims registration for CBOR Web Tokens" draft-ietf-spice-oidc-cwt (Beltram Maldant) - 15 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-oidc-cwt/ | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
This document registers OpenID Connect standard claims already used in JSON Web Tokens for use in CBOR Web Tokens.

### A reference architecture for direct presentation credential flows
Draft: draft-johansson-direct-presentation-arch · Working group: spice
Agenda: "A reference architecture for direct presentation credential flows' draft-johansson-direct-presentation-arch (Leif Johansson) - 10 min
page: https://datatracker.ietf.org/doc/draft-johansson-direct-presentation-arch/ | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
This document defines a reference architecture for direct presentation flows of digital credentials. The architecture introduces the concept of a presentation mediator as the active component responsible for managing, presenting, and selectively disclosing credentials while preserving a set of security and privacy promises that will also be defined. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/leifj/wallet-refarch.

### Selective Disclosure CBOR Web Tokens (SD-CWT)
Draft: draft-ietf-spice-sd-cwt · Working group: spice
Agenda: "SPICE SD-CWT" draft-ietf-spice-sd-cwt 15+10 min (Rohan Mahy/Henk Birkholz) - 15 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spice-sd-cwt-update-for-ietf123-00 | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
This specification describes a data minimization technique for use with CBOR Web Tokens (CWTs). The approach is inspired by the Selective Disclosure JSON Web Token (SD-JWT), with changes to align with CBOR Object Signing and Encryption (COSE) and CWTs.

### SPICE GLUE
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spice-spice-glue-00 | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

### OpenId Connect claims registration
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spice-openid-connect-claims-registration-00 | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

### Reference Architecture
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spice-reference-architecture-00 | video: https://www.youtube.com/watch?v=LsJ8s8VlHow | materials: https://datatracker.ietf.org/meeting/123/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

## Working Group: spring

### Segment Routing over IPv6 (SRv6) Security Considerations
Draft: draft-ietf-spring-srv6-security · Working group: spring
Agenda: draft-ietf-spring-srv6-security
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-security/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-ietf-123-srv6-security-considerations-update-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
Segment Routing over IPv6 (SRv6) is the instantiation of Segment Routing on the IPv6 data plane, using IPv6 addresses to identify segments. This document discusses security considerations in SRv6 networks, including the potential threats and the possible mitigation methods. The document does not define any new security protocols or extensions to existing protocols.

### Performance Measurement Using Simple Two-Way Active Measurement Protocol (STAMP) for Segment Routing Networks
Draft: draft-ietf-spring-stamp-srpm · Working group: spring
Agenda: draft-ietf-spring-stamp-srpm
page: https://datatracker.ietf.org/doc/draft-ietf-spring-stamp-srpm/ | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
Segment Routing (SR) leverages the source routing paradigm and applies to both Multiprotocol Label Switching (SR-MPLS) and IPv6 (SRv6) data planes. This document describes the procedures for Performance Measurement in SR networks using the Simple Two-Way Active Measurement Protocol (STAMP), as defined in RFC 8762, along with its optional extensions defined in RFC 8972 and further augmented in RFC 9503. The described procedure is used for links and SR paths (including SR Policies, SR IGP best paths, and SR IGP Flexible Algorithm paths), as well as Layer-3 and Layer-2 services in SR networks, and is applicable to both SR-MPLS and SRv6 data planes.

### YANG Data Model for SRv6 Base and Static
Draft: draft-ietf-spring-srv6-yang · Working group: spring
Agenda: draft-ietf-spring-srv6-yang
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-yang/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-update-on-yang-models-for-srv6-base-and-static-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
This document describes a YANG data model for Segment Routing IPv6 (SRv6) base. The model serves as a base framework for configuring and managing an SRv6 subsystem and expected to be augmented by other SRv6 technology models accordingly. Additionally, this document also specifies the model for the SRv6 Static application. The YANG modules in this document conform to the Network Management Datastore Architecture (NMDA).

### YANG Data Model for Segment Routing Policy
Draft: draft-ietf-spring-sr-policy-yang · Working group: spring
Agenda: draft-ietf-spring-sr-policy-yang
page: https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-yang/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-update-on-yang-model-for-sr-policy-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
This document defines a YANG data model for Segment Routing (SR) Policy that can be used for configuring, instantiating, and managing SR policies. The model is generic and applies equally to the MPLS and SRv6 instantiations of SR policies.

### SRv6 Policy SID List Optimization
Draft: draft-ali-spring-srv6-policy-sid-list-optimization · Working group: spring
Agenda: draft-ali-spring-srv6-policy-sid-list-optimization
page: https://datatracker.ietf.org/doc/draft-ali-spring-srv6-policy-sid-list-optimization/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-draft-ali-spring-srv6-policy-sid-list-optimization-00-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
Segment Routing (SR) allows a node to steer a packet flow along any path. SR Policy is an ordered list of segments (i.e., instructions) that represent a source-routed policy. The packets steered into an SR Policy carry an ordered list of segments associated with that SR Policy. An SR Policy can be instantiated SR-MPLS and SRv6 data planes. In some use cases, an SRv6 Policy's SID list ends with the policy endpoint's node SID, and the traffic steered (over policy) already ensures that it is taken to the policy endpoint. In such cases, the SID list can be optimized by excluding the endpoint Node SID when installing the policy. This draft specifies procedures to indicate whether the endpoint's node SID needs to be included or excluded when installing the SRv6 Policy.

### Eligibility Concept in Segment Routing Policies
Draft: draft-karboubi-spring-sr-policy-eligibility · Working group: spring
Agenda: draft-karboubi-spring-sr-policy-eligibility
page: https://datatracker.ietf.org/doc/draft-karboubi-spring-sr-policy-eligibility/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-eligibility-concept-in-segment-routing-policies-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
Segment Routing (SR) introduces new challenges for pinning candidate paths on their intended paths (the path the PCE computed based on provided intent and may have made bandwidth reservations on). The actual path through a network can change or no longer meet the required constraints if a SID list of an SR Policy candidate path is not fully expressed as a list of adjacency SIDs or when a change in the topology does happen. The introduction of the new candidate path eligibility concept permits a path to be signaled and established as operationally up, but controls whether the path is eligible to carry traffic, thus influencing its active state. The eligibility concept allows a system (operator, pce, headend, etc.) to set eligibility as false when path deviations may have occurred, or path constraints are no longer met for one or more SID lists of a candidate path and clear it when candidate path deviations are removed or constraints are met again.

### SID as source address in SRv6
Draft: draft-yang-spring-sid-as-source-address · Working group: spring
Agenda: draft-yang-spring-sid-as-source-address
page: https://datatracker.ietf.org/doc/draft-yang-spring-sid-as-source-address/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-sid-as-source-01 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. Both the carrier market and the enterprise market are adopting SRv6 for end-to-end service delivery. However, if a firewall exists along an SRv6 path, not only legitimate SRv6 traffic but also ICMP packets generated on SRv6 transit node will be dropped. This proposal addresses this issue by using SID as source address in SRv6 packets.

### SRv6 Path Verification
Draft: draft-yang-spring-srv6-verification · Working group: spring
Agenda: draft-yang-spring-srv6-verification
page: https://datatracker.ietf.org/doc/draft-yang-spring-srv6-verification/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-9-srv6-path-verification-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. However, we have also observed that SRv6 is beginning to extend toward customer site devices, e.g., SD-WAN and enterprise network deployments. Both of the scenarios can be deployed in third-party clouds or at customer sites. This introduces certain security risks, such as packet injection and path manipulation attacks. Section 6 of [I-D.draft-ietf-spring-srv6-security] identifies these risks as well, including Section 6.2.1 on Modification Attacks and Section 6.2.3 on Packet Insertion. This proposal mitigates these risks by enhancing the HMAC mechanism defined in [RFC8754].

### Multipath Traffic Engineering for Segment Routing
Draft: draft-stone-spring-mpte-sr · Working group: spring
Agenda: draft-stone-spring-mpte-sr
page: https://datatracker.ietf.org/doc/draft-stone-spring-mpte-sr/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-multipath-traffic-engineering-for-segment-routing-01 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
This document describes a mechanism to achieve Multipath Traffic Engineering for Segment Routing based networks. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Source Packet Routing in Networking Working Group mailing list (spring@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/spring/. Source for this draft and an issue tracker can be found at https://github.com/astone282/draft-stone-spring-mpte-sr.

### Performance Measurement Using STAMP for Segment Routing Networks
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-spring-performance-measurement-using-stamp-for-segment-routing-networks-00 | video: https://www.youtube.com/watch?v=ciGVGa2U3NQ | materials: https://datatracker.ietf.org/meeting/123/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

## Working Group: srv6ops

### SRv6 Deployment Options
Draft: draft-mcbride-srv6ops-srv6-deployment · Working group: srv6ops
Agenda: draft-mcbride-srv6ops-srv6-deployment
page: https://datatracker.ietf.org/doc/draft-mcbride-srv6ops-srv6-deployment/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-31-compressed-srv6-deployment-and-operations-white-paper-05 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
When deciding to migrate a network from MPLS/SR-MPLS to SRv6, common questions involve how to go about performing the migration, what's the least amount of impact to an existing network and what existing techniques are available. This document presents various options for networks being migrated from MPLS/SR-MPLS to SRv6.

### SRv6 End-to-End DC Frontend and WAN
Draft: draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan · Working group: srv6ops
Agenda: draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan
page: https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-42-srv6-end-to-end-dc-frontend-wan-00 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
The SRv6 Network Programming architecture allows an application to control the end-to-end journey of traffic flows through different network domains in a unified and stateless manner, without requiring intermediate network devices to maintain per-flow information. This document covers its application to the integration of data center (DC) and wide area network (WAN) architectures using SRv6 with uSID (NEXT-CSID). It describes a unified IPv6 data plane from tenant workloads through the DC frontend to Internet peering, replacing designs that stitch separate overlay protocols at the Data Center Interconnect (DCI). The solution enhances scalability and enables flexible stateless service insertion by unifying underlay, overlay, and service steering under SRv6.

### SRv6 for Deterministic Path Placement in AI Backends
Draft: draft-filsfils-srv6ops-srv6-ai-backend · Working group: srv6ops
Agenda: draft-filsfils-srv6ops-srv6-ai-backend
page: https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-43-srv6-for-deterministic-path-placement-in-the-ai-backend-00 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
This document describes how SRv6 NEXT-CSID enables deterministic path placement in AI backend fabrics through L3-L4 integration on end hosts: the transport stack on the NIC encodes each path as an ordered list of segments (a NEXT-CSID network program) in the packet header, while the fabric forwards statelessly. It explains operational benefits including deterministic probing and alignment with hyperscale production deployments.

### Extending ICMPv6 for SRv6-related Information Validation
Draft: draft-liu-6man-icmp-verification · Working group: srv6ops
Agenda: draft-liu-6man-icmp-verification
page: https://datatracker.ietf.org/doc/draft-liu-6man-icmp-verification/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-srv6-sid-related-information-validation-00 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
This document introduces the mechanism to verify the data plane against the control plane and detect data plane failures in IPv6/SRv6 networks by extending ICMPv6 messages.

### Advancing Deutsche Telekom’s Traffic Engineering for SRv6
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-21-advancing-deutsche-telekoms-traffic-engineering-for-srv6-01 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 @ IX.br
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-22-srv6-ixbr-01 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 @ MTS Web Services
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-srv6-a-cloud-use-case-mws-00 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Deployment Options
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-srv6ops-srv6-deployment-options-00 | video: https://www.youtube.com/watch?v=HsoGR_8m2UM | materials: https://datatracker.ietf.org/meeting/123/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

## Working Group: tcpm

### Proportional Rate Reduction
Draft: draft-ietf-tcpm-prr-rfc6937bis · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-prr-rfc6937bis-21
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-prr-rfc6937bis/ | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
This document specifies a standards-track version of the Proportional Rate Reduction (PRR) algorithm that obsoletes the experimental version described in RFC6937. PRR regulates the amount of data sent by TCP or other transport protocols during fast recovery. PRR accurately regulates the actual flight size through recovery such that at the end of recovery it will be as close as possible to the slow start threshold (ssthresh), as determined by the congestion control algorithm.

### TCP ACK Rate Request Option
Draft: draft-ietf-tcpm-ack-rate-request · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-ack-rate-request-09
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-ack-rate-request/ | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
TCP Delayed Acknowledgments (ACKs) is a widely deployed mechanism that allows reducing protocol overhead in many scenarios. However, Delayed ACKs may also contribute to suboptimal performance. When a relatively large congestion window (cwnd) can be used, less frequent ACKs may be desirable. On the other hand, in relatively small cwnd scenarios, eliciting an immediate ACK may avoid unnecessary delays that may be incurred by the Delayed ACKs mechanism. This document specifies the TCP ACK Rate Request (TARR) option. This option allows a sender to request the ACK rate to be used by a receiver, and it also allows to request immediate ACKs from a receiver.

### An Upgraded TCP Session Type
Draft: draft-bonica-tcpm-extended-options · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-bonica-tcpm-extended-options-00
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tcpm-extended-options-00 | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
Currently, TCP maintains ordinary sessions (SES-O) in which ordinary segments (SEG-O) are exchanged. Each SEG-O can accommodate up to 40 octets of options. In the future, applications may require more than 40 octets of options. For example, an application may use a 36-byte TCP Authentication Option (TCP-AO), leaving insufficient space for other required options. Therefore, this document describes an experiment in which upgraded sessions (SES-U) and upgraded segments (SEG-U) are introduced. Each SEG-U can accommodate up to 1,016 octets of Individual Options.

### TCP ETS: Extensible Timestamp Options
Draft: draft-yang-tcpm-ets · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-yang-tcpm-ets-00
page: https://datatracker.ietf.org/doc/draft-yang-tcpm-ets/ | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
This document presents ETS: an Extensible TimeStamps option for TCP. It allows hosts to use microseconds as the unit for timestamps to improve the precision of timestamps, and extends the information provided in the [RFC7323] TCP Timestamps Option by including the receiver delay in the TSecr echoing, so that the receiver of the ACK is able to more accurately estimate the portion of the RTT that resulted from time traveling through the network. The ETS option format is extensible, so that future extensions can add further information without the overhead of extra TCP option kind and length fields.

### Multipath TCP with longer DSS mappings
Draft: draft-baerts-tcpm-mptcpdss · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-baerts-tcpm-mptcpdss-00
page: https://datatracker.ietf.org/doc/draft-baerts-tcpm-mptcpdss/ | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
This document proposes an extension to improve Multipath TCP based on operational experience by allowing Multipath TCP to use DSS mappings that are longer than 64 KBytes.

### Multipath TCP with external keys
Draft: draft-baerts-tcpm-mptcpext · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-baerts-tcpm-mptcpext-00
page: https://datatracker.ietf.org/doc/draft-baerts-tcpm-mptcpext/ | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
This document proposes an extension to Multipath TCP that allows application layer protocols such as TLS or SSH to provide keys to authenticate the creation of new subflows.

### prr
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tcpm-prr-00 | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### tarr
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tcpm-tarr-00 | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### ets
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tcpm-ets-00 | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### mptcp-extensions
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tcpm-mptcp-extensions-00 | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

### optimistic-ack-attack
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tcpm-optimistic-ack-attack-00 | video: https://www.youtube.com/watch?v=6JtuA6pUPzA | materials: https://datatracker.ietf.org/meeting/123/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

## Working Group: tls

### A well-known URI for publishing service parameters
Draft: draft-ietf-tls-wkech · Working group: tls
Agenda: draft-ietf-tls-wkech (5min)
page: https://datatracker.ietf.org/doc/draft-ietf-tls-wkech/ | materials: https://datatracker.ietf.org/meeting/123/session/tls
We define a well-known URI at which an HTTP origin can inform an authoritative DNS server, or other interested parties, about its Service Bindings. Service binding data can include Encrypted ClientHello (ECH) configurations, that may change frequently. This allows the HTTP origin, in collaboration with DNS infrastructure elements, to publish and rotate its own ECH keys. Other service binding data such as information about TLS supported groups is unlikely to change quickly, but the HTTP origin is much more likely to have accurate information when changes do occur. Service data published via this mechanism is typically available via an HTTPS or SVCB resource record.

### Extended Key Update for Transport Layer Security (TLS) 1.3
Draft: draft-ietf-tls-extended-key-update · Working group: tls
Agenda: draft-ietf-tls-extended-key-update
page: https://datatracker.ietf.org/doc/draft-ietf-tls-extended-key-update/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-extended-key-update-01 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
TLS 1.3 ensures forward secrecy by performing an ephemeral Diffie- Hellman key exchange during the initial handshake, protecting past communications even if a party's long-term keys (typically a private key with a corresponding certificate) are later compromised. While the built-in KeyUpdate mechanism allows application traffic keys to be refreshed during a session, it does not incorporate fresh entropy from a new key exchange and therefore does not provide post- compromise security. This limitation can pose a security risk in long-lived sessions, such as those found in industrial IoT or telecommunications environments. To address this, this specification defines an extended key update mechanism that performs a fresh execution of the key exchange negotiated during the initial handshake within an active session, thereby ensuring post-compromise security. By forcing attackers to exfiltrate new key material repeatedly, this approach mitigates the risks associated with static key compromise. Regular renewal of session keys helps contain the impact of such compromises. The extension is applicable to both TLS 1.3 and DTLS 1.3.

### Large Record Sizes for TLS and DTLS with Reduced Overhead
Draft: draft-ietf-tls-super-jumbo-record-limit · Working group: tls
Agenda: draft-ietf-tls-super-jumbo-record-limit
page: https://datatracker.ietf.org/doc/draft-ietf-tls-super-jumbo-record-limit/ | materials: https://datatracker.ietf.org/meeting/123/session/tls
TLS 1.3 records limit the inner plaintext (TLSInnerPlaintext) size to 2^14 + 1 bytes, which includes one byte for the content type. DTLS 1.3 uses the same plaintext size limit. This document defines a TLS extension that allows endpoints to advertise larger per-direction maximum inner plaintext sizes, up to 2^30 - 256 bytes, while reducing overhead in TLS 1.3 and DTLS 1.3 record headers.

### ML-KEM Post-Quantum Key Agreement for TLS 1.3
Draft: draft-ietf-tls-mlkem · Working group: tls
Agenda: draft-ietf-tls-mlkem
page: https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-ml-kem-post-quantum-key-agreement-for-tls-13-ietf-123-madrid-00 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as NamedGroups and registers IANA values in the TLS Supported Groups registry for use in TLS 1.3 to achieve post-quantum (PQ) key establishment.

### A Password Authenticated Key Exchange Extension for TLS 1.3
Draft: draft-bmw-tls-pake13 · Working group: tls
Agenda: draft-bmw-tls-pake13
page: https://datatracker.ietf.org/doc/draft-bmw-tls-pake13/ | materials: https://datatracker.ietf.org/meeting/123/session/tls
The pre-shared key mechanism available in TLS 1.3 is not suitable for usage with low-entropy keys, such as passwords entered by users. This document describes an extension that enables the use of password-authenticated key exchange protocols with TLS 1.3.

### Post-Quantum Traditional (PQ/T) Hybrid Authentication with Dual Certificates in TLS 1.3
Draft: draft-yusef-tls-pqt-dual-certs · Working group: tls
Agenda: draft-yusef-tls-pqt-dual-certs
page: https://datatracker.ietf.org/doc/draft-yusef-tls-pqt-dual-certs/ | materials: https://datatracker.ietf.org/meeting/123/session/tls
The anticipated emergence of cryptographically relevant quantum computers (CRQCs) poses a threat to the authentication mechanisms used in TLS 1.3. This document defines a hybrid authentication mechanism that uses two independent certificates, one traditional and one post-quantum, ensuring that an attacker must break both algorithms to compromise a TLS connection. The two certificate chains are carried in a single Certificate message and two independent signatures are encoded in the CertificateVerify message.

### Workload Identifier Origin Hint for TLS ClientHello
Draft: draft-rosomakho-tls-wimse-cert-hint · Working group: tls
Agenda: draft-rosomakho-tls-wimse-cert-hint
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-sessb-workload-identifier-scope-hint-00 | video: https://www.youtube.com/watch?v=1KsqfSxLWpo | materials: https://datatracker.ietf.org/meeting/123/session/tls
This document defines a TLS extension that allows clients to indicate one or more workload identifier origins in the ClientHello message. Each origin consists of a URI scheme and trust domain component, representing the administrative domain and identifier namespace in which the client operates. These identifier origins serve as hints to enable the server to determine whether client authentication is required and which policies or trust anchors should apply. This mechanism improves efficiency in mutual TLS deployments while minimising the exposure of sensitive identifier information. To protect confidentiality, this extension can be used in conjunction with Encrypted Client Hello (ECH).

### Certificate Update in TLS 1.3
Draft: draft-rosomakho-tls-cert-update · Working group: tls
Agenda: draft-rosomakho-tls-cert-update
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-cert-update/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-sessb-tls-13-certificate-update-00 | video: https://www.youtube.com/watch?v=1KsqfSxLWpo | materials: https://datatracker.ietf.org/meeting/123/session/tls
This document defines a mechanism that enables TLS 1.3 endpoints to update their certificates during the lifetime of a connection using Exported Authenticators. A new extension is introduced to negotiate support for certificate update at handshake time. When negotiated, either endpoint can provide a post-handshake authenticator containing an updated certificate, delivered via a new handshake message. This mechanism allows long-lived TLS connections to remain valid across certificate rotations without requiring session termination.

### Reliable Transparency and Revocation Mechanisms
Draft: draft-mcmillion-tls-transparency-revocation · Working group: tls
Agenda: draft-mcmillion-tls-transparency-revocation
page: https://datatracker.ietf.org/doc/draft-mcmillion-tls-transparency-revocation/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-reliable-transparency-and-revocation-mechanisms-00 | video: https://www.youtube.com/watch?v=1KsqfSxLWpo | materials: https://datatracker.ietf.org/meeting/123/session/tls
This document describes reliable mechanisms for the publication and revocation of Transport Layer Security (TLS) certificates. This reliability takes several forms. First, it provides browsers a strong guarantee that all certificates they accept are truly published and unrevoked at the time they're accepted. Second, it allows operators to monitor for mis-issuances related to their websites in a highly efficient way without relying on third-party services. Third, it provides a high degree of operational redundancy to minimize the risk of cascading outages.

### Proposed Document Template for TLS FATT Process
Draft: draft-usama-tls-fatt-extension · Working group: tls
Agenda: draft-usama-tls-fatt-extension
page: https://datatracker.ietf.org/doc/draft-usama-tls-fatt-extension/ | materials: https://datatracker.ietf.org/meeting/123/session/tls
This document applies only to non-trivial extensions of TLS, which require formal analysis. FATT process has successfully discovered CVEs of *CVSS 7.5* and most recently expected *CVSS 9.1* in the *production* implementations of the drafts proposed for adoption in the TLS WG. To achieve high cryptographic assurances, this document proposes the drafts specify a clear threat model and informal security goals in the Security Considerations section, as well as motivation and a protocol diagram in the draft.

### WKECH
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-wkech-00 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Large Record Size
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-large-record-size-00 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### TLS PAKE Extension
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-tls-pake-extension-00 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Dual Certificates in TLS 1.3
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-sessa-dual-certificates-in-tls-13-00 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### FATT Process Extensions
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-sessb-fatt-process-extensions-00 | video: https://www.youtube.com/watch?v=QZd6sjcPeRo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Remote Attestation with Exported Authenticators
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-remote-attestation-with-exported-authenticators-00 | video: https://www.youtube.com/watch?v=1KsqfSxLWpo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### ECH Signed Config
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tls-ech-signed-config-00 | video: https://www.youtube.com/watch?v=1KsqfSxLWpo | materials: https://datatracker.ietf.org/meeting/123/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

## Working Group: tsvwg

### Quic Logging for Convergence of Congestion Control from Retained State
Draft: draft-ietf-tsvwg-careful-resume-qlog · Working group: tsvwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-careful-resume-qlog/
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-careful-resume-qlog/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-careful-resume-qlog-01 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
This document specifies a logging format for a cautious method for Careful Resume when using the IETF quic transport protocol. It defines the logging format for qlog.

### Operational Guidance on Coexistence with Classic ECN during L4S Deployment
Draft: draft-ietf-tsvwg-l4sops · Working group: tsvwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/ | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
This document provides guidance in order to ensure successful deployment of Low Latency Low Loss Scalable throughput (L4S) in the Internet. Other L4S documents provide guidance for running an L4S experiment, but this document is focused solely on potential interactions between L4S flows and flows using the original ('Classic') ECN over a Classic ECN bottleneck. The document discusses the potential outcomes of these interactions, describes mechanisms to detect the presence of Classic ECN bottlenecks, and identifies opportunities to prevent and/or detect and resolve fairness problems in such networks. This guidance is aimed at operators of end-systems, operators of networks, and researchers.

### ISP Dual Queue Networking Deployment Observations
Draft: draft-livingood-low-latency-deployment · Working group: tsvwg
Agenda: https://datatracker.ietf.org/doc/draft-livingood-low-latency-deployment/
page: https://datatracker.ietf.org/doc/draft-livingood-low-latency-deployment/ | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
The IETF's Transport and Services Working Group (TSVWG) has finalized experimental RFCs for Low Latency, Low Loss, Scalable Throughput (L4S) and new Non-Queue-Building (NQB) per hop behavior. These documents describe a new architecture and protocol for deploying low latency networking. Since deployment decisions are left to implementers, this document explores some of the implications of those decisions and makes suggestions that can help drive adoption and acceptance of L4S and NQB based on observations from the world's first large scale deployment.

### Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm
Draft: draft-tahiliani-tsvwg-fq-pie · Working group: tsvwg
Agenda: https://datatracker.ietf.org/doc/draft-tahiliani-tsvwg-fq-pie/
page: https://datatracker.ietf.org/doc/draft-tahiliani-tsvwg-fq-pie/ | slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-fq-pie-00 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
This document presents Flow Queue Proportional Integral controller Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue Management (AQM) algorithm to isolate flows and tackle the problem of bufferbloat. FQ-PIE uses hashing to classify incoming packets into different queues and provide flow isolation. Packets are dequeued by using a variant of the round robin scheduler. Each such flow is managed by the PIE algorithm to maintain high link utilization while controlling the queue delay to a target value.

### Datagram Transport Layer Security (DTLS) based key-management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-westerlund-tsvwg-sctp-dtls-handshake · Working group: tsvwg
Agenda: https://datatracker.ietf.org/doc/draft-westerlund-tsvwg-sctp-dtls-handshake/
page: https://datatracker.ietf.org/doc/draft-westerlund-tsvwg-sctp-dtls-handshake/ | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
This document defines a key-management solution based on Datagram Transport Layer Security 1.3 (DTLS) to protect the content of Stream Control Transmission Protocol (SCTP) packets using the packet protection framework provided by the SCTP DTLS chunk. The combination provides encryption, source authentication, integrity and replay protection for the SCTP association with in-band DTLS based key-management and mutual authentication of the peers. The specification is enabling very long-lived sessions of weeks and months and supports mutual re-authentication and rekeying with ephemeral key exchange. The key-management solution does not require any additional defined features or implementation support beyond core DTLS 1.3. This is intended as a replacement to using DTLS/SCTP (RFC6083) and SCTP-AUTH (RFC4895).

### Using Datagram Transport Layer Security (DTLS) for Key Management for the Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-tuexen-tsvwg-dtls-chunk-key-management · Working group: tsvwg
Agenda: https://datatracker.ietf.org/doc/draft-tuexen-tsvwg-dtls-chunk-key-management/
page: https://datatracker.ietf.org/doc/draft-tuexen-tsvwg-dtls-chunk-key-management/ | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
This document defines how Datagram Transport Layer Security (DTLS) 1.3 is used to establish keys for securing SCTP using the DTLS Chunk mechanism. It specifies how a DTLS handshake is used to establish the initial security context for an SCTP association and describes procedures for key updates and post-handshake authentication. The goal is to enable authenticated, and confidential communication over SCTP using the DTLS Chunk, leveraging standardized DTLS features for key management and rekeying.

### L4S Operational Guidance
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-l4s-operational-guidance-00 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### L4S Deployment - Livingood
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-sessa-l4s-deployment-livingood-00 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### Design Team Report on DTLS for SCTP
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-design-team-report-on-dtls-for-sctp-00 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### L4S Interop Events
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-l4s-interop-events-00 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### L4S with Apple devices
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-tsvwg-l4s-with-apple-devices-00 | video: https://www.youtube.com/watch?v=ly851tMUs4A | materials: https://datatracker.ietf.org/meeting/123/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

## Working Group: v6ops

### Tommy Jensen - CLAT Recommendations
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-01-tommy-jensen-clat-recommendations-01 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Linkova - Using Dummy IPv4 Address and Node Identification Extensions for IP/ICMP translators (XLATs)
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-02-linkova-using-dummy-ipv4-address-and-node-identification-extensions-for-ipicmp-translators-xlats-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Ben Patton - Basic Requirements for IPv6 Customer Edge Routers - 7084bis
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-basic-requirements-for-ipv6-customer-edge-routers-7084bis-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Ondřej Caletka - Filtering address records in stub resolvers
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-filtering-address-records-in-stub-resolvers-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jordi - slides
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-05-jordi-slides-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Chenhao Ma - Considerations of Gradual IPv6-only Deployment in 5G Mobile Networks
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-considerations-of-gradual-ipv6-only-deployment-in-5g-mobile-networks-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Cong Li - Basic Requirements for IPv6-only Provider Edge Routers
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-08-cong-li-basic-requirements-for-ipv6-only-provider-edge-routers-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Nick - CLAT Implementation status on non-mobile platforms
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-v6ops-clat-implementation-status-on-non-mobile-platforms-00 | video: https://www.youtube.com/watch?v=T8qofHbakzY | materials: https://datatracker.ietf.org/meeting/123/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

## Working Group: wimse

### WIMSE and Agentic AI
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-wimse-and-agentic-ai-01 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Zero Trust Sovereign AI - WIMSE impact
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-zero-trust-sovereign-ai-wimse-impact-04 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload to workload draft
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-slides-123-wimse-workload-to-workload-draft-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WImse Architecture (draft)
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-wimse-architecture-draft-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Workload Identifier
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-workload-identifier-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Accessing static secrets in Multi Service Environments
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-accessing-static-secrets-in-multi-service-environments-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Headless JWT Authentication and Authorization
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-wimse-headless-jwt-authentication-and-authorization-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Workload Identity Practices
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-wimse-workload-identity-practices-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Trustworthy Workload Identity Extensions for WIMSE
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-trustworthy-workload-identity-extensions-for-wimse-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Architecture
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-wimse-architecture-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Credential Exchange
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/123/materials/slides-123-wimse-wimse-credential-exchange-00 | video: https://www.youtube.com/watch?v=Mv4lgHLxOH4 | materials: https://datatracker.ietf.org/meeting/123/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

