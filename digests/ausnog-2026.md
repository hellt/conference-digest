<!--
conference: AusNOG 2026
type: operator
source_url: https://www.ausnog.net/events/ausnog-2026/program
generated: 2026-11-02
registry_key: ausnog-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AusNOG 2026

A note on sources: no abstracts were published for this program — titles and speakers only. The write-ups below are grounded in the slide decks ToFaRev extracted from each session. Two sessions (the Unit 42 security talk and the opening keynote) have no published materials at all; they are flagged inline.

## Core

### Return loss problems associated with faster optical networks

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/TakayaNakagawa-NTT.pdf) · [Recording](https://www.youtube.com/watch?v=QZF0pWCU45I)

Takaya Nakagawa - NTT Advanced Technology Corporation

- **Why**: As links move from 10G to 100G/400G and beyond, reflections at connector points — not just insertion loss — become an error source. This is core physical-layer optics knowledge for anyone running DC or WAN fiber plants, and it comes with real experimental data rather than folklore.
- **What**: A controlled demonstration that 100GBASE-LR4 links develop bit errors when *total* return loss degrades below the IEEE limit (21 dB) across multiple connection points. A single poor (<21 dB) connection point did not immediately produce errors, but three poor points did, via multiple reflections between connectors (eye closure, jitter, rising BER). BER worsens as received power drops, and the three transceivers tested showed materially different tolerance to poor return loss. The talk also catalogues causes: dust contamination takes a clean connector pair from 0.05 dB IL / 52.6 dB RL to 1.1 dB / 22.7 dB; hand oil to 44.2 dB RL; a partially seated connector hit 13.8 dB RL; legacy PC polishing only guarantees ~25 dB. Notably, poor reflection points spaced 20 km apart produced no errors — the reflected signal is attenuated over distance.
- **How**: Testbed of a 100GBASE-LR4 link with variable optical attenuator and deliberately poor connectors, measuring eye diagrams and BER across three transceiver vendors; PAM4 (400G+) flagged as even more exposed since it is now mainstream.
- **Where applicable**: Any single-mode plant with dense patching — meet-me rooms, DC cross-connects, ROADM/MUX shelves — especially at 100G+ and at low receive power. Broadly applicable physics, though NTT-AT sells connector cleaning/polishing products, so the "Clean Before Connect" conclusion aligns with their business.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/ThomasWeible-Flexoptix.pdf) · [Recording](https://www.youtube.com/watch?v=oB5cn_QkArk)

Thomas Weible - Flexoptix

- **Why**: DWDM topology planning for the 800G/1.6T coherent era — squarely in the PM's physical WAN interconnect interest. This is about how to structure a C-band plant so future superchannels don't strand you.
- **What**: An argument for planning DWDM networks in frequency terms (THz/GHz) rather than channel numbers or wavelengths, and for a "colorless," flexible architecture: carve the C-band into 12 × 400 GHz subbands using low-cost PLC 1×4 splitters to combine TX / split RX, and run each subband through ordinary 50 GHz DWDM MUX/DeMUX. This yields DIY coherent superchannels (425 Gbps @ 53.125 GBd dual-polarization 16-QAM per the deck) that can be re-arranged as optics evolve. The deck also notes ~100 GHz spacing as the observed optimum (attributed to Blake Willis), 800G ZR+ in DD/OSFP form factors arriving, 12.8T liquid-cooled XPO optics approaching, 300 GHz options appearing, and that coherent BIDI needs a second laser for the RX local oscillator.
- **How**: Coherent intradyne detection with phase- and polarization-diversity balanced receivers; higher-order modulation constellations (4 bits/symbol × 2 polarizations); superchannels assembled from COTS PLC splitters plus standard DWDM muxes; "make a frequency plan for your spans."
- **Where applicable**: Operators building or re-planning their own DWDM plant. This is a vendor session (Flexoptix sells tunable optics), but the frequency-plan method and superchannel construction approach are vendor-neutral engineering. The slide text is fragmentary and fast-paced; expect the talk to be denser than the deck.

### Securing modern telco networks

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/PatrickOhearn-AARNET.pdf) · [Recording](https://www.youtube.com/watch?v=YGl8yffnySs)

Patrick Ohearn - AARNet Pty Ltd

- **Why**: A practitioner's prioritized view of what actually matters in SP security right now — fundamentals, PQC, routing security, and the AI vulnerability-discovery wave — directly in the PM's network security core.
- **What**: A survey of telco security practice, organized by layer: fundamentals (backups, SSO/RBAC, MFA on external paths, segmentation, per-device credentials, never sharing auth between corporate and telco domains, JIT access, one-time break-glass creds, jumphost controls); NOS hygiene (consistent config/software deployment, vendor hardening guides, disable telnet, CoPP/RE filters, alert on reboots and firmware/software changes, investigate all coredumps); supply chain (signed package updates, trusted computing, vetted suppliers, less second-hand gear, secure shipping); hardware (SecureBoot, physical security, real-time inventory change logging, passive asset monitoring, cameras); OSS/BSS (billing is a prime target, CDRs and metadata are espionage targets, JIT for external vendors/contractors, audit SaaS access). Notable current items: frontier-lab security models (Cisco, Juniper/HPE, Nokia working with frontier labs) have surfaced ~10,000 high/critical vulnerabilities; patch velocity is rising to fortnightly NOS updates; transport encryption should be pushed at L1 (OTNSec, WDM encryption) through L4; PQC is coming sooner than expected and impacts SecureBoot/package signing (potentially requiring new hardware) more than transport; routing security = RPKI, route filtering, BGP enforce-first-AS, OTC (RFC 9234), and ASPA (draft — APNIC support as of July 2026). Core message: fundamentals matter most; vendor QA is lagging; make encryption a purchase criterion.
- **How**: A field-informed checklist rather than a single mechanism, closing with industry collaboration (peer telcos, ASD/Home Affairs, conference lists).
- **Where applicable**: Broadly applicable to any SP/telco; the regulation references (SOCI/TSRMP, CI Fortify) are Australian-specific, but the technical content is general.

### Revocation

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/GeoffHuston-APNIC.pdf) · [Recording](https://www.youtube.com/watch?v=YsH63Pr1jrw)

Geoff Huston - APNIC

- **Why**: Directly in the PM's identity/authentication core. PKI revocation assumptions underpin everything from Web TLS to workload identity — and this talk empirically shows revocation does not work in practice.
- **What**: A live experiment: generate a Let's Encrypt certificate, revoke it, wait weeks, and check browsers. Only Firefox had learned of the revocation; Chrome (which disabled OCSP in 2012 and never supported Must-Staple) and Safari (CRLset-style downloads plus stapled OCSP) did not. The talk walks the whole failure chain: CRLs are too large and weekly-fresh (a DigiCert example with 17,527 entries); OCSP adds latency, leaks client activity to the CA, concentrated load (Akamai once answered 2/3 of Let's Encrypt OCSP), and forces fail-open (DDoS vector) or fail-closed (availability vector) choices; stapling adds nothing because a server holding a revoked cert would never staple its own revocation. Conclusion: revocation is unfixable within X.509 — shorter cert lifetimes bound the damage but CA infrastructure can't scale to hour-long lifetimes. The provocative alternative: DANE — put DNSSEC-signed public keys in the DNS with TTL-scale freshness and staple the DNSSEC chain into the TLS handshake, eliminating the CA third party entirely.
- **How**: Demonstration-first methodology (generate/revoke/wait/check across Chrome, Safari, Firefox), plus a structural analysis of CRL/OCSP/stapling mechanics.
- **Where applicable**: Universal for anyone depending on Web PKI or designing certificate-based workload/agent identity. The DANE proposal is contrarian and has no browser support — treat it as direction-setting, not deployable. Highly relevant to short-lived-certificate designs (SPIFFE-style) where "we'll just revoke" is a non-answer.

