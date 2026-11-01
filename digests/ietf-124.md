<!--
conference: IETF 124 (Montreal)
type: standards
source_url: https://datatracker.ietf.org/meeting/124/agenda.json
generated: 2026-11-01
registry_key: ietf-124
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 124 (Montreal) — Digest for the Networking/Identity PM

A note on depth: none of the 24 pre-selected items carried `pdf:`, `page:`, or `video:` links in the program data, and no full source text was available for this run. Every write-up below is therefore **from the abstract only** — substance and maturity signals are reasoned from draft names, stream (`draft-ietf-*` = WG-adopted vs. personal-name drafts = individual), and the abstracts themselves.

## Core

These land squarely on the PM's desk: DC fabric routing, lossless/low-latency transport, DC/WAN interconnect, BGP internals and security, and workload/agentic identity.

### RIFT: Routing in Fat Trees

**Tier:** Core — Working Group: rift (authors not listed in program text)

- **Why:** The PM designs and operates Clos/fat-tree IP fabrics; RIFT is the only routing protocol purpose-built for that topology class, and it is a long-running WG document (`draft-ietf-rift-rift`) — i.e., moving toward (or through) publication, meaning implementations will start to matter commercially.
- **What:** A dynamic routing protocol specialized for Clos, fat-tree, and variants, explicitly optimized to minimize (a) control-plane state so very large substrates scale, and (b) configuration/operational complexity so fabrics are simple to deploy. The abstract draws the lineage from crossbar/backplane interconnects to IP fabrics.
- **How:** (From abstract only.) Topology-aware design that exploits the predictable structure of fat trees to suppress state and configuration rather than treating the fabric as a generic IGP graph.
- **Where applicable:** Large spine-leaf/Clos IP fabrics in datacenters; broadly applicable to any operator building fat-tree fabrics, not tied to a specific vendor or silicon. It is a complement/alternative to eBGP- or IGP-based underlays, not a WAN protocol.

### SRIFT: Segment Routing in Fat Trees

**Tier:** Core — Working Group: rift (authors not listed in program text)

- **Why:** Extends RIFT with Segment Routing traffic steering — directly relevant if the PM is evaluating SR (MPLS or SRv6) for policy-based steering and telemetry in a DC fabric.
- **What:** Signaling procedures for Segment Routing in RIFT: how node loopbacks, the SRGB, and Node-SIDs get distributed and how traffic is steered.
- **How:** (From abstract only.) Node loopbacks, SRGB, and Node-SIDs are distributed *southbound* from Top-of-Fabric nodes using RIFT's Key-Value distribution mechanism, so each node can compute paths to the active SID in a packet. An SDN/SR controller signals SR policies to ingress nodes to impose desired segment lists.
- **Where applicable:** RIFT fabrics only — depends on deploying RIFT as the underlay. WG-adopted (`draft-ietf-rift-sr`), but newer than RIFT itself, so expect it to trail RIFT in implementation maturity.

### Use of BGP for Routing in Large-Scale Data Centers

**Tier:** Core — Working Group: rtgwg (authors not listed in program text)

- **Why:** The canonical "BGP as the only routing protocol in the DC" design document; if the PM runs eBGP fabrics, this is the consensus reference design others will cite and build to.
- **What:** An operational-experience document covering data centers with over 100,000 servers ("large-scale"), where the driving requirements are operational simplicity and network stability. It reports a proven, stable routing design using BGP alone, intended to be leveraged by the rest of the industry.
- **How:** (From abstract only.) Design guidance distilled from running BGP-only DCs at that scale, rather than a new protocol — the contribution is the documented, validated design pattern.
- **Where applicable:** Large-scale DCs where eBGP is (or will be) the underlay. Broadly applicable since it is operator experience, not tied to specific hardware; most relevant to organizations building or auditing DC routing design.

### Data Center TCP (DCTCP): TCP Congestion Control for Data Centers

**Tier:** Core — Working Group: tcpm (authors not listed in program text)

