>>> HOW TO RUN THIS <<<
This is the digest prompt for nlnog-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/nlnog-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/nlnog-2026.md
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

Below is the program for NLNOG Day 2026 (Hilversum) (operator). Read it and produce a digest
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
conference: NLNOG Day 2026 (Hilversum)
type: operator
source_url: https://nlnog.net/events/past-events/nlnog-day-2026/
generated: 2026-11-02
registry_key: nlnog-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

### The Hitchhiker’s Guide to IPv6: Don’t Panic… We’ve Only Got 30 Minutes
Speakers: Nicole Wajer (Cisco)
slides: https://nlnog.net/events/nlnog-day-2026/presentations/2a_-_Nicole_Wajer_-_The_Hitchhiker_s_Guide_to_IPv6__Don_t_Panic_We_ve_Only_Got_30_Minutes.pdf | video: https://youtu.be/3BcJobyHcag?si=6JYrb_80YVKXBMAI
No abstract published; title, speakers and materials only.

### The Art of Making Vendors Agree: Lessons from Interoperability Testing
Speakers: Patrick Prangl (Arista)
slides: https://nlnog.net/events/nlnog-day-2026/presentations/3a_-_Patrick_Prangl_-_The_Art_of_Making_Vendors_Agree.pdf | video: https://youtu.be/M4_AoyEnGZs?si=GWDlR-iMpbh_PMRi
No abstract published; title, speakers and materials only.

### VPP eVPN Controlplane
Speakers: Pim van Pelt (IPng)
slides: https://nlnog.net/events/nlnog-day-2026/presentations/4a_-_IPng_Networks_-_eVPN_NLNOG26.pdf | video: https://youtu.be/oZUfbciI2Ww?si=0XGdNizxOAA00t7x
No abstract published; title, speakers and materials only.

### Networking without the Internet
Speakers: Marlies Heijkoop
slides: https://nlnog.net/events/nlnog-day-2026/presentations/5a_-_Marlies_Heijkoop_-_Networking_without_the_Internet.pdf
No abstract published; title, speakers and materials only.

### NLNAM: A Home for Network Automation in the Netherlands
Speakers: Bart Dorlandt (Dream Networking and Automation)
slides: https://nlnog.net/events/nlnog-day-2026/presentations/6a_-_Bart_Dorlandt_-_NLNAM_a_home_for_network_automation.pdf
No abstract published; title, speakers and materials only.

### Kubernetes for Network Engineers
Speakers: Egbert Verhage (NIT Solutions)
slides: https://nlnog.net/events/nlnog-day-2026/presentations/7a_-_Egbert_Verhage_-_Kubernetes_for_Network_Engineers.pdf | video: https://youtu.be/TkUj9hZs3ys?si=Fyz5EF9WpxXPrTkF
No abstract published; title, speakers and materials only.

### How to change the Internet itself?
Speakers: Job Snijders
slides: https://nlnog.net/events/nlnog-day-2026/presentations/8a_-_Job_Snijders_-_How_to_change_the_internet_itself.pdf | video: https://youtu.be/qHV_IZJxIKE?si=PzT659fNaWGa4dBU
No abstract published; title, speakers and materials only.

### Lessons from 10 months of ASPA
Speakers: Tim Bruijnzeels (RIPE NCC)
slides: https://nlnog.net/events/nlnog-day-2026/presentations/9a_-_Tim_Bruijnzeels_-_Lessons_from_10_months_of_ASPA.pdf | video: https://youtu.be/xII4eXXALWY?si=9qU76kmrB23ytzpT
No abstract published; title, speakers and materials only.

### Internet exchanges in space
Speakers: Iljitsch van Beijnum
slides: https://nlnog.net/events/nlnog-day-2026/presentations/10a_Iljitsch_van_Beijnum_-_IXes_in_space_v05.pdf | video: https://youtu.be/PW6IcB7dOW4?si=MtDAUivdef9ZzQPm
No abstract published; title, speakers and materials only.

