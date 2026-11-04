<!--
conference: IETF 125 (Shenzhen)
type: standards
source_url: https://datatracker.ietf.org/meeting/125/agenda.json
generated: 2026-11-01
registry_key: ietf-125
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 125 (Shenzhen)

A standards meeting: the substance is in the drafts, and the signal is in what is moving toward adoption. This cycle is dominated by two waves: **AI/ML Ethernet fabrics** (adaptive routing, sub-100µs fast reroute, lossless DCN+WAN flow control, multicast for collectives) and **agentic identity** (OAuth transaction tokens, delegation chains, SPIFFE client auth, workload identity hints in TLS). Both are moving from individual drafts toward WG adoption.

## Core

### Fully Adaptive Routing Ethernet using BGP

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xu-idr-fare/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessb-4-1-fully-adaptive-routing-ethernet-using-bgp-01) · [Session recording](https://youtu.be/yw6h3n-7qXE) · [Materials](https://datatracker.ietf.org/meeting/125/session/idr)

Qingliang Zhang (H3C), Hang Wu (Ruijie), Yadong Liu, Yinben Xia (Tencent), Peilong Wang (Baidu), Xiaohu Xu (China Mobile), Shraddha Hegde (HPE), Keyur Patel (Arrcus), Zongying He (Broadcom), et al.

- **Why**: Static ECMP in Clos fabrics breaks down for elephant-flow AI training traffic — collisions on equal-cost paths cost throughput exactly when a multi-thousand-GPU job is running. This is the most implementation-proven adaptive-routing item in the routing area.
- **What**: FARE extends BGP so that each node advertises real-time path bandwidth in a path-bandwidth extended community; receivers compute weighted ECMP (WECMP) next-hops and rebalance per the live capacity of each spine path. New in -04: multihoming handling — when a prefix is multihomed to N leaf nodes, the advertised path bandwidth is divided by N (or the local link bandwidth multiplied by N) before taking the minimum, so weights stay honest.
- **How**: Leaf takes min(local link bandwidth, advertised path bandwidth) as the route weight for weighted load-balancing; congestion or link-state changes propagate via ordinary BGP updates carrying the bandwidth community. The slides state the draft is ready for WG adoption call.
- **Where applicable**: Broadly applicable to scale-out IP fabrics — implemented by at least 2 cloud providers (China Mobile Cloud, Baidu Cloud) and 5+ vendors, adapted to four mainstream merchant switch chips including Broadcom Tomahawk 5, Nvidia Spectrum-4, HiSilicon SD58XX, and Centec Arctic. Ethernet Clos fabrics only; not a WAN mechanism.

### Fully Adaptive Routing Ethernet in Scale-Up Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xu-rtgwg-fare-in-sun/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-06-xu-fare-in-sun-01) · [Session recording](https://youtu.be/nzitn4M1Tc8) · [Materials](https://datatracker.ietf.org/meeting/125/session/rtgwg)

Yongtao Yang (Centec), Yinben Xia, Weifeng Zhang (Tencent), Peilong Wang (Baidu), Yan Zhuang (Huawei), Xiaohu Xu (China Mobile), Zongying He (Broadcom), Nan Wang (Intel, Hygon), Jian Guo (Biren), Xiang Li (Enflame), et al.

- **Why**: The same WECMP idea moved into the scale-up (GPU back-end) network, where MoE expert/tensor parallel traffic is low-entropy, bursty, and collision-prone across multi-plane topologies — and the GPU itself becomes a routing participant. This is where physical fabric design and GPU interconnect are converging (OCP ESUN, AMD UALoE, Broadcom SUE-T).
- **What**: Extends FARE from switches to GPUs: each GPU has multiple 800G ports, at least one sub-port per scale-up plane, and performs per-flow or per-packet weighted load-balancing across planes using path-bandwidth feedback. New in -02: considerations for memory-semantic operations — weak ordering (full packet spray + GPU reorder buffers), strong ordering (in-order per QP), and partial ordering, selectable via the per-flow vs per-packet mode.
- **How**: Per-flow mode needs ≥1 RDMA queue pair per sub-port per GPU pair and per-flow switch balancing (ordered delivery); per-packet mode needs a single QP per GPU pair and spraying across planes (disordered delivery). Switches do matching weighted balancing.
- **Where applicable**: Ethernet-based scale-up networks specifically. A 64-GPU disaggregated SuperPod PoC over single-stage Clos is near completion; a 1024-GPU opto-electronic hybrid cascaded pod is under development. Co-authorship from GPU vendors (Intel, Hygon, Biren, Enflame) signals real hardware engagement, but this is early-stage (individual draft, -02).

### BGP Deterministic Path Forwarding (DPF)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-wang-idr-dpf/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-sessb-2-bgp-deterministic-path-forwarding-dpf-00) · [Session recording](https://youtu.be/yw6h3n-7qXE) · [Materials](https://datatracker.ietf.org/meeting/125/session/idr)

Kevin Wang, Michal Styszynski, Wen Lin, Mahesh Subramaniam, Thomas Kampa, Diptanshu Singh (Juniper)

- **Why**: Hop-by-hop EBGP gives every flow one best-effort service; AI/LLM flows, multi-tenant GPU-as-a-service SLAs, and PRP-style replication need path separation that plain IP fabrics don't offer. This is a lightweight traffic-engineering answer for IP fabrics.
- **What**: Partitions a physical Clos fabric into multiple logical fabrics by "coloring" EBGP sessions and routes. Use cases shown: queue-pair pinning for ROCEv2 (pinning QPs to disjoint paths), per-tenant SLA separation for GPU-as-a-service, and fate-sharing avoidance (exception flows and PRP redundant flows mapped to different logical fabrics).
- **How**: Each EBGP session carries a color community; a route is only accepted over a session of matching color (uncolored routes match any). A new SESSION-COLOR capability in the BGP OPEN negotiates color, in strict mode (early misconfiguration detection, session flaps on color change) or loose mode (no flap, late detection). Coloring modes: primary-only, primary+backup (AIGP makes backup劣 — backup paths carry AIGP so primary wins), primary+all-backups (the QPP mode), and all-colors ECMP with firewall-filter flow mapping.
- **Where applicable**: Any EBGP Clos fabric (RFC 7938 style). Individual draft (-00) presented at IDR — early, no adoption signal yet; vendor-driven (Juniper) with concrete switch-level use cases.

### BGP Link-State Extensions for BGP-only Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-bgp-only-fabric/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-idr-bgp-link-state-extensions-for-bgp-only-networks-00) · [Session recording](https://youtu.be/a0BiAUtfF4c) · [Materials](https://datatracker.ietf.org/meeting/125/session/idr)

Ketan Talaulikar (independent), Aravind Babu MahendraBabu, Clarence Filsfils, Krishna Swamy (Cisco), Shawn Zandi (LinkedIn), Gaurav Dawra, Muhammad Durrani (Equinix)

- **Why**: In BGP-only DC/AI fabrics, nodes have no visibility beyond direct neighbors — which blocks LFA/TI-LFA computation, remote protection, and controller TE. This draft is the enabler several other RTGWG/IDR drafts depend on, including the IPFRR-for-AI/ML draft below.
- **What**: A WG draft (draft-ietf-idr-bgp-ls-bgp-only-fabric-04, adopted by IDR) that lets each BGP speaker advertise its local topology via existing BGP-LS NLRI types (Node, Link, Prefix), giving controllers a full underlay link-state and TE view in networks with no IGP.
- **How**: Reuses existing BGP-LS descriptors and attribute TLVs (link bandwidth, SR adjacency SIDs, affinities, TE metric, SR prefix SIDs); adds one new BGP Route Type TLV in the Prefix Descriptor. Works via route-reflector distribution to controllers or a centralized BGP-LS collector; the base eBGP underlay is untouched.
- **Where applicable**: BGP-only fabrics — DC/MSDN per RFC 7938 and emerging AI DC networks. The draft focuses on eBGP single-hop peering; other models not precluded. Implementations in progress; code-point allocation requested. Directly feeds draft-clad-rtgwg-ipfrr-aiml and efficient-remote-protection.

### IP Fast Reroute for AI/ML Fabrics

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-clad-rtgwg-ipfrr-aiml/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-07-ip-fast-reroute-for-aiml-fabrics-00) · [Session recording](https://youtu.be/nzitn4M1Tc8) · [Materials](https://datatracker.ietf.org/meeting/125/session/rtgwg)

Francois Clad, Clarence Filsfils (Cisco), Roy Jiang, Dennis Cai

- **Why**: AI backend networks lose huge compute value per millisecond of fabric failure; existing FRR (ECMP, LFA, TI-LFA) is CPU-activated and orders of magnitude too slow, plus it can't react to capacity/quality degradation (e.g., a failed bundle member or a down spine-to-super-spine path causing congestion rather than outage).
- **What**: A requirements document for sub-100µs convergence in AI DC fabrics and DCI: it enumerates the limits of RFC 5714 mechanisms in large multi-tier Clos and BGP-only fabrics, and lays out what a replacement needs.
- **How**: Four requirements: (1) hardware-accelerated protection activation using extended NPU capabilities without CPU intervention; (2) hardware-accelerated network notifications (the FANTEL discussion, draft-ietf-rtgwg-net-notif-ps, draft-camarillo-rtgwg-lsn); (3) complete topology visibility via BGP-LS in BGP-only fabrics (the draft above); (4) quality-aware remote protection — reacting to remote degradation by adjusting ECMP weights or using repair paths outside the ECMP set (solution sketched in draft-clad-rtgwg-efficient-remote-protection).
- **Where applicable**: Scale-out AI backend networks (2/3-tier folded Clos, multi-plane/multi-rail, eBGP) and scale-across DCI; scale-up explicitly deferred. Requirements stage — individual draft seeking WG feedback; this is the umbrella over several companion solution drafts rather than a deployable mechanism itself.

### EVPN Fast Notification and Handling for Multihoming

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-zzhang-bess-evpn-mh-fast-notification/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-bess-evpn-mh-fast-notification-01) · [Session recording](https://youtu.be/hr5963eGggU) · [Materials](https://datatracker.ietf.org/meeting/125/session/bess)

Jeffrey Zhang, Wen Lin (HPE), Changwang Lin (H3C)

- **Why**: EVPN multihoming (DF election, local bias) assumes the Ethernet Segment type-4 route is withdrawn and processed quickly on link failure. BGP update propagation over TCP between routing engines isn't quick — delayed handling means traffic loss (DF down) or duplication (link-up local-bias lag). Per-<PE, ES> BFD doesn't scale.
- **What**: A UDP-based data-plane notification originated and processed in the forwarding plane of MH peers, (near-)instantly updating DF-election/local-bias state without waiting for the BGP control plane. Optionally also notifies all remote PEs (useful for single-active backup switchover and load-balancing rebalance), preferring multicast for the notification address unless the PE count is small.
- **How**: UDP messages sent from the failing PE's forwarding plane to peers' forwarding planes, several sent back-to-back to compensate for UDP loss; fully independent of control-plane signaling, no EVPN protocol changes in the data plane, all local behavior — hence no interop issues.
- **Where applicable**: EVPN multihoming deployments generally (All-Active and Single-Active). Individual draft, early — authors are collecting comments before an adoption request; complements time-synchronized DF election (RFC 9722).

### Requirements and Gap Analysis of Multicast in AI Data Centers

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-zhang-rtgwg-multicast-requirements-gaps-aidc/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-09-requirements-and-gap-analysis-of-multicast-in-ai-data-centers-00) · [Session recording](https://youtu.be/nzitn4M1Tc8) · [Materials](https://datatracker.ietf.org/meeting/125/session/rtgwg)

Junye Zhang, Weiqiang Cheng, Kefei Liu (China Mobile)

- **Why**: MoE token dispatch (AlltoAll), AllReduce broadcast phases, model distribution, and checkpoint saving are all point-to-multipoint; unicast replication burns source GPU/NIC capacity and bandwidth. If network multicast could serve AIDCs, it would offload replication to switches — but no existing multicast tech fits.
- **What**: A requirements-and-gap document. Requirements: interactivity (backward MP2P forwarding and ACK/congestion-feedback aggregation), reliability (lossless — RDMA throughput collapses to 0 at ~2% loss), dynamics (µs-scale member-set adaptation for MoE gating, no pre-defined groups), sparseness (e.g., 9 of 256 experts active in DeepSeekV3 — no BIER BitString bloat), and simplicity.
- **How**: Gap analysis: PIM/MLDP convergence too slow and too complex; SR-P2MP needs global recalculation; BIER relatively good on dynamics/simplicity but BitString overhead hurts sparse membership; none handle MP2P feedback or losslessness. Conclusion: a new architecture or deep enhancement of existing multicast is needed for AIDCs.
- **Where applicable**: AIDC scale-out fabrics. Individual gap-analysis draft (-00) seeking feedback — this is a problem statement that could charter new work rather than a solution; useful for the PM to anticipate where multicast requirements are heading.

### Use cases and Requirement for Flow Control Collaboration Across DCNs and WAN

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-han-rtgwg-codeployment-pfc-fgfc/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-07-use-cases-and-requirement-for-flow-control-collaboration-across-dcns-and-wan-00) · [Session recording](https://youtu.be/nzitn4M1Tc8) · [Materials](https://datatracker.ietf.org/meeting/125/session/rtgwg)

Zhengxin Han, Ran Pang, Yi Yue, Jie Dong, Zheng Ruan, Quan Xiong (China Unicom)

- **Why**: Distributed AI training and inference now span data centers over WAN, but PFC — the DCN lossless mechanism — fails badly in WANs: head-of-line blocking, congestion spreading, and deadlock under multipathing, with long RTTs amplifying everything. Extending lossless RDMA end-to-end across DCN+WAN requires the two flow-control regimes to interwork.
- **What**: Use cases and requirements for co-deploying PFC inside DCNs with fine-grained flow control (fgfc) in the WAN: fgfc is a data-plane L3 backpressure mechanism (carried in ICMPv6 or UDP) operating at tenant/flow granularity, bounded to specific paths and slices, with ms-level response.
- **How**: Edge gateways (R1/R5 in the examples) do bidirectional translation: DCN PFC pause → fgfc packet (priority, slice ID, pause time) upstream; WAN fgfc → standard PFC frame toward the DC. Requirements on edge nodes: PFC↔fgfc protocol conversion, port-level↔tenant/flow-level semantic mapping, policy coordination, slicing and HQoS support, buffer management. Supports both hop-by-hop and tunneled cross-hop WAN backpressure for legacy intermediate nodes.
- **Where applicable**: DC-interconnect WANs carrying RDMA/AI traffic. Field trials reported over 200+km (Hangzhou–Jinhua storage/compute separation training) achieving >95% computational efficiency with RDMA lossless over the WAN — operator-specific (China Unicom) evidence but the mechanism is general. Individual requirements draft, seeking review.

### Encapsulating IPsec ESP in UDP for Load-balancing

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xu-ipsecme-esp-in-udp-lb/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-ipsecme-encapsulating-ipsec-esp-in-udp-for-load-balancing-00) · [Session recording](https://youtu.be/-0_gLUb5r3c) · [Materials](https://datatracker.ietf.org/meeting/125/session/ipsecme)

Xiaohu Xu (China Mobile), Shraddha Hegde (HPE), Boris Pismenny (Nvidia), Dacheng Zhang, Liang Xia (Huawei), Mahendra Puttaswamy (HPE)

- **Why**: ESP has no entropy, so IPsec tunnels hash onto one ECMP path / one LAG member and one CPU core (no RSS spread). For SD-WAN branch interconnects and, increasingly, cloud-provider encryption of DCI WAN traffic (financial/governmental clouds), this strands bandwidth and CPU.
- **What**: A UDP encapsulation of ESP where the 16-bit UDP source port carries a per-flow entropy value, letting unmodified switches and routers load-balance IPsec traffic across ECMP/LAG, and letting x86 IPsec gateways RSS-distribute across cores. Alternative to running multiple parallel tunnels.
- **How**: Standard UDP encapsulation with source-port-as-entropy; no changes required in transit switches or core routers. The slides state it is implemented by vendors (Juniper/HPE cited) and the draft (-15) is ready for WG adoption call.
- **Where applicable**: Broadly applicable — enterprise SD-WAN, cloud DCI encryption, multi-core IPsec gateways. Mature individual draft on the edge of WG adoption; the closest to shipping of the security items here.

### Deprecating IPv6 Extension Headers on the Internet

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-herbert-deprecate-eh/) · [Session recording](https://youtu.be/A1QUaZ9HG9o) · [Materials](https://datatracker.ietf.org/meeting/125/session/6man)

Tom Herbert (individual)

- **Why**: Measurement shows packets carrying IPv6 extension headers are discarded at high rates across the public Internet, EHs enable DoS amplification and carry known vulnerabilities, and the loss rates deter anyone from deploying new EHs at all. For anyone operating both a limited domain (DC) and Internet-facing paths, this decides whether EH-based mechanisms (e.g., SRH) are ever viable outside the domain.
- **What**: Recommends deprecating all IPv6 extension headers on the public Internet except ESP: relegate them to limited domains and discard EH-carrying packets at domain boundary routers — essentially formalizing what operators already do (from abstract only).
- **How**: A recommendations document changing expectations about EH handling at domain boundaries rather than a wire-format change; motivated by discard-rate data, DoS vectors, and the chilling effect on new EH development.
- **Where applicable**: Internet-facing IPv6 globally; the carve-out for limited domains is what keeps SRv6/segment-routing DC fabrics unaffected. Note maturity carefully: this is an individual draft that was never adopted by 6man and has expired on the datatracker — treat it as a provocative position statement shaping the EH debate, not emerging consensus.

### The OAuth 2.1 Authorization Framework

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-identity-assertion-authorization-grant-00) · [Session recording](https://youtu.be/C72Saxe03tk) · [Materials](https://datatracker.ietf.org/meeting/125/session/oauth)

Dick Hardt (Hellō), Aaron Parecki (Okta), Torsten Lodderstedt (SPRIND)

- **Why**: OAuth 2.1 will be the baseline spec every identity product implements for the next decade. It obsoletes RFC 6749 and RFC 6750, folding a decade of security BCPs into one normative document — anything the PM ships that speaks OAuth will be measured against it.
- **What**: A consolidation of RFC 6749 (core), RFC 8252 (native apps), RFC 9700 (security BCP), and RFC 10017 (browser-based apps) into a single framework, removing features found insecure in RFC 9700 — the TOC confirms removal of the implicit grant, changes to the redirect URI parameter in token requests, and deeply reworked security considerations including mix-up defenses via issuer identification and distinct redirect URIs, sender-constrained tokens (DPoP, mTLS) promoted to SHOULD, and extensive native/browser app guidance.
- **How**: Same grant architecture (authorization code, refresh, client credentials, extension grants) with the insecure options deleted; supports both bearer and sender-constrained access tokens; explicitly HTTP-only.
- **Where applicable**: Universal for OAuth implementations. Maturity is high: WG document at -17 with a WG milestone of submission to IESG by Dec 2026. (Note: the slides link attached to this agenda item actually presents a different OAuth draft — the Identity Assertion Authorization Grant — so use the draft text itself.)

### Updates to OAuth 2.0 Security Best Current Practice

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-security-topics-update/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-updates-to-oauth-20-security-best-current-practice-00) · [Session recording](https://youtu.be/C72Saxe03tk) · [Materials](https://datatracker.ietf.org/meeting/125/session/oauth)

Tim Würtele, Pedram Hosseyni (University of Stuttgart), Kaixuan Luo (CUHK), Adonis Fung (Samsung Research America)

- **Why**: This documents two new real-world attack classes found in production OAuth ecosystems — including agentic AI token vaults — with 20+ and 40+ affected vendors respectively. If the PM builds anything with connector marketplaces, integration platforms, or agent toolkits, these attack classes apply directly.
- **What**: WG-adopted update to RFC 9700 covering: (1) audience injection attacks against client-authentication assertions, with attack mechanics and countermeasures (single audience value, issuer identifier, exact endpoint URI); (2) Cross-toolkit OAuth Account Takeover (COAT) — a malicious AS introduced via a connector/toolkit exploits mix-up defenses that don't work because issuer identifiers are unavailable, untrusted, or non-unique in practice (none of 20+ client vendors investigated applied issuer-based defenses); countermeasure: a client-assigned identifier for each toolkit, embedded in `redirect_uri`, matched at the client; (3) cross-user OAuth session fixation — platforms and AI token vaults introduce standalone auth sessions decoupled from the user-agent session, fixatable by sharing a request URL (Amazon Alexa, IFTTT, Microsoft Copilot, n8n, Perplexity, Manus, Bedrock AgentCore, Arcade.dev, Composio among 40+ affected); countermeasures are high-level (return to the origin where the original session lives; validate session binding), with concrete flows left to future profiling.
- **How**: BCP-format security analysis with per-attack threat models, generalized deployment scenarios (integration platforms, agent token vaults), and immediately applicable client-side mitigations.
- **Where applicable**: Every OAuth 2.0 deployment with multi-AS clients — especially connector/integration platforms and agentic token vaults. WG-adopted (-01); authors target WG last call after IETF 126.

### OAuth SPIFFE Client Authentication

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-oauth-spiffe-client-authentication-00) · [Session recording](https://youtu.be/C72Saxe03tk) · [Materials](https://datatracker.ietf.org/meeting/125/session/oauth)

Stian Thorgersen, Scott Rose, Pieter Kasselman, Arndt Schwenkschuster

- **Why**: This is the concrete SPIFFE↔OAuth bridge — exactly the workload-identity-meets-authorization intersection the PM owns. Workloads acting as OAuth clients today carry static client secrets in config files (the slides show Spring and JSON examples); this replaces them with automatically rotated SVIDs.
- **What**: WG-adopted draft (draft-ietf-oauth-spiffe-client-auth) profiling RFC 7521/7523 so JWT-SVIDs serve as OAuth client-assertion credentials, X.509-SVIDs ride RFC 8705 mTLS client auth, and — new since IETF 124 — WIT-SVIDs (WIMSE workload identity tokens) fit the attestation-based client-auth draft, with key possession where applicable. New `token_endpoint_auth_methods_supported` values: `spiffe_jwt`, `spiffe_x509`, `spiffe_wit`.
- **How**: The AS fetches SPIFFE trust bundles via the SPIFFE Bundle Endpoint (JWKS, RFC 7517) for SVID validation; trust establishment and client registration are prerequisites (enterprise environments typically require registration anyway). Works for 2-legged (client credentials) and 3-legged (auth code + PKCE) flows.
- **Where applicable**: Any environment running SPIFFE/SPIRE or managed workload identity (Entra Workload ID, Google Managed Workload Identity; deployed at Uber, Netflix, ByteDance, etc.). Keycloak 26.4 ships a preview implementation; an MCP-OAuth client-auth demo exists. The strongest "adopt and implement soon" signal in the identity set.

### Cryptographically Verifiable Actor Chains for OAuth 2.0 Token Exchange

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-mw-spice-actor-chain/) · [Session recording](https://youtu.be/T43MLoaWsbI) · [Materials](https://datatracker.ietf.org/meeting/125/session/spice)

A Prasad, Ramki Krishnan, Diego Lopez (Telefónica), Srinivasa Addepalli (individual, SPICE WG)

- **Why**: Multi-hop service-to-service and agentic workflows need delegation-path continuity: RFC 8693 allows nested `act` claims but prior actors are informational only — nothing today cryptographically proves the chain of token exchanges that produced a token. That's the auditability gap for agent-driven API access.
- **What**: Six actor-chain profiles for RFC 8693 token exchange — Declared vs Verified, each in Full/Subset/Actor-Only disclosure variants — trading off visible chain-based authorization, cryptographic accountability, auditability, privacy, and long-running workflow support. `sub`, `act`, `may_act` semantics are preserved; plain RFC 8693 impersonation-shaped outputs remain valid but sit outside the profile family (from abstract only).
- **How**: Profiling of token-exchange outputs such that the delegation path is preserved and validated across successive exchanges, with per-profile processing rules (from abstract only).
- **Where applicable**: Same-domain and cross-domain delegation chains in service meshes and agentic workflows. Status caveat: presented in SPICE, but the individual draft (draft-mw-spice-actor-chain-05) has since expired and been replaced by draft-mw-oauth-actor-chain — the work is alive but moving to the OAuth WG; expect the successor document when tracking it.

### Agent-to-Agent (A2A) Profile for OAuth Transaction Tokens

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-liu-oauth-a2a-profile/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-a2a-profile-for-oauth-transaction-tokens-02) · [Session recording](https://youtu.be/C72Saxe03tk) · [Materials](https://datatracker.ietf.org/meeting/125/session/oauth)

Chunchi Peter Liu, Yuan Ni

- **Why**: Agent-to-agent call chains are exposed to goal hijack, context poisoning, and privilege abuse (per OWASP's agentic-AI top 10). Transaction Tokens (draft-ietf-oauth-transaction-tokens, at -08) already propagate user/workload identity and authorization context across service chains; this profiles them for the agent case.
- **What**: Extends Transaction Tokens from service-to-service to agent-to-agent, embedding A2A call-chain context — user and agent identity, authorization context, and A2A message structure (task_id, context_id, message_id, role, metadata) — as claims so identity and intent survive across distributed agent workloads.
- **How**: Uses the Tx Token claim set: `scope(purp)` as immutable transaction purpose, `tctx` for immutable chain details, `rctx` for changeable environmental context; A2A message fields map into these. Open design questions flagged for the WG: whether `scope` derives from the A2A `task_id` or the external access token, and whether a new claim carries A2A context or `rctx` is reused. A merger with draft-oauth-transaction-tokens-for-agents is under discussion.
- **Where applicable**: Trusted-domain multi-agent workflows. Early individual draft (-00/-02) — but Transaction Tokens themselves are mature, and this is one of the two live profiles competing to be the A2A identity mechanism; watch the consolidation.

### Agent Operation Authorization

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-liu-agent-operation-authorization/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-oauth-agent-operation-authorization-02) · [Session recording](https://youtu.be/C72Saxe03tk) · [Materials](https://datatracker.ietf.org/meeting/125/session/oauth)

Dapeng Liu, Suresh Krishnan

- **Why**: The sharpest articulation of OAuth's agent gap: OAuth grants broad permissions (`scope=write`), but prompt injection can steer an agent into malicious actions that are *within* the granted permission — permission ≠ behavior — and OAuth proves who the user is, not "agent X acting for user Y on task Z." This draft proposes binding behavioral policy plus delegation plus user-intent evidence into the access token.
- **What**: The Agent Operation Authorization (AOA) framework: a structured, machine-readable `agent_operation_proposal` (a JWT, deliberately excluding the user's natural-language input), validated by the AS into an Agent Operation Authorization Token that cryptographically binds user + agent instance + operation policy constraints (e.g., amount ≤ 50, time == "Nov 11 night"), enforceable at runtime by agents and verifiers — resisting both prompt injection and hallucinated parsing of intent.
- **How**: Tripartite binding via AS-signed evidence; trust model treats the LLM as untrusted, the agent runtime as trusted (signs requests), the AS as sole witness. Ecosystem fit: PAR, JWT, standard error codes; WIMSE workload identity for agent authentication; OPA/Rego for policy enforcement. Open-source implementation: Open Agent Auth (Alibaba), demoed at the IETF 125 hackathon.
- **Where applicable**: Any autonomous-agent platform calling protected APIs. Early individual draft — the authors are explicitly seeking WG consensus on the *problem* and on the shift from scope-based to policy-based authorization. Whether or not this exact design wins, the problem statement is the one to align products against.

### Workload Identifier Origin Hint for TLS ClientHello

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-tls-workload-identifier-origin-hint-00) · [Session recording](https://youtu.be/2GkmQmRlkto) · [Materials](https://datatracker.ietf.org/meeting/125/session/tls)

Yaroslav Rosomakho, Jonathan Hoyland (individual, TLS WG)

- **Why**: mTLS works well for workloads but there's no easy way to enable it on a shared endpoint — today you typically need a separate TLS server endpoint just to issue CertificateRequests. This extension lets a workload client signal mTLS capability and identity namespace in the ClientHello.
- **What**: A TLS ClientHello extension carrying a list of workload identifier origins (URI scheme + trust domain, e.g., the `spiffe://` scheme and trust-domain part of a SPIFFE ID). Presence of the extension tells the server the client (a) won't break on a CertificateRequest and (b) can present a certificate for one of the listed origins; the server uses the hint to decide whether client authentication is required and which policies/trust anchors apply.
- **How**: An optional origin list in the extension; an empty list degenerates into a pure "request mTLS" flag. For privacy, the list can be carried in the Inner ClientHello under ECH with an empty outer list, hiding identifier information from on-path observers.
- **Where applicable**: Machine-to-machine TLS deployments — SPIFFE/WIMSE-style workload identity, proxies, OT/IoT — not user-facing browsers. Early individual draft (-01) gauging TLS WG interest; complements SPIFFE client auth (OAuth layer) and the WIMSE effort.

### Use of Remote Attestation with Certification Signing Requests

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-lamps-csr-attestation/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-csr-attestation-00) · [Session recording](https://youtu.be/RyqnmLpaRBw) · [Materials](https://datatracker.ietf.org/meeting/125/session/lamps)

M. Ounsworth, H. Tschofenig, H. Birkholz, M. Wiseman, N. Smith (LAMPS WG)

- **Why**: CAs increasingly must verify policy compliance before issuance — e.g., that a CSR's private key lives in an HSM and is non-exportable. Today that's a zoo of proprietary attestation mechanisms. This standardizes carrying attestation evidence inside PKCS#10/CRMF, which matters for anyone automating certificate issuance for workloads and devices.
- **What**: ASN.1 structures carrying attestation data in CSRs, supporting both standardized (RATS-family) and proprietary attestation formats. WG draft at -22/-23: a design team (formed to break an author stalemate over design options) did a deep editorial pass; the Attestation OID registry was removed in -23; two PRs remain open (one debating whether a "Hint" should become a full CMS Attribute — the authors lean toward dropping hints entirely; one revisiting ASN.1 choices).
- **How**: Attestation evidence is generated, transmitted in the CSR, and verified by the CA as part of issuance policy (from abstract plus status slides; the precise ASN.1 details are still in flux per the open PRs).
- **Where applicable**: Any PKI where issuance is gated on key-protection or environment properties — HSM-bound keys, device identity, workload certificates. Mature WG draft (years in progress, design-team-reviewed) — on the path to last call but not there yet.

## Adjacent

### ML-KEM Post-Quantum Key Agreement for TLS 1.3

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) · [Materials](https://datatracker.ietf.org/meeting/125/session/tls)

Deirdre Connolly (Selkie Cryptography, TLS WG)

- **Why**: The standalone post-quantum key agreement for TLS 1.3 is essentially done — this defines what PQ TLS looks like at the wire level for every product the PM ships.
- **What**: Registers ML-KEM-512/768/1024 as TLS NamedGroups (0x0200–0x0202) for use in supported_groups/key_share, replacing (EC)DHE in the TLS 1.3 key schedule. Encapsulation keys run 800–1568 bytes with 768–1568-byte ciphertexts — the handshake-size implications every implementation will feel.
- **How**: Client sends pk in KeyShareClientHello; server returns the ML-KEM ciphertext in KeyShareServerHello; the 32-byte shared secret feeds the key schedule. Server must run the FIPS 203 encapsulation-key check (abort illegal_parameter on failure); ciphertext reuse is forbidden; RNG hygiene is called out (encapsulation randomness discloses raw RNG output). Security considerations cite formal analyses that IND-CCA-secure KEM substitution preserves TLS 1.3 handshake security, and hybrid constructions (RFC 9954, RFC 10024) give compositional safety. Intended status is Informational; the registry entries are currently Recommended=N.
- **Where applicable**: All TLS 1.3/DTLS 1.3 implementations. Maturity: WG draft at -11, submitted to IESG, in the RFC Editor queue with completed SECDIR/GenArt last-call reviews. Decisions remaining for implementers are deployment-level — standalone ML-KEM vs. PQ/T hybrids — not the spec itself.

### Using the Well-Known IPv6 Prefix to Represent Non-Global IPv4 Addresses

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-v6ops-nat64-wkp-1918/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-v6ops-01-jen-linkova-draft-ietf-v6ops-nat64-wkp-1918-00) · [Session recording](https://youtu.be/eAcZXJI89rU) · [Materials](https://datatracker.ietf.org/meeting/125/session/v6ops)

Warren Kumari, Jen Linkova (v6ops WG)

- **Why**: RFC 6052 currently forbids using 64:ff9b::/96 for RFC 1918 addresses and requires translators to drop such packets — which breaks IPv6-only nodes reaching IPv4-only services with private addresses, a daily pain in enterprise/SMB IPv6-only deployments.
- **What**: A WG draft that updates RFC 6052 to relax the MUST NOT/MUST-drop: allow the Well-Known Prefix to represent non-globally-reachable IPv4 addresses and let translators process them. It keeps existing deployments safe: implementations keep default behavior, gain a config knob; administrators apply explicit drop policies where the old behavior was relied upon. The slides note the same restriction removal was proposed by Fred Baker in erratum eid5547 back in 2018, and discuss why the Network-Specific Prefix isn't always feasible.
- **How**: A change to translation deployment guidance, not a new wire format — translate-or-not becomes an explicit policy question.
- **Where applicable**: NAT64/DNS64-based IPv6-only enterprise and SMB networks. Mature: WG draft, WGLC requested at this meeting — close to done.

### JSON Web Proof

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-jose-json-web-proof-update-03) · [Session recording](https://youtu.be/UtOpOWqveFw) · [Materials](https://datatracker.ietf.org/meeting/125/session/jose)

Mike Jones, David Waite (JOSE WG)

- **Why**: Selective-disclosure credentials are moving from SD-JWT toward BBS-style ZK-friendly algorithms; JWP is the container that makes them usable in the JWT-shaped ecosystem the PM's identity stack already speaks.
- **What**: A JWS-like container ("JSON Web Proof") that integrity-protects multiple payloads in one message and adds a presentation form supporting selective disclosure of individual payloads, plus a Presentation Header against replay. Recent -13 changes: `proof_alg` (separate from JOSE/COSE algorithm registries) in JWKs/COSE_Keys, and deterministic crypto operations in all examples.
- **How**: Issuer proves over multiple payload slots; holder presents a subset with per-claim disclosure. Open work presented: JSON Proof Token subclaim support (selective disclosure *within* claims, e.g., `address-country` — proposed syntax aligns with SD-JWT VC metadata), BBS extensions (experimental, described separately), BBS blind signatures (holder-known messages), and per-verifier pseudonyms.
- **Where applicable**: Digital-credential ecosystems (wallets, verifiable credentials) targeting unlinkability. WG draft, active; BBS-related pieces are explicitly less mature than the core.

### YANG Model for Border Gateway Protocol (BGP-4)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-model/) · [Materials](https://datatracker.ietf.org/meeting/125/session/idr)

Mahesh Jethanandani, Keyur Patel (Arrcus), Susan Hares, Jeff Haas (HPE) — IDR WG

- **Why**: A standard YANG model for BGP config/ops matters to anyone building automated DC or WAN fabrics — today every vendor's BGP schema differs. Once published, this becomes the north-star schema for BGP automation.
- **What**: YANG data model for configuring and managing BGP — protocol, policy, and operational aspects including RIB — based on data center, carrier, and content provider requirements. The draft (presented at -19, now at -23) is modular: separate submodules for types, capabilities, common/neighbor state, multiprotocol AFI/SAFI, policy, RIB tables/attributes, and session security (key chains, TCP-AO), with IANA-maintained modules for capabilities, notification codes, AFI/SAFI types, and community types.
- **How**: Standard NETCONF/RESTCONF data-model machinery layered on ietf-routing, ietf-routing-policy, ietf-key-chain, ietf-tcp, and BFD types.
- **Where applicable**: BGP automation across DC, carrier, and enterprise; vendor-neutral intent for gNMI/NETCONF pipelines. Maturity: long-running WG draft (-23, updated the day before this digest), intended Proposed Standard, still clearing YANG validation errors — close to the end of a long road, not a finished RFC.

## Wildcard

### DNS for AI Discovery

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/) · [Materials](https://datatracker.ietf.org/meeting/125/session/dnsop)

Jim Mozley, Nic Williams (Infoblox), Behcet Sarikaya, Roland Schott (Deutsche Telekom), Jeffrey Damick (Amazon)

- **Why**: A quietly ambitious idea: use DNS — not a third-party registry — as the discovery substrate for AI agents. If agentic workloads standardize on DNS for finding each other, discovery becomes cacheable, deterministic, and organization-controlled, and the PM's agents stop depending on brokered directories.
- **What**: DNS-AID publishes agents via SVCB records at the agent's own name (TargetName, ipv4/ipv6 hints, ALPN carrying agent protocols `mcp`/`a2a` alongside h2/h3, well-known URI for the agent card, a `cap` capability-descriptor locator plus `cap-sha256` digest) and an organization-wide index at `_index._agents.<domain>`. Scope covers "known agent" and "known organization" discovery; cross-domain capability search is explicitly out of scope (derivable). No new RR types, opcodes, or response codes.
- **How**: One SVCB query for the fast path; TLSA (DANE) records optionally authenticate the agent's TLS endpoint in permissive/preferred/strict postures with WebPKI fallback; DNSSEC-signed zones SHOULD; downgrade resistance via SVCB `mandatory=`. Security considerations are unusually honest: authentic records can still point at a malicious agent; `cap-sha256` is integrity, not trust — trust judgments stay out of band. Experimental extensions (EDNS(0) discovery hints, zero-trust enroll-uri, domain-control validation) are fenced off in a future-work section.
- **Where applicable**: Public and private networks, including agents hosted in provider domains. Individual draft (-02) — very early, and its fate in dnsop is uncertain — but this is the draft that makes "DNS as the agent directory" concrete, and it intersects directly with the A2A/MCP identity work above.

### One Signature Certificates

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-santesson-one-signature-certs/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-lamps-one-signature-certificates-01) · [Session recording](https://youtu.be/RyqnmLpaRBw) · [Materials](https://datatracker.ietf.org/meeting/125/session/lamps)

Stefan Santesson, Russ Housley (LAMPS WG)

- **Why**: A genuinely novel certificate profile: certificates that exist to validate exactly one signature, with the key destroyed immediately after — eliminating expiry and revocation complexity for long-lived document validation.
- **What**: Per the slides: key pair generated, certificate issued, document signed, private key destroyed. The certificate never expires (`notAfter` = 99991231235959Z), never revokes (`id-ce-noRevAvail`), and is bound to the single signed document via a new `signedDocumentBinding` extension (dataTbsHash + hash algorithm + binding type), with binding-type variants for CAdES/XAdES/JWS/COSE that hash only the payload where the signing process covers certificate data.
- **How**: Binding the certificate to the document hash makes the certificate meaningless for any other use; long-term validation reduces to verifying the signature against a certificate that can never be revoked or expire.
- **Where applicable**: Long-lived signed documents (contracts, archival records) rather than TLS/workload identity. The LAMPS adoption call ended 2026-03-13 and the draft is being republished as a LAMPS WG document — a small but real shift in how PKI can work.

### Symmetry-Driven Asynchronous Forwarding with Fast Reroute for LEO Satellite Networks (SDAF)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-luan-rtgwg-sdaf/) · [Slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-rtgwg-symmetry-driven-asynchronous-forwarding-with-fast-reroute-for-leo-satellite-networks-sdaf-00) · [Session recording](https://youtu.be/nzitn4M1Tc8) · [Materials](https://datatracker.ietf.org/meeting/125/session/rtgwg)

Shenshen Luan (Beihang University), Wenting Wei, Mingliang Ke (Xidian University), Dongxu Hou, Min Xiao (ZTE)

- **Why**: Not the PM's domain — but a fresh routing idea: instead of fighting topology churn in LEO constellations, exploit the toroidal symmetry of Walker-Delta constellations to get microsecond convergence with almost no state. It's a reminder that geometric structure can replace protocol machinery.
- **What**: SDAF performs failure-driven reverse-flow forwarding using only local link-state detection and a static Interface Symmetry Mapping Table — no control-plane convergence, no protocol extensions, no header changes. Compatible as-is with OSPFv3, IS-IS, MPLS.
- **How**: On detecting a failed egress, a node tags packets by ingress port; when egress matches ingress (packet returning to its origin arc), it reverse-forwards along the ring's major arc to a Phase Transition Point, then resumes forward flow. Two policies — RF-CF (counter-facing detour first, best for intra-orbit failures) and RF-LF (lateral-facing first, best for inter-orbit) — scale from ring to torus. Simulation on a 16×16 torus: up to 17.5% packet-loss reduction vs. normal forwarding under link faults, RF-LF best. Real 5-router ring experiments with OSPFv3: total packet loss drops by ~3 orders of magnitude (e.g., 310 vs. 432,485 packets), microloop loss eliminated, black-hole loss near zero, latency/jitter comparable, peak congestion reduced from 3,000 to 2,000 Mbps.
- **Where applicable**: LEO constellations with torus-like topology only, and only while the topology remains connected — a partitioned network needs higher-layer recovery. Individual draft (-00) seeking RTGWG feedback on whether the problem is even in scope. The evaluation is simulation plus a small physical testbed, not a production constellation.

## Themes

- **AI fabrics are pulling the whole routing area toward determinism**: adaptive routing (FARE scale-out and scale-up), logical fabric partitioning (DPF), sub-100µs FRR with NPU-driven notifications, lossless flow control extended across DCN+WAN, and multicast for collectives — a collective push to make plain Ethernet/BGP fabrics behave like an interconnect for training traffic.
- **BGP is becoming the single control plane of the data center**: BGP-LS topology export for BGP-only fabrics, bandwidth-as-communities (FARE), and color-based logical fabrics (DPF) all extend BGP into roles IGP/TE protocols used to own — and the drafts explicitly reference each other.
- **The control plane is too slow; move failure handling into the forwarding plane**: EVPN UDP fast notification, hardware-accelerated network notifications (FANTEL), and NPU-activated protection all share the same diagnosis — CPU-mediated reaction can't meet AI-era timers.
- **Agentic identity has become the OAuth/SPICE/TLS agenda**: transaction tokens for A2A, actor-chain delegation profiles, agent operation authorization, SPIFFE client auth, and workload-identifier TLS hints are five separate drafts converging on one problem — cryptographically binding user intent, agent identity, and delegated action across multi-hop agent workflows.
- **Security BCPs are being updated from live attack data, not theory**: the OAuth security-topics update documents COAT and session-fixation classes found in 20+/40+ shipping products, many of them agentic token vaults — agentic AI is now a primary source of new OAuth attacks, not just a new consumer of OAuth.
- **PQ and PKI modernization are quietly crossing the finish line**: ML-KEM for TLS is in the RFC Editor queue, CSR attestation is design-team-finalized, and one-signature certificates challenge the expiry/revocation model — all worth tracking for roadmaps even though none changes the PM's DC fabric designs.