- **Why:** DCTCP is the ECN-based congestion control that underpins low-latency DC networking and is a key reference point for anyone engineering RDMA/lossless-adjacent fabrics where TCP and lossless traffic share buffers. The abstract reads as a finished document ("This Informational RFC describes…") documenting what major OSes already ship.
- **What:** A TCP congestion control scheme that extends ECN processing to *estimate the fraction of bytes* encountering congestion rather than merely detecting that congestion occurred, then scales the congestion window from that estimate. Result: high burst tolerance, low latency, and high throughput with shallow-buffered switches.
- **How:** (From abstract only.) Fine-grained ECN marking at switches + sender-side estimation of the congested-byte fraction + proportional cwnd scaling. The document also covers coexistence with conventional TCP, the lack of sender-receiver negotiation, and possible mitigations.
- **Where applicable:** Controlled environments like data centers only — the abstract is explicit that it must not be deployed over the public Internet without additional measures. Requires ECN-capable (shallow-buffered) switch configuration; already implemented in major operating systems, so this is codification, not blue-sky work.

### More Accurate Explicit Congestion Notification (AccECN) Feedback in TCP

**Tier:** Core — Working Group: tcpm (authors not listed in program text)

- **Why:** A wire-format change to TCP itself — the enabling substrate for DCTCP, L4S, and ConEx, all of which need multiple ECN feedback signals per RTT. If the PM cares about low-latency DC transport or L4S-style queueing, this is the piece that makes it deployable, and it also specifies middlebox treatment (historically the killer for TCP header changes).
- **What:** An update to RFC 3168 specifying AccECN: more than one ECN feedback signal per RTT carried in the TCP header, plus feedback of the IP-ECN field seen during connection establishment, with optional supplementary feedback in two new TCP options.
- **How:** (From abstract only.) Reuses scarce header space: it takes the TCP header bit previously reserved for the ECN-Nonce and overloads the two existing ECN flags; the new options are never used on the SYN. The document also normatively covers how middleboxes must treat the modified wire protocol.
- **Where applicable:** Any TCP endpoint pair that opts in — DC (with DCTCP), Internet L4S deployments, and ConEx. Broadly applicable, but the ECN-Nonce sacrifice and middlebox behavior mean deployment tracking matters; WG-adopted and mature (`draft-ietf-tcpm-accurate-ecn`).

### Topology Independent Fast Reroute using Segment Routing (TI-LFA)

**Tier:** Core — Working Group: rtgwg (authors not listed in program text) — *individual draft* (`draft-bashandy-...`), widely implemented but not yet WG-adopted

- **Why:** Sub-50ms protection for SR underlays — relevant to the PM's DC underlay and WAN interconnect planning. Notably this remains an individual-submission draft despite broad vendor implementation, so its status here signals whether the rtgwg is finally moving it into the WG stream.
- **What:** TI-LFA: Fast Reroute protection for node and adjacency segments in the SR framework, with *guaranteed* coverage in any IGP network — closing the coverage gaps of classic LFA/RLFA/DLFA.
- **How:** (From abstract only.) Builds on proven IP-FRR concepts (LFA, remote LFA, remote LFA with directed forwarding) and extends them with SR segment insertion. Its key trick is computing the FRR path as the *post-convergence* path from the repair point, which eliminates the operational pain of tuning tie-breaks among FRR candidates.
- **Where applicable:** IGP + Segment Routing networks — DC underlays and WANs. Broadly applicable across SR deployments; not applicable where SR is absent.

### Secure EVPN

**Tier:** Core — Working Group: bess (authors not listed in program text)

- **Why:** Changes both the security mechanism and the signaling model for DC/enterprise inter-site encryption: IKEv2 is *removed* from the picture. For a PM whose remit spans DC fabric and network security, this is the highest-leverage security item in the set — it changes how keys and policy are distributed for tenant traffic over public Internet.
- **What:** A method to secure EVPN tenant traffic (privacy, integrity, authentication equivalent to IKEv2-based IPsec tunnels) for inter-site and WAN connectivity over the public Internet, using EVPN/BGP across DC, SP, and enterprise segments.
- **How:** (From abstract only.) Leverages BGP point-to-multipoint signaling for key and policy exchange among PE devices, creating private pairwise IPsec Security Associations — without IKEv2 point-to-point signaling or any direct peer-to-peer session establishment.
- **Where applicable:** EVPN deployments needing encrypted inter-site/WAN tenant connectivity — DC NVE gateways, enterprise WAN edges. Tied to EVPN control-plane infrastructure (broadly applicable to EVPN shops, useless without one). WG-adopted (`draft-ietf-bess-secure-evpn`).

