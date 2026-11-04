>>> HOW TO RUN THIS <<<
This is the digest prompt for zanog-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/zanog-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/zanog-2026.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

Below is the program for ZANOG@iWeek 2026 (operator). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is an operator program (network/infrastructure operators). Focus on
operational practice, failure stories, and techniques that transfer across
environments rather than org-specific anecdotes. Up-rank concrete postmortems,
tooling and automation that others can adopt, and hard-won lessons about
running networks at scale. Down-rank vendor-sponsored sessions that are pitches
in disguise. Note when a technique depends on a specific operator's scale or
topology.

## Enriching from the source material (best effort)

The program text gives you a title, authors, and an abstract per item, and
often links (`page:`, `pdf:`, `slides:`, `video:`). The abstract alone is thin — the full
paper has the methodology, real results, and limitations that make the What /
How / Where-applicable sections accurate instead of guessed.

If you have a tool to fetch URLs, then for EACH selected item (Core, Adjacent,
and Wildcard) try to retrieve the fuller source before writing it up:

- Prefer a `pdf:` link; else fetch the `page:` link (often has the full text or
  a longer description); a `video:` link is a last resort, don't transcribe it.
- Use what you retrieve to ground What/How/Where-applicable in the paper's
  actual contributions, evaluation, and stated constraints.

This is strictly best-effort. Many links fail or are paywalled:

- If a fetch fails, is paywalled, returns only an abstract, or you have no fetch
  tool, just fall back to the abstract already in the program text. That is
  fine and expected — do not stall or skip the item.
- NEVER invent paper contents, numbers, or findings from a failed or partial
  fetch. If you only had the abstract, write from the abstract.
- Note when an item's write-up is based only on the abstract, e.g. end its
  What line with "(from abstract only)", so the reader knows the depth.
- Do not let enrichment change which items you select or their tier; selection
  is from the program. Enrichment only deepens the write-up.

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to the PM's core interests as listed above
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title**: the `###` heading is the item's title exactly as the program
  gives it, with nothing added. Speaker(s)/author(s) with affiliation go on
  the line below it.
- No links section: the pipeline puts a links row (abstract page, paper,
  slides, recording) under every heading after you finish, from the program's
  `page:`/`pdf:`/`slides:`/`video:` lines and from verified sources. Do not
  write one, and do not link the title.
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

The digest is read on GitHub (GitHub-Flavored Markdown viewed in the repo) and
on the project's Zensical site, which renders the same file. Use only syntax
both render reliably, and follow these rules:

- Headings with `#`/`##`/`###`; bold with `**...**`; italics with `*...*`.
- Bullet lists with `-`. Put a blank line before every list, before every
  heading, and between paragraphs, or they won't render correctly.
- Indent nested lists by four spaces per level; avoid deeper nesting.
- Any link you do write is `[text](url)` — never a bare URL — and uses a URL
  exactly as the program text gives it.
- No raw HTML except the metadata comment below. Do not use heading IDs,
  footnotes, definition lists, or other non-GFM extensions.
- You may use tables and `code spans` where they genuinely help, since GitHub
  supports them; don't force them.

Begin the output with this metadata, wrapped in an HTML comment so it does not
show in the rendered view but stays in the source:

<!--
conference: ZANOG@iWeek 2026
type: operator
source_url: https://www.iweek.org.za/agenda
generated: 2026-11-04
registry_key: zanog-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Wednesday 22 April

### The State of Communications in South Africa
page: https://www.iweek.org.za/sessions/state-communications-south-africa
Speakers: Honourable Minister Solly Malatsi
When: 09:00, Plenary Room
Track: Industry Landscape
Universal and Meaningful Connectivity is a national priority for South Africa, as well as the theme of the conference. Honourable Minister Malatsi will be providing his view of the state of communications in South Africa, including a look at government broadband initiatives, progress of SA Connect, and projects and policy developments that are likely to have an impact on the internet sector.

### Transformation by Design
page: https://www.iweek.org.za/sessions/transformation-design
Speakers: Katharina Pillay - Seacom
When: 09:30, Plenary Room
Track: Industry Landscape
ICASA's requirements for licensee ownership, Equity Equivalent Investment Programmes (EEIPs) for international operators and the pending review of the ICT sector charter have all been in the news recently. This presentation unpacks these issues and looks at the way forward for companies to comply with these various requirements.

