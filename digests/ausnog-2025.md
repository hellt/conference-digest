<!--
conference: AusNOG 2025
type: operator
source_url: https://www.ausnog.net/events/ausnog-2025/program
generated: 2026-11-06
registry_key: ausnog-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AusNOG 2025

A compact operator program (~19 substantive talks, no published abstracts — all write-ups below are grounded in the extracted slide decks). Cloud-native networking (eBPF, Kubernetes, service mesh) and identity (passkeys, SPIFFE) are essentially absent from this program; the value here is concentrated in physical DC/optics, WAN interconnect, routing security, and transport.

## Core

### No Packet Left Behind: AWS's approach to building and operating reliable networks

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-03-LincolnDale.pdf) · [Recording](https://www.youtube.com/watch?v=GeE-4V7iXek)

Lincoln Dale — Amazon

- **Why**: The reference talk on hyperscale DC fabric design and closed-loop network operations — architecture, auto-remediation, and a vendor-agnostic discard-metric standardization effort the PM should track.
- **What**: AWS's design tenets and numbers: cellular datacenter architecture (access cells, intra-/inter-AZ core cells) for blast-radius isolation; single-chip 1RU 12.8T fixed-port switches (32×400G) as the capacity building block — 100Tbps per rack, 3,200Tbps per 32 racks — explicitly choosing redundancy *between* boxes (3-tier Clos) over large-chassis dual-monolith. Operations side: 5-stage auto-remediation, >1.8Bn metrics/min, >96% of events auto-remediated; deployments always automated with intent validation (Batfish for routing-policy/ACL errors, plus an internal VM/containerlab-style system for scale validation) and rollback on any out-of-expectation metric.
- **How**: Key insight that auto-remediation needs (a) architecture that supports it, (b) an accurate signal of impact that indicates cause, (c) a deliberately small action set (isolate/restore device or link, roll back, move traffic, escalate) — because the wrong action is worse than none (draining a congested device worsens congestion). Notably, vendor discard counters were too inconsistent (grey failures, double counting), so AWS defined its own classification scheme, published as an IETF individual draft (`draft-evans-discardclass`), and mapped 64–256 hardware drop counters per platform onto it.
- **Where applicable**: AWS-specific production scale and tooling, but the tenets, the rollback discipline, and especially the discard-classification work transfer to any large fabric operator. The discard taxonomy draft is relevant to anyone doing grey-failure detection in DC fabrics.

### Building AI Clusters: What Network Engineers need to know

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-04-BrianWalsh.pdf) · [Recording](https://www.youtube.com/watch?v=ReuAmLGa5O8)

Brian Walsh — Nokia

- **Why**: AI training clusters are now the dominant forcing function in DC fabric design — rail-optimized topology, RoCE/lossless-adjacent behavior, and elephant-flow traffic patterns. squarely in the PM's RDMA/lossless-fabrics and topology interests.
- **What**: A structured primer mapping the AI stack to network engineering decisions: programming frameworks (PyTorch DDP, NCCL/RCCL collectives) → parallelism strategies (data/pipeline/tensor) → collective operations (all-reduce, all-gather, send/recv) → the resulting NIC traffic pattern: periodic synchronized bursts, a few elephant flows, and job completion time bound by the *worst-case tail latency across the cluster* — fundamentally different from steady cloud traffic. In-node is NVLink/NVSwitch (or Infinity Fabric); across nodes it's InfiniBand, RoCEv2, and the emerging UEC. Cluster build-out is modular "Scalable Units": e.g., 256 air-cooled B200 GPUs in 9 racks, or a liquid-cooled GB200/NVL72 SU of 576 GPUs across 10 racks with 4 Ethernet GPU rails, NVLink switch trays, and CDUs — pre-validated at line rate, with fixed cabling/routing/software per SU and scale-out via spine/core.
- **How**: Walks the full stack (CUDA kernels → collectives → topology) and shows concrete rack-elevation layouts per SU variant, with SU node count tied directly to GPU-server NIC count and leaf radix. Rail-optimized design: each NIC homed to its own rail-leaf.
- **Where applicable**: Vendor-educational (Nokia) but not a product pitch — the GPU/collective/topology content is vendor-neutral. Directly applicable to anyone designing or evaluating AI back-end fabrics; assumes Ethernet/RoCEv2 as the baseline with IB/UEC as context.

### Evolution of Transport Protocols

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-05-GeoffHuston.pdf) · [Recording](https://www.youtube.com/watch?v=nc6Qb-LvPos)

Geoff Huston — APNIC

- **Why**: Connects end-host congestion control to switch-silicon design constraints — buffer sizing math, on-chip memory tradeoffs, ECN, and BBR. Rare to see transport theory and switching hardware economics in one talk; directly relevant to physical DC networking and lossless-fabric thinking.
- **What**: Why TCP session speeds have stalled in the tens of Gbps while optical transport heads to multi-terabit. The progression: Reno AIMD → CUBIC (fast capacity reaction but extended queue-formation phases and bufferbloat exacerbation) → BBR (pacing plus periodic RTT-based capacity probes every 8th RTT with 25% rate excursions; does *not* change its bandwidth estimate on loss). Buffer theory: single-flow sizing = BW·RTT; N desynchronized flows need BW·RTT/√N (Appenzeller/McKeown/Keslassy); with paced senders the residual requirement drops to O(log W). The punchline for switching: on-chip memory is only ~16–64MB, memory/memory-control consumes 20–60% of switch die area, and memory speed isn't scaling with transmission — so future capacity gains mandate *smaller* buffers, which demands paced, queue-sensitive senders (ECN or delay probing). ECN deployment remains sparse despite being the natural router-side queue-onset signal.
- **How**: Control-law mechanics (ACK pacing, loss vs. delay probing, queue drain timing), buffer-sizing derivations, and a candid closing: "we don't know all that much about fine-grained behaviour of large-scale high-capacity switching systems… the Internet still contains important unsolved problems."
- **Where applicable**: Broadly applicable fundamentals, vendor-neutral. The buffer-size and chip-memory sections directly inform DC switch selection and capacity planning; relevant context (not a treatment of) RDMA/lossless fabrics, which sidestep TCP control loops entirely.

### AARNet - Australia's Academic and Research Network

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-07-PeterStamp.pdf) · [Recording](https://www.youtube.com/watch?v=oVw9q91Yv1w)

Peter Stamp — AARNet

- **Why**: A clean packet-optical convergence case study — coherent 400G ZR+ pluggables plugged straight into routers, eliminating transponder shelves — plus a well-explained model-driven automation stack. Core to the PM's optics and DC/WAN interconnect interests.
- **What**: AARNet5 redesign: at each ROADM site, a 1RU low-power router (2–4× 400G/100G ports) uses DWDM 400G QSFP-DD ZR+ coherent pluggables configured to a specific wavelength with high launch power, multiplexed directly by the ROADM — removing most transponders (each was 1RU and ~150W; ZR+ optics draw ~25W) and retiring end-of-life SDH. Every ROADM site becomes a regional PE offering 1/10/25/100G access with L2 e-line/e-LAN and L3VPN, eliminating city hairpins (a 30km regional circuit previously hauled 300km via the metro PE) and replacing manually provisioned optical protection with inherent IP fast-reroute. Automation: Cisco NSO with YANG service models ("order forms") and multi-vendor templates driving full service lifecycle — example backbone-link service encodes LAG members, micro-BFD, ISIS-SR/OSPF-LDP selection, delay measurement, SRLGs, MTU.
- **How**: YANG models abstract vendor CLI; templates expand to device config via RESTCONF; hierarchical service model (Internet service → logical access circuit → device/interface) means editing the access circuit migrates the BGP neighbor, filters, and service to the new device automatically.
- **Where applicable**: AARNet-specific topology and scale, but the techniques are broadly adoptable: ZR+-into-router requires close optical/router team coordination (wavelength, power, dispersion) and ROADM access; the NSO service-modeling pattern is generic. Steers usefully toward Steenbergen's NANOG optical tutorial for fundamentals.

### The Scourge of Excessive AS-SETs

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-07-DougMadory.pdf) · [Recording](https://www.youtube.com/watch?v=2FVJlXDPV_w)

Doug Madory — Kentik (with Job Snijders)

- **Why**: A routing-security postmortem plus measurement study showing exactly how IRR-based filtering breaks down and what the replacement path looks like — squarely in the PM's BGP/security interests.
- **What**: Case study of the March 11, 2024 MTS (AS8359) leak of 30,000+ HKIX routes to Lumen and Arelion — exacerbated by AS-MTU, an AS-SET that expands to 43,823 ASNs (~52% of all ~83,617 routed ASNs). bgpq4 against AS-MTU produces a 1.29M-line Junos filter (271k lines even aggregated), covering 1.8 billion of the ~3 billion IPv4 addresses in the table. 2,192 AS-SETs expand to over 1,000 ASNs; nested recursion mixes customer/peer/IXP-member semantics — one traced chain runs Ukraine → Bulgaria (Balkan-IX) → NL-IX → Russia (TTK) → China (CN2) → South Africa → CTGNet → Rostelecom, ending at an *unrouted* ASN. Expansion also varies by source IRR (APNIC/RIPE/RADB), so authoritative sources must be declared in PeeringDB.
- **How**: Demonstrated with bgpq4, Job's `irrtree`, and bgp.tools data; proposed hygiene (minimum membership, minimal recursion) acknowledged as unrealistic at global scale, with the real fix being RFC 9234 (BGP roles / in-band leak signaling) plus RPKI ASPA verification and future signed prefix lists.
- **Where applicable**: Any operator generating BGP filters from IRR AS-SETs — no special scale required. The ASPA/signed-prefix-list direction is the globally relevant follow-on for route-leak mitigation.

### How far can you get with IX Route Servers?

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-08-BenCartwrightCox.pdf) · [Recording](https://www.youtube.com/watch?v=6yapG6nV7O0)

Ben Cartwright-Cox — bgp.tools / Port 179 LTD

- **Why**: Takes a peering design question ("can I run route-server-only?") and answers it with real measurement, using a genuinely clever data-plane technique for the part BGP cannot signal. Directly relevant to BGP/peering work.
- **What**: Across 113 IXes (bgp.tools collector presence), outbound RS-only reachability is 56.6% of the IPv4 DFZ (557,996 of 986,502 prefixes) and 60% of IPv6. Inbound is the surprise: BGP gives no "I accepted your prefix" signal, so he announced a dedicated prefix (203.10.63.0/24, courtesy APNIC/Geoff Huston) to all route servers, then pinged known-responsive hosts *sourcing from that prefix* — replies return only if the target network actually imports RS routes. Result: only 14.3% of testable prefixes can reach an RS-only network; 85% cannot. Three big European IXes alone yield 12% vs 14.3% for all 113 — a small set of large downstream-heavy networks dominates. Many networks export to RS; few import (131k vs 558k prefixes).
- **How**: RIB-diffing for outbound; ICMP-source-prefix probing via bgp.tools "IX satellite machines" for inbound, reusing its naughty-packet detection pipeline to attribute which networks replies came from (top sources: BBIX Tokyo/Singapore, DE-CIX FRA — China Mobile Intl, Bharti, FPT, Telkom Indonesia, RETN, EdgeUno).
- **Where applicable**: Survey is specific to the 113 IXes bgp.tools inhabits (notably excluding Equinix IX and Internet Australia/IX Australia). Caveats stated by the speaker: 60% of prefixes ≠ 60% of traffic (eyeball traffic concentrates in ~5 ASNs), and more-specific TE announcements aren't captured. Oceania-only RS presence yields just 4.8%/0.51% depending on direction. Directly useful for transit-vs-RS-only strategy in the region.

### Defending Telco Networks

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-08-AnthonySchofield.pdf)

