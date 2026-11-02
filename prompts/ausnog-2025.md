>>> HOW TO RUN THIS <<<
This is the digest prompt for ausnog-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ausnog-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ausnog-2025.md
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

Below is the program for AusNOG 2025 (operator). Read it and produce a digest
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
conference: AusNOG 2025
type: operator
source_url: https://www.ausnog.net/events/ausnog-2025/program
generated: 2026-11-02
registry_key: ausnog-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Conference Day 1 - Wednesday 3rd September
### Welcome to AusNOG 2025
Speakers: David Hughes - AusNOG
No abstract published; title, speakers and materials only.

### Rethinking Network Troubleshooting: Smarter Tools and Better Visibility at Nexthop
Speakers: David Brown - Nexthop
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-01-DavidBrown.pdf | video: https://www.youtube.com/watch?v=f0u0XZHcrDs
No abstract published; title, speakers and materials only.

### Network State Checking: A Case Study in Automation
Speakers: Craig Henderson - REANNZ
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-02-CraigHenderson.pdf | video: https://www.youtube.com/watch?v=FL28XtauK7o
No abstract published; title, speakers and materials only.

### No Packet Left Behind: AWS's approach to building and operating reliable networks
Speakers: Lincoln Dale - Amazon
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-03-LincolnDale.pdf | video: https://www.youtube.com/watch?v=GeE-4V7iXek
No abstract published; title, speakers and materials only.

### Building AI Clusters: What Network Engineers need to know
Speakers: Brian Walsh - Nokia
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-04-BrianWalsh.pdf | video: https://www.youtube.com/watch?v=ReuAmLGa5O8
No abstract published; title, speakers and materials only.

### How geopolitics is rerouting submarine cables
Speakers: Jocelinn Kang - Nodalys
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-05-JocelinnKang.pdf | video: https://www.youtube.com/watch?v=1S9CBUmAkXs
No abstract published; title, speakers and materials only.

### Keynote Presentation : Beyond the Firewall: The Human, AI, and Network Revolution
Speakers: Amanda Spencer - Director Solutions Engineering, Cloudflare
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-06-AmandaSpencer.pdf | video: https://www.youtube.com/watch?v=WmEXhxtKaYk
No abstract published; title, speakers and materials only.

### The Scourge of Excessive AS-SETs
Speakers: Doug Madory - Kentik
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-07-DougMadory.pdf | video: https://www.youtube.com/watch?v=2FVJlXDPV_w
No abstract published; title, speakers and materials only.

### How far can you get with IX Route Servers?
Speakers: Ben Cartwright-Cox - bgp.tools
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-08-BenCartwrightCox.pdf | video: https://www.youtube.com/watch?v=6yapG6nV7O0
No abstract published; title, speakers and materials only.

### BFD going down... from BGP timers expiring?
Speakers: Louis Jarasius - 5GN
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-09-LouisJarasius.pdf | video: https://www.youtube.com/watch?v=Ldsz3tRvEX8
No abstract published; title, speakers and materials only.

### A smaller NBN Aggregation Network
Speakers: Craig Askings - Telair
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-01-10-CraigAskings.pdf | video: https://www.youtube.com/watch?v=SPfKzz3Awek
No abstract published; title, speakers and materials only.

### Lightning Talks
Speakers: Various Speakers
No abstract published; title, speakers and materials only.

### AusNOG Social
Speakers: Conference foyer area, Pullman Conference & Event Centre
No abstract published; title, speakers and materials only.

## Conference Day 2 - Thursday 4th September
### Cryptography in the Quantum Era
Speakers: Paresh Khatri - Nokia
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-01-PareshKhatri.pdf | video: https://www.youtube.com/watch?v=hqlpCY1CUVk
No abstract published; title, speakers and materials only.

### Designing a mikrotik cgnat solution that scales
Speakers: Matthew Enger - Leaptel
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-02-MatthewEnger.pdf | video: https://www.youtube.com/watch?v=2rpbAIkkARg
No abstract published; title, speakers and materials only.

### Evolving Broadband Design in Australia
Speakers: Travis O'Hara - Juniper
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-03-TravisOHara.pdf | video: https://www.youtube.com/watch?v=H-Y0lt_DYYE
No abstract published; title, speakers and materials only.

### Transport Protocols Evolution or how to migrate your configuration today.
Speakers: Alex Mitev - Cisco
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-04-AlexMitev.pdf | video: https://www.youtube.com/watch?v=O664YnFGpbQ
No abstract published; title, speakers and materials only.

### Evolution of Transport Protocols
Speakers: Geoff Huston - APNIC
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-05-GeoffHuston.pdf | video: https://www.youtube.com/watch?v=nc6Qb-LvPos
No abstract published; title, speakers and materials only.

### AARNet - Australia's Academic and Research Network
Speakers: Peter Stamp - AARNet
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-07-PeterStamp.pdf | video: https://www.youtube.com/watch?v=oVw9q91Yv1w
No abstract published; title, speakers and materials only.

### Defending Telco Networks
Speakers: Anthony Schofield - Vocus
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-08-AnthonySchofield.pdf
No abstract published; title, speakers and materials only.

### The comfortable complexity of Overlays
Speakers: Claudiu Captari - Arista
slides: https://www.ausnog.net/sites/default/files/ausnog-2025/presentations/ausnog-2025-02-09-ClaudiuCaptari.pdf | video: https://www.youtube.com/watch?v=fbZDDJb0sdM
No abstract published; title, speakers and materials only.

### Conference Close
Speakers: David Hughes - AusNOG
No abstract published; title, speakers and materials only.

