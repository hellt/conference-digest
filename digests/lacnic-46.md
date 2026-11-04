<!--
conference: LACNIC 46
type: operator
source_url: https://lacnic46.lacnic.net/
generated: 2026-11-02
registry_key: lacnic-46
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# LACNIC 46

## Core

### BGP in 2026: Threats, Incidents, and Solutions

**Links:** [Slides (PPTX)](https://apievt.lacnic.net/wp-content/uploads/2026/09/bgp-en-2026-amenazas-incidentes-y-soluciones-v1-erika-vega-valenzuela-alvaro-retana-guillermo-cicileo.pptx) · [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/09/bgp-en-2026-amenazas-incidentes-y-soluciones-v1-erika-vega-valenzuela-alvaro-retana-guillermo-cicileo.pdf) · [Recording](https://youtu.be/-rJxv367cE8)

Erika Vega Valenzuela, Álvaro Retana, Guillermo Cicileo

- **Why**: The best single map of the current BGP threat and mitigation landscape, grounded in regional incident data rather than vendor framing. Directly in the PM's routing-security and BGP-internals lane.
- **What**: A structured tutorial mapping each threat class to its mitigations — origin hijack → ROA/ROV; AS_PATH manipulation → ASPA (with BGPsec still undeployed); route leaks → filters, BGP Roles/OTC, ASPA; session abuse → GTSM, TCP-AO, max-prefix; volumetric DDoS → RTBH, BLACKHOLE community, Flowspec — plus real incident data for LAC and a monthly Argentina table for Jan–Oct 2026 (route misoriginations ranging 0–6 per month, bogon announcements 2–8, route leaks 0).
- **How**: Threat/example/mitigation blocks sourced from RFC 4272, RFC 7454, SIDROPS, GROW, and MANRS; concrete config patterns for bogon prefix-lists and AS-path ACLs; a discussion of why static bogon lists go stale (today's bogon is tomorrow's IANA allocation); IRR vs RPKI as the two external sources for validating received announcements.
- **Where applicable**: Broadly applicable to any BGP operator; the incident tables are LAC/Argentina-specific public-monitoring data. Ends with a practical adoption roadmap from information hygiene to path protection.

### Beyond RPKI Origin Validation: How to Close the Route Leak Gap with ASPA, Today.

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/mas-alla-de-la-validacion-de-origen-en-rpki-como-cerrar-la-brecha-de-las-route-leaks-con-aspa-hoy-mismo-v2-sthefany-conceicao-duquini.pdf) · [Recording](https://youtu.be/VIcW7bJUmSw)

Sthefany Conceição Duquini (UFMS); slides co-credit Antonio Marcos Moreiras (NIC.br)

- **Why**: ROV is now treated as done; route leaks are the unsolved residue because origin validation says nothing about path. This talk gives the actual deployment state of ASPA and a go/no-go framework, not just theory.
- **What**: How ASPA works (an object lists an AS's authorized transit providers; upstream/downstream algorithms verify adjacent AS_PATH pairs via up-ramp/down-ramp counting, catching valley violations), current adoption (3.66% of routed ASNs globally — 3,249 of 88,714 per Hurricane Electric, Oct 14 2026; 195 LACNIC ASNs publishing, 156 of them in Brazil), tooling (Krill ≥0.14.0, Routinator ≥0.13 with ASPA enabled explicitly or objects silently ignored, FORT 1.7.0 experimental, RTR v2 required), and router support (OpenBGPD and BIRD available now; Juniper in Junos 26.1; Huawei NetEngine 8000; FRR not yet; MikroTik waiting on RFCs; Cisco testing in IOS XR). Includes a real misconfiguration case: AS945's ASPA omitted a genuine provider (AS61138), turning legitimate routes ASPA-Invalid.
- **How**: Publish an ASPA listing only real transit providers — never peers or transparent IXP route servers; use {AS0} for ASes with no providers (e.g., tier-1s); the recommended posture is observe first, enforce later. Validation checks what you published, not what you intended.
- **Where applicable**: Any AS that has finished ROA/ROV. IXPs are the best early testbed (route servers on BIRD/OpenBGPD reach many members at once). In the LAC region, publication is available hosted via MiLACNIC or delegated via Krill. Missing providers in your ASPA is the main operational risk.

### The BGP Analyst's Notebook: 17 Years In

**Links:** [Slides (PPTX)](https://apievt.lacnic.net/wp-content/uploads/2026/07/el-cuaderno-de-un-analista-de-bgp-17-anos-despues-v1-doug-madory.pptx) · [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/07/el-cuaderno-de-un-analista-de-bgp-17-anos-despues-v1-doug-madory.pdf) · [Recording](https://youtu.be/EH-9DQ0_nTE)

Doug Madory (Head of Internet Analysis, Infoblox)

- **Why**: Seventeen years of documented routing incidents from the analyst who published most of them — the right lens for separating durable trends (RPKI uptake) from headline noise, and for threat-modeling and monitoring product direction.
- **What**: A retrospective in two buckets. Geopolitical: Egypt 2011 as the start of the shutdown era; Iran's 2026 shutdowns described as the most impactful in history (BGP routes stayed up while the country went offline via GFW-like filtering, nightly curfews, a national internet, and 2026 allowlisting); the Kherson switchover to Russian transit; the ALBA-1 submarine cable. Attacks: the first documented BGP MITM hijacks (Belarusian ASes, Feb 2013, targets including Visa, Mastercard, and foreign ministries); the coordinated Bitcanal (AS197426) takedown; and the IPv4 leasing / residential-proxy economy — Ukraine's routed footprint shrank 18.5% post-invasion as providers leased IPv4 for revenue, only for it to be abused by proxy networks (per Krebs). Also: China's ROA coverage jumped from 4% to 81% since April 2026, lifting the APNIC region from 55% to 77%.
- **How**: His methodology: reconstruct the hidden per-AS routing-table state over time from merged BGP views rather than individual announcements, and analyze events by scope, duration, and context.
- **Where applicable**: Global internet measurement; not a deployment talk but a high-signal framing of what changed, what hasn't (path validation), and what's coming (ASPA as the next question after ROV).

### RPKI in Action: Updates and Routing Security

**Links:** [Slides (PPTX)](https://apievt.lacnic.net/wp-content/uploads/2026/07/rpki-en-accion-novedades-y-seguridad-de-enrutamiento-v1-gerardo-rada-jorge-cano-carlos-martinez.pptx) · [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/07/rpki-en-accion-novedades-y-seguridad-de-enrutamiento-v1-jorge-cano.pdf) · [Recording](https://youtu.be/YTTa9F-YIRo)

Gerardo Rada, Jorge Cano, Carlos Martínez (LACNIC)

- **Why**: LACNIC's open-source RPKI stack — FORT validator plus the Barry and Rapport test tools — is production tooling anyone can adopt, and the session also covers ASPA and delegated-CA enablement in MiLACNIC.
- **What**: FORT 1.7.0 (July 2026): experimental ASPA support, OpenSSL 4, recommended for production; FORT 2.0 targeted for December 1 with 51 improvements and a more modular architecture. Barry ("the eccentric cousin of FORT") generates valid and invalid RPKI test repositories for validator testing and research. Rapport is an automated test suite for validators — roughly 20 categories and 350 tests (e.g., aspa-profile, rfc6481, rfc6487, router connectivity), extensible to any validator — which replaced the manual smoke-testing that used to accompany every FORT code change. The session also runs interactive route-hijack scenarios and hands-on ASPA configuration, with ASPA and the delegated RPKI model now available through MiLACNIC.
- **How**: The validator flow shown explicitly: fetch RPKI repositories → local cache → cryptographic validation → serve to routers; Barry scenarios define TA/CA/ROA objects with controlled parameters (validity windows, IP extensions) to build arbitrary test cases.
- **Where applicable**: Any operator running or evaluating an RPKI validator, and any team building RPKI/ASPA tooling — all three tools are open source with public repositories.

### From Classic L3VPN to EVPN: Mastering Type 5 Routes on the Backbone

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/de-l3vpn-clasico-a-evpn-dominando-las-rutas-tipo-5-en-el-backbone-v1-samuel-emanuel-urbano-tomassoni.pdf) · [Recording](https://youtu.be/-CAbGJIpnfs)

Samuel Emanuel Urbano Tomassoni, Fernando Neiverth

- **Why**: This is the talk in the program squarely inside physical datacenter/campus fabric design — eliminating the centralized-L3-gateway tromboning problem in a leaf-spine EVPN-VXLAN fabric.
- **What**: A migration from an edge running EVPN-VXLAN as "dumb" L2 transport with IRB gateways concentrated on a heavy core router, to distributed anycast gateways extended to the leaf/edge switches using EVPN Type 5 (IP prefix) routes. Reported control-plane effect on their network: the `bgp.evpn` table dropped from 141,156 routes (Type-2 host routes) to 276 summarized Type-5 advertisements — over 99% reduction. Spines act as route reflectors, removing full-mesh iBGP.
- **How**: First-hop routing at the network edge via distributed anycast IRB on the leaves; Type-5 IP-prefix advertisements associated with BGP communities for granular inter-VRF traffic control; the EVPN control plane is decoupled from transport, so the underlay can move from VXLAN to SR-MPLS or SRv6 without refactoring edge configurations; BUM and management traffic confined to the edge.
- **Where applicable**: Leaf-spine datacenter and campus fabrics with routing-capable (EVPN Type-5 capable) edge switches. The before/after route counts are from the presenters' own network — org-specific — but the design pattern and the Type-2-to-Type-5 summarization argument are general.

### Latency-Based BGP Route Selection – An Intelligent Failover Engine Optimized with Supervised Learning

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/seleccion-de-rutas-bgp-basada-en-latencia-un-motor-de-failover-inteligente-optimizado-con-aprendizaje-supervisado-1.pdf) · [Recording](https://youtu.be/a1eB6ZnUDwQ)

Ernesto Sánchez (Universidad Católica de Salta, Argentina), Henri Alves de Godoy (Universidade Estadual de Campinas, Brasil)

- **Why**: Performance-aware routing is entering BGP via the IETF (a draft adding a NETWORK_LATENCY TLV to AIGP); this is a concrete, honestly-reported prototype of latency-triggered failover plus ML-based policy tuning.
- **What**: A failover engine that scores peer/DNS/jitter metrics (weights 0.27/0.50/0.23, packet loss as a severity multiplier), switching providers when the max DNS score exceeds 1.10 sustained over consecutive cycles and returning below 0.80 — rules designed to filter noise (trend, coefficient of variation, p95 deviation, z-score acceleration). Supervised learning over ~62 features and 50,000 simulated cycles (~26 days, 98.7% "normal" class): XGBoost ranks feature importance (DNS dominates at ~30% gain), logistic regression yields interpretable weights, both suggesting DNS should carry ~0.76–0.79 vs the current 0.50. Results: recall 0.95–0.97, precision 0.65–0.72, ROC-AUC ≈0.999, stratified 5-fold cross-validation. The authors are explicit that the dataset is synthetic (Ornstein-Uhlenbeck background noise, Poisson episode starts) calibrated to real measurements, and recommend validating against months of real history.
- **How**: Containerlab dual-provider ISP topology with DNS nodes, TimescaleDB metric store, Python capture/feature pipeline; the ML calibrates the existing deterministic scoring function rather than replacing it — that is the transferable idea.
- **Where applicable**: Dual-transit ISPs and enterprises; lab-validated only, not production-proven. Recall-heavy/precision-light tuning means false positives are the operational cost to watch.

### The mystery of the routes that refused to die

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/el-misterio-de-las-rutas-que-no-querian-morir-v2-andres-pugawko.pdf) · [Recording](https://youtu.be/_LmqccuTYAs)

Andrés Pugawko

- **Why**: By title, a routing postmortem — routes that persisted after they should have been withdrawn — which is exactly the sticky-state / withdrawal-propagation class of BGP datapath bug the PM cares about, and postmortems are the highest-transfer format at operator events.
- **What**: The program publishes no description for this talk, and no source text was available, so this entry reflects the title and speaker only. Judged by the title it is a troubleshooting narrative about routes that survived expected withdrawal; anything beyond that requires the slides or recording.
- **How**: Not determinable from the program text; slides and video are published.
- **Where applicable**: Unknown until reviewed — flagged here because the format and subject area are high-value for this reader.

### NTPv5 and Updated Time Security: What Changes for Network Operators

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/ntpv5-y-la-renovacion-de-la-seguridad-horaria-que-cambia-para-los-operadores-de-redes-v1-antonio-marcos-moreiras-1.pdf) · [Recording](https://youtu.be/O2yRiTr73oE)

Antonio Marcos Moreiras (NIC.br)

- **Why**: Time is a load-bearing security dependency — RPKI ROA validity windows, TLS certificates, Kerberos' 5-minute skew, log forensics; NDSS 2016 showed a few days of clock shift suffices to attack RPKI. And time rides on routing: ~2M NTP servers use a single upstream, and the 14,153 ASes hosting those upstreams publish no ROAs (IMC 2025), so a prefix hijack could set the time.
- **What**: NTS (RFC 8915) is deployable now (chrony ≥4.0, ntpd-rs; Ubuntu 25.10+ ships chrony with NTS by default) — yet 374 of 583 NTS servers are misconfigured (blocked TCP 4460, size filters dropping NTS packets on UDP 123). NTPv5 (draft 09, last call end-2026): client-server only, explicit timescale (UTC/TAI/UT1/smeared) and era fields, client cookies replacing request timestamps, 120-bit reference IDs. The 2035–2038 wall: leap seconds end by 2035, NTP era 0 ends 7 Feb 2036, 32-bit `time_t` overflows 19 Jan 2038 — equipment in service today will still be running. Plus NTP Pool research: ~10 well-weighted servers could capture most countries' time traffic (NDSS 2026), and some pool servers scan clients' IPv6 addresses (CCS 2026); Khronos (RFC 9523) and Roughtime as complements.
- **How**: NTS = TLS 1.3 key exchange on TCP 4460 with stateless cookies. Concrete checklist: allow 4460, review UDP 123 size filters, NTS on clients and servers with auto-renewed certificates, 4 or more identified independent sources by name, ROAs (and eventually ASPA) for your time servers; test NTPv5 in the lab within 12–24 months and inventory devices that will live past 2036.
- **Where applicable**: Any operator of time infrastructure or of anything time-dependent (PKI, RPKI, Kerberos, SIEM). Fully general, with an IETF document-status table (RFCs 8915, 9523, 9769, 10030; drafts for NTPv5, NTS pools, Roughtime, NTS4PTP).

## Adjacent

### Going IPv6-Only: From Myths to Modern Network Realities

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/07/transicion-a-ipv6-only-de-los-mitos-a-las-realidades-de-las-redes-modernas-v1-jen-linkova.pdf) · [Recording](https://youtu.be/tXvvk5DnYaY)

Jen Linkova (Google)

- **Why**: The clearest statement of the "IPv6-only is becoming the default for high-performing networks" argument, from one of the most experienced IPv6-only operators — and it comes with a deep hands-on companion track elsewhere in the program.
- **What**: Myth-busting (IPv6 is not "IPv4 with longer addresses," and the transition is not indefinitely deferrable), transition-technology realities in complex enterprise networks, and OS behavior with IPv4 fully disabled. Note: the published deck for this talk is largely charts (APNIC regional adoption stats; an addressing-efficiency example where a /19 was downsized to a /22, saving ~7K addresses). The concrete war stories live in the same speaker's tutorial in this program ("Hacia la transición definitiva de redes IPv6 Only"): Neighbor Discovery state-machine failures and unidirectional connectivity from broken multicast/ND filtering, ICMPv6 filtering breaking PMTUD, NAT64 MTU pitfalls (some vendors default NAT64 MTU to 1280; fragment-extension headers dropped by ACLs), IPv6 IPSec without UDP encapsulation, and AP/switch binding tables silently blocking the N+1 address of multi-address IPv6 hosts. The tutorial also covers DHCP option 108 via DHCP-Relay, 464XLAT with Jool on OpenWrt, DHCPv6-PD, and RFC 8950 (IPv4 routes with IPv6 next-hops) tested on MikroTik RouterOS v7.
- **How**: Systematic troubleshooting discipline (verify/reproduce → localize/isolate → one-variable controlled changes) applied to IPv6 specifics, with pcap-level ND case studies.
- **Where applicable**: Enterprise, campus, and access networks moving toward IPv6-only or IPv6-mostly; techniques are general, not Google-specific.

### IPv6-Mostly on Campus

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/ipv6-mostly-en-campus-1.pdf) · [Recording](https://youtu.be/DNDdFoDC014)

Henri Alves de Godoy (UNICAMP)

- **Why**: Measured, published evidence of what DHCP Option 108, PREF64, and CLAT actually do on a production campus — rare empirical data for anyone planning IPv6-mostly rollouts.
- **What**: A pilot on the FCA-Unicamp campus Wi-Fi (2,524 undergraduates). Findings: Option 108 (RFC 8925) does not prevent or disable IPv4 — the client decides; PREF64 (RFC 8781) is necessary but not sufficient; automatic CLAT activation is strongly associated with the absence of native IPv4. macOS/iOS/Android have native CLAT; Linux needs clatd or maturing NetworkManager support; Windows 11 began rolling out CLAT in September 2026. Dual-stack devices still send traffic toward PREF64/NAT64 (DNS64, Happy Eyeballs effects). Net effect: IPv4 DHCP pool pressure drops, and residual IPv4 dependency becomes visible and measurable — consistent with draft-ietf-v6ops-6mops (v10, Sep 2026).
- **How**: Standard tooling — radvd, Kea DHCPv4, BIND, Jool NAT64 (`--pool6 64:ff9b::/96`) — plus Python measurement scripts the authors published for download.
- **Where applicable**: Campus/enterprise managed networks; the methodology and scripts are replicable anywhere. Framed as "map where IPv4 is still needed" rather than "eliminate IPv4."

### Bypassing CGNAT. You Don’t Need PBR, and I Can Prove It!

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/bypass-de-cgnat-no-necesitas-pbr-y-puedo-demostrarlo-v1-douglas-fernando-fischer-1.pdf) · [Recording](https://youtu.be/Z1Fqa-zOXK0)

Douglas Fernando Fischer (NZM — network consultancy for ISPs)

- **Why**: A sharp, transferable edge-design pattern: steering CGNAT vs public-IP subscribers at a BNG without policy-based routing.
- **What**: The argument, walked through topology by topology, that PBR for CGNAT steering becomes unmanageable ("cancerígeno") as BNGs and CGNAT nodes multiply — and that doubling BNG hardware per subscriber type is the resource-infinite fantasy. The alternative: per-subscriber-type VRFs on a single BNG — the CGNAT VRF holds a default route to the CGNAT, the public-IP VRF defaults to the border router — i.e., source classification by VRF membership instead of per-flow policy matching. Bonus: VRFs as quarantine zones for infected CPEs.
- **How**: Logical-topology evolution from pre-CGNAT BNG designs, deliberately presented without CLI so the concepts transfer across vendors.
- **Where applicable**: ISP BNG/CGNAT environments with MPLS/VRF capability; a general technique, no hardware dependency stated. Most valuable to access networks with multiple BNGs and CGNAT nodes.

### Mission Accomplished? The 2026 KSK Rollover Story

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/09/mision-cumplida-la-historia-del-rollover-de-la-ksk-de-2026-v1-nicolas-antoniello-carlos-martinez.pdf)

Carlos Martínez (LACNIC), Nicolás Antoniello (ICANN)

- **Why**: The Internet's largest trust-anchor key rotation executed 11 October 2026 — and the talk's core message is a per-instance verification checklist, not a victory lap. A good template for any large-scale key-rollover program, including workload-identity trust roots.
- **What**: KSK-2024 (key tag 38696 / 0x9728) has signed the root DNSKEY set since 11 Oct 2026 14:00 UTC, after 21 months of prepublication (published Jan 2025, RFC 5011 acceptance Feb 2025). KSK-2017 stays published but non-signing until revocation (11 Jan 2027) and retirement (22 Mar 2027). Telemetry reading: RFC 8145 `_ta-` anchor-tagging queries (one capture showed ~38,989 unique source IPs still announcing only the old anchor) are a risk signal, not a census of failures — the 2018 lessons hold: forwarders mask the origin, signaling does not prove validating, and few reports do not prove absence of failures. "Completed" does not mean "all systems verified."
- **How**: Per-instance verification: 38696 present as accepted (not pending) in the effective trust-anchor state (`rndc managed-keys status`, `rndc secroots`), state persistence across restarts/replicas/containers/standbys and forwarding paths, and functional tests (valid root SOA with the AD bit; SERVFAIL on a known-broken domain; `+cdflag` as diagnostic only).
- **Where applicable**: Anyone operating DNSSEC-validating resolvers — especially forwarders and replicated/containerized deployments where RFC 5011 state can be lost on restart. Fully general.

### Keynote Presentation: Lessons in Digital Resilience: Multistakeholder Response and Connectivity Recovery in Venezuela Following the 2026 Earthquakes

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/09/presentacion-keynote-lecciones-de-resiliencia-digital-respuesta-multisectorial-y-recuperacion-de-la-conectividad-en-venezuela-tras-los-sismos-de-2026-v1-alejandra-stolk-ganteaume.pdf) · [Recording](https://youtu.be/RX5FInLGVPo)

Alejandra Stolk Ganteaume (Internet Society Venezuela; Head of Networks and Connectivity, Universidad de Los Andes)

- **Why**: A postmortem of physical-layer, national-scale infrastructure failure and recovery — exactly the class of hard-won lesson operator programs exist to surface.
- **What**: The 24 June 2026 earthquakes (a holiday, coinciding with a World Cup match at 18:00; alert at 18:04:31) produced simultaneous physical shear exceeding theoretical redundancy models for La Guaira's coastal infrastructure; NASA estimated 800+ collapsed buildings. Digitel's Direct-to-Device satellite roaming went from zero usage to peak within 5 days (Ookla measurements, 24 Jun–5 Jul). Around 77 emergency community networks were deployed by ISOC Venezuela and partners across isolated, rural, health, and education sites; the SAC submarine cable was cut and repaired; ISPs physically rescued fiber to reconnect communities.
- **How**: The architectural lessons: deploy CDN nodes directly at the local IXP (nap.ve) to keep traffic in-country and avoid tromboning via Miami; treat decentralized switching as the resilience model; and coordinate in three layers — institutional (regulator, universities, ISOC, LACNIC), field (UN agencies, NGOs, community leaders), and specialized (TSF, satellite providers).
- **Where applicable**: Venezuela-specific event, but the design lessons (IXP-localized traffic, edge caching, D2D as an emergency tier, converting emergency networks into self-sustaining community networks) transfer to resilience planning anywhere. Next step proposed: a regional technical emergency group for digital resilience.

### A Network Tomography Approach to Imputing OD Traffic in an IP/MPLS Network

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/10/un-enfoque-de-tomografia-en-redes-para-imputar-trafico-od-en-una-red-ip-mpls-v1-claudio-risso-carlos-martinez-pablo-cuello.pdf) · [Recording](https://youtu.be/GuxZLeRFLH0)

Claudio Risso (Universidad de la República – FING), Carlos Martínez (LACNIC), Pablo Cuello (ANTEL)

- **Why**: Origin-destination traffic matrices drive capacity planning, what-if/failure analysis, anomaly detection, and interconnect optimization — and per-LSP statistics in IP/MPLS networks are unreliable precisely because they are not standardized.
- **What**: A network-tomography method that infers OD traffic by combining LSP statistics with trusted physical-interface counters. Production validation on ANTEL's international network (May 2025: 31 nodes, 930 tunnels, 128 directed links, 5-minute samples): 47,430 model parameters fit against 261,248 measurements (~5.5:1) via positivity-constrained least squares that exploit the daily traffic profile's temporal correlation. The top 25 LSPs (2.69% of tunnels) carried 60% of traffic; solving sequentially from the heaviest LSPs first stabilizes the initialization-sensitive iterative fit. The "blackbox" mode is technology-independent (native IP, MPLS, Segment Routing) and works even where LSP statistics are absent.
- **How**: Linear model Y = AX where A holds ECMP-aware routing fractions per link/tunnel, plus a piecewise-linear daily-profile constraint matrix B; constrained least squares; the toy example makes the underdetermination explicit (34 link measurements vs 132 OD unknowns).
- **Where applicable**: Validated on ANTEL's production network — org-specific data — but the method generalizes to any IP/MPLS backbone with interface counters and known topology. Transient failures/restorations are explicitly out of scope, and results are approximations of an inherently underdetermined problem.

### Lightning Talks

**Links:** [Slides (PPTX)](https://apievt.lacnic.net/wp-content/uploads/2026/08/the-enemy-within-el-enemigo-en-casa-v1-roberto-oya-luengo.pptx) · [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/08/the-enemy-within-el-enemigo-en-casa-v1-roberto-oya-luengo.pdf)

Multiple speakers, incl. Roberto Oya Luengo (Nokia Deepfield), Jen Linkova, Hernan Uriel Kleinman, Antonio Marcos Moreiras, Sergio Kleiman, Celsa Sánchez, Christian O’Flaherty

- **Why**: The densest signal-per-minute slot in the program; several land directly in the PM's lanes.
- **What**: Highlights from the source material: "The enemy within" (Roberto Oya Luengo, Nokia Deepfield) — residential proxy services renting out compromised endpoints, a market the presenter puts at over US$4B/year, growing exponentially since 2022 when content providers began blocking AI crawlers and AI companies began paying to masquerade as consumer traffic; US IPs priced ~100x Russian ones; supply from factory-compromised devices and infected SDKs; used for fraud and outbound DDoS; edge-based botnet C2 disruption demonstrably works. "rpki-selflab" (Antonio Marcos Moreiras) — a self-contained Docker RPKI lab (on GitHub) exercising ROA, ROV and ASPA across BIRD+Routinator, OpenBGPD+FORT, and OpenBGPD+rpki-client stacks while following a hijacker and a leaky peer. Also relevant: "Proxies residenciales" (Hernan Uriel Kleinman) on the same proxy economy from the ISP angle, "Updating the MANRS Network Operators baseline" (Sergio Kleiman), and "DNS anycast — who answers behind the cloud" (Celsa Sánchez).
- **How**: 10-minute talks plus 5 minutes Q&A, selected by the LACNOG program committee.
- **Where applicable**: Mixed by construction; the residential-proxy analysis and the RPKI selflab are the two most broadly adoptable items.

### Between the Law and the Protocol: An Overview of Blocking Orders on the Brazilian Internet

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/entre-el-derecho-y-el-protocolo-un-panorama-general-de-las-ordenes-de-bloqueo-en-internet-en-brasil-v1-pedro-de-botelho-marcos.pdf) · [Recording](https://youtu.be/Cyl1GHusKKY)

Pedro de Botelho Marcos, with Thiago Ayub and Vinícius Anselmo (NIC.br, per slides)

- **Why**: Court-ordered blocking has become a routine operator workload with measurable collateral damage — relevant both operationally and to any DNS/security product with filtering features.
- **What**: Brazil is estimated to have blocking orders covering roughly 135,000 Internet resources. One ISP received 733 orders between December 2022 and October 2026 (period growth: 16 → 150 → 295 → 272). Motivators: piracy, cybercrime, fake news. The mechanics are walked through end-to-end: ISP-resolver blocking vs public resolvers vs the registry sinkhole, IP/TCP-SYN interception at the AS border; and the evasions: VPNs, domain re-registration, IP changes. Collateral effects: shared-IP hosting takes down unrelated domains, indefinite IP blocks strand addresses as infringers move, and secret orders leave users unable to distinguish blocking from outages.
- **How**: Measurement over a single ISP's order corpus plus public data; the presenters explicitly do not question the validity of the orders themselves. Caveat from the slides: no guarantee all ISPs received the same order set.
- **Where applicable**: Brazil-specific dataset, but the overblocking mechanics and evasion patterns generalize to any jurisdiction with blocking regimes. A companion LACNIC/MARYVA study elsewhere in the program ("Site Blocking in Latin America and the Caribbean") covers 18 countries and finds reactive blocking now dominant, with dynamic IP lists and growing ISP obligations trending region-wide.

## Wildcard

### Monitoring to Mitigate Micro-Outages in MikroTik-Based ISP Topologies Using Natural Language

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/10/monitoreo-para-mitigar-microcortes-en-topologias-isp-basadas-en-mikrotik-mediante-lenguaje-natural-v1-joaquin-tadeo-riedmaier-santiago-agustin-zualet.pdf) · [Recording](https://youtu.be/7342HApR9F8)

Joaquin Tadeo Riedmaier, Santiago Agustín Zualet (Universidad Nacional de Misiones, Argentina)

- **Why**: The clearest example at this meeting of LLMs entering network operations — and it is designed privacy-first, which is the pattern most likely to survive contact with real enterprises.
- **What**: An on-prem monitoring stack for MikroTik-based small ISPs: syslog push plus RouterOS v7 REST pull (interface traffic/errors, CPU/RAM, connection tracking, ARP, PPPoE/RADIUS sessions) through Django/Python/PostgreSQL, with noise filtering (37 cyclic log lines collapsed into one event row), threshold alerts via Telegram, and a locally hosted LLM answering natural-language questions via text-to-SQL over flattened read-only views with RAG-anchored responses (grounding goal ≥95%). Projected effect: critical-event diagnosis from ~90 minutes to ~18. Everything stays inside the ISP (framed against Argentine data-protection law 25.326); an external-API extension exists only as an anonymized option.
- **How**: Flattened schema (fewer JOINs → fewer hallucinations), a SELECT-only database user so the model cannot modify anything, and cross-signal correlation of L2/L3 metrics, conntrack, RADIUS sessions, and syslog. The LLM runs on 32 GB of RAM locally.
- **Where applicable**: Built for the 1,500+ small ISP/cooperative context in Argentina, but the architecture — a read-only natural-language query layer over normalized telemetry — transfers to any environment. The time-savings figure is a projection; the slides explicitly label the flagship correlation scenario as illustrative, not measured.

### Beyond the Radio Link: Routing Dynamics in LEO Satellite Networks

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/08/mas-alla-del-enlace-de-radio-dinamica-del-enrutamiento-en-redes-de-satelites-leo-v1-katarina-stefanovic-1.pdf) · [Recording](https://youtu.be/btqpBfW38wk)

Katarina Stefanović

- **Why**: LEO constellations are becoming a standard connectivity tier (the Venezuela keynote's emergency D2D roaming is the same trend), and routing over continuously changing topologies is a genuinely different routing problem — one the PM would not otherwise encounter in a routing-security-heavy program.
- **What**: No abstract was published and no source text was available, so this entry reflects the title only: by its title, the talk addresses routing dynamics beyond the radio link in LEO satellite networks. (from abstract only — title and materials only)
- **How**: Not determinable from the program text; slides and video are published.
- **Where applicable**: Unknown until reviewed; flagged as a wildcard because the subject sits outside the program's routing-security mainstream while signaling where interconnect is heading.

### From CLI to Autonomous Networks: How the Evolution of Protocols Made Operational AI Possible

**Links:** [Slides (PPTX)](https://apievt.lacnic.net/wp-content/uploads/2026/08/de-cli-a-redes-autonomas-como-la-evolucion-de-los-protocolos-ha-posibilitado-la-ia-operativa-v1-luiz-cosme-puppin-magalhaes.pptx) · [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/08/de-cli-a-redes-autonomas-como-la-evolucion-de-los-protocolos-ha-posibilitado-la-ia-operativa-v2-luiz-cosme-puppin-magalhaes.pdf) · [Recording](https://youtu.be/TtdnnsSlssQ)

Luiz Cosme Puppin Magalhaes

- **Why**: The thesis in the title — that protocol evolution (machine-readable, model-driven interfaces and telemetry) is what made AI-driven operations possible — is the correct frame for where operator automation is heading, and it complements the two other AI
