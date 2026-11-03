<!--
conference: NLNOG Day 2026 (Hilversum)
type: operator
source_url: https://nlnog.net/events/past-events/nlnog-day-2026/
generated: 2026-11-02
registry_key: nlnog-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NLNOG Day 2026 — Digest

A compact, single-track operator program. No abstracts were published; every write-up below is grounded in the actual slides extracted for this run. Nine items total; one (the NLNAM community announcement) carries no technical content and is skipped.

## Core

### VPP eVPN Controlplane

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/4a_-_IPng_Networks_-_eVPN_NLNOG26.pdf) · [Recording](https://youtu.be/oZUfbciI2Ww?si=0XGdNizxOAA00t7x)

Pim van Pelt (IPng)

- **Why**: The most substantive talk for anyone working on DC/WAN fabric software. It demonstrates that a fully open-source, commodity-hardware eVPN fabric — DPDK/VPP dataplane plus BIRD control plane — can run a real production network (IPng operates AS8298 with 22 VPP/BIRD routers and ~2,200 BGP adjacencies), not just a lab.
- **What**: A complete open-source eVPN stack: an eVPN management/control plane for VPP, a custom `vppevpn` protocol for BIRD, and a management plane (`vpp-evpn` / `epvnd` daemon) that orchestrates eVPN services across Mellanox BlueField DPUs at scale targets of O(100) routers, O(1,000) L3 subnets, and O(10,000) P2MP L2 segments.
- **How**: VPP provides the building blocks (bridge domains, BVIs, VXLAN tunnels, split-horizon groups, learn/flood disabled on tunnels); BIRD speaks BGP eVPN NLRI (MAC/IP/IMET routes, RD/RT, RFC 5512 encapsulation ext-communities for VXLAN) against route reflectors, and the new `vppevpn` protocol reconciles VPP state with BIRD every N seconds — creating tunnels from IMETs, programming L2FIB from MAC routes. A per-DPU daemon adds a healthchecker (CARP/HSRP-style multicast IPv6 probes), gRPC endpoint, and Prometheus metrics; the whole thing interoperates with Arista EOS, Juniper, Cisco, and Centec VTEPs.
- **Where applicable**: Broadly adoptable — all components are open source (VPP 26.06+, BIRD 2.19 with a patch) and the demo includes multi-vendor VTEPs, so it's not an island. Performance claims (100Mpps+/100Gbps+ per node on commodity x86) are IPng's own production numbers, and the scale figures are IPng-specific, but the architecture transfers to any operator willing to run DPUs as eVPN PE devices.

### The Art of Making Vendors Agree: Lessons from Interoperability Testing

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/3a_-_Patrick_Prangl_-_The_Art_of_Making_Vendors_Agree.pdf) · [Recording](https://youtu.be/M4_AoyEnGZs?si=GWDlR-iMpbh_PMRi)

Patrick Prangl (Arista)

- **Why**: Directly relevant to running multi-vendor DC fabrics. It explains how EANTC's Berlin interop event works, what actually failed when vendors met, and what the 2026 test scope says about where DC/SP technology is heading (EVPN-VXLAN, SR-MPLS/SRv6, and a brand-new AI/UEC testbed).
- **What**: An operator-usable guide to reading the EANTC interoperability report — plus concrete failure examples from the 2026 event, including malformed IS-IS TLV 222 (MT routing, RFC 5120) that led to corrupted LSPs, missing SRv6 Capability TLV 25 breaking backup-path calculation, and TI-LFA initially steering SRv6 routes to DROP. Also useful maturity signals: OISM (overlay multicast) control planes converge but data planes diverge; NOS-only vendor participation is shrinking.
- **How**: Multi-vendor test beds (EVPN-VXLAN, EVPN-SR, MPLS-SR, SRv6, SDN/PCEP) run over two weeks with EANTC-validated results; the report only includes successful tests, and config/image details are reported to EANTC but not published. The talk walks through how ambiguous RFC language ("SHOULD", reserved bits) turns into real interop bugs.
- **Where applicable**: The EANTC report and methodology are vendor-neutral and freely usable by anyone doing DC fabric procurement or PoCs. Speaker is an Arista systems engineering lead, so the framing leans toward a participant's perspective, but the content is the test event, not a product pitch. Explicit caveat from the speaker: passing interop tests does not replace your own PoC.

### Lessons from 10 months of ASPA

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/9a_-_Tim_Bruijnzeels_-_Lessons_from_10_months_of_ASPA.pdf) · [Recording](https://youtu.be/xII4eXXALWY?si=9qU76kmrB23ytzpT)

Tim Bruijnzeels (RIPE NCC)

- **Why**: Routing security is squarely in the PM's network-security scope, and this is the rare talk with actual deployment telemetry rather than aspiration. It gives a clean mental model of what ROA, ASPA, and BGPsec each do and don't protect against, plus real uptake numbers.
- **What**: A status report on ASPA (AS Provider Authorization) ten months in: how ASPA objects work, the AS0 convention for transit-free networks, valley-free path validation from both ends of a path, and the deployment picture. Key data points: signing UIs landed across Krill, RIPE NCC, ARIN, and APNIC through 2025–2026; relative signing uptake as of 15 Aug 2026 is 2.2% of registered ASNs worldwide, 4.6% in the RIPE region, 6.1% in NL, and 10.9% in CZ. Validation is coming: supported in BIRD, OpenBGPd, and NIST-BGP-SR, with Cisco IOS-XR in test; YYCIX was the first to drop ASPA-invalid (2023).
- **How**: ASPA objects are RPKI-signed by a customer AS listing its provider ASes; validators feed routers over RPKI-RTR (no router crypto), and routers evaluate plausible up-ramp/down-ramp paths. The talk shows working config: `deny quick from ebgp avs invalid` in OpenBGPd, and `aspa_check_downstream()` filters in BIRD 3.2.1+ as deployed in the RIPE meeting network. RIS-based path analysis toward AS0 networks shows how common invalids already are.
- **Where applicable**: Any operator with an ASN. Actionable today: sign ASPAs (include all transits, maintain them), and plan to reject invalids — with the explicit warning that ASPA is a "sharp tool" and people will drop invalids. Not org-specific; the uptake figures are global/regional RIR statistics.

### How to change the Internet itself?

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/8a_-_Job_Snijders_-_How_to_change_the_internet_itself.pdf) · [Recording](https://youtu.be/qHV_IZJxIKE?si=PzT659fNaWGa4dBU)

Job Snijders

- **Why**: Part retrospective on routing-security wins (Large Communities, RPKI ROV, ASPA design), part forward look at a genuinely new piece of RPKI infrastructure — Erik Synchronisation — from someone who ships RPKI validator code. The process lessons for effecting protocol change are a bonus for anyone who has to drive standards adoption.
- **What**: Four case studies: how BGP Large Communities finally solved a problem IETF discussion had failed to close for 15+ years; how RPKI ROV deployment snowballed from the Netherlands; why ASPA deliberately unified IPv4/IPv6 upstream handling against academic objections; and why rsync and RRDP are both poor fits for RPKI repository distribution and what replaces them. The recurring thesis: minimum viable solutions, implementer preferences over academic elegance, and relentless evangelization.
- **How**: Erik Synchronisation combines Merkle trees, content-addressable storage, and concurrency control to take the best of rsync (stateless, jump-to-latest, delta-only) and RRDP (pre-calculated static content over HTTP). The key differentiator: anyone can run an "Erik Relay" mirroring all global RPKI data, and clients can rotate between relays for robustness — solving the "you can't force the origin to sit behind a good CDN" problem of RRDP.
- **Where applicable**: The RPKI/Erik material matters to every RPKI publisher and validator operator, and permissionless incremental deployment is the design goal. The case-study methodology (pick a problem, find who owns the solution space, build a PoC, teach it) is general. No org-specific constraints.

## Adjacent

### The Hitchhiker's Guide to IPv6: Don't Panic… We've Only Got 30 Minutes

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/2a_-_Nicole_Wajer_-_The_Hitchhiker_s_Guide_to_IPv6__Don_t_Panic_We_ve_Only_Got_30_Minutes.pdf) · [Recording](https://youtu.be/3BcJobyHcag?si=6JYrb_80YVKXBMAI)

Nicole Wajer (Cisco)

- **Why**: Practical IPv6 operational hardening in the trenches — the kind of small failure modes (ACLs, neighbor discovery, wireless RA handling) that bite during dual-stack or IPv6-only rollouts. Relevant background for anyone running DC edge or enterprise access alongside the fabric.
- **What**: A war-story tour of IPv6 gotchas: IPv6 ACLs have *implicit* permits for ND-NS/ND-NA (so "tightening" an ACL can still break or unexpectedly pass neighbor discovery); a GUA-loss case caused by SSID jumping and stale neighbor cache; and a case where Windows + Cisco Secure Client stopped receiving unsolicited RAs, killing IPv6 after ~15 minutes until a bug fix shipped. Closes with an IPv4-to-IPv6-only migration path slide.
- **How**: Diagnosis via neighbor-cache state machines, RA/RS behavior on interface bounce, and Wireshark captures — emphasizing that IPv6 failure modes are control-plane (ND/RA) rather than the IPv4-style ARP debugging people reach for.
- **Where applicable**: General dual-stack/enterprise-wireless advice, not org-specific. Speaker is a Cisco evangelist and the war stories involve Cisco gear and Cisco Secure Client specifically, so some fixes are vendor-fix rather than technique; the diagnostic approach transfers anywhere.

### Kubernetes for Network Engineers

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/7a_-_Egbert_Verhage_-_Kubernetes_for_Network_Engineers.pdf) · [Recording](https://youtu.be/TkUj9hZs3ys?si=Fyz5EF9WpxXPrTkF)

Egbert Verhage (NIT Solutions)

- **Why**: For the PM this is mostly foundational, but it is a well-structured, demo-driven (asciinema recordings) walkthrough of exactly the K8s networking primitives in their interest area — CNI choice, MetalLB and Cilium BGP announcements, IPAM (pod/service CIDRs, Whereabouts), and Multus/SR-IOV — useful as enablement/reference material for network teams they work with.
- **What**: A bottom-up tour of Kubernetes networking aimed at network engineers: pods and their disposable IPs, Services (ClusterIP/LoadBalancer/NodePort), namespaces (explicitly *not* a network boundary), pod-CIDR vs. service-CIDR, flannel as a first CNI, then progressively more network-y builds: MetalLB for bare-metal LoadBalancer services, swapping to Cilium to announce pod pools and LoadBalancer IPs over BGP without node masquerade, and Multus to attach extra interfaces (e.g., macvlan) to pods. Brief pointers to KubeVirt, Rook, SR-IOV CNI, and Whereabouts IPAM.
- **How**: Live demos via asciinema casts: deploy flannel, apply an IP pool with MetalLB, then configure `ciliumbgpadvertisements.cilium.io` CRDs to originate BGP for pod and service prefixes, and Multus for multi-interface pods.
- **Where applicable**: Broadly applicable — vanilla kubeadm clusters, no specific vendor platform. Introductory level: for someone already working on Cilium/K8s networking daily this covers familiar ground, with the Cilium-BGP and Multus demos being the most transferable bits.

## Wildcard

### Internet exchanges in space

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/10a_Iljitsch_van_Beijnum_-_IXes_in_space_v05.pdf) · [Recording](https://youtu.be/PW6IcB7dOW4?si=MtDAUivdef9ZzQPm)

Iljitsch van Beijnum

- **Why**: Genuinely novel — an ESA-commissioned study (STARS, prime SINTEF) on whether Internet exchanges can be built on LEO satellites using optical inter-satellite links, with real BGP simulation results. It stress-tests basic protocol assumptions (BGP convergence, layer-2 vs. layer-3 IX models) in an environment where topology changes at 7 km/s.
- **What**: A feasibility analysis of IX-in-space: motivations (removing the ground bottleneck, cheaper/faster interconnection between LEO constellations like Starlink/OneWeb/Leo/IRIS², new use cases such as alliance-flexible diplomatic peering), hardware reality-check (a Tbps-class 32-port switch at ~€6,000/11 kg/1500 W plus an ARM route server, radiation-hardened), and the finding that satellites move slowly *relative to each other*, so handovers can be hours apart. SINTEF's BGP simulation showed ~180-second link-down detection; the speaker's FreeRangeRouting-in-Docker setup with tweaked timers plus BFD was "immediately much better." Follow-up proposals include embeddable "PIGS" (Programmable Internet Gateway Subsystems) modules for other satellites, paralleling NASA's Space BACN.
- **How**: Optical ISLs (~100 Gbps laser links between satellites) replace fiber; BGP sessions are taken down proactively just before leaving communication range; and — the notable architectural conclusion — a mature space IX would almost certainly be layer-3, because a dozen-plus IX satellites each peered with many "peering satellites" would exhaust any sane layer-2 addressing plan. A live interactive demo was made available.
- **Where applicable**: Currently a study/simulation, not a deployed system — early-stage and ESA/European-program specific. The BGP-over-dynamic-topology lessons (BFD, proactive session teardown, L3 vs. L2 peering economics) generalize to any highly-dynamic interconnect problem.

### Networking without the Internet

**Links:** [Slides](https://nlnog.net/events/nlnog-day-2026/presentations/5a_-_Marlies_Heijkoop_-_Networking_without_the_Internet.pdf) · [Recording](https://www.youtube.com/watch?v=QXxfAU91Ejk)

Marlies Heijkoop

- **Why**: Not a technical deep dive and it says so upfront — but a thought-provoking look at a nationwide license-free LoRa mesh (Meshcore) that achieves near-countrywide coverage on cheap hardware, and a candid perspective piece on staying engaged with networking as a craft (from a founding architect at Gomibo/Belsimpel, speaking openly about burnout).
- **What**: An accessible overview of the Dutch Meshcore network: companions (end devices, e.g., nrf52-based Heltec T114) and solar-powered repeaters (Heltec v4, SenseCAP), packet characteristics (tiny, text-only, no delivery guarantees — "the Two Generals have nothing like TCP sequence numbers"), and an honest assessment of the flooding model (worse than an Ethernet hub — even the sender hears its own frame back). Practical uses are deliberately modest: Home Assistant integration, out-of-band "is it my house or is it Ziggo" checks, and last-resort communication. The talk's real argument: play with networks for fun to keep the flame burning.
- **How**: LoRa modulation giving long range at very low power and terrible SNR, with repeaters re-broadcasting everything they hear (no spanning tree — counter-intuitively it works). Concrete recommendations: flash "Dutch Meshcore" firmware, buy a companion-plus-repeater pair rather than a standalone cyberdeck, and there's an NLNOG channel on the mesh.
- **Where applicable**: Hobbyist/community infrastructure in the Netherlands specifically (Meshcore firmware variant, national radio settings), not production tooling — the speaker explicitly says you won't need this for monitoring prod. Worth it as a working example of an extreme-constraint mesh network and its emergent behavior.

## Themes

- **Routing security is shifting from theory to deployment data.** Two of nine talks are on RPKI/ASPA, and both ground themselves in real numbers (regional signing uptake, path-validity analysis from RIS) rather than advocacy — plus a concrete new distribution protocol (Erik Synchronisation) aimed at the RPKI ecosystem's weakest operational link.
- **Open-source dataplanes are in production, not just conference demos.** The VPP + BIRD eVPN talk is the standout: a carrier network of 22 routers built from open source on commodity DPUs, interoperating with major NOS vendors, with stated scale targets and failover automation.
- **Multi-vendor DC fabrics remain hard, and interop testing is the canary.** EANTC remains the only global event of its type; its 2026 scope added an AI/UEC testbed, signaling that AI-networking protocols are next in line for the ambiguous-RFC interop problems that have long plagued EVPN/OISM.
- **BGP keeps escaping the WAN.** It shows up in three very different contexts this year: originated from Kubernetes via Cilium/MetalLB, redesigned for LEO satellite IXes, and reshaped by ASPA path validation — the same protocol being pushed in three directions at once.
- **IPv6 content has matured from migration strategy to operational hygiene.** The IPv6 talk is about ACL footguns, neighbor-cache state machines, and RA bugs — the unglamorous long tail of dual-stack operation, including a pragmatic IPv6-only path.
- **Operators are making room for joy and community.** A LoRa mesh talk that argues for tinkering as burnout recovery, and a network-automation meetup (NLNAM) growing a local community — small signals that the human layer of network operations is getting explicit attention on the agenda.
