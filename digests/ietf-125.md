<!--
conference: IETF 125 (Shenzhen)
type: standards
source_url: https://datatracker.ietf.org/meeting/125/agenda.json
generated: 2026-11-01
registry_key: ietf-125
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 125 (Shenzhen) — Digest for the Networking & Identity PM

**A note on sources and depth.** The program entries below carried no author/affiliation lists and no paper, slide, or recording links, and nothing further was retrievable — every write-up is therefore **based on the program abstracts only**. Maturity signals (WG document vs. individual draft) are inferred from the draft names: `draft-ietf-<wg>-…` denotes a working-group document; `draft-<author>-<wg>-…` denotes an individual submission not yet adopted. The IETF 125 session schedule itself was not itemized per draft, so session timing should be confirmed on the Datatracker agendas for each WG (rift, bess, nvo3, rtgwg, tcpm, quic, savnet, grow, wimse, oauth, tls, lamps, cose).

## Core — Physical DC networking, overlays, and transport

- **RIFT: Routing in Fat Trees** (`draft-ietf-rift-rift`) — WG draft, rift.

  **Why:** The only IETF routing protocol purpose-built for Clos/fat-tree IP fabrics. If the PM owns physical DC fabric design, this is the standards-track event of the cycle for that domain.

  **What:** A dynamic routing protocol specialized for Clos and fat-tree topologies (and variants), optimized first for minimizing control-plane state so very large substrates are feasible, and second for minimizing configuration and operational complexity.

  **How:** Rather than being a general-purpose IGP, the protocol is specialized to the structure of fat trees — topology-derived behavior replaces generic link-state machinery and per-node configuration, which is where the state and config minimization comes from. The draft also notes these topologies descend from crossbar/backplane interconnects, now applied to IP fabrics.

  **Where applicable:** Leaf-spine / fat-tree DC fabrics at large scale. Not a general topology protocol — its specialization is the trade. Broadly applicable to any operator building Clos fabrics; it is a long-running WG document, i.e., mature in process.

- **Secure EVPN** (`draft-ietf-bess-secure-evpn`) — WG draft, bess.

  **Why:** EVPN is already pervasive across DC, SP, and enterprise segments. This draft changes the security properties of DC inter-site and WAN connectivity: tenant traffic gets IPsec-grade privacy/integrity/auth over the public Internet, without the operational cost of IKEv2.

  **What:** A mechanism that leverages BGP point-to-multipoint signaling to exchange keys and policy among PE devices, creating private pairwise IPsec Security Associations — with no IKEv2 point-to-point signaling and no other direct peer-to-peer session establishment.

  **How:** The existing BGP/EVPN control plane doubles as the key- and policy-distribution plane; SAs are derived per PE pair from BGP-distributed material rather than negotiated over per-tunnel IKE sessions.

  **Where applicable:** EVPN-based fabric overlays needing inter-site/WAN connectivity over public or untrusted infrastructure. Requires an EVPN PE deployment to ride on; otherwise broadly applicable across the DC and enterprise segments named in the draft.

- **Interconnect Solution for EVPN Overlay Networks** (`draft-ietf-bess-dci-evpn-overlay`) — WG draft, bess.

  **Why:** This is the DC/WAN seam itself — how Network Virtualization Overlay (NVO) datacenters extend tenant L2 into a WAN. Directly in the PM's DC-to-WAN interconnect territory.

  **What:** Specifies how EVPN-overlay NVO networks interconnect with WAN L2VPN technologies (VPLS, PBB-VPLS, EVPN, PBB-EVPN), how EVPN routes are processed on the interconnecting gateways, and the Interconnect Ethernet Segment (I-ES) for multihoming across that boundary. Also specifies the Unknown MAC Route (UMR) to avoid MAC-table scale problems on Data Center NVE devices.

  **How:** Gateway route-processing rules plus the I-ES construct extend EVPN multihoming semantics across the overlay/MPLS boundary; UMR lets NVEs avoid learning every remote MAC.

  **Where applicable:** Any deployment where EVPN-overlay DCs must hand off to MPLS-based or VPLS-based WANs — the classic DCI case. Protocol-level work, generally applicable, and a long-running WG document.

