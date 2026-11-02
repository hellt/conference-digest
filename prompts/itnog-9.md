>>> HOW TO RUN THIS <<<
This is the digest prompt for itnog-9. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/itnog-9.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/itnog-9.md
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

Below is the program for ITNOG9 (operator). Read it and produce a digest
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
conference: ITNOG9
type: operator
source_url: https://www.itnog.it/itnog9
generated: 2026-11-01
registry_key: itnog-9
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## ITNOG program
### sFlow on Smartwall one
Speakers: Corero
No abstract published; title, speakers and materials only.

### Secure your IXPs data and network: protect with Next-Gen DDoS Protection Advanced Strategies and Secure Transport  solution.
Speakers: Nokia
No abstract published; title, speakers and materials only.

### Unlock your network (Fiber broadband)
Speakers: Harmonic
No abstract published; title, speakers and materials only.

### How optics can improve the quality of your WISP business
Speakers: Flexoptix
No abstract published; title, speakers and materials only.

### ITNOG updates and local NOGs
Speakers: Various
slides: https://www.itnog.it/files/1-Associazione ITNOG - Financial Updates 2025-localnogs.pdf
No abstract published; title, speakers and materials only.

### Power Consumption Considerations in Optical Metro Transport Networks
Speakers: Steve Jones
slides: https://www.itnog.it/files/2-Power_SJ_ITNOG.pptx.pdf
No abstract published; title, speakers and materials only.

### Analyzing network reliability up to 800G - Impact of SNR thresholds on BER for Coherent (16QAM) and Non-Coherent (PAM4) high speed transceivers under environmental variations
Speakers: Thomas Weible
slides: https://www.itnog.it/files/3-Flexoptix - Network Reliability Analysis Coherent Non-Coherent.pdf
No abstract published; title, speakers and materials only.

### From Clicks to Code: Optical Network Automation Journey in GARR
Speakers: Matteo Colantonio
slides: https://www.itnog.it/files/4-ITNOG9_Dai Click al Codice_Matteo_Colantonio.pdf
No abstract published; title, speakers and materials only.

### ISDN - Protocol Wars
Speakers: Leonardo Rizzi
slides: https://www.itnog.it/files/5-isdn_pub.pdf
No abstract published; title, speakers and materials only.

### Quality of Experience in an application first world: giving networks the tools to maintain value in an increasingly OTT controlled environment
Speakers: Roberta Maglione
No abstract published; title, speakers and materials only.

### EVPN/VxLAN outside the data center
Speakers: Nicola Modena
slides: https://www.itnog.it/files/7-202505-nmodena-evpnvxlan-wan-ITNOG9.pdf
No abstract published; title, speakers and materials only.

### KINDNS
Speakers: Ulrich Wisser
slides: https://www.itnog.it/files/8-ITNOG-KINDNS-20250520.pdf
No abstract published; title, speakers and materials only.

### PeeringDB updates
Speakers: Livio Morina
slides: https://www.itnog.it/files/9-20250520_ITNOG9_Morina_Livio_r2.pptx.pdf
No abstract published; title, speakers and materials only.

### Costruire un ambiente di test sicuro per un IXP
Speakers: Marta Burocchi
slides: https://www.itnog.it/files/10-Building_a_secure_Test_Environment_for_an_IXP_ITNOG_final_version (1).pptx.pdf
No abstract published; title, speakers and materials only.

### Automating a Service Provider Network: A Practical Introduction
Speakers: Elia Aielli
slides: https://www.itnog.it/files/11-[ITNOG9]Aielli.pdf
No abstract published; title, speakers and materials only.

### PACMAN: Automazione della configurazione di rete in GARR, tra sfide tecnologiche e cambiamento culturale
Speakers: Francesco Lombardo
slides: https://www.itnog.it/files/12-itnog9_pacman_v2.pdf
No abstract published; title, speakers and materials only.

### Routing Security
Speakers: Marco Paesani
slides: https://www.itnog.it/files/13-20250520_Presentazione_ITNOG9_PAESANI.pdf
No abstract published; title, speakers and materials only.

### Whats new in Ripe
Speakers: Riccardo Stagni
slides: https://www.itnog.it/files/14-ITNOG9 - RIPE NCC Updates.pdf
No abstract published; title, speakers and materials only.

### Networking for AI and Ultra Ethernet
Speakers: Massimo Magnani
slides: https://www.itnog.it/files/15-Networking for AI and HPC, and Ultra Ethernet - ITNOG9.pptx.pdf
No abstract published; title, speakers and materials only.

### IXP updates
Speakers: Various
slides: https://www.itnog.it/files/16-itnog9-ixp-updates.pdf.pdf
No abstract published; title, speakers and materials only.

