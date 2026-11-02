>>> HOW TO RUN THIS <<<
This is the digest prompt for ausnog-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ausnog-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ausnog-2026.md
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

Below is the program for AusNOG 2026 (operator). Read it and produce a digest
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
conference: AusNOG 2026
type: operator
source_url: https://www.ausnog.net/events/ausnog-2026/program
generated: 2026-11-01
registry_key: ausnog-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Conference Day 1 - Thursday 3rd September
### Welcome to AusNOG 2026
Speakers: David Hughes - AusNOG
No abstract published; title, speakers and materials only.

### Rethinking Address Reality: IPv4 Utilisation and Proxy Network Exposure in Australia
Speakers: Aftab Siddiqui - APNIC Foundation
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/AftabSiddiqu-APNICFoundation.pdf | video: https://www.youtube.com/watch?v=72gu9nlu384
No abstract published; title, speakers and materials only.

### Mission Possible: Disabling IPv4 on Google Enterprise Network
Speakers: Jen Linkova - Google
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/JenLinkova-Google.pdf | video: https://www.youtube.com/watch?v=mcGKJbji-OU
No abstract published; title, speakers and materials only.

### Revocation
Speakers: Geoff Huston - APNIC
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/GeoffHuston-APNIC.pdf | video: https://www.youtube.com/watch?v=YsH63Pr1jrw
No abstract published; title, speakers and materials only.

### Architecture and Troubleshooting: A Guide to AWS Peering
Speakers: Chitiz Shrestha - Amazon Web Services (AWS)
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/ChitizShrestha-AWS.pdf | video: https://www.youtube.com/watch?v=uaLHBiIeL5A
No abstract published; title, speakers and materials only.

### Migrating a Large Telco Networks IGP from OSPF/OSPFv3 to ISIS
Speakers: Sam Faunt - Aussie Broadband
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/SamFaunt-ABB.pdf | video: https://www.youtube.com/watch?v=Rw0IUguOsAM
No abstract published; title, speakers and materials only.

### Keynote Presentation : Will Australia be all at sea on national sovereign AI connectivity by 2030?
Speakers: Bevan Slattery - SUBCO
video: https://www.youtube.com/watch?v=JfFB4jjAmAo
No abstract published; title, speakers and materials only.

### From Human‑Centric to AI‑Assisted Operations
Speakers: Tim Raphael - Nokia
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/TimRaphael-Nokia.pdf | video: https://www.youtube.com/watch?v=amDmtZ3EOQE
No abstract published; title, speakers and materials only.

### Assurance on a budget
Speakers: Tim Warnock - Superloop
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/TimWarnock-Superloop.pdf | video: https://www.youtube.com/watch?v=opHGF4ylx78
No abstract published; title, speakers and materials only.

### Return loss problems associated with faster optical networks
Speakers: Takaya Nakagawa - NTT Advanced Technology Corporation
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/TakayaNakagawa-NTT.pdf | video: https://www.youtube.com/watch?v=QZF0pWCU45I
No abstract published; title, speakers and materials only.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Speakers: Thomas Weible - Flexoptix
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/ThomasWeible-Flexoptix.pdf | video: https://www.youtube.com/watch?v=oB5cn_QkArk
No abstract published; title, speakers and materials only.

### Lightning Talks
Speakers: Various Speakers
No abstract published; title, speakers and materials only.

### AusNOG Social
Speakers: Held at the conference venue, join your industry peers for some networking over drinks and light cocktail food
No abstract published; title, speakers and materials only.

## Conference Day 2 - Friday 4th September
### Optimizing Traffic Flow with Akamai
Speakers: Kams Yeung - Akamai
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/KamsYeung-Akamai.pdf | video: https://www.youtube.com/watch?v=Gzf8wTkVZOI
No abstract published; title, speakers and materials only.

### Our journey on "how we are modernising our network"
Speakers: Richard Vander Reyden - Optus
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/RichardVanderReyden-Optus.pdf | video: https://www.youtube.com/watch?v=v7HLjDyG7E0
No abstract published; title, speakers and materials only.

### How nbn co manages large scale emergency events prior, during and post.
Speakers: Alan Pendrigh - nbn co
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/AlanPendrigh-nbn.pdf | video: https://www.youtube.com/watch?v=Q4TDx8_GOuE
No abstract published; title, speakers and materials only.

### Securing modern telco networks
Speakers: Patrick Ohearn - AARNet Pty Ltd
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/PatrickOhearn-AARNET.pdf | video: https://www.youtube.com/watch?v=YGl8yffnySs
No abstract published; title, speakers and materials only.

### Lessons from the State-Sponsored Siege on Core Telecom Infrastructure
Speakers: Taylor Reed - Palo Alto Unit 42
No abstract published; title, speakers and materials only.

### Rural Fibre Co
Speakers: Phil Britt - Rural Fibre Co
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/PhilBritt-RuralFibre.pdf | video: https://www.youtube.com/watch?v=5XsAALiTEr0
No abstract published; title, speakers and materials only.

### BGP EVPN. A view from the field
Speakers: Alex Mitev - Cisco System
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/AlexMitev-Cisco.pdf | video: https://www.youtube.com/watch?v=FjdYI9RIoGM
No abstract published; title, speakers and materials only.

### ...because copy+paste isn’t a network configuration strategy - automation for amateurs
Speakers: James Morgan - VERNet
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/JamesMorgan-Vernet.pdf | video: https://www.youtube.com/watch?v=PFcfyAzgeic
No abstract published; title, speakers and materials only.

### The CDN Landscape Revisited: Static, Live, and AI
Speakers: Steve Meuse - Kentik
slides: https://www.ausnog.net/sites/default/files/ausnog-2026/presentations/SteveMeuse-Kentik.pdf | video: https://www.youtube.com/watch?v=QHVNPcc_7fQ
No abstract published; title, speakers and materials only.

### Conference Close
Speakers: David Hughes - AusNOG
No abstract published; title, speakers and materials only.

