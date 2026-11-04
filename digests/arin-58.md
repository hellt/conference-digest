<!--
conference: ARIN 58 Public Policy and Members Meeting
type: operator
source_url: https://www.arin.net/participate/meetings/ARIN58
generated: 2026-11-02
registry_key: arin-58
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ARIN 58 Public Policy and Members Meeting

## Core

### Routing Security Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_routingsecurity.pdf) · [Recording](https://www.youtube.com/watch?v=RhO-2Cqaejo&t=3131s)

Brad Gorman, ARIN (Director of Customer Technical Services)

- **Why**: Routing security is squarely in the PM's network-security remit, and this is the one session with hard adoption data and a preview of ASPAs — the next RPKI object after ROAs. It also matters for anyone building products that depend on customers having their RPKI in order.
- **What**: A data-driven status report on RPKI adoption in the ARIN region plus ARIN's RPKI roadmap. Headline numbers: 9,673 organizations registered for RPKI (up 27% year over year), but roughly 1 in 7 hosted-RPKI organizations has never created a single ROA — "registered is not the same as protected." 59.4% of ARIN-registered IPv4 blocks seen in announcements are RPKI Valid. Globally, 3,389 ASPAs (Autonomous System Provider Authorizations) now exist across the five RIR repositories (2,081 at RIPE NCC, 685 at ARIN), and all five RIRs will support ASPA creation by end of 2026 as the RFC finishes ratification.
- **How**: The adoption analysis slices coverage by entity type (government vs. education vs. commercial) and by geography within the ARIN region, isolating where ROA coverage lags. On the tooling side, ARIN is building "BGP Insight": correlating prefixes on a resource certificate with what's actually seen in the global BGP table, explaining Invalid/Not Found states, showing the impact of proposed ROA changes before they're made, and presenting paths to a Valid state. Also in flight: ASPA info in the RPKI changelog, new Reg-RWS RESTful API capabilities, and inter-RIR work toward RPKI feature parity.
- **Where applicable**: RPKI validity and ASPA trends are global; the hosted/delegated/repository service tiers and the adoption figures are ARIN-region-specific. ASPA momentum is the transferable takeaway for any operator doing BGP security planning in 2027 — the object class is about to become generally creatable across all RIRs.

### Policy Block 2: Draft Policy ARIN 2026-2

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2026_2/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_2.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=19874s)

Matthew Wilder (Advisory Council; co-drafted with Alicia Trotman)

- **Why**: This is a proposal to rewrite the entire IPv6 allocation framework from formula-based sizing to documented network plans. If the PM's organization (or its customers) ever requests IPv6 space from ARIN, this changes what "justification" means — it effectively makes IPAM discipline the allocation criterion.
- **What**: A full revision of NRPM Section 6.5 that replaces rigid sizing calculations, utilization thresholds, and IPv4-dependent qualification with a planning-based evaluation model. Requests must include a network plan identifying typical assignment sizes (/48, /56, /64), the addressing hierarchy, and projected utilization at 1-, 2-, and 5-year horizons. Subsequent allocations require 75% assignment of the prefix units in the 2-year plan plus evidence deployment matched the submitted hierarchy, with ARIN issuing additional space contiguously to protect aggregation. Deployment must begin within 12 months of issuance. Community survey at the meeting: 40% support, 40% oppose, 20% neutral — genuinely contested.
- **How**: The mechanism shifts review from arithmetic (e.g., the 75%-of-/48s nibble-boundary rules elsewhere in Section 6.5) to evaluating a documented plan: hierarchy, aggregation strategy, and growth projections over defined time horizons, applied consistently to LIR and end-user/PI allocations.
- **Where applicable**: Applies to ARIN-region IPv6 allocations only, but the shift from formula-based to plan-based justification is a direction other RIRs watch. Broadly applicable to any org requesting space; the open community question — should ARIN *require* network plans, and does ARIN need to define what a plan is — is where the practical friction will land.

