<!--
conference: Netnod Tech Meeting 2025
type: operator
source_url: https://www.netnod.se/netnod-tech-meeting-2025
generated: 2026-11-04
registry_key: netnod-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Netnod Tech Meeting 2025

A single-day operator program (Netnod, Stockholm, 9 October 2025). Note on source quality: almost no abstracts were published for this program — several picks below are grounded in slide decks extracted by the pipeline, and the remainder had only titles and speakers to work from. That is flagged per item. Host updates (Netnod), the ICANN keynote, the DNS-OARC event update, and the closing/social slots are skipped as housekeeping.

## Core

### Ultra Ethernet

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/15.Ultra%20Ethernet%20-%20Arista.pptx_.pdf) · [Recording](https://youtu.be/fRizzhFzcEU)

Johan Ervenius — Arista Networks (Systems Engineer)

- **Why**: The AI/HPC fabric problem — how to carry RDMA-like traffic at scale without RoCEv2's lossless-network crutches — is squarely in the PM's lossless-fabric/DC interconnect territory, and UEC 1.0 is the standards answer the whole industry is converging on.
- **What**: A technical walkthrough of the Ultra Ethernet Consortium specification (~500 pages, >100 member companies) and its transport (UET). The core finding: flow-based ECMP hashing degrades badly with few large flows — the slide deck quantifies 32 servers with 8×10 Gbps flows each achieving only ~71% worst-case efficiency on 32 uplinks, versus 99.98% when traffic is packet-sprayed 204 ways. UET is designed so spraying works: packets carry their ultimate destination memory location so out-of-order packets go straight into posted buffers.
- **How**: Key mechanisms: (1) out-of-order-capable RMA transport so one flow can use all paths; (2) packet trimming — switches truncate to 64 bytes and DSCP-mark "trimmed" instead of dropping, giving a fast congestion/loss signal; (3) sender-based Network Signal Congestion Control using delay, ECN and trimming together, plus an optional receiver-credit mode for incast (VOQ-like); (4) link-layer retransmission (ACK/NACK via 802.3 OCodes, negotiated via LLDP) to improve tail latency in pods with 256K–512K transceivers; (5) libfabric 2.0 as the application API.
- **Where applicable**: Standards-track and multi-vendor rather than Arista-proprietary, so broadly relevant to any Ethernet AI fabric planning. But UET requires new NIC and switch silicon — nothing here deploys on a RoCE fleet today. The efficiency numbers are the speaker's own modeling, not an independent benchmark.

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/Flexoptix%20-%20Network%20Reliability%20Analysis%20Coherent%20Non-Coherent-Netnod%20%282%29.pdf) · [Recording](https://youtu.be/4_1pM6o-pD4)

Dr.-Ing. Gerhard Stein — FLEXOPTIX (with Thomas Weible)

- **Why**: Rare, concrete hardware lab data on how 100G–800G transceivers actually behave at the edge of their operating envelope — exactly the optics/physical-layer evidence a DC networking PM rarely gets at operator meetings.
- **What**: A lab study of six device types (100G QSFP28 single-lambda DR and ER, 400G ZR coherent, 400G LR4, 400G QSFP112 DR4, 800G QSFP-DD DR8) measuring BER against fiber length, attenuation and temperature, up to and well past spec (~120 °C). Headline findings: direct-detection (grey/PAM4) transceivers' BER depends on both temperature and fiber length; coherent (400ZR) BER is largely insensitive to temperature and dominated by reach; there is very little margin between the CMIS high-alarm threshold and loss of signal; and after a thermal excursion, post-FEC BER recovered to roughly 10× worse than before the cooker was removed. Also a practical warning: short-reach testing of long-reach optics needs ≥11 dB attenuation or you damage the photodiodes.
- **How**: FLEXOPTIX's programmable-transceiver platform (FLEXBOX5) used as the test rig, with BERT measurements, controlled attenuation on G.652.D spools, and passive heatsinks/fans to manipulate temperature; pre-FEC and post-FEC BER tracked as rolling averages rather than snapshots.
- **Where applicable**: The measurement methodology and the failure-mode findings transfer to any 400G/800G optics deployment, DC or DCI. Caveats: the presenter works for a transceiver vendor, and this is component-level bench testing — no multi-vendor fleet statistics. Ends with a product-flavored live demo.

### SRv6 uSID: fundamental transformation of the IP stack

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/20251009-Netnod-SRv6-uSID-rev2.pdf) · [Recording](https://youtu.be/-Q9JYxKOp4U)

Ahmed Abdeslam — Cisco

- **Why**: uSID is now a Proposed Standard (RFC 9800) with real hyperscaler deployments, and the talk connects it directly to AI backend fabrics and DCI — the PM's datapath-internals and DC/WAN-interconnect interests. It is also the clearest signal that SRv6 is displacing VXLAN/SR-MPLS layering in new DC designs.
- **What**: A Cisco view of SRv6 uSID: the 128-bit destination address becomes an ordered list of uSID instructions (typically ≤6 fit in the DA, SRH available for ultra-scale TE), replacing per-domain shims (MPLS core, VXLAN DC, GTP mobility). Includes third-party evidence: Microsoft quotes on why SRv6 fits AI backends (source routing instead of ECMP, path enumeration for latency, coupling with the workload scheduler, source-side failure detection), a Nebius design replacing VXLAN-in-DC + SR-MPLS-in-metro with one end-to-end uSID design with stateless service insertion, and an Alibaba ultra-scale DCI deployment across China. Claims >85k Cisco routers shipped uSID-capable and SONiC mainline support (350+ PRs, 1600+ commits, contributors incl. Microsoft, Alibaba, Broadcom, NVIDIA).
- **How**: uSID instructions bind to underlay TE, overlay, or service chaining; L3VPN/GRT services carried via BGP RFC 9252; AI backends run static uSID fabric + SDN controller rather than distributed routing; AI DCI argument is that MPLS TE doesn't fit (no MPLS in SONiC or DC hardware, pervasive-deployment cost, breaks end-to-end model).
- **Where applicable**: The technology is standardized and multi-vendor, but this is a vendor talk with marketing framing ("fundamental transformation") and the deployment evidence is hyperscaler-specific (Microsoft, Alibaba, Nebius). For an operator, the transferable content is the architecture pattern — single protocol end-to-end, source-routed TE — not a drop-in design.

### Building Modern and Scalable DC Fabrics

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/17.Building%20Modern%20and%20Scalable%20DC%20Fabrics%20-%20Alperen%20Akpinar%20061025.pptx_.pdf) · [Recording](https://youtu.be/JwlfAEgXw7o)

Alperen Akpinar — Nokia

- **Why**: A useful map of how a major vendor is restructuring its DC portfolio around AI fabrics — backend fabrics, lossless/QoS, and DC gateways/DCI — plus an automation stack (EDA) that operators can actually try without a license.
- **What**: An evolution framing (STP/VLANs → VPLS → EVPN/VXLAN → SRv6/uSID, 10M → 800G+) anchored on the scale challenge: AI is redefining "large DC" from ~30 MW (2013) to 100K–1M-GPU "AI factories". The concrete architecture: two-tier topologies for 1K–16K GPU clusters, multi-plane topologies for 100K+; 800G AI backend fabrics on 7220 IXR-H5 / 7250 IXR; dynamic load balancing and RDMA-aware (Q-pair) hashing; DCQCN with PFC/ECN; real-time congestion telemetry; backend multi-tenancy segmentation; DC gateways with 800G ZR+ coherent DCI and 4×400G FlexE bundles; Event-Driven Automation (EDA) on SR Linux with a model-driven NDK and Kubernetes-based foundation.
- **How**: The transferable pattern is the tiering of designs by cluster size (two-tier vs multi-plane) and the coupling of backend fabric features (DLB, Q-pair hashing, congestion indicators) with an intent/event-driven automation layer rather than box-by-box config.
- **Where applicable**: The portfolio specifics are Nokia-only (IXR platforms, EDA) — this is a vendor solution overview, not a neutral paper. The sizing/topology patterns and the "try-eda" unlicensed playground (`make try-eda`, no registration) are the broadly applicable bits.

### Your AS-set is crucial to your routing security. 3 tips on securing your AS-set

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/10.Securing%20your%20AS-Set-Netnod.pptx_.pdf)

