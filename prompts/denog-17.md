>>> HOW TO RUN THIS <<<
This is the digest prompt for denog-17. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/denog-17.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/denog-17.md
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

Below is the program for DENOG 17 (Essen) (operator). Read it and produce a digest
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
conference: DENOG 17 (Essen)
type: operator
source_url: https://www.denog.de/de/meetings/denog17/agenda.html
generated: 2026-11-02
registry_key: denog-17
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## 2025-11-09 — Leadership Track (Room 413)

### Leadership in dynamic systems? The Esquai Leadership Framework provides orientation
Speakers: Philip Scherenberg
page: https://pretalx.com/denog17/talk/AATHPE/ | slides: https://pretalx.com/media/denog17/submissions/AATHPE/resources/251108_DENOG_Leade_KH4XbrN.pdf
In our rapidly evolving world of networks and technologies, dynamic systems are the
norm. Whether it's the integration of service provider networks, the transition from
services to product-oriented startups, or digital transformation... Managers are faced
with constant challenges. But how do you successfully navigate these complex and
ever-changing environments?

Dr. Philip Scherenberg, economist and philosopher as well as managing director of
Esquai Leadership Advisors GmbH, brings an application-oriented perspective to this
crucial question. As an expert in executive coaching, leadership advisory and
stakeholder management, he supports companies, board members and executives in
special situations, especially in situations of strong growth, changes in ownership or
management as well as in crisis and transformation processes.

In his presentation, Philip introduces the Esquai Leadership Framework . This
conceptual foundation provides precise guidance in abstract leadership situations by
illustrating the interactions between culture, strategy, and organization. With this
framework, his clients create clarity, increase the performance of their organization
and enable teams and individuals to operate successfully in dynamic environments.
Be inspired by how good leadership creates concrete value and helps to master the
complexity of real leadership issues that ultimately lead to sustainable change.

### 01: Know where to go! Supernavigation in coaching and beyond
Speakers: Philip Scherenberg
page: https://pretalx.com/denog17/talk/T83AUV/ | slides: https://pretalx.com/media/denog17/submissions/T83AUV/resources/251108_DENOG_WS01__a2FEZ2A.pdf
A simple yet universally applicable process of navigating difficult
challenges will be presented. In this deep dive all participants will share
and crack up one particular topic.

### 02: Measure what matters. Using data for personal development in a rolling 360 feedback system
Speakers: Philip Scherenberg
page: https://pretalx.com/denog17/talk/PACL8M/ | slides: https://pretalx.com/media/denog17/submissions/PACL8M/resources/251108_DENOG_WS02__gDk5mjL.pdf
The do’s and dont’s of implementing 360 feedback to your organization.
Including a real life case study with ANEXIA that will make the decision easier for you if this „sharpest of swords“ is suitable for you.

### 03: Measure what matters. Using data for team building by applying regular TKI surveys (30
Speakers: Philip Scherenberg
page: https://pretalx.com/denog17/talk/WKSVTZ/ | slides: https://pretalx.com/media/denog17/submissions/WKSVTZ/resources/251108_DENOG_WS03__8sLMunY.pdf
How do you find out what your team needs to flourish? You ask them!
This TKI tool is all about that. From science and leadership literature, we know the characteristics of high-performing teams well. This tool is made to measure exactly that. We’ll introduce you to some of the most relevant team performance characteristics and how we measure them.
Simple and clean.

### 04: Measure what matters. Using data for leading your organisation by checking the pulse
Speakers: Philip Scherenberg
page: https://pretalx.com/denog17/talk/SDEJ7G/ | slides: https://pretalx.com/media/denog17/submissions/SDEJ7G/resources/251108_DENOG_WS04__pCrlHkm.pdf
Do your people know the strategy? Is everybody aligned in terms of what’s important in your culture? Where are the structural bottlenecks in your organisation? These questions are all linked through the Esquai Leadership Framework. We’ll peek behind the curtain of how we get to the relevant data, what the struggle is in collecting good data, and ultimately how great leaders react to whatever is thrown at them.

### 05: What can go wrong? And right? Aligning personal motives with your team- and corporate culture
Speakers: Philip Scherenberg
page: https://pretalx.com/denog17/talk/JUNFEA/ | slides: https://pretalx.com/media/denog17/submissions/JUNFEA/resources/251108_DENOG_WS05__3HBuWaS.pdf
In coaching, we use the term „values“ to describe what’s valuable to us in our lives. Having one’s own values misaligned with your team’s and
your company’s values is a prime source for frustration, tiredness, and ultimately burnout. In this sharing session, each participant reflects upon
their own set of values and brings this together with the outside expectations of heads, colleagues, clients, or investors... whoever the main stakeholders are.

## 2025-11-09 — Workshop 505

### BGP Workshop 4.0
Speakers: Vincentz Petzholtz, Peter Sievers, Sebastian Graf
page: https://pretalx.com/denog17/talk/MKNDET/
Want to perform the bgp handshake in real life based on a realistic topology? We got you covered ... in this workshop for intermediates we will dive into some network basics of bgp driven networks and also explore route filtering best practices (mainly for the DfZ = default free zone).

After some theory every attendee will receive one network node to configure. The fellow participants will be your peers. You will depend on the peers to reach your goals.

Teams work together in small groups. One group either jointly manages an AS consisting of 3 routers and a customer downlink router or the IXP infrastructure based on EVPN with additional route server. Troubleshooting takes place across groups in order to verify the corresponding availability within the lab topology.

Warning: You will have to socialise with the peers around you!

Topics Covered:
- Introduction into Internet/Routing Hierarchy
- Routing/Announcement Basics/Strategy
- Route Filtering
- Lab Introduction

Technologies Covered:
- TO BE DEFINED

Pre-requisites:
- Network Fundamentals, user level UNIX and maybe some system administration,
- Some use of network design preferably TCP/IP-based is also helpful.
- Dynamic routing Fundamentals (BGP, ISIS/OSPF is a plus)
- Participants must have technical hands on experience of routers.