### Technology Disruption and Innovation
page: https://www.iweek.org.za/sessions/technology-disruption-and-innovation
Speakers: Andile Ngcaba - Chairman Convergence Partners and Solcon Capital
When: 10:15, Plenary Room
Track: Industry Landscape
Industry veteran Andile Ngcaba takes a look at technology disruption and innovation and maps out the pathway to pervasive IPv6 adoption in South Africa by 2030.

### ISP Business Models in a Price-Sensitive Market
page: https://www.iweek.org.za/sessions/isp-business-models-price-sensitive-market
Speakers: Jacques du Toit - Vox | CEO
When: 11:30, Plenary Room
Track: Business Sustainability
This presentation will explore how ISPs structure their business models in highly price sensitive markets balancing affordability with sustainability.

### Welcome and Overview / Overview of the Regulatory Framework for Domains in South Africa
page: https://www.iweek.org.za/sessions/welcome-and-overview-overview-regulatory-framework-domains-south-africa
Speakers: William Stucke, Neil Dundas - ZA Registry Consortium (ZARC) | CEO
When: 11:30, Breakaway Room
Track: Domain Name Workshop
William will open the workshop and address what the workshop hopes to achieve. The overview of the regulatory framework for domains in South Africa session will highlight the opportunities for interested parties to engage with and participate in policy development processes.

### Funding and Investment Opportunities for South African ISPs
page: https://www.iweek.org.za/sessions/funding-and-investment-opportunities-south-african-isps
Speakers: Robert Bergman
When: 12:00, Plenary Room
Track: Business Sustainability
This topic will highlight funding and investment opportunities available to ISPs and how ISPs can leverage investment to expand infrastructure, improve connectivity and support digital growth.

### Potential Impact of Draft ZADNA Licensing Regulations
page: https://www.iweek.org.za/sessions/potential-impact-draft-zadna-licensing-regulations
Speakers: Dominic Cull - Ellipsis | ISPA Regulatory Advisor
When: 12:00, Breakaway Room
Track: Domain Name Workshop
The overview of the regulatory framework for domains in South Africa session will highlight the opportunities for interested parties to engage with and participate in policy development processes.

### Submarine Overland Cable Technology
page: https://www.iweek.org.za/sessions/submarine-overland-cable-technology
Speakers: Nic Breytenbach, Afrim Beka - Nokia | Director of Subsea Networks Solutions
When: 12:30, Plenary Room
Track: Business Sustainability
Subsea cable technology is driving the expansion of data and telecommunications into remote and climate-challenged regions. As demand grows for connectivity - from basic services to AI/ML applications - new approaches are needed. With the ability to span thousands of kilometers without regeneration and long distances without amplification, these systems may offer powerful solutions for extending resilient, high-performance connectivity into terrestrial networks.

### IPv6 and DNSSEC for Managers
page: https://www.iweek.org.za/sessions/ipv6-and-dnssec-managers
Speakers: Mark Elkins
When: 12:30, Breakaway Room
Track: Domain Name Workshop
IPv6 and DNSSEC for Managers will focus on the business reasons for implementing IPv6 and DNSSEC, specifically why it is important for registrars to support both.

### DNS Resolution from Operators in South Africa
page: https://www.iweek.org.za/sessions/dns-resolution-operators-south-africa
Speakers: Yazid Akanho
When: 14:30, Plenary Room
Track: Thirty Years, A Few DNS Queries and Way Too Many Metrics

### New gTLD Applications
page: https://www.iweek.org.za/sessions/new-gtld-applications
Speakers: Lucky Masilela - ZA Registry Consortium | Co-CEO, Bob Ochieng
When: 14:30, Breakaway Room
Track: Domain Name Workshop
A look at the ICANN process for new gTLDs and what impact it might have on the South African domain name ecosystem.

### Dynamic Spectrum the Future
page: https://www.iweek.org.za/sessions/dynamic-spectrum-future
Speakers: Paul Colmer - WAPA | Executive Committee
When: 15:00, Plenary Room
Track: Thirty Years, A Few DNS Queries and Way Too Many Metrics
An update from the Wireless Access Providers' Association of South Africa (WAPA), covering the current state of the fixed wireless access market, regulatory developments affecting wireless ISPs, and the association's priorities for the year ahead. The session also addresses spectrum policy, infrastructure sharing, and the role of wireless access in extending broadband into underserved communities.

### Growth and Sustainability of the .ZA Namespace
page: https://www.iweek.org.za/sessions/growth-and-sustainability-za-namespace
Speakers: Khathutshelo Thovheyi
When: 15:00, Breakaway Room
Track: Domain Name Workshop
Growth and sustainability of the .ZA Domain namespace will focus on trend analysis.