- **Geneve: Generic Network Virtualization Encapsulation** (`draft-ietf-nvo3-geneve`) — WG draft, nvo3.

  **Why:** Geneve is the encapsulation behind modern DC overlays (notably OVS-based stacks). Its defining feature — the extensible option header — is the wire-format surface every overlay endpoint, software or hardware, has to agree on.

  **What:** An encapsulation protocol designed for flexibility: it recognizes that tunnels tie together software tunnel endpoints, hardware endpoints, transit fabrics, and centralized control clusters, and it accommodates those changing capabilities via options rather than new tunnel types.

  **How:** Extensible, TLV-style option headers carried in the encapsulation let new capabilities (the abstract cites the general case of evolving endpoints and controllers) be added without redefining the base protocol.

  **Where applicable:** NVO3-style overlays spanning heterogeneous endpoint types; broad and vendor-neutral. WG document, i.e., moving with WG consensus behind it.

- **VXLAN: A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks** (`draft-ietf-nvo3-rfc7348bis`) — WG draft, nvo3.

  **Why:** Less a technical change than a governance one with real wire-format consequences: this moves the industry's most-deployed overlay encapsulation from an informational RFC (7348) into the IETF stream, opening the door to registered VXLAN header extensions.

  **What:** Obsoletes RFC 7348. The format and processing are fully compatible with the deployed protocol; what changes is stewardship — the spec becomes an IETF document so extensions requiring header additions can be standardized and registered with IANA.

  **How:** Re-publication on the IETF stream with explicit extension/IANA machinery; no behavioral change to existing packets.

  **Where applicable:** Every cloud-provider and enterprise DC running VXLAN today. Watch this if you care about future header extensions (e.g., new telemetry or security bits) landing in a standardized way.

- **Use of BGP for Routing in Large-Scale Data Centers** (`draft-ietf-rtgwg-bgp-routing-large-dc`) — WG draft, rtgwg.

  **Why:** The canonical write-up of running BGP as the *only* routing protocol in datacenters supporting 100,000+ servers — the design pattern behind eBGP DC fabrics that the PM's BGP/datapath work touches daily.

  **What:** An operational-experience document (informational) summarizing a proven, stable BGP-only routing design for large-scale DCs, where requirements emphasize operational simplicity and network stability above all.

  **How:** Reports design and operating practice at scale rather than specifying new protocol machinery — the value is the documented, replicable design.

  **Where applicable:** Large-scale DCs specifically; smaller infrastructures are explicitly out of scope by the draft's own framing. Broadly applicable as a design reference.

- **Data Center TCP (DCTCP)** (`draft-ietf-tcpm-dctcp`) — WG draft, tcpm.

  **Why:** The foundational ECN-based congestion control for DC traffic — high burst tolerance, low latency, and high throughput over shallow-buffered switches. This sits at the heart of low-latency DC transport, adjacent to the lossless/RDMA fabric work the PM tracks.

  **What:** An informational RFC documenting DCTCP as currently implemented by several major operating systems: it extends ECN processing to estimate the *fraction* of bytes encountering congestion (not merely that congestion occurred) and scales the congestion window on that estimate.

  **How:** Fine-grained ECN marking interpretation at the receiver produces a multi-bit-equivalent congestion signal from single-bit marks; the sender scales cwnd by the measured fraction.

  **Where applicable:** Controlled environments like datacenters only — the draft is explicit that DCTCP must not be deployed over the public Internet without additional measures. It also candidly covers coexistence with conventional TCP and the lack of a sender/receiver negotiation mechanism, with mitigations. Deployment guidance as much as protocol.

- **More Accurate ECN (AccECN) Feedback in TCP** (`draft-ietf-tcpm-accurate-ecn`) — WG draft, tcpm.

  **Why:** A genuine TCP wire-format change, and the enabling layer for DCTCP-class and L4S-class congestion control: original RFC 3168 ECN allows only one feedback signal per RTT, which is too coarse for these mechanisms.

  **What:** An update to RFC 3168 specifying a scheme providing more than one ECN feedback signal per RTT in the TCP header itself, by allocating the reserved bit previously used for the ECN-Nonce and overloading the two existing ECN flags; the reclaimed space also feeds back the IP-ECN field seen at connection establishment. Optional supplementary feedback comes via two new TCP options (never on the SYN), and the document specifies middlebox treatment of the changed wire protocol.

  **How:** Header surgery on scarce TCP bits, with careful rules for what middleboxes must and must not do — the hard part of this work.

  **Where applicable:** Any TCP endpoint or middlebox path where finer ECN feedback matters (DC, and L4S more broadly). Note the ECN-Nonce bit is being repurposed — a compatibility consideration for anything that consumed the nonce.