Some experience with EOS or a comparable CLI will be helpful.

## 2025-11-09 — Workshop 506

### Containerlab: A guide to building your own virtual datacenter and monitoring it
Speakers: Mathis Bramkamp, Gordon Gidófalvy
page: https://pretalx.com/denog17/talk/FTHSAH/ | slides: https://pretalx.com/media/denog17/submissions/FTHSAH/resources/Containerlab_Preso_oInT61T.pdf
This beginner-level workshop aims to teach participants how to use containerlab as a network labbing and testing tool, and showcases both simple and complex network infrastructures that can be modelled with it. During the workshop, participants will build a simple virtual EVPN-VXLAN datacenter network and set up network telemetry collection using open-source tools. As a closing task, we will show of how a Kubernetes-based network orchestration and telemetry collection system works with the same topology that the participants have put together.

This hand-on workshop will cover:

**1. Creating containerlab topologies, from CLI to GUI**
You'll learn how to install and use containerlab, and how a containerlab topology file looks like. We present how containerlab works, the commands containerlab uses, the topology syntax, and also showcase some recent additions and changes made to containerlab in 2025. At the end of this section, you will have a ready-to use containerlab topology serving as a baseline for the next sections. 

   For veteran containerlab users, we provide a prepared topology that allows you to skip to the next section.
 
**2. Sending and observing traffic in your virtual datacenter**
In order to collect meaningful telemetry data, we should have some client traffic going across our topology. Hence, clients are added to the topology and test traffic is sent between the nodes. As part of this section, we also configure Edgeshark to allow us to perform remote packet captures from the containerlab host, and learn how to use the VS Code extension to capture live traffic and simulate link impairments.
 
**3. Setting up a modern open-source telemetry stack**
Having a virtual network is one thing, but most networks come with supporting infrastructure. We can leverage the Linux container ecosystem to easily add components of a network telemetry stack to our containerlab topology, which allows us to collect, store and visualize telemetry data from the network elements. We use gNMIc, Prometheus and Grafana to create a streaming telemetry dashboard that allows to monitor our datacenter.
 
**4. Giving a Kubernetes-based network automation and telemetry solution a spin**
Kubernetes is the de-facto industry standard container orchestration system, used worldwide from small scale to hyperscale environments. This robust system is not only useful for container orchestration, but for network management and orchestration as well, as we demonstrate this during this section.

   You will use a Kubernetes-based network orchestrator to manage the configuration of the virtual datacenter and to collect telemetry from it. This section requires no prior Kubernetes experience, the whole interaction can be done through a UI or API.

## 2025-11-09 — Workshop 421

### The easy way to IPv6 - IPv6 migration for enterprises
Speakers: Wilhelm  Boeddinghaus
page: https://pretalx.com/denog17/talk/TLF9GT/
A workshop for enterprise administrators who want to implement IPv6 in their companies. You will get a good idea where to start your journey to IPv6, who to take with you and which path to take. The workshop will be interactive and you should bring a laptop or tablet for getting the most out of this learning experience. After two hours you are ready to start your IPv6 project.

### SSH essentials
Speakers: Felix Schüren
page: https://pretalx.com/denog17/talk/39B3SK/
I would like to start by talking about the things everybody assumes you already know about SSH. This is aimed at giving you the essentials of using SSH, with the focus on using it for work. The workshop covers topics like pub/privkey handling, key-based (passwordless) authentication and keeping your keys secure. The goal for this first part is to hopefully give you a foundational understanding of how to start working (and what not to do) with SSH and SSH keys.

Once we get done with the basics, we can start talking about useful things you can do with ssh beyond the basics. Covering topics like port forwarding, proxy jump, SSH certificates, control channel reuse, properly using ssh_config etc

The goal is for you to walk out of this workshop with a good understanding of how to use SSH efficiently to help you to focus on the thing you're actually working on.

## 2025-11-09 — Workshop 701

### BGP for networks who peer (BGP beginners workshop)
Speakers: Wolfgang Tremmel
page: https://pretalx.com/denog17/talk/SEKB9D/
Workshop about the basics of BGP. Topics include:

- Prefixes and Autonomous Systems
- Why you also need an IGP (like OSPF, IS-IS)
- iBGP: BGP within your network
- eBGP: Talking to your neighbours
- Multihoming and Peering
- BGP Best Path Selection
- Bonus-Topics, if time permits:
    - BGP Communities
    - BGP Security

Lab experiments will be done using FRRouting, so participants do need a laptop. No special software is needed.

## 2025-11-09 — Workshop 901

### (Network) Troubleshooting Is Hard
Speakers: Jens Link
page: https://pretalx.com/denog17/talk/DUTQBM/
Every now and then, I see people do some pretty odd things when trying to troubleshoot network issues. Like using curl to test a domain name right after DNS resolution failed. Or jumping into a random GitHub issue because it mentions IPv6—so it must be the same problem. Or offering troubleshooting advice that's fine in general, but has nothing to do with the actual issue.

I've run a few troubleshooting trainings before, and honestly… I didn’t love them. They were always aimed at experienced network folks, but I kept finding myself going back to explain the basics.

So this time, let’s flip the script: I’ll walk through the fundamentals first, show how things connect, and then walk you through how I solved some real-world problems I’ve seen in the wild.

Expect plenty of live demos (mostly Linux-based), and if the group size allows, you’ll get your hands dirty in some labs too.

Oh, and fair warning: I’m going to say the word “documentation” a lot. You’ve been warned.

## 2025-11-09 — Workshop 811

### How to Talk to People Who Don’t Get You (Without Burning Out or Blowing Up)
Speakers: Susi Bauer
page: https://pretalx.com/denog17/talk/CV3TVJ/ | slides: https://pretalx.com/media/denog17/submissions/CV3TVJ/resources/DENOG_NVC_with_Sus_1MGTH18.pdf | slides: https://pretalx.com/media/denog17/submissions/CV3TVJ/resources/DENOG_NVC_with_Sus_0GlDTmF.pdf
Workplaces can be challenging to navigate when you’re part of one or more minority groups, e.g. neurodivergent, queer, and more. Misunderstandings, harsh feedback, and difficulty bringing across what they can leave talented people feeling overlooked or unheard. This workshop offers a practical approach to navigating these situations with calmness and clarity.

