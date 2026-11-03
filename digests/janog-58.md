<!--
conference: JANOG 58 Meeting
type: operator
source_url: https://www.janog.gr.jp/meeting/janog58/program-timetable/
generated: 2026-11-03
registry_key: janog-58
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# JANOG 58 Meeting — Digest for networking/identity PM

JANOG 58 (Matsuyama, July 2026, theme: “技術の成熟と次代への継承” / maturing technology and handing it to the next generation) leaned heavily into two things this cycle: the physical consequences of AI infrastructure (liquid-cooled rack-scale GPU, 800G cabling, optics) and the productionization of AI agents in network operations. Both map directly onto this PM's core interests.

## Core

### プライベートクラウドを”継承”する ― Cycloudのネットワークを全面刷新した話

小障子尚太朗（サイバーエージェント グループIT推進本部 CIU）

- **Why**: A rare full postmortem of a ~20-year-old private cloud network rebuilt from scratch — the failure modes of a long-lived DC fabric (centralized firewall chokepoints, vendor-proprietary redundancy blocking replacement, manual VRF/subnet provisioning) and the standards-based fixes.
- **What**: CyberAgent's CIU rebuilt its "Cycloud" private cloud with a new region (opened April 2026) fixing: tenant isolation moved from per-subsidiary VRFs to per-project VPCs; the firewall removed from the traffic path; 10G-based DCI replaced; M-LAG/HA/chassis-cluster replaced with EVPN multihoming and anycast gateways.
- **How**: VPCs implemented with EVPN Route Type 5 (IP prefix routes) plus vrf-import/export for VPC peering — inter-VPC traffic bypasses the firewall and is controlled by security groups; EVPN Multihoming for L2 leaf redundancy; anycast gateways for active-active VM default gateways; NAT concentrated at PoPs; inter-DC connectivity via 波長貸し (wavelength service) / 400G-ZR; VRF/subnet provisioning automated. L2 is deliberately confined to a single DC (AZ-style), no stretched L2, no duplicate IPs.
- **Where applicable**: CyberAgent-specific scale and history, but the design decisions (RT5 for VPC peering, dropping DSR for an N+1 LB architecture, choosing network appliances over hypervisor-based VPC for maintainability) transfer to any private-cloud/AZ fabric design. Explicit trade-off: ASIC resource limits (VRF/VLAN/MAC-IP scale) vs. the ops simplicity of "buy it and it works."

### 人のための自動化がAIエージェント運用への道を拓く ― IOWN APN × VXLAN/EVPNをまたぐマルチレイヤ抽象化の実践