Lasse Jarlskov — Telia

- **Why**: Routing security hygiene with a concrete rule of thumb and free tooling — the kind of immediately actionable operator talk this digest exists to surface. Mismanaged IRR AS-SETs are a real leak/hijack vector via recursive expansion.
- **What**: Three tips from a transit operator: (1) know your AS-set's purpose — customer vs. peer vs. IXP-member sets serve different filter-building use cases and conflating them causes confusion (example: AS-DATAIX, an IX AS-set that expands to more ASNs and prefixes than the global table, with a shown inclusion chain from AS-DATAIX down to Bahnhof's AS8473); (2) watch what you include — recursive references are powerful and dangerous, bigger is not better, check the size of customers' AS-sets; (3) monitor who includes *you* — every inclusion of your ASN/AS-set in someone else's policy is a potential hijack or leak affecting your customers, with no automatic approval mechanism.
- **How**: RPSL/IRR objects built into upstream route filters; audit via bgp.tools' reverse-inclusion tool and Cloudflare Radar's IRR AS-set view; the recurring decision heuristic is "would you readvertise this in BGP?" — if not, it doesn't belong in the set.
- **Where applicable**: General technique, applicable to any network with transit customers, peering, or route-server sessions — no scale or topology dependency. References (DKNOG, Kentik, MANRS, Cloudflare) are all public. Based on the slide deck (no abstract was published).

