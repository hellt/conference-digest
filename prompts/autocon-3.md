>>> HOW TO RUN THIS <<<
This is the digest prompt for autocon-3. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/autocon-3.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/autocon-3.md
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

Below is the program for AutoCon 3 (Prague) (operator). Read it and produce a digest
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
conference: AutoCon 3 (Prague)
type: operator
source_url: https://networkautomation.forum/autocon3
generated: 2026-11-01
registry_key: autocon-3
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Wednesday, 28 May 2025

### Start at the Beginning; Automating Network Design
Speakers: Claudia de Luna
Session: Wednesday, 28 May 2025, 13:15 - 14:00 (Opening Keynote)
video: https://www.youtube.com/watch?v=PoQUA3dgmkQ
This conference has its roots in the premise that, of all the IT disciplines, networking has been a bottleneck to service delivery. Networking has been slow to embrace automation. We talk about operations. We talk about "source of truth". We talk about tools. It’s time to expand our perspective beyond just operations and talk about the start. While there are big wins to be found in operations as we have seen, ignoring the start inhibits profound progress. We struggle with frameworks and a lexicon because most of our experience to date involves starting in the middle. That has shaped certain bad behaviors. For example, the fixation on the "source of truth" stems at least in part from beginning midstream. Until we consider the end-to-end process, we have only part of the map and no clear anchor. We can never go back to the start because we skipped it. I propose shifting the conversation toward design, where every project truly begins. For years, I’ve aimed to move beyond monolithic diagrams and documents that are difficult to consume programmatically. Instead, we should start with patterns, data models, and structured data. Programmatically consumable design data is the foundation. From it, everything else flows—diagrams, documentation, configurations, connectivity, build guides, and work instructions. Here is our first truth, our baseline! This shift has already started, and my hope here is to shine a big bright light on this concept and some of the great work already underway

### Clash of the Titans: Nornir Vs Ansible
Speakers: Suhaib Saeed
Session: Wednesday, 28 May 2025, 14:00 - 14:10
video: https://www.youtube.com/watch?v=tERBjiB-Lv8
This talk will share real-world lessons from leading network automation initiatives using the two frameworks (Nornir Vs Ansible) evaluated head-to-head, with all biases removed. Drawing from hands-on experience, I'll compare technical capabilities, business outcomes, and where each framework excels (or falls short). We'll also look at when it makes sense to move beyond plain Python scripts, and how to choose the right approach for your network and your team.

### Taking Automation to next level: Drive your network with Microservices
Speakers: Shirish Basant Rai
Session: Wednesday, 28 May 2025, 14:10 - 14:40
video: https://www.youtube.com/watch?v=ab0QTB7xTOk
This presentation will walk through Colt Technology’s transformative journey from a simple workflow engine-based architecture to a robust, event-driven microservices model. We’ll explain why the evolution was necessary, detail the considerations that led us to adopt microservices, and demonstrate how our architecture naturally aligned with the TMF ODA NaaS standards. Attendees will gain insights into the scalability benefits, separation of concerns, streamlined code promotion without service disruption, and the acceleration of development cycles—all while hiding the underlying complexity of asynchronous workflows and service orchestration.

### Making Network Automation Consumable: A Junior Engineer's Perspective
Speakers: Emre Cinar
Session: Wednesday, 28 May 2025, 15:25 - 15:55
video: https://www.youtube.com/watch?v=Tn_EvoEc6vU
As a Junior Engineer, the consumability of a network automation tool can really make or break your experience. Some incredibly smart engineers and developers build amazing tools for specific use cases, but they can be tough to use unless you know all their quirks. This is especially frustrating when you're just starting out. That is why I want to share my first small project I worked on including all the applications I used and what I learned from it. Fancy tools are great, but at the end of the day, someone has to actually use them—both now and in the future, right?

### A Marathon and Not a Sprint: Lessons Learnt from Trying (and sometimes succeeding!) to Automate Enterprise Campus Networks
Speakers: Robert Mertling-Blake
Session: Wednesday, 28 May 2025, 15:55 - 16:25
video: https://www.youtube.com/watch?v=1k-3oECPaK8
Network automation is a journey - but often some of the biggest obstacles aren't technical - and these can seem overwhelming in campus networking where there's often very little homogeneity between devices and locations compared to trying to automate cloud, data centre and service provider networks. This is a 'story so far' going through the drivers, the hurdles and successes in our journey in adopting automation across multiple campus networks – covering the wins and challenges trying to automate and assure networking in AEG's entertainment venues worldwide, both in new venues as well as existing venues (where change has to happen around a packed events schedule).