### IPv6 Task Force

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_ipv6taskforce.pdf) · [Recording](https://www.youtube.com/watch?v=RhO-2Cqaejo&t=7573s)

Lee Howard (ARIN Board of Trustees)

- **Why**: The task force's framing is a real shift: IPv6 adoption is "no longer principally a matter of awareness" — the remaining problem is practical deployment obstacles (IPv6-mostly, network autonomy, host/network readiness). That's exactly the territory a networking PM lives in, and ARIN is soliciting input on how to structure the program.
- **What**: A Board-chartered task force (SP 1.5) recommending the structure of an ARIN IPv6 program: identifying and prioritizing deployment obstacles, a community peer-support platform for IPv6 problems (with moderation model and code of conduct), and metrics of success. Existing efforts include an IPv6 address-planning e-learning course, outreach focused on "IPv6 Mostly" and network autonomy, and business-case/case-study blog series.
- **How**: Program plan for engagement and problem-solving, a community interaction tool for peer support, and advice on longer-term advocacy including government/public-sector engagement. Task force members are Lee Howard, Rob Seastrom, and Tina Morris, and they are explicitly asking for input on program structure and how to record and prioritize issues.
- **Where applicable**: ARIN-region outreach, but the obstacle catalog and peer-support approach are generally applicable. The notable argument in the deck: single-stack is better than dual-stack and you can't single-stack on IPv4 — plus fraud pressure on the residual IPv4 market as a driver.

### Data Accuracy Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_dataaccuracy.pdf) · [Recording](https://www.youtube.com/watch?v=RhO-2Cqaejo&t=5325s)

John Sweeting (ARIN, Chief Experience Officer)

- **Why**: Registry accuracy is network security infrastructure — the stated objectives are preventing resource hijacking and supporting law enforcement. For anyone building systems that consume WHOIS/RDAP data or dealing with hijacked/legacy space, the mechanics of how ARIN is cleaning up non-agreement holdings are directly relevant.
- **What**: Progress report on driving the remaining "not under agreement" space to zero: 372,877 /24-equivalents remain outside agreements (Q3 2026), down 26,313 quarter-over-quarter and down 81% since Q1 2024; 16,212 legacy CIDR blocks; 2,195 /24-equivalents already returned to the IPv4 waitlist. A Q4 2025 step change brought 1.28M /24-equivalents under RSAs in one quarter. The remaining center of gravity: 715 /16-sized blocks hold 49.1% of the outstanding space, and just 23 blocks of /15 or larger hold 38% of it.
- **How**: A cohort model. Cohort 1 (2,660 orgs with zero usable contact info) gets services stopped, a 12-month quarantine hold, then release via the waitlist with rights extinguished. Cohort 2 (10,218 orgs with contacts pending verification) gets targeted outreach and DAP contact validation; organizations whose contacts prove inaccurate fall back to Cohort 1. The /16 population is managed as a named list with account-level engagement.
- **Where applicable**: ARIN-registry-specific, but the quarantine-then-rights-extinguishment pattern for unreachable holders is a notable operational model for any registry-like system. The 49%-in-/16s concentration means most remaining work is a small number of very large legacy accounts.

## Adjacent

### ARIN Directory Services Roadmap

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_directoryservices.pdf) · [Recording](https://www.youtube.com/watch?v=RhO-2Cqaejo&t=8315s)

Hollis Kara (ARIN, Director of Communications)

- **Why**: Directory-data consolidation onto RDAP touches the PM's directory/identity instincts, and the Port 43 WHOIS debate is a live case study in legacy-protocol retirement politics — relevant to anyone whose tooling still scripts `whois`.
- **What**: Outcome of a community consultation on retiring three legacy services in favor of RDAP as ARIN's single directory protocol. RWhois: uncontested, retiring on a 365-day countdown after a migration tool ships. Whois-RWS: uncontested in principle, API sunset set for July 2026/2027 path (July 2027 per deck), gated on RDAP closing one parity gap (CIDR more-specifics / hierarchy walking); web UI to run in parallel with a beta Advanced RDAP Search for ~6 months. Port 43 WHOIS: real opposition — of 43 substantive comments, 24 opposed or wanted a much longer transition (56% against), 11 supported, 8 neutral — so ARIN paused and will reconsult once RDAP clients ship by default in OS distributions.
- **How**: Analysis grounded in actual query traffic (79% IP lookups, 9% ASN, 10% org) and a candid visibility caveat: the top queriers all resolve to cloud provider addresses, so ARIN can't see the real end users. Engineering judged a WHOIS-compatible proxy in front of RDAP to cost more operational risk than keeping native WHOIS running longer — the reason the proxy compromise was rejected.
- **Where applicable**: Anyone with scripts or products querying ARIN directory data. The security argument (unauthenticated, unencrypted, MITM-tamperable) vs. the ecosystem-readiness argument (RDAP clients not yet default in OS distros) is the transferable lesson for any forced protocol migration.

### Policy Implementation and Experience Report

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policyimplementation.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=2301s)

