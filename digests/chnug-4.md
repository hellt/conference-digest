<!--
conference: CHNUG #4
source_url: https://chnug.ch/chnug004
generated: 2026-11-11
registry_key: chnug-4
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# CHNUG #4

CHNUG #4 is a compact, single-evening Swiss networking user group event (17:00–22:00) with three talks, all in the network automation and monitoring space. No abstracts were published for any of the talks — write-ups below are grounded in the slide decks, which ToFaRev extracted.

## Core

### Network Monitoring with the gNMIc Operator

**Links:** [Slides](https://chnug.ch/chnug004/slides/chnug004-BA-gNMIc_operator-chnug.pdf) · [Recording](https://youtu.be/Tq85WB6UK7c)

Speakers: Roman Weber (OST Students), Valentino Diller (OST Students)

- **Why**: Streaming telemetry (gNMI) is the successor to SNMP polling for anyone operating DC fabrics and cloud infrastructure, but the operational gap has always been the collector: hand-edited config files, no HA, and no live sync with the network source of truth. This addresses that gap with a Kubernetes-native pattern the PM already lives in.
- **What**: A bachelor thesis project from OST (Ostschweizer Fachhochschule) that packages gNMIc — the open-source gNMI CLI/collector — as a Kubernetes Operator, adding declarative configuration, high availability, a constant reconciliation loop, and automatic target discovery. Open-sourced in 2026.
- **How**: The operator subscribes to YANG paths via gNMI (gRPC-based, OpenConfig) so the router pushes data on its own schedule instead of being polled. Target auto-discovery closes the "synchronization gap" between the network source of truth and the monitoring stack: target info is pulled from a SoT via export templates, or pushed via webhook. The demo ran targets in containerlab, with Prometheus/Grafana as the monitoring stack and NetBox as the SoT — both the pull and webhook examples ship in the operator docs.
- **Where applicable**: Broadly applicable — anyone running gNMIc on Kubernetes with a NetBox-class SoT. Note the maturity level: this is a brand-new (2026) open-source project born from a student thesis, so treat it as promising tooling to evaluate rather than battle-hardened production software.

### DDI: Managing IP Allocation with an Open-Source DDI

**Links:** [Slides](https://chnug.ch/chnug004/slides/chnug004-Managing_IP_Allocation_with_an_Open-Source_DDI.pdf) · [Recording](https://youtu.be/i8VJbY-0uO4)

Speakers: Marco Martinez

- **Why**: Commercial DDI suites (Infoblox-class) are the default answer to unified DNS/DHCP/IPAM, but they're priced out of reach for smaller environments and lock addressing data in a proprietary management plane. IPAM is squarely in the PM's remit, and this is a practical build-vs-buy analysis plus a working reference architecture.
- **What**: A survey of the DDI landscape followed by a concrete argument (backed by a prototype) that a "reasonably good" open-source DDI can be assembled with reasonable effort by composing three existing open-source products rather than writing any of DNS, DHCP, or IPAM from scratch.
- **How**: The requirements are a single API over DNS, DHCP and IPAM, full transparency, HA, and operations driven by data. The slides compare two integration approaches: Approach I glues components together but suffers from divergent automation tooling and configuration-consistency problems; Approach II (the one that works) is a single event-driven configuration plane over separate components. The stack referenced in the sources: Infrahub (OpsMill) as the data/source-of-truth layer, ISC Kea for DHCP, and PowerDNS for DNS, with everything running on containers or Linux.
- **Where applicable**: General technique, org-agnostic — but the speaker is explicit about the trade-offs: no single vendor supporting the whole stack, HA is your own problem, complexity is likely *higher* than a traditional DDI, and there's no hardware-appliance option. Best fit for teams that already run containerized infrastructure and want ownership of their components; a prototype ("DDI Version 1") is on GitHub.

### What's Next for Nornir: Project Update and Roadmap

**Links:** [Slides](https://chnug.ch/chnug004/slides/chnug004-CHNUG_Nornir_Update_&_Roadmap.pdf) · [Recording](https://youtu.be/U_eGZHYqObg)

Speakers: Damien Garros (OpsMill)

- **Why**: Nornir is one of the two mainstay frameworks for pure-Python network automation (≈100K PyPI downloads/month, 8 years in production at enterprises, ISPs and research networks). The stewardship just changed hands — OpsMill, whose Infrahub product is a source-of-truth platform — and the roadmap that follows has direct consequences for how the PM's teams automate network operations. It also signals where the field is heading: agents replacing orchestrators, with the execution layer standing alone.
- **What**: A project-state talk covering the stewardship change (OpsMill became steward in June 2026, with core maintainer Patrick Ogenstad and nornir-netbox author Wim Van Deun already on the team; creator David Barroso becomes Technical Advisor), the explicit commitments (stays open source and community-driven, ecosystem plugins stay with their maintainers), and a published roadmap proposal: (1) native async support, (2) enhanced runners (streaming, timeouts, cancellation, detach), (3) typed multi-vendor "Operations", (4) documentation overhaul, (5) support for agentic development. Target is version 3.7 — no breaking changes, no migration guide.
- **How**: The architecture rules are notable: small core with every implementation as a plugin, additive-only evolution (no signature or entry-point changes). Async arrives as an opt-in sibling runner (`nr.arun()`) since `Nornir.run()` delegates all concurrency to the runner — so async transports and non-blocking processors are new plugins, not core rewrites. Runners gain partial result streaming, per-host timeouts, in-flight cancellation and detached submit/reattach. "Operations" are a new typed task class (Pydantic input/output, per-vendor drivers registered via entry points) for cross-platform actions like `get_config`. Agentic development support means writing the unwritten maintainer knowledge down in machine-readable form (AGENTS.md, .agents/, SpecKit spec-driven development) so AI agents can contribute reliably — deliberately opt-in for human contributors.
- **Where applicable**: Broadly applicable to any Python-based network automation practice, multi-vendor by design (netmiko/napalm/scrapli/netconf plugins). The Infrahub–Nornir pairing is a natural consequence of the steward (OpsMill's positioning: Infrahub holds intent/source of truth, Nornir executes), but the framework works with NetBox, Nautobot, Ansible, and plain YAML inventories too. Everything shown is a proposal under active public discussion — the roadmap is explicitly "nothing final yet", so don't plan migrations around it today.

## Wildcard

None. With a three-talk program, all sessions map directly to the PM's core interests; there is nothing genuinely outside the core portfolio that would earn a wildcard slot, and padding the tier would be dishonest.

## Themes

- **Kubernetes-native patterns are absorbing network tooling**: the gNMIc Operator applies the operator/reconciliation model to telemetry collection — the same declarative, self-healing approach the PM already uses for cloud-native workloads, now applied to the network monitoring stack.
- **Source of truth as the integration hub**: all three talks converge on a SoT-centric architecture — NetBox/Infrahub feeding monitoring targets (gNMIc Operator), driving DNS/DHCP/IPAM (DDI), and supplying Nornir's inventory. The SoT is becoming the single control point that everything syncs from.
- **Open-source composition vs. commercial appliances**: the DDI talk is a template for the build-vs-buy decision (Kea + PowerDNS + Infrahub instead of Infoblox), accepting higher integration complexity in exchange for transparency, API ownership and cost.
- **Agents are redefining the automation stack**: the Nornir roadmap explicitly frames agents taking over the orchestrator role while execution layers stand alone, and invests in machine-readable specs (AGENTS.md, SpecKit) to make AI-assisted contribution reliable — an early, concrete signal of how network automation practice is changing.
- **Open-source project governance matters again**: both the Nornir stewardship change (company steward with community commitments) and the fresh gNMIc Operator release show the ecosystem's health depends on sustained commercial-ish stewardship without closed-sourcing — worth watching as a pattern for other NetOps tools.
