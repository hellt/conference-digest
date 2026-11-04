<!--
conference: NLNOG Day 2025 (Amsterdam)
type: operator
source_url: https://nlnog.net/events/nlnog-day-2025/
generated: 2026-11-04
registry_key: nlnog-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NLNOG Day 2025 (Amsterdam)

A small, single-track operator program (10 sessions, no published abstracts — all write-ups below are grounded in the extracted slide decks). Nothing here on identity, passkeys, or SPIFFE, and only one session touches cloud-native tooling; the program's center of gravity is classical operator work: optics, BGP visibility, DHCP lifecycle, and automation failure stories.

## Core

### WHY 400G FTTH

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/5_-_Arjan_Koopen_-_WHY_400G_FTTH.pdf) · [Recording](https://youtu.be/6OWZtS_BPv0?si=SKhQ2qgk5pjwclet)

Nicola von Thadden (PFALZKOM), Arjan Koopen (i3D.net)

- **Why**: A rare, fully worked optical engineering case: pushing 400G over a *simplex* (single-strand) fiber 50 km to Amsterdam. Directly exercises the PM's physical-networking interests (coherent optics, DWDM, loss budgets, DC/WAN interconnect) with a problem most DC folk never face — no return strand.
- **What**: The WHY2025 hacker festival built a temporary ISP with its own AS and needed a 400G uplink from the field to Nikhef. The path used a SURF alien-wave (one 100 GHz DWDM channel) to Alkmaar, then rented duplex KPN dark fiber plus a friendly local FTTH provider's fiber — which turned out to be simplex only. The deck documents the history of camp uplinks (HAR2009 10G → SHA2017 100G coherent → MCH2022 200G → WHY2025 400G) and how they solved the simplex problem.
- **How**: The core finding: current coherent optics require RX and TX on the *same* frequency, so a standard 400G ZR transceiver cannot be split across two channels on one strand (initial ADVA tests failed; ADVA confirmed you need different product). Two escape hatches: (1) optical circulators to share one channel — works but adds attenuation/reflection risk; (2) the "cursed idea": use *two separate optics*, one TX-only on channel A and one RX-only on channel B, with active DWDM/OpenZR+ Smartoptics transponders in the middle because they ignore Ethernet link state ("it's a cable"). The DWDM mux doubles as the BiDi mux. The local fiber also surprised them with ~20 dB of loss over 50 km (KPN fiber behaving like 80 km).
- **Where applicable**: Event-specific topology (alien waves, donated strands, temporary AS), but the technique — BiDi over simplex via dual unidirectional optics or circulators, and the coherent-same-frequency constraint — transfers to anyone constrained to single-strand fiber (FTTH plant, leased simplex pairs, some campus runs). Real measured loss figures included.

### Expanding Internet Routing Visibility with BMP

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/10_-_Thomas_Holterbach_-_Expanding_Routing_Internet_Visibility_with_BMP.pdf) · [Recording](https://youtu.be/_gRVy0tTxOY?si=tepRYdbsz4HzrBXL)

Thomas Holterbach (University of Strasbourg), joint work with Thomas Alfroy and Cristel Pelsser

- **Why**: Two of the PM's interests converge here: BGP internals and routing-security visibility. The talk quantifies exactly what standard BGP-based collectors (RIPE RIS, RouteViews) *cannot* see and proposes BMP as the fix.
- **What**: A new next-gen route-collection platform, bgproutes.io, which inverts the priorities of RIS/RouteViews: it prioritizes *coverage* (percentage of ASes sharing data) over historical depth, with perpetual data retention and an open peering policy. Context: only ~1.2% of ASes share data with existing platforms; the new project got ~40 peers in ~1 year. The central technical argument: even when an operator shares data via BGP, inbound/outbound filters and the best-path decision process hide most routes ("BGP route hiding") — denied routes and backup paths are invisible, and Add-path only partially helps (and loses the per-peer mapping). BMP exposes route updates at every stage of the BGP pipeline.
- **How**: BMP sessions export per-peer, per-stage RIBs (`adj_in_pre`, `adj_in_post`, `local_rib`, `adj_out_pre`, `adj_out_post`). Their operational recommendation: export `adj_in_pre` only — one BMP session on a multi-peer router yields data equivalent to dozens of vantage points (their RGNET example: 7 BGP sessions replaced by 2 BMP sessions = 10 VPs). Onboarding is fully automated via PeeringDB login, with an opt-out list for peers you don't want to export. Data access in three forms: MRT archive (bulk), API (slices), websocket (realtime), with Python clients (`pybgproutesmrt`, `pybgproutesapi`, `pybgprouteslive`) that make the collection protocol transparent and also aggregate RIS and PCH data.
- **Where applicable**: Broadly applicable — any operator with BMP-capable routers can peer (MikroTik notably lacks BMP support). The dataset is public and intended to power next-gen BGP monitoring tools; the looking-glass example in the deck is directly reusable. Academic–operator collaboration, not vendor-backed.

### Collecting and analyzing routing information with Rotonda

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/8_-_Luuk_Hendriks_-_Rotonda_-_nlnog2025.pdf) · [Recording](https://youtu.be/B9cEQD5Mad0?si=wm0MvkYB7pR_1KiD)

Luuk Hendriks (NLnet Labs)

- **Why**: BGP/datapath tooling the PM can adopt directly. Rotonda is the open-source engine for exactly what the previous talk argues for: ingesting BMP at scale and making it queryable.
- **What**: NLnet Labs' Rotonda: a routing-data collector and store that ingests BMP, live BGP, MRT dumps, and even RTR feeds; maintains RIBs per peer and per stage (pre/post policy, in/out/local); and exposes everything over an HTTP API. Example queries from the deck: `/api/v1/ribs/ipv4unicast/routes/185.49.140.0/23`, with filters like `filter[ribType]=inPre` (Adj-RIB-In pre-policy), `filter[rovStatus]=valid` (RPKI ROV status), `filter[originAsn]=1133`, `filter[community]=AS1103:9876`, plus `include=moreSpecifics` — all AND-combined.
- **How**: The standout mechanism is **Roto**, a strongly-typed, *compiled* scripting language for filtering route data inside API queries — Roto compiles through Cranelift IR down to native x86_64/ARM64, so user-supplied filter functions run at compiled speed over stored RIBs rather than as interpreted per-route callbacks. Outputs include HTTP/JSON, MQTT, and files; `/metrics` provides Prometheus-style monitoring (the speaker candidly warns some built-in metrics are currently off and being overhauled).
- **Where applicable**: General-purpose operator tooling, open source from NLnet Labs, deployable by anyone running BMP-capable routers — it pairs naturally with bgproutes.io-style collection and with internal route-monitoring/alerting pipelines.

### The Living Source of Truth: Network Automation with Infrahub and Terraform

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/6_-_Marco_Martinez_-_The_Living_Source_of_Truth.pdf) · [Recording](https://youtu.be/8bVhExTWtYY?si=6cW9sfR28fY4zmNg)

Marco Martinez (Swisscom)

- **Why**: Network automation with a cloud-native deployment model — the closest this program comes to the PM's software-networking interests, and a realistic brownfield framing rather than a greenfield demo.
- **What**: A concept talk on a "living source of truth": mutable, real-time synchronization between the SOT and the actual infrastructure, instead of the classic Git/file-based desired state that drifts. The stated pain points are drift, delay, poor visibility, and manual multi-step changes across split domains (technical docs, org requirements, security policies). The stack: Infrahub as the SOT, Terraform to define/aggregate desired state, Infrahub artifacts consumed by **Vidra** (which applies them to a Kubernetes cluster and overwrites manual changes, keeping the cluster congruent with the SOT), and an SDC layer to push device configuration.
- **How**: Pipeline pattern: define desired state → aggregate desired states → create infrastructure from the data source, with each tool doing only what it does best. The deck is mostly screenshots of the Infrahub/Terraform/Vidra flow (thin on numbers), but the brownfield advice is concrete: centralize the data source, start small, fix the most time-consuming issues first, use existing tools. Goal stated as idempotent infrastructure on a reliable data source with transparency and a single pane of glass.
- **Where applicable**: Swisscom-scale enterprise context, but the pattern (SOT → artifacts → GitOps-style enforcement on both K8s and network devices) is broadly adoptable. Caveat: the slides are light on evaluation/results — treat this as an architecture reference, not a validated case study.

### From ISC DHCP to KEA DHCP

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/2_-_Rinse_Kloek_-_ISC_to_KEA_DHCPv0.4.pdf) · [Recording](https://youtu.be/AieM0YUFHIM?si=sWoi4SyNtxS_wrop)

Rinse Kloek (Kloek Internetdiensten)

- **Why**: ISC DHCP went EOL in 2022 — this is a forced migration every remaining ISC shop must make, told with a real 4-year production track record and, crucially, a sharp automation postmortem. IPAM/address-management is a core PM interest and this is one of the best-credentialled migration stories around.
- **What**: Why migrate (EOL, no modern API, reboots needed for changes, no Option-82 lease binding for modem swaps) and what KEA gives you: database-backed leases/hosts/subnets (CSV/PostgreSQL/MySQL), a hooks/plugin mechanism (Flex-ID, RADIUS, legal logging), a REST API with 200+ commands, HA with heartbeat and outage detection, multi-threading, and the Stork dashboard. The Delta Fiber production context: 5 DHCP clusters across ~260 routing areas (~30 servers), IPv4 pools split CGNAT/public/fixed, provisioned via Nautobot + a DHCP manager + Ansible. A notable anti-fragility move: lease times raised from 30 minutes to 24 hours (renew at 12h) — the platform now survives a 12-hour DHCP outage for existing clients and carries lower steady-state load.
- **How**: Migration executed crawl/walk/run/fly — start with the easiest service (VoIP/IPTV) in pre-production, hardest last (Internet IPv4 with its 3 pool types), migrating existing leases for customer friendliness. Monitoring via Grafana (pool usage, DHCP packet anomalies, migration status) and Elasticsearch for deep dives. The postmortem is the highlight: a Friday Nautobot permission change made provisioning receive an *empty* dataset, and at 2:00 AM Saturday it deleted all subnets; monitoring caught it at 4:00, fixed by 10:00. The 12-hour renew timers halved the blast radius. Lessons: separate DB backend + small config is very manageable, KEA stable over 4 years, "modern DHCP is the whole ecosystem, not just the software," and — implicit — automation that consumes a SOT must validate for empty inputs.
- **Where applicable**: ISP/access-network specifics (Option 82, modem swaps, CGNAT pools) are Delta-Fiber-shaped, but the migration methodology, the lease-time resilience argument, and the empty-dataset automation failure are universally transferable. The Flex-ID hook (any DHCP option as client identifier) is the key feature enabling modem swaps that ISC couldn't do.

## Adjacent

### The How and Why of Internet.nl

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/7_-_Sasha_Romijn_-_Internet.nl_-_nlnog-inl.pdf) · [Recording](https://youtu.be/ZEtglnvTSyc?si=mcrT_y92-qUEPDjH)

Sasha Romijn (Reliably Coded)

- **Why**: Internet.nl is the compliance-testing tool that effectively sets the practical bar for IPv6, DNSSEC, RPKI, TLS, and mail authentication across the Dutch internet (and beyond) — 1M tests in 2024 on the public site, 8M total. For a network-security-adjacent PM, it's a fascinating case study in turning fuzzy standards into deterministic, defensible test criteria.
- **What**: A tour of how the test suite decides "good or bad": the normative references (IETF RFC/BCP, CA/Browser Forum, Dutch NCSC, Dutch law on government websites, the Standardisation Forum's comply-or-explain), and the constraint that everything must be testable remotely, quickly, without privileges, without harming the target, and consistently. The deck walks concrete judgment calls — e.g., 3 nameservers where 2 have IPv6 but one is unreachable; NS responding only over TCP; a most-specific route with a ROA while a covering less-specific route has none — and classifies test difficulty: RPKI/DNSSEC/SPF/DMARC easy, HTTPS/headers/DKIM medium, mail TLS genuinely hard (TLS has no way to communicate its config; rate-limited mail servers break tests).
- **How**: Test areas cover IPv6, DNSSEC (full chain, following CNAME), HTTPS (BCP 195, RFC 8996/9325 informed), HTTP security headers + security.txt, DMARC/DKIM/SPF (with the SPF lookup-limit trap, shown via a real `spftrace` of internet.nl), STARTTLS+DANE, RPKI, and CAA. Everything is open source, Docker-deployable, with dashboard/API for certain groups; they cross-check against DNSviz, Zonemaster, SSL Labs, RIPE Atlas, and the NLNOG ring.
- **Where applicable**: Dutch-standards-flavored (some criteria come from Dutch law/policy) but the codebase and methodology are open and self-deployable anywhere. Useful both as a testing tool and as a model for anyone building automated standards-compliance scoring.

### Why would anyone want to run a personal ASN?!

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/4_-_Nick_Bouwhuis_-_Personal_ASN.pdf) · [Recording](https://youtu.be/4DFNQ5vacF8?si=GBdFV42HOQe_VW4k)

Nick Bouwhuis (Speakup), Peter-Paul Kurstjens (Red Hat), Jelle Luteijn

- **Why**: Not a product pitch — a three-person survey of the "personal ASN" ecosystem (1,354 listed on bgp.tools, 61 in the Netherlands), which is quietly a showcase for the modern lightweight BGP stack: Bird2 + KEES automation, NetBox IPAM, RPKI/ASPA, and VPP on Linux. For the PM's datapath-internals interest, one of the three case studies runs VPP as a production router in a VM.
- **What**: Three personal networks at increasing ambition: a content network (AS202585) on MikroTik CRS310 hardware at Nikhef/InterDC with Bird2 automated by KEES; an "enterprise" personal network (AS212855) with two Amsterdam routers, Bird 2.17, RPKI/ASPA, IRR dropped in favor of better sources, and a peering portal; and a genuine personal *carrier* network (AS200132) offering free transit for non-commercial users — Arista 7280SE-64 plus a Dell PowerEdge R640 running Proxmox with VM routers, VPP, Bird, ~160 Gbps capacity, serving a real community (31 of 54 ports occupied, ~4 Gbit traffic, mirrors for CentOS/Fedora/EPEL).
- **How**: Lots of transferable technique despite the hobby framing: VPP as the datapath on RHEL VMs with resource isolation (PCI passthrough, CPU L2 isolation + taskset); a fork of the KEES automation stack (from Coloclue) handling RPKI/IRR/BGP communities; NetBox for IPAM; Ansible + Semaphore for config; LibreNMS/Smokeping/RIPE Atlas/NLNOG ring for monitoring. War stories: reverse-path filter pain, soft-IRQ tuning killing them, no packaged VPP for RHEL (custom work required).
- **Where applicable**: Hobby scale, single-digit gigabits — but the patterns (VPP on commodity Linux, KEES-style Bird automation, small-team BGP ops) are exactly what small cloud/DC operators use, and the "addressing crisis" debate about whether hobby ASNs pollute the DFZ is worth knowing. The VPP-on-RHEL lessons apply to anyone considering Linux-vector dataplane routers.

### Hardwired for Chaos: The No-Bullsh*t Way to Build Infrastructure That Lasts

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/11_-_RETN_NLNOG_Presentation_2025_NOBSTONY.pdf) · [Recording](https://youtu.be/IcnkElly1AY?si=eF6WvOdd-Oe3Y_4T)

Tony O'Sullivan (RETN, CEO)

- **Why**: Physical WAN resilience with three recent, well-known stress tests — 2025 Taiwan subsea cable cuts (two suspected sabotage), the Red Sea cable cuts, and the Ukraine war. For a PM whose remit includes DC/WAN interconnect, this is a carrier's argument for geo/vendor/route diversity in the transport layer.
- **What**: RETN's resilience-first philosophy, backed by case studies: five genuinely diverse, vendor-separated cable paths to Taiwan (stable latency through a 70-day repair window while Tier 1s degraded for weeks/months); the TRANSKZ terrestrial Asia–Europe route absorbing 60–70% of traffic during Red Sea cuts (~70% of EU–Asia subsea capacity lost) at 99.9% uptime; and in Ukraine, a new southern Kyiv route, 72-hour deployable autonomous PoPs with pre-positioned spares, and a capacity-swap deal within a week of the invasion.
- **How**: Three engineering rules: build for risk (geographic, supplier, and infrastructure diversity with automated reroute, MTTR < 6 h); design smart not big (unique routes like a Milan–Zurich bypass, lean team); optimize efficiency (400GbE rollout, vendor energy benchmarking, watts/Gbps). Plus a call to arms: reclaim the meaning of "resilience," stop buying obviously under-engineered services, demand transparency on infrastructure reality vs. marketing maps, and treat 100% SLA promises as fiction.
- **Where applicable**: RETN-scale carrier specifics (their own terrestrial routes, cable investments) — but the diversity rules and the industry-myth critique (Tier 1 fallacy, DWDM-ownership-without-control illusion) are broadly applicable to anyone buying transport. Caveat: it's a CEO keynote with promotional intent; the case studies are real but the numbers are RETN's own, not independently evaluated.

## Wildcard

### SNTPings: Abusing IPv6 for Art

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2025/presentations/3_-_Luc_Haaijer_-_SNTPings.pdf) · [Recording](https://youtu.be/bGg6g9W2CTE?si=2DX7x7EKeR8zDa4T)

Luc Haaijer (Studenten Net Twente)

- **Why**: Not a talk the PM would ever search for — and exactly why it's worth 15 minutes. Under the "art project" framing is serious fast-path dataplane engineering: line-rate packet processing, userspace networking with DPDK, and an accidental distributed load test that saturated a 40G NIC, a stateful firewall, and a university's upstream.
- **What**: A 1920×1080 collaborative pixel canvas (in the spirit of r/place and pixelflut) where each "pixel write" is an ICMPv6 echo to a destination address that *encodes the pixel* — the IPv6 address bits carry X, Y, and BGRA color (`ping6 2001:610:1908:a000:<X>:<Y>:<B><G>:<R><A>`). Over 100 participants; the hardware packet counters wrapped multiple times; sustained rate above 72 Mpps, saturating the 40G NIC, a newly installed stateful Fortinet firewall (which, at least, does support IPv6 — through 1920×1080×color distinct destination IPs), and the upstream infrastructure, prompting a "my Wi-Fi is slow" moment campus-wide.
- **How**: DPDK ingests packets in userspace (kernel bypass, NIC hijacked for line-rate receive); destination-address bits are memcpy'd directly into the frame buffer; OpenCV + Gstreamer encode an x264 live stream (codec-compatibility hell noted: Firefox/Linux ∩ Chrome/Windows = ∅); MediaMTX distributes. Network notes: the workload is pps-limited rather than bandwidth-limited; a 40G external tap with 10G internal, and the university upgraded to 2×100G for headroom. Future work: GPU processing via RDMA, FPGA, multiple servers — plus a P4 tap with BGP.
- **Where applicable**: Campus/event-specific as a project, but the pattern transfers: DPDK userspace receive at tens of Mpps, address-bits-as-payload as a legitimate technique for creative telemetry or encoding, and a vivid reminder that stateful middleboxes are the bottleneck long before the link is.

## Themes

- **BMP is having a moment**: two independent sessions (bgproutes.io and Rotonda) argue that BMP — with its per-peer, pre/post-policy visibility into `adj_rib_in` — is the successor to BGP-session-based route collection, which structurally cannot see filtered or backup routes. Operators should expect BMP-derived datasets and tooling to become the default substrate for routing monitoring and security research.
- **The optics renaissance reaches operator conferences**: 400G coherent over simplex strands (via dual unidirectional optics or circulators), alien waves, DWDM channel planning, and measured loss budgets — a physical-layer skillset reappearing in 2025 programs after years of software-dominated agendas.
- **Automation can kill your network "very gracefully"**: the Delta Fiber postmortem (a permission change yielding an empty dataset that silently deleted all DHCP subnets) is this cycle's canonical lesson — SOT-driven automation needs empty/invalid-input guardrails, and architectural choices (12h renew timers) are what bounded the blast radius.
- **Forced lifecycle migrations are producing the best operational content**: ISC DHCP's EOL turns every KEA migration talk into a transferable playbook (crawl/walk/run staging, lease migration, monitoring during cutover).
- **Resilience rhetoric vs. resilience engineering**: the RETN keynote and the Taiwan/Red Sea cable events are pushing the operator community to demand route/vendor/geo diversity evidence rather than SLA numbers — with terrestrial route diversity (TRANSKZ) proving itself under real cable cuts.
- **Notable gaps for this PM**: zero sessions on identity, passkeys/FIDO, SPIFFE/SPIRE, or agentic identity, and nothing on eBPF/Cilium/service mesh — only the Swisscom talk touches Kubernetes, via GitOps-style artifact enforcement. If those topics matter to the PM's roadmap, this community is not yet discussing them.
