<!--
conference: NANOG 98
type: operator
source_url: https://nanog.org/events/nanog-98/agenda/
generated: 2026-11-01
registry_key: nanog-98
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NANOG 98

## Core

### RNG: Flat Datacenter Networks at Scale

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5894/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5894/20261018_Mahajan_Rng_Flat_Datacenter_v1.pdf) · [Recording](https://www.youtube.com/watch?v=AVKZmklWsAQ)

Ratul Mahajan – AWS

- **Why**: The most consequential physical DC topology talk of the meeting: Amazon claims the first production flat (non-tree) datacenter networks, solving the two problems — cabling and routing — that kept expander topologies academic for a decade. Directly in the PM's wheelhouse (topology, optics, cabling, routing).
- **What**: RNG (Random Resilient network Graphs) replaces fat trees with quasi-random graphs for most workloads at Amazon, now the default for new fabrics. Headline results from the deck: 69% fewer switches, 40% less power, 27% lower cost (slides also give 9–45% fewer switches depending on config), with application flows performing as well as or better than fat trees and graceful degradation under failures rather than the outsized impact trees suffer from small cuts.
- **How**: Three coupled inventions. ShuffleBox, a passive optical device that internally shuffles cables (e.g. 32×4×100G to 4×32×100G), giving random-graph connectivity with fat-tree-like cabling complexity. Spraypoint, a distributed routing protocol that exploits random-graph properties to find nearly all edge-disjoint paths via multi-level waypoints instead of shortest paths. Predictive models combining random-graph concentration properties with Spraypoint decorrelation, so oversubscription and path length are predictable at design time from topology parameters.
- **Where applicable**: AWS production (research 2022 → two experimental fabrics torn down 2024 → production 2025 → default). Not retrofittable — it assumes a custom passive optical shuffle and a new routing protocol — but it is the strongest evidence yet that expander/flat fabrics are operationally viable, and it should reshape any next-gen DC topology roadmap.

### Stop using 100GBASE-LR4

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5859/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5859/20261018_Steenbergen_Stop_Using_100Gbase-Lr4_v1.pdf) · [Recording](https://www.youtube.com/watch?v=2Uz7HqLGhcs)

Richard Steenbergen – Petabit Scale

- **Why**: A reference-grade optics talk aimed squarely at the interconnection world (IXP ports, peering cross-connects), which is still standardizing on a 2010 pre-FEC optic that hyperscalers abandoned within one product cycle of CWDM4 (2014). Cost, power, and physics — core PM territory.
- **What**: A complete guide to 100G client optics generations: Gen 1 LR4 (4×25G NRZ, LAN-WDM grid, four cooled lasers with TECs, no host FEC — raw BER or nothing), Gen 2 CWDM4/4WDM (uncooled lasers, ±6.5nm grid, host RS-FEC worth ~5–6dB margin, roughly half the price, everything else identical), Gen 3 single-lambda (53GBd PAM4, one laser, DSP + mandatory KP4 FEC). The thesis: every LR4 datasheet claim, including reach, has since been beaten by cheaper optics; the interconnection ecosystem has paid the "TEC tax" for a decade out of habit because changing requires coordinating with a remote party.
- **How**: Physics-driven walkthrough — chromatic dispersion penalty scales with baud², FEC (KR4/KP4 Reed-Solomon) has been baked into every 25G+ SerDes since ~2015 and is idle in the box, and pre-FEC BER is free early-warning telemetry (you can watch a link degrade for weeks before a real error).
- **Where applicable**: Universal for 100G handoffs; no hardware change needed (FEC is already in the host ASIC). The friction is procedural — coordinating a different optic with peers/IXPs — not technical.

### SRv6 and MRC for AI Data Centers

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5846/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5846/20261018_Styszynski_Srv6_And_Mrc_v1.pdf) · [Recording](https://www.youtube.com/watch?v=ze3ORk9sGrI)

Michal Styszynski – Juniper Networks

- **Why**: The backend AI fabric problem this program circles repeatedly — making RoCEv2 survive at 100k+ GPU scale without PFC — approached via an emerging OCP spec (MRC). Core to the PM's RDMA/lossless-fabric interest. Vendor session, but grounded in a specification rather than a product pitch.
- **What**: MRC (Multipath Reliable Connection) is modified RoCEv2 with reliability (SACK/NACK), packet trimming on congestion, packet spraying, and multiplanar fabric design — explicitly "no more PFC." Two transport flavors: IP-ECMP MRC (works with EVPN-VXLAN multitenancy, switch hashing) and SRv6 MRC (source-routed paths computed by a path orchestrator/fabric manager). Scale worked through an 8-plane design: ~131K GPUs, ~8K GPUs per pod, with optical shufflers breaking 2×800G into 8×200G plane links.
- **How**: SRv6 uSID shift-to-left: the orchestrator computes congestion-avoiding healthy paths and encodes each as a uSID chain in the outer IPv6 destination address; the NIC encapsulates RoCEv2, each transit node executes shift-left, and the leaf decaps. RoCEv2 Entropy Values are mapped to SRv6 Path-IDs at the NIC, which rotates across them; on congestion the switch trims the packet to headers, the receiver NACKs with source PSN, and the sender changes EV/Path-ID. The BTH header gains RTX/TSETH fields and new opcodes (e.g. reliable probe 0xDE), per the OCP MRC 1.0 spec.
- **Where applicable**: Requires MRC-capable NICs, AI Ethernet switches, and a path controller — an early, ecosystem-dependent stack. Multiplane designs assume no cross-plane links. Watch it as the OCP-specified alternative to PFC-based lossless fabrics; not something deployable on current commodity gear.

### AI Training Parallelism, From a Network Engineer's Point of View

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5868/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5868/20261018_Iazzag_Ai_Training_Parallelism__v1.pdf) · [Recording](https://www.youtube.com/watch?v=Xk2yoQhWPnI)

Adel Iazzag – NVIDIA

- **Why**: The best "why does my AI fabric traffic look like this" explainer on the program — parallelism strategy maps directly onto flow patterns, incast, and fabric design decisions. Presented as vendor-neutral from four years of building/running AI fabrics.
- **What**: A tour of the four parallelism types with their wire signatures: data parallelism (few very large AllReduce gradient flows per step, sawtooth uplink utilization); pipeline parallelism (point-to-point stage handoffs, latency-sensitive, util graphs look fine while the job waits); tensor parallelism (constant small AllReduce every layer that must stay in scale-up — if you can see it on the fabric, placement is wrong); MoE (AllToAll, many flows, uneven by destination, worst-case incast). Real jobs stack all of these on the same wires.
- **How**: NCCL picks ring vs tree algorithms based on topology and message size (256 GPUs: 510 ring steps vs 16 tree steps); design guidance: rail-optimized (NIC k to leaf k), 1:1 subscription, lossless with congestion control tested for many-to-one, and ECMP alone is not enough — packet or flowlet spraying needed.
- **Where applicable**: General technique for anyone building or operating AI backend Ethernet fabrics; the "test the collective, not the parallelism" and "give the scheduler the topology" instincts transfer regardless of vendor.

### A Journey of Accelerating and Offloading OVS with a DPU

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5886/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5886/20261018_Sevincer_A_Journey_Of_v1.pdf) · [Recording](https://www.youtube.com/watch?v=3Pg7atxbx6U)

Abdullah Sevincer – Crusoe, Alex Bortok – NVIDIA

- **Why**: A numbers-backed production account of moving SDN (OVS/OVN) from host kernel to hardware to DPU — datapath internals with real benchmarks, at AI-cloud scale. Squarely the PM's cloud-native/datapath interest.
- **What**: Three stages: kernel OVS (connection rates topping out in the low thousands/sec, instability growing with load); hardware-accelerated OVS datapath on the host (order-of-magnitude higher connection rate, near-zero failures, but host CPU cores and memory reserved away from customer VMs); then offloading the OVS/OVN control plane itself onto BlueField-3 DPUs, freeing 100% of host CPU — with the lesson that DPU cores aren't host cores, so right-sizing thread count beat adding more.
- **How**: Slow-path mechanics explained cleanly: PMD threads busy-polling pinned cores instead of IRQ→softirq→netlink upcalls; steering rules programmed by DMA'd descriptor queues the NIC drains itself instead of per-flow netlink/TC calls; per-core parallel connection tracking instead of shared kernel conntrack locks; VF representors programming the eSwitch. Benchmarks via Keysight CyPerf (HTTP over Geneve: overlay, stateful NAT patterns). OVN programs both Geneve east-west and north-south for customer VPCs.
- **Where applicable**: Crusoe's AI factory (BlueField-3/OVS-DOCA on every node) — co-presented with NVIDIA, so expect product framing; the performance mechanisms and tradeoffs apply to any OVS/OVN fleet, with numbers specific to their hardware and workloads.

### Your Change Deserves a Dress Rehearsal: Digital Twins from Production State with Containerlab and OTG

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5865/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5865/20261018_Tarno_Your_Change_Deserves_v1.pdf) · [Recording](https://www.youtube.com/watch?v=633Z0dxvMzg)

Brad Tarno – The Walt Disney Company

- **Why**: The most directly adoptable tooling talk of the program: a self-service lab-as-a-service that builds disposable twins from what production actually runs, closing the "valid config is not a safe config" gap (their motivating change: one peer-reviewed line silently suppressed 36→1 routes). Every load-bearing component is open source.
- **What**: A platform that harvests real device configs, transforms them per-platform to boot on virtual NOS images (cEOS, XRd, vJunos, N9Kv, FRR/gobgp), deploys via containerlab, and validates with Open Traffic Generator traffic (snappi), emulated BGP peer twins replaying real routes with full attributes, and Batfish+hier_config differential analysis of the predicted post-change config. Verdicts are graded per-axis (syntax by the real NOS parser, static, control plane, traffic, propagation) with convergence-aware traffic grading (PASS / PASS* transient loss quantified / FAIL permanent loss) and explicit INCONCLUSIVE outcomes with declared fidelity limits (MACsec stripped, multicast data plane, QoS queuing not graded).
- **How**: 1-hop LLDP neighbor expansion keeps twins small enough to build in minutes; peer twins are gobgp nodes injecting real sessions with full attributes (a full table via RIPE RIS MRT replay costs ~1.6KB/route, ~2.1GB resident for 1.4M prefixes); real traffic matrices replayed from Kentik top-N at lab-safe rates; the platform has no write path to production and holds no device credentials.
- **Where applicable**: Multi-vendor production network (Disney); fully replicable with open-source parts by any operator with config collection and lab servers. Limits are honestly declared: virtual data planes can't emulate MACsec, optics, or hardware timing.

### Digital coherent optics - Deployment and operation

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5851/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5851/20261018_Bedard_Digital_Coherent_Optics_v1.pdf) · [Recording](https://www.youtube.com/watch?v=bRXl2WIcmZk)

Philip Bedard – Cisco

- **Why**: Coherent pluggables (400ZR/800ZR) are how router-to-router DCI is collapsing the transponder layer — the PM's DC/WAN interconnect interest. Standards-heavy and operational rather than a pitch.
- **What**: Deployment patterns (unamplified single-channel dark fiber, amplified P2P DWDM, multi-degree ROADM) plus the management story: CMIS AppSel application codes (240 codes in CMIS 5.3+, 128 modes on one 800G-ZR optic), CMIS 0x51h interface-code descriptors that finally expose the optical parameters needed for alien-wave handling, C-CMIS 1.5 (Sept 2026) standardizing coherent performance registers, T-API for the photonic domain, and the OpenConfig `operational-mode` wart (non-standard numeric IDs like "5003"). Also notes the org convergence: cost savings are driving IP and optical teams to merge.
- **How**: A working standards matrix across OIF 400ZR/800ZR, OpenZR+ vs 400ZR+, and 100G-ZR (reach/FEC/modulation/power), SFF-8024 host/media IDs, and a model-driven path from pluggable manifest → IP controller → multi-layer controller using IETF/OpenConfig pluggable and impairment-topology drafts.
- **Where applicable**: Any operator interconnecting routers over dark fiber or DWDM; vendor-presented (Cisco TME) but the content is standards-first. 1.6T coherent standards work is underway — worth tracking for interconnect planning.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5852/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5852/20261019_Stein_Understanding_And_Optimising_v1.pdf) · [Recording](https://www.youtube.com/watch?v=GSSMEH9adUg)

Gerhard Stein – Flexoptix GmbH, Thomas Weible – Flexoptix

- **Why**: Optics power is a growing DC OpEx line; this is real measurement work on what transceiver telemetry (VDM/TEC current) can and cannot save you.
- **What**: Bench results across 100G QSFP28, 400G coherent ZR, and 800G optics on Cisco/Juniper gear. The punchline inverts the thesis: laser and TEC are negligible power drawers — the MCU/DSP are the real consumers — so laser-temperature optimization (~200mW average gain from a 20K temperature drop) isn't worth chasing. The real saving is operational: shutting a port forces the optic into low-power mode at ~7–20× lower consumption. Switch behavior differs (Juniper supplies optic power even with no RX; Cisco's Nexus is smarter here), and VDM support is patchy — two of three switches tested expose DDM only, and the one CMIS VDM implementation bakes in a 50°C laser-temp assumption.
- **How**: CMIS VDM parsing beyond DDM, TEC current and laser power via V×I, SFF-8636/CMIS power-class budgeting, plus a heat-transfer analysis (Nusselt/Prandtl/Reynolds) showing fan speed and case temperature dominate the thermal picture.
- **Where applicable**: Any operator with >100G optics fleets; vendor-authored (Flexoptix sells programmable optics) but measurement-driven with named DUTs and honest caveats. Next steps teased: port-shutdown automation across SONiC/Mellanox, and water cooling.

