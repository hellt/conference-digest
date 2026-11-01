>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-126. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-126.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-126.md
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

Below is the program for IETF 126 (Vienna) (standards). Read it and produce a digest
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
conference: IETF 126 (Vienna)
type: standards
source_url: https://datatracker.ietf.org/meeting/126/agenda.json
generated: 2026-11-01
registry_key: ietf-126
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Working Group: 6man

### IPv6 wants 802.11 Flexible Multicast Service
Draft: draft-ietf-6man-ieee80211-fms · Working group: 6man
Agenda: draft-ietf-6man-ieee80211-fms , David Lamparter, 10 mins
page: https://datatracker.ietf.org/doc/draft-ietf-6man-ieee80211-fms/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-ipv6-wants-80211-flexible-multicast-service-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
IEEE 802.11 Flexible Multicast Service (FMS) addresses reliability issues in IPv6 due to aggressive powersave optimizations in 802.11 client devices. The intent of this document is to collect consensus in the IETF 6man (IPv6 Maintenance) working group to request either/both the IEEE 802.11 Working Group and/or the Wifi Alliance's certification process to make implementing FMS a requirement.

### Sub-Link Scoped IPv6 Multicast Addressing
Draft: draft-ietf-6man-sub-link-scope-multicast · Working group: 6man
Agenda: draft-ietf-6man-sub-link-scope-multicast , David Lamparter, 10 mins
page: https://datatracker.ietf.org/doc/draft-ietf-6man-sub-link-scope-multicast/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-sub-link-scoped-ipv6-multicast-addressing-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
The IPv6 addressing architecture for multicast has the scope of a multicast group embedded in its address, with the smallest non- reserved scopes being interface-local and link-local, numbered 1 and 2. This document suggests the introduction of a scope inbetween these two, for use with lower-layer transport multicast that reaches parts of a link. Since there is no room to insert a scope value for this, a separate address block is used. A mapping for Ethernet as lower-layer transport is provided.

### IPv6 Node Requirements
Draft: draft-ietf-6man-rfc8504-bis · Working group: 6man
Agenda: draft-ietf-6man-rfc8504-bis
page: https://datatracker.ietf.org/doc/draft-ietf-6man-rfc8504-bis/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-ipv6-node-requirements-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
This document defines requirements for IPv6 nodes. It is expected that IPv6 will be deployed in a wide range of devices and situations. Specifying the requirements for IPv6 nodes allows IPv6 to function well and interoperate in a large number of situations and deployments. This document obsoletes RFC 8504, and in turn RFC 6434 and its predecessor, RFC 4294.

