<!--
conference: NZNOG 2025
type: operator
source_url: https://www.nznog.org/conferences/nznog-2025/talks.html
generated: 2026-11-05
registry_key: nznog-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NZNOG 2025

NZNOG's operator program skews toward access networks, DNS, and NZ-specific infrastructure, but several sessions land squarely on physical datacenter optics, AI fabric interconnect, timing/sync transport, and operational security postmortems. None of the items below had fuller source text available, so every write-up is grounded in the program abstract only.

## Core

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations

Thomas Weible (Flexoptix)

- **Why**: Directly on the PM's physical-optics beat. As 800G and coherent-lite pluggables move from WAN long-haul into DC interconnect and even intra-fabric links, operators need to know how close to the SNR cliff a link can run and still stay within BER targets — and how temperature and cable length shift that cliff. This is the reliability data that informs margining decisions for 100G/400G/800G deployments.
- **What**: A measurement-driven analysis of how much SNR headroom coherent (16QAM) versus non-coherent (PAM4) transceivers need to sustain a tolerable BER, factoring in environmental variation (temperature, cable length) to predict how long a link stays reliable. (from abstract only)
- **How**: Data collected via Flexoptix's Flexbox programmable transceiver platform, comparing error behavior of coherent 16QAM and PAM4 optics across the SNR range and environmental conditions, with implications drawn for network performance.
- **Where applicable**: Broadly applicable to anyone buying or margining high-speed optics, but note the data comes from the vendor's own Flexbox tooling — the framing favors Flexoptix's ecosystem. The coherent-vs-PAM4 comparison itself transfers to any 400G/800G link budget decision.

### AI Networking, UltraEthernet, the road to 1.6T and beyond.

Matthew Thurbon (Arista)

- **Why**: Sits at the intersection of the PM's core interests: AI/HPC fabrics, lossless Ethernet design, next-generation optics (LPO), and the 800G→1.6T speed roadmap. UltraEthernet Consortium (UEC) is the emerging open-standards answer to InfiniBand for AI clusters — worth tracking for anyone in DC fabric work, since UEC's latency/lossless/reliability semantics will shape merchant Ethernet for AI back-end networks regardless of vendor.
- **What**: A survey of the design requirements AI applications impose on networks (bandwidth, scale, latency, energy), how UEC's open-standards approach addresses them, and the optics roadmap — specifically standards-based LPO transceivers and 800GbE/1.6TbE — that enables next-gen AI interconnect. (from abstract only)
- **How**: Architectural walkthrough of AI fabric requirements and the UEC transport specification direction, paired with the optical layer: LPO as a power/cost-reduced alternative to full DSP pluggables, and the 800G/1.6T port speeds those enable.
- **Where applicable**: Datacenter and AI/HPC fabric design generally. Vendor-presented (Arista), so expect the framing to favor Ethernet/merchant-silicon answers over InfiniBand, but the UEC and LPO content is standards-level and broadly relevant.

### Implementing Precision Timing / Sync as a Service in a Telecommunications Network

Phil Carlisle (Chorus)

- **Why**: Timing distribution is physical-network infrastructure: PTP (IEEE1588v2) and SyncE over terrestrial transport is both a hard operational problem (asymmetry, wander, hop budget) and a growing service as GNSS jamming/spoofing makes antenna-per-site architectures risky. Relevant to anyone building or consuming time-sensitive transport — including sync-sensitive DC fabrics — and a good case study in hardening a WAN service against GNSS vulnerability.
- **What**: Chorus's investigation and lab/customer trials of delivering precision timing as a network service over its own transport using IEEE1588v2 and SyncE, instead of deploying GNSS receivers at every consumer site, and what rolling that out across the Chorus network implies. (from abstract only)
- **How**: Terrestrial time transfer over existing fiber transport (PTP with SyncE frequency assist), replacing per-site GNSS clocks — motivated by both deployment cost (clock + antenna + cabling per site at scale) and GNSS's vulnerability to jamming, spoofing, and space weather.
- **Where applicable**: The trial findings are Chorus/topology-specific (NZ access network), but the pattern — PTP-as-a-service over operator transport to eliminate fragile distributed GNSS — transfers to any operator or large campus/DC environment with sync consumers (mobile, power, finance).

### DNSSEC for .nz: post-incident recovery and improvement (or, how to see the train coming down the tunnel next time. For Sure.)

Paul Radford (InternetNZ)

- **Why**: A concrete, transferable postmortem in network security: the failure wasn't the zone data being internally consistent, it was that nobody validated how the zone behaves against *caching recursive resolvers* in the real world. The lesson — your correctness checks must model the consumer's cache, not just your own output — generalizes far beyond DNSSEC to any system validated in isolation from its consumers.
- **What**: The story of the .nz DNSSEC incident, what observability gaps it exposed, and the "fake root" validation system InternetNZ built afterward: a test harness with caching recursive resolvers in the loop that validates zone outputs against real-world query/validation behavior before publication. (from abstract only)
- **How**: Pre-release validation that replays the resolver ecosystem — not just checking zone files for internal consistency but exercising DNSSEC validation through caching recursive servers in scenarios approximating production, catching negative side effects before the zone ships.
- **Where applicable**: Broadly applicable to any DNS operator (TLD, enterprise authoritative, or hosted zones); the harness approach is adoptable by anyone running authoritative DNS with DNSSEC. Org-specific only in the incident details.

