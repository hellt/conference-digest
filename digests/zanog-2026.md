<!--
conference: ZANOG@iWeek 2026
type: operator
source_url: https://www.iweek.org.za/agenda
generated: 2026-11-04
registry_key: zanog-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ZANOG@iWeek 2026 — Operator Digest

A compact regional operator program (South Africa / AFRINIC region). Much of the agenda is policy, licensing, and ISP business-model content, which has been filtered out. What remains is a solid routing-security thread, a rare hands-on trust-infrastructure talk, two optical/transport sessions, and adoptable open tooling. All session-page fetches returned only the program abstracts, so most write-ups below are abstract-grounded; the two sessions with no abstract at all are flagged explicitly.

## Core

### Securing Internet Routing - The Puzzle Pieces

**Links:** [Abstract](https://www.iweek.org.za/sessions/securing-internet-routing-puzzle-pieces)

Tashi Phuntsho

- **Why**: Route leaks and hijacks are the systemic risk of the interdomain routing system, and this is the program's main survey of the defense stack — squarely in the intersection of network security and BGP internals. Worth the PM's time as a structured view of how the pieces (origin validation, path validation, filtering) do and don't compose.
- **What**: A review of the full routing-security toolkit — RPKI, Route Origin Authorisations (ROAs), BGPsec, IRR-based filtering, and emerging proposals — examining how the pieces fit together, where each excels, and the practical and organisational challenges blocking universal adoption (from abstract only).
- **How**: Mechanism-by-mechanism comparison: cryptographic origin validation via RPKI/ROAs against misorigination, IRR route objects for prefix filtering at AS boundaries, BGPsec for AS-path integrity, and newer proposals for leak detection — against a frank accounting of why adoption remains partial despite mature tooling.
- **Where applicable**: Broadly applicable to any network announcing or accepting BGP routes; vendor-neutral and global in scope despite the regional venue. A 30-minute slot, so expect survey depth rather than new results. Pairs naturally with the ASPA session immediately before it.

### ASPA

Massimiliano Stucchi

- **Why**: ASPA (Autonomous System Provider Authorization) is the newest piece of the RPKI puzzle and targets exactly the gap left by ROAs and BGPsec: route *leaks* (invalid AS paths) rather than misorigination. If the PM's organisation runs BGP with upstreams, this is the next deployment decision after ROV.
- **What**: No abstract is provided in the program or on the session page — content cannot be confirmed. Judging from title, speaker, and the adjacent routing-security session, expect an introduction to ASPA: what the objects are, what attacks they address, and the current state of implementation and adoption. Treat this write-up's mechanism description as background, not as confirmed talk content.
- **How**: (Mechanism background.) An ASPA is an RPKI-signed object in which a customer AS lists its authorized transit providers. Relying parties use these provider sets to verify AS-path plausibility — a route announced to an unauthorized upstream is flagged as a leak — without requiring the full cryptographic path signing of BGPsec, so it is deployable incrementally.
- **Where applicable**: Any AS with upstream providers; verification value grows with ecosystem adoption (RPKI relying parties, IXP route servers). Caveat: with no abstract, the talk's actual depth and specifics are unknown — check the recording if it matters.

### Certificate Transparency: Running Static CT Logs

**Links:** [Abstract](https://www.iweek.org.za/sessions/certificate-transparency-running-static-ct-logs)

Pim van Pelt - IPng Networks

- **Why**: CT is the audit layer that makes misissued TLS certificates detectable — core trust/identity infrastructure, and this is a rare *operational* talk about running it. The PM gets both an architecture update (the new Static-CT log design) and a production postmortem-style account from a small operator doing ecosystem-critical work.
- **What**: The hands-on experience of IPng Networks operating four production CT logs (Rennet, Lipase, Gouda, Halloumi) using Sunlight and TesseraCT — two open-source implementations of the Static CT protocol — covering technical setup, operational lessons learned, and the role of community-run logs in Internet security (from abstract only).
- **How**: Static-CT logs replace the classic RFC 6962 continuously-updating Merkle log with a pre-populated, shardable, statically-servable structure; the talk walks deploying the two open-source implementations and the ongoing operational burden of keeping production logs healthy.
- **Where applicable**: Broadly applicable to anyone operating or auditing certificate-trust infrastructure; both implementations are open source, and the story proves a small community operator can run production-grade trust infrastructure — not a hyperscaler-only or org-specific result.

### Threat Landscape in Southern Africa from a Shadowserver

**Links:** [Abstract](https://www.iweek.org.za/sessions/threat-landscape-southern-africa-shadowserver)

Andy Chadwick - Shadowserver Foundation | Director for Africa

- **Why**: Free, immediately adoptable threat intelligence — the highest "tooling others can adopt" value in the security track, with a regional Southern Africa lens the PM won't get from global feeds.
- **What**: An introduction to what the Shadowserver Foundation does and why its cyber threat intelligence benefits network operators and all network owners, at no cost (from abstract only). Expect an overview session rather than deep technique — the digest value is knowing the resource and the regional picture, not new methods.
- **How**: (Mechanism background.) Shadowserver aggregates internet-wide scanning and sinkhole/honeypot telemetry into free per-network reports — exposed vulnerable services, malware callbacks, etc. — that any network owner can request and act on.
- **Where applicable**: Any network, any size, no product purchase (non-profit). The service is global even though this talk's framing is Southern Africa.

### Submarine Overland Cable Technology

**Links:** [Abstract](https://www.iweek.org.za/sessions/submarine-overland-cable-technology)

Nic Breytenbach - Seacom (Senior Transmission Architect), Afrim Beka - Nokia | Director of Subsea Networks Solutions

- **Why**: Long-haul optical transport is squarely in the PM's physical-networking core (WAN interconnect, optics). The premise — carrying subsea cable engineering onto terrestrial routes — speaks to two live problems: extending resilient capacity into remote and climate-challenged regions, and meeting AI/ML-driven traffic growth.
- **What**: How subsea transmission techniques — spanning thousands of kilometres without regeneration and long distances without amplification — can be applied as powerful solutions for extending resilient, high-performance connectivity into terrestrial networks (from abstract only).
- **How**: Mechanism detail is thin in the abstract; expect coherent long-reach optics and cable-system design that minimises regeneration/amplification sites, presented as a new approach for terrestrial builds serving both basic connectivity and AI/ML demand.
- **Where applicable**: Long-haul subsea and terrestrial transport builds; most relevant where routes are long and terrain/climate makes frequent regeneration sites costly — an Africa-flavoured problem, but the engineering transfers to any long-haul WAN build. Vendor-anchored session (Nokia subsea solutions), jointly presented with Seacom's transmission architect — expect some product positioning around the technique.

## Adjacent

### gNMIc — On Your Marks, GET / SET / Subscribe / Collect

**Links:** [Abstract](https://www.iweek.org.za/sessions/gnmic-your-marks-get-set-subscribe-collect)

Nardus le Roux - Nokia | IP Consulting Systems Engineer

- **Why**: The SNMP-polling-to-streaming-telemetry shift is the network-ops equivalent of a transition the cloud-native world already made; this session covers a concrete, open-source tool an operator can deploy this quarter.
- **What**: An introduction to gNMIc — a scalable gNMI collector with full protocol support (GET / SET / Subscribe / Collect) — and how it delivers continuous visibility into network state, moving beyond SNMP-based monitoring toward a data-rich operational model (from abstract only).
- **How**: Devices expose state via gNMI Subscribe RPCs; gNMIc collects, aggregates, and feeds the stream into downstream operational systems, replacing periodic polling with event-driven telemetry.
- **Where applicable**: Broadly applicable to any environment with gNMI-capable devices (most modern router/switch OSes) — multi-vendor and not org-specific. The speaker is Nokia consulting staff, but gNMIc is a community open-source project, so this reads as tool adoption rather than a product pitch.

### IPv6 - Measuring Uptake

**Links:** [Abstract](https://www.iweek.org.za/sessions/ipv6-measuring-uptake)

Jaco Kroon

- **Why**: The PM already runs IPv6; the value here is measurement methodology and an honest data read on where South Africa and the continent actually stand — useful input for regional capacity/feature planning, and part of this program's most persistent theme (an entire track is named "Please Just Deploy IPv6").
- **What**: Why continued IPv6 migration matters, the methodologies available for tracking adoption across networks and regions, and what the data reveals about IPv6 uptake in South Africa and the broader African continent (from abstract only).
- **How**: Survey of adoption-measurement approaches — content-side user statistics, routing-table/BGP visibility, per-network enablement metrics — plus a regional read-out; the abstract does not specify which methods are used.
- **Where applicable**: Regional focus (South Africa/Africa), but the methodology generalises to any operator or product with a regional footprint; worth skimming for the measurement framework more than the conclusion.

### From Light to Leverage

**Links:** [Abstract](https://www.iweek.org.za/sessions/light-leverage) · [Recording](https://www.youtube.com/watch?v=eppA1hx_ec4)

Byren Meinjes, Brett van Rooyen - NEC XON | Pre-Sales Consultant

- **Why**: For a PM in optical/WAN networking, this is less about new physics and more about packaging: how a provider turns WDM from a bespoke engineering discipline into a productised 100G/400G enterprise service. The product-model framing is directly relevant to product strategy even if the optics is familiar.
- **What**: The Managed Optical Fibre Network (MOFN) model — a WDM-based service framework that lets operators productise optical networking, extend fibre asset life, and deliver high-capacity connectivity to enterprise customers who lack in-house optical expertise, illustrated with real-world use cases and deployment models (from abstract only).
- **How**: WDM layered as a managed-service framework over fibre already in the ground: the provider absorbs the optical transmission engineering, and enterprises consume native 100G/400G connectivity for cloud and AI platforms without bespoke design per circuit.
- **Where applicable**: Aimed at service providers selling high-capacity connectivity to enterprises — the demand signal (enterprises moving past 1G/10G, AI/cloud workloads) is real and broadly applicable, but MOFN itself is a vendor's service model (NEC XON pre-sales presenting), so treat the framework partly as a services pitch.

## Wildcard

### A Guide to Open PON Environment

**Links:** [Abstract](https://www.iweek.org.za/sessions/guide-open-pon-environment)

Radosław Ziemba, Piotr Golubski

- **Why**: Access-network PON is outside the PM's DC/cloud core, but this is a genuinely interesting anti-lock-in technique: an ONT that adapts itself to whichever OLT it faces. Interoperability-vs-vendor-control fights are universal across networking domains, and the access network is currently the most live one.
- **What**: How operators escape OLT-vendor lock-in using multi-vendor HALNy Networks terminals with an "Adaptive OMCI Stack" — plug-and-play ONTs that automatically discover and adapt to a range of OLTs (Huawei, ZTE, Nokia) without firmware changes — plus cloud management via OpenOLT.com and Smart WiFi dashboards, with claimed benefits of fewer truck rolls and lower OPEX (from abstract only).
- **How**: The ONT detects the OLT's management dialect and adapts its OMCI behaviour — inverting the usual model where the OLT vendor whitelists terminals — with remote troubleshooting and optimisation via cloud dashboards.
- **Where applicable**: GPON/XGS-PON access operators. Caveat: the Adaptive OMCI Stack is a specific vendor's (HALNy) feature and the session is effectively vendor-flavoured, so apply pitch-grade skepticism to the interoperability claims; the open-interoperable-access-hardware direction is the signal worth taking away.

### DNS Resolution from Operators in South Africa

**Links:** [Abstract](https://www.iweek.org.za/sessions/dns-resolution-operators-south-africa) · [Recording](https://www.youtube.com/watch?v=e-2KGZf4kik)

Yazid Akanho

- **Why**: Included as a flagged gamble. The only content signal is the track title — "Thirty Years, A Few DNS Queries and Way Too Many Metrics" — which suggests a metrics-heavy, operator-perspective retrospective on DNS resolution. Measurement practice from a regional operator community is the kind of thing worth a skim even when it isn't on the core beat.
- **What**: Unknown — no abstract is provided in the program or on the session page. Based on title and track alone, expect an operator-perspective, data/metrics-driven look at DNS resolution in South Africa rather than a technique talk.
- **How**: Unknown; nothing in the program or session page describes the approach.
- **Where applicable**: South African operator context. Given the missing abstract, this pick stands or falls on the delivered content — check the recording before investing time.

## Themes

- **Routing security has moved from "deploy RPKI" to "assemble the full toolkit."** Two dedicated sessions (Puzzle Pieces, ASPA) treat ROAs as baseline and focus on path/leak verification and the organisational friction that now blocks adoption — the bottleneck is deployment practice, not missing technology.
- **Small operators are running core trust infrastructure.** A one-of-a-kind talk on community-run Certificate Transparency logs (open-source Sunlight/TesseraCT) plus free non-profit CTI from Shadowserver — a pattern of ecosystem-critical trust roles being filled by community and non-profit actors, matching the "Trust Nobody" track title.
- **IPv6 as a measured obligation, not an exhortation.** An entire track named "Please Just Deploy IPv6," a measurement/methodology session on SA and continental uptake, and a 2030 adoption pathway in the keynote — the regional community is moving to data-driven accountability for adoption.
- **Optical capacity is being monetised under AI/cloud demand pressure.** Subsea techniques going overland for long unregenerated spans, and WDM productised as managed 100G/400G enterprise services (MOFN) — both about extracting more value from fibre already in the ground, driven by AI/ML and cloud traffic.
- **Polling to streaming telemetry.** gNMIc presented as the concrete next step past SNMP — open tooling, not vendor platform lock-in — mirroring the observability shift already standard in cloud-native environments.
- **Interoperability as an operator strategy.** Multi-vendor ONTs with adaptive OMCI, open-source CT log implementations, open telemetry protocols — across access, trust, and monitoring layers, this program keeps returning to anti-lock-in via open implementations.