### The IPv6 Loopback Address Prefix
Draft: draft-kumari-ipv6-loopback · Working group: 6man
Agenda: draft-kumari-ipv6-loopback ,
page: https://datatracker.ietf.org/doc/draft-kumari-ipv6-loopback/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-04-the-ipv6-loopback-address-prefix-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
{ *Editor's note:* This document requests the allocation of a new IPv6 address prefix to be used for loopback instead of expanding into the existing ::/96. The specific prefix to be allocated is TBD/96, and the document updates the relevant RFCs and IANA registries to reflect this change. } This document updates the IP Version 6 Address Architecture to expand the size of the IPv6 loopback space from a single address to a /96 prefix. This change allows for a much larger number of loopback addresses in IPv6, which can be used for inter-process communication within a host and for network diagnostics. The document also updates the IANA IPv6 Address registry and the IPv6 Special Purpose Address registry to reflect this change. It updates RFC4291 to reflect the new loopback prefix and its functional semantics.

### A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label
Draft: draft-hu-6man-ipv6-flowlabel-load-balancing-rdma · Working group: 6man
Agenda: draft-hu-6man-ipv6-flowlabel-load-balancing-rdma
page: https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-slides-126-6man-ipv6-flowlabel-load-balancing-rdma-01-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
This document proposes a method for achieving flow-level load balancing in RoCEv2 (RDMA over Converged Ethernet version 2) networks. Traditional per-flow load balancing based on the 5-tuple cannot distinguish between different RDMA sessions that share the same 5-tuple. This causes "elephant flows" to be hashed to the same path, leading to network congestion. This method resolves this issue by having the ingress network device (e.g., a top-of-rack switch or router) parse the QP (Queue Pair) information from the IB BTH (Base Transport Header) and IB DETH (Datagram Extended Transport Header) headers of the RoCEv2 packet. By combining this with portions of the IPv6 source and destination addresses as an entropy source, a CRC32 hash algorithm generates a 20-bit value, which is then written into the Flow Label field of the IPv6 header. Network devices can subsequently use the updated "5-tuple + Flow Label" for more granular flow-level load balancing, thereby effectively improving transmission efficiency in high-performance networks such as AI computing.

### ICMP Error Handling for VPNs in SRv6 Networks
Draft: draft-varhal-6man-icmp-srv6-vpn · Working group: 6man
Agenda: draft-varhal-6man-icmp-srv6-vpn
page: https://datatracker.ietf.org/doc/draft-varhal-6man-icmp-srv6-vpn/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-icmp-error-handling-for-vpns-in-srv6-networks-draft-varhal-6man-icmp-srv6-vpn-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
This document specifies ICMP error handling in SRv6-based Virtual Private Networks, that support direct localization of failures. It provides a solution for connectivity check and fault localization without adding complexity to P nodes and keeps P nodes service agnostic. ICMP processing is changed only on ingress PE nodes and gains from adding VPN-specific information to the SRv6 encapsulated packet. Egress PE nodes are not involved in the forwarding of the ICMP error messages therefore, the solution provides visibility upto the failure even if ingress PE to egress PE connectivity is broken within the SR domain.

### ICMP Error Handling in SRv6 based VPN Networks
Draft: draft-ali-6man-srv6-vpn-icmp-error-handling · Working group: 6man
Agenda: draft-ali-6man-srv6-vpn-icmp-error-handling
page: https://datatracker.ietf.org/doc/draft-ali-6man-srv6-vpn-icmp-error-handling/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-draft-ali-6man-srv6-vpn-icmp-error-handling-04-00 | video: https://youtu.be/MR_SV1EFB6Y | materials: https://datatracker.ietf.org/meeting/126/session/6man
The document specifies procedures for handling ICMP error in SRv6-based Virtual Private Network (VPN).

## Working Group: acme

### ACME Integrations for Device Certificate Enrollment
Draft: draft-ietf-acme-integrations · Working group: acme
Agenda: draft-ietf-acme-integrations
page: https://datatracker.ietf.org/doc/draft-ietf-acme-integrations/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document outlines multiple advanced use cases and integrations that ACME facilitates without any modifications or enhancements required to the base ACME specification. The use cases include ACME integration with EST, BRSKI and TEAP.

### Automatic Certificate Management Environment (ACME) Device Attestation Extension
Draft: draft-ietf-acme-device-attest · Working group: acme
Agenda: draft-ietf-acme-device-attest
page: https://datatracker.ietf.org/doc/draft-ietf-acme-device-attest/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document specifies new identifiers and a challenge for the Automatic Certificate Management Environment (ACME) protocol which allows validating the identity of a device using attestation. This document updates RFC 8555 to enable a privacy-preserving mode for the identifiers defined in this document.

### JWTClaimConstraints profile of ACME Authority Token
Draft: draft-ietf-acme-authority-token-jwtclaimcon · Working group: acme
Agenda: draft-ietf-acme-authority-token-jwtclaimcon (in WGLC) – [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-authority-token-jwtclaimcon/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document defines an authority token profile for the validation of JWTClaimConstraints and EnhancedJWTClaimConstraints certificate extensions within the Automated Certificate Management Environment (ACME) protocol. This profile is based on the Authority Token framework and establishes the specific ACME identifier type, challenge mechanism, and token format necessary to authorize a client to request a certificate containing these constraints.

### Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge
Draft: draft-ietf-acme-dns-account-label · Working group: acme
Agenda: draft-ietf-acme-dns-account-label (in WGLC) – [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dns-account-label/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document outlines a new DNS-based challenge type for the ACME protocol that enables multiple independent systems to authorize a single domain name concurrently. By adding a unique label to the DNS validation record name, the dns-account-01 challenge avoids CNAME delegation conflicts inherent to the dns-01 challenge type. This is particularly valuable for multi-region or multi-cloud deployments that wish to rely upon DNS-based domain control validation and need to independently obtain certificates for the same domain.

### Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation
Draft: draft-ietf-acme-dns-persist · Working group: acme
Agenda: draft-ietf-acme-dns-persist – [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-dns-persist/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document specifies "dns-persist-01", a new validation method for the Automated Certificate Management Environment (ACME) protocol. This method allows a Certification Authority (CA) to verify control over a domain by confirming the presence of a persistent DNS TXT record containing CA and account identification information. This method is particularly suited for environments where traditional challenge methods are impractical, such as multi-tenant hosting platforms, enterprise DNS environments, and IoT deployments. The validation method is designed with a strong focus on security and robustness, incorporating widely adopted industry best practices for persistent domain control validation. This design aims to make it suitable for Certification Authorities operating under various policy environments, including those that align with the CA/Browser Forum Baseline Requirements.

### Automated Certificate Management Environment (ACME) Profiles Extension
Draft: draft-ietf-acme-profiles · Working group: acme
Agenda: draft-ietf-acme-profiles – [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-profiles/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document defines how an ACME Server may offer a selection of different certificate profiles to ACME Clients, and how those clients may indicate which profile they want.

### Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type
Draft: draft-ietf-acme-rats · Working group: acme
Agenda: draft-ietf-acme-rats – [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-rats/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document describes an approach where an ACME Server can challenge an ACME Client to provide Evidence, Endorsements, or Attestation Result according to the Remote ATtestation procedureS (RATS) framework in any format supported by the Conceptual Message Wrapper (CMW). The ACME Server can optionally challenge the Client for specific claims that it wishes attestation for.

### Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0
Draft: draft-ietf-acme-openid-federation · Working group: acme
Agenda: draft-ietf-acme-openid-federation – [no presentation]
page: https://datatracker.ietf.org/doc/draft-ietf-acme-openid-federation/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
The Automatic Certificate Management Environment (ACME) protocol allows server operators to obtain TLS certificates for their websites, based on a demonstration of control over the website's domain via a fully-automated challenge/response protocol. OpenID Federation 1.0 defines how to build a trust infrastructure using a trusted third-party model. It uses a trust evaluation mechanism to attest to the possession of private keys, protocol specific metadata and miscellaneous administrative and technical information related to a specific entity. This document defines how X.509 certificates associated with a given OpenID Federation Entity can be issued by an X.509 Certification Authority through the ACME protocol to the organizations which are part of a federation built on top of OpenID Federation 1.0.

### Automated Certificate Management Environment (ACME) Extension for Public Key Challenges
Draft: draft-geng-acme-public-key · Working group: acme
Agenda: draft-geng-acme-public-key – Xin Chen [10 mins]
page: https://datatracker.ietf.org/doc/draft-geng-acme-public-key/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-acme-acme-extension-for-public-key-challenges-00 | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
The Automatic Certificate Management Environment (ACME) [RFC8555] requires a PKCS#10 Certificate Signing Request (CSR) at the finalization stage. This document defines a new ACME challenge type, "pk-01", that allows a client to prove possession of a private key directly, without constructing a CSR. The primary motivation is to support key types that cannot generate CSR self-signatures, notably post-quantum Key Encapsulation Mechanism (KEM) keys. The client declares the public key via a popKey field in the "newOrder" request; the server attaches the "pk-01" challenge to existing identifier authorizations. When all required authorizations are satisfied, the ACME server issues a certificate using the validated public key and the authorized identifiers, eliminating the need for a CSR in the finalization stage.

### Merkle Tree Certificates
Draft: draft-ietf-plants-merkle-tree-certs · Working group: acme
Agenda: PLANTS / MTC ( draft-ietf-plants-merkle-tree-certs-04 , Section 9) – David Benjamin [10 mins]
page: https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document describes Merkle Tree certificates, a new form of X.509 certificates which integrate public logging of the certificate, in the style of Certificate Transparency. The integrated design reduces logging overhead in the face of both shorter-lived certificates and large post-quantum signature algorithms, while still achieving comparable security properties to existing X.509 constructions and Certificate Transparency. Merkle Tree certificates additionally admit an optional size optimization that avoids signatures altogether, at the cost of only applying to up-to-date relying parties and older certificates.

### Quantum-Ready ACME Mechanism
Draft: draft-ar-acme-pqc-tlsjws · Working group: acme
Agenda: draft-ar-acme-pqc-tlsjws – Aritra [10 mins]
page: https://datatracker.ietf.org/doc/draft-ar-acme-pqc-tlsjws/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-acme-quantum-ready-profiles-for-acme-00 | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document updates RFC 8555 (ACME) to specify post-quantum and PQ/ T hybrid cryptographic requirements for quantum-ready deployments. The Automatic Certificate Management Environment (ACME) automates certificate issuance, validation, and management over HTTPS using JSON Web Signatures (JWS) to authenticate client request payloads. Current ACME deployments rely on traditional public-key algorithms in both JWS and TLS, which are vulnerable to attacks from Cryptographically Relevant Quantum Computers (CRQCs). This specification defines PQC or PQ/T hybrid TLS 1.3 key establishment and specifies PQC or PQ/T authentication mechanisms for JWS and TLS under the quantum-ready ACME mechanism. This specification enables ACME clients and servers to achieve quantum-resistant confidentiality and authentication.

### Post-Quantum Cryptographic Agility Profile for ACME
Draft: draft-vicente-acme-pqc-agility-profile · Working group: acme
Agenda: draft-vicente-acme-pqc-agility-profile – Brian?
page: https://datatracker.ietf.org/doc/draft-vicente-acme-pqc-agility-profile/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document defines an Automated Certificate Management Environment (ACME) [RFC8555] profile extension that enables ACME servers and clients to express per-account and per-order post-quantum cryptographic (PQC) posture. The extension introduces a pqcAgility metadata object in the ACME directory, an optional pqcAgility member in order objects, and a server-side adequacy scoring mechanism that determines whether a given order satisfies an account's declared PQC readiness threshold. The profile is designed for both public and private ACME deployments and does not modify the core ACME state machine: it adds discoverable capability metadata and per-order policy directives that servers MAY enforce. Multi-tenant ACME servers MUST implement tenant-isolation controls that prevent cross-account PQC posture leakage. This document is distinguished from draft-giron-acme-pqcnegotiation [I-D.giron-acme-pqcnegotiation], which defines algorithm negotiation at the ACME protocol level. This profile operates above the negotiation layer: it defines per-account posture scoring, adequacy thresholds, hybrid policy bits, rotation epoch anchoring, and tenant- isolation requirements that apply regardless of which negotiation mechanism is used.

### ACME Extension for SM2 Dual-Certificate System
Draft: draft-geng-acme-sm2dualcert-extension · Working group: acme
Agenda: draft-geng-acme-sm2dualcert-extension-00
page: https://datatracker.ietf.org/doc/draft-geng-acme-sm2dualcert-extension/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
This document describes the extension of the ACME protocol [RFC8555] to support automated issuance of SM2 dual certificates (signature certificates and encryption certificates) in the Chinese National Cryptography certificate system. This document does not represent IETF consensus; the technical solution is applicable only to PKI environments based on an SM2 dual-certificate system. Under the framework of the ACME protocol [RFC8555], this document proposes using two separate Orders to request the two certificates. For the signature certificate, the existing ACME workflow is reused, optionally using the standard CSR approach or the pk-01 challenge [I-D.geng-acme-public-key]. For the encryption certificate, this document defines a new challenge type, auth-01, specifically for *identity authorization* scenarios: the client proves possession of the *signature private key* to authorize the Key Management Center (KMC) to generate an encryption key pair and issue the encryption certificate on behalf of the entity. This challenge type intrinsically binds the issuance of the encryption certificate to the signature key, requiring no additional binding identifiers. All extensions are compatible with the existing ACME resource model. No new Order types are introduced. This document only adds optional fields in the client's newOrder request (authKey, includeEnvelope) and an additional field in the server's response (envelope), without changing the core semantics or state machine of Order.

### ACME STAR Extension for SM2 Dual-Certificate Automated Key Rotation
Draft: draft-geng-acme-sm2dualcert-rotation · Working group: acme
Agenda: draft-geng-acme-sm2dualcert-rotation-00
page: https://datatracker.ietf.org/doc/draft-geng-acme-sm2dualcert-rotation/ | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
The SM2 dual-certificate system, specified in [GMT.0034-2014], employs a dual-certificate architecture in which each entity holds both a signature certificate and an encryption certificate. The encryption private key is generated and escrowed by the Key Management Center (KMC). This document defines an *ACME Profile* that adapts the core protocol of [RFC8555] to the specific deployment scenario of SM2 dual- certificate management in the ShangMi (SM) ecosystem. Building upon the dual-certificate foundation framework defined in [I-D.geng-acme- sm2dualcert-extension], this document defines a STAR extension for the ACME protocol that enables *synchronized short-term automatic renewal* of SM2 dual certificates. The signature certificate follows [RFC8739] (ACME STAR) for automatic renewal with the same key pair; the encryption certificate achieves automated key rotation with a fresh key pair per epoch based on *Asynchronous Remote Key Generation (ARKG)* [Frymann2020]. This extension establishes a *unified ARKG seed chain key derivation system*: the KMC holds a seed seed_kmc and derives all encryption certificate key pairs (pk_i, sk_i) for all epochs via the ARKG algorithm, enabling stateless, lightweight KMC operations. On this basis, this extension provides *two private key delivery modes*: * *Mode A (ARKG Envelope Delivery)*: delivers sk_i to the client via a digital envelope, fully inheriting the envelope mechanism of the base framework. * *Mode B (ARKG Offline DH Derivation)*: the initial private key is obtained via envelope delivery; subsequent private keys are derived offline by the client, providing key insulation security properties. Both modes share the same ARKG cryptographic infrastructure, differing only in the final delivery mechanism of the private key. Deployers may choose according to their requirements, with full compatibility and coexistence achieved through ACME directory object negotiation. *Document Positioning*: This document is intended for the *specific SM ecosystem* as a practical guide and interoperability reference, and does not seek to become a general Internet standard.

### ACME Persistent DNS Challenge
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-acme-acme-persistent-dns-challenge-01 | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### acme-rats presentation
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-acme-ietf-126-acme-rats-presentation-00 | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### ACME and MTC / PLANTS
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-acme-acme-and-plants-00 | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

### SM2 Dual Certificates on ACME: From Bootstrap Issuance to STAR-Based Renewal
Presentation · Working group: acme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-acme-sm2-dual-certificates-on-acme-from-bootstrap-issuance-to-star-based-renewal-00 | video: https://youtu.be/0DOjvhF7VgU | materials: https://datatracker.ietf.org/meeting/126/session/acme
Slides presented at the acme session; no Internet-Draft is linked to them.

## Working Group: anima

### cBRSKI and Join Proxy
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-cbrski-and-join-proxy-00 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### The Constrained GRASP (cGRASP)
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-slide-126-anima-the-constrained-grasp-03-01 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Autonomic Traffic Management in Artificial Intelligence Data Centers
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-autonomic-traffic-management-in-artificial-intelligence-data-centers-00 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### AI for Autonomic Networking and Agentic AI for Intent-Based Networking
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-ai-for-autonomic-networking-03 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Problem Statement and Gap Analysis for Autonomic Networking with AI-ASA
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-06-problem-statement-and-gap-analysis-for-autonomic-networking-with-ai-asa-00 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### GRASP through routers: a Problem Statement
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-grasp-through-routers-a-problem-statement-01 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Use Cases and Requirements for Network Admission of AI Agent Instances
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-use-cases-and-requirements-for-network-admission-of-ai-agent-instances-01 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

### Campus Agent Identification and Scope-Down Access Control
Presentation · Working group: anima
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-anima-campus-agent-identification-and-scope-down-access-control-02 | video: https://youtu.be/pYdTj9ljty4 | materials: https://datatracker.ietf.org/meeting/126/session/anima
Slides presented at the anima session; no Internet-Draft is linked to them.

## Working Group: bess

### Extended Procedures for EVPN Optimized Ingress Replication
Draft: draft-ietf-bess-extended-evpn-optimized-ir · Working group: bess
Agenda: draft-ietf-bess-extended-evpn-optimized-ir Wen Lin 10 min 9:15 - 9:25
page: https://datatracker.ietf.org/doc/draft-ietf-bess-extended-evpn-optimized-ir/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-draft-ietf-bess-extended-evpn-optimized-ir-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
In the Virtualization Overlay (NVO) network with Ethernet VPN (EVPN), optimized ingress replication uses Assisted-Replication (AR) to achieve more efficient delivery of Broadcast and Multicast (BM) traffic. An AR-LEAF, which is a Network Virtualization Edge (NVE) device, forwards received BM traffic from its tenant system to an AR- REPLICATOR. The AR-REPLICATOR then replicates it to the remaining AR-LEAFs in the network. However, when replicating the packet on behalf of its multihomed AR-LEAF, an AR-REPLICATOR may face challenges in retaining the source IP address or including the expected Ethernet Segment Identifier (ESI) label that is required for EVPN split-horizon filtering. This document extends the optimized ingress replication procedures to address such limitations. The extended procedures specified in this document allow the support of EVPN multihoming on the AR-LEAFs as well as optimized ingress replication for the rest of the EVPN NVO network.

### EVPN First Hop Security
Draft: draft-ietf-bess-evpn-first-hop-security · Working group: bess
Agenda: draft-ietf-bess-evpn-first-hop-security Krishna 05 min 9:25 - 9:30
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-first-hop-security/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-evpn-first-hop-security-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
The Dynamic Host Configuration Protocol (DHCP) snoop database stores valid IPv4-to-MAC and IPv6-to-MAC bindings by snooping on DHCP messages. These bindings are used by security functions like Dynamic Address Resolution Protocol Inspection (DAI), Neighbor Discovery Inspection (NDI), IPv4 Source Guard, and IPv6 Source Guard to safeguard against traffic received with a spoofed address. These functions are collectively referred to as First Hop Security (FHS). This document proposes BGP extensions and new Ethernet VPN (EVPN) procedures to distribute and synchronize the DHCP snoop database to support FHS. Such synchronization is needed to support EVPN host mobility and multihoming.

### Applications and Procedures for the Unknown MAC Route in EVPN
Draft: draft-ietf-bess-evpn-umr-mobility · Working group: bess
Agenda: draft-ietf-bess-evpn-umr-mobility Krishna 05 min 9:30 - 9:35
page: https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-umr-mobility/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-applications-and-procedures-for-the-unknown-mac-route-in-evpn-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
The Interconnect Solution for Ethernet VPN defines Unknown MAC (Media Access Control) Route (UMR) utilization for Data Center Interconnect (DCI) when EVPN MPLS or EVPN VXLAN is used as an overlay network for such interconnects. The use of UMR has implications for EVPN MAC mobility procedures, for EVPN Layer 2 and IRB operations, and for EVPN Proxy ARP/ND operations. This document describes additional enhancements required to EVPN procedures and operations when using UMR. This document updates RFC9014 to clarify and extend the procedures for UMR usage.

### Per-Flow EVPN Designated Forwarder Election
Draft: draft-kriswamy-bess-evpn-perflow-df · Working group: bess
Agenda: draft-kriswamy-bess-evpn-perflow-df Krishna 05 min 9:35 - 9:40
page: https://datatracker.ietf.org/doc/draft-kriswamy-bess-evpn-perflow-df/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-per-flow-evpn-designated-forwarder-election-01 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
The Ethernet Virtual Private Network (EVPN) solution offers procedures for electing a Designated Forwarder (DF) for multihomed Ethernet Segments. In this context, the Provider Edge (PE) router is responsible for sending Broadcast, Unknown Unicast, and Multicast (BUM) traffic to a multihomed device or network. This applies in cases of an all-active multihomed Ethernet Segment (ES) as well as for BUM and unicast traffic in the case of single-active multihoming. While the Default Algorithm provides an efficient and automated mechanism for selecting the DF across Ethernet Tags within an Ethernet Segment, it does not provide Per-flow DF selection within an EVPN Instance (EVI). This document defines a new DF Election Algorithm that performs Per- flow DF selection by defining a new DF Algorithm value.

### Multicast Router State Synchronization in EVPN Networks
Draft: draft-jot-bess-evpn-mcast-router-sync · Working group: bess
Agenda: draft-jot-bess-evpn-mcast-router-sync-00 Jorge 10 min 9:40 - 9:50
page: https://datatracker.ietf.org/doc/draft-jot-bess-evpn-mcast-router-sync/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-ietf126-bess-draft-jot-evpn-mcast-router-sync-00-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
Ethernet VPN (EVPN) networks support multicast applications in which multicast routers and multicast hosts are attached to the same tenant. Existing specifications define how Provider Edge (PE) devices synchronize the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) membership state of multihomed multicast hosts, and how Optimized Inter-Subnet Multicast (OISM) forwarding interacts with multicast routers via PIM EVPN Gateways. However, none of the existing specifications addresses the synchronization of the state associated with a multicast router (an IGMP/MLD Querier or a Protocol Independent Multicast (PIM) router) when that router is multihomed to a set of EVPN PEs. This document specifies a new EVPN route, the Multicast Router Discovery (MRD) route, and the procedures to synchronize multicast router state across the PEs of an Ethernet Segment, for routers attached to multicast Broadcast Domains or to Layer 3 interfaces.

### Multipath for EVPN Ethernet Auto-Discovery Routes
Draft: draft-li-bess-evpn-ead-multipath · Working group: bess
Agenda: draft-li-bess-evpn-ead-multipath Zhiqiang Li 10 min 9:50 - 10:00
page: https://datatracker.ietf.org/doc/draft-li-bess-evpn-ead-multipath/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-multipath-for-evpn-ethernet-auto-discovery-routes-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
In EVPN multi-homing deployments, multiple PE devices attached to the same Ethernet Segment each originate Ethernet Auto-Discovery (EAD) routes. Standard BGP best-path selection retains only one route per NLRI key, which can suppress reachability information needed for EVPN aliasing, fast convergence, and split-horizon filtering. This document specifies that BGP speakers MUST treat EAD routes as multipath and MUST advertise and install all valid EAD routes for a given Ethernet Segment, rather than selecting a single best path.

### Dual MPLS and SRv6 Service Advertisement in the Absence of Transposition
Draft: draft-many-bess-rfc9252-dual-sid · Working group: bess
Agenda: draft-many-bess-rfc9252-dual-sid Himanshu Shah 10 min 10:00 - 10:10
page: https://datatracker.ietf.org/doc/draft-many-bess-rfc9252-dual-sid/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-dual-mpls-and-srv6-service-advertisement-himanshu-shah-02 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
RFC 9252 defines BGP signaling procedures for SRv6 services, including the use of an MPLS Label field and transposition semantics. However, when transposition is not used (i.e., TL = 0), RFC 9252 does not explicitly define the interpretation of the MPLS Label field, leading to ambiguity in control-plane signaling. This document specifies a minimal, backward-compatible extension to RFC 9252 that enables a single route to unambiguously advertise both a valid MPLS Service Label and an SRv6 Service SID. The extension relies on existing MPLS label semantics, without introducing new TLVs, attributes, or changes to the base encoding format.

### SRv6 Deployment Options
Draft: draft-ietf-srv6ops-srv6-deployment · Working group: bess
Agenda: draft-ietf-srv6ops-srv6-deployment Jacub Horn 15 min 10:10 - 10:25
page: https://datatracker.ietf.org/doc/draft-ietf-srv6ops-srv6-deployment/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-draft-ietf-srv6ops-srv6-deployment-slides-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
When deciding to migrate a network from existing data-plane technologies (e.g. MPLS, SR-MPLS or overlay encapsulations such as VXLAN) to SRv6, common questions involve how to perform the migration, how to minimize impact to the existing network and what techniques are available to support a smooth transition. This document presents various deployment and migration options for networks evolving toward SRv6 from prior transport or overlay technologies.

### Reservation of EVPN Route Types for Experimental Use
Draft: draft-tantsura-bess-evpn-route-type-exp-use · Working group: bess
Agenda: draft-tantsura-bess-evpn-route-type-exp-use-00 Jeff Tantsura 10 min 10:25 - 10:35
page: https://datatracker.ietf.org/doc/draft-tantsura-bess-evpn-route-type-exp-use/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-reservation-of-evpn-route-types-for-experimental-use-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
This document reserves codepoints in the EVPN Route Type registry for experimental use to enable implementations to carry out development and test of new EVPN features. It updates RFC7432 to modify the registration policy for the EVPN Route Type registry.

### Interconnecting domains with IBGP
Draft: draft-smn-idr-inter-domain-ibgp · Working group: bess
Agenda: draft-smn-idr-inter-domain-ibgp Moshiko Nayman 10 min 10:35 - 10:45
page: https://datatracker.ietf.org/doc/draft-smn-idr-inter-domain-ibgp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-interconnecting-domains-with-ibgp-00 | video: https://youtu.be/3lzjKPn9HdE | materials: https://datatracker.ietf.org/meeting/126/session/bess
This document describes the building of Inter-domain L3VPN architecture with internal BGP, applying the multi-domain options specified in BGP/MPLS IP Virtual Private Networks (VPNs) within a single Autonomous System, where route reflectors set the NEXT_HOP attribute to self as described in BGP Route Reflector with Next Hop Self.

## Working Group: cose

### AES-CMAC for COSE
Draft: draft-ietf-cose-cmac · Working group: cose
Agenda: [10 min] draft-ietf-cose-cmac - Brian Sipos
page: https://datatracker.ietf.org/doc/draft-ietf-cose-cmac/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-aes-cmac-for-cose-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
The CBOR Object Signing and Encryption (COSE) specification defines structures for generating, conveying, and verifying Message Authentication Code (MAC) tags. This document registers code points for using the Advanced Encryption Standard (AES) block cipher in Cipher-based Message Authentication Code (CMAC) mode within those COSE structures. Specifically, these uses are for computing MAC tag values with no additional parameters.

### Split Signing Algorithms for COSE
Draft: draft-ietf-cose-split-signing-algs · Working group: cose
Agenda: [15 min] draft-ietf-cose-split-signing-algs - Emil Lundberg
page: https://datatracker.ietf.org/doc/draft-ietf-cose-split-signing-algs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-split-signing-algorithms-for-cose-pptx-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
This specification defines COSE algorithm identifiers for negotiating how to split a signature algorithm between two cooperating parties. Typically the first party hashes the data to be signed and the second party finishes the signature over the hashed data. This is a common technique, useful for example when the signing private key is held in a smart card or similar hardware component with limited processing power and communication bandwidth. The resulting signatures are identical in structure to those computed by a single party, and can be verified using the same verification algorithm without additional steps to preprocess the signed data.

### FN-DSA for JOSE and COSE
Draft: draft-ietf-cose-falcon · Working group: cose
Agenda: ~~[15 min] draft-ietf-cose-falcon - Hannes Tschofenig~~
page: https://datatracker.ietf.org/doc/draft-ietf-cose-falcon/ | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
This document specifies JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA), a Post-Quantum Cryptography (PQC) digital signature scheme defined in US NIST FIPS 206 (expected to be published in late 2026 early 2027). It does not define new cryptographic primitives; rather, it specifies how existing FN-DSA mechanisms are serialized for use in JOSE and COSE. This document registers signature algorithms for JOSE and COSE, specifically FN-DSA-512 and FN-DSA-1024.

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for COSE
Draft: draft-ietf-jose-pqc-kem · Working group: cose
Agenda: [10 min] draft-ietf-jose-pqc-kem way forward - Tirumaleswar Reddy
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pqc-kem/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-post-quantum-key-encapsulation-mechanisms-pq-kems-for-cose-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
This document describes conventions for using Post-Quantum Key Encapsulation Mechanisms (PQ-KEMs) with CBOR Object Signing and Encryption (COSE).

### COSE Algorithms for KangarooTwelve, TurboSHAKE and KMAC
Draft: draft-bormann-cose-turbo-kanga-kmac · Working group: cose
Agenda: [10 min] draft-bormann-cose-turbo-kanga-kmac - Quynh Dang
page: https://datatracker.ietf.org/doc/draft-bormann-cose-turbo-kanga-kmac/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-cose-turbo-kanga-kmac-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
RFC 9861 defined and registered four eXtendable-Output Functions (XOFs), hash functions with output of arbitrary length, named TurboSHAKE128, TurboSHAKE256, KT128, and KT256; the present document is intended as the IETF consensus document that is now needed to give these algorithms Recommended status in the COSE registry. This document specifies concrete instances of those four functions above to be used as MACs in COSE. This document also specifies concrete instances of KMAC128 and KMAC256 in [NIST.SP.800-185] to be used as MACs in COSE and registers code points for them. And, this document provides "Recommended" status for those algorithms for COSE.

### Ascon-AEAD128 and Ascon-Hash256 for COSE
Draft: draft-ochkas-cose-ascon · Working group: cose
Agenda: [10 min] draft-ochkas-cose-ascon - Dmytro OCHKAS
page: https://datatracker.ietf.org/doc/draft-ochkas-cose-ascon/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-ascon-aead128-and-ascon-hash256-for-cose-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
This document describes CBOR Object Signing and Encryption (COSE) serialization with Ascon, a NIST standard for lightweight cryptography. In 2019, as a part of CAESAR competition, Ascon-128 and Ascon-128a were selected as the first choice for the lightweight authenticated encryption. After, in 2023, National Institute of Standards and Technology (NIST) selected Ascon family of cryptographic algorithms to be the standard for lightweight cryptography. In August 2025, NIST Special Publication 800-232 was released, defining Ascon-based lightweight cryptography standards for constrained devices. This recognition makes it particularly interesting to enable using Ascon with COSE structures.

### CBOR Encoded Certificate Revocation Management
Draft: draft-liao-cose-c509-revocation · Working group: cose
Agenda: [15 min] draft-liao-cose-c509-revocation - Rikard Höglund
page: https://datatracker.ietf.org/doc/draft-liao-cose-c509-revocation/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-cbor-encoded-certificate-revocation-slides-revised-jul23-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
This document specifies CBOR-encoded PKI structures for use with C509 certificates (draft-ietf-cose-cbor-encoded-cert), X.509 certificates (RFC 5280), and future certificate types. It defines C509 CRL and C509 OCSP, compact CBOR encodings of X.509 Certificate Revocation Lists (RFC 5280) and OCSP messages (RFC 6960), respectively. The structures defined in this document are certificate-type agnostic and can be used with C509 certificates, X.509 certificates, or future certificate types without modification. C509 OCSP improves on RFC 6960 by signing a wider set of fields to prevent algorithm- substitution and certificate-chain substitution attacks, replacing plaintext serial numbers with hashes to preserve requestor privacy, replacing the two-hash issuer identity with a single certificate hash, and identifying all participants (requestor, responder, issuer) by a uniform certificate hash rather than type-specific fields. C509 CRL and C509 OCSP are not wire-format-compatible with their DER- encoded X.509 counterparts and cannot be converted to or from them without semantic interpretation.

### CBOR Encoded Certificate Revocation slides draft
Presentation · Working group: cose
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-cose-cbor-encoded-certificate-revocation-slides-draft-00 | video: https://youtu.be/vFvw9gl8Zno | materials: https://datatracker.ietf.org/meeting/126/session/cose
Slides presented at the cose session; no Internet-Draft is linked to them.

## Working Group: dnsop

### Integration of DNS Domain Names into Application Environments: Motivations and Considerations
Draft: draft-ietf-dnsop-integration · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-integration/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-integration/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-dns-integrations-draft-ietf-dnsop-integration-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document describes considerations when integrating a DNS domain name into an application environment. Goals of this document include minimizing conflicts between the global DNS and applications that integrate with the global DNS, providing a consistent user experience (unique identifier across environments), and avoiding impacts to the security, stability, and resiliency of the global DNS. While all sources of potential concern cannot be enumerated in one document, accounting for at least the considerations discussed here should improve the security posture of both the global DNS and integrating applications.

### DNSSEC Key Restore
Draft: draft-ietf-dnsop-dnssec-keyrestore · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-dnssec-keyrestore/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-dnssec-keyrestore/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-sessa-dnssec-key-restore-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document describes the issues surrounding the handling of DNSSEC private keys in a DNSSEC signer. It presents operational guidance in case a DNSSEC private key becomes inoperable. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Domain Name System Operations Working Group mailing list (dnsop@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/dnsop/. Source for this draft and an issue tracker can be found at https://github.com/ietf-wg-dnsop/draft-ietf-dnsop-dnssec-keyrestore.

### Automating DNS Delegation Management via DDNS
Draft: draft-ietf-dnsop-delegation-mgmt-via-ddns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delegation-mgmt-via-ddns/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-delegation-mgmt-via-ddns/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-delegation-mgmt-via-ddns-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
Delegation information (i.e. the NS RRset, possible glue, possible DS records) should always be kept in sync between child zone and parent zone. However, in practice that is not always the case. When the delegation information is not in sync the child zone is usually working fine, but without the amount of redundancy that the zone owner likely expects to have. Hence, should any further problems ensue it could have catastrophic consequences. The DNS name space has lived with this problem for decades and it never goes away. Or, rather, it will never go away until a fully automated mechanism for how to keep the information in sync automatically is deployed. This document proposes such a mechanism based on DNS Dynamic Updates (DDNS) secured with SIG(0) signatures, sent from the child to the parent across the zone cut. The target of the update is discovered via the DSYNC record defined in [RFC9859]. TO BE REMOVED: This document is being collaborated on in Github at: https://github.com/johanix/draft-ietf-dnsop-delegation-mgmt-via-ddns (https://github.com/johanix/draft-ietf-dnsop-delegation-mgmt-via- ddns). The most recent working version of the document, open issues, etc, should all be available there. The authors (gratefully) accept pull requests.

### Disclosure of Negative Trust Anchors in DNS Responses
Draft: draft-farrokhi-dnsop-ede-nta · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-farrokhi-dnsop-ede-nta/
page: https://datatracker.ietf.org/doc/draft-farrokhi-dnsop-ede-nta/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-disclosure-of-negative-trust-anchors-in-dns-responses-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document describes a mechanism for disclosing that a Negative Trust Anchor (NTA) was in effect at the time that a DNS response was generated, using an Extended DNS Error (EDE).

### Signalling a Zone Cut to Nowhere in the DNS
Draft: draft-jabley-dnsop-zone-cut-to-nowhere · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-jabley-dnsop-zone-cut-to-nowhere/
page: https://datatracker.ietf.org/doc/draft-jabley-dnsop-zone-cut-to-nowhere/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-sessa-signalling-a-zone-cut-to-nowhere-in-the-dns-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document defines a standard mechanism to signal the existence of a DNS zone cut without specifying authoritative nameservers for the delegated child zone. This "zone cut to nowhere" is particularly useful in split-horizon environments, allowing parent zones to explicitly signal that a child zone exists but is only resolvable within a private namespace.

### Add TTLs to DNS errors
Draft: draft-homburg-dnsop-dettl · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-homburg-dnsop-dettl/
page: https://datatracker.ietf.org/doc/draft-homburg-dnsop-dettl/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-add-ttls-to-dns-errors-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
When a DNS server replies an error other than NXDOMAIN, there is no mechanism to specify how long this error can be cached by the recepient. This document introduces a mechanism where a server can specify the time to live (TTL) of an error by adding a SOA record to the additional section of a reply. Clients can use this TTL at their discretion. In particular, clients can limit the TTL to a maximum value, impose a minimum value or just ignore the TTL value all together.

### Domain Key Authorities (DKA): DNS-Designated Public Key Distribution for Email-Address Identifiers
Draft: draft-swaminathan-dka-framework · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-swaminathan-dka-framework/
page: https://datatracker.ietf.org/doc/draft-swaminathan-dka-framework/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-domain-key-authorities-dka-dns-designated-public-key-distribution-for-email-address-identifiers-pdf-version-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document specifies the Domain Key Authority (DKA) framework, a DNS-anchored public-key distribution mechanism for the email-address namespace. The framework enables an Internet domain to designate an authoritative key service that verifies, stores, and distributes selector-scoped public keys for email-address identifiers under that domain. The result is a decentralized, deterministic, and application-agnostic framework for verified public-key discovery that supports incremental deployment and cryptographic agility.

### Domain Authority (DA): A DNS-Designated Service Endpoint for Domain Information
Draft: draft-swaminathan-da · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-swaminathan-da/
page: https://datatracker.ietf.org/doc/draft-swaminathan-da/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-domain-authority-da-a-dns-designated-service-endpoint-for-domain-information-pdf-version-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document specifies a minimal standard by which a domain designates, via a single DNS record, a Domain Authority (DA) as a service endpoint accessible at a well-known HTTPS URI. The DA exposes five namespaces for capabilities beyond what DNS can natively deliver: atomic record bundles, public key distribution, domain- defined APIs, authenticated access, and private domain control verification. The standard is organized in three layers. The Designation Layer specifies how a domain publishes a DNS record that points to its DA. The Retrieval Layer specifies the five namespaces through which consumers access domain information. The Trust Layer specifies how consumers establish confidence in the DA and its responses. The standard preserves full backward compatibility with existing DNS resolution. It requires no changes to DNS resolvers, no new DNS record types, and no ecosystem-wide coordination. Any domain can adopt unilaterally and gain immediate operational benefit.

### DNS Extensions to Energy Efficiency as a Service(EEAS)
Draft: draft-zhu-dnsop-de-eeas · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-zhu-dnsop-de-eeas/
page: https://datatracker.ietf.org/doc/draft-zhu-dnsop-de-eeas/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-dns-extensions-to-energy-efficiency-as-a-service-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document describes a new Mechanism and DNS resource record (RR) type to carry information about energy-related characteristics for end-to-end internet access. The "EE" ("Energy Efficiency") record allows the network to provide different levels of energy-saving service. By providing more energy information to the client before it attempts to establish a connection, these records offer potential benefits to enhancements on energy as service criteria.

### UTXO6-DNS: Resolving Payment Endpoints via Private-use RRTYPE and Prefix Isolation
Draft: draft-guorong-utxo-dns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-guorong-utxo-dns/
page: https://datatracker.ietf.org/doc/draft-guorong-utxo-dns/ | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document specifies the _utxo application namespace for DNS. It defines how wallet clients and TEE (Trusted Execution Environment) applications resolve verifiable payment endpoints and blockchain UTXO (Unspent Transaction Output) references using DNS. To avoid exacerbating public RRTYPE space congestion and DNS-layer transparent parsing, this document utilizes the RFC 3597 Private-use space (QTYPE 65400). The DNS protocol does not parse the payload. Application semantics are isolated strictly via the _utxo underscore prefix in the owner name, while the RDATA consists of a purely opaque CBOR-encoded byte stream.

### DNS-Based Address Mapping Record (AMR) for IPv4/IPv6 Mapping in IPv6-only Networks
Draft: draft-dong-dnsop-dns-record-amr · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-dong-dnsop-dns-record-amr/
page: https://datatracker.ietf.org/doc/draft-dong-dnsop-dns-record-amr/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-dns-based-address-mapping-record-amr-for-ipv4ipv6-mapping-in-ipv6-only-networks-01 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document defines a new Domain Name System (DNS) resource record type called the Address Mapping Record (AMR). The AMR record enables querying of IPv6 mapping prefixes associated with the destination address of an IPv4 packet in IPv6-only networks. This mechanism facilities the transmission of IPv4 service data across multi-domain in IPv6-only environment, supporting IPv4-as-a-Service (IPv4aaS) implementations.

### Delegation Revalidation by DNS Resolvers
Draft: draft-ietf-dnsop-ns-revalidation · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-ietf-dnsop-ns-revalidation/
page: https://datatracker.ietf.org/doc/draft-ietf-dnsop-ns-revalidation/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-sessb-parent-centric-delegation-handling-in-dns-resolvers-01 | video: https://youtu.be/4iMG3aGyRBU | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document describes an optional algorithm for the processing of Name Server (NS) resource record (RR) sets (RRsets) during iterative resolution, and describes the benefits and considerations of using this approach. When following a referral response from an authoritative server to a child zone, DNS resolvers should explicitly query the authoritative NS RRset at the apex of the child zone and cache this in preference to the NS RRset on the parent side of the zone cut. The (A and AAAA) address RRsets in the additional section from referral responses and authoritative NS answers for the names of the NS RRset, should similarly be re-queried and used to replace the entries with the lower trustworthiness ranking in cache. Resolvers should also periodically revalidate the delegation by re-querying the parent zone at the expiration of the shortest TTL among the parent NS RRset, the DS RRset (if present), and the child NS RRset.

### Parent-Centric Delegation Handling in DNS Resolvers
Draft: draft-sury-dnsop-parent-centric-resolver · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-sury-dnsop-parent-centric-resolver/
page: https://datatracker.ietf.org/doc/draft-sury-dnsop-parent-centric-resolver/ | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document specifies an optional parent-centric behavioral model for DNS recursive resolvers, in which delegation decisions are always based on the NS RRset (or DELEG RRset) received from the parent side of a zone cut and are never overwritten by child-side NS data. The parent-centric model eliminates the "two sources of truth" problem inherent in the current DNS delegation design, closes the Ghost Domain and Phoenix Domain attack vectors, provides deterministic behavior in the presence of parent/child NS mismatches, and enables resolvers to safely accept sibling (out-of-bailiwick) glue by scoping delegation information to individual zone cuts. It also provides the behavioral foundation required for deployment of the DELEG extensible delegation mechanism. This document updates [RFC1034] and [RFC1035].

### DNS Catalog Zone Properties for Zone Transfers
Draft: draft-axu-dnsop-catalog-zone-xfr-properties · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-axu-dnsop-catalog-zone-xfr-properties/
page: https://datatracker.ietf.org/doc/draft-axu-dnsop-catalog-zone-xfr-properties/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-dns-catalog-zone-properties-for-zone-transfers-01 | video: https://youtu.be/4iMG3aGyRBU | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document specifies DNS Catalog Zones Properties that define the primary name servers from which specific or all member zones can transfer their associated zone, as well as properties related to zone transfers such as access control. This document also defines a groups property, for the apex of the catalog zone, as a location to assign the additional properties to certain catalog zone groups. Besides the additional properties, this document updates RFC9432 by explicitly allowing CNAME and DNAME records.

### Optimistic DNS
Draft: draft-gakiwate-dnsop-optimistic-dns · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-optimistic-dns/
page: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-optimistic-dns/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-optimistic-dns-00 | video: https://youtu.be/4iMG3aGyRBU | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
DNS lookups introduce user-visible delay, particularly when cached records have expired and must be refreshed from the network. This document describes Optimistic DNS, a client-side stub resolver mechanism that immediately returns expired cached DNS records to applications while simultaneously refreshing them with a network query. The application receives an answer in microseconds rather than milliseconds, and if the data has changed receives an updated answer shortly thereafter. Optimistic DNS is complementary to RFC 8767, which addresses serving stale data at recursive resolvers. This document focuses exclusively on client-side stub resolver behavior, including explicit signaling from the application to inform the stub resolver that the application is able to handle old and possibly incorrect information.

### DNS Root Server System Usage Considerations
Draft: draft-hardaker-dnsop-rss-usage-considerations · Working group: dnsop
Agenda: https://datatracker.ietf.org/doc/draft-hardaker-dnsop-rss-usage-considerations/
page: https://datatracker.ietf.org/doc/draft-hardaker-dnsop-rss-usage-considerations/ | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
This document explores various technologies developed to enhance the DNS, focusing specifically on interactions with the DNS Root Server System (RSS). It examines a number of the protocols and evaluates their impact on communication with the RSS.

### IETF 126 DNS Operations (I)
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-sessa-ietf-126-dns-operations-i-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### UTXO Domain Name System (UTXO6-DNS) Base Protocol and PRN Regulatory Extensions
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-utxo-domain-name-system-utxo6-dns-base-protocol-and-prn-regulatory-extensions-00 | video: https://youtu.be/qASW86uosQw | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### IETF 126 DNS Operations (II)
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-sessb-ietf-126-dns-operations-ii-01 | video: https://youtu.be/4iMG3aGyRBU | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### Delegation Revalidation
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-delegation-revalidation-00 | video: https://youtu.be/4iMG3aGyRBU | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

### RSS communication and the future of LocalRoot / RootCache
Presentation · Working group: dnsop
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-dnsop-rss-communication-and-the-future-of-localroot-rootcache-00 | video: https://youtu.be/4iMG3aGyRBU | materials: https://datatracker.ietf.org/meeting/126/session/dnsop
Slides presented at the dnsop session; no Internet-Draft is linked to them.

## Working Group: grow

### BMP Extension for Path Status TLV
Draft: draft-ietf-grow-bmp-path-marking-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-path-marking-tlv/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-path-marking-tlv/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-bmp-path-marking-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
The BGP Monitoring Protocol (BMP) provides an interface for obtaining BGP path information, which is conveyed through BMP Route Monitoring (RM) messages. This document specifies a BMP extension to convey the status of a path after being processed by the BGP process.

### A YANG Data Model for BMP
Draft: draft-ietf-grow-bmp-yang · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-yang/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-yang/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-bmp-yang-model-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document defines a YANG data model for the configuration and monitoring of the BGP Monitoring Protocol (BMP).

### Filtering Adj-Rib-In and Adj-Rib-Out to BMP receivers
Draft: draft-ietf-grow-bmp-adj-ribs-filtered · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-adj-ribs-filtered/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
Filtering RIBs in BMP (BGP Monitoring Protocol) can be desirable for several use-cases like, for example, limiting the amount of data a collector station has to process or allow a sender to export only a certain afi/safi of interest. This document defines an indicator to inform a collector station that a Adj-Rib-In or Adj-Rib-Out data feed is being filtered at the BMP exporter. This document updates RFC 7854.

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-bmp-v4-extended-tlv-support-for-bgp-monitoring-protocol-01 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
Most of the BGP Monitoring Protocol (BMP) message types make provision for data in Type, Length, Value (TLV) format. However, Route Monitoring messages (which provide a snapshot of the monitored Routing Information Base) Stats Reports (which supply periodical counters) and Peer Down messages (which indicate that a peering session was terminated) do not. Supporting (optional) data in TLV format across all BMP message types provides consistent and extensible structures that would be useful among the various use- cases where conveying additional data to a monitoring station is required. This document updates RFC 7854 [RFC7854] to support TLV data in all message types and defines some essential TLVs. Additionally, this document introduces support for enterprise- specific TLVs in the BGP Monitoring Protocol by defining an Enterprise Bit (E-bit) that allows usage of per-vendor Type values.

### Definition for Aggregated BMP Route Monitoring Message
Draft: draft-liu-grow-bmp-rm-aggregated · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-rm-aggregated/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document proposes an aggregated BMP Route Monitoring message based on the BMP Multi-Peer Header message (draft-liu-grow-bmp- multiple-peer-header). It can compress multiple BMP Route Monitoring messages into one aggregated BMP Route Monitoring message to reduce the amount of reported BMP Route Monitoring messages and reduce the network overhead.

### Definition for BMP Multiple Peer Header
Draft: draft-liu-grow-bmp-multiple-peer-header · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-multiple-peer-header/
page: https://datatracker.ietf.org/doc/draft-liu-grow-bmp-multiple-peer-header/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document proposes a format of multiple peer header for aggregating BMP messages. It can be used to compress multiple BMP messages with per-peer header into one aggregated BMP message, which could reduce the amount of reported BMP messages and reduce network overhead.

### Common BMP Route-Monitoring Messages for Routes Unchanged by Policy
Draft: draft-patki-grow-bmp-common-updates · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/
page: https://datatracker.ietf.org/doc/draft-patki-grow-bmp-common-updates/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
A route unmodified by the inbound policy on a monitored router is included both in Pre-Policy Adj-RIB-In as well as Post-Policy Adj- RIB-In Route-Monitoring messages when both the Pre-Policy and Post- Policy Route-Monitoring modes are enabled. Similarly, a route unmodified by the outbound policy is included in Pre-Policy Adj-RIB- Out as well as Post-Policy Adj-RIB-Out Route-Monitoring messages. This document defines a method to avoid duplicate inclusion of routes unmodified by policy either in Adj-RIB-In or Adj-RIB-Out.

### Generic Event Notification (GEN) for BGP Monitoring Protocol (BMP)
Draft: draft-sp-grow-bmp-gen · Working group: grow
Agenda: • Update on direction of merger of draft-sp-grow-bmp-gen and draft-ietf-grow-bmp-rel
page: https://datatracker.ietf.org/doc/draft-sp-grow-bmp-gen/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document defines a new BMP message type: the Generic Event Notification (GEN). The BMP GEN message provides a flexible mechanism for reporting a wide variety of events related to BGP at different levels of hierarchy, such as routing instance, AFI/SAFI, or peer level. The BMP GEN message enables operators and automated systems to receive detailed context for operational events, such as policy triggers, administrative interventions, and state management notifications (e.g., RIB view unmonitor events).

### Logging of routing events in BGP Monitoring Protocol (BMP)
Draft: draft-ietf-grow-bmp-rel · Working group: grow
Agenda: • Update on direction of merger of draft-sp-grow-bmp-gen and draft-ietf-grow-bmp-rel
page: https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-rel/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-log-more-routing-events-in-the-bgp-monitoring-protocol-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
The BGP Monitoring Protocol (BMP) does provide for BGP session event logging (Peer Up, Peer Down), state synchronization (Route Monitoring), debugging (Route Mirroring) and Statistics messages, among others. This document defines a new Route Event Logging (REL) message type for BMP with the aim of covering use cases with affinity to alerting, reporting and on-change analysis.

### Route Server Next Hop Translation
Draft: draft-marenamat-grow-route-server-nh-translation · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-marenamat-grow-route-server-nh-translation/
page: https://datatracker.ietf.org/doc/draft-marenamat-grow-route-server-nh-translation/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-route-server-next-hop-translation-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
With the advent of RFC8950, Internet Exchange Points (IXPs) are enabled to rely solely on IPv6 addresses for adressing in their peering LANs. However, routers not supporting RFC8950 are a technical roadblock. It is easier to extend the capabilities of the IXP Route Server (RS) instead of those of every unsupporting router. Thus, this document introduces the concept of Specific Local Address Tables (SLATs). SLATs translate BGP next hops between all IXP members, regardless of their RFC8950 support, paving the way for IPv6-only IXPs. This document also introduces another, more transparent variant of BGP next hop translation applicable in IXPs which do not employ ARP and ND proxying. This document updates RFC 7947 by specifying an allowed route modification at the route server.

### A YANG Data Model for BGP Communities
Draft: draft-ietf-grow-yang-bgp-communities · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-yang-bgp-communities/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-yang-bgp-communities/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-draft-ietf-grow-yang-bgp-communities-10-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document defines a YANG data model for the structured specification of BGP communities. The model provides operators with a way to publish their locally defined BGP communities in a standardized format. Two YANG modules are defined in this document. The first is designed for stand-alone usage. The second is used to augment the "ietf-bgp" YANG module[I-D.ietf-idr-bgp-model] with BGP community annotations. Additionally, this document provides an optional discovery mechanism based on publishing of community definition locations through the Resource Public Key Infrastructure (RPKI).

### Storing BMP messages in MRT Format
Draft: draft-petrie-grow-mrt-bmp · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-petrie-grow-mrt-bmp/
page: https://datatracker.ietf.org/doc/draft-petrie-grow-mrt-bmp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-hackathon-results-storing-bmp-messages-in-mrt-format-01 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document extends the Multi-threaded Routing Toolkit (MRT) export format to support the storage of BMP messages.

### BMP Snapshots
Draft: draft-lucente-grow-bmp-offline · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-lucente-grow-bmp-offline/
page: https://datatracker.ietf.org/doc/draft-lucente-grow-bmp-offline/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
BMP (BGP Monitoring Protocol) is perfectly suited for real-time consumption but less ideal in stream processing and off-wire historical scenarios. The issue is that the necessary information to produce a complete view and enabling correct processing of all messages in the stream, is only sent out at the beginning of the BMP session. This document introduces the concept of BMP Snapshots, enabling BMP stations to synchronize mid-stream, and, providing the basis for self-contained, time-binned archiving of BMP data.

### Requirements for Monitoring RPKI-Related Processes on Routers Using BMP
Draft: draft-wang-grow-bmp-rpki-mon-reqs · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/
page: https://datatracker.ietf.org/doc/draft-wang-grow-bmp-rpki-mon-reqs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-requirements-for-monitoring-rpki-related-processes-on-routers-using-bmp-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document outlines requirements for extending the BGP Monitoring Protocol (BMP) to provide comprehensive monitoring of RPKI-related processes on routers, including RPKI data acquisition, RPKI-related policy configuration, route validation, and the impact of validation on routing decisions. The proposed extensions aim to standardize router-side monitoring of RPKI within BMP, focusing specifically on RPKI's effect on BGP routing decisions while maintaining a clear scope boundary with other monitoring mechanisms such as YANG modeling and streaming telemetry for RPKI-to-Router (RTR) protocol operations.

### Current Options for Securing Global Routing
Draft: draft-ietf-grow-routing-ops-sec-inform · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-sec-inform/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-sec-inform/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-current-options-for-securing-global-routing-et-al-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
The Border Gateway Protocol (BGP) is used for exchanging routing information between Autonomous Systems in the Internet. Due to its importance, it is necessary to ensure the basic security properties for BGP and BGP speaking routers. While the general principles for securing BGP operations are outlined in RFC 7454, that document does not detail the technical and implementation options for securing BGP. This document serves as a contemporary, non-exhaustive repository of options and methods for securing BGP. This document explicitly does not make value statements on the efficacy of individual techniques, nor does it mandate or prescribe the use of specific techniques or implementation details. Operators are advised to carefully consider whether the listed methods are applicable for their use-cases. Furthermore, the options listed in this document may change over time, and should not be used as a timeless ground-truth of applicable or sufficient methods.

### Currently Used Terminology in Global Routing Operations
Draft: draft-ietf-grow-routing-ops-terms · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-terms/
page: https://datatracker.ietf.org/doc/draft-ietf-grow-routing-ops-terms/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
Operating the global routing ecosystem entails a diverse set of interacting components, while operational practice evolved over time. In that time, terms emerged, disappeared, and sometimes changed their meaning. To aid operators and implementers in reading contemporary drafts, this document provides an overview of terms and abbreviations used in the global routing operations community. The document explicitly does not serve as an authoritative source of correct terminology, but instead strives to provide an overview of practice.

### Log More Routing Events in the BGP Monitoring Protocol (BMP)
Draft: draft-geng-grow-bmp-rel-enhancement · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rel-enhancement/
page: https://datatracker.ietf.org/doc/draft-geng-grow-bmp-rel-enhancement/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
The Route Event Logging (REL) message is defined in [I-D.ietf-grow-bmp-rel], which enables monitored routers to report event-driven operational data to BMP collectors. This document defines additional event code points for BGP FlowSpec RFC8955 [RFC8956] and BGP SR Policies [I-D.ietf-idr-sr-policy-safi]. These extensions enhance monitoring visibility for policy execution failures and improve network operation and troubleshooting capabilities.

### BMP Extension for Configuration Monitoring TLV
Draft: draft-gao-grow-bmp-config-monitor-tlv · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-gao-grow-bmp-config-monitor-tlv/
page: https://datatracker.ietf.org/doc/draft-gao-grow-bmp-config-monitor-tlv/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-bmp-extension-for-configuration-monitoring-tlv-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document defines two types of BMP extended TLV, which are used to carry configuration information and configuration effective time related to BGP route changes. Through this extension, the BGP monitoring platform can associate various BGP events with configuration operations, providing traceable evidence for identifying network failures caused by configuration changes.

### PAVA: BGP AS_PATH Validation by Querying ASes about Their Relationships
Draft: draft-flechier-sidrops-pava · Working group: grow
Agenda: https://datatracker.ietf.org/doc/draft-flechier-sidrops-pava/
page: https://datatracker.ietf.org/doc/draft-flechier-sidrops-pava/ | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
This document defines PAth VAlidation (PAVA), a scheme for validating the Border Gateway Protocol (BGP) AS_PATH field based on the AS relationships. Validation involves sending queries to the ASes along the path and each query specifies information about the prefix and the relevant path segment. In this draft, for the decentralized distribution system that ASes on a path need for distributing the information, we propose to use the Domain Name System (DNS) and DNSSEC.

### ADJ-RIB inout filtering
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-adj-rib-inout-filtering-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

### Draft Updates - Use-cases, Multi Peer, Rmon Aggr, Common updates, Gen & Rel (Prasad)
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-draft-updates-use-cases-multi-peer-rmon-aggr-common-updates-gen-rel-prasad-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

### PAVA: BGP AS PATH Validation v2
Presentation · Working group: grow
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-grow-pava-bgp-as-path-validation-v2-00 | video: https://youtu.be/bJpnkPWYS9U | materials: https://datatracker.ietf.org/meeting/126/session/grow
Slides presented at the grow session; no Internet-Draft is linked to them.

## Working Group: httpbis

### Resumable Uploads
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-resumable-uploads-00 | video: https://youtu.be/NxxvIMMNCt8 | materials: https://datatracker.ietf.org/meeting/126/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP/1.1 Request Smuggling Defense using Cryptographic Message Binding -01 version of draft
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-http11-request-smuggling-defense-using-cryptographic-message-binding-01-version-of-draft-00 | video: https://youtu.be/NxxvIMMNCt8 | materials: https://datatracker.ietf.org/meeting/126/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### HTTP Signature Keys
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-http-signature-keys-00 | video: https://youtu.be/NxxvIMMNCt8 | materials: https://datatracker.ietf.org/meeting/126/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### RESET STREAM AT in HTTP/3
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-reset-stream-at-in-http3-00 | video: https://youtu.be/NxxvIMMNCt8 | materials: https://datatracker.ietf.org/meeting/126/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### CONNECT-TCP
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-connect-tcp-00 | video: https://youtu.be/NxxvIMMNCt8 | materials: https://datatracker.ietf.org/meeting/126/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

### OHTTP: PFS & Key Config
Presentation · Working group: httpbis
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-httpbis-ohttp-pfs-key-config-00 | video: https://youtu.be/NxxvIMMNCt8 | materials: https://datatracker.ietf.org/meeting/126/session/httpbis
Slides presented at the httpbis session; no Internet-Draft is linked to them.

## Working Group: idr

### A Border Gateway Protocol 4 (BGP-4)
Draft: draft-ietf-idr-bgp4-rfc4271bis · Working group: idr
Agenda: draft-ietf-idr-bgp4-rfc4271bis-01
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-revised-slides-for-rfc4271bis-01-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document discusses the Border Gateway Protocol (BGP), which is an inter-Autonomous System routing protocol. The primary function of a BGP-speaking system is to exchange network reachability information with other BGP systems. This network reachability information includes information on the list of Autonomous Systems (ASes) that reachability information traverses. This information is sufficient for constructing a graph of AS connectivity for this reachability from which routing loops may be pruned, and, at the AS level, some policy decisions may be enforced. BGP-4 provides a set of mechanisms for supporting Classless Inter- Domain Routing (CIDR). These mechanisms include support for advertising a set of destinations as an IP prefix, and eliminating the concept of network "class" within BGP. BGP-4 also introduces mechanisms that allow aggregation of routes, including aggregation of AS paths. This document obsoletes RFC 4271 and many other RFCs. It updates RFC 7606 by subsuming its core functionality.

### BGP BFD Strict-Mode
Draft: draft-ietf-idr-bgp-bfd-strict-mode · Working group: idr
Agenda: draft-ietf-idr-bgp-bfd-strict-mode-18
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-bfd-strict-mode/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-2-bgp-bfd-strict-mode-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document specifies extensions to RFC4271 BGP-4 that enable a BGP speaker to negotiate additional Bidirectional Forwarding Detection (BFD) extensions using a BGP capability. This BFD Strict-Mode Capability enables a BGP speaker to prevent a BGP session from being established until a BFD session is established. This is referred to as BFD "strict-mode".

### YANG Model for Border Gateway Protocol (BGP-4)
Draft: draft-ietf-idr-bgp-model · Working group: idr
Agenda: draft-ietf-idr-bgp-model-19
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-4-yang-data-model-for-bgp-outbound-route-filtering-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document defines a YANG data model for configuring and managing BGP, including protocol, policy, and operational aspects, such as RIB, based on data center, carrier, and content provider operational requirements.

### YANG Data Model for BGP Outbound Route Filtering
Draft: draft-zw-idr-bgp-orf-yang-model · Working group: idr
Agenda: draft-zw-idr-bgp-orf-yang-model-00
page: https://datatracker.ietf.org/doc/draft-zw-idr-bgp-orf-yang-model/ | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document defines YANG data models for managing BGP Outbound Route Filter (ORF), including Address Prefix ORF, Covering Prefixes ORF (CP-ORF), and VPN Prefix ORF.

### Fully Adaptive Routing Ethernet using BGP
Draft: draft-xu-idr-fare · Working group: idr
Agenda: draft-xu-idr-fare-05
page: https://datatracker.ietf.org/doc/draft-xu-idr-fare/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-5-1-fully-adaptive-routing-ethernet-fare-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
Large language models (LLMs) like ChatGPT have become increasingly popular in recent years due to their impressive performance in various natural language processing tasks. These models are built by training deep neural networks on massive amounts of text data, as well as visual and video data, and often consist of billions or even trillions of parameters. However, the training process for these models can be extremely resource-intensive, requiring the deployment of thousands or even tens of thousands of GPUs in a single AI training cluster. Therefore, three-stage or even five-stage CLOS networks are commonly adopted for AI networks. The non-blocking nature of the network becomes increasingly critical for large-scale AI model training. Therefore, adaptive routing is necessary to dynamically distribute traffic to the same destination across multiple equal-cost paths, based on network capacity information along those paths.

### Fully Adaptive Routing Ethernet in Multi-Plane Scale-Out Networks
Draft: draft-xu-idr-fare-in-mpson · Working group: idr
Agenda: draft-xu-idr-fare-in-mpson-00
page: https://datatracker.ietf.org/doc/draft-xu-idr-fare-in-mpson/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-5-2-fully-adaptive-routing-ethernet-in-multi-plane-scale-out-networks-fare-in-mpson-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
FARE-BGP enables weighted ECMP load balancing using a path-bandwidth extended community. FARE-in-SUN extends this mechanism from switches to GPUs for scale-up networks, which are typically multi-plane. Large AI training clusters are increasingly adopting multi-plane scale-out network topologies. This document further extends FARE-BGP from switches to RoCE NICs (RNICs) for such multi-plane scale-out networks. The document also presents two techniques to address route scalability concerns caused by the injection of numerous host routes.

### BGP RR Deployment Considerations
Draft: draft-smith-idr-rr-deployment-considerations · Working group: idr
Agenda: draft-smith-idr-rr-deployment-considerations-00
page: https://datatracker.ietf.org/doc/draft-smith-idr-rr-deployment-considerations/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-bgp-rr-deployment-considerations-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
In BGP networks, Route Reflectors (RRs) simplify the provisioning of the Internal BGP (IBGP) control plane and mitigate the scaling challenges of maintaining a full mesh of IBGP sessions among border routers. Because of these operational benefits, RRs are widely deployed in modern networks utilizing BGP. This document describes common RR design options, their associated trade-offs, and deployment best practices based on industry operational experience. Operators should consider these suggestions when designing and operating BGP networks because BGP control plane stability is essential to overall network stability.

### BGP best path next-hop selection enhancements
Draft: draft-vroonen-idr-bgp-bestpath-nh-selection · Working group: idr
Agenda: draft-vroonen-idr-bgp-bestpath-nh-selection-03
page: https://datatracker.ietf.org/doc/draft-vroonen-idr-bgp-bestpath-nh-selection/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-7-bgp-best-path-next-hop-selection-enhancements-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
BGP [RFC4271] has originally been designed to carry IPv4 routing information over the Internet. IP routing being "hop-by-hop" in nature, NEXT_HOP which purpose is to carry the address of the next router to send the IP packet to. In BGP, the next-hop may not be a directly connected router, hence, when evaluating paths, a BGP speaker must determine if the next-hop is resolvable and, if so, determine the internal cost to reach it. The incremental use of tunneling technologies to carry traffic between routers (e.g.: GRE, MPLS, SR-MPLS, SRv6...) may violate the assumption that the address carried in the NEXT_HOP is representative of the actual forwarding next-hop. These technologies decouple the BGP control-plane's view of the next-hop from the data-plane's actual forwarding endpoint. This document describes the problems that arise from this decoupling. These problems include sub-optimal path selection, incorrect resolvability tracking of the forwarding path leading to traffic drop or misrouting, and others. This document specifies how BGP obtains resolvability, preference, metric, and tracking information from resolution of the forwarding path and uses those values as inputs to BGP path selection.

### Source-Selective BGP Framework
Draft: draft-braet-idr-source-selective-bgp-framework · Working group: idr
Agenda: draft-braet-idr-source-selective-bgp-framework-00
page: https://datatracker.ietf.org/doc/draft-braet-idr-source-selective-bgp-framework/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-source-selective-bgp-01 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
The Border Gateway Protocol (BGP) routes traffic solely based on destination IP prefixes. Source Selective BGP (SSB) introduces an architecture combining BGP and Resource Public Key Infrastructure (RPKI) extensions, which allows prefix holders to cryptographically signal RPKI source authorization policies for their advertised reachability. SSB distributes references to these policies via a new BGP path attribute, allowing routing systems to incorporate source-based constraints into local forwarding policies. Crucially, SSB does not define a source address validation mechanism, mandate packet filtering behavior, or alter fundamental destination-based routing; interpretation remains a matter of local operator policy. This document provides the overall architectural context and deployment rationale for the SSB protocol suite.

### BGP Source-Selective Attribute
Draft: draft-braet-idr-bgp-source-selective-attr · Working group: idr
Agenda: draft-braet-idr-bgp-source-selective-attr-00
page: https://datatracker.ietf.org/doc/draft-braet-idr-bgp-source-selective-attr/ | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document specifies a new Border Gateway Protocol (BGP) Path Attribute, the BGP SOURCE_SELECTIVE Attribute. This attribute allows BGP speakers to reference Resource Public Key Infrastructure (RPKI) Source Authorization (SA) objects, including Source Prefix Authorization (SPA), within BGP UPDATE messages. These objects are created by prefix holders to define sources authorized to originate traffic toward their prefixes or subprefixes. Receiving BGP speakers can use this information to enforce security policies. The SOURCE_SELECTIVE Path Attribute supports multiple Source Authorization Identifier (SA-ID) fields to preserve authorization semantics during BGP route aggregation and summarization. This mechanism applies to BGP AFI 1 / SAFI 1 (IPv4 Unicast) and AFI 2 / SAFI 1 (IPv6 Unicast).

### Canonical textual representation of BGP Path Attributes
Draft: draft-marenamat-idr-bgp-attribute-formatting · Working group: idr
Agenda: draft-marenamat-idr-bgp-attribute-formatting-01
page: https://datatracker.ietf.org/doc/draft-marenamat-idr-bgp-attribute-formatting/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-1-9-canonical-textual-representation-of-bgp-path-attributes-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
Various implementations of the Border Gateway Protocol (BGP) use different formats for displaying the Path Attributes. This document defines the preferred textual formatting which is recommended for the implementations to use for human interfaces. To achieve consistent value formatting, this document formally updates RFC 9026 by canonicalizing the well-known community name formats. This document updates RFC 4360, RFC 4577, RFC 7432, and ... by specifying the canonical textual formatting of extended communities specified there. This document updates RFC 4940 by adding a textual tag column to the OSPFv2 Link State Type registry. This document updates RFC 7153 by adding a textual tag column to the extended community registry. (REMOVE THIS) This document is incomplete and needs completing the tables.

### BGP Enhancements for ECMP EBGP Scenarios
Draft: draft-lin-idr-bgp-ecmp-ebgp-enhancements · Working group: idr
Agenda: draft-lin-idr-bgp-ecmp-ebgp-enhancements-00
page: https://datatracker.ietf.org/doc/draft-lin-idr-bgp-ecmp-ebgp-enhancements/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-110-bgp-enhancements-for-ecmp-ebgp-scenarios-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document proposes extensions to BGP to apply the RFC 5004 route persistence algorithm across parallel EBGP sessions and to suppress unnecessary advertisements between EBGP peers in the same AS. This document updates RFC 5004.

### Threat Model for BGP Color Extended Community
Draft: draft-yuan-idr-bgp-color-threats · Working group: idr
Agenda: draft-yuan-idr-bgp-color-threats-00
page: https://datatracker.ietf.org/doc/draft-yuan-idr-bgp-color-threats/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-11-threat-model-for-bgp-color-extended-community-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
The BGP Color Extended Community carries a user-defined Color value that is configured locally and has no globally standardized semantics. Although this design is suitable for local policy expression, it raises security concerns when Color values are propagated across Autonomous System (AS) boundaries and used to influence forwarding behavior in another domain. This document describes a threat model for that context, following the structure used by RFC 7132. It defines relevant terminology, characterizes the classes of adversaries considered to be threats, examines the classes of attacks that those threats are able to effect against Color-based forwarding, and concludes with a discussion of residual vulnerabilities. It does not revisit attacks against unprotected BGP, and it defines no new protocol mechanism.

### BGP Signaling of MASQUE Tunnel Encapsulation
Draft: draft-rosomakho-idr-bgp-masque-tunnel · Working group: idr
Agenda: draft-rosomakho-idr-bgp-masque-tunnel-00
page: https://datatracker.ietf.org/doc/draft-rosomakho-idr-bgp-masque-tunnel/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessb-bgp-signaling-of-masque-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document defines BGP Tunnel Encapsulation Attribute tunnel types for MASQUE CONNECT-TCP, CONNECT-UDP, CONNECT-IP, and CONNECT- ETHERNET. It also defines URI Template and SVCB Parameters Sub-TLVs for advertising the MASQUE proxy endpoint, the HTTP request target template, and extensible connection parameters used to establish the corresponding MASQUE tunnel.

### BGP Unreachable Prefix Announcement (UPA)
Draft: draft-krierhorn-idr-upa · Working group: idr
Agenda: draft-krierhorn-idr-upa-03
page: https://datatracker.ietf.org/doc/draft-krierhorn-idr-upa/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-upav2-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
Summarization is often used in multi-domain networks to improve network efficiency and scalability. With summarization in place, there is a need to signal loss of reachability to an individual prefix covered by the summary. This enables fast convergence by steering traffic away from the node which owns the prefix and is no longer reachable. This document specifies the mechanism, referred to as Unreachable Prefix Announcement (UPA), for networks where BGP is used to carry summary routes. It is also equally beneficial for operators to share the unreachable prefixes.

### BGP PORT EC for AIDC
Draft: draft-zhang-idr-portid-ec · Working group: idr
Agenda: draft-zhang-idr-portid-ec-02
page: https://datatracker.ietf.org/doc/draft-zhang-idr-portid-ec/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-2-3-bgp-port-ec-for-aidc-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document introduces a new BGP extended community attribute for AI computing scenarios. This attribute is used to carry the port ID when advertising routes on the switch before launching AI tasks, preparing for negotiation before sending large-scale traffic.

### RT-Constrain Optimization in Hierarchical Route Reflection Scenarios
Draft: draft-ietf-idr-rtc-hierarchical-rr · Working group: idr
Agenda: draft-ietf-idr-rtc-hierarchical-rr-05
page: https://datatracker.ietf.org/doc/draft-ietf-idr-rtc-hierarchical-rr/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessb-2-4-extensions-to-rt-constrain-in-hierarchical-route-reflection-scenarios-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
The Route Target (RT) Constrain mechanism specified in RFC 4684 is used to build a route distribution graph in order to restrict the propagation of Virtual Private Network (VPN) routes. In network scenarios where hierarchical route reflection (RR) is used, the existing RT-Constrain mechanism cannot guarantee a correct route distribution graph. This document describes the problem scenario and proposes solutions to address the RT-Constrain issue in hierarchical RR scenarios.

### Advertising p2mp policies in BGP
Draft: draft-ietf-idr-sr-p2mp-policy · Working group: idr
Agenda: draft-ietf-idr-sr-p2mp-policy-01
page: https://datatracker.ietf.org/doc/draft-ietf-idr-sr-p2mp-policy/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessb-2-6-bgp-sr-policy-extensions-for-bfd-configuration-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
SR P2MP policies are set of policies that enable architecture for P2MP service delivery. A P2MP policy consists of candidate paths (CPs) that connects the Root of the Tree to a set of Leaves. The P2MP policy is composed of replication segments [RFC9524]. A replication segment is a forwarding instruction for a candidate path which is downloaded to the Root, transit nodes and the leaves. This document specifies a new BGP SAFI with a new NLRI in order to advertise P2MP policy from a controller to a set of nodes. This document introduces three new route types within this NLRI, one for P2MP policy and its candidate paths that need to be programmed on the Root node, one for the replication segment incoming SID which uniquely will identify the replication state and another for each outgoing interface that the packets get replicated to. The last two route types are forwarding instructions that needs to be programmed on the Root, and optionally on Transit and Leaf nodes. It should be noted that this document does not specify how the Root and the Leaves are discovered on the controller, it only describes how the P2MP Policy and Replication Segments are programmed from the controller to the nodes.

### BGP SR Policy Extensions for BFD Configuration
Draft: draft-li-idr-bgp-sr-policy-bfd-extension · Working group: idr
Agenda: draft-li-idr-bgp-sr-policy-bfd-extension-02
page: https://datatracker.ietf.org/doc/draft-li-idr-bgp-sr-policy-bfd-extension/ | materials: https://datatracker.ietf.org/meeting/126/session/idr
Segment Routing (SR) Policies require fast failure detection for Candidate Paths (CPs) to enable rapid rerouting and high availability. Currently, the provisioning of SR Policies and the configuration of the associated Seamless Bidirectional Forwarding Detection (S-BFD) sessions are performed independently. This often necessitates separate mechanisms (e.g., manual configuration, NETCONF, or additional signaling) to associate S-BFD sessions with the SR Policies, resulting in complex and error-prone operations. This document defines extensions to BGP SR Policy for the simultaneous provisioning of SR Policy CPs and their S-BFD configuration parameters during policy advertisement. The extensions include optional sub-TLVs within the Tunnel Encapsulation Attribute to carry S-BFD configuration parameters (e.g., discriminators, intervals, multipliers). These extensions simplify deployment in distributed or controller- based environments, reduce configuration overhead, and enhance operational efficiency for SR-based traffic engineering.

### BGP Extensions for Inter-Domain Flexible Algorithm with Segment Routing over IPv6 (SRv6)
Draft: draft-gong-idr-inter-domain-srv6-flex-algo · Working group: idr
Agenda: draft-gong-idr-inter-domain-srv6-flex-algo-01
page: https://datatracker.ietf.org/doc/draft-gong-idr-inter-domain-srv6-flex-algo/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessb-2-7-bgp-extensions-for-inter-domain-flexible-algorithm-with-segment-routing-over-ipv6-srv6-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
IGP Flexible Algorithm (Flex-Algo) provides a mechanism for IGP nodes to compute the best paths according to a set of constraints in both the topology and computation metrics. Segment Routing over IPv6 (SRv6) can be used as one of the data plane of IGP Flex-Algo. In SRv6 networks, services may be carried across multiple network domains which are under the same administration. For some services, it is expected that the an end-to-end inter-domain path can be computed according to the same constraints (such as low latency) defined by Flex-Algo. This document describes BGP extensions to advertise SRv6 locators as IPv6 prefixes, together with the associated algorithm across the AS boundary.

### BGP Extensions for Network Resource Partition
Draft: draft-li-idr-bgp-nrp · Working group: idr
Agenda: draft-li-idr-bgp-nrp-01
page: https://datatracker.ietf.org/doc/draft-li-idr-bgp-nrp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessb-2-8-bgp-extensions-for-network-resource-partition-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
Existing approaches bind a Segment Routing (SR) Policy to a Network Resource Partition (NRP) on a one-to-one basis, which lacks flexibility and introduces significant operational overhead as the number of NRPs scales, especially when multiple NRPs share the same SR Policy path. This document defines BGP extensions to advertise NRP Identifier (NRP ID) information within BGP Update messages between headend and endpoint nodes. It decouples SR Policies from NRPs, allowing multiple NRPs to share a common SR Policy path and avoiding linear growth of SR Policies. The proposed design reduces operational complexity and also applies to SR Best Effort (SR BE) scenarios.

### BGP Link-State Extensions for BGP-only Networks
Draft: draft-ietf-idr-bgp-ls-bgp-only-fabric · Working group: idr
Agenda: draft-ietf-idr-bgp-ls-bgp-only-fabric-05
page: https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-bgp-only-fabric/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-bgp-link-state-extensions-for-bgp-only-networks-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
BGP is used as the only routing protocol in some networks today. In such networks, it is useful to get a detailed topology view similar to one available when using link state routing protocols. This document defines extensions to the BGP Link-state (BGP-LS) address- family and the procedures for advertisement of topology information in a BGP-only network.

### Advertising SAV Rule-related Information using BGP Link-State
Draft: draft-tong-idr-bgp-ls-sav-rule · Working group: idr
Agenda: draft-tong-idr-bgp-ls-sav-rule-05
page: https://datatracker.ietf.org/doc/draft-tong-idr-bgp-ls-sav-rule/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-2-10advertising-sav-rule-related-information-using-bgp-link-state-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document proposes extensions to the BGP Link-State protocol for advertising Source Address Validation (SAV) rule-related information for monitoring and management purposes.

### Problem Statement and Roadmap for BGP FlowSpec Monitoring
Draft: draft-cui-idr-flowspec-feedback-roadmap · Working group: idr
Agenda: draft-cui-idr-flowspec-feedback-roadmap-00
page: https://datatracker.ietf.org/doc/draft-cui-idr-flowspec-feedback-roadmap/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessc-3-1-problem-statement-and-roadmap-for-bgp-flowspec-monitoring-01 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document describes the problem space and roadmap for monitoring BGP Flow Specification (FlowSpec) deployments. It outlines the operational motivation for FlowSpec monitoring, identifies representative classes of monitoring information, and positions relevant work on FlowSpec, the BGP Monitoring Protocol (BMP), IP Flow Information Export (IPFIX), and YANG-based operational state within a common framework. The resulting roadmap provides common context for related protocol-specific work in the relevant IETF working groups.

### BGP Flow Specification Version 2 - for Basic IP
Draft: draft-ietf-idr-fsv2-ip-basic · Working group: idr
Agenda: draft-ietf-idr-fsv2-ip-basic-07
page: https://datatracker.ietf.org/doc/draft-ietf-idr-fsv2-ip-basic/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessc-3-2-bgp-flow-specification-version-2-for-basic-ip-00 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC 8956, and RFC 9117, describes the distribution of traffic filter policy (traffic filters and actions) distributed via BGP. During the deployment of BGP FSv1 a number of issues were detected, so version 2 of the BGP flow specification (FSv2) protocol addresses these issues. In order to provide a clear demarcation between FSv1 and FSv2, a different NLRI encapsulates FSv2. The IDR WG requires two implementation. Early feedback on implementations of FSv2 indicate that FSv2 has a correct design direction, but that breaking FSv2 into a progression of documents would aid deployment of the draft (basic and adding user ordered actions). This document specifies the basic FSv2 NLRI with user ordering of filters added to FSv1 IP Filters and FSv2 actions.

### Bitwise IP Filters for BGP FlowSpec
Draft: draft-kao-idr-bitwise-ip-filters · Working group: idr
Agenda: draft-kao-idr-bitwise-ip-filters-05
page: https://datatracker.ietf.org/doc/draft-kao-idr-bitwise-ip-filters/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessc-bitwise-ip-filters-for-bgp-flowspec-00 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document introduces the bitwise match filter component for source and destination IPv4/IPv6 address fields. These components enhance the BGP Flow Specification framework and provide a solution for dynamic symmetric traffic load-balancing.

### BGP Extensions to Enable BGP FlowSpec based IFIT
Draft: draft-he-idr-bgp-flowspec-ifit · Working group: idr
Agenda: draft-he-idr-bgp-flowspec-ifit-03
page: https://datatracker.ietf.org/doc/draft-he-idr-bgp-flowspec-ifit/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-bgp-extensions-to-enable-bgp-flowspec-based-ifit-00 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
Border Gateway Protocol (BGP) Flow Specification (FlowSpec) is an extension to BGP that supports the dissemination of traffic flow specifications and resulting actions to be taken on packets in a specified flow. In-situ Flow Information Telemetry (IFIT) denotes a family of flow-oriented on-path telemetry techniques, which can provide high-precision flow insight and real-time network issue notification. This document defines BGP extensions to distribute BGP FlowSpec based traffic filtering carrying IFIT information. Therefore, IFIT behavior can be automatically applied to the matched flow to capture real-time network dynamics.

### BGP Flow Specification for QUIC
Draft: draft-lin-idr-flowspec-quic · Working group: idr
Agenda: draft-lin-idr-flowspec-quic-00
page: https://datatracker.ietf.org/doc/draft-lin-idr-flowspec-quic/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessc-3-7-bgp-flow-specification-by-classid-01 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
A BGP Flow Specification is an n-tuple consisting of several matching criteria that can be applied to IP traffic. This document defines how to perform Flow Specification traffic diversion based on the characteristics of QUIC packets.

### BGP Flowspec Redirect Load Balancing Group Community
Draft: draft-wu-idr-flowspec-redirect-group · Working group: idr
Agenda: draft-wu-idr-flowspec-redirect-group
page: https://datatracker.ietf.org/doc/draft-wu-idr-flowspec-redirect-group/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessc-3-6-bgp-flowspec-redirect-load-balancing-group-community-00 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
This document defines an extension to the BGP Community Container Attribute, which allows flowspec redirection to multiple paths. This extended community serves to redirect traffic to a load balancing group and supports both equal-cost multi-path (ECMP) and unequal-cost multi-path (UCMP) scenarios.

### BGP Flow Specification by ClassID
Draft: draft-song-idr-flowspec-classid-filter · Working group: idr
Agenda: draft-song-idr-flowspec-classid-filter-01
page: https://datatracker.ietf.org/doc/draft-song-idr-flowspec-classid-filter/ | materials: https://datatracker.ietf.org/meeting/126/session/idr
BGP Flowspec mechanism (BGP-FS) [RFC8955] [RFC8956] propagates both traffic Flow Specifications and Traffic Filtering Actions by making use of the BGP NLRI and the BGP Extended Community encoding formats. This document specifies a new BGP-FS component type named ClassID to support ClassID filtering.

### 3. BGP YANG Update
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-3-bgp-yang-update-00 | video: https://youtu.be/csKXfIQpUXs | materials: https://datatracker.ietf.org/meeting/126/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### 5. Advertising p2mp policies in BGP
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessb-2-5-advertising-p2mp-policies-in-bgp-00 | video: https://youtu.be/XclSKFBYC18 | materials: https://datatracker.ietf.org/meeting/126/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

### 5. Filter for QUIC Connection ID
Presentation · Working group: idr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-3-5filter-for-quic-connection-id-00 | video: https://youtu.be/qr7hKbk8Y4c | materials: https://datatracker.ietf.org/meeting/126/session/idr
Slides presented at the idr session; no Internet-Draft is linked to them.

## Working Group: ipsecme

### Use of KMAC and SHAKE in the Internet Key Exchange Protocol Version 2 (IKEv2) and IPsec
Draft: draft-ietf-ipsecme-sha3 · Working group: ipsecme
Agenda: draft-ietf-ipsecme-sha3
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-sha3/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-use-of-sha-3-in-the-internet-key-exchange-protocol-version-2-ikev2-and-ipsec-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
This document specifies the use of KMAC128 and KMAC256 within the Internet Key Exchange Version 2 (IKEv2), Encapsulating Security Payload (ESP), and Authentication Header (AH) protocols. These algorithms can be used as integrity protection algorithms for ESP, AH and IKEv2, and as Pseudo-Random Functions (PRFs) for IKEv2. Requirements for supporting signature algorithms in IKEv2 that use SHA3-256, SHA3-384, SHA3-512, SHAKE128 and SHAKE256 are also specified.

### Post-quantum Key Exchange in IKEv2 with FrodoKEM
Draft: draft-ietf-ipsecme-hybrid-kem-ikev2-frodo · Working group: ipsecme
Agenda: draft-ietf-ipsecme-hybrid-kem-ikev2-frodo
page: https://datatracker.ietf.org/doc/draft-ietf-ipsecme-hybrid-kem-ikev2-frodo/ | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
FrodoKEM is an unstructured lattice based Key Encapsulation Mechanism (KEM), standardized by ISO. Compared to ML-KEM, it is considered with more conservative security. This draft specifies how to use FrodoKEM by itself or as an additional key exchange in IKEv2 along with a traditional key exchange. These options enable to negotiate IKE and Child SA keys that are safe against a Cryptographically Relevant Quantum Computer (CRQC).

### Multi-Authentication in IKEv2 with Post-quantum Security
Draft: draft-wang-ipsecme-multi-auth-ikev2-pq · Working group: ipsecme
Agenda: draft-wang-ipsecme-multi-auth-ikev2-pq
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-multi-auth-ikev2-pq/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-hybrid-post-quantum-and-traditional-authentication-for-ikev2-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
Motivated to mitigate security threats against quantum computers, this draft specifies a general authentication mechanism in the Internet Key Exchange Protocol Version 2 (IKEv2) [RFC7296], called Multi-Authentication. Namely, two peers can negotiate two or more authentication methods to authenticate each other. The authentication methods selected do not necessarily belong to the same category. This mechanism is achieved by adding a new value (17) (TBD) in the "IKEv2 Authentication Method" registry [IANA-IKEv2], maintained by IANA. To run Multi-Authentication, two peers send the SUPPORTED_AUTH_METHODS Notify, defined in [RFC9593], to negotiate two or more authentication methods for authentication in IKEv2. [EDNOTE: Code points for Multi-Authentication may need to be assigned in the "IKEv2 Authentication Method" registry [IANA-IKEv2], maintained by IANA]

### Post-Quantum Traditional (PQ/T) Hybrid PKI Authentication in the Internet Key Exchange Version 2 (IKEv2)
Draft: draft-hu-ipsecme-pqt-hybrid-auth · Working group: ipsecme
Agenda: draft-hu-ipsecme-pqt-hybrid-auth
page: https://datatracker.ietf.org/doc/draft-hu-ipsecme-pqt-hybrid-auth/ | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
One IPsec area that would be impacted by Cryptographically Relevant Quantum Computer (CRQC) is IKEv2 authentication based on traditional asymmetric cryptographic algorithms: e.g RSA, ECDSA, which are widely deployed authentication options of IKEv2. There are new Post-Quantum Cryptographic (PQC) algorithms for digital signature like NIST [ML-DSA], However, it takes time for new cryptographic algorithms to mature, There is security risk to use only the new algorithm before it is field proven. This document describes a hybrid PKI authentication scheme for IKEv2 that incorporates both traditional and PQC digital signature algorithms, so that authentication is secure as long as one algorithm in the hybrid scheme is secure.

### Hybrid Post-Quantum and Traditional Authentication for IKEv2
Draft: draft-reddy-ipsecme-pqt-hybrid-auth · Working group: ipsecme
Agenda: draft-reddy-ipsecme-pqt-hybrid-auth
page: https://datatracker.ietf.org/doc/draft-reddy-ipsecme-pqt-hybrid-auth/ | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
A Cryptographically Relevant Quantum Computer (CRQC) can break traditional public-key algorithms (e.g., RSA, ECDSA), which are typically used for authentication in IKEv2. Combining the post- quantum ML-DSA signature algorithm with a traditional signature algorithm provides protection against potential weaknesses or implementation flaws in ML-DSA. This draft defines a hybrid PKI authentication method for IKEv2 using composite certificates that ensures authentication remains secure as long as at least one of the component signature algorithms remains unbroken.

### PQ/T Hybrid Composite Key Exchange and Reliable Transport for IKEv2
Draft: draft-reddy-ipsecme-ikev2-hybrid-reliable · Working group: ipsecme
Agenda: draft-reddy-ipsecme-ikev2-hybrid-reliable
page: https://datatracker.ietf.org/doc/draft-reddy-ipsecme-ikev2-hybrid-reliable/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-pqt-hybrid-composite-key-exchange-reliable-transport-for-ikev2-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
The eventual transition to post-quantum key exchange will require elimination of traditional key exchange for reduced protocol complexity and efficiency. IKEv2 therefore requires a mechanism that can operate in a PQC-only environment, without depending on traditional key exchange algorithms (e.g., MODP DH or ECDH). As IKEv2 permits arbitrary combinations of algorithms, unnecessary complexity and insecure hybrid constructions are easily implemented. This document defines PQ/T hybrid composite key exchange algorithms for IKEv2 and a single combined KE payload that carries both the traditional and post-quantum components. It also leverages the existing IKEv2 reliable transport mechanism so that large PQC key exchange messages can be reliably exchanged over TCP. Together, these mechanisms enable secure and efficient PQ/T hybrid deployments today and provide a clear path for IKEv2 to operate in environments where traditional algorithms have been replaced by PQC algorithms.

### KEM-based Authentication for IKEv2 with Post-quantum Security
Draft: draft-wang-ipsecme-kem-auth-ikev2 · Working group: ipsecme
Agenda: draft-wang-ipsecme-kem-auth-ikev2
page: https://datatracker.ietf.org/doc/draft-wang-ipsecme-kem-auth-ikev2/ | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
This draft specifies a new authentication mechanism, called KEM (Key Encapsulation Mechanism) -based authentication, for the Internet Key Exchange Protocol Version 2 (IKEv2). This is motivated by the fact that some post-quantum KEMs (like ML-KEM) are more efficient than post-quantum signature algorithms (like ML-DSA).

### MLS for IPsec Group Key Exchange
Draft: draft-kohbrok-ipsecme-mls-gike · Working group: ipsecme
Agenda: draft-kohbrok-ipsecme-mls-gike
page: https://datatracker.ietf.org/doc/draft-kohbrok-ipsecme-mls-gike/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-mls-for-ipsec-group-key-management-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
This document describes a profile that uses the Messaging Layer Security (MLS) protocol as the group key-management substrate for Group Key Management using IKEv2 (G-IKEv2). The intent is to preserve the operational model of G-IKEv2, including IKEv2 transport, GSA policy distribution, a central GCKS, and the IPsec ESP data plane, while replacing GDOI-style group key distribution with an MLS group. The resulting design can be read as G-IKEv2 where MLS produces the per-epoch group secret used to key the IPsec ESP Data- Security SA.

### Stateless Encryption Profile for Enhanced Encapsulating Security Payload (EESP)
Draft: draft-xia-ipsecme-eesp-stateless-encryption · Working group: ipsecme
Agenda: draft-xia-ipsecme-eesp-stateless-encryption
page: https://datatracker.ietf.org/doc/draft-xia-ipsecme-eesp-stateless-encryption/ | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
This document specifies a stateless encryption profile for Enhanced Encapsulating Security Payload (EESP). The profile is intended for large-scale deployment scenarios in which maintaining per-flow or per-session encryption state is operationally expensive or infeasible. Instead of storing a distinct data key for each secure flow, endpoints derive per-packet or per-context data keys from a smaller set of provisioned root keying material together with packet- carried context. The document describes the deployment motivation, the stateless keying model, the mapping of required fields onto EESP extension points, context construction rules, data-key derivation processing, IV construction requirements, security considerations, and operational considerations. The intent is to realize stateless encryption as an extension profile over EESP, rather than as a parallel encapsulation format.

### Discussions and improvements on RFC 9370 ADDKE algorithm
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-discussions-and-improvements-on-rfc-9370-addke-algorithm-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### FrodoKEM for IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-frodokem-for-ikev2-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### Multi-Authentication in IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-multi-authentication-in-ikev2-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### PQ/T Hybrid PKI Authentication in IKEv2
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-pqt-hybrid-pki-authentication-in-ikev2-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

### PQC IKEv2 Authentication Analysis
Presentation · Working group: ipsecme
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-ipsecme-pqc-ikev2-authentication-analysis-00 | video: https://youtu.be/tPWaaKK39-I | materials: https://datatracker.ietf.org/meeting/126/session/ipsecme
Slides presented at the ipsecme session; no Internet-Draft is linked to them.

## Working Group: jose

### Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)
Draft: draft-ietf-jose-hpke-encrypt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-encrypt/ | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
This specification defines how to use Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE). HPKE enables public key encryption of arbitrary-sized plaintexts to a recipient's public key, and provides security against adaptive chosen ciphertext attacks. This specification chooses a specific subset of the HPKE features to use with JWE. This specification updates RFC 7516 (JWE) to enable use of Integrated Encryption as a Key Management Mode.

### JOSE: Deprecate 'none' and 'RSA1_5'
Draft: draft-ietf-jose-deprecate-none-rsa15 · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-deprecate-none-rsa15/ | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
This document updates RFC 7518 to deprecate the JWS algorithm "none" and the JWE algorithm "RSA1_5". These algorithms have known security weaknesses. It also updates the Review Instructions for Designated Experts to establish baseline security requirements that future algorithm registrations are expected to meet.

### JOSE HPKE PQ & PQ/T Algorithm Registrations
Draft: draft-ietf-jose-hpke-pq-pqt · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-pq-pqt/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-hpke-pq-pqt/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-jose-jose-hpke-pq-pqt-algorithms-01 | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
This document registers Post-Quantum (PQ) and Post-Quantum/ Traditional (PQ/T) hybrid algorithm identifiers for use with JSON Object Signing and Encryption (JOSE), building on the Hybrid Public Key Encryption (HPKE) framework.

### PQ/T Hybrid Composite Signatures for JOSE and COSE
Draft: draft-ietf-jose-pq-composite-sigs · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-jose-pqt-hybrid-composite-signatures-for-jose-and-cose-00 | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
This document describes JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) serializations for Post- Quantum Traditional (PQ/T) hybrid composite signatures. The composite algorithms described combine the Module-Lattice-Based Digital Signature Algorithm (ML-DSA) as the post-quantum component and either the Elliptic Curve Digital Signature Algorithm (ECDSA) or the Edwards-Curve Digital Signature Algorithm (EdDSA) as the traditional component.

### JSON Proof Algorithms
Draft: draft-ietf-jose-json-proof-algorithms · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-algorithms/ | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
The JSON Proof Algorithms (JPA) specification registers cryptographic algorithms and identifiers to be used with the JSON Web Proof, JSON Web Key (JWK), and COSE specifications. It defines IANA registries for these identifiers.

### JSON Proof Token and CBOR Proof Token
Draft: draft-ietf-jose-json-proof-token · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/ | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving representation of claims to be transferred between three parties. The claims in a JPT are encoded as base64url-encoded JSON objects that are used as the payloads of a JSON Web Proof (JWP) structure, enabling them to be digitally signed and selectively disclosed. JPTs also support reusability and unlinkability when using Zero-Knowledge Proofs (ZKPs). A CBOR-based representation of JPTs is also defined, called a CBOR Proof Token (CPT). It has the same properties as JPTs, but uses the JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based JWP Compact Serialization.

### JSON Web Proof
Draft: draft-ietf-jose-json-web-proof · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/
page: https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-jose-json-web-proofs-00 | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
The JOSE set of standards established JSON-based container formats for Keys, Signatures, and Encryption. They also established IANA registries to enable the algorithms and representations used for them to be extended. Since those were created, newer cryptographic algorithms that support selective disclosure and unlinkability have matured and started seeing early market adoption. The COSE set of standards likewise does this for CBOR-based containers, focusing on the needs of environments which are better served using CBOR, such as constrained devices and networks. This document defines a new container format similar in purpose and design to JSON Web Signature (JWS) and COSE Signed Messages called a _JSON Web Proof (JWP)_. Unlike JWS, which integrity-protects only a single payload, JWP can integrity-protect multiple payloads in one message. It also specifies a new presentation form that supports selective disclosure of individual payloads, enables additional proof computation, and adds a Presentation Header to prevent replay.

### BBS and Modular Sub-proofs with JSON Web Proofs
Draft: draft-bormann-jwp-modular-bbs · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-bormann-jwp-modular-bbs/
page: https://datatracker.ietf.org/doc/draft-bormann-jwp-modular-bbs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-jose-bbs-and-modular-sub-proofs-with-json-web-proofs-00 | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
This document defines a digital credential format that uses JSON Web Proofs (JWP) as its container format and Blind BBS Signatures as its signature scheme combined with a modular framework for attaching zero-knowledge sub-proofs. This allows a Holder to reveal some attributes directly while proving predicates such as range or equality over the ones they keep hidden. A credential can additionally be bound to a Holder-held device key, with possession of the key proven in every presentation without revealing the public key or signature. Concrete sub-proof and device-binding constructions are not defined in this document, only the core serialization. The credential type definition and data model follow SD-JWT VC.

### Long-Term Validation for JSON Web Signature (LTV-JWS)
Draft: draft-miyachi-ltv-jws · Working group: jose
Agenda: https://datatracker.ietf.org/doc/draft-miyachi-ltv-jws/
page: https://datatracker.ietf.org/doc/draft-miyachi-ltv-jws/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-jose-long-term-validation-for-json-web-signature-ltv-jws-02 | video: https://youtu.be/50iW_6AQzAk | materials: https://datatracker.ietf.org/meeting/126/session/jose
This specification extends JSON Web Signature (JWS, [RFC7515]) and defines LTV-JWS, a lightweight long-term signature format for Long- Term Validation (LTV). LTV-JWS adds signature extension elements, timestamps [RFC3161], validation information (certificates [RFC5280], CRLs [RFC5280], and OCSP responses [RFC6960]), and archive structures as minimal extensions, thereby enabling the validity of signatures to be verified over extended periods of time. In addition, archive timestamps enable continued validation even after the obsolescence or compromise of cryptographic algorithms. LTV-JWS preserves the simple structure and concept of JWS while progressively adding timestamps and validation information. It also enables more general-purpose signing use cases through indirect signatures using external references (refs).

## Working Group: lamps

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)
Draft: draft-ietf-lamps-kyber-certificates · Working group: lamps
Agenda: a) draft-ietf-lamps-kyber-certificates ( RFC 9935 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). This document specifies the conventions for using the ML-KEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Use of ML-KEM in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-kyber · Working group: lamps
Agenda: b) draft-ietf-lamps-cms-kyber ( RFC 9936 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-kyber/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a quantum-resistant key-encapsulation mechanism (KEM). Three parameter sets for the ML-KEM algorithm are specified by the US National Institute of Standards and Technology (NIST) in FIPS 203. In order of increasing security strength (and decreasing performance), these parameter sets are ML-KEM-512, ML-KEM-768, and ML-KEM-1024. This document specifies the conventions for using ML-KEM with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in "Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" (RFC 9629).

### Updates to Lightweight OCSP Profile for High Volume Environments
Draft: draft-ietf-lamps-rfc5019bis · Working group: lamps
Agenda: c) draft-ietf-lamps-rfc5019bis ( RFC 9919 )
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5019bis/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This specification defines a profile of the Online Certificate Status Protocol (OCSP) that addresses the scalability issues inherent when using OCSP in large scale (high volume) Public Key Infrastructure (PKI) environments and/or in PKI environments that require a lightweight solution to minimize communication bandwidth and client- side processing. This specification obsoletes RFC 5019. The profile specified in RFC 5019 has been updated to allow and recommend the use of SHA-256 over SHA-1.

