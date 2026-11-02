>>> HOW TO RUN THIS <<<
This is the digest prompt for arin-57. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/arin-57.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/arin-57.md
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

Below is the program for ARIN 57 Public Policy and Members Meeting (operator). Read it and produce a digest
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
conference: ARIN 57 Public Policy and Members Meeting
type: operator
source_url: https://www.arin.net/participate/meetings/ARIN57
generated: 2026-11-01
registry_key: arin-57
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Public Policy & Members Meeting, Day 1 - Monday, 20 April 2026, 9:00 AM ET
### Opening and Announcements
Speakers: Hollis Kara
video: https://www.youtube.com/live/-Fwz65uQp3E?t=22m02s
No abstract; agenda item, speaker and materials only.

### Welcome from ARIN’s President and CEO and Board Chair
Speakers: John Curran and Nancy Carter
video: https://www.youtube.com/live/-Fwz65uQp3E?t=33m58s
No abstract; agenda item, speaker and materials only.

### Board of Trustees Report
Speakers: Nancy Carter
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_boardreport.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=39m59s
No abstract; agenda item, speaker and materials only.

### Financial Report
Speakers: Hank Kilmer
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_financialreport.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=49m38s
No abstract; agenda item, speaker and materials only.

### KEYNOTE: Demystifying RPKI: Exploring Tools to Simplify ROA Planning and Visualize Validation
Speakers: Steve Wallace
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_internet2_keynote.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=1h12m38s
No abstract; agenda item, speaker and materials only.

### Regional Policy Update
Speakers: Eddie Diego
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_regionalpolicy.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=1h42m31s
No abstract; agenda item, speaker and materials only.

### Policy Implementation and Experience Report
Speakers: John Sweeting
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policyimplementation.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=2h22m06s
No abstract; agenda item, speaker and materials only.

### Advisory Council Update and On-Docket
Speakers: Kathleen Hunter
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_acdocket.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=2h50m36s
No abstract; agenda item, speaker and materials only.

### Advisory Council Working Group Updates
Speakers: Douglas Camin, Alison Wood, Matthew Wilder
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_acworkinggroup.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=3h12m35s
No abstract; agenda item, speaker and materials only.

### KEYNOTE: The Nine Lives of an Early Adopter: Leading Cats to Water in the IPv6 Era
Speakers: Nick Burlagio, Inder Monga
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_IPv6keynote.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=4h51m36s
No abstract; agenda item, speaker and materials only.

### Number Resource Organization Report
Speakers: John Curran
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_nroupdate.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=5h40m57s
No abstract; agenda item, speaker and materials only.

### Number Resource Organization Number Council and RIR Governance Document Status Update
Speakers: Amy Potter
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_rirgovernance.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=5h51m00s
No abstract; agenda item, speaker and materials only.

### ARIN Annual Report
Speakers: Richard Jimmerson
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_annualreport.pdf | video: https://www.youtube.com/live/-Fwz65uQp3E?t=6h59m59s
No abstract; agenda item, speaker and materials only.

### Open Microphone
Speakers: John Curran, Nancy Carter
video: https://www.youtube.com/live/-Fwz65uQp3E?t=7h18m07s
No abstract; agenda item, speaker and materials only.

### Closing Announcements and Adjournment
Speakers: Hollis Kara
video: https://www.youtube.com/live/-Fwz65uQp3E?t=7h25m04s
No abstract; agenda item, speaker and materials only.

## Public Policy & Members Meeting, Day 2 - Tuesday, 21 April 2026, 9:00 AM ET
### Engineering Update
Speakers: Mark Kosters
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_engreport.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=375s
No abstract; agenda item, speaker and materials only.

### Information Security Update
Speakers: Christian Johnson
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_infosec.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=1558s
No abstract; agenda item, speaker and materials only.

### Routing Security Update
Speakers: Brad Gorman
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_routingsecurity.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=3844s
No abstract; agenda item, speaker and materials only.