- **Multi-segment SD-WAN via Cloud DCs** (`draft-dmk-rtgwg-multisegment-sdwan`) — **individual draft, not yet WG-adopted; early.**

  **Why:** A trust-property change for cloud interconnect: it lets a cloud backbone stitch together multiple SD-WAN segments while the cloud gateways never decrypt tenant payloads — relevant to both the PM's security and DC/WAN interconnect interests.

  **What:** A method in which SD-WAN CPEs use GENEVE (RFC 8926) to encapsulate already-IPsec-encrypted packets toward their nearest Cloud GW; the cloud backbone steers the encrypted payload to the egress Cloud GW, which forwards it to the destination CPE.

  **How:** Layering is the trick: GENEVE provides transport/routing over the cloud backbone around an inner IPsec layer that remains opaque end-to-end — no decrypt/re-encrypt at cloud gateways.

  **Where applicable:** SD-WAN CPE fleets plus a cloud-provider backbone; assumes a cloud GW fabric. Early-stage individual draft (draft-dmk-…), so treat as a proposal seeking traction in rtgwg, not consensus output.

- **QUIC-LB: Generating Routable QUIC Connection IDs** (`draft-ietf-quic-load-balancers`) — WG draft, quic.

  **Why:** QUIC's address migration (and the connection-ID rotation that protects against linkability) breaks classic 4-tuple L4 load balancers. This is the standard fix for LB infrastructure in front of QUIC — core cloud-native datapath plumbing.

  **What:** A standardized means of securely encoding routing information into server-issued connection IDs so that properly configured load balancers route migrated-address packets correctly; the structured CID format also lets CIDs self-encode their length to aid hardware offloads.

  **How:** The server embeds an encrypted/structured routing token in the CID; the LB decodes (or passfully trusts) that token instead of the 4-tuple, while clients still get fresh CIDs per address for linkability protection.

  **Where applicable:** Any load-balancer tier fronting QUIC servers — cloud LBs, appliances, and the config interface between server and LB. Broadly applicable; WG document.

## Core — Identity, authentication, and authorization

- **Workload Identity in a Multi System Environment (WIMSE) Architecture** (`draft-ietf-wimse-arch`) — WG draft, wimse.

  **Why:** The IETF's architecture for workload identity conveyance — the standards-track effort in the same space as SPIFFE/SPIRE, which the PM works with directly. This is the umbrella document the rest of the wimse cluster hangs off.

  **What:** An architecture for designing and standardizing protocols and payloads that convey workload identity and security-context information, where a workload is software executing for a specific purpose, potentially with multiple running instances.

  **How:** Defines the problem space and the protocol/payload design points for carrying identity and security context between systems; the companion WG document `draft-ietf-wimse-identifier` (see below) grounds the naming layer.

  **Where applicable:** Cloud and microservice deployments generally — multi-service, multi-cloud, multi-tenant by construction. Broadly applicable, not org-specific.

- **Workload Identifier** (`draft-ietf-wimse-identifier`) — WG draft, wimse.

  **Why:** The naming semantics of the whole WIMSE stack live here. Anyone integrating SPIFFE-style identity with token-based systems cares about exactly this: a canonical, interoperable workload identifier.

  **What:** Defines the Workload Identifier — a URI that uniquely identifies a workload within the context of a specific trust domain — embeddable in Workload Identity Credentials including X.509 certificates and JWT-based tokens.

  **How:** A URI format with defined semantics per trust domain, carried inside existing credential formats so authentication, authorization, and policy enforcement can key off one consistent identifier across diverse systems.

  **Where applicable:** Any system that must federate or consistently interpret workload identity across heterogeneous platforms. This is the interop layer between SPIFFE-IDs, X.509 SANs, and JWT subjects in practice.

- **WIMSE Workload Proof Token** (`draft-ietf-wimse-wpt`) — WG draft, wimse.

  **Why:** Closes the bearer-token replay gap in workload-to-workload communication: possession of a credential alone isn't proof the current request came from the key holder.

  **What:** The Workload Proof Token (WPT) — a mechanism for workloads to prove possession of the private key associated with their Workload Identity Token (WIT). The WPT is a signed JWT that binds the workload's authentication to a specific HTTP request, providing application-layer proof of possession.

  **How:** Per-request signed JWT proofs (DPoP-like binding, applied to workload credentials), designed to work alongside the WIT credential format from `draft-ietf-wimse-workload-creds` and combinable with other WIMSE protocols in multi-hop call chains.

  **Where applicable:** HTTP-based workload-to-workload and multi-hop call chains in any runtime environment covered by the WIMSE architecture — the mechanism is general, not tied to a specific platform.