### Mission Possible: Disabling IPv4 on Google Enterprise Network

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/JenLinkova-Google.pdf) · [Recording](https://www.youtube.com/watch?v=mcGKJbji-OU)

Jen Linkova - Google

- **What**: Google's production rollout of "IPv6-mostly" networks (RFC 8925 DHCPv4 Option 108) across its enterprise network: clients that signal Option 108 receive no IPv4 address and run IPv6-only with NAT64, PREF64 signalled in Router Advertisements (RFC 8781/9872), DNS64, and CLAT (464XLAT, RFC 6877) for IPv4-literal and legacy apps. Rollout ran March–December 2023 (pilot → greenfields first → incremental 10%→100% of existing subnets). Results: no blocking issues; Apple/Android/ChromeOS devices went IPv6-only automatically; 75–80% of hosts became IPv6-only; DHCPv4 utilization dropped 3–4× on WiFi segments; 500K+ IPv4 addresses reclaimed (a /19 was downsized to /22). Documented pitfalls: devices with disabled/link-local-only IPv6, extension-header filtering breaking ESP (VPN, WiFi calling), APs blocking multiple IPv6 addresses (and multiple EVPN Type-2 routes), tethering/hosts-as-routers breaking, and Happy Eyeballs masking IPv6 bugs ("users do not report problems; network bugs remain unfixed").
- **Why**: IPv4 reclamation is a live operational problem everywhere; this is the most complete public deployment data on the IPv6-mostly pattern, and it's directly relevant to IPAM and enterprise addressing strategy.
- **How**: Standard-track mechanisms only — Option 108 in DHCPDISCOVER/REQUEST parameter list, NAT64 at site edge, RA-signalled PREF64, CLAT on the client; the dedicated IPv6-only SSID/VLAN approach is explicitly rejected (user confusion, higher IPv4 consumption, low issue visibility).
- **Where applicable**: Enterprise/campus wired + wireless with central DHCPv4 and SLAAC. The specific numbers are Google-scale, but the technique is deployable now wherever clients are Apple/Android/ChromeOS (they send Option 108 by default); Linux requires manual opt-in; Windows is the open gap. Prerequisite: IPv6 must already genuinely work.

### Migrating a Large Telco Networks IGP from OSPF/OSPFv3 to ISIS

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/SamFaunt-ABB.pdf) · [Recording](https://www.youtube.com/watch?v=Rw0IUguOsAM)

Sam Faunt - Aussie Broadband

- **Why**: IGP migrations at telco scale are rare war stories with real failure detail — core routing/WAN interest, and a candid postmortem-style account of what broke.
- **What**: Aussie Broadband moved its backbone IGP from OSPF/OSPFv3 (two processes for two address families) to IS-IS, motivated by one protocol for v4+v6, unifying the IGP across AS4764 and AS9268, segment routing readiness, and vendor support. Method: lab first (convergence testing, choosing FRR/SRLG-disjoint/node-protection/microloop-avoidance features, prefix policy — loopbacks only vs loopbacks + links, OSPF/IS-IS coexistence on the same box, cross-platform behavior); deploy IS-IS alongside running OSPF; cut over by lowering OSPF/OSPFv3 admin distance below IS-IS so IS-IS takes over. AS4764 cut over cleanly. During AS9268, traffic blackholed — the RIB still preferred OSPF for some loopbacks; they assumed stale routes, rebooted the core router, and it did not come back. The network was eventually migrated fully to IS-IS.
- **How**: Admin-distance-based cutover with both IGPs running simultaneously; phased AS-by-AS; lab validation before deployment.
- **Where applicable**: SP/telco backbones running dual OSPFv2/v3. The specific blackhole and failed reboot are org- and platform-specific, but the lab-first, coexistence-then-cutover method is broadly transferable. The slides are thin on detail — the talk is likely richer than the deck.

### BGP EVPN. A view from the field

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/AlexMitev-Cisco.pdf) · [Recording](https://www.youtube.com/watch?v=FjdYI9RIoGM)

Alex Mitev - Cisco System

- **Why**: EVPN is consolidating L2/L3 service delivery and DCI under one BGP control plane, and this is a field-density walkthrough of design options and — most valuably — in-service migration paths from legacy redundancy schemes. Relevant to both DC fabric and telco access work.
- **What**: The core framing: EVPN (RFC 7432/7623/8214/9135) replaces MC-LAG/ICCP, ICCP-SM, nV Edge, and VPLS flood-and-learn by moving coordination into BGP — deleting peer-links and sync protocols, eliminating split-brain, enabling N-way multi-vendor multihoming; risk changes shape ("more failure events, smaller blast radius — each one survivable"). Multihoming modes mapped: all-active (per-flow), single-active (per-VLAN), port-active (per-port), plus single-flow-active for L2 ring protocols (G.8032/STP-AG). Migration recipes with actual IOS-XR config: MC-LAG → port-active EVPN (no CE change, NDF sets LACP out-of-service, then ICCP removed); VPLS → EVPN (add EVI, PEs auto-discover, pseudowires shut down; both VFIs and EVIs default to split-horizon group 1 so no PE forwards between them during transition); VPWS seamless integration where EVPN VPWS is preferred over the legacy PW when both exist for the same AC; nV Edge is the one migration requiring downtime (de-clustering). Also covers hierarchical EVPN (EVPN-HE) with P-bit/B-bit service carving, flexible cross-connects to bundle thousands of services into fewer tunnels (cutting BGP state and OAM), and real Australian use cases: RSPs delivering BNG services over EVPN with SRG-driven service carving, and wholesale fan-in (thousands of L2 sub-ifs onto BNG pairs) solved via VLAN-aware FXC and L2 NNI handoff.
- **How**: Config-level sequencing and DF-election/service-carving modes (preference-based, access-driven, srg-driven) with show-command output from a lab.
- **Where applicable**: SP access/aggregation and enterprise DCI. This is a Cisco SE session with IOS-XR-specific configs — vendor-flavored, but the design concepts and migration orderings are multi-vendor standards work and directly reusable.

### Rethinking Address Reality: IPv4 Utilisation and Proxy Network Exposure in Australia

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/AftabSiddiqu-APNICFoundation.pdf) · [Recording](https://www.youtube.com/watch?v=72gu9nlu384)

Aftab Siddiqui - APNIC Foundation

- **Why**: Two halves, both valuable: ground-truthing Australian IPv4 holdings/geolocation (registry data vs reality), and a genuinely novel measurement of residential proxy networks — including a NetFlow-based detection technique consumer ISPs can deploy today. The proxy half is a network-security problem that lands on operators' laps.
- **What**: Part 1: NRO delegation data shows Australia actually holds ~45.9M IPv4 addresses (179K /24s, 9,867 delegations) vs what APNIC REX presents; transfer analysis shows Australia is a net *exporter* of IPv4 (net −500 transfers / −2.1M addresses over ten years). Only 5.3% of AU delegations publish RFC 8805 geofeeds (94.7% silent), with common breakage (GitHub blob URLs returning HTML, dead URLs); cross-checking commercial (IPinfo) vs geofeed data shows 99.97% country agreement but only ~80.5% city agreement, with commercial data biased toward capitals. Part 2: instrumented five residential proxy providers (Oxylabs, IPRoyal, FloppyData, Shifter, Bright Data) with ~500K requests, 28,217 unique exit IPs across Sydney/Melbourne/Brisbane: 2,747 IPs appeared in ≥2 providers (Oxylabs–Shifter overlap largest at 1,375); exits concentrate in consumer ASNs (Telstra 6,668, TPG 4,776, Optus 3,099, Aussie Broadband 2,571, Starlink 1,925); and TCP timestamp-rate fingerprinting (fitting TSval slope within connections) clustered exits into ~1000/300/250/100 Hz families (70.8% at ~1000 Hz) — a device-class signal the proxy relay cannot fake because the exit's own kernel builds the segments. The exits never fetched any sub-resource (zero of five tracking pixels loaded).
- **How**: Per-provider hostnames + per-request tokens to join client and server logs; SYN pcap analysis (TTL, MSS, window, TCP option order); timestamp-rate fitting requiring ≥3 samples over 250 ms; browser fingerprint page. Operator guidance: proxy SDKs hold persistent outbound connections from consumer CPE to a small set of gateways — visible in NetFlow as long-lived flows to the same destinations from thousands of unrelated subscriber lines, no DPI needed.
- **Where applicable**: The dataset and geofeed findings are Australia-specific; the measurement methodology and the NetFlow detection guidance transfer to any consumer ISP. Provider device-count claims quoted from vendor marketing are explicitly unverified.

### ...because copy+paste isn't a network configuration strategy - automation for amateurs

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/JamesMorgan-Vernet.pdf) · [Recording](https://www.youtube.com/watch?v=PFcfyAzgeic)

James Morgan - VERNet (presented with Mitch Blair, VERNet, per the slides)

- **Why**: A 15-person research network replaced CLI copy-paste and spreadsheet IPAM with NetBox-as-source-of-truth and full configuration generation — a complete, honest, adoptable automation pattern touching IPAM, a core PM interest.
- **What**: VERNet's journey from 2019 ("configs lived on devices, IPAM was a classy spreadsheet, everyone gets read/write") to today: NetBox holds IPAM, L2/L3 hardware inventory, OOB, racks, and config metadata; ConnectMaster holds fiber plant; the OSS holds customer/service records. Golden configs were rebuilt from first principles (a box with no services, plus role-dictated sections); services were classified and their differences turned into properties; Jinja templates (in Git, synced to NetBox) render full device configs. The pipeline: device state change in NetBox → generated candidate config → diffed against the approved repo → pull request → on approval, AWX/Ansible pushes a full overwrite with on-box validation, automatic rollback on failed checks, and commit-confirm; scheduled AWX jobs track drift (running vs approved config) and open GitHub issues on divergence. Refreshingly honest about pain: the first generated config errors out, the second is six lines, "by about the 12th generation you'll get a full config," and the diffing phase surfaced hundreds of edge cases and embarrassing legacy mistakes nobody owned.
- **How**: NetBox + Git + GitHub Actions + AWX + Ansible; config templates inherit; review shifts from config diffs to template diffs; fewer people need write access; provisioning a new box takes minutes.
- **Where applicable**: Small and mid-size networks of any vendor mix. Explicitly framed as "if we can do this, you absolutely can" — though they candidly note they haven't yet decided whether their particular sync approach works for them. Adopt the pattern, not their exact choices.

### Lessons from the State-Sponsored Siege on Core Telecom Infrastructure

Taylor Reed - Palo Alto Unit 42

- **Why**: State-sponsored targeting of core telecom infrastructure is the current frontier of the PM's network security interest, and Unit 42 threat intelligence is usually substantive.
- **What**: **No abstract, slides, or recording are published for this session** — only the title and speaker are available, so the content cannot be assessed. From the title alone, it presumably covers threat intelligence on nation-state actors targeting core telecom/ISP infrastructure, in the vein of the recent wave of edge-router and telco-core compromises.
- **How**: Unknown — no materials available.
- **Where applicable**: Unknown. Flagged as a gap in the published program; worth seeking the speaker's materials or a Unit 42 publication on the topic if the subject matters to you (it should, given this program's AARNet talk names it as context).

