>>> HOW TO RUN THIS <<<
This is the digest prompt for netnod-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/netnod-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/netnod-2025.md
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

Below is the program for Netnod Tech Meeting 2025 (operator). Read it and produce a digest
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
conference: Netnod Tech Meeting 2025
type: operator
source_url: https://www.netnod.se/netnod-tech-meeting-2025
generated: 2026-11-01
registry_key: netnod-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Netnod Tech Meeting — 9th October
### Netnod update
Speakers: Danny Berg - Netnod
slides: https://www.netnod.se/sites/default/files/2025-10/2.Netnod%20tech%20meeting2025.pdf | video: https://youtu.be/4LAg_go_-iw
No abstract published; title, speakers and materials only.

### The global impact of individual actions and our collective work
Speakers: Kurt Erik “Kurtis” Lindqvist - ICANN
video: https://youtu.be/Kv9sBLIJ-Zc
No abstract published; title, speakers and materials only.

### Recursive DNS in Telia Company Sweden
Speakers: Björn Hellqvist - Telia
video: https://youtu.be/zdM0jF1WGSE
No abstract published; title, speakers and materials only.

### DNS Week update
Speakers: Phil Regnauld - DNS-OARC
video: https://youtu.be/8Acl0j5w4-4
No abstract published; title, speakers and materials only.

### SRv6 uSID: fundamental transformation of the IP stack
Speakers: Ahmed Abdesalam - Cisco
slides: https://www.netnod.se/sites/default/files/2025-10/20251009-Netnod-SRv6-uSID-rev2.pdf | video: https://youtu.be/-Q9JYxKOp4U
No abstract published; title, speakers and materials only.

### Mastering Network Operations: The Power of Abstraction in Automation
Speakers: Jaakko Rautanen - Rautanen
slides: https://www.netnod.se/sites/default/files/2025-10/9.netnod2025%20-%20The%20Power%20of%20Abstraction.pdf | video: https://youtu.be/yK7xxkBPnew
No abstract published; title, speakers and materials only.

### Your AS-set is crucial to your routing security. 3 tips on securing your AS-set
Speakers: Lasse Jarlskov - Telia
slides: https://www.netnod.se/sites/default/files/2025-10/10.Securing%20your%20AS-Set-Netnod.pptx_.pdf
No abstract published; title, speakers and materials only.

### Optics was instrumental in building the Internet—and will be crucial in an AI-driven world
Speakers: Magnus Grenfeldt - Smartoptics
video: https://youtu.be/WhkyBnPKbDM
No abstract published; title, speakers and materials only.

### Meta – Big Trends and how it will change the Network
Speakers: Janne Elvelid - META, Fredrik “Hugge” Korsbäck - META
No abstract published; title, speakers and materials only.

### Encrypted Network Traffic Analysis and Protection
Speakers: David Hasselquist - Sectra
No abstract published; title, speakers and materials only.

### Ultra Ethernet
Speakers: Johan Ervenius - Arista Networks
slides: https://www.netnod.se/sites/default/files/2025-10/15.Ultra%20Ethernet%20-%20Arista.pptx_.pdf | video: https://youtu.be/fRizzhFzcEU
No abstract published; title, speakers and materials only.

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations
Speakers: Dr.-Ing. Gerhard Stein - FLEXOPTIX
slides: https://www.netnod.se/sites/default/files/2025-10/Flexoptix%20-%20Network%20Reliability%20Analysis%20Coherent%20Non-Coherent-Netnod%20%282%29.pdf | video: https://youtu.be/4_1pM6o-pD4
No abstract published; title, speakers and materials only.

### Building Modern and Scalable DC Fabrics
Speakers: Alperen Akpinar - NOKIA
slides: https://www.netnod.se/sites/default/files/2025-10/17.Building%20Modern%20and%20Scalable%20DC%20Fabrics%20-%20Alperen%20Akpinar%20061025.pptx_.pdf | video: https://youtu.be/JwlfAEgXw7o
No abstract published; title, speakers and materials only.

### The Illusion of Control: Trusting Software in the Age of Compromise
Speakers: Moin Rahman
slides: https://www.netnod.se/sites/default/files/2025-10/18.The%20Illusion%20of%20Control.pdf | video: https://youtu.be/mWIxKHxxTG0
No abstract published; title, speakers and materials only.

### One more Thing & Closing
Speakers: Joel Söderman - Netnod
video: https://youtu.be/KCdd3CznWxI
No abstract published; title, speakers and materials only.

### Social
No abstract published; title, speakers and materials only.