**By the end of this workshop, participants will**:
- Understand the core principles of Nonviolent Communication (NVC) and how to use them in everyday workplace interactions.
- Gain tools for expressing needs in a way that resonates with colleagues who may not share their lived experiences.
- Learn how to translate critical or poorly-worded feedback into actionable steps 
- Develop strategies for setting boundaries and standing up for themselves without burning bridges.

**Example workplace scenarios that we'll look into**:
- _A manager gives vague or insensitive feedback (“You’re too intense in meetings”)_ → We’ll practise breaking this down into practical next steps.
- _A colleague makes assumptions about your identity or needs (“Everyone’s fine with this open-plan setup, right?”)_ → We’ll explore ways to express needs in a constructive and relatable way.
- _You want to ask a manager for some accommodations, but don't feel confident they'll take you seriously_ → We’ll work on language and techniques that increase the chance of being heard and understood

**Workshop approach**
This will be an interactive and supportive session. Participants will practise new communication techniques through roleplay, guided exercises, and reflection. They’ll leave with practical frameworks, strategies, and confidence to apply immediately in their own workplaces.

### From Networks to Products: Breaking the Consulting Mold
Speakers: Moritz Frenzel
page: https://pretalx.com/denog17/talk/DB3UVV/
The network engineering industry is rich with technical talent but remains surprisingly underrepresented in the world of product-driven startups. In this workshop, Thomas Weible (CTO and Co-Founder, FLEXOPTIX) and Moritz Frenzel (CEO and Co-Founder, EdgeOps) share their entrepreneurial journeys, each shaped by a deep technical background and a commitment to building products instead of pursuing the traditional consulting route.

With FLEXOPTIX drawing on over 15 years of experience in building and growing a sustainable product company, and EdgeOps bringing the perspective of a fresh startup less than a year into its journey, the session offers both long-term insight and real-time relevance. Thomas and Moritz will each present a focused 15-minute talk covering their paths, followed by an open and interactive 90-minute discussion.

This workshop aims to inspire and equip engineers, founders, and future entrepreneurs with the confidence and perspective to transition from services to products, shifting from billing hours to building something that lasts, while also fostering connections between existing and aspiring founders.

## 2025-11-09 — Workshop 419

### Fiber Testing in Data Centers – Bringing Theory and Practice Workshop
Speakers: Svetoslav Nikolov, Jürgen Rummelsberger, Kimberley Rotolo, Markus Eilers
page: https://pretalx.com/denog17/talk/UVQNPF/ | slides: https://pretalx.com/media/denog17/submissions/UVQNPF/resources/High_Speed-Portfol_5MAWaFp.pdf | slides: https://pretalx.com/media/denog17/submissions/UVQNPF/resources/DENOG_Workshop_EXF_PPLOJbn.pdf
This workshop aims to provide participants with both a theoretical foundation and hands-on experience in modern fiber testing methodologies, specifically tailored to data center environments. As data rates increase and infrastructure complexity grows, accurate and efficient fiber testing becomes critical. The session will cover the essential testing principles, introduce the latest testing tools, and conclude with a practical component demonstrating real-world applications.  

The workshop will also introduce an innovative topic: Measurement techniques for hollow core fiber (HCF). HCF is emerging as a promising solution for ultra-low latency and high-capacity applications, presenting new challenges for testing and validation. Participants will gain early insights into how this technology is tested and what its adoption means for future measurement practices.

## 2025-11-09 — Workshop 420

### The basics of maintaining fiber optic connections
Speakers: Takaya Nakagawa, Yoshihisa Sakai, Miho Kudo
page: https://pretalx.com/denog17/talk/ST9LKU/ | slides: https://pretalx.com/media/denog17/submissions/ST9LKU/resources/Denog17workshop_11_IUdVttS.pdf
1. Basic knowledge of optical connectors and transceiver, explanation of the need for cleaning (30 minutes) - review of last year's content
2. Hands-on cleaning (45 minutes) - cable and transceiver cleaning procedures, inspection methods using a microscope, etc.
3. Hands-on polishing machine (45 minutes) - Participants will have the opportunity to experience working with handheld machine that engineers use on-site.
Will also learn about polishing methods, explanations of polishing grades, and precautions to take when polishing.
In the afternoon, you will be free to try and experience polishing and cleaning.(Free to leave at any time.)

## 2025-11-10 — Saal A

### Edge-of-Your-Seat Streaming: inside waipu’s terabit-scale live-video CDN
Speakers: Leo Antunes
page: https://pretalx.com/denog17/talk/SZZGTP/
Live video stresses every layer of a CDN: traffic spikes hit terabit scale in seconds, latency budgets shrink to single-digit seconds, and a single congested peering link can stall millions of viewers. This talk walks through how we built a custom Golang edge stack that now serves 5.5 Tbps across five German PoPs. We’ll unpack the caching hierarchy, peer-aware user steering that exploits BGP and ECMP, and the trade-offs between channel affinity, cache size, and uplink utilization. We'll also touch on observability with Prometheus and client-app telemetry enriched by CMCD.

### QoE Matters – How Application-Level Monitoring Pinpoints Network Issues
Speakers: Alexander Martin Dethof
page: https://pretalx.com/denog17/talk/WJ8JGT/
Network operations engineers maintain the backbone of our digital experiences, ensuring robust connectivity and managing complex routing. Yet, even with great network health, where are the current limits of today’s routing technology? What does it mean when your manager calls you and says “Our customers can’t watch Netflix!”? Can we measure how the end users experience the high variety of OTT-services, beyond classical speedtests? In this talk, we will investigate real-world scenarios where network issues, even seemingly minor ones, impacted video QoE. We'll demonstrate how solutions to these problems often go miles beyond classic NOC-room resolutions, requiring a deeper understanding of streaming protocols, user-centric performance, and QoE. Drawing on insights from standardized QoE metrics, we'll demonstrate how understanding the user's perception of video quality provides a critical new layer of visibility. This talk aims to equip network engineers with insights to proactively diagnose and address the hidden causes of poor customer video experience.