### Certificate Management over CMS (CMC)
Draft: draft-ietf-lamps-rfc5272bis · Working group: lamps
Agenda: a) draft-ietf-lamps-rfc5272bis (RFC-to-be 10002)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5272bis/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines the base syntax for CMC, a Certificate Management protocol using the Cryptographic Message Syntax (CMS). This protocol addresses two immediate needs within the Internet Public Key Infrastructure (PKI) community:

### Certificate Management over CMS (CMC): Transport Protocols
Draft: draft-ietf-lamps-rfc5273bis · Working group: lamps
Agenda: b) draft-ietf-lamps-rfc5273bis (RFC-to-be 10003)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5273bis/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines a number of transport mechanisms that are used to move CMC (Certificate Management over CMS (Cryptographic Message Syntax)) messages. The transport mechanisms described in this document are HTTP, file, mail, and TCP. This document obsoletes RFC 5273 and RFC 6402.

### Certificate Management Messages over CMS (CMC): Compliance Requirements
Draft: draft-ietf-lamps-rfc5274bis · Working group: lamps
Agenda: c) draft-ietf-lamps-rfc5274bis (RFC-to-be 10004)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc5274bis/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document provides a set of compliance statements about the CMC (Certificate Management over CMS) enrollment protocol. The ASN.1 structures and the transport mechanisms for the CMC enrollment protocol are covered in other documents. This document provides the information needed to make a compliant version of CMC. This document obsoletes RFC 5274 and RFC 6402.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-sigs · Working group: lamps
Agenda: d) draft-ietf-lamps-pq-composite-sigs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines combinations of US NIST Module-Lattice-Based Digital Signature Algorithm (ML-DSA) in hybrid with traditional algorithms RSASSA-PKCS1-v1.5, RSASSA-PSS, ECDSA, Ed25519, and Ed448. These combinations are tailored to meet regulatory guidelines in certain regions. Composite ML-DSA is applicable in applications that use X.509 or PKIX data structures that accept ML-DSA, but where the operator wants extra protection against breaks or catastrophic bugs in ML-DSA, and where existential unforgeability (EUF-CMA) level security is acceptable.

### Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for use in Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-composite-sigs · Working group: lamps
Agenda: e) draft-ietf-lamps-cms-composite-sigs
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-sigs/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) defines combinations of ML-DSA with RSA, ECDSA, and EdDSA. This document specifies the conventions for using Composite ML-DSA algorithms within the Cryptographic Message Syntax (CMS).

### Media Access Control (MAC) Addresses in X.509 Certificates
Draft: draft-ietf-lamps-macaddress-on · Working group: lamps
Agenda: f) draft-ietf-lamps-macaddress-on
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-macaddress-on/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines a new GeneralName.otherName for inclusion in the X.509 Subject Alternative Name (SAN) and Issuer Alternative Name (IAN) extensions to carry an IEEE Media Access Control (MAC) address. The new name form makes it possible to bind a layer-2 interface identifier to a public key certificate. Additionally, this document defines how constraints on this name form can be encoded and processed in the X.509 Name Constraints extension (NCE).

### Clarification to Processing Key Usage Values During Certificate Revocation List (CRL) Validation
Draft: draft-ietf-lamps-keyusage-crl-validation · Working group: lamps
Agenda: g) draft-ietf-lamps-keyusage-crl-validation
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-keyusage-crl-validation/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
RFC 5280 (Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile) defines the profile of X.509 certificates and CRLs for use in the Internet. Section 4.2.1.3 of RFC 5280 requires CRL issuer certificates to contain the keyUsage extension with the cRLSign bit asserted. However, the CRL validation algorithm specified in Section 6.3 of RFC 5280 does not explicitly include a corresponding check for the presence of the keyUsage certificate extension. This document updates RFC 5280 to require that check.

### Composite ML-KEM for use in X.509 Public Key Infrastructure
Draft: draft-ietf-lamps-pq-composite-kem · Working group: lamps
Agenda: a) draft-ietf-lamps-pq-composite-kem
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines combinations of US NIST ML-KEM in hybrid with traditional algorithms RSA-OAEP, ECDH, X25519, and X448. These combinations are tailored to meet security best practices and regulatory guidelines. Composite ML-KEM is applicable in any application that uses X.509 or PKIX data structures that accept ML- KEM, but where the operator wants extra protection against breaks or catastrophic bugs in ML-KEM.

### Composite ML-KEM for use in Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-composite-kem · Working group: lamps
Agenda: b) draft-ietf-lamps-cms-composite-kem
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-composite-kem/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Composite ML-KEM defines combinations of Module-Lattice-based Key Encapsulation Mechanism (ML-KEM) with RSA-OAEP, ECDH, X25519, and X448. This document specifies the conventions for using Composite ML-KEM algorithms with the Cryptographic Message Syntax (CMS) using the KEMRecipientInfo structure defined in “Using Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)” (RFC 9629).

### Best Practices for Signed Attributes in CMS SignedData
Draft: draft-ietf-lamps-cms-euf-cma-signeddata · Working group: lamps
Agenda: c) draft-ietf-lamps-cms-euf-cma-signeddata
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-euf-cma-signeddata/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
The Cryptographic Message Syntax (CMS) has different signature verification behaviour based on whether signed attributes are present or not. This results in a potential existential forgery vulnerability in CMS and protocols which use CMS. This document describes the vulnerability and lists mitigations and best practices to avoid it. This document updates RFC 5652 by prohibiting the use of the id-data content type for new uses of the CMS SignedData type.

### Use of Remote Attestation with Certification Signing Requests
Draft: draft-ietf-lamps-csr-attestation · Working group: lamps
Agenda: d) draft-ietf-lamps-csr-attestation
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Certification Authorities (CAs) issuing certificates to Public Key Infrastructure (PKI) end entities may require a certificate signing request (CSR) to include additional verifiable information to confirm policy compliance. For example, a CA may require an end entity to demonstrate that the private key corresponding to a CSR's public key is secured by a hardware security module (HSM), is not exportable, etc. The process of generating, transmitting, and verifying additional information required by the CA is called remote attestation. While work is currently underway to standardize various aspects of remote attestation, a variety of proprietary mechanisms have been in use for years, particularly regarding protection of private keys. This specification defines ASN.1 structures which may carry attestation data for PKCS#10 and Certificate Request Message Format (CRMF) messages. Both standardized and proprietary attestation formats are supported by this specification.

### Requesting a Freshness Nonce for Attestation Evidence in Certificate Signing Requests
Draft: draft-ietf-lamps-attestation-freshness · Working group: lamps
Agenda: a) draft-ietf-lamps-attestation-freshness (Hannes, Hendrik)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-attestation-freshness/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-attestation-freshness-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
When an end entity includes attestation statements in a Certificate Signing Request (CSR), the freshness of the conveyed Evidence often needs to be established. A common mechanism is a nonce that is obtained from a Relying Party or Verifier and included by the Attester in the Evidence. This document specifies how an end entity requests such an attestation freshness nonce from an RA/CA when using certificate lifecycle management protocols. It defines message formats and protocol bindings for the conveyance of nonce request and response messages in the Certificate Management Protocol (CMP), Enrollment over Secure Transport (EST), and Certificate Management over CMS (CMC), including optional type-specific information needed to produce fresh Evidence for inclusion in a CSR.

### A Mechanism for X.509 Certificate Discovery
Draft: draft-ietf-lamps-certdiscovery · Working group: lamps
Agenda: b) draft-ietf-lamps-certdiscovery (John)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-certdiscovery/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document specifies a method to discover a referenced X.509 certificate associated with the current X.509 certificate. This enables efficient multi-certificate or fallback certificate handling in protocols. The objective is threefold: to enhance cryptographic agility, improve operational availability, and accommodate multi-key/ certificate usage. The proposed method aims to maximize compatibility with existing systems and is designed to be legacy- friendly, making it suitable for environments with a mix of legacy and new implementations. It includes mechanisms to provide a URI from which the referenced X.509 certificate can be retrieved as well as information about the target certificate's signature and public key algorithm, empowering relying parties to make informed decisions on whether to retrieve the Referenced Certificate, and a certificate hash to ensure that the correct certificate was retrieved.

### One Signature Certificates
Draft: draft-ietf-lamps-one-signature-certs · Working group: lamps
Agenda: c) draft-ietf-lamps-one-signature-certs (Stefan)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-one-signature-certs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-one-signature-certs-02 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines the signedDocumentBinding certificate extension, which binds a certificate to the signed content of a single digital signature. Each certificate is created at the time of signing; the associated signing key is generated for the sole purpose of producing that one signature, is used for no other purpose, and is destroyed immediately afterwards. Certificates carrying this extension are intended to be issued without a revocation mechanism and with no expiration, which simplifies long-term validation.

### Internet X.509 Public Key Infrastructure -- Algorithm Identifiers for the Fast-Fourier Transform over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA)
Draft: draft-ietf-lamps-fn-dsa-certificates · Working group: lamps
Agenda: d) draft-ietf-lamps-fn-dsa-certificates (Sean)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-fn-dsa-certificates/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Digital signatures are used within X.509 certificates and Certificate Revocation Lists (CRLs), and to sign messages. This document specifies the conventions for using, the forthcoming, FIPS 206, the Fast-Fourier Transform over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA), in Internet X.509 certificates and CRLs. The conventions for the associated signatures, subject public keys, and private key are also described.

### Use of the FN-DSA Signature Algorithm in the Cryptographic Message Syntax (CMS)
Draft: draft-ietf-lamps-cms-fn-dsa · Working group: lamps
Agenda: e) draft-ietf-lamps-cms-fn-dsa (Sean)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-cms-fn-dsa/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
The Fast-Fourier Transform over NTRU-Lattice-Based Digital Signature Algorithm (FN-DSA), as defined by NIST in FIPS 206, is a post-quantum digital signature scheme that aims to be secure against an adversary in possession of a Cryptographically Relevant Quantum Computer (CRQC). This document specifies the conventions for using the FN-DSA signature algorithm with the Cryptographic Message Syntax (CMS). In addition, the algorithm identifier is provided.

### Certificate Renewal Recommendations for Enrollment over Secure Transport
Draft: draft-ietf-lamps-est-renewal-info · Working group: lamps
Agenda: f) draft-ietf-lamps-est-renewal-info (Rifaat)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-est-renewal-info/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document describes an extension to RFC7030, Enrollment over Secure Transport to give an indication to a end-entity device when it should start attempting to renew its certificates. Prior art is that client decides, with a typical recommmendation to start when the remaining lifetime of the certificate is at the 50% point. As typical certificate lifetimes are reduced from years to fractions of a year, the 50% may be far too early, and this document provides a way to give alternate advice.

### Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Certificate Handling
Draft: draft-ietf-lamps-rfc8550bis · Working group: lamps
Agenda: g) draft-ietf-lamps-rfc8550bis (Sean)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc8550bis/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document specifies conventions for X.509 certificate usage by Secure/Multipurpose Internet Mail Extensions (S/MIME) v4.0 agents. S/MIME provides a method to send and receive secure MIME messages, and certificates are an integral part of S/MIME agent processing. S/ MIME agents validate certificates as described in RFC 5280 ("Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile"). S/MIME agents must meet the certificate-processing requirements in this document as well as those in RFC 5280. This document obsoletes RFC 5750.

### Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Message Specification
Draft: draft-ietf-lamps-rfc8551bis · Working group: lamps
Agenda: h) draft-ietf-lamps-rfc8551bis (Sean)
page: https://datatracker.ietf.org/doc/draft-ietf-lamps-rfc8551bis/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines Secure/Multipurpose Internet Mail Extensions (S/MIME) version 4.0. S/MIME provides a consistent way to send and receive secure MIME data. Digital signatures provide authentication, message integrity, and non-repudiation with proof of origin. Encryption provides data confidentiality. Compression can be used to reduce data size. This document obsoletes RFC 5751.

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for FrodoKEM
Draft: draft-smyslov-lamps-frodokem-certificates · Working group: lamps
Agenda: a) draft-smyslov-lamps-frodokem-certificates
page: https://datatracker.ietf.org/doc/draft-smyslov-lamps-frodokem-certificates/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
FrodoKEM is an unstructured lattice-based Key Encapsulation Mechanism (KEM). Compared to ML-KEM, FrodoKEM is considered as having more conservative design. This document specifies the conventions for using FrodoKEM in X.509 Public Key Infrastructure. The conventions for the subject public keys and private keys are also specified.

### Use of FrodoKEM in the Cryptographic Message Syntax
Draft: draft-chen-lamps-cms-frodokem · Working group: lamps
Agenda: b) draft-chen-lamps-cms-frodokem
page: https://datatracker.ietf.org/doc/draft-chen-lamps-cms-frodokem/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-lamps-cms-frodokem-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
FrodoKEM is a quantum-resistant key encapsulation mechanism (KEM) based on the standard Learning With Errors (LWE) problem，standardized by ISO. FrodoKEM offers multiple parameter sets, with the recommended sets for general use including (e)FrodoKEM-976-AES and (e)FrodoKEM-976-SHAKE for security level 3, and (e)FrodoKEM-1344-AES and (e)FrodoKEM-1344-SHAKE for security level 5. This document specifies the conventions for using FrodoKEM in the Cryptographic Message Syntax (CMS), using the KEMRecipientInfo structure defined in "Use of Key Encapsulation Mechanism (KEM) Algorithms in the Cryptographic Message Syntax (CMS)" [RFC9629].

### Updated Parameterized SIGNED ASN.1 Type for X.509 (PKIX)
Draft: draft-vangeest-lamps-update-asn1-signed-type · Working group: lamps
Agenda: c) draft-vangeest-lamps-update-asn1-signed-type (Daniel)
page: https://datatracker.ietf.org/doc/draft-vangeest-lamps-update-asn1-signed-type/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-updated-parameterized-signed-asn1-type-for-x509-pkix-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document updates some ASN.1 modules which conform to the syntax of the 2002 version of ASN.1 but feature constraints that are no longer consistent with usage of the associated structures. There are no bits-on-the-wire changes to any of the formats; this is simply a change to the syntax to better align with current practices.

### Preventing Key Reuse and Cross-Key Forgeries in Composite ML-DSA
Draft: draft-gray-lamps-compositepkc · Working group: lamps
Agenda: d) draft-gray-lamps-compositepkc (John)
page: https://datatracker.ietf.org/doc/draft-gray-lamps-compositepkc/ | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines a small, backwards-compatible change to composite ML-DSA that cryptographically binds the signature to the specific composite public key. It does so by defining a Public-Key Context value (pkc) equal to a hash of the serialized composite public key, and by setting the composite context field to that value. This prevents key reuse and cross-key forgeries across different composite keys, while preserving the API of Composite ML-DSA. The construction introduces two helper procedures to compute pkc from either the composite private key or the composite public key.

### Composite FN-DSA and LMS Digital Signature Algorithm for use in X.509 Public Key Infrastructure
Draft: draft-gray-lamps-composite-fndsa-lms · Working group: lamps
Agenda: e) draft-gray-lamps-composite-fndsa-lms (John)
page: https://datatracker.ietf.org/doc/draft-gray-lamps-composite-fndsa-lms/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-composite-fndsa-and-lms-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
This document defines a composite signature scheme combining the FN- DSA (Falcon) digital signature algorithm with the Leighton-Micali Signature (LMS) scheme defined in RFC 8554. This construction is designed for use within X.509 Public Key Infrastructure (PKI) and follows the composite signature paradigm defined in [I-D.ietf-lamps-pq-composite-sigs].