## Adjacent

### Architecture and Troubleshooting: A Guide to AWS Peering

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/ChitizShrestha-AWS.pdf) · [Recording](https://www.youtube.com/watch?v=uaLHBiIeL5A)

Chitiz Shrestha - Amazon Web Services (AWS)

- **Why**: Useful for anyone interconnecting with AWS — which spans the PM's DC/WAN interconnect interest — as it explains how AWS actually runs and troubleshoots peering, and what will break maintenance operations on their side.
- **What**: AWS's peering operation explained: AS16509 (public peering), 14618, 7224 (Direct Connect); selective, IX-centric peering (175 IXs, 189 interconnection facilities); regional route scoping — peers receive region-specific routes to localize traffic and keep it off the AWS backbone. Capability matrix: AS-path prepending is their primary TE; RPKI/ROA filtering yes; MD5 optional; BFD and BGP communities *not* supported. Operational content: common issues (link errors, discards, session flapping, non-optimal paths); auto-mitigation with the caveat that "taking the wrong action can be worse than taking no action"; the maintenance workflow (drain via BGP filtering / IGP metric poisoning before work); a hard rule that peers must not static-route to AWS (it breaks their zero-traffic-then-deploy model); and self-service diagnostics — the EC2 reachability checker (first triage step: if the test host is reachable, the problem is WAF/security groups, not peering), RIPE Atlas probes hosted on EC2 (reverse traces, since AWS has no looking glass), and NLNOG Ring nodes. Provisioning is portal-automated (interconnect.amazon with PeeringDB auth) with pre-deployment checks (RPKI validation, no private ASN, stable sessions) and auto-disconnect of dead sessions.
- **How**: Explanation of their internal model plus concrete self-service tooling a peer can use before escalating.
- **Where applicable**: Only relevant if you peer or interconnect with AWS. It is a hyperscaler explaining its own operational contract — informative context, not a transferable technique.

### Assurance on a budget

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/TimWarnock-Superloop.pdf) · [Recording](https://www.youtube.com/watch?v=opHGF4ylx78)

Tim Warnock - Superloop

- **Why**: A catalog of low-cost lab techniques for validating vendor claims, supplier conformance, and regressions — exactly the kind of tooling others can adopt, and the talk openly exists because "vendors often tell porkies about capabilities."
- **What**: How Superloop built an assurance lab on MikroTik CCRs, x86 compute, and open-source software: bulk traffic generation (MikroTik traffic-gen, snake tests that loop ports and multiply traffic uplinks — with pitfalls: rate adaptation hammers buffers, invalid MACs, generated frames with bad CRCs); RtBrick BNG Blaster for emulating PPPoE/IPoE subscribers at scale (tested to 32k sessions on a 10-core server; a multi-hour 4,000-session / 48k pps full-duplex test with zero flaps ran on an HP T740 thin client under Proxmox); MikroTik vCPE for simulating Q-in-Q DHCP subscribers with per-subscriber option-82; ROS7 "fantasy routing" for RIB/FIB stress testing (with the real insight that not all TCAM is the same — LEM vs LPM vs eTCAM, IPv4 vs IPv6 key sizes); scripted Python PCAP generation for traffic no tool produces (16,000 ICMP requests, each with unique source IP, MAC, S-TAG/C-TAG, and valid CRC); tcpreplay/MikroTik PCAP injection with speed control; thousands of RFC-compliant DHCP requests to test CoPP. Process advice: keep a problem register, maintain a regression suite with reference PCAPs.
- **How**: Cheap hardware + open-source tooling, with concrete configs and commands in the deck.
- **Where applicable**: Any operator without a vendor-grade test lab. The NBN TC4 conformance specifics are Australian, but the techniques are general.

### Optimizing Traffic Flow with Akamai

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/KamsYeung-Akamai.pdf) · [Recording](https://www.youtube.com/watch?v=Gzf8wTkVZOI)

Kams Yeung - Akamai

- **Why**: Understanding why conventional BGP traffic engineering does not move a major CDN is operationally important for capacity planning and interconnect strategy at any eyeball network.
- **What**: Akamai maps users via DNS (unicast, per-requester answers based on latency, throughput, loss, server load, cache policy) — not anycast — so AS-path prepending, MED, and more-specific advertisements all do nothing. Clusters are islands (no inter-cluster backbone) with preference on-net cache > PNI > IX > transit. Operator guidance: run your own recursive resolvers with anycast IPs and per-location external IPs (mapping follows the resolver's IP), ACL them, never rewrite Akamai hostnames' TTLs, or else use Google/OpenDNS with ECS; announce complete and consistent prefixes (both DNS and end-user ranges) or risk whole-ASN blocking; carry everything you announce — no holes or filtered /24s, since Akamai edge routers don't hold full tables; don't filter or rate-limit ICMP (used for performance monitoring); avoid CGNAT (or use 100.64.0.0/10 and place caches outside CGNAT); and enable IPv6 — Australia sits at 30.1% adoption, ranked #69, with Telstra at 60.3% and TPG at 24.7%.
- **How**: Explanation of the mapping system followed by a concrete do/don't list for ISPs.
- **Where applicable**: Networks delivering Akamai-served content (i.e., most eyeball ISPs). A vendor session, but framed as operational guidance rather than a product pitch.

### Our journey on "how we are modernising our network"

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/RichardVanderReyden-Optus.pdf) · [Recording](https://www.youtube.com/watch?v=v7HLjDyG7E0)

Richard Vander Reyden - Optus

- **Why**: A large telco's target-state architecture is a useful directional signal for where SP fabrics are heading — SRv6, IGP consolidation, core separation — even if the specifics don't transfer.
- **What**: A history (Bay Networks → Cisco 7200/7500/GSR → Juniper M320/MX960/PTX; VPLS → Seamless MPLS) and a pointed critique of the current state: internet traffic (~90% of volume) sharing a complex telco core (OSPF + LDP + iBGP/eBGP-LU) with in-band management. The target state: internet core separated from telco core, IS-IS + SRv6 end to end (already IS-IS + SR-MPLS in access), dual-vendor dual-plane core, defined interconnects, VxLAN in access, built for 400/800G colored optics, and a dedicated OOB management network (star topology, dual SYD/MEL hubs, carrier-diverse paths). On operations: from manual CLI (typo-outages, no rollback, knowledge silos) to CI/CD with atomic commits and automatic rollback, Git + NetBox + NSO as single source of truth, one YAML intent layer across Cisco/Juniper, continuous drift detection, AI anomaly detection with humans deciding.
- **How**: Architecture-program level description; the deck contains little implementation detail.
- **Where applicable**: Optus-specific scale and topology — a direction signal, not a copyable design. Pair with the Aussie Broadband IGP talk for the IS-IS/SR trend.

## Wildcard

### The CDN Landscape Revisited: Static, Live, and AI

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/SteveMeuse-Kentik.pdf) · [Recording](https://www.youtube.com/watch?v=QHVNPcc_7fQ)

Steve Meuse - Kentik

- **Why**: Not a core PM area, but it carries a genuinely surprising empirical result — AI traffic on real networks is still tiny — plus the clearest available account of CDN market consolidation.
- **What**: Since 2023: Stackpath exited, Lumen's CDN was dismantled, and Edgio went Chapter 11 (AS22822 dark), with roughly 15% market share mostly absorbed by Akamai. Content delivery is commoditized (transit price pressure, no differentiation, hyperscaler bundles); survivors are re-tooling into edge compute/GPU platforms — the deck maps Cloudflare, Akamai, Fastly, and GCore product timelines (Workers → containers → inference; Akamai's Linode/Ondat/Geko/NVIDIA Blackwell), with the strategic asymmetry that CDNs can't match hyperscaler capital but pay zero egress. Live events: mega-streams (72.5M concurrent, T20 World Cup) were handled fine; the Jake Paul–Mike Tyson failure (60M streams, 2.5–3× normal peak) was *not* the network — interconnect and cache capacity had headroom, root cause suspected on the streaming/replication side, no Netflix postmortem. The AI surprise: on a large US SP, video is Tb/s while AI in August 2025 measured in hundreds of Mb/s (~1.5 Gb/s in 2026 samples) — the exec-level panic is hype-cycle artifact, not operational concern; inference is served largely via Cloudflare/Google (Anthropic's $1.8B/7yr Akamai deal noted), and the unknown is agent-driven traffic directionality (per the Schaeffer NANOG keynote), which is not yet visible in flow data.
- **How**: Kentik OTT mapping (DNS queries joined with flow data) plus flow-based unique-destination-IP counts as a user proxy.
- **Where applicable**: Industry-level perspective grounded in Kentik's customer visibility (US-weighted). Best used to calibrate capacity-planning and AI-traffic assumptions.