### Evolving Inter.link's Software Delivery: Lessons in Fast, Consistent, and Safe Deployments
Speakers: Poh
page: https://pretalx.com/denog17/talk/RZJPC9/ | slides: https://pretalx.com/media/denog17/submissions/RZJPC9/resources/Evolving_Inter.lin_AWMHbUw.pdf
Automation is at the heart of Inter.link's operations. Our team manages complex software that automates the entire customer journey, from correctly accepting orders for services such as IP Transit or DDoS and translating them into precise network configurations, to setting up billing and robust monitoring. This automation is critical, allowing us to rapidly develop and deploy new features while maintaining operational excellence.

Achieving this level of automation required investment in our software environment and tooling. Over time, we have significantly evolved our tooling, emphasizing easy and consistent environment setups, and we have implemented robust CI/CD pipelines that ensure changes are delivered to our customers safely, consistently, and quickly.

In this talk, we will provide a behind-the-scenes look at Inter.link's software stack. We will then explore challenges we faced that impeded quick, consistent and safe deployments, and how they informed and evolved our software environment. We will show the solutions we adopted, and how they became principles that provide guidance for the team. We will also finish off with a glimpse into some of our future initiatives.

### EVPN for the rest of us – what happens when software people try to use EVPN
Speakers: Molly Miller
page: https://pretalx.com/denog17/talk/BWHD38/
Last year we migrated our datacentre networks from a flat layer 2-based architecture to EVPN-VXLAN. As an organisation whose primary technical background is in software, a network project of this complexity has been a journey into new and uncharted territory.

Our previous network design had been showing signs of reaching its limits for several years, so in late 2023 we started designing a replacement based on EVPN-VXLAN, terminated directly on our Linux hypervisors. After not quite nine months of development the project culminated in an intensive week-long migration in our production datacentre – with zero downtime for our customers.

In this talk I'll explore our experiences developing and operating an EVPN-based network in production coming from a software background, including debugging tales from the lab and some of our more peculiar technical decisions, as well as the unexpected surprises along the way and ongoing pain points we're still dealing with a year down the line. What *does* happen when software people try to use EVPN anyway?

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings
Speakers: Dr. Gerhard Stein
page: https://pretalx.com/denog17/talk/NRBPX9/ | slides: https://pretalx.com/media/denog17/submissions/NRBPX9/resources/Flexoptix_-_Unders_DF4TtuC.pdf
In high-performance optical communication systems transceiver health and efficiency are critical to network reliability and energy consumption. This presentation explores the powerful capabilities of Versatile Diagnostics Monitoring (VDM) features found in modern optical transceivers (beyond the speed of 100G) with a particular focus on the Thermoelectric Cooler (TEC) current metrics. By analysing TEC current alongside temperature and cable length data we should be able to identify the optimal operating conditions that will minimise power consumption while maintaining performance. In order to prove this thesis we developed a couple of software prototypes to perform the data analysis. Using real-world VDM data this talk will demonstrate how to evaluate and visualise transceiver efficiency in terms of Watts, uncovering practical insights for engineers aiming to design or operate greener, more efficient optical networks and finally save energy.
Made by FLEXOPTIX Research - Gerhard and Thomas.

### Security.txt across the industry
Speakers: Sascha Heinemann
page: https://pretalx.com/denog17/talk/WKBJGE/ | slides: https://pretalx.com/media/denog17/submissions/WKBJGE/resources/20251110_Sectxt_Sa_KOxqk21.pdf | slides: https://pretalx.com/media/denog17/submissions/WKBJGE/resources/20251110_Sectxt_S_YeC31eD.pptx
This talk explores the adoption of `security.txt`, as defined in [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116),  that enables websites to publish security contact information in a consistent and accessible way. We begin with a brief introduction to the RFC and the motivation behind standardized vulnerability disclosure.
But is this even important to the network industry? To find out, we conclude with a focused analysis of security.txt adoption among organizations represented by this conference’s attendees, highlighting real-world trends, blind spots, and where we go from here.

### Sorry we messed up
Speakers: Stefan Funke
page: https://pretalx.com/denog17/talk/KQ9JWA/ | slides: https://pretalx.com/media/denog17/submissions/KQ9JWA/resources/DENOG17-lowres-com_ct1oD1K.pdf
How we route-leaked everything to everyone due to a fun Arista bug.

A post-mortem kind of story about us changing Arista RCF function names, resulting in a global route leak. The talk includes the history of why we intended to make a change, how we rollout configurations, why it resulted in an unexpected behavior and how it was fixed.

### Th3 Flock of Bird s
Speakers: Marcel Fest
page: https://pretalx.com/denog17/talk/XRVTP3/ | slides: https://pretalx.com/media/denog17/submissions/XRVTP3/resources/denog-17-slides_3affe3S.pdf
As Bird is evolving over the years and we now have Bird version 3 available at our fingertips, maybe we should know the capabilities of it and what performance we can expect from it.

Get some numbers in comparison with other routing stacks.
Let's take a quick look on the shiny new feathers Bird prepared for us.

### 400G ZR+ BiDi does not exist, it can't hurt you. Or can it?
Speakers: Nicola von Thadden (aka nicoduck), Arjan Koopen
page: https://pretalx.com/denog17/talk/KLXJS8/
As it's common practice, each new hacker event needs something weird and funky. For this years summer camp in the Netherlands called WHY2025, we build a 400G link over a single fibre. Since 400G BiDi does not exist (yet), we had to get creative and built something, which might be considered out of spec.

