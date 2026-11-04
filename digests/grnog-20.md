<!--
conference: GRNOG 20
type: operator
source_url: https://grnog.indico.nogalliance.org/event/13/
generated: 2026-11-03
registry_key: grnog-20
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# GRNOG 20

GRNOG 20 (June 30, 2026, Athens) published **no abstracts for any session** — the program gives titles and speakers only. I fetched each selected item's event page; those confirmed speakers, durations, and slide attachments but added no descriptions. Every write-up below is therefore **(program text and speaker/slide metadata only)** — grounded in what the titles, affiliations, and attached deck names indicate, not in a substantive abstract. Depths are correspondingly shallow; treat this as a watch-list, not a summary of findings.

## Core

### WebPKI, automation and the push for more agility

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/178/) · [Slides](https://grnog.indico.nogalliance.org/event/13/contributions/178/attachments/116/207/HARICA_GRNOG_20.pptx)

Dimitris Zacharopoulos

- **Why**: Certificate automation and lifecycle agility sits squarely in the PM's identity/PKI interests. WebPKI is the trust root for TLS everywhere — DC, cloud, and enterprise — and the operational pain of short-lived certs, ACME, and CA/B Forum rule changes is shared across every environment.
- **What**: The attached deck is titled `HARICA_GRNOG_20.pptx`, strongly suggesting this is a talk by the HARICA CA (the Greek academic/regional certificate authority) about the state of WebPKI, certificate automation, and the push for faster certificate issuance/rotation cycles (program text and slide metadata only).
- **How**: Unknown from the program. Presumably a CA-operator's perspective on automation (ACME/short-lived certificates) and the policy/standards environment driving agility — the speaker is active in CA/Browser Forum and PKI standards work, so expect a standards-informed view.
- **Where applicable**: Broadly applicable — WebPKI affects every HTTPS endpoint. Note the perspective is that of a CA operator, not an enterprise certificate consumer, so operational detail will be issuance-side rather than fleet-rollover-side.

### EVPN – One Control Plane to Rule Them All

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/186/)

Patrick Prangl (Arista Networks)

- **Why**: EVPN is the de facto control plane for modern physical DC fabrics (VXLAN overlays, multi-dimensional ECMP, integrated bridging/routing) — directly in the PM's physical DC networking core. The "one control plane" framing speaks to a live operational debate: collapsing L2/L3/overlay/underlay services onto a single BGP-based control plane instead of stitching VLANs + IGP + separate overlay signaling.
- **What**: A position/tutorial-style talk arguing for EVPN as the unified control plane across datacenter (and possibly WAN) services, per the title and the speaker's vendor affiliation (program text only).
- **How**: Unknown from the program; expect BGP EVPN route types, VXLAN overlay with an underlay, and EVPN's L2/L3 service models (E-LAN/E-Tree, IRB) as the framing.
- **Where applicable**: Applicable to any multi-tenant or leaf-spine DC being designed or refreshed. **Caveat**: the speaker is from Arista, so treat this as a vendor-lensed architectural pitch — worth watching for the conceptual argument (consolidated control plane, one failure domain to reason about), not for vendor-neutral tradeoffs.

### ASPA and Roles: What's up with that?

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/177/)

Antonis Chariton (AS4601 | Cisco)

- **Why**: Routing security is a core interest, and ASPA (Autonomous System Provider Authorization) is the current frontier of RPKI-based BGP security — the mechanism that extends protection beyond ROAs/origin validation to *AS-path* verification. "Roles" refers to the ASPA registration taxonomy (e.g., provider vs. peer relationships) that has been actively debated in the RPKI working group. A talk titled "What's up with that?" from an operator/standardista (Chariton runs AS4601/Packet Clearing House infrastructure and works on RPKI tooling) is likely a candid status-and-interop report, exactly the kind of transferable operational content this program should surface.
- **What**: An update on ASPA adoption, the roles model in RPKI, and the practical questions operators face when registering ASPA records and enabling AS-path verification (program text and speaker metadata only).
- **How**: Presumably: RPKI-signed ASPA objects binding a customer AS to its authorized providers, plus BGP AS-path verification at receiving ASes, with discussion of the role registration semantics that caused deployment confusion.
- **Where applicable**: Any operator running BGP with RPKI ROV today. Broadly applicable and standards-based (not org-specific), though real-world enforcement value depends on upstream adoption rates — which is likely the crux of the talk.

