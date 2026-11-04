<!--
conference: ARIN 57 Public Policy and Members Meeting
type: operator
source_url: https://www.arin.net/participate/meetings/ARIN57
generated: 2026-11-04
registry_key: arin-57
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ARIN 57 Public Policy and Members Meeting — Digest

ARIN 57 is a registry policy and governance meeting, not a research conference, so the yield for a networking PM is different in kind than a NANOG or SIGCOMM: the value here is routing-security operations (RPKI/ASPA tooling and adoption data), IPv6-only transition practice from large research networks, registry integrity/fraud operations, and the policy currents that will shape IPv4/IPv6 availability over the next few years. All selected items below had full slide text extracted, so write-ups are grounded in the actual deck content rather than titles alone.

## Core

### KEYNOTE: Demystifying RPKI: Exploring Tools to Simplify ROA Planning and Visualize Validation

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_internet2_keynote.pdf) · [Recording](https://www.youtube.com/live/-Fwz65uQp3E?t=1h12m38s)

Steve Wallace, Internet2 (NSF-supported, OAC-2530871)

- **Why**: ROA creation is the single biggest friction point in RPKI adoption — operators fear creating a ROA that accidentally invalidates their own (or a customer's) more-specific announcements. This is a set of free, working tools that directly address that fear, plus an early look at ASPA object planning.
- **What**: Three web tools hosted at `rootbeer.internet2.edu`: an RPKI-ROA Planner that computes candidate ROAs for a prefix and the *safest order* to create them; an RPKI-ROA Visualizer that walks through Route Origin Validation bit by bit (useful for training staff who don't intuit maxLength semantics); and an experimental RPKI-ASPA Planner that suggests a draft ASPA object for an ASN.
- **How**: The ROA Planner correlates three data sources — IRR route objects, currently observed Internet routes, and historical routing data — to derive the set of plausible origins for a prefix, then lets the user pick which apply and sequences ROA creation to avoid transient Invalid states. The ASPA Planner builds its suggestion from CAIDA AS-relationship data ("and some magic," per the speaker).
- **Where applicable**: Broadly applicable to any operator with ARIN-region resources; the tools are public and free. The ASPA Planner is explicitly experimental and should be treated as a starting draft, not a turnkey ASPA — ASPA semantics are still moving through the IETF.

### Routing Security Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_routingsecurity.pdf) · [Recording](https://www.youtube.com/live/HGTbhKYk_0g?t=3844s)

Brad Gorman, ARIN (Director, Customer Technical Services)

- **Why**: The best single data source on where RPKI actually stands in the ARIN region — which is directly actionable when prioritizing your own ROA coverage and when deciding how much to lean on ROV in filtering. Also the first production deployment of ASPA objects worth watching.
- **What**: A quarter-over-quarter adoption report plus new features. Key numbers (NIST RPKI monitor, 1 April): global RPKI validity has climbed steadily through Q1 2026, with IPv4 and IPv6 both in the roughly 60–66% range. In-region: 8,403 organizations registered for ARIN RPKI services (25% growth since Q1 2025), 98% of them on Hosted RPKI — but ~15% of registered orgs have never created a single ROA, only 50% of RPKI-eligible IPv4 blocks are covered by ROAs, and 54% of ARIN-registered IPv4 blocks seen in announcements are RPKI Valid. ASPAs are live in production (198+ created and trending up), enabling IETF draft testing with real data. An upcoming "RPKI Routing Intelligence" feature will show orgs their prefixes as seen in the global BGP table, explain why announcements are Invalid or Not Found, and simulate the effect of proposed ROA changes.
- **How**: The update combines NRO/NIST monitoring data with ARIN's own registry cross-referencing (allocations under agreement vs. ROA coverage vs. announcements). The Routing Intelligence feature is essentially a BGP-table diff against your resource certificate with counterfactual analysis.
- **Where applicable**: The stats are ARIN-region-specific, but the gap they expose (signup ≠ protection; the bottleneck is ROA coverage, not registration) generalizes. The Routing Intelligence preview matters to any ARIN resource holder; worth benchmarking your own coverage against the 50%-of-eligible-blocks regional figure.

### KEYNOTE: The Nine Lives of an Early Adopter: Leading Cats to Water in the IPv6 Era

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_IPv6keynote.pdf) · [Recording](https://www.youtube.com/live/-Fwz65uQp3E?t=4h51m36s)

Nick Burlagio (Planning and Architecture) and Inder Monga (Executive Director), ESnet

- **Why**: ESnet is one of the few production networks that has actually gone IPv6-only on its management plane (with the ESnet6 buildout, completed 2022), and this keynote frames the "why now" argument in terms directly relevant to cloud-native and agentic workloads. It is a rare operator talk where the transition strategy, not the nostalgia, is the payload.
- **What**: A history-to-present narrative of ESnet's IPv6 journey — 6Bone participant, 6REN founder, recipient of the first production IPv6 allocation from ARIN in 1999 — culminating in ESnet6, which runs an IPv6-only management plane with comprehensive automation and visibility. The forward-looking argument: AI agents on the network need simplicity (elimination of middleboxes), one consistent addressing scheme for end-to-end automation, and any-to-any hyper-connectivity — none of which survive NAT and dual-stack sprawl.
- **How**: Primarily a strategy and lessons talk rather than a mechanism talk (the deck walks the 1995–2026 timeline of IPv6 touchpoints). The concrete operational takeaway is the IPv6-only management plane as proof that a large WAN can run single-stack for infrastructure traffic even while carrying dual-stack customer traffic.
- **Where applicable**: ESnet-scale (DOE national labs, 100G/400G backbone) is specific, but the management-plane-first pattern is broadly transferable — it's the least risky place to go v6-only and it forces the tooling/automation to become v6-native. The agentic-workload argument is relevant to anyone planning for machine-dense networks.

### Engineering Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_engreport.pdf) · [Recording](https://www.youtube.com/live/HGTbhKYk_0g?t=375s)

Mark Kosters, ARIN (CTO)

- **Why**: Densely useful for three of the PM's interests at once: identity (ARIN's own MFA mix), physical DC work (ARIN's data center migration), and routing security infrastructure (RPKI trust anchor constraints, ASPA, and the planned retirement of legacy directory services).
- **What**: The operational report on ARIN's public services. Highlights: MFA adoption across 53,065 users is 61% TOTP, 36% SMS, and only 3% FIDO2 — a sobering data point for anyone betting on passkey adoption in registry-adjacent systems; all authorizations have moved into ARIN Online (email-based approvals retired); ASPA support released; RPKI Trust Anchor Constraints work is underway, leveraging extended stats and extended transfer logs to attest registry contents per the IETF constraining-trust-anchors draft (already implemented in `rpki-client`); a consultation is planned on retiring RWhois and Whois-RWS, collapsing four directory-service interfaces (Whois, RWhois, Whois-RWS, RDAP) down toward RDAP.
- **How**: On infrastructure, ARIN moved its computer room from HQ to a new Northern Virginia data center, replaced end-of-life hardware, and now runs public-facing services on Red Hat OpenShift with services under OpenShift KubeVirt virtual machines, with Prometheus monitoring displacing Sensu. RRDP is now the largest public-facing traffic class at 46.6% — a signal of how RPKI repo synchronization has become the dominant directory workload.
- **Where applicable**: ARIN-specific as an implementation, but the pattern — registry services re-platformed onto hosted Kubernetes with VMs for legacy services, and protocol-surface reduction (retiring RWhois/Whois-RWS in favor of RDAP) — is a template any infrastructure registry operator (including internal IPAM/identity services) can study. The FIDO2-at-3% figure is a broadly citable adoption reality check.

### Grant Reports

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_communitygrantreports.pdf) · [Recording](https://www.youtube.com/live/HGTbhKYk_0g?t=7308s)

Harlen Stenn (Network Time Foundation), James Harr (Internet2), Matt Griswold (20C)

- **Why**: Three community-grant reports, and the middle one is a genuinely reusable operator tool: a cheap, pre-configured device that stands up IPv6-only/IPv6-mostly test environments — the exact environments that are otherwise a multi-week lab project.
- **What**: (1) Internet2's IPv6 Test Pod: a sub-$150 device, funded by a $16,000 grant (follow-on to $7,000 in 2023), that creates dual-stack, NAT64/DNS64, IPv6-mostly (DHCPv4 Option 108), and IPv6-only wired/wifi networks over an IPv6 tunnel, pre-configured and distributed free to participants (45 units delivered, 20 more in April). Testing to date includes the Windows 11 CLAT private preview, NetworkManager 1.58 CLAT support, and HPN-SSH Happy Eyeballs behavior. (2) NTF's grant adds native Markdown output to GNU AutoGen to unify NTP documentation formats. (3) 20C's "From Raw to Ready" delivers a web UI (reg.fullctl.io) over regCtl, which normalizes RDAP responses across RIRs into consistent object views.
- **How**: The pod encapsulates the hard-to-assemble mix — NAT64 (poorly supported on low-end platforms), DNS64, PREF64, and Option 108 signaling — so a developer, IT support team, or network engineer can test client behavior in a v6-only environment without building the bed themselves. The rationale laid out is worth internalizing: dual-stack hides problems (Happy Eyeballs), doubles address pools and firewall policies, and makes troubleshooting ambiguous.
- **Where applicable**: The pod is available by application (ipv6-pod.info) to anyone in the ARIN community — this is the transferable piece. The AutoGen and regCtl work is niche but the RDAP normalizer is handy for anyone scripting against registry data across RIRs.

## Adjacent

### Registry Integrity and Oversight

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_registryintegrity.pdf) · [Recording](https://www.youtube.com/live/3jGjPBGK03c?t=2h10m10s)

Reese Radcliffe, ARIN (Senior Manager, Registry Integrity and Oversight)

- **Why**: The operational security underside of the registry: how number-resource fraud actually manifests, with numbers. Directly relevant to anyone whose address space could be hijacked or whose counterparties might not be who they claim.
- **What**: A threat-landscape and casework report. Notable findings: of out-of-region organizations creating ARIN Org IDs "to expand into the region," roughly 30% are found announcing ARIN resources out-of-region within 60 days; ~240 Org Creates per month, of which ~35 are escalated to RIO, with 42% of those being out-of-region expansion attempts; NRPM 4.10 (IPv4-to-facilitate-IPv6) space is abused via out-of-region announcement, reassignment to customers, leasing, or announcing with no associated IPv6; 223 policy non-compliance reports were received in 2025, of which 28 were actionable.
- **How**: RIO runs escalated review of suspicious Org Creates, Section 12 audits with video identity verification, fraud investigation, and law-enforcement collaboration, plus inter-RIR knowledge sharing.
- **Where applicable**: ARIN-specific process, but the threat taxonomy (entity fraud, unauthorized reassignment, out-of-region leakage, IRR misinformation) is the same one any resource holder or IX should assume exists. The 30%-within-60-days figure is a good calibration for how quickly out-of-region misuse follows a new Org ID.

### Policy Implementation and Experience Report

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policyimplementation.pdf) · [Recording](https://www.youtube.com/live/-Fwz65uQp3E?t=2h22m06s)

John Sweeting, ARIN (Chief Experience Officer)

- **Why**: Where policy text meets operational reality — the most interesting part is ARIN staff's frank account of IPv4 leasing and inter-RIR transfer arbitrage, which affects the market everyone buys address space in.
- **What**: Three items. (1) AFRINIC's inter-RIR transfer policy was ratified 4 February 2026; ARIN staff have reviewed it as reciprocal and will allow IPv4/ASN transfers to and from AFRINIC once AFRINIC implements. (2) On LACNIC's new third-party sub-assignment (leasing) policy: ARIN does not consider leasing to be efficient needs-based utilization for transfers (NRPM 8.3/8.4) or waitlist qualification — and staff have observed ARIN-originated space appearing on leasing platforms in other regions after inter-RIR transfer. (3) Options floated for encouraging IPv6 adoption: requiring demonstrated IPv6 deployment for IPv4 waitlist access.
- **How**: A staff-practice report rather than a new mechanism; the leverage points are transfer approval criteria and waitlist eligibility rules.
- **Where applicable**: Relevant to anyone acquiring or transferring IPv4 in the ARIN region, and to anyone modeling IPv4 market behavior across RIRs. The AFRINIC change materially alters the global transfer map.

### Policy Block: Draft Policy ARIN-2025-3: Change Section 9 Out Of Region Use Minimum Criteria

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2025_3/) · [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20253.pdf) · [Recording](https://www.youtube.com/live/HGTbhKYk_0g?t=16999s)

Gerry George (with Matthew Wilder), ARIN Advisory Council

- **Why**: A live example of how a seemingly small threshold change (/22 → /24) can materially shift address-market behavior — the staff review itself says so.
- **What**: Reduces the in-region IPv4 utilization required to justify out-of-region use from a /22 to a /24. Staff and Legal review flags the consequence explicitly: nothing in Section 9 caps out-of-region use, so a single in-region /24 could in practice unlock substantially larger blocks for deployment entirely outside the ARIN region; staff anticipate a significant increase in IPv4 waitlist volume and ticket workload.
- **How**: A one-line NRPM text change, with the "real and substantial connection" requirement as the only remaining guard.
- **Where applicable**: ARIN-region policy, but relevant to any multi-region operator's IPv4 planning: if adopted, it lowers the entry cost for using ARIN as the source of globally-deployed space, and community feedback notes it could push organizations with heavy out-of-region growth toward other RIRs.

### Policy Block: Draft Policy ARIN-2025-8: Reserve 4.10 Space for In-Region Use

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2025_8/) · [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20258.pdf) · [Recording](https://www.youtube.com/live/HGTbhKYk_0g?t=23529s)

E. Marie Brierley (with Kaitlyn Pellak), ARIN Advisory Council

- **Why**: The policy counterpart to the RIO fraud report — 4.10 space (the IPv4 block reserved to facilitate IPv6 deployment) is one of the documented abuse vectors, and this codifies the in-region restriction.
- **What**: Amends Section 4.10 to state the set-aside is dedicated to facilitating IPv6 deployment *within the ARIN service area*. Staff review confirms this codifies existing practice with no operational impact. The live controversy is scope: PPML commenters noted the vague wording could block legitimate uses — e.g., an org with a globally-used ARIN IPv6 allocation using its 4.10 IPv4 to provide NAT64 for that global v6 space.
- **How**: A two-word textual amendment; the interesting question posed to the community is whether "only" should be specified.
- **Where applicable**: ARIN-region policy; matters mainly to orgs holding or seeking 4.10 space — which, per the RIO report, includes the more inventive lessees.

### Advisory Council Working Group Updates

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_acworkinggroup.pdf) · [Recording](https://www.youtube.com/live/-Fwz65uQp3E?t=3h12m35s)

Douglas Camin, Alison Wood, and Matthew Wilder, ARIN Advisory Council

- **Why**: The forward worklist for number-resource policy — a cheap way to see which NRPM sections will be churned over the next 12–18 months.
- **What**: The Policy Experience Report Working Group's "What's Hot" list: eliminating NRPM 8.5.7 (alternative additional IPv4 transfer criteria, judged redundant and little-used); simplifying the IPv6 initial allocation formula in 6.5.2.1; reconciling inter-RIR transfer discrepancies in 8.4 (needs-based requirements differ across RIRs, creating asymmetric transfer flows); and consolidating the overlapping IPv4 direct-allocation sections (4.1.8, 4.4, 4.10). The Policy Engagement WG is surveying the community on modernizing participation beyond the mailing list / meeting format.
- **How**: Status reports on working-group deliberation — no mechanism, but each item names the section and the observed problem.
- **Where applicable**: ARIN-region policy process. The inter-RIR transfer asymmetry item is the one with the most practical consequence for multi-region footprint planning.

## Wildcard

### Policy Block: Draft Policy ARIN-2026-1: Taking IP To Other Planets (TIPTOP)

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2026_1/) · [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20261.pdf) · [Recording](https://www.youtube.com/live/HGTbhKYk_0g?t=24051s)

Alison Wood (with Brian Jones), ARIN Advisory Council

- **Why**: The first formal attempt to recognize off-Earth use cases in any RIR's policy manual, and a genuinely novel addressing problem: how do you allocate IP space for a topology whose "regions" are gravity wells? For anyone who thinks about aggregation and hierarchical addressing, this is a fun and occasionally rigorous stress test of the concepts.
- **What**: A draft policy, proposed jointly with the IETF TIPTOP working group (see `draft-li-tiptop-address-space` and `draft-many-tiptop-ip-architecture`), to let ARIN allocate address space to Extra-Terrestrial Networks (defined as beyond the GEO arc — LEO and GEO excluded). It proposes hierarchically organizing allocations by "Celestial Region" (Moon, Earth-Moon Lagrange points, asteroid belt, planetary systems), prefers IPv6 with a /48 minimum, employs sparse allocation within the ETN block for growth, and relaxes utilization verification where "active host" checks are impractical for high-latency nodes.
- **How**: Topology-aligned aggregation: agencies currently select space ad hoc from multiple RIRs, forcing disaggregated announcements when deep-space networks interconnect; contiguous per-region blocks would let each gravity well aggregate to a single route advertised back to terrestrial ground stations.
- **Where applicable**: Not implementable as written — staff and legal review is explicit that it presumes unsatisfied prerequisites: an IETF determination, an IANA allocation, an ARIN Board finding that serving as (even interim) deep-space registry fits ARIN's mission, and concurrence of the other RIRs. Near-term demand is small and specialized. The precedent (first off-Earth recognition in RIR policy) and the routing-scalability framing are the real content.

### Number Resource Organization Number Council and RIR Governance Document Status Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_rirgovernance.pdf) · [Recording](https://www.youtube.com/live/-Fwz65uQp3E?t=5h51m00s)

Amy Potter, ASO AC Vice Chair / NRO NC

- **Why**: Not technical, but this is the rewrite of the constitutional document of the RIR system — including, for the first time, how an RIR gets *derecognized* and what happens to its registry in an emergency. After the AFRINIC governance crisis, this is where the field is heading institutionally, and it will shape who holds and administers number resources globally.
- **What**: A status report on Version 2 of the "RIR Governance Document" (the ICP-2 replacement), targeting finalization by Q4 2026. Key mechanics agreed or in drafting: recognition of a new RIR at "unanimity minus one" (with conflict-of-interest handling); targeted compliance reviews initiable by any group of RIRs, by 25% of an RIR's membership (or 2,000 members, whichever is lower), or by ICANN; regular audits at least every 5 years; and an Emergency Continuity procedure allowing an affected RIR to trigger continuity for itself (or others/ICANN at sub-unanimity), with an "Emergency Operator" taking over the affected RIR's services, staged transfer, and no cap on renewals.
- **How**: Multi-round global consultation (298 RIR questionnaire responses, two public comment rounds), with substantive issues tracked in published status reports.
- **Where applicable**: Global RIR system governance — affects every resource holder indirectly, and directly if you operate in a region whose RIR ever enters distress. The Emergency Operator concept is the piece to watch: it is effectively a pre-agreed continuity plan for the Internet's number registry.

## Themes

- **RPKI is shifting from signup to substance**: registration growth (25% YoY) is outpacing ROA coverage (50% of eligible blocks), and the frontier has moved to ASPA objects in production (198+ live) and trust anchor constraints. Expect tooling (ARIN Routing Intelligence, Internet2's planners) to close the operational gap next.
- **IPv6-only is being treated as the destination, not a phase**: ESnet's IPv6-only management plane, Internet2's test pod, DHCP Option 108, and finally-arriving client CLAT support (Windows 11, NetworkManager) together mark the pivot from "dual-stack forever" to "dual-stack as a transitional state that hides problems."
- **The agentic/AI workload argument for flat addressing**: ESnet explicitly framed agent-dense networks as requiring one addressing scheme and any-to-any connectivity — the first time this meeting has tied IPv6 strategy to machine/agent connectivity rather than IPv4 exhaustion.
- **Registry integrity is now an operational security discipline**: identity verification, fraud pattern analysis, and Section 12 audits at ARIN mirror classic account-takeover and entitlement-abuse work — and the data (30% of out-of-region Org IDs misannouncing within 60 days) shows why.
- **IPv4 scarcity policy is converging on out-of-region leakage**: three separate items (Section 9 thresholds, 4.10 in-region codification, staff observations of leased space crossing RIRs) all address the same phenomenon — IPv4 arbitraging across heterogeneous RIR policies.
- **Protocol-surface reduction and auth modernization at the registry itself**: retiring RWhois/Whois-RWS in favor of RDAP, killing email-based authorizations, and a sobering 3% FIDO2 adoption rate — useful reference points for anyone running legacy directory or authentication infrastructure.