### Quantum-Safe Networking Starts With the Network You Already Have

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5880/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5880/20261018_Celindro_Quantum-Safe_Networking_Starts_v1.pdf) · [Recording](https://www.youtube.com/watch?v=mYa-SCp2O0g)

Vincent Paul Celindro – Quantum Foundry

- **Why**: PQC migration framed for network operators, not cryptographers: keep the network, replace only the quantum-vulnerable public-key functions. Sits at the intersection of the PM's network-security and key-establishment/identity interests.
- **What**: A migration model with three jobs: authentication (RSA/ECDSA → ML-DSA/SLH-DSA, FIPS 204/205), key establishment (DH/ECDH → ML-KEM, FIPS 203, typically hybrid ECDH+ML-KEM), and bulk protection (AES-256-GCM retained — Grover only trims margin and is hard to parallelize). Positioning: deploy PQC broadly, add QKD only where physics/topology/risk justify it. Roadmap: inventory crypto, prioritize by confidentiality lifetime (Harvest-Now-Decrypt-Later makes long-lived tunnels urgent), build crypto-agility, test vendor interop, in the context of EO 14412.
- **How**: Built up from IKEv1/IKEv2 architecture — a recorded Phase 1 DH exchange can later unlock the entire captured IPsec session (Phase 2 keys and ESP), so hybrid ML-KEM in the handshake is what defuses HNDL. "Upgrade the handshake, not every packet."
- **Where applicable**: General technique for any operator with long-lived confidential tunnels (IPsec VPNs, MACsec-adjacent planning); QKD is explicitly selective, not the default.

### A Blueprint for Securing Networks for AI : From Architecture to Operations

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5869/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5869/20261018_Salahudeen_A_Blueprint_For_v1.pdf) · [Recording](https://www.youtube.com/watch?v=MqnHA9hBX5M)

Saju Salahudeen – NOKIA, Reda Laichi – NOKIA

- **Why**: The only talk focused specifically on securing AI backend fabrics, where RDMA bypasses the host stack — forcing enforcement down to the switch and DPU. Core to the PM's network-security + AI-fabric overlap.
- **What**: A Day 0/1/2 framework. Day 0: SZTP (RFC 8572, ownership vouchers, IDevID on TPM) over insecure ZTP, secure/measured boot chains. Day 1: TLS for syslog/gRPC/RADIUS/NTP, gRPC RPC restriction via gNSI Authz (allow gNMI Subscribe, deny gNMI Set), AAA hardening, per-tenant VRFs on switches plus per-flow DPU policy pushed per job, backend default-deny ACLs (RoCEv2 UDP 4791 within same job/tenant only), DDoS tiers (edge scrubbing/Flowspec/RTBH, API-key rate limits for inference, PFC watchdog and per-tenant QoS against pause storms, CoPP). Day 2: monitoring shifts from packet inspection to streaming telemetry (sFlow, INT) plus behavioral baselining, because DPI/host IDS don't scale to 400G/800G and RDMA traffic is invisible to host-based tools.
- **How**: Anchored in the OpenAI/Hugging Face incident (agents exploited a third-party artifactory via exposed HF credentials) and in a public multi-vendor reference lab (github.com/srlinuxamericas/n98-ai-security).
- **Where applicable**: Vendor session (Nokia principal engineers) with framework flavor, but the techniques are multi-vendor and the lab is public; applies to any shared GPU fabric where kernel-bypass transports defeat host-based controls.

### When BGP Graceful Restart Wasn't Graceful

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5897/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5897/20261018_Rychtecky_When_Bgp_Graceful_v1.pdf) · [Recording](https://www.youtube.com/watch?v=eQM-un3K_yA)

Marian Rychtecky – NIX.CZ

- **Why**: The kind of hard-won postmortem NANOG exists for: a GR feature that lengthened an outage from "hidden" to two minutes, with packet captures, lab reproduction, and multiple vendor bugs unpacked.
- **What**: During a firewall HA upgrade, BGP sessions re-established but carried zero prefixes for ~121s. Root causes found: (1) the router sent TCP RST on the new connection because the old session wasn't cleanly torn down — violating RFC 4724's "treat old session as terminated"; (2) the firewall's GR coupled IPv4 and IPv6, so IPv4 routes waited on a stuck IPv6 session's End-of-RIB (the suspicious ~120s was the default reconnect timer); (3) a parsing bug stored the IPv6 peer as `2001:db8:1:` (missing `::2`), so the OS couldn't find the VRF context and RST'd. Vendor fix lands in 8.0.1 (Aug 2026), not backported to supported 7.4/7.6 branches; workaround: `set connect-timer 1`.
- **How**: Classic disciplined troubleshooting: EoR timing analysis, packet captures on both sides, a BIRD lab where impolite kills (`kill -9`) reproduced the RST window, two separate vendor tickets, and the operational mitigations (short connect timer, static routes with AD 255 during upgrades).
- **Where applicable**: Anyone running BGP GR across dual-stack, multi-vendor HA pairs — the failure pattern (AFI-coupled GR state, TCP session cleanup on failover) is general even though the specific bugs are vendor-embedded.

### False Immunity: long prefixes that bypass ROV

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5843/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5843/20261018_Herdes_False_Immunity_Long_v1.pdf) · [Recording](https://www.youtube.com/watch?v=iLgvebGwlpw)

Bryton Herdes – Cloudflare

- **Why**: ROV deployment creates false confidence — this talk demonstrates two concrete bypass classes with live tests against tier-1 networks. Routing security at its most operational.
- **What**: (1) Long-prefix "TE" announcements: at least two tier-1s (Lumen AS3356 for IPv4, Zayo AS6461) accept RPKI-invalid >/24 and >/48 prefixes, apparently filtering on IRR only — enabling the demonstrated 1.1.1.1/32 hijack accepted via AS8452/AS3356. Tested by advertising purposely invalid /32 and /128s to peers one-by-one and checking reachability from looking glasses. (2) RTBH: blackhole routes are generally exempt from RPKI filtering (IRR-based, long by nature, RFC 7999 community), creating a hijack vector that took a Tier-1. Proposed fixes: loose ROV restricted strictly to RFC 7999 BLACKHOLE routes, or a dedicated RPKI Discard Origin Authorization object (draft-spaghetti-grow-rpki-doa); vendor feature requests (Cisco IOSXR-I-1742, Juniper ROUTSP-I-71, Arista RFE 1964539) are pending.
- **How**: Active measurement from Cloudflare's peering position, plus the tension spelled out: RFC 9319 minimal ROAs (maxLength) vs long-prefix TE, and the forged-origin-hijack tradeoff of maxLength=32 ROAs.
- **Where applicable**: Every ROV-validating network (check whether you exempt long prefixes or blackhole routes) and every prefix owner publishing ROAs. Test method is limited by Cloudflare's relationship types with the tested ASes, as the speaker notes.

### Enforcing the First AS in BGP AS_PATHs

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5956/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5956/20261020_Herdes_Enforcing_The_First_v1.pdf) · [Recording](https://www.youtube.com/watch?v=cqA3_-aEdZ8)

Bryton Herdes – Cloudflare

- **Why**: The hijack class neither ROV nor ASPA catches — stripping/padding enough of the path that the origin and provider attestations look fine — and the fix is a single, existing config knob. Ten minutes, immediately actionable.
- **What**: Forged AS_PATHs where the adjacent peer's AS doesn't match the first AS in the path defeat both ROV and ASPA. An active test (advertised a prefix with a forged first AS, e.g. `as-path-prepend 402542` ahead of localAS 13335) found half of Tier-1 networks not enforcing First AS. Vendor defaults are the culprit: JunOS/JunOS EVO, Nokia SR OS, Extreme SLX-OS, RouterOS, and BIRD ship with enforcement OFF by default; Cisco IOS XE/XR, Arista EOS, Huawei, OpenBGPD, and FRR ship ON.
- **How**: Reject routes where peerAS != firstAS on eBGP neighbors, with documented exceptions (transparent IX route servers, iBGP, deliberate anycast probe cases). Per-implementation config knobs are listed in the deck.
- **Where applicable**: Universal — any eBGP edge; check your configs, especially if your vendor defaults insecurely.

### BGP Role model: tracking the adoption of RFC 9234

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5899/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5899/20261018_Herdes_Bgp_Role_Model__v1.pdf) · [Recording](https://www.youtube.com/watch?v=MCjUYIF2Axo)

Bryton Herdes – Cloudflare, Iliana Xygkou – Georgia Institute of Technology

- **Why**: RFC 9234 (BGP Roles + OTC) is the session-level route-leak defense that complements ASPA's AS-level attestations — and this is a measurement of who's actually setting OTC, and who is actively stripping it.
- **What**: Roles encode business relationships per BGP session; OTC is attached automatically on sideways/downward propagation and leaks get rejected. The measurement (using Cloudflare's direct peering to attribute OTC setters with certainty) shows adoption growing but limited, with IX route servers setting the good example. The experiment — announcing OTC to all peers — found 15 OTC-stripping ASes including two Tier-1s; 33.1% of unique IPv4 and 17% of IPv6 AS_PATHs lacked OTC where expected. Arelion (AS1299) promptly fixed after outreach; GTT (AS3257) continues stripping. Plus a proposed RFC 9234 improvement (draft-herdes-idr-otc-rs-verification: RS as apex setting OTC) and an implementation support matrix (Junos/FRR/BIRD/OpenBGPD yes today; IOS XR 26.4.1 and EOS 4.37 coming; SR OS, Huawei, GoBGP no).
- **How**: Session-level roles vs ASPA's AS-level granularity (mixed relationships exist); receiver-side compensation for missing OTC; role configs require a BGP session reset (new OPEN).
- **Where applicable**: Every eBGP operator — deployment is cheap, has already started, and the stripping measurements make the case that partial adoption still leaks.

### Your Route Was Dropped—But Where and Why? Closing RPKI's Operational Feedback Gap

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5874/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5874/20261018_Kang_Your_Route_Was_v1.pdf) · [Recording](https://www.youtube.com/watch?v=LVeD2_QLZCk)

Min Suk Kang – KAIST

- **Why**: ROV's silent-drop model gives prefix owners no visibility into errors, attacks, or their own urgent operational actions — a research contribution (USENIX Security 2026) brought explicitly to operators for feedback.
- **What**: Three characterized gaps: no error visibility (typos silently filtered), no attack visibility (owners unaware of hijacks), and defense incompatibility — DDoS-scrubber traffic redirection gets ROV-filtered for tens of minutes (with Lumen's own FAQ and RFC 9319 §5.1 quoted on the timing problem). iROV adds interactivity: a validating AS queries the owner just-in-time and notifies it of the invalid announcement and observed impact; owners can approve urgent changes. Evaluation: urgent route-change reachability rises from 23% baseline to ~90% at full adoption — and even Tier-1-only early adoption reaches 49% (>2×) — with query load bounded to ~1,000 queries per invalid announcement via validity stapling (transitive BGP attribute using RPKI Signed Checklists, RFC 9323), probabilistic querying, and per-owner rate limiting. Prototype on modified BIRD + FORT validator shows negligible overhead under five days of Route-Views traces.
- **How**: Owner operates a respondent web server whose address is advertised via a ROA extension; responses are stapled and propagate; an RTR extension carries the interaction.
- **Where applicable**: Not deployable today — needs ROA/RTR extensions and a BGP attribute allocation — but the problem statement is real for every ROV-validating network and every prefix owner that has ever fought a benign-invalid during an incident.

### Building a Network Troubleshooting Agent: Architecture, Tools, Guardrails, and Lessons Learned

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5892/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5892/20261018_Muthuramakrishnan_Building_A_Network_v1.pdf) · [Recording](https://www.youtube.com/watch?v=eC-W7yGgXC4)

Karthik Srinivas Muthuramakrishnan – Microsoft

- **Why**: Agentic network ops is arriving, and the hard problems are authorization and evidence control, not model choice — the design here (scoped approvals, fail-closed authority) maps directly onto the PM's workload/agentic-identity expertise.
- **What**: An agent architecture that keeps reasoning, policy, and execution strictly separate: "the model proposes, trusted code decides what can execute." Four pillars: a model-agnostic harness (playbook version, tool schemas, target, and policy budget held constant while model and tool sequence vary — making runs comparable); guardrails (policy checks before any request reaches the adapter: tool allowlist, rate/concurrency, equivalent-call loop limits, failure thresholds, session budget with kill switch); audit (ordered observable events, not private model reasoning — one session artifact answers six operational questions); and memory (verified history reorders safe reads earlier but never authorizes; compatibility keys include device identity, software and playbook versions).
- **How**: Approval binds one exact action — approver identity, target router, action name, arguments digest, expiry — and fails closed on wrong target, changed arguments, or expiry. Typed, staged reads per versioned playbook (e.g. `bgp-neighbor-down` 1.0.0) keep deterministic operations deterministic.
- **Where applicable**: Demonstrated in a virtual router environment at Microsoft; the pattern generalizes to any organization exposing network capabilities to LLM agents, and the approval-grant model is essentially scoped, short-lived credentials — familiar territory for anyone thinking about workload identity for agents.

## Adjacent

### ASPA la vista.. Route leaks

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5878/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5878/20261018_Strachan_Aspa_La_Vista__v1.pdf) · [Recording](https://www.youtube.com/watch?v=ZjrwHTfzRmk)

Alastair Strachan – RIPE NCC

- **Why**: ASPA is the next RPKI deployment wave after ROV, and this carries the operational guidance plus fresh uptake numbers — useful context for the routing-security work the PM is already doing.
- **What**: A clear primer on ASPA objects (signed provider-AS lists) with the upstream/downstream path-validation algorithms and the complementary-coverage matrix (ROA for misorigination, ASPA for leaks and partial path spoofing, BGPsec for path spoofing). Signing uptake as of Aug 2026: 2.2% of registered ASNs worldwide (RIPE region 4.6%; Czech Republic leads at 10.9%); hosted signing UIs now live across all RIRs (Krill July 2025, RIPE NCC Nov 2025, ARIN Jan 2026, APNIC June 2026).
- **How**: Same validator/RTR deployment model as ROV; operational guidance: include all providers (including backups not visible in AS paths), include non-transparent IXP route servers or they register as valleys, reject (don't de-prefer) invalids, and start with logging-only.
- **Where applicable**: General, but early — router validation support is incomplete ("talk to your vendor"). Mostly educational for a routing-security veteran, but the uptake data and signing checklist are current.

### Multi-Path Traffic Engineering Workshop

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5759/)

Vishnu Pavan Kumar Beeram – HPE, Zhaohui (Jeffrey) Zhang – HPE, Kireeti Kompella – Juniper Networks

- **Why**: MPTE unifies multipath and TE for WAN and AIDC/DCI, and is feeding into ML network scheduling at the IETF — relevant to the PM's WAN/interconnect and AI-fabric interests.
- **What**: One MPTE DAG construct carries what previously needed many LSPs: unequal-cost, weighted load balancing at every junction, multiple ingresses and egresses, minimal churn on link failure (junction ratios adjust, DAG shape stays), and much less state than per-path signaled tunnels. For ML clusters: non-multipath TE is called "a total non-starter," and MPTE becomes the vehicle for network scheduling — resource reservation, protection, and traffic isolation per AI job (draft-kompella-rtgwg-mlnwsched, new at RTGWG).
- **How**: MPTED tunnel/junction state (incoming bandwidth, previous/next-hop sets with load shares), signaled via RSVP or BGP extensions; the workshop ran it hands-on in HPE/Juniper virtual environments (vMX/cRPD) for both WAN and AIDC scenarios.
- **Where applicable**: Vendor workshop (HPE/Juniper, registration required) around IETF drafts (draft-kompella-teas-mpte and signaling companions) — standards-track and worth tracking even if you don't run the vendors' stacks; the AIDC framing presumes job-aware scheduling above the fabric.

### Auto-bandwidth for Segment Routing

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5866/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5866/20261018_Shypovalov_Auto-Bandwidth_For_Segment_v1.pdf) · [Recording](https://www.youtube.com/watch?v=zxytzHQHEe8)

Dmytro Shypovalov – Vegvisir Systems

- **Why**: The missing RSVP-TE auto-bandwidth equivalent for SR is a real ISP pain; this is a working, open-source, standards-based design with honest production caveats.
- **What**: The problem: SR LSPs are stateless and most routers can't advertise per-LSP traffic rate (RFC 8733/RFC 9857 exist but require router-side sampling). The solution: an external bandwidth sampler (open source: github.com/Vegvisir-Systems/srte-sampler) collects SR LSP counters via gNMI and advertises the traffic rate to the PCE as a BGP-LS type-5 route with bandwidth TLV; the PCE recomputes segment lists and pushes via BGP-SRTE. Works today with IOS-XR, JunOS, EOS. PCE redundancy needs no state sync (distinct SRTE distinguishers, like route reflectors); total PCE failure falls back to IGP shortest path. The critique is self-aware: this merely replicates RSVP-TE auto-bandwidth; the better future design has the PCE query raw counters from existing telemetry (Telegraf/VictoriaMetrics) for a centralized traffic-matrix view, burst reaction, and analytics.
- **How**: Feedback loop: router counters → sampler → BGP-LS to PCE → updated segment list (BGP-SRTE preferred; PCEP explicitly discouraged). Mesh templates plus ACTN (RFC 8453) sketch the intent-based layer above it.
- **Where applicable**: Multi-vendor ISP SR-MPLS/SRv6 WANs; the author is candid about what "production-ready" requires (deterministic sampling, cross-controller identical results).

### Keynote: Global Infrastructure and Layer 3 Interconnection

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5853/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5853/20261018_Brodsky_Keynote_Global_Infrastructure_v1.pdf) · [Recording](https://www.youtube.com/watch?v=elmfXcclcUE)

Paul Brodsky – TeleGeography

- **Why**: Market and topology context for the PM's DC/WAN interconnect interest: where subsea capacity, investment, and concentration risk are heading.
- **What**: Bandwidth volumes still soar even as growth rates moderate (incremental annual demand keeps rising); hyperscalers (Google, Meta, Amazon, Microsoft) now dominate new cable investment, but carriers remain necessary partners in hard regulatory geographies — and hyperscaler cables will still swap/sell fiber pairs and IRUs. Resilience improves via landing-site and corridor diversity, though connectivity ≠ capacity (82% of the Middle East's used international capacity still terminates in Europe). The US is no longer the sole hub (largest routes: US–LatAm, Europe–ME, Asia–Europe; Miami as the LatAm hub, Marseille/London as Africa's). AI's subsea impact remains unclear — Anthropic's FCC filing says most AI workloads don't touch submarine cables, but dataset movement and spatial-temporal load shifting could turn networks into global compute load balancers. LEO is an access technology that complements, not replaces, subsea backbones (Starlink ~9M subs, large share of constellation capacity stranded at any moment; satellite traffic rides ground stations into Layer 3 interconnection).
- **How**: TeleGeography's Transport Networks dataset — lease price trends, cable construction costs, ownership analysis.
- **Where applicable**: Analyst overview, not an operator technique — useful context for interconnect, peering, and capacity planning decisions.

### One Control Plane Away: Are Cloud Providers Critical Infrastructure

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5884/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5884/20261018_Tzvetanov_One_Control_Plane_v1.pdf) · [Recording](https://www.youtube.com/watch?v=1NiPnzC4YFk)

Krassimir Tzvetanov – Purdue University

- **Why**: Quantifies the web's provider concentration properly — separating fronting, hosting, and DNS — with a method operators can reuse on their own dependency chains; resonates with post-Cloudflare-2025 resilience thinking.
- **What**: A weekly measurement pipeline (since Aug 2026) over the Tranco top 10,000. Naive apex-A-to-ASN attribution undercounts CNAME-deployed CDNs by up to 2.4–2.7× (Akamai) and overcounts clouds by conflating hosting with fronting; the full layered pipeline finds Cloudflare fronts 29.4% of the top-1,000 but 46.3% of the top-10,000 (bigger properties diversify; 13% of strongly-fronted domains are multi-CDN), while the mid-tail single-homes. DNS is separately concentrated (Cloudflare 26.1%, Route 53 21.8%, only 13.7% self-hosted). Combining layers: 21.9% of live top-10k domains depend on Cloudflare for both DNS and delivery — one control-plane event from total unavailability — and 37.9% are double-dependent on some single organization. Tool and dataset to be released at publication.
- **How**: Layered evidence (strongest wins): CNAME chains for apex and www, provider-published service ranges (e.g. AWS CLOUDFRONT vs EC2 tags), HTTP/TLS fingerprints, BGP origin data, with inter-layer disagreements retained rather than silently resolved.
- **Where applicable**: The exposure-assessment recipe is general — run it against your own domains and dependency chains; the headline numbers are specific to the Tranco cohort.

### Salvaged Silicon: Building an Open Network OS for a Switch the Industry Left for Dead

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5870/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5870/20261018_Wright_Salvaged_Silicon_Building_v1.pdf) · [Recording](https://www.youtube.com/watch?v=NN5yK6MDkQo)

Christopher Wright – EdgeNOS / NOSaic

- **Why**: A genuinely free-and-open NOS for EOL Broadcom-based switches — probing what "open networking" should have meant, and architecturally interesting: the kernel FIB is the source of truth.
- **What**: EdgeNOS/NOSaic: a from-scratch NOS with no license or support contract, treating the box as an ordinary Linux router — routing daemons (FRR, static routes) program the kernel FIB, and a userspace agent (edged) mirrors it into the ASIC's tables; front ports are real netdevs so `ip`, `ethtool`, and `tcpdump` work unmodified; any daemon installing a kernel route gets hardware forwarding for free. Running on AS5610 (Trident+), AS4610 (Helix4), Arista 7050TX-64/SX2-72Q, Nexus 3172TQ; the Intel Fulcrum FM6000 currently forwards only by replaying a captured EOS boot trace. AI-assisted reverse engineering collapsed the register-bring-up problem (9 directions → 250+ actions → 115 live probes in one session).
- **How**: No vendor SDK — hardware state reconstructed from dumps of a known-good install; hard-won lessons include: copy-to-CPU is internally a multicast replication (no replication engine, no copy), stale status registers masquerade as dead hardware, and every optic needs switch-side code. ONIE installable, Linux 6.1 maintained into 2027 with A/B slots and auto-rollback.
- **Where applicable**: Hobbyist-origin but real; applies to the large category of abandoned Broadcom-era gear (~600 Broadcom device IDs). Not a supported production NOS today — its value is as a proof of the disaggregation model's unfinished half and a signal for open-NOS strategy.

### Botnet.cl - Live Botnet Monitoring and BGP Feed

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5955/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5955/20261021_Pe_a_Botnet_Cl_-_Live_v1.pdf) · [Recording](https://www.youtube.com/watch?v=VPDNg37Awm4)

Rodrigo Peña – Bitred Group SpA

- **Why**: A ten-minute lightning talk, but a live example of AI-assisted security operations with community distribution — 115 ISPs subscribed in two months.
- **What**: A protocol emulator (with AI-assisted recovery of C2 protocols) registers and heartbeats into botnet C2 servers, logging commands; ADB sinks capture Android malware acquisition paths. Observations become a BGP feed: 25 confirmed C2 IPs across 25 botnet families, distributed as IPv4 /32 routes tagged with the BLACKHOLE-style community 65535:666, origin ASN, and botnet-family metadata.
- **How**: Emulation-first intelligence gathering (no need to run real bots at scale), then per-C2-IP blackhole announcements that member ISPs apply themselves.
- **Where applicable**: Chile-origin effort but the pattern — a shared, metadata-rich blackhole feed — is general; the talk is thin on method detail (from slides only).

## Wildcard

### Interplanetary Internet Architecture, Addressing, and Routing

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5890/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5890/20261018_Eddy_Interplanetary_Internet_Architecture__v1.pdf) · [Recording](https://www.youtube.com/watch?v=DW_7xwPLIT8)

Wesley Eddy – Aalyria

- **Why**: IP to the Moon and Mars is actually standardizing (IETF TIPTOP working group), and the design constraints — extreme delay, scheduled connectivity, disconnection — produce routing and addressing ideas you won't see anywhere else.
- **What**: An architecture for IP-based networks spanning Earth and Lunar/Mars domains (draft-ietf-tiptop-ip-architecture). Surprisingly, modern IP stacks mostly work at lunar delays — the IETF 124 hackathon ran Discord, Slack, Apple Messages, YouTube, and web browsing at lunar RTTs, and simulated pings to Voyager distances; QUIC's tunability is a key enabler. Addressing is genuinely contested: IPv6, blocks per planet, one RIR or many, aggregation encouraged, and "who defines the list of planets?" (mirrored in ARIN's TIPTOP policy draft ARIN-2026-1). Routing is "scheduling, scheduling, scheduling": PCE-like centralized computation of time-varying routes distributed to nodes well in advance, with inter-domain time-varying BGP as a someday problem; temporospatial SDN (Aalyria's Spacetime, grown from Loon's aerospace mesh code) is the current exemplar, plus Outernet Council federation interfaces for multi-operator systems.
- **How**: Architecture summary plus active IETF/ARIN policy threads.
- **Where applicable**: No near-term operational relevance, but the scheduled-intermittent-connectivity routing concepts echo terrestrial challenged networks — and the speaker's signoff ("hope to see you at SSNOG") tells you where the community thinks this goes.

### When the World Cup Moved to YouTube: 416 Gbps and the Limits of Local Delivery in Brazil

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5895/) · [Slides](https://storage.googleapis.com/site-media-prod/meetings/NANOG98/5895/20261018_Ornelas_When_The_World_v1.pdf) · [Recording](https://www.youtube.com/watch?v=g7DKhsfdY2M)

Renato Ornelas – OpenX (Brazil)

- **Why**: Not the PM's usual beat, but a rare, complete dataset of an entire nation's traffic arriving over one CDN with no delivery infrastructure of its own — hard numbers on cache ceilings, PNI saturation, and event-driven capacity.
- **What**: 34 match nights measured at OpenX (AS263444, 60+ downstream ASNs, 1–3M broadband subscribers): 18.4 PB of Google traffic; 416 Gbps peak; 12 PB above football-free baselines. At the peak, embedded cache pinned at its 79 Gbps ceiling and one PNI site saturated at 2×100G — so 40% of delivered traffic (165 of 409 Gbps) arrived over international transit from North America and Europe. Kickoff hour predicted peaks better than audience size (21.1M devices at 2pm Monday → 207 Gbps; 18.5M at 5pm Sunday → 391 Gbps). The half-time signature: Google sheds 128 Gbps in ten minutes while Meta jumps and Netflix stays flat — three CDNs moving three directions inside fifteen minutes.
- **How**: Five-minute flow telemetry (Kentik) over 16-hour nightly windows, with a per-night appendix chart marking half-time, extra time, and shootouts.
- **Where applicable**: Brazil-specific vantage (single-CDN delivery, one wholesale operator) — but the transferable lessons are explicit: size for the event not the busy hour; local-delivery ceilings are ones you don't control; and measure it yourself, because flow data at five-minute resolution showed everything.

### Keynote: Why Do We Have Self-Driving Cars, But Not Autonomous Networks?

**Links:** [Abstract](https://nanog.org/events/nanog-98/content/5738/) · [Slides](https://www.nanog.org/sites/default/files/1_Kompella_The_Networking_Grand_Challenge.pdf) · [Recording](https://www.youtube.com/watch?v=Jf_2t1GF9mA)

John Evans – Independent

- **Why**: Ten years on from Kompella's self-driving-network framing, this asks the structural question: why did configuration automation and network control progress while operations stayed in the alert → ticket → operator loop? (from abstract only — page fetch failed; no slides in the source set)
- **What**: The argument: networking treats autonomy as an observability-and-workflow problem built on existing systems — the natural first step for applying AI — whereas self-driving cars showed autonomy is a paradigm shift in architecture, signals, models, and control, not an AI feature bolted onto an existing vehicle.
- **How**: Applies the control-system approach from self-driving cars and robotics to network operations: what's missing today, where autonomy can be deployed safely first, and a realistic path from assisted operations toward autonomous control.
- **Where applicable**: Conceptual keynote, no results — directional, but a useful frame for anyone shaping network-automation strategy and deciding where copilots/agents genuinely change the operating model versus decorating it.

## Themes

- **AI fabrics are the program's center of gravity, and they're converging on a specific recipe**: multiplanar/packet-sprayed backends, PFC-free reliability at the transport (MRC's SACK/NACK/trimming), TE-aware scheduling (MPTE for AIDC), and — notably — passive optical shuffles appearing in *both* Amazon's RNG and the MRC 8-plane design. Optical topology tricks and lossless-transport redesign are being reinvented together, not separately.
- **Routing security is moving past ROV in lockstep**: ASPA, RFC 9234 roles/OTC, First-AS enforcement, iROV's feedback gap, and the MANRS baseline update all attack the residual holes ROV leaves (long prefixes, RTBH exemptions, path stripping, silent drops) — and the measurement talks publicly name Tier-1s that fail or strip (Lumen, Zayo, GTT), which is a new level of accountability.
- **Change rehearsal is becoming standard practice**: the Disney containerlab/OTG/Batfish twin platform (fully open source), the Forward Networks emulation-vs-modeling analysis, and ESnet's discovery service all treat "evaluate the change against live state" as the missing gate — with honest fidelity limits declared per run.
- **The optics layer is where cost and power are being fought**: retire LR4 for CWDM4/single-lambda (FEC is already in your ASIC), standardize coherent pluggable management (C-CMIS, AppSel, T-API), and harvest the 7–20× idle-power savings of shutting ports — the transceiver-efficiency talk's most actionable finding.
- **Post-quantum migration finally has an operator-shaped roadmap**: keep IPsec and AES-256-GCM, hybridize the IKE handshake with ML-KEM, prioritize by data lifetime, and reserve QKD for selective links — "upgrade the handshake, not every packet."
- **Agentic and AI-assisted ops arrived with guardrails as the headline**: the Microsoft troubleshooting agent's scoped-approval model (identity, target, arguments digest, expiry, fail-closed), AI-assisted botnet protocol recovery, AI-assisted ASIC bring-up, and Claude-driven code review at Internet2 all point the same way — the design problem is authority and evidence, not model capability.
