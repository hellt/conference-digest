>>> HOW TO RUN THIS <<<
This is the digest prompt for grnog-20. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/grnog-20.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/grnog-20.md
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

Below is the program for GRNOG 20 (operator). Read it and produce a digest
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
conference: GRNOG 20
type: operator
source_url: https://grnog.indico.nogalliance.org/event/13/
generated: 2026-11-01
registry_key: grnog-20
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Program
### WebPKI, automation and the push for more agility
Speakers: Zacharopoulos, Dimitris
page: https://grnog.indico.nogalliance.org/event/13/contributions/178/
No description published; title and speakers only.

### EVPN – One Control Plane to Rule Them All
Speakers: Prangl, Patrick (Arista Networks)
page: https://grnog.indico.nogalliance.org/event/13/contributions/186/
No description published; title and speakers only.

### ASPA and Roles: What's up with that?
Speakers: Chariton, Antonis (AS4601 | Cisco)
page: https://grnog.indico.nogalliance.org/event/13/contributions/177/
No description published; title and speakers only.

### DNS best practices
Speakers: Wisser, Ulrich (ICANN)
page: https://grnog.indico.nogalliance.org/event/13/contributions/182/
No description published; title and speakers only.

### A comprehensive analysis of the IRR landscape
Speakers: Konstantaras, Stavros (AMS-IX)
page: https://grnog.indico.nogalliance.org/event/13/contributions/181/
No description published; title and speakers only.

### The Future of Network Visibility: LLM and Intelligent Monitoring
Speakers: Deri, Luca (ntop)
page: https://grnog.indico.nogalliance.org/event/13/contributions/184/
No description published; title and speakers only.

### MPTE update
Speakers: Kompella, Kireeti (HPE Networking)
page: https://grnog.indico.nogalliance.org/event/13/contributions/179/
No description published; title and speakers only.

### Peering market at a glance
Speakers: Luciani, Flavio, Souter, John
page: https://grnog.indico.nogalliance.org/event/13/contributions/180/
No description published; title and speakers only.

### DNS4EU Public DNS Resolver Infrastructure
Speakers: Palias, Panagiotis (Whalebone)
page: https://grnog.indico.nogalliance.org/event/13/contributions/185/
No description published; title and speakers only.

### Agentic AI in Networking
Speakers: Kaminaras, Ioannis, Gerakaris, Kostas (Uni Systems)
page: https://grnog.indico.nogalliance.org/event/13/contributions/187/
No description published; title and speakers only.

### Balkan Digital Gateway: Enhancing Greece’s Regional Connectivity
Speakers: Kudriashova, Polina, Velichkov, Valentin
page: https://grnog.indico.nogalliance.org/event/13/contributions/188/
No description published; title and speakers only.

### Infrahub: Next-gen data management platform for Design-Driven Automation
Speakers: Crocker, Pete (OpsMill)
page: https://grnog.indico.nogalliance.org/event/13/contributions/183/
No description published; title and speakers only.