### Inventing the wheel - Network Orchestration at scale
Speakers: Tom Merlin Eichhorn
page: https://pretalx.com/denog17/talk/JECPAH/
At DE-CIX, we're redefining network orchestration from first principles. Confronted with the limitations of existing systems, we set out to design a modern orchestration stack—one capable of managing a truly global network, seamlessly interfacing with a variety of upstream and downstream systems, supporting fully managed network devices, and, above all, delivering uncompromising reliability.

In this talk, we share our transformation journey—from our starting point to our vision for the future. We'll delve into the architectural choices, design principles, and decision-making frameworks that guided our approach. We’ll also explore how we rigorously test our systems and highlight the critical lessons we’ve learned—insights that are applicable to any complex network automation project.

Our solution is built on three key pillars: a tightly integrated central source of truth for configuration management, an event-driven architecture for service orchestration, and a highly scalable design that accommodates rapid global growth.

To ensure stability and correctness, we've implemented a digital twin—internally dubbed Shadow—which mirrors the production environment. This shadow stack enables us to validate and test new software iterations in parallel, minimizing risk and accelerating confidence before deployment to real hardware.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T
Speakers: Thomas Weible
page: https://pretalx.com/denog17/talk/8N7Q3A/ | slides: https://pretalx.com/media/denog17/submissions/8N7Q3A/resources/Flexoptix_-_Channe_Xqpo1a5.pdf
Past approaches for maximizing the data capacity per fiber pair went for running more and more DWDM channels with grid spacings as small as possible. This meant that grid spacings shrank from 200GHz to 100Ghz and then 50GHz with some applications even going for 25Ghz. In recent years the bandwidth per channel kept increasing, as complex modulation schemes came into favor over ON-OFF-Keying which has been a staple in fiber optic communication for decades. Those increased per channel bandwidths of 400Gbps, 800Gbps and now pushing into the 1.6Tbps realm demand for lager grids to accommodate the spectrum necessary to operate such “Superchannels”. Especially the fact of coherent detection being “blind” to anything but its own wavelength has enabled interesting topologies that can omit filters altogether. Of course that comes at a cost of reduced flexibility. Learn how you can harvest some of those benefits by moving to 400GHz filters while keeping a lot of your flexibility. Keep your 10Gbps and below legacy signals on the same fiber as your fast stuff and easily reassign your bandwidth without the cost ROADMs.
Made by FLEXOPTIX Research - Gert and Thomas.

## 2025-11-10 — Saal B

### EVPN Flex Cross Connect - L2 P2P VPNs can be agile as well!
Speakers: Tobias Heister
page: https://pretalx.com/denog17/talk/FNVVFQ/ | slides: https://pretalx.com/media/denog17/submissions/FNVVFQ/resources/DENOG17_-_Tobias_H_CTPBKn6.pdf
EVPN is (now) a well know Service Framework and is widely used as a replacement for VPLS ELAN Services and even some IP-VPN Services.

EVPN was able to also do P2P ELINE Style services for quite some time, but with the finalization of RFC9744 it got some very interesting capabilities that can especially help aggregation networks to reduce scaling problems.

The talk will give a very brief primer on how the EVPN Service Framework is being setup to allow for easy extension, focuses on the Flex Part of the new extension and will give some examples on how this impacts some (near to) real world scenarios.

### Entering the big Cloud Game: A journey of ups and downs towards sovereignity at scale
Speakers: Michael Bayr, Gerhard Bader
page: https://pretalx.com/denog17/talk/F9DVEL/
This talk would be held by my two colleagues: Michael Bayr (artcodix) and Gerhard Bader (Yorizon Cloud)

Yorizon Cloud is the joint venture of HOCHTIEF PPP Solutions and Thomas-Krenn.AG

In these times of global political and technical threats and disruptions, we are driven by our spirit of digital sovereignty when we design a new European, de-centralized, sustainable and custom-made cloud infrastructure.

In their talk, my two colleagues would give an insight into the technologies we apply, open source based and European to the core. One basic focus will be the network technology and the standardized stack that we use.

We will be happy to present this talk at DENOG17, feel free to contact me personally if you would like to get in touch with our two potential speakers.

### Performance measurement goes Flow
Speakers: Péter György
page: https://pretalx.com/denog17/talk/YGMU8X/ | slides: https://pretalx.com/media/denog17/submissions/YGMU8X/resources/20251107_Performa_NS4FVUM.pptx
Do you have probes installed to monitor your network border? Ever struggled to estimate the fallout-perimeter of a probe alerting quality-deterioration? We show an example how to firmly map probes to interconnect points and secondly, how to identify which other traffic is likely affected by the same problem.

### "What can possibly go wrong?" Stories of peculiarities of modern server hardware
Speakers: Vladimir Smirnov
page: https://pretalx.com/denog17/talk/VJJ9RC/ | slides: https://pretalx.com/media/denog17/submissions/VJJ9RC/resources/DENOG17_22What_ca_UOzA5i3.pdf
After discussing building a 1 Tbps/1 Gpps load generator on commodity x86-64 hardware, one of the most common follow-up topics was the reasoning behind some of the decisions. And here I've realised that it is not commonly understood that modern systems are more complex than classic multi-socket NUMA systems, and that if you don't consider some of their peculiarities, you won't achieve the expected performance. In this talk, I want to explore what happens when you break those assumptions and how you can identify them. All examples would be based on the assumption that you are using Cisco T-Rex for load generation and fd.io VPP as a target load.

### 200 GbE network processing with 100 W - or "can I *make* a chip for that?"
Speakers: Philipp Keydel
page: https://pretalx.com/denog17/talk/VEGBSU/ | slides: https://pretalx.com/media/denog17/submissions/VEGBSU/resources/network_offloading_Id8Nh2e.pdf
This talk presents how to to offload networking tasks onto dedicated hardware/smartNICs/NPUs (network processing units) - chips, and why this is a great idea.
First, we take a look at chips in general - how they are made, integrated into networks, and why time is playing to the advantage of dedicated chips vs. CPUs/software.
Then, focus is on how offloading network tasks is a particularly beautiful example of the advantages of hardware-implementing logic, with examples like TCP offloading, cybersecurity applications, or traffic shaping.
To be fair and balanced, there will also be a look at the downsides of chips, but of course also ideas for mitigating them.
Finally, there will be a look at what's out there, and how to integrate custom chips into your systems.