### Coding for infrastructure is just coding, on how we moved from a script based model to an object oriented architecture
Speakers: Antonio Balmaseda & Alberto Villegas Erce
Session: Wednesday, 28 May 2025, 16:25 - 16:55
video: https://www.youtube.com/watch?v=rtzYbAPlkAs
In our quest to automate the Roche Pharma optical network (same devices also used by, for example, ESnet and GEANT), we hit roadblocks both with Ansible/AWX and with the vendor's controller. While Ansible worked for basic device upgrades, it turned out to be harder than other general-purpose programming languages because of no dedicated Ansible modules ensuring idempotency. Regarding the vendor's controller API, we soon realized that it is a stripped-down version of the GUIs' functionality, thus missing important features we needed and forcing us to compromise or wait months for updates. In the end, we started adopting the Workflow Orchestrator last November. Rather than trying to automate everything at once, we took an incremental approach starting with the most important and widely deployed services. We created abstract service models, built Python clients to communicate directly with the devices (using RESTCONF, except for ROADMs requiring TL1 shell), and developed workflows such that changing the hardware simply requires adding implementations to existing functions (using Python’s single-dispatch approach). This gives us clear boundaries between abstract intents and device configurations while easing expandability and adaptability. No more scattered playbooks or vendor-specific solutions! Currently in lab testing, our solution is expected to be in production by the conference date. In general, when talking about this approach with the packet network colleagues, I find a s

## Thursday, 29 May 2025

### The Road to EVPN: Automated Service Migrations
Speakers: Luke Gollan
Session: Thursday, 29 May 2025, 9:10 - 9:40
video: https://www.youtube.com/watch?v=dyeclGDa6yU
The Story of Megaport's automated EVPN Deployment Across a Global Telco Network. From the initial network/automation architecture phase, to the automated network config rollout, and finally to migrating services to EVPN. Automating a productive and smooth transition to EVPN across a global telco network. Streamlining service migrations for a seamless transition, ensuring minimal disruptions for customers. Generating simple and intuitive tools for our customers and support teams to use for service migrations. How to use an object driven database for generating device configurations. Leveraging different Netconf operations to configure, log, and track config changes. How using diversity zones can minimise unexpected impacts. Incorporating APIs and message queuing to trigger service migrations. Having clear, detailed steps of the migration process, including a clear rollback plan is a good base for a successful rollout. Testing is crucial when it comes to ensuring you are very familiar with each phase of the rollout, including rolling back. Ensuring you have the right tools for tracking network changes. Making sure business stakeholders have at least a high level overview of the changes being made, the risks associated, and rollback plan.

### From Clicks to Code: Optical Network Automation Journey at GARR
Speakers: Matteo Colantonio
Session: Thursday, 29 May 2025, 9:50 - 10:20
video: https://www.youtube.com/watch?v=5ZhNN28xgmo
This presentation outlines GARR's ongoing journey to automate its optical network. We'll share our initial experiences with Ansible/AWX and vendor controllers, highlighting the significant limitations encountered. The lack of dedicated modules in Ansible proved cumbersome, while the vendor's API offered limited functionality compared to its GUI. Recognizing these roadblocks, we pivoted last November to the Workflow Orchestrator framework, pursuing incremental automation starting with critical services. By designing abstract service models and developing clients for direct device communication, we created workflows that separate intent from device-specific configurations. This approach ensures adaptability and expandability to new devices, eliminating scattered playbooks and vendor-specific solutions. While currently in an early alpha testing phase in production with substantial development ongoing, this architecture shows significant promise. This talk also offers insights that may inspire new approaches for those automating packet networks, which often rely on intricate configuration templates in contrast to optical networks historically managed through GUIS. Though slow and tedious, GUIs avoided heavy CLI dependency, offering a unique starting point for automation.

### Transforming Network Automation with Temporal
Speakers: Naveen Achyuta
Session: Thursday, 29 May 2025, 11:05 - 11:35
video: https://www.youtube.com/watch?v=1PqbtACGW80
Temporal has emerged as a powerful workflow engine across industries, valued for its state management, instrumentation, durability, and human-in-loop capabilities but yet remains underutilized in networking. This presentation introduces Temporal to the networking industry, outlines its architecture, showcases successful implementations in other sectors, and demonstrates various network automation use-cases. Attendees will learn how Temporal can solve common challenges in network operations through its robust orchestration framework, potentially transforming how we approach configuration management, service provisioning, automated remediation workflows and more.

### An Epic Journey: Automating networks with Terraform
Speakers: Eduardo Pozo
Session: Thursday, 29 May 2025, 11:45 - 12:15
video: https://www.youtube.com/watch?v=xlacAhxHQgM
This talk follows the journey of using Terraform as the primary tool to automate critical network infrastructure (on oil, health, and enterprise projects) and migrate a large-scale, multi-site data center to a fully automated deployment. A story with what worked, what didn’t, and the challenges encountered. Key topics include navigating limited vendor support and bugs, using Git/NetDevOps/pipelines with a stateful tool, data transformation, the pros and cons of a stateful approach to automation, and the process of scaling these tools. Along the way, we will explore solutions, lessons, and insights for approaching similar automation projects.