### Mastering Network Operations: The Power of Abstraction in Automation

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/9.netnod2025%20-%20The%20Power%20of%20Abstraction.pdf) · [Recording](https://youtu.be/yK7xxkBPnew)

Jaakko Rautanen — Rautanen

- **Why**: Network automation done as a layered abstraction pipeline — the exact discipline the PM needs for cloud-native/fabric automation, presented as a transferable method rather than a product.
- **What**: A consultant's automation stack built around NetBox (with a custom "Ninja" plugin): abstract service models at the top, detailed network state in the middle, vendor-specific configurations at the bottom, with a configuration pipeline translating between layers. A worked example models a virtual network both as a detailed per-site entity and as a generic abstract service. A four-step design process is laid out — split the service into parts, design each data model (fields, types, references, create/edit/delete logic), implement and test as a NetBox plugin in Python, deploy with data migrations.
- **How**: Declarative, model-driven state in NetBox as the single source of truth, with code generation down the stack; lessons learned are: eliminate arbitrary rules, follow the declarative model, keep models generic.
- **Where applicable**: Broadly applicable to any shop that can run NetBox — this is a method, not a product. Caveat: the deck is high-level and conceptual; there are no metrics, scale figures, or postmortem detail, so treat it as a design pattern rather than a case study.

### Encrypted Network Traffic Analysis and Protection

David Hasselquist — Sectra

- **Why**: Encrypted-traffic analysis sits in the PM's network-security interest — how to reason about (and protect) traffic you cannot decrypt, increasingly the default state of the network.
- **What**: Unknown — no abstract, slides, or source text were published for this talk; only the title and speaker are available. The title indicates analysis of encrypted network traffic and protection mechanisms, and Sectra's background is in secure communications, so it may lean toward their secure-messaging domain rather than operator ETA tooling.
- **How**: Not determinable from the program. Recommend watching the recording if ETA is on the roadmap this cycle.
- **Where applicable**: Cannot be assessed. Flagged explicitly: **no abstract or materials published; assessed from title and speaker affiliation only.**

## Adjacent

### Meta – Big Trends and how it will change the Network

Janne Elvelid — META, Fredrik “Hugge” Korsbäck — META

- **Why**: Two Meta network engineers on macro trends reshaping networks — useful as a demand-side signal (what AI-era traffic and topologies will force on vendors and operators alike).
- **What**: Not published — no abstract, slides, or source text for this session; only title and speakers are available.
- **How / Where applicable**: Not determinable from the program. Worth a recording watch given the speakers' vantage point (Meta's infrastructure is a leading indicator for DC fabric and WAN build-outs), but this pick is based on the speakers alone. **No abstract or materials published.**

### Recursive DNS in Telia Company Sweden