John Sweeting (ARIN, Chief Experience Officer)

- **Why**: The rare policy session with quantified operational results, and the waitlist/transfer mechanics matter to any org acquiring or moving IPv4 space.
- **What**: Three implementation reviews. (1) The waitlist multi-block question: policy forces single contiguous blocks, so an org qualifying for a /22 that accepts down to a /24 gets one /24 even when four noncontiguous /24s are free — staff asked the community whether that restriction, aggregation-driven, is still necessary. (2) The NRPM 8.3/8.4 12-month recipient-to-source wait is invisible in the recipient-facing policy text, causing surprises. (3) ARIN-2025-2 (implemented 3 March 2026) removed the "within the last two versions" RSA constraint: of 490 transfer-participating orgs in the first six months, 72 were spared a new RSA — faster transfers, less legal overhead (vs. 11.7% forced re-signing in the prior six months).
- **How**: Staff-experience reporting with before/after ticket-level numbers, feeding directly into new policy proposals (several ARIN-2025/2026 items originated here).
- **Where applicable**: ARIN-region transfer and waitlist operations; broadly relevant as a model of policy-implementation feedback loops.

### Policy Block 1: Recommended Draft Policy ARIN-2025-7

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2025_7/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_7.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=11228s)

Lily Botsyoe (Advisory Council; co-presented with Leif Sawyer)

- **Why**: A concrete IPAM rule fix — the sizing table for IPv6 end-user allocations — that any org planning IPv6 address structure should know is changing.
- **What**: Fixes a math loophole in NRPM 6.5.8.2: the "75% of /48s in a prefix" rule accidentally qualified single-site organizations for a /44, contradicting the examples. The revision makes a single site = /48, with 2–12 sites = /44, 13–192 = /40, 193–3,072 = /36, 3,073–49,152 = /32, and renames "assignment" to "allocation" throughout to match current ARIN practice.
- **How**: Pure text clarification; staff review says no operational change, implementable in 3 months, strong community support.
- **Where applicable**: Any ARIN-region org requesting IPv6 end-user allocations; the nibble-boundary site-count table is the durable takeaway for IPv6 address planning.

### Policy Block 1: Recommended Draft Policy ARIN-2025-1

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2025_1/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_1.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=8418s)

Leif Sawyer (Advisory Council; co-drafted with Elizabeth Goodson)

- **Why**: Defines who counts as an LIR vs. an ISP across the whole policy manual — which determines which allocation rules apply to the PM's org and its customers.
- **What**: Creates an explicit ISP definition (connectivity, web services, colocation, dedicated/VPS, VPNs), rewrites the LIR definition (LIRs include but aren't limited to large enterprises, universities, and ISPs), and replaces "ISP" with "LIR" throughout the NRPM — treating ISP as a type of LIR, not an equivalent.
- **How**: Terminology harmonization; notably it states all LIRs without IPv4 automatically qualify for an initial /24 (up to /22 with a 24-month plan). Staff estimate six months to implement due to docs/systems updates; no material change to how requests are evaluated.
- **Where applicable**: ARIN-region allocation eligibility. Relevant to enterprises and universities that didn't previously self-identify as LIRs — they're now explicitly in scope.

### Policy Block 1: Recommended Draft Policy ARIN-2025-3

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2025_3/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_3.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=9444s)

