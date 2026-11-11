<!--
conference: CHNUG #3
source_url: https://chnug.ch/chnug003
generated: 2026-11-11
registry_key: chnug-3
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# CHNUG #3

A compact three-talk program, but unusually dense for a regional user group: one operator's containerlab-driven greenfield/brownfield DC story with real deployment numbers, one vendor's map of AI-era fabric requirements, and one operator-led IETF telemetry standards deep-dive with production backing. All three land squarely in physical DC networking, automation, and operations.

## Core

### Change with Confidence: Containerlab at Proton

**Links:** [Slides](https://chnug.ch/chnug003/slides/chnug003-change-with-confidence-containerlab-at-proton.pdf) · [Recording](https://www.youtube.com/watch?v=RtJqWRYKf88)

Speakers: John Howard (Proton)

- **Why**: This is the strongest talk on the program for anyone running DC fabric operations: a full production migration story — vendor switch, greenfield build, and an 86-device brownfield cutover — where the entire risk was retired in container-based labs before hardware shipped. It is a transferable process story, not a Proton anecdote.
- **What**: Proton (privacy services, ex-CERN) built a new Norwegian datacenter in 2024 on a vendor they had never operated (Nokia 7220 IXR / SR Linux fabric, 7750 SR-1 / SR OS edge), with no hardware lab available, and then repeated the trick in 2025 with an 86-device Swiss brownfield migration plus a 23.10→24.10 upgrade backfilled to Norway. Reported results: 36 devices racked-to-in-service in 14 days, zero post-deploy config changes, and 100% of scaling limits measured in containerlab held on real hardware. The slides are candid about why they left Juniper (QFX hardware failure cascades, monthly bugs, weak virtual lab tooling, pricing) and about containerlab's limits.
- **How**: Containerlab runs vendor-faithful NOS container images (not slow QEMU VMs like vQFX/vMX) with YAML topology + configs + deploy/test scripts versioned in a repo; a whole multi-layer EVPN-VXLAN fabric fit on a 32 GB laptop. Validation covered control plane and data plane (Linux netns/vnet links for capture, injection, flap, packet loss). Design changes in round two: VRF leaking replaced with interface ACLs toward the core, simplified anycast routing, and unnumbered IPv6 BGP everywhere (numbered BGP and OSPF removed). Documented failure modes include HW-only bugs (a gNMI race when tagging many VLAN interfaces, link-local ND quirks, BFD-over-unnumbered-BGP broken in v23) and lifecycle gaps (an upgrade that swapped CentOS for Debian and missed SSD trim) — caught during commissioning, not in prod.
- **Where applicable**: Broadly applicable to any shop building or migrating EVPN fabrics — the technique is vendor-agnostic in principle (containerlab supports multiple NOSes), though the faithful-image claim and the 100%-scaling-figures-held result are specific to Nokia-provided SR Linux images. Performance testing is explicitly out of scope for containers ("you can't speed test a container"). Next steps stated: CI/CD for every change (templates → CMDB → config → lab → prod) and a Clabernetes cluster to lab the global network. Based on the speaker's slides.

### Network Observability Innovations at the IETF

**Links:** [Slides](https://chnug.ch/chnug003/slides/chnug003-network-observability-innovations-at-the-ietf.pdf) · [Recording](https://www.youtube.com/watch?v=IAJaIFwwkxA)

Speakers: Thomas Graf (Swisscom)

- **Why**: Model-driven streaming telemetry is the direction of travel for every serious network operator, and this talk is a practitioner's map of the actual standards you would build on — from a Swisscom production deployment, not a slide-ware architecture. It answers a concrete ops question: how to get real-time network state without logging into routers, and how to join control-plane, management-plane, and data-plane views into one correlated stream.
- **What**: Three connected pieces. (1) Real-time L3VPN observability by correlating IPFIX (MPLS/SRv6 provider and IPv4/6 customer data plane), BMP (BGP VPNv4/6 RIBs with path-decision and route-policy metadata), and YANG-Push — using BGP standard communities to tag logical connections/connection points and SRv6 VPN SIDs on the IPv6 next-hop to stitch customer flows to services. (2) IPFIX segment-routing coverage: RFC 9160 (MPLS SR labels), RFC 9487 (SRv6 segment lists, endpoint behavior), RFC 9951 (per-hop forwarding-path delay), plus an IOAM direct-export on-path-delay draft leveraging RFC 9378/9197 and enhanced alternate marking (RFC 9341). (3) The YANG-Push-to-data-mesh architecture: a YANG Schema Registry that assigns schema IDs so YANG notifications can flow unchanged through a message broker (Kafka) with semantic validation at the consumer — plus an honest 23-year timeline of YANG/Push standardization, including that RFC 8639/8641 finished in 2019 with no major vendor implementations and that gNMI was taken to IETF in 2017.
- **How**: Subscribe to YANG datastores (periodic for statistics, on-change with sync-on-start for state, per RFC 8641/9196), collect module dependencies via `<get-schema>` and YANG Library, register schema trees centrally, prefix broker messages with schema IDs, and transform BMP messages into YANG-modeled telemetry at the monitoring station per the `ietf-bmp` and message-broker drafts. Node-based flow aggregation joins IPFIX records with control-plane context.
- **Where applicable**: The L3VPN/SRv6 correlation pipeline is Swisscom-specific production, but every mechanism cited is an IETF RFC or active draft (BMP RFC 7854/8671/9069/9972, IPFIX SR RFCs, YANG-Push data-mesh drafts in NMOP/GROW) — so the patterns transfer to any SRv6/BGP shop building a telemetry pipeline. Most valuable if you run VPN services and want per-hop delay and service-level flow context from standards rather than vendor probes. Based on the speaker's slides.

### Building Modern & Scalable DC Fabrics

**Links:** [Slides](https://chnug.ch/chnug003/slides/chnug003-building-modern-scalable-dc-fabrics.pdf) · [Recording](https://www.youtube.com/watch?v=OuGXD0PPRnw)

Speakers: Alperen Akpinar (Nokia)

- **Why**: A useful one-slide-deep map of how AI workloads are rewriting DC fabric requirements — worth the PM's time for the framing and the terminology even though it is a Nokia sales-informed deck. It lays out the scale-up / scale-out / scale-across taxonomy and the specific feature checklist an "AI-ready" Ethernet fabric now needs (DLB, RDMA-aware hashing, DCQCN, multi-plane topologies), which is exactly the vocabulary for evaluating any vendor's AI-networking claims — including Nokia's competitors'.
- **What**: A technology-evolution and requirements talk: speed progression (10/100M → 800G+/1.6T) alongside a protocol progression (STP → BGP/EVPN-VXLAN → UET/uSIDs/DCQCN); AI resetting DC scale (Meta Luleå 30 MW in 2013 → Altoona 500 MW in 2025 → gigawatt-class in 2026); and the three-axis scaling model — scale-up (Nvidia NVLink/NVSwitch, AMD UALink, Broadcom SUE, OCP ESUN), scale-out (InfiniBand, RoCEv2, UEC), scale-across (DCI via 800G ZR/ZR+ coherent optics in C+L band over ~1000 km, 4x400G FlexE bundles, RDMA over WAN, encryption). Concrete detail on GB200 NVL72 intra-rack copper fabric (9 NVLink switches, 18 chips, 144 ports at 100GB/s, 1.8TB/s per GPU) and on why AI traffic differs from traditional apps (imbalanced flows → tail latency → job completion time dominated by slowest GPU). The Nokia product content maps requirements to platforms: 800G/1.6T backend fabrics on 7220 IXR-H5/H6 and 7250 IXR Gen3+, DLB and RDMA-aware (Q-pair) hashing, DCQCN (PFC/ECN) plus MRC, congestion-indicator telemetry, backend multi-tenancy, EDA automation, and deployment archetypes from inference edge clusters through 1K–16K-GPU two-tier clusters to 100K–1M-GPU multi-plane "AI factories."
- **How**: Conceptual/architectural rather than a mechanism — the value is the requirements taxonomy (scalable, lossless, automated for in-DC; maximum capacity and high-frequency congestion-aware steering for DC-to-DC), not any single technique. No empirical evaluation is presented.
- **Where applicable**: The landscape framing is generally applicable to anyone designing or buying AI-era fabrics; the product mapping, feature claims (e.g., DLB/Q-pair behavior, telemetry capabilities), and deployment examples are Nokia-specific and unvalidated — treat them as a vendor's positioning to be checked against your own bake-offs and silicon. Based on the speaker's slides.

## Wildcard

No true wildcards this cycle — with a three-item program, every talk maps directly onto the PM's stated core interests, and padding this tier would add noise rather than signal.

## Themes

- **AI is the organizing problem for DC fabric design.** Even at a regional user group, the fabric talk is framed entirely around GPU clusters — scale-up vs scale-out vs scale-across, JCT/tail-latency reasoning, and the InfiniBand-vs-Ethernet (RoCEv2/UEC/UET) contest — confirming that AI backend networking is now the default lens for DC architecture.
- **Lab-as-code is becoming the primary risk-reduction tool for physical builds.** Proton's story — committing to hardware from a vendor they'd never touched, validated entirely in containerlab — signals that container-based NOS emulation (vs slow VM labs) has crossed the threshold from hobby tooling to production migration methodology, with CI/CD and clustered labs (Clabernetes) as the next step.
- **Streaming telemetry standards are finally ready to build on.** The YANG-Push/BMP/IPFIX stack has matured from specifications without implementations (2019) to production correlation pipelines (2024+); the emerging pattern is schema-registry-governed message brokers ("data mesh") rather than per-vendor collector stacks.
- **Ethernet everywhere, including across DCs.** Both the fabric and observability talks assume an Ethernet/SRv6 end-to-end world — 800G ZR+ coherent DCI carrying RDMA traffic, unnumbered IPv6 BGP fabrics, SRv6 VPN SIDs as correlation keys — continuing the retreat of IB/FabricPath-era alternatives except inside GPU islands.
- **Honest limitations as a credibility signal.** The two operator-fronted talks both included explicit failure catalogs (containerlab's HW-only bugs; YANG-Push's two-decade standardization stall), which is exactly the kind of transferable operational detail that separates practitioner talks from pitches.