**Links:** [Recording](https://youtu.be/zdM0jF1WGSE)

Björn Hellqvist — Telia

- **Why**: National-telco operational practice on recursive resolver infrastructure — a domain adjacent to the PM's core, and an operator talk where deployment/failure stories often surface.
- **What**: Unknown — no abstract or slides were published; only a title, speaker, and video are available.
- **How / Where applicable**: Not determinable from the program. **No abstract or materials published; assessed from title and speaker affiliation only.**

### Optics was instrumental in building the Internet—and will be crucial in an AI-driven world

**Links:** [Recording](https://youtu.be/WhkyBnPKbDM)

Magnus Grenfeldt — Smartoptics

- **Why**: Optics is core PM territory, but this session is a vendor presentation with no published abstract, slides, or source text — likely a Smartoptics DWDM product-lens view of the AI build-out.
- **What**: Unknown beyond the title's thesis: optical transport as a historical Internet enabler and a future AI-driven one.
- **How / Where applicable**: Not determinable from the program. Listed as adjacent rather than core precisely because there is no way to verify substance over pitch; the FLEXOPTIX talk (Core, above) is the optics session with actual data. **No abstract or materials published; assessed from title and speaker affiliation only.**

## Wildcard

### The Illusion of Control: Trusting Software in the Age of Compromise

**Links:** [Slides](https://www.netnod.se/sites/default/files/2025-10/18.The%20Illusion%20of%20Control.pdf) · [Recording](https://youtu.be/mWIxKHxxTG0)

Moin Rahman — Independent consultant / FreeBSD contributor

- **Why**: Not a networking talk at all — but it takes the "zero trust" idea the network world lives by and applies it to the software supply chain that *builds* the network stack (OS images, NOS builds, tooling). That framing — you don't control your security if you don't control your build — is a genuine signal of where infrastructure trust is heading.
- **What**: An argument that the drift from DIY source builds (LFS, Gentoo, BSDs) to package managers and now CI/CD pipelines created "assumed, not verified" security, illustrated with SolarWinds, XZ, and CCleaner. The proposal is "Zero Trust Builds": trusted source selection, reproducible builds, isolated build environments, cryptographic verification of every step. Includes a concrete catalogue of what breaks reproducibility (timestamps, non-deterministic compilation, hardcoded paths, embedded UUIDs, locale sensitivity, unpinned internet dependencies) and what upstream developers should do about it (`SOURCE_DATE_EPOCH`, fixed seeds, pinned dependencies, `diffoscope` checks), plus the state of reproducible-build testing across Debian, FreeBSD, OpenBSD, NixOS, and others. A memorable demo point: `github.com/freebsd` vs `github.com/free6sd` — one character off, full pipeline compromise.
- **How**: Deterministic/reproducible builds verified by byte-for-byte comparison, hardened isolated pipelines, and independent verification of vendor artifacts rather than trusting signatures alone ("signed binaries ≠ secure binaries").
- **Where applicable**: General — applies to any organization's software supply chain, and by extension to how you trust the firmware and NOS images running your network. The speaker is an independent FreeBSD contributor, not a vendor; the content is a practice guide, not a pitch. Based on the slide deck (no abstract was published).

## Themes

- **AI fabrics swallowed the program**: nearly every infrastructure talk — Ultra Ethernet, SRv6 uSID, Nokia, optics — reframed itself around AI backend networks, multi-GPU clusters, and AI DCI. Even a Nordic IX meeting is now an AI-fabric meeting.
- **Lossless is being redesigned, not tuned**: the field's collective move is away from RoCEv2's ECMP + PFC/DCQCN constraints toward packet spraying with out-of-order transports, new congestion signals (trimming, delay+ECN), and link-layer retransmission — UET is the concrete spec, and vendor roadmaps (DLB, Q-pair hashing) are converging on the same ideas.
- **Optics reliability is getting quantified**: 800G-era talks are starting to bring measured BER-vs-temperature/reach data rather than spec-sheet claims, with coherent and PAM4 showing clearly different environmental sensitivities.
- **Standards are arriving faster**: SRv6 uSID hit Proposed Standard (RFC 9800) with hyperscaler deployments, and UEC shipped a 500-page 1.0 spec — both are reaching operator audiences within a couple of years of first deployment, compressing the usual diffusion cycle.
- **Routing hygiene framed as shared responsibility**: the AS-set talk positions IRR hygiene as a collective-good contribution, with free tooling (bgp.tools, Cloudflare Radar) making audit a low-effort routine task.
- **A programing caveat**: this meeting published almost no abstracts, so slide decks (where they existed) did the heavy lifting; several potentially relevant talks (Meta, Sectra, Telia recursive DNS) remain unauditable from text and would require the recordings.