### Ultra Ethernet: Addressing AI/HPC Interconnect Challenges Beyond the InfiniBand Monopoly
Speakers: Andreas Roeder
page: https://pretalx.com/denog17/talk/W8W77A/ | slides: https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEtherne_RJk4QyN.pdf | slides: https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEtherne_vMqLytv.pdf | slides: https://pretalx.com/media/denog17/submissions/W8W77A/resources/DENOG-UltraEthern_9wZpuEn.pptx
For years, InfiniBand has dominated high-performance interconnects. Yet for strategic and technical reasons, there has been a huge industry ask to develop a new next-generation protocol for use in AI and HPC environments. This session introduces Ultra Ethernet, an innovative standard designed to tackle the limitations seen in RDMA around scalability, latency and congestion management, crucial for democratizing future AI/HPC build outs. Join us for a comprehensive exploration of the technologies poised to redefine Storage or GPU interconnectivity and challenge the status quo.
We also discuss the future of the UEC and how collaboration among standards organizations will benefit the industry.

### Forwarding packets at scale - Building a Cloud Data Plane using eBPF/XDP
Speakers: Maximilian Wilhelm, Marcus Wichelmann
page: https://pretalx.com/denog17/talk/VNLHD7/ | slides: https://pretalx.com/media/denog17/submissions/VNLHD7/resources/slides_tUew2WC.pdf
At Hetzner we’ve historically used an Open vSwitch based data plane for connecting hundred thousands of cloud servers to the network. This has served us well for many years and mostly still does. We have however reached some limitations and wanted to improve scalability, resiliency and flexibility with a more specialized data plane that's tailored to our needs while being easy to operate and building a strong foundation for new features.

When checking our options back in 2022, the team reached the conclusion that the best path to achieve this goal is to build and maintain our own highly specialized networking stack based on eBPF/XDP, and so we went on a journey to make it reality.

Today, roughly three years later, we’ve implemented a versatile network stack, called `hcnet`, which handles public and private cloud networking (using VXLAN encapsulation), stateful firewalls, and provides DHCP services as well as traffic capture tooling - all of this using XDP with a control plane written in Go.

To make operation’s life easier, the stack is collecting and exposing meaningful metrics and is designed to self-heal whenever possible. We’ve been using `hcnet` in our internal cloud for two years now, with every new feature getting its first real-world tests there on a daily basis, including customer-facing applications. We are looking forward to a public beta, once we have full feature parity with our existing stack.

In this talk we want to provide an overview of how we’ve built the new network stack, what challenges we’ve faced and where we're hitting current limitations of XDP. As of today the most pressing challenges are support for offloading and driver maturity in general.

## 2025-11-10 — Working-Groups (Room 901)

### Access and ISP WG - Kick-Off Meeting
Speakers: Christian Giese, Andreas Kimpfler
page: https://pretalx.com/denog17/talk/L8QFRX/
The new working group aims to create a dedicated forum for the exchange and development of solutions relating to national challenges in the field of Internet Service Providers (ISPs) and access infrastructures in Germany. Our mission is to fill the gap between the Routing WG and all the other essential topics involved in running an ISP in Germany. 

The aim is to create a forum where internet service providers, vendors, and other interested parties can come together to discuss these topics and collaboratively develop an ISP handbook.

Whether you’re an expert, a tech enthusiast, a legal mind, or simply interested, you’re welcome to join our young and open working group.

Topics such as routing or peering are dealt with in the sister group, the Routing WG. Both groups work together where there may be areas of overlap.

**Key Topics:**
* Access Technologies like xDSL, PON, AON, and how to build access networks
* BNG-related stuff
* Added value services like Telephony or IPTV
* L2BSA / L3BSA
* IT-systems need to run your network (RADIUS, DHCP, Logging, Provisioning, ...)
* Auto Configuration (ACS) and CPE Management
* Regulatory Requirements in Germany (TKG, LI, VDS,...)
* Create reference configurations

As all these topics are mainly related to local regularities in Germany, the meetup's primary language will be German.

## 2025-11-11 — Saal A

### Making Network Automation Consumable: A Junior Engineer's Perspective
Speakers: Emre Cinar
page: https://pretalx.com/denog17/talk/VA9SFE/ | slides: https://pretalx.com/media/denog17/submissions/VA9SFE/resources/DENOG_Presentatio_dib5bcy.pptx
As a Junior Engineer, the consumability of a network automation tool can really make or break your experience. Some incredibly smart engineers and developers build amazing tools for specific use cases, but they can be tough to use unless you know all their quirks. This is especially frustrating when you're just starting out. That is why I want to share a small project I worked on including all the applications I used and what I learned from it. Fancy tools are great, but at the end of the day, someone has to actually use them—both now and in the future, right?

### PPPoE vs IPoE: A Practical Guide for ISPs
Speakers: Christian Giese
page: https://pretalx.com/denog17/talk/RMB983/ | slides: https://pretalx.com/media/denog17/submissions/RMB983/resources/PPPoE_vs_IPoE_-_DE_jXNB9cD.pdf
**Is PPPoE really legacy? Is IPoE really better? And what actually happens when something breaks?**

This talk takes a hands-on look at PPPoE and IPoE (DHCPv4/v6) in real ISP environments, based on actual deployments, not just specs. We’ll walk through the key operational differences that show up when things get serious: high availability, failover, MTU handling, multicast, and how dual-stack plays out in practice.

We’ll also dive into the hidden pain points, like why hardware offloading fails in unexpected places, why VLAN models (N:1 vs 1:1) must be considered here, and how session state behaves when routers crash or links go dark.