## Adjacent

### DNS Resolvers and Nameservers in New Zealand

Geoff Huston (APNIC)

- **Why**: Rigorous measurement of how resolvers actually pick and re-evaluate authoritative servers, and whether popular domains' NS provisioning matches that behavior — directly useful for anyone reasoning about DNS performance, anycast placement, or NS-set design in production.
- **What**: An extension of prior resolver-behavior and RIPE-Atlas studies using APNIC's distributed ad system to observe the authoritative-server selection process from millions of real end-users worldwide, then checking how two name sets — the root-zone TLDs and the .nz domains in the Tranco top 1M — are provisioned against observed resolver behavior. (from abstract only)
- **How**: Recruits end-users via APNIC's ad-based measurement network (much larger vantage point base than Atlas probes), instruments their resolvers' selection process for a controlled domain set, and compares the observed selection dynamics against the NS configuration of high-traffic zones.
- **Where applicable**: General measurement results, applicable to any operator thinking about authoritative DNS placement; the .nz/Tranco slice gives it a local angle.

### Communications Resilience

Jon Brewer (Telco2)

- **Why**: Physical-infrastructure risk modeling is squarely in the "running networks" skillset: knowing that your fiber routes share a road, a transformer, or a liquefaction zone is the difference between claimed and actual redundancy. This is a practical methodology talk for infrastructure dependency mapping.
- **What**: An approach to mapping telecom infrastructure to identify vulnerabilities and assess risk: data collection and maintenance strategies, dependency mapping (shared power transformers, single-road access routes), and visualization of natural hazards (fault lines, liquefaction zones, landslide-prone areas). (from abstract only)
- **How**: Correlate asset location data with shared-dependency and geohazard datasets, visualize overlap, and use the resulting map to drive risk assessment and hardening priorities.
- **Where applicable**: Methodology is broadly applicable to any operator or large enterprise with physical plant; the hazard layers shown are NZ-specific (fault/liquefaction data), but the technique transfers anywhere geohazard data exists.

### IP Quirks and Features

Mark Smith

