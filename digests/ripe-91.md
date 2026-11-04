<!--
conference: RIPE 91 (Bucharest)
type: operator
source_url: https://ripe91.ripe.net/programme/meeting-plan/
generated: 2026-11-04
registry_key: ripe-91
written_by: ToFaRev (zai-org/GLM-5.3)
-->

## Core

### PON in the Datacenter: Hyperscale for Management and Console

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/19/LVTBYA/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/LVTBYA/resources/RIPE_talk__PON_in_the_XJUogPt.pdf) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/LVTBYA/resources/RIPE_talk__PON_in_the_C4EG6bG.pdf) · [Recording](https://ripe91.ripe.net/media/videos/mike-joseph_pon-in-the-datacenter-hyperscale-for-management-and-console_main_20251021-145654.mp4)

Mike Joseph, Meta

- **Why**: A genuinely novel direction in physical datacenter networking: Meta is running Passive Optical Networking — residential access technology — as the management, console, and out-of-band fabric in production hyperscale DCs. For anyone whose job includes DC cabling plant and topology, this is a production data point on killing copper at scale.
- **What**: Meta's Infrastructure Network Engineering team replaced per-row fixed Ethernet switches and terminal servers with a PON-based handoff: each rack gets up to 20 Ethernet + 20 console connections (or 32 + 8 tradeoff), configurable per rack without row-level coordination. Two centralized OLT routers serve 12 rows; a row can carry up to 1,280 Ethernet and 800 console connections. Copper cable trays and copper distribution are eliminated entirely from the data halls.
- **How**: Passive splitters plus per-rack ONUs and purpose-built console cards; OLT configuration is generated from Meta's network modeling service and asset databases. ONUs are barcode-scanned as racks are deployed, updating asset management in real time; because ONUs are stateless, hardware replacement is just scanning a new one. OMCI-based management gives uniform control over multi-vendor ONUs and console devices.
- **Where applicable**: The scale and automation stack are Meta-specific, and the technique targets low-speed (≤1GE + RS-232) connectivity, not production fabric. But the concept — PON as a cheap, flexible, copper-free fan-out for management/OOB — is broadly adoptable by any DC operator; it requires buying into the PON ecosystem and OMCI tooling rather than any Meta-internal dependency.

### Getting 1+ Tbps from an x86 server

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/19/QFTE87/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/QFTE87/resources/RIPE91_1Tbps_Branimir_JaVg5wW.pdf) · [Recording](https://ripe91.ripe.net/media/videos/branimir-rajtar_getting-1-tbps-from-an-x86-server_main_20251021-142824.mp4)

Branimir Rajtar, 5x9 Networks

- **Why**: A concrete, quantified datapath-tuning story: a virtualized BNG went from 160 Gbps to 1.2 Tbps on a single commodity x86 server with no specialized hardware. The optimization methodology (profiling-driven, cache-focused) transfers to any high-packet-rate software datapath — exactly the kind of datapath-internals work that is core here.
- **What**: A CUPS (control/user-plane separation) vBNG — dashboard, controller, and DPDK-based forwarder — was pushed through successive optimization waves: ~30% from newer hardware plus application tuning, ~30% from deep DPDK/CPU/PCIe/BIOS/NIC configuration, and ~20% from Intel vTune-guided code rewrites. The final revelation: the dominant residual cost was CPU cache misses — data structures not fitting 64-byte cache lines, plus 4K memory pages, causing constant main-memory round trips. A major cache-alignment rewrite and a shift from many small 4-vCPU VMs to one large instance closed the gap to 1.2 Tbps.
- **How**: SR-IOV and Intel DPDK bypass the kernel entirely (with the known tradeoff of CPU running at 100% in poll mode); vTune identifies hot spots; code is restructured to separate read/write data sections, reorder instructions for multiple execution units, use full cache lines, and force compiler optimizations. Each change was performance-tested in isolation.
- **Where applicable**: Results are specific to their PPPoE/IPoE BNG workload on Intel Xeon Gold with DPDK-supported NICs — treat the numbers as one datapoint, not a guarantee. The method (profile, fix cache behavior, consolidate instances) is generally applicable to anyone writing or buying software datapaths.

### gNMI and you: The death of SNMP was greatly exagerated

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/8/X7N8NC/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/X7N8NC/resources/gNMI_Talk_RIPE_AUJo4zH.pdf) · [Recording](https://ripe91.ripe.net/media/videos/tom-strickx_gnmi-and-you-the-death-of-snmp-was-greatly-exagerated_main_20251020-150134.mp4)

Tom Strickx, Cloudflare

- **Why**: Network observability is a core ops responsibility, and gNMI/OpenConfig is the leading SNMP replacement — but real production experience, including failures, is rarely shared. Cloudflare's honest accounting of what works and what still hurts is exactly the decision-support material needed before betting a monitoring stack on it.
- **What**: An introduction and comparison: gNMI (gRPC-based, OpenConfig YANG models, ProtoBuf, TLS required by default, pub/sub) versus SNMP (OID sprawl, ASN.1, plaintext by default, pull-plus-traps). Then the unvarnished problems: uneven vendor adoption ("your fridge probably ships with SNMP"), vendor inconsistency, and thin documentation. Production pain points include distributed counting (correctly counting events across a fleet is genuinely hard) and per-linecard counters on Juniper requiring monotonicity handling (Prometheus-style counter-reset adjustment).
- **How**: Cloudflare runs gNMIc (Nokia-developed, now OpenConfig-owned, actively maintained) with internal processors and an aggregation layer; the talk surveys the wider toolchain (gNMI-gateway, ExaRing's exporter, Telegraf with gNMI plugins) and notes which are unmaintained-but-working.
- **Where applicable**: Broadly applicable — the gNMI/SNMP comparison and tooling recommendations are vendor-neutral. The scale and some quirks are Cloudflare/Juniper-specific; vendor consistency caveats should be validated against your own fleet before migration.

### Collecting and analyzing routing information with Rotonda

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/15/CLRNRY/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/CLRNRY/resources/rotonda_ripe91_eFWBjdb.pdf) · [Recording](https://ripe91.ripe.net/media/videos/luuk-hendriks_collecting-and-analyzing-routing-information-with-rotonda_main_20251021-090048.mp4)

Luuk Hendriks, Jasper den Hertog — NLnet Labs

- **Why**: Route monitoring at scale is hard: vendor platforms give limited insight, especially into RPKI's effect on routes. Rotonda is adoptable, open-source tooling that lets an operator ask their own questions of their BGP/BMP data — the kind of tooling the triage guidance says to up-rank.
- **What**: A single self-contained Rust binary that ingests routing data via BMP (pre/post-policy Adj-RIB-in/out and Loc-RIB), live BGP, and MRT files, combines it with RPKI data via RTR, and exposes HTTP API, MQTT, and file outputs. Its distinguishing feature is Roto, a strongly-typed scripting language for filtering routes and monitoring events — compiled to native machine code (via Cranelift, to x86_64 or ARM64), so customization costs negligible overhead even in the hottest ingestion paths.
- **How**: Operators write small typed filters (reject iBGP, drop specific peers, log prefixes matching prefix lists) that run inside the collection pipeline rather than as post-processing. Designed to scale from 50 routes to 50 million with the same single binary.
- **Where applicable**: General-purpose and self-hostable by networks of any size — explicitly built for small operators who find heavyweight monitoring disproportionate. Still young; the presenters were actively soliciting feedback and use cases.

### Querying the DFZ

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/22/3Q7AUL/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/3Q7AUL/resources/20251020_querying_the_VpHijNI.pdf) · [Recording](https://ripe91.ripe.net/media/videos/ties-de-kock_querying-the-dfz_main_20251021-165631.mp4)

Ties de Kock, RIPE NCC

- **Why**: MRT parsing has always been the barrier to doing your own BGP analysis — most teams default to whatever prebuilt tools offer. RIPE RIS publishing its data as indexed Parquet makes DFZ-scale analysis a SQL problem, which changes what a network team can realistically do for itself.
- **What**: RIPE RIS BGP RIBs and updates are now published as Parquet files: a daily RIB of ~350M rows (~2.4 GB) and hourly update files (~50M rows, 350–400 MB), with columns for timestamp, prefix, origin AS, peer, AS path, and communities. Query with DuckDB, SQL, or dataframe tools instead of MRT parsers; analyses that previously took 10+ minutes run in seconds. RIPE NCC has already used it operationally — assessing BGP impact of the Baltic Sea cable damage and the Iberian power outage in minutes instead of hours.
- **How**: Parquet plus DuckDB replaces both custom MRT parsing scripts and expensive database indexing; the schema is designed to be ergonomic for queries and correct for analysis (AS sets are supported rather than flattened away).
- **Where applicable**: Free and broadly usable by any operator or researcher. Caveat: the short-term archive covers 14 days of RIBs/updates (an 18-month experiment with a go/no-go decision), so deep historical work still goes through MRT files.

### A Farewell to ARPs - IPv6 resolved gateways

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/10/Y8YVLE/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/Y8YVLE/resources/ipv6_resolved_gateway_68S55oI.pdf) · [Slides (Keynote)](https://pretalx.ripe.net/media/ripe91/submissions/Y8YVLE/resources/ipv6_resolved_gateway_ZwyAD62.key) · [Recording](https://ripe91.ripe.net/media/videos/remco-van-mook_a-farewell-to-arps-ipv6-resolved-gateways_main_20251020-171800.mp4)

Remco van Mook

- **Why**: IPv6-only fabrics with native IPv4 reachability is a live design problem for DC/WAN interconnect. This proposes a clean mechanism to give IPv4-capable hosts on an IPv6-only network a working IPv4 default gateway without ARP, tunnels, or translation — complementary to RFC 8950 (IPv4 NLRI with IPv6 next-hop).
- **What**: A draft I-D requesting 192.0.0.11/32 from the IANA IPv4 special-purpose registry. The address is a signal: hosts configured with it as their IPv4 default gateway resolve the gateway's link-layer address from the IPv6 default gateway learned via RA/ND — reusing the IPv6 neighbor cache instead of running ARP. IPv4 packets remain native and unaltered; no IPv4 subnets, no tunneling, no NAT.
- **How**: The host treats the gateway IP as a pure identifier for "use the IPv6 gateway's L2"; working code exists in Linux user space (kernel 5.2+) using rtnetlink to track the IPv6 gateway. A transitional deployment — DHCP-assigned /32 address plus a host route for 192.0.0.11 with the address answered on router interfaces — is essentially what some hosting providers (Hetzner-style) already do.
- **Where applicable**: General technique for IPv6-only datacenters and hosts; cleanly it needs OS network-stack support (currently user-space/known-config), but the transitional method is deployable today. Aligns with ongoing IETF v4-via-v6 work; the presenter was soliciting review of the draft and code.

### Rewriting BGP Origin

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/30/GJ8PFJ/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/GJ8PFJ/resources/RIPE91_-_BGP_Origin_T_HYCTVQf.pdf) · [Recording](https://ripe91.ripe.net/media/videos/james-bensley_rewriting-bgp-origin_main_20251022-120705.mp4)

James Bensley, Inter.link

- **Why**: A rare public airing of a quiet interdomain game: carriers rewrite the BGP ORIGIN attribute to IGP because IGP beats INCOMPLETE in best-path selection, thereby attracting traffic. Anyone buying or selling transit — or wondering why traffic prefers a peer's path — needs to know this is happening.
- **What**: Based on looking-glass captures of all Tier-1s, 6 of 16 were rewriting ORIGIN to IGP at the time of the talk (AS1299, 2914, 3356, 3491, 6453, 6939; note the speaker's post-talk correction that AS3320 was incorrectly listed and does *not* do this). The DFZ is already >90% IGP-origin. Inter.link (AS5405) resisted, but lost customers over the resulting traffic asymmetry and will now rewrite to IGP on all eBGP advertisements — with a per-customer opt-out — arguing that universal adoption implicitly deprecates the attribute. Bonus intel: some T1s use addresses in 2/8 as BGP router IDs to win router-ID tie-breaks.
- **How**: Exploits the ORIGIN tie-break in best-path selection; RFC 4271 says ORIGIN "SHOULD NOT" be changed, and rewriting carriers lean on RFC 2119's wiggle room to justify "normalization".
- **Where applicable**: Relevant to any network announcing prefixes or selecting transit providers. The who-does-it list is a point-in-time snapshot (October 2025) and the game is zero-sum — expect more networks to follow once competitors start.

### PQC for the RPKI

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/10/7NJSVS/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/7NJSVS/resources/pqc-rpki-ripe91_m6SZgmM.pdf) · [Recording](https://ripe91.ripe.net/media/videos/dirk-doesburg_pqc-for-the-rpki_main_20251020-160112.mp4)

Dirk Doesburg, Radboud University / SIDN Labs

- **Why**: The RPKI is RSA-only, and a quantum-capable attacker is *worse* than no RPKI at all: forged ROAs can make legitimate announcements ROV-Invalid while malicious ones validate. Migration will take years, so the groundwork — which signatures, how to migrate — matters now. This is routing security with a long planning horizon.
- **What**: An MSc thesis laying out the full migration path. (1) Attack analysis: forged ROAs/revocations (including entire CAs), AS0-roa DoS, and ASPA forgery. (2) Signature evaluation across post-quantum schemes: Falcon-512 wins (NIST level 1, 897 B public key, 666 B signature; RPKI grows from 838 MB to ~1.4 GB, download from ~14.5 s to ~24 s, versus catastrophes like SLH-DSA at ~14 GB). (3) The "null scheme": replaces the one-time EE key and signature in each signed object with a SHA256 digest, cutting the median hybrid (Falcon-512 + RSA-2048) ROA from 4,354 to 2,295 bytes and ~35% of verification CPU — largely paying for the PQC switch; documented as an Internet-Draft with working prototypes in Krill and Routinator. (4) A mixed-tree migration procedure simpler than RFC 6916: no globally coordinated milestone days, no top-down switch, ordinary RFC 6489-style key rollovers per CA, with relying-party software and trust anchors updated first.
- **How**: Measured real costs (RPKI download ~14.5 s, ~13 CPU-seconds of verification as baseline) across candidate algorithms; hybrid signatures recommended for safety during transition.
- **Where applicable**: RPKI-wide — every RIR, CA, and relying party, not org-specific. Prototypes exist for two of the main open-source tools; actual migration requires SIDRops standards work and multi-year lead time, which is precisely the argument for engaging now.

### Exploring the Blind Spot of IXP Route Server

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/27/C3ZSGJ/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/C3ZSGJ/resources/RIPE_91_aFUJkm1.pdf) · [Recording](https://ripe91.ripe.net/media/videos/stefano-servillo_exploring-the-blind-spot-of-ixp-route-server_main_20251022-090928.mp4)

Stefano Servillo, Sapienza University of Rome

- **Why**: Most peering-edge routing security attention goes to RPKI, but IRR-based route-server filtering — still the primary mechanism at most IXPs — has a structural hole that enables prefix hijacking. If you peer via route servers, this is a direct exposure assessment.
- **What**: The blind spot: IRR validation expands a member's AS-SET into a prefix list but never binds a prefix to its real owner. So an attacker whose route object for a prefix lists an AS that appears in some member's AS-SET gets their (hijacked or misconfigured) announcement accepted by the route server. The authors found most analyzed IXPs in the EURO-IX community affected, and validated the practical impact against real route-server RIBs of two major European IXPs. Feasibility is real: roughly a third of prefixes are RPKI NotFound (no ROA coverage), leaving IRR as the only filter — and AS-SETs are badly maintained (they accumulate inactive ASes against ~77k active of ~130k allocated, plus duplication in non-authoritative IRRs).
- **How**: Walks through how IXPs compile IRR data (bgpq4 expansion into prefix lists linked to peer sessions), derives the attack preconditions (no covering ROA, prefix in a route object for an AS that's in a member's AS-SET), and proposes fixes for both IXP operators (filtering changes) and members (ROA coverage, AS-SET hygiene).
- **Where applicable**: Applies to any IXP using IRR-based RS filtering and any member relying on RS filtering instead of bilateral sessions. The validation data is from two large European IXPs, but the mechanism is protocol-level and general.

### Assessing the feasibility of routing security compliance tests

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/30/L3FE7Y/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/L3FE7Y/resources/ripe_presentation_hLR4Uxr.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe91/submissions/L3FE7Y/resources/ripe_presentation_7mjXJkB.pptx) · [Recording](https://ripe91.ripe.net/media/videos/moritz-muller_assessing-the-feasibility-of-routing-security-compliance-tests_main_20251022-110409.mp4)

Moritz Müller, Lisa Bruder — SIDN Labs, University of Twente

- **Why**: Routing-security hygiene (MANRS and its elevated "MANRS+" tier) has been self-attested; this work asks whether it can be *measured* — and builds an open-source, containerlab-based harness to do it. Two interests in one: routing security plus a transferable use of Containerlab as an automated audit testbed.
- **What**: A prototype that audits an AS's routing-security controls (route origin validation, customer prefix filtering, bogon filtering) by standing up the audited AS between two local ASes in a containerlab topology: one exports prefixes to it, the other imports what it re-advertises. Analyzing the imported prefixes reveals the filters actually configured. In the testbed it reliably audits correct filter implementation — for example, by mutating a route object to disallow a prefix and observing whether the audited AS stops exporting it.
- **How**: Fully containerized local testbed (code open source on GitHub as SIDN/manrs-prototype); import filters compiled with bgpq4 against IRR; test prefixes withdrawn immediately to avoid unintended propagation.
- **Where applicable**: The prototype works locally; auditing production ASes is future work with identified pitfalls (RPKI/IRR propagation delays, multi-control-plane ASes, risk of test announcements leaking). The community was being asked for feedback on what a production deployment (led by GCA) should handle. The containerlab-as-auditor pattern is adoptable by anyone wanting to verify routing hygiene of partners or their own network.

## Adjacent

### Free and open-source network labs with Containerlab: an intro, an update, a workshop

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/2/9HJZQY/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/9HJZQY/resources/Containerlab_Preso_No_2MIPNyQ.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe91/submissions/9HJZQY/resources/Containerlab_Preso_N_lEs9jGc.pptx) · [Recording](https://ripe91.ripe.net/media/videos/gordon-gidofalvy_free-and-open-source-network-labs-with-containerlab-an-intro-an-update-a-work_main_20251020-090126.mp4)

Gordon Gidofalvy, Nokia

- **Why**: Lab-as-code is the closest thing network engineering has to CI for topology and config change — useful for prototyping fabrics, regression-testing config, and reproducing vendor claims before they touch production. This is the tool's 5-year status review plus a hands-on workshop.
- **What**: Containerlab at ~300K installations, 140+ contributors, 35+ supported network OSes (13 added in the last 12 months). Node types span containerized NOSes (SR Linux, SR OS, cEOS, XRd, cRPD, and more), VM-based NOSes wrapped in containers via vrnetlab (Juniper vMX/vJunosRouter, Arista vEOS, Cisco XRv9k/NX-OS, Fortinet, Palo Alto, OcNOS), and arbitrary regular containers — FRR, traffic generators, telemetry stacks, IPAM/DCIM, flow collectors. Declarative YAML topologies make labs versionable, shareable artifacts.
- **How**: Docker-based; a topology file defines nodes and links; the workshop walks from a first FRR lab through expanding topologies to collaboratively building a working "Internet". Requires a Linux host on kernel 5.4+ (physical or VM).
- **Where applicable**: Broadly applicable anywhere Docker runs; the intro half is 101 material, but the ecosystem update (including non-labbing use cases like the SIDN routing-security audit prototype) is where the value is for someone already past the basics.

### What happens when you overshare? A Look into the BGP Maximum-Prefix Feature

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/30/JDHZFZ/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/JDHZFZ/resources/slides_UDSaivF.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe91/submissions/JDHZFZ/resources/slides_p7lkxZE.pptx) · [Recording](https://ripe91.ripe.net/media/videos/orlando-eduardo-martinez-durive_what-happens-when-you-overshare-a-look-into-the-bgp-maximum-prefix-feature_main_20251022-115547.mp4)

Orlando Eduardo Martínez-Durive — NetAI & IMDEA Networks (work done as a research intern at Cisco ThousandEyes); Antonis Chariton — Cisco

- **Why**: Everyone configures max-prefix limits, almost nobody knows what actually happens when they're exceeded. This quantifies it over 6.5 months, which turns a superstition into data for setting limits.
- **What**: Using RIPE RIS RIBs (Jan 1 – mid-July 2025) plus historical PeeringDB data: of 88,223 identified ASes, only 16,351 (18.5%) had PeeringDB entries updated within two years and were analyzable. Findings: only a relatively small number of ASes exceed their advertised limit; on average only a small fraction of peers drop the session when it happens — but there are extreme cases where a network loses >80% of its peers, with obvious connectivity impact. Notably, the authors could not confirm that observed drops were actually caused by the limit being exceeded.
- **How**: Correlating announced prefix counts against PeeringDB-listed maximum-prefix values over time, plus tracking peer-count changes after exceedance.
- **Where applicable**: General BGP session-management practice. Big caveat: PeeringDB-listed limits are a proxy for actual peer-side configuration, and the analyzable population is skewed toward networks that maintain their PeeringDB entries. Practical takeaway offered: set peer limits "just slightly higher" than expected, and the open question of per-session limit signaling (à la OPEN extension) is worth community thought.

### The BGP Clock and the BGP Observatory: Hunting Stuck Routes

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/19/87WNTB/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/87WNTB/resources/RIPE91_-_Observatory_5R1avlF.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe91/submissions/87WNTB/resources/RIPE91_-_Observatory_vUkJEcP.pptx) · [Recording](https://ripe91.ripe.net/media/videos/antonios-chariton_the-bgp-clock-and-the-bgp-observatory-hunting-stuck-routes_main_20251021-140237.mp4)

Antonis Chariton, Cisco

- **Why**: Stuck BGP routes (withdrawals lost to router bugs) silently keep traffic flowing toward dead paths — and after a route goes stale, nobody notices. This provides both a permanent public measurement beacon and a free detection tool anyone can point at their own network.
- **What**: Follow-up to the RIPE 89 study (which found prefixes still stuck in RIBs months after withdrawal, despite being RPKI Invalid). The BGP Clock announces time-encoded prefixes on a fixed schedule: IPv6 `2a0d:3dc1:NNNN::/48` indexed by 10-minute period since New Year (recycled yearly), and IPv4 `147.189.(216+N).0/24` by hour-of-day modulo 8, announced at XX:00 and withdrawn at XX:10. The BGP Observatory is a free, no-login service that detects and surfaces stuck routes, searchable by AS. RFC 9687 attempts to reduce the impact but needs vendor support.
- **How**: Beacon prefixes are originated from a dedicated AS (AS4601, moving to AS210312); operators can sanity-check their own RIBs directly (`show route` for the beacon prefixes) or use the Observatory's automated analysis.
- **Where applicable**: Any operator or researcher; the phenomenon's prevalence depends on the vendor/bug mix in the forwarding path, so absolute numbers will shift over time — the value is the standing instrument, not a single result.

### Are NTP Clients Always Right?

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/17/RNBMHH/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/RNBMHH/resources/RACI_7mUlSus.pdf) · [Recording](https://ripe91.ripe.net/media/videos/shreyas-konjerla_are-ntp-clients-always-right_main_20251021-113305.mp4)

Shreyas Konjerla, TU Delft

- **Why**: Time infrastructure trust underpins everything else — TLS, Kerberos, log forensics — but client-side NTP hardening is rarely examined. This stress-tests the default time clients of major operating systems and finds the weakest of them are trivially manipulable.
- **What**: Eight (S)NTP clients across three OSes were baselined for 60 hours and then attacked. All SNTP clients — the *defaults* of major OSes — are vulnerable to time-shift attacks (macOS accepted injected offsets from 900 s up to two years); none of the full NTP clients were. Five bugs and one vulnerability were disclosed, including: NTPD-RS flooded with queries under certain Kiss-of-Death packets, OpenNTPd unable to handle the NTP timestamp rollover, and TimesyncD using a single server (a single point of failure). Also forecast: Ubuntu's planned default move to NTS/chrony will multiply query volume ~11x and traffic ~25x per host.
- **How**: Controlled testbed of three local NTP servers with a threat model of malicious-server redirection (via NTP pool or DNS hijack); clients measured for query behavior, server rotation, and spec compliance.
- **Where applicable**: Directly actionable for fleet configuration choices (which client, how many servers, panic thresholds); thesis-scale work but with real vendor disclosures. The Ubuntu/NTS traffic forecast matters to anyone operating NTP infrastructure at enterprise or ISP scale.

### An empirical evaluation of longitudinal anycast catchment stability

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/22/RQBH3N/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe91/submissions/RQBH3N/resources/anycast_stability_RIP_q1Xz8KX.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe91/submissions/RQBH3N/resources/anycast_stability_RI_fw0Yv8z.pptx) · [Recording](https://ripe91.ripe.net/media/videos/remi-hendriks_an-empirical-evaluation-of-longitudinal-anycast-catchment-stability_main_20251021-164229.mp4)

Remi Hendriks, University of Twente (with Bernhard Degen, Bas Palinckx, Raffaele Sommese, Roland van Rijswijk-Deij)

- **Why**: Anyone running an anycast service (DNS, CDN edges, global ingress) needs to know how often to remap catchments — too rarely and traffic engineering is stale, too often and you burn effort. This replaces guesswork with six months of daily measurements.
- **What**: Daily Verfploeter catchment mappings on an industry-grade 32-PoP anycast testbed (20 countries, 6 continents) across IPv4 and IPv6 for six months (~3.5M responsive /24s, ~0.5M IPv6 /48s probed). Result: catchments are very stable short-term — 95% of prefixes route to the same PoP at one-week granularity, >99% day-to-day — and an IPv4 mapping stays valid roughly two months at a 10% error rate. But sudden routing events can shift catchments dramatically: in July, the Tokyo PoP lost most of its traffic to a Sydney PoP that expanded five-fold; north-eastern China switched to Frankfurt; Vietnamese addresses moved to Seoul.
- **How**: Active probing with one target per smallest propagated BGP prefix, using the USC/ISI and TUM IPv6 hitlists; stability measured across timescales from days to months.
- **Where applicable**: The recommendations (how frequently to run catchment analysis) apply to anycast operators generally, but absolute stability numbers come from a Vultr-hosted testbed — your mileage will vary with topology, peering, and remote-peering prevalence. The event-driven instability finding (plan for sudden shifts, not gradual drift) is the transferable lesson.

### What's new at the IETF?

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/17/CGDZGZ/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/CGDZGZ/resources/RIPE_IETF_Whats_New_S_AQNgBgL.pdf) · [Recording](https://ripe91.ripe.net/media/videos/suresh-krishnan_whats-new-at-the-ietf_main_20251021-110114.mp4)

Suresh Krishnan, Cisco (IAB)

- **Why**: A standards radar sweep — and for this reader, the standout is one line item rather than the survey itself: **Web Bot Auth**, a group in chartering around *cryptographic identity for bots/agents* as UA- and IP-based signals fail. That is an early standards-body signal on agentic identity, the only one in this entire program.
- **What**: Operator-relevant IETF developments: newly started AI work — aipref (expressing preferences about AI collection/use of content) and Web Bot Auth (likely a WG before the November IETF); AI agents and networking research-group proposals, agent-to-agent lists, AI agent discovery via DNS; DNS work — DELEG (authoritative servers signaling capabilities via SVCB-like records), Domain Connect (DCONN), DNSOP rechartered around split operations and DNSSEC crypto refresh; the green WG on energy-efficiency metrics; and space networking topics.
- **How**: Structured as an area/working-group survey (Routing, Internet, Transport, Ops, Security) with a filter for operator impact.
- **Where applicable**: General context for anyone tracking standards adoption; the Web Bot Auth item is pre-charter/early-charter and worth watching rather than acting on yet.

## Wildcard

### Internet Resiliency Club update

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/55/BCMZQH/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/BCMZQH/resources/IRC_Update_RIPE_91_3iurFhR.pdf) · [Recording](https://ripe91.ripe.net/media/videos/valerie-aurora_internet-resiliency-club-update_main_20251024-112334.mp4)

Valerie Aurora, Bow Shock Systems Consulting

- **Why**: Not a fit for any of the core areas — and exactly why it's a wildcard: a grassroots operator collective building a LoRa/Meshtastic mesh for text communication during power and Internet outages. It's a failure-mode frame (total infrastructure loss) that DC/WAN people rarely practice, assembled by exactly the kind of people who could pull it off.
- **What**: The Amsterdam Internet Resiliency Club (started January 2025) now has ~20 members, monthly in-person meetups, a working private Meshtastic channel, a partnership with Waag Futurelab, €10K received in grants (of €50K applied for), and contact with the city of Amsterdam and the Dutch defense ministry. Key operational lesson: Meshtastic worked great at the WHY hacker camp (high node density) but is unreliable across Amsterdam — the constraint is node density, and the fix is more nodes, i.e., money for hardware.
- **How**: Low-power LoRa radios running Meshtastic in a decentralized mesh; the human layer is Doodle-scheduled meetups, a mailing list, and personal invitations. Hardware recommendations given (solar-powered WisMesh Repeater Mini enclosures, card-shaped trackers, T-Beam home stations; avoid the T-Deck keyboard).
- **Where applicable**: Explicitly replicable — the recipe quoted is 1–2 hours/week, ~€200 of floatable cash, and a large personal network. Amsterdam-density findings will differ by city; the model is aimed at the gap before government disaster-recovery programs arrive (~2028 by their estimate).

### Cyberattack Observation Using IoT Honeypots at Yokohama National University

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/44/QBTJJJ/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/QBTJJJ/resources/RIPE91-XPOT-3_aav6FCr.pdf) · [Recording](https://ripe91.ripe.net/media/videos/takayuki-sasaki_cyberattack-observation-using-iot-honeypots-at-yokohama-national-university_side_20251023-140444.mp4)

Takayuki Sasaki (with Katsunari Yoshioka), Yokohama National University

- **Why**: Not IoT per se — the signal is the *operational pattern*: a hybrid rule-engine-plus-LLM triage pipeline that turns a honeypot into a near-real-time exploit classifier. That AI-assisted-triage design is where security operations tooling is heading, demonstrated on real long-running data with a public dataset release.
- **What**: X-POT, an adaptive HTTP honeypot that emulates a wide range of IoT devices using real WebUI HTML collected by scanning IP ranges around observed attackers — so the honeypot presents genuinely realistic device interfaces. The analysis pipeline: identify attacks (payloads fetching malware via wget/curl), tag against rules, classify novel exploits by request-path/parameter patterns, alert the operator immediately on new exploits, and auto-generate analysis reports with GPT-5 plus web search — sent to Slack, manually verified, then turned into new tagging rules. Long-term operation captured entire exploit lifecycles from emergence to decline, including zero-days and campaigns against industrial targets like solar power monitors.
- **How**: Two components — attack observation (emulation + malware collection) and HTTP response collection (scanning attacker neighborhoods to harvest device WebUIs); the LLM proposes, the human verifies before rules ship.
- **Where applicable**: University research deployment, but the rule+LLM hybrid with human-in-the-loop verification is a pattern any SOC or honeypot operator can adopt today; the public dataset makes the data reusable for collaborative research.

### Network Measurement in the Dark

**Links:** [Abstract](https://ripe91.ripe.net/programme/meeting-plan/sessions/22/DGX8XV/) · [Slides](https://pretalx.ripe.net/media/ripe91/submissions/DGX8XV/resources/2025-10-21-darknetwor_R3K3kvE.pdf) · [Recording](https://ripe91.ripe.net/media/videos/geoff-huston_network-measurement-in-the-dark_main_20251021-160357.mp4)

Geoff Huston, APNIC

- **Why**: The premise underneath every observability investment — that the network can see what traverses it — is being dismantled by protocol design. This is the big-picture frame for why measurement and monitoring assumptions need rethinking, delivered by the person who has been documenting that shift for a decade.
- **What**: A synthesis of ~15 years of change: operators were once the trusted observers of who-talks-to-whom; that trust eroded through ad-tech profiling and state surveillance (the Snowden papers as watershed), and the IETF responded with RFC 7258 declaring pervasive monitoring an attack. The consequences, with adoption data: HTTPS became near-universal; DNS queries moved behind DoH/DoT/DoQ; and the next step — MASQUE with two-layer encryption and relays — hides the endpoints entirely, so no single network observation point ever sees both ends of a transaction plus the content. The implicit question: what is left for network measurement, and what should operators do about it?
- **How**: Narrative argument anchored in public adoption statistics (Cloudflare radar for HTTPS, APNIC's encrypted-DNS measurements).
- **Where applicable**: Universal — it's a framing talk, not a solution talk. Directly relevant to anyone planning traffic measurement, network forensics, capacity planning, or policy enforcement that presumes visibility into flows.

## Themes

- **The softwarized edge has reached carrier scale.** A 1.2 Tbps vBNG on one commodity x86 server and gNMI telemetry running in production at Cloudflare make "vendor appliance vs. software datapath" a genuinely contested decision, with the hard lessons (cache-line alignment, distributed counting) now being shared openly.
- **Physical DC fabric ideas are coming from unexpected directions.** Meta's PON-based management/console fabric — eliminating copper trays entirely — shows residential access optics finding a hyperscale role; simplification of the physical plant is back as a first-order design goal.
- **Routing security is in its second act.** With ROV broadly deployed, the community's attention moved to the residual holes: the IRR/AS-SET blind spot at IXP route servers, ASPA tooling arriving in production UIs, automated compliance auditing for MANRS+, max-prefix misconfiguration risk, and — on the longest horizon — post-quantum migration planning for the RPKI.
- **BGP data analysis lost its barrier to entry.** Between Rotonda (live BMP ingestion with compiled inline scripts), RIS-as-Parquet (SQL over the DFZ), and the BGP Observatory (free stuck-route detection), MRT-parsing scripts and custom parsers are no longer the gating factor for doing your own routing analysis.
- **Interdomain traffic games continue quietly, and regulation is adding new risk.** Six of sixteen Tier-1s rewrite BGP ORIGIN to win traffic; meanwhile court-ordered blocking (Piracy Shield, LaLigaGate) and the EU's Digital Networks Act are creating collateral damage — blocked-and-released IP ranges, peering under regulatory threat — that network engineers now have to treat as an input.
- **Identity for non-human actors surfaced at the standards layer.** Beyond this program's single mention (Web Bot Auth in the IETF talk, alongside AI-preferences and agent-discovery work), there was essentially no FIDO/OAuth/SPIFFE-style identity content at RIPE 91 — a notable gap, and a signal that agentic identity conversations are currently happening in standards bodies more than operator venues.