### Interconnect Solution for Ethernet VPN (EVPN) Overlay Networks

**Tier:** Core — Working Group: bess (authors not listed in program text)

- **Why:** The DC/WAN interconnect seam — exactly the boundary the PM works. This is the WG-mature document defining how EVPN-overlay DCs stitch into WAN L2VPN technologies, including gateway behavior and a route-type trick for MAC-scale control.
- **What:** How Network Virtualization Overlays (NVOs) connect to a WAN to extend tenant L2 connectivity; analyzes interactions between EVPN-overlay networks and WAN L2VPN technologies (VPLS, PBB-VPLS, EVPN, PBB-EVPN), and extends EVPN procedures where needed.
- **How:** (From abstract only.) Two concrete mechanisms: (1) processing of EVPN routes on gateways that interconnect EVPN-Overlay to EVPN-MPLS networks, plus the Interconnect Ethernet Segment (I-ES) for multihoming across the boundary; (2) the Unknown MAC Route (UMR) to prevent MAC-table scale problems on DC NVE devices.
- **Where applicable:** DC-to-WAN L2 extension for tenants — DC NVE gateways and SP edge devices. Broadly applicable wherever EVPN overlays meet MPLS-based VPNs; presumes EVPN on both sides.

### SRv6 Segment Identifiers in the IPv6 Addressing Architecture

**Tier:** Core — Working Group: 6man (authors not listed in program text)

- **Why:** An addressing-architecture decision that shapes SRv6 deployment everywhere — SIDs look like IPv6 addresses but don't always behave like them, and this document makes a dedicated prefix allocation for them. That has direct consequences for IPAM systems, ACL/filter design, and core-routing security (filtering SRv6 space) in any SRv6 datapath the PM operates.
- **What:** An exploration of SRv6 SID characteristics and their relationship to the IPv6 Addressing Architecture (RFC 4291 territory), culminating in the allocation of a dedicated prefix for SRv6 SIDs.
- **How:** (From abstract only.) Analysis plus a concrete IANA-facing prefix allocation, giving SIDs a recognizable home so nodes and tools can distinguish SID space from ordinary unicast address space.
- **Where applicable:** Any SRv6 deployment — DC underlays, WANs, and service programming. Broadly applicable; WG-adopted (`draft-ietf-6man-sids`), and the prefix allocation is the kind of change that lands in filters and IPAM tooling once finalized.

### Updated BGP Operations and Security

**Tier:** Core — Working Group: grow (authors not listed in program text) — *individual draft* (`draft-fiebig-...`)

- **Why:** RFC 7454 is the de-facto BGP hardening runbook; this is its refresh. For the PM's BGP-internal and network-security interests, it is the current statement of what "well-operated BGP" means, including post-RPKI-era topics.
- **What:** An update to RFC 7454 best current practices: reiterates prior guidance and adds practices that emerged since — session protection (TTL/hop limits, TCP-AO, control-plane filtering), routing-information control (prefix filtering and automation, max-prefix, AS-path filtering, route flap dampening, BGP community scrubbing), plus new material.
- **How:** (From abstract only.) Structured as an operational BCP refresh: unified terminology aligned to RFC 9234 (BGP roles), IXP LAN prefix recommendations updated to actual practice, expanded coverage of ASPA and BGP roles, community scrubbing, filter generation/evaluation to limit performance overhead, defense-in-depth outbound and internal filtering, global prefix limits, and community-based downstream prefix filtering.
- **Where applicable:** Any operator of BGP — DC fabs, enterprise WANs, IXPs, and SPs. Broadly applicable; being an individual draft, its trajectory at this meeting (adoption?) is the signal to watch.

### Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3

**Tier:** Core — Working Group: tls (authors not listed in program text)

- **Why:** The concrete crypto migration the PM's identity stack will ride on — every TLS-terminated endpoint (API gateways, OIDC endpoints, SPIFFE-style workload TLS) will negotiate these. This defines the exact hybrid mechanisms and is WG-adopted and far along.
- **What:** Three hybrid key agreement mechanisms for TLS 1.3 — X25519MLKEM768, SecP256r1MLKEM768, and SecP384r1MLKEM1024 — combining classical ECDHE with the post-quantum ML-KEM (module-lattice KEM).
- **How:** (From abstract only.) Hybrid construction: both the ECDHE shared secret and the ML-KEM encapsulation secret contribute, so security degrades only to today's level if either is broken.
- **Where applicable:** All TLS 1.3 endpoints; broadly applicable. Practical note for the PM: larger handshake sizes affect DC-internal mTLS meshes and high-rate connection workloads (service-to-service TLS), so rollout pacing and middlebox/CDN behavior are worth tracking.

### Workload Identity in a Multi System Environment (WIMSE) Architecture

**Tier:** Core — Working Group: wimse (authors not listed in program text)

- **Why:** The IETF's home for workload identity — the standards-track counterpart to the SPIFFE/SPIRE ecosystem the PM already works with. The architecture document is the umbrella for the other two WIMSE drafts below, and this WG is where cross-vendor workload identity semantics are being settled.
- **What:** An architecture for designing and standardizing protocols and payloads that convey *workload identity and security context information* across systems, motivated by cloud computing and microservices architectures where complex functions are composed of many workload instances.
- **How:** (From abstract only.) Defines the architectural components and the protocol/payload design space for propagating identity and security context — a framework document intended to guide the specific mechanisms (identifiers, token conveyance) rather than one wire protocol.
- **Where applicable:** Multi-system cloud/microservice environments — broadly applicable to any organization doing workload identity federation; directly relevant alongside SPIFFE/SPIRE, Kubernetes service accounts, and mesh mTLS. WG-adopted (`draft-ietf-wimse-arch`).

### AI Identity Management System (AIMS)

**Tier:** Core — Working Group: wimse (authors not listed in program text)

- **Why:** Agentic identity is explicitly in the PM's remit, and this is the IETF's focused attempt at it: how AI agents authenticate and authorize their interactions, deliberately built on existing standards rather than inventing new ones.
- **What:** Best practices for authentication and authorization of AI agent interactions, leveraging WIMSE and the OAuth 2.0 family. Rather than defining new protocols, it describes how existing, widely deployed standards can be applied or extended for agent authN/authZ, and frames where the gaps are.
- **How:** (From abstract only.) A framework document: maps existing OAuth/WIMSE mechanisms onto agent-to-agent and agent-to-service interactions, identifies gaps, and is intended to guide future standardization rather than specify a wire format.
- **Where applicable:** Any platform deploying AI agents that call services or other agents — broadly applicable precisely because it reuses deployed primitives. Early-stage WG work (`draft-ietf-wimse-aims`); watch it for gap analysis that could spawn new drafts the PM should track.

### Workload Identifier

**Tier:** Core — Working Group: wimse (authors not listed in program text)

- **Why:** The naming layer of workload identity — a canonical identifier is the precondition for interoperable authN/authZ/policy across heterogeneous systems. Directly comparable to (and in conversation with) SPIFFE IDs, which are also URIs.
- **What:** Defines the Workload Identifier: a URI that uniquely identifies a workload within the context of a specific trust domain, embeddable in workload identity credentials including X.509 certificates and JWT-based tokens.
- **How:** (From abstract only.) Canonical URI format with defined semantics, carried in existing credential types so that authentication, authorization, and policy enforcement can share one identifier across systems; designed for interoperability, secure identity federation, and consistent identity semantics.
- **Where applicable:** Any environment issuing workload credentials — k8s-adjacent platforms, meshes, SPIFFE-style deployments. Trust-domain scoping is the key constraint: identifiers are not globally unique, so federation semantics (defined in the WIMSE arch) carry the weight.