### Rural Fibre Co

**Links:** [Slides](https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/PhilBritt-RuralFibre.pdf) · [Recording](https://www.youtube.com/watch?v=5XsAALiTEr0)

Phil Britt - Rural Fibre Co

- **Why**: Outside the PM's core areas, but two things here are genuinely novel signals: operational software built by a network engineer with Claude Code in eight weeks, and hard economics on vertically integrated fiber builds.
- **What**: A 16-month-old Gippsland FTTP overbuilder: 1,431 premises passed, 430 connected, 130 km of duct, built by 42 people, targeting 10,000 passed by mid-2029. Key choices: Nokia end-to-end stack (Lightspan MF-2 OLT, Altiplano, 7750 SR-1s) chosen partly so the network is saleable without the founder; a wholesale product deliberately shaped like NBN's (QinQ S-tag/C-tag from ONT to RSP handoff, AVC-style IDs in DHCP option 82) because every Australian RSP already has those integrations — "inventing a better product would mean asking every RSP to build a new integration for a network with 1,431 premises." Automation: no human touches an order until the technician knocks on the door; the design system generates all construction tasks, work orders, inventory, and purchase orders ("the design is the work orders"). The workforce management system was built in eight weeks by a network engineer with Claude Code — zero developers, no PMO — and drill productivity tripled (250 → 775 m/day total) attributed to visibility and gamification rather than the machinery. Take-up against NBN fixed wireless reached 52% at ~9 months. Hard lesson: an unlocated NBN duct got drilled through, taking down ~3,000 premises; asset-locating checks are now enforced in software, blocking tasks until completed.
- **How**: Vertical integration across design → civils → splicing → network → provisioning → billing to eliminate margin stacking and coordination tax; software-enforced process gates.
- **Where applicable**: The regulatory frame (Part 8 superfast broadband obligations, TEBA/POI, open-access wholesale) and the NBN-overbuild economics are Australian. The transferable ideas are the AI-assisted software build and design-as-single-source-of-truth.

### Keynote Presentation : Will Australia be all at sea on national sovereign AI connectivity by 2030?

**Links:** [Recording](https://www.youtube.com/watch?v=JfFB4jjAmAo)

Bevan Slattery - SUBCO

- **Why**: A keynote on sovereign AI connectivity from one of the region's most consequential subsea/DC infrastructure investors is a direct where-is-the-field-headed signal for WAN capacity and interconnect planning.
- **What**: **No abstract or slides are published; a recording exists but has not been transcribed**, so this write-up reflects only the title and speaker. From those, the topic is Australia's international capacity and connectivity position relative to AI-era workloads and digital sovereignty by 2030 — presumably covering subsea cable investment and whether Australia can host and serve AI compute domestically.
- **How**: Unknown from available material.
- **Where applicable**: Australia/Pacific-specific by construction; relevant to anyone whose WAN interconnect strategy depends on trans-Pacific or intra-Asian capacity trajectories. Check the recording.

## Themes

- **The physical layer is back in the program**: two dedicated optics talks (return loss at 100G+/PAM4, DWDM frequency planning for 1.6T) plus 400/800G colored optics in the Optus target state — as speeds climb, connector hygiene, reflection budget, and C-band topology are again operational disciplines, not afterthoughts.
- **IPv6-only as an operational technique, against stubbornly low adoption**: Google demonstrates the IPv6-mostly pattern (Option 108 + NAT64 + CLAT) reclaiming 500K+ IPv4 addresses, while Akamai reports Australia at 30.1% adoption (#69) and both Akamai and APNIC push geofeeds/resolver hygiene as enablers.
- **Telco cores converging on IS-IS + SR + EVPN**: Aussie Broadband's OSPF→IS-IS migration, Optus's IS-IS/SRv6 target state, and the Cisco EVPN field guide (including Australian BNG-over-EVPN deployments) all point the same direction — one protocol, one unified BGP control plane, smaller failure domains.
- **Automation is table stakes, and its center of gravity is the source of truth**: VERNet (NetBox + full config generation at 15 staff), Superloop (lab assurance and regression suites), Optus (Git/NetBox/NSO intent layer) — the pattern is state in a database, generated configs, PR review, automated rollback, drift detection.
- **Security talks returned to fundamentals — and to unfixable brokenness**: AARNet's fundamentals checklist plus PQC and ASPA/routing security, and Huston's empirical demonstration that certificate revocation simply does not work in shipping browsers — a direct input to any short-lived-certificate identity design.
- **AI's impact is on operations, not (yet) on traffic**: Nokia's AI-assisted operations framing, Optus's AI anomaly detection, Rural Fibre's Claude-Code-built workforce system — while Kentik's measurement shows actual AI traffic on SP networks is hundreds of Mb/s against video's Tb/s. This cycle, AI is a network-operations and software-build story; the traffic story is still hype.