- **OAuth 2.0 Client Assertion in Workload Environments** (`draft-ietf-wimse-workload-identity-bcp`) — WG draft, wimse.

  **Why:** Codifies the pattern the industry has converged on for containers: stop provisioning client secrets, federate the underlying platform's credentials as OAuth client assertions (RFC 7521, especially RFC 7523). This is the exact seam where platform workload identity meets OAuth — SPIFFE-to-OAuth in practice.

  **What:** A specification describing a meta flow (Section 3.1), security recommendations (Section 4), and concrete patterns (Appendix A) for using workload-platform credentials as assertions toward an OAuth authorization server instead of manually provisioned client_id/client_secret pairs.

  **How:** The RFC 7521/7523 client-assertion flow, with platform-issued credentials (the WIMSE credential family) as the assertion, plus BCP-level guidance on doing it safely.

  **Where applicable:** Container orchestration systems of any kind fronted by an OAuth AS. Broadly applicable; this is best-practice codification of a deployed pattern, not a new protocol.

- **AI Identity Management System (AIMS)** (`draft-ietf-wimse-aims`) — WG draft, wimse; early-stage.

  **Why:** The IETF's first WG draft squarely aimed at agentic identity — the PM's explicit interest. Notably, it chooses reuse over new protocol invention.

  **What:** Best practices for authentication and authorization of AI agent interactions, built by applying/extension of existing standards — the WIMSE architecture and the OAuth 2.0 family — rather than defining new protocols; it also identifies gaps and is intended to guide future standardization.

  **How:** Framework-and-gap-analysis approach: map agent authn/authz onto WIMSE workload identity and OAuth machinery, then use the identified gaps to steer what gets standardized next.

  **Where applicable:** Agent-to-service and agent-to-agent interactions generally. Early in its lifecycle, so expect it to be a framing document rather than a deployable spec this cycle.

- **The OAuth 2.1 Authorization Framework** (`draft-ietf-oauth-v2-1`) — WG draft, oauth.

  **Why:** The baseline refresh of the single most-deployed authorization framework on the internet. Wherever OAuth 2.1 lands, every AS, client, and RS implementation eventually moves relative to it.

  **What:** Consolidates the OAuth 2.0 Authorization Framework (RFC 6749) and Bearer Token Usage (RFC 6750) into one specification that replaces and obsoletes both.

  **How:** Re-publication and consolidation under one document — the substance is in which errata, security practices, and deprecations get baked in; the abstract frames it as enabling limited access to protected resources on behalf of, or on behalf of itself for, the application.

  **Where applicable:** All OAuth deployments, everywhere. This is the reference point, not an option.

- **OAuth 2.0 Demonstrating Proof of Possession (DPoP)** (`draft-ietf-oauth-dpop`) — WG draft, oauth.

  **Why:** Sender-constrained tokens are the practical middle ground between bearer tokens and full mTLS sender binding; DPoP is the mechanism most OAuth stacks are adopting for replay-resistant tokens.

  **What:** A mechanism for sender-constraining OAuth 2.0 tokens via an application-level proof-of-possession, allowing detection of replay attacks with access and refresh tokens.

  **How:** The client proves possession of a key per use (per-request proofs bound to the token), so a stolen bearer string alone is useless.

  **Where applicable:** Any OAuth 2.0 deployment; the mechanism is defined at the application level, deliberately independent of transport-layer (mTLS) binding. General technique, no environment constraints.

- **Transaction Tokens** (`draft-ietf-oauth-transaction-tokens`) — WG draft, oauth.

  **Why:** The multi-hop problem — a request entering a trust domain must carry user identity, workload identity, and authorization context coherently through the whole call chain. This is the OAuth-side counterpart to the WIMSE work above.

  **What:** Transaction Tokens (Txn-Tokens) maintain and propagate user identity, workload identity, and authorization context throughout the call chain within a trusted domain, during processing of external requests (e.g., API calls) or internally initiated requests.

  **How:** Short-lived, chained tokens issued along the call chain carrying the combined identity/authz context, ensuring it is preserved and consistent across services.

  **Where applicable:** Complex multi-service architectures *within* a trusted domain — note the trust-domain boundary in the design; this is not an inter-domain federation mechanism. Complementary to WIMSE's proof-token work.

