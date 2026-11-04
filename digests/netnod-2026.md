<!--
conference: Netnod Tech Meeting 2026
type: operator
source_url: https://www.netnod.se/netnod-tech-meeting-2026
generated: 2026-11-02
registry_key: netnod-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Netnod Tech Meeting 2026

## Core

### Telstra outage: The night a network decided the year was 2006

**Links:** [Recording](https://www.youtube.com/watch?v=mJWE8npJKzA)

Speakers: Sven-Christian Ebenhag - Netnod

- **Why**: Outage postmortems are the highest-transfer-value content at an operator meeting, and the title suggests a time/date-handling fault at the root — a class of failure (certificate validity, RPKI/TLS time checks, protocol timers) that cuts across every network, not just one operator's.
- **What**: A walkthrough of a real Telstra outage in which the network apparently behaved as if the date were 2006. *(from title only — no abstract published)*
- **How**: Unknown until the talk; expect an incident timeline, root-cause analysis, and the detection/remediation path. Netnod's involvement suggests a Swedish/IX perspective on a global event.
- **Where applicable**: Broadly applicable — time-dependence is universal in routing, PKI, and control-plane security. The specific trigger may be Telstra-topology-specific, but the lessons on time sanity checks and blast-radius control transfer anywhere.

### AI clusters scale, data center networks are being pushed to their absolute physical limits.

Speakers: not listed in the program.

- **Why**: This is squarely the PM's physical-DC core interest — AI/ML workloads are the current forcing function on fabric design, optics, cabling, and power, and this is the meeting's dedicated session on where those limits actually break.
- **What**: A talk on how AI cluster scale is stressing datacenter networking past its physical limits. *(from title only)*
- **How**: Unknown; likely covers the usual pain points at this scale — lossless/RDMA-capable fabrics, optics reach and power density, topology (rail-optimized/flat) choices — but this is inference from the title, not confirmed content.
- **Where applicable**: Relevant to anyone building or evaluating AI-scale fabrics; the specific breaking points cited will likely depend on the speaker's silicon and scale assumptions, so check those when watching.

### Evolution and trends of optical networks

**Links:** [Recording](https://www.youtube.com/watch?v=leS6_JonBIc)

Speakers: not listed in the program.

- **Why**: Optics are a core PM interest, and a dedicated trends talk is the cheapest way to recalibrate assumptions about coherent pluggables, DCI economics, and where the transport market is heading.
- **What**: A survey of current evolution and trends in optical networking. *(from title only)*
- **How**: Unknown; trend talks at operator meetings typically span coherent DSP generations, pluggable vs. line-system trade-offs, and DC/WAN interconnect economics — treat those as the likely territory, not confirmed content.
- **Where applicable**: Broadly applicable to DC/WAN interconnect planning; watch whether the framing is carrier-transport-centric or DC-centric, since that changes which trends transfer.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Recording](https://www.youtube.com/watch?v=VuElGwCq6rY)

Speakers: not listed in the program.

- **Why**: Transceiver power is becoming a first-order constraint in DC design (often a large fraction of a port's total power budget), and a talk about driving savings from *internal* transceiver metrics — not vendor datasheets — is exactly the operational, measurement-driven optics content the PM values.
- **What**: A method for understanding and optimizing transceiver power efficiency using the transceivers' internal telemetry. *(from title only)*
- **How**: Presumably reads internal metrics (per-lane power, DSP/CDR state, temperature) from pluggable optics and tunes operating points for power savings — plausible given the title, but unconfirmed.
- **Where applicable**: Potentially broadly applicable since it works on standard pluggables; the savings and the specific metrics exposed depend on the transceiver vendors/generations tested, so note those constraints.

### Prevent route leaking with ASPA and BGP roles

Speakers: Johan Ervenius - Arista Networks

- **Why**: Route leaks remain one of the highest-impact, recurring Internet failures, and this covers the two current standards-track defenses — ASPA (RPKI-based AS provider authorization) and BGP roles (RFC 9234 OTC) — which is directly relevant to the PM's network-security and BGP-internals interests and to any operator's routing hygiene roadmap.
- **What**: A technical talk on deploying ASPA and BGP role/OTC mechanisms to prevent route leaks. *(from title only)*
- **How**: ASPA lets an AS cryptographically authorize its providers, enabling a validator on the receiving AS to detect and reject leaks; BGP roles add a per-session role (e.g., customer/provider/peer) signaled in the session so OTC-marked routes from the wrong direction can be dropped. This framing is from the standards, not the talk's confirmed content.
- **Where applicable**: Broadly applicable standards work, though the speaker is from Arista — expect standards content rather than a product pitch, but verify the deployment guidance isn't vendor-feature-shaped.

### StratoWeave: A New Architecture for Network Automation

**Links:** [Recording](https://www.youtube.com/watch?v=HXuK0YCMDGc)

Speakers: not listed in the program.

- **Why**: Automation tooling that others can adopt is exactly what an operator program should be up-ranked for, and a named "new architecture" suggests a designed system rather than a status update — worth the PM's attention as both a potential adopter and as a signal of where network automation architecture is heading.
- **What**: A proposed new architecture for network automation, presented under the name StratoWeave. *(from title only — no abstract published, so the actual contribution, scope, and any evaluation are unknown)*
- **How**: Unknown; the name hints at layered/multi-stratum weaving of automation concerns (config, state, intent across layers), but this is speculation from the title.
- **Where applicable**: Cannot be assessed from the title; check whether it assumes a particular operator scale or network model before judging transferability.

### Panel discussion - Beyond the Looking Glass: The Future of BGP Visibility

Speakers: panel, not individually listed in the program.

- **Why**: BGP visibility (looking glasses, route collectors, RIS/RIPE-style infrastructure) is the substrate for everything from route-leak detection to research on Internet behavior; Netnod runs major route-server and collector infrastructure, so a panel here carries practitioner weight. Fits the PM's BGP/datapath-internals interest.
- **What**: A panel on the future of BGP visibility tooling and infrastructure. *(from title only)*
- **How**: Unknown; likely covers limits of current looking-glass/collector models and what richer visibility (real-time, per-vantage, ASPA/ROV-aware) should look like.
- **Where applicable**: Broadly relevant — visibility tooling decisions at IX/collector level affect every operator's debugging and research.

## Adjacent

### Keynote speech: High volume AI vulnerability reports

**Links:** [Recording](https://www.youtube.com/watch?v=mmYFHkkCAV8)

Speakers: not listed in the program.

- **Why**: Security-adjacent but significant: AI is generating large volumes of vulnerability reports aimed at maintainers and PSIRTs, and how the receiving side triages that flood is a live operational problem that will reach every security team, including the PM's.
- **What**: A keynote on handling high volumes of (AI-assisted) vulnerability reports. *(from title only)*
- **How**: Unknown; expect discussion of triage pipelines, signal-vs-noise in AI-submitted reports, and coordinated-disclosure process strain.
- **Where applicable**: Relevant to any organization running a disclosure intake or PSIRT function; specifics may depend on the speaker's organization and its report volume.

### Internet Resilience in Ukraine

**Links:** [Recording](https://www.youtube.com/watch?v=C5vO-bwxtVI)

Speakers: not listed in the program.

- **Why**: Ukraine is the richest live case study of national-network resilience under sustained physical and cyber attack — connectivity engineering under war conditions, and a key input to European resilience planning, which is squarely an operator concern in the Nordics.
- **What**: A talk on how the Ukrainian Internet has maintained (or lost) resilience. *(from title only)*
- **How**: Unknown; likely covers re-routing around damaged infrastructure, IX and interconnect behavior, and regulatory/operational coordination.
- **Where applicable**: Lessons are Ukraine-context-specific but transfer well to any resilience/continuity planning effort; this session is followed by a related *Q&A Internet Resilience* session (Fredrik Lindeberg, Netnod), which suggests a substantive discussion block.

### Surviving in the new geopolitical landscape

**Links:** [Recording](https://www.youtube.com/watch?v=NyM55Lq-TCA)

Speakers: Patrik Fältström - Netnod

- **Why**: Fältström is a long-time authority on Internet governance and DNS/security policy; for infrastructure operators, geopolitical shifts (sanctions, jurisdictional control of infrastructure, cable and IX targeting) increasingly shape technical risk. Useful strategic context around the PM's network-security work, though not hands-on technical.
- **What**: A strategic talk on operating Internet infrastructure in a changed geopolitical environment. *(from title only)*
- **How**: Unknown; expect a policy/risk framing rather than a technical mechanism talk.
- **Where applicable**: Broadly relevant to any European infrastructure operator; not a technique talk.

## Wildcard

### The Internet Change Clock

Speakers: not listed in the program.

- **Why**: A genuinely novel-sounding measurement concept — apparently a way of quantifying the *rate of change* of the Internet's structure or behavior over time. This is the kind of thing the PM wouldn't search for, but which can reframe how they think about measuring their own network's stability and churn.
- **What**: Presentation of something called the "Internet Change Clock" — an instrument for tracking change in the Internet. *(from title only; the actual metric, data source, and findings are unknown)*
- **How**: Unknown; plausibly built on BGP/route-collector time series measuring structural change over time, but this is inference from the name.
- **Where applicable**: Unknown from the title; if the underlying data is public collector data, the approach may be reusable by anyone doing network trend analysis.

### AS112 Deployment Characteristics and Security

Speakers: not listed in the program.

- **Why**: AS112 — the distributed, volunteer-run service that sinkholes reverse-DNS queries for RFC 1918 and reserved space — is infrastructure almost everyone's network touches and almost nobody thinks about. A deployment + security study of it is exactly the "wouldn't have searched for it, glad I saw it" item, with real DDoS/abuse implications for anyone running or depending on it.
- **What**: An analysis of how AS112 nodes are deployed in practice and their security posture. *(from title only)*
- **How**: Unknown; likely measurement of node distribution, load, and misconfiguration/attack exposure.
- **Where applicable**: Directly relevant to operators who run AS112 nodes or see AS112-bound leakage; the deployment characteristics are inherently distributed-system-specific.

## Themes

- **Time and trust failures in the control plane**: The Telstra postmortem (a network "deciding" it was 2006) plus ASPA/BGP-roles route-leak prevention and the BGP visibility panel all circle the same theme — subtle trust-relationship and time-dependence bugs in BGP and its PKI are where the Internet keeps breaking.
- **AI as the new forcing function on physical networking**: Two sessions (AI clusters at physical limits; transceiver power efficiency) treat AI workload scale as the driver reshaping fabrics, optics, and power budgets — the physical-DC agenda is now the AI agenda.
- **Power as a first-class network metric**: Optimizing transceiver efficiency from internal metrics signals a shift from performance-only to performance-per-watt thinking in optics and fabric design.
- **Resilience under geopolitical stress**: Ukraine's Internet resilience, Fältström's geopolitical talk, and the resilience Q&A make up a substantial track — a distinctly European operator concern this cycle.
- **AI changing the security workflow itself**: The keynote on high-volume AI vulnerability reports shows AI arriving not just as a threat surface but as a load on the receiving end of disclosure processes — a field-level shift worth tracking.
- **Measuring the Internet's change, not just its state**: The Internet Change Clock and the BGP visibility panel both point at better longitudinal and per-vantage measurement as a growing operator interest.
