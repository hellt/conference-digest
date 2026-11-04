<!--
conference: Peering Days 2026
type: operator
source_url: https://2026.peeringdays.eu/programme/
generated: 2026-11-04
registry_key: peeringdays-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Peering Days 2026

A small operator program (IXP updates, RPKI/routing security, optics, fabric design) with an unusual amount of real technical slide content despite most talks publishing no abstract. Picks below are grounded in the extracted slide text where available; the Krill workshop is the only selected item with nothing but its abstract. No `page:` links existed in the program, so no further enrichment was possible.

## Core

### Technical Workshop: A focus on ROAs and ASPAs, and how to handle them with Krill

Massimiliano Stucchi

- **Why**: RPKI is mainstream; ASPA is the next routing-security primitive and directly addresses the class of route leaks that ROV cannot catch (path leaks) — the same gap the AS-SETs talk in this program quantifies. Hands-on delegated RPKI with Krill is adoptable tooling, not theory.
- **What**: A refresher on RPKI and ROAs, an introduction to ASPAs (what they assert, how to create them, their role in global routing), and the bulk of the session is practical Krill setup for delegated RPKI, including preparing different publication setups. (from abstract only)
- **How**: Workshop format: software setup and publication-architecture walkthroughs. (from abstract only)
- **Where applicable**: Any operator running or considering delegated RPKI; vendor-neutral open-source tooling. The ASPA portion's practical payoff depends on how far ASPA verification has spread among your transits. No slides or paper were in the source material, so depth beyond the abstract is unknown.

### Demystifying Coherent Optics for Network Professionals

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/Salumanus_Marcin_Bala.pdf)

Marcin Bala, Salumanus

- **Why**: Coherent pluggables (100ZR, 400G ZR/ZR+/ZR++, 800G ZR/ZR+) are collapsing the router-to-DWDM boundary and changing DC/WAN interconnect economics — squarely the PM's physical-optics territory. This is a working engineer's guide, not a marketing deck.
- **What**: A market/standards map (OIF 400ZR/800ZR, OpenZR+, CMIS) and a four-step deployment method: link requirements (length, dark fiber vs DWDM, grid, OSNR, throughput) → transceiver selection → matching application to link budget → configuration. Worked examples: a 200 km DWDM link on a 50 GHz grid at 19 dB OSNR served by either QSFP28 100ZR or QSFP-DD OpenZR+ ZR100-OFEC-QPSK; a 21 dB/100 GHz path running ZR300-OFEC-8QAM with 3x100GbE host-side, or ZR++ to keep 400GbE host-side; an 18 dB flex-grid path forcing ZR200-OFEC-QPSK or an 800G module in ZR400-OFEC-QPSK (150 GHz passband). Also covers the 400G-to-100G interconnect case via muxponder (75 GHz spectrum instead of 200 GHz, future-ready for direct 400G optics), and SFF modules emulating QSFP28 LR4/LR1/DWDM2 for CMIS-less legacy gear.
- **How**: Concrete CLI on four platforms — Juniper (`optics-options application mediaid/hostid`, `tx-power`, `wavelength`), Nokia (`optics-profile 400ZR`, `dwdm coherent target-power`, `frequency`), Cisco (`zrp-optics fec oFEC muxponder …`), OcNOS (`qsfp-dd application`, laser grid/fine-tune). Parameter guidance: OSNR ~24 dB for 400G 16QAM vs ~16 dB for 200G QPSK; Q-factor >8 dB good, 6.5–8 monitor, <6.5 failure risk. Common failure modes: mismatched host/media applications between ends, mismatched channel number, ignored optical budget.
- **Where applicable**: Broadly applicable — open OIF/OpenZR+ standards, multi-vendor config. Speaker is an optics vendor CTO, but the content is standards- and config-centric, with deployment mistakes/checklists rather than product claims.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/Flexoptix_Gerhard_Stein.pdf)

Gerhard Stein (with Thomas Weible), Flexoptix