There’s no silver bullet, but you’ll leave this session with a clear picture of the trade-offs. Whether operating PPPoE or IPoE, or stuck managing both, this talk gives you the good, the bad, and the “we didn’t see that one coming”.

If you’ve ever had to troubleshoot weird subscriber issues at 2 AM or explain to management why “it’s complicated”, this talk is for you.

### An introduction to qGIS for current Google Earth Users
Speakers: Christian Dieckhoff
page: https://pretalx.com/denog17/talk/HFMA8N/
The defacto standard in network planning is to use Google Earth for dealing with a large collection of kmz and kml files that are provided by partners. Sadly this can quickly introduce spontaneous combustion of your computer or at least of google earth, as the data collection can grow quite quickly and that software as probably never meant to deal with such an enourmous amount of geodata.
Luckliy there is a widely adopted open source GIS software called qGIS that can help with exploring large amounts of data. I will give a quick intro what shortcuts, plugins and quirks you can utilize to use qGIS for your KMZ Collection and do a "first steps for people in the network industry" tutorial.

### Slow network, fast money: How Deutsche Telekom breaks the internet
Speakers: Thomas Lohninger
page: https://pretalx.com/denog17/talk/8NGPVU/
In Europe, net neutrality is a principle enshrined in EU law which states that all data on the internet should be treated equally - but what happens when large providers such as Deutsche Telekom systematically violate it with their interconnection practices? 

The Netzbremse project documents an alarming case: millions of Deutsche Telekom customers are experiencing artificial throttling of their connection because Telekom refuses to expand its peering capacities appropriately. As the only internet provider in Germany, users and network operators have to pay at both ends of the line to avoid congestion. The result: massive quality losses in video streaming, gaming and online conferencing - especially in the evening. Network operators and content providers who are not prepared to pay for an uncongested connection suffer from poor service quality. An alliance of consumer protection, civil society and research is now taking action against this direct attack on the open and free internet.

### IXP Update
Speakers: Tim Kleefass
page: https://pretalx.com/denog17/talk/CMR8MS/
News from IXPs in Germany
As introduced 2021 we collect some parameters from all IXPs, which are active in Germany.
This talk aggregates the Updates for all the IXPs in a common format and will be presented in a neutral way.

### Merging Service Provider Networks
Speakers: Markus Jungbluth, Bastian Hoss
page: https://pretalx.com/denog17/talk/L7TDFF/ | slides: https://pretalx.com/media/denog17/submissions/L7TDFF/resources/denog17-merging-sp_tTpqc3X.pdf
As the German service provider market slowly consolidates, network engineers and architects will increasingly face the complex challenge of merging service provider networks. This technical talk dives into the intricacies of integrating distinct IP/MPLS network infrastructures, focusing on practical considerations and potential pitfalls. Based on past experience, we will discuss the general approach to such a project, key architectural considerations, and challenges related to routing protocols and vendor interoperability.

### You can’t just model a train in Netbox: About Architecting and running modern IT Infrastructure in Trains
Speakers: Vanessa Gaube
page: https://pretalx.com/denog17/talk/K3HSNK/
At DB Fernverkehr, we are running some IT Infrastructure on a large fleet of ICE Trains. 
In the past, there was only WIFI for the passengers, and many systems were handled as “embedded systems”. Nowadays, more aspects of “modern IT infrastructure” are part of the IT in trains, providing additional services like passenger information.

This talk gives a quick introduction of what is happening on the trains, as well as some of the challenges compared to infrastructure built in data centers: How to get proper internet on the train? How can a network look like? What is the difference to the data center with regards to hardware selection and lifecycle? Do we even have racks? And most importantly: Why can’t we just model a train in netbox?

## 2025-11-11 — Saal B

### Uncovering Blackholes: Advanced Detection Techniques for Complex Networks
Speakers: Anton Elita
page: https://pretalx.com/denog17/talk/GJNTXH/
Blackholing events often have prolonged impacts and typically require manual intervention for recovery. Even a single occurrence is highly disruptive, frequently triggering executive-level escalations. Resolving such incidents demands top-tier expertise and often involves engagement with the vendor’s advanced technical support.

To accelerate root cause identification, we present several methods for detecting blackholing events, identifying the affected transit flows, and analyzing potential correlations. This approach aims to reduce response times and improve overall network resilience.

### The Asian internet - A guide for the uninitiated
Speakers: Bernhard Pusch
page: https://pretalx.com/denog17/talk/CAD9N7/
The Internet is not the same everywhere. And in Asia, the world’s most populous region with some of the fastest growing economies, it can be especially complex. 
Join Telstra to learn about how differently the Internet operates in Asia compared to Europe and North America, how those behaviour are likely to change as the impact of new AI workloads is felt across global networks, and what variables you need to think about when architecting your own network so that your company can make the most of the huge market opportunity Asia offers.

This talk will cover:
	The history of the internet in Asia
	How routing has developed between countries within Asia and to the rest of the world
	Geographic influences on digital infrastructure across the region
	Geopolitical influences on network traffic and market access
	How AI is starting to influence subsea and IP networks in Asia Pacific
	Recommendations on how to make your digital infrastructure future ready to capture the growth opportunity in Asia

### The return of EGP or the curious case of the BGP Origin attribute
Speakers: Wolfgang Tremmel
page: https://pretalx.com/denog17/talk/ASAQKE/ | slides: https://pretalx.com/media/denog17/submissions/ASAQKE/resources/e-wt-20250807-RIPE_kmDkegi.pdf
The BGP Origin attribute has been around for decades and did not attract much attention. It is simply there, shown either as "?" for "incomplete" or as "i" for IGP.

During writing slides for my BGP training I found a large number (868) of prefixes in the global routing table tagged with "e" for EGP. The presentation does not give any answers but simply raises the question who and why is playing with that attribute.