**Links:** [Slides](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-automation-yoshi-suzuki-01.pdf) · [Recording](https://www.youtube.com/watch?v=45OktsTp6zA)

芳政信、鈴木佑輔（NTT西日本）

- **Why**: Directly hits the PM's DC interconnect + automation interests: how to operate a 3-site distributed-DC fabric (L1 photonic wavelength paths + VXLAN/EVPN overlay) with a tiny team, and how the abstraction layer built for humans doubles as the interface for AI agents.
- **What**: NTT West runs a distributed DC backbone on IOWN APN (Fujitsu/NEC/Ciena optical transport) with Cisco Nexus VXLAN/EVPN overlays. The problem: wavelength paths and overlays are built/changed as separate systems with separate procedures, change/rollback is per-case and siloed, and physical-to-logical mappings are maintained by hand. Their fix is a controller API with three pillars: (1) a multilayer control-integration API — set up a wavelength path and VXLAN overlay with a handful of simple parameters; (2) cross-vendor transaction management with automatic rollback; (3) a unified information-retrieval API over controller config, topology, and per-device live status.
- **How**: Complex vendor-specific parameters (shelf/slot/port, OTU/ODU/OTM optics concepts, VNID/MP-BGP/EVPN) are abstracted behind a small JSON REST surface backed by a YANG DB of physical inventory; wavelength assignment picks unused λ via NETCONF queries; the same simple API + transactional consistency + live-state retrieval is argued to reduce AI-agent inference-error risk, and they demo an agent doing natural-language information gathering, config change, and status confirmation across the multilayer environment.
- **Where applicable**: IOWN APN-specific as deployed, but the architecture pattern — few-parameter multilayer API, transactional rollback, unified state retrieval as the substrate for both human and agentic operation — is broadly applicable to any multilayer/multivendor DC-WAN environment.

### Rack-Scale GPUサーバーのNW設計と運用までの苦悩

**Links:** [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/j56-lt4.pdf) · [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-rack-scale-gpu-%E5%86%85%E7%94%B0-%E6%B3%B0%E5%BA%83-%E5%BC%B5-%E6%9C%9D%E7%A8%8B-1.pdf) · [Recording](https://www.youtube.com/watch?v=hSLDQ12By9Y)

内田泰広、張朝程 ほか（ソフトバンク）

- **Why**: First-build lessons from rack-scale GPU clusters — the physical constraints (liquid cooling, CDU/manifold, ORv3 racks) that now shape network design rather than the other way around.
- **What**: SoftBank's first large-scale rack-scale GPU server build, covering how physical constraints were reflected into the network design, layout optimization to compress build time, and the operational issues that surfaced (breakout cabling pain, liquid-cooled-rack-specific problems, link flaps and transceiver triage methods, multi-tenant realization).
- **How**: The companion material (JANOG56 follow-on on liquid cooling) details why water-cooled switches became necessary: next-gen 102.4Tbps Tomahawk-class ASICs with 1.6Tbps ports (~25–30W/port, transceivers alone ~1.9kW per 64-port switch) exceed air cooling; liquid-cooled servers must be bought as validated rack solutions (manifold + CDU), third-party switches can't just be dropped into another vendor's rack, and coolant variables (flow rate, pressure, valve tuning, water temperature, pH, connector shapes) are mostly proprietary. Their asks: reference architectures for liquid-cooled switch integration (which racks/CDUs are validated), and ultimately liquid-cooling standardization (OCP ACS / ORv3 direction).
- **Where applicable**: SoftBank-specific AI DC, but the constraint list — rack power (50–150kW+ vs. the traditional few-kW–20kW rack), 200G/400G/800G interfaces, liquid-cooling vendor lock-in, transceiver/link-flap field triage — is what every first AI-DC build is hitting. Practical and transferable.

### AIインフラ時代のデータセンター内光配線の実践知 ～高密度実装の課題と解決策～

井上喬視（さくらインターネット）、菊地秀夫（TWCCパートナーズ／光配線コンサルタント）

- **Why**: The most concrete cabling-heavy talk in the program — photo-rich practice from one of Japan's largest GPU clouds, updating JANOG56's cabling session with a year of new pain.
- **What**: Sakura Internet's AI infrastructure build (Tsubame/SakuraONE-class: H100/H200/B200 clusters, TOP500-ranked, liquid-cooled container data centers) and how optical cabling design determines operability: in containers, liquid cooling raises per-rack server density (2 to 4–5 racks of servers), pushing a single build toward ~30,000 fiber cores with low ceilings and coolant piping competing for rack space.
- **How**: Concrete techniques: 800G-SR8 over multimode MPO16 APC for short leaf-spine runs (fewer fibers), symmetric rack layouts around spine switches so cabling flows don't cross, high-density 144-fiber MPO/LC termination units, slack-absorption trays, thin-diameter multi-fiber MPO cables, spine-port partitioning (left half serves left, right half serves right), deliberately accepting "re-pull rather than replace" for failed trunk cables, and spine switches placed in adjacent racks with leaves flanking them. Their second-generation container (B200, ~1,100 GPUs, Arista 7060X6 leaf-spine with EVPN/VXLAN + RoCEv2, partial LPO transceiver adoption, deep-buffer Jericho2C+ for storage) incorporated improvements from gen 1.
- **Where applicable**: Container-DC and GPU-cluster specific, but the cabling techniques (MPO multi-fiber strategy, WDM optics for core reduction, layout-for-routability, LPO adoption experience) transfer to any high-density 800G build. The framing — cabling is now a first-class design input, not "later work" — is the takeaway.

### 爆発するMACアドレスとの戦い EVPN VESPA/仮想イーサネットセグメントとProxy ARPの活用

**Links:** [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/06/janog58-pr-mac-address-explosion-tsuchiya-00.pdf) · [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-mac-address-explosion-kawakami-yamamoto-00.pdf) · [Recording](https://www.youtube.com/watch?v=2OhKM2dhjvE)

土屋師子生（アリスタネットワークスジャパン）ほか

- **Why**: MAC table scale is quietly returning as a DC/campus problem — server density per node keeps rising per Moore's law while per-VM service specs stay flat, plus containers; on campus, MAC randomization (iOS 14+/Android 11+, rotating addresses in Win11/iOS18/macOS15) breaks MAC-based auth, port security, DHCP/IPAM planning, and analytics.
- **What**: A solution for environments targeting ~500,000 wireless/VM clients across ~30,000 access devices: EVPN VESPA (Virtual Ethernet Segment with Proxy ARP) — EVPN multihoming extended so Ethernet Segments can be built dynamically over tunnels (VXLAN VTEPs) instead of static physical interfaces, with ESI Type-6 encoding carrying the AP's VTEP IP and a gateway Set ID.
- **How**: Access points act as L2 MAC proxies; VESPA gateways use a virtual VTEP (shared anycast loopback) and maintain ARP entries for wireless clients, refreshed by AP-generated GARPs and agent-based unicast refresh; hub-and-spoke VXLAN bridging (vtep-to-vtep) avoids the flood/loop problems of full-mesh VXLAN for AP tunnels; proxy/MAC-rewrite-offload keeps MAC learning off the fabric. Replaces single-point WiFi gateways and their ICMP-failover hacks, and replaces per-AP static EVPN multihoming config.
- **Where applicable**: Explicitly Arista EOS-specific (VESPA, dynamic-tunnel MH Set ID, MRO are Arista features). For this PM: the problem analysis (MAC randomization impact, scale numbers) is universally valid; the specific mechanism requires Arista. Worth tracking for equivalent mechanisms elsewhere.

### バックボーンをスケールアウトで“運用する”段階へ ～ DDBR商用化までの歩みと、実運用に渡して見えた論点 ～

熊木健二、石嶋紘大（KDDI）

- **Why**: The first full "we actually run it" report on distributed disaggregated backbone routers — cluster-router design methodology, real capex numbers, and the operational questions (fault isolation, responsibility boundaries in multivendor support) that only surface in commercial deployment.
- **What**: KDDI finished building its scale-out backbone on DDBR (TIP Open Optical & Routing project) and moved cluster-type DDBRs into commercial operation as core routers in major cities (June 2026), after peering routers in 2023. Reported: ~50% introduction-cost reduction vs. same-generation chassis routers (commodity silicon + optimized procurement), stable operation with no service impact, and validation passing KDDI's full carrier test regime.
- **How**: Cluster router design flow worth stealing: decide max forwarding capacity → pick Switching Fabric hardware and count ("cluster size") → pick Packet Forwarder (line-card equivalents) → revisit fabric count for N+1 redundancy, because a small cluster means more links per counterpart and traffic spill on fabric failure, and cell-ification overhead must be budgeted. Cluster size changes require physical re-cabling — so size for the end-state traffic. Components can be spaced up to 100m across racks/rows, letting per-rack power be tuned to each building's cooling capacity. Data plane uses cell transfer between forwarders and fabric (no link-skew congestion, but header overhead). Operationally: SW/HW first-triage goes to the software vendor; cluster-internal failure and monitoring tests were added to the standard regime.
- **Where applicable**: KDDI/TIP-specific program, but the cluster-sizing math, the "decide cluster size once because changing it means recabling" warning, and the multivendor responsibility-splitting experience apply to anyone evaluating disaggregated routing. Pairs with KDDI's validation-automation talk (same OpenConfig/ONDATRA platform, validation ~6 months → ~1 week).

### プラットフォームにおける組織間対話の重要性 – 実例から見るNWにおけるソフトウェア運用 –

サイボウズ NW&DCチーム・Kubernetesネットワークチーム（尾崎、寺嶋）

- **Why**: The clearest talk in the program on cloud-native networking internals actually running a production SaaS (kintone/cybozu.com, AS131912): Cilium + eBPF + BGP-unnumbered IP-Clos, told from the "what the network team and the k8s team must understand about each other" angle.
- **What**: Cybozu's Neco platform (k8s-based) on a leaf-spine IP-Clos: AS-per-rack, BGP unnumbered between spine and leaf, BIRD on each node advertising node loopback, Pod IPs (Coil IPAM), and LoadBalancer Service IPs (Cilium BGP control plane) into the fabric; ClusterIP handled by Cilium's kube-proxy replacement (eBPF DNAT on the pod's veth — switches only ever see pod-to-pod traffic); ingress via Cilium L4 LB (Maglev hashing, DSR, Geneve encapsulation between LB nodes).
- **How**: The value is in the cross-layer failure stories: Cilium's IP-option mode sent custom IP Options that pushed packets into the spine switch's L2 slow path, causing ~20% packet loss until they reimplemented over Geneve encap; spine ECMP route-table limits cap theoretical LB capacity (racks × spine path limit / 2); Maglev hashing means ECMP rebalancing during maintenance doesn't break TCP sessions (any LB node picks the same backend). Also a "No route to host during full-cluster rolling reboot" case diagnosed from BIRD/Cilium agent startup ordering. Their conclusion: both teams must know which IPs land in switch routing tables (node/pod/LB-IP) and which never do (ClusterIP, rewritten by eBPF), and that physical device limits can cap software's theoretical performance.
- **Where applicable**: Cybozu-specific stack but built entirely from adoptable OSS (Cilium, Coil, BIRD, eBPF) — directly reusable patterns and pitfalls for anyone running L3-routed k8s fabrics. This is the talk for the PM's eBPF/Cilium/K8s/BGP interests.

### マルチベンダーバックボーンで実現するDDoS対策 ～RFC Internet-DraftのBGP Flowspec Redirect-to-IP導入への挑戦～

**Links:** [Slides](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-multivendor-ddos-biglobe.pdf) · [Recording](https://www.youtube.com/watch?v=wEfBFfC2tnk)

津山訓司・阿部孝一・中野龍（ビッグローブ）

- **Why**: Network security + BGP datapath in one: a production deployment of BGP Flowspec Redirect-to-IP for DDoS scrubbing, and a candid account of deploying an Internet-Draft where router vendors reference different draft versions and are mutually incompatible.
- **What**: BIGLOBE (AS2518, backbone of 3 vendors / 7 models) rebuilt its DDoS mitigation in FY2025. Classic BGP off-ramp (announce /32s and return clean traffic via GRE or dedicated circuits) forced per-protected-site circuits and construction work, limiting protection scope — a real constraint when 100Gbps+ attacks on the FTTH network surged from late 2024. They chose Flowspec Redirect-to-IP: flow-collector detects the attack via NetFlow, advertises a Flowspec route matching src/dst/port, external-facing interfaces redirect matching traffic to the scrubber's next-hop IP, and scrubbed clean traffic returns via normal routing — no GRE, no extra circuits, and works for self-AS protection and multihomed transit customers.
- **How**: Because draft-ietf-idr-flowspec-redirect-ip is still an I-D, each router vendor implemented a different draft revision with incompatible encodings; BIGLOBE built (and commercially deployed) its own conversion appliance, based on ExaBGP, that translates the collector's Redirect-to-IP routes into each router's implementation dialect. Flowspec is enabled only on external-facing interfaces and disabled on internal ones to prevent redirect loops.
- **Where applicable**: BIGLOBE-specific backbone and conversion device, but the mechanism comparison table (BGP+GRE, BGP+separate-AS+GRE, Flowspec Redirect-to-VRF, Flowspec Redirect-to-IP) is a genuinely useful decision aid for anyone extending scrubbing coverage across a multivendor backbone. The I-D-interop lesson generalizes: expect draft-stage features to diverge across vendors and plan a translation shim.

### RPKIキャッシュサーバの課題と提案 -より信頼できるRPKIを目指して-

**Links:** [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/RPKI%E3%82%AD%E3%83%A3%E3%83%83%E3%82%B7%E3%83%A5%E3%82%B5%E3%83%BC%E3%83%90%E3%81%AE%E8%AA%B2%E9%A1%8C%E3%81%A8%E6%8F%90%E6%A1%88-%E3%82%88%E3%82%8A%E4%BF%A1%E9%A0%BC%E3%81%A7%E3%81%8D%E3%82%8BRPKI%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%A6_%E5%B1%B1%E5%8F%A3%E5%8B%9D%E5%8F%B8-2.pdf) · [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/RPKI%E3%82%AD%E3%83%A3%E3%83%83%E3%82%B7%E3%83%A5%E3%82%B5%E3%83%BC%E3%83%90%E3%81%AE%E8%AA%B2%E9%A1%8C%E3%81%A8%E6%8F%90%E6%A1%88-%E3%82%88%E3%82%8A%E4%BF%A1%E9%A0%BC%E3%81%A7%E3%81%8D%E3%82%8BRPKI%E3%82%92%E7%9B%AE%E6%8C%87%E3%81%97%E3%81%A6_%E5%BE%8C%E8%97%A4%E6%B1%B0%E7%8F%A0.pdf)

山口勝司（ビッグローブ）、後藤汰珠（長崎県立大学）

- **Why**: ROV in Japan has crossed into "mature technology" (~40% INVALID-discard as of 2026, accelerated by JPNIC guidelines since 2024) — so the interesting question shifts from "should we do RPKI" to "what happens when the VRP feed itself is incomplete." This is the operational next frontier of routing security.
- **What**: A structured risk analysis of incomplete VRPs: if the repository or the repository↔cache-server path loses ROAs, routes that should be INVALID become NOTFOUND and get admitted — a silent security regression. Conversely, in a future where NOTFOUND is also rejected (RFC 7115 currently only mandates dropping INVALID; a "ROA-Strict" BGP Large Community intent draft exists), the same incompleteness would mass-reject *valid* routes and cause outages. Real incidents cited: JPNIC RRDP stale data (2025/3), APNIC repository server down (2025/6), plus LACNIC/AFRINIC/RIPE issues 2022–2024.
- **How**: Two mitigations: (1) operational monitoring from day one of ROV — alert thresholds on sync-successful repository count, failure ratio (<20%), VRP total count (non-zero), ROA collection time (<1h), with the option to pause ROV on anomaly; (2) the "VRP breaker" (joint BIGLOBE–Nagasaki Institute of Applied Language research, patent pending): validates the ROA set *before* distributing VRPs to routers, and temporarily halts distribution when anomalies are detected — a circuit breaker for the trust feed itself.
- **Where applicable**: General to any RPKI/ROV operator; the discussion explicitly scopes out router-side and cache-server software implementation details. Directly relevant to the PM's routing-security interest, and the VRP breaker is a design pattern worth watching.

### 耐量子計算機暗号への移行準備してますか？ ～2030年台の安全なネットワークに向けて～

高橋康（パナソニックホールディングス）

- **Why**: PQC migration is now a network-equipment lifecycle problem, not a crypto research topic: ML-KEM/ML-DSA are standardized (FIPS, Aug 2024), deadlines across US/UK/EU/JP converge on 2035 with several pulled to 2030, and March 2026 results (RSA-2048 breakable with <1M qubits, ECDSA with ~10K) moved threat estimates earlier. Routing protocols are the laggards.
- **What**: A routing-focused PQC status map: DNSSEC has active drafts (pqc-dnssec-strategy; SLH-DSA-MTL); RPKI only an early draft (yoshikawa-sidrops-pqc-rpki); BGPsec and ASPA have nothing. Combined with the practical constraint that PQC keys/signatures are 10–100× larger with 10–100× memory use (ML-DSA stack usage ~38KB vs. ECDSA's ~1.6KB) — a packet-size and performance problem for routers and constrained devices, echoing the "packet size increase, next-gen router throughput" concerns raised for operators.
- **How**: Also includes concrete Panasonic implementation work: an HQC implementation with ~4–8× memory and ~70–85× speed improvements for constrained devices (ACM WiSec 2026), and a parameterized ML-DSA time/memory trade-off (~4× improvement on the chosen axis). The framing for operators: PQC migration is not for future security but for product/service continuity (CRA, JC-STAR, CNSA 2.0 supply-chain requirements), and historical crypto migrations (SHA-1, 3DES, RSA-1024) took 10–15 years — so a 2030/2035 deadline means starting inventory and prioritization now.
- **Where applicable**: General; the IoT/BGPsec implementation specifics are Panasonic's, but the timeline argument, the IETF draft landscape for routing security, and the key-size/throughput implications apply to every network operator and equipment PM.

### 朝から晩まで MCP　—　AI エージェントと私

日本大学（演者名はプログラムに記載なし）

- **Why**: A day-in-the-life account of running a 100k-user university network almost entirely through MCP-wrapped tools and Claude Code — notable for the PM because it treats MCP server *authentication, distribution, and audit* as first-class operational problems, which is exactly where agentic identity is heading.
- **What**: A small university IT team rebuilt its accumulated Python/shell API scripts as MCP servers — junos-mcp (NETCONF to Juniper, dry-run/rollback), eos-mcp (16 tools), aruba-central-mcp, keycloak-mcp (21 tools), GWS MCP, plus a stdio relay — and now runs morning health checks (Zabbix/KeyCloak MCP + xFlow/Shadowserver), config diff review with dry-run, and evening reporting through agents (from abstract only).
- **How**: The transferable part is the hardening list: stdio's limits forcing migration to Streamable HTTP with OAuth2 for MCP server auth/distribution; MCP server development/operation/security management practices; design patterns to prevent LLM runaway; and audit log retention for configuration changes agents make — traceability of who/what changed the network (from abstract only).
- **Where applicable**: Single-university "solo ops" context, but the MCP authentication/audit/runaway-prevention patterns are general to anyone exposing network tooling to agents. Reads as a preview of the workload/agentic identity questions (agent authn to infrastructure, change audit trails) the PM works on (from abstract only).

### NWトポロジー可視化から時系列化へ: BGP-LS+BMP+αによるトポロジー把握の時間軸拡張

**Links:** [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/%E3%80%90%E4%BA%8B%E5%89%8D%E5%85%AC%E9%96%8B%E7%94%A8%E3%80%91JANOG58_pr-topology-timeseries.pdf) · [Slides (PDF)](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-topology-timeseries-uchimi-main.pdf)

内海友輔・伊藤達真・魏亮（ソフトバンク）

- **Why**: Addresses a real observability gap: SNMP/NetFlow/telemetry watch per-device metrics, but "what did the routing topology look like at 23:42, and did my change cause the detour?" is unanswerable. BGP-LS + BMP as a time-series data source is a technique any large operator can adopt.
- **What**: SoftBank built an L3-topology observation system: BGP-LS for IGP topology (nodes, links, adjacencies, metrics — quasi-real-time and as time series) and BMP for BGP path-state changes, stored in a GraphDB, enabling reconstruction of the network's logical topology at an arbitrary past time, diff detection between two timestamps (link add/remove, metric changes — for pre/post-change and intent-vs-state verification), and post-hoc failure analysis.
- **How**: GraphDB chosen over RDBMS because router-vertex/link-edge models map naturally and avoid join explosion; an LLM agent generates graph queries from natural language so network engineers don't need deep graph-query skills. Honest scope limits: BGP-LS covers only logical IGP information — no physical IF/bundle/LAG mapping (needs config/LLDP/telemetry), no L1/L2 or traffic state (needs SNMP/syslog/flow), and it can't by itself build a simulation environment. Their position on Network Digital Twins: a full always-on mirror of a commercial network is unrealistic; instead, slice out "what you need, when you need it" from the time-series store and map onto static config/inventory data on demand.
- **Where applicable**: Built in a commercial carrier network (SoftBank mobile/core), but BGP-LS/BMP/GraphDB are vendor-neutral standards — broadly adoptable, and the intent-vs-state reconciliation framing ties directly into automation safety verification.

## Adjacent

### CLIパーサーからの脱却 – モデル駆動型プラットフォームによるマルチベンダー検証の完全自動化

荻原拓也、横山直（KDDI）

- **Why**: The most adoptable automation-tooling story in the program: how KDDI turned multi-vendor network validation (1,500+ basic-function tests, 200+ IOT tests, 10+ device models) from months of CLI-parsing scripts into a model-driven platform, cutting validation from ~6 months to days.
- **What**: Follows their JANOG54 OpenConfig/ONDATRA PoC through 500+ scenarios of at-scale deployment and the technical debt it created: vendor if/switch branches bloating scenarios, unmaintainable CLI parsers (regex that breaks on version-dependent output, false PASSes), and outsourced code nobody internally could fix. The redesign: ygot/ygnmi YANG-driven Go development (generated typed code, no CLI parsers), an abstraction layer where vendor-specific models sit behind a common OpenConfig model, hybrid coverage using Vendor Native YANG and CLI only where OpenConfig falls short, topology variables externalized, and a platform layer for one-click CI execution with auto-generated reports.
- **How**: ONDATRA binding separates logical test topology from physical/virtual testbeds; the platform builds and distributes code so scenario execution needs no local environment; the same platform was reused for DDBR commercial validation. Validation period: 3–6 months → days (with the DDBR deck citing ~1 week for full carrier test regimes).
- **Where applicable**: KDDI's scale and organization, but the architecture (Google's ONDATRA + featureprofiles ecosystem, ygot/ygnmi) is open source and directly reusable by any team doing multi-vendor validation. The organizational lesson — don't outsource automation code you can't read — is universal.

### そのトラフィックは誰のため？ 生成AIがもたらす「AI-to-AI」通信時代のNWデザイン

**Links:** [Slides](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-traffic-for-whom-KanameNishizuka.pdf)

西塚要（NTTドコモビジネス）

- **Why**: A useful corrective for capacity planning: while everyone talks about AI DC traffic, ISP statistics show the last mile is still video-dominated — this talk maps where AI traffic actually flows and constructs a thesis for what changes next.
- **What**: Maps traffic across the AI lifecycle (crawl → training → inference → retrieval): training/inference are East-West in DCs; North-South is crawler and agentic-retrieval bots (Cloudflare Radar: bots ≈ 1/3 of HTTP requests, AI bots now top-accessors; Common Crawl pulls 2.1B pages/355TiB per ~2 weeks). The "human bottleneck" hypothesis: last-mile traffic is capped by population × disposable time × sensory bandwidth, so AI-to-AI (agents fan-outing browsing/API calls, on-device AI pre-fetching, content compressed for agents via llms.txt / Markdown-for-agents / MCP / A2A) becomes the growth vector.
- **How**: Argues metrics shift from Mbps/Tbps toward latency, fan-out, cache-hit, and token cost; LLM serving and CDNs converge into a retrieval/summarization middle layer that sits between content and users.
- **Where applicable**: Analysis/hypothesis rather than deployed system; the speculative parts are explicitly flagged as such. Valuable input for any PM reasoning about CDN/edge/last-mile product strategy in the agentic-web era.

### ネットワーク監視の自動化はどこまでできるのか? -Apache Airflowによるアラート対応基盤-

**Links:** [Slides](https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-auto-nw-monitoring-HonaiUeoka.pdf)

上岡輔乃（LINEヤフー）

- **Why**: A template other operators can copy for the alert-handling problem: replacing 24/365 staffed first-line response with an automated platform across 22,000+ network devices — and honestly cataloging what Airflow alone can't do.
- **What**: LINE Yahoo's DC network operation had mature runbooks but human-bound first response (load, slow improvement, knowledge-transfer limits) and per-team automation sprawl (Jenkins/FaaS/AWX per team). Their answer: a common Airflow-based platform ("oyakata") where a platform team provides shared Operators (SSH, Slack, Jira sensors) and each NW team writes its own DAGs — teams own operational knowledge, the platform owns plumbing. Example PSU-alert workflow: ticket → config DB lookup → PSU status check → history/DC-work check → replacement order or escalation — 5–10 min manual becomes 1–2 min automated, zero labor.
- **How**: Airflow chosen over scratch/FaaS/Jenkins/AWX on intro-ease, execution-environment freedom (Python/any container), Operator-based commonality, and visualized workflow history (debuggable, not black-box). Airflow's gaps they had to build: alert-triggered DAG launch, alert-type→workflow mapping managed by NW teams, and alert dedup for flapping events. LLM agents slot in as tasks — related-alert aggregation and two-stage alert classification (classifier agent → specialist agents).
- **Where applicable**: Broadly applicable — built on OSS, org-agnostic design (platform provides Operators, teams provide workflows). The dedup/routing glue they built is the reusable insight.

### データセンター構築・移設のリアル​〜国内外の事例から考えるスムーズな進め方〜​ 

竹﨑友哉（IIJ）

- **Why**: Physical DC/WAN facility work from IIJ (AS2497, 44 POPs): real trouble logs from building and migrating equipment domestically and overseas — the unglamorous failure mode layer above the network design.
- **What**: Three FY2024–25 projects with what actually went wrong: Singapore equipment refresh (local rules they didn't know — "don't do unfamiliar things in unfamiliar places"); Osaka Central expansion + Osaka North new build (vendor delivery delays, mis-orders, a construction accident, missing parts, weather-affected shipping — "troubles come in threes"); and the Seattle POP migration (strong union rules on delivery timing, COI insurance certificates required for site entry — unfamiliar to Japanese practice, multi-layered subcontractors complicating paperwork; FS.com as a fast US parts source; the whole 4-person crew rotating through illness).
- **How**: Common success factors distilled: schedule slack, on-site surveys, recovery plans, spare units/parts, stakeholder alignment — "assume the unexpected will happen." Includes practical overseas procurement notes (US return culture, 1–2 day optics delivery).
- **Where applicable**: IIJ/POP-specific anecdotes, but the checklist transfers to any cross-border DC build or migration; Chatham-house style sharing of failure stories is itself the value.

### 「生成AIを用いたネットワーク監視」の実運用課題と利用コスト～そのLLM、いくらかかってますか？～

高野悠生、レヌグンタ・タンマイ（NTTアドバンステクノロジ）

- **Why**: The rare AIOps talk about *cost and failure modes* rather than demos — grounded in a service (GAIPAR) actually sold to customers plus a large-scale field test at Interop ShowNet 2026.
- **What**: The core finding: LLM-based network monitoring "works well enough" — the problem is cost and prompt information volume. Quantified: ~400 managed devices at ShowNet produce 5,000–10,000 syslog/sec (~1.5TB over 3 days), which fills a 400K-token context in ~5 seconds. "Information overload causes information omission" — too much noise both hides the causal log (analysis failure) and triggers hallucination. Skilled operators don't dump everything; they search small-and-iteratively.
- **How**: Their fix: agentic iterative log analysis — an agent loops search keyword/count/time against the packet-log/syslog DB (small queries with feedback), a small model (e.g. gpt-class mini) does per-query reports, and a large model integrates into a final report. Also covers initial vs. running token costs, non-monetary costs (operator AI literacy, environment updates), and proprietary-to-open-model substitution options.
- **Where applicable**: Vendor service (NTT-AT) but the context-math and "search iteratively, don't dump" pattern applies to any log-LLM deployment; useful for PMs pricing or designing AI-assisted observability products.

### 脱・人間計算機！AIで光NWグランドデザインの“手作業地獄”から抜け出す

増田陽（双日テックイノベーション）

- **Why**: Optical WAN grand design (topology comparison, wavelength planning) is normally a manual Excel hell where engineers burn out computing one pattern — this LT shows the division of labor: AI computes, human judges.
- **What**: An evaluation engine that takes physical network info, candidate topologies, per-destination traffic, device parameters (capacity/latency/failure rates/MTTR/cost), and design policy (Work/Protection disjoint paths, 64λ C-band, 400G/λ), then exhaustively computes all-pair delays, redundant route design, reliability (MTBF/availability), wavelength packing per link, and cost — producing a comparison table (e.g. star vs. partial mesh vs. low-latency-biased: 346μs vs. 311μs vs. 267μs mean delay, bottleneck λ utilization 78%/63%/71%, cost 100/112/121%).
- **How**: Hours of manual recomputation per topology change become minutes; weights per use case (broadcast: latency; finance/medical: reliability; enterprise-line growth: wavelength efficiency; capex: cost) stay a human decision.
- **Where applicable**: SIer tooling (Sojitz Tech-Innovation) with stated simplifications (uniform/one-sided traffic patterns, no SRLG/building-level failures, client-side redundancy assumed) — a design-support pattern for optical transport planning rather than a product, but directly relevant to physical WAN design workflows.

## Wildcard

### 景観保護のための空間光通信(FSO)活用事例 〜松山城周辺の観光を支える次世代インフラ〜

土居誉伸・堀内貴行（愛媛CATV）、畠山豊・藤原稔（NTTアドバンステクノロジ）

- **Why**: Not a normal fit for a DC/optics PM, but worth seeing: free-space optics surviving its 2010s dead period and now delivering a real 10Gbps-class carrier backhaul — a genuine technology-transition story.
- **What**: Ehime CATV replaced an end-of-life 25GHz wireless link (~870m, Matsuyama Castle area, no new fiber permitted for landscape/cultural-property protection) with FSO, choosing it over 60GHz mmWave (~400Mbps estimated, insufficient for Wi-Fi-7-era plans).
- **How**: The interesting part is why FSO is viable now when it failed ~7 years earlier in their own disaster-drill test: modern units are ~3kg (vs. ~10kg), 1550nm (less solar interference), PoE, GUI-based alignment with automatic tracking to compensate vibration/building sway, 10–25Gbps. The small pole-mountable form factor let them reuse the existing mount, which in turn simplified the permit process under cultural-property and landscape regulations. Remaining physics: fog, birds, tree growth, axis misalignment.
- **Where applicable**: Regional ISP/CATV last-mile context, but the "FSO is back" technology assessment (what changed: miniaturized optics, motor control, sensors, software) and the licensing advantage (no radio license) are relevant to anyone tracking physical-layer alternatives for fiber-impossible spans.

### ベテランエンジニアの「勘」はLLMに移植できるのか RAGで再現できるもの・できないもの

石井秀和・春原寿里（NTTドコモ）

- **Why**: Not a network-technology talk — a knowledge-representation talk that happens to be about network operations, and one of the sharpest experimental designs seen for testing AI operational judgment.
- **What**: A 3-layer model of veteran tacit knowledge: (1) cross-system intuition, (2) analytical "kata" (judgment frames — how to narrow impact, what to suspect), (3) system-specific case knowledge. Thesis: RAG retrieves only layer 3; the missing layer 2 is why AIOps fails in the field. They then built a deliberately adversarial failure scenario (disk-full → keepalived death → dual-system outage, with three traps: a restart manual that would cause secondary damage, a loudest-but-not-root alert, and all-null alert priorities) and tested 2×2: with/without the "type" (prompt-encoded judgment rules), with/without complete logs.
- **How**: Results: no-type + full logs = correctly identifies disk-full but recommends the manual's destructive restart ("dangerous rookie"); no-type + missing logs = confidently recommends full environment teardown (worst case); with-type + full logs = re-orders procedures to free disk first; with-type + missing logs = fail-safe reasoning that suspects an invisible root cause. The "type" is injected as generic instructions (e.g., "infer criticality from surroundings when priority is null"; "never recommend restarts under suspected resource exhaustion") rather than system-specific rules.
- **Where applicable**: docomo MEC environment for the scenario, but the methodology (layered tacit-knowledge model, adversarial test scenarios, type-vs-information matrix) transfers to any team building or evaluating AI-assisted incident response — and it directly informs what "senior-operator judgment" means for agentic ops products.

### 遠くの国のモバイル回線をどう知るか

吉野純平（MIXI）

- **Why**: A refreshingly honest field-measurement talk: how to actually learn what mobile networks feel like in countries you can't instrument — using client-side techniques (QUIC/TCP RTT estimation, TCP_INFO, RSRP/RSRQ/SINR) that most server-side network engineers never touch.
- **What**: A MIXI executive's methodology for measuring real user environments abroad: local-major-carrier SIMs (roaming exits elsewhere), smartphones rather than PCs, ICMP to CDN edges plus QUIC/TCP in-protocol RTT estimation (since you can't instrument the origin or the CDN), radio-quality logging from the phone's interfaces, and AI-assisted on-site app development for measurement. Findings include indoor dead spots (a mall floor with signal but no throughput; hotels capped ~4Mbps), suspicion of weak indoor-antenna investment, and the observation that global measurement coverage (pingdom probes, cloudperf, cdnperf) has a mobile-sized hole.
- **How**: Client-side RTT/loss estimation via QUIC and TCP socket mechanisms; server-side, sketches an eBPF/TCP_INFO-based passive recorder (RTT variance, window, retransmits, out-of-order counts, close reasons) for when you still run a global-IP server — noting such measurement points are shrinking as managed front-ends (LB/API gateways/CDN) absorb them.
- **Where applicable**: App-operator perspective rather than operator infrastructure, but the measurement gap (managed services removing observability points) is a real product insight for anyone building network-quality telemetry.

## Themes

- **AI infrastructure has made JANOG a physical-facilities conference**: liquid-cooled rack-scale GPU, CDU/manifold/ORv3 constraints, 800G cabling with ~30k fiber cores per container, MPO/WDM/LPO selection, transceiver triage — the physical layer is now the bottleneck and the content.
- **Agentic AI crossed from PoC to production-ops this cycle**: MCP standardization (with OAuth2 and audit questions emerging), Agent Skills replacing bespoke multi-agent tuning, real token-cost accounting, closed-network AI platforms — with a recurring conclusion that *abstraction* (few-parameter APIs, typed models, skill files, workflow platforms) is what makes agents safe enough to operate networks.
- **Routing security matured from "adopt RPKI" to "survive RPKI's failure modes"**: ~40% ROV in Japan, cache/reliability and VRP-completeness risks, circuit-breaker designs, and Flowspec-based DDoS scrubbing across multivendor backbones (including building translation shims for draft-stage IETF features).
- **Model-driven automation is displacing CLI parsing for real**: OpenConfig/ONDATRA/ygot platforms reporting order-of-magnitude validation time reductions, and AI-assisted NOS lifecycle validation (IIJ) compressing release qualification from months to days.
- **Time-series network state is the new observability frontier**: BGP-LS/BMP topology snapshots, intent-vs-state reconciliation, GraphDB + LLM query interfaces — positioned both as human forensic tooling and as the substrate agents need to reason about network state.
- **PQC timelines hardened from 2035 toward 2030**: framed as product-continuity (CRA/CNSA 2.0) rather than security, with routing (BGPsec/ASPA: nothing yet; RPKI: early draft) the clear laggard and key-size/throughput the router-relevant constraint.
