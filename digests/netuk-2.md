<!--
conference: NetUK2 (The Brewery)
type: operator
source_url: https://indico.netuk.org/event/2/
generated: 2026-11-04
registry_key: netuk-2
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NetUK2 (The Brewery)

A small, single-track UK operator event. The program is dominated by
interconnection, physical-layer resilience, and honest failure stories — a
good match for a PM whose core work includes physical DC/WAN systems. Several
sponsor slots (Kubus/Juniper, Arista EVPN overview) and welcome/announcement
items were reviewed and skipped: they are either pitches in disguise or carry
no technical abstract.

## Core

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/21/)

Dr Gerhard Stein (Lead Research Engineer), co-author Thomas Weible (Chief Technology Officer)

- **Why**: As datacenter and DC-interconnect links move to 400G/800G, the
  margin between "link is up" and "link is silently degrading" narrows. This is
  one of the few operator-conference talks that quantifies that margin rather
  than asserting it, and the coherent-vs-PAM4 comparison maps directly onto
  DC/metro/WAN optics decisions the PM makes today.
- **What**: A measurement-driven analysis of how close to a low SNR threshold
  100G/400G/800G transceivers can run while still holding a tolerable BER, and
  how temperature and cable length shift that threshold — used to estimate how
  long a link can reliably sustain a connection between two transceivers.
  Coherent (16QAM) and non-coherent (PAM4) parts are compared head to head
  (write-up based on the abstract and program page; slides are Flexoptix-branded
  and the data was gathered with a Flexbox, so the measurement apparatus is
  Flexoptix tooling).
- **How**: SNR is swept toward the failure threshold while BER is tracked,
  with temperature and cable length as controlled environmental variables, and
  the resulting curves are used to predict link reliability duration rather
  than a binary pass/fail.
- **Where applicable**: Broadly applicable to anyone specifying or
  commissioning 400G/800G optics for DC fabrics or DC-to-metro interconnect —
  the physics is vendor-neutral even if the measurement rig is not. Expect the
  practical numbers to depend on the specific transceiver families tested.

### Slash your cloud network costs with eBPF network monitoring

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/28/) · [Slides](https://indico.netuk.org/event/2/contributions/28/attachments/29/121/multi-zone-network-monitoring-final.odp) · [Recording](https://www.youtube.com/watch?v=h6jysoUwyFE)

Mario Macias, Nikola Grcevski (Grafana Labs)

- **Why**: Cross-AZ data transfer is a large, recurring, and poorly-attributed
  line item for anyone running Kubernetes in public cloud. This is a
  production-tested, OSS-only approach to attributing that cost to pods —
  squarely in the PM's eBPF/Kubernetes observability space.
- **What**: A walk-through of how Grafana Labs cut their own cloud network
  costs using eBPF-based packet-level traffic analysis: identifying which pods
  and workloads generate elevated cross-AZ traffic, with zero application code
  changes and low overhead (write-up based on the abstract and program page
  summary).
- **How**: eBPF performs packet-level analysis in the kernel; the low-level
  flow data is enriched with Kubernetes pod and node metadata so cross-AZ
  traffic can be attributed per workload, regardless of CNI, using only
  open-source tooling. The talk shows how to rebuild the same monitoring stack
  yourself.
- **Where applicable**: Any Kubernetes-on-public-cloud environment where
  cross-AZ egress/transfer billing applies. The cost-saving framing is
  multi-AZ-cloud specific, but the eBPF-plus-pod-metadata attribution technique
  transfers to on-prem K8s traffic visibility generally. Rooted in Grafana's
  own production experience but the method is broadly adoptable.

### Some interesting stuff I found on IX LANs

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/43/)

Ben Cartwright-Cox (bgp.tools)

- **Why**: Every IX fabric is a shared Ethernet broadcast domain, and what
  actually appears on it versus what the AUP forbids is a recurring L2 security
  and hygiene problem. This is empirical, at scale — 100 peering exchanges
  observed from one vantage point — and directly relevant to anyone running or
  consuming IX infrastructure.
- **What**: A survey of "bad" broadcast/multicast traffic bgp.tools has
  observed across ~100 peering exchanges' LANs, an assessment of the real-world
  impact of that traffic, and concrete suggestions for how exchanges could
  police it (from abstract only; the program page notes the slides are an
  evolving version previously shown at EuroIX).
