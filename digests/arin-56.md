<!--
conference: ARIN 56 Public Policy and Members Meeting
type: operator
source_url: https://www.arin.net/participate/meetings/ARIN56
generated: 2026-11-04
registry_key: arin-56
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ARIN 56 Public Policy and Members Meeting — Digest

ARIN 56 is a policy and governance meeting, not a deep-technical conference, so the yield for hands-on networking work is concentrated in a handful of operational updates: RPKI, DNSSEC trust-anchor operations, registry directory services, and Geoff Huston's macro view of Internet evolution. The rest of the program is NRPM policy text changes and RIR governance, of which the IXP micro-allocation rewrite and the inter-RIR transfer data are the pieces with real operational consequences.

## Core

### Routing Security Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_routingsecurity.pdf) · [Recording](https://www.youtube.com/live/BV3Izae-f8I?t=5377s)

Brad Gorman, Director of Customer Technical Services, ARIN

- **Why**: RPKI is now table stakes for anyone announcing space, and this is the one session with concrete adoption data plus ARIN's roadmap for ROA tooling. Directly relevant to BGP/routing security work.
- **What**: A data-driven state-of-RPKI report plus new features. Global RPKI-valid share of announced space rose from ~54% (Dec 2024) to ~57% IPv4 / ~59% IPv6 (Sep 2025, per NIST's monitor), with ARIN openly asking whether a plateau is coming. 7,612 organizations now use ARIN's RPKI services (39% YoY growth); 97.8% choose hosted RPKI, only 161 run delegated (88 of those on ARIN's Repository Publication Service). 47.1% of ARIN-allocated IPv4 is RPKI-valid. New shipped: ROA Modify, a year of ROA change history with CSV export, automatic ROA re-rolling during resource transfers, and ASPA object support in OT&E.
- **How**: The interesting roadmap items are "RPKI Routing Intelligence" (show users live BGP announcements against their certificate, explain RPKI-invalid states, and offer a fix-the-ROA flow) and RPKI for reallocated/reassigned resources — letting direct holders delegate RPKI decision rights to downstream recipients, revocable at any time.
- **Where applicable**: Any org announcing ARIN-region space; the hosted-vs-delegated guidance is broadly applicable. ASPA support in OT&E is an early signal for anyone planning ASPA adoption. Entity-type data (gov at 18.4% org adoption but 6.7% prefix coverage) is ARIN-region-specific.

### ICANN/IANA Update

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_ianaupdate.pdf) · [Recording](https://www.youtube.com/live/9gvjMYs6XT0?t=5808s)

James Mitchell, IANA/ICANN

- **Why**: Two operationally significant DNSSEC events are on the calendar, and every operator running a validating resolver needs them on a roadmap, not a surprise.
- **What**: The second-ever Root Zone KSK rollover is scheduled for 11 October 2026, establishing a recurring 3-year rollover cycle (delayed by COVID and a key-hardware vendor change). Separately, a proposal to change the KSK algorithm from RSA/SHA-256 to ECDSA P-256 with SHA-256 goes to public comment in February 2026. The trust anchor has been published in the DNS itself since 11 January 2025; operators should verify their systems have adopted it via software updates.
- **How**: Rollover propagates through vendor updates and the XML trust-anchor file rather than manual operator action for most deployments; the algorithm change is a slower, more disruptive migration being run through open IETF/community process. Also noted: `.arpa` domains are being published in the RDAP bootstrap (reverse-DNS queries will redirect to the relevant RIR) as ICANN sunsets WHOIS, and IANA is investigating participating in RPKI for reserved or special-use space — an early watch item.
- **Where applicable**: General — anyone operating validating resolvers or DNSSEC-signing infrastructure. The RPKI-for-special-use-space item is exploratory but relevant to routing-security watchers.

### ARIN Directory Services

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_directoryservices.pdf) · [Recording](https://www.youtube.com/live/9gvjMYs6XT0?t=21573s)

Mark Kosters, Chief Technology Officer, ARIN

- **Why**: ARIN runs four redundant directory services (Whois port 43, RWhois, Whois-RWS, RDAP) and is preparing a consultation to retire three of them. If your security tooling, abuse workflows, or automation still hits port 43 or the whois.arin.net REST API, this is a deprecation notice in embryo.
- **What**: ARIN proposes retiring RWhois (a 2013 community suggestion, requirement already removed from the NRPM but users remain — the migration path is RDAP, possibly with an ARIN-built translation tool, or pushing reassignment data into ARIN's database), retiring the Whois-RWS API (web front end would move to an RDAP backend), and eventually retiring Whois port 43 itself. Context: since ICANN dropped the Whois requirement for gTLDs in January 2025, at least 139 gTLDs have shut theirs off; usage is falling on the domain side of the industry.
- **How**: Consolidation on RDAP (RFC 7480–7485, 9224), which has defined queries/results, 26 client implementations, 11 authoritative server implementations, UTF-8, auth support, and emerging extensions for geolocation and RPKI registration data. A formal ARIN consultation is forthcoming.
- **Where applicable**: Broadly applicable to anyone consuming registry data programmatically; org-specific urgency depends on whether you run RWhois for delegated reassignments or have scripts against port 43 / Whois-RWS.

## Adjacent

### Internet Evolution and IPv6

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_ipv6evolution.pdf) · [Recording](https://www.youtube.com/live/9gvjMYs6XT0?t=27084s)

Geoff Huston AM, Chief Scientist, APNIC

- **Why**: The best strategic talk on the program. Huston connects trends the PM cares about — edge delivery, the end of per-core performance scaling, and why the DNS has quietly become the Internet's identity layer.
- **What**: The argument: abundant fiber capacity, compute, and storage shifted provisioning from on-demand to just-in-case, shrinking "packet miles" and pushing service to the edge. The warning: processor clock speeds topped out a decade ago, so the IPv4-workaround stack (NAT, dynamic naming, content steerage) embeds ever more per-packet processing into infrastructure that no longer scales exponentially — IPv6 is the complexity-reduction escape valve, which is what India's and China's adoption curves show. The reframe: identity and authenticity credentials now attach to service names, not IP addresses; IP addresses are mere topology tokens dynamically bound by DNS — and that binding is masking dual-stack, removing traditional pressure from the IPv6 transition.
- **How**: A synthesis of capacity, compute, and adoption trend data rather than a mechanism; the "application is the service" framing ties CDN/edge architecture to naming and identity.
- **Where applicable**: General and vendor/region-agnostic; most useful as input to multi-year network strategy and IPv6 business cases rather than immediate operations.

### Policy Implementation and Experience Report

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_policyimplementation.pdf) · [Recording](https://www.youtube.com/live/9gvjMYs6XT0?t=3251s)

John Sweeting, Chief Experience Officer, ARIN

- **Why**: The one session with hard numbers on the IPv4 transfer market and an honest account of where policy text fails operational reality — useful for anyone acquiring address space or watching IPv4 market mechanics.
- **What**: Three findings. (1) Section 4.10 (IPv4 for IPv6 deployment): ARIN cannot detect when IPv6 reallocations/reassignments are removed downstream, so it keeps landing in resource-intensive Section 12 audits — staff asked whether the policy needs rewriting. (2) The initial /24 policies (4.2.2/4.3.2) never stated in-region-only use, and have been broadly interpreted; staff suggests codifying it. (3) Inter-RIR transfers: 2020–2025 ARIN sent 126,326 /24-equivalents to RIPE NCC vs 38,176 received; in 2024 alone, 30,747 out vs 16,293 in. A single large broker moved 1,792 /24s for "network operational needs" into RIPE NCC, mostly now leased — driven by RIPE's permissive temporary-transfer/leasing policy vs ARIN's and LACNIC's stricter stances.
- **How**: Policy-experience reporting with transfer tables and a cross-RIR comparison of needs-based tests and leasing rules as the explanatory mechanism.
- **Where applicable**: Directly relevant to orgs buying/selling/leasing IPv4 or operating multi-region; the policy divergence analysis explains why transfer flows are so lopsided.

### Policy Block 1: ARIN-2024-5: Rewrite of NRPM Section 4.4 Micro-Allocation

**Links:** [Abstract](https://www.arin.net/participate/policy/drafts/2024_5/) · [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_2024_5.pdf) · [Recording](https://www.youtube.com/live/9gvjMYs6XT0?t=9504s)

Chris Woodfield, ARIN Advisory Council

- **Why**: This is the one policy text change with direct fabric-adjacent consequences: it rewrites the rules for the dedicated pool IXPs and core DNS operators draw IPv4 from, and it resolves the long-standing ambiguity about whether IXP space may be routed.
- **What**: A Recommended Draft (closest to adoption of anything on the docket) renaming Section 4.4 from "Micro-Allocation" to "Critical Internet Infrastructure (CII)" allocations. Key terms: a /15-equivalent reserved for CII; allocations no smaller than /24, sparse where practical; IXPs must justify with at least three initial participants not under common control on a shared *physical switching fabric* (with ASNs and contacts named; the IXP's own ASNs don't count); IXP space may be publicly announced at the operator's discretion but must be used only for IXP operations; gTLD operators capped at a /23-equivalent per gTLD from the free pool or transfers, not the reservation; 24-month supply requests; renumber-and-return within 12 months when expanding; ARIN publishes a record of all 4.4 allocations.
- **How**: Policy text with an implementable-as-written staff review, ~3-month implementation, and a full community-feedback trail (including pushback that "CII" is an arbitrary definition and on gTLD treatment).
- **Where applicable**: IXP operators and root/ccTLD/gTLD operators in the ARIN region; indirectly relevant to anyone engineering IX fabrics or peering policy, since it shapes what appears (and routes) on exchange fabrics.

### NRO EC Update and State of the RIR System

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_nroecupdate.pdf) · [Recording](https://www.youtube.com/live/BV3Izae-f8I?t=9252s)

John Curran, President and CEO, ARIN (NRO Executive Committee Vice Chair)

- **Why**: Current-state context for the global registry system, including the AFRINIC situation and a concrete IANA SLA change affecting reverse DNS operations.
- **What**: The NRO's report covering: close monitoring of AFRINIC (coordination with ICANN, support offered to the private receiver, engagement with the African community, and a welcome to the newly elected AFRINIC board); the first amendment to the IANA Services SLA (November 2024) adding reverse-DNS resolution service levels for `ip6.arpa`, `in-addr.arpa`, and the two `-servers.arpa` zones; and the NRO RPKI Program, whose goals are a single spec interface for entities interacting with multiple RIRs plus better cross-RIR robustness and consistency.
- **How**: Governance and coordination reporting — NRO cost distribution (ARIN pays 32.71%), coordination groups, and the IANA Review Committee structure.
- **Where applicable**: General awareness; the reverse-DNS SLA and NRO RPKI program are the two items with eventual operational touchpoints for multi-RIR organizations.

## Wildcard

### ASO AC Update/ICP-2 Consultation

**Links:** [Slides](https://www.arin.net/participate/meetings/ARIN56/materials/arin56_asoacupdate.pdf) · [Recording](https://www.youtube.com/live/BV3Izae-f8I?t=2614s)

Amy Potter, ASO Address Council (ARIN region)

- **Why**: Not a networking topic, but a rare look at hard governance machinery being redesigned in public — derecognition of failing RIRs, emergency continuity, audit triggers — which will shape who holds the keys to Internet number resources for the next decade.
- **What**: The revised "RIR Governance Document" (ICP-2's replacement, consultation closed 7 November 2025) introduces: recognition of a new RIR without unanimous existing-RIR support if an ICANN-appointed third party finds a dissenting RIR made a material error; derecognition proposals initiable by 2,000 members or 25% of an RIR's membership (whichever is lower) or by ICANN (though derecognition still needs RIR approval); ad hoc audits requestable by RIR majority (previously unanimous), member threshold, or ICANN; mandatory periodic audits at least every three years; a new Emergency Continuity procedure to temporarily transfer an RIR's responsibilities to an "Emergency Operator" (90-day cap, unanimous RIR+ICANN agreement, mandatory published postmortem); a required member dispute-resolution mechanism; and an explicit good-faith clause.
- **How**: Legal-structural mechanisms — thresholds, third-party review, time-boxed emergency authority with sunset and public review — rather than technology.
- **Where applicable**: Governance watchers and multi-RIR organizations; clearly shaped by the AFRINIC experience, and the feedback loop was still open at meeting time.

## Themes

- **RPKI is shifting from opt-in to operational default** — validity at ~57–59% globally, ARIN signups up 39% YoY — and the tooling is moving up the stack: change logs, transfer automation, BGP-aware advisories, and ASPA in test. The open question ARIN itself raised is whether adoption plateaus before full coverage.
- **The registry data plane is consolidating on RDAP.** ARIN's proposed retirement of Whois, RWhois, and Whois-RWS mirrors the gTLD world's post-WHOIS migration (139 gTLDs already dropped it). Anyone with scripts against port 43 has a migration coming.
- **IPv4 scarcity economics are visibly distorting policy.** Inter-RIR transfer flows are heavily asymmetric toward RIPE's permissive leasing regime, and nearly every policy proposal on the docket (out-of-region use minimums, 4.10 in-region reservation, initial-allocation in-region use) is a reaction to space leaking out of region or into lease markets.
- **RIR governance is being hardened in AFRINIC's shadow.** The ICP-2 rewrite adds derecognition triggers, audits, and an emergency-operator procedure — accountability mechanics the 25-year-old framework never had.
- **Huston's counterintuitive take worth carrying forward**: the DNS-as-identity binding has *reduced* pressure on IPv6 transition by masking dual-stack, meaning IPv6 adoption will be driven by scale economics (India, China) rather than Western migration urgency — while the end of per-core processing scaling quietly raises the cost of every NAT-and-steerage workaround left in the network.
- **DNSSEC operational milestones are stacked**: KSK rollover October 2026, a proposed ECDSA algorithm change in comment February 2026, and reverse-DNS service levels newly added to the IANA SLA.