- **Why**: Optics power draw is a real DC cost line at 400G/800G scale, and this is one of the few talks with actual measurements of where transceiver watts go — a topic the PM works on physically and strategically.
- **What**: A measurement study across 100G QSFP28, 400G QSFP-DD coherent ZR, and 800G QSFP-DD transceivers on Cisco Nexus 93600CD-GX, Catalyst C9500, and Juniper QFX5120. Findings: laser and TEC draw is negligible at any transceiver temperature (laser at its ~50 °C target is most efficient, but it barely matters); the real consumers are the MCU/DSP, flagged as the next research step; shutting a port forces low-power mode and cuts transceiver consumption 7–20x; "doubling the speed does not double the Watts." VDM (CMIS calculated metrics) vs DDM support varies sharply by platform — only the Nexus 93600CD-GX with a 400G coherent module reported a real laser temperature (49.98 °C); the QFX5120 and C9500 expose DDM only.
- **How**: VDM reads calculated values from module bytes (e.g., P_laser = V_fwd × I_laser, P_TEC = V_Trc × I_TEC) where DDM gives raw currents; power budget and fan/heat-exchange modeling (Nusselt/Prandtl/Reynolds); measurements taken via a Flexbox-based research tool, including a frozen-transceiver experiment showing laser behavior across a ~20 °C differential.
- **Where applicable**: The port-shutdown power lever and platform-dependent VDM support are broadly useful to any switch operator. Flexoptix is a vendor, but the work is measurement-based and spans three switch vendors' hardware.

### The Scourge of Excessive AS-SETs

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/Jac_Kloots_Kentik.pdf)

Jac Kloots, Kentik

- **Why**: IRR AS-SETs remain the operational backbone of BGP filtering, and this talk quantifies — with real case data — how uncontrolled nesting has made many of them useless as allowlists, then points at the actual fix (ASPA, RFC 9234). Directly relevant to network security and BGP-internals work.
- **What**: An analysis anchored on the March 11, 2024 MTS (AS8359) / HKIX route leak. The leaker's AS-MTU expands to 43,823 ASNs; `bgpq4 -J` produces a ~1.29M-line Junos config (271k lines even with `-A` aggregation) covering 1.8 billion of the ~3 billion routable IPv4 addresses — so any transit filtering on AS-MTU is effectively filtering nothing. The largest AS-SETs (e.g., `AS39533:AS-PEERS`) expand past 100k ASNs, exceeding the ~90k ASNs in the global table, because nested sets pull in unrouted ASNs; 2,192 AS-SETs expand beyond 1,000 ASNs. A traced nesting chain from AS-XUA-UA runs Ukraine → NL-IX → Balkan-IX → TTK → CN2 → South Africa → CTGNet → Rostelecom before landing on an unrouted Russian air-traffic-corporation ASN. Root cause: AS-SETs mix semantically undefined member types (customers, peers, IXP members) with no limits on membership or recursion depth.
- **How**: Recursive IRR expansion mechanics; tools (`bgpq4`, `irrtree`, bgp.tools) as measurement instruments; a key operational gotcha — AS-SET contents differ by source IRR (NTT mirror is bgpq4's default), so authoritative source must be declared, e.g., in PeeringDB. Proposed long-term fix: RFC 9234 BGP role signaling in-band, RPKI ASPA verification, and Signed Prefix Lists, rather than ever-larger self-asserted allowlists.
- **Where applicable**: Every transit operator filtering with IRR data. Speaker is from an observability vendor, but this is data analysis with named collaborators (bgp.tools, Comcast, Cogent, Google, Telia), not a product pitch.

### Securing IXP Fabric

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/Nokia_Alessandro_Bulletti.pdf)

Alessandro Bulletti, Nokia

