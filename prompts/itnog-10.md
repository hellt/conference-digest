>>> HOW TO RUN THIS <<<
This is the digest prompt for itnog-10. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/itnog-10.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/itnog-10.md
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

Below is the program for ITNOG10 (operator). Read it and produce a digest
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
conference: ITNOG10
type: operator
source_url: https://www.itnog.it/itnog10
generated: 2026-11-02
registry_key: itnog-10
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## ITNOG program
### HaliveOS: da operatore a innovatore
Speakers: WIC powered by Hal
No abstract published; title, speakers and materials only.

### OTN oltre il trasporto: reti programmabili, latenze garantite e architetture quantum-safe
Speakers: OPNET
No abstract published; title, speakers and materials only.

### Migrazione del nostro Backbone a SR-MPLS perdendo pochi ping...
Speakers: Denis Corradini
slides: https://www.itnog.it/files/1-2_Il nostro Backbone - ITNOG10.pdf
No abstract published; title, speakers and materials only.

### National Layer-2 wholesale FWA leveraging VxLAN
Speakers: Christian Biasibetti
slides: https://www.itnog.it/files/1-3_202604-cbiasibetti-L2FWA-ITNOG10-Public.pdf
No abstract published; title, speakers and materials only.

### Integration of Security Functions in EVPN/VXLAN Using Group-Based Policy
Speakers: Nicola Modena
slides: https://www.itnog.it/files/1-4_202604-nmodena-EVPN-VXLAN-Group-Based-Policy-ITNOG10.pdf
No abstract published; title, speakers and materials only.

### Coffee break
No abstract published; title, speakers and materials only.

### Transforming BGP operations to serve the best prefix out of 26 million
Speakers: Alessandro D'Eliseo Antonio Prado
slides: https://www.itnog.it/files/1-5_Transforming BGP Operations.pdf
No abstract published; title, speakers and materials only.

### Diffusione Edge Computing nelle reti Telco: local break traffico
Speakers: Fabio Randone
slides: https://www.itnog.it/files/1-6_Edge Computing in Telco Networks Fabio Randone_final.pdf
No abstract published; title, speakers and materials only.

### Reimagining Networking in the Age of AI: Empowering Engineers to Shape the Future
Speakers: Giampaolo Panariello
slides: https://www.itnog.it/files/1-7_Reimagining Networking in the Age of AI Empowering Engineers to Shape the Future v5 - Giampaolo Panariello.pdf
No abstract published; title, speakers and materials only.

### MIX DC3
Speakers: Mauro Magrassi
slides: https://www.itnog.it/files/1-8_MIX-ITNOG10-DC3.pdf
No abstract published; title, speakers and materials only.

### Inside Seabone: experiences of a Tier-1 Backbone
Speakers: Gabriele Laghi Patrizia Rossi Antonio Ferretti
slides: https://www.itnog.it/files/1-9_ITNOG_ Inside Seabone - Experiences of a Tier-1 Backbone.pdf
No abstract published; title, speakers and materials only.

### IXP Updates
Speakers: Various
slides: https://www.itnog.it/files/1-9_ixp_updates.pdf
No abstract published; title, speakers and materials only.

### Hollow Core Fibre - Nothing is better than glass for guiding light
Speakers: Steve Jones
slides: https://www.itnog.it/files/1-11_ITNOG_hollowcorefiber.pdf
No abstract published; title, speakers and materials only.

### Building the longest SR-TE lsp in the world
Speakers: Umberto M
slides: https://www.itnog.it/files/1-12_longesttunnel-itnog_26_um_2.pdf
No abstract published; title, speakers and materials only.

### SRv6 uSID: Deterministic AI Backend Networking and Unified DC Frontend Design
Speakers: Alberto Donzelli
slides: https://www.itnog.it/files/1-13_2026_ITNOG_adonzell_Cisco-final.pdf
No abstract published; title, speakers and materials only.

### News and How to be involved in PeeringDB
Speakers: Livio Morina
slides: https://www.itnog.it/files/1-14_20260421_ITNOG10_Morina_Livio.pdf
No abstract published; title, speakers and materials only.

### Improve IPv6 Peering
Speakers: Federico Paesani
slides: https://www.itnog.it/files/1-15_Presentazione improveipv6peeringITNOG10 Paesani v2.0.pdf
No abstract published; title, speakers and materials only.

### Coffee Break
No abstract published; title, speakers and materials only.

### HERABIT - Interprovider VPN
Speakers: Fabio Moglia
slides: https://www.itnog.it/files/1-16_HERABIT_InterproviderVPN_INOG10.pptx.pdf
No abstract published; title, speakers and materials only.

### BGP nell'underlay multi-cloud: resilienza e simmetria tra on-prem e public cloud
Speakers: Carlo Pio Luigi Ciciriello
slides: https://www.itnog.it/files/1-17_ITNOG10-BGPunderlayMultiCloud-CPLC-20260421.pdf
No abstract published; title, speakers and materials only.

### Open Lab: A collaborative multi-vendor platform for experimentation and validation of next-generation networking
                                        technologies
Speakers: Flavio Luciani
slides: https://www.itnog.it/files/1-18_A collaborative multi-vendor platform for experimentation and validation of next-generation networking technologies.pdf
No abstract published; title, speakers and materials only.

### ITNOG Updates
Speakers: Marco Marzetti
No abstract published; title, speakers and materials only.

### The Network Automation Map: Navigate Your Journey with the NAF Automation Framework
Speakers: Christian Adell
slides: https://www.itnog.it/files/2-11_ITNOG - The Network Automation Map.pdf
No abstract published; title, speakers and materials only.

### Antares: Multi-Agent AI for Automated Network Analysis and Troubleshooting in GARR Data Centers
Speakers: Francesco Lombardo
slides: https://www.itnog.it/files/2-12_Antares-ITNOG10.pdf
No abstract published; title, speakers and materials only.

### AS/IXP Traffic Observability / Osservabilità del traffico AS/IXP
Speakers: Luca Deri Federico Santulli
slides: https://www.itnog.it/files/2-13_trafficobservabilityITNOG_0426_FINALE.pdf
No abstract published; title, speakers and materials only.

### Semplificare l'automazione multi-vendor: Client RESTCONF auto-generati dai moduli YANG
Speakers: Matteo Colantonio
slides: https://www.itnog.it/files/2-14_Matteo Colantonio semplificare automazione multivendor ITNOG10.pdf
No abstract published; title, speakers and materials only.

### Measuring the public Internet
Speakers: João Damas
slides: https://www.itnog.it/files/2-15_APNIC ITNOG 10.pdf
No abstract published; title, speakers and materials only.

### Deep Dive nei KPI della Telefonia - Modelli Matematici e Architetture Dati per la Fraud Detection e la Revenue
                                        Assurance
Speakers: Emanuela Bevilacqua
slides: https://www.itnog.it/files/2-16_kpi_ITNOG_EmanuelaBevilacqua_final.pdf
No abstract published; title, speakers and materials only.

### Open Networking and IPoDWDM in Production: Operational Lessons from European Networks
Speakers: Alessandro Giudice
slides: https://www.itnog.it/files/2-17_IPoDWDM 400G ZR+ ITNOG10 v1.pdf
No abstract published; title, speakers and materials only.

### Splitting ottico passivo per ridondanza link
Speakers: Mirko Mosca
slides: https://www.itnog.it/files/2-18_itnog10.2026-mosca-splitting-ottico.pdf
No abstract published; title, speakers and materials only.

