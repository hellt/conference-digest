<!--
conference: CHNUG #2
source_url: https://chnug.ch/chnug002
generated: 2026-11-11
registry_key: chnug-2
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# CHNUG #2

CHNUG #2 was a single-evening program (17:30–22:00) of four talks from the Swiss network user group, spanning network automation, open-source NetOps, cloud interconnect, and optical fundamentals. No abstracts were published; this digest is grounded in the speakers' slide decks. Given the small program, all four items earn a slot; there is no true Wildcard this cycle.

## Core

### Network Configuration in the Real World: Standards, Surprises and 'Creative' Implementations

**Links:** [Slides](https://chnug.ch/chnug002/slides/chnug002-network-config-in-the-real-world.pdf) · [Recording](https://www.youtube.com/watch?v=uQ3UDeY73OE)

Jens Vogler (Init7)

- **Why**: Everyone building network automation hits the same wall: model-driven configuration (NETCONF/YANG) promises vendor-agnostic, atomic, validated changes — and then reality intervenes. This is a candid operator postmortem of that gap, from an ISP that actually tried to industrialize service provisioning rather than demo it.
- **What**: A practitioner's account of automating end-to-end service provisioning from OSS/BSS inventory to device configuration at Init7. The core finding: IETF YANG models are barely usable for real configs, OpenConfig's vendor support is very limited, and what vendors call "NETCONF support" varies wildly in practice — enough that the team fell back to pushing CLI via Ansible. The honest learnings: single source of truth doesn't solve everything, escape hatches are still necessary for urgent fixes, abstract data models will always contain gaps, and once synchronization exists, divergence is possible.
- **How**: NetBox as the network inventory feeding a glue system that reconciles OSS (network operations) and BSS (CRM/billing) around the customer order flow. The intended path was NETCONF (RFC 4741) with YANG schemas for atomic commit and section-level config replacement; the working path ended up template-driven CLI with Ansible — well-understood tooling, but non-atomic applies and no reliable section replacement.
- **Where applicable**: Broadly applicable. The lessons are from an ISP's service-provisioning pipeline but transfer directly to any enterprise or cloud operator running NetBox-driven automation: verify vendor NETCONF/YANG claims before betting on them, keep deterministic escape hatches, and treat model-reality gaps as a design constraint, not a bug. Notable tooling observations (Cisco YANG Suite is powerful but slow and closed-source; pyang/ncclient are the friendliest automation entry points) are useful shopping guidance.

### Leveraging an Open Source NetOps-Stack: A Practical Approach for Orchestration and Observability

**Links:** [Slides](https://chnug.ch/chnug002/slides/chnug002-leveraging-open-source-network-automation.pdf) · [Recording](https://www.youtube.com/watch?v=rCe-FaalATE)

Patrick Mosimann (Cisco)

- **Why**: Two currents the PM tracks — open-source network automation stacks and AI agents entering operations — converge here in a concrete, reproducible reference implementation. This is the most direct example in the program of how LLM-driven operations can be built *on top of* a deterministic pipeline rather than replacing it.
- **What**: A practical, NAF-aligned (Network Automation Framework) open-source stack: NetBox + GitLab as intent/source of truth, GitLab CI/CD + Ansible as the deterministic executor (collect → compare → apply → rollback), gNMIc/Syslog/IPFIX as collectors, Prometheus/Vector/ClickHouse for observability, and a LibreChat-based "NetOps Assistant" MCP client on top. The interesting design decision is the explicit determinism boundary: same playbooks + inventory + variables → same actions, every time, with the LLM deliberately kept outside the deterministic core. Runbooks live as MCP resources (application-controlled context) while execution steps are MCP tools (model-controlled actions) — so the LLM drives NetBox, Prometheus, ClickHouse, and GitLab but "cannot skip automation."
- **How**: MCP (Model Context Protocol, Anthropic's open standard) as the connective tissue — a host/protocol/server architecture exposing tools (actions), resources (data), and prompts (templates). The talk includes an IOS XE MCP server implementation, and the whole stack is published on GitHub for inspection and reuse.
- **Where applicable**: The stack itself is vendor-agnostic in components (all open source, with an IOS XE example). The speaker is a Cisco Solutions Engineer, so expect a Cisco-flavored framing, but the deck is a working architecture with public code rather than a product pitch. Directly relevant to anyone evaluating how AI assistants should be wired into an existing GitOps/NetOps pipeline.

### Connecting Clouds over FTTH: How Easy Can CES Be?

**Links:** [Slides](https://chnug.ch/chnug002/slides/chnug002-init7-acp-connecting-clouds-over-ftth-how-easy-can-itbe.pdf) · [Recording](https://www.youtube.com/watch?v=9g8QD-Mjd4o)

Darragh Grealish (56K.Cloud), with Stefan Thoma (Init7)

- **Why**: Hybrid cloud connectivity usually means Direct Connect colocation, cross-connects, and intermediate carrier hops. This talk presents a materially different on-ramp — reaching cloud over mass-market FTTH — and pulls back the curtain on the L2 service (Ethernet7) that makes it work, including real constraints an architect needs to know before designing on top of it.
- **What**: How Init7's Ethernet7 (EVP-LAN, MEF E-LAN MP2MP) extends across their P2P FTTH access network (400+ regional PoPs, 2.5M+ ports) to CSP interconnects at datacenters where Init7 is already present — collapsing the classic multi-hop Direct Connect chain into a single provider L2 domain. The deck includes a worked AWS Direct Connect example, an air-gapped AI/data-to-cloud use case running RDMA over RoCE with MACsec, a FINMA-regulated banking B2B deployment, and dual-site/dual-link HA designs — plus the actual order-to-provision process (OTO installation, validation, ~2 weeks to service).
- **How**: Ethernet7 runs on Cisco Catalyst 9500 platforms, with BGP EVPN via Init7 route reflectors exchanging L2 information and VXLAN (UDP 4789) encapsulating frames across the fabric, MTU 9100. Customer-side L3 sits on a custom gateway above the L2 service; cloud ports are cross-connected directly to Init7 equipment in DCs.
- **Where applicable**: Init7/Europe-specific (Swiss FTTH plant, specific PoP/DC footprint) and partly a joint service pitch for ACP Cloud Connect and Init7 Direct Cloud Access. But the service constraints are broadly instructive for anyone evaluating L2 cloud on-ramps: no QinQ, one VLAN per L2 domain, VLAN IDs provider-managed, max 3 MAC addresses per VLAN, CPE managed by customer/partner. Those limits shape which designs (e.g. simple gateway-on-top vs. richer L2 extension) are feasible on any similar EVP-LAN service.

### Optical Foundations for IP Engineers: From Fiber Basics to CWDM/DWDM and Link Budgeting

**Links:** [Slides](https://chnug.ch/chnug002/slides/chnug002-flexoptix-optical-foundations-for-ip-engineers.pdf) · [Recording](https://www.youtube.com/watch?v=20qlPdcyW4Q)

Thomas Weible (FLEXOPTIX)

- **Why**: The PM's physical-layer core interest — and this is a compact, well-structured refresher that turns "optics folklore" into numbers you can plan with. Useful both as a personal grounding and as a model for what every IP engineer on a DC/WAN team should internalize before capacity and reach limits get blamed on the network instead of the fiber plant.
- **What**: A bottom-up tutorial on optical transport for IP engineers: fiber cross-sections and total internal reflection, MMF vs SMF trade-offs (OM1–OM5 vs OS1/OS2, modal vs chromatic dispersion, VCSEL vs DFB lasers), connector zoo (LC/SC/MPO-MTP) with the UPC-vs-APC polish distinction and why unmated high-power interfaces can be damaged by reflections, transmission bands (850 nm through L-band, including why DWDM lives in C/L), CWDM vs DWDM parameters, the three impairment categories (attenuation, dispersion, noise/OSNR), and link budget calculation.
- **How**: The actionable core is the link budget method: budget = min TX power − min RX sensitivity, then subtract fiber loss (≈0.38 dB/km at 1310, ≈0.22 dB/km at 1550 for SMF), connectors (0.3–0.6 dB each), splices (0.05–0.1 dB), plus a safety margin for aging, temperature, and future repairs — with the explicit rule that planning uses estimates but deployment should rely on measured values. WDM sizing: CWDM up to 18 wavelengths (20 nm spacing) over 80–120 km; DWDM C+L reaching 90–120+ channels at 100 GHz spacing over 1,000+ km with amplification, planned for a >10-year lifetime.
- **Where applicable**: Foundational and broadly applicable to any DC or WAN environment; no operator- or silicon-specific dependencies. The speaker is FLEXOPTIX's CTO, so expect a vendor's vantage point, but the deck is educational — physics and budget math, not a product pitch.

## Adjacent

*(No items were tiered Adjacent this cycle — with a four-talk program, each talk either hit the PM's core interests directly or is covered above.)*

## Wildcard

*(No true wildcards. All four talks fall within the PM's stated core interests; nothing here is outside their usual scan radius.)*

## Themes

- **The model-driven config dream vs. the CLI fallback**: Init7's NETCONF/YANG postmortem is part of a recurring industry pattern — standards exist, "support" is uneven, and operators ship with Ansible-over-CLI escape hatches while keeping the model-based target alive. Verification of vendor claims is becoming a first-class automation task.
- **Open-source NetOps stacks are consolidating**: NetBox + Git + CI/CD + Ansible + Prometheus/ClickHouse, aligned to community reference frameworks (NAF), is emerging as a recognizable default architecture rather than bespoke per-operator glue.
- **AI agents entering network ops — with guardrails**: The MCP-based NetOps Assistant pattern (LLM orchestrates tools and runbooks but never bypasses the deterministic pipeline) is an early, concrete template for "AI for infrastructure operations" that treats non-determinism as a design constraint.
- **Cloud on-ramps democratizing to mass-market access**: Extending EVPN/VXLAN L2 services over FTTH to CSP interconnects collapses the traditional Direct Connect chain — a structural shift for multi-site hybrid cloud, though with service constraints (MAC limits, single VLAN per domain) that shape what's buildable.
- **Physical-layer literacy as a planning discipline**: Link budgets, WDM channel planning, and connector hygiene presented as engineering math rather than trivia — a signal that as AI clusters and DC interconnect push optics harder, IP-level engineers are being asked to reason at the photon level.