- **Delegated Credentials for TLS and DTLS** (`draft-ietf-tls-subcerts`) — WG draft, tls.

  **Why:** Changes who controls certificate lifetime, usage, and algorithm policy: the operator, not the CA. Matters for short-lived-credential strategies and for shrinking the blast radius of key compromise.

  **What:** A mechanism that overcomes the limitations created by organizational separation between TLS/DTLS endpoint operators and the CA — whose policy ultimately determines certificate lifetimes, usage, and supported algorithms — by letting operators delegate their own credentials for use in TLS and DTLS.

  **How:** A delegated credential signed by the operator's certificate that the endpoint can then use in the handshake; designed to remain compatible with peers that do not support the extension.

  **Where applicable:** TLS/DTLS server deployments where CA policy is too coarse — large operators running their own fleets under a CA they don't fully control. Broadly applicable to any TLS implementation once supported on both ends.

## Adjacent — Useful context, near-term influence

- **Topology Independent Fast Reroute using Segment Routing (TI-LFA)** (`draft-bashandy-rtgwg-segment-routing-ti-lfa`) — individual draft, not WG-adopted.

  **Why:** Sub-second local repair is table stakes in the WAN/interconnect segments the PM touches; TI-LFA is the widely implemented SR answer with guaranteed coverage. Interesting as a standards signal: heavily deployed in shipped silicon/OS but still an individual draft.

  **What:** Topology-Independent LFA: fast reroute for node and adjacency segments in the Segment Routing framework, extending proven IP-FRR concepts (LFA, RLFA, DLFA) to guarantee coverage in any IGP network.

  **How:** The key design choice is that the FRR path selection establishes protection over the *post-convergence* path from the point of local repair — so the backup path is the path routing will converge to anyway, dramatically reducing the need to tune tie-breaks among FRR options.

  **Where applicable:** SR-enabled IGP networks — service-provider WAN and large enterprise cores rather than the DC fabric itself. Broadly applicable within that scope.

- **Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)** (`draft-ietf-sidrops-bar-sav`) — WG draft, savnet.

  **Why:** Interdomain security hardening: robust source-address validation filters built from data operators already have (BGP, RPKI). Part of the ASPA wave reshaping routing-security practice.

  **What:** A method for deriving more robust SAV filters that minimizes false positives (not blocking legitimate traffic) while maintaining directionality per RFC 8704; it updates RFC 8704 and combines BGP UPDATE messages, ASPA, and ROA data.

  **How:** Uses the AS-level and origin-level information in BGP/ASPA/ROA records to compute what legitimately *originates* where, producing directionally correct ingress filters.

  **Where applicable:** Network-operator edge filtering at interdomain boundaries; general technique, though its quality depends on ASPA/ROA adoption in the relevant address space.

- **Updated BGP Operations and Security** (`draft-fiebig-grow-bgpopsecupd`) — individual draft in GROW.

  **Why:** A refresh of the canonical BGP security BCP (RFC 7454) is directly useful to the PM's BGP practice — it aggregates a decade of drift in operational practice into one reference.

  **What:** An update to RFC 7454 that reiterates its best practices and adds new ones: session protection (TTL/hop limits, TCP-AO, control-plane filtering), routing-information control (prefix and max-prefix filtering, AS-path filtering, route flap dampening, BGP community scrubbing), plus new material on terminology alignment with RFC 9234, revised IXP LAN prefix recommendations, ASPA and BGP roles, filter generation/evaluation practices for performance, in-depth outbound and internal filtering, global prefix limits, and community-based filtering for downstream prefixes.

  **How:** Best-current-practice document — codifies operator practice rather than specifying protocol.

  **Where applicable:** Any BGP operator, DC or otherwise. Individual draft, so still moving through GROW rather than settled consensus.

- **Managing multiple paths for a QUIC connection** (`draft-ietf-quic-multipath`) — WG draft, quic.

  **Why:** Standardized multipath for QUIC affects client connectivity (multi-interface), and increasingly the path-selection machinery that cloud-native and edge systems will build on. Also a useful datapoint on the QUIC ecosystem's modular growth.

  **What:** A QUIC extension enabling simultaneous use of multiple paths for a single connection, via explicit path identifiers to create, delete, and manage paths. Deliberately scoped: it does not specify address discovery/management, nor how applications schedule traffic across paths.

  **How:** Path IDs decouple path management from address handling, letting connection state span multiple network paths while leaving policy (scheduling, discovery) to the application or higher layers.

  **Where applicable:** QUIC implementations generally; deployment value shows up wherever multiple interfaces/paths exist (mobile, multi-homed edge). The explicit non-goals mean ecosystems will differentiate above this layer.