Anthony Schofield — Vocus

- **Why**: A concrete, staged attack/defense walkthrough of router-plane compromise using only native device functionality — exactly the operational security depth the PM values, and unusually detailed for an operator conference.
- **What**: An LOTL (living-off-the-land) kill chain against telco gear, explicitly derived from Vocus wargames/tabletops, not production: (1) initial access via an exposed SNMPv2 RW community on a BNG — legacy "best practice" strings now brute-forceable; config exfiltrated via SNMP-set copy-to-TFTP, then an SSH backdoor provisioned via SNMP sets; (2) credential harvesting using the router's own packet-capture utility to grab RANCID credentials and the TACACS+ secret, decrypted offline; (3) lateral movement on the rancid service account — indistinguishable from normal rancid logins, hiding in plain sight; (4) persistence via IOS XR application-hosting to spawn an SSH daemon (port 57722) in the underlying Linux shell. Defenses per stage: control-plane ACL compliance automation, SNMP brute-force alerting, RadSec, SIEM alerting on "Configured from x.x.x.x by SNMP" (should never happen), least-privilege lockdown of service accounts and jump hosts, no device-to-device lateral movement, MFA on jump hosts, microsegmentation, retiring legacy, plus passkeys/EDR/NDR.
- **How**: Live demos against a real, internet-connected lab ("Bozo Networks", documented at bozo.net.au), each attack stage paired with specific countermeasures; references the CISA/ASD joint advisory of 28 August.
- **Where applicable**: Explicitly hypothetical/wargame material, not a production postmortem — but the patterns (SNMP RW, RANCID credential risk, vendor Linux shells on routers) are generic and apply to any operator with legacy Cisco gear. Cisco-centric examples; the control-plane discipline transfers to any vendor.