### The OAuth 2.1 Authorization Framework

**Tier:** Core — Working Group: oauth (authors not listed in program text)

- **Why:** OAuth 2.1 obsoletes OAuth 2.0 and Bearer Token usage — the base protocol of the PM's entire identity surface. Even though it consolidates rather than invents, it becomes the single normative reference implementations and audits will be held to.
- **What:** A single specification that replaces RFC 6749 (OAuth 2.0) and RFC 6750 (Bearer Token Usage), defining how an application obtains limited access to a protected resource — either via a resource-owner approval interaction with an authorization service, or on the application's own behalf.
- **How:** (From abstract only.) Consolidation of the authorization framework; the abstract does not enumerate which security-mandatory practices (e.g., exact redirect matching, PKCE) got folded in, so treat the details as to-be-verified against the draft.
- **Where applicable:** Essentially every web/API identity product. Broadly applicable by definition; the migration/compatibility story (existing OAuth 2.0 deployments and profiles) is the operational risk to watch.

### Delegated Credentials for TLS and DTLS

**Tier:** Core — Working Group: tls (authors not listed in program text)

- **Why:** Short-lived, operator-controlled credentials for TLS endpoints — the mechanism behind big-CDN practice of issuing 24-hour-ish leaf credentials without waiting on the CA. Directly relevant to certificate-lifetime strategy for the PM's fleet endpoints.
- **What:** A mechanism letting operators of TLS/DTLS endpoints overcome CA-imposed limits (certificate lifetime, usage constraints, supported algorithms) by delegating their own credentials for use in TLS/DTLS — without breaking compatibility with peers that don't support it.
- **How:** (From abstract only.) The CA grants the operator a delegation capability; the operator then mints short-lived credentials locally for its frontends. Backwards compatibility is preserved because unsupported peers simply see the normal certificate path.
- **Where applicable:** Large TLS endpoint fleets — CDNs, SaaS frontends, and by extension large internal mTLS estates where short-lived leaf certs are desirable. Broadly applicable; requires CA buy-in to issue the delegation.

### Client-Cert HTTP Header Field

**Tier:** Core — Working Group: httpbis (authors not listed in program text)

- **Why:** Standardizes the mTLS-offload pattern every gateway/LB already improvises: a TLS-terminating reverse proxy needs to tell the origin who the client certificate says it is. Today this is ad-hoc headers (and often spoofable); a standardized, predictable field changes the security posture of the pattern the PM's Gateway-API/mesh stack almost certainly uses.
- **What:** HTTP extension header fields that allow a TLS-terminating reverse proxy (TTRP) to convey the client certificate information of a mutually authenticated TLS connection to the origin server in a common, predictable manner.
- **How:** (From abstract only.) Proxy inserts the client-cert-derived fields into forwarded requests; the "common and predictable" framing suggests a single interop-relevant format rather than per-vendor headers.
- **Where applicable:** Any architecture where TLS terminates at a proxy in front of services — API gateways, service mesh ingress, k8s ingress. Broadly applicable; the trust model (origin must know it can trust the TTRP) is the inherent constraint.

## Adjacent

Useful context and near-term influence on the PM's areas, without being directly on the critical path.

### Active OAM for use in Geneve

**Tier:** Adjacent — Working Group: nvo3 (authors not listed in program text)

- **Why:** Geneve is the encapsulation used by major hypervisor overlay stacks (and some k8s-adjacent networking); OAM is what makes overlay fabrics operable. Without in-band active OAM, overlay troubleshooting devolves to packet captures across three layers.
- **What:** Requirements and a framework for OAM in Geneve networks — the functions needed to monitor, diagnose, and troubleshoot Geneve overlays, guiding implementation of OAM mechanisms so operators can maintain reliable virtualized environments.
- **How:** (From abstract only.) A requirements/framework document rather than a single protocol — it defines the OAM function space (liveness, path verification, fault isolation) that implementers of Geneve OAM options should build to.
- **Where applicable:** Geneve-based overlays (hypervisor networking, NVE edges). Broadly applicable to Geneve deployments; irrelevant to VXLAN-only or MPLS-only estates. WG-adopted (`draft-ietf-nvo3-geneve-oam`).

### Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)

**Tier:** Adjacent — Working Group: sidrops (authors not listed in program text)

- **Why:** SAV is the current hot topic in routing security (driven by prefix-hijack-driven reflection attacks); this WG-adopted method shows how RPKI artifacts (ROAs, and the newer ASPA) become inputs to anti-spoofing filters, not just route origin validation.
- **What:** A method to build more robust SAV filters by combining BGP UPDATE messages, ASPA, and ROA data — improving network resilience while minimizing false positives (blocking legitimate traffic) and maintaining directionality per RFC 8704. It updates RFC 8704.
- **How:** (From abstract only.) Derives SAV filter entries from BGP-announced reachability cross-checked against ASPA and ROA authorization, so an interface only accepts source addresses legitimately originating/routed toward it.
- **Where applicable:** Primarily edge/WAN operators (IXP-adjacent and inter-AS boundaries) rather than DC fabrics — that's why it's Adjacent for this PM. Broadly applicable to operator edge deployments; deployment coordination between neighbors affects false-positive behavior.

### Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0

**Tier:** Adjacent — Working Group: acme (authors not listed in program text)

- **Why:** Bridges the two identity worlds the PM spans — X.509/ACME automation and OIDC federation trust — so certificates can be issued to federation entities automatically. Relevant wherever federated trust (education/healthcare/gov ecosystems) meets TLS automation.
- **What:** Defines how X.509 certificates for an OpenID Federation Entity are issued by an X.509 CA through ACME, to organizations participating in an OpenID Federation 1.0 trust infrastructure.
- **How:** (From abstract only.) ACME's automated challenge/response demonstration of control is combined with OpenID Federation's trust evaluation (attesting key possession, entity metadata, administrative/technical info) so federation membership substitutes for the usual ACME domain-control validation path.
- **Where applicable:** OpenID Federation 1.0 deployments — mostly federated identity ecosystems (research/education, public sector). Broadly applicable within that model; not relevant to non-federated ACME use.

### Direct Anonymous Attestation for the Remote Attestation Procedures Architecture

**Tier:** Adjacent — Working Group: rats (authors not listed in program text)

- **Why:** Privacy-preserving remote attestation sits at the intersection of the PM's identity and security interests — DAA is the mechanism behind anonymity-conscious device attestation (best known from TPM ecosystems), and this draft gives it a standards-architecture home.
- **What:** Maps Direct Anonymous Attestation onto the RATS architecture, introducing the DAA Issuer protocol entity and specifying how it maps to existing RATS roles in DAA protocol steps.
- **How:** (From abstract only.) An architectural-mapping document — it defines where the DAA Issuer fits among RATS roles (attesters, verifiers, RPs) during the DAA protocol flow, rather than specifying new cryptography.
- **Where applicable:** Environments needing anonymous (unlinkable) attestation — hardware-rooted device identity, privacy-sensitive deployments. Relevant to confidential-computing and device-supply-chain work; narrower than the PM's core workload-identity scope, hence Adjacent.

## Wildcard

Not a direct fit, but genuinely novel or directionally important.

### Updates to X.509 Policy Validation

**Tier:** Wildcard — Working Group: lamps (authors not listed in program text)

- **Why:** A quiet, excellent piece of security engineering: the RFC 5280 certificate-policy validation algorithm has worst-case *exponential* behavior, meaning a maliciously crafted certificate chain could DoS path validation in any TLS library. Everyone who validates certificates — including every one of the PM's identity endpoints — is affected.
- **What:** Replaces the RFC 5280 policy-validation algorithm with an equivalent but polynomial-time algorithm, eliminating the DoS vector while preserving validation outcomes.
- **How:** (From abstract only.) Reformulates the certificate-policies graph computation so it scales linearly rather than exponentially in chain length/policy branching.
- **Where applicable:** Every X.509 path-validation implementation — broadly applicable, and the kind of change that lands as CVEs and patch cycles in TLS stacks. The equivalence requirement (same accept/reject results) is what makes it drop-in.