### MPTE update

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/179/) · [Slides](https://grnog.indico.nogalliance.org/event/13/contributions/179/attachments/115/205/MPTE.pptx)

Dr Kireeti Kompella (HPE Networking)

- **Why**: Kompella is one of the principal authors of the MPLS and segment-routing protocol family, and "MPTE" refers to the emerging **multi-path traffic engineering** work (the successor direction to per-flow SR-TE and PRECISION-style path steering) being pursued in the IETF SPRING/RTGWG space. DC/WAN interconnect and TE internals are core to this PM. An "update" from the author himself is a first-hand read on where large-scale path steering is heading — worth the slot even with no abstract.
- **What**: A progress report on the MPTE architecture — steering traffic across multiple paths with fine granularity, aimed at fixing what per-destination ECMP and heavy per-flow TE can't do well (program text and speaker metadata only; the MPTE.pptx deck exists but was not readable here).
- **How**: Presumably the MPTE label/segment approach: encoding per-path/per-flow steering state compactly so a single tunnel can carry many flows with independent placement, without per-flow session state in the core.
- **Where applicable**: Operators with SR-MPLS or SRv6 underlays, or building DC-to-WAN fabrics that need granular steering (elephant/mice separation, non-minimal path routing, loss-aware placement). Vendor-neutral in intent (it is IETF-track work presented by a long-time individual contributor), but expect it to reflect HPE's implementation timeline.

## Adjacent

### A comprehensive analysis of the IRR landscape

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/181/) · [Slides](https://grnog.indico.nogalliance.org/event/13/contributions/181/attachments/117/201/A%20comprehensive%20analysis%20of%20the%20IRR%20landscape.pptx)

Stavros Konstantaras (AMS-IX)

- **Why**: IRR (Internet Routing Registry) data is still what most networks generate route filters from, and its well-known staleness/inconsistency is a routing-security hygiene problem that also affects RPKI deployment. A *comprehensive analysis* — with the program having no abstract — suggests a data study across registries (RIPE, RADB, ARIN, etc.): freshness, coverage vs. RPKI, hijack-attributable errors. That's evidence, not anecdote — the kind of cross-environment content the PM should watch.
- **What**: A landscape-scale analysis of IRR data quality and coverage, from AMS-IX (which has both exchange-point visibility and a public IRR mirror) (program text only).
- **How**: Unknown; presumably registry-scraping and cross-correlation of route/route6 objects against observed announcements and/or RPKI ROAs.
- **Where applicable**: Any operator that uses IRR-derived filters (near-universal). The findings should be broadly applicable; note AMS-IX's vantage point means analysis is anchored on the European exchange ecosystem.

### Infrahub: Next-gen data management platform for Design-Driven Automation

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/183/)

Pete Crocker (OpsMill)

- **Why**: Network automation source-of-truth is a persistent operational problem. "Design-driven automation" — declarative, design-first intent feeding validation and provisioning — is the current generation's answer to the limits of pure inventory-SoT tools (NetBox-style) and bespoke scripts. Tooling that others can adopt is explicitly what this operator program should surface.
- **What**: A talk introducing Infrahub, OpsMill's data-management platform for network automation: managing the intended design (schemas, relationships, hierarchical data) and driving automation from it (program text only — no abstract, and the event page shows **no presentation materials and "Not scheduled"**, which suggests this session may have been cut or not yet scheduled; verify before seeking the recording).
- **How**: Presumably a graph/schema-oriented data model with versioning and constraints, integrated into provisioning pipelines rather than a flat IPAM inventory.
- **Where applicable**: Any network team building declarative automation. **Caveat**: the speaker is from the vendor itself, so expect product framing; the transferable content is the design-driven paradigm, which can be evaluated independently of the product.

### DNS4EU Public DNS Resolver Infrastructure

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/185/)

Panagiotis Palias (Whalebone)

- **Why**: DNS4EU is the European Commission-backed public DNS resolver platform — a multi-node, privacy-focused resolver alternative to 8.8.8.8/1.1.1.1. For a PM watching internet infrastructure, this is a real-world case study in operating geographically distributed resolver infrastructure with policy/filtering layers, and it carries sovereignty/identity implications (who resolves your names).
- **What**: The architecture and operation of the DNS4EU public resolver infrastructure, presented by Whalebone, one of the platform's operators (program text only).
- **How**: Unknown; presumably anycast/distributed resolver nodes, filtering and malware-blocking policy tiers, and privacy handling, though details aren't in the program.
- **Where applicable**: Relevant as operational context for anyone running or evaluating public recursive DNS; **specific to the DNS4EU consortium's design** — treat the numbers (deployment size, load) as org-specific rather than transferable benchmarks.

