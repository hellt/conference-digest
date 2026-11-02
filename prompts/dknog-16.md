>>> HOW TO RUN THIS <<<
This is the digest prompt for dknog-16. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/dknog-16.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/dknog-16.md
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

Below is the program for DKNOG16 (Scandic Copenhagen) (operator). Read it and produce a digest
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
conference: DKNOG16 (Scandic Copenhagen)
type: operator
source_url: https://events.dknog.dk/event/35/
generated: 2026-11-02
registry_key: dknog-16
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## DKNOG Main Track
### Understanding and optimising transceiver efficiency using internal metrics for improved power savings
Speakers: Stein, Gerhard (Flexoptix GmbH)
page: https://events.dknog.dk/event/35/contributions/310/
In high-performance optical communication systems transceiver health and efficiency are critical to network reliability and energy consumption. This presentation explores the powerful capabilities of Versatile Diagnostics Monitoring (VDM) features found in modern optical transceivers (beyond the speed of 100G) with a particular focus on the Thermoelectric Cooler (TEC) current metrics. By analysing TEC current alongside temperature and cable length data we should be able to identify the optimal operating conditions that will minimise power consumption while maintaining performance. In order to prove this thesis we developed a couple of software prototypes to perform the data analysis. Using real-world VDM data this talk will demonstrate how to evaluate and visualise transceiver efficiency in terms of Watts, uncovering practical insights for engineers aiming to design or operate greener, more efficient optical networks and finally save energy.

### Network Automation in the Modern Age
Speakers: Stoegbauer, Marcus, Heller, Veit
page: https://events.dknog.dk/event/35/contributions/325/
Network Automation has been around long enough that it progressed through different stages. In the early days network engineers were happy that we could write templates, merge them with variables and push the result out to the devices. By now, we can see that we need a place where to store those variables in a sensible way, through documentation systems (or DCIMs). But with this we enter a new stage of automation, which brings increased complexity and additional knowledge requirements to the people designing the automation and documentation systems. We need to understand our data and our models better than ever before, and make our decisions based on how we model the world, without being constrained by the limits of our documentation systems. This is not a "here is the solution" talk. This is more the beginning of a longer conversation we want to start in the networking community, showing where we, the network people, need to figure out for ourselves what is still lacking in our automation skill and toolsets and how to progress from here. And maybe a glimpse on an early draft of a potential solution.

### Auto-bandwidth for SR-TE
Speakers: Shypovalov, Dmytro (Vegvisir Systems)
page: https://events.dknog.dk/event/35/contributions/315/
The presentation covers a prototype of my auto-bandwidth solution for Segment Routing Traffic Engineering. The solution is open standard and multi-vendor (existing bandwidth-aware SR-TE solutions are vendor specific). The prototype also includes an open source tool SR-TE bandwidth sampler, which collects SR policy counters via GNMI, calculates traffic rate and converts it into the BGP-LS format per RFC9857.

### IXP+ based observations on peering and routing changes after Middle East cable outages
Speakers: Kjellgren, Kaj (DE-CIX), Speiss, Bernd (DE-CIX)
page: https://events.dknog.dk/event/35/contributions/314/
This presentation is showing and discussing observations of what trends and changes can be seen after the cable cuts near the shore of Yemen in September. We try to highlight findings and interesting changes in routing or traffic shifts. The findings are valid globally and not just Middle East related. It serves as a great example of do's and don'ts in your routing-setup.

### How far can you get with IX Route Servers?
Speakers: Cartwright-Cox, Ben (bgp.tools)
page: https://events.dknog.dk/event/35/contributions/320/
Route servers are the most important service (other than moving packets itself) on an internet exchange fabric, however in most exchanges peering with them is not mandatory. This talk aims to answer the question of how effective route servers are and distributing routes to many networks, using the large internet exchange deployment footprint of the bgp.tools route collector network, we will look at how relevant internet exchange routes servers are, and how many people (and who) actually import from them.

### Automate what makes sense: Data, principles and practice
Speakers: Jeggesen, Brian
page: https://events.dknog.dk/event/35/contributions/332/
“Automate what makes sense” sounds practical. In many network orgs, it becomes a permanent excuse to not automate anything. This talk explains why automation stalls even when the tools are fine: unclear definitions of “safe” and “correct,” fragile inputs, and changes that can’t be proven before they ship. You’ll get a pragmatic way to turn automation from a special project into a normal way of working — with guardrails and evidence instead of optimism. You’ll leave with a clear first step you can implement immediately, plus a simple path to build confidence and scale without betting the network on heroics.