### From Light to Leverage
page: https://www.iweek.org.za/sessions/light-leverage
Speakers: Byren Meinjes, Brett van Rooyen - NEC XON | Pre-Sales Consultant
When: 15:30, Plenary Room
Track: Thirty Years, A Few DNS Queries and Way Too Many Metrics
As South African enterprises push beyond traditional 1G and 10G connectivity toward native 100G and 400G services to support cloud adoption, AI platforms and data-intensive applications, service providers face growing pressure to scale routing capacity efficiently and extract greater value from fibre already in the ground. This presentation introduces the Managed Optical Fibre Network (MOFN) model — a WDM-based service framework that allows operators to productise optical networking, extend fibre asset life, and deliver high-capacity connectivity to enterprise customers who lack in-house optical transmission expertise. Through real-world use cases and deployment models, the talk explores how WDM evolves from a specialist network architecture into a commercially viable, scalable service — enabling both providers and enterprises to meet the next wave of connectivity demands without treating optical engineering as bespoke or inaccessible.

### The Future of the Domain Name Industry in South Africa [Panel]
page: https://www.iweek.org.za/sessions/future-domain-name-industry-south-africa-panel
Speakers: William Stucke, Neil Dundas - ZA Registry Consortium (ZARC) | CEO, Dominic Cull - Ellipsis | ISPA Regulatory Advisor, Mark Elkins, Lucky Masilela - ZA Registry Consortium | Co-CEO, Khathutshelo Thovheyi
When: 15:30, Breakaway Room
Track: Domain Name Workshop
The Pannel discussion will address the following question: Would direct second-level registrations make sense for .ZA? How does the use of social media affect the need for domain names? Interaction between ZADNA and the industry How do industry parties feel about processing PID?

## Thursday 23 April

### Threat Landscape in Southern Africa from a Shadowserver
page: https://www.iweek.org.za/sessions/threat-landscape-southern-africa-shadowserver
Speakers: Andy Chadwick - Shadowserver Foundation | Director for Africa
When: 09:30, Plenary Room
Track: Cybersecurity and Resilience
The Shadowserver Foundation: World Class Cyber Threat Intelligence at no cost. www.shadowserver.org I’ll give a presentation on what we do and why is can be extremely beneficial for network operators (and all network owners)

### A Guide to Open PON Environment
page: https://www.iweek.org.za/sessions/guide-open-pon-environment
Speakers: Radosław Ziemba, Piotr Golubski
When: 09:30, Breakaway Room
Track: ZANOG
Many ISPs operate in an environment where OLT manufacturers restrict the use of third-party ONTs, creating costly and inflexible vendor lock-in. This presentation explores how operators can break free from those constraints using multi-vendor HALNy Networks terminals powered by an innovative Adaptive OMCI Stack — a plug-and-play solution that allows ONTs to automatically discover and adapt to a wide range of OLTs (including Huawei, ZTE, and Nokia) without firmware changes. The talk covers the financial and operational benefits of transitioning to open, interoperable PON deployments, and demonstrates how cloud management integration via OpenOLT.com and Smart WiFi dashboards enable remote troubleshooting and network optimisation — reducing truck rolls and OPEX while future-proofing the network for emerging open standards.

### Cyber Security Challenges
page: https://www.iweek.org.za/sessions/cyber-security-challenges
Speakers: Heloise Meyer - SANReN (CSIR) | Senior SANReN Engineer | Cybersecurity Specialist
When: 10:00, Plenary Room
Track: Cybersecurity and Resilience
An overview of the SANReN Cyber Security Challenge and ISPA's contribution to the competition.

### gNMIc — On Your Marks, GET / SET / Subscribe / Collect
page: https://www.iweek.org.za/sessions/gnmic-your-marks-get-set-subscribe-collect
Speakers: Nardus le Roux - Nokia | IP Consulting Systems Engineer
When: 10:00, Breakaway Room
Track: ZANOG
Modern network operations demand a shift from periodic polling to real-time, streaming observability. This talk introduces gNMIc — a modern, highly scalable gRPC Network Management Interface collector with full gNMI protocol support for streaming telemetry. The session covers how gNMIc can be deployed to deliver continuous visibility into network state, enabling operators to move beyond traditional SNMP-based monitoring toward a more responsive, data-rich operational model.

