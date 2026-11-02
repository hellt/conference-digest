>>> HOW TO RUN THIS <<<
This is the digest prompt for cfgmgmtcamp-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/cfgmgmtcamp-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/cfgmgmtcamp-2026.md
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

Below is the program for CfgMgmtCamp Ghent 2026 (vendor). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a vendor / community program (e.g. a CNCF or vendor conference).
Separate genuine technical or strategic substance from product marketing.
Down-rank pure product pitches and sponsor slots. Up-rank end-user case studies
with real numbers (scale, latency, cost, incident detail), contributor-led
architecture and internals talks, and sessions that reveal where an open-source
project is actually heading. Be skeptical of "we adopted X and it was great"
talks with no metrics or failure discussion.

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
conference: CfgMgmtCamp Ghent 2026
type: vendor
source_url: https://cfp.cfgmgmtcamp.be/ghent2026/schedule/export/schedule.json
generated: 2026-11-01
registry_key: cfgmgmtcamp-2026
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## 2026-02-02 — D.Aud

### We Built for Predictability; the Workloads Didn’t Care
Speakers: Michael Stahnke
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/AGSYJ3/
Infrastructure engineering has been built on predictability. If you specify the state, enforce it consistently, and eliminate drift, the system behaves as expected. Determinism was the goal and configuration management gave us the tools to get there. However, today’s AI models, agentic systems, and other probabilistic workloads break that mental model. You can deliver a perfectly reproducible environment and still see the application layer behave differently from run to run. The foundations didn’t fail; the workloads simply play by different rules. This talk is about how to reason in that new world. When outcomes aren’t guaranteed, what can you rely on? How do you decide what must stay deterministic, and where you can safely allow randomness? How do you operate and troubleshoot when “it depends” becomes even more of a normal, expected answer? Instead of fighting to make probabilistic systems behave deterministically, we’ll explore how infrastructure engineers can build clarity, confidence, and reliability by embracing a different way of thinking; one that treats unpredictability as a property we can work with rather than a flaw we must eliminate.

### The exploitation paradox in open source
Speakers: Richard Fontana
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/KP9YPK/
Open source has always balanced freedom and power. Each era, from the rise of Linux to the cloud to generative AI, reveals the same flaw and the same strength: ideals built to maximize liberty inevitably create new leverage points. This talk traces that recurring pattern and argues that open source’s periodic crises are not failures but feedback loops, teaching us how to keep freedom alive in changing infrastructures.

### AI Native Infrastructure Automation: how I learned to stop worrying and love Claude
Speakers: Adam Jacob
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/UGTUYH/
I get it. You tried using AI tooling to write some terraform, or to vibe code an application, and it generated an unholy mess of slop. We’re ruining the planet with the heat generated from datacenters, people are losing their jobs, and the whole thing feels like a bad speed run of web-3 style crypto grift combined with astronomical levels of unattainable hype. It’s a bubble that’s bound to pop. What you want is for the whole thing to just go away, really, if we’re being honest with each other.

But it won’t. Because it turns out, LLMs are incredibly useful technologies, and the industry has only really learned how to use them well in the last six months. The metaphorical genie is, in fact, out of the bottle. In this talk I’ll show you how building an AI Agent transformed System Initiative from the top down, and radically changed my perspective on what’s possible in infrastructure automation. I’ll go deep into how things work, why they work, and what it all means for how our corner of the industry works moving forward.

### Just Enough Container Orchestration
Speakers: Kris Buytaert
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/GAV8C3/
Lets face it ... containers are here to stay,  yes plenty of people abuse them for the wrong reasons , but they have some benefits too. 
But the ecosystem to run them is till way to complex for the average organisation.    You are not Google, You ain't gonna need K8s.  But do want  Just Enough Container Orchestration.

This Ignite will give you an idea on how to get there. 
Maybe even a working Proof of Concept.

### The 7 Deadly Sins of GitOps
Speakers: Koray Oksay
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/H3TNHR/
GitOps promises simplicity, consistency, and automation, but without discipline, it can just as easily invite drift, outages, and operational pain.  GitOps is not a "set it and forget it" solution; it's a living, breathing system that requires ongoing maintenance and nurturing over time.

In this talk, you will learn to understand the pitfalls of not caring about best practices in GitOps through real-world examples and lessons learned. We will cover sins such as pride (ignoring drift), envy (Blindly copying other GitOps setups), sloth (ignoring reconciliation errors), and others, as well as practical fixes and patterns that teams can apply to build more resilient and sustainable workflows.

Whether you're new to GitOps or scaling an enterprise platform, this talk will help you spot warning signs early, avoid painful mistakes, and strengthen your GitOps practices with confidence.

### OpenVoxView - Current State
Speakers: Sebastian "Spritzgebaeck" Rakel
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/8GGRD8/
Short Talk about the new features in OpenVoxView and short Introduction to OpenVoxView

### A step to build 10x engineering teams
Speakers: Ulf Månsson
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/HJSY8S/
This talk examines the factors that can significantly increase developer and team efficiency. According to a study by IDC, developers today spend only about 30% of their time on coding and requirements. I’ll share experiences from teams where I’ve helped build a developer experience that raised that number to around 80%. Through standardization and automation, we improved both productivity and team collaboration. These foundations also make it easier to adopt AI effectively and gain even more efficiency from AI-driven workflows.

