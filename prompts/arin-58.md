>>> HOW TO RUN THIS <<<
This is the digest prompt for arin-58. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/arin-58.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/arin-58.md
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

Below is the program for ARIN 58 Public Policy and Members Meeting (operator). Read it and produce a digest
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
conference: ARIN 58 Public Policy and Members Meeting
type: operator
source_url: https://www.arin.net/participate/meetings/ARIN58
generated: 2026-11-01
registry_key: arin-58
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Public Policy & Members Meeting, Day 1 - Thursday, 22 October 2026
### Opening and Announcements
Speakers: Hollis Kara
video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=0s
No abstract; agenda item, speaker and materials only.

### Welcome from ARIN’s President and CEO
Speakers: John Curran
video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=737s
No abstract; agenda item, speaker and materials only.

### Welcome and Board of Trustees Report
Speakers: Nancy Carter
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_boardupdate.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=975s
No abstract; agenda item, speaker and materials only.

### NANOG Update
Speakers: Jonathan Black
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_nanog.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=1734s
No abstract; agenda item, speaker and materials only.

### Policy Implementation and Experience Report
Speakers: John Sweeting
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policyimplementation.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=2301s
No abstract; agenda item, speaker and materials only.

### Advisory Council Report and On-Docket
Speakers: Kathleen Hunter
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_acupdate.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=7194s
No abstract; agenda item, speaker and materials only.

### Policy Block 1: Recommended Draft Policy ARIN-2025-1
Speakers: Leif Sawyer
page: https://www.arin.net/participate/policy/drafts/2025_1/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_1.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=8418s
No abstract; agenda item, speaker and materials only.

### Policy Block 1: Recommended Draft Policy ARIN-2025-3
Speakers: Gerry George
page: https://www.arin.net/participate/policy/drafts/2025_3/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_3.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=9444s
No abstract; agenda item, speaker and materials only.

### Policy Block 1: Recommended Draft Policy ARIN-2025-7
Speakers: Lily Botsyoe
page: https://www.arin.net/participate/policy/drafts/2025_7/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_7.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=11228s
No abstract; agenda item, speaker and materials only.

### Policy Block 1: Recommended Draft Policy ARIN-2025-8
Speakers: Kaitlyn Pellak
page: https://www.arin.net/participate/policy/drafts/2025_8/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2025_8.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=16280s
No abstract; agenda item, speaker and materials only.

### Policy Block 2: Draft Policy ARIN 2026-1
Speakers: Alison Wood
page: https://www.arin.net/participate/policy/drafts/2026_1/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_1.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=17410s
No abstract; agenda item, speaker and materials only.

### Policy Block 2: Draft Policy ARIN 2026-2
Speakers: Matthew Wilder
page: https://www.arin.net/participate/policy/drafts/2026_2/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_2.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=19874s
No abstract; agenda item, speaker and materials only.

### Policy Block 2: Draft Policy ARIN 2026-3
Speakers: E. Marie Brierley
page: https://www.arin.net/participate/policy/drafts/2026_3/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_3.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=20847s
No abstract; agenda item, speaker and materials only.

### Policy Block 2: Draft Policy ARIN 2026-4
Speakers: Brian Jones
page: https://www.arin.net/participate/policy/drafts/2026_4/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_4.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=21334s
No abstract; agenda item, speaker and materials only.

### Policy Block 2: Draft Policy ARIN 2026-5
Speakers: Gus Reese
page: https://www.arin.net/participate/policy/drafts/2026_5/ | slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_policy_2026_5.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=23541s
No abstract; agenda item, speaker and materials only.

### 2026 ARIN Elections
Speakers: Ron da Silva
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_elections.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=24058s
No abstract; agenda item, speaker and materials only.

### Address Supporting Organization Address Council (ASO AC) Update
Speakers: Kevin Blumberg
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_asoacupdate.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=25095s
No abstract; agenda item, speaker and materials only.

### RIR Governance Document Update
Speakers: Michael Abejuela
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_rirgovernance.pdf | video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=26029s
No abstract; agenda item, speaker and materials only.

### Open Microphone
Speakers: Nancy Carter, John Curran
video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=26746s
No abstract; agenda item, speaker and materials only.

### Closing Announcements
Speakers: Hollis Kara
video: https://www.youtube.com/watch?v=b9CYdQfMNQ4&t=27435s
No abstract; agenda item, speaker and materials only.

## Public Policy & Members Meeting, Day 2 - Friday, 23 October 2026
### 2026 Customer Satisfaction Survey
Speakers: Adam Wedlake
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_customersurvey.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=1274s
No abstract; agenda item, speaker and materials only.

### Routing Security Update
Speakers: Brad Gorman
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_routingsecurity.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=3131s
No abstract; agenda item, speaker and materials only.

### ARIN Financial Report
Speakers: Hank Kilmer
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_financialreport.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=4461s
No abstract; agenda item, speaker and materials only.

### Data Accuracy Update
Speakers: John Sweeting
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_dataaccuracy.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=5325s
No abstract; agenda item, speaker and materials only.

### IPv6 Task Force
Speakers: Lee Howard
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_ipv6taskforce.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=7573s
No abstract; agenda item, speaker and materials only.

### ARIN Directory Services Roadmap
Speakers: Hollis Kara
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_directoryservices.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=8315s
No abstract; agenda item, speaker and materials only.

### Information Security Update
Speakers: Christian Johnson
slides: https://www.arin.net/participate/meetings/ARIN58/materials/ARIN58_infosec.pdf | video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=9338s
No abstract; agenda item, speaker and materials only.

### Closing Announcements and Adjournment
Speakers: Ashley Perks
video: https://www.youtube.com/watch?v=RhO-2Cqaejo&t=11511s
No abstract; agenda item, speaker and materials only.