### Grant Reports
Speakers: Harlen Stenn, James Harr, Matt Griswold
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_communitygrantreports.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=7308s
No abstract; agenda item, speaker and materials only.

### Internet Governance 2025-2026
Speakers: Nate Davis
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_internetgovernance.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=9443s
No abstract; agenda item, speaker and materials only.

### Caribbean Collaboration 2025-2026
Speakers: Bevil Wooding
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_caribbean.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=10485s
No abstract; agenda item, speaker and materials only.

### Policy Block: Draft Policy ARIN-2025-1: Clarify ISP and LIR Definitions and References to Address Ambiguity in NRPM Text
Speakers: Leif Sawyer
page: https://www.arin.net/participate/policy/drafts/2025_1/ | slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20251.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=16354s
No abstract; agenda item, speaker and materials only.

### Policy Block: Draft Policy ARIN-2025-3: Change Section 9 Out Of Region Use Minimum Criteria
Speakers: Gerry George
page: https://www.arin.net/participate/policy/drafts/2025_3/ | slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20253.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=16999s
No abstract; agenda item, speaker and materials only.

### Policy Block: Draft Policy ARIN-2025-6: Fix Formula in 6.5.2.1c
Speakers: William Herrin
page: https://www.arin.net/participate/policy/drafts/2025_6/ | slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20256.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=18449s
No abstract; agenda item, speaker and materials only.

### Policy Block: Draft Policy ARIN-2025-7: Make Policy in 6.5.8.2 Match the Examples
Speakers: Lily Botsyoe
page: https://www.arin.net/participate/policy/drafts/2025_7/ | slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20257.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=20896s
No abstract; agenda item, speaker and materials only.

### Policy Block: Draft Policy ARIN-2025-8: Reserve 4.10 Space for In-Region Use
Speakers: E. Marie Brierley
page: https://www.arin.net/participate/policy/drafts/2025_8/ | slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20258.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=23529s
No abstract; agenda item, speaker and materials only.

### Policy Block: Draft Policy ARIN-2026-1: Taking IP To Other Planets (TIPTOP)
Speakers: Alison Wood
page: https://www.arin.net/participate/policy/drafts/2026_1/ | slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_policy_20261.pdf | video: https://www.youtube.com/live/HGTbhKYk_0g?t=24051s
No abstract; agenda item, speaker and materials only.

## Public Policy & Members Meeting, Day 3 - Wednesday, 22 April 2026, 9:00 AM ET
### Department Reports: Human Resources and Administration
Speakers: Erin Alligood
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_hrupdate.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=34m24s
No abstract; agenda item, speaker and materials only.

### Department Reports: Communications Department
Speakers: Ashley Perks
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_commsreport.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=46m47s
No abstract; agenda item, speaker and materials only.

### Department Reports: Registration Services Department
Speakers: John Sweeting
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_registrationservices.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=59m06s
No abstract; agenda item, speaker and materials only.

### Department Reports: Customer Experience and Strategy Department
Speakers: Joe Westover
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_cxsupdate.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=1h19m36s
No abstract; agenda item, speaker and materials only.

### Outreach and Fellowship
Speakers: Amanda Gauldin
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_fellowship.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=1h36m48s
No abstract; agenda item, speaker and materials only.

### Registry Integrity and Oversight
Speakers: Reese Radcliffe
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_registryintegrity.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=2h10m10s
No abstract; agenda item, speaker and materials only.

### ARIN General Counsel Update
Speakers: Michael Abejuela
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_legalupdate.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=2h33m20s
No abstract; agenda item, speaker and materials only.

### 2026 ARIN Election Preview
Speakers: Joe Westover
slides: https://www.arin.net/participate/meetings/ARIN57/materials/ARIN57_electionpreview.pdf | video: https://www.youtube.com/live/3jGjPBGK03c?t=2h42m20s
No abstract; agenda item, speaker and materials only.