- **How**: bgp.tools passively observes IX LANs as part of its normal data
  collection, so the findings are longitudinal, real traffic rather than a lab
  reproduction.
- **Where applicable**: Broadly applicable — the failure modes of shared L2
  domains (stray ARP/ND, unwanted multicast, leaking protocols) are not
  IX-specific; the same lessons apply to any large shared switching fabric.
  The mitigation proposals are aimed at IX operators, but members can use the
  findings to check their own edge hygiene.

### Detecting Non-Spoofed Traffic at ISP Ingress Points

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/37/) · [Slides](https://indico.netuk.org/event/2/contributions/37/attachments/32/103/Identifying_Non_Spoofed_Traffic_ISP_Ingress.key) · [Recording](https://www.youtube.com/watch?v=T5Ys223Mt7M)

Petros Gigis (University College London)

- **Why**: "Traffic from source X arriving at the wrong ingress" is a daily
  operator puzzle: is it a route leak, a BGP hijack, a commercial-agreement
  mismatch, or just spoofed background noise? This talk offers a genuinely
  clever, deployable test to tell them apart — a small research idea with
  unusually direct operational payoff.
- **What**: Penny, a traffic checker that distinguishes non-spoofed traffic
  aggregates arriving at unexpected ingress points from spoofed ones, with a
  planned open-source release (openPenny). Beyond the core detection, the tool
  is positioned to surface routing misconfigurations, BGP-hijack indications,
  upstream/downstream packet loss, abruptly terminated TCP flows, and
  load-balancing behaviour (write-up based on the abstract and program page
  summary).
- **How**: The mechanism is elegant: when new traffic appears at an unexpected
  router, drop a few TCP packets. Non-spoofed flows retransmit; spoofed ones
  don't. The research contribution is making that robust — minimising harm to
  legitimate flows, tolerating path changes and remote loss that look like
  drops, and resisting spoofers who adapt to evade the probe.
- **Where applicable**: Any ISP or large operator with multiple ingress points
  and BGP-speaking neighbors; the technique is TCP-dependent and
  ingress-diversity-dependent, so it fits transit/peering-heavy networks best.
  Research-stage (UCL) but explicitly aimed at open-source operator adoption.

### How the Internet routed around Cable Damage in the Baltic Sea

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/25/) · [Slides](https://indico.netuk.org/event/2/contributions/25/attachments/26/112/BALTIC%20SEA%20CABLES%20NETUK%20%28Final%29.pptx) · [Recording](https://www.youtube.com/watch?v=LYUe3_2-g3o)

Alastair Strachan (RIPE NCC)

- **Why**: Submarine cable cuts (several in the Baltic recently under
  suspicious circumstances) are the canonical physical-layer WAN failure. This
  talk uses actual measurement data to show what happens to latency, loss, and
  routing when a regional cable plant degrades — evidence rather than folklore
  about redundancy.
- **What**: An analysis of the impact of outages affecting the BSC East-West
  and C-LION1 cables, using RIPE Atlas measurements to track latency shifts,
  packet loss, and rerouting before and after the incidents. The program page
  summary reports the headline finding: only minor latency increases were
  observed, with inter-domain and intra-domain rerouting maintaining
  connectivity with minimal disruption.
- **How**: RIPE Atlas probe meshes provide continuous latency/loss time series
  across affected paths; changes around the incident window reveal which
  traffic moved, where it moved to, and how quickly.
- **Where applicable**: The specific event is Baltic-regional, but the
  methodology (Atlas-based before/after analysis of physical failures) is
  reusable by any operator for their own resilience validation, and the
  conclusion — meshed redundancy absorbs single/few cable failures — transfers
  to DC/WAN interconnect design generally.

### Sorry we messed up

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/24/) · [Recording](https://www.youtube.com/watch?v=0YPelOFDlo0)

Stefan Funke (Inter.link)

- **Why**: A route leak that leaked "everything to everyone" is exactly the
  class of BGP incident every operator dreads, and this one was triggered by a
  seemingly innocuous change (renaming RCF functions) interacting with an
  Arista behaviour. Postmortems like this are the highest-value content at an
  operator event: the lesson transfers to anyone using vendor scripting/RCF
  for config automation.
- **What**: A postmortem of a global route leak at a transit provider: the
  motivation for the change, how configurations are rolled out at Inter.link,
  why renaming Arista RCF functions produced unexpected behaviour and a global
  leak, and how it was detected and fixed (from abstract and program page
  summary; the speaker notes it is deliberately high-level, aimed at a general
  NOG audience).
- **How**: Narrative postmortem: intended change → rollout path → surprise
  behaviour → blast radius → fix. The interesting mechanism is the interaction
  between operator-managed RCF function names and vendor handling of them.
- **Where applicable**: The specific bug is Arista EOS/RCF-specific, but the
  transferable lessons — "cosmetic" config changes are not cosmetic, function
  naming indirection can silently change policy semantics, and rollout
  safeguards need to cover refactors — apply to any network with scripted
  configuration generation. Inter.link's global transit footprint made the
  blast radius unusual; smaller networks leak less far but the same way.

### Power Consumption Considerations in Metro Optical Networks

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/22/) · [Slides](https://indico.netuk.org/event/2/contributions/22/attachments/23/113/Power_SJ%20%282%29.pptx) · [Recording](https://www.youtube.com/watch?v=vo7Y4uRPPt8)

Steve Jones (Unicorn Farmer)

- **Why**: Optical transport power draw is becoming a hard constraint in DC and
  metro builds — pluggable choices, coherent DSPs, and port counts all trade
  against watts per bit. This pairs naturally with the 800G transceiver talk
  and the AI-DC power talk in the same program.
- **What**: A look at the growing power needs of a metro optical network and
  the options available to mitigate them. This abstract is unusually thin — the
  program text literally says "Draft Powerpoint presentation attached," with the
  page summary adding only that it covers mitigation options — so expect an
  experienced-operator perspective piece rather than a paper (from abstract
  only).
- **How**: Not described in the program material; based on the speaker's
  background this is expected to be a practitioner's walkthrough of where the
  power goes in a metro optical plant and what levers exist.
- **Where applicable**: Metro/regional optical operators and anyone building
  DC-to-metro interconnects. Org-agnostic in principle, but with so little
  published detail, judge the talk on delivery.

## Adjacent

### High Level Perspectives on Artificial Intelligence Data Centers

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/23/) · [Slides](https://indico.netuk.org/event/2/contributions/23/attachments/24/97/2025-06%20High%20Level%20Perspectives%20on%20AI%20-%20NetUK-Final.pptx) · [Recording](https://www.youtube.com/watch?v=zZW_g0xr-fs)

Geoff Bennett (Nokia)

- **Why**: AI training clusters are reshaping DC networking demand — and the
  binding constraint is increasingly electrical power, not optics or silicon.
  For a PM whose portfolio spans physical DC networking, understanding the power
  budget conversation around AI DCs is near-term essential context.
- **What**: A tutorial on resource trends for AI datacenters, focusing on power
  demand: how hyperscaler AI compute growth strains grids and water supplies,
  how published hyperscaler power strategies match up against realistic
  sources, and an assessment of enhanced geothermal and nuclear options
  (from abstract only).
- **How**: Synthesis of published trends and vendor/ hyperscaler power
  strategies rather than new measurements — a well-informed survey talk.
- **Where applicable**: Context for anyone planning DC capacity, siting, or
  fabric strategy over the next planning cycle. Vendor-delivered (Nokia), and
  explicitly high-level, so treat it as a framing talk, not a technical deep
  dive.

### BNG Blaster Hands-On Training

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/19/)

