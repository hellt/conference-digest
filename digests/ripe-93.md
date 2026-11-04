<!--
conference: RIPE 93
type: operator
source_url: https://ripe93.ripe.net/programme/meeting-plan/
generated: 2026-11-02
registry_key: ripe-93
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# RIPE 93

## Core

### Digital Coherent Optics Tutorial

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/118/SEVGKR/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/SEVGKR/resources/RIPE93_DCO_Tutorial__Ehb0qFr.pdf) · [Recording](https://ripe93.ripe.net/media/videos/michel-lanners_digital-coherent-optics-tutorial_side_20261026-090035.mp4)

Michel Lanners, LU-CIX

- **Why**: Coherent pluggables (400ZR/800ZR-class) are becoming the default way to light DC-to-DC and metro dark fiber, and spec sheets for them are notoriously hard to read. This is a rare vendor-neutral, operator-led on-ramp to the technology.
- **What**: A full tutorial (grown out of a Euro-IX workshop, co-presented with Flexoptix and Arista) covering fundamentals, choosing optics from standards and datasheets, host compatibility, power and cooling, link/network design, commissioning, monitoring, troubleshooting, and deployment case studies.
- **How**: The material goes deep enough to be useful: NRZ→PAM4 trade-offs (half the spectrum, ~9.5 dB less SNR margin per eye, KP4 FEC RS(544,514)), coherent modulation tables (DP-QPSK for long-haul 100G/200G ZR+, DP-16QAM for 400ZR/800ZR/1600ZR), dual-polarization MIMO equalization tracking PMD and polarization transients, and the line-rate math (a 59.84 GBd 400ZR fits a 75 GHz DWDM slot; 800ZR at 118.2 GBd needs 150 GHz).
- **Where applicable**: Anyone buying or deploying coherent optics for router-to-router or DCI links, on any vendor's platform — the physics and the standards are the same. The form-factor/host-compatibility sections matter for mixed-estate DCs.

### BIRD on an Open Linux Switch: Mainline Linux, switchdev and Hardware L3 Offload

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/143/WQNNDD/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/WQNNDD/resources/RIPE93-Banelli-BIRDT_8guDtE1.pdf) · [Recording](https://ripe93.ripe.net/media/videos/bruno-banelli_bird-on-an-open-linux-switch-mainline-linux-switchdev-and-hardware-l3-offload_side_20261028-093516.mp4)

Bruno Banelli, Novarq d.o.o.

- **Why**: This is a real engineering report on the question every open-networking skeptic asks: can a fully Linux-native stack — no SAI, no FPM, no vendor NOS — route at line rate on commodity switching silicon?
- **What**: BIRD 3.1.7 running on the Novarq Tactical 1000 (LAN969x/Sparx5 silicon, Debian arm64), establishing dual-stack eBGP sessions and installing routes through the standard kernel path. Results: four eBGP sessions up, IPv4 hardware offload at 9.41 Gbit/s of TCP and IPv6 at 9.28 Gbit/s with the switch CPU never seeing transit packets; route changes propagate from peer withdrawal to the Linux FIB in 0.40–0.45 s; a 256-route add/withdraw batch works cleanly (a functional test, not a capacity test).
- **How**: BIRD exports routes via its kernel protocol over rtnetlink; FIB notifiers drive the LAN969x driver, which programs the ASIC; switchdev carries bridge, VLAN, FDB and multicast state, with neighbour entries supplying next-hop MACs. Explicit BIRD filters keep the kernel table clean; a per-layer observability checklist (birdc, `ip -d route`, `ip -s neigh`, captures at receiver and switch CPU) verifies offload.
- **Where applicable**: Hardware-specific today — the L3 routing driver lives in the Novarq kernel tree, not mainline Sparx5, and two setup steps need care. The architecture and the collaboration gaps (BIRD devs, kernel/switchdev maintainers, open hardware vendors) generalize to the whole open-Linux-switching effort.

### Multi-Layer Routing Domain Protection at Hyperscale: From Route Leak to Automated Enforcement

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/134/TN3ZHZ/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/TN3ZHZ/resources/RIPE_93_-_Multi-Laye_wyACzkg.pdf) · [Recording](https://ripe93.ripe.net/media/videos/daria-shantalova_multi-layer-routing-domain-protection-at-hyperscale-from-route-leak-to-automate_main_20261027-150238.mp4)

Daria Shantalova, Express Backbone Team, Meta

- **Why**: A concrete, high-quality postmortem plus the system built in response — exactly the failure-driven content that transfers, because the preconditions (multiple routing domains, BGP between them, community-based policy) describe most large networks.
- **What**: An internal domain advertised a large volume of prefixes toward Meta's Express Backbone (the DC-to-DC backbone), each carrying a community the ingress route-map legitimately matched. The routes propagated through the iBGP mesh to every site, DC aggregation routers exhausted memory and restarted, and service disruption followed. The core insight: community-based filtering answers "is this tag allowed at this boundary?" but not "is this prefix allowed to carry this tag?" — that gap is where leaks live.
- **How**: Three independent layers at every domain boundary: (1) ID Communities — a registered tagging scheme where each prefix carries exactly one identity community defining origination and propagation scope, with missing/wrong/multiple tags as violations; (2) a Route Registry — an internal IRR-equivalent permit list per boundary, auto-generated into inbound prefix filters with a freshness SLA; (3) control-plane health monitoring that continuously validates the RIB against intent. Deployment exposed pervasive violations that were remediated within months, and automated enforcement now prevents recurrence.
- **Where applicable**: Built at Meta scale (dozens of data centers), but the three-layer pattern is deliberately presented as applicable without their stack — any operator running multi-domain BGP with community-scoped policy can copy the architecture.

### Expanding Routing Visibility at IXPs with BMP

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/130/LLUPSG/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/LLUPSG/resources/RIPE_2026_c23luM9.pdf) · [Recording](https://ripe93.ripe.net/media/videos/thomas-holterbach_expanding-routing-visibility-at-ixps-with-bmp_main_20261027-085952.mp4)

Thomas Holterbach, bgproutes.io

- **Why**: Route-server looking glasses only show what survived policy; BMP exposes the whole routing pipeline at an IXP — pre-policy, filtered, and non-best routes plus peer/session state — which changes what both IXP operators and participants can detect (hijacks, leaks, misbehaving peers).
- **What**: A proposal and practical demonstration (the bgproutes.io IXP Explorer) for BMP-based monitoring at IXPs, plus an honest treatment of the open problems: processing and storing large BMP volumes at big IXPs, efficient data serving, and consistent access across collection platforms and storage architectures, ending with a roadmap for community adoption.
- **How**: Both BIRD and FRRouting can export BMP when deployed as route servers; BMP is positioned as complementary to existing approaches (direct route-server queries à la Alice-LG, and dedicated add-path collection sessions). The talk frames IXP monitoring as serving two audiences: IXP operators securing the fabric, and participants making peering and troubleshooting decisions.
- **Where applicable**: Any IXP operator; of the 1,226 IXPs listed on PeeringDB most are small/medium and can adopt this sooner — the scaling challenges are specific to the largest exchanges.

### ASPA: the new protocol for improving BGP routing security

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/117/Y87HT8/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/Y87HT8/resources/RIPE93-ASPA-tutorial_1fPdvkk.pdf) · [Recording](https://ripe93.ripe.net/media/videos/ondrej-caletka_aspa-the-new-protocol-for-improving-bgp-routing-security_main_20261026-090008.mp4)

Ondřej Caletka, RIPE NCC

- **Why**: ASPA (Autonomous System Provider Authorization) is the 2026 RPKI deployment milestone — the first broadly deployed step beyond origin validation toward path verification — and this tutorial is the operator's manual for both signing and validating sides.
- **What**: A deep dive covering ASPA principles, creating ASPA objects for your ASNs, configuring validation in routers, and troubleshooting validation failures. An ASPA object lists the set of provider ASNs for a customer AS, signed via the RPKI chain of trust; validating operators can drop routes arriving via unauthorized providers. It complements ROV (which stops misorigination but not path spoofing or route-leak types 1–4), supports partial deployment, and is address-family agnostic.
- **How**: Signing works through the standard RPKI models (hosted, delegated, hybrid) and the RIPE NCC portal; the tutorial includes practical guidance on what belongs in the object — transit providers, backup providers, DDoS-scrubbing providers, non-transparent IXP route servers — and what does not (customers, lateral peers, unless they can act as providers under some circumstances).
- **Where applicable**: Every ASN holder and every operator doing inbound filtering; value grows with adoption, so early signers shape the ecosystem.

### When Routing Evidence Conflicts: Measuring IRR and RPKI for BGP Filtering

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/132/JBBTFH/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe-93/submissions/JBBTFH/resources/RIPE93_irr_rpki_filt_1LcO0UB.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe-93/submissions/JBBTFH/resources/RIPE93_irr_rpki_fil_gDZKfQW.pptx) · [Recording](https://ripe93.ripe.net/media/videos/antonis-chariton_when-routing-evidence-conflicts-measuring-irr-and-rpki-for-bgp-filtering_main_20261027-112800.mp4)

Antonis Chariton and Usama Ejaz, Cisco ThousandEyes

- **Why**: Operators treat IRR route objects and RPKI ROAs as corroborating evidence for the same announcement; this measurement shows they disagree in specific, quantified ways that directly affect filter correctness.
- **What**: A time-aligned comparison of BGP, IRR and RPKI for 8–14 August 2026 (57 RIS/RouteViews collectors, 19 IRR sources, 18 relying-party views). Findings: 64.6–65.1% of daily public BGP prefix-origin pairs had an exact IRR match, and 79.9% of those matches existed in only one IRR source; 786 exact IRR matches stayed RPKI Invalid all week (371 maxLength, 415 wrong-origin), concentrated in a handful of origins — five ASNs account for 43.4% of maxLength and 50.4% of wrong-origin cases, and 99.5% of the persistent conflicts were registered in a single IRR source; 22.2% of exact-match pairs remained RPKI NotFound. A PeeringDB AS-SET replay retained 99.27% of exact matches.
- **How**: Daily snapshots at a fixed time, recursive AS-SET expansion through declared IRR sources, consensus classification across relying-party views, and a separate replay of PeeringDB-declared AS-SETs.
- **Where applicable**: Any edge-filtering pipeline using IRR and/or RPKI. The operational guidance is the point: an exact IRR match does not imply RPKI Valid, and incomplete AS-SET evidence is not grounds to exclude an origin ASN from a filter.

### Measuring Propagation Time of RPKI Validity Changes on the Dataplane

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/132/M9LAQ9/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/M9LAQ9/resources/RIPE93-Slides_eqnTvwv.pdf) · [Recording](https://ripe93.ripe.net/media/videos/alexander-mannel_measuring-propagation-time-of-rpki-validity-changes-on-the-dataplane_main_20261027-110203.mp4)

Alexander Männel, TU Dresden

- **Why**: When you change a ROA — including an emergency change during a hijack — how long until actual dataplane reachability changes? This is the first Internet-wide answer, and the numbers should inform every operator's incident playbook.
- **What**: RPKI propagation is at least an order of magnitude slower than plain BGP: invalid-to-valid transitions take 9–12 minutes and valid-to-invalid transitions 30–42 minutes to take effect at 50% of vantage points. The public measurement platform ReRPKI lets operators observe how RIPE Atlas probes connected through their AS experience reachability during ROA changes.
- **How**: The method uses the CDN origin of the RIPE RRDP repository plus an optimized validator to detect ROA changes earlier than the ecosystem (at least 57 seconds faster, median 5:07 minutes before the fastest public validator, n=24,886), then triggers traceroutes from 300+ CAIDA Ark vantage points every three minutes for an hour, covering all RIPE prefixes in the RPKI hosted model.
- **Where applicable**: Internet-wide and vendor-neutral; the latencies reflect current relying-party fetch intervals and validator configurations, so they bound what any ROV deployment can expect today.

### The End of Prefix Filtering

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/142/G9TM8M/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/G9TM8M/resources/RIPE93_-_The_End_of__B5eWm0u.pdf) · [Recording](https://ripe93.ripe.net/media/videos/james-bensley_the-end-of-prefix-filtering_main_20261028-092052.mp4)

James Bensley, Inter.link

- **Why**: A deliberately provocative operator thesis with data behind it: IRR-derived prefix filtering may now cost more to generate, deploy and maintain than the security it adds, and ROA coverage has grown enough to switch edge filtering to RPKI alone.
- **What**: A three-way comparison of DFZ, IRR and ROA datasets (single-day snapshots) showing DFZ data tracking ROA data more closely than IRR, IRR containing substantial redundancy, and redundant ROA data beginning to accumulate; decision-flow analysis of what each filtering combination actually rejects; and the observation that tier-1 transit feeds are already accepted as full tables without prefix or AS-path filters.
- **How**: Snapshot-based dataset comparison plus stepwise filter decision trees (origin in AS path → ROA valid/unknown → IRR presence → reject/accept), ending with the "are we there yet?" assessment.
- **Where applicable**: Explicitly scoped to the standard edge case (excludes RTBH, private ASNs, Flowspec). Read it against *When Routing Evidence Conflicts* in the same program — that talk quantifies exactly the IRR/RPKI disagreements that make a wholesale cutover non-trivial. Operator judgment required; the debate itself is the value.

### Early Attestation is Very Harmful. Why is it Required?

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/137/GJXMGP/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/GJXMGP/resources/20261027_RIPE_93_Sec_e4tTL66.pdf) · [Recording](https://ripe93.ripe.net/media/videos/muhammad-usama-sardar_early-attestation-is-very-harmful-why-is-it-required_side_20261027-162413.mp4)

Muhammad Usama Sardar, GA4GH

- **Why**: Attested TLS — binding remote attestation into the TLS handshake — is being standardized and deployed for confidential computing and workload identity; this talk shows the early-attestation variant carries critical-severity CVEs, directly relevant to workload/TEE identity design.
- **What**: Formal verification (ProVerif) surfaced a family of critical and high CVEs in early (intra-handshake) attestation: relay attacks from missing connection binding (CVE-2026-33697, CVSS 7.5), diversion attacks from missing hardware/machine-ID binding, and the EarlyAttestationBleed/EAT series at CVSS 9.1–9.6 — in deployments handling the health data of more than 40 million Germans. Still-vulnerable implementations include Cocos AI ≤ v0.8.2, Privasys rustls/Go, and code following the withdrawn early-attestation draft.
- **How**: Symbolic security analysis of the attested-TLS handshake, root-caused into two failures — no binding to the connection and no binding to the hardware — plus an architectural argument: early attestation leaks hardware-level information, can only express boot-time claims, adds handshake latency and failure modes, and every use case works with standard post-handshake attestation instead.
- **Where applicable**: Anyone building or procuring attested TLS, TEE-based workload verification, or confidential-computing pipelines; the talk feeds directly into IETF standardization (SEAT-adjacent) and explicitly invites operator feedback.

### Let's talk about some topics of interest at the IETF

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/127/QKQXWT/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/QKQXWT/resources/RIPE_93_IETF_v6_EBjRjjA.pdf) · [Recording](https://ripe93.ripe.net/media/videos/suresh-krishnan_lets-talk-about-some-topics-of-interest-at-the-ietf_main_20261026-180151.mp4)

Suresh Krishnan, Internet Architecture Board

- **Why**: This IAB/IESG BoF is the most direct hit on the agentic-identity agenda at the whole meeting: workload identity standards (WIMSE) being applied to AI agents, OAuth working-group work on AI-agent authorization, and two new AI-focused WGs.
- **What**: An interactive session on IETF topics relevant to operators: AI (AGENTPROTO for AI-agent application interoperability; DAWN for AI resource discovery over mDNS), identity/authentication/authorization/audit (WIMSE guidelines for AI-agent authN/authZ and gap analysis — workload identity methods designed to apply to AI agents; OAuth WG work on AI-agent authorization; a new "audit" BoF on auditing distributed, time-evolving systems), post-quantum cryptography (PQUIP operational guidance, RFC 9958, hybrid work across tls/jose/cose/lamps, Merkle-tree certificates in PLANTS), plus IPv6, DNS, routing and space topics.
- **How**: Presentation-light, feedback-heavy: the explicit goal is to collect operator positions and feed them back into the IETF process.
- **Where applicable**: Anyone whose roadmap depends on workload identity, OAuth/OIDC extension points, or PQC migration timelines for BGP/DNS security.

### Nothing left to take away

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/152/DPPNML/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe-93/submissions/DPPNML/resources/nothing_left_to_take_G7rob7m.pdf) · [Slides (Keynote)](https://pretalx.ripe.net/media/ripe-93/submissions/DPPNML/resources/nothing_left_to_take_rYGqKaH.key) · [Recording](https://ripe93.ripe.net/media/videos/remco-van-mook_nothing-left-to-take-away_main_20261029-100153.mp4)

Remco van Mook

- **Why**: draft-ietf-intarea-ipv6-resolved-gateway removes ARP from access and hosting segments while keeping dual-stack hosts unmodified — a structural simplification aimed squarely at datacenter fabrics, containers, Kubernetes and GPU clusters running out of RFC1918.
- **What**: A mechanism that lets IPv4 service endpoint identifiers survive on an IPv6-only segment: hosts get a sentinel IPv4 gateway (DHCPv4 Option 3, placeholder 192.0.2.11) and resolve its MAC from the IPv6 neighbour cache instead of ARPing; unmodified hosts still ARP for the sentinel and the router answers — both host generations coexist on the same segment, with no DHCPv4 client/server/relay changes.
- **How**: Updated hosts use the RFC 4861 default-router list and RFC 4191 preferences (no ARP at all); gains include active/active gateways without FHRP, inbound ECMP to the last hop, no ARP spoofing, no broadcasts, per-host /32s anywhere in the footprint, and — via RFC 8950 — IPv4 service addresses delivered straight to pods without SNAT/DNAT/conntrack. Running code exists on the host side (v4gwd.py for ifupdown/NetworkManager, a systemd-networkd patch, FreeBSD 13.1+).
- **Where applicable**: Target use cases are explicitly DC fabrics, campuses, DOCSIS MAC domains, FTTH/PON aggregation, containers/Kubernetes, and AI/GPU clusters. Draft stage (-01 will add ND health prerequisites and a MAY-level ARP fallback), so it needs host-side adoption; the design is general.

### InterLAN IX Lighthouse - Yet Another Network Automation Tool

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/142/PCYRUS/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/PCYRUS/resources/InterLAN_Lighthouse__LM4dPhn.pdf) · [Recording](https://ripe93.ripe.net/media/videos/andrei-dinu_interlan-ix-lighthouse-yet-another-network-automation-tool_main_20261028-095036.mp4)

Andrei Dinu, InterLAN IX

- **Why**: A production self-service portal with checked, reversible, recorded changes over a multi-vendor estate (Nokia SR OS + Arista EOS) — a transferable template for anyone automating a physical fabric, including how to keep humans in the loop.
- **What**: Lighthouse (network automation) alongside BirdNest (Rust-based BIRD route servers with IRR/RPKI/looking-glass) and NoSignal (live TV) behind one member portal. Lighthouse automates Nokia L2/L3/EVPN services, ports/LAGs/multihoming, routing and traffic policy, plus Arista access ports/trunks/VLANs/ACLs. One member request fans out to several routers as an atomic multi-device transaction with per-device preview, a rollback timer, a reachability check, and confirm-one-router-at-a-time; when safe recovery can't be proven, a human takes over.
- **How**: gNMI for Nokia config/state/streaming telemetry, eAPI+SNMP for Arista; the database owns intended state so hand-made device changes surface as deviations and are never silently adopted; a digital twin built from production snapshots (same topology, same NETCONF/gNMI writes) rehearses changes; an AI assistant with strictly read-only tools writes reports and migration plans; IPFIX/sFlow lands in ClickHouse for who-exchanges-with-whom analytics and trial attack detection.
- **Where applicable**: Built for an IXP (Nokia core, Arista access), but the pattern — intended-state database, preview/rollback transactions, deviation surfacing, rehearsal twin — generalizes to any multi-vendor DC or campus estate.

### Embracing NETCONF

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/125/AA9HSF/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/AA9HSF/resources/embracing-netconf-v2_jGfVge2.pdf) · [Recording](https://ripe93.ripe.net/media/videos/maria-matejka_embracing-netconf_main_20261026-160213.mp4)

Maria Matejka, BIRD | CZ.NIC

- **Why**: Twenty years after RFC 4741, NETCONF/YANG/RESTCONF are the default network-automation interfaces — and this is a practitioner's fine-print audit of whether the zoo of protocols, formats and schemas can actually be relied on.
- **What**: A critical tour of the ecosystem: NETCONF's datastore and locking semantics, RESTCONF's HTTP mapping and its quirks (it cannot manipulate NETCONF locks, and auto-commits the candidate datastore after every successful edit — silently committing other sources' staged edits), YANG modeling with XML and JSON encodings (RFC 7951), and where canonical vs. alternate representations diverge.
- **How**: Quote-the-spec analysis: each claim is anchored to the exact RFC text, contrasting what the documents promise with what implementations deliver — the "have you read the fine print?" framing from the abstract.
- **Where applicable**: Anyone consuming NETCONF/RESTCONF/YANG in automation or tooling; the practical constraint is vendor support variance, which is precisely what the talk surfaces.

### Detecting and Characterizing Exposed BGP Routers​

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/130/RGPF9L/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/RGPF9L/resources/Exposed_BGP_routers__z76THOA.pdf) · [Recording](https://ripe93.ripe.net/media/videos/shyam-krishna-khadka_detecting-and-characterizing-exposed-bgp-routers_main_20261027-100325.mp4)

Shyam Krishna Khadka, University of Twente

- **Why**: RFC 7454 told operators to restrict TCP 179 to configured peers twenty years ago; this measurement shows 20,432 routers across 4,194 ASes still accept unsolicited BGP OPENs — a concrete, checkable exposure for any network.
- **What**: An Internet-wide IPv4 scan (February 2026): 6.25M IPs respond on TCP/179, 277k speak BGP, and 141k (51%) complete an OPEN exchange. Using the BGP Identifier (unique per router per ASN per RFC 6286) plus OPEN ASN and interface ASN mapping, these resolve to 20,432 unique routers — 16,124 internal, 1,127 border, 3,181 unclassified — across 4,194 ASes. Around 75% of border routers face one AS; ~90% have fewer than 10 IPs, while 10% of internal routers expose up to 1,208 IPs. A partial vendor view via Shodan's SNMPv3 data identifies 8,871 routers (43.4%), dominated by Juniper (5,448) and Teldat (2,956).
- **How**: ZMap TCP/179 scan → custom BGP speaker sends OPEN → OPEN-response analysis → router/AS association and border-vs-internal classification by ASN visibility.
- **Where applicable**: The finding is Internet-wide and vendor-agnostic; the operator action is trivial to execute — audit your edge ACLs with nmap/zmap from outside — and the talk explicitly invites operators to explain why these ports are open.

## Adjacent

### RS-API - Accept announcments as legit as possible

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/142/9BLCQT/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/9BLCQT/resources/slides-short_oFD7MzQ.pdf) · [Recording](https://ripe93.ripe.net/media/videos/evann-dreumont_rs-api-accept-announcments-as-legit-as-possible_main_20261028-090549.mp4)

Evann Dreumont and Alarig Le Lay, Breizh-IX

- **Why**: Route-server filter generation is a solved-looking problem that isn't: PeeringDB max-pref values are self-reported and unreliable, and an AS-SET can quietly pull in hundreds of thousands of prefixes (one shown bgpq4 expansion: 202,416). This is adoptable open-source tooling that confronts registry data with observed reality.
- **What**: RS-API, a caching proxy around bgpq4, bgp.tools and bgproutes.io that generates route-server configuration: RPKI (ROA + ASPA), OTC checks (RFC 9234), bogon and specificity filters, IRR prefix-lists, and a recomputed max-pref derived from the peer's actual AS cone rather than their PeeringDB claim, with AMS-IX-style scaling applied.
- **How**: JSON API with a 24-hour TTL cache (config generation across 2 route servers × 4 cities would otherwise hammer the upstream APIs); AS-cone sizing via the bgp.tools API with a bgproutes.io looking-glass fallback; deployed in production at Breizh-IX (Rennes, Nantes, Lille, Strasbourg); open source.
- **Where applicable**: Any IXP route server, especially small and medium ones; it depends on third-party APIs (bgp.tools, bgproutes.io) being available and accurate — the talk explicitly asks larger IXPs how they solve the same problem.

### PSA: Removing AS-SET Ambiguity

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/153/AJMFLA/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/AJMFLA/resources/RIPE93_-_PSA_-_Remov_n5yDfQd.pdf) · [Recording](https://ripe93.ripe.net/media/videos/james-bensley_psa-removing-as-set-ambiguity_side_20261029-093300.mp4)

James Bensley, Inter.link

- **Why**: AS-SET names are not globally unique, and the same name can resolve differently per database (AS-APPLE in RIPE: 2 ASNs, 0 prefixes; in RADB: 2 ASNs, 244 prefixes) — producing silently empty or silently wrong prefix filters. The ecosystem has just changed a lot at once, and this rounds it up.
- **What**: A public service announcement consolidating independent fixes: RIR enforcement of hierarchical AS-SET names (RIPE, APNIC and LACNIC done; AFRINIC and ARIN coming); PeeringDB requiring registry-scoped AS-SETs (with auto-suggested scope) and limiting networks to a single AS-SET (of 37,130 networks, 19,942 declare an AS-SET and 304 declared more than one); MANRS considering making both mandatory; and IETF drafts for registry-scoped members (`src-members: RIPE::AS-BAR`) and member exclusion (`excl-members:`, motivated by an AS-SET expanding to 76,337 ASNs and 1.32M prefixes).
- **How**: Concrete database/policy changes already shipped or in flight, each with links to the enforcing organization and draft.
- **Where applicable**: Anyone generating IRR-derived filters today — the action items (rename to hierarchical, scope your AS-SETs in PeeringDB) are immediate.

### Post-Quantum DNSSEC at Cloudflare

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/156/Z8RVVH/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/Z8RVVH/resources/RIPE93_dns-wg_PQ_DNS_25I6IcZ.pdf) · [Recording](https://ripe93.ripe.net/media/videos/joe-abley_post-quantum-dnssec-at-cloudflare_side_20261029-110226.mp4)

Joe Abley, Cloudflare

- **Why**: The first production deployment of a post-quantum DNSSEC algorithm in a large public resolver — a working answer to "how do we even start?" for PQ migration of Internet infrastructure.
- **What**: Cloudflare implemented ML-DSA-44 (algorithm 18, via draft-westerbaan-dnssec-mldsa) in the 1.1.1.1 resolver, fully live for all clients since 10 September 2026, handling 2,420-byte signatures; a public checker (dnstest.dev) tells users what their local resolver does. The wider landscape remains at zero: no PQ algorithms specified for DNSSEC, no registries accepting PQ DS records, root still on RSA/SHA-256 — and the response-size/TCP-fallback problem is the gating issue.
- **How**: Implementation and measurement experience, plus a new problem class: DNSSEC has no downgrade protection, and a failing PQ signature alongside a valid legacy signature is indistinguishable from a quantum attack — motivating draft-jabley-dnsop-local-signing-algorithm-policy for local validation policy. Framed against NIST IR 8547's ~2030 deprecation and 2035 disallowance clock.
- **Where applicable**: DNS operators and anyone planning PQC timelines for signing infrastructure; the multi-signature downgrade problem generalizes to other PQ migrations.

### The State of ECN Adoption in the Internet

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/136/38HZHM/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/38HZHM/resources/ECN-RIPE93-2026_v2_fyEOjnK.pdf) · [Recording](https://ripe93.ripe.net/media/videos/danesh-zeynali_the-state-of-ecn-adoption-in-the-internet_main_20261027-163400.mp4)

Danesh Zeynali, Max Planck Institute for Informatics

- **Why**: L4S and low-latency transport depend on ECN surviving end-to-end; this re-measures adoption a decade after the classic studies and finds a specific, named blocker.
- **What**: A revisiting and extension of the Bauer and Trammell ECN characterization studies: the majority of Internet service infrastructure is now ECN-aware, but a nontrivial fraction of hosts, routers and middleboxes bleach ECN bits — and many hyper-giants bleach along the path, with substantial implications for L4S. IPv6 endpoints and paths show stronger ECN support than IPv4.
- **How**: Active measurements covering endpoint support (handshake negotiation), network support (marking and bleaching on path), and a longitudinal view.
- **Where applicable**: Anyone counting on ECN or L4S — including teams whose lossless/low-latency DC designs assume ECN works beyond the fabric; the hyper-giant bleaching is the deployment blocker to watch.

### Beyond NIS2: Software Supply Chains and the Cyber Resilience Act (CRA)

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/143/AHLDQR/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/AHLDQR/resources/2026-11_RIPE93_-_INE_QUxgndJ.pdf) · [Recording](https://ripe93.ripe.net/media/videos/barry-odonovan_beyond-nis2-software-supply-chains-and-the-cyber-resilience-act-cra_side_20261028-090638.mp4)

Barry O'Donovan, INEX

- **Why**: NIS2 governs how you run your network; the CRA governs the software you run it with — including the open-source stacks most operators depend on. With mandatory vulnerability reporting live since September 2026, this is now procurement-reality, not policy theory.
- **What**: A bridge from NIS2 operator obligations to CRA software requirements: the critical distinction between Commercial OSS Manufacturers (full product liability, CE marking, fines) and Open-Source Software Stewards (non-profit foundations under a light-touch regime, duties from 11 December 2027), with ecosystem examples — INEX and NLnet Labs as stewards vs. enterprise Linux vendors as manufacturers. Also covers what operators can legally expect from upstream maintainers on SBOMs, vulnerability disclosure and patch timelines, and reporting duties (24-hour early warning, 72-hour notification).
- **How**: Walkthrough of the Commission's scope examples and the "intended for commercial activities" test, plus a roadmap for auditing open-source dependencies and consuming standardized security feeds.
- **Where applicable**: EU-market entities, but the checklist is useful for any operator publishing community tools or procuring network software.

### Maybe it is time to consider layer 3 internet exchanges

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/245/MVTX9A/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/MVTX9A/resources/layer_3_ix_presentin_9tu0wAm.pdf) · [Recording](https://ripe93.ripe.net/media/videos/james-rice_maybe-it-is-time-to-consider-layer-3-internet-exchanges_side_20261026-175849.mp4)

James Rice, Jump Networks Ltd

- **Why**: A structured challenge to thirty years of IXP orthodoxy — should exchanges offer routed, point-to-point L3 ports instead of a shared L2 peering LAN with route servers? The whole industry replaced large L2 domains with routed ones everywhere else.
- **What**: The case for L3 exchanges built on three qualities of connectivity: correct forwarding (L2 fabrics have silent forwarding failure modes with confidentiality and availability consequences), shorter physical paths (an L2 participant picks next-hops without knowing which is closer; an L3 fabric does closest-exit routing like a transit provider), and capacity headroom (with a real 9/11 case study where LINX port headroom let the BBC keep broadcasting). Historical reasons for L2 (1990s: expensive CPU routers vs cheap switches) no longer hold since switches and routers both forward L2/L3 in hardware. Followed by a panel including Inter.link, LINX, Cloudflare, Google and Zayo.
- **How**: Argument plus worked example of where a shared peering LAN falls short; the rest was structured audience/panel discussion on whether networks would prefer L3 ports and which IXs would offer them.
- **Where applicable**: IXP operators and anyone buying exchange ports — a design conversation, not a deployment; the remote-peering latency caveat (attracting traffic via distant PoPs) applies to participants more than the fabric model.

### Debugging Stupid Things: If it only was DNS for once...

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/170/JLVACT/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/JLVACT/resources/presentation_AVV6CdU.pdf) · [Recording](https://ripe93.ripe.net/media/videos/tobias-fiebig_debugging-stupid-things-if-it-only-was-dns-for-once_main_20261030-112621.mp4)

Tobias Fiebig, TU Wien

- **Why**: The program's purest "hard-won lessons" talk: weird corner-case bugs, the debugging process used to find them, and the belief systems that got in the way — exactly the kind of content that transfers across environments.
- **What**: A tour of production corner cases, including a PMTUD failure where downloads for users on one transit path crawled because ICMP "need to frag (mtu 1420)" messages were being lost or ignored while other paths were fine; Microsoft treating ED25519 DKIM signatures as a syntax error while RSA validated; FRR treating 'extended-nexthop' as 'unnumbered' and emitting rogue Router Advertisements onto the AMS-IX exchange LAN; and solar-panel power monitoring causing random shutdowns whose reconnect pattern triggered a null-pointer crash in OpenBGPD. No DNS packets were the root cause in any case.
- **How**: Reproduce, then PCAP ("PCAP or didn't happen"), then work outward from what the packets actually say — with each case paired by a lesson about questioning the assumptions ("why one has not yet understood what one told said system").
- **Where applicable**: Universal; the methodology and the humility travel to any network or systems team.

### The Internet's Path MTUs: How Big Can You Go?

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/136/9W9JWP/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/9W9JWP/resources/RIPE93-4_hPMXiyh.pdf) · [Recording](https://ripe93.ripe.net/media/videos/tobias-fiebig_the-internets-path-mtus-how-big-can-you-go_main_20261027-160734.mp4)

Tobias Fiebig, TU Wien, and Vaishnavi Raghavajosyula, Max Planck Institute for Informatics

- **Why**: PMTUD is unreliable, so protocols fall back to conservative sizes; knowing where the real MTU bottlenecks are — and that they're at the edges, not the core — is directly useful for interconnect and MSS-clamp decisions.
- **What**: A measurement of 76,700 paths (access, core, and web-serving) using a PMTUD-independent traceroute-based method: 97 distinct PMTUs, but three dominate — 1500 B (80.5%), 1492 B (11.7%), 1480 B (1.5%). 99% of IPv4 paths support at least 1420 B; IPv6 paths commonly operate at 1280 B. Sub-1500 breaks concentrate near network edges (1492 B maps cleanly to PPPoE overhead in fiber/DSL ASes) while core paths are rarely constrained. PMTU is asymmetric: reverse-direction PMTUs are larger in >92% of sub-1500 pairs (~64% of those are 1500 B). 18.5% of paths show PMTU-vs-MSS-inferred mismatches.
- **How**: RIPE Atlas anchors and probes, traceroute-based PMTU discovery independent of PMTUD (iterative search over a coarse size list), cross-checked against ICMP PTB hints and TCP-MSS, with heuristic attribution of break locations using AS, TTL and external network documentation.
- **Where applicable**: WAN/DC-interconnect MTU planning and any jumbo-vs-1500 end-to-end decision; the edge-vs-core finding means the core can safely run large MTUs while edge paths need clamping.

## Wildcard

### Networks as Sensors: Passive Measurement as a Lens on Society, A case study on two European elections

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/134/DLCKAN/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/DLCKAN/resources/Elections__Apps____Z7QvTZO.pdf) · [Recording](https://ripe93.ripe.net/media/videos/orlando-eduardo-martinez-durive_networks-as-sensors-passive-measurement-as-a-lens-on-society-a-case-study-on-t_main_20261027-143022.mp4)

Orlando Eduardo Martínez-Durive, IMDEA Networks Institute & Net AI

- **Why**: Not a networking-ops talk, but a genuinely surprising result about what the passive measurements operators already run for engineering can reveal: per-antenna app demand from a major French mobile operator (market share ~31%, ~22M subscribers) predicts political alignment — and the study is an open invitation to operators to build this instrumentation together.
- **What**: Using aggregated, GDPR-compliant mobile metadata (per-antenna demand for 22–27 apps, residential evening window) across the 2019 and 2024 European Parliament elections, digital consumption carries an independent signal about vote share that for several parties matches or exceeds traditional socioeconomic indicators; combining both increases explanatory power by up to 28.23%, consistently across both elections. The illustrative case: two demographically near-identical towns 10 km apart with far-right vote shares of 31% vs 20% differ mainly in app-consumption profiles (Facebook +5% vs −26%; online news −21% vs +43%).
- **How**: Revealed Comparative Advantage normalization to make per-app volumes comparable across antennas, alignment of antenna-level demand with commune-level socioeconomic and vote data, and regression modeling of vote shares.
- **Where applicable**: Research collaboration with MNO/ISP/IXP vantage points; the broader argument is that operator passive measurement could become a platform-independent instrument for observing society — with all the privacy and governance questions that implies.

### Using IPv6 and DNS to implement a new addressing architecture for the Internet

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/152/SP3LJE/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/SP3LJE/resources/20261016_ilnp_ripe93_zH6L8wG.pdf) · [Recording](https://ripe93.ripe.net/media/videos/saleem-bhatti_using-ipv6-and-dns-to-implement-a-new-addressing-architecture-for-the-internet_main_20261029-090425.mp4)

Saleem Bhatti, University of St Andrews, UK

- **Why**: A follow-up born from RIPE 92 attendee demand: the identifier/locator split is a decades-old idea whose time may be coming back, and this is a working IPv6-native implementation rather than a position paper.
- **What**: ILNP (Identifier Locator Network Protocol) — the "Why/What/How" of splitting the IP address's semantic overload into an Identifier (node identity, DNS-published) and a Locator (network location), reducing global routing state, enabling multihoming, multipath and mobility without extra machinery, and improving privacy. Unlike LISP, HIP and SHIM6, it does not overload the IP address semantics. It runs across today's IPv6 infrastructure and is backwards-compatible with IPv6 applications.
- **How**: Locators and identifiers as new addressing data types bound dynamically to protocol-stack objects, with DNS supplying the mapping; a FreeBSD implementation is ongoing (with ICANN Grant Program support) and the talk covers what works across today's Internet — protocol, routing, API and naming compatibility.
- **Where applicable**: Research and standards exploration, not deployment — but relevant to anyone designing the next iteration of DC addressing, mobility, or identity-adjacent network architecture.

### TTL Jumps: Unexpected TTL Rewrites Impacting Inferences from Traceroutes

**Links:** [Abstract](https://ripe93.ripe.net/programme/meeting-plan/sessions/125/9388Q3/) · [Slides](https://pretalx.ripe.net/media/ripe-93/submissions/9388Q3/resources/presentation_8QIVkpM.pdf) · [Recording](https://ripe93.ripe.net/media/videos/tobias-fiebig_ttl-jumps-unexpected-ttl-rewrites-impacting-inferences-from-traceroutes_main_20261026-171559.mp4)

Tobias Fiebig, TU Wien, and Johannes Zirngibl, Max Planck Institute for Informatics

- **Why**: A systematic blind spot in the field's most-used measurement tool: some devices rewrite TTL (often to 255), hiding the rest of the path and corrupting topology inference — and the affected paths include a large fraction of one major Tier-1's IPv6 network.
- **What**: At least 47 ASes contain path-impairing devices that rewrite TTL. The flagship example: more than 90% of outgoing IPv6 paths from CAIDA Ark nodes have been affected at AT&T since 2023. Measurement towards a single node found 365 probes (138 IPv4, 236 IPv6) seeing rewrites, with 63 ASes implicated on-path; extending to all IPv4 RIPE Atlas traces, 1.8M traces end in ICMP errors, 86.3k contain a TTL > 1, and 23.1k are genuine rewrites (others are liveness probes using TTL 255 after five unresponsive hops).
- **How**: Controlled experiments plus public RIPE Atlas and CAIDA Ark data; the authors distinguish true rewrites from liveness-check artifacts and trace where along the path the rewriting happens.
- **Where applicable**: Anyone building topology inference, AS-link datasets, or traceroute-based triage tooling — the spurious-router/AS-link failure mode directly affects measurement products the PM may depend on.

## Themes

- **RPKI is leveling up from origin validation to path verification.** ASPA goes live in 2026, and the program supplies an operator's checklist around it: how to sign and validate (ASPA tutorial), how slow ROA changes really propagate (9–42 minutes to half the vantage points), how often IRR and RPKI evidence conflicts (786 week-long Invalids hiding inside exact IRR matches), and whether IRR prefix filtering can finally be retired (Bensley's thesis vs. the conflict measurements that complicate it).
- **The open, Linux-native data plane is doing production work.** BIRD routing at 9.4 Gbit/s through mainline-Linux switchdev on merchant silicon, coherent ZR optics as ordinary router pluggables, gNMI-driven multi-vendor automation with rollback and digital twins — the whitebox/open-source stack is no longer a demo.
- **The strongest content is failure-driven.** Meta's route-leak postmortem turned into a three-layer enforcement architecture; Breizh-IX and InterLAN built tooling explicitly around reversibility and audit; Fiebig's debugging stories (and his MTU and TTL measurement papers) mine corner cases for transferable lessons.
- **Agentic AI has reached the identity and standards agenda.** WIMSE workload identity applied to AI agents, OAuth work on agent authorization, AGENTPROTO, and AI-assistant design constrained to read-only tools — the same cycle also shows AI compressing CVE intake (50x at the Erlang CNA) and forcing a trust-ladder discussion for network operations.
- **The Internet's measurement assumptions are being audited.** TTL rewrites corrupting traceroute, PMTU reality vs. MSS inference (18.5% mismatch), ECN bleaching by hyper-giants, mislocated Atlas probes — the community's own instruments have quantified systematic blind spots this cycle.
- **EU regulation is now an engineering input.** CRA reporting duties active since September 2026, steward-vs-manufacturer obligations for open source from December 2027, and the Digital Networks Act debate reaching into interconnection — all with concrete operator checklists attached.