Gerry George (Advisory Council; co-drafted with Matthew Wilder)

- **Why**: The out-of-region-use rules govern when ARIN space can be deployed outside the ARIN region — a real constraint for anycast or multinational deployments rooted in ARIN allocations.
- **What**: Lowers the in-region IPv4 utilization threshold to justify out-of-region use from /22 to /24. Staff review flags the sharp edge: with no maximum on out-of-region requests, a single in-region /24 could unlock substantially larger blocks deployed entirely outside the region. An amendment also bars using out-of-region justification for waitlist, micro-allocation (4.4), and IPv6-deployment (4.10) space — which drew community objection as an unrelated, precedent-setting restriction on waitlist eligibility by *intended use*.
- **How**: Single-text threshold change with carve-outs; implementable in 3 months.
- **Where applicable**: ARIN-region resource holders with any non-ARIN-region deployment; the community fight over the waitlist restriction is the part worth watching.

### Policy Block 2: Draft Policy ARIN 2026-5

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2026_5/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_5.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=23541s)

Gus Reese (Advisory Council; co-drafted with Bill Herrin)

- **Why**: Directly resolves the anycast ambiguity: the question of whether geographically diverse (anycast) use of ARIN space counts as "out of region" has been a recurring community concern.
- **What**: Adds a definition of Out Of Region Use to the NRPM: "the *sole* use of ARIN-allocated resources in locations outside the ARIN service region" — explicitly excluding simultaneous use of a resource both inside and outside the region.
- **How**: One definitional section; new to the PPML as of September 2026, feedback pending.
- **Where applicable**: Any ARIN resource holder doing anycast or multi-region deployment — this is the clarification that keeps anycast out of Section 9's restrictions.

### Policy Block 1: Recommended Draft Policy ARIN-2025-8

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2025_8/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_8.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=16280s)

Kaitlyn Pellak (Advisory Council; co-drafted with E. Marie Brierley)

- **Why**: Closes an abuse vector in the last ARIN-controlled IPv4 pool — relevant to anyone tracking where fraudulent IPv4 leasing/announcement pressure comes from.
- **What**: Codifies that 4.10 space (dedicated IPv4 allocations to facilitate IPv6 deployment) may only be used within the ARIN service region, adding "within the ARIN service area" to NRPM 4.10. ARIN's Registry Integrity Report identified 4.10 as the highest-target pool for fraud: announced out of region, reassigned to customers, leased, or announced with no associated IPv6.
- **How**: One-sentence amendment codifying existing staff practice; implementable in 3 months, overwhelmingly positive meeting feedback.
- **Where applicable**: 4.10-space holders only, but a useful data point on which IPv4 pools fraudsters target as scarcity deepens.

## Wildcard

### Policy Block 2: Draft Policy ARIN 2026-1

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2026_1/) · [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_1.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=17410s)

Alison Wood (Advisory Council; co-drafted with Brian Jones)