### Leafy Greens - End Entity Name Restrictions
Draft: draft-beck-lamps-leafy-greens · Working group: lamps
Agenda: f) draft-beck-lamps-leafy-greens (Bob)
page: https://datatracker.ietf.org/doc/draft-beck-lamps-leafy-greens/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-draft-beck-leafy-greens-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
The interaction of name constraint matching in [RFC5280] and wildcard subject alternative names creates a gap in which an excluded name constraint cannot be relied upon to prevent the issuance of certificates usable for the excluded name. This document defines End Entity Name Restrictions (EENR), a new critical X.509 extension for CA certificates that constrains the dNSName Subject Alternative Name entries which may appear in end entity certificates issued beneath the CA. EENR specifies its own matching semantics, including for wildcard dNSName entries, so that it does not depend on application- defined interpretations. The extension is scoped to use in certificate path validation for TLS client and TLS server authentication.

### S/MIMEbis (Certificates and Message Specifications)
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-smimebis-certificates-and-message-specifications-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Certificate Discovery
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-certificate-discovery-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Composite Public Key Context (PKC)
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-composite-public-key-context-pkc-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

### Name Constraints and Wildcards
Presentation · Working group: lamps
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lamps-name-constraints-and-wildcards-00 | video: https://youtu.be/-6giaIwniaY | materials: https://datatracker.ietf.org/meeting/126/session/lamps
Slides presented at the lamps session; no Internet-Draft is linked to them.

## Working Group: lsr

### IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)
Draft: draft-many-lsr-power-group · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-many-lsr-power-group/
page: https://datatracker.ietf.org/doc/draft-many-lsr-power-group/ | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
[I-D.many-teas-power-steering] introduces a Power Conserving Path Placement Strategy (PCPPS). When possible, PCPPS concentrates traffic onto a small set of network resources. When traffic is concentrated onto a small set of network resources, other network resources become idle and can be powered down until they are needed again. This conserves energy and reduces environmental impact. PCPPS uses information that is distributed by an IGP. This document specifies the IS-IS encoding for that information.

### IS-IS Packet Timestamping
Draft: draft-many-lsr-isis-packet-timestamping · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-many-lsr-isis-packet-timestamping/
page: https://datatracker.ietf.org/doc/draft-many-lsr-isis-packet-timestamping/ | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
Many applications in today’s networks rely on reliable and timely flooding of link-state information, such as, but not limited to Traffic Engineered networks. If such link-state information is delayed it can be difficult for those applications to adequately fulfill their intended functionality. This document describes extensions to ISIS supporting distribution of fragment origination time. The origination time can be used to aid troubleshooting and/or by the applications themselves to improve their behavior. Timestamping can be also used to detect replay attack which are not addressed in IS-IS currently.

### IS-IS Aggregated SNP Hash Packets
Draft: draft-prz-lsr-ash-packets · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/
page: https://datatracker.ietf.org/doc/draft-prz-lsr-ash-packets/ | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
The document presents an optional new type of database synchronization packet called an Aggregated SNP Hash (ASH). When feasible, it compresses traditional SNP exchanges into a dynamic Merkle tree-like structure, which speeds up synchronization of large databases and adjacency numbers while reducing the load from regular CSNP exchanges during normal operation. Just like CSNPs and PSNPs, ASH packets come in two flavors, called Complete ASH (CASH) and Partial ASH (PASH).

### Advertising IGP Active Measurement Groups in Router Capabilities
Draft: draft-admnr-lsr-igp-measurement-group · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/
page: https://datatracker.ietf.org/doc/draft-admnr-lsr-igp-measurement-group/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-igp-active-measurement-group-01 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
This document defines IGP capability advertisements for measurement group membership for Active Measurement Protocols (AMPs) such as TWAMP and STAMP. An IS-IS capability sub-TLV is defined for IS-IS and an OSPF Router Information (RI) LSA TLV is defined for OSPFv2 and OSPFv3. The mechanism allows IGP routers to discover other routers participating in different measurement groups, enabling automatic discovery of measurement endpoints throughout an IS-IS or OSPF routing domain. The solution uses a Group ID to identify measurement group membership, where the same interface address (IPv4 or IPv6) may be used for multiple measurement groups. A corresponding BGP - Link State (BGP-LS) node-level attribute is defined to distribute measurement group membership beyond a single IGP domain.

### IS-IS Traffic Engineering Extensions For Microburst
Draft: draft-ruan-lsr-isis-te-extensions-for-microburst · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-ruan-lsr-isis-te-extensions-for-microburst/
page: https://datatracker.ietf.org/doc/draft-ruan-lsr-isis-te-extensions-for-microburst/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-06-is-is-traffic-engineering-extensions-for-microburst-02 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
This document defines IS-IS and OSPF sub-TLVs and a BGP-Link State (BGP-LS) Link Attribute TLV for advertising aggregated measurements of microburst activity on a unidirectional link. The information is reported for an identified traffic class and includes event, packet- drop, and queue-occupancy statistics. An Anomalous (A) bit carries a locally determined anomaly indication. This document specifies the encoding and distribution of the information. Microburst detection, loss attribution, threshold selection, and actions taken by a consumer are outside the scope of this document.

### Distributed Congestion Mitigation
Draft: draft-psenak-lsr-igp-dcm · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-psenak-lsr-igp-dcm/
page: https://datatracker.ietf.org/doc/draft-psenak-lsr-igp-dcm/ | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
This document describes the Distributed Congestion Mitigation (DCM) mechanism using the Interior Gateway Protocols (IGPs) such as IS-IS [RFC1195], OSPFv2 [RFC2328], or OSPFv3 [RFC5340]. DCM is a tactical, distributed mechanism, designed to mitigate network congestion by offloading traffic to an alternate, congestion-free paths. DCM is fully integrated in IGPs.

### IGP Encoding for SRv6 Mirror SID in Egress Protection
Draft: draft-he-lsr-srv6-mirror-sid-igp-encoding · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-he-lsr-srv6-mirror-sid-igp-encoding/
page: https://datatracker.ietf.org/doc/draft-he-lsr-srv6-mirror-sid-igp-encoding/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-8-srv6-mirror-sid-igp-encoding-02 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
This document specifies the IGP protocol extensions required to support SRv6 path egress protection using the Mirror SID (End.M) mechanism. It reuses the existing SRv6 End SID sub-TLV defined in RFC 9352 (IS-IS, Section 7.2) and RFC 9513 (OSPFv3, Section 8) with the End.M endpoint behavior (74) to advertise the Mirror SID and the set of protected locators, and defines a new Protected Locators sub-(sub-)TLV. enabling a backup egress node (protector) to signal its capability to protect a primary egress node within a single link- state IGP area. This document is a companion to [I-D.ietf-rtgwg-srv6-egress-protection], which specifies the overall SRv6 path egress protection mechanism and the End.M behavior. The IGP encoding defined herein provides the signaling substrate for that mechanism.

### IS-IS Originator Sequence Number Checksum TLV
Draft: draft-hegde-lsr-isis-osnc · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-hegde-lsr-isis-osnc/
page: https://datatracker.ietf.org/doc/draft-hegde-lsr-isis-osnc/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-draft-hegde-lsr-isis-osnc-00-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
This document introduces a new top-level TLV in IS-IS to carry a checksum over the LSP IDs and sequence numbers of all self-originated LSP fragments. A receiving node uses this value to validate the integrity of the originator's Link State Database (LSDB).

### IS-IS Process ID Verification
Draft: draft-hu-lsr-isis-process-verification · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-hu-lsr-isis-process-verification/
page: https://datatracker.ietf.org/doc/draft-hu-lsr-isis-process-verification/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-draft-hu-lsr-isis-process-verification-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
In IS-IS deployments, the process identifier (process ID) is used on a local router to distinguish and manage different IS-IS protocol instances. Process ID is local to the router and is not transmitted to neighbors, providing operational flexibility. However, because the process ID is also used to implement route redistribution and specify administrative tags for fine-grained control, its misconfiguration can lead to severe impacts (e.g., routing loops or black holes) with difficult troubleshooting. To address this problem, network operators typically deploy a consistent process ID on both ends of a link within the same domain, to reduce configuration complexity. In this context, to avoid the misconfiguration of the IS-IS process ID, this document introduces two optional approaches for process ID verification. When process ID verification is enabled, an IS-IS adjacency can be established only when the process identifiers at both ends of the link match.

### Metric Normalize for IGP Flex-algo
Draft: draft-gl-lsr-metric-normalize · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/
page: https://datatracker.ietf.org/doc/draft-gl-lsr-metric-normalize/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-12-metric-normalize-for-igp-flex-algo-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
When multiple links in a network have the same metric, they can serve as ECMP equivalent links for load balancing during forwarding. However, slight fluctuations in metric values can prevent the formation of ECMP equivalent links, leading to the idle state of suboptimal links and thus wasting bandwidth resources. This document proposes a metric normalization method by advertising metric normalization parameters corresponding to a specific Metric- Type for Flexible Algorithm. During route calculation, slight fluctuations across multiple links are adjusted according to these normalization parameters, making the computed metric values more consistent. This approach enables the formation of ECMP equivalent links and promotes load sharing in the forwarding process.

### Detection of Router-ID Conflicts in IGPs
Draft: draft-lg-lsr-router-id-conflict-detect · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-lg-lsr-router-id-conflict-detect/
page: https://datatracker.ietf.org/doc/draft-lg-lsr-router-id-conflict-detect/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-13-lsr-router-id-conflict-detect-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
In link-state Interior Gateway Protocols (IGPs) such as OSPF and IS- IS, the router ID (or system ID) serves as a unique identifier for routers within a routing domain. Duplicate router IDs can lead to severe network instability, including persistent Link State Advertisement (LSA/LSP) flooding, inconsistent Link State Databases (LSDBs), and permanent forwarding loops. This document defines mechanisms for detecting such conflicts between non-adjacent routers and proposes procedures to alert network operators, along with defining the corresponding YANG interface and event YANG notifications for OAM operations.

### Export of IGP Algorithm Information in IPFIX
Draft: draft-liu-opsawg-ipfix-igp-algo · Working group: lsr
Agenda: https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-igp-algo/
page: https://datatracker.ietf.org/doc/draft-liu-opsawg-ipfix-igp-algo/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-export-of-igp-algorithm-information-in-ipfix-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
This document introduces two IPFIX information elements (IEs) to identify the IGP Algorithm and Multi-Topology Identifier associated with the forwarding entry used for an observed packet.

### LSR Status
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-01-lsr-status-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### Using IS-IS to Advertise Power Groups
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-using-is-is-to-advertise-power-groups-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### lsr-timestamp
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-lsr-timestamp-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### ash-00
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-ash-00-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

### ISIS DCM IETF 126
Presentation · Working group: lsr
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-lsr-isis-dcm-ietf-126-00 | video: https://youtu.be/ExzDVs2e4o0 | materials: https://datatracker.ietf.org/meeting/126/session/lsr
Slides presented at the lsr session; no Internet-Draft is linked to them.

## Working Group: masque

### Extensions to Compress and Derive Fields in HTTP Datagrams
Draft: draft-ietf-masque-http-datagram-compression · Working group: masque
Agenda: draft-ietf-masque-http-datagram-compression by Yaroslav Rosomakho, Tommy Pauly (20 minutes)
page: https://datatracker.ietf.org/doc/draft-ietf-masque-http-datagram-compression/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-masque-http-datagram-compression-00 | video: https://youtu.be/_aGL2D7LuA8 | materials: https://datatracker.ietf.org/meeting/126/session/masque
This document defines extensions for HTTP Datagram-based protocols that improve transmission efficiency by introducing templates for compressing or deriving datagram fields. These templates allow endpoints to define parts of datagrams that are static and can be removed, and other parts that can be derived (such as packet lengths and checksum values). Additionally, this document defines a checksum offload procedure enabling receivers to complete Internet checksums using sender- provided partial values. These optimisations reduce per-packet overhead and processing cost. Compression can allow larger original packets to fit in QUIC DATAGRAM frames, depending on the applicable processing context and path maximum transmission unit (MTU).

### ECN and DSCP support for HTTPS's Connect-UDP
Draft: draft-ietf-masque-connect-udp-ecn-dscp · Working group: masque
Agenda: draft-ietf-masque-connect-udp-ecn-dscp by Mirja Kühlewind (20 minutes)
page: https://datatracker.ietf.org/doc/draft-ietf-masque-connect-udp-ecn-dscp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-masque-ecn-and-dscp-support-for-httpss-connect-udp-00 | video: https://youtu.be/_aGL2D7LuA8 | materials: https://datatracker.ietf.org/meeting/126/session/masque
HTTP's Extended Connect's Connect-UDP protocol enables a client to proxy a UDP flow from the HTTP server towards a specified target IP address and UDP port. QUIC and Real-time transport protocol (RTP) are examples of transport protocols that use UDP and support Explicit Congestion Notification (ECN) and provide the necessary feedback. This document specifies how ECN and DSCP can be supported through an extension to the Connect-UDP protocol for HTTP without per-packet byte overhead, solely using Context IDs.

### HTTP Header Fields for Proxying DNS SVCB Information
Draft: draft-gakiwate-dnsop-proxy-dns-svcb · Working group: masque
Agenda: draft-gakiwate-dnsop-proxy-dns-svcb by Gautam Gakiwate (10 minutes)
page: https://datatracker.ietf.org/doc/draft-gakiwate-dnsop-proxy-dns-svcb/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-masque-http-header-fields-for-proxying-dns-svcb-information-00 | video: https://youtu.be/_aGL2D7LuA8 | materials: https://datatracker.ietf.org/meeting/126/session/masque
When HTTP clients use the CONNECT method or UDP proxying (CONNECT- UDP) to reach target servers through a proxy, the proxy performs DNS resolution on behalf of the client. This prevents the client from accessing Service Binding (SVCB and HTTPS) DNS records that carry service configuration such as supported protocols and Encrypted Client Hello keys. This document defines HTTP header fields that enable the proxy to relay SVCB information to the client, and introduces a conditional early closure mechanism that allows the client to coordinate with the proxy to abort a connection when specific SVCB parameters are present, so that the client can retry with a different connection strategy.

### BGP Signaling of MASQUE
Presentation · Working group: masque
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-masque-bgp-signaling-of-masque-00 | video: https://youtu.be/_aGL2D7LuA8 | materials: https://datatracker.ietf.org/meeting/126/session/masque
Slides presented at the masque session; no Internet-Draft is linked to them.

## Working Group: oauth

### Identity Assertion JWT Authorization Grant
Draft: draft-ietf-oauth-identity-assertion-authz-grant · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessa-identity-assertion-jwt-authorization-grant-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This specification provides a mechanism for an application to use an identity assertion to obtain an access token for a third-party API by coordinating through an identity provider that the downstream Resource Authorization Server already trusts for single sign-on (SSO), using OAuth 2.0 Token Exchange (RFC 8693) and the JWT Profile for OAuth 2.0 Authorization Grants (RFC 7523). This pattern is informally referred to as Cross-App Access (XAA).

### OAuth Client ID Metadata Document
Draft: draft-ietf-oauth-client-id-metadata-document · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessa-client-id-metadata-document-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This specification defines a mechanism through which an OAuth client can identify itself to authorization servers, without prior dynamic client registration or other existing registration. This is through the usage of a URL as a client_id in an OAuth flow, where the URL refers to a document containing the necessary client metadata, enabling the authorization server to fetch the metadata about the client as needed.

### Updates to OAuth 2.0 Security Best Current Practice
Draft: draft-ietf-oauth-security-topics-update · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-security-topics-update/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-security-topics-update/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessa-updates-to-oauth-20-security-best-current-practice-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document updates the set of best current security practices for OAuth 2.0 by extending the security advice given in RFC 6749, RFC 6750, and RFC 9700, to cover new threats that have been discovered since the former documents have been published.

### OAuth SPIFFE Client Authentication
Draft: draft-ietf-oauth-spiffe-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessa-oauth-spiffe-client-authentication-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This specification profiles the Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants [RFC7521], the JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants [RFC7523], and OAuth 2.0 Attestation-Based Client Authentication [I-D.draft-ietf-oauth-attestation-based-client-auth] to enable the use of SPIFFE Verifiable Identity Documents (SVIDs) as client credentials in OAuth 2.0. It defines how OAuth clients with SPIFFE credentials can authenticate to OAuth authorization servers using their JWT-SVIDs, WIT-SVIDs, or X.509-SVIDs without the need for client secrets. This approach enhances security by enabling seamless integration between SPIFFE-enabled workloads and OAuth authorization servers while eliminating the need to distribute and manage shared secrets such as static client secrets.

### OAuth Transaction Authorization Challenge
Draft: draft-rosomakho-oauth-txn-challenge · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-rosomakho-oauth-txn-challenge/
page: https://datatracker.ietf.org/doc/draft-rosomakho-oauth-txn-challenge/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessa-oauth-transaction-authorization-challenge-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document defines an OAuth mechanism for transaction-specific authorization challenges. A protected resource can require additional authorization for a particular operation by returning a transaction authorization challenge. This is useful when requests are mediated by agents, automated workflows, or delegated services and the protected resource requires confirmation from a human user, resource owner, or organizational authority. The client presents the challenge to an authorization server, which validates the challenge, obtains any required approval, and issues an OAuth 2.0 access token whose granted authorization details, expressed using Rich Authorization Requests, describe the approved operation. The access token is then presented to the protected resource as evidence that the challenged operation was authorized.

### AAuth Protocol
Draft: draft-hardt-oauth-aauth-protocol · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/
page: https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/ | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document defines the AAuth authorization protocol for agent-to- resource authorization and identity claim retrieval. The protocol supports five resource access modes — agent identity, resource- managed (two-party), person identity, PS authorization (three-party), and federated authorization (four-party) — with agent governance as an orthogonal layer. It builds on the HTTP Signature Keys specification ([I-D.hardt-httpbis-signature-key]) for HTTP Message Signatures and key discovery.

### KYAPay Token
Draft: draft-skyfire-oauth-kyapay-token · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/
page: https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/ | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document defines a token format for agent identity and payment tokens in JSON Web Token (JWT) format. Authorization servers and resource servers from different vendors can leverage this token format to consume identity and payment tokens in an interoperable manner.

### Agent Authorization use cases and gap analysis
Draft: draft-chen-oauth-agent-authz-use-cases · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/
page: https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-agent-authorization-use-cases-and-gap-analysis-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document provides a systematic analysis of these emerging agent- based use cases. It categorizes them into distinct scenarios, details their specific authorization requirements, and performs a comprehensive gap analysis against the existing OAuth 2.0 framework[RFC6749] and its common extensions. The analysis identifies fundamental gaps and requirements, providing a foundation for future work on new extensions within the OAuth Working Group toward creating a more secure and interoperable ecosystem for agent- based systems.

### OAuth 2.0 Attestation-Based Client Authentication
Draft: draft-ietf-oauth-attestation-based-client-auth · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/
page: https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessb-attestation-based-client-authentication-00 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This specification defines an extension to the OAuth 2.0 protocol (RFC 6749) that enables a client instance to include a key-bound attestation when interacting with an Authorization Server or Resource Server. This mechanism allows a client instance to prove its authenticity, as verified by a client attester, without revealing its target audience to that attester. It may also serve as a mechanism for client authentication as per OAuth 2.0.

### OAuth Proof of Possession Tokens with HTTP Message Signatures
Draft: draft-richer-oauth-httpsig · Working group: oauth
Agenda: https://www.ietf.org/archive/id/draft-richer-oauth-httpsig-01.html
page: https://datatracker.ietf.org/doc/draft-richer-oauth-httpsig/ | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This extension to the OAuth 2.0 authorization framework defines a method for using HTTP Message Signatures to bind access tokens to keys held by OAuth 2.0 clients. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Web Authorization Protocol Working Group mailing list (oauth@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/oauth/. Source for this draft and an issue tracker can be found at https://github.com/jricher/draft-richer-oauth-httpsig.

### OAuth 2.0 RAR Metadata and Error Remediation
Draft: draft-zehavi-oauth-rar-metadata · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-zehavi-oauth-rar-metadata/
page: https://datatracker.ietf.org/doc/draft-zehavi-oauth-rar-metadata/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-rar-metadata-and-error-remediation-02 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
OAuth 2.0 Rich Authorization Requests (RAR) [RFC9396] standardizes the exchange and processing of authorization details but does not define metadata for describing authorization details types. In addition, no interoperable guidance is offered to clients, to remediate failures by resource servers due to insufficient authorization details. This document addresses this interoperability challenge, allowing clients to dynamically discover metadata instead of relying on out- of-band agreements, as well as standardizes failure signaling including interoperable remediation when insufficient authorization details are the cause of failure.

### OAuth Client Challenge Protocol
Draft: draft-kahrer-oauth-client-challenge-protocol · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/html/draft-kahrer-oauth-client-challenge-protocol
page: https://datatracker.ietf.org/doc/draft-kahrer-oauth-client-challenge-protocol/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-oauth-client-challenge-protocol-00 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document extends the OAuth 2.0 token endpoint error response (RFC 6749) with a new error code that indicates to the client that it must provide additional input for the authorization server to authorize it and accept its request. This mechanism enables just-in-time authorization flows in which the authorization server dynamically challenges the client during a request and the client tries to satisfy it. For example, the authorization server can ask the client mid-flow to provide an assertion, a verifiable presentation, or other proof-of-possession material.

### Deferred Token Response
Draft: draft-gerber-oauth-deferred-token-response · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-gerber-oauth-deferred-token-response/
page: https://datatracker.ietf.org/doc/draft-gerber-oauth-deferred-token-response/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessb-deferred-token-response-01 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document defines the Deferred Token Response (DTR) extension for OAuth 2.1. In existing OAuth grants, the token endpoint either issues an access token or returns an error. DTR establishes a generic asynchronous token request mechanism that any OAuth grant may plug into. In DTR-aware flows, the authorization server returns a deferral_code and a polling interval, indicating that the final token response will be available at a later time. The client retrieves the eventual response by polling the token endpoint, or by receiving a callback from the authorization server when one is configured.

### JSON Web Token (JWT) Profile for OAuth 2.0 Enveloped Proof of Possession (EPOP)
Draft: draft-ambekar-oauth-epop · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-ambekar-oauth-epop/
page: https://datatracker.ietf.org/doc/draft-ambekar-oauth-epop/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-jwt-profile-for-oauth-20-enveloped-proof-of-possession-epop-00 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This specification defines a profile for OAuth 2.0 sender-constrained credentials in which access tokens and refresh tokens are cryptographically bound to the client's private key as a single inseparable envelope. Authorization code flows are also covered: the client declares its public key binding via cnf.jkt in the EPOP token presented at the token endpoint, ensuring the authorization code can only be exchanged by the key-holding client; the code itself travels as the standard code form parameter. Unlike existing mechanisms, EPOP provides proof-of-possession uniformly across both JWT and opaque access tokens, and across HTTP and non-HTTP transports. The profile extends sender-constraining beyond HTTP to non-HTTP transports including MQTT, Kafka, the Model Context Protocol (MCP), gRPC, and SASL-based protocols such as those defined in [RFC7628]. It introduces atomic proof-of-possession key rotation, enabling clients to rotate key pairs without disrupting active sessions, and an offline-derived client nonce (cnonce) that eliminates the server- issued nonce round-trip required by existing mechanisms — enabling stateless proof validation critical for non-HTTP and high-throughput deployments. Authorization servers, resource servers, and clients from different vendors can implement this profile interoperably.

### Delegate SD-JWT
Draft: draft-gco-oauth-delegate-sd-jwt · Working group: oauth
Agenda: https://datatracker.ietf.org/doc/draft-gco-oauth-delegate-sd-jwt/
page: https://datatracker.ietf.org/doc/draft-gco-oauth-delegate-sd-jwt/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-delegate-sd-jwts-00 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
This document specifies an extension to Selective Disclosure JSON Web Tokens to support further delegation from the Holder to a Delegate Holder. This is done by allowing the Key Binding JWT to also be an SD-JWT, optionally with its own Key Binding. This has particular applicability to Agentic systems.

### Self Driving Software
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-self-driving-software-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Agentic Use Cases and Gaps Informed by Experience with KYAPay Technologies
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-agentic-use-cases-and-gaps-informed-by-experience-with-kyapay-technologies-00 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### HTTP Message Signatures for OAuth PoP
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-http-message-signatures-for-oauth-pop-02 | video: https://youtu.be/yhE1FL8VW7E | materials: https://datatracker.ietf.org/meeting/126/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Policy Language Binding for OAuth
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessb-policy-language-binding-for-oauth-00 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

### Clustering of OAuth WG Work
Presentation · Working group: oauth
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessb-clustering-of-oauth-wg-work-00 | video: https://youtu.be/XxkhXxInz3k | materials: https://datatracker.ietf.org/meeting/126/session/oauth
Slides presented at the oauth session; no Internet-Draft is linked to them.

## Working Group: quic

### Reverso for the QUIC protocol
Draft: draft-frochet-quicwg-reverso-for-quic · Working group: quic
Agenda: https://datatracker.ietf.org/doc/draft-frochet-quicwg-reverso-for-quic/
page: https://datatracker.ietf.org/doc/draft-frochet-quicwg-reverso-for-quic/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-reverso-for-quic-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
This document describes a QUIC version re-designing the layout of the QUIC protocol to avoid memory fragmentation at the receiver and allows implementers seeking a more efficient implementation to have the option to implement contiguous zero-copy at the receiver. This document describes the change from QUIC v1 required in packet formats, variable-length integers and frame formats. Everything else from QUIC v1 described in [RFC9000] is untouched.

### QMux
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-qmux-01 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Extended Key Update
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-extended-key-update-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Receive Timestamps
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-receive-timestamps-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### qlog
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-qlog-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### TAPS - CTAPS and gaps
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-taps-ctaps-and-gaps-01 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### GCM-SST in QUIC
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-gcm-sst-in-quic-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Mutable Idle Timeout?
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-mutable-idle-timeout-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### Telemetry on HTTPS RR and QUIC v2 adoption
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-telemetry-on-https-rr-and-quic-v2-adoption-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### QUIC and multicast
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-quic-and-multicast-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

### n0 NAT Traversal
Presentation · Working group: quic
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-n0-nat-traversal-00 | video: https://youtu.be/Pzy_4svJ4vY | materials: https://datatracker.ietf.org/meeting/126/session/quic
Slides presented at the quic session; no Internet-Draft is linked to them.

## Working Group: rats

### Evidence Encoding for Hardware Security Modules
Draft: draft-ietf-rats-pkix-key-attestation · Working group: rats
Agenda: (10 + 5 QA + 5 LC): Mike Ounsworth - draft-ietf-rats-pkix-key-attestation
page: https://datatracker.ietf.org/doc/draft-ietf-rats-pkix-key-attestation/ | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
This document specifies a vendor-agnostic format for Evidence produced and verified within a PKIX context. The Evidence produced this way includes claims collected about a cryptographic module, such as a Hardware Security Module (HSM), and elements found within it such as cryptographic keys. One scenario envisaged is that the state information about the cryptographic module can be securely presented to a remote operator or auditor in a vendor-agnostic verifiable format. A more complex scenario would be to submit this Evidence to a Certification Authority to aid in determining whether the storage properties of this key meet the requirements of a given certificate profile.

### Concise Selector for Endorsements and Reference Values
Draft: draft-ietf-rats-coserv · Working group: rats
Agenda: (10+5 min) Paul Howard - draft-ietf-rats-coserv
page: https://datatracker.ietf.org/doc/draft-ietf-rats-coserv/ | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
In the Remote Attestation Procedures (RATS) architecture, Verifiers require Endorsements and Reference Values to assess the trustworthiness of Attesters. This document specifies the Concise Selector for Endorsements and Reference Values (CoSERV), a structured query/result format designed to facilitate the discovery and retrieval of these artifacts from various providers. CoSERV defines a query language and corresponding result structure using CDDL, which can be serialized in CBOR format, enabling efficient interoperability across diverse systems.

### Concise Reference Integrity Manifest
Draft: draft-ietf-rats-corim · Working group: rats
Agenda: (20 min) Yogesh Deshpande - draft-ietf-rats-corim
page: https://datatracker.ietf.org/doc/draft-ietf-rats-corim/ | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
Remote Attestation Procedures (RATS) enable Relying Parties to assess the trustworthiness of a remote Attester and therefore to decide whether or not to engage in secure interactions with it. Evidence about trustworthiness can be rather complex and it is deemed unrealistic that every Relying Party is capable of the appraisal of Evidence. Therefore that burden is typically offloaded to a Verifier. In order to conduct Evidence appraisal, a Verifier requires not only fresh Evidence from an Attester, but also trusted Endorsements and Reference Values from Endorsers and Reference Value Providers, such as manufacturers, distributors, or device owners. This document specifies the information elements for representing Endorsements and Reference Values in CBOR format.

### Remote Attestation with Multiple Verifiers
Draft: draft-ietf-rats-multi-verifier · Working group: rats
Agenda: (10 min) Yogesh Despande or Jun Zhang - draft-ietf-rats-multi-verifier
page: https://datatracker.ietf.org/doc/draft-ietf-rats-multi-verifier/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-multi-verifier-progress-update-00 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
IETF RATS Architecture, defines the key role of a Verifier. In a complex system, this role needs to be performed by multiple Verifiers coordinating together to assess the full trustworthiness of an Attester. This document focuses on various topological patterns for a multiple Verifier system. It only covers the architectural aspects introduced by the Multi Verifier concept, which is neutral with regard to specific wire formats, encoding, transport mechanisms, or processing details.