### Classic Infrastructures Command & Control
Speakers: Alessandro Franceschi
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/U78BGH/
Pabawi is a new Web frontend to manage and inventory your infrastructure systems: it currently supports Bolt and Puppet, with planned integrations with Ansible and other tools that interface with good old "legacy" physical or virtual systems (there's always an OS somewhere to deal with, after all).
The Ignite is a quick overview of Pabawi features.

### Try to do one thing, and do it well
Speakers: Yair Etziony
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/TF9BZB/
After 30 years in this field and too many years away from actual code, I came back. What I found frustrated me enough to start building. AI gave me the velocity, but the direction came from decades of seeing the same patterns return, dressed in new syntax.
I built most of these tools around Kubernetes. Not because I love it, but because I was already frustrated from working with it. After five years of managing a DevOps consultancy, I understood something: you can't convince everyone who doesn't need it not to use it. It's a standard now. It's everywhere. So I stopped fighting.
But going deep into its ecosystem, really learning it, something clicked. I remembered there was something else out there. Something that could do some of these things more elegantly.
Eleven tools in seven months. Still a work in progress. Our modern stack has real engineering in it. But somewhere along the way, we fragmented what used to be unified. We solved problems that were already solved, just in places we weren't looking.

### 7 Ways to Fail at Building a Platform
Speakers: Coté
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CU9TCZ/
Building your own internal developer platform can seem attractive, but it's a risky proposition. In a platform as a product approach, when you build it, you own it, and now you're in the business of developing a product instead of your actual business. In this talk, drawing from 10 years of platform engineering case studies of large organizations, Coté will go over seven risks of building your own platform: expansive scopes, underestimating cost, project mindsets, death by customization, skills, security and compliance, resume-driven development. You can learn from the many people who've suffered these risks already and, hopefully, avoid them yourself.

### A Pkl companion tool to bind tasks to configuration data
Speakers: Stoned Elipot
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/R8ABQZ/
Infrastructure as Code may seem to be all about tools and their languages but it is mostly about models and the data to express them. This data must often be processed to facilitate its use by multiple tools, like
Ansible, OpenTofu, Helm or your favorite new shiny tool.

Hence data pipelines must be implemented. The targeted IaC tools can be used for this implementation, and also, of course your favorite interpreter.

The [Pkl](https://pkl-lang.org/) configuration language is a powerful ecosystem to organize, shape, validate, transform, etc. data and provide it to those tools in the appropriate form and syntax.

The proposal here is to use a simple companion tool to the Pkl language to help implementing the mentioned pipelines.
This tool defines so-called "tasks", written in the Pkl language, eventually embedded in the very same Pkl modules defining the processed data.  The tasks consist of any commands, parametrized by and consuming data produced by Pkl evaluations.

It is a tool to "bind tasks and Pkl", or tpkl.

### How automation games can make us better engineers
Speakers: Greg Sutcliffe, David Moreau-Simard
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CBHVKV/
We all have constraints, like budget, time, and resources. Dealing with them through imperfect choices results in technical debt, while learning and better technology creates opportunities for optimizations and refactors. 

How can we practice dealing with these things *before* they cause us significant issues ?

Factory‑sim games (like Factorio, Satisfactory, and many others) might drop us on an alien world with a pickaxe and a deadline: survive long enough to research technology and build supply chains to launch stuff in space.

- Starting from scratch, we'll need to learn what tools and architecture are available to us.
- At first we'll craft things manually like we would with a CLI but that doesn't scale.
- Soon, we start automating with machines (like scripts) and eventually we automate the automators, Ansible or Terraform style.
- Then, entire factories can be packaged with clear inputs and outputs just like containerized applications.
- Before long, these factories are connected by networks of conveyor belts, drones and trains like supply chains in the middle of pipelines.
- We'll need to troubleshoot issues and identify bottlenecks with the help of observability and alerting, too.
- We might even need to defend ourselves and set up security.

Sound familiar ?

These games mirror the skills we need as engineers. In this talk, we'll explore some of these games, in order to show how they provide a fun and safe place to improve our skills in designing & building scalable systems. Recording available: https://www.youtube.com/watch?v=yxzghm3Fdj8&t=24413s

### Mgmt Config: Unexpected things mgmt can do
Speakers: James (purpleidea)
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/AAUVX8/
Mgmt is a real-time automation tool that is fast and safe. It has passed version 1.0.0 and is almost too powerful to describe, so we'll demo!

It can manage GNOME settings, change firmware BIOS settings, build virtual machines, manage firefox, and more.

This will be a smorgasborg of small mgmt demos and other topics which will showcase many of the things that were built for customers.

We are managing routers, vm hosts, provisioning metal with automatic power-on, and so much more.

We'll show new features in the 1.0.0 release including real-time exported resources (how they should have been done) declarative looping, show our gloriously fast function engine, and more!

As usual, I'll live demo to your hearts content!

Some introductory documentation is available: https://mgmtconfig.com/docs/guide/
Attendees are encouraged to read some before the talk if they want to get up to speed.
A number of blog posts on the subject are available: https://purpleidea.com/tags/mgmtconfig/

### Community and Business
Speakers: Martin Alfke
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/TQJT8P/
Open Source is essential for most IT orgs.

Whether you run native applications or containers, there is always open source underneath.

Open Source is developed in public by people who are interested and engaged.

Companies take open source, change colors and sell this as a product. The larger the company, the higher the price.

Why should a community not participate as business and get their value? I will talk about possible ways a community can collect and spend money.

But community and business are difficult to combine.

In my talk I will give an insight, how the OpenVox/Puppet community has started becoming more "business-like".

## 2026-02-02 — B.Con

### In 30 minutes from scratch to an enterprise-grade web app with open source & GenAI
Speakers: Marcel Kornegoor
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/AARD3F/
Can you build an enterprise-grade web app and get it up and running from scratch in exactly 30 minutes using nothing but GenAI and open source software? That's the question and goal of this talk. We'll start using a .env file with credentials, a detailed design describing the desired app and... an empty git repo! Let's hope the demo gods will be kind to us. Can you build an enterprise-grade web app and get it up and running from scratch in exactly 30 minutes using nothing but GenAI and open source software? That's the question and goal of this talk. We'll start using a .env file with credentials, a detailed design describing the desired app and... an empty git repo! Let's hope the demo gods will be kind to us.

After a short introduction, we'll put GenAI to work and discover whether it will deliver a working end result after 30 minutes of crunching GPUs. 

Some clear boundaries will be set, including:
- app will be written in Python
- must use open source software and modules only
- will be hosted on Hetzner using only IaaS (for portability reasons)
- must use security best practices (IAM, secrets management, encryption etc.)
- will use Stripe for payments
- must use IaC, so the whole project is fully portable and versioned (e.g. Ansible, Terraform, etc.)
- end result will be open sourced on GitHub using an MIT license
- must be well documented (SBOM, README, getting started etc.)
- LLM used will be decided shortly before the talk (because they change a lot)

There is no telling upfront whether GenAI will succeed or fail on this mission -and that's the point. This session aims to show what GenAI is currently capable of, and where it still might have flaws or limitations. So let's focus on the journey here and not on the end result.

### Automation Without Apprentices: How AI Challenges the Open Source Way
Speakers: Bernd Erk
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/7YDSYT/
Infrastructure used to be something you learned by breaking things, fixing them, and asking people smarter than you for help.

Today, AI tools promise to skip that part. You can generate configs, debug systems, and write code without ever really understanding what’s going on. It’s fast and efficient, but it also quietly removes the path from junior to senior.

If we replace learning with automation, we won’t just lose jobs; we’ll lose the next generation of people who know how things work. This isn’t only a technical problem. It’s a cultural one.

As a community, we have to decide whether open source remains a space for shared learning and mentorship or just another layer of abstraction we consume.
This talk is a reflection on what we’re giving up in the name of progress and how the open source world might still hold the antidote. AI makes everything faster, except learning.
If we automate the path from junior to senior, we risk losing not just skills, but the communities that pass them on.
This talk explores how AI changes how we grow, share, and build, and why open source might be our last real school of engineering.

### On the Path to Digital Twins: Loosely Coupled Infrastructure Models
Speakers: Pavel Lavrenko
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/RZ8FQZ/
Operations and DevOps teams – both human and agent-based – struggle to keep a coherent view of their infrastructure. Infrastructure as Code repositories, configuration management tools, orchestrators and monitoring systems often drift apart from each other and from reality. Knowledge about “what is running where and why” is fragmented across people, services and tools, especially in fast-moving hybrid setups spanning on-premise and multiple clouds.

In this talk we present Foliage, an open-source project that helps to build a distributed, graph-based “digital twin of infrastructure”. The system aggregates facts from cloud and on-prem sources, enriches them with human and automated knowledge, and formalizes the relationships between them in a loosely-coupled set of models that continuously update themselves from events in your infrastructure.

Instead of a single monolithic model, we work with many small, loosely coupled graphs that can evolve independently, be owned by different teams and shared or reused across domains. These models can be sliced into task-specific views – from incident investigation and drift detection to change-impact analysis and migration planning. We will show real-world examples from production and a live demo of how such models look and behave.

The talk targets operations and DevOps engineers, SREs, platform and tooling architects who are interested in building flexible, extensible and transparent knowledge systems around the infrastructure they manage:

– collecting facts from cloud and on-prem sources;

– building distributed graph models on top of configuration and runtime data;

– creating domain- and task-specific “slices” of the model to support day-to-day operations and automation;

– sharing knowledge, practices, and policies via exchangeable fragments of the knowledge graph.

### Cloud Native at the Far(m) Edge: Running Kubernetes and AI on Tractors
Speakers: Mauro Morales, Jordan Karapanagiotis
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/UYXXAQ/
How do you take the best of cloud-native beyond the data center, to empower farmers in the field?

Aurea Imaging powers precision agriculture by running AI inference directly on devices mounted on tractors. Using onboard sensors, cameras, and GPUs, these devices analyze trees in real time to optimize spraying and reduce waste. But getting cloud-native workloads to run reliably on the far edge, in environments that are often air-gapped, disconnected, and physically demanding, requires more than just containerizing code.

Together with the CNCF Sandbox project Kairos, Aurea Imaging built a production platform where devices boot from container images: an immutable, reproducible system running K3s and managing its lifecycle “as code.” This approach replaces traditional embedded provisioning with declarative configuration, image-based deployment, and seamless OTA updates, bringing the power of cloud-native and AI beyond the data center.

### ASO(cial) Superpowers: Streamlined App Deployments with Azure Service Operator
Speakers: Daniel Paulus
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/FCTQXS/
When every dev team rolls out their own infrastructure dependencies you know what is coming: chaos. In one of my recent projects I ended up with hundreds of Terraform solutions, sometimes even split across different teams working on the same app. It worked, but it was not pretty.

That is when I gave the teams some ASO powers. With the Azure Service Operator they could deploy their application dependencies in the same way they already deploy their containers. Suddenly things looked a lot cleaner, more consistent and easier to manage.

In this session I will share what that looked like in practice, the lessons learned, the benefits and of course a demo. You will walk away with concrete ideas on how to cut down Terraform sprawl, make life easier for your developers and bring some order back into your deployments.

## 2026-02-02 — B.1.011

### Getting started with CI/CD using Forgejo Actions and why this is important AF
Speakers: Jeroen Baten
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/PQUPEQ/
Continuous Integration and Continuous Delivery (CI/CD) have become essential practices for modern software development—but many teams still rely on centralized, proprietary platforms like GitHub or GitLab for all their build automation. In this talk, we introduce Forgejo Actions, a powerful, self-hostable CI/CD solution that is largely compatible with GitHub Actions. This makes it incredibly easy for beginners and experienced developers alike to get started with automated testing and delivery pipelines—without surrendering control of their code or infrastructure.

We will walk through the core concepts of Forgejo CI/CD: the Forgejo server, the Docker-powered runners, workflow files, and practical examples to get newcomers up and running. In the second half, we zoom out and explain why this matters "AF": digital autonomy, reducing vendor lock-in, and avoiding dependency on increasingly centralized platforms. Migrating from GitHub Actions to Forgejo Actions is often surprisingly painless, giving developers the freedom to host their own pipelines while still syncing code to major platforms when needed.

Finally, we'll explore how Forgejo connects to the broader ecosystem—most notably Codeberg, the fast-growing European non-profit hosting platform with 200,000+ repositories and over 1,200 paying members (membership €24/year; €12 discounted). Together, Forgejo and Codeberg demonstrate that modern CI/CD doesn’t need to depend on Big Tech.

Attendees will walk away with a clear understanding of how to start implementing Forgejo-based CI/CD workflows today—and why doing so is strategically vital for long-term developer independence.

Links:
-  Forgejo: https://forgejo.org
- Codeberg: https://codeberg.org
- Codeberg e.V.: https://codeberg.org/Codeberg/org
- Forgejo Actions docs: https://forgejo.org/docs/latest/admin/actions/
- Submitter’s involvement (LibrePlan CI/CD work): 
-- https://github.com/LibrePlan/libreplan
-- https://www.libreplan.dev/ Getting started with CI/CD using Forgejo Actions — and why this is important AF

Want to get started with CI/CD without locking your entire development workflow into GitHub or GitLab? Curious how to run modern pipelines on your own infrastructure while still keeping full compatibility with the tools you already know? In this session, you’ll discover how Forgejo Actions makes all of this not only possible — but surprisingly easy.

We’ll walk you through the basics of setting up CI/CD with Forgejo, a fully open-source Git server that comes with a GitHub-compatible Actions engine. You’ll learn how the server and runners work, how to write your first workflow, and how existing GitHub Actions pipelines can be migrated with minimal effort.

But this talk goes beyond the technical “how”. We’ll also look at the “why”, and why it’s important AF: digital autonomy, avoiding vendor lock-in, maintaining control over your code, your builds, and your infrastructure. You’ll see how Forgejo fits into a growing ecosystem of community-driven tooling — including Codeberg, the rapidly expanding European hosting platform with 200k+ repositories.

Whether you’re a beginner taking your first steps into automated testing and delivery, or a seasoned developer questioning your dependence on centralized services, this talk will give you the tools — and the motivation — to stand on your own CI/CD legs.

Join us and learn how to build, test, and deploy with confidence… on your terms.

### CI/CD Observability, Metrics and DORA: Shifting Left and Cleaning Up!
Speakers: Peter Souter
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/98XRKP/
Most teams have observability and monitoring strategies to fix problems with their applications in production, but what if the issue is actually earlier in the delivery process? 

You might have CI/CD systems to test and deploy your applications, but what happens when your CI/CD tools themselves become the issue? 

Without granular visibility into the performance of your pre-production testing and deployment pipelines, organizations often experience development outages due to slow builds or increases in failing or flaky tests. 

In this session, Peter Souter will talk about how to fix that, move observability left, and bring observability into your pipelines and test runs. He’ll go through tracking key CI/CD metrics over time, catching those pesky flaky tests, and building out a DORA-based culture to improve your pre-production processes.

### Event-Driven CI/CD Observability: Infrastructure as Observable Events
Speakers: David Bernard
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/M993WU/
Modern infrastructure teams manage CI/CD pipelines across diverse tools but lack standardized observability, creating blind spots in deployment workflows.

This talk demonstrates event-driven observability using CDEvents, a vendor-neutral specification for continuous delivery events. See real deployment data visualized in Grafana: deployment frequency, promotion delays between environments, and pipeline duration trends—collected from GitHub Actions, artifact registries, and ArgoCD.

Learn the open source architecture (CDviz collector + PostgreSQL/TimescaleDB + Grafana), incremental adoption path, and how standardized events enable future automation—providing pipeline observability without vendor lock-in. Attendees will learn:
- Why CI/CD observability is fragmented across heterogeneous tools
- How CDEvents provides a standardization layer for delivery events
- Technical architecture: event collector, time-series storage, visualization stack
- Practical steps to add observability incrementally (instrument CI → registries → CD tools)
- How standardized events unlock automation possibilities beyond observability

The presentation shows Grafana dashboards with real deployment metrics, demonstrating what teams can observe once CDEvents is integrated into their infrastructure.

Open source technologies: CDEvents, CDviz, PostgreSQL with TimescaleDB, Grafana.

### Beyond SHA Pinning: Security for CI/CD Pipelines
Speakers: Andoni Alonso, Paco Sanchez
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/E9ANZ8/
Recent months have seen several supply chain attacks, such as the `tj-actions` incident. Is your CI/CD pipeline prepared to defend against them?

Pipelines have privileged access to your code, infrastructure, and secrets, making them a critical component of any modern software development lifecycle (SDLC).

In this talk, we will show practical strategies to secure your pipeline, covering both common vulnerabilities and lesser-known attack vectors. We will go beyond basic recommendations like pinning actions by SHA, and explore how misconfigured repositories can lead to remote code execution (RCE) simply by opening a pull request.

Attendees will leave with actionable steps and a deeper understanding of how to fortify their pipelines against real-world threats.

### CI Testing with Beaker
Speakers: Steven Pritchard
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/HQLRFF/
Modern Puppet module development requires more than just local Vagrant tests. In this talk, we’ll explore Beaker providers like **beaker-kubevirt** and **beaker-google**, and show how they make it possible to test modules in Kubernetes and cloud environments. We’ll also demonstrate how to integrate Beaker tests into CI pipelines using GitLab CI and GitHub Actions, making acceptance testing easier and more reliable. We’ll dive into real-world workflows that combine Beaker with modern CI/CD pipelines. Attendees will see how to switch between providers, run tests across multiple platforms, and use CI to validate modules automatically. Along the way, we’ll share insights from our own development practices and product testing, with demos that show how to bring Beaker into your CI pipeline today.

## 2026-02-02 — B.1.0.14

### Composing systems in an automated way with Ansible, Podman, and bootc
Speakers: Fabio Alessandro "Fale" Locati
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/KU78JX/
As organizations increasingly adopt containerization, Kubernetes has become the de facto standard for orchestrating clusters. However, for many teams, the complexity and operational overhead of managing a Kubernetes environment can be daunting.
In this talk, we'll explore a practical alternative built on open standards and simple tools: using:
* Ansible for automation
* Podman for container management
* bootc for the operating system.
While Ansible and Podman are very established technologies, bootc is an emerging technology that reimagines how systems are built and updated by transforming container images into fully bootable, atomic operating systems. It brings the simplicity, consistency, and automation of container workflows all the way down to the OS layer.
You'll learn how to use Ansible to define and manage containerized applications and services, leverage Podman's daemonless architecture for secure deployments, and then go one step further by using bootc to build and manage image-based operating systems directly from your container definitions.
We'll wrap up with a live demo creating podman containers using Ansible on a bootc system, showing how these tools together can deliver lightweight, reproducible, and maintainable infrastructure in a simple way.

### Debugging Playbooks Made Easy: The Ansible Playbook Debugger
Speakers: Jure Medvesek
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/AJAMAN/
The Ansible community lacks official debugging tools. In this session, I’ll present our reference implementation of an Ansible Playbook Debugger that allows you to inspect variables without relying on 'printf' debugging. 

This debugger is useful in many scenarios, such as: 

Retrieving structured results from tasks 

Evaluating Jinja expressions or real variables and facts at runtime 

Listing Ansible facts 

Checking actual FQCN used when a short name was used in a playbook 

In this session, I’ll showcase practical use cases where this tool has proven valuable, including live demos that highlight how it simplifies development, inspects variables, and improves visibility into your playbooks. Ansible Playbook Debugger is open-source under the MIT license, with the code is available in the repository here: https://gitlab.com/xlab-steampunk/steampunk-spotter-client/spotter-ansible-playbook-debugger

### Don't Fear the Jinja - Beyond the Handlebars with Ansible
Speakers: Matt Davis
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/QXPYAU/
Jinja's tricky. Few things can so quickly evoke chutzpah, fear, and regret in the soul of a playbook author; often all at once! Join Ansible Core architect nitzmahone for a light-hearted exploration of some Jinja anti-patterns, and a dive into powerful new Jinja features enabled in recent Ansible Core releases. Learn to confidently embed handlebars in your automation without going "over the handlebars".

### Behind The Scene- How We Ship Ansible Network Collections
Speakers: Chetna Agrawal
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/QGSZTT/
How do you transform dozens of ansible network collections into predictable, “always-green” releases? We will share how the Ansible Networking team standardizes structure, testing, and release hygiene across collections, so users get fewer surprises and faster fixes. We will cover our CI gates (sanity/unit/integration), Galaxy readiness checks, branch strategy, and what “Done” means before publishing. Managing a diverse set of Ansible Network collections from multiple vendors requires a disciplined approach to release management. This talk explores how the Ansible Networking team achieves consistent, reliable releases at scale. We will break down our CI gates, branching model, testing standards, and release criteria that keep our collections high-quality and production-ready.
We’ll take you through the key strategies and tools we use, including:

 Best Practices: How to standardize development and release processes across multiple collections.
CI/CD Strategy: Leverage sanity, unit, and integration tests to ensure high-quality, stable releases.
Automation Hub Readiness: Define clear criteria for collection readiness before publishing.
Branch Strategy: Implement a disciplined branching model to simplify releases and development parallelism.
Definition of Done: How to ensure quality by establishing clear, measurable release criteria.

Outcomes-

1.quality workflows that ensure smooth, predictable releases for users and partners
2.Take home a repeatable release checklist you can copy

### ansible-docsmith - ultimate tool to document ansible roles
Speakers: Kirill Satarin
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/UJHJE7/
Maintaining accurate, up-to-date documentation for Ansible roles is a persistent challenge when maintaining ansible roles. ansible-docsmith solves this problem by automating documentation generation from a single source of truth - argument_specs.yml file. 

  In this talk, we'll explore ansible-docsmith and how to use it to forget about ever updating the readme.md file for the role, but always keeping it up to date. 

  - Using argument_specs.yml as the single source of truth for ansible role readme.md file
  - Using ansible-docsmith in CI/CD: automation pipelines and pre-commit hooks, making documentation updates effortless
  - Available customization options in ansible-docsmith: how to use Jinja2 templates to generate readme.md according to your specific documentation standards
  - Compare ansible-docsmith with ansibull-docs - pros and cons, use case scenarios

https://github.com/foundata/ansible-docsmith Attendees will gain hands-on familiarity with:
  - Installing and configuring ansible-docsmith in their environment
  - Setting up documentation markers in README files
  - Using ansible-docsmith generate and validate commands effectively
  - Integrating the tool into CI/CD pipelines and Git hooks
  - Creating custom Jinja2 templates for specialized documentation needs
  - Best practices for maintaining argument_specs.yml as documentation source

 Whether you maintain a handful of roles or manage entire collections, you'll learn how to save time, reduce errors, and keep your role documentation perfectly synchronized with your code.

  Target Audience: Ansible users, DevOps engineers, infrastructure automation practitioners

## 2026-02-02 — B.1.015

### Mopping up the mess after a rug pull
Speakers: Ben Ford
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/GDFPNH/
I'm sure I don't have to describe the chaos inflicted on the Puppet community when Perforce decided to sequester the source away. Open Source Puppet is no more and many of us have been suddenly thrust into the roles of managing a large group maintaining a large, mature, and very hairy bit of software.

Let's take a no-holds-barred stroll through the story of this last year. I'll share some of the things that worked really well, and a whole lot of things that haven't. We'll talk about some tech challenges that were smaller hills to climb than we thought, and some that turned out to be real bears. I'll talk a bit about the biggest challenge we've faced. (Hint, it's people, time, and communication. It's always people, time and communication.)

### One year OpenVoxProject
Speakers: Tim Meusel
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/XAHTHZ/
At Config Management Camp 2025 we started the OpenVoxProject.
In the past year we worked on open source successors for Puppet Agent, Server, DB and Bolt.
We secured funding, scaled our CI infrastructure and organized our first own conference in Nürnberg!

Let us make a recap about everything we achived.
Also I want to provide an overview about upcoming topics and possible ways to engage and support the community!

* The slides are [available online](https://bastelfreak.de/cfgmgmtcamp2026/openvox.html#1)
* I also have a collection of my other talks at [github.com/bastelfreak/talks](https://github.com/bastelfreak/talks)
* I will demo the OpenBolt integration into Foreman [in the afternoon] in the Foreman Dev room(https://cfp.cfgmgmtcamp.org/ghent2026/talk/DVS97G/)

### Managing a mixed landscape of Linux and Windows servers with Puppet - our dos and don'ts
Speakers: Markus Spanner-Denzer
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/7BXZNX/
At noris network, a German IT service provider, we have a long history of using OpenSource Puppet (or now OpenVox) for configuration management of Linux servers which we operate for our customers. From time to time, we set up dedicated Puppet setups for individual customers with special security requirements. While these customers usually have a mix of Linux and Windows servers, we initially used Puppet only on the Linux servers and managed Windows servers in different ways. About 4 years ago, we started to use Puppet on Windows servers as well. Our goal was to harmonize configuration and operating processes of both operating systems.

This talk is about our experiences with puppet in a mixed Linux/Windows environment, both from the technical and the organizational perspective.
The technical part include e.g. the structure of git repos, our hiera data tree, and module selection. The organizational aspect is the cooperation of Linux engineers with a deep puppet knowledge and Windows engineers new to puppet.

What works well for us? What did not?

### Beyond Basics: Hiera Hacks for Fun!
Speakers: Benedikt Trefzer
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/BJKHMX/
Managing advanced Hiera data can be tough. Nevertheless, I will share two additional techniques for even more headaches:
-   Use dynamic hierarchy paths with scoped Puppet variables to streamline services
-   Incorporate Puppet functions in Hiera lookups for powerful data retrieval.

See (im)practical hacks that can simplify complex OpenVox configurations and make your automation more fun! I expect the audience to be familiar with the Puppet language and the structure and functionality of Hiera.

### Using containers in openvox environments
Speakers: Robert Waffen
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/EQ8VWB/
“The use of containers in a Puppet environment offers numerous advantages. Containers enable efficient deployment of the Puppet infrastructure, accelerate testing cycles with VoxBox, and automate software updates through the integration of Renovate with GitLab/GitHub. The combination of Semantic Release and containers also simplifies versioning and changelog creation of Puppet modules. Thus, containers contribute significantly to increased efficiency and automation in this environment.”

## 2026-02-02 — B.1.017

### Ansible for Beginners: What I Wish Someone Had Told Me Before I Learned the Hard Way
Speakers: James Freeman
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/X8VAJV/
Getting started with Ansible is exciting and rapidly improves your productivity. However I've revisited playbooks that I wrote almost a decade ago and found the code today to be almost unmaintainable. Should I have created a role instead of a playbook? Was it really a good idea to copy-paste between projects? (Spoiler: yes, but we've all done it somewhere!) This talk shares the practical knowledge I've gathered over years of working with Ansible—the kind of insights that only come from actually using it in production, making mistakes, and finding better approaches. In this talk, I'll share what worked, what didn't, and why—so you can build automation you'll still be happy with months down the line. You'll leave with both the fundamentals and the perspective that usually takes years to develop.

### Building a self-contained, zero-dependency deployment with Ansible
Speakers: Daniel Podwysocki
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/WRKSNK/
This talk will show you how to finally solve bootstrapping your infrastructure/laptop/coffee machine anywhere.


I will show you how I've solved packaging Ansible into a self-contained, offline-capable installer that can run anywhere, with zero dependencies - no docker or other OCI runtime, no python, just a minimal linux box. Since I started using Ansible to manage my infrastructure 10 years ago, I had always grappled with the problem of bootstrapping - that is getting the first node in the environment ready. An ideal setup I always wanted would let me deploy to any Linux-based environment without having to wrangle dependencies or install anything extra such as docker on the first node.

As luck would have it, I recently got to work through a real-world case of handling such a deployment and the customer I did it for has open-sourced the solution! The example we'll be able to look at is a Linux-based container platform that we'll install with a single command, with no dependencies needed on the host whatsoever - and all powered by Ansible. 

After this talk, you will:

- have an understanding of how you can leverage Linux internals to contain your dependencies without the extra work of installing a container runtime (no docker needed!)
- you'll see how a real-world platform integrates Ansible to bootstrap and expand a full k3s cluster
- you'll see a single command provision a full platform in 1-3 minutes

The day of the talk, the presentation slides will be made public here: https://github.com/danielpodwysocki/self-contained-ansible-demo

### Building CI/CD Pipelines for your Ansible code
Speakers: Ottavia Balducci
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/W3GX3U/
Ansible has become indispensable for modern configuration management. Once you start writing Ansible code, the first thing that you should do is to put it under version control. From there, a whole new world of automation possibilities through CI/CD pipelines opens up.

In this session, we will explore how to leverage CI/CD pipelines to supercharge your Ansible repositories. Using GitLab CI/CD as the primary example, we will walk through several real-life scenarios, each illustrated with a live demo. We will start with the simple yet impactful step of adding automatic linting. We will then move on to more advanced use cases such as automatically building collections and execution environments, generating CHANGELOGs with antsibull-changelog, and performing automated testing with Molecule.

Whether you are just starting with Ansible or already managing complex automation frameworks, this talk will offer practical examples and ideas to take your Ansible code management to the next level. Code examples can be found here: https://github.com/OttaviaB/cfgmgmt_camp_2026 .

### Using antsibull-nox to test your Ansible collection
Speakers: Felix Fontein
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CSS3XT/
Antsibull-nox is a extension for nox that makes it easy to run various tests and other testing tools for Ansible collections. In this talk, I want to present some background on why I created antsibull-nox, why I chose nox (instead of, say, tox), and demonstrate on how you can use antsibull-nox to test your Ansible collections. This talk is aimed at collection maintainers, but also at contributors who want to know more about collection testing. You will get a (historic) overview of existing collection testing tools, starting with ansible-test, learn of the challenges these tools pose to collection testing and collection CI, and how this led to the development of antsibull-nox - and, most importantly, how antsibull-nox tries to address these challenges.

Talk slides: https://github.com/felixfontein/cfgmgmtcamp-2026-talk
Demo repository: https://github.com/felixfontein/cfgmgmtcamp-2026-demo

## 2026-02-02 — B.1.0.29

### Software Distribution and Lifecycle Management With Katello
Speakers: Ian Ballou
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/UXRHYC/
Katello adds a suite of content management tools to Foreman. Content mirroring & distribution, patching, lifecycle management, and access management are all included. This presentation will teach you how to get started with a Katello environment along with the conceptual knowledge necessary to start applying it into your computing environment. Features new to the past few releases, like bootable containers and OCI flatpaks, will be discussed as well. This presentation will focus first on Katello basics: repositories, lifecycle environments, and content views. We'll discuss concepts that apply to each of the supported content types: “yum” (RPMs, module streams, etc), debian, container, python, ansible-collection, ostree, and generic files.

Afterwards, we'll discuss how Katello can help you get your synced content deployed onto machines. We'll cover topics like host registration, patching, and kickstart provisioning with synced content. Smart proxies will be discussed as well in case the content needs to be distributed to machines across different geographical regions.

At the end, I will show how a Katello user could tie the presentation materials together to create a production-ready environment. The demo will cover scenarios like quickly applying emergency patches via incremental update, caching content on the local network, and automating software delivery.

### Integrating Pulp with Build Systems
Speakers: Dennis Kliban
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/KAKLSD/
This talk will examine some of the challenges I encountered while helping various teams at Red Hat integrate their CI/CD pipelines with Pulp. The solutions to these problems required changes in client tooling, Pulp's REST API, and the Tasking System architecture. As we examine each problem we will take a look at Bash and Python scripts that help upload and organize content that is produced by multiple different build systems at Red Hat. I will also hightlight some of the new features that were inspired by the problems we experienced over the last year.

### Client tooling to integrate with Pulp
Speakers: Matthias Dellweg
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/BLCULB/
In this talk we will discuss client tools like ansible modules or cli to interact with your repositories managed on a Pulp server. We will focus on the technical aspect of how they are similar and why we build them on a library called pulp_glue.

### The Future of Bootable Containers in Katello
Speakers: Ian Ballou
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/XGAVZK/
Bootable container images and image mode machines form a new concept that the Enterprise Linux world is still deciding how to use. Katello, the content management plugin to Foreman, has already begun making decisions about how systems administrators would like to manage image mode machines. Come to this talk to learn about bootable container images, learn how Katello can help keep your image mode machines up to date, and to discuss how the future of image mode machine management should look. This presentation will provide users with the background necessary to participate in a Foreman & Katello themed discussion about our present and future bootable containers integration. Ideas about the future will be proposed, and the audience will have a chance to share their experiences and thoughts. The suggestions will be noted for inclusion in future Foreman community RFC posts.

Depending on where the discussion goes, there may also be:
- A demo of the current bootable containers integration with a technical deep-dive
- A discussion about provisioning bootable containers via Foreman
- An overview of Katello’s container registry, which can host bootable container images

### What Is New in Pulp Python
Speakers: Jitka Halova
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/YX8ZTC/
Curious about what is new in Pulp Python? This talk highlights recent features with a focus on their practical application. In 2025, the Pulp Python plugin gained significant attention and received several new features and refinements. Key updates include support for new core metadata (with the ability to fix them), a JSON-based Simple API, synchronous uploads, improved pull-through caching and data serving, and newly implemented vulnerability reports. In this session, we will explore some of these changes in detail, explain how they work, and show how you can use them to streamline your workflow and improve security.

### Upgrading Fedora's Monitoring - a real Tech Debt story
Speakers: Greg Sutcliffe
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/TMVAMQ/
Over the last year I've been working on migrating Fedora's aging Nagios & Collectd stack to Zabbix, using Ansible to deliver the full Zabbix config - no UI-side config needed. 

In this talk, we'll explore:
- Why we moved to Zabbix over other tools
- The perils of a separate monitoring role, and how to instead put your application monitoring in your application roles
- The tech debt of figuring out how & why checks exist in your old stack... is "this one" even needed any more?
- The people side of tech debt work - practicalities for helping the people around you to get on board when "the current thing still works, doesn't it?"

It's been an interesting journey getting this project over the line, and while there might not be any shiny new technologies to come from it, I think there are lessons worth sharing. We all have tech debt, after all.

## 2026-02-02 — B.1.031

### Foreman Community Updates
Speakers: Shimon Shtein
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/KVFHMX/
Join us for the annual Foreman Community Updates to explore the key developments, discussions, and long-term efforts shaping the Foreman ecosystem over the past year.
We’ll cover major feature work, including the new Job Invocation Detail page, the RFC on Recurring Logic Redesign, and improvements to testing plugins from Foreman Core. On the Katello side, beyond the headline features in the Katello 4.19 release, we are introducing enhancements to Image Mode and Flatpak support. We’re actively seeking user feedback on the use of Image Mode (known upstream as bootable containers) with Foreman & Katello, as well as on our container registry experience.
A significant multi-year effort is underway to modernize the entire Foreman UI to PatternFly 5. This will be a long process (roughly two years) and users can expect many UI changes throughout that period.
We’ll also highlight improvements to the documentation site, such as clearer navigation, new version banners ("Pre-release", "Unsupported", reworked guide/flavor navigation, and continued plans to update documentation around the containerization work. As containerization progresses, especially through the emerging foremanctl tooling, we anticipate extensive documentation updates, including a future streamlined installation guide. For now, only the foremanctl quickstart guide is published.
We’ll review documentation updates including a restructured Provisioning Hosts guide and new OpenSCAP content for non-RHEL clients.
We will also touch on recent community activities, such as the Foreman + AI meetup held in Brno. While AI isn’t a major community focus yet, we plan to share the event recordings soon.
This session is your chance to stay informed, give feedback, and help influence the direction of Foreman’s next generation.

### Risk and Vulnerability Management on Premise in Foreman
Speakers: Viliam Krizan
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/KSY7P9/
Red Hat Lightspeed offers predictive analytics and risk assessment in a hosted environment. To extend this value, an initiative is underway to integrate core capabilities—such as Advisor (proactive risk identification) and Vulnerability (security management for RHEL systems)—into self-managed Foreman (with Katello) environments, leveraging open source collaboration with the Foreman project.

This presentation will detail bringing these capabilities to on-premises users, covering the project's history, open source strategy, high-level architecture, and roadmap. Attendees will understand the initial services' function and integration. The talk aims to foster engagement, gather feedback, and explore contribution opportunities within the Foreman community.

### Foreman Plugin to Provision Hosts via OpenTofu for Diverse Compute and Virtualization Platforms
Speakers: Manisha Singhal, Markus Bucher
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/TQFALN/
Foreman provides framework for host provisioning and lifecycle management, but its integration with different compute resources remains limited. We are working on developing a new Foreman plugin for host provisioning via OpenTofu, enabling administrators to leverage OpenTofu’s extensive provider ecosystem directly within Foreman. The plugin abstracts OpenTofu operations to provision hosts across diverse compute environments while maintaining Foreman’s familiar management interface. Designed with extensibility in mind, it supports easy adaptation for new resource types and providers. The integration brings together Foreman’s orchestration and OpenTofu’s declarative model to simplify and automate provisioning. The talk discusses the plugin’s architecture, implementation details, and use cases demonstrating improved scalability and flexibility in diverse compute and virtualization environments.

### Foreman - A Swiss Army Knife for multiple systems administration
Speakers: Shimon Shtein
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CZKHZN/
An introduction session into the Foreman project - one tool to manage the whole lifecycle of your servers fleet from a web-based UI. The Foreman project is a tool that is used to manage the whole lifecycle of server fleets. From provisioning through configuration management and content management to connection to online health and security recommendations services.
We will talk about the various aspects of managing hosts using the Foreman and how to get started with it in your organization.

### Agama? How SUSE SLES16 Provisioning works with Foreman.
Speakers: Bernhard Suttner
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/VCTJTA/
This talk demonstrates how to deploy SUSE Linux Enterprise Server 16 (SLES16) hosts using Foreman, streamlining provisioning and configuration processes. With SLES16 replacing YaST with Agama, additional adjustments are required for host provisioning in Foreman. The session also highlights the integration with the SUSE Customer Center (SCC) for seamless access to official SLES repositories.

### Bringing OpenBolt into Foreman
Speakers: Tim Meusel
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/DVS97G/
[OpenBolt](https://github.com/OpenVoxProject/openbolt) is a CLI application from the [OpenVoxProject](https://voxpupuli.org/openvox/). It 
provides different ways to run your beloved sysadmin scripts with proper 
guardrails and it makes it easy to glue them together into Plans. For 
years, people wanted to have a Web UI, besides the CLI, to run the 
various tasks and plans. We now added a Foreman plugin, which enables 
people to run everything via the Web UI or the Foreman API!

* What is OpenBolt and where does it come from?
* What are Tasks?
* What are Plans?
* How does it fit into the Foreman ecosystem?

In this talk I would like to answer those questions showcase what OpenBolt is and the benefits it provides, and also do a live demo.

* [Foreman OpenBolt Plugin sourcecode](https://github.com/overlookinfra/foreman_openbolt?tab=readme-ov-file#foreman-openbolt)
* [Foreman Smartproxy OpenBolt Plugin sourcecode](https://github.com/overlookinfra/smart_proxy_openbolt?tab=readme-ov-file#smart-proxy---openbolt)

The slides are [available online](https://bastelfreak.de/cfgmgmtcamp2026/openbolt.html#1). A collection of all my talks is at [github.com/bastelfreak/talks](https://github.com/bastelfreak/talks).

## 2026-02-02 — B.1.036

### Nix at work ? How ? Why ? How about you ?
Speakers: Pol Dellaiera
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/N3NCAJ/
In an age where GitOps and Configuration as Code are redefining how we build and operate systems, reproducibility has become essential. Yet, while we often talk about Infrastructure as Code, the developer experience is still too often left behind.

In this talk, we’ll explore how to extend the "... as Code" philosophy to the entire software development lifecycle. From Development Environment as Code, through custom package builds, to full Infrastructure as Code, using the Nix ecosystem as the backbone.

We will walk step by step through the process of evolving a trivial Nix setup into a fully reproducible, modular, and GitOps-friendly workflow:

* Starting from a traditional `shell.nix`,
* Transitioning to a declarative `flake.nix` setup,
* Leveraging a flake framework for modular design,
* Defining multiple development shells (for NodeJS, Go, Python, Java, etc.),
* Building wrappers to ensure custom and consistent environment behaviour.
* Building full operating system and deploy them on a real machine or simply testing them in a virtual machine

The session will be highly practical and supported by live demos.

All examples will be based on an open-source tutorial I have started to develop. Attendees will be able to reproduce every step afterwards and apply the same ideas directly in their own environments or workplaces. Designing the repository for educational purposes has been a challenge in itself: each commit is tagged and associated with a dedicated branch, illustrating the evolution of the project step by step. Every new feature or idea comes with its own commit and branch, making it easy to compare changes and understand the reasoning behind each decision. You could even call it "Tutorial as Code": a fully reproducible learning experience where every change tells a story.

By the end of the presentation, you’ll see how Nix enables a seamless continuum from developer laptop to production system, empowering teams to tame complexity, ensure reproducibility, and make their workflows truly "Everything as Code", a real GitOps approach.

Whether you’re a DevOps engineer, software engineer, or curious technologist, this session will provide you with concrete techniques and design patterns to strengthen your GitOps practice and simplify your daily workflow.

### Reactive Nix: Enabling Functional Reactive Configuration with mgmt
Speakers: Jannik Höfler
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/LCHTBT/
Nix lets us define entire systems as pure functions - deterministic, reproducible, and immutable.
Once evaluated, though, these functions produce fixed values: snapshots in time of the desired state.

Functional Reactive Programming (FRP), as implemented in **mgmt**, extends this model.
In FRP, instead of yielding a fixed value, functions can return a *dynamic signal*: a value that evolves over time, responding to other changes in the system.

**Reactive Nix** explores how these two paradigms meet:
What if Nix's purely functional configurations could describe *continuous systems* - systems which stay declarative but react automatically as their dependencies change? Nix models derivations as pure mathematical functions:

```go
system = f(configuration)
```

Each build yields a fixed, reproducible output.
But between builds that output is static - it cannot express time or change.

Functional Reactive Programming generalizes this idea:

```go
system(t) = f(configuration, environment(t))
```

Here, the configuration remains pure, yet depends on signals that evolve continuously.
Despite its mathematical elegance, Nix as we use it today produces fixed values.
The world may change, but the configuration cannot react.

**mgmt's FRP runtime** provides a concrete realization of this idea: it observes the environment, reacts, and converges continuously to the declared state.

The [**rx.nix (Reactive Nix)** project](https://github.com/karpfediem/rx.nix) explores what happens when Nix's purely functional configuration model meets mgmt's continuous evaluation.
By treating Nix outputs as *functions over time* (not as fixed values), we can imagine systems that remain declarative, reproducible, and yet perpetually aligned with reality.


We will discuss:
- Current struggles of NixOS and the limits of static outputs
- Building intuition for Functional Reactive Programming
- How FRP can complement Nix
- Possibilities we gain by combining Nix with mgmt

### Overengineering my personal infrastructure with NixOS
Speakers: Lander Van den Bulcke
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/A88MRQ/
In this talk I will go over how I set up my personal infrastructure using Nix. I will cover how I manage my hypervisors and VMs using microvm.nix, how I set up advanced networking (vpn tunnels, bgp, connection to DN42, ...), how I monitor everything and will share tips and tricks I discovered along the way. Topics include:

- Remote hypervisor installation using nixos-anywhere
- Remote disk unlocking using SSH during initrd phase
- Using impermanence and an ephemeral root volume
- Managing VMs using microvm.nix
- Configuring Wireguard and GENEVE tunnels
- Configuring Bird to connect to DN42, an experimental VPN network where you can experiment with things like BGP (https://dn42.dev)
- Automating configuration of nameservers
- Automating Prometheus scrape target configuration

### Reproducible C++ Development Environments with Nix
Speakers: Wout Swinkels
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/H3UXV8/
This talk introduces how Nix-based tools (nix-shell, devenv, and flox) can create reproducible, portable, and team-friendly C++ development environments. Through practical examples, we’ll see how each of these tools work and help eliminate “It Works On My Machine” problems. Modern C++ development often demands consistent toolchains, reproducible builds, and seamless onboarding, goals that traditional environment-setup methods struggle to meet. In this talk, we explore how Nix and related tools can transform the way you manage C++ development environments. We begin with nix-shell, examining how it provides fully reproducible, declarative build and runtime environments without polluting your system. From there, we introduce devenv, a higher-level workflow tool built on Nix that simplifies environment configuration for teams, integrates services, and improves day-to-day developer experience. Finally, we look at flox, a more user-friendly and collaborative approach to managing Nix-based environments across machines and teams. Through practical examples and comparisons, you’ll learn how these tools help eliminate “It Works On My Machine” problems.

## 2026-02-02 — B.2.015

### Building an Infrastructure Automation Platform using Platform Engineering principles
Speakers: Niklas Werker
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/8VCRHU/
Nowadays, everybody seems to be talking about Platform Engineering. The world of software development and cloud native technologies have been flooded with new tools and frameworks under the label of Platform Engineering. This talk aims to unpack these technologies by exploring their underlying principles and addressing the following questions:

- What is Platform Engineering?
- What are the core principles that define Platform Engineering and differentiate it from traditional DevOps?
- How do Infrastructure as Code (IaC) and Configuration Management interplay with Platform Engineering?
- Can we build platforms tailored to the needs of infrastructure automation developers and how would they look like?

The session concludes with a live demo of an Infrastructure Automation Platform that combines the following technologies:
- Backstage
- Ansible
- HashiCorp Vault
- GitLab
- Eclipse Che

This demonstration showcases a practical approach to architecting, building and maintaining an Infrastructure Automation Platform - an approach that can be adapted to platforms composed out of other tech stacks as well. Finally, we will take a glimpse in the future of possible platform capabilities and how they might reshape the way we collaborate.

### Use Best-in-Class Tools for End-to-End Automation
Speakers: Vincent  Seynhaeve
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/RQUJBF/
Ansible, Terraform, OpenTofu: Choosing between one of these tools becomes a dilemma when teams have to automate their IT environment.

Like many community members, we are also convinced by how these tools work together and their potential to automate and standardize infrastructure.

In this presentation, we'll explore different ways to take infrastructure-as-code to the next level and leverage an end-to-end automation flow.
The presentation will conclude with a live demo showcasing a concrete use case for integrating these tools. It has always been a struggle to make IaC and orchestration tools work together in a seamless way. If you had to do it a couple of years ago, you had to invest time creating and maintaining your own platform to make them work together.

Nowadays, thanks to platforms such as Ansible Automation Platform, you can easily create a workflow including Terraform/OpenTofu and Ansible to automate the entire lifecycle of your resources from a single entry point.

The code to build the demo environment is available in this repository https://github.com/RedHatBelux/AAP2_opentofu

### Growing a startup using ansible
Speakers: Johan Van de Wauw
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/8MGGNK/
[Fluves](https://www.fluves.com/) and [Marlinks](https://marlinks.com/) are two sister companies in Ghent focusing on monitoring water & energy infrastucture, both onshore and offshore mostly using fiber optic sensing.
I want to tell the story of how our infrastructure grow with the company, from our first ansible playbook almost 9 years ago to the company we are now with 30 employees and deployments at different critical infrastructure sites all around the world, and under scrutiny of audits such as ISO 27001.
Due to the high volume of data we gather (acoustic sensing can generate terabytes of data per day) and our own interests, we have been self-hosting most of our work, in a time before data sovereignty was a thing and the cloud was still all the hype.
Most of our own development is done in Python, deployments are done using Ansible and I'll touch which open source tools worked for us (amongst other proxmox, postgres, gitea, prometheus, grafana, restic) and how we deploy them, which problems we faced and solved and which ones we didn't.

Even though we are not an open source company, we have contributed back patches to many of the tools we use, and we maintain a number of libraries.

The session is meant to be highly interactive. I want to mention which difficulties we are facing, such as stricter rules on remote access, and hope to hear how others are handling this.

### Uyuni: connecting two distinct worlds of Salt and Ansible
Speakers: Victor Zhestkov, Pablo Suárez Hernández
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/9GEJXP/
There is a list conceptual differences between Salt and Ansible, but we want to provide some solutions to build a bridge between these two distinct worlds. Uyuni is the open-source configuration and infrastructure management solution for software-defined infrastructure, which could provide some advanced features to connect Salt and Ansible worlds togather by using Salt to trigger Ansible playbooks execution with Salt. There are some ideas how the Ansible integration can be extended, but what are the expectations of real users?

### Automating Config Deployment with NetBox
Speakers: Christopher Rössler
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/RLFAJQ/
At BCIX we have moved from writing switch configurations by hand to a mostly automated process centered around NetBox.

Previously, the information required for the network switch configurations has been scattered across different tools and locations:
- IXP Manager (an open-source management platform designed to facilitate the operations and administration of Internet Exchange Points (IXPs) developed by INEX)
- NetBox 
- existing device configurations.

This over time created inconsistencies. To solve this issue, we have come up with a four step plan:
 - Collecting Data in NetBox using ansible
 - Generating the configs with jinja2-templates
 - Compare and validate actual vs intended configurations
 - Deployment of the configs on the switches

This improved consistency across IXP Manager, NetBox and the switch configurations. Additionally this has enabled us to leverage NetBox for further automation tasks like preparing, announcing and doing Maintenances on the BCIX Peering Platform more efficiently.

## 2026-02-02 — B.3.0.13

### OpenTofu Track Kickoff
Speakers: Sebastian Stadil
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/J7EH3N/
Sebastian Stadil is a cofounder of OpenTofu and serves as the program chair for OpenTofu at Kubecon, part of the CNCF and Linux Foundation.

This short talk provides an update on the project, and presents the agenda for the day.

### OpenTofu Builds It, Ansible Configures It: Using the Right Tool for the Right Job
Speakers: James Freeman
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/RTUESF/
For years, I was asking myself the wrong question: "Terraform or Ansible?" As if infrastructure provisioning and configuration management were the same problem. Spoiler: they're not, and trying to make one tool do both jobs is why your infrastructure code is a mess. This talk is about the liberation of discovering that OpenTofu (the Terraform fork) excels at infrastructure provisioning while Ansible owns configuration management—and that they work beautifully together when you go with the flow and use each tool for exactly what it was designed for. You'll learn:

- Why declarative infrastructure provisioning (OpenTofu) and imperative configuration (Ansible) solve fundamentally different problems
- How to generate dynamic Ansible inventories directly from OpenTofu state
- Practical patterns: OpenTofu provisions the servers, creates the inventory, then hands off to Ansible for the "Day 2" configuration
- When to stop: knowing which tool should own which resources (hint: if you're using Ansible's cloud modules, you're probably doing it wrong)
- Real examples from production: building cloud infrastructure with OpenTofu and configuring it with Ansible in a clean, maintainable pipeline

You'll leave with a clearer mental model of the provisioning/configuration boundary, working code examples, and the confidence to tell your team "we're using both, and here's why that's correct."

### Debugging Slow Infrastructure Runs with OpenTelemetry in OpenTofu
Speakers: James humphries
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/YWH8NT/
Infrastructure-as-code runs are black boxes. When a deployment takes 20 minutes, operators have no visibility into what's actually slow: provider API calls,s tate operations, network latency, or something else entirely. Traditional logs show what happened, but not why it's slow.

This talk demonstrates how OpenTofu integrated native OpenTelemetry support to expose infrastructure deployment internals through distributed tracing. The speaker walks through real-world debugging scenarios where OTel traces revealed hidden bottlenecks such as slow provider downloads, inefficient state operations, and API throttling, previously all things that may be invisible in traditional logs.

### Q&A with the OpenTofu maintainers
Speakers: Sebastian Stadil
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/UQPK87/
Come listen of a panel of OpenTofu maintainers talk about their experience running the project and collaborating with the community.

>50% of the panel time will be dedicated to answering questions from the community, gathering feedback, and perhaps even sharing fun anecdotes from the journey.

## 2026-02-02 — B.3.0.32

### Kubernetes can be more than just APIs
Speakers: Marko Bevc
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/BW9SC3/
Kubernetes is often described as "just a bunch of APIs" - powerful, flexible, and notoriously opaque. But it doesn’t have to stay that way. In this talk, we’ll look at how tools like Headlamp can turn Kubernetes from a wall of YAML and kubectl output into something far more approachable and insightful.

We’ll explore how Headlamp provides a clean, extensible UI that surfaces real-time cluster state, RBAC insights, workloads, and events — without compromising on power or security. You’ll see how to deploy it safely, extend it for your team’s needs, and use it alongside existing tooling to improve developer experience and operational visibility.

If you’ve ever wished your cluster had a single dashboard that your teammates could actually use, this session with demos will show you how to make Kubernetes not just manageable, but genuinely user-friendly.

### CDK8s: unleash programming language power for correct and testable Kubernetes charts
Speakers: Benjamin Führmann
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/USPZHD/
Debugging Kubernetes YAML can be frustrating, especially when wrestling with missing line breaks or maintaining hundreds of lines of curly template brackets. Fortunately, there are alternative approaches to declaring complex infrastructures with more suitable programming languages! In this talk, I’ll present how CDK8s can be used to enhance your Infrastructure as Code organization and share valuable tips we gleaned during our migration journey within the Datadog Alerting team. Kubernetes manifests, traditionally written in plain YAML or templated with systems like Kustomize and Helm, presented significant challenges for Datadog's Alerting team. With hundreds of applications deployed constantly, these methods proved inefficient for expressing complex needs, leading to maintenance difficulties, a lack of out-of-the-box validation, and insufficient testing capabilities. The team often spent excessive time on development and debugging, even causing incidents due to templating errors and inadequate validation.

Our Automation team needed a solution to manage charts and system complexity across cloud providers, features, scale, and sharding. Adopting a programming language-based approach became essential. This would facilitate chart generation, enable robust testing, promote efficient code sharing, and offer an easier onboarding experience for developers. CDK8s provides precisely this solution: an open-source framework, renders Kubernetes manifests directly from languages like Javascript, Python, Java, and Go.

This presentation will introduce CDK8s concepts and showcase its practical application within the Datadog Alerting team. Attendees will gain insights into managing infrastructure complexity using CDK8s, drawing from our team's experience. We will detail our transition from Helm templates and propose reusable patterns for enhancing DevOps infrastructure declaration.

### Inspecting your Kubernetes cluster with eBPF and Inspektor Gadget
Speakers: Soham Chakraborty
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/FSWFQB/
Kubernetes is the de-facto container orchestration system. However debugging Kubernetes in production environment, is not straightfoward. That’s where the power of eBPF and Inspektor Gadget comes in, which allows to do real time, in-cluster debugging to find out root cause of an issue.

Inspektor Gadget leverages eBPF to instrument the Linux kernel dynamically, exposing valuable insights about what’s really happening inside Kubernetes cluster — all in real time and without requiring to install any sort of agent. In this talk, we will explore how we can use different gadgets from the Inspektor Gadget toolkit to find out things like:

TCP connections made by a pod

DNS requests

syscalls

traceloop - a flight recorder for syscalls
and others

This will be a practical talk, starting with an introduction of eBPF and going into the Inspektor Gadget suite. We will see different gadgets in action, and at the end, audience will be able to understand how to make their lives easier by using Inspektor Gadget to debug when there is a difficult problem. We will also learn how to capture the output in a much more user friendly manner, for parsing them later.

### It Doesn't Always Have to Be Caviar: Enterprise Alternatives and the Challenge of Default Stacks
Speakers: Gergely Szalay, Amir Zahirovic
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/R8TJ3F/
When onboarding a new enterprise client to the world of DevOps and Kubernetes, it’s tempting to deploy the usual, dominant tools. However, we introduced a twist: we strategically sought, tested, and implemented robust open-source alternatives.

This presentation chronicles our journey to build a highly available, production-ready environment without relying on the most common software defaults. We will detail the how—creating a foundation using tools like Podman instead of Docker, Gitea instead of GitLab, and implementing PostgreSQL with Timescale for critical, high-volume tasks.

Crucially, we explore the why. Why challenge the status quo? What are the true technical benefits, security gains, and cost advantages of these non-standard yet powerful combinations? Learn how we achieved reliability and enterprise-level functionality while avoiding "caviar" solutions, providing valuable lessons for any team looking to customize their technology stack.

### Simplifying Infrastructure Maintenance with Declarative Updates
Speakers: Vernin Olivier
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/GA93UM/
Managing infrastructure-related repositories can be repetitive and error-prone—keeping dependencies, configurations, and manifests up-to-date is a constant challenge. Updatecli offers a practical, declarative approach to automate these updates, making infrastructure maintenance safer, faster, and more predictable.

In this session, I’ll demonstrate how to use Updatecli in real-world scenarios:

Detecting and updating dependencies across multiple repositories.

Writing declarative update rules that are safe and repeatable.

Integrating Updatecli into CI/CD pipelines to automate maintenance.

Through a live demo, attendees will see how to turn tedious manual updates into automated workflows. You’ll leave with actionable knowledge to keep your infrastructure repositories current, compliant, and easier to manage—without adding complexity.

## 2026-02-02 — The Zone

### Social Event
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/U7RVYV/
Social event across the street

## 2026-02-03 — D.Aud

### Beyond Static Files: Dynamic Configurations for a Future-Proof World
Speakers: Marcel van Lohuizen, Roger Peppe
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/S93BW8/
Configuration management has long struggled to reconcile the stability of static definitions with the agility of dynamic environments. This traditional separation has led to fragmented tools, complex workflows, and costly outages.

Challenging the common view of configuration as a purely static entity, we will demonstrate how to seamlessly integrate static schemas and versioned configurations with the demands of dynamic components, such as policy enforcement, monitoring, and ephemeral configuration using CUE's logic-based approach to configuration. We show by means of real-life examples that this approach goes beyond mere templating, enabling the slicing and dicing of configuration from different sources and formats to enable cross-cutting functionality that adapts to evolving conditions.

### The Gilded Age of Open Source is over
Speakers: Joe Brockmeier
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/QV7JPB/
The first two decades of the 21st Century were a Gilded Age for open source, and the tech industry, with all that implies. That age is over, and open source is now entering a new era; the available resources for open source development are declining, with corporate layoffs, shifting priorities, the adoption of source-available licensing, and developer burnout all taking a toll. 

What comes now is uncertain; open source is here to stay, but in what form? Open source has enjoyed immense success during the first quarter (or so) of the 21st century. It has gone from a niche development model to a dominant part of the technology industry; it has enabled the rise of major tech companies that have, in turn, funded open source development and courted the favor of the open source community. 

However, the open source honeymoon seems to be over. Budgets have been slashed, entire teams of open source maintainers have been cut with little warning, and many companies are more interested in picking over the bones of open source repositories to feed large-language models than helping to fund open source maintenance. 

This talk will look at the history of open source's gilded age, examine its current state, and provide a glimpse into likely futures.

### Panel:  Souvereign Computing
Speakers: Walter Heck, Toshaan Bharvani, Kris Buytaert, Frank Louwers, Marcel Kornegoor, therojam, Koen de Jonge
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/AURM7P/
Panel discussion about Souverign Computing / Building a European Cloud ..

### Untaggling Strings: Getting CI Visibility for Vox Pupuli Tests
Speakers: Peter Souter
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/UTCKK9/
In the course of their module stewardship over community Puppet code and tooling, the Vox Pupuli organzation maintains a sprawling ecosystem of Puppet modules with lint, spec, and acceptance tests across many OS/version matrices. This Ignite shows how they turned noisy CI into signal by wiring GitHub Actions to Datadog CI Visibility - surfacing flaky tests, speeding triage, and tracing bottlenecks. We’ll share the dashboards, alerts, and tags that keep regressions at bay- and how to reuse the pattern in your repos.

### Every day I’m hustlin’
Speakers: Ben Ford
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/MFY3SB/
Are you interested in starting a company? A year ago, a friend and I got a wild hair and did just that. We took no VC, committed to Open Source and sticking it to the man. A year in, things are developing much slower than I’d wanted but we’re doing all right. We’re signing some decent contracts and have made our first few hires.

I’d like to tell you a few quick stories and maybe help you work up the nerve to jump in the pool too.

### Dopamine, Dunning-Kruger, and a Life in Technology: Why We're All Confidently Wrong About Everything (And That's Okay)
Speakers: James Freeman
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/MGVWWM/
Ever shipped a "simple fix" at 4 PM on Friday that took down production? Felt like a genius after making Kubernetes work, only to realize six months later you understood nothing? Welcome to the beautiful, chaotic feedback loop of technology work. This talk explores how our brains betray us in the most predictable ways. You'll discover why dopamine hits from solving problems make us addicted to complexity, how the Dunning-Kruger effect means we're most confident when we know the least, and why the tech industry's rapid change keeps us perpetually cycling through peaks of "I've got this!" and valleys of "I know nothing."

### How We Treat Each Other At Work
Speakers: Richard W. Bown
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/TKV8RR/
We love to do Agile and have DevOps and implement tools and frameworks and processes, but are we really any better off than we were fifteen or more years ago? What is the basis for how we go forward as engineers? Despite all of our tools and processes and our advances in engineering, sometimes we just need to remember we're working with humans and that engineering isn't just about productivity and solutions. Richard talks (quickly!) about his experiences with software engineering and how we can connect, and what drove him to write a novel, "Human Software", about putting human engineers above profits.

### Keeping the Netherlands secure and accessible with Nix
Speakers: Johan Bloemberg
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/WTLM8B/
Learn how 3 nerds help keep the Netherlands secure and accessible using Nix and NixOS. This talk will (briefly) explain what the Internet Cleanup Foundation does, its various websites like Basisbeveiliging.nl, Basistoegankelijk.nl, their Belgian counterpart and the impact 3 nerds can make on Dutch cybersecurity with lots of open source software. It will also be detailing our journey from a Docker/Puppet development and deployment environment into a fully Nix/NixOS setup. How we approached it, some practical examples and the challenges along the way.

### Free Software Needs Free Tools: Making Your Project Truly Open
Speakers: Jan Ainali
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/LHWU8T/
Your code is released with a free license, but your project runs on proprietary platforms like Slack, GitHub, Notion, or Zoom. Does it matter? In this talk, I will show how relying on non-free tools contradicts open source values, excludes contributors, locks your community into corporate ecosystems, and drives away idealistic contributors who care deeply about freedom. We’ll also tackle common justifications, like convenience or popularity, and show how they often mask deeper trade-offs. The goal with this talk is to spark reflection and conversation about the tools used to build open source projects, not just the code we bring to life. I hope it encourages both new and experienced maintainers to think critically about how proprietary tools may, unintentionally, be limiting their communities and values. The audience will leave with a better understanding of the trade-offs involved and the motivation to make small changes that lead to more open, inclusive, and resilient projects. If more projects switch even just one of their proprietary tools to an open alternative, it strengthens the entire open source ecosystem by reducing dependency on tech giants and supporting community-owned infrastructure.

Whether you're starting a new project or maintaining a mature one, this talk will challenge you to think critically about the tools you use and advocate for open, community-controlled alternatives that align with the spirit of FOSS.

[Slides](https://aina.li/cfgmgmt/)

### The Day Two Problem: Examining Decades of Infrastructure Automation Evolution
Speakers: Yair Etziony
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/LLCCHN/
Day One operations focus on initial deployment, provisioning resources, and achieving operational state. Day Two operations encompass ongoing lifecycle management: updates, drift correction, decommissioning, and sustained operational health.
The evolution from Puppet and Chef to Ansible, Terraform, Pulumi, and platforms like Crossplane represents decades of innovation in infrastructure automation. Each generation has advanced deployment capabilities, yet consistent patterns emerge in post-deployment operational challenges.
This talk explores the intricate transition from deployment to sustained operations, a journey marked by recurring themes in the evolution of configuration management. We'll dissect how different approaches handle this transition, exploring operational challenges across infrastructure layers from bare metal through hypervisors to cloud platforms.
Through comprehensive historical analysis, we'll delve into questions such as: Why do similar operational challenges persist across different generations of tooling? How do state management approaches compare to distributed coordination systems? What can we learn from examining infrastructure as dynamic systems rather than static code?
Additionally, we'll explore the relationship between infrastructure automation tools and observability platforms, investigating how the separation between these domains affects operational visibility and decision-making during Day Two operations.
You'll gain insights into approaches to infrastructure management that address the complete operational lifecycle, leaving you prepared to tackle the challenges ahead. Day One operations focus on initial deployment, while Day Two covers everything that follows: updates, drift correction, and lifecycle management. You deploy perfectly with Terraform, everything shows green, then six months later, you discover a database running somewhere that nobody remembers creating, and no monitoring covers it.
After decades working with configuration management tools from Puppet to Terraform, through the rise of DevOps and platform engineering, I've watched each generation promise to be the next breakthrough while somehow repeating the same conceptual blind spots. During recent paternal leave, I had time to examine why similar patterns emerge across different tooling generations, how state management compares to distributed coordination systems, and why infrastructure automation remains disconnected from observability platforms.
This talk explores these recurring themes and what we can learn from them.
The database example is relatable - everyone's found mystery infrastructure running somewhere!

### Expectations Driven Deployments
Speakers: Roman Mazur
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/EMBSD3/
Ever scaled your database to handle more users, only to find the WAF's old rate-limiting rules are now blocking legitimate traffic?

This is one of examples of the classic configuration drift problem. Maintaining a coherent configuration of the many components the modern systems are composed of is a challenging task. 
Evolving this configuration to match the constantly changing world is even tougher.

This talk introduces "Expectations Driven Deployments" (EDD), a practical engineering approach influenced by Test Driven Development. EDD suggests encoding our expectations about the system behavior with the goal of driving infrastructure, application, and observability configuration then refining these expectations using the data obtained from the live system.

Implementation examples we'll consider in the talk are based on CUE language which gives powerful means to achieve sustainable composition of a complex system.

The source code used during the talk is available on GitHub: [roman-mazur/poll](https://github.com/roman-mazur/poll).

### Software Defined Interviews Live Recording: Andrew Clay Shafer
Speakers: Coté
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/3A8E9G/
We'll do a live recording of [Software Defined Interviews](https://www.softwaredefinedinterviews.com)/[Software Defined Talk](https://www.softwaredefinedtalk.com). We'll do a live recording of [Software Defined Interviews](https://www.softwaredefinedinterviews.com)/[Software Defined Talk](https://www.softwaredefinedtalk.com).

## 2026-02-03 — B.Con

### Introducing Choria Configuration Manager
Speakers: R.I.Pienaar
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/YHL3JY/
Introducing a new style of Configuration Management tool that is first class usable in many situations:

 * Easily write idempotent shell scripts
 * Easily manage groups of resources in manifests
 * Simple to deploy networked schedular
 * Global scale distributed application manager via Choria Autonomous Agents

In this talk we will introduce these capabilities and demonstrate various use cases.

Information about the project can be found on its website https://choria-cm.dev

### Introducing Pabawi. Puppet Ansible Bolt Awesome Web Interface.
Speakers: Alessandro Franceschi
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/XD8SWD/
Modern times allow extraordinary things, like writing from scratch modern web interfaces to hosts management tools without knowing how to code.
Pabawi is a Web Interface to Puppet, Ansible, Bolt and potentially any infrastructure management tool. It's mostly written by Claude Sonnet, via Kiro, where the human, Alessandro Franceschi, keeps on asking, testing and asking again.

The presentation is both about Pabawi usage and features, and about the AI tools used in the process, with the inevitable lessons learned and things that proved to be useful.

### Mgmt Config: Solving the bootstrapping problem
Speakers: James (purpleidea), Andrew Clay Shafer
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/WCDFP8/
Mgmt is a real-time automation tool that is fast and safe. It has passed version 1.0.0 and is almost too powerful to describe, so we'll demo!

In this demo, I'll bootstrap an mgmt cluster, build a virtual machine host, spin up a cluster of vm's, and then build and show a small container scheduler. Everything in around ~200 lines of mcl. We can then scale it in real-time, kill hosts, and have fun by seeing it react.

Of note, everything gets deployed with a "single enter key press" to start up mgmt the very first time. Building out your infrastructure without a bootstrapping problem, is something we rarely see, even at the hyperscalers. We can do better.

I'll also throw in CPU hot swapping, and automatic wireguard clustering to really show things off. And it wouldn't be eye candy if you didn't see a GUI generated entirely in mcl using golang and wasm.

As usual, I'll live demo to your hearts content!

Some introductory documentation is available: https://mgmtconfig.com/docs/guide/
Attendees are encouraged to read some before the talk if they want to get up to speed.
A number of blog posts on the subject are available: https://purpleidea.com/tags/mgmtconfig/

### From Code to Context: Infrastructure as Code and the Model Context Protocol
Speakers: Mar
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/VM78AU/
Infrastructure as Code (IaC) describes standardized infrastructure using code - versionable, reproducible, and automated. But as environments become larger and more diverse, teams must develop and maintain more different API integrations to connect tools, platforms, and processes.
The result: a complex interface landscape of (proprietary) interfaces, small-scale workarounds, and selective bridges that are not only prone to errors but also difficult to scale.
The Model Context Protocol (MCP) offers a different approach here: instead of building a separate API solution for each tool connection, MCP creates a uniform, standardized format for context information. The extension by MCP Server represents the next logical step, in which they become the linchpin for keeping models, metadata, and infrastructure knowledge accessible independently of specific tools. They store the required context centrally, version it, and make it available organization-wide - as a “single source of truth” for infrastructure knowledge. 

This talk will present the concept and possibilities and discuss the advantages and disadvantages of MCP. It will also touch on the cultural and technical implications of such a new standard.

### Next-Level Infrastructure as Code with AWS CDK and LocalStack
Speakers: Matheus das Merces
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/AXBWWR/
You know the AWS Cloud Development Kit (CDK) lets you define infrastructure as code using programming languages like TypeScript and Python, but what if you could do much more than that?
In this talk, we will see code: from CDK Constructs, Blueprints, and Aspects to fine-grained assertions. Then, we will explore the powerful combination of CDK and LocalStack, showing how simulating AWS environments locally or in CI can help you level up your infrastructure. When you walk out of this session, you will learn how to structure your AWS CDK projects with TypeScript, when and how to apply fine-grained assertions for regression testing, and how to apply best practices with reusable CDK Constructs and enforce consistency with Blueprints and Aspects. Additionally, you will learn why LocalStack can be the best friend of your CDK project.

## 2026-02-03 — B.1.011

### How to Use an AI Assistant with Your Monitoring System
Speakers: Dmytro Kozlov
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CE9YF8/
s observability systems grow more complex, the cognitive load on users increases quite fast. This talk presents an approach that could be game-changer in the future: using AI assistants as intelligent interfaces to your observability stack. By implementing and using MCP (Model Context Protocol) servers, we can transform how observability users interact with metrics, logs, and traces. You will see how teams can query their stack in plain English and use natural language to explore data, debug issues, and even work with configurations.
The session covers both theoretical foundations and practical implementation. It demonstrates how you can integrate AI assistants directly into your day-to-day workflows and provides a comprehensive walkthrough of:
- MCP architecture and how it enables LLMs (Large Language Models) to execute observability tasks
- Setting up and configuring MCP servers (demonstrated with VictoriaMetrics) and integration with popular AI assistants
- Current and planned features of VictoriaMetrics MCP Server
- Real-world use cases: data exploring, query explanation, working with alerting rules, cardinality analysis, intelligent debugging, obtaining context-rich answer for your questions, etc
- Various tips on how to make AI assistants work better with the observability stack
Whether you're an SRE looking to reduce toil, a platform engineer seeking to democratize monitoring access, or a leader evaluating AI's role in operations, this talk provides practical insights and tools for possible transformation of your observability practice.
This approach doesn't replace monitoring expertise at the moment — it amplifies it, making expert knowledge accessible to entire teams, giving you a powerful teammate in the form of AI assistant.

### OpenTelemetry Tracing, not just for webapps
Speakers: Pieter Lexis
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/88YNP8/
The OpenTelemetry framework has, next to log and metrics, signals for application tracing information. The ecosystem is geared towards webapplications, but is not exclusive to it. In this talk, I'll discuss how we added basic tracing support to PowerDNS, how we pass trace info to downstream servers via DNS, and what this looks like in Jeager. We did this without using the existing OpenTelemetry C++ SDK, so strap in for some code and protocol hijinks and get more familiar with OpenTelemetry Tracing in the process.

### A walk through the Open Source Eco-System in the CNCF Observability Landscape
Speakers: Syed Usman Ahmad
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/QLFDWN/
CNCF Landscape is continuously evolving as more new projects are emerging either in the category of cloud-native, CI-CD, container runtime, or more.

The main source of these projects is the Open Source contributors that help to drive these projects from Sandbox to the Graduate ones by providing valuable feedback, identifying bugs and addressing real-world use cases.

However, there are times when you need to find the right Open Source tools and get help from the Community to get the best results for your project.

In this talk, you will get an understanding about the the Grafana Open Source Eco-system and how it is helping the CNCF Community/Projects. This will be a beginner-level talk, but everyone is welcome to join no matter how much experience you might have.

### Open Source Cloud-Native Observability with VictoriaMetrics and OpenTelemetry
Speakers: Dmytro Kozlov
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/9L8DKK/
In cloud-native environments, understanding the behavior of distributed applications requires complete observability across metrics, logs, and traces. OpenTelemetry has become the standard for data collection, but it still depends on a backend capable of handling all three signals efficiently.
VictoriaMetrics, fully compatible with the Prometheus ecosystem, was designed to ingest and query large volumes of metrics with recognized performance and efficiency. Today, it extends these capabilities to logs and traces, enabling teams to centralize observability in a single open source system.
This session builds on the OpenTelemetry demo to show how signals are collected, stored, and correlated in VictoriaMetrics, then explored in Grafana. Attendees will see how this approach reduces operational complexity and provides a cloud-native, scalable observability stack without reliance on proprietary solutions. All tools and platforms presented in this talk are open source.

### Can We Manage Bedrock with IaC Yet? A Practical Look Using OpenTofu and CDK
Speakers: Michelangelo Markus
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/F8UXJQ/
Amazon Bedrock makes it easy to start building with generative AI, but managing it with Infrastructure as Code is another story.
In this talk I’ll go through what actually works right now when using OpenTofu and the AWS CDK to define a small Bedrock environment.
I’ll show what parts you can manage cleanly, what still needs workarounds, and how both tools can fit together in a simple workflow.
The goal is to give an honest view of where things stand and what you can expect if you try to do this yourself today. Generative AI services like Amazon Bedrock are becoming common, but the Infrastructure as Code support for them is still limited.
This session looks at what can be done today using OpenTofu and AWS CDK together to manage a small Bedrock setup on AWS.

I’ll build a simple proof of concept that uses:
	•	OpenTofu for core AWS infrastructure (VPC, S3, IAM)
	•	CDK for Bedrock resources (Knowledge Base, Agent)
	•	A small integration step to run both tools in sequence

The talk focuses on what worked, what didn’t, and how close we are to being able to manage Bedrock workloads fully through IaC.
It’s meant for engineers and architects who want a realistic view of what’s possible right now, not a perfect demo.

## 2026-02-03 — B.1.0.14

### Reliable Network Backups & Restore with Ansible: Idempotent, Vendor-Neutral, — with AI/ML Diff Severity
Speakers: Rohit Thakur
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/8NZDMV/
In network automation, reliable backups are critical but often overlooked. This session explores how to design a consistent, vendor-neutral backup and restore workflow using Ansible.
Backups that “usually work” aren’t good enough. This talk presents a battle-tested,   backup/restore workflow for Cisco IOS/IOS-XR/NX-OS using Ansible and Validated Content. We’ll show how to pick the right transfer method (SCP/SFTP/TFTP), enable and secure internal file servers, and make tasks idempotent across vendors. We’ll also cover selecting device-native paths (bootflash:/, disk0:, /misc/config) to avoid path pitfalls.
 We will also go through a lightweight, offline rules + ML approach that scores the severity of configuration diffs (e.g., VLAN/ACL/BGP/interface changes) to prioritize reviews and automate safe rollbacks. Live demos include copying configs, verifying hashes, ranking diff severity, and controlled restores. Modern network automation needs backups that are deterministic, auditable, and work without Internet access. This session walks through:
Patterns & pitfalls:  Use absolute on-device paths (e.g., flash:/configs/backup.cfg, bootflash:/...) and do not rely on shell shortcuts like ~ (most network OSes don’t expand them). Choose the right transfer method (SFTP vs SCP) and prefer secure, internal file servers.


Idempotent backups: canonicalizing configs, hashing (SHA-256), and writing only on change.


Vendor neutrality: switching cleanly across IOS / IOS-XR / NX-OS with a single role interface.


Device-native storage: choosing bootflash:/, disk0:, /misc/config and verifying available space.


Restore safety: stage → replace/merge → post-verify via hash/lines match.



Diff severity scoring: simple feature extraction + rules (optional scikit-learn) to rank risk and trigger rollbacks.

### How we opened up Ansible's documentation infrastructure to the community
Speakers: Don Naro
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/TTBHGC/
The Ansible community team at Red Hat work to dismantle closed infrastructure and open up workloads and processes to community contributors.

Join me to hear how we moved from locked-down Jenkins jobs to transparent, community-managed GitHub workflows. I'll share how we navigated the technical challenges of migrating a truly chonky Sphinx build process, preserved a decade of SEO authority, and scored some major quality improvements by providing contributor access.

It all started at an Ansible contributor summit at CfgMgmtCamp 2023 too! So please join me as I share what we learned about infrastructure, trust, and some unexpected ways investment in OSS can unlock community potential. Some key points we'll cover in this session:

- Why closed infrastructure hurts open source projects, even when it seems "necessary"
- Tackling massive sphinx-builds (spoiler alert: I/O and memory constraints)
- Preserving SEO while migrating unmaintainable legacy content and 10k+ http redirects
- Replacing Jenkins jobs with GHA workflows
- How Read The Docs saved the day!

### Writing, running, and testing awesome Ansible content with natural language and AI - powered by Ansible's MCP server
Speakers: Shatakshi Mishra
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/WG9ST8/
Ansible content developers lose hours each day to context switching, which kills productivity and increases the risk of human errors.

We've integrated an AI-powered Model Context Protocol (MCP) server directly into the Ansible VS Code extension to address this problem. The result is a single, unified development experience that goes beyond an ordinary AI code assistant. Adding MCP server capabilities to the Ansible VS Code extension gives you an intelligent development environment that allows you to work within the context of all your existing Ansible content, including playbook, roles, and inventories. As a result, teams can reduce fragmentation in their workflows to gain productivity and standardise and accelerate Ansible content development. In this session you will see live demos of scenarios including …

- Configuring the MCP server through the VS Code extension.
- Enabling Ansible development tools with MCP server capabilities.
- Scaffolding new Ansible projects and collections using the ansible-creator MCP tool.
- Validating playbook and automatically fixing issues using the ansible-lint MCP tool.
- Debugging a complex playbook run with ansible-navigator to review and troubleshoot issues in your automation content and much more.

## 2026-02-03 — B.1.015

### Cross-Platform Compliance
Speakers: Steven Pritchard, Kendall Moore
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/NRVBJE/
Compliance as Code shouldn’t stop at a single operating system. With Compliance Engine, we’ve expanded support beyond the traditional RHEL family to include Windows systems, and we’re working toward Ubuntu/Debian as well. This talk will explore the challenges and lessons learned while bringing compliance data and enforcement to multiple platforms. We’ll discuss differences in compliance frameworks, strategies for testing and verification, and how to keep compliance data consistent and reusable across diverse environments. Attendees will get a detailed look at how Compliance Engine enables cross-platform compliance in Puppet/OpenVox. We’ll show how Windows support has been implemented, outline what’s needed to bring Ubuntu/Debian into the mix, and share insights into testing strategies across heterogeneous infrastructures. By the end of the talk, participants will understand how to approach compliance in mixed OS environments and where the community can help shape the next steps.

### Introduction to the Automated Operation and Maintenance System at IHEP
Speakers: Xiaofei Yan
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/C7SJ99/
IHEPCC is the Computing Center of the Institute of High Energy Physics, Chinese Academy of Sciences. We have been using Foreman and Puppet to manage our high-energy physics computing platform since 2013, currently managing over 4000 nodes and multiple data centers. In this report, I will introduce how we use Foreman and Puppet, and the corresponding development we have done for our local computing environment. I also hope to share and learn from other experts in this area.

### How to migrate your Puppet [Enterprise] CA to OpenVox server
Speakers: Robert Waffen
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/NDAM98/
How to migrate your Puppet [Enterprise] CA to OpenVox server. Just a short step by step guide on how to migrate. How to migrate your Puppet [Enterprise] CA to OpenVox server.
Just a short step by step guide on how to migrate.

### Into the Spiderverse of Puppet test pipelines
Speakers: Ben Ford
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/F9MXXR/
With the unexpected proliferation of Puppet implementations, you may be wondering how to test your modules effectively. Interestingly, this isn't a new problem. It's a somewhat known secret that even the Supported modules on the Puppet Forge weren't ever tested against Puppet Enterprise, but like Bruno we don't talk about that. Because it didn't really matter, except -- well, when it did.

That was bad enough, but now we've splintered into four separate implementations built by two wildly different groups with very different priorities. We have the legacy Open Source Puppet that's still in broad use, there's the new proprietary Puppet Core which requires a EULA and a license key to download, there's Puppet Enterprise which used to be built on OSP but will be based on Puppet Core going forward. And now we have the truly Open Source OpenVox implementation built by your friends at Vox Pupuli. They're diverging as we speak.

This talk will go over topics such as
- why it's difficult for community module authors to test their code against Puppet Core.
- why it's (was) effectively impossible to test modules against multiple implementations.
- the legal thorniness preventing Vox Pupuli from signing the EULA.
- the rough spot the ecosystem has been forced into in which paid customers were being forced into using effectively untested modules.

Many of my customers are current or former Puppet customers and they're methodically migrating from legacy OSP to OpenVox so they can keep up with security patches, project evolution, and new features. But module and gem test suites have always been written with the assumption that they only had to test against legacy OSP. Some can be tricked into running against OpenVox, but being able to test against both at the same time? Not a chance.

My customers cannot and will not accept an ecosystem with untested code, and you probably don't want to either. But you still need a way to continue testing on legacy OSP until your migration to OpenVox is complete.

We have been hard at work building a pipeline that makes this possible, with very little upstream modification. Come see how it works.

### Migrating Modules to OpenVox
Speakers: Steven Pritchard
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/SRNZYS/
Over the past year, we’ve migrated dozens of Puppet modules to OpenVox. This talk focuses on the technical aspects of migration from tooling and automation to testing strategies, providing a roadmap for others facing the same challenges. We’ll share lessons learned from real-world migrations, covering what went smoothly, what required workarounds, and how to plan for success. Attendees will leave with practical guidance on migrating Puppet code to OpenVox, along with strategies to validate and test their environments throughout the transition.

### Should we rewrite OpenVox server in plain ruby?
Speakers: Marcus Poller
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/7HGANT/
OpenVox server runs on top of the Java Virtual Machine (JVM). JVM ist just the interpreter, but the languages used are Clojure and Ruby. Once upon a time this architecture was choosen for performance reasons. OpenVox server is hard to bundle, it uses its own package manager (ezbake) and service supervision (read systemd clone aka trapperkeeper). The JVM in production use is hard to deal with, there are constraints on memory, caching, and scaling.
Can we ditch the JVM (and Clojure)?
Yes, but...
... these are all the tradeoffs you need to know:

 - ruby implementations
 - ruby concurrency
 - performance
 - architecture workarounds

## 2026-02-03 — B.1.017

### Ansible - State of the Community
Speakers: John "gundalow" Barker, Don Naro
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/PES9FE/
As one of the big events on the Ansible Community calendar, CfgMgmtCamp is an opportunity to get together and review how we're doing as a community.

This talk is aimed at anyone with an interest in Ansible, as all voices are welcome in the discussion of how to shape the community in the coming year. Thanks for making the time to join the review of the Ansible Community in 2025

We will start by highlighting some wins the community has had, before digging into details of some of the larger projects.

Finally I'll explain what I hope you'll get out of Wednesday's Contributor Summit, and how this talk, and in fact, some of the other talks over the next 2 days hope to plant seeds for future discussions, so together we can continue to drive Ansible forward.

### Asking a local LLM about my Ansible playbooks because why not
Speakers: David Moreau-Simard
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/Y833ZQ/
LLMs can write Ansible roles and playbooks as well as plugins and modules to a relative degree of competency with commodity hardware that you can run offline, at home, with less privacy and security concerns.

They certainly understand what Ansible is, how it works and they can write YAML, Jinja or Python.

What about troubleshooting an issue with an Ansible playbook ?
You could provide it with a log file or copy & paste the results of your ansible-playbook command.
Maybe it could point you in the right direction... or hallucinate. Who knows ? ¯\\_(ツ)_/¯

ARA Records Ansible playbook results to a database and provides an API to query the results.
What if we gave a LLM programmatic access to that API using Model Context Protocol (MCP) ?
It would allow the model to include context like host facts, playbook files and detailed task results, amongst other things.

The author experimented with it (for science) and the results are interesting.

Join us to learn about the experiment, how it works and how it might be useful in a number of ways. Recording available: https://www.youtube.com/watch?v=WvMmCr8Ho4c

### Ansible Style Guide and guidelines for compatibility with newer versions of Ansible community package/ansible-core (Ansible 12/ansible-core 2.19 and above)
Speakers: Kostiantyn Volenbovskyi
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/NNFGN9/
There are several Ansible Style Guides and I would like to present a different one based on existing ones with certain guidelines added and changed

It covers topics such as list of dictionaries as recommended structure for "more complex" variable, usage of set_fact, etc. The presentation in PDF: https://github.com/abacusresearch/ansible-style-guide

List of topics:
- Changed/removed functionality in ansible-core 2.19 (and above)
- Guidelines on using variables defaults/ vs. vars/
- Jinja: conditionals, various variable types
- List of dictionaries and various filters used for list of dictionaries
- Multiline strings
- import_tasks vs. include_tasks
etc.

### A Love Letter to Ansible Core 2.19
Speakers: Matt Davis
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CQDEPX/
Nervous about upgrading to Ansible Core 2.19? Learn how the revamped template engine and error handling in Ansible's latest release will make your life easier from a self-proclaimed Ansible lover.

## 2026-02-03 — B.1.031

### The Director's Cut: A new role for Ansible in Foreman
Speakers: Thorben Denzer, Jan Bundesmann
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/SYSTYP/
Ansible has long been a cornerstone of configuration management in the Foreman ecosystem.
While the existing integration offers robust capabilities, users have expressed desire for DevOps workflows.

In this talk, we will introduce a reimagined Ansible integration, designed to address these needs.
This new approach brings advanced features, such as

* version control integration,
* isolated execution environments and
* lifecycle management.

For Foreman users and developers alike, this talk gives an overview of "foreman_ansible_director", ATIX's new Ansible integration for Foreman.
This overview consists of our design decisions, lessons learned during development, a look ahead and a live demo!

### EU OS use case study: bootc-based laptop fleet management with foreman
Speakers: Robert Riemann, Stefan Bogner, Jonas Trüstedt
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/LDHSVL/
The demand for more control over corporate IT assets grow significantly in the last 2 years. The project EU OS proposes a concept based on open source to setup and control a corporate Linux laptop fleet in the public (and private) sector.

In this talk, we present the problem EU OS attempts to solve, the proposed solution based on bootc clients managed by foreman, report on on-going proof of concepts and present our wish list to cover missing features. For this, we leverage foreman for provisioning of EU OS, imagemode patching, artefact store for both the OS and for corporate flatpaks, and enrolment in FreeIPA for user management.

### Insights Compliance in Foreman
Speakers: Roman Blanco
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/8WDVVM/
Integrating Red Hat Insights Compliance into Foreman Together with Red Hat Insights Compliance team, we're investigating integration of Insights Compliance from Red Hat Hybrid Cloud Console (console.redhat.com) as an add-on into Foreman to provide better Compliance monitoring for users on-premise.

The project is being maintained publicly on github.com/RedHatInsights/compliance-backend since September 2018.
Our solution, also based on OpenSCAP, lets you create, customize, and track multiple policies at once, and it gives you a view of individual systems’ compliance levels.

We would like to present our idea to the Foreman community and hear-out their comments or concerns.

### Simplifying the deployment of Foreman as a bare-metal provisioning system
Speakers: Alexander Olofsson
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/QHPTF3/
Foreman is a powerful - and complex - piece of software, especially if you want to use its Metal-as-a-Service functionality, or just simply provision bare metal on it.  
What if we could strip it down to _just_ a Rails service, without losing any of that functionality? Setting up fully featured installs of Foreman with all its MaaS and lifecycle-management functionality requires a lot of surrounding configuration and software, and not just with static configuration either.  
What if we could strip down Foreman to its Rails core, and still be able to do full Metal-as-a-Service with it?

This talk explores how to strip out the pieces of Foreman that require the use of Smart Proxies, instead leveraging iPXE, static DHCP configuration snippets, and a few small plugins.  
All to allow the MaaS functionality to remain, but without requiring any of the dynamic configuration or network orchestrating that would normally be needed for them.

### From 'undefined' to 'I Told You So' - TypeScript for the Foreman Frontend
Speakers: Thorben Denzer
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/F8DXGP/
While JavaScript has long been the backbone of the Foreman frontend, both for plugins and core alike, I decided to shake things up for *foreman_ansible_director*.
A year and over 9,000 lines of TypeScript code later, I'm here to share what I learned.

This talk will explore:

* The surprisingly smooth integration of TypeScript into an existing JavaScript ecosystem
* The real benefits of type safety
* Interoperability with existing code
* What this implies for packaging

This talk isn’t just about TypeScript - it’s a story of how type safety can reduce errors, make life easier for developers, and improve maintainability of the codebase.

### Static vs. Dynamic Secrets: What Are We Really Talking About?
Speakers: Leon Krass
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/RRDMZZ/
Secrets are everywhere in modern infrastructure - API keys, credentials, tokens, certificates - but what exactly qualifies as a "secret"? What are static and dynamic secrets? How do they behave? This talk begins by defining the term itself and mapping out where secrets typically appear across systems, environments, and workflows.

We’ll dive into the distinction between static and dynamic secrets, examining whether the difference is technical, operational, or even philosophical.

Within a live demo, we’ll explore how secrets behave in practice, how they’re provisioned and rotated, and what implications they have for security and operations.

This session aims to clarify terminology, challenge assumptions, and help attendees make informed decisions about how they handle secrets in their own environments.

Demo Tech Stack: OpenBao, Keycloak, PostgreSQL, OpenSSH

## 2026-02-03 — B.1.036

### Rudder: automate system security and configuration with GUI, API and YAML
Speakers: Nicolas CHARLES
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/W8NCFX/
Rudder is an open source solution for managing system security and configuration, with a strong focus on continuous checks and compliance.

With its GUI, it makes it easier for users to  define  security configurations and get feedback. Its API allows integration with most softwares that interact with your infrastructure.

This talk will present Rudder and its use cases, then focus on the new version, Rudder 9.0, and conclude with a demo of configuring and hardening new instances on AWS

### The missing layer: Security auditing of configuration files
Speakers: Alexis Mousset
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/EJRFHU/
Automation management tools focus on enforcement, pushing desired state 
to systems. But we see growing needs for configuration auditing, especially for security reasons, which do not fit this workflow. It requires the ability to fetch real values and check them with a wide range of criteria.
This talk presents a tool designed specifically for configuration files auditing. It is based on Augeas, leveraging its powerful parsing capabilities and lens-based architecture, and extends  it with dedicated auditing keywords, such as regex matching, numerical comparisons, allowed-value lists, and more. Output is designed to provide useful context, using compiler-like messages, diffs outputs, etc. The tool stays capable of doing remediation.
We' will demonstrate configuration files checks in the context of several security benchmarks, showing how this approach bridges the gap dedicated audit scripts and automation tooling.

### SysInspect: from prototype to production
Speakers: Bo Maryniuk
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/JGE9KE/
SysInspect began life as an ADAS integrity observer in automotive systems. Over time, it morphed into a full-blown configuration & anomaly monitoring framework. Now it’s pushing into the embedded & IoT domain, where the usual CM tools usually don’t dare to. In this talk I’ll show how SysInspect handles anomaly detection, integrity in very constrained devices, and scales seamlessly up to full clusters. Everyone solved configuration management on big servers. But embedded devices and IoT are still a mess — no SSH, flaky networks, tiny memory, and thousands of quirky devices that existing tools simply ignore.

SysInspect started as an ADAS integrity observer and grew into a configuration and anomaly platform built for exactly these forgotten environments. It works without heavy (that much) agents, tracks state, detects drift and inspects runtime behavior. Telemetry modules stream structured JSON logs or OTLP traces even over poor links.

It scales from a few-megabyte sensor board to large clusters and integrates with existing observability stacks. Typical use cases:

- Validate system state before OTA rollouts.
- Detect anomalies in the field in real time.
- Provide continuous visibility across distributed fleets.
- Feed inspection results directly into whatever uses OTel standard: Loki, Elasticsearch, Vector, Grafana etc.

This talk shows how SysInspect builds a live model of each device, explains anomalies in context, and adapts its configuration logic across wildly different environments — plus what’s new since last year and where the project is heading.

P.S. Of course it uses WASM. Your system doesn’t? 😏

### Watch paint dry - Monitoring what doesn't change
Speakers: Ole Herman Schumacher Elgesem
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/78VKZV/
Many monitoring solutions exist for tracking numbers and percentages which change, trends, outliers, spikes, and so on. However, what about things that don't change, or rather, shouldn't change? There are many examples of these relevant for security teams to know about. And since you don't expect them to change, any change is noteworthy. In this talk I will discuss the idea, and launch my open source implementation of it. It uses PostgreSQL as the database, and has a modular architecture, so it is easy to expand it with the things you want to monitor. History and changes for each variable are tracked in the database, making it simple to implement new modules.

Some examples for things to track are: number of script tags on your website, checksum of a released version of software, commit SHA of a tag (version), number of unsigned / untrusted commits in a repo, number of admins in an organization, IP address (DNS entry) of your website, etc. When any of these change, it can be a signal of some kind of compromise or malicious activity, and a way to track and alert on these changes is useful.

### Crowdsec and Mikrotik integration
Speakers: Michal Sochon
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/XBH3UZ/
Crowdsec is something like fail2ban but across multiple hosts/clusters. Mitigation of the attacks can be done by for example in web server module, firewalls or custom components (formerly called bouncers). This is a story how to use a Mikrotik router as mitigation tool for Crowdsec using opensource project I forked few weeks ago. This project is not affiliated in any way with CrowdSec nor MikroTik, thus use at your own risk.

Crowdsec is something like fail2ban but across multiple hosts/clusters. Mitigation of the attacks can be done by for example in web server module such as lua scripts in nginx, firewalls via iptables/nftables, kubernetes (yay because why not), or custom components (formerly called bouncers).

This is a story how the project was forked and how to to integrate Crowdsec into a Mikrotik router  - https://github.com/nvtkaszpir/cs-mikrotik-bouncer-alt which is fully opensource . I will provide a short history why I did it, and what are the pros/cons of that solution. I provide some working examples of how much resources it takes to implement it, real usage graphs from the working system.

Few words about the ideas for improvements I have.
I'm also eager to listen to the suggestions from more advanced people in improving the solution.

### crinit - an embedded, dependable, security-aware init system
Speakers: Thomas Brinker, Andreas Zdziarstek
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/NWW3JZ/
Crinit [krinit] is a new lightweight init system targeted at embedded systems. The feature set includes parallelism, authenticated configuration, and a runtime control interface. In this presentation, we will show the goals, the architecture and some details on the API for this project.

The startup phase of a Linux system is largely ruled by systemd and it does a great job of that.
But sometimes it would be nice to have something simpler and smaller without returning to the highly shell-dependent solution "SystemV-init".
Along with these requirements, security needs to be addressed, by dropped privileges to the least minimum level. Resource consumption controlled by crinit using cgroups.

crinits code base is small and fast, it initialises the userland by traversing a directed dependency graph that can be modified dynamically.
Config-files and service-definitions can be signed to ensure usage of configurations from authorized sources only.

In dependable systems crinit is used to startup processes handlings tasks that need to be development according IEC61508 ISO26262.

crinit is an open source community project under MIT license and we wish to encourage its wide spread adoption and contribution.

This presentation will present the goals, the architecture and some details on the API for this project. 

crinit can be found here: https://github.com/Elektrobit/crinit

## 2026-02-04 — ALL

## 2026-02-04 — B.1.011

### mgmtconfig workshop - morning
Speakers: James (purpleidea)
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CCG7LJ/
# Mgmt Config: Training Workshop

## Hands-on automation in a virtual machine

[Mgmt](https://github.com/purpleidea/mgmt/) is a real-time automation tool that is fast and safe.
In this workshop, we'll give you a virtual machine running mgmt, the tools to try out some examples, and the encouragement to build your own. Both new users and seasoned veterans are all welcome. We expect to also have some experienced mgmt developers present too! You are also welcome to join to hack on mgmt itself.

It's strongly recommended that you come with a modern Linux laptop, particularly if you want to hack on the core. At the minimum, all you'll need is to be able to SSH into the vm where the full test environment will be available to you.

The **workshop is free** but spaces are limited, so please register in advance.
On-site registration is possible if space permits. **Registration is required to
participate in the workshop.** https://forms.gle/EmgWu9DwpTzsEbBz6

Some introductory documentation is available: https://mgmtconfig.com/docs/guide/
Attendees are encouraged to read some before the workshop if they want a preview!

### mgmtconfig workshop - afternoon
Speakers: James (purpleidea)
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/KSD7ET/
# Mgmt Config: Training Workshop

## Hands-on automation in a virtual machine

[Mgmt](https://github.com/purpleidea/mgmt/) is a real-time automation tool that is fast and safe.
In this workshop, we'll give you a virtual machine running mgmt, the tools to try out some examples, and the encouragement to build your own. Both new users and seasoned veterans are all welcome. We expect to also have some experienced mgmt developers present too! You are also welcome to join to hack on mgmt itself.

It's strongly recommended that you come with a modern Linux laptop, particularly if you want to hack on the core. At the minimum, all you'll need is to be able to SSH into the vm where the full test environment will be available to you.

The **workshop is free** but spaces are limited, so please register in advance.
On-site registration is possible if space permits. **Registration is required to
participate in the workshop.** https://forms.gle/EmgWu9DwpTzsEbBz6

Some introductory documentation is available: https://mgmtconfig.com/docs/guide/
Attendees are encouraged to read some before the workshop if they want a preview!

## 2026-02-04 — B.1.0.14

### Ansible Contributor Summit - Morning Sessions
Speakers: John "gundalow" Barker, Don Naro
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/HPHLRM/
Ansible Contributor Summit is a full day working session for community users and contributors to interact with each another along with Ansible development teams. We will discuss important issues facing the Ansible community with a goal to shape the future of Ansible in a way that improves and increases collaboration.

### Ansible Contributor Summit - Afternoon Sessions
Speakers: Don Naro, John "gundalow" Barker
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/MQVURC/
Ansible Contributor Summit is a full day working session for community users and contributors to interact with each another along with Ansible development teams. We will discuss important issues facing the Ansible community with a goal to shape the future of Ansible in a way that improves and increases collaboration.

## 2026-02-04 — B.1.017

### Vox Pupuli Community Day - Morning Sessions
Speakers: Ben Ford
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/VENJ3R/
Vox Pupuli's Community Day is a space for community and contributors to engage directly with each other and collaboratively learn and make some magic. Do you have a burgeoning project you want to workshop and get feedback and ideas on? Do you want get the first glimpses at changes coming to the OpenVox platform? Or maybe you'd just like to help shape the next year of the community.

Expect a full day of content facilitated by the Vox Pupuli community leaders. We'll talk about the roadmap for the platform. We'll collaborate on ideas and get a pulse on what people are working on and help each other solve problems. If time and interest allows, we will hold bird of a feather sessions and/or lightning talks.

Bring projects you'd like to work on and get advice and guidance from peers and Vox Pupuli contributors. We'll have workshop time on TBD topics.

New to the community? Learn about ways to participate and how to get involved with Vox Pupuli, our premier community group.

### Vox Pupuli Community Day - Afternoon Sessions
Speakers: Ben Ford
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CCCJWF/
Vox Pupuli's Community Day is a space for community and contributors to engage directly with each other and collaboratively learn and make some magic. Do you have a burgeoning project you want to workshop and get feedback and ideas on? Do you want get the first glimpses at changes coming to the OpenVox platform? Or maybe you'd just like to help shape the next year of the community.

Expect a full day of content facilitated by the Vox Pupuli community leaders. We'll talk about the roadmap for the platform. We'll collaborate on ideas and get a pulse on what people are working on and help each other solve problems. If time and interest allows, we will hold bird of a feather sessions and/or lightning talks.

Bring projects you'd like to work on and get advice and guidance from peers and Vox Pupuli contributors. We'll have workshop time on TBD topics.

New to the community? Learn about ways to participate and how to get involved with Vox Pupuli, our premier community group.

## 2026-02-04 — B.1.031

### Hands-On Infrastructure Management with System Initiative
Speakers: Paul Stack
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/BVZBGX/
### Session 1: Getting Started & Discovery (60 min)

**Intro (10 min)**
- Workshop goals and environment setup
- Install SI: `curl -fsSL systeminit.com/install | bash`

**Hands-On: Building Your Digital Twin (50 min)**
- Connect SI to a sample cloud environment
- Import existing infrastructure resources
- Explore the visual map of resources, relationships, and dependencies
- Exercise: Use AI to analyze and document what's actually running
- Discussion: Compare discovered state vs. expected state

---

### Session 2: Troubleshooting & Remediation (45 min)

**Hands-On: Fix It in Simulation (45 min)**
- Introduce a broken service scenario
- Walk through issue identification with SI
- Pull in relevant resources automatically
- Propose and review fixes in simulation mode
- Exercise: Approve and apply the fix
- Debrief: How this changes incident response workflows

---

### Break (15 min)

---

### Session 3: Repeatable Infrastructure with Dynamic Templates (60 min)

**Hands-On: From Working to Replicated (60 min)**
- Take a working infrastructure setup
- Create a dynamic template from it
- Exercise 1: Deploy to a new region
- Exercise 2: Promote from dev to prod with parameter changes
- Demonstrate importing a new service without breaking automation
- Discussion: Template strategies for HA, DR, and multi-environment

---

### Session 4: Policy Enforcement (45 min)

**Hands-On: Three Layers of Policy (45 min)**

- **Layer 1 - Cloud Provider Policies (10 min)**
  - Configure AWS SCPs/RCPs to block non-compliant resources

- **Layer 2 - Component Qualifications (15 min)**
  - Exercise: Set standards (encryption, instance types, backups)
  - Trigger and review qualification flags

- **Layer 3 - AI-Driven Compliance (20 min)**
  - Write a compliance control in plain English
  - Run evaluation against infrastructure
  - Review compliance report (SOC 2 / HIPAA / PCI-DSS example)

---

### Wrap-Up & Q&A (15 min)

- Recap of workflows covered
- Resources for continued learning
- Open Q&A

---

**Materials Needed:**
- Laptop with terminal access
- Cloud account credentials (sandbox provided or bring your own)
- Pre-configured sample environments for each exercise

### Own Your Data: Unlocking Documents with Docling
Speakers: Carol Chen, Ming Zhao
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/9CV7CY/
Docling is rapidly becoming the de-facto standard in open source document AI. The project has achieved remarkable adoption with over 45K GitHub stars, more than 1.5 million monthly downloads, and multiple top rankings on global GitHub and HuggingFace trending leaderboards. Incubated as a Linux Foundation AI & Data project, Docling provides local-first, enterprise-grade capabilities, excelling at parsing complex layouts, extracting tables, and converting unstructured documents into AI-ready structured formats.

In this hands-on session, you'll get a chance to:
- ingest and parse multiple doc formats including PDF, DOCX and more
- convert complex tables into usable formats
- extract and prepare images for AI processing
- preserve metadata for visual grounding
- explore AI integration with frameworks like LangChain to power RAG and model training

Prerequisite: (the Jupyter notebooks for this workshop can be run locally on your laptop or remotely via Colab)
- local: git, python 3.11 or 3.12, jupyter, replicate account (sign in with github)
- remote: Colab (requires google account), replicate account (sign in with github) Project links:
- https://www.docling.ai/
- https://github.com/docling-project
- https://lfaidata.foundation/projects/docling/

## 2026-02-04 — B.1.036

### IaC workshop
Speakers: Stefan Joosten
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/BRZSV9/
Infrastructure-as-code is a large landscape. Talks typically focus on a specific tool and provide introductory to in-depth knowledge for that tool, which is great! In practice one needs to bring a combinations of tools together to deploy some application or service. This workshop aims to provide you with a lab environment and some guidance to do just that, in practice. In this workshop you will wear the coat of a DevOps engineer. The mission: package and deploy an application using configuration management tools. The idea is to gain hands-on experience with a combination of popular tools used in the infrastructure-as-code and configuration management landscape. Learning as you go and, hopefully, have fun along the way!

With the support of some explanatory slides and a trainer as your guide, you will explore a Python application stored in Git, learn about automated tasks in VSCode, package your application in a container image (using Docker or Podman), define infrastructure using OpenTofu, write an Ansible Playbook to deploy the and test if you were successful. If not... more opportunity to learn, fix and demystify the landscape of Infrastructure-as-Code.

### Pulp User Group Meetup
Speakers: Dennis Kliban
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/7MTYET/
Anyone interested in using Pulp should join this event hosted by Pulp developers.

## 2026-02-04 — B.3.0.13

### From Zero to Immutable Kubernetes: Your First Cluster, Step by Step
Speakers: Mauro Morales, Dimitris Karakasilis
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/W9LUC3/
## Abstract

Immutability at the OS level is gaining traction as a way to simplify, secure, and scale Kubernetes operations — without the fragility of hand-crafted node configurations or the false sense of control offered by traditional configuration management systems, which often still result in drift and snowflakes. In this hands-on workshop, you’ll learn how to build Kubernetes clusters that are easier to deploy, upgrade, and recover — and do it all step-by-step, without needing to become an OS expert.

### You’ll learn how to:
- Understand what an immutable OS is and why it matters  
- Deploy Kubernetes on top of an immutable system  
- Add and manage read-only worker nodes  
- Upgrade nodes manually or via Kubernetes-native workflows  
- Create your own tailored, immutable OS image
- Integrating OS builds into your CI/CD pipelines

### If time allows, we’ll also explore:
- Air-gapped and hybrid-cloud deployments  
- PXE/netboot cluster bootstrapping  
- Trusted Boot with TPM/UEFI  
- High-availability setups on immutable infrastructure  
- Raspberry Pi and edge use cases with mesh networking

All examples will be built using [Kairos](https://kairos.io), an open-source Linux toolkit designed to make immutability practical and flexible — but the patterns you’ll learn are applicable beyond any single tool.

## Audience

This workshop is designed for **platform engineers, SREs, and solution architects** who need more flexibility than fully managed Kubernetes solutions typically allow — but who also want to avoid taking on the burden of maintaining yet another complex system. If you’re comfortable with Linux, familiar with Kubernetes basics, and can spin up a VM or cloud instance, you’ll leave with real-world skills you can apply immediately. ## Outline

1. **What are immutable OS and how to think about operations with this paradigm**

   Explore the philosophy and architecture of immutable systems versus traditional configuration management tools. Learn how immutability enables atomic upgrades, reduced drift, simplified recovery, and stronger security postures.

   **Resources**

   - [Immutable Architecture](https://kairos.io/docs/architecture/immutable/)
   - [Understanding Immutable Linux OS: Benefits, Architecture, and Challenges](https://kairos.io/blog/2023/03/22/understanding-immutable-linux-os-benefits-architecture-and-challenges/)

2. **Introduction to Kairos and its major concepts**

   Get familiar with Kairos as a cloud-native, distro-agnostic, immutable Linux meta-distribution. Understand key concepts like A/B system partitions, persistent data separation, recovery mode, and cloud-config-driven provisioning.

   **Resources**

   - [Getting Started](https://kairos.io/getting-started/)
   - [What is Kairos](https://kairos.io/getting-started/what-is-kairos/)
   - [Architecture](https://kairos.io/docs/architecture/)
   - [Reference](https://kairos.io/docs/reference/)

3. **Deploying a single-node cluster**

   Deploy Kairos on a VM or bare-metal machine and initialize a Kubernetes control plane using K3s and cloud-init. Validate node readiness and explore initial workloads.

   **Resources**

   - [Manual Single-Node Cluster](https://kairos.io/docs/examples/single-node/)

4. **Build your own immutable OS**

   Use the **Kairos Factory** (from the Web or CLI) to create a custom immutable OS image tailored to your needs. Learn how to configure the base system, embed Kubernetes, and prepare for consistent provisioning.

   **Resources**

   - [The Kairos Factory](https://kairos.io/docs/reference/kairos-factory/)
  
5. **Integrating OS builds into your CI/CD pipelines**

  Automate OS image building and publishing using GitHub Actions or similar CI systems.

  **Resources**

  - Pending

6. **Upgrading your cluster manually**  
   
   Perform manual upgrades using A/B partitions and Kairos commands. Practice rolling back and verifying upgraded systems.

   **Resources**

   - [Manual Upgrade](https://kairos.io/docs/upgrade/manual/)

7. **Deploying a multi-node cluster**  
   
   Scale to a multi-node setup by bootstrapping additional Kairos worker nodes. Learn how to use cloud-config to preconfigure joining behavior.

   **Resources**

   - [Manual Multi-Node Cluster](https://kairos.io/docs/examples/multi-node/)
   
8. **Upgrading your cluster through Kubernetes**  
  
   Set up the **Kairos Operator** to manage in-cluster, declarative upgrades. Apply upgrade plans to roll out updates across multiple nodes in a safe, automated way.

  **Resources**

  - [Kairos Operator README](https://github.com/kairos-io/kairos-operator)

### ⏱️ Optional Advanced Topics *(time and interest permitting)*

- **Build an air-gapped cluster**
  
  Mirror container images and OS builds to run a Kubernetes cluster completely offline.

  **Resources**

  - [How to Create an Airgap K3s Installation with Kairos](https://kairos.io/docs/examples/airgap/)

- **Perform a hybrid-cloud deployment**
  
  Combine public cloud and on-prem nodes into a single cluster using Kairos-based images.

  **Resources**

  - Pending

- **PXE/netboot cluster bootstrapping**
  
  Use AuroraBoot to provision nodes over the network without local install media i.e. cdrom/usb

  **Resources**

  - [Netboot](https://kairos.io/docs/installation/netboot/)
  - [P2P Multi-Node Cluster Provisioned via Netboot](https://kairos.io/docs/examples/p2p_e2e/)

- **Trusted Boot with TPM/UEFI for maximum security**

  Enable cryptographic boot verification to ensure system integrity at startup.

  **Resources**

  - [Architecture](https://kairos.io/docs/architecture/trustedboot/)
  - [Installation](https://kairos.io/docs/installation/trustedboot/)
  - [Upgrading](https://kairos.io/docs/upgrade/trustedboot/)
  - [System Extensions](https://kairos.io/docs/advanced/sys-extensions/)
  - [Unlocking the Mysteries of Trusted Boot: A Deep Dive into Secure System Boot Processes](https://kairos.io/blog/2024/04/10/unlocking-the-mysteries-of-trusted-boot-a-deep-dive-into-secure-system-boot-processes/)

- **Deploying an HA multi-node cluster**

  Set up a highly available control plane using immutable nodes and external etcd or load balancing.

  **Resources**

  - [Manual HA Cluster](https://kairos.io/docs/examples/ha/)
  - [Self-coordinating HA Cluster](https://kairos.io/docs/examples/multi-node-p2p-ha/)
  - [Self-coordinating P2P Multi-Node Cluster with High Availability and KubeVIP](https://kairos.io/docs/examples/multi-node-p2p-ha-kubevip/)

- **Deploying a multi-node self-coordinating cluster**

  Use Kairos mesh networking features to create clusters that auto-discover and join each other.

  **Resources**

  - [Self-Coordinating Multi-Node Cluster](https://kairos.io/docs/examples/multi-node-p2p/)

- **Raspberry Pi deployments**

  Boot Kairos on ARM devices and set up a lightweight edge Kubernetes deployment with real hardware.

  **Resources**

  - [Installation](https://kairos.io/docs/installation/raspberry/)

### Your Workstation Defined in Code—Bluefin, Chezmoi, and Gopass
Speakers: James Freeman
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/FYUEWV/
What if your entire workstation—OS configuration, installed packages, dotfiles, and secrets—lived in Git repositories? What if spinning up a perfectly configured development environment was just git clone and a reboot away? This workshop teaches you to define your computing environment entirely as code. No manual configuration. No "I think I installed this package." No hunting for that config file you tweaked six months ago. Everything—from the base operating system to your shell prompt—declared, versioned, and reproducible. **Your Workstation as Code:**

- Bluefin custom image: Your OS definition—packages, settings, services—in a Containerfile you can build and version
- Chezmoi: Your dotfiles as templated, version-controlled code with conditional logic for different machines
- Gopass: Encrypted secrets stored in Git, decrypted on-demand, never in plaintext

**What We'll Build:**

- A complete workstation definition living in GitHub repositories
- Automated deployment from code to running system
- The ability to replicate your environment on any machine—or recover from disaster in under an hour
Configuration management patterns without traditional CM tools

**Why This Matters:**
- This is infrastructure as code for personal computing. Your laptop becomes cattle, not a pet. Breaking things stops being scary. New machines stop being painful. You gain the same confidence in your workstation that you have in your production infrastructure.

**You'll Need:**

- GitHub account (free)
- Optional: virtualization-capable laptop to test your builds
- Desire to never manually configure a system again

Leave with your entire computing environment defined in code and the skills to maintain it forever.

## 2026-02-04 — B.3.029

### Hands-on Infrastructure-as-Code with OpenTofu (Terraform)
Speakers: Patrick Mölk
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/CWFLVM/
Curious about DevOps? Learn the Infrastructure-as-Code (IaC) part of DevOps with OpenTofu. In this workshop you will provision cloud resources and deploy a simple web app on them. Using Terragrunt you will then replicate the same infrastructure in different environments. 

No experience? No problem! We'll start from zero.    

To get the most out of this hands-on workshop it would be best if you have access to an AWS account to play with. However, it's not strictly necessary. Whether you're used to clicking around your cloud provider's UI to deploy your apps or you are completely new to cloud computing and infrastructure management, this workshop will get you started.

We will cover the following concepts:

* basics
	* providers, resources - quickly deploy something
	* variables, inputs, outputs - minor clean up
	* destroying infrastructure
* state management
	* manipulating state
	* importing existing infrastructure
	* generating code for existing infrastructure
	* remote state to enable collaboration (bootstrapping problem)
* terragrunt and abstractions
	* modules (OpenTofu)
	* units (Terragrunt)
	* stacks (Terragrunt)
	* solution to the remote state bootstrapping problem
* deploy a simple web app with a frontend, backend, and database
* final exercise
    * split web app in modules and units
    * deploy app in different environments utilizing stacks

---

Resources

* GitLab Repo: https://gitlab.com/patrickmoelk-consulting/workshops/infrastructure-as-code-with-opentofu/
* GitHub Repo: https://github.com/patrickmoelk-consulting/infrastructure-as-code-with-opentofu/
* Slides: https://patrick-moelk.eu/en/events/workshops/2026-02-04-hands-on-workshop-iac-with-opentofu/

### Foreman UI future - the vision and the strategy
Speakers: Shimon Shtein
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/H7GMM7/
Lately I have published vision and strategy documents to outline the way we want to continue developing Foreman UI. I would like to discuss those documents in more details in a face to face meeting with a broader group.

## 2026-02-04 — B.3.0.32

### Building AI-Assisted Operations: Agentic AI Workshop
Speakers: Engin Diri, Zaid Ajaj
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/DCRWVC/
It's 2am. Deployments are failing. Your team scrambles between ArgoCD, Kubernetes dashboards, and Git history trying to correlate what changed. What if an AI assistant could traverse these tools for you, not just suggesting commands, but actually executing investigations with your approval?

This hands-on workshop teaches you to build AI-assisted operational workflows using Agents supported by MCPs. We're going to create a multi-agent setup that leverages several MCPs (Kubernetes, ArgoCD, GitHub, Pulumi) to autonomously work on classical DevOps and SRE tasks while having a human in the loop for full enterprise compatibility.

**What You'll Build**

Participants will construct a working multi-agent system where:
- Specialized agents handle different operational domains (infrastructure, application delivery, source control)
- Agents autonomously detect configuration drift across Kubernetes namespaces
- Cross-agent coordination correlates ArgoCD sync failures with infrastructure changes in Pulumi
- GitHub integration queries recent commits and proposes remediation PRs
- Human approval gates maintain control over critical operations **Prerequisites**

- Laptop
- Basic familiarity with Kubernetes and GitOps concepts
- GitHub account (for hands-on exercises)

**Setup Requirements**

- Wi-Fi for all participants
- Each participant needs: GitHub personal access token
- Pulumi accounts (free tier sufficient)

**Audience**

Platform engineers, SREs, and DevOps practitioners who want to explore AI-assisted operations beyond chatbot interfaces. Basic programming experience required.

### Prowler - Maximize your Cloud Security Compliance Assessments with Open Source and a pinch of AI
Speakers: Andoni Alonso, Pedro Martin
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/VK3NKE/
Misconfigured cloud resources remain one of the top causes of security breaches, yet manual compliance audits don't scale in fast-moving, multi-cloud environments.

This hands-on workshop dives into Prowler, a powerful open-source tool designed to assess and improve your cloud security posture, with support for AWS, Azure, GCP, M365, Github, Kubernetes and more.  In this workshop, participants will learn how to deploy and customize Prowler to perform automated compliance checks aligned with industry standards such as CIS, GDPR, HIPAA, and more. 

The session will also introduce practical techniques for extending Prowler’s capabilities with (or without) the help from our MCP, and basic AI-assisted analysis to prioritize risks and surface actionable insights.

## 2026-02-04 — B.3.036

### Flox: The power of nix without the pain (mostly)
Speakers: Michael Stahnke
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/MBMLEU/
In this hands-on workshop, we will use Flox to introduce the core concepts and advantages of the Nix ecosystem without requiring participants to learn the Nix language or climb its steep learning curve. We will start by tackling the classic “works on my machine” problem and show how Flox environments create consistent and reproducible setups across laptops, CI systems, and production hosts. After that foundation is set, we will explore advanced environment features such as layering, composition, version pinning, and secret management. These examples will give participants practical patterns they can apply immediately in their own workflows.

Once everyone has a solid grasp of environments, we will move into packaging and deployment. Participants will learn how to build software with Flox, how to manage reproducible artifacts, and how to run those environments reliably using systemd or Kubernetes. Along the way, we will occasionally look under the hood to show where Nix concepts appear and where Flox intentionally simplifies them with more guided workflows. By the end of the workshop, attendees will have working environments, a clear mental model of how Nix-style reproducibility functions, and enough hands-on experience to decide how Flox can improve their current development or automation practices.

## 2026-02-04 — B.3.009

### Modern Network Observability
Speakers: Christian Adell
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/GQYAVR/
Modern networks generate vast amounts of telemetry—but turning that data into actionable insight requires more than dashboards. In this 4-hour hands-on workshop, based on the book Modern Network Observability (Packt), we’ll build a complete observability stack from the ground up using open-source and cloud-native tools.

Participants will explore how to collect, model, and visualize network telemetry using modern protocols and data pipelines. We’ll move from raw gNMI/streaming telemetry to rich network context and analytics, integrating observability directly into automation workflows and CI/CD pipelines.

Through guided exercises and live demos, attendees will learn how to:

- Collect and normalize telemetry using Telegraf.
- Stream and store data in a Prometheus time-series setup.
- Build contextual dashboards in Grafana, correlating metrics, traces, and topology.
- Integrate event-driven insights using Kafka, NATS, or webhooks to trigger network automation.

By the end of the workshop, participants will have built their own working observability lab—capable of monitoring, analyzing, and reacting to changes in a dynamic network environment.

This workshop is designed for network engineers, SREs, and automation practitioners who want to move beyond legacy monitoring and embrace an open, programmable, and analytics-driven approach to network operations.

Lab Requirements:
- Local setup: Python >3.10, Docker, Containerlab
or
- Playbook to deploy a virtual server in Digital Ocean with all the dependencies

### Latest and greatest developments in CUE
Speakers: Marcel van Lohuizen, Daniel Martí, Unnamed user, Roger Peppe
page: https://cfp.cfgmgmtcamp.org/ghent2026/talk/WBGXFJ/
Learn about the latest features of CUE and new ideas on how to organize CUE. As usual, we will use this opportunity to gather much appreciated user feedback. In this workshop we will introduce the latest features of CUE. We also present a new model on how to organize CUE to allow for managing cross-cutting concerns (such as augmenting data and policy) in a scalable.