- **Why**: An IXP fabric is a giant shared L2 exchange LAN, and the hardening techniques here — proxy ARP/ND, BUM policing, duplicate MAC-IP detection — transfer to any shared L2 fabric including DC interconnect. The talk also carries current, concrete DDoS threat numbers.
- **What**: Two parts. First, inherent fabric protection with EVPN Proxy-ARP/ND in three "gated lines of defense": (1) static MAC per customer logical interface + ACL filters blocking unknown multicast/broadcast so only assigned MAC/IPv4/v6 can source traffic into the fabric; (2) ingress policers for BUM and ARP per customer interface, with hardware rate-limiters keeping CPU load controlled; (3) Proxy-ARP/ND with static ARP entries, dynamic proxy ARP with MAC lists, and EVPN MAC-duplication detection — eliminating ARP/ND flooding and enforcing that customers only use assigned addresses. Second, DDoS mitigation at the IXP itself: detection keyed on the peering partner's destination MAC (SPM or IPFIX IE315) on L2 interfaces, with auto-mitigation via IP filters in the fabric rather than rerouting to a scrubbing center. Includes Nokia 2025 threat-intelligence data: attacks over 10/20/40 Tbps recorded within a single month (Sep–Oct 2025); 78% of attacks complete within five minutes (up from 44% in 2024), 37% within two minutes; 52% carpet-bomb multiple hosts; AI-orchestrated vector switching and botnet proxy wars.
- **How**: EVPN proxy-ARP/ND converts flood-and-learn L2 into controlled control-plane learning, with distributed CPU protection so punted ARP is handled in hardware; references DE-CIX's EVPN peering-LAN work and IX.br's SRv6 fabric as real-world precedents.
- **Where applicable**: The fabric-hardening mechanics apply to any EVPN fabric (all major vendors implement proxy-ARP/ND variants); the DDoS-as-a-service portion is Nokia Deepfield-specific and partly a pitch. Take the techniques and the threat statistics, treat the product framing accordingly.

### EVPN - One control plane to rule them all

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/Arista_Patrick_Prangl.pdf)

Patrick Prangl, Arista Networks

- **Why**: Consolidating all L2/L3 VPN service delivery onto one BGP control plane across DC and WAN is exactly the PM's DC/WAN interconnect space, and this maps the RFC landscape, the SR-MPLS→SRv6 migration tiers, and the gateway designs that make it real.
- **What**: The case for EVPN as the single service control plane: EVPN-VPWS (RFC 8214) for E-LINE, EVPN-L2VPN (RFC 7432) for E-LAN, EVPN-L3VPN Type-5 (RFC 9136), and EVPN multicast (RFC 9625 OISM) — replacing LDP/BGP-VPLS, MC-LAG, Draft-Rosen/NG-MVPN, and per-service signaling protocols. Transport strategy: SR-MPLS reusing existing MPLS hardware and BGP control plane (TI-LFA for 50 ms FRR, FlexAlgo for controller-less macro-TE, controller-based micro-TE), with three SRv6 maturity tiers — SR-MPLSv4 (no hardware change), SR-MPLSv6 (IPv6 forwarding plane, possible HW upgrade), SRv6 uSID (likely HW upgrade, new control plane). EVPN gateway design per BESS RFCs/drafts (8365, 9014, `draft-ietf-bess-evpn-ipvpn-interworking`): VXLAN↔MPLS interworking where Type-2/5 routes are re-advertised across domains with re-encapsulation while Type-1/3/4 stay local; gateway next-hop chaining so leaves only learn local next-hops; D-PATH attribute for inter-domain loop prevention. Forward-looking pieces: Unknown MAC Route (MAC=0 + gateway ESI) to bound MAC scale in multi-domain fabrics, and the multicast gateway family (MEG, PEG, EEG).
- **How**: One BGP AFI/SAFI across all service types; gateways translate encapsulation and own inter-domain next-hop re-advertisement, containing control-plane state per domain; D-PATH domain-ID tagging prevents route loops across gateway meshes.
- **Where applicable**: Explicitly covers greenfield build-outs and brownfield MPLS/SR coexistence with interop gateways; transport per use case (VXLAN in DC/campus, MPLS-SR/SRv6 in WAN, VXLAN-over-IPSec for SD-WAN). Arista vendor session, but anchored in IETF standards — the architecture applies to multi-vendor EVPN deployments.

## Adjacent

### 30 Years of Interconnection: Experience from an Italian IXP

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/NAMEX_Maurizio_Goretti.pdf)

