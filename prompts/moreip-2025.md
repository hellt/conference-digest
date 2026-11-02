>>> HOW TO RUN THIS <<<
This is the digest prompt for moreip-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/moreip-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/moreip-2025.md
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

Below is the program for MORE-IP 2025 (operator). Read it and produce a digest
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
conference: MORE-IP 2025
type: operator
source_url: https://more-ip-event.net/more-ip-2025/agenda/
generated: 2026-11-01
registry_key: moreip-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Day one — Wednesday, June 4
### Welcome to MORE-IP
Speakers: Tim Vriend - AMS-IX
video: https://www.youtube.com/watch?v=x10KL2qBLCE
Introduction

### Opening Speech
Speakers: Peter van Burgel - AMS-IX
video: https://www.youtube.com/watch?v=Tm8bAU_AfFc
No description published; title and speakers only.

### Panel: Securing the Vital Digital Infrastructures
Speakers: Lieuwe-Jan Koning - On2it, Peter van Burgel - AMS-IX, Alex de Joode - AMS-IX
video: https://www.youtube.com/watch?v=YpHoGptvGi4
No description published; title and speakers only.

### Defending Europe against DDoS in a multi-polar world
Speakers: Octavia de Weerdt - NBIP Foundation
video: https://www.youtube.com/watch?v=f3VsWS03-lc
No description published; title and speakers only.

### Digital sovereignty in search of modern-day knights
Speakers: Evelyn Austin - Bits of Freedom
video: https://www.youtube.com/watch?v=Yx3hlUPC2gU
No description published; title and speakers only.

### Racing against exponential change – Navigating the next digital wave
Speakers: Ruben Horbach
video: https://www.youtube.com/watch?v=pP5lmA3knds
No description published; title and speakers only.

### AMS-IX Innovation update
Speakers: Jan van Boeschoten - AMS-IX, Tim Vriend - AMS-IX
video: https://www.youtube.com/watch?v=ypM5k3qKPyU
No description published; title and speakers only.

### Next-Gen Sustainability: Shaping the Digital Ecosystem Together
Speakers: Demos Kyriacou - Wingu Africa Group, Theo Voss - Inter.link, Anton Mors - Nikhef
video: https://www.youtube.com/watch?v=bHSkrdOHqNM
No description published; title and speakers only.

### Partnering for Impact
Speakers: Hanna Kreitem - Internet Society
video: https://www.youtube.com/watch?v=xuI_v4aZJvM
No description published; title and speakers only.

### Panel: Cross-IX: Easy Peering across IXPs
Speakers: Mauro Roberto Magrassi - MIX, Simon Muyal - France-IX, Karin Ahl - Netnod, Mike Baron - AMS-IX
video: https://www.youtube.com/watch?v=u3AzdAdQKhE
No description published; title and speakers only.

### AMS-IX General Meeting 63
For AMS-IX Members only

## Day two — Thursday, June 5
### Juniper Migration Journey
Speakers: Leroy de Vos - AMS-IX
video: https://www.youtube.com/watch?v=swv2lqzaQKw
Technical Track

### Giving our Birds a New Pair of Wings
Speakers: Stavros Konstantaras - AMS-IX
video: https://www.youtube.com/watch?v=swv2lqzaQKw
Technical Track

### Farewell, Legacy
Speakers: Ivan Kovacevic  - Codetribe
video: https://www.youtube.com/watch?v=cvWaFnE2NJc
Technical Track - Boosting Security, Scalability, and Performance

### The Floor
Speakers: Bas Hickendorff - AMS-IX
video: https://www.youtube.com/watch?v=ykximzsyxEc
Technical Track - Access the right data, under your terms, at the best price

### From zero to SSL Automation
Speakers: Daniel Osielczak - AMS-IX
video: https://www.youtube.com/watch?v=aGz2qWU3wrg
Technical Track - How we secure both internal and external environments.

### Traffic Statistics
Speakers: Steven Bakker - AMS-IX
video: https://www.youtube.com/watch?v=K-WeHK3IFWI
Technical Track - Counting for Beginners

### Panel: The Power of Precision: Why Time as a Service Matters
Speakers: Jos van Eycken - Adtran, Michael van Schaik - VSL, Jan van Boeschoten - AMS-IX, Erwin uit de Bos - Digital Realty, Miguel Regalado Querol - AMS-IX
video: https://www.youtube.com/watch?v=G9-59S_wlmo
No description published; title and speakers only.

### IPv6-only IXPs Are Coming?
Speakers: Aleksi Suhonen - TREX Tampere Region  Exchange Oy
video: https://www.youtube.com/watch?v=mYbkT1vVC6k
No description published; title and speakers only.

### SNEAK PREVIEW – The ERIK Protocol for use with the RPKI
Speakers: Job Snijders - PeeringDB
video: https://www.youtube.com/watch?v=65wifHK4nWc
No description published; title and speakers only.

### It’s a wrap
No description published; title and speakers only.

### Closing Drinks
No description published; title and speakers only.