- **Why**: The most novel thing in the program: a first-of-its-kind proposal to allocate IP address space for networks beyond Earth orbit, with topological aggregation by celestial region. Even in draft form, it signals where hierarchical addressing thought is heading and is tightly coupled to a live IETF working group.
- **What**: "Taking IP To Other Planets" (TIPTOP) would let ARIN allocate IPv4/IPv6 for extra-terrestrial networks (beyond GEO — the Moon, Mars, Lagrange points), organized hierarchically by celestial region so lunar/planetary prefixes can aggregate into single advertisements back to terrestrial ground stations. Staff's verdict: *not implementable as written* — it presumes IETF determination that dedicated space is needed, IANA allocation, RIR concurrence on who runs the registry, and a Board mission-scope decision. Meanwhile the IETF TIPTOP WG advanced its use-case and IP-architecture documents, and a joint IPv6 address-space draft (draft-limarsjenwar-tiptop-address-space-00, by Li, Eubanks, Atkinson, Kumari, and Linkova) was published 15 September, asking IANA for dedicated space with suballocation per celestial body and the NRO to determine allocation within celestial bodies.
- **How**: Policy defines an Extra-Terrestrial Network, a dedicated allocation pool, sparse allocation within the ETN block to allow growth without fragmentation, and utilization exceptions where "active host" verification is impractical (high-latency cold-storage nodes, orbital relays).
- **Where applicable**: Aspirational and multi-year; contingent on IETF/IANA/NRO process. Watch it as an addressing-architecture thought experiment — aggregation-by-gravity-well is the interesting design idea, and the deep-space transport assumptions (intermittent links, buffering, long delay) are in the WG documents.

### Address Supporting Organization Address Council (ASO AC) Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_asoacupdate.pdf) · [Recording](https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=25095s)

Kevin Blumberg (ASO AC / NRO NC)

- **Why**: Not a technical talk, but it covers a genuine structural shift in Internet governance: the multi-year ICP-2 rewrite that will define how an RIR can be audited, placed under emergency operation, or derecognized. That's the failure-domain design of the registry system itself — worth one read even for a purely technical PM.
- **What**: Status of the RIR Governance Document: a recommended draft published 1 September 2026 after two consultation rounds, now with ICANN for consideration after productive discussions at ICANN 87. Key changes: a five-year regular audit cycle, a distinct Compliance Review process with misuse safeguards, Rehabilitation Plans as the preferred path, a Temporary Emergency Continuity Arrangement an affected RIR can initiate for its own services (90-day limit, two-thirds RIR threshold), a derecognition process requiring two-thirds RIR support excluding the subject RIR, and amendment freezes during emergency arrangements or pending derecognition.
- **How**: Multi-stakeholder consultation timeline running since October 2024; open mailing lists and ASO AC teleconferences; Oscar Robles selected to fill the vacant ICANN Board Seat 9.
- **Where applicable**: Governance-level; affects all five RIRs. No operator action, but it is the framework that would govern any future RIR failure — the "datacenter redundancy plan" equivalent for the registry layer.

## Themes

- **RPKI is hitting the "registered ≠ protected" wall**: adoption grows (9,673 orgs, +27% YoY) but ~1 in 7 hosted orgs has zero ROAs and only 59.4% of announced ARIN IPv4 is Valid; the frontier is moving from ROAs to ASPAs, creatable at all five RIRs by end of 2026.
- **IPv6 allocation policy is being rebuilt around network plans**: 2026-2 replaces formula-based sizing with documented hierarchy and 1/2/5-year projections, 2025-7 fixes the site-count sizing table, and the Task Force reframes adoption as an obstacle-removal problem — IPAM discipline is becoming the allocation criterion.
- **Registry hygiene is being treated as security work**: the data-accuracy program uses quarantine and rights-extinguishment for unreachable holders, and the remaining unagreed space is concentrated in a few hundred /16s — fraud pressure on residual IPv4 (4.10 space worst) is the stated driver.
- **Legacy protocol retirement is political**: RDAP consolidation is uncontested except Port 43 WHOIS, where OS client readiness beat the security argument — a reusable lesson for any forced protocol migration.
- **Addressing is stretching beyond terrestrial topology**: TIPTOP and the IETF joint draft propose aggregation by celestial region, the first serious attempt at topological addressing outside Earth's gravity well.
- **The IPv4 endgame dominates policy ops**: waitlist mechanics, transfer RSAs, out-of-region thresholds, and anycast carve-outs — nearly every implementation-experience item traces back to scarcity economics.
