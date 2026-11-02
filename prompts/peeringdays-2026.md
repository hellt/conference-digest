>>> HOW TO RUN THIS <<<
This is the digest prompt for peeringdays-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/peeringdays-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/peeringdays-2026.md
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

Below is the program for Peering Days 2026 (operator). Read it and produce a digest
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
conference: Peering Days 2026
type: operator
source_url: https://2026.peeringdays.eu/programme/
generated: 2026-11-01
registry_key: peeringdays-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Monday 23 rd March 2026
### Technical Workshop: A focus on ROAs and ASPAs, and how to handle them with Krill
Speakers: Massimiliano Stucchi
This workshop will present a quick refresher on RPKI, discussing the role of ROAs, and then will talk about the most recent addition, ASPAs. We will discuss how to create ASPAs and what their role is in global routing. The main part of the session will be about how to setup Krill to manage delegated RPKI, covering the setup of the software, and how to prepare for different types of publication setups. This workshop is meant for network engineers and network managers who would like to understand more about ASPA, and would also like to understand how delegated RPKI works.

## Tuesday 24 th March 2026
### 30 Years of Interconnection: Experience from an Italian IXP
Speakers: NAMEX - Maurizio Goretti
slides: https://2026.peeringdays.eu/media/documents/NAMEX_Maurizio_Goretti.pdf
No abstract published; title, speakers and materials only.

### Agentic DDoS OPS/AI-Powered Operations Layer for GenieATM
Speakers: Genie Networks - Siarhei Matashuk
slides: https://2026.peeringdays.eu/media/documents/Genie_Networks_Siarhei_Matashuk.pdf
No abstract published; title, speakers and materials only.

### Demystifying Coherent Optics for Network Professionals
Speakers: Salumanus - Marcin Bala
slides: https://2026.peeringdays.eu/media/documents/Salumanus_Marcin_Bala.pdf
No abstract published; title, speakers and materials only.

### "Meet" update
Speakers: NIX.CZ - Marian Rychtecky
slides: https://2026.peeringdays.eu/media/documents/NIX_Marian_Rychtecky.pdf
No abstract published; title, speakers and materials only.

### Get the benefits of a non-profit local/sub-regional IX
Speakers: BIX - Janos Gergely & BIX - Janos Angeli
slides: https://2026.peeringdays.eu/media/documents/BIX_Janos_Gergely_Janos_Angeli.pdf
No abstract published; title, speakers and materials only.

### VIX Update 2026
Speakers: VIX - Monika Schneider
slides: https://2026.peeringdays.eu/media/documents/VIX_Monika_Schneider.pdf
No abstract published; title, speakers and materials only.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings
Speakers: Flexoptix - Gerhard Stein
slides: https://2026.peeringdays.eu/media/documents/Flexoptix_Gerhard_Stein.pdf
No abstract published; title, speakers and materials only.

### Peering market at a glance
Speakers: NAMEX - Flavio Luciani
slides: https://2026.peeringdays.eu/media/documents/NAMEX_Flavio_Luciani.pdf
No abstract published; title, speakers and materials only.

### How an IX does on Roller Coasters
Speakers: MIX-IT - Simone Morandini
No abstract published; title, speakers and materials only.

### Bilateral Meetings
No abstract published; title, speakers and materials only.

### Transfer by bus from the conference venue to the Social Evening - Museo Ferruccio Lamborghini
No abstract published; title, speakers and materials only.

### Social Evening - Museo Ferruccio Lamborghini
Address: S.P. Galliera n. 319 – 40050 Funo di Argelato, Bologna

## Wednesday 25 th March 2026
### Peering DB update
Speakers: PeeringDB - Arnold Nipper
slides: https://2026.peeringdays.eu/media/documents/PeeringDB_Arnold_Nipper.pdf
No abstract published; title, speakers and materials only.

### The Scourge of Excessive AS-SETs
Speakers: Kentik - Jac Kloots
slides: https://2026.peeringdays.eu/media/documents/Jac_Kloots_Kentik.pdf
No abstract published; title, speakers and materials only.

### Hardwired for Chaos: The No-Bullsh*t Way to Build Infrastructure That Lasts
Speakers: RETN - Tony O'Sullivan
No abstract published; title, speakers and materials only.

### Securing IXP Fabric
Speakers: NOKIA - Alessandro Bulletti
slides: https://2026.peeringdays.eu/media/documents/Nokia_Alessandro_Bulletti.pdf
No abstract published; title, speakers and materials only.

### EVPN - One control plane to rule them all
Speakers: Arista Networks - Patrick Prangl
slides: https://2026.peeringdays.eu/media/documents/Arista_Patrick_Prangl.pdf
No abstract published; title, speakers and materials only.

### Were you paying attention as there will be a quiz at the end…
Speakers: Massimiliano Stucchi
To finish off the Plenary we will be running a Kahoot quiz with questions drawn from the talks so far. And of course quizzes mean prizes!

