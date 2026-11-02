>>> HOW TO RUN THIS <<<
This is the digest prompt for ciscolive-eu-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ciscolive-eu-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ciscolive-eu-2025.md
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

Below is the program for Cisco Live Europe 2025 (Amsterdam) (vendor). Read it and produce a digest
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
conference: Cisco Live Europe 2025 (Amsterdam)
type: vendor
source_url: https://www.ciscolive.com/on-demand/on-demand-library.html?search.event=1737762187215001jsy4
generated: 2026-11-02
registry_key: ciscolive-eu-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## 2025 Amsterdam

### AIOPS for Cisco Secure Firewall: Enhancing Operational Efficiency and Security - PSOSEC-2151
Speakers: Gayathri Nagarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098472728001deZx
In the face of increasing network complexity and evolving cyber threats, effective firewall management has become a critical concern for organizations. Managing firewalls remains a complex and challenging task for IT and security teams. This session provides valuable insights into the vision and strategy behind AIOps for Cisco Secure Firewall. AIOps, with proactive insights and recommendations, helps in enhancing security posture and achieving operational efficiency. Delivered directly by product management, the session provides an opportunity to engage and comprehend the innovations steering AIOps. Participants will gain understanding of leveraging AIOps' proactive insights for reduced downtime, minimized misconfigurations, and lowered OPEX.

### Enhancing Day 2 Operations with Cisco Compute and Ansible Automation - DEVNET-2066
Speakers: Massimo Ferrari (Red Hat), Chris O'Brien (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098436350001dLpp
Join us for an insightful technical session as part of the Cisco Validated Design program, focusing on optimizing Day 2 operations using Cisco Compute Solutions for Converged Infrastructure and Red Hat's Ansible Automation Platform. This session is tailored for IT professionals looking to streamline their infrastructure management through automation. We will explore advanced capabilities for network configuration, storage integration, and virtualization enhancements, showcasing how to achieve minimal disruption and maximum operational efficiency. Our expert speakers will provide a comprehensive overview of best practices and innovative solutions that empower you to handle operational complexities with ease and confidence. Don't miss this opportunity to enhance your skills and leverage validated designs to optimize your IT environment.

### Fostering an Agile Leadership Mindset - ITLGEN-1509
Speakers: Adele Trombetta (Cisco), Oliver Tuszik (Cisco), Fletcher Previn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098459174001dc5P
As we stand on the brink of unprecedented technological transformation, the role of leadership is being redefined. Join us for a dynamic panel discussion featuring top executives from Cisco as they explore the evolving landscape of leadership in the age of AI. This session will delve into how leaders can adapt to rapid changes, manage global workforces, and leverage AI to drive business transformation. Oliver Tuszik will moderate a conversation with Fletcher Previn and Adele Trombetta, who will share their insights on fostering an agile leadership mindset, reskilling teams, and retaining talent in a digital-first world.

### Let Generative AI Agents Do the Work for You - DEVNET-1736
Speakers: Flo Pachinger (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098434892001ddeW
This session aims to give you a fundamental overview of generative AI agents and how you can use them with Cisco technologies. At first, the latest research on generative AI will be covered, including large language models (LLMs), prompting, vector databases, and fine-tuning. The main focus will be on generative AI agents and AI agentic frameworks. You will learn how you can build and use LLM-powered agents. Various use-cases will be presented along the way and will give you an inspiration of how you can use AI agents to do the work for you.

### Navigating the Return to Office: A Collaborative Approach - ITLGEN-1504
Speakers: Kieran Higgins (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098458260001dMBv
As organizations transition back to the office post-pandemic, the collaboration between IT, Facilities, and HR is crucial for a successful workplace transformation. This Cisco Live session will discuss strategies for rebalancing space to support hybrid work models, enhancing employee health and wellness, and digitizing real estate platforms to meet sustainability goals. Join us to learn how to leverage technology and cross-departmental partnerships to navigate the complexities of returning to the office and building a future-ready workplace.

### SAN Congestion Management and SAN Analytics - BRKDCN-2942
Speakers: Ed Mazurek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294584001d2Up
Demand for storage is growing at an unprecedented pace. At the same time, the demand for high performance is driving an increased need to understand and detect issues before they become a problem. This session covers the most common issues observed in modern Storage Area Networks (SANs) and introduces the latest Cisco innovations to help you detect, identify, and most importantly, prevent congestion from happening. Furthermore, you will learn how to utilize the latest innovations with MDS switches, SAN Analytics, and Nexus Dashboard SAN Insights to answer the toughest questions SAN administrators face today, such as how to identify the root cause of performance issues, pinpoint the source of link over-utilization, and predict congestion before it ever occurs.

### Simplify the Analyst Experience by Harnessing AI and Machine Learning - BRKSEC-2786
Speakers: Craig Saunderson (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098378695001d7nL
Discover how generative AI and large language models (LLMs) can revolutionize your security investigations. This session explores the future of AI in security operations and shows how it can streamline complex tasks, making them more accessible - even for SOC analysts with little to no Splunk experience. Learn how AI can empower your team to handle sophisticated incidents with greater speed and efficiency. If you're ready to see how AI can transform your security workflows, this session is a must.

### Stop the Chaos, Organize your Network with NSO and Netbox - DEVNET-1506
Speakers: Anna Wojcik (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098433438001dnhX
Deploying new devices, updating or decommissioning them requires network admins to make changes in device's configuration, IP reservations, database etc. On top of that, all the changes should be documented for future reference. Having a single and consolidated network source of truth can bring numerous benefits and allow for automation of some of required tasks. NSO provides automation and orchestration solutions towards hybrid multi-vendor networks. Add an open source Netbox on top of it, and get all the benefits of a single source of truth. This session will focus on use cases of NSO and Netbox working together, with examples of the integrations and demos, focused on NSO and Netbox API.

### Webex Troubleshooting Superpowers with ThousandEyes and Meraki Integrations - BRKCOL-2662
Speakers: Paul Giralt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098284106001djna
Cisco Webex Control Hub offers valuable insights into media quality issues, but understanding the underlying cause of these issues can be elusive. ThousandEyes and Meraki Dashboard, providing unrivaled network-level visibility, but until now, have not had an easy way to correlate network events with media quality events. By seamlessly integrating Webex with ThousandEyes and Meraki Dashboard, you gain unparalleled visibility into your Webex traffic, empowering you to swiftly identify and resolve any challenges that arise. Join us for an enlightening session as we delve into the art of media quality troubleshooting within Webex Control Hub. Discover how the integration of ThousandEyes and Meraki Dashboard elevates your troubleshooting capabilities by incorporating additional telemetry into Control Hub. With real-world examples, we will showcase how these integrations can effectively help diagnose and address real-world issues.

### -40C Industrial Networking: Where Enterprise Products Fear to Go - BRKIOT-2104
Speakers: DJ Cole (Cisco), Emmanuel Tychon (Cisco), Albert Mitchell (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161407724001N4EX
Why does Cisco even have Industrial Networking? Cisco has lots of Ethernet Switching, Routing and Wireless (not just wifi) products. This session will cover why Industrial Networking devices exist. What makes them 'industrialized'? You may have a use case and not even know it. Cisco Industrial Networking devices leverage the same Enterprise technology and features whenever possible. This session will compare the Industrial, and Enterprise products pointing out the differences and similarities. The similarities are what make the industrial products easy to manage. The differences are the reasons Enterprise products need to stay indoors where it's safe. Underlying intent is to provide guidance to the network administrators and solution architects in where and how to deploy Industrial Ethernet as opposed to enterprise equivalent. We'll share interesting use cases where Industrial Networking products are brave enough. Products covered: IE3400, IE3300, IE3200, IE3100, IE9300, IW6300, IW9165, IW9167, IR1101, IR1800, IR8140, IR8340

### 1 to 100: Master All Steps of Deployment, Seamless Integration, and Migration of Large SDA and SD-WAN Networks - BRKENS-3834
Speakers: Jennifer Bowman (Cisco), Dhrumil Prajapati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098303312001dozM
Do you know what it takes to plan and migrate a site of any size to Cisco SD-Access and SD-WAN network at scale? This session explains just that. We will cover every bit of detail involving how to deploy, seamlessly integrate, and migrate SD-Access and SD-WAN networks at scale in large enterprise networks. This session will demonstrate the key fundamentals in designing, deploying, and operating a software-driven network at scale. Key concepts include creating modules and prescriptive handoffs, transport considerations, security, migrating the brownfield environment from circuits to change controls, and how automation will bring you scale. In the end, you will walk away with a comprehensive plan to start your SDA and SD-WAN journey.

### 10 Steps to Architecting your Webex Contact Center Solution - BRKCCT-2504
Speakers: Carles Duz Palau (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098276169001dOnE
Keeping up with today's customers means delivering a top-notch service. That's why a powerful, flexible contact center is essential. Cisco Webex Contact Center is that tool. It's a cloud-based platform that helps businesses wow customers, boost agent performance, and streamline operations. Want to know how to build a killer Webex Contact Center? Join us for a use case based session where we'll walk you through ten crucial steps. Whether you're starting from scratch or already migrating your contact center, this session is designed to provide you with a structured approach to solution design. This session is for you if you're an IT leader, contact center manager, or solution architect looking to supercharge your customer service game. Learn how to design a world-class contact center that drives business success.

### 4 Steps to Unlock Location Based Intelligence from your Wi-Fi Network with Cisco Spaces - BRKEWN-2718
Speakers: Rosario Medrano Pena (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161405090001Nou3
Discover how to maximize your Wi-Fi network's potential with location-based intelligence and Cisco Spaces. We will cover the essentials of Location Services RF technologies, mastering maps and antenna placements, various deployment options, and their outcomes. Whether you're struggling to use your IT infrastructure for detecting rogue endpoints, curious about leveraging our APIs, or interested in enabling use cases such as occupancy, asset tracking, and environmental monitoring, this session is for you. Join us to enhance your network's capabilities and unlock new possibilities!

### 4 Ways to Cut Your Energy Use with PoE - PSOENT-1862
Speakers: Veera Bhaskar Mutyala (Cisco), Jeff Meek (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098468875001dtWC
In this session, we'll discuss the impact Power over Ethernet (PoE) can have on energy consumption. We'll explore how Cisco has achieved energy savings of up to 37% in its own offices by using the network to power operational technologies like lighting and blinds, while laying out the partner landscape and discussing the potential for PoE technology in the future. We'll even dive into the sustainable side of Cisco switches and access points, including visibility, flexibility and intelligence around power management and consumption in features like auto-off and much more.

### 400G, 800G, and Terabit Pluggable Optics: What You Need to Know - BRKOPT-2699
Speakers: Mark Nowell (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098360350001d2Hf
Optical interfaces are fundamental in our networks, and the technology is always being pushed to higher speeds. New developments happening in this space will enable the next generation of higher-capacity networks. This session will provide participants with insights into the current trends and the next development areas for high-speed optical interconnects, what is driving the development, and what the priorities are for success. The session will focus on these following areas: Current 400G pluggable optics technologies and their applications Next-generation pluggable form factors for 800G and 1.6T (including their breakout use cases) New 800 Gb/s and 1.6 Tb/s Ethernet standardization Next-generation optical co-packaging developments for integrating optical interfaces into ASICs The session will cover both coherent and noncoherent optics and will target participants with a working knowledge of deploying optical interfaces and modules. Finally, we will also highlight some of the implications to the systems and networks that incorporate these optical interfaces.

### 5 Tools You Should Learn to Level Up Your Network Automation Game - DEVNET-2149
Speakers: Quinn Snyder (Cisco), Kareem Iskander (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098438915001dtdN
So, you're on the journey to becoming a DevNet Expert, huh? You've got the lowdown on Python and APIs for network wizardry. But now, it's time to kick it up a notch and dive into some real-deal industry tricks to boost your automation mojo. Meet Kareem and Quinn, two jabronis who've done it all from network engineering to software development. Hang out with these two cool cats as they spill the beans on the top 5 gotta-know tools to rock your way to becoming a DevNet automation guru!

### 5 Ways to Deploy Scalable , Secure AND Cost Sensitive Industrial IoT Solutions for Customers using Cisco Catalyst SD-WAN ! - BRKIOT-2990
Speakers: Nipun Jain (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098333020001dvqc
Utility customers and Public Service (transport, mass transit) customers need a massively scaling network automation and security. How do we address the cost aspect of such solutions? How do we optimize for rising costs of data usage under cellular plans for IoT customers? How do we plan the network and topology for maximum connectivity and minimal cost and downtime. These issues have traditionally not been a concern for enterprise customers and hence we want to tackle these for IoT customers specifically, through a technical breakout. The session will address new optimization in SD-WAN for reduced bandwidth usage, tackling network planning for optimizing which WAN circuits to use under certain conditions for IoT customers, and finally how to create and plan for the right network topology for optimal network management . At the end of this session, an IT or OT administrator should be able to deploy Industrial IoT routers at scale, efficiently and with minimal operational cost increases .

### 5G Non-Terrestrial Networking using Cisco Converged SDN Transport - BRKSPG-1583
Speakers: Shahid Ajmeri (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161413402001NRUL
As mobile communication technology advances, seamless global coverage becomes essential. To address coverage gaps and meet the demand for high-speed internet, the 3rd Generation Partnership Project (3GPP) has proposed non-terrestrial networks (NTNs) for mobility. NTNs offer a cost-effective, flexible solution for providing global wireless connectivity. However, to realize its full potential within 5G ecosystem requires collaboration among satellite operators, service providers, equipment vendors, and system integrators to ensure efficient deployment and management. This collaboration is key to unlocking the full benefits of NTNs and enabling sustainable global connectivity. In this session, we will outline Cisco's strategic initiative to develop a blueprint architecture that enables satellite operators and service providers to deploy 5G Xhaul, SD-WAN, and IoT services over non-terrestrial networks.

### 5G Security: Why and How? - BRKSEC-2763
Speakers: Oussama Naffati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098378318001dbZL
There's a popular myth that 5G networks are secure by design, but is that really the case? Join this session to uncover the reality of 5G security, including real-world attacks and challenges facing 5G networks today. Understanding the challenges is just the first step. The real question is: how can we effectively secure these networks against modern threats? Whether you're a security engineer curious about how breaches occur in mobile networks, or a mobility engineer seeking insights into the security challenges and solutions for 5G, this session is for you. Let's dive into the "why" and "how" of 5G security together!

### 7 Habits for Optimizing Your Cisco Catalyst Center Environment - BRKOPS-2416
Speakers: Lila Rousseaux (Cisco), Adam Radford (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098351986001d4bB
There is a massive focus on network automation and visibility through network insights. Successful adoption requires technical, operational, and process changes. How do you maximize benefit and minimize risk when adopting Cisco Catalyst Center? This session gives some tips to achieve success when leveraging Cisco Catalyst Center: Habit 1) Understand Cisco Catalyst Center Resiliency and Tailor the Design to Your Environment Habit 2) Master Device Lifecycle Management: Support, Replacement, and Refresh Habit 3) Keeping software current - simplified software upgrades Habit 4) Automate Your Wired and Wireless Infrastructure for Greater Efficiency Habit 5) Stay Ahead of Problems: Use Telemetry to Identify Issues Before Users Do Habit 6) Drive Operational Transformation with AIOps Habit 7) Elevate Your Automation Game with APIs and Integrations The presenters have 16+ collective years of experience with customers and partners deploying Cisco Catalyst Center and will share their experience and best practices. The session includes a mix of presentation and demo. This session does not cover SD-Access.

### 7 Steps: Master the Art of Unifying Multicloud Secure Connectivity and Design - Cisco SD-WAN + Multicloud Defense - BRKENT-2283
Speakers: John Clark (Cisco), Prashant Tripathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098308333001dZJn
Cisco SD-WAN seamlessly orchestrates connectivity, enabling access to workloads across multiple clouds. Through native integration with leading cloud service providers like AWS, Azure, and Google Cloud, as well as middle-mile providers such as Megaport and Equinix, it ensures secure inter-site/inter-region connectivity. The solution integrates with AWS Cloud WAN, leveraging Transit Gateway architecture, collaborates with Google NCC for Google Cloud connectivity, and utilizes Azure's vWAN and vHUBs. Inter-cloud SD-WAN connectivity between diverse cloud providers is facilitated by SD-WAN Gateways. With the powerful addition of Multicloud Defense, the solution delivers comprehensive security, unifying policies across AWS, Azure, and Google Cloud for on-demand protection of workloads and inter-cloud traffic. This paves the way for converged multi-cloud networking and security

### 7 Ways to Fail as a Wireless Expert on Wi-Fi 7 - BRKEWN-1770
Speakers: Steven Heinsius (Comstor), Dan Jones (Hamina Wireless), Sofya Strunskaya (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161401639001NULg
Have you ever heard of a session called '7 Ways to Fail as a Wireless Expert' ? Good news: IT'S BACK, and it's better than ever! This session dives into the most common pitfalls in Wi-Fi network design and deployment, this time with a Wi-Fi 7 focus. Why would you want to learn how to fail? Knowing what can go wrong makes it that much easier to get it right. And, let's be honest, the "fails" are a lot more fun to talk about! Join us for a session that's informative and entertaining. You'll gain insights not only to prevent common errors but also to justify the critical investments your network deserves. If you are a seasoned Wi-Fi Expert, I'm pretty sure we won't teach you anything new But you'll still be entertained. But if you have a different Networking or Software background, and want to learn about Wireless Technologies, you'll leave with key perspectives on what's working (and what's not) in Wi-Fi 7. In this session, we'll cover: A rapid-fire recap of Wi-Fi history and key terminology The 7 "Fails" to avoid in Wi-Fi 7 deployments Best practices and insights from real-world deployments And if you don't tell anyone we will also give you a sneak peek at what's next in Wi-Fi technology Join Sofya Strunskaya & Steven Heinsius for an hour of learning, laughter, and insights into making the most of Wi-Fi 7. See you in the room!

### 7 Ways to Fail with Cisco Catalyst SD-WAN... and How to Prevent That - BRKTRS-3241
Speakers: Denis Kodentsev (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098395301001dl3G
As it is widely known, a key Cisco SD-WAN's advantage is the architecture, which keeps the solution's moving parts interconnected, yet decoupled. This prevents issues in the control-plane to affect the data-plane, and vice-versa. The approach translates into enterprise-class domain fault isolation, and eventually into high scalability. What is not that widely known, is that with certain customer's configurations, these built-in guardrails of decoupling may be silently weakened.. or even completely disabled. This could happen for a very valid reason and not by any mistake, yet will disable most (if not all) fault isolations in a Cisco SD-WAN network. The session explores 7 real-life customer case-studies with Cisco TAC illustrating configurations and design decisions which led customers into trouble. We will investigate every each case on what configuration led to a fail or an outage, why it wasn't prevented by embedded fault-isolation, and how exactly it could be prevented in your network if by any chance you're looking to implement similar configuration/design. As part of the session, we will cover details on Cisco SD-WAN control-plane and data-plane well-known, and not-so-well-known, dependencies which are essential for keeping fault isolation in Cisco SD-WAN up and running. The topic of dependencies will be explored from both network-wide and system-level perspectives, providing a holistic view on Cisco SD-WAN fault isolation architecture.

### A Better Wi-Fi 7 Blueprint: Designing Future-Proofed Wireless Networks - CENEWN-1338
Speakers: Simone Arena (Cisco), Vivek Menon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228646035001sQwr
Cisco Wi-Fi 7 brings new experience opportunities to every industry with more bandwith, tighter security, and better performance across the board. But, what considerations should you account for when planning for Wi-Fi 7? What are the design implications of 6Ghz, UWB, and the opportunities Spaces and location-based services can bring to your campus and branch? Join our wireless and spaces experts in this Center Stage session and get an architect's view of how organizations are redesigning their wireless networks to take advantage of Wi-Fi 7's increased density, new hyperlocation services with Ultra Wideband, and better ways to assure and optimize your wireless experience with AI.

### A Developer's Introduction to Splunk Observability Cloud - DEVNET-2366
Speakers: Greg Leffler (Splunk)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098442842001dl3a
Observability offers a lot of benefits - faster MTTD, better understanding of your architecture, and the ability to find root causes faster, but getting started can be tough - and understanding exactly what observability tools can do for you can be even harder. In this session, you'll learn how to instrument applications to send data into Splunk Observability Cloud with zero code changes. Starting with an overview of observability in general, next, you'll see a demo of our automatic OpenTelemetry instrumentation for a Java app. Finally, you'll see a troubleshooting workflow in Splunk Observability Cloud, highlighting the use of Splunk APM and Splunk Log Observer Connect to quickly isolate a problem to the root cause.

### A Hands-On Guide To Cloud Infrastructure Monitoring - DEVSKL-1550
Speakers: Abdiel Hernandez Fentanes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098451798001dbvu
In today's world, cloud infrastructure obfuscation is a prevalent trend. This has created a significant challenge in maintaining visibility over cloud environments, which is crucial for identifying and resolving issues with cloud workloads. Attendees will learn how to effectively monitor their AWS Cloud environments by leveraging traffic flows and correlating configuration changes with availability and performance of cloud-deployed workloads, services, and applications. This session will provide a clear strategy for achieving this level of monitoring. This session is ideal for Site Reliability Engineers (SREs), IT network engineers, cloud engineers, and other professionals involved in managing and monitoring cloud infrastructures. A solid understanding of cloud infrastructure and basic experience with AWS Cloud services is expected. Familiarity with monitoring and troubleshooting cloud environments will be beneficial. Experience a live demonstration of how ThousandEyes Cloud Insights can be used to monitor and resolve issues in AWS Cloud environments in a single view across all owned and unowned environments and increase Mean Time to Resolution. This session will provide a comprehensive walkthrough of the configuration steps required to deploy an effective cloud monitoring strategy. Following this, we will transition into a session on how to automate it. Please note that there will be a 15 minute break between sessions. If you attend the first session (and stay seated for the break), you may keep your seat for the second session.

### A Network Engineer's Blueprint for ACI Forwarding - BRKDCN-3900
Speakers: Joseph Young (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098297267001deXI
As the Cisco Application Centric Infrastructure (ACI) list of features continues to expand and encompass more data center architectures, it is more important than ever to have a good understanding of how a packet is forwarded end to end. This session will provide a deep dive into how ACI forwards traffic. Important questions that will be covered include: How do the basic forwarding mechanisms in ACI work (VXLAN, TEP reachability, end point learning, etc.)? In what ways does ACI forwarding differ from legacy environments? What do the forwarding-related configuration options do? How can an engineer effectively prove what is happening to a packet? At the end of this session attendees should be able to explain in detail how ACI would handle a specific flow as well as use available tools to debug and verify what is happening. Attendees should already have a deep understanding of routing and switching fundamentals in legacy environments and knowledge of basic ACI constructs (endpoint groups, contracts, bridge domains, VRFs).

### A New Era of Cross-domain Diagnostics with AI and Agentic Systems - BRKETI-2172
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098314827001darf
Agentic AI, an evolution in artificial intelligence (AI) defined by enhanced autonomy, decision-making capabilities, and adaptability has the potential to create a sea change. AI Agent teams collaborating to achieve outcomes have demonstrated capabilities surpassing those of even the most advanced Large Language Models (LLMs) in single-query scenarios. Agentic Frameworks facilitate the creation of these AI agent teams and define their interaction and reasoning patterns, such as Chain-of-Thought, Reflection, etc. This session begins with a discussion on the emergence of agents, followed by a survey of current agentic frameworks including LangGraph, DSPy, Crew.ai, and Autogen. Fundamental concepts such as goal-oriented planning and re-planning, agent selection, team composition, decision-making, memory, action selection, and adaptation in complex environments will be reviewed. The session explores trade-offs between specialization and generalization, as well as emerging trends in multi-agent distributed systems and human-AI collaboration. The session concludes with an assessment of open challenges and future directions in agentic AI.

### A Song of ISE and Posture: Advanced Deployment and Troubleshooting - BRKSEC-3077
Speakers: Andrea Bertorello (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098381240001dcdA
Endpoint Security is nowadays a pillar of all organizations, and increasing their compliance checks before connecting to the organization networks is a trend. Your endpoint security is your armor. This armor is not a single piece of steel but instead, it's a set of security components, where a single weakness in one of them may destroy the efficiency of the entire system. ISE posture services help, to ensure that your endpoints armor is always in good shape. During the session, attendees will have the opportunity to explore advanced posture scenarios and settings, such as load balancing, posture session management, MFA and bidirectional-posture. A demo will provide in-depth information on these topics. Furthermore, after the session, attendees will possess the knowledge and skills to troubleshoot any posture-related issues using log references, to solve the problem of now from where I start if something is not working.

### A Unified Nexus Dashboard Experience - PSODCN-1870
Speakers: Karishma Gupta (Cisco), Arthur Scrimo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098467600001dXCj
In this session, you'll learn about the value of the Cisco Nexus Dashboard and the real-world problems the platform can solve. We'll discuss high-level Nexus Dashboard architecture and the unification of services under one Nexus Dashboard product. This session will introduce network management, fabric controller, insights, and orchestration, all under a single Nexus Dashboard instance.

### ACI Layer 4-7 Policy-Based Redirect (PBR) Deep Dive and Tips - BRKDCN-3982
Speakers: Minako Higuchi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098298348001dkHR
When designing network security in a data center, have you ever wondered where to enforce security policies and how to steer traffic to get firewalls to inspect the traffic? How would the use of Cisco ACI affect your layer 4-7 services such as firewalls, IPSs, and load balancers? This session will provide a deep dive into ACI layer 4-7 service integration capabilities, especially PBR service graphs. It will cover ACI contract security capabilities, how forwarding works to steer traffic, design options with common use cases, and multi-location data center design options. The basic assumption is that participants will have a solid knowledge of Cisco ACI and its functional components, including EPGs, contracts, VRF, bridge domains, multi-pod, multi-site, etc.

### ACI Multi-Site Architecture and Deployment - BRKDCN-2980
Speakers: John Weston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296023001dVRu
The need to deploy ACI in multiple data center sites to provide redundancy is a common requirement for both enterprise and service providers. This session introduces the application, operation, and availability considerations for Cisco ACI multi-site and covers multiple aspect of the architecture, including an introduction and positioning between multi-pod and multi-site architectures, inter-site network (ISN) deployment considerations, ACI Nexus Dashboard Orchestrator (NDO, formerly MSO) architecture and deployment, ACI multi-site control and data plane, connecting to the external layer 3 domain, and network services integration. The expectation is that attendees already have at least a basic understanding of ACI in order to get the best out of this session.

### ACI Troubleshooting: A Deep Dive into Policy-Based Redirect (PBR) - BRKDCN-3615
Speakers: Roland Ducomble (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296737001deyB
Cisco Application Centric Infrastructure (ACI) provides the capability to redirect traffic as you see fit through service graphs. With an increasing need to integrate transparent services such as load balancers and firewalls, a good understanding of this feature is essential to configure and operate it. This session will dive deep into ACI's Policy-Based Redirect (PBR) functionality with practical use cases and troubleshooting examples.

### ACI Troubleshooting: Advanced Layer 3 Out Features - BRKDCN-3678
Speakers: Roland Ducomble (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098297092001d1Az
A layer 3 outside (L3Out) network configuration in Cisco Application Centric Infrastructure (ACI) controls the external connectivity toward the fabric. In this session, we will build on earlier Cisco Live L3Out sessions and dive deep into features such as route control and transit routing. We will cover this from both a single-pod and multi-pod perspective, and explore troubleshooting, best practices, and the inner workings.

### ACI Troubleshooting: Expand Your Tool Set with Nexus Dashboard Insights - BRKDCN-2626
Speakers: Ivan Kovacevic (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098290924001dc4z
Attend this session to learn how to troubleshoot your ACI fabric through NDI's Day 2 ops capabilities. We will demonstrate how these tools fit into your troubleshooting tool belt and show through practical examples how you can use them on a daily basis. Tired of spending hours and hours on troubleshooting? We're looking forward to meeting you and showing you a different way.

### ACI Troubleshooting: Optimize Your APIC User Experience through API Mastery - BRKDCN-2635
Speakers: Gabriel Monroy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098291291001deQ3
All configuration interactions with an application-centric infrastructure (ACI) fabric begin with an API call. Every day brings new integrations and monitoring tools, which take advantage of the APIC's single-northbound API. It is imperative to understand that APIC performance has a direct correlation to API request handling, and to have a methodology to isolate issues related to both. You will leave this session having learned how the API relies on APIC subsystems, which features are available to optimize and protect the API, and how to isolate and troubleshoot APIC and API performance issues.

### ACI: The Foundation of an Internal Private Cloud - BRKDCN-2984
Speakers: Steve Sharman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296199001dlfi
There are thousands of customers globally who have successfully deployed ACI fabrics and operate them as "just another network," but what if you could operate your ACI fabric as programmable private cloud infrastructure? In this session, we will look at how you can operate your ACI fabric as the foundation of an internal private cloud. We will look at how to migrate services onto an ACI fabric (network centric) and then implement segmentation (application centric). We will look at how to use endpoint security groups to wrap security around endpoints within a VRF. We will then see how we can block east/west traffic within a hypervisor, and finally, we'll dynamically add in firewalls to provide targeted layer 7 control.

### AI Agents and Agentic Frameworks: An Overview - AIHUB-2170
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161395785001ND1r
Agentic AI represents a significant advancement in artificial intelligence (AI), characterized by its enhanced autonomy, decision-making capabilities, and adaptability, which could lead to transformative developments. Unlike conventional AI systems that are rigidly programmed for specific tasks, agentic AI can understand and interpret complex and nuanced context and goals, allowing for more sophisticated interactions and decision-making processes. AI agent teams have shown proficiency and results that exceed those of even the most sophisticated Large Language Models (LLMs) in single-query situations. This session delves into the principal innovations and core principles that underpin Agentic AI, drawing on examples from current frameworks such as LangGraph, Autogen, Semantic Kernel and Swarms. It evaluates trends in multi-agent distributed systems and the evolving dynamics of human-AI cooperation. The session concludes by assessing open challenges and future directions in agentic AI.

### AI Agents with Cisco and Splunk - AIHUB-2494
Speakers: Dave Zacks (Cisco), Errol Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161396931001NbSh
AI-enabled agents are the talk of the industry and can serve as the basis to address many important customer issues around network, application visibility, security and control. But which agents and which capabilities to use to address which set of issues? Come to this fast-paced, fun AI Hub session to dive into the world of AI agents available from both Cisco and Splunk, showcasing key capabilities and highlighting how they can be used to address real-world use cases. Presenting this session are Errol Roberts and Dave Zacks, both Cisco Distinguished Engineers as well as Cisco Live Distinguished Speakers and AI enthusiasts. Come to this exciting and engaging session to see the latest AI agents and tools from Splunk and Cisco in action!

### AI Infra for the Rest of Us - BRKDCN-2677
Speakers: Shelly Cadora (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292197001dGCB
The dazzling speed and scale of shiny new AI factories can sometimes overshadow a simple truth: cloud-based AI is not for everyone. If your AI use case requires enhanced data security, regulatory compliance, lower latencies or just better economics, then an on-prem AI cluster might be the better answer. But building and operating your own cluster can be daunting. How do you build a lossless Ethernet fabric? Do you need GPUs, CPUs, DPUs or all three? What kind of storage maximizes performance? And how do you connect it all together? In this session, we will show how Nexus HyperFabric for AI meets the challenge, delivering a simple-to-operate (really!) AI cluster, complete with compute, storage and networking for your on-prem use cases. HyperFabric for AI handles the whole process, from design to ordering, to deployment to maintenance, and operations, so you can focus on your AI apps, not your infrastructure.

### AI Innovations with Cisco Webex: Transforming Industries through Smart Applications - DEVNET-2127
Speakers: Adam Weeks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098438561001d8Cf
Explore the future of industry innovation in our session "AI Innovations with Cisco Webex: Transforming Industries through Smart Applications." Discover the game-changing integration of AI technologies, like Generative Pre-trained Transformers (GPTs), with Cisco Webex SDKs, and how they're making waves in healthcare, finance, retail, and manufacturing. Learn how developers are utilizing Natural Language Processing, Machine Learning, and Image Recognition to create applications that enhance communication, improve operational efficiency, and provide personalized customer experiences. This compact yet insightful presentation will showcase how the power of AI and Webex can be harnessed to not only meet the evolving demands of these industries but propel them into a new era of technological excellence.

### AI Is Your Copilot: Lead With the Right Use Cases and Stay Ahead - PARAI-1278
Speakers: Vishal Shukla (AVIZ NETWORKS), Thomas Scheibe (Aviz Networks)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161423239001NIVD
In an era where AI is more than a buzzword, it's a business imperative, our session at Cisco Live will equip you with the strategies to not just compete, but lead. Learn how to transform AI concepts into concrete advantages: Build a Future-Proof Foundation: Key architectural elements that scale and adapt with your growth. Leverage Agentic-Based AI Assistants: Integrate AI that performs autonomously yet under control, enhancing your network's capabilities without disruption. AI Assist Use Cases: Focus on automation of routine tasks and enhanced observability that deliver immediate returns and pave the way for advanced AI adoption. Learn how to architect, adopt, and act with AI and stay ahead in the fast-evolving networking landscape. Join us to dive deep into how AI can become your strategic advantage, driving substantial ROI and setting you apart in your field.

### AI Wireless Assurance - when AI meets Cisco Meraki Wireless - BRKEWN-2039
Speakers: Minse Kim (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161402410001NsAd
We are living in a world where tech is synonymous to the AI. like MSG, everything seems to get more savory with AI. But can AI solve my latest challenges such as 6GHz, WPA3 and plethora of new devices and ever hiking expectations? This session provides the answers to the network operators who are seeking pragmatic examples and workflows of how to use the latest AI technologies in the Cisco Meraki wireless management to accelerate and assist your wireless deployment, operation and troubleshooting using AI. #GenAI #AI-RRM #chatbot #packetcapture #CUI

### AI for All: Bridging Innovation and Inclusive Pathways - CENGEN-1013
Speakers: Jason Warfield (Cisco), Zoe Rose (Canon Europa), Rebecca Stone (Cisco), Kimberly Moss (Natilik)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228982245001TZly
Today's rapid technological changes present both a challenge and opportunity: ensuring underrepresented groups not only participate in but lead technological innovation that shapes our digital future. Join industry leaders for a discussion on the increasingly clear impact that diverse IT teams have on business outcomes. You'll leave this session with insights to help you: - Unlock technical innovation through inclusive leadership - Design resilient teams that strengthen innovation through diverse perspectives - Prepare for emerging tech and the upcoming generation of talent

### AI in Collaboration: Techniques and Architectures for Audio, Video and Language A.I. - BRKCOL-2976
Speakers: Keith Griffin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098285932001dbTG
In this session, we will look at the AI architectures behind audio, video and language AI in collaboration technology. This includes real time media models for audio and video along with cloud architectures for interaction with large language models (LLM). This session will look at the generative AI technology behind commonly used features such as message and meeting summarization, contact centre AI assistants, Slido poll generation and AI generated vidcasts. We will also look at edge AI models for realtime media such as face detection and background noise removal.

### AI in Manufacturing: Building Resilience with Smart, Secure and Sustainable Operations - PSOIND-1779
Speakers: Ewald Munz (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098469792001dHiU
In the era of Industry 5.0, AI, robust cybersecurity, and energy management are crucial for resilient manufacturing. This session will highlight how Splunk's AI-powered platform can optimize operations, strengthen IT and OT security in conjunction with Cybervision, and drive sustainable energy usage. Discover how AI models can predict equipment failures, enhance production, and reduce energy consumption, while real-time monitoring boosts defenses against cyber threats. Join us to explore how integrating AI-driven insights can build smarter, more secure, and energy-efficient operations, ensuring manufacturers stay competitive and sustainable in the face of modern challenges.

### AI in an Inclusive World: Challenges and Opportunities - IF-1080
Speakers: Adele Trombetta (Cisco), Britney Bartlett (Cisco), Jose van Dijk (Cisco Systems, Inc.), Kim Pasche (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098453254001dOOQ
This session explores the multifaceted relationship between artificial intelligence (AI) and inclusivity. We will discuss about the manifestations of gender bias in AI systems, and the career pathways and educational initiatives designed to attract and support more diverse teams entering AI-related fields. The session also addresses the ethical implications of AI development, underlining the necessity of diverse perspectives to ensure responsible and fair AI solutions. Through these discussions, we aim to shed light on the challenges and opportunities AI presents in creating a more inclusive world.?

### AI with Integrity: Understanding Cisco's Responsible AI Framework in the Cisco Networking Cloud Experience - AIHUB-1963
Speakers: Priya Ram (Cisco), Lalli Flores Jimenez (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161392396001Nb5d
Artificial Intelligence (AI) is revolutionizing industries by enhancing team productivity and workflows. However, ensuring that AI operates ethically and appropriately in various contexts is crucial. This session will guide participants through Cisco's Responsible AI framework on which Cisco AI Assistant is built, highlighting how Cisco builds trustworthy AI solutions. You will explore the core principles of Cisco's approach to AI ethics and responsibility. Real-world examples from the Cisco AI Assistant in the Meraki Dashboard will demonstrate how these principles are implemented in practice. Discover how Cisco ensures that its AI systems are designed with trust, transparency, and accountability at their core. Learn how these practices contribute to delivering reliable and effective AI solutions for your network management needs.

### AI-Assisted Code Generation for Network Automation with CWM and NSO - DEVNET-2635
Speakers: Wai Tai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098446473001dWJ7
AI is being used in a lot of different areas in the networking industry for improving productivity. This talk is on my experiment of using GitHub Copilot to generate code for Crosswork Workflow Manager Workflows, adapters, and for retrieving information from NSO via its RESTCONF interface. I will share the challenges I have encountered and the good results I got with persistence. You'll leave this session with an understanding on the maturity level of AI assisted code generation and ideas on what's possible for network automation.

### AI-Driven Transformation in Cisco Secure Firewall Operations - CISCOU-2049
Speakers: Dmytro Kontsevyi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098412165001dcwR
Discover how artificial intelligence is revolutionizing the way we manage and operate Cisco Secure Firewall systems. This session delves into the integration of AI technologies that enhance operational efficiency, streamline security management, and improve threat detection capabilities. Attendees will gain insights into the latest AI-driven features that automate routine tasks, reduce human error, and elevate the overall security posture of your network infrastructure. Join us to explore real-world applications of AI in firewall operations. This session will equip IT professionals, security analysts, and network managers with the knowledge to enhance cybersecurity in their organizations.

### AI-Native SOCs: A Strategic Blueprint for Business Leaders - PSOCX-1792
Speakers: Barry Reddan (Cisco Systems, Inc.), Simon Crocker (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098467063001dsaI
Business leaders face the critical challenge of aligning security operations with broader business goals while enhancing organizational resilience. Traditional Security Operations Centers (SOCs) are often hampered by their inherent complexity and inability to scale across various domains. As we move further into the age of automation and AI, it's essential to rethink how SOCs operate. "AI-Native SOCs: A Strategic Blueprint for Business Leaders," will explore how automation and AI can revolutionize SOC processes from end-to-end. We'll discuss how leveraging data-driven automation and AI for threat detection and contextual inference can transform security operations. Furthermore, we'll delve into the implications for governance, people, processes, and technology, providing actionable insights into building robust transformation programs. Join us to discover how you can lead your organization's security initiatives into the future.

### AI-Powered Chatbots and Virtual Assistants in Cisco Contact Centers - AIHUB-2155
Speakers: Raad Al-Jawahiry (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161395408001NnVP
In today's fast-paced digital landscape, customer expectations are higher than ever. AI-powered chatbots and virtual assistants are revolutionizing the way contact centers operate, providing seamless and efficient customer interactions. This session delves into the development, deployment, and management of AI chatbots within Cisco Contact Centers, highlighting how these technologies enhance efficiency, reduce operational costs, and elevate customer satisfaction.

### AI-Powered Lifecycle Management: Balancing Innovation and Existing Assets - PAROPS-1735
Speakers: Roberto Fasiani (NTT ITALIA SPA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161425466001NPn2
In recent years, businesses have increasingly leveraged a variety of options to procure and utilize software. However, achieving desired outcomes remains challenging. Many organizations face difficulties in managing their software assets, often resulting in underutilized tools and misalignments between IT hardware and software. Key Challenges: - Complex commercial constructs from multiple vendors - Lack of timely visibility into license consumption within organizational units - Unexpected true-ups and true-forwards - Struggles to measure business outcomes.These issues hinder efficient planning, exposing businesses to risks and missed savings. Addressing these challenges is essential to maximize investments and ensure a seamless IT environment. Session Highlights: - Our approach and best practices in license and asset management - How AI can enhance user interaction and provide better insights into critical asset information - Strategies to optimize operational efficiency and reduce compliance risks Join the session to learn how to navigate these complexities and achieve a balanced, efficient IT ecosystem.

### AI-Powered Scripting with GitHub Copilot - DEVNET-2159
Speakers: Erika Dietrick (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098439639001dZSi
The irony of automation is that although there is plenty to be automated, we don't always have time to do it. With GitHub Copilot, you can provide natural language prompts and receive AI code suggestions, answers to questions found in your organization's documentation, and suggested descriptions for pull requests. This session dives into how these features can power your scripting workflow by using AI-powered scripts and Cisco Security APIs as examples.

### AI-Ready Data Center - Sustainability vs. Infrastructure Requirements - How to get your Data Center Ready for the Coming AImagedon - BRKGRN-2419
Speakers: Christopher Liljenstolpe (Cisco), Heiko Ebermann (Vertiv), John Bean (GR Cooling)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098326253001dF62
Within the period of 2 years, we have seen planning on per-rack power footprints go from 16-30 kW to 150-250 kW. That is an order of magnitude. In this talk we will explore the impact of various choices in rack power and thermal density and explore how AI can help maintain optimal operating conditions while minimizing the energy required for cooling and can optimize the distribution of workloads across servers. Be future ready by modernizing with more energy-efficient hardware and computing architectures while determining the best cooling systems that prioritizes energy efficiency without compromising performance.

### AI/ML for Network Engineers - BRKENT-2209
Speakers: Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161400849001NSX2
This is an updated session for Cisco Live Amsterdam 2025 with a keen focus on AI and large language models (LLMs) for network engineers. In this fun and engaging session, attendees will review the various advanced Cisco AI/ML capabilities available to address network and application use cases, explore how AI network infrastructures are built, and most importantly, delve into practical examples of how you can use AI and LLMs to address your own network deployments, as well as expand your understanding of AI use cases and available tool sets. Presenting this session are the dynamic duo of Dave Zacks and Patrick leMaistre, both Cisco Live distinguished speakers with a passion for all things AI. Come to this session to gain insight into how AI can be used to help your organization succeed.

### AIOps 101: What is AIOps and How it Can Help You - BRKOBS-1938
Speakers: Annette Sheppard (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098340851001dDl4
Generative AI is THE focus of the business world, but when it comes to IT operations and observability, what is AIOps? In this session, we'll cut through the hype to define AIOps, how it can help you, and how to get started. With real-world examples of how businesses succeed using Splunk's AIOps capabilities, we'll discuss applying AI and ML to accelerate incident response, reduce MTTD and MTTR, cut, costs and empower teams with the tools they need to make decisions quickly.

### AIPO: A Glimpse into the Future of GenAI-Powered Agile Workflows - DEVLIT-1973
Speakers: Peter Bosch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098425518001dBBK
In today's fast-paced tech landscape, product owners face significant challenges in managing backlogs, prioritizing tasks, and planning sprints effectively within agile workflows. Enter AIPO, a GenAI-powered solution that transforms everyday product owner tasks. This session demonstrates how AIPO leverages artificial intelligence to streamline product ownership tasks, enhancing decision-making and boosting team productivity. Through live demonstrations, you'll witness AIPO's capabilities in epic analysis, story breakdown, and automated sprint planning. Discover practical strategies for implementing AI-driven tools in your agile process, strategies for overcoming common product ownership hurdles and gain insights into the future of AI-assisted product development.

### AMD DPU-Accelerated Networking for AI and Services in High-Performance Data Centers - PARDCN-1333
Speakers: Shane Corban (AMD)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098462447001dUUf
In this session, we'll explore AMD's portfolio of DPU-based networking products designed to meet the needs of high-performance, low-latency AI, in conjunction with services acceleration for the largest hyperscale and enterprise customers. We'll also showcase how the Cisco partnership on UCS with AMD Pollara AI networking, and DPU-accelerated switching on Cisco Silicon One and Nexus can deliver leading-edge performance for the most challenging data center customer deployments.

### API design principles and considerations for massive scale - CISCOU-2039
Speakers: John Kuchta (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098408627001dAL0
Whether you're building on top of Meraki's APIs, managing software development teams, or even developing your own APIs, these principles and new feature releases should streamline your operations, making it easier to achieve your critical business outcomes with limited resources. This year's preso will feature a number of new releases since last year's talk.

### AWX 101: Getting Started in Automation with the Ansible AWX Platform - DEVNET-1060
Speakers: Tim Glen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098428339001dAj5
Have you heard of Ansible but are concerned about another CLI? Do you know Ansible and want to take your skillset to the next level? Are you ready for the POWER of the Ansible AWX Platform!? Ansible is the industry's de facto automation tool and can automate almost any product a network engineer could use. But it gets better; AWX is Ansible's open-source big brother and provides Ansible with a powerful, user-friendly GUI front end. In this introductory session, participants will learn practical AWX concepts such as credentials, inventories, templates, and jobs. Demos will include AWX's Git integration for source control, building inventories, configuring templates, and reviewing jobs. Finally, we will discuss and automate some of the latest IOS XE sustainability features to help reduce power usage across all your Cat 9000 switches!

### AWX 201: Advanced Automation Techniques with the Ansible AWX Platform and GitHub Copilot - DEVNET-2517
Speakers: Tim Glen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098445373001dcRp
Do you need better troubleshooting tools than Ansible CLI provides? Is managing your Ansible Playbooks, inventories, and logs cumbersome? Are you wondering how to incorporate AI into your Ansible lifecycle? Get ready to see some POWERFUL automation with the Ansible AWX Platform! In this session, participants will acquire advanced skills that will enable them to tackle more complex automation tasks. This session will focus on several things, including AWX Multi-Project Workflows, RAVPN certificate management using AWX and Let's Encrypt and coding and troubleshooting with GitHub CoPilot. Participants should already be familiar with practical AWX concepts such as credentials, inventories, jobs, and templates.

### AccelTex Solutions - Connectivity with Cisco Access Point - PARIOT-1406
Speakers: Jason Rinaldi (Hubbell Premise Wiring / AccelTex)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161424729001Nizy
In this session, participants will learn about the innovative solutions and unique deployments that AccelTex Solutions has implemented utilizing Cisco technology and access points.

### Accelerate Your Partner's Lifecycle Practice in Three Steps - PSOCX-1786
Speakers: Lucy Godfrey (Cisco Systems, Inc.), Michel Gaspard (Cisco Systems, Inc.), JP Paternostre (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098466703001dkrL
Cisco is investing to help partners develop and accelerate their lifecycle practices through a three-pronged approach: white-glove support, readiness at scale, and dedicated funding. In this session, learn how you can leverage these resources to build a lifecycle practice that is solid, scalable and delivers rapid value to your customers.

### Accelerate Zero Trust Access - PSOSEC-1438
Speakers: Prabhu Barathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098472182001dD3v
By taking an identity-first and context-aware approach to Security Service Edge (SSE), Cisco Zero Trust Access provides comprehensive coverage, and a seamless experience securing all users, all locations, all applications, and all devices, enabling organizations to successfully achieve real-world zero trust for today's remote-first workforce.

### Accelerating AI Everywhere: VMware Private AI with Intel Xeon and Gaudi 3 - BRKPAR-1485
Speakers: Simon Todd (Intel Corporation)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161409581001Nu9U
Explore how VMware Private AI, powered by Intel's cutting-edge 4th, 5th and 6th Gen Xeon processors and the latest Gaudi3 AI accelerators, delivers exceptional performance and efficiency for AI workloads. This session highlights the capabilities of Intel AMX and Gaudi3, enabling breakthroughs in NLP, generative AI, and large-scale training. Discover how to choose the right compute solution CPU, GPU, or AI accelerators based on workload demands, cost considerations, and sustainability goals. Learn how VMware's multi-cloud platform ensures data privacy and operational scalability. Empower your AI strategy with a robust, future-ready infrastructure that drives innovation and lowers total cost of ownership.

### Accelerating Customer Growth: Partner Innovation Meets Cisco Sustainability - IFGRN-1166
Speakers: Guillaume CHABAS (Orange Business), Alisdair Mckeand (CAE Technology Services Ltd), Richard Simmons (Logicalis), Denise Lee (Cisco), Colin Seward (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098457344001d2nq
Sustainability is a business driver for partner success with customers, a value-add to every customer conversation. Learn from three Cisco sustainability focused partners on how they win business, and support their customers with sustainability goals. You will also hear from Denise Lee and Colin Seward on how Cisco has: Incorporated sustainability (and energy management and monitoring) across our product portfolio Built a dynamic 'Sustainability Data Foundation' to show 'Product Carbon Footprint' data across our portfolio Created sales enablement tools to help partners deliver and differentiate with sustainability Partners are critical to disseminating Cisco's sustainability message and building upon our sustainability offerings. During this session, we will showcase key sustainability offerings and case studies from three of our most prolific sustainability partners. Logicalis, CAE and Orange Business are driving the sustainability agenda across their customer base, and are innovating across energy management, circularity and data. These partnerships can amplify impact by combining resources, fostering innovation, and driving systemic change.

### Accelerating Infrastructure Modernization and Execution Strategies for AI - CENCX-1004
Speakers: Adele Trombetta (Cisco), Carlos Pereira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227080090001JqyX
AI is a strategic imperative for gaining a competitive advantage. With many enterprises transitioning from piloting to operationalizing AI, the push to modernizing their IT infrastructure to support AI initiatives and other advanced technologies has accelerated. As, in turn, have broader concerns surrounding topics such as energy consumption and regulatory compliance. Join us for an insightful discussion to learn how, with Cisco Customer Experience, customers can rapidly transform their infrastructure to be well-prepared for the AI era. You?ll also hear how our AI strategy, data-driven insights, and expertise can support you on your own transformation journey for AI.

### Accelerating Threat Analysis with Intelligent Automation - BRKSEC-2623
Speakers: George Panousopoulos (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098376862001d7Js
SOCs struggle with overwhelming numbers of potential threats as well as the development and maintenance of effective repeatable procedures and response plans to deal with the constantly evolving threat landscape. Join this session to learn how the powerful combination of Splunk Attack Analyzer and Splunk SOAR provides initial triage at scale, significantly reduces the effort to construct and maintain threat analysis playbooks, and allows security teams to respond to attacks at machine speed.

### Achieve Digital Resilience with AI-Enabled Automation - PSOSP-1867
Speakers: Nils Petter Tisell (Cisco Systems, Inc.), Greg Owens (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098473094001dfeZ
As subscriber expectations grow, service providers must increase service agility, improve efficiencies, and enhance customer experiences. In this session, you'll see how Cisco AI-enabled end-to-end automation and assurance solutions equip service providers with predictive insights and analytics that empower them to plan, deploy, and assure networks intelligently with speed and accuracy at scale. Plus, see how AI automation turns massive amounts of network data into actionable insights, and how these solutions harness AI/ML to manage performance, detect anomalies, and strengthen digital resilience. This allows customers to shift from manual, reactive actions to proactive solutions and better, faster, more reliable decision-making.

### Achieving Mass Scale Automation: Insights from Organizational Evolution in Automating the World's Largest Networks - BRKOPS-2827
Speakers: Bryn Pounds (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098357052001dyW0
How are large, diverse organizations automating and modernizing complex networks made up of 100,000+ devices that run the most active and dynamic network services? What can we learn from others who have already gone down this path? What choices did they make, what were the outcomes, and is your organization ready? Come join us to look at some case studies about some Fortune 500 companies and large Universities have learned as they have evolved some of the largest networks in the world. We'll look at their lessons learned over years exploring various open source alternatives such as ansible, terraform and others, as well as some of the industry leading Cisco solutions such as Network Services Orchestrator (NSO) and how they can best complement each other.

### Achieving Success in Your Migration from Prime to Cisco Catalyst Center and Data Migration between New and Old Catalyst Centers - BRKOPS-2540
Speakers: Stefan Honeder (Cisco), Soren Dulong Andreasen (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098354499001dmIy
Cisco Catalyst Center is taking over Prime Infrastructure. Believe us, the time to migrate was yesterday! Don't wait migrate now! Participating in this session will equip you with the necessary tools and knowledge for a successful Prime to Catalyst Center migration. We will show you how to use the available Prime assessment and migration tools,'share valuable tips and best practices'that we have learned from helping many customers and partners through their migration journey. This session will also cover the best practices on how to migrate from older physical Catalyst Center appliances to Virtual (AWS or Vmware) or latest physical Catalyst Center appliances. To give you a good understanding of the capabilities of Catalyst Center, the session will also cover the operation of your network with Catalyst Center.

### Add Visibility to Your S(A)SE with ThousandEyes - BRKOPS-2857
Speakers: Primoz Kolman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098357411001diHz
Your organization may be utilizing Cisco Secure Access and Cisco SD-WAN. Perhaps you are contemplating the deployment of Security Service Edge (SSE) or the more comprehensive Secure Access Service Edge (SASE) technologies. Are you concerned about the loss of control and visibility during the transition of your infrastructure to the Internet and the cloud? This session will demystify how ThousandEyes enables Experience Insights within Secure Access and provides you visibility across your SD-WAN network. You will learn how and what to deploy to assure your employee's digital experience against software as a service (SaaS) and on-prem applications, regardless of where your users are (in the office, at home, or abroad), whether you use Cisco Secure Access, Cisco SD-WAN, or a combination of both. This is an intermediate level session. Attendees should have a basic knowledge about ThousandEyes, Secure Access or Cisco SD-WAN solutions.

### Advanced Campus Network Design: Multilayer Architectures and Next-Gen Protocols - BRKENS-2500
Speakers: Shawn Wargo (Cisco), Jakub Matela (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098300588001dwEg
This advanced session builds on the foundational knowledge from "Introduction to Campus Wired LAN Deployment Using Cisco Validated Designs" and refreshes the core concepts of "Enterprise Campus Design: Multilayer Architectures and Design Principles" Attendees will explore the details of designing high-performance, scalable multilayer campus networks, with an emphasis on advanced protocols and technology integration. Key topics include: - Advanced aspects of multilayer campus network design - Pros and cons of different design models (1-2-3 or 4+ Tier) - Advanced protocol implementations (ECMP vs. StackWise / MPLS vs. EVPN vs. SD-Access) - Integration with wireless and security solutions - Real-world examples and best practices for optimizing enterprise networks This session is geared towards professionals responsible for the design, deployment, and management of enterprise campus networks, who possess a solid understanding of LAN switching and routing fundamentals.

### Advanced Innovations in SRv6 uSID and IP Measurements - BRKSPG-3198
Speakers: Alexey Gorovoy (NEBIUS), Pablo Camarillo (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161418290001NGBp
With over 85,000 routers deployed, SRv6 uSID is revolutionizing network architecture with a unified end-to-end dataplane across domains. This session explores cutting-edge use cases and innovations in SRv6 uSID, demonstrating its ability to build any service - VPN, TE, FRR, NFV, Green Routing, and more, without additional shim layers, showcasing real-world deployments with leading operators. The session will also feature a case study from Nebius, showcasing their Frontend DC design powered by SRv6 uSID. This innovative architecture leverages SRv6's end-to-end stateless dataplane to seamlessly integrate VPN, TE, and NFV from the front-end to peering. Additionally, the session will unveil the latest advancements in IP Measurements (IPM) achieving a groundbreaking 14 million probes per second with Silicon One hardware for one-way loss, latency, and liveness measurements. Surpassing traditional methods, IPM delivers precise SLA measurements with accurate routing correlation. Attendees will explore innovations like Path Tracing, gaining practical insights for next-generation network design.

### Advanced LISP SD-Access Forwarding Architecture - BRKENS-3826
Speakers: Jerome Dolphin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098302950001dGtA
This session will examine the core use cases for LISP Pub/Sub, SISF (Switch Integrated Security Features), and CEF (Cisco Express Forwarding) within the framework of LISP Pub/Sub SD-Access fabric. We will systematically examine how each technology addresses its specific set of requirements, incorporating concise lab demonstrations to illustrate the underlying concepts. Participants should anticipate a session with a moderate concentration of protocol analysis, debugging, and CLI operations. By the conclusion of this presentation, attendees will have acquired a comprehensive understanding of the critical technical elements that imlpement packet forwarding within an SD-Access Fabric. It is recommended that participants familiarize themselves with the content of BRKENS-2810 and BRKENS-2811 prior to attending.

### Advanced RF Tuning in Cisco Wireless - Become an Expert While Getting a Little Help from Cisco AI - BRKEWN-3413
Speakers: Jim Florwick (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161406609001NUzJ
Participants will learn the RF design and implementation guidelines necessary to plan, configure, and implement Wi-Fi networks that meet the evolving regulatory (6 GHz) and customer RF demands. Wi-Fi is changing, and there has never been a more exciting time to be in RF technologies. In this session you will learn about Cisco's newest Catalyst Wireless Access Points and antennas, including the latest Wi-Fi 6E access point and the new Wi-Fi 6 stadium antennas. Participants will learn and understand the current coverage and design best practices, as well as what this means to the evolving RF landscape around the world. Everything we know is evolving. This session will provide a deep dive on how to think about and manage Wi-Fi 6E, radio resource management (RRM), Spectrum Intelligence, and the evolution of multiband operations (MBO) within infrastructure. The evolution to Wi-Fi 6E brings amazing RF capacity gains. Wi-Fi 6E also means new pressures on the wired infrastructures capacity and power that supports it. Attendees will learn what to expect and how to manage and plan the future needs now. Session attendees will be able to successfully use the information to navigate and understand todays fluid RF and mobility landscapes and to articulate the benefits to their customers, enabling the best wireless and mobility experiences yet.

### Advanced SD-WAN Policies Troubleshooting - BRKENT-3797
Speakers: Eugene Khabarov (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098313043001dQA6
This is a deep-dive session about Cisco SD-WAN policies troubleshooting based on extensive TAC and BU escalation team experience. This session is very TAC cases-driven and the main goal is to demonstrate interesting failure scenarios and common pitfalls that we've seen in the field, including configuration and design mistakes, including centralized control policies, data policies, and application-aware routing. This session will be based on various real-life scenarios with DIA, NAT, traffic engineering, routing, deep packet inspection, classification, and QoS when behaviors are not expected at a first glance, but how truth can be revealed with the help of advanced troubleshooting methodologies. And yes, we like CLI a lot. Please note that this is an advanced-level session and it does not cover the basics of SD-WAN. The main audience is network architects, consultants, engineers, and network designers who are seeking a deeper level of knowledge about SD-WAN policies to avoid common mistakes in their day-to-day operations, design, and deployment activities while dealing with a Cisco SD-WAN solution. This session is recommended as complimentary to "Advanced SD-WAN Routing Troubleshooting."

### Advanced SGT - Multi Domain Context - BRKSEC-3707
Speakers: Darrin Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098383742001dQys
This session examines the use cases for Security Group Tags (SGTs) and how SGTs have evolved into the defacto language for security policy within Cisco and the industry. SGT uses software defined network abstractions to enable scaling of network security within enterprises for a Unified Zero Trust Network Access solution. This session will review lower level design, configuration, monitoring and troubleshooting of SGTs and SGACLs applied to use cases like user/device segmentation, IaaS and SaaS policy controls as well malware mitigate Security Group technology will be discussed as applied to LAN, WLAN, WAN and Data Center networks. This session is aimed at Network/Network Security Specialists and Architects involved in designing and building advanced security solutions scenarios using Cisco network and security appliance deployment models. Attendees should be familiar with SGTs, Cisco routing, switching, wireless and security appliances at a conceptual level and a detail knowledge of one of those disciplines. Suggested prior sessions include sessions on the Identity Services Engine (ISE), SDA, Segmentation and network authentication (802.1X on wired and WLAN).

### Advanced Storage Area Network Design - BRKDCN-2941
Speakers: Ed Mazurek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294409001d324
This session presents the details of the protocols, principles, and practices used in designing Fibre Channel(FC) storage area networks (SANs). A review of FC protocols will be followed with a discussion of the advanced capabilities of the Cisco MDS 9000 family. Design principles and practices for building FC SANs in a multi-speed, multi-protocol environments, including high availability, security, scalability, and management. Included are topology design choices, optimal use of hardware, fabric routing (FSPF), link aggregation (Port Channels), TCAM usage and Virtual Fabrics (VSANs). The last section will cover integration of intelligent SAN services such as SAN extension with FCIP using the new 1/10/40G IPS,2/4/8/10/16G FC Module and optical extension (CWDM and DWDM), Acceleration, and Data Mobility. This session also covered SAN management using Nexus Dashboard.

### Advanced Terraform Techniques: Moving Beyond the Scaffolding - DEVNET-3722
Speakers: Quinn Snyder (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098450654001dxiz
A lot of emphasis is put on the use of Terraform to create immutable structures within an API-enabled product or platform. However, this barely scratches the surface of what is possible. In this session, we'll discuss the creation of Terraform modules, how to manipulate data, and how to use conditionals, loops, and other "programmatic constructs" to take your Terraform HCL to the next level!

### Advanced YANG Data Modeling for Cisco NSO - DEVNET-3014
Speakers: Bartosz Luraniec (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098449914001dgCr
Cisco Network Services Orchestrator (NSO) is software for automating services across traditional and virtualized networks. Used with YANG data models enables us to manage large topologies, work with multi-vendor nodes, automate, and scale. The participants will have the possibility to see how YANG tricks combined with NSO can make their business more agile and promote non-stop operations as they will be able to manage network changes, modify services, and reconfigure devices in real time. During this session, the participants will be able to discover YANG solutions derived from Cisco CX best practices on various large scale NSO deployments, and discuss strengths and limitations over a demonstration.

### Advancements and Applications of Coherent Pluggable Technology in High Bandwidth Transport Networks - BRKOPT-2556
Speakers: Anuj Malik (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098359983001dTG9
Coherent pluggable technology has emerged as a pivotal solution, integrating coherent optics into pluggable transceivers. This innovation offers a scalable, flexible, and cost-effective approach to meet the increasing demand for bandwidth. This presentation will delve into the technical underpinnings of coherent pluggable technology, including key components such as tunable lasers, high-speed ADC/DACs, and sophisticated DSP algorithms. It will also explore the performance metrics, such as data rates, reach, and power consumption, comparing them with traditional coherent solutions. Furthermore, the session will highlight real-world deployment scenarios, case studies, and future trends, underscoring the transformative impact of coherent pluggables leading to convergence of IP and Optical layers.

### Agentic AI for Troubleshooting and Change Management: A Glimpse at the Future - DEVNET-2094
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098437071001dBW2
Agentic AI, characterized by autonomous decision-making capabilities, is poised to revolutionize troubleshooting and change management in IT operations. This presentation explores how agentic AI systems can autonomously identify, diagnose, and resolve issues, minimizing downtime and reducing human intervention. By leveraging machine learning and real-time data analysis, these AI agents can diagnose complex multi-domain systems like humans do. Gone are the days, where cross domain troubleshooting and change impact prediction required consolidation of all data into a single data-lake, complex rule systems and ontologies. Join us for a glimpse into the future where agentic AI transforms how we manage IT systems.

### Agentic IaC, Security, and Networking - the Good, the Bad and the Ugly - DEVNET-2940
Speakers: Peter Bosch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098449560001duHk
IT, security and network teams spend up to 30% of their time on pull-request reviews. Why? Why, in this gen-AI age, are they spending so much time on reviewing these PRs in the first place? Gen-AI enables the creation and validation of infrastructure changes autonomously. Moreover, by learning on the job, agentic assistance can help IT teams to scale and sustain the growth of ever expanding organization and IT footprint, and mitigate cost and talent scarcity challenges while focusing existing talent on high value tasks. Agentic teams can replicate, augment, review and approve PRs. This talk presents the issues to rid many of these mundane, error-prone and complex infrastructure config jobs by agentic teams. With use cases and demos, this session presents what works and what not for cloud-native, security and network tasks. Specifically, we present mechanisms to: Capture cloud-native and network state in GitHub a source of truth How to manage both cloud-native and network state through GitHub How to reduce Terraform/IaC, security and network state review overhead while maintaining governance Optimizing Terraform/IaC, security and network state against target objectives and best practices Automatically writing Terraform/IaC, security and network operations for complex updates using natural language The session demonstrates the approach, showcasing agentic IT/security/network teams that learn and optimize on the job. Moreover, we are asking for your help: can you help test, contribute and move forward this tech?

### All You Need To Know About App Hosting on Catalyst - BRKOPS-2490
Speakers: Anna Summerauer (Cisco), Dominik Soukup (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098353417001dljm
The time when network devices were used just for packet forwarding is definitely over. Due to continuous enhancements, there are many options for using them - e.g., network traffic analysis, app hosting, and autonomous troubleshooting. Moreover, all these features are already part of your network devices. The main question is where and how to start and what it brings to you. In this session, we will look at the edge computing concept and its benefits for our computer networks. You will see how to create and run your own application on various Cisco devices (switches, APs, routers) from scratch or use existing apps. Additionally, we will look at more practical examples that you can use in your daily life, such as guestshell, network troubleshooting and IoT.

### Always Like Never Before: Fabric Networking at Wimbledon 2024 - CSSENT-2505
Speakers: Kevin Ward (AELTC), Sam Hastings (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098416839001de0Q
A Catalyst 9000 fabric networking customer success story with the All England Lawn Tennis Club - hosts of The Championships, Wimbledon tennis tournament every year.

### An Introduction to Cloud Security - it's More than Just a Virtual Firewall - BRKCLD-1102
Speakers: Conor Murphy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098276895001dLex
As network admins we might often think that on-premises security = a firewall + access list. Therefore, would cloud and cloud-native security = a virtual firewall? As it turns out, over the past few years, cloud-native security has extended well beyond traditional firewalling and access control. In this introductory'session, we will explore the comprehensive, multi-layered approach to cloud security. We will look at various aspects of cloud security such as infrastructure, cloud-native or platform, and application-level security. We'll define'some of the many acronyms you may have heard such as CSPM, CNAPP, SBOM, and CWPP and examine where each one fits within an overall cloud or cloud-native security architecture.

### An Introduction to Quantum Mechanics, Computing, and Networking - BRKETI-1401
Speakers: Tim Szigeti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098314124001dnCW
Cisco is making a major R&D investment in quantum networking, as future communication systems equipped with quantum networks will open new possibilities in several technology domains, including distributed quantum computing, secure communications, global clock synchronization, high-accuracy sensors, and more. This is an introductory session to the science and technologies that enable quantum networking. This session will begin with a brief introduction to quantum mechanics, with a focus on quantum bits (qubits) and some of their special properties, including superposition, entanglement, and no-cloning (Note: this discussion will include some mathematical concepts and proofs). This will be followed by an overview of quantum computing, to better understand the direct impact and demands this emerging technology is already having on network communications and security. Finally, we'll bring it all together to outline the building blocks, opportunities, and challenges of building quantum networks, as well as highlight what Cisco is already doing in this exciting space!

### An Introduction to Quantum Mechanics, Computing, and Networking - CISCOU-1034
Speakers: Tim Szigeti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098400707001dJas
Cisco is making a major R&D investment in quantum networking, as quantum networks will open new possibilities in several technology domains. This session will begin with a brief introduction to quantum mechanics, with a focus on quantum bits (qubits) and some of their special properties, including superposition, entanglement, and no-cloning This will be followed by an overview of quantum computing, to better understand the direct impact and demands this emerging technology is already having on network communications and security. Finally, we'll bring it all together to outline the building blocks, opportunities, and challenges of building quantum networks, as well as highlight what Cisco is already doing in this exciting space!

### An Introduction to eBPF for Network Security Engineers - DEVNET-2927
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098449378001dqDa
In today's rapidly evolving cybersecurity landscape, staying ahead of threats requires cutting-edge tools and techniques. Extended Berkeley Packet Filter (eBPF) is transforming how network security engineers monitor and protect systems in real-time. This session will introduce eBPF's powerful capabilities for network security, offering live examples tailored for security professionals. Participants will learn how to leverage eBPF to monitor network traffic and detect suspicious patterns and potential attacks, trace system calls to identify unauthorized access attempts, and block malicious connections based on predefined security policies. You'll leave this session with ideas to help you enhance your security monitoring, detect anomalies, and respond to threats more effectively. Understanding of basic network protocols and Linux system internals is recommended. The session includes live demonstrations of eBPF in action, showcasing practical use cases and real-time analysis techniques. You will also learn how eBPF is leveraged by Cisco Hypershield, a groundbreaking security architecture designed to defend modern, AI-scale data centers. Join us to explore how eBPF can be a game-changer in your security toolkit and empower you to safeguard your network with advanced, real-time monitoring capabilities.

### AppDynamics and Splunk: A Better Together Story - PSOOBS-1904
Speakers: Ori Broit (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098471610001dL7V
AppDynamics and Splunk bring the most detailed visibility into your applications and infrastructure, regardless of whether you run your apps on-prem, in the cloud, whether they are 3-tier apps, microservices, or anything inbetween. But that's not all! We go beyond that to provide you with more details and understanding of how your Cisco infrastructure is helping your business achieve its goals! Join this session to learn more about how we're thinking of bringing together these two Observability powerhouses!

### Applying AI/ML Methods to Diagnose Network Issues Using Telemetry Data - AIHUB-2006
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161393523001NMXV
Troubleshooting remains largely a manual process, with substantial time devoted to diagnosing issues. This session explores how AI/ML can expedite initial diagnoses. It delves into the suitability of various AI/ML techniques for network data and different phases of analysis, such as problem identification and diagnosis. Using real-world telemetry data as a foundation, we will collectively examine and demonstrate the use of diverse AI/ML approaches, including large language models, to pinpoint and diagnose issues. Concurrently, we will discuss the advantages and drawbacks of the various technologies employed.

### Architecting Hybrid Multicloud Infrastructures - BRKDCN-2916
Speakers: David Jansen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098293317001d7N5
Cloud continues to be the disruptor, and customers have been on the cloud journey for several years. This session will address the following architectural trends and provide guidance for the growing demand of users and applications being everywhere in a multicloud world. As applications and data migrate from traditional private data centers to public clouds, private data centers and applications remain critical. This session will offer architectural guidance to help customers optimize and understand traffic flows, achieve operational efficiencies, and gain visibility in a multicloud world.

### Architecting Layer 4-7 Network Services in a Multi-Tenant Data Center with VXLAN EVPN - BRKDCN-2974
Speakers: Matthias Wessendorf (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098295839001dYi6
With VXLAN BGP EVPN data center fabrics, we now embrace integrated multi-tenant capabilites. With this, not only is the requirement for tenant separation present but also interconnectivity and attachment of layer 4-7 services. This session specifically covers requirements and approaches for deploying multi-tenant data center fabric with a focus on how to archive multi-tenancy within data plane and control plane around VxLAN with BGP EVPN. Further, the session will cover integration of layer 4-7 services to satisfy the needs of tenant interconnectivity, security appliance, and load balancers attachment. We will define the notion of multi-tenancy and how it relates to small, medium, and large enterprises, as well as discuss hardware and software technologies as they map to multi-tenant data centers. Subsequently, the integrating of layer 4-7 services into VxLAN with BGP EVPN is approached. This session will focus exclusivly on data center fabric deployments with VXLAN BGP EVPN including EVPN multi-site.

### Architecting Private 5G for Resiliency, Security, and Enterprise Network Convergence - BRKSPM-2042
Speakers: Filipe Rodrigues (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161419414001NYzu
Overview: As Private 5G (P5G) becomes increasingly prevalent among enterprise customers, there is a growing demand for highly reliable, secure, and trusted wireless connectivity. Enterprises often have existing Wi-Fi and wired networks and seek to leverage consistent operational paradigms across all access technologies. Session Highlights: This session will demonstrate how Cisco's differentiated P5G offerings meet the reliability demands of mission-critical applications while seamlessly integrating with existing Cisco portfolio elements. We will explore the resiliency capabilities of the Cisco P5G platform and its enterprise integrations: Identity and Policy Management : Integration with Cisco ISE provides a unified identity and policy management experience across enterprise domains, supporting VLAN segmentation, SGT Unified Security : Cisco Umbrella integration delivers comprehensive security policies across networks Full-Stack Observability : Collaboration with ThousandEyes enables comprehensive visibility across network layers Seamless Mobility : Ensure smooth transitions between Wi-Fi 6 and P5G networks for seamless connectivity PTP and QoS Design Guidelines : Best practices for implementing Precision Time Protocol (PTP) for RAN sync and Quality of Service (QoS) to ensure optimal network performance and reliability

### Architecting Seamless and Secure Multidomain Networks: Integration of ACI, SDA, SD-WAN, MPLS, and Cloud Technologies - BRKXAR-2022
Speakers: Navin Suvarna (Cisco), Dhrumil Prajapati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098397481001dXxT
In today's evolving digital landscape, software-defined technologies are rapidly deployed across diverse organizations. However, these often operate in isolation, devoid of seamless integration. This session unveils the mysteries of integrating these domains effectively, using real-world examples. Authors of the Cisco Press book, "Designing Real World Multi-Domain Networks" will illustrate how diverse domains like data center, WAN, LAN, CNFs, Cloud, Security, and SR-MPLS can be harmoniously integrated for next-gen network architecture. Sharing indispensable lessons and insights from years of architectural guidance, this session is a must-attend for those aiming to elevate their understanding of cross-domain network architecture and design.

### Architecting a Private Cloud for AI Workloads - BRKCOM-2519
Speakers: Dan Stacks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098287926001dVXW
As artificial intelligence (AI) continues to revolutionize industries, the need for robust and scalable infrastructure to support AI workloads becomes paramount. This session will provide an overview of AI workloads and the critical infrastructure considerations necessary to support them. Participants will learn how to translate model cards into specific infrastructure requirements, effectively size their deployments, and understand the power and physical capacity considerations essential for optimal performance.

### Architecting a Private Cloud for AI Workloads - CISCOU-2031
Speakers: Dan Stacks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098406116001dxPF
As artificial intelligence (AI) continues to revolutionize industries, the need for robust and scalable infrastructure to support AI workloads becomes paramount. This session will provide an overview of AI workloads and the critical infrastructure considerations necessary to support them. Participants will learn how to translate model cards into specific infrastructure requirements, effectively size their deployments, and understand the power and physical capacity considerations essential for optimal performance.

### Architecting your Cisco Catalyst Center for Resiliency and Business Continuity - Best Practices and Recommendation for HA,DR, Backup & Restore - BRKOPS-2608
Speakers: Sean Sivak (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098355950001d6q0
We will discuss how to deploy Cisco Catalyst Center's high availability to provide the resilience needed for your mission-critical operations. This session will provide details on the high availability capabilities of Catalyst Center, design recommendations for optimal high availability and best practices for disaster recovery. We will demonstrate how to configure high availability, disaster recovery, and backup and restore in Catalyst Center. This session will cover: HA & DR deployment considerations for physical and virtual appliance HA & DR configuration for physical and virtual appliance Failure scenarios Best practices and considerations for HA & DR

### Architectural Best Practices for Ensuring High Availability in Service Provider IP/MPLS Backbone Networks - BRKSPG-2080
Speakers: David Smith (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161414893001NetS
Network failures and erroneous events can significantly compromise network performance and availability, posing challenges for service providers in retaining existing customers and attracting new ones. Predicting and preventing every type of failure event is a complex task. Therefore, implementing high availability (HA) strategies is crucial to mitigate the adverse impacts of such events on network performance and reliability. In this breakout session, we will review architectural principles and best practices to ensure the high availability of service provider IP/MPLS backbone networks using IOS XR software. Join us to gain valuable insights and practical guidance on enhancing the resilience and robustness of your IOS XR network infrastructure.

### Assurance, Experience, and Insights: Building Digital Resilience - CENOBS-1198
Speakers: Chris Crocco (Cisco), Steven Moore (Cisco), Matt Gillies (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228646399001sw9f
Digital resilience is crucial for preventing potential disruptions to business operations, including exposure to security threats and revenue loss due to performance issues. This session will demonstrate how the combination of Cisco Networking and Splunk enables customers to integrate their infrastructure with Splunk's industry-leading platform. We will showcase how Assurance and Digital Experience Management, together with ThousandEyes and IT Service Intelligence (ITSI), are used to correlate network infrastructure performance across the enterprise.

### Atomic Config Replace with Cisco Catalyst 9000 - DEVNET-2385
Speakers: Ashil Parekh (Cisco), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098443202001dqnf
Atomic Configuration and atomic config replace is becoming more and more requested, and this session dives deep into the newly introduced features within IOS XE and the Catalyst 9000 family. Being able to manage configuration in an atomic fashion allows teams to more effectively manage the change and network configuration drift. Using CLI or API the atomic config replace features will be demonstrated so that you can immediately benefit from leveraging either partial config or complete config replace. Easily replace ACL, policies, or interface configurations, or supply a complete config and that config will be set regardless of existing configuration.

### Authentication, Authorization and Provision for Cisco Collaboration - BRKCOL-2007
Speakers: Paulo Jorge Correia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098280435001dJSC
We will understand the best practice to bridge identity between cloud and on-premises and will understand when and how to leverage the different protocols and mechanisms (SCIM, LDAP, REST API) to do provision of users. We will also explore the new directory services for cloud register and linked devices/clients. We will understand how SCIM 2 will allow Cisco to better interconnect to Cloud IdM's We will understand how the Cisco Webex Azure wizard is going to improve the life of the collaboration administrators. We will explore new protocols like OpenID Connect. We also understand how Authentication and Authorization evolved in Cisco Collaboration, with the latest new features, like the support for multiple Idp per ORG.

### Automate Cisco IOS XE Device Configuration Using Terraform - DEVLIT-2083
Speakers: Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098426585001dYTm
Terraform is an open-source cloud native tooling. Terraform is an infrastructure provisioning tool with zero server-side dependencies and a single binary file. Terraform for Cisco IOS XE utilizes RESTCONF and the YANG interface. It is comparable to Ansible tooling, and the two can be used together.

### Automate Network Operation Tasks with NetDevOps and Source of Truth - BRKOPS-2357
Speakers: Patrick Mosimann (Cisco), Luca Gubler (onway (schweiz) ag)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098351277001d6Yb
If you want to learn more about using NetDevOps practices with a flexible Source of Truth (SoT) framework and how it can change the way you approach network operations, then join this session. Gain insights into an adaptable workflow showcasing how tools such as NetBox, Ansible, GitLab CI/CD pipelines, and more can automate tasks ranging from configuration management to testing and verification. Experience the integration of new sites into the SoT and their deployment using the Cisco Catalyst Center through practical demonstrations. Additionally, discover how pyATS can be leveraged for automated testing to validate configurations and ensure seamless operations. Whether you are using these tools or evaluating alternatives, this session is ideal for network engineers, DevOps practitioners, IT leaders, and architects. You will not only get access to what was demonstrated but also discover content that can be adapted to meet your needs. Join us and see network automation in action!

### Automate the Deployment of a Wireless Network with the Help of Cisco Catalyst Center - BRKOPS-2402
Speakers: Christian Gauer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098351632001dLdK
Join us in this session as we delve into the practicalities of deploying a Wi-Fi 6/6E network using Catalyst 9800 controllers and Catalyst access points, facilitated by Cisco Catalyst Center (formerly Cisco DNA Center). Our discussion will guide you through the process of designing for Software-Defined Networking (SDN) and executing an effective network deployment. Learn how to harness plug-and-play for effortless onboarding of wireless controllers and access points. We'll also explore how to position access points using maps from Ekahau imports. Finally, we'll focus on operating your network, taking full advantage of the monitoring capabilities offered by Catalyst Center, and efficiently managing software updates.

### Automating Cisco Multicloud Defense Deployments with Terraform: Best Practices and Techniques - DEVNET-2435
Speakers: Akshay Dubey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098444280001dIbi
In this session, we will explore how to leverage Terraform to automate the deployment and management of Cisco Multicloud Defense solutions. Attendees will gain hands-on insights into best practices, techniques, and real-world use cases that demonstrate the power of infrastructure as code (IaC) in enhancing security and operational efficiency across multi-cloud environments.

### Automating Cloud Monitoring: Accelerate Deployment with Terraform - DEVSKL-1551
Speakers: Abdiel Hernandez Fentanes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098451980001dR5Y
In today's rapidly evolving IT landscape, cloud infrastructure obfuscation has become a significant trend, creating challenges in maintaining visibility and resolving issues within cloud environments. This session is the second part of a two-session series designed to provide a comprehensive approach to cloud monitoring. While the first session focused on manual click-ops methods, this session will shift the focus to automation using Terraform. Attendees will explore how to automate their cloud monitoring strategies with Terraform, enabling quicker and more seamless deployment of monitoring solutions across AWS Cloud environments. We will provide a clear strategy for automating these processes, reducing manual intervention, and improving overall efficiency. Participants will discover the advantages of using Terraform to automate cloud monitoring deployment, enhancing the speed and reliability of their monitoring setup. The session includes a live demonstration of deploying ThousandEyes Cloud Insights using Terraform, illustrating the simplicity and effectiveness of automated deployment. This session is ideal for Site Reliability Engineers (SREs), IT network engineers, cloud engineers, and other professionals involved in managing and monitoring cloud infrastructures. A solid understanding of cloud infrastructure and basic experience with AWS Cloud services and Terraform is recommended. Familiarity with monitoring and troubleshooting cloud environments will be beneficial. By attending both sessions, you will gain valuable hands-on knowledge and practical skills to streamline your cloud infrastructure management, reduce downtime, and improve efficiency through both manual and automated approaches. This is an excellent opportunity to enhance your expertise and elevate your cloud monitoring capabilities. Please note that there will be a 15 minute break between sessions. If you do not attend the first session, you are not guaranteed a seat in this session as seating is first come first served regardless of previous registration.

### Automating Cloud Security: From Legacy Solutions to Agile Application Protection - PART ONE - DEVSKL-2801
Speakers: Brennan Bouchard (Cisco), Ed McNicholas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098452360001dPcw
In Part One [DEVSKL-2801] of this two part session, we focus on Manually deploying security to cloud. In Part Two [DEVSKL-2802] of this two part session, we focus on Automating the deployment of security to the cloud. Is your company transitioning applications to the public cloud and relying on outdated on-premises security solutions? Are you struggling to adapt these traditional solutions to secure more dynamic application stacks deployed in Kubernetes and serverless environments? If so, this session is designed for you. In this session, we will demonstrate how to secure applications either being migrated to, or built natively in the public cloud using automation. We will begin by discussing deployment models, such as Centralized and Distributed, to determine appropriate firewall placements, like Firewall Threat Defense (FTD) or Multicloud Defense. Next, we will explore securing workloads, focusing on segmentation and visibility options for cloud instances, containers, serverless applications, and Database as a Service (DBaaS) backends, utilizing emerging technologies such as Hypershield, Isovalent, Panoptica, and Secure Workload. By leveraging the visibility and telemetry from these solutions, we can enhance our data and streamline our Incident, Threat, Detection, and Response (ITDR) processes through integration with Splunk and Cisco XDR. Finally, we will review options for automating the entire architecture into a secure CI/CD pipeline.

### Automating Cloud Security: From Legacy Solutions to Agile Application Protection - PART TWO - DEVSKL-2802
Speakers: Brennan Bouchard (Cisco), Ed McNicholas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098452540001dISB
In Part One [DEVSKL-2801] of this two part session, we focus on Manually deploying security to cloud. In Part Two [DEVSKL-2802] of this two part session, we focus on Automating the deployment of security to the cloud. Is your company transitioning applications to the public cloud and relying on outdated on-premises security solutions? Are you struggling to adapt these traditional solutions to secure more dynamic application stacks deployed in Kubernetes and serverless environments? If so, this session is designed for you. We will demonstrate how to secure applications either being migrated to or built natively in the public cloud using automation. We will begin by discussing deployment models, such as Centralized and Distributed, to determine appropriate firewall placements, like Firewall Threat Defense (FTD) or Multicloud Defense. Next, we will explore securing workloads, focusing on segmentation and visibility options for cloud instances, containers, serverless applications, and Database as a Service (DBaaS) backends, utilizing emerging technologies such as Hypershield, Isovalent, Panoptica, and Secure Workload. By leveraging the visibility and telemetry from these solutions, we can enhance our data and streamline our Incident, Threat, Detection, and Response (ITDR) processes through integration with Splunk and Cisco XDR. Finally, we will review options for automating the entire architecture into a secure CI/CD pipeline.

### Automating Conversations and Customer Experience with AI Agent - DEVNET-1240
Speakers: David Veevers (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098430894001dxiU
With the advancements in AI and Large Language Models, we invite you to dive into Webex AI Agent and our new Customer Experience AI capabilities. Expect a exploration of AI Agent, its core and advanced features, including data training, multilingual support, action and its new LLM features! In this session, you'll learn about the new Webex AI Agent LLM feature set, and how Webex Customer Experience AI agent can create seamless integration strategies for Contact Centers such as Webex Contact Center. You'll also gain knowledge in how to go about setting up and creating your first LLM or Conversational Bots to power any of your digital channels OR your contact center! Transform your customer interactions with cutting-edge AI.

### Automating Detection & Response Outcomes using Cisco XDR & Generative AI - BRKOPS-1557
Speakers: Scott Dozier (Cisco), Steve Holl (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098346920001dIOm
In this session, participants will learn how to leverage Cisco XDR Automate to create no-to-low code workflows, equipped with AI, to automate investigation and remediation of security events occurring in their network environment to accomplish detection and response outcomes. You will leave this session with ideas on: Creating & executing Cisco XDR Automate workflows using a rich library of plug-and-play atomic actions How to turn your XDR Automate workflows into tools for AI Develop & deploy your first AI-powered XDR Incident Response Agent that works with Cisco Secure products All sample code presented during this session will be made available through DevNet Automation Exchange.

### Automating across domains: CCGM and Cisco Workflows deliver across domains - CISCOU-1037
Speakers: Magdy Louis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098401436001drPo
Ready to make your network smarter and your life easier? Join us for a quick 20-minute dive into how Catalyst Centre Global Manager and Cisco Workflows can supercharge your automation game. We'll show you how Catalyst Centre Global Manager serves as your central command, giving you control over different domains across your network. Then, explore Cisco Workflows to see how automating complex tasks can cut down on manual work and reduce errors. With real-world examples, you'll see the impact of automation on network management. Perfect for Cisco learners ready to boost their automation skills!

### Automation and In-Depth Troubleshooting of Cisco Catalyst 8000, ASR 1000, ISR, and SD-WAN Edge - BRKTRS-3475
Speakers: Frederic Detienne (Cisco), Olivier Pelerin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098395664001dFkA
In this session, we will start by explaining the architecture of the Cisco Catalyst 8000, ASR 1000, and ISR in autonomous or SD-WAN Edge mode. With this knowledge, we will gain in-depth understanding of traffic forwarding and advanced feature processing. We will also introduce RADKit, a troubleshooting automation tool, to accelerate network-wide or complex data capture. We will demonstrate problem isolation and root cause analysis on a live, feature-rich network such as routing, QoS, IPsec (FlexVPN and SD-WAN), and NAT.

### Balancing Generative and Foundational AI in an Observability Context - BRKOBS-2069
Speakers: William Cappelli (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098341566001dsMk
Both Generative and Foundational AI are required to ensure that Observability technology and processes deliver value. Nonetheless, the contributions they make are rather different. As the use of both becomes more widespread, practitioners need to understand how the two types of AI complement one another in an Observability context, and how to ensure each type is being optimally deployed. In this presentation, the speaker will discuss: The differences and similarities between Foundational and Generative AI What are the respective skill sets and culture required to make optimal use of each one? What is the proper architecture of an Observability platform that incorporates both Foundational and Generative AI?

### Become a network doctor using packet captures and Wireshark - CISCOU-2032
Speakers: Prapanch Ramamoorthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098406471001d3d5
Whether you have been a network engineer for a few months or several years, chances are that you have had to work with packet captures to answer the question "what is really happening?". Its no wonder then that packet captures and Wireshark are often referred to as a "network engineer's best friend". However, the key to success lies in knowing how to effectively use the tools in order to get to the bottom of the problem. Come and attend this session where you will get to learn tips and techniques for analyzing packet captures using live demonstrations and begin your journey towards becoming a network doctor.

### Beginner's Guide to ThousandEyes - BRKENT-1656
Speakers: Primoz Kolman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098305478001d12a
Your company relies on various connectivity options to ensure all your locations can connect over the same network. Your business-critical applications are migrating into the cloud and you rely on internet connectivity to process critical workloads. Your IT and networking teams are working on SD-WAN and SASE implementation, but are burdened with incident management, spending a great deal of unproductive time in war rooms, avoiding accountability, and struggling with inefficient tools. ThousandEyes plays a central role in identifying the source of critical performance degradation incidents. You will learn how ThousandEyes can help you gather and visualize data across network layers and quickly identify the source of critical incidents.

### Best Practices for Troubleshooting Cisco Catalyst 8000 Edge Platforms - BRKTRS-2572
Speakers: Michal Stanczyk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098393861001deDu
In this session, attendees will learn various techniques and tools used by Cisco TAC experts to diagnose Cisco Catalyst 8000 Edge Platforms effectively. The session is crafted to provide practical solutions to everyday challenges in the field, including common issues related to system performance and packet forwarding. Relevant serviceability capabilities that help reduce the time to identify the problem will be also covered. Participants will walk away with actionable guidance that can be immediately implemented in their day-to-day job.

### Best Practices of Virtual Port Channel in VXLAN - BRKDCN-2912
Speakers: Parth Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292785001dC2w
This session introduces the basic concepts and terminology of the virtual port channel and covers virtual port channel best practices for VXLAN environments. The session will cover how EVPN routes are advertised from vPC domains with traditional vPC, advertise PIP, and vPC fabric peering where the peer link is formed over fabric. The session will also cover use cases of VXLAN multi-site that can be satisfied with vPC border gateway.

### Best Practices to Simplify and Optimize Firewall D2Ops in a Hybrid Environment - BRKOPS-1402
Speakers: Vijayanand C D (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098346196001d1U4
Hybrid everywhere is the new norm in the IT industry, best practices helps to enhance the operations of firewall in this hybrid and distributed environment. In this session, we will discuss the operational best practices using three common types of deployments: - a) "On-prem" management with Firewall Management Centre (FMC) and Firewall Device Manager (FDM), b) 'saaS' management with Cloud-delivered FMC (cdFMC) in SCC platform and c) "Hybrid" management model using both On-Prem (FMC) and Cloud (cdFMC in SCC). In the end, you will understand the capabilities of each deployment model to deploy the most suitable best practices to optimize the firewall D2Ops for your organization.

### Beyond the spotlight: Securing the Paris 2024 Olympic Games - ITLGEN-1506
Speakers: Gemma Trowbridge (Cisco), Beatrice Ghorra (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098458622001dsmr
Securing the Paris 2024 Olympic Games was a transformative journey, showcasing the power of preparation, collaboration, and resilience. This session takes you behind the scenes to explore the meticulous planning and execution required to safeguard this iconic event. Attendees will gain insights into the pivotal role of robust infrastructure, comprehensive risk management strategies, and seamless teamwork across diverse stakeholders. By the end of this session, participants will leave with actionable lessons on how to plan, orchestrate complex projects, ensure readiness, and foster collaboration to achieve operational excellence in any high-stakes environment.

### Bidir-PIM Made Easy - CISCOU-2052
Speakers: Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098413231001dVHU
Understanding basic multicast routing is often a challenging task on its own, and Bidirectional PIM may seem like a topic from another world. And yet, explaining and understanding Bidir-PIM is surprisingly easy :) Come and see for yourself! We will touch the principles of multicast routing, discuss use cases for Bidir-PIM, and focus on explaining the Bidir-PIM mechanics while drawing analogies to another well-known protocol you might not have expected :)

### BlueCat and Cisco: Integrate, Automate, Protect and Analyze to Drive Network Change - PARENT-1432
Speakers: Ronny Wolf (BlueCat Networks)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098463170001dE13
Modern network complexities can introduce security risks, operational risks, and create huge operational expense on your organizations when not properly managed. Operational health of your network depends both on proper planning and management as well as active monitoring to reduce risks. During the session, participants will learn how BlueCat's helps you augment your Cisco implementations to address modern network issues. Learn about: The importance of managing this information and how it impacts your policy driven systems from firewalls to SecureAccess and SDWAN and LAN policies. How to leverage automation of IP changes and DNS to reduce operational load on your network teams How to leverage monitoring and analytics across your network devices and firewalls to prevent service interruptions.

### Boosting Customer Experience with Flow Orchestration in Webex Contact Center - BRKCCT-2345
Speakers: Dimitri Bokatov (Cisco), Yaroslav Bondar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098275991001d7XC
In the ever-evolving landscape of cloud contact centers, delivering an exceptional customer experience is paramount. This 1.5-hour session will provide an in-depth exploration of the Flow Designer, the pivotal tool for crafting superior customer journeys in Webex Contact Center. As we navigate through both basic and advanced features, including the latest enhancements, you'll gain a comprehensive understanding of how to leverage Flow Designer to meet and exceed business objectives. Participants will: Acquire a solid foundation in using Flow Designer to build and optimize IVR scripts Discover advanced features and the newest updates that enhance functionality and flexibility Learn best practices and practical tips for designing, implementing, and managing effective contact center flows The session includes real-time demos and practical business use cases. You'll see firsthand how to navigate the Flow Designer, apply its features, and integrate it seamlessly into your contact center operations. Join us to transform your contact center's customer experience with the power of Flow Designer in Webex Contact Center.

### Branch Provisioning using Terraform and Catalyst IOS-XE - DEVLIT-2107
Speakers: Serban Cozma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161420919001N0Xq
Terraform is an open-source cloud native tooling used to infrastructure-as-code scenarios. Terraform is an infrastructure provisioning tool with no code required on the server-side. Terraform for Cisco IOS XE utilises RESTCONF protocol and YANG data models. You'll leave this session with ideas to help you to automate device configuration using Terraform, see how easily a Secure Branch can be provisioned (IPsec tunnels to Umbrella Secure Internet Gateway and basic wireless configuration) and a comparison between Ansible and Terraform in automation scenarios. In terms of technical expectations, basic automation knowledge such as RESTCONF/NETCONF and YANG models is needed.

### Breaking Barriers: An Automation Framework for Multicloud Access with the SP Service Exchange - BRKENT-2666
Speakers: Jean-Marc Barozet (Cisco), Magdy Louis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098310851001dUyD
In today's rapidly evolving digital landscape, enterprises are increasingly leveraging multicloud environments to meet their diverse service requirements. The growing market demand for multi-cloud offerings necessitates a robust and clear blueprint for construction, automation, and provisioning to ensure seamless operations. This session delves into the intricate process of automating and constructing a service exchange that caters to the multi-cloud aspirations of customers. Furthermore, the session will explore ways to augment these core services with additional capabilities, all while maintaining agility, bolstering security, and embracing full-scale automation. Join us to discover the pivotal frameworks and best practices that will empower your organization to not only keep pace with the market demands, but also to excel in delivering multicloud services with unprecedented efficiency and reliability.

### Breaking the IT Bottleneck: Infrastructure Analytics and Risk Management as the Key to IT Agility - BRKPAR-1413
Speakers: Lauren Malhoit (IP Fabric)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098361087001dof0
IT leaders are expected to drive innovation with automation and AI all while maintaining security posture, but hidden risks, technical debt, and fragmented visibility continue to slow progress. Traditional approaches to digital transformation fail to account for the unknown unknowns interdependencies, compliance gaps, and architectural inefficiencies that derail IT projects and increase operational risk. In this session, we'll explore how infrastructure analytics and risk management provide IT leaders with the clarity needed to move beyond reactive troubleshooting and into proactive, strategic decision-making. It's time to turn infrastructure from a bottleneck to a business enabler..

### Bridging the Gap from AppDynamics to Splunk Observability Cloud for Hybrid Applications - BRKOBS-1605
Speakers: Alexander Stoklasa (Cisco Systems, Inc.), Daniel riquart (BPCE-IT), Vincent Ziec (BPCE-IT)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098340140001dXR8
In today's complex IT environments, robust observability is essential. Join us to explore how Splunk AppDynamics and OpenTelemetry can enhance your observability strategy. This session will provide a comprehensive overview of AppDynamics, a leading APM solution, OpenTelemetry, a standardized observability framework; and Splunk Observability Cloud, a leading cloud-native observability solution. Participants will be introduced to the Hybrid Agent, which accelerates the journey for application modernization. Participants will gain insights into: Integration techniques for merging telemetry data from AppDynamics and OpenTelemetry Enhancing visibility for existing services operated in the cloud with Splunk Observability Key use cases and demos, including emitting data to Splunk Observability Cloud and integrating AppDynamics and Otel instrumented services You'll leave this session with the knowledge to integrate and optimize telemetry data effectively and understand the value of the Hybrid Agent. The session includes live demos to illustrate critical use cases. A basic understanding of APM solutions and observability frameworks is recommended. Enhance your observability practices and drive better performance insights with Cisco AppDynamics and OpenTelemetry!

### Bridging the Gap: Executive Perspectives on ?Inclusion and Allyship - IF-1082
Speakers: Agostino Santoni (Cisco), Emma Carpenter (Cisco), Cynthia Koetsier-Beerten (Cisco Systems, Inc.), Sam Oliver (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098453431001dwge
In today's rapidly evolving tech landscape, diversity and allyship have emerged as critical components for fostering innovation and driving sustainable growth. This panel session brings together executives to share their insights and strategies on fostering inclusive practices within organizations. Panelists will explore the current state of diversity in the tech sector, identifying both challenges and opportunities. They will discuss how to champion inclusion for all and the importance of cultivating allyship at all organizational levels. Join us for this enlightening discussion and discover how we may continue to bridge gaps and drive progress in the tech industry.?

### Bring IT Into Focus with the AI Assistant for Networking - PSOENT-1860
Speakers: George Mokdessi (Cisco), Mohamed Abouelseoud (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098468512001dfG3
Join us to see how Cisco Networking uses advanced AI technology to deliver proactive business outcomes for our customers and your networks' users. We'll discuss our full-stack, use case-driven AI functionality, which utilizes the industry's largest networking data lake. As your network and users continue to evolve, cross-platform networking with automation, proactivity, and enhanced end-to-end security is more important than ever. That's where the AI assistant from Cisco comes in: to make your network work for you. In this session, we'll show you how to chat with documentation, get to root-cause analysis quicker, and help with change management.

### Build a Simple yet Powerful CI/CD Pipeline with Cisco ACI and Nexus Dashboard Insights - DEVNET-2473
Speakers: Alejandro De Alda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098444651001dD9W
Infrastructure as Code is a paradigm many companies are looking into, as it brings many benefits in terms of agility, time to market, consistency and more. CI/CD pipelines are a fundamental part of that model for operating a network, but sometimes can be perceived as difficult. In this session, you will explore how to build a simple pipeline to automate Cisco ACI that also includes a pre-change validation step with Nexus Dashboard Insights. You will have a better understanding of not only how to build the pipeline, but also how to automate pre-change validation jobs on Nexus Dashboard Insights using the recently released Ansible modules for ND.

### Building Advanced Workspace Automations for Cisco Video Devices - BRKCOL-3247
Speakers: William Mills (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098286468001dRF8
In this session, you will learn how to create a Workspace Integration and leverage the Webex REST APIs and Device Cloud xAPIs to process events and perform bulk configuration changes. You will also learn how to integrate your Workspace Integration with our Webex Connect CPaaS solution and its low-code flow designer to build your integration logic while also extending your integration's communication capabilities with Webex Connect's extensive communication channels. You will leave this session with knowledge and ideas on the following: How to create and activate a scalable Workspace Integration solution for your Webex Org. Real examples of use cases with Workspace Integration solutions and a breakdown of their architectures How to restrict your integration's Webex REST API and Cloud xAPIs access via Scopes and location-based access control How to receive, process, and respond to RoomOS-generated xEvents and xStatus changes relayed by Workspace Integration Webhooks or Long Polling services How to build your Workspace Integration on Webex Connect using webhook-triggered flows and its low-code designer

### Building BridgeIT: How a Design Team Led the Launch of the Cisco-Wide AI IT Assistant - ITLGEN-1517
Speakers: Kristin Wisnewski (Cisco), KC Lathrop (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098460452001d9wY
It is critical to safeguard the human element in the AI tools we use today. Only a team that prioritizes the user experience can holistically lead the strategic planning and execution to make that happen. Working with IT developers and partners across the enterprise, the Cisco IT Design team successfully led the launch of BridgeIT, Cisco's internal AI IT assistant, in 2024. Learn about the Design team's approach to leading the strategy based on user research, ensuring compliance with confidentiality standards, and keeping the user at the epicenter. Gain insights into the collaboration among IT and other business units, challenges, solutions implemented to design a platform enhancing employee productivity, and plans for the future.

### Building NIS2-Ready Cyber-Resilient Industrial Networks - PSOIOT-1015
Speakers: Ruben Lobo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098470159001dLvP
Industrial organizations and critical infrastructures are facing growing cyber threats. How can IT support the line of business in their efforts to digitize industrial operations while helping them to implement cybersecurity best practices to meet ever more stringent regulations such as NIS2? How can Splunk help gain visibility across both IT and OT domains to better detect threats and drive compliance? Join this session to learn how Cisco can help you build industrial networks that are easy to manage, scale, and secure: Why is the industrial network critical to deploy OT security at scale and comply with NIS2 requirements? What is the SOC of the future and how Splunk can help to unify IT and OT security? How to automate network segmentation protect operations? Which key capabilities to look for when building OT networks that are ready for AI and software-driven industrial processes?

### Building Next-Generation Data Centres: Lessons from Cisco - ITLGEN-1501
Speakers: Jeremy Foster (Cisco), Fletcher Previn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098457717001dOz4
AI is revolutionizing industries across the board, but there's no one-size-fits-all guide to adoption. To stay competitive, you need your infrastructure to support existing workloads and scale for the next wave of applications. But the increasing cost and complexity associated with new power, cooling, management and security demands many of which stretch beyond the walls of the traditional data centre can be daunting. Learn how Cisco is tackling these challenges in our own data centres, and how we're partnering with industry leaders and innovators to make this journey easier for you.

### Building Resilient SASE Solutions with Secure Connect - BRKMER-2577
Speakers: Ana Andrijic (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098337648001dqRY
As organizations transition to digitalized SASE solutions and increasingly rely on cloud-provided availability, a critical question arises: can you trust it to meet your uptime needs? This session will explore the best practices and designs of the Meraki Secure Connect SASE solution, demonstrating how to achieve the highest availability to ensure reliable, always-available, and secure connectivity for your users, regardless of their location. We will delve into designs and best practices for Meraki Secure Connect SASE, examining various methods for connecting to the Secure Connect cloud fabric. Scenarios covered will include the design, monitoring and troubleshooting of Meraki SD-WAN Auto VPN, new Catalyst or third-party IPSec, and Zero Trust Network Access (ZTNA) connections to Secure Connect cloud fabric. We will explore built-in resilient multi-tunnel deployments and available Equal Cost Multi-Path (ECMP) options. Additionally, we will discuss reliable connectivity to major cloud providers where your private applications are hosted. By the end of this session, you will understand how to best integrate and migrate your existing environments into the resilient Secure Connect solution, ensuring optimal reliability, high availability, and robust security for all users and applications.

### Building Scalable VXLAN BGP EVPN Fabrics for Enterprise networks with Catalyst 9000 Switches - BRKENS-2092
Speakers: Raj Kumar Goli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098299849001d531
This session will cover the enterprise BGP EVPN solution in the campus using Catalyst 9000 platforms. We will discuss the major drivers behind the adoption of the technology, supported features, interoperability between other Cisco platforms, and different design considerations when it comes to deploying it in production. This session is more focused on design considerations from an enterprise network perspective. During the session, we will also cover some best practices, newly added capabilities, and enhancements to the solution.

### Building Tomorrows Office: IT is the New Concrete, Blending Network, IoT, Collaboration and Data for a Smart Workspace? ? - BRKCOC-2819
Speakers: Gemma Trowbridge (Cisco), Anjitha Shanmughan (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279791001dkb8
Cisco IT's smart workplace combines the Network, Collaboration, IoT, Data, Observability and Security. This session is for engineers and architects responsible for enabling technology-powered workspace enhance efficiency, productivity, and user experience. Cisco IT will share how it's pioneering the office of the future by deploying Catalyst 90W UPOE+ switches, Cisco Catalyst Center, Identity Services Engine, Cisco Spaces, and a range of Cisco IoT partner technologies for Internet of Things (IoT), including lighting, shading, desks, and environmental sensors. We will discuss how data is utilized to control fundamental building systems like heating & cooling (HVAC), both automatically and by empowering employees to manage their workspace environment via Webex Devices. Additionally, we will explore how this technology facilitates way finding for employees who are using our smart workspace. From recent Smart Building deployments, Cisco IT will share challenges and lessons learned. The session will explore practical use cases and architectures, providing valuable insights and actionable knowledge to implement in your own smart workplace projects.

### Building Transport-Grade Packet-Based Networks with Routed Optical Networking - BRKOPT-2016
Speakers: Christian Schmutzer (Cisco), Kent Dailey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098359244001dbGH
In order to provide transport services and meet strict SLAs, most of today's networks are created with multiple layers and topologies. These include fiber, optical, OTN, and routing hardware deployed across each other. This session will detail current deployment scenarios and explore an opportunity to collapse and simplify the network where the fiber topology = routing topology leveraging Routed Optical Networking, while meeting transport grade requirements for network resiliency, service protection, and SLAs.

### Building Zero-Trust Campus Networks with BGP EVPN on Cisco Catalyst 9000 Switches - BRKENS-2830
Speakers: Benjamin Pimor (Cisco), Thomas Matzeu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098302399001dP5y
This session will show you how to deploy zero trust solutions on a Cisco Catalyst 9000 BGP EVPN fabric. Traditional campus networks do not meet today's requirements to satisfy customer business needs. To solve their challenges, the network fabric has proven itself to be one of the best solutions. Especially BGP EVPN fabric, which brings flexibility in terms of architecture, deployment, and automation. In this session, we will focus on the next level of topics and see how to integrate security, including secure underlay with IPsec, security group-based access control, service chaining fabric, and automated threat containment. With this session, attendees will have the opportunity to see demonstrations and take away some configuration examples.

### Building a Resilient Future: Key Stages in Observability Excellence - CENOBS-1500
Speakers: Laura Vetter (Evolutio), Mike Cohen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228646576001sOWY
Join us to discover the future of observability. We will dive into the four key stages essential for building a leading observability practice and talk about incorporating AI the right way for maximum impact. You will learn how Splunk Observability, supercharged by AppDynamics, provides unparalleled visibility across even the most diverse tech environments, and hear real-world success stories from companies using it today for faster troubleshooting and improving reliability on an ongoing basis.

### Building a Successful AI Stack with Cisco UCS Solutions and Best Practices - BRKCOM-2018
Speakers: Archana Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098287193001dHkk
Artificial Intelligence (AI) is revolutionizing industries by offering unprecedented capabilities and efficiencies. However, harnessing the full potential of AI requires a robust and scalable infrastructure. Join us in this session as we explore cutting-edge deployment models and best practices using the Cisco Unified Computing System (UCS). In this session, you will gain insights into: -Cisco Compute for Hyperconverged with Nutanix GPT-in-a-Box: Learn how to streamline AI workloads and enhance performance with our integrated hyper-converged solutions. -Cisco Converged Infrastructures for Inferencing and AI RAG: Discover the advantages of converged infrastructures designed specifically for AI inferencing and Retrieval-Augmented Generation (RAG). -AI with Cisco Data Intelligence Platform: Explore how the Cisco Data Intelligence Platform can empower your AI initiatives by providing comprehensive data management and analytics capabilities. -ML Operations with Red Hat OpenShift AI: Understand how to manage and scale machine learning operations efficiently using the powerful combination of Cisco UCS and Red Hat OpenShift. We will share practical insights, real-world use cases, and best practices to help you build a resilient and high-performing AI stack tailored to your organization's needs. This session will equip you with the knowledge and tools to leverage Cisco UCS solutions for your AI initiatives successfully.

### Building and Sustaining Diverse Teams and Communities in Times of Economic Uncertainty in the Hybrid World - IF-1956
Speakers: Theresa Decola (Cisco Systems, Inc.), Jessica Quiroga (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098456625001duOC
Often there is a focus on creating a diverse pipeline for hiring candidates, but less of a focus on retention and understanding why diverse employees choose to leave for other opportunities. When selling to diverse customers it is important to ensure that the teams supporting them understand and empathize with them, not just as potential customers but also as humans who bring their whole selves and needs to work. This session focuses on the strategies we've developed while running the San Francisco chapter of the Cisco PRIDE organization.

### Building for the Future - Top IT Trends - ITLGEN-1505
Speakers: Chintan Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098458441001dXaW
Staying ahead of the curve is imperative for all IT professionals. This session will help by giving you valuable insights into the impact of emerging technology trends, industry shifts and innovations set to transform our industry. Chintan will explore how advancements in AI, cybersecurity, networking, quantum and more will redefine the IT landscape over the next few years. You will gain a peak into the future as to how these predictions may influence your strategic planning and operational approaches, with the aim to get you ready to navigate the ever changing world of technology.

### Building the AI-Ready Data Center - PSODCN-1871
Speakers: Swetha Velamuri (Cisco), Gerald Richard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098467781001dRrP
We will showcase the latest innovations in Cisco Nexus 9000 Series switches which would transform your data center fabrics into secure non-blocking lossless AI-ready data center fabrics. We are enabling the design of secure next-generation AI/ML fabrics with the introduction of new high port density 800G Ethernet switches and new security infused 100G Ethernet switches that melt security into the network. These new switches extend the broad portfolio of Nexus 9000 Series modular/fixed 400G/100G switches and combined with the Cisco Data Center Networking Blueprint for AI/ML Applications ensure interoperability and consistent performance with GPU vendors to provide a robust framework for optimizing AI/ML applications. Additionally, Cisco Nexus Hyperfabric AI and AI Pods provide options for a cloud-managed on-premises high-performance AI clusters and speed up infrastructure deployments for AI inferencing with validated designs.

### CCNA Prep brings a DNS Deepdive: Exploring a Backbone of Network Communication - CISCOU-1046
Speakers: Hank Preston (Cisco), Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098404696001deSG
Step into the dynamic world of DNS in this engaging, lab-focused live event. Discover how to configure basic DNS servers and clients while unraveling the mystery of how domain names translate into IP addresses. Through practical demonstrations, you'll see firsthand how DNS keeps your network running smoothly and efficiently, mastering this vital technology before you take your CCNA exam.

### CCNP Enterprise Network Troubleshooting Deep Dive - BRKCRT-2285
Speakers: Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098289237001ddeC
On Monday, your colleague Max tried to upgrade the network, but now Rohan can't access data on a server, Emma can't connect to the internet, and Joe can't SSH to a core switch. What can you do? Where do you start? This session will help you improve the skills and knowledge you need to maintain an enterprise network and to diagnose and resolve network problems quickly and effectively. You will hone your troubleshooting skills in real-world networking scenarios in preparation for the CCNP Enterprise ENCOR and ENARSI certification exams. Attendees should already be familiar with the implementation and verification of enterprise routing and switching technologies, such as: Layer 2 switching (VLANs, trunks, port security, LACP, PAgP, STP) Inter-VLAN routing HSRP, VRRP, and GLBP EIGRP, OSPF, and BGP Layer 3 path control Redistribution IPv6 networking This session is for you if you are currently preparing for CCNP Enterprise certification, or seeking to advance your existing troubleshooting skills relating to IPv4 and IPv6 network solutions. During the session, you will review some basic troubleshooting methodologies and procedures, as well as participate in an interactive debrief of the issues presented.

### CI/CD Pipelines for Infrastructure Automation - BRKDEV-2117
Speakers: Adrian Iliesiu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098298528001dfC8
CI/CD pipelines have been used as part of software development lifecycle for years. With the advent of network programmability and infrastructure automation, it is now possible to extend the benefits of using CI/CD pipelines to also manage and monitor infrastructure. In this talk, I will go over how to build and use a CI/CD pipeline based on GitLab CE for infrastructure management and automation. The pipeline can be used for testing network configurations in a Cisco CML environment before deploying to production. Other components of the pipeline are Cisco pyATS, Ansible and Cisco Open NX-OS.

### CUBE v14 Updates - BRKCOL-2314
Speakers: Hussain Ali (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098283567001dsxs
CUBE Enterprise has been Cisco's flagship on-premises session border controller (SBC) on the routing platform for over a decade. We have also introduced vCUBE on Azure/AWS and CUBE on the Catalyst 8200/8300 series platforms. This session will begin with a quick recap on CUBE followed by new features introduced as part of various v14.x releases such as Managed Gateways from the cloud, RTP keepalives for NAT traversal, DNS SRV load balancing, multiple TLS profiles, and support for non-Cisco cloud calling offers. CUBE as a Local Gateway for Webex Calling and Survivability Gateway will be covered in BRKCOL-2312.

### Calling Interoperability with Microsoft Teams - BRKCOL-2067
Speakers: Sara Macias Salete (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098281015001dik6
This intermediate-level session provides attendees with a detailed understanding of how the Cisco communication solutions can interoperate with Microsoft Teams, with a specific focus on the calling scenarios. The following topics will covered in this breakout: Using Cisco Phones and Peripherals with Microsoft Teams (overview) Direct Routing for Microsoft Phone System (overview) Direct Routing with CUBE Direct Routing with Unified Communications Manager via Cisco Unified Border Element (CUBE) Cisco Call for Microsoft Teams Client-side integration for Webex Calling and Cisco Unified Communications Manager A basic understanding of Cisco calling solutions is required to get a good understanding of the content in this session. For a deeper understanding on Microsoft Direct Routing, please consider attending the session BRKCOL-2314: CUBE v14 Updates.

### Catalyst 9000 Series Switching Family: Access - BRKARC-2098
Speakers: Minhaj Uddin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098274302001djbe
This session will cover the platform overview of Catalyst 9000 access switches. It will share the details of the Catalyst 9000 product portfolio, which will include new additions in fixed and modular access series: Catalyst 9200, Catalyst 9300/X, and Catalyst 9400/X. The session will discuss the component at the heart of these switches, which is the ASIC. It will also cover common attributes, technologies, and features of Catalyst 9000 switches.

### Catalyst 9000 Series Switching Family: Core and Distribution - BRKARC-2099
Speakers: Kenny Lei (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098274499001d4oQ
This session will cover the platform overview of Cisco Catalyst 9000 Series core and distribution switches. It will share the details of the Catalyst 9000 product portfolio, which will include new additions in fixed and modular core and distribution switching series (Catalyst 9500/X and Catalyst 9600/X). The session will talk about the component at the heart of these switches which is the ASIC. It will also cover common attributes, technologies, and features in the Catalyst 9000 Series Switches.

### Catalyst 9000 Sustainability and Smart Buildings - BRKENS-2099
Speakers: Veera Bhaskar Mutyala (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098300405001dDEK
This session covers Catalyst 9K Switching innovations for sustainability, focusing on energy efficiency and regulatory compliance. Topics include new power savings features, 90-watt PoE, DC microgrid designs, and smart building capabilities. Through IOS-XE and Catalyst Center, we'll demonstrate how analytics and automation support ESG goals, energy savings, and improved reporting.

### Catalyst 9800 Configuration Best Practices - BRKEWN-2339
Speakers: Justin Loo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161403942001Njek
Understand the best practices, design recommendations, and useful practical deployment tips on how to successfully migrate from your current AireOS wireless network to a Catalyst wireless one, covering from day 0 to day n.

### Catalyst SD-WAN Application-Aware Routing, SASE, and Policy Innovations - BRKENT-2428
Speakers: Karthik Kumar Thatikonda (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098309046001doSP
WAN path quality degradation issues can impact the application quality and experience of your users accessing business-critical applications in your organizations. How do we plan and design our network to address these path quality degradation issues and improve application experience? How do we ensure traffic is symmetrical for these applications from branch to DC and vice versa. The session will address the new capability in SDWAN called Enhanced Application Aware Routing (AAR) and AAR Remote color preference. The session will also cover the SSE/SASE innovations that secure traffic towards the internet destinations. At the end of this session an IT or MSP Netops administrator should be able to deploy these innovations in the SDWAN network to optimize the application experience for their users who are accessing business-critical applications.

### Celebrating a Decade of Digital Transformation: A Retrospective on Cisco's Country Digital Acceleration in EMEA - CENIF-1004
Speakers: Guy Diedrich (Cisco), Valeriya Ionan (Ministry of Digital Transformation of Ukraine)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227081336001JKRd
Join Guy Diedrich, SVP & Global Innovation Officer at Cisco, for an inspiring keynote session at Cisco Live EMEA, celebrating a decade of the Country Digital Acceleration (CDA) program. This session will delve into the transformative impact of CDA's strategic investments and partnerships across Europe, the Middle East, and Africa. Discover how Cisco, in collaboration with customers and partners, has driven innovation, strengthened digital infrastructure, and empowered communities. Hear from industry and government leaders about the program's achievements and gain valuable insights into how these advancements are shaping the future of digital transformation in the region.

### Chatting with your SD-WAN Network - Power of AI & LLMs to Simplify SD-WAN Network Operations - BRKENT-2156
Speakers: Sai Suchandan Reddy Marapareddy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098306918001d4TB
Cisco Catalyst SD-WAN builds a secure, unified connectivity over any transport and provides simplified operations with centralized management, policy control and application visibility across the Enterprise WAN Network. Unified SD-WAN Assurance & Network Wide Path Insights (NWPI) integrated within the SD-WAN Manager, provides extensive insights into network and application performance issues. In this session, we will explore how the power of Large Language Models (LLMs) and AI/ML can be leveraged to gain enhanced visibility into network & application performance and simplify network operations. By making Assurance & NWPI data more accessible and actionable, these advanced technologies can transform the way you manage your network. Come to this session to see the live demo of seamless integration of NWPI and LLMs in action!

### Cisco 8000 and OVHcloud a Successful Adoption since 2020 - CSSSPG-2389
Speakers: Antoine Petit (Cisco Systems, Inc.), Laurent Galais (Cisco), Simon Peccaud (OVHcloud)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098421931001dlr5
This presentation showcases a customer success story that highlights Cisco 8000 Series routers deployment and use cases at OVHcloud; European leader in Cloud Infrastructure. The Cisco 8000 Series, known for its groundbreaking Silicon One architecture, advanced routing capabilities, and energy-efficient design, provided the customer with a competitive edge in network performance and operational efficiency. Subsequent sections detail the deployment process, the collaborative efforts between OVHcloud's team and Cisco's support specialists, and the seamless integration of the 8000 Series routers into the existing network ecosystem. The conclusion of the presentation underscores the successful partnership between OVHcloud and Cisco, reflecting on the lessons learned and next steps.

### Cisco ACI Multi-Pod Design and Deployment - BRKDCN-2949
Speakers: John Weston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098295310001dnlw
Deploying ACI across multiple data center locations or rooms to ensure redundancy is a common requirement for enterprises and service providers. This session will explore the ACI Multi-Pod solution, which uses a single APIC controller cluster to manage and connect separate ACI sites over an inter-pod network. We will discuss: The functional components of the Multi-Pod architecture Deployment considerations, including APIC cluster options Updated with ACI features for Multi-Pod fabrics, such as: Connecting APIC clusters over a Layer 3 network Virtual APIC clusters Multi-Pod back-to-back connectivity without an IPN BGP underlay support Join us to gain insights into effectively deploying the ACI Multi-Pod solution.

### Cisco Catalyst 8500 Series Edge Platform Deep Dive - BRKARC-2885
Speakers: Sumant Mali (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098274680001d1eg
Enterprise networks today are seeking more powerful WAN aggregation edge routers. The Catalyst 8500 Series Edge Platforms are purpose-built to deliver high-performance WAN aggregation for SD-WAN and routing. The session will start with a basic platform overview and will evolve into a deep dive of data path ASIC, the third-generation quantum flow processor, control and data plane architecture, port configurations, product comparisons, performance, and positioning. At the end, it will cover SD-WAN and traditional routing use cases and troubleshooting best practices for real-world deployments.

### Cisco Catalyst 9000 Series, Cisco Silicon One, and IOS XE Architecture and Innovation - BRKARC-2092
Speakers: Shawn Wargo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098273796001dV89
This is a combined session covering Cisco ASICs on Catalyst 9000 Series Switches (BRKARC-2091) and Cisco IOS-XE on Catalyst 9000 Series Switches (BRKARC-2090). This level II (intermediate) session will focus on the hardware and software components upon which the Cisco Catalyst 9000 Series Switches are built. Key topics covered regarding Cisco IOSXE on Catalyst 9000 Series Switches: Why do we need ASICs? (CPUs vs. FPGAs vs. ASICs) Cisco UADP and programmable ASICs (the heart of Catalyst 9000 Series Switches) An introduction to Cisco SiliconOne ASICs (what's new and different?) A glimpse into the future of Catalyst 9000 Series Switches hardware Key topics covered regarding Cisco IOS-XE on Catalyst 9000 Series Switches: Recap of the basic principles and history of Cisco IOS Overview of the software components of Catalyst 9000 IOS-XE Key innovations enabled by IOS-XE releases 17.9-17.12 A glimpse into the future of Catalyst 9000 Series Switches software This session can be used to help design and position different Catalyst 9000 Series products with a deeper understanding of the underlying hardware and software.

### Cisco Catalyst Center Platform: APIs, Event Notifications, Integrations, and DevOps Resources - DEVNET-1087
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098429057001dqrq
Do you have Cisco Catalyst Center in production, in the lab, or are you just interested in getting started? This session will focus on how to manage your network infrastructure-as-code using the Catalyst Center platform. We will review the Catalyst Center REST APIs, real-time event notifications, out-of-the-box and open-source integrations, and how to build a custom integration. We will also go over the developer resources available to accelerate the consumption of Catalyst Center REST APIs. The session will be use-case based, exploring the options to build innovative new solutions, services, and integrations on top of the Catalyst Center platform. Demos and Python and JavaScript sample code are included, as needed.

### Cisco Catalyst SD-WAN Fundamentals - CISCOU-2030
Speakers: Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098405763001dvhm
Learn the basics of Cisco Catalyst SD-WAN in this short, interactive session. Discover what all the hype is about Cisco Catalyst SD-WAN, how it works, why it's augmenting the traditional WAN, and how it makes it easier to securely access cloud-based services such as AWS, MS Azure, GCP, Cisco Umbrella, Cisco ThousandEyes and Megaport. We will look at some customer use-cases and benefits, as well as see how Cisco Catalyst SD-WAN can help solve today's business challenges.

### Cisco Certifications Portfolio Updates - CISCOU-1027
Speakers: Mubasher Nawaz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098398199001dBcc
Learn about upcoming changes to the Cisco Certification exams aligning with Annual Certificaiton roadmaps and get answer to all your Certification quesitons as you prepare for your Certification Journey from Entry to Expert

### Cisco Hypershield: Mastering Next-Generation Security - BRKSEC-2265
Speakers: Jeroen Wittock (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098372908001dnH8
If ever I did a security masterclass in 90 minutes, this is it. We will talk about eBPF, dual dataplane, and the many different types of AI that are the core of Cisco Hypershield. In addition, we will spend some time on our vision where security operators and administrators can move away from writing policy and spend more time on increasing the overall security of the environment in it's entirety. We will show the tools to do that, as well as the tools that will make it easy to discover if any known CVE's are applicable in your environment, and how to deploy shields to address these CVE's without impacting the application itself. We'll show how Cisco Hypershield will make it easier to deploy the right segmentation strategies for your specific environment, and how to keep those segmentation policies current to actual state of your environment. The session will end with an overview of the native automation capabilities through the API and demo scripts.

### Cisco IP Phones, Headsets, and Webcams: The Product Updates that we all Need to Know - BRKCOL-2068
Speakers: David Scott (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098281196001d8B3
Explore the latest information on features for the Cisco IP Phones along with the many Cisco peripherals that can benefit your organization. Deep Dive on the new Cisco Desk Phone 9800 Series Hotdesking and meetings Phone migration DECT Wireless Phones and Cisco Wireless Phones 840/860. Which to deploy where? Cisco Headsets including Microsoft Certified Cisco Headsets

### Cisco ISE Meets Azure Cloud. Deploy, Automate, Integrate with Entra ID and Intune - BRKSEC-2416
Speakers: Eugene Korneychuk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098373994001dDTl
ISE perfectly fits into ZTN, Today, ISE can be a Azure cloud native solution as well. This session will unleash ISE in Azure capabilities, talk about ISE deployment in Azure, Automation of such deployment, Integration with Entra ID and Intune.

### Cisco ISE Performance, Scalability and Best Practices - BRKSEC-3234
Speakers: Jesse Dubois (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098382318001d23o
In today's world of constant attacks, malware and Ransomware, it's important to design, deploy and manage your network with an identity aware secure access platform. Cisco ISE plays a key role for many security solutions and is also one of the main pillars in the overall Cisco's Software defined Access Architecture. This session will show you how to deliver scalable and highly available access control services using ISE for wired, wireless, and VPN from a single campus to a global deployment. Methodologies for increasing scalability and redundancy will be covered, such as load distribution with and without load balancers, optimal profiling design, lessons learned from the trenches, as well as serviceability tips and tricks to help you gain optimal value and productivity from ISE. Attendees of this session will gain knowledge on how to best design ISE to ensure peak operational performance, stability, and to support large volumes of authentication activity. Various deployment architectures will be discussed including ISE platform selection, sizing, and network placement. Cisco ISE also enables cross-platform network system collaboration across your IT infrastructure by using pxGrid to monitor security, detect threats, and set network policy. Manage assets, configuration, identity, and access. The session will go through such deployment considerations and common architectures.

### Cisco IT's Blueprint for SSE Transformation - ITLGEN-1508
Speakers: Roel Bernaerts (Cisco Systems, Inc.), Sanjeet Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098458993001d3lU
Welcome to a new era where security meets simplicity, with user experience at the forefront. In our fast-paced digital world, Security Services Edge (SSE) is changing the game. It not only simplifies IT operations but also enhances the hybrid work experience and fortifies cybersecurity. This means employees can work smarter and safer from anywhere. In this session, we will share Cisco IT's journey, featuring our use of Cisco Secure Access, and the best practices we've developed along the way. Whether you're just starting to explore or looking to optimize your current setup, you'll find valuable insights to guide your transition.

### Cisco IT's Journey to SSE - Enabling Hybrid Work with Cisco Secure Access - BRKCOC-2040
Speakers: Roel Bernaerts (Cisco Systems, Inc.), Sanjeet Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279387001dtwg
In this session, you'll discover how Cisco IT is addressing real-world IT challenges with Cisco Secure Access (SSE), transforming the hybrid work experience into a more secure and seamless journey. We'll share our strategic vision and highlight the value this solution brings to IT organizations. Learn how we've transitioned our remote access VPN and Zero Trust access services to the cloud. Discover how we've embraced Zero Trust principles to secure our business and tackle modern challenges, such as unsanctioned GenAI use. Gain insights from our experiences and practical tips on Cisco's effective approach to IT security and user satisfaction.

### Cisco IT: Streamlining Network Management and Decisions with Catalyst Center Automation and Splunk - BRKCOC-2483
Speakers: Marianna Pittokopiti (Cisco), Dipesh Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279596001dOce
In the fast-paced world of network management, automation is essential for achieving efficiency and reliability. This session will delve into the powerful automation capabilities of Cisco Catalyst Center, focusing on three critical functionalities: automated software upgrades with SWIM (Software Image Management), automated incident creation utilising predictive AI network trends with automated resolution and last but not least, data visualisation in Splunk. To enhance efficiency and minimize errors, Cisco IT developed Atomic SWIM, an automated system that leverages Catalyst Center's APIs to schedule and activate upgrades while ensuring system health. Day N templates enable the quick and standardized configuration of network devices, ensuring compliance with best practices. Additionally, automated incident resolution can be achieved by deploying the relevant Day N template to correct any incorrect or outdated configurations. The Catalyst Center APIs are also employed to pull various data sets and send it to Splunk for comprehensive visualisations, empowering data-driven decision-making. One of the key projects driven by Splunk data insights is Managed Access, where we transitioned to a certificate-only wireless. By leveraging data visualised in Splunk, we were able to identify devices still using username/password as well as have an understanding of the user-base being affected to ensure a smoother user-experience during migration. This session will explore the practical applications of Catalyst Center and Splunk, highlighting real-world scenarios and lessons learned from Cisco IT's deployments. Attendees will gain insights into how these tools can be leveraged together to enhance network management, drive strategic projects, and make more informed decisions.

### Cisco Live Network and NOC: Panel Discussion – PNLNMS-1035
Speakers: Lionel Hercot (Cisco), Andrew Yourtchenko (Cisco), Remco Kamerman (Cisco), Joe Clarke (Cisco), Luke Hebditch (Cisco), Michal Kowalik (Cisco), Anthony Jesani (Cisco Systems, Inc.), Sebastien Marchal (Cisco Systems, Inc.), Christian Gauer (Cisco), Abhinav Singh (NETAPP INC), James Botting (Cisco systems, inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1741306971570001yXXV
Have you ever wondered what is involved building and tearing down a network in the span of a week? Our panelist will talk about the Cisco Live network and the technologies in use, as well as the Network Operations Center or NOC that manages it. We'll discuss what worked, leading practices that we followed, and statistics from the event. This is a must-see panel for anyone involved in operating a network, especially one that has to move with agility and adapt constantly. We hope you have more than a few days to build and fine tune your network. But even so, you will benefit from hearing what we did, how we did it and what we learned all over the course of the week. We will have panelists representing Routing, Switching, Wireless, the design, products and roll out of security as well as Cisco's Remote Monitoring Service for security plus Storage, Network Management and of course fun stats from the show.

### Cisco Meraki Dashboard Meets Cisco Catalyst Center - Better Together! - BRKOPS-1894
Speakers: Priya Ram (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098347997001deLN
This session unveils the convergence of Cisco's Meraki Dashboard and Cisco Catalyst Center, designed to enhance hybrid network management. Participants will learn about Meraki Dashboard and Catalyst Center's seamless convergence, and the architecture that supports this integration. The session will also highlight the advantages of unified hardware and licensing for operational simplicity. Learn how Cisco's unified management solution can transform your network management strategies, allowing you to embrace the hybrid world with confidence and efficiency. Live demonstrations will showcase smooth transitions between the cloud and on-prem environments and participants will understand how Cisco ensures operational simplicity for future-ready networks. Real-world examples will illustrate troubleshooting user and device issues across both platforms.

### Cisco Multidomain for SDA, SD-WAN and ACI Automation with End-to-End Policy - BRKXAR-2001
Speakers: Markus Harbeck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098396764001dAiN
What is Cisco Multidomain for SDA, SD-WAN and ACI? Cisco SD-Access is the modern way of automating the Campus while SD-WAN is structuring and modernizing the WAN, but how do they come together? And how can you extend your Microsegment all the way to the Datacenter with ACI? The session will demonstrate how the SDA-SDWAN-ACI interfaces works between Cisco Catalyst Center, SDWAN Manager and APIC. The session shows how build an end-to-end software defined enterprise from the campus to the DC branch and into the data center. The session will focus on design best practices for SDA to SDWAN and ACI. Finally, a live demonstration will allow the attendee to visualize the building of the software defined enterprise and secure segmentation.

### Cisco Nexus 9000 Architecture - BRKDCN-3939
Speakers: Faraz Taifehesmatian (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098297811001dhx0
This session presents an in-depth study of the architecture of the latest generation of Nexus 9000 modular and top-of-rack data center switches. Topics include ASIC architecture, forwarding mechanics, and physical design elements, as well as a discussion of key hardware-enabled features and capabilities that combine to provide high-performance data center network services.

### Cisco SD-Access LISP VXLAN Fabric Best Practices: Design and Deployment - BRKENS-2502
Speakers: Mahesh Nagireddy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098300959001d12c
Join us in this interactive session to learn about the design and deployment best practices adopted by our customers while designing the Cisco SD-Access LISP VXLAN Fabric network. This session includes a brief introduction of Cisco SD-Access components, and dives into design and scale considerations and deployment options, for single-site designs covering greenfield and brownfield converged wired and wireless infrastructures. Participants will gain insights into how Cisco SD-Access can provide a journey to digitalization and immediate benefits at every step of embracing the zero-trust architecture. This session will focus on multi-site design and deployment options, with the intent to provide end-to-end segmentation with consistent policy across the enterprise. It is highly recommended that attendees have an understanding of the Cisco SD-Access architecture, which can be learned with previously recorded sessions (BRKCRS-2810 and BRKCRS-2811) available in the Cisco Live On-Demand library.

### Cisco SD-Access Migration Tools and Strategies - BRKENS-2827
Speakers: Kedar Karmarkar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098302218001dLmB
Previous Cisco Live sessions such as DGTL-BRKENS-3822 and BRKENS-2008 have shared real-world migration tools and strategies along with recommended best practices for migrating existing networks to Cisco SD-Access. This session augments the existing content to include the latest SD-Access features and lessons learned from the field. It is highly recommended that attendees have an understanding of SD-Access operation, design, and migration. This information is available in the On-Demand Library of ciscolive.com. Sessions recommended for review prior to attending this seminar are: BRKCRS-2810, BRKCRS-2502, BRKCRS-2812, BRKENS-2008 and DGTL-BRKENS-3822.

### Cisco SD-Access and Multi-Domain Segmentation - BRKENS-2819
Speakers: Jerome Dolphin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098301669001dkfN
Using Cisco SD-Access LISP Fabric as a foundation, this session will explore and integrate important LAN, WAN and cloud segmentation solutions. Theory will be reinforced with real-world demonstrations of each concept. Beginning with Cisco Catalyst Center, cabled networking devices, and a basic preliminary configuration, you will learn how and why to build end-to-end network segmentation while preserving and adapting security context. During this session you'll learn about: Cisco Software-Defined Access, Transit routing and VRFs Identity Services Engine (ISE) and Security Group Tags (SGT) SXP and pxGrid for sharing of security context Cisco Secure Firewall SGT-aware policy Segmentation policy extended from the LAN to ACI, AWS and the traditional data center Endpoint Analytics Cisco Extended Detection and Response (XDR) for threat identification and containment Please note that due to the breadth of material covered during this presentation, a basic level of knowledge of all in scope topic domains is recommended.

### Cisco SD-WAN, Hidden Complexity Revealed: How Cisco TAC Addresses Really Tricky Problems - BRKTRS-3050
Speakers: Denis Kodentsev (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098394584001dWf2
The key benefit of Cisco SD-WAN is providing an easy and scalable way to implement and manage extremely complex WAN networks. This comes with a cost: the complexity does not go anywhere and becomes hidden. It's fine for normal network operations, as most of the outages could be easily addressed by leveraging the vManage GUI or by CLI in case of tricky issues. There's also a well-developed set of troubleshooting tools used by Cisco TAC also available for customers. But what if something goes wrong and the issue requires a much deeper understanding of the "moving parts" working in the SD-WAN background? These moving parts are essentially logically separated processes operating on a WAN edge router or SD-WAN controllers continuously interacting with each other. Such interactions could be really intensive while also insightful for understanding how Cisco SD-WAN works. These processes mostly do not reveal themselves as they deliver low-level logic of the Cisco SD-WAN technology and could be considered as "hidden" to the end user. The session will explore key aspects of the hidden complexity of Cisco SD-WAN technology so customers and partners can leverage the knowledge to navigate across very complex issues and situations while troubleshooting and designing their Cisco SD-WAN networks. We'll start with the troubleshooting tools available today and how Cisco TAC utilizes them. What are a tool's scope, applicability, limitations, and best practices? Next, to translate the tool's output into something meaningful we'll dig deep into control-plane and data-plane processes running on an SD-WAN edge router and how they interact with each other. What is the expected behavior and what are the major dependencies out there? Finally, we'll check some techniques we're using in TAC to navigate around the most troublesome issues - intermittent issues which are really hard to chase and even harder to isolate.

### Cisco SD-WAN: Better NetOps for Better DevOps - DEVNET-1318
Speakers: Sai Suchandan Reddy Marapareddy (Cisco), Alberto Rodriguez-Natal (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098431997001dAAh
Modern applications, typically made of many on-prem, cloud, and SaaS components, are more distributed than ever and require a solid WAN foundation that provides optimal connectivity services. This challenges the Network Operations teams (NetOps) to provide WAN services to a very agile community of Development Operations teams (DevOps) who use agile application infrastructure (e.g. Cloud, Kubernetes, etc) to dynamically deploy and configure those distributed application components. This session will showcase some Cisco Catalyst SD-WAN capabilities, that enable seamless network alignment with the application infrastructure, to help reduce the friction between NetOps and DevOps teams. Attendees will learn about integrations that enable automated discovery of Kubernetes clusters and Kubernetes applications, Cloud OnRamp features that help with cloud deployments and SaaS traffic optimization, and different APIs that allow to configure all this programmatically and see it in action with a live demo. Some understanding of SD-WAN, Kubernetes, and Cloud is helpful, but not required.

### Cisco SD-WAN: Start Here - BRKENT-2108
Speakers: Lars Granberg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098306208001dLRZ
Cisco SD-WAN is on everyone's lips these days, but what is all the fuss about? Start your Cisco Catalyst SD-WAN journey here and learn about the platform architecture, the different components of the solution, and how they interact with each other and secure the user to application traffic. The session will be a great place to start for your SD-WAN journey and give you the right foundation before joining the many other great feature-specific SD-WAN sessions at Cisco Live.

### Cisco SDWAN Use Cases & Best Practices - BRKSEC-2708
Speakers: Jeff Fanelli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098377945001df6q
In this session, we will explore Cisco's robust secure SDWAN capabilities in the Catalyst, Meraki MX and Secure Firewall branch platforms. The most common deployment use cases of each will be covered, in an effort to guide customers to the perfect capabilities match for their environment.

### Cisco Secure Access Unveiled - BRKSEC-1586
Speakers: Anders Piilmann (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098363530001duh6
Learn about Cisco Secure Access, the latest Cisco Security SSE innovation which launched just a few months ago. We will talk about SSE in general and dig into the Cisco Secure Access Platform. In this session, you will learn about the Architecture of Secure Access and various different deployment use cases, such as securing your mobile workforce and branches. We will also cover how easily you can adopt Cisco Secure Access into your existing SD-WAN and integrate your mobile workforce into a Zero Trust architecture. We will also be discussing the new Resource Connectors which are able to provide Access to private applications and we will take a look at Digital Experience Monitoring which gives you end to end visibility and improved end user usability and experience.

### Cisco Secure Firewall Platforms Deep Dive - BRKSEC-2239
Speakers: Lukasz Bromirski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098371829001d6BY
This intermediate session will provide a deep dive into Secure Firewall security platforms and the associated application use cases. We'll go through overview of Secure Firewall 1/2/3/4/9k hardware and 7.7 software release news, as well as various aspects of the security application framework. The session will also address'specific popular topics in design with NGFW like:'single-flow, EVE, QUIC and TLS inspection implications on FTD throughput, inter-chassis clustering, multi-tenancy with Multi-and VRFs. At the end of the session, we'll also cover common internet edge scenarios with BGP. Working knowledge of FTD knowledge is required.

### Cisco Security Cloud Control (SCC) Platform to simplify Day-2 Operations with APIs, Event Notification and Integration - DEVNET-1375
Speakers: Vijayanand C D (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098432361001dnZJ
Cisco Security Cloud Control (SCC) is a cloud-based multi-device manager that facilitates management of security policies in highly distributed environments. In this session, we will focus on a step-by-step process on how to integrate in-built event notification to Webex using webhooks and how to automate work-flow for Firewall management using RESTful new SCC APIs.

### Cisco Silicon for AI: Capabilities, Designs and Results - BRKARC-2095
Speakers: Dave Zacks (Cisco), Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161400461001NugF
We all know that AI is changing the world. But have you ever wondered how you can build networks that support AI/ML workloads and how Cisco designs and builds the platforms to support your AI efforts? If so, this is the session for you. Attendees at this session will learn how Cisco platforms are being architected to support and optimize AI/ML workloads, the benefits these capabilities provide, and most importantly, how you can leverage these sets of functionality in your own network designs and implementations. Presenting this session is the dynamic duo of Peter Jones, Distinguished Engineer and Cisco Live Distinguished Speaker, and Dave Zacks, Distinguished Engineer and Cisco Live Distinguished Speaker Hall of Fame Elite member. Come to this exciting, in-depth, and fun session to see the latest in Cisco silicon and platform innovations to support AI.

### Cisco Software-Defined Access LISP Solution Fundamentals - BRKENS-2810
Speakers: Kedar Karmarkar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098301313001d6gN
Cisco SD-Access LISP is an evolution from traditional campus LAN to networks that directly implement the intent of an organization through a zero-trust architectural framework. SD-Access LISP intent-based automation seamlessly scales from one to tens of thousands of wired and wireless networking devices, reliably connecting and securing businesses of all sizes around the world. This presentation will be a technical introduction to SD-Access LISP, exploring and explaining the high-level concepts and components that underpin the solution.

### Cisco Video Devices for Microsoft Teams - Zero to Fully Deployed made easy! (Live demo!) - BRKCOL-2185
Speakers: Charlie Thorpe (Cisco), Davide Preti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098282662001dIc4
This intermediate-level session will guide attendees through the deployment of a Cisco Video Device enabled with the Microsoft Teams experience. We will cover the pre-configuration steps, supported capabilities and the End User experience. The following topics, amongst others, will be covered: - Office 365 Admin center - Exchange Online - Teams Admin center - Intune - Webex Control Hub - Workspaces - Devices - Analytics We will show the entire process from the stage, with live demos for onboarding of devices.

### Cisco Video Endpoints Update - BRKCOL-2390
Speakers: Charlie Thorpe (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098283747001d5uT
In this session, we'll explore the latest updates to the Cisco collaboration portfolio, with a focus on Cisco video devices, RoomOS, and Microsoft Teams Rooms. We'll also delve into Cinematic experiences and take a closer look at the newly released Ceiling Microphone Pro. For a comprehensive understanding of Microsoft Teams Rooms on Cisco video devices, attending session BRKCOL-2185 is highly recommended.

### Cisco Wireless Supercharged by Catalyst Center: The Ultimate Guide - BRKEWN-2667
Speakers: Stefan Honeder (Cisco), Ignacio Fite Lopez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161404715001NWUP
If Cisco Catalyst Center is the platform of choice for your wireless operation, and you aim to use it to its full potential, then this is a session for you. We will cover a selection of AIOps, NetOps, and DevOps capabilities offered by Cisco Catalyst Center up to release 2.3.7, in combination with IOS-XE 17.12/17.15 on Cisco Catalyst 9800 Controllers. This allows you to put everything you learn in this session into practice immediately. We will share all the learnings and best practices collected throughout the years so that you have a shortcut to supercharge your Cisco Wireless with Catalyst Center and be successful. Some remarks, We plan to deliver also content on Wifi7/6GHz T-shooting and Assurance the level of detail will depend on the product availability at the time of Cisco Live Things we plan to show in the NetOps section this year are AP Auto Locate, AP refresh workflow for Assurance only customers

### Cisco XDR - Making Sense of all the Parts and Pieces - BRKSEC-2113
Speakers: Oxana Sannikova (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098367120001dJQm
Cisco made a lot of noise at the 2023 RSA Conference announcing the new Cisco XDR. But what is it? What is eXtended Detection and Response (XDR)? Join us for a session where we delve into how Extended Detection and Response (XDR) can transform your security operations and drive impactful business outcomes. We will help answer the following questions and much more! What should an XDR be? Is Cisco XDR a SIEM or a SOAR? Is it something else? Is Cisco XDR just an evolution to Cisco SecureX, or is it different? How does it work, and what is happening behind the scenes? How does Cisco XDR make my Security Response more efficient & effective? What components are critical to make an XDR an effective tool? In this session, you will get a full walkthrough of Cisco XDR feature set, and latest innovations with concrete use cases and demos that will allow you to accelerate your SOC.

### Cisco's Reimagined Workspaces: Recipes for Success - PSOCOL-1789
Speakers: Mark Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098465977001dJCv
When people returned to the office was it the experience they expected? Are your workspaces adequately addressing the challenges of hybrid work? Cisco has been rethinking its approach to workspace design. Join this session to hear how Cisco IT, HR, and Corporate Real Estate Teams worked in lockstep to: Create a shared vision for workspaces of the future Understand the different purposes that Cisco properties fulfil Transform flagship sites in New York, Chicago, Atlanta, Paris, Milan, and London Save real-estate costs, increase occupancy levels, and reduce carbon footprint Embrace collaboration-centric workspaces, and unassigned seating plans Leverage rich workspace analytics to continually improve the employee experience and well-being You'll hear how Cisco smart buildings solutions with PoE network infrastructure, Cisco Collaboration devices, and suite of cloud management tools facilitate future-ready workspaces. Plus discover resources that we've created that enable you to learn from Cisco's experience and apply standardized workspace templates that can accelerate your own workspace transformation.

### Cleared for Take-Off - Network Assurance in a Modern Airport Network - PARENT-1447
Speakers: Riccardo Guglielmi (IP Fabric), Kristine Botha (IP Fabric), Mirko Gradillo (AEROPORTI DI ROMA SPA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098463350001dKUW
Join IP Fabric and Aeroporti di Roma as they discuss the collaboration that helped tackle long-standing operational challenges with a complex multi-vendor network. AdR have all but removed their manual documentation burden and massively reduced time required for compliance audits using IP Fabric's Network Assurance technology, and so could you!

### Closing the Loop: Automated Discovery and Assurance for Cisco Networks with NetBox - CISCOU-2050
Speakers: Rich Bibby (NetBox Labs)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098412522001dZ6m
Explore the power of automation with NetBox in this engaging Cisco U. Theater session. We'll demonstrate how to use NetBox as your single Source of Truth for your Cisco devices for streamlined network automation. Dive into a discovery and assurance workflow showcasing a foundational reference architecture, where NetBox Discovery automates device discovery and provides real-time insights, while driving automated response actions to address network drift. This session offers practical insights and hands-on techniques to help you implement modern automation workflows in Cisco environments, enhancing both efficiency and reliability.

### Cloud Management of Cisco Secure Firewall - BRKSEC-2166
Speakers: Ted Bedwell (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098369333001dALP
Cloud delivered management of secure firewall increases reliability, scalability, and capability. Join Ted Bedwell in this exploration of the inner workings of this unique solution, new innovations, and how it differs from the traditional Firewall Management Center.

### Cloud Native Security - The Challenges and The Opportunities - BRKETI-2491
Speakers: Tim Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098315901001d2U6
Over 85% of organizations have embraced cloud-first principles and are leveraging cloud-native architectures in their cloud adoption strategies. Businesses are still struggling to secure these complex environments as a result of a perfect storm of industry trends: ever increasing cloud services and configuration options, new attack vectors and exploding attack surface, and global shortage of cybersecurity professionals. With threat actors adopting AI to speed their time to breach, enterprises need a broad range of capabilities and techniques to help secure their applications. In this session, attendees will learn about the challenges facing cloud native application security and see live demonstrations of how you can bring together multiple areas of security (software supply chain, cloud security posture management, cloud workload protection, etc.) to give you comprehensive visibility of your cloud environments and their security posture, rapidly prioritize risks that an attacker would leverage to breach your environment, and how we can leverage Generative AI (GenAI) to enhance our provide targeted remediations as well as enhance our user experience. Attendees will also see how the Cisco Security portfolio works together to further enhance your cloud security posture.

### Cloud Security APIs and Splunk: Best Practices In Practice - DEVNET-2125
Speakers: Yaron Caspy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098438184001dUlQ
The Cloud Security App for Splunk utilizes a number of Cloud Security APIs (Umbrella, Investigate and Cloudlock APIs). Our design focused on using our public facing APIs for a number of use cases our customers need. During this session, we are not only going to walk you through how the different modules answer SOC, (Security Operations Center), and Threat Hunter needs, but also take you under the hood to see which APIs we use, why we chose them and what the implementation looks like.

### Cloud-Managed Data Center Networking Made Easy: Introducing Cisco Nexus Hyperfabric - PSODCN-1869
Speakers: Russell Rice (Cisco), Jake Katz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098467422001dVVA
Join us to discover the future of data center networking and AI. Cisco Nexus Hyperfabric is a revolutionary cloud-managed data center networking solution that empowers you to effortlessly design, deploy, and manage any number of fabrics across diverse locations, including primary data centers, colocation facilities, and distributed edge sites. This innovative solution streamlines the IT operations lifecycle, ensuring repeatable and predictable outcomes for IT generalists, application teams, and DevOps engineers. We'll explore the purpose-built hardware, software, cloud management, automation, and Cisco support. In addition, we will show how Cisco Nexus Hyperfabric AI, enables you to seamlessly transform your data centers to support demanding AI workloads. By simplifying the AI journey through a cloud-managed, on-premises solution, you can accelerate the design and deployment of high-performance AI clusters.

### Cloud-Managed Networking: Insights and Perspectives from a Catalyst Center SE - BRKOPS-2488
Speakers: Felix Meixner (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098353063001dOsQ
In the quest for agility, scalability, and enhanced security, cloud-managed networking is increasingly becoming a cornerstone for modern enterprises - at least, this is what cloud-managed network vendors tell us these days. But what does this shift mean for you, if you are currently utilising on-premises network management platforms? Why should these touted benefits apply to your network, and what unexpected challenges or advantages might you encounter? How will a transition to cloud management impact your daily operational tasks? Which approach fits your organization better: an incremental move to cloud management or transitioning all at once? Join this session and get familiar with these questions through real-world examples. The session will cover key topics such as onboarding, monitoring and management options for Catalyst wireless and Catalyst switching platforms powered by Cisco IOS-XE. Can cloud management truly revolutionize business connectivity with next-generation Cloud-Native architecture on Catalyst platforms, or is it more prudent to stick with the tried-and-true Catalyst Center? Or could it even be a good approach to leverage the strengths of both platforms in coexistence? Whether you are an experienced but cloud-sceptic network architect or a cloud-enthusiast networking engineer trying to grasp why proven on-premises technology continues to remain relevant, attending this session will provide you with a deeper understanding and fresh perspectives. It will help you understand and evaluate which operational model aligns best with your organization's goals and needs.

### Co-locating Local Gateway and Site Survivability for Webex Calling - BRKCOL-2312
Speakers: Hussain Ali (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098283386001d9Et
The same CUBE Enterprise platform can now be used as a Local Gateway (LGW) and Survivability Gateway (SGW) for Webex Calling. This session will begin with a recap of Webex Calling registration-based LGW/Trunking including the newly introduced multitenancy options for the partner-hosted Local Gateway. This will be followed by a technical deep dive into certificate-based trunks using CUBE as a LGW. Subsequently, we will introduce site survivability for Webex Calling using an SGW and review configurations required to co-locate the LGW with the SGW. BRKCOL-2314 would be a pre-requisite for this session.

### Collab AI: A Practical Use Case of Toll Fraud Prevention on Expressway using Machine Learning - BRKCOL-2116
Speakers: Luca Pellegrini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098281749001dohN
Since early 2000, several companies have opened their collaboration boundaries by allowing calls through the Internet. Consequently toll fraud has now evolved, and bots try to exploit the company's Internet access to reach the PSTN, placing calls to auto-answer toll numbers. Identifying these calls before they get connected is crucial to mitigate toll fraud. This session focuses on a machine-learning approach to identify and block toll fraud and spam calls on Expressway following these steps: identifying non-legitimate calls through CDR analysis choose a machine-learning prediction model train and test the model. Calculate the accuracy towards stability: addressing multicollinearity and overfitting towards stability: perform cross validation finalise and refine the model

### Complete Provisioning of Cisco Switches using Cisco Catalyst Center Templates - BRKOPS-2566
Speakers: Jaromir Pilar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098354865001dK5f
Automation of device configurations and checking configuration compliance, is one of the key tasks which has high priority for many customers. Cisco Catalyst Center offers multiple options to solve this task, like automation, using predefined workflows for certain solutions like SD Access or using APIs for "network-as-a-code" type of provisioning. One of the most common and most flexible options is using CLI templates. In combination with plug-and-play functionality, it allows users to configure devices from unpacking it from the box, to full participation in the network with desired configuration, without touching the device console, and without a terminal session to the device. In this session, participants will learn how to onboard a device into a network via plug-and-play process, providing basic configuration via an onboarding template ,and how to provide full configuration via "workflow like" composite template configuring VLANs, interfaces, 802.1x authentication, Cisco TrustSec and many more functions. Examples of templates in Apache Velocity Language will be shown including cycles, conditions, methods to work with data objects, template variables, links to Catalyst Center inventory etc. At the end of the session, a recorded demo of the entire process will be shown.

### Comprehensive AI Model Deployment Strategies - DEVNET-2905
Speakers: Nikhil Ghodki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098449003001diUD
This theater delves into a spectrum of model deployment methods tailored for different use cases, including single model, multi-model, and multi-modal environments. Participants will gain in-depth knowledge of different deployment strategies such as using Amazon EC2 instances for initial proof of concepts, Amazon EKS for scalable Kubernetes-based deployments, and Lorax for advanced multi-LoRA(Low Ranking Adapter) adapter configurations. Additionally, the theater will explore "Inference Components" with both single and multiple models, providing a holistic view of deployment options. By the end of this session, attendees will gain practical insights and hands-on experience in selecting and implementing the most efficient and effective deployment strategy for their specific needs, ensuring optimal performance and resource utilization. This theater is ideal for data scientists, ML engineers, and IT professionals seeking to enhance their deployment skills and streamline their AI workflows.

### Config Changes without Breaking the Network? Yes Please! - PSOENT-1863
Speakers: Reid Butler (Cisco), Kamden Schewitz (Cisco), Daniel Finein (Red River Technology LLC)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098469061001dAq0
Cisco is bringing powerful capabilities to your network to help streamline operations, whether you're on-premises, in the cloud or somewhere in between. In this session, we cover innovations across campus and branch networking that allow you to work seamlessly across management platforms including Meraki, Catalyst Center, Catalyst SD-WAN, and more. Join us to learn how Cisco Workflows is powering network automation across domains so that you can make the most out of your investment with Cisco. See how Cisco Workflows allows users of varying skill levels to seamlessly apply changes across any combination of Cisco and third-party applications.

### Configure IOS XE Using Automation - DEVSKL-1111
Speakers: Ashil Parekh (Cisco), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098451065001dT7N
This session will cover automating the process to configure for model driven telemetry (MDT), interface configuration and adding a crypto key to a device using Terraform. These demos will be using the DevNet sandboxes and can be replicated after the session. This session is paired with SKILLS-1110 immediately before this session. It is recommended that you register for both session, but this is not required. Please note that there will be a 15 minute break between sessions. If you do not attend the first session, you are not guaranteed a seat in this session as seating is first come first served regardless of previous registration.

### Configure IOS XE Using the CLI - DEVSKL-1110
Speakers: Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098450847001dwi0
This session will cover manual CLI configuration for model driven telemetry (MDT), interface configuration and adding a crypto key to a device. This session is paired with SKILLS-1111 immediately following. It is recommended that you register for both sessions, but this is not required. Please note that there will be a 15 minute break between sessions. If you attend the first session (and stay seated for the break), you may keep your seat for the second session.

### Connect, Secure, Assure: Designing a Future-Proofed Workplace - KDDENT-1000
Speakers: Lawrence Huang (Cisco), Simeon Solarsky (SAMSØE SAMSØE), Vikas Butaney (Cisco Systems, Inc), Joe Vaccaro (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227082587001Ju4R
As the landscape of work continues to evolve, organizations are transforming workspaces to seamlessly integrate physical and digital environments. Workplace experiences are more connected, more complex and more distributed than ever before, increasing risk across both the network and security landscape. The network and generative AI are foundational to mitigating this risk. Discover how Cisco's AI-driven networking innovations such as Wi-Fi 7, advanced zero trust security, and comprehensive assurance can help you design future-proofed workplaces and deliver resilient, secure and exceptional digital experiences.

### Connecting Cisco SD-Access LISP to the World: Use Cases and Segmentation - BRKENS-2811
Speakers: Devi Bellamkonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098301492001drk1
Prepare to embark on a thrilling journey into the dynamic realm of Cisco Software-Defined Access (SD-Access). Experience the revolution Cisco SD-Access has brought to the deployment of wired and wireless campus networks, utilizing the potent automation and orchestration features of Cisco Catalyst Center (formerly Cisco DNA Center). Adopting Cisco SD-Access simplifies the creation of your campus network like never before. Imagine transforming your campus network into a secure and adaptable hub, where connections to the external world are as effortless as a finger snap. During this session, we will unveil powerful features designed to tackle common challenges encountered when connecting a Cisco SD-Access network to external networks, including the internet, shared services, Data Center. Our objective is to provide comprehensive network segmentation and maintain consistent policy management across the entire network infrastructure. Please keep in mind that this session assumes some prior knowledge of the solution, including fabric roles and terminology. If you need a refresher, we recommend referring to the previously recorded BRKCRS-2810 available in the Cisco Live On-Demand Library. Don't miss out on this exciting opportunity to enhance your networking prowess.

### Connecting Remote and Critical Assets with Cisco IoT Solutions - BRKIOT-1126
Speakers: Emmanuel Tychon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161407361001NGjo
More than ever the current trend is to connect remote assets such as green energy production sites, mines, sentitive locations under monitoring to the network, providing connectivity and opening new possibilities. We will cover some possible options to connect assets that are isolated in the open world. Cisco IoT Industrial routers and cellular connectivity in 4G or 5G including the unique challenge with device management, as they are posing a number of challenges to traditional management platforms. Be prepared to discover a whole new spectrum of possibilities to connect the unconnected.

### Connecting Your Data to LLMs: Identity, Functions and Agents are all you Need - BRKETI-2411
Speakers: Marcelo Yannuzzi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098315547001dOiX
To truly exploit the benefits of Generative AI, most organizations need to connect their data to LLMs, but the challenges immediately start to pile up. Indeed, most organizations would like to use the data in their current systems just as they are today, without going through data adaptations and cumbersome migrations. Moreover, many organizations need to bring Generative AI to their data (e.g., residing on prem or on their own datacenters) instead of moving the data to models hosted in public clouds. In this session, you will learn about new architectures and tools enabling to connect your data to LLMs under your control. You will learn new techniques to inspect user prompts in real time and automatically: Identify and confirm the data required to complete the request carried in a prompt Determine whether the user has rightful access to such data Serve 'the right' data Finally, you will learn about Cisco's innovations in this space and the tools available for connecting your data to LLMs.

### Connecting and Securing Renewable Energy - Enabling Green Technologies with Cisco IoT - BRKIOT-1203
Speakers: Marcus Smith (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098328398001d4mi
Renewable energy is key to enabling a green future and hitting many countries commitments to move away from fossil fuels. Learn how Cisco's IoT technologies are connecting and securing diverse renewable energy assets such as Offshore Wind farms and Solar installations to Grid scale battery storage. This session will present the relevant solutions and products enabling the secure and highly available networks that are required to integrate Renewable Energy assets into the modern day grid with automation and security a key requirement.

### Considerations on Data Center Sustainability - BRKDCN-2625
Speakers: Fausto Vaninetti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098290730001dWcy
The impact of carbon emissions, and the need to be more conscious of the effects of IT operations and solutions in the context of environmental goals, is rapidly becoming a key topic. In this session, we will introduce the topic with some non-obvious concepts and facts and give an overview of elements within Cisco UCS X-Series, Intersight, and cloud networking offerings that can help advance organizations towards achieving these goals. As more data and processing needs exist, and are growing rapidly everywhere from the cloud to edge, providers and customers are exploring methods to reduce the impact on the environment from all operations, including the key area of IT.

### Container Orchestration using Kubernetes - CISCOU-2041
Speakers: Mohit Hooda (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098409327001dD6f
In this session, attendees will learn the fundamentals of Kubernetes, the leading platform for automating the deployment, scaling, and management of containerized applications. The session will cover key Kubernetes components such as Pods, Deployments, and Services, along with its architecture and operational concepts. Attendees will learn how Kubernetes simplifies the orchestration of containerized workloads, ensuring high availability and scalability across distributed systems. By the end of this session, attendees will be equipped with the knowledge to effectively use Kubernetes in their network automation workflows, enabling more efficient and resilient infrastructure management.

### Converge IT and OT Networks with Cisco Catalyst Center: In-Depth look into Industrial Networks - BRKIOT-2362
Speakers: P Surya Prakash Rao (Cisco), Krishna S Diwakar (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098330556001dC9A
Application of Cisco Catalyst Center expands beyond the boundary of Enterprise Network. Catalyst Center can provide a curated view for Industrial IOT with set of functions to perform key network management tasks, consistently and scalably. By harnessing the power of Catalyst Center, Industrial Enterprises can achieve better convergence with the IT Network, automate operations, streamline processes, and meet the challenges of the Industry 4.0 era with greater efficiency and reliability. Join our session to understand the best practices for onboarding, automating and securing your Industrial Network with simplified Day-0 and Day-N Automation Workflows, also learn Network monitoring and analytics for proactive identification and remediation of Industrial Network events using Catalyst Center.

### Create Future-Ready Workspaces with Cisco Workspace Designer - PSOCOL-1788
Speakers: Gyorgy Gyarmati (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098465797001deJY
AI is unlocking human potential by improving employee experiences, enhancing collaboration and raising productivity. But are your workspaces ready to capitalize on this potential? Join this session to discover how Cisco Workspace Designer is helping organizations to: Simplify and accelerate workplace transformation with standardized room templates that can be customized for your needs Create spaces that leverage AI-powered camera and audio-intelligence that enables immersive, equitable, and secure collaboration Deliver consistent user experiences in any workspace, on any platform Webex, Microsoft Teams, Google, and Zoom Provide IT, HR, and Corporate Real Estate with blueprints featuring equipment lists, installation guides, and room coverage charts We'll demo the new Cisco Workspace Designer, featuring the latest Cisco collaboration devices such as the Ceiling Microphone Pro, and cinematic meeting experiences with Cross-View. Plus, hear about smart buildings integrations for room booking and hotdesking with Cisco Spaces.

### Cross Architecture Approach to AI - AIHUB-1009
Speakers: John Cuneo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161391449001N7gH
Interest in AI has exploded in the past year, thanks in part to the popularity of ChatGPT and subsequent GPT implementations. Organizations across all verticals are evaluating and building strategy around how AI driven technologies can transform business processes and customer engagement. With this, teams are facing new challenges and considerations to deliver architectures that meet the demand and scale of these solutions. This speaker led session will cover an overview on how to approach and design a scalable architecture for AI workloads. The session will cover how Cisco's platform approach can handle density and scale of training models, with the simplicity and management to deploy inferencing at scale. Attendees will leave with a roadmap to explore the power of AI while maintaining the controls and sovereignty over their data.

### Cross-Architecture Integrations : Unlock End-to-End Segmentation - DEVSKL-2450
Speakers: Marion Vailler (Cisco Systems, Inc.), Xavier VALETTE (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098452159001d06X
Did you know that by 2026, 60% of enterprises working toward zero trust architecture will use more than one deployment form of microsegmentation? Join us for a transformative session where we reveal how Cisco can help streamline your microsegmentation. Learn how ISE can seamlessly bridge your Campus, your SD-WAN, your SSE and your Cloud security policies together. In this session, we will explore real customer use cases through key integrations that enhance network efficiency and security. Ideal for NetOps, DevOps, SecOps, this session will demonstrate the power of automation in transforming your network and security operations.

### Crosswork Planning using Predictive Analytics to power AI OPS - BRKOPS-1643
Speakers: Bruno Vermeiren (Cisco Systems, Inc.), Fung Lim (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098347274001diwz
Crosswork Planning was recently introduced to the market. This next generation microservices-based architecture, with modern GUI, is the successor to WAE, the World's leading network planning tool. Join us to hear how you can use this predictive analytics operation tool for proactively managing the capacity of your IP core network. This session will start at the basics and cover among other topics: Modeling - Network Model construction and validation Visibility - Visualize your network and traffic in a single pane of glass De-risking - Automate worse-case failure analysis of the entire network Capacity Planning - Plan for the future and minimize spend Optimization - optimal metrics, optimal Segment Routing paths This will be a combination of slides (argh! kept to a minimum) and live demos (much more fun!) Attendees will walk away knowing that Crosswork Planning has been built by network Engineers for Network Engineers. Look forward to welcoming you to the future of network planning.

### Customer Case Studies: Lessons Learned from the Cisco SD-WAN Design Council - BRKENT-2660
Speakers: Tom Kunath (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098310495001dNtJ
In this session, we discuss lessons learned from different non-typical SD-WAN designs submitted to the Cisco design council. These will be presented as anonymized case studies, highlighting the diverse set of Catalyst SD-WAN connectivity and security features that our customers have deployed to meet their unique business needs. Example designs and best practices will be provided for multiple industries, such as retail, financial services, healthcare, energy, and transportation.

### Customer Experience (CX) Global Customer Experience Partner of the Year for 2024 - PARCX-1618
Speakers: Kyle Killebrew (INSIGHT), Steve Jarrett Reeves (INSIGHT NETWORKING SOLUTIONS LIMITED)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098462059001d74P
Join us to celebrate Insight's global recognition as the Customer Experience (CX) Global Customer Experience Partner of the Year for 2024 by Cisco. Explore Insight's journey to excellence in customer service, innovation, and technical expertise, setting new standards and driving success worldwide. Gain insights into the strategies and collaborative efforts that have earned Insight this prestigious award and positioned the company as a leader in customer experience excellence.

### Cut the Cord: Design Principles to Deliver a Wireless-First Enterprise - BRKEWN-2107
Speakers: Leigh Jewell (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098319258001dOEb
Cut the cord and learn how to design a reliable wireless-first deployment. If you have been deploying legacy Ethernet networks for decades but are unsure how to bring the same reliability to your wireless, this session is for you. This session aims to provide you with the tips and tricks you need to ensure that your wireless network can meet the demands of the most important method for which your clients will connect to your enterprise network. It doesn't matter if you use Meraki or Catalyst, this session will cover both on-premises and cloud-managed deployment architectures.

### Cybersecurity Chess: AI vs. AI in Network Defense - DEVNET-2415
Speakers: Edwin Muriyaden Wilson (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098443562001daZF
In the ever-evolving cybersecurity landscape, AI is emerging as both a powerful defender and a formidable adversary. This session explores how to harness AI for advanced threat detection and automated response using Cisco's integrated security platforms. Through live demonstrations, we'll showcase AI-powered attack simulations and defense mechanisms at Layer 2 and Layer 3 - critical yet often overlooked areas of network security - using Cisco XDR, Umbrella, ISE, and DNA Center. You'll witness the dynamic interplay between offensive and defensive AI, revealing how to safeguard your network against cutting-edge threats such as MAC flooding, ARP spoofing, DNS tunneling, and BGP manipulation. By the end of this session, you'll gain actionable insights to: Implement AI-driven threat detection strategies with Cisco XDR Develop automated, AI-enhanced response workflows by integrating XDR with ISE and DNA Center to mitigate Layer 2/3 risks Deploy comprehensive Layer 2/3 security strategies using Cisco's robust security portfolio This session underscores the importance of securing your network's foundational layers while leveraging AI-driven automation to stay ahead of evolving threats. Join us'to experience the future of cybersecurity and learn how Cisco's innovative tools can help you build a resilient, AI-powered defense strategy.

### DORA, Resilience, and the Role of Observability - BRKOBS-2070
Speakers: William Cappelli (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098341928001daAl
DORA and similar regulatory frameworks being put in place around the world place central emphasis on the ability of financial services to respond rapidly to what is beileved to be an inevitable stream of disruptive events - whether those events are the result of technical breakdowns and errors or the consequence of intentional malicious interventions. Observability and AI working together have a key role in enabling the level of resilience now being demanded by the authorities and this presentation will explore the exact nature of their contribution. The speaker will discuss: Why is AI-enhanced Observability central to DORA and similar frameworks ? How do the demands made by DORA impact the architecture of Observability deployments ? What cultural changes are required to make an enterprise 'resilience-conscious.' ?

### Data Center Network Design for the Media and Entertainment Industry - BRKDCN-2924
Speakers: Chris Lapp (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098293865001dXGX
The media broadcasting and entertainment industry is going through a massive transition as it moves from legacy SDI to IP networks for live production. The network built to carry this workflow must offer reliable transport of video and audio streams along with distribution of timing using precision time protocol. This session will help educate network admins on how to build the network by leveraging Cisco's non-blocking multicast and will introduce the Cisco IP fabric for media. The session will also go beyond production and cover network design for other use cases such as playout, contribution, and other file-based workflows which are relevant to the media industry.

### Data Center Networking Enabled by Cisco Green Pay: a Win/Win Circularity Story - IF-1818
Speakers: Kasper Skriver (Cisco Systems, Inc.), Koen Claeys (DLL), Tim Martin (DLL)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098456451001dhr6
De Lage Landen (DLL) has demonstrated a steadfast commitment to environmental stewardship by embedding sustainability into the very fabric of their business strategy. Through innovative approaches and tangible actions, DLL has partnered with Cisco to drive a transformative shift toward circular IT solutions, reducing electronic waste and enhancing sustainable practices in the technology leasing sector. This session will spotlight a landmark $1.1 million Data Center networking acquisition for DLL, facilitated by Cisco Green Pay. This acquisition marks a pivotal step in DLL's strategy to embrace circular IT, setting a precedent for future sustainable endeavors. Join us to explore how strategic partnerships can catalyze meaningful change in advancing sustainability goals.

### Data Center Operations Maintenance and Migration Best Practices - BRKDCN-2958
Speakers: Anis Edavalath (Cisco), Arvind Durai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098295485001dL66
This session will cover the best practices and solutions that help plan the change window and migrations with minimal disruption to the existing production environment. Attendees will understand the solutions to deal with planned and unplanned outages in ACI, VXLAN, and traditional VPC environments. The session will also cover the capabilities and features of the Nexus platform that assist in isolation strategies, image management, performance monitoring, and hardware migrations. Attendees will also be introduced to migration strategies for modernization, scaling, and lifecycle management.

### Day 0 to Day N with Meraki Automation - DEVSKL-1221
Speakers: John Kuchta (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098451430001dXjS
Learn how APIs can be used to confidently and repeatedly deploy multiple sites and related network and security configurations. In addition, examine how action batches can be used to consolidate API calls across several deployments, and how web hooks can be used to support event driven monitoring. Finally, learn how APIs can be used to build consolidated dashboards for what your organization cares about. This session is paired with SKILLS-1220 immediately before this session. It is recommended that you register for both session, but this is not required. Please note that there will be a 15 minute break between sessions. If you do not attend the first session, you are not guaranteed a seat in this session as seating is first come first served regardless of previous registration.

### Day 0 to Day N with Meraki Dashboard - DEVSKL-1220
Speakers: Priya Ram (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098451247001dzoh
Create, configure and deploy a multisite SDWAN network that includes MX, Switching, APs, and Cameras/Edge devices. Learn the basics of organization and network creation and how to harden your networks through firewall and policy configuration. Once your networks are deployed, see how you can use the Dashboard to monitor your networks and Meraki Insights to optimize your deployments. This session is paired with SKILLS-1221 immediately following this session. It is recommended that you register for both sessions, but this is not required. Please note that there will be a 15 minute break between sessions. If you attend the first session (and stay seated for the break), you may keep your seat for the second session.

### Deep Dive into Cisco's Use of QUIC, MASQUE and OS Native Capabilities to Deliver Frictionless Zero Trust Access - BRKSEC-3027
Speakers: Vinny Parla (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098380884001dgEP
Zero Trust has not yet reached its full adoption potential in the market, largely due to the degree of friction for both end users and IT administrators. Cisco's design goal is to develop Zero Trust solutions that frustrate attackers, not users. The experience should be as seamless and easy-to-use as turning on a Wifi connection. In this Tech Talk, we explore technologies that can help us deliver on this frictionless vision in collaboration with ecosystem partners such as Apple, Google, and Samsung. This session will examine industry standard protocols such as MASQUE as well as other technologies like WebAuthN, passkeys, and private 5G access that will eventually make Frictionless Secure Access as ubiquitous as Wifi in the enterprise and home. The session will also provide for an overview of native OS clients from Apple & Samsung as well as the Cisco Zero Trust Access module built into Cisco Secure Client, and how they leverage industry standards such as MASQUE and QUIC to deliver a seamless Zero Trust Access user experience.

### Demystifying IP Multicast in SD-Access - BRKENS-2820
Speakers: Marcin Hamróz (Cisco Systems, Inc.), Luis Villatoro (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098301855001dYYA
For the past few years, multicast has gained wider acceptance and become one of the crucial elements of modern Enterprise Networks. This session will provide a concise coverage of multicast in the SD-Access fabric, from scalability to design considerations for a successful deployment. During this session, we will explore two multicast deployment models in SD-Access: head-end replication (forwarding in overlay) and native Multicast (forwarding in underlay). We will also discuss layer 2 flooding mechanisms which rely on multicast underneath. This session will also present many examples of common, and not-so-common, multicast networks problems in SD-Access and show what commands to use and how to solve them.

### Demystifying the Role of AI in Your Cisco Wireless Deployments - BRKEWN-3007
Speakers: Vishal Desai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161406228001NBxT
Whether your wireless network runs on simplified IT management through Meraki Cloud or leverages the richness of wireless features with on-premises Cisco Catalyst Center, your wireless network is only as good as your ability to optimize it. In today's world, filled with many AI/ML applications for essential and ubiquitous services like Wi-Fi, it only raises the question of how AI/ML can really help deliver stable and yet best-in-class experiences to meet capacity needs, and maintain SLAs for your 5GHz and 6E wireless clients. But models generated by AI/ML are only as good as your data lake! With the right data and the right approach, it can multiply tenfold the efficiency of your network operations, your management and troubleshooting, but if you don't know how to use it, it is just like a laser saber without a battery!! In this session, you will learn about under-the-hood details of powerful Applied AI-based applications available for both cloud-managed and on-premises Cisco wireless platforms. You will also learn Applied AI is enabling closed-loop optimizations that transform your wireless networks, maximizing client experiences, and making network operations more efficient by leveraging AIOps to automatically tune your wireless networks with tailor-made config recommendations based on the unique RF signatures, all of this done without compromising your privacy.

### Deploying Catalyst Center for IPv6 Networks - BRKIPV-1007
Speakers: P Surya Prakash Rao (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098333381001dZp7
Let us enlighten you with what Cisco Catalyst Center can do for an IPv6 Network. Learn how to deploy Catalyst Center with IPv6 and discover the capabilities it has for managing IPv6 Enterprise Network.

### Deploying Cisco Catalyst Center in Seconds with CICD - DEVNET-2176
Speakers: Keith Baldwin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098440346001d67p
This session expands your knowledge and delves into CICD and how pipelines may be leveraged with Cisco Catalyst Center (formerly Cisco DNA Center). We will discuss REST API and how to leverage templates and external data sources in conjunction CICD pipelines. Here we will demonstrate the use of a realistic set of predefined Rest-API collections, and templates and an external data source in a controlled environment for the following tasks, utilizing CICD pipelines: Build Hierarchy Assign Settings, Credentials and Telemetry Device Discovery Retrieving Network Inventory Template and Project Deployment This session builds your knowledge in utilizing Rest-API with CICD pipelines and Ansible for orchestration over Catalyst Center.

### Deploying IPv6 Routing Protocols: Specifics and Considerations - BRKIPV-2418
Speakers: Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098335153001d4ao
Even though all major IPv6 routing protocols are rooted in their well-known IPv4 counterparts, they all come with their own unique set of idiosyncrasies, and when faced with the task of deploying an IPv6 routing protocol along with its IPv4 variant, there are often multiple ways of doing it, but the best choice is not always obvious. The goal of this session is to discuss the specifics of IPv6 support in OSPFv3, IS-IS, EIGRP, and BGP in IOS XE. For each of these protocols, we will do a quick IPv6-focused refresher, and then focus on the protocol's unique IPv6 traits (and quirks). We will also look at how the protocol supports the co-existence of IPv4 and IPv6, and if there are multiple options to choose from, we will discuss the pros and cons of each of them. To benefit the most from this session, it is highly recommended to have a working knowledge of routing protocols in general.

### Deploying LEOsat Use Cases, Leveraging Cisco Technologies - BRKOPS-2071
Speakers: Kemal Sanjta (Cisco), Dave Zacks (Cisco), Ian Procyk (Cisco), Oliver Boehmer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098349856001dZx6
Low Earth Orbit satellite (LEOsat) systems such as Starlink, OneWeb, and others have revolutionized high-performance, reliable data connectivity to any point on the planet. Come to this fun, fast-paced and interactive session to delve into a wide variety of use cases for LEOsats, from IoT and remote sensing to resource extraction, emergency response, and more and explore how Cisco technologies make LEOsat deployments better, more responsive, and more secure. Delivering this session are the dynamic duo of Dave Zacks and Ian Procyk, both Cisco Live Distinguished Speakers as well as LEOsat users and enthusiasts. Come to this session for a fun, engaging, fast-paced exploration of LEOsats and Cisco technologies they can leverage!

### Deploying Nexus Dashboard in Your Organization - BRKDCN-2914
Speakers: Tim Kuik (Cisco Systems, Inc.), Matthias Wessendorf (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098293138001drLw
This technical breakout will provide an end-to-end view of deploying and operating the unified release of Cisco Nexus Dashboard, which provides unprecedented simplicity by integrating operational services to manage customers on-premises and in cloud and hybrid fabrics through a single dashboard. You'll learn that by using the Cisco Nexus Dashboard, IT operations teams can seamlessly navigate all aspects of infrastructure lifecycle tasks from initial configuration and capacity planning to running and troubleshooting the entire IT infrastructure. Understanding how an infrastructure is deployed for usage of new tools and methodologies in your organizations is one side, but effectively operating the infrastructure is the other side. This session will review some common tasks and activities for deploying and operating Cisco Nexus Dashboard for day-to-day operations.

### Deploying VPNs over Segment Routed Networks Made Easy - BRKMPL-2131
Speakers: Krishnan Thirukonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161409210001Nsai
With segment routing, a software-defined network (SDN) approach to program paths for transport services such as layer 3 and layer 2 VPN becomes possible, enabling new approaches for managing transport networks based on segment routing. In this session, a review of the requirements and capabilities for an SDN approach for transport networks is discussed. This is followed by a description of the Cisco solution for multivendor SDN controller for transport networks to deploy and manage VPN services over SR-TE using MPLS or SRv6, using the Cisco Crosswork Network Controller (CNC). The main use cases covered by CNC will be described and a walkthrough of UI- and API-based workflows to create VPNs, SR-TE policies, and bind layer 2/layer 3 VPNs to these policies will be shown. Additionally, advance capabilities to do tactical bandwidth management and monitor service health will be discussed. The goal of this session is to understand how to bring an SDN approach to managing transport networks and understanding the Cisco solution for it.

### Deploying Your First Cisco SD-Access Project - BRKENS-2824
Speakers: Sergey Nasonov (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098302034001dt45
So, you got your first SD-Access project and do not know where to start? This session will explore what it takes to plan, design, and implement a typical SD-Access project for an imaginary company. During this presentation, we will discuss the lessons learned from previous deployments, typical misunderstandings, and evaluate design options and the migration approach from traditional networking to fabric. The session is going to cover scope and effort estimates, risk management, external dependencies, build, and migration techniques. Wired and wireless migration considerations will be examined, as well as ISE and Cisco Catalyst Center roles and functions. This session is aimed for solution architects getting their hands dirty with SD-Access.

### Deploying an AI/ML Hybrid Cisco and Azure Infrastructure for Advanced AI Use Cases - BRKCLD-2944
Speakers: Jeff Teeter (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279201001d2Ej
In today's digital landscape, integrating AI and ML into enterprise operations is essential for staying competitive and driving innovation. This session explores deploying a hybrid Cisco and Azure infrastructure to support advanced AI/ML use cases, such as ChatGPT, sustainability initiatives, smart buildings, and public safety applications. Participants will gain insights into creating secure and scalable AI/ML environments leveraging Cisco and Azure technologies, as well as Splunk as an operational intelligence platform. This comprehensive session offers a deep dive into how hybrid AI infrastructure can address business challenges in sustainability, public safety, securely integrating ChatGPT with enterprise data using Retrieval-Augmented Generation (RAG), and various company workflows. Additionally, the session will cover the Cisco AI-Driven Secure Enterprise Data Architecture, which ensures robust data protection and operational efficiency. Participants will learn to harness these technologies to create impactful AI systems, enhancing organizational efficiency and resilience, and ensuring their organizations remain at the forefront of technological innovation.

### Deploying the Webex App to your Organization - BRKCOL-2198
Speakers: Shane Long (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098282848001d6lI
The Webex App unifies multiple collaboration workloads into a single modern user interface. This session will focus on deployment of the Webex App to your organization. We will focus on enabling calling, messaging and meetings workloads within the Webex App for your users. We will also provide in depth detail on the best practices for installing and updating the Webex App.

### Deployment of Micro-Segmentation in Cisco NX-OS VXLAN EVPN Fabrics with VXLAN Group Policy Option (GPO) - BRKDCN-2933
Speakers: Max Ardica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294232001dxed
In traditional data center environments, security enforcement for protecting applications/workloads is typically implemented using perimeter firewalls and other security inspection devices. However, this approach is not effective against the advanced nature of modern attacks, which have an attack surface that spans the entire data center, affecting both east-west and north-south traffic flows. This session introduces the use of micro-segmentation with security groups and security group ACLs in Cisco NX-OS VXLAN EVPN-based data center fabrics. This feature, also known as VXLAN Group Policy Option (GPO) (IETF draft: draft-smith-vxlan-group-policy-05), can provide application-specific policies to tightly control the communication of application workloads regardless of where they reside within the network. The first part of the session covers the functional component of the Cisco GPO implementation, both for a control and data plane perspective. The second part discusses the most common use cases for the deployment of this micro-segmentation option, including service chaining improvement and simplification.

### Deployment of VXLAN EVPN Gateways with Cisco ACI for the Interconnection of Heterogeneous Data Center Fabrics - BRKDCN-2634
Speakers: Takuya Kishida (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098291106001dxRP
In recent years, the use of the VXLAN EVPN technology has become the de-facto standard for the deployment of data center fabrics. Cisco leverages this technology for its two flavors of fabric (and multi-fabric) architectures: Cisco ACI and Cisco NX-OS VXLAN EVPN. As a consequence, customers are very often challenged with the requirement of interconnecting those heterogeneous fabrics, both for co-existence or migration purposes. This session introduces the use of a VXLAN EVPN gateway functionality in a Cisco ACI fabric to establish native Layer 2 and Layer 3 connectivity with standard-based VXLAN BGP EVPN fabrics. The session covers the functional components and the control and data plane mechanisms, required to implement the VXLAN EVPN gateway functionality in an ACI fabric. It will also discuss how to interconnect pre-existing (brownfield) heterogeneous fabrics, a functionality usually referred to as "namespace normalization" and how to provide end-to-end micro-segmentation support between ACI and VXLAN EVPN fabrics through the integration of VXLAN EVPN gateways with the VXLAN Group Policy Option (GPO) technology. This session is a companion of breakout BRKDCN-2933, and the expectation is that attendees already have at least a basic understanding of Cisco NX-OS VXLAN EVPN technology in order to get the best out of this session.

### Design and Deploy Cisco Network Detection and Response with Cisco Breach Suite - BRKSEC-2248
Speakers: Hanna Jabbour (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098372187001dzyN
Network Detection and Response (NDR) tools are critical components for any SOC or NOC and provide a great value for both users. Designing and deploying an NDR to provide complete visibility across hybrid network is key for successful and smooth day to day operation. This session will provide details on how to design and deploy Cisco NDR solution Network Analytics (NA) in a hybrid environment. You will learn all the components (new and old) and how they fit in your network to provide visibility into workloads on-prem and in the cloud as well as users and devices locally or remotely. The participants will learn how to integrate the different telemetry sources and their contribution into the analytics including Firewall, Network, endpoint and Cloud data. This session includes details on NA architecture as well as configuration and troubleshooting guidelines based on requirements and uses cases.

### Design and Deployment of Unified Communication Services in SD-WAN - BRKCOL-2078
Speakers: Arun Arunachalam (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098281374001dFlF
As you migrate multi-service Edge routers to SD-WAN solution, it is important to ensure that end users continue to have the same high quality, secure communication experience when collaborating with external organizations. This session provides an in-depth view of SD-WAN architecture and best practices on how to design and deploy Unified communications features in Edge devices. The Catalyst 8000 Edge platform will be deployed as a Cisco Unified Border Element (CUBE) to demonstrate configuration management using Cisco Catalyst SD-WAN Manager. The ThousandEyes platform integration with SD-WAN edge devices will be leveraged to accelerate troubleshooting process. The intended audience for this intermediate level session are UC network engineers and architects.

### Design your Enterprise Wireless Network with Cisco Meraki - BRKEWN-2035
Speakers: Simone Arena (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098317251001ddW0
Are you looking at cloud management for your enterprise wireless? Then this session is for you. We will explore the advantages of the Meraki cloud platform, introduce you to the new enterprise-class features available, and guide you on how to design and apply best practices to build your enterprise wireless campus with Meraki.

### Design, Deployment, and Management of Next-Generation Network Fabrics - BRKSPG-2227
Speakers: Phil Bedard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161415273001NIBH
In this session, we will explore the evolution of provider network designs over the last 30 years, and the state of the art deploying modern network fabrics. Network fabrics provide full mesh connectivity between endpoints with efficiency, scale, and advanced assurance capabilities. We will look at common applications and data sources connected to the network fabric and how best to design the network to support them as well as future applications. We will also cover best practices on deploying the networks and how best to manage and assure the network fabric infrastructure.

### Designing Highly Available Networks using Catalyst 9000 Series Switches - BRKENS-2095
Speakers: Minhaj Uddin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098300224001dDvW
This session will cover new and existing high-availability features introduced in IOS-XE on Catalyst 9000 Series switching platforms. We will discuss how you can achieve high availability in your network through various stages in the design lifecycle. During the initial design, we will discuss the benefits of features like StackPower, power resiliency modes, StackWise-480, and StackWise Virtual. After the design phase, we will discuss features like GIR, extended fast software upgrade (xFSU), patchability, and ISSU that will help maintain resiliency during the operational phase. We will then conclude by covering how you can efficiently leverage all the high-availability features in different network designs and achieve maximum uptime and resiliency.

### Designing Regular and Irregular Meeting Rooms - BRKCOL-1176
Speakers: Svein Terje Steffensen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098280163001d73w
Ever tried to set up a room with out of the ordinary requirements? This session will help you create the best experiences, both for regular and irregular meeting rooms, either in Microsoft Teams Room or RoomOS mode. Cisco is often approached with questions on how to design and set up specific types of rooms, be it a board room, a campfire layout, a divisible room, a training room or a court room. The common theme is they all have needs beyond a regular meeting room. This session will demystify Cinematic meetings and describe how to design to solve for various needs, both using the capabilities within the Cisco Room Devices, and when integrating with external equipment. It will also touch on physical accoustic considerations, lighting, camera and display placements. Finally we will touch on how AV over IP plays a role in setups like this, and what the best practices are around deployment of these technologies.

### Designing Routed Optical Networks: IP/MPLS Considerations - BRKSPG-2029
Speakers: Emerson Moura (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161413770001NO6n
Routed optical networking (RON) is a new IP/DWDM network architecture vision that greatly improves the economics and efficiency of networking as well as enables a new application paradigm. This session will specifically focus on the IP routing layer of RON and how this simpler, multi-service IP-centric architecture reduces operator costs while at the same time improves network asset utilization and resiliency, as well as enables optimization of the network for distributed applications, content, and internet peering. A comparison of a traditional IP/DWDM architecture vs. RON architecture will also be presented.

### Designing and Future-Proofing Energy Systems from the Data Center to the Campus - CENGRN-1000
Speakers: Denise Lee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227081152001JK5R
Cisco is at the forefront of shaping the future of energy, playing a critical role in innovating and transforming the energy landscape. We believe we must sustainably design and future-proof energy grids, buildings, networks, data centers and technology for whatever energy requirements are around the corner - whether that's AI or whatever comes next. Cisco understands the urgency of designing and future-proofing energy systems. As technology evolves, so too must our energy infrastructure, so that we can meet emerging demands efficiently and sustainably.

### Designing and Observing for Optimal Application Experience - BRKCLD-2310
Speakers: Stefano Gioia (Cisco), Tjerk Bijlsma (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098277860001dGsP
Experience the Cisco Observability solution in a live demo environment and understand how this solution, powered by Splunk AppDynamics and ThousandEyes, works to deliver experience assurance across applications, infrastructure, and networks. Using an application deployed across the hybrid cloud, we will show you how, leveraging the latest technology, you can deliver insights that will immediately benefit your users and customers.

### Detect and Prioritize App Security Vulnerabilities - BRKAPP-2005
Speakers: Luca Relandini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098273423001dC6E
IT and security teams are constantly challenged to prioritize initiatives that help accelerate the business while lowering risk. At the same time, they need to optimize application performance across both modern and traditional applications to provide a delightful customer experience. In this session, you will learn how to model overall business risk, encompassing security and application contexts across your traditional and modern applications. You will also learn how application security solutions from Splunk AppDynamics provide a ready-made business risk score to align your teams on the most critical security issues that need to be addressed to accelerate your business. AppDynamics business risk leverages the power of the Cisco security stack, including Kenna Security, Cisco Cloud Application Security (Panoptica), and Talos, to provide application security issues remediation guidance so your teams get to resolution in moments - not months.

### DevOps Tools Fight for Relevance! - DEVNET-1280
Speakers: Adrian Iliesiu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098431625001dkbE
Two of the most popular DevOps configuration management tools are Ansible and Terraform. If you're just getting started with configuration automation and are not sure which one would suit best your environment and use cases, then join me in exploring both of these tools. We'll have a look at their features, how to install and run them, and advantages and disadvantages for each of them. And we might just find out also which one would fare better in the struggle for survival.

### DevOps and Observability: Where Magic Happens, Thanks to Automation - BRKOBS-2284
Speakers: Luca Relandini (Cisco), Stefano Gioia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098342654001dHhy
Modern systems require an observability approach; traditional monitoring is no longer sufficient. OpenTelemetry grants an open and future-proof solution, and Splunk Observability is founded on it. You will see a live demo of automation (observability as code) and openness (hybrid applications, legacy, and cloud-native together). 'the session will show a CI/CD pipeline building simultaneously with the application and the observability framework so that every release is tested automatically and ready to run in production.

### Differentiating B2B Services and Transport with QoE and Proactive Service Assurance - BRKSPG-2643
Speakers: Ramesh Reddy (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098390242001df7m
No longer just a nice-to-have, service assurance is a foundational requirement of today's high-performance networks. Service providers will simply not deliver business value without consistent, accurate, and end-to-end performance visibility on service quality and the hidden "micro" issues that cause delays and impact network stability and user experience. In this session, we will discuss the evolution of service assurance and the use cases that are delivering ROI, including mobile transport, B2B services, end-customer portals, and proactive SLA compliance. Learn how proactive visibility and insights are helping service providers reduce costs and monetize new differentiated SLA-backed services that customers want.

### Digital Resilience in the Modern World - ITLGEN-1512
Speakers: Dipesh Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098459537001dNQi
As our users and applications continue to disperse across corporate enterprise boundaries, ensuring digital resilience of application availability and performance becomes an ever-daunting task. Here in Cisco IT, we have leveraged the power of observability by utilizing Thousand Eyes agents coupled with operational event driven data via Splunk, to help improve our position on Digital Resilience wherever our users or applications may be. We can now very quickly correlate and react to not only outages on owned infrastructure but also on connectivity and availability of infrastructure on the internet. Using this data, in some instances also start to predict issues before they become user impacting and ultimately provide this data to our end users to help them solve issues without ever opening a ticket!

### Digital Risk & Reward: Preparing for a World Where Resilience Matters - ITLGEN-1511
Speakers: Joe Vaccaro (Cisco), Jonas Fischer (OMV AG)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098459358001dt1M
Today's IT operations depend on a complex digital environment that spans owned and unowned networks, infrastructure, and applications. Any disruption to that environment could impact an organization's reputation, bottom line, and even regulatory compliance. Join us to hear what resilience looks like in a digital economy and how end-to-end visibility can not only prepare IT teams for digital regulation but also help them deliver on the promise of superior user experiences.

### Discovering and Managing Brownfield Deployment with Cisco Catalyst Center (formerly Cisco DNA Center) - BRKOPS-1461
Speakers: Sneha Amarapuram (Cisco), Ramkumar Chellappa (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098346556001dpFr
This session is dedicated to demonstrating the streamlined integration of brownfield deployments into Cisco Catalyst Center, with a strong emphasis on efficient management practices. It comprehensively addresses crucial aspects, including essential configurations within Cisco Catalyst Center, and delves into the intricacies of device configurations pushed by Cisco Catalyst Center to manage network devices. By the end of this session, attendees will acquire the knowledge and confidence needed to seamlessly navigate day-n operations within their brownfield deployment.

### Diverse Virtualization Deployment Strategies with Cisco UCS: VMware, Red Hat, Azure, Nutanix, and More - BRKCOM-2460
Speakers: Ulrich Kleidon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098287747001dmLY
In today's dynamic IT landscape, organizations require flexible and scalable deployment options to meet their diverse computing needs. The Cisco Unified Computing System (UCS) offers a multitude of deployment alternatives designed to optimize performance, simplify management, and accelerate business outcomesall without requiring infrastructure silos or unique operational models. Join us for an engaging session where we will delve into various deployment models, including: - VMware vSphere: Understand how to effectively deploy and manage VMware vSphere on Cisco UCS, leveraging best practices for virtualization efficiency and reliability. - Red Hat OpenShift Virtualization: Discover the benefits and strategies for deploying Red Hat OpenShift Virtualization, ensuring seamless integration and a natural extension to the cloud-native Red Hat OpenShift platform. - Bare Metal Deployments: Learn about the advantages and key considerations for deploying bare metal servers on Cisco UCS to achieve maximum performance and control. - Microsoft Azure Stack HCI: Gain insights into deploying Azure Stack on Cisco UCS, enabling hybrid cloud solutions that extend Azure services to your on-premises environment. - Cisco Compute for Hyperconverged with Nutanix: Explore how to streamline AI workloads and enhance performance with our integrated hyperconverged solutions. - And More We will share practical insights and best practices to help you select and implement the most suitable deployment models for your organization. This session will equip you with the knowledge and tools to leverage the full potential of Cisco UCS in optimizing your IT infrastructure.

### Do You Know Where Your Data Is? A Deep Dive on Cisco Secure Access CASB and DLP and How to Protect Your Locations, Data and Users - BRKSEC-2143
Speakers: Nitin Kumar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098367846001dWTM
Do you know where your data is? As cloud adoption is on the rise, so are bad actors preying on companies and users. This session will provide a technical overview of Cisco Secure Access' CASB and DLP offering which is a core part of Cisco's overall SASE strategy. Cloud Access Security Broker (CASB) provide the initial visibility to cloud app usage. Are your users only using business approved apps sanctioned by your company, or are they using unapproved apps to share and collaborate? This is what CASB is designed to find out. Umbrella also features DLP capabilities to monitor and enforce data for all web traffic. This is a core tenant of security and you'll learn how you can best protect your sensitive data from ever leaving the perimeter.

### Do you Use MS365 for Email? We can Make your Solution Safer! - BRKSEC-2263
Speakers: Sergio Pinto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098372547001dE1X
In today's digital landscape, securing your organization's email is more critical than ever. With the widespread adoption of Microsoft 365 for email services, businesses face evolving security challenges that require robust, proactive measures. This session delves into advanced strategies and tools to fortify your MS365 email environment against potential threats. We will discuss why you should deploy ETD, and what you can expect from it with a quick go-through of the integration process and examples of the additional detections ETD can do. By the end of this session, you will be equipped with practical knowledge and actionable steps to enhance the security of your MS365 email system, safeguarding your organization's sensitive information and maintaining the integrity of your communications. Don't miss this opportunity to make your MS365 email solution safer and more resilient against the ever-changing threat landscape.

### Don't Just Connect, Grow Your IoT Business with Cisco IoT Cellular Connectivity Management - BRKSPG-1002
Speakers: Christian Falckenberg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161411841001NJQt
From operating autonomous vehicles, to managing manufacturing robots, to tracking life-saving vaccine shipments, cellular IoT is transforming the way we work and live. Today there are over two billion cellular IoT connected devices worldwide, and the global cellular IoT market will exceed $18.2 billion by 2027. To successfully launch and manage thousands of devices in the field, organizations need to adopt new technical and operational approaches to allow them to scale faster, operate smarter, and protect better. In this session, you will learn how the key capabilities of Cisco IoT Control Center can enable you to rapidly innovate and expand your IoT business by delivering better customer experiences while lowering costs and streamlining operations.

### Driving Business Success Through Seamless Connectivity Across Datacenter, Cloud, and Beyond - PAROBS-1907
Speakers: Kyle Wickert (AlgoSec)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098464918001dY6D
In today's fast-paced business environment, the demand for rapid rollout of new applications and services is reshaping the way organizations manage connectivity. Business needs drive the urgency for seamless, secure, and consistent provisioning of security policies across diverse network security technologies. Simplifying connectivity delivery is essential for supporting business innovation and agility. Achieving this requires early visibility into compliance and governance during the design phase of access requirements, ensuring alignment with business goals and fostering collaboration among application teams, developers, and stakeholders. Empowering connectivity owners through self-service capabilities further accelerates the adoption of modern, scalable application connectivity management, enabling organizations to meet evolving business demands, while maintaining security and compliance. This session explores how businesses can standardize and streamline connectivity management to create a strong foundation for growth and innovation in the datacenter, cloud, and beyond.

### Driving IT/OT Excellence with AI-Powered Cisco Catalyst Center at the Worldwide Vehicle Industry - CSSENT-1144
Speakers: Marcello Ishida (Cisco), Bruno Silva (Scania LATAM), Tiago Santos (Scania LATAM)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098415765001dIV5
As a global leader in sustainable transportation, producing premium truck vehicles for over 130 years, Scania relies on seamless IT/OT integration for its diverse manufacturing operations across 100+ countries. Managing this complex network landscape poses significant challenges. Cisco Catalyst Center with AI empowers IT/OT excellence. This session explores how Scania leverages Catalyst Center's AI capabilities to: optimize network performance: gain real-time insights, predict and prevent IT/OT issues, and automate troubleshooting for maximized uptime boost efficiency: streamline workflows with intelligent automation and data-driven decision making enhance security: proactively identify and mitigate security risks across the converged network Join Scania's Network and Security Architect/Lead as they share transferable knowledge and real-world examples applicable to any organization navigating IT/OT convergence, showing how AI transformed their operations, leading to improved efficiency, agility, and security.

### Driving Innovation in Network Security and Visibility with AI - BRKOPS-2491
Speakers: Dave Zacks (Cisco), Errol Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098353784001djAe
Organizations everywhere need better security and visibility into network and application performance and control. The question today is, how can the latest wave of AI-enabled platforms help you get the insights, and implement the security controls, that you need? Attendees at this fast-paced, deep dive breakout will examine highlights from both Cisco's innovative Hypershield and Splunk portfolios to provide you with these tools and most importantly, showcase how you can use these tools in your own deployments. Presenting this session are Errol Roberts and Dave Zacks, both Cisco Distinguished Engineers as well as Cisco Live Distinguished Speakers as well as security and AI enthusiasts. Come to this fun, engaging session to see the latest Cisco and Splunk security and visibility tools in action!

### Driving Sustainability Excellence: Exploring Key Data Considerations and Metrics Modeling Approaches - BRKOPS-2064
Speakers: Marisol Palmero Amador (Cisco Systems, Inc.), Snezana Mitrovic (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098349468001daaG
Governments worldwide have a goal: net-zero emissions by 2050. Today, corporations are actively engaged in reducing their greenhouse gas emissions and tracking their progress. The path towards a net-zero strategy starts by grasping its business implications and determining which metrics, factors, and data to consider, collect, and use. While Scope 1 and 2 emissions are often straightforward to measure and even predict, Scope 3 typically accounts for the majority of a company's carbon footprint. This session aims to offer a comprehensive understanding of the parameters that should be considered when developing data-driven strategies for a sustainable future. It will prove beneficial for network operators, architects, and businesses, as well as SPs and enterprises.

### EVPN Deep Dive with IOS-XR Configuration Examples for Service Provider Metro and Data Center - BRKMPL-2253
Speakers: Jiri Chaloupka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098339050001db5t
This EVPN deep-dive session will explain EVPN (BGP) control plane in detail together with configuration examples for each use case, such as service provider metro (access) or service provider data center, and how EVPN can help integrate these two parts of the network together. The last part of the session will cover integration with existing services. This session will be real Deep Dive to technology.

### EVPN Troubleshooting and Debugging - BRKSPG-2473
Speakers: David Jakl (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161416414001N4Jk
EVPN is a technology initially designed for Ethernet multipoint services to provide advanced multi-homing capabilities. By using BGP for distributing MAC address reachability information over the MPLS network, EVPN brought the same operational and scale characteristics of IP-based VPNs to layer 2 VPNs. Today, beyond DCI and E-LAN applications, the EVPN solution family provides a common foundation for all Ethernet service types, including E-LINE and E-TREE, as well as data center routing and bridging scenarios. EVPN also provides options to combine layer 2 and layer 3 services into the same instance. This session is a continuation of the EVPN troubleshooting and debugging series presented in earlier Cisco Live conferences. This time, we will look into specific EVPN use cases related to EVPN convergence like Mobility, Fast-Reroute, IRB Gateway and more.

### Earning Your CCNP Enterprise Certification: What You Need to Know - BRKCRT-2008
Speakers: George Koukis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098288487001d5jZ
Are you an enterprise network professional ready to take your career to the next level? Do you want to develop your skills and increase your opportunities for advancement by certifying your expertise? If you answered "Yes", this session is for you!

### Elevate Your Digital Experience: Mastering User Journeys with ThousandEyes Transaction Testing - BRKCLD-1032
Speakers: Aditya Chellam (Cisco Systems, Inc.), Kiran Kabdal (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098276715001dPQu
Unlock the full potential of your internal and SaaS applications with ThousandEyes' transaction tests. In this session, you'll learn to monitor user journeys end-to-end, beyond basic page load tests. Discover how ThousandEyes can enhance user satisfaction by preventing disruptions, optimize performance with deep insights into server and network health, and drive business efficiency with strategies that keep you competitive in today's market. Join us to see how ThousandEyes can improve user experiences and streamline your digital operations.

### Elevating Broadband Networks with Cisco Subscriber Edge aka Cloud-Native CUPS BNG - BRKSPG-1315
Speakers: Gurpreet Dhaliwal (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161412967001NPH7
The Broadband Network Gateway (BNG) is essential for delivering high-speed internet services. Leveraging cloud-native technologies and the Control and User Plane Separation (CUPS) model, BNGs are evolving to meet the demands of modern broadband. This session offers an in-depth look at the TR-459 compliant Cloud-Native BNG (cnBNG), focusing on its architecture, operational advantages, and deployment strategies using Red Hat OpenShift, culminating with a hands-on demonstration. The session will delve into the cnBNG architecture compliant with TR-459 standard, emphasizing the benefits of CUPS, such as independent scaling and accelerated service rollout. We will discuss operational management, including the role of automation and streamlined maintenance to ensure robust broadband network. Focusing on deployment, we will demonstrate how to deploy cnBNG control plane on Red Hat OpenShift and use inbuilt monitoring tools for real-time visibility into the performance. A live demonstration will provide a practical example of deploying and managing a cnBNG Control Plane on OpenShift. Attendees will conclude the session with an understanding of how cloud-native BNGs can be effectively deployed and operated.

### Embracing DevOps for my NSO Use Cases lifecycle - DEVNET-2224
Speakers: Alfonso Sandoval Rosas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098441051001dhRt
Cisco Network Services Orchestrator (NSO) is a powerful platform for network automation and coding of custom services. However, have you ever wondered which version of your services is rock-solid stable, or why something that worked flawlessly in your lab is a mess in production? Or maybe you're scratching your head over why new features are throwing old ones out of whack? This session is your gateway to mastering those challenges. We'll explore how DevOps practices, automated testing and seamless packaging can become your new best friends. Get ready to design pipelines using tools like GitHub, Robot, and the official NSO Docker image, all tuned to supercharge your development & deployment process. Intermediate skills in NSO and Git are recommended. Check out our demo project in this repository, and let's turn those use cases into success stories together!

### Empowering Businesses with Secure, Private and Sovereign AI: A Guide to Deploying Large Language Models - DEVNET-2708
Speakers: Jock Reed (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098447911001dA9r
The success of large language models (LLMs) such as OpenAI's ChatGPT, Anthropic's Claude 2, and Google's Bard has indisputably sparked a renaissance in AI utilization across businesses. The ability to harness these powerful technologies is enticing, yet there remain understandable concerns about data security, sovereignty, and accessibility that need addressing. Enter a brave new world where you have control over your AI's data and infrastructure. This session provides a deep dive into deploying LLMs with open-source technologies on cloud-native infrastructure, fostering a ChatGPT-like interactive AI experience that is both private and secure. While the prospect of using and controlling your own LLM is enticing, the path to realizing it isn't without challenges. Join us as we unveil the nitty-gritty of managing your LLM on cloud or on-premise infrastructure. Gain insights into the trade-offs in terms of engineering time, costs, and performance, preparing you to navigate the potential pitfalls and unexpected hurdles. But we won't stop at just helping you deploy your models. This session will explore the steps you can take to safeguard the APIs and software that interact with your LLM services. By the end, you will be equipped with the knowledge to bring more control and privacy back to your users and developers, revolutionizing the way your business leverages AI technology.

### Empowering Inclusion in Tech: Shaping Future Tech Talent - IF-1769
Speakers: DP Venkatesh (Cisco Systems, Inc.), Sarah Walker (Cisco), Pablo Gabriel Steiner (Cisco Systems, Inc.), Rebecca Stone (Cisco), Chris Dexter (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098456273001d4tU
Join us for "Empowering Inclusion in Tech: Shaping Future Tech Talent," a session dedicated to unlocking the full potential of the tech industry through diversity. Discover strategies to create an inclusive ecosystem where diverse voices and perspectives lead innovation. We will delve into actionable approaches for building pathways that attract diverse skillsets to tech careers, equipping them with opportunities to thrive. Learn about successful initiatives that break down barriers. Mark your calendars and be part of the movement towards a tech future driven by inclusion and collaboration. Inclusive Communities represented :EMEA Women in Science and Engineering (WISE) and EMEA Women of Cisco (WOC)

### Empowering People and Technology with Cisco's AI-Powered Collaboration - CENCOL-1016
Speakers: Edel Joyce (Cisco), Amit Barave (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227079677001Jlkg
It IS possible to get employee experience right - and doing so is simpler than you might think. Join us as we show how IT, HR, and Facilities teams can be the HEROES of Hybrid Work by leveraging Cisco-powered workplaces and the Webex Suite. With hardware and software working together, backed by the power of Cisco's networking, security, and observability solutions, YOU can modernize every where and every way people and technology work. Stop by this session to learn how to transform your workplace, home offices, and anywhere you work into a sustainable, interoperable, intelligent, and manageable hub for Hybrid Work.

### Empowering Retail with Data: A Cisco Spaces and Webex Connect Solution - BRKXAR-1851
Speakers: Simon Light (Cisco), Jordan Kirby (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098396405001dJmW
Today's retail environments are data blind spots and are often competing with the data driven world of online shopping. Cisco Spaces and Webex Connect can help identify customers in store, engage with relevant information, and help guide customers to purchasing decisions. Participants will learn how to utilise Cisco Spaces and Webex Connect to significantly enhance instore customer experience by driving brand and product engagement, helping navigate the store environment and helping drive relevant offers. This session will include a demo of how to implement AI lead engagements, location-based marketing and foster customer loyalty through digital touchpoints. Participants should have a good understanding of today's retail landscape, customer loyalty and the technologies used to engage them.

### Empowering Use Case Provisioning and Closed-Loop automation: GenAI and Splunk in Action - AIHUB-1573
Speakers: Shrikanth Rao (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161392012001NKlT
Splunk is traditionally used in networking as an analytics tool with immense capabilities to identify & report anomalies. However, additional value to customers would come when we extend the feature to automatically remediate network anomalies as well as provision use-cases like configuration backup/restore, configuration compliance checks, Software upgrades etc. The solution leverages Splunk as the data ingestion platform and GenAI based agentic framework built using LangGraph to orchestrate features of various systems like Cisco Radkit, Cisco Catalyst center, ServiceNow etc. The solution also leverages cutting edge GenAI technologies like RAG fusion, advanced RAG indexing with LangSmith for traceability.

### Empowering Your Network with SD-WAN OMP: Path Optimization and Policy Insights Use Cases - BRKENT-3115
Speakers: Waqas Ahmad Daar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098311970001drig
This technical session is a comprehensive exploration of the intricate workings of OMP (Overlay Management Protocol) in SDWAN (Software-Defined Wide Area Networking). Participants will embark on a journey to understand the entire lifecycle of OMP sessions, beginning with the establishment process, exploring different fields, and gaining insights into reading logs and executing show commands. The session includes an in-depth examination of OMP's best path selection, where participants will explore various use cases and delve into the algorithmic aspects that drive efficient path selection. Additionally, attendees will discover how SDWAN policies are manipulated within the OMP framework through a series of practical use cases. Throughout the session, live demos will be conducted to provide participants with real-world demonstrations of OMP routing use cases, with specific scenarios in various topologies, including full mesh, hub and spoke etc.. The session also covers the SDWAN Multicast from the OMP perspective how control packets are exchanged to build multicast tree in SDWAN fabric. By the end of this technical deep dive session, participants will emerge equipped with a profound understanding of OMP's architecture, routing mechanisms, and policy manipulation capabilities within SDWAN. The knowledge gained will empower participants to optimize network performance, streamline data transmission, and overcome complex SDWAN challenges. Join us in this enlightening session to elevate your expertise in SDWAN OMP and pave the way for enhanced network efficiency.

### Empowering the Talent of Tomorrow from Root to Fruit - IF-1614
Speakers: Armand Leblois (Cisco), Ryan Rose (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098455531001dpqp
The Cisco Networking Academy and Cisco Learning and Certifications are two programs offering unique opportunities in technology education and professional development. Cisco Networking Academy: Over its 27-year history, the Cisco Networking Academy has empowered more than 8.8 million learners in the EMEA region, with 4.5 million in Europe alone. The Cisco Networking Academy program provides a free and agnostic curriculum that integrates seamlessly into educational systems throughout the region. Cisco Learning and Certifications prepares students and professionals with the skills and knowledge needed to confidently address the technology challenges of the future. It offers a variety of learning opportunities tailored to equip individuals for successful careers in the ever-evolving tech landscape. Today, as part of the Digital Impact Office, both the Cisco Networking Academy and Cisco Learning and Certifications present a unique offering to help employers source and develop the talent required for comprehensive, inclusive, and secure digital transformation. Discover how the Digital Impact Office can serve as a one-stop talent solution for you, your customers, and society at large.

### Enable Zero Trust Network Access for Industrial Networks with Cisco Secure Equipment Access - BRKIOT-1005
Speakers: Emmanuel Tychon (Cisco), Andrew McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098327342001dxe6
Industrial Network operators rely on 3rd party vendors to maintain equipment in their network. Can operators trust them to access their network securely? Zero Trust Network Access (ZTNA) is a security service that verifies 3rd party vendors and users, grants access to specific applications based on identity and context policies. By not allowing access to an entire network, ZTNA lowers the impact of a breach, reduces business visibility on the public internet, and minimizes security risk. Cisco Secure Equipment Access (SEA) not to be confused with Cisco's Secure Access, is a purpose built solution for ZTNA by allowing remote access into Industrial networks to ensure remote employees & vendors only access the devices that they have been given permission to access. This session explains the ZTNA solution, how it differs from a traditional VPN solutions, and how Cisco's SEA tailors' connectivity to OT environments.

### Enabling SP transformation through Autonomous Networking and the Cisco SP NaaS Framework - BRKSP-2133
Speakers: Brian Meaney (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161410706001Nxwm
The Communications Service Provider (CSP) market is undergoing the biggest transformation in the history of telecommunications. Increased competition and heightened expectation from their customers means now is the time for some radical changes. This session will focus on a number of growing trends in the Service Provider (SP) market, including the organisational split between the service layer (often referred to as the Service Company or ServCo) and the network layer (Network Company or NetCo). This transformation gives rise to a more simplified, automated, programmable and intelligent network layer whose characteristics are encompassed in the industry drive around Autonomous Networking. A more detailed description of objectives and desired outcomes of Autonomous Networks will be provided along with Cisco's three pillar approach around Network Simplification, advances in Automation and Autonomics and the need for Data Intelligence and AI. The session will proceed to describe the service layer or ServCo and identify some of evolving "service factory" solutions which are being developed to address the direct needs of their customers. The session will describe the Cisco SP Network as a Service (NaaS) framework and some use-cases specifically around the B2B segment which includes aspects of Enterprise connectivity, trusted services and security and cloud. The session will conclude with some discussion on the newer use-cases and other segments being supported in this framework.

### Enabling Smarter Workplaces - BRKCOL-2265
Speakers: Vanessa Sulikowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098283030001dXmk
As organizations settle into a more permanent hybrid work model they need to enable their people with the capabilities to successfully work from anywhere, including providing smarter more inclusive workspace experiences. This is leading to some new workplace capabilities requirements emerging, such as the need for real-time and historical workspace analytics, more intelligent booking solutions for more efficient workspace management, and intelligent capabilities and automation in the collaboration spaces. This session will delve into creating more intelligent workplaces by leveraging Cisco Spaces smart workspaces, providing more intelligent room scheduling and the shift to on demand usage models while still leveraging OBTP across the workplace, options of Navigator in stand-alone mode and detailed workspace analytics. This will include how to enable the right technology and capabilities for the different workspace types, to maximize, automate and customize the employee experience.

### Enabling stc's Digital Customer Experience Assurance - CSSSPG-2256
Speakers: Hatim Alshehri (STC), Elias Azar (Cisco Systems, Inc.), Omar Sinno (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098421562001dgPx
stc was the sole connectivity provider for the first global Esports World Cup which took place in Riyadh July-Aug 2024. stc is heavily invested in Cisco Networking tech - Cisco Routers, SIlicon One, 8k routers, ASR 9K, Automation/Crosswork Controller, Cisco Provider Connectivity Assurance (formerly Accedian Skylight), and ThousandEyes. In this session, we will present how stc relied on Cisco's Provider Connectivity Assurance (formerly Accedian Skylight), and ThousandEyes to ensure their end customer digital experience. Active monitoring of end to end circuit and per game monitoring and related actions, played a crucial role in the success of the event. In the session, we will highlight stc's ambition to achieve Autonomous Network with Cisco's Automation solution.

### End to End Segmentation with Cisco Catalyst SD-WAN and ISE - BRKENT-2166
Speakers: Ahmet Uncu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098307279001d71o
With the increased sophistication and number of network attacks, controlling the ability for threats to move laterally throughout the network is more important than ever. In this session you will learn how: The combination of SD-WAN and ISE will allow for flexible end-to-end macro and microsegmentation of users, devices, and applications ISE can assign secure group tags (SGTs) based on user/device identification, SD-WAN propagates those SGTs across the WAN, and policy can be created to control access to resources Integration with ISE allows security policy in SD-WAN to match on user identity instead of traditional attributes like IP addresses This session will be targeted for an audience with a baseline understanding of SD-WAN and segmentation concepts. The session will consist of a combination of presentation and demonstration. The presentation will focus on the details of the different integrations and segmentation options. The demo will focus on how to enable the integration, enable SGT propagation, and build policy.

### End-to-End Security Strategy for Enterprise Campuses with Catalyst 9000 Series Switches - BRKENS-2602
Speakers: Ama Owusu-Hammond (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098301134001dXm8
Enterprises are looking to overcome traditional security approaches that assume anything inside the corporate network can be trusted. The reality is that this assumption no longer holds true with mobility, bring your own device (BYOD), IoT, cloud adoption, increased collaboration, and a focus on business resiliency. This session is focused primarily on the Cisco Catalyst 9000 Series Switches, which can provide end-to-end security from campus and branch to cloud. The session also covers secure infrastructure with Cisco Trustworthy Solutions, secure transport with MACsec and IPsec (site-to-site, site-to-cloud), secure endpoints with native connectors, Cisco Secure Network Analytics (Stealthwatch), Cisco Umbrella, auto-profile and secure endpoints, and using endpoint analytics and trust analytics. After this session, you will be able to take away how Catalyst 9000 Series Switches are built with security in mind for fulfilling various use cases.

### Enhance Your Contact Center with Webex: A Developer's Introduction to APIs and Automation - CISCOU-2043
Speakers: Adam Weeks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098410031001d3Al
Explore the possibilities within the Webex Contact Center Developer Ecosystem in this introductory session. Whether you're a developer or a customer eager to understand what developers can achieve, this session will guide you through the fundamentals of Webex Contact Center APIs. Learn about common use cases, including administration, custom analytics, and tailored agent interfaces. Discover how these tools can be leveraged for effective troubleshooting and automation, providing the insights needed to implement innovative solutions in your organization.

### Enhanced Metric Visibility: Continuous Monitoring of Cisco Compute with Intersight - BRKCOM-1003
Speakers: Mohit Vaswani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098286820001dxcT
With complexity increasing in your datacenter, troubleshooting and understanding what is going on in your datacenter becomes challenging. In this session, we will use Intersight Monitoring to get real time visibility of what is happening to our servers and we will go back in time to understand what happened with our servers. How much energy did my servers consume? Do I need to increase capacity? Was there a network issue? These are some of the questions we will answer. Gaining insight into your datacenter may help infrastructure and operations (I&O) managers as they address aggressive SLO and SLA objective.

### Enhancing API Workflows with GraphQL - DEVLIT-1847
Speakers: Lori Jakab (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098425155001difq
REST is dominating the API world as well as most of your API calls. You make numerous requests to different services, and can receive a lot of information, sometimes too much. In some cases, you may spend a lot of time gathering data before doing what you really have to do. What if for certain use-cases you could make fewer requests, receive only the data you need and have it ready for your task? Join this session to learn how GraphQL can be layered over existing Cisco REST APIs to reduce latency, and improve batching and reusability under certain conditions.

### Enhancing Collaboration with the Future: Webex and Generative AI Integration - AIHUB-1000
Speakers: Omer Ilyas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161390649001NzV4
In this session, we will demystify the concepts of AI and Machine Learning (ML), positioning Generative AI as a transformative force within this spectrum, with a special focus on Large Language Models (LLMs). We'll delve into the technical essence of quantization and its role in optimizing AI performance. Following this foundational understanding, we'll explore how these innovations can enhance communication, culminating in a live demonstration that showcases the practical integration of generative AI with Cisco's collaboration solutions.

### Enhancing Network Automation with Event-Driven Architecture - DEVNET-1640
Speakers: Kareem Iskander (Cisco), Akhila Pamukuntla (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098434154001dbty
In today's fast-paced network environments, it's crucial to respond quickly and automatically to keep things running smoothly and securely. In this session, we will explore how to implement an event-driven architecture that seamlessly integrates NetBox for network management and documentation, Splunk for real-time data analysis and alerting, and Cisco Cloud Networking for robust network functionality. You will discover how to harness the power of these tools to create an agile network management system where events in NetBox trigger automated actions and alerts in Splunk, boosting overall network efficiency and reliability. We will: Explore the key motivations behind adopting event-driven architectures for network automation Delve into the inner workings of NetBox Events Demonstrate the practical application of Splunk, highlighting Cisco Meraki Dashboard and NetBox Events in action

### Enhancing Security Solutions with XDR and Splunk - CISCOU-1036
Speakers: Rob Gresham (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098401067001dzl5
Explore the integration of Cisco's XDR with Splunk's security solutions in our session, "Enhancing Security Solutions with XDR and Splunk." We examine current offerings, identify gaps, and uncover integration opportunities to optimize performance and customer value. By leveraging the strengths of both platforms, we aim to enhance threat detection, streamline workflows, and improve compliance coverage. Discover practical use cases and actionable solutions to overcome data integration challenges. Join us to learn strategic recommendations for aligning efforts and maximizing benefits, paving the way for a unified security platform.

### Enhancing Traditional Industrial Networks with Cisco SD-Routing: Monitoring, Security, and Management - BRKENT-1530
Speakers: Rishabh Mahajan (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098304751001dzAY
Industrial customers worldwide are increasingly adopting software-defined routing to enhance performance and reliability with revolutionizing network management. This session provides an introduction to SD-Routing, highlighting its fundamental capabilities, benefits, and implications for modern network architectures. SD-Routing reduces OpEx by leveraging the Cisco Catalyst SD-WAN Manager as the unified network management platform that can bridge the gap between traditional WAN routing and SD-WAN environments. It provides intuitive device lifecycle orchestration workflows for secure device onboarding, software upgrades, and cloud and security integrations, as well as monitoring and troubleshooting capabilities. SD-Routing offers a flexible and scalable solution to meet the evolving needs of modern enterprises. Via a live demo, participants will learn to onboard Catalyst IR1101, IR1800 and IR8340 routers to enable SD-Routing and experience enhanced monitoring, security & troubleshooting capabilities via Catalyst SD-WAN manager.

### Enhancing User Experiences with Data-Driven Intelligence - PSOSP-1868
Speakers: Tom Foottit (Cisco), Peter Coppens (COLT TECHNOLOGY SERVICES), Amrit Nijjer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098473279001dt64
Data is central to the autonomous network concept, with effective automation relying on actionable intelligence. All aspects of the network should be informed by data-driven inferences from network data, customer context, product context, and business inputs. Join this session to see how connecting these domains ensures services are optimized for network performance and CX. We'll explore building data-driven intelligence into network fabrics, incorporating observability and AI/ML, and using orchestration to bring intelligent action to the network. This supports richer features, superior performance, and sustainability while enhancing customer experience, reducing churn, and lowering OpEx.

### Ethernet Based Fabric for AI Cluster - Powered by Silicon One & SONiC, an Ultra High Performance, Scalable & Non-Blocking Ethernet Fabric - BRKCOC-3005
Speakers: Lieven Colman (Cisco), John Banner (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279978001dSBw
Network infrastructure practitioner session based on a Cisco-on-Cisco story explaining how we built multiple non-blocking Ethernet Fabrics for AI workloads. This session will cover the technology stacks used, key configurations considered, challenges faced and lessons learned while building network infrastructure to deliver 256 and 512 GPU Compute clusters for AI Workloads using Cisco SiliconOne with SONiC, and Nexus based networks.

### Evaluating and Improving Defenses With MITRE ATT&CK - BRKSEC-2227
Speakers: Mike McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098371115001df6O
Security architectures can pose complexity and cast doubt. How can we be certain that the solutions we have acquired are adequate? How can we know they are configured properly to cover the many vectors of attack? Cisco, and much of the industry, have taken to using frameworks like MITRE's Adversarial Tactics, Techniques, and Common Knowledge Database (ATT&CK) to help objectively assess those solutions and their coverage of the attackers that an environment is most likely to encounter. In this session, participants will follow along as we follow an example threat from identification to gap analysis and validation of mitigations. Together we'll: Discover the benefits of learning from the mistakes of others Learn and see how to use MITRE ATT&CK to evaluate their blind spots See demonstrations of Coverage Mapping, Secure Endpoint & Orbital Scanning, Threat Grid, and MITRE Caldera Use!

### Everything In One Place: Introduction to Splunk IT Service Intelligence (ITSI) - BRKOBS-1073
Speakers: Annette Sheppard (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098339419001dJZi
Are you looking for that mythical 'single pane of glass? Are you also looking to reduce your MTTD and MTTR? Join us to learn how Splunk IT Service Intelligence can help you gain complete visibility across your entire estate - from applications to infrastructure, business services, network health and help you identify "Is this a network problem?" Learn how Splunk ITSI applies AI and machine learning to help teams find and fix issues faster, and what exciting innovations and integrations, the team is planning for the future.

### Everything You Ever Wanted to Know about Power in Routers and Switches (and Quite a Bit More) - BRKGRN-2161
Speakers: LJ Wobker (Cisco), Lane Wigley (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098325149001dRBH
This session provides the foundation for a deep understanding of power usage in networking equipment. It discusses all aspects of power in routers and switches. Topics include provisioning vs. typical vs. peak power; power usage by component; how traffic, temperature, and other factors impact power usage; optimizing power supply efficiency; optics power; conversion loss; power redundancy models; thermal challenges in high power systems; modeling power consumption; and what does and doesn't move the needle on power savings during off-peak times. The session will also provide examples from system testing to support the concepts covered in this breakout.

### Evolving Network Security: From Managed SD-WAN to Managed Security - PSOMS-1794
Speakers: Rupal Hada (Cisco), Mohammed Ishaq (Emircom)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098471063001d5iy
As organizations continue to adopt cloud-based applications and remote work models, the complexity of network security has increased significantly. Traditional network security solutions, while effective, often struggle to keep pace with the evolving threat landscape. This session explores the evolution of network security, from Managed SD-WAN to Managed XDR. We will delve into the key benefits of Managed SD-WAN, including improved network performance, reliability, and visibility. Additionally, we will discuss how Managed XDR can extend security beyond the network perimeter, providing advanced threat detection, incident response, and automation capabilities. By combining the power of Managed SD-WAN and Managed XDR, organizations can achieve a comprehensive and proactive security posture.

### Expedite your Troubleshooting with SD-WAN Manager Tools - BRKTRS-2595
Speakers: Uma Mohanty (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098394218001dsWf
Cisco Catalyst SD-WAN Solution represents an evolution of networking from an older, hardware-based model to a secure, software-based, virtual IP fabric. With Legacy network it was very difficult to represent the network on the GUI and also take further troubleshooting steps based on some of the scenarios encountered on the network. SD-WAN solution being a evolved one, we not only have the GUI but also have a bag of tools that comes along with the SDWAN Manager that can help us troubleshoot the network further and expedite the resolution to the issues. This session will focus mostly on the bag of tools that comes along with SDWAN Manager which can be used to troubleshoot the issues further. We will discuss some of the tricky issues faced in the customers network and how to utilize these tools in order to expedite the troubleshooting and hence reduce the Mean time to resolution of the faults. This will be a fun session where we bring in some of the issues that have already been dealt in the past by the customers and we will see how the SDWAN Manager tools set helps us to identify & resolve the issues timely. The highlight of this session would be to showcase how well we can utilize the API docs on SD-WAN manager and gather some quick data points that can be used in out troubleshooting workflow.

### Experience Seamless Support: Unlocking Value with AI-enhanced TAC - PSOCX-1787
Speakers: Chris Dexter (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098466882001dd9O
Cisco Technical Assistance Center's (TAC) journey with AI started nearly a decade ago, embedding automation and analytics into the way our engineers work. Rapidly evolving into autonomous case handling through our award-winning TAC Virtual Engineer, the Cisco support experience is now powered by a suite of transformational AI capabilities. We're meeting you where you are by putting TAC innovations inside Cisco's products in new and exciting ways. Get inspired by the journey of AI-powered TAC and experience faster case resolutions, improved customer satisfaction, and more personalized, proactive, and predictive service. We are on a mission to make TAC THE key differentiator for Cisco, and we are eager to show you how we are enhancing your support experience with these capabilities today.

### Experience the Simplicity of SASE Made Easy - PSOENT-1864
Speakers: Eric Eddy (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098469251001dKXr
Imagine bringing together the power of Cisco Networking and Cisco Security to deliver an org-wide firewall policy engine that seamlessly centralizes policies across cloud, WAN edge, and LAN - all in just a few easy steps. You don't have to imagine anymore. Join this session to see how single-vendor SASE with Cisco removes the headache from secure networking to make managing resilient networks easier than ever.

### Experiences Amplified: AI and the Power of One Cisco Fuel Amazing Employee, Customer and IT Experiences - KDDCOL-1000
Speakers: Snorre Kjesbu (Cisco), Jay Patel (Cisco), George Farid (DB Schenker)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227082258001J7hH
Imagine a world where employees can work together seamlessly from anywhere in the world, and customer interactions are deeply personalized. Where AI Agents handle routine tasks, and AI Assistants support more meaningful, human interactions. The growth of AI is creating new possibilities with technology - and we're just beginning to see the benefits. Despite this, to realize the true value of AI, it needs to deliver better experiences. Experience sets employee productivity and customer delight apart from being just another technology trend. In this session, Snorre Kjesbu, Senior Vice President and General Manager of Collaboration, Employee Experience, and Jay Patel, Senior Vice President and General Manager of Collaboration, Webex Customer Experience, will explore the future of work and how Webex, supercharged with AI and the full power of Cisco's portfolio, fuel amazing experiences for employees and customers, driving better business outcomes.

### Explore AI Agent Capabilities: Revolutionizing Digital Interactions and Network Management - DEVNET-2427
Speakers: Oleksii Borysenko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098443918001dy4C
In this talk, we'll explore the transformative world of AI agents powered by large language models (LLMs) and their potential to revolutionize digital interactions and network management. We'll also explore how these sophisticated agents are reshaping corporate environments, network management, and cybersecurity approaches. Key points we'll cover include: AI agents' technical foundations include using LLMs, pattern recognition, and adaptive learning mechanisms. Real-world applications in cybersecurity, data analysis, and DevOps. Crucial capabilities such as autonomous decision-making, continuous learning, real-time processing, and natural language understanding. AI agents can significantly enhance network management by leveraging Cisco APIs. This integration allows for more efficient, automated, and intelligent network operations, demonstrating the practical benefits of AI agents in complex technological ecosystems.

### Exploring AI Possibilities: Creating an Experimental CCNA Mentor Chatbot - CISCOU-1045
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098404338001diof
Explore the innovative potential of AI in education with our experimental CCNA Mentor Chatbot. This session highlights how the chatbot explains networking topics, provides interactive study scenarios using Cisco Modeling Labs topologies, delivers on-demand multiple choice questions, and engages in dynamic dialogue to deepen understanding. Join us for a glimpse at how Learning and Certifications is looking to use AI to enable personalized learning for everyone in our community.

### Exploring the Future of Multi-Modal AI: Integrating Text, Audio, Images, and Video - AIHUB-1970
Speakers: Prapanch Ramamoorthy (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161392582001ND0y
One of the key ways in which generative artificial intelligence has started innovating and growing, is in the area of multi-modality. Multi-modal AI models enable systems to understand and generate diverse types of data including text, audio, images, and videos, thereby opening new avenues for applications across industries such as healthcare, entertainment, education, and more. This session, hosted by Prapanch Ramamoorthy and Patrick leMaistre who are both Cisco Live distinguished speakers, will provide an overview of multi-modal AI models, their underlying technologies, and their transformative potential. Participants will get to delve into the architecture and functioning of these models by getting at a fun, and still educational, live demonstration of various modalities of open source models that one can run locally.

### Extended Detection with Cisco XDR: Data, Analytics and Attack Chains - BRKSEC-2178
Speakers: Matthew Robertson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098370410001dSrW
Exactly what is an extended detection? This session will deep dive into the data and analytics pipeline in Cisco XDR and explore how Cisco XDR collects, synthesises, and analyses data to arrive at a detection of maliciousness, and create a correlated and extended incident. Covering multiple telemetry sources including network, endpoint, email and identity, this session will explore how analytics can bring these detections together and deliver on the XDR objective and accelerate your security operations.

### Extending CML: Terraforming the Lost City - BRKDEV-3008
Speakers: Quinn Snyder (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098298719001dHof
Now that Cisco Modeling Labs (CML) is API-enabled, the automation possibilities of ephemeral lab infrastructure are endless. However, if we truly want to turn our CML instance into a component of our DevOps-driven lives, we need to insert it as part of our network build pipelines. This session will show how using CML, Terraform, and some open tooling, we can build a continuous-delivery pipeline right from our source code manager of choice, with full change records as part of our pull-request (PR) workflows.

### Extending End-to-End Visibility Deep into Public Cloud Environments using ThousandEyes - BRKAPP-2161
Speakers: Mike Hicks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098273608001d4kY
As an operator responsible for managing networks, if you are seeking to extend and proactively monitor your cloud networks, you may have encountered challenges with the cloud networking visibility tools provided by your cloud provider. Often, these tools are tailored for developers and may not meet the needs of network engineers. In this session, we will showcase and explore methods to expand visibility throughout public cloud environments. We will delve into creating detailed topological maps of your AWS environments, illustrating service connectivity, configuration changes, and traffic patterns. By linking cloud infrastructure and services with user experience, application health, and end-to-end network paths, you will gain unparalleled insights that can empower network, SRE, and cloud operations teams to swiftly pinpoint and address their most complex issues.

### Extending Webex Contact Center with Flow Designer Extensibility - DEVNET-2915
Speakers: Adam Weeks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098449183001dMqj
Unlock the full potential of your contact center with Webex Contact Center Flow Designer Extensibility. This theater session provides an in-depth look at how to extend the capabilities of the Flow Designer using advanced features such as subflows, flow templates, flow and global variables, custom connectors, HTTP activities, screen pops, surveys, and custom events for virtual agents. Participants will learn how to work with data in Flow, utilize flow storage, and implement business rules engines to create more dynamic and responsive contact center solutions. You'll leave this session with ideas to help you understand how to extend the Flow Designer with advanced features, implement custom connectors and activities, and leverage flow storage and business rules engines to enhance your contact center operations. This session is ideal for developers and IT professionals with experience in Webex Contact Center. Join us to gain valuable insights and practical knowledge on extending the Flow Designer to create more efficient and effective contact center workflows.

### Falck's Network Transformation Journey with Cisco SD-WAN - PARENT-1852
Speakers: Ali Imran (Falck Danmark A/S), Rakesh Kapoor (HCLTech), Mads Johansen (Falck)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098463895001dKss
Discover how HCLTech successfully transformed Falck's network infrastructure with the migration from DMVPN to Cisco Catalyst SD-WAN across 200+ global sites. By deploying SDWAN cloud controllers and prioritizing critical traffic, HCLTech delivered a unified management platform, enhanced network stability with active-active WAN connectivity, streamlined policy enforcement, and robust end-to-end encryption. This comprehensive solution ensured improved performance, centralized visibility, and secure connections for all migrated sites.

### Fantastic APIs on your Factory Floor, and Where to Find Them. - BRKIOT-1073
Speakers: Stien Vanderhallen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098327702001dKkM
Keep your industrial networks close, but your APIs closer! The Cisco IoT portfolio is built to connect, secure, and ruggedize industrial networks. But isn't your business more than its network? The people in your warehouse are concerned with tracking product orders, and your production plant needs real-time, accurate monitoring of environmental conditions. By design, Cisco IoT is ready to support exactly those business-specific, critical use cases. Through programmable device interfaces, edge computing capabilities, and controller-level APIs, your industrial network becomes a catalyst for innovation. In this session, we will explore the programmability features of the Cisco IoT portfolio, and see them at work in real Cisco customer use cases.

### Five Emerging Trends Impacting the Future of the Internet - BRKGEN-1250
Speakers: Annie Hardy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098323967001dcl6
Everyone is keenly aware that there is much hope riding on the infrastructure plans in front of us. Business users find opportunities to use digital twins, digital-native workers join the workforce, cyber attacks are overwhelming industries, and AI is changing almost everything. In this session, Senior Visioneer Annie Hardy will walk through five key trends that are impacting the future of the internet, ranging from generative artificial intelligence, to the future of energy, spatial computing, and more. Expect to learn about how the future we see can impact the choices you make today.

### From Alerts to Action: ThousandEyes Meets ServiceNow - BRKCLD-2524
Speakers: Heba Dabbagh (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098278410001dyB9
In today's rapidly evolving IT landscape, efficient network monitoring and seamless alert management are more critical than ever. As organizations strive to maintain optimal performance and swift response times, the integration of powerful tools like ThousandEyes and ServiceNow becomes indispensable. This session explores the advanced functionalities of ThousandEyes Alerts and Custom Webhooks, and demonstrates how they can be seamlessly integrated with ServiceNow to enhance alert notifications and incident response. Participants will leave this session with practical knowledge on: Managing ThousandEyes Alerts to detect network issues proactively Utilizing ThousandEyes Custom Webhooks to customize alert workflows to specific requirements Integrating ThousandEyes with ServiceNow to streamline alert notifications and improve incident management processes This session targets network administrators, IT operations professionals, and those with a basic understanding of network monitoring tools. Expect live demos showcasing the integration in action to unlock the full potential of ThousandEyes and ServiceNow, transforming your network alerts into proactive actions.

### From Bot-tastrophes to Brilliance: How we are Transforming Infrastructure Provisioning at Cisco Live - DEVLIT-1749
Speakers: Jara Osterfeld (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098424790001d1hJ
Need a new VM, change request, or more resources for an app, like, yesterday? Welcome to the Cisco Live NOC team's world, where the event infrastructure is staged ahead of time, but within only two weeks. In this whirlwind, we aim to turn manual tasks into automated magic. Enter one of our star players: a chat bot, introduced last year to streamline our infrastructure provisioning process. In this lightning talk, we'll demo what the bot is up to today, share some hilarious (and slightly nerve-wracking) stories of how it almost became our VM villain last year, and preview our plans to make it even smarter next year. Whether you're a seasoned engineer or a newbie to automation, these 20 minutes will leave you laughing and inspired to 'bot up' your infrastructure game.

### From Digit Recognition to Large Language Models (LLM): Cisco Value Proposition - BRKAI-1371
Speakers: Antoine Orsoni (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161398507001NNgp
From face recognition to unlock our smartphones, to predictive outages in networking infrastructures, Artificial Intelligence (AI) is everywhere. Large Language Models (LLM), an AI subcomponent is the ability for a machine to understand and answer back in written human language. Everyone who sent a query to Chat GPT has thus already consumed a LLM. This introduction session will help participants understand how LLM are trained, fined-tuned and consumed; to clarify the role of Graphics Processing Units (GPU) for AI. This session will present examples of Customer's AI use cases and Cisco 3-Fold AI strategy. Participants are not expected to have any prior knowledge about AI.

### From Everything to Nothing to Everything : the Tale of Intersight, UCS and Nutanix - BRKCOM-1338
Speakers: Peter Charpentier (Cisco), Felix Maurer (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098287011001dNLv
Imagine workloads running on top a Cisco UCS server and Nutanix software. We take this setup and tear it down to factory default, and rebuild it in front of your eyes. This session will show you how to configure Cisco Intersight and Nutanix, step by step, from a state where the UCS hardware is fresh out of the boxes and unconfigured, to a state where virtual machines are happily running on a hyperconverged setup. By the end of this session, you will be equipped with actionable insights and the confidence to build your own server running Nutanix on UCS.

### From IT Challenges to Business Solutions: The Future of Observability - ITLGEN-1507
Speakers: James Hodge (Cisco), MANFRED RUEHRNESSEL (Engel Austria GmbH)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098458811001dHX7
Join us at this IT Leadership session to explore how the convergence of Cisco and Splunk technologies is transforming observability into a strategic business advantage. Discover how unified visibility across diverse tech stacks can power observability for the entire enterprise and learn how AI-driven triage can make issue resolution faster and smarter than ever before. We will hear real-world success stories from companies doing this today, and get an in product look at core functionality that can help your teams prioritize problems and help you optimize technology investments based on their impact to your business.

### From Infrastructure to AI Agents: Building a Framework for Trustworthy AI - CENAI-1310
Speakers: Vijoy Pandey (Cisco), Jen Yokoyama (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228982073001TTuj
As organizations increasingly integrate AI into their operations, building safe and trustworthy AI is critical to maintaining customer trust. And yet, according to Cisco's 2024 AI Readiness Index, only 1 in 3 organizations have highly comprehensive AI governance policies in place and 80% report shortcomings in data preparation for AI projects. Join Vijoy Pandey, SVP, Outshift by Cisco and Jen Yokoyama, SVP, Legal Innovation, Strategy and Technology for an engaging Center Stage conversation about Cisco's approach to AI and data governance. You'll leave this session with: - A clear understanding of the AI regulatory landscape and ways to avoid compliance missteps - Strategies for assessing AI products and vendors before deployment within your organization - Practical frameworks for building governance strategies that foster innovation and build customer trust Vision of how trust frameworks need to evolve as AI becomes more collaborative and agentic

### From Machine Learning to GenAI and Beyond: An Introduction to AI Technologies - BRKETI-1005
Speakers: Ivan Padilla Ojeda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098313401001d3Cz
In the dynamic landscape of enterprise operations, the integration of Generative AI heralds a transformative era of innovation and efficiency. This cutting-edge technology empowers businesses to not only analyze and understand data but to also create novel solutions and content. Cisco is introducing its new service allowing the secure access to all these GenAI resources, providing the IT departments with all the necessary tools for policy, control and billing. Cisco streamlines the integration of Retrieval-Augmented Generation processes, enabling enterprises to enhance their content creation capabilities by blending learned data with real-time information and creating a dynamic and responsive approach to generating context-aware content.

### From Network Automation to Network Autonomy. How the Crosswork and Splunk Portfolio can Help in your Journey for Transport Networks - BRKOPS-2033
Speakers: Roque Gagliano (Cisco), Henning Gehrts (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098348366001d6p2
Since the start of the SDN era, transport networks are adopting network automation and software defined technologies. Today, the new goal is to make network autonomous, just like a self-driving car. This session will drive attendees through this journey, starting with an introduction to automation and network autonomy and a review of the latest industry standards. The session will continue with a description of the latest updates from the Crosswork automation portfolio, including Crosswork Network Controller, Crosswork Network Services Orchestrator and Crosswork Planning. Finally, the session will address how Splunk can bring additional intelligence and AIOPS to add more use cases to our automation library of self-driving networks.

### From Packets to Predictions : Transforming Network from OSI-to-AI - BRKOPS-1079
Speakers: Rosario Medrano Pena (Cisco), Aavrinder Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098344420001d5lG
In this session, we will explore Cisco's solutions into the AI era, showcasing our AI-ready portfolio and AI-driven solutions that are reshaping the networking landscape. As organizations transition from human operated networks to AI-powered predictive networks, Cisco is at the forefront of that transition. Key topics include: Cisco's AI-Ready Infrastructure : Discover how our latest hardware is designed to support AI workloads and enable edge computing for real-time analysis AI-Driven Network Management : Learn about our AI-powered platforms and solutions that automate routine tasks, predict network issues, and optimize performance Intelligent Security Solutions : Explore how AI enhances our cybersecurity offerings, providing proactive threat detection and automated response mechanisms Data Analytics to Decision Support :'see how Cisco's AI solutions transform raw network data into actionable insights, enabling smarter decisions

### From Zero to Multi-Cloud Hero in 60 Minutes - BRKCLD-2409
Speakers: Pedro Antunez (Cisco), Matthew Howlin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098278049001daLe
As the session begins, the timer will start - and the countdown to Multi-Cloud'success will begin. You will see that it is possible to deploy a Multi-Cloud'setup in 60 minutes. Whilst the automation pipelines flow, attendees will be guided through exactly what is happening in real time. First up, deployment of an on-premises Cloud Platform, achieved through Infrastructure-as-Code and cross-domain orchestration of Application Centric Infrastructure (ACI), Virtual Machines and Kubernetes. Second, we extend to the Public Cloud using Cilium, deploying a microservice application across our Cloud locations. We will then monitor the distributed application with Hubble.

### Future-Proof Your Career with Cisco Security Certifications - CISCOU-1040
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098402528001dGrm
In today's complex cybersecurity environment, having the right certifications is crucial. This session explores Cisco's security certification paths, including network security, cybersecurity operations, and ethical hacking. Participants will understand the skills required, preparation strategies, and potential career advancements. Ideal for IT professionals at any level pursuing Cisco security certifications.

### Future-Proofed Workplaces - From AI Hype to Reality - ITLGEN-1503
Speakers: Keith Griffin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098458080001dajF
Generative AI offers tremendous opportunities for the workplace, but also comes with risks. This session will cover the application of AI to enable hybrid work and best practices to enable adoption of AI using Cisco's responsible AI framework.

### Future-Proofing Industrial Networks for Cybersecurity and AI - PSOIOT-1017
Speakers: Bryan Tantzen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098470523001dI1E
Operational Technology (OT) networks that support essential infrastructure are at a critical inflection point. Increasing cybersecurity threats, rising operational complexity, and a global shortage of skilled labor threaten their stability and efficiency. Simultaneously, the growing need for data-driven capabilities, AI-ready infrastructure and digital resilience demands modern, scalable, and secure networks. This session explores the opportunity to accelerate IT/OT collaboration, how to identify the right strategic solutions and partners and highlights the operational and financial benefits IT/OT collaboration delivers. Attend this session to learn more about how: Cybersecurity urgency and AI readiness are driving OT network modernization Operational networking leaders are accelerating IT/OT collaboration for success Early movers are seeing significant operational and financial benefits

### GAME Time! Will You Be the Networker of the Year? - BRKENT-2837
Speakers: Jerome Durand (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098311246001djLG
Learning is always better when it's fun. Come to this super quiz session and test your knowledge on enterprise networking technologies, routing, switching, wireless, Cisco SD-Access, SD-WAN... and more! You will have a great time and learn tons of stuff in a pleasant atmosphere... And who knows, maybe you will be the networker of the year!

### Gain Scalable, Deep Visibility into Network Traffic with Cisco Nexus Dashboard Data Broker - BRKDCN-1614
Speakers: Mallikarjuna Rao Mudigonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098289591001dEch
Visibility into network and application traffic has become increasingly important in our modern data centers. Network visibility is integral to network security, compliance, troubleshooting, and capacity planning. Custom monitoring solutions cannot cope with the explosive growth of data center networks. In order to match the port density and port capabilities of the data center, monitoring networks must also leverage those same switches used in the production network. Cisco Nexus Dashboard Data Broker (NDDB) is an automated, intelligent packet brokering solution that can scale with your data center. NDDB provides a software-defined, programmable solution that can aggregate, filter, and replicate network traffic using SPAN or optical TAPs for network monitoring and visibility. This solution offers a simple, scalable, and cost-effective solution that is well suited to customers who have a need for monitoring large amounts of traffic or business-critical traffic. This session will cover the following: Introduction to Nexus Dashboard Data Broker TAP and SPAN aggregation use case In-line monitoring use case Integration with other Cisco products Customer case study Demonstration of the NDDB interface

### Generative AI Demystified: How Cisco is Empowering the Future with LLMs - BRKXAR-2019
Speakers: Robert Barton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098397125001d7xP
Generative AI and LLMs have captured the world's attention, but how they work remains a mystery for many. In this session, we will break down the inner workings of the transformer, the core building block of modern Generative AI. We will explain how LLMs are designed and trained, and how they have been implemented in some of the most common tools, such as ChatGPT, Google Gemini, and LLaMA. We will explore how Cisco is unlocking the potential of GenAI and LLMs across our portfolio, from Cisco Security Cloud, to Enterprise Network systems, to Webex.

### Generative AI for Unifying User Experience Across Security, Networking, & Collaboration - BRKAI-2655
Speakers: Richard Jang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161399664001NjcR
AI is reshaping the world, from facial recognition and voice-enabled IoT devices'to the latest generative AI-powered chatbots. Its integration into our daily lives has unlocked unparalleled convenience and innovation. But how does AI actually work, and how is it transforming IT operations? Join this session to explore the technical fundamentals of how AI works, including machine learning, neural networks, and a focus on generative AI. Once we've covered the technical fundamentals, we'll dive into Cisco's cutting-edge generative AI technology across each domain, with a special focus on the Unified AI Assistant. This innovative solution integrates Cisco's platforms, delivering unified insights across networking, security, and collaboration dramatically improving IT efficiency and creates a cohesive experience across all Cisco software platforms! Don't miss the opportunity to learn how generative AI works and see how Cisco is driving the future of IT through the Unified AI Assistant.

### Get Out of the 90s: Modern Troubleshooting with Cisco APIs and Splunk - DEVNET-2879
Speakers: Juulia Santala (Cisco), Francois Caen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098448826001duX9
Are you fed up with your users blaming the network every single day? Do you waste vast amounts of time chasing down root causes across too many platforms? Your Cisco infrastructure is full of real-time data, telemetry, alerts and APIs. Yet your monitoring is stuck in 1999, with a classic mix of SNMP interface graphs, a pile of syslogs, and emails nobody reads. Is anybody even catching SNMP traps anymore? Become the hero of your network's story! In this session, you will learn how to utilize the APIs already available in your network to access troubleshooting data and telemetry from multiple sources, combine them in a meaningful way, and take better action faster. This session will take you on a multi-platform adventure full of demos, covering how Cisco solutions such as Catalyst, Meraki, ISE, and Splunk can be brought together for easier monitoring and troubleshooting. Let's sprinkle some magic on your use cases with a little help from your network's APIs!

### Getting Ready for Quantum Security and API Interaction for Post Quantum Cryptography - DEVLIT-1054
Speakers: Vinay Saini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098422660001dreC
Quantum computing is becoming a reality with new research paving the way for a functional QC with a Quantum advantage. Quantum Computers are fundamentally different from classical computers and need new ways of interacting with them via custom programming interfaces that can send the right pulses to alter the quantum properties and state of the qubit. Listen to our Quantum Enthusiast Vinay Saini talk about the quantum computing fundamentals, what you need to start using quantum security with Cisco Devices, and how APIs-based integration works between Cisco Devices and QKD [Quantum Key Distribution] devices.

### Getting Started with Policy-as-Code for Cisco configurations using Open Policy Agent - DEVNET-1167
Speakers: Lori Jakab (Cisco), Grace Brickley (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098429778001dnUn
As your enterprise policies grow in complexity and scope, it might be challenging to maintain them, particularly at scale. Open Policy Agent (OPA) is a generic policy-as-code open source engine that separates policy from business logic, allowing for centralization of policy review and analysis. Join this session for an introduction into the advantages of leveraging a centralized policy-as-code approach for your Cisco infrastructure.

### Getting Started with Secure Zero Touch Provisioning - DEVLIT-2062
Speakers: Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098426226001dCLB
Zero Touch Provisioning (ZTP) allows us to automate the deployment Cisco IOS XE and Catalyst platforms on enterprise and campus networks using the embedded CentOS "GuestShell" Linux Container and the Python and NETCONF API's to completely onboard, configure and manage network devices. This session details the ZTP and Guest Shell features and explores some common basic and advanced use cases. With the newest release of Cisco IOS XE, we now support Secure ZTP. This feature, including an explanation of the key components, including conveyed information, the ownership certificate, and the ownership voucher. The setup configuration for Secure ZTP will be covered in this session.

### Getting Up and Running with Open-Source Local LLMs on UCS - with NVIDIA and AMD - AIHUB-2102
Speakers: Dave Zacks (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161395029001NWEw
Many organizations need to deploy local LLMs leveraging private, confidential data using on-premises compute resources, leveraging Generative AI systems enhanced with RAG (Retrieval Augmented Generation). The Cisco UCS platform provides a number of key advantages for such deployments, including X-Fabric for unrivalled flexibility. Come to this session to explore how Cisco UCS can be used with both NVIDIA and AMD GPUs to accomplish this goal and see for yourself the benefits that this solution provides. Hosting this session is the dynamic duo of Dave Zacks and Patrick leMaistre, both experienced Cisco Live speakers as well as AI enthusiasts. Come to this session for a fun, engaging and fast-paced exploration of using open-source LLMs, RAG, and Patrick's own custom toolkit to drive LLM projects that you can deploy within your own organization!

### Global Major Event Security: Insights from Talos Incident Response - BRKSEC-2224
Speakers: Yuri Kramarz (Cisco Systems, Inc.), Giannis Tziakouris (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098370761001dvKZ
Imagine the challenge of defending against denial of service attacks, phishing, and malware in real-time during a major global events. The Talos Incident Response team plays a crucial role in ensuring the security of these events, which connect millions of viewers and participants worldwide. But what goes on behind the scenes to make each event a success? In this session, we'll share our experiences and dive into the cybersecurity strategies employed by hosting countries, supporting companies, and third-party participants to secure major events. Attendees will gain an understanding of the complexities involved in event security and the ongoing efforts required to stay ahead of emerging threats.

### Global Regulations On AI: Insights Before Action - AIHUB-1380
Speakers: Vardaan Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161391826001NxOY
Artificial Intelligence (AI) is the buzzword of this century with countless applications across diverse domains. The field is rapidly evolving with vendors swiftly competing to utilize its capabilities. However, governments and authorities worldwide recognize both the potential and risks of AI if mismanaged. As a result it has attracted significant global scrutiny as well. With the recently passed landmark EU (European Union) legislation on classifying and supervising AI, it's crucial for Cisco's engineers and management professionals to stay updated on the global regulations and sentiments towards AI ensuring their products and strategies are compliant minimizing legal and administrative roadblocks. This session aims to: Compare and contrast the existing domestic AI laws and trends in EMEA, AMER, and APJC regions Discuss the impacts and sentiments of the Hiroshima AI Process (G7 Summit), New Delhi Declaration (G20 Summit) and the Bletchley Declaration on AI Conduct an ideation session to identify potential socio-cultural and political risks of AI and develop strategies for effective compliance and innovation By attending, participants will gain valuable insights into navigating the complex AI landscape further futureproofing their innovations.

### Goodbye Legacy, the Move to an IPv6-Only Enterprise - BRKENT-2008
Speakers: David Prall (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098305834001dCsZ
This session is for those who currently have IPv6 deployed in a dual-stack environment and are looking to transition from dual stack, to IPv6-mostly, and on to IPv6-only. IPv6 was chosen as the recommendation for the IP next-generation protocol in RFC 1752 in January 1995. Many RFCs since have delivered updates and enhancements. The specification RFC 1883 was published in December 1995, becoming RFC 8200 (STD 86) in July 2017, making IPv6 an internet standard. Just as we've said goodbye to legacy protocols IPX/SPX, DECnet, AppleTalk, and others, it is now time to say goodbye to IPv4. IPv6 is becoming a mandatory requirement across EMEA. In Germany the IPv6 mandate for German government was released in November 2020. There is a mandate for Dual Stack on Web Servers in NL. The Czech Republic has set 2032 as the end date for support for IPv4 and there are more mandates in Norway (paragraph 12) and a lot of activity in Belgium. Outside Europe the most significant mandate is Memorandum M-21-07 in November 2020, titled "Completing the Transition to Internet Protocol Version 6 (IPv6)." They set a timeline for 80% IPv6-only completion by September 30, 2025, end of fiscal year 2025. In this session, we will focus on the move from dual-stacked IPv4 and IPv6 enterprise infrastructure to an IPv6-only infrastructure. What do we need to know before we make the move? What about IPv4-only enclaves? We will look at NetFlow as the picture of truth and NAT64/DNS64 as the transition gateway(s).

### Green Tech: Driving Growth and Solving Environmental Challenges - IFGRN-1050
Speakers: Patrik Moller (CorPower Ocean), Mary de Wysocki (Cisco), Jon Koplin (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098456983001dFjq
In this session you will meet fellow technologists who are driving innovations designed to help the world avoid the consequences of climate change. You will hear how companies can help accelerate these technologies through funding, investments, knowledge sharing and their ecosystem relationships. According to a McKinsey report, many of the climate technologies needed to reduce greenhouse gas emissions in the atmosphere already exist. The challenge now is accelerating innovation and scaling them to achieve technical and commercial breakthroughs. This session is targeted towards anyone with an interest in sustainability and no advanced knowledge is required. Get inspired about the role technology plays in powering an inclusive and sustainable future.

### Growing Your Technical Career: Looking Forward and Lessons Learned - BRKGEN-1002
Speakers: Dave Zacks (Cisco), Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098323183001dmgv
Everyone needs to grow their career, through the inevitable twists and turns on the way. Finding your right path, one that suits your skills, interests and passions, is not simple. Come to this session to explore with two Cisco Distinguished Engineers the evolution of their careers, the challenges, triumphs, and pitfalls encountered along the way, and the lessons learned as a means of navigating your own career journey. This session will be hosted by the dynamic duo of Peter Jones and Dave Zacks, two friends who have navigated their career paths, together and apart, for over a decade. Come learn about growth, mentoring, and inclusion, and explore areas that can help guide your own technical and personal career journey.

### Guardians of the Network: How Meraki MV Cameras and MT Sensors Secure the Future - BRKMER-1691
Speakers: Victoria Engh (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098335853001d8Lb
In today's fast-evolving digital landscape, safeguarding physical and digital assets is crucial. Join us for an engaging session where we explore the powerful capabilities of Cisco Meraki MV Cameras and MT Sensors, reimagined through an immersive narrative. Follow our team of "Guardians of the Network" as they uncover the full potential of Meraki solutions to protect against real-world cyber threats. Through real-time monitoring, environmental data analysis, and intelligent threat detection, this session will show you how to leverage Meraki technology to keep your network and environment secure. Learn how these tools provide actionable insights, detect vulnerabilities, and empower organizations to stay one step ahead of malicious actors. Whether you're a security analyst, IT specialist, or network engineer, this session will dive into the knowledge on integrating Meraki MV Cameras and MT Sensors for a secure, future-ready infrastructure. Takeaways: Advanced features of Meraki MV Cameras for threat detection and network monitoring How Meraki MT Sensors provide critical environmental data Best practices for integrating these technologies to create a secure, vigilant network environment

### Guided vs. Autonomous Incident Response: 3 demos how Cisco XDR will streamline your SOC using Low-to-no-Code Workflows - DEVNET-2214
Speakers: Christopher Van Der Made (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098440701001dfCe
This session will show how the power of automation can be leveraged through Cisco XDR Automation without needing to write any code (but having the flexibility to do so as needed with the embedded low-to-no-code platform). This will enable organizations to make the R count double in Cisco's XDR (eXtended Detection and Response). We will also review what parts of incident response should be guided, and which can be fully autonomous. We will walk through 3 valuable real-life demos that will make you hit the ground running. We will use the amount of clicks that are needed in the console as metric, to prove to you how you can get access to powerful automation without too much hassle. At the end, you will also learn how to take this a step further and slowly become a master at automation for your security operations. You will get all of the materials afterwards to get started yourself. This session is meant for incident responders, security analysts, SOC managers, or anyone with interest in automation and security.

### Hardening IT Environments: A Proactive Approach to Security - CISCOU-2047
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098411451001doPm
As cyber threats rise, strengthening IT infrastructure is essential. This session covers key techniques to harden systems and protect against vulnerabilities, aligning with cloud-first strategies. Key takeaways include practical methods for securing infrastructure and enhancing resilience. Designed for IT professionals, the session features real-world examples to boost your cybersecurity skills.

### Harness AI to Accelerate Time to Value with Cisco UCS - PSODCN-1872
Speakers: Eugene Kim (Cisco), Mahesh Natarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098467964001dIBC
Is your company considering using AI to innovate, improve efficiency, help make better data-driven decisions, reduce costs, or enhance customer experiences? In this session, learn how Cisco UCS servers and validated solutions can help you get your data center AI-ready, designed and optimized to handle the unique demands of AI workloads. With Cisco's expertise and UCS-based solutions, you can be confident your AI solutions will be implemented with the security and performance you demand.

### Harness a Bold New Era: Transform Data Center and Service Provider Connectivity - KDDDCN-1000
Speakers: Jeremy Foster (Cisco), Colin Bannon (BT), Vladimir Ester (Cluster Power), Kevin Wollenweber (Cisco), Tom Gillis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227082424001JxmR
Step into the most intense period of innovation the technology industry has ever seen. The relentless surge in bandwidth requirements and scalability demands fueled by AI, cloud computing, IoT, streaming services, and observability is reshaping every aspect of our business and yours. Prepare to be inspired as new innovations are unveiled. This session will dive deeper into how Cisco is enabling service provider and data center businesses to unlock unprecedented value through AI-native infrastructure, simplified operations, and groundbreaking solutions.

### Help Me Identify and Implement the Right SIEM/SOAR Capabilities at the Right Time - BRKSEC-2322
Speakers: Angelo Brancato (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098373627001dUXR
In this session, we take on the role of a customer who has purchased Cisco/Splunk SIEM/SOAR and wants to maximize their investment. The one thing that both the vendor and the customer need to avoid is "shelfware", which we address by defining and implementing an adoption roadmap. You will learn how this roadmap is built and how we support this fictional customer (based on a real customer situation) to implement specific capabilities. Namely: Operationalizing the right Use Cases and Risk Based Alerting.

### High-Density Wi-Fi Design, Deployment and Optimization - BRKEWN-2087
Speakers: Josh Suhr (Cisco), Matt Swartz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161402787001N02z
This session will cover an array of detailed tips, tricks, and tools for configuring and optimizing high-density Wi-Fi networks in today's most challenging environments, including valuable real-world insights on how the latest Cisco Catalyst access points, antennas, and Catalyst wireless controllers can be leveraged to deliver an optimized and reliable user experience. Attend this session to hear real-world hints directly from engineers who have deployed networks for some of the largest sports venues and events worldwide.

### High-Value Wavelength/Private Line Services:- Understanding the Customer and Provider Perspective - BRKOPT-1005
Speakers: Christian Schmutzer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098358875001dAoG
Routers are no longer expensive nor power hungry it's time for a change! Stop considering DWDM and OTN for High-capacity point-to-point network connectivity and embrace a converged MPLS / segment routing network for delivering bit-transparent 'circuits' with 5-nines reliability, low latency and guaranteed high capacity. In this session, service SLA attributes will be discussed and how technology building blocks such as EVPN-VPWS, PLE, OAM, circuit-style SR-TE, PCE, QoS and protection paradigms can work together to deliver those mission critical services in a fundamental new and beneficial way for both end-customers and service providers.

### How AI-Powered Webex Suite and Calling Deliver Exceptional Employee Experiences - PSOCOL-1785
Speakers: Shweta Vijayaraghavan (Cisco), Manu Parhar (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098465615001d58R
Webex Suite is a comprehensive, AI-powered collaboration solution with 8 powerful workflows, built for today's modern work. Join this session to discover how Webex Suite and Calling are redefining communication in real-time and async by harnessing the power of AI to ensure millions are seen, heard, and feel included in the conversation. Get a peek behind the curtain with an in-depth session that explores our latest innovations transforming the workplace and enhancing collaboration with the Webex Suite. You don't want to miss this session!

### How Cisco Devices can Make your Microsoft and Zoom Meetings Better - BRKCOL-2697
Speakers: Dustin Baker (Cisco Systems, Inc.), Astrid Kongelf Jensen (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098284471001dE26
Cisco has went all in on making our devices the best overall interoperable experience no matter your meeting platform. This technical session will go in depth to explain how our unique architecture allows us to provide rich native experiences in multiple platforms, while still providing unique industry leading features powered by RoomOS! We will dive deep into the methodology and intent behind how we were able to accomplish this. Topics will include: RoomOS - The foundation What is RoomOS? How we provide Android in a Container vs Hypervysor Using On-device AI vs Cloud How this benefits other meeting platforms (MSFT, Zoom, Google) How to co-exist with other platform AI features Device Management How do we work with other platforms to make management easier Talking together ? How we leverage API's to communicate to MSFT, Zoom, and Google What's Next? How can we leverage our unique platform to provide next generation features and functionality Sneak peek into the "art of possible"

### How Cisco uses Generative AI to make TAC Engineers Super-Human - AIHUB-2008
Speakers: David White (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161394292001NF1n
Everybody is talking about Generative AI, but few are actually implementing it into production. Come hear how Cisco is leveraging the latest in Generative AI to assist Cisco TAC engineers to solve customer problems more quickly. This session will cover: Cisco TAC's approach to AI Overall architecture of solution How we inject AI right into a TAC engineer's workflow How we measure usage, value, and accuracy Feedback from our engineers Approaches you can take to leverage Generative AI at your company

### How Decathlon Enhanced Visibility, Security and Automation on their Networks Leveraging Cisco Meraki API - CSSMER-1868
Speakers: Julien Riby (Cisco Systems, Inc.), Remy Beaucamp (Decathlon), Guillaume Sauvage (Decathlon)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098418986001dUHw
With the increasing demand for IT operations to be managed more efficiently, the Cisco Meraki API became a game changer for Network Administrators. Decathlon, a renowned sporting goods retailer, had the same expectations and will share their experience in this session. You will leave this session with ideas on how to begin or enhance your Cisco API journey, save time by avoiding redundant activities, uphold your security standards and communicate more efficiently with your field engineers. Decathlon's IT team leveraged the Meraki API to its full potential to enhance visibility, security, and automation on their networks. They created a web-based application portal to easily: - push configuration across thousands of networks within seconds - meet their security standard across 70 countries - get a centralized view on firmware compliance - provide autonomy to field engineers - monitor best practices Participants will see a live demo of the portal and gain insights into how the tool was designed. Whether you are a beginner or an advanced Cisco API user, come join us to discover more about this remarkable success story.

### How Sustainability Data can Unlock Business and Environmental Benefits - PSOGRN-1893
Speakers: Colin Seward (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098469612001dR7s
Having accurate sustainability-related data, such as product energy consumption and greenhouse gas (GHG) emissions, is important to a business for many reasons. It can help you better understand your environmental footprint, more accurately report your emissions, and inform more strategic business decisions. This is especially important today, with AI driving a need for more computing power and more energy. Building robust datasets can be a complex endeavor; however, Cisco has risen to the challenge with the Sustainability Data Foundation (SDF), and end-to-end platform that connects a variety of complex datasets and shows them through user-friendly dashboards. A sold data foundation can help you understand the environmental footprint of your installed base, and the financial and environmental benefits of modernizing your existing infrastructure. During this session, you will learn about the importance of accurate sustainability data, how a company can compile those datasets, and how the information in Cisco's SDF can help you with your business and sustainability goals.

### How a Digital Twin Delivers $14.2M in Annual Benefits - PAROBS-1678
Speakers: Chiara Regale (FORWARD NETWORKS)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098464738001dTmE
Recent research found that the average Forward Networks customer experiences an impressive $14.2 million in annual benefits. These benefits encompass reduced downtime, heightened productivity, and additional operational efficiencies. For example, the time savings for one use case delivers the equivalent of over 90 additional full-time employees. Join our Senior Vice President of Product and User Experience, Chiara Regale, to hear real-world examples of how ForForward Networks enables clients to realize substantial financial advantages.

### How a Global Entertainment Company Accelerates Modernization Efforts With a Digital Twin - PAROBS-1095
Speakers: Chiara Regale (FORWARD NETWORKS)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098464556001doFA
Join this session to learn how a multinational entertainment company used the Forward Networks digital twin to accelerate global modernization efforts and improve the effectiveness of automation tasksefforts. An always accurate network inventory, including OS versions, provides the foundation for a global modernization effort while pre and post-change configuration checks to ensure automated updates deliver the expected results

### How to Adopt Zero Trust using SD-Access and Default-Deny without Tears - BRKENS-3810
Speakers: Raphael Lienard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098302580001dB8K
In this session, you will learn how to leverage the full potential of Cisco SD-Access within a Zero Trust Architecture. Discover all the requirements and best-practices before breaking the network by turning the default security policy from Permit IP to Deny IP. You will also get insights on how to combine Cisco Telemetry Broker and Splunk to create a TrustSec live-log dashboard.

### How to Be a Network Engineer in a Artificial Age? - CISCOU-1044
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098403982001dLBT
'I'm sorry Carl, I'm afraid I can't do that.' Are we approaching the time when the network might decide it knows better than the engineer at the console? Are we on the cusp of a new age of network engineering - THE ARTIFICIAL AGE? It is certainly a time of excitement, ideas, and maybe a bit just a tiny big of fear. That's okay, that is what it means to be a network explorer and we are totally here for it. Join this session where we consider how AI fits into programmability, automation, and NetDevOps.

### How to Build a Secure Multi-Cloud Environment with Cisco Secure Workload and Multicloud Defense - BRKSEC-2421
Speakers: Dirk Stoeckmann (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098374347001drKh
Join this session on Cisco Cloud Security and protect your Cloud with precision. We will delve into the cutting-edge world of cloud security. With cloud computing dominating the digital landscape, safeguarding data and applications is non-negotiable. In this breakout, we'll explore a layered approach to fend off cyber threats and unauthorized access. Discover how to fortify public cloud environments using Cisco Multicloud Defense, securing the Ingress/egress and achieving robust segmentation between virtual networks. Elevate your cloud security with Cisco Secure Workload and embrace micro-segmentation strategies for comprehensive application protection. Immerse yourself in practical use cases and master the art of operating on a policy model for seamless defense. Don't miss this opportunity to enhance your cloud security knowledge and safeguard your organization's future. Register now for an empowering journey into cloud defense excellence.

### How to Choose the Correct Branch Router - BRKENT-2139
Speakers: Jason Yang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098306566001doX1
Having a tough time choosing the proper branch platforms? This session will help you get back to the basics, to understand the changes in the WAN landscape, what are the new branch use cases and the well-established ones, and show the simplified T-shirt size branch platform selection based on those use cases. You will learn about the flexible Catalyst 8000 branch platform architecture and demystified DNA license along the way.

### How to Choose the Right LLM for Your Application - AIHUB-2007
Speakers: Robert Barton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161393899001New8
ChatGPT exploded on the scene in 2022 and has seen unprecedented adoption ever since. In the meantime, several other compelling LLMs have emerged, including Google Gemini and Anthropic Claude. As well, there are numerous powerful open-source LLMs available, including LLaMA and BERT. What's the difference between these models, and which one should you choose for your application or project? How does Cisco choose LLMs for our solutions? In this session, learn key differences between popular open-source and closed-source LLMs. You will learn how to benchmark LLMs, and how you can get your own LLM up and running in a matter of minutes. At the end of the course, you'll understand how LLMs can apply in your projects.

### How to Get the Most out of your Events and Interactions with Clients and Employees using Webex Events and Webex Webinars - BRKCOL-2663
Speakers: Clemens Geyer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098284293001d3Gh
In a hybrid world, like the one we are in now, it is difficult to connect your attendees if you have hybrid or virtual events. You have surely wondered if the message reaches your attendees, if you are connecting your virtual audience as you would in a physical event, and you have also asked yourself how to have the best of your brand for both people who are on site and people who are remote. In this session, you will learn how to have your audience connected to your message, how to keep your brand in the top of mind of your participants in hybrid and virtual events without losing the experience. This session will demonstrate how to make events effective in a hybrid world using Webex Events, Webex Webinars and Slido.

### How to Improve Digital Channels Customer Interactions with Video Combining Instant Connect and Webex Connect - DEVNET-2701
Speakers: Victor Vazquez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098447728001daMz
Organizations in all verticals want to improve customer service, and being able to offer video communications with experts is demanded. For end customer based use cases, solutions need to be easy to use, and offer the possibility to employ customer digital channel of choice. Join us in this session to explore Instant Connect video features and APIs, and to learn how you can integrate them into digital channels with Webex Connect (CPaaS). You will leave this session: Understanding how Instant Connect will enable you to have WebRTC based video communications, leveraging its APIs With a real use case example of Webex Connect orchestration power, integrating not only with Instant Connect but also with externals systems like CRMs With a fully working Webex Connect flow in your own developer sandbox

### How to Network LLMs! Splitting Large Language Models Running on GPUs Across a Network - BRKOPS-2931
Speakers: Dave Zacks (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098357780001dsak
We all know that LLMs can do some amazing things. But as capable as they are, they often don't fit in a single GPU or even a single server with multiple GPUs. Enter the network split the AI models across multiple hosts and use the network to link them to address this gap! Come to this session to learn how a properly designed network can distribute your AI model across multiple systems and use the network to link them on-premises with private, local data sets! This session is delivered by the dynamic duo of Patrick LeMaistre and Dave Zacks, both distinguished Cisco Live speakers. Come to this session for a fun, engaging deep dive on how the networks are critical in hosting large AI models all within 60 minutes from start to finish!

### How to Optimize SaaS Applications using Cisco Catalyst SD-WAN? - BRKENT-2630
Speakers: Sai Suchandan Reddy Marapareddy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098310109001dQpR
Cisco Catalyst SD-WAN builds a secure, unified connectivity over any transport and provides simplified operations with centralized management, policy control and application visibility across the Enterprise WAN Network. Catalyst SD-WAN offers Cloud OnRamp for SaaS to optimize SaaS applications and provides a seamless way to use Internet circuits for SaaS applications. Cloud OnRamp for SaaS helps mitigate SaaS user experience challenges with unreliable circuit performance changes and Optimize SaaS user experience by leveraging path probing & failover to alternate best paths when circuit performance changes. In this session, we are going to cover the latest innovations around Cloud OnRamp for SaaS on how we can further enhance SaaS optimization for Microsoft 365, Webex, etc. & Custom Enterprise SaaS Applications using the Cloud OnRamp for SaaS and cover on how to Optimize SaaS applications when going via SSE.

### How to Prepare for the CCNP Enterprise Advanced Routing Concentration Certification - BRKCRT-2016
Speakers: Muhammad Aamir (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098288683001dvjM
Are you an Enterprise routing professional and considering pursuing CCNP Enterprise certification? Do you need a deeper understanding of the technical topics covered to pass the Advanced Routing concentration exam? If you answered "Yes," this session is for you!

### How to Setup a Nexus HyperFabric from Scratch - BRKDCN-2907
Speakers: Ramses Smeyers (Cisco), Christopher Paggen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292376001dvWO
Imagine a fully functional Nexus HyperFabric where virtual and physical workloads are happily communicating, where leafs are talking BGP and where everything is pretty. We are going to take that fabric and "write erase" it all before your very eyes. We will then rebuild it completely together step by step and bring it all back to its fully working state!

### How to Setup an ACI Multi-Site with Single Pod and Multi-Pod - BRKDCN-2919
Speakers: Ramses Smeyers (Cisco), Max Ardica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098293499001d9fZ
Imagine a fully functional ACI multi-site domain comprised of a single pod fabric and a multi-pod fabric where virtual and physical workloads are happily communicating across all sites with locally optimized layer 3 outs. We are going to take that fabric and "write erase" it all before your very eyes. We will then rebuild it completely together step-by-step and bring it all back to its fully working state.

### How to Successfully Champion an IT Project - Learn the Language of Executive Decision Makers - BRKGEN-1008
Speakers: Jerel Howell (Cisco), Tim Anderson (Cisco), Pat Bodin (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098323556001dpZ7
Have you ever felt like you are speaking a different language than your leadership? Do you find it difficult to translate the importance of a budgetary request that has been declined? Would you like to learn how to document a technical need in such a way that it is understood by the non-technical executives who must approve your request? You are not alone! This session will equip you with the language and processes necessary for you to understand your relevance to the business and turn you into an IT Hero!! The knowledge you gain will elevate you from being a good engineer/architect to a valued IT Strategist. This session will include a bonus section from a guest speaker about the impact of AI on the landscape of IT, both from an architecture and leadership perspective, and what you should be doing now to remain relevant in the coming years.

### How to Use Multimodal LLMs to Unlock Enterprise Data for Key Use Cases - AIHUB-2596
Speakers: Mahesh Viswanathan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161397331001NWkh
Enterprise-generated documents consist of visually crowded content with diagrams, workflows, invoices, purchase orders, contracts, financial reports, spreadsheets, insurance claims, and other similar records. These documents carry rich semantic content that is embedded in text, tables, and figures. These mixed mode documents can be analyzed by generative AI, specifically multimodal LLMs, to understand information buried images or images-and-text. Imagine being able to find and answer questions such as "which was ABC Corp's top selling product for 2022?" or "what is the year-to-date and five-year performance of ABC?" or "how many POs have we processed this year?" hidden in pie charts and spreadsheets in a corpus of PDFs. Multimodal LLMs can be used to process and comprehend both visual text and visual objects and the interplay between the two. Join us to understand how this transformative technology can be used for your enterprise and to build new value-added services for your customers. We will walk through examples of how to use this technology, which LLMs to use, and how to apply it to some common enterprise use cases. You will understand how it opens up new search and retrieval capabilities for your visually rich documents across industry use cases. Finally, gain a deep understanding of what challenges there are for its adoption, and how to mitigate them. This session will be an intermediate level and is for an audience that has some experience using generative AI for text-based applications.

### How to be a CIO: A Practical How-To Guide to being a CIO - ITLGEN-1500
Speakers: Fletcher Previn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161421673001NuYZ
Every minute an employee spends struggling with a system is a minute they're not doing the work they were hired to do and the work they're passionate about. That's friction that IT has a unique responsibility to alleviate. Join Fletcher Previn, Cisco SVP & Chief Information Officer, for a keynote address on the unique role and responsibility of IT in shaping culture and employee experience in enterprise organizations, and how Cisco IT leverages AI as a force multiplier.

### Human-Centered Design in AI: Bridging Ethics and Innovation - IF-1029
Speakers: Rishabh Mahajan (Cisco Systems, Inc.), Nikita Joshi (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098453077001dONU
The convergence of AI and Human-Centered Design (HCD) presents an exciting yet complex landscape in today's technological sphere. As AI systems become increasingly integrated into our daily lives, it is imperative to prioritize human values, inclusivity, and ethical considerations in their design. This design thinking session aims to delve into the critical intersection of ethics, innovation, and user-centric approaches within AI development along with exploring how the principles of HCD can be harnessed to ensure that AI technologies are not just advanced but also ethically sound and user-centric. Through a series of design thinking tools such as empathising with users, defining relevant problems, ideation sessions and rapid prototyping exercises, participants will gain insights into the end-to-end Design Thinking methodologies and frameworks. As an outcome, the strategies from the session can enable the infusion of ethical considerations throughout the AI development lifecycle and place human needs and ethical concerns at the forefront.

### Hybrid Agent - Where AppDynamics and OpenTelemetry Meet - BRKOBS-3603
Speakers: Alexander Stoklasa (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098344067001dVFU
With the adoption of hybrid and polyglot application architectures, achieving comprehensive observability is essential for optimal digital resilience. This session offers an in-depth exploration of the AppDynamics Hybrid Agent, providing seamless integration between Cisco AppDynamics and OpenTelemetry instrumentation. Participants will gain insights into: Core concepts of the AppDynamics Agent How to enable OpenTelemetry within AppDynamics Key capabilities related to traces, metrics, and logs How to correlate instrumented services between AppDynamics and OpenTelemetry You'll leave this session with ideas to help you integrate and optimize your observability practices, including practical demonstrations of the Hybrid Agent and methods for debugging the OpenTelemetry pipeline. Basic understanding of APM and OpenTelemetry is recommended. Enhance your observability practices and drive better performance insights with Cisco AppDynamics and OpenTelemetry.

### IP/Ethernet Storage Networking for AI Infrastructure - BRKDCN-2945
Speakers: Paresh Gupta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294941001dzv0
This session covers the following topics: Storage networking design and operations for AI training and inferencing workloads. Cisco UCS connectivity options using networked file, object, and block storage protocols Foundation of Priority-based Flow Control (PFC) used by RoCEv2 traffic via lossless Ethernet. Trade-offs between dedicated and shared storage networks including the effects of QoS on storage traffic and using PFC with ECN for RoCEv2 congestion management (RCM). Storage network designs using 100G/400G/800G Nexus Switches for RDMA, iSCSI, and NVMe over TCP traffic and operations using Nexus Dashboard. Best practices for all-flash and NVMe over fabrics (NVMe-oF) traffic.

### IPv6 - What Do you Mean There Isn't a Broadcast? - BRKIPV-1616
Speakers: Fish Fishburne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098333738001dTUb
Super new to IPv6? Trying to wrap your head around the basics, like how this all works without using broadcast and what the heck that "solicited-node multicast" thing is? If this describes you and your current knowledge of IPv6, and you want to try to "put the puzzle pieces together," this session is definitely for you. This session dives into all this by bringing to life Fish's very popular seven-part blog series, "Understanding IPv6". By the end of this session, you will be able to better "see" how the underlying puzzle pieces fit together in order for two IPv6 addresses in the same subnet to be able to "talk" with each other without ARP.

### IPv6 Groove: Get By with a Little Help from My Friends! - CISCOU-1038
Speakers: Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098401802001davj
Join us for a 30-minute journey through the world of IPv6, set to the upbeat rhythm of The Beatles' classic, "HELP!" Discover how IPv6, the essential upgrade from IPv4, is like the friend you call on in times of need addressing space exhaustion and enhancing network capabilities. We'll break down the core concepts of IPv6, such as its expanded address space, improved routing, and built-in security, using relatable analogies and a splash of musical flair. Whether you're a network pro or just curious, this session promises to educate and entertain, showcasing how IPv6 is the helping hand for the digital age.

### IPv6 Networking in a Cloud Native World - BRKIPV-2186
Speakers: Josh Halley (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098334091001dqHo
Learn the best practices involved in optimising, scaling and maintaining IPv6 deployments in your micro services based environments, from on-prem to the cloud. This session will provide an overview of the key differences and nuances involved in IPv6 dual stack and single stack deployments, and how the environments can be best optimised to ensure are reliable and observable end-to-end architecture.

### IPv6 Security in the Local Area with First Hop Security - BRKENT-3002
Speakers: Eric Vyncke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098311603001d7G3
A big difference in the security between IPv4 and IPv6 are the layer-2/layer-3 interactions, as DHCP is optional in IPv6 and ARP is replaced by Neighbor Discovery Protocol (NDP). Legacy IPv4 attacks such as ARP or DHCP spoofing have their equivalent in IPv6. Cisco has developed techniques for many years to secure this interaction in the local area (WLAN, LAN, SD-WAN access, Meraki, ACI, etc). This session explains the attacks and how Cisco can help protect your networks. A good knowledge of IPv6 is required, especially NDP.

### IPv6-Enabled Wi-Fi Access: Design and Deployment Strategies - BRKEWN-2834
Speakers: Vinay Saini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098321228001dKNq
As networks transition to IPv6 and shift their services, careful planning, evaluation of services, and migration procedures are essential. Wi-Fi is the predominant access medium for a diverse range of client devices. Therefore it is crucial to design, configure, and comprehend the features and traffic patterns for both dual-stack and pure IPv6 Wi-Fi scenarios. This session focuses on understanding IPv6 communication flows and the various features of the Catalyst WLAN controller with IPv6. It will also discuss common design scenarios for Data and Guest IPv6 wireless, considering different client mixes including Apple iOS, Windows, and Android devices. Additionally, the session will explore IPv6 wireless in conjunction with Cisco SD-Access.

### IPv6:: It's Happening! - BRKIPV-2191
Speakers: Nathan Sherrard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098334451001dyBR
IPv6 has had a long and winding history, with many organizations ignoring it. Yet in recent years its use has exploded, and we are now at a point where everyone needs to take it seriously and get ready for an IPv6-only future. If you're looking at the steps toward enabling IPv6, and are wondering where and how to start, this is the session for you. We will look at recent adoption trends and government mandates that are forcing the issue, do a walkthrough on the protocol itself, and finally explore some best practices around addressing plans and transition technologies. This session is targeted for enterprise, commercial, and public sector customers who are only just beginning their IPv6 adoption. We will not be discussing issues relating to service provider and mobile network providers. No IPv6 knowledge is required to attend, though basic familiarity with IPv4 networking is assumed. If you attended the TECIPV Technical Seminars, you do not need to attend this session.

### ISE APIs in Practice - Better Endpoint Profiling with Network Packet Analyzers - DEVNET-2292
Speakers: Taylor Cook (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098442122001d8iz
Cisco ISE has long supported integrations with 3rd party systems to ingest additional contextual data for endpoints to enhance Network Access Control policy decisions. These integrations can be built using either ISE's Platform Exchange Grid (pxGrid) or the growing library of ISE OpenAPIs. This session will provide an overview of an ISE integration built using open-source packet analyzers to inspect network traffic and gain additional context for profiling endpoint devices. You will receive an overview of ISE APIs and existing publicly available toolsets, as well as learn how to use analyze live traffic across various protocols to learn more about devices on the network. This session will then showcase how to combine information learned from traffic analysis with the ISE platform to improve network policies. Participants are encouraged, but not required, to have a basic understanding of Python, REST APIs, Wireshark, and network packet structure (OSI model).

### ISE Your Meraki Network with Group Based Adaptive Policy - BRKSEC-2100
Speakers: Alex Burger (Cisco), Thomas Howard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098366755001dNwj
Learn the latest about how you can better protect your network with the latest developments in software-defined segmentation capabilities from Cisco Identity Services Engine (ISE) and your Cisco Meraki network. Meraki wired and wireless devices have had Adaptive Policy capabilities for several years but it was difficult to synchronize with the TrustSec/Software Defined Access (SDA) tags and security group ACLs defined in ISE until now. We will show you how to configure your various Meraki network devices with Adaptive Policy, synchronize the TrustSec Matrix in ISE to the Meraki Dashboard, and authenticate your Meraki networks with ISE.

### Identity Intelligence Demystified - BRKSEC-2162
Speakers: Aaron Woland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098368969001dh34
"Why hack in when I can log in?" The market is abuzz with the talk of Cisco Identity Intelligence (CII), which comes to Cisco via the acquisition of Oort. What is identity security all about? What types of attacks and risks are we seeing in the wild? What we see in the real world has shown us that organizations have more than one Identity Providers (IdP) like Okta, Micrsoft EntraID and Duo SSO, but the security team isn't getting a complete or holistic view across the different IdPs. Come join Distinguished Engineer, Aaron Woland, as he talks all about identity threats and Cisco Identity Intelligence. How it is part of Cisco XDR and Duo Security, integrations, how it relates to the Identity Services Engine (ISE) and most importantly how to improve your Security Posture by getting a hold of the identity related threats.

### If You Don't Have a Security Reference Architecture, You Must Get One! - BRKSEC-1240
Speakers: Jerry Lin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098362495001d5zT
This breakout session will explain Cisco's latest security reference architecture covering the most common solutions that customers are deploying. Solutions such as Zero Trust, Secure Access Service Edge(SASE), Compliance, Security Operations with eXtended Detection & Response(XDR), Vulnerability Management, third party non-Cisco integrations, and others will be explained in terms of customer use cases. Demos of these covered solutions will be shown to highlight each outcome. Attendees should walk away from this session understanding how the Cisco Security Reference Architecture can help them or even identify any potential gaps in their existing environment, even if they have a mixed vendor environment today.

### Impact of AI Traffic in Transport Networks - BRKSPG-1180
Speakers: Virginia Teixeira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161412588001Nf2D
Artificial Intelligence (AI) is set to revolutionize every industry and the way users interact with the digital world. It's still early phases of AI adoption and still unclear what are the deployment models and AI technics that will become more prevalent. However, it's already apparent that AI traffic patterns are different from traditional internet traffic and that the use of AI frameworks such as RAG (Retrieval-Augmented Generation), grounding, AI agents and AI distribution to the edge, will have an impact on transport network design considerations. This session includes an analysis of the AI traffic characteristics for a set of AI use cases, and their impact on WAN and DCI design requirements.

### Implementing Customer Interaction Automation Using Webex Connect - BRKCOL-2956
Speakers: Gavin Shurmer (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098285756001ds1j
IT is at the heart of all digital transformation projects that aim to deliver smarter, richer customer interactions but there is constant pressure to speed up innovation to support the requirements from the broader business. As a consequence, developers are looking for quick and easy-to-use communications APIs and tools that also reduce technical complexity. In this session, learn about our CPaaS platform, Webex Connect. Having a single, central communications platform that combines APIs and low code tools with a high-performance execution engine, unifies all interactions to support the customer conversation in one place. In this session, we will focus on hands on demonstrations of three areas - integrating with enterprise systems, tools for productivity, and conversational automation on multiple channels - to enable you to orchestrate and automate customer journeys quickly and easily.

### Implementing OAuth 2.0 Authorization for Webex Integrations - DEVNET-2675
Speakers: Joe Zanini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098447548001diJd
OAuth is a powerful way to allow users to grant permission over their accounts to third parties. Join the Webex Developer Evangelism team for a walk-through of how to create an OAuth flow so your Webex Integrations users can authorize your app to run on their accounts or simply authenticate with Login with Webex.

### Implementing Segmentation in Industrial Networks - BRKIOT-2882
Speakers: Andrew McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098332288001dYK9
Securing industrial operations is top of mind, but the implementation can be challenging. The operations team often lacks the cybersecurity expertise to manage the network, and there is a concern that the IT team will take actions that reduce operational uptime. The purpose of this session is to understand Cisco's phased approach to securing the industrial network. The Cisco Industrial Security solution follows the zones and conduits model outlined by IEC 62443, and provides the tools necessary for both IT and OT to work in collaboration to secure the Industrial network.

### Improving Contact Center Operations with Cisco Workforce Optimization - BRKCCT-2854
Speakers: Tarig Farid (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098276532001dALt
The most valuable asset in a customer service organization or contact center is your workforce. Hiring, training, upskilling, and retaining agents are activities critical to your success. Also, gathering full insights on 100% of interactions in your contact center can help you learn about your agents and customers, and identify what needs to be done to resolve & improve your services & operations. Therefore, Workforce Optimization strategies should be front and center to your business goals. This intermediate level session will cover the business value of Cisco Workforce Optimization and deep dive on the architecture and integration options with Webex Contact Center & Webex Contact Center Enterprise. This will be categorized into three main sections: Agent Experience, Supervisor Experience & Business Analyst Experience.

### Incident Response With Cisco XDR: How To Level Up Your SOC Using Both Guided and Automated Response - BRKSEC-2502
Speakers: Sander Zumbrink (HOB IT SERVICES BV), Christopher Van Der Made (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098375782001dmjJ
Ever wondered what to do when a security incident strikes? Discover the secrets to effective incident response with SANS PICERL and Cisco XDR! In this session, dive into actionable insights as we unravel a real-world attack through an exciting demo, guided by an expert guest speaker. We'll explore the technical workings of Cisco XDR's out-of-the-box Response Playbook, including how to use, customize, and automate these processes. After the session, participants will get access to the automation workflows demonstrated, ready for real-world application. This session is perfect for incident responders, security analysts, SOC managers, and anyone eager to enhance their security and automation skills. Don't miss this opportunity to transform your incident response strategy!

### Inclusion in Cybersecurity Panel - IF-1020
Speakers: Shannon Wellington (Cisco Systems, Inc.), Sue Lin (Cisco Systems, Inc.), Nancy Cam-Winget (Cisco), Oxana Sannikova (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098452899001d5Np
The ISC2 Cybersecurity Workforce Study 2024 reports the continued shortage of over 4 million Cybersecurity professionals worldwide, highlighting that inclusion in Cybersecurity recruitment will help us close this talent gap. Support from organizations like ISC2 and ENISA are creating programs to help both close the skills gap and promote inclusion within the Cybersecurity workforce. Please join this Cisco panel of experts in Cybersecurity, with varying roles and levels of experience, for a discussion on their journey in Cybersecurity, and perspectives on how we can close the talent gap.

### Increase Scale and Efficiency with Simplified Networks - PSOSP-1866
Speakers: Yoav Schreiber (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098472913001d0Gg
Discover how simplified architecture with autonomous networking can scale your business and deliver exceptional digital experiences. We'll discuss how optimization and convergence can transform network economics and provide assured connectivity for AI and provider workloads. You'll learn to simplify your network by converging optical and IP layers for DCI, metro, and long-haul transport. Plus, see how service optimization with segment routing helps you generate new revenue and differentiate services across the network. And, explore how intelligent metro edge can monetize network performance, thanks to digital experience assurance with real-time telemetry and AI-enabled operations.

### Industrial Wireless for Manufacturing - New Solution - BRKIOT-2555
Speakers: Paul Didier (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161408464001Njrk
Industrial wireless is no longer just an extension of enterprise Wi-Fi. Industrial wireless supports a broad range of use cases; AGVs/AMRs, process skids, AR/VR assistance, location services, and SW downloads for products. Industrial wireless choices are also growing; WiFi 6/6E, 5G/Private5G and Cisco's Ultra-Reliable Wireless Backhaul (URWB). This session will explore the wireless options, review their pros/cons and provide key design considerations based on actual testing with industrial applications all to help manufacturers meet demanding mobility requirements. The session will provide architectural recommendations based on testing and customer examples that support plantwide Wi-Fi and Cisco URWB for mobile users and industrial assets. All of which are available in Cisco's new Industrial Wireless for Manufacturing Cisco Validated Design (CVD).

### Industry Standard Streaming Telemetry with Cisco NX-OS - DEVNET-2235
Speakers: Gerard Sheehan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098441409001dIZl
Come and learn about the latest way to monitor the health of devices and activity in your network: Streaming Telemetry. See how simple it is to deploy in NX-OS and integrate with Open Source solutions to consume and visualize the data. Also watch how anomalies can generate alerts, and how the data can be integrated with messaging buses and AI/ML applications!!

### Infrastructure as Code for NXOS and NDFC with Ansible - BRKDCN-2946
Speakers: Mike Wiebe (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098295117001d3gI
In this session, we'll explore how Ansible and NXOS can be used to provide various automation and orchestration capabilities to operate your VXLAN EVPN data center fabric using Infrastructure of Code (IaC) principles. Ansible is widely adopted and used across the industry as a foundation for IaC, which uses established best practices for software development and applies them to your network. Network configuration is stored in a structured manner using a source control management system like GitLab and becomes the source of truth for making network changes. In the session, we will walk through getting started with a development environment for Ansible and the Ansible NXOS collection. Next, we will define an Ansible playbook structure using available NXOS modules. We will then show you how you can store your Ansible playbook(s) in GitLab as a source of truth and build a CI/CD pipeline to push network configuration changes. The focus will then transition into how you use the same Ansible environment and IaC concepts to manage your VXLAN EVPN fabric using Nexus Dashboard Fabric Controller (NDFC) with the VXLAN as Code Ansible collection which provides a data model driven abstraction. NDFC is the management controller for all NXOS-enabled deployments and offers a robust northbound-REST API for Ansible modules to leverage. Finally, we will build upon our GitLab CI/CD pipeline to make network changes to our NDFC-managed fabric.

### Infrastructure as Code for Network Operations: An Executive's Guide for Achieving 100% Change Success - ITLGEN-1513
Speakers: Jesse Reed (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098459718001drxT
To stay competitive, businesses need rapid transformation without risking service disruption. Humans are the leading cause of network-related service interruptions. Infrastructure as Code (IaC), using open-source principles and Cisco best practices, can modernize and automate network operations. Many teams already use IaC for cloud, but network operations still rely on legacy methods. This session will explore achieving change five times faster by integrating IaC and AI into your network operations. Learn how Cisco has implemented IaC, and digitized the continual knowledge of 20k Cisco engineers to ensure 100% change success. All IT leaders are encouraged to attend.

### Infrastructure as Code for Networks - DEVNET-2562
Speakers: Snezana Mitrovic (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098445740001dlKI
To stay competitive, businesses need rapid transformation without risking service disruption. Humans are the leading cause of network-related service interruptions. Infrastructure as Code (IaC), using open source principles integrated with the expertise of thousands of Cisco engineers, can modernize and automate network operations.

### Ingest Telemetry and KPI at Scale: Hyperscaler and Service Providers - CSSSEC-2249
Speakers: Ashish Binjola (Cisco Systems, Inc.), SYED AHSAN (Amazon)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098421189001dgwU
Participants will learn directly from Principal/engineers with service providers how they build telemetry and ingest data across multiple devices (firewalls, firepower, other devices) using built-in data dog services. The data is scraped, filtered, and can be published to Splunk or 3rd party tools like Prometheus or any other time series database. Participants will also learn how to turn this data into actionable events, build automated operational playbooks etc.

### Ingesting Network Telemetry Events and Alerts into the Splunk Data platform - DEVNET-1765
Speakers: Steven Barth (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098435617001dJ9x
The addition of Splunk into the Cisco ecosystem brings new opportunities for analyzing and correlating network telemetry and events together with data from other IT systems in one unified data platform. This session will show you various methods of ingesting data from IOS XE and IOS XR routing and switching platforms into Splunk, such as using syslog, model driven telemetry (MDT) and utilizing network-related events and alerts from Crosswork Network Controller and Crosswork Element Management Function. You will learn using examples to configure collectors and use relevant Crosswork APIs as a data source and get to know the Splunk HTTP Event Collector (HEC) to easily feed metrics and events into the platform.

### Innovation Unleashed: AI's Transformative Role in Enabling Innovation, Operational Efficiency, and Trust - AIHUB-1148
Speakers: Luca Antiga (Lightning AI), Amy Gerrie (Cisco Systems, Inc.), Jacob Woodfield (Securiti)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161391637001NXot
Join us for an engaging panel discussion with Cisco Investments portfolio companies Scale, Lightning AI, and Securiti AI, as we delve into the interplay between scalability, innovation, and security in AI. Discover how these groundbreaking solutions are driving transformative change, reshaping the future of enterprise operations, and unlocking new possibilities across industries. Scale AI sets the stage by providing high-quality data annotation and labeling, forming the essential backbone for developing precise and effective AI models. Leveraging these foundations, Lightning AI demonstrates how AI can be seamlessly integrated into workflows. By focusing on the efficient development, scaling, and deployment of AI applications, Lightning AI transforms foundational potential into powerful operational solutions that significantly enhance efficiency and innovation. Securiti AI addresses the critical aspect of trust in AI adoption. By ensuring data privacy, security, and compliance, Securiti AI ensures that as organizations deploy AI, they do so with confidence, safeguarding sensitive information and meeting regulatory standards. Together, these companies illustrate the comprehensive impact of AI, highlighting a continuum from foundational data practices to operational deployment and the essential management of trust and security.

### Innovation through Inclusion: A Collaborative Frontier - IF-1098
Speakers: Priyanka Shiravadekar (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098453619001dNTP
With the increasing competition in the market across all technology domains, there is a constant requirement to Innovate to stand out. Organisations are striving to foster innovation by creating an environment that nurtures Innovation. This session will bring industry insights and best practices gathered from industry experts with experience working for large diverse organisations. Addressing the pressing need to be innovative and inclusion to create something novel. The session talks about how diversity is pivotal for sustaining competition in the business environment. This session will explore the business case for inclusion, strategies to foster an innovative workforce, and real-world insights from leaders across different sectors by sharing real- world examples and success stories. The participants will learn about the impact Cisco is creating with the inclusive communities within Cisco and how these communities are encouraging the diverse profiles in the fields of Science, Technology, Engineering and Mathematics. The session will encourage participants to think about their personal growth and advocating for an inclusive work environment for all.

### Innovations in Silicon and Software: Defining the Next Generation of Enterprise Technology - BRKARC-2093
Speakers: Dave Zacks (Cisco), Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098273979001dtOw
Ever wonder what's "under the covers" in Cisco platform architecture? Come to this session to explore what's next in Cisco's Enterprise product portfolio, exploring the latest advances in silicon hardware, modular software, and end-to-end solutions. This session will examine the current state-of-the-art in ASIC, platform, and software design, and examine the many use cases to which Cisco networking and security technologies are being applied. Presenting this session is the dynamic duo of Peter Jones and Dave Zacks, both Cisco Distinguished Engineers as well as Cisco Live Distinguished speakers. If you are interested in what makes Cisco products and platforms "tick," this is the session for you!

### Innovative Strategies for Securing and Simplifying IT Infrastructure Management - PAROPS-1629
Speakers: Daniel Cecalacean (Opengear)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098465103001dn7b
In today's increasingly complex IT environments, compliance, security, and AI are driving the need for secure and simplified infrastructure management. This requires a platform built to streamline oversight, enhance protection, and enable seamless collaboration. Join Daniel Cecalacean as he shares how Opengear delivers immediate value by helping overcome compliance and security hurdles through physical segmentation and unified visibility -- from physical infrastructure to virtual network functions. This session offers valuable insights into how Opengear redefines and simplifies IT infrastructure management: Secure remote access and visibility across diverse infrastructure layers The role of Smart Out of Band in enabling flexible options for day-one provisioning while enhancing compliance and security by limiting lateral access Accelerated time-to-value through automation strategies that reduce complexity, streamline operations and improve monitoring and reporting Don't miss this opportunity to explore how Opengear solutions can transform your infrastructure management strategy. Join us for a solutions-driven discussion packed with real-world examples and actionable takeaways.

### Inside Cisco's Incubation Engine: From Bold Bets to Enterprise Impact - CENETI-1280
Speakers: Vijoy Pandey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227080667001JwE9
In today's rapidly evolving technology landscape, enterprises must master the art of incubating emerging technologies from concept to scale. Through Outshift's journey as Cisco's incubation engine, we've developed a proven framework for transforming early-stage ideas in AI, quantum, and next-gen infrastructure into enterprise-ready solutions. You'll leave this session understanding: - How Outshift's five-phase incubation model (ideate, build, launch, land, scale) accelerates the path from concept to productInside Cisco's Incubation Engine: From Bold Bets to Enterprise Impact - Why product-company fit and alignment with go-to-market strengths are critical for successful enterprise incubation - How to balance startup-speed experimentation with enterprise requirements, illustrated through real examples from Outshift's portfolio The session features practical case studies from Outshift's incubation experiences in cloud security and AI, including key learnings from both successful graduates and pivoted projects. Discover how we validate early bets in quantum networking and agentic AI while maintaining enterprise standards. Recommended for technology leaders interested in building effective incubation programs within large organizations.

### Integrate and Automate Cisco Compute Hyperconverged with Nutanix - DEVNET-1144
Speakers: Jens Depuydt (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098429416001d2QC
Get ready to kickstart your journey into integration and automation with Cisco Compute Hyperconverged and Nutanix. This session will introduce you to the powerful REST API and SDK for both Nutanix and Cisco Intersight. You'll learn how to leverage these tools in practical scenarios, integrating them seamlessly using Python or Ansible. For each of the topics, there will be practical examples and a demo. This session is all you need to get started with successfully integrating and improve the monitoring capabilities of Cisco HCI with Nutanix and provides all the info you need to make this a success.

### Integrating ThousandEyes with Splunk Observability Cloud via OpenTelemetry - DEVNET-1213
Speakers: Lukasz Ciukaj (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098430526001dtWz
Discover how to enhance your observability strategy by integrating ThousandEyes with Splunk Observability Cloud using OpenTelemetry. In this session, we'll demonstrate how to send ThousandEyes test results in OpenTelemetry format to Splunk Observability Cloud and create insightful dashboards. Learn best practices for seamless integration, visualize network performance data, and gain actionable insights to proactively manage your IT environment. Additionally, explore how to monitor your applications both from the inside using Splunk Observability Cloud and from the outside using ThousandEyes, ensuring comprehensive visibility and performance optimization. Join us to unlock the full potential of your observability tools and drive operational excellence.

### Intelligent Security and Segmentation with Common Policy and ISE - PSOENT-1861
Speakers: Bill Rubino (Cisco Systems, Inc.), Jonothan Eaves (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098468694001dXNX
Complex multicloud environments often suffer from connectivity issues, security vulnerabilities, lack of visibility, and inefficient manual processes. Join this session to learn how to put a common network policy in place via SDA, ISE, and Cisco network management platforms. These solutions streamline operations, ultimately leading to improved performance, reduced risks, and greater operational efficiency.

### Interactive Network Docs with Jupyter Notebooks and Netmiko - CISCOU-1042
Speakers: Jason Belk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098403254001du74
Learn how to get up and running with Jupyter Notebooks within a network automation context. Jupyter Notebooks are interactive web pages that you can run Python code and visualize the output. This popular data science library can be very helpful for writing Markdown Documentation or just exploring your learning journey with Python code. Join this session to see live demos of the framework and how to get started!

### Intersight Fundamentals: An Engineer's Journey to Proficiency - BRKCLD-1666
Speakers: Justin Blinn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098277266001dIKN
The Cisco Intersight platform offers a cloud operating model which enables faster delivery, streamlined operations, and ongoing optimization of infrastructure. This platform manages on-premises Cisco Unified Computing System (UCS), hyperconverged (HCI) clusters and third-party infrastructure. In this fundamentals session, participants will gain an understanding of the Intersight platform's components and capabilities, how it securely interfaces to its platform targets, and the business value outcomes it can provide. Real-world use cases of the Intersight platform will be discussed and demonstrated, making this an interactive session. By the end of the session, participants will have an understanding of the Intersight architecture, the components of the operating model along with use cases and scenarios that can be addressed with Intersight operations.

### Intersight Managed Mode (IMM) Architecture Deep Dive - BRKCOM-3280
Speakers: Vincent Esposito (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098288107001dioW
Have you ever wondered how Intersight Managed Mode works under the cover? What happens when a new hardware gets discovered, or when a Server Profile is deployed to a server? This session will look into the details of how this new management paradigm works, to help you better understand, manage and troubleshoot your own infrastructure.

### Intro to Cisco Cybersecurity Operations - CISCOU-1041
Speakers: Alessio Valdez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098402888001df56
Are you a Network engineer looking to learn about Cybersecurity? In this session, we will be covering the fundamentals of Cisco Cybersecurity Operations, security concepts, and common network and applications attacks as well as the type of data required to investigate security incidents. We will also go over the essential skills, technologies and concepts needed to become a member of a Security Operations Center (SOC) team.

### Introduction to ACI - BRKDCN-1601
Speakers: Chris Merkel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098289414001dHmk
Not sure what Cisco ACI is? Looking for a starter session to understand the architecture, nomenclature and capabilities of ACI? How it can transform your data center? Join this session to get a crash course in ACI!

### Introduction to AI Infrastructure - CISCOU-1047
Speakers: Chris Gascoigne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098405045001dxfB
The AI hype is real today and there is lots of discussion around AI infrastructure speeds and feeds, but have you ever wondered "Why? What is it about AI workloads that needs high powered GPUs, 400/800G networking and scale-up interconnects?" If so, join this session to learn about the fundamentals of AI training and inferencing and why (and in what circumstances) they have different infrastructure requirements than traditional applications.

### Introduction to Campus Network Design and Multilayer Architectures - BRKENS-1500
Speakers: Jakub Matela (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098299076001d5xr
Understanding how to design a campus network that is scalable, reliable, and aligned with modern needs is a critical skill for today's network professionals. In this session, we'll introduce the core concepts of multilayer campus architecture and show you how to design and plan your network using the best practices outlined in Cisco Validated Designs (CVD). Whether you're working with small or large networks, this session will guide you through: - The key building blocks of a multilayer campus network. - How to choose the right design model for your needs. - Practical tips to get the most from CVD recommendations. This session is perfect for those with a solid understanding of LAN switching and routing basics (CCNA-level) and provides a strong foundation for exploring more advanced topics. Start here to learn the fundamentals, gain practical design insights, and prepare to optimize your campus networks for the future For those ready to take the next step, BRKENS-2500: Advanced Campus Network Design: Multilayer Architectures and Next-Gen Protocols, builds on this knowledge to dive deeper into advanced protocols, design strategies, and next-gen integrations.

### Introduction to Cilium - The De-Facto Networking and Security Platform for Kubernetes - BRKCLD-2696
Speakers: Raphaël Pinson (Cisco Systems, Inc.), Nico Vibert (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098278606001dYa6
More than 60% of enterprises have adopted Kubernetes, and the Cloud Native Computing Foundation (CNCF) annual survey shows that the adoption rates of Kubernetes have increased to 96%. While networking is a fundamental aspect of Kubernetes, it remains an intimidating topic for many engineers, especially those in the networking industry. In this session, you will learn that Kubernetes networking and the de-facto networking platform Cilium don't need to be daunting subjects after all! This session will provide an introduction to the core Kubernetes networking requirements and how Cilium addresses these use cases. Expect an demo-packed and inclusive session where newcomers and experienced network engineers alike will improve their cloud native networking knowledge and understand the benefits of using Cilium and eBPF for networking, observability and security. Finally, the session will also provide tips on some of the core topics and domains covered in the recently-launched Cilium Certified Associate (CCA) certification.

### Introduction to Deep Learning for Networking - AIHUB-1846
Speakers: August Martens (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161392200001NsIH
With the rapid advancements in artificial intelligence, understanding deep learning is essential for modern network management. This AI Hub session provides a concise overview of deep learning principles and demonstrates a practical application in network management, focusing on anomaly detection. Participants will learn the basics of neural network architectures and parameters, and see a live example of how deep learning can enhance network performance by identifying and mitigating anomalies. The session will highlight the use of TensorFlow and Keras, leveraging pre-trained models from leading open-source research. You'll leave this session with ideas to help you: Understand the core principles of deep learning Recognize how deep learning can be applied to network anomaly detection Explore practical tools and frameworks like TensorFlow and Keras No prior deep learning experience is required, but familiarity with basic networking concepts is recommended. Join us to get a foundational understanding of deep learning and see its potential in network management.

### Introduction to Infrastructure as Code for ACI using Ansible - BRKDCN-2606
Speakers: Rafael Muller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098290336001dSNC
Infrastructure as code (IaC) allows you to define via data structures, the configuration of your network. Ansible has become an industry standard automation tool used to manage large scale compute stacks and network devices. Cisco Application Centric Infrastructure (ACI) is Cisco's premier API-based data center network architecture with 100% API coverage. The combination of these, allows you to operationalize your network with security , accuracy and speed . In this session we will cover: Best practices to setup Ansible for ACI operations How best to organize your data structures to allow for growth and reaching infrastructure as code state Pitfalls to avoid from lessons learned working with Ansible and large data-sets

### Introduction to Infrastructure as Code for ACI using Terraform - BRKDCN-2607
Speakers: Thomas Renzy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098290528001dyFg
Infrastructure as code (IaC) allows you to define via data structures, the configuration of your network. Terraform has become a standard in the cloud to manage large scale deployments of many different type of resources. Cisco Application Centric Infrastructure (ACI) is Cisco's premier API-based data center network architecture with 100% API coverage. With the Terraform and ACI automation capabilities in Terraform you can configure ACI easily in a fashion that can lead to secure, accurate and fast configuration changes. In this session we will cover: Best practices to setup Terraform for ACI operations Understand the different ACI specific Terraform resources available Pitfalls to avoid from lessons learned working with Terraform and some of it's unique powerful toolsets.

### Introduction to NDFC: Simplifying Management of Your Data Center - BRKDCN-1619
Speakers: Richard Licon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098289780001de4i
Cisco Nexus Dashboard Fabric Controller (NDFC) formerly known as Data Center Network Manager (DCNM), is the network management platform for all NX-OS (Nexus switching)-enabled deployments, spanning LAN fabric and classic LAN architectures, IP fabric for media, and storage networking deployments for the Cisco Nexus-powered data center. This session will serve as an introduction to NDFC providing an overview of the product while highlighting the main features of the latest NDFC 12 release. NDFC 12 is an application that runs on top of Nexus Dashboard (ND). In this session, we will briefly look at Nexus Dashboard, NDFC installation, and various deployment options with ND. We will then move on to LAN fabric mode for VXLAN EVPN and classic LAN fabric. The focus will be on best practice template-based provisioning capabilities with built-in configuration compliance and the myriad deployment scenarios. We will also walk through Day 2 features like compute visibility using virtual machine manager (VMM) integration, the switch dashboard, and real-time topology search. No prior knowledge of NDFC is required.

### Introduction to SRv6 uSID Technology - BRKSPG-2203
Speakers: Jakub Horn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098388600001dksG
This session will provide an overview of the SRv6 uSID technology and use cases. The session will demonstrate application of SRv6 uSID building blocks on real use cases like layer 3 VPN, flexible algorithm, and traffic engineering.

### Introduction to Segment Routing - BRKSP-2551
Speakers: Michiel Koolen (Rijkswaterstaat NL), Alberto Donzelli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161411458001NJLT
This session offers an introduction to Segment Routing and its various use cases. Segment Routing, a modern routing paradigm, provides exceptional operational simplicity, scalability, and flexibility, making it the preferred technology for implementing IP transport networks across Service Providers and Enterprises. Participants will gain an understanding of the fundamental concepts behind Segment Routing for both MPLS and IPv6 forwarding planes. The session covers its extensive applicability, from Automated Protection to basic transport for VPN services to more advanced applications such as traffic engineering and Network Slicing. Additionally, the benefits of Segment Routing in the context of Software-Defined Networking (SDN) and Cloud Networking, will be explored. The session will also feature a customer testimonial from Public Sector in the Netherlands, Rijkswaterstaat (RWS), highlighting their experiences, motivations, and the benefits they have realised by fully embracing Segment Routing technology, including their end-to-end implementation of Segment Routing IPv6.

### Introduction to VXLAN: The Future Path of Your Data Center - BRKDCN-1621
Speakers: Richard Licon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098289956001dF8X
Learn more about VXLAN and delve deeper into it. This session will cover what VXLAN is, how it works and the problems it solves. The need for flexibility in the data center opens the door to network overlays. Several standards have been proposed and implemented to enable virtualized networks to be layered over a physical network. The data center network needs to be flexible enough to support workloads that can move from one host to another, and for new services to be deployed rapidly. VXLAN is one such technology that provides massively scalable virtual network overlays on top of existing IP infrastructures. This session will include 101s and packet walks as we cover the insides of VXLAN. No prior knowledge of VXLAN is required. A basic understanding of unicast and multicast routing protcol is needed, along with an understanding of MP BGP.

### Introduction to eBPF - DEVLIT-1545
Speakers: Adrian Iliesiu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098424435001dKaf
In this lightning talk we will discuss what is eBPF, how it came to be and why is an important technology for networkers. We will also cover typical use cases from basic security to building advanced service meshes.

### Introduction to eBPF! - BRKSEC-2169
Speakers: Liz Rice (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098369701001dCu8
eBPF is an industry-changing technology that is enabling a new generation of security, networking and observability tools. This session provides an in-depth exploration of its origins, rewards, and challenges, with live demos to give you concrete explanations of what eBPF is, and how it enables advanced, high performance capabilities. You'll leave this talk understanding why eBPF has been called "Superpowers for Linux!"

### It's Cats vs Rats Going Hybrid! Attack and Defense in the Cloud - BRKSEC-2485
Speakers: Hakan Nohre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098375432001dPCT
Cyber security is a cat and mouse game - a constant evolution of new ways to attack and defend. The cloud transformation may bring many benefits, such as reduced cost and increased agility, but it also increases the attack surface for determined adversaries. New technologies including - AI technologies - can be used by both sides. In this breakout, we will look at the new possibilities to attack and defend. The intended audience are Security and Networking Architects. Some understanding of cloud concepts such as IaaS and PaaS is expected.

### Keep Your Cisco Catalyst Wireless Network Healthy - Wireless Config Analyzer Express and Other Advanced Tools - BRKEWN-3006
Speakers: Javier Contreras (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161405861001NjeO
Hear it explained directly from the horse's mouth. Wireless config analyzer express (WCAE) is the evolution of the well-known WLCCA tool, now adapted to work on the cloud, supporting 9800/AireOS and offering multi-platform access. The tool will perform close to 500 total configuration checks, all coming from the collective experience and learning of worldwide Cisco Wireless Technical Assistance Center (TAC) and escalation teams, with a large list of RF analysis features developed for internal use, now in your hands.

### Keeping Up on Network Security with Cisco Secure Firewall - BRKSEC-2236
Speakers: Andrew Ossipov (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098371478001d15E
The network security death rumors are highly exaggerated, and Cisco Secure Firewall is the best proof of all. Whether you are an experienced Firepower aficionado, or someone who is open to trying something new, this session will get you the fix. From app security, to blazing-fast new hardware platforms, to maintaining visibility in the world of pervasive TLS encryption, there is something for everyone to get at least a little excited about.

### Knock, Knock. Who is There Behind your Firewall? - All About Identity on Cisco Secure Firewall - BRKSEC-2590
Speakers: Christopher Grabowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098376497001dK72
This session provides a comprehensive walkthrough of identity feature set of Cisco Secure Firewall. Participants will learn how to apply user and resource identities in the firewall policy obtained with available methods: SAML, RADIUS, LDAP, pxGrid, TS Agent, CSDAC, and more. Understand the flavours of user and resource object types along with active and passive authentication flows: captive portal, remote access VPN, 802.1x, Zero Trust Access and PassiveID. Familarity with Cisco Secure Firewall feature set is required.

### Kubernetes (K8s) Infrastructure Connectivity for ACI Network Designs for the Modern Data Center - BRKDCN-2663
Speakers: Camillo Rossi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098291654001dJvz
Kubernetes provides the capability to create micro-service-based applications that are flexible, scalable, and secure in the modern data center. Cisco Application Centric Infrastructure (ACI) can be integrated with a Kubernetes cluster using our native, open source, and free CNI plug-in: ACI CNI. In this session, we will explore the integration of ACI with ACI CNI and Cilium (no overlay with eBGP), focusing on the different capabilities of each architecture and concluding with a brief demo of the two integrations.

### Lab Up For Success With Cisco Modeling Labs - BRKCRT-2059
Speakers: Joe Clarke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098288862001d1ag
No matter what Cisco certification you're preparing for, you know you need to do more than just read the book to be successful. You need to practice. You can scour the internet looking for used gear, but when you get it, you still need the space to rack it, not to mention the power and cooling. Cisco Modeling Labs (CML) is a tool that provides you the virtual gear you need to practice for several Cisco certification exams with almost limitless topology possibilities. What's more, you can "plug" packet sniffers in with just a few clicks, introduce link problems, and even connect to physical kit you do have. In this session, we will explore how you can use CML to setup your own home labs. We'll dive into features such as traffic generation, packet capture, and external connectivity. Example topologies will be shared for a few scenarios to kick-start your studying and set you up for success.

### Leading Technical Teams in the Era of AI: Coaching as a Full Stack Observability Tool - IF-2093
Speakers: Anastasia Frolova (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098456801001dXuR
At the time when AI is taking over more and more tasks and there is a lot of uncertainty in the macro-environment it is really crucial to be able to create healthy team dynamics where people feel safe and heard. In this session, you will learn what influence on business the quality of interaction within the team has, what are the scientific processes behind and how to use coaching approach as a tool to create awareness and foster the culture of creativity and innovation. You will leave the session with ideas and practical tips on how to use coaching to get the required results via building individual and team growth mindset, and troubleshooting techniques that might be useful for creating the desired team dynamics.

### Leading the Way to a More Secure, Multicloud World with Cisco Security - PSOSEC-1623
Speakers: Chris Consolo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098472370001dKb7
Security complexity continues to be one of the most common challenges for organizations as they build and expand their multicloud footprint. Learn how you can leverage the power of Cisco Multicloud Defense and Cisco Firewall, as part of the Cisco Security Cloud Control platform, to achieve unified visibility across cloud environments through centralized, cloud management, reduce security complexity through automation and orchestration of enforcement points, and streamline operations with simplified policy creation.

### Learn Network Automation with Github Copilot - BRKOPS-1726
Speakers: Gowtham Tamilselvan (Cisco), Praveen Poojary (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098347633001dYXh
Generative AI-powered tools are rapidly transforming productivity, with research predicting an AI-driven boost to global GDP by over $1.5 trillion. GitHub Copilot, the world's leading AI developer tool, has shown that nearly 30% of its code suggestions are accepted by users, significantly enhancing efficiency and productivity. In this session, discover how to leverage GitHub Copilot to write Python code and automate essential day-2 network operational tasks for Cisco Enterprise Networks. Participants will also learn to utilize GitHub CI Pipeline automation to create procedural workflows that automate a series of tasks to solve more complex use-cases. Participants will gain an understanding on Github Copilot, network automation with Python, DevOps and CI/CD principles. Are you ready to become an automation engineer with your trusty Copilot assistant?

### Learnings Behind the Biggest Network Outages: Executive Insights for the AI Era - ITLGEN-1514
Speakers: Angelique Medina (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098459900001dAcq
Organizations rely on a complex web of networks, services, and internal environments to deliver both the customer and employee digital experiences that are crucial to their success. Outages are an inevitable part of that, and it's how you identify, mitigate and resolve the problem that sets you apart. Understanding the entire delivery chain and having independent visibility across all connecting components is crucial. This session will use real-life examples to demonstrate how analysis at scale can assist in identifying where the issue is occurring and who is accountable for its resolution, how and where that impacts the business and the value of that data set in assuring business continuity moving forward.

### Lessons Learned: Zero Trust Implementation for "Smart" Architectures - CISCOU-2045
Speakers: Patrick Lloyd (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098410747001d2Kp
The pursuit of micro segmentation is enough to keep most CISO's up at night. Knowing that devices with significant security vulnerabilities need to exist on the network further influences the need to segment the network, and protect critical assets. Utilizing the Zero Trust Model published in "Zero Trust Architecture" this session covers lessons learned in the planning, design, and implementation of 'smart' technologies, buildings, and cities. Use cases such as connecting HVAC systems, MRI machines, and manufacturing technology to the network are used as illustrative examples. Focus for this presentation is on easing complexity, maintaining security of the network, easing enforcement, and realizing ROI quicker

### Let Cisco Catalyst Center be your Guide to a Zero-Trust Workplace - BRKOPS-2683
Speakers: Rojda Cicek (Cisco Systems, Inc.), Felix Meixner (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098356321001d4zm
SecOps teams today are hyper-aware of the threats that face their network as the landscape becomes more complex and difficult to predict. Cisco's Zero-Trust for workplace solution provides a security architecture based on key pillars of endpoint visibility, network segmentation and continuous trust monitoring. Cisco Catalyst Center (formerly Cisco DNA Center) provides critical insights into endpoint type and traffic patterns, automated management of configuration policies and continuous trust assessment provide NetOps and SecOps teams immense value. This session targets everyone interested to raise the level of security and trust in the campus network in a simplified and automated way, and explains the value of multiple product capabilities in Cisco Catalyst Center. The session helps to explore the various paths that you can take to achieve a Zero-Trust Workplace. Explore what a system could look like with various network connectivity and services like Catalyst 9000 (C9K), Identity Services Engine (ISE) and SD-Access. Discover your optimal path based on where your network is currently and explore the benefits of each added step on your Zero-Trust journey. For a more detailed coverage of the topic, we recommend visiting the four hour technical seminar TECOPS-2002 on Monday.

### Let's Get Physical - with Security! - PSOENT-1865
Speakers: Shashank Reddy Nalla (Cisco Systems, Inc.), Lesly Anzo (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098469432001dh7R
In our increasingly interconnected world, the convergence of physical and network security is crucial for safeguarding sensitive information and infrastructure. The role of physical security is growing more and more important in a world driven by digital technology. In this session, we'll examine real-world case studies illustrating how physical security breaches can lead to vulnerabilities in network security, then get into the latest innovations in Cisco Meraki cameras and sensors. Don't miss out on this session to see our newest cameras!

### Leveraging AI in Cybersecurity for Government - PSOIND-1780
Speakers: Matthew Dietz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098469976001d4UC
As global threats become increasingly sophisticated, government organizations must stay ahead with robust, innovative solutions aligned with zero trust principles. This session will explore how advanced AI-driven analytics and machine learning capabilities enhance visibility, threat detection, automate responses, and optimize network performance, providing government agencies with the tools they need to maintain situational awareness and respond swiftly to emerging threats. We will also delve into a comprehensive cybersecurity suite designed to protect critical infrastructure, secure communications, and ensure data integrity aligned with zero trust mandates. Learn how end-to-end security frameworks can safeguard your operations against the most sophisticated cyber threats. With strategic insights into existing and emerging capabilities, discover how continuous innovation and strategic partnerships are empowering government entities to meet their mission-critical needs.

### Leveraging Cisco Security APIs for threat hunting based on automated alerting and intel-driven detections - BRKDEV-3098
Speakers: Oxana Sannikova (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098298897002dPG5
This session is intended to help organizations in investigating computer security incidents by providing practical guidance on performing threat hunting activities using Application Programmable Interfaces of respective Cisco Security solutions. Specifically, the session describes practical examples of how to automate alerting and operationalize threat intelligence to initiate threat hunting and provides advice regarding different capabilities and features to automate forensics gathering. Its purpose is to inform attendees of various technologies and potential ways of using them in performing threat hunting and incident response activities.

### Leveraging Cloud Native Tools for AI Connectivity - DEVNET-2609
Speakers: Shannon McFarland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098446098001dUZJ
Dive into the complexities of AI infrastructure connectivity with cutting-edge cloud native solutions in this dynamic session. We'll tackle real-world challenges when integrating AI across hybrid cloud environments and demonstrate how to streamline operations using advanced open-source tools. Explore a use case where GenAI and its dependencies operate seamlessly within a Cloud Native setup. Learn how to harness the full potential of Cloud Native open source projects like Cilium, Istio Service Mesh, Kubernetes networking, and other open-source AI tools to optimize your AI connectivity for peak performance.

### Leveraging Digital Twin Technology for Advanced Network Management with Cisco Catalyst Center - BRKOPS-2442
Speakers: Christopher Beye (Cisco), Abhay Kaviya (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098352348001dSd4
In the evolving landscape of network management, the integration of Digital Twin technology offers unparalleled capabilities for monitoring, managing, and optimizing network infrastructures. With increasing network complexity and the severe business impact of outages, testing and simulating network configuration deployments has become essential. This session will explore how to create and utilize a computer-simulated model, or Digital Twin, that replicates your network's operating environment, devices, configurations, and traffic flows using Cisco Catalyst Center and Cisco Modeling Labs (CML). Key points include: Introduction to Digital Twin Technology: Understanding the fundamentals and benefits of Digital Twin in network management. Cisco Catalyst Center Integration: How to harness the power of Cisco Catalyst Center to build and manage a Digital Twin of your network. Creating a Network Digital Twin with CML: Step-by-step process to simulate your network using Cisco Modeling Labs. Simulating Cisco and Non-Cisco Networks: Efficient simulation leveraging real Cisco images to create a reliable virtual copy of your network. Advanced Monitoring and Optimization: Techniques for leveraging your Digital Twin to enhance network performance, predict issues, and optimize configurations. Automated Testing with CI/CD Pipelines: Building an automated testing workflow that reliably tests new configurations before deploying them in production, mitigating the risk of downtime due to bugs and configuration errors.

### Leveraging the Intersight Code Repo for Community-Driven Automation - DEVLIT-1508
Speakers: Marc Abu El Ghait (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098424083001d0fD
Discover in this session the power of the Intersight Code Repo, designed to enhance collaboration and automation. Learn how to access and contribute to a variety of open-source projects aimed at automating Intersight functionalities. The session highlights the EasyUCS project, showcasing how it automates inventory, configuration deployments and summaries with visual documentation. Gain insights utilizing the Code Repo to streamline IT operations, improve infrastructure management, and engage with the Intersight community for innovative automation solutions.

### Live Better with Technology - IF-1160
Speakers: James Blair (Pavelka)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098454830001dx1n
Wearable devices, trackers, and apps promise us the world. Longer, happier lifespans where stress, strains, and chronic conditions are managed for us by all-knowing technology. But how reliable are our new robot overlords? Are the marketing claims to be trusted? How are they best used? In this entertaining, interactive session we use science to unpick the facts and fiction.

### Make Technology Adoption Easier With ALLYANS and Cisco Training! - PARCRT-1890
Speakers: CHRISTOPHE DERVIEUX (ALLYANS)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098461876001dOpm
Technology is moving faster than people. Should we just accept this? We have a responsibility here at ALLYANS to help people everywhere build skills they need to leverage emerging technology and stay at the forefront of innovation. Come and see our Advanced Training offering on-stage with by our CISCO awarded Distinguished Instructors.

### Making SD-WAN Easy: Operational Simplification and User Experience - BRKENT-1313
Speakers: Nikolai Pitaev (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098304393001daBz
Cisco Catalyst SD-WAN (formerly Viptela) builds a secure, unified connectivity over any transport and provides simplified operations with centralized management, policy control, and application visibility across the enterprise network. This session will showcase how SD-WAN operations are made easier and more efficient with the introduction of new features and an enhanced user experience (UX 2.0). They address customer challenges in the areas of onboarding, configuration, user interface, troubleshooting, visibility, and AI Assistant for Networking. A live demonstration will also be provided. Participants will become familiar with the new, intuitive, and consistent GUI and will learn a fresh approach to configuration and guided workflows, improved visibility, and new troubleshooting aids. Also, a Conversion Tool from UX 1.0 configuration based on device and feature templates to UX 2.0 based configuration using configuration and policy groups will be presented.

### Making the Internet a Better Place by Participating in the IETF - BRKGEN-1385
Speakers: Eric Vyncke (Cisco), Prapanch Ramamoorthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098324327001d4AB
Ever wondered how innovation for the Internet works? The IETF is the main place where a community of engineers that come together to share ideas and innovate. It can be daunting to think of developing and writing standards at first but know that this is a journey. Everyone is welcome at the IETF, this is free, and there is something for everyone to do and to learn. The presentation will be a unique and fun conversation between a veteran and a newcomer at the IETF to provide attendees with varied perspectives. Come to this session to learn about the IETF, the kind of work that happens there, and how you can get started with your journey at the IETF.

### Malware Execution As A Service: A Deep Dive into CSMA Advanced File Analysis - BRKSEC-3101
Speakers: Jesse Munos (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098381595001d3QG
In this advanced session, you will learn how the Secure Malware Analytics(SMA) file analysis pipeline is designed. You will gain an understanding of the file analysis process from file ingest to detonation in a virtual machine, followed by a deep dive discussion of the SMA malware detection methodology. In addition, we will provide a technical overview of the Cisco Security Ecosystem and how detections in SMA surface in other Cisco Security Products such as Email Security, Firepower, and Secure Endpoint. The session will close with a review of the various APIs available to customers, their use cases, and example code to help users get started with the APIs.

### Malware Exposed: Understanding Tactics and Behaviors - CISCOU-2046
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098411095001dhLw
In today's digital landscape, understanding malware is crucial. This session explores how malware operates and the tactics used by cybercriminals. Participants will learn about behaviors like code obfuscation and lateral movement. You'll gain insights into malware mechanics to better anticipate threats. Designed for security professionals with foundational cybersecurity knowledge, this session includes case studies like Ryuk ransomware to illustrate common tactics.

### Manage your Cisco NX-OS fabric with OpenConfig - DEVNET-1677
Speakers: Sreenivas Rao (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098434529001dYdu
OpenConfig is fast becoming the industry standard, to manage and monitor network fabrics. Come and see how you can manage your NX-OS fabric, from Day 1-N with OpenConfig, leveraging open-source tools, and workflows.

### Managing Your Data Center Network with ServiceNow - BRKDCN-2969
Speakers: Lionel Hercot (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098295661001dv4W
In this session, we will showcase the new capabilities of the Cisco Data Center Network integrations with ServiceNow. We will cover how to inventory your stand-alone Nexus, ACI, and NDFC fabrics; and how to automatically create incidents based on alarms, faults, and events captured from ACI, NDFC, and Nexus dashboards. We will also showcase how to use the ServiceNow service catalog to make configuration changes to your ACI fabric. At the end of this session, you will have a good understanding of how the ServiceNow integration with Cisco Data Center Network products works and how you can use it in your own data center network.

### Managing the Managers, when OpenTelemetry and Network Automation Meet - DEVNET-2733
Speakers: Roque Gagliano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098448470001dEd0
OpenTelemetry is revolutionising Application performance management. But how is this connected to network management and automation? In this section we will discuss what OpenTelemetry is, the relationship between OpenTelemetry and network automation (including some recent IETF standards), and how you can use it to instrument your automation code. Finally, I will show a demo where we mix opensource and Cisco NSO automation, all instrumented by Splunk Observability Cloud to bring insights into a network automation stack.

### Mastering Cisco Observability: Seamless Integration with Splunk - DEVLIT-1266
Speakers: Aakriti Saxena (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098423378001dyWs
This session is demo based with live troubleshooting. In this session, you will see integration between AppDynamics application monitoring and Splunk ITSI. The resulting dashboard will combine intelligence from both these solutions.

### Mastering Cisco UCS: Innovations, Best Practices and Troubleshooting - BRKCOM-2456
Speakers: Michael Maurer (Cisco), Riccardo Tortorici (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098287567001dwPu
Your Cisco servers and network are up and running, and now you want to prepare for troubleshooting? We will discuss server networking problems, as well as problems that you might encounter between your server and your upstream data center network. Finally, we will demonstrate how you can effectively collaborate when troubleshooting using your compute and networking tools. At the end of this session, you should be able to troubleshoot most common server network problems from both perspectives.

### Mastering ISE Upgrades: Best Practices, Tips, and Tricks - BRKSEC-2889
Speakers: Romain PASSEREL (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098380172001dRxM
Planning an ISE upgrade can be challenging, with overwhelming documentation and unanswered questions. In this session, we will address the following key points: ISE lifecycle strategy: Remind the importance of ISE lifecycle and its impact on upgrades Upgrade options and method selection: Review different upgrade options available and provide recommendations on choosing the most suitable method Process check points: Highlight important checkpoints during the upgrade process Tips and tricks for successful operations: Share valuable insights to ensure a smooth and successful ISE upgrade Join us to boost your network security and performance as we guide you through these essential steps for a seamless ISE upgrade.

### Mastering Observability: A Unified Approach with Cisco-Splunk - BRKCLD-2282
Speakers: Luca Relandini (Cisco), Stefano Gioia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098277638001dVoN
Organizations today need help with using multiple tools to monitor and manage the health of their networks, applications, and systems. This session focuses on simplifying observability and provides insights into how a unified Cisco-Splunk solution can quickly identify and resolve issues impacting critical business services. During a live demo, witness the synergy of Cisco, Splunk, and other tools in action. This session will present several use cases, highlighting seamless interaction across multiple platforms. This collaboration provides a comprehensive view of your operations, enhances incident management, and improves MTTR efficiency and service reliability.

### Mastering Tenant Automation: Cisco Security Cloud Control APIs for MSPs - DEVSKL-2939
Speakers: Siddhu Warrier (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098452719001djpu
A Managed Service Provider's journey with any product typically involves designing automated systems to onboard a customer, manage their operations (including upgrades), and monitor the service in order to proactively handle issues as and when they arise. In this talk, we will show you how Cisco Security Cloud Control's APIs, built from the ground-up for MSPs, can help you design a streamlined solution at scale to offer a managed Cisco Secure Firewall solution as a service to your customers. We will first look at the tenant creation and service provisioning APIs that allow you to go from zero to a managed customer environment with a cloud-delivered Firewall Management Center and Multicloud Defense in a matter of minutes. We will then walk through APIs to onboard your customer's firewalls into your environment and start managing their policies, and about how you can react quickly to security advisories by upgrading all of your customers' firewalls using just a set of simple APIs. Finally, we will look at monitoring APIs that you can hook straight into your own alerting system so that you're always one step ahead of any problems.

### Mastering Test Automation Bliss with Robot Framework - CISCOU-1033
Speakers: Alfonso Sandoval Rosas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098400341001deHy
Learn how to effortlessly create comprehensive test suites that address the key points of your upcoming software releases, while integrating into your CI/CD pipelines, generating HTML reports and beyond. Everything with the aid of an open-source framework. Say goodbye to complex unit testing, and hello to your new favourite Robot!

### Mastering Troubleshooting with Cisco Catalyst Center & SD-Access - BRKTRS-3821
Speakers: Mariusz Kaźmierski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098396044001dIgP
Tired of spending excessive time troubleshooting Cisco Catalyst Center or SD-Access? Come to this session to enhance your troubleshooting skills, delve into the latest tools and troubleshooting techniques, and learn about the recent enhancements introduced in this space in Cisco Catalyst Center 2.3.7. So whether you are tackling issues independently or collaborating with Cisco TAC, this session is for you as it will empower you with essential skills to further boost your troubleshooting proficiency.

### Mastering Your Meraki Dashboard: Uncover Hidden Insights and Troubleshoot Effectively - BRKMER-2844
Speakers: Lina Alduaikat (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098338010001drUb
In today's fast-paced IT world, mastering network infrastructure management is more important than ever. Join this session to unlock the full potential of your Meraki Dashboard and gain a competitive edge. Learn how to discover hidden insights to optimize network performance, tackle advanced troubleshooting techniques, and apply best practices to ensure smooth, secure operations. By attending, you'll walk away with actionable strategies to enhance network visibility, streamline troubleshooting, and implement proven methods for managing Meraki devices. Don't miss this opportunity to elevate your network management skills and keep your organization ahead of the curve!

### Maximizing AI Potential: Best Practices for Leveraging Cisco and Splunk Data - CISCOU-2029
Speakers: Faisal Azizullah (Cisco), David Stanford (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098405404001dXRr
This session offers a deep dive into best practices for applying AI to Cisco-generated telemetry, network data, and Splunk's operational intelligence. Attendees will learn how to harness AI to optimize network performance, enhance security, and drive predictive analytics using data from Cisco platforms such as DNA Center, ThousandEyes, SecureX, and now Splunk. The session will provide actionable insights and real-world examples of turning raw data into valuable intelligence, enabling attendees to improve operational efficiency and make more informed decisions.

### Maximizing Cisco IOS XE Efficiency with YANG Suite - CISCOU-1043
Speakers: Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098403615001dxnm
Working more efficiently and effectively with Cisco Catalyst IOS XE starts with using programmability and automation to reduce troubleshooting time. Instead of wasting time troubleshooting, let's work on solving the difficult problems! In this session, we will explore the capabilities of YANG-based APIs through the free and publicly available tooling YANG Suite. This tool will help enable our devices to be configured with ease at scale. We will answer questions such as: how can I find the equivalent YANG Model for the CLI I use today? We will also build payloads to configure devices programmatically and generate Python Scripts and Ansible Playbooks to repeat those configurations at a larger scale.

### Me, My Email and AI - BRKSEC-2670
Speakers: Abdalla Taha (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098377585001dLhj
From simple spam to sophisticated AI-crafted attacks, email threats have evolved rapidly. Discover how Cisco's AI-powered defense system combats this evolution. Learn about the intricate workings of AI-driven threat detection engines and how they protect your data. Explore the challenges posed by AI-powered defense systems and how Cisco Secure Email Threat Defense addresses them. Gain insights into data privacy and security in an AI-driven world.

### Mean Time to Innocence: A Use Case Approach to Troubleshooting and Visibility with Nexus Insights - BRKDCN-3924
Speakers: Camillo Rossi (Cisco), Domenico Dastoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098297448001dxhK
Most operations paradigms in data center networks are reactive as operators struggle to fix business-impacting network, security, and compliance issues much later than the actual change in network that caused them. What if you had a powerful and intelligent assistant that could tell you exactly when something is wrong in the network and how to fix it before it impacts your business? In this session, we will walk you through how you can leverage Nexus Dashboard Insight (NDI) to identify issues in a Cisco Application Centric Infrastructure (ACI) or NXOS fabric, and then use the insight from NDI to address them.

### Media & Time Sensitive Networking with C9K Switches: Converging Time Sensitive Applications & Devices onto Ethernet - BRKENS-2094
Speakers: Randeep Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098300038001dBza
In this session, we will discuss how you can leverage Precision Time Protocol to build a network that can onboard time sensitive applications or devices onto an existing Ethernet Network. We will discuss technical details, supported features, limitations, and design considerations around the PTP & AVB Solution on Catalyst 9000 switching platforms.

### Meraki Unleashed: Programmatic Access, Programmatic Action - DEVNET-2482
Speakers: Jon Hartman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098445014001dgsT
In this session, you'll learn how to programmatically interact with the Meraki dashboard. We'll show how to leverage API endpoints, webhooks, and MQTT to harvest data and act upon it. We'll also cover resources to speed up and simplify your efforts, like the interactive documentation, Postman collection, and SDK. Modern networks and managed services require instant and automated control. Unleash the power of programmability and drive toward greater efficiency, fewer errors, more rapid action, and increased business value. You've outgrown the CLI, now it's time to outgrow the GUI!

### Meraki Wireless from a Troubleshooter Perspective - BRKEWN-2399
Speakers: Jakub Talalaj (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161404327001N77q
The session will help you to unleash the Power of Meraki Wireless. Get an exclusive look into how Meraki's cutting-edge technology, powered by the robust Meraki Cloud, assists to pre-emptively identify client issues and root causes, before end-users realize them. This informative session promises not just theoretical knowledge but practical insights and tips that can be immediately applied to your daily work. Come, explore the future of wireless networking, and equip yourself with the skills needed to create efficient, seamless, and reliable wireless environments. Your journey to mastering the Meraki Wireless begins here.

### Meraki and Ansible: A Collaboration Made in the Cloud - DEVNET-1399
Speakers: Cory Guynn (Cisco), Stephen Fulmer (Red Hat)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098432718001dsD4
In today's fast-paced digital landscape, businesses are continually striving to maximize their IT efficiency and agility. We are excited to unveil the latest fruit of the innovative cooperation between Cisco-Meraki and Red Hat - the new Ansible collection designed exclusively for Meraki's cutting-edge networking solutions. This collaboration promises to redefine network management by leveraging the powerful capabilities of Ansible automation platform in conjunction with Meraki's cloud-managed architecture. During this engaging session, participants will embark on a journey through the seamless integration of Ansible with Cisco-Meraki, enabling businesses to achieve unparalleled automation capabilities. Discover how this combined force empowers network administrators, IT teams, and DevOps professionals to simplify complex network configurations and operations while unleashing their full potential for innovation and business growth.

### Mission Critical OT Network Best Practices Using Private-5G Wireless Services - BRKSPM-3581
Speakers: Derick Linegar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161420169001NhX2
Private cellular deployments covering 4G and 5G connectivity are rapidly becoming a valid approach that provides private wireless services for a variety of enterprise customers and their use cases today. But where private 5G can really shine is in providing mission-critical services, leveraging deterministic radio behavior, QoS, and low latency-based connectivity services to finally enable wireless operational technology (OT) connectivity. Based on OT-oriented security and OT traffic separation framework, this new approach requires a new set of engineering best practices that are critical for a successful deployment. This session will review these best practices and provide examples for a private 5G-based deployment for the purpose of onboarding and operating mission-critical wireless OT infrastructure.

### Modern Authentication Explained to the Network Professional - BRKSEC-2144
Speakers: Aaron Woland (Cisco), Josh Green (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098368211001dMNs
Identity Security is all the rage (again). However the identity attacks look quite a bit different than they used to. To understand the modern identity landscape, you have to start to understand these crazy concepts like "Single-Sign-On" (SSO), what on earth OIDC is, and how come "cookies" are so important. However, the more things change, the more they stay the same, too. AAA: Authentication, Authorization & Accounting does not mean "RADIUS". Those of us in Network Security are usually familiar with 802.1X and authenticating to networks for wireless, wired, and even VPN. AAA is a fundamental and foundational security principle, not a product. Those concepts are universal and still apply when you hear the "new" authentication protocol types like: OAuth, SAML and OIDC, as well as terms like FIDO and WebAuthN. This session focuses on explaining modern web-based authentication protocols & teaching about them in a way that compares & contrasts them to network security authentication methods. In other words: come learn about the latest in identity attacks (like session hijacking, and MFA fatigue) and the latest in authentication protocols and how to understand them with your networking background. If you know all about SAML & OAuth already, but don't understand 802.1X or EAP this session is also for you!

### Modernizing Cisco's Data Center for AI - CENCOM-1025
Speakers: Daniel McGinniss (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227079912001Jf46
As AI continues to transform industries, Cisco is at the forefront, modernizing its data centers to meet the evolving demands of AI workloads. But it's not just about modernization. Cisco IT is reimagining its role and partnering with Cisco business units to power Generative AI programs and AI innovation. From high-performance compute to scalable storage solutions, we'll discuss Cisco's journey in building and deploying AI clusters. We'll also dive into how Cisco's approach to AI-driven networking and security enhances performance while reducing operational complexity through simple operational platforms. Join us to learn how Cisco is paving the way for AI-enabled data centers.

### Modernizing Private WAN Architecture for Critical Networks Infrastructure - BRKSPG-2063
Speakers: Cees de Gruijter (Rijkswaterstaat NL), Roberta Maglione (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161414516001N9ew
Several large Enterprises, like financial institutions, and Public Sector entities, like government agencies, military forces, transportation and utilities companies, have the need to evolve their own Private WAN infrastructure to obtain better controlled performance, increased scale, enhanced security, and flexibility at a lower cost. Attend this session to learn more about how to modernize and optimize this critical network infrastructure with advanced technologies like Segment Routing, Routed Optical Networking and security capabilities available on fixed and modular, high density and power efficient routing platforms. The session will also feature a customer testimonial from Public Sector in the Netherlands, Rijkswaterstaat (RWS), highlighting their experiences, motivations, and the benefits they have realised by fully embracing Segment Routing technology, including their end-to-end implementation of Segment Routing IPv6.

### Multi-Tier Fabrics: Network Designs for the Modern Data Center - BRKDCN-2999
Speakers: Marina Ferreira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296558001d0ED
Have you ever asked yourself what "clos" is or where that leaf/spine thing comes from? If yes, this is the right session for you. We are going to cover fat-tree, clos, and leaf/spine designs and expand beyond just the spine layer. We will spend some time on the super-spine and even hyperscale plane designs, as well as how you can cost-effectively use 400G/800G and where fixed vs. modular switches make sense.

### Multicast with EVPN, Segment Routing, and Traffic Engineering - BRKMPL-1123
Speakers: Mankamana Mishra (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161408837001NS4f
Segment Routing (SR) is an industry-standard approach aimed at simplifying transport network, including traffic engineering and management across multiple domains. Ethernet VPN (EVPN) serves as a widely adopted overlay solution for Layer-2 extensions when L3 VPN serves as an overlay solution for IPv4 and IPV6 private services.'this session offers a comprehensive exploration of multicast service delivery within EVPN and L3VPN networks. It delves into transport and services multicast delivery methods, covering both distributed protocols Multicast tree computation and controller-based approaches. Additionally, the session will focus on deploying multicast over the SRv6 transport network, providing a clear path forward for integrating multicast in SRv6 environments.

### Multimodality is the Future of GenAI - BRKAI-2552
Speakers: Ramin Pishehvar (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161399284001Ni2L
Multimodality is a relatively new term for something that has been around for ages: how people have learned about the world since they started to communicate with each other and interacted with the external environment. Individuals receive information from myriad sources via their senses, including sight, sound, and touch. Human brains combine these different modes of data into a highly nuanced, holistic picture of reality. Until very recently, the majority of GenAI solutions proposed by the Tech Industry were focused on the text-based modality. However, in recent months we have seen an explosion in the number of solutions proposed by tech companies, where at least some type of modalities is integrated into products: either as an input to the GenAI system or as an output (response) of the GenAI system. According to the global technology forecaster and brand consultant, KBV Research, the market of multimodal GenAI will reach $8.4 billion by 2030, marking an average annual growth of 32% in a seven-year period from 2023 to 2030 [1]. Furthermore, multimodal GenAI can be key to the development of Artificial General Intelligence (AGI), through the integration of modalities, contextual reasoning, multimodal interaction, and transfer learning and adaptability. In this session, you will learn about new challenges your IT department would face when designing a GenAI solution, which supports different types of modalities beyond text (e.g., image, video, audio, and beyond). We will discuss challenges ranging from the cost of training/finetuning of multimodal LLMs, to the sparsity of publicly available data for training such multimodal LLMs, to the technical challenges of fusing information from different types of modalities, to the importance of designing guardrails and safeguards against harmful content and/or vicious attacks. You will also learn about what specific challenges an engineer will face in adapting multimodality to GenAI applications specific to enterprises, such as the analysis of enterprise content in a multimodal Retrieval Generated Augmentation (RAG) setup. You will learn about different techniques on how to deal with multimodality in the realm of multimodal GenAI with practical examples and discussions. We will also discuss techniques that will allow you to use one generic learned representation to tackle all different modalities in your designed products. We will then present our initiative around integrating multimodality into Mofitic.ai and the supported multimodality features in our products. The session will conclude with a list of challenges we anticipate in the coming years on the integration of multimodality into GenAI products such as Motific.ai and beyond from technical, ethical, and marketing standpoints, which will open the floor for discussions. [1] Multimodal: AI's new frontier, MIT Technology Review Insights, May 2024

### My CxO had a Bad Meeting! - Best Practices to Deploy and Troubleshoot Webex within your Environment - BRKCOL-2055
Speakers: Christian Wolf (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098280646001d9Ig
The CxO had a bad meeting! Audio and video had poor quality, and the connectivity overall was choppy. Obviously Webex has a problem, so go and fix it! Does this escalation sound familiar to you? There are so many touch points (TCP vs UDP, HW vs SW, various forms of Proxies, (Application-) Firewalls, Network paths, ISPs, Cloud services), that can influence the meeting quality and result in a "bad" meeting experience. But how to identify the actual factors leading to this particular issue and how to prevent it from happening again. And what actually is a "good" or a "bad" meeting experience? This session will provide you with the necessary insights into security requirements, network dependencies and other potential implications. Key to successfully run Webex is a solid design for your organisation. You will learn how to successfully deploy Webex and Webex devices, continuously monitor and review your environment, and to analyse and troubleshoot leveraging the combined power of both Webex and the tightly integrated ThousandEyes capabilities interworking with the Webex platform and devices.

### NBAR and SD-AVC Operations and Troubleshooting in Cisco SD-WAN - BRKENT-2336
Speakers: Luis Daniel Martinez Mercado (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098308694001dO48
Application recognition is a fundamental component in SD-WAN solutions for traffic engineering, security features, and telemetry. Since application recognition functionality in SD-WAN solution is accomplished through NBAR and enhanced through SD-AVC, providing customers and the audience with a high to intermediate level of understanding of the NBAR and SD-AVC interaction and workflow, and how they are leveraged as a service by all the features in the routing platforms running in controller mode, will improve participants' experience and confidence in the solution. The session will contain a brief introduction to NBAR and SD-AVC features and focus primarily on their interaction and troubleshooting in the SD-WAN edge for known applications and custom application recognition. Troubleshooting will also include SD-WAN Edge communication with the SD-AVC container in Cisco SD-WAN Manager, as well as some known conditions, such as application cache poisoning. This session can be complemented with a walk-in lab for customers to experience first-hand use cases and troubleshooting techniques for application recognition based features in Cisco SD-WAN cEdge devices.

### Natural Language Processing (NLP) using Python - DEVNET-2160
Speakers: Erika Dietrick (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098439992001dVyW
NLP is the subset of AI that interprets human language. In this session, we'll first cover the foundations of NLP and its practical applications in modern networking. In the second half of the session, we'll demonstrate how to get started with NLP using popular Python libraries. This session assumes no prior knowledge of NLP, though basic knowledge of Python is helpful.

### Navigating Wi-Fi 7: Innovations with Cisco and Qualcomm - PSOENT-1859
Speakers: Jayanthi Srinivasan (Cisco Systems, Inc.), Sreeja Nair (Qualcomm Atheros)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098468325001dKxY
Join this session to explore the dynamic world of Wi-Fi 7 and the latest industry data, trends, and use cases that showcase how and why this next generation of wireless will have a transformative impact on connectivity. Highlighting the strategic partnership between Cisco and Qualcomm, you will learn how this collaboration has created a distinctive Wi-Fi 7 portfolio designed to deliver superior performance and innovation for modern applications everywhere. Attendees of this session will gain a clear understanding of Wi-Fi 7 market data based on third-party research and what the Cisco and Qualcomm partnership delivers for Wi-Fi 7 customers.

### Navigating the Sea of Change: Set Sail with Webex Contact Center for an Unmatched Customer Experience - BRKCCT-1331
Speakers: Juliette Ros (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098275244001dBwz
In today's dynamic business landscape, staying afloat requires navigating constant changes in order to achieve customer satisfaction. Join us for an exploratory session on Webex Contact Center where we'll investigate how its powerful components can help you anchor exceptional customer experiences. This session will provide a comprehensive overview of the latest features and updates, practical tips for smooth sailing, and realistic business outcomes. Whether you're new to Webex or looking to enhance your current setup, you'll leave equipped with the knowledge and tools to start navigating your journey towards customer experience excellence.

### Navigating the Webex App Hub Review Process: Best Practices for Developers - DEVLIT-1203
Speakers: Joe Zanini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098423020001dMAX
The Webex App Hub enables developers to share their Bots, Integrations, and Embedded Apps with the rest of the Webex Community. The App Hub is a marketplace, where Webex users and Admins can browse for potential value adds to the Webex experience. The Developer Portal is stocked with guidance in the documentation around submitting an application for listing in the Webex App Hub. Even though these processes are well documented, there are still nuances that are difficult to capture on paper. This presentation is an attempt to outline some of the common mistakes seen in App Hub Submissions and how to avoid them for a smooth and easy App Hub Review experience.

### NetDevOps AI Copilot: Automate the Automations - BRKOPS-1358
Speakers: Vinay Saini (Cisco), Srinjoy Chakraborty (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098345843001dDvy
In the rapidly evolving digital era, the traditional NetDevOps practices fall short of desired outcomes. They demand continuous analysis, planning, adjustments, validation, and time-consuming manual oversight. This session presents a Generative AI framework to optimize the different infrastructure automation outcomes. By leveraging chat conversations, AI analytics, standardized automation, accelerated deployment, and test validations, the framework enables a transformative approach to NetDevOps. The session will include Real-world case studies, showcasing how complex NetDevOps practices can be streamlined and executed effortlessly using simple mobile chat applications, achieving unprecedented levels of simplicity and efficiency in action.

### NetDevOps Unplugged: From Theory to Automation with Bayer AG - DEVNET-1175
Speakers: Ayca Ruppert (Cisco), Robert Kretschmer (Bayer)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098430150001dWpZ
Join us for an in-depth exploration of NetDevOps in action with Bayer AG. This session will take you on a journey from foundational concepts to practical implementation. Discover how we conducted comprehensive automation workshops and their outcomes, delving into Infrastructure as Code (IaC) frameworks and DevOps methodologies. We'll share our process of exploring various use cases, narrowing down to a specific use case around automated IOS-Updates, and developing a detailed workflow implemented into a IaC framework.This session should help sorting automation frameworks tailored for IaC, give you an idea where to start and what to focus on, and some "Oopsies"along the way.

### Network Best Practices for Artificial Intelligence (AI/ML) Data Center - BRKDCN-2921
Speakers: Chris Lapp (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098293681001dWoE
AI/ML is dominating the news cycle. Using the right infrastructure is critical to running AI/ML workloads. In this session, learn how to build a modern network suited to run your company's AI/ML workloads, manage congestion on Cisco Nexus 9000 Series switches, automate your network, and have visibility in AI workloads with Cisco Nexus Dashboard.

### Network Infrastructure Security in a Nexus 9K NX-OS VXLAN BGP EVPN Data Center Fabric - BRKDCN-3941
Speakers: G. Shankar Gopalkrishnan (Cisco Systems, Inc.), Tarique Shakil (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098297997001dykT
Hardening network infrastructure is critical to protecting your data center infrastructure. Network infrastructure security is the foundational protection of any network. If the network nodes have security loose ends, everything, such as the host, applications, and services, depending on the network, will collapse with the network. The most sophisticated encryption techniques may be used at the application layer, but the application's connectivity is lost if the network is unavailable. In this session, we review the various security aspects of a VXLAN BGP EPVN fabric. We address issues related to protecting the fabric from malicious hosts and attacks. First hop security is a VXLAN feature that validates the authenticity of the hosts using DHCP snooping and IP ARP inspection. A vital aspect of a VXLAN fabric is providing the same level of security, especially when hosts move within it. These moves could occur within VXLAN fabric and across the Multisite fabric domain. In addition, NXOS on the N9k provides security features to protect the routing protocols running in the underlay and overlay. These features, such as routing protocol authentication, BGP EVPN Null Route to protect against DDOS attacks, and BGP EVPN storm control to protect against broadcast storms, are also discussed. The session is tailored to educate customers on using our VXLAN features to their maximum benefit and maintaining network security. This session assumes the audience has a strong background in VXLAN BGP EVPN technology on the NX-OS Nexus 9k platform.

### Network Observability Reimagined: The New Meraki + Splunk Integration - CISCOU-1030
Speakers: Cory Guynn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098399257001do8s
See the next evolution of the Meraki and Splunk integration, built from the ground up to bring clarity to network operations. This major release delivers sensor analytics, enhanced security monitoring, intelligent alerting and network performance data through a streamlined interface. Through live demonstrations, see how Meraki's expanded API capabilities feed Splunk's analytics engine, turning network data into instant insights. Learn practical techniques to spot issues before they impact users and respond to threats faster than ever. Join us to see what's possible when powerful analytics meets network intelligence.

### Network Sustainability Metrics: from Device View to Per Service Path Visibility - BRKSPG-1065
Speakers: Monica Aguado (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161412205001NGkB
There are many approaches for reaching sustainability goals in the industry. In this session we will focus on how Cisco Provider Connectivity Assurance exposes network sustainability metrics not only at the device level, but also at the service path, providing end-to-end visibility of power and carbon footprint over time. Sustainability metrics are displayed and correlated with other service SLA based metrics such as packet loss or latency deriving greater insights from the combination with other performance assurance metrics.? Key outcomes include detecting trends or abnormal power consumption for corrective actions, enabling well-informed decisions based on power or carbon footprint, and be monetized by Service Providers by launching differentiated services that offer customers real value and real-time insights into their service's SLA and carbon footprint.

### Network Telemetry and AI for Network Incident Response - DEVNET-3707
Speakers: jesus Illescas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098450470001d8Ji
In this session, you will learn how to use open source tools and LLM to monitor and react to network incidents. You will see how to develop a solution that collects telemetry data from network devices and applications, and how to use a LLM to analyze the data and help you troubleshoot issues.

### New Business and Performance Innovations that Enhance Observability for Hybrid and On-Prem Applications - BRKAPP-1026
Speakers: Gregg Ostrowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098273175001dAkp
Join us for an informative session discussing the latest innovations in AppDynamics, designed to revolutionize your approach to observability and application security. Discover how new AI capabilities enhance user experience and operational efficiency, and deliver deep insights into your AI-powered apps. We will also explore the integrations across the Splunk Observability portfolio, which enable a unified view of your IT environment, enhancing collaboration and decision making. Additionally, learn about the advancements in application security that ensure robust protection against emerging threats. This session is essential for IT professionals looking to optimize their application ecosystems and safeguard digital assets.

### New Horizons in Observability: Managing Artificial Intelligence and Quantum Computing Systems - BRKETI-1816
Speakers: Scott Phillips (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098314473001d7wL
Two disruptive technologies are leaving the realms of scholarly research and finding their way into businesses that differentiate themselves through innovation. Artificial Intelligence and Quantum Computing utilize fundamentally different hardware and software platforms than traditional IT environments. What approaches will be needed to observe and optimize these emerging technologies? Participants will gain a better understanding of Artificial Intelligence and Quantum Computing workloads and be able to: Identify strategic use cases across industry verticals Describe basic architecture and components Recognize similarities and differences of these new platforms Prioritize current techniques and promising new methods of data collection and interpretation This session is designed for both executive leaders and influential technologists without requiring knowledge of data science or physics.

### New innovations in Splunk AppDynamics to enhance observability for hybrid and on-prem applications - PSOOBS-1889
Speakers: Cale Hilts (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098471425001d8mQ
In the rapidly evolving landscape of hybrid and cloud-native applications, monitoring application performance and troubleshooting end-user experience is more challenging than ever. Whether it's managing legacy applications, adopting microservices, or orchestrating containers, organizations can't afford to have technology teams spend time in costly war rooms while wasting time finger-pointing. In this session, we'll explore the latest innovations in Splunk AppDynamics that empower IT professionals and DevOps teams with unparalleled insights into their application environments, including: The latest AppDynamics integrations across the Splunk Observability portfolio The new capabilities for the AppDynamics virtual appliance form factor that improves time-to-value in time-to-value, increase deployment flexibility, and application security when'supporting self-hosted applications Optimize the user experience by analyzing the end user user interaction on the mobile application

### News and Updates to Webex Security Mechanisms - BRKCOL-2279
Speakers: Marc Dionysius (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098283206001dB8T
As organisations rely more on digital collaboration tools, it is crucial to have secure and compliant communication platforms. The presentation will provide you with best practices to deploy Webex within your network, understand network, firewall and proxy requirements as well as different deployment scenarios for secure networks. On top of that, we will explore the latest changes to the security mechanisms provided by Webex that are specifically designed to fulfil security and privacy requirements, and allow you to deliver a robust solution that guarantees both. This session aims to educate customers and partners about news and updates to those mechanisms, as well as the overall security and privacy benefits offered by the most secure collaboration solution available today.

### Next Gen Infrastructure AI, Security and Observability - ITLGEN-1502
Speakers: Shridevi Rajeshwar (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098457898001dCev
In this session, you will enter Cisco IT's vast infrastructure environment and discover how they have been developing innovative solutions to address complex challenges with themes that will resonate across any IT organization. As Cisco's first customer, the Infrastructure Team utilizes Cisco technologies to build world-class infrastructure - featuring AI, Security, and Observability at the core of their innovation and operations. This session will cover how the Cisco IT infrastructure team combines talent with technology to formulate strategies for success. Join us to gain valuable insights into the future of IT infrastructure and discover how these methods can be applied to your organization. All IT leaders are encouraged to attend

### Next-Gen Hyperconvergence: Cisco Compute and Nutanix Innovations Unveiled - PSODCN-1873
Speakers: Jeff Mercier (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098468146001dfqG
Join this session to explore innovative AI solutions, UCS X-Series support, and groundbreaking management integrations between Cisco and Nutanix, providing enhanced visibility and insights into the industry's most complete hyperconverged solution. Discover how the latest innovations in the Cisco Compute Hyperconverged with Nutanix offering simplify the processes of purchasing, deploying, managing, and supporting hyperconverged infrastructure, making it superior to other HCI options available.

### Next-Gen TAC Insights: Leveraging AI and API's to Boost Your Operational Efficiency - AIHUB-2406
Speakers: Vivek Singh (Cisco Systems, Inc.), David Hanes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161396155001N54J
As a Cisco customer or partner, you open cases for support on various technologies and solutions. This generates case data that when viewed holistically over time, can provide compelling insights on your interactions with Cisco support and products. This session provides you the building blocks and shows you how to assemble them to easily obtain these insights and transform your support and RMA processes. Leveraging GenAI and an agentic approach, in conjunction with available Cisco APIs, you can automate tasks, enhance productivity, streamline operations, and improve your overall support efficiency. Join us and learn to enable Next-gen TAC insights for yourself.

### Nexus-as-Code - Kick-Start Your Automation with ACI - BRKDCN-2673
Speakers: Daniel Schmidt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292019001dAv9
Infrastructure-as-Code (IaC) is becoming the prevailing approach to building, managing, and operating infrastructure. In this session, you will learn how to leverage Nexus-as-Code with its easy-to-use, opinionated data model to instantiate Cisco Application Centric Infrastructure (ACI) fabrics in minutes. ACI resources can be defined in human-readable configurations that can be versioned, reused, and shared. Adding CI/CD helps standardize and enforce a change process. All of this provides a solid baseline to develop further automation.

### Not More Mindfulness - IF-1158
Speakers: James Blair (Pavelka)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098454478001dtYr
Mindfulness, isn't it just meditating? You've heard a lot about mindfulness, and perhaps even tried some apps or isolated sessions. But why hasn't it stuck, and exactly what is it you are supposed to be feeling? Our experienced facilitator will lead you through a guided mindfulness practice, lowering your stress and clearing your mind whilst explaining the science backed benefits and basis of each exercise.

### Nutanix GPT-in-a-Box with Cisco: The Power of Two? - PARAI-1551
Speakers: Laura Jordana (Nutanix)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161424367001NGuw
AI can transform businesses, whether by increasing productivity, reducing processing times or accelerating time to value. Discover how easy it is to build, deploy, and run generative AI securely using the power of Nutanix Cloud Platform and Cisco Infrastructure. Understand the key use cases to support and optimize your AI initiatives.

### OSPF LSA Types Made Simple - CISCOU-2051
Speakers: Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098412875001d03Q
Link State Advertisements (LSAs) are a favourite topic when it comes to discussing Open Shortest Path First (OSPF) details of operation, and deservedly so: Understanding any advanced topic in OSPF depends on understanding LSAs. The rewards can not be overstated, ranging from profoundly understanding the area types, filtering and summarization specifics, network types, through the ability to interpret the link-state database, to truly making OSPF workings crystal clear and intuitive. Have you been through a truly decent explanation of LSAs and their types, though? For once, let's explain the LSAs and their types the right way - a way that is illustrative, intuitive, and makes the explanations stick as the LSAs become your second nature!

### Observability with OpenTelemetry: It Just Makes Sense - BRKOBS-1891
Speakers: Stephane Estevez (Cisco Systems, Inc.), Patrick Peeters (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098340498001dexx
What if there was an open-source, vendor-neutral framework for collecting telemetry data? One single agent that provides a consistent and standardised way of instrumenting applications and infrastructures? Good news there is! What we've just described is OpenTelemetry a joint project between Splunk, Google, Microsoft, Amazon and several other organisations that currently has the second-largest number of contributors in the Cloud Native Computing Foundation after Kubernetes. But do you know how to use it? Or if you should use it? The best thing to do is to learn about OpenTelemetry from the major contributor of the code. This session is an introduction to OpenTelemetry and will explain why it doesn't make sense to have an Observability strategy without OpenTelemetry.

### Observability: Web Perf for when Milliseconds Make Millions - BRKOBS-2890
Speakers: Arthur Hamon (Cisco Systems, Inc.), Robert Castley (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098343009001da2Q
Cloud and online applications promise scalability, but handling massive traffic on your application also requires optimizing them. Each of us has experienced the frustration of waiting for content to appear on the screen, whether when shopping online or trying to complete a transaction on a business application. Using some examples, we'll explore how painfully this can hurt businesses, then how to measure, (this section will include a high-level description of methodology and tools that are part of the Splunk Observability portfolio), and optimize to ultimately contribute to building a culture of performance in your organization.

### Observing GenAI-Infrastructure: You Can't Protect What You Can't See - DEVNET-3310
Speakers: Shannon McFarland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098450099001dFf5
In this ultra-fast-paced world of AI and Cloud Native, knowing what is running, where, and what it is doing is challenging. Managing and protecting workloads is incredibly difficult if you can't see what is happening. In this technical session, discover how open source projects like OpenTelemetry, Jaeger, Cilium with eBPF, Tetragon, and others can enhance observability and security for Generative AI (GenAI) infrastructure like Agents. Through practical demonstrations, attendees will gain actionable knowledge on deploying these tools to ensure GenAI workloads are both performant and secure.

### Omnichannel Contact Center: How to Elevate Your Customers Experience and Deliver Solutions for Your Business - BRKCCT-2017
Speakers: David Veevers (Cisco), Emerik Giorgetti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098275804001dlP6
Want to learn about implementing cutting edge CX to improve brand loyalty while keeping down operational costs and specifically? Are you curious to see how you can achieve these goals leveraging Cisco's CX product portfolio? With new channels emerging such as RCS, smarter AI agents using LLMs, proactive outbound campaigns that dip into the wealth of data businesses hold on customers - the time is ripe to re-design the CX strategy! Wait no more and register now! Learn how to leverage the latest omnichannel features in Webex Contact Center and Contact Center Enterprise to create stellar experiences. I'll walk you through real-world examples and provide a clear strategy to help you design and implement these solutions effectively in your business.

### On-the-Move Unified Wireless Network Across 5G, Wi-Fi, and Satellite for Emergency Services - BRKSPG-2046
Speakers: Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161414142001NpRe
Unified wireless communications is another way of describing an infrastructure model that offers ubiquitous IP connectivity over any underlying infrastructure, focusing primarily on wireless technologies, with private 5G and Wi-Fi being the most common, but not exclusive. In this session, we will describe a system co-developed with BWI, the IT services provider to the German armed forces, that creates such an infrastructure across private 5G, Wi-Fi, and satellite while being extensible to all other wireless and wired technologies using IP and routing as the unifying layer. This allows BWI to offer a common transport infrastructure to all applications in a reliable and access-agnostic manner. Any available spectrum can be utilized by the applications. In partnership with the BWI CTO, we will discuss the application of such an infrastructure to the critical/emergency communications domain by showing how this can be integrated into a fully mobile system that can be dropped in and deployed ad hoc, with easy extensibility for dynamic geographical coverage. The system has full automation and full lifecycle management in any field situation, with self-healing connectivity as a key characteristic.

### Open Telemetry 101 - DEVNET-1755
Speakers: Diyar Alyasiri (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098435253001dY1m
An open industry standard for telemetry is exciting, and opens up possibilities for providing observability that have not been available in the past. This session will cover the basics of Open Telemetry, also known as OTEL. We will review what OTEL is, how Cisco has contributed to the OTEL standard, and what is possible when you leverage OTEL in your observability strategy.

### Open-Source GenAI Bot for Catalyst Center - DEVNET-3000
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098449736001dFql
Are you looking to simplify network management using Cisco Catalyst Center REST APIs and Generative AI, to transform your existing network automation Apps? Participants will learn how to develop a Cisco Catalyst Center open-source AI ChatBot. We will step-by-step build the AI platform, reviewing the options to use real-time or near-real time datasets, retrieved with API calls to Catalyst Center. We will review different LLM models and data transformers and find one that meets your technical requirements and enterprise policies. The ChatBot allows network engineers to easily find relevant information using natural language, filtering only what is important. The GenAI open-source Bot will transform how we manage network infrastructure, enriching and simplifying network management tasks. The attendees will receive the Python open-source code for a complete AI system, that may be used in their labs for future testing and development.

### OpenShift and Hypershield: Revolutionizing Unified Security Controls for VM and Container Protection - BRKCLD-2522
Speakers: Michael Hrivnak (Red Hat), Matt Correll (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098278229001dtk7
Red Hat and Cisco have partnered to integrate OpenShift with Cisco Hypershield, revolutionizing security for containerized and traditional workloads in hybrid cloud environments. This integration streamlines the transition from legacy VM platforms to modern, cloud-ready applications. This 90-minute session will highlight the challenges of siloed orchestration commonly used for VMs and containers, then explore how the OpenShift+Hypershield integration transforms security controls and visibility across these traditionally separate domains. Key topics include: Unified security fabric across containerized and traditional workloads AI-powered protection with auto-segmentation and distributed exploit prevention Dual data plane innovation for live policy validation Kubernetes-native security orchestration Ideal for OpenShift administrators, security professionals, cloud architects, and IT leaders, this session will demonstrate how the OpenShift+Hypershield integration sets new benchmarks in hybrid cloud security, operational efficiency, and workload protection. Attendees will gain practical insights into implementing this solution in diverse hybrid cloud environments.

### Opening Keynote: Go Beyond - KEYGEN-1111
Speakers: Oliver Tuszik (Cisco), Jeetu Patel (Cisco), Martin Lund (Cisco), Tom Gillis (Cisco), Anurag Dhingra (Cisco), Kamal Hathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227083075001JIfR
Get a front row seat to hear directly from Cisco executives on how we are revolutionizing the way infrastructure and data connect and protect organizations in the AI era. You will hear about innovations to power AI-ready data centers, deliver future-proofed workplaces, and drive unparalleled digital resilience.

### Operational GenAI: Practical Application of AI in the Stack - CENDEV-1007
Speakers: Shannon McFarland (Cisco), Matt DeNapoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227080453001Jp8S
This technical presentation examines how Generative AI (GenAI) can be leveraged to accelerate automation adoption in IT and developer operations. We first will investigate how GenAI can be used to the lower the barrier to entry for organizations looking to employ automation in their infrastructure management. Then we will move "up the stack" and see how cloud native application architectures can take advantage of agentic frameworks to optimize deployments and mitigate issues. The focus will be on GenAI's role in advancing automation, streamlining CI/CD processes, and employing its emerging function in predictive analytics for operational efficiency. Attendees will gain insights into GenAI's practical applications, implications for infrastructure as code (IaC), and the future of collaborative human-AI development environments. The session aims to equip technical professionals with a clear understanding of GenAI's impact on their field and actionable knowledge on leveraging these advancements within their practices.

### Operationalizing AI: Best Practices in Data Protection and Responsible AI - PSOCOL-1795
Speakers: Keith Griffin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098466336001dsTg
A new wave of generative AI capabilities is set to transform how we work and engage with customers. From collaboration features like message and meeting summarizations, highlights, and action items to purpose-built contact center AI, Large Language Models (LLMs) and other machine learning techniques are being deployed to improve hybrid work and deliver exceptional customer experiences. Join us to explore effective strategies for operationalizing AI, minimizing risks, and ensuring data protection through responsible AI implementation and best practices in enterprise settings.

### Operationalizing Cisco's Multicloud Defense Logs in Splunk - CISCOU-2037
Speakers: Raja Soundaramourty (Cisco Systems, Inc.), Marcin Kope? (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098407900001dKyC
Cisco Multicloud Defense offers robust security threat visualization and analytical capabilities. However, if you seek enhanced custom visualizations, advanced analytics, and log correlation with other security tools, Splunk is the solution. In this session, we will demonstrate how integrating Cisco Multicloud Defense with Splunk is straightforward and how to derive greater value from Cisco Multicloud Defense logs using Splunk.

### Optimizing ACI Data Center with AI-Powered Infrastructure as Code - AIHUB-2010
Speakers: Rafael Muller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161394658001NZql
Explore the dynamic fusion of Infrastructure as Code (IAC) and AI, designed to expedite the adoption in Application Centric Infrastructure (ACI) in data center environments. You will delve into real-world examples through live demonstrations where AI augments IAC including provisioning, declarative configuration changes, and day-to-day administration. Leaving this session, you will have a clear picture of how the combination of AI and IAC can increase productivity, and reduce risk in your data centers. Join us for a grounded exploration of how Cisco ACI and AI can revolutionize infrastructure automation without compromising credibility.

### Optimizing Security and Agility: Leveraging SD-WAN Capabilities in Cisco Secure Firewall - BRKSEC-2086
Speakers: Alejandra Paez Castro (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098366398001ddPB
As organizations expand their operations, ensuring secure and streamlined connectivity becomes paramount. To address the challenges related to secure connectivity, Cisco Secure Firewall introduces SD-WAN capabilities that provide connectivity without compromising security. This session will cover the SD-WAN capabilities that can be leveraged in the Cisco Secure Firewall Threat Defense, such as firewall configuration to steer traffic directly to the Internet through multiple active WAN links based on either applications or users (DIA), firewall operation and configuration to select the best egress interface based on link metrics (DIA with Path Monitoring), simplified branch to hub communication using DVTI, SASE/SSE integration, and the newly introduced SD-WAN Wizard to simplify the deployment of VPN tunnels and routing configuration between Hub and Spokes. At the end of the session, a demo will allow attendees to visualize how these features work and how to identify and troubleshoot potential issues.

### Outsmarting the Adversary: A Proactive Security Strategy with Managed XDR - PSOMS-1784
Speakers: Bruno Marques (Cisco Systems, Inc.), Stefan Gutekunst (Logicalis)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098470884001dZfh
The cyber threat landscape is rapidly evolving, with attacks becoming increasingly sophisticated and targeted. To effectively combat these threats, organizations must adopt a comprehensive and proactive security strategy. Managed Extended Detection and Response (XDR) offers a powerful solution by consolidating security tools and processes into a unified platform. This abstract explores the critical role of Managed XDR in enhancing an organization's security posture, detecting threats early, and responding swiftly to incidents. It delves into the key benefits of Managed XDR, including improved threat detection, accelerated incident response, and reduced security operations costs. Additionally, it discusses the challenges organizations may face in implementing Managed XDR and provides insights into best practices for successful deployment. By adopting a Managed XDR approach, organizations can gain a significant advantage in the ongoing battle against cyber threats.

### Overlay Design Options for Campus Networks - BRKENS-2501
Speakers: Raj Kumar Goli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098300779001dc3u
This presentation will delve into the various overlay design options available with the state-of-the-art Catalyst 9000 Switching Platforms. We'll start by defining the concept of network overlay and its critical role in modern network architecture, especially in the era of cloud computing and virtualization. The focus will then shift to the Catalyst 9000 series, exploring how these switches leverage advanced technologies to support multiple overlay design options. This includes discussion on technologies like Virtual Extensible LAN (VXLAN) and Software-Defined Access (SD-Access), which are integral for creating network overlays.

### Overlay Multicast in VXLAN EVPN (Tenant Routed Multicast - TRM) - BRKDCN-3638
Speakers: Tarique Shakil (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296914001duzN
Data centers host servers that host various multicast applications such as collaboration, multimedia, video streaming, and conferencing. As video traffic is the highest bandwidth-consuming application in the network, it is imperative to implement architectures that most optimally forward traffic for multicast within the data center for east-west traffic and exiting/entering the data center for north-south traffic to/from external networks. This unique advanced-level session introduces Tenant Routed Multicast (TRM) routing in a VXLAN BGP EVPN fabric. The session will address the following questions: What problem does Tenant Routed Multicast address, and what are its benefits? What is an IPv4/IPv6 network architecture enabled for TRM? How do the control and data planes work in a network with TRM configured? What are the latest TRM innovations from Cisco? It is assumed the audience has a strong background in VXLAN BGP EVPN technology, MP-BGP, and fundamentals in IP multicast routing concepts such as PIM, and IGMP. You will leave this session with an introductory-level understanding of the TRM feature in VXLAN fabrics, applications, and architecture.

### Packet Buddy - Chatting with your PCAPs, via the Cloud or Locally on Your Own Machine! - AIHUB-2000
Speakers: Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161392766001Nu0p
This session will showcase a fun and innovative solution that allows attendees to chat, via a variety of Large Language Models (LLMs), with their own Wireshark packet captures. Ask the LLM what kind of traffic you have - what errors it sees - or use it to delve into and understand packets and packet flows better! The choice is yours. This engaging and entertaining session is hosted by the dynamic duo of Prapanch Ramamoorthy and Dave Zacks, both Cisco Live Distinguished Speakers as well as enthusiasts for AI and it's use in network, security, and analytics applications. Prapanch and Dave will show you what this capability can do, and more importantly, how you can set it up and use it in your own deployments. Come to this fun, interactive session to see how using our open-source "PACKET BUDDY" solution can get an LLM chatting with your own packet captures!

### Packet Journey inside Catalyst 9000 Switches - BRKARC-3090
Speakers: Ivan Shirshin (Cisco), Nathan Pan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098274867001dmQU
The Catalyst 9000 series is the backbone of enterprise networking, empowering businesses of all sizes from traditional campus setups to advanced SDA and EVPN overlay architectures. To manage and optimize these networks effectively, network engineers need a solid understanding of packet forwarding on the Catalyst 9000, including both hardware and control planes, as well as the diagnostic tools in IOS-XE that can analyze packet flows. This session dives into how Catalyst 9000 switches handle packet forwarding to streamline traffic path verification and troubleshooting. We'll explore various packet-handling scenarios, including: Catalyst 9000 data plane architecture: An overview of UADP and SiliconOne models Transit packet flow: How packets pass through the switch In-band packet flow to the CPU: Understanding in-band management traffic Unicast packet forwarding: Tracing the unicast forwarding path Multicast replication: Investigating how multicast packets are replicated Diagnosing packet drops and forwarding issues: Practical insights for tackling packet handling problems Join us to deepen your expertise on Catalyst 9000 and boost your skills in network path analysis and troubleshooting!

### Pig-in-the-Middle - TLS Decryption and Encrypted Visibility Engine Deep Dive on Cisco Secure Firewall - BRKSEC-3320
Speakers: Christopher Grabowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098383033001dvTy
This session dives deeply into TLS and QUIC decryption on Cisco Secure Firewall Threat Defense. Participants will learn how TLS and QUIC work, followed with step-by-step explanation of decryption logic on the Cisco Secure Firewall in detail, along with examples and demonstrations. We will also look at how to gain visibility into secured traffic without decryption using the machine-learning-empowered Encrypted Visibility Engine. Learn the best practices to maximize the performance and inspection efficacy of the encrypted traffic in your network. Familiarity with general knowledge of TLS, cryptographic concepts like Diffie-Hellman exchange, hashing functions, and symmetric/asymmetric encryption is recommended. This session is targeted to pre-sales decision makers, post-sales technical support, and senior/middle management.

### Planning and Designing Successful Cloud Calling Deployments with Webex Calling - BRKCOL-2787
Speakers: Johannes Krohn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098285215001doI0
Customers and Partners considering a cloud calling deployment based on Webex Calling need to tackle a number of decisions including PSTN selection, location planning, dial plan design, integrations with existing call control systems and mapping business requirements to Webex Calling features. In this session, the participants will get guidance on all of the above and, in addition, in this session multiple examples will be presented of how to use and combine Webex Calling features to implement smart call handling and group functions. The participants will also get insights into the existing bulk provisioning options for Webex Calling. This session does not cover Webex Calling dedicated instance.

### Platform Engineering: Building Golden Paths for Modern Applications using Cisco Technologies - BRKCLD-2226
Speakers: Jara Osterfeld (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098277444001deKc
Platform engineering and Spotify's "golden paths" are the new kids on the block. We talked DevOps, we talked SRE, and now we talk platform engineering. Why? Because managing modern application environments is complex, and the more solutions we find, the more challenges seem to arise. In this session, we will take a closer look at what platform engineering is, and build golden paths for deploying and maintaining VMs, Kubernetes clusters, and Generative AI applications. The focus of this session is on building a toolchain and workflow using Cisco and open-source technologies with the goal to deliver standardized services and to create a first set of opinionated best practices for application developers to consume enterprise-managed cloud infrastructure.

### Plenty of Spots Available! Take Charge of your Parking Management with Meraki Vision and Webex Connect - DEVNET-2775
Speakers: Juliette Ros (Cisco Systems, Inc.), August Martens (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098448648001dyTm
Discover how Cisco's hybrid work innovations can revolutionize parking facilities in this electrifying DEVNET session! Ever been frustrated by the lack of available parking spots or EV chargers? We've been there too. This session uncovers the journey of designing and deploying an EV parking management solution, tailor-made for a strategic account and implemented in a Cisco office. With the intelligent use of Meraki MV cameras, we can alert users via WhatsApp when a parking spot becomes available. The cameras can also detect and alert users when their vehicle is fully charged. This is not a complex system; it's a solution you can build yourself with the latest Cisco technologies, including Meraki Custom Computer Vision with Cogniac and Webex Connect Omni-channels. Prepare to delve into the world of modern software development with Google Cloud Functions and Webhooks. Get ready to supercharge your knowledge and gain inspiration for your future DEVNET projects. This is more than a DevNet Classroom; it's a thrilling journey into the future of smart parking solutions. Don't miss it!

### Power Security Operations with Cisco XDR - PSOSEC-1791
Speakers: Jon Speer (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098472548001d4gN
Whether you are an IT leader with security response on your long list of duties, a network security engineer getting blindsided by incidents originating outside of your control, or running a SOC that just can't keep up, the Cisco XDR team has been innovating and building to your use cases. In this session, we'll review how we're adapting to the constantly shifting threat landscape, catch you up on the latest updates, and give insights into where we see the platform going as we integrate with the world's leading security operations solution.

### Power Your WAN with SD-Routing - BRKENT-1039
Speakers: Lars Granberg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098304022001dgif
Enterprise WAN networks are a labyrinth of myriad use cases. There is an ever-increasing need for a single management solution that can bridge the gap between traditional WAN routing and SD-WAN environments. This session will introduce the participants to the Software-Defined Routing (SD-Routing) solution, which aims to modernize traditional routing deployments with innovations in cloud and security, while providing operational simplicity and rich observability. Power the platforms with SD-Routing.

### Power the SOC of the Future with Splunk and Cisco - BRKSEC-1885
Speakers: Antonio Forzieri (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098364610001dHrr
Discover how Splunk empowers your security strategy by seamlessly integrating with Cisco solutions to deliver actionable insights. This session goes beyond the basics, showing you how to leverage Splunk's advanced analytics to strengthen your cybersecurity posture. See real-world applications of the platform and learn how it fits into your IT and security operations to enhance visibility, accelerate threat detection, and boost overall resilience. If you're looking to harness data for smarter, faster security decisions, this session is a must-attend.

### Powering Social Inclusion & Economic Stability In the Age of Artificial Intelligence - ITLGEN-1518
Speakers: Guy Diedrich (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098460630001dW1K
In our fast-paced digital world, the global shortage of skills and technological inequities present major hurdles to achieving social inclusion and economic stability. Join Guy Diedrich, Cisco's Senior Vice President & Global Innovation Officer, for an illuminating session that explores how investments in technology and skill-building can address these critical issues. This presentation will demonstrate the transformative potential of AI and other innovative technologies, combined with extensive training initiatives, to uplift diverse communities, enhance job prospects, and foster sustainable economic development. Attendees will learn about Cisco's comprehensive strategy for workforce development, which includes cutting-edge learning tools, digital literacy programs, and inclusive talent development pathways designed to equip individuals for the digital workforce.

### Powering Sustainability @ Home with Cisco IoT, Meraki Sensors, Home Automation, and AI - BRKETI-1006
Speakers: Ivan Padilla Ojeda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098313772001dNNS
The integration of state-of-the-art technologies in home automation holds great potential for contributing to global sustainability by optimizing resource consumption. Advanced home automation systems, leveraging cutting-edge technologies like AI and the Internet of Things (IoT), enable intelligent energy management, resulting in significant reductions in energy and water consumption. Smart sensors and AI algorithms precisely regulate lighting, heating, and cooling systems, adapting to occupants' preferences and environmental conditions. And not only enhances convenience but also aligns with the global imperative of resource conservation, fostering a more sustainable and eco-friendly living environment. In this session, we will go a little deeper into how we can leverage Cisco's advanced technologies to implement home automation policies that will positively impact on our day to day live, in a significant reduction of our utility bills and what is more important, in leaving a better world to our children.

### Preparing for AI and Automation: Building a Resilient and Predictive Network - PARENS-1522
Speakers: Lauren Malhoit (IP Fabric)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098462628001dR4m
Over 25% of planned IT initiatives overrun their planned budgets by 2x - 4x, and rarely finish on time. Enterprises in 2025 aim to align with the business while also managing workforce changes, but maintaining continuity across multivendor networks during this time is challenging. Gartner reports that 40% of global IT budgets are spent on technical debt because of this. This session highlights how network assurance/digital twin platforms enable IT teams to sustain stability and mitigate risk. Learn how leveraging a comprehensive assurance solution can streamline decision-making, reduce downtime financial impact, and improve collaboration'supporting strategic goals in competitive landscapes.

### Preparing for the New DevNet Associate Certification - BRKCRT-2080
Speakers: Kareem Iskander (Cisco), George Koukis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098289044001d2c9
Perhaps you're considering a career in IT or in Automation, and you're looking for a way to get started. You may be preparing for the DevNet Associate now. Or maybe you're just considering the possibility. Regardless, this session is for you. We will show how the engineer evolved and why automation skills are needed, how Certifications are created, possible exam questions, and real-life examples. You'll come away with strategies to study for the exam and a clear path forward in your learning journey. Come to this session to learn best practices in prepping for your DevNet Associate.

### Proactive and AI-driven Managed Campus: A Smarter Approach for Business Continuity - PSOMS-1802
Speakers: Shai Silberman (Cisco), Andrew Small (BT)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098471247001dEKI
In today's digital age, reliable and secure wireless connectivity has become a critical component of business operations. However, managing complex wireless networks can be challenging, especially in critical environments. This session will explore how a proactive and AI-driven Managed Campus service can significantly enhance network performance, reliability, and security and align with the needs of current organisations. Leveraging Catalyst Center's robust automation, assurance, and technical intelligence capabilities, Managed Service Partners can deliver superior network services, accelerate service delivery, and improve operational efficiency, empowering organizations to achieve their digital transformation goals.

### Programmability Skills for Engineers Who Don't Want to Code - BRKOPS-1237
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098345132001d0g5
Are you tired of being told to learn Python? This session is for network engineers who focus on building and running networks. Programmability topics such as APIs, REST, data formats, and source of truth will be broken down from a network engineering perspective, allowing participants to better partner with their network automation peers. Useful tools and techniques that don't require coding and that participants can use immediately to validate network state and building configurations will be demonstrated. Programmability and automation are tools every network engineer can benefit from, even if you'd rather not learn to code. Strong networking teams require the network engineers and automation engineers to collaborate on projects together.

### Public Key Cryptography - From RSA and EC to Post-Quantum - BRKSEC-3129
Speakers: Frederic Detienne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098381966001dxGi
We will explain how public key cryptography works, what are the challenges posed by quantum computers and, ultimately, we will look into quantum-resistant algorithms. This session is industry-level. We will not focus on a specific type of product or application - instead, this is a general culture session meant to offer a solid basis into the jargon and technicalities of cryptography. The type of knowledge needed to take good decisions (or to delay decisions). Expect some maths to be displayed but mostly expect a lot of fun and enlightenment.

### Put the Cisco AI Assistant to Work: Getting Cisco AI Assistants to Work for You - BRKAI-1623
Speakers: Prashanth Arun (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161398900001N7n4
Generative AI is revolutionizing the daily experience of network and security administrators by automating complex threat detection, enhancing predictive maintenance, and streamlining security policy management. Cisco has been at the forefront of this change, launching AI Assistants for CDO (Cisco Defense Orchestrator), FMC (Firewall Management Console), CSA (Cisco Secure Access), Cisco XDR for SOC (Security Operations Center) as of July 2024. Cisco has also announced a Unified AI Assistant platform, enabling seamless interaction with all Cisco products through a single interface. Come, discover the technology and architecture behind the AI Assistants and how you can make it work for you. Discover how you can leverage the AI Assistant across Cisco's product range to enhance networking, security and SOC operations. Streamline your daily tasks with ease by accessing product information, uncovering new features, managing and updating configurations, generating reports, and troubleshooting issues - all using the Cisco AI Assistant. You'll leave this session feeling empowered and ready to make the most of Cisco AI.

### QKD Impact on Optical System and PQC Solution - BRKOPT-3086
Speakers: Maurizio Gazzola (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098360722001d3sU
The coming of Quantum Computing is placing a threat to current PPK implementation. Market is offering Quantum key Distribution as a possible solution. This breakout will show what are the implications for an optical transport network to Host Quantum Channels. We will also provide an overview about Cisco strategy focused on PQC.

### RADKit: Collect Data at Scale, Automate, and Expedite TAC Cases Securely and Efficiently - BRKOPS-3065
Speakers: Alex Honore (Cisco Systems, Inc.), Frederic Detienne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098358142001dr7w
Have you ever dreamed of reducing your workload on TAC cases by 80%? Having problems resolved effortlessly? Not being asked for yet another pesky "show tech" or support bundle? Or simply getting more value out of any service contract? Remote Automation Development Kit, or RADKit, is for you. RADKit is the new Cisco SDK used by Cisco Customer Experience (CX), including TAC and professional services, to securely and remotely manage or troubleshoot any type of device. With RADKit, you can manually and programmatically address your network through SSH, REST APIs, NETCONF/YANG, SNMP, web UIs, remote desktop, and more. In this session, we will introduce RADKit in depth: its architecture, security features, user interface, CLI, and API. Slideware will be reduced to the minimum necessary, and numerous live demonstrations will be provided. We will code on stage. These examples will help you understand the span of control of RADKit, its ability to tap into almost any data source, and how it can empower your network operations teams through automation and ready-made procedures. Multiple practical use cases will be shown, covering day-to-day management, troubleshooting, and remediation.

### Real-World Success Stories Powered by Cisco SD-Access! - BRKENS-1803
Speakers: Jacxine James Fernadez (BIAL), Kanu Gupta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098299255001dsT3
Join us for an exclusive session from global leaders across aviation, retail and manufacturing. Discover how these trailblazers are overcoming network challenges and setting new benchmarks in operational efficiency, security, and scalability-all while driving innovation and agility. Bangalore International Airport - Secure, Efficient Operations One of India's leading airports, handling 37 million passengers and 440 kilo tonnes of cargo annually, was an early adopter of SD-Access. Discover how they have achieved three years of stable, cost-effective operations with advanced segmentation, automation and an enhanced passenger experience. IKEA Industry - Facilitating Industry 4.0 Innovation IKEA Industry is transforming their 31 global production sites with Cisco SD-Access, enabling innovation through greater efficiency and scalability across the OT landscape by leveraging automation, secure segmentation, and visibility. BLUM Manufacturing - Programmatic Efficiency Driving automated network management through advanced programmability with Catalyst APIs, seamlessly integrating with third-party systems. Why Attend? This is your opportunity to gain valuable insights, proven strategies in deployment approach, and practical takeaways from industry experts. Whether you are focused on scale, security, or innovation, discover how Cisco SD-Access is enabling businesses to stay ahead in today's changing landscape.

### Redefine your AI/ML networks with Cisco Silicon One - AIHUB-1004
Speakers: Yaron Agami (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161391067001NxxV
The network that many organizations have used in the past for high-performance computing (HPC) cannot scale to meet the demands of AI/ML. As an industry, we must evolve our thinking and build a scalable and sustainable network for AI/ML. Cisco Silicon One is helping the industry meet rapid large-scale buildouts of AI/ML that networks. Power your AI/ML networks and configure the network to deploy standard Ethernet, enhanced Ethernet, or scheduled Ethernet to achieve best-in-class characteristics for each use case.

### Redefining Universal ZTNA: Security and Resilience for All Users and Things - CENSEC-1112
Speakers: Prabhu Barathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227081796001Jalw
In today's increasingly distributed IT environment with users everywhere and thousands of IOT devices to secure, you need the ability to efficiently enforce and monitor least privilege access. That's the original promise of Zero Trust, but why do so many projects stall out? We need to evolve our approach and acknowledge that to build an effective Zero Trust stance, your strategy must include all locations, users, and devices, and the network that connects them all. In this session, you'll learn about Cisco's Universal Zero Trust Network Access, our expanded approach that fuses networking and security to deliver unique value. Hear Cisco experts describe how this solution delivers granular security controls that can be enforced across both private and public traffic, how detailed identity attributes and contextual data can inform intelligent access decisions for users and devices, and how real-time performance data and new policy result simulation can drive consistent performance and avoid downtime. If you're looking to simplify your zero trust projects, this is the session for you.

### Reduce Alert Noise and Resolve the Issues that Matter Most with Splunk IT Service Intelligence (ITSI) - BRKOBS-1939
Speakers: Isha Gandhi (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098341204001dg3L
Drowning in Alerts? It's not enough to just keep your head above water, you need to find out how to turn off the tap and get your feet on dry land so you can find and fix problems faster. In this session, we'll dive deep into a wide spread problem: alert noise. We'll discuss how Splunk ITSI can help you address both your chronic alert fatigue, and how you can detect and triage incoming alert storms. Join us to learn how to filter out the noise, catch your breath, and more easily focus on keeping everything up and running.

### Reduce Risk of Your GenAI Investments - BRKSEC-1554
Speakers: Spencer Colemere (Cisco), Keith O'Brien (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161409961001NFFW
As organizations increasingly integrate generative AI into their operations, many do so without the robust security measures needed to navigate advanced cyber threats, compliance requirements, and ethical considerations. This leaves them vulnerable to data breaches, regulatory infractions, and reputational harm. A sophisticated, user-focused security solution is essential to ensure data protection, legal compliance, and responsible use. At run-time, when generative AI models are actively used, organizations face several critical risks. These include potential attacks on AI models leading to data theft, service interruptions, and model damage. Sensitive data may also be exposed during storage or training, raising privacy concerns. Additionally, models can be manipulated to perform off-topic, dangerous, or harmful tasks. Generative AI models can also respond with sensitive or harmful content, posing financial and reputational risks. For instance, data breaches can result in costly fines and loss of customer trust, while harmful outputs can lead to legal liabilities and brand damage. Cisco offers a comprehensive solution to mitigate these risks with robust security, privacy, and relevancy guardrails. Our technology monitors prompts and responses to identify and neutralize security threats, prevent data loss, and keep users on-topic and safe. Additionally, our solution allows organizations to measure and reduce the risk introduced by adopting generative AI. By implementing these security measures, organizations can confidently leverage generative AI, knowing their investments are protected against potential threats and vulnerabilities. This ensures data protection, compliance, and the responsible use of AI technologies.

### Reducing Enterprise Risk with Comprehensive, Continuous Intelligence and Asset Visibility - BRKSEC-1626
Speakers: George Panousopoulos (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098364248001dV9z
Discover how Splunk transforms asset discovery and compliance monitoring, redefining how organizations approach security investigations and risk management. Learn how to leverage existing Splunk data to build a complete, up-to-date asset inventory. Learn how to seamlessly leverage existing Splunk data sources to empower your security teams to quickly identify compliance gaps, effectively reduce risk exposure, and conduct more in-depth security investigations with accurate context.

### Reimagining Workplaces for All: Inclusive Spaces with Smart Tech Solutions. - IF-1685
Speakers: Giovanna Jagger (International WELL Building Institute), Alison Mackay (Cisco Systems, Inc.), Brian Tippens (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098456083001dE9M
As the future of work continues to evolve, companies must be primed to create environments that meet the needs of an increasingly diverse workforce. Join Cisco's leaders of real estate and social impact and inclusion as they uncover how the shifting generational expectations of today are being met through a blend of smart workplace technology and inclusive design. Drawing from examples of actual Cisco offices, this session will explore how to create environments that not only foster innovation and collaboration, but elevate accessibility, accommodate personal identity, and account for sustainability and personal wellbeing. Participants will walk away with valuable insights on how to harness technology to enhance comfort, productivity, and adaptability to create an inclusive future-proofed workplace.

### Resilient Networks: From Prevention to Recovery - BRKSPG-2695
Speakers: Marius Stoica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161416790001NI9d
In today's digital landscape, network uptime and performance are essential for business success. This session explores the critical components of operational excellence in network operations. Learn how to elevate your network from reactive to proactive by implementing best practices for software consistency, proactive audits, and intelligent automation. Discover strategies to optimize network performance, minimize downtime, and ensure business continuity through effective incident response and maintenance planning. By adopting an holistic approach to network management, you'll gain the tools and knowledge to build a resilient, high-performing network that drives business growth and customer satisfaction.

### Resolve Network Security Challenges with Tufin: Harnessing AI to Simplify Policy Management and Mitigate Network Exposure - PARENT-1407
Speakers: Erez Tadmor (Tufin)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098462986001dKbm
As enterprises embrace hybrid and multi-cloud environments, managing network security policies has become increasingly complex. Misconfigurations, regulatory pressures, and rapid infrastructure changes amplify the challenge of ensuring compliance and minimizing risk. This session explores how Tufin uses AI-driven insights to streamline security policy management, reduce network exposure, and tackle these challenges effectively. Participants will gain insights into: How Tufin's AI-powered capabilities simplify managing hybrid and multi-cloud security policies. Strategies to minimize network exposure while enhancing operational efficiency and compliance. Practical approaches to automate policy management, mitigate risks, and accelerate secure network changes. You'll leave this session with ideas to help you: Use AI to proactively identify and remediate network exposure points. Automate repetitive tasks and focus on strategic priorities. Adapt to complex regulations and dynamic environments confidently. This session provides actionable strategies to improve network security management using AI and policy-driven methods. Basic familiarity with network security and policy management concepts is recommended.

### Rethink Your Edge Routing Architecture - BRKSP-2275
Speakers: Emerson Moura (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161411073001NTxG
This session will look at industry and technology trends and discuss how they can be applied to design novel edge routing architectures. It will explore how the availability of high-performance, more power efficient silicon and router designs, paired with optics and automation software, opened the door to designing new edge routing systems that are simpler, more cost-effective, and future-ready, while delivering the rich services and strict SLAs that are required for value-added and business-critical services. The session will also discuss how this shift aligns with other trends that have been forcing the push of services edge functions closer to end users and applications. Together, these industry trends and innovations, can bring many technical and business benefits to service providers that are looking at modernizing their edge routing architecture for the long term.

### Revolutionize Customer Experience with Webex AI-Powered Innovations - PSOCOL-1796
Speakers: Vinod Muthukrishnan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098466524001dFRp
In the rapidly expanding AI landscape, organizations are faced with a plethora of options to enhance customer experience (CX). This session will reveal strategies for gradual AI adoption, focusing on areas that quickly maximize value for both customers and the business. Learn how Webex Customer Experience solutions enable organizations to create AI-powered, connected customer journeys across voice and digital channels. Join us to learn more on: Leveraging AI and automation at different points across a customer's journey How to achieve the right balance between assisted and unassisted support to boost contact center efficiency and CX outcomes The transformative potential of proactive communications and digital messaging.

### Revolutionize Your Data Centre with Cutting-Edge Solutions from AMD and Cisco - PARDCN-1256
Speakers: Ted Marena (AMD), Matt Foley (AMD)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098462238001dpUj
As the demands for modern data centers evolve, the need for scalable, intelligent solutions becomes more critical. During this session AMD, will highlight how the AMD product portfolio creates a unified, full-stack solution designed to match the complexities of today's data center challenges. We will be showcasing how our complete suite of products - from CPUs to GPUs - delivers fully programable cutting-edge performance. Join us and discover how together we can advance innovation.

### Revolutionize Your Network Management with Cisco Catalyst Center: Physical or Virtual on AWS or VMware ESXi - BRKOPS-2596
Speakers: Shai Silberman (Cisco), Sum Nguyen (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098355586001ds3p
Are you looking to manage your network infrastructure with Cisco Catalyst Center? Are you interested in learning how you can plan, deploy, and manage Catalyst Center as a physical or virtual appliance on AWS or your private cloud/data center in less than an hour? During this session, we will show you step-by-step how to: Choose the right Catalyst Center appliance for your network, whether it's physical or virtual Orchestrate the deployment of Cisco Catalyst Center VA on VMware ESXi Connect to your enterprise network and start managing devices and clients Understand the enterprise readiness features: HA, backup/restore, DR Manage the lifecycle of the Cisco Catalyst Center This session will include demos of orchestration applications that Cisco has created to bring up Cisco Catalyst Center VA on AWS and ESXi.

### Revolutionizing Communication: Harnessing Generative AI and Cisco Collaboration for Advanced Interactions - BRKCOL-2160
Speakers: Omer Ilyas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098282297001deFu
In this session, we'll demystify AI, setting the stage to explore how technologies such as machine learning and Large Language Models can enhance our daily digital interactions. We'll focus on integrating these AI advancements with the WebEx API, LLM models(chatGPT), and Langchain . This integration enables the creation of systems that understand and respond to natural language, significantly improving digital communication's efficiency and user experience.We will dive deep into the technical aspects of this integration, covering the basics, the architecture, and how we can overcome implementation challenges, and exploring effective solutions. Whether you're a developer, an IT professional, or simply fascinated by AI's potential, this session will provide valuable insights into making digital communication more intuitive and impactful. Additionally, we will showcase a live demo, highlighting the practical applications of AI in revolutionizing digital communication. Attendees will leave with a clear understanding of how to leverage AI models for enhancing digital platforms, equipped with knowledge to implement these innovations in their own projects.

### Revolutionizing Manufacturing: The Dawn of Industry 4.0 and Smart Factory Integration - BRKIOT-2720
Speakers: Paul Didier (Cisco Systems, Inc.), Arun Siddeswaran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098331582001dWMS
Dive into the digital transformation with our expert-led session, where we unveil the secrets of forging a robust, unified network that bridges plant operations with business prowess using the Cisco Connected Factory solution. Discover the blueprints of success with our Industry 4.0, Connected Factory Network, Wireless, and Security reference architectures. Gain insights into industry-proven best practices and engage with compelling real-world scenarios showcasing how to drive triumphant business results. This exclusive event is tailored for visionaries seeking to revolutionize control networks within manufacturing spheres and beyond. Join the architecture that transforms operational transparency, supercharges efficiency, and fortifies your enterprise with layered security. Step into the spotlight of innovation, empower your manufacturing landscape with Connected Factory architectures that illuminate your operational ecosystem, streamline your productivity, and solidify your defenses. Join us and become the architect of your industry's future.

### Revolutionizing Retail: Securing the Future of Retail IT with Cisco Meraki - PNLADV-1669
Speakers: Sabrina Winischhofer (Cisco Systems, Inc.), Simeon Solarsky (SAMSØE SAMSØE), Apurva Mehta (adidas AG)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1741803181748001jtrm
In the ever-evolving retail landscape, innovation and security are paramount. From sourcing to delivery, the need for a robust IT infrastructure that secures the supply chain and enhances customer experience is critical. Join industry leaders as they discuss Cisco's innovative role in transforming retail operations. This session will provide insights to help you: Implement cross-architecture solutions to secure the entire supply chain Utilize networking and observability to create a future-proofed workplace Monitor and optimize store performance through a single pane of glass, ensuring superior customer experiences

### SD-WAN Analytics for Optimized Monitoring and Predictive Networking - BRKENT-1552
Speakers: Anastasia Chaloulakou (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098305116001d2L3
In today's rapidly evolving IT landscape, the ability to effectively monitor and optimize network performance is more critical than ever. With the growing adoption of SD-WAN (Software-Defined Wide Area Networks), robust analytics are needed to gain insights and drive faster, better-informed decisions. This session will delve into SD-WAN Analytics, a state-of-the-art, cloud-delivered tool that is essential for network administrators and IT professionals today. Participants will leave this session with ideas to help them: Leverage advanced analytics from their SD-WAN data to optimize performance and reliability, while easing monitoring and troubleshooting tasks Utilize real-time data to enhance decision-making processes and network security Transition from reactive monitoring to intent-based and predictive networking

### SD-WAN as Code - DEVNET-1016
Speakers: Antonio Piepoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098427977001dsdI
Cisco Catalyst SD-WAN is designed to streamline the operational workflows and take the complexity out of network configurations. At the heart of this transformation is automation, a crucial element in the journey towards network simplification. In this session, participants will learn how to use the SD-WAN as a Code, a powerful automation framework based on Terraform, to configure the network 'as code.

### Saving Energy and Money with Your Cisco Wireless Network - BRKEWN-2043
Speakers: Simone Arena (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098317931001dOag
Learn how your Cisco wireless network can help accelerate progress toward your sustainability goals and potentially help reduce energy costs. Get answers to this important questions: Why does sustainability matter in networking? Why act now? How do I build an energy-efficient wireless network? Get to know Cisco's commitment to sustainability and what it means for you and discover how to start saving energy, emit less Co2, and reduce OpEx today.

### Scalable Meraki Access Switching - BRKMER-1415
Speakers: Brennan Martin (Cisco), Julie Nguyen (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098335505001dhLV
As network demands increase, don't let your switches become a bottleneck. Delivering continuous and resilient performance across sites requires pairing enterprise-grade switches with a powerful, cloud-native management platform. Whether you're intimately familiar with Meraki switching or just starting your cloud management journey, this session is your opportunity to catch up on the technical innovations that Cisco Meraki is bringing to switching. Participants will learn how all of these features streamline remote network management, how cloud management enables scalability and visibility across multiple sites, and you'll leave the session with ideas to help you ensure consistent, simple, yet powerful security across your organization.

### Scaling and Securing the Future: A Managed Service Partnership on Cisco Secure Networking - PSOMS-1782
Speakers: Alessio Valdez (Cisco), Juan Campillo Alonso (Telef�nica Tech), Francisco Torrecillas Gilabert (Cosentino)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098470703001dQHP
In today's rapidly evolving digital landscape, businesses are increasingly reliant on cloud technologies. This has driven a significant shift in managed services, evolving from basic infrastructure management to encompass advanced cloud networking capabilities. As organizations embrace cloud-native architectures and distributed workforces, the demand for Secure Access Service Edge (SASE) solutions has surged, providing secure and consistent connectivity across diverse environments. Additionally, the sophistication and frequency of cyberattacks continues to increase, demanding more robust security measures. This creates the need for organizations to adopt Security Operations Center (SOC) services to help protect their networks, applications and data from digital attacks. These services provide advanced threat detection, incident response, and security monitoring capabilities. In this session, you will hear directly from a Cisco MSP that adopted Cisco Secure Networking Solutions to address the challenges of today's digital landscape as well as from one of their end customers.

### Secure Connectivity Anywhere - The Evolution of Cisco Remote Access Technologies - BRKSEC-2057
Speakers: Greg Griessel (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098366043001dvQb
In this session, we will explore the evolution of Cisco's Remote Access technologies allowing organisations to secure their remote workforce. Remote work comes with its own inherent challenges such as an expanded attack surface, as well as the problem of managing the additional touchpoint such as the endpoints and the VPN concentrators where these sessions terminate . We will further explore how we can evolve from existing on premise self managed solutions to Cloud "SAAS" Services where there is no need to own, scale, upgrade the various touch points inherit to a traditional remote access VPN solution. Technologies that will be investigated include Cisco Secure Client, Cisco Secure Access as well as Cisco Secure Firewall. This session should interest new customers with a mobile workforce as well as customers already using Cisco solutions such as AnyConnect and Cisco ASA RAS VPN solutions.

### Secure Data Center in Record Time using Cisco to Automate, Deliver, and Validate Your Pipeline - BRKCLD-2731
Speakers: Jeff Comer (Cisco), Kelly Jones (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098278830001doHn
This session presents use cases and examples that demonstrate the value that Cisco programmability, automation, and full-stack visibility technologies bring to a traditional DevOps pipeline using open source like GitLab, Ansible, and Jenkins. Attendees will learn how to create a zero-trust data center infrastructure in minutes using Ansible and Python to deploy an ACI fabric, Nexus Dashboard to validate network changes before deployment, and AppDynamics to measure post-change metrics. Examples will also show how Cisco Network Services Orchestrator (NSO) anchors the pipeline and provides vendor-neutral, full lifecycle support with provisioning, managing, and assurance end-to-end. The session will also explore how integrating Stealthwatch into the pipeline provides continuous compliance and validation against a verified gold image.

### Secure Firewall in ACI - BRKDCN-2992
Speakers: Fabien Gandola (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098296382001d5fo
In modern data centers, it is crucial to be able to insert, deploy, and operate next-generation firewalls (NGFWs) as easily as possible. This session won't make you a service insertion ACI expert nor a Cisco Secure Firewall expert in just 90 minutes. Instead, this session aims to explain and demonstrate how Cisco Firepower Threat Defense (FTD) can offer more than just any NGFW in ACI. We will first introduce very quickly the necessary key concepts on ACI to insert an NGFW, followed by the shortest Cisco Secure Firewall introduction ever. We will then cover the most common ways to insert NGFW nowadays, focusing mostly on service graphs leveraging L3 PBR. Finally, we will hit the key part of the session with few a key points that FTD brings to the table: The advantages of leveraging clustering, especially in multipod deployments The role of dynamic objects in FTD and how they can help accelerate enforcement, especially if leveraged by Cisco Secure Dynamic Attribute Connector (CSDAC) Integration with Cisco Secure Workload using FTD, for both policy and virtual patching The ability to automatically remediate with the remediation module in Firewall Management Center (FMC) The session is targeted at customers who already using FTD in ACI and wish to improve their integration, as well as those interested in implementing ACI and looking to learn about FTD insertion capabilities.

### Secure Networking & Segmentation for Multicloud Architectures - BRKDCN-3930
Speakers: Brenden Buresh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098297630001d4ZL
This session will focus on how to design and build secure network connectivity and segmentation for multicloud data center architecture. First, we'll review best practices for single fabric and multi-site VXLAN designs. Next, we'll introduce the pivotal role the network plays to enable segmentation highlighting the tools and capabilities a VXLAN network fabric provides. Then we'll explore group policy and how this simplifies and extends security capabilities to address both north-south and east-west traffic flows in the data center. We will review how network-attached security devices integrate in data center designs to provide in-depth stateful security controls and address more stringent regulatory and compliance use cases. Then, we will expand beyond on-premises data centers to include connectivity to multiple public clouds leveraging SD WAN cloud onRamp for branch-to-cloud, DC-to-cloud, and cloud-to-cloud use cases. Finally we'll describe how to extend network segmentation integrating MultiCloud Defense to provide cloud-native enforcement controls for ingress and egress connectivity between VPCs, regions, clouds, and the Internet.

### Secure Operations for an IPv6 Network - BRKSEC-2044
Speakers: Eric Vyncke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098365329001d8Rq
Nowadays, IPv6 is in all networks as all hosts have IPv6 enabled by default. While network operators are experienced with secure operations in the IPv4 world, what are the specific challenges and techniques to be used to securely operate an IPv6 network? This session, by one author of RFC 9099, will present the main differences between IPv4 and IPv6 with respect to security, how to prevent attacks, what about extension headers, how to run audit and event correlation in a dual-stack network (from Data Center to wireless network).

### Secure Your Cisco Wireless Network with Identity Services Engine (ISE) - BRKEWN-2325
Speakers: Surendra Reddy Kanala (Cisco), Rasheed Hamdan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161403555001Nehz
Security is an important aspect in any pre-existing or new network deployment, and securing a Wireless Network can add an extra layer of complexity on top of that. This session aims to showcase the integration of Cisco Identity Services Engine(ISE) with 9800 WLC and leveraging its diverse set of features in order to secure access to the WLC, manage wireless users and secure their sessions and utilize the use of SGT's for network segmentation. ?

### Secure Zero Touch Provisioning (SZTP) with Cisco Catalyst Switches - DEVNET-1249
Speakers: Ashil Parekh (Cisco), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098431260001d6sD
Zero Touch Provisioning (ZTP) allows us to automate the deployment Cisco IOS XE and Catalyst platforms on enterprise and campus networks using the embedded CentOS "GuestShell" Linux Container and the Python and NETCONF API's to completely onboard, configure and manage network devices. This session details the ZTP and Guest Shell features and explores some common basic and advanced use cases. With the newest release of Cisco IOS XE, we now support Secure ZTP. This feature includes an explanation of the key components including conveyed information, the ownership certificate, and the ownership voucher. The setup configuration for Secure ZTP will be covered in this session.

### Secure the Wired Network using Identity - in Less than 60 Minutes! - BRKOPS-2584
Speakers: Matt Graham (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098355223001dTYS
Discover how automation can deliver 802.1x and Identity Based Networking without the headache. In this session, we will learn how to transform network operations, simplify switch configurations and deliver security in the wired LAN in some very simple steps!. Leveraging the power of Cisco Catalyst Centre and Identity Services Engine, this session will take an existing LAN switch deployment to the next level, ensuring visibility security and assurance are consistent and deployed correctly. Real time demonstrations will show how to enable 802.1x, Cisco TrustSec, Device profiling and posture checking in less than 60 minutes! This session will also highlight how the same result can be fully automated and deployed with Software Defined Access.

### Secure your Water Utility Operations with Cisco Industrial Threat Defense - BRKIOT-1968
Speakers: Evangelos Kostas (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098328753001dUAt
According to World Economic Forum, global freshwater demand will exceed supply by 40% by 2030, posing a significant pressure to European Water Utilities to keep their operations resilient against a growing landscape of cyber-attacks. Cisco's (OT) security solutions offer robust protection for European Water Utilities safeguarding their critical infrastructures while letting them continue digitizing their operations in an attempt to reduce water losses and increase water supply. During the session, it will be showcased how Cisco IoT solutions like Cyber Vision, can enable Water Utility Operators to gain insights into their network behavior and can quickly respond to anomalies or potential malicious OT attacks. Additionally, Cisco's Secure Equipment Access solution facilitates secure remote access to industrial assets for maintenance purposes, while reducing the environmental footprint of Utilities due to reduced onsite travelling. You'll leave this session with ideas on how these solutions can help you comply with NIS2 European Security Framework, ensuring that your critical systems will be uninterrupted by external Cyber-attacks while meeting stringent security requirements.

### Securing Endpoint Devices with Cisco Security Stack - BRKMER-2180
Speakers: Paul Fidler (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098336934001dlq3
Whilst many organisations, from schools, hospitals and enterprises, have their devices managed with an MDM (EMM) capability, many have not looked beyond the initial enrolment and provisioning. Devices tend to be left alone once in their intended role, and never looked at again. However, there are some simple steps that can be taken to ensure they are secure from day 1, and remain so. This session looks at how you can augment your managed device, whether this is with Meraki Systems Manager or another MDM platform, with tools from Cisco Security, including Duo, Umbrella, Secure Endpoint, as well as automating alerts when issues happen into your existing workflows.

### Securing Industrial Networks: Strategies and Best Practices - BRKSEC-2821
Speakers: Tilman Taubert (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098379070001dTw3
In today's rapidly evolving digital landscape, industrial networks (as used in OT) are becoming increasingly complex and interconnected. With the advent of Industry 4.0, the Internet of Things (IoT), and smart manufacturing, securing these networks has become a critical priority. This session aims to provide a comprehensive overview of the challenges and solutions in safeguarding industrial environments against cyber threats. Within this session, you'll learn how you can apply Zero Trust principles in an OT environment and which products can be used for this. You'll also learn how an integrated architecture can make a difference in the capability to identify, analyze and respond to threats in a proper and efficient manner. This session is designed for cybersecurity professionals, network architects, IT and OT managers, engineers, and decision-makers responsible for the security of industrial environments.

### Securing Industrial Networks: Where to start - using Cyber Vision for OT Asset Visibility - BRKIOT-2910
Speakers: Nicolas Deville (Cisco), Abubakar Maaroof (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098332645001dTVl
As industrial organizations embrace digital transformation and adopt industry 4.0 technologies, seamless integration between IT, cloud, and industrial networks becomes a game-changer, but with this innovation, comes new cyber threats that demand attention. Imagine having complete visibility beyond the Industrial DMZ - empowering you to understand your security landscape like never before, and take decisive, informed actions to protect your operations. In this session, discover how to turn your network into a powerful sensor, driving OT security at scale while seamlessly integrating with Cisco's cutting-edge solutions, including ISE, Firewall (CSDAC), XDR and Splunk. Don't miss the opportunity to transform your security strategy and stay ahead in today's dynamic threat environment.

### Securing Retrieval Augmented Generation (RAG) Implementations and the LLM Stack - AIHUB-2001
Speakers: Omar Santos (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161393150001NGU2
In the rapidly evolving landscape of AI, Retrieval-Augmented Generation (RAG) represents a cutting-edge combination of natural language processing and information retrieval, empowering AI to generate more informed and contextually relevant responses. However, as these systems become more integral to decision-making processes, their susceptibility to cyber threats and manipulation becomes a critical concern. This presentation goes into the unique security challenges posed by RAG implementations, including data integrity, privacy concerns, and potential vectors for adversarial attacks. We will explore a multi-layered cybersecurity strategy, including data validation, encryption, access controls, and continuous monitoring, tailored to safeguard RAG systems. Additionally, we will discuss ethical hacking techniques to identify and mitigate vulnerabilities, incident response frameworks tailored for AI systems, and best practices for developing resilient AI. Gain insights from the Cisco Security and Trust AI Research lead.

### Securing User to Application and Everything in Between - KDDSEC-1000
Speakers: Kirsty Paine (Cisco Systems, Inc.), Ambika Kapur (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227082914001J6BM
Cisco shines when security meets the network. Hear Tom Gillis, SVP/GM for Cisco Security, Data Center, Internet and Cloud infrastructure share how we are using the power of the network to deliver the most significant innovations in security and analytics in our 40-year history. Learn and see how these solutions are setting new standards in efficacy, resilience, and economics for zero trust access, data center security and firewalls, and security operations. Additionally, hear from Splunk's leadership on our collaborative efforts to revolutionize threat detection, investigation, and response (TDIR) to empower the SOC of the future. This is the keynote you won't want to miss!

### Securing Webex Meetings - Privacy, Confidentiality and Security Options for Meetings in a Virtual World - BRKCOL-2876
Speakers: Tony Mulchrone (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098285398001dnFG
Come along to this breakout session if you want learn more about Webex Meetings Security e.g.: How, as a Webex administrator, you can secure Webex Meetings for users in your organization How, as a Webex meeting host and scheduler, you can secure your Webex Meetings Security features and recommendations for Scheduled Meetings and Personal Meeting Rooms Deepfakes - Meeting participant identity and identity verification Blocking Recording Bots and unwanted users Webex Secure Meeting Types : Standard, Private, End to End Encrypt and the benefits and trade off of each meeting type Recently introduced features e.g. Block by domain Participant Label controls Upcoming new features: Webex 1:1 End to End Encrypted Calls Zero Trust Webex End to End Encrypted Meetings with support for Trusted On Premises meeting participants and services Post Quantum Cryptography

### Securing Your Workforce - IF-1613
Speakers: Scott Herpolsheimer (Cisco), Anand Raghavan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098455354001dVHC
The integration of artificial intelligence (AI) into business processes is not just an advantage - it's a necessity. This session will delve into how organizations can effectively harness AI to empower their workforce and enhance operational efficiency. Attendees will gain insights into our methodology for building AI capabilities across our portfolio and our culture, ensuring that AI becomes a seamless part of our tools and solutions through the lens of security. Join this session to unlock the full potential of AI and drive your organization toward a future of intelligent automation and empowered human creativity.

### Securing the Foundation: Optimizing Critical Infrastructure Resiliency? - BRKIND-1781
Speakers: Stephan Luhn (Cisco Systems, Inc.), Joshua Lieder (Universit�tsklinikum T�bingen)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098326980001dB0l
Healthcare is a vital part of society's critical infrastructure. It requires resilience like no other sector, as its ability to operate securely and reliably directly impacts lives. Accelerating digital transformation to improve healthcare outcomes calls for robust operational and cybersecurity strategies that can adapt to unique challenges in clinical environments. This session showcases a compelling customer success story from the healthcare sector, where Cisco solutions were implemented to create a secure, resilient network foundation. Attendees will gain insights into how these tools enabled shared visibility, automated threat responses, and seamless orchestration across IT and OT teams. The customer will share their journey of achieving operational excellence and compliance while fortifying their critical infrastructure-demonstrating how collaboration and innovation drive superior outcomes in healthcare. Join us to explore this transformative approach and learn how Cisco's solutions empower healthcare organizations to secure the foundation of their critical infrastructure.

### Securing the Olympics: The Cybersecurity Architecture for Paris 2024 - BRKSEC-2019
Speakers: Piotr Jarzynka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098364965001duar
The Olympics and Paralympics Games are the largest and most significant sporting events globally, necessitating an advanced and comprehensive cybersecurity framework to ensure their security and success. Designing a robust cybersecurity architecture for securing the competitions involved a holistic approach to protect against emerging threats. By focusing on governance, prevention, detection and response, the event was safeguarded against a wide range of cyber threats. Discover the advanced blueprint implemented during the Paris 2024 Olympics. This session highlights the lessons learned and best practices used. You will gain a deeper understanding of the architecture securing the Olympics and the technical solutions that protected the games.

### Securing your network against Quantum Adversaries. - CISCOU-1032
Speakers: Vinay Saini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098399976001dJBb
This session provides an accessible introduction to quantum computing, exploring its basics and the unique security threats posed by quantum-enabled adversaries. As quantum computers advance, traditional encryption methods, including IPsec and MACsec, face unprecedented vulnerabilities. Join us to understand the key security risks quantum computing introduces and learn how Cisco's quantum-safe solutions, such as quantum-secure IPsec and MACsec, offer robust protection to future-proof network security. Participants will gain insights into Cisco's strategies and solutions designed to keep data secure in a post-quantum world.

### Security Automation: Developing with Cisco XDR - DEVNET-1083
Speakers: Matt Vander Horst (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098428697001dNBD
Did you know that Cisco XDR has multiple ways you can automate your security operations and build powerful integrations? Integration modules allow you to bring data from other platforms into your investigations, APIs allow you to automate how you investigate and respond to threats, and XDR Automate allows you to build powerful orchestration workflows using a no-to-low code drag and drop editor. Stop by this session to learn more about each of these three facets of Cisco XDR and how you can use them to supercharge your security operations.

### Security Cloud Control 101: Simplifying Security Management Across Cisco Products - BRKSEC-1603
Speakers: Adam Bragg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098363885001dZE3
Join us for an introductory session to explore how Cisco's Security Cloud Control platform management is bringing together our security portfolio under one architecture, starting with securing data center capabilities. Discover how Security Cloud Control is bringing together our security management capabilities into a comprehensive platform, while providing a single administrative identity, common provisioning, common access, and other common services for security products. Join to understand the feature set, architecture, and future plans for Security Cloud Control and our platform capabilities. Learn how to get started, add your existing products, and manage users and roles - all with a single login. We'll also share what's coming next, including new integrations and features to help you stay ahead. Perfect for anyone looking to simplify their security management and get the most out of their Cisco tools.

### Security Journey of a Router: Design to Deployment & Beyond - BRKSPG-2868
Speakers: Rakesh Kandula (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161417179001NGFz
In today's dynamic threat environment with increasing attacks on networks, it's important to build a trustworthy network from the ground up and be able to maintain trust over the lifetime of the devices. This session presents the security journey of a Cisco router, starting from development, factory, deployment to production and beyond. A host of operational security features are presented that help maintain the same level of trust over the years. Most of the features presented will be based on IOS-XR routers but the same will apply to other Cisco products too. Counterfeit hardware is another major issue for operators and the session includes a demo on how users can verify the hardware identity at zero cost. In addition to the threats posed by current technologies, operators must safeguard the networks from future threats posed by Quantum Computers. The session will demystify the threat to various aspects of security from Quantum Computers and presents a roadmap to the future.

### Security for AI: Cisco AI Defense in Action - CENSEC-1801
Speakers: DJ Sampath (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228982412001T8Kt
AI apps bring new safety and security risks to enterprises. Cisco AI Defense solves these challenges by embedding our purpose-built AI security technology into existing network visibility and enforcement points in the Cisco Security Cloud. We'll show how AI Defense manages shadow AI use, identifies security risks in AI models and apps, and protects your AI apps in production.

### Security, VMware, and AI - Oh My! - PARSEC-1919
Speakers: Michael Hommer (NetApp)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098465437001d4nT
The pressures on IT are ever increasing and having to balance productivity, security, sustainability and innovation may seem like a no-win situation. Hear how Cisco and NetApp, through FlexPod, can reduce compromise and increase results with sustainability effective Zero Trust infrastructures, VMware optimization and modernization as well as Enterprise class AI.

### Seeing the Invisible: Integrating Splunk and Meraki for Large Scale Data Analysis - BRKMER-1887
Speakers: Mihail Papazoglou (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098336212001dQur
In today's data-driven market, the ability to harness and analyze data is crucial for gaining competitive advantages. Cisco Meraki devices generate a wealth of data that can be a goldmine for business, socio-economic or IT insights. This session will explore how, particularly large-scale customers, can effectively explore Meraki-generated data to drive meaningful outcomes that otherwise would be very complex, if not impossible, to gather. You'll leave this session with ideas to help you: Integrate Meraki data with existing analytics platforms, including Splunk, PowerBi, etc. to enhance decision-making Employ data visualization techniques to uncover trends and patterns This session is designed for IT professionals with an understanding of network architecture and basic data structures. No previous experience in software development or related is required. You will learn how to get the most of your Meraki dashboard, and transform your Meraki data into actionable business intelligence.

### Segment Routing Innovations in IOS XE - BRKENT-2520
Speakers: Jason Yang (Cisco), Sumant Mali (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098309398001dSPX
ASR 1000 and Catalyst 8000 Enterprise Edge platforms recently started supporting SRv6 capabilities. Segment Routing is a key capability desired by multiple network infrastructures today to establish end to end capabilities. High end Enterprise routing platforms have been supporting SR-MPLS capabilities for a long time with IPsec and NAT, Firewall, DPI services for edge deployments. IOS XE software is now getting uplifted with Segment Routing v6 feature set. The session will cover all availables tools and feature knobs to establish services capable Segment Routing edge presence and associated best practices in the form of IOS XE platforms.

### Setting the Stage for ISE Deployment Success: A Guide to Effective Planning - BRKSEC-2660
Speakers: Francesca Martucci (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098377224001dsNa
This session focuses on the preparation work that a customer should perform in order to ensure a successful ISE deployment. Like any technology, a deployment cannot be successful unless the proper planning and design isn't done first. We will examine best practices to follow in order to avoid some of the common pitfalls while preparing for an ISE deployment. At the end of the session, attendees can expect to have a better understanding of how to prepare their environment and their staff for an ISE deployment. This session is targeted at Network and Security Engineers, who are tasked in deploying ISE successfully.

### Sick of Wellbeing - IF-1156
Speakers: James Blair (Pavelka)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098454125001d2N4
Tired of the taste of turmeric? Suspicious of vitamin C? Ready to throw your Zinc down the sink? More than $18 Billion is spent a year on so called immune-boosting products, yet around the world, days lost to sickness are rising rapidly year on year. This entertaining, informative live session explores what the research actually says about boosting our immune systems, and how we can really reduce time lost to illness.

### Simple Leaf/Spine with a Touch of ToR - Network Designs for the Modern Data Center - BRKDCN-2667
Speakers: Brenden Buresh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098291838001dtOK
This session will step back and review the rationale behind building Cisco FEX and some of the deployment history in conjunction with virtual port channel (vPC) technology. We will review the predominant two-tier/three-tier data center designs that leveraged FEX with vPC and how those designs are now evolving to overlay based fabric buildouts. We will outline how the data center requirements are evolving to accommodate changing traffic patterns based on cloud operating models and how that's driving overlay fabric solutions. We will introduce VXLAN EVPN as the primary overlay fabric solution being deployed in the data center and how it's best suited to modern data center use cases. We will start with single fabric VXLAN EVPN designs and expand that to multi-site data center deployments where we are engineering for high availability, fault tolerance, and optimal performance characteristics.

### Simple VXLAN/EVPN Fabric Setup with Nexus Dashboard - BRKDCN-2929
Speakers: Marc Belle-Isle (Cisco), Christian Capitan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294046001d6kd
VXLAN provides network capabilities and architecture scale that is not possible with traditional VLANs. With expanded use cases and increased scalability come challenges in how to best deploy and manage VXLAN-based fabric networks. NDFC provides a deep and rich set of features to tackle these problems, providing automation and analytics that can drive efficiency and scalability. In this session, we will provide an overview of how NDFC can alleviate operational hurdles with the deployment of NX-OS fabrics. We will start with initially standing up a single fabric either as a new greenfield environment or integrating a preexisting brownfield setup in a very condensed timeframe. We will review creating a multi-fabric design, enabling external connectivity and providing layer 4-layer 7 service node stitching. We will explore configuration change control, snapshot, and rollback, and how we address compliance use cases. Finally, we will outline how intelligent analytics can be leveraged to provide advanced visibility and insights for day-to-day operations.

### Simplify Network Management using GenAI and Cisco Catalyst Center APIs - BRKOPS-3429
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098358507001dRdz
Are you looking for options to enhance and automate your network management workflows using Cisco Catalyst Center REST APIs? Do you want to simplify your network management experience using Generative AI, to use natural language to manage your network? During the session, we will review how to automate common, repetitive tasks using Catalyst Center REST APIs. We will step-by-step build an open-source platform that will complete typical network management tasks, while providing a Natural Language interface for the network engineer, or employees of your organization. The AI powered platform will perform input data validation, verify compliance with enterprise network management policies, and deploy configurations to network devices. We will review GenAI features like Retrieval Augmented Generation and vector representation, Function calling, Tool calling, and test results when using different LLM models. Prior experience with GenAI and LLMs is beneficial, but not required. Demos and complete solution sample code will be included.

### Simplifying Hybrid Cloud Complexity: Practical Use Cases on How Integrating DDI and Cisco Solutions Drives Efficiency - PARCLD-1417
Speakers: Peter Goodwin (EfficientIP)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098461679001d8KY
Hybrid multicloud adoption is accelerating, with 92% of organizations now using more than one public cloud. While this brings flexibility, it also introduces significant network complexity. In this session, you will learn why DDI (DNS, DHCP, IP Address Management) serves as the backbone of modern networks by consolidating network asset data and metadata into an extended, comprehensive Network Source of Truth (NSoT) across distributed infrastructures. You will discover through practical use cases how integrating your DDI platform with Cisco Networking solutions - such as Cisco Meraki, Cisco ACI, and Cisco DNA - enables robust end-to-end automation, increases agility, and improves operational efficiency. This session will equip you with strategies to reduce complexity across your SDN, SD-WAN, and hybrid multicloud architectures by streamlining your network operations through holistic visibility and automation.

### Simplifying Micro-Segmentation with Group Based Adaptive Policy - BRKMER-2164
Speakers: Andreu Mateu Torrello (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098336566001dX2l
As cyber threats grow more sophisticated, it is imperative to strengthen your organization's network security. Adopting a microsegmentation strategy effectively limits exposure by restricting the lateral movement of malware. This session will guide you through the best practices for implementing a cloud-managed operating model and illustrate how Adaptive Policy can be used to implement a zero-trust framework for your network. The session explores a case study with real-world use cases relevant to various industries featuring practical demonstrations, including initiating cloud management on Catalyst switches and dynamically assigning policies through Meraki Dashboard. You will also learn how to implement Adaptive Policy in hybrid environments, providing a comprehensive understanding of the cutting-edge cloud-managed microsegmentation solution.

### Simplifying Operations and Upgrades on Your Nexus Switch using Modular NXOS Software - BRKDCN-2639
Speakers: Samer Theodossy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098291472001d58N
This session will start with a discussion of the NX-OS overall system architecture and discuss upgrade procedures and best practices on Nexus switches for both the stand-alone and ACI product lines and what the best approaches are to take. Customers want ease of operations on their systems with Cisco software, and one of the biggest areas is upgrades and changing versions of software. Cisco's goal is to focus on best-in-class high availability. In-Service Software Upgrade (ISSU) is a major table-stake feature that requires coordination and patching. Customers want the ability to choose the software components based on deployment scenario and hardware they are using and there is a need to provide a more modular software to accommodate these goals and help bring lower memory footprint to Nexus switches. We will see how the Nexus architecture lends itself to the modular/optional design and will discuss how this helps with creating an NXOS software image that is more lean and provides a smaller memory footprint. In addition, this will lead to asynchronous delivery of features/fixes which can be deployed on the system. With the introduction of feature optionality, we will discuss how this provides the flexibility to remove unused RPM packages and how to install/uninstall an optional RPM package on the system.

### Simplifying Security Automation With Cisco Umbrella And Cisco Secure Access APIs - DEVNET-2325
Speakers: Oleksii Borysenko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098442484001d6by
Cisco Umbrella, a leading product in enterprise network security, adopts an API-first strategy that equips users to automate their daily security routines and proactively counter cyber threats, enhancing their network security capabilities. This session will enable the participants to: Play with Umbrella and Secure Access APIs in a sandbox to solve real-world use cases; Simplify DNS Policy Management With New Umbrella Tagging APIs; Programmatically manage API Keys; Improve efficiency and detect issues with the Umbrella API usage report;

### Sizing Compute Resources for Large Language Models - AIHUB-2659
Speakers: Rob Browne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161397724001Nl4R
This session will provide insights and guidelines on how properly sized compute resources for Large Language Models (LLMs) are essential for optimizing performance, managing costs, and ensuring scalability. This process involves selecting the right hardware components to meet the specific demands of LLMs, balancing efficiency and budget considerations. Understanding these requirements enables effective deployment and future-proofing of AI infrastructure.

### Small Part of a Big Team: Cisco Crisis Response at Natural Disasters - IF-1596
Speakers: Matt Runyan (Cisco), John-Henry Saxby (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098455177001dZPi
Private Sector plays a huge role in communications response to disasters and emergencies. Learn how a small group can have a big impact. Preparedness activities, both internal and external, close monitoring and situational awareness, quickly mobilizing resources, being responsive to requests, and implementing new ideas on the fly - we'll cover all of this and more. Including: How we responded to the floods of inquiries and offers of support How we mobilized people and equipment from all over the country How we implemented new approaches to cybersecurity in a disaster context How we manage equipment and resources We'll discuss the wins and challenges from an incident that hit, quite literally, close to home, and others that were farther away.

### Smart Building Maturity Model: Building a Roadmap to Real Estate Optimization - BRKGRN-2692
Speakers: Westley Thurley (Schneider Electric Limited), Andrew Lu (Cisco), Daniel Cope (Para), Jason Shearer (Cisco), Moto Shakoori (Ideal)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098326612001dUwv
The concept of a 'smart building is well established but existing implementations are often just the digitization of specific functional silos. Breaking through to the next level of what's possible for sustainability, occupant experience, and building automation will require a more comprehensive approach that breaks down these silos. What the industry lacks is a simple framework to assess and guide professionals in their evolution of real estate portfolio capabilities and performance for modern office environments. Cisco and other industry leading partners have developed a five-level Smart Building Maturity Model which provides a comprehensive framework to assist organizations in benchmarking their current state, setting improvement goals, and tracking progress. By defining levels of maturity, the Smart Building Maturity Model helps in prioritizing investments, optimizing building operations, and enhancing occupant experiences. Included in the analysis are domains critical to smart building operations: Energy Management Building Automation Data and Analytics User Experience Maintenance and Operations Security and Safety During the session, we will review SBMM scoring for existing offices and show how this framework can help attendees accelerate the benchmarking of their own facilities.

### Smart and More Sustainable Workplaces: Unlocking Value From Your Network - PARGRN-1437
Speakers: Sawar Khan (BT)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098464076001dSOV
Reimagine your network to enhance colleague experience, health, and sustainability. Discover how BT's carbon and energy tools and network design expertise are transforming workplaces for a low-carbon future, driving impactful outcomes that extend beyond the network.

### Solving Cyber Insecurity - BRKSEC-1159
Speakers: Martin Lee (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098362141001dFk6
The current threat landscape should not be accepted as normal, cyber attacks should not be accepted as an inevitable cost of business. Too many cyber attacks are affecting too many businesses. Nevertheless, there have been many improvements in cyber security over the past 30 years, and some clear opportunities for improving security in the near future. Although we can't expect to change the negative side of human nature, we can aspire to a world free from the burden of cyber insecurity. In this session, you'll learn the advances that we can reasonably expect in the medium term to help defeat cyber insecurity and the areas that are always likely to pose security risks.

### Solving DevOps and SecOps Challenges with Cisco Cloud Security - BRKSEC-1037
Speakers: Jatin Sachdeva (Cisco), Fabien Gandola (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098361780001dhdA
Have you ever witnessed DevOps and SecOps teams blaming each other for world hunger? In this session, Jatin and Fabien will acknowledge the main challenges that those teams are facing, such as managing vulnerabilities, deploying and operating security at the pace of Cloud native needs, providing an accurate view to the security team of the dynamic security state of their hybrid and agile application environments. More importantly you will be presented with solutions that can help both teams fulfill their respective requirements while working better together!

### Solving Global WAN Challenges with Multi-Region Fabric - BRKENT-2609
Speakers: Jean-Marc Barozet (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098309753001dSlS
Multi-Region Fabric (MRF) is a foundational capability of Cisco SD-WAN that underpins the journey to multi-cloud and SDCI. This major evolution of SD-WAN introduces new capabilities to support a truly scalable 2-level customer overlay, improve Cloud OnRamp for multicloud and expand managed service provider (MSP) solutions. The objective of this session is to provide a brief technology overview and to go over common/real-world scenarios/use cases/challenges/problems that customers encounter when rolling out an SD-WAN fabric with a global footprint. Enterprises and MSPs require a scalable, region-aware architecture. Some use cases MRF solves: connecting disjointed WAN transports in a given region, leveraging a cloud provider's backbone (AWS/GCP/Azure) to speed up connectivity to cloud-hosted workloads, leveraging an SDCI or Service Provider backbone to connect faster to SaaS apps and Cloud Providers, providing inter-region site-to-site connectivity between branches and how to scale out your data plane more easily at your regional hubs/colo/PoPs.

### Solving the Segmentation Puzzle with Secure Workload! - BRKSEC-2161
Speakers: Jorge Quintero (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098368585001dFbS
In a world of application workloads deployed anywhere, at any time, and with multi-cloud solutions, applying network security controls is no longer a trivial task. The policy control toolset just keeps growing, with multiple enforcement points in the network to protect our application workloads using different approaches such as the host firewalls, network firewalls and SDN controllers, or cloud-based in the form of security groups. With different teams managing each policy control and usually working in organizational siloes, there is no wonder why it often leads to inconsistent islands of policy controls across the environment. Secure Workload has been solving this puzzle, by defining a common policy model across all of these enforcement points (host-based, network-based and cloud-based) harmonizing all policy controls into an effective Zero-Trust Segmentation policy. This session will navigate through the Network/NetSec team lenses on how you can leverage Secure Workload to define a common policy model using agent and agentless approaches to protect your application workloads regardless of their form factor (baremetal, VM or container) or location (on-prem or multi-cloud).

### Splunk It Up: Turbocharge Your Network Monitoring with Cisco Meraki & Catalyst Center! - CISCOU-1039
Speakers: Kareem Iskander (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098402164001dIel
Unlock the full potential of network monitoring by leveraging Splunk to centralize and analyze data from Cisco Meraki and Catalyst Center. In this session, designed for technical network engineers, you'll learn how to install and configure Splunk, set up the HTTP Event Collector (HEC), and integrate it with Cisco Meraki and Catalyst Center via webhooks. We'll guide you through setting up alerts, ingesting network data, and utilizing Splunk as a unified monitoring platform. Whether you manage cloud or on-prem networks, this session will empower you with new insights and skills to optimize your network operations.

### Splunk Observability Cloud: Essential Insights for Cloud-Native Applications - PSOOBS-1936
Speakers: Greg Leffler (Splunk)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098471794001dRsH
Splunk Observability Cloud was built to monitor complex, microservice applications in real-time, across multiple cloud providers, all powered by OpenTelemetry. In this session, you'll learn what Splunk Observability Cloud is, what its capabilities are, and see how it can be used to solve a problem in minutes. We will cover Application Performance Monitoring, Infrastructure Monitoring, Splunk Synthetic Monitoring, and of course, the Splunk Platform for logging. See how these tools are integrated in one common workflow and learn about the out-of-the-box integrations with common cloud providers and applications.

### Stay Connected, Stay Informed: Splunk Meets Webex for Observability - CISCOU-2042
Speakers: Osama Hantool (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098409678001dm7u
In today's data-driven world, real-time observability is key to maintaining seamless communication and operational insights. This session will explore how to effortlessly integrate Splunk with Webex, enhancing data observability across platforms. Through a step-by-step guide, we'll demonstrate how easy it is to configure this integration, bringing Webex's data analytics into the Splunk environment for actionable insights, better correlations, and wider personas. Join us to discover how this integration can simplify workflows, improve team collaboration, and empower your organization with greater visibility and control.

### Stream ThousandEyes Data to Any Observability Platform using OpenTelemetry - DEVNET-2658
Speakers: Antonio Jimenez Martinez (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098446835001dgXC
In this session, we will demonstrate how ThousandEyes network telemetry data can be seamlessly exported and visualized on any observability backend, including Grafana, Honeycomb, Splunk, New Relic, Dynatrace, Elastic, and SigNoz. By leveraging the flexibility and power of OpenTelemetry, we will show you how to integrate ThousandEyes data with your preferred observability tools, enabling comprehensive monitoring and insightful analytics. Join us to explore practical use cases, see live demos, and learn how to easily enhance your network visibility and performance.

### Streaming ThousandEyes Data using OpenTelemetry - BRKOPS-1124
Speakers: Edwin Salazar (Cisco Systems, Inc.), Kyle Prins (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098344775001dZzv
ThousandEyes offers you a clear view of the digital experience, whether within your enterprise, over the Internet, in the cloud, or through SaaS, with no boundaries. It swiftly identifies issues in real time, significantly reducing MTTR and minimizing the business impact of network and application anomalies. ThousandEyes collects network and application data, correlates it, and presents a unified view of the end-to-end digital experience via web or API. ThousandEyes OpenTelemetry integration ensures data standardization and portability within the ThousandEyes platform, making it a seamless process for any OpenTelemetry-compliant vendor. In this session, we will demonstrate how to effortlessly stream your ThousandEyes data into other platforms such as Splunk and Grafana.

### Stretch Goals: Enabling High Performance Ethernet Connectivity Beyond 100 m - PARENT-1757
Speakers: Jonathan Dunbar (Leviton)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098463706001dBj7
Smart building technologies are transforming the modern workplace, leading to an ever-increasing number of devices being connected to the building's network. Some of these devices can be located more than 100 m away from the existing telecommunications room. Attempts to connect these devices using typical copper structured cabling may be initially successful, but there can be unforeseen performance consequences. Channels even slightly beyond the 100 m standard can suffer from high latency, low performance, and even service interruptions. In this session, you will learn about solutions and the required conditions to reliably achieve extended distances and select the right network infrastructure to assure performance as you stretch the limits of your installation beyond 100 m.

### Stronger Together: Cisco Secure Access and Duo Identity Security - BRKSEC-2455
Speakers: Tariq Bader (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098375068001doN2
In today's dynamic IT landscape, balancing robust security with seamless access to resources has never been more critical. As hybrid work models, BYOD policies, SaaS expansion, and multi-cloud infrastructures become standard, organizations face the challenge of ensuring strong security while maintaining a seamless user experience. Cisco Secure Access, a comprehensive Security Services Edge (SSE) solution, ensures secure access to both internet and private resources, regardless of user location. Cisco Duo, a pioneer in identity security and authentication, focuses on verifying user identity to ensure that only authorized individuals gain access, enhancing security without introducing friction. Together, these solutions create a robust security framework that strengthens Zero Trust principles and enhances the user experience. In this session, you'll learn: The architecture for deploying an SSE solution that focuses on identity security to strengthen Zero Trust and improve the user experience The added value and use cases of integrating Cisco Secure Access with Duo Identity Security, going beyond Single Sign-On (SSO) and Multi-Factor Authentication (MFA) Best practices for configuring and seamlessly integrating both solutions to maximize security and usability This session is ideal for security professionals, network security architects, IT security administrators, and anyone involved in remote access security, Security Services Edge (SSE), identity management, identity security, and Zero Trust initiatives and projects whether as technical decision-makers or influencers. It is also especially valuable for anyone currently using, implementing or evaluating Cisco Secure Access and/or Duo who wish to maximize their value.

### Stronger Together: Enhance your Threat Visibility with Cisco Security Solutions and Splunk Applications - BRKSEC-2133
Speakers: Zaid AlKurdi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098367482001dqzc
It is no secret that most networks require more than one security solution to provide sufficient protection. The result is a fragmented approach to security with multiple user interfaces that create blind spots to be exploited. Splunk Enterprise is one of the industry's best Event Management'solutions which works well with other Cisco Security Solutions and provides robust integration capabilities. This session introduces the participant to the latest Cisco Splunk Applications that can be used to integrate with different Cisco Security product, while highlighting the value and enhanced capabilities they offer. Using the Splunk apps for Cisco ISE, Secure Firewall, Secure Network Analytics (SNA) and Cisco XDR, an admin can quickly gain the context they need to assess and respond to security incidents and view key information about threats, high priority events, and IoCs.

### Succeed with Test-Driven Network Automation - Practical Examples Using Python and your Network's APIs - BRKOPS-2528
Speakers: Juulia Santala (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098354142001dwUD
How do you verify you didn't break your network when deploying configuration changes? The risk of breaking your network with misplaced configuration updates is amplified through automation - the more you automate your network, the more important it is to validate your network's performance. Let Python have your back: implement automated testing into your workflows! By utilizing the APIs of your network together with Python logic you can create test cases that cover different levels of your network verification - whether you have Catalyst, Meraki, or both in your environment. In this breakout, you will see practical examples and demos on how to plan and execute Test Driven Automation with real life solutions across products such as Catalyst Center, Meraki and ThousandEyes. The participant is expected to have a basic understanding of Python and REST APIs, but testing knowledge is not expected.

### Successful Migrations from Unified CM to Webex Calling - BRKCOL-2481
Speakers: Johannes Krohn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098283926001dOkz
Moving to Webex Calling offers benefits including reduced Opex, superior security, deployment flexibility, and scalability. In this session, we will discuss migration options from Unified Communications Manager to Webex Calling multi-tenant and dedicated instance. As part of a migration, users and devices need to be moved from the existing on-premises Unified Communications Manager, features need to be mapped and users need to be trained for the new experience. In this session, we want to highlight the main aspects of a successful migration and discuss migration strategies and interworking requirements. Finally we will give an overview of the existing options for bulk migration, automation using APIs and existing tools. Some experience with both Unified Communications Manager and Webex Calling, is a prerequisite.

### Successfully Configuring Cisco Catalyst 9800 Series Wireless on Your First Shot - BRKEWN-2094
Speakers: Federico Ziliotto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098318596001dUD8
Throughout this session, we will go through the first steps and best practices to bring up a Cisco Catalyst 9800 Wireless Controller in no time. From initial CLI/GUI access to AAA settings and recommended radio parameters, all the way through our first working WLANs. Remember the feeling of having forgotten some screws or bolts while building that Ikea furniture? This is the session which ensures nothing is left out when deploying a greenfield Catalyst 9800, or when reviewing and enhancing an existing setup.

### Sustainability Data Collection, Analysis and Management: Why, Who, and How? - IFGRN-1090
Speakers: Mary de Wysocki (Cisco), Colin Seward (Cisco), Wiebren van der Zee (ABN Amro)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098457165001dNUk
In the EU and other parts of the world, certain companies are required to publish regular reports on how their activities impact people and the environment. Meanwhile, customers are increasingly concerned about the environmental impact of the products they buy. Having accurate sustainability-related data is critical for both meeting reporting requirements and remaining competitive, but it can also help drive sustainability strategy and decision-making. Join two of Cisco's sustainability leaders and a sustainability reporting expert to learn about the complex and evolving reporting landscape, and hear how Cisco is addressing the challenges and opportunities it presents. During this session you will learn about the importance of accurate sustainability data, how a company can compile those datasets, and how they can be applied for multiple purposes to benefit your business

### Sustainable Product Design: How Designing with Sustainability in Mind can Help your Organization Meet its Climate Commitments - BRKGRN-1337
Speakers: Michael King (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098324787001d9sX
In 2018, the Intergovernmental Panel on Climate Change (IPCC)'s Special Report on Global Warming of 1.5�C was formally approved. It warned that the world must limit global temperature rise to 1.5�C above pre-industrial levels and reach net-zero carbon dioxide (CO2) emissions by 2050 for the best chance of avoiding challenging impacts on ecosystems, human health and well-being. Organizations in turn began making net zero Greenhouse Gas (GHG) commitments based on this 2050 timeline and began looking to reduce their carbon footprint through more sustainable product purchases. But what makes a product more sustainable? And how does it affect its carbon footprint and contribute to GHG reductions? At Cisco, we've created our Circular Design Principals to help guide our design teams on what steps they need to take to reduce the environmental impacts of our products and solutions. In this session, participants will learn how those principles are implemented and how these changes affect the carbon accounting at the product level and organizational level. This session is targeted towards anyone with an interest in sustainability and no advanced knowledge is required.

### Synchronizing 5G Mobile Networks - BRKSPG-3050
Speakers: Dennis Hagarty (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161417924001NAPK
This session will cover Cisco's approach to addressing stringent 5G timing and synchronization requirements. Timing and synchronization are critical components of an efficient mobile network architecture. If it is not properly designed, implemented, and managed, it can have a dramatic (negative) effect on the efficiency, reliability, and capacity of the network. Subscribers will likely suffer dropped calls, interrupted data sessions, and a generally poor user experience. Timing and synchronization standards are continuously evolving to address 5G and 6G RAN requirements. In this session, we will cover timing and synchronization performance requirements, ITU-T and IEEE standards, and overall deployment best practices with Cisco's Converged Transport architecture. The goal of this session is to clearly articulate Cisco's solution approach and product features to address 5G timing and synchronization requirements covering new standards and solution options as well as best practices for implementing reslient and redundant timing architecture.

### TAC and Engineering on Cisco Secure Firewall Threat Detection Performance - Performance Profiling tools, Tuning and Best Practices - BRKSEC-3274
Speakers: Foster Lipkey (Cisco), Costas Kleopa (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098382673001dc1C
Unlock the full potential of your network security with expert guidance at Cisco Live! Dive into the dynamic world of firewall optimization, where the mantra "set it and forget it" becomes a tale of the past. Join us for a compelling breakout session where we transform routine maintenance into a strategic advantage for your network's defense. Experience the thrill of mastering your firewall's performance as we equip you with insider knowledge on configuring threat detection, leveraging the collective wisdom of Cisco's TAC and Engineering teams. Discover the latest innovations that allow you to proactively identify and resolve performance issues with surgical precision. This session promises a treasure trove of real-world scenarios, showcasing the immediate impact of applying these tools and best practices. You'll walk away with a robust set of strategies to enhance your firewall's effectiveness and ensure it operates at the zenith of its capabilities. Key Takeaways: Embrace the most effective firewall performance best practices validated by Cisco TAC and Engineering Explore cutting-edge features that revolutionize monitoring and profiling, giving you a crystal-clear insight into your firewall's health Learn through practical examples how to seamlessly integrate these practices and tools into your security framework for optimal performance Join us for an interactive journey to elevate your firewall maintenance from routine to remarkable, and become the vanguard of your network's security at Cisco Live! Please note: This is not an introductory session. It is expected that attendees have deployed Cisco Secure Firewall using the Snort Threat Detection featureset.

### TLS Journey to Building AI Infused Capacities in the Integrated DC - PARAI-1323
Speakers: Plamen Staikov (IBM)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161423621001NWEd
The accelerating adoption of AI is transforming the IT landscape, and businesses need trusted partners to navigate this journey. IBM and Cisco, with over 25 years of collaboration, offer unique synergies to empower enterprises in their AI Datacenter, Secure Workplace, and Connected Business environments. This session will explore how our joint solutions can help you harness AI to drive innovation and efficiency across your IT infrastructure. You'll leave this session with ideas to help you: Leverage AI-driven strategies to enhance operational agility. Strengthen security and connectivity in AI-powered environments. Optimize your IT investments with IBM and Cisco's integrated solutions.

### Take the Easy Road to the Intersight API - DEVLIT-1490
Speakers: Chris Gascoigne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098423732001dooh
Everyone wants to reap the productivity benefits of programmability but sometimes the learning curve is too steep. In this session, you will learn how to utilise the power of the Intersight API without ever needing to write any code. The session will introduce the fundamentals of the Intersight API and demonstrate how to take advantage of it with tools such as isctl, an Intersight command line interface. The session will also demonstrate some common use-cases to level up your Intersight productivity. Programming knowledge is not required but an understanding of API basics and JSON/YAML will be beneficial.

### Taking ACI towards Lightspeed - DEVNET-2105
Speakers: Anvitha Jain (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098437439001dhBR
Experience unparalleled network automation with generative AI! Cisco ACI and Ansible Lightspeed combine to craft optimized playbooks for ACI, empowering admins to deploy robust playbooks swiftly. Achieve higher network automation levels, operational efficiency, and adaptability to changing business needs. Gain insights into creating reusable playbook templates using ACI's abstraction and Ansible Lightspeed's optimized performance, dynamic policy adaptation for agile network management, and cross-domain integration for end-to-end automation workflows. Unveil the secrets of writing Ansible playbooks for ACI like never before, witnessing a remarkable increase in efficiency. Unlock the true power of automation, propelling your network management to new heights.

### Taking Authentication to the Next Level with Duo Security - BRKSEC-2584
Speakers: Stefan Duernberger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098376136001dPiF
We are all looking for a secure and easy way to authenticate users when accessing applications. This intermediate session is about how Duo makes this process convenient and inherently secure. We will have a closer look at how Duo Passwordless works, a deeper dive into FIDO2 and recent enhancements such as Passkeys. In addition, we explore the latest product developments to get a deeper understanding of various AuthN flows supported by Duo Security. This session is targeted for Security Architects and Security Admins that want to get a deeper understanding about Duo Security and its role in a Zero Trust architecture.

### Teaching Coding Skills in the Age of AI - DEVNET-2720
Speakers: Brian Dietrick (East Carolina University), Erika Dietrick (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098448290001dyuq
Providing an effective and efficient developer education has long been a challenge, from upskilling an existing IT department to teaching university students relevant and practical development skills. Over time, industry standards have been created for how we educate, upskill, and evaluate developers. However, in the age of AI, what we thought we knew about teaching and assessing developer skills has been flipped on its head. How can we teach new developers to code when an AI assistant can generate it for them? How can we evaluate student assignments if we're unsure what code has been AI-generated? Attendees will leave with a proposed developer curriculum, new evaluation methodologies, and AI tool guidance from two combined developer perspectives: an early-in-career software engineer who re-trained into the field, and a senior software engineer currently teaching university courses.

### Techniques of a Network Detective - CISCOU-2035
Speakers: Fish Fishburne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098407547001dTc0
Just like detectives trying to solve crimes, the big picture techniques and mindset of being a great Network Detective are similar regardless of the actual specialty. This session presents an Introductory look at basic methodologies and approaches involved with being a Network Detective trying to solve a network "who done it" as quickly as possible. - Be Prepared - Find the Suspects - Question the Suspects - Improve

### The 525 program: a structured and mentored approach to become a CCIE in one year - CISCOU-1031
Speakers: Elizabeth Dafne Di Rocco (NIL)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098399614001dcmH
Cisco Certifications are one of the most recognized and respected in the IT industry. And among them, none is more coveted than the CCIE certification. The CCIE 525 program was created by NIL Learning in collaboration with Cisco to help candidates achieve their CCIE certification. One year of structured learning and practice labs with the help of CCIE mentors, will take candidates from the professional to the expert level and get them ready for the CCIE lab exam. The program has delivered on its goals with a pass rate of the CCIE lab exam above 50% on the first try. If you are an aspiring CCIE or seeking an expert level program for your organisation, join us to learn all about the CCIE 525 program.

### The Art of Designing ThousandEyes Alerts and Dashboards - BRKOPS-2076
Speakers: Dirk Woellhaf (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098350214001dGp1
Join this session to learn how to interpret, create, and design ThousandEyes alert rules and dashboards. Relevant examples and demos will also be shared. Having a baseline of traffic patterns is a must when you monitor your network, and maintaining a proactive and well-designed approach will determine if you are successful at it. Dashboards are the key to efficiently monitor network and application health, provide statistics, trends, and overall performance. Basic understanding of ThousandEyes is required.

### The Automation Travel Guide for Your IPv6 Journey - BRKIPV-2228
Speakers: Markus Harbeck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098334802001dcrj
Embarking on the journey from IPv4 to IPv6 is a major step in modernizing your network infrastructure, but it can be fraught with challenges and complexities. Know the technology is one but how can you start with automation and not just a boring IPv6 Project? This session, is designed for network engineers, architects, and IT professionals, it will delve into the power of automation in streamlining IPv6 enablement and migration processes. We will explore state-of-the-art automation tools with Infra Structure as Code (IaC) delivered via Services as Code (SaC) from Cisco Customer Experience Team (CX) that simplifies IPv6 deployment, from initial planning and address allocation to dual-stack implementation and routing protocol configurations. By leveraging automation, you can significantly reduce errors, ensure seamless operation, and enhance network security and scalability as well as prepare yourself towards the future. Key takeaways will include best practices for orchestrating a smooth migration, strategies for effective address management, and techniques for monitoring and troubleshooting throughout the transition. Real customer case studies will provide actionable insights into overcoming typical migration hurdles, showcasing successful implementations and the tangible benefits of a well-executed IPv6 migration strategy. Join us on this informative journey to empower your organization with the robust, future-ready capabilities of IPv6. Equip yourself with the knowledge and tools to automate your migration process, ensuring a seamless and efficient transition.

### The Complete WLAN Lifecycle with Hamina and Cisco Meraki - PARMER-1411
Speakers: Joel Crane (Hamina Wireless)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161425094001NKOx
In this session, we'll demonstrate (live!) using Hamina and Cisco Meraki together to perform a wireless network design, deployment, validation, and operation of a Cisco Meraki wireless network! We'll create a quick design in Hamina Network Planner, use Hamina's direct integration with the Meraki Cloud to deploy the network, perform a validation, and monitor the network with utilization monitoring and live heatmaps!

### The Coolest Cloud-Native DevOps Tools - CISCOU-2033
Speakers: Julio Gomez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098406833001dUVb
You are a network engineer and the network is there to provide connectivity services to applications. It is only natural you want to understand how app developers work, so you can provide them with the best possible experience. But the ecosystem of tools is huge... which ones are THE COOLEST? In this session we will go through some of them, and demonstrate how you can leverage those in cloud-native development environments. We will discuss the value of virtualisation and how modern tools like Telepresence, MirrorD and Okteto enable developers to have their local environment interact transparently with remote kubernetes clusters.

### The Difference Dimensions Make: Analysing High Dimensional Observability Data Sets - BRKOBS-2080
Speakers: William Cappelli (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098342293001dsMD
MELT data sets generated in modern environments are characterised by the high dimensionality of their contents (i.e., the large number of attributes required to distinguish data items from one another.) While this fact is widely acknowledged, far less appreciated is the reality that many traditional methods of statistical analysis crumble, in the face of high dimensionality, yielding results that are more or less meaningless or, worse, seriously misleading. There are, however, analytic techniques of recent vintage, that overcome many of the obstacles laid down by high dimensionality. These techniques ought to be understood and utilised by the practitioners of AI-enahnced Observability. In this presentation, the speaker will: explain in what sense Observability data is high dimensional and how that dimensionality undermines traditional modes of analysis outline some of the key techniques that can be used to manage and make sense of high dimensional Observability data discuss market trends shaping the technologies and products that support high dimensional statistical analysis

### The Engineer Experiences for Cisco Nexus HyperFabric - DEVNET-1454
Speakers: Lionel Hercot (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098433080001dxY7
In this session, we will go over the different user experiences that Cisco Nexus HyperFabric, Cisco's SaaS-based Data Center Networking solution, offers for Engineers managing it to best suits their needs. We will focus on the automation and programmability capabilities offered by the solution so you can find the right experience for your needs. We will cover experiences from API to Inventory-driven and much more. Join us for an exploration of HyperFabric automation capabilities and prepare yourself to get in the HyperFabric journey!

### The Era of Accelerated Reskilling - AIHUB-1002
Speakers: Annie Hardy (Cisco), Susan Mintz (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161390887001Ni9x
The race towards AI adoption isn't simply a technological one: upskilling and reskilling the workforce for AI is critical. Employees across the company need to understand what AI is, how it impacts their specific roles, and how they can responsibly adopt new Generative AI tools within their existing processes today. Join Annie Hardy, Global AI Architect, and Susan Mintz, Cisco Learning Leader, to learn about how Cisco is teaching and training 80,000 employees for the emergence of Generative AI. Leave with an understanding of how Cisco prioritized the human element of reskilling for AI, and where you can start your own reskilling journey.

### The Era of Accelerated Reskilling - CISCOU-1028
Speakers: Annie Hardy (Cisco), Susan Mintz (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098398555001dZth
The race towards AI adoption isn't just technological; upskilling and reskilling the workforce is crucial. Employees need to understand AI, its impact on their roles, and how to responsibly adopt Generative AI tools. Join Annie Hardy, Senior Visioneer, and Susan Mintz, Cisco Learning Leader, to learn how Cisco is preparing 88,000 employees for Generative AI. Customers will discover how to address the human element of AI introduction and reskill their workforce. This supports our focus on AI and establishes us as a thought leader with an industry-leading approach. We discuss industry trends and future vision, receiving great customer feedback on such presentations.

### The Flow of Things: Navigating and Properly Enabling NetFlow-based Solutions through Cisco Catalyst Center - BRKOPS-2038
Speakers: Nathan Lee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098348733001dAaQ
Application Telemetry and Visibility, Endpoint Analytics, Group-Based Policy Analytics--what do these have in common? They are all Cisco Catalyst Center (formerly Cisco DNA Center) solutions that rely on NetFlow/IPFIX to function properly. This session will present an overview of these solutions in both fabric-based (e.g. SD-Access) and non-fabric networks. More importantly, step-by-step guidelines will be provided on how to properly deploy them using Catalyst Center. Integration and implementation guidelines with Cisco security solutions will also be explored. Join us to learn how to enable valuable insights into your enterprise network and realize the maximum value that Catalyst Center can provide. To gain the most from this session, all you need is basic knowledge of NetFlow/IPFIX protocols and some navigational experience with Catalyst Center.

### The Future of Reskilling for AI - ITLGEN-1515
Speakers: Alex Pujols (Cisco), Annie Hardy (Cisco), Ryan Rose (Cisco), Rebecca Stone (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098460083001dZhT
To truly reskill a workforce takes more than online courses: it takes collaboration between teams, strategic pathways to evolving careers, and a learner-centered approach. In this conversation, Annie Hardy, Global AI Architect, will be joined by Rebecca Stone (SVP, Global Revenue Marketing), Par Merat (VP, Learning at Cisco), and Alex Pujols (VP, Global Partner Engineering) in a conversation that delves into the diverse ways Cisco has explored training 85,000 workers with increasingly important digital skills. Leave with a better understanding of divergent approaches that different teams are taking to reskill their staff, and with actionable next steps to take back to your own company.

### The Hitchhiker's Guide to Troubleshooting IPv6 - BRKENT-3340
Speakers: Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098312332001diAp
Are you about to deploy IPv6 in your enterprise network Afraid that you do not have enough experience yet? Don't panic. In this session, we will cover easy mistakes being made, the various states of an address, RA throttle host aAttachment, and we'll dig into Wireshark.

### The Hour of Networking - DEVSKL-1414
Speakers: Antonio Piepoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098451618001dRcT
Have you ever tried to explain to a child what do you do for living? Right... it's hard. This session will make your life easier! We will experience network automation from a different angle, we'll build a game to introduce children to networking! After this session, you will be able to schedule and deliver your own 'Hour of networking' with your community and start building a bridge between our daily job and our future generations. Join this session if you willing to see something different and if you want to play a role in child education.

### The Journey to Terabit Transport Solutions - BRKOPT-2019
Speakers: Maurizio Gazzola (Cisco), Lorenzo Ghioni (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098359620001dPrl
This session aims to describe how Cisco is leading the rush to the terabit transport era and how we are doing so by leveraging automation to make things simpler rather than more complex. The latest innovations with Open Line System (NCS 1010), WDM Transport (NCS 1014), and Digital Coherent Optics will be presented, along with some real-life examples of deployments that showcase our leadership in this space.

### The Latest in Cisco Secure Access (SSE) Innovation - BRKSEC-2285
Speakers: Neil Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098373274001d1sT
Join us for a closer look into the latest innovations happpening around securing access for all your users and applications. Cisco Secure Access is a cloud-delivered, unified secure service edge, offering a complete secure internet and private access solution. We will take a closer look at the newest innovations in the entire security stack and applications of the latest AI and ML capabilities to help secure access and streamline management. Whether your environment has roaming users, branch users, or both - Cisco Secure Access can help enable a unified, consistent security experience for administrators and users alike.

### The Lister Alliance - IF-1157
Speakers: James Clegg (Milton Keynes University Hospital NHS Foundation Trust), Chris Reeves (Cisco), Declan Hadley (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098454300001d1Bi
The Lister Alliance is a CDA funded project that aims at creating a network of NHS Trusts, practitioners, industry and academia to reshape the future of healthcare technology, creating better outcomes for patients. Through our Living Labs, the alliance demonstrates how digital technology meaningfully impacts healthcare outcomes, while supporting a resilient, adaptable, and sustainable NHS in the UK.

### The Network Whisperer: Ask Away, It's Got Answers! - DEVNET-2668
Speakers: Rohan Dev (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098447190001drv2
Cisco software-defined networks (SDN) have come a long way in ingesting, consolidating, and aggregating live statistics from network infrastructure - making life significantly easier for NOC teams daily. However, I can show you how LLMs can make sense of seemingly 'jargon-ish' Cisco SDN-generated insights in natural language and even orchestrate automated workflows via DevNet's RESTful APIs by issuing commands on Webex. This will be a practical application of AI that can unlock the true capabilities of managing end-to-end networks from centralized software controllers, and democratizing network operations across all job functions.

### The Network of the Future is Here - Let's Automate your IPv6 deployment with Python! - BRKOPS-2223
Speakers: Juulia Santala (Cisco), Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098350921001dupG
IPv6 marks a new horizon in the world of networking, promising limitless IP addresses and enhanced network performance. It is time to embark on this journey - but let's do it the right way from the beginning: using automation! In this 90 minute breakout you will learn how to plan your IPv6 transition and how to use Python to automate setting the plan into action. You will learn about the must knows of IPv6 as well as useful Python libraries that can help you on this journey, and see practical real life Python examples of deploying IPv6 configurations in your network. Workflow decisions such as automated testing and sources of truth will also be covered. This session is designed for network engineers who have a need to start implementing IPv6. The session's target audience has little or no prior experience with Python automation and is fairly new to IPv6 as well.

### The New Digital Substation - more efficient, more secure and ready for demanding modern Grid applications - BRKIOT-2015
Speakers: Elena Maria Leidinger (Cisco), Marcus Smith (Cisco), Frank Tuhus (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098329142001dhNN
The new Substation Automation solution architecture overhauls the substation network to drive out costs, improve security and support demanding new SmartGrid applications while reliably providing control and visibility of substation operations. In this session, we will review the updated network and security architecture enhanced with new industrial routing (IR8300) and switching (IE9300) infrastructure, running industrial cybersecurity with Cisco's Cyber Vision, support of multiple WAN options including SD-WAN and deploys software defined network management with Cisco Catalyst Center (formerly Cisco DNA Center) and vManage to reduce maintenance effort, increase uptime and simply and consistently deploy the network. The solution has rich cybersecurity features such establishing an Electronic Security Perimeter for critical substation systems, deplloying TrustSec-based micro-segmentation, and the visbility of substation devices and protocols with Cyber Vision.

### The New, Encrypted Protocol Stack Taking over the Internet and How to Deal with It - BRKSPM-2024
Speakers: Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161419037001N347
Network traffic is transitioning from TCP to QUIC very fast, QUIC being 50% of total traffic and doubling every 18 months. QUIC, with HTTP/3, DoH, and eSNI/ECH, obfuscates the traffic between applications and changes flow behavior with applications now disintermediating the network. Application visibility is eliminated by this stack, congestion management transitions to the application and the key assumptions SP networks are built on are rapidly being obsoleted. In this session, we will show how this protocol stack is constructed and evolving, its behavior in terms of both visibility and flow control, and the impact it has on infrastructure elements. We will also discuss the techniques SPs can use to keep pace with it, enabling better traffic visibility, QoE, and efficient use of 5G spectrum and other scarce resources.

### The Power of Extending SD-WAN to OT Networks - PSOIOT-1016
Speakers: Jenifer Piccioni (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098470340001dvEy
SD-WAN can make it easy to unify your management and security across the enterprise and operational edge. Whether it's traffic intersections, utilities substations, windfarms, and more - with Cisco IIoT, businesses can achieve greater visibility, control, and efficiency in their industrial operations, while reducing downtime, and improving safety. If you are using Catalyst SD-WAN in the enterprise, it's a small step to extend to the industrial space with our Catalyst industrial routers. Come and see how this shared management experience delivers the robustness and simplicity you need to easily and securely manage your IT and OT networks as one.

### The Risk Managed Revolution: Don't Fear Change - PSOSEC-1083
Speakers: Ant Ducker (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098471998001doNU
In many organizations, planned changes to the network or applications often lead to faults or issues. To prevent this, there's a thorough change management process in place where those responsible for the changes must prove to a review board that their actions won't result in downtime or problems. Change review boards can take up a lot of time, and ultimately slow down the rollout of new applications or features. Cisco Hypershield can transform your change management processes by providing solid proof that a change is safe and won't lead to any business disruptions or unexpected faults.

### The Role of Observability in Cloud Native Applications: Ensuring Reliability and Minimizing Downtime - BRKOBS-2937
Speakers: Greg Leffler (Splunk)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098343714001drEU
Cloud-native applications are different than traditional applications, and need to be monitored and observed in a different way. As more workloads go to the cloud, organizations realize that it's harder than ever to really understand what's going on in these applications, thanks to the complexity of modern application design. In this session, you will learn why cloud-native applications need observability, the value of real-time monitoring, tracing, and logging, and how you can proactively identify and resolve performance issues to build better digital experiences. Finally, you'll see a demo of Splunk Observability Cloud and see how this tool can help solve issues in minutes, even in complicated environments.

### The Science of Stress - IF-1159
Speakers: James Blair (Pavelka)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098454655001djzD
We all know the effects of stress and the things that stress us, but what biological processes underpin our feelings of tension and feeling overwhelmed? In this interactive session, share and vote on the things that get you down, and explore the science behind them before getting a taste of our easy to implement activities that can be used to lower stress impact on your life.

### The Small Branch ISR: More Powerful Than You Think - BRKENT-3482
Speakers: Ashton Williams (Cisco), Abhishek Keswani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098312690001dXg7
Discover how the ISR 1000 series can transform your small branch office into a powerhouse of connectivity and security. In this session, we delve into the ISR 1000's robust features and solutions designed to solve your business challenges. Participants will learn how to configure the ISR 1000 series in SD-WAN for: Dual active WAN - Connectivity with ethernet and cellular options, ensuring seamless redundancy Security - Configuring the next generation in-built firewall and secure group tagging, ensures that your network remains protected and easily managed Application and Monitoring - Experience top-tier performance with embedded Wi-Fi 6, Geofencing, ThousandEyes integration, and TCP Optimization. For non-SD-WAN/traditional routing participants will learn how to: Simplify and optimize licensing Adapt to changing connectivity needs with layer 2 to layer 3 port conversion Seamlessly integrate VoIP phones with unified communications Power cellular gateways, access points, and VoIP phones efficiently with PoE support All these capabilities are delivered with excellent performance for small branch offices Explore SD-Routing deployments for a traditional routing network and how it can be seamlessly integrated into the SD-WAN Manager dashboard All these capabilities are delivered with excellent performance for small branch offices.

### The Software-defined Factory Enabled by SDA - BRKIOT-2299
Speakers: Thomas Kampa (Audi AG), Erika Franco (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098330195001dqOz
This presentation explores the application of Software-Defined Access (SDA) technology in industrial automation environments. It aims to provide a comprehensive understanding of when SDA is a suitable choice, its limitations, and practical guidelines for deploying SDA in industrial automation networks. The session will feature Audi, showcasing their innovative approach to virtualizing Industrial Automation and Control Systems (IACS) hardware. By leveraging hyperconverged infrastructure and SDA, Audi is creating efficient virtual environments that connect seamlessly to the plant floor. We will cover: Common Deployment Models Industrial Network Management with Catalyst Center Operational Considerations Known limitations Audi Use Case By the end of this session, you will understand how to introduce SDA in manufacturing and gain a clear vision of what the factory of the future could look like.

### The Top 10 Glass Table Design Tips to Enhance your Observability Practice - BRKOBS-2892
Speakers: Stephane Estevez (Cisco Systems, Inc.), Henning Gehrts (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098343362001dKSb
You have a powerful data platform like Splunk (or any other) that generates powerful dashboards? It generates critical KPIs but still... your management barely looks at it. Join this session to learn about the 10 principles for effective data visualization and dashboard design on glass tables and dashboards. It discusses choosing the right visualization for different types of data, using colors and fonts effectively, following principles of visual hierarchy and proximity, leveraging diagrams and flows, and using alerts and a dramatic approach when needed. It also recommends starting with paper prototypes, using simple tools like PowerPoint, and following current design trends like flat and minimalist styles.

### The Value of the CCNA for EVERY Engineer - Yes that Means You! - BRKCRT-1004
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098288300001drLc
In the ever-evolving world of technology, it's crucial for engineers to stay ahead of the curve and possess a diverse skillset to thrive in the ever-changing landscape. While specialization is essential, the ability to understand and interact with networking fundamentals is a valuable asset across all disciplines. This is where the Cisco Certified Network Associate (CCNA) certification comes into play. The CCNA certification is the industry standard for networking fundamentals, providing a comprehensive understanding of networking concepts, protocols, and technologies. Whether you're securing the network, enabling collaboration or just living the cloud the CCNA can provide you with knowledge to make you a more well-rounded engineer.

### The latest innovations in Cisco Secure Access (SSE) - CISCOU-2040
Speakers: Jonny Noble (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098408978001doTy
Join this session for a closer look at the latest innovations in Cisco Secure Access, including our leading ZTNA client-based and clientless capabilities, simplified policy management, and a unified client that removes the frustration of secure connections for your hybrid workforce. The session will dive into details of innovations such as value-added incremental features, integrations, AI-based innovations, and other differentiation that have been provided to Secure Access customers over the last few months.

### Think Like a TAC Engineer: A Guide to Cisco Secure Firewall most Common Pain Points - BRKSEC-3533
Speakers: Ghada Ayman Hijazi (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098383391001dZut
Tired of struggling with troubleshooting firewall issues that might hinder your daily tasks and activities? Cisco Secure Firewall is one of the most critical security controls in the modern network. Managing and troubleshooting potential issues is critical to ensure a stable and efficient network. The purpose of the session is to familiarize admins with the troubleshooting methodology for the latest, day-to-day, most common Firewall issues. The examples and use cases provided during this session are from real-life customer scenarios that were handled by Cisco TAC. By the end of the session, the attendee will have knowledge of the most recent common issues and should be able to troubleshoot and if possible, fix them before reaching TAC.

### Think Like a TAC Engineer: Troubleshooting Secure Client Remote Access Issues - BRKSEC-3935
Speakers: Tomasz Kmiec (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098384098001dZii
Have you ever struggled with troubleshooting Remote Access? Have you had an issue with isolating or resolving such problems? The Secure Client (formerly AnyConnect) is one of the most popular Remote Access solutions that can be deployed on multiple platforms. The purpose of the session is to familiarise you with the troubleshooting methodology from the time when a connection is initiated until the tunnel goes up and forwards the traffic. At each step of the connection flow, common problems and relevant troubleshooting tools will be presented. Examples of troubleshooting control and data plane issues come directly from service requests that the Cisco CX (TAC) has solved. Join the session and think like a TAC engineer.

### ThousandEyes and Splunk - Better Together - BRKOPS-2167
Speakers: Todd Anscombe (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098350565001d3eg
Today operations are siloed, with tools focused on network performance or application performance. Furthermore, each operations team works to provide a measurement of their respective innocence because they lack the end to end visibility of a user experience. With ThousandEyes, operations is able to provide a user context over network, server, and application performance. Additionally, with our ability to stream network telemetry from ThousandEyes into your investment in Splunk, you are now able to correlate security events, with network and server performance measurements. Additionally with Splunk observability, you can build a comprehensive view of the full stack, starting at the application, and working through to the network and server performance supporting the application.

### Traffic management with a Service Mesh - CISCOU-2034
Speakers: Julio Gomez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098407189001dAlO
You are a network engineer and the network is there to provide connectivity to applications. It is only natural you want to understand the kind of services app developers really need. This session will cover the practical benefits of a service mesh and its traffic management capabilities for microservices-based applications. You will be able to implement real use cases, like gradual traffic migration to new service versions, fault and delay injection, or traffic mirroring.

### Transform your Network Automation Apps with GenAI - DEVNET-3419
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098450275001dnlT
Are you looking to simplify network management using Cisco Catalyst Center REST APIs and Generative AI, to transform your existing network automation Apps? Participants will learn how to innovate, enhancing existing Infrastructure-as-Code apps using Generative AI, to transform and simplify network management. We will review existing common use cases that calling Catalyst Center APIs and how to take advantage of Generative AI transformative capabilities. The session will start by introducing the audience to AI code generation capabilities, using the Python SDK and Ansible playbooks for Catalyst Center. The second part of the presentation will review Function Calling and how to create a Natural Language interface for your existing network automation workflows. The use cases will explore the options to use Cloud based or on-prem LLM models. Demos and Python sample code are included.

### Transforming Data Center Security: Innovations, Partnerships, and Real-World Solutions - CENDCN-1738
Speakers: Yousuf Khan (AMD), Murali Gandluru (Cisco), MEHMET DURMUS (TURKCELL ILETISIM HIZMETLERI A.S.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227080268001Jsz2
As data centers become the backbone of modern business operations, securing these critical infrastructures is more urgent than ever. In this session, we will explore the rapidly evolving landscape of data center security. Discover how Cisco is leading the way with innovative solutions that tackle these challenges head-on and learn how our strategic partnership with AMD is turning visionary concepts into practical, scalable security strategies. Together, we are empowering businesses to protect their data, ensure operational continuity, and build resilient infrastructures capable of withstanding future threats. You?ll hear directly from a customer who is navigating these challenges firsthand, sharing insights on the latest security strategies and a real-world use case. This session offers a unique opportunity to gain actionable insights from industry leaders and learn how to transform your own data center security strategy.

### Transforming Enterprise Infrastructure as Code: The Foundation of Unified Enterprise-wide Automation and AIOps - PSOCX-1799
Speakers: Jesse Reed (Cisco), Michael Kaemper (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098467242001dDZB
Join us for an illuminating session where we delve into the transformative power of automation in the AI era. Discover how industry leaders are revolutionizing the management of networks, data centers, and security infrastructures with AIOPs and treating them as software code. how you can apply advanced DevSecOps methods to enable efficient provisioning, configuration, change, testing, and deployment. With Cisco's Services as Code and Network APIs, transcend traditional approaches and go beyond into a future dominated by AIOps and comprehensive automated infrastructure management. This session is designed to furnish you with the knowledge and foresight necessary to elevate your operational agility, enhance quality, and fortify security.

### Transforming Network Operations with Closed-Loop Automation using AI Insights - BRKOPS-2814
Speakers: Christopher Beye (Cisco), Joerg Schultz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098356687001dNNw
The need for reliable and advanced automated networks is increasing due to the rise of agile applications and complex, distributed infrastructures. While network controllers and Infrastructure as Code (IaC) are usually domain-specific, organizations use cross-domain workflow orchestration tools to align business intent with network-wide changes. These tools trigger CI/CD pipelines across different domains to manage network components for their business services. The goal of this breakout session is to showcase how closed-loop automation is used to provision, self-diagnose, and dynamically update intent-based networks. This session will highlight the tools and design principles of how closed-loop automation can be implemented. Participants will witness the integration of AI-driven solutions for proactive troubleshooting, showcasing how these technologies work together to reduce downtime and enhance operational efficiency.

### Transforming Service Provider Networks: Spotlight on Simplicity, Reliability and Service Readiness - CENSPG-1017
Speakers: Joan Garcia (Colt Technology Services), Mattias Fridstrom (Arelion Sweden AB), Bill Gartner (Cisco), Gurudatt Shenoy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739228982583001T9Ny
The service provider landscape is rapidly evolving, with providers grappling with the challenge of managing increasingly complex networks while ensuring secure, scalable, and resilient connectivity for their customers. At the same time, they are seeking monetization opportunities through new services, including those enabled by AI. Discover how Cisco's latest solutions are helping service providers simplify their networks, enhance agility for future service delivery, and boost operational efficiency through automation, assurance, and AI-powered insights.

### Transforming Workforce Dynamics: Cultivating Leadership Skills in the Age of AI - CISCOU-1029
Speakers: Shannon Woo (Cisco Systems, Inc.), Dr. LaTricia Frederick (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098398904001dzMo
We invite you to join this exciting fireside chat session with Dr. LaTricia Frederick, Cisco Exec & Board, and Shannon Woo, Senior Leader Employee Development. You will learn about how we embrace, elevate, and LEAD in the era of AI and get a behind the curtain view of how Cisco is transforming workforce dynamics through essential AI-ready leadership skills. This session will enlighten you on how we cultivate talent, lead from the front, and foster a growth-oriented organizational mindset. Participants will gain valuable insights into developing visionary leadership, becoming the cultural architects and change agents that set you apart and excel with unprecedented speed. AI is the new toolbox that can help leaders thrive.

### Transition to a New Hypervisor & Build AI Infrastructures Simultaneously with Red Hat OpenShift and Cisco UCS - BRKCOM-2214
Speakers: Boris Aelen (Cisco), Michael Hrivnak (Red Hat)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098287390001dFkT
Three big disruptions in our IT sector are all coming together; Application modernization by containerization Finding VMware alternatives Building AI infrastructure Red Hat OpenShift is the platform of the future that runs all virtualized, containerized and AI workloads! Now is the time to learn about OpenShift and the best server platform in the world to run it on, Cisco UCS with Intersight. This session is delivered by Red Hat and Cisco together and demonstrates how to deploy and operate OpenShift Container Platform with unique integrations between Red Hat and Cisco. We focus on the technical capabilities from both platforms that will simplify your daily operations and help you deploy a secure and future proof compute platform to run your existing virtualized workloads. This session is specifically built for VMware admins to learn about OpenShift Virtualization but will prepare you for running containerized and AI workloads in the future.

### Troubleshoot Cisco Catalyst 9800 Wireless Controllers - BRKEWN-3628
Speakers: Nicolas Darchis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161406995001N2sb
This session covers troubleshooting tips and tricks when working with Cisco Wireless. From Cisco Catalyst Center (formerly Cisco DNA Center) Assurance, to the Cisco Catalyst 9800, and the Catalyst Access Points themselves. Learn where to look and what to look for, for most common issues.

### Troubleshooting Segment Routing - BRKSPG-3624
Speakers: Luc De Ghein (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161418669001N8XN
This breakout session on troubleshooting'segment Routing (SR) covers troubleshooting the basic deployment scenarios, such as control plane and data plane troubleshooting with basic SR, SR policy, and Ti-LFA, both for SR-MPLS and SRv6. The session also covers some'troubleshooting examples. The requirement is that you have a basic knowledge of segment routing prior to attending this session. While many topics covered in this session are operating system agnostic, only IOS-XR will be covered.

### Troubleshooting UCM Calling in the Webex App - BRKCOL-3818
Speakers: Philip Smeuninx (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098286646001dxbm
The Calling in Webex (Unified CM) solution lets you register Webex directly to your Cisco Unified Communications Manager call control environment. Join me for this session where we will review commonly seen mistakes and issues within a Webex UCM Calling solution during deployment and operations. You will gain insights on how to troubleshoot and resolve these, what tools are available and increase your knowledge on the technologies enabling this solution. After this session you will be better equipped to successfully deploy and operate UCM Calling in the Webex app.

### Troubleshooting Webex Authentication and Provisioning - BRKCOL-3117
Speakers: Paul Stojanovski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098286292001d6pG
Webex administration is continually evolving. If you're thinking about deploying Webex, growing it, or are interested in avoiding a call to TAC, this session will help you understand the most common pitfalls customers run into when managing Webex. The content will be based on the most common challenges customers face when opening TAC cases around the following topics: Directory integrations such as Directory Connector and Azure AD Sync (includes understanding troubleshooting approach, available logs, and sync issues) Group synchronization issues and migration challenges Single sign-on configuration issues and certificate updates (includes understanding a SAML assertion, SSO auth flow, and login issues)

### Troubleshooting the Cisco Catalyst 9000 Series Switches - BRKTRS-3090
Speakers: Michel Peters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098394940001dbKO
This session covers troubleshooting of the Cisco Catalyst 9000 series hardware and the Cisco IOS XE operating system that powers it. It demonstrates various tools and techniques available on this platform to troubleshoot CPU, memory, TCAM resources, packet forwarding, and QoS. Last, but not least, this session will show some of the next generation of troubleshooting methodologies enabled by Cisco IOS XE software and discuss how users can use these methods to troubleshoot their networks quickly and effectively. First-hand knowledge of the Cisco Catalyst 9000 product is expected. This session covers the Catalyst 9200, 9300, 9400, 9500 and 9600 switches, but it does not include Catalyst 9100 series access points or the Catalyst 9800 series wireless LAN controllers.

### Troubleshooting the Session Initiation Protocol (SIP) - BRKCOL-2143
Speakers: Paul Giralt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098282115001d5pA
The Session Initiation Protocol (SIP) is the de-facto standard for real-time collaboration session establishment. It is core to Cisco Webex Calling and the Cisco on-premises collaboration portfolio on products such as Unified Communications Manager (UCM) and the Cisco Unified Border Element (CUBE) as well as many 3rd party products. Having a solid understanding of the protocol is essential to understanding how to troubleshoot signaling flows across a variety of products and systems. This session will primarily focus on understanding of the protocol itself and will try to remain relatively product agnostic. The session will start with the basic format of SIP messages and how they are used to set up and tear down calls, then will dive deeper into more complex call flows. We will cover session establishment, requests and responses, media negotiation including SDP and ICE, session refresh, invoking supplementary services (hold, transfer, conference, etc...), and securing SIP with TLS and SRTP. We will also briefly cover tools that can be used to more easily parse through SIP logging information to make troubleshooting easier. After completing this session, you should have a firm understanding of how to troubleshoot a SIP call flow on any platform that supports SIP.

### TrustSec Refresh Reinforced with Common Policy Innovations - BRKENS-1852
Speakers: Jonothan Eaves (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098299671001dB0m
Segmentation is a top priority within any zero-trust journey. Participants will receive a refresher on TrustSec technology, how the Security Group Tag (SGT) is utilized, and how it simplifies segmentation operations and reduces risk. The session will continue by explaining and demonstrating new innovative capabilities which enhance interoperability and simplify deployments. Participants with little TrustSec knowledge are welcome, as an introduction will be provided. More advanced participants will also benefit from this session due to the presentation of new features and innovations. Significant time will be provided explaining and demonstrating a new Common Policy initiative for sharing policy context between ISE and ACI and classifying Cloud Workloads. This will show how to facilitate a consistent security policy across multiple domains. You will leave this session with a good understanding of TrustSec capabilities, how they help to simplify segmentation and deployment operations, and what new functions are available to enhance the deployment experience.

### Tune your Cisco Wireless networks for Roaming clients and demanding Real-Time applications...with some help from AI! - BRKEWN-2926
Speakers: Jerome Henry (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161405467001NAYY
Are you running a Cisco Wi-Fi network? Great news! Thanks to a unique partnership with Apple, Samsung, Intel, and other great names in the client device ecosystem, Cisco Wi-Fi has features that allow your clients to tell you how they are performing, and for your access points to optimize the experience of your Wi-Fi clients, including those in the hands of users who move and roam all day long between APs, and including those that run real-time and demanding applications and for which increased latency of jitter means disastrous experience. Join us in this session, where you will learn what these unique features are, and how to tune your Cisco Wi-Fi network to offer a seamless experience to all your clients, mobile phones, tablets, IoT and laptops.

### Turn AI to ROI with a Solid Data Foundation - PARAI-1141
Speakers: Sasan Moaveni (HITACHI VANTARA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161422463001Nhxo
Achieving AI success starts with a strong foundation. From identifying the best use cases to building a secure efficient, and reliable data platform ready to handle AI's demanding workloads. Cisco and Hitachi Vantara provide the critical building blocks for your AI data platform. With a proven track record in meeting the mission-critical needs of top organizations worldwide, the path from AI to ROI is clear and actionable. Join us and learn how to jumpstart AI success and unlock its full potential for your business.

### Turn Your Security Policy Into Code and Make Your Weekends More Enjoyable - DEVNET-2076
Speakers: Brennan Bouchard (Cisco), Ed McNicholas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098436709001d0QC
Deploying and updating security policy has always been risky business. This is typically why most policy changes are done during maintenance windows over the weekend. What if there was a better way to develop, test and deploy security policy in an environment before being pushed to production. Would that be of interest? In this session, we introduce Security as Code where you will learn how to dynamically update and deploy security policy into the application pipeline using Ansible and Terraform, giving you that warm and fuzzy feeling that your weekends won't be rudely interrupted.

### Turnkey Observability: Orchestrating ThousandEyes Deployment - DEVLIT-2976
Speakers: Cihan Yilmazer (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098427621001dVNo
Orchestration is getting a more important role everyday for organizations. Instead of spending on side-missions, businesses encourage engineers to focus on core tasks which bring the actual value. Observability is always important to ensure that we have enough data to fix issues or prevent them. Using the power of cloud, ThousandEyes has different implementation models. It can perfectly fit in any DevOps pipeline for a turnkey deployment. Join this session to learn how to deploy ThousandEyes Enterprise Agents(EA), configure tests and enable alerts just with a simple Git Push, using GitLab CI, Terraform, Ansible and AWS. The session will present a step by step approach to help you enable your first Turnkey ThousandEyes deployment.

### Under the hood of IOS-XE EVPN/VXLAN on Catalyst 9000 - BRKENS-3840
Speakers: Dmytro Vishchuk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098303666001dsfi
Ethernet VPN (EVPN) has become de-facto an industry standard for data center fabrics and L2/L3 VPN connectivity in service provider. EVPN functionality was also expanded into Campus networks, to address the drive of network operators toward simplicity and automation with a unified inter-domain connectivity technology. This session covers in detail packet path in the Fabric in case BUM, bridged and routed flows with verification of the Fabric states and deep explanation of the CLI outputs of the show commands for relevant components. Focus of the session is to build deep knowledge of EVPN "mechanics" on Catalyst 9000 and a clear understanding of the process of packet forwarding and related verification methods.

### Understanding Cisco Private Cloud Contact Center Enterprise offering: WCCE - BRKCCT-1001
Speakers: Zin Elabidine Karzazi (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098275048001dqXK
Webex Contact Center Enterprise (Webex CCE) provides a complete, customizable, and highly secure solution to meet the complex needs of the world's largest contact centers. Available only from a trusted brand like Cisco, Webex CCE opens the way to the cloud for even the most business-critical contact centers. In this session, we will explore aspects like architecture, security, connectivity options for voice and data, multi and omni channel based on Webex Connect, support model and responsibilities. We will also go through a comparison with Webex Contact Center (WCC) and Unified Contact Center Enterprise (UCCE) solution including migration path from prem to cloud. We will briefly analyse the competitive landscape as well as more operational aspects such as partner onboarding and the creation of new tenants.

### Understanding HyperFabric: a Groundbreaking Cloud-Controlled Data Center Network Solution - BRKDCN-2944
Speakers: Dan Backman (Cisco), Minako Higuchi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098294760001dBx2
What is an ideal cloud-controlled data center network solution? One that makes it easy for anyone to deploy reliable fabrics anywhere. In this lively session, you will get a first-hand view of an upcoming solution that re-imagines every phase of the process - design, order, deploy, validate, monitor, and upgrade. And we will reveal novel capabilities the solution embeds including an abstracted & managed underlay, plug & play deployment, built-in assertion-based health monitoring, and the elimination of on-box CLI. Join us to see this Cisco innovation in action.

### Understanding Voice Media and Real-time Media Handling for Webex Contact Center - BRKCCT-2723
Speakers: Bryan Morris (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098276350001d3ZH
Cisco is working to consolidate its access edge services for Webex Contact Center and Webex Calling. Common edge services deliver a simplified deployment model for accessing Webex. It allows customers to use the same gateways with a single SIP trunk for both Webex Calling and Contact Center. Webex Control Hub becomes the single management portal providing self-service provisioning and managing of all your gateways, call routing and contact center. Common edge services also gives contact center customers access to Webex's global network of cloud connected PSTN partners. In this session we will look at the various options to bring voice channels into Webex Contact Center using common edge services. We will discuss Webex Calling, SIP integrations to on premise environments like Cisco Communications Manager, integration with Microsoft Teams and finally WebRTC support. We will then go on to discover how Webex Contact center allows you select, blend and optimize different media connections for global contact center deployment. This session will be of interest to anyone engaged in contact center architecture, design and implementation but especially to those with an interest in voice services in a multi-location environment.

### Understanding Wireless Security and the Implications for Secure Wireless Network Design - BRKEWN-2104
Speakers: Mark Krischer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161403170001NMa0
This session will explore secure wireless network design with a key focus on the latest Wi-Fi and WPA standards. Mobility brings unique challenges to network security, such as the need for strong authentication and support for secure fast roaming. Participants will learn how 802.11 addresses these requirements and will explore the changes WPA3 brings and the implications for wireless deployments. This session will also explore how Cisco Catalyst Center and the Meraki Dashboard expand on wireless security standards with rogue access point detection and location, and advanced wireless intrusion detection and prevention. The intent is to provide a deeper understanding of wireless security capabilities from the perspective of the attacks they defend against.

### Understanding and Implementing GenAI Security - DEVNET-2718
Speakers: Erika Dietrick (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098448108001dBDl
As GenAI innovation evolves rapidly, so should our vigilance against cybersecurity threats. But what does GenAI security even entail? This is the ultimate session for understanding current problems (and best practices) in securing GenAI apps and tooling, emerging attack vectors, data privacy concerns, and both the positive and negative impacts of GenAI on secure coding practices. Attendees will walk away with a practical understanding of how to mitigate and protect against GenAI threats wherever possible and where Cisco security products can provide value.

### Understanding and Troubleshooting the Cisco Catalyst Center - BRKOPS-2464
Speakers: Abhay Kaviya (Cisco), Rahul Rammanohar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098352708001dzbR
Cisco Catalyst Center (formerly Cisco DNA Center) is the central management platform and the command center for the Enterprise Campus network. Troubleshooting the Catalyst Center has mainly been performed via the CLI (Command Line Interface) and has been perceived to be difficult. There have been many enhancements added to the GUI (Graphical User Interface) recently to simplify troubleshooting and provide an enhanced view of the connectivity and the internals. Please join this session as we cover the following major topics based on customer case studies: 'A review of the Catalyst Center System Architecture and Catalyst Center upgrade process and troubleshooting 'troubleshooting the Catalyst Center using the new tools available in the GUI and the typical scenarios when TAC would use these tools (Grafana dashboards, Diagnostic Center, 'system 360, System Analyzer, Enhancements in the Inventory dashboard) 'troubleshooting issues commonly seen in the field

### Unified Access and Aggregation with Cisco Routed PON - BRKSP-1169
Speakers: Tejas Lad (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161410337001NHmy
Service providers are heavily investing in broadband deployments using passive optical network (PON) technology to cater unprecedented demands of end users. Billions of dollars have been funded by government organizations to bring broadband to everyone. With 10 gigabit symmetrical PON (XGS-PON), service providers are looking to converge business, mobile backhaul, and residential services onto a common platform and architecture. Cisco's routed PON solution reduces the footprint and power of the optical line terminal (OLT) to a small form-factor pluggable (SFP) that can be hosting in Cisco's NCS-based platforms running IOS-XR. Cisco NCS platforms are widely deployed as access and aggregation, and integrating the XGS-PON pluggable brings tremendous operations and cost advantages. In this session, you will learn the different components of the XGS-PON system and its integration into Cisco's converged SDN transport using segment routing and EVPN. The session will cover the shift in PON technology and deep dive into Cisco routed PON with both residential and business use cases. We will keep the session interactive with live demos showcasing the deployment and benefits of the solution.

### Unified Observability: Maximizing Value with AppDynamics, Splunk, and ThousandEyes - BRKOBS-1110
Speakers: Lukasz Ciukaj (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098339778001dK0c
In today's complex IT environments, integrating multiple observability tools is essential for a unified view of operations. This session is designed for customers who have AppDynamics, Splunk, and ThousandEyes implemented across various departments. We will explore advanced integration techniques, best practices, and real-world use cases to help you maximize the value of your observability investments. Discover how to seamlessly integrate these tools to support all types of applications'traditional 3-tier, cloud-native, and SaaS. Learn to correlate data for enhanced root cause analysis, set up advanced monitoring and alerts, and leverage predictive analytics for proactive management. Hear success stories from enterprise customers and gain actionable insights to implement in your organization. Whether you're aiming to improve performance, reduce downtime, or gain deeper operational insights, this session will equip you with the knowledge and tools to achieve unified observability and drive excellence across your IT landscape.

### Unified Wireless for Industries - from WIFI to Private 5G and Beyond - BRKIOT-2365
Speakers: Matthias Falkner (Cisco), Gino Corleto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161408092001N1Fd
Have you ever wondered why there are so many wireless technologies available, and why some seem to overlap? Choosing the right wireless technology - or combination of technologies - can be challenging, especially as more business-critical processes rely on them. With digitization and wireless mobility closely linked, understanding our wireless toolbox is essential. In this session, we'll explore key wireless technologies like Wi-Fi 6/6E/7, CURWB and Private 5G. We'll dive into real-life use cases to determine when each technology is most appropriate. Additionally, we'll discuss the importance of security, highlighting a unified policy approach and the best practices for integrating these technologies into your existing OT/EN networks and policies.

### Unify Threat Detection, Investigation, and Response with Splunk Enterprise Security and SOAR - BRKSEC-2887
Speakers: Andreas Buis (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098379798001dTqv
Learn how to supercharge your security operations with Splunk Enterprise Security and Splunk SOAR. This session will show you how to streamline threat detection, investigation and response, empowering your team with automated workflows and real-time analytics. Discover how the integration of SIEM and SOAR enables faster, more efficient investigations and responses, giving your security operations the agility needed to stay ahead of evolving threats. If you're ready to enhance your security team's capabilities and elevate your organization's security posture, this session is for you.

### Unifying User Experiences with Generative AI: Security, Networking & Collaboration - AIHUB-2695
Speakers: Richard Jang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161398113001Ngde
AI is reshaping the world, from facial recognition and voice-enabled IoT devices, to the latest generative AI-powered chatbots. Its integration into our daily lives has unlocked unparalleled convenience and innovation. But how does AI actually work, and how is it transforming IT operations? Join this session to explore the technical fundamentals of how AI works, including machine learning, neural networks, and a focus on generative AI. Once we've covered the technical fundamentals, we'll dive into Cisco's cutting-edge generative AI technology across each domain, with a special focus on the Unified AI Assistant. This innovative solution integrates Cisco's platforms, delivering unified insights across networking, security, and collaboration - dramatically improving IT efficiency and creates a cohesive experience across all Cisco software platforms! Don't miss the opportunity to learn how generative AI works and see how Cisco is driving the future of IT through the Unified AI Assistant.

### Unlock Intersight Monitoring with OpenTelemetry - DEVNET-2118
Speakers: Chris Gascoigne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098437815001dpn2
OpenTelemetry is a free, open source and vendor neutral observability framework that is rapidly growing in popularity and gaining wide support from industry leaders. In this session, you will learn how OpenTelemetry metrics can be generated from the Intersight API. Once converted to OpenTelemetry metrics, the Intersight telemetry can be flexibly exported to a variety of monitoring backends. The session will demonstrate this use case in action, showing how to export Intersight metrics with OpenTelemetry to a Prometheus time-series database and Grafana dashboard. Programming knowledge is not required but an understanding of API basics and YAML will be beneficial.

### Unlock Value at the Edge: Unleash your networks hardware for AI/ML based analytics! - BRKIOT-2210
Speakers: Daniel Eckstein (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098329834001dnB5
From multivariate, time-based recurrent neural networks to geo-position aware alerting? What if you could add autonomous AI/ML based analytical capabilities to your connectivity solution and provide data-focused functionality at the edge, without being dependent on a remote service? In our session, we are going to increase the value of the hardware providing connectivity by leveraging it also as a platform for running analytics. We will deploy examples and see demos for geo-fencing and for automated and unsupervised multivariate IoT telemetry value forecasting to detect deviations of desired operational statuses.

### Unlock the Future: Leveraging Generative AIOPs for Enterprise Innovation and Performance - AIHUB-1006
Speakers: Sanjit Aiyappa (Cisco Systems, Inc.), Joel Jose (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161391259001NNA0
AIOps, empowered by Generative AI (GenAI), is revolutionizing IT operations by streamlining processes, reducing costs, and enhancing service quality. This synergy ensures significant cost savings through automation and efficient resource utilization, making high-quality IT services more affordable. With predictive performance, reduced MTTR, and capacity forecasting, AIOps guarantees reliable, scalable services aligned with customer needs and business goals. GenAI introduces a new level of automation, from incident handling to system optimization, ensuring dependable services. It personalizes user experiences and strengthens security measures, safeguarding customer data. Beyond traditional systems, GenAI's creativity and adaptability tackles complex challenges, leveraging data for insights and driving operational efficiencies and new innovations. This session will showcase a live Webex MSP bot demo powered by GPT-4, highlighting how Cisco partners use AIOps and GenAI for interactive customer engagement, service assurance and exceptional experiences.

### Unlocking Digital Resilience Through Unified Observability - KDDOBS-1000
Speakers: Richard Erda (Engel Austria GmbH), James Hodge (Cisco), Mike Cohen (Cisco), MANFRED RUEHRNESSEL (Engel Austria GmbH)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1739227082749001JCt8
Dive into the future of digital resilience with Splunk Observability, enhanced by AppDynamics. As downtime costs escalate and digital resilience becomes critical, we'll discuss how our unified approach empowers organizations to gain comprehensive visibility, detect issues faster, and manage costs effectively in complex environments. With recognition from top analysts and a compelling customer success story, this session is essential for anyone looking to elevate their observability strategy. Register now!

### Unlocking Human-Centered Leadership with AI - IF-1100
Speakers: Kelly Jones (Cisco), Jacqueline Carter (Potential Project)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161421292001N5rn
With the power, promise, and potential of AI, leaders have an extraordinary opportunity to leverage it to enhance the way they lead. In this session, we will explore "the AI-Enabled Leader" framework walking through several practical examples of how AI can help leaders to do hard things in a more human way, share practical tips and strategies to enhance leadership effectiveness through AI, and learn how to harness the power of AI ethically and responsibly.

### Unlocking Human-Centered Leadership with AI - ITLGEN-1516
Speakers: Scott Herpolsheimer (Cisco), Jacqueline Carter (Potential Project)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098460263001dyYO
With the power, promise, and potential of AI, leaders have an extraordinary opportunity to leverage it to enhance the way they lead. In this session, we will explore 'The AI-Enabled Leader" framework walking through several practical examples of how AI can help leaders to do hard things in a more human way, share practical tips and strategies to enhance leadership effectiveness through AI, and learn how to harness the power of AI ethically and responsibly.

### Unlocking the Power of Cisco Catalyst SD-WAN: Enhanced Network Operations - BRKENT-2195
Speakers: Mateusz Krupiński (Cisco), Filipe Moreira (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098307649001dM1n
In today's fast-paced world, operational agility is critical, but true business success hinges on application excellence. Imagine ACME Corporation responding to a natural disaster by rapidly deploying a branch either over satellite and/or LTE connections to maintain operations while ensuring top-tier application performance. This session highlights how Cisco Catalyst SD-WAN empowers rapid branch deployment, combining operational excellence with superior application optimization. Discover streamlined workflows for fast setup, proactive health monitoring for reliability, and actionable analytics for flawless application delivery even over high-latency networks. Join us for live demos and real-world scenarios showcasing the latest Cisco Catalyst SD-WAN innovations, designed to help you achieve both operational and application excellence. Prior knowledge of Cisco Catalyst SD-WAN is recommended.

### Untangling the Multi Cloud Maze: Simplify Hybrid Connectivity with Catalyst SD-WAN - BRKCLD-1512
Speakers: Saswat Praharaj (Cisco), Michalina Słomiańska (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098277087001dKkU
In this session, we'll dive into the complex world of hybrid connectivity and explore how Catalyst SD-WAN can streamline your multi-cloud strategy. We'll address the challenges of connecting on-premises infrastructure to cloud environments, navigating the differences between AWS, Azure, and GCP, and simplifying VPC-VRF-VPC connections. Discover how Catalyst SD-WAN Cloud OnRamp features can eliminate the need to master individual cloud provider networking intricacies, making your hybrid cloud journey smoother and more efficient.

### Use Observability to enable a quicker move to Multi-cloud - BRKCLD-2769
Speakers: Peter Charpentier (Cisco), Morten Skriver (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098279016001d0si
Transforming an IT landscape to multi-cloud can't be done overnight -- it's a journey. How your resources are used, on-premises and/or cloud, are important topics to consider to achieve a successful multi-cloud strategy. This session covers both the methodology and technical aspects of multi-cloud migration-based Cisco CX best practices and how Observability can support to ensure success. It will also explore how scale can be tracked using Observability and how it can ensure a good customer experience. The session will show how to securely connect on-premises to public cloud and how workloads can be migrated to cloud and back to on-premises, but also with an overview on how running as cloud-native services (containers) will help workload mobility. When migrating applications to cloud, user experience should remain the same. This can be achieved by using Splunk AppD and ThousandEyes, as it enables monitoring and analyses user experience, performance, and stability of applications regardless of the deployment model. These will also help to track system load, bottlenecks, user experience and impact, and how things can be addressed quickly.

### Ushering in a New Era of 5G Innovation with Cisco's Multi-Use Case Mobility Services Platform (MSP) - BRKSPM-2341
Speakers: David Perez Gil (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161419797001NWZf
Today there are hundreds of mobile core networks around the world that are individually deployed, configured, integrated and operated with almost the same functionality, in hundreds of permutations. A radical new approach is required to drive adoption and monetization of new technologies such as 5G stand-alone (SA) with the flexibility required by both Service Providers and Enterprises. Cisco's multi-tenant Mobility Services Platform (MSP) has been designed to address this challenge and allow Service Providers and Enterprises alike to benefit from state-of-the-art tech practices to deliver growth and develop new business models. In this session, you will learn about Cisco's Mobility Services Platform (MSP) and how its "as-a-Service" approach differs from traditional on-prem and managed services models. You will also discover key real-life Use Cases across multiple domains including private 5G, IoT, B2B, MVNE/O, FWA, etc and the way these Use Cases are enabled through modern API-driven programmability in line with TM Forum specifications, combined with an AnyG Converged Core and simplified operations. Understanding of Mobile Packet Core technologies is recommended.

### Using Agentic IaC for Managing Infrastructure: the Good, the Bad, and the Ugly - BRKETI-2286
Speakers: Peter Bosch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098315199001droG
IT, security and network teams spend up to 30% of their time on pull-request reviews. Why? Why, in this gen-AI age, are they spending so much time on reviewing these PRs in the first place? Gen-AI enables the creation and validation of infrastructure changes autonomously. Moreover, by learning on the job, agentic assistance can help IT teams to scale and sustain the growth of ever expanding organization and IT footprint, and mitigate cost and talent scarcity challenges while focusing existing talent on high value tasks. Agentic teams can replicate, augment, review and approve PRs. This talk presents the issues to rid many of these mundane, error-prone and complex infrastructure config jobs by agentic teams. With use cases and demos, this session presents what works and what not for cloud-native, security and network tasks. Specifically, we present mechanisms to: Capture cloud-native and network state in GitHub - a source of truth How to manage both cloud-native and network state through GitHub How to reduce Terraform/IaC, security and network state review overhead while maintaining governance Optimizing Terraform/IaC, security and network state against target objectives and best practices Automatically writing Terraform/IaC, security and network operations for complex updates using natural language The session demonstrates the approach, showcasing agentic IT/security/network teams that learn and optimize on the job. Moreover, we are asking for your help: can you help test, contribute and move forward this tech?

### Using Energy Management Dashboards to Accelerate your Net Zero Journey - BRKGRN-2398
Speakers: Tripta Gulati (Cisco Systems, Inc.), Jay Kothari (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098325894001dtIS
Achieving energy management requires IT and line of business leaders to collaborate closely, and work towards a common goal. Business leaders want visibility into operations, so they can make informed decisions about energy management and CO2 emissions. However, they depend on IT teams on the front lines to recommend the best technology to achieve it. Join us and hear about how Cisco is executing to enable customers to make data driven decisions for Energy Management in Campus and Data Center environments.

### Using Ethernet for AI Networking - CISCOU-2038
Speakers: Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098408268001dmuN
The emergence of GenAI is driving an un-precedented investment in AI focused data centers. InfiniBand is the incumbent networking technology, but the industry wants standards based technologies to drive efficiencies. What will it take for Ethernet to succeed in this emerging enormous market?

### Using ThousandEyes to CYB - DEVLIT-2048
Speakers: Marc Nufrio (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098425871001dZFp
Making changes to a production network can be the most intimidating and nerve-racking task an operator can do. Ensuring that the network is healthy before and after the change can be a challenging task, especially when speed and efficiency are critical. This session will explore several automated approaches with the ThousandEyes API's to cover your butt(CYB) and help detect operational mishaps, fast!

### VXLAN BGP EVPN Multi-Site - BRKDCN-2913
Speakers: Lukas Krattiger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292962001dLLT
This session will cover the evolution of Cisco's approaches for efficiently connecting separate VXLAN BGP EVPN fabrics. We'll start by introducing the difference to multi-pod and multi-fabric, with the goal of understanding the evolution to the VXLAN multi-site approach that represents the optimal and recommended way to interconnect separate VXLAN EVPN islands. VXLAN provides an excellent encapsulation and EVPN provides extensive capabilities as a control plane. With VXLAN and EVPN, we have excellent capabilities for data center fabric deployments with an integrated layer-2 and layer-3 approach. With the maturity of the control and data plane, new capabilities for interconnecting multiple fabrics is experiencing growing interest with VXLAN BGP EVPN. Note: This session is exclusively focused on NX-OS stand-alone VXLAN EVPN and does not discuss the multi-pod and multi-site solutions offered with Cisco ACI.

### VXLAN EVPN: A Deep Dive into Packet Forwarding - BRKDCN-3966
Speakers: Lukas Krattiger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098298175001dD9t
This session focuses on a day in the life of a VXLAN EVPN packet. How we route and bridge and how multi-destination traffic is handled. This session will help you to understand what happens on the ingress VTEP all the way to the egress VTEP and beyond.

### Vim: Its Easier to Use than You Think! - CISCOU-2044
Speakers: Quinn Snyder (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098410385001djdy
You never need to use Vim ... until you need to use it. While there are other text editors, Vim (or at least Vi) is installed on every Linux machine by default, making it an editor of last resort if you need to edit a text file on a jump host or a system to which you only have SSH access. This session will walk you through basic and intermediate tips and tricks to make your Vim experience a bit less painful when you need to use it. Who knows, you may start using it all the time!

### Webex Calling - How Do I Begin? - BRKCOL-2065
Speakers: Justin Jordan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098280833001dY9g
Well you have decided on Webex Calling, that's great! Let's take at look at the technical requirements, steps to success, and the process needed to get you up and running. We will cover topics from Identity to authentication, migration to devices and all things in between. When you leave, you will feel confident in the steps needed to successfully get your Webex Calling organization setup and making calls. We will discuss some best practices and scenarios around different approaches to implementation and migration of your current system to the cloud.

### Webex Calling Multi-Tenant Architecture - BRKCOL-2698
Speakers: Owen Friel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098284654001dnzX
This session pulls back the covers on the Webex Calling Multi-Tenant Architecture and will provide in-depth information on the technical details of key Webex Calling capabilities. This session will give customers and partners insights into how Webex Calling operates, and give them the information they need to understand how Webex Calling provides secure and reliable services. Topics will include: Global topology: what services run in what geographic regions? Data residency: where is my data stored? Media: how is media routed and processed for my globally distributed users? AI: how do Webex Calling AI features work? Where is my data processed? High availability: how does HA work? What happens on failures? Security: how is my media and data at rest and in transit secured?

### Webex Calling: Elevate Mission-Critical Communication to the Cloud with our AI-Powered Platform - PSOCOL-1790
Speakers: Manu Parhar (Cisco Systems, Inc.), Amey Parandekar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098466155001dz5C
Unlock the future of communication with Webex Calling. Cisco premises customers can now enjoy a seamless, flexible migration path to the cloud that enhances efficiency across your business. Join this session to explore: AI-powered Webex Calling user experience: Boost productivity and efficiency, anywhere, on any device Customer experience tools: Integrated directly into Webex Calling to replace premises solutions like UCCX Simple, yet powerful IT experience: Flexible migration options, centralized administration, and unmatched global availability Don't miss this chance to transform your calling experience!

### Webex Contact Center - AI Powered Routing to Enhance Customer Experience - BRKCCT-2009
Speakers: Vikram Gururaj (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098275609001ddd1
As more and more customers want to enhance Customer eXperience (CX) in Contact Centers, they are seeking ways to see how AI plays a role. Join us in this technical breakout to discover how you can unlock the potential of Webex Contact Centers using AI. We'll delve deep into the platform's CORE routing and orchestration capabilities, recent feature improvements for self-service including IVR, inbound & outbound campaign management and demonstrate some of the key customer use cases. We will show you both inbound features & outbound campaign management capabilities and flow capabilities. You'll learn how AI plays a role in potential use cases across contact center in IVR & Self-Service, Routing contacts. This session also teaches you how Webex Contact Center AI capabilities can be used to select the best agent to Maximize CSAT, Minimize Wait & Handle times. The most important highlight of this session shows you how to orchestrate your work flows to achieve AI based routing.

### Webex Contact Center: How AI will Revolutionize Contact Center Experiences - BRKCCT-1710
Speakers: Mags Moran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098275425001dL1J
As we experience this tectonic shift in the domain of AI, few domains are as well-positioned to embrace AI as Customer Experience and the traditional Contact Center, which handles inbound, outbound, or proactive workloads to support and sustainably grow businesses. During this session, attendees will be introduced to the true potential of AI in the Contact Center by using the Webex Contact Center platform, with a focus on practical use cases with Webex Contact Center. This will include incorporating AI across the customer journey, augmenting agent and supervisor workflows with AI, and extracting business intelligence from the Contact Center data platform supplemented with customer journey data. The session will showcase technologies like virtual agents, sentiment analysis, call summaries, topic analysis, agent assistance technologies, automated surveys on Webex Contact Center, now augmented by the latest trends in AI including generative AI technologies. Attendees will discover how the Webex Contact Center platform effectively enables AI solutions to boost efficiency, productivity and customer satisfaction.

### Webex Data Management, Control, and Loss Prevention - BRKCOL-2126
Speakers: Matthew Jordy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098281931001dCVd
Webex provides organizations with a full suite of cloud collaboration services enabling users to communicate and share content with other users both inside and outside the organization. With this collaboration comes risk and Webex customers must ensure that their organization's sensitive data is secured and protected from unauthorized access and loss. This session examines organization data management and control topics for Webex deployments including: Built-in data control and data retention capabilities of Webex Webex APIs for monitoring and controlling organization data External compliance platform integrations for data loss prevention (DLP), eDiscovery, legal hold, and archiving To illustrate key concepts and operations, these topics will be demonstrated using Webex organizations and integrations to three external compliance platforms: Cisco Cloudlock, Theta Lake, and AGAT SphereShield. Attendees should have some familiarity with Webex collaboration services and the Webex Control Hub management and administration portal.

### Webex Edge Connect Design and Deployment for Webex Meetings, Calling and Dedicated Instance - BRKCOL-2094
Speakers: Richard Murphy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098281564001dSyA
Webex is a highly advanced cloud platform that is constantly evolving and improving. With Webex Edge Connect, you can access the Webex backbone for Meetings and Calling services. In this session, we'll go over the Edge Connect solution, talk about important design considerations for each architecture type, share deployment best practices, and discuss the latest updates to the offering. You should have a basic understanding of the Webex Meetings and Calling products to get the most out of this session.

### Webex Meetings Master Class - BRKCOL-2700
Speakers: Clemens Geyer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098285033001dfdX
Online meetings have become a standard tool of our daily business lives. However, many participants are confronted with "meeting fatigue" and consider them as a necessary evil. Effective and engaging online meetings already start with proper planning and setting up the right environment for every use case - one type doesn't fit all. This session is targeting hosts and end users of Webex Meetings and will explain how you can successfully schedule, plan and conduct a meeting. You will learn how to use the advanced scheduling options of Webex Meetings and how Artificial Intelligence features can support you during and after the meeting. You should be familiar with the basic concepts of Webex Meetings when attending the session.

### Webex Video Interoperability with Microsoft Teams - UPDATES and ROADMAP session! - BRKCOL-2184
Speakers: Davide Preti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098282482001dVC7
This intermediate-level session provides attendees with the latest information about how the Cisco Collaboration solution can interoperate with Microsoft Teams, specifically for devices and meetings. We will have a special focus on the latest updates and an overview of our short-term roadmap for: Cisco video devices and Cisco RoomOS experience: Interoperability using VIMT (CVI) Gateway Interoperability using WebRTC (Direct Guest Join) Cisco video devices and the Microsoft Teams experience: Microsoft Teams Rooms and Panels For those interested in deploying Cisco Video Devices for Microsoft Teams, with a Live demo, check out BRKCOL-2185 For those interested in Calling interop with Microsoft Teams, check out BRKCOL-2067

### Webex on the Go - How Webex Integrates with Mobile Networks & Phones - BRKCOL-2699
Speakers: Mark Rankin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098284842001drNe
Europe has always been at the forefront of mobile communications and, as many industries and users move toward new ways of working, both laptops and smartphones are our tools of choice. This session focusses on the latter, an increasingly powerful internet connected computer with very specific network attributes, defined by 3GPP, that can be leveraged to deliver enhanced and improved user experiences when it comes to collaboration. This session will cover the various ways the Webex Service and App works on mobile phones, focusing on some of the recent offers and architectural changes behind the WebexGo Service and how it integrates with mobile platforms. We will cover: Basic Mobile Network Primer (APNs/DNNs, IMS, SMS/RCS etc) Different integration models eSIM, IMS Native and OTT with pros and cons of each WebexGo Models and Architecture a peak under the hood including how signalling and media are handled Webex App companion mode features and capabilities SMS in Webe how this is handled and what are the possibilities? Short Demo of some of the above capabilities The goal of the session is to show you why mobile integration is important, how we do it at Cisco Webex, and that not all collaboration services are equal.

### Webhooks in Cisco XDR Automation - DEVLIT-2553
Speakers: Matt Vander Horst (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098427268001dQH1
Ever wanted to trigger an XDR automation workflow from an external system? Webhooks can do just that. In this lightning talk, we'll demo how to create a webhook, add it to a workflow, and trigger it. You can then use this knowledge in your own environment to trigger workflows from other systems. Examples of use cases include triggering a workflow when a ticket is approved in your ITSM platform or when a message is received in a Webex room.

### Websockets and Webhooks: Embed Network Intelligence into your Applications - DEVNET-1841
Speakers: Adrian Iliesiu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098435983001dRgl
In this session, I will introduce the audience to websockets and webhooks and Cisco products that expose these two interfaces. From what are websockets and webhooks, to how to use them in the best way, to Python sample code, this session will showcase the power of these two interfaces and how to integrate the network intelligence that they expose into software applications in order to make them more resilient and fail-proof.

### Wellbeing Doesn't Work - IF-1155
Speakers: James Blair (Pavelka)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098453947001d30q
we've all tried changing our lives and started diet and exercise plans. Likewise, many organizations have tried to improve wellbeing and productivity. Why do so many initiatives fail to return results? This immersive, entertaining session delves into the science of motivation and hard research via trialling fun, experiential activities your people can replicate to improve their health, focus and productivity in and out of the office.

### What's New in Webex Platform APIs: Messaging, Meetings, Calling, SDKs, and Embedded Apps - BRKCOL-2907
Speakers: Phil Bellanti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098285580001dQEh
Stay up-to-date with the latest innovations in Webex Platform APIs in this dynamic classroom session. Tailored for developers and IT professionals, this session highlights the newest updates and announcements across Webex messaging, meetings, and calling APIs, as well as SDKs and embedded apps. Participants will gain insights into the latest features and enhancements designed to create more integrated and efficient communication solutions. You'll leave this session with ideas to help you understand the most recent updates to Webex Platform APIs and SDKs, explore new capabilities for enhancing messaging, meetings, and calling experiences, and learn about the latest tools for developing and deploying embedded apps within the Webex ecosystem. This session is ideal for developers and IT professionals who are already familiar with the Webex Platform and want to stay current with its latest advancements. Join us to discover the cutting-edge developments that will drive the future of communication and collaboration.

### What's in a Platform? A Guided Tour of the Webex Cloud Infrastructure - BRKCOL-2990
Speakers: Stefano Giorcelli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098286115001dNYa
Have you ever wondered what's really inside the Webex cloud-shaped icon you often see in network diagrams? Do you want to understand how Webex reliably delivers cloud Collaboration services to customers around the world? Come and join us for a guided tour of the Webex cloud infrastructure and learn about the following topics: the geographic distribution of Cisco Webex data centers and Webex services how each Cisco Webex data center (and IaaS providers used by Cisco) delivers specific services the types of availability modelsfor Cisco Webex workloads the cloud-native platform layer and shared Webex services how your provisioning choices determine data residency for different types of personal data where and how the Cisco Webex backbone interfaces with the public Internet (including some information on IPv6 support) how the Webex edge is structured and what connectivity options are available to customers and partners

### Why You Shouldn't Fear Upgrading Your ACI Fabric: The Handbook! - BRKDCN-2910
Speakers: Joey Ristaino (Cisco), Takuya Kishida (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098292607001dPgz
The Cisco Application Centric Infrastructure (ACI) architecture provides a single dashboard to manage hundreds of switches within your data center. This allows for a simple and seamless upgrade workflow, since everything can be automated or initiated from one place: the APIC controller. However, without knowing what happens "under the hood" when an upgrade is started, planning and executing a successful ACI upgrade may feel more like "shooting from the hip." This session aims at removing that doubt by providing a concise overview of what is happening to the APICs and switches as they undergo a software upgrade. Furthermore, this session will cover best practices and provide tools you can leverage to do "health checks" and audits of the pre-upgrade environment. This ensures that known issues are caught beforehand rather than during the upgrade, thus mitigating failure and enabling success. With this knowledge, you will have the utmost confidence in how to perform your ACI upgrade successfully, on time, and without heartburn.

### Why a Lifecycle Strategy Should Be at the Heart of Network Transformation - PARENT-1383
Speakers: Torsten Lange (COMPUTACENTER), Chris Flynn (COMPUTACENTER)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098462811001d039
By leveraging a systematic lifecycle strategy our customers are gaining maximum value from their Cisco networking investments. From strategic advisory through informed technology sourcing to service deployment we will discuss how time to value can be accelerated while delivering improved performance, security and resilience. With a unique modular approach to managed service delivery, we enable the seamless integration of supported legacy assets with the operational management of software driven technologies. Custom designed service accelerators streamline service deployment leveraging deep professional services expertise to mitigate risk and reduce complexity. A commitment to Cisco powered architectures is the foundation of our managed services strategy, augmented by investment in AI and automation to enhance experience and proactivity. No lifecycle strategy is complete without a focus on sustainability, we will share how our investment in circular services allows organisations to recover capital from their technology purchases whilst reducing the rate of equipment turnover and subsequent environmental impact. It's time to take a new look at Computacenter, we look forward to meeting you at Cisco Live

### Wi-Fi 7 is Here - Are you Ready? - BRKEWN-2025
Speakers: Anand Gurumurthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161402025001NXnb
Wi-Fi standards continuously evolve to cater to the needs of the latest applications and use cases. The next generation of Wi-Fi, i.e Wi-Fi 7, has created a lot of buzz, and is set to enhance wireless connectivity with unprecedented speeds, ultra-low latency and very high efficiency. As this next-generation standard emerges, organizations must be prepared to leverage its full potential. This session will explore the key advancements of Wi-Fi 7, that includes 4K QAM, 320 MHz channel width, Multi-Link Operation, Preamble Puncturing, Multi Resource Units, and how these features will impact network performance, scalability and security. We'll also discuss the necessary infrastructure updates, security updates and strategies to ensure a smooth transition. Join us to discover how Wi-Fi 7 can elevate your network capabilities and learn about the steps you need to take to stay ahead.

### Wireless Wonders: How To Build Your Wi-Fi 7 Network with the Cisco Portfolio - BRKEWN-1722
Speakers: Maren Kostede (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161401235001NnTu
Join this session to see how Cisco is setting the pace in wireless innovations, including Wi-Fi 7. You will receive an overview and guidance on Cisco's comprehensive product suite to start a high-level design for on-premises, cloud operations, or a mix of both. Over the past year, the range of design and solution options has significantly expanded, and all options will be explained. Key differentiators such as AI-RRM, CleanAir Pro, CURWB, and UWB will be highlighted.The session will cover the current Access Point portfolio and integration aspects with platforms like ISE, Meraki Dashboard, Catalyst Center, and Cisco Spaces. By the end of the session, participants will have a solid understanding of the Cisco Wireless portfolio and its various design options. The target audience includes IT decision-makers, newcomers, and everyone who needs a refresher on the Cisco Wireless Solution.

### Workplace Zero Trust Security: You Know of Segmentation, but What About Endpoint Visibility and Trust? - BRKOPS-1263
Speakers: Srilatha Vemula (Cisco Systems, Inc.), Orestes Matos (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098345491001dzp3
If you are like most customers who are dealing with the proliferation of IoT endpoints, sharing the IT network with IoT endpoints, and are worried that this may lead to a compromised environment, then this session is for you. Participants will learn how to easily maximize endpoint visibility and apply security policies using Cisco Catalyst Center and ISE. You will learn how to extract data through network probes, deep packet inspection, and NetFlow to help keep tabs on all discovered endpoints. This session will also show you how to monitor the trustworthiness of these endpoints and automate a restrictive policy in the event of anomalies such as MAC spoofing.

### XDR as easy as 1, 2, 3 : Simplifying Security Operations on the Meraki Dashboard - BRKMER-2527
Speakers: Chris Pacheco (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098337290001dt4q
Using the simplicity of the Meraki dashboard, the power of the MX Firewall and the intelligence of Cisco XDR, in this session you will learn: The technical details behind the integration between the MX firewall & Cisco XDR To easily onboard Cisco XDR on the Meraki dashboard To monitor & troubleshoot security incidents on the Meraki Security Center To provide more access on the Meraki dashboard to the SOC for security visibility

### Years of Experience on a Micro Segmentation Journey in Public Sector - CSSSEC-1810
Speakers: Dirk Stoeckmann (Cisco), Nico Oppelt (CITY OF MUNICH), MICHAEL STARNBERGER (MUNICIPALITY OF VIENNA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098420443001dJx6
In this session, two of the largest communities in Europe, city of Vienna and city of Munich, will talk about their experience building a segmentation journey for their IT processes, and how to align them to international regulations. One of them will talk about their way following an architectural approach, while the other one will talk about the people and political movements to be fixed on their way. Finally, they will show how they met at the technology level coming from the opposite side of people or processes. This session is valuable for understanding the multifaceted approaches to IT process management, and can provide insights into best practices for other cities or organisations facing similar challenges.

### Your Kick-Start for the Sustainability Journey - BRKGRN-2201
Speakers: Marisol Palmero Amador (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098325531001dbPM
Today we are dealing with a complex and unprecedented brew of social, environmental, market, and technological trends. Join us to learn how you can start and elevate your sustainability journey, based on: Environmental impact when a product is used, that includes power consumed, thermal cooling, and interconnect speed efficiency. Solution Impact as the offset that the solution provides and it can be translated to "CO2e emissions" saved, or eco-efficiency optimization; i.e., travel saved, power consumption reduction. Product Lifecycle provides information on manufacturing process efficiency, carbon impact, transport, waste management, and Circularity. This session will benefit Service Provider and Enterprise customers.

### Zero Touch Provisioning & Config Management of Cisco FTD in Azure using Terraform & Ansible - DEVNET-2150
Speakers: Ed McNicholas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098439278001dwzM
This session will leverage the Infrastructure as Code (Terraform Template) capability to build Cloud Infrastructure with Cisco Security Product. During a demonstration, Cisco NGFW deployment with the help of terraform Template will be shown to address following use cases: Deploy Cisco NGFW instance using Terraform Day 0 Configuration Manage Cisco NGFWv Day-1 and Day-2 configuration using Ansible

### Zero Trust: Secure the Workplace with Cisco Software-Defined Access - BRKENS-1851
Speakers: Keith Baldwin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740098299487001dLoa
Attackers use a variety of methods to compromise targets, often causing significant business disruption. To combat this issue, Cisco has developed a comprehensive solution: Software-Defined Access (SD-Access). This platform provides a foundational pillar for automating network-segmentation capabilities and allowing users to establish micro-perimeters for users, devices, and IoT networks. SD-Access meets the strict zero-trust requirements by establishing trust, enforcing trust-based access, continuously verifying trust, and responding to changes in trust. In this session, attendees will gain an understanding of the challenges posed by traditional networks and how SD-Access fabric architecture overcomes these issues with a policy-driven approach. Additionally, attendees will have the opportunity to hear from a peer who will share their experience on how this solution solved their zero-trust needs.

### Zero to RAG in 60 Minutes! How to Get Started with LLM Retrieval Augmented Generation - BRKAI-2920
Speakers: Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1740161400058001NBIS
We all know that LLMs can do some amazing things. But as capable as they are, they often lack domain-specific knowledge to address customized or domain-specific use cases. Enter RAG Retrieval Augmented Generation to address this gap! Come to this session to learn how RAG can be used to make LLMs truly useful for a variety of critical use cases, and most importantly, how you can implement RAG in your own LLM deployments even on-premises with private, local data sets! This session is delivered by the dynamic duo of Prapanch Ramamoorthy and Dave Zacks, both distinguished Cisco Live speakers. Come to this session for a fun, engaging deep dive on how and when to deploy RAG all within 60 minutes from start to finish!