### Tackling Cybersecurity on a Constrained Budget - Business Focus
page: https://www.iweek.org.za/sessions/tackling-cybersecurity-constrained-budget-business-focus
Speakers: Muhammad Amod - Senior Cybersecurity Engineer- Cybersec Cliniqu
When: 10:30, Plenary Room
Track: Cybersecurity and Resilience
Dealing with cybersecurity is a challenge for ISPs of all sizes, but can be particular difficult for SMMEs operating on a limited budget. This presentation will cover some options and ideas for tackling security issues with limited resources.

### ASPA
page: https://www.iweek.org.za/sessions/aspa
Speakers: Massimiliano Stucchi
When: 10:30, Breakaway Room
Track: ZANOG

### Securing Internet Routing - The Puzzle Pieces
page: https://www.iweek.org.za/sessions/securing-internet-routing-puzzle-pieces
Speakers: Tashi Phuntsho
When: 11:30, Plenary Room
Track: Trust Nobody, Log Everything, and Please Just Deploy IPv6
Route leaks and route hijacks continue to destabilise the global routing system, with significant consequences for network operators and their customers. This talk reviews the full toolkit of mechanisms available to secure Internet routing — including RPKI, Route Origin Authorisations (ROAs), BGPsec, IRR filtering and emerging proposals — examining how these puzzle pieces fit together, where each tool excels, and the practical and organisational challenges that still stand in the way of universal adoption.

### ISP Association Workshop
page: https://www.iweek.org.za/sessions/isp-association-workshop
When: 11:30, Breakaway Room
Track: ISP Association Workshop
This workshop is an opportunity for representatives for ISP associations in different countries to share their experiences and identify common threats and challenges. Proposed topics for discussion include: • Internet blocking - how to educate and inform policy makers • Strategies for dealing with dominant incumbent operators • AFRINIC - what role should ISP associations be playing • International satellite operators - threats or opportunities? • Cybersecurity challenges and consumer education

### Certificate Transparency: Running Static CT Logs
page: https://www.iweek.org.za/sessions/certificate-transparency-running-static-ct-logs
Speakers: Pim van Pelt
When: 12:00, Plenary Room
Track: Trust Nobody, Log Everything, and Please Just Deploy IPv6
Certificate Transparency (CT), defined in RFC 6962, provides a mechanism for publicly logging TLS certificates in a way that allows anyone to audit Certificate Authority activity and detect the issuance of suspect or unauthorised certificates. This talk shares the hands-on experience of IPng Networks in operating instances of Sunlight and TesseraCT — two open source implementations of the Static CT protocol — running four production CT logs: Rennet, Lipase, Gouda and Halloumi. The presentation covers the technical setup, operational lessons learned, and the role community-run CT logs play in the broader ecosystem of Internet security.

### IPv6 - Measuring Uptake
page: https://www.iweek.org.za/sessions/ipv6-measuring-uptake
Speakers: Jaco Kroon
When: 12:30, Plenary Room
Track: Trust Nobody, Log Everything, and Please Just Deploy IPv6
With IPv4 exhaustion long established, the global transition to IPv6 is well underway — but how do we actually measure progress, and where does South Africa stand? This presentation examines why continued migration to IPv6 remains critically important, the methodologies available for tracking adoption across networks and regions, and what the data reveals about the state of IPv6 uptake in South Africa and on the broader African continent.

### The Role of Civil Society in Connecting People Online (Zero-rating and Beyond)
page: https://www.iweek.org.za/sessions/role-civil-society-connecting-people-online-zero-rating-and-beyond
Speakers: Busisiwe Kabane-Bailey - DG Murray Trust | Innovation Director
When: 14:30, Plenary Room
Track: Skills and Collaboration
This speech reflects DGMT’s journey in advancing zero-rating as a tool to expand access to critical services, particularly for underserved communities. It highlights key learnings that access alone is insufficient without meaningful use and positions the current moment as a shift towards a more holistic approach to digital inclusion. Looking ahead, it introduces the Connectivity Coalition as a collaborative platform to drive systems-level change, emphasizing the importance of partnerships across civil society, government, and the private sector.

### Importance of AFRINIC as a Regional Institution
page: https://www.iweek.org.za/sessions/importance-afrinic-regional-institution
Speakers: Honourable Deputy Minister Mondli Gungubele
When: 15:00, Plenary Room
Track: Zero-rating/AFRINIC

### AFRINIC AMA
page: https://www.iweek.org.za/sessions/afrinic-ama
When: 15:30, Plenary Room
Track: AFRINIC