### How We Eliminated Security Vulnerabilities with Network Automation—And That’s Just the Beginning!
Speakers: Lee Harper
Session: Thursday, 29 May 2025, 13:45 - 14:15
video: https://www.youtube.com/watch?v=iXglcgf5BS4
When the network team at Terracon Consultants began its automation journey, the network was in a very sad state. With over 120 locations across the continental United States, the network equipment at each location was often left with the OS that was installed when it shipped, and variations in configuration were too common. On those occasions when a bug or critical need required pushing changes, it was often a multi-day project for the 4-member team. The introduction of Gluware in 2019 was a game-changer. The team was able to standardize configuration and OS versions across all their locations. Implementation of configuration changes dwindled down to a few hours in a single night. This freed up man-hours for more proactive projects, including further implementing features in Gluware. Overall, automating with Gluware allowed Terracon to increase locations by over 50%, do a complete network stack refresh and move to SD-WAN, and decrease findings on the annual cybersecurity insurance audit from over 30 to 9. This was all done while only adding a single team member that was dedicated to firewall management. Join Lee Harper, enterprise administrator at Terracon Consultants, as he discusses how Terracon accomplished these changes and how they are utilizing Gluware for even more, including: CIS (Center for Internet Security) benchmark audits, real-time device audits, and free-form automation with Network RPA.

### Network Event Correlation. Stories to keep you awake
Speakers: Javier Antich
Session: Thursday, 29 May 2025, 14:25 - 14:55
video: https://www.youtube.com/watch?v=FaCafKfnQ_4
Network Event correlation is a history of frustration and misconceptions. Let's open up and discuss the different approaches to operational noise reduction (i.e. event correlation. Let's uncover how they work and why they mostly do not work well. Let's be completely honest at what they can do and what they cannot. Let's explore how we can do better. And yes, Al has a role on it. We can do much better to help network operation engineers deal with the noise. Let's review how event correlation works today, and how it should be in the future.

### Mastering Network Operations: The Power of Abstraction
Speakers: Jaakko Rautanen
Session: Thursday, 29 May 2025, 15:40 - 16:10
video: https://www.youtube.com/watch?v=gDBvYY6pBng
By thinking of networking concepts—such as devices, cables, and configurations—as services, we’ve achieved higher levels of abstraction. Daily operations become faster and easier when performed at this abstract level. Services are carefully modeled, hiding complex details under the hood. This transforms each abstracted service into a ‘Lego block’—simple to understand and effortlessly connect with others. The result? A ‘design once, use repeatedly’ approach that boosts efficiency and scalability.

### The Why, What, and How about Design-Driven Automation
Speakers: Christian Adell Querol
Session: Thursday, 29 May 2025, 16:10 - 16:40
video: https://www.youtube.com/watch?v=0sQPqpohEuo
Structured data is widely recognized as essential in the evolving landscape of network automation. However, traditional approaches often focus on managing individual data objects rather than treating network elements as cohesive entities. A design-driven approach to data governance shifts this paradigm, grouping related data meaningfully to simplify network management. This session will explore the key principles behind design-driven network automation, highlighting how it enables intuitive workflows, reduces complexity, and accelerates adoption. Attendees will gain insights into practical implementation strategies that provide engineers and users with a streamlined entry point—minimizing required inputs while dynamically expanding data according to the network’s design. By the end of this talk, participants will understand how to move beyond theoretical best practices and apply a structured yet flexible approach to real-world automation challenges.

## Friday, 30 May 2025

### From the CLI to API and IDE: A Tale of the Network Engineer
Speakers: Jason Edelman
Session: Friday, 30 May 2025, 9:10 - 9:55 (Closing Keynote)
video: https://www.youtube.com/watch?v=I7vHnKbCOc0
The skills of the network engineer have fundamentally changed over the past decade. What was once dominated by the CLI has evolved into a landscape driven by APIs, IDEs, and automation. This shift represents more than just new technologies-it's a radical change in how network engineers work, think, and solve problems. Looking back on discussions, open source projects, and tools that have shaped this evolution, we can draw lessons that point to and shape the future. And with Al's growing role in network automation, transformation is only accelerating. This talk will celebrate the past and embrace the future, so we can march toward the goal we all dream about a world with truly automated networks.