### Balkan Digital Gateway: Enhancing Greece's Regional Connectivity

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/188/)

Polina Kudriashova, Valentin Velichkov

- **Why**: Regional fiber/cross-border connectivity projects shape the physical WAN topology that interconnects Greek (and Balkan) datacenters and IXs. For a PM whose remit includes physical DC/WAN interconnect, hearing where new regional capacity is being built — and its latency/route-diversity implications — is useful planning context, even if the talk is more project-update than deep technical.
- **What**: An overview of the Balkan Digital Gateway initiative and Greece's position as a regional interconnect hub (program text and deck metadata only).
- **How**: Unknown; expect maps of new/expanded routes and interconnection points rather than protocol-level detail.
- **Where applicable**: Directly relevant only to operators with SE-European footprint or Greece-landing infrastructure; **project- and geography-specific**, and pitched at policy/funding-body level rather than engineer level.

## Wildcard

### The Future of Network Visibility: LLM and Intelligent Monitoring

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/184/)

Luca Deri (ntop)

- **Why**: Luca Deri is the creator of ntop/ntopng — decades in packet-analysis and flow-monitoring tooling. Seeing *that* lineage pivot to LLM-driven monitoring is a strong signal of where observability tooling is heading: natural-language querying of flow data, automated anomaly explanation, and conversational triage. Not a fit for the PM's core topics, but a genuine "I wouldn't have searched for this, but…" pick.
- **What**: A look at integrating LLMs into network monitoring/visibility tooling (program text only).
- **How**: Unknown; presumably pairing ntop flow/packet telemetry with LLM-driven summarization, query, and root-cause suggestion.
- **Where applicable**: Any operator with flow visibility (NetFlow/IPFIX). Caveat: ntop is a vendor of monitoring tooling, so the talk may double as product positioning — the signal is the *direction*, not the specific integration.

### Agentic AI in Networking

**Links:** [Abstract](https://grnog.indico.nogalliance.org/event/13/contributions/187/) · [Slides](https://grnog.indico.nogalliance.org/event/13/contributions/187/attachments/121/203/Agentic_AI_%CE%9Detworking_GRNOG%20%282%29.pptx)

Ioannis Kaminaras, Kostas Gerakaris (Uni Systems)

- **Why**: Agentic AI — autonomous LLM agents that plan and execute multi-step network changes — is the emerging subfield where the PM's identity interests (agentic/workload identity) meet their networking interests. This is an early, practitioner-level look at the concept from a systems integrator (Uni Systems), useful for understanding what's being *attempted* in the field today (and what its authorization/trust-model problems are).
- **What**: An overview of agentic AI applied to networking operations (program text and deck metadata only — no abstract).
- **How**: Unknown; expect LLM-agent architectures (tool use, planning loops) applied to network operations tasks like configuration, troubleshooting, or assurance.
- **Where applicable**: Conceptual relevance to any network team; **approach is vendor- and lab-stage**, so treat claims of production maturity with skepticism. Notably, running agents that make network changes raises exactly the identity/authorization questions the PM works on — a natural cross-reference with the WebPKI talk.

## Themes

- **The program is abstract-starved**: a recurring hazard of regional NOGs — only 2 of 12 sessions had any slide material published, and none had written descriptions, so triage here leans on titles and affiliations. Where the field is collectively heading must be inferred, not read.
- **PKI/routing-security tooling is maturing into an "automation era"**: WebPKI automation, ASPA/ROV progress, and IRR landscape analysis together signal the community pushing trust infrastructure from "manually provisioned" toward "continuously verified" — a shift that touches both identity and routing.
- **Physical-layer regional buildouts remain a NOG topic in Southeast Europe**: the Balkan Digital Gateway and (to a lesser degree) DNS4EU reflect where EU-funded connectivity initiatives are concentrating — the physical substrate matters to this audience.
- **AI/LLM is appearing in two distinct operator-facing shapes**: LLM-assisted observability (Deri) and agent-driven network operations (Uni Systems) — both early-stage, both likely to grow; the second directly raises agentic-identity questions.
- **Single-control-plane consolidation for DC fabrics continues to be the standard-bearer argument**: the EVPN talk (vendor-lensed as it is) confirms EVPN's position as the converged L2/L3/overlay control plane of record, with the debate now about how far one control plane should reach (DC→WAN).
- **No talks on datacenter optics, lossless fabrics, RDMA, eBPF, or Kubernetes networking** at this edition — GRNOG 20's program skews routing/DNS/policy rather than cloud-native or physical-fabric internals, so this digest is thinner on those core interests than a NANOG or OCP-scale program would be.