### An EAT Profile for Trustworthy Device Assignment
Draft: draft-poirier-rats-eat-da · Working group: rats
Agenda: (10 + 5 min) Thomas Fossati or Henk Birkholz - draft-poirier-rats-eat-da-10
page: https://datatracker.ietf.org/doc/draft-poirier-rats-eat-da/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-eat-da-00 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
In confidential computing, device assignment (DA) is the method by which a device (e.g., network adapter, GPU), whether on-chip or behind a PCIe Root Port, is assigned to a Trusted Virtual Machine (TVM). For the TVM to trust an assigned device, the device must provide the TVM with attestation Evidence confirming its identity, the state of its firmware and configuration. Since Evidence claims can be processed by 3rd party entities (e.g., Verifiers, Relying Parties) external to the TVM, there is a need to standardize the representation of DA-related information in Evidence to ensure interoperability. This document defines an attestation Evidence format for DA as an EAT (Entity Attestation Token) profile.

### Verifiable Proof of Environment Attestation Profile
Draft: draft-lkspa-rats-verifiable-geo-fence · Working group: rats
Agenda: (5 + 5 min) Ramki Krishnen or Michael Richardson - draft-lkspa-rats-verifiable-geo-fence
page: https://datatracker.ietf.org/doc/draft-lkspa-rats-verifiable-geo-fence/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-verifiable-proof-of-environment-attestation-profile-v-pea-00 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
Operators of regulated, sovereign, and high-assurance deployments require hardware-rooted, machine-verifiable proof that a workload executes in its approved environment. Current remote attestation mechanisms address two relevant properties in isolation: platform integrity — that the hardware and software stack are in an approved, untampered state — and physical residency — that the hardware resides within an approved geographic boundary. Neither property alone is sufficient: integrity without residency permits a valid platform to operate outside approved boundaries; residency without integrity permits a compromised platform to claim valid placement. This document defines the *Verifiable Proof of Environment Attestation Profile (V-PEA)*, a profile of the RATS Architecture (RFC 9334) in which a platform binds location Claims to its own integrity Evidence in a single TPM-sealed Evidence structure (lah-bundle). V-PEA does not generate location Claims: they are produced by location sources, such as GNSS receivers, mobile network operators, or timing-based anchors, and V-PEA binds them to the particular platform that will receive a credential or key. V-PEA defines two Evidence dimensions: *WHAT* — hardware provenance (TPM Attestation Key registered and manufacturer-endorsed), platform integrity (firmware and OS state matching reference values), and workload agent software integrity (binary digest matching an approved value); and *WHERE* — physical residency within an approved geographic boundary, as reported by one or more location sources. A TPM quote seal binds WHAT and WHERE into a single unforgeable statement: neither dimension can be forged or transplanted without invalidating the other. For the WHERE dimension, V-PEA supports Transparent Zero-Knowledge Proofs (ZKPs), enabling an Attester to prove geographic compliance without disclosing precise coordinates. A positive V-PEA Attestation Result enables a Relying Party to issue hardware-rooted credentials or authorize operations — combining verified execution environment (WHAT) with verified physical placement (WHERE) — before releasing sensitive assets or granting access. Integration with workload identity systems is described in the WIMSE Integration appendix.

### Geographic Attestation Results
Draft: draft-richardson-rats-geographic-results · Working group: rats
Agenda: (5 + 5 min) Ramki Krishnen or Michael Richardson - draft-richardson-rats-geographic-results
page: https://datatracker.ietf.org/doc/draft-richardson-rats-geographic-results/ | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
Many workloads have limitations on what geography they are allowed to operate in. This is often due to a regulation that requires that the computation occur in a particular jurisdiction. There are many mechanisms by which Evidence of location may be created and then evaluated by a Verifier. No matter which mechanism is appropriate for a given situation, the result of the Verification can be expressed in a similiarly defined EAT Attestation Result. This document is about encoding a variety of geographical conclusions conclusions in an Attestation Result. In addition, one mechanism of directly creating a geographic result in the form of an Endorsement is described in an appendix.

### Privacy Framework for Remote ATtestation procedureS
Draft: draft-ounsworth-rats-privacy-framework · Working group: rats
Agenda: (5 + 5 min) Mike Ounsworth - draft-ounsworth-rats-privacy-framework
page: https://datatracker.ietf.org/doc/draft-ounsworth-rats-privacy-framework/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-rats-privacy-framework-00 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
This document extends the RATS Architecture to consider "coercive uses of RATS" where a malicious Verifier or Relying Party uses RATS protocols to extract sensitive information from an Attester or a victim Verifier that it would not otherwise be inclined to disclose. This over-disclosure can include revealing sensitive measurements, stable identifiers, device fingerprints, vendor information, or conclusions derived from Evidence. This document defines a privacy framework for Remote Attestation that identifies this threat surfaces; classifies claims produced by Attesters and Presenters; restricts sensitive Evidence disclosure to authorized Trusted Verifiers using confidentiality protection; and describes privacy- preserving Attestation Results based on data minimization, Selective Disclosure, and Zero-Knowledge Proofs.

### Evidence Encoding for HSMs
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-evidence-encoding-for-hsms-01 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### CoSERV Progress Update
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-coserv-progress-update-00 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

### CoRIM Progress Update
Presentation · Working group: rats
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-corim-progress-update-00 | video: https://youtu.be/IhxaSHCwdv0 | materials: https://datatracker.ietf.org/meeting/126/session/rats
Slides presented at the rats session; no Internet-Draft is linked to them.

## Working Group: rtgwg

### SRv6 Egress Protection in Multi-homed scenario
Draft: draft-cheng-rtgwg-srv6-multihome-egress-protection · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-srv6-multihome-egress-protection/
page: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-srv6-multihome-egress-protection/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-02-rtgwg-srv6-egress-protection-in-multi-homed-scenario-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
This document describes a SRv6 egress node protection mechanism in multi-homed scenarios.

### SRv6 Path Egress Protection
Draft: draft-ietf-rtgwg-srv6-egress-protection · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-srv6-egress-protection/
page: https://datatracker.ietf.org/doc/draft-ietf-rtgwg-srv6-egress-protection/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-03-srv6-egress-protection-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
This document describes the mechanism and operational considerations for fast protecting the egress node and link of a Segment Routing for IPv6 (SRv6) path. Topology Independent Loop-Free Alternate (TI-LFA) specifies fast protections for transit nodes and links of an SR path, but does not present protections for the egress node. The solution uses a Mirror SID (End.M) behavior to steer traffic to a protector egress upon failure of the primary egress. The Interior Gateway Protocol (IGP) (IS-IS/OSPFv3) extensions used to advertise the Mirror SID and protected locators are specified in [I-D.ietf-lsr-srv6-mirror-sid-igp-encoding]; they build on the IS-IS and OSPFv3 SRv6 extensions defined in [RFC9352] and [RFC9513].

### Unicast Support for the Virtual Router Redundancy Protocol (VRRP)
Draft: draft-abinabraham-vrrp-unicast · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-abinabraham-vrrp-unicast/
page: https://datatracker.ietf.org/doc/draft-abinabraham-vrrp-unicast/ | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
The Virtual Router Redundancy Protocol (VRRP) Version 3 as specified in RFC 9568 assumes multicast operation on a shared LAN. Some deployments require the VRRP first-hop redundancy function but cannot use multicast delivery for VRRP advertisements. This document updates RFC 9568 by defining an optional configured unicast mode for VRRP Version 3 in which advertisements are sent to configured peer addresses rather than to the VRRP multicast group. The VRRP packet format, state machine, protocol number, virtual IP semantics, and Virtual Router MAC behavior remain unchanged from RFC 9568.

### PFC PAUSE Frame Forwarded Transparently in Wide Area Networks
Draft: draft-he-rtgwg-wan-pfc · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-he-rtgwg-wan-pfc/
page: https://datatracker.ietf.org/doc/draft-he-rtgwg-wan-pfc/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-pfc-pause-frame-forwarded-transparently-in-wide-area-networks-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
This document describes a solution for transparent forwarding of PFC PAUSE frames in wide area networks, which does not require the nodes in wide area networks to support PFC flow control capabilities.

### Elastic Bandwidth-aware Routing Framework
Draft: draft-czz-rtgwg-elastic-bandwidth-routing · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/
page: https://datatracker.ietf.org/doc/draft-czz-rtgwg-elastic-bandwidth-routing/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-06-elastic-bandwidth-routing-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
IGP normally computes the shortest paths in a network for packet forwarding, without taking the traffic demands and available bandwidth into consideration. When there is a link degradation or partial link failure in a network which causes throughput reduction, or the volume of specific traffic flows increase dramatically, unexpected congestion may happen if only the shortest paths are used for IP forwarding. Conventional centralized Traffic Engineering (TE) focuses on long- term bandwidth and routes planning based on traffic demands, which can not react to the congestions in networks timely. This document describes a distributed path computation and load balancing mechanism named Elastic Bandwidth-aware Routing (EBR), which can alleviate congestions timely before TE finishes the global optimization. It allows IGP-enabled nodes which face congestion to distribute traffic among the shortest paths and load-balancing alternate paths through Segment Routing (SR) strict path, with weights determined based on the bandwidth utilization and available bandwidth of these paths. It provides an efficient, accurate and backward compatible approach for dynamic link congestion avoidance.

### GSE architecture for AIDC
Draft: draft-zhuang-rtgwg-aidc-gse-architecture · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-zhuang-rtgwg-aidc-gse-architecture/
page: https://datatracker.ietf.org/doc/draft-zhuang-rtgwg-aidc-gse-architecture/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-07-gse-architecture-for-aidc-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
This document introduces a Global Scheduling Ethernet (GSE) architecture for data centers used for AI computing. This architecture can minimize the probability of packet forwarding congestion in the network and improve the efficiency of packet interaction.

### Enhanced ECMP for AI Cluster
Draft: draft-cheng-rtgwg-enhanced-ecmp · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/
page: https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-08-enhanced-ecmp-for-ai-cluster-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
In AI training scenarios, the current mainstream load balancing technology is per-flow ECMP. However, hash collision issues lead to imbalanced traffic distribution, adversely affecting application performance. To address this problem, this document proposes an enhanced ECMP method that resolves load imbalance caused by hash collisions. The proposed solution effectively improves load balancing efficiency, reduces network congestion, and enhances overall network performance.

### Distributed Inference Network (DIN) Problem Statement, Use Cases, and Requirements
Draft: draft-song-rtgwg-din-usecases-requirements · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/draft-song-rtgwg-din-usecases-requirements/
page: https://datatracker.ietf.org/doc/draft-song-rtgwg-din-usecases-requirements/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-09-din-problem-statement-use-cases-and-requirements-00 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
This document describes the problem statement, use cases, and requirements for a "Distributed Inference Network" (DIN) in the era of pervasive AI. As AI inference services become widely deployed and accessed by billions of users, applications and devices, traditional centralized cloud-based inference architectures face challenges in scalability, latency, security, and efficiency. DIN aims to address these challenges by leveraging distributed edge-cloud collaboration, intelligent scheduling, and enhanced network security to support low- latency, high-concurrency, and secure AI inference services.

