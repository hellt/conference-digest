<!--
conference: SwiNOG #41
type: operator
source_url: https://www.swinog.ch/meetings/swinog41/
generated: 2026-11-04
registry_key: swinog-41
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# SwiNOG #41 — Digest

A compact, operator-heavy program: routing security (ASPA/BMP), physical-layer efficiency (optics power, shared spectrum), EVPN fabric scaling, automation frameworks, and one unusually data-rich talk on agentic AI in network operations. Community/organizational items (CHNUG intro, closing remarks) are omitted as non-technical.

## Core

### EVPN Unleashed: Scaling Multi-Domain Fabrics with EVPN Gateways

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/04/Remi_Locherer-Arista-EVPN_Unleashed_-_Multi-Domain_Fabrics.pdf) · [Recording](https://youtu.be/d2f9ttGe2kk)

Remi Locherer - modus one ag with Arista Networks

- **Why**: Flat EVPN-VXLAN fabrics hit hard scale limits — per-VTEP flood lists, full-mesh EVPN state (MAC/ARP/IP/IMET routes), and state churn across every node on each failure. Anyone running multi-POD or multi-DC EVPN hits this.
- **What**: A walkthrough of the IETF BESS standards for hierarchical EVPN gateways — RFC 9014 (L2 interconnect), draft-ietf-bess-evpn-ipvpn-interworking (L3), plus multi-site and D-PATH drafts — with concrete per-route-type gateway behavior and three GW resiliency/loop-prevention models. Despite the Arista banner, this is a standards-centric deep-dive, not a product pitch.
- **How**: GW nodes scope Type-1/3/4 routes to their domain and re-originate Type-2 and Type-5 routes with the GW as next-hop (RD change optional for Type-2, unchanged for Type-5 in the Arista L3 model). Each GW originates its own Type-3 IMET per stretched bridge-domain, producing hierarchical flood lists: local VTEPs list local peers + GW only. L3 forwarding does VXLAN decap → VRF lookup → re-encap at each GW. Loop prevention differs by resiliency model: MLAG shared-VTEP (routes from peer marked invalid; single MLAG domain per site), anycast VTEP IP (no peer link, no directly attached hosts, up to 16 GWs), all-active I-ESI (routes stay valid, so D-PATH/Site-of-Origin policy is required).
- **Where applicable**: Multi-site/multi-POD EVPN-VXLAN datacenters and DCI over VXLAN/MPLS/SR WANs. The standards (RFC 9014, BESS drafts) are vendor-agnostic; the implementation details shown (e.g., `domain remote` peering config, RD/RT handling) are Arista-specific and should be re-checked against your vendor's gateway implementation.

### Understanding and optimising transceiver power consumption using internal metrics

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/03/Flexoptix_Transceiver_improved_power_savings_SWINOG41-3.pdf) · [Recording](https://youtu.be/whrtvO4Z01M)

Gerhard Stein - Flexoptix GmbH

- **Why**: Optics power is a growing slice of DC energy budgets, and the common assumptions (laser temperature tuning matters, TEC is a big draw) turn out to be wrong. This talk replaces folklore with measurements.
- **What**: A measurement study of >100G transceivers (100G QSFP28, 400G coherent ZR, 800G QSFP-DD) in Cisco Nexus 93600CD-GX, C9500, and Juniper QFX5120, using Versatile Diagnostics Monitoring (VDM/CMIS) internals. Headline findings: laser and TEC power draw is negligible at any transceiver temperature (the 50 °C laser target makes no efficiency difference; a ~20 °C ambient delta moves only ~200 mW); the real energy consumers are the DSP/MCU. The single biggest lever is administrative: shutting a port forces the transceiver into low-power mode at **7–20× less** energy. Also documents real power-per-speed trends (400G FR4 from 12 W → 9 W via DSP node shrink 16→7 nm; 1.6T OSFP 30 → 26 W).
- **How**: Read VDM metrics (TEC current, laser temperature) alongside DDM; compute P_laser = V_fwd × I_laser and P_TEC = V_trc × I_TEC; measure per-state transceiver draw with a Flexbox research tool (their pytest/PyQt/matplotlib prototype); a "frozen transceiver" experiment with ice cubes validated the temperature insensitivity.
- **Where applicable**: Any operator with >100G optics. Practically constrained: VDM support is patchy — Juniper QFX5120 (JunOS 25.2R1.9) and Cisco C9500 (IOS XE 17.14.1) expose DDM only; the Nexus 93600CD-GX (NX-OS 10.5.3(f)) supports CMIS VDM. Flexoptix is a vendor and the Flexbox is theirs, but the talk's findings (port shutdown as the dominant lever, DSP as the consumer) transfer to any environment.

### Shared Spectrum & MOFN

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/04/Liam_Taylor-EXA-Shared_Spectrum_and_MOFN.pdf) · [Recording](https://youtu.be/c9LmnTkqkag)

Liam Taylor - EXA Infrastructure

- **Why**: The gap between buying individual wavelengths (low bandwidth, high cost/Gbit) and building your own DWDM line system (high complexity, staffing, licensing) is exactly where inter-DC and long-haul capacity buyers are stuck. Spectrum products are the current answer.
- **What**: A taxonomy of photonic-layer sharing models with their operational trade-offs: **Alien Waves** (customer transponders directly on the vendor's mux — cheapest, but limited monitoring, fixed transmission modes, one cross-connect per wave), **Managed Spectrum** (customer-owned WSS add/drop, vendor-assigned channels — advanced monitoring, power policing, privacy, but changes need negotiation and require customer line-terminal equipment), and **Unmanaged Spectrum** (a spectral block assigned by the vendor, channels fully customer-managed — maximum flexibility, but demands the most expertise). Plus MOFN (Managed Optical Fiber Network): a provider-built dedicated fiber + DWDM system delivered as a managed service. Spectrum sizing depends on distance, fiber quality, ROADM count, amplification (Raman vs EDFA), and transponder generation (e.g., Nokia ICE6).
- **How**: The vendor assigns and polices GHz-wide spectrum blocks in its photonic layer; the customer brings transponders and manages the optical/electrical layers above them.
- **Where applicable**: Operators scaling WAN/inter-DC capacity without building their own line system; terrestrial and submarine (subsea may require ASE fill). Note this is an EXA Infrastructure talk and is largely a product-landscape explainer rather than a neutral engineering treatment — useful for the model taxonomy and the acceptance-criteria/change-process checklist it implies, not as vendor-independent advice.

### bgproutes.io: A next-gen BGP data collection platform

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/04/Thomas_Holterbach-University_of_Strasbourg-next-gen_BGP_data_collection.pdf) · [Recording](https://youtu.be/_OgWAjyxDGU)

Thomas Holterbach - University of Strasbourg

- **Why**: RIPE RIS and RouteViews only see best-path, post-filter BGP — the "top of the iceberg." Route leaks, hijacks, and zombie routes often live in the invisible majority of routes. This platform attacks exactly that, and every operator can feed it.
- **What**: bgproutes.io, a next-gen collection platform launched ~1.5 years before the talk. Direct contributions from ~100 networks, plus aggregation of RIS, RouteViews, PCH, and CGTF data into a single database covering **>5,000 vantage points** (111 in Switzerland alone). It runs **~39 BMP sessions with 19 networks** — BMP exports all route updates from every peer at every stage of the BGP decision process, *including pre-filter*, which even BGP Add-Path cannot do (one network, Edge-connect AS328365, exports everything it receives from 465 peers). Every collected route is annotated with RPKI ROV and ASPA validation status at receipt time. A public API (endpoints: vantage_points, updates, rib, topology) and Python client replace the pain of intermingled 1000+-file MRT archives; users can filter updates by ROV/ASPA status. Current ASPA reality check from their data: 99.3% of downstream paths are Unknown, with fewer than 1,000 ASPA objects existing (Feb 2026).
- **How**: Automated peering establishment (authenticate via PeeringDB, fill a form, start feeding); central aggregation of all existing collectors; BMP where operators can provide it. Perpetual data retention is a priority alongside coverage, where RIS/RouteViews deprioritize it.
- **Where applicable**: Broadly applicable — routing monitoring, hijack/leak detection, research. Any ASN can contribute a BGP or BMP session; BMP contribution multiplies visibility per session. Not a deployment dependency, purely a monitoring/analysis win.

### An Introduction to ASPA – Validating AS-Paths with the help of RPKI

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/04/Max_Stucchi-SwiNOG-An_Introduction_to_ASPA.pdf) · [Recording](https://youtu.be/MmxbGUU8U1Q)

Max Stucchi - SwiNOG

- **Why**: ROAs validate only the origin AS; path manipulation and hijacks above the origin remain invisible. BGPSec is standardized but has no full implementations ("the future"). ASPA is the path-validation building block that is actually becoming deployable *now* — this is routing security's current frontier, and the talk is an honest adoption-stage briefing.
- **What**: ASPA (Autonomous System Provider Authorisation): a signed RPKI object listing an ASN's authorized upstreams. Still IETF draft, expected to become RFCs soon; creatable today on RIPE NCC, ARIN, and APNIC (end of Q2 2026) hosted RPKI and via Krill for delegated setups; served via RPKI-RTR v2 (RFC8210-bis draft). Path validation available in BIRD and OpenBGPd (Cisco IOS-XR in testing; Arista expected end of June); Routinator and rpki-client support ASPA objects. AS0 attestation marks "no upstream" (for Tier 1s, IXP route servers, route collectors). Validation fails open by design — absence of an ASPA means "No Attestation," not invalid. Also rounds up the wider object set (BGPSec, RPKI Signed Checklists).
- **How**: ASPAs build a provider-authorization graph; validators check each AS-pair for "Not Provider" relationships. A clean path shows no violations; hijacks and route leaks (valleys) surface as Not Provider hits. Tools to start: an online ASPA path viewer (oskar456.github.io/aspa.html) and BGPalerter for monitoring your own announcements. Recommended rollout: create ROAs and ASPAs, run at least two relying parties, and **log before you filter**.
- **Where applicable**: Any BGP-speaking operator — a general technique, no scale dependency. The constraint is adoption: with <1,000 ASPA objects worldwide, validation coverage is still sparse, so this is early-adopter territory for the next year or two.

### SCION Inter-Domain Routing

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/04/Tilmann_Zaschke-ETH_Zurich-SCION_Inter-Domain_Routing.pdf) · [Recording](https://youtu.be/_xg5LNhLeZE)

Tilmann Zäschke - ETH Zürich

- **Why**: SCION has crossed from research architecture to regulated critical-infrastructure deployments (Swiss banking, payments, healthcare, power). For anyone whose remit covers inter-domain security and next-gen network identity/trust, this is the most concrete clean-slate architecture actually in production.
- **What**: A 2026 status briefing by the ETH group. Trust model: Isolation Domains (ISDs) — groups of ASes with self-governed trust roots and no third-party CAs, ASes authenticated via X.509 certificates. Path-awareness: endpoints build end-to-end paths from beaconed segments and select among them (latency, bandwidth, geolocation — enabling geofencing and hijack prevention), with failover in ~RTT and concurrent multi-path use. Real deployments: SSFN (Secure Swiss Finance Network, ~300 finance institutions, governed by Swiss National Bank and SIX), SEPN (EFTPOS payments), HIN (healthcare), SSUN (planned all Swiss electricity market partners by 2030), SCIERA (research/education). Public network: 242 registered ASes, 98 publicly reachable, median 204 paths per destination (max 5,828); fastest path median 4 hops / 4.1 ms. Specs: data plane and control plane drafts are with the RFC editor (independent submission stream); reference implementation v0.15.0 adds NAT support; native SCION endhost apps expected to bring 100k+ native users by end of year; client libraries in Go, Rust, C, Java, Python, plus a Chromium plugin.
- **How**: Control plane: beacon service propagates path segments, path servers store them, certificate service manages inter-AS keys. Data plane: packets carry the end-to-end path; border routers forward per-path. Deployment needs no changes to intra-AS infrastructure; legacy endpoints attach via SCION gateways (SIGs) translating IP ↔ SCION.
- **Where applicable**: Inter-AS/critical-infrastructure connectivity — multi-ISP L2/L3 services with enforceable governance and path control. Not a DC fabric or general-Internet technology yet; the deployment footprint is heavily Swiss/European, and the ecosystem is still anchored on ETH tooling and Anapaya as the commercial vendor.

## Adjacent

### Rethinking Network Strategy & Building Resilience Through PNIs, Peering and Smart Geographical Expansion

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/03/Rethinking-Network-Strategy-Building-Resilience.pdf)

Wouter Van Renterghem - RETN GmbH

- **Why**: A carrier candidly decomposing how real incidents — the 2024/2025 Red Sea subsea cuts, Taiwan's 2025 cable cuts, and the Ukraine invasion — reshaped its network design. The failure stories are genuinely transferable; the technical detail is thinner.
- **What**: RETN (self-described 11th-largest IP network) frames a "resilience-first philosophy" through incident case studies: Red Sea 2024 — ~70% EU–Asia subsea capacity loss, RETN moved 60–70% of traffic to the TRANSKZ terrestrial route within the 70-day repair window and held 99.9% uptime while Tier 1s degraded for weeks; Taiwan 2025 — repairs stalled for weeks-to-months; Ukraine — a capacity-swap deal within a week of the invasion, 72-hour deployable autonomous PoPs with pre-positioned spares, and a new southern Kyiv bypass route. Distilled rules: build for risk (geographic/supplier/infrastructure diversity, automated reroute, MTTR < 6 hours), design smart not big (unique routes, lean team), optimize efficiency (400GbE rollout, watts/Gbps benchmarking) — plus procurement-side rules (stop buying visibly under-engineered services, demand transparency, educate customers on their Plan B).
- **How**: Architectural and organizational principles — diversity, in-house engineering, controlled supply chain, multi-vendor strategy — rather than specific protocols.
- **Where applicable**: Long-haul international carriers and anyone buying WAN transport with resilience SLAs. RETN-specific scale and topology; take it as design posture and procurement checklist, not as a technique you can deploy. The slide deck is strategy-heavy (titled "6 stages of network de-sh*tification") and light on engineering specifics.

### 25 Years of SwissIX – A Quarter Century of Peering in Switzerland

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/03/20260428_SwissIX_SwiNOG41_V1.01.pdf) · [Recording](https://youtu.be/EDQPZvfBxvk)

Arist Volger - SwissIX

- **Why**: Beyond the retrospective, this doubles as the SwissIX operational update, and the IXP industry trends it names (big flows moving to PNIs, cross-connects as a hot topic, rising expectations of free ports, IX bandwidth growth slowing) are directly relevant to DC interconnect and peering strategy anywhere.
- **What**: SwissIX crossed the 1 Tbps peak mark (Terabit Club member #77), serving >240 peers across 8 PoPs. Recent and planned changes: backbone upgraded to 400 Gbps (enabling retirement of the end-of-life "Groove" platform), 400G ports now available at ColoZueri, Digital Realty ZUR1, and Equinix ZH4 (second maintenance window in June), a new PoP at CERN Geneva (initially an aggregation switch, to be upgraded to a Nokia 7750-2s like the other PoPs), and secured expansion space at Equinix ZH4. Organizationally: a lean model of 5 volunteer board members, 1 FTE peering development manager, and outsourced 24x7 operations. Pricing: 100G port prices cut from HY2 2026, free upgrades for the rest of 2026, no OTCs for new ports >1G for new peers.
- **How**: N/A — an operational and organizational update, not a technique.
- **Where applicable**: Swiss-market-specific details, but the structural trends (PNI offload of large flows, free-port expectations, outsourced IXP ops) generalize to similar national IXPs (their comparison set: BCIX, BIX.hu, LU-CIX, NAMEX, VIX.at).

### The Network Automation Map: Navigate Your Journey with the NAF Automation Framework

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/05/Damien_Garros-OpsMill-Network_Automation_Map_and_NAF_Framework.pdf) · [Recording](https://youtu.be/WpTHsS_HWbY)

Damien Garros - OpsMill

- **Why**: Most automation programs stall in ad-hoc scripts and tool-specific arguments. NAF offers a tool-agnostic shared vocabulary that teams can use to assess maturity and compare architectures — useful regardless of your stack.
- **What**: The Network Automation Forum framework: seven functional building blocks — **Intent, Collector, Observability, Executor, Orchestrator, Presentation, Infrastructure** — each defined by purpose, MUST/SHOULD/MAY capabilities, and boundaries. Explicitly not a standard or reference architecture; a living community document. Tools map to multiple blocks and blocks to multiple tools (e.g., Infrahub = Intent + Presentation; SuzieQ/Kentik each span Collector → Observability → Presentation). A worked example rolls a new subnet out to 50 mixed-vendor NETCONF branches across 8 tools, including an automated drift-detect-and-remediate loop (Observability → Orchestrator → Executor → Collector → Observability).
- **How**: Functional decomposition first, tools second; each block has clear inputs/outputs so responsibility boundaries and tool gaps become visible. Backed by community docs on GitHub and a solution-wizard app.
- **Where applicable**: Any network automation program, any vendor mix — that is the point. No requirement to implement all blocks; start from your use case.

### Building a Vendor-Agnostic E2E Testing Ecosystem with Netlab

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/05/zebbra_SwiNOG_20260428_v1.3_PDF.pdf) · [Recording](https://youtu.be/tK5VOWVgw4M)

Leandro Lerena & Andy Griesbeck - Zebbra AG

- **Why**: "Automation fails in surprising ways the moment it hits production" — this is one of the more rigorous public answers: make network automation testable like software, with real CI-runnable tests against virtual topologies.
- **What**: Two coupled contributions. (1) A **transactional workflow model**: workflows move through NEW → VALID → SCHEDULED → LOCKING → RUNNING → COMPLETED / FAILED_SAFE / FAILED_UNSAFE, with a locking phase that derives and exclusively locks context to prevent the race conditions that silently drop concurrent config changes (their interleaving example shows actor A's port change lost under non-atomic updates). Function blocks are marked pure / idempotent / rollback-aware, letting the orchestrator retry safely and distinguish clean failures from ones needing manual review. (2) A **Remote Lab service**: a FastAPI orchestrator that provisions netlab/Containerlab topologies on the fly; pytest decorators (`@fb_test_case`, `@fb_test_case_with_lab`) make a full virtual fixture (Cisco IOL, Nokia SR Linux, FRR) one line of test code. Vendor-agnosticism comes from a capability-contract pattern — one `AdminStateCapability` interface, per-vendor plugins (Scrapli for IOL, Netmiko for SR Linux), zero vendor logic in the function block. Developer preview at github.com/zebbra/neops-remote-lab.
- **How**: Typed function-block SDK + capability interfaces + pytest fixtures wrapping netlab `topology.yaml`; teardown guarantees zero residual state so CI and multiple engineers can share one lab.
- **Where applicable**: Any team doing network automation with virtualizable platforms. Coverage is bounded by which vendors have plugins (IOL, SR Linux, FRR shown); the transactional model itself is stack-independent.

## Wildcard

### Toward Agentic Network Operations: What AI Can (and Can’t) Do

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/04/Tobias_Buhler-NetFabric-Agentic_Network_Ops_-_What_AI_Can_and_Cant_Do.pdf) · [Recording](https://youtu.be/lFyXsezhDW8)

Tobias Bühler - netfabric.ai

- **Why**: Not one of your four core areas, but if agentic identity is on your radar, this is the ops-side mirror: a fact-driven talk (by an ETH Vanbever-group PhD, now NetFabric CTO) with real numbers on where agentic AI in networking actually stands — including the failure modes and the cost math most talks omit.
- **What**: An honest positioning: most operators sit between awareness and experimentation; production use is blocked by hallucinations, privacy, unstable results, and cost. The concrete worked example is syslog: a ~100-device network produces millions of log lines/day; naive LLM ingestion costs ~$500k/year (100 tokens/log, 5M logs/day, $3/1M tokens) and overflows any context window. Their key mechanism: **LL-generated parsers** that compress 69M raw log lines into ~700 typed event types — and their deployment data shows new event types keep appearing even after a month (OS upgrades, maintenance days), so parser generation must be continuous. Documented pitfalls: overly specific parsers, overly general parsers, missing domain knowledge. Five enablers that measurably improved performance: in-context learning with clustering-selected diverse examples, injecting expert parsers for known parameters (e.g., MAC-address formats), guardrails/error checks, targeted system prompts, dedicated log-prefix handling. On agentic data access, a clean control-vs-flexibility framing: agent-written SQL queries (expressive, unsafe) vs targeted tool calls (safe, limited) — recommendation is to choose per LLM model, not one-size-fits-all.
- **How**: Log abstraction layer first (parsers → events), then LLM reasoning over events rather than raw logs; the agent interacts with structured stores via either SQL or curated tool interfaces.
- **Where applicable**: Brownfield multi-vendor environments; the numbers come from NetFabric's own deployments (vendor talk, but unusually candid about limitations). The parser-generation pattern itself — LLM + clustering + human correction — is directly stealable for any log-heavy system, networking or not.

## Themes

- **Routing security's next act is path validation.** ROV is settled; the program collectively moves up the stack: ASPA objects now creatable on most RIR hosted RPKI with validator support in BIRD/OpenBGPd, bgproutes.io annotating every collected route with ROV *and* ASPA status, BGPSec acknowledged as still having no full implementation, and SCION going further with cryptographically authenticated path selection. ASPA's fail-open design means adoption can start now (log, don't filter).
- **The photonic layer is where cost and scale are being fought.** 400G is becoming table stakes (SwissIX backbone and ports, RETN rollout), spectrum-sharing products are formalizing the space between wavelengths and dark fiber, and the optics-energy work shows the DSP — not laser/TEC tuning — is the real consumer, with port shutdown as the dominant power lever.
- **Monitoring visibility is being rebuilt on BMP.** Best-path-only collection throws away most of the routing table's information; BMP exposes pre-filter routes from every peer, changing what route-leak and hijack analysis can even see.
- **Network automation is consolidating around shared models and CI-grade testing.** NAF's functional building blocks give the field a common lexicon; the Zebbra talk pairs it with transactional workflows and netlab/Containerlab test fixtures — the same maturity software engineering went through.
- **AI is entering ops through abstraction, not magic.** The one AI talk stands out for honest numbers — $500k/yr naive token costs, 69M logs → 700 event types, failure taxonomy — which is exactly the shape agentic-infrastructure work will take as it meets your identity workloads.
- **Resilience-first is being driven by physical-world events.** Sabotage-suspected subsea cuts, cable-repair timelines measured in months, and war-driven rerouting are pushing diversity, multi-vendor, and MTTR targets from slide-ware into procurement rules.
