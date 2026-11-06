<!--
conference: ITNOG9
source_url: https://www.itnog.it/itnog9
generated: 2026-11-05
registry_key: itnog-9
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ITNOG9

ITNOG9 (Bologna, May 2025) is a single-track, operator-driven event: most sessions have no published abstract, so several picks below are judged from title, speaker, and slides where ToFaRev could extract them. Vendor-keynote slots (Corero, Nokia, Harmonic, Flexoptix's WISP talk) and organizational updates (ITNOG itself, RIPE NCC) are skipped.

## Core

### Networking for AI and Ultra Ethernet

**Links:** [Slides](https://www.itnog.it/itnog9/files/15-Networking%20for%20AI%20and%20HPC,%20and%20Ultra%20Ethernet%20-%20ITNOG9.pptx.pdf)

Massimo Magnani

- **Why**: AI cluster networking is the biggest forcing function on datacenter fabric design today — it is reshaping Ethernet itself (congestion management, telemetry, load balancing at job granularity). Even a regional-NOG take is worth the PM's time as a pulse check on how far Ultra Ethernet thinking has spread beyond the hyperscalers driving it.
- **What**: The program publishes no abstract and no extractable materials were available, so content cannot be described beyond the title — the session covers networking for AI/HPC workloads and the Ultra Ethernet effort. Treat this as a topic-signal pick, not a validated-results pick. (from abstract only — actually, no abstract at all; title and speaker only)
- **How**: Unknown from the program text. If it follows the shape of similar 2025 NOG talks, expect UEC's profile (telemetry, congestion control, RDMA-over-Ethernet semantics) — but that is inference, not a claim about this deck.
- **Where applicable**: Relevant to anyone tracking where lossless-Ethernet/RDMA fabric requirements are heading; depth and neutrality unknown.

### Power Consumption Considerations in Optical Metro Transport Networks

**Links:** [Slides](https://www.itnog.it/itnog9/files/2-Power_SJ_ITNOG.pptx.pdf)

Steve Jones

- **Why**: Power is becoming a first-order constraint on transport design — the deck cites telecom at 2–3% of humanity's power consumption and energy at 20–40% of telco OPEX. For the PM this is the physical-layer/WAN-transport side of their core interests with concrete, quantified trade-offs.
- **What**: A per-link power model (1G–400G, 10–80 km metro links) comparing passive WDM (colored transceivers in the host) against active transponding and muxponding. Headline results: transponding consumes ~4–5× the power of passive WDM per link, muxponding ~10–20×; worst-case deployments (hot-running industrial-temp optics, underutilized chassis, data-sheet-based cooling sizing) can exceed technologically-necessary power by >100×.
- **How**: Bottom-up model from ~10 manufacturers' data sheets, normalized per link: chassis/PSU/fan/management-card overhead amortized per line, client TRX power modeled at typical rather than max (direct-detect 1–25G parts actually draw ~40–60% of data-sheet max — 97% of sampled products consume under half of spec; coherent ≥100G ~75–90%), cooling approximated at a 2× multiplier. Muxponding compared against the equivalent client-rate alternative, not the line rate.
- **Where applicable**: Broadly applicable to metro DC-interconnect and carrier transport decisions; the model is deliberately parametric. Caveat: the speaker is affiliated with Huber+SUHNER/Cube Optics, a passive-WDM vendor, and the analysis strongly favors passive WDM — the numbers are useful, the framing is vendor-adjacent. Operators mixing passive and active WDM on the same metro plant is the recommended real-world pattern.

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations

**Links:** [Slides](https://www.itnog.it/itnog9/files/3-Flexoptix%20-%20Network%20Reliability%20Analysis%20Coherent%20Non-Coherent.pdf)

Thomas Weible

- **Why**: Transceiver reliability under real environmental conditions (temperature, SNR margin) is exactly the kind of physical-layer grounding the PM values when evaluating pluggable strategies — especially at 400G/800G where coherent-vs-PAM4 is a live architectural decision for DC and DCI links.
- **What**: An analysis of how SNR thresholds map to BER for coherent (16QAM) and direct-detect (PAM4) transceivers at speeds up to 800G, under environmental variation. No abstract was published and no source text was extracted, so the depth of the empirical work (sample size, test conditions) cannot be verified from the program. (title only — no abstract available)
- **How**: Presumably comparative BER-vs-SNR characterization of the two modulation families under temperature/environmental stress, per the title; methodology unconfirmed.
- **Where applicable**: Relevant to link-budget and transceiver-selection decisions in DCI/metro. Note the speaker is from Flexoptix (transceiver vendor), so treat conclusions with the usual vendor-analysis caution.

### EVPN/VxLAN outside the data center

**Links:** [Slides](https://www.itnog.it/itnog9/files/7-202505-nmodena-evpnvxlan-wan-ITNOG9.pdf)

Nicola Modena

- **Why**: EVPN/VXLAN is datacenter fabric technology escaping the DC — campus, WAN, and IXP backbones (MINAP's migration, see IXP updates below, is the same trend). This matters to the PM's DC/WAN-interconnect interest: the same control plane now spans both worlds.
- **What**: A technically dense practitioner walkthrough of using EVPN/VXLAN as an MPLS alternative for multi-tenant campus and WAN — solving multitenancy, any-to-any optimal pathing, and HA without spanning-tree or centralized L2. The speaker's core message: EVPN/VXLAN's real value is seamless L3 integration, not L2 stretching — "when in doubt, route."
- **How**: IP-only underlay (no leaf/spine or eBGP required; OSPF + loopbacks suffices, MTU 1550 since VXLAN fragmentation is unsupported), BGP L2VPN EVPN AFI/SAFI with FRR-based route reflectors placed anywhere; Type-3 for VTEP discovery, Type-2 MAC/IP (with ARP/ND suppression) eliminating flood-and-learn, ESI multihoming, and Type-5 prefixes with L3VNI for symmetric IRB and anycast gateways. Concrete config shown for Arista EOS, IOS XE, and Juniper. Also notable: native Linux kernel VXLAN with FRR as control plane, and Proxmox/NSX integration.
- **Where applicable**: Broadly applicable and multi-vendor; constraints called out honestly (MTU on WAN links, route-leaking between VRFs is platform-dependent, stretched L2 only for specific cases). The speaker is an independent network architect, not a vendor.

### Routing Security

**Links:** [Slides](https://www.itnog.it/itnog9/files/13-20250520_Presentazione_ITNOG9_PAESANI.pdf)

Marco Paesani

- **Why**: RPKI/ROV is now baseline; the frontier is path-origin validation (route leaks) via ASPA — this is both BGP operation and network security, squarely in the PM's core, and the deck has a concrete adoption timeline (global ASPA target 2027).
- **What**: A survey of the routing-security stack: why BGP's lack of security is structural (hijacks per RFC 7908 types 5–6, route leaks types 1–4), the MANRS history from 2013/14, RPKI v0/v1 (RFC 6810/8210) and ROV adoption trajectory (2019–2023, now best practice), BGPsec's practical problems (router hardware/software changes, slower convergence, needs near-universal deployment), and ASPA as "RPKI v2" — incremental, partial-adoption-beneficial, using existing RPKI infrastructure with minimal overhead.
- **How**: ASPA verification per draft-ietf-sidrops-aspa-verification-22 (March 2025): ASes register authorized providers, and BGP roles per RFC 9234 (Provider, RS, RS-Client, Customer, Lateral-Peer, Sibling) constrain which learned paths may be re-advertised — catching route leaks ROV cannot. Includes a real static-ASPA config example on Huawei NetEngine 8000 and Routinator 0.14.2 support; NIST monitoring references. RIPE's ASPA support is on hold pending IETF consensus.
- **Where applicable**: Any AS operating BGP. Caveats: ASPA is still Internet-Draft stage, and it complements rather than replaces ROV — the deck is explicit that both are needed together.

## Adjacent

### PACMAN: Automazione della configurazione di rete in GARR, tra sfide tecnologiche e cambiamento culturale

**Links:** [Slides](https://www.itnog.it/itnog9/files/12-itnog9_pacman_v2.pdf)

Francesco Lombardo

- **Why**: One of the more complete config-automation case studies on the program: full production deployment at national scale (~160 devices), with the cultural-change narrative that usually determines whether these projects survive.
- **What**: GARR-T's Ansible-based packet-layer configuration manager for its 135-device (now ~160) Juniper MX/PTX IP/MPLS backbone — replacing device-by-device SSH CLI work, with the entire fleet now "pacmanized" and PACMAN integrated into daily operations.
- **How**: YAML intent models per device + Jinja2 templates rendered by an Ansible engine with per-vendor modules (Juniper/Arista/Cisco), GitLab CI/CD with merge-request review as the change workflow, AWX scheduled jobs running plan-mode drift detection across all devices, results pushed to Git with last-commit-author attribution, and a NetBox plugin giving compliance dashboards. The honest half of the talk: CLI-era NOC resistance to Git/Docker/YAML, large-scale refactoring of legacy configs into per-device intent models, and cross-team (DevOps/NOC/eng) misalignment.
- **Where applicable**: GARR-specific implementation, but the pattern (template + SoT + CI review + scheduled drift checks) transfers to any mid-size operator. Roadmap: customer-premises routers, a workflow orchestrator, auto-remediation of non-compliant devices.

### Automating a Service Provider Network: A Practical Introduction

**Links:** [Slides](https://www.itnog.it/itnog9/files/11-[ITNOG9]Aielli.pdf)

Elia Aielli

- **Why**: A bottom-up, production-first automation story — valuable precisely because it starts from one repetitive, high-risk task rather than a grand platform, which is how most operators actually begin.
- **What**: How Timenet automated the single border ACL aligned across all its edge routers (Cisco ASR9k, IOS-XR): a YAML source-of-truth model generated from the running config, then deployed atomically so the network is never left open mid-change — with attention to TCAM exhaustion and IOS-XR best practices.
- **How**: Netmiko/SSH to collect running ACLs, TextFSM with NTC templates for parsing (a local template was written for the XR ACL command, planned for upstream contribution), a Python function converting structured output into the YAML model, Jinja2 to adapt the model to the `cisco.iosxr.iosxr_acls` module with `state: replaced` (single commit, ACL always applied to interfaces), plus a cron script checking for drift. Deliberately simple stack: Ubuntu, Python, Ansible, Jinja2, Netmiko.
- **Where applicable**: Any operator starting automation on CLI-first gear; explicitly vendor-agnostic in approach even though the example is IOS-XR. Future work acknowledges the limits: moving to a structured SoT, Git versioning/CI-CD, object-group alignment.

### From Clicks to Code: Optical Network Automation Journey in GARR

**Links:** [Slides](https://www.itnog.it/itnog9/files/4-ITNOG9_Dai%20Click%20al%20Codice_Matteo_Colantonio.pdf)

Matteo Colantonio

- **Why**: The optical-layer counterpart to PACMAN — automating DWDM/transponder provisioning is where physical-transport operators are heading, and it pairs directly with the PM's optics and DC/WAN interconnect interests.
- **What**: GARR's journey from manual, GUI/clicks-driven optical network operations toward code-driven automation. No abstract was published and no source text was extracted, so the specifics of the tooling and results cannot be described beyond the title. (title only — no abstract available)
- **How**: Unknown from the program text; the title indicates a transition from portal/manual workflows to automated, code-based management of the optical plant.
- **Where applicable**: National research and education networks and carriers with their own DWDM estates; presumably GARR-specific in tooling, transferable in pattern.

### KINDNS

Ulrich Wisser

- **Why**: DNS operational hygiene is a resilience topic that touches every operator the PM works with, and KINDNS is ICANN's attempt to make DNS best practices auditable and adoptable — with a v2 revision actively under discussion.
- **What**: An overview of KINDNS (Knowledge-sharing and Instantiating Norms for DNS and Naming Security), ICANN's voluntary framework that breaks DNS operators into categories (TLD/critical zone, SLD, closed/private resolver, public resolver) and gives each 6–8 concrete practices.
- **How**: Category-specific MUST/SHOULD practice sets: DNSSEC signing and key management, restricted zone transfers, zone-integrity control, authoritative/recursive separation, infrastructure diversity (network, geography, software), monitoring; for resolvers, DNSSEC validation, ACLs on recursion, QNAME minimization, and DoT/DoH; for public resolvers, data-retention limits. v2 discussion points: response-rate limiting on authoritative servers, split operational responsibility (e.g. root-zone operators), IPv6 reachability and RPKI ROAs for the DNS prefixes themselves, and community steering.
- **Where applicable**: Any DNS operator from small to large; it is a checklist/framework, not a technology — its value is as an audit baseline and procurement reference.

### PeeringDB updates

**Links:** [Slides](https://www.itnog.it/itnog9/files/9-20250520_ITNOG9_Morina_Livio_r2.pptx.pdf)

Livio Morina

- **Why**: PeeringDB is the de-facto interconnection data layer, and this update has a directly relevant identity angle: mandatory phishing-resistant-adjacent MFA (TOTP plus FIDO U2F) and the elimination of password-based API auth — a small but real instance of passkey-class auth reaching core Internet infrastructure.
- **What**: The 2024/2025 PeeringDB review: 2024 growth (networks 29,148→31,597, exchanges 1,152→1,239, users +11.2%), new Carrier (L1/L2 providers) and Campus (multi-facility cross-connect) object types, automatic removal of RIR-reclaimed ASNs, KML/KMZ geographic export, and the 2025 roadmap.
- **How**: MFA becomes mandatory for all authenticated users on 1 July 2025 — TOTP with backup codes, or FIDO U2F; API access moves to API keys, no more username/password. A new web tool will compare interconnection opportunities across facilities; peeringdb-py local sync is recommended to avoid query limits and PeeringDB-side load. The whole platform is BSD-2-Clause open source on GitHub.
- **Where applicable**: Universal for peering coordinators and anyone using PeeringDB data in automation (it is a common input for router config generation). The MFA/API-key mandate is an early signal of what Internet infrastructure services will require of integrators.

### IXP updates

**Links:** [Slides](https://www.itnog.it/itnog9/files/16-itnog9-ixp-updates.pdf.pdf)

Various

- **Why**: Bundled here for one genuinely valuable postmortem: the 12 May control-plane incident at MIX, plus a fleet-wide VPLS→EVPN-VXLAN migration at MINAP — operational lessons that transfer to any switching environment.
- **What**: Rapid updates from Italian IXPs. The MIX incident: a dormant bug that silently disabled control-plane filters combined with high ARP traffic (a /21 expansion plus scanning activity) and illicit traffic on the peering LAN drove switch CPU very high; ~25 hours on calls with the vendor; incident not formally closed; next actions are BGP parameter revision on the L3 network and restoring border-router redundancy. MINAP (3rd Italian IXP by traffic, peak 625 Gbps): all POPs upgraded to 100GE, migrated from VPLS to EVPN-VXLAN, sFlow implemented for members, OpenBGPD route server planned. TOP-IX/VSIX/GE-DIX: federation work, ISO 27001/14001, PMACCT-based stats, a GPU-accelerated biomedical data project, and a university "digital twin" test environment for an IXP.
- **How**: The incident mechanism (control-plane filtering silently lost + ARP amplification on a large broadcast domain) is the transferable part — as is the remediation sequence (BGP/L3 parameter review, border redundancy) and the decision to publish the timeline.
- **Where applicable**: Any L2 peering fabric and IXP operator; the EVPN-VXLAN migration mirrors the "EVPN outside the DC" talk above. Presentation is in Italian.

### Costruire un ambiente di test sicuro per un IXP

**Links:** [Slides](https://www.itnog.it/itnog9/files/10-Building_a_secure_Test_Environment_for_an_IXP_ITNOG_final_version%20%281%29.pptx.pdf)

Marta Burocchi

- **Why**: Testing and pre-production validation of IXP infrastructure is an under-served practice, and a dedicated talk on building a secure test environment signals growing operator investment in validation before change.
- **What**: Building a secure test environment for an IXP. No abstract was published and no source text was extracted, so scope and tooling cannot be described beyond the title. (title only — no abstract available)
- **How**: Unknown from the program text.
- **Where applicable**: IXP and shared-facility operators; likely useful as a pattern for anyone standing up network test beds isolated from production.

## Wildcard

### ISDN - Protocol Wars

**Links:** [Slides](https://www.itnog.it/itnog9/files/5-isdn_pub.pdf)

Leonardo Rizzi

- **Why**: A deliberately different pick — a retrocomputing talk that is actually a compressed history of the protocol wars that shaped today's Internet: circuit vs packet, virtual circuits vs datagrams, X.25/OSI vs TCP/IP. Those same debates recur in modern dress (SDN's central control, deterministic networking, SR's source-routed paths), which makes the historical grounding worth an hour.
- **What**: A tour from the 1973 ARPANET (1822/NCP, IMP maps, DS0 uplinks) through the circuit-vs-packet and VC-vs-datagram arguments (state, congestion control, failure behavior — laid out in a clean comparison table), the Internet-vs-OSI outcome, and then ISDN itself: TDM/E1 framing, BRI/PRI channel architecture, Italy's 1991–1994 "Rete Intelligente" rollout, and an inflation-adjusted 1993 price comparison across European countries (Italian PRI at ~13,800 EUR/yr MCR).
- **How**: The living part of the talk is OCTOI — the Osmocom community's TDM/ISDN/SS7 network over IP, where retrocomputing enthusiasts interconnect real TDM equipment worldwide, using devices like the icE1usb (dual E1 + GPS-DO + USB, on an iCE40 FPGA). An EWSD switch was even installed at 38C3.
- **Where applicable**: Not operational — but the datagram-vs-VC argument table is genuinely useful framing for anyone reasoning about connection-oriented revivals in modern fabrics, and the community-TDM-over-IP network is a quirky demonstration that legacy circuit infrastructure can be virtualized over packet networks.

## Themes

- **Automation is the dominant storyline**: three independent Italian operators (GARR twice — packet and optical layers, plus Timenet) presented source-of-truth/CI-CD journeys, and the recurring sub-theme is that the hard part is cultural (CLI-era NOCs adopting Git review), not technical.
- **Power and reliability of optics as OPEX front-and-center**: quantified passive-vs-active transport power models and 800G transceiver reliability analysis signal that the physical layer is being re-examined through an energy/operational-cost lens.
- **AI fabrics arrive at regional NOGs**: an Ultra Ethernet talk on a NOG program shows AI-cluster networking requirements (lossless Ethernet semantics, job-level behaviors) diffusing beyond the hyperscaler tier that defined them.
- **Routing security moves from ROV to ASPA**: RPKI ROV is treated as settled best practice; the live frontier is ASPA for route-leak detection, with a 2027 global adoption target and draft-stage tooling already shipping in routers.
- **EVPN/VXLAN is escaping the datacenter**: both a dedicated tutorial and MINAP's production VPLS→EVPN-VXLAN migration confirm DC fabric tech becoming the default campus/WAN/IXP backbone pattern.
- **Identity and testing reach core Internet infrastructure**: PeeringDB's mandatory TOTP/FIDO MFA plus API-key auth, KINDNS's DNS hardening framework, and a dedicated IXP secure-test-environment talk show even the most legacy corners of the interconnection world adopting modern identity and validation practice.