### Geographic Based Dynamic Routing in LEO Satellite Networks
Draft: draft-yang-rtgwg-grc-based-routing · Working group: rtgwg
Agenda: https://datatracker.ietf.org/doc/html/draft-yang-rtgwg-grc-based-routing-01
page: https://datatracker.ietf.org/doc/draft-yang-rtgwg-grc-based-routing/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-10-geographic-based-dynamic-routing-in-leo-satellite-networks-01 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
This document proposes a dynamic routing mechanism for Low Earth Orbit(LEO) satellite networks based on geographic region coding. By decoupling IP addressing from physical location, the mechanism uses hierarchical geographic grid codes (inspired by Uber's H3 spatial index) as temporary IP addresses for satellites. Routing decisions are made based on the relative geographic position encoded in the destination address, rather than traditional prefix-based IP routing. Satellite ephemeris data is leveraged to pre-compute routing tables for discrete time slices, eliminating the need for real-time link- state flooding and enabling stable, predictable routing in highly dynamic satellite topologies.

### Unicast VRRP
Presentation · Working group: rtgwg
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-03-unicast-vrrp-01 | video: https://youtu.be/0lOx_vRs1no | materials: https://datatracker.ietf.org/meeting/126/session/rtgwg
Slides presented at the rtgwg session; no Internet-Draft is linked to them.

## Working Group: savnet

### Provider Interface SAV for Customer Cone Sources
Draft: draft-huang-savnet-pi-sav-for-cc · Working group: savnet
Agenda: Draft link: draft-huang-savnet-pi-sav-for-cc-02
page: https://datatracker.ietf.org/doc/draft-huang-savnet-pi-sav-for-cc/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-updates-on-pi-sav-for-cc-01 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
Current source address validation (SAV) on an AS's provider interfaces mainly relies on loose uRPF, which cannot defend against IP spoofing using routable prefixes and is ineffective when a default route is present. This document describes a *framework* for provider interface source address validation against spoofing of customer cone source prefixes (PI-SAV for CC). Two architectural approaches are presented: * *PI-SAV for Standalone CC*: a static solution that builds a blocklist based on topology information from BGP RIBs, RPKI ASPA, and local configuration (SLURM) etc. It requires no inter-AS communication. * *PI-SAV for Standalone+ CC*: an enhanced solution that uses lightweight query-response coordination between the top AS and member ASes to identify sub-cones that do not actually cause traffic detours, thereby enlarging the effective blocklist. This document is *informational* and provides only the framework, conceptual procedures, and requirements for future protocol specifications. Detailed wire protocols (e.g., for partial transit information provisioning or for query-response messaging) are out of scope and will be defined in separate documents.

### Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)
Draft: draft-ietf-sidrops-bar-sav · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-sidrops-bar-sav/
page: https://datatracker.ietf.org/doc/draft-ietf-sidrops-bar-sav/ | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
Designing an efficient source address validation (SAV) filter requires minimizing false positives (i.e., avoiding blocking legitimate traffic) while maintaining directionality (see RFC8704). This document advances the technology for SAV filter design through a method that makes use of BGP UPDATE messages, Autonomous System Provider Authorization (ASPA), and Route Origin Authorization (ROA). The proposed method's name is abbreviated as BAR-SAV. BAR-SAV can be used by network operators to derive more robust SAV filters and thus improve network resilience. This document updates RFC8704.

### A Profile for Source Origin Authorization (SOA) Service Profiles
Draft: draft-ren-sidrops-soa-profile · Working group: savnet
Agenda: •https://datatracker.ietf.org/doc/draft-ren-sidrops-soa-profile/
page: https://datatracker.ietf.org/doc/draft-ren-sidrops-soa-profile/ | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
This document defines Source Origin Authorization (SOA), a new object in the Resource Public Key Infrastructure (RPKI), for publishing an AS-level service profile used by inter-AS source address protection services. An SOA object is a digitally signed artifact that carries the publisher AS, its service role, a service descriptor, and the bootstrap information needed to authenticate a private synchronization channel, such as an endpoint address, an optional port, an optional protocol identifier, and a public key. An SOA does not itself create a subscriber-provider service relation, authorize arbitrary protected prefixes, or carry legitimate predecessor AS sets. A concrete service relation is established only after discovery, bilateral request validation, and provider acceptance. Routing-dependent data and subsequent updates are exchanged over the authenticated private channel rather than being stored in the RPKI repository.

### Source Address Validation Using Source Origin Authorizations (SOAs)
Draft: draft-ren-sidrops-soa-usage · Working group: savnet
Agenda: •https://datatracker.ietf.org/doc/draft-ren-sidrops-soa-usage/
page: https://datatracker.ietf.org/doc/draft-ren-sidrops-soa-usage/ | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
Given that an AS collaboration scheme for inter-domain source address validation requires an information-sharing platform, this document proposes a two-tier approach. In the first tier, Resource Public Key Infrastructure (RPKI) is used for service discovery, identity authentication, and transmission of the minimum bootstrap information needed to establish a private channel. Source Origin Authorization (SOA) is a newly defined cryptographically signed AS-level service- profile object for that purpose. Subscribers and providers each publish their own SOA profiles; a concrete service relation exists only after discovery, bilateral request validation, and provider acceptance. In the second tier, the legitimate predecessor AS information and its subsequent updates are exchanged over the authenticated private channel, by default using TLS[RFC8446] carrying CBOR[RFC8949]-encoded logical messages, enabling other ASes to collaboratively filter spoofed traffic while avoiding frequent routing-driven updates to RPKI and reducing exposure of subscriber- specific routing data. This revision also describes a logical synchronization state model, evidence-tagged authorization state, and fail-open handling for unavailable synchronized state, while leaving private-channel wire encoding to future specifications or bilateral deployment profiles.

### Inter-domain Source Address Validation based on AS relationships
Draft: draft-rly-savnet-inter-domain-as-relationships · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-rly-savnet-inter-domain-as-relationships/
page: https://datatracker.ietf.org/doc/draft-rly-savnet-inter-domain-as-relationships/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-updates-on-inter-domain-source-address-validation-based-on-as-relationships-00 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
This draft introduces a distributed inter-domain source address validation scheme based on AS relationships named AS Relationship Based Inter-domain Filtering (ARBIF). It primarily describes this method from seven aspects: a brief introduction to the scheme, an overview of the AS relationship classification and acquisition methods, the architecture of the ARBIF system, implementation based on BGP extension, typical use cases, experiments of ARBIF, and considerations for deployability.

### Source Prefix Advertisement for Inter-domain SAVNET
Draft: draft-geng-savnet-inter-domain-spa · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-geng-savnet-inter-domain-spa/
page: https://datatracker.ietf.org/doc/draft-geng-savnet-inter-domain-spa/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-source-prefix-advertisement-spa-for-inter-domain-savnet-01 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
This document proposes a mechanism that enables a Source AS to actively advertise their locally observed Customer Cone and prefix information to the adjacent Validating AS via a new inter-domain message called Source Prefix Advertisement (SPA). The Validating AS then combines this SPA-carried information with local source address validation-related information to construct more accurate prefix allowlists for interfaces connected to Source ASes.

### Intra-domain Source Address Validation Architecture
Draft: draft-ietf-savnet-intra-domain-architecture · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/
page: https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-update-on-intra-domain-source-address-validation-architecture-00 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
This document describes a generic architecture for intra-domain Source Address Validation (SAV). It provides a common framework for developing new intra-domain SAV mechanisms and describes the conditions under which this architecture can improve SAV accuracy and operational efficiency with respect to existing intra-domain SAV mechanisms.

### Information Requirements for Monitoring Source Address Validation (SAV) Enforcement
Draft: draft-qin-savnet-sav-monitoring-requirements · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-qin-savnet-sav-monitoring-requirements/
page: https://datatracker.ietf.org/doc/draft-qin-savnet-sav-monitoring-requirements/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-information-requirements-for-monitoring-source-address-validation-enforcement-00 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
Source Address Validation (SAV) enforcement requires operational visibility into validation results, traffic-handling outcomes, SAV rule generation and state, and SAV configuration. Such visibility helps operators understand how SAV operates in the network and supports operational decisions, including staged deployment where traffic that fails validation may be permitted while being monitored and analyzed. This document identifies information requirements for monitoring SAV enforcement.

### ICMP Extension for SAVNET Validation
Draft: draft-yl-savnet-icmp-extension · Working group: savnet
Agenda: Draft link: https://datatracker.ietf.org/doc/draft-yl-savnet-icmp-extension/
page: https://datatracker.ietf.org/doc/draft-yl-savnet-icmp-extension/ | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
This document defines new ICMP and ICMPv6 error codes to send error messages to the source device when forwarding Ping or Traceroute packets is dropped due to SAVNET validation failure. The error message explicitly states the reason for dropping as "SAVNET Validation Failed," thereby enhancing network observability and troubleshooting capabilities.

### Update on the BAR-SAV Draft
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-update-on-the-bar-sav-draft-01 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

### Using SOAs to Bootstrap Inter-AS Source Address Protection Services
Presentation · Working group: savnet
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-savnet-using-soas-to-bootstrap-inter-as-source-address-protection-services-01 | video: https://youtu.be/Nz_BBF58YWE | materials: https://datatracker.ietf.org/meeting/126/session/savnet
Slides presented at the savnet session; no Internet-Draft is linked to them.

## Working Group: scitt

### IETF 126 Supply Chain Integrity Transparency and Trust Vienna (slides-126-scitt-ietf-126-supply-chain-integrity-transparency-and-trust-vienna)
Presentation · Working group: scitt
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-scitt-ietf-126-vienna-scitt-04 | video: https://youtu.be/zvTPgrObh5Q | materials: https://datatracker.ietf.org/meeting/126/session/scitt
Slides presented at the scitt session; no Internet-Draft is linked to them.

## Working Group: spice

### GLobal Unique Enterprise (GLUE) Identifiers
Draft: draft-ietf-spice-glue-id · Working group: spice
Agenda: GLobal Unique Enterprise (GLUE) Identifiers draft-ietf-spice-glue-id (Brent Zundel) - 40 minutes
page: https://datatracker.ietf.org/doc/draft-ietf-spice-glue-id/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spice-global-unique-enterprise-glue-identifiers-00 | video: https://youtu.be/9faaBsrPT0k | materials: https://datatracker.ietf.org/meeting/126/session/spice
This specification establishes a URI scheme for GLobal Unique Enterprise (GLUE) Identifiers. This enables URI identifiers to be used for businesses and organizations. It enables organizational identities from existing authorities to be represented within this URI scheme.

### Selective Disclosure CBOR Web Tokens (SD-CWT)
Draft: draft-ietf-spice-sd-cwt · Working group: spice
Agenda: SPICE SD-CWT draft-ietf-spice-sd-cwt (Rohan Mahy/Henk Birkholz) - 15 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spice-update-on-sd-cwt-00 | video: https://youtu.be/9faaBsrPT0k | materials: https://datatracker.ietf.org/meeting/126/session/spice
This specification describes a data minimization technique for use with CBOR Web Tokens (CWTs). The approach is inspired by the Selective Disclosure JSON Web Token (SD-JWT), with changes to align with CBOR Object Signing and Encryption (COSE) and CWTs.

### OpenID Connect Standard Claims Registration for CBOR Web Tokens
Draft: draft-ietf-spice-oidc-cwt · Working group: spice
Agenda: OIDC-CWT Status draft-ietf-spice-oidc-cwt (Mike Jones) - 5 min
page: https://datatracker.ietf.org/doc/draft-ietf-spice-oidc-cwt/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spice-openid-connect-standard-claims-registration-for-cbor-web-tokens-00 | video: https://youtu.be/9faaBsrPT0k | materials: https://datatracker.ietf.org/meeting/126/session/spice
This document registers OpenID Connect standard claims already used in JSON Web Tokens for use in CBOR Web Tokens.

### A reference architecture for direct presentation credential flows
Draft: draft-johansson-direct-presentation-arch · Working group: spice
Agenda: Call for adoption: "A reference architecture for direct presentation credential flows' draft-johansson-direct-presentation-arch (Brent Zundel) - 20 min
page: https://datatracker.ietf.org/doc/draft-johansson-direct-presentation-arch/ | video: https://youtu.be/9faaBsrPT0k | materials: https://datatracker.ietf.org/meeting/126/session/spice
This document defines a reference architecture for direct presentation flows of digital credentials. The architecture introduces the concept of a presentation mediator as the active component responsible for managing, presenting, and selectively disclosing credentials while preserving a set of security and privacy promises that will also be defined. Discussion Venues This note is to be removed before publishing as an RFC. Source for this draft and an issue tracker can be found at https://github.com/leifj/wallet-refarch.

### SPICE Architecture IETF 126
Presentation · Working group: spice
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spice-spice-architecture-ietf-126-00 | video: https://youtu.be/9faaBsrPT0k | materials: https://datatracker.ietf.org/meeting/126/session/spice
Slides presented at the spice session; no Internet-Draft is linked to them.

## Working Group: spring

### SRv6 for Redundancy Protection
Draft: draft-ietf-spring-sr-redundancy-protection · Working group: spring
Agenda: draft-ietf-spring-sr-redundancy-protection
page: https://datatracker.ietf.org/doc/draft-ietf-spring-sr-redundancy-protection/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-srv6-for-redundancy-protection-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
Redundancy Protection is a generalized protection mechanism to achieve high reliability for services provided in Segment Routing networks. The mechanism uses the "Live-Live" methodology, i.e., multiple copies of the data packets are sent on different paths to provide protection. This document introduces one new SRv6 Segment Endpoint Behavior, the associated Headend Encapsulation Behaviors and the associated Redundancy Policy to provide replication and elimination functions on specific network nodes by leveraging SRv6 Network Programming capabilities.

### Segment Routing Policy Extension for Network Resource Partition
Draft: draft-ietf-spring-sr-policy-nrp · Working group: spring
Agenda: draft-ietf-spring-sr-policy-nrp
page: https://datatracker.ietf.org/doc/draft-ietf-spring-sr-policy-nrp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-segment-routing-policy-extension-for-network-resource-partition-slides-126-draft-ietf-spring-sr-policy-nrp-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
Segment Routing (SR) Policy is a set of candidate paths, each consisting of one or more segment lists and the associated information. A Network Resource Partition (NRP), is a subset of the resources and associated policies in the underlay network. In SR networks with multiple NRPs, an SR Policy can be associated with a particular NRP. In that case, SR Policy can be used for steering and forwarding traffic which is mapped to the NRP, so that the packets can be processed with the subset of network resources and policy of the NRP for guaranteed performance. Thus the association between SR Policy and NRP needs to be specified. This document defines extensions to the SR Policy Architecture to allow the association of the SR Policy candidate paths with NRPs.

### SRv6 Service Programming
Draft: draft-ietf-spring-srv6-service-programming · Working group: spring
Agenda: draft-ietf-spring-srv6-service-programming
page: https://datatracker.ietf.org/doc/draft-ietf-spring-srv6-service-programming/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-draft-ietf-spring-srv6-service-programming-00-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
This document defines data plane functionality required to implement service segments and achieve service programming in SRv6 networks.

### SID as source address in SRv6
Draft: draft-yang-spring-sid-as-source-address · Working group: spring
Agenda: draft-yang-spring-sid-as-source-address
page: https://datatracker.ietf.org/doc/draft-yang-spring-sid-as-source-address/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-sid-as-source-address-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. Both the carrier market and the enterprise market are adopting SRv6 for end-to-end service delivery. However, if a firewall exists along an SRv6 path, not only legitimate SRv6 traffic but also ICMP packets generated on SRv6 transit node will be dropped. This proposal addresses this issue by using SID as source address in SRv6 packets.

### Multipath Traffic Engineering for Segment Routing
Draft: draft-stone-spring-mpte-sr · Working group: spring
Agenda: draft-stone-spring-mpte-sr
page: https://datatracker.ietf.org/doc/draft-stone-spring-mpte-sr/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-multipath-traffic-engineering-for-segment-routing-01 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
This document describes a mechanism to achieve Multipath Traffic Engineering for Segment Routing based networks. Discussion Venues This note is to be removed before publishing as an RFC. Discussion of this document takes place on the Source Packet Routing in Networking Working Group mailing list (spring@ietf.org), which is archived at https://mailarchive.ietf.org/arch/browse/spring/. Source for this draft and an issue tracker can be found at https://github.com/astone282/draft-stone-spring-mpte-sr.

### SRv6 BSID with Notification Message Relay
Draft: draft-liu-spring-srv6-bsid-relay · Working group: spring
Agenda: draft-liu-spring-srv6-bsid-relay
page: https://datatracker.ietf.org/doc/draft-liu-spring-srv6-bsid-relay/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-srv6-bsid-with-notification-message-relay-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
This document defines a new SRv6 Endpoint behavior, End.B6.Encaps.Relay, for Binding SID (BSID) nodes in SRv6 networks. The behavior enables BSID nodes to relay tunnel-internal notification messages, such as ICMPv6 errors and congestion notifications, back to the upstream tunnel source node through a mapping mechanism.

### SRv6 Path Verification
Draft: draft-yang-spring-srv6-verification · Working group: spring
Agenda: draft-yang-spring-srv6-verification
page: https://datatracker.ietf.org/doc/draft-yang-spring-srv6-verification/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-srv6-path-verification-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
SRv6 is being rapidly deployed and is currently primarily used in trusted-domain backbone networks. However, we have also observed that SRv6 is beginning to extend toward customer site devices, e.g., SD-WAN and enterprise network deployments. Both of the scenarios can be deployed in third-party clouds or at customer sites. This introduces certain security risks, such as packet injection and path manipulation attacks. Section 6 of [I-D.draft-ietf-spring-srv6-security] identifies these risks as well, including Section 6.2.1 on Modification Attacks and Section 6.2.3 on Packet Insertion. This proposal mitigates these risks by enhancing the HMAC mechanism defined in [RFC8754].

### SRv6 behavior extention for Flow Control in WAN
Draft: draft-ruan-spring-priority-flow-control-sid · Working group: spring
Agenda: draft-ruan-spring-priority-flow-control-sid
page: https://datatracker.ietf.org/doc/draft-ruan-spring-priority-flow-control-sid/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-srv6-behavior-extension-for-flow-control-in-wan-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
In the wake of the continuous emergence of novel AI technologies, including collaborative training, distributed inference and the like, the scenario in which different data centers communicate via the RDMA (Remote Direct Memory Access) protocol has emerged as a new requirement. similar to data center networks, wide area networks (WANs) should also be equipped with certain flow control capabilities, nodes in the wide area network (WAN) need to quickly and accurately notify upstream traffic nodes of their congestion status. Upon receiving the congestion notification, upstream nodes can take responsive actions to mitigate network congestion. By extending SRv6[RFC 8986] technology, specific services can be carried over SRv6 policies, which enables the precise delivery and response of congestion signals. For traffic carried over SRv6 policies, the service traffic path is explicitly orchestrated via the Segment List in the SRH header. By parsing the sequence of the Segment List, downstream nodes or controllers can accurately identify the upstream nodes and interfaces corresponding to the current traffic, thus enabling the rapid notification of congestion information to the upstream. Since each SID in the Segment List is a 128-bit IPv6 address that represents a specific behaviour (e.g., End, End.X), extending existing behaviours to mark their capability to receive and process congestion signals allows flexible control over the delivery mode of congestion signals in the WAN. The specific packet formats and contents of congestion signals vary in various ways and are continuously being updated. This document takes the most commonly used PFC backpressure notification mechanism as an example to elaborate on the overall workflow of WAN congestion information notification and the extensions to the SRv6 protocol. PFC technology is widely deployed in RoCEv2 networks within data centers to report congestion signals. By leveraging SRv6 and NRP technologies, it is possible to effectively control the propagation range and path of PFC backpressure signals in wide area networks, thereby avoiding issues such as deadlocks and the excessive propagation of congestion scope.

### SRv6 for PPPoE Transport
Draft: draft-huang-spring-pppoe-srv6 · Working group: spring
Agenda: draft-huang-spring-pppoe-srv6
page: https://datatracker.ietf.org/doc/draft-huang-spring-pppoe-srv6/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-srv6-for-pppoe-transport-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
This document proposes a method that employs SRv6 underlay tunnel to transport PPPoE session information across broadband networks. By leveraging the programmability of SRv6 SIDs, the approach not only delivers trusted authentication and secure subscriber access, but also enables operators to offer differentiated services and flexibly instantiate network functions for broadband users.

### draft-varhal draft-ali ICMP Error Handling in SRv6-based VPNs combine presentation
Presentation · Working group: spring
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-draft-varhal-draft-ali-icmp-error-handling-in-srv6-based-vpns-combine-presentation-00 | video: https://youtu.be/3ui3EfTTLkA | materials: https://datatracker.ietf.org/meeting/126/session/spring
Slides presented at the spring session; no Internet-Draft is linked to them.

## Working Group: srv6ops

### SRv6 Deployment and Operation Problem Summary
Draft: draft-ietf-srv6ops-problem-summary · Working group: srv6ops
Agenda: draft-ietf-srv6ops-problem-summary
page: https://datatracker.ietf.org/doc/draft-ietf-srv6ops-problem-summary/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-srv6-deployment-and-operation-problem-summary-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
This document aims to provide a concise overview of the common problems encountered during SRv6 deployment and operation, which provides foundations for further work, including for example of potential solutions and best practices to navigate deployment.

### Addressing Recommendations for SRv6
Draft: draft-horn-srv6ops-srv6addressing · Working group: srv6ops
Agenda: draft-horn-srv6ops-srv6addressing
page: https://datatracker.ietf.org/doc/draft-horn-srv6ops-srv6addressing/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-33-addressing-recommendations-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
This document provides recommendations for addressing SRv6 locators format. It introduces concepts of Blocks, Sets, and Node IDs, and explains how summarization boundaries and flexible algorithm support can be implemented for both small and large networks.

### SRv6 for Deterministic Path Placement in AI Backends
Draft: draft-filsfils-srv6ops-srv6-ai-backend · Working group: srv6ops
Agenda: draft-filsfils-srv6ops-srv6-ai-backend
page: https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-34-srv6-in-ai-backend-01 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
This document describes how SRv6 NEXT-CSID enables deterministic path placement in AI backend fabrics through L3-L4 integration on end hosts: the transport stack on the NIC encodes each path as an ordered list of segments (a NEXT-CSID network program) in the packet header, while the fabric forwards statelessly. It explains operational benefits including deterministic probing and alignment with hyperscale production deployments.

### SRv6 End-to-End DC Frontend and WAN
Draft: draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan · Working group: srv6ops
Agenda: draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan
page: https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-e2e-dc-frontend-wan/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-35-srv6-in-end-to-end-dc-frontend-01 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
The SRv6 Network Programming architecture allows an application to control the end-to-end journey of traffic flows through different network domains in a unified and stateless manner, without requiring intermediate network devices to maintain per-flow information. This document covers its application to the integration of data center (DC) and wide area network (WAN) architectures using SRv6 with uSID (NEXT-CSID). It describes a unified IPv6 data plane from tenant workloads through the DC frontend to Internet peering, replacing designs that stitch separate overlay protocols at the Data Center Interconnect (DCI). The solution enhances scalability and enables flexible stateless service insertion by unifying underlay, overlay, and service steering under SRv6.

### SRv6 Service Function Chaining Deployment
Draft: draft-watal-srv6ops-srv6-sfc-deployment · Working group: srv6ops
Agenda: draft-watal-srv6ops-srv6-sfc-deployment
page: https://datatracker.ietf.org/doc/draft-watal-srv6ops-srv6-sfc-deployment/ | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
This document describes the deployment and operational experience of the SRv6 Service Function Chaining (SFC) architecture defined in [I-D.draft-watal-spring-srv6-sfc-sr-aware-functions] on an academic IPv6 backbone network. The deployed system integrates SRv6 forwarding, service function management, topology collection, path computation, and flow classification to enable dynamic provisioning of SFC services via a web-based management interface. This document summarizes the deployment architecture, operational workflow, experience, and lessons learned, and provides guidance for network operators deploying SRv6 SFC services.

### ESP Protection for Services over SRv6
Draft: draft-wdh-srv6ops-secservice · Working group: srv6ops
Agenda: draft-wdh-srv6ops-secservice
page: https://datatracker.ietf.org/doc/draft-wdh-srv6ops-secservice/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-37-esp-protection-for-services-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
This document describes a mechanism for protecting selected service traffic using IPsec ESP while transporting the traffic over an SRv6 domain. The approach enables service payloads to be encrypted prior to SRv6 encapsulation, allowing the SRv6 header to remain visible for segment-based forwarding within the provider network. This mechanism supports services or applications that require additional confidentiality and integrity protection, even when carried over an operator-managed SRv6 domain.

### Introduction
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-1-introduction-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### DT Road towards SRv6
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-21-dt-road-towards-srv6-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Practices for Migrating MPLS Networks to SRv6
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-22-practices-for-migrating-mpls-networks-to-srv6-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SRv6 @ SONiC
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-23-srv6-sonic-01 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### Deployment Options
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-srv6-deployment-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

### SFC Deployments
Presentation · Working group: srv6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-36-sfc-deployments-00 | video: https://youtu.be/kxTId7do_y4 | materials: https://datatracker.ietf.org/meeting/126/session/srv6ops
Slides presented at the srv6ops session; no Internet-Draft is linked to them.

## Working Group: tcpm

### TCP ACK Rate Request Option
Draft: draft-ietf-tcpm-ack-rate-request · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-ack-rate-request-12
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-ack-rate-request/ | video: https://youtu.be/pS7dKMeaHeE | materials: https://datatracker.ietf.org/meeting/126/session/tcpm
TCP Delayed Acknowledgments (ACKs) is a widely deployed mechanism that allows reducing protocol overhead in many scenarios. However, Delayed ACKs may also contribute to suboptimal performance. When a relatively large congestion window (cwnd) can be used, less frequent ACKs may be desirable. On the other hand, in relatively small cwnd scenarios, eliciting an immediate ACK may avoid unnecessary delays that may be incurred by the Delayed ACKs mechanism. This document specifies the TCP ACK Rate Request (TARR) option. This option allows a sender to request the ACK rate to be used by a receiver, and it also allows to request immediate ACKs from a receiver.

### Cryptographic Algorithms That Produce 128-bit MACs For Use With TCP-AO
Draft: draft-ietf-tcpm-tcp-ao-algs · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-ietf-tcpm-tcp-ao-algs-05
page: https://datatracker.ietf.org/doc/draft-ietf-tcpm-tcp-ao-algs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tcpm-additional-cryptographic-algorithms-for-tcp-ao-00 | video: https://youtu.be/pS7dKMeaHeE | materials: https://datatracker.ietf.org/meeting/126/session/tcpm
RFC 5926 established a registry of cryptographic algorithms that can be used with TCP-AO. This document expands that registry, adding two Message Authentication Code (MAC) algorithms, HMAC-SHA256-128 and KMAC256-128. For each MAC algorithm, a corresponding Key Derivation Function (KDF) is also added. The MAC algorithms described by this document produce 128-bit (i.e., 16-byte) MACs. When 16-byte MACs are encoded in TCP-AO, the TCP-AO consumes 20 of the 40 bytes available for TCP options.

### Cryptographic Algorithms That Produce 256-bit MACs For Use With TCP-AO
Draft: draft-bonica-tcpm-tcp-ao-long-algs · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-bonica-tcpm-tcp-ao-long-algs-04
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-tcp-ao-long-algs/ | video: https://youtu.be/pS7dKMeaHeE | materials: https://datatracker.ietf.org/meeting/126/session/tcpm
RFC5926 creates a registry of cryptographic algorithms that can be used with TCP-AO. This document expands that registry, adding two Message Authentication Code (MAC) algorithms, HMAC-SHA256 and KMAC256. The MAC algorithms described by this document produce 256-bit (i.e., 32-byte) MACs. When 32-byte MACs are encoded in TCP-AO, the TCP-AO consumes 36 of the 40 bytes available for TCP options.

### An Upgraded TCP Session Type
Draft: draft-bonica-tcpm-extended-options · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-bonica-tcpm-extended-options-04
page: https://datatracker.ietf.org/doc/draft-bonica-tcpm-extended-options/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tcpm-tcp-extended-options-01 | video: https://youtu.be/pS7dKMeaHeE | materials: https://datatracker.ietf.org/meeting/126/session/tcpm
Currently, TCP maintains ordinary sessions (SES-O) in which ordinary segments (SEG-O) are exchanged. Each SEG-O can accommodate up to 40 octets of options. In the future, applications may require more than 40 octets of options. For example, an application may use a 36-byte TCP Authentication Option (TCP-AO), leaving insufficient space for other required options. Therefore, this document describes an experiment in which upgraded sessions (SES-U) and upgraded segments (SEG-U) are introduced. Each SEG-U can accommodate up to 1,016 octets of Individual Options.

### TCP Packet Trimming Extension
Draft: draft-mazilu-tcpm-packet-trimming · Working group: tcpm
Agenda: https://datatracker.ietf.org/doc/html/draft-mazilu-tcpm-packet-trimming-00
page: https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tcpm-tcp-packet-trimming-slides-126-tcpm-packet-trimming-00 | video: https://youtu.be/pS7dKMeaHeE | materials: https://datatracker.ietf.org/meeting/126/session/tcpm
This document specifies a TCP extension that enables TCP endpoints in data center networks or similarly controlled administrative domains to use packet trimming information when it is available. When switch buffers exceed a threshold, rather than silently dropping a packet, the switch trims the payload and forwards the header. This allows the destination to issue a deterministic Negative Acknowledgment (NACK), enabling faster, more deterministic loss recovery.

### tarr
Presentation · Working group: tcpm
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tcpm-tarr-01 | video: https://youtu.be/pS7dKMeaHeE | materials: https://datatracker.ietf.org/meeting/126/session/tcpm
Slides presented at the tcpm session; no Internet-Draft is linked to them.

## Working Group: tls

### The Datagram Transport Layer Security (DTLS) Protocol Version 1.3
Draft: draft-ietf-tls-rfc9147bis · Working group: tls
Agenda: draft-ietf-tls-rfc9147bis
page: https://datatracker.ietf.org/doc/draft-ietf-tls-rfc9147bis/ | materials: https://datatracker.ietf.org/meeting/126/session/tls
This document specifies version 1.3 of the Datagram Transport Layer Security (DTLS) protocol. DTLS 1.3 allows client/server applications to communicate over the Internet in a way that is designed to prevent eavesdropping, tampering, and message forgery. The DTLS 1.3 protocol is based on the Transport Layer Security (TLS) 1.3 protocol and provides equivalent security guarantees with the exception of order protection / non-replayability. Datagram semantics of the underlying transport are preserved by the DTLS protocol. This document obsoletes RFC 6347.

### Authenticated ECH Config Distribution and Rotation
Draft: draft-sullivan-tls-signed-ech-updates · Working group: tls
Agenda: draft-sullivan-tls-signed-ech-updates
page: https://datatracker.ietf.org/doc/draft-sullivan-tls-signed-ech-updates/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessa-authenticated-ech-config-distribution-and-rotation-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Encrypted ClientHello (ECH) requires clients to have the server's ECH configuration before connecting. Currently, when ECH fails, servers can send updated configurations but clients cannot authenticate them unless the server has a valid certificate for the public name, limiting deployment flexibility. This document specifies a new mechanism for authenticating ECH configurations. Servers include additional information in their initial ECH configurations, which enables clients to authenticate updated configurations without relying on a valid certificate for the public name.

### Workload Identifier Origin Hint for TLS ClientHello
Draft: draft-rosomakho-tls-wimse-cert-hint · Working group: tls
Agenda: draft-rosomakho-tls-wimse-cert-hint
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessa-workload-identifier-scope-hint-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
This document defines a TLS extension that allows clients to indicate one or more workload identifier origins in the ClientHello message. Each origin consists of a URI scheme and trust domain component, representing the administrative domain and identifier namespace in which the client operates. These identifier origins serve as hints to enable the server to determine whether client authentication is required and which policies or trust anchors should apply. This mechanism improves efficiency in mutual TLS deployments while minimising the exposure of sensitive identifier information. To protect confidentiality, this extension can be used in conjunction with Encrypted Client Hello (ECH).

### Supplemental Authentication in TLS 1.3
Draft: draft-rosomakho-tls-supplemental-auth · Working group: tls
Agenda: draft-rosomakho-tls-supplemental-auth
page: https://datatracker.ietf.org/doc/draft-rosomakho-tls-supplemental-auth/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessa-supplemental-authentication-in-tls-13-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
TLS 1.3 allows endpoints to authenticate using certificates during the handshake and supports optional post-handshake client authentication. However, some deployments require presenting additional certificate-based authentication statements bound to the same TLS connection, such as separate device and user identities, attestation evidence, or multiple certificate chains during cryptographic transitions. This document defines Supplemental Authentication for TLS 1.3, a mechanism that allows endpoints to present additional certificate authentication messages after the handshake while preserving the authentication semantics of TLS 1.3. Supplemental authentication reuses the existing Certificate, CertificateVerify, and Finished message structure and allows endpoints to exchange one or more additional certificate-based authentication statements before sending application data or other post-handshake TLS messages.

### PQC Continuity: Downgrade Protection for TLS Servers Migrating to PQC
Draft: draft-sheffer-tls-pqc-continuity · Working group: tls
Agenda: draft-sheffer-tls-pqc-continuity
page: https://datatracker.ietf.org/doc/draft-sheffer-tls-pqc-continuity/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessa-pqc-continuity-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
As the Internet transitions toward post-quantum cryptography (PQC), many TLS servers will continue supporting traditional certificates to maintain compatibility with legacy clients. However, this coexistence introduces a significant vulnerability: an undetected rollback attack, where a malicious actor strips the PQC or composite certificate and forces the use of a classical certificate once quantum-capable adversaries exist. To defend against this, this document defines a TLS extension that allows a TLS client to cache a server's declared commitment to present PQC or composite certificates for a specified duration. On subsequent connections, the client enforces that cached commitment and rejects traditional-only certificates that conflict with it. This mechanism, inspired by HTTP Strict Transport Security (HSTS) but operating at the TLS layer, provides PQC downgrade protection without requiring changes to certificate authority (CA) infrastructure.

### A Password Authenticated Key Exchange Extension for TLS 1.3
Draft: draft-ietf-tls-pake · Working group: tls
Agenda: draft-ietf-tls-pake
page: https://datatracker.ietf.org/doc/draft-ietf-tls-pake/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-a-password-authenticated-key-exchange-extension-for-tls-13-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
The pre-shared key mechanism available in TLS 1.3 is not suitable for usage with low-entropy keys, such as passwords entered by users. This document describes an extension that enables the use of password-authenticated key exchange protocols with TLS 1.3.

### Post-Quantum Traditional (PQ/T) Hybrid Authentication with Dual Certificates in TLS 1.3
Draft: draft-yusef-tls-pqt-dual-certs · Working group: tls
Agenda: draft-yusef-tls-pqt-dual-certs
page: https://datatracker.ietf.org/doc/draft-yusef-tls-pqt-dual-certs/ | materials: https://datatracker.ietf.org/meeting/126/session/tls
The anticipated emergence of cryptographically relevant quantum computers (CRQCs) poses a threat to the authentication mechanisms used in TLS 1.3. This document defines a hybrid authentication mechanism that uses two independent certificates, one traditional and one post-quantum, ensuring that an attacker must break both algorithms to compromise a TLS connection. The two certificate chains are carried in a single Certificate message and two independent signatures are encoded in the CertificateVerify message.

### Use of Composite ML-DSA in TLS 1.3
Draft: draft-reddy-tls-composite-mldsa · Working group: tls
Agenda: draft-reddy-tls-composite-mldsa-10
page: https://datatracker.ietf.org/doc/draft-reddy-tls-composite-mldsa/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessb-use-of-composite-ml-dsa-in-tls-13-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Compositing the post-quantum ML-DSA signature with traditional signature algorithms provides protection against potential breaks or critical bugs in ML-DSA or the ML-DSA implementation. This document specifies how such a composite signature can be formed using ML-DSA with RSA-PKCS#1 v1.5, RSA-PSS, ECDSA, Ed25519, and Ed448 to provide authentication in TLS 1.3, including use in certificates.

### TLS 1.3 Cipher Suites with Alternative Key-Schedule Profiles
Draft: draft-sullivan-tls-xof-ciphers · Working group: tls
Agenda: draft-sullivan-tls-xof-ciphers
page: https://datatracker.ietf.org/doc/draft-sullivan-tls-xof-ciphers/ | materials: https://datatracker.ietf.org/meeting/126/session/tls
TLS 1.3 builds its key schedule on HKDF over the cipher suite's hash. This document defines TLS 1.3 cipher suites that build it on a deck function over a single permutation instead, the one a deployment already carries when it uses SHA-3, ML-KEM, or ML-DSA. One permutation then runs the whole schedule, and a full handshake takes about a third of the permutation calls an HKDF schedule over that permutation would. Such a cipher suite names an AEAD algorithm together with a schedule profile that defines every key-schedule function the connection uses. The profile follows from the negotiated cipher suite alone, so no new extension is defined and the TLS 1.3 state machine and wire format are unchanged. Two profiles are defined, one on the standard SHA-3 function and one on a faster reduced-round variant of it.

### DTLS 1.3
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-dtls-13-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Framing PQ + T Signatures for TLS
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-framing-pq-t-signatures-for-tls-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Dual Certs in TLS 1.3
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessb-dual-certs-in-tls-13-01 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### XOF-based key schedules for TLS 1.3
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessb-xof-based-key-schedules-for-tls-13-00 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

### Encrypted Client Hello (ECH) - An active measurement perspective
Presentation · Working group: tls
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-encrypted-client-hello-ech-an-active-measurement-perspective-01 | video: https://youtu.be/RO-Drvzquc4 | materials: https://datatracker.ietf.org/meeting/126/session/tls
Slides presented at the tls session; no Internet-Draft is linked to them.

## Working Group: tsvwg

### User Ports and Port Identifiers for Experiments
Draft: draft-ietf-tsvwg-usr-exp · Working group: tsvwg
Agenda: Wes Eddy: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-usr-exp/ (10)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-usr-exp/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-user-ports-and-port-identifiers-for-experiments-00 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document defines user ports for experiments using transport protocols and the use of experiment identifiers to enable shared use of these ports. It updates RFC 4727 to recommend the use of these experimental identifiers for the system ports for experiments in the same manner.

### Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-ietf-tsvwg-sctp-dtls-chunk · Working group: tsvwg
Agenda: Magnus Westerlund: draft-ietf-tsvwg-sctp-dtls-chunk-02 (15)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-sctp-dtls-chunk/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-ericssons-proposal-for-key-management-for-dtls-chunk-01 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document describes a method for adding Datagram Transport Layer Security (DTLS) based authentication and cryptographic protection to the Stream Control Transmission Protocol (SCTP). This SCTP extension is intended to enable communication privacy for applications that use SCTP as their transport protocol and allows applications to communicate in a way that is designed to prevent eavesdropping and detect tampering or message forgery. Once enabled, this also applies to the SCTP payload as well as the SCTP control information. Applications using this SCTP extension can use most of the transport features provided by SCTP and its other extensions. The use of the SCTP Authentication extension defined in RFC 4895 is incompatible with the extension defined in this document but would not provide any additional service. This implies that the Dynamic Address Reconfiguration as specified in RFC 5061 can only be used as described in this document. This document obsoletes RFC 6083 and updates RFC 5061.

### Transport Layer Security (TLS) based Key Management of the Stream Control Transmission Protocol (SCTP) DTLS Chunk
Draft: draft-porfiri-tsvwg-sctp-dtls-handshake · Working group: tsvwg
Agenda: Magnus Westerlund: https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/ (15)
page: https://datatracker.ietf.org/doc/draft-porfiri-tsvwg-sctp-dtls-handshake/ | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document defines how Transport Layer Security (TLS) 1.3 is used as a key management method for the SCTP DTLS Chunk mechanism. It specifies how a TLS handshake establishes the initial security context for an SCTP association and how subsequent TLS handshakes provide key updates and re-authentication. The goal is to enable authenticated and confidential communication over SCTP using the DTLS Chunk, leveraging standardized TLS 1.3 features for key management and rekeying.

### Flow Queue PIE: A Hybrid Packet Scheduler and Active Queue Management Algorithm
Draft: draft-ietf-tsvwg-fq-pie · Working group: tsvwg
Agenda: Mohit Tahiliani: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/ (10)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-fq-pie/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-fq-pie-01 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document presents Flow Queue Proportional Integral controller Enhanced (FQ-PIE), a hybrid packet scheduler and Active Queue Management (AQM) algorithm to isolate flows and tackle the problem of bufferbloat. FQ-PIE uses hashing to classify incoming packets into different queues and provide flow isolation. Packets are dequeued by using a variant of the round robin scheduler. Each such flow is managed by the PIE algorithm to maintain high link utilization while controlling the queue delay to a target value.

### Operational Guidance on Coexistence with Classic ECN during L4S Deployment
Draft: draft-ietf-tsvwg-l4sops · Working group: tsvwg
Agenda: Greg White: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/ (10)
page: https://datatracker.ietf.org/doc/draft-ietf-tsvwg-l4sops/ | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document provides guidance in order to ensure successful deployment of Low Latency Low Loss Scalable throughput (L4S) in the Internet. Other L4S documents provide guidance for running an L4S experiment, but this document is focused solely on potential interactions between L4S flows and flows using the original ('Classic') ECN over a Classic ECN bottleneck. The document discusses the potential outcomes of these interactions, describes mechanisms to detect the presence of Classic ECN bottlenecks, and identifies opportunities to prevent and/or detect and resolve fairness problems in such networks. This guidance is aimed at operators of end-systems, operators of networks, and researchers.

### SCTP Negotiation Acceleration Protocol
Draft: draft-hancke-tsvwg-snap · Working group: tsvwg
Agenda: Phillip Hancke: https://datatracker.ietf.org/doc/draft-hancke-tsvwg-snap/ (10)
page: https://datatracker.ietf.org/doc/draft-hancke-tsvwg-snap/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-sctp-negotiation-acceleration-protocol-for-webrtc-00 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
WebRTC Data Channels use the Stream Control Transmission Protocol (SCTP) over a Datagram Transport Layer Security (DTLS) association. The standard SCTP connection establishment requires a handshake that introduces latency. This document specifies a method to accelerate the datachannel establishment by embedding the SCTP initialization parameters within the Session Description Protocol (SDP) offer/answer exchange. This reduces the time required to open a data channel by up to two network round-trip times.

### Best Practices for L4S implementation for Mobile Devices
Draft: draft-sporeba-tsvwg-mobile-l4s · Working group: tsvwg
Agenda: Sebastian Poreba: https://datatracker.ietf.org/doc/draft-sporeba-tsvwg-mobile-l4s/ (10)
page: https://datatracker.ietf.org/doc/draft-sporeba-tsvwg-mobile-l4s/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-slides-draft-sporeba-tsvwg-mobile-l4s-00 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document documents best practices for deployment of Low Latency, Low Loss, and Scalable Throughput (L4S) in mobile devices. It defines the responsibilities of the host operating system, the link- layer (modem and WiFi) subsystems to ensure successful end-to-end low-latency communication.

### Export of ECN Information in IPFIX
Draft: draft-song-opsawg-ipfix-ecn · Working group: tsvwg
Agenda: Xueyan Song: https://datatracker.ietf.org/doc/draft-song-opsawg-ipfix-ecn/ (10)
page: https://datatracker.ietf.org/doc/draft-song-opsawg-ipfix-ecn/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-export-of-ecn-information-in-ipfix-00 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
This document defines a set of IPFIX Information Elements for monitoring Explicit Congestion Notification (ECN), specifically in the context of the Low Latency, Low Loss, and Scalable Throughput (L4S) service. These Information Elements allow network operators to observe ECN codepoint usage within L4S deployments and evaluate the corresponding traffic performance.

### TCP and UDP checksum calculations for ILNP
Draft: draft-bhatti-ilnp-tcp-udp-checksums · Working group: tsvwg
Agenda: Saleem Bhatti: https://datatracker.ietf.org/doc/draft-bhatti-ilnp-tcp-udp-checksums/
page: https://datatracker.ietf.org/doc/draft-bhatti-ilnp-tcp-udp-checksums/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-tcp-and-udp-checksum-calculations-for-ilnp-00 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
The Identifier Locator Network Protocol (ILNP) for IPv6 is described in Experimental RFCs 6740-6744. ILNP defines the use of an Identifier-Locator Vector (I-LV) with a zero value L64 value and a relevant Node Identifier (NID) value in place of an IPv6 address in the pseudo-header for transport protocol checksum computations. However, as TCP and UDP predate ILNP, this change causes TCP and UDP checksum values to be generated for ILNP flows that are different to the same flows on IPv6. This document changes the checksum computation for TCP and UDP with ILNP so that the checksum values are the same for ILNP and IPv6. This document updates the checksum processing for TCP and UDP described in RFC6740 and RFC6741, and the way the checksum processing should be applied for TCP and UDP in RFC6748.

### DTLS Chunk for SCTP
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-dtls-chunk-for-sctp-00 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

### L4Sops Draft and L4S Interops
Presentation · Working group: tsvwg
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-tsvwg-l4sops-draft-and-l4s-interops-01 | video: https://youtu.be/Qy_MJ2BvUTA | materials: https://datatracker.ietf.org/meeting/126/session/tsvwg
Slides presented at the tsvwg session; no Internet-Draft is linked to them.

## Working Group: v6ops

### IPv6 Prefix Assignment to End-Sites
Draft: draft-ietf-v6ops-prefix-to-end-sites · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-prefix-to-end-sites/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-prefix-to-end-sites/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-jordi-palet-ipv6-prefix-assignment-to-end-sites-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document describes different alternatives and best current practices for assignment of IPv6 prefixes for end-sites in broadband networks, including considerations about point-to-point links, their size, numbering choices, pool choices, customer prefix assignment size and persistence of those assignments.

### 464XLAT/MAT-T Optimization
Draft: draft-ietf-v6ops-464xlat-optimization · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-464xlat-optimization/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-464xlat-optimization/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-jordi-palet-464xlatmap-t-optimization-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
IP/ICMP Translation Algorithm (SIIT) can be used to provide access for IPv4-only hosts or applications to IPv4-only or dual-stack destinations over IPv6-only infrastructure. In that case, the traffic flows are translated twice: first from IPv4 to IPv6 (stateless NAT46 at the ingress point to the IPv6-only infrastructure) and then from IPv6 back to IPv4 (stateful NAT64, at the egress point). When the destination is IPv6-enabled, the second translation might be avoided. This document describes a possible optimization to 464XLAT and MAP-T to avoid translating IPv6 flows back to IPv4 if the destination is reachable over IPv6. The proposed solution would significantly reduce the NAT64 utilization in the operator's network, increasing the performance.

### IPv6 Terminology Definitions
Draft: draft-ietf-v6ops-ipv6-only · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-only/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-jordi-palet-ipv6-only-and-ipv6-mostly-terminology-definition-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document defines the terminology regarding the usage of expressions such as "IPv6-Only" and "IPv6-Mostly", in order to avoid confusions when using them in IETF and other documents. In particular, a goal is to provide a reference that describes the actual "IPv6-Only" functionality being used in a given scope, not the installed protocol stack support.

### Testing Applications' IPv6 Support
Draft: draft-ietf-v6ops-ipv6-app-testing · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-ipv6-app-testing/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-draft-ietf-v6ops-ipv6-app-testing-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document provides guidance for application developers and software as a service providers on how to approach IPv6 testing in Dual-stack (IPv4+IPv6), and IPv6-only scenarios, including "IPv6- only-strict" scenarios without any connectivity towards any relevant IPv4 endpoint. It discusses common misconceptions about the degree to which operating systems and libraries can abstract IPv6 issues away and explains common regressions to avoid when deploying IPv6 support.

### A recommendation for filtering address records in stub resolvers
Draft: draft-ietf-v6ops-aaaa-filtering · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-aaaa-filtering/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-aaaa-filtering/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-filtering-address-records-in-stub-dns-resolvers-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Since IPv4 and IPv6 addresses are represented by different resource records in the Domain Name System, operating systems capable of running both IPv4 and IPv6 need to execute two queries when resolving a host name. This document discusses the conditions under which a stub resolver can optimize the process by not sending one of the queries if the host is connected to a single-stack network.

### Basic Requirements for IPv6 Customer Edge Routers
Draft: draft-ietf-v6ops-rfc7084bis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/
page: https://datatracker.ietf.org/doc/draft-ietf-v6ops-rfc7084bis/ | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document specifies requirements for an IPv6 Customer Edge (CE) router. Specifically, the current version of this document focuses on the basic provisioning of an IPv6 CE router and the provisioning of IPv6 hosts attached to it. The document obsoletes RFC 7084.

### Enhanced Dual Stack: Connectivity-Informed IPv6/IPv4 Selection
Draft: draft-xiao-v6ops-eds · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/
page: https://datatracker.ietf.org/doc/draft-xiao-v6ops-eds/ | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document describes Enhanced Dual Stack (EDS), a framework intended to reduce the operational risk and upfront workload of introducing IPv6 into an existing IPv4 network. EDS consists of two complementary mechanisms. First, connectivity-informed destination selection updates Rule 6 of RFC 6724 Section 6 from "Prefer higher precedence" to "Prefer higher precedence unless recently failed", so that recently failed IPv6 connectivity is not repeatedly preferred over IPv4. Second, operational diagnostics provide information that helps network administrators understand why IPv6 was not used and identify problems that can be corrected over time. With these mechanisms, IPv6 deployment can move from extensive upfront validation toward practical upfront validation followed by gradual operational improvement. This simpler IPv6 introduction approach can enable enterprises that do not have much IPv6 expertise and do not need a large number of IP addresses provided by IPv6 to try IPv6.

### Unicast Unsolicited Router Advertisements for Propagating Network Configuration Updates
Draft: draft-linkova-6man-ununra · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-linkova-6man-ununra/
page: https://datatracker.ietf.org/doc/draft-linkova-6man-ununra/ | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Multicast transmissions on Wi-Fi links are known to be unreliable, making the propagation of critical network configuration changes via multicast Router Advertisements (RAs) prone to failure or severe delay. Existing approaches to improve reliability, such as sending multiple unsolicited multicast RAs, require fine-tuning timers and packet counts that may not fit all deployment scenarios. This document updates RFC 4861 by introducing an optimization: when a router detects a configuration change that must be propagated to hosts, it sends unicast Router Advertisements to every client recently observed on that interface.

### Observations on the Reachability and Evasion of Packets with IPv6 Extension Headers on the Internet
Draft: draft-zedongjia-v6ops-ipv6eh-measurement · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-zedongjia-v6ops-ipv6eh-measurement/
page: https://datatracker.ietf.org/doc/draft-zedongjia-v6ops-ipv6eh-measurement/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-observations-on-the-reachability-and-evasion-of-packets-with-ipv6-extension-headers-on-the-internet-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
IPv6 Extension Headers (EHs) are designed to provide protocol flexibility and support for emerging features, while maintaining a concise base header and efficient processing. In practice, their reachability is affected by middlebox handling along the path, and their flexibility also introduces security considerations. This document presents observations from a comprehensive, large-scale measurement study of IPv6 Extension Header path traversal across more than 23,000 autonomous systems. Using a feedback-driven measurement framework called 6Travel, the reachability of 11 common IPv6 Extension Headers is measured over ICMPv6, TCP, and UDP. The measurements indicate a change relative to earlier work: contrary to past observations of heavy filtering, specific Extension Headers now achieve reachability comparable to plain traffic. Two distinct forms of policy ossification are observed across industry categories, together with widespread potential Extension-Header-based firewall evasion signatures in nearly 5,000 autonomous systems, particularly under TCP and UDP. These signatures appear consistent with a combination of implementation flaws and security misconfigurations, spanning both on-path and host-side firewalls.

### Considerations of IPv6-only Deployment in 5G Mobile Networks
Draft: draft-ma-v6ops-5g-ipv6only · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/
page: https://datatracker.ietf.org/doc/draft-ma-v6ops-5g-ipv6only/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-considerations-of-ipv6-only-deployment-in-5g-mobile-networks-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document describes a practical guide of deploying 464XLAT based IPv6-only technology on user plane in 3GPP 5G networks. It also covers key 5G concepts and architectures, configuration methods and operational challenges.

### Measurement and Analysis of IPv6 Interface Identifier Patterns in the Real World
Draft: draft-ren-v6ops-ipv6-iid-patterns-measurement · Working group: v6ops
Agenda: Draft: https://www.ietf.org/archive/id/draft-ren-v6ops-ipv6-iid-patterns-measurement-01.txt
page: https://datatracker.ietf.org/doc/draft-ren-v6ops-ipv6-iid-patterns-measurement/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-measurement-and-analysis-of-ipv6-interface-identifier-patterns-in-the-real-world-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Interface Identifiers (IIDs) are critical components of IPv6 addresses, significantly impacting user privacy and the feasibility of network reconnaissance. RFC 7707 previously provided a comprehensive analysis of IID patterns based on data from the early stages of IPv6 deployment. However, with the widespread adoption of privacy-enhancing standards such as RFC 7217, historical data no longer accurately reflects the current IPv6 ecosystem. This document provides updated measurements of IID patterns by utilizing an improved pattern recognition method and incorporating novel data sources, such as public mailing lists. The measurement data reveals that while "Low-byte" patterns have decreased significantly in server addresses, a substantial number of seemingly random addresses actually belong to non-random, specific patterns, implying that heuristic scanning remains a viable vector. Meanwhile, client devices have widely adopted randomized addresses, effectively enhancing privacy. This document aims to update the statistics and analysis regarding IID pattern distribution found in RFC 7707, providing essential insights for modern network defense strategies and standard compliance.

### Requirements for Provider Edge in IPv6-only Underlay Networks
Draft: draft-ma-v6ops-pe-ipv6only-reqs · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-ma-v6ops-pe-ipv6only-reqs/
page: https://datatracker.ietf.org/doc/draft-ma-v6ops-pe-ipv6only-reqs/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-requirements-for-provider-edge-in-ipv6-only-underlay-networks-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document defines functional, protocol, and operational requirements for Provider Edge (PE) devices operating in a multi- domain network environment where the underlay is exclusively based on IPv6. These requirements ensure consistent service delivery, interoperability, and efficient operations across autonomous domains while supporting IPv4-as-a-Service (IPv4aaS).

### IPv6 Wireless Access in Satellite Networks (IPWASN): Problem Statement and Use Cases
Draft: draft-lee-6man-ipv6-satellite-networks · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-lee-6man-ipv6-satellite-networks/
page: https://datatracker.ietf.org/doc/draft-lee-6man-ipv6-satellite-networks/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-ipv6-wireless-access-in-satellite-networks-ipwasn-problem-statement-and-use-cases-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document describes use cases and a problem statement for IPv6 Wireless Access in Satellite Networks (IPWASN). IPWASN aims at the IPv6-based wireless access in Non-Terrestrial Networks (NTNs), that is, satellite networks. It considers NTN characteristics such as dynamic topology, multi-hop communication over inter-satellite links, High-Altitude Platform Station (HAPS)-assisted relay paths, frequent handovers, variable link quality, and intermittent connectivity. Based on these characteristics, this document identifies key challenges in applying existing IPv6 protocols to NTN environments. It also analyzes the applicability of current IPv6 mechanisms and outlines requirements to support efficient data forwarding, Quality of Service (QoS), Segment Routing (SR)-based traffic engineering, and connectivity in satellite-based networks.

### IPv6 Deployment Statistics and Analysis
Draft: draft-pang-v6ops-ipv6-deployment-stats-analysis · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-deployment-stats-analysis/00/
page: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-deployment-stats-analysis/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-15-jing-zhao-ipv6-deployment-statistics-and-analysis-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
This document explains why existing observations of IPv6 deployment are often insufficient to identify the operational gaps and bottlenecks that limit IPv6 utilization and service quality. It describes the need for correlated analysis across different parts of the service path and discusses examples of statistical evidence that can support such analysis.

### IPv6 Path Performance Degradation in Dual-Stack Networks
Draft: draft-pang-v6ops-ipv6-path-degradation · Working group: v6ops
Agenda: Draft: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-path-degradation/
page: https://datatracker.ietf.org/doc/draft-pang-v6ops-ipv6-path-degradation/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-16-jing-zhao-ipv6-path-performance-degradation-in-dual-stack-networks-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
The document analyzes contributing factors across the content service layer and the network transport layer, and discusses why existing mechanisms such as RFC 6724 and Happy Eyeballs do not fully address performance failures that appear after connection establishment. This document is limited to problem analysis, scope clarification, and areas for further study. It does not define new network-to-host signaling mechanisms or require hosts to use network-provided information when making address-family or path selection decisions.

### How to upgrade a SaaS giant to IPv6
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-how-to-upgrade-a-saas-giant-to-ipv6-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Tim Winters - IPv6 CE Router (7084bis)
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-ipv6-ce-router-7084bis-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### xipeng xiao - Enhanced Dual Stack
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-10-xipeng-xiao-enhanced-dual-stack-00 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

### Jen Linkova UnicastUnsolicitedRAs 02
Presentation · Working group: v6ops
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-v6ops-10-jenlinkova-unicastunsolicitedras-01 | video: https://youtu.be/M8A47ED8OO8 | materials: https://datatracker.ietf.org/meeting/126/session/v6ops
Slides presented at the v6ops session; no Internet-Draft is linked to them.

## Working Group: wimse

### WIMSE Workload Credentials
Draft: draft-ietf-wimse-workload-creds · Working group: wimse
Agenda: a. Workload Identity Credentials — WGLC status & open issues (5 min): Arndt Schwenkschuster / Brian Campbell ( https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/ )
page: https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-workload-credentials-witwic-01 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
The WIMSE architecture defines authentication and authorization for software workloads in a variety of runtime environments, from the most basic ones up to complex multi-service, multi-cloud, multi- tenant deployments. This document defines the credentials that workloads use to represent their identity. They can be used in various protocols to authenticate workloads to each other. To use these credentials, workloads must provide proof of possession of the associated private key material, which is covered in other documents. This document focuses on the credentials alone, independent of the proof-of- possession mechanism.

### WIMSE Workload Proof Token
Draft: draft-ietf-wimse-wpt · Working group: wimse
Agenda: b. Workload Proof Token (8 min): Brian Campbell ( https://datatracker.ietf.org/doc/draft-ietf-wimse-wpt/ )
page: https://datatracker.ietf.org/doc/draft-ietf-wimse-wpt/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
The WIMSE architecture defines authentication and authorization for software workloads in a variety of runtime environments, from basic deployments to complex multi-service, multi-cloud, multi-tenant systems. This document specifies the Workload Proof Token (WPT), a mechanism for workloads to prove possession of the private key associated with a Workload Identity Token (WIT). The WPT is a signed JWT that binds the workload's authentication to a specific HTTP request, providing application-layer proof of possession for workload-to-workload communication. This specification is designed to work alongside the WIT credential format defined in draft-ietf- wimse-workload-creds and can be combined with other WIMSE protocols in multi-hop call chains.

### WIMSE Workload-to-Workload Authentication with HTTP Signatures
Draft: draft-ietf-wimse-http-signature · Working group: wimse
Agenda: c. HTTP Signature (8 min): Yaron Sheffer ( https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/ )
page: https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-http-signatures-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
The WIMSE architecture defines authentication and authorization for software workloads in a variety of runtime environments, from the most basic ones to complex multi-service, multi-cloud, multi-tenant deployments. This document defines one of the mechanisms to provide workload authentication, using HTTP Signatures. While only applicable to HTTP traffic, the protocol provides end-to-end protection of requests (and optionally, responses), even when service traffic is not end-to-end encrypted, that is, when TLS proxies and load balancers are used. Authentication is based on the Workload Identity Token (WIT).

### Workload Authentication Using Mutual TLS
Draft: draft-ietf-wimse-mutual-tls · Working group: wimse
Agenda: d. Mutual TLS (8 min): Joseph Salowey ( https://datatracker.ietf.org/doc/draft-ietf-wimse-mutual-tls/ )
page: https://datatracker.ietf.org/doc/draft-ietf-wimse-mutual-tls/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
The WIMSE architecture defines authentication and authorization for software workloads in a variety of runtime environments, from the most basic ones to complex multi-service, multi-cloud, multi-tenant deployments. This document profiles workload authentication based on X.509 Workload Identity Certificates using mutual TLS (mTLS).

### Workload Identity in a Multi System Environment (WIMSE) Architecture
Draft: draft-ietf-wimse-arch · Working group: wimse
Agenda: e. WIMSE Architecture (8 min): Joseph Salowey ( https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/ )
page: https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
The increasing prevalence of cloud computing and micro service architectures has led to the rise of complex software functions being built and deployed as workloads, where a workload is defined as software executing for a specific purpose, potentially comprising one or more running instances. This document discusses an architecture for designing and standardizing protocols and payloads for conveying workload identity and security context information.

### Workload Identifier
Draft: draft-ietf-wimse-identifier · Working group: wimse
Agenda: f. WIMSE Identifier (8 min): Yaroslav Rosomakho ( https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/ )
page: https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-workload-identifier-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
This document defines a canonical identifier for workloads, referred to as the Workload Identifier. A Workload Identifier is a URI that uniquely identifies a workload within the context of a specific trust domain. This identifier can be embedded in Workload Identity Credentials, including X.509 certificates and JWT-based tokens, to support authentication, authorization, and policy enforcement across diverse systems. The Workload Identifier format ensures interoperability, facilitates secure identity federation, and enables consistent identity semantics.

### WIMSE Trust Domain Discovery
Draft: draft-schwenkschuster-wimse-trust-domain-discovery · Working group: wimse
Agenda: a. WIMSE Trust Domain Discovery (5 min): Arndt Schwenkschuster / Yaroslav Rosomakho ( https://datatracker.ietf.org/doc/draft-schwenkschuster-wimse-trust-domain-discovery/ )
page: https://datatracker.ietf.org/doc/draft-schwenkschuster-wimse-trust-domain-discovery/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-wimse-trust-domain-discovery-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
The WIMSE architecture scopes workload identifiers to a trust domain. To validate a workload identity credential, a relying party must securely obtain the cryptographic trust anchors associated with the credential's trust domain. The WIMSE architecture requires that this mapping between a trust domain and its trust anchors is obtained through a secure mechanism, but leaves that mechanism undefined. This document defines such a mechanism for open environments in which no prior trust relationship exists between the relying party and the trust domain. It specifies the WIMSE Trust Bundle, a document that conveys the trust anchors of a trust domain for both JWT-based and X.509-based workload identity credentials, and a discovery mechanism based on a well-known HTTPS endpoint that allows a relying party to resolve a trust domain name to its trust bundle on demand.

### AI Agent Authentication and Authorization
Draft: draft-klrc-aiagent-auth · Working group: wimse
Agenda: b. AI Agent Authentication and Authorization (10 min): Yaroslav Rosomakho ( https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/ )
page: https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-aims-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
This document proposes best practices for authentication and authorization of AI agent interactions. It leverages existing standards such as the Workload Identity in Multi-System Environments (WIMSE) architecture and OAuth 2.0 family of specifications. Rather than defining new protocols, this document describes how existing and widely deployed standards can be applied or extended to establish agent authentication and authorization. By doing so, it aims to provide a framework within which to use existing standards, identify gaps and guide future standardization efforts for agent authentication and authorization.

### Heterogeneous Credential Verification for Workload and Agentic Systems
Draft: draft-jiang-wimse-heterogeneous-credential · Working group: wimse
Agenda: d. Heterogeneous Credential Verification (10 min): Yuning Jiang ( https://datatracker.ietf.org/doc/draft-jiang-wimse-heterogeneous-credential/ )
page: https://datatracker.ietf.org/doc/draft-jiang-wimse-heterogeneous-credential/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-heterogeneous-credential-verification-for-workload-and-agentic-systems-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
Workloads in multi-system environments, including AI agents acting on behalf of users and organizations, increasingly present multiple credentials of heterogeneous types within a single request: workload identity tokens, user-delegated OAuth access tokens, W3C Verifiable Presentations, X.509 certificates, or platform-specific API keys. These are issued by different authorities, follow different formats, are verified by different verifiers, and carry different assurance semantics. A relying party that receives such a heterogeneous credential set has no common way to represent the set, identify each credential's type, determine the authoritative verifier for it, interpret verification results consistently, or combine multiple results into a single handling decision. This document defines a mechanism for processing a heterogeneous credential set on receipt. It specifies a representation of the credential set, a procedure for identifying each credential's type and determining its verifier, a minimal common model for verification results that lets results from different verifiers be compared, and a policy model that combines multiple results into one handling decision. The mechanism is transport-agnostic and does not constrain where the processing functions are deployed.

### PEDIGREE: Verifiable Delegation Identity for Agentic AI Systems
Draft: draft-rampalli-pedigree · Working group: wimse
Agenda: e. PEDIGREE: per-hop delegation above workload credentials (10 min): Karthik Rampalli ( https://datatracker.ietf.org/doc/draft-rampalli-pedigree/ )
page: https://datatracker.ietf.org/doc/draft-rampalli-pedigree/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-karthikrampalli-pedigree-deck-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
This document defines PEDIGREE (Per-Agent Delegation Identity with Governance-Enforced Execution), an identity and delegation framework for AI agents that extends the workload-identity model of SPIFFE (RFC 9542 / draft-ietf-wimse) with cryptographic per-hop delegation, monotonic scope attenuation enforced at mint and at verify, and dual- layer authority enforcement combining an operator-controlled ceiling with per-parent mandate narrowing. PEDIGREE complements AAuth (draft-hardt-aauth-protocol) and AIP (draft-prakash-aip) by providing: (a) dual-enforcement semantics absent from both, (b) Cedar-policy mandates with static-analysis proofs of narrowing, (c) strict cryptographic parent-token re- verification that catches parent-swap attacks missed by append-only token chains, and (d) a native bridge to existing SPIFFE deployments.

### WIMSE Workload Attestation
Draft: draft-reddy-wimse-workload-attestation · Working group: wimse
Agenda: f. WIMSE Workload Attestation (5 min): Tirumal Reddy / Nathanael Ritz ( https://datatracker.ietf.org/doc/draft-reddy-wimse-workload-attestation/ )
page: https://datatracker.ietf.org/doc/draft-reddy-wimse-workload-attestation/ | slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-wimse-workload-attestation-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
This document extends the WIMSE workload-to-workload authentication architecture with a mechanism for conveying attestation across TLS- terminating proxies, a deployment topology where TLS-layer attestation mechanisms lose their end-to-end security properties.

### Binding Named-Human Authorization Evidence into Agent-Action Records
Draft: draft-schrock-human-authorization-binding · Working group: wimse
Agenda: g. Human authorization as a verifier input (5 min, remote): Iman Schrock ( https://datatracker.ietf.org/doc/draft-schrock-human-authorization-binding/ ) ( https://datatracker.ietf.org/doc/draft-schroc
page: https://datatracker.ietf.org/doc/draft-schrock-human-authorization-binding/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
A recurring pattern spans the agent-action record formats now in development: a record about an agent's action reserves a place for "the human authorization" — an approver disposition, an authority context, a human-override field, an actor slot, a signed grant, an approval reference — and leaves its semantics undefined. Each format, reasonably, does not want to specify human-authorization evidence itself; none, so far, says what filling the slot means. This document defines that one thing, host-agnostically: how any record binds named-human authorization evidence, either BY REFERENCE (a content digest of the authorization artifact's canonical bytes) or EMBEDDED (a compact, self-describing claim carrying named approvals and optional distinct-human quorum semantics), with five requirements that make the binding mean the same thing in every host: digest grounding, action agreement, verified-versus-accepted discipline, fail-closed absence, and embedded/referenced consistency. The SCITT signed-statement host family is expressed concretely (digest selection, and the observed-absence statement that is the only way absence of authorization becomes evidence); an informative appendix maps the binding onto the reserved slots of eleven current documents. This document defines no new authorization format: the referenced evidence verifies under its own specification.

### Authorization Receipts for High-Risk Agent Actions
Draft: draft-schrock-ep-authorization-receipts · Working group: wimse
Agenda: g. Human authorization as a verifier input (5 min, remote): Iman Schrock ( https://datatracker.ietf.org/doc/draft-schrock-human-authorization-binding/ ) ( https://datatracker.ietf.org/doc/draft-schroc
page: https://datatracker.ietf.org/doc/draft-schrock-ep-authorization-receipts/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
This document defines the EMILIA Protocol (EP) authorization receipt, an evidence artifact binding an enrolled approver key to one canonical action before execution. An approver-held key signs an Authorization Context containing the action hash, policy reference, shared authorization instance, per-signoff nonce, audience, and validity window. A Trust Receipt carries the signed contexts, terminal consumption record, and Merkle inclusion material so a relying party can verify the recorded event offline under independently selected log, directory, policy, and approver trust inputs. The receipt establishes only the guarantees of the selected verification profile. The mapping from an enrolled approver identifier to a natural person is asserted by the directory authority. Offline verification does not establish current revocation status, global non-replay, comprehension, legality, safety, or execution. Replay prevention requires an online atomic consumption store at the executor. The state-machine invariants are machine-checked under the assumptions stated in this document. This revision defines the closed EP-AUTHORIZATION-BUNDLE-v1 pre- execution profile and its verification algorithm. The bundle carries the Action Object, signed Authorization Contexts, signoffs, key proofs, and presentation evidence; it deliberately carries no terminal consumption or execution claim. An optional, profile- identified authorization binding can commit the human evidence to an independently verified native authorization artifact without replacing that artifact or making this receipt format depend on its transport or trust model. A receipt is evidence, not authorization. This document does not treat a local user interaction as an authorization decision. It defines one evidence artifact that an authorization architecture can use in a human-confirmation flow: the signed Authorization Context is action-bound confirmation evidence an authorization server MAY validate and bind to the grant it issues. The resulting Trust Receipt records terminal consumption and remains evidence; neither object makes the authorization decision. That decision remains with the authorization server.

### The Mandate JWT (MJWT) for Agentic AI Systems
Draft: draft-sato-soos-mjwt · Working group: wimse
Agenda: h. SOOS: Mandate JWT & Cross-Principal Transaction ID (XPID) (5 min): Tom Sato ( https://datatracker.ietf.org/doc/draft-sato-soos-mjwt/ ), ( https://datatracker.ietf.org/doc/draft-sato-soos-kia/ )
page: https://datatracker.ietf.org/doc/draft-sato-soos-mjwt/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
An AI agent that can act without a verifiable, human-traceable authorization record is an agent without an owner. Existing authorization credentials tell you what an agent is permitted to do; none of them tell you who authorized it, on which specific object, under which mission, or how far that authority can be delegated before it reaches this agent. This document defines the Mandate JWT (MJWT): a WIMSE workload credential profile that binds an AI agent's authority to a specific Sovereign Object instance under a named human principal, with a cryptographically enforced delegation ceiling and an eight-dimensional Narrowing Property that prevents any sub-agent from exceeding the authority of the human principal at the root of the chain. Version -02 adds a seventh narrowing dimension (consent scope), the consent_scope claim carrying data subject consent state for APPI/GDPR compliance, the sub_agent_scope claim for consent attenuation across delegation hops, a Purpose Code Registry, and HEM_CONSENT_REQUIRED integration for fail-closed consent enforcement. The MJWT is the authorization primitive referenced by the other SOOS governance drafts. Version -03 corrects an IANA registration issue: the two registries requested there are renamed to drop the redundant word "Registry" from the registry name itself, and each now includes the Designated Expert Guidance that a Specification Required registration policy requires. No new claims, codes, or normative behavior are introduced in -03; this is a registration-format correction only. Version -04 addresses four findings from a WIMSE security review checklist dry-run against -02/-03 (DR-MJWT-KIA-CHECKLIST-01): the parent-mandate check at Cedar-action verification time is tightened from a disjunctive "retrieve or verify" to a mandatory live re-verification of the parent's current signature and revocation status, closing a parent-swap-class window; the Revocation Registry is now stated explicitly to be the same Revocation Registry the KIA draft defines, and the residual cross-instance propagation-lag risk this implies is now named explicitly, mirroring how that draft discloses its own XPID revocation gap; and a new Security Considerations entry states plainly that MJWT does not itself establish or verify a human_principal_id's root authority. Version -05 closes gaps surfaced by a WIMSE-style security review pass against -04's own text: an eighth Narrowing Property dimension, max_delegation_depth, closes an unbounded-delegation- depth Denial of Service vector that -04's own text named but did not bound; the consent_reference staleness defense is upgraded from a SHOULD-level recommendation to a MUST, extending the same live-re-verification discipline already applied to parent mandates; and the Introduction's description of RFC 8693 inheritance is corrected to no longer claim use of the optional may_act claim, which this document does not in fact use. This revision also carries minor idnits and citation-hygiene fixes. Version -06 is an editorial revision with no normative content changes: six sibling-draft citations (HEM, CAP, KIA, MAD, AEP, IDP) had gone stale against those drafts' current live versions and are updated to draft-sato-soos-hem-07, draft-sato-soos-cap-06, draft-sato-soos-kia-06, draft-sato-soos-mad-04, draft-sato-soos-aep-04, and draft-sato-soos-idp-06 respectively.

### Kernel Identity and Attestation for Governing Enforcement Components
Draft: draft-sato-soos-kia · Working group: wimse
Agenda: h. SOOS: Mandate JWT & Cross-Principal Transaction ID (XPID) (5 min): Tom Sato ( https://datatracker.ietf.org/doc/draft-sato-soos-mjwt/ ), ( https://datatracker.ietf.org/doc/draft-sato-soos-kia/ )
page: https://datatracker.ietf.org/doc/draft-sato-soos-kia/ | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
This document specifies the Kernel Identity and Attestation (KIA) protocol for the Sovereign Object OS (SOOS) governance architecture. KIA defines the cryptographic identity of the GEC, the trust chain anchoring kernel authority from hardware root through operator root keypair to every signed Event Log entry, the GEC Manifest schema for runtime state attestation, and the Revocation Registry maintenance requirements. KIA is the Layer 0 signing and attestation component on which the audit trail guarantees of draft-sato-soos-gar, the mandate enforcement guarantees of draft-sato-soos-mjwt, and the multi-agent delegation chain of draft-sato-soos-mad all depend. Version -03 adds FROST threshold signing for high-availability GEC keypair deployments, the Cross-Principal Identifier (XPID) for cross-instance federation audit correlation, the XPID cross- instance trust model, and four new Security Considerations addressing FROST nonce reuse, XPID revocation gap, identity takeover via claimed identifier (CVE-2025-13609 class), and attestation channel binding (CVE-2026-33697 class). This document is the reference specification for the KIA RATS WG presentation at IETF 126 Vienna. The XPID primitive and the CVE-2026-33697 attestation channel binding defense are the primary novel contributions presented to the RATS WG. Version -04 corrects a registry-format mismatch identified by IANA early review (#1456067): the IANA Considerations request to register XPID_DERIVED and XPID_VERIFICATION_FAILED into the GAR Authority Lifecycle Event Types Registry the GAR draft defines now uses that registry's actual column set (Event Type, Class, Reference) and assigns both entries the newly-defined Class ID (Identity/ Federation event). No new event types, fields, or normative behavior are introduced in -04; this is a registration-format correction only. Version -05 discloses a known open issue found by a WIMSE security review checklist dry-run against -03 (DR-MJWT-KIA-CHECKLIST-01, Finding 4): the Cross-Instance Trust Model verifies an XPID but does not restrict which federation participants can see the underlying Evidence in the first place. This is named as OQ-KIA-EVIDENCE-VIS, following the same acknowledge-rather-than- silently-omit pattern this document already uses for OQ-S-XPID-REV. No mechanism is specified in -05; resolution is deferred, consistent with how OQ-S-XPID-REV is treated. Version -06 closes out a full WIMSE Security Review checklist pass (Stage 0 through Stage 2) run against -05. It restores seven GEC Manifest fields silently absent since -03 despite -03's text claiming the -02 schema was carried forward in full, including attestation_certificate; mints a dedicated XPID namespace UUID in place of the reused DNS namespace UUID; updates the FROST reference from the CFRG working draft to RFC 9591 and corrects the nonce-generation section citations; resolves a genuine bootstrapping contradiction between the quorum-failure signing prohibition and the quorum-failure alerting requirement (new CONF-KIA-24); tightens Security Considerations wording describing the XPID derivation input; adds a new Denial of Service Security Considerations entry for the quorum-isolation availability asymmetry; and adds a Privacy Considerations section addressing XPID's by-design stability and cross-context linkability. No prior conformance requirement is weakened by this revision. Version -07 is an editorial revision with no normative content changes: sibling-draft citations had gone stale against those drafts' current live versions and are updated to draft-sato-soos-cap-06, draft-sato-soos-gar-08, draft-sato-soos-mad-05, draft-sato-soos-mjwt-06, and draft-sato-soos-idp-06; the companion-drafts discussion's HEM and AEP mentions are similarly updated to hem-07 and aep-04.

### WPT of WIMSE
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-wpt-of-wimse-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE MTLS
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-wimse-mtls-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### WIMSE Architecture
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-wimse-architecture-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### Offline workload access for user-owned resources without refresh tokens
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-offline-workload-access-for-user-owned-resources-without-refresh-tokens-01 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

### SOOS: Mandate JWT & Cross-Principal Transaction ID (XPID)
Presentation · Working group: wimse
slides: https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-soos-mandate-jwt-cross-principal-transaction-id-xpid-00 | video: https://youtu.be/0a4HZRJ5d9c | materials: https://datatracker.ietf.org/meeting/126/session/wimse
Slides presented at the wimse session; no Internet-Draft is linked to them.