- **Why**: For a PM whose interests include protocol internals, this is the "why is IP the way it is" talk — the historical design decisions (ARP's late arrival, IPv4 addressing complexity, why IPv6 grew to 128 bits) that explain today's protocol behavior and deployment friction. Context that makes IPv6 and datapath design decisions more legible.
- **What**: A historical tour of IP feature evolution from the 1974 Cerf/Kahn paper through the multi-protocol 1990s (IPX, AppleTalk) to IPv6, framed around design goals and why the protocols became more complicated than their designers intended, with IPv6's design and deployment model as the through-line. (from abstract only)
- **How**: Historical analysis rather than new research — the speaker's long IETF IPv6 working-group involvement and multi-protocol-era operating experience used to explain design decisions and their operational consequences.
- **Where applicable**: Educational/contextual rather than a technique to adopt; useful background for anyone operating or designing IP networks, especially around IPv6 deployment strategy.

### Chorus is going boost fibre plans for over 700,000 Kiwi homes – find out how we will technically deliver the upgrade and how you can get the best performance out of Chorus' services 😮‍💨

Brent Marquis (Chorus)

- **Why**: A mass-change automation story: re-homing 700k+ live services to new speed tiers without customer impact, across a web of interlocking systems. The decoupling and migration-scripting techniques are what make it worth the PM's time, independent of the access-network specifics.
- **What**: How Chorus will apply wholesale plan speed upgrades (50/10→100/20, 300/100→500/100 from June 2025) across its network without impacting live services, including how the network configuration enables the change, the process/scripts used for the service migration, and how RSPs and customers can extract best performance. (from abstract only)
- **How**: Decoupling the network change from the surrounding in-flight work and systems interactions, using scripted service migration over a network configuration designed to tolerate live modification.
- **Where applicable**: Org-specific in its details (Chorus's GPON wholesale systems), but the pattern — decouple, script, migrate at scale without customer-visible impact — transfers to any operator running mass service modifications.

### KINDNS: Promoting DNS Security Best Practices

Champika Wijayatunga (ICANN)

- **Why**: Security-hygiene framework for DNS operators of all sizes; useful as a checklist and as a signal of what the DNS ecosystem considers baseline defenses. Lightweight on novelty but practical for anyone running authoritative or recursive infrastructure.
- **What**: ICANN's KINDNS framework — a curated set of simple, straightforward operational security measures that DNS operators of any size can implement, aimed at closing the patchwork of uneven security levels across the DNS ecosystem that attackers exploit. (from abstract only)
- **How**: Norm-setting via a published best-practice framework: identify the highest-impact security measures (the ones smaller operators struggle to track and larger operators selectively skip) and package them for adoption.
- **Where applicable**: Broadly applicable to any DNS operator; not a technical innovation but a gap-closing checklist.

### Passive Optical Networking

Daniel Hutchins (Ciena)

- **Why**: Marginal for the PM, but PON's evolution beyond 10G (25G/50G time- and wavelength-domain options) is the access-side bookend of the optics roadmap they track — the same traffic-growth forces pushing 800G in the DC push higher split ratios and rates at the edge.
- **What**: A recap of PON fundamentals, where standards and deployments stand today, and how PON evolves beyond 10G to support higher speeds and increasing traffic demands. (from abstract only)
- **How**: Standards/deployment survey of next-generation PON options and their capacity implications.
- **Where applicable**: Access/broadband networks; vendor-presented (Ciena), and pitched as a recap-plus-roadmap, so treat the evolution claims with the usual vendor filter. Skippable if your remit doesn't touch access networks.

## Wildcard

### Challenges in simulating LEO satellite networks like Starlink

Wayne Reiher (UoA)

- **Why**: Not the PM's domain, but a genuinely interesting emulation technique: reproducing LEO's time-varying latency, load, and handover dynamics on real physical hardware at ~150 devices — a problem most people solve badly in software simulators. The approach (continuously driving netem and token-bucket parameters from an orbital model) is a reusable pattern for testing any time-varying transport path, and LEO is increasingly a real WAN-transit option to reason about.
- **What**: The University of Auckland's work extending an existing hardware-based GEO/MEO satellite simulator to LEO constellations, and the technical challenges of doing so on an extensive physical setup of around 150 devices. (from abstract only)
- **How**: Continuous real-time updates to `netem` delay and token-bucket-filter rate parameters to replicate the changing latencies and data rates a ground station experiences as satellites move, clients hand over, and inter-satellite links switch — as opposed to the static latencies/rates that make GEO and MEO easy to simulate.
- **Where applicable**: Test-lab technique; adoption requires a physical emulation rig, so it's academic-lab-scale rather than something to lift directly, but the parameter-driving methodology transfers to any hardware path-emulation setup.

### We're not in Kansas anymore: my experiences with IP geolocation

Shane Alcock (Alcock Network Intelligence, IODA)

- **Why**: Not core, but a candid consumer-side account of geolocation data quality — how the datasets are derived, where they go wrong, and the gotchas in using them — which matters to anyone doing geo-based policy, content access, or outage attribution. The IODA outage-attribution use case makes it concrete.
- **What**: The speaker's experiences consuming IP geolocation data inside IODA (Internet Outage Detection and Analysis) to attribute observed Internet outages to geographic regions, plus a documentation of how geolocation datasets are built and the failure modes encountered. (from abstract only)
- **How**: Practitioner experience report: working with commercial/derived geolocation feeds against observed outage data, and the mismatches that arise when the data's granularity, freshness, or methodology doesn't match the attribution task.
- **Where applicable**: Applicable to anyone using IP geolocation for analytics, geo-blocking, or content delivery decisions; not a technique with infrastructure prerequisites, but a set of caveats.

## Skipped

- **The Weakest Link in the Modern Cyber Threat Landscape** (CyberFern) — general security-awareness messaging, no transferable technique.
- **AI-Powered Telco SecOps Use Cases** (Fortinet) — vendor pitch in substance.
- **Resilient and Inclusive Networks** (TUANZ) — policy/social accessibility framing, not technical.
- **Internet Governance** (InternetNZ) — WSIS+20/multistakeholderism policy track, no operational content.

## Themes

- **AI fabrics pull the whole optics stack along**: Two talks (Arista's UltraEthernet/LPO/1.6T, Flexoptix's 800G SNR/BER analysis) show AI-cluster demands driving coherent techniques and LPO into short-reach optics — a shift from "best-effort Ethernet, throw margin at it" to engineered link budgets at 800G+.
- **The cache is part of your system**: The .nz DNSSEC incident and Huston's resolver study both center the same lesson — correctness must be validated against real resolver/caching behavior, not against your own internally-consistent output.
- **GNSS is a single point of failure**: Chorus's Sync-as-a-Service trials reflect a wider move to terrestrial PTP/SyncE distribution as jamming/spoofing awareness grows — timing is becoming a delivered, hardened network service rather than a per-site antenna.
- **Mass change without disruption is the operator skill**: Chorus's 700k-home speed migration is representative: the hard problems are decoupling, scripting, and sequencing across interlocking systems, not the config change itself.
- **Mapping the physical plant against the physical world**: Communications Resilience's shared-dependency and geohazard mapping signals growing operator investment in physical-layer risk data — claimed redundancy versus actual shared-road/shared-transformer reality.
- **A regional program with strong local operators**: Several strong sessions are NZ-infrastructure-specific (Chorus, InternetNZ, Chorus timing trials); the techniques transfer even where the topology doesn't.