### Baremetal Server Management with Redfish
Speakers: Matthias Haag
page: https://pretalx.com/denog17/talk/79G7TQ/ | slides: https://pretalx.com/media/denog17/submissions/79G7TQ/resources/Manage_baremetal_s_sICOr5i.pdf
Managing bare metal servers has always been quite time-consuming and prone to errors. Manual steps are required to configure the BMC, adjust BIOS settings, and, if necessary, perform firmware updates. If you have many servers to manage, you have to repeat everything on each individual server which likely to cause errors and diverging configurations.

We have been working for some time to automate all of this with Redfish. OpenStack Ironic helps with this, among other things, but it does not work out-of-the-box with all hardware. Unfortunately, most manufacturers believe that the Redfish standard should be implemented differently or some endpoints are not necessary.

In this talk, I will provide insight into the experience we have gained, how far we are currently, and what we still have planned.

### CGNAT scale testing using TRex
Speakers: Philipp Glaser
page: https://pretalx.com/denog17/talk/G8PZUA/
I would like to present my testing methodology and the results of using TRex to generate "stateful" traffic for the purpose of scale testing CGNAT solutions. The main focus of the test is to determine the actual scale around Juniper's SRX solution.

### Compliance in Practice: Making NIS2 and ISO 27001 Work in Daily Operations
Speakers: Mathias Handsche
page: https://pretalx.com/denog17/talk/DUMD8G/ | slides: https://pretalx.com/media/denog17/submissions/DUMD8G/resources/20251111_Lean_Comp_CkVft3e.pdf
With NIS2, ISO 27001 and requirements of BNetzA raising the bar for security and operational compliance, many internet providers are asking the same question: *How do we meet these requirements without drowning in bureaucracy?*

This talk bridges the gap between regulation and real-world implementation. Instead of focusing on theory or checklists, we’ll look at how to integrate compliance into the day-to-day work of running a network—with minimal friction.

**Topics include:**

- Turning compliance into a continuous, manageable process  
- Using a Single Source of Truth (SSoT) to manage documentation, assets, and controls  
- The “document once, but right” principle: reducing duplication and inconsistency  
- Assigning and tracking responsibilities that actually get done  
- Lessons from real-life audits and what works in lean teams  
- Tooling, automation, and pragmatic templates to stay compliant while staying sane

We will demonstrate these concepts using open-source tools like:

- **NetBox** for infrastructure inventory and network documentation  
- **Snipe-IT** for asset lifecycle management  
- **Zammad** for task and ticket tracking  
- **Eramba** for managing risk, controls, and policy compliance  
- **GitLab** for documentation, version control, and approval workflows

These tools help create a practical compliance framework that integrates seamlessly into daily operations and supports both audit readiness and operational efficiency.

This session is tailored for engineers, DevOps, and infrastructure managers at ISPs and hosting providers who want to build a compliant operation—without losing focus on uptime, performance, and business continuity.

**You’ll walk away with concrete strategies and examples you can apply on Monday.**

### Fun with Optics
Speakers: Patrick Prangl
page: https://pretalx.com/denog17/talk/AXEKSR/ | slides: https://pretalx.com/media/denog17/submissions/AXEKSR/resources/2025-DENOG-Fun_wit_0buk8u3.pdf
This talk dives into the cutting-edge developments shaping today's silicon landscape, showcasing the leap to 800Gbps Ethernet and setting the stage for the transition toward 1600Gbps. We’ll spotlight Linear Interface Optics technologies and show how those can reduce the power consumption. To wrap up, we’ll explore the evolution of ZR and ZR+ optics.

### IPv6 multihoming without BGP, quo vadis?
Speakers: David 'equinox' Lamparter
page: https://pretalx.com/denog17/talk/QNDD3G/ | slides: https://pretalx.com/media/denog17/submissions/QNDD3G/resources/slides-denog17-ipv_0gJks2a.pdf
Well, there's always NAT, or NPT. But that's supposed to be the *dark ages* 20th century IPv4 solution. So how do you do it *nicely* in IPv6?

The "nicest" possible approach seems to be dst-src routing (aka SADR, aka sourcedest) — this talk summarizes the situation before diving into that solution. You will hopefully come away with an understanding of how this isn't policy routing, what router features are still spotty, what RFC 6724 "rule 5.5" and RFC 8028 are, and why a Linux based system is simultaneously the best router and the worst end host in this.

### Going Large: Extended Route Targets or Extended Confusion?
Speakers: Robin Christ
page: https://pretalx.com/denog17/talk/JVGJ8S/ | slides: https://pretalx.com/media/denog17/submissions/JVGJ8S/resources/DENOG_Extended_Rou_arhUVKT.pdf
Conventional BGP Route-Targets are not large enough for modern large-scale eBGP-only EVPN-VXLAN fabrics. We will look into a new type of Route Target I propose, the "Extended Route Target" based on BGP Large Communities

## 2025-11-11 — Working-Groups (Room 901)

### Routing WG Meeting
Speakers: Vincentz Petzholtz, Andreas Kimpfler
page: https://pretalx.com/denog17/talk/G3YJBS/
Meeting of the DENOG Routing-WG:
Since a couple of years we have driven a working group called routing which focuses on public peering, policy drafting, strategy and filtering best practices. One of the main goals is to create a guide containing these BCPs for different vendors on https://routing.denog.de. 

The working group acts as an point of discussion, coordination and reviewing those BCPs. We take care of content as well as reviews and merging PRs on our Github repo https://github.com/denog/routing-guide.

Everyone can participate and be part of the WG. But even if you don't want to deal with the WG you can still draft PRs on Github and submit them for review!

The meeting at denog will be used to discuss any topics as long as we can make it happen within the given timeframe. We will also have to vote for our chair this year. We would be happy to have you with us!

Your WG Org
Vincentz (Chair) and Andreas (Co-Chair)

PS: 
Mail List/Group:
https://groups.google.com/a/denog.de/g/denog-wg-routing
Matrix Chat Channel:
https://matrix.to/#/#wg-routing-general:denog.de