Maurizio Goretti, NAMEX

- **Why**: A three-decade operator's view of how regional interconnection actually evolves — good strategic context for anyone whose products ride IXP/edge infrastructure, though light on transferable technique.
- **What**: The Italian IXP landscape (MIX Milan 451 AS / 3.4 Tbps, NAMEX Rome 278 AS / 1.4 Tbps, plus MINAP, TOP-IX, VSIX and a long tail of local exchanges), Rome's role as the content↔access hub for central/southern Italy (the country spans >20 ms), NAMEX's 113 unique local ASNs (40%), why Italian IXPs run their own datacenters (a historical lack of carrier-neutral facilities), not-for-profit economics (>€6M 2025 revenue, fully reinvested), and a Mediterranean alliance with TOP-IX spanning peering, DCs, cloud federation and QKD.
- **How**: Personal retrospective with IXPDB-derived figures.
- **Where applicable**: Italy-specific market observations; the "local / neutral / not-for-profit / community" IXP model argument is general. Mostly context, not technique.

### Get the benefits of a non-profit local/sub-regional IX

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/BIX_Janos_Gergely_Janos_Angeli.pdf)

Janos Gergely & Janos Angeli, BIX

- **Why**: Sold as an IXP promo, but the slides double as a disclosed reference design of a multi-city EVPN peering backbone — the technical content is the reason to read it.
- **What**: BIX Budapest's fabric: VXLAN-based L2 peering LAN over an OSPF L3 underlay with a BGP EVPN control plane (spines as route reflectors), Bird v3 route servers, RPKI + IRRDB prefix filtering. Physical plant: Nokia 7750 SR / 7220 IXR and Arista 7280R nodes, Budapest dark-fiber rings (7–28 km IRU links), three 400G Budapest–Vienna wavelengths (3.4–6.3 ms) and 400G Budapest–Frankfurt wavelengths; the 2026 refresh moves spines to 32x800G-capable Nokia 7220 IXR. Commercial model: free peering up to 2G, MRC-free cross-connects, hybrid ports/PNI/MMR, subspeed ports (1/10G, 40/100G) billed at 95th percentile.
- **How**: Standard EVPN fabric + Bird route servers; a small, fully documented multi-PoP IXP architecture.
- **Where applicable**: BIX-specific (Budapest/Vienna/Frankfurt topology and pricing), but the EVPN-plus-route-server design is broadly reproducible by any small regional exchange or operator building a similar fabric.

### Peering market at a glance

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/NAMEX_Flavio_Luciani.pdf)

Flavio Luciani (with John Souter), NAMEX

- **Why**: An evidence-based counter to the "peering is dying" narrative, useful for interconnect strategy and for anticipating where IXP/edge investment flows next.
- **What**: A synthesis of a multi-region paper (published on RIPE Labs, APNIC, LACNIC, ARIN blogs): peering is structurally transforming, not declining. The misread comes from mature-hub stabilization, lost visibility as traffic moves to PNIs/in-network caching/edge, and hyperscaler selective interconnection (CAIDA port-capacity trends for Meta/Microsoft/Apple/AWS shown). Growth is strongest in emerging markets (Kenya, Nigeria, Philippines, Indonesia, Japan, Mexico, Colombia, Peru). IXP success factors: telecom liberalization, local content and eyeballs, population scale, carrier-neutral DC ecosystems. Forward look: IXPs as strategic infrastructure for resilience and sovereignty, micro-IXPs, and edge/low-latency architectures.
- **How**: CAIDA snapshots, PeeringDB, and IXPDB data compared across regions.
- **Where applicable**: Strategy level — relevant to interconnection planning generally; country specifics vary and the slides are a condensed version of a longer paper worth reading for depth.

### Hardwired for Chaos: The No-Bullsh*t Way to Build Infrastructure That Lasts

Tony O'Sullivan, RETN