### Introduction to Design-Driven Network Automation
Speakers: Coleman, Mark
page: https://events.dknog.dk/event/35/contributions/326/
Design‑driven automation treats the high-level design of infrastructure as a first‑class artifact: an explicit model of topology, roles, relationships, and constraints that exists independently of any particular device configuration. In this talk, we will explore what design‑driven automation means in practice, why it emerged, and why it keeps resurfacing whenever networks reach a certain level of scale or complexity. We will look at how working from a design model changes everyday operational thinking — from how state is understood, to how drift is interpreted, to how refactoring and unplanned change are handled. We will trace how these ideas have evolved, from early topology‑aware network management and fabric controllers to modern intent‑based and fabric‑oriented systems. The focus will be on the underlying mechanics: how networks are modeled, how change is reasoned about over time, and where design‑driven approaches help — and where they still struggle in real operational environments.

### Merging Service Provider Networks
Speakers: Hoss, Bastian (Xantaro Deutschland GmbH), Jungbluth, Markus (Xantaro Deutschland GmbH)
page: https://events.dknog.dk/event/35/contributions/312/
As the service provider market slowly consolidates, network engineers and architects will increasingly face the complex challenge of merging service provider networks. This technical talk dives into the intricacies of integrating distinct IP/MPLS network infrastructures, focusing on practical considerations and potential pitfalls. Based on past experience, we will discuss the general approach to such a project, key architectural considerations, and challenges related to routing protocols and vendor interoperability.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Speakers: Weible, Thomas
page: https://events.dknog.dk/event/35/contributions/313/
In the old days of traditional separation of IP and DWDM, there was no need for IP folks to care about much other than what they used on their routers/switches (while the transport team ran the DWDM infra). These past DWDM infra approaches for maximizing the data capacity per fiber pair went for running more and more DWDM channels with grid spacings as small as possible. This meant that grid spacings shrank from 200GHz to 100GHz and then 50GHz with some applications even going for 25GHz. Now in the age of IPoDWDM the bandwidth per channel keeps increasing, as complex modulation schemes come into favor over ON-OFF-Keying which has been the de facto standard so far. Those increased per channel bandwidths of 400Gbps, 800Gbps and now pushing into the 1.6Tbps realm demand for larger grids to accommodate the spectrum necessary to operate such “Superchannels”. Especially the fact of coherent detection being “blind” to anything but its own wavelength has enabled interesting topologies that can omit filters altogether. Of course that comes at a cost of reduced flexibility. Which means, IP folks now will need to understand the nuances of how coherent detection works, need for larger filters for 800Gbps and higher, and how 400GHz filters (key word here being COTS) would future proof your network by not only allowing you to grow to 1.6Tbps, but also allow backwards compatibility for legacy services on 50GHz, etc. Made by FLEXOPTIX Research - Gert and Thomas.

### Command-Line to Codebase: Learning Software to Expand Your Engineering Toolkit
Speakers: Kjær, Thomas
page: https://events.dknog.dk/event/35/contributions/316/
This talk is a short, practical story about a network engineer who wanted repeatable ECMP troubleshooting and also wanted to learn a new programming language. Starting from familiar tools (traceroute, Wireshark, RFCs), I built a small ECMP‑aware probing tool and translated manual workflows into code. The focus is less on the tool itself and more on the method: start in a domain you trust, measure everything, and build in small slices. I’ll share the learning process I followed: start with familiar tools, test one change at a time, explain results to yourself as you go, and how I got unstuck when progress stalled. Attendees will leave with concrete, low‑risk ways to start small software projects in their own networking work: how to pick a problem, how to validate changes, and how to keep momentum even when day‑to‑day priorities shift.

### ASPA: the new protocol for improving BGP routing security
Speakers: Caletka, Ondřej (RIPE NCC)
page: https://events.dknog.dk/event/35/contributions/311/
In the past it was believed that network operators should periodically download clear text data from the Internet and put them into the configuration of their routers to make routing more secure. RPKI is a technology to secure routing which employs proper cryptography. For years we have used it for Route Origin Authorization. New feature of routing security is being deployed now: Autonomous System Provider Authorization. It complements existing Route Origin validation with a partial path validation: each autonomous system can declare which autonomous systems are expected to provide transit services. Network operators validating ASPA can then drop routes coming via unauthorized providers.