### Proxying Ethernet Frames in HTTP

**Tier:** Wildcard — Working Group: masque (authors not listed in program text)

- **Why:** The logical endpoint of the MASQUE line of thinking: if you can proxy TCP, UDP, and IP in HTTP, why not entire Ethernet segments? It signals where overlay networking is heading — L2 connectivity as a commodity riding QUIC/HTTP, which is a genuinely different world from the PM's Geneve/VXLAN tooling.
- **What:** A protocol that lets an HTTP client create a tunnel to exchange Layer-2 Ethernet frames through an HTTP server with an attached physical or virtual Ethernet segment — the L2 analogue of IP proxying in HTTP. Notably, it does not guarantee in-order frame delivery.
- **How:** (From abstract only.) Extends the MASQUE proxying model with an Ethernet-frame capsule/stream type; the explicit no-in-order-delivery guarantee keeps it simple at the cost of pushing reliability concerns up the stack.
- **Where applicable:** Remote access to an Ethernet segment over an HTTP intermediary — enterprise remote-L2 access, cloud-provider L2 attachment over the open Internet. Broadly applicable in principle; the no-ordering guarantee constrains which L2 protocols tolerate it.

### COSE (CBOR Object Signing and Encryption) Receipts

**Tier:** Wildcard — Working Group: cose (authors not listed in program text)

- **Why:** Transparency infrastructure (Merkle-tree-logged, auditor-checkable commitments) is spreading from certificate transparency into messaging, supply chain, and — plausibly soon — workload credential ecosystems. This is the concise, CBOR-native building block for that, which could matter for verifiable identity/attestation supply chains adjacent to the PM's remit.
- **What:** COSE Receipts: proofs of properties of a verifiable data structure, enabling security properties such as minimal disclosure, transparency, and non-equivocation, with CBOR encodings for Merkle inclusion and consistency proofs as the demonstrated extensibility mechanism.
- **How:** (From abstract only.) Builds on CBOR/COSE to express compact proofs that a given item is in a committed data structure (inclusion) and that the structure only grew (consistency) — the standard transparency toolkit at a fraction of the encoding weight.
- **Where applicable:** Transparency-oriented systems — certificates, end-to-end encrypted messaging key transparency, supply-chain security. Broadly applicable as a building block; adoption depends on ecosystems wanting lightweight rather than existing (RFC 6962-style) transparency machinery.

## Themes

- **Workload and agentic identity is the IETF's newest gravitational center.** The WIMSE WG is stacking architecture + canonical identifier + AI-agent practices, deliberately reusing OAuth/OIDC — the PM should read the three drafts as one program with the identifier draft being the fastest-to-matter piece.
- **TLS/credential hygiene is converging on a deployable package.** MLKEM hybrids, delegated credentials, client-cert forwarding, OAuth 2.1, and the X.509 policy-graph DoS fix collectively say: the wire-security substrate is being refreshed this cycle.
- **The DC fabric is getting protocol purpose-built for it.** RIFT + SRIFT (topology-aware routing) alongside a matured DCTCP + AccECN pair — the ECN machinery for low-latency, shallow-buffer fabrics is being finished, which matters for TCP/RDMA coexistence in lossless networks.
- **Security is being folded into existing signaling planes.** Secure EVPN does IKEv2's job via BGP; BAR-SAV derives anti-spoofing filters from RPKI artifacts; the BGP ops/security refresh codifies a post-RPKI-era runbook. The pattern is security as a property of routing protocols, not a parallel stack.
- **EVPN is the interconnect lingua franca.** Both bess drafts treat EVPN as the universal adapter — overlay-to-MPLS gateways, interconnect multihoming, and now encrypted inter-site service — reinforcing EVPN as the seam between the PM's DC and WAN worlds.
- **Maturity split worth watching:** most items are WG-adopted (`draft-ietf-*`), but TI-LFA and the BGP-ops update are still individual submissions despite being industry de-facto practice — their adoption status at this meeting is a signal about how the rtgwg/grow streams are curating operational reality.
