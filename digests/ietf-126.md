<!--
conference: IETF 126 (Vienna)
type: standards
source_url: https://datatracker.ietf.org/meeting/126/agenda.json
generated: 2026-11-01
registry_key: ietf-126
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 126 (Vienna) — Standards Digest

This is a standards program: working-group sessions and Internet-Drafts, so the substance lives in the drafts. From the pre-selected subset, 25 items made the cut, grouped into Core / Adjacent / Wildcard below. Notes on sourcing:

- The program text provided titles, draft names, and abstracts only — no authors/affiliations and no per-item `pdf:`/`page:`/`video:` links — so no Links sections are reproduced here; every draft is findable on the IETF Datatracker under its draft name.
- No full-text sources were available for this run, so **every write-up below is based on the program abstract only** (marked per item). Maturity signals are read from the draft names: an `ietf-` prefix means the draft is WG-adopted; drafts without it are individual submissions.

## Core

### RIFT: Routing in Fat Trees (draft-ietf-rift-rift)

*Core · WG: rift · WG-adopted draft · long-running WG effort with an ecosystem building around it*

- **Why:** A rare thing: an IETF routing protocol designed specifically for the PM's home topology — Clos/fat-tree IP fabrics. It attacks the two things that hurt at DC scale: control-plane state growth and per-node configuration burden, both of which make eBGP spine-leaf fabrics operationally expensive.
- **What:** A specialized, dynamic routing protocol for Clos, fat-tree, and variants, optimized to minimize control-plane state for very large substrates and to minimize configuration and operational complexity for simplified deployment (from abstract only).
- **How:** The protocol is designed to exploit the structure of the topology (the tree's levels and directionality) rather than treating the fabric as a generic graph; the companion Auto-EVPN draft confirms a zero-touch (ZTP) provisioning model as a core property.
- **Where applicable:** Greenfield IP fabrics built as Clos/fat-tree — primarily datacenters, with the topology family originating in crossbar/backplane designs. Requires NOS/silicon support; not a retrofit for arbitrary or non-Clos topologies. Broadly applicable to any operator building fat-tree fabrics; not org-specific.

### RIFT Auto-EVPN (draft-ietf-rift-auto-evpn)

*Core · WG: rift · WG-adopted draft · newer companion to RIFT itself*

- **Why:** Configuration burden is the main tax on EVPN overlays; this removes it by deriving overlay provisioning from the RIFT underlay's zero-touch architecture. If RIFT gains traction, this is the document that makes RIFT + EVPN a deployable "fabric in a box."
- **What:** Procedures that allow an EVPN overlay to be fully and automatically provisioned when RIFT is the underlay, by leveraging RIFT's no-touch ZTP architecture (from abstract only).
- **How:** Reuses RIFT's zero-touch operation so EVPN overlay service state comes up without per-node overlay configuration.
- **Where applicable:** Only where RIFT is the underlay and EVPN is the overlay — tightly coupled to RIFT adoption. Datacenter fabric overlays; not applicable to non-RIFT fabrics.

### Secure EVPN (draft-ietf-bess-secure-evpn)

*Core · WG: bess · WG-adopted draft*

- **Why:** EVPN overlays spanning sites over the public internet today drag in IKEv2/IPsec meshes, which are painful to operate at DC scale. This draft reuses the BGP/EVPN control plane the fabric already runs to signal keys and policy and build pairwise IPsec SAs with no direct peer-to-peer session setup — a real change in security properties and operational model for DC interconnect.
- **What:** A solution where BGP point-to-multipoint signaling is leveraged for key and policy exchange among PE devices, creating private pairwise IPsec Security Associations that provide the same privacy, integrity, and authentication for tenant traffic as IKEv2-based IPsec tunneling — without IKEv2 signaling or any other direct peer-to-peer session establishment (from abstract only).
- **How:** The existing BGP p2mp signaling machinery carries keys and policy to the PEs, which then construct private pairwise SAs from that distribution.
- **Where applicable:** DC and Enterprise inter-site/WAN connectivity over public internet where EVPN is already deployed. Assumes the PEs share a trust relationship via the BGP control plane — worth scrutinizing the security considerations on key distribution versus IKEv2's authenticated exchange. Broadly applicable across EVPN deployments.

### Interconnect Solution for Ethernet VPN (EVPN) Overlay Networks (draft-ietf-bess-dci-evpn-overlay)

*Core · WG: bess · WG-adopted draft · long-running WG document*

- **Why:** The canonical DC-WAN interconnect problem: EVPN-overlay datacenters needing L2 extension into WAN L2VPN technologies (VPLS, PBB-VPLS, EVPN-MPLS, PBB-EVPN). Gateway route handling, multihoming across the interconnect, and MAC scale at the NVE are exactly the issues that bite in production DCI.
- **What:** How Network Virtualization Overlays connect to WANs for tenant L2 extension: processing of EVPN routes on gateways between EVPN-Overlay and EVPN-MPLS networks, the Interconnect Ethernet Segment (I-ES) for multihoming, and the Unknown MAC Route (UMR) to avoid MAC-scale problems on NVE devices (from abstract only).
- **How:** Extends the existing EVPN procedures for gateway interconnect; I-ES provides multihoming across the interconnect; UMR lets NVEs handle unknown-destination traffic without learning every tenant MAC.
- **Where applicable:** DC NVEs/gateways connecting EVPN-overlay sites into MPLS- or VPLS-based WANs where tenants need L2 extension. A general technique, not org-specific; requires both sides to implement the relevant specs.

### Data Center TCP (DCTCP): TCP Congestion Control for Data Centers (draft-ietf-tcpm-dctcp)

*Core · WG: tcpm · WG-adopted draft · Informational; documents behavior already implemented by several major operating systems*

- **Why:** The reference specification for the ECN-based congestion control that shallow-buffered DC fabrics assume. Having it documented as an Informational RFC matters for interop and for anyone reasoning about lossless/low-latency fabric design — the abstract itself notes it is already implemented by several major OSes.
- **What:** DCTCP extends ECN processing to estimate the *fraction* of bytes that encounter congestion (rather than merely detecting that some congestion occurred) and scales the TCP congestion window on that estimate, achieving high burst tolerance, low latency, and high throughput with shallow-buffered switches. The memo also covers coexistence with conventional TCP, the lack of a sender-receiver negotiation mechanism, and mitigations (from abstract only).
- **How:** The receiver feeds back ECN markings; the sender computes the fraction of bytes that saw congestion and scales cwnd proportionally instead of reacting to a single congestion signal.
- **Where applicable:** Controlled environments only — datacenters — and explicitly must not be deployed over the public Internet without additional measures. Requires ECN-capable, shallow-buffered switching. Broadly applicable across DC TCP stacks; already shipped.

### More Accurate Explicit Congestion Notification (AccECN) Feedback in TCP (draft-ietf-tcpm-accurate-ecn)

*Core · WG: tcpm · WG-adopted draft · upgraded from the proposed adjacent tier: this is a TCP wire-format change that underpins DCTCP-class and L4S behavior*

- **Why:** A wire-format change to TCP (updating RFC 3168): receivers today can echo at most one ECN signal per RTT, which is too coarse for DCTCP, ConEx, and L4S senders. AccECN is the plumbing that makes per-marking feedback possible beyond the DC — and its explicit middlebox treatment spec addresses the place where such changes usually break in deployment.
- **What:** A scheme providing more than one ECN feedback signal per RTT in the TCP header — by allocating the reserved bit previously assigned to the ECN-Nonce and overloading the two existing ECN flags — plus optional feedback via two new TCP options (never used on the SYN). It also feeds back the IP-ECN field received during connection establishment and specifies middlebox treatment of the updated wire protocol (from abstract only).
- **How:** Accumulates the CE markings received and returns a count in reclaimed header space, giving senders the accurate multi-marking feedback that DCTCP/L4S-style control needs.
- **Where applicable:** Host TCP stacks generally — not DC-only. Deployment risk is middlebox interference, hence the middlebox spec. Pairs naturally with DCTCP above and with L4S-era work.

### BGP Flow Specification Version 2 (draft-ietf-idr-flowspec-v2)

*Core · WG: idr · WG-adopted draft · changes the FS wire format via a new NLRI*

- **Why:** FSv1 is load-bearing in DDoS mitigation, BGP/MPLS VPN filtering, centralized firewall control, and SFC — and its deployed pain is real: no consistent TLV encoding of rules, no user ordering of rules/actions, and unclear interaction with peers that don't support FS. V2 fixes all three and deliberately demarcates itself with a different NLRI. Every flowspec consumer (scrubbing centers, controllers, router firewalls) will need to handle this.
- **What:** Version 2 of BGP flow specification: consistent TLV encoding for rules, user ordering of filter rules and actions, and clear definitions of interaction with BGP peers not supporting FSv1 — encapsulated in a new NLRI to separate FSv1 and FSv2 cleanly (from abstract only).
- **How:** Re-encodes flow-spec components as uniform TLVs within a new NLRI and specifies ordering and backward-compatibility semantics.
- **Where applicable:** Anyone using BGP flow-spec today: DDoS mitigation, VPN traffic filtering, centralized traffic control of router firewall functions, SFC insertion. General-purpose; requires FSv2 support on originator and applying routers.

### BGP Flow Specification for QUIC (draft-ietf-idr-fsv2-quic)

*Core · WG: idr · WG-adopted draft · builds on FSv2*

- **Why:** As traffic shifts to QUIC/HTTP-3, classic 5-tuple flow-spec loses usefulness, and QUIC's encryption hides most of what filters traditionally keyed on. Defining diversion based on QUIC packet characteristics is how DDoS mitigation and traffic steering remain possible in a QUIC-heavy internet.
- **What:** Defines how to perform Flow Specification traffic diversion based on the characteristics of QUIC packets (from abstract only).
- **How:** Extends the FSv2 matching framework with criteria derived from QUIC packets — necessarily the characteristics still observable outside the encrypted payload — so traffic can be diverted without decryption.
- **Where applicable:** Flow-spec deployments (scrubbing, steering) confronting QUIC traffic; depends on FSv2 adoption. A general technique, not org-specific.

### Workload Identity in a Multi System Environment (WIMSE) Architecture (draft-ietf-wimse-arch)

*Core · WG: wimse · WG-adopted draft · the umbrella document for WIMSE's other work*

- **Why:** The IETF's architecture for workload identity and security-context propagation — the standards-track analog of the SPIFFE/SPIRE world the PM already works in. The other WIMSE documents (identifier, AIMS, the client-assertion BCP) all hang off this one.
- **What:** An architecture for designing and standardizing the protocols and payloads that convey workload identity and security-context information in cloud/microservice environments, where software is built and deployed as workloads with one or more running instances (from abstract only).
- **How:** Decomposes workload identity and context propagation into the architectural components and interface points where standardized protocols and payloads are needed.
- **Where applicable:** Cloud and microservice deployments broadly; complements rather than replaces SPIFFE/SPIRE and service-mesh identity mechanisms. Not org-specific.

### AI Identity Management System (draft-ietf-wimse-aims)

*Core · WG: wimse · WG-adopted draft · newer document*

- **Why:** Agentic identity — authentication and authorization of AI agents — is the fastest-moving identity topic, and this is the IETF's position: reuse OAuth 2.0 and WIMSE rather than invent new protocols, and use the document to surface the gaps. Directly on the PM's agentic-identity interest.
- **What:** Best practices for authentication and authorization of AI agent interactions, leveraging the WIMSE architecture and the OAuth 2.0 family; explicitly avoids defining new protocols, instead describing how existing, widely deployed standards can be applied or extended, identifying gaps, and guiding future standardization (from abstract only).
- **How:** Maps agent interactions onto existing OAuth/WIMSE mechanisms (token issuance, delegation, assertions) and frames where those mechanisms fall short.
- **Where applicable:** Any environment where AI agents invoke APIs on a user's or system's behalf; applies to existing OAuth/identity infrastructure. The gap analysis is useful even outside IETF process.

### Workload Identifier (draft-ietf-wimse-identifier)

*Core · WG: wimse · WG-adopted draft*

- **Why:** The interop primitive of the WIMSE stack: a canonical workload identifier — a URI scoped to a trust domain, embeddable in both X.509 certificates and JWTs. It plays the role a SPIFFE ID plays today, on a standards track, and is what makes identity federation between the X.509/mTLS world and the JWT world coherent.
- **What:** Defines the Workload Identifier: a URI that uniquely identifies a workload within the context of a specific trust domain, embeddable in workload identity credentials (X.509 certificates and JWT-based tokens) to support authentication, authorization, and policy enforcement across diverse systems (from abstract only).
- **How:** One canonical URI format carried inside credentials, so identity semantics stay consistent regardless of credential type or consuming system.
- **Where applicable:** Multi-system environments where X.509 and JWT credentials coexist — the common case in service meshes and SPIFFE-adjacent deployments. Broadly applicable.

### OAuth 2.0 Client Assertion in Workload Environments (draft-ietf-wimse-workload-identity-bcp)

*Core · WG: wimse · WG-adopted draft · upgraded from the proposed adjacent tier: this is the "how you do it today" document for a SPIFFE + OAuth shop*

- **Why:** Container platforms can't safely manage static `client_id`/`client_secret` material, and the industry has converged on federating workload-platform credentials as OAuth client assertions. This BCP — meta-flow, security recommendations, and concrete patterns — is directly the day-to-day problem of running Kubernetes workloads against OAuth authorization servers.
- **What:** Describes using the OAuth client-assertion flows (RFC 7521, particularly RFC 7523) with credentials of the underlying workload platform instead of manually provisioned secrets; gives a meta flow (Section 3.1), security recommendations (Section 4), and outlines concrete patterns (Appendix A) (from abstract only).
- **How:** Platform-issued credentials are presented as JWT client assertions to the authorization server (the abstract leaves the concrete credential types open — SPIFFE-style SVIDs are the common instance of this pattern).
- **Where applicable:** Container orchestration systems and any workload platform able to issue federatable credentials. A general practice document, not org-specific.

### Transaction Tokens (draft-ietf-oauth-transaction-tokens)

*Core · WG: oauth · WG-adopted draft*

- **Why:** Identity and authorization-context propagation through a service call chain is what service meshes bolt on ad hoc today; Txn-Tokens standardize it. For a PM spanning identity and service mesh, this is the convergence point.
- **What:** Txn-Tokens maintain and propagate user identity, workload identity, and authorization context throughout a call chain within a trusted domain, for external requests (e.g., API calls) or internally initiated requests, preserving that context across the chain (from abstract only).
- **How:** A token carried between services in the chain that carries the accumulated identity and authorization context so downstream services can enforce policy with full context.
- **Where applicable:** Trusted domains only — internal microservice call chains; by design not a third-party federation mechanism. Complements the WIMSE stack.

### The OAuth 2.1 Authorization Framework (draft-ietf-oauth-v2-1)

*Core · WG: oauth · WG-adopted draft · intended to obsolete RFC 6749/6750*

- **Why:** The consolidation of OAuth 2.0 and Bearer Token Usage into a single baseline that folds in a decade of security hardening. Every OAuth implementation the PM touches will eventually be measured against this; migration and compatibility planning is the practical concern.
- **What:** A single authorization framework enabling an application to obtain limited access to a protected resource — either on behalf of a resource owner via an approval interaction, or on its own behalf — replacing and obsoleting RFC 6749 and RFC 6750 (from abstract only).
- **How:** Consolidates the RFC 6749/6750 baseline with subsequent security practice into one specification; expect the accumulated best-current-practice requirements to become normative here.
- **Where applicable:** All OAuth deployments. Watch conformance implications for existing clients, authorization servers, and resource servers.

### OAuth 2.0 Demonstrating Proof of Possession (DPoP) (draft-ietf-oauth-dpop)

*Core · WG: oauth · WG-adopted draft · mature WG work, widely implemented across the identity ecosystem*

- **Why:** Bearer tokens are replayable by design; DPoP sender-constrains OAuth tokens at the application level and is becoming the default for high-value APIs where mTLS token binding isn't available. Directly relevant to API security architecture.
- **What:** A proof-of-possession mechanism on the application level that sender-constrains OAuth 2.0 tokens, enabling detection of replay of access and refresh tokens (from abstract only).
- **How:** The client binds tokens to a key it holds and demonstrates possession on each use, so a token presented without the key can be detected and rejected.
- **Where applicable:** OAuth deployments wanting sender-constrained tokens without mutual-TLS infrastructure; requires coordinated support across client, authorization server, and resource server. Broadly applicable.

### JSON Web Proof (draft-ietf-jose-json-web-proof)

*Core · WG: jose · WG-adopted draft · first structural extension of the JWS container model*

- **Why:** JOSE is getting a new container format designed for selective disclosure and unlinkability — the cryptographic direction of the identity ecosystem (verifiable credentials). This changes token formats, not just algorithms, and the draft notes these techniques are maturing into early market adoption.
- **What:** JWP: a JWS-like container that can integrity-protect multiple payloads in one message, plus a new presentation form supporting selective disclosure of individual payloads, additional proof computation, and a Presentation Header to prevent replay (from abstract only).
- **How:** A multi-payload container whose presentation form lets the holder reveal chosen payloads while cryptographically proving the undisclosed ones — rather than revealing everything that was signed.
- **Where applicable:** Selective-disclosure credential use cases (the emerging digital-credential ecosystem); not a replacement for JWS in ordinary API tokens.

### Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3 (draft-ietf-tls-ecdhe-mlkem)

*Core · WG: tls · WG-adopted draft · changes every TLS 1.3 handshake's wire format*

- **Why:** The concrete PQ migration step for TLS: hybrid key agreement combining classical ECDHE with ML-KEM, with deployment already underway in mainstream browsers and TLS stacks. Every TLS termination point the PM operates — load balancers, mesh sidecars, APIs — has this on its roadmap, and it changes the handshake wire format (notably larger key shares).
- **What:** Three hybrid key agreement mechanisms for TLS 1.3 — X25519MLKEM768, SecP256r1MLKEM768, and SecP384r1MLKEM1024 — each combining ML-KEM with an ECDHE exchange (from abstract only).
- **How:** Both classical and PQ key shares go into the ClientHello and the resulting secrets are combined, so the handshake stays secure as long as either mechanism holds.
- **Where applicable:** All TLS 1.3 endpoints. Practical constraints: larger handshake messages (a real concern for middleboxes and constrained links) and ecosystem performance; broadly applicable and already shipping.

## Adjacent

### YANG Model for Border Gateway Protocol (BGP-4) (draft-ietf-idr-bgp-model)

*Adjacent · WG: idr · WG-adopted draft · long-running; check current NOS/controller adoption before betting on it*

- **Why:** BGP configuration and policy automation is where the PM's BGP interest meets operations. This is the IETF's standard YANG model for BGP, distilled from datacenter, carrier, and content-provider operational requirements — the natural comparison point against OpenConfig-style models.
- **What:** A YANG data model for configuring and managing BGP — protocol, policy, and operational aspects such as the RIB — based on datacenter, carrier, and content-provider requirements (from abstract only).
- **How:** YANG modules covering protocol configuration, routing policy, and operational state (RIB), consumable via NETCONF/RESTCONF tooling.
- **Where applicable:** BGP automation toolchains generally. Long-running WG document; adoption across NOSes and controllers is the deciding factor.

### Updated BGP Operations and Security (draft-fiebig-grow-bgpopsecupd)

*Adjacent · WG: grow · individual draft (note: no `ietf-` prefix — not yet WG-adopted; early)*

- **Why:** RFC 7454 is the canonical BGP opsec BCP and is a decade old. This rewrite brings it current — TTL security, TCP-AO, ASPA, BGP roles, automated prefix-filter generation, community scrubbing — and BCP updates shape operator expectations and audit checklists. Flagged adjacent because it is an individual draft without WG consensus yet.
- **What:** An update to RFC 7454 reiterating its best practices and adding: session protection (TTL, TCP-AO, control-plane filtering); routing-information control (prefix filtering with automation, max-prefix, AS-path filtering, route flap dampening, community scrubbing); terminology unified per RFC 9234; revised IXP LAN prefix recommendations; ASPA and BGP roles; outbound/internal filtering for defense in depth; global prefix limits; and community-based filtering for downstream prefixes (from abstract only).
- **How:** Best-current-practice guidance; no protocol change.
- **Where applicable:** Anyone operating BGP — DC WAN edges, enterprises, IX participants. Content is usable today, but treat it as pre-consensus.

### Delegated Credentials for TLS and DTLS (draft-ietf-tls-subcerts)

*Adjacent · WG: tls · WG-adopted draft · mature; already deployed in production by large edge/CDN operators*

- **Why:** The organizational split between endpoint operators and the CA limits certificate lifetime, usage, and algorithm agility. Delegated credentials let edge operators mint their own short-lived credentials — a production-proven pattern at major CDNs — while remaining compatible with peers that don't support the extension.
- **What:** A mechanism enabling operators to delegate their own credentials for use in TLS and DTLS, overcoming CA-imposed limitations without breaking compatibility with non-supporting peers (from abstract only).
- **How:** The endpoint operator issues scoped, short-lived credentials under its existing CA-issued certificate, presenting them in the handshake with a negotiated extension.
- **Where applicable:** Large TLS endpoint operators (CDNs, edge platforms) needing short-lived credentials and algorithm agility; requires client-side negotiation support, which mainstream browsers already ship.

### Proxying IP in HTTP (draft-ietf-masque-connect-ip)

*Adjacent · WG: masque · WG-adopted draft · updates RFC 9298; this line of work is mature*

- **Why:** Completes the CONNECT family: UDP proxying is RFC 9298, and this defines proxying arbitrary IP packets over HTTP — the substrate for modern zero-trust/egress architectures that ride HTTP/2-3 instead of VPN appliances. Adjacent rather than core for a K8s/eBPF-centric role, but it is the access-layer complement to service-mesh egress.
- **What:** A protocol allowing an HTTP client to create an IP tunnel through an HTTP server acting as an IP proxy, transmitting arbitrary IP packets; updates RFC 9298 (from abstract only).
- **How:** Extends the MASQUE/CONNECT tunneling model over HTTP connections to full Layer-3 packets between client and proxy.
- **Where applicable:** Client environments where egress must traverse HTTP infrastructure (browsers, zero-trust client agents) and where an IP-capable proxy server exists. Check publication status — the work is near final form.

### CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Registrations for Web Authentication (WebAuthn) Algorithms (draft-ietf-cose-webauthn-algorithms)

*Adjacent · WG: cose · WG-adopted draft · registry housekeeping, but interop-relevant for the passkey ecosystem*

- **Why:** Thin but directly useful to anyone in passkeys: WebAuthn/CTAP use COSE algorithm identifiers, and this registers the algorithms those implementations actually use into the COSE and JOSE registries, so passkey credentials can be represented consistently across the CBOR and JWT ecosystems.
- **What:** IANA registrations of RSASSA-PKCS1-v1_5 (with SHA-256/384/512/SHA-1) and ECDSA over secp256k1 with SHA-256 into the COSE Algorithms registry; secp256k1 into the COSE Elliptic Curves registry; and the corresponding JOSE algorithm and curve registrations (from abstract only).
- **How:** Registry actions only — no new protocol mechanics.
- **Where applicable:** Implementations that must express WebAuthn/FIDO2 credentials in COSE or JOSE structures (passkey APIs, cross-ecosystem credential portability).

## Wildcard

### The SSLKEYLOGFILE Format for TLS (draft-ietf-tls-keylogfile)

*Wildcard · WG: tls · WG-adopted draft*

- **Why:** A delightful example of the IETF codifying de-facto practice: the SSLKEYLOGFILE convention is already parsed by every TLS debugging tool but has never been specified. Standardizing it — with an explicit "test data only" boundary — makes the debugging toolchain interoperable and the safety limits official.
- **What:** A format for recording the secrets used in a TLS connection to a file, allowing diagnostic and logging tools to decrypt the messages exchanged by TLS endpoints; intended for use in systems where TLS only protects test data (from abstract only).
- **How:** A specified file format for per-connection secrets, matching what existing tools already parse.
- **Where applicable:** Development and test environments only — by construction catastrophic in production. Interesting as a signal of the TLS WG taking ownership of its debugging ecosystem.

### Proxying Ethernet Frames in HTTP (draft-ietf-masque-connect-ethernet)

*Wildcard · WG: masque · WG-adopted draft*

- **Why:** Layer 2 over HTTP is a genuinely surprising combination: remote access to an Ethernet segment — physical lab networks, virtual L2 segments, device access — tunneled through an ordinary HTTP server with no VPN infrastructure. The kind of primitive that enables odd but useful things (remote NIC/lab access, distributed testbeds).
- **What:** A protocol allowing an HTTP client to create a tunnel to exchange Layer-2 Ethernet frames through an HTTP server with an attached physical or virtual Ethernet segment; the protocol does not guarantee in-order frame delivery (from abstract only).
- **How:** A CONNECT-style extension of the MASQUE framework carrying Ethernet frames instead of IP packets.
- **Where applicable:** Remote access to Ethernet segments over HTTP infrastructure — labs, testbeds, virtual segments — rather than production DC fabric work. Constrained by the lack of in-order delivery and the need for a proxy attached to the target segment.

### COSE (CBOR Object Signing and Encryption) Receipts (draft-ietf-cose-merkle-tree-proofs)

*Wildcard · WG: cose · WG-adopted draft*

- **Why:** Generalizes the certificate-transparency idea into a compact CBOR/COSE building block: proofs about verifiable data structures delivering minimal disclosure, transparency, and non-equivocation. Already applied to certificates, E2E messaging, and supply-chain security — and a plausible substrate for future credential transparency in the identity world the PM inhabits.
- **What:** COSE Receipts that prove properties of a verifiable data structure to a verifier, providing security properties such as minimal disclosure, transparency, and non-equivocation; includes CBOR encodings for Merkle inclusion and consistency proofs to demonstrate extensibility (from abstract only).
- **How:** Receipts carried in COSE structures with proof types bound to verifiable data structures; the Merkle proof encodings are the demonstration instance.
- **Where applicable:** Transparency-oriented systems, especially in CBOR/constrained environments: supply-chain security, E2E messaging, certificate and credential transparency. A building block, not a turnkey system.

## Themes

- **The DC fabric stack is consolidating inside the IETF:** RIFT, RIFT Auto-EVPN, Secure EVPN, and the EVPN DCI interconnect document together cover underlay automation, encrypted inter-site connectivity, and DC-WAN interconnect — a coherent push to make fat-tree fabrics and EVPN overlays less hand-built.
- **ECN is graduating from trick to plumbing:** DCTCP documented as already-deployed practice, AccECN changing the TCP wire format for accurate multi-signal feedback — the foundations for DCTCP-class and L4S behavior in and beyond the datacenter.
- **BGP's second life as a policy bus, plus an opsec refresh:** FSv2 (new NLRI, ordered rules), QUIC-aware flow-spec, the BGP YANG model, and a rewrite of the BGP opsec BCP — BGP increasingly distributes filtering and mitigation policy in a QUIC-heavy internet.
- **Identity for non-humans is the most active new area:** the WIMSE trio (architecture, workload identifier, client-assertion BCP), agentic identity (AIMS), and Transaction Tokens — all deliberately reusing OAuth rather than inventing new protocols, with gap analysis to guide what comes next.
- **The OAuth baseline is being consolidated and hardened:** OAuth 2.1, DPoP, and Txn-Tokens together re-baseline the core identity protocol family while fixing the bearer-token weaknesses.
- **A lot of this cycle is the IETF writing down deployed reality:** DCTCP, delegated credentials, SSLKEYLOGFILE, the WebAuthn algorithm registrations, and hybrid ML-KEM TLS — codifying what already ships is often the signal that a technology has crossed over.