### Sovereignty for whom? Between digital (in)dependence and Big Tech expansionism
Speakers: Lai, Signe Sophus (University of Copenhagen), Flensburg, Sofie (University of Copenhagen)
page: https://events.dknog.dk/event/35/contributions/323/
Recent geopolitical tensions have placed digital sovereignty as a key buzzword in public and political debates, emphasising the dominance of US-based tech corporations across the digital market. In Denmark, the Minister of Digitalisation has taken several measures to ‘liberate’ the public sector from infrastructural dependencies and the economic consequences they entail. Meanwhile, corporations such as Microsoft, Amazon, and Google increasingly promote their services as tools for enhancing sovereignty (e.g., through offering national data storage, risk assessment tools, and so forth). Sovereignty is, in other words, a deeply political concept, characterised by distinct ambiguity and several (conflicting) interests. In this talk, we provide an overview of the variety of ways different stakeholders use the concept of sovereignty to steer the political debate and ultimately consolidate existing and emerging forms of power. On this basis, we argue that a persistent focus on applications and services rather than the underlying infrastructures is hindering more fundamental discussions of the power structures that shape digital ecosystems. As an alternative perspective, we provide a series of examples from our research on global submarine data cables, emphasising the altered ownership structures and conditions around global internet routing. Through this, we open up for discussions of how to better connect the dots between the ongoing sovereignty debate and the technological and economic realities faced by industry professionals.

### Lost in translation: philologist tries to decode the Tech-Sales Interface
Speakers: Vaske, Katja
page: https://events.dknog.dk/event/35/contributions/322/
What happens when a language teacher is dropped into the deep end of the telecom industry, with zero background in fiber, DWDM, or why “it depends” is the only honest answer to anything? This talk is a personal journey of switching careers from academia and language teaching into the world of tech sales in a fast-moving, acronym-rich, and precision-driven industry. The presentation will explore the early days of trying to sell services she barely understood, the awkward moments of miscommunication with engineers, and the hard-earned lessons of navigating between customer expectations and technical reality. It will touch on the cultural gap between sales and tech: how each side uses language differently, and how learning to "speak engineer" was just as hard as learning a foreign language. From amusing misunderstandings to practical strategies that helped bridge the gap, this talk is for anyone who's ever had to translate between departments, roles, or mindsets. Key Points / Takeaways: * Switching from humanities to telecom: a career change story * First encounters with technical product language (and confusion) * What “cannot be done” really means (and what it doesn’t) * Why sales and tech often miscommunicate, and how to fix it * Lessons in building trust with engineers * Learning to translate between customer needs and engineering limitations * Humility, curiosity, and the importance of asking “dumb” questions * How being a language teacher actually helps in tech, unexpectedly

### Who put the "inter" in internet?
Speakers: Kamp, Poul-Henning
page: https://events.dknog.dk/event/35/contributions/328/
More to come

## Program
### DKNOG announcements
Speakers: Jarlskov, Lasse (DKNOG)
page: https://events.dknog.dk/event/35/contributions/330/
No description published; title and speakers only.

### Geopolitics and Digital Sovereignty in Greenland
Speakers: Ravn-Højgaard, Signe (Tænketanken Digital Infrastruktur)
page: https://events.dknog.dk/event/35/contributions/319/
Greenland’s digital ecosystem is characterised by structural dependence on U.S.-controlled infrastructure across multiple layers: limited international backbone connectivity via a small 2 submarine cables and limited satellite links, routing and traffic flows largely terminating outside Greenland. This talk examines how constrained path diversity, external routing and hosting, minimal local traffic localisation and vulnerable infrastructure intersect with heightened geopolitical attention. The slides for this presentaion can be accessed here: https://www.canva.com/design/DAHCs0CGAas/7evoVC1E0QgefQbs5CIdvw/view

## Short talks
### The DKNOG Quiz!
Speakers: Stucchi, Massimiliano (Glevia GmbH)
page: https://events.dknog.dk/event/35/contributions/321/
This is the "classic" DKNOG Quiz. You will be tested on your knowledge of Routing, RPKI, Unix history, and most important on the content of the talks of the whole two days. So, pay attention to all the talks, take note of all the details of slidesets, and prepare your fingers to answer as quick as possible. Prizes will be given to the three highest scorers!

### Old habits die hard, how to kill them easily
Speakers: Willems Kristiansen, Martin (Norlys Mobil A/S)
page: https://events.dknog.dk/event/35/contributions/317/
We have an issue in the network industry - we're stuck in the ways we think and the ways we work. Why change something just to change it? Well, why not? This lightning talk aims to challenge our industry's resistance to change and provides food for thought on breaking free from outdated practices.

### A different way to success
Speakers: Pedersen, Henrik Haue (Norlys Digital A/S), Rønne Madsen, Peter (Norlys Digital A/S)
page: https://events.dknog.dk/event/35/contributions/318/
This talk is about how, I, as a person with disabilities managed to get a job in Norlys, one of Denmark biggest telecom companies. It is my story from education up until now and how I, as an untraditional workforce, manages to get telecom issues solved. Additionally, I have invited my manager to give his point of view from first meeting at DKNOG 15 through the hiring process and how it is to have a worker like me employed.