## Wildcard

- **Updates to X.509 Policy Validation** (`draft-ietf-lamps-x509-policy-graph`) — WG draft, lamps.

  **Why:** A quiet but important fix to a real vulnerability class: the RFC 5280 certificate-policy validation algorithm is worst-case exponential, and implementations have been DoS-able through it. If the PM touches any path-validating PKI component, this is the correction their libraries need.

  **What:** Replaces the RFC 5280 X.509 policy-validation algorithm with an equivalent but efficient one — same validation results, polynomial-time structure.

  **How:** Reformulates the policy tree/graph computation so worst-case complexity no longer explodes; "equivalent" meaning implementations can adopt it without changing validation outcomes.

  **Where applicable:** Every conforming X.509 path-validation implementation — broadly applicable by definition.

- **QMux** (`draft-ietf-quic-qmux`) — WG draft, quic.

  **Why:** A genuinely novel reuse play: take QUIC's stream/datagram API and run it over ordinary TLS streams — "QUIC semantics without the QUIC transport." Signals where the field is heading: protocol *APIs* becoming portable across transports.

  **What:** QMux version 1 provides, over bi-directional streams such as TLS, the same set of stream and datagram operations applications rely on in QUIC version 1.

  **How:** Re-implements the QUIC stream/datagram state machine atop a byte-stream transport instead of UDP, with development tracked publicly on the QUIC WG GitHub (`quicwg/qmux`) and the quic@ list.

  **Where applicable:** Environments where UDP is unavailable, blocked, or poorly handled (middlebox-hostile networks, some managed runtimes) but applications want QUIC-like multiplexing semantics. Watch what adopts it.

- **COSE Receipts** (`draft-ietf-cose-merkle-tree-proofs`) — WG draft, cose.

  **Why:** Generalizes the transparency idea behind certificate transparency into a compact, reusable cryptographic building block — Merkle-based proofs in COSE/CBOR. This is the plumbing future "token transparency" or supply-chain attestation systems are likely to be built on, including for identity workloads.

  **What:** COSE Receipts prove properties of a verifiable data structure to a verifier, enabling security properties such as minimal disclosure, transparency, and non-equivocation; the draft demonstrates the extensibility by providing CBOR encodings for Merkle inclusion and consistency proofs.

  **How:** Standard COSE structures carrying Merkle-tree proofs (inclusion: "this item is in the set"; consistency: "the set only grew"), letting a verifier check guarantees without seeing the whole structure.

  **Where applicable:** Transparency-oriented systems generally — the abstract cites certificates, end-to-end encrypted messaging, and supply-chain security as prior applications. A general building block, not org-specific.

## Themes

- **Workload and agentic identity is the largest single cluster in this selection.** The WIMSE suite (architecture, identifier, proof token, OAuth client-assertion BCP) is maturing as WG documents, and AIMS arrives *on top of* WIMSE rather than inventing new protocols — a strong signal that agentic identity will be standardized as workload identity plus policy, not as a parallel universe.

- **The identity cluster's center of gravity is shifting from bearer to proof-of-possession and richer context propagation.** DPoP, WPT, and Transaction Tokens all attack replay and context loss from different layers; expect them to be composed in practice.

- **The datacenter is becoming standards-track territory.** RIFT, Geneve, the VXLAN re-publication, and DCTCP are all long-deployed technologies being brought under IETF change control — which matters less for today's packets than for who governs tomorrow's header extensions.

- **Congestion signaling is getting more precise.** DCTCP (estimate the congested fraction) and AccECN (feed back more than one mark per RTT) together form the substrate for low-latency DC transport and L4S; AccECN's TCP header changes and middlebox rules are the deployment bottleneck to watch.

- **EVPN is hardening into the universal DC/WAN glue — including its security model.** Secure EVPN replacing IKEv2 point-to-point signaling with BGP key/policy distribution changes the trust topology of inter-site connectivity; the DCI overlay draft covers the corresponding L2-interconnect mechanics.

- **Interdomain hygiene keeps grinding forward:** BAR-SAV, ASPA integration, and the BGP opsec refresh show routing-security practice consolidating around RPKI-derived data — plus a reminder that TI-LFA, despite being broadly implemented, is still an individual draft.