### A smaller NBN Aggregation Network

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-10-CraigAskings.pdf) · [Recording](https://www.youtube.com/watch?v=SPfKzz3Awek)

Craig Askings — Telair

- **Why**: A small-operator counter-trend worth attention: using long-reach optics over leased dark fiber to *collapse* a distributed aggregation footprint into a few DCs, on whitebox hardware. Physical interconnect economics in the wild.
- **What**: Triggered by NBN pricebook changes (10GBaseER NNI activation/MRC drops, plus Infraco dark-fiber offers between DCs and POIs), Telair redesigned: 10GBaseER NNI on dark fiber back to nearby DCs, collapsing 39 POIs into 8 PoPs, 82+ routers down to 16 (2 per PoP), and bringing 5 DCs on net. Hardware: Ufispace S9510-28DC whitebox (24×25G SFP28, 2×400G QSFP-DD OpenZR+, 2×100G) running IP Infusion OcNOS with the MPLS license. Migration was executed in batches (single POI → multi-POI batches → mopup, sequenced state by state), i.e., ordinary churn. The deck also flags real DC cross-connect economics: NEXTDC's single cable licence fee vs. Equinix charging per tie-cable pair vs. Polaris free within the carrier room; Vocus DC cross-connects "close to impossible" to organize.
- **How**: Long-reach ER optics over point-to-point dark fiber let the L3 NNI handoff physically live in the DC instead of at each POI — the whole aggregation layer follows. Amusing fiber-path reality checks included (2.5km by road = 12km fiber; 31km road = 81km fiber path).
- **Where applicable**: Australia/NBN-specific economics (pricebook, Infraco DF offers) — the constraints are org- and market-specific. But the technique (ER/ZR+ optics + whitebox + DF to consolidate scattered handoff points into DCs) transfers to any metro/regional aggregation design, and the DC cross-connect pricing comparison is useful for any co-location strategy.

## Adjacent

### Rethinking Network Troubleshooting: Smarter Tools and Better Visibility at Nexthop

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-01-DavidBrown.pdf) · [Recording](https://www.youtube.com/watch?v=f0u0XZHcrDs)

David Brown — Nexthop

- **Why**: An honest walk through monitoring blind spots — especially optics — and a buildable open-source visibility stack. The optics lesson alone is worth the PM's time.
- **What**: A "typical fault process" case: intermittent loss, everything looks fine, eventually reproduced with sustained pings — root cause a marginal optic (RX -18.86dBm, a 10km optic inside a DC). Hard-won lesson stated bluntly: "optics die a slow death and TX monitoring lies all the time," and monitoring is too inward-facing. The response: ping-all-the-things mesh (8.8.8.8 the most-pinged target, 1.1.1.1 second), a flow pipeline of pmacct (sFlow+BGP) → Kafka → ClickHouse → Grafana correlated with Telegraf/SNMP, and a custom Python daemon (`PingMonitorAgent`) running natively on Arista EOS via the agent framework — Kafka-driven ping targets, fping processes per source interface/IP/VRF, results keyed by router_id and if_index so they join cleanly with sFlow data, with ProcMgr auto-relaunch on crash.
- **How**: EOS agent framework for in-switch active probing; pmacct/Kafka/ClickHouse for per-AS loss/jitter dashboards. Includes an Arista-as-Linux exploration (network namespaces, iperf on the switch CPU: 237Mbps, then 1.21Gbps after stripping iptables and control-plane protection — a lab demo, not a recommendation).
- **Where applicable**: Nexthop is a small Australian DC/hosting operator; the pmacct pipeline and RX-power alerting are broadly adoptable. The in-switch agent portion is Arista EOS-specific. Good source of adoptable tooling patterns rather than strategy.

### Network State Checking: A Case Study in Automation

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-02-CraigHenderson.pdf) · [Recording](https://www.youtube.com/watch?v=FL28XtauK7o)

Craig Henderson — REANNZ

- **Why**: A model case study in migration-verification automation with an unusually honest evaluation — including the incidents the tooling failed to catch and its structural limitations.
- **What**: During a national hardware refresh (~97% generated configs, 8–12 member handovers per 3-hour nightly window), REANNZ built tooling to snapshot all per-interface state pre/post-migration — link/MTU/optical RX, VLAN push/pop, EVPN multi-homing forwarding/blocking status, BFD session state, BGP neighbors with routes received/accepted/advertised, OSPF adjacencies — and diff it so the engineer's attention goes to the most-likely-broken services. The "trial" section is the gem: three real incidents (omitted BGP domain attribute causing loop detection to suppress active routes; omitted MTU isolating a remote region; omitted downstream BGP config), each with a verdict — tooling innocent, tooling available-but-unused, or no tooling ("terrible engineer"). Stated limitations: the tool only knows what it knows (unanticipated config flies under the radar), network-as-source-of-truth doesn't scale for service metadata, and the approach is network-centric, not service-centric.
- **How**: The "Bender" automation monorepo (unified config parsing since 2019, generator library for standard configs) feeding pre/post state capture and diffing; next step is an intent database plus an orchestration layer owning service lifecycle, with custom config managed inside the orchestrator for visibility.
- **Where applicable**: REANNZ NREN context (member handovers, perfSONAR) is org-specific, but the pattern — automated state-diff verification plus honest post-hoc attribution — transfers to any refresh/migration project, DC or otherwise.

### Cryptography in the Quantum Era

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-01-PareshKhatri.pdf) · [Recording](https://www.youtube.com/watch?v=hqlpCY1CUVk)

Paresh Khatri — Nokia

- **Why**: PQC migration affects the PM's identity/PKI portfolio (TLS, certificates, protocol auth). This is a primer, but it carries a current, vendor-neutral snapshot of the standards and policy timelines.
- **What**: The standard framing, done well: Shor breaks RSA/DH/ECC (breaking RSA-2048 estimated at ~4,000 logical qubits / 100M gates vs. today's hundreds of qubits); Grover only halves symmetric strength, so AES-128 remains fine; the present-day threat is HNDL — harvest-now-decrypt-later — with expert-survey "Q-Day" estimates as early as ~2030 and the explicit note that we won't be told when a CRQC first exists. Mosca's inequality (x + y > z) drives migration urgency. Standards snapshot: NIST FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA), HQC selected as an ML-KEM alternative; IETF hybrid PQ/T key-exchange and signature drafts for TLS 1.3 and IKE/IPsec; 3GPP PQC studies in 6G Rel-20 with normative specs targeted at Rel-21. Positioning: QKD (physics-based, point-to-point key distribution only, eavesdrop-detectable, ETSI GS 0014 interfaces) and PQC as complementary — QKD for symmetric key distribution on fixed paths, PQC for authentication and key agreement at scale. Strategy: crypto-agility plus layered defense-in-depth starting now.
- **How**: Explanatory, from qubit/superposition basics through HNDL attack flow to a migration decision framework.
- **Where applicable**: Vendor (Nokia) educational talk with an IP-transport lens — the standards/timeline content is global and vendor-neutral. For a PM already deep in identity this is closer to a checklist than news; its value is the consolidated IETF/3GPP status and the QKD-vs-PQC boundary, which is directly relevant to certificate/protocol roadmaps.

### Designing a mikrotik cgnat solution that scales

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-02-MatthewEnger.pdf) · [Recording](https://www.youtube.com/watch?v=2rpbAIkkARg)

Matthew Enger — Leaptel

- **Why**: Solid operator content on cheap whitebox CGNAT — and the static-port-block logging pattern is a genuinely smart answer to a hard compliance problem.
- **What**: Leaptel (~70k subscribers, >300G national aggregate) built CGNAT on Mikrotik CCR2216 (~$5k AUD/box; 2×100G + 12×25G; 16 ARM cores; ~42G real-world "conditions apply"). Law-enforcement logging is solved by *static* port allocation — 250 (currently) / 200 (new design) ports mapped per CGNAT customer IP, so the only record needed is the RADIUS entry for the CGNAT IP plus a lookup table; no per-flow NAT logs. Redundancy: VRRP toward the BNGs, BGP toward an L3 switch with AS-prepend per box and address-list-partitioned pools, all NAT rules pre-staged on both boxes; `tcp-established-timeout` cut to 31 minutes to stretch conntrack (max 1,048,576 entries) across ~7,000+ services. Failover testing: VRRP takeover in ≤3s, but conntrack resets on cutover — impact minutes, and QUIC's path-validation may stretch recovery to ~30s. Honest limitations: ~75% CPU on some cores, no dynamic port allocation on Mikrotik, occasional spontaneous reboots (recovers quickly), and load distribution across appliances still unsolved.
- **How**: Full config walkthrough (VLANs/VRRP, ROS7 BGP templates/connections/filters, the Mikrotik wiki's CGNAT port-block script generating hundreds of chained NAT rules, fasttrack with HW offload), all validated on a spare-parts test rig (two Mikrotiks plus a mock BNG and an Arista L3 switch) before production.
- **Where applicable**: Leaptel-specific scale and traffic; best suited to small/mid ISPs — the largest east-coast sites are moving to a commercial CGNAT solution and the freed hardware bolsters other sites. The static-port-block logging pattern and the failover/conntrade-off lessons transfer broadly.

### The comfortable complexity of Overlays

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-09-ClaudiuCaptari.pdf) · [Recording](https://www.youtube.com/watch?v=fbZDDJb0sdM)

Claudiu Captari — Arista

- **Why**: The "EVPN everywhere" architectural argument, cleanly organized — useful as the current vendor-consensus view on unifying DC/campus/WAN overlays, which the PM touches via DC fabric work.
- **What**: The case for EVPN as a single service plane across domains, with transport chosen per domain: VXLAN where bandwidth is cheap (DC/campus leaf-spine with ECMP), VXLAN-over-IPsec / Secure-EVPN for branch, SR/SRv6 for bandwidth-constrained or TE-needing WAN — stitched by EVPN gateways (RFC 9014) that re-originate type-2/type-5 routes with new next-hop/encapsulation per domain, providing hierarchical flood-list scaling for BUM traffic and reduced EVPN state churn across domains. Includes the full EVPN RFC map (7432, 8214, 8365, 9135/9136, 9014, 9251, OISM) with ~48 active drafts, EANTC multi-vendor interop testing across six testbeds, high-speed in-flight encryption options (MACSec, IPSec, VXLANsec), and SRv6 use cases including AI-fabric TE where the *server NIC* computes and applies SRv6 encapsulation and leaf/spine nodes just perform uSID forwarding.
- **How**: Architecture pitch built on open standards: gateway route re-origination, all-active multi-homing, symmetric/asymmetric/centralized IRB, OISM multicast, FlexAlgo and dynamic SR-TE for the WAN.
- **Where applicable**: Arista session — an architecture pitch for a consistent operational model, though grounded in open RFCs and EANTC interop rather than proprietary features. Relevant to multi-domain enterprise/DC designers evaluating overlay convergence; the domain-by-transport mapping is the transferable part.

### Transport Protocols Evolution or how to migrate your configuration today.

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-04-AlexMitev.pdf) · [Recording](https://www.youtube.com/watch?v=O664YnFGpbQ)

Alex Mitev — Cisco

- **Why**: Practical, config-level RSVP-TE→SR migration guidance for WAN transport — complements the Arista overlay talk with the "how to actually move" side.
- **What**: Historical framing of RSVP-TE's scaling failure (headend 8k→32k and midpoint 64k→256k state growth, k·n² core state, no inter-domain) versus SR's state-in-the-packet model, then a use-case ladder: Ti-LFA for post-convergence-path FRR with 100% coverage and ECMP backups (replacing the hard-to-complete RSVP FRR configurations shown in full); microloop avoidance via segment-routing with RIB-update delay; Flex-Algo covering ~80% of transport intents with metric+constraints (delay, affinities, SRLG); explicit SR paths for the 5–10% needing strict/weighted SID lists; on-demand nexthop + automated steering (~95% of use); disjointness; guaranteed-bandwidth circuit-style policies with SDN-controller-managed reservation and QoS admission control; auto-bandwidth (RSVP-style behavior without midpoint state); tactical TE for congestion mitigation. Full IOS XR config snippets throughout, and an RFC reference set (8402, 8754, 8986, 9252, 9256, 9350, 9352, 9259, 9503, 9800).
- **How**: Config-first teaching: each ladder rung gets its problem statement, config, and a "share of use cases" estimate.
- **Where applicable**: Configs are Cisco IOS XR-specific; the concepts and RFCs are multi-vendor (and overlap with the Arista WAN-SR content). Most useful to operators with existing MPLS/RSVP estates planning incremental SR migration. Vendor-educational rather than a product pitch.

## Wildcard

### How geopolitics is rerouting submarine cables

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-05-JocelinnKang.pdf) · [Recording](https://www.youtube.com/watch?v=1S9CBUmAkXs)

Jocelinn Kang — Nodalys

- **Why**: Not something the PM would search for, but it reframes intercontinental capacity planning as a geopolitical exercise — cables now follow politics and hyperscaler balance sheets, not shortest paths. This changes how long-haul interconnect and DC site decisions get made.
- **What**: The subsea industry's two new shapers: hyperscalers — Google, Meta, AWS, Microsoft account for >70% of global subcable bandwidth usage (2023), connecting data centers rather than population centers and vertically integrating supply chains (cables in service grew from ~130 in 2010 to 570 in 2025) — and geostrategic competition, exercised through permits and licenses (increasingly hard Chinese permits for South China Sea routes, so installers avoid the SCS; US opposition to US–China/Hong Kong landings, rerouting systems to SEA and Australia) and supply-chain exclusion. Case studies: PLCN, BtoBE→CAP-1, SEA-ME-WE 6, SJC2. Also covered: minilateral state partnerships (Coral Sea, Palau, East Micronesia, Google's Pacific Connect including Tuvalu), historical wartime cable cutting (1898, 1914), peacetime surveillance (Ivy Bells, Snowden disclosures), current hybrid-warfare activity (Baltic and Taiwan cable incidents, Salt Typhoon, an attempted cyber attack on submarine-cable management systems in Oahu), and the net effect: Hong Kong losing hub appeal while Australia rises as a safer Indo-Pacific route and digital hub.
- **How**: Case-study narrative with maps and a breakdown of the concrete levers (permits, licenses, vendor participation, vessel access) through which governments now shape physical topology.
- **Where applicable**: Analyst/consultant perspective with no hands-on technique — but directly relevant input to anyone doing trans-Pacific capacity planning, DC site selection, or evaluating route diversity claims on submarine cables. Australian-market lens.

### BFD going down... from BGP timers expiring?

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-09-LouisJarasius.pdf) · [Recording](https://www.youtube.com/watch?v=Ldsz3tRvEX8)

Louis Jarasius — 5GN

- **Why**: The title alone signals an obscure control-plane protocol interaction (BGP timer expiry manifesting as BFD failure) — the kind of datapath/control-plane quirk worth knowing about given the PM's BGP-internals interest, and the sort of thing that bites silently in production.
- **What**: Unknown — no abstract was published for this session and no materials could be extracted; the program lists title, speaker, and links only. Assessment is from the title alone.
- **How**: Not determinable from available materials; the slides and video links are published and should be reviewed directly.
- **Where applicable**: Appears to be a 5GN operational case study; flagged here on the strength of the topic, with the explicit caveat that the write-up could not be grounded in source material.

## Themes

- **AI clusters are the new design driver**: Nokia's collectives/tail-latency/SU framing, Cloudflare's "AI demands on the carrier network" (bursty elephant flows, congestion), and Arista/Cisco's SRv6-based AI-fabric TE all point the same way — the next DC fabric generation is being designed around synchronized elephant flows, not steady-state cloud traffic.
- **Packet-optical convergence is real and shipping**: AARNet's 400G ZR+ pluggables directly into routers (transponders at 150W→25W) and Telair's ER-optics-over-dark-fiber consolidation show coherent pluggables physically re-shaping interconnect economics at both NREN and small-operator scale.
- **Scale-down as a counter-trend**: alongside hyperscaler talks, the program features two operators shrinking hardware footprints profitably (Telair's 82→16 routers; Leaptel's $5k whitebox CGNAT) — whitebox economics have reached aggregation and broadband edges.
- **Demand for precise, standards-based signals over self-asserted data**: AWS's discard-classification draft, Kentik's AS-SET pollution analysis (with RFC 9234/ASPA as the fix), and bgp.tools's RS measurement all reflect the same push — replace folklore-grade data (IRR sets, vendor drop counters, "I import from the RS, trust me") with classified, measurable, or cryptographically verifiable signals.
- **Honest evaluation as a genre**: REANNZ's "tooling on trial" (with incident-by-incident verdicts), Vocus's wargame-derived attack chain, and Nexthop's failed-troubleshooting walkthrough all model the postmortem discipline the best operator content is built on.
- **Automation maturing from scripts to intent**: REANNZ's progression (one-off scripts → config-parsing monorepo → intent database + orchestrator) and AARNet's NSO/YANG service models echo AWS's closed-loop pipeline — network-as-source-of-truth is being retired across the board.
