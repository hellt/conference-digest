<!--
conference: MORE-IP 2025
type: operator
source_url: https://more-ip-event.net/more-ip-2025/agenda/
generated: 2026-11-04
registry_key: moreip-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# MORE-IP 2025

A note on this program: it is an operator event built around AMS-IX's own technical track, and most sessions have **no published abstract** — only titles, speakers, and (for some) a track subtitle. Only `video:` links exist; no `page:` or `pdf:` sources were available to fetch. Write-ups below are grounded in the title, speaker affiliation, and track text only, flagged per item; nothing beyond that has been invented.

## Core

### Defending Europe against DDoS in a multi-polar world

**Links:** [Recording](https://www.youtube.com/watch?v=f3VsWS03-lc)

Octavia de Weerdt - NBIP Foundation

- **Why**: DDoS defense is squarely in the PM's network-security remit, and this is a practitioner's view of how European defensive coordination is holding up as geopolitics fragment the old assumptions. It is also a rare operator talk about collective defense — scrubbing and mitigation as shared infrastructure — rather than a box to buy.
- **What**: A talk on defending European networks against DDoS in a "multi-polar world" — the framing implies a shift from treating DDoS as a generic nuisance to treating it as a geopolitical threat with national/European-scale response structures. (No abstract published — from title and speaker only.)
- **How**: Not stated in the program. Context: the speaker is from NBIP Foundation, the Dutch not-for-profit known for operating the shared NaWas scrubbing service; expect the mechanics of cooperative scrubbing and member-driven defense to be the likely substance.
- **Where applicable**: European operator/internet-infrastructure environments; the collective-scrubbing model presumes a community of connected networks and national coordination. Broadly transferable to any multi-tenant mitigation effort; the geopolitical framing is Europe-specific. *No abstract published; treat this write-up as title-level only.*

### SNEAK PREVIEW – The ERIK Protocol for use with the RPKI

**Links:** [Recording](https://www.youtube.com/watch?v=65wifHK4nWc)

Job Snijders - PeeringDB

- **Why**: New protocol work in routing security is rare and slow-moving; a sneak preview from Job Snijders (a long-time RPKI/BGP practitioner) is one of the more forward-looking items on the program. Anyone whose products touch routing security or trust-anchor infrastructure should see what shape this takes before it lands in drafts.
- **What**: A first public preview of a proposed protocol intended to work with the RPKI. The program gives no further detail on ERIK's purpose or mechanism. (No abstract published — from title and speaker only.)
- **How**: Not stated. Given the RPKI framing, the plausible design space is signing/publication/validation extensions around the existing RPKI object model — but the program text does not say this, so do not plan on specifics until the draft or slides are published.
- **Where applicable**: Any environment that consumes or publishes RPKI data — IXPs, operators, and vendors of routing-security tooling. Early-stage protocol work; expect it to signal direction rather than be deployable. *Title-level only; the value here is being early to it.*

### Juniper Migration Journey

**Links:** [Recording](https://www.youtube.com/watch?v=swv2lqzaQKw)

Leroy de Vos - AMS-IX

- **Why**: A large exchange platform migrating its core to Juniper is exactly the kind of hard-won operator postmortem this PM values: multi-year hardware/vendor cutover on live infrastructure, with all the migration sequencing, risk management, and "what we'd do differently" detail that transfers across environments. Given the PM's core interest in switching and fabric operations, this is the program's most concrete systems talk.
- **What**: An AMS-IX technical-track session recounting the organization's migration of its exchange platform to Juniper. (No abstract published — from title and track only.)
- **How**: Not stated; presumably the migration plan, cutover approach, and lessons learned for running a production fabric through a vendor transition.
- **Where applicable**: AMS-IX-specific in topology (one of the world's largest IXes), but the migration-management lessons — how you stage a cutover of a system that cannot go down — apply to any operator replacing core switching or routing platforms. *No abstract; write-up is from the title and Technical Track designation only.*

### IPv6-only IXPs Are Coming?

**Links:** [Recording](https://www.youtube.com/watch?v=mYbkT1vVC6k)

Aleksi Suhonen - TREX Tampere Region Exchange Oy

- **Why**: IPv6-only operations are the concrete form of "IPv4 exhaustion planning," and an IXP is a good forcing function: if an exchange runs v6-only, its members must follow. For a PM whose portfolio includes DC/WAN interconnect and IPAM, this is a preview of a real operational shift rather than a compliance checkbox.
- **What**: A talk arguing (or asking, per the title's question mark) whether IPv6-only IXPs are imminent, presumably drawing on TREX's experience as a small regional exchange. (No abstract published — from title and speaker only.)
- **How**: Not stated. TREX is known in the operator community for having run IPv6-only peering experiments; expect the practical mechanics — v6-only peering, translation/NAT64 for stragglers, member readiness — to be the substance.
- **Where applicable**: Most immediately relevant to small/regional IXPs and their members, where the coordination problem is tractable; the big hub IXes will lag. For enterprise/cloud PMs, it's a leading indicator for when multi-cloud and interconnect products need first-class v6-only paths. *Title-level only; the TREX-experiment framing is background context, not program text.*

### From zero to SSL Automation

**Links:** [Recording](https://www.youtube.com/watch?v=aGz2qWU3wrg)

Daniel Osielczak - AMS-IX

- **Why**: Certificate lifecycle automation is a persistent pain point in both enterprise security and identity infrastructure, and "from zero" stories are the useful kind — the adoption path, not the finished state. The track line says this covers securing both internal and external environments, which is exactly the split most orgs struggle with.
- **What**: An AMS-IX technical-track session on building out SSL/TLS certificate automation from nothing, applied to both internal and external-facing environments. (No abstract published — from title and track subtitle only.)
- **How**: Not stated. "SSL automation" in current practice almost always means ACME-style issuance and renewal, but the program does not specify; the interesting content will be the internal-environment half, which is usually the hard part (discovering what exists, getting non-web workloads onto automated issuance).
- **Where applicable**: Broadly applicable to any org with a certificate estate — this is not IXP-specific. Watch for whether their internal PKI approach assumes AD-integrated enterprise tooling or something more portable. *Title and track-subtitle only.*

## Adjacent

### Farewell, Legacy

**Links:** [Recording](https://www.youtube.com/watch?v=cvWaFnE2NJc)

Ivan Kovacevic - Codetribe

- **Why**: The track line — "Boosting Security, Scalability, and Performance" — plus a title about retiring legacy systems reads as a decommissioning/legacy-modernization story. Getting rid of legacy is one of the few levers that improves security, scalability, and performance simultaneously, and the failures in such projects are instructive.
- **What**: A technical-track talk about retiring legacy systems, framed as a security/scalability/performance play. (No abstract published — from title and track only.)
- **How**: Not stated. The interesting unknowns are what "legacy" means here (code, hardware, process) and how they handled the dependency unblocking that kills most retirement projects.
- **Where applicable**: Unclear whose environment this describes — the speaker is from Codetribe, an external consultancy, so this may be a client story or general practice guidance. Treat as transferable by default but verify scope. *Title-level only.*

### Traffic Statistics

**Links:** [Recording](https://www.youtube.com/watch?v=K-WeHK3IFWI)

Steven Bakker - AMS-IX

- **Why**: "Counting for Beginners" is a disarming title for what is usually the hardest measurement talk of the day: how you actually produce trustworthy traffic numbers on a shared fabric — counter semantics, sampling, aggregation, and what the numbers mean (and don't). Measurement methodology is foundational for anyone building network telemetry features, and IXes are among the best places to learn it because the incentives to be honest are high.
- **What**: An AMS-IX technical-track session on how traffic statistics are counted at the exchange. (No abstract published — from title and track subtitle only.)
- **How**: Not stated; expect the mechanics of per-member traffic accounting and the pitfalls of naive counting.
- **Where applicable**: AMS-IX-scale shared fabric, but the counting-methodology lessons (counter rollover, interval semantics, aggregation honesty) generalize to any traffic-reporting product. *Title and track-subtitle only.*

### Giving our Birds a New Pair of Wings

**Links:** [Recording](https://www.youtube.com/watch?v=swv2lqzaQKw)

Stavros Konstantaras - AMS-IX

- **Why**: Included with a caveat: no abstract exists, and the title is opaque. The "Birds" wording in an AMS-IX technical track immediately following a platform-migration talk strongly suggests the BIRD routing daemon used for IXP route servers — i.e., a route-server software upgrade/re-architecture story, which would sit squarely in the PM's BGP-internals interests. But this is inference, not program text.
- **What**: An AMS-IX technical-track session; subject matter not published. (No abstract published — from title only.)
- **How**: Unknown. If the BIRD-route-server reading is right, expect content on route-server policy, filter management, or the upgrade path for a service thousands of members depend on.
- **Where applicable**: Unknown without a description. *Title-level only — verify against the recording before investing attention; the BIRD interpretation is speculation, clearly flagged as such.*

### Panel: Cross-IX: Easy Peering across IXPs

**Links:** [Recording](https://www.youtube.com/watch?v=u3AzdAdQKhE)

Mauro Roberto Magrassi - MIX, Simon Muyal - France-IX, Karin Ahl - Netnod, Mike Baron - AMS-IX

- **Why**: Federated peering across exchanges touches the PM's interconnect interests: the panel mixes four European IXes discussing making peering work across their platforms. Whatever mechanism they discuss — remote peering, shared member provisioning, or inter-IX policy — is a signal about where interconnect product friction is heading.
- **What**: A panel on enabling peering across IXP boundaries, with representatives from four exchanges. (No abstract published — from title and panel composition only.)
- **How**: Not stated; likely covers the operational and trust questions of cross-exchange peering rather than a single mechanism.
- **Where applicable**: Multi-IX European peering ecosystems; relevant to anyone building interconnect or peering products that span exchanges. *Title-level only.*

### Panel: Securing the Vital Digital Infrastructures

**Links:** [Recording](https://www.youtube.com/watch?v=YpHoGptvGi4)

Lieuwe-Jan Koning - On2it, Peter van Burgel - AMS-IX, Alex de Joode - AMS-IX

- **Why**: A policy-plus-practice panel on treating internet exchange-class infrastructure as critical infrastructure, with AMS-IX's CEO and its security leadership. Not a technique talk, but useful context for how the regulatory and threat landscape around critical network infrastructure is being framed in the EU.
- **What**: A panel on securing vital digital infrastructure. (No description published — from title and speakers only.)
- **How**: Not stated; the presence of AMS-IX's CISO-adjacent leadership (de Joode) suggests it will cover both governance and operational security practice.
- **Where applicable**: European critical-infrastructure framing (NIS2-adjacent); relevant as context for compliance-driven product decisions in the EU, not as a technique. *Title-level only.*

## Wildcard

### Panel: The Power of Precision: Why Time as a Service Matters

**Links:** [Recording](https://www.youtube.com/watch?v=G9-59S_wlmo)

Jos van Eycken - Adtran, Michael van Schaik - VSL, Jan van Boeschoten - AMS-IX, Erwin uit de Bos - Digital Realty, Miguel Regalado Querol - AMS-IX

- **Why**: Not something this PM would search for, but the panel composition is the tell: a national metrology institute (VSL), an optical/timing vendor (Adtran), a datacenter operator (Digital Realty), and an IX. That mix means the talk is about distributing precision timing (think PTP-class accuracy) as a commercial/managed service into datacenters — a small field today that grows as 5G, sensing, HFT, and distributed measurement workloads demand better than NTP.
- **What**: A panel arguing for "time as a service" — delivering precision timing as an offered service rather than something each operator builds. (No description published — from title and panel composition only.)
- **How**: Not stated. The mechanics to listen for: how precise timing survives last-mile distribution into a facility, how it's monitored and held to SLA, and what a DC operator (Digital Realty's presence) has to change to deliver it.
- **Where applicable**: Multi-tenant facilities and any operator whose customers need audited, accurate time; the metrology-institute involvement suggests a standards/traceability angle. Genuinely emerging — few places to hear this discussed. *Title and panel-composition only; this is the program's best "glad I saw it" pick.*

### The Floor

**Links:** [Recording](https://www.youtube.com/watch?v=ykximzsyxEc)

Bas Hickendorff - AMS-IX

- **Why**: The track line — "Access the right data, under your terms, at the best price" — frames this as a talk about network/traffic **data as a marketable product**: who owns it, who gets it, and at what cost. For a PM, the shift from telemetry being a free byproduct to being a priced, permissioned product is a real trend (the same debate happening around AI-training data and cloud egress data). This is a small session pointing at a big question.
- **What**: An AMS-IX session on accessing data under controlled terms and pricing, apparently centered on a data-access product or platform ("The Floor"). (No abstract published — from title and track subtitle only.)
- **How**: Not stated; expect the mechanics of data access tiers, terms, and pricing for network traffic data.
- **Where applicable**: AMS-IX's platform initially, but the data-as-a-product pattern is broadly relevant to any operator sitting on traffic data. Watch for whether it's product announcement or market discussion. *Title and track-subtitle only.*

## Themes

- **Platform modernization is the story of the moment**: the Juniper migration, "Farewell, Legacy," and the Birds session all point to operators replacing decade-old core infrastructure and telling the cutover stories — the classic second-generation systems problem arriving at IXes.
- **Routing security is getting protocol-level attention again**: a *new* RPKI-adjacent protocol preview (ERIK) alongside national-scale DDoS defense shows routing trust and volumetric threats treated as first-class engineering problems, not just filtering hygiene.
- **IPv6-only is moving from thought experiment to pilot**: the IPv6-only IXP talk signals that the exhaustion endgame is now being operationalized at the (smaller) exchange level first, dragging member networks along.
- **Security lifecycle automation as a from-zero project**: the SSL automation talk reflects that cert automation is now table stakes but rarely started — and the internal environment is the unsolved half.
- **Interconnect as a federated service**: cross-IX peering, shared DDoS scrubbing, and cross-IX cooperation collectively sketch IXes becoming a coordinated service layer rather than isolated switching fabrics.
- **Data and time as monetizable services**: "The Floor" and the time-as-a-service panel both push network-adjacent utilities (traffic data, precision timing) toward productized, SLA'd offerings — a direction worth watching even if neither is core to this PM's portfolio today.