### Building Trustworthy Network Automation, From Principles to Practice
Speakers: Damien Garros
Session: Friday, 30 May 2025, 9:55 - 10:25
video: https://www.youtube.com/watch?v=G3XqT-UhQ6Q
Trust is essential for successful network automation adoption. When automation platforms exhibit predictable behaviors and transparent processes, teams can confidently delegate critical network operations. Building trustworthy automation doesn't happen by itself, it needs to be baked into the design of every workflow. This technical session examines core principles that build trust, including idempotency, declarative workflows, and robust version control. Using practical examples from production environments, we'll analyze how specific technical decisions affect automation reliability and team confidence. The presentation covers key implementation patterns like state verification, diff-based changes, and failure handling. Attendees will learn concrete approaches for building automation platforms that network teams can trust and rely on daily.

### Using a SONiC Abstraction API (for fun and profit)
Speakers: Josh Saul
Session: Friday, 30 May 2025, 11:10 - 12:00 (Lightning Talk)
video: https://www.youtube.com/watch?v=Mf6uLZZtwFs
SONiC comes in many flavors, often presenting challenges for DevOps practitioners who want to support multiple vendors in their cloud and AI infra provisioning stack. In this demonstration, we will show how traditional IaC tools can use abstractions to generate actual device configurations across multiple SONiC platforms, including methods such as gNMI and SNMP/CLI.

### Automation Transforms $70 APs into Enterprise-Grade Networks
Speakers: Henry Haller
Session: Friday, 30 May 2025, 11:10 - 12:00 (Lightning Talk)
video: https://www.youtube.com/watch?v=vVrjvB6QTYQ
This talk showcases automation features developed in order to support the entire lifecycle of running Wireless LANs (WLANs) on commodity hardware from the adoption of the Wireless Access Points (WAPs) into a command and control system to provisioning of the actual WLANs. The OpenWiFi Gateway (OWGW), which is deployed as a VM with custom bootstrapping logic, and the OpenWiFi WAPs both run open source software from the Telecom Infrastructure Project (TIP). The onboarding lifecycle involves generating SSL certificates on these devices and sending those certificates to a Certificate Authority for signing, then using these certificates for mutual authentication between the OWGW and the WAPs via mutual Transport Layer Security (mTLS). This creates a web of trust between devices in the environment. Management of the Certificate Authority for this purpose is also included. After the WAPs are onboarded, they must be provisioned with configuration based on operator intent. This is accomplished via JSON API transactions with the OWGW and Websocket transactions between the OWGW and the WAPs. This means that many WLAN configuration options, e.g., Open, Pre-Shared Key (PSK), multiple Pre-Shared Key via Remote Authentication Dial In User Service (mPSK-RADIUS), hidden, 2.4/5/6 GHz, WiFi Protected Access 2/3 (WPA2/3, including transitional WPA), tunneling via Generic Routing Encapsulation (GRE) and Opportunistic Wireless Encryption (OWE), are operator-configurable parameters that get translat

### Going beyond show commands and screen scraping with BMP
Speakers: Bart Dorlandt
Session: Friday, 30 May 2025, 11:10 - 12:00 (Lightning Talk)
video: https://www.youtube.com/watch?v=MgK2YSfTvD8
With the automation around configuration generation and deployment already in place. It was the desire to present back to the customer that the BGP prefixes configured to be advertised were arrived as such. Though not only that, but also accepted through the policy. I will take you on the journey from where some felt that screen scraping was a good idea, to the current solution using BMP (BGP Monitoring Protocol). The chosen architecture, the challenges faced with the amount of data that comes with BGP and how we dealt with them. If you were looking on how to deal with your BGP data, especially your pre policy data, this should kickstart your adventure.

### Pls stop exposing your... secrets
Speakers: John Howard
Session: Friday, 30 May 2025, 11:10 - 12:00 (Lightning Talk)
video: https://www.youtube.com/watch?v=-_qMVdsOq8g
In the beginning it was you and your laptop. It was a simpler time. Then other people got involved and you have to not only comment this and document that, but now you have DevSecOps pipelines calling you an imbecile as well. As you look around you find hard coded creds everywhere and "verify=False" on every REST call you make. All those time saving scripts are suddenly looking a lot like technical debt. In this lightning session we will take a whistle stop tour of a handful of useful features found in the secrets management tool known as Vault. We will create a PoC instance and leverage a couple of the built in engines to solve these challenges in a way that scales, and improves your security posture, so that you too can stop exposing your... secrets. ;)

### Teaching "old" LLMs new tricks
Speakers: Urs Baumann
Session: Friday, 30 May 2025, 11:10 - 12:00 (Lightning Talk)
video: https://www.youtube.com/watch?v=X073YnquOho
Fine-tuning Large Language Models (LLMs) for network automation tasks requires substantial resources. However, Low- Rank Adaptation (LoRa) provides a lightweight and efficient alternative. In this lightning talk, we will examine how LoRa fine-tuning can significantly enhance the accuracy of LLMs for specialized automation tasks without the necessity for extensive computational power. We will also outline a practical fine-tuning pipeline.