- **Why**: By title, a hard-won-lessons talk on building resilient infrastructure from a pan-European transit operator — normally exactly the transferable operational content this program rewards.
- **What**: Cannot be assessed — no abstract and no slides were published; title, speaker, and affiliation only. RETN operates one of Europe's larger long-haul networks, so resilience lessons would likely transfer across environments.
- **Where applicable**: Unknown without materials. Treat this as "watch if a recording appears" rather than a recommendation of known content.

## Wildcard

### Agentic DDoS OPS/AI-Powered Operations Layer for GenieATM

**Links:** [Slides](https://2026.peeringdays.eu/media/documents/Genie_Networks_Siarhei_Matashuk.pdf)

Siarhei Matashuk, Genie Networks

- **Why**: Not optics, not BGP — it's an early, concrete look at how LLM agents get wired into live NOC operations, and the design patterns (git-versioned markdown skills, a hard privacy boundary, an earned-autonomy trust model) generalize far beyond DDoS tooling, including into the identity and authorization questions agentic systems raise for the PM's own portfolio.
- **What**: An agent layer ("DjiNN") on top of GenieATM implementing nine virtual NOC/SOC roles as "skills" — Baseline Analyst (continuous detection-threshold tuning with auto-rollback, replacing set-and-forget thresholds), Traffic Analyst (natural-language queries over a 1M-flow in-memory snapshot, e.g., breakdown of a new uplink by origin ASN/protocol with no query syntax), Peering Coordinator (cross-referencing per-AS traffic against PeeringDB to surface peering ROI, e.g., "40% of traffic to AS 13335 rides transit but they're at AMS-IX where you already peer, est. €2,400/month savings"), plus Incident Responder, Platform SRE, and others clearly staged as MVP vs Phase 2/3. Notably honest limitations: LLM latency handled by rule-based fallback for time-critical detection (the LLM does enrichment, not first-trigger); trust via a maturity model from L0 alert-only to L3 autonomous-with-audit-trail, with all destructive actions human-approved; data privacy via an MCP anonymization layer (IP→`prefix_UUID`, Router→`router_XXX`) so only tokenized data crosses to the LLM provider, with a local-model option for zero exposure.
- **How**: Skills are plain ~30-line .md job descriptions in git — a NOC engineer can read and modify one in five minutes, no SDK; an orchestrator routes tasks → skills → tools → data sources; southbound to GenieATM's Snapshot API/NetFlow plus PeeringDB, RIPE RIS, RouteViews, and threat intel.
- **Where applicable**: The data source is GenieATM-specific and the closing slide recruits for an early-access program (vendor session — discount accordingly), but the skill-file architecture, trust maturity model, and anonymization boundary are platform-agnostic patterns worth borrowing.

## Themes

- **Routing integrity is migrating from IRR self-assertion to signed and in-band signals.** The AS-SETs critique (allowlists that filter nothing), the ASPA workshop, and the RFC 9234 references form one coherent thread: the industry is working its way past IRR as the leak-prevention mechanism.
- **Coherent pluggables are collapsing the router-to-DWDM boundary.** Two optics talks — a coherent-transceiver engineering guide and a transceiver power measurement study — both treat 100ZR/400G/800G pluggables as switch-port config problems now, with real multi-vendor CLI and measured power data.
- **EVPN is the consolidation layer everywhere.** IXP fabrics (Nokia's secure fabric, BIX's backbone) and pan-domain service delivery (Arista) all converge on BGP EVPN as the single control plane, from peering LANs to DCI.
- **Physical-layer power is now an operator concern.** The Flexoptix measurements (DSP, not laser/TEC, is the draw; port shutdown as a 7–20x lever) and Nokia's "sustainable operations" framing both reflect energy arriving as a first-class network design input.
- **Agentic AI is entering operator workflows from both directions.** GenieATM's agent NOC roles and Nokia's AI-vs-AI DDoS narrative bookend the same shift: agents are attacking networks and being proposed to run them — with the trust/privacy boundary design questions that implies.
- **Local and regional interconnection is ascendant.** The Italian IXP retrospective, the BIX sub-regional pitch, and the peering-market paper all argue the same case: growth and strategic relevance (resilience, sovereignty) are shifting from mega-hubs to local and emerging-market ecosystems.
