>>> HOW TO RUN THIS <<<
This is the digest prompt for nlnog-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/nlnog-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/nlnog-2025.md
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

Below is the program for NLNOG Day 2025 (Amsterdam) (operator). Read it and produce a digest
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
conference: NLNOG Day 2025 (Amsterdam)
type: operator
source_url: https://nlnog.net/events/nlnog-day-2025/
generated: 2026-11-02
registry_key: nlnog-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

### From ISC DHCP to KEA DHCP
Speakers: Rinse Kloek (Kloek Internetdiensten)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/2_-_Rinse_Kloek_-_ISC_to_KEA_DHCPv0.4.pdf | video: https://youtu.be/AieM0YUFHIM?si=sWoi4SyNtxS_wrop
No abstract published; title, speakers and materials only.

### SNTPings: Abusing IPv6 for Art
Speakers: Luc Haaijer (Studenten Net Twente)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/3_-_Luc_Haaijer_-_SNTPings.pdf | video: https://youtu.be/bGg6g9W2CTE?si=2DX7x7EKeR8zDa4T
No abstract published; title, speakers and materials only.

### Why would anyone want to run a personal ASN?!
Speakers: Nick Bouwhuis, Peter-Paul Kurstjens, Jelle Luteijn
slides: https://nlnog.net/events/nlnog-day-2025/presentations/4_-_Nick_Bouwhuis_-_Personal_ASN.pdf | video: https://youtu.be/4DFNQ5vacF8?si=GBdFV42HOQe_VW4k
No abstract published; title, speakers and materials only.

### WHY 400G FTTH
Speakers: Nicola von Thadden (PFALZKOM), Arjan Koopen (i3D.net)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/5_-_Arjan_Koopen_-_WHY_400G_FTTH.pdf | video: https://youtu.be/6OWZtS_BPv0?si=SKhQ2qgk5pjwclet
No abstract published; title, speakers and materials only.

### The Living Source of Truth: Network Automation with Infrahub and Terraform
Speakers: Marco Martinez
slides: https://nlnog.net/events/nlnog-day-2025/presentations/6_-_Marco_Martinez_-_The_Living_Source_of_Truth.pdf | video: https://youtu.be/8bVhExTWtYY?si=6cW9sfR28fY4zmNg
No abstract published; title, speakers and materials only.

### The How and Why of Internet.nl
Speakers: Sasha Romijn (Reliably Coded)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/7_-_Sasha_Romijn_-_Internet.nl_-_nlnog-inl.pdf | video: https://youtu.be/ZEtglnvTSyc?si=mcrT_y92-qUEPDjH
No abstract published; title, speakers and materials only.

### Collecting and analyzing routing information with Rotonda
Speakers: Luuk Hendriks (NLnet Labs)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/8_-_Luuk_Hendriks_-_Rotonda_-_nlnog2025.pdf | video: https://youtu.be/B9cEQD5Mad0?si=wm0MvkYB7pR_1KiD
No abstract published; title, speakers and materials only.

### How to get the most out of your support contracts (because you paid for it…)
Speakers: Peter Foppen (Comstor)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/9_-_Peter_Foppen_-_How_to_get_the_most_out_of_your_support_contracts.pdf | video: https://youtu.be/sW-pjFmRH2U?si=UAcLKcqMMZUltOR1
No abstract published; title, speakers and materials only.

### Expanding Internet Routing Visibility with BMP
Speakers: Thomas Holterbach (University of Strasbourg)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/10_-_Thomas_Holterbach_-_Expanding_Routing_Internet_Visibility_with_BMP.pdf | video: https://youtu.be/_gRVy0tTxOY?si=tepRYdbsz4HzrBXL
No abstract published; title, speakers and materials only.

### Hardwired for Chaos: The No-Bullsh*t Way to Build Infrastructure That Lasts
Speakers: Tony O’Sullivan (RETN)
slides: https://nlnog.net/events/nlnog-day-2025/presentations/11_-_RETN_NLNOG_Presentation_2025_NOBSTONY.pdf | video: https://youtu.be/IcnkElly1AY?si=eF6WvOdd-Oe3Y_4T
No abstract published; title, speakers and materials only.