Alex Le Heux, Christian Giese

- **Why**: Automated, reproducible control-plane testing of access/routing
  gear is something most operators hand-roll badly. BNG Blaster is open-source,
  CICD-friendly, and this is a hands-on session with a pre-configured DUT —
  the kind of adoptable tooling an operator-focused program should surface.
- **What**: A practical workshop on BNG Blaster, an open-source testing tool,
  covering access protocols (PPPoE, L2TP) and routing (ISIS, BGP) against a
  provided device under test, with exercises attendees can customise or extend
  (from abstract only).
- **How**: Each participant SSHes into a pre-configured test environment with
  a DUT and works through provided or self-built test scenarios; prior
  familiarity via previous DKNOG/DENOG talks is recommended.
- **Where applicable**: Primarily for operators of subscriber/edge
  infrastructure (BNGs, access concentrators) and vendors testing such gear;
  the general pattern — open-source protocol-level test harness in CI —
  transfers to any environment doing conformance/regression testing of network
  gear.

## Wildcard

### Carbon-Aware Routing: Metrics and Challenges

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/29/) · [Slides](https://indico.netuk.org/event/2/contributions/29/attachments/30/91/NetUK_SawsanElZahr.pptx) · [Recording](https://www.youtube.com/watch?v=Ikq5TOg1nwQ)

Sawsan El Zahr (University of Oxford)

- **Why**: Not a core interest for this PM, but carbon-aware routing is an
  emerging subfield that could eventually change link costing and TE policy the
  way latency-based TE did. It also connects directly to two other sessions in
  this program (metro optical power, AI DC power), making it part of a real
  trend rather than an outlier.
- **What**: Research on making fixed wired networks carbon-aware: which
  carbon-related metrics can serve as link costs in link-state routing, what
  realistic topologies/traffic/grid-carbon-intensity data show about their
  limits, and CATE, a heuristic carbon-aware traffic engineering algorithm
  combining grid carbon intensity with router dynamic power draw and port
  power-down. The honest headline: no silver bullet, but promising directions
  that require no new router hardware (from abstract only).
- **How**: Carbon-intensity signals and per-router power models feed a link
  cost/TE heuristic that reroutes or powers down ports to reduce emissions
  without equipment changes.
- **Where applicable**: ISP-scale fixed networks with geographically diverse
  paths and dynamic power features in their routers; benefits are largest where
  grid carbon intensity varies meaningfully across a footprint. Research-stage
  (Oxford), evaluated on realistic but synthetic topologies rather than a named
  production network.

### How to wash your servers (handling extremes of weather as a WISP)

**Links:** [Abstract](https://indico.netuk.org/event/2/contributions/26/) · [Slides](https://indico.netuk.org/event/2/contributions/26/attachments/27/107/250109_WISP_Diaries_Ep2_How_to_wash_your_servers_NETUK_Edit.odp) · [Recording](https://www.youtube.com/watch?v=miXKr6ug3_E)

Oli Stockman (Fram Broadband Ltd/NGA Connect Ltd/Superhero Broadband)

- **Why**: Outside the PM's core areas, but this is a pure
  physical-infrastructure survival story: running a network when your office
  and primary POP are under four feet of floodwater. The lessons about
  physical vulnerability of head-end sites generalize to any DC or POP
  operator thinking about site risk.
- **What**: A long-form talk on operating an outdoor-heavy WISP through wind,
  snow, heat and cold, centred on the October 2023 Storm Babet floods — how the
  network was kept running with the primary POP flooded, and the lessons
  learned (from abstract only).
- **How**: First-person operational narrative — what failed, what was
  improvised, and what was changed afterwards.
- **Where applicable**: Very org- and climate-specific (UK WISP, single-site
  POP, river flooding), so the specifics do not transfer directly. The
  transferable part is the thought exercise: what does your critical-site
  failure plan look like when the site itself is the outage?

## Themes

- **The physical layer is back as the failure domain.** Submarine cable cuts,
  flooded POPs, and SNR margins on 800G optics — three separate sessions
  converge on physical infrastructure as the thing that actually breaks, and on
  how much design margin (redundant paths, headroom) operators really have.
- **Energy is becoming a first-class network design input.** AI DC power
  budgets, metro optical power draw, and carbon-aware routing form a coherent
  thread: watts (and their carbon intensity) are joining latency and cost as
  optimization objectives.
- **eBPF has moved from novelty to cost engineering.** The Grafana talk is
  representative: eBPF plus Kubernetes metadata used not for security or
  debugging glamour, but to put numbers on a cloud bill line item.
- **Measurement-driven debugging and honest postmortems dominate.** Penny's
  drop-and-watch-retransmissions test, RIPE Atlas cable-cut analysis, bgp.tools'
  IX-LAN observations, and Inter.link's route-leak confession all share a
  pattern: instrument reality, report what actually happened, publish it.
- **The UK NOG scene is healthy but small-scale.** Most talks are UK/regional
  operators or UK-based research (UCL, Oxford); hyperscale techniques appear
  mainly via vendors (Nokia, Arista), so treat the practitioner content here as
  bottom-up rather than hyperscaler-derived.
